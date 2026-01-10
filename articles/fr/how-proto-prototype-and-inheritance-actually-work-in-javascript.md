---
title: Comment __proto__, prototype et l'héritage fonctionnent réellement en JavaScript
subtitle: ''
author: Shejan Mahamud
co_authors: []
series: null
date: '2025-11-04T16:44:51.663Z'
originalURL: https://freecodecamp.org/news/how-proto-prototype-and-inheritance-actually-work-in-javascript
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1762210692821/651a67f9-cbe5-4f09-b048-957caaa5e1ac.png
tags:
- name: JavaScript
  slug: javascript
- name: inheritence
  slug: inheritence
- name: prototypeal-inheritance
  slug: prototypeal-inheritance
- name: Object Oriented Programming
  slug: object-oriented-programming
seo_title: Comment __proto__, prototype et l'héritage fonctionnent réellement en JavaScript
seo_desc: 'Have you ever wondered why everything in JavaScript acts like an object?
  Or how inheritance actually works behind the scenes? What''s the difference between
  __proto__ and prototype?

  If these questions have crossed your mind, you''re not alone. These ar...'
---

Vous êtes-vous déjà demandé pourquoi tout en JavaScript se comporte comme un objet ? Ou comment l'héritage fonctionne réellement en coulisses ? Quelle est la différence entre `__proto__` et `prototype` ?

Si ces questions vous ont déjà traversé l'esprit, vous n'êtes pas seul. Ce sont certains des concepts les plus fondamentaux de JavaScript, et pourtant ils déroutent souvent les développeurs.

Dans ce tutoriel, nous allons démystifier les prototypes, les chaînes de prototypes et l'héritage en JavaScript. À la fin, vous comprendrez le « quoi », le « pourquoi » et le « comment » du système de prototypes de JavaScript.

### Voici ce que je vais aborder :

