import mysql.connector
import csv
import ConfigParser

inifile = ConfigParser.ConfigParser()
inifile.read("config/database.ini")
dbcon = mysql.connector.connect(
  database=inifile.get("database", "db"),
  user=inifile.get("database", "user"),
  password=inifile.get("database", "password"),
  host=inifile.get("database", "host")
)
dbcur = dbcon.cursor()
with open('RCdata/chefmozaccepts.csv') as csvfile:
  reader = csv.reader(csvfile)
  next(reader, None)
  for row in reader:
    dbcur.execute('INSERT INTO restaurants_payments_methods (restaurant_id, payment_method) VALUES(%s, "%s")' % tuple(row))
dbcon.commit()
