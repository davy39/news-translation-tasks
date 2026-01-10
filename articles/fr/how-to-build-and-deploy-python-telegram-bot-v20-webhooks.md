---
title: Comment construire et déployer un webhook python-telegram-bot v20
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-11-20T20:43:21.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-and-deploy-python-telegram-bot-v20-webhooks
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/iPhone-8
seo_title: Comment construire et déployer un webhook python-telegram-bot v20
---

1--1-.png
étiquettes:
- name: bots
  slug: bots
- name: Python
  slug: python
- name: webhooks
  slug: webhooks
seo_title: null
seo_desc: 'Par Chua Hui Shun

  La version v20 de python-telegram-bot a introduit des changements structurels majeurs. Selon
  la documentation,


  «Toute la logique réseau et d'E/S fonctionne désormais via des fonctions coroutine (c'est-à-dire des fonctions _async
  def ..._). En particulier, toutes les méthodes de la classe _telegram.Bot_ qui font des requêtes à l'API Bot sont désormais des fonctions coroutine et doivent être `await`-ées.»—[journal des changements de python-telegram-bot v20](https://telegra.ph/Release-notes-for-python-telegram-bot-v200a0-05-06)

Le processus de transition de la version 13 à la version 20 de python-telegram-bot s'est avéré plus complexe que je ne l'avais initialement anticipé. Convertir les fonctions synchrones `def` en `async def` et ajouter `await` aux nouvelles coroutines était relativement facile. Mais la principale difficulté était de trouver une documentation détaillée sur la façon de **construire et déployer des webhooks python-telegram-bot v20 dans un environnement de production**.

Cet article explique pourquoi et comment j'ai migré depuis :

1. python-telegram-bot v13 → v20
2. Flask → FastAPI
3. Gunicorn → Gunicorn + Uvicorn

## Pourquoi passer de la v13 à la v20 ?

