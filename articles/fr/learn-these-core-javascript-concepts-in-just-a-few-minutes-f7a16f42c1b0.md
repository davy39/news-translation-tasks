---
title: Apprenez ces concepts fondamentaux de JavaScript en quelques minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-27T16:50:06.000Z'
originalURL: https://freecodecamp.org/news/learn-these-core-javascript-concepts-in-just-a-few-minutes-f7a16f42c1b0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*H-25KB7EbSHjv70HXrdl6w.png
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Apprenez ces concepts fondamentaux de JavaScript en quelques minutes
seo_desc: 'By Dler Ari

  Sometimes, you just want to learn something quickly. And reading through comprehensive
  articles that describe specific JavaScript concepts may cause cognitive overload.
  The purpose of this article is to describe a few common concepts as s...'
---

Par Dler Ari

Parfois, vous voulez simplement apprendre quelque chose rapidement. Et lire des articles complets qui décrivent des concepts spécifiques de JavaScript peut causer une surcharge cognitive. Le but de cet article est de décrire quelques concepts courants aussi simplement que possible avec :

* Une courte description
* Pourquoi c'est pertinent
* Un exemple de code pratique (ES5/ES6 avec des fonctions fléchées).

Il est toujours bon d'avoir des connaissances générales lorsque vous travaillez avec l'écosystème JS. Vous serez conscient de comment les choses fonctionnent et interagissent, et vous pourrez apprendre et améliorer les choses plus rapidement.

Ces concepts JS sont choisis en fonction de leur popularité et de leur pertinence que j'ai observées au sein de la communauté. Si vous voulez apprendre un concept qui ne fait pas partie de cet article, laissez un commentaire et je l'ajouterai dans un proche avenir.

> Si vous voulez devenir un meilleur développeur web, lancer votre propre entreprise, enseigner aux autres, ou simplement améliorer vos compétences en développement, je publierai des conseils et astuces hebdomadaires sur les derniers langages de développement web.

