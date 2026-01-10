---
title: Have you had “The Talk” with your chatbot about graph data structures?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-19T00:28:53.000Z'
originalURL: https://freecodecamp.org/news/have-you-had-the-talk-with-your-chatbot-about-graph-data-structures-3aaf5c3ae52c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*AeUDHuLM_pyfNZ3ZP5znyQ.png
tags:
- name: '#chatbots'
  slug: chatbots
- name: graph database
  slug: graph-database
- name: IBM Watson
  slug: ibm-watson
- name: Recommendation System
  slug: recommendation-system
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Mark Watson

  A coming-of-age story for your database model


  _Image credit: [Charlotte Parent](http://www.charlotteparent.com/CLT/Health-Development/More-Than-the-Birds-and-the-Bees-Teaching-Your-Child-About-Healthy-Sexuality/"
  rel="noopener" target...'
---

By Mark Watson

#### A coming-of-age story for your database model

![Image](https://cdn-media-1.freecodecamp.org/images/1*AeUDHuLM_pyfNZ3ZP5znyQ.png)
_Image credit: [Charlotte Parent](http://www.charlotteparent.com/CLT/Health-Development/More-Than-the-Birds-and-the-Bees-Teaching-Your-Child-About-Healthy-Sexuality/" rel="noopener" target="_blank" title=")_

Graph databases are a great way to store conversational data. A simple [dialog](https://hackernoon.com/chatbot-architecture-496f5bf820ed#320b) [tree](https://en.wikipedia.org/wiki/Dialog_tree) can add depth to character interactions in a video game. A [knowledge](https://gigaom.com/2013/05/15/how-google-is-setting-the-new-search-standard-with-voice-and-knowledge-graph/) [graph](http://www.aclweb.org/anthology/N15-1086) can extract more meaning from dialog to better understand how user intent relates to an application’s data.

In this article, I’ll show you a basic graph model for capturing chatbot interactions and how to persist them using the [Apache TinkerPop](https://tinkerpop.apache.org/) framework. I’ll also show you some [Gremlin](http://tinkerpop.apache.org/gremlin.html) queries for adding a recommendation feature to the chatbot. The source code and setup instructions for my example “Recipe Bot” are [on GitHub](https://github.com/ibm-cds-labs/watson-recipe-bot-nodejs-graph).

### Review: Recipe Bot

The Recipe Bot is a [Slack Bot User](https://api.slack.com/bot-users) that lets people request recipes based on specified ingredients or cuisines. Previously I showed you how to add support for users to request their favorite recipes, like so:

![Image](https://cdn-media-1.freecodecamp.org/images/1*SjILWmRnPN3sSdr133pHRg.png)

The graph version of the bot has all of the same features I discussed in my [previous article on persisting metadata with JSON](https://medium.com/ibm-watson-data-lab/persisting-data-for-a-smarter-chatbot-be599480f7b2#.jvmry69xz), but with the graph version you’ll be adding recommendations.

### How it works with TinkerPop

Here is an architecture diagram of how the bot works:

![Image](https://cdn-media-1.freecodecamp.org/images/1*uGXlWtFX65TWPtvpKUkWGg.png)
_My Recipe Bot. Hey! The diagram is actually an [undirected graph](https://en.wikipedia.org/wiki/Graph_theory" rel="noopener" target="_blank" title="). Who knew?_

You’ll see that I’m using the Watson Conversation service. Watson Conversation lets me describe the flow of the conversation through the use of dialogs, and it helps me extract information and user intent from chat messages. You can code your own dialog tree and perform your own message parsing, or you can use tools like Watson Conversation or Botkit to help. Here is how the dialog tree for the Recipe Bot is modeled:

![Image](https://cdn-media-1.freecodecamp.org/images/1*qaJL5vQGKkhUCShVpiusGg.png)
_The Watson Conversation UI. Graphs are everywhere._

You can follow a conversation through the dialog tree similar to how you can follow vertices and edges in a graph (after all, [trees are graphs](https://en.wikipedia.org/wiki/Tree_(graph_theory)) too):

![Image](https://cdn-media-1.freecodecamp.org/images/1*fzxYyM3iP9Qc08yu4spt_g.png)
_It’s not much of a tree, but I’m keeping it simple, y’all._

In the simplified graph above, the Recipe Bot cares only about the progression between the major entities of the bot:

1. People
2. Ingredients
3. Cuisines
4. Recipes

### Data model & access pattern

As the conversation progresses, you store the following vertices and edges using the TinkerPop API:

1. **Person vertex:** For each person that interacts with the bot, store that person as a vertex in the graph.

```
{  "label": "person",  "type": "vertex",  "properties": {    "name": "U2JBLUPL2"  }}
```

**2. Ingredient or cuisine vertex:** When a person requests a specific ingredient or cuisine, you store that ingredient or cuisine — along with the list of recipes retrieved from [Spoonacular](https://spoonacular.com/food-api) — as a vertex.

```
{  "label": "cuisine",  "type": "vertex",  "properties": {    "name": "chinese",    "detail": "[{\"id\": 573147, \"title\": \"Kale Fried Rice\"..."  }}
```

**3. Selects edge, person → (ingredient | cuisine):** You create an edge, labelled `"selects"`, between the person and the ingredient or cuisine (that is, “person selects cuisine”). In addition, store a `"count"` property on the edge and increment its value each time the user requests the same ingredient or cuisine.

```
{  "label": "selects",  "type": "edge",  "inV": 4152,  "outV": 4224,  "properties": {    "count": 3  }}
```

4. **Recipe vertex:** When a user requests a recipe, store the recipe as a vertex.

```
{  "label": "recipe",  "type": "vertex",  "properties": {    "name": "573147",    "detail": "Ok, it takes *45* minutes to make...*",    "title": "Kale Fried Rice"  }}
```

5. **Selects edge, (ingredient | cuisine) → recipe:** You create another `"selects"` edge between the ingredient or cuisine and the recipe (that is, “cuisine selects recipe”). In addition, store a `"count"` property on the edge and increment it each time the ingredient or cuisine selects the same recipe.

```
{  "label": "selects",  "type": "edge",  "inV": 4320,  "outV": 4152,  "properties": {    "count": 22  }}
```

**6. Selects edge, person → recipe:** You create yet another `"selects"` edge directly between the person and the recipe (that is, “person selects recipe”). Store a `"count"` property on the edge and increment it each time a person requests the same recipe.

```
{  "label": "selects",  "type": "edge",  "inV": 4320,  "outV": 4224,  "properties": {    "count": 4  }}
```

**7. Has edge, recipe → (ingredient | cuisine):** Finally, create an edge, labelled `"has"`, between the recipe and the ingredient or cuisine (that is, “recipe has cuisine”). This relationship allows you to find all the ingredients and cuisines that a recipe uses. There is no count field on this edge.

```
{  "label": "has",  "type": "edge",  "inV": 4152,  "outV": 4320}
```

The graph for a single user looks something like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*h6fvJxvuKB_6EVn-w1itTg.png)
_This graph has it going on. It’s a [(weakly) connected graph](https://en.wikipedia.org/wiki/Connectivity_%28graph_theory%29#Definitions_of_components.2C_cuts_and_connectivity" rel="noopener" target="_blank" title="). There are all kinds of graphs._

So far, by using a graph database, you get the following benefits:

1. Reduce third-party API calls by caching entities.
2. Provide a more personal experience for users by harnessing metadata on their interactions.

A “more personal experience” for Recipe Bot means allowing users to request their favorite recipes. To find a user’s favorite recipes, you use the Gremlin [graph traversal](http://tinkerpop.apache.org/docs/current/reference/#traversal) language. The following Gremlin query will give you a user’s top-five favorite recipes, sorted by count:

### Adding recommendations

Since you track every user interaction with the bot as a graph, you can find popular ingredients, cuisines, or recipes requested by all users. You can use Gremlin to find popular recipes based on an ingredient or cuisine. Here’s how it works:

Let’s say, a user is looking for recipes that use onions:

![Image](https://cdn-media-1.freecodecamp.org/images/1*Yf49Io2lbpZeHrsvfyMxLA.png)

You can find popular recipes that use onions by issuing the following query. (I’ll unpack it further below—don’t worry!):

This query says, “Give me anyone, excluding the calling user, who has requested recipes more than once that have onions.” It breaks down like so:

1. Start with `"onions"`:

```
g.V().hasLabel("ingredient").has("name","onions")
```

2. Get the recipes that have `"onions"`. This API call uses the `"has"` edge coming from the recipe vertex into the ingredient vertex. Using `.in()` skips the edge and only returns the recipe vertex. (You don’t need any properties from the edge object, so there’s no reason to return it here.)

```
.in("has")
```

3. Get the users that have requested these recipes more than once. This call uses the `"selects"` edge coming from the person to the recipe:

```
.inE().has("count",gt(1)).order().by("count", decr)
```

4. Get the users, excluding the current user:

```
.outV().hasLabel("person").has("name",neq("CURRENT_USER"))
```

5. Get the full path:

```
.path()
```

This call returns an array of matching paths that looks like this:

> ingredient ← recipe ← edge ← person

You can access these recommended recipes at index 1.

When you return this recipe list to the user, the app puts the recommended recipes at the top and highlights the number of users who have previously used which recipe:

![Image](https://cdn-media-1.freecodecamp.org/images/1*HS0ft98ZPG4AezihLIHnFA.png)

### What’s Next?

Try a deployment for yourself. The [project’s README](https://github.com/ibm-cds-labs/watson-recipe-bot-nodejs-graph#watson-recipe-bot--ibm-graph) has step-by-step instructions for completing your first deployment on IBM Bluemix. There’s also a [Java port](https://github.com/ibm-cds-labs/watson-recipe-bot-java-graph) of the example app.

If you’re already using a dialog tree in your applications and want to use a graph database to persist metadata on interactions, I hope the source code in the repo above gives you some ideas on delivering more personalized experiences to your users.

And if you’ve enjoyed this article, please hit the ol’ ♥ so other Medium users might find it and dig it too. Happy coding!

