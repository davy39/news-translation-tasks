---
title: Comment manipuler les classes sans jQuery en utilisant l'API classList de HTML5
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-10-03T01:58:46.000Z'
originalURL: https://freecodecamp.org/news/how-to-manipulate-classes-using-the-classlist-api-f876e2f58236
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Lk7YWiSeDYGd-ITVUXbBbA.png
tags:
- name: HTML5
  slug: html5
- name: JavaScript
  slug: javascript
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Comment manipuler les classes sans jQuery en utilisant l'API classList
  de HTML5
seo_desc: 'By Ayo Isaiah

  As a front end developer, you often need to change CSS rules based on how a user
  interacts with elements on a page.

  In the past, I relied on jQuery to handle these kinds of DOM manipulations for me.
  But in some cases, it doesn’t make se...'
---

Par Ayo Isaiah

En tant que développeur front-end, vous devez souvent changer les règles CSS en fonction de la manière dont un utilisateur interagit avec les éléments d'une page.

Dans le passé, je comptais sur jQuery pour gérer ce type de manipulations DOM pour moi. Mais dans certains cas, il n'a pas de sens d'importer toute la bibliothèque jQuery, juste pour effectuer quelques manipulations DOM de base.

Heureusement, HTML5 offre un moyen de faire cela nativement, sans avoir besoin de jQuery.

### Comment j'ai découvert la méthode classList de HTML5

Il y a quelques jours, je lisais du code. J'ai remarqué qu'un projet incluait jQuery comme dépendance, juste pour ajouter et supprimer des classes lorsque l'utilisateur cliquait sur un bouton de la page. Le code d'interaction complet ne faisait que 11 lignes de code.

J'ai trouvé étrange qu'ils fassent cela de cette manière. C'était l'équivalent d'utiliser un bazooka (jQuery) pour tuer un moustique (ajouter et supprimer des classes lors d'un clic).

