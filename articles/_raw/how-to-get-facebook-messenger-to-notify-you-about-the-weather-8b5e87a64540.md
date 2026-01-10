---
title: How to get Facebook messenger to notify you about the weather
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-24T18:22:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-facebook-messenger-to-notify-you-about-the-weather-8b5e87a64540
coverImage: https://cdn-media-1.freecodecamp.org/images/1*RBHbkOfMOzl7o_crT4Rg7g.jpeg
tags:
- name: Facebook Messenger
  slug: facebook-messenger
- name: bots
  slug: bots
- name: how-to
  slug: how-to
- name: Python
  slug: python
- name: weather
  slug: weather
seo_title: null
seo_desc: 'By Ekapope Viriyakovithya

  A complete DIY guide to build your own weather alert bot.

  The morning routine is always stressful. Wouldn’t it be wonderful if you had one
  less thing to worry about in the morning?

  What if you had a customizable weather aler...'
---

By Ekapope Viriyakovithya

### A complete DIY guide to build your own weather alert bot.

The morning routine is always stressful. Wouldn’t it be wonderful if you had one less thing to worry about in the morning?

What if you had a customizable weather alert bot that sent you a short message ONLY when there was a chance of rain above your pre-defined threshold?

Don’t waste your time checking the weather in a separate app. It can be live on your Facebook messenger chatbox!

### What do you need?

