---
title: De Zéro à Héros du Front-end (Partie 2)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-05-24T12:05:24.000Z'
originalURL: https://freecodecamp.org/news/from-zero-to-front-end-hero-part-2-adfa4824da9b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2HMyUzkxeVEguBwDI9-rYg.png
tags:
- name: Design
  slug: design
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: De Zéro à Héros du Front-end (Partie 2)
seo_desc: 'By Jonathan Z White

  This article is part two of the “From Zero to Front-end Hero” series. In part one,
  you learned how to create layouts with HTML and CSS as well as some best practices.
  In part two, we will focus on learning JavaScript as a standalo...'
---

Par Jonathan Z White

Cet article est la deuxième partie de la série « De Zéro à Héros du Front-end ». Dans [la partie un](https://medium.com/@JonathanZWhite/from-zero-to-front-end-hero-part-1-7d4f7f0bff02), vous avez appris à créer des mises en page avec HTML et CSS ainsi que certaines bonnes pratiques. Dans la partie deux, nous nous concentrerons sur l'apprentissage de JavaScript en tant que langage autonome, sur la façon d'ajouter de l'interactivité aux interfaces, sur les modèles de conception et les motifs architecturaux JavaScript, et sur la façon de construire des applications web.

Tout comme avec HTML et CSS, il existe de nombreux tutoriels JavaScript. Cependant, surtout pour quelqu'un de nouveau dans le front-end, il est difficile de savoir quels tutoriels utiliser et dans quel ordre les suivre. L'objectif principal de cette série est de vous fournir une feuille de route pour vous aider à naviguer dans l'apprentissage du développement front-end.

Si vous n'avez pas encore lu la partie un, faites-le avant de continuer.

[**De Zéro à Héros du Front-end (Partie 1)**](https://medium.com/p/7d4f7f0bff02)  
[_Un guide complet pour apprendre le développement front-end_medium.com](https://medium.com/p/7d4f7f0bff02)

### Bases de JavaScript

![Image](https://cdn-media-1.freecodecamp.org/images/1*TWVs8hNCI7B7t2Y4tA-u1A.png)

JavaScript est un langage de programmation multiplateforme qui peut être utilisé pour presque tout de nos jours, mais nous y reviendrons plus tard une fois que vous aurez compris les bases de la façon dont les développeurs utilisent JavaScript pour le web.

#### Langage

Avant d'apprendre à appliquer JavaScript au web, apprenez d'abord le langage lui-même. Pour commencer, lisez le [cours accéléré sur les bases du langage](https://developer.mozilla.org/fr/docs/Web/JavaScript/Guide/Grammaire_et_types) du Mozilla Developer Network. Ce tutoriel vous enseignera les constructions de base du langage comme les variables, les conditionnelles et les fonctions.

Après cela, lisez les sections suivantes dans le [guide JavaScript](https://developer.mozilla.org/fr/docs/Web/JavaScript/Guide) de MDN :

* [Grammaire et types](https://developer.mozilla.org/fr/docs/Web/JavaScript/Guide/Grammaire_et_types)
* [Contrôle de flux et gestion des erreurs](https://developer.mozilla.org/fr/docs/Web/JavaScript/Guide/Contr%C3%B4le_de_flux_et_gestion_des_erreurs)
* [Boucles et itérations](https://developer.mozilla.org/fr/docs/Web/JavaScript/Guide/Boucles_et_it%C3%A9rations)
* [Fonctions](https://developer.mozilla.org/fr/docs/Web/JavaScript/Guide/Fonctions)

Ne vous inquiétez pas trop de mémoriser la syntaxe spécifique. Vous pouvez toujours la chercher. Concentrez-vous plutôt sur la compréhension des concepts importants comme l'instantiation des variables, les boucles et les fonctions. Si le matériel est trop dense, ce n'est pas grave. Parcourez la lecture ; vous pourrez toujours revenir plus tard. Et en mettant ces concepts en pratique, ils deviendront beaucoup plus clairs.

Pour rompre la monotonie de l'apprentissage basé sur le texte, consultez le [cours JavaScript](https://www.codecademy.com/fr/learn/javascript) de Codecademy. Il est pratique et amusant. De plus, si vous avez le temps, pour chaque concept que j'ai listé ci-dessus, lisez le chapitre correspondant dans [Eloquent JavaScript](http://eloquentjavascript.net/) pour renforcer votre apprentissage. Eloquent JavaScript est un excellent livre en ligne gratuit que tout aspirant développeur front-end devrait lire.

#### Interactivité

![Image](https://cdn-media-1.freecodecamp.org/images/1*V4UtSyfCN9DDpl70IxXSHA.gif)
_[Une utilisation de JavaScript est l'animation de vos mises en page](https://dribbble.com/shots/2067564-Replace" rel="noopener" target="_blank" title=")_

Maintenant que vous avez une compréhension de base de JavaScript en tant que langage, la prochaine étape est de l'appliquer au web. Pour comprendre comment JavaScript interagit avec les sites web, vous devez d'abord connaître le [Document Object Model (DOM)](https://developer.mozilla.org/fr/docs/Web/API/Document_Object_Model/Introduction).

Le DOM est une structure représentationnelle des documents HTML. C'est une structure en forme d'arbre composée d'[objets JavaScript](http://javascriptissexy.com/javascript-objects-in-detail/) qui correspondent aux nœuds HTML. Pour plus de lectures sur le DOM, lisez [Qu'est-ce que le DOM](https://css-tricks.com/dom/) par CSSTricks. Il fournit une explication simple et directe du DOM.

![Image](https://cdn-media-1.freecodecamp.org/images/1*o1lGaXpnKYgp2r9CFOI_9A.png)
_[Inspection du DOM](https://dribbble.com/shots/1169778-Chrome-and-Sublime-text" rel="noopener" target="_blank" title=")_

JavaScript interagit avec le DOM pour le changer et le mettre à jour. Voici un exemple où nous sélectionnons un élément HTML et changeons son contenu :

```
var container = document.getElementById("container"); 
```

```
container.innerHTML = 'Nouveau Contenu !';
```

Ne vous inquiétez pas, ce n'était qu'un simple exemple. Vous pouvez faire beaucoup plus que cela avec la manipulation du DOM JavaScript. Pour en savoir plus sur la façon d'utiliser JavaScript pour interagir avec le DOM, parcourez les guides suivants dans la section de MDN, [Le Document Object Model](https://developer.mozilla.org/fr/docs/Web/API/Document_Object_Model).

* [Événements](https://developer.mozilla.org/fr/docs/Web/API/Document_Object_Model/Events)
* [Exemples de développement web et XML utilisant le DOM](https://developer.mozilla.org/fr/docs/Web/API/Document_Object_Model/Examples)
* [Comment créer un arbre DOM](https://developer.mozilla.org/fr/docs/Web/API/Document_object_model/How_to_create_a_DOM_tree)
* [Introduction au DOM](https://developer.mozilla.org/fr/docs/Web/API/Document_Object_Model/Introduction)
* [Localisation des éléments DOM à l'aide de sélecteurs](https://developer.mozilla.org/fr/docs/Web/API/Document_object_model/Locating_DOM_elements_using_selectors)

Encore une fois, concentrez-vous sur les concepts plutôt que sur la syntaxe. Soyez capable de répondre aux questions suivantes :

* Qu'est-ce que le DOM ?
* Comment interrogez-vous les éléments ?
* Comment ajoutez-vous des écouteurs d'événements ?
* Comment changez-vous les propriétés des nœuds DOM ?

Pour une liste des interactions JavaScript DOM courantes, consultez [JavaScript Functions and Helpers](https://plainjs.com/javascript/) par PlainJS. Ce site fournit des exemples de comment faire des choses comme définir des [styles sur des éléments HTML](https://plainjs.com/javascript/styles/set-and-get-css-styles-of-elements-53/) et [attacher des écouteurs d'événements de clavier](https://plainjs.com/javascript/events/getting-the-keycode-from-keyboard-events-17/). Et si vous voulez approfondir, vous pouvez toujours lire la section sur le DOM dans [Eloquent JavaScript](http://eloquentjavascript.net/13_dom.html).

#### Inspecteur

Pour déboguer le JavaScript côté client, nous utilisons des outils de développement intégrés aux navigateurs. Le panneau d'inspection est disponible dans la plupart des navigateurs et vous permet de voir le source des pages web. Vous pouvez suivre JavaScript lors de son exécution, imprimer des instructions de débogage dans la console et voir des choses comme les requêtes réseau et les ressources.

Voici un [tutoriel](https://developer.chrome.com/devtools) sur l'utilisation de l'outil de développement Chrome. Si vous utilisez Firefox, vous pouvez consulter ce [tutoriel](https://developer.mozilla.org/fr/docs/Tools/Page_Inspector).

![Image](https://cdn-media-1.freecodecamp.org/images/1*wW-FbgJhP0R_id-XPOSKpg.jpeg)
_[Outils de développement Chrome](https://dribbble.com/shots/995021-Discover-DevTools" rel="noopener" target="_blank" title=")_

### Pratique des bases

À ce stade, il y a encore beaucoup plus à apprendre sur JavaScript. Cependant, la dernière section contenait beaucoup de nouvelles informations. Je pense qu'il est temps de faire une pause et de s'attaquer à quelques petites expériences. Elles devraient aider à solidifier certains des concepts que vous venez d'apprendre.

#### Expérience 1

Pour l'expérience 1, allez sur [AirBnB](https://www.airbnb.com/), ouvrez l'[inspecteur de page](https://developer.chrome.com/devtools) de votre navigateur et cliquez sur l'onglet [console](https://developer.chrome.com/devtools/docs/console). Ici, vous pouvez exécuter JavaScript sur la page. Ce que nous allons faire, c'est nous amuser à manipuler certains des éléments de la page. Voyez si vous pouvez faire toutes les manipulations DOM suivantes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5L17hFKIMTsBFQOLCy8tCQ.png)
_[Airbnb.com](https://www.airbnb.com/" rel="noopener" target="_blank" title=")_

J'ai choisi le site web d'AirBnB parce que leurs noms de classes CSS sont relativement simples et ne sont pas obfusqués par un compilateur. Cependant, vous pouvez choisir de faire cela sur n'importe quelle page que vous voulez.

* Sélectionnez une balise d'en-tête avec un nom de classe unique et changez le texte
* Sélectionnez n'importe quel élément sur la page et supprimez-le
* Sélectionnez n'importe quel élément et changez une de ses propriétés CSS
* Sélectionnez une balise de section spécifique et déplacez-la vers le bas de 250 pixels
* Sélectionnez n'importe quel composant, comme un panneau, et ajustez sa visibilité
* Définissez une fonction nommée _doSomething_ qui alerte « Hello world » et exécutez-la ensuite
* Sélectionnez une balise de paragraphe spécifique, ajoutez un écouteur d'événement _click_ et exécutez _doSomething_ chaque fois que l'événement est déclenché

Si vous êtes bloqué, référez-vous au guide [JavaScript Functions and Helpers](https://plainjs.com/javascript/). J'ai basé la plupart de ces tâches sur celui-ci. Voici un exemple de la façon de compléter le premier point :

```
var header = document.querySelector('.text-branding')
```

```
header.innerText = 'Boop'
```

Le but principal de cette expérience est de prendre certaines des choses que vous avez apprises sur JavaScript et la manipulation du DOM et de les voir en action.

#### Expérience 2

![Image](https://cdn-media-1.freecodecamp.org/images/1*7365CToqHiLkXf16Di8xRw.gif)
_[JavaScript permet aux développeurs de créer des interfaces interactives](https://dribbble.com/shots/2716909-Opening-screen-for-banking-App" rel="noopener" target="_blank" title=")_

En utilisant [CodePen](https://twitter.com/JonathanZWhite), écrivez une expérience JavaScript lourde de base qui utilise la manipulation du DOM et nécessite une certaine [logique programmatique](https://fr.wikipedia.org/wiki/Logique_en_informatique) pour fonctionner. L'objectif de cette expérience est de prendre certaines des choses que vous avez apprises dans [De Zéro à Héros du Front-end Partie 1](https://medium.freecodecamp.com/from-zero-to-front-end-hero-part-1-7d4f7f0bff02#.qp3n3h8ew) et de les combiner avec JavaScript. Voici quelques exemples de référence qui pourraient servir d'inspiration.

* [Tableau Périodique](http://codepen.io/tony_the_coder/pen/GZdNQY)
* [Générateur de Couleurs d'Humeur](http://codepen.io/mecarter/pen/RNomVo)
* [Calculatrice](http://codepen.io/nodws/pen/heILd)
* [Quiz JavaScript](http://codepen.io/jasonchan/pen/wMaEwN)
* [Astéroïdes Jouables sur Canvas](http://codepen.io/jeffibacache/pen/bzBsp)

### Plus de JavaScript

Maintenant que vous connaissez un peu JavaScript et que vous avez eu un peu de pratique, nous allons passer à des concepts plus avancés. Les concepts ci-dessous ne sont pas directement liés les uns aux autres. Je les ai regroupés dans cette section parce qu'ils sont nécessaires pour comprendre comment construire des systèmes front-end plus complexes. Vous comprendrez mieux comment les utiliser une fois que vous atteindrez la section sur les expériences et les frameworks.

#### Langage

En faisant plus de travail avec JavaScript, vous rencontrerez certains concepts de niveau supérieur. Voici une liste de certains de ces concepts. Lorsque vous avez le temps, parcourez chaque point. De plus, [Eloquent JavaScript](http://eloquentjavascript.net/) couvre une grande partie de ce matériel, si vous voulez compléter votre apprentissage.

* [Héritage prototypal](https://developer.mozilla.org/fr/docs/Web/JavaScript/Guide/H%C3%A9ritage_et_cha%C3%AEne_de_prototypes)
* [Portée](https://spin.atomicobject.com/2014/10/20/javascript-scope-closures/)
* [Fermetures](https://developer.mozilla.org/fr/docs/Web/JavaScript/Closures)
* [Boucle d'événements](https://developer.mozilla.org/fr/docs/Web/JavaScript/EventLoop)
* [Remontée d'événements](http://javascript.info/tutorial/bubbling-and-capturing)
* [Apply, call, et bind](http://javascriptissexy.com/javascript-apply-call-and-bind-methods-are-essential-for-javascript-professionals/)
* [Rappels et promesses](https://www.quora.com/Quelle-est-la-diff%C3%A9rence-entre-une-promesse-et-un-rappel-en-Javascript)
* [Hissage des variables et des fonctions](http://adripofjavascript.com/blog/drips/variable-and-function-hoisting)
* [Currying](http://www.sitepoint.com/currying-in-functional-javascript/)

#### Impératif vs. Déclaratif

Il existe deux types d'approches pour la façon dont JavaScript interagit avec le DOM : impératif et déclaratif. D'une part, la programmation déclarative se concentre sur _ce qui_ se passe. D'autre part, la programmation impérative se concentre sur _ce qui_ ainsi que sur le _comment_.

```
var hero = document.querySelector('.hero')
```

```
hero.addEventListener('click', function() {  var newChild = document.createElement('p')
```

```
  newChild.appendChild(document.createTextNode('Hello world!'))    newChild.setAttribute('class', 'text')    newChild.setAttribute('data-info', 'header')    hero.appendChild(newChild) })
```

Ceci est un exemple de programmation impérative où nous interrogeons manuellement un élément et stockons l'état de l'UI dans le DOM. En d'autres termes, nous nous concentrons sur _comment_ atteindre quelque chose. Le plus gros problème avec ce code est qu'il est fragile. Si quelqu'un travaillant sur le code change le nom de la classe en HTML de _hero_ à _villain_, l'écouteur d'événement ne se déclenchera plus puisque la classe _hero_ n'existe plus dans le DOM.

La programmation déclarative résout ce problème. Au lieu de devoir sélectionner des éléments, vous laissez cela au framework ou à la bibliothèque que vous utilisez. Cela vous permet de vous concentrer sur le _quoi_ au lieu du _comment_. Pour plus de lectures, consultez [The State Of JavaScript — A Shift From Imperative To Declarative](http://www.tysoncadenhead.com/blog/the-state-of-javascript-a-shift-from-imperative-to-declarative#.Vz0WEZMrIUE) et [Three D’s of Web Development #1: Declarative vs. Imperative](http://developer.telerik.com/featured/three-ds-of-web-development-1-declarative-vs-imperative/).

Ce guide vous enseigne d'abord l'approche impérative avant d'introduire l'approche déclarative avec des frameworks comme Angular et des bibliothèques comme React. Je recommande d'apprendre dans cet ordre car cela vous permet de voir le problème que le JavaScript déclaratif résout.

#### Ajax

Tout au long de certains de ces articles et tutoriels, vous avez probablement vu le terme [Ajax](https://developer.mozilla.org/fr/docs/Web/Guide/AJAX) mentionné plusieurs fois. Ajax est une technique qui permet aux pages web d'interfacer avec un serveur en utilisant JavaScript.

![Image](https://cdn-media-1.freecodecamp.org/images/1*kkezNwUnuEiAztlQRkJ69A.gif)
_[Ajax est ce qui rend le contenu dynamique](https://dribbble.com/shots/1911260-Loading-with-Swift" rel="noopener" target="_blank" title=")_

Par exemple, lorsque vous soumettez un formulaire sur un site web, il collecte votre entrée et fait une requête HTTP qui envoie ces données à un serveur. Lorsque vous publiez un tweet sur Twitter, votre client Twitter fait une requête HTTP à l'API du serveur de Twitter et met à jour la page avec la réponse du serveur.

Pour des lectures sur Ajax, consultez [Qu'est-ce que Ajax](http://www.vandelaydesign.com/what-is-ajax-webdev/). Si vous ne comprenez toujours pas entièrement le concept d'AJAX, jetez un coup d'œil à [Explain it like i'm 5, what is Ajax](https://www.reddit.com/r/explainlikeimfive/comments/19gvn9/explain_it_like_im_5_what_is_ajax/). Et si tout cela ne suffit pas, vous pouvez lire le [chapitre](http://eloquentjavascript.net/17_http.html) d'Eloquent JavaScript sur HTTP.

Aujourd'hui, la norme à venir pour les navigateurs pour faire des requêtes HTTP est [Fetch](https://developer.mozilla.org/fr/docs/Web/API/Fetch_API). Vous pouvez en savoir plus sur Fetch dans cet article de [Dan Walsh](https://davidwalsh.name/fetch). Il couvre comment Fetch fonctionne et comment l'utiliser. Vous pouvez également trouver un [polyfill](http://stackoverflow.com/questions/7087331/what-is-the-meaning-of-polyfills-in-html5) Fetch avec une documentation [ici](https://github.com/github/fetch).

#### jQuery

Jusqu'à présent, vous avez effectué des manipulations DOM avec uniquement JavaScript. La vérité est qu'il existe de nombreuses bibliothèques de manipulation DOM qui fournissent des API pour simplifier le code que vous écrivez.

L'une des bibliothèques de manipulation DOM les plus populaires est [jQuery](https://jquery.com/). Gardez à l'esprit que jQuery est une bibliothèque impérative. Elle a été écrite avant que les systèmes front-end ne soient aussi complexes qu'ils le sont aujourd'hui. Aujourd'hui, la réponse à la gestion des UI complexes sont les frameworks et bibliothèques déclaratifs comme Angular et React. Cependant, je recommande toujours d'apprendre jQuery car vous le rencontrerez très probablement au cours de votre carrière en tant que développeur front-end.

![Image](https://cdn-media-1.freecodecamp.org/images/1*4XD5t8AEjQFWeTWEIdhQpw.gif)
_[jQuery est une abstraction au-dessus de la manipulation DOM JavaScript simple](https://dribbble.com/shots/2677538-Recipe-Application" rel="noopener" target="_blank" title=")_

Pour apprendre les bases de jQuery, consultez le [Centre d'Apprentissage](http://learn.jquery.com/) de jQuery. Il passe étape par étape à travers des concepts importants comme les [animations](http://learn.jquery.com/effects/intro-to-effects/) et la [gestion des événements](http://learn.jquery.com/events/handling-events/). Si vous voulez un tutoriel plus pratique, vous pouvez essayer le [cours jQuery](https://www.codecademy.com/learn/jquery) de Codecademy.

Gardez à l'esprit que jQuery n'est pas toujours la solution pour la manipulation DOM impérative. [PlainJS](https://plainjs.com/javascript/) et [You Might Not Need jQuery](http://youmightnotneedjquery.com/) sont deux bonnes ressources qui vous montrent des fonctions JavaScript équivalentes aux fonctions jQuery fréquemment utilisées.

#### ES5 vs. ES6

Un autre concept important à comprendre sur JavaScript est [ECMAScript](https://fr.wikipedia.org/wiki/ECMAScript) et comment il se rapporte à JavaScript. Il existe deux principales versions de JavaScript que vous rencontrerez aujourd'hui : ES5 et ES6. ES5 et ES6 sont des normes ECMAScript que JavaScript utilise. Vous pouvez les considérer comme des versions de JavaScript. Le projet final de ES5 a été finalisé en 2009 et c'est ce que vous avez utilisé jusqu'à présent.

ES6, également connu sous le nom de ES2015, est la nouvelle norme qui apporte de nouvelles constructions de langage comme les [constantes](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Instructions/const), les [classes](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Classes), et les [littéraux de gabarit](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Template_literals) à JavaScript. Il est important de noter que ES6 apporte de nouvelles fonctionnalités de langage mais les définit toujours sémantiquement en termes de ES5. Par exemple, les classes dans ES6 ne sont que du [sucre syntaxique](https://fr.wikipedia.org/wiki/Sucre_syntaxique) sur l'[héritage prototypal](https://developer.mozilla.org/fr/docs/Web/JavaScript/Guide/H%C3%A9ritage_et_cha%C3%AEne_de_prototypes) JavaScript.

Il est essentiel de connaître à la fois ES5 et ES6 car vous verrez des applications aujourd'hui qui utilisent l'un ou l'autre. Une bonne introduction à ES6 est [ES5, ES6, ES2016, ES.Next : Que se passe-t-il avec la versioning de JavaScript](http://benmccormick.org/2015/09/14/es5-es6-es2016-es-next-whats-going-on-with-javascript-versioning/) et [Getting Started with ES6 — The Next Version of JavaScript](http://weblogs.asp.net/dwahlin/getting-started-with-es6-%E2%80%93-the-next-version-of-javascript) de Dan Wahlin. Après cela, vous pouvez voir une liste complète des changements de ES5 à ES6 sur [ES6 Features](http://es6-features.org/#Constants). Si vous voulez encore plus, consultez ce [dépôt Github](https://github.com/lukehoban/es6features) des fonctionnalités ES6.

### Plus de Pratique

Si vous êtes arrivé à ce stade, félicitez-vous. Vous avez déjà appris beaucoup sur JavaScript. Mettons en pratique certaines des choses que vous avez apprises.

#### Expérience 3

![Image](https://cdn-media-1.freecodecamp.org/images/1*vThR7vEzW40OloxGnbmwuA.png)
_[Flipboard.com](https://flipboard.com/" rel="noopener" target="_blank" title=")_

L'expérience 3 se concentrera sur l'enseignement de l'application de compétences comme la manipulation du DOM et jQuery. Pour cette expérience, nous allons adopter une approche plus structurée. L'expérience 3 consistera à cloner la page d'accueil de Flipboard en suivant le tutoriel de Codecademy [Flipboard's home page and add interactivity with JavaScript](https://www.codecademy.com/skills/make-an-interactive-website).

Pendant le tutoriel, concentrez-vous sur la compréhension de la façon de rendre un site interactif, du moment où il faut le rendre interactif et de la façon d'appliquer jQuery.

#### Expérience 4

![Image](https://cdn-media-1.freecodecamp.org/images/1*OxwMghRSssqkALRIaS72iw.png)
_[Horloge de Dieter Rams](https://dribbble.com/shots/1036844-Clock" rel="noopener" target="_blank" title=")_

L'expérience 4 combine ce que vous avez appris sur HTML et CSS avec votre cours d'introduction à JavaScript. Pour cette expérience, vous créerez une horloge de votre propre design et la rendrez interactive avec JavaScript. Avant de commencer, je recommande de lire [Decoupling Your HTML, CSS, and JavaScript](http://philipwalton.com/articles/decoupling-html-css-and-javascript/) pour apprendre les conventions de nommage des classes CSS de base lorsque JavaScript est ajouté au mélange. J'ai également préparé une liste de pens sur CodePen que vous pouvez utiliser comme référence pour cette expérience. Pour plus d'exemples, recherchez [clock](http://codepen.io/search/pens?q=clock&limit=all&type=type-pens) sur CodePen.

* [Horloge Plate](http://codepen.io/stevenfabre/pen/Cyhjb)
* [Horloge Murale jQuery](http://codepen.io/mattlitzinger/pen/ruEyz)
* [Horloge Fancy](http://codepen.io/rapidrob/pen/IGEhn)
* [Horloge Rétro](http://codepen.io/OfficialAntarctica/pen/VYzvgj)
* [Horloge JavaScript Simple](http://codepen.io/dudleystorey/pen/unEyp)

Vous pouvez faire cette expérience de deux manières. Vous pouvez soit commencer par concevoir et créer la mise en page en HTML et CSS puis ajouter l'interactivité avec JavaScript. Ou vous pouvez écrire la logique JavaScript en premier puis passer à la mise en page. De plus, vous pouvez utiliser jQuery, mais vous pouvez également utiliser du JavaScript simple.

### Frameworks JavaScript

Avec les bases de JavaScript sous votre ceinture, il est temps d'apprendre les frameworks JavaScript. Les frameworks sont des bibliothèques JavaScript qui vous aident à structurer et organiser votre code. Les frameworks JavaScript fournissent aux développeurs des solutions répétables à des problèmes front-end complexes, comme la gestion d'état, le routage et l'optimisation des performances. Ils sont couramment utilisés pour construire des [applications web](http://www.visionmobile.com/blog/2013/07/web-sites-vs-web-apps-what-the-experts-think/).

Je n'inclurai pas une description de chaque framework JavaScript. Cependant, voici une liste rapide de quelques frameworks : [Angular](https://angularjs.org/), [React](https://facebook.github.io/react/) + [Flux](https://facebook.github.io/react/docs/flux-overview.html), [Ember](http://emberjs.com/), [Aurelia](http://aurelia.io/), [Vue](http://vuejs.org/), et [Meteor](https://www.meteor.com/). Vous n'avez pas à apprendre chaque framework. Choisissez-en un et apprenez-le bien. Ne courez pas après les frameworks. Comprenez plutôt les philosophies et principes de programmation sous-jacents sur lesquels les frameworks sont construits.

#### Motifs Architecturaux

Avant de regarder les frameworks, il est important de comprendre quelques motifs architecturaux que les frameworks tendent à utiliser : [modèle-vue-contrôleur](https://fr.wikipedia.org/wiki/Mod%C3%A8le-vue-contr%C3%B4leur), [modèle-vue-vue-modèle](https://fr.wikipedia.org/wiki/Mod%C3%A8le-vue-vue-mod%C3%A8le), et [modèle-vue-présentateur](https://fr.wikipedia.org/wiki/Mod%C3%A8le-vue-pr%C3%A9sentateur). Ces motifs sont conçus pour créer une [séparation claire des préoccupations](https://fr.wikipedia.org/wiki/S%C3%A9paration_des_pr%C3%A9occupations) entre les couches de l'application.

La séparation des préoccupations est un principe de conception qui suggère de diviser les applications en différentes couches spécifiques à un domaine. Par exemple, au lieu d'avoir du HTML qui conserve l'état de l'application, vous pouvez utiliser un objet JavaScript — généralement appelé un modèle — pour stocker l'état.

Pour en savoir plus sur ces motifs, lisez d'abord sur MVC chez [Chrome Developers](https://developer.chrome.com/apps/app_frameworks). Après cela, lisez [Comprendre MVC et MVP (Pour les Développeurs JavaScript et Backbone)](https://addyosmani.com/blog/understanding-mvc-and-mvp-for-javascript-and-backbone-developers/). Dans cet article, ne vous inquiétez pas d'apprendre Backbone, passez simplement par les parties avec des explications de MVC et MVP.

Addy Osman a également écrit sur MVVM dans [Comprendre MVVM — Un Guide Pour les Développeurs JavaScript](https://addyosmani.com/blog/understanding-mvvm-a-guide-for-javascript-developers/). Pour en savoir plus sur les origines de MVC et pourquoi il est apparu, lisez l'essai de Martin Fowler sur [GUI Architectures](http://martinfowler.com/eaaDev/uiArchs.html). Enfin, lisez la section, [JavaScript MV* Patterns](https://addyosmani.com/resources/essentialjsdesignpatterns/book/#detailmvcmvp), dans Learning JavaScript Design Patterns. [Learning JavaScript Design Patterns](https://addyosmani.com/resources/essentialjsdesignpatterns/book/) est un livre en ligne gratuit fantastique.

#### Motifs de Conception

Les frameworks JavaScript ne réinventent pas la roue. La plupart d'entre eux reposent sur des [motifs de conception](https://fr.wikipedia.org/wiki/Motif_de_conception). Vous pouvez penser aux motifs de conception comme des modèles généraux pour résoudre des problèmes courants dans le développement logiciel.

Bien que la compréhension des motifs de conception JavaScript ne soit pas un prérequis pour apprendre un framework, je suggère de parcourir la liste suivante à un moment donné.

* [Décorateur](https://addyosmani.com/resources/essentialjsdesignpatterns/book/#decoratorpatternjavascript)
* [Fabrique](https://addyosmani.com/resources/essentialjsdesignpatterns/book/#factorypatternjavascript)
* [Singleton](https://addyosmani.com/resources/essentialjsdesignpatterns/book/#singletonpatternjavascript)
* [Module révélateur](https://addyosmani.com/resources/essentialjsdesignpatterns/book/#revealingmodulepatternjavascript)
* [Façade](https://addyosmani.com/resources/essentialjsdesignpatterns/book/#facadepatternjavascript)
* [Observateur](https://addyosmani.com/resources/essentialjsdesignpatterns/book/#observerpatternjavascript)

Comprendre et être capable de mettre en œuvre certains de ces motifs de conception ne fera pas seulement de vous un meilleur ingénieur, mais vous aidera également à comprendre ce que certains frameworks font sous le capot.

#### AngularJS

AngularJS est un framework JavaScript [MVC](https://addyosmani.com/resources/essentialjsdesignpatterns/book/#detailmvc) et parfois [MVVM](https://addyosmani.com/resources/essentialjsdesignpatterns/book/#detailmvvm). Il est maintenu par Google et a pris d'assaut la communauté JavaScript lorsqu'il a été publié pour la première fois en 2010.

![Image](https://cdn-media-1.freecodecamp.org/images/1*lFZ7nP3KlRtb69abn19xJQ.png)
_[AngularJS - ce que HTML aurait dû être](https://dribbble.com/shots/2445643-Angular-JS-Developers" rel="noopener" target="_blank" title=")_

Angular est un framework déclaratif. L'une des lectures les plus utiles qui m'a aidé à comprendre comment passer de la programmation JavaScript impérative à la programmation déclarative est [How is AngularJS different from jQuery](http://stackoverflow.com/questions/13151725/how-is-angularjs-different-from-jquery) sur StackOverflow.

Si vous voulez en savoir plus sur Angular, consultez la [documentation](https://docs.angularjs.org/guide) d'Angular. Ils ont également un tutoriel appelé [Angular Cat](https://docs.angularjs.org/tutorial/step_00) qui vous permet de vous lancer dans le codage immédiatement. Un guide plus complet pour apprendre Angular peut être trouvé dans ce [dépôt Github](https://github.com/timjacobi/angular2-education) par Tim Jacobi. De plus, consultez ce guide de style des [meilleures pratiques](https://github.com/johnpapa/angular-styleguide) écrit par John Papa.

#### React + Flux

Angular résout de nombreux problèmes auxquels les développeurs sont confrontés lors de la construction de systèmes front-end complexes. Un autre outil populaire est [React](https://facebook.github.io/react/), qui est une bibliothèque pour construire des interfaces utilisateur. Vous pouvez le considérer comme le V dans MVC. Puisque React n'est qu'une bibliothèque, il est souvent vu avec une architecture connue sous le nom de [Flux](https://facebook.github.io/flux/).

![Image](https://cdn-media-1.freecodecamp.org/images/1*c0JXNVxVnTlOuQCnDqA6CA.png)
_[Une bibliothèque JavaScript pour construire des interfaces](https://dribbble.com/shots/2484828-React-Illustration" rel="noopener" target="_blank" title=")_

Facebook a conçu React et Flux pour répondre à certaines des lacunes de MVC et à ses problèmes d'échelle. Jetez un coup d'œil à leur présentation bien connue [Hacker Way: Rethinking Web App Development at Facebook](https://www.youtube.com/watch?list=PLb0IAmt7-GS188xDYE-u1ShQmFFGbrk0v&v=nYkdrAPrdcw). Elle passe en revue Flux et ses origines.

Pour commencer avec React et Flux, apprenez d'abord React. Une bonne introduction est la [documentation React](https://facebook.github.io/react/docs/getting-started.html). Après cela, consultez [React.js Introduction For People Who Know Just Enough jQuery To Get By](http://reactfordesigners.com/labs/reactjs-introduction-for-people-who-know-just-enough-jquery-to-get-by/) pour vous aider à passer de l'état d'esprit jQuery.

Une fois que vous avez une compréhension de base de React, commencez à apprendre Flux. Un bon point de départ est la [documentation officielle de Flux](https://facebook.github.io/flux/docs/overview.html). Après cela, consultez [Awesome React](https://github.com/enaqx/awesome-react), qui est une liste organisée de liens qui vous aideront à avancer dans votre apprentissage.

### Pratique avec les Frameworks

Maintenant que vous avez quelques connaissances de base sur les frameworks JavaScript et les motifs architecturaux, il est temps de les mettre en pratique. Pendant ces deux expériences, concentrez-vous sur l'application des concepts architecturaux que vous avez appris. En particulier, gardez votre code [DRY](https://fr.wikipedia.org/wiki/Ne_vous_r%C3%A9p%C3%A9tez_pas), avez une [séparation claire des préoccupations](https://fr.wikipedia.org/wiki/S%C3%A9paration_des_pr%C3%A9occupations), et adhérer au [principe de responsabilité unique](https://fr.wikipedia.org/wiki/Principe_de_responsabilit%C3%A9_unique).

#### Expérience 5

L'expérience 5 consiste à démonter et reconstruire l'application Todo MVC en utilisant JavaScript agnostique de framework. En d'autres termes, du bon vieux JavaScript sans framework. Le but de cette expérience est de vous montrer comment fonctionne MVC sans mélanger la syntaxe spécifique au framework.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ISCVxjX3_691DLnV3EPZ3w.png)

Pour commencer, consultez le résultat final sur [TodoMVC](http://todomvc.com/examples/vanillajs/). La première étape consiste à créer un nouveau projet localement et à établir d'abord les trois composants de MVC. Comme il s'agit d'une expérience impliquée, référez-vous au code source complet dans ce [dépôt Github](https://github.com/tastejs/todomvc/tree/gh-pages/examples/vanillajs). Si vous ne pouvez pas complètement reproduire le projet ou n'avez pas le temps, ce n'est pas grave. Téléchargez le code du dépôt et jouez avec les différents composants MVC jusqu'à ce que vous compreniez comment ils se corréleront les uns aux autres.

#### Expérience 6

L'expérience 6 était un bon exercice pour appliquer MVC. Comprendre MVC est une étape importante vers l'apprentissage des frameworks JavaScript. L'expérience 6 consiste à suivre un tutoriel de Scotch.io pour construire un clone d'Etsy avec Angular.

![Image](https://cdn-media-1.freecodecamp.org/images/1*zOIJ31nV3rDYBidYkPSH_A.png)

[Build an Etsy Clone with Angular and Stamplay](https://scotch.io/tutorials/build-an-etsy-clone-with-angular-and-stamplay-part-1) vous apprendra à construire une application web avec Angular, à interfacer avec des [APIs](https://fr.wikipedia.org/wiki/Interface_de_programmation), et à structurer de grands projets. Après avoir fait ce tutoriel, soyez capable de répondre aux questions suivantes.

* Qu'est-ce qu'une application web ?
* Comment MVC/MVVM est-il appliqué avec Angular ?
* Qu'est-ce qu'une API et que fait-elle ?
* Comment organisez-vous et structurez-vous de grandes bases de code ?
* Quels sont les avantages de diviser votre UI en composants de directives ?

Si vous voulez essayer de construire plus d'applications web Angular, essayez [Build a Real-Time Status Update App with AngularJS & Firebase](https://www.sitepoint.com/real-time-status-update-app-angularjs-firebase/).

#### Expérience 7

![Image](https://cdn-media-1.freecodecamp.org/images/1*3HrnGSbAzIM5Lwu0_eqmjw.png)
_[React et Flux sont une combinaison puissante pour construire des applications web complexes](https://egghead.io/series/react-flux-architecture" rel="noopener" target="_blank" title=")_

Maintenant que vous avez appliqué MVC, il est temps d'essayer [Flux](https://facebook.github.io/flux/). L'expérience 7 consiste à construire une liste de tâches en utilisant [React](https://facebook.github.io/react/) et l'architecture Flux. Vous pouvez trouver le tutoriel complet sur le [site de documentation Flux de Facebook](https://facebook.github.io/flux/docs/todo-list.html). Il vous apprendra étape par étape comment utiliser React pour construire des interfaces et comment Flux est appliqué à la construction d'applications web.

Une fois que vous avez terminé ce tutoriel, vous pouvez passer à des tutoriels plus avancés comme [How to Build a Todo App Using React, Redux, and Immutable.js](https://www.sitepoint.com/how-to-build-a-todo-app-using-react-redux-and-immutable-js/) et [Build a Microblogging App With Flux and React](http://code.tutsplus.com/courses/build-a-microblogging-app-with-flux-and-react).

### Restez à jour

Tout comme le reste du front-end, le paysage JavaScript évolue rapidement. Il est important de rester à la pointe.

![Image](https://cdn-media-1.freecodecamp.org/images/1*gcVLvWktBPvc3rgp5fLvBA.jpeg)
_[Le paysage JavaScript change rapidement](http://www.deviantart.com/art/Fantasy-Ocean-Landscape-497289755" rel="noopener" target="_blank" title=")_

Voici une liste de sites web, de blogs et de forums qui sont à la fois agréables à lire et informatifs.

* [Smashing Magazine](https://www.smashingmagazine.com/tag/javascript/)
* [JavaScript Weekly](http://javascriptweekly.com/)
* [Ng Weekly](http://www.ng-newsletter.com/)
* [Reddit JavaScript](https://www.reddit.com/r/javascript/)
* [JavaScript Jabber](https://devchat.tv/js-jabber)

### Apprendre par l'exemple

Comme toujours, la meilleure façon d'apprendre est par l'exemple.

#### Guides de style

Les guides de style JavaScript sont des ensembles de conventions de codage conçues pour aider à garder votre code lisible et maintenable.

* [Guide de style JavaScript d'AirBnB](https://github.com/airbnb/javascript)
* [Principes pour écrire du JavaScript cohérent et idiomatique](https://github.com/rwaldron/idiomatic.js/)
* [Guide de style Node](https://github.com/felixge/node-style-guide)
* [Style de codage MDN](https://developer.mozilla.org/fr/docs/Mozilla/Developer_guide/Coding_Style)

#### Bases de code

Je ne peux pas assez insister sur l'utilité de lire du bon code. Apprenez à rechercher des [dépôts pertinents](https://github.com/) sur Github chaque fois que vous apprenez quelque chose de nouveau.

* [Lodash](https://github.com/lodash/lodash)
* [Underscore](https://github.com/jashkenas/underscore)
* [Babel](https://github.com/babel/babel)
* [Ghost](https://github.com/TryGhost/Ghost)
* [NodeBB](https://github.com/NodeBB/NodeBB)
* [KeystoneJS](https://github.com/keystonejs/keystone)

### Conclusion

À la fin de ce guide, vous devriez avoir une solide compréhension des fondamentaux de JavaScript et de la façon de les appliquer au web. N'oubliez pas que ce guide vous donne une feuille de route générale. Si vous voulez devenir un héros du front-end, il est important que vous passiez du temps à travailler sur des projets pour appliquer ces concepts. Plus vous ferez de projets et plus vous serez passionné par eux, plus vous apprendrez.

Cet article est la deuxième partie de la série en deux parties. Ce qui manque à ce guide est une introduction à [Node](https://nodejs.org/en/), qui est une plateforme qui permet à JavaScript de s'exécuter sur des serveurs. À l'avenir, je pourrais écrire une troisième partie qui couvre le développement côté serveur avec Node et des choses comme les bases de données [noSQL](https://fr.wikipedia.org/wiki/NoSQL).

Si vous voulez que j'élabore sur quelque chose ou si vous avez des questions, n'hésitez pas à me laisser un mot ou à me [Tweeter](https://twitter.com/jonathanzwhite).

_P.S. Si vous avez aimé cet article, cela signifierait beaucoup si vous cliquiez sur le bouton de recommandation ou le partagez avec des amis._

Si vous voulez plus, vous pouvez me suivre sur [Twitter](https://twitter.com/JonathanZWhite) où je poste des divagations sans sens sur le design, le développement front-end, les bots et l'apprentissage automatique.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UOsjAdUZ9O0QSyfXOpQPbA.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*mxQhZLqG7l5dMLvxYAklgw.png)