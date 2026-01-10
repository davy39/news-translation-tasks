---
title: Apprenez EmotionJS pendant votre café du matin — c'est aussi simple que ça.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-21T16:50:32.000Z'
originalURL: https://freecodecamp.org/news/learn-emotionjs-during-your-morning-coffee-its-that-easy-2bc60213aca7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*V-DbP3ZYLJwyoxRneLdoog.png
tags:
- name: CSS
  slug: css
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: Apprenez EmotionJS pendant votre café du matin — c'est aussi simple que
  ça.
seo_desc: 'By shahar taite

  EmotionJS is a CSS-in-JavaScript library with incredible capabilities. Let’s see
  how the world of CSS evolved to this solution, and then deep dive into what you
  can do with it today.

  The CSS wars (a recap)

  In the last couple of years,...'
---

Par shahar taite

EmotionJS est une bibliothèque CSS-in-JavaScript avec des capacités incroyables. Voyons comment le monde du CSS a évolué vers cette solution, puis plongeons-nous dans ce que vous pouvez faire avec aujourd'hui.

#### Les guerres du CSS (un récapitulatif)

Au cours des dernières années, nous avons vu une transition vers différentes méthodes de stylisation, toutes basées sur le CSS. Voici l'essentiel dans l'ordre chronologique :

#### **Le bon vieux CSS**

C'est la méthode classique et simple d'application du CSS. Nous référençons un fichier CSS dans notre index.html et il est appliqué à nos fichiers HTML par les règles classiques du CSS.

Cette approche pose des problèmes lorsqu'elle est appliquée à grande échelle, car le CSS est basé sur la spécificité, qui doit être gérée avec soin si nous voulons éviter les collisions CSS.

Il est également difficile de déboguer lors de l'inspection dans le navigateur. Il est difficile de comprendre quelle combinaison de propriétés CSS a fini par influencer le style que nous voyons sur une balise HTML.

#### **Préprocesseurs CSS**

Le bon vieux CSS avait certaines limitations, donnant naissance à des extensions de CSS telles que Less et Sass. Ces extensions de langage nous permettent d'écrire dans un langage avec des capacités plus fortes. Les exemples incluent la nesting des sélecteurs CSS, les fonctions, et plus encore. Notre outil de build compile ces fichiers en fichiers CSS simples et ils sont appliqués de manière ordinaire.

#### **Modules CSS**

Cette approche a été introduite une fois que le développement web a commencé à traiter les pages web comme des arbres de composants. CSS-modules consiste à styliser un composant de manière indépendante, sans affecter d'autres parties de l'UI et sans être affecté par elles.

Après avoir introduit CSS-modules dans notre projet, chaque composant référence un fichier CSS avec du CSS ordinaire ou préprocessé. Pendant le processus de build, notre système de build (tel que webpack) prend chaque classe CSS, la préfixe avec le nom du composant et la suffixe avec un identifiant unique afin que la classe soit unique.

Cette approche est excellente car il est très facile d'atteindre l'isolation CSS. De plus, il est facile de comprendre quelles règles CSS ont été appliquées à nos éléments HTML et d'où elles proviennent. J'ai été un grand défenseur de cette approche — jusqu'à la sortie d'EmotionJS.

#### **CSS-in-JS**

Cette approche remet en question la pratique d'isoler le CSS dans des fichiers CSS. Elle nous permet de déclarer nos règles CSS dans notre code JavaScript sous forme d'objets JS.

Certains frameworks comme React ont un support intégré pour cette méthode. Plusieurs bibliothèques ont émergé du besoin de fournir une solution plus isolée et évolutive. Les principales bibliothèques sont Styled Components et EmotionJS.

Développons cela.

### Styled Components versus EmotionJS !

Styled Components est arrivé en premier, et EmotionJS a été clairement fortement influencé par celui-ci.

Les Styled Components sont des composants React simples et petits. Ils définissent une balise HTML et ses styles en fonction des props du composant.

Cela isole la sémantique HTML et CSS de nos composants React plus fonctionnels. Cela fournit à son tour une expérience de développement plus lisible et maintenable.

