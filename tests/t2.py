import sqlite3

## DB connect
conn =  sqlite3.connect('test.db')
c = conn.cursor()

## create table
c.execute(
    """
    insert into SCHEDULE_LIST values(1,'john','2024/03/31','2024/04/20','not easy','and',3);
"""
)

conn.commit()

c.close()
conn.close()    