_Améliorez vos [compétences JavaScript avec ces méthodes JS utiles](https://medium.freecodecamp.org/7-javascript-methods-that-will-boost-your-skills-in-less-than-8-minutes-4cc4c3dca03f)_.

#### Les concepts JS que nous allons examiner :

1. Portée (Scope)
2. IIFE
3. MVC
4. Async/await
5. Fermeture (Closure)
6. Rappel (Callback)

### 1. Portée (Scope)

**La portée est simplement une boîte avec des frontières.** Il existe deux types de frontières en JS : locale et globale, également appelées intérieure et extérieure.

Locale signifie que vous avez accès à tout ce qui se trouve dans les frontières (à l'intérieur de la boîte), tandis que globale est tout ce qui se trouve à l'extérieur des frontières (à l'extérieur de la boîte).

Ces termes sont souvent utilisés lorsque nous parlons de classes, de fonctions et de méthodes. Ils permettent de déterminer ce qui est accessible (visible) dans le contexte actuel.

#### **Pourquoi est-ce pertinent ?**

* Sépare la logique
* Réduit la portée
* Améliore la lisibilité

#### **Exemple**

Supposons que vous créez une fonction et que vous voulez accéder à une variable définie dans la portée globale.

#### **ES5**

![Image](https://cdn-media-1.freecodecamp.org/images/FH-wWl6GjJqSkNku4tZBKaAGkFjDdwZhbICJ)
_Portée locale/globale en JavaScript_

#### ES6

![Image](https://cdn-media-1.freecodecamp.org/images/ismFUwaw2zTkQCszmFA7xTTzR7HLWZKYnBSk)
_Portée locale/globale en JavaScript (fonctions fléchées)_

Comme le montre l'exemple ci-dessus, la fonction `showName()` a accès à tout ce qui est défini dans ses frontières (localement), et aussi à l'extérieur (globalement). Rappelez-vous, la portée globale ne peut pas accéder aux variables définies dans la portée locale car elles sont enfermées du monde extérieur, sauf si vous les retournez.

### 2. IIFE

**IIFE (Immediately Invoked Function Expression), comme son nom l'indique, signifie que la fonction est « immédiatement invoquée » lorsqu'elle est créée.** Avant que ES6++ présente des classes/méthodes pour supporter le paradigme de programmation orientée objet (OOP), la manière commune était de mimiquer IIFE comme un nom de classe, et d'invoquer des fonctions comme des méthodes enveloppées dans un type `return`.

**Pourquoi est-ce pertinent ?**

* Exécute immédiatement le code
* Évite que la portée globale ne soit polluée
* Supporte la structure asynchrone
* Améliore la lisibilité (certains peuvent argumenter le contraire)

#### Exemple

La technologie a beaucoup changé au cours des dernières années. Maintenant, par exemple, vous avez la capacité de changer la couleur de presque n'importe quoi — comme votre voiture. Regardons un exemple de code.

#### **ES5**

![Image](https://cdn-media-1.freecodecamp.org/images/skU76x-Bf186aOzCFNC5ztWMrORzDeWragCa)
_IIFE en JavaScript (Immediately Invoked Function Expression)_

#### **ES6**

![Image](https://cdn-media-1.freecodecamp.org/images/1mYlt8zccdCyawVfU2Wjyz9bIKkIY3b3L3sC)
_IIFE en JavaScript (fonctions fléchées)_

Dans l'exemple ci-dessus, nous avons enveloppé deux fonctions dans le type `return` (`changeColorToRed()` & `changeColorToBlack()`). Cela nous permet d'accéder à plusieurs fonctions, et d'invoquer la méthode que nous voulons.

En bref, nous invoquons d'abord la `car` (expression de fonction) afin d'accéder à ce qui se trouve à l'intérieur. Ensuite, nous pouvons utiliser la notation `.` pour invoquer la fonction qui est définie dans le type `return`. Cette approche est similaire à la structure de l'utilisation de classes/méthodes où nous appelons d'abord le nom de la classe avant de pouvoir appeler le nom de la méthode. De cette façon, vous pouvez écrire un code propre, maintenable et réutilisable.

### 3. MVC

Modèle-vue-contrôleur est un cadre de conception (*pas un langage de programmation) qui nous permet de séparer le comportement en une structure pratique du monde réel. Presque 85 % des applications basées sur le web aujourd'hui ont ce modèle sous-jacent d'une manière ou d'une autre. Il existe d'autres types de cadres de conception, mais celui-ci est de loin le plus fondamental et le plus facile à comprendre.

#### Pourquoi est-ce pertinent ?

* Scalabilité et maintenabilité à long terme
* Facile à améliorer, mettre à jour et déboguer (basé sur l'expérience personnelle)
* Facile à configurer
* Fournit une structure et une vue d'ensemble

#### Exemple

Regardons un court exemple du cadre de conception MVC.

#### ES5

![Image](https://cdn-media-1.freecodecamp.org/images/IYMt5aQAhY2zLTisweqQjuo6OIHcsjDmZyBf)
_Modèle de conception modèle-vue-contrôleur_

#### ES6

![Image](https://cdn-media-1.freecodecamp.org/images/m-NV7R88VET9ZkFZrG5IP7kljkBocaP8Avz4)
_Modèle de conception modèle-vue-contrôleur (fonctions fléchées)_

Comme le montre l'exemple ci-dessus, nous diviserions généralement la `vue`, le `modèle` et le `contrôleur` en dossiers/fichiers séparés en termes de bonnes pratiques, mais juste pour illustrer le concept, nous les avons tous mis dans un seul fichier. Les objectifs du cadre de conception sont de simplifier le processus de développement et de soutenir un environnement collaboratif durable.

### 4. Async/await

**Arrêtez et attendez jusqu'à ce que quelque chose soit résolu.** Cela fournit un moyen de maintenir le traitement asynchrone de manière plus synchrone. Par exemple, vous devez vérifier si le mot de passe d'un utilisateur est correct (comparer à ce qui existe sur le serveur) avant de permettre à l'utilisateur d'entrer dans le système. Ou peut-être avez-vous effectué une requête REST API et vous voulez que les données soient complètement chargées avant de les pousser vers la vue.

#### Pourquoi est-ce pertinent ?

* Capacités synchrones
* Contrôle le comportement
* Réduit l'« enfer des rappels »

#### Exemple

Supposons que vous voulez obtenir tous les utilisateurs d'une [API REST](https://jsonplaceholder.typicode.com/) et afficher les résultats au format JSON.

#### ES5

![Image](https://cdn-media-1.freecodecamp.org/images/8UAkzKiRlj-iOuRldGvPHvgOKwzvCg0eH2qJ)
_Promesses Async et Await_

#### ES6

![Image](https://cdn-media-1.freecodecamp.org/images/nN3ogGjjsQWjI-Cg4P-33hxyVI0hT8zP1r1p)
_Promesses Async et Await (fonctions fléchées)_

Pour utiliser `await`, nous devons l'envelopper dans une fonction `async` pour notifier JS que nous travaillons avec des promesses. Comme le montre l'exemple, nous attendons deux choses : `response` et `users`. Avant de pouvoir convertir la `response` au format JSON, nous devons nous assurer que la `response` est récupérée, sinon nous pouvons finir par convertir une `response` qui n'est pas encore là, ce qui déclenchera probablement une erreur.

### 5. Fermeture (Closure)

**Une fermeture est simplement une fonction à l'intérieur d'une autre fonction.** Elle est utilisée lorsque vous voulez étendre le comportement, comme passer des variables, des méthodes ou des tableaux d'une fonction externe à une fonction interne. Nous pouvons également accéder au contexte défini dans la fonction externe à partir de la fonction interne, mais pas l'inverse (rappellez-vous les principes de portée dont nous avons parlé ci-dessus).

#### **Pourquoi est-ce pertinent ?**

* Étend le comportement
* Utile lorsque vous travaillez avec des événements

#### **Exemple**

Supposons que vous travaillez comme ingénieur de développement pour Volvo, et qu'ils ont besoin d'une fonction qui imprime simplement le nom de la voiture.

#### ES5

![Image](https://cdn-media-1.freecodecamp.org/images/0IezBqbOGhYtOc69mqYc1s62a6iVlrjROYQh)
_Fermeture en JavaScript_

#### ES6

![Image](https://cdn-media-1.freecodecamp.org/images/u5gESTsVRAEEzcpzYBvYZs17HCrwjyYTkaZd)
_Fermeture en JavaScript (fonctions fléchées)_

La fonction `showName()` est une fermeture, car elle étend le comportement de la fonction `showInfo()`, et a également accès à la variable `carType`.

### 6. Rappel (Callback)

**Un rappel est une fonction qui s'exécute après qu'une autre fonction a été exécutée. On l'appelle aussi un appel-après.** Dans le monde JavaScript, une fonction qui attend qu'une autre fonction s'exécute ou retourne une valeur (tableau ou objet) est appelée un rappel. Un rappel est un moyen de rendre les opérations asynchrones plus synchrones (ordre séquentiel).

#### **Pourquoi est-ce pertinent ?**

* Attend qu'un événement s'exécute
* Fournit des capacités synchrones
* Moyens pratiques pour enchaîner des fonctionnalités (Si A est terminé, alors exécutez B, et ainsi de suite)
* Fournit une structure de code et un contrôle
* Soyez conscient, vous avez peut-être entendu parler de l'_enfer des rappels_. Cela signifie simplement que vous avez une structure récursive de rappels (rappels dans des rappels dans des rappels et ainsi de suite). [Ce n'est pas pratique](http://blog.mclain.ca/assets/images/callbackhell.png).

#### **Exemple**

Disons qu'Elon Musk chez SpaceX a besoin d'une fonctionnalité qui allumera les 27 moteurs Merlin de Falcon Heavy (la fusée la plus puissante au monde par un facteur de deux) lorsqu'un bouton est pressé.

#### ES5

![Image](https://cdn-media-1.freecodecamp.org/images/by0SLg-QlbxG7OQ5CuiXGLxuZ9WXnfkLIsrB)
_Rappel en JavaScript_

#### ES6

![Image](https://cdn-media-1.freecodecamp.org/images/rPoRbhRgRbETZ5bKxo5tBJfVHehh784r5t99)
_Rappel en JavaScript (fonctions fléchées)_

Remarquez qu'il attend qu'un événement se produise (un clic sur un bouton) avant d'effectuer une action (allumer les moteurs). En bref, nous passons la fonction `fireUpEngines()` comme argument (rappel) à la fonction `pressButton()`. Lorsque l'utilisateur presse le bouton, cela allume les moteurs.

Voilà ! Certains des concepts JS les plus populaires expliqués simplement avec des exemples. J'espère que ces concepts vous ont aidé à comprendre un peu mieux JS et comment il fonctionne.

Vous pouvez me trouver sur Medium où je publie sur une base hebdomadaire. Ou vous pouvez me suivre sur [Twitter](http://twitter.com/dleroari), où je publie des conseils et astuces pertinents sur le développement web ainsi que des histoires personnelles.

_P.S. Si vous avez aimé cet article et que vous en voulez plus comme celui-ci, applaudissez 💙 et partagez avec des amis, c'est bon pour le karma._