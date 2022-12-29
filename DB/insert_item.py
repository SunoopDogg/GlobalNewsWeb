def insertItem(DB, item):  # {
    TABLE_NAME = "globalNewsWeb"

    sqlInsert = f"INSERT INTO {TABLE_NAME} (country, category, url, title) VALUES ('%s', '%s', '%s', '%s')"

    db = DB
    cursor = db.cursor()

    for i in range(len(item)):  # {
        cursor.execute(sqlInsert % (
            item[i]['country'], item[i]['category'], item[i]['url'], item[i]['title']))
    # }

    db.commit()
# }
