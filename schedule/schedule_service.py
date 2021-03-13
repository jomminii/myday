from flask import jsonify, g
from schedule.schedule_dao import ScheduleDao

class ScheduleService:
    """ 스케줄 서비스
    """
    def get_today_schedule_data_list(self, user_id, db_connection):
        """ 일일 스케줄 리스트 조회
        """
        schedule_dao = ScheduleDao()
        data_list = schedule_dao.get_today_schedule_data_list(user_id, db_connection)
        return data_list
