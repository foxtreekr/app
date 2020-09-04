import psycopg2
import pandas as pd

conn_string ="host='192.168.80.133' dbname='pyappdb' user='postgres' password='cicsii'"
conn = psycopg2.connect(conn_string)
cur = conn.cursor()

cur.execute("select * from account;")
result = cur.fetchall()

your_dataframe = pd.DataFrame(cur.fetchall())
# your_dataframe.columns = [desc[0] for desc in cur.description]