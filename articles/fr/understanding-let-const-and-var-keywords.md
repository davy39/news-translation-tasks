---
title: Comment fonctionnent les mots-clés let, const et var en JavaScript
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2022-01-11T16:47:43.000Z'
originalURL: https://freecodecamp.org/news/understanding-let-const-and-var-keywords
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/freeCodeCamp-Cover-1.png
tags:
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Comment fonctionnent les mots-clés let, const et var en JavaScript
seo_desc: "As a JavaScript beginner, you probably learned how to declare variables\
  \ and assign values. \nIn the old, pre-ES6 era of JavaScript, developers used to\
  \ declare variables using the keyword var or without any keywords. But times have\
  \ changed!\nWith ES6 (E..."
---

En tant que débutant en JavaScript, vous avez probablement appris à déclarer des variables et à leur assigner des valeurs. 

À l'époque ancienne, avant ES6, les développeurs déclaraient les variables en utilisant le mot-clé `var` ou sans aucun mot-clé. Mais les temps ont changé !

Avec ES6 (EcmaScript 2015), le début de l'ère moderne en JavaScript, le langage a obtenu deux nouveaux mots-clés pour nous aider à déclarer des variables. Ce sont `let` et `const`. 

Dans cet article, nous allons apprendre tous ces mots-clés (oui, y compris `var`) avec des exemples, et nous verrons quand les utiliser, et quand ne pas les utiliser.

Si vous aimez apprendre à partir de contenu vidéo également, cet article est également disponible sous forme de tutoriel vidéo YouTube ici : 
ud83d
de42

