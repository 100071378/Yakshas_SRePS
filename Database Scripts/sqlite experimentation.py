import sqlite3

conn = sqlite3.connect('test.db')

c = conn.cursor()

# c.execute("""CREATE TABLE test ( first int, second int)""")

# c.execute("INSERT INTO test VALUES (10,15)")

#second way
# "INSERT INTO test VALUES ( ?, ?)", (variable1, variable2)

#third way
## "INSERT INTO test VALUES ( :first, :second)", {'first': variable1, 'second': variable2}

# c.execute("SELECT * FROM test WHERE first=?",('value',))

# c.execute("SELECT * FROM test WHERE first=:first",{'first': 'value'})

c.execute("SELECT * FROM test")

print(c.fetchall())

conn.commit()
conn.close()