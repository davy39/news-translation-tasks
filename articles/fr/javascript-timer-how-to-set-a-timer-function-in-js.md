---
title: Minuteur JavaScript – Comment définir une fonction de minuterie en JS
subtitle: ''
author: Tantoluwa Heritage Alabi NB
co_authors: []
series: null
date: '2024-09-16T18:59:45.207Z'
originalURL: https://freecodecamp.org/news/javascript-timer-how-to-set-a-timer-function-in-js
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1726513174015/54470912-08b3-4a23-9a0c-9b6f9b57617b.jpeg
tags:
- name: JavaScript
  slug: javascript
seo_title: Minuteur JavaScript – Comment définir une fonction de minuterie en JS
seo_desc: In Javascript, the timer function prevents your code from running everything
  at once when an event triggers or the page loads. This gives you more control over
  the timing of your program's actions and can enhance the user experience by creating
  smoot...
---

En JavaScript, la fonction de minuterie empêche votre code d'exécuter tout en même temps lorsqu'un événement se déclenche ou que la page se charge. Cela vous donne plus de contrôle sur le timing des actions de votre programme et peut améliorer l'expérience utilisateur en créant des interactions ou des animations plus fluides. 

Dans ce tutoriel, vous apprendrez à utiliser les fonctions de minuterie.

## **Comment définir une fonction de minuterie**

Il existe différentes façons de définir une fonction de minuterie, telles que les fonctions `setTimeout`, `setInterval`, `clearTimeout` et `setImmediate`. Vous découvrirez chacune d'entre elles dans cet article.

### **Comment utiliser** `setTimeout` **et** `setInterval`

La fonction `setTimeout` exécute une expression après un délai spécifié en millisecondes, tandis que la fonction `setInterval` exécute une expression après un intervalle spécifié en millisecondes.

Vous pouvez utiliser la fonction `setTimeout()` lorsque vous souhaitez exécuter un bloc de code avec un délai spécifique, mais une seule fois.

La fonction setTimeout est désignée par `setTimeout()`. Voici un exemple de la façon dont vous pouvez l'utiliser :

```javascript
// Exécuter une fonction après 3 secondes
const timeoutId = setTimeout(() => {
    console.log('Timeout exécuté après 3 secondes');
}, 3000);
```

Le bloc de code ci-dessus montre comment utiliser la syntaxe `setTimeout` pour exécuter une fonction après 3 secondes. Le nom de la variable est `timeoutId`, laquelle stocke l'exécution du setTimeout. Le temps défini est de 3000 millisecondes (soit 3 secondes).

Vous pouvez utiliser la fonction `setInterval()` lorsque vous souhaitez exécuter un bloc de code de manière répétée à des intervalles spécifiques – par exemple, lors de l'animation d'éléments.

La fonction setInterval est désignée par `setInterval()`. Voici comment vous pouvez l'utiliser :

```javascript
// Exécuter une fonction toutes les 1 seconde
const intervalId = setInterval(() => {
    console.log('Intervalle exécuté toutes les 1 seconde');
}, 1000);
```

Le bloc de code ci-dessus montre comment utiliser la syntaxe `setInterval` pour exécuter une fonction après 1 seconde. Le nom de la variable est `intervalId`, laquelle stocke l'exécution du setInterval. Le temps est réglé sur 1000 millisecondes (1 seconde).

### **Comment utiliser** `clearTimeout` **et** `clearInterval`

La fonction `clearTimeout` annule un timeout précédemment programmé avec la fonction `setTimeout`. `clearInterval` annule un intervalle précédemment défini avec `setInterval`.

La fonction clearTimeout est désignée par `clearTimeout();`. Elle accepte un argument qui stocke la fonction `setTimeout`.

Voici un exemple de son fonctionnement :

```javascript
const timeoutId = setTimeout(() => {
    console.log('Timeout exécuté après 3 secondes');
}, 3000);

clearTimeout(timeoutId);
console.log('Timeout annulé');
```

La fonction `clearTimeout` prend le nom de la variable `timeoutID` qui stocke la fonction `setTimeout` et annule la fonction.

La fonction `clearInterval` est désignée par `clearInterval();`. Elle accepte un argument qui stocke la fonction `setInterval` sous le bloc de la fonction `setTimeout`.

Voici un exemple de son fonctionnement :

```javascript
const intervalId = setInterval(() => {
    console.log('Intervalle exécuté toutes les 1 seconde');
}, 1000);

setTimeout(() => {
    clearInterval(intervalId);
    console.log('Intervalle annulé. La fonction ne s\'exécutera plus.');
}, 5000);
```

Dans le bloc de code ci-dessus, la fonction `setTimeout` est introduite. La fonction `clearInterval` est passée dans le bloc de code, l'argument `intervalId` est transmis, puis la fonction est exécutée.

Une autre fonction de minuterie est `setImmediate`, qui exécute une fonction de manière asynchrone dès que possible après la fin de l'exécution du bloc de code actuel. Cependant, elle n'est pas universellement prise en charge par tous les navigateurs, elle est donc rarement utilisée.

## Conclusion

Il est important de savoir comment utiliser les fonctions de minuterie JavaScript et quand les appliquer à votre code. Et rappelez-vous que la minuterie est réglée en millisecondes, donc quel que soit le nombre que vous utilisez, divisez-le par 1000 pour déterminer à combien de secondes cela correspond.

Si vous avez des questions, vous pouvez me contacter sur [Twitter](https://twitter.com/HeritageAlabi1) 💙.