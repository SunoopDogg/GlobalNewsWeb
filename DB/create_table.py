from my_db import getLocalDB


TABLE_NAME = "globalNewsWeb"

sqlDropTable = "DROP TABLE IF EXISTS %s"
sqlCreateTable = "CREATE TABLE %s (id INT NOT NULL AUTO_INCREMENT, \
                                   country VARCHAR(50) NOT NULL, \
                                   category VARCHAR(50) NOT NULL, \
                                   url VARCHAR(255) NOT NULL, \
                                   title VARCHAR(255) NOT NULL, \
                                   PRIMARY KEY (id))"

db = getLocalDB()
cursor = db.cursor()

cursor.execute(sqlDropTable % TABLE_NAME)
cursor.execute(sqlCreateTable % TABLE_NAME)

db.commit()

db.close()