%[https://www.youtube.com/watch?v=ehn_BcusA_c]

D'ailleurs, c'est un sujet largement discuté. Alors, pourquoi en écrire à nouveau ? Eh bien, ces mots-clés peuvent être difficiles à apprendre parce que :

1. De nombreux développeurs essaient de les utiliser de manière interchangeable (surtout `let` avec les deux autres).
2. Parfois, vous pourriez être confus sur la relation de ces mots-clés avec un concept fondamental de JavaScript appelé `Scope`.

Donc, cet article vise à enseigner ces mots-clés dans le contexte de trois concepts essentiels. J'espère que vous apprécierez sa lecture.

## Comment déclarer des variables en JavaScript

En JavaScript, nous pouvons déclarer des variables de trois manières différentes comme ceci :

```js
// Sans mots-clés. C'est essentiellement la même chose que var 
// et non autorisé en mode 'strict'.
name = 'Jack'; 

// En utilisant var
var price = 100;

// En utilisant let
let isPermanent = false; 

// En utilisant const
const PUBLICATION = 'freeCodeCamp' 

```

Il est préférable de comprendre var, let et const avec ces trois concepts :

* Portée (Scope)
* Réassigner une nouvelle valeur
* Lorsque vous accédez à une variable avant de la déclarer

Ces mots-clés diffèrent dans leur utilisation par rapport à ces concepts. Voyons comment. 

## Portée des variables en JavaScript

En JavaScript, nous utilisons la portée comme moyen d'identifier où et si nous pouvons utiliser une variable. Les variables peuvent exister dans un bloc, à l'intérieur d'une fonction, ou à l'extérieur d'une fonction et d'un bloc.

Alors, qu'est-ce qu'un bloc ? Un bloc (c'est-à-dire un bloc de code) est une section du code que nous définissons en utilisant une paire d'accolades ({...}). Quelque chose comme ceci :

```js
{
  let name = "alex";
}

```

D'autre part, une fonction est un ensemble d'instructions de code que vous souhaitez regrouper logiquement.

Habituellement, vous définissez une fonction en utilisant le mot-clé `function` et un nom. Soyez simplement conscient que vous pouvez définir une fonction sans nom, que nous appelons une `fonction anonyme`. Mais nous n'en discuterons pas dans l'article d'aujourd'hui pour simplifier.

Voici une fonction avec le nom `test`.

```js
function test() {
  let name = "alex";
}

```

Tout ce qui est en dehors d'un bloc ou d'une fonction, nous l'appellerons `Global`. Donc, lorsque nous déclarons des variables, elles peuvent exister dans un bloc, à l'intérieur d'une fonction, ou à l'extérieur d'un bloc/fonction – c'est-à-dire qu'elles ont une portée globale.

Il existe principalement trois types de portée :

* Portée de bloc  
* Portée fonctionnelle  
* Portée globale 

Les trois mots-clés `var`, `let` et `const` fonctionnent autour de ces portées. Alors, comprenons comment les choses s'emboîtent.

### Comment utiliser les variables JavaScript dans la portée de bloc

Si vous **ne voulez pas** qu'une variable déclarée à l'intérieur d'un bloc `{ }` soit accessible en dehors du bloc, vous devez les déclarer en utilisant les mots-clés `let` ou `const`. Les variables déclarées avec le mot-clé `var` à l'intérieur du bloc `{ }` **sont** également accessibles en dehors du bloc. Donc, soyez prudent.

Prenons un exemple :

```js
{
    let f_name  = 'Alex';
    const ZIP = 500067;
    var age = 25;
}

console.log(f_name); // Uncaught ReferenceError: f_name is not defined
console.log(ZIP);  // Uncaught ReferenceError: ZIP is not defined
console.log(age);  // 25
```

Comme vous le voyez, la valeur de la variable age peut être écrasée sans le savoir et éventuellement introduire un bug. Donc, la morale de l'histoire est,

> N'utilisez pas le mot-clé `var` à l'intérieur d'un bloc (portée de bloc). Utilisez toujours `let` et `const` à la place.

### Comment utiliser les variables JavaScript dans la portée fonctionnelle

Une variable déclarée à l'intérieur d'une fonction en utilisant ces mots-clés **n'est pas** accessible en dehors de la fonction. C'est la portée fonctionnelle appliquée.

C'est vrai, que vous utilisiez var, let ou const. À l'intérieur de la fonction, ils sont assez similaires dans la gestion de la portée d'une variable.

Prenons un exemple à nouveau :

```js
// f1() est une fonction

function f1() {
 let f_name = "Alex";
 const ZIP = 560089;
 var age = 25;   
}

f1();

console.log(f_name); // Uncaught ReferenceError: f_name is not defined
console.log(ZIP);  // Uncaught ReferenceError: ZIP is not defined
console.log(age);  // Uncaught ReferenceError: age is not defined
```

Comme vous le voyez ci-dessus, aucune des variables n'est accessible en dehors de la fonction, pas même `age` qui est déclaré en utilisant `var`. Donc, la conclusion est,

> La variable déclarée avec `var` à l'intérieur d'une fonction n'est pas accessible en dehors de celle-ci. Le mot-clé `var` a une portée fonctionnelle.

### Comment utiliser les variables JavaScript dans la portée globale

Les variables déclarées en dehors de toute fonction et de tout bloc sont `globales` et sont dites avoir une `portée globale`. Cela signifie que vous pouvez y accéder depuis n'importe quelle partie du programme JavaScript actuel. 

Vous pouvez utiliser `var`, `let` et `const` pour déclarer des variables globales. Mais vous ne devriez pas le faire trop souvent.

```js
let f_name = "Alex";
 const ZIP = 560089;
 var age = 25;  

// f1() est une fonction
function f1() {
  console.log(f_name); // Alex
  console.log(ZIP);  // 560089
  console.log(age);  // 25
}

f1();

console.log(f_name); // Alex
console.log(ZIP);  // 560089
console.log(age);  // 25
```

Comme vous le voyez, les variables sont accessibles partout. 

Donc, pour restreindre la portée d'une variable en utilisant les mots-clés `var`, `let` et `const`, voici l'ordre d'accessibilité dans la portée en commençant par le plus bas :

* `var` : Le niveau de portée fonctionnelle 
* `let` : Le niveau de portée de bloc 
* `const` : Le niveau de portée de bloc

L'image ci-dessous montre une carte mentale de ces trois mots-clés en référence aux différentes portées.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/28.png)

Passons au concept suivant pour comprendre comment ces trois mots-clés influencent le comportement du code lorsque nous réassignons une nouvelle valeur à une variable.

## Comment réassigner une nouvelle valeur à une variable en JavaScript

Une fois que vous avez déclaré une variable avec `var` ou `let`, vous **pouvez** réassigner une nouvelle valeur à la variable dans votre flux de programmation. C'est possible si la variable est accessible pour assigner une valeur. Mais avec `const`, vous **ne pouvez pas** réassigner une nouvelle valeur du tout.

```js
// Déclarer des variables avec des valeurs initiales
let f_name = "Alex";
const ZIP = 560089;
var age = 25;

// Réassigner des valeurs
f_name = "Bob"; // la valeur de f_name est 'Bob"
ZIP = 65457; // Uncaught TypeError: Assignment to constant variable.
age = 78; // la valeur de age est 78
```

Il y a une partie délicate avec `const` dont vous devez être conscient. Lorsqu'un objet est déclaré et qu'une valeur lui est assignée avec `const`, vous pouvez toujours changer la valeur de ses `propriétés`. Mais vous ne pouvez pas réassigner une autre valeur d'objet à la même variable. C'est une erreur courante que font de nombreux développeurs.

Consultez l'exemple ici :

```js
const blog = {
    'url': 'https://greenroots.info'
}

blog.url = 'https://blog.greenroots.info'; // Autorisé

blog = {}; // Uncaught TypeError: Assignment to constant variable.
```

Voici une carte mentale pour vous aider à comprendre comment fonctionne la réassignation pour les variables déclarées avec ces trois mots-clés.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/29-1.png)

## Que se passe-t-il lorsque vous accédez à une variable avant de la déclarer en JavaScript

En tant que programmeur pragmatique, vous ne devriez jamais essayer d'accéder à une variable sans la déclarer. Mais au cas où cela arriverait, voyons comment la variable peut se comporter.

Avec `var` en mode non strict, la variable aura une valeur `undefined`. Cela signifie qu'une variable a été déclarée mais n'a pas de valeur assignée. 

En mode strict, vous obtiendrez une `ReferenceError` indiquant que la variable n'est pas déclarée.

Avec `let` et `const`, si vous essayez d'accéder à une variable avant de la déclarer, vous obtiendrez toujours une `ReferenceError`.

Voici à nouveau une carte mentale pour vous aider à comprendre visuellement. Dans la carte mentale, `var` est représenté pour le mode non strict.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/30.png)

C'est tout, mes amis. Vous devez considérer ces circonstances et concepts pour évaluer comment `var`, `let` et `const` se comportent. Donc, la règle est :

* N'utilisez plus `var`. 
* Utilisez `let` ou `const`. 
* Utilisez `const` plus souvent. Utilisez `let` lorsque vous devez réassigner une autre valeur à une variable.
* N'essayez pas d'accéder à une variable sans la déclarer.

## Avant de terminer...

Voici l'histoire derrière `let`, `const` et `var`. J'espère que vous avez trouvé l'article perspicace et informatif. Mes DM sont ouverts sur `Twitter` si vous souhaitez discuter davantage.

Restons en contact. Je partage mes apprentissages sur JavaScript, le développement Web et le blogging sur ces plateformes également :

* [Suivez-moi sur Twitter](https://twitter.com/tapasadhikary)
* [Abonnez-vous à ma chaîne YouTube](https://www.youtube.com/tapasadhikary?sub_confirmation=1)
* [Projets secondaires sur GitHub](https://github.com/atapas)

À bientôt avec mon prochain article. En attendant, prenez soin de vous et restez heureux.