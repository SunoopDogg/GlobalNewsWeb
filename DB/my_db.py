import pymysql


def getLocalDB():
    DATABASE_HOST = "localhost"
    DATABASE_PORT = 3306
    DATABASE_USERNAME = "SunoopDogg"
    DATABASE_PASSWORD = "0210"
    DATABASE_NAME = "test"

    db = pymysql.connect(host=DATABASE_HOST, user=DATABASE_USERNAME,
                         passwd=DATABASE_PASSWORD, db=DATABASE_NAME)
    return db