Les versions v13.x et antérieures ne sont [plus supportées](https://stackoverflow.com/questions/76196067/the-python-telegram-bot-library-does-not-see-messages-in-a-group) par l'équipe de développement de python-telegram-bot. Si l'API Telegram introduit de nouvelles fonctionnalités, elles ne seront disponibles que sur la v20 et au-delà.

### Pourquoi utiliser un Webhook et non le Polling ?

La plupart des exemples fournis par l'équipe de développement de python-telegram-bot utilisent `Application.run_polling`. Mais les webhooks sont généralement recommandés plutôt que le polling pour la plupart des cas d'utilisation des bots Telegram, car le polling nécessite que votre bot fasse constamment des requêtes aux serveurs de Telegram, ce qui peut consommer des ressources significatives. D'autre part, les webhooks offrent une [fonctionnalité étendue](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Frequently-requested-design-patterns#running-ptb-alongside-other-asyncio-frameworks), des mises à jour plus rapides et une meilleure scalabilité.

## Le défi d'utiliser Flask avec python-telegram-bot v20

### Utiliser un WSGI comme Flask avec python-telegram-bot v20 est maladroit.

Flask, un WSGI (Web Server Gateway Interface), est synchrone et ne peut gérer qu'une seule requête à la fois. Mais vous pouvez toujours [exécuter des fonctions asynchrones dans Flask](https://www.reddit.com/r/flask/comments/xvw1vi/misunderstandings_about_how_async_works_with/) en utilisant `asyncio.run()`, comme dans l'exemple de [bot webhook personnalisé](https://docs.python-telegram-bot.org/en/v20.6/examples.customwebhookbot.html) fourni par l'équipe de développement de python-telegram-bot.

`asyncio.run()` démarre une boucle d'événements et exécute la coroutine donnée jusqu'à ce qu'elle soit terminée. Si des tâches asynchrones sont en cours d'exécution avant ou après que la requête soit traitée, ces tâches seront exécutées dans une boucle d'événements séparée.

```python
# Extrait de code de https://docs.python-telegram-bot.org/en/v20.6/examples.customwebhookbot.html

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
  await webserver.serve() # démarrer le serveur web du bot
  await application.stop()
```

Cependant, cette implémentation est légèrement maladroite car Flask est intrinsèquement [incompatible avec les globals async](https://sethmlarson.dev/flask-async-views-and-async-globals).

### Les exemples dans la [documentation](https://docs.python-telegram-bot.org/en/v20.6/examples.customwebhookbot.html) ne sont pas adaptés aux environnements de production.

Utiliser `asyncio.run()` comme point d'entrée en production n'est généralement pas recommandé. La fonction `asyncio.run()` est conçue pour le développement et les tests, et elle peut ne pas offrir le même niveau de robustesse et de fiabilité que les serveurs de production comme Gunicorn ou UWSGI.

Ces serveurs de production offrent de nombreuses fonctionnalités supplémentaires, telles que la journalisation, la surveillance et les vérifications de santé, qui sont essentielles pour garantir la stabilité et la sécurité d'une application de production.

Si vous souhaitez déployer votre bot en production, il est beaucoup plus propre d'utiliser un ASGI (Asynchronous Server Gateway Interface) avec une implémentation de serveur web ASGI.

## Comment faire — Migration et Déploiement

### De Flask (WSGI) à FastAPI (ASGI)

Migrer une application Flask vers un ASGI est simple. J'ai choisi FastAPI car j'ai trouvé un tutoriel de migration complet [ici](https://testdriven.io/blog/moving-from-flask-to-fastapi/). Les syntaxes des deux frameworks sont assez similaires, ce qui signifie que vous n'aurez pas à faire trop de changements de code.

```python
# De python-telegram-bot v20
application = (
    Application.builder()
    .updater(None)
    .token(<votre-token-de-bot>) # remplacer <votre-token-de-bot>
    .read_timeout(7)
    .get_updates_read_timeout(42)
    .build()
)

# De FastAPI
@asynccontextmanager
async def lifespan(app: FastAPI):
    async with application:
        await application.start()
        yield
        await application.stop()
```

Quart semble être une alternative réalisable, mais il [n'offre pas de support](https://pgjones.gitlab.io/quart/tutorials/deployment.html) pour les déploiements utilisant Uvicorn, qui est l'implémentation de serveur web que j'adaptais du [script](https://docs.python-telegram-bot.org/en/v20.6/examples.customwebhookbot.html) fourni par l'équipe python-telegram-bot.

### Un exemple fonctionnel

Le code suivant montre un exemple minimal qui utilise FastAPI pour construire un webhook python-telegram-bot v20. Ce bot répondra par « démarrage... » lorsqu'il recevra la commande `/start`.

```python
# main.py

from contextlib import asynccontextmanager
from http import HTTPStatus
from telegram import Update
from telegram.ext import Application, CommandHandler
from telegram.ext._contexttypes import ContextTypes
from fastapi import FastAPI, Request, Response

# Initialiser le bot telegram python
ptb = (
    Application.builder()
    .updater(None)
    .token(<votre-token-de-bot>) # remplacer <votre-token-de-bot>
    .read_timeout(7)
    .get_updates_read_timeout(42)
    .build()
)

@asynccontextmanager
async def lifespan(_: FastAPI):
    await ptb.bot.setWebhook(<votre-url-de-webhook>) # remplacer <votre-url-de-webhook>
    async with ptb:
        await ptb.start()
        yield
        await ptb.stop()

# Initialiser l'application FastAPI (similaire à Flask)
app = FastAPI(lifespan=lifespan)

@app.post("/")
async def process_update(request: Request):
    req = await request.json()
    update = Update.de_json(req, ptb.bot)
    await ptb.process_update(update)
    return Response(status_code=HTTPStatus.OK)

# Exemple de gestionnaire
async def start(update, _: ContextTypes.DEFAULT_TYPE):
    """Envoyer un message lorsque la commande /start est émise."""
    await update.message.reply_text("démarrage...")

ptb.add_handler(CommandHandler("start", start))
```

Pour démarrer le bot, installez toutes les dépendances requises avec pip et exécutez la commande de démarrage : `gunicorn main:app -k uvicorn.workers.UvicornWorker`.

Cet extrait de code est adapté d'un vrai bot Telegram en production. Consultez le code source de [@cron_telebot](https://t.me/cron_telebot) [ici](https://github.com/hsdevelops/cron-telebot) pour voir comment il est implémenté. N'hésitez pas à adapter le script à votre cas d'utilisation.

## Conclusion

Dans cet article, nous avons appris comment construire et déployer un webhook python-telegram-bot v20.

J'espère que ce tutoriel vous a aidé. Si vous avez aimé cet article, veuillez [me suivre sur Medium](https://huishun.medium.com/) pour montrer votre soutien.

Merci pour votre lecture !