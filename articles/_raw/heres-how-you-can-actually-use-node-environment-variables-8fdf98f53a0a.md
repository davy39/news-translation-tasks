---
title: Here’s how you can actually use Node environment variables
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-08T06:17:53.000Z'
originalURL: https://freecodecamp.org/news/heres-how-you-can-actually-use-node-environment-variables-8fdf98f53a0a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*akTd5oP32aXargVxiCOB8g.png
tags:
- name: humor
  slug: humor
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Burke Holland

  Environment variables are a fundamental part of Node development, but for some reason
  I never bothered with learning how to properly use them.

  Maybe because they are called “Environment Variables.”

  Just the words “Environment Variabl...'
---

By Burke Holland

Environment variables are a fundamental part of Node development, but for some reason I never bothered with learning how to properly use them.

Maybe because they are called “Environment Variables.”

Just the words “Environment Variable” trigger a PTSD-laced flashback in which I am trying to add the correct path to the Java Home directory on Windows. Does it go in PATH or JAVA_HOME or both? Do I need to end it with a semicolon? WHY AM I USING JAVA?

![Image](https://cdn-media-1.freecodecamp.org/images/ALjN6DcPA7VdZAcLA1vpTCzYLdx1lU3NtbOW)
_KILL_ME_

In Node, environment variables can be global (like on Windows), but are often used with a specific process that you want to run. For instance, if you had a web application, you might have environment variables that define:

* The HTTP Port to listen on
* The Database Connection String
* The JAVA_HOME…wait…no — sorry. The healing process takes time.

In this context, environment variables are really more like “Configuration Settings.” See how much nicer that sounds?

If you’ve done .NET before, you might be familiar with something like a `web.config` file. Node environment variables work much the same was as settings in a `web.config` — they’re a way for you to pass in information that you don’t want to hard code.

![Image](https://cdn-media-1.freecodecamp.org/images/lPJ7qP4TxdCmfuP6yYy5vnHuoUa8WH23RSqh)
_Quoting yourself is the pinnacle of delusion_

But how do you **use** these variables in your Node application? I had a hard time finding good resources on this with the requisite amount of Java jokes, so I decided to create one. Here are some of the different ways you can define and then read environment variables in your Node applications.

#### Pass it in the terminal

You can pass environment variables on the terminal as part of your Node process. For instance, if you were running an Express app and wanted to pass in the port, you could do it like this…

```bash
PORT=65534 node bin/www
```

Fun fact: port 65535 is the largest TCP/IP network value available. How do I know that? [StackOverflow of course](https://stackoverflow.com/questions/113224/what-is-the-largest-tcp-ip-network-port-number-allowable-for-ipv4). How does anybody know anything? But you can only go as high as port 65534 for a web app because that’s the highest port Chrome will connect to. How do I know **that?** Because [Liran Tal](https://www.freecodecamp.org/news/heres-how-you-can-actually-use-node-environment-variables-8fdf98f53a0a/undefined) told me in the comments. You should follow him. Between the two of us he’s the one who knows what he’s doing.

Now to use the variable in your code, you would use the `process.env` object.

```js
var port = process.env.PORT;
```

But this could get ugly. If you had a connection string, you probably wouldn’t want to start passing multiple variables on the terminal. It would look like you are hoarding configuration values, and someone who loves you could stage an intervention and that would be awkward for everyone involved.

```
PORT=65534
DB_CONN="mongodb://react-cosmos-db:swQOhAsVjfHx3Q9VXh29T9U8xQNVGQ78lEQaL6yMNq3rOSA1WhUXHTOcmDf38Q8rg14NHtQLcUuMA==@react-cosmos-db.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
SECRET_KEY="b6264fca-8adf-457f-a94f-5a4b0d1ca2b9"
```

This doesn’t scale, and everyone wants to scale. According to every architect I’ve ever sat in a meeting with, “scaling” is more important than the application even working.

So let’s look at another way: .env files.

#### Use a .env file

.env files allow you to put your environment variables inside a file. You just create a new file called `.env` in your project and slap your variables in there on different lines.

```
PORT=65534

DB_CONN="mongodb://react-cosmos-db:swQOhAsVjfHx3Q9VXh29T9U8xQNVGQ78lEQaL6yMNq3rOSA1WhUXHTOcmDf38Q8rg14NHtQLcUuMA==@react-cosmos-db.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"

SECRET_KEY="b6264fca-8adf-457f-a94f-5a4b0d1ca2b9"
```

To read these values, there are a couple of options, but the easiest is to use the `dotenv` package from npm.

```bash
npm install dotenv --save
```

Then you just require that package in your project wherever you need to use environment variables. The `dotenv` package will pick up that file and load those settings into Node.

```js
Use dotenv to read .env vars into Node
require('dotenv').config();
var MongoClient = require('mongodb').MongoClient;

// Reference .env vars off of the process.env object
MongoClient.connect(process.env.DB_CONN, function(err, db) {
  if(!err) {
    console.log("We are connected");
  }
});
```

PROTIP: Don’t check your `.env` file into Github. It has all you secrets in it and Github will email you and tell you so. Don’t be like me.

OK — Nice. But this is kind of a pain. You have to put this in every single file where you want to use environment variables AND you have to deploy the `dotenv` to production where you don’t actually need it. I’m not a huge fan of deploying pointless code, but I guess I just described my whole career.

Luckily, you are using [VS Code](https://code.visualstudio.com/?wt.mc_id=dotenv-medium-buhollan) (because **of course you are**), so you have some other options.

#### Working with .env files in VS Code

First off, you can [install the DotENV extension](https://marketplace.visualstudio.com/items?itemName=mikestead.dotenv&wt.mc_id=dotenv-medium-buhollan) for code which will give you nice syntax highlighting in your .env files.

[**DotENV - Visual Studio Marketplace**](https://marketplace.visualstudio.com/items?itemName=mikestead.dotenv&WT.mc_id=dotenv-medium-buhollan)  
[_Extension for Visual Studio Code - Support for dotenv file syntax_](https://marketplace.visualstudio.com/items?itemName=mikestead.dotenv&WT.mc_id=dotenv-medium-buhollan)  
[marketplace.visualstudio.com](https://marketplace.visualstudio.com/items?itemName=mikestead.dotenv&WT.mc_id=dotenv-medium-buhollan)

![Image](https://cdn-media-1.freecodecamp.org/images/5TqqPI4CyihReGrXCaFqLDEAADqD-AJtHS4Y)

The VS Code Debugger also offers some more convenient options for loading values from .env files **if** you are using the VS Code Debugger.

#### VS Code Launch Configurations

The Node debugger for VS Code (already there, no need to install anything) supports loading in .env files via launch configurations. You can read more more about Launch Configurations [here](https://code.visualstudio.com/docs/nodejs/nodejs-debugging?WT.mc_id=dotenv-medium-buhollan).

![Image](https://cdn-media-1.freecodecamp.org/images/f6NKkdg6vZOubtIzh4k4EGEVUWtvC7ZC88SK)

When you create a basic Node Launch Configuration (click on the gear and select Node), you can do one or both of two things.

The first is you can simply pass variables in on the launch config.

![Image](https://cdn-media-1.freecodecamp.org/images/OKoRgCmVBQJG3p2ZQ9em6NaMIYwNauEwp6Wd)

This is nice, but the fact that every value has to be a string bothers me a bit. It’s a number, not a string. JavaScript only has, like, 3 types. Don’t take one of them away from me.

There is a simpler way here. We’ve already learned to love `.env` files, so instead of passing them, we can just give VS Code the name of the .env file.

![Image](https://cdn-media-1.freecodecamp.org/images/5mkXYjMBORiWKSTBZzCcZTK33ubGUTFy7SuZ)

And as long as we are starting our process from VS Code, environment variables files are loaded in. We don’t have to mutilate numbers into strings and we aren’t deploying worthless code into production. Well, at least you aren’t.

#### Starting with NPM instead of Node

You might have gotten this far and thought, “Burke, I never ever run `node` anything. It’s always an npm script like `npm start`”.

In this case you can still use VS Code Launch configs. Instead of using a standard Node Launch process, you add a config that is a “Launch Via NPM” task.

![Image](https://cdn-media-1.freecodecamp.org/images/7tUmGEn-i6T30kHkzfXYj5qzAK8rB6qMTZir)

Now you can add back in your `envFile` line and tweak the `runtimeArgs` so that they launch the correct script. This is _usually_ something like “start” or “debug”.

![Image](https://cdn-media-1.freecodecamp.org/images/bkDqIcWImMhXbMrGry73ABhvBWCG2x5Sy92k)

**Note that you have to add the `--inspect` flag to your npm script so that VS Code can attach the debugger**. Otherwise the task will launch, but the VS Code debugger will time out like me trying to get a date in high school.

![Image](https://cdn-media-1.freecodecamp.org/images/tGcPy6sdBlu9sR1OD07VdHD9MuSgj9-uDb7K)

### Production environment variables

So far we’ve looked at how to define variables for development. You likely won’t use .env files in production, and VS Code Launch Configurations aren’t going to be super helpful on a server.

In production, variables will be defined however your platform of choice allows you to do so. In the case of Azure, there are 3 different ways to define and manage environment variables.

The first way is to use the [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/webapp/config/appsettings?view=azure-cli-latest&wt.mc_id=dotenv-medium-buhollan).

```bash
az webapp config appsettings set -g MyResourceGroup -n MyApp --settings PORT=65534
```

Which works, but, ew.

Another way is via the Azure web portal. I don’t always use a web portal, but when I do, it’s to set environment variables.

In the case of Azure, these are called “Application Settings”.

![Image](https://cdn-media-1.freecodecamp.org/images/prz52i4eiyXapzYAPqEIQ9ggSnCYwFGTYWzi)

And since you are using VS Code, you can install the App Service extension and manage all the App Settings [right from the editor](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azureappservice&WT.mc_id=dotenv-medium-buhollan).

![Image](https://cdn-media-1.freecodecamp.org/images/4L4UwQ0TYob3wz--qcO2AQfmjFIxhMQ6ecax)

I love not having to leave VS Code to do anything. I would write emails in VS Code if I could.

WAIT A MINUTE!

[**markdown-mail - Visual Studio Marketplace**](https://marketplace.visualstudio.com/items?itemName=ccccly.markdown-mail&WT.mc_id=dotenv-medium-buhollan)  
[_Extension for Visual Studio Code - Using markdown to write your email and send！_](https://marketplace.visualstudio.com/items?itemName=ccccly.markdown-mail&WT.mc_id=dotenv-medium-buhollan)  
[marketplace.visualstudio.com](https://marketplace.visualstudio.com/items?itemName=ccccly.markdown-mail&WT.mc_id=dotenv-medium-buhollan)

### Now you know

Now you know what I know (which aint a lot, let me tell you) and I feel like I accomplished my goal of a tasteful amount of Java jokes along the way. Just in case I didn’t, I’ll leave you with this one.

> Java is a very powerful tool for turning XML into stack traces  
>   
> — Unknown

_Satire Disclaimer: Most of this is a poor attempt at humor, and some of it at the expense of Java; which isn’t nice but is very easy. These jokes don’t write themselves._

