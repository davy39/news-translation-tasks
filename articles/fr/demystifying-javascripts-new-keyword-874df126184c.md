---
title: Démystifions le mot-clé 'new' de JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-24T00:33:18.000Z'
originalURL: https://freecodecamp.org/news/demystifying-javascripts-new-keyword-874df126184c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yF1csYj3s_p4lBZW8L0iCA.jpeg
tags:
- name: code
  slug: code
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Démystifions le mot-clé 'new' de JavaScript
seo_desc: 'By Cynthia Lee

  Over the weekend, I completed Will Sentance’s JavaScript: The Hard Parts. It might
  not sound like the most glorious way to spend a weekend, but I actually found it
  pretty fun and relaxing to complete the course. It touched on functiona...'
---

Par Cynthia Lee

Ce week-end, j'ai terminé [JavaScript: The Hard Parts](https://frontendmasters.com/courses/javascript-hard-parts/) de Will Sentance. Cela ne semble peut-être pas être la façon la plus glorieuse de passer un week-end, mais j'ai trouvé cela plutôt amusant et relaxant de suivre ce cours. Il abordait la programmation fonctionnelle, les fonctions d'ordre supérieur, les fermetures et JavaScript asynchrone.

Pour moi, le point fort du cours était la manière dont il a développé les approches JavaScript de la programmation orientée objet (POO) et démystifié la magie derrière l'opérateur **new**. J'ai maintenant une compréhension bien arrondie de ce qui se passe sous le capot lorsque l'opérateur **new** est utilisé.

### Programmation Orientée Objet en **JavaScript**

