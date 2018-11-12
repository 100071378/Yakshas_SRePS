
import pymysql

db = pymysql.connect("localhost", "kavi", "kavi", "TestDB")

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data =  cursor.fetchone()
print('Database ver: %s' % data)

sql = """CREATE TABLE product (
  prodID varchar(5) NOT NULL,
  category varchar(15) DEFAULT NULL,
  brand varchar(20) DEFAULT NULL,
  name varchar(50) DEFAULT NULL,
  instockNo varchar(10) DEFAULT NULL,
  Price double NOT NULL
)"""

sqlinsert = """INSERT INTO product (prodID, category, brand, name, instockNo, Price) VALUES
('100', 'skin care', 'Activase', 'Neostrata', '100', 55.00),
('101', 'skin care', 'Acuvail', 'Vichy', '101', 95.10),
('102', 'skin care', 'Adagen', 'SilkN', '102', 50.10),
('103', 'skin care', 'Actimmune', 'Gergens', '103', 75.10),
('104', 'skin care', 'Advair HFA', 'Garnier', '104', 100.10),
('105', 'skin care', 'Adlyxin', 'Olay', '105', 25.15),
('106', 'eye drop', 'Systane', 'Alcaftadine', '50', 15.25),
('107', 'hygiene', 'Good Virtues', 'Body Wash', '20', 52.00),
('108', 'hygiene', 'Sunsilk', 'Hand Soap', '10', 20.00),
('109', 'healthcare', 'Sunsilk', 'Shampoo', '50', 28.00),
('110', 'hygiene', 'Pantene', 'Conditioner', '25', 30.50),
('111', 'healthcare', 'Bajaj', 'Panadol', '50', 7.00),
('112', 'intimacy', 'Nivea', 'Alcaftadine', '50', 80.00),
('113', 'intimacy', 'Good Virtues', 'Face Wash', '75', 65.00),
('114', 'healthcare', 'Bajaj', 'Doliprane', '60', 25.60),
('115', 'hygiene', 'Erycalm', 'Body Wash', '15', 45.80),
('116', 'healthcare', 'Sensodyne', 'Toothpaste', '30', 12.50),
('117', 'healthcare', 'Brozers', 'Piriton', '20', 15.15),
('118', 'medical equip', 'Elianors', 'Glucose Tester', '50', 89.50),
('119', 'medical equip', 'Elianors', 'Blood Pressure Tester', '20', 215.30),
('120', 'medicine', 'Axcel Paediatric Syrup', 'Ibuprofen', '100', 5.60),
('121', 'medicine', 'Bactidol Mouthwash', 'Hexetidine 0.1%', '55', 17.90),
('122', 'medicine', 'Acriflavine', 'Acriflavine 0.1% Cream', '102', 4.50),
('123', 'medicine', 'Actapin', 'Amlodipine 10mg Tablet', '25', 0.80),
('124', 'medicine', 'Apo', 'Dipyridamole 25 mg Tablet', '50', 0.30),
('125', 'medicine', 'Apo', 'Dipyridamole 75 mg Tablet', '50', 0.40),
('126', 'medicine', 'Apo', 'Diazepam 5 mg Tablet', '50', 0.60),
('127', 'medicine', 'Apo', 'Diazepam 10 mg Tablet', '50', 0.80),
('128', 'medicine', 'Apo', 'Hydrochlorothiazide 25 mg Tablet', '50', 0.20),
('129', 'medical equip', 'JosheLive', 'Lumbar Waist Support', '45', 26.30),
('130', 'medical equip', 'OEM China', 'Lumbar Waist Support', '28', 24.00),
('131', 'medical equip', 'GoSport', 'Lumbar Waist Support', '49', 25.50),
('132', 'medical equip', 'Big House', 'Lumbar Waist Support', '71', 22.00),
('133', 'medical equip', 'TabTab', 'Lumbar Waist Support', '21', 29.00),
('134', 'medical equip', 'Pure Fitness', 'Body Fat Analyzer', '10', 186.20),
('135', 'medical equip', 'Project EB', 'Body Fat Analyzer', '15', 166.10),
('136', 'medical equip', 'Wenco', 'Body Fat Analyzer', '30', 267.40),
('137', 'medical equip', 'Stonbike', 'Electrical Wheelchair', '12', 2900.15),
('138', 'medical equip', 'Hopkin', 'Deluxe Steel Wheelchair', '5', 688.50),
('139', 'medical equip', 'Accu-Chek', 'Glucose Monitoring System', '7', 181.70),
('140', 'Eye drop', 'Refresh', 'Plus Lubricant Eye Drop', '66', 33.80),
('141', 'Eye drop', 'BAUSCH & LOMB', 'Vidisic Eye Gel', '75', 24.10),
('142', 'Eye drop', 'Blincon', 'Intensive Cleaner', '22', 15.00),
('143', 'Eye drop', 'Optrex', 'Rehydrating Eye Drops', '55', 31.35),
('144', 'Eye drop', 'Vismed', 'Lubricant Eye Drop', '14', 38.50),
('145', 'Eye drop', 'Allergan', 'Optive Fusion UD', '65', 48.80),
('146', 'Eye drop', 'Pharma', 'Allergocrom Eye Drops ', '25', 35.00),
('147', 'Eye drop', 'Alcon', 'Tears Naturale 2 Eye Drops', '20', 27.50),
('148', 'Eye drop', 'Blink', 'Intensive Tears', '17', 30.00),
('149', 'Eye drop', 'Sante', 'Pc Eye Drops', '52', 33.50),
('150', 'healthcare', 'Ba Zhen', 'Herbal Soup', '25', 9.50),
('151', 'healthcare', 'Ba Zhen', 'Chrysanthemum Flower Tea', '42', 10.50),
('152', 'healthcare', 'Ba Zhen', 'Natural Dried Figs Turkey ', '75', 28.80),
('153', 'healthcare', 'Ba Zhen', 'Phnom Penh Rose Flower Tea', '20', 19.00),
('154', 'healthcare', 'Ba Zhen', 'Xinjiang Red Date', '15', 11.00),
('155', 'healthcare', 'Dang Gui', 'Radix Angelica Sinensis', '45', 8800),
('156', 'healthcare', 'Ba Zhen', 'Mulberry Leaf Tea', '26', 10.50),
('157', 'healthcare', 'Ba Zhen', 'XIANG ZHOU LOTUS SEED', '81', 9.80),
('158', 'healthcare', 'Dang Gui', 'Grade 3 Codonopsis pilosula', '31', 67.00),
('159', 'healthcare', 'Ba Zhen', ' Polygonatum Odoratum', '46', 25.00),
('160', 'hygiene', 'Kotex', 'Soft & Smooth Maxi Wing', '25', 12.00),
('161', 'hygiene', 'Kotex', 'Overnight Panties', '77', 9.43),
('162', 'hygiene', 'SanNap', 'Maternity Sanitary Napkin ', '44', 17.90),
('163', 'hygiene', 'Laurier ', 'Super Slimguard Day ', '64', 26.10),
('164', 'hygiene', 'Natracare', 'Organic Cotton Tampons', '14', 14.65),
('165', 'hygiene', 'Johnsons', 'Baby Bubble Bath', '15', 35.15),
('166', 'hygiene', 'Johnsons', 'Baby Powder', '50', 30.36),
('167', 'hygiene', 'Johnsons', 'Soothing Vapor', '20', 38.25),
('168', 'hygiene', 'Himalaya', 'Gentle Baby Shampoo', '10', 28.90),
('169', 'hygiene', 'Himalaya', ' Baby Lotion 400ml', '50', 30.90),
('170', 'hygiene', 'Himalaya', 'Happy Baby Gift Pack', '25', 21.00),
('171', 'intimacy', 'Intimate', '106 ml Eau De Toilette', '50', 152.00),
('172', 'intimacy', 'Apvita', 'Gentle Cleansing Gel', '50', 94.10),
('173', 'intimacy', 'Apvita', 'Gentle Cleansing Gel XL', '75', 117.20),
('174', 'intimacy', 'Intimate', 'Sparkly Little Black Dress Bath Bombs', '60', 167.00),
('175', 'intimacy', 'Intimate', 'White Sage with Hemp Oil Bath Bomb', '15', 95.00),
('176', 'intimacy', 'Intimate', 'Care Cream, Natures Sources', '30', 212.00),
('177', 'intimacy', 'Intimate', 'Love Spell Deep Black Chasm Bath Bomb', '20', 93.15),
('178', 'intimacy', 'Intimate', 'Black Velvet and Gold Sparkles Bath Bomb', '50', 89.30),
('180', 'intimacy', 'Intimate', '2 Winter Wishes Snowflake Bath Bombs', '20', 87.30);"""

try:

    cursor.execute()
    db.commit()
    print('Sucess')

except:
    db.rollback()
    print('fail')

db.close()











