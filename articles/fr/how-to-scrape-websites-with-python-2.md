---
title: Tutoriel de Web Scraping en Python – Comment extraire des données de n'importe
  quel site web avec Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-08-10T17:42:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-scrape-websites-with-python-2
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/how-to-scrape-data-from-any-website-with-python.jpg
tags:
- name: Python
  slug: python
- name: web scraping
  slug: web-scraping
seo_title: Tutoriel de Web Scraping en Python – Comment extraire des données de n'importe
  quel site web avec Python
seo_desc: 'By Sorin-Gabriel Marica

  Web scraping is the process of extracting specific data from the internet automatically.
  It has many use cases, like getting data for a machine learning project, creating
  a price comparison tool, or any other innovative idea t...'
---

Par Sorin-Gabriel Marica

Le web scraping est le processus d'extraction automatique de données spécifiques depuis Internet. Il a de nombreuses utilisations, comme obtenir des données pour un projet de machine learning, créer un outil de comparaison de prix, ou toute autre idée innovante nécessitant une immense quantité de données.

Bien que vous puissiez théoriquement faire de l'extraction de données manuellement, l'immensité du contenu sur Internet rend cette approche irréaliste dans de nombreux cas. Savoir comment construire un web scraper peut donc être utile. 

L'objectif de cet article est de vous apprendre à créer un web scraper en Python. Vous apprendrez à inspecter un site web pour préparer le scraping, extraire des données spécifiques en utilisant BeautifulSoup, attendre le rendu JavaScript avec Selenium, et sauvegarder le tout dans un nouveau fichier JSON ou CSV.

Mais d'abord, je dois vous avertir sur la légalité du web scraping. Bien que l'acte de scraping soit légal, les données que vous pourriez extraire peuvent être illégales à utiliser. Assurez-vous de ne pas toucher à :

* Contenu protégé par copyright – puisque c'est la propriété intellectuelle de quelqu'un, il est protégé par la loi et vous ne pouvez pas simplement le réutiliser.
* Données personnelles – si les informations que vous collectez peuvent être utilisées pour identifier une personne, alors elles sont considérées comme des données personnelles et pour les citoyens de l'UE, elles sont protégées par le RGPD. À moins d'avoir une raison légale de stocker ces données, il est préférable de les ignorer complètement.

En général, vous devriez toujours lire les conditions générales d'un site web avant de faire du scraping pour vous assurer de ne pas aller à l'encontre de leurs politiques. Si vous n'êtes jamais sûr de la manière de procéder, contactez le propriétaire du site et demandez son consentement. 

## De quoi aurez-vous besoin pour votre Scraper ?

Pour commencer à construire votre propre web scraper, vous devrez d'abord avoir [Python](https://www.python.org/downloads/) installé sur votre machine. Ubuntu 20.04 et d'autres versions de Linux sont livrés avec Python 3 préinstallé. 

Pour vérifier si vous avez déjà Python installé sur votre appareil, exécutez la commande suivante :

```
python3 -v

```

Si vous avez Python installé, vous devriez recevoir une sortie comme celle-ci :

```
Python 3.8.2
```

De plus, pour notre web scraper, nous utiliserons les packages Python BeautifulSoup (pour sélectionner des données spécifiques) et Selenium (pour rendre le contenu chargé dynamiquement). Pour les installer, exécutez simplement ces commandes :

```
pip3 install beautifulsoup4
```

et

```
pip3 install selenium
```

La dernière étape consiste à vous assurer d'installer [Google Chrome](https://support.google.com/chrome/answer/95346?co=GENIE.Platform%3DDesktop&hl=en) et [Chrome Driver](https://chromedriver.chromium.org/downloads) sur votre machine. Ceux-ci seront nécessaires si nous voulons utiliser Selenium pour scraper du contenu chargé dynamiquement.

## Comment inspecter la page

Maintenant que vous avez tout installé, il est temps de commencer notre projet de scraping en earnest. 

Vous devriez choisir le site web que vous souhaitez scraper en fonction de vos besoins. Gardez à l'esprit que chaque site web structure son contenu différemment, vous devrez donc ajuster ce que vous apprenez ici lorsque vous commencerez à scraper par vous-même. Chaque site web nécessitera des modifications mineures du code.

