from django.shortcuts import render
from django.http import *
from twitter import *
from twitterfeed import settings
import json


def home(request):
    return  render(request,"home.html",{})

def getfeed(request):
    #create initiate twitter api
    twitter = Twitter(format="json",
		auth = OAuth(settings.access_key, settings.access_secret, settings.consumer_key, settings.consumer_secret))
    #getting nick name
    user = request.GET['name']
    #get last 5 tweets
    results = twitter.statuses.user_timeline(screen_name = user,count=5)
    #return results in json format
    return   HttpResponse(json.dumps(results))
