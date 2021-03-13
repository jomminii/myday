from flask import jsonify

class ScheduleDao:
    """ 스케줄 모델

    """
    def get_today_schedule_data_list(self, user_id, db_connection):
        """ 일일 스케줄 리스트 조회

        :param user_id:
        :param db_connection:
        :return:
        """

        # try:
        print(5)
        with db_connection.cursor() as db_cursor:
            get_stmt = """
            SELECT
                *
            FROM
                mydayDB.schedules
            WHERE
                user_id = %(user_id)s
            """

            db_cursor.execute(get_stmt, {'user_id': user_id})
            print(6)
            data_list = db_cursor.fetchall()
            if data_list:
                return jsonify(data_list), 200
            return jsonify({'message': 'SCHEDULE_DOES_NOT_EXIST'}), 404

        # except Exception as e:
        #     print(f'DATABASE_CURSOR_ERROR_WITH {e}')
        #     db_connection.rollback()
        #     return jsonify({'message': 'DB_CURSOR_ERROR'}), 500