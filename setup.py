import sqlite3 as db

with db.connect('database.db') as conn:
    conn.execute('drop table if exists counts;')
    conn.execute('create table counts (id integer primary key not null)')
    conn.execute('insert into counts (id) VALUES (1)')
    conn.commit()
    print('Successfully created database')
