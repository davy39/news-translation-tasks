---
title: Une introduction à JavaScript Fonctionnel
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-20T17:31:24.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-functional-javascript-e8dab63bb51d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*DxjfBur9XKUWgSgceIv11Q.jpeg
tags:
- name: books
  slug: books
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Une introduction à JavaScript Fonctionnel
seo_desc: 'By Cristian Salcescu

  Hey everybody! I’ve written a book called Discover Functional JavaScript, and it’s
  now ready in both paperback and Kindle formats.

  After publishing several articles on Functional Programming in JavaScript, at some
  point I realize...'
---

Par Cristian Salcescu

Bonjour à tous ! J'ai écrit un livre intitulé [Discover Functional JavaScript](https://www.amazon.com/dp/B07PBQJYYG), et il est maintenant disponible en formats papier et Kindle.

Après avoir publié plusieurs articles sur la programmation fonctionnelle en JavaScript, à un moment donné, j'ai réalisé que j'avais assez de matériel pour penser à un livre. J'ai donc commencé à partir de mes écrits précédents, j'ai comblé les parties manquantes et j'ai créé un livre sur la programmation fonctionnelle en JavaScript.

Ce que j'ai essayé de faire dans ce livre, c'est de donner des exemples pratiques des concepts fonctionnels de base. Je pense que si nous maîtrisons les fondamentaux, il sera plus facile de gérer des situations plus complexes. Et c'est à cela que sert ce livre.

J'ai approfondi la compréhension des fonctions pures au-delà du fait qu'elles sont formidables. Si elles sont si bonnes, pourquoi n'écrivons-nous pas toute l'application en utilisant uniquement des fonctions pures ?

L'autre raison derrière ce livre est de souligner la nouvelle façon de construire des objets encapsulés sans classes ni prototypes en JavaScript. J'ai même vu des classes présentées comme un moyen d'apporter l'encapsulation aux objets. L'encapsulation signifie cacher l'information. Les objets construits avec des classes en JavaScript sont construits sur le système de prototypes. Toutes leurs propriétés sont publiques, elles ne sont pas encapsulées.

J'ai essayé, et j'espère avoir réussi, de présenter les concepts fondamentaux de la programmation fonctionnelle de manière facile à apprendre et pratique. Après avoir lu le livre, vous comprendrez mieux les concepts tels que les fonctions de première classe, les fermetures, le currying et l'application partielle. Vous comprendrez ce que sont les fonctions pures et comment les créer. Vous comprendrez mieux l'immuabilité et comment elle peut être réalisée en JavaScript.

Une autre chose qui n'est pas suffisamment prise en compte est le nommage. Avec l'essor des fonctions fléchées, de plus en plus de fonctions anonymes sont créées. Le prétexte derrière tout cela est le fait que les fonctions fléchées n'ont pas de `this` et ont une syntaxe plus courte. Je ne conteste pas cela, je conteste simplement le fait que les noms significatifs sont ce que nous comprenons le mieux. Supprimer cela rendra le code plus difficile à comprendre.

Le livre est assez condensé, vous pouvez donc le lire plusieurs fois. En ce qui concerne les concepts de base de JavaScript, il vise à en faire un aperçu, sans entrer dans les détails. Il existe de nombreuses ressources pour cela.

Pour moi, ce fut une grande expérience d'essayer d'organiser mes pensées pour exprimer ces idées de manière simple et pratique. J'ai essayé de me concentrer sur les concepts pratiques principaux et de simplement éliminer tout ce qui n'ajoute aucune valeur au lecteur.

Une compréhension plus approfondie des concepts fondamentaux en JavaScript nous rend meilleurs pour résoudre des problèmes complexes. J'espère que vous l'aimerez.

Voici ce que vous pouvez trouver à l'intérieur :

#### Chapitre 1 : Un bref aperçu de JavaScript

JavaScript a des primitives, des objets et des fonctions. Tous sont des valeurs. Tous sont traités comme des objets, même les primitives.

Number, boolean, string, `undefined` et `null` sont des primitives.

Les variables peuvent être définies en utilisant `var`, `let` et `const`. La déclaration `let` a une portée de bloc.

Les primitives, sauf `null` et `undefined`, sont traitées comme des objets, dans le sens où elles ont des méthodes mais ne sont pas des objets.

