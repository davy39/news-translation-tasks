---
title: 'Apprendre ES6 à la manière cool Partie II : Les fonctions fléchées et le mot-clé
  ''this'''
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-05-16T10:40:45.000Z'
originalURL: https://freecodecamp.org/news/learn-es6-the-dope-way-part-ii-arrow-functions-and-the-this-keyword-381ac7a32881
coverImage: https://cdn-media-1.freecodecamp.org/images/1*qb02fqNhhC5mRIdzLA83Hg.png
tags:
- name: education
  slug: education
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: Tutorial
  slug: tutorial
- name: Web Development
  slug: web-development
seo_title: 'Apprendre ES6 à la manière cool Partie II : Les fonctions fléchées et
  le mot-clé ''this'''
seo_desc: 'By Mariya Diminsky

  Welcome to Part II of Learn ES6 The Dope Way, a series created to help you easily
  understand ES6 (ECMAScript 6)!

  So, what the heck is =>; ?

  You’ve probably seen these strange Egyptian-looking hieroglyphics symbols here and
  there, e...'
---

Par Mariya Diminsky

Bienvenue dans la Partie II de **Apprendre ES6 à la manière cool**, une série créée pour vous aider à comprendre facilement ES6 (ECMAScript 6) !

#### **Alors, qu'est-ce que c'est que ce => ?**

Vous avez probablement vu ces étranges symboles ressemblant à des hiéroglyphes égyptiens ici et là, surtout dans le code de quelqu'un d'autre, où vous déboguez actuellement un problème de mot-clé '_this_'. Après une heure de bidouillage, vous errez maintenant dans la barre de recherche Google et traquez Stack Overflow. Ça vous dit quelque chose ?

Ensemble, couvrons trois sujets dans **Apprendre ES6 à la manière cool** Partie II :

* Comment le mot-clé '_this_' se rapporte à **=>**.
* Comment migrer les fonctions de ES5 à ES6.
* Les particularités importantes à connaître lors de l'utilisation de **=>**.

#### Fonctions fléchées

Les fonctions fléchées ont été créées pour simplifier la portée des fonctions et rendre l'utilisation du mot-clé '_this_' beaucoup plus simple. Elles utilisent la syntaxe **=&gt;**, qui ressemble à une flèche. Même si je ne pense pas qu'elle ait besoin de faire un régime, les gens l'appellent « la flèche grasse » (et les enthousiastes de Ruby la connaissent mieux sous le nom de « hash rocket ») — quelque chose à garder à l'esprit.

#### Comment le mot-clé 'this' se rapporte aux fonctions fléchées

Avant de plonger plus profondément dans les fonctions fléchées ES6, il est important d'avoir d'abord une image claire de ce à quoi '_this_' se lie dans le code ES5.

Si le mot-clé '_this_' était à l'intérieur d'une **méthode** d'un objet (une fonction qui appartient à un objet), à quoi ferait-il référence ?

```js
// Testez-le ici : https://jsfiddle.net/maasha/x7wz1686/
var bunny = {
  name: 'Usagi',
  showName: function() {
    alert(this.name);
  }
};

bunny.showName(); // Usagi
```

Correct ! Il ferait référence à l'objet. Nous verrons pourquoi plus tard.

Et si le mot-clé '_this_' était à l'intérieur d'une fonction d'une méthode ?

```js
// Testez-le ici : https://jsfiddle.net/maasha/z65c1znn/
var bunny = {
  name: 'Usagi',
  tasks: ['transform', 'eat cake', 'blow kisses'],
  showTasks: function() {
    this.tasks.forEach(function(task) {
      alert(this.name + " wants to " + task);
    });
  }
};

bunny.showTasks();
// [object Window] wants to transform
// [object Window] wants to eat cake
// [object Window] wants to blow kisses

// veuillez noter, dans jsfiddle, [object Window] est nommé 'result' dans les fonctions internes des méthodes.
```

Qu'avez-vous obtenu ? Attendez, qu'est-il arrivé à notre lapin...

Ah, pensiez-vous que '_this_' fait référence à la fonction interne de la méthode ?

Peut-être à l'objet lui-même ?

Vous avez raison de le penser, mais ce n'est pas le cas. Permettez-moi de vous enseigner ce que les anciens du codage m'avaient autrefois enseigné :

Ancien du codage : « Ah oui, le code est fort avec celui-ci. Il est en effet pratique de penser que le mot-clé 'this' se lie à la fonction, mais la vérité est que 'this' est maintenant hors de portée... Il appartient maintenant à... », il pause comme s'il ressentait une tourmente intérieure, « l'objet window. »

