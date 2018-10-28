import twitter_auth
from twython import Twython
from twython import TwythonError
import mysql_connect as mc
from datetime import datetime

twitter = Twython(
    twitter_auth.consumer_key,
    twitter_auth.consumer_secret,
    twitter_auth.access_token,
    twitter_auth.access_token_secret
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