Les tableaux sont des collections indexées de valeurs. Chaque valeur est un élément. Les éléments sont ordonnés et accessibles par leur numéro d'index.

JavaScript a une typage dynamique. Les valeurs ont des types, les variables non. Les types peuvent changer à l'exécution.

Le runtime principal de JavaScript est monothread. Deux fonctions ne peuvent pas s'exécuter en même temps.

#### Chapitre 2 : Nouvelles fonctionnalités dans ES6+

ES6 apporte plus de fonctionnalités au langage JavaScript. Une nouvelle syntaxe vous permet d'écrire du code de manière plus expressive, certaines fonctionnalités complètent la boîte à outils de la programmation fonctionnelle, et certaines fonctionnalités sont discutables.

La déclaration `let` a une portée de bloc.

```
function doTask(){   
  let x = 1;   
  {       
    let x = 2;   
  }
   
  console.log(x); 
}  
doTask(); //1
```

La déclaration `var` a une portée de fonction. Elle n'a pas de portée de bloc.

```
function doTask(){   
  var x = 1;   
  {       
    var x = 2;   
  }
   
  console.log(x); 
}  
doTask(); //2
```

#### Chapitre 3 : Fonctions de première classe

Les fonctions sont des objets de première classe. Les fonctions peuvent être stockées dans des variables, des objets ou des tableaux, passées en arguments à d'autres fonctions ou retournées par des fonctions.

Une fonction d'ordre supérieur est une fonction qui prend une autre fonction en entrée, retourne une fonction, ou fait les deux.

`map()` transforme une liste de valeurs en une autre liste de valeurs en utilisant une fonction de mappage.

```
let numbers = [1,2,3,4,5];

function doubleNo(x){
  const result = x*2;
  console.log(`${x} -> ${result}`)
  return result;
}

const doubleNumbers = numbers.map(doubleNo);
//1 -> 2
//2 -> 4
//3 -> 6
//4 -> 8
//5 -> 10
//[2, 4, 6, 8, 10]
```

#### Chapitre 4 : Fermetures

