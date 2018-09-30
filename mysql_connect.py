import mysql.connector
import datetime

def add_to_database(time, temp, hum, pres):
    mydb = mysql.connector.connect(
        host="localhost",
        user="pi",
        passwd="Gaborka11",
        database="Weather"
        )
    
    cursor = mydb.cursor()
    
    add_data = ("INSERT INTO data "
                "(date, temp, hum, pres) "
                "VALUES (%s, %s, %s, %s)")
    data= (time, temp, hum, pres)
    
    cursor.execute(add_data, data)
    
    mydb.commit()

    
