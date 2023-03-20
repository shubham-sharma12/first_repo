import sqlite3
con = sqlite3.connect('bank.db')
print(con)
cur = con.cursor()
print(cur)