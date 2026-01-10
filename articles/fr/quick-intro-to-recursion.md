---
title: Une introduction rapide à la récursivité en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-03T07:00:00.000Z'
originalURL: https://freecodecamp.org/news/quick-intro-to-recursion
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/cover-image.jpeg
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Recursion
  slug: recursion
- name: technology
  slug: technology
seo_title: Une introduction rapide à la récursivité en JavaScript
seo_desc: 'By Yazeed Bzadough

  The function calls itself until someone stops it.

  Recursion can feel difficult to new developers. Perhaps that''s because many resources
  teach it using algorithmic examples (Fibonacci, linked-lists). This piece will hopefully
  introd...'
---

Par Yazeed Bzadough

La fonction s'appelle elle-même jusqu'à ce que quelqu'un l'arrête.

La récursivité peut sembler difficile pour les nouveaux développeurs. Peut-être est-ce parce que de nombreuses ressources l'enseignent en utilisant des exemples algorithmiques (Fibonacci, listes chaînées). Cet article espère introduire les choses simplement, en utilisant un exemple simple.

## Idée principale
La **récursivité**, c'est lorsqu'une fonction s'appelle elle-même jusqu'à ce que quelqu'un l'arrête. Si personne ne l'arrête, elle va **récurser** (s'appeler elle-même) indéfiniment.

