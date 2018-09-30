from twython import Twython

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
    msg = "%s - Homerseklet: %.2f C, Para tartalom: %.2f g/m, Legnyomas: %.2f"
    % (date, temp, hum, pres)
    twitter.update_status(status = msg)