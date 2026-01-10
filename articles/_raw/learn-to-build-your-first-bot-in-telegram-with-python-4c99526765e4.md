---
title: Learn to build your first bot in Telegram with Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-13T14:40:49.000Z'
originalURL: https://freecodecamp.org/news/learn-to-build-your-first-bot-in-telegram-with-python-4c99526765e4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*vUK3nWPkSEJVAFRLLJbxHA.jpeg
tags:
- name: api
  slug: api
- name: bots
  slug: bots
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: Software Engineering
  slug: software-engineering
seo_title: null
seo_desc: 'By Dzaky Widya Putra

  Imagine this, there is a message bot that will send you a random cute dog image
  whenever you want, sounds cool right? Let’s make one!

  For this tutorial, we are going to use Python 3, python-telegram-bot, and public
  API RandomDog....'
---

By Dzaky Widya Putra

Imagine this, there is a message bot that will send you a random cute dog image whenever you want, sounds cool right? Let’s make one!

For this tutorial, we are going to use **Python 3, [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot),** and public API [**RandomDog**](https://random.dog/)**.**

At the end of this tutorial, you will have a stress relieving bot that will send you cute dog images every time you need it, yay!

### Getting started

Before we start to write the program, we need to generate a token for our bot. The token is needed to access the Telegram API, and install the necessary dependencies.

#### 1. Create a new bot in BotFather

If you want to make a bot in Telegram, you have to “register” your bot first before using it. When we “register” our bot, we will get the token to access the Telegram API.

Go to the [BotFather](https://telegram.me/BotFather) (if you open it in desktop, make sure you have the Telegram app), then create new bot by sending the `/newbot` command. Follow the steps until you get the username and token for your bot. You can go to your bot by accessing this URL: `[https://telegram.me/YOUR_BOT_USERNAME](https://telegram.me/YOUR_BOT_USERNAMEa)` and your token should looks like this.

```
704418931:AAEtcZ*************
```

#### 2. Install the library

Since we are going to use a library for this tutorial, install it using this command.

```
pip3 install python-telegram-bot
```

If the library is successfully installed, then we are good to go.

### Write the program

Let’s make our first bot. This bot should return a dog image when we send the `/bop` command. To be able to do this, we can use the public API from [**RandomDog**](https://random.dog/) to help us generate random dog images.

The workflow of our bot is as simple as this:

> access the API -> get the image URL -> send the image

#### 1. Import the libraries

First, import all the libraries we need.

```py
from telegram.ext import Updater, CommandHandler
import requests
import re
```

#### 2. Access the API and get the image URL

Let’s create a function to get the URL. Using the requests library, we can access the API and get the json data.

```
contents = requests.get('https://random.dog/woof.json').json()
```

You can check the json data by accessing that URL: `https://random.dog/woof.json` in your browser. You will see something like this on your screen:

```
{“url":"https://random.dog/*****.JPG"}
```

Get the image URL since we need that parameter to be able to send the image.

```
image_url = contents['url']
```

Wrap this code into a function called `get_url()` .

```py
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
```

#### 3. Send the image

To send a message/image we need two parameters, the image URL and the recipient’s ID — this can be group ID or user ID.

We can get the image URL by calling our `get_url()` function.

```
url = get_url()
```

Get the recipient’s ID using this code:

```
chat_id = update.message.chat_id
```

After we get the image URL and the recipient’s ID, it’s time to send the message, which is an image.

```
bot.send_photo(chat_id=chat_id, photo=url)
```

Wrap that code in a function called `bop` , and make sure your code looks like this:

```py
def bop(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
```

#### 4. `Main program`

Lastly, create another function called `main` to run our program. **Don’t forget to change** `YOUR_TOKEN` with the token that we generated earlier in this tutorial.

```py
def main():
    updater = Updater('YOUR_TOKEN')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()
```

At the end your code should look like this:

```py
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

def bop(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def main():
    updater = Updater('YOUR_TOKEN')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
```

#### 5. Run the program

Awesome! You finished your first program. Now let’s check if it works. Save the file, name it `main.py` , then run it using this command.

```
python3 main.py
```

Go to your telegram bot by accessing this URL: `https://telegram.me/YOUR_BOT_USERNAME`. Send the `/bop` command. If everything runs perfectly the bot will reply with a random dog image. Cute right?

![Image](https://cdn-media-1.freecodecamp.org/images/cgojJGcVwIVamFkYrpcRzrOOBJ0xFB0cTkTP)
_One random generatedly image_

### Handling errors

Great! Now you have a bot that will send you a cute dog image whenever you want.

There is more! The [**RandomDog**](https://random.dog/) API not only generates images, but also videos and GIFs. If we access the API and we get a video or GIF, there is an error and the bot won’t send it to you.

Let’s fix this so the bot will only send a message with an image attachment. If we get a video or GIF then we will call the API again until we get an image.

#### 1. Match the file extension using regex

We are going to use a regex to solve this problem.

To distinguish an image from video or GIF, we can take a look at the file extension. We only need the last part of our URL.

```
https://random.dog/*****.JPG
```

We need to define, first, what file extensions are allowed in our program.

```
allowed_extension = ['jpg','jpeg','png']
```

Then use the regex to extract the file extension from the URL.

```
file_extension = re.search("([^.]*)$",url).group(1).lower()
```

Using that code, make a function called `get_image_url()` to iterate the URL until we get the file extension that we want (jpg,jpeg,png).

```py
def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url
```

#### 2. Modify your code

Great! Now for the last part, replace the `url = get_url()` line in the `bop()` function with `url = get_image_url()` , and your code should look like this:

```py
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

def bop(bot, update):
    url = get_image_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def main():
    updater = Updater('YOUR_TOKEN')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
```

Nice! Everything should run perfectly. You can also check out my [GitHub](https://github.com/dzakyputra/doggobot) account to get the code.

Finally, congratulations for finishing this tutorial, plus you have a cool Telegram bot now.

Please leave a comment if you think there are any errors in my code or writing, because I’m still learning and I want to get better.

Thank you and good luck practicing! :)

