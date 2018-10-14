import matplotlib.pyplot as plt
import mpld3
import mysql.connector
import datetime

mydb = mysql.connector.connect(
    host="localhost",
    user="pi",
    passwd="Gaborka11",
    database="Weather"
    )
cursor = mydb.cursor()

dates = []
temps = []
hums = []
presures = []
today = datetime.date.today()

def plot_all():
    global temps, dates, hums,presures
    dates = []
    temps = []
    hums = []
    presures = []
    query = ("SELECT date, temp, hum, pres FROM data")
    cursor.execute(query)
    for (date,temp,hum,pres) in cursor:
            dates.append(date)
            temps.append(temp)
            hums.append(hum)
            presures.append(pres)
    all = plt.figure(1,figsize=(5,4))
    plt.plot(dates,temps,"o-", label="Hőmérséklet")
    plt.plot(dates,hums,"o-", label="Páratartalom")
    plt.plot(dates,presures, "o-", label="Légnyomás")
    plt.title("Összes mérési adat")
    plt.xlabel("Dátum")
    plt.ylabel("Érték")
    plt.grid()
    mpld3.save_html(all, "all.html")
    plt.close('all')
    
def plot_avg():
    global temps, dates, hums,presures
    dates = []
    temps = []
    hums = []
    presures = []
    query = ("SELECT date, AVG(temp), AVG(hum), AVG(pres) FROM data "
             "GROUP BY DATE(date)")
    cursor.execute(query)
    for (date,temp,hum,pres) in cursor:
            dates.append(date.date())
            temps.append(temp)
            hums.append(hum)
            presures.append(pres)
    avg = plt.figure(1,figsize=(5,4))
    plt.plot(dates,temps,"o-", label="Hőmérséglet")
    plt.plot(dates,hums,"o-")
    plt.plot(dates,presures,"o-")
    plt.title("Átlag mérési adatok")
    plt.xlabel("Dátum")
    plt.ylabel("Érték")
    plt.grid()
    plt.legend()
    mpld3.save_html(avg, "avg.html")
    plt.close('all')
    
def plot_min():
    global temps, dates, hums,presures
    dates = []
    temps = []
    hums = []
    presures = []
    query = ("SELECT date, MIN(temp), MIN(hum), MIN(pres) FROM data "
             "GROUP BY DATE(date)")
    cursor.execute(query)
    for (date,temp,hum,pres) in cursor:
            dates.append(date.date())
            temps.append(temp)
            hums.append(hum)
            presures.append(pres)
    min = plt.figure(1,figsize=(5,4))
    plt.plot(dates,temps,"o-", label="Hőmérséglet")
    plt.plot(dates,hums,"o-")
    plt.plot(dates,presures,"o-")
    plt.title("Legalacsonyabb mérési adatok")
    plt.xlabel("Dátum")
    plt.ylabel("Érték")
    plt.grid()
    plt.legend()
    mpld3.save_html(min, "min.html")
    plt.close('all')
    
def plot_max():
    global temps, dates, hums,presures
    dates = []
    temps = []
    hums = []
    presures = []
    query = ("SELECT date, MAX(temp), MAX(hum), MAX(pres) FROM data "
             "GROUP BY DATE(date)")
    cursor.execute(query)
    for (date,temp,hum,pres) in cursor:
            dates.append(date.date())
            temps.append(temp)
            hums.append(hum)
            presures.append(pres)
    max = plt.figure(1,figsize=(5,4))
    plt.plot(dates,temps,"o-", label="Hőmérséglet")
    plt.plot(dates,hums,"o-")
    plt.plot(dates,presures,"o-")
    plt.title("Legmagasabb mérési adatok")
    plt.xlabel("Dátum")
    plt.ylabel("Érték")
    plt.grid()
    plt.legend()
    mpld3.save_html(max, "max.html")
    plt.close('all')

plot_all()
plot_avg()
plot_min()
plot_max()