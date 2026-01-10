---
title: Commencer avec ES6 en utilisant quelques-unes de mes choses préférées
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-06T09:51:49.000Z'
originalURL: https://freecodecamp.org/news/getting-started-with-es6-using-a-few-of-my-favorite-things-ac89c27812e0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*TjHw7JGRxc6RQ6cG-1uEow.jpeg
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Commencer avec ES6 en utilisant quelques-unes de mes choses préférées
seo_desc: 'By Todd Palmer

  This tutorial walks you through some easy steps to get started learning the newest
  version of JavaScript: ES6.

  To get a feel for the language, we will delve into a few of my favorite features.
  Then I will provide a short list of some g...'
---

Par Todd Palmer

Ce tutoriel vous guide à travers quelques étapes faciles pour commencer à apprendre la dernière version de JavaScript : **ES6.**

Pour vous familiariser avec le langage, nous allons explorer quelques-unes de mes fonctionnalités préférées. Ensuite, je fournirai une courte liste de ressources pour apprendre ES6.

### ES6 ou ECMAScript 2015 ?

> « Qu'y a-t-il dans un nom ? »   
> – Juliet dans « Roméo et Juliet » de Shakespeare

Le nom officiel de la **6ème édition d'ECMAScript** est **ECMAScript 2015**, car elle a été finalisée en juin 2015. Cependant, en général, les gens semblent simplement l'appeler **ES6**.

