---
title: Que signifie le circonflexe en RegEx ? Métacaractère circonflexe dans les expressions
  régulières
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-04-20T16:47:22.000Z'
originalURL: https://freecodecamp.org/news/what-does-the-caret-mean-in-regex-how-to-match-the-start-of-a-line-in-regular-expressions
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/caretMeta.png
tags:
- name: Regex
  slug: regex
seo_title: Que signifie le circonflexe en RegEx ? Métacaractère circonflexe dans les
  expressions régulières
seo_desc: "A caret (^) is one of the many symbols for creating patterns in regular\
  \ expressions. \nA caret matches the start of a line or a particular string. But\
  \ that’s not all there is to the caret (^) symbol.\nThe caret symbol (^) is often\
  \ referred to as an \"an..."
---

Un circonflexe (`^`) est l'un des nombreux symboles permettant de créer des motifs dans les expressions régulières. 

Un circonflexe correspond au début d'une ligne ou d'une chaîne de caractères. Mais ce n'est pas tout ce que fait le symbole circonflexe (`^`).

Le symbole circonflexe (`^`) est souvent appelé une "ancre" car il ancre le motif au début d'une ligne ou d'une chaîne. Vous pouvez donc l'appeler "ancre de début de ligne". 

L'autre ancre est le signe dollar (`$`), qui ancre le motif à la fin de la ligne, ce qui signifie qu'il s'agit d'une "ancre de fin de ligne".


## Ce que nous allons couvrir
- [Que fait le symbole circonflexe en RegEx](#heading-que-fait-le-symbole-circonflexe-en-regex)
- [Comment faire correspondre le début d'une ligne avec le circonflexe](#heading-comment-faire-correspondre-le-debut-dune-ligne-avec-le-circonflexe)
- [Comment nier un ensemble de caractères avec le circonflexe](#heading-comment-nier-un-ensemble-de-caracteres-avec-le-circonflexe)
- [Comment faire correspondre le circonflexe en tant que caractère dans une chaîne](#heading-comment-faire-correspondre-le-circonflexe-en-tant-que-caractere-dans-une-chaine)
- [Comment utiliser le métacaractère circonflexe en JavaScript](#heading-comment-utiliser-le-metacaractere-circonflexe-en-javascript)
- [Conclusion](#heading-conclusion)


## Que fait le symbole circonflexe en RegEx ?
Il y a deux choses principales que fait le symbole circonflexe : il correspond au début d'une ligne ou d'une chaîne, et il nie un ensemble de caractères lorsque vous le placez à l'intérieur des crochets.

De plus, vous pourriez vouloir faire correspondre le symbole circonflexe lui-même puisqu'il est utilisé pour d'autres choses en dehors des expressions régulières. Dans ce cas, vous devez l'échapper.


## Comment faire correspondre le début d'une ligne avec le circonflexe
Pour faire correspondre le début d'une ligne avec le symbole circonflexe, placez-le devant votre motif.

Dans l'exemple ci-dessous, j'ai le motif `/^hello\s*world/igm` qui ne correspondra qu'à un texte `hello world` qui se trouve au début d'une ligne. Tout autre `hello world` au milieu ou à la fin d'une ligne ne sera pas une correspondance :
![Screenshot-2023-04-20-at-14.21.33](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-20-at-14.21.33.png)

De plus, le motif `/^c/igm` ne correspondra qu'aux mots commençant par la lettre `c` uniquement s'ils sont au début de la ligne :
![Screenshot-2023-04-20-at-14.22.33](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-20-at-14.22.33.png)


## Comment nier un ensemble de caractères avec le circonflexe
Une autre chose que vous pouvez faire avec le circonflexe est de nier un ensemble de caractères. Par exemple, si vous voulez nier les voyelles, vous pouvez les placer dans un ensemble de caractères et placer le circonflexe devant elles :
![Screenshot-2023-04-20-at-14.29.46](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-20-at-14.29.46.png)

Vous pouvez voir que toutes les voyelles n'ont pas été correspondantes.


## Comment faire correspondre le circonflexe en tant que caractère dans une chaîne
Vous pouvez utiliser le circonflexe pour d'autres choses comme l'exponentiation en mathématiques et l'opérateur XOR bit à bit en C++. 

Si vous voulez le faire correspondre, vous devez l'échapper avec une barre oblique inverse `\` puisqu'il est reconnu comme un métacaractère par les moteurs RegEx :
![Screenshot-2023-04-20-at-14.39.07](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-20-at-14.39.07.png)


## Comment utiliser le métacaractère circonflexe en JavaScript
Le métacaractère circonflexe fonctionne bien en JavaScript. L'extrait de code ci-dessous montre que je le teste avec quelques chaînes :

```js
const text1 = `Il y a hello world dans chaque langage de programmation
Hello world est ce qui commence de nombreux cours de langage de programmation.
De nombreux programmeurs ne connaissent pas d'autre hello que hello world.`;

const text2 = `le circonflexe est une ancre qui fixe votre motif au début d'une ligne
Pour faire correspondre le circonflexe lui-même, vous devez l'échapper.`;

const text3 = '4 élevé à la puissance 2 en mathématiques est 4 ^ 2';

const re1 = /^hello\s*world/gim;
const re2 = /^c/gim;
const re3 = /\^/;

console.log(re1.test(text1)); //true
console.log(re2.test(text2)); //true
console.log(re3.test(text3)); //true
```


## Conclusion
Cet article vous a montré comment utiliser l'"ancre de début de ligne" (métacaractère circonflexe `^`) pour ancrer un motif au début d'une ligne ou d'une chaîne dans les moteurs RegEx et JavaScript.

Pour en savoir plus sur l'ancre de fin de ligne (`$`), vous pouvez lire [cet article](https://www.freecodecamp.org/news/what-does-mean-in-regex/).

Bon codage !