C'est exactement ce qui s'est passé.

Pourquoi '_this_' se lie-t-il à l'objet window ? **Parce que '_this_' fait toujours référence au propriétaire de la fonction dans laquelle il se trouve, dans ce cas — puisque il est maintenant hors de portée — l'objet window/global.**

Lorsque '_this_' est à l'intérieur d'une méthode d'un objet — le propriétaire de la fonction est l'objet. Ainsi, le mot-clé '_this_' est lié à l'objet. Pourtant, lorsqu'il est à l'intérieur d'une fonction, soit seule ou dans une autre méthode, il fera toujours référence à l'objet window/global.

```js
// Testez-le ici : https://jsfiddle.net/maasha/g278gjtn/
var standAloneFunc = function(){
  alert(this);
}

standAloneFunc(); // [object Window]
```

Mais pourquoi...

Ceci est connu comme une particularité de JavaScript, ce qui signifie quelque chose qui se produit simplement dans JavaScript et qui n'est pas exactement simple et ne fonctionne pas comme vous le penseriez. Cela a également été considéré par les développeurs comme un mauvais choix de conception, qu'ils corrigent maintenant avec les fonctions fléchées de ES6.

Avant de continuer, il est important d'être conscient de deux façons astucieuses dont les programmeurs résolvent le problème de '_this_' dans le code ES5, surtout puisque vous continuerez à rencontrer ES5 pendant un certain temps (tous les navigateurs n'ont pas encore migré vers ES6) :

**#1** Créer une variable en dehors de la fonction interne de la méthode. Maintenant, la méthode 'forEach' obtient l'accès à '_this_' et ainsi aux propriétés de l'objet et à leurs valeurs. Cela est dû au fait que '_this_' est stocké dans une variable alors qu'il est encore dans la portée de la méthode directe de l'objet 'showTasks'.

```js
// Testez-le ici : https://jsfiddle.net/maasha/3mu5r6vg/
var bunny = {
  name: 'Usagi',
  tasks: ['transform', 'eat cake', 'blow kisses'],
  showTasks: function() {
    var _this = this;
    this.tasks.forEach(function(task) {
      alert(_this.name + " wants to " + task); 
    });
  }
};

bunny.showTasks();
// Usagi wants to transform
// Usagi wants to eat cake
// Usagi wants to blow kisses
```

**#2** Utiliser bind pour attacher le mot-clé '_this_' qui fait référence à la méthode à la fonction interne de la méthode.

```js
// Testez-le ici : https://jsfiddle.net/maasha/u8ybgwd5/
var bunny = {
  name: 'Usagi',
  tasks: ['transform', 'eat cake', 'blow kisses'],
  showTasks: function() {
    this.tasks.forEach(function(task) {
      alert(this.name + " wants to " + task);
    }.bind(this));
  }
};

bunny.showTasks();
// Usagi wants to transform
// Usagi wants to eat cake
// Usagi wants to blow kisses
```

Et maintenant, voici les fonctions fléchées ! Traiter avec le problème de '_this_' n'a jamais été aussi facile et direct ! La solution simple ES6 :

```js
// Testez-le ici : https://jsfiddle.net/maasha/che8m4c1/

var bunny = {
  name: 'Usagi',
  tasks: ['transform', 'eat cake', 'blow kisses'],
  showTasks() {
    this.tasks.forEach((task) => {
      alert(this.name + " wants to " + task);
    });  
  }
};

bunny.showTasks();
// Usagi wants to transform
// Usagi wants to eat cake
// Usagi wants to blow kisses
```

Alors qu'en ES5 '_this_' faisait référence au parent de la fonction, en ES6, les fonctions fléchées utilisent la portée lexicale — '_this_' fait référence à sa portée environnante actuelle et rien de plus. Ainsi, la fonction interne savait se lier uniquement à la fonction interne, et non à la méthode de l'objet ou à l'objet lui-même.

#### Comment migrer les fonctions de ES5 à ES6.

```js
// Avant
let bunny = function(name) {
  console.log("Usagi");
}

// Après
let bunny = (name) => console.log("Usagi")

// Étape 1 : Retirez le mot 'function'.
let bunny = (name) {
  console.log("Usagi");
}

// Étape 2 : Si votre code fait moins d'une ligne, retirez les accolades et placez-le sur une ligne.
let bunny = (name) console.log("Usagi");

// Étape 3 : Ajoutez la flèche.
let bunny = (name) => console.log("Usagi");
```