* [Le mystère des méthodes de chaînes de caractères](#heading-le-mystere-des-methodes-de-chaines-de-caracteres)
    
* [Comment les objets fonctionnent en interne](#heading-comment-les-objets-fonctionnent-en-interne)
    
* [Comprendre la chaîne de prototypes](#heading-comprendre-la-chaine-de-prototypes)
    
* [Pourquoi tout est un objet en JavaScript](#heading-pourquoi-tout-est-un-objet-en-javascript)
    
* [La différence entre __proto__ et prototype](#heading-la-difference-entre-proto-et-prototype)
    
* [Comment les prototypes fonctionnent avec les fonctions](#heading-comment-les-prototypes-fonctionnent-avec-les-fonctions)
    
* [Comment les prototypes fonctionnent avec les classes](#heading-comment-les-prototypes-fonctionnent-avec-les-classes)
    
* [Conclusion](#heading-conclusion)
    

## Prérequis

Pour tirer le meilleur parti de ce tutoriel, vous devriez avoir :

* Une compréhension de base des fondamentaux de JavaScript
    
* Une familiarité avec les objets, les fonctions et les classes en JavaScript
    
* La connaissance de la déclaration et de l'utilisation des variables
    
* Une expérience de travail avec le mot-clé `new` (utile mais pas obligatoire)
    

## Le mystère des méthodes de chaînes de caractères

Commençons par un exemple simple qui démontre quelque chose d'intéressant à propos de JavaScript :

```javascript
let name = "Shejan Mahamud";
```

Après avoir déclaré cette variable, nous pouvons utiliser des méthodes de String comme :

```javascript
name.toLowerCase(); // "shejan mahamud"
name.toUpperCase(); // "SHEJAN MAHAMUD"
```

Cela semble normal au premier abord, mais attendez – quelque chose d'inhabituel se produit. Remarquez-vous quelque chose d'étrange ici ? Nous utilisons la notation pointée sur une primitive de chaîne.

Voici la partie intrigante : nous savons que les chaînes sont des types primitifs en JavaScript, pas des objets. Alors, comment pouvons-nous utiliser la notation pointée pour accéder à des méthodes ? Après tout, la notation pointée ne fonctionne généralement qu'avec les objets.

La réponse à ce mystère réside dans la compréhension de la manière dont JavaScript gère les primitives et les prototypes. Mais avant d'en arriver là, examinons d'abord comment les objets fonctionnent en interne.

## Comment les objets fonctionnent en interne

Lorsque vous créez un objet en JavaScript comme ceci :

```javascript
const info1 = {
  fName: "Shejan",
  lName: "Mahamud"
};
```

JavaScript fait quelque chose d'intéressant en coulisses. Il ajoute automatiquement une propriété cachée appelée `__proto__` à votre objet. Cette propriété pointe vers `Object.prototype`, qui est le prototype de la classe intégrée Object.

Vous pourriez vous demander : est-ce que `Object.prototype` a aussi un `__proto__` ? Oui, c'est le cas, mais sa valeur est `null`. C'est parce que `Object.prototype` est au sommet de la chaîne de prototypes et n'hérite de rien d'autre.

Regardons un exemple plus complexe pour mieux comprendre cela :

```javascript
const info1 = {
  fName1: "Shejan",
  lName1: "Mahamud"
};

const info2 = {
  fName2: "Boltu",
  lName2: "Mia",
  __proto__: info1
};

const info3 = {
  fName3: "Habu",
  lName3: "Mia",
  __proto__: info2
};
```

Dans cet exemple, nous avons intentionnellement défini la propriété `__proto__` pour `info2` et `info3`. Maintenant, voici une question intéressante : pouvons-nous accéder à `fName1` depuis `info3` ?

```javascript
console.log(info3.fName1); // "Shejan"
```

Oui, nous le pouvons ! Comprenons comment cela fonctionne.

## Comprendre la chaîne de prototypes

Lorsque vous essayez d'accéder à une propriété sur un objet, JavaScript suit un processus de recherche spécifique :

1. D'abord, il cherche la propriété dans l'objet lui-même (l'objet de base)
    
2. S'il ne la trouve pas là, il regarde dans le `__proto__` de l'objet
    
3. S'il ne la trouve toujours pas, il continue à remonter la chaîne, en vérifiant chaque `__proto__` jusqu'à ce qu'il trouve la propriété ou atteigne `null`
    

Dans notre exemple avec `info3.fName1` :

* JavaScript regarde d'abord dans `info3` – et il ne trouve pas `fName1`
    
* Ensuite, il vérifie `info3.__proto__`, qui pointe vers `info2` – il ne trouve pas non plus `fName1` là-bas
    
* Ensuite, il vérifie `info2.__proto__`, qui pointe vers `info1` – et il trouve `fName1` ici !
    

C'est ce qu'on appelle la **chaîne de prototypes**, et c'est ainsi que l'héritage fonctionne en JavaScript. Voici une représentation visuelle :

```javascript
┌─────────────┐
│  info3      │
│ fName3      │
│ lName3      │
└────┬────────┘
     │ __proto__
     ▼
┌─────────────┐
│  info2      │
│ fName2      │
│ lName2      │
└────┬────────┘
     │ __proto__
     ▼
┌─────────────┐
│  info1      │
│ fName1      │
│ lName1      │
└────┬────────┘
     │ __proto__
     ▼
┌──────────────────┐
│ Object.prototype │
└────┬─────────────┘
     ▼
    null
```

Chaque objet pointe vers l'objet suivant dans la chaîne via sa propriété `__proto__`. Cette chaîne continue jusqu'à ce qu'elle atteigne `null`.

## Pourquoi tout est un objet en JavaScript

Résolvons maintenant le mystère par lequel nous avons commencé : comment les types primitifs peuvent-ils utiliser des méthodes d'objet ?

En JavaScript, presque tout se comporte comme un objet, même si les types primitifs (comme les chaînes, les nombres et les booléens) ne sont techniquement pas des objets. Cela fonctionne grâce à un processus appelé **auto-boxing** ou **objets wrappers**.

Voyons cela en action :

```javascript
let yourName = "Boltu";
```

Lorsque vous essayez d'utiliser une méthode sur cette chaîne :

```javascript
yourName.toLowerCase();
```

Voici ce que JavaScript fait en coulisses :

1. Il enveloppe temporairement la valeur primitive dans un objet wrapper : `new String("Boltu")`
    
2. Le `__proto__` de cet objet temporaire pointe automatiquement vers `String.prototype`
    
3. La méthode est trouvée dans `String.prototype` et exécutée
    
4. Une fois l'opération terminée, l'objet wrapper est jeté
    
5. `yourName` redevient une simple valeur primitive
    

C'est pourquoi vous pouvez utiliser des méthodes sur des primitives même si ce ne sont pas des objets. JavaScript crée un objet temporaire, l'utilise pour accéder à la méthode, puis s'en débarrasse.

Le même processus se produit avec d'autres types primitifs :

* Les nombres utilisent `Number.prototype`
    
* Les booléens utilisent `Boolean.prototype`
    

Et ainsi de suite. Ce système élégant est la raison pour laquelle les développeurs disent souvent que « tout en JavaScript est un objet » – même quand ce n'est pas techniquement vrai, il se comporte ainsi quand c'est nécessaire.

## La différence entre `__proto__` et `prototype`

C'est l'un des aspects les plus déroutants de JavaScript pour de nombreux développeurs. Décomposons-le clairement.

### Qu'est-ce que `prototype` ?

Lorsque vous créez une fonction ou une classe en JavaScript, le langage crée automatiquement un objet modèle appelé `prototype`. Cela se passe en coulisses.

Voici un exemple :

```javascript
function Person(name) {
  this.name = name;
}
```

Lorsque JavaScript voit cette fonction, il fait ceci en interne :

```javascript
Person.prototype = { 
  constructor: Person 
};
```

La fonction `Person` possède désormais une propriété cachée appelée `prototype`, qui est un objet contenant une propriété `constructor`.

Vous pouvez ajouter des méthodes à cet objet prototype :

```javascript
Person.prototype.sayHi = function() {
  console.log("Hi, I'm " + this.name);
};
```

### Qu'est-ce que `__proto__` ?

`__proto__` est une propriété qui existe sur chaque instance d'objet (tableaux, fonctions, objets – tout). C'est une référence interne ou un pointeur qui indique de quel prototype l'objet hérite.

Par défaut, lorsque vous créez un objet, son `__proto__` pointe vers `Object.prototype`.

### Comment ils travaillent ensemble

Lorsque vous utilisez le mot-clé `new` :

```javascript
const p1 = new Person("Shejan");
```

JavaScript effectue ces étapes en interne :

1. Crée un nouvel objet vide : `p1 = {}`
    
2. Définit le `__proto__` de l'objet : `p1.__proto__ = Person.prototype`
    
3. Appelle la fonction constructeur avec le nouvel objet : `Person.call(p1, "Shejan")`
    
4. Retourne l'objet : `return p1`
    

Maintenant, quand vous essayez d'accéder à une méthode :

```javascript
p1.sayHi(); // "Hi, I'm Shejan"
```

JavaScript cherche d'abord `sayHi` dans `p1`. Lorsqu'il ne le trouve pas, il vérifie `p1.__proto__`, qui pointe vers `Person.prototype`, où la méthode est définie.

La relation peut être exprimée ainsi :

```javascript
p1.__proto__ === Person.prototype; // true
Person.prototype.constructor === Person; // true
```

**En résumé :**

* `prototype` est une propriété des fonctions/classes qui sert de modèle pour les instances
    
* `__proto__` est une propriété des instances d'objets qui pointe vers le prototype dont elles héritent
    

## Comment les prototypes fonctionnent avec les fonctions

Voyons un exemple complet avec des fonctions :

```javascript
function Person(name, age) {
  this.name = name;
  this.age = age;
}

// Ajout d'une méthode au prototype
Person.prototype.introduce = function() {
  console.log(`Hi, I'm ${this.name} and I'm ${this.age} years old.`);
};

// Création d'instances
const person1 = new Person("Alice", 25);
const person2 = new Person("Bob", 30);

person1.introduce(); // "Hi, I'm Alice and I'm 25 years old."
person2.introduce(); // "Hi, I'm Bob and I'm 30 years old."

// Les deux instances partagent le même prototype
console.log(person1.__proto__ === Person.prototype); // true
console.log(person2.__proto__ === Person.prototype); // true
console.log(person1.__proto__ === person2.__proto__); // true
```

Le principal avantage ici est l'efficacité de la mémoire : la méthode `introduce` n'existe qu'une seule fois dans `Person.prototype`, mais toutes les instances peuvent y accéder via la chaîne de prototypes.

## Comment les prototypes fonctionnent avec les classes

L'ES6 a introduit la syntaxe `class`, qui semble différente mais fonctionne de la même manière sous le capot :

```javascript
class User {
  constructor(name) {
    this.name = name;
  }
  
  sayHi() {
    console.log(`Hi, I'm ${this.name}`);
  }
}

const user1 = new User("Charlie");
user1.sayHi(); // "Hi, I'm Charlie"

// Vérifions ce qui se passe réellement
console.log(typeof User); // "function"
console.log(User.prototype); // { sayHi: f, constructor: f User() }
console.log(user1.__proto__ === User.prototype); // true
```

Les classes sont essentiellement du sucre syntaxique sur l'héritage basé sur les prototypes de JavaScript. En interne :

* Une classe est toujours une fonction constructeur
    
* Les méthodes définies dans la classe sont ajoutées à `ClassName.prototype`
    
* Les instances créées avec `new` ont leur `__proto__` défini sur le prototype de la classe
    

Cela signifie que tout ce que nous avons appris sur les prototypes de fonctions s'applique également aux classes.

## Conclusion

Comprendre les prototypes et la chaîne de prototypes est fondamental pour maîtriser JavaScript. Ces concepts forment la base de la manière dont JavaScript implémente l'héritage et la programmation orientée objet.

### Points clés à retenir

Récapitulons ce que nous avons appris :

1. **Chaque objet possède** `__proto__` : Cette propriété pointe vers le prototype dont l'objet hérite, activant le mécanisme de recherche de la chaîne de prototypes.
    
2. **Les fonctions et les classes possèdent** `prototype` : Cette propriété sert de modèle pour les instances créées avec le mot-clé `new`.
    
3. **La chaîne de prototypes permet l'héritage** : Lorsque JavaScript ne trouve pas une propriété sur un objet, il remonte la chaîne de prototypes jusqu'à ce qu'il trouve la propriété ou atteigne `null`.
    
4. **Les primitives utilisent des objets wrappers** : Même si les primitives ne sont pas des objets, JavaScript les enveloppe temporairement dans des objets pour donner accès aux méthodes.
    
5. **Les classes sont du sucre syntaxique** : La syntaxe moderne `class` est plus propre, mais elle utilise toujours des prototypes sous le capot.
    

JavaScript peut sembler original au début, mais une fois que vous comprenez comment il fonctionne sous le capot, vous apprécierez sa conception élégante et flexible.

Bon codage !