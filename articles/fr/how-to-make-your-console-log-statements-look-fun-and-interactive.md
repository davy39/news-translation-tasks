---
title: Comment rendre votre sortie console amusante et interactive en JavaScript et
  Node.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-02T21:11:25.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-your-console-log-statements-look-fun-and-interactive
coverImage: https://cdn-media-2.freecodecamp.org/w1280/60190c1a0a2838549dcbcd11.jpg
tags:
- name: console
  slug: console
- name: JavaScript
  slug: javascript
- name: node js
  slug: node-js
seo_title: Comment rendre votre sortie console amusante et interactive en JavaScript
  et Node.js
seo_desc: 'By Vasyl Lagutin

  In this tutorial, you''ll learn how to add a randomized delay to the console.log
  statements in JavaScript and Node.js.


  Why would you want to do this?

  First of all, programming should be fun. And making a boring thing like console.log...'
---

Par Vasyl Lagutin

Dans ce tutoriel, vous apprendrez à ajouter un délai aléatoire aux instructions `console.log` en JavaScript et Node.js.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/ezgif.com-gif-maker.gif)

## Pourquoi voudriez-vous faire cela ?

Tout d'abord, la programmation doit être amusante. Et rendre une chose ennuyeuse comme `console.log` plus agréable est très satisfaisant.

