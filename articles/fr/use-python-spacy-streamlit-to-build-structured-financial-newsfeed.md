---
title: Utiliser Python, SpaCy et Streamlit pour créer un fil d'actualités financières
  structuré
subtitle: ''
author: Harshit Tyagi
co_authors: []
series: null
date: '2021-09-23T17:01:09.000Z'
originalURL: https://freecodecamp.org/news/use-python-spacy-streamlit-to-build-structured-financial-newsfeed
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/stock_thumb.png
tags:
- name: natural language processing
  slug: natural-language-processing
- name: Python
  slug: python
seo_title: Utiliser Python, SpaCy et Streamlit pour créer un fil d'actualités financières
  structuré
seo_desc: 'One of the very interesting and widely used applications of Natural Language
  Processing is Named Entity Recognition (NER).

  Getting insights from raw and unstructured data is of vital importance. Uploading
  a document and getting the important bits of ...'
---

L'une des applications très intéressantes et largement utilisées du traitement du langage naturel est la reconnaissance d'entités nommées (NER).

Obtenir des informations à partir de données brutes et non structurées est d'une importance vitale. Télécharger un document et en extraire les informations importantes s'appelle la récupération d'informations.

La récupération d'informations a toujours été une tâche et un défi majeurs en NLP. Et nous pouvons utiliser la NER (ou NEL — Named Entity Linking) dans plusieurs domaines comme la finance, la recherche pharmaceutique, le commerce électronique, et plus encore à des fins de récupération d'informations.

Dans ce tutoriel, je vais vous montrer comment vous pouvez exploiter la NEL pour développer un fil d'actualités boursières personnalisé qui liste les actions en vogue sur Internet.

### Prérequis

Il n'y a pas de prérequis réels à proprement parler. Il serait utile d'avoir une certaine familiarité avec Python et les tâches de base du NLP comme la tokenisation, l'étiquetage POS, l'analyse de dépendance, et ainsi de suite.

Je vais couvrir les points importants en plus de détails, donc même si vous êtes un débutant complet, vous pourrez comprendre ce qui se passe.

Alors, commençons ! Suivez et vous aurez un fil d'actualités boursières minimal que vous pourrez commencer à rechercher à la fin de ce tutoriel.

## Ce dont vous aurez besoin pour commencer :

1. Google Colab pour les tests initiaux et l'exploration des données et de la bibliothèque SpaCy.
   
2. VS Code (ou tout autre éditeur) pour coder l'application Streamlit.
   
3. Source d'informations boursières (actualités) sur laquelle nous effectuerons la NER et plus tard la NEL.
   
4. Un environnement Python virtuel (j'utilise conda) avec des bibliothèques comme Pandas, SpaCy, Streamlit, Streamlit-Spacy (si vous voulez montrer quelques rendus SpaCy).
   

## Objectifs du projet

Le but de ce projet est d'apprendre et d'appliquer la reconnaissance d'entités nommées pour extraire les entités importantes (sociétés cotées en bourse dans notre exemple) et ensuite lier chaque entité avec certaines informations en utilisant une base de connaissances (liste des entreprises Nifty500).

Nous obtiendrons les données textuelles à partir de flux RSS sur Internet et extrairons les noms des actions en vogue. Nous tirerons ensuite leurs données de prix de marché pour tester l'authenticité des actualités avant de prendre une position sur ces actions.

> Note : La NER peut ne pas être un problème de pointe, mais elle a de nombreuses applications dans l'industrie.

Passons à Google Colab pour l'expérimentation et les tests.

## Étape 1 : Comment extraire les données des actualités des actions tendances

Pour obtenir des actualités boursières authentiques et fiables, j'utiliserai les flux RSS de [Economic Times](https://economictimes.indiatimes.com/markets/stocks/rssfeeds/2146842.cms) et [Money Control](https://www.moneycontrol.com/rss/buzzingstocks.xml) pour ce tutoriel. Mais vous pouvez également utiliser/ajouter les flux RSS de votre pays ou les données Twitter/Telegram (groupes) pour rendre votre flux plus informatif/précis.

Les opportunités sont immenses. Ce tutoriel devrait servir de tremplin pour appliquer la NEL afin de construire des applications dans différents domaines, résolvant différents types de problèmes de récupération d'informations.

Si vous allez voir le flux RSS, il ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-20-at-11.25.40-PM.png align="left")

