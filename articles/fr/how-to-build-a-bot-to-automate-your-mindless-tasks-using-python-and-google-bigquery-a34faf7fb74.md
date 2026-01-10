---
title: Comment créer un bot pour automatiser vos tâches répétitives en utilisant Python
  et Google BigQuery
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-08T16:40:50.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-bot-to-automate-your-mindless-tasks-using-python-and-google-bigquery-a34faf7fb74
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xaB3nYYGNzuhdRJZuat3Cg.jpeg
tags:
- name: automation
  slug: automation
- name: Data Science
  slug: data-science
- name: General Programming
  slug: programming
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
seo_title: Comment créer un bot pour automatiser vos tâches répétitives en utilisant
  Python et Google BigQuery
seo_desc: 'By Dzaky Widya Putra

  Do you have repetitive tasks? Something that you do regularly, every week or even
  every day? Reporting might be one of your weekly or daily tasks. You query or ask
  for the data, and do some visualizations, then give it to your bo...'
---

Par Dzaky Widya Putra

Avez-vous des tâches répétitives ? Quelque chose que vous faites régulièrement, chaque semaine ou même chaque jour ? La génération de rapports peut être l'une de vos tâches hebdomadaires ou quotidiennes. Vous interrogez ou demandez les données, et faites quelques visualisations, puis les donnez à votre patron. Et si, au lieu de le faire manuellement, vous l'automatisiez pour ne pas avoir à faire les choses ennuyeuses, et pour pouvoir utiliser votre temps précieux pour faire autre chose ?

Dans ce tutoriel, nous allons créer un bot Telegram qui automatisera les parties ennuyeuses de votre travail — la génération de rapports. Oh, et ai-je mentionné que cela ne prendra pas plus de 50 lignes de code pour le construire ? ;)

Si c'est votre première fois à construire un bot Telegram, vous pourriez vouloir lire [cet article](https://medium.freecodecamp.org/learn-to-build-your-first-bot-in-telegram-with-python-4c99526765e4) d'abord.

### Pour commencer

#### 1. Installer les bibliothèques

