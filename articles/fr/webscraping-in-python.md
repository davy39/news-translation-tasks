---
title: Comment scraper des sites web avec Python 3
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-17T22:51:00.000Z'
originalURL: https://freecodecamp.org/news/webscraping-in-python
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9af8740569d1a4ca28f1.jpg
tags:
- name: Python
  slug: python
- name: web scraping
  slug: web-scraping
seo_title: Comment scraper des sites web avec Python 3
seo_desc: 'By André Jaenisch

  Web scraping is the process of extracting data from websites.

  Before attempting to scrape a website, you should make sure that the provider allows
  it in their terms of service. You should also check to see whether you could use
  an A...'
---

Par André Jaenisch

Le web scraping est le processus d'extraction de données à partir de sites web.

Avant d'essayer de scraper un site web, vous devez vous assurer que le fournisseur l'autorise dans ses conditions d'utilisation. Vous devriez également vérifier si vous pourriez utiliser une API à la place.

Le scraping massif peut mettre un serveur sous une grande pression, ce qui peut entraîner un déni de service. Et vous ne voulez pas cela.

## Qui devrait lire ceci ?

Cet article s'adresse aux lecteurs avancés. Il supposera que vous êtes déjà familier avec le langage de programmation Python.

Au minimum, vous devriez comprendre la compréhension de liste, le gestionnaire de contexte et les fonctions. Vous devriez également savoir comment configurer un environnement virtuel.

Nous exécuterons le code sur votre machine locale pour explorer certains sites web. Avec quelques ajustements, vous pourriez le faire fonctionner sur un serveur également.

## Ce que vous apprendrez dans cet article

À la fin de cet article, vous saurez comment télécharger une page web, l'analyser pour en extraire des informations intéressantes et la formater dans un format utilisable pour un traitement ultérieur. Cela est également connu sous le nom de [ETL](https://en.wikipedia.org/wiki/Extract,_transform,_load).

Cet article expliquera également quoi faire si ce site web utilise JavaScript pour rendre le contenu (comme React.js ou Angular).

## Prérequis

Avant de commencer, je veux m'assurer que nous sommes prêts. Veuillez configurer un environnement virtuel et installer les packages suivants :

