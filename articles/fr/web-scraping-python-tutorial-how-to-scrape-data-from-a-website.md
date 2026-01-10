---
title: Tutoriel de Web Scraping Python – Comment extraire des données d'un site web
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-25T20:24:10.000Z'
originalURL: https://freecodecamp.org/news/web-scraping-python-tutorial-how-to-scrape-data-from-a-website
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/webscrapingposter.jpg
tags:
- name: Python
  slug: python
- name: web scraping
  slug: web-scraping
seo_title: Tutoriel de Web Scraping Python – Comment extraire des données d'un site
  web
seo_desc: 'By Mehul Mohan

  Python is a beautiful language to code in. It has a great package ecosystem, there''s
  much less noise than you''ll find in other languages, and it is super easy to use.

  Python is used for a number of things, from data analysis to server ...'
---

Par Mehul Mohan

Python est un langage magnifique pour coder. Il dispose d'un écosystème de packages formidable, il y a beaucoup moins de bruit que dans d'autres langages, et il est super facile à utiliser.

Python est utilisé pour de nombreuses choses, de l'analyse de données à la programmation serveur. Et un cas d'utilisation passionnant de Python est le Web Scraping.

Dans cet article, nous allons couvrir comment utiliser Python pour le web scraping. Nous allons également travailler à travers un guide pratique complet de classe au fur et à mesure que nous avançons.

_Note : Nous allons scraper une page web que j'héberge, afin que nous puissions apprendre le scraping en toute sécurité. De nombreuses entreprises n'autorisent pas le scraping sur leurs sites web, donc c'est une bonne façon d'apprendre. Assurez-vous simplement de vérifier avant de scraper._

## Introduction au Web Scraping en classe

