---
title: Comment fonctionne réellement String.padStart ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-31T20:40:59.000Z'
originalURL: https://freecodecamp.org/news/how-does-string-padstart-actually-work-abba34d982e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*jANUTARhf9DaSPo_FdobsQ.gif
tags:
- name: binary
  slug: binary
- name: bitwise
  slug: bitwise
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment fonctionne réellement String.padStart ?
seo_desc: 'By Yazeed Bzadough

  Previously, I shared my usage of padStart to elegantly replace what would’ve been
  loads of if statements. This magical method threw me off my rocker. I simply couldn’t
  believe it existed.

  What it does

  Mozilla Developer Network (MDN...'
---

Par Yazeed Bzadough

[Précédemment](https://medium.com/@yazeedb/youtube-durations-in-4-lines-of-javascript-e9a92cea67a4), j'ai partagé mon utilisation de `padStart` pour remplacer élégamment ce qui aurait été des tonnes de déclarations `if`. Cette méthode magique m'a laissé sans voix. Je ne pouvais tout simplement pas croire qu'elle existait.

### Ce qu'elle fait

[Documentation Mozilla Developer Network (MDN)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/padStart):

> La méthode `padStart()` complète la chaîne actuelle avec une autre chaîne (répétée, si nécessaire) de sorte que la chaîne résultante atteigne la longueur donnée. Le remplissage est appliqué à partir du début (à gauche) de la chaîne actuelle.

Continuer à **préfixer une chaîne** à **une autre chaîne** jusqu'à ce que la **longueur cible** soit atteinte.

![](https://cdn-media-1.freecodecamp.org/images/1*XgjBHs6faLKurpx6WOxmaQ.png)![](https://cdn-media-1.freecodecamp.org/images/1*kvWWV9-Le3akATlMGLFIUA.png)

Si la longueur est déjà inférieure à la longueur de la chaîne originale, rien ne se passe.

![](https://cdn-media-1.freecodecamp.org/images/1*tmVv1tdy9Ye099ca2YBD4w.png)

Et puisque `padStart` retourne une chaîne, nous pouvons enchaîner ses méthodes.

![](https://cdn-media-1.freecodecamp.org/images/1*LhQzpSiSSlvTDkcHyL8HtA.png)

Vous voyez ? 1, 2, 3, 4 et 5 sont tous inférieurs ou égaux à la longueur de `world` qui est de 5, donc `padStart` ne fait rien.

### Support des navigateurs

Malheureusement, le support est actuellement "meh"

![](https://cdn-media-1.freecodecamp.org/images/1*OsJkuMt7gxC407zlxv1Imw.png)Support desktop![](https://cdn-media-1.freecodecamp.org/images/1*dtwqtBR1j9vDDi2AkpP61Q.png)Support mobile

Vous pouvez soit utiliser [babel-polyfill](http://babeljs.io/#polyfill) ou [le polyfill de MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/padStart#Polyfill).

Voici le polyfill de MDN.

![](https://cdn-media-1.freecodecamp.org/images/1*Zf4kxLLpi3CsYN94Nl4axQ.png)

### Quelques points d'intérêt :

- **Prototypes** (lignes 1 et 2)
- **Opérateurs bit à bit** (ligne 4)
- `padString.repeat` (ligne 14)
- `padString.slice` (ligne 17)

Je suis prêt à les passer en revue si vous êtes intéressés ?

Les lignes 1 et 2 ne sont pas si mauvaises : "Si `padStart` n'est pas supporté par le navigateur, créons notre propre `padStart` et ajoutons-le" (c'est le polyfill en résumé).

Une manière courante de vérifier le support d'une méthode par le navigateur est d'inspecter le prototype de son objet. Puisque `padStart` est une méthode de chaîne, elle devrait exister sur `String.prototype`.

Ma vieille version de Safari ne supporte pas `padStart`.

![](https://cdn-media-1.freecodecamp.org/images/1*8zmT7mTVUn2Q4MqunHXicg.png)Support de padStart dans mon Safari

Mais mon Chrome et Firefox le supportent.

![](https://cdn-media-1.freecodecamp.org/images/1*paNRJ_6YQ9ThHHxkwEpZwA.png)Support de padStart dans Chrome![](https://cdn-media-1.freecodecamp.org/images/1*jn3Exskqn_8EAQORGs_FKg.png)Support de padStart dans Firefox

Considérez cette vérification de sécurité à la ligne 1

```js
if (!String.prototype.padStart) {
}
```

Cette déclaration `if` ne retournerait `true` que dans mon vieux Safari. Elle retourne `false` dans Chrome/Firefox, donc aucun polyfill n'est appliqué.

![](https://cdn-media-1.freecodecamp.org/images/1*Zf4kxLLpi3CsYN94Nl4axQ.png)

Passons à la ligne 2, qui crée une nouvelle fonction appelée `padStart` et l'assigne à `String.prototype.padStart`. Grâce au modèle d'héritage de JavaScript, toute chaîne créée par la suite peut utiliser `padStart`.

Cette fonction prend deux paramètres

1. `targetLength` : Quelle doit être la longueur de la chaîne résultante ?

2. `padString` : Avec quoi la complétons-nous ?

Ajoutons des déclarations `debugger` à ce code.

![](https://cdn-media-1.freecodecamp.org/images/1*ttFL0luCSlQzdyOh-lpzOA.png)

J'ai également supprimé cette déclaration `if` de la ligne 1, donc même le `String.prototype.padStart` natif sera remplacé par cette fonction—ce qui est utile si vous voulez déboguer dans Chrome.

**_Ne remplacez pas les prototypes en production, les enfants !_**

![](https://cdn-media-1.freecodecamp.org/images/1*srYXzRnU1Qt46J3x91vKjQ.png)

En utilisant notre exemple initial

```js
'world'.padStart(11, 'hello ');
```

![](https://cdn-media-1.freecodecamp.org/images/1*lFrlt-xxEwyByiesDNqHpw.png)

Regardez la ligne 2. Nous voyons que `targetLength` et `padString` ont trouvé leur chemin dans notre fonction. Pas de folie pour l'instant, mais ça arrive. J'ai évité la ligne 5 assez longtemps.

### Opérateurs bit à bit

Le commentaire au-dessus de la ligne 5 décrit brièvement son but : "Si `targetLength` est un nombre, arrondissez-le à l'entier inférieur. Si ce n'est pas un nombre, mettez-le à 0".

**Les opérateurs bit à bit** rendent cela possible.

`targetLength >> 0;`

Cet opérateur `>>` est connu comme un [déplacement binaire à droite avec propagation du signe](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_Operators#Right_shift) (LOLWUT?).
Vous l'utilisez avec deux nombres

`a >> b`

**Ce que cela fait :**

1. `a` est converti en binaire ([détails ici](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_Operators#Signed_32-bit_integers)).
2. Le binaire `a` est déplacé à droite `b` fois.

Notre `targetLength` est 11—ce qui est 1011 en binaire (voici un [convertisseur](https://www.binaryhexconverter.com/binary-to-decimal-converter) si vous ne me croyez pas ?).

Un effet secondaire de la conversion en binaire est que les nombres sont arrondis à l'entier inférieur et que _la plupart_ des non-nombres deviennent 0.

Essayez les exemples suivants

![](https://cdn-media-1.freecodecamp.org/images/1*G9R342JuTLzAhZ3zXB5qYw.png)

Vous voyez ? Les fractions deviennent des nombres entiers. Les non-nombres deviennent 0, avec une exception notable...

![](https://cdn-media-1.freecodecamp.org/images/1*S5QRnVnjsJaP6LSR-f1yVg.png)

Le binaire n'est que des 1 et des 0, n'est-ce pas ? Ces 1 et 0 représentent des interrupteurs "on" et "off"—`true` et `false`. La forme binaire de `true` est 1, et celle de `false` est 0. Gardez cela à l'esprit.

Maintenant que nous avons "sanitisé" `targetLength`, nous commençons le déplacement à droite.

Le déplacement à droite signifie que vous déplacez chaque bit à droite `n` fois. C'est tout.

Voici une visualisation PowerPoint de `11 >> 1` (J'avais oublié à quel point PowerPoint est génial).

![](https://cdn-media-1.freecodecamp.org/images/1*jANUTARhf9DaSPo_FdobsQ.gif)

Transformez 11 en 1011 et déplacez-le à droite 1 fois. Votre résultat final est 101, qui est 5 en binaire.

![](https://cdn-media-1.freecodecamp.org/images/1*hWhIMjgIzV8HsBHsoqaXkw.png)

Mais notre code dit `targetLength >> 0`.

### Donc nous déplaçons à droite 0 fois...

Le but de déplacer à droite 0 fois est d'abuser de cet effet secondaire de la conversion de `targetLength` en binaire. Nous ne voulons pas vraiment déplacer quoi que ce soit car cela changerait la valeur.

### Continuons

![](https://cdn-media-1.freecodecamp.org/images/1*9fp5LQLp8M02XXNypggPAw.png)

Passez maintenant au `debugger` de la ligne 7. `targetLength` a été sanitisé. **Suivant !**

![](https://cdn-media-1.freecodecamp.org/images/1*5olkuOlk90Alu9tVfbjS9Q.png)

**Ligne 11.**

```js
padString = String(padString || ' ');
```

Si nous ne fournissons pas d'argument `padString`, il est par défaut un espace vide. Je ne l'avais jamais remarqué jusqu'à maintenant.

![](https://cdn-media-1.freecodecamp.org/images/1*esccGoVlxpemIBmMunjmXA.png)

**Ligne 17.**

Remarquez comment la ligne 13 avait une autre vérification de sécurité, "Si la longueur de la chaîne originale est supérieure à `targetLength`, ne faites rien. Retournez simplement la chaîne originale"

Cela a du sens car si notre `targetLength` est 1, mais que la chaîne fait déjà 10 caractères, quel est l'intérêt ? Nous l'avons démontré plus tôt avec

```js
// retourne simplement 'world'
'world'.padStart(0, 'hello ');
```

La ligne 18 détermine combien de **caractères supplémentaires** nous avons besoin en soustrayant `targetLength` de la longueur de la chaîne originale. Nous avons besoin de 6, dans ce cas.

![](https://cdn-media-1.freecodecamp.org/images/1*fNa4w2qk360VICQLqvp6jQ.png)

**Ligne 27.**

Nous avons sauté cette déclaration `if` à la ligne 20 parce que `targetLength` et `padString.length` se sont avérés être les mêmes, mais nous y reviendrons bientôt.

Pour l'instant, nous sommes arrêtés juste avant la ligne 29. Décomposons-la.

```js
padString.slice(0, targetLength);
```

La bonne vieille méthode `String.prototype.slice`.

[**Documentation MDN**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/slice):

> La méthode `slice()` extrait une section d'une chaîne et la retourne en tant que nouvelle chaîne.

Elle est basée sur l'index, donc nous commençons à l'index 0 de `padString`, et nous prenons le nombre de caractères égal à `targetLength`. C'est un peu comme

![](https://cdn-media-1.freecodecamp.org/images/1*5fgldncMrn1M42TDNexc5w.png)

Retournez cette `padString` découpée combinée avec la chaîne originale, et vous avez terminé !

![](https://cdn-media-1.freecodecamp.org/images/1*dPcP4geY5bM3H_Qu53rF3Q.png)

### _Presque_ terminé

Normalement, je conclurais ici, mais nous n'avons pas exploré cette déclaration `if` à la ligne 20. Pour nous assurer de l'atteindre cette fois, essayons un autre exemple précédent

```js
'yo'.padStart(20, 'yo');
```

![](https://cdn-media-1.freecodecamp.org/images/1*xMe4-5cz9E4TcaxRV-OpCw.png)

J'ai sauté à la ligne 20 parce que nous savons déjà ce qui se passe jusqu'à ce point.

`if (targetLength > padString.length)`

`targetLength` est 18, et `padString` est `'yo'`, avec une longueur de 2.
18 > 2, donc quoi ensuite ?

```js
padString += padString.repeat(targetLength / padString.length);
```

Rappelez-vous, `padStart` retourne une `padString` _découpée_ + la chaîne originale. Si vous voulez compléter `'yo'` avec `'yo'` jusqu'à ce qu'il fasse 20 caractères de long, vous devrez le répéter plusieurs fois. C'est là que cette logique se produit, en utilisant `padString.repeat`.

[**Documentation MDN**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/repeat):

> La méthode `repeat()` construit et retourne une nouvelle chaîne qui contient le nombre spécifié de copies de la chaîne sur laquelle elle a été appelée, concatenées ensemble.

Donc, elle copie/colle la chaîne `n` fois.

Afin de déterminer combien de répétitions nous avons besoin, divisez `targetLength` par `padString.length`.

![](https://cdn-media-1.freecodecamp.org/images/1*8uNfkR56h7AhooHJILFSJQ.png)

Répétez `'yo'` 9 fois et obtenez une chaîne de `'yo'` qui fait 18 caractères de long. Ajoutez cela à votre `'yo'` original, et votre compte final est de 20 caractères.

![](https://cdn-media-1.freecodecamp.org/images/1*0A9siQbKWnKn6cFuidfNMQ.png)

Mission accomplie. À la prochaine !