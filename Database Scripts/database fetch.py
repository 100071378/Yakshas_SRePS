
import pymysql

def StoreData(datas):
    x = datas
    print('This is the stored data: %s'%(x))

db = pymysql.connect("localhost", "kavi", "kavi", "TestDB")

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

sql = """SELECT * FROM product WHERE category = '%s'""" % ('Skin care')

sqlinsert = """INSERT INTO product (prodID, category, brand, name, instockNo, Price) VALUES 
('%d', '%s', '%s', '%s', '%d', '%.2f')""" % (222, 'Skin care', 'Trojan', 'XXL Condom', 629, 125.2)

sqlupdate = """UPDATE product SET Price = '%f' WHERE prodID = '%d'""" % (22.2, 110)

sqldelete = """DELETE FROM product WHERE prodID = '%d'"""%(100)

sqldrop = """DROP TABLE product"""


try:
    cursor.execute(sqldrop)
    cursor.execute(sql)
    results = cursor.fetchall()

    for row in results:
        name = row[3]
        StoreData(name)

        #print('Name: %s'% (x))

    db.commit()

except:
    print('Error! unable to fetch data')
    db.rollback()



db.close()
