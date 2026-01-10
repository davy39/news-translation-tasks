---
title: Web Scraping en Python – Comment scraper un site eCommerce en utilisant Beautiful
  Soup et Pandas
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-23T20:33:06.000Z'
originalURL: https://freecodecamp.org/news/scraping-ecommerce-website-with-python
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/Untitled-design--1-.png
tags:
- name: Python
  slug: python
- name: web scraping
  slug: web-scraping
seo_title: Web Scraping en Python – Comment scraper un site eCommerce en utilisant
  Beautiful Soup et Pandas
seo_desc: "By Manthan Koolwal\nIn this post we are going to scrape an ecommerce website.\
  \ We'll get into each individual product page and retrieve our information from\
  \ there. This is the website we are going to scrape – it's an online shop that sells\
  \ whisky. \nDo ..."
---

Par Manthan Koolwal

Dans cet article, nous allons scraper un site eCommerce. Nous allons accéder à chaque page de produit individuelle et récupérer nos informations à partir de là. Voici le [site](https://www.thewhiskyexchange.com/c/35/japanese-whisky) que nous allons scraper – il s'agit d'une boutique en ligne qui vend du whisky. 

N'oubliez pas de consulter le fichier `robots.txt` avant de scraper un site web. Vous devez garder à l'esprit que vous pouvez inutilement faire tomber un site web et nuire à leurs services. Alors, veuillez ne pas inonder leurs serveurs avec des requêtes de scraping. 

![Image](https://www.freecodecamp.org/news/content/images/2021/03/japwhis.PNG)

Je suis allé à une sous-section du site ici, et il semble qu'il y ait beaucoup de choix. Et si vous voulez savoir quelles sont les notes des utilisateurs pour chaque produit, alors vous devez ouvrir chaque page de produit pour obtenir les notes (vous ne pouvez pas les trouver sur la page principale).

![Image](https://www.freecodecamp.org/news/content/images/2021/03/jap2.PNG)

Nous allons donc obtenir une liste de tous les liens pour chaque produit des cinq pages. Ensuite, nous allons accéder à chaque produit individuellement et scraper nos données souhaitées. 

Mais certains d'entre eux n'ont pas de note. Dans ces cas, nous allons accéder à chaque produit et obtenir également le texte **à propos**. C'est parti !

# Comment configurer le projet de scraping

Notre configuration est assez simple. Créez simplement un dossier et installez Beautiful Soup, pandas et requests. Pour créer un dossier et installer les bibliothèques, entrez les commandes données ci-dessous. Je suppose que vous avez déjà installé Python 3.x.

```shell
mkdir scraper 
pip install beautifulsoup4 
pip install requests
pip install pandas
```

Maintenant, créez un fichier dans ce dossier et nommez-le comme vous le souhaitez. J'utilise le nom `scraper.py`. Nous allons importer requests, pandas et bs4.

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd
```

Maintenant, nous allons définir l'URL de base de la page principale car nous en aurons besoin lorsque nous construirons nos URLs pour chacun des produits individuels. 

De plus, nous allons envoyer un user-agent à chaque requête HTTP, car si vous faites une requête GET en utilisant **requests**, alors par défaut le user-agent est **Python**, ce qui pourrait être bloqué. 

Donc, pour remplacer cela, nous allons déclarer une variable qui stockera notre user-agent.

```python
baseurl = "https://www.thewhiskyexchange.com"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
```

Maintenant, nous devons investiguer la page afin de comprendre où se trouvent les liens et comment nous allons les obtenir. Vous devez ouvrir les outils de développement Chrome en utilisant l'inspection (Command+Option+C).

![Image](https://www.freecodecamp.org/news/content/images/2021/03/jap3.PNG)

Nous allons écrire un script pour parcourir chacun de ceux-ci et créer une URL pour nous. Pour cela, nous devons d'abord faire un appel HTTP. Ensuite, nous allons extraire l'élément **li** en utilisant BeautifulSoup.

```python
k = requests.get('https://www.thewhiskyexchange.com/c/35/japanese-whisky').text
soup=BeautifulSoup(k,'html.parser')
productlist = soup.find_all("li",{"class":"product-grid__item"})
print(productlist)
```

Juste pour vérifier que nous sommes sur la bonne voie, nous avons imprimé la liste complète.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/jap4.PNG)
_Sortie_

Ensuite, obtenez le HTML pour les éléments de cette page. Maintenant, à l'intérieur de chacune de ces listes, il y a un lien vers la page de produit individuelle. Nous allons écrire un script pour scraper tous ces liens de la **productlist**. 

```python
productlinks = []
for product in productlist:
        link = product.find("a",{"class":"product-card"}).get('href')                 productlinks.append(baseurl + link)
```

Ici, nous avons d'abord déclaré une liste vide appelée **productlinks.** Ensuite, nous avons utilisé une **boucle for** pour atteindre chaque élément **productlist** afin d'extraire le lien. Nous avons utilisé la fonction **.get()** pour obtenir la valeur de l'**attribut href**. Après avoir extrait le lien, nous stockons chaque lien à l'intérieur de la liste **productlinks.** Puisque nous devons créer une URL légitime, nous avons ajouté baseurl au lien. 

![Image](https://www.freecodecamp.org/news/content/images/2021/03/jap6.PNG)
_Sortie_

Comme nous l'avons discuté précédemment, nous devons couvrir les cinq pages du site web. Pour ce faire, nous allons introduire une boucle for avant de faire l'appel HTTP. Puisqu'il y a 5 pages, nous allons exécuter la boucle de 1 à 6. Assurez-vous également de changer l'URL cible.

```python
productlinks = []
for x in range(1,6):  
 k = requests.get('https://www.thewhiskyexchange.com/c/35/japanese-whisky?pg={}&psize=24&sort=pasc'.format(x)).text  
 soup=BeautifulSoup(k,'html.parser')  
 productlist = soup.find_all("li",{"class":"product-grid__item"})
 
    for product in productlist:
        link = product.find("a",{"class":"product-card"}).get('href')
        productlinks.append(baseurl + link)
```

Cela nous donnera tous les liens disponibles sur le site web. Maintenant, pour confirmer, vous pouvez imprimer la longueur de **productlinks**. Nous devrions obtenir 97 liens au total.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/jap7.PNG)
_Sortie_

Maintenant, nous pouvons parcourir chacun de ces liens pour extraire les informations sur les produits de chaque page et les stocker dans une autre liste ou un dictionnaire.

Ensuite, nous allons analyser le modèle dans lequel les informations sont affichées sur la page du produit. Nous allons extraire le nom, le prix, les notes et le texte à propos. 

![Image](https://www.freecodecamp.org/news/content/images/2021/03/jap8.PNG)

Le **Nom** est sous une balise **h1**, le texte **à propos** est sous la balise **div**, le **prix** est sous une balise **p**, et la **note** est sous la balise **span**. Maintenant, extrayons-les.

```python
data=[]
for link in productlinks:
    f = requests.get(link,headers=headers).text
    hun=BeautifulSoup(f,'html.parser')

    try:
        price=hun.find("p",{"class":"product-action__price"}).text.replace('\n',"")
    except:
        price = None

    try:
        about=hun.find("div",{"class":"product-main__description"}).text.replace('\n',"")
    except:
        about=None

    try:
        rating = hun.find("div",{"class":"review-overview"}).text.replace('\n',"")
    except:
        rating=None

    try:
        name=hun.find("h1",{"class":"product-main__name"}).text.replace('\n',"")
    except:
        name=None

    whisky = {"name":name,"price":price,"rating":rating,"about":about}

    data.append(whisky)
```

Ici, les choses sont assez simples. Nous avons démarré une boucle for pour itérer sur chaque lien individuel de **productlinks.** Nous allons faire un appel HTTP GET à chaque **lien** et extraire le **prix, le nom, la note** et le texte **à propos**. 

Nous utilisons **try** et **except** pour éviter toute erreur si un élément n'est pas trouvé. Utilisez la fonction **replace** pour supprimer toutes les sauts de ligne ou chaînes inutiles que nous obtenons avec les informations extraites. 

Nous avons créé un dictionnaire avec le nom **whisky** où nous allons stocker toutes les informations extraites. À la toute fin, nous stockons le dictionnaire à l'intérieur de la liste **data**. 

Maintenant, avant d'imprimer les données, nous allons rendre les données plus présentables. Ici, nous allons utiliser pandas. J'adore utiliser pandas ! 

```python
df = pd.DataFrame(data)

print(df)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/jap9.PNG)
_Sortie_

## Voici le code complet pour le scraper

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd

baseurl = "https://www.thewhiskyexchange.com"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
productlinks = []
t={}
data=[]
c=0
for x in range(1,6):
    k = requests.get('https://www.thewhiskyexchange.com/c/35/japanese-whisky?pg={}&psize=24&sort=pasc'.format(x)).text
    soup=BeautifulSoup(k,'html.parser')
    productlist = soup.find_all("li",{"class":"product-grid__item"})


    for product in productlist:
        link = product.find("a",{"class":"product-card"}).get('href')
        productlinks.append(baseurl + link)


for link in productlinks:
    f = requests.get(link,headers=headers).text
    hun=BeautifulSoup(f,'html.parser')

    try:
        price=hun.find("p",{"class":"product-action__price"}).text.replace('\n',"")
    except:
        price = None

    try:
        about=hun.find("div",{"class":"product-main__description"}).text.replace('\n',"")
    except:
        about=None

    try:
        rating = hun.find("div",{"class":"review-overview"}).text.replace('\n',"")
    except:
        rating=None

    try:
        name=hun.find("h1",{"class":"product-main__name"}).text.replace('\n',"")
    except:
        name=None

    whisky = {"name":name,"price":price,"rating":rating,"about":about}

    data.append(whisky)
    c=c+1
    print("completed",c)

df = pd.DataFrame(data)

print(df)

```

## Conclusion

Enfin, nous avons réussi à scraper toutes les informations de chaque page du site web. De la même manière, vous pouvez scraper d'autres textes de ce site web. En guise d'exercice, vous pouvez essayer de scraper ce [site](https://books.toscrape.com/). Si vous avez des questions pour moi, veuillez me contacter sur mon [compte twitter](https://twitter.com/scrapingdog).