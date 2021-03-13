import datetime
import constants

from flask import jsonify, g
from schedule.schedule_dao import ScheduleDao

class ScheduleService:
    """ 스케줄 서비스
    """
    def get_today_schedule_data_list(self, user_id, db_connection):
        """ 일일 스케줄 리스트 조회
        """
        result = {
            'night': [],
            'morning': [],
            'dayTime': [],
            'evening': [],
        }
        schedule_dao = ScheduleDao()
        data_list = schedule_dao.get_today_schedule_data_list(user_id, db_connection)
        
        converted_data_list = []
        for data in data_list:
            converted_start_hour = int(data['start_time'].strftime('%H'))

            converted_start_time = data['start_time'].strftime('%Y-%m-%d %H:%M:%S')
            converted_end_time = data['end_time'].strftime('%Y-%m-%d %H:%M:%S')

            data['start_time'] = converted_start_time
            data['end_time'] = converted_end_time
            
            # NIGHT
            if converted_start_hour < constants.NIGHT_END_HOUR:
                result['night'].append(data)
            elif converted_start_hour < constants.MORNING_END_HOUR:
                result['morning'].append(data)
            elif converted_start_hour < constants.DAY_TIME_END_HOUR:
                result['dayTime'].append(data)
            else:
                result['evening'].append(data)
        return jsonify(result), 200
