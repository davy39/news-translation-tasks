---
title: Le guide complet pour extraire les meilleurs films à la télévision depuis le
  web
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-03T22:30:01.000Z'
originalURL: https://freecodecamp.org/news/scrape-the-web-for-top-rated-movies-on-tv
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/0_D52CsZmqCYvifA3M.jpeg
tags:
- name: Python
  slug: python
- name: '#Scrapy'
  slug: scrapy
- name: web scraping
  slug: web-scraping
seo_title: Le guide complet pour extraire les meilleurs films à la télévision depuis
  le web
seo_desc: 'By Bert Carremans

  In this article, I will show how to scrape the internet for top-rated films with
  the Scrapy framework. The goal of this web scraper is to find films that have a
  high user rating on The Movie Database. The list with these films will ...'
---

Par Bert Carremans

Dans cet article, je vais montrer comment extraire des informations sur les films les mieux notés avec le **_framework Scrapy_** (http://scrapy.org/). L'**_objectif_** de ce scraper web est de trouver des films qui ont une note élevée sur [The Movie Database](https://www.themoviedb.org/). La liste de ces films sera stockée dans une **_base de données SQLite_** et **_envoyée par email_**. Ainsi, vous saurez que vous ne manquerez plus jamais un blockbuster à la télévision.

# Trouver une bonne page web à scraper

Je commence par un guide TV en ligne pour trouver des films sur les chaînes de télévision belges. Mais vous pourriez facilement adapter mon code pour l'utiliser sur n'importe quel autre site web. Pour faciliter votre tâche lors de l'extraction de films, assurez-vous que le site web que vous souhaitez scraper :

* a des balises HTML avec une **_classe ou un id compréhensible_**
* utilise des classes et des ids de manière **_cohérente_**
* a des **_URLs bien structurées_**
* contient toutes les **_chaînes de télévision sur une seule page_**
* a une **_page séparée par jour de la semaine_**
* **_liste uniquement des films_** et aucun autre type de programme comme des émissions en direct, des nouvelles, des reportages, etc. Sauf si vous pouvez facilement distinguer les films des autres types de programmes.

Avec les résultats trouvés, nous allons scraper [**_The Movie Database_**](https://www.themoviedb.org/) (TMDB) pour obtenir la note du film et quelques autres informations.

# Décider quelles informations stocker

Je vais extraire les informations suivantes sur les films :

* titre du film
* chaîne de télévision
* l'heure à laquelle le film commence
* la date à laquelle le film est diffusé à la télévision
* genre
* intrigue
* date de sortie
* lien vers la page de détails sur TMDB
* note TMDB

Vous pourriez compléter cette liste avec tous les acteurs, le réalisateur, des faits intéressants sur le film, etc. – toutes les informations que vous aimeriez connaître.

Dans Scrapy, ces informations seront stockées dans les champs d'un **_Item_**.

# Créer le projet Scrapy

Je vais supposer que vous avez Scrapy installé. Si ce n'est pas le cas, vous pouvez suivre l'excellent [guide d'installation de Scrapy](http://doc.scrapy.org/en/latest/intro/install.html).

Lorsque Scrapy est installé, ouvrez la ligne de commande et allez dans le répertoire où vous souhaitez stocker le projet Scrapy. Ensuite, exécutez :

```
scrapy startproject topfilms
```

Cela créera une structure de dossiers pour le projet des meilleurs films comme montré ci-dessous. Vous pouvez ignorer le fichier topfilms.db pour l'instant. Il s'agit de la base de données SQLite que nous créerons dans le prochain article sur les Pipelines.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/0_dZ6phochXc8Dq1L6.png)

# Définir les Items Scrapy

Nous allons travailler avec le fichier **_items.py_**. Items.py est créé par défaut lors de la création de votre projet Scrapy.

Un `scrapy.Item` est un conteneur qui sera rempli pendant le scraping web. Il contiendra tous les champs que nous voulons extraire de la ou des pages web. Le contenu de l'Item peut être accédé de la même manière qu'un **_dictionnaire Python_**.

Ouvrez items.py et ajoutez une `classe scrapy.Item` avec les champs suivants :

```python
import scrapy
class TVGuideItem(scrapy.Item):
    title = scrapy.Field()
    channel = scrapy.Field()
    start_ts = scrapy.Field()
    film_date_long = scrapy.Field()
    film_date_short = scrapy.Field()
    genre = scrapy.Field()
    plot = scrapy.Field()
    rating = scrapy.Field()
    tmdb_link = scrapy.Field()
    release_date = scrapy.Field()
    nb_votes = scrapy.Field()
```

# Traiter les Items avec les Pipelines

Après avoir démarré un nouveau projet Scrapy, vous aurez un fichier appelé **pipelines.py**. Ouvrez ce fichier et copiez-collez le code montré ci-dessous. Ensuite, je vous montrerai étape par étape ce que chaque partie du code fait.

```python
import sqlite3 as lite
con = None  # connexion à la base de données
class StoreInDBPipeline(object):
    def __init__(self):
        self.setupDBCon()
        self.dropTopFilmsTable()
        self.createTopFilmsTable()
def process_item(self, item, spider):
    self.storeInDb(item)
    return item
def storeInDb(self, item):
    self.cur.execute("INSERT INTO topfilms(\
    title, \
    channel, \
    start_ts, \
    film_date_long, \
    film_date_short, \
    rating, \
    genre, \
    plot, \
    tmdb_link, \
    release_date, \
    nb_votes \
    ) \
    VALUES( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )",
    (
    item['title'],
    item['channel'],
    item['start_ts'],
    item['film_date_long'],
    item['film_date_short'],
    float(item['rating']),
    item['genre'],
    item['plot'],
    item['tmdb_link'],
    item['release_date'],
    item['nb_votes']
    ))
    self.con.commit()
def setupDBCon(self):
    self.con = lite.connect('topfilms.db')
    self.cur = self.con.cursor()
def __del__(self):
    self.closeDB()
def createTopFilmsTable(self):
    self.cur.execute("CREATE TABLE IF NOT EXISTS topfilms(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, \
    title TEXT, \
    channel TEXT, \
    start_ts TEXT, \
    film_date_long TEXT, \
    film_date_short TEXT, \
    rating TEXT, \
    genre TEXT, \
    plot TEXT, \
    tmdb_link TEXT, \
    release_date TEXT, \
    nb_votes \
    )")
def dropTopFilmsTable(self):
    self.cur.execute("DROP TABLE IF EXISTS topfilms")
    
    def closeDB(self):
    self.con.close()
```

Tout d'abord, nous commençons par importer le [package SQLite](https://docs.python.org/2/library/sqlite3.html) et lui donnons l'alias `lite`. Nous initialisons également une variable `con` qui est utilisée pour la connexion à la base de données.

## Créer une classe pour stocker les Items dans la base de données

Ensuite, vous créez une [**_classe_**](https://docs.python.org/2/tutorial/classes.html) avec un nom logique. Après avoir activé le pipeline dans le fichier de paramètres (plus d'informations à ce sujet plus tard), cette classe sera appelée.

```python
class StoreInDBPipeline(object):
```

## Définir la méthode constructeur

La méthode constructeur est la méthode avec le nom `__init__`. Cette méthode est automatiquement exécutée lors de la création d'une instance de la classe `StoreInDBPipeline`.

```python
def __init__(self):
    self.setupDBCon()
    self.dropTopFilmsTable()
    self.createTopFilmsTable()
```

Dans la méthode constructeur, nous lançons trois autres méthodes qui sont définies sous la méthode constructeur.

## Méthode SetupDBCon

Avec la méthode `setupDBCon`, nous créons la base de données `topfilms` (si elle n'existait pas encore) et établissons une connexion avec la fonction `connect`.

```python
def setupDBCon(self):
    self.con = lite.connect('topfilms.db')
	self.cur = self.con.cursor()
```

Ici, nous utilisons l'alias lite pour le package SQLite. Deuxièmement, nous créons un objet Curseur avec la fonction `cursor`. Avec cet objet Curseur, nous pouvons exécuter des instructions SQL dans la base de données.

## Méthode DropTopFilmsTable

La deuxième méthode appelée dans le constructeur est `dropTopFilmsTable`. Comme son nom l'indique, elle supprime la table dans la base de données SQLite.

Chaque fois que le scraper web est exécuté, la base de données sera complètement supprimée. C'est à vous de décider si vous souhaitez faire de même. Si vous souhaitez effectuer des requêtes ou des analyses sur les données des films, vous pourriez conserver les résultats de chaque exécution.

Je veux simplement voir les films les mieux notés des jours à venir et rien de plus. Par conséquent, j'ai décidé de supprimer la base de données à chaque exécution.

```python
def dropTopFilmsTable(self):
    self.cur.execute("DROP TABLE IF EXISTS topfilms")
```

Avec l'objet Curseur `cur`, nous exécutons l'instruction `DROP`.

## Méthode CreateTopFilmsTable

Après avoir supprimé la table des meilleurs films, nous devons la créer. Cela est fait par le dernier appel de méthode dans la méthode constructeur.

```python
def createTopFilmsTable(self):
    self.cur.execute("CREATE TABLE IF NOT EXISTS topfilms(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, \
    title TEXT, \
    channel TEXT, \
    start_ts TEXT, \
    film_date_long TEXT, \
    film_date_short TEXT, \
    rating TEXT, \
    genre TEXT, \
    plot TEXT, \
    tmdb_link TEXT, \
    release_date TEXT, \
    nb_votes \
    )")
```

Encore une fois, nous utilisons l'objet Curseur `cur` pour exécuter l'instruction `CREATE TABLE`. Les champs ajoutés à la table des meilleurs films sont les mêmes que dans l'Item Scrapy que nous avons créé précédemment. Pour simplifier les choses, j'utilise exactement les mêmes noms dans la table SQLite que dans l'Item. Seul le champ `id` est supplémentaire.

_**Note de côté**_ : une bonne application pour visualiser vos bases de données SQLite est le [plugin SQLite Manager dans Firefox](https://addons.mozilla.org/nl/firefox/addon/sqlite-manager/). Vous pouvez regarder ce [tutoriel SQLite Manager sur Youtube](https://youtu.be/y-yA7YT-7gw) pour apprendre à utiliser ce plugin.

## Méthode Process_item

Cette méthode doit être implémentée dans la classe Pipeline et elle doit retourner un dict, un Item ou une exception DropItem. Dans notre scraper web, nous retournerons l'item.

```python
def process_item(self, item, spider):
    self.storeInDb(item)
	return item
```

Contrairement aux autres méthodes expliquées, elle a deux arguments supplémentaires. L'`item` qui a été scrapé et le `spider` qui a scrapé l'item. À partir de cette méthode, nous lançons la méthode `storeInDb` et retournons ensuite l'item.

## Méthode StoreInDb

Cette méthode exécute une instruction `INSERT` pour insérer l'item scrapé dans la base de données SQLite.

```python
def storeInDb(self, item):
    self.cur.execute("INSERT INTO topfilms(\
    title, \
    channel, \
    start_ts, \
    film_date_long, \
    film_date_short, \
    rating, \
    genre, \
    plot, \
    tmdb_link, \
    release_date, \
    nb_votes \
    ) \
    VALUES( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )",
                     (
                         item['title'],
                         item['channel'],
                         item['start_ts'],
                         item['film_date_long'],
                         item['film_date_short'],
                         float(item['rating']),
                         item['genre'],
                         item['plot'],
                         item['tmdb_link'],
                         item['release_date'],
                         item['nb_votes']
                     ))
    self.con.commit()
```

Les valeurs pour les champs de la table proviennent de l'item, qui est un argument pour cette méthode. Ces valeurs sont simplement appelées comme une valeur de dictionnaire (rappelons qu'un Item n'est rien de plus qu'un dictionnaire ?).

## Chaque constructeur a un... destructeur

Le contrepartie de la méthode constructeur est la méthode destructeur avec le nom `__del__`. Dans la méthode destructeur pour cette classe de pipelines, nous fermons la connexion à la base de données.

```python
def __del__(self):
    self.closeDB()
```

## Méthode CloseDB

```python
def closeDB(self):
    self.con.close()
```

Dans cette dernière méthode, nous fermons la connexion à la base de données avec la fonction `close`. Nous avons donc écrit un pipeline entièrement fonctionnel. Il reste encore une dernière étape pour activer le pipeline.

## Activer le pipeline dans settings.py

Ouvrez le fichier **_settings.py_** et ajoutez le code suivant :

```python
ITEM_PIPELINES = {
    'topfilms.pipelines.StoreInDBPipeline':1
}
```

La **_valeur entière_** indique l'ordre dans lequel les pipelines sont exécutés. Comme nous n'avons qu'un seul pipeline, nous lui attribuons la valeur 1.

# Créer un Spider dans Scrapy

Maintenant, nous allons examiner le cœur de Scrapy, le **_Spider_**. C'est ici que le travail intensif de votre scraper web sera effectué. Je vais vous montrer étape par étape comment en créer un.

## Importer les packages nécessaires

Tout d'abord, nous allons importer les packages et modules nécessaires. Nous utilisons le module `CrawlSpider` pour suivre les liens dans le guide TV en ligne.

`Rule` et `LinkExtractor` sont utilisés pour déterminer quels liens nous voulons suivre.

Le module `config` contient certaines constantes comme `DOM_1, DOM_2` et `START_URL` qui sont utilisées dans le Spider. Le module config se trouve un répertoire au-dessus du répertoire actuel. C'est pourquoi vous voyez deux points avant le module config.

Et enfin, nous importons le `TVGuideItem`. Ce TVGuideItem sera utilisé pour contenir les informations pendant le scraping.

```python
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from fuzzywuzzy import fuzz
from ..config import *
from topfilms.items import TVGuideItem
```

## Dire au Spider où aller

Deuxièmement, nous sous-classons la classe CrawlSpider. Cela est fait en insérant CrawlSpider comme argument pour la classe `TVGuideSpider`.

Nous donnons au Spider un `nom`, fournissons les `domaines autorisés` (par exemple, themoviedb.org) et les `start_urls`. Les start_urls est dans mon cas la page web du guide TV, donc vous devriez la changer par votre propre site web préféré.

Avec `rules` et l'argument `deny`, nous disons au Spider quelles URLs (ne pas) suivre sur l'URL de départ. L'URL à ne pas suivre est spécifiée avec une expression régulière.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/0_r0r11AyaIBEC7ODH.png)

Je ne suis pas intéressé par les films qui ont été diffusés hier, ne permettez pas au Spider de suivre les URLs se terminant par « _gisteren_ ».

D'accord, mais quelles URLs le Spider doit-il suivre ? Pour cela, j'utilise l'argument `restrict_xpaths`. Il dit de suivre toutes les URLs avec la `class="button button--beta"`. Ce sont en fait des URLs avec des films pour la semaine à venir.

Enfin, avec l'argument `callback`, nous faisons savoir au Spider quoi faire lorsqu'il suit l'une des URLs. Il exécutera la fonction `parse_by_day`. Je vais expliquer cela dans la partie suivante.

```python
class TVGuideSpider(CrawlSpider):
    name = "tvguide"
    allowed_domains = [DOM_1, DOM_2]
    start_urls = [START_URL]
# Extraire les liens de la navigation par jour
    # Nous ne scraperons pas les films d'hier
    rules = (
        Rule(LinkExtractor(allow=(), deny=(r'\/gisteren'), restrict_xpaths=('//a[@class="button button--beta"]',)), callback="parse_by_day", follow= True),
    )
```

## Analyser les URLs suivies

La fonction `parse_by_day`, partie du TVGuideScraper, scrape les pages web avec l'aperçu de tous les films par chaîne par jour. L'argument `response` provient de la `Request` qui a été lancée lors de l'exécution du programme de scraping web.

Sur la page web en cours de scraping, vous devez trouver les éléments HTML utilisés pour afficher les informations qui nous intéressent. Deux bons outils pour cela sont les [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools/) et le [plugin Firebug dans Firefox](https://addons.mozilla.org/nl/firefox/addon/firebug/).

Une chose que nous voulons stocker est la `date` des films que nous scrapons. Cette date peut être trouvée dans le paragraphe (p) dans la div avec `class="grid__col__inner"`. Clairement, c'est quelque chose que vous devriez modifier pour la page que vous scrapez.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/0_-EML6UFd2TbqVCmY.png)

Avec la `méthode xpath` de l'objet Response, nous extrayons le texte dans le paragraphe. J'ai appris beaucoup de cela dans le [tutoriel sur l'utilisation de la fonction xpath](http://zvon.org/comp/r/tut-XPath_1.html).

En utilisant `extract_first`, nous nous assurons de ne pas stocker cette date sous forme de liste. Sinon, cela nous posera des problèmes lors du stockage de la date dans la base de données SQLite.

Par la suite, j'effectue un nettoyage des données sur film_date_long et crée `film_date_short` avec le format AAAAMMJJ. J'ai créé ce format AAAAMMJJ pour trier les films chronologiquement plus tard.

Ensuite, la chaîne de télévision est scrapée. Si elle est dans la liste des `ALLOWED_CHANNELS` (définie dans le module config), nous continuons à scraper le titre et l'heure de début. Ces informations sont stockées dans l'item, qui est initié par `TVGuideItem()`.

Après cela, nous voulons continuer à scraper sur The Movie Database. Nous utiliserons l'URL [**https://www.themoviedb.org/search?query=**](https://www.themoviedb.org/search?query=) pour afficher les résultats de recherche pour le film en cours de scraping. À cette URL, nous voulons ajouter le titre du film (`url_part` dans le code). Nous réutilisons simplement la partie URL trouvée dans le lien sur la page web du guide TV.

Avec cette URL, nous créons une nouvelle requête et continuons sur TMDB. Avec `request.meta['item'] = item`, nous ajoutons les données déjà scrapées à la requête. De cette façon, nous pouvons continuer à remplir notre TVGuideItem actuel.

`Yield request` lance effectivement la requête.

```python
def parse_by_day(self, response):
    film_date_long = response.xpath('//div[@class="grid__col__inner"]/p/text()').extract_first()
    film_date_long = film_date_long.rsplit(',',1)[-1].strip()  # Supprimer le nom du jour et les espaces blancs
    # Créer une date de film avec un format court comme AAAAMMJJ pour trier les résultats chronologiquement
    film_day_parts = film_date_long.split()
    months_list = ['janvier', 'février', 'mars',
                  'avril', 'mai', 'juin', 'juillet',
                  'août', 'septembre', 'octobre',
                  'novembre', 'décembre' ]
    year = str(film_day_parts[2])
    month = str(months_list.index(film_day_parts[1]) + 1).zfill(2)
    day = str(film_day_parts[0]).zfill(2)
    film_date_short = year + month + day
    for col_inner in response.xpath('//div[@class="grid__col__inner"]'):
        chnl = col_inner.xpath('.//div[@class="tv-guide__channel"]/h6/a/text()').extract_first()
        if chnl in ALLOWED_CHANNELS:
            for program in col_inner.xpath('.//div[@class="program"]'):
                item = TVGuideItem()
                item['channel'] = chnl
                item['title'] = program.xpath('.//div[@class="title"]/a/text()').extract_first()
                item['start_ts'] = program.xpath('.//div[@class="time"]/text()').extract_first()
                item['film_date_long'] = film_date_long
                item['film_date_short'] = film_date_short
                detail_link = program.xpath('.//div[@class="title"]/a/@href').extract_first()
                url_part = detail_link.rsplit('/',1)[-1]
                # Extraire les informations de la base de données de films www.themoviedb.org
                request = scrapy.Request("https://www.themoviedb.org/search?query="+url_part,callback=self.parse_tmdb)
                request.meta['item'] = item  # Passer l'item avec la requête à la page de détails
    yield request
```

## Scraper des informations supplémentaires sur The Movie DataBase

Comme vous pouvez le voir dans la requête créée dans la fonction `parse_by_day`, nous utilisons la fonction de rappel `parse_tmdb`. Cette fonction est utilisée lors de la requête pour scraper le site web TMDB.

Dans la première étape, nous obtenons les informations de l'item qui ont été passées par la fonction `parse_by_day`.

La page avec les résultats de recherche sur TMDB peut éventuellement lister plusieurs résultats de recherche pour le même titre de film (url_part passée dans la requête). Nous vérifions également s'il y a des résultats avec `if tmddb_titles`.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/0_ncBMqbk9fzZ-Szi0.png)

Nous utilisons le package [fuzzywuzzy](https://pypi.python.org/pypi/fuzzywuzzy) pour effectuer une correspondance floue sur les titres de films. Afin d'utiliser le package fuzzywuzzy, nous devons ajouter l'instruction `import` avec les instructions d'importation précédentes.

```python
from fuzzywuzzy import fuzz
```

Si nous trouvons une correspondance de 90 %, nous utilisons ce résultat de recherche pour faire le reste du scraping. Nous ne regardons plus les autres résultats de recherche. Pour cela, nous utilisons l'instruction `break`.

Ensuite, nous recueillons le `genre`, la `note` et la `date de sortie` de la page des résultats de recherche de manière similaire à celle dont nous avons utilisé la fonction xpath précédemment. Pour obtenir un format AAAAMMJJ pour la date de sortie, nous exécutons un traitement des données avec les fonctions `split` et `join`.

Encore une fois, nous voulons lancer une nouvelle requête vers la page de détails sur TMDB. Cette requête appellera la fonction `parse_tmdb_detail` pour extraire l'intrigue du film et le nombre de votes sur TMDB. Cela est expliqué dans la section suivante.

```python
def parse_tmdb(self, response):
    item = response.meta['item']  # Utiliser l'item passé


    tmdb_titles = response.xpath('//a[@class="title result"]/text()').extract()
    if tmdb_titles:  # Vérifier s'il y a des résultats sur TMDB
        for tmdb_title in tmdb_titles:
            match_ratio = fuzz.ratio(item['title'], tmdb_title)
            if match_ratio > 90:
                item['genre'] = response.xpath('.//span[@class="genres"]/text()').extract_first()
                item['rating'] = response.xpath('//span[@class="vote_average"]/text()').extract_first()
                release_date = response.xpath('.//span[@class="release_date"]/text()').extract_first()
                release_date_parts = release_date.split('/')
                item['release_date'] = "/".join(
                    [release_date_parts[1].strip(), release_date_parts[0].strip(), release_date_parts[2].strip()])
                tmdb_link = "https://www.themoviedb.org" + response.xpath(
                    '//a[@class="title result"]/@href').extract_first()
                item['tmdb_link'] = tmdb_link
                # Extraire plus d'informations de la page de détails
                request = scrapy.Request(tmdb_link, callback=self.parse_tmdb_detail)
                request.meta['item'] = item  # Passer l'item avec la requête à la page de détails
    yield request
    break  # Nous ne considérons que la première correspondance
    else:
        return
```

## Scraper l'intrigue du film depuis la page de détails

La dernière fonction que nous allons discuter est courte. Comme précédemment, nous obtenons l'item passé par la fonction parse_tmdb et scrapons la page de détails pour l'`intrigue` et le `nombre de votes`.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/0_C-Tj8dZ8yxfx_3gV.png)

À ce stade, nous avons terminé le scraping des informations pour le film. En d'autres termes, l'item pour le film est complètement rempli. Scrapy utilisera ensuite le code écrit dans les pipelines pour traiter ces données et les mettre dans la base de données.

```python
def parse_tmdb_detail(self, response):
    item = response.meta['item']  # Utiliser l'item passé
    item['nb_votes'] = response.xpath('//span[@itemprop="ratingCount"]/text()').extract_first()
    item['plot'] = response.xpath('.//p[@id="overview"]/text()').extract_first()
    yield item
```

# Utiliser les Extensions dans Scrapy

Dans la section sur les Pipelines, nous avons déjà vu comment nous stockons les résultats du scraping dans une base de données SQLite. Maintenant, je vais vous montrer comment vous pouvez **_envoyer les résultats du scraping par email._** De cette façon, vous obtenez un bel aperçu des films les mieux notés pour la semaine à venir dans votre boîte mail.

## Importer les packages nécessaires

Nous allons travailler avec le fichier **_extensions.py_**. Ce fichier est automatiquement créé dans le répertoire racine lorsque vous avez créé le projet Scrapy. Nous commençons par importer les packages que nous utiliserons plus tard dans ce fichier.

```python
import logging
from scrapy import signals
from scrapy.exceptions import NotConfigured
import smtplib
import sqlite3 as lite
from config import *
```

Le package `logging` n'est pas vraiment requis. Mais ce package peut être utile pour déboguer votre programme ou simplement pour écrire quelques informations dans le journal. 
Le module `signals` nous aidera à savoir quand l'araignée a été ouverte et fermée. Nous enverrons l'email avec les films après que l'araignée ait fait son travail.

Du module `scrapy.exceptions`, nous importons la méthode `NotConfigured`. Cela sera levé lorsque l'extension n'est pas configurée dans le fichier **_settings.py_**. Concrètement, le paramètre `MYEXT_ENABLED` doit être défini sur `True`. Nous verrons cela plus tard dans le code.

Le package `smtplib` est importé pour pouvoir envoyer l'email. J'utilise mon adresse Gmail pour envoyer l'email, mais vous pourriez adapter le code dans config.py pour utiliser un autre service d'email.

Enfin, nous importons le package `sqlite3` pour extraire les films les mieux notés de la base de données et importons `config` pour obtenir nos constantes.

## Créer la classe SendEmail dans les extensions

Tout d'abord, nous définissons l'objet `logger`. Avec cet objet, nous pouvons écrire des messages dans le journal à certains événements. Ensuite, nous créons la classe `SendEmail` avec la méthode constructeur. Dans le constructeur, nous attribuons `FROMADDR` et `TOADDR` aux attributs correspondants de la classe. Ces constantes sont définies dans le fichier **_config.py_**. J'ai utilisé mon adresse Gmail pour les deux attributs.

```python
logger = logging.getLogger(__name__)
class SendEmail(object):
    def __init__(self):
        self.fromaddr = FROMADDR
        self.toaddr  = TOADDR
```

## Instancier l'objet d'extension

La première méthode de l'objet `SendEmail` est `from_crawler`. La première vérification que nous faisons est de savoir si `MYEXT_ENABLED` est activé dans le fichier settings.py. Si ce n'est pas le cas, nous levons une exception `NotConfigured`. Lorsque cela se produit, le reste du code dans l'extension n'est pas exécuté.

Dans le fichier **_settings.py_**, nous devons ajouter le code suivant pour activer cette extension.

```python
MYEXT_ENABLED = True
EXTENSIONS = {
    'topfilms.extensions.SendEmail': 500,
    'scrapy.telnet.TelnetConsole': None
}
```

Nous définissons donc le drapeau booléen `MYEXT_ENABLED` sur `True`. Ensuite, nous ajoutons notre propre extension `SendEmail` au dictionnaire `EXTENSIONS`. La valeur entière de 500 spécifie l'ordre dans lequel l'extension doit être exécutée. J'ai également dû désactiver le `TelnetConsole`. Sinon, l'envoi de l'email ne fonctionnait pas. Cette extension est désactivée en mettant `None` au lieu d'une valeur d'ordre entière.

Ensuite, nous instancions l'objet d'extension avec la fonction `cls()`. À cet objet d'extension, nous connectons certains `signals`. Nous sommes intéressés par les signaux `spider_opened` et `spider_closed`. Et enfin, nous retournons l'objet `ext`.

```
@classmethod
def from_crawler(cls, crawler):
    # première vérification si l'extension doit être activée et lever
    # NotConfigured sinon
    if not crawler.settings.getbool('MYEXT_ENABLED'):
        raise NotConfigured
    # instancier l'objet d'extension
    ext = cls()
    # connecter l'objet d'extension aux signaux
    crawler.signals.connect(ext.spider_opened, signal=signals.spider_opened)
    crawler.signals.connect(ext.spider_closed, signal=signals.spider_closed)
    # retourner l'objet d'extension
    return ext
```

## Définir les actions dans l'événement spider_opened

Lorsque l'araignée a été ouverte, nous voulons simplement écrire cela dans le journal. Par conséquent, nous utilisons l'objet `logger` que nous avons créé en haut du code. Avec la méthode `info`, nous écrivons un message dans le journal. `Spider.name` est remplacé par le nom que nous avons défini dans le fichier TVGuideSpider.py.

```python
def spider_opened(self, spider):
    logger.info("opened spider %s", spider.name)
```

## Envoyer l'email après l'événement spider_closed

Dans la dernière méthode de la classe `SendEmail`, nous envoyons l'email contenant l'aperçu des films les mieux notés.

Encore une fois, nous envoyons une notification au journal que l'araignée a été fermée. Deuxièmement, nous créons une connexion à la base de données SQLite contenant tous les films de la semaine à venir pour les **_ALLOWED_CHANNELS_**. Nous sélectionnons les films avec une `note >= 6.5`. Vous pouvez changer la note pour un seuil plus élevé ou plus bas selon vos souhaits. Les films résultants sont ensuite triés par `film_date_short`, qui a le format AAAAMMJJ et par l'heure de début `start_ts`.

Nous récupérons toutes les lignes dans le curseur `cur` et vérifions si nous avons des résultats avec la fonction `len`. Il est possible de n'avoir aucun résultat lorsque vous définissez la note de seuil trop élevée, par exemple.

Avec `for row in data`, nous parcourons chaque film résultant. Nous extrayons toutes les informations intéressantes de la `row`. Pour certaines données, nous appliquons un encodage avec `encode('ascii','ignore')`. Cela permet d'ignorer certains des caractères spéciaux comme 9, 0, 8, etc. Sinon, nous obtenons des erreurs lors de l'envoi de l'email.

Lorsque toutes les données sur le film sont recueillies, nous composons une variable de chaîne `topfilm`. Chaque `topfilm` est ensuite concaténé à la variable `topfilms_overview`, qui sera le message de l'email que nous envoyons. Si nous n'avons aucun film dans notre résultat de requête, nous le mentionnons dans un court message.

À la fin, nous envoyons le message avec l'adresse Gmail, grâce au package `smtplib`.

```python
def spider_closed(self, spider):
    logger.info("closed spider %s", spider.name)
    # Obtenir les films avec une note supérieure à un seuil
    topfilms_overview = ""
    con = lite.connect('topfilms.db')
    cur = con.execute(
        "SELECT title, channel, start_ts, film_date_long, plot, genre, release_date, rating, tmdb_link, nb_votes "
        "FROM topfilms "
        "WHERE rating >= 6.5 "
        "ORDER BY film_date_short, start_ts")


    data = cur.fetchall()
    if len(data) > 0:  # Vérifier si nous avons des enregistrements dans le résultat de la requête
        for row in data:
            title = row[0].encode('ascii', 'ignore')
            channel = row[1]
            start_ts = row[2]
            film_date_long = row[3]
            plot = row[4].encode('ascii', 'ignore')
            genre = row[5]
            release_date = row[6].rstrip()
            rating = row[7]
            tmdb_link = row[8]
            nb_votes = row[9]
            topfilm = ' - '.join([title, channel, film_date_long, start_ts])
            topfilm = topfilm + "\r\n" + "Date de sortie : " + release_date
            topfilm = topfilm + "\r\n" + "Genre : " + str(genre)
            topfilm = topfilm + "\r\n" + "Note TMDB : " + rating + " sur " + nb_votes + " votes"
            topfilm = topfilm + "\r\n" + plot
            topfilm = topfilm + "\r\n" + "Plus d'informations sur : " + tmdb_link
            topfilms_overview = "\r\n\r\n".join([topfilms_overview, topfilm])
    con.close()
    if len(topfilms_overview) > 0:
        message = topfilms_overview
    else:
        message = "Il n'y a pas de films bien notés pour la semaine à venir."
    msg = "\r\n".join([
        "De : " + self.fromaddr,
        "À : " + self.toaddr,
        "Sujet : Aperçu des meilleurs films",
        message
    ])
    username = UNAME
    password = PW
    server = smtplib.SMTP(GMAIL)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(self.fromaddr, self.toaddr, msg)
    server.quit()
```

## Résultat de l'envoi d'emails via Extensions

Le résultat final de ce morceau de code est un aperçu des films les mieux notés dans votre boîte mail. Super ! Maintenant, vous n'avez plus besoin de chercher cela sur le guide TV en ligne.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/0_SuRZuKi2RIkRJD3y.png)

# Astuces pour éviter le bannissement de l'IP

Lorsque vous faites de nombreuses requêtes en peu de temps, vous risquez d'être banni par le serveur. Dans cette section finale, je vais vous montrer quelques astuces pour éviter le bannissement de l'IP.

## Retarder vos requêtes

Une façon simple d'éviter le bannissement de l'IP est de **_faire une pause entre chaque requête_**. Dans Scrapy, cela peut être fait en définissant simplement un paramètre dans le fichier **_settings.py_**. Comme vous l'avez probablement remarqué, le fichier settings.py a beaucoup de paramètres commentés.

Recherchez le paramètre `DOWNLOAD_DELAY` et décommentez-le. J'ai défini la **_durée de la pause à 2 secondes_**. Selon le nombre de requêtes que vous devez faire, vous pouvez changer cela. Mais je le définirais à au moins 1 seconde.

```python
DOWNLOAD_DELAY=2
```

## Méthode plus avancée pour éviter le bannissement de l'IP

Par défaut, chaque fois que vous faites une requête, vous le faites avec le **_même agent utilisateur_**. Grâce au package `fake_useragent`, nous pouvons facilement changer l'agent utilisateur pour chaque requête.

Tous les crédits pour ce morceau de code vont à [Alecxe](https://github.com/alecxe/scrapy-fake-useragent) qui a écrit un joli script Python pour utiliser le package fake_useragent.

Tout d'abord, nous créons un dossier **_scrapy_fake_useragent_** dans le répertoire racine de notre projet de scraper web. Dans ce dossier, nous ajoutons deux fichiers :

* **___init__.py_** qui est un fichier vide
* **_middleware.py_**

Pour utiliser ce [middleware](http://doc.scrapy.org/en/latest/topics/spider-middleware.html), nous devons l'activer dans le fichier **_settings.py_**. Cela se fait avec le code :

```python
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddleware.useragent.UserAgentMiddleware': None,
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
}
```

Tout d'abord, nous désactivons le `UserAgentMiddleware` par défaut de Scrapy en spécifiant _None_ au lieu d'une valeur entière. Ensuite, nous activons notre propre middleware `RandomUserAgentMiddleware`. Intuitivement, le middleware est un morceau de code qui est exécuté **_pendant une requête_**.

Dans le fichier **_middleware.py_**, nous ajoutons le code pour **_randomiser l'agent utilisateur_** pour chaque requête. Assurez-vous d'avoir le package fake_useragent installé. Du [package fake_usergent](https://pypi.python.org/pypi/fake-useragent), nous importons le module `UserAgent`. Celui-ci contient **_une liste de différents agents utilisateurs_**. Dans le constructeur de la classe RandomUserAgentMiddleware, nous instancions l'objet UserAgent. Dans la méthode **_process_request_**, nous définissons l'agent utilisateur sur un agent utilisateur aléatoire de l'objet `ua` dans l'en-tête de la requête.

```python
from fake_useragent import UserAgent
class RandomUserAgentMiddleware(object):
    def __init__(self):
        super(RandomUserAgentMiddleware, self).__init__()
        self.ua = UserAgent()
    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', self.ua.random)
```

# Conclusion

C'est tout ! J'espère que vous avez maintenant une vue claire sur la façon d'utiliser Scrapy pour vos projets de scraping web.