![Image](https://cdn-media-1.freecodecamp.org/images/HsJD8MO76vZOEiIbpPHz8xpJVVrX5e5-w3wT)
_Le code en question_

Il m'est venu à l'esprit que j'avais probablement fait des choses similaires dans mes précédents projets de codage. J'ai donc décidé d'essayer de reproduire la même fonctionnalité en utilisant du JavaScript pur et de voir ce que je pouvais en apprendre.

Une recherche rapide a révélé plusieurs options pour faire cela en JavaScript pur. J'ai choisi la méthode _classList_ parce qu'elle est facile à comprendre et que la compatibilité entre navigateurs est assez bonne.

![Image](https://cdn-media-1.freecodecamp.org/images/xfP4t1yhn2CEkRiJLnYWath02Vo1GJPIGtQN)
_Selon [Can I Use](http://caniuse.com/#search=classList" rel="noopener" target="_blank" title="), classList fonctionne partout sauf sur Opera Mini et Internet Explorer 8._

Notez que si vous devez supporter des versions d'Internet Explorer antérieures à IE 11, vous devrez peut-être trouver une méthode alternative ou utiliser un [polyfill](https://github.com/eligrey/classList.js).

Si vous dépendez entièrement de jQuery pour la manipulation du DOM, c'est un excellent point de départ pour gagner un peu d'indépendance par rapport à jQuery.

### Qu'est-ce que l'API classList ?

L'API classList de HTML5 fournit un moyen de récupérer toutes les classes associées à un élément afin que vous puissiez utiliser JavaScript pour les modifier.

L'utilisation de la propriété DOM classList sur un élément renverra un [_DOMTokenList_](https://developer.mozilla.org/en/docs/Web/API/DOMTokenList)_._ Cela contient toutes les classes appliquées à un élément, et la propriété _length_, qui indique le nombre total de classes sur cet élément.

Voici un exemple :

```
<!-- html --><section class="content-wrapper about animated" id="about"></section>
```

```
//JavaScriptvar about = document.getElementById("about"); console.log(about.classList); //logs { 0: "content-wrapper" 1: "about" 2: "animated" length: 3 value: "content-wrapper about animated" }
```

Vous pouvez essayer ce qui précède dans votre navigateur pour voir cela en action.

![Image](https://cdn-media-1.freecodecamp.org/images/C0X8e1sHbCkCciImugkP4gANA20hq9dx8vfD)

Récupérer les classes d'un élément est bien et bon, mais ce n'est pas très utile en soi. Nous avons besoin d'un moyen de gérer et de mettre à jour ces classes. La propriété classList fournit quelques méthodes qui font exactement cela :

* **add()** : Ajoute des classes spécifiées
* **remove()** : Supprime des classes spécifiées
* **contains()** : Vérifie si la classe spécifiée existe sur l'élément
* **toggle()** : Basculer la classe spécifiée
* **index()** : retourne la classe à une position spécifiée dans la liste
* **length** : retourne le nombre de classes

Examinons chacune d'entre elles à tour de rôle.

### Ajout de classes

Ajouter une classe à un élément est simple. Il suffit d'appliquer le nom de la classe comme argument à la méthode _add()_. Notez que si le nom de la classe existe déjà sur l'élément, il ne sera pas ajouté à nouveau.

```
<!-- html --><span class="heading" id="headline"></span>
```

```
//JavaScriptdocument.getElementById("headline").classList.add("title"); //gives class="heading title"
```

Pour ajouter plusieurs classes, séparez chaque classe par une virgule :

```
<!-- html --><span class="heading" id="headline"></span>
```

```
//JavaScriptdocument.getElementById("headline").classList.add("title", "headline"); //gives class="heading title headline"
```

### Suppression de classes

Pour supprimer une classe, il suffit de passer le nom de la classe comme argument à la méthode _remove()_. Si le nom de la classe n'existe pas déjà dans le _classList_, une erreur est générée.

```
<!-- html --><header class="masthead clearfix" id="header"></header>
```

```
//JavaScriptdocument.getElementById("header").classList.remove("masthead"); //gives class="clearfix"
```

Pour supprimer plusieurs classes, séparez chaque classe par une virgule :

```
<!-- html --><header class="masthead clearfix headline" id="header"></header>
```

```
//JavaScriptdocument.getElementById("header").classList.remove("masthead", "headline"); //gives class="clearfix"
```

### Vérifier si une classe existe

En utilisant la méthode _contains()_, nous pouvons vérifier si une classe spécifiée est présente dans le _classList_ d'un élément et effectuer des opérations en fonction de la valeur de retour.

Par exemple :

```
<!-- html --><button class="hidden" id="btn">Click Me</button>
```

```
//JavaScriptvar button = document.getElementById("btn"); if (button.classList.contains("hidden")) {   //do something } else {   //do something else}
```

### Basculer les classes

Ajouter ou supprimer une classe en fonction de l'action de l'utilisateur est une chose courante à faire. C'est exactement ce que je voulais réaliser avec classList.

Vous pouvez basculer entre l'ajout et la suppression en utilisant la méthode _toggle()_.

Voici ce que j'ai finalement fait :

```
<!-- html --><div class="menu" id="menu" onclick="hasClass()"></div>
```

```
//JavaScriptvar page = document.getElementById("page"); var menu = document.getElementById("menu"); var nav = document.getElementById("navigation"); 
```

```
function hasClass() {   page.classList.toggle("open");   menu.classList.toggle("active");  nav.classList.toggle("hidden"); }
```

### Vérifier le nombre de classes

Pour savoir combien de classes sont appliquées à un élément, utilisez la propriété _length_ :

```
<!-- html --><nav class="nav hidden" id="navbar"></nav>
```

```
//JavaScriptdocument.getElementById("navbar").classList.length; // 2
```

### Conclusion

Comme vous pouvez le voir, l'API classList est facile à utiliser. Je vous encourage à commencer à explorer ses capacités dans vos propres applications.

De plus, laissez un commentaire si vous avez des questions, ou contactez-moi sur [Twitter](https://twitter.com/ayisaiah). Pour plus d'articles comme celui-ci, consultez [mon blog](https://ayoisaiah.com/blog/). Merci d'avoir lu !