* Python 3.6 (or earlier) with pandas and [fbchat](https://github.com/carpedm20/fbchat) packages installed

```bash
pip install fbchat
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*Uy6HxLRFNAOcpu40NDfXSw.png)
_AccuWeather Free Account_

* [AccuWeather developer account](https://developer.accuweather.com/packages), the free package should be enough. It provides 50 calls/day with 1 key/developer account.

### Let’s get started!

At the end of this how-to, you will have 3 files in the scripts folder:

[keys.py](https://github.com/ekapope/Weather_Alert_Notification_Facebook_Chat/tree/master/scripts) : to store your facebook email, password, and accuweather API key

[params.py](https://github.com/ekapope/Weather_Alert_Notification_Facebook_Chat/blob/master/scripts/params.py) : to store the threshold and weather forecast location id

[main.py](https://github.com/ekapope/Weather_Alert_Notification_Facebook_Chat/blob/master/scripts/main.py) : this is the main script, it will call the keys.py and params.py

#### 1. Setup Facebook account and AccuWeather API key

First, let’s put your account detail in the [keys.py](https://github.com/ekapope/Weather_Alert_Notification_Facebook_Chat/blob/master/scripts/keys.py) file.

```py
# Your Facebook usersname (email)
FB_USERNAME= "" 

# Your Facebook password
FB_PASSWORD= "" 

# Your AccuWeather API key
ACCUWEATHER_API_KEY= ""
```

#### **2. Setup parameters**

In this step, we will define the threshold for the probability of rain or snow, delay time between each request and message, and also location.

Currently, we set the threshold at 25% for both rain and snow. We will get the alert message only if the AccuWeather data shows the probability ≥ 25%.

The scripts below will request data from AccuWeather every 1 hour ( UPDATE_INTERVAL_HR= 1) and will send a message every 4 hours ( DELAY_TIME_HR= 4).

These parameters will be stored in the [params.py](https://github.com/ekapope/Weather_Alert_Notification_Facebook_Chat/blob/master/scripts/params.py) file.

```py
# Define % threshold for probability of rain and snow. 
# The msg will be sent out if the % chance exceed the value
RAIN_THRESHOLD = 25
SNOW_THRESHOLD = 25

# time between Accuweather request (in hour)
UPDATE_INTERVAL_HR = 1 

# delay time between msg (in hour)
DELAY_TIME_HR = 4 

# location id
# for example, https://www.accuweather.com/en/fr/lille/135564/weather-forecast/135564
# location id is 135564
LOCATION_ID = "135564" 
```

#### 3. Retrieve data from AccuWeather

Now here comes the fun part. We will now work on the main script.

If you plan to run it locally, setup your directory and import keys and params. Make sure you put [keys.py](https://github.com/ekapope/Weather_Alert_Notification_Facebook_Chat/blob/master/scripts/keys.py) and [params.py](https://github.com/ekapope/Weather_Alert_Notification_Facebook_Chat/blob/master/scripts/params.py) in the same folder as this [main.py](https://github.com/ekapope/Weather_Alert_Notification_Facebook_Chat/blob/master/scripts/main.py) script.

```py
#set the current directory
import os
os.chdir(r".\YOUR_PATH")
###############################################################################
#import keys and parameters other scripts in the same folder
from keys import FB_USERNAME,FB_PASSWORD,ACCUWEATHER_API_KEY
from params import RAIN_THRESHOLD,SNOW_THRESHOLD,UPDATE_INTERVAL_HR,DELAY_TIME_HR,LOCATION_ID

```

Import required modules.

```py
#import required modules
import urllib
import urllib.parse
import json
import time
import requests
import pandas as pd
import logging
import sys
from fbchat import Client
from fbchat.models import *
from datetime import datetime
```

Define ‘url_page’ to be requested, in this example, we will retrieve 12-hour hourly forecast. Convert our update/delay time into seconds.

```py
url_page = "http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/"+str(LOCATION_ID)+"?apikey="+ACCUWEATHER_API_KEY+"&details=true&metric=true"
#convert hours to seconds
update_interval_sec = 60*60*UPDATE_INTERVAL_HR 
delay_time_sec = 60*60*DELAY_TIME_HR 
```

Then, request the data and put in pandas DataFrame called ‘json_df’.

At this point, we can inspect the retrieved table. Extract and rename the elements that we need. In this example, we will need AccuWeather link, % rain, % snow, date, and time in the desired format.

```py
    json_page = urllib.request.urlopen(url_page)
    json_data = json.loads(json_page.read().decode())
    json_df = pd.DataFrame(json_data)
    
    # set maximum width, so the links are fully shown and clickable
    pd.set_option('display.max_colwidth', -1)
    json_df['Links'] = json_df['MobileLink'].apply(lambda x: '<a href='+x+'>Link</a>')
    
    json_df['Real Feel (degC)'] = json_df['RealFeelTemperature'].apply(lambda x: x.get('Value'))
    json_df['Weather'] = json_df['IconPhrase'] 
    json_df['Percent_Rain'] = json_df['RainProbability'] 
    json_df['Percent_Snow'] = json_df['SnowProbability'] 
```

If we look closely, the ‘DateTime’ column is a bit tricky to extract and needs some work. After clean up, save it in ‘current_retrieved_datetime’ variable.

```py
json_df[['Date','Time']] = json_df['DateTime'].str.split('T', expand=True)
# trim the time to hh:mm format, change to str
json_df[['Time']] = json_df['Time'].str.split('+', expand=True)[0].astype(str).str[:5]

current_retrieved_datetime = str(json_df['Date'][0])+' '+str(json_df['Time'][0])
```

Next, write an if-else condition to customize the alert message. The retrieved table provides us a 12-hr forecast. We will check each element of both the rain and snow columns and return a message if the probability is above the threshold.

First, initialize the alert message for each case.

```py
rain_msg=""
snow_msg=""
```

Check ‘Percent_Rain’ and ‘ Percent_Snow’ columns, flag with 1 if the % probability is above threshold (or 0 otherwise).

Sum the columns and modify the ‘rain_msg’ and ‘snow_msg’.

```py
    # check % Rain column, return rain_msg
    json_df.loc[json_df['Percent_Rain'] >= RAIN_THRESHOLD, 'Rain_Alert'] = 1  
    json_df.loc[json_df['Percent_Rain'] < RAIN_THRESHOLD, 'Rain_Alert'] = 0
    if (sum(json_df['Rain_Alert']) > 0):
        rain_msg = 'There is ' \
                    +str(json_df['Percent_Rain'][json_df['Rain_Alert']==1][0]) \
                    +' % chance of rain' \
                    +' at ' \
                    +str(json_df['Time'][json_df['Rain_Alert']==1][0])
    
    # check % Snow column
    json_df.loc[json_df['Percent_Snow'] >= SNOW_THRESHOLD, 'Snow_Alert'] = 1  
    json_df.loc[json_df['Percent_Snow'] < SNOW_THRESHOLD, 'Snow_Alert'] = 0
    if (sum(json_df['Snow_Alert']) > 0):
        snow_msg = 'There is ' \
                    +str(json_df['Percent_Snow'][json_df['Percent_Snow']==1][0]) \
                    +' % chance of snow' \
                    +' at ' \
                    +str(json_df['Time'][json_df['Percent_Snow']==1][0])
```

Initialize ‘alert_msg’, modify the messages if there is any ‘rain_msg’ or ‘snow_msg’.

```py
alert_msg =""
if(len(rain_msg)|len(snow_msg)!=0):
     alert_msg = rain_msg +" "+snow_msg
```

Add the link to variable ‘ link_for_click’ this will be attached to the message when we send later on.

```py
link_for_click = json_df['MobileLink'][0]
```

Up until this point, we can now wrap them into a function. Don’t worry if you get lost, I have put them together below.

```py
def func_get_weather(url_page):

    json_page = urllib.request.urlopen(url_page)
    json_data = json.loads(json_page.read().decode())
    json_df = pd.DataFrame(json_data)
    
    # set maximum width, so the links are fully shown and clickable
    pd.set_option('display.max_colwidth', -1)
    json_df['Links'] = json_df['MobileLink'].apply(lambda x: '<a href='+x+'>Link</a>')
    
    json_df['Real Feel (degC)'] = json_df['RealFeelTemperature'].apply(lambda x: x.get('Value'))
    json_df['Weather'] = json_df['IconPhrase'] 
    json_df['Percent_Rain'] = json_df['RainProbability'] 
    json_df['Percent_Snow'] = json_df['SnowProbability'] 
    json_df[['Date','Time']] = json_df['DateTime'].str.split('T', expand=True)
    # trim the time to hh:mm format, change to str
    json_df[['Time']] = json_df['Time'].str.split('+', expand=True)[0].astype(str).str[:5]
    
    current_retrieved_datetime = str(json_df['Date'][0])+' '+str(json_df['Time'][0])
    
    rain_msg=""
    snow_msg=""
    
    # check % Rain column, return rain_msg
    json_df.loc[json_df['Percent_Rain'] >= RAIN_THRESHOLD, 'Rain_Alert'] = 1  
    json_df.loc[json_df['Percent_Rain'] < RAIN_THRESHOLD, 'Rain_Alert'] = 0
    if (sum(json_df['Rain_Alert']) > 0):
        rain_msg = 'There is ' \
                    +str(json_df['Percent_Rain'][json_df['Rain_Alert']==1][0]) \
                    +' % chance of rain' \
                    +' at ' \
                    +str(json_df['Time'][json_df['Rain_Alert']==1][0])
    
    # check % Snow column
    json_df.loc[json_df['Percent_Snow'] >= SNOW_THRESHOLD, 'Snow_Alert'] = 1  
    json_df.loc[json_df['Percent_Snow'] < SNOW_THRESHOLD, 'Snow_Alert'] = 0
    if (sum(json_df['Snow_Alert']) > 0):
        snow_msg = 'There is ' \
                    +str(json_df['Percent_Snow'][json_df['Percent_Snow']==1][0]) \
                    +' % chance of snow' \
                    +' at ' \
                    +str(json_df['Time'][json_df['Percent_Snow']==1][0])

    alert_msg =""
    if(len(rain_msg)|len(snow_msg)!=0):
         alert_msg = rain_msg +" "+snow_msg
    
    link_for_click = json_df['MobileLink'][0]
    
    return(current_retrieved_datetime,alert_msg,link_for_click)
```

#### 4. Automated loop

Finally, for the last part, we will automate the process by using loops. The scripts below are putting the number of loops as ‘num_repeat = 999’.

```py
num_repeat = 999 # number of loops to repeat
previous_alert_msg = "" # initialize alert msg
```

Use try and except to overcome errors (just in case something goes wrong with connections). Call ‘func_get_weather’ function and assign to variables.

```py
for i in range(num_repeat):
    try:
        current_retrieved_datetime,alert_msg,link_for_click = func_get_weather(url_page)
    except (RuntimeError, TypeError, NameError, ValueError, urllib.error.URLError):
        print('error catched')
```

Then, check if there are any changes in the weather. If nothing has changed, print the message to the screen. No chat message will be sent.

```py
    #if the weather forecast has not changed, no alert msg will be sent
    if len(alert_msg) > 0 and previous_alert_msg == alert_msg:
        print(i, current_retrieved_datetime, 'no changes in weather forecast')
```

The message will be sent only if there is any change in the weather.

We can finalize our message at this point. Fetch your user id of your friends and store in ‘friend_list’. Loop to send the message to each friend one-by-one. We put sleep time = 2 seconds between each message and logout after finish.

```py
    if len(alert_msg) > 0 and previous_alert_msg != alert_msg:    
        # login and send facebook msg 
        client = Client(FB_USERNAME,FB_PASSWORD)
        users = client.fetchAllUsers()
        friend_list=[user.uid for user in users if user.uid!="0"]
        # loop though all friends
        for id in friend_list: 
            client.send(Message(text=current_retrieved_datetime+' '+'12-hr Weather Forecast' +' '+ alert_msg +' '+link_for_click),thread_id=id, thread_type=ThreadType.USER)
            #sleep for 2 secs between each msg
            time.sleep(2) 
        #logout after sent
        client.logout()   
```

Execute delay time for the next message. Already defined in [params.py](https://github.com/ekapope/Weather_Alert_Notification_Facebook_Chat/blob/master/scripts/params.py) file — in this case, it is 4 hours. And another one for AccuWeather request delay is 1 hour.

```py
    time.sleep(delay_time_sec)                         
time.sleep(update_interval_sec)
```

Again, don’t worry if you get lost. I have put the complete loop together below.

```py
# Execute functions, retrieve data and send facebook msg
num_repeat = 999 # number of loops to repeat
previous_alert_msg = "" # initialize alert msg
for i in range(num_repeat):
    
    try:
        current_retrieved_datetime,alert_msg,link_for_click = func_get_weather(url_page)
    except (RuntimeError, TypeError, NameError, ValueError, urllib.error.URLError):
        print('error catched')

    #if the weather forecast has not changed, no alert msg will be sent
    if len(alert_msg) > 0 and previous_alert_msg == alert_msg:
        print(i, current_retrieved_datetime, 'no changes in weather forecast')
    #if there is any changes in weather       
    if len(alert_msg) > 0 and previous_alert_msg != alert_msg:    
        # login and send facebook msg 
        client = Client(FB_USERNAME,FB_PASSWORD)
        users = client.fetchAllUsers()
        friend_list=[user.uid for user in users if user.uid!="0"]
        # loop though all friends
        for id in friend_list: 
            client.send(Message(text=current_retrieved_datetime+' '+'12-hr Weather Forecast' +' '+ alert_msg +' '+link_for_click),thread_id=id, thread_type=ThreadType.USER)
            #sleep for 2 secs between each msg
            time.sleep(2) 
        #logout after sent
        client.logout()    
        time.sleep(delay_time_sec)                         
    time.sleep(update_interval_sec)
print(current_retrieved_datetime,'Run Completed')
```

Ta-da! After all our hard work, here is a snapshot of the message we will get.

![Image](https://cdn-media-1.freecodecamp.org/images/1*34jxVzSyVzO86-OKGlzVHw.png)
_Facebook chatbox msg. The location id in this example is 135564._

In case we need to know more detail, we can directly click on the link. It will navigate to the AccuWeather mobile website.

![Image](https://cdn-media-1.freecodecamp.org/images/1*sZ6uWgjnGDF1rVBoKy44Ng.png)
_AccuWeather Link_

The completed script for this how-to is also [documented on GitHub](https://github.com/ekapope/Weather_Alert_Notification_Facebook_Chat).

Thank you for reading. Please give it a try, have fun and let me know your feedback!

If you like what I did, consider following me on [GitHub](https://ekapope.github.io/), [Medium](https://medium.com/@ekapope.v), and [Twitter](https://twitter.com/EkapopeV). Make sure [to star it on GitHub](https://github.com/Ekapope) :D

