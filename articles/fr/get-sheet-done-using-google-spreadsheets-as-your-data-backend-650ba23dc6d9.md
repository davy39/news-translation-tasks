---
title: Get Sheet Done — utiliser Google Spreadsheets comme backend de données
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-21T16:03:16.000Z'
originalURL: https://freecodecamp.org/news/get-sheet-done-using-google-spreadsheets-as-your-data-backend-650ba23dc6d9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ulO04x_24taM1kWjlBHW7w.jpeg
tags:
- name: Productivity
  slug: productivity
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Get Sheet Done — utiliser Google Spreadsheets comme backend de données
seo_desc: 'By Gilad Dayagi

  If you want to rapidly prototype your next web apps, try using Google Spreadsheets
  as your data backend.

  With a small library I created called get-sheet-done, you can have a free cloud
  database with GUI editor up and running in less t...'
---

Par Gilad Dayagi

Si vous souhaitez rapidement prototyper vos prochaines applications web, essayez d'utiliser Google Spreadsheets comme backend de données.

Avec une petite bibliothèque que j'ai créée appelée [get-sheet-done](https://www.npmjs.com/package/get-sheet-done), vous pouvez avoir une base de données cloud gratuite avec un éditeur GUI opérationnelle en moins de 5 minutes.

### L'histoire derrière Get Sheet Done

Il y a quelque temps, j'avais besoin de prototyper rapidement une application web capable d'afficher des données structurées. Le problème était que ces données devaient être fréquemment éditées par une personne non technique.

Étant donné que c'était un prototype, je cherchais une solution qui me donnerait le meilleur rapport qualité-prix, en tenant compte du temps de développement et des coûts de maintenance.

J'ai considéré plusieurs solutions, y compris l'utilisation d'une approche complète de backend-as-a-service qui stockait les données sous forme de fichier dans Dropbox. J'ai ensuite choisi une solution quelque peu non orthodoxe : j'ai stocké les données dans une feuille de calcul Google.

### Quand une base de données basée sur une feuille de calcul est-elle une solution appropriée ?

Utiliser Google Spreadsheets comme base de données pour des applications web n'est pas une solution grand public, et elle peut ou non convenir à votre prochain projet.

Pour vous aider à décider si c'est une bonne option, j'ai dressé la liste suivante de considérations.

Rappel : nous parlons d'une feuille de calcul, qui fonctionne très bien pour des données structurées et tabulaires. Mais qui ne fonctionne pas bien pour un stockage de documents/objets.

Autrement que cela, voici quelques avantages et inconvénients à considérer :

#### Avantages

* C'est gratuit
* Très facile à installer — pas besoin de clés API ou de SDK compliqués
* Zéro maintenance
* Vous obtenez un éditeur de données GUI gratuitement
* Vous obtenez une gestion des accès en écriture gratuitement
* Peut inclure des calculs internes en utilisant des fonctions de feuille de calcul
* L'application qui utilise les données peut être facilement mise à niveau dans une phase ultérieure pour utiliser une vraie base de données, car les données sont exposées sous forme de JSON standard
* Un certain niveau d'automatisation peut être atteint en utilisant apps-scripts en combinaison avec des [déclencheurs basés sur le temps](https://developers.google.com/apps-script/guides/sheets#triggers)
* Il peut être combiné avec Google Forms pour la collecte de données

#### Inconvénients

* Pas de logique de filtrage côté serveur à mentionner
* Toutes les données que vous souhaitez accéder doivent être publiquement accessibles
* L'ensemble de la base de données est modifiable manuellement, donc une erreur humaine peut casser l'application. Par exemple, si quelqu'un change accidentellement l'étiquette d'un champ, il ne sera plus disponible pour l'application.  
Cela peut être partiellement remédié en protégeant les cellules critiques
* Vous pouvez avoir [jusqu'à 2 millions de cellules](https://support.google.com/drive/answer/37603?hl=en) dans une feuille de calcul

### Comment j'ai implémenté cela

Je n'ai pas trouvé beaucoup d'informations ni de bonnes bibliothèques pour lire facilement des données depuis une feuille de calcul Google. J'ai donc décidé de créer ma propre solution. Elle est maintenant disponible sur npm sous le nom de [get-sheet-done package](https://www.npmjs.com/package/get-sheet-done).

Mon implémentation est basée sur le fait qu'une fois qu'une feuille de calcul est publiée sur le web, elle est également disponible sous forme de flux RSS standard, qui peut être récupéré et analysé.

Une complication est que vous devez le récupérer en utilisant JSONP ou gérer CORS d'une manière ou d'une autre. J'ai choisi d'utiliser JSONP et la bibliothèque [fetch-jsonp](https://www.npmjs.com/package/fetch-jsonp) pour gérer cela, donc il n'y a pas besoin de mesures spéciales.

### Comment l'utiliser

Voici ce que vous devez faire pour obtenir une base de données éditable simple pour votre application web :

1. Créez une feuille de calcul Google avec des données
2. Publiez la feuille sur le web : `Fichier -> Publier sur le` web.  
Notez l'ID du document depuis l'URL
3. Installez le package : `npm install --save get-sheet-done`
4. Obtenez les données :

```
import GetSheetDone from 'get-sheet-done'
```

```
GetSheetDone.labeledCols(DOCUMENT_ID).then(sheet => console.log(sheet))
```

5. Profitez-en !

Notez qu'il y a trois fonctions que vous pouvez utiliser pour récupérer les données, selon la manière dont elles doivent être analysées : tableau 2D brut, tableau d'objets, objet d'objets.

Voici une [démo en direct](https://giladaya.github.io/get-sheet-done/) avec laquelle vous pouvez jouer.

Il vaut la peine de considérer l'utilisation de Google Spreadsheets comme source de données pour une application web, surtout si vous construisez simplement un prototype rapide. Cela présente certains avantages uniques, et l'implémentation est facile avec (ou sans) ma bibliothèque.

Faites-moi savoir dans les commentaires si vous avez trouvé cette bibliothèque utile et s'il manque des fonctionnalités.