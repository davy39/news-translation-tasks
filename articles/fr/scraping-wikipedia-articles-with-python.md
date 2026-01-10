---
title: Comment extraire des articles Wikipedia avec Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-24T17:24:24.000Z'
originalURL: https://freecodecamp.org/news/scraping-wikipedia-articles-with-python
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/artem-maltsev-vgQFlPq8tVQ-unsplash-1.jpg
tags:
- name: Python
  slug: python
- name: web scraping
  slug: web-scraping
seo_title: Comment extraire des articles Wikipedia avec Python
seo_desc: "By Dirk Hoekstra\nIn this article I'm going to create a web scraper in\
  \ Python that will scrape Wikipedia pages. \nThe scraper will go to a Wikipedia\
  \ page, scrape the title, and follow a random link to the next Wikipedia page.\n\
  I think it will be fun to ..."
---

Par Dirk Hoekstra

Dans cet article, je vais créer un scraper web en Python qui extraira des pages Wikipedia. 

Le scraper ira sur une page Wikipedia, extraira le titre et suivra un lien aléatoire vers la page Wikipedia suivante.

Je pense que ce sera amusant de voir quelles pages Wikipedia aléatoires ce scraper visitera !

## Installation du scraper

Pour commencer, je vais créer un nouveau fichier Python appelé `scraper.py` :

```
touch scraper.py
```

Pour effectuer la requête HTTP, je vais utiliser la bibliothèque `requests`. Vous pouvez l'installer avec la commande suivante :

```
pip install requests
```

Utilisons la page wiki sur le web scraping comme point de départ :

```python
import requests

response = requests.get(
	url="https://en.wikipedia.org/wiki/Web_scraping",
)
print(response.status_code)

```

Lors de l'exécution du scraper, il devrait afficher un code de statut 200 :

```
python3 scraper.py
200
```

Très bien, jusqu'à présent tout va bien ! 💡

## Extraction des données de la page

Extrayons le titre de la page HTML. Pour me faciliter la vie, je vais utiliser le package BeautifulSoup.

```
pip install beautifulsoup4
```

En inspectant la page Wikipedia, je vois que la balise de titre a l'ID `#firstHeading`.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screen-Shot-2020-08-23-at-4.10.44-PM.png)

BeautifulSoup permet de trouver un élément par son ID.

```python
title = soup.find(id="firstHeading")
```

En mettant tout ensemble, le programme ressemble maintenant à ceci :

```python
import requests
from bs4 import BeautifulSoup

response = requests.get(
	url="https://en.wikipedia.org/wiki/Web_scraping",
)
soup = BeautifulSoup(response.content, 'html.parser')

title = soup.find(id="firstHeading")
print(title.string)

```

Et lors de l'exécution, il affiche le titre de l'article Wiki : 💡

```
python3 scraper.py
Web scraping
```

## Extraction d'autres liens

Maintenant, je vais plonger profondément dans Wikipedia. Je vais récupérer un tag `<a>` aléatoire vers un autre article Wikipedia et extraire cette page.

Pour cela, j'utiliserai BeautifulSoup pour trouver tous les tags `<a>` dans l'article wiki. Ensuite, je mélange la liste pour la rendre aléatoire.

```python
import requests
from bs4 import BeautifulSoup
import random

response = requests.get(
	url="https://en.wikipedia.org/wiki/Web_scraping",
)
soup = BeautifulSoup(response.content, 'html.parser')

title = soup.find(id="firstHeading")
print(title.content)

# Obtenir tous les liens
allLinks = soup.find(id="bodyContent").find_all("a")
random.shuffle(allLinks)
linkToScrape = 0

for link in allLinks:
	# Nous ne sommes intéressés que par d'autres articles wiki
	if link['href'].find("/wiki/") == -1: 
		continue

	# Utiliser ce lien pour extraire
	linkToScrape = link
	break

print(linkToScrape)
```

Comme vous pouvez le voir, j'utilise `soup.find(id="bodyContent").find_all("a")` pour trouver tous les tags `<a>` dans l'article principal.

Puisque je ne suis intéressé que par les liens vers d'autres articles Wikipedia, je m'assure que le lien contient le préfixe `/wiki`.

Lors de l'exécution du programme, il affiche maintenant un lien vers un autre article Wikipedia, bien !

```
python3 scraper.py
<a href="/wiki/Link_farm" title="Link farm">Link farm</a>
```

## Création d'un scraper sans fin

D'accord, faisons en sorte que le scraper extraie réellement le nouveau lien.

Pour cela, je vais déplacer tout dans une fonction `scrapeWikiArticle`.

```python
import requests
from bs4 import BeautifulSoup
import random

def scrapeWikiArticle(url):
	response = requests.get(
		url=url,
	)
	
	soup = BeautifulSoup(response.content, 'html.parser')

	title = soup.find(id="firstHeading")
	print(title.text)

	allLinks = soup.find(id="bodyContent").find_all("a")
	random.shuffle(allLinks)
	linkToScrape = 0

	for link in allLinks:
		# Nous ne sommes intéressés que par d'autres articles wiki
		if link['href'].find("/wiki/") == -1: 
			continue

		# Utiliser ce lien pour extraire
		linkToScrape = link
		break

	scrapeWikiArticle("https://en.wikipedia.org" + linkToScrape['href'])

scrapeWikiArticle("https://en.wikipedia.org/wiki/Web_scraping")
```

La fonction `scrapeWikiArticle` récupérera l'article wiki, extraira le titre et trouvera un lien aléatoire.

Ensuite, elle appellera à nouveau `scrapeWikiArticle` avec ce nouveau lien. Ainsi, elle crée un cycle sans fin d'un scraper qui rebondit sur Wikipedia.

Exécutons le programme et voyons ce que nous obtenons :

```
python3 scraper.py
Web scraping
Digital object identifier
ISO 8178
STEP-NC
ISO/IEC 2022
EBCDIC 277
Code page 867
Code page 1021
EBCDIC 423
Code page 950
G
R
Mole (unit)
Gram
Remmius Palaemon
Encyclopædia Britannica Eleventh Edition
Geography
Gender studies
Feminism in Brazil
```

Super, en environ 10 étapes, nous sommes passés de "Web Scraping" à "Feminism in Brazil". Incroyable !

## Conclusion

Nous avons construit un scraper web en Python qui extrait des pages Wikipedia aléatoires. Il rebondit sans fin sur Wikipedia en suivant des liens aléatoires.

C'est un gadget amusant et Wikipedia est assez indulgent en matière de web scraping.

Il existe également des sites web plus difficiles à extraire, comme Amazon ou Google. Si vous souhaitez extraire un tel site, vous devriez mettre en place un système avec des navigateurs Chrome headless et des serveurs proxy. Ou vous pouvez utiliser un service qui gère tout cela pour vous [comme celui-ci](https://scraperbox.com).

Mais faites attention à ne pas abuser des sites web et à n'extraire que les données que vous êtes autorisé à extraire.

Bon codage !