import pymysql

db = pymysql.connect("localhost", "root", "", "pharmacy")

cursor = db.cursor()

sql = "SELECT * FROM user"
cursor.execute(sql)

file = open ("users.csv", "w")

for row in cursor:
    file.write(row[0] + ',' + row[1]+ ',' + row[2] + ',' + row [3] + '\n')
file.close()
cursor.close()
db.close()