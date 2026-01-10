---
title: Comment créer un crawler d'URL pour cartographier un site web en utilisant
  Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-15T15:42:22.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-url-crawler-to-map-a-website-using-python-6a287be1da11
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ZxUfhtbRROKqcBqyfT8plA.jpeg
tags:
- name: Computer Science
  slug: computer-science
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Comment créer un crawler d'URL pour cartographier un site web en utilisant
  Python
seo_desc: 'By Ahad Sheriff

  A simple project for learning the fundamentals of web scraping


  Before we start, let’s make sure we understand what web scraping is:


  Web scraping is the process of extracting data from websites to present it in a
  format users can eas...'
---

Par Ahad Sheriff

#### Un projet simple pour apprendre les bases du web scraping

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZxUfhtbRROKqcBqyfT8plA.jpeg)

Avant de commencer, assurons-nous de bien comprendre ce qu'est le web scraping :

> **Le web scraping** est le processus d'extraction de données depuis des sites web pour les présenter dans un format que les utilisateurs peuvent facilement comprendre.

Dans ce tutoriel, je souhaite démontrer à quel point il est facile de créer un simple crawler d'URL en Python que vous pouvez utiliser pour cartographier des sites web. Bien que ce programme soit relativement simple, il peut offrir une excellente introduction aux bases du web scraping et de l'automatisation. Nous allons nous concentrer sur l'extraction récursive de liens depuis des pages web, mais les mêmes idées peuvent être appliquées à une multitude d'autres solutions.

Notre programme fonctionnera comme suit :

1. Visiter une page web
2. Extraire toutes les URL uniques trouvées sur la page web et les ajouter à une file d'attente
3. Traiter récursivement les URL une par une jusqu'à épuisement de la file d'attente
4. Afficher les résultats

### D'abord, les bases

La première chose à faire est d'importer toutes les bibliothèques nécessaires. Nous allons utiliser [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/), [requests](http://docs.python-requests.org/en/master/), et [urllib](https://docs.python.org/3/library/urllib.html) pour le web scraping.

```
from bs4 import BeautifulSoup
import requests
import requests.exceptions
from urllib.parse import urlsplit
from urllib.parse import urlparse
from collections import deque
```