![Image](https://www.freecodecamp.org/news/content/images/2020/09/screenzy-1601054558203.png)
_Aperçu de la classe codedamn_

Si vous souhaitez coder en même temps, vous pouvez utiliser [cette classe gratuite codedamn](https://codedamn.com/practice/web-scraping-python-beautifulsoup) qui se compose de plusieurs laboratoires pour vous aider à apprendre le web scraping. Ce sera un exercice d'apprentissage pratique sur codedamn, similaire à la façon dont vous apprenez sur freeCodeCamp.

Dans cette classe, vous utiliserez cette page pour tester le web scraping : [https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/](https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/)

Cette classe se compose de 7 laboratoires, et vous résoudrez un laboratoire dans chaque partie de cet article de blog. Nous utiliserons Python 3.8 + BeautifulSoup 4 pour le web scraping.

## Partie 1 : Chargement des pages web avec 'request'

Voici le [lien vers ce laboratoire](https://codedamn.com/practice/web-scraping-python-beautifulsoup/a674e637-d958-4527-8930-cc53d1fb68e9).

Le module `requests` vous permet d'envoyer des requêtes HTTP en utilisant Python.

La requête HTTP retourne un objet Response avec toutes les données de réponse (contenu, encodage, statut, etc.). Un exemple pour obtenir le HTML d'une page :

```py
import requests

res = requests.get('https://codedamn.com')

print(res.text)
print(res.status_code)
```

### Conditions de validation :

* Obtenez le contenu de l'URL suivante en utilisant le module `requests` : **https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/**
* Stockez la réponse texte (comme montré ci-dessus) dans une variable appelée `txt`
* Stockez le code de statut (comme montré ci-dessus) dans une variable appelée `status`
* Affichez `txt` et `status` en utilisant la fonction `print`

Une fois que vous comprenez ce qui se passe dans le code ci-dessus, il est assez simple de valider ce laboratoire. Voici la solution de ce laboratoire :

```py
import requests

# Faire une requête à https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/
# Stocker le résultat dans la variable 'res'
res = requests.get(
    'https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/')
txt = res.text
status = res.status_code

print(txt, status)
# afficher le résultat
```

Passons maintenant à la partie 2 où vous allez construire davantage sur votre code existant.

## Partie 2 : Extraction du titre avec BeautifulSoup

Voici le [lien vers ce laboratoire](https://codedamn.com/practice/web-scraping-python-beautifulsoup/e55282e8-8481-4fb9-9a95-5df4d4a526ce).

Dans cette classe, vous allez utiliser une bibliothèque appelée `BeautifulSoup` en Python pour faire du web scraping. Certaines fonctionnalités qui font de BeautifulSoup une solution puissante sont :

1. Il fournit de nombreuses méthodes simples et idiomes Pythoniques pour naviguer, rechercher et modifier un arbre DOM. Il ne faut pas beaucoup de code pour écrire une application
2. Beautiful Soup s'appuie sur des parseurs Python populaires comme lxml et html5lib, vous permettant d'essayer différentes stratégies de parsing ou de troquer la vitesse contre la flexibilité.

En gros, BeautifulSoup peut parser tout ce que vous lui donnez sur le web.

Voici un exemple simple de BeautifulSoup :

```py
from bs4 import BeautifulSoup

page = requests.get("https://codedamn.com")
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.title.text # vous obtient le texte du <title>(...)</title>
```

### Conditions de validation :

* Utilisez le package `requests` pour obtenir le titre de l'URL : https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/
* Utilisez BeautifulSoup pour stocker le titre de cette page dans une variable appelée `page_title`

En regardant l'exemple ci-dessus, vous pouvez voir qu'une fois que nous avons alimenté le `page.content` dans BeautifulSoup, vous pouvez commencer à travailler avec l'arbre DOM analysé de manière très pythonique. La solution pour le laboratoire serait :

```py
import requests
from bs4 import BeautifulSoup

# Faire une requête à https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/
page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')

# Extraire le titre de la page
page_title = soup.title.text

# afficher le résultat
print(page_title)
```

C'était aussi un laboratoire simple où nous devions changer l'URL et afficher le titre de la page. Ce code validerait le laboratoire.

## Partie 3 : Corps et tête de la soupe

Voici le [lien vers ce laboratoire](https://codedamn.com/practice/web-scraping-python-beautifulsoup/a91108fd-2f13-4640-ac62-d7877235376a).

Dans le dernier laboratoire, vous avez vu comment extraire le `title` de la page. Il est tout aussi facile d'extraire certaines sections également.

Vous avez également vu que vous devez appeler `.text` sur ceux-ci pour obtenir la chaîne, mais vous pouvez les afficher sans appeler `.text` également, et cela vous donnera le balisage complet. Essayez d'exécuter l'exemple ci-dessous :

```py
import requests
from bs4 import BeautifulSoup

# Faire une requête
page = requests.get(
    "https://codedamn.com")
soup = BeautifulSoup(page.content, 'html.parser')

# Extraire le titre de la page
page_title = soup.title.text

# Extraire le corps de la page
page_body = soup.body

# Extraire la tête de la page
page_head = soup.head

# afficher le résultat
print(page_body, page_head)
```

Regardons comment vous pouvez extraire les sections `body` et `head` de vos pages.

### Conditions de validation :

* Répétez l'expérience avec l'URL : `https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/`
* Stockez le titre de la page (sans appeler .text) de l'URL dans `page_title`
* Stockez le contenu du corps (sans appeler .text) de l'URL dans `page_body`
* Stockez le contenu de la tête (sans appeler .text) de l'URL dans `page_head`

Lorsque vous essayez d'afficher le `page_body` ou `page_head`, vous verrez qu'ils sont affichés sous forme de `strings`. Mais en réalité, lorsque vous `print(type page_body)`, vous verrez qu'il ne s'agit pas d'une chaîne mais cela fonctionne bien.

La solution de cet exemple serait simple, basée sur le code ci-dessus :

```py
import requests
from bs4 import BeautifulSoup

# Faire une requête
page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')

# Extraire le titre de la page
page_title = soup.title

# Extraire le corps de la page
page_body = soup.body

# Extraire la tête de la page
page_head = soup.head

# afficher le résultat
print(page_title, page_head)
```

## Partie 4 : select avec BeautifulSoup

Voici le [lien vers ce laboratoire](https://codedamn.com/practice/web-scraping-python-beautifulsoup/0ee9fa0e-e7ac-4afa-ad8a-b4b3d16900ef).

Maintenant que vous avez exploré certaines parties de BeautifulSoup, voyons comment vous pouvez sélectionner des éléments DOM avec les méthodes BeautifulSoup.

Une fois que vous avez la variable `soup` (comme dans les laboratoires précédents), vous pouvez travailler avec `.select` sur celle-ci qui est un sélecteur CSS à l'intérieur de BeautifulSoup. C'est-à-dire que vous pouvez descendre dans l'arbre DOM tout comme vous sélectionnez des éléments avec CSS. Regardons un exemple :

```py
import requests
from bs4 import BeautifulSoup

# Faire une requête
page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')

# Extraire le premier texte <h1>(...)</h1>
first_h1 = soup.select('h1')[0].text
```

`.select` retourne une liste Python de tous les éléments. C'est pourquoi vous avez sélectionné uniquement le premier élément ici avec l'index `[0]`.

### Conditions de validation :

* Créez une variable `all_h1_tags`. Définissez-la comme une liste vide.
* Utilisez `.select` pour sélectionner toutes les balises `<h1>` et stockez le texte de ces h1 dans la liste `all_h1_tags`.
* Créez une variable `seventh_p_text` et stockez le texte du 7ème élément `p` (index 6) à l'intérieur.

La solution pour ce laboratoire est :

```py
import requests
from bs4 import BeautifulSoup
# Faire une requête
page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')

# Créer all_h1_tags comme une liste vide
all_h1_tags = []

# Définir all_h1_tags sur toutes les balises h1 de la soupe
for element in soup.select('h1'):
    all_h1_tags.append(element.text)

# Créer seventh_p_text et le définir sur le texte du 7ème élément p de la page
seventh_p_text = soup.select('p')[6].text

print(all_h1_tags, seventh_p_text)

```

Continuons.

## Partie 5 : Les éléments les plus scrapés en ce moment

Voici le [lien vers ce laboratoire](https://codedamn.com/practice/web-scraping-python-beautifulsoup/0f404796-1b8f-491b-9b50-9e47893d2e47).

Allons-y et extrayons les éléments les plus scrapés de l'URL : https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/

Si vous ouvrez cette page dans un nouvel onglet, vous verrez certains éléments en tête. Dans ce laboratoire, votre tâche est d'extraire leurs noms et de les stocker dans une liste appelée `top_items`. Vous allez également extraire les avis pour ces éléments.

Pour réussir ce défi, prenez soin des éléments suivants :

* Utilisez `.select` pour extraire les titres. (Indice : un sélecteur pour les titres de produits pourrait être `a.title`)
* Utilisez `.select` pour extraire l'étiquette de compte de révisions pour ces titres de produits. (Indice : un sélecteur pour les révisions pourrait être `div.ratings`) Note : il s'agit d'une étiquette complète (c'est-à-dire **2 reviews**) et non seulement d'un nombre.
* Créez un nouveau dictionnaire au format :

```py
info = {
   "title": 'Asus AsusPro Adv...   '.strip(),
   "review": '2 reviews\n\n\n'.strip()
}
```

* Notez que vous utilisez la méthode `strip` pour supprimer les nouvelles lignes/espaces supplémentaires que vous pourriez avoir dans la sortie. Cela est **important** pour réussir ce laboratoire.
* Ajoutez ce dictionnaire dans une liste appelée `top_items`
* Affichez cette liste à la fin

Il y a plusieurs tâches à accomplir dans ce défi. Regardons d'abord la solution et comprenons ce qui se passe :

```py
import requests
from bs4 import BeautifulSoup
# Faire une requête
page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')

# Créer top_items comme une liste vide
top_items = []

# Extraire et stocker dans top_items selon les instructions à gauche
products = soup.select('div.thumbnail')
for elem in products:
    title = elem.select('h4 > a.title')[0].text
    review_label = elem.select('div.ratings')[0].text
    info = {
        "title": title.strip(),
        "review": review_label.strip()
    }
    top_items.append(info)

print(top_items)
```

Notez que ce n'est qu'une des solutions. Vous pouvez également tenter cela d'une autre manière. Dans cette solution :

1. Tout d'abord, vous sélectionnez tous les éléments `div.thumbnail` qui vous donnent une liste de produits individuels
2. Ensuite, vous itérez sur eux
3. Parce que `select` vous permet de chaîner sur lui-même, vous pouvez utiliser select à nouveau pour obtenir le titre.
4. Notez que parce que vous exécutez déjà dans une boucle pour `div.thumbnail`, le sélecteur `h4 > a.title` ne vous donnera qu'un seul résultat, à l'intérieur d'une liste. Vous sélectionnez le 0ème élément de cette liste et extrayez le texte.
5. Enfin, vous supprimez les espaces supplémentaires et l'ajoutez à votre liste.

Simple, non ?

## Partie 6 : Extraction des liens

Voici le [lien vers ce laboratoire](https://codedamn.com/practice/web-scraping-python-beautifulsoup/be9b007a-ff03-45d5-ad44-1adecdb21e2a).

Jusqu'à présent, vous avez vu comment extraire le texte, ou plutôt le innerText des éléments. Voyons maintenant comment vous pouvez extraire les attributs en extrayant les liens de la page.

Voici un exemple de la façon d'extraire toutes les informations d'image de la page :

```py
import requests
from bs4 import BeautifulSoup
# Faire une requête
page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')

# Créer top_items comme une liste vide
image_data = []

# Extraire et stocker dans top_items selon les instructions à gauche
images = soup.select('img')
for image in images:
    src = image.get('src')
    alt = image.get('alt')
    image_data.append({"src": src, "alt": alt})

print(image_data)
```

Dans ce laboratoire, votre tâche est d'extraire l'attribut `href` des liens avec leur `text` également. Assurez-vous des éléments suivants :

* Vous devez créer une liste appelée `all_links`
* Dans cette liste, stockez toutes les informations de dictionnaire des liens. Cela doit être au format suivant :

```py
info = {
   "href": "<link here>",
   "text": "<link text here>"
}
```

* Assurez-vous que votre `text` est dépouillé de tout espace blanc
* Assurez-vous de vérifier si votre `.text` est None avant d'appeler `.strip()` dessus.
* Stockez tous ces dictionnaires dans `all_links`
* Affichez cette liste à la fin

Vous extrayez les valeurs des attributs tout comme vous extrayez les valeurs d'un dictionnaire, en utilisant la fonction `get`. Regardons la solution de ce laboratoire :

```py
import requests
from bs4 import BeautifulSoup
# Faire une requête
page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')

# Créer top_items comme une liste vide
all_links = []

# Extraire et stocker dans top_items selon les instructions à gauche
links = soup.select('a')
for ahref in links:
    text = ahref.text
    text = text.strip() if text is not None else ''

    href = ahref.get('href')
    href = href.strip() if href is not None else ''
    all_links.append({"href": href, "text": text})

print(all_links)

```

Ici, vous extrayez l'attribut `href` tout comme vous l'avez fait dans le cas de l'image. La seule chose que vous faites est de vérifier également s'il est None. Nous voulons le définir comme une chaîne vide, sinon nous voulons supprimer les espaces blancs.

## Partie 7 : Génération de CSV à partir des données

Voici le [lien vers ce laboratoire](https://codedamn.com/practice/web-scraping-python-beautifulsoup/a10e33c1-7780-40bc-a541-adc632fab185).

Enfin, comprenons comment vous pouvez générer un CSV à partir d'un ensemble de données. Vous allez créer un CSV avec les en-têtes suivants :

1. Nom du produit
2. Prix
3. Description
4. Avis
5. Image du produit

Ces produits sont situés dans le `div.thumbnail`. Le code de base du CSV est donné ci-dessous :

```py
import requests
from bs4 import BeautifulSoup
import csv
# Faire une requête
page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')

all_products = []

products = soup.select('div.thumbnail')
for product in products:
    # TODO: Travail
    print("Travail sur le produit ici")


keys = all_products[0].keys()

with open('products.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(all_products)

```

Vous devez extraire les données du site web et générer ce CSV pour les trois produits.

### Conditions de validation :

* Le nom du produit est la version épurée des espaces du nom de l'article (exemple - Asus AsusPro Adv..)
* Le prix est l'étiquette de prix complète épurée des espaces du produit (exemple - $1101.83)
* La description est la version épurée des espaces de la description du produit (exemple - Asus AsusPro Advanced BU401LA-FA271G Dark Grey, 14", Core i5-4210U, 4GB, 128GB SSD, Win7 Pro)
* Les avis sont la version épurée des espaces du produit (exemple - 7 reviews)
* L'image du produit est l'URL (attribut src) de l'image pour un produit (exemple - /webscraper-python-codedamn-classroom-website/cart2.png)
* Le nom du fichier CSV doit être **products.csv** et doit être stocké dans le même répertoire que votre fichier **script.py**

Regardons la solution de ce laboratoire :

```py
import requests
from bs4 import BeautifulSoup
import csv
# Faire une requête
page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')

# Créer top_items comme une liste vide
all_products = []

# Extraire et stocker dans top_items selon les instructions à gauche
products = soup.select('div.thumbnail')
for product in products:
    name = product.select('h4 > a')[0].text.strip()
    description = product.select('p.description')[0].text.strip()
    price = product.select('h4.price')[0].text.strip()
    reviews = product.select('div.ratings')[0].text.strip()
    image = product.select('img')[0].get('src')

    all_products.append({
        "name": name,
        "description": description,
        "price": price,
        "reviews": reviews,
        "image": image
    })


keys = all_products[0].keys()

with open('products.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(all_products)

```

Le bloc `for` est le plus intéressant ici. Vous extrayez tous les éléments et attributs de ce que vous avez appris jusqu'à présent dans tous les laboratoires.

Lorsque vous exécutez ce code, vous obtenez un beau fichier CSV. Et c'est à peu près tout ce qu'il y a à savoir sur les bases du web scraping avec BeautifulSoup !

## Conclusion

J'espère que cette classe interactive de [codedamn](https://codedamn.com) vous a aidé à comprendre les bases du web scraping avec Python.

Si vous avez aimé cette classe et ce blog, parlez-moi-en sur mon [twitter](https://twitter.com/mehulmpt) et [Instagram](https://instagram.com/mehulmpt). J'adorerais avoir des retours !