Exemple de Styled Components :

Ce que nous voyons ici est un bouton HTML avec quelques props CSS.

Les propriétés CSS `color` et `background` sont déterminées en fonction d'une prop `primary` qui est passée (ou non) au composant.

Remarquez comment le JSX est très simple et sémantique, et comment la partie CSS et HTML est isolée dans le composant stylisé.

Maintenant, regardons EmotionJS.

![Image](https://cdn-media-1.freecodecamp.org/images/1*p236DRigU2r56RfNuPhzuQ.png)

EmotionJS prend la puissance des styled components et ajoute quelques fonctionnalités utiles supplémentaires (ainsi que le logo le plus cool jamais).

Démontrons les choses que j'ai trouvées les plus impressionnantes avec EmotionJS.

Une chose que je détestais jusqu'à présent était la maintenance des [CSS media queries](https://www.w3schools.com/css/css_rwd_mediaqueries.asp).

Les règles CSS pour chaque breakpoint résidaient dans différentes zones des fichiers CSS. Il était difficile de voir et de gérer les propriétés qui se chevauchaient.

Dans EmotionJS, nous pouvons créer une constante contenant les largeurs de nos breakpoints avec l'aide de la bibliothèque Facepaint.

Nous pouvons ensuite référencer cette constante, déclarant les valeurs d'une propriété CSS pour chaque breakpoint en un seul endroit.

Décomposons cet exemple :

* Lignes 4-9 : nous définissons les largeurs de nos breakpoints, en un seul endroit dans notre application
* Lignes 13-23 : nous définissons un composant Button qui est une balise div avec quelques propriétés CSS. Ses valeurs `width` et `height` sont définies sous forme de tableau de valeurs, une pour chaque breakpoint. Remarquez comment nous n'avons pas besoin de spécifier les unités `px`. Elles sont ajoutées automatiquement. Remarquez également la propriété `background-color` qui dépend de la prop `primary` fournie au composant Button. Cela est similaire à l'exemple des Styled components.
* Lignes 26-33 : dans notre composant React, nous référençons notre bouton EmotionJS et l'utilisons comme une balise JSX

#### Autres fonctionnalités d'EmotionJS

EmotionJS offre d'autres moyens d'atteindre certaines de ces capacités :

* La prop CSS — nous pouvons fournir à nos composants React une prop CSS qui est un objet JavaScript ou une chaîne définissant nos propriétés CSS.

* Les media queries peuvent également être ciblées avec l'approche de la prop CSS

### Pour conclure : le bon, le mauvais et l'émotionnel

![Image](https://cdn-media-1.freecodecamp.org/images/0*npYL5O9g1fbrRj6p.jpg)

**Avantages :**

* Facile à intégrer et à remplacer d'autres solutions CSS.
* Facile à identifier et à supprimer le code mort par rapport à d'autres solutions.
* Plus facile à travailler avec les media queries, les valeurs sont rassemblées.
* Les composants React deviennent plus sémantiques car le HTML et le CSS sont isolés.

**Inconvénients :**

* Avec les CSS-modules, il est facile de comprendre exactement d'où vient la règle CSS lors de l'inspection dans le navigateur. Cela est dû au fait que les noms de classe sont générés avec des préfixes de nom de composant React. Avec EmotionJS, cela ne se produit pas.
* Si nous définissons une propriété CSS pour une media query, nous devons la définir pour les autres également, car nous fournissons un tableau de valeurs. Dans de nombreux cas, nous voulons simplement adresser une ou deux media queries et laisser les autres avec la valeur par défaut.

### Le verdict

EmotionJS est la prochaine étape dans la bonne direction, traitant les pièges du CSS. Il fournit un environnement isolé et maintenable, gardant la logique de nos composants principaux centrée et sémantique.

Il m'a littéralement fallu dix minutes pour l'apprendre et l'intégrer, et c'est une amélioration majeure dans ce domaine.

N'oubliez pas d'applaudir si vous avez aimé cela, et suivez-moi sur Twitter : [https://twitter.com/shahar_taite](https://twitter.com/shahar_taite)