Notre objectif est d'obtenir les titres textuels de ce flux RSS, puis nous utiliserons SpaCy pour extraire les principales entités des titres.

Les titres sont présents à l'intérieur de la balise `<title>` du XML ici.

Tout d'abord, nous devons capturer l'ensemble du document XML et nous pouvons utiliser la bibliothèque `**requests**` pour cela. Assurez-vous d'avoir ces packages installés dans votre environnement d'exécution dans colab.

Vous pouvez exécuter la commande suivante pour installer presque n'importe quel package directement depuis une cellule de code de colab :

```shell
!pip install <package_name>
```

Envoyez une requête `GET` à l'URL fournie pour capturer le document XML.

```python
import requests
resp = requests.get("https://economictimes.indiatimes.com/markets/stocks/rssfeeds/2146842.cms")
```

Exécutez la cellule pour vérifier ce que vous obtenez dans l'objet de réponse.

Cela devrait vous donner une réponse réussie avec le code HTTP 200 comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-21-at-12.06.11-AM.png align="left")

Maintenant que vous avez cet objet de réponse, nous pouvons passer son contenu à la classe BeautifulSoup pour analyser le document XML comme suit :

```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(resp.content, features='xml')
soup.findAll('title')
```

Cela devrait vous donner tous les titres à l'intérieur d'une liste Python :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-21-at-12.29.31-AM.png align="left")

Super — nous avons les données textuelles à partir desquelles nous allons extraire les principales entités (qui sont des sociétés cotées en bourse dans ce cas) en utilisant le NLP.

Il est temps de mettre le NLP en action.

## Étape 2 : Comment extraire les entités des titres

C'est la partie excitante. Nous allons utiliser un **modèle de langage principal pré-entraîné** de la bibliothèque `**spaCy**` pour extraire les principales entités d'un titre.

Parlons un peu plus de spaCy et des modèles principaux.

[**spaCy**](https://spacy.io/) est une bibliothèque NLP open-source qui traite les données textuelles à une vitesse ultra-rapide. C'est la bibliothèque de référence en recherche NLP qui est utilisée dans des applications de niveau entreprise à grande échelle.

spaCy est bien connu pour évoluer avec le problème. Et il supporte plus de 64 langues et fonctionne bien avec TensorFlow et PyTorch.

En parlant des modèles principaux, spaCy dispose de deux grandes classes de modèles de langage pré-entraînés qui sont entraînés sur différentes tailles de données textuelles pour nous donner des inférences de pointe.

1. Modèles principaux — pour les tâches NLP de base à usage général.
   
2. Modèles de démarrage — pour les applications de niche qui nécessitent un apprentissage par transfert. Nous pouvons exploiter les poids appris du modèle pour affiner nos modèles personnalisés sans avoir à entraîner le modèle à partir de zéro.
   

Puisque notre cas d'utilisation est basique dans ce tutoriel, nous allons nous en tenir au pipeline du modèle principal `en_core_web_sm`.

Alors, chargeons cela dans notre notebook :

```javascript
nlp = spacy.load("en_core_web_sm")
```

**Note :** Colab a déjà téléchargé cela pour nous, mais si vous essayez de l'exécuter dans votre système local, vous devrez d'abord télécharger le modèle en utilisant la commande suivante :

```javascript
python -m spacy download en_core_web_sm
```

`en_core_web_sm` est essentiellement un pipeline anglais optimisé pour le CPU qui comprend les composants suivants :

* tok2vec — token to vector (effectue la tokenisation sur les données textuelles),
   
* tagger — ajoute des métadonnées pertinentes à chaque token. spaCy utilise certains modèles statistiques pour prédire la partie du discours (POS) de chaque token. Plus d'informations dans la [documentation](https://spacy.io/models/en).
   
* parser — l'analyseur de dépendance établit des relations entre les tokens.
   
* D'autres composants incluent senter, ner, attribute_ruler et lemmatizer.
   

Maintenant, pour tester ce que ce modèle peut faire pour nous, je vais passer un seul titre à travers le modèle instancié, puis vérifier les différentes parties d'une phrase.

```javascript
# assurez-vous d'extraire le texte des balises <title>
processed_hline = nlp(headlines[4].text)
```

Le pipeline effectue toutes les tâches, de la tokenisation à la NER. Voici d'abord les tokens :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-21-at-2.04.54-AM.png align="left")

Vous pouvez regarder la partie du discours étiquetée en utilisant l'attribut `pos_`.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-21-at-2.08.40-AM.png align="left")

Chaque token est étiqueté avec des métadonnées. Par exemple, Trade est un nom propre, Setup est un nom, `:` est une ponctuation, et ainsi de suite. La liste complète des balises est donnée [ici](https://spacy.io/models/en).

Ensuite, vous pouvez voir comment ils sont liés en regardant le graphe de dépendance en utilisant l'attribut `dep_` :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-21-at-2.11.15-AM.png align="left")

Ici, Trade est un composé, Setup est la racine, Nifty est un appos (modificateur appositionnel). Encore une fois, toutes les balises syntaxiques peuvent être trouvées [ici](https://spacy.io/models/en).

Vous pouvez également visualiser les dépendances de relation entre les tokens en utilisant la méthode `render()` de displacy :

```python
spacy.displacy.render(processed_hline, style='dep',
jupyter=True, options={'distance': 120})
```

ce qui donnera ce graphe :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-21-at-2.18.43-AM.png align="left")

### Extraction d'entités

Et pour voir les entités importantes de la phrase, vous pouvez passer `**'ent'**` comme style dans le même code :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-21-at-2.24.26-AM.png align="left")

Nous avons différentes balises pour différentes entités comme le jour a DATE, et Glasscoat a GPE qui peut être des pays/villes/états. Nous recherchons principalement des entités qui ont la balise ORG qui nous donnera des entreprises, des agences, des institutions, et ainsi de suite.

Nous sommes maintenant capables d'extraire des entités du texte. Descendons à l'extraction des organisations de tous les titres en utilisant les entités ORG.

```python
ent.py
companies = []
for title in headlines:
    doc = nlp(title.text)
    for token in doc.ents:
        if token.label_ == 'ORG':
            companies.append(token.text)
        else:
            pass
```

Cela retournera une liste de toutes les entreprises comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-21-at-2.36.31-AM.png align="left")