Nous allons utiliser [google-cloud-bigquery](https://github.com/googleapis/google-cloud-python) pour interroger les données de Google BigQuery. [matplotlib](https://matplotlib.org/), [numpy](http://www.numpy.org/) et [pandas](https://pandas.pydata.org/) nous aideront avec la visualisation des données. [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) enverra l'image de visualisation via le chat Telegram.

```py
pip3 install google-cloud-bigquery matplotlib numpy pandas python-telegram-bot
```

#### 2. Activer l'API Google BigQuery

Nous devons activer l'API Google BigQuery d'abord si nous voulons utiliser le service.

Allez sur [Google Developers Console](https://console.developers.google.com/) et créez un nouveau projet (ou sélectionnez celui que vous avez).

Dans le tableau de bord du projet, cliquez sur **ACTIVER LES APIS ET SERVICES**, et recherchez l'API BigQuery.

![Image](https://cdn-media-1.freecodecamp.org/images/1*L-1tAU905-5SO-cQz9giIQ.png)

Cliquez sur **ACTIVER** pour activer l'API.

![Image](https://cdn-media-1.freecodecamp.org/images/1*nrq8lk3lR-BXzvSr1AnEgA.png)

####  
3. Créer la clé de compte de service

Si nous voulons utiliser les services Google Cloud comme Google BigQuery, nous avons besoin d'une clé de compte de service. Cela ressemble à nos identifiants pour utiliser les services de Google.

Allez sur [Google Developers Console](https://console.developers.google.com/), cliquez sur l'onglet **Identifiants**, choisissez **Créer des identifiants** et cliquez sur **Clé de compte de service**.

Choisissez **Nouveau compte de service**, dans le champ **Nom du compte de service**, entrez un nom.

Dans la liste déroulante **Rôle**, sélectionnez **Projet** > **Propriétaire**, puis cliquez sur **Créer**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Y2yJZZCasDbtQ1ia7icaDA.png)

Il y a un fichier .json qui sera automatiquement téléchargé, nommez-le `creds.json`.

Définissez la variable `GOOGLE_APPLICATION_CREDENTIALS` avec le chemin de notre fichier `creds.json` dans le terminal.

```
export GOOGLE_APPLICATION_CREDENTIALS='[PATH_TO_CREDS.JSON]'
```

Tout devrait être bon maintenant, il est temps d'écrire notre programme.

### Écrire le programme

Nous allons écrire le programme qui interrogera les données de BigQuery (nous supposons que les données y sont stockées). Ensuite, nous visualiserons les données et les enregistrerons sous forme d'image. L'image sera ensuite envoyée via le chat Telegram.

Pour ce tutoriel, nous utilisons le jeu de données `bigquery-public-data.stackoverflow`, et nous prendrons les données quotidiennes totales des publications pour notre rapport.

Le flux de travail de notre programme est assez simple :

> _**Interroger**_ la table -> **Visualiser** les données -> **Enregistrer** la visualisation -> **Envoyer** l'image

Définissons une seule fonction pour chaque flux.

#### 1. Interroger BigQuery

Importons d'abord la bibliothèque.from google.cloud import bigquery

Créons une fonction appelée `query_to_bigquery` qui prend `query` comme paramètre.

```py
def query_to_bigquery(query):
    client = bigquery.Client()    
    query_job = client.query(query)    
    result = query_job.result()    
    dataframe = result.to_dataframe()    
    return dataframe
```

Cette fonction retournera les données sous forme de dataframe.

#### 2. Visualiser les données

Nous allons utiliser matplotlib pour visualiser les données.

```
import matplotlib.pyplot as plt
```

Nous prenons cinq paramètres qui sont `x` comme les données de l'axe x, `x_label` comme le nom de l'étiquette de l'axe x, `y` comme les données de l'axe y, `y_label` comme le nom de l'étiquette de l'axe y, et `title` comme notre titre de visualisation.

```py
def visualize_bar_chart(x, x_label, y, y_label, title):
    plt.title(title)    
    plt.xlabel(x_label)    
    plt.ylabel(y_label)    
    index = np.arange(len(x))    
    plt.xticks(index, x, fontsize=5, rotation=30)    
    plt.bar(index, y)    
    return plt
```

#### 3. Enregistrer l'image

Utilisons les deux fonctions ci-dessus pour créer une visualisation puis enregistrer l'image.

Comme je l'ai mentionné précédemment, nous voulons envoyer les données quotidiennes totales des publications. Écrivons d'abord la requête.

```py
query = """ 
            SELECT DATE(creation_date) date, COUNT(*) total_posts
            FROM `bigquery-public-data.stackoverflow.post_history`
            GROUP BY 1
            HAVING date > DATE_SUB('2018-12-02', INTERVAL 14 DAY)
            ORDER BY 1
        """
```

Notez que dans la requête ci-dessus, `HAVING date > DATE_SUB('2018-12-02', INTERVAL 14 DAY)` signifie que nous voulons rassembler les données à partir de 14 jours avant le 2018-12-02.

Nous utilisons cette date car `2018-12-02` est la dernière donnée enregistrée dans `bigquery-public-data.stackoverflow.post_history`, dans différents cas, vous pourriez vouloir utiliser `CURRENT_DATE()` à la place pour obtenir les données les plus récentes.

Appelons la fonction `query_to_bigquery` pour obtenir les données.

```
dataframe = query_to_bigquery(query)
```

Prenons la colonne `date` comme nos données de l'axe x, et la colonne `total_posts` comme nos données de l'axe y.

```py
x = dataframe['date'].tolist()
y = dataframe['total_posts'].tolist()
```

Visualisons les données en utilisant la fonction `visualize_bar_chart`, puis enregistrons-les sous forme d'image.

```py
plt = visualize_bar_chart(x=x, 
			  x_label='Date', 
                          y=y, 
                          y_label='Total Posts', 
                          title='Daily Posts')
plt.savefig('viz.png')
```

Enveloppons ce code dans une fonction appelée `get_and_save_image`.

```py
def get_and_save_image():    
	query = """ 
                SELECT DATE(creation_date) date, COUNT(*) total_posts
                FROM `bigquery-public-data.stackoverflow.post_history`
                GROUP BY 1
                HAVING date > DATE_SUB('2018-12-02', INTERVAL 14 DAY)
                ORDER BY 1
                """
        dataframe = query_to_bigquery(query)
        x = dataframe['date'].tolist()
        y = dataframe['total_posts'].tolist()
        plt = visualize_bar_chart(x=x, 
			  	  x_label='Date', 
                          	  y=y, 
                          	  y_label='Total Posts', 
                          	  title='Daily Posts')
        plt.savefig('viz.png')
```

#### 4. Envoyer l'image

Pour pouvoir l'envoyer à la bonne personne, nous devons connaître leur `chat_id` car c'est l'un des paramètres requis.

Allez sur [userinfobot](https://telegram.me/userinfobot) puis tapez `/start`. Le bot répondra avec nos informations utilisateur, et notre `chat_id` est le numéro dans le champ `Id`.

Créons une fonction appelée `send_image`. Cette fonction appellera d'abord la fonction `get_and_save_image` pour obtenir et enregistrer la visualisation, puis l'enverra à la personne dont le chat_id est déclaré dans la variable `chat_id`.

```py
def send_image(bot, update):
    get_and_save_image()
    chat_id = 'CHAT_ID_RECEIVER'
    bot.send_photo(chat_id=chat_id, photo=open('viz.png','rb'))
```

#### 5. Programme principal

Enfin, créez une autre fonction appelée `main` pour exécuter notre programme. **N'oubliez pas de changer** `YOUR_TOKEN` par le token de votre bot.

Rappelez-vous, ce programme enverra l'image automatiquement en fonction du jour et de l'heure que nous avons définis.

Par exemple, dans ce tutoriel, nous allons le définir à 9h00 chaque jour.

```py
def main():
    updater = Updater('YOUR_TOKEN')
    updater.job_queue.run_daily(send_image, time=datetime.datetime.strptime('9:00AM', '%I:%M%p').time(),days=(0,1,2,3,4,5,6))
    updater.start_polling()
    updater.idle()
 
 if __name__ == '__main__':    main()
```

À la fin, votre code devrait ressembler à ceci :

```py
from google.cloud import bigquery
from telegram.ext import Updater

import matplotlib.pyplot as plt
import numpy as np
import datetime

def query_to_bigquery(query):
    client = bigquery.Client()
    query_job = client.query(query)
    result = query_job.result()
    dataframe = result.to_dataframe()
    return dataframe

def visualize_bar_chart(x, x_label, y, y_label, title):
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    index = np.arange(len(x))
    plt.xticks(index, x, fontsize=5, rotation=30)
    plt.bar(index, y)
    return plt

def get_and_save_image():
    query = """ 
            SELECT DATE(creation_date) date, COUNT(*) total_posts
            FROM `bigquery-public-data.stackoverflow.post_history`
            GROUP BY 1
            HAVING date > DATE_SUB('2018-12-02', INTERVAL 14 DAY)
            ORDER BY 1
            """
    dataframe = query_to_bigquery(query)   
    x = dataframe['date'].tolist()
    y = dataframe['total_posts'].tolist()
    plt = visualize_bar_chart(x=x, x_label='Date', y=y, y_label='Total Posts', title='Daily Posts')
    plt.savefig('viz.png')

def send_image(bot, update):
    get_and_save_image()
    chat_id = 'CHAT_ID_RECEIVER'
    bot.send_photo(chat_id=chat_id, photo=open('viz.png', 'rb'))

def main():
    updater = Updater('YOUR_TOKEN')
    updater.job_queue.run_daily(send_image, time=datetime.datetime.strptime('9:00AM', '%I:%M%p').time(), days=(0,1,2,3,4,5,6))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
```

Enregistrez le fichier et nommez-le `main.py`.

Exécutez le programme en tapant cette commande dans le terminal.python3 main.py

Super ! Maintenant vous avez un générateur de rapports automatique construit avec pas plus de 50 lignes de code — assez cool, non ?

Allez vérifier le bot [ici](https://telegram.me/automatereportbot), et tapez la commande `/send` pour voir un exemple de l'image de visualisation.

L'image ci-dessous montre la visualisation que le bot enverra. Maintenant vous pouvez simplement vous asseoir, vous détendre, et attendre que le bot vous envoie le rapport tous les jours :)

![Image](https://cdn-media-1.freecodecamp.org/images/1*fG34xiHEQXck40BgDeeeog.jpeg)

Vous pouvez visiter mon [GitHub](https://github.com/dzakyputra/automatebot) pour obtenir le code, et n'hésitez pas à me contacter et à laisser un message sur mon profil [Linkedin](https://www.linkedin.com/in/dzakywp/) si vous voulez poser des questions.

Veuillez laisser un commentaire si vous pensez qu'il y a des erreurs dans mon code ou mon écriture.

Si vous vous intéressez à la science des données ou à l'apprentissage automatique, vous pourriez vouloir lire mon article sur [la construction d'un analyseur de sentiments](https://medium.freecodecamp.org/how-to-make-your-own-sentiment-analyzer-using-python-and-googles-natural-language-api-9e91e1c493e).

Encore une fois, merci et bonne chance ! :)