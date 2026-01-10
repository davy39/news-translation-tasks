---
title: Un guide pratique pour fetch(), reduce() et la mise en forme des données d'une
  API externe
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-05-15T00:54:04.000Z'
originalURL: https://freecodecamp.org/news/a-practical-guide-to-fetch-reduce-and-formatting-data-from-an-external-api-283ddd9bfdcb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*nROAmzDLiFCLQ9z7pMx8Wg.jpeg
tags:
- name: api
  slug: api
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Un guide pratique pour fetch(), reduce() et la mise en forme des données
  d'une API externe
seo_desc: 'By JS

  JavaScript has built-in methods that make it easy to get and manipulate data from
  an external API. I’ll walk through a practical example from one of my current projects
  that you can use as a template when starting something of your own.

  For thi...'
---

Par JS

JavaScript dispose de méthodes intégrées qui facilitent l'obtention et la manipulation de données provenant d'une API externe. Je vais vous guider à travers un exemple pratique issu de l'un de mes projets actuels, que vous pourrez utiliser comme modèle pour démarrer quelque chose de votre propre initiative.

Pour cet exercice, nous allons examiner les données actuelles des offres d'emploi pour les agences de la ville de New York. La ville de New York est excellente pour publier [toutes sortes de jeux de données](https://opendata.cityofnewyork.us/), mais j'ai choisi celui-ci en particulier parce qu'il ne nécessite pas de gérer des clés API — l'endpoint est une URL publique accessible.

Tout d'abord, nous allons obtenir les données des serveurs de la ville de New York en utilisant l'API Fetch de JavaScript. C'est une bonne façon de commencer à travailler avec les [promesses](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise). Je vais passer en revue les bases les plus élémentaires ici, mais je recommande l'excellent blog illustré de Mariko Kosaka [_The Promise of a Burger Party_](http://kosamari.com/notes/the-promise-of-a-burger-party) pour une introduction plus approfondie (et délicieuse).

Si vous avez déjà utilisé `$.getJSON()` dans jQuery, vous êtes presque là conceptuellement. Jetez un coup d'œil au code ci-dessous :

```
const cityJobsData = fetch('https://data.cityofnewyork.us/resource/swhp-yxa4.json');
```

Nous déclarons une variable, `cityJobsData`, et définissons sa valeur sur `fetch(l'URL qui contient les données que nous voulons)` qui retourne ce qu'on appelle une promesse. Pour l'instant, pensez simplement à une promesse comme les données que nous obtiendrons *éventuellement* de l'URL lorsque la requête sera terminée. Nous pouvons accéder et manipuler ces données une fois qu'elles sont chargées en appelant ensuite `then()` sur `cityJobsData`. Pour effectuer plusieurs opérations, nous pouvons continuer à enchaîner `then()` ensemble, en veillant à 1) toujours passer nos données en tant qu'argument à la fonction de rappel, et 2) retourner une valeur.

```
const cityJobsData = fetch('https://data.cityofnewyork.us/resource/swhp-yxa4.json');
```

```
cityJobsData.then(data => data.json())
```

Dans l'extrait ci-dessus, nous disons à l'ordinateur d'exécuter tout ce qui est contenu dans `then()` *une fois les données récupérées de l'URL*. C'est ce qu'on appelle du code 'asynchrone'. Dans ce cas, `.then(data => data.json())` retourne les données au format JSON, ce qui nous permettra de les manipuler.

Une petite parenthèse pour gérer de grandes quantités de JSON : Si vous allez dans votre navigateur web à l'[URL qui contient les données que nous voulons](https://data.cityofnewyork.us/resource/swhp-yxa4.json), vous verrez un énorme bloc de texte non formaté qui est très difficile à lire. Cependant, vous pouvez copier et coller ce texte dans quelque chose comme [jsonviewer.stack.hu](http://jsonviewer.stack.hu/). Il vous montrera une vue organisée et hiérarchique du contenu.

Supposons que nous voulons voir combien il y a d'offres pour chaque agence de la ville. Si nous regardons notre schéma JSON dans ce visualiseur, nous pouvons voir qu'il s'agit d'un tableau d'objets. Chaque objet contient toutes les données qui composent une seule offre d'emploi.

![Image](https://cdn-media-1.freecodecamp.org/images/1*RoXGqr-4JSiGhkfeZvMa0w.png)
_capture d'écran du JSON formaté de jsonviewer.stack.hu_

Notez que chaque objet contient une clé, `agency`, dont la valeur est le nom de l'agence de la ville qui a un emploi disponible.

Par conséquent, si nous pouvons d'une manière ou d'une autre suivre le nombre de fois que chaque agence est mentionnée dans ce tableau d'objets, nous pourrons savoir combien d'emplois sont actuellement disponibles par agence.

Une façon de compter les emplois par agence est d'utiliser `reduce()`. [D'après MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce?v=example), « La méthode `reduce()` applique une fonction contre un accumulateur et chaque élément du tableau (de gauche à droite) pour le réduire à une seule valeur. » Si cela vous semble être un charabia, ne vous inquiétez pas ! C'est plus clair avec un exemple.

La plupart des introductions à `reduce()` impliquent une simple addition, ce qui est un bon point de départ. Passons en revue cet exemple ensemble :

```
const arr = [1, 2, 4, 6];
const added = arr.reduce((accumulator, item) => { return accumulator + item; }, 0);
```

```
console.log(added); // 13
```

Voici comment cela fonctionne : la fonction `reduce()` parcourt le tableau, `arr`, et ajoute chaque `item` à un accumulateur. L'accumulateur a une valeur initiale de `0` qui est définie avec le deuxième argument de `reduce()`, après la fonction de rappel. La valeur actuelle de l'accumulateur est retournée à la fin de chaque boucle, ce qui est ainsi que l'addition se produit. Ainsi, la valeur finale de `added` est 13.

