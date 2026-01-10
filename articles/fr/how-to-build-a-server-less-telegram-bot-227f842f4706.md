---
title: J'ai construit un bot Telegram serverless ce week-end. Voici ce que j'ai appris.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-25T06:40:30.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-server-less-telegram-bot-227f842f4706
coverImage: https://cdn-media-1.freecodecamp.org/images/1*IU6691dCvEaCl46zvhZMrg.jpeg
tags:
- name: '#chatbots'
  slug: chatbots
- name: Python
  slug: python
- name: serverless
  slug: serverless
- name: startup
  slug: startup
- name: telegram
  slug: telegram
seo_title: J'ai construit un bot Telegram serverless ce week-end. Voici ce que j'ai
  appris.
seo_desc: 'By Moses Soh

  I built a Telegram chatbot that sends out a SOS to rescuers when someone is stranded
  in the rain. It’s written in Python using AWS Lambda, Zappa and Flask.

  You can try it here. I haven’t added in persistence yet ? but I think some of thi...'
---

Par Moses Soh

J'ai construit un bot Telegram qui envoie un SOS aux secours lorsqu'une personne est bloquée sous la pluie. Il est écrit en Python en utilisant AWS Lambda, Zappa et Flask.

Vous pouvez l'essayer [ici](https://t.me/UmbrellaNetworkBot). Je n'ai pas encore ajouté de persistance ? mais je pense que certaines de ces informations pourraient être utiles à toute personne intéressée par un projet similaire.

J'ai normalement du mal à faire discuter ma fiancée de technologie. C'est arrivé à un point où elle ne peut s'empêcher de bâiller dès que je dis « code ».

Imaginez ma surprise ce week-end quand elle m'a demandé — presque sans raison — combien cela coûterait de créer une application mobile.

Après avoir un peu réfléchi, voici ce que j'ai découvert.

### **Le problème**

Le lieu de travail de ma fiancée est proche de deux stations de MRT, mais il n'y a pas de chemins couverts depuis les stations de MRT jusqu'à son bâtiment. Quand il pleut, les personnes sans parapluie se retrouvent bloquées aux stations. Elle et ses collègues descendent souvent aider des amis, mais il y a souvent plus de personnes bloquées que prévu.

Ses collègues discutaient de savoir si une application pourrait aider à résoudre ce problème. Eh bien, j'ai pensé qu'un chatbot pourrait avoir les mêmes fonctions (comme envoyer une demande de parapluies, partager la localisation, recevoir des réponses). Et vous pourriez éviter de convaincre les gens de télécharger une autre application.

Puisque je voulais essayer les API de bot de Telegram depuis un moment, je me suis porté volontaire pour aider à construire un prototype afin que nous puissions voir à quel point cela pourrait être intéressant.

### Le chatbot

J'ai commencé à travailler sur cela samedi après-midi et je me suis couché à 2h du matin dimanche. Mais je suis vraiment heureux d'être passé de ne rien savoir sur les API de bot à être capable de faire quelque chose comme ça.

**N'importe qui peut demander un parapluie.** Le bot demande où se trouve la personne, combien de parapluies elle pourrait avoir besoin, et quand elle aimerait être récupérée (les options sont limitées pour ne pas trop solliciter nos secours).

![Image](https://cdn-media-1.freecodecamp.org/images/1*8fRnEXxnziTXq0_eCPFaJw.gif)
_C'est ce que fait le chatbot lorsque vous demandez un parapluie_

**Les personnes peuvent s'inscrire pour être secours.** Un peu de bon karma fait du bien ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*OTwyQWY2fa8j2-UbRNoR7A.gif)
_C'est ainsi que quelqu'un devient un secours_

**Les secours sont notifiés chaque fois que quelqu'un près d'eux est bloqué sous la pluie.** Je voulais que ce soit clair pour les secours s'ils étaient responsables de la demande une fois qu'ils avaient appuyé sur « Oui ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*HMzdeOZzu7wwGzunxn5rOg.gif)
_C'est ainsi qu'un secours reçoit et répond à une demande_

En cours de route, j'ai appris quelques astuces pour rendre le développement beaucoup plus rapide. J'ai passé presque six heures avant de trouver les bons outils et un flux de travail de développement qui fonctionnait pour moi. La construction de la logique du bot m'a pris beaucoup moins de temps.

### Ce que j'ai utilisé

#### AWS Lambda

Au lieu de faire tourner un serveur 24/7, vous pouvez héberger des fonctions dans Lambda de sorte que le serveur ne dure que pour le cycle de vie de la requête. C'est idéal pour les prototypes puisque vous obtenez 1 million de requêtes gratuites par mois.

#### Zappa

