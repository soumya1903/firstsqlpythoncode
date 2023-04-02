import psycopg2
#from config import config

# first comment
# changing this code on local machine first time after creating repository in github
# changing this code on github
# changing this code on github secondtime
conn = psycopg2.connect(
    database="test",
    user="postgres",
    password="postgres",
    host="localhost",
    port='5432'
)


cur = conn.cursor()


cur.execute("SELECT * FROM car")

rows = cur.fetchall()

for row in rows:
    print(row)