Si vous voulez un accès rapide au code source, vous pouvez consulter ce [dépôt GitHub](https://github.com/AgileNix/funkylog/).

## Étape 1 : Créer une fonction qui prend une chaîne et la passe à console.log

Pour nous assurer que chaque étape est claire, nous allons commencer modestement et créer une fonction qui accepte une chaîne comme paramètre et la journalise dans la console.

```javascript
const log = (s) => {
  console.log(s);
}
```

## Étape 2 : Journaliser les caractères de la chaîne un par un

Avant de pouvoir ajouter un délai entre la sortie des caractères individuels, nous devons nous assurer qu'ils sont effectivement séparés.

Ajoutons une boucle `for` qui itère sur chaque lettre de la chaîne et l'imprime dans la console.

```javascript
const log = (s) => {
  for (const c of s) {
    console.log(c);
  }
}
```

## Étape 3 : Comment corriger le problème de nouvelle ligne

Maintenant, chaque lettre est imprimée sur une nouvelle ligne car chaque appel à `console.log` ajoute une ligne vide.

Nous allons remplacer `console.log` par `_**process**_.stdout.write` qui fait essentiellement la même chose, mais n'ajoute pas de nouvelle ligne après la sortie.

Cependant, nous avons maintenant perdu la nouvelle ligne à la toute fin de la sortie, ce qui est toujours souhaitable. Nous allons l'ajouter en imprimant explicitement le caractère `\n`.

```javascript
const log = (s) => {
  for (const c of s) {
    process.stdout.write(c);
  }
  process.stdout.write('\n');
}
```

## Étape 4 : Implémenter la fonction `sleep`

En JavaScript, nous ne pouvons pas simplement arrêter l'exécution du code synchrone pendant un certain temps. Pour que cela se produise, nous devons écrire notre propre fonction. Appelons-la sleep.

Elle doit accepter un seul paramètre `ms` et retourner une Promesse qui se résout après un délai de `ms` millisecondes.

```javascript
const sleep = (ms) => {
  return new Promise(resolve => setTimeout(resolve, ms));
};
```

## Étape 5 : Ajouter le délai

Nous sommes donc prêts à ajouter un délai à notre sortie ! Nous avons besoin de quelques éléments ici :

* ajouter un paramètre `delay` à la fonction `log`
* rendre la fonction `log` asynchrone en ajoutant le mot-clé `async`
* appeler une fonction `sleep` qui retardera la prochaine itération de la boucle de `delay` millisecondes

```javascript
const sleep = (ms) => {
  return new Promise(resolve => setTimeout(resolve, ms));
};

const log = async (s, delay) => {
  for (const c of s) {
    process.stdout.write(c);
    await sleep(delay);
  }
  process.stdout.write('\n');
}
```

## Étape 6 : Implémenter un délai aléatoire

La sortie sera encore plus belle si nous randomisons le timing.

Ajoutons un autre paramètre booléen `randomized` à la fonction `log`. Si c'est vrai, alors l'argument passé à `sleep` doit être dans la plage de `0` à `delay` millisecondes.

```javascript
const sleep = (ms) => {
  return new Promise(resolve => setTimeout(resolve, ms));
};

const log = async (s, delay, randomized) => {
  for (const c of s) {
    process.stdout.write(c);
    await sleep((randomized ? Math.random() : 1) * delay);
  }
  process.stdout.write('\n');
}
```

J'ai utilisé un opérateur ternaire, mais vous pouvez le remplacer par une instruction `if` régulière :

```javascript
if (randomized) {
  sleep(Math.random * delay);
} else {
  sleep(delay);
}
```

## Étape 7 : Rendre le log configurable

Pour l'instant, nous avons implémenté presque tout ce que nous voulions. Mais l'appeler n'est pas très propre car nous devons passer le `delay` et le drapeau de randomisation chaque fois que nous voulons imprimer quelque chose dans la console.

```javascript
log('Bonjour, le monde !', 100, true);
log("Qu'est-ce qu'il y a ?", 100, true);
log('Comment allez-vous ?', 100, true);
```

Ce serait bien si nous pouvions avoir un log configurable qui pourrait être appelé avec un seul paramètre - une chaîne que nous voulons sortir.

Pour ce faire, nous devons réécrire notre code. Voici le plan :

* envelopper toute la fonctionnalité actuelle dans une seule fonction `funkylog` qui accepte un objet avec 2 champs, `delay` et `randomized`
* `funkylog` doit retourner la fonction fléchée anonyme. Son implémentation doit être la même que `log`, que nous avons implémentée dans les étapes 1 à 6
* les paramètres `delay` et `randomized` doivent être supprimés de la fonction `log` car ils seront maintenant transmis par `funkylog`

```javascript
const funkylog = ({ delay, randomized }) => {
  const sleep = (ms) => {
    return new Promise(resolve => setTimeout(resolve, ms));
  };
    
  return async (s) => {
    for (const c of s) {
      process.stdout.write(c);
      await sleep((randomized ? Math.random() : 1) * delay);
    }
    process.stdout.write('\n');
  }
};
```

## Étape 8 : Ajouter la touche finale

Voyons ce que nous avons obtenu :

```javascript
const log = funkylog({ delay: 100, randomized: true });

log('Bonjour, le monde !');
log("Qu'est-ce qu'il y a ?");
log('Comment allez-vous ?');
```

* Nous pouvons créer un logger configurable en utilisant la fonction `funkylog`
* Nous pouvons sélectionner n'importe quel délai que nous voulons
* L'utilisation du logger ne nous oblige pas à passer le `delay` chaque fois que nous l'appelons

Une autre amélioration que nous pouvons apporter est de fournir une valeur par défaut pour le paramètre `delay`.

```javascript
const funkylog = ({ delay = 100, randomized }) => {
    ..
    ..
```

Ainsi, maintenant nous pouvons créer le `funkylog` sans aucun argument et il fonctionnera toujours !

```javascript
const log = funkylog();

console.log('Bonjour, le monde !');
```

## Idées d'amélioration

Comme je l'ai dit dès le début, avant tout, la programmation doit être amusante. Sinon, cela deviendra une routine et vous n'aimerez plus le faire.

Apportez des améliorations supplémentaires à `funkylog` et faites-moi savoir à quoi ressemblent vos résultats ! Par exemple, vous pouvez pimenter la sortie en la colorisant. Vous pouvez utiliser le module `npm` `chalk` pour cela.

Ensuite, une fois que vous avez implémenté différentes couleurs, vous pouvez ajouter un autre drapeau qui ajouterait un délai supplémentaire entre les mots de la chaîne.

Merci d'être resté avec moi tout au long de ce tutoriel !  
J'écris un blog de programmation sur [learn.coderslang.com](https://learn.coderslang.com) et je construis un [cours Full Stack JS](https://js.coderslang.com).

### Si vous avez des commentaires ou des questions sur ce tutoriel, n'hésitez pas à me tweeter **@coderslang** ou à rejoindre la discussion sur Telegram **@coderslang_chat**