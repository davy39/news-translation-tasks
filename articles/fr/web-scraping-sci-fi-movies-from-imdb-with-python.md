---
title: Web Scraping en Python – Comment extraire des films de science-fiction depuis
  IMDB
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-08-09T19:50:10.000Z'
originalURL: https://freecodecamp.org/news/web-scraping-sci-fi-movies-from-imdb-with-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/pexels-pixabay-270348--1-.jpg
tags:
- name: Python
  slug: python
- name: web scraping
  slug: web-scraping
seo_title: Web Scraping en Python – Comment extraire des films de science-fiction
  depuis IMDB
seo_desc: "By Riley Predum\nHave you ever struggled to find a dataset for your data\
  \ science project? If you're like I am, the answer is yes. \nLuckily, there are\
  \ many free datasets available – but sometimes you want something more specific\
  \ or bespoke. For that, w..."
---

Par Riley Predum

Avez-vous déjà eu du mal à trouver un ensemble de données pour votre projet de science des données ? Si vous êtes comme moi, la réponse est oui. 

Heureusement, il existe de nombreux ensembles de données gratuits disponibles – mais parfois vous voulez quelque chose de plus spécifique ou sur mesure. Pour cela, le web scraping est une compétence utile à avoir dans votre boîte à outils pour extraire des données de votre site web préféré.

## Qu'est-ce qui est couvert dans cet article ?

