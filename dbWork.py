import sqlite3

conn = sqlite3.connect('friends.sqlite')
cur = conn.cursor()

cur.execute('''DROP table if exists 'school' ''')
cur.execute('''
create table school('id' INTEGER PRIMARY KEY AUTOINCREMENT, 'schoolName' text, 'num' numeric)
''')

first = input('Enter School ')

cur.execute('''insert into school(schoolName,num) values(?, 4)''',(first,) )

for row in cur.execute("select * from school"):
    print(row)
