---
title: Comment automatiser votre stratégie commerciale avec Python et les APIs
subtitle: ''
author: Marco Venturi
co_authors: []
series: null
date: '2022-12-06T18:11:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-automate-e-commerce-operations-with-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/cover-1.png
tags:
- name: api
  slug: api
- name: automation
  slug: automation
- name: Python
  slug: python
seo_title: Comment automatiser votre stratégie commerciale avec Python et les APIs
seo_desc: "When you work in e-commerce operations, you'll have to perform many tasks\
  \ daily to implement your company's business strategies. \nBut these often repetitive\
  \ tasks can be time-consuming and leave room for errors. Some of these errors can\
  \ cost your com..."
---

Lorsque vous travaillez dans les opérations de commerce électronique, vous devrez effectuer de nombreuses tâches quotidiennement pour mettre en œuvre les stratégies commerciales de votre entreprise. 

Mais ces tâches souvent répétitives peuvent être chronophages et laisser place aux erreurs. Certaines de ces erreurs peuvent coûter à votre entreprise de l'argent, de la réputation et du temps. 

Heureusement, Python et les APIs peuvent vous aider à prévenir de telles erreurs ainsi qu'à économiser du temps et de l'argent. Votre équipe peut alors investir ce temps et cet argent dans d'autres activités comme le développement de nouvelles stratégies ou méthodes pour être plus efficace.

## Vous avez peut-être déjà entendu parler des APIs 

Si vous travaillez dans l'industrie technologique, vous avez probablement entendu parler des APIs au moins une fois dans votre vie. Si vous n'en avez jamais entendu parler, ne vous inquiétez pas – je vais vous donner une brève explication ici.

**"API"** signifie **Interface de Programmation d'Application**. Elles aident les services ou applications à communiquer entre eux. 

Pour vous donner un exemple, si vous êtes un développeur frontend, on vous demandera d'appeler un service backend via son API pour récupérer les informations que vous souhaitez afficher à l'écran. C'est ainsi que le backend et le frontend envoient et reçoivent des données. Lorsque vous appelez une API, vous obtenez un fichier JSON ou XML en réponse.

Les APIs peuvent également être **"RESTful"**, ce qui signifie **Representational State Transfer**. Rest est un ensemble de contraintes architecturales qui vous aident à concevoir des APIs efficaces et sécurisées. 

