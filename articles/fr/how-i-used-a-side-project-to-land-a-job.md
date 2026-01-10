---
title: Comment j'ai construit un scraper web avec Beautiful Soup et l'ai utilisé pour
  décrocher mon premier emploi
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-03T18:16:39.000Z'
originalURL: https://freecodecamp.org/news/how-i-used-a-side-project-to-land-a-job
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/alvaro-reyes-6avV9oeHxfo-unsplash.jpg
tags:
- name: career advice
  slug: career-advice
- name: Job Hunting
  slug: job-hunting
- name: Python
  slug: python
- name: 'self-improvement '
  slug: self-improvement
seo_title: Comment j'ai construit un scraper web avec Beautiful Soup et l'ai utilisé
  pour décrocher mon premier emploi
seo_desc: 'By Daniel Chae

  Landing any job, let alone a first job, can be a difficult process. Employers often
  tell you that you don''t have enough experience for them to hire you. But that means
  you also won''t get an opportunity to gain that experience (like a j...'
---

Par Daniel Chae

Décrocher un emploi, et encore plus un premier emploi, peut être un processus difficile. Les employeurs vous disent souvent que vous n'avez pas assez d'expérience pour qu'ils vous embauchent. Mais cela signifie aussi que vous n'aurez pas l'opportunité d'acquérir cette expérience (comme un emploi). 

Décrocher un emploi dans le domaine de la technologie peut sembler encore plus difficile. D'une part, vous devez bien répondre aux questions d'entretien, comme pour tout autre emploi. D'autre part, vous devez prouver que vos compétences techniques sont à la hauteur du poste pour lequel vous postulez. 

Ces obstacles peuvent être difficiles à surmonter. Dans cet article, je vais partager comment j'ai construit un scraper web pour m'aider à décrocher mon premier emploi dans le domaine de la technologie. Je vais expliquer exactement ce que j'ai construit et les leçons clés que j'ai apprises. Plus important encore, je vais partager comment j'ai utilisé ces leçons pour réussir mes entretiens et obtenir une offre d'emploi. 

## Ce que j'ai construit 

![Image](https://www.freecodecamp.org/news/content/images/2021/02/william-iven-gcsNOsPEXfs-unsplash.jpg)

Lorsque je cherchais mon premier emploi, j'étais sur le point d'entamer ma dernière année d'université. J'allais obtenir mon diplôme un semestre plus tôt, alors je me suis fixé comme objectif de décrocher un emploi à temps plein d'ici décembre. Avec cela en tête, je savais que je devais trouver des moyens créatifs pour me démarquer parmi mes pairs. 

J'avais fait quelques excellents stages (dont un chez Facebook), mais je savais que j'avais besoin de quelque chose pour renforcer mon CV. 

J'ai découvert que les projets parallèles avaient un grand potentiel pour y parvenir. J'ai cherché des projets stimulants mais réalisables. Ces projets devaient mettre en valeur mes compétences en programmation et ma passion pour le logiciel. Mais ils devaient aussi montrer mon talent pour le traitement de données (je voulais me diriger vers un rôle dans l'analyse de données).

Après un peu plus de recherches, j'ai trouvé un tutoriel utile similaire à [celui-ci](https://realpython.com/beautiful-soup-web-scraper-python/) qui m'a montré comment extraire des données d'un site web. Le tutoriel m'a inspiré pour construire mon propre scraper web. Mais au lieu de scraper un site aléatoire, je voulais scraper des données boursières. Voici une décomposition de la manière dont je me suis lancé dans la construction de mon projet parallèle. 

## Comment j'ai construit le scraper web

La première chose que j'ai faite a été de réfléchir au type de données que je voulais extraire. À l'époque, je m'intéressais aux données financières. J'ai fait quelques recherches et j'ai découvert que le [site web du NASDAQ](https://www.nasdaq.com/) était un bon point de départ. J'avais fait un stage chez Facebook l'été précédent, alors j'ai pensé que j'essaierais d'extraire les données boursières de Facebook :

```python
#import libraries
import urllib.request
from bs4 import BeautifulSoup

#specify the url
quote_page = 'https://www.nasdaq.com/symbol/fb/after-hours'

# query the website and return the html to the variable 'page'
page = urllib.request.urlopen(quote_page) 

# parse the html using beautiful soup and store in the variable 'soup'
soup = BeautifulSoup(page, 'html.parser') 

# Take out the <div> of name and get its value
name_box = soup.find('h1')

#define variable for where we'll store the name of our stock
name = name_box.text.strip() # strip() is used to remove starting and trailing
print(name)

# get the index price
price_box = soup.find('div', attrs={'class':'qwidget-dollar'})
# define variable for where we'll store the price of our stock
price = price_box.text
print(price)
```

Le script ci-dessus imprimait le prix des actions Facebook ce jour-là. Mais je savais que je ne pouvais pas m'arrêter là. Je devais montrer que je pouvais extraire des données boursières ainsi que faire quelque chose avec ces données. Je ne voulais pas trop compliquer le projet. Mais je voulais aussi inclure suffisamment d'analyse pour impressionner les employeurs potentiels. 

Après un mois de travail, j'ai créé un script Python qui faisait ce qui suit :

* Extraire et ajouter les prix des actions de trois entreprises dans un fichier CSV sur une période de 30 jours
* Importer le CSV sous forme de dataframe et calculer le prix moyen pour chaque action sur les 30 derniers jours
* Visualiser l'évolution du prix des actions pour chaque entreprise à l'aide de matplotlib

Lorsque j'ai acheté un nouvel ordinateur, j'ai oublié de sauvegarder le script réel. Voici un pseudocode au cas où l'un d'entre vous souhaiterait reproduire ce que j'ai fait :

```python
#import libraries
import pandas as pd
from datetime import date, datetime, timedelta
import math
import numpy as np

#Scrape and append three companies' stock prices to a pandas dataframe over the course of 30 days

#1) Scrape stock prices for Company A, Company B, and Company C
#2) Append each stock price for the day to a separate column within a CSV using ExcelWriter (pandas function)
#3) Include a single column in the CSV for the date
#4) Repeat until you have 30 days' worth of data for each company

#Calculate the average price for each stock over the course of the 30 days in the dataframe
#1) Import CSV file back into the script as a dataframe
#2) Generate basic statistics (describe() function) for each column or use the .mean() function if you're looking for just the average

#Visualize the average stock price over the last 30 days using matplotlib
#1) Create a different Time Series line plot for Company A, Company B, and Company C

```

Après avoir terminé l'écriture et le test du script, j'ai rédigé un bref rapport sur ce que j'avais fait. J'ai résumé tout ce que le scraper pouvait faire et comment il pouvait s'appliquer à différents cas d'utilisation. 

Lorsque j'ai mentionné le rapport aux employeurs, ils ne m'ont rarement demandé de le lire. Mais je l'ai gardé à portée de main, au cas où.

## Les leçons clés que j'ai apprises

![Image](https://www.freecodecamp.org/news/content/images/2021/02/moren-hsu-8mifpgpiyBs-unsplash.jpg)

Il y avait trois leçons clés que j'ai apprises de ce projet.

1. La bibliothèque Beautiful Soup est une ressource amusante et ingénieuse pour extraire des données de sites web publics (bien qu'elle soit un peu critiquée). 
2. Il existe un cadre utile pour ceux qui veulent se tailler une carrière dans la technologie, en particulier dans les données. Ce cadre consiste à sourcer des données (interroger une base de données, scraper le web, etc.), formater ces données (Excel, DataFrames, etc.) et en tirer des insights (recommandations clés, statistiques, etc.). 
3. Construire des projets parallèles est la partie facile. Vous devez être capable d'expliquer ce que vous avez fait, pourquoi vous l'avez fait et comment ce que vous avez fait peut s'appliquer à un employeur potentiel. 

## Comment j'ai utilisé ces leçons pour réussir mes entretiens et décrocher mon premier emploi

![Image](https://www.freecodecamp.org/news/content/images/2021/02/linkedin-sales-navigator-W3Jl3jREpDY-unsplash.jpg)

Après avoir écrit les scripts pour le scraper web et l'analyse, je me suis senti prêt à commencer à postuler pour des emplois. Il y avait deux domaines clés sur lesquels je devais me concentrer : mon CV et l'entretien.

### Comment j'ai amélioré mon CV

Je devais me concentrer sur la manière dont je présenterais le scraper web sur mon CV. Je voulais qu'il soit clair que le scraper web pouvait ajouter de la valeur et être bénéfique pour les entreprises auxquelles je postulais. 

Tout d'abord, j'ai réservé une section pour les projets parallèles sur mon CV. Ensuite, j'ai indiqué que j'avais construit un scraper web avec Python en utilisant la bibliothèque Beautiful Soup. 

Cela dit, je ne pouvais pas simplement dire que j'avais construit un scraper web et laisser le CV comme ça. J'ai également veillé à lister des points qui décrivaient les types de données que j'avais extraites. J'ai également listé les composants du script et ce que j'ai fait avec les données. Voici quelques-uns des points que j'ai écrits :

* Extrait les dix principales actions de l'indice NASDAQ en fonction des rendements depuis le début de l'année
* Généré un mois de données NASDAQ et écrit dans un fichier CSV
* Réalisé une analyse statistique approfondie et automatisée en utilisant les données NASDAQ

### Comment je me suis préparé pour l'entretien

Je voulais être sûr de pouvoir expliquer le scraper web à un intervieweur. Je savais que je devais expliquer pourquoi j'avais construit le scraper web en premier lieu. Mais je devais aussi être prêt à expliquer pourquoi le scraper web était précieux pour le poste. 

Cela nécessitait deux étapes : identifier les compétences techniques que j'ai utilisées dans le projet parallèle et relier ces compétences aux responsabilités clés dans la description de poste. 

J'ai pris le temps de réfléchir à chaque chose que j'ai faite pour construire le scraper web. Après avoir fait un remue-méninges, voici les compétences techniques que j'ai identifiées :

* Python
* Excel
* Web Scraping
* Data Wrangling
* Data Automation
* Data Analysis
* Statistical Analysis
* Financial Forecasting

Pour les responsabilités clés, je me suis assuré de préparer des réponses pour l'entretien. Je l'ai fait en reliant une compétence technique que j'ai utilisée pour le scraper web à la responsabilité correspondante. 

Prenons cette responsabilité clé d'un rôle d'analyste de données chez Hulu :

> "Build data models, data visualizations and automated analytics that operationalize insights across the business"

Pour cela, j'ai préparé une histoire sur la manière dont j'ai utilisé les données NASDAQ pour créer une visualisation de prévision financière. J'ai également préparé une histoire sur la manière dont j'ai automatisé le web scraping et l'analyse.

## Ensuite, j'ai obtenu une offre d'emploi

![Image](https://www.freecodecamp.org/news/content/images/2021/02/stefan-stefancik-Ue2-23uBwNw-unsplash.jpg)

Plusieurs semaines se sont écoulées avant que je ne tombe sur un poste d'analyste de données pour une entreprise de divertissement. 

Ils m'ont contacté au sujet de ma candidature et m'ont fait passer le processus d'entretien. J'ai vérifié chaque détail. Je me suis assuré de pouvoir relier chaque compétence technique du scraper web aux responsabilités clés de la description de poste. 

Chaque intervieweur a posé des questions sur différentes parties du scraper web. Ils étaient très intéressés par les parties de traitement de données et d'analyse automatisée du projet parallèle. Je me suis assuré de pouvoir expliquer ces facettes du scraper web. J'ai utilisé le format S.T.A.R. (Situation, Tâche, Action et Résultat) pour chacune de mes réponses d'entretien. 

Quatre tours d'intervieweurs plus tard, l'entreprise m'a proposé un poste à temps plein et salarié. La lettre d'offre est arrivée à la mi-décembre.

## Allez trouver votre prochain projet parallèle

![Image](https://www.freecodecamp.org/news/content/images/2021/02/sigmund-Fv2J-aK0Acs-unsplash.jpg)

Lorsque je regarde en arrière le processus d'obtention de ma première offre d'emploi, je suis content d'avoir construit le scraper web. C'était stressant de passer les entretiens comportementaux et techniques. Mais je suis content d'avoir eu les moyens de me préparer et de réussir ces entretiens.

Décrocher ce premier emploi peut être difficile car vous devez somehow obtenir de l'expérience avant de pouvoir le faire pratiquement. C'est un cycle potentiellement vicieux dont il peut être difficile de sortir. 

Cela dit, soyez assuré qu'il existe un chemin clair vers le succès. Vous avez une opportunité incroyable d'acquérir de l'expérience de manière créative (comme construire un scraper web) et de décrocher ce premier emploi.