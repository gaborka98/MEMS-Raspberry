from twython import Twython
from twython import TwythonError
import mysql_connect as mc
from datetime import datetime
from sense_hat import SenseHat

sense = SenseHat()

consumer_key = 'ofoSudll3PZmPyDOaBpshBEe8'
consumer_secret = 'BSWUqEfCF3G1HRODKwUN51O5qwUfURi2r3Joxv7u4HY2hBDfQp'
access_token = '479690115-B83jqVyzF6Ed4GwYpQJgWkTQPIv604ny5wdh8iVF'
access_token_secret = 'SKZN10FaCJJCeZjIHbLpw6gQiiLB9TOPGVzBFh7JKhY65'

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

megjo = True
def post_avg(date):
    global megjo
    if megjo and (date.hour == 20):
        msg = """A mai nap átlag hőmérséklete: %s
A mai nap legnagyobb hőmérséklete: %s
A mai nap legkisebb hőmérséklete: %s""" % (mc.avg("",""), mc.max("",""), mc.min("",""))
        twitter.update_status(status = msg)
        megjo = False
    else:
        megjo = True


def post(date, temp, hum, pres):
    msg = "%s - Hőmérséklet: %.2f C, Pára tartalom: %.2f g/m, Légnyomás: %.2f Pa" \
        % (date, temp, hum, pres)
    twitter.update_status(status = msg)