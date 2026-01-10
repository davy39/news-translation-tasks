---
title: Qu'est-ce que Punct en RegEx ? Comment faire correspondre tous les signes de
  ponctuation dans les expressions régulières
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-04-28T11:28:37.000Z'
originalURL: https://freecodecamp.org/news/what-is-punct-in-regex-how-to-match-all-punctuation-marks-in-regular-expressions
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/matchPunctuationRegEx.png
tags:
- name: Regex
  slug: regex
seo_title: Qu'est-ce que Punct en RegEx ? Comment faire correspondre tous les signes
  de ponctuation dans les expressions régulières
seo_desc: "In regular expressions, \"punct\" means punctuation marks. It is all non-word\
  \ and non-space characters. \"Punct\" is a predefined character class in regular\
  \ expressions, and you can use it in any regex flavor that supports it. \nThe Punct\
  \ character class ..."
---

Dans les expressions régulières, "punct" signifie signes de ponctuation. Il s'agit de tous les caractères non-mots et non-espaces. "Punct" est une classe de caractères prédéfinie dans les expressions régulières, et vous pouvez l'utiliser dans n'importe quel type de regex qui la supporte. 

La classe de caractères `Punct` est désignée par `\p{Punct}` ou simplement `\p{P}`. Elle correspond à tout signe de ponctuation dans une chaîne. Cela inclut des caractères tels que les points, les virgules, les points d'exclamation et les guillemets. 

Puisqu'il existe un moyen de faire correspondre tous les signes de ponctuation, c'est ce que nous allons examiner dans cet article.


## Comment faire correspondre tous les signes de ponctuation dans les moteurs RegEx
Peu de moteurs regex supportent `\p{P}`. Donc, pour ceux qui le supportent, `\p{P}` correspondra à tous les signes de ponctuation. 
![Screenshot-2023-04-28-at-08.07.14](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-28-at-08.07.14.png)

Pour les moteurs regex qui ne supportent pas `\p{P}`, vous pouvez faire correspondre tous les signes de ponctuation en niant les caractères mots et les caractères espaces avec le motif `[^\w\s]+` :
![Screenshot-2023-04-28-at-08.10.24](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-28-at-08.10.24.png)


## Comment faire correspondre tous les signes de ponctuation dans les RegEx JavaScript
Si vous souhaitez utiliser le motif `\p{P}` pour faire correspondre tous les signes de ponctuation en JavaScript, vous devez lui attribuer le flag Unicode comme ceci `/\p{P}/u`. Sinon, cela ne fonctionnera pas. Voyons cela en action :

```js
const text = `That said, Kolade, you don't have to forget to take home things you buy at the store again. Do you understand?

I just said that to show you that the pattern really matches punctuation marks. I don't forget things at the store. Here are other punctuation marks:! " # $ % & ' ( ) * + , - . / : ; | < = > { } ? @ [ \ ] ^ _ `;

const regex1 = /\p{P}/gu;
const regex2 = /[^\w\s]+/g;

console.log(regex1.test(text)); //true
console.log(regex2.test(text)); //true

console.log(regex1.exec(text));
console.log(regex2.exec(text));
```

Puisque `exec()` ne retournera qu'une seule correspondance et `test()` ne retournera qu'un booléen, vous pouvez parcourir les correspondances avec `exec()` et une boucle `while` pour les voir toutes :

```js
const text = `That said, Kolade, you don't have to forget to take home things you buy at the store again. Do you understand?

I just said that to show you that the pattern really matches punctuation marks. I don't forget things at the store. Here are other punctuation marks:! " # $ % & ' ( ) * + , - . / : ; | < = > { } ? @ [ \ ] ^ _ `;

const regex1 = /\p{P}/gu;
const regex2 = /[^\w\s]+/g;

let match;

while ((match = regex1.exec(text)) !== null) {
  console.log('A match: ', match[0], 'at index: ', match.index);
}
```
![Screenshot-2023-04-28-at-08.28.30](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-28-at-08.28.30.png)


## Conclusion
Voici comment vous pouvez faire correspondre tous les signes de ponctuation dans les moteurs regex et JavaScript. N'oubliez pas que si vous utilisez `\p{P}` pour faire correspondre les signes de ponctuation, vous devez l'utiliser avec le flag Unicode comme ceci `/\p{P}/u`. Vous pouvez également appliquer la même chose à d'autres langages de programmation.

Si vous souhaitez en savoir plus sur les expressions régulières, vous pouvez utiliser [cette vidéo](https://www.youtube.com/watch?v=ZfQFUJhPqMM) réalisée par Beau Carnes de freeCodeCamp.

Continuez à coder !