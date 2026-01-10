---
title: Comment créer un compte à rebours
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-21T21:59:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-countdown-timer
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e90740569d1a4ca3dc5.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment créer un compte à rebours
seo_desc: 'Building a simple countdown timer is easy with JavaScript''s native timing
  events. You can read more about those in this article.

  Building the countdown timer

  Start by declaring an empty function called startCountdown that takes seconds as
  an argument...'
---

Créer un simple compte à rebours est facile avec les événements de temporisation natifs de JavaScript. Vous pouvez en apprendre plus à ce sujet dans [cet article](https://www.freecodecamp.org/news/p/50cdf5da-8359-4bd2-8718-d5bd7c0de03d/www.freecodecamp.org/news/javascript-timing-events-settimeout-and-setinterval/).

### Construction du compte à rebours

Commencez par déclarer une fonction vide appelée `startCountdown` qui prend `seconds` comme argument :

```javascript
function startCountdown(seconds) {
    
};
```

Nous voulons suivre les secondes qui passent une fois le compte à rebours démarré, donc utilisez `let` pour déclarer une variable appelée `counter` et définissez-la égale à `seconds` :

```js
function startCountdown(seconds) {
  let counter = seconds;
}
```

Rappelez-vous qu'il est considéré comme une bonne pratique de sauvegarder votre fonction d'événement de temporisation dans une variable. Cela rend beaucoup plus facile l'arrêt du compte à rebours plus tard. Créez une variable appelée `interval` et définissez-la égale à `setInterval()` :

```js
function startCountdown(seconds) {
  let counter = seconds;
    
  const interval = setInterval();
}
```

Vous pouvez passer une fonction directement à `setInterval`, donc passons-lui une fonction fléchée vide comme premier argument. De plus, nous voulons que la fonction s'exécute chaque seconde, donc passez 1000 comme deuxième argument :

```js
function startCountdown(seconds) {
  let counter = seconds;
    
  const interval = setInterval(() => {
    
  }, 1000);
}
```

Maintenant, la fonction que nous avons passée à `setInterval` s'exécutera chaque seconde. Chaque fois qu'elle s'exécute, nous voulons enregistrer la valeur actuelle de `counter` dans la console avant de la décrémenter :

```js
function startCountdown(seconds) {
  let counter = seconds;
    
  const interval = setInterval(() => {
    console.log(counter);
    counter--;
  }, 1000);
}
```

Maintenant, si vous exécutez la fonction, vous verrez qu'elle fonctionne, mais ne s'arrête pas une fois que `counter` est inférieur à 0 :

```js
startCountdown(5);

// Sortie de la console // 
// 5
// 4
// 3
// 2
// 1
// 0 
// -1
// -2 
```

Pour corriger cela, écrivez d'abord une instruction `if` qui s'exécute lorsque `counter` est inférieur à 0 :

```js
function startCountdown(seconds) {
  let counter = seconds;
    
  const interval = setInterval(() => {
    console.log(counter);
    counter--;
      
    if (counter < 0 ) {
      
    }
  }, 1000);
}
```

Ensuite, à l'intérieur de l'instruction `if`, effacez l'`interval` avec `clearInterval` et enregistrez une chaîne de son d'alarme dans la console :

```js
function startCountdown(seconds) {
  let counter = seconds;
    
  const interval = setInterval(() => {
    console.log(counter);
    counter--;
      
    if (counter < 0 ) {
      clearInterval(interval);
      console.log('Ding!');
    }
  }, 1000);
}
```

### **Exécution**

Maintenant, lorsque vous démarrez le compte à rebours, vous devriez voir ce qui suit :

```javascript
startCountdown(5);

// Sortie de la console // 
// 5
// 4
// 3
// 2
// 1
// 0 
// Ding!
```

### **Plus de ressources**

[Événements de temporisation JavaScript : setTimeout et setInterval](https://www.freecodecamp.org/news/p/50cdf5da-8359-4bd2-8718-d5bd7c0de03d/www.freecodecamp.org/news/javascript-timing-events-settimeout-and-setinterval/)