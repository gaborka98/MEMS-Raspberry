import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(
    host="localhost",
    user="pi",
    passwd="Gaborka11",
    database="Weather"
    )
cursor = mydb.cursor()

def add_to_database(time, temp, hum, pres):
    add_data = ("INSERT INTO data "
                "(date, temp, hum, pres) "
                "VALUES (%s, %s, %s, %s)")
    data= (time, temp, hum, pres)
    
    cursor.execute(add_data, data)
    
    mydb.commit()
    
def set_date(a,b):
    if a == "" and b == "":
        today = datetime.datetime.now().replace(microsecond = 0)
        a = datetime(today.year, today.month, today.day,8,00,00)
        b = datetime(today.year, today.month, today.day,20,00,00)
    else:
        a = datetime.strptime(str(a), "%Y-%m-%d %H:%M:%S")
        b = datetime.strptime(str(b), "%Y-%m-%d %H:%M:%S")
    return (a,b)
        
def avg(a,b):   
    query = ("SELECT AVG(temp) FROM data "
             "WHERE date BETWEEN %s AND %s")
    
    cursor.execute(query, set_date(a,b))
    for avg in cursor:
        return avg
        #print("Átlag %s és %s közt: %.2f" % a, b, temp)
def max(a,b):
    query = ("SELECT MAX(temp) FROM data "
             "WHERE date BETWEEN %s AND %s")
    
    cursor.execute(query, set_date(a,b))
    for max in cursor:
        return max
    
def min(a,b):
    query = ("SELECT MIN(temp) FROM data "
             "WHERE date BETWEEN %s AND %s")
    
    cursor.execute(query, set_date(a,b))
    for min in cursor:
        return min
    
    