![Image](https://cdn-media-1.freecodecamp.org/images/OjGA-narSWLOzyUTLWqTITXh4qD6KIcE36ag)
_Photo par [Unsplash](https://unsplash.com/@nickkarvounis?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Nick Karvounis</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

La Programmation Orientée Objet (POO) est un paradigme de programmation basé sur le concept d'« objets ». Les données et les fonctions (attributs et méthodes) sont regroupées au sein d'un objet.

Un objet en JavaScript est une collection de paires clé-valeur. Ces paires clé-valeur sont des propriétés de l'objet. Une propriété peut être un tableau, une fonction, un objet lui-même ou tout type de données primitif tel que des chaînes de caractères ou des entiers.

Quelles techniques avons-nous dans notre boîte à outils JavaScript pour la création d'objets ?

Supposons que nous créons des utilisateurs dans un jeu que nous venons de concevoir. Comment stockerions-nous les détails des utilisateurs tels que leurs noms, leurs points, et implémenterions-nous des méthodes telles qu'une incrémentation de points ? Voici deux options pour la création d'objets de base.

#### **Option 1 — Notation littérale d'objet**

```js
let user1 = {
  name: "Taylor",
  points: 5,
  increment: function() {
    user1.points++;
  }
};
```

Un littéral d'objet JavaScript est une liste de paires nom-valeur enveloppées dans des accolades. Dans l'exemple ci-dessus, l'objet 'user1' est créé, et les données associées sont stockées à l'intérieur.

#### **Option 2 — Object.create()**

`Object.create(proto, [ propertiesObject ])`

Les méthodes `Object.create` acceptent deux arguments :

1. proto : l'objet qui devrait être le prototype du nouvel objet créé. Il doit s'agir d'un objet ou null.
2. propertiesObject : propriétés du nouvel objet. Cet argument est facultatif.

En gros, vous passez à `Object.create` un objet dont vous voulez hériter, et il retourne un nouvel objet qui hérite de l'objet que vous avez passé.

```js
let user2 = Object.create(null);

user2.name = "Cam";
user2.points = 8;
user2.increment = function() {
  user2.points++;
}
```

Les options de création d'objets de base ci-dessus sont répétitives. Chaque objet doit être créé manuellement.

Comment surmonter cela ?

### Solutions

#### **Solution 1 — Générer des objets en utilisant une fonction**

Une solution simple est d'écrire une fonction pour créer de nouveaux utilisateurs.

```js
function createUser(name, points) {
  let newUser = {};
  newUser.name = name;
  newUser.points = points;
  newUser.increment = function() {
    newUser.points++;
  };
  return newUser;
}
```

Pour créer un utilisateur, vous entreriez maintenant les informations dans les paramètres de la fonction.

```js
let user1 = createUser("Bob", 5);
user1.increment();
```

Cependant, la fonction increment dans l'exemple ci-dessus est juste une copie de la fonction increment originale. Ce n'est pas une bonne façon d'écrire votre code, car toute modification potentielle de la fonction devra être faite manuellement pour chaque objet.

#### **Solution 2 — Utiliser la nature prototypale de JavaScript**

Contrairement aux langages orientés objet comme Python et Java, JavaScript n'a pas de classes. Il utilise le concept de prototypes et de chaînage de prototypes pour l'héritage.

Lorsque vous créez un nouveau tableau, vous avez automatiquement accès à des méthodes intégrées telles que `Array.join`, `Array.sort`, et `Array.filter`. Cela est dû au fait que les objets de tableau héritent des propriétés de Array.prototype.

![Image](https://cdn-media-1.freecodecamp.org/images/CHrqNxf5I7tIo4-CfbSXqC6fnDd2H273ieWJ)
_Crédit image : [JavaScript Prototype Chains, Scope Chains, and Performance ](https://www.toptal.com/javascript/javascript-prototypes-scopes-and-performance-what-you-need-to-know" rel="noopener" target="_blank" title=") par Diego Castorina_

Chaque fonction JavaScript a une propriété prototype, qui est vide par défaut. Vous pouvez ajouter des fonctions à cette propriété prototype, et sous cette forme, elle est connue comme une méthode. Lorsque qu'une fonction héritée est exécutée, la valeur de this pointe vers l'objet héritant.

```js
function createUser(name, points) {
  let newUser = Object.create(userFunction);
  newUser.name = name;
  newUser.points = points;
  return newUser;
}

let userFunction = {
  increment: function() {this.points++};
  login: function() {console.log("Veuillez vous connecter.")};
}

let user1 = createUser("Bob", 5);
user1.increment();
```

Lorsque l'objet `user1` a été créé, un lien de chaîne de prototype avec userFunction a été formé.

Lorsque `user1.increment()` est dans la pile d'appels, l'interpréteur cherchera user1 dans la mémoire globale. Ensuite, il cherchera la fonction increment, mais ne la trouvera pas. L'interpréteur regardera l'objet suivant dans la chaîne de prototypes et trouvera la fonction increment là.

#### **Solution 3 — Mots-clés _new_ et _this_**

![Image](https://cdn-media-1.freecodecamp.org/images/OQKKYIojqDyXBnOwHdtZfxKL8YMOCii-2GTl)

L'opérateur **new** est utilisé pour créer une instance d'un objet qui a une fonction constructeur.

Lorsque nous appelons la fonction constructeur avec new, nous automatisons les actions suivantes :

* Un nouvel objet est créé
* Il lie `this` à l'objet
* L'objet prototype de la fonction constructeur devient la propriété __proto__ du nouvel objet
* Il retourne l'objet de la fonction

C'est fantastique, car l'automatisation entraîne moins de code répétitif !

```js
function User(name, points) {
 this.name = name; 
 this.points = points;
}
User.prototype.increment = function(){
 this.points++;
}
User.prototype.login = function() {
 console.log("Veuillez vous connecter.")
}

let user1 = new User("Dylan", 6);
user1.increment();
```

En utilisant le modèle de prototype, chaque méthode et propriété est ajoutée directement sur le prototype de l'objet.

L'interpréteur remontera la chaîne prototypale et trouvera la fonction increment sous la propriété prototype de User, qui est elle-même également un objet avec les informations à l'intérieur. Rappelez-vous — **Toutes les fonctions en JavaScript sont également des objets**. Maintenant que l'interpréteur a trouvé ce dont il a besoin, il peut créer un nouveau contexte d'exécution local pour exécuter `user1.increment()`.

**Note de côté : Différence entre __proto__ et prototype**

Si vous êtes déjà confus à propos de __proto__ et prototype, ne vous inquiétez pas ! Vous êtes loin d'être le seul à être confus à ce sujet.

Prototype est une propriété de la fonction constructeur qui détermine ce qui deviendra la propriété __proto__ sur l'objet construit.

Ainsi, __proto__ est la référence créée, et cette référence est connue sous le nom de lien de chaîne de prototype.

#### **Solution 4 — Le 'syntactic sugar' d'ES6**

![Image](https://cdn-media-1.freecodecamp.org/images/svX1DgD7SmEqaQLIchi26EuKUV4toaacQSJG)

D'autres langages nous permettent d'écrire nos méthodes partagées au sein de l'objet 'constructeur' lui-même. ECMAScript6 a introduit le mot-clé **class**, qui nous permet d'écrire des classes qui ressemblent aux classes normales d'autres langages classiques. En réalité, il s'agit d'un sucre syntaxique sur le comportement prototypal de JavaScript.

```js
class User {
  constructor(name, points) {
    this.name = name;
    this.points = points;
  }
  increment () {
    this.points++;
  }
  login () {
    console.log("Veuillez vous connecter.")
  }
}

let user1 = new User("John", 12);
user1.increment();
```

Dans la solution 3, les méthodes associées étaient précisément implémentées en utilisant `User.prototype.functionName`. Dans cette solution, les mêmes résultats sont obtenus mais la syntaxe semble plus propre.

### **Conclusion**

Nous avons maintenant appris davantage sur les différentes options que nous avons en JavaScript pour créer des objets. Bien que les déclarations de **class** et l'opérateur **new** soient relativement faciles à utiliser, il est important de comprendre ce qui est automatisé.

Pour résumer, les actions suivantes sont automatisées lorsque la fonction constructeur est appelée avec **new** :

* Un nouvel objet est créé
* Il lie `this` à l'objet
* L'objet prototype de la fonction constructeur devient la propriété __proto__ du nouvel objet
* Il retourne l'objet de la fonction

Merci d'avoir lu mon article, et applaudissez si vous l'avez aimé ! Consultez mes autres articles comme [Comment j'ai construit mon application Pomodoro Clock, et les leçons que j'ai apprises en cours de route](https://medium.freecodecamp.org/how-i-built-my-pomodoro-clock-app-and-the-lessons-i-learned-along-the-way-51288983f5ee).