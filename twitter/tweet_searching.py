import tweepy
from tweepy import OAuthHandler
import  json

consumer_key = "ERaD9fEP8ARELnwfV5qbpbMYo" # The application's consumer key
consumer_secret = "vlG9htHUwmdMq3s271QUzgqrvTxnlXzFkBeNHMfWYMJYdaKVxr" # The application's consumer secret
access_token = "171383939-OOIv348clmL6mDDvNBEhcpRxYdsnO8wUEygbMleS" #The access token granted after OAuth authorization
access_secret = "xx5Of6kIDXytsH8PTqmIO6uwYIQLzFuBAo4MtzeRnkFXn" # The access token secret granted after OAuth authorization

## Authenticate with your app credentials
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
## get tweet's from your timeline
# with open('search.json', 'w') as f:
#     for status in tweepy.Cursor(api.search, q="advanced analytics solutions").items(50):
#         f.writelines(json.dumps(status._json, indent=4, sort_keys=True))
#         print status.user.name

#Getting Geo ID for USA
places = api.geo_search(query="Noida", granularity="city")

#Copy USA id
place_id = places[0].id
print('USA id is: ',place_id)