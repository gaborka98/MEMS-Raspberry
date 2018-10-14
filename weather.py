#!/usr/bin/env python3.5
from sense_hat import SenseHat
import mysql_connect as mc
import os, sys
import time, datetime
import argparse
import twitter_bot as tw

sense = SenseHat()
date = datetime.datetime.now().replace(microsecond=0)
file = "Project/data/"+str(date.year)+"-"+str(date.month)+"-"+str(date.day)+".csv"
retry = True

#command line argument
parser = argparse.ArgumentParser(description="Weather Station with python.", epilog="Kilépés a programból: ctrl+c")
parser.add_argument("-t", "--time",dest="time", help="get data intervall in second.", type=int, default=(60*60)) #60 1 óra
parser.add_argument("-o", "--out",dest="out", help="Output filename (with path, extension) Example: -o fol/der/data.dat", type=str, default=file)
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
        try:
            os.makedirs(os.path.dirname(file))
            os.chmod(os.path.dirname(file), 0o775)
            f = open(file, "w+")
            f.writelines("[time]\t\t[temp]\t[hum]\t[pres]\n")
            sense.load_image("img/folder.png")
            time.sleep(1)
            sense.load_image("img/done.png")
            time.sleep(1)
            f.close()
        except OSError as exc:
            time.sleep(1)
            sense.load_image("img/bad.png")
            time.sleep(1)
            raise
    elif not("/" in file):
        try:
            f = open(file, "w+")
            f.writelines("[time]\t\t[temp]\t[hum]\t[pres]\n")
            f.close()
            sense.load_image("img/folder.png")
            time.sleep(1)
            sense.load_image("img/done.png")
            time.sleep(1)
        except IOError:
            sense.load_image("img/folder.png")
            time.sleep(1)
            sense.load_image("img/bad.png")
            time.sleep(1)
            raise

def exit_joystick(event):
    global retry
    retry = False
    sense.show_message("Goodbye!", scroll_speed=0.4, (255,0,0))

def main():
    try:
        #create folders and files
        global file
        check_file(file)
        file = open(file, "a+")
        print("Az adatok ide mentodnek:",file.name)
        while (not os.path.exists("/home/pi/Project/stop")) and retry:
            #initialize
            temp = sense.get_temperature_from_humidity()
            hum = sense.get_humidity()
            pres = sense.get_pressure()
            correct = temp - ((get_cpu_temp()-temp)/0.98)
            global date
            date = datetime.datetime.now().replace(microsecond=0)
				
            #printing and write to file
            print("%d:%d:%d\t%.2f\t%.2f\t%.2f" %(date.hour, date.minute, date.second, correct, hum, pres))
            file.writelines("%d:%d:%d\t%.2f\t%.2f\t%.2f" %(date.hour, date.minute, date.second, correct, hum, pres)+"\n")
            mc.add_to_database(date, correct, hum, pres)
            tw.post(date, correct, hum, pres)
            sense.stick.direction_any = exit_joystick
            
            time.sleep(wait_time) #wait 1 hour 60^2, *60 percbe adja meg a paraméter
    except KeyboardInterrupt:
        #mc.avg()
        file.close()
        sense.show_message("Goodbye!", scroll_speed=0.4, (255,0,0))
        pass

if __name__ == "__main__":
    main()

os.system("sudo rm Project/stop")
sense.show_message("Goodbye!", scroll_speed=0.4, (255,0,0))
file.close()
sense.clear()
