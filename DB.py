import sqlite3


conn = sqlite3.connect('example2.db')

#create curser
c = conn.cursor()

#creating table in the database where the products and it's information will be store

#c.execute("INSERT INTO products VALUES (4,'Titanic (DVD)', 4.75,30)")
#c.execute("INSERT INTO products VALUES (5,'Brave Heart (DVD)', 8.97,20)")
#c.execute("INSERT INTO products VALUES (6,'Heat (DVD)', 6.5,15)")





conn.commit()
conn.close()