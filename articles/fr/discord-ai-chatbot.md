---
title: Comment créer un chatbot Discord IA qui parle comme votre personnage préféré
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
seo_title: Comment créer un chatbot Discord IA qui parle comme votre personnage préféré
seo_desc: 'Would you like to talk to a chatbot that speaks like your favorite character,
  fictional or non-fictional? Let''s build one!

  In case you''ve seen my previous tutorial on this topic, stick with me as this version
  features lots of updates.

  You can follow ...'
---

Aimeriez-vous parler à un chatbot qui parle comme votre personnage préféré, fictif ou non ? Construisons-en un !

Si vous avez vu mon précédent tutoriel sur ce sujet, restez avec moi car cette version contient de nombreuses mises à jour.

Vous pouvez suivre ce tutoriel en utilisant le code sur mon GitHub :

%[https://github.com/RuolinZheng08/twewy-discord-chatbot]

Si vous le souhaitez, vous pouvez plonger directement dans mon tutoriel vidéo sur YouTube – ou continuer à lire pour plus de détails. 😊

%[https://youtu.be/Rk8eM1p_xgM]

## À quoi s'attendre dans ce tutoriel

Voici un exemple du chatbot Discord IA que nous aurons construit à la fin de ce tutoriel.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/discord.gif align="left")

*Démonstration de chat avec mon bot sur Discord. J'ai dessiné l'icône du bot 😊*

Mon projet de chatbot a commencé comme une blague avec un ami lorsque nous jouions à des jeux vidéo.

Je suis honnêtement surpris de sa popularité – il y a eu 5,9k vues de mon précédent tutoriel, et lorsque j'ai déployé mon bot sur un serveur de 1k+ utilisateurs, les gens l'ont submergé de 300+ messages en une heure, provoquant ainsi son crash. 😳 Vous pouvez [lire plus sur mon post-mortem de déploiement dans cet article](https://www.freecodecamp.org/news/recovering-from-deployment-hell-what-i-learned-from-deploying-my-discord-bot-to-a-1000-user-server/).

Puisque beaucoup de gens sont intéressés à construire leurs propres bots basés sur leurs personnages préférés, j'ai mis à jour mon tutoriel pour inclure une explication approfondie sur la manière de collecter des données textuelles pour n'importe quel personnage, fictif ou non.

Vous pouvez également créer un ensemble de données personnalisé qui capture les échanges entre vous et vos amis et construire un chatbot qui parle comme vous !

D'autres mises à jour dans ce tutoriel abordent les changements dans les services d'hébergement de modèles de Hugging Face, y compris les modifications de l'API qui affectent la manière dont nous poussons le modèle vers les dépôts de modèles de Hugging Face.

## Plan de ce tutoriel

La version vidéo de ce tutoriel dure une heure au total et aborde les sujets suivants :

1. Collecter des données textuelles pour votre personnage en utilisant l'une de ces deux méthodes : trouver des ensembles de données pré-construits sur **Kaggle** ou créer des ensembles de données personnalisés à partir de transcriptions brutes.

2. Entraîner le modèle dans **Google Colab**, un environnement Jupyter Notebook basé sur le cloud avec des GPU gratuits.

3. Déployer le modèle sur **Hugging Face**, un service d'hébergement de modèles d'IA.

4. Construire un bot Discord en **Python** ou **JavaScript**, au choix ! 🤩

5. Configurer les permissions du bot Discord pour qu'il ne spamme pas les canaux non-bot.

6. Héberger le bot sur **Repl.it**.

7. Garder le bot en ligne indéfiniment avec **Uptime Robot**.

Pour en savoir plus sur la construction de bots Discord, vous pouvez également trouver ces deux articles de freeCodeCamp utiles – il y a une [version Python](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/) et une [version JavaScript](https://www.freecodecamp.org/news/create-a-discord-bot-with-javascript-nodejs/).

## Comment préparer les données

Pour que notre chatbot apprenne à converser, nous avons besoin de données textuelles sous forme de dialogues. C'est essentiellement ainsi que notre chatbot va répondre à différents échanges et contextes.

### Votre personnage préféré est-il sur Kaggle ?

Il existe de nombreux ensembles de données intéressants sur Kaggle pour des dessins animés, émissions de télévision et autres médias populaires. Par exemple :

* [Rick and Morty](https://www.kaggle.com/andradaolteanu/rickmorty-scripts)

* [Harry Potter](https://www.kaggle.com/gulsahdemiryurek/harry-potter-dataset?select=Harry+Potter+1.csv)

* [The Big Bang Theory](https://www.kaggle.com/mitramir5/the-big-bang-theory-series-transcript)

* [Game of Thrones](https://www.kaggle.com/anderfj/game-of-thrones-series-scripts-breakdowns)

Nous n'avons besoin que de deux colonnes de ces ensembles de données : **nom du personnage** et **ligne de dialogue**.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-25-at-14.07.59.png align="left")

*Exemple de jeu de données : transcription du film Harry Potter*

### Vous ne trouvez pas votre personnage préféré sur Kaggle ?

Vous ne trouvez pas votre personnage préféré sur Kaggle ? Pas de problème. Nous pouvons créer des ensembles de données à partir de transcriptions brutes. Un excellent endroit pour chercher des transcriptions est [Transcript Wiki](https://transcripts.fandom.com/wiki/Transcripts_Wiki). Par exemple, consultez [cette transcription de Peppa Pig](https://transcripts.fandom.com/wiki/Peppa_Pig).

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-25-at-14.13.57.png align="left")

*Exemple : transcription de Peppa Pig*

En utilisant une expression régulière comme `([a-zA-Z|\s]+): (.+)`, nous pouvons extraire les deux colonnes d'intérêt, le nom du personnage et la ligne de dialogue.

[Essayez-le vous-même sur ce site de regex Python !](https://pythex.org/?regex=\(%5Ba-zA-Z%7C%5Cs%5D%2B\)%3A%20\(.%2B\)&test_string=Peppa%20Pig%3A%20George%2C%20I%20could%20see%20you%20too%20easily.%0A%0ANarrator%3A%20Now%20it%20is%20Peppa%27s%20turn%20to%20hide.%0A%0AGeorge%3A%20One...%20um...%20three.%0A%0AMummy%20Pig%3A%20I%27ll%20help%20George%20to%20count.%20&ignorecase=0&multiline=0&dotall=0&verbose=0)

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-25-at-14.58.35.png align="left")

## Comment entraîner le modèle

Sous le capot, notre modèle sera un **Generative Pre-trained Transformer (GPT)**, le modèle de langage le plus populaire ces jours-ci.

Au lieu d'entraîner à partir de zéro, nous allons charger [le GPT pré-entraîné de Microsoft](https://huggingface.co/microsoft/DialoGPT-small), `DialoGPT-small`, et l'affiner en utilisant notre ensemble de données.

Mon dépôt GitHub pour ce tutoriel contient [le fichier notebook](https://github.com/RuolinZheng08/twewy-discord-chatbot/blob/main/model_train_upload_workflow.ipynb) nommé `model_train_upload_workflow.ipynb` pour vous aider à démarrer. Tout ce que vous avez à faire est ce qui suit : (veuillez vous référer à la vidéo pour un guide détaillé)

1. Téléchargez le fichier sur [Google Colab](https://colab.research.google.com/)

2. Sélectionnez **GPU** comme environnement d'exécution, ce qui accélérera notre entraînement de modèle.

3. Changez l'ensemble de données et le personnage cible dans des extraits de code comme :

```python
data = pd.read_csv('MON-DATASET.csv')
CHARACTER_NAME = 'MON-PERSONNAGE'
```

L'exécution de la section d'entraînement du notebook devrait prendre moins de trente minutes. J'ai environ 700 lignes et l'entraînement prend moins de dix minutes. Le modèle sera stocké dans un dossier nommé `output-small`.

Vous voulez un modèle encore plus intelligent et plus éloquent ? N'hésitez pas à entraîner un modèle plus grand comme `DialoGPT-medium` ou même `DialoGPT-large`. La taille du modèle ici fait référence au nombre de paramètres dans le modèle. Plus de paramètres permettront au modèle de capter plus de complexité à partir de l'ensemble de données.

Vous pouvez également augmenter le nombre d'époques d'entraînement en recherchant `num_train_epochs` dans le notebook. Il s'agit du nombre de fois que le modèle va parcourir l'ensemble de données d'entraînement. Le modèle deviendra généralement plus intelligent lorsqu'il aura plus d'exposition à l'ensemble de données.

Cependant, faites attention à ne pas sur-entraîner le modèle : si le modèle est entraîné pendant trop d'époques, il peut mémoriser l'ensemble de données et réciter des lignes de l'ensemble de données lorsque nous essayons de converser avec lui. Ce n'est pas idéal car nous voulons que la conversation soit plus organique.

## Comment héberger le modèle

Nous allons héberger le modèle sur Hugging Face, qui fournit une API gratuite pour interroger le modèle.

Inscrivez-vous sur [Hugging Face](https://huggingface.co/) et créez un nouveau dépôt de modèle en cliquant sur **New model**. Obtenez votre jeton API en allant dans **Edit profile > API Tokens**. Nous aurons besoin de ce jeton lorsque nous construirons le bot Discord.

Suivez cette section dans ma vidéo pour pousser le modèle. N'oubliez pas non plus de le taguer comme **conversational** dans sa Carte de Modèle (équivalemment son `README.md`) :

```pgsql
---
tags:
- conversational
---

# Mon Modèle Génial
```

Vous saurez que tout fonctionne bien si vous êtes en mesure de discuter avec le modèle dans le navigateur.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/huggingface3.gif align="left")

## Comment construire le bot Discord

Allez sur la [page des développeurs de Discord](https://discord.com/developers/applications), créez une application et ajoutez un bot à celle-ci. Puisque notre chatbot ne va répondre qu'aux messages des utilisateurs, cocher **Text Permissions > Send Messages** dans les paramètres des permissions du bot est suffisant. Copiez le jeton API du bot pour une utilisation ultérieure.

Inscrivez-vous sur [Repl.it](https://repl.it/) et créez un nouveau Repl, **Python** ou **Node.js** pour JavaScript, selon ce avec quoi vous travaillez.

Stockez nos jetons API pour **Hugging Face** et **Discord** comme variables d'environnement, nommées `HUGGINGFACE_TOKEN` et `DISCORD_TOKEN` respectivement. Cela aide à les garder secrets.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/repl.png align="left")

Copiez [mon script Python](https://github.com/RuolinZheng08/twewy-discord-chatbot/blob/main/discord_bot.py) pour un bot Python et [mon script JS](https://github.com/RuolinZheng08/twewy-discord-chatbot/blob/main/discord_bot.js) pour un bot JS. Notez que pour le bot JS, en raison d'une incompatibilité de version avec le Node et NPM de Repl.it, nous devrons spécifier explicitement une version inférieure de l'API Discord dans `package.json`.

```pgsql
"dependencies": {
    "discord.js": "^12.5.3",
}
```

Avec cela, notre bot est prêt à partir ! Démarrez le script Repl en cliquant sur **Run**, ajoutez le bot à un serveur, tapez quelque chose dans le canal et profitez de la réponse spirituelle du bot.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/discord-1.gif align="left")

## Comment garder le bot en ligne

Un problème avec notre bot est qu'il s'arrête dès que nous arrêtons le Repl en cours d'exécution (équivalemment, si nous fermons la fenêtre du navigateur Repl.it).

Pour contourner cela et garder notre bot en ligne indéfiniment, nous allons configurer un serveur web pour contenir le script du bot, et utiliser un service comme [Uptime Robot](https://uptimerobot.com/) pour ping notre serveur toutes les cinq minutes afin que notre serveur reste actif.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-25-at-15.29.06.png align="left")

Dans mon tutoriel vidéo, j'ai copié le code du serveur à partir de ces deux articles de freeCodeCamp ([version Python](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/), [version JavaScript](https://www.freecodecamp.org/news/create-a-discord-bot-with-javascript-nodejs/)). Ensuite, j'ai configuré le moniteur sur Uptime Robot. Maintenant, mon bot continue de répondre à mes messages même si je ferme le navigateur (ou éteins mon ordinateur complètement).

Félicitations pour être arrivé à la fin de ce tutoriel ! J'espère que vous avez apprécié créer le bot et que vous vous amuserez à discuter avec votre personnage préféré ! 🤩

## Lien vers la vidéo du tutoriel

%[https://youtu.be/Rk8eM1p_xgM]

## Plus d'informations sur moi et mon projet de chatbot

Je m'appelle Lynn, ingénieure logicielle chez Salesforce. J'ai obtenu mon diplôme de l'Université de Chicago en 2021 avec un BS/MS conjoint en informatique, spécialisée en apprentissage automatique. [Venez dire bonjour sur mon site personnel !](https://ruolinzheng08.github.io/)

Je publie des tutoriels de projets amusants comme celui-ci sur ma chaîne YouTube. N'hésitez pas à vous abonner pour suivre mon dernier contenu. 😊

%[https://www.youtube.com/channel/UCZ2MeG5jTIqgzEMiByrIzsw]

Vous voulez en savoir plus sur mon bot ? Consultez cette démonstration de chat en temps réel de 15 minutes mettant en vedette moi, mon ami et mon bot !

%[https://youtu.be/-n6uWu8PZzo]

Intéressé par le modèle que j'ai entraîné ? Consultez-le sur Hugging Face :

%[https://huggingface.co/r3dhummingbird/DialoGPT-medium-joshua]

Mon chatbot était si populaire sur un serveur de 1k+ utilisateurs qu'il a planté. 🤯 Lisez mon post-mortem de déploiement dans cet article :

%[https://www.freecodecamp.org/news/recovering-from-deployment-hell-what-i-learned-from-deploying-my-discord-bot-to-a-1000-user-server/]

Merci d'avoir lu !