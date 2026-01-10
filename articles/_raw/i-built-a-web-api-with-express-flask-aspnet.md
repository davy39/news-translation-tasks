---
title: I rebuilt the same web API using Express, Flask, and ASP.NET. Here's what I
  found.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-29T19:00:00.000Z'
originalURL: https://freecodecamp.org/news/i-built-a-web-api-with-express-flask-aspnet
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c5c740569d1a4ca31ac.jpg
tags:
- name: Aspnetcore
  slug: aspnetcore
- name: 'Back end development '
  slug: back-end-development
- name: backend
  slug: backend
- name: Backend Development
  slug: backend-development
- name: C#
  slug: csharp
- name: Express
  slug: express
- name: Flask Framework
  slug: flask
- name: full stack
  slug: full-stack
- name: JavaScript
  slug: javascript
- name: Python
  slug: python
- name: REST API
  slug: rest-api
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "By M. S. Farzan\nI've been shopping around for a back end framework to\
  \ support a tabletop game app, and decided to do some research to determine the\
  \ best fit for my needs. \nThe objective was straightforward: to build a simple\
  \ RESTful API that would al..."
---

By M. S. Farzan

I've been shopping around for a back end framework to support a [tabletop game app](https://www.nightpathpub.com/entromancy), and decided to do some research to determine the best fit for my needs. 

