---
title: Meilleur web scraping en Python avec Selenium, Beautiful Soup et pandas
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-16T16:03:07.000Z'
originalURL: https://freecodecamp.org/news/better-web-scraping-in-python-with-selenium-beautiful-soup-and-pandas-d6390592e251
coverImage: https://cdn-media-1.freecodecamp.org/images/1*DiffPQdgEAjDK4M_unUd4Q.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
seo_title: Meilleur web scraping en Python avec Selenium, Beautiful Soup et pandas
seo_desc: 'By Dave Gray

  Web Scraping

  Using the Python programming language, it is possible to “scrape” data from the
  web in a quick and efficient manner.

  Web scraping is defined as:


  a tool for turning the unstructured data on the web into machine readable, str...'
---

Par Dave Gray

### Web Scraping

En utilisant le langage de programmation Python, il est possible de "scraper" des données sur le web de manière rapide et efficace.

Le web scraping est défini comme :

> un outil pour transformer les données non structurées sur le web en données structurées et lisibles par machine, prêtes pour l'analyse. ([source](https://www.promptcloud.com/blog/should-data-scientists-learn-web-scraping))

Le web scraping est un outil précieux dans [l'ensemble des compétences du data scientist](https://medium.com/@Francesco_AI/data-science-skills-list-9f38863adab5).

_Maintenant, que scraper ?_

![Image](https://cdn-media-1.freecodecamp.org/images/1*PFcYTwR35sTl2we1WhUuFg.jpeg)
_"Options de recherche approfondie" == Continuez à cliquer jusqu'à trouver ce que vous voulez._

### Données publiquement disponibles

Le site [KanView](http://kanview.ks.gov/PayRates/PayRates_Agency.aspx) soutient la "Transparence dans le Gouvernement". C'est aussi le slogan du site. Le site fournit des données de paie pour l'État du Kansas. Et c'est génial !

Cependant, comme de nombreux sites gouvernementaux, il enterre les données dans des liens et des tableaux à plusieurs niveaux. Cela nécessite souvent une "navigation par supposition" pour trouver les données spécifiques que vous recherchez. Je voulais utiliser les données publiques fournies pour les universités du Kansas dans un projet de recherche. Scraper les données avec Python et les sauvegarder en JSON était ce que je devais faire pour commencer.

### Les liens JavaScript augmentent la complexité

Le web scraping avec Python nécessite souvent rien de plus que l'utilisation du module [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) pour atteindre l'objectif. [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) est une bibliothèque Python populaire qui facilite le web scraping en parcourant le DOM (modèle d'objet de document).

Cependant, le site [KanView](http://kanview.ks.gov/PayRates/PayRates_Agency.aspx) utilise des liens JavaScript. Par conséquent, les exemples utilisant Python et Beautiful Soup ne fonctionneront pas sans quelques ajouts supplémentaires.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Xw5kfdCZT3ndmQiK6gFpDA.jpeg)
_[https://pypi.python.org/pypi/selenium](https://pypi.python.org/pypi/selenium" rel="noopener" target="_blank" title=")_

### Selenium à la rescousse

Le [package Selenium](https://pypi.org/project/selenium/) est utilisé pour automatiser l'interaction avec le navigateur web depuis Python. Avec Selenium, il est possible de programmer un script Python pour automatiser un navigateur web. Ensuite, ces liens JavaScript ennuyeux ne posent plus de problème.

```py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
import os
```

Selenium va maintenant démarrer une session de navigateur. Pour que Selenium fonctionne, il doit accéder au pilote du navigateur. Par défaut, il cherchera dans le même répertoire que le script Python. Les liens vers les pilotes Chrome, Firefox, Edge et Safari sont [disponibles ici](https://pypi.python.org/pypi/selenium). Le code exemple ci-dessous utilise Firefox :

```py
# lancer l'URL
url = "http://kanview.ks.gov/PayRates/PayRates_Agency.aspx"

# créer une nouvelle session Firefox
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.get(url)

python_button = driver.find_element_by_id('MainContent_uxLevel1_Agencies_uxAgencyBtn_33') #FHSU
python_button.click() # cliquer sur le lien fhsu
```

Le `python_button.click()` ci-dessus indique à Selenium de cliquer sur le lien JavaScript de la page. Après être arrivé sur la page des titres de poste, Selenium transmet la source de la page à Beautiful Soup.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_jcqKfi3H0vETIPeGhiAfg.jpeg)
_[https://www.crummy.com/software/BeautifulSoup/](https://www.crummy.com/software/BeautifulSoup/" rel="noopener" target="_blank" title=")_

### Transition vers Beautiful Soup

[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) reste le meilleur moyen de parcourir le DOM et de scraper les données. Après avoir défini une liste vide et une variable de compteur, il est temps de demander à Beautiful Soup de récupérer tous les liens de la page qui correspondent à une expression régulière :

```py
# Selenium transmet la source de la page à Beautiful Soup
soup_level1=BeautifulSoup(driver.page_source, 'lxml')

datalist = [] # liste vide
x = 0 # compteur

for link in soup_level1.find_all('a', id=re.compile("^MainContent_uxLevel2_JobTitles_uxJobTitleBtn_")):
    ## code à exécuter dans la boucle for
```

Vous pouvez voir dans l'exemple ci-dessus que Beautiful Soup récupérera un lien JavaScript pour chaque titre de poste de l'agence d'État. Maintenant, dans le bloc de code de la boucle for / in, Selenium cliquera sur chaque lien JavaScript. Beautiful Soup récupérera ensuite le tableau de chaque page.

```py
# Beautiful Soup récupère tous les liens des titres de poste
for link in soup_level1.find_all('a', id=re.compile("^MainContent_uxLevel2_JobTitles_uxJobTitleBtn_")):
    
    # Selenium visite chaque page de titre de poste
    python_button = driver.find_element_by_id('MainContent_uxLevel2_JobTitles_uxJobTitleBtn_' + str(x))
    python_button.click() # cliquer sur le lien
    
    # Selenium transmet la source de la page de poste spécifique à Beautiful Soup
    soup_level2=BeautifulSoup(driver.page_source, 'lxml')

    # Beautiful Soup récupère le tableau HTML sur la page
    table = soup_level2.find_all('table')[0]
    
    # Donner le tableau HTML à pandas pour le mettre dans un objet dataframe
    df = pd.read_html(str(table),header=0)
    
    # Stocker le dataframe dans une liste
    datalist.append(df[0])
    
    # Demander à Selenium de cliquer sur le bouton retour
    driver.execute_script("window.history.go(-1)") 
    
    # incrémenter la variable de compteur avant de redémarrer la boucle
    x += 1
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*GB1VDH40BeSMPHcbTYVT9g.jpeg)
_[https://pandas.pydata.org/](https://pandas.pydata.org/" rel="noopener" target="_blank" title=")_

### pandas : Bibliothèque d'analyse de données Python

Beautiful Soup transmet les résultats à pandas. Pandas utilise sa fonction `read_html` pour lire les données du tableau HTML dans un dataframe. Le dataframe est ajouté à la liste vide définie précédemment.

Avant que le bloc de code de la boucle ne soit terminé, Selenium doit cliquer sur le bouton retour dans le navigateur. Cela permet au lien suivant dans la boucle d'être disponible pour cliquer sur la page de liste des postes.

Lorsque la boucle for / in est terminée, Selenium a visité chaque lien de titre de poste. Beautiful Soup a récupéré le tableau de chaque page. Pandas a stocké les données de chaque tableau dans un dataframe. Chaque dataframe est un élément de la datalist. Les dataframes de tableaux individuels doivent maintenant être fusionnés en un seul grand dataframe. Les données seront ensuite converties au format JSON avec [pandas.Dataframe.to_json](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_json.html) :

```py
# la boucle est terminée

# terminer la session du navigateur Selenium
driver.quit()

# combiner tous les dataframes pandas de la liste en un seul grand dataframe
result = pd.concat([pd.DataFrame(datalist[i]) for i in range(len(datalist))],ignore_index=True)

# convertir le dataframe pandas en JSON
json_records = result.to_json(orient='records')
```

Maintenant, Python crée le fichier de données JSON. Il est prêt à être utilisé !

```py
# obtenir le répertoire de travail actuel
path = os.getcwd()

# ouvrir, écrire et fermer le fichier
f = open(path + "\\fhsu_payroll_data.json","w") #FHSU
f.write(json_records)
f.close()
```

### Le processus automatisé est rapide

Le processus de web scraping automatisé décrit ci-dessus se termine rapidement. Selenium ouvre une fenêtre de navigateur que vous pouvez voir fonctionner. Cela me permet de vous montrer une vidéo de capture d'écran de la rapidité du processus. Vous voyez à quelle vitesse le script suit un lien, récupère les données, revient en arrière et clique sur le lien suivant. Cela rend la récupération des données de centaines de liens une question de minutes à un seul chiffre.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Hhvf4IOt88A" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Le code Python complet

Voici le code Python complet. J'ai inclus un import pour tabulate. Il nécessite une ligne de code supplémentaire qui utilisera tabulate pour afficher joliment les données dans votre interface de ligne de commande :

```py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
from tabulate import tabulate
import os

# lancer l'URL
url = "http://kanview.ks.gov/PayRates/PayRates_Agency.aspx"

# créer une nouvelle session Firefox
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.get(url)

# Après avoir ouvert l'URL ci-dessus, Selenium clique sur le lien de l'agence spécifique
python_button = driver.find_element_by_id('MainContent_uxLevel1_Agencies_uxAgencyBtn_33') #FHSU
python_button.click() # cliquer sur le lien fhsu

# Selenium transmet la source de la page à Beautiful Soup
soup_level1=BeautifulSoup(driver.page_source, 'lxml')

datalist = [] # liste vide
x = 0 # compteur

# Beautiful Soup trouve tous les liens des titres de poste sur la page de l'agence et la boucle commence
for link in soup_level1.find_all('a', id=re.compile("^MainContent_uxLevel2_JobTitles_uxJobTitleBtn_")):
    
    # Selenium visite chaque page de titre de poste
    python_button = driver.find_element_by_id('MainContent_uxLevel2_JobTitles_uxJobTitleBtn_' + str(x))
    python_button.click() # cliquer sur le lien
    
    # Selenium transmet la source de la page de poste spécifique à Beautiful Soup
    soup_level2=BeautifulSoup(driver.page_source, 'lxml')

    # Beautiful Soup récupère le tableau HTML sur la page
    table = soup_level2.find_all('table')[0]
    
    # Donner le tableau HTML à pandas pour le mettre dans un objet dataframe
    df = pd.read_html(str(table),header=0)
    
    # Stocker le dataframe dans une liste
    datalist.append(df[0])
    
    # Demander à Selenium de cliquer sur le bouton retour
    driver.execute_script("window.history.go(-1)") 
    
    # incrémenter la variable de compteur avant de redémarrer la boucle
    x += 1
    
    # fin du bloc de boucle
    
# la boucle est terminée

# terminer la session du navigateur Selenium
driver.quit()

# combiner tous les dataframes pandas de la liste en un seul grand dataframe
result = pd.concat([pd.DataFrame(datalist[i]) for i in range(len(datalist))],ignore_index=True)

# convertir le dataframe pandas en JSON
json_records = result.to_json(orient='records')

# afficher joliment dans l'interface de ligne de commande avec tabulate
# convertit en un tableau ascii
print(tabulate(result, headers=["Nom de l'employé","Titre du poste","Paiement des heures supplémentaires","Paiement brut total"],tablefmt='psql'))

# obtenir le répertoire de travail actuel
path = os.getcwd()

# ouvrir, écrire et fermer le fichier
f = open(path + "\\fhsu_payroll_data.json","w") #FHSU
f.write(json_records)
f.close()
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*Pn_kqhr2-rqQ7yNV-ymn6Q.jpeg)
_Photo par [Unsplash](https://unsplash.com/photos/ZMraoOybTLQ?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Artem Sapegin</a> sur <a href="https://unsplash.com/search/photos/coffee-laptop?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

### Conclusion

Le **web scraping** avec **Python** et **Beautiful Soup** est un excellent outil à avoir dans votre ensemble de compétences. Utilisez le web scraping lorsque les données dont vous avez besoin pour travailler sont disponibles pour le public, mais pas nécessairement de manière pratique. Lorsque JavaScript fournit ou "cache" du contenu, l'automatisation du navigateur avec **Selenium** garantira que votre code "voit" ce que vous (en tant qu'utilisateur) devriez voir. Et enfin, lorsque vous scrapez des tableaux pleins de données, **pandas** est la bibliothèque d'analyse de données Python qui gérera tout.

### Référence :

L'article suivant a été une référence utile pour ce projet :

[https://pythonprogramminglanguage.com/web-scraping-with-pandas-and-beautifulsoup/](https://pythonprogramminglanguage.com/web-scraping-with-pandas-and-beautifulsoup/)

Contactez-moi à tout moment sur [LinkedIn](https://www.linkedin.com/in/davidagray/) ou [Twitter](https://twitter.com/yesdavidgray). Et si vous avez aimé cet article, donnez-lui quelques applaudissements. Je les apprécierai sincèrement.

[https://www.linkedin.com/in/davidagray/](https://www.linkedin.com/in/davidagray/)

[**Dave Gray (@yesdavidgray) | Twitter**](https://twitter.com/yesdavidgray)  
[_Les derniers Tweets de Dave Gray (@yesdavidgray). Instructeur @FHSUInformatics * Développeur * Musicien * Entrepreneur *_](https://twitter.com/yesdavidgray)  
[twitter.com](https://twitter.com/yesdavidgray)