---
title: Le meilleur mème JavaScript que j'ai jamais vu, expliqué en détail
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-30T07:00:00.000Z'
originalURL: https://freecodecamp.org/news/explaining-the-best-javascript-meme-i-have-ever-seen
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/cover-photo.png
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: Le meilleur mème JavaScript que j'ai jamais vu, expliqué en détail
seo_desc: 'By Yazeed Bzadough

  TLDR: Coerce yourself to use triple equals.

  I unintentionally found this JavaScript meme on Reddit, and it''s the best one I''ve
  ever seen.


  You can verify this meme''s accuracy by running each code snippet in Developer Tools.
  The res...'
---

Par Yazeed Bzadough

### TLDR : Forcez-vous à utiliser le triple égal.

J'ai involontairement trouvé ce mème JavaScript sur Reddit, et c'est le meilleur que j'aie jamais vu.

![best-js-meme-to-date-2](https://www.freecodecamp.org/news/content/images/2019/07/best-js-meme-to-date-2.png)

Vous pouvez vérifier l'exactitude de ce mème en exécutant chaque extrait de code dans les outils de développement. Le résultat n'est pas surprenant, mais reste un peu décevant.

Bien sûr, cette petite expérience m'a conduit à me demander...

## Pourquoi cela arrive-t-il ?
![why-does-this-happen](https://www.freecodecamp.org/news/content/images/2019/07/why-does-this-happen.png)

Avec l'expérience, j'ai appris à embrasser les côtés lisses de JavaScript tout en me méfiant de ses piques. Néanmoins, les détails de ce cas particulier m'ont encore piqué.

C'est exactement comme le dit Kyle Simpson...
> "Je ne pense pas que quiconque connaisse vraiment JS, du moins pas complètement."

Lorsque ces cas apparaissent, il est préférable de consulter la source – la [spécification officielle ECMAScript](http://ecma-international.org/ecma-262/) sur laquelle JavaScript est basé.

Avec la spécification en main, comprenons profondément ce qui se passe ici.

## Panneau 1 - Introduction à la coercition
![panel-1-1](https://www.freecodecamp.org/news/content/images/2019/07/panel-1-1.png)

Si vous exécutez `0 == "0"` dans votre console de développement, pourquoi retourne-t-il `true` ?

`0` est un nombre, et `"0"` est une chaîne de caractères, ils ne devraient jamais être identiques ! La plupart des langages de programmation respectent cela. `0 == "0"` en Java, par exemple, retourne ceci :

```
error: incomparable types: int and String
```

Cela a parfaitement du sens. Si vous voulez comparer un int et une String en Java, vous devez d'abord les convertir vers le même type.

Mais nous sommes en JavaScript, les amis !
![this-is-javascript](https://www.freecodecamp.org/news/content/images/2019/07/this-is-javascript.jpeg)

Lorsque vous comparez deux valeurs via `==`, l'une des valeurs peut subir une _coercition_.

> Coercition – **Automatiquement** changer une valeur d'un type à un autre.

_**Automatiquement**_ est le mot clé ici. Au lieu de convertir vous-même _explicitement_ vos types, JavaScript le fait pour vous en coulisses.

![scumbag-javascript](https://www.freecodecamp.org/news/content/images/2019/07/scumbag-javascript.jpeg)

Cela est pratique si vous l'exploitez intentionnellement, mais potentiellement dangereux si vous n'êtes pas conscient de ses implications.

Voici la [spécification officielle du langage ECMAScript](https://www.ecma-international.org/ecma-262/5.1/#sec-11.9.3) à ce sujet. Je vais paraphraser la partie pertinente :

> Si x est un Number et y est une String, retourner x == ToNumber(y)

Donc pour notre cas de `0 == "0"` :
> Puisque 0 est un Number et "0" est une String, retourner 0 == ToNumber("0")

Notre chaîne `"0"` a été secrètement convertie en `0`, et maintenant nous avons une correspondance !

```js
0 == "0" // true
// Le second 0 est devenu un nombre !
// donc 0 est égal à 0 est vrai....
```

![that-string-secretly-became-a-number](https://www.freecodecamp.org/news/content/images/2019/07/that-string-secretly-became-a-number.jpeg)

Bizarre, non ? Eh bien, habituez-vous, nous ne sommes même pas à moitié terminés.

## Panneau 2 - Les tableaux subissent aussi la coercition
![panel-2](https://www.freecodecamp.org/news/content/images/2019/07/panel-2.png)

Ces absurdités ne sont pas limitées aux types primitifs comme les chaînes de caractères, les nombres ou les booléens. Voici notre prochaine comparaison :

```js
0 == [] // true
// Qu'est-il arrivé... ?
```

Encore la coercition ! Je vais paraphraser la partie pertinente de la spécification :
> Si x est une String ou un Number et y est un Object, retourner x == ToPrimitive(y)

Trois points ici :

### 1. Oui, les tableaux sont des objets
![arrays-are-objects](https://www.freecodecamp.org/news/content/images/2019/07/arrays-are-objects.jpg)

Désolé de vous l'apprendre.

### 2. Un tableau vide devient une chaîne vide
Encore une fois [selon la spécification](https://www.ecma-international.org/ecma-262/5.1/#sec-8.12.8), JS cherche d'abord la méthode `toString` d'un objet pour le coerce.

Dans le cas des tableaux, `toString` joint tous ses éléments et les retourne sous forme de chaîne.

```js
[1, 2, 3].toString() // "1,2,3"
['hello', 'world'].toString() // "hello,world"
```

Puisque notre tableau est vide, nous n'avons rien à joindre ! Par conséquent...
```js
[].toString() // ""
```

![empty-array-coerces-to-empty-string-1](https://www.freecodecamp.org/news/content/images/2019/07/empty-array-coerces-to-empty-string-1.jpeg)

La fonction `ToPrimitive` de la spécification transforme ce tableau vide en une chaîne vide. Les références sont [ici](https://www.ecma-international.org/ecma-262/5.1/#sec-9.1) et [ici](https://www.ecma-international.org/ecma-262/5.1/#sec-8.12.8) pour votre commodité (ou confusion).

### 3. La chaîne vide devient ensuite 0
![empty-strings-become-0](https://www.freecodecamp.org/news/content/images/2019/07/empty-strings-become-0.jpeg)

On ne peut pas inventer ce genre de choses. Maintenant que nous avons coercé le tableau en `""`, nous revenons au premier algorithme...

> Si x est un Number et y est une String, retourner x == ToNumber(y)

Donc pour `0 == ""`
> Puisque 0 est un Number et "" est une String, retourner 0 == ToNumber("")

`ToNumber("")` retourne 0.

Par conséquent, `0 == 0` une fois de plus...

![coercion-every-time-2](https://www.freecodecamp.org/news/content/images/2019/07/coercion-every-time-2.jpeg)

## Panneau 3 - Récapitulatif rapide
![panel-3-1](https://www.freecodecamp.org/news/content/images/2019/07/panel-3-1.png)

### Ceci est vrai
```js
0 == "0" // true
```

Parce que la coercition transforme cela en `0 == ToNumber("0")`.

### Ceci est vrai
```js
0 == [] // true
```

Parce que la coercition s'exécute deux fois :
1. `ToPrimitive([])` donne une chaîne vide
2. Ensuite `ToNumber("")` donne 0.

Alors dites-moi... selon les règles ci-dessus, que devrait retourner ceci ?
```js
"0" == []
```

## Panneau 4 - FAUX !
![panel-4-1](https://www.freecodecamp.org/news/content/images/2019/07/panel-4-1.png)

FAUX ! Correct.

Cette partie a du sens si vous avez compris les règles.

Voici notre comparaison :
```js
"0" == [] // false
```

En référence à la spécification une fois de plus :
> Si x est une String ou un Number et y est un Object, retourner x == ToPrimitive(y)

Cela signifie...
> Puisque "0" est une String et [] est un Object, retourner x == ToPrimitive([])

`ToPrimitive([])` retourne une chaîne vide. La comparaison est maintenant devenue

```js
"0" == ""
```

`"0"` et `""` sont toutes deux des chaînes de caractères, donc JavaScript dit _plus de coercition nécessaire_. C'est pourquoi nous obtenons `false`.

## Conclusion
![just-use-triple-equals](https://www.freecodecamp.org/news/content/images/2019/07/just-use-triple-equals.jpeg)

Utilisez le triple égal et dormez paisiblement la nuit.

```js
0 === "0" // false
0 === [] // false
"0" === [] // false
```

Cela évite complètement la coercition, donc je suppose que c'est aussi plus efficace !

Mais l'augmentation de performance est presque négligeable. Le vrai gain est la confiance accrue que vous aurez dans votre code, ce qui rend cette frappe supplémentaire totalement digne.

## Vous voulez un coaching gratuit ?
Si vous souhaitez planifier un appel **gratuit** de 15 à 30 minutes pour discuter de questions sur le développement Front-End concernant le code, les entretiens, la carrière ou autre chose, [suivez-moi sur Twitter et envoyez-moi un DM](https://twitter.com/yazeedBee).

Après cela, si vous appréciez notre première rencontre, nous pouvons discuter d'une relation de coaching continue qui vous aidera à atteindre vos objectifs de développement Front-End !

## Merci d'avoir lu
Pour plus de contenu comme celui-ci, consultez <a href="https://yazeedb.com">https://yazeedb.com !</a>

À la prochaine !