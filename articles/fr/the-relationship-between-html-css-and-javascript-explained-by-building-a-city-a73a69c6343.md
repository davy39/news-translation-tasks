---
title: La relation entre HTML, CSS et JavaScript expliquée par la construction d'une
  ville
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-09T04:04:25.000Z'
originalURL: https://freecodecamp.org/news/the-relationship-between-html-css-and-javascript-explained-by-building-a-city-a73a69c6343
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4jvOC7UafUwx4f1xEWMQiA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: La relation entre HTML, CSS et JavaScript expliquée par la construction
  d'une ville
seo_desc: 'By Kevin Kononenko

  If you have ever visited a walkable city like New York, then you can understand
  the way that HTML, CSS and JavaScript work together.

  When you start learning web development, you can usually try a series of basic challenges
  on the p...'
---

Par Kevin Kononenko

**Si vous avez déjà visité une ville où l'on peut se déplacer à pied comme New York, alors vous pouvez comprendre la manière dont HTML, CSS** et **JavaScript fonctionnent ensemble.**

Lorsque vous commencez à apprendre le développement web, vous pouvez généralement essayer une série de défis de base sur les principes de HTML, CSS et JavaScript. Cependant, chaque défi se déroule dans un environnement isolé et ne vous teste pas sur plusieurs langages à la fois.

Par exemple, un tutoriel "Introduction à JavaScript" se concentrera généralement sur les fondamentaux comme les boucles et les instructions 'if', plutôt que sur l'utilisation de JavaScript avec HTML.

Après avoir terminé ces exercices préliminaires, vous atteignez le point où vous devez configurer votre premier site web complet. Même s'il s'agit d'un site personnel d'une seule page que vous ne prévoyez jamais de publier, vous faites toujours face à une série de nouveaux défis comme :

1. Comment connecter les trois différents types de fichiers ?
2. Une fois connectés, comment vont-ils fonctionner ensemble ?
3. Comment tester tout cela sur mon propre ordinateur ?

Après avoir réfléchi à cela pendant un moment, j'ai réalisé que ces éléments fonctionnent ensemble de la même manière que les villes peuvent encore fonctionner. Cela s'applique même lorsque les entreprises déménagent constamment ou ferment, ou que les promoteurs immobiliers transforment certains quartiers.

Alors, je vais vous montrer comment configurer votre premier environnement de développement avec ces trois éléments. Pour comprendre ce tutoriel, vous devez simplement connaître les bases de HTML, CSS et JavaScript.

Même si vous n'avez jamais écrit de code de votre vie, vous serez toujours en mesure de comprendre comment lier les trois langages.

### Les différences entre HTML, CSS et JavaScript

Imaginons que vous êtes responsable de la planification de la disposition d'un nouveau quartier dans la ville. Ce quartier comportera quelques bâtiments résidentiels, quelques restaurants, une succursale bancaire et un centre commercial.

