---
title: Analyse de données de base sur Twitter avec Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-17T17:56:08.000Z'
originalURL: https://freecodecamp.org/news/basic-data-analysis-on-twitter-with-python-251c2a85062e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*SsrUI-q_kWKPd-HKmcRNvg.png
tags:
- name: Data Science
  slug: data-science
- name: data visualization
  slug: data-visualization
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: Twitter
  slug: twitter
seo_title: Analyse de données de base sur Twitter avec Python
seo_desc: 'By Lucas Kohorst

  After creating the Free Wtr bot using Tweepy and Python and this code, I wanted
  a way to see how Twitter users were perceiving the bot and what their sentiment
  was. So I created a simple data analysis program that takes a given numbe...'
---

Par Lucas Kohorst

Après avoir créé le bot [Free Wtr](https://twitter.com/freewtr) en utilisant Tweepy et Python et [ce code](https://medium.freecodecamp.org/creating-a-twitter-bot-in-python-with-tweepy-ac524157a607), je voulais un moyen de voir comment les utilisateurs de Twitter percevaient le bot et quel était leur sentiment. J'ai donc créé un programme d'analyse de données simple qui prend un nombre donné de tweets, les analyse et affiche les données dans un nuage de points.

![Image](https://cdn-media-1.freecodecamp.org/images/Oi2DdKx2eKA9W5Pc8KtXO3aEFBWDVOvYdNiW)
_Image [crédit](https://pixabay.com/en/facebook-analytics-graphs-2265786/" rel="noopener" target="_blank" title=")._

### Installation

J'ai dû installer quelques packages pour créer ceci : **Tweepy**, **Tkinter**, **Textblob** et **matplotlib**. Vous pouvez installer chacun de ces packages avec le gestionnaire de paquets pip. Par exemple :

```
pip install tweepy
```

ou vous pouvez cloner le dépôt Github comme ceci.

```
git clone https://github.com/sloria/textblobcd textblobpython setup.py install
```

Ensuite, vous devrez créer un nouveau fichier **Python** et importer les packages suivants.

```
import tweepy #L'API Twitterfrom Tkinter import * #Pour l'interface graphiquefrom time import sleepfrom datetime import datetimefrom textblob import TextBlob #Pour l'analyse de sentimentimport matplotlib.pyplot as plt #Pour graphiquer les données
```

### Identifiants Twitter

Maintenant, nous devons lier un compte Twitter à notre script. Si vous n'en avez pas déjà un, créez-en un.

Rendez-vous sur [apps.twitter.com](https://apps.twitter.com/) et connectez-vous avec votre compte. Créez une application Twitter et générez une Clé Consommateur, un Secret Consommateur, un Jeton d'Accès et un Secret de Jeton d'Accès.

Sous vos instructions d'importation, stockez vos identifiants dans des variables, puis utilisez le deuxième bloc de code pour authentifier votre compte avec Tweepy.

```
consumer_key = 'clé consommateur'consumer_secret = 'secret consommateur'access_token = 'jeton d'accès'access_token_secret = 'secret de jeton d'accès'
```

```
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)auth.set_access_token(access_token, access_token_secret)api = tweepy.API(auth)
```

Si vous souhaitez tester pour voir si votre compte est correctement authentifié, vous pourriez simplement imprimer votre nom d'utilisateur dans la console.

```
user = api.me()print (user.name)
```

### Création de l'interface graphique

Pour l'interface, nous utiliserons deux labels : un pour la **recherche** et l'autre pour la **taille de l'échantillon** ou le nombre de tweets à analyser. Nous aurons également besoin d'un bouton de soumission afin que, lorsqu'il est cliqué, nous puissions appeler notre fonction `getData`.

```
root = Tk()
```

```
label1 = Label(root, text="Recherche")E1 = Entry(root, bd =5)
```

```
label2 = Label(root, text="Taille de l'échantillon")E2 = Entry(root, bd =5)
```

```
submit = Button(root, text ="Soumettre", command = getData)
```

Pour que l'ordinateur sache qu'il doit garder l'interface graphique à l'écran, nous devons **pack** nos labels puis **boucler** l'affichage racine.

```
label1.pack()E1.pack()
```

```
label2.pack()E2.pack()
```

```
submit.pack(side =BOTTOM)
```

```
root.mainloop()
```

En exécutant simplement ce code, vous devriez voir une fenêtre qui ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/7Zb3LMvzGDc1Aryk2mlEMqwglNSEHBKsxIJ-)

Cependant, lorsque du texte est saisi dans les labels ou que le bouton **soumettre** est cliqué, rien ne se passe. Nous devons collecter les données.

### Analyse des Tweets

Tout d'abord, nous devons obtenir le texte saisi dans les labels.

```
def getE1():    return E1.get()
```

```
def getE2():    return E2.get()
```

Maintenant, nous sommes prêts à coder la fonction `getData`. À partir de maintenant, tout le code est dans cette fonction :

```
def getData():    #Code
```

Nous devons utiliser les fonctions `GetE1()` et `GetE2()`. Celles-ci stockent notre **recherche** et notre **taille d'échantillon** dans des variables que nous pouvons parcourir.

```
getE1()    keyword = getE1()
```

```
getE2()    numberOfTweets = getE2()    numberOfTweets = int(numberOfTweets)
```

Afin de stocker nos données, nous pouvons utiliser des listes. Une liste est pour la polarité (ou sentiment) des tweets, et une autre pour le numéro du tweet (afin que nous puissions graphiquer les données).

```
    polarity_list = []    numbers_list = []    number = 1
```

Le nombre de tweets doit être déclaré comme 1 car la valeur par défaut est 0.

Nous pouvons maintenant commencer à itérer à travers les tweets et les analyser. En utilisant TextBlob, nous pouvons trouver le sentiment de chaque tweet et le stocker dans une variable `polarity`. Nous pouvons ensuite ajouter cette variable à notre `polarity_list` ainsi qu'ajouter le numéro à notre `number_list`.

```
analysis = TextBlob(tweet.text)analysis = analysis.sentimentpolarity = analysis.polarity            polarity_list.append(polarity)            numbers_list.append(number)number = number + 1
```

Nous prenons ce code et, en utilisant une boucle `for` et une instruction `try`, nous l'itérons sur le nombre de tweets pour le mot-clé de **recherche**.

```
for tweet in tweepy.Cursor(api.search, keyword, lang="en").items(numberOfTweets):        try:            analysis = TextBlob(tweet.text)            analysis = analysis.sentiment            polarity = analysis.polarity            polarity_list.append(polarity)            numbers_list.append(number)            number = number + 1
```

```
except tweepy.TweepError as e:            print(e.reason)
```

```
except StopIteration:            break
```

### Graphique en nuage de points

Afin de graphiquer notre nuage de points avec **matplotlib**, nous devons d'abord définir l'axe.

```
axes = plt.gca()axes.set_ylim([-1, 2])
```

et ensuite tracer nos listes de données.

```
plt.scatter(numbers_list, polarity_list)
```

Les informations clés sont affichées dans une boîte. Afin de montrer le sentiment général des tweets que nous avons collectés, nous calculons la moyenne de tous les tweets collectés. De plus, comme nous affichons le sentiment à un moment spécifique, nous voulons afficher la date et l'heure.

```
averagePolarity = (sum(polarity_list))/(len(polarity_list))averagePolarity = "{0:.0f}%".format(averagePolarity * 100)time  = datetime.now().strftime("À: %H:%M\nLe: %m-%d-%y")
```

```
plt.text(0, 1.25, "Sentiment Moyen:  " + str(averagePolarity) + "\n" + time, fontsize=12, bbox = dict(facecolor='none', edgecolor='black', boxstyle='square, pad = 1'))
```

![Image](https://cdn-media-1.freecodecamp.org/images/dqJLeSkMRD4JgICY25kJ6BzmEGboBKCEtiyh)

Pour le titre, nous pouvons utiliser ceci :

```
plt.title("Sentiment de " + keyword + " sur Twitter") plt.xlabel("Nombre de Tweets")plt.ylabel("Sentiment")
```

et enfin utiliser `plot.show()` pour afficher le graphique.

![Image](https://cdn-media-1.freecodecamp.org/images/vIjdFG0xozfQTtwIstdIRKg5zCzYVQTZCtaE)

### Exemple

En testant cela pour mon bot [**Free Wtr**](https://twitter.com/freewtr), le sentiment était très élevé !

![Image](https://cdn-media-1.freecodecamp.org/images/IOQQg59OGPt-yHb7lsOewrUtnwEsxXFI5ELn)
_Taille de l'échantillon de 250 Tweets_

En ce qui concerne **Donald Trump**, je ne peux pas en dire autant :

![Image](https://cdn-media-1.freecodecamp.org/images/RYhlPLyIbna6XdhRUoV7TT2x8yX6t7Yi3Mfk)

Voici le [code source complet](https://github.com/Fidel-Willis/Twitter-Data) sur Github.