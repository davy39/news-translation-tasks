---
title: 'Modules JavaScript : Un guide pour débutants'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-01-22T16:10:07.000Z'
originalURL: https://freecodecamp.org/news/javascript-modules-a-beginner-s-guide-783f7d7a5fcc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*bcZz-qb_DNpvrNNwQBhQmQ.jpeg
tags:
- name: education
  slug: education
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: 'Modules JavaScript : Un guide pour débutants'
seo_desc: 'By Preethi Kasireddy

  If you’re a newcomer to JavaScript, jargon like “module bundlers vs. module loaders,”
  “Webpack vs. Browserify” and “AMD vs. CommonJS” can quickly become overwhelming.

  The JavaScript module system may be intimidating, but understa...'
---

Par Preethi Kasireddy

Si vous êtes nouveau dans le monde de JavaScript, le jargon comme « module bundlers vs. module loaders », « Webpack vs. Browserify » et « AMD vs. CommonJS » peut rapidement devenir accablant.

Le système de modules JavaScript peut sembler intimidant, mais le comprendre est vital pour les développeurs web.

Dans cet article, je vais démystifier ces termes à la mode pour vous en anglais simple (et quelques exemples de code). J'espère que vous le trouverez utile !

_Note : pour simplifier, cela sera divisé en deux sections : La Partie 1 expliquera ce que sont les modules et pourquoi nous les utilisons. La Partie 2 (publiée la semaine prochaine) expliquera ce que signifie regrouper des modules et les différentes façons de le faire._

### Partie 1 : Quelqu'un peut-il m'expliquer à nouveau ce que sont les modules ?

Les bons auteurs divisent leurs livres en chapitres et sections ; les bons programmeurs divisent leurs programmes en modules.

Comme un chapitre de livre, les modules sont simplement des regroupements de mots (ou de code, dans ce cas).

Cependant, les bons modules sont très autonomes avec des fonctionnalités distinctes, permettant de les mélanger, supprimer ou ajouter selon les besoins, sans perturber le système dans son ensemble.

### Pourquoi utiliser des modules ?

Il y a de nombreux avantages à utiliser des modules plutôt qu'une base de code tentaculaire et interdépendante. Les plus importants, à mon avis, sont :

**1) Maintenabilité :** Par définition, un module est autonome. Un module bien conçu vise à réduire les dépendances aux autres parties de la base de code autant que possible, afin qu'il puisse évoluer et s'améliorer indépendamment. Mettre à jour un seul module est beaucoup plus facile lorsque le module est découplé des autres parties du code.

Pour revenir à notre exemple de livre, si vous vouliez mettre à jour un chapitre de votre livre, ce serait un cauchemar si un petit changement dans un chapitre vous obligeait à modifier tous les autres chapitres également. Au lieu de cela, vous voudriez écrire chaque chapitre de manière à ce que les améliorations puissent être apportées sans affecter les autres chapitres.

**2) Espace de noms :** En JavaScript, les variables en dehors de la portée d'une fonction de premier niveau sont globales (c'est-à-dire que tout le monde peut y accéder). À cause de cela, il est courant d'avoir une « pollution de l'espace de noms », où des codes complètement non liés partagent des variables globales.

Partager des variables globales entre des codes non liés est un grand [non-non en développement](http://c2.com/cgi/wiki?GlobalVariablesAreBad).

Comme nous le verrons plus tard dans cet article, les modules nous permettent d'éviter la pollution de l'espace de noms en créant un espace privé pour nos variables.

**3) Réutilisabilité :** Soyons honnêtes ici : nous avons tous copié du code que nous avions précédemment écrit dans de nouveaux projets à un moment ou à un autre. Par exemple, imaginons que vous avez copié certaines méthodes utilitaires que vous avez écrites d'un projet précédent vers votre projet actuel.

C'est très bien, mais si vous trouvez une meilleure façon d'écrire une partie de ce code, vous devrez revenir en arrière et vous souvenir de le mettre à jour partout ailleurs où vous l'avez écrit.

