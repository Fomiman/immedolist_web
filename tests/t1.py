import sqlite3

## DB connect
conn =  sqlite3.connect('test.db')
c = conn.cursor()

## create table
c.execute(
    """
    CREATE TABLE IF NOT EXISTS SCHEDULE_LIST (
        id INT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        start_date DATE NOT NULL,
        end_date DATE NOT NULL,
        schedule_type VARCHAR(50) NOT NULL,
        frequency VARCHAR(50) NOT NULL,
        recurrence INT NOT NULL
)
"""
)

conn.commit()

c.close()
conn.close()    