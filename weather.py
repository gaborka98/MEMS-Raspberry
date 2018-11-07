#!/usr/bin/python3
from sense_hat import SenseHat
import mysql_connect as mc
import os, sys
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
wait_time = parser.parse_args().time
file = parser.parse_args().out


#if 2 > len(sys.argv):
#    wait_time= 60^2
#else:
#    wait_time = int(sys.argv[1])

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
    loop = True
    while loop:
        #get data
        temp = sense.get_temperature_from_humidity()
        hum = sense.get_humidity()
        pres = sense.get_pressure()
        correct = temp - ((get_cpu_temp()-temp)/0.98)
        date = datetime.now().replace(microsecond = 0)

        
        #printing and write to file
        print("%d:%d:%d\t%.2f\t%.2f\t%.2f" %(date.hour, date.minute, date.second, correct, hum, pres))
        file.writelines("%d:%d:%d\t\t%.2f\t%.2f\t%.2f" %(date.hour, date.minute, date.second, correct, hum, pres)+"\n")
        mc.add_to_database(date, correct, hum, pres)
        plot.plot("all")
        plot.plot("min")
        plot.plot("max")
        plot.plot("avg")
        tw.post(date, correct, hum, pres)
        sendemail.send_email(sendemail.set_text(correct,date),date)
        
        file.flush()
        
        try:
            sleep(wait_time*60) #wait 1 hour 60^2, *60 percbe adja meg a paraméter
        except KeyboardInterrupt:
            loop = False
            raise KeyboardInterrupt
except KeyboardInterrupt:
    sense.show_message("Goodbye!", scroll_speed=0.05, text_colour=(255,0,0))
    file.close()
    sense.clear()
finally:
    print("\nKilépés...")