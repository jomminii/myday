import pymysql

from config import DATABASES


def get_db_connection():
    """ 데이터베이스 커넥션을 만들어주는 클래스

    Returns:
        database connection 객체

    History:
        2021-03-13 (leejm): 초기 생성
    """
    _db_config = {
        'host': DATABASES['host'],
        'port': DATABASES['port'],
        'user': DATABASES['user'],
        'password': DATABASES['password'],
        'database': 'MYDAY_DB',
        'charset': DATABASES['charset'],
        'cursorclass': pymysql.cursors.DictCursor,
    }

    # try:
    db = pymysql.connect(**_db_config)
#    db = pymysql.connect( host='myday-database.cp4cgr7ypiij.ap-northeast-2.rds.amazonaws.com', port=3306, user='admin', password='akdlepdl13!#', database='MYDAY_DB')
    return db

    # except Exception as e:
    #     print(e)
