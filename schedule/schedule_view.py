
from flask import request, Blueprint, jsonify, g
from schedule.schedule_service import ScheduleService
from connection import get_db_connection

class ScheduleView:
    """ 스케쥴 뷰

    """
    schedule_app = Blueprint('schedule_app', __name__, url_prefix='/schedule')
    @staticmethod
    @schedule_app.route('/<int:user_id>', methods=['GET'])
    def get_today_schedule_data_list(user_id):
        """ 일일 스케줄 리스트 조회
        """

        try:
            print(0)
            db_connection = get_db_connection()
            print(db_connection)
            print(11)
            if db_connection:
                schedule_service = ScheduleService()
                print(1)
                data_list = schedule_service.get_today_schedule_data_list(user_id, db_connection)
                return data_list

        except Exception as e:
            print(e)
            return jsonify({'message': f'{e}'}), 500

        finally:
            try:
                db_connection.close()

            except Exception as e:
                return jsonify({'message': f'{e}'}), 500