[Cela](https://github.com/Miserlou/Zappa) automatise les étapes nécessaires pour obtenir votre code Python local sur AWS Lambda. Il configure également la passerelle API d'Amazon pour que vous ayez un bel endpoint HTTPS pour héberger vos fonctions de chatbot.

#### ngrok

[Cela](https://ngrok.com/) rend tout serveur local accessible via Internet. C'est un excellent moyen de prototyper des webhooks avant de les déployer réellement dans le cloud.

Ces outils m'ont aidé à éviter beaucoup de maux de tête qui accompagnent la création d'un chatbot (par exemple, louer un serveur, le configurer pour HTTPS, comprendre comment rendre le serveur non bloquant puisque c'est un chatbot).

Aujourd'hui, je vais vous montrer comment j'ai utilisé ces outils pour développer le chatbot ci-dessus. J'espère que cela aidera quelqu'un d'autre dans un voyage similaire.

### Guide pratique

Ce tutoriel suppose que vous créez un chatbot sans connaître le fonctionnement de l'API de bot de Telegram, mais avec une connaissance pratique de Flask et Python. Si quelque chose vous semble trop simple, n'hésitez pas à passer à la suite !

#### Créer un bot Telegram

Visitez le [Botfather](https://t.me/botfather). Tapez `/newbot` et suivez ses instructions pour configurer un nouveau bot.

![Image](https://cdn-media-1.freecodecamp.org/images/1*j6lJlDAPADGvjhFlhrOQGA.png)
_Et voilà, nous avons un chatbot configuré sur Telegram !_

⚡ **Astuce pro :** sauvegardez le token quelque part, nous allons l'utiliser bientôt !

N'hésitez pas à jouer avec l'image de profil du bot, le texte de présentation et la description pour lui donner la personnalité que vous souhaitez. Taper `/help` avec le Botfather vous donne la liste complète des paramètres que vous pouvez ajuster pour votre bot.

#### Configurer un serveur de développement avec Flask

J'ai travaillé avec [pipenv](https://github.com/kennethreitz/pipenv) pour gérer les dépendances Python de mon projet. Si vous utilisez encore pip et virtualenv, je vous encourage à essayer cela. Il y a des instructions d'installation à ce lien.

Ensuite, nous installerons [Flask](http://flask.pocoo.org/). Nous utiliserons également la bibliothèque [requests](http://docs.python-requests.org/en/master/). Dans votre ligne de commande, tapez :

```
pipenv install flask
pipenv install requests
```

Après l'installation de Flask, nous configurerons un serveur de base pour tester notre bot. Copiez le texte suivant dans un fichier appelé `server.py`.

⚡ **Astuce pro :** Assurez-vous de remplacer `<your-bot-token>` par le token API que nous avons obtenu du Botfather.

Décomposons ce que cela fait. L'API de Telegram fonctionne de cette manière. Tout d'abord, lorsqu'une personne envoie un message à votre bot, ce message est envoyé aux serveurs de Telegram. Telegram nous transmet ensuite ce message à l'adresse que nous spécifions comme notre webhook sous forme de requête POST.

La fonction `process_update()` et le décorateur au-dessus indiquent que lorsque quelqu'un POSTe sur le domaine `[http://127.0.0.1:5000](http://127.0.0.1:5000)/<your-bot-token>`, nous allons extraire les données JSON. Si c'est un message texte normal, il aura la clé `message` dans le JSON. Nous vérifions cela et si c'est un message normal, nous répondons en utilisant `process_message(update)`.

La fonction `process_message()` construit la charge utile que l'API Telegram attend si nous voulons répondre au message. Nous devons essentiellement spécifier notre texte de réponse dans `data["text"]` et le chat auquel nous répondons dans `data["chat_id"]`.

Enfin, nous envoyons une requête POST avec cette charge utile à l'[endpoint de l'API Telegram pour la méthode `sendMessage`](https://core.telegram.org/bots/api#sendmessage). Cela nous permet d'envoyer un message de manière programmatique.

**Il est temps de lancer le serveur.** Maintenant, dans votre invite de commande, tapez :

```
pipenv shell
```

Cela active l'environnement virtuel et nous donne accès à Flask. Maintenant, nous devons lancer le serveur localement. Tapez dans l'invite de commande :

```
export FLASK_APP=server.py
flask run
```

Nous avons un serveur en cours d'exécution ! Si vous n'avez pas modifié les paramètres par défaut, cela s'exécute sur [http://127.0.0.1:5000](http://127.0.0.1:5000)/.

Lisez plus dans la documentation Flask et le [guide de démarrage rapide](http://flask.pocoo.org/docs/0.12/quickstart/).

Mais cela s'exécute localement, et l'API de bot de Telegram ne peut pas envoyer ses requêtes POST à une URL locale. Nous allons donc utiliser **ngrok** pour exposer ce serveur local à Internet.

#### Utiliser ngrok pour rendre le serveur local accessible sur Internet

Obtenez le package pour votre système d'exploitation à partir de [ce lien sur le site web de ngrok](https://ngrok.com/download). Une fois que vous l'avez téléchargé et installé, allez dans le répertoire où vous avez décompressé le fichier et exécutez la commande suivante dans l'invite de commande.

```
./ngrok http 5000
```

Vous verrez quelque chose de similaire dans votre invite de commande. Maintenant, tout serveur que vous exécutez sur localhost:5000 est exposé aux URL suivantes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ajbuzROMpw1Tpkqhj1BPfQ.png)

⚡ **Astuce pro :** Copiez l'URL https, nous allons l'utiliser bientôt.

**Il est temps de faire savoir à Telegram quelle est notre adresse de webhook.** Nous allons utiliser à nouveau l'API Telegram pour définir notre webhook.

Créez un fichier appelé `webhook.py` avec le contenu suivant :

⚡ **Astuce pro :** N'oubliez pas de remplacer `<your-bot-token>` et `<your-https-url>` !

`pprint` nous permet d'imprimer des données JSON bien formatées. Nous envoyons notre URL de webhook sous forme de requête POST à l'[endpoint](https://core.telegram.org/bots/api#setwebhook) `setWebhook` de l'API Telegram. Maintenant, exécutez les lignes suivantes dans votre invite de commande :

```
pipenv install pprint
python webhook.py
```

Vous devriez voir `200` et un bloc JSON avec `'ok': True`.

#### Testez votre chatbot

Maintenant, nous avons terminé la configuration de notre serveur. Rendez-vous sur votre bot dans Telegram et dites bonjour ! Si tout a été configuré correctement, vous verrez qu'il répond `Je peux vous entendre !`

Dans la prochaine partie de ce tutoriel, nous apprendrons comment déployer ce serveur sur Internet en utilisant Zappa et AWS Lambda. Donnez quelques applaudissements si cela vous a été utile — j'adorerais savoir si c'était le cas. Merci ?