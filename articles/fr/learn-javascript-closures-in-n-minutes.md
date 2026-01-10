---
title: Apprendre les closures JavaScript en 6 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-07T07:00:00.000Z'
originalURL: https://freecodecamp.org/news/learn-javascript-closures-in-n-minutes
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/cover-card.png
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
- name: technology
  slug: technology
seo_title: Apprendre les closures JavaScript en 6 minutes
seo_desc: "By Yazeed Bzadough\nClosures are a notoriously difficult to grasp. But\
  \ they are vital to advancing as a JavaScript developer. \nUnderstanding closures\
  \ can lead to more elegant code and better job opportunities.\nI hope this post\
  \ helps the concept stick ..."
---

Par Yazeed Bzadough

Les closures sont notoirement difficiles à comprendre. Mais elles sont essentielles pour progresser en tant que développeur JavaScript. 

Comprendre les closures peut mener à un code plus élégant et à de meilleures opportunités d'emploi.

J'espère que cet article aidera à assimiler le concept le plus rapidement possible.

**BONUS** : Les closures ne sont pas spécifiques à JS ! Ce sont un concept d'informatique que - une fois que vous les aurez apprises - vous commencerez à reconnaître partout ailleurs dans le développement logiciel.

## Les fonctions sont aussi des valeurs
Tout d'abord, comprenez que JavaScript supporte les _fonctions de première classe_.