Si facile, n'est-ce pas ?

C'est la magie de spaCy maintenant !

L'étape suivante consiste à rechercher toutes ces entreprises dans une base de connaissances pour extraire le bon symbole boursier pour cette entreprise. Ensuite, nous utiliserons des bibliothèques comme yahoo-finance pour extraire leurs détails de marché comme le prix, le rendement, et ainsi de suite.

## Étape 3 — Named Entity Linking

Apprendre quelles actions sont en vogue sur le marché et obtenir leurs détails sur votre tableau de bord sont les objectifs de ce projet.

Nous avons les noms des entreprises, mais pour obtenir leurs détails de trading, nous aurons besoin du symbole boursier de l'entreprise.

Puisque j'extrais les détails et les actualités des entreprises indiennes, je vais utiliser une base de données externe des [entreprises Nifty 500 (un fichier CSV).](https://www1.nseindia.com/products/content/equities/indices/nifty_500.htm)

Pour chaque entreprise, nous la rechercherons dans la liste des entreprises en utilisant pandas, puis nous capturerons les statistiques du marché boursier en utilisant la bibliothèque [yahoo-finance](https://pypi.org/project/yfinance/).

```python
import yfinance as yf

## collecter divers attributs de marché d'une action
stock_dict = {
    'Org': [],
    'Symbol': [],
    'currentPrice': [],
    'dayHigh': [],
    'dayLow': [],
    'forwardPE': [],
    'dividendYield': []
}

## pour chaque entreprise, recherchez-la et collectez toutes les données de marché à son sujet
for company in companies:
    try:
        if stocks_df['Company Name'].str.contains(company).sum():
            symbol = stocks_df[stocks_df['Company Name'].\
                                str.contains(company)]['Symbol'].values[0]
            org_name = stocks_df[stocks_df['Company Name'].\
                                str.contains(company)]['Company Name'].values[0]
            stock_dict['Org'].append(org_name)
            stock_dict['Symbol'].append(symbol)
            stock_info = yf.Ticker(symbol+".NS").info
            stock_dict['currentPrice'].append(stock_info['currentPrice'])
            stock_dict['dayHigh'].append(stock_info['dayHigh'])
            stock_dict['dayLow'].append(stock_info['dayLow'])
            stock_dict['forwardPE'].append(stock_info['forwardPE'])
            stock_dict['dividendYield'].append(stock_info['dividendYield'])
        else:
            pass
    except:
        pass

## créer un dataframe pour afficher les actions en vogue
pd.DataFrame(stock_dict)
```

Une chose à laquelle vous devez faire attention ici est que j'ai ajouté un « .NS » après chaque symbole boursier avant de le passer à la classe `Ticker` de la bibliothèque `yfinance`. Cela est dû au fait que les symboles boursiers indiens NSE sont stockés avec un suffixe `.NS` dans `yfinance`.

Et les actions en vogue apparaîtraient dans un dataframe comme ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-21-at-4.43.01-AM.png align="left")

