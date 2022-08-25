from datetime import datetime, timezone
from itertools import dropwhile, takewhile
import pandas as pd
import instaloader
import pytz

L = instaloader.Instaloader()

username = 'sebuah_username'
password = 'sebuah_password'

L.login(username, password)

searchuser = 'instagram'
posts = instaloader.Profile.from_username(L.context, "instagram").get_posts()

profile = instaloader.Profile.from_username(L.context, searchuser)

SINCE = datetime(2022, 1, 1)
UNTIL = datetime(2022, 7, 1)

dt_aware_tz = datetime.utcnow().replace(tzinfo=timezone.utc)

def convert_time_to_wib(dt_object):
  tz = pytz.timezone("Asia/Jakarta")

  utc = pytz.timezone("UTC")

  tz_aware_dt = utc.localize(dt_object)
  local_dt = tz_aware_dt.astimezone(tz)

  return local_dt.strftime("%Y-%m-%d %H:%M:%S")

posts = profile.get_posts()

likeslist = []
commentlist = []
dateslist = []

for post in takewhile(lambda p: p.date >= SINCE, dropwhile(lambda p: p.date > UNTIL, posts)):
        
        dates = convert_time_to_wib(post.date)
        
        n_comments = 0
        for comment in post.get_comments() :
            n_comments += 1

        likes = post.likes

        likeslist.append(likes)
        commentlist.append(n_comments)
        dateslist.append(dates)

data = pd.DataFrame({"Dates":dateslist, "Likes":likeslist, "Comments":commentlist})

data.to_csv('instagram.csv')
