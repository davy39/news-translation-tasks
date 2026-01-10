---
title: 'ES2018 : les nouvelles fonctionnalités de JavaScript en 2018'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-12T16:14:32.000Z'
originalURL: https://freecodecamp.org/news/es9-javascripts-state-of-art-in-2018-9a350643f29c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xx6p4fNNuiKZe3bHO8M-kQ.png
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
seo_title: 'ES2018 : les nouvelles fonctionnalités de JavaScript en 2018'
seo_desc: 'By Flavio H. Freitas

  Our friends from TC39 have released new updates for our beloved JavaScript language.


  If you want to follow the process of the new releases by the committee, you can
  access this link. The process of approving and making a change ...'
---

Par Flavio H. Freitas

Nos amis de TC39 ont [publié](https://www.ecma-international.org/publications/standards/Ecma-262.htm) de nouvelles mises à jour pour notre langage JavaScript bien-aimé.

![Image](https://cdn-media-1.freecodecamp.org/images/bocZipyVNaJoZ43Q0DuUVShsFUBtYgbmhOAH)

Si vous souhaitez suivre le processus des nouvelles versions par le comité, vous pouvez accéder à ce [lien](https://github.com/tc39/proposals/blob/master/finished-proposals.md). Le processus d'approbation et de réalisation d'un changement passe par cinq étapes :

* Étape 0 : Strawman — Permettre l'entrée dans la spécification
* Étape 1 : Proposition — Faire valoir l'addition ; Décrire la forme d'une solution ; Identifier les défis potentiels
* Étape 2 : Brouillon — Décrire précisément la syntaxe et la sémantique en utilisant un langage de spécification formel
* Étape 3 : Candidat — Indiquer que d'autres raffinements nécessiteront des retours des implémentations et des utilisateurs
* Étape 4 : Terminé — Indiquer que l'addition est prête pour l'inclusion dans la norme ECMAScript formelle

Plus de détails peuvent être vus [ici](https://tc39.github.io/process-document/). Si vous voulez en savoir plus sur les changements précédents, consultez [ES6](https://medium.com/@flaviohfreitas/es6-javascript-does-love-you-f36c532c87db), [ES7](https://medium.com/@flaviohfreitas/es7-a-simple-and-useful-guide-to-master-it-6aba54abb4df) et [ES8](https://medium.freecodecamp.org/es8-the-new-features-of-javascript-7506210a1a22).

Alors voyons ce qu'ils ont ajouté ou mis à jour l'année dernière :

### 1. Beaucoup de changements dans les Regex

Nous avons quatre modifications pour les regex. Voyons-les :

#### Le drapeau `s` (`dotAll`) pour les expressions régulières

Lors de l'utilisation d'expressions régulières, vous vous attendez à ce que le point `.` corresponde à un seul caractère, mais ce n'est pas toujours vrai. Une exception est avec les caractères de terminaison de ligne :

```
/hello.bye/.test('hello\nbye') // affiche false
```

La solution est le nouveau drapeau /s (de singleline) :

```
/hello.bye/s.test('hello\nbye')  // affiche true
```

#### Groupes de capture nommés RegExp

Voici l'ancienne manière d'obtenir l'année, le mois et le jour à partir d'une date :

```
const REGEX = /([0-9]{4})-([0-9]{2})-([0-9]{2});const results = REGEX.exec('2018-07-12');console.log(results[1]); // affiche 2018console.log(results[2]); // affiche 07console.log(results[3]); // affiche 12
```

Et si vous travaillez avec une longue regex, vous savez à quel point il est difficile de suivre les groupes, les parenthèses et les indices. Avec le nouveau groupe de capture nommé, il est possible de :

```
const REGEX = /(?<year>[0-9]{4})-(?<month>[0-9]{2})-(?<day>[0-9]{2});const results = REGEX.exec('2018-07-12');console.log(results.groups.year);  // affiche 2018console.log(results.groups.month); // affiche 07console.log(results.groups.day);   // affiche 12
```

#### Assertions de look behind RegExp

Il existe deux versions d'assertions de look behind : positive et négative.

**a) Positive (?<**=\…)

```
'$foo #foo @foo'.replace(/(?<=#)foo/g, 'XXX')// affiche $foo #XXX @foo
```

Cette regex `(?<=#)foo/g` indique que le mot doit commencer par # et ne contribue pas à la chaîne globale correspondante (donc elle ne remplacera pas le caractère #).

**b) Négative (?<**!\…)

```
'$foo #foo @foo'.replace(/(?<!#)foo/g, 'XXX')// affiche $XXX #foo @XXX
```

Au contraire, cette assertion garantit qu'il ne commence pas par #.

#### Échappements de propriétés Unicode RegExp

Maintenant, nous pouvons rechercher des caractères en mentionnant leur propriété de caractère Unicode à l'intérieur de `\p{}`

```
/\p{Script=Greek}/u.test('\u03bc') // affiche true
```

Vous pouvez consulter plus de propriétés en cliquant [ici](http://unicode.org/reports/tr18/#RL1.2).

### 2. Propriétés Rest/Spread

L'opérateur rest `(...)` copie les clés de propriétés restantes qui n'ont pas été mentionnées. Regardons un exemple :

```
const values = {a: 1, b: 2, c: 3, d: 4};const {a, ...n} = values;console.log(a);   // affiche 1console.log(n);   // affiche {b: 2, c: 3, d: 4}
```

### 3. `Promise.prototype.finally`

Ce nouveau rappel sera toujours exécuté, que catch ait été appelé ou non.

```
fetch('http://website.com/files').then(data => data.json()).catch(err => console.error(err)).finally(() => console.log('traité !'))
```

### 4. Itération asynchrone

Enfin !

Maintenant, nous pouvons utiliser `await` dans nos déclarations de boucles.

```
for await (const line of readLines(filePath)) {  console.log(line);}
```

Et ce sont tous les changements de cette année. Attendons de voir ce qu'ils nous apporteront l'année prochaine.

*Si vous avez aimé cet article, n'oubliez pas de l'aimer et de m'applaudir — cela signifie beaucoup pour l'auteur ? Et [suivez-moi](https://medium.com/@flaviohfreitas) si vous voulez lire plus d'articles sur la Culture, la Technologie et les Startups.*

**Flávio H. de Freitas** est un entrepreneur, ingénieur, amateur de technologie, rêveur et voyageur. Il a travaillé en tant que **CTO** au **Brésil**, dans la **Silicon Valley et en Europe**.