---
title: How to build a movie bot with SAP Conversational AI and NodeJS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-09T15:46:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-movie-bot-with-sap-conversational-ai-and-nodejs-5d7221b83267
coverImage: https://cdn-media-1.freecodecamp.org/images/1*a5MNUev1pIuETQ5pmMeDrw.png
tags:
- name: '#chatbots'
  slug: chatbots
- name: Machine Learning
  slug: machine-learning
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Paul Pinard

  Get movie recommendations from The Movie Database by asking your own chatbot on
  Facebook Messenger.


  By the end of this tutorial, you will be able to build a fully functional movie
  bot, able to make movie recommendations based on sever...'
---

By Paul Pinard

#### Get movie recommendations from The Movie Database by asking your own chatbot on Facebook Messenger.

![Image](https://cdn-media-1.freecodecamp.org/images/EUP4sAEVPCw2mrbMoWCdTEm-KswXPl3f5tLI)

By the end of this tutorial, you will be able to build a fully functional movie bot, able to make movie recommendations based on several criteria. We’re using [SAP Conversational AI bot building platform](https://cai.tools.sap/) ([sign up here for free](https://cai.tools.sap/signup)) and [The Movie Database](https://www.themoviedb.org/?language=en) for information on movies.

Here’s a demo chat with Movie Bot:

![Image](https://cdn-media-1.freecodecamp.org/images/O56iGQjerGE0F9WdgLGex49JxiMA3cnhG7em)

### **What are we building today?**

Interacting with third party APIs allows for much more interesting use cases than simple Q/A chatbots. With **Bot Skills**, we added the option to call **webhooks** directly from the builder, which makes it even easier.

Today’s bot requires several steps:

1. Extracting key pieces of information in a sentence
2. Building the bot flow (triggers, requirements, actions)
3. Creating and connecting a bot API able to fetch data from The Movie Database

You’ll need an [SAP Conversational AI account](https://cai.tools.sap/signup/?utm_source=blog), [Node.JS](https://nodejs.org/en/) and potentially [Ngrok](https://ngrok.com/) for testing.

_Before we jump in, [please check this guide instead](https://medium.freecodecamp.org/how-to-build-your-first-chatbot-with-the-sap-conversational-ai-9a1a2bd44e3c) if you are looking for a guide detailing the creation of your first bot._

Let’s get to it!

### Step 1: Extracting key info from a sentence

_Intents_ are helpful to determine the overall meaning of a sentence. For our use case, knowing that the user _wants to watch something_ is not enough.

We need to know _what_ the users want to watch.

_Entities_ are designed to solve this problem: they extract key information in a sentence.

Intents make you understand that you have to do something. Entities help you actually do something.

Let’s imagine you are a telco company providing phone and internet access. Your bot has an intent that understands when people are complaining about an outage:

![Image](https://cdn-media-1.freecodecamp.org/images/8hGqHmVQENpDX2v2WXeffdEftwwgtLJNpsDl)

The entities extracted will help understand _what_ is going wrong, _where_ and since _when_.

For our movie bot, we will try to extract **3 key pieces of information**:

1. What the user wants to watch (a movie vs a TV show)
2. What genre they are looking for
3. In which language

#### Using gold entities

To help you speed up your development, SAP Conversational AI extracts several entities by default: dates, locations, phone numbers…

[An exhaustive list is available here](https://cai.tools.sap/docs/concepts/gold-entities).

The `Language` entity will be helpful:

![Image](https://cdn-media-1.freecodecamp.org/images/VdVfd0K3zmwPi7ZmWNVrrFIUgIm6lFDPTXxs)
_Gold Entities — Language_

_See the little star next to the entity name? It differentiates a gold entity from a custom one._

We will use it to fulfill our third requirement: the movie language.

#### Creating custom entities

We will create custom entities to extract the information we need. As with intents, training is very important: the more examples you add to your bot, the more accurate it gets.

Training your entities can happen through multiple intents. Entities are independent of intents.

For our movie bot, we only need one intent, `discover`, and 2 entities:

* `recording` to identify that the user wants to watch a movie **or** a tv show
* `genre`

Open the intent `discover` and add expressions. Make sure to cover every possibility, this means a healthy mix of expressions with:

* No entities at all: “My boyfriend wants to watch something tonight”
* One entity: “I want to watch a movie”
* Many entities: “Can you recommend me some French drama TV shows?”

To tag your expressions, select the text you want to tag and type your entity name:

![Image](https://cdn-media-1.freecodecamp.org/images/yhKnnRD1yk6i6lIqLJMlDANVtPhOP1cJ5hcw)
_Tagging custom entities_

You should add many more examples: 15 would be nice, but a production-ready bot would require at least 50 examples to perform well. To speed up the process you can fork the entities built within [this bot](https://cai.tools.sap/pe/movie-bot-skills-training/train/intents) [[recording entity](https://cai.tools.sap/pe/movie-bot-skills-training/train/entities/recording), [genre entity](https://cai.tools.sap/pe/movie-bot-skills-training/train/entities/genre)] and then fork the [discover intent](https://cai.tools.sap/pe/movie-bot-skills-training/train/discover) from this [bot](https://cai.tools.sap/pe/movie-bot-skills-training/train/intents).

You can see here that “French” was detected as a nationality, not a language because that’s what it is in this context. When building the bot flow, we’ll make sure to check for these two entities.

#### Adding custom enrichments

Now that we have labeled have our entities we are going to enrich them! Open the entities panel from your bot under the training tab as shown below:

![Image](https://cdn-media-1.freecodecamp.org/images/gwfaUd43f6ACQBoQHuNnwQ6LC7ZFI77YEPQa)
_Entities section_

Now let’s open the `genre` entity. If you look at the top right of the panel you should see a toggle saying `free - restricted` and `settings`. Open it so we can explain in details the different options you have access to:

![Image](https://cdn-media-1.freecodecamp.org/images/Q8xVSh16bzQ488cSTcROi5V3mlSceufSLKIJ)
_Entity panel_

Within the entity panel you have access to different options for your entity:

* Free vs Restricted — A free custom entity is used when you don’t have a strict list of values and want machine learning to detect all possible values. Whereas a restricted custom entity is used if you have a strict list of words to detect and don’t need automatic detection of the entity.
* Fuzzy matching — Fuzzy matching is an index between 0 and 1 to indicate how close a word can be from the one in your entity list of values. If the word is above this index then the platform will tag it as the closest value within your list.
* List of values — This is where you can add all the list of values of your entity which could be different values or synonyms

For more in-depth information about entities, you can read our detailed [documentation](https://cai.tools.sap/docs/concepts/entity).

In our case, our `genre` entity is going to be `restricted` as theMovie Database API only manages a specific list of genres. Here is the list below:

```
[ { id: 28, name: 'Action' }, { id: 12, name: 'Adventure' }, { id: 16, name: 'Animation' }, { id: 35, name: 'Comedy' }, { id: 80, name: 'Crime' }, { id: 99, name: 'Documentary' }, { id: 18, name: 'Drama' }, { id: 10751, name: 'Family' }, { id: 14, name: 'Fantasy' }, { id: 36, name: 'History' }, { id: 27, name: 'Horror' }, { id: 10402, name: 'Music' }, { id: 9648, name: 'Mystery' }, { id: 10749, name: 'Romance' }, { id: 878, name: 'Science Fiction' }, { id: 53, name: 'Thriller' }, { id: 10752, name: 'War' }, { id: 37, name: 'Western' } ]
```

Add all the different genres to our list of values. Don’t forget to also add synonyms such as SF, Sci-Fi for Science Fiction, Romantic for Romance or Animated, Cartoon for Animation. You can fetch the list of values from [there](https://cai.tools.sap/pe/movie-bot-skills-training/train/entities/genre).

As you can see from the JSON above, there are IDs associated with the genres. The reason is that the Movie Database can’t search for a specific genre based on its English name, but rather on a custom number. We can associate for each of the genre values a specific id that will be returned within the JSON of the NLP API. We can pass it on to the Movie Database API. This is the purpose of custom enrichments. Whenever an entity is detected, the JSON returned by the NLP API is enriched with additional information about the entity.

Within the custom enrichment panel we need to create 3 keys:

* `name` – to map synonyms under the same value
* `id` – to enrich with the id of the Movie Database
* `article` – to add the article of the genre (we will use this later)

In order to add a custom enrichment click `add new key` and add the three keys listed above. For the article set the default key value to ‘a’ as most of the genres would be with ‘a’. Within name, you can start adding the specific enrichment and map it to all the different values for your `article`, `id` and `name` such as below:

![Image](https://cdn-media-1.freecodecamp.org/images/jvvvrr6uuWhE9NjDqjZFIGW8E2MHdqIT4wRx)
_Custom enrichments for name_

![Image](https://cdn-media-1.freecodecamp.org/images/uEAKe1oA85jEzP2p3yNRGAYIjVcRZPMhiw-9)
_Custom enrichments for ids_

![Image](https://cdn-media-1.freecodecamp.org/images/TflusjaW8yoiOyMm3d3IexkQGGSdCYgi6Bki)
_Custom enrichments for article_

You can fork the whole entity from this [page](https://cai.tools.sap/pe/movie-bot-skills-training/train/entities/genre) which will include the enrichment. Now that this is done, let’s test it within the test console. If you send the sentence “I want to watch an animation movie” you now should now see the following custom enrichment:

```
"genre": [      {        "value": "animated",        "raw": "animated",        "confidence": 0.99,        "name": "animation",        "id": 16,        "article": "an"      }
```

Great, now our enrichment gives us the generic name, id, and the article! Let’s do the same thing for the recording entity. Go back to the entities panel and click on recording. Then make it restricted and add all possible values and synonyms for tv show and movie (such as tv shows, shows, motion picture, film, films, movies, etc.). See the entire list [here](https://cai.tools.sap/pe/movie-bot-skills-training/train/entities/recording). Now go to custom enrichments and add the key `type` and add 2 specific values:

* `movie` – for all movies synonyms
* `tv` – for all tv shows synonyms

It should look like this:

![Image](https://cdn-media-1.freecodecamp.org/images/U-4UQBHoxtIfzoINnX8yeuQVwJ3GKNw7Kbt-)
_Custom enrichments for type_

Sending back our sentence “I want to watch an animation movie” we now also have the enrichment for recording:

```
"recording": [      {        "value": "movie",        "raw": "movie",        "confidence": 0.99,        "type": "movie"      }    ]
```

### **Step 2: Building your bot flow**

Since we just need to make sure all our criteria are filled before calling a Node.JS API, the build part will be rather simple.

We will just need one skill, let’s call it `discover`.

_You can find an example of a configured skill [here](https://cai.tools.sap/pe/movie-bot-skills-training/skills/discover)._

#### Triggers

We want to trigger this skill if the intent _@discover_ is present:

![Image](https://cdn-media-1.freecodecamp.org/images/1Xo2CXSJBFkQABHq-Ud91SyGXqziobNdWJY0)
_Message triggers_

This tab helps you collect data before moving to _Actions_. We want to make sure the user specifies a recording, a genre, a language, and a yes or no intent before moving on:

![Image](https://cdn-media-1.freecodecamp.org/images/Q4UFIR2YRkwB2CsXIIrbWN1NeVXw0wTYebvP)
_Requirements_

The requirements will be checked one by one. They can all be fulfilled on the first message. For example, if the user says _I want to watch a crime movie in English_, then the _Actions_ will be triggered immediately.

For each Requirement, you can choose to send a message if it is complete or if it is missing.

Sending messages when a requirement is complete can make your bot more lively: _A crime movie? I love them too!_, but are almost mandatory when the requirement is missing: You need to ask your users to fill what you need to know.

For example, I send quick replies with suggested genres if #genre is missing:

![Image](https://cdn-media-1.freecodecamp.org/images/4Ax7ygxJtW5VaxrrA0jTwszkrRj670W7W32j)
_Conditional message if a requirement is missing_

For the confirmation we are using the memory to display a dynamic message to validate the choice of the user using @yes and @no intent:

![Image](https://cdn-media-1.freecodecamp.org/images/nROyecbgUlEHaotWNzZEhGNF95BB3cTGqVel)
_Using the memory for dynamic message_

Once you have set up questions for the 4 groups of entities, go to the `Actions` tab.

#### Actions

Once the requirements are fulfilled, we want to call our API to actually perform the search if the user said yes. Else we reset the memory and ask again what the user wants to watch.

If `_memory.no` is present – reset the whole memory and send a message such as “Let’s start again, what do you want to watch?”

If `_memory.yes` is present create a `CALL WEHBOOK` action. You can either type a full URL (eg: `https://mydomainname.com/discover-movies`), or a relative URL (`/discover-movies`). SAP Conversational AI will use the parameter `Bot base URL` in your bot settings when you type a relative URL.

Next, add an action `UPDATE CONVERSATION > EDIT MEMORY > RESET ALL` MEMORY to empty the memory once the call has been made.

![Image](https://cdn-media-1.freecodecamp.org/images/rW-kEaNQAgLfQE5PLhMv6gpIHkQIeMFLC-2p)
_Actions_

If you **don’t have a public server**, or if you want to test your bot during development, ngrok is a very handy tool. It creates a public URL for you and forwards requests to your computer.

Once you installed it, run

```
ngrok http 5000
```

And copy the `Forwarding` URL in **HTTPS** (https://XXX.ngrok.io) to your bot Settings (“Bot webhook base URL” field). All requests made to these URL will be forwarded to the port 5000 of your computer.

All your bot needs now are its API to get your movies!

### Step 3: Creating the movie bot API

The NodeJS part of this bot is fairly simple: It will behave as an HTTP proxy between SAP Conversational AI and The Movie Database.

When your application receives a request from SAP Conversational AI, it sends a search query to the Movie Database with the criteria of your user and formats the JSON answer to the SAP Conversational AI message format.

![Image](https://cdn-media-1.freecodecamp.org/images/s1HGCz1C-dk350aA4t0dRyDQJPGgQPNb1dAT)
_Bot API diagram_

#### Option 1: the automatic way

You can clone the entire project directly from our Git repository: [https://github.com/plieb/movie-bot-skills-training](https://github.com/plieb/movie-bot-skills-training)

#### Option 2: the manual way

**Step 1 — scaffolding your project**

```
mkdir movie-bot && cd movie-botnpm initnpm install --save express body-parser axiostouch index.js config.jsmkdir discover-movies && cd discover-moviestouch index.js movieApi.jscd..
```

**Step 2— getting a TMDb API token**

You will need a token to use the Movie Database API, [go here to generate one](https://developers.themoviedb.org/3), and edit your `config.js` file:

```
module.exports = { MOVIEDB_TOKEN: process.env.MOVIEDB_TOKEN || 'PURYOURTOKENHERE', PORT: process.env.PORT || 5000, };
```

**Step 3 — filling your index.js with an Express application**  
   
Let’s create an Express application to handle the requests from SAP Conversational AI. To better organize our project, as seen in Step 1, we have a folder `/discover-movies/` which contains the core of our bot code (instead of putting all our files in the same folder), and we call it through `loadMovieRoute`.

```
const express = require('express');const bodyParser = require('body-parser');const config = require('./config');const loadMovieRoute = require('./discover-movies');const app = express();app.use(bodyParser.json());loadMovieRoute(app);app.post('/errors', function(req, res) {  console.log(req.body);  res.sendStatus(200);});const port = config.PORT;app.listen(port, function() {  console.log(`App is listening on port ${port}`);});
```

**Step 4 — filling discover-movies/index.js**

We ask SAP Conversational AI to send a POST request to `/discover-movies` when a user has filled his search criteria.

The main goal of our controller is to pick and format the preferences from the memory to send them to the Movie Database’s API:

```
const config = require('../config'); const { discoverMovie } = require('./movieApi'); function loadMovieRoute(app) { app.post('/discover-movies', function(req, res) { console.log('[GET] /discover-movies'); const kind = req.body.conversation.memory['recording'].type; const genre = req.body.conversation.memory['genre'].id; const language = req.body.conversation.memory['language']; const nationality = req.body.conversation.memory['nationality']; const isoCode = language ? language.short.toLowerCase() : nationality.short.toLowerCase(); return discoverMovie(kind, genreId, isoCode) .then(function(carouselle) { res.json({ replies: carouselle, conversation: { } }); }) .catch(function(err) { console.error('movieApi::discoverMovie error: ', err); }); }); } module.exports = loadMovieRoute;
```

**Step 5— filling discover-movies/movieApi.js**

Now that we have extracted and formatted all the filters of the request, we need to send the request to the Movie Database and format the answer:

```
const axios = require('axios');const config = require('../config');function discoverMovie(kind, genreId, language) {  return moviedbApiCall(kind, genreId, language).then(response =>    apiResultToCarousselle(response.data.results)  );}function moviedbApiCall(kind, genreId, language) {  return axios.get(`https://api.themoviedb.org/3/discover/${kind}`, {    params: {      api_key: config.MOVIEDB_TOKEN,      sort_by: 'popularity.desc',      include_adult: false,      with_genres: genreId,      with_original_language: language,    },  });}function apiResultToCarousselle(results) {  if (results.length === 0) {    return [      {        type: 'quickReplies',        content: {          title: 'Sorry, but I could not find any results for your request :(',          buttons: [{ title: 'Start over', value: 'Start over' }],        },      },    ];  }  const cards = results.slice(0, 10).map(e => ({    title: e.title || e.name,    subtitle: e.overview,    imageUrl: `https://image.tmdb.org/t/p/w600_and_h900_bestv2${e.poster_path}`,    buttons: [      {        type: 'web_url',        value: `https://www.themoviedb.org/movie/${e.id}`,        title: 'View More',      },    ],  }));  return [    {      type: 'text',      content: "Here's what I found for you!",    },    { type: 'carousel', content: cards },  ];}module.exports = {  discoverMovie,};
```

**Step 6 — Start the engine!**

That’s all! You’re ready to test your bot.

Start your application by running: `node index.js`

All being well, you should see: `App started on port 5000`

Movie recommendations, weather, health, traffic… With third-party APIs, everything is possible! Now that you’re familiar with the workflow, we can’t wait to hear from you about what you’re building! And remember, you’re very welcome to contact us if you need help, trough the comment section below or via [Slack](https://slack.cai.tools.sap/).

_Originally published on [SAP Conversational AI blog](https://cai.tools.sap/blog/nodejs-chatbot-movie-bot/)._

