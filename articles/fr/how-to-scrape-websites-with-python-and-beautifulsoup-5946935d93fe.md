---
title: Comment scraper des sites web avec Python et BeautifulSoup
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-06-10T14:16:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe
coverImage: https://cdn-media-1.freecodecamp.org/images/1*BrUAg3-OqIHkoTz_CRIzTA.png
tags:
- name: Life Hacking
  slug: life-hacking
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: Comment scraper des sites web avec Python et BeautifulSoup
seo_desc: 'By Justin Yek

  There is more information on the Internet than any human can absorb in a lifetime.
  What you need is not access to that information, but a scalable way to collect,
  organize, and analyze it.

  You need web scraping.

  Web scraping automatical...'
---

Par Justin Yek

Il y a plus d'informations sur Internet que ce qu'un humain peut absorber en une vie. Ce dont vous avez besoin, ce n'est pas d'un accès à ces informations, mais d'une manière scalable pour les collecter, les organiser et les analyser.

Vous avez besoin du web scraping.

Le web scraping extrait automatiquement les données et les présente dans un format que vous pouvez facilement comprendre. Dans ce tutoriel, nous nous concentrerons sur ses applications dans le marché financier, mais le web scraping peut être utilisé dans une grande variété de situations.

Si vous êtes un investisseur passionné, obtenir les prix de clôture chaque jour peut être fastidieux, surtout lorsque les informations dont vous avez besoin se trouvent sur plusieurs pages web. Nous allons faciliter l'extraction des données en construisant un scraper web pour récupérer automatiquement les indices boursiers depuis Internet.

