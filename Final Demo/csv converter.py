import pymysql

class CSV():

    db = pymysql.connect("localhost", "kavi", "kavi", "TestDB")
    cursor = db.cursor()

    sql = "SELECT * FROM recorddescri"
    cursor.execute(sql)

    file = open("sales.csv", "w")

    for row in cursor:
        file.write(str(row[0]) + ',' + str(row[1]) + ',' + str(row[2]) + ',' + str(row[3]) + '\n')
    file.close()
    cursor.close()
    db.close()