* beautifulsoup4 (version 4.9.0 au moment de l'écriture)
* requests (version 2.23.0 au moment de l'écriture)
* wordcloud (version 1.17.0 au moment de l'écriture, optionnel)
* selenium (version 3.141.0 au moment de l'écriture, optionnel)

Vous pouvez trouver le code de ce projet dans ce [dépôt git sur GitHub](https://github.com/Ryuno-Ki/fcc-web-scraping-example).

Pour cet exemple, nous allons scraper la [Loi fondamentale de la République fédérale d'Allemagne](https://www.gesetze-im-internet.de/gg/index.html). (Ne vous inquiétez pas, j'ai vérifié leurs Conditions d'utilisation. Ils offrent une version XML pour le traitement automatique, mais cette page sert d'exemple de traitement HTML. Donc, cela devrait être correct.)

## Étape 1 : Télécharger la source

D'abord, je crée un fichier `urls.txt` contenant toutes les URLs que je veux télécharger :

```
https://www.gesetze-im-internet.de/gg/art_1.html
https://www.gesetze-im-internet.de/gg/art_2.html
https://www.gesetze-im-internet.de/gg/art_3.html
https://www.gesetze-im-internet.de/gg/art_4.html
https://www.gesetze-im-internet.de/gg/art_5.html
https://www.gesetze-im-internet.de/gg/art_6.html
https://www.gesetze-im-internet.de/gg/art_7.html
https://www.gesetze-im-internet.de/gg/art_8.html
https://www.gesetze-im-internet.de/gg/art_9.html
https://www.gesetze-im-internet.de/gg/art_10.html
https://www.gesetze-im-internet.de/gg/art_11.html
https://www.gesetze-im-internet.de/gg/art_12.html
https://www.gesetze-im-internet.de/gg/art_12a.html
https://www.gesetze-im-internet.de/gg/art_13.html
https://www.gesetze-im-internet.de/gg/art_14.html
https://www.gesetze-im-internet.de/gg/art_15.html
https://www.gesetze-im-internet.de/gg/art_16.html
https://www.gesetze-im-internet.de/gg/art_16a.html
https://www.gesetze-im-internet.de/gg/art_17.html
https://www.gesetze-im-internet.de/gg/art_17a.html
https://www.gesetze-im-internet.de/gg/art_18.html
https://www.gesetze-im-internet.de/gg/art_19.html
```

Ensuite, j'écris un peu de code Python dans un fichier appelé `scraper.py` pour télécharger le HTML de ces fichiers.

Dans un scénario réel, cela serait trop coûteux et vous utiliseriez une base de données à la place. Pour garder les choses simples, je vais télécharger les fichiers dans le même répertoire à côté du magasin et utiliser leur nom comme nom de fichier.

```py
from os import path
from pathlib import PurePath

import requests

with open('urls.txt', 'r') as fh:
    urls = fh.readlines()
urls = [url.strip() for url in urls]  # strip `\n`

for url in urls:
    file_name = PurePath(url).name
    file_path = path.join('.', file_name)
    text = ''

    try:
        response = requests.get(url)
        if response.ok:
            text = response.text
    except requests.exceptions.ConnectionError as exc:
        print(exc)
    
    with open(file_path, 'w') as fh:
        fh.write(text)

    print('Written to', file_path)
```

En téléchargeant les fichiers, je peux les traiter localement autant que je veux sans dépendre d'un serveur. Essayez d'être un bon citoyen du web, d'accord ?

## Étape 2 : Analyser la source

Maintenant que j'ai téléchargé les fichiers, il est temps d'en extraire les caractéristiques intéressantes. Pour cela, je vais sur l'une des pages que j'ai téléchargées, je l'ouvre dans un navigateur web et j'appuie sur Ctrl-U pour voir sa source. L'inspecter me montrera la structure HTML.

Dans mon cas, j'ai compris que je voulais le texte de la loi sans aucun balisage. L'élément qui l'entoure a un id de `container`. En utilisant BeautifulSoup, je peux voir qu'une combinaison de [`find`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find) et [`get_text`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#get-text) fera ce que je veux.

Puisque j'ai une deuxième étape maintenant, je vais refactoriser le code un peu en le mettant dans des fonctions et ajouter une CLI minimale.

```py
from os import path
from pathlib import PurePath
import sys

from bs4 import BeautifulSoup
import requests


def download_urls(urls, dir):
    paths = []

    for url in urls:
        file_name = PurePath(url).name
        file_path = path.join(dir, file_name)
        text = ''

        try:
            response = requests.get(url)
            if response.ok:
                text = response.text
            else:
                print('Bad response for', url, response.status_code)
        except requests.exceptions.ConnectionError as exc:
            print(exc)
    
        with open(file_path, 'w') as fh:
            fh.write(text)

        paths.append(file_path)

    return paths

def parse_html(path):
    with open(path, 'r') as fh:
        content = fh.read()

    return BeautifulSoup(content, 'html.parser')

def download(urls):
    return download_urls(urls, '.')

def extract(path):
    return parse_html(path)

def transform(soup):
    container = soup.find(id='container')
    if container is not None:
        return container.get_text()

def load(key, value):
    d = {}
    d[key] = value
    return d

def run_single(path):
    soup = extract(path)
    content = transform(soup)
    unserialised = load(path, content.strip() if content is not None else '')
    return unserialised

def run_everything():
    l = []

    with open('urls.txt', 'r') as fh:
        urls = fh.readlines()
    urls = [url.strip() for url in urls]

    paths = download(urls)
    for path in paths:
        print('Written to', path)
        l.append(run_single(path))

    print(l)

if __name__ == "__main__":
    args = sys.argv

    if len(args) is 1:
      run_everything()
    else:
        if args[1] == 'download':
            download([args[2]])
            print('Done')
        if args[1] == 'parse':
            path = args[2]
            result = run_single(path)
            print(result)
```

Maintenant, je peux exécuter le code de trois manières :

1. Sans aucun argument pour tout exécuter (c'est-à-dire télécharger toutes les URLs et les extraire, puis sauvegarder sur le disque) via : `python scraper.py`
2. Avec un argument `download` et une URL à télécharger `python scraper.py download https://www.gesetze-im-internet.de/gg/art_1.html`. Cela ne traitera pas le fichier.
3. Avec un argument `parse` et un chemin de fichier à analyser : `python scraper.py art_1.html`. Cela sautera l'étape de téléchargement.

Avec cela, il manque une dernière chose.

## Étape 3 : Formater la source pour un traitement ultérieur

Supposons que je veux générer un nuage de mots pour chaque article. Cela peut être un moyen rapide de se faire une idée de ce dont parle un texte. Pour cela, installez le package `wordcloud` et mettez à jour le fichier comme suit :

```py
from os import path
from pathlib import Path, PurePath
import sys

from bs4 import BeautifulSoup
import requests
from wordcloud import WordCloud

STOPWORDS_ADDENDUM = [
    'Das',
    'Der',
    'Die',
    'Diese',
    'Eine',
    'In',
    'InhaltsverzeichnisGrundgesetz',
    'im',
    'Jede',
    'Jeder',
    'Kein',
    'Sie',
    'Soweit',
    'Über'
]
STOPWORDS_FILE_PATH = 'stopwords.txt'
STOPWORDS_URL = 'https://raw.githubusercontent.com/stopwords-iso/stopwords-de/master/stopwords-de.txt'


def download_urls(urls, dir):
    paths = []

    for url in urls:
        file_name = PurePath(url).name
        file_path = path.join(dir, file_name)
        text = ''

        try:
            response = requests.get(url)
            if response.ok:
                text = response.text
            else:
                print('Bad response for', url, response.status_code)
        except requests.exceptions.ConnectionError as exc:
            print(exc)
    
        with open(file_path, 'w') as fh:
            fh.write(text)

        paths.append(file_path)

    return paths

def parse_html(path):
    with open(path, 'r') as fh:
        content = fh.read()

    return BeautifulSoup(content, 'html.parser')

def download_stopwords():
    stopwords = ''

    try:
        response = requests.get(STOPWORDS_URL)
        if response.ok:
            stopwords = response.text
        else:
            print('Bad response for', url, response.status_code)
    except requests.exceptions.ConnectionError as exc:
        print(exc)

    with open(STOPWORDS_FILE_PATH, 'w') as fh:
        fh.write(stopwords)

    return stopwords

def download(urls):
    return download_urls(urls, '.')

def extract(path):
    return parse_html(path)

def transform(soup):
    container = soup.find(id='container')
    if container is not None:
        return container.get_text()

def load(filename, text):
    if Path(STOPWORDS_FILE_PATH).exists():
        with open(STOPWORDS_FILE_PATH, 'r') as fh:
            stopwords = fh.readlines()
    else:
        stopwords = download_stopwords()

    # Strip whitespace around
    stopwords = [stopword.strip() for stopword in stopwords]
    # Extend stopwords with own ones, which were determined after first run
    stopwords = stopwords + STOPWORDS_ADDENDUM

    try:
        cloud = WordCloud(stopwords=stopwords).generate(text)
        cloud.to_file(filename.replace('.html', '.png'))
    except ValueError:
        print('Could not generate word cloud for', key)

def run_single(path):
    soup = extract(path)
    content = transform(soup)
    load(path, content.strip() if content is not None else '')

def run_everything():
    with open('urls.txt', 'r') as fh:
        urls = fh.readlines()
    urls = [url.strip() for url in urls]

    paths = download(urls)
    for path in paths:
        print('Written to', path)
        run_single(path)
    print('Done')

if __name__ == "__main__":
    args = sys.argv

    if len(args) is 1:
      run_everything()
    else:
        if args[1] == 'download':
            download([args[2]])
            print('Done')
        if args[1] == 'parse':
            path = args[2]
            run_single(path)
            print('Done')
```

Qu'est-ce qui a changé ? Pour commencer, j'ai téléchargé une [liste de mots vides allemands](https://github.com/stopwords-iso/stopwords-de/) depuis GitHub. De cette façon, je peux éliminer les mots les plus courants du texte de la loi téléchargée.

Ensuite, j'instancie une instance WordCloud avec la liste de mots vides que j'ai téléchargée et le texte de la loi. Il sera transformé en une image avec le même nom de base.

Après la première exécution, je découvre que la liste de mots vides est incomplète. J'ajoute donc des mots supplémentaires que je veux exclure de l'image résultante.

Avec cela, la partie principale du web scraping est complète.

## Bonus : Qu'en est-il des SPAs ?

Les SPAs - ou Single Page Applications - sont des applications web où toute l'expérience est contrôlée par JavaScript, qui est exécuté dans le navigateur. En tant que tel, le téléchargement du fichier HTML ne nous mène pas loin. Que devrions-nous faire à la place ?

Nous utiliserons le navigateur. Avec Selenium. Assurez-vous d'[installer un driver](https://selenium-python.readthedocs.io/installation.html#drivers) également. Téléchargez l'archive .tar.gz et décompressez-la dans le dossier `bin` de votre environnement virtuel afin qu'elle soit trouvée par Selenium. C'est le répertoire où vous pouvez trouver le script `activate` (sur les systèmes GNU/Linux).

En tant qu'exemple, j'utilise ici le [site web Angular](https://angular.io/). Angular est un Framework SPA populaire écrit en JavaScript et garanti d'être contrôlé par celui-ci pour le moment.

Puisque le code sera plus lent, je crée un nouveau fichier appelé `crawler.py` pour cela. Le contenu ressemble à ceci :

```py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from wordcloud import WordCloud

def extract(url):
    elem = None
    driver = webdriver.Firefox()
    driver.get(url)

    try:
        found = WebDriverWait(driver, 10).until(
            EC.visibility_of(
                driver.find_element(By.TAG_NAME, "article")
            )
        )
        # Make a copy of relevant data, because Selenium will throw if
        # you try to access the properties after the driver quit
        elem = {
          "text": found.text
        }
    finally:
        driver.close()

    return elem

def transform(elem):
    return elem["text"]
        
def load(text, filepath):
    cloud = WordCloud().generate(text)
    cloud.to_file(filepath)

if __name__ == "__main__":
    url = "https://angular.io/"
    filepath = "angular.png"

    elem = extract(url)
    if elem is not None:
        text = transform(elem)
        load(text, filepath)
    else:
        print("Sorry, could not extract data")
```

Ici, Python ouvre une instance de Firefox, navigue sur le site web et recherche un élément `<article>`. Il copie son texte dans un dictionnaire, qui est lu dans l'étape `transform` et transformé en un WordCloud pendant `load`.

Lors de la manipulation de sites riches en JavaScript, il est souvent utile d'utiliser des [Waits](https://selenium-python.readthedocs.io/waits.html) et peut-être d'exécuter même [`execute_script`](https://selenium-python.readthedocs.io/api.html#selenium.webdriver.remote.webdriver.WebDriver.execute_script) pour différer à JavaScript si nécessaire.

## Résumé

Merci d'avoir lu jusqu'ici ! Résumons ce que nous avons appris maintenant :

1. Comment scraper un site web avec le package `requests` de Python.
2. Comment le traduire en une structure significative en utilisant `beautifulsoup`.
3. Comment traiter davantage cette structure en quelque chose avec lequel vous pouvez travailler.
4. Que faire si la page cible repose sur JavaScript.

## Lectures complémentaires

Si vous voulez en savoir plus sur moi, vous pouvez [me suivre sur Twitter](https://twitter.com/AndreJaenisch) ou visiter [mon site web](https://jaenis.ch/).

Je ne suis pas le premier à avoir écrit sur le Web Scraping ici sur freeCodeCamp. Yasoob Khalid et Dave Gray l'ont également fait dans le passé :

%[https://www.freecodecamp.org/news/an-intro-to-web-scraping-with-lxml-and-python-b02b7a3f3098/]

%[https://www.freecodecamp.org/news/better-web-scraping-in-python-with-selenium-beautiful-soup-and-pandas-d6390592e251/]