The objective was straightforward: to build a simple [RESTful API](https://restfulapi.net/) that would allow a front end app to perform basic [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) operations, providing me with an introduction to what the development process would look like.

There are a lot of back end framework options out there, and I'm most familiar with JavaScript, C#, and Python (in that order), which limited my options somewhat.  The natural starting point was to build a simple front end that would send requests to an API, which would in turn read from and write to a local database.

I began my development process with Express, which, for reasons I'll soon explain, led me to also check out Flask and ASP.NET. I thought my findings might prove useful to others out there who are researching back end frameworks for small projects. In this article, I'll also provide code examples and the resources that I used to build everything.

You can access the full code on [GitHub](https://github.com/sominator/web-api-project), as well.

I should caveat that I won't be promoting one framework over another, and haven't yet compared things like deployment, authentication, or scalability.  Your mileage may vary if those particulars are important to you!

I will, however, provide a **TL;DR** at the bottom if you just want to get the summary and key learnings.

Here we go!

## Defining the API

If you're new to web development, you might be asking, "what's an API?"

I've had to ask the question a hundred times to find an answer that made sense. And it really wasn't until I built my own that I could say I understood what an API _does_.

Put simply, an API, or "application programming interface", allows two different computing systems to talk to one another. In this article, I'll show a simple front end app that displays a "quest" tracker that players can view for their tabletop roleplaying game. Each quest has a "name" and a "description," both of which are displayed in the web browser.

If I already had all of the quests listed on the website and just wanted players to view them, I would have no need for an API or back end. For this project, however, I want the ability to allow users to add quests, search for them, delete them, and so on. For those operations, I need to store the quests somewhere, but my front end app isn't able to transfer information directly to a database.

For that, I need an API that can receive HTTP requests from the website, figure out what to do with those requests, interact with my database, and send more information back up the chain so that the user can see what happened.

The whole thing - the front end "client", the back end "API" or server, and the database - is called a "stack," or more precisely, the "full stack." For this project, I built a simple front end website as the top of the stack, and switched out everything beneath it as I tried out different frameworks and databases.

## Project Structure

The structure for this project was fairly simple, with the front end client separated from three different servers that I would spin up as necessary to serve the API.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Project-Structure.PNG)

I used [Visual Studio Community](https://visualstudio.microsoft.com/vs/community/) as my code editor and IDE, with the requisite language packages installed for JavaScript, Python, and C#.

I'll provide an overview of my experience with each framework in turn, with links to the tutorials and packages that I used to get them to work with the client. But first, let's take a look at the front end!

## The Client: Vue.js

The goal for the client was to have a simple website that would receive information from the database through the API and display it to the user. To streamline the process, my requirements were that the client would only need to "read" all of the items in the database, and provide the user with the ability to "create" a new quest.  

These "read" and "create" operations - the "R" and "C" in "CRUD" - are analogous to the HTTP methods of "GET" and "POST," which we'll see in the code below.

In front end development, I'm most comfortable using [Vue](https://vuejs.org/), and used the [Vue CLI](https://cli.vuejs.org/) to scaffold a basic client, with the following file structure:   

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Client-Structure.PNG)

I replaced the boilerplate markup provided by the Vue CLI with the following:

```html
<template>
    <div id="app">
        <h1>RPG Quests</h1>
        <p v-for="(quest, index) in quests" v-bind:key="index">{{quest.name}}: {{quest.description}}</p>
        <input type="text" v-model="newQuestName" placeholder="Quest Name" /> <br />
        <input type="text" v-model="newQuestDescription" placeholder="Quest Description" /><br /><br />
        <button v-on:click="postQuest">Add Quest</button>
    </div>
</template>
```

And the corresponding Vue code:

```javascript
import axios from 'axios';

    export default {
        name: 'App',
        data: function () {
            return {
                quests: null,
                newQuestName: null,
                newQuestDescription: null
            }
        },
        methods: {
            getQuests: function () {
                axios
                    .get('http://localhost:3000/quests')
                    .then(response => (this.quests = response.data));
            },
            addQuest: function () {
                axios
                    .post('http://localhost:3000/quests', {
                        name: this.newQuestName,
                        description: this.newQuestDescription
                    });
            },
            postQuest: function () {
                axios.all([this.addQuest(), this.getQuests()]);
                this.$forceUpdate();
            }
        },
        mounted: function () {
            this.getQuests();
        }
    }
```

If you're not familiar with Vue, the specifics of the front end aren't that important! Of significance here is that I'm using a JavaScript package called [Axios](https://github.com/axios/axios) to make my GET and POST requests to a potential server. 

When the client loads, it'll make a GET request to the URL http://localhost:3000/quests to load all quests from the database. It also provides a couple of input fields and a button that will POST a new quest.

Using the Vue CLI to serve the client on http://localhost:8080, the front end of the app looks like this in action:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Client.PNG)

Once quests are added to the database, they'll start appearing in between the "RPG Quests" header and the input fields.

### Client Resources

To build the client, I used:

* [NodeJS](https://nodejs.org/en/)/[NPM](https://www.npmjs.com/) for package management
* [Vue CLI](https://cli.vuejs.org/) for scaffolding, serving, and building projects
* [Axios](https://github.com/axios/axios) for making HTTP requests to the API
* [Vue Axios Documentation](https://vuejs.org/v2/cookbook/using-axios-to-consume-apis.html) for making sense of how to use Axios in concert with the API
* [Postman](https://www.postman.com/) for testing API requests through the browser before implementing them in the client.

## JavaScript API: Express

[Express](https://expressjs.com/) is a lightweight web framework for [NodeJS](https://nodejs.org/en/) that allows you to write server-side applications with JavaScript.

It's un-opinionated, which means that you can build your applications how you like without it defining the architecture for you. You can add packages to improve functionality as you fancy, which I found to be a double-edged sword as a newbie to the framework. More on that later.

Being most comfortable in JavaScript, I was excited by the prospect of having the entire stack run on just one language instead of several. I had heard of the "MEVN Stack," which denotes a full stack application that is comprised of [MongoDB](https://www.mongodb.com/), Express, Vue, and NodeJS, and decided to try that out for this iteration of the project.

I followed a [web API tutorial](https://dev.to/beznet/build-a-rest-api-with-node-express-mongodb-4ho4) to first build a template app, then used another [MEVN tutorial](https://medium.com/@anaida07/mevn-stack-application-part-1-3a27b61dcae0) to fill in the details of how to get the API to communicate with the Vue client that I had built. The Express API that I created for this project follows a similar structure to the former, using MongoDB as the database:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Express-Structure.PNG)

If you're coming from a JavaScript background, Express is fairly easy to read, even if you're not familiar with some of the back end terminology. The following is a snippet from /routes/quests.js, for example, which handles the HTTP [endpoint](https://en.wikipedia.org/wiki/Web_API#Endpoints) requests:

```javascript
router.get('/', async (req, res) => {
    try {
        const quests = await Quest.find();
        res.json(quests);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

router.post('/', async (req, res) => {
    const quest = new Quest({
        name: req.body.name,
        description: req.body.description
    });
    try {
        const newQuest = await quest.save();
        res.status(201).json(newQuest);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});
```

The general theme of the code is to receive a request, attempt to contact the database to do work, and then send a response back to whoever's asking. The specifics can be quite complex, particularly if you're writing your own [middleware](https://expressjs.com/en/guide/using-middleware.html) that does things in between the request and response, but the code is at least readable.

I found MongoDB to be painless to work with as a [NoSQL](https://www.mongodb.com/nosql-explained) database.  If you're working with Express, you'll most likely use [Mongoose](https://mongoosejs.com/) as an [ODM](https://en.wikipedia.org/wiki/Object-relational_mapping#Object-oriented_databases) - basically like a "middle person" that translates a model of what your data looks like to the database.

The model in this app (called a "schema" in Mongoose terms) is really simple, located in /models/quests.js:

```language
const questSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true
    },
    description: {
        type: String,
        required: true
    }
});
```

The above indicates that the database should store our two fields: a quest name and a quest description.  Both of these fields are strings, and required. All GET and POST requests will have to conform to this model to interact with the database.

After wiring all of this up and POSTing a few new quests, the front end site started populating with data:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Vue-Front-End-1.PNG)

The process of setting up the Express API was not without its hair pulling, however. Being a primarily front end and 2D game developer, I've become intimately familiar with how dispersed the JavaScript ecosystem can feel. This frustration was magnified in attempting to build a back end app. There are a _lot_ of packages required to get everything up and running, each of which having its own required configuration and implementation.

If you're looking for a framework that just does everything out of the box, Express is most certainly not the choice for you. It's lightweight, flexible, and easy to read, in a very "choose-your-own-adventure" fashion. I quite like how clean the code is and the ability to structure my projects as I see fit, but troubleshooting and error handling do leave a lot to be desired.

### JavaScript/Express Resources

To build the JavaScript API, I used:

* [NodeJS](https://nodejs.org/en/)/[NPM](https://www.npmjs.com/) for package management
* [Express](https://expressjs.com/) as the main web framework
* [Dotenv](https://www.npmjs.com/package/dotenv) to create environment-specific variables
* [Nodemon](https://nodemon.io/) to watch files for changes and restart the server so I didn't have to
* [CORS](https://expressjs.com/en/resources/middleware/cors.html) to allow for [cross-origin requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) (basically a pain if you're trying to make requests from a client to a server that are both running locally on your machine)
* [MongoDB](https://www.mongodb.com/) for the [NoSQL](https://www.mongodb.com/nosql-explained) database
* [Mongoose](https://mongoosejs.com/) for writing models that map onto MongoDB 
* [This API tutorial](https://dev.to/beznet/build-a-rest-api-with-node-express-mongodb-4ho4) to provide a basic understanding of how to create an Express-MongoDB stack
* [This MEVN tutorial](https://medium.com/@anaida07/mevn-stack-application-part-1-3a27b61dcae0) to fill in the gaps of running a MongoDB-Express-Vue-Node full stack

## Python API: Flask

In the process of building the Express API, I had a conversation with a data science friend who works in Python. This gave me the idea of trying out non-JavaScript frameworks to see if they were better suited for my app.

I took a cursory look at [Django](https://www.djangoproject.com/), since I'd been hearing about it as a powerhouse back end framework that provides everything out of the box. I was a little intimidated by how opinionated it seemed, and opted to try out [Flask](https://palletsprojects.com/p/flask/) instead, which kind of felt like the Python equivalent of Express.

I followed the first few bits of the excellent [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) to get my app structure set up, using the companion [RESTful API tutorial](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask) to fill in the pieces of HTTP requests. The file structure turned out to be only a shade more complex than that of the Express API:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Flask-Structure.PNG)

The tutorial I followed uses [SQLite](https://www.sqlite.org/index.html) for its database, with [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) as an [ORM](https://en.wikipedia.org/wiki/Object-relational_mapping). The HTTP request code that's most analogous to the Express API is located in /app/routes.py:

```python
@app.route('/quests', methods=['GET'])
def get_quests():
    questQuery = Quest.query.all()
    quests = {}
    for quest in questQuery:
        quests[quest.name] = quest.description
    return jsonify(quests)

@app.route('/quests', methods=['POST'])
def post_quest():
    newQuest = Quest(name=request.json['name'], description=request.json['description'])
    db.session.add(newQuest)
    db.session.commit()
    return "Quest Added!"
```

Similarly, the database model (akin to the Mongoose "schema") is in /app/models.py:

```python
class Quest(db.Model):
    name = db.Column(db.String(256), primary_key=True, index=True, unique=True)
    description = db.Column(db.String(256), index=True, unique=True)
```

As I mentioned, I'm more familiar with JavaScript and C# than with Python, and working with the latter to build the Flask API felt like cheating. Certain things like pathing, package handling, and writing workable code were just _easy_, although I did get hung up on getting the API to correctly parse JSON for the client. I suspect that was more of an issue of my unfamiliarity with the language than anything else, but it did take time to troubleshoot.

To be quite honest, coming from a non-Flask background, I did kind of expect to complete a couple of tutorials and spin up an API without having to do all that much work for it.  

I can't say that it turned out that way, as Python does have its own particulars that require some time to get used to. Still, the Python ecosystem appears to be extremely well organized, and I enjoyed my time building the Flask API.

I've also heard that Django is a better and more scalable option for larger projects. But it seems like it would involve a separate, and steeper, learning curve to become proficient. 

Flask was easy enough for me as a non-Python developer to pick up and build something over a weekend. I suspect that learning Django would take quite a bit longer, but with potentially greater dividends over the long run. 

### Python/Flask Resources

To build the Flask API, I used:

* [Python 3](https://www.python.org/)/[pip](https://pip.pypa.io/en/stable/) for package management
* [Flask](https://palletsprojects.com/p/flask/) as the main web framework
* [python-dotenv](https://pypi.org/project/python-dotenv/) to configure environment variables
* [SQLite](https://www.sqlite.org/index.html) as the database 
* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) as the ORM to work with SQLite
* [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) as an additional tool to migrate data to SQLite 
* [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/) to handle the same CORS issue as with the Express API
* The [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) to learn the basics
* The [Flask REST API tutorial](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask) to understand how to receive HTTP requests

## C# API: ASP.NET

I can't tell you how many times I've Googled ".[NET](https://dotnet.microsoft.com/)" to understand what it is, how it's different from [ASP.NET](https://dotnet.microsoft.com/apps/aspnet), and why I'd want to use any of it. My C# knowledge comes mainly from working with [Unity](https://unity.com/), which exists somewhat adjacent to .NET and doesn't provide for a lot of exposure to Microsoft's larger ecosystem.

I've spent some time researching [Razor Pages](https://docs.microsoft.com/en-us/aspnet/core/razor-pages/?view=aspnetcore-3.1&tabs=visual-studio) and [MVC](https://docs.microsoft.com/en-us/aspnet/core/mvc/overview?view=aspnetcore-3.1), and finally came to understand ASP.NET's breadth of features as Microsoft's open source web framework. I decided to toss ASP.NET into the hat for a potential back end for my app, and set about working through the [official web API tutorial](https://docs.microsoft.com/en-us/aspnet/core/tutorials/first-mongo-app?view=aspnetcore-3.1&tabs=visual-studio) with ASP.NET Core and MongoDB.

The file structure for this version of the API was more complex than the others, given that .NET projects tend to have a much larger footprint:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/ASPNet-Structure.PNG)

I should also mention that I already had Visual Studio and all of the required workloads installed, which made the setup process easier. Plus, having spent time with MongoDB for the Express API, I found the database portion of the project to be similar, although by default, ASP.NET seems to prefer using Microsoft's [SQL Server](https://www.microsoft.com/en-us/sql-server/default.aspx) and the [Entity Framework ORM](https://docs.microsoft.com/en-us/ef/).

The ASP.NET code for HTTP requests is a bit more complex than what we've seen with the two other APIs, but it's no match for all of the code that sits _around_ it.  

First, consider this snippet in /Controllers/QuestController.cs that handles requests:

```c#
namespace QuestAPI.Controllers
{
    [Route("quests/")]
    [ApiController]
    public class QuestsController : ControllerBase
    {
        private readonly QuestService _questService;

        public QuestsController(QuestService questService)
        {
            _questService = questService;
        }

        [HttpGet]
        public ActionResult<List<Quest>> Get() =>
            _questService.Get();

        [HttpPost]
        public ActionResult<Quest> Create(Quest quest)
        {
            _questService.Create(quest);
            return CreatedAtRoute("GetQuest", new { id = quest.Id.ToString() }, quest);
        }
    }
}
```

Not too terrible, almost kind of readable, in a C# sort of way. The data model in /Models/Quest.cs is even easier:

```c#
namespace QuestAPI.Models{
    public class Quest
    {
        [BsonId]
        [BsonRepresentation(BsonType.ObjectId)]
        public string Id { get; set; }

        [BsonElement("Name")]
        public string Name { get; set; }

        public string Description { get; set; }
    }
}
```

These two snippets essentially do the same things as the previous examples that we've seen: take requests from the front end, process them to get or modify data in the database, and send a response back to the client.  

Yet, as you can probably tell from the complex file structure, there's so much code that surrounds these snippets, along with [Interfaces](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/interfaces/), [Dependency Injection](https://docs.microsoft.com/en-us/aspnet/core/fundamentals/dependency-injection?view=aspnetcore-3.1), and other abstractions, that it can be challenging to understand how it all works together.

Consider the following configuration code in /Startup.cs:

```c#
        public void ConfigureServices(IServiceCollection services)
        {
            services.Configure<QuestDatabaseSettings>(Configuration.GetSection(nameof(QuestDatabaseSettings)));

            services.AddSingleton<IQuestDatabaseSettings>(sp => sp.GetRequiredService<IOptions<QuestDatabaseSettings>>().Value);

            services.AddSingleton<QuestService>();

            services.AddCors(options =>
            {
                options.AddPolicy(MyAllowSpecificOrigins, builder =>
                {
                    builder.WithOrigins("http://localhost:3000/quests", "http://localhost:8080").AllowAnyHeader().AllowAnyMethod();
                });
            });

            services.AddControllers();
        }
```

Or this particularly nested bit from a separate [SQL Server web API tutorial](https://docs.microsoft.com/en-us/aspnet/core/tutorials/first-web-api?view=aspnetcore-3.1&tabs=visual-studio):

```c#
    [HttpGet]
    public async Task<ActionResult<IEnumerable<TodoItemDTO>>> GetTodoItems()
    {
        return await _context.TodoItems
            .Select(x => ItemToDTO(x))
            .ToListAsync();
    }
```

Lol. What?? As a new user, even familiar as I am with C#, I can go line-by-line to understand each abstraction, or I can just trust that the framework is handling everything for me and forget about it.

I tend to want to know exactly how my code works so that I can fix or alter it if necessary. But I certainly feel like my time spent learning the ins-and-outs of ASP.NET could be better utilized towards mastering another framework.

To be fair, ASP.NET appears to be similar to Django in being more opinionated and providing you with a ton of stuff out of the box, including an authentication solution, database management, and the lot. If these things are important to you, it's certainly worth considering.  

It also has the full support of Microsoft and an open source community. So if you're looking at developing enterprise-level applications that need to scale, you might want to take a longer look at ASP.NET as a potential solution.

### C#/ASP.Net Resources

To build the ASP.Net API, I used the following resources:

* [Visual Studio Community](https://visualstudio.microsoft.com/downloads/) as my code editor and IDE, with the ASP.NET and web development workload installed (I already had MongoDB running from the Express API)
* Microsoft's [official tutorial](https://docs.microsoft.com/en-us/aspnet/core/tutorials/first-mongo-app?view=aspnetcore-3.1&tabs=visual-studio) for building web APIs with ASP.NET and MongoDB

## TL;DR

In all, with some slight variations and hiccups among them, I've gotten each of the web APIs to work with the Vue client, with the ability to view quests from and add quests to the database. Hopefully, my explanation of the process has been helpful in your own search for a back end framework, but here are some additional recommendations just in case:

* If you're a JavaScript developer and/or want to manage everything that your application does, including its architecture, consider using Express.
* If you're a Python developer and/or want a pleasant experience in developing small projects, try Flask, but consider using Django if you need more out-of-the-box support and don't mind conforming to an opinionated framework.
* If you're a C# developer and willing to spend the time to learn the most arcane details of C# coding best practices, consider using ASP.NET. Alternatively, if you need enterprise-level support right out of the box, you'd be hard-pressed to find better.
* If you don't know what to use and just want to learn back end development, take a look at Flask.  It's easy to work with and will teach you the basics that you'll need to know for building web apps in any coding language.
* If you don't know what to use and want an adventure, choose Express. There's a rabbit hole of package management and Stack Overflow questions waiting that may make you tear your hair out, but you'll learn a lot about the JavaScript ecosystem and web development in general.

Additionally, two things bear mentioning that threw me for a spin in this process: CORS and environment variables. The former I've mentioned in this article a couple of times already, but it's worth discussing again to understand the scope of building a full stack app on your machine.

Unless you have an integrated development environment that's handling the whole stack for you, you'll likely have a client, a server, and a database that are all running independently of one another.  

In the Express API section above, for example, I was running 

1. the Vue CLI server, which rendered my front end app on port 8080; 
2. an NPM script to spin up the Express API server on port 3000; and
3. a separate instance of the Mongo database to get everything working together. That's three command prompts open and a general mess!

If you dig into the Vue code above (or on GitHub), you'll see that the requests made on behalf of the client, running on http://localhost:8080, are to the server on http://localhost:3000, which is where the Express API is listening. This is called "cross-origin resource sharing," or [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS), and it's blocked by the browser for security concerns. Most frameworks require you to install an additional package to get the whole thing running in your local environment.

Second, you'll want to become comfortable with [environment variables](https://en.wikipedia.org/wiki/Environment_variable), which can really help smooth some rough pathing edges at runtime. I used [dotenv](https://www.npmjs.com/package/dotenv) and [Flask-Env](https://pypi.org/project/Flask-Env/) for the Express and Flask projects, respectively. 

Both packages allow you to configure things like where your database lives, or what default port your application should be using, in one document. Your application then uses that document at runtime to figure out where to find everything, without any further configuration needed from you.

One final note that may be helpful if you're just working on a back end project and don't want to go through the trouble of building a front end client: consider using a third-party app like [Postman](https://www.postman.com/). I used it to make HTTP requests to each of the APIs to make sure they were working properly before layering on the Vue client and trying to get the whole stack running altogether. 

I hope this article has been helpful for you in your own process of looking for a back end framework.  Let me know what you find! 

If you enjoyed this article, please consider [checking out my games and books](https://www.nightpathpub.com/), [subscribing to my YouTube channel](https://www.youtube.com/msfarzan?sub_confirmation=1), or [joining the _Entromancy_ Discord](https://discord.gg/RF6k3nB).

M. S. Farzan, Ph.D. has written and worked for high-profile video game companies and editorial websites such as Electronic Arts, Perfect World Entertainment, Modus Games, and MMORPG.com, and has served as the Community Manager for games like _Dungeons & Dragons Neverwinter_ and _Mass Effect: Andromeda_. He is the Creative Director and Lead Game Designer of _[Entromancy: A Cyberpunk Fantasy RPG](https://www.nightpathpub.com/rpg)_ and author of _[The Nightpath Trilogy](http://nightpathpub.com/books)_. Find M. S. Farzan on Twitter [@sominator](https://twitter.com/sominator).