Pour cet article, j'ai décidé de scraper des informations sur les dix premiers films de la liste des 250 meilleurs films d'IMDb : [https://www.imdb.com/chart/top/](https://www.imdb.com/chart/top/). 

Tout d'abord, nous obtiendrons les titres, puis nous irons plus loin en extrayant des informations de chaque page de film. Certaines des données nécessiteront un rendu JavaScript.

Pour commencer à comprendre la structure du contenu, vous devriez faire un clic droit sur le premier titre de la liste, puis choisir « Inspecter l'élément ».

![Image](https://lh4.googleusercontent.com/e6DE3zczzQa-VSBIynK-fR4oyAjVbpx2PztpEDKbi3K0NII9_lFkFhGQmiOjc_-Y_Kg26cM3pecnSKNiPlLZGpntqVKUrcX9E4gDWaTsolWoCFzQ6EEhj3GruBvrlEIzrUffvdjU)

En appuyant sur CTRL+F et en recherchant dans la structure du code HTML, vous verrez qu'il n'y a qu'une seule balise **<table>** sur la page. Cela est utile car cela nous donne des informations sur la manière dont nous pouvons accéder aux données.

Un sélecteur HTML qui nous donnera tous les titres de la page est **`table tbody tr td.titleColumn a`**. C'est parce que tous les titres sont dans une ancre à l'intérieur d'une cellule de tableau avec la classe « titleColumn ». 

L'utilisation de ce sélecteur CSS et l'obtention du **innerText** de chaque ancre nous donnera les titres dont nous avons besoin. Vous pouvez simuler cela dans la console du navigateur à partir de la nouvelle fenêtre que vous venez d'ouvrir et en utilisant la ligne JavaScript :

```
document.querySelectorAll("table tbody tr td.titleColumn a")[0].innerText
```

Vous verrez quelque chose comme ceci :

![Image](https://lh4.googleusercontent.com/T1pgLUXJHX_s3gubDKvBjwkWeK1neZxiysoneD2Q1NU3Sj_pD8defdKorTlcsiiqShlmPDEeCu3Goo5T9CgzPKCml9dq_kCCu7KUyTx7uSrU8VN9QzJZhO6AwBM-kfQ8r0uNxbn9)

Maintenant que nous avons ce sélecteur, nous pouvons commencer à écrire notre code Python et extraire les informations dont nous avons besoin.

## Comment utiliser BeautifulSoup pour extraire du contenu chargé statiquement 

Les titres des films de notre liste sont du contenu statique. C'est parce que si vous regardez dans le code source de la page (CTRL+U sur la page ou clic droit puis choisir Afficher le code source de la page), vous verrez que les titres sont déjà là.

Le contenu statique est généralement plus facile à scraper car il ne nécessite pas de rendu JavaScript. Pour extraire les dix premiers titres de la liste, nous utiliserons BeautifulSoup pour obtenir le contenu, puis l'afficher dans la sortie de notre scraper.

```python
import requests
from bs4 import BeautifulSoup
 
page = requests.get('https://www.imdb.com/chart/top/') # Obtention du HTML de la page via une requête
soup = BeautifulSoup(page.content, 'html.parser') # Analyse du contenu en utilisant beautifulsoup
 
links = soup.select("table tbody tr td.titleColumn a") # Sélection de toutes les ancres avec les titres
first10 = links[:10] # Garder seulement les 10 premières ancres
for anchor in first10:
    print(anchor.text) # Afficher le innerText de chaque ancre

```

Le code ci-dessus utilise le sélecteur que nous avons vu dans la première étape pour extraire les ancres des titres de films de la page. Il parcourt ensuite les dix premiers et affiche le innerText de chacun.

La sortie devrait ressembler à ceci :

![Image](https://lh3.googleusercontent.com/RrmEldjCrbz7V1-o4r6UsKNuWkj_yD2cWwfyuMMbdnRn7lk9cI0yhMi85PK4NrvX7L2KY0pY8047f9CmAeXo1W51HvFENMPxxh36ACqu3kNKuoFNNfhB_WSCMntIB-UB0usEU2n5)

## Comment extraire du contenu chargé dynamiquement

Avec l'avancement de la technologie, les sites web ont commencé à charger leur contenu dynamiquement. Cela améliore les performances de la page, l'expérience de l'utilisateur, et supprime même une barrière supplémentaire pour les scrapers.

Cela complique les choses, cependant, car le HTML récupéré à partir d'une simple requête ne contiendra pas le contenu dynamique. Heureusement, avec Selenium, nous pouvons simuler une requête dans le navigateur et attendre que le contenu dynamique soit affiché.

### Comment utiliser Selenium pour les requêtes

Vous devrez connaître l'emplacement de votre chromedriver. Le code suivant est identique à celui présenté dans la deuxième étape, mais cette fois nous utilisons Selenium pour faire la requête. Nous analyserons toujours le contenu de la page en utilisant BeautifulSoup, comme nous l'avons fait auparavant.

```python
from bs4 import BeautifulSoup
from selenium import webdriver
 
option = webdriver.ChromeOptions()
# J'utilise les options suivantes car ma machine est un sous-système windows linux. 
# Je recommande d'utiliser au moins l'option headless, parmi les 3
option.add_argument('--headless')
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-sh-usage')
# Remplacez YOUR-PATH-TO-CHROMEDRIVER par l'emplacement de votre chromedriver
driver = webdriver.Chrome('YOUR-PATH-TO-CHROMEDRIVER', options=option)
 
driver.get('https://www.imdb.com/chart/top/') # Obtention du HTML de la page via une requête
soup = BeautifulSoup(driver.page_source, 'html.parser') # Analyse du contenu en utilisant beautifulsoup. Remarquez driver.page_source au lieu de page.content
 
links = soup.select("table tbody tr td.titleColumn a") # Sélection de toutes les ancres avec les titres
first10 = links[:10] # Garder seulement les 10 premières ancres
for anchor in first10:
    print(anchor.text) # Afficher le innerText de chaque ancre

```

N'oubliez pas de remplacer « YOUR-PATH-TO-CHROMEDRIVER » par l'emplacement où vous avez extrait le chromedriver. De plus, vous devriez remarquer qu'au lieu de **`page.content`**, lorsque nous créons l'objet BeautifulSoup, nous utilisons maintenant **`driver.page_source`**, qui fournit le contenu HTML de la page.

### Comment extraire du contenu chargé statiquement en utilisant Selenium

En utilisant le code ci-dessus, nous pouvons maintenant accéder à chaque page de film en appelant la méthode click sur chacune des ancres.

```python
first_link = driver.find_elements_by_css_selector('table tbody tr td.titleColumn a')[0]
first_link.click()

```

Cela simulera un clic sur le lien du premier film. Cependant, dans ce cas, je recommande de continuer à utiliser **`driver.get`**. Cela est dû au fait que vous ne pourrez plus utiliser la méthode **`click()`** après être allé sur une page différente puisque la nouvelle page n'a pas de liens vers les neuf autres films.

Par conséquent, après avoir cliqué sur le premier titre de la liste, vous devriez revenir à la première page, puis cliquer sur le deuxième, et ainsi de suite. Cela est une perte de performance et de temps. Au lieu de cela, nous utiliserons simplement les liens extraits et y accéderons un par un.

Pour « The Shawshank Redemption », la page du film sera [https://www.imdb.com/title/tt0111161/](https://www.imdb.com/title/tt0111161/). Nous extrairons l'année et la durée du film de la page, mais cette fois nous utiliserons les fonctions de Selenium au lieu de BeautifulSoup comme exemple. En pratique, vous pouvez utiliser l'un ou l'autre, alors choisissez votre préféré.

Pour récupérer l'année et la durée du film, vous devriez répéter la première étape que nous avons suivie ici sur la page du film. 

Vous remarquerez que vous pouvez trouver toutes les informations dans le premier élément avec la classe **`ipc-inline-list`** (sélecteur ".ipc-inline-list") et que tous les éléments de la liste contiennent l'attribut **`role`** avec la valeur **`presentation`** (le sélecteur `[role='presentation']`).

```python
from bs4 import BeautifulSoup
from selenium import webdriver
 
option = webdriver.ChromeOptions()
# J'utilise les options suivantes car ma machine est un sous-système windows linux. 
# Je recommande d'utiliser au moins l'option headless, parmi les 3
option.add_argument('--headless')
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-sh-usage')
# Remplacez YOUR-PATH-TO-CHROMEDRIVER par l'emplacement de votre chromedriver
driver = webdriver.Chrome('YOUR-PATH-TO-CHROMEDRIVER', options=option)
 
page = driver.get('https://www.imdb.com/chart/top/') # Obtention du HTML de la page via une requête
soup = BeautifulSoup(driver.page_source, 'html.parser') # Analyse du contenu en utilisant beautifulsoup
 
totalScrapedInfo = [] # Dans cette liste nous sauvegarderons toutes les informations que nous scrapons
links = soup.select("table tbody tr td.titleColumn a") # Sélection de toutes les ancres avec les titres
first10 = links[:10] # Garder seulement les 10 premières ancres
for anchor in first10:
    driver.get('https://www.imdb.com/' + anchor['href']) # Accéder à la page du film
    infolist = driver.find_elements_by_css_selector('.ipc-inline-list')[0] # Trouver le premier élément avec la classe 'ipc-inline-list'
    informations = infolist.find_elements_by_css_selector("[role='presentation']") # Trouver tous les éléments avec role='presentation' du premier élément avec la classe 'ipc-inline-list'
    scrapedInfo = {
        "title": anchor.text,
        "year": informations[0].text,
        "duration": informations[2].text,
    } # Sauvegarder toutes les informations scrapées dans un dictionnaire
    totalScrapedInfo.append(scrapedInfo) # Ajouter le dictionnaire à la liste totalScrapedInformation
    
print(totalScrapedInfo) # Afficher la liste avec toutes les informations que nous avons scrapées

```

### Comment extraire du contenu chargé dynamiquement en utilisant Selenium

La prochaine grande étape dans le web scraping est l'extraction de contenu qui est chargé dynamiquement. Vous pouvez trouver un tel contenu sur chacune des pages de films (comme [https://www.imdb.com/title/tt0111161/](https://www.imdb.com/title/tt0111161/)) dans la section Editorial Lists. 

Si vous regardez en utilisant l'inspecteur sur la page, vous verrez que vous pouvez trouver la section en tant qu'élément avec l'attribut **`data-testid`** défini comme **`firstListCardGroup-editorial`**. Mais si vous regardez dans le code source de la page, vous ne trouverez pas cette valeur d'attribut nulle part. C'est parce que la section Editorial Lists est chargée dynamiquement par IMDB.

Dans l'exemple suivant, nous allons scraper la liste éditoriale de chaque film et l'ajouter à nos résultats actuels des informations totales scrapées. 

Pour ce faire, nous allons importer quelques packages supplémentaires qui permettent d'attendre que notre contenu dynamique se charge.

```python
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
option = webdriver.ChromeOptions()
# J'utilise les options suivantes car ma machine est un sous-système windows linux. 
# Je recommande d'utiliser au moins l'option headless, parmi les 3
option.add_argument('--headless')
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-sh-usage')
# Remplacez YOUR-PATH-TO-CHROMEDRIVER par l'emplacement de votre chromedriver
driver = webdriver.Chrome('YOUR-PATH-TO-CHROMEDRIVER', options=option)
 
page = driver.get('https://www.imdb.com/chart/top/') # Obtention du HTML de la page via une requête
soup = BeautifulSoup(driver.page_source, 'html.parser') # Analyse du contenu en utilisant beautifulsoup
 
totalScrapedInfo = [] # Dans cette liste nous sauvegarderons toutes les informations que nous scrapons
links = soup.select("table tbody tr td.titleColumn a") # Sélection de toutes les ancres avec les titres
first10 = links[:10] # Garder seulement les 10 premières ancres
for anchor in first10:
    driver.get('https://www.imdb.com/' + anchor['href']) # Accéder à la page du film 
    infolist = driver.find_elements_by_css_selector('.ipc-inline-list')[0] # Trouver le premier élément avec la classe 'ipc-inline-list'
    informations = infolist.find_elements_by_css_selector("[role='presentation']") # Trouver tous les éléments avec role='presentation' du premier élément avec la classe 'ipc-inline-list'
    scrapedInfo = {
        "title": anchor.text,
        "year": informations[0].text,
        "duration": informations[2].text,
    } # Sauvegarder toutes les informations scrapées dans un dictionnaire
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='firstListCardGroup-editorial']")))  # Nous attendons 5 secondes pour notre élément avec l'attribut data-testid défini comme `firstListCardGroup-editorial`
    listElements = driver.find_elements_by_css_selector("[data-testid='firstListCardGroup-editorial'] .listName") # Extraction des éléments des listes éditoriales
    listNames = [] # Création d'une liste vide puis ajout des textes des éléments uniquement
    for el in listElements:
        listNames.append(el.text)
    scrapedInfo['editorial-list'] = listNames # Ajout des noms des listes éditoriales à notre dictionnaire scrapedInfo
    totalScrapedInfo.append(scrapedInfo) # Ajouter le dictionnaire à la liste totalScrapedInformation
    
print(totalScrapedInfo) # Afficher la liste avec toutes les informations que nous avons scrapées

```

Pour l'exemple précédent, vous devriez obtenir la sortie suivante :

![Image](https://lh4.googleusercontent.com/geHhbKeeP2ATtz-OnIx9MATB3UvXcrobnO4eUNOLrzQll9ebPlq_2PqKaT_oT6e-3h7NmRkRh_9mrDuSvuW3Wbs3sRi1iuM3paCa8HBpTqWrZuSQc8sIu5y4EVZ_5j-60TmPs71Z)

## Comment sauvegarder le contenu scrapé

Maintenant que nous avons toutes les données que nous voulons, nous pouvons les sauvegarder sous forme de fichier .json ou .csv pour une meilleure lisibilité. 

Pour ce faire, nous utiliserons simplement les packages JSON et CSV de Python et écrirons notre contenu dans de nouveaux fichiers :

```python
import csv
import json
 
...
        
file = open('movies.json', mode='w', encoding='utf-8')
file.write(json.dumps(totalScrapedInfo))
 
writer = csv.writer(open("movies.csv", 'w'))
for movie in totalScrapedInfo:
    writer.writerow(movie.values())

```

## Conseils et astuces pour le scraping

Bien que notre guide jusqu'à présent soit déjà suffisamment avancé pour gérer les scénarios de rendu JavaScript, il reste encore beaucoup de choses à explorer dans Selenium. 

Dans cette section, je vais partager quelques conseils et astuces qui peuvent être utiles.

### 1. Chronométrez vos requêtes

Si vous spammez un serveur avec des centaines de requêtes en peu de temps, il est très probable qu'à un moment donné, un code captcha apparaisse, ou que votre IP soit même bloquée. Malheureusement, il n'y a pas de solution en Python pour éviter cela. 

Par conséquent, vous devriez mettre des pauses de timeout entre chaque requête afin que le trafic semble plus naturel.

```python
import time
import requests
 
page = requests.get('https://www.imdb.com/chart/top/') # Obtention du HTML de la page via une requête
time.sleep(30) # Attendre 30 secondes
page = requests.get('https://www.imdb.com/') # Obtention du HTML de la page via une requête

```

### 2. Gestion des erreurs

Puisque les sites web sont dynamiques et peuvent changer de structure à tout moment, la gestion des erreurs peut être utile si vous utilisez le même web scraper fréquemment.

```python
try:
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "your selector")))
    break
except TimeoutException:
    # Si le chargement a pris trop de temps, afficher un message et réessayer
    print("Le chargement a pris trop de temps !")
```

La syntaxe try et error peut être utile lorsque vous attendez un élément, l'extrayez, ou même lorsque vous faites simplement la requête.

### 3. Prendre des captures d'écran

Si vous avez besoin d'obtenir une capture d'écran de la page web que vous scrapez à tout moment, vous pouvez utiliser :

```python
driver.save_screenshot('nom-du-fichier-de-capture.png')
```

Cela peut aider à déboguer lorsque vous travaillez avec du contenu chargé dynamiquement.

### 4. Lire la documentation

Enfin, mais non des moindres, n'oubliez pas de lire la [documentation de Selenium](https://selenium-python.readthedocs.io/). Cette bibliothèque contient des informations sur la manière de faire la plupart des actions que vous pouvez faire dans un navigateur. 

Avec Selenium, vous pouvez remplir des formulaires, appuyer sur des boutons, répondre à des messages pop-up, et faire beaucoup d'autres choses cool. 

Si vous êtes confronté à un nouveau problème, leur documentation peut être votre meilleure amie.

## Réflexions finales

L'objectif de cet article est de vous donner une introduction avancée au web scraping en utilisant Python avec Selenium et BeautifulSoup. Bien qu'il reste encore de nombreuses fonctionnalités des deux technologies à explorer, vous avez maintenant une base solide pour commencer à scraper.

Parfois, le web scraping peut être très difficile, car les sites web commencent à mettre de plus en plus d'obstacles sur le chemin des développeurs. Certains de ces obstacles peuvent être des codes Captcha, des blocs IP, ou du contenu dynamique. Les surmonter uniquement avec Python et Selenium peut être difficile ou même impossible. 

Je vais donc vous donner une alternative. Essayez d'utiliser une [API de web scraping](https://webscrapingapi.com) qui résout tous ces défis pour vous. Elle utilise également des proxies rotatifs afin que vous n'ayez pas à vous soucier d'ajouter des timeouts entre les requêtes. N'oubliez simplement pas de toujours vérifier si les données que vous voulez peuvent être extraites et utilisées légalement.