Vous l'avez fait ! Bon travail ! Assez simple, non ? Voici quelques exemples supplémentaires utilisant la flèche — euh, la flèche mince, pour habituer vos yeux :

```js
// #1 ES6 : si vous passez un argument, vous n'avez pas besoin d'inclure les parenthèses autour du paramètre.
var kitty = name => name;

// même chose en ES5 :
var kitty = function(name) {
  return name;
};

// #2 ES6 : exemple sans paramètres.
var add = () => 3 + 2;

// même chose en ES5 :
var add = function() {
  return 3 + 2;
};

// #3 ES6 : si la fonction se compose de plus d'une ligne ou est un objet, incluez les accolades.
var objLiteral = age => ({ name: "Usagi", age: age });

// même chose en ES5 :
var objLiteral = function(age) {
  return {
    name: "Usagi",
    age: age
  };
};

// #4 ES6 : promesses et rappels.
asyncfn1().then(() => asyncfn2()).then(() => asyncfn3()).then(() => done());

// même chose en ES5 :
asyncfn1().then(function() {
  asyncfn2();
}).then(function() {
  asyncfn3();
}).done(function() {
  done();
});
```

#### Particularités importantes à connaître lors de l'utilisation des fonctions fléchées

Si vous utilisez le mot-clé 'new' avec les fonctions =>, cela générera une erreur. Les fonctions fléchées ne peuvent pas être utilisées comme constructeur — les fonctions normales supportent 'new' via la propriété prototype et la méthode interne [[Construct]]. Les fonctions fléchées n'utilisent ni l'une ni l'autre, donc new (() => {}) génère une erreur.

D'autres particularités à considérer :

```js
// Les sauts de ligne ne sont pas autorisés et généreront une erreur de syntaxe
let func1 = (x, y)
=> {
  return x + y;
}; // SyntaxError

// Mais les sauts de ligne à l'intérieur d'une définition de paramètre sont acceptés
let func6 = (
  x,
  y
) => {
	return x + y;
}; // Fonctionne !

// Si une expression est le corps d'une fonction fléchée, vous n'avez pas besoin d'accolades :
asyncFunc.then(x => console.log(x));

// Cependant, les instructions doivent être placées dans des accolades :
asyncFunc.catch(x => { throw x });

// Les fonctions fléchées sont toujours anonymes, ce qui signifie que vous ne pouvez pas simplement les déclarer comme en ES5 :
function squirrelLife() {
  // jouer avec les écureuils, creuser pour trouver de la nourriture, etc.
}

// Doit être à l'intérieur d'une variable ou d'une propriété d'objet pour fonctionner correctement :
let squirrelLife = () => {
  // jouer avec les écureuils, creuser pour trouver de la nourriture, etc.
  // une autre action super écureuil.
}
```

Félicitations ! Vous avez terminé **Apprendre ES6 à la manière cool** Partie II et vous avez maintenant une base de connaissances sur les fonctions fléchées, les avantages lexicaux qu'elles offrent à '_this_' et vous avez également acquis des compétences sur les particularités de JavaScript ! :)

Gardez votre sagesse à jour en aimant et en suivant car plus de **Apprendre ES6 à la manière cool** arrive bientôt sur Medium !

**[Partie I : const, let & var](https://www.freecodecamp.org/news/learn-es6-the-dope-way-i-const-let-var-ae828580472b/)**

**[Partie II : (Fonctions fléchées) => et le mot-clé 'this'](https://www.freecodecamp.org/news/learn-es6-the-dope-way-part-ii-arrow-functions-and-the-this-keyword-381ac7a32881/)**

**[Partie III : Littéraux de gabarit, opérateurs de propagation & générateurs !](https://www.freecodecamp.org/news/learn-es6-the-dope-way-part-iii-template-literals-spread-operators-generators-592765337294/)**

**[Partie IV : Paramètres par défaut, affectation par décomposition, et une nouvelle méthode ES6 !](https://www.freecodecamp.org/news/learn-es6-the-dope-way-part-iv-default-parameters-destructuring-assignment-a-new-es6-method-44393190b8c9/)**

**[Partie V : Classes, transpilation du code ES6 & plus de ressources !](https://www.freecodecamp.org/news/learn-es6-the-dope-way-part-v-classes-browser-compatibility-transpiling-es6-code-47f62267661/)**

Vous pouvez également me trouver sur github ❤ [https://github.com/Mashadim](https://github.com/Mashadim)