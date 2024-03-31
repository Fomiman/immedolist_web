import sqlite3

## DB connect
conn =  sqlite3.connect('test.db')
c = conn.cursor()

## create table
c.execute(
    """
    select * from SCHEDULE_LIST;
"""
)

rows = c.fetchall()

for row in rows :
    print(row)

conn.commit()

c.close()
conn.close()    
