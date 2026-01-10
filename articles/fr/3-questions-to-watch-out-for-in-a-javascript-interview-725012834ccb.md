---
title: 3 questions JavaScript à surveiller lors des entretiens de codage
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-03T20:25:17.000Z'
originalURL: https://freecodecamp.org/news/3-questions-to-watch-out-for-in-a-javascript-interview-725012834ccb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*pTg8YVc-Hdps3vGURqJGDQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: 3 questions JavaScript à surveiller lors des entretiens de codage
seo_desc: 'By Daniel Borowski

  JavaScript is the official language of all modern web browsers. As such, JavaScript
  questions come up in all sorts of developer interviews.

  This article isn’t about the newest JavaScript libraries, common development practices,
  or ...'
---

Par Daniel Borowski

JavaScript est le langage officiel de [tous les navigateurs web modernes](https://developer.mozilla.org/en-US/docs/Web/JavaScript). Ainsi, les questions sur JavaScript apparaissent dans toutes sortes d'entretiens pour développeurs.

Cet article ne traite pas des dernières bibliothèques JavaScript, des pratiques de développement courantes, ou de l'une des nouvelles [fonctions ES6](https://hackernoon.com/es6-features-you-need-to-know-now-b525e2b0755e#.seo0weyr4). Il s'agit plutôt de 3 choses qui reviennent généralement lors des entretiens sur JavaScript. On m'a posé ces questions, et mes amis m'ont dit qu'on les leur avait également posées.

Bien sûr, ce ne sont pas les seules 3 choses que vous devriez étudier avant un entretien JavaScript — il existe une [multitude](http://jstherightway.org/#getting-started) de [façons](https://medium.com/javascript-scene/10-interview-questions-every-javascript-developer-should-know-6fa6bdf5ad95#.7fty5p61c) de [mieux vous préparer](http://www.thatjsdude.com/interview/js2.html) pour un entretien à venir — mais voici 3 questions qu'un recruteur pourrait poser pour évaluer votre connaissance et votre compréhension du langage JavaScript et du [DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction).

Alors, commençons ! Notez que nous allons utiliser du JavaScript vanilla dans les exemples ci-dessous, car votre interlocuteur voudra généralement voir à quel point vous comprenez JavaScript et le DOM sans l'aide de bibliothèques comme jQuery.

### Question #1 : La délégation d'événements

Lors de la création d'une application, il est parfois nécessaire d'attacher des écouteurs d'événements à des boutons, du texte ou des images sur la page afin d'effectuer une action lorsque l'utilisateur interagit avec l'élément.

Si nous prenons une simple liste de tâches comme exemple, l'interviewer peut vous dire qu'il veut qu'une action se produise lorsque l'utilisateur clique sur l'un des éléments de la liste. Et il veut que vous implémentiez cette fonctionnalité en JavaScript en supposant le code HTML suivant :

```html
<ul id="todo-app">
  <li class="item">Promener le chien</li>
  <li class="item">Payer les factures</li>
  <li class="item">Préparer le dîner</li>
  <li class="item">Coder pendant une heure</li>
</ul>
```

Vous pourriez vouloir faire quelque chose comme ceci pour attacher des écouteurs d'événements aux éléments :

```js
document.addEventListener('DOMContentLoaded', function() {
  
  let app = document.getElementById('todo-app');
  let items = app.getElementsByClassName('item');
  
  // attacher un écouteur d'événement à chaque élément
  for (let item of items) {
    item.addEventListener('click', function() {
      alert('vous avez cliqué sur l\'élément : ' + item.innerHTML);
    });
  }
  
});
```

Bien que cela fonctionne techniquement, le problème est que vous attachez un écouteur d'événement à chaque élément individuellement. Cela va pour 4 éléments, mais que se passe-t-il si quelqu'un ajoute 10 000 éléments (ils peuvent avoir beaucoup de choses à faire) à leur liste de tâches ? Votre fonction créera alors 10 000 écouteurs d'événements séparés et les attachera chacun au DOM. Ce n'est pas très [efficace](https://www.kirupa.com/html5/handling_events_for_many_elements.htm).

Lors d'un entretien, il serait préférable de demander d'abord à l'interviewer quel est le nombre maximum d'éléments que l'utilisateur peut entrer. Si cela ne peut jamais dépasser 10, par exemple, alors le code ci-dessus fonctionnerait bien. Mais s'il n'y a pas de limite au nombre d'éléments que l'utilisateur peut entrer, alors vous voudrez utiliser une solution plus efficace.

Si votre application pourrait se retrouver avec des centaines d'écouteurs d'événements, la solution la plus efficace serait d'attacher **un** écouteur d'événement à l'ensemble du conteneur, puis de pouvoir accéder à chaque élément lorsqu'il est effectivement cliqué. Cela s'appelle la [délégation d'événements](https://davidwalsh.name/event-delegate), et c'est beaucoup plus efficace que d'attacher des gestionnaires d'événements séparés.

Voici le code pour la délégation d'événements :

```js
document.addEventListener('DOMContentLoaded', function() {
  
  let app = document.getElementById('todo-app');
  
  // attacher un écouteur d'événement à l'ensemble du conteneur
  app.addEventListener('click', function(e) {
    if (e.target && e.target.nodeName === 'LI') {
      let item = e.target;
      alert('vous avez cliqué sur l\'élément : ' + item.innerHTML);
    }
  });
  
});
```

### Question #2 : Utilisation d'une fermeture dans une boucle

Les fermetures sont parfois abordées lors d'un entretien afin que l'interviewer puisse évaluer votre familiarité avec le langage et savoir quand implémenter une fermeture.

Une fermeture est essentiellement lorsque qu'une [fonction interne a accès](https://medium.com/javascript-scene/master-the-javascript-interview-what-is-a-closure-b2f0d2152b36#.44xk49tyt) à des variables en dehors de sa portée. Les fermetures peuvent être utilisées pour des choses comme [l'implémentation de la confidentialité](https://medium.com/written-in-code/practical-uses-for-closures-c65640ae7304#.70gp35hbn) et la création de [fabriques de fonctions](https://medium.com/javascript-scene/javascript-factory-functions-vs-constructor-functions-vs-classes-2f22ceddf33e#.1817w0lmb). Une question courante d'entretien concernant l'utilisation des fermetures est quelque chose comme ceci :

_Écrivez une fonction qui parcourra une liste d'entiers et imprimera l'index de chaque élément après un délai de 3 secondes._

Une implémentation courante (incorrecte) que j'ai vue pour ce problème ressemble à ceci :

```js
const arr = [10, 12, 15, 21];
for (var i = 0; i < arr.length; i++) {
  setTimeout(function() {
    console.log('L\'index de ce nombre est : ' + i);
  }, 3000);
}
```

Si vous exécutez ceci, vous verrez que vous obtenez en réalité le **4** imprimé à chaque fois au lieu des **0, 1, 2, 3** attendus après un délai de 3 secondes.

Pour identifier correctement pourquoi cela se produit, il serait utile de comprendre pourquoi cela se produit en JavaScript, ce qui est exactement ce que l'interviewer essaie de tester.

La raison en est que la fonction `setTimeout` crée une fonction (la fermeture) qui a accès à sa portée externe, qui est la boucle contenant l'index `i`. Après que 3 secondes se soient écoulées, la fonction est exécutée et imprime la valeur de `i`, qui à la fin de la boucle est à 4 car elle passe par 0, 1, 2, 3, 4 et la boucle s'arrête enfin à 4.

Il existe en réalité [plusieurs façons](http://stackoverflow.com/questions/3572480/please-explain-the-use-of-javascript-closures-in-loops) d'[écrire correctement](https://coderbyte.com/algorithm/3-common-javascript-closure-questions) la fonction pour ce problème. En voici deux :

```js
const arr = [10, 12, 15, 21];
for (var i = 0; i < arr.length; i++) {
  // passer la variable i pour que chaque fonction 
  // ait accès à l'index correct
  setTimeout(function(i_local) {
    return function() {
      console.log('L\'index de ce nombre est : ' + i_local);
    }
  }(i), 3000);
}
```

```js
const arr = [10, 12, 15, 21];
for (let i = 0; i < arr.length; i++) {
  // en utilisant la syntaxe let de ES6, elle crée une nouvelle liaison
  // à chaque fois que la fonction est appelée
  // lire plus ici : http://exploringjs.com/es6/ch_variables.html#sec_let-const-loop-heads
  setTimeout(function() {
    console.log('L\'index de ce nombre est : ' + i);
  }, 3000);
}
```

### Question #3 : Le débogage

Il existe certains événements du navigateur qui peuvent se déclencher de nombreuses fois en un court laps de temps très rapidement, comme le redimensionnement d'une fenêtre ou le défilement d'une page. Si vous attachez un écouteur d'événement à l'événement de défilement de la fenêtre par exemple, et que l'utilisateur fait défiler la page très rapidement, votre événement peut se déclencher des milliers de fois en l'espace de 3 secondes. Cela peut causer de sérieux problèmes de performance.

Si vous discutez de la création d'une application lors d'un entretien, et que des événements comme le défilement, le redimensionnement de la fenêtre ou la pression de touches sont abordés, assurez-vous de mentionner le débogage et/ou le throttling comme moyen d'améliorer la vitesse et les performances de la page. Un exemple réel tiré de cet [article invité sur css-tricks](https://css-tricks.com/debouncing-throttling-explained-examples/) :

> En 2011, un problème est apparu sur le site web de Twitter : lorsque vous faisiez défiler votre fil Twitter, il devenait lent et peu réactif. John Resig a publié [un article de blog sur le problème](http://ejohn.org/blog/learning-from-twitter) où il était expliqué à quel point il est mauvais d'attacher directement des fonctions coûteuses à l'événement `scroll`.

Le débogage est un moyen de résoudre ce problème en limitant le temps qui doit s'écouler jusqu'à ce qu'une fonction soit appelée à nouveau. Une implémentation correcte du débogage regrouperait donc plusieurs appels de fonction en un seul et ne l'exécuterait qu'une seule fois après qu'un certain temps se soit écoulé. Voici une implémentation en JavaScript pur qui utilise des sujets tels que [la portée](https://toddmotto.com/everything-you-wanted-to-know-about-javascript-scope/), les fermetures, [this](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this), et [les événements de timing](http://www.w3schools.com/jsref/met_win_settimeout.asp) :

```js
// fonction de débogage qui enveloppera notre événement
function debounce(fn, delay) {
  // maintenir un minuteur
  let timer = null;
  // fonction de fermeture qui a accès au minuteur
  return function() {
    // obtenir la portée et les paramètres de la fonction 
    // via 'this' et 'arguments'
    let context = this;
    let args = arguments;
    // si l'événement est appelé, effacer le minuteur et recommencer
    clearTimeout(timer);
    timer = setTimeout(function() {
      fn.apply(context, args);
    }, delay);
  }
}
```

Cette fonction — lorsqu'elle est enveloppée autour d'un événement — ne s'exécutera qu'après qu'un certain temps se soit écoulé.

Vous utiliseriez cette fonction comme suit :

```js
// fonction à appeler lorsque l'utilisateur fait défiler
function foo() {
  console.log('Vous faites défiler !');
}

// envelopper notre fonction dans un débogage pour qu'elle se déclenche une fois que 2 secondes se sont écoulées
let elem = document.getElementById('container');
elem.addEventListener('scroll', debounce(foo, 2000));
```

Le throttling est une autre technique similaire au débogage, sauf qu'au lieu d'attendre qu'un certain temps se soit écoulé avant d'appeler une fonction, le throttling répartit simplement les appels de fonction sur un intervalle de temps plus long. Ainsi, si un événement se produit 10 fois en 100 millisecondes, le throttling pourrait répartir chacun des appels de fonction pour qu'ils soient exécutés une fois toutes les 2 secondes au lieu de tous se déclencher en 100 millisecondes.

Pour plus d'informations sur le débogage et le throttling, les articles et tutoriels suivants peuvent être utiles :

* [Throttling et Debouncing en JavaScript](https://medium.com/@_jh3y/throttling-and-debouncing-in-javascript-b01cad5c8edf#.ly8uqz8v4)
* [La différence entre Throttling et Debouncing](https://css-tricks.com/the-difference-between-throttling-and-debouncing/)
* [Exemples de Throttling et Debouncing](https://css-tricks.com/debouncing-throttling-explained-examples/)
* [Article de blog de Remy Sharp sur le Throttling des appels de fonction](https://remysharp.com/2010/07/21/throttling-function-calls)

Si vous avez aimé lire cet article, alors vous aimerez peut-être lire les tutoriels JavaScript et résoudre certains des défis de codage JavaScript que j'héberge sur [Coderbyte](https://www.coderbyte.com). J'adorerais avoir votre avis !