C'est évidemment une énorme perte de temps. Ne serait-il pas beaucoup plus facile s'il y avait — attendez-le — un module que nous pouvons réutiliser encore et encore ?

### Comment pouvez-vous incorporer des modules ?

Il existe de nombreuses façons d'incorporer des modules dans vos programmes. Passons en revue quelques-unes :

#### Modèle de module

Le modèle de module est utilisé pour imiter le concept de classes (puisque JavaScript ne supporte pas nativement les classes) afin que nous puissions stocker à la fois des méthodes et des variables publiques et privées à l'intérieur d'un seul objet — similaire à la façon dont les classes sont utilisées dans d'autres langages de programmation comme Java ou Python. Cela nous permet de créer une API publique pour les méthodes que nous voulons exposer au monde, tout en encapsulant les variables et méthodes privées dans une portée de fermeture.

Il existe plusieurs façons d'accomplir le modèle de module. Dans ce premier exemple, j'utiliserai une fermeture anonyme. Cela nous aidera à atteindre notre objectif en mettant tout notre code dans une fonction anonyme. (Rappelez-vous : en JavaScript, les fonctions sont le seul moyen de créer une nouvelle portée.)

**Exemple 1 : Fermeture anonyme**

```js
(function () {
  // Nous gardons ces variables privées à l'intérieur de cette portée de fermeture
  
  var myGrades = [93, 95, 88, 0, 55, 91];
  
  var average = function() {
    var total = myGrades.reduce(function(accumulator, item) {
      return accumulator + item}, 0);
    
      return 'Votre moyenne est de ' + total / myGrades.length + '.';
  }

  var failing = function(){
    var failingGrades = myGrades.filter(function(item) {
      return item < 70;});
      
    return 'Vous avez échoué ' + failingGrades.length + ' fois.';
  }

  console.log(failing());

}());

// 'Vous avez échoué 2 fois.'
```

Avec cette construction, notre fonction anonyme a son propre environnement d'évaluation ou « fermeture », et nous l'évaluons immédiatement. Cela nous permet de masquer les variables de l'espace de noms parent (global).

Ce qui est bien avec cette approche, c'est que vous pouvez utiliser des variables locales à l'intérieur de cette fonction sans écraser accidentellement les variables globales existantes, tout en ayant toujours accès aux variables globales, comme ceci :

```js
var global = 'Bonjour, je suis une variable globale :)';

(function () {
  // Nous gardons ces variables privées à l'intérieur de cette portée de fermeture
  
  var myGrades = [93, 95, 88, 0, 55, 91];
  
  var average = function() {
    var total = myGrades.reduce(function(accumulator, item) {
      return accumulator + item}, 0);
    
    return 'Votre moyenne est de ' + total / myGrades.length + '.';
  }

  var failing = function(){
    var failingGrades = myGrades.filter(function(item) {
      return item < 70;});
      
    return 'Vous avez échoué ' + failingGrades.length + ' fois.';
  }

  console.log(failing());
  console.log(global);
}());

// 'Vous avez échoué 2 fois.'
// 'Bonjour, je suis une variable globale :)'
```

