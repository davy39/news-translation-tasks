---
title: Quand (et pourquoi) utiliser les fonctions fléchées ES6 — et quand ne pas le
  faire
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-05T16:44:13.000Z'
originalURL: https://freecodecamp.org/news/when-and-why-you-should-use-es6-arrow-functions-and-when-you-shouldnt-3d851d7f0b26
coverImage: https://cdn-media-1.freecodecamp.org/images/1*GRUP3Ml4piJhZQ8EOHkFDA.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Quand (et pourquoi) utiliser les fonctions fléchées ES6 — et quand ne pas
  le faire
seo_desc: 'By Cynthia Lee

  Arrow functions (also called “fat arrow functions”) are undoubtedly one of the more
  popular features of ES6. They introduced a new way of writing concise functions.

  Here is a function written in ES5 syntax:

  function timesTwo(params) {

  ...'
---

Par Cynthia Lee

Les fonctions fléchées (également appelées « fonctions fléchées grasses ») sont sans doute l'une des fonctionnalités les plus populaires d'ES6. Elles ont introduit une nouvelle façon d'écrire des fonctions concises.

Voici une fonction écrite en syntaxe ES5 :

```js
function timesTwo(params) {
  return params * 2
}

timesTwo(4);  // 8
```

Maintenant, voici la même fonction exprimée sous forme de fonction fléchée :

```js
var timesTwo = params => params * 2

timesTwo(4);  // 8
```

C'est beaucoup plus court ! Nous pouvons omettre les accolades et l'instruction return grâce aux retours implicites (mais seulement s'il n'y a pas de bloc — plus d'informations à ce sujet ci-dessous).

Il est important de comprendre comment la fonction fléchée se comporte différemment par rapport aux fonctions ES5 régulières.

### Variations

![Image](https://cdn-media-1.freecodecamp.org/images/c1-i0BPczDkbeDybCAzWCHsEyVFX0Ttg5bpL)
_La variété est le sel de la vie_

Une chose que vous remarquerez rapidement est la variété des syntaxes disponibles dans les fonctions fléchées. Passons en revue quelques-unes des plus courantes :

#### 1. Aucun paramètre

Si aucun paramètre n'est présent, vous pouvez placer des parenthèses vides avant `=>`.

```js
() => 42
```

En fait, vous n'avez même pas besoin des parenthèses !

```js
_ => 42
```

#### 2. Paramètre unique

Avec ces fonctions, les parenthèses sont facultatives :

```js
x => 42  || (x) => 42
```

#### **3. Plusieurs paramètres**

Les parenthèses sont requises pour ces fonctions :

```js
(x, y) => 42
```

#### **4. Instructions (par opposition aux expressions)**

Dans sa forme la plus basique, une _expression de fonction_ produit une valeur, tandis qu'une _instruction de fonction_ effectue une action.

Avec la fonction fléchée, il est important de se rappeler que les instructions doivent avoir des accolades. Une fois les accolades présentes, vous devez toujours écrire `return` également.

Voici un exemple de la fonction fléchée utilisée avec une instruction if :

```js
var feedTheCat = (cat) => {
  if (cat === 'hungry') {
    return 'Feed the cat';
  } else {
    return 'Do not feed the cat';
  }
}
```

#### **5. « Corps de bloc »**

Si votre fonction est dans un bloc, vous devez également utiliser l'instruction `return` explicite :

```js
var addValues = (x, y) => {
  return x + y
}
```

#### **6. Littéraux d'objet**

Si vous retournez un littéral d'objet, il doit être enveloppé dans des parenthèses. Cela force l'interpréteur à évaluer ce qui se trouve à l'intérieur des parenthèses, et le littéral d'objet est retourné.

```js
x =>({ y: x })
```

### Syntactiquement anonyme

![Image](https://cdn-media-1.freecodecamp.org/images/hS7maItiZiV0IIYACtt0PiD3VStILiS1n4sd)

Il est important de noter que les fonctions fléchées sont anonymes, ce qui signifie qu'elles n'ont pas de nom.

Cette anonymité crée certains problèmes :

1. Plus difficile à déboguer

Lorsque vous obtenez une erreur, vous ne pourrez pas tracer le nom de la fonction ou le numéro exact de la ligne où elle s'est produite.

2. Pas d'auto-référence

Si votre fonction doit avoir une auto-référence à un moment donné (par exemple, récursion, gestionnaire d'événements qui doit se désengager), elle ne fonctionnera pas.

### Principal avantage : Pas de liaison de 'this'

![Image](https://cdn-media-1.freecodecamp.org/images/3Rc2e8J5whHdFrH3IzPckp5GCQ-QtMvEOH1k)
_Photo par [Unsplash](https://unsplash.com/@davideragusa?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">davide ragusa</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Dans les expressions de fonction classiques, le mot-clé `this` est lié à différentes valeurs en fonction du _contexte_ dans lequel il est appelé. Avec les fonctions fléchées, cependant, `this` est _lié lexicalement_. Cela signifie qu'il utilise `this` du code qui contient la fonction fléchée.

Par exemple, regardez la fonction `setTimeout` ci-dessous :

```js
// ES5
var obj = {
  id: 42,
  counter: function counter() {
    setTimeout(function() {
      console.log(this.id);
    }.bind(this), 1000);
  }
};
```

Dans l'exemple ES5, `.bind(this)` est requis pour aider à passer le contexte `this` dans la fonction. Sinon, par défaut `this` serait indéfini.

```js
// ES6
var obj = {
  id: 42,
  counter: function counter() {
    setTimeout(() => {
      console.log(this.id);
    }, 1000);
  }
};
```

Les fonctions fléchées ES6 ne peuvent pas être liées à un mot-clé `this`, donc elles remontent lexicalement d'une portée et utilisent la valeur de `this` dans la portée dans laquelle elles ont été définies.

### Quand ne pas utiliser les fonctions fléchées

Après avoir appris un peu plus sur les fonctions fléchées, j'espère que vous comprenez qu'elles ne remplacent pas les fonctions régulières.

Voici quelques cas où vous ne voudriez probablement pas les utiliser :

1. Méthodes d'objet

Lorsque vous appelez `cat.jumps`, le nombre de vies ne diminue pas. C'est parce que `this` n'est lié à rien et héritera de la valeur de `this` de sa portée parente.

```js
var cat = {
  lives: 9,
  jumps: () => {
    this.lives--;
  }
}
```

2. Fonctions de rappel avec contexte dynamique

Si vous avez besoin que votre contexte soit dynamique, les fonctions fléchées ne sont pas le bon choix. Regardez ce gestionnaire d'événements ci-dessous :

```js
var button = document.getElementById('press');
button.addEventListener('click', () => {
  this.classList.toggle('on');
});
```

Si nous cliquons sur le bouton, nous obtiendrions une erreur TypeError. C'est parce que `this` n'est pas lié au bouton, mais plutôt à sa portée parente.

3. Quand cela rend votre code moins lisible

Il vaut la peine de prendre en considération la variété de syntaxes que nous avons couvertes précédemment. Avec les fonctions régulières, les gens savent à quoi s'attendre. Avec les fonctions fléchées, il peut être difficile de déchiffrer ce que vous regardez immédiatement.

### Quand les utiliser

Les fonctions fléchées brillent particulièrement dans tout ce qui nécessite que `this` soit lié au contexte, et non à la fonction elle-même.

Malgré le fait qu'elles soient anonymes, j'aime aussi les utiliser avec des méthodes telles que `map` et `reduce`, car je pense que cela rend mon code plus lisible. Pour moi, les avantages l'emportent sur les inconvénients.

Merci d'avoir lu mon article, et partagez si vous l'avez aimé ! Consultez mes autres articles comme [Comment j'ai construit mon application Pomodoro Clock, et les leçons que j'ai apprises en cours de route](https://www.freecodecamp.org/news/how-i-built-my-pomodoro-clock-app-and-the-lessons-i-learned-along-the-way-51288983f5ee/), et [Démystifions le mot-clé 'new' de JavaScript](https://www.freecodecamp.org/news/demystifying-javascripts-new-keyword-874df126184c/).