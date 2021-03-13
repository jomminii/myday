import pymysql

from config import DATABASES


def get_db_connection():
    """ 데이터베이스 커넥션을 만들어주는 클래스

    Returns:
        database connection 객체

    History:
        2021-03-13 (leejm): 초기 생성
    """
    print('$'*100, DATABASES)
    _db_config = {
        'host': DATABASES['database'],
        'port': DATABASES['port'],
        'user': DATABASES['user'],
        'password': DATABASES['password'],
        'database': DATABASES['database'],
        'charset': DATABASES['charset'],
        'cursorclass': pymysql.cursors.DictCursor,
    }
    print('config', _db_config)
    # try:
    db = pymysql.connect(**_db_config)
    print('aaaaa' , db)
    return db

    # except Exception as e:
    #     print(e)
