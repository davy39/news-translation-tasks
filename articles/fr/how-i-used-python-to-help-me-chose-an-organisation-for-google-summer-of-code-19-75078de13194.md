---
title: Comment j'ai utilisé Python pour m'aider à choisir une organisation pour le
  Google Summer of Code 2019
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-10T16:59:38.000Z'
originalURL: https://freecodecamp.org/news/how-i-used-python-to-help-me-chose-an-organisation-for-google-summer-of-code-19-75078de13194
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ucoUbiOID-texxFdJ8v2jw.jpeg
tags:
- name: data analysis
  slug: data-analysis
- name: gsoc
  slug: gsoc
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: web scraping
  slug: web-scraping
seo_title: Comment j'ai utilisé Python pour m'aider à choisir une organisation pour
  le Google Summer of Code 2019
seo_desc: 'By Vaibhav Gupta

  In this tutorial, I’ll be using python to scrape data from the Google Summer of
  Code (GSoC) archive about the participating organizations from the year 2009.

  My Motivation Behind This Project

  While I was scrolling through the huge li...'
---

Par Vaibhav Gupta

Dans ce tutoriel, j'utiliserai Python pour extraire des données de l'archive du Google Summer of Code (GSoC) concernant les organisations participantes de l'année 2009.

### Ma Motivation Derrière Ce Projet

Alors que je faisais défiler la longue liste des organisations ayant participé au GSoC 2018, j'ai réalisé qu'explorer une organisation est une tâche répétitive : en choisir une, explorer ses projets, vérifier si elle a participé les années précédentes ou non. Mais il y a plus de 200 organisations, et les parcourir toutes prendrait beaucoup de temps. Alors, étant une personne paresseuse, j'ai décidé d'utiliser Python pour faciliter mon travail.

### Prérequis

