---
title: JavaScript Discord Bot Tutorial – Code a Discord Bot And Host it for Free
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-03-08T14:45:50.000Z'
originalURL: https://freecodecamp.org/news/create-a-discord-bot-with-javascript-nodejs
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/discordjs.png
tags:
- name: discord
  slug: discord
- name: youtube
  slug: youtube
seo_title: null
seo_desc: 'This tutorial will show you how to use JavaScript and Node.js to build
  your own Discord bot completely in the cloud.

  You do not need to install anything on your computer, and you do not need to pay
  anything to host your bot.

  We are going to use a num...'
---

This tutorial will show you how to use JavaScript and Node.js to build your own Discord bot completely in the cloud.

You do not need to install anything on your computer, and you do not need to pay anything to host your bot.

We are going to use a number of tools, including the Discord API, Node.js libraries, and a cloud computing platform called [Repl.it](https://www.repl.it).

If you'd rather code your discord bot using Python instead of JavaScript, [read this tutorial instead](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/).

There is also a video version of this written tutorial. The video is embedded below and the written version is after the video.

%[https://youtu.be/7rU_KyudGBY]

## How to Create a Discord Bot Account

In order to work with the Node.js library and the Discord API, we must first create a Discord Bot account.

Here are the step to creating a Discord Bot account.

1. Make sure you’re logged on to the [Discord website](https://discord.com).

2. Navigate to the [application page](https://discord.com/developers/applications).

3. Click on the “New Application” button.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-117.png)

4. Give the application a name and click “Create”.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-118.png)

5. Go to the “Bot” tab and then click “Add Bot”. You will have to confirm by clicking "Yes, do it!"

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-119.png)

Keep the default settings for **Public Bot** (checked) and **Require OAuth2 Code Grant** (unchecked).

Your bot has been created. The next step is to copy the token.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-122.png)

This token is your bot's password so don't share it with anybody. It could allow someone to log in to your bot and do all sorts of bad things.

You can regenerate the token if it accidentally gets shared.

## How to Invite Your Bot to Join a Server

Now you have to get your Bot User into a server. To do this, you should create an invite URL for it.

Go to the "OAuth2" tab. Then select "bot" under the "scopes" section.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-123.png)

Now choose the permissions you want for the bot. Our bot is going to mainly use text messages so we don't need a lot of the permissions. You may need more depending on what you want your bot to do. Be careful with the "Administrator" permission.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-124.png)

After selecting the appropriate permissions, click the 'copy' button above the permissions. That will copy a URL which can be used to add the bot to a server.

Paste the URL into your browser, choose a server to invite the bot to, and click “Authorize”.

To add the bot, your account needs "Manage Server" permissions.

Now that you've created the bot user, we'll start writing the Python code for the bot.

## How to Code a Basic Discord Bot with the discord.js Library

We'll be using the discord.js Node library to write the code for the bot. discord.js is an API wrapper for Discord that makes it easier to create a Discord bot in Node.js / JavaScript.

### How to Create a Repl and Install discord.js

You can develop the bot on your local computer with any code editor. However, in this tutorial, we'll be using Repl.it because it will make it simpler for anyone to follow along. Repl.it is an online IDE that you can use in your web browser.