![Image](https://cdn-media-1.freecodecamp.org/images/0*87frx07SsrDA4UZl)
_La disposition de notre quartier_

Cela peut sembler unidimensionnel. En d'autres termes, chaque bâtiment est simplement un point sur une carte, sans nuance. Mais lorsque vous creusez un peu plus, vous pouvez voir que chaque bâtiment a en réalité trois parties que vous pouvez modifier :

1. La structure du bâtiment lui-même
2. La décoration intérieure et extérieure du bâtiment
3. Les fonctions réelles que les visiteurs peuvent effectuer dans chaque bâtiment

Cela correspond aux trois différents types de fichiers que vous pouvez utiliser dans votre premier site web.

Un **fichier HTML** contient la structure de la page elle-même. C'est un peu comme la structure du bâtiment.

Un **fichier CSS** contient le style de la page. Il vous permet de changer les couleurs, le positionnement et plus encore. C'est un peu comme le design du bâtiment lui-même.

Un **fichier JavaScript** détermine les éléments dynamiques et interactifs de la page. Il détermine ce qui se passe lorsque les utilisateurs cliquent, survolent ou tapent dans certains éléments. C'est un peu comme la fonctionnalité du bâtiment.

Prenons l'exemple de l'une des maisons. Une maison a deux chambres, deux salles de bain et deux étages. C'est le HTML du bâtiment.

Elle est faite de briques et a une porte en bois massif. Cela correspond au CSS du bâtiment.

Que pouvez-vous faire dans la maison ? Vous pouvez manger, dormir, préparer des repas... tout ce que vous faites à la maison, vraiment ! C'est le JavaScript du bâtiment.

![Image](https://cdn-media-1.freecodecamp.org/images/1*3GaOb3tSGoZe4DjTZg9VXQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*5GAPClpa09DmNcCslMA23Q.png)

### Un exemple de répertoire de fichiers de base

Puisque chacun de ces trois langages sert un but différent, les développeurs web utilisent généralement des fichiers séparés pour chacun. Cette idée est appelée « [séparation des préoccupations](https://en.wikipedia.org/wiki/Separation_of_concerns) » — chaque fichier doit avoir une fonction différente au sein du site dans son ensemble.

Bien que vous puissiez techniquement inclure tout le code dans un seul fichier HTML, cela finira par conduire à un code répétitif à mesure que votre site grandit.

Examinons le code nécessaire pour créer une maison complète. Les trois fichiers doivent être dans le même **répertoire** — un dossier sur votre ordinateur. Dans ce cas, appelons le dossier _maison_. Dans notre dossier maison, nous aurons un fichier de chaque type. J'appellerai le fichier HTML principal _index_, le fichier CSS principal _styles_, et le fichier JavaScript principal _scripts_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*YZOpTO65ASByn5i29VDmRQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*18ZU8N-2YsccoCU8z9uWOw.png)

Maintenant, nous pouvons aborder la manière dont les fichiers sont liés dans le code.

Notre fichier HTML a en réalité trois sections séparées :

1. Le `<head>`, où vous pouvez inclure des métadonnées et des liens vers des services comme Google Fonts.
2. Le `<body>`, où vous incluez les éléments HTML réels.
3. Les balises `<script>`, qui peuvent lier à Google Analytics et aux fichiers JavaScript

Pour l'instant, les trois fichiers sont contenus dans un seul dossier, donc les chemins de fichiers sont assez simples dans le fichier HTML.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pOBUVpf8jG1SMvlv7R4E9g.png)

La balise `<link>` vous permettra de créer une feuille de style séparée à utiliser avec toutes les maisons en briques en utilisant le fichier _styles.css_.

Et la balise `<script>` vous permet de créer un ensemble de fonctions qui s'appliqueraient à tout type de maison dans le fichier _scripts.js_.

### Scénario 1 : une nouvelle chaîne de pizzerias s'installe (changement de fichier CSS)

Examinons un exemple concret. Imaginez que dans ce quartier, l'un des bâtiments est une pizzeria appelée Neighborhood Pizza (super nom). Mais Neighborhood Pizza a du mal à survivre, et Domino's (une énorme chaîne de pizzerias) décide d'acheter la propriété et de servir le quartier à la place.

![Image](https://cdn-media-1.freecodecamp.org/images/0*HM67ZGkZ913HLLqu)

Savez-vous ce que cela signifierait en termes de code ?

Eh bien, réfléchissons à chacun des trois éléments.

1. La structure du bâtiment est la même. C'est toujours la même pizzeria. C'est le HTML.
2. La fonctionnalité du bâtiment est la même. Il existe toujours pour servir des pizzas, et lorsque les clients entrent, c'est la seule chose qu'ils attendent. C'est le JavaScript.
3. Mais le style et la marque du bâtiment sont différents ! Cela signifie que le CSS est nouveau.

Nous avons donc maintenant créé un nouveau fichier CSS (appelons-le _Dominos.css_). Nous devons créer un dossier appelé _pizza_ pour montrer que nous parlons maintenant d'une pizzeria, et substituer _dominos.css_ à l'ancien fichier _styles.css_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Cbrhmfv7aXM-LkfrfL2JUQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*1YOCfrsFIWq-bJRYioaaFQ.png)

### Scénario 2 : un nouveau bâtiment d'appartements

Voici un autre exemple. Supposons que votre quartier subit une certaine [gentrification](https://en.wikipedia.org/wiki/Gentrification). Cela signifie que des résidents plus riches emménagent et que des logements plus chers sont construits. Certains promoteurs immobiliers décident d'acheter un terrain avec une maison dessus, de démolir la maison et d'y construire des appartements luxueux.

![Image](https://cdn-media-1.freecodecamp.org/images/0*_PA4fk1-hIzyQRc2)

Réfléchissons à ce que cela signifierait en termes de notre système de fichiers.

1. La fonctionnalité est la même. C'est toujours un logement. Cela signifie que JavaScript est le même.
2. Le CSS doit être différent car il n'y a aucun moyen qu'un bâtiment d'appartements puisse être stylisé de la même manière qu'une maison !
3. Et le fichier HTML doit être différent, car les deux bâtiments ont des structures complètement différentes.

Appelons le nouveau bâtiment _appartement.html_, et le nouveau CSS sera _fancy.css_. Puisque nous avons un fichier HTML entièrement nouveau, nous ne nous contentons pas de lier un nouveau fichier CSS. La page entière est différente. Et elle lie également à un nouveau fichier CSS.

![Image](https://cdn-media-1.freecodecamp.org/images/1*T8leHgkgP-X8L_wcsM2kCQ.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*aKoiZBHRCzjLCPp6weEwWA.png)

Les fichiers CSS et JavaScript modifient simplement le HTML. Ils doivent être référencés dans le fichier HTML pour être chargés. C'est pourquoi, dans le diagramme ci-dessus, le dossier lui-même est le même. Mais le fichier HTML et le code qui le lie aux autres fichiers sont différents.

### Création d'un répertoire de fichiers avec plusieurs dossiers

Jusqu'à présent, nous avons couvert un seul type de bâtiment à la fois. Mais c'est un peu comme un site web avec une seule page — très inhabituel. Même un site personnel pourrait avoir une page "À propos", une page "Portfolio", et ainsi de suite. Alors, que se passe-t-il lorsqu'il y a plusieurs bâtiments ? Comment pouvez-vous structurer votre répertoire de fichiers ?

Supposons que votre quartier a une banque, un centre commercial et une pizzeria. C'est un peu comme un site web avec trois pages. Chacune est un fichier HTML avec un fichier CSS et un fichier JavaScript liés à celui-ci.

![Image](https://cdn-media-1.freecodecamp.org/images/1*nXl1p_RnKNh3_iOD7fPXhw.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*tUpDr4vgMsncf2XgHRv5Yg.jpeg)

Mais, remarquez comment nous n'avons pas utilisé trois sous-dossiers dans un dossier de quartier plus grand ! Bien que nous aurions certainement pu le faire, de nombreux développeurs front-end aiment créer un dossier _scripts_ séparé pour tous les fichiers JS, et un dossier _styles_ pour tous les fichiers CSS.

À mesure que votre site grandit, vous constaterez que certaines parties de CSS et de JavaScript sont réutilisables et peuvent être liées à plusieurs fichiers HTML. Les dossiers scripts et styles vous permettent d'organiser vos efforts et de réduire le code redondant.

Dans notre exemple, vous pouvez commander une part de pizza grasse à la fois dans un centre commercial ET dans une pizzeria. Vous pourriez donc vous attendre à ce que les deux partagent un fichier JavaScript, mais aient également des fonctionnalités uniques dans leurs propres fichiers JavaScript individuels.

En tout cas, voici une disposition potentielle de l'ensemble du répertoire de fichiers.

![Image](https://cdn-media-1.freecodecamp.org/images/0*6ADmIY53-wQGVP9M)

Remarquez comment les fichiers HTML et les dossiers sont au même niveau de profondeur dans le dossier _quartier_ plus grand. Pour référencer des fichiers qui se trouvent dans des dossiers au même niveau, vous devez commencer votre chemin de fichier par le nom du dossier au lieu d'un nom de fichier. Donc, si vous vouliez référencer le fichier _bank.css_ depuis bank.html, vous utiliseriez `scripts/bank.css` comme chemin de fichier.

### Obtenez les derniers tutoriels

Avez-vous apprécié ce tutoriel ? Donnez-lui un "clap" et faites-le-moi savoir dans les commentaires. Ou, obtenez mes dernières explications sur le développement web en vous inscrivant à ma newsletter :