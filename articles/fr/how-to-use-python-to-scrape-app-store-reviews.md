---
title: Comment utiliser Python pour extraire les avis de l'App Store
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-09-16T18:04:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-python-to-scrape-app-store-reviews
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/Shittu-Olumide-How-to-use-Python-to-scrape-App-Store-reviews-Freecodecamp.png
tags:
- name: Python
  slug: python
- name: web scraping
  slug: web-scraping
seo_title: Comment utiliser Python pour extraire les avis de l'App Store
seo_desc: "By Shittu Olumide\nData scraping, commonly referred to as web scraping,\
  \ is a technique for getting data and content from the internet.\nYou usually keep\
  \ this information in a local file so that you can change and inspect it as needed.\
  \ \nWeb scraping is ..."
---

Par Shittu Olumide

L'extraction de données, communément appelée web scraping, est une technique pour obtenir des données et du contenu depuis Internet.

Vous conservez généralement ces informations dans un fichier local afin de pouvoir les modifier et les inspecter selon vos besoins. 

Le web scraping consiste essentiellement à copier et coller du contenu d'un site web dans une feuille de calcul Excel à très petite échelle.

L'objectif principal de cet article est de vous aider à commencer avec le web scraping en utilisant des étapes rapides et faciles. Vous apprendrez comment extraire les avis de l'App Store en utilisant la bibliothèque `app_store_scraper` en Python. Il existe d'autres outils et bibliothèques que vous pouvez utiliser tels que `Scrapy`, `Pandas` et `BeautifulSoup`, mais ici nous utiliserons `app_store_scraper`. 

Selon le mécanisme que vous choisissez pour le web scraping, cela peut être soit très simple, soit assez complexe. 

Heureusement, il existe un logiciel simple et excellent qui peut vous aider à collecter des avis sur votre application depuis l'App Store d'Apple et à les utiliser pour une analyse de sentiment plus approfondie.

### Pourquoi le web scraping est-il utile ?

Les professionnels de l'analyse de données utilisent le web scraping pour diverses tâches, notamment la création de leads, l'analyse de marché, l'analyse des sentiments des consommateurs et l'intégration de données.

Vous pouvez également utiliser le web scraping pour suivre les prix des actions, les opportunités en ligne (telles que les bourses, les emplois, les stages, etc.), les données d'inventaire des concurrents, ainsi que les avis et les notes des clients.  
  
Dans cet article, vous apprendrez comment utiliser Python pour extraire les avis de l'App Store en 4 étapes faciles. 

Avant de commencer, voici quelque chose à garder à l'esprit : certains sites n'autorisent pas l'extraction de leur contenu, alors assurez-vous de vérifier avant de le faire. Le web scraping n'est pas précisément interdit, mais vous devez faire attention à savoir quand et où vous pouvez extraire des données. Je vous recommande fortement d'extraire des données uniquement à des fins d'information et d'éducation.

## Étape 1 – Installer et configurer les packages

Tout d'abord, vous devez installer et configurer les packages nécessaires. Dans cette étape, vous allez installer `app_store_scraper` en utilisant l'installateur de packages Python.

```py
pip install app_store_scraper 

#ou

pip3 install app_store_scraper

```

## Étape 2 – Obtenir le nom et l'ID de l'application

Je vais utiliser une application aléatoire et je vais extraire ses avis pour cette démonstration. Mais si vous avez une application personnelle que vous avez développée et qui est sur l'App Store, vous pouvez utiliser cette application avec les mêmes techniques. Vous devez simplement obtenir le nom et l'ID de l'application, que vous pouvez trouver en tapant le nom de l'application dans Google en utilisant votre PC. 

Exemple : "_Slack app on apple app store_"

![Image](https://www.freecodecamp.org/news/content/images/2022/09/slack-google-search.PNG)

Vous devez cliquer sur le premier résultat qui vous redirigera vers l'App Store officiel. Là, vous trouverez l'application "Slack" et tout ce qui la concerne. 

Une fois la page chargée dans l'URL, vous verrez le nom de l'application (Slack) et l'ID de l'application (618783545). Copiez-les dans votre bloc-notes.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/slack-app-name-app-id.PNG)

Maintenant, vous devrez importer certains packages et exécuter du code :

```py
import pandas as pd
import numpy as np
import json

from app_store_scraper import AppStore
slack = AppStore(country='us', app_name='slack', app_id = '618783545')

slack.review(how_many=2000)

```

Dans le code ci-dessus, vous allez importer la bibliothèque `pandas` qui vous aide à ajouter des évaluations/avis à un dataframe. Vous allez également importer la bibliothèque `numpy` pour la transformation et la modification des données. Enfin, vous allez obtenir le package `app_store_scraper` lui-même pour extraire les avis du site web. 

Vous devrez créer une instance de la classe `Appstore`, puis passer les arguments `country`, `app_name` et `app_id`. 

![Image](https://www.freecodecamp.org/news/content/images/2022/09/slack-web-scraping.PNG)
_notes de l'application slack_

Tous les avis sont stockés dans la variable `slack`, alors exécutez la commande ci-dessous pour voir les avis stockés au format JSON.

```py
slack.reviews

```

![Image](https://www.freecodecamp.org/news/content/images/2022/09/slack-reviews.PNG)
_avis extraits de l'application slack_

## Étape 3 – Convertir les données du format JSON

Pour rendre les données plus lisibles et correctement formatées, vous devez les convertir du format JSON vers un dataframe Pandas. Vous pouvez le faire avec le code suivant :

```py
slackdf = pd.DataFrame(np.array(slack.reviews),columns=['review'])
slackdf2 = df.join(pd.DataFrame(slackdf.pop('review').tolist()))
slackdf2.head()

```

![Image](https://www.freecodecamp.org/news/content/images/2022/09/slack-generated-reviews.PNG)
_avis générés dans un dataframe pandas_

## Étape 4 – Convertir le Dataframe en CSV

Voici l'étape finale : vous allez convertir le dataframe en format CSV (valeurs séparées par des virgules) afin de pouvoir l'avoir sur votre machine locale. Ensuite, vous pourrez le visualiser dans une feuille de calcul et également le partager avec un collègue.

```py
slackdf2.to_csv('Slack-app-reviews.csv')

```

Enfin, vous devriez avoir votre fichier "Slack-app-reviews.csv" enregistré dans votre dossier de projet et vous êtes prêt à partir. 

## Conclusion

Dans cet article court, vous avez pu extraire les avis de l'App Store de Slack dans un dataframe, puis les enregistrer sur votre machine locale en utilisant 4 étapes faciles. J'espère que vous l'avez apprécié, à votre santé.

Voici le [dépôt GitHub](https://github.com/zenUnicorn/App-rating-scraper-with-python) où j'ai hébergé le code, n'hésitez pas à mettre une étoile au dépôt.