Voilà ! N'est-ce pas génial ? Une application si simple mais profonde qui pourrait vous orienter dans la bonne direction avec les bonnes actions.

Maintenant, pour la rendre plus accessible, nous pouvons créer une application web à partir du code que nous venons d'écrire en utilisant Streamlit.

## Étape 4 — Comment construire une application web en utilisant Streamlit

Il est temps de passer à un éditeur et de créer un nouveau projet et un environnement virtuel pour l'application NLP.

Commencer avec Streamlit est super facile pour de telles applications de données de démonstration. Assurez-vous d'avoir Streamlit installé.

```javascript
pip install Streamlit
```

Maintenant, créons un nouveau fichier appelé app.py et commençons à écrire du code fonctionnel pour préparer l'application.

Importez toutes les bibliothèques requises en haut comme ceci :

```python
import pandas as pd
import requests
import spacy
import streamlit as st
from bs4 import BeautifulSoup
import yfinance as yf
```

Ajoutez un titre à votre application :

```python
st.title('Actions en vogue :zap:')
```

Testez votre application en exécutant `streamlit run app.py` dans votre terminal. Cela devrait ouvrir une application dans votre navigateur web.

J'ai ajouté une fonctionnalité supplémentaire pour capturer des données à partir de plusieurs sources. Maintenant, vous pouvez ajouter une URL de flux RSS de votre choix dans l'application et les données seront traitées et les actions tendances seront affichées dans un dataframe.

Pour accéder à l'ensemble de la base de code, vous pouvez consulter mon dépôt ici :

[https://github.com/dswh/NER\_News\_Feed](https://github.com/dswh/NER_News_Feed)

Si vous voulez me suivre étape par étape, regardez-moi coder cette application ici :

%[https://youtu.be/G5ycs1hFSKk] 

Vous pouvez ajouter plusieurs éléments de style, différentes sources de données et d'autres types de traitement pour la rendre plus efficace et utile.

Mon application dans son état actuel ressemble à l'image de la bannière.

## Prochaines étapes

Au lieu de choisir un cas d'utilisation financier, vous pouvez également choisir une autre application de votre choix — santé, commerce électronique, recherche, et bien d'autres. Toutes les industries nécessitent que des documents soient traités et que des entités importantes soient extraites et liées. Essayez une autre idée.

Une idée simple consiste à extraire toutes les entités importantes d'un article de recherche, puis à créer un graphe de connaissances à partir de celui-ci en utilisant l'API Google Search.

De plus, si vous souhaitez emmener l'application de flux d'actualités boursières à un autre niveau, vous pouvez ajouter des algorithmes de trading pour générer des signaux d'achat et de vente également.

Je vous encourage à laisser libre cours à votre imagination.

### Comment vous pouvez me contacter

Si vous avez aimé cet article et que vous souhaitez voir plus de contenu de ce type, vous pouvez vous abonner à [**ma newsletter**](https://dswharshit.substack.com/publish/settings#twitter-account) **ou** [**ma chaîne YouTube**](https://www.youtube.com/channel/UCH-xwLTKQaABNs2QmGxK2bQ) où je continuerai à partager des projets utiles et rapides que l'on peut construire.

Si vous êtes quelqu'un qui commence tout juste avec la programmation ou qui souhaite se lancer dans la science des données ou le ML, vous pouvez consulter mon cours à [**WIP Lane Academy**](https://www.wiplane.com/p/foundations-for-data-science-ml).