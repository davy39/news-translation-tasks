---
title: How to delete your past tweets — in bulk and for free — and save your career
  from your past self
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2018-07-22T14:24:22.000Z'
originalURL: https://freecodecamp.org/news/how-to-delete-your-past-tweets-in-bulk-and-for-free-save-yourself-from-your-past-self-f8844cdbda2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*JU7deLCU5l54IDbLwO5M2A.jpeg
tags: []
seo_title: null
seo_desc: '“He who controls the past controls the future. He who controls the present
  controls the past.” — George Orwell


  James Gunn was on top of the world. He’d just directed two of the best action-comedy
  movies of the past decade. Both of his Guardians of t...'
---

> “He who **controls the past controls the future**. He who **controls** the present **controls the past**.” — George Orwell

James Gunn was on top of the world. He’d just directed two of the best action-comedy movies of the past decade. Both of his Guardians of the Galaxy movies were well-received by critics and audiences alike.

![Image](https://cdn-media-1.freecodecamp.org/images/-r3W9nzAsguP1bt89slbASRnkhBJVVm33O3Z)

But that wasn’t enough to save him from his past self.

It turns out that earlier in his career Gunn had tweeted some rather shocking “jokes” on Twitter. (I won’t share them here — you’re probably better off not reading them.)

Back then, Gunn was an obscure budget horror movie maker. And the tweets in question lie dormant for years in his Twitter history, with nobody reading them or caring.

That is, until a few reporters decided to dig up dirt on him, and unearthed the tweets for all the world to see.

His bosses at Disney immediately decided to “sever their business relationship” with Gunn.

So within the span of a few hours, Gunn went from star director to Hollywood pariah. All because of a few tweets from 2012.

### Control your past

In this tutorial, I’m going to show you how you can download all your old tweets from Twitter, then quickly delete as many of those tweets as you want — all without sharing any of your data with anyone.

I did this myself a few minutes ago.

Sure, I like the idea of future historians scrutinizing my Tweets asking: “What was Quincy Larson really like?” But not as much as I dislike the idea of some hater digging through my Twitter feed and cherry picking a tweet where I sounded like a jerk.

There are a lot of services you can find that will delete your tweets for you if you give them access to your Twitter account (and maybe some money, too).

I didn’t feel comfortable sharing access to my Twitter accounts with any of those services. In fact, creating such a “tweet deleting” service jumped out at me as a evil genius kind of thing to do. “Oh, you have something to hide, do you?”

But we can leave such dirty work to the digital paparazzi.

Instead, this tutorial will show you how to delete all your tweets from before a certain date yourself — for free and in bulk — using a simple Python script.

It may feel like every tweet from your past is a special and unique snowflake. If you feel this way, you may want to instead manually go through your old tweets and just delete the old tweets that embarrass you.

But if you have thousands of tweets like I do, that’s going to take you hours and hours.

Note that deleting old tweets will not affect your Twitter followers at all, other than to remove some stuff they are frankly too busy to go back and ever read. (There are 350,000 new tweets created every minute on Twitter. Ain’t nobody got time for that!)

Let’s get started!

### Step 1: How to create a personal backup of all your tweets

The first thing you need to do is create a backup of all your tweets. Twitter allows you to easily export all of your past tweets into a convenient CSV file.

Navigate to Twitter’s “Your Twitter Data” section in their settings. [Here’s a direct link](https://twitter.com/settings/your_twitter_data).

Twitter will ask you to confirm your password. Then click “request data” at the bottom of the page.

![Image](https://cdn-media-1.freecodecamp.org/images/bTEKJOohOMH0klHEMP7z0AkJ228foEx7HE8H)

Twitter emailed me a nice zip file within a few minutes.

If you think you’ll ever want to read the old tweets you’re about to delete, be sure to backup this zip file some safe.

Then unzip the folder. Here’s what the folder looks like:

![Image](https://cdn-media-1.freecodecamp.org/images/PVuZ9EvjKXsD0Mywm2MeiT8GxnsWSVAsObA6)

You can open up index.html in a browser and you’ll see a nice user interface where you can scroll through your tweets by month and year.

Note that you’ll need the `tweets.csv` file for the final step of this tutorial.

### Step 2: Install the Python library

For this step, I’m going to assume you’re using a MacOS. If someone wants to create a clear list of step-by-step Linux or Windows instructions for this step, share them in a comment below. I’ll add them here and credit you. ?

Go into your command line and run this command to clone the repository:

```
git clone git@github.com:QuincyLarson/delete-tweets.git
```

Go into the newly-created directory:

```
cd delete-tweets
```

Make sure you have PIP (a Python package manager) installed:

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```

Now you can install all the library’s dependencies:

```
pip install -r requirements.txt
```

Note that you may have to run some of these commands with “sudo” at the beginning to get them work properly. And you may get some “can’t find xyz library” messages. I was able to ignore those messages and still get this to work.

### Step 3: Create Twitter API keys

Go to [https://apps.twitter.com/app/new](https://apps.twitter.com/app/new) and fill out the form like so:

![Image](https://cdn-media-1.freecodecamp.org/images/a1gWcgtupB6bBxWNkZKHtSmsfKf1jIO450ps)

You can put basically anything here — the only person who’s going to use this Twitter app is you.

Now in your newly created Twitter app, click “Keys and Access Tokens” and then at the bottom, click “Create my access token”.

![Image](https://cdn-media-1.freecodecamp.org/images/-A2x3QqJ6RcjUIO2jOHHp0i6ZJgWQkYqgTQ8)

Now use your trusty text editor of choice and open up `deletetweets.py.`

![Image](https://cdn-media-1.freecodecamp.org/images/1irYIAk3F7SIZUeaPRjK7oAcpDHNkScvFA1H)

Scroll down to line 54. You are going to manually copy/paste your keys over to here.

![Image](https://cdn-media-1.freecodecamp.org/images/BdmnWKyZYJwMXfno0NVbjLEUjQ5vtaqeYjZK)

Save the file and exit.

### Step 4: Copy your tweets.csv file over

In step 1 you downloaded an personal backup of all your past tweets. Copy the `tweets.csv` file from that folder over to your new delete-tweets folder. It will replace the placeholder tweets.csv file.

### Step 4: Delete the tweets

Now you just need to decide on a “cut-off date” — a date before which all of your tweets will be deleted.

For example, if that date was October 1, 2013 then you’d use the following command in your terminal:

```
python deletetweets.py -d 2013-10-01
```

The script will then start with that date and go in reverse chronological order, deleting one tweet each second until it’s done.

![Image](https://cdn-media-1.freecodecamp.org/images/UG4b1mVeLdcsDRrgOSZSKC1vdHXLglID3F4x)

At the end, it will tell you how many tweets it deleted.

Congratulations — you have controlled your past.

And now you have one less thing to worry about in the future.

Now close your terminal and get on with your life.

You should [follow me on Twitter](https://www.twitter.com/ossia) for practical tech stuff that’s worth your time.

