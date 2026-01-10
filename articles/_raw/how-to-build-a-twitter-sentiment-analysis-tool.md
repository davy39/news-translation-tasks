---
title: How to Build a Twitter Sentiment Analysis Tool
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-04T23:52:05.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-twitter-sentiment-analysis-tool
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b3f740569d1a4ca2aa8.jpg
tags:
- name: nlp
  slug: nlp
- name: Node.js
  slug: nodejs
- name: Sentiment analysis
  slug: sentiment-analysis
seo_title: null
seo_desc: 'By Dirk Hoekstra

  This weekend I had some time on my hands and decided to build a Twitter sentiment
  analysis tool.

  The idea is that you enter a search term and the tool will search recent tweets.
  It will then use sentiment analysis to determine how po...'
---

By Dirk Hoekstra

This weekend I had some time on my hands and decided to build a Twitter sentiment analysis tool.

The idea is that you enter a search term and the tool will search recent tweets. It will then use sentiment analysis to determine how positive or negative Twitter is about the subject.

For example, you could search "Donald Trump" to get Twitter's sentiment on the president.

Let's dive in!

## Getting a Twitter API key

The very first thing we need to do is create a Twitter application in order to get an API key. 

Head over to the [Twitter apps page](https://developer.twitter.com/en/apps) to create a new application. You must have a developer account to be able to create an application.

If you don't have a developer account you can apply for one. Most requests are granted instantly. ?

Copy down the `API Key` and `API Key Secret` that you find in your Twitter application.

## Creating a NodeJS project

I'm going to use NodeJS to create this application. 

To create a new project I run:

```
npm init
npm install twitter-lite
```

This will create a new NodeJS project and install the `twitter-lite` package. This package makes interacting with the Twitter API super easy.

To authenticate our requests we are going to use an OAuth2.0 bearer token. The `twitter-lite` package has an easy way of handling the Twitter authentication.

Let's create a new `index.js` file and add the following code to it:

```javascript
const Twitter = require('twitter-lite');

const user = new Twitter({
    consumer_key: "YOUR_API_KEY",
    consumer_secret: "YOUR_API_SECRET",
});

// Wrap the following code in an async function that is called
// immediately so that we can use "await" statements.
(async function() {
    try {
        // Retrieve the bearer token from twitter.
        const response = await user.getBearerToken();
        console.log(`Got the following Bearer token from Twitter: ${response.access_token}`);
        
        // Construct our API client with the bearer token.
        const app = new Twitter({
            bearer_token: response.access_token,
        });
    } catch(e) {
        console.log("There was an error calling the Twitter API.");
        console.dir(e);
    }
})();
```

When running this the console outputs the following:

```
Got the following Bearer token from Twitter: THE_TWITTER_BEARER_TOKEN
```

Awesome, so far everything works. ?

## Getting recent tweets

The next part is retrieving recent tweets from the Twitter API.

On the [Twitter documentation](https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets) you can see that there is an endpoint to search for recent tweets. 

To implement this I add the following code to the `index.js` file:

```javascript
const Twitter = require('twitter-lite');

(async function() {
    const user = new Twitter({
        consumer_key: "YOUR_API_KEY",
        consumer_secret: "YOUR_API_SECRET",
    });

    try {
        let response = await user.getBearerToken();
        const app = new Twitter({
            bearer_token: response.access_token,
        });

        // Search for recent tweets from the twitter API
        response = await app.get(`/search/tweets`, {
            q: "Lionel Messi", // The search term
            lang: "en",        // Let's only get English tweets
            count: 100,        // Limit the results to 100 tweets
        });

        // Loop over all the tweets and print the text
        for (tweet of response.statuses) {
            console.dir(tweet.text);
        }
    } catch(e) {
        console.log("There was an error calling the Twitter API");
        console.dir(e);
    }
})();
```

When running this you can see a lot of twitter comments about Lionel Messi, meaning that it works perfectly! ⚽

```
"RT @TheFutbolPage: Some of Lionel Messi's best dribbles."

"RT @MagufuliMugabe: Lionel Messi ? didn't just wake up one day  and become the best player in the world no  HE trained. So if your girl is…"

""RT @goal: The boy who would be King ? Is Ansu Fati the heir to Lionel Messi's throne?"

and many more... 
```

## Performing sentiment analysis

To perform the sentiment analysis I'm going to use Google Cloud's Natural Language API. With this API you can get the sentiment score of a text with a simple API call.

First, head over to the [Google Cloud Console](https://console.cloud.google.com/) to create a new cloud project.

Next, head over to the [Natural Language API](https://console.cloud.google.com/apis/api/language.googleapis.com) and enable it for the project.

Finally, we need to create a service account to authenticate ourselves. Head over to the [create a service account page](https://console.cloud.google.com/apis/credentials/serviceaccountkey) to create a service account. 

When creating a service account you will need to download the `json` file containing the private key of that service account. Store this file in the project folder.

Google has a NodeJS package to interact with the Natural Language API so let's use that. To install it run:

```
npm install @google-cloud/language
```

In order for the language package to work, it needs to know where the private key file is. 

The package will attempt to read a `GOOGLE_APPLICATION_CREDENTIALS` environment variable that should point to this file.

To set this environment variable I update the `script` key in the `package.json` file.

```json
"scripts": {
  "start": "GOOGLE_APPLICATION_CREDENTIALS='./gcloud-private-key.json' node index.js"
}
```

_Note that in order for this to work you must start the script by running `npm run start`._

With all that set up we can finally start coding.

I add a new `getSentiment` function to the `index.js` file:

```javascript
const language = require('@google-cloud/language');
const languageClient = new language.LanguageServiceClient();

async function getSentiment(text) {
    const document = {
        content: text,
        type: 'PLAIN_TEXT',
    };

    // Detects the sentiment of the text
    const [result] = await languageClient.analyzeSentiment({document: document});
    const sentiment = result.documentSentiment;

    return sentiment.score;
}
```

This function calls the Google Natural Language API and returns a sentiment score between -1 and 1.

Let's test it out with a few examples:

```javascript
getSentiment("I HATE MESSI");
```

Returns the following.

```
The sentiment score is -0.40
```

Similarly:

```javascript
getSentiment("I LOVE MESSI");
```

Returns a higher sentiment. ?

```
The sentiment score is 0.89
```

## Bringing it all together

The final thing to do is calling the `getSetiment` function with the text from the tweets.

There is a catch though: only the first 5,000 API requests are free, after that Google will charge you for subsequent API requests. 

To minimise the amount of API calls I'm going to combine all the tweets into one single string like so:

```javascript
let allTweets = "";
for (tweet of response.statuses) {
	allTweets += tweet.text + "\n";
}

const sentimentScore = await getSentimentScore(allTweets);
console.log(`The sentiment about ${query} is: ${sentimentScore}`);
```

Now I only have to call the API once instead of 100 times.

The final question is of course: what does Twitter think about Lionel Messi? When running the program it gives the following output:

```
The sentiment about Lionel Messi is: 0.2
```

So, Twitter is lightly positive about Lionel Messi.

## Conclusion

We've created a NodeJS program that interacts with the Twitter API to get recent tweets. It then sends these tweets to the Google Cloud Natural Language API to perform a sentiment analysis.

You can find a live version of this [sentiment analysis here](https://coffeecoding.dev/twitter-sentiment-analysis).

You can also view the completed code [here on Github](https://github.com/Dirk94/twitter-sentiment-analysis).