![Image](https://cdn-media-1.freecodecamp.org/images/JSAYSH9IZCpQfKGWJdklasvq1VmXf7aLpBB5)

Une fermeture est une fonction interne qui a accès à la portée externe, même après que le conteneur de la portée externe a été exécuté.

La fonction `count()` dans l'exemple suivant est une fermeture :

```
const count = (function(){
  let state = 0;
  return function(){
    state = state + 1;
    return state;
  }
})();

count(); //1
count(); //2
count(); //3
```

#### Chapitre 5 : Décorateurs de fonctions

> Un décorateur de fonction est une fonction d'ordre supérieur qui prend une fonction comme argument et retourne une autre fonction, et la fonction retournée est une variation de la fonction argument — Reginald Braithwaite, auteur de [Javascript Allongé](https://leanpub.com/javascript-allonge/read#decorators)

Le décorateur `unary()` retourne une nouvelle version de la fonction qui accepte uniquement un argument. Il peut être utilisé pour corriger les problèmes lorsque la fonction est appelée avec plus d'arguments que nécessaire.

```
function unary(fn){
 return function(first){
   return fn(first);
 }
}

const numbers = ['1','2','3','4','5','6'];
numbers.map(parseInt); 
//[1, NaN, NaN, NaN, NaN, NaN]

numbers.map(unary(parseInt)); 
//[1, 2, 3, 4, 5, 6]
```

#### Chapitre 6 : Fonctions pures

![Image](https://cdn-media-1.freecodecamp.org/images/6XNeBIiQldZ1bK7AK3-5GrQuUyEprm50TNq8)

Une fonction pure est une fonction qui, étant donné la même entrée, retourne toujours la même sortie et n'a pas d'effets secondaires.

Vous avez peut-être vu des exemples de fonctions pures comme ceux ci-dessous et vous voulez regarder quelques exemples pratiques de fonctions pures.

```
function double(x){
  return x * 2;
}

function add(a, b){
  return a + b;
}

function multiply(a, b) {
  return a * b;
}
```

Comme d'autres paradigmes de programmation, la programmation fonctionnelle pure promet de rendre le code plus facile à lire, comprendre, tester, déboguer et composer. Peut-elle tenir sa promesse ? Si oui, pouvons-nous construire une application en utilisant uniquement des fonctions pures ? Ce sont des questions auxquelles ce chapitre tente de répondre.

#### Chapitre 7 : Immuabilité

Une valeur immuable est une valeur qui, une fois créée, ne peut pas être modifiée.

L'immuabilité a-t-elle à voir avec des variables qui ne peuvent pas changer ou des valeurs qui ne peuvent pas changer ? Et comment pouvons-nous faire en sorte que cela se produise ? Pourquoi nous soucions-nous même de cela ? Ce chapitre tente de répondre à ces questions.

![Image](https://cdn-media-1.freecodecamp.org/images/THSwkY8IPNQ0UjMPr5yzQG0vij3fEhdeaoIp)

#### Chapitre 8 : Application partielle et currying

L'application partielle fait référence au processus de fixation d'un certain nombre de paramètres en créant une nouvelle fonction avec moins de paramètres que l'originale.

Le currying est le processus de transformation d'une fonction avec de nombreux paramètres en une série de fonctions qui prennent chacune un seul paramètre.

Habituellement, nous trouvons des exemples utilisant le currying pour additionner ou multiplier quelques nombres, comme dans le code ci-dessous :

```
function add(a) {
  return function(b){
    return function(c){
      return a + b + c;
    }
  }
}

add(1)(2)(3);
//6
```

Le currying a-t-il une application pratique ? Ce chapitre montre quelques exemples pratiques d'utilisation de l'application partielle et du currying.

#### Chapitre 9 : Composition de fonctions

La composition de fonctions consiste à appliquer une fonction au résultat d'une autre.

```
function compose(...functions){
  return function(x){
    return functions.reduceRight((value, f) => f(value), x);
  }
}

f(g(x)) === compose(f,g)(x);
```

#### Chapitre 10 : Noms révélant l'intention

Les fonctions peuvent être créées avec ou sans nom. La syntaxe des flèches crée généralement des fonctions anonymes.

```
(() => {
    /*code*/
    (() => {
        /*code*/
    })();
})();
```

Les fonctions anonymes apparaissent comme « (anonymous) » dans la pile d'appels.

Les noms révélant l'intention améliorent la lisibilité du code.

#### Chapitre 11 : Rendre le code plus facile à lire

Ce chapitre montre des exemples de refactorisation de code impératif avec des techniques de programmation fonctionnelle et examine la lisibilité du code final.

#### Chapitre 12 : Programmation asynchrone

Dans une application, il existe deux types de fonctions : synchrones et asynchrones. Nous examinons le modèle de programmation asynchrone en JavaScript.

#### Chapitre 13 : Objets avec prototypes

Les objets sont des collections dynamiques de propriétés, avec une propriété « cachée » vers le prototype de l'objet.

Les objets héritent d'autres objets.

`class` est une syntaxe sucrée pour créer des objets avec un prototype personnalisé.

```
class Counter {
  constructor(){
    this.state = 0;
  }
  
  increment(){
    this.state = this.state + 1;
    return this.state;
  }
  
  decrement(){
    this.state = this.state - 1;
    return this.state;
  }
}

const counter = new Counter();
counter.increment(); //1
counter.increment(); //2
counter.increment(); //3
counter.decrement(); //2
```

#### Chapitre 14 : Objets avec fermetures

Avec les fermetures, nous pouvons créer des objets encapsulés et flexibles. Considérez le même objet compteur créé avec des fermetures :

```
function Counter() {
  let state = 0;
  
  function increment(){
    state = state + 1;
    return state;
  }
  
  function decrement(){
    state = state - 1;
    return state;
  }
  
  return Object.freeze({
    increment, 
    decrement
  })
}

const counter = Counter();
counter.increment(); //1
counter.increment(); //2
counter.increment(); //3
counter.decrement(); //2
```

Ce chapitre présente des objets plus encapsulés et discute de la différence entre les objets construits avec des fermetures et des prototypes.

#### Chapitre 15 : Décorateurs de méthodes

Les décorateurs de méthodes sont un outil pour réutiliser la logique commune.

#### Chapitre 16 : Attendre le nouveau paradigme de programmation

Le dernier chapitre contient des réflexions sur la programmation fonctionnelle et orientée objet en JavaScript.

[**Profitez du livre**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_j0hTCbF0B1230)**!**

Vous pouvez me trouver sur [Twitter](https://twitter.com/cristi_salcescu).