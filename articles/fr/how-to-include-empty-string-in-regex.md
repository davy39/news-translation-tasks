---
title: Comment inclure une chaîne vide dans RegEx
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-03-31T11:50:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-include-empty-string-in-regex
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/start-graph--7-.png
tags:
- name: Regex
  slug: regex
seo_title: Comment inclure une chaîne vide dans RegEx
seo_desc: "Regular expressions (RegEx or RegExp for short) are a sequence of characters\
  \ that define a search pattern. \nYou can use them to search, replace, and validate\
  \ the strings of a text in a wide variety of applications, such as text editors,\
  \ developer too..."
---

Les expressions régulières (RegEx ou RegExp en abrégé) sont une séquence de caractères qui définissent un motif de recherche. 

Vous pouvez les utiliser pour rechercher, remplacer et valider les chaînes de texte dans une grande variété d'applications, telles que les éditeurs de texte, les outils de développement et les outils en ligne de commande.

RegEx est également largement utilisé dans les langages de programmation car beaucoup de ces langages ont un support intégré pour celui-ci.

Puisque vous pouvez faire correspondre les chaînes de texte avec RegEx, cela signifie que vous pouvez également faire correspondre des chaînes vides. 

Dans cet article, je vais vous montrer trois façons de faire correspondre une chaîne vide dans RegEx.

## Ce que nous allons couvrir
- [Comment faire correspondre une chaîne vide dans RegEx avec les métacaractères caret et dollar](#heading-comment-faire-correspondre-une-chaine-vide-dans-regex-avec-les-metacaracteres-caret-et-dollar)
- [Comment faire correspondre une chaîne vide dans RegEx avec un lookahead](#heading-comment-faire-correspondre-une-chaine-vide-dans-regex-avec-un-lookahead)
- [Comment faire correspondre une chaîne vide dans RegEx avec un negative lookahead](#heading-comment-faire-correspondre-une-chaine-vide-dans-regex-avec-un-negative-lookahead)
- [Conclusion](#heading-conclusion)


## Comment faire correspondre une chaîne vide dans RegEx avec les métacaractères caret et dollar
Les métacaractères caret (`^`) et dollar (`$`) correspondent respectivement au début et à la fin d'une chaîne.
![Screenshot-2023-03-31-at-08.22.21](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-31-at-08.22.21.png)

Ainsi, si vous ne mettez rien entre les deux `^` et `$`, cela correspond à une chaîne vide :

```console
^$
```


## Comment faire correspondre une chaîne vide dans RegEx avec un lookahead
Dans RegEx, un lookahead est une assertion de largeur nulle qui vous permet de faire correspondre une chaîne uniquement si elle est suivie d'une autre chaîne spécifique sans inclure cette chaîne spécifique dans le résultat de la correspondance. 

Il existe des lookaheads positifs et négatifs dans RegEx. `?=` indique un lookahead positif et `?!` indique un lookahead négatif. Vous pouvez les utiliser pour créer des expressions régulières plus complexes.

Voyons comment faire correspondre une chaîne vide avec un lookahead positif :

```console
^(?=\s*$)
```

Dans le motif ci-dessus :
* le caractère `^` correspond au début de la chaîne
* le `(?=\s*$)` est un lookahead positif qui correspond à une position dans la chaîne où ce qui suit est vrai :
* `\s*` correspond à zéro ou plusieurs caractères d'espace blanc
* `$` correspond à la fin de la chaîne

Puisque le lookahead ne correspond qu'à la position et non à des caractères, l'expression régulière ne correspondra qu'à une chaîne vide.


## Comment faire correspondre une chaîne vide dans RegEx avec un negative lookahead
Comme je l'ai mentionné précédemment, `?!` spécifie un lookahead négatif. Vous pouvez utiliser le lookahead négatif ci-dessous pour faire correspondre une chaîne vide :

```console
^(?!.*\S)
```

Dans le RegEx ci-dessus :
* le caractère `^` correspond au début de la chaîne
* le `(?!.*\S)` est un lookahead négatif qui correspond à une position dans la chaîne où ce qui suit n'est pas vrai :
* `.*` correspond à zéro ou plusieurs caractères
* `\S` correspond à n'importe quel caractère non blanc

Puisque le lookahead négatif ne correspond qu'à la position et non à des caractères, l'expression régulière correspondra à une chaîne vide.


## Conclusion
Dans de nombreux moteurs de test RegEx, vous n'obtiendrez pas de correspondance pour une chaîne vide si vous testez une chaîne vide avec des métacaractères de début et de fin, un lookahead négatif et un lookahead positif.
![Screenshot-2023-03-31-at-09.19.48](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-31-at-09.19.48.png)

Mais en JavaScript, par exemple, vous obtiendrez une correspondance :
```js
// Métacaractères de début et de fin
const regEx1 = /^$/g;

// Lookahead positif
const regEx2 = /^(?=\s*$)/g;

// Lookahead négatif
const regEx3 = /^(?!.*\S)/g;

const text = '';

console.log(regEx1.exec(text)); // [ '', index: 0, input: '', groups: undefined ]
console.log(regEx2.exec(text)); // [ '', index: 0, input: '', groups: undefined ]
console.log(regEx3.exec(text)); // [ '', index: 0, input: '', groups: undefined ]

console.log('\n');

console.log(regEx1.test(text)); // true
console.log(regEx2.test(text)); // true
console.log(regEx3.test(text)); // true
```

Bonne programmation !