![winnie-1](https://www.freecodecamp.org/news/content/images/2019/08/winnie-1.jpeg)

Un nom sophistiqué, mais cela signifie simplement que les fonctions _sont traitées comme n'importe quelle autre valeur_. Des valeurs comme les chaînes de caractères, les nombres et les objets.

Que pouvez-vous faire avec les valeurs ?

### Les valeurs peuvent être des variables
```js
const name = 'Yazeed';
const age = 25;
const fullPerson = {
    name: name,
    age: age
};
```

### Les valeurs peuvent être dans des tableaux
```js
const items = [
    'Yazeed',
    25,
    { name: 'Yazeed', age: 25 }
]
```

### Les valeurs peuvent être retournées par des fonctions
```js
function getPerson() {
    return [
        'Yazeed',
        25,
        { name: 'Yazeed', age: 25 }
    ];
}
```

Devinez quoi ? Les fonctions peuvent aussi faire tout cela.

![functions-can-do-that-too](https://www.freecodecamp.org/news/content/images/2019/08/functions-can-do-that-too.jpeg)

### Les fonctions peuvent être des variables
```js
const sayHi = function(name) {
    return `Hi, ${name}!`;
}
```

### Les fonctions peuvent être dans des tableaux
```js
const myFunctions = [
    function sayHi(name) {
        return `Hi, ${name}!`;
    },
    function add(x, y) {
        return x + y;
    }
];
```

Et voici le plus important...

## Les fonctions peuvent retourner d'autres fonctions
Une fonction qui retourne une autre fonction a un nom spécial. Elle est appelée une fonction _d'ordre supérieur_.

C'est la base sur laquelle les closures reposent. Voici notre premier exemple de fonction _d'ordre supérieur_.

```js
function getGreeter() {
    return function() {
        return 'Hi, Jerome!';
    };
}
```

`getGreeter` retourne une fonction. Pour être salué, appelez-la deux fois.

```js
getGreeter(); // Retourne une fonction
getGreeter()(); // Hi, Jerome!
```

Un appel pour la fonction retournée, et un autre pour le salut.

Vous pouvez la stocker dans une variable pour une réutilisation plus facile.

```js
const greetJerome = getGreeter();

greetJerome(); // Hi, Jerome!
greetJerome(); // Hi, Jerome!
greetJerome(); // Hi, Jerome!
```

## Obtenez une closure
Maintenant, pour la grande révélation.

Au lieu de coder en dur Jerome, nous allons rendre `getGreeter` dynamique en acceptant un paramètre appelé `name`.

```js
// Nous pouvons saluer n'importe qui maintenant !
function getGreeter(name) {
    return function() {
        return `Hi, ${name}!`;
    };
}
```

Et l'utiliser comme ceci...

```js
const greetJerome = getGreeter('Jerome');
const greetYazeed = getGreeter('Yazeed');

greetJerome(); // Hi, Jerome!
greetYazeed(); // Hi, Yazeed!
```

![fallout-hold-up](https://www.freecodecamp.org/news/content/images/2019/08/fallout-hold-up.jpg)

Regardez ce code à nouveau.

```js
function getGreeter(name) {
    return function() {
        return `Hi, ${name}!`;
    };
}
```

## Nous avons utilisé une closure
La fonction _externe_ prend `name`, mais la fonction _interne_ l'utilise plus tard. C'est le pouvoir des closures.

Quand une fonction retourne, son cycle de vie est terminé. Elle ne peut plus effectuer de travail, et ses variables locales sont nettoyées.

_Sauf_ si elle retourne une autre fonction. Si cela se produit, alors la fonction retournée a toujours accès à ces variables externes, même après que la fonction parente a disparu.

## Avantages des closures
![why-do-i-care](https://www.freecodecamp.org/news/content/images/2019/08/why-do-i-care.jpeg)

Comme je l'ai dit, les closures peuvent faire passer votre jeu de développeur au niveau supérieur. Voici quelques utilisations pratiques.

## 1. Confidentialité des données
La confidentialité des données est essentielle pour partager du code en toute sécurité.

Sans elle, toute personne utilisant votre fonction/bibliothèque/framework peut manipuler malicieusement ses variables internes.

### Une banque sans confidentialité
Considérez ce code qui gère un compte bancaire. Le `accountBalance` est exposé globalement !

```js
let accountBalance = 0;
const manageBankAccount = function() {
    return {
        deposit: function(amount) {
            accountBalance += amount;
        },
        withdraw: function(amount) {
            // ... logique de sécurité
            accountBalance -= amount;
        }
    };
}
```

Qu'est-ce qui m'empêche de gonfler mon solde ou de ruiner celui de quelqu'un d'autre ?

```js
// plus tard dans le script...

accountBalance = 'Whatever I want, muhahaha >:)';
```

![who-reset-my-balance-this-time](https://www.freecodecamp.org/news/content/images/2019/08/who-reset-my-balance-this-time.jpeg)

Des langages comme Java et C++ permettent aux classes d'avoir des champs privés. Ces champs ne peuvent pas être accessibles en dehors de la classe, permettant une confidentialité parfaite.

JavaScript ne supporte pas les variables privées ([encore](https://github.com/tc39/proposal-class-fields)), mais nous pouvons utiliser des closures !


### Une banque avec une confidentialité appropriée
Cette fois, `accountBalance` se trouve _à l'intérieur_ de notre gestionnaire.

```js
const manageBankAccount = function(initialBalance) {
    let accountBalance = initialBalance;
    
    return {
        getBalance: function() { return accountBalance; },
        deposit: function(amount) { accountBalance += amount; },
        withdraw: function(amount) {
            if (amount > accountBalance) {
                return 'You cannot draw that much!';
            }

            accountBalance -= amount;
        }
    };
}
```

Et peut-être l'utiliser comme ceci...

```js
const accountManager = manageBankAccount(0);

accountManager.deposit(1000);
accountManager.withdraw(500);
accountManager.getBalance(); // 500
```

Remarquez que je ne peux plus accéder directement à `accountBalance`. Je ne peux le voir qu'à travers `getBalance`, et le changer via `deposit` et `withdraw`.

Comment cela est-il possible ? Grâce aux closures !

Même si `manageBankAccount` a créé la variable `accountBalance`, les trois fonctions qu'elle retourne ont toutes accès à `accountBalance` via la closure.

![i-wish-my-bank-did-that](https://www.freecodecamp.org/news/content/images/2019/08/i-wish-my-bank-did-that.jpeg)

## 2. Currying
[J'ai déjà écrit sur le currying](https://www.yazeedb.com/posts/deeply-understand-currying-in-7-minutes). C'est lorsque une fonction prend ses arguments un à la fois.

Au lieu de ceci...

```js
const add = function(x, y) {
    return x + y;
}

add(2, 4); // 6
```

Vous pouvez _curry_ `add` en utilisant les closures...

```js
const add = function(x) {
    return function(y) {
        return x + y;
    }
}
```

Et vous savez que la fonction retournée a accès à `x` et `y`, donc vous pourriez faire quelque chose comme ceci...


```js
const add10 = add(10);

add10(10); // 20
add10(20); // 30
add10(30); // 40
```

Le currying est génial si vous souhaitez "pré-charger" les arguments d'une fonction pour une réutilisation plus facile. Encore une fois, cela n'est possible qu'avec les closures JavaScript !

## 3. Les développeurs React utilisent les closures
Si vous avez suivi les actualités de React, vous avez entendu qu'ils ont publié [hooks](https://reactjs.org/docs/hooks-intro.html) l'année dernière. Le hook le plus déroutant, `useEffect`, repose sur les closures.

Cet article ne contiendra pas un tutoriel complet sur React, donc j'espère que l'exemple est assez simple pour tous.

<iframe src="https://codesandbox.io/embed/react-hooks-closures-example-2kixb?fontsize=14" title="react-hooks-closures-example" allow="geolocation; microphone; camera; midi; vr; accelerometer; gyroscope; payment; ambient-light-sensor; encrypted-media" style="width:100%; height:500px; border:0; border-radius: 4px; overflow:hidden;" sandbox="allow-modals allow-forms allow-popups allow-scripts allow-same-origin"></iframe>

### Voici la partie importante...

```js
function App() {
  const username = 'yazeedb';

  React.useEffect(function() {
    fetch(`https://api.github.com/users/${username}`)
      .then(res => res.json())
      .then(user => console.log(user));
  });
  
  // blah blah blah
}
```

Changez `username` dans le code, remarquez qu'il récupérera ce nom d'utilisateur et enregistrera la sortie dans la console.

C'est encore des closures. `username` est défini à l'intérieur de la fonction _externe_, mais la fonction _interne_ de `useEffect` l'utilise réellement.

## Résumé

1. Les fonctions sont aussi des valeurs.
2. Les fonctions peuvent retourner d'autres fonctions.
3. Les variables d'une fonction externe sont toujours accessibles à sa fonction interne, _même après que la fonction externe a disparu_.
4. Ces variables sont aussi connues sous le nom d'_état_.
5. Par conséquent, les closures peuvent aussi être appelées des fonctions _stateful_.

## Vous voulez un coaching gratuit ?
Si vous souhaitez planifier un appel **gratuit** de 15 à 30 minutes pour discuter de questions de développement Front-End concernant le code, les entretiens, la carrière ou autre chose, [suivez-moi sur Twitter et envoyez-moi un DM](https://twitter.com/yazeedBee).

Après cela, si vous appréciez notre première rencontre, nous pouvons discuter d'une relation de coaching continue qui vous aidera à atteindre vos objectifs de développement Front-End !

## Merci d'avoir lu
Pour plus de contenu comme celui-ci, consultez <a href="https://yazeedb.com">https://yazeedb.com!</a>

À la prochaine !