![no-this-is-patrick](https://www.freecodecamp.org/news/content/images/2019/09/no-this-is-patrick.jpeg)

Les fonctions récursives vous permettent d'effectuer une unité de travail plusieurs fois. C'est exactement ce que les boucles `for/while` nous permettent d'accomplir ! Parfois, cependant, les solutions récursives sont une approche plus élégante pour résoudre un problème.

## Fonction de compte à rebours
Créons une fonction qui compte à rebours à partir d'un nombre donné. Nous allons l'utiliser comme ceci.

```js
countDownFrom(5);
// 5
// 4
// 3
// 2
// 1
```

Et voici notre algorithme pour résoudre ce problème.

1. Prendre un paramètre appelé `number`. C'est notre point de départ.
2. Aller de `number` à `0`, en enregistrant chaque nombre en cours de route.

Nous allons commencer par une approche avec une boucle `for` puis la comparer à une approche récursive.

### Approche impérative (boucles)
```js
function countDownFrom(number) {
	for (let i = number; i > 0; i--) {
		console.log(i);
	}	
}

countDownFrom(5);
// 5
// 4
// 3
// 2
// 1
```

Cette version contient les deux étapes algorithmiques.

1. ✅ Prendre un paramètre appelé `number`.
2. ✅ Enregistrer tout de `number` à `0`.

### Approche récursive
```js
function countDownFrom(number) {
	if (number === 0) {
		return;
	}

    console.log(number);    
    countDownFrom(number - 1);
}

countDownFrom(5);
// 5
// 4
// 3
// 2
// 1
```

Cette version fonctionne également.

1. ✅ Prendre un paramètre appelé `number`.
2. ✅ Enregistrer tout de `number` à `0`.

Ainsi, conceptuellement, les deux approches sont les mêmes. Cependant, elles accomplissent la tâche de différentes manières.

### Débogage de notre solution impérative
Pour un exemple plus visuel, plaçons un `debugger` dans notre version de boucle et lançons-la dans les outils de développement Chrome.

```js
function countDownFrom(number) {
	for (let i = number; i > 0; i--) {
		console.log(i);
		debugger;
	}	
}
```

![countdownFrom-iterative](https://www.freecodecamp.org/news/content/images/2019/09/countdownFrom-iterative.gif)

Voyez comment elle utilise une variable supplémentaire, `i`, pour suivre le nombre actuel ? À chaque itération, `i` diminue, finissant par atteindre `0` et se terminer.

Et dans la boucle `for`, nous avons spécifié "arrêter si `i > 0`".

### Débogage de notre solution récursive
```js
function countDownFrom(number) {
	if (number === 0) {
		return;
	}

    console.log(number);
	
	debugger;

    countDownFrom(number - 1);
}
```

![countdownFrom-recursive](https://www.freecodecamp.org/news/content/images/2019/09/countdownFrom-recursive.gif)

La version récursive n'a pas besoin de variables supplémentaires pour suivre sa progression. Remarquez comment la pile de fonctions (_call stack_) grandit à mesure que nous récursons ?

C'est parce que chaque appel à `countDownFrom` ajoute à la pile, lui passant `number - 1`. En faisant cela, nous passons un `number` mis à jour à chaque fois. Pas besoin d'état supplémentaire !

C'est la principale différence entre les deux approches.

1. L'approche itérative utilise un état interne (variables supplémentaires pour compter, etc).
2. L'approche récursive ne le fait pas, elle passe simplement des paramètres mis à jour entre chaque appel.

Mais comment chaque version sait-elle quand s'arrêter ?

## Boucles infinies
Au cours de vos aventures, vous avez peut-être été averti des redoutables boucles infinies.

```js
⚠️ CECI S'EXÉCUTE INDÉFINIMENT, ATTENTION ⚠️
while (true) { console.log('POURQUOI AVEZ-VOUS EXÉCUTÉ CECI ?!') }

⚠️ CECI S'EXÉCUTE INDÉFINIMENT, ATTENTION ⚠️
for (i = 0;;) { console.log('POURQUOI AVEZ-VOUS EXÉCUTÉ CECI ?!') }
```

Puisqu'elles s'exécuteraient théoriquement indéfiniment, une boucle infinie arrêtera votre programme et pourrait faire planter votre navigateur. Vous pouvez les éviter en codant toujours une _condition d'arrêt_.

```js
✅ Ceci ne s'exécute pas indéfiniment
x = 0;
while (x < 3) { console.log(x); x++; }

✅ Ceci ne s'exécute pas indéfiniment
for (x = 0; x < 3; x++) { console.log(x); }
```

Dans les deux cas, nous enregistrons `x`, l'incrémentons et nous arrêtons lorsqu'il devient `3`. Notre fonction `countDownFrom` avait une logique similaire.

```js
// Arrêter à 0
for (let i = number; i > 0; i--)
```

Encore une fois, les boucles ont besoin d'un état supplémentaire pour déterminer quand elles doivent s'arrêter. C'est à quoi servent `x` et `i`.

## Récursivité infinie
La récursivité présente également le même danger. Il n'est pas difficile d'écrire une fonction auto-référencée qui fera planter votre navigateur.

```js
⚠️ CECI S'EXÉCUTE INDÉFINIMENT, ATTENTION ⚠️
function run() {
    console.log('running');
    run();
}

run();
// running
// running
// ...
```

![is-this-a-recursive](https://www.freecodecamp.org/news/content/images/2019/09/is-this-a-recursive.jpg)

Sans condition d'arrêt, `run` s'appellera elle-même indéfiniment. Vous pouvez corriger cela avec une instruction `if`.

```js
✅ Ceci ne s'exécute pas indéfiniment

function run(x) {
    if (x === 3) return;
    
    console.log('running');
    run(x + 1);
}

run(0);
// running
// running
// running

// x est 3 maintenant, nous avons terminé.
```

### Cas de base
Ceci est connu sous le nom de **cas de base** – notre fonction récursive `countDownFrom` en avait un.

```js
if (number === 0) {
    return;
}
```

C'est la même idée que la logique d'arrêt de notre boucle. Quelle que soit l'approche que vous choisissez, n'oubliez pas qu'à un moment donné **elle doit être arrêtée**.

![is-this-you-need-to-be-stopped](https://www.freecodecamp.org/news/content/images/2019/09/is-this-you-need-to-be-stopped-2.png)

## Résumé
* La récursivité, c'est lorsqu'une fonction s'appelle elle-même jusqu'à ce que quelqu'un l'arrête.
* Elle peut être utilisée à la place d'une boucle.
* Si personne ne l'arrête, elle récursera indéfiniment et fera planter votre programme.
* Un **cas de base** est une condition qui arrête la récursivité. N'oubliez pas de les ajouter !
* Les boucles utilisent des variables d'état supplémentaires pour le suivi et le comptage, tandis que la récursivité n'utilise que les paramètres fournis.

![disappearing-loops](https://www.freecodecamp.org/news/content/images/2019/08/disappearing-loops.jpg)

## Merci d'avoir lu
Pour plus de contenu comme celui-ci, consultez <a href="https://yazeedb.com">https://yazeedb.com</a>. Et faites-moi savoir ce que vous aimeriez voir d'autre ! [Mes DM sont ouverts sur Twitter.](https://twitter.com/yazeedBee)

À la prochaine !