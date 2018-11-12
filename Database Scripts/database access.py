
import pymysql

db = pymysql.connect("localhost", "kavi", "kavi", "TestDB")

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data =  cursor.fetchone()
print('Database ver: %s' % data)

sqlp = """CREATE TABLE product (
  prodID varchar(20) NOT NULL,
  category varchar(15) DEFAULT NULL,
  brand varchar(20) DEFAULT NULL,
  name varchar(50) DEFAULT NULL,
  instockNo varchar(10) DEFAULT NULL,
  Price double NOT NULL
)"""

sqlr = """CREATE TABLE recorddescri (
  recordID varchar(20) NOT NULL,
  prodID varchar(20) NOT NULL,
  quantity int(11) DEFAULT NULL,
  userID varchar(15) DEFAULT NULL
)"""


sqlinsertr = """INSERT INTO recorddescri (recordID, prodID, quantity, userID) VALUES
('301', '100', 1, '201'),
('301', '102', 6, '201'),
('301', '119', 1, '201'),
('302', '103', 1, '202'),
('303', '110', 2, '203'),
('304', '115', 1, '201'),
('305', '115', 4, '204'),
('306', '113', 1, '204'),
('307', '107', 3, '203'),
('308', '108', 1, '202'),
('309', '105', 2, '205'),
('309', '115', 1, '205'),
('310', '115', 4, '203'),
('311', '116', 1, '204'),
('311', '117', 5, '204'),
('312', '118', 2, '201'),
('312', '119', 1, '201'),
('313', '106', 3, '203'),
('314', '107', 1, '204'),
('314', '108', 1, '204');"""

# sqlinsert = """INSERT INTO user (userID, username, password, name, email) VALUES
# ('%d', '%s', '%s', '%s', '%s')""" % (788, 'drdh', 'sunni', 'Oshane', 'kinji@kunji.com')

sql = """CREATE TABLE salesrecord (
  recordID varchar(20) NOT NULL,
  Date date DEFAULT NULL
)"""

sqlinsert = """INSERT INTO salesrecord (recordID, Date) VALUES
('301', '28/02/18'),
('302', '20/03/18'),
('303', '12/05/18'),
('304', '28/08/18'),
('305', '02/06/18'),
('306', '16/10/18'),
('307', '17/10/18')
('308', '12/10/18'),
('309', '12/10/18'),
('310', '19/10/18'),
('311', '19/10/18'),
('312', '08/10/18'),
('313', '18/10/18'),
('314', '04/10/18'),
('315', '02/10/18'),
('316', '03/10/18'),
('317', '02/10/18'),
('318', '01/10/18'),
('319', '01/10/18'),
('320', '12/10/18');"""

try:
    cursor.execute(sqlinsert)
    db.commit()
except:
    db.rollback()

db.close()