Auparavant, vous deviez utiliser un **transpileur** comme [Babel](https://babeljs.io/) pour commencer avec ES6. Maintenant, il semble que presque tout le monde, sauf Microsoft Internet Explorer, supporte la plupart des fonctionnalités d'ES6. Pour être juste, Microsoft supporte ES6 dans Edge. Si vous voulez plus de détails, consultez le tableau de compatibilité de **kangax** [ici](https://kangax.github.io/compat-table/es6/).

### Environnement d'apprentissage ES6

La meilleure façon d'apprendre ES6 est d'écrire et d'exécuter du code ES6. Il existe de nombreuses façons de le faire. Mais les deux que j'utilise lorsque je fais des expériences sont :

* [Node.js](https://nodejs.org)
* La page [Essayez-le](https://babeljs.io/repl/) de Babel.io

#### Node.js et Visual Studio Code

L'une des meilleures façons d'explorer les agréments d'ES6 est d'écrire votre code dans un éditeur comme [Visual Studio Code](https://code.visualstudio.com/) puis de l'exécuter dans [Node.js](https://nodejs.org).

Installez Visual Studio Code et créez un fichier appelé `helloworld.js`. Collez le code suivant :

```
console.log('Hello world');
```

Enregistrez-le. Cela devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*qTe3mqHxVKx1TiLFQnEIwg.png)

Depuis la version 6.5, Node.js supporte la plupart des standards ES6. Pour exécuter notre exemple, ouvrez l'invite de commande Node.js dans le dossier où vous avez créé le fichier `helloworld.js`. Et tapez simplement :

```
node helloworld.js
```

Notre instruction `console.log` affiche en sortie :

![Image](https://cdn-media-1.freecodecamp.org/images/1*FbpDvDA0x-1aAOapzj2WYg.png)

#### Babel.io

Ce n'est pas aussi amusant que Node.js, mais une façon pratique d'exécuter du code ES6 est la page [Essayez-le](https://babeljs.io/repl) sur [Babel.io](https://babeljs.io/repl). Développez les **Paramètres** et assurez-vous que **Évaluer** est coché. Ensuite, ouvrez la **Console** de votre navigateur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*P23x3sFTvWnyfgLwR7kyNQ.png)
_Babel REPL_

Tapez le code ES6 dans la colonne de gauche. Babel le compile en JavaScript classique. Vous pouvez utiliser `console.log` et voir la sortie dans la console Web à droite.

### Quelques-unes de mes fonctionnalités préférées

> « Ce sont quelques-unes de mes choses préférées. »   
> – Maria dans « La Mélodie du Bonheur » de Rodgers et Hammerstein

Dans cette section, nous allons jeter un coup d'œil rapide à quelques-unes des nouvelles fonctionnalités d'ES6, notamment :

* Utiliser `let` et `const` au lieu de `var`
* Fonctions fléchées
* Chaînes de caractères de modèle
* Déstructuration

#### const et let versus var

Maintenant que vous codez en ES6 : Arrêtez d'utiliser `var` ! Sérieusement, n'utilisez plus jamais `var`.

Désormais, utilisez soit `const`, soit `let`. Utilisez `const` lorsque vous définirez la valeur une seule fois. Utilisez `let` lorsque vous prévoyez de changer la valeur.

```
let bar = { x: 'x' };
const foo = { x: 'x' };
```

```
bar.x = 'other'; // Cela fonctionne
foo.x = 'other'; // Cela fonctionne aussi
```

```
bar = {}; // Cela fonctionne aussi
foo = {}; // Cela génère une erreur
```

Typiquement, j'aime utiliser `const` en premier. Ensuite, si cela se plaint, je regarde mon code et je m'assure que j'ai vraiment besoin de pouvoir modifier la variable. Si c'est le cas, je la change en `let`.

Assurez-vous de consulter les ressources plus tard dans cet article pour plus d'informations sur `let` et `const`. Vous verrez qu'ils fonctionnent de manière beaucoup plus intuitive que `var`.

#### Fonctions fléchées

Les fonctions fléchées sont l'une des caractéristiques définissant ES6. Les fonctions fléchées sont une nouvelle façon d'écrire des fonctions. Par exemple, les fonctions suivantes fonctionnent de manière identique :

```
function oneMore(val) {
  return val + 1;
}
console.log('3 et un de plus est :', oneMore(3));
```

```
const oneMore = (val) => val + 1;
console.log('3 et un de plus est :', oneMore(3));
```

Il y a quelques choses à retenir sur les fonctions fléchées :

* Elles retournent automatiquement la valeur calculée.
* Elles ont un `this` lexical.

La première fois que j'ai vu cela, je me suis demandé : « Qu'est-ce qu'un **this lexical** ? Et est-ce que cela m'intéresse vraiment ? » Regardons un exemple de pourquoi le `this` lexical est si utile et comment il rend notre code beaucoup plus intuitif :

Dans les lignes 1 à 31, nous définissons une classe appelée `ThisTester`. Elle a deux fonctions `thisArrowTest()` et `thisTest()` qui font essentiellement la même chose. Mais l'une utilise une fonction fléchée et l'autre utilise la notation de fonction classique.

À la ligne 33, nous créons un nouvel objet `myTester` basé sur notre classe `ThisTester` et nous appelons les deux fonctions de notre classe.

```
const myTester = new ThisTester();
console.log('TEST : thisArrowTest');
myTester.thisArrowTest();
console.log('');
console.log('TEST : thisTest');
myTester.thisTest();
```

Dans la fonction `thisTest()`, nous voyons qu'elle essaie d'utiliser `this` à la ligne 26.

```
console.log('la fonction this échoue', this.testValue);
```

Mais elle échoue parce que cette fonction obtient son propre `this` et ce n'est pas le même `this` que celui de la classe. Si vous pensez que c'est confus, c'est parce que c'est le cas. Ce n'est pas intuitif du tout. Et les nouveaux développeurs passent parfois leur première semaine à lutter avec `this` dans les fonctions de rappel et les promesses comme je l'ai fait.

Finalement, après avoir examiné un tas d'exemples, j'ai compris l'astuce standard consistant à utiliser une variable appelée `self` pour conserver le `this` que nous voulons utiliser. Par exemple, à la ligne 17 :

```
let self = this;
```

Cependant, remarquez comment dans la fonction fléchée à la ligne 10, nous pouvons accéder directement à `this.testValue` et cela fonctionne magiquement :

```
let myFunction = (x) => console.log('arrow "this" fonctionne :', this.testValue)
```

C'est le **this lexical** en action. Le `this` dans la fonction fléchée est le même que le `this` dans la fonction environnante qui l'appelle. Et donc nous pouvons utiliser `this` de manière intuitive pour accéder aux propriétés de notre objet comme `this.testValue`.

#### Chaînes de caractères de modèle

Les chaînes de caractères de modèle (parfois appelées littéraux de modèle) sont un moyen facile de construire des chaînes de caractères. Elles sont idéales pour les chaînes de caractères multilingues telles que celles utilisées dans les modèles Angular. Les chaînes de caractères de modèle utilisent la **backtick** ` au lieu des guillemets ou apostrophes.

Voici un exemple de création d'une longue chaîne de caractères multilingue :

```
const myLongString = `Cette chaîne s'étend en fait sur plusieurs lignes. Et je n'ai même pas besoin d'utiliser de notation "étrange".`;
console.log(myLongString);
```

Vous pouvez facilement lier des variables à votre chaîne de caractères, par exemple :

```
const first = 'Todd', last = 'Palmer';
console.log(`Bonjour, mon nom est ${first} ${last}.`)
```

En regardant cette affectation de variable, la question se pose : 
« Et si j'ai besoin d'utiliser les caractères $, { ou } dans ma chaîne de caractères ? »

Eh bien, le seul qui nécessite un traitement spécial est la séquence `${`.

```
console.log(`Je peux les utiliser tous séparément $ { }`);
console.log(`$\{ nécessite une barre oblique inverse.`);
```

Les chaînes de caractères de modèle sont particulièrement utiles dans [Angular](https://angular.io/) et [AngularJS](https://angularjs.org/) où vous créez des modèles HTML, car ils tendent à être multilingues et à avoir beaucoup de guillemets et d'apostrophes. Voici à quoi ressemble un petit exemple de modèle Angular utilisant la backtick :

```
import { Component } from '@angular/core';
```

```
@Component({
  selector: 'app-root',
  template: `
    <h1>{{title}}</h1>
    <h2>Mon héros préféré est : {{myHero}}</h2>
  `
})
export class AppComponent {
  title = 'Tour des Héros';
  myHero = 'Windstorm';
}
```

#### Déstructuration

La déstructuration vous permet de prendre des parties d'un objet ou d'un tableau et de les assigner à vos propres variables nommées. Pour plus d'informations sur la déstructuration, consultez mon article sur [ITNEXT](https://itnext.io/es6-destructuring-b8c50a20b46c).

### Ressources ES6

Ce n'était qu'un aperçu rapide de quelques-unes des nouvelles fonctionnalités d'ES6. Voici quelques excellentes ressources pour continuer votre voyage sur le chemin de l'apprentissage d'ES6 :

* [Apprendre ES2015](https://babeljs.io/learn-es2015/) sur Babel  
Ceci est un aperçu de toutes les nouvelles fonctionnalités. Bien qu'il n'entre pas dans les détails, cette page est une excellente référence rapide avec des exemples.
* [Conseils et astuces ES6 pour rendre votre code plus propre, plus court et plus facile à lire !](https://medium.freecodecamp.org/make-your-code-cleaner-shorter-and-easier-to-read-es6-tips-and-tricks-afd4ce25977c) par [Sam Williams](https://medium.freecodecamp.org/@samwsoftware)  
Ceci est un excellent article dans la publication Medium de [Free Code Camp](https://medium.freecodecamp.org/).
* La série vidéo de [MPJ](https://www.bing.com/search?q=funfunfunction) : [Fonctionnalités JavaScript ES6](https://www.youtube.com/playlist?list=PL0zVEGEvSaeHJppaRLrqjeTPnCH6vw-sm)  
Si vous préférez les vidéos, MPJ est votre homme. Non seulement il est bon techniquement, mais son contenu est vraiment divertissant.
* La série [ES6 en profondeur](https://hacks.mozilla.org/category/es6-in-depth/) sur [Mozilla Hacks](https://hacks.mozilla.org/)  
Ceci est une excellente série en profondeur.
* La série de Eric Elliott [Composing Software](https://medium.com/javascript-scene/composing-software-an-introduction-27b72500d6ea)  
Lisez ceci pour un vrai défi. Soyez cependant prévenu, certaines des choses de Eric sont de niveau universitaire en informatique.

Cet article est basé sur une conférence que j'ai donnée en mars 2018.