Si vous souhaitez en savoir plus sur les APIs REST, je vous recommande de [lire cet article d'Ihechikara](https://www.freecodecamp.org/news/what-is-rest-rest-api-definition-for-beginners/) ici sur la publication de freeCodeCamp.

## Comment les APIs peuvent-elles vous aider à accomplir votre travail ?

Comme je l'ai dit, les APIs concernent l'échange d'informations. Même si vous ne développez pas une application frontend, vous pouvez récupérer les données dont vous avez besoin et les manipuler ou les traiter pour obtenir les informations dont vous avez besoin. Ensuite, vous pouvez demander à un autre service d'effectuer l'action que vous souhaitez.

Je vais vous donner un exemple de la vie quotidienne pour vous montrer comment vous pouvez utiliser les APIs pour automatiser les tâches afin d'aider à mettre en œuvre votre stratégie commerciale.

### Exemple de cas d'utilisation d'une API

Disons que notre entreprise vend des parapluies et que nous voulons mettre à jour notre liste de prix en fonction de la météo de la ville où se trouve notre magasin. Lorsqu'il pleut, nous voulons augmenter le prix des parapluies, tandis que nous voulons le diminuer lorsque le temps est beau. Dans tous les autres cas, nous voulons laisser le prix tel quel.

Bien sûr, il s'agit d'un scénario excessivement simplifié, mais je pense qu'il est bien adapté pour montrer à quel point les APIs peuvent être puissantes pour vous aider à automatiser vos stratégies commerciales en ligne.

Sans aucune automatisation, vous devriez vérifier les prévisions météorologiques chaque jour et mettre à jour manuellement le prix de l'article. Comme je l'ai dit au début de cet article, ce type de processus manuel peut être chronophage et laisser place aux erreurs. De plus, n'oubliez pas que vous auriez besoin de quelqu'un pour effectuer ces tâches 365 jours par an.

Heureusement, nous pouvons automatiser ce processus. Voici ce dont nous avons besoin :

* Python (3.10 et versions ultérieures)
* Un CMS/commerce électronique exposant des APIs (j'utilise Woocommerce pour ce tutoriel)
* Des APIs de prévisions météorologiques

### Comment utiliser Python et les APIs pour automatiser les mises à jour

Nous allons implémenter un script écrit en Python – qui s'exécute toutes les 24 heures – pour mettre à jour le prix des parapluies en fonction de la réponse d'une API de prévisions météorologiques que nous appelons.

Plongeons dans le script et analysons-le étape par étape. 

Tout d'abord, je déclare les variables d'environnement. Voici la liste :

```python
API_BASEURL #L'URL de base du service de prévisions météorologiques que j'appelle

API_CITY #La ville pour laquelle je veux obtenir des informations météorologiques

API_COUNTRY #Le pays où se trouve API_CITY 

API_KEY #La clé secrète que je dois passer pour récupérer les informations météorologiques

CONSUMER_KEY #La clé dont j'ai besoin pour travailler avec les APIs Woocommerce 

CONSUMER_SECRET #Le secret dont j'ai besoin pour travailler avec les APIs Woocommerce

DOMAIN #Le domaine de mon e-commerce
```

Ensuite, je commence à importer les bibliothèques dont j'ai besoin :

```python
import os
from dotenv import load_dotenv
```

J'importe **os** et j'importe également **load_dotenv** pour travailler avec les variables d'environnement.

Ensuite, j'importe requests et JSON pour gérer la réponse de l'API.

```python
import requests
import json
```

Ensuite, j'importe le module API de la bibliothèque Python Woocommerce. Vous pouvez trouver plus d'informations dans sa riche [documentation](https://woocommerce.github.io/woocommerce-rest-api-docs/?python#libraries-and-tools).

```python
from woocommerce import API
```

Une fois que j'ai importé toutes les bibliothèques et modules dont j'ai besoin, j'instancie les variables que j'utiliserai dans mon script :

```python
load_dotenv()
product_to_sell_id = "1736" #L'ID lié aux parapluies dans mon e-commerce
raised_price = "12" #Le prix que je veux définir lorsqu'il pleut
lowered_price = "8" #Le prix que je veux définir lorsque le temps est beau
regular_price = "10" #Le prix régulier de l'article 
```

Ensuite, je déclare la fonction **changePrice** :

```python
def changePrice(price, idProduct):

    wcapi = API(
        url= os.getenv('DOMAIN'), 
        consumer_key= os.getenv('CONSUMER_KEY'), 
        consumer_secret= os.getenv('CONSUMER_SECRET'), 
        wp_api=True, 
        version="wc/v3" 
    )

    data = {
        "regular_price": price
    }

    wcapi.put("products/" + idProduct, data).json()
    
    print("Nouveau prix défini à " + data["regular_price"])
```

La fonction a deux arguments : le prix que je veux définir (price) et l'ID du produit que je veux mettre à jour (idProduct).

À l'intérieur de la fonction, je stocke dans la variable **wcapi** la méthode API avec les informations dont j'ai besoin pour atteindre mon e-commerce (URL de base, clé de consommateur et secret).

Je stocke dans la variable **data** la charge utile que je veux passer : je veux mettre à jour la valeur de la clé "regular_price" avec la valeur de l'argument "price".

Après cela, je mets à jour la base de données de l'e-commerce avec la méthode PUT en passant le chemin du produit que je veux mettre à jour (il s'agit d'une concaténation de la chaîne "products/" et de la valeur de l'argument "idProduct") et la valeur de la variable data.

Enfin, j'affiche un message de succès.

Une fois la fonction **changePrice** prête, je dois en définir une nouvelle pour faire fonctionner le script. Mais avant d'aller plus loin, nous devons voir les données que nous obtenons de notre appel d'API.

Le fichier JSON que nous recevons en réponse retourne beaucoup d'informations. Mais, comme je l'ai dit au début, nous voulons simplement savoir quel temps il fait. 

Nous obtenons ces données avec la clé "code". Chaque statut météorologique est associé à un nombre. Dans notre cas, nous nous concentrons sur ces deux codes : 

```python
502 #pluvieux
800 #ensoleillé
```

Maintenant que nous avons ce dont nous avons besoin, nous définissons la fonction **getWeather** :

```python
def getWeather():

    url = os.getenv('API_BASEURL')

    headers = {
    "Accept": "application/json"
    }
    
    payload = {
    "key": os.getenv('API_KEY'),
    "city": os.getenv('API_CITY'),
    "country": os.getenv('API_COUNTRY')
    }
    

    response = requests.request(
    "GET",
    url,
    params=payload,
    headers=headers  
    )

    data = response.text

    parse_json = json.loads(data)

    get_parse_result = parse_json["data"][0]["weather"]["code"]
    
    match get_parse_result:
        case 502:
            changePrice(raised_price, product_to_sell_id)

        case 800:
            changePrice(lowered_price, product_to_sell_id)

        case _:
            changePrice(regular_price, product_to_sell_id)
```

Dans la variable **url**, nous définissons l'URL de base de l'API que nous appelons. Dans la variable payload, je passe notre clé secrète, la ville et le pays pour lesquels je veux obtenir la météo.

J'effectue ma requête GET en passant l'URL, le payload et les headers. Une fois que j'obtiens la réponse, je la parse et implémente une instruction switch avec 3 cas :

* **get_parse_result** est égal à 502 : nous appelons la fonction changePrice en passant comme premier argument la variable raised_price pour augmenter le prix du produit
* **get_parse_result** est égal à 800 : nous appelons la fonction changePrice en passant comme premier argument la variable lowered_price pour diminuer le prix du produit
* **get_parse_result** a une valeur différente : nous appelons la fonction changePrice en passant comme premier argument la variable regular_price pour garder le prix du produit tel quel

À la fin du script, j'appelle la fonction getWeather :

```python
getWeather()

```

Et voilà – les prix seront automatiquement mis à jour grâce à un peu de code.

## Conclusion

Donc, ce n'est qu'un exemple rapide de la façon dont vous pouvez utiliser les APIs pour automatiser vos stratégies commerciales, économiser du temps et éviter les erreurs qui peuvent coûter de l'argent à votre entreprise. 

C'est un exemple assez basique mais je pense qu'il montre le potentiel des APIs et leurs avantages. Ici vous pouvez trouver mon [dépôt](https://github.com/mventuri/automate-ecom-prices) avec le script complet.