* _Python (j'utiliserai Python 3.6, car les f-strings sont géniales ?)_
* _Pipenv (pour l'environnement virtuel)_
* _requests (pour récupérer la page web)_
* _Beautiful Soup 4 (pour extraire les données des pages web)_

### Construction de Notre Script

Voici les pages web que nous allons scraper :

1. Pour les années 2009–2015 : [Lien](https://www.google-melange.com/archive/gsoc)
2. Pour les années 2015–2018 : [Lien](https://summerofcode.withgoogle.com/archive/)

### Partie Codage

![Image](https://cdn-media-1.freecodecamp.org/images/1*u5vEWeGuTXMWZiQQz8PbqQ.gif)
_[GIF de Giphy](https://giphy.com/gifs/nascar-owen-wilson-daytona-500-xTiN0GMUaOI726QYZa" rel="noopener" target="_blank" title=")_

#### Étape 1 : Configuration de l'environnement virtuel et installation des dépendances

_virtualenv_ peut être utilisé pour créer un environnement virtuel, mais je recommande d'utiliser _Pipenv_ car il minimise le travail et supporte _Pipfile_ et _Pipfile.lock_.

Créez un nouveau dossier et entrez la série de commandes suivante dans le terminal :

```
pip install pipenv
```

Ensuite, créez un environnement virtuel et installez toutes les dépendances avec une seule commande (Pipenv est génial ?) :

```
pipenv install requests beautifulsoup4 --three
```

La commande ci-dessus effectuera les tâches suivantes :

* Créer un environnement virtuel (pour Python 3).
* Installer _requests_ et _beautifulsoup4_.
* Créer `Pipfile` et `Pipfile.lock` dans le même dossier.

Maintenant, activez l'environnement virtuel :

```
pipenv shell
```

Remarquez le nom du dossier avant `$` lors de l'activation, comme ceci :

```
(gsoc19) $
```

#### Étape 2 : Extraction des données pour les années 2009–2015

Ouvrez un éditeur de code et créez un nouveau fichier Python (je vais le nommer `2009–2015.py`). La page web contient les liens vers la liste des organisations de chaque année. Tout d'abord, écrivez une fonction utilitaire dans un fichier séparé `utils.py` qui récupérera n'importe quelle page web pour nous et lèvera une `Exception` s'il y a une erreur de connexion.

Maintenant, obtenez le lien de la page web qui contient la liste des organisations pour chaque année.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pyKlRbBI5wfHuxFmSxoWjQ.png)
_Aperçu de la page web_

Pour cela, créez une fonction `get_year_with_link`. Avant d'écrire la fonction, nous devons inspecter un peu cette page web. Faites un clic droit sur une année et cliquez sur _Inspecter_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*4qOIYUKISEcOIPcshCZ8KQ.png)

Notez qu'il y a une balise `<ul>`, et à l'intérieur, des balises `<li>`, chacune contenant une balise `<span>` avec la classe mdl-list__item-primary-content, à l'intérieur de laquelle se trouvent notre lien et l'année. Notez également que ce motif est le même pour chaque année. Nous voulons récupérer ces données.

Les tâches effectuées par cette fonction sont dans cet ordre :

1. Obtenir la `MAIN_PAGE`, lever une exception s'il y a une erreur de connexion.
2. Si le code de réponse est `200 OK`, analyser la page web récupérée avec BeautifulSoup. Si le code de réponse est autre chose, quitter le programme.
3. Trouver toutes les balises `<li>` avec la classe `mdl-list__item mdl-list__item — one-line` et stocker la liste retournée dans `years_li`.
4. Initialiser un dictionnaire `years_dict` vide.
5. Commencer à itérer sur la liste `years_li`.
6. Obtenir le texte de l'année (2009, 2010, 2011, ...), supprimer tous les `\n`, et le stocker dans `year`.
7. Obtenir le lien relatif de chaque année (/archive/gsoc/2015, /archive/gsoc/2016, ...) et le stocker dans `relative_link`.
8. Convertir le `relative_link` en lien complet en le combinant avec le lien `HOME_PAGE` et le stocker dans `full_link`.
9. Ajouter ces données au dictionnaire `year_dict` avec l'année comme clé et `full_link` comme valeur.
10. Répéter cela pour toutes les années.

Cela nous donnera un dictionnaire avec les années comme clés et leurs liens comme valeurs dans ce format :

```
{  ...  '2009': 'https://www.google-melange.com/archive/gsoc/2009',  '2010': 'https://www.google-melange.com/archive/gsoc/2010',  ...}
```

Maintenant, nous voulons visiter ces liens et obtenir le nom de chaque organisation avec leurs liens depuis ces pages. Faites un clic droit sur le nom de n'importe quelle organisation et cliquez sur _Inspecter_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ISaEmvazH3dr8Knfe3MtqA.png)

Notez qu'il y a une balise `<ul>` avec la classe `mdl-list`, qui contient des balises `<li>` avec la classe `mdl-list__item mdl-list__item — one-line`. À l'intérieur de chacune, il y a une balise `<a>` qui contient le lien et le nom de l'organisation. Nous voulons récupérer cela. Pour cela, créons une autre fonction `get_organizations_list_with_links`, qui prend les liens des pages web contenant la liste des organisations pour chaque année (que nous avons scrapées dans `get_year_with_link`).

Les tâches effectuées par cette fonction sont dans cet ordre :

1. Obtenir la page de la liste des organisations ([https://www.google-melange.com/archive/gsoc/2015](https://www.google-melange.com/archive/gsoc/2015), [https://www.google-melange.com/archive/gsoc/201](https://www.google-melange.com/archive/gsoc/2015)6, ...), lever une exception s'il y a une erreur de connexion.
2. Si le code de réponse est `200 OK`, analyser la page web récupérée avec BeautifulSoup. Si le code de réponse est autre chose, quitter le programme.
3. Trouver toutes les balises `<li>` avec la classe `mdl-list__item mdl-list__item — one-line` et stocker la liste retournée dans `orgs_li`.
4. Initialiser un dictionnaire `orgs_dict` vide.
5. Commencer à itérer sur la liste `orgs_li`.
6. Obtenir le nom de l'organisation, supprimer tous les `\n`, et le stocker dans `org_name`.
7. Obtenir le lien relatif de chaque organisation (/archive/gsoc/2015/orgs/n52, /archive/gsoc/2015/orgs/beagleboard, ...) et le stocker dans `relative_link`.
8. Convertir le `relative_link` en lien complet en le combinant avec le lien `HOME_PAGE` et le stocker dans `full_link`.
9. Ajouter ces données au dictionnaire `orgs_dict` avec `org_name` comme clé et `full_link` comme valeur.
10. Répéter cela pour toutes les organisations d'une année particulière.

Cela nous donnera un dictionnaire avec les noms des organisations comme clés et leurs liens comme valeurs, comme ceci :

```
{  ...  'ASCEND': 'https://www.google-melange.com/archive/gsoc/2015/orgs/ascend',
```

```
'Apache Software Foundation': 'https://www.google-melange.com/archive/gsoc/2015/orgs/apache',  ...}
```

En continuant, nous voulons visiter ces liens et obtenir le titre, la description et le lien de chaque projet de chaque organisation pour chaque année (?). Faites un clic droit sur le titre de n'importe quel projet et cliquez sur _Inspecter_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Sb8nG8HeNSqrwUVG5BTiAQ.png)

Encore une fois, le même motif. Il y a une balise `<ul>` avec la classe `mdl-list` qui contient des balises `<li>` avec la classe `mdl-list__item mdl-list__item — two-line`, à l'intérieur desquelles il y a une balise `<span>` qui contient une balise `<a>` contenant le nom de notre projet. De plus, il y a une balise `<span>` avec la classe `mdl-list__item-sub-title` contenant la description du projet. Pour cela, créez une fonction `get_org_projects_info` pour accomplir cette tâche.

Les tâches effectuées par cette fonction sont dans cet ordre :

1. Obtenir la page de description de l'organisation ([https://www.google-melange.com/archive/gsoc/2015/orgs/ascend](https://www.google-melange.com/archive/gsoc/2015/orgs/ascend), [https://www.google-melange.com/archive/gsoc/2015/orgs/apache](https://www.google-melange.com/archive/gsoc/2015/orgs/apache), ...), lever une exception s'il y a une erreur de connexion.
2. Si le code de réponse est `200 OK`, analyser la page web récupérée avec BeautifulSoup. Si le code de réponse est autre chose, quitter le programme.
3. Trouver toutes les balises `<li>` avec la classe `mdl-list__item mdl-list__item — two-line` et stocker la liste retournée dans `projects_li`.
4. Initialiser une liste `projects_info` vide.
5. Commencer à itérer sur la liste `projects_li`.
6. Initialiser un dictionnaire `proj_info` vide à chaque boucle.
7. Obtenir le titre du projet, supprimer tous les `\n`, et le stocker dans `proj_title`.
8. Obtenir le lien relatif de chaque projet ([https://www.google-melange.com/archive/gsoc/2015/orgs/apache/projects/djkevincr.html](https://www.google-melange.com/archive/gsoc/2015/orgs/apache/projects/djkevincr.html), ...) et le stocker dans `proj_relative_link`.
9. Convertir le `proj_relative_link` en lien complet en le combinant avec le lien `HOME_PAGE` et le stocker dans `proj_full_link`.
10. Stocker le titre, la description et le lien du projet dans le dictionnaire `proj_info` et ajouter ce dictionnaire à la liste `projects_info`.

Cela nous donnera une liste contenant des dictionnaires avec les données des projets.

```
[  ...  {    'title': 'Titre du Projet 1',    'description': 'Description du Projet 1',    'link': 'http://lien-projet-1.com/',  },  {    'title': 'Titre du Projet 2',    'description': 'Description du Projet 2',    'link': 'http://lien-projet-2.com/',  }  ...]
```

#### Étape 3 : Implémentation de la fonction principale

Regardons d'abord le code :

Les tâches effectuées par cette fonction sont dans cet ordre :

1. Nous voulons avoir un dictionnaire `final_dict` afin de pouvoir l'enregistrer sous forme de fichier `.json`.
2. Ensuite, nous appelons notre fonction `get_year_with_link()`, qui retournera un dictionnaire avec les années comme clés et les liens vers la liste des organisations comme valeurs et le stockera dans `year_with_link`.
3. Nous itérons sur le dictionnaire `year_with_link`.
4. Pour chaque année, nous appelons la fonction `get_organizations_list_with_links()` avec le lien correspondant comme paramètre, qui retournera un dictionnaire avec le nom des organisations comme clés et les liens vers la page web contenant des informations à leur sujet comme valeurs. Nous stockons la valeur retournée dans `final_dict`, avec `year` comme clés.
5. Ensuite, nous itérons sur chaque organisation pour chaque année.
6. Pour chaque organisation, nous appelons la fonction `get_org_projects_info()` avec le lien de l'organisation comme paramètre, qui retournera une liste de dictionnaires contenant les informations de chaque projet.
7. Nous stockons ces données dans le `final_dict`.
8. Après la fin de la boucle, nous aurons un dictionnaire `final_dict` comme suit :

```
{    "2009": {        "Org 1": [            {                "title": "Projet - 1",                "description": "Description-Projet-1",                "link": "http://lien-projet-1.com/"            },            {                "title": "Projet - 2",                "description": "Description-Projet-2",                "link": "http://lien-projet-2.com/"            }        ],        "Org 2": [            {                "title": "Projet - 1",                "description": "Description-Projet-1",                "link": "http://lien-projet-1.com/"            },            {                "title": "Projet - 2",                "description": "Description-Projet-2",                "link": "http://lien-projet-2.com/"            }        ]    },    "2010": {        ...    }}
```

9. Ensuite, nous l'enregistrerons sous forme de fichier `json` avec `json.dumps`. ? ?

#### Prochaines Étapes

Les données pour les années 2016–2018 peuvent être extraites de manière similaire. Ensuite, Python (ou tout autre langage approprié) peut être utilisé pour analyser les données. Ou une application web peut être créée. En fait, j'ai déjà créé ma version d'une application web en utilisant _Django_, _Django REST Framework_ et _ReactJS_. **Voici le lien pour la même chose :** [https://gsoc-data-analyzer.netlify.com/](https://gsoc-data-analyzer.netlify.com/)

> Tout le code pour ce tutoriel est disponible sur mon [github](https://github.com/dojutsu-user/GSoC-Data-Analyser).

### Améliorations

Le temps d'exécution du script peut être amélioré en utilisant le multithreading. Actuellement, il récupère un lien à la fois, il peut être modifié pour récupérer plusieurs liens simultanément.

### À Propos de Moi

Bonjour.

Je suis **Vaibhav Gupta**, un étudiant en licence à l'**Indian Institute of Information Technology, Lucknow**. J'adore Python et JS.

Voir mon [portfolio](https://dojutsu-user.github.io/) ou me trouver sur [Facebook](https://www.facebook.com/vaib79), [LinkedIn](https://www.linkedin.com/in/vaibhavgupta79/) ou [Github](https://github.com/dojutsu-user).