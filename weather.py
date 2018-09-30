from sense_hat import SenseHat
import mysql_connect as mc
import os, sys
import time, datetime
import argparse
import twitter_bot as tw

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

sense = SenseHat()
sense.set_rotation(180)
date = datetime.datetime.now().replace(microsecond=0)
file = "Project/data/"+str(date.year)+"-"+str(date.month)+"-"+str(date.day)+".txt"

#command line argument
parser = argparse.ArgumentParser(description="Weather Station with python.",
                                 epilog="Kilépés a programból: ctrl+c")
parser.add_argument("-t", "--time",dest="time", help="get data intervall in second.", type=int, default=(60*60))
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
            os.chmod(os.path.dirname(file), 0o777)
            f = open(file, "w+")
            f.close()
        except OSError as exc:
            raise
    elif not("/" in file):
        f = open(file, "w+")
        f.close()

def main():
    try:
        #create folders and files
        global file
        check_file(file)
        file = open(file, "a+")
        print("Az adatok ide mentődnek:",file.name)
        while True:
            #initialize
            temp = sense.get_temperature_from_humidity()
            hum = sense.get_humidity()
            pres = sense.get_pressure()
            correct = temp - ((get_cpu_temp()-temp)/5.466)-6
            global date
            date = datetime.datetime.now().replace(microsecond=0)
            
            
            #printing and write to file
            print("%d:%d:%d - T: %.2f - H: %.2f - P: %.2f" %(date.hour, date.minute, date.second, correct, hum, pres))
            file.writelines("%d:%d:%d - T: %.2f - H: %.2f - P: %.2f" %(date.hour, date.minute, date.second, correct, hum, pres)+"\n")
            mc.add_to_database(date, correct, hum, pres)
            tw.post(date, correct, hum, pres)
            
            
            time.sleep(wait_time) #wait 1 hour 60^2
    except KeyboardInterrupt:
        file.close()
        pass

if __name__ == "__main__":
    main()

sense.clear()