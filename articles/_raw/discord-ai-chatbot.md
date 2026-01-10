---
title: How to Build a Discord AI Chatbot that Talks Like Your Favorite Character
subtitle: ''
author: Lynn Zheng
co_authors: []
series: null
date: '2021-08-26T19:30:00.000Z'
originalURL: https://freecodecamp.org/news/discord-ai-chatbot
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/lynns-thumbnail.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: '#chatbots'
  slug: chatbots
- name: discord
  slug: discord
seo_title: null
seo_desc: 'Would you like to talk to a chatbot that speaks like your favorite character,
  fictional or non-fictional? Let''s build one!

  In case you''ve seen my previous tutorial on this topic, stick with me as this version
  features lots of updates.

  You can follow ...'
---

Would you like to talk to a chatbot that speaks like your favorite character, fictional or non-fictional? Let's build one!

In case you've seen my previous tutorial on this topic, stick with me as this version features lots of updates.

You can follow along with this tutorial using the code on my GitHub:

%[https://github.com/RuolinZheng08/twewy-discord-chatbot] 

If you want, you can dive right into my video tutorial on YouTube – or read on for more details. 😎

%[https://youtu.be/Rk8eM1p_xgM] 

## What to Expect from this Tutorial

Here is an example of the Discord AI chatbot that we will have built by the end of this tutorial.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/discord.gif align="left")

*Chat demo with my bot in Discord. I drew the bot's icon 😊*

My chatbot project started as a joke with a friend when we were playing video games.

I'm honestly surprised by how popular it became – there were 5.9k views of my previous tutorial, plus, when I deployed my bot to a 1k+ user server, people flooded it with 300+ messages in an hour, effectively crashing the bot. 😳 You can [read more about my deployment post-mortem in this post.](https://www.freecodecamp.org/news/recovering-from-deployment-hell-what-i-learned-from-deploying-my-discord-bot-to-a-1000-user-server/)

Since a lot of people are interested in building their own bots based on their favorite characters, I updated my tutorial to include an in-depth explanation on how to gather text data for any character, fictional or non-fictional.

You may also create a custom dataset that captures the speech between you and your friends and build a chatbot that speaks like yourself!

Other updates in this tutorial address changes in Hugging Face's model hosting services, including API changes that affect how we push the model to Hugging Face's model repositories.

## Outline of this Tutorial

The video version of this tutorial runs for a total of one hour and features the following topics:

1. Gather text data for your character using one of these two methods: find pre-made datasets on **Kaggle** or make custom datasets from raw transcripts.
    
2. Train the model in **Google Colab,** a cloud-based Jupyter Notebook environment with free GPUs.
    
3. Deploy the model to **Hugging Face,** an AI model hosting service.
    
4. Build a Discord bot in either **Python** or **JavaScript**, your choice! 🤩
    
5. Set up the Discord bot's permissions so they don't spam non-bot channels
    
6. Host the bot on **Repl.it.**
    
7. Keep the bot running indefinitely with **Uptime Robot.**
    

To learn more about how to build Discord bots, you may also find these two freeCodeCamp posts useful – there's a [Python version](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/) and a [JavaScript version](https://www.freecodecamp.org/news/create-a-discord-bot-with-javascript-nodejs/).

## How to Prepare the Data

For our chatbot to learn to converse, we need text data in the form of dialogues. This is essentially how our chatbot is going to respond to different exchanges and contexts.

### Is Your Favorite Character on Kaggle?

There are a lot of interesting datasets on Kaggle for popular cartoons, TV shows, and other media. For example:

* [Rick and Morty](https://www.kaggle.com/andradaolteanu/rickmorty-scripts)
    
* [Harry Potter](https://www.kaggle.com/gulsahdemiryurek/harry-potter-dataset?select=Harry+Potter+1.csv)
    
* [The Big Bang Theory](https://www.kaggle.com/mitramir5/the-big-bang-theory-series-transcript)
    
* [Game of Thrones](https://www.kaggle.com/anderfj/game-of-thrones-series-scripts-breakdowns)
    

We only need two columns from these datasets: **character name** and **dialogue line**.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-25-at-14.07.59.png align="left")

*Example dataset: Harry Potter movie transcript*

### Can't Find Your Favorite Character on Kaggle?

Can't find your favorite character on Kaggle? No worries. We can create datasets from raw transcripts. A great place to look for transcripts is [Transcript Wiki](https://transcripts.fandom.com/wiki/Transcripts_Wiki). For example, check out [this Peppa Pig transcript.](https://transcripts.fandom.com/wiki/Peppa_Pig)

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-25-at-14.13.57.png align="left")

*Example: Peppa Pig transcript*

Using a regular expression like `([a-zA-Z|\s]+): (.+)`, we can extract out the two columns of interest, character name, and dialogue line.

[Try it out on this Python regex website yourself!](https://pythex.org/?regex=\(%5Ba-zA-Z%7C%5Cs%5D%2B\)%3A%20\(.%2B\)&test_string=Peppa%20Pig%3A%20George%2C%20I%20could%20see%20you%20too%20easily.%0A%0ANarrator%3A%20Now%20it%20is%20Peppa%27s%20turn%20to%20hide.%0A%0AGeorge%3A%20One...%20um...%20three.%0A%0AMummy%20Pig%3A%20I%27ll%20help%20George%20to%20count.%20&ignorecase=0&multiline=0&dotall=0&verbose=0)

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-25-at-14.58.35.png align="left")

## How to Train the Model

Under the hood, our model will be a **Generative Pre-trained Transfomer (GPT),** the most popular language model these days.

Instead of training from scratch, we will load [Microsoft's pre-trained GPT](https://huggingface.co/microsoft/DialoGPT-small), `DialoGPT-small`, and fine-tune it using our dataset.

My GitHub repo for this tutorial contains [the notebook file](https://github.com/RuolinZheng08/twewy-discord-chatbot/blob/main/model_train_upload_workflow.ipynb) named `model_train_upload_workflow.ipynb` to get you started. All you need to do is the following: (please refer to the video for a detailed walkthrough)

1. Upload the file to [Google Colab](https://colab.research.google.com/)
    
2. Select **GPU** as the runtime, which will speed up our model training.
    
3. Change the dataset and the target character in code snippets like:
    

```python
data = pd.read_csv('MY-DATASET.csv')
CHARACTER_NAME = 'MY-CHARACTER'
```

Running through the training section of the notebook should take less than half an hour. I have about 700 lines and the training takes less than ten minutes. The model will be stored in a folder named `output-small` .

Want an even smarter and more eloquent model? Feel free to train a larger model like `DialoGPT-medium` or even `DialoGPT-large`. Model size here refers to the number of parameters in the model. More parameters will allow the model to pick up more complexity from the dataset.

You may also increase the number of training epochs by searching for `num_train_epochs` in the notebook. This is the number of times that the model will cycle through the training dataset. The model will generally get smarter when it has more exposure to the dataset.

However, do take care not to overfit the model: If the model is trained for too many epochs, it may memorize the dataset and recite back lines from the dataset when we try to converse with it. This isn't ideal as we want the conversation to be more organic.

## How to Host the Model

We will host the model on Hugging Face, which provides a free API for us to query the model.

Sign up for [Hugging Face](https://huggingface.co/) and create a new model repository by clicking on **New model.** Obtain your API token by going to **Edit profile &gt; API Tokens.** We will need this token when we build the Discord bot.

Follow along with this section in my video to push the model. Also, remember to tag it as **conversational** in its Model Card (equivalently its `README.md`):

```pgsql
---
tags:
- conversational
---

# My Awesome Model
```

You will know that everything works fine if you are able to chat with the model in the browser.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/huggingface3.gif align="left")

## How to Build the Discord Bot

Go to the [Discord Developer's page](https://discord.com/developers/applications), create an application, and add a bot to it. Since our chatbot is only going to respond to user messages, checking **Text Permissions &gt; Send Messgaes** in the Bot Permissions Setting is sufficient. Copy the bot's API token for later use.

Sign up for [Repl.it](https://repl.it/) and create a new Repl, **Python** or **Node.js** for JavaScript, whichever you are working with.

Let's store our API tokens for **Hugging Face** and **Discord** as environment variables, named `HUGGINGFACE_TOKEN` and `DISCORD_TOKEN` respectively. This helps keep them secret.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/repl.png align="left")

Copy [my Python script](https://github.com/RuolinZheng08/twewy-discord-chatbot/blob/main/discord_bot.py) for a Python bot and [my JS script](https://github.com/RuolinZheng08/twewy-discord-chatbot/blob/main/discord_bot.js) for a JS bot. Note that for the JS bot, because of a version incompatibility with Repl.it's Node and NPM, we will need to explicitly specify a lower version of the Discord API in `package.json`.

```pgsql
"dependencies": {
    "discord.js": "^12.5.3",
}
```

With that, our bot is ready to go! Start the Repl script by hitting **Run**, add the bot to a server, type something in the channel, and enjoy the bot's witty response.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/discord-1.gif align="left")

## How to Keep the Bot Online

One problem with our bot is that it halts as soon as we **stop** the running Repl (equivalently, if we close the Repl.it browser window).

To get around this and keep our bot running indefinitely, we will set up a web server to contain the bot script, and use a service like [Uptime Robot](https://uptimerobot.com/) to pin our server every five minutes so that our server stays alive.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-25-at-15.29.06.png align="left")

In my video tutorial, I copied the server code from these two freeCodeCamp posts ([Python version](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/), [JavaScript version](https://www.freecodecamp.org/news/create-a-discord-bot-with-javascript-nodejs/)). Then, I set up the monitor on Uptime Robot. Now my bot continues to reply to my messages even if I close the browser (or shut down my computer all together).

Congratulations on reaching the end of this tutorial! I hope you enjoyed creating the bot and have fun chatting with your favorite character! 🥳

## Tutorial Video Link

%[https://youtu.be/Rk8eM1p_xgM] 

## More About Me and My Chatbot Project

I'm Lynn, a software engineer at Salesforce. I graduated from the University of Chicago in 2021 with a joint BS/MS in Computer Science, specializing in Machine Learning. [Come say hi on my personal website!](https://ruolinzheng08.github.io/)

I post fun project tutorials like this on my YouTube channel. Feel free to subscribe to catch up on my latest content. 😃

%[https://www.youtube.com/channel/UCZ2MeG5jTIqgzEMiByrIzsw] 

Want to learn more about my bot? Check out this 15-minute real-time chat demo featuring me, my friend, and my bot!

%[https://youtu.be/-n6uWu8PZzo] 

Interested in the model I trained? Check it out on Hugging Face:

%[https://huggingface.co/r3dhummingbird/DialoGPT-medium-joshua] 

My chatbot was so popular on a 1k+ user server that... it crashed. 🤯 Read about my deployment post-mortem in this post:

%[https://www.freecodecamp.org/news/recovering-from-deployment-hell-what-i-learned-from-deploying-my-discord-bot-to-a-1000-user-server/] 

Thanks for reading!
