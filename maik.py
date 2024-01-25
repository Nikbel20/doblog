import sqlite3

con = sqlite3.connect('zad2.db')
cursor = con.cursor()
cursor.execute("""insert into NIKITA(id, name, age) values (1,'Nikita',20)""")
cursor.execute("""insert into NIKITA(id, name, age) values (2,'Ivan',22)""")
cursor.execute("""insert into NIKITA(id, name, age) values (3,'Ruslan',24)""")
con.commit()
con.close()
