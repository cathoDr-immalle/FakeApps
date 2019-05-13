import csv
import sqlite3
import os

db_filename = 'FakeApps.sqlite3'
def create_db():

    conn = sqlite3.connect(db_filename)
    c = conn.cursor()

    #c.execute("CREATE TABLE FakeApps(id text primary key, name text,category text, downloads text, price text)")

    with open('FakeApps.csv', newline ='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            print(', '.join(row))

    conn.commit()
    c.close()

if __name__ == '__main__':
    if os.path.isfile(db_filename):
        os.remove(db_filename)
    create_db()