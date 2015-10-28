# twitter_feeds
geting last 5 tweets by nickname
<br><br>
requirements:<br>
python2.7<br>
Django==1.8<br>
argparse==1.2.1<br>
oauthlib==0.7.2<br>
requests==2.6.0<br>
requests-oauthlib==0.4.2<br>
twitter==1.17.1<br>
wsgiref==0.1.2<br>
<br><br>
 4 importants files:<br>
 templates/home.html   // conatin the ui form where you enter the username and display the tweets (evento free template) <br>
 static/js/main.js   // collecting data from user and send ajax request and wait for server replay <br>
 twitterfeed/urls.py   // direct the user to home page and handle ajax request <br>
 feed/views.py   /// returning home view and processes the ajax request  <br>
 
 
 
