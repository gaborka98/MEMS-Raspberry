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
twitter.verify_credentials()

megjo = True
def post_avg(date):
    global megjo
    if megjo and (date.hour == 20):
        msg = """%s
A mai nap átlag hőmérséklete: %s
A mai nap legnagyobb hőmérséklete: %s
A mai nap legkisebb hőmérséklete: %s""" % (date, mc.twitter("avg"), mc.twitter("max"), mc.twitter("min"))
        try:
            twitter.update_status(status = msg)
        except TwythonError:
            print("Valami hiba történt a napi eredmények tweetelésekor")
        megjo = False
    else:
        megjo = True


def post(date, temp, hum, pres):
    msg = "%s - Hőmérséklet: %.2f C, Pára tartalom: %.2f g/m, Légnyomás: %.2f Pa" \
        % (date, temp, hum, pres)
    try:
        twitter.update_status(status = msg)
    except TwythonError:
        print("valamu hiba történt tweetelés közben")
    post_avg(date)