---
title: Qu'est-ce qu'une boucle JavaScript ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-07T20:33:22.000Z'
originalURL: https://freecodecamp.org/news/what-in-the-world-is-a-javascript-loop-for
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/joanna-kosinska-1_CMoFsPfso-unsplash.jpg
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: JavaScript
  slug: javascript
- name: Loops
  slug: loops
seo_title: Qu'est-ce qu'une boucle JavaScript ?
seo_desc: 'By Syk Houdeib

  This article is a beginner''s introduction to JavaScript loops. We''ll go over why
  we need them, and how they fit into the front-end context. It’s a bird''s eye view
  of accessing data and doing things to it, covering fundamental every-day...'
---

Par Syk Houdeib

Cet article est une introduction aux boucles JavaScript pour les débutants. Nous allons voir pourquoi nous en avons besoin et comment elles s'intègrent dans le contexte front-end. C'est une vue d'ensemble de l'accès aux données et de leur manipulation, couvrant des concepts fondamentaux pour un développeur front-end.

## Introduction.

_Donc, nous prenons ce tableau, nous itérons dessus, nous traitons les données et hop !_  
Lorsque j'ai commencé à apprendre à programmer, des phrases comme celle-ci ressemblaient à des incantations mystiques. Une langue qui ressemble à l'anglais mais qui était au-delà de ma compréhension. Venant d'un milieu non technique, je ne pouvais pas comprendre où une boucle s'insérait dans ce que je voulais faire. Et pourquoi exactement j'en avais besoin.

Aujourd'hui, en tant que développeur front-end, j'utilise une boucle pour une chose ou une autre tout le temps. Mais je n'ai pas oublié à quel point tout cela était mystérieux. Mon objectif ici est de donner un aperçu de haut niveau conçu pour les personnes qui n'ont pas de formation technique. Nous allons au-delà de la syntaxe et nous concentrons plutôt sur un contexte réel de pourquoi nous utilisons des boucles et comment tout cela s'emboîte.

Dans cet article, nous allons parler de la façon dont nous accédons aux données et ensuite de la façon dont nous les manipulons avec des **boucles**. Plus important encore, nous allons essayer de répondre à **pourquoi** nous devons faire cela. Et **comment cela est pertinent** pour vous dans la construction de sites web et d'applications web.

Il y aura aussi un exemple **pratique** pour débutants. Vous pouvez le suivre pour pratiquer les concepts et les voir en action par vous-même.

### L'installation

Imaginons que nous travaillons sur une plateforme en ligne qui nous permet de faire nos courses de supermarché depuis un site web. C'est une application réelle des choses dont nous voulons parler ici.

Jetez un coup d'œil à [Lola Market](https://lolamarket.com/tienda), où je travaille, pour un exemple de ce à quoi cela pourrait ressembler.

Supposons que nous avons une série de produits stockés dans notre base de données. Notre tâche est de prendre ceux-ci et de les afficher sur le site web sous forme de liste. C'est une tâche simple qui imite les choses que nous faisons tous les jours en front-end.

## Boucles

Pour parler des boucles, nous allons travailler avec des tableaux. Si vous souhaitez un rappel sur ce qu'est un tableau et pourquoi nous en avons besoin, vous pouvez consulter mon article à ce sujet qui s'articule bien avec celui-ci.

