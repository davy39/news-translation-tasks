---
title: How to Build and Deploy a python-telegram-bot v20 Webhook
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-11-20T20:43:21.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-and-deploy-python-telegram-bot-v20-webhooks
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/iPhone-8---1--1-.png
tags:
- name: bots
  slug: bots
- name: Python
  slug: python
- name: webhooks
  slug: webhooks
seo_title: null
seo_desc: 'By Chua Hui Shun

  The python-telegram-bot v20 release introduced major structural changes. According
  to the documentation,


  “All networking and I/O-related logic now works via coroutine functions (i.e. _async
  def ..._ functions). In particular, all me...'
---

By Chua Hui Shun

The python-telegram-bot v20 release introduced major structural changes. According to the documentation,

> “All networking and I/O-related logic now works via coroutine functions (i.e. `_async def ..._` functions). In particular, all methods of the `_telegram.Bot_` class that make requests to the Bot API are now coroutine functions and need to be `await`-ed.” — [python-telegram-bot v20 change logs](https://telegra.ph/Release-notes-for-python-telegram-bot-v200a0-05-06)

The process of transitioning from python-telegram-bot version 13 to version 20 turned out to be more complex than I had originally anticipated. Converting synchronous `def` functions to `async def` and adding `await` to new coroutines was fairly easy. But the main difficulty was finding detailed documentation on how to **build and deploy python-telegram-bot v20 webhooks in a production setting**.

This article explains why and how I migrated from:

1. python-telegram-bot v13 → v20
2. Flask → FastAPI
3. Gunicorn → Gunicorn + Uvicorn

## Why Upgrade from v13 to v20?

v13.x and older are [no longer supported](https://stackoverflow.com/questions/76196067/the-python-telegram-bot-library-does-not-see-messages-in-a-group) by the python-telegram-bot dev team. If Telegram API introduces any new features, they will only be available on v20 and above.

### Why Use a Webhook and Not Polling?

Most examples provided by the python-telegram-bot dev team use `Application.run_polling`. But webhooks are generally recommended over polling for most Telegram bot use cases, because polling requires your bot to constantly make requests to Telegram’s servers, which can consume significant resources. On the other hand, webhooks offer [extended functionality](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Frequently-requested-design-patterns#running-ptb-alongside-other-asyncio-frameworks), update faster, and scale better.

## The Challenge of using Flask with python-telegram-bot v20

### Using a WGSI like Flask with python-telegram-bot v20 is awkward.

Flask, a WSGI (Web Server Gateway Interface), is synchronous and can handle only one request at a time. But you can still [run async functions in Flask](https://www.reddit.com/r/flask/comments/xvw1vi/misunderstandings_about_how_async_works_with/) using `asyncio.run()`, as in the [custom webhook bot example](https://docs.python-telegram-bot.org/en/v20.6/examples.customwebhookbot.html) provided by the python-telegram-bot dev team. 

`asyncio.run()` starts an event loop and executes the given coroutine until it completes. If there are any asynchronous tasks running before or after the request is handled, those tasks will be executed in a separate event loop.

```python
# Code snippet from https://docs.python-telegram-bot.org/en/v20.6/examples.customwebhookbot.html

webserver = uvicorn.Server(
    config=uvicorn.Config(
        app=WsgiToAsgi(flask_app),
        port=PORT,
        use_colors=False,
        host="127.0.0.1",
    )
)

async with application:
  await application.start()
  await webserver.serve() # start bot's webserver
  await application.stop()
```

However, this implementation is slightly awkward because Flask is intrinsically [incompatible with async globals](https://sethmlarson.dev/flask-async-views-and-async-globals).

### Examples in the [documentation](https://docs.python-telegram-bot.org/en/v20.6/examples.customwebhookbot.html) are not suitable for production environments.

Using `asyncio.run()` as an entry point in production is usually not recommended. The `asyncio.run()` function is designed for development and testing purposes, and it may not provide the same level of robustness and reliability as production servers like Gunicorn or UWSGI. 

These production servers offer many additional features, such as logging, monitoring, and health checks, which are essential for ensuring the stability and security of a production application.

If you want to deploy your bot in production, it’s much cleaner to use an ASGI (Asynchronous Server Gateway Interface) with an ASGI web server implementation.

## How to Do It — Migration and Deployment

### From Flask (WSGI) to FastAPI (AGSI)

Migrating a Flask application to an ASGI is straightforward. I chose FastAPI because I found a comprehensive migration tutorial [here](https://testdriven.io/blog/moving-from-flask-to-fastapi/). The syntaxes of both frameworks are quite similar, which means you won’t have to make too many code changes.

```python
# From python-telegram-bot v20
application = (
    Application.builder()
    .updater(None)
    .token(<your-bot-token>) # replace <your-bot-token>
    .read_timeout(7)
    .get_updates_read_timeout(42)
    .build()
)

# From FastAPI
@asynccontextmanager
async def lifespan(app: FastAPI):
    async with application:
        await application.start()
        yield
        await application.stop()
```

Quart appears to be a feasible alternative, but it [does not offer support](https://pgjones.gitlab.io/quart/tutorials/deployment.html) for deployments using Uvicorn, which is the webserver implementation I was adapting from the [script](https://docs.python-telegram-bot.org/en/v20.6/examples.customwebhookbot.html) provided by the python-telegram-bot team.

### A working example

The following code shows a minimal example that uses FastAPI to build a python-telegram-bot v20 webhook. This bot will respond with “starting…” when it receives the `/start` command.

```python
# main.py

from contextlib import asynccontextmanager
from http import HTTPStatus
from telegram import Update
from telegram.ext import Application, CommandHandler
from telegram.ext._contexttypes import ContextTypes
from fastapi import FastAPI, Request, Response

# Initialize python telegram bot
ptb = (
    Application.builder()
    .updater(None)
    .token(<your-bot-token>) # replace <your-bot-token>
    .read_timeout(7)
    .get_updates_read_timeout(42)
    .build()
)

@asynccontextmanager
async def lifespan(_: FastAPI):
    await ptb.bot.setWebhook(<your-webhook-url>) # replace <your-webhook-url>
    async with ptb:
        await ptb.start()
        yield
        await ptb.stop()

# Initialize FastAPI app (similar to Flask)
app = FastAPI(lifespan=lifespan)

@app.post("/")
async def process_update(request: Request):
    req = await request.json()
    update = Update.de_json(req, ptb.bot)
    await ptb.process_update(update)
    return Response(status_code=HTTPStatus.OK)

# Example handler
async def start(update, _: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /start is issued."""
    await update.message.reply_text("starting...")

ptb.add_handler(CommandHandler("start", start))
```

To start the bot, pip install all required dependencies and run the start command: `gunicorn main:app -k uvicorn.workers.UvicornWorker`.

This code snippet is adapted from a real Telegram bot in production. Check out the source code for [@cron_telebot](https://t.me/cron_telebot) [here](https://github.com/hsdevelops/cron-telebot) to see how it is implemented. Feel free to adapt the script to suit your use case.

## Conclusion

In this article, we learnt how to build and deploy a python-telegram-bot v20 webhook.

Hope this tutorial helped you. If you enjoyed this article, please [follow me on Medium](https://huishun.medium.com/) to show your support. 

Thank you for reading!

