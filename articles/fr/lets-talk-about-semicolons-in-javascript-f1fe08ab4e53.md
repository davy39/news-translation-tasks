---
title: Parlons des points-virgules en JavaScript
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2018-07-23T15:55:08.000Z'
originalURL: https://freecodecamp.org/news/lets-talk-about-semicolons-in-javascript-f1fe08ab4e53
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xAFAiAxqZVrOVLBTo9tf6w.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Parlons des points-virgules en JavaScript
seo_desc: 'To use them, or not to use them…

  Semicolons in JavaScript divide the community. Some prefer to use them always, no
  matter what. Others like to avoid them.

  I put out a poll on Twitter to test the waters, and I found lots of semicolon supporters:

  After...'
---

#### Les utiliser, ou ne pas les utiliser...

Les points-virgules en JavaScript divisent la communauté. Certains préfèrent les utiliser toujours, quoi qu'il arrive. D'autres aiment les éviter.

J'ai lancé un sondage sur Twitter pour tester les eaux, et j'ai trouvé beaucoup de partisans des points-virgules :

Après avoir utilisé des points-virgules pendant des années, à l'automne 2017, j'ai décidé d'essayer de les éviter lorsque c'était possible. J'ai configuré [Prettier](https://flaviocopes.com/prettier/) pour supprimer automatiquement les points-virgules de mon code, sauf s'il y avait une structure de code particulière qui les nécessitait.

Maintenant, je trouve naturel d'éviter les points-virgules, et je pense que le code est plus beau et plus propre à lire.

Tout cela est possible parce que JavaScript ne nécessite pas strictement les points-virgules. Lorsqu'il y a un endroit où un point-virgule est nécessaire, il l'ajoute en coulisses.

Cela s'appelle **l'insertion automatique de points-virgules**.

Il est important de connaître les règles qui régissent les points-virgules. Cela vous permettra d'éviter d'écrire du code qui générera des bugs avant de ne pas se comporter comme vous l'attendez.

### Les règles de l'insertion automatique de points-virgules en JavaScript

L'analyseur JavaScript ajoutera automatiquement un point-virgule lorsque, lors de l'analyse du code source, il trouvera ces situations particulières :

1. lorsque la ligne suivante commence par du code qui rompt la ligne actuelle (le code peut s'étendre sur plusieurs lignes)
2. lorsque la ligne suivante commence par un `}`, fermant le bloc actuel
3. lorsque la fin du fichier source est atteinte
4. lorsqu'il y a une instruction `return` sur sa propre ligne
5. lorsqu'il y a une instruction `break` sur sa propre ligne
6. lorsqu'il y a une instruction `throw` sur sa propre ligne
7. lorsqu'il y a une instruction `continue` sur sa propre ligne

### Exemples de code qui ne font pas ce que vous pensez

Sur la base de ces règles, voici quelques exemples.

Prenez ceci :

```js
const hey = 'hey'
const you = 'hey'
const heyYou = hey + ' ' + you

['h', 'e', 'y'].forEach((letter) => console.log(letter))
```

Vous obtiendrez l'erreur `Uncaught TypeError: Cannot read property 'forEach' of undefined` parce que, selon la règle `1`, JavaScript essaie d'interpréter le code comme

```js
const hey = 'hey';
const you = 'hey';
const heyYou = hey + ' ' + you['h', 'e', 'y'].forEach((letter) => console.log(letter))
```

Ce morceau de code :

```js
(1 + 2).toString()
```

affiche `"3"`.

```js
const a = 1
const b = 2
const c = a + b
(a + b).toString()
```

Au lieu de cela, il lève une exception `TypeError: b is not a function`, parce que JavaScript essaie de l'interpréter comme

```js
const a = 1
const b = 2
const c = a + b(a + b).toString()
```

Un autre exemple basé sur la règle 4 :

```js
(() => {
  return
  {
    color: 'white'
  }
})()
```

Vous vous attendriez à ce que la valeur de retour de cette fonction immédiatement invoquée soit un objet contenant la propriété `color`, mais ce n'est pas le cas. Au lieu de cela, c'est `undefined`, parce que JavaScript insère un point-virgule après `return`.

Au lieu de cela, vous devriez mettre l'accolade ouvrante juste après `return` :

```js
(() => {
  return {
    color: 'white'
  }
})()
```

Vous penseriez que ce code montre '0' dans une alerte :

```js
1 + 1
-1 + 1 === 0 ? alert(0) : alert(2)
```

mais il montre 2 à la place, parce que JavaScript (selon la règle 1) l'interprète comme :

```js
1 + 1 -1 + 1 === 0 ? alert(0) : alert(2)
```

### Conclusion

Soyez prudent — certaines personnes ont des opinions très tranchées sur les points-virgules. Honnêtement, je m'en fiche. L'outil nous donne la possibilité de ne pas les utiliser, donc nous pouvons éviter les points-virgules si nous le voulons.

Je ne suggère rien d'un côté ou de l'autre. Faites simplement votre propre choix en fonction de ce qui fonctionne pour vous.

Quoi qu'il en soit, nous devons simplement faire un peu attention, même si la plupart du temps ces scénarios de base n'apparaissent jamais dans votre code.

Choisissez quelques règles :

* Soyez prudent avec les instructions `return`. Si vous retournez quelque chose, ajoutez-le sur la même ligne que le return (même chose pour `break`, `throw`, `continue`)
* Ne commencez jamais une ligne par des parenthèses, car celles-ci pourraient être concaténées avec la ligne précédente pour former un appel de fonction, ou une référence d'élément de tableau

Et finalement, testez toujours votre code pour vous assurer qu'il fait ce que vous voulez.

> Je publie 1 tutoriel de programmation gratuit par jour sur [flaviocopes.com](https://flaviocopes.com), allez y faire un tour !

*Initialement publié sur [flaviocopes.com](https://flaviocopes.com/javascript-automatic-semicolon-insertion/).