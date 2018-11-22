#!/usr/bin/python3
from sense_hat import SenseHat
import mysql_connect as mc
import os
from time import sleep
from datetime import datetime
import argparse
import twitter_bot as tw
import sendemail
import plot

sense = SenseHat()
date = datetime.now().replace(microsecond = 0)
file = "/var/www/html/data/"+str(date.year)+"-"+str(date.month)+"-"+str(date.day)+".csv"

#command line argument
parser = argparse.ArgumentParser(description="Weather Station Pythonnal.", epilog="Kilépés a programból: ctrl+c")
parser.add_argument("-t", "--time",dest="time", help="Meresi idokoz perben.", type=float, default=60) #60 1 óra
parser.add_argument("-o", "--out",dest="out", help="Kimeneti fajl helye, neve, kiterjesztese Pl.: -o fol/der/data.dat", type=str, default=file)
parser.add_argument("-F", "--from", dest="fromdate", help='Kezdo datum Pl.: "2018-03-31 12:00:00"', type=str, default=None)
parser.add_argument("-T", "--to", dest="todate", help='Veg datum Pl.: "2018-04-30 08:00:00"', type=str, default=None)
wait_time = parser.parse_args().time
file = parser.parse_args().out
fromdate = parser.parse_args().fromdate
todate = parser.parse_args().todate

def get_cpu_temp():
    res = os.popen("vcgencmd measure_temp").readline()
    t = float(res.replace("temp=","").replace("'C\n",""))
    return(t)

def check_file(file):
    if not os.path.exists(os.path.dirname(file)) and ("/" in file):
        os.makedirs(os.path.dirname(file))
        os.chmod(os.path.dirname(file), 0o775)
        f = open(file, "w+")
        f.writelines("[time]\t\t[temp]\t[hum]\t[pres]\n")
        f.close()
    elif not("/" in file):
        f = open(file, "w+")
        f.writelines("[time]\t\t[temp]\t[hum]\t[pres]\n")
        f.close()
    
try:
    #create folders and files
    check_file(file)
    file = open(file, "a+")
    print("Az adatok ide mentodnek:",file.name)
    while True:
        #get data
        temp = sense.get_temperature_from_humidity()
        hum = sense.get_humidity()
        pres = sense.get_pressure()
        correct = temp - ((get_cpu_temp()-temp)/0.98)
        date = datetime.now().replace(microsecond = 0)
        
        #printing and write to file
        print("%d:%d:%d\t\t%.2f\t%.2f\t%.2f" %(date.hour, date.minute, date.second, correct, hum, pres))
        #file.writelines("%d:%d:%d\t\t%.2f\t%.2f\t%.2f" %(date.hour, date.minute, date.second, correct, hum, pres)+"\n")
        #mc.add_to_database(date, correct, hum, pres)
        #plot.plot("all")
        #plot.plot("min")
        #plot.plot("max")
        #plot.plot("avg")
        #if fromdate != None and todate != None:
        #    plot.plot("custom", fromdate, todate)
        #tw.post(date, correct, hum, pres)
        #sendemail.send_email(sendemail.set_text(correct,date))
        
        file.flush()
        
        try:
            sleep(wait_time*60) #wait 1 hour 60^2, *60 percbe adja meg a paraméter
        except KeyboardInterrupt:
            raise KeyboardInterrupt
except KeyboardInterrupt:
    sense.show_message("Goodbye!", scroll_speed=0.05, text_colour=(255,0,0))
    file.close()
    sense.clear()
finally:
    print("\nKilépés...")
