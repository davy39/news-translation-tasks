---
title: Comment créer une API fetch personnalisée à partir de XMLHttpRequest
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-24T08:18:41.000Z'
originalURL: https://freecodecamp.org/news/create-a-custom-fetch-api-from-xmlhttprequest-2cad1b84f07c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XXsfkhk3zt2Y70p2FFeutQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: 'tech '
  slug: tech
seo_title: Comment créer une API fetch personnalisée à partir de XMLHttpRequest
seo_desc: 'By Samuel Omole

  What is your worst nightmare?

  That sounded dark, but it’s not a rhetorical question. I really want to know because
  I am about to tell you mine. Along the way, we will learn some things like how the
  fetch API works and also how functio...'
---

Par Samuel Omole

Quel est votre pire cauchemar ?

Cela semble sombre, mais ce n'est pas une question rhétorique. Je veux vraiment savoir parce que je suis sur le point de vous dire le mien. En chemin, nous apprendrons quelques choses comme le fonctionnement de l'API fetch et aussi comment fonctionnent les constructeurs de fonctions.

Désolé, je m'égare, revenons à mon pire cauchemar. Si vous m'aviez posé cette question la semaine dernière, cela aurait été la liste ci-dessous, dans aucun ordre particulier :

* Écrire la syntaxe Pre-ES6
* Pas d'API fetch
* Pas de Transpiler (Babel/Typescript)
* [Uncle Bob](https://en.wikipedia.org/wiki/Robert_C._Martin) a dit que je suis une déception (Je plaisante)

Si votre liste correspond à la mienne, alors je dois dire que vous êtes une personne très étrange. Par chance, j'ai été appelé à travailler sur un projet qui a donné vie à ma liste de cauchemars (à l'exclusion du dernier). Je devais ajouter une nouvelle fonctionnalité à l'application. C'était une base de code héritée qui utilisait purement la syntaxe pre-es6 et XMLHttpRequest (l'horreur) pour ses requêtes AJAX.

Alors, dans un effort pour rendre l'expérience plus supportable, j'ai décidé de créer une fonction qui abstrait toutes les requêtes AJAX que je devrais faire et expose des API qui imitent la nouvelle [API fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) (enfin, pas vraiment). C'est aussi après avoir regardé la vidéo [Javascript: The new hard parts](https://frontendmasters.com/courses/javascript-new-hard-parts/) sur frontend masters où une explication amazing du fonctionnement de l'API fetch sous le capot a été donnée. Commençons.

D'abord, j'ai dû chercher comment [XMLHttpRequest](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest) fonctionne. Ensuite, j'ai commencé à écrire la fonction. Ma première itération ressemblait à ceci :

```javascript
"use strict";


function fetch() {
  var url = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : '';
  var options = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : {};

var xhr = new XMLHttpRequest();
  var onFufillment = [];
  var onError = [];
  var onCompletion = [];
  var method = "GET" || options.method;
  xhr.onreadystatechange = function () {
    var _data = this;
    if (this.readyState == 4 && this.status == 200) {
      // Action à effectuer lorsque le document est lu;
      onFufillment.forEach(function (callback) {
          callback(_data);
      });
     onCompletion.forEach(function (callback) {
        callback(_data);
      });
    } else if (this.readyState == 4 && this.status !== 200) {
      onError.forEach(function (callback) {
        callback(_data);
      });
      onCompletion.forEach(function (callback) {
        callback(_data);
      });
    }
  };
  xhr.open(method, url, true);
  xhr.send();


return {
    then: function then(fufillmentFunction) {
      onFufillment.push(fufillmentFunction);
    },
    catch: function _catch(errorFunction) {
      onError.push(errorFunction);
    },
    finally: function _finally(completionFunction) {
      onCompletion.push(completionFunction);
    }
  };
}
```

Laissez-moi expliquer ce que fait la fonction :

* Nous vérifions si l'argument `url` est passé dans la fonction. Par défaut, une chaîne vide si rien n'est passé
* Nous faisons de même pour l'argument `options`. Par défaut, un objet vide si rien n'est passé
* Ensuite, nous créons une nouvelle instance de XMLHttpRequest
* Nous créons 4 variables `onFufillment, onError, onCompletion et method`
* `onFufillment` est un tableau qui stocke toutes les fonctions passées dans la méthode `then`
* `onError` est un tableau qui stocke toutes les fonctions passées dans la méthode `catch`
* `onCompletion` est un tableau qui stocke toutes les fonctions passées dans la méthode `finally`
* `method` est utilisé pour stocker la méthode HTTP qui sera utilisée, par défaut `GET`
* Nous passons ensuite une fonction dans la méthode `onreadystatechange` de `xhr` qui sera appelée lorsque l'état de la requête change
* Dans la fonction, nous sauvegardons `this` dans une variable `_data` afin qu'elle puisse être passée dans les fonctions forEach sans perdre son contexte (je sais que `this` est ennuyeux)
* Nous vérifions ensuite si la requête est terminée (`readyState == 4`) et si la requête est réussie, puis nous parcourons les tableaux `onFufillment et onCompletion`, appelant chaque fonction et passant `_data` dedans
* Si la requête échoue, nous faisons de même avec les tableaux `onCompletion et onError`
* Ensuite, nous envoyons la requête avec les paramètres passés
* Après cela, nous retournons un objet contenant trois fonctions, then. `catch et finally` qui ont les mêmes noms que l'API fetch.
* `catch` pousse la fonction qui est passée en argument dans le tableau `onError`
* `then` fait de même avec le tableau `onFufillment`
* `finally` fait de même avec le tableau `onCompletion`

L'utilisation de cette API ressemblera à ceci :

```javascript
var futureData = fetch('https://jsonplaceholder.typicode.com/todos/2');
futureData.then(function(data){
  console.log(data)
})

futureData.finally(function(response){
  console.log(response);
});

futureData.catch(function(error){
  console.log(error);
})
```

Cela fonctionne !!! Mais pas près de l'implémentation réelle de fetch. Pouvez-nous faire mieux ? Bien sûr, nous pouvons. Nous pouvons encore ajouter plus de fonctionnalités à la fonction. Nous pourrions la rendre chaînable, c'est-à-dire, nous pouvons lui donner la capacité de chaîner les méthodes ensemble.

À la deuxième itération, voici à quoi cela ressemble :

```javascript
"use strict";

function fetch() {
  var url = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : '';
  var options = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : {};
var xhr = new XMLHttpRequest();
  var onFufillment = [];
  var onError = [];
  var onCompletion = [];
  var method = "GET" || options.method;
  xhr.onreadystatechange = function () {
    var _data = this;
    if (this.readyState == 4 && this.status == 200) {
      // Action à effectuer lorsque le document est lu;
      onFufillment.forEach(function (callback) {
          callback(_data);
      });
     onCompletion.forEach(function (callback) {
        callback(_data);
      });
    } else if (this.readyState == 4 && this.status !== 200) {
      onError.forEach(function (callback) {
        callback(_data);
      });
      onCompletion.forEach(function (callback) {
        callback(_data);
      });
    }
  };
  xhr.open(method, url, true);
  xhr.send();


	return {
    	then: function then(fufillmentFunction) {
          onFufillment.push(fufillmentFunction);
          return this;
   		},
    	catch: function _catch(errorFunction) {
      	  onError.push(errorFunction);
      	  return this;
      },
        finally: function _finally(completionFunction) {
         onCompletion.push(completionFunction);
         return this;
    }
  };
}
```

L'utilisation de l'API ressemblera à ceci :

```javascript
var futureData = fetch('https://jsonplaceholder.typicode.com/todos/2');


futureData.then(function(data){
  console.log(data)
}).then(function(response){
  console.log(response);
}).catch(function(error){
  console.log(error);
});
```

Qu'a-t-il fait ? La seule différence dans la deuxième itération était dans `then, catch et finally` où j'ai simplement retourné `this` ce qui signifie que chaque fonction se retourne elle-même, permettant ainsi d'être chaînée (partiellement).

Mieux, non ? Mais pouvons-nous faire mieux ? Bien sûr, nous pouvons. L'objet retourné peut être mis dans le prototype de la fonction afin que nous puissions économiser de la mémoire dans une situation où la fonction est utilisée plusieurs fois.

Voici à quoi cela ressemble à la troisième itération :

```javascript
"use strict";
function fetch() {
  var fetchMethod = Object.create(fetch.prototype);
  var url = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : '';
  var options = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : {};
var xhr = new XMLHttpRequest();
  fetchMethod.onFufillment = [];
  fetchMethod.onError = [];
  fetchMethod.onCompletion = [];
  var method = "GET" || options.method;
  xhr.onreadystatechange = function () {
    var _data = this;
    if (this.readyState == 4 && this.status == 200) {
      // Action à effectuer lorsque le document est lu;
      fetchMethod.onFufillment.forEach(function (callback) {
          callback(_data);
      });
     fetchMethod.onCompletion.forEach(function (callback) {
        callback(_data);
      });
    } else if (this.readyState == 4 && this.status !== 200) {
      fetchMethod.onError.forEach(function (callback) {
        callback(_data);
      });
      fetchMethod.onCompletion.forEach(function (callback) {
        callback(_data);
      });
    }
  };
  xhr.open(method, url, true);
  xhr.send();
  return fetchMethod;
};
fetch.prototype.then = function(fufillmentFunction) {
      this.onFufillment.push(fufillmentFunction);
      return this;
};
fetch.prototype.catch = function(errorFunction) {
      this.onError.push(errorFunction);
      return this;
};
fetch.prototype.finally = function(completionFunction) {
      this.onCompletion.push(completionFunction);
      return this;
};
```

Cette version déplace essentiellement la fonction retournée dans le prototype de fetch. Si vous ne comprenez pas cette déclaration, je vous recommande de consulter cet article sur le [prototype de Javascript](https://dev.to/tylermcginnis/a-beginners-guide-to-javascripts-prototype-5kk) (Merci, Tyler McGinnis).

Est-ce une amélioration ? Oui !!! Pouvez-nous faire mieux ? Bien sûr, nous pouvons. Nous pouvons utiliser le mot-clé `new` à notre avantage ici et supprimer l'instruction de retour explicite.

La prochaine itération ressemblera à ceci :

```javascript
"use strict";
function Fetch() {
  var url = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : '';
  var options = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : {};
  var xhr = new XMLHttpRequest();
  this.onFufillment = [];
  this.onError = [];
  this.onCompletion = [];
  var method = "GET" || options.method;
  var internalFetchContext = this;
  xhr.onreadystatechange = function () {
    var _data = this;
    if (this.readyState == 4 && this.status == 200) {
      // Action à effectuer lorsque le document est lu;
      internalFetchContext.onFufillment.forEach(function (callback) {
          callback(_data);
      });
     internalFetchContext.onCompletion.forEach(function (callback) {
        callback(_data);
      });
    } else if (this.readyState == 4 && this.status !== 200) {
      internalFetchContext.onError.forEach(function (callback) {
        callback(_data);
      });
      internalFetchContext.onCompletion.forEach(function (callback) {
        callback(_data);
      });
    }
  };
  xhr.open(method, url, true);
  xhr.send();
};
Fetch.prototype.then = function(fufillmentFunction) {
      this.onFufillment.push(fufillmentFunction);
      return this;
};
Fetch.prototype.catch = function(errorFunction) {
      this.onError.push(errorFunction);
      return this;
};
Fetch.prototype.finally = function(completionFunction) {
      this.onCompletion.push(completionFunction);
      return this;
};
```

Laissez-moi expliquer les changements :

* J'ai changé le nom de la fonction de fetch à Fetch, c'est juste une convention lors de l'utilisation du mot-clé `new`
* Puisque j'utilise le mot-clé `new`, je peux alors sauvegarder les différents tableaux créés dans le contexte `this`.
* Parce que la fonction passée dans `onreadystatechange` a son propre contexte, j'ai dû sauvegarder le `this` original dans sa propre variable pour pouvoir l'appeler dans la fonction (je sais, `this` peut être ennuyeux)
* J'ai converti les fonctions de prototype au nouveau nom de fonction.

L'utilisation ressemblera à ceci :

```javascript
var futureData = new 

Fetch('https://jsonplaceholder.typicode.com/todos/1');
futureData.then(function(data){
  console.log(data)
}).then(function(response){
  console.log(response);
}).catch(function(error){
  console.log(error);
})
```

Voilà ! C'était vraiment amusant. Mais pouvons-nous faire mieux ? Bien sûr, nous pouvons.

Mais je vais vous laisser cela. J'adorerais voir votre propre implémentation de l'API dans les commentaires ci-dessous.

Si vous avez aimé l'article (et même si ce n'était pas le cas), j'apprécierais un applaudissement (ou 50) de votre part. Merci.