Ensuite, nous devons sélectionner une URL pour commencer le crawling. Bien que vous puissiez choisir n'importe quelle page web avec des liens HTML, je recommande d'utiliser [ScrapeThisSite](https://scrapethissite.com/). C'est un bac à sable sûr que vous pouvez crawler sans risque.

```
url = "https://scrapethissite.com"
```

Ensuite, nous allons devoir créer un nouvel objet [deque](https://docs.python.org/3.3/library/collections.html#collections.deque) afin de pouvoir facilement ajouter de nouveaux liens et les supprimer une fois que nous avons terminé de les traiter. Prépopulez la deque avec votre variable `url` :

```
# une file d'attente d'URL à crawler ensuite
new_urls = deque([url])
```

Nous pouvons ensuite utiliser un [set](https://docs.python.org/3.3/library/stdtypes.html?highlight=set#set) pour stocker les URL uniques une fois qu'elles ont été traitées :

```
# un ensemble d'URL que nous avons déjà traitées
processed_urls = set()
```

Nous voulons également garder une trace des URL locales (même domaine que la cible), étrangères (domaine différent de la cible) et des URL cassées :

```
# un ensemble de domaines à l'intérieur du site web cible
local_urls = set()
```

```
# un ensemble de domaines à l'extérieur du site web cible
foreign_urls = set()
```

```
# un ensemble d'URL cassées
broken_urls = set()
```

### Temps de crawler

Avec tout cela en place, nous pouvons maintenant commencer à écrire le code réel pour crawler le site web.

Nous voulons examiner chaque URL dans la file d'attente, voir s'il y a des URL supplémentaires dans cette page et ajouter chacune d'elles à la fin de la file d'attente jusqu'à ce qu'il n'y en ait plus. Dès que nous avons terminé de scraper une URL, nous la retirerons de la file d'attente et l'ajouterons à l'ensemble `processed_urls` pour une utilisation ultérieure.

```
# traiter les URL une par une jusqu'à épuisement de la file d'attente
while len(new_urls):
    # déplacer l'URL de la file d'attente vers l'ensemble des URL traitées
    url = new_urls.popleft()
    processed_urls.add(url)
    # imprimer l'URL actuelle
    print("Processing %s" % url)
```

Ensuite, ajoutez une exception pour attraper les pages web cassées et les ajouter à l'ensemble `broken_urls` pour une utilisation ultérieure :

```
try:
    response = requests.get(url)
```

```
except(requests.exceptions.MissingSchema, requests.exceptions.ConnectionError, requests.exceptions.InvalidURL, requests.exceptions.InvalidSchema):
    # ajouter les URL cassées à leur propre ensemble, puis continuer
    broken_urls.add(url)
    continue
```

Nous devons ensuite obtenir l'URL de base de la page web afin de pouvoir facilement différencier les adresses locales et étrangères :

```
# extraire l'URL de base pour résoudre les liens relatifs
parts = urlsplit(url)
base = "{0.netloc}".format(parts)
strip_base = base.replace("www.", "")
base_url = "{0.scheme}://{0.netloc}".format(parts)
path = url[:url.rfind('/')+1] if '/' in parts.path else url
```

Initialisez BeautifulSoup pour traiter le document HTML :

```
soup = BeautifulSoup(response.text, "lxml")
```

Maintenant, scrapez la page web pour tous les liens et ajoutez-les à leur ensemble correspondant :

```
for link in soup.find_all('a'):
    # extraire l'URL du lien depuis l'ancre
    anchor = link.attrs["href"] if "href" in link.attrs else ''
```

```
if anchor.startswith('/'):
        local_link = base_url + anchor
        local_urls.add(local_link)
    elif strip_base in anchor:
        local_urls.add(anchor)
    elif not anchor.startswith('http'):
        local_link = path + anchor
        local_urls.add(local_link)
    else:
        foreign_urls.add(anchor)
```

Puisque je souhaite limiter mon crawler aux adresses locales uniquement, j'ajoute ce qui suit pour ajouter de nouvelles URL à notre file d'attente :

```
for i in local_urls:
    if not i in new_urls and not i in processed_urls:
        new_urls.append(i)
```

Si vous souhaitez crawler toutes les URL, utilisez :

```
if not link in new_urls and not link in processed_urls:
    new_urls.append(link)
```

**_Avertissement :_** _La manière dont le programme fonctionne actuellement, le crawling des URL étrangères prendra un_ **_TRÈS_** _long moment. Vous pourriez éventuellement avoir des ennuis pour avoir scrapé des sites web sans permission._ **_À utiliser à vos propres risques !_**

![Image](https://cdn-media-1.freecodecamp.org/images/1*Y5DwSdLwAIGOWuuyvp1HnA.png)
_Exemple de sortie_

Voici tout mon code :

Et cela devrait être tout. Vous venez de créer un outil simple pour crawler un site web et cartographier toutes les URL trouvées !

### En conclusion

N'hésitez pas à construire et à améliorer ce code. Par exemple, vous pourriez modifier le programme pour rechercher des adresses e-mail ou des numéros de téléphone sur les pages web pendant que vous les crawlez. Vous pourriez même étendre les fonctionnalités en ajoutant des arguments de ligne de commande pour fournir l'option de définir des fichiers de sortie, limiter les recherches en profondeur, et bien plus encore. Apprenez à créer des interfaces de ligne de commande pour accepter des arguments [ici](https://medium.com/@ahadsheriff/the-best-way-to-make-command-line-interfaces-in-python-e00e8b9d10c9).

Si vous avez des recommandations, des conseils ou des ressources supplémentaires, n'hésitez pas à les partager dans les commentaires !

Merci d'avoir lu ! Si vous avez aimé ce tutoriel et souhaitez plus de contenu comme celui-ci, n'oubliez pas de cliquer sur ce bouton de suivi. ❤️

N'oubliez pas non plus de consulter mon [site web](https://ahadsheriff.com/), [Twitter](https://twitter.com/ahadsheriff), [LinkedIn](https://linkedin.com/in/ahadsheriff), et [Github](https://github.com/ahadsheriff).