Si vous avez du mal à visualiser cela, essayez d'ajouter une instruction `console.log()` avant votre retour qui affiche les valeurs actuelles de l'accumulateur et de l'élément. De cette façon, vous pourrez voir la boucle qui se produit en arrière-plan. Voici un ensemble d'instructions de journalisation pour l'exemple ci-dessus :

```
adding 1 to accumulator: 0
adding 2 to accumulator: 1
adding 4 to accumulator: 3
adding 6 to accumulator: 7
```

C'est bien et c'est amusant de faire un peu d'addition avec *~`*functional programming*`~*, mais saviez-vous que `reduce()` peut faire plus que simplement compter des choses ? Et que l'accumulateur peut être autre chose qu'un nombre ?

Vous pouvez faire toutes sortes de choses cool avec `reduce()` — c'est comme un couteau suisse. Dans notre cas, nous allons l'utiliser pour découvrir combien il y a d'offres d'emploi actuelles par agence de la ville de New York. Cela peut sembler un grand pas en avant par rapport à la simple addition de nombres, mais les concepts de base de la boucle et de l'accumulation sont les mêmes.

Cette fois, au lieu de réduire un tableau de quatre nombres, nous voulons réduire notre blob JSON de données d'offres d'emploi. Et au lieu de réduire à un seul nombre, nous allons réduire à un seul _objet_. Oui, un objet ! Une fois la fonction terminée, les clés de l'objet accumulateur seront les noms des agences de la ville et les valeurs des clés seront le nombre d'offres qu'elles ont, comme ceci : `{"nom de l'agence": nombre d'offres d'emploi}`. Voici le programme complet :

Comment cela fonctionne-t-il exactement ? Décomposons-le. À chaque tour de boucle, nous examinons une `value` spécifique, c'est-à-dire un objet dans `data`, notre tableau d'objets mentionné précédemment. Nous vérifions si une clé avec le nom de l'agence actuelle (`value.agency`) existe déjà dans notre objet accumulateur. Si ce n'est pas le cas, nous l'ajoutons à l'objet accumulateur et définissons sa valeur à 1. Si une clé avec le nom de l'agence actuelle *existe déjà dans l'objet accumulateur*, nous ajoutons 1 à sa valeur existante. Nous retournons l'objet accumulateur lorsque nous avons terminé et obtenons cet ensemble de données :

```
{ 'FIRE DEPARTMENT': 17,  'DEPT OF ENVIRONMENT PROTECTION': 134,  'DEPARTMENT OF INVESTIGATION': 22,  'DEPARTMENT OF SANITATION': 14,  'DEPT OF HEALTH/MENTAL HYGIENE': 247,  'OFFICE OF THE COMPTROLLER': 14,  'ADMIN FOR CHILDREN\'S SVCS': 43,  'DEPT OF DESIGN & CONSTRUCTION': 48,  'ADMIN TRIALS AND HEARINGS': 16,  'DEPT OF PARKS & RECREATION': 34,  'HUMAN RIGHTS COMMISSION': 4,  'POLICE DEPARTMENT': 36,  'DEPT OF INFO TECH & TELECOMM': 50,  'DISTRICT ATTORNEY KINGS COUNTY': 4,  'TAXI & LIMOUSINE COMMISSION': 11,  'HOUSING PRESERVATION & DVLPMNT': 21,  'DEPARTMENT OF BUSINESS SERV.': 18,  'HRA/DEPT OF SOCIAL SERVICES': 31,  'DEPARTMENT OF PROBATION': 3,  'TAX COMMISSION': 4,  'NYC EMPLOYEES RETIREMENT SYS': 6,  'OFFICE OF COLLECTIVE BARGAININ': 2,  'DEPARTMENT OF BUILDINGS': 9,  'DEPARTMENT OF FINANCE': 29,  'LAW DEPARTMENT': 21,  'DEPARTMENT OF CORRECTION': 12,  'DEPARTMENT OF TRANSPORTATION': 67,  'DEPT OF YOUTH & COMM DEV SRVS': 5,  'FINANCIAL INFO SVCS AGENCY': 7,  'CULTURAL AFFAIRS': 1,  'OFFICE OF EMERGENCY MANAGEMENT': 12,  'DEPARTMENT OF CITY PLANNING': 5,  'DEPT OF CITYWIDE ADMIN SVCS': 15,  'DEPT. OF HOMELESS SERVICES': 3,  'DEPARTMENT FOR THE AGING': 2,  'CONSUMER AFFAIRS': 7,  'MAYORS OFFICE OF CONTRACT SVCS': 7,  'DISTRICT ATTORNEY RICHMOND COU': 3,  'NYC HOUSING AUTHORITY': 9,  'CIVILIAN COMPLAINT REVIEW BD': 5,  'OFF OF PAYROLL ADMINISTRATION': 1,  'EQUAL EMPLOY PRACTICES COMM': 1 }
```

_Et voilà_ ! Nous savons maintenant que si nous voulons travailler pour le gouvernement de la ville de New York, nous devrions consulter les 247 offres du Département de la Santé et de l'Hygiène Mentale !

Nous pouvons faire un tas de choses utiles avec ces données — personnellement, je veux me lancer dans la visualisation de données, alors je vais les utiliser pour créer un simple graphique. J'espère que vous pourrez utiliser cet exemple comme point de départ pour vos propres projets.

Si vous avez aimé cet article, n'hésitez pas à me contacter sur [Twitter](http://twitter.com/j_speda) !

Merci à [Jim O'Brien](http://twitter.com/jimcodes) pour l'édition.