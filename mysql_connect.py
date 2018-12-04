import mysql.connector
import mysql_auth as auth
from datetime import datetime

mydb = mysql.connector.connect(
    host = auth.host,
    user = auth.user,
    password = auth.passwd,
    database = auth.database
    )
cursor = mydb.cursor()

def add_to_database(time, temp, hum, pres):
    add_data = ("INSERT INTO data "
                "(date, temp, hum, pres) "
                "VALUES (%s, %s, %s, %s)")
    data= (time, round(temp,2), round(hum,2), round(pres,2))
    
    cursor.execute(add_data, data)
    
    mydb.commit()
    
def twitter(arg,a=None,b=None):
    if arg == "avg":
        query = ("SELECT AVG(temp) FROM data "
                 "WHERE date BETWEEN %s AND %s")
    elif arg == "min":
        query = ("SELECT MIN(temp) FROM data "
                 "WHERE date BETWEEN %s AND %s")
    elif arg == "max":
        query = ("SELECT date, MAX(temp) FROM data "
                 "WHERE date BETWEEN %s AND %s")
    
    cursor.execute(query, (a,b))
    for data in cursor:
        return data[0]

def plot(arg, a=None, b=None):
    data = []
    dates = []
    temps = []
    hums = []
    presures = []
    if arg == "avg":
        query = ("SELECT date, AVG(temp), AVG(hum), AVG(pres) FROM data "
                 "GROUP BY DATE(date)")
    elif arg == "min":
        query = ("SELECT date, MIN(temp), MIN(hum), MIN(pres) FROM data "
                 "GROUP BY DATE(date)")
    elif arg == "max":
        query = ("SELECT date, MAX(temp), MAX(hum), MAX(pres) FROM data "
                 "GROUP BY DATE(date)")
    elif arg == "custom":
        query = ("SELECT date, temp, hum, pres FROM data "
                 "WHERE date BETWEEN %s AND %s")
    else:
        query = ("SELECT date, temp, hum, pres FROM data")
    cursor.execute(query,(a,b))
    for (date,temp,hum,pres) in cursor:
            dates.append(date)
            temps.append(temp)
            hums.append(hum)
            presures.append(pres)
    data.append(dates)
    data.append(temps)
    data.append(hums)
    data.append(presures)
    return data