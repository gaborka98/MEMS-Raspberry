from twython import Twython
import mysql_connect as mc

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

def post(date, temp, hum, pres):
    if date.hour == 20 and date.minute == 0 and date.second == 0:
        msg = "A napi átlag hőmérséklet (8:00 és 20:00 közt): %.2f" % mc.avg("","")
        twitter.update_status(status=msg)
        msg = "A mai nap legmagasabb hőmérséklete (8:00 és 20:00 ,özt): %.2f" % mc.max("","")
        twitter.update_status(status=msg)
        msg = "A mai nap legalacsonyabb hőmérséklete (8:00 és 20:00 ,özt): %.2f" % mc.min("","")
        twitter.update_status(status=msg)
        
    msg = "%s - Homerseklet: %.2f C, Para tartalom: %.2f g/m, Legnyomas: %.2f" \
        % (date, temp, hum, pres)
    twitter.update_status(status = msg)