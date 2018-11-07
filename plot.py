#! /usr/bin/python3

import mysql_connect as mc
import matplotlib.pyplot as plt
import mpld3
import datetime
import sys

mydb = mc.mydb
cursor = mc.cursor

def plot(arg, a = None, b = None):
    data = mc.plot(arg, a, b)
    fig = plt.figure(1,figsize=(5,4))
    plt.plot(data[0],data[1],"o-", label="Hőmérséklet")
    plt.plot(data[0],data[2],"o-", label="Páratartalom")
    plt.plot(data[0],data[3], "o-", label="Légnyomás")
    if arg == "max":
        plt.title("Napi legmagasabb mérési adatok")
    elif arg == "min":
        plt.title("Napi legalacsonyabb mérési adatok")
    elif arg == "avg":
        plt.title("Napi átlag mérési adatok")
    elif arg == "all":
        plt.title("Összes mérési adatok")
    elif arg == "custom":
        plt.title("Mérési adatok az adott dátum közt")
    plt.xlabel("Dátum")
    plt.ylabel("Érték")
    plt.grid()
    plt.legend()
    #plt.show()
    mpld3.save_html(fig, "/var/www/html/%s.html" %arg)
    plt.close('all')

plot("all")
plot("avg")
plot("max")
plot("min")
if len(sys.argv) > 1:
    plot(sys.argv[1], sys.argv[2], sys.argv[3])