[https://www.freecodecamp.org/news/what-in-the-world-is-a-javascript-array/](https://www.freecodecamp.org/news/what-in-the-world-is-a-javascript-array/)

En bref, nous avons pris une série de produits qui sont dans notre base de données. Nous les avons emballés dans un tableau et avons fait une demande pour les amener dans notre code front-end. Et voici à quoi ressemble ce tableau.

```js
['champignons', 'steak', 'poisson', 'aubergines', 'lentilles']
```

Une fois que nous avons le tableau de produits, c'est là que les boucles entrent en jeu. Simplement dit, une boucle est un moyen de prendre notre tableau, de l'ouvrir et de prendre un élément. De nous le donner pour que nous fassions ce que nous voulons avec. Puis de répéter avec l'élément suivant jusqu'à la fin du tableau.

Nous utilisons une boucle lorsque nous devons répéter le même code pour chacun des éléments de nos données.

### Prêt

Ce que nous voulons faire, c'est afficher cette liste de produits sur le site web. Imaginez cela comme ceci. La plupart des sites web seraient plus complexes, nous l'espérons. Mais ce n'est que notre première étape.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/products-list-2.png)
_Liste de produits_

Pour garder l'exemple simple et accessible aux débutants, nous allons utiliser les **outils de développement** pour faire tout le travail. Cela ne nécessite aucune installation autre que l'ouverture des outils de développement de votre navigateur.

Nous devons prendre en compte quelques éléments.

* Nous ne ferons pas d'appel à la base de données pour obtenir notre liste de produits. Au lieu de cela, nous taperons un tableau à la main et l'utiliserons directement dans notre code front-end.
* Nous n'afficherons pas la liste de produits sur un site web. Au lieu de cela, nous allons simplement journaliser la liste dans la console des outils de développement.
* Dans le monde réel, nous n'utiliserions pas les instructions `console.log()` que vous voyez ici. À la place, la logique dont nous avons besoin pour afficher notre liste sur le site web serait à sa place.

OK, nous sommes prêts. Allons-y.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-215.png)
_Photo par [Unsplash](https://unsplash.com/@vandateixeira?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Vanda Teixeira</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

### Pour chaque produit

Tout d'abord, prenons notre boucle et stockons-la dans une **variable**. Cela permet de la lire et de travailler avec plus facilement.

```js
const products = ['champignons', 'steak', 'poisson', 'aubergines', 'lentilles']
```

Maintenant, chaque fois que nous utilisons `products`, nous faisons en réalité référence à notre tableau. C'est très pratique car notre tableau pourrait facilement contenir des centaines de produits.

Alors, passons au plat principal, laissez-moi vous présenter la boucle `forEach()`. Et voici à quoi elle ressemble en action :

```js
products.forEach( product => {
	// faire des choses
})
```

Nous allons décomposer cela pièce par pièce maintenant. Pour commencer, convertissons ce snippet de code en **anglais simple**. Cela se lit littéralement : Prenez le tableau des produits. Pour chaque élément de ce tableau, prenez cet élément, appelez-le `product` et _faites des choses_ avec.

Examinons cela de plus près.

```js
TABLEAU  BOUCLE  COURANT FONCTION
products.forEach( product => {
	// faire des choses
})
```

* `products` : C'est notre **tableau** qui contient les données.
* `.forEach()` : C'est notre méthode de tableau, la **boucle**.
* `product` : C'est l'élément **actuellement sélectionné**. C'est l'élément du tableau que notre boucle a pris et nous a donné pour travailler avec.
* `=> { }` : C'est une déclaration de **fonction**, une fonction fléchée pour être précis. Elle dit grossièrement exécuter le code suivant.
* `// faire des choses` : C'est là que le code réel va. Faire des choses pour chacun des éléments du tableau.

Il est important de se souvenir de deux choses ici concernant l'élément actuellement sélectionné. Premièrement, que `product` est un nom de variable. Le nom lui-même est à nous de décider, nous aurions pu l'appeler `food` ou `x` ou autre chose. Cependant, si nous traitons avec un tableau de `products`, il est d'usage d'utiliser le singulier pour un élément individuel de ce tableau : `product`. Si c'était un tableau de `animals`, alors nous l'appellerions `animal`.

Deuxièmement, `product` change à chaque tour que la boucle fait. Chaque fois que la boucle prend un élément, `product` devient ce nouvel élément actuellement sélectionné.

En gros, la boucle commence par prendre le premier élément du tableau, champignons dans ce cas. `product` fait maintenant référence à champignon. La boucle exécute ensuite la fonction et exécute le code qui s'y trouve. Une fois terminé, elle retourne au tableau et prend l'élément suivant. `product` n'est plus champignons, c'est steak maintenant. Une fois de plus, le code s'exécute. Et cela se répète **pour chaque** élément du tableau.

Chacun de ces tours que la boucle fait s'appelle une **itération**.

### Essayez par vous-même

Alors essayons cela et voyons comment cela fonctionne. Allez-y et ouvrez la console dans les outils de développement de votre navigateur. Par exemple, dans Chrome, c'est Command + Option + J (Mac) ou Control + Shift + J (Windows).

* Tapez notre tableau sauvegardé dans une variable `const products = ['champignons', 'steak', 'poisson', 'aubergines', 'lentilles']`.
* Appuyez sur Entrée. Vous obtiendrez un `undefined`. C'est normal.
* Ensuite, tapez notre boucle et cette fois nous ajouterons un `console.log()` comme code à exécuter :

```js
products.forEach( product => {
	console.log(product)
})
```

Voici à quoi cela ressemblerait :

![La console des outils de développement montrant notre tableau de produits et la boucle](https://www.freecodecamp.org/news/content/images/2019/08/loops-1.png)
_La console des outils de développement de Chrome_

Ce que nous voulons ici, c'est imprimer dans la console la valeur qui est `product` à chaque itération. Essayez par vous-même. Appuyez sur Entrée.

Une fois que vous l'avez fait, la boucle va commencer. Pour chaque produit, elle va journaliser celui actuellement sélectionné dans la console jusqu'à ce qu'elle ait terminé avec tous les produits de notre tableau.

![Le code exécuté dans la console montre le nom de chaque produit du tableau imprimé dans la console](https://www.freecodecamp.org/news/content/images/2019/09/loop-results.PNG)
_Les résultats de la boucle dans la console_

Et c'est tout. Nous avons imprimé tout notre tableau dans la console. Et nous pouvons utiliser la même idée pour manipuler le DOM afin d'afficher et de modifier le contenu sur un site web. Ou faire une myriade d'autres choses avec les données.

Et si nous voulions traiter certaines de ces données différemment et ne pas exécuter le même code pour tous les produits ? Par exemple, si nous voulons afficher un "(v)" uniquement à côté des articles végétariens.

Dans l'article suivant, j'explique justement cela. Je prends notre exemple à l'étape suivante et parle de la façon dont les **conditionnelles** nous permettent de faire cela - allez-y !

[https://www.freecodecamp.org/news/what-in-the-world-is-a-javascript-conditional-for/](https://www.freecodecamp.org/news/what-in-the-world-is-a-javascript-conditional-for/)

## Conclusion

Pour résumer, une **boucle** prend nos données (un tableau dans ce cas) et nous permet d'y accéder. Elle **itère** ensuite sur chaque élément du tableau et **exécute** un code pour chaque élément.

J'espère que la prochaine fois que vous rencontrerez une boucle, vous trouverez plus facile de comprendre comment elle fonctionne. Et qu'il sera plus clair pourquoi vous pourriez en avoir besoin dans un contexte front-end.

Dans cet article, nous avons vu une boucle `forEach()`. Mais à part `forEach()`, il existe de nombreuses autres **boucles** et **méthodes de tableau** à apprendre. De la boucle `for` la plus basique à des méthodes plus avancées comme `map()` et `filter()`. Ce sont des outils extrêmement puissants pour le développement avec lesquels vous devriez vous familiariser. Vous vous retrouverez à les utiliser en travaillant sur tout type d'application.

### Clôture

Merci d'avoir lu. J'espère que vous avez trouvé cela utile. Et si vous avez apprécié, partager cela serait grandement apprécié. Si vous avez des questions ou des commentaires, je suis sur [Twitter](https://twitter.com/Syknapse) [@Syknapse](https://twitter.com/Syknapse) et j'adorerais avoir de vos nouvelles.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-157.png)
_Photo par [Claudia](https://twitter.com/__Santaella)_

Je m'appelle Syk et je suis développeur front-end chez [Lola Market](https://twitter.com/Tech_LolaMarket) à Madrid. J'ai changé de carrière pour devenir développeur web dans un domaine sans rapport, donc j'essaie de créer du contenu pour ceux qui sont sur un chemin similaire. Mes messages privés sont toujours ouverts pour les développeurs web en herbe ayant besoin de soutien. Vous pouvez également lire ma transformation dans [cet article](https://medium.com/free-code-camp/how-i-switched-careers-and-got-a-developer-job-in-10-months-a-true-story-b8895e855a8b).

[https://www.freecodecamp.org/news/how-i-switched-careers-and-got-a-developer-job-in-10-months-a-true-story-b8895e855a8b/](https://www.freecodecamp.org/news/how-i-switched-careers-and-got-a-developer-job-in-10-months-a-true-story-b8895e855a8b/)

---