Cet article contient un script Python que vous pouvez utiliser pour extraire les données sur les films de science-fiction (ou tout autre genre que vous choisissez !) depuis le site [IMDB](https://www.imdb.com/). Il peut ensuite écrire ces données dans un dataframe pour une exploration plus approfondie. 

Je conclurai cet article avec une analyse exploratoire des données (EDA). À travers cela, vous verrez quels autres projets de science des données sont possibles pour vous d'essayer.

_Avertissement : bien que le web scraping soit un excellent moyen d'extraire des données de sites web de manière programmatique, veuillez le faire de manière responsable. Mon script utilise la fonction sleep, par exemple, pour ralentir intentionnellement les requêtes de pull, afin de ne pas surcharger les serveurs d'IMDB. Certains sites web désapprouvent l'utilisation de web scrapers, alors utilisez-les judicieusement._

## Script de Web Scraping et de Nettoyage des Données

Passons au script de scraping et faisons-le fonctionner. Le script extrait les titres de films, les années, les notes (PG-13, R, etc.), les genres, les durées, les critiques et les votes pour chaque film. Vous pouvez choisir le nombre de pages que vous souhaitez scraper en fonction de vos besoins en données. 

_Note : cela prendra plus de temps si vous sélectionnez plus de pages. Il faut 40 minutes pour scraper 200 pages web en utilisant le [Google Colab Notebook](https://colab.research.google.com/drive/11avx1TqYw_2sb5tUNi0ZO4ABRc50LNxK?usp=sharing)._

Pour ceux d'entre vous qui ne l'ont pas encore essayé, Google Colab est un outil de développement Python basé sur le cloud, de style [Jupyter Notebook](https://realpython.com/jupyter-notebook-introduction/#:~:text=The%20Jupyter%20Notebook%20is%20an,the%20people%20at%20Project%20Jupyter.), qui fait partie de la suite d'applications Google. Vous pouvez l'utiliser directement avec de nombreux packages déjà installés, courants en science des données. 

Ci-dessous se trouve une image de l'espace de travail Colab et de sa disposition :

![Image](https://lh4.googleusercontent.com/R9sAuHzGHrEvRK_hiAWsy4W41W72et6clD38gIYeAA6AtA32e97xxw0W5ub_96xmgSMTDB2VjRK-gz_YgYtZoV1YyCHjKftaB7-HD2NQ7qt_8hcdnDfqaibp0ONwPr9-4zO5gv3FuXdxiOMsN6eF8bA)
_Présentation de l'interface utilisateur de Google Colab_

Avec cela, plongeons-nous ! Tout d'abord, vous devez toujours importer vos packages dans leur propre cellule. Si vous oubliez un package, vous pouvez réexécuter uniquement cette cellule. Cela réduit le temps de développement. 

Note : certains de ces packages nécessitent d'exécuter `pip install package_name` pour les installer d'abord. Si vous choisissez d'exécuter le code localement en utilisant quelque chose comme un Jupyter Notebook, vous devrez le faire. Si vous voulez vous lancer rapidement, vous pouvez utiliser le notebook Google Colab. Tous ces packages sont installés par défaut.

```python
from requests import get
from bs4 import BeautifulSoup
from warnings import warn
from time import sleep
from random import randint
import numpy as np, pandas as pd
import seaborn as sns
```

## Comment faire du Web Scraping

Vous pouvez exécuter le code suivant qui effectue le web scraping proprement dit. Il extraira toutes les colonnes mentionnées ci-dessus dans des tableaux et les remplira un film à la fois, une page à la fois. 

J'ai également ajouté et documenté quelques étapes de nettoyage des données dans ce code. J'ai supprimé les parenthèses des données de chaîne mentionnant l'année du film, par exemple. J'ai ensuite converti celles-ci en entiers. Des choses comme cela rendent l'analyse exploratoire des données et la modélisation plus faciles.

Notez que j'utilise la fonction sleep pour éviter d'être limité par IMDB lorsqu'il s'agit de parcourir leurs pages web trop rapidement.

```python
# Notez que cela prend environ 40 minutes à exécuter si np.arange est défini à 9951 comme point d'arrêt.

pages = np.arange(1, 9951, 50) # La dernière fois que j'ai essayé, je ne pouvais aller que jusqu'à 10000 éléments car après cela, l'URI n'a pas de motif discernable pour contrer les webcrawlers ; j'ai juste fait 4 pages à des fins de démonstration. Vous pouvez augmenter cela pour vos propres projets.
headers = {'Accept-Language': 'en-US,en;q=0.8'} # Si cela n'est pas spécifié, la langue par défaut est le mandarin

#initialiser des listes vides pour stocker les variables scrapées
titles = []
years = []
ratings = []
genres = []
runtimes = []
imdb_ratings = []
imdb_ratings_standardized = []
metascores = []
votes = []

for page in pages:
  
   #requête get pour la science-fiction
   response = get("https://www.imdb.com/search/title?genres=sci-fi&"
                  + "start="
                  + str(page)
                  + "&explore=title_type,genres&ref_=adv_prv", headers=headers)
  
   sleep(randint(8,15))
   
   #lancer un avertissement pour les codes de statut autres que 200
   if response.status_code != 200:
       warn('Request: {}; Status code: {}'.format(requests, response.status_code))

   #analyser le contenu de l'itération actuelle de la requête
   page_html = BeautifulSoup(response.text, 'html.parser')
      
   movie_containers = page_html.find_all('div', class_ = 'lister-item mode-advanced')
  
   #extraire les 50 films de cette page
   for container in movie_containers:

       #conditionnel pour tous ceux avec un metascore
       if container.find('div', class_ = 'ratings-metascore') is not None:

           #titre
           title = container.h3.a.text
           titles.append(title)

           if container.h3.find('span', class_= 'lister-item-year text-muted unbold') is not None:
            
             #année de sortie
             year = container.h3.find('span', class_= 'lister-item-year text-muted unbold').text # supprimer les parenthèses autour de l'année et en faire un entier
             years.append(year)

           else:
             years.append(None) # chacune des clauses if supplémentaires sert à gérer les données de type None, en les remplaçant par une chaîne vide afin que les tableaux soient de la même longueur à la fin du scraping

           if container.p.find('span', class_ = 'certificate') is not None:
            
             #note
             rating = container.p.find('span', class_= 'certificate').text
             ratings.append(rating)

           else:
             ratings.append("")

           if container.p.find('span', class_ = 'genre') is not None:
            
             #genre
             genre = container.p.find('span', class_ = 'genre').text.replace("\n", "").rstrip().split(',') # supprimer le caractère d'espace blanc, strip, et split pour créer un tableau de genres
             genres.append(genre)
          
           else:
             genres.append("")

           if container.p.find('span', class_ = 'runtime') is not None:

             #durée
             time = int(container.p.find('span', class_ = 'runtime').text.replace(" min", "")) # supprimer le mot minute de la durée et en faire un entier
             runtimes.append(time)

           else:
             runtimes.append(None)

           if float(container.strong.text) is not None:

             #notes IMDB
             imdb = float(container.strong.text) # variable non standardisée
             imdb_ratings.append(imdb)

           else:
             imdb_ratings.append(None)

           if container.find('span', class_ = 'metascore').text is not None:

             #Metascore
             m_score = int(container.find('span', class_ = 'metascore').text) # en faire un entier
             metascores.append(m_score)

           else:
             metascores.append(None)

           if container.find('span', attrs = {'name':'nv'})['data-value'] is not None:

             #Nombre de votes
             vote = int(container.find('span', attrs = {'name':'nv'})['data-value'])
             votes.append(vote)

           else:
               votes.append(None)

           else:
               votes.append(None)
```

Les dataframes pandas prennent en entrée des tableaux de données pour chacune de leurs colonnes dans des paires clé:valeur. J'ai fait quelques étapes supplémentaires de nettoyage des données ici pour finaliser le nettoyage des données. 

Après avoir exécuté la cellule suivante, vous devriez avoir un dataframe avec les données que vous avez scrapées.

```python
sci_fi_df = pd.DataFrame({'movie': titles,
                      'year': years,
                      'rating': ratings,
                      'genre': genres,
                      'runtime_min': runtimes,
                      'imdb': imdb_ratings,
                      'metascore': metascores,
                      'votes': votes}
                      )

sci_fi_df.loc[:, 'year'] = sci_fi_df['year'].str[-5:-1] # deux transformations de données supplémentaires après le scraping
# Supprimer le bug 'ovie'
# Faire de l'année un int
sci_fi_df['n_imdb'] = sci_fi_df['imdb'] * 10
final_df = sci_fi_df.loc[sci_fi_df['year'] != 'ovie'] # Un petit problème avec le scraping sur ces deux films, donc je les supprime simplement.
final_df.loc[:, 'year'] = pd.to_numeric(final_df['year'])
```

## Analyse Exploratoire des Données

Maintenant que vous avez les données, l'une des premières choses que vous pourriez vouloir faire est d'en apprendre davantage à un niveau élevé. Les commandes suivantes sont un premier aperçu utile de toute donnée et nous les utiliserons ensuite :

```python
final_df.head()
```

Cette commande vous montre les 5 premières lignes de votre dataframe. Elle vous aide à voir que rien ne semble bizarre et que tout est prêt pour l'analyse. Vous pouvez voir le résultat ici :

![Image](https://lh3.googleusercontent.com/TCYKlpEKIJOVJIAtIGN4wzDhCySaYIXI9cyBizZxR3XHsAQO_YH9mh626hCq8fdItaAF0N0cxSs1PP1eYujRsOt8HgeXtcC3hff-y0Jl4tvN__itH97iXqb6DrN6wJrngdsNaKQTQag5StHfOIcy5A0)
_Les cinq premières lignes de données produites en utilisant la commande `final_df.head()`_

```python
final_df.describe()
```

Cette commande vous fournira la moyenne, l'écart type et d'autres résumés. Le compte peut vous montrer s'il y a des valeurs nulles dans certaines des colonnes, ce qui est une information utile à connaître. La colonne année, par exemple, vous montre la plage de films scrapés – de 1927 à 2022. 

Vous pouvez voir le résultat ci-dessous et inspecter les autres :

![Image](https://lh6.googleusercontent.com/Zeo_Y8ipyIejyYIBa2Aaocz4obHNlMVU76YTylZGl_wpRovYVFNS4e0m1DYAwkcqhpoYikJFL_dSgZSH-qoghJM3VMXESMUykrfs1e3JuXRkrp9iEZhPPnqGvsSamdYQe6Noz0Q0OA-Wen616-pmbDQ)
_L'exécution de `final_df.describe()` produit des statistiques récapitulatives montrant le nombre de points de données, les moyennes, les écarts types, et plus encore._

```python
final_df.info()
```

Cette commande vous informe des types de données avec lesquels vous travaillez dans chacune de vos colonnes. 

En tant que scientifique des données, cette information peut vous être utile. Certaines fonctions et méthodes nécessitent certains types de données. Vous pouvez également vous assurer que vos types de données sous-jacents sont dans un format qui a du sens pour ce qu'ils sont. 

Par exemple : une note de 5 étoiles doit être un float ou un int (si les décimales ne sont pas autorisées). Elle ne doit pas être une chaîne de caractères puisque c'est un nombre. Voici un résumé du format des données pour chaque variable après le scraping :

![Image](https://lh3.googleusercontent.com/PT7Fa9XFYErtorVw6bNxw7Q1mI-p2_hlKgTbTs90RRpALPDlqd95F_EOwCQ7cV2cDymqZ-mXIa_0blqxxJ5wZ8Bznzd0iFyTB6kFroIUK2DJNzfRZgwgsRHr0pjDyE1ZUrQILf-22w856OoufnnKmRI)
_L'exécution de `final_df.info()` montre combien de valeurs vous avez dans chaque colonne et quels sont leurs types de données._

La commande suivante pour en savoir plus sur vos variables produit une heatmap. La heatmap montre la corrélation entre toutes vos variables quantitatives. C'est un moyen rapide d'évaluer les relations qui peuvent exister entre les variables. J'aime voir les coefficients plutôt que d'essayer de déchiffrer le code couleur, donc j'utilise l'argument `annot=True`.

```python
sns.heatmap(final_df.corr(), annot=True);
```

La commande ci-dessus produit la visualisation suivante en utilisant le package de visualisation de données Seaborn :

![Image](https://lh3.googleusercontent.com/niHLKP7bps1EpZ_39u5k3dPDF0Xuz8Zuhal8Bbc8wtImKUv50M_7fEH65rCAkrTglGtZTJpZ2sRfIE0E6Kjn9m_CYGkRct83_3wWzVp0rnHA8nh5UuveFO0OqtjVfoOzMsKGq0lZ2uxw66Lp4g69aMo)
_Une heatmap des corrélations après l'exécution de `sns.heatmap(final_df.corr(), annot=True);`_

Vous pouvez voir que la corrélation la plus forte est entre le score IMDB et le metascore. Cela n'est pas surprenant puisque il est probable que deux systèmes de notation de films notent de manière similaire.

La corrélation suivante la plus forte que vous pouvez voir est entre la note IMDB et le nombre de votes. Cela est intéressant car, à mesure que le nombre de votes augmente, vous avez un échantillon plus représentatif de la population notant. Il est étrange de voir qu'il existe une association faible entre les deux, cependant.

Le nombre de votes augmente également à mesure que la durée augmente.

Vous pouvez également voir une légère association négative entre IMDB ou metascore et l'année de sortie du film. Nous examinerons cela sous peu.

Vous pouvez vérifier certaines de ces relations visuellement via un nuage de points avec ce code :

```python
x = final_df['n_imdb']
y = final_df['votes']
plt.scatter(x, y, alpha=0.5) # s= est la variable de taille, c= est la variable de couleur
plt.xlabel("Note IMDB Standardisée")
plt.ylabel("Nombre de Votes")
plt.title("Nombre de Votes vs. Note IMDB")
plt.ticklabel_format(style='plain')
plt.show()
```

Cela donne la visualisation suivante :

![Image](https://lh3.googleusercontent.com/vvqxh5VwbHPoypyGlNBstgZW8puVWKa5m_hl6MYB_r78OfRC7TWBx9jxjf8PFflJO93hq83ZdIqX97uq6C_WjlZV5jorCDgtU3U3_dESuUgsStfLEgkeiikHTq2noabW_tPJQRRGpFrVmQ90gja4xAo)
_Notes IMDB vs. Nombre de Votes_

L'association ci-dessus montre quelques valeurs aberrantes. En général, nous voyons un plus grand nombre de votes sur les films qui ont une note IMDB de 85 ou plus. Il y a moins de critiques sur les films avec une note de 75 ou moins. 

En traçant ces boîtes autour des données, vous pouvez voir ce que je veux dire. Il y a environ deux regroupements de magnitudes différentes :

![Image](https://lh6.googleusercontent.com/QEUbjZrtSiLCbdcXIR1MN0MKvcCZgVxeW2sPzMo4KL36pjCQq87rkRdgKKwK2yWSh2Uz0HMoIckyOa0qcNX4hCQok_kuuyqq4PddFHVuC5Tzyg9-WdZobdZgWfOpW1PnKWFKfQLaDAEDXoDHfiuU5mY)
_Deux Groupes Principaux dans les Données_

Une autre chose qui pourrait être intéressante à voir est le nombre de films pour chaque note. Cela peut vous montrer où la science-fiction tend à se situer dans les données de notation. Utilisez ce code pour obtenir un graphique à barres des notes :

```python
ax = final_df['rating'].value_counts().plot(kind='bar',
                                   figsize=(14,8),
                                   title="Nombre de Films par Note")
ax.set_xlabel("Note")
ax.set_ylabel("Nombre de Films")
ax.plot();
```

Ce code donne le graphique suivant qui nous montre que R et PG-13 constituent la majorité de ces films de science-fiction sur IMDB.

![Image](https://lh3.googleusercontent.com/7896rs2HtqgI4nIPyI-vUU5w43C3_Dcuyc_DdjUOudq76aIHstBINNVf5e0-1G3MUZzFgKDzK_2Jhsnno5swbXIoZwMuxqg1icY8aPbxWjOsCIm3BB9lObzY7HiDSAhmLTfcpfi2HWdW4VoUjBcnbrk)
_Nombre de Films par Note_

J'ai remarqué qu'il y avait quelques films notés "Approuvé" et j'étais curieux de savoir ce que cela signifiait. Vous pouvez filtrer le dataframe avec ce code pour approfondir cela :

```python
final_df[final_df['rating'] == 'Approved']
```

Cela a révélé que la plupart de ces films ont été réalisés avant les années 80 :

![Image](https://lh3.googleusercontent.com/OIxMNDTgcXcPo_Wy8N7miq44OOAai4o-A8upYa1pNbqWjDVzPduRxNcMgUPuG9-OFyNd1AFgwWeq_o4E3Kv9pXy8xVSH7p6ZZi9uoOy78dBFK0LjvDnN9k7WYDTiZYxwpVgCiqXokWLPuMo746jvWMo)
_Tous les Films avec la Note "Approuvé"_

Je suis allé sur le site web de la MPAA et il n'y avait aucune mention d'eux sur leur page d'informations sur les notes. Cela a dû être abandonné à un moment donné.

Vous pourriez également vérifier si certaines années ou décennies ont surpassé les autres en termes de critiques. J'ai pris la moyenne des metascores par année et j'ai tracé cela avec le code suivant pour explorer davantage :

```python
# Quelles sont les moyennes des metascores par année ?
final_df.groupby('year')['metascore'].mean().plot(kind='bar', figsize=(16,8), title="Moyenne des Metascores par Année", xlabel="Année", ylabel="Moyenne des Metascores")
plt.xticks(rotation=90)
plt.plot();
```

Cela donne le graphique suivant :

![Image](https://lh5.googleusercontent.com/BTwJBQhq0zBTr5UH5J3n7CSR6k3Ft8l9GBQ_czZRlu_LO192AXd0G_ozwXzsb6pctS-8lHCvgVLx6VZ7hWH-trp8C4oFAPCGufh2gq-F2WV96u90xt05KqUGYCqSFpmXxPEsFKSZQceglNItwChRnfE)
_Moyenne des Metascores par Année de Film_

Je ne dis pas que je sais pourquoi, mais il y a un déclin progressif et léger à mesure que l'on avance dans l'histoire de la variable moyenne des metascores. Il semble que les notes se soient stabilisées autour de 55-60 au cours des dernières décennies. Cela pourrait être dû au fait que nous avons plus de données sur les films plus récents ou que les films plus récents tendent à être plus souvent critiqués.

```python
final_df['year'].value_counts().plot(kind='bar', figsize=[20,9])
```

Exécutez le code ci-dessus et vous verrez que le film de 1927 n'avait qu'un échantillon de 1 critique. Ce score est alors biaisé et surévalué. Vous verrez également que les films plus récents sont mieux représentés dans les critiques comme je le soupçonnais :

![Image](https://lh6.googleusercontent.com/d2C-t1DLqSjRY8DpeoudyBNHG4SevXCZXFK4xoaw3QHpj_j4qnEf479Tn7wNyBqOwKAzR5GVidaRZ79XB5Eo36msA8LRBxNaJu_9Xk1VKE5oeo2Pue1TLnbjMX3y48Gc5xfOBnlZ1x9rdTktI_N2Bpg)
_Nombre de Films par Année_

## Idées de Projets de Science des Données pour Aller Plus Loin

Vous avez ici des variables textuelles, catégorielles et numériques. Il y a quelques options que vous pourriez essayer pour explorer davantage.

Une chose que vous pourriez faire est d'utiliser le traitement du langage naturel (NLP) pour voir s'il existe des conventions de nommage pour les notes de films, ou dans le monde de la science-fiction (ou si vous choisissez de faire un autre genre, celui que vous avez choisi !). 

Vous pourriez modifier le code de web scraping pour inclure beaucoup plus de genres. Avec cela, vous pourriez créer une nouvelle base de données inter-genres pour voir s'il existe des conventions de nommage par genre.

Vous pourriez ensuite essayer de prédire le genre en fonction du nom du film. Vous pourriez également essayer de prédire la note IMDB en fonction du genre ou de l'année de sortie du film. Cette dernière idée fonctionnerait mieux au cours des dernières décennies puisque la plupart des observations s'y trouvent.

J'espère que ce tutoriel a éveillé votre curiosité sur le monde de la science des données et ce qui est possible ! 

Vous constaterez dans l'analyse exploratoire des données qu'il y a toujours plus de questions à poser. Travailler avec cette contrainte consiste à prioriser en fonction des objectifs commerciaux. Il est important de commencer avec ces objectifs dès le départ, sinon vous pourriez vous perdre dans les données en explorant indéfiniment.

Si le domaine de la science des données vous intéresse et que vous souhaitez développer vos compétences et entrer dans ce domaine professionnellement, envisagez de consulter le [Data Science Career Track](https://www.springboard.com/courses/data-science-career-track/) de Springboard. Dans ce cours, Springboard vous guide à travers tous les concepts clés en profondeur avec un mentor expert en 1:1 pour vous soutenir dans votre parcours.

J'ai écrit d'autres articles qui cadrent les projets de science des données en relation avec des problèmes commerciaux et qui passent en revue des approches techniques pour les résoudre sur mon [Medium](https://medium.com/@rileypredum). Consultez-les si vous êtes intéressé !

Bonne programmation !

Riley