Start by going to [Repl.it](https://repl.it). Create a new Repl and choose "Node.js" as the language. This means the programming language will be JavaScript.

To use the discord.js library, just add `const Discord = require("discord.js");` at the top of `main.js`. Repl.it will automatically install this dependency when you press the "run" button.

### How to Set Up Discord Events for Your Bot

discord.js revolves around the concept of events. An event is something you listen to and then respond to. For example, when a message happens, you will receive an event about it that you can respond to.

Let’s make a bot that replies to a specific message. This simple bot code is taken directly from [the discord.js documentation](https://discord.js.org/#/docs/main/stable/general/welcome). We will be adding more features to the bot later.

Add this code to main.js. I'll explain what all this code does shortly.

```javascript
const Discord = require("discord.js")
const client = new Discord.Client()

client.on("ready", () => {
  console.log(`Logged in as ${client.user.tag}!`)
})

client.on("message", msg => {
  if (msg.content === "ping") {
    msg.reply("pong");
  }
})

client.login(process.env.TOKEN)
```

When you created your bot user on Discord, you copied a token. Now we are going to create a `.env` file to store the token. 

`.env` files are used for declaring environment variables. On Repl.it, most files you create are visible to anyone but `.env` files are only visible to you.  Other people viewing a public repl will not be able to see the contents of the `.env` file.

So if you are developing on Repl.it, only include private information like tokens or keys in a `.env` file.

Click the "Add file" button and create a file named `.env`.

Inside the file add the following line, including your actual token you copied previously:

```
TOKEN=[paste token here]
```

Now let's go over what each line of code is doing in your Discord bot code.

The first line imports the discord.js library.  Next, we create an instance of a [`Client`](https://discordpy.readthedocs.io/en/latest/api.html#discord.Client). This is the connection to Discord.

The `client.on()` is used to check for events.  It accepts an event name, and then a callback function to be called when the event takes place. In this code, the `ready` event is called when the bot is ready to start being used. Then, when the Discord server has a new message, the `message` event is called. 

The code checks if the [`msg.content`](https://discordpy.readthedocs.io/en/latest/api.html#discord.Message.content) equals `'ping'`. If so, then the bot replies with `'pong'` to the channel.

Now that the bot is set up, the final line runs the bot with the login token. It gets the token from out `.env` file.

We have the code for the bot so now we just have to run it.

### How to Run the Bot

Now click run button on the top to run your bot in repl.it.

Now go to your Discord room and type "ping". Your bot should return "pong".

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image.png)

## How to Improve the Bot

Now that we have a basic bot working, we'll improve it. It is called "Encourage Bot" for a reason. 

This bot will respond with a message of encouragement whenever someone sends a message containing a sad or depressing word.

Anyone will be able to add encouraging messages for the bot to use and the user-submitted messages will be stored in the Repl.it database.

The bot will also return a random inspirational quote from an API when someone types the message "$inspire" into the chat.

We'll start with adding the "$inspire" feature.

### How to Add Inspirational Quotes to the Bot

We will get inspirational quotes from an API called zenquotes.io. We need to import the node-fetch module, add a `getQuote()` function, and update our bot code to call the function. 

Here is the updated code. After the code, I'll explain the new parts.

```javascript
const Discord = require("discord.js")
const fetch = require("node-fetch")
const client = new Discord.Client()

function getQuote() {
  return fetch("https://zenquotes.io/api/random")
    .then(res => {
      return res.json()
      })
    .then(data => {
      return data[0]["q"] + " -" + data[0]["a"]
    })
}

client.on("ready", () => {
  console.log(`Logged in as ${client.user.tag}!`)
})

client.on("message", msg => {
  if (msg.author.bot) return
    
  if (msg.content === "$inspire") {
    getQuote().then(quote => msg.channel.send(quote))
  }
})

client.login(process.env.TOKEN)
```

We now have to import the `node-fetch` module. This module allows our code to make an HTTP request to get data from the API. 

The `getQuote()` function is pretty straightforward. First, it uses the node-fetch module to request data from the API URL. The API returns a random inspirational quote. This function could easily be rewritten to get quotes from a different API, if the current one stops working.

Then the function converts the response from the API to JSON and creates a string to return. Through trial and error I figured out how to get the quote from the JSON into the string format I wanted. The quote is returned from the function as a string.

The final part updated in the code is toward the end. Previously it looked for the message "ping". Now it looks for "$inspire". Instead of returning "pong", it gets the quote with `getQuote()` and returns the quote. We use `msg.channel.send()` to send the message to the channel. Also, the code checks if the message comes from the bot itself and if it does, it leaves the function so it does not do anything.

At this point you can run your code and try it out.

## How to Add Encouraging Messages to the Bot

Now we will implement the feature where the bot responds with encouraging messages when a user posts a message with a sad word.

### How to Add Sad Words to the Bot

First we need to create an array that contains the sad words that the bot will respond to.

Add the following line after the `client` variable is created:

`sadWords = ["sad", "depressed", "unhappy", "angry", "miserable"]`

Feel free to add more words to the list.

### How to Add Encouraging Messages to the Bot

Now we'll add an array of encouraging messages that the bot will respond with.

Add the following array after the `sadWords` list you created:

```python
encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person / bot!"
]
```

Like before, feel free to add more phrases of your choice to the array . I'm just using three items for now because later we'll add the ability for users to add more encouraging phrases for the bot to use.

### How to Respond to Messages

Now we need to update our bot to use the two lists we created. 

Now we will update the `message` function to check all messages to see if they contain a word from the `sadWords` list. If a sad word is found, the bot will send a random message of encouragement. 

Here is the updated code:

```javascript
client.on("message", msg => {
  if (msg.content === "$inspire") {
    getQuote().then(quote => msg.channel.send(quote))
  }

  if (sadWords.some(word => msg.content.includes(word))) {
    const encouragement = encouragements[Math.floor(Math.random() * encouragements.length)]
    msg.reply(encouragement)
  }

})
```

This is a good time to test the bot. You know enough now to create your own bot. But next you'll learn how to implement more advanced features and store data using the Repl.it database.

### How to Enable User-submitted Messages

The bot is completely functional, but now let's make it possible to update the bot right from Discord. A user should be able to add more encouraging messages for the bot to use when it detects a sad word.

We are going to use Repl.it's built-in database to store user-submitted messages. This database is a key-value store that’s built into every repl.

At the top of the code, under the other import statements, add:

```javascript
const Database = require("@replit/database")
const db = new Database()
```

This will allow us to use the Repl.it database. When you run the code, Repl.it should install the database module automatically. If for some reason it doesn't, you may have to go into the Shell tab (not the Console) and type "npm install @replit/database".

After where the `encouragements` array is created, insert the following code to add the encouragements to the database if needed:

```javascript
db.get("encouragements").then(encouragements => {
  if (!encouragements || encouragements.length < 1) {
    db.set("encouragements", starterEncouragements)
  }  
})
```

Also, rename the `encouragements` array toward the top to `starterEncouragements`.

Users will be able to add custom encouraging messages for the bot to use directly from the Discord chat. Before we add new commands for the bot, let's create two helper functions that will add custom messages to the database and delete them.

Add the following code after the `getQuote()` function:

```javascript
function updateEncouragements(encouragingMessage) {
  db.get("encouragements").then(encouragements => {
    encouragements.push([encouragingMessage])
    db.set("encouragements", encouragements)
  })
}

function deleteEncouragment(index) {
  db.get("encouragements").then(encouragements => {
    if (encouragements.length > index) {
      encouragements.splice(index, 1)
      db.set("encouragements", encouragements)
    }
  })
}
```

The `updateEncouragements()` function accepts an encouraging message as an argument.

First it gets the "encouragements" from the database. Then, it adds the new encouragement to the array, and stores the updated array back in the database under the "encouragements" key. 

The `deleteEncouragement()` function accepts an index as an argument.

It gets the list of encouragements from the database stored under the "encouragements" key. If the length is more than the index, then the list item at that index is deleted. Finally, the updated list is stored back in the database under the "encouragements" key.

Here is the updated code for the `message` function. After the code, I'll explain the new sections.

```javascript
client.on("message", msg => {
  if (msg.content === "$inspire") {
    getQuote().then(quote => msg.channel.send(quote))
  }

  
  if (sadWords.some(word => msg.content.includes(word))) {
    db.get("encouragements").then(encouragements => {
      const encouragement = encouragements[Math.floor(Math.random() * encouragements.length)]
      msg.reply(encouragement)
    })
  }

  if (msg.content.startsWith("$new")) {
    encouragingMessage = msg.content.split("$new ")[1]
    updateEncouragements(encouragingMessage)
    msg.channel.send("New encouraging message added.")
  }

  if (msg.content.startsWith("$del")) {
    index = parseInt(msg.content.split("$del ")[1])
    deleteEncouragment(index)
    msg.channel.send("Encouraging message deleted.")
  }
})
```

The sad words section has been updated to use the encouraging messages from the database so user submitted messages can be used.

The next new section of code is used to add a new user-submitted message to the database. If a Discord message starts with "$new", then the text after "$new" will be used as a new encouraging message. 

The code `msg.content.split('$new ')[1]` splits off the message from the "$new" command and stores the message in a variable. In that line of code, take note of the space in `'$new '`. We want everything _after_ the space.

We call the `updateEncouragements` helper function with the new message, and then the bot sends a message to the discord chat confirming that the message was added.

The third new section (at the end of the code above) checks if a new Discord message starts with "$del". This is the command to delete an item from the "encouragements" list in the database.

The index is split off from the Discord message starting with "$del". Then, the `deleteEncouragement()` function is called passing in the index to delete. The updated list of encouragements is loaded into the `encouragements` variable, and then the bot sends a message to Discord with the current list.

## Final Bot Features

The bot should work so this is a good time to test it. We will now add a few final features.

We will add the ability to get a list of user-submitted messages right from Discord and we will add the ability to turn off and on whether the bot responds to sad words.

I will give you the full final code of the program, and then I'll discuss the updates below the code.

```javascript
const Discord = require("discord.js")
const fetch = require("node-fetch")
const Database = require("@replit/database")

const db = new Database()
const client = new Discord.Client()

const sadWords = ["sad", "depressed", "unhappy", "angry", "miserable"]

const starterEncouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person / bot!"
]

db.get("encouragements").then(encouragements => {
  console.log(encouragements)
  if (!encouragements || encouragements.length < 1) {
    db.set("encouragements", starterEncouragements)
  }  
})

db.get("responding").then(value => {
  if (value == null) {
    db.set("responding", true)
  }  
})

function getQuote() {
  return fetch("https://zenquotes.io/api/random")
    .then(res => {
      return res.json()
      })
    .then(data => {
      return data[0]["q"] + " -" + data[0]["a"]
    })
}

function updateEncouragements(encouragingMessage) {
  db.get("encouragements").then(encouragements => {
    encouragements.push([encouragingMessage])
    db.set("encouragements", encouragements)
  })
}

function deleteEncouragment(index) {
  db.get("encouragements").then(encouragements => {
    if (encouragements.length > index) {
      encouragements.splice(index, 1)
      db.set("encouragements", encouragements)
    }
  })
}

client.on("ready", () => {
  console.log(`Logged in as ${client.user.tag}!`)
})

client.on("message", msg => {
  if (msg.content === "$inspire") {
    getQuote().then(quote => msg.channel.send(quote))
  }

  db.get("responding").then(responding => {
    if (responding && sadWords.some(word => msg.content.includes(word))) {
      db.get("encouragements").then(encouragements => {
        const encouragement = encouragements[Math.floor(Math.random() * encouragements.length)]
        msg.reply(encouragement)
      })
    }
  })

  if (msg.content.startsWith("$new")) {
    encouragingMessage = msg.content.split("$new ")[1]
    updateEncouragements(encouragingMessage)
    msg.channel.send("New encouraging message added.")
  }

  if (msg.content.startsWith("$del")) {
    index = parseInt(msg.content.split("$del ")[1])
    deleteEncouragment(index)
    msg.channel.send("Encouraging message deleted.")
  }

  if (msg.content.startsWith("$list")) {
    db.get("encouragements").then(encouragements => {
      msg.channel.send(encouragements)
    })
  }
    
  if (msg.content.startsWith("$responding")) {
    value = msg.content.split("$responding ")[1]

    if (value.toLowerCase() == "true") {
      db.set("responding", true)
      msg.channel.send("Responding is on.")
    } else {
      db.set("responding", false)
      msg.channel.send("Responding is off.")
    }
  }
})

client.login(process.env.TOKEN)
```

The first section added to the code is right under the `starterEncouragements` list:

```javascript
db.get("responding").then(value => {
  if (value == null) {
    db.set("responding", true)
  }  
})
```

We create a new key in the database called "responding" and set it to "true". We'll use this to determine if the bot should respond to sad words or not. Since the database is saved even after the program stops running, we only create the new key if it doesn't already exist.

The next new part of the code is in the section that responds to sad words is now inside this if statement. The bot will only respond to sad words if `db.get("responding") = true`. The ability to update this value comes after this next section.

Next, after the code to make the bot respond to the "$del" command, there is new code to respond to the "$list" command when sent as a Discord message. 

The bot sends the list of encouragements as a Discord message.

The final new section comes next. This code makes the bot respond to the "$responding" command. This command takes an argument of either "true" or "false". Here is a usage example: "$responding true". 

The code first pulls off the argument with `value = msg.content.split("$responding ")[1]` (like before, note the space in `"$responding "`). Then there is an if/else statement that appropriately sets the "responding" key in the database and sends a notification message back to Discord. If the argument is anything but "true", the code assumes "false".

The code for the bot is complete! You can now run the bot and try it out. But there is one more important step that we will discuss next.

## How to Set Up the Bot to Run Continuously

If you run your bot in repl.it and then close the tab it is running in, your bot will stop running.

But there are two ways you can keep your bot running continuously, even after you close your web bowser.

The first way and simplest way is to sign up for paid plan in Repl.it. Their cheapest paid plan is called the Hacker Plan and it includes five always-on Repls. 

You can get three months free using this link (limited to first 1000 people):  https://repl.it/claim?code=tryalwayson2103

Once you have signed up for that plan, open your Repl and click the name at the top. Then select the "Always On" option.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-36.png)

There is another way to keep your code running even on the free tier but it is a little more complicated. Repl.it will continue running a web server even after the tab is closed. But even a web server will only run for up to an hour without any use.

Here is what the repl.it docs say:

> Once deployed, the server will continue to run in the background, even after you close the browser tab. The server will stay awake and active until an hour after its last request, after which it will enter a sleeping stage. Sleeping repls will be woken up as soon as it receives another request; there is no need to re-run the repl. However, if you make changes to your server, you will need to restart the repl in order to see those changes reflected in the live version.

To keep the bot running continuously, we'll use another free service called Uptime Robot at [https://uptimerobot.com/](https://uptimerobot.com/).

Uptime Robot can be set up to ping the bot's web server on repl.it every 5 minutes. With constant pings, the bot will never enter the sleeping stage and will just keep running.

So we have to do two more things to get our bot to run continuously:

1. create a web server in repl.it and
2. set up Uptime Robot to continuously ping the web server.

### How to Create a Web Server in repl.it

Creating a web server is simpler than you may think. 

To do it, create a new file in your project called `server.js`.

Then add the following code:

```javascript
const express = require("express")

const server = express()

server.all("/", (req, res) => {
  res.send("Bot is running!")
})

function keepAlive() {
  server.listen(3000, () => {
    console.log("Server is ready.")
  })
}

module.exports = keepAlive
```

In this code, we use express to start a web server. The server returns "Bot is running!" to anyone who visits it. The server will run on a separate thread from our bot. We won't discuss everything here since the rest is not really relevant to our bot.

Now we just need the bot to run this web server.

Add the following line toward the top of `index.js`  to import the server.

```python
const keepAlive = require("./server")
```

To start the web server when `index.js` is run, add the following line as the second-to-last line, right before the bot runs.

`keepAlive()`

When you run the bot on repl.it after adding this code, a new web server window will open up. There is a URL shown for the web server. Copy the URL so you can use it in the next section.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-1.png)

### How to Set Up Uptime Robot

Now we need to set up Uptime Robot to ping the web server every five minutes. This will cause the bot to run continuously.

Create a free account on [https://uptimerobot.com/](https://uptimerobot.com/).

Once you are logged in to your account, click "Add New Monitor".

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-21.png)

For the new monitor, select "HTTP(s)" as the Monitor Type and name it whatever you like. Then, paste in the URL of your web server from repl.it. Finally, click "Create Monitor".

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-22.png)

We're done! Now the bot will run continuously so people can always interact with it on Repl.it.

## Conclusion

You now know how to create a Discord bot with JavaScript, and run it continuously in the cloud. 

There are a lot of other things that the discord.js library can do. So if you want to give a Discord bot even more features, your next step is to check out [the docs for discord.js.](https://discord.js.org/#/docs/main/stable/general/welcome)