![Image](https://cdn-media-1.freecodecamp.org/images/trTuoesIzruCn5cstkdhl9poG5I8IjL9K5kP)

### Prise en main

Nous allons utiliser Python comme langage de scraping, ainsi qu'une bibliothèque simple et puissante, BeautifulSoup.

* Pour les utilisateurs de Mac, Python est préinstallé dans OS X. Ouvrez le Terminal et tapez `python --version`. Vous devriez voir que votre version de Python est 2.7.x.
* Pour les utilisateurs de Windows, veuillez installer Python via le [site officiel](https://www.python.org/downloads/).

Ensuite, nous devons obtenir la bibliothèque BeautifulSoup en utilisant `pip`, un outil de gestion de paquets pour Python.

Dans le terminal, tapez :

```bash
 easy_install pip
 pip install BeautifulSoup4
```

**Note** : Si vous ne parvenez pas à exécuter les commandes ci-dessus, essayez d'ajouter `sudo` devant chaque ligne.

### Les bases

Avant de nous lancer dans le code, comprenons les bases du HTML et quelques règles de scraping.

**Balises HTML**
Si vous comprenez déjà les balises HTML, vous pouvez sauter cette partie.

```html
<!DOCTYPE html>
<html>
    <head>
    </head>
    <body>
        <h1> Premier Scraping </h1>
        <p> Bonjour le Monde </p>
    <body>
</html>
```

Voici la syntaxe de base d'une page web HTML. Chaque `<balise>` sert de bloc à l'intérieur de la page web :
1. `<!DOCTYPE html>` : Les documents HTML doivent commencer par une déclaration de type.
2. Le document HTML est contenu entre `<html>` et `</html>`.
3. La déclaration meta et script du document HTML est entre `<head>` et `</head>`.
4. La partie visible du document HTML est entre les balises `<body>` et `</body>`.
5. Les titres sont définis avec les balises `<h1>` à `<h6>`.
6. Les paragraphes sont définis avec la balise `<p>`.

D'autres balises utiles incluent `<a>` pour les hyperliens, `<table>` pour les tableaux, `<tr>` pour les lignes de tableau et `<td>` pour les colonnes de tableau.

De plus, les balises HTML viennent parfois avec des attributs `id` ou `class`. L'attribut `id` spécifie un identifiant unique pour une balise HTML et la valeur doit être unique dans le document HTML. L'attribut `class` est utilisé pour définir des styles égaux pour les balises HTML de la même classe. Nous pouvons utiliser ces identifiants et classes pour nous aider à localiser les données que nous voulons.

Pour plus d'informations sur les balises HTML, [id](http://www.w3schools.com/tags/att_global_id.asp) et [class](http://www.w3schools.com/html/html_classes.asp), veuillez consulter les tutoriels de W3Schools [Tutoriels](http://www.w3schools.com/).

**Règles de scraping**

1. Vous devriez vérifier les termes et conditions d'un site web avant de le scraper. Lisez attentivement les déclarations concernant l'utilisation légale des données. Généralement, les données que vous scrapez ne devraient pas être utilisées à des fins commerciales.
2. Ne demandez pas les données du site web trop agressivement avec votre programme (également connu sous le nom de spamming), car cela peut casser le site web. Assurez-vous que votre programme se comporte de manière raisonnable (c'est-à-dire qu'il agit comme un humain). Une requête par seconde pour une page web est une bonne pratique.
3. La mise en page d'un site web peut changer de temps en temps, alors assurez-vous de revisiter le site et de réécrire votre code si nécessaire.

### Inspection de la page

Prenons une page du site [Bloomberg Quote](http://www.bloomberg.com/quote/SPX:IND) comme exemple.

En tant que personne suivant le marché boursier, nous aimerions obtenir le nom de l'indice (S&P 500) et son prix à partir de cette page. Tout d'abord, faites un clic droit et ouvrez l'inspecteur de votre navigateur pour inspecter la page web.

![Image](https://cdn-media-1.freecodecamp.org/images/i3mWoIwj3FWfSPQPnyfBEQn3oWNp5czTCg0U)

Essayez de survoler le prix avec votre curseur et vous devriez voir une boîte bleue l'entourer. Si vous cliquez dessus, le HTML correspondant sera sélectionné dans la console du navigateur.

![Image](https://cdn-media-1.freecodecamp.org/images/2Tnvx-rIrmKbElQGgSnPaNK1xiG6LJI5xwR8)

À partir du résultat, nous pouvons voir que le prix est à l'intérieur de plusieurs niveaux de balises HTML, qui est `<div class="basic-quote">` → `<div class="price-container up">` → `<div class="price">`.

De même, si vous survolez et cliquez sur le nom « S&P 500 Index », il est à l'intérieur de `<div class="basic-quote">` et `<h1 class="name">`.

![Image](https://cdn-media-1.freecodecamp.org/images/o0p8x2WILUOE7lXyS1beHcztnAH63knKOyqd)

Maintenant, nous connaissons l'emplacement unique de nos données grâce aux balises `class`.

### Plongeons dans le code

Maintenant que nous savons où se trouvent nos données, nous pouvons commencer à coder notre scraper web. Ouvrez votre éditeur de texte maintenant !

Tout d'abord, nous devons importer toutes les bibliothèques que nous allons utiliser.

```py
# importer les bibliothèques
import urllib2
from bs4 import BeautifulSoup
```

Ensuite, déclarez une variable pour l'URL de la page.

```py
# spécifier l'url
quote_page = 'http://www.bloomberg.com/quote/SPX:IND'
```

Puis, utilisez urllib2 de Python pour obtenir la page HTML de l'URL déclarée.

```py
# interroger le site web et retourner le html à la variable 'page'
page = urllib2.urlopen(quote_page)
```

Enfin, analysez la page au format BeautifulSoup afin que nous puissions utiliser BeautifulSoup pour travailler dessus.

```py
# analyser le html en utilisant beautiful soup et stocker dans la variable `soup`
soup = BeautifulSoup(page, 'html.parser')
```

Maintenant, nous avons une variable, `soup`, contenant le HTML de la page. Voici où nous pouvons commencer à coder la partie qui extrait les données.

Vous vous souvenez des couches uniques de nos données ? BeautifulSoup peut nous aider à accéder à ces couches et à extraire le contenu avec `find()`. Dans ce cas, puisque la classe HTML `name` est unique sur cette page, nous pouvons simplement interroger `<div class="name">`.

```py
# Extraire le <div> du nom et obtenir sa valeur
name_box = soup.find('h1', attrs={'class': 'name'})
```

Après avoir obtenu la balise, nous pouvons obtenir les données en obtenant son `text`.

```py
name = name_box.text.strip() # strip() est utilisé pour supprimer les espaces de début et de fin
print name
```

De même, nous pouvons obtenir le prix aussi.

```py
# obtenir le prix de l'indice
price_box = soup.find('div', attrs={'class':'price'})
price = price_box.text
print price
```

Lorsque vous exécutez le programme, vous devriez voir qu'il imprime le prix actuel de l'indice S&P 500.

![Image](https://cdn-media-1.freecodecamp.org/images/R7W6VXymQPtfUACuiHkwldc1CuMEs2NYdcW1)

### Exporter vers Excel CSV

Maintenant que nous avons les données, il est temps de les sauvegarder. Le format Excel Comma Separated est un bon choix. Il peut être ouvert dans Excel afin que vous puissiez voir les données et les traiter facilement.

Mais d'abord, nous devons importer le module csv de Python et le module datetime pour obtenir la date d'enregistrement. Insérez ces lignes dans votre code dans la section d'importation.

```py
import csv
from datetime import datetime
```

En bas de votre code, ajoutez le code pour écrire les données dans un fichier csv.

```py
# ouvrir un fichier csv en mode append, afin que les anciennes données ne soient pas effacées
with open('index.csv', 'a') as csv_file:
 writer = csv.writer(csv_file)
 writer.writerow([name, price, datetime.now()])
```

Maintenant, si vous exécutez votre programme, vous devriez pouvoir exporter un fichier `index.csv`, que vous pouvez ensuite ouvrir avec Excel, où vous devriez voir une ligne de données.

![Image](https://cdn-media-1.freecodecamp.org/images/7O7PaHRqlgGALct2ZdjI2K773eGgXMAaJvMH)

Ainsi, si vous exécutez ce programme tous les jours, vous pourrez facilement obtenir le prix de l'indice S&P 500 sans avoir à fouiller dans le site web !

### Aller plus loin (Utilisations avancées)

**Plusieurs indices**
Alors, scraper un seul indice ne vous suffit pas, n'est-ce pas ? Nous pouvons essayer d'extraire plusieurs indices en même temps.

Tout d'abord, modifiez `quote_page` en un tableau d'URLs.

```py
quote_page = ['http://www.bloomberg.com/quote/SPX:IND', 'http://www.bloomberg.com/quote/CCMP:IND']
```

Ensuite, nous changeons le code d'extraction des données en une boucle `for`, qui traitera les URLs une par une et stockera toutes les données dans une variable `data` sous forme de tuples.

```py
# boucle for
data = []
for pg in quote_page:
 # interroger le site web et retourner le html à la variable 'page'
 page = urllib2.urlopen(pg)
 
# analyser le html en utilisant beautiful soap et stocker dans la variable `soup`
 soup = BeautifulSoup(page, 'html.parser')
 
# Extraire le <div> du nom et obtenir sa valeur
 name_box = soup.find('h1', attrs={'class': 'name'})
 name = name_box.text.strip() # strip() est utilisé pour supprimer les espaces de début et de fin
 
# obtenir le prix de l'indice
 price_box = soup.find('div', attrs={'class':'price'})
 price = price_box.text
 
# sauvegarder les données dans un tuple
 data.append((name, price))
```

De plus, modifiez la section de sauvegarde pour sauvegarder les données ligne par ligne.

```py
# ouvrir un fichier csv en mode append, afin que les anciennes données ne soient pas effacées
with open('index.csv', 'a') as csv_file:
 writer = csv.writer(csv_file)
 # La boucle for
 for name, price in data:
 writer.writerow([name, price, datetime.now()])
```

Relancez le programme et vous devriez pouvoir extraire deux indices en même temps !

### Techniques de scraping avancées

BeautifulSoup est simple et idéal pour le scraping web à petite échelle. Mais si vous êtes intéressé par le scraping de données à plus grande échelle, vous devriez envisager d'utiliser ces autres alternatives :

1. [Scrapy](http://scrapy.org/), un puissant framework de scraping Python
2. Essayez d'intégrer votre code avec certaines APIs publiques. L'efficacité de la récupération des données est beaucoup plus élevée que le scraping de pages web. Par exemple, jetez un œil à [Facebook Graph API](https://developers.facebook.com/docs/graph-api), qui peut vous aider à obtenir des données cachées qui ne sont pas affichées sur les pages web de Facebook.
3. Envisagez d'utiliser une base de données backend comme [MySQL](https://www.mysql.com/) pour stocker vos données lorsqu'elles deviennent trop volumineuses.

### Adoptez la méthode DRY

![Image](https://cdn-media-1.freecodecamp.org/images/e71XWhRmRZLario-leNUQuWlNwrMzZXv-e8n)

DRY signifie « Don't Repeat Yourself » (Ne vous répétez pas), essayez d'automatiser vos tâches quotidiennes comme [cette personne](http://www.businessinsider.com/programmer-automates-his-job-2015-11). D'autres projets amusants à considérer pourraient être de suivre le temps actif de vos amis Facebook (avec leur consentement, bien sûr), ou de récupérer une liste de sujets dans un forum et d'essayer le traitement du langage naturel (qui est un sujet brûlant pour l'intelligence artificielle en ce moment) !

Si vous avez des questions, n'hésitez pas à laisser un commentaire ci-dessous.

**Références**
[http://www.gregreda.com/2013/03/03/web-scraping-101-with-python/](http://www.gregreda.com/2013/03/03/web-scraping-101-with-python/)
[http://www.analyticsvidhya.com/blog/2015/10/beginner-guide-web-scraping-beautiful-soup-python/](http://www.analyticsvidhya.com/blog/2015/10/beginner-guide-web-scraping-beautiful-soup-python/)

_Cet article a été initialement publié sur le blog d'Altitude Labs [blog](http://altitudelabs.com/blog/) et a été écrit par notre ingénieur logiciel, [Leonard Mok](https://medium.com/@leonardmok). [Altitude Labs](http://altitudelabs.com) est une agence logicielle spécialisée dans les applications React personnalisées et mobiles._