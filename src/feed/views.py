from django.shortcuts import render
from django.http import *
from twitter import *
import json
# Create your views here.


consumer_key = "iSyU15L2TdWpV9wk0zZUTZTg6"
consumer_secret = "ytpM49Xf0OkR36nEYqBIypY0pFJOXiAfCyQYlIEznfSXaCzfkO"
access_key = "248807542-TafarFd7nluXlj8Eg5maPnw7EgjZ1HO2a5g5GKx0"
access_secret = "4pbBZSW8Cfi6ASs5Cks6HPakAz82ceEMyMs4YPgDwp5D0"
def home(request):

    return  render(request,"home.html",{})

def getfeed(request):
    config = {}

    twitter = Twitter(format="json",
		auth = OAuth(access_key, access_secret, consumer_key, consumer_secret))

    user = request.GET['name']

    results = twitter.statuses.user_timeline(screen_name = user,count=5)

    #for status in results:
	 #  print "(%s) %s" % (status["created_at"], status["text"].encode("ascii", "ignore"))

    return   HttpResponse(json.dumps(results))

twitter = Twitter(
		auth = OAuth(access_key, access_secret, consumer_key, consumer_secret))


results = twitter.statuses.user_timeline(screen_name = "AllStateBanners",count=5)
for status in results:
  print "(%s) %s" % (status["created_at"], status["text"].encode("utf8", "ignore"))