Notez que les parenthèses autour de la fonction anonyme sont requises, car les instructions qui commencent par le mot-clé _function_ sont toujours considérées comme des déclarations de fonction (rappelons que vous ne pouvez pas avoir de déclarations de fonction sans nom en JavaScript). Par conséquent, les parenthèses environnantes créent une expression de fonction à la place. Si vous êtes curieux, vous pouvez [en lire plus ici](http://stackoverflow.com/questions/1634268/explain-javascripts-encapsulated-anonymous-function-syntax).

**Exemple 2 : Importation globale**   
Une autre approche populaire utilisée par des bibliothèques comme [jQuery](https://github.com/jquery/jquery/tree/master/src) est l'importation globale. Elle est similaire à la fermeture anonyme que nous venons de voir, sauf que maintenant nous passons les globaux en tant que paramètres :

```js
(function (globalVariable) {

  // Gardez cette variable privée à l'intérieur de cette portée de fermeture
  var privateFunction = function() {
    console.log('Chut, ceci est privé !');
  }

  // Exposez les méthodes ci-dessous via l'interface globalVariable tout
  // en masquant l'implémentation de la méthode dans le
  // bloc de fonction()

  globalVariable.each = function(collection, iterator) {
    if (Array.isArray(collection)) {
      for (var i = 0; i < collection.length; i++) {
        iterator(collection[i], i, collection);
      }
    } else {
      for (var key in collection) {
        iterator(collection[key], key, collection);
      }
    }
  };

  globalVariable.filter = function(collection, test) {
    var filtered = [];
    globalVariable.each(collection, function(item) {
      if (test(item)) {
        filtered.push(item);
      }
    });
    return filtered;
  };

  globalVariable.map = function(collection, iterator) {
    var mapped = [];
    globalUtils.each(collection, function(value, key, collection) {
      mapped.push(iterator(value));
    });
    return mapped;
  };

  globalVariable.reduce = function(collection, iterator, accumulator) {
    var startingValueMissing = accumulator === undefined;

    globalVariable.each(collection, function(item) {
      if(startingValueMissing) {
        accumulator = item;
        startingValueMissing = false;
      } else {
        accumulator = iterator(accumulator, item);
      }
    });

    return accumulator;

  };

 }(globalVariable));
  
```

Dans cet exemple, **_globalVariable_** est la seule variable qui est globale. L'avantage de cette approche par rapport aux fermetures anonymes est que vous déclarez les variables globales dès le début, ce qui rend les choses cristallines pour les personnes lisant votre code.

**Exemple 3 : Interface d'objet**  
Une autre approche consiste à créer des modules en utilisant une interface d'objet autonome, comme ceci :

```js
var myGradesCalculate = (function () {
    
  // Gardez cette variable privée à l'intérieur de cette portée de fermeture
  var myGrades = [93, 95, 88, 0, 55, 91];

  // Exposez ces fonctions via une interface tout en masquant
  // l'implémentation du module dans le bloc de fonction()

  return {
    average: function() {
      var total = myGrades.reduce(function(accumulator, item) {
        return accumulator + item;
        }, 0);
        
      return 'Votre moyenne est de ' + total / myGrades.length + '.';
    },

    failing: function() {
      var failingGrades = myGrades.filter(function(item) {
          return item < 70;
        });

      return 'Vous avez échoué ' + failingGrades.length + ' fois.';
    }
  }
})();

myGradesCalculate.failing(); // 'Vous avez échoué 2 fois.' 
myGradesCalculate.average(); // 'Votre moyenne est de 70,33333333333333.'
```

Comme vous pouvez le voir, cette approche nous permet de décider quelles variables/méthodes nous voulons garder privées (par exemple, **_myGrades_**) et quelles variables/méthodes nous voulons exposer en les mettant dans l'instruction return (par exemple, **_average_** & **_failing_**).

**Exemple 4 : Modèle de module révélateur**  
Cela est très similaire à l'approche ci-dessus, sauf qu'il garantit que toutes les méthodes et variables sont gardées privées jusqu'à ce qu'elles soient explicitement exposées :

```js
var myGradesCalculate = (function () {
    
  // Gardez cette variable privée à l'intérieur de cette portée de fermeture
  var myGrades = [93, 95, 88, 0, 55, 91];
  
  var average = function() {
    var total = myGrades.reduce(function(accumulator, item) {
      return accumulator + item;
      }, 0);
      
    return 'Votre moyenne est de ' + total / myGrades.length + '.';
  };

  var failing = function() {
    var failingGrades = myGrades.filter(function(item) {
        return item < 70;
      });

    return 'Vous avez échoué ' + failingGrades.length + ' fois.';
  };

  // Révélez explicitement les pointeurs publics vers les fonctions privées 
  // que nous voulons révéler publiquement

  return {
    average: average,
    failing: failing
  }
})();

myGradesCalculate.failing(); // 'Vous avez échoué 2 fois.' 
myGradesCalculate.average(); // 'Votre moyenne est de 70,33333333333333.'
```

Cela peut sembler beaucoup à assimiler, mais ce n'est que la partie émergée de l'iceberg en ce qui concerne les modèles de modules. Voici quelques-unes des ressources que j'ai trouvées utiles dans mes propres explorations :

* [Learning JavaScript Design Patterns](https://addyosmani.com/resources/essentialjsdesignpatterns/book/#modulepatternjavascript) par Addy Osmani : une mine d'informations dans une lecture impressionnamment succincte
* [Adequately Good par Ben Cherry](http://www.adequatelygood.com/JavaScript-Module-Pattern-In-Depth.html) : un aperçu utile avec des exemples d'utilisation avancée du modèle de module
* [Blog de Carl Danley](https://carldanley.com/js-module-pattern/) : aperçu du modèle de module et ressources pour d'autres modèles JavaScript.

### CommonJS et AMD

Les approches ci-dessus ont toutes un point commun : l'utilisation d'une seule variable globale pour envelopper son code dans une fonction, créant ainsi un espace de noms privé pour elle-même en utilisant une portée de fermeture.

Bien que chaque approche soit efficace à sa manière, elles ont leurs inconvénients.

Tout d'abord, en tant que développeur, vous devez connaître le bon ordre de dépendance pour charger vos fichiers. Par exemple, imaginons que vous utilisez Backbone dans votre projet, vous incluez donc la balise de script pour le code source de Backbone dans votre fichier.

Cependant, comme Backbone a une dépendance forte à Underscore.js, la balise de script pour le fichier Backbone ne peut pas être placée avant le fichier Underscore.js.

En tant que développeur, gérer les dépendances et faire en sorte que ces choses soient correctes peut parfois être un casse-tête.

Un autre inconvénient est qu'ils peuvent encore conduire à des collisions de noms. Par exemple, que se passe-t-il si deux de vos modules ont le même nom ? Ou si vous avez deux versions d'un module, et que vous avez besoin des deux ?

Vous vous demandez probablement : pouvons-nous concevoir un moyen de demander l'interface d'un module sans passer par la portée globale ?

Heureusement, la réponse est oui.

Il existe deux approches populaires et bien implémentées : CommonJS et AMD.

#### CommonJS

CommonJS est un groupe de travail bénévole qui conçoit et implémente des API JavaScript pour déclarer des modules.

Un module CommonJS est essentiellement une pièce réutilisable de JavaScript qui exporte des objets spécifiques, les rendant disponibles pour que d'autres modules puissent les _requérir_ dans leurs programmes. Si vous avez programmé en Node.js, vous serez très familier avec ce format.

Avec CommonJS, chaque fichier JavaScript stocke les modules dans son propre contexte de module unique (comme s'il était enveloppé dans une fermeture). Dans cette portée, nous utilisons l'objet _module.exports_ pour exposer les modules, et _require_ pour les importer.

Lorsque vous définissez un module CommonJS, cela peut ressembler à ceci :

```js
function myModule() {
  this.hello = function() {
    return 'bonjour !';
  }

  this.goodbye = function() {
    return 'au revoir !';
  }
}

module.exports = myModule;
```

Nous utilisons l'objet spécial module et plaçons une référence de notre fonction dans _module.exports_. Cela permet au système de modules CommonJS de savoir ce que nous voulons exposer afin que d'autres fichiers puissent le consommer.

Ensuite, lorsque quelqu'un veut utiliser _myModule_, il peut le requérir dans son fichier, comme ceci :

```js
var myModule = require('myModule');

var myModuleInstance = new myModule();
myModuleInstance.hello(); // 'bonjour !'
myModuleInstance.goodbye(); // 'au revoir !'
```

Il y a deux avantages évidents à cette approche par rapport aux modèles de modules que nous avons discutés auparavant :

1. Éviter la pollution de l'espace de noms global  
2. Rendre nos dépendances explicites

De plus, la syntaxe est très compacte, ce que j'adore personnellement.

Une autre chose à noter est que CommonJS adopte une approche « serveur d'abord » et charge les modules de manière synchrone. Cela compte parce que si nous avons trois autres modules que nous devons _requérir_, il les chargera un par un.

Maintenant, cela fonctionne très bien sur le serveur, mais malheureusement, cela rend plus difficile l'utilisation lors de l'écriture de JavaScript pour le navigateur. Il suffit de dire que lire un module depuis le web prend _beaucoup_ plus de temps que de lire depuis le disque. Tant que le script pour charger un module est en cours d'exécution, il bloque le navigateur de faire autre chose jusqu'à ce qu'il ait fini de charger. Il se comporte ainsi parce que le thread JavaScript s'arrête jusqu'à ce que le code soit chargé. (Je couvrirai comment nous pouvons contourner ce problème dans la Partie 2 lorsque nous discuterons du regroupement de modules. Pour l'instant, c'est tout ce que nous devons savoir).

#### AMD

CommonJS est très bien, mais que se passe-t-il si nous voulons charger des modules de manière asynchrone ? La réponse s'appelle Asynchronous Module Definition, ou AMD en abrégé.

Charger des modules en utilisant AMD ressemble à ceci :

```js
define(['myModule', 'myOtherModule'], function(myModule, myOtherModule) {
  console.log(myModule.hello());
});
```

Ce qui se passe ici, c'est que la fonction **_define_** prend en premier argument un tableau de chacune des dépendances du module. Ces dépendances sont chargées en arrière-plan (de manière non bloquante), et une fois chargées, **_define_** appelle la fonction de rappel qui lui a été donnée.

Ensuite, la fonction de rappel prend, en arguments, les dépendances qui ont été chargées — dans notre cas, **_myModule_** et **_myOtherModule_** — permettant à la fonction d'utiliser ces dépendances. Enfin, les dépendances elles-mêmes doivent également être définies en utilisant le mot-clé **_define_**.

Par exemple, **_myModule_** pourrait ressembler à ceci :

```js
define([], function() {

  return {
    hello: function() {
      console.log('bonjour');
    },
    goodbye: function() {
      console.log('au revoir');
    }
  };
});
```

Ainsi, contrairement à CommonJS, AMD adopte une approche « navigateur d'abord » avec un comportement asynchrone pour accomplir la tâche. (Notez qu'il y a beaucoup de gens qui croient fermement que le chargement dynamique des fichiers pièce par pièce au fur et à mesure que le code commence à s'exécuter n'est pas favorable, ce que nous explorerons davantage dans la prochaine section sur la construction de modules).

Outre l'asynchronicité, un autre avantage d'AMD est que vos modules peuvent être des objets, des fonctions, des constructeurs, des chaînes, du JSON et de nombreux autres types, tandis que CommonJS ne supporte que les objets en tant que modules.

Cela dit, AMD n'est pas compatible avec les fonctionnalités orientées serveur comme les E/S, le système de fichiers, etc., disponibles via CommonJS, et la syntaxe d'enveloppement de fonction est un peu plus verbeuse par rapport à une simple instruction _require_.

#### UMD

Pour les projets qui vous obligent à supporter à la fois les fonctionnalités AMD et CommonJS, il existe un autre format : Universal Module Definition (UMD).

UMD crée essentiellement un moyen d'utiliser l'un ou l'autre des deux, tout en supportant la définition de variable globale. Par conséquent, les modules UMD sont capables de fonctionner à la fois sur le client et le serveur.

Voici un rapide aperçu de la manière dont UMD s'y prend :

```js
(function (root, factory) {
  if (typeof define === 'function' && define.amd) {
      // AMD
    define(['myModule', 'myOtherModule'], factory);
  } else if (typeof exports === 'object') {
      // CommonJS
    module.exports = factory(require('myModule'), require('myOtherModule'));
  } else {
    // Variables globales du navigateur (Note : root est window)
    root.returnExports = factory(root.myModule, root.myOtherModule);
  }
}(this, function (myModule, myOtherModule) {
  // Méthodes
  function notHelloOrGoodbye(){}; // Une méthode privée
  function hello(){}; // Une méthode publique car elle est retournée (voir ci-dessous)
  function goodbye(){}; // Une méthode publique car elle est retournée (voir ci-dessous)

  // Méthodes publiques exposées
  return {
      hello: hello,
      goodbye: goodbye
  }
}));
```

Pour plus d'exemples de formats UMD, consultez ce [dépôt éclairant](https://github.com/umdjs/umd) sur GitHub.

### JS Natif

Ouf ! Vous êtes toujours là ? Je ne vous ai pas perdu dans les bois ? Bien ! Parce que nous avons *un autre* type de module à définir avant d'avoir terminé.

Comme vous l'avez probablement remarqué, aucun des modules ci-dessus n'était natif à JavaScript. Au lieu de cela, nous avons créé des moyens d'_émuler_ un système de modules en utilisant soit le modèle de module, CommonJS ou AMD.

Heureusement, les gens intelligents de TC39 (l'organisme de normalisation qui définit la syntaxe et la sémantique d'ECMAScript) ont introduit des modules intégrés avec ECMAScript 6 (ES6).

ES6 offre une variété de possibilités pour importer et exporter des modules, que d'autres ont bien expliquées — voici quelques-unes de ces ressources :

* [jsmodules.io](http://jsmodules.io/cjs.html)
* [exploringjs.com](http://exploringjs.com/es6/ch_modules.html)

Ce qui est génial avec les modules ES6 par rapport à CommonJS ou AMD, c'est qu'ils parviennent à offrir le meilleur des deux mondes : une syntaxe compacte et déclarative _et_ un chargement asynchrone, ainsi que des avantages supplémentaires comme un meilleur support pour les dépendances cycliques.

Probablement ma fonctionnalité préférée des modules ES6 est que les imports sont des vues en lecture seule _en direct_ des exports. (Comparez cela à CommonJS, où les imports sont des copies des exports et par conséquent ne sont pas en direct).

Voici un exemple de fonctionnement :

```js
// lib/counter.js

var counter = 1;

function increment() {
  counter++;
}

function decrement() {
  counter--;
}

module.exports = {
  counter: counter,
  increment: increment,
  decrement: decrement
};


// src/main.js

var counter = require('../../lib/counter');

counter.increment();
console.log(counter.counter); // 1
```

Dans cet exemple, nous créons essentiellement deux copies du module : une lorsque nous l'exportons, et une lorsque nous le requérons.

De plus, la copie dans main.js est maintenant déconnectée du module original. C'est pourquoi même lorsque nous incrémentons notre compteur, il retourne toujours 1 — parce que la variable de compteur que nous avons importée est une copie déconnectée de la variable de compteur du module.

Ainsi, incrémenter le compteur l'incrémentera dans le module, mais n'incrémentera pas votre version copiée. La seule façon de modifier la version copiée de la variable de compteur est de le faire manuellement :

```js
counter.counter++;
console.log(counter.counter); // 2
```

D'autre part, ES6 crée une vue en lecture seule en direct des modules que nous importons :

```js
// lib/counter.js
export let counter = 1;

export function increment() {
  counter++;
}

export function decrement() {
  counter--;
}


// src/main.js
import * as counter from '../../counter';

console.log(counter.counter); // 1
counter.increment();
console.log(counter.counter); // 2
```

Des trucs sympas, n'est-ce pas ? Ce que je trouve vraiment convaincant dans les vues en lecture seule en direct, c'est la façon dont elles vous permettent de diviser vos modules en morceaux plus petits sans perdre de fonctionnalité.

Ensuite, vous pouvez les fusionner à nouveau, sans problème. Cela fonctionne simplement.

### Vers l'avant : le regroupement de modules

Wow ! Où est passé le temps ? C'était une aventure folle, mais j'espère sincèrement que cela vous a donné une meilleure compréhension des modules en JavaScript.

Dans la prochaine section, je vais passer en revue le regroupement de modules, en couvrant les sujets principaux, notamment :

* Pourquoi nous regroupons les modules
* Différentes approches pour le regroupement
* L'API de chargeur de modules d'ECMAScript
* ...et plus encore. :)

_NOTE : Pour garder les choses simples, j'ai omis certains détails fastidieux (pensez : dépendances cycliques) dans cet article. Si j'ai omis quelque chose d'important et/ou de fascinant, faites-le moi savoir dans les commentaires !_