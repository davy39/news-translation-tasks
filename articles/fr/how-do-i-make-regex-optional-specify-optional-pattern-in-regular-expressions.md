---
title: Comment rendre RegEx optionnel ? Spécifier un motif optionnel dans les expressions
  régulières
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-03-09T11:34:42.000Z'
originalURL: https://freecodecamp.org/news/how-do-i-make-regex-optional-specify-optional-pattern-in-regular-expressions
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/start-graph--5-.png
tags:
- name: Regex
  slug: regex
seo_title: Comment rendre RegEx optionnel ? Spécifier un motif optionnel dans les
  expressions régulières
seo_desc: 'Regular expressions are greedy by default, meaning they try to match as
  many strings as possible. One of the ways to write accurate regular expressions
  is to make them as lazy as possible.

  The metacharacter that helps achieve laziness is the question...'
---

Les expressions régulières sont gourmandes par défaut, ce qui signifie qu'elles tentent de faire correspondre autant de chaînes que possible. L'une des façons d'écrire des expressions régulières précises est de les rendre aussi paresseuses que possible.

Le métacaractère qui aide à atteindre la paresse est le point d'interrogation `?`. Il vous aide à rendre n'importe quel motif RegEx optionnel.

Dans cet article, nous allons examiner le métacaractère du point d'interrogation et comment vous pouvez rendre n'importe quel motif RegEx optionnel avec lui.


## Qu'est-ce que le métacaractère du point d'interrogation `?` ?
Le métacaractère du point d'interrogation `?` est un quantificateur qui spécifie 0 ou 1. Les autres quantificateurs courants sont l'astérisque (`*`) et le plus (`+`). L'astérisque signifie 0 ou plusieurs et le plus signifie 1 ou plusieurs.

Contrairement à de nombreux autres métacaractères, vous n'avez pas besoin d'échapper le métacaractère du point d'interrogation `?` pour qu'il fonctionne. La seule fois où vous devez l'échapper est lorsque vous voulez faire correspondre le symbole du point d'interrogation lui-même.
![Screenshot-2023-03-09-at-08.54.31](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-09-at-08.54.31.png)


## Comment utiliser le quantificateur zéro ou un `?` dans RegEx
Le quantificateur du point d'interrogation peut être utile lorsque vous attendez deux entrées différentes mais acceptables de la part d'un utilisateur.

Par exemple, si vous attendez que l'utilisateur tape "color" ou "behavior", mais que vous n'êtes pas sûr s'il parle anglais britannique ou américain, vous pouvez rendre le "u" optionnel :
![Screenshot-2023-03-09-at-09.08.31](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-09-at-09.08.31.png)

En plaçant le symbole du point d'interrogation devant la lettre "u", cela signifie que le "u" est optionnel. Ainsi, "color" et "colour" sont appariés, "behavior" et "behaviour" sont également appariés.

Vous pouvez également utiliser le quantificateur du point d'interrogation pour réduire la gourmandise dans vos expressions régulières.

Par exemple, essayons de faire correspondre tout ce qui se trouve à l'intérieur des balises de paragraphe ci-dessous :
```html
<p>freeCodeCamp est le meilleur endroit pour apprendre à coder gratuitement</p> <p>freeCodeCamp est omniprésent</p>

<p>Vous pouvez apprendre n'importe quelle compétence technique avec freeCodeCamp</p>
```

Ce motif, `/<p>.*<\/p>/g` correspondrait à tout ce qui se trouve à l'intérieur des balises. Tout serait deux correspondances en raison du retour à la ligne séparant la dernière balise `p` des autres :
![Screenshot-2023-03-09-at-09.18.06](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-09-at-09.18.06.png)

Vous pouvez séparer toutes les balises en correspondances séparées avec le quantificateur zéro ou un (`?`) :
![Screenshot-2023-03-09-at-09.19.44](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-09-at-09.19.44.png)

Et si vous voulez que seule la première balise de paragraphe soit la correspondance, vous pouvez désactiver le drapeau `global` :
![Screenshot-2023-03-09-at-09.20.41](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-09-at-09.20.41.png)

Le quantificateur zéro ou un (`?`) fonctionnerait également bien dans n'importe quelle langue qui supporte RegEx. Voici un exemple en JavaScript :
```js
let str1 = 'Color is American';
let str2 = 'Colour is British';

let re1 = /colou?r/i;

console.log(re1.exec(str1)); // [ 'Color', index: 0, input: 'Color is American', groups: undefined ]
console.log(re1.exec(str2)); // [ 'Colour', index: 0, input: 'Colour is British', groups: undefined ]
```

## Conclusion
Le quantificateur zéro ou un aide à empêcher les expressions régulières d'être gourmandes en rendant une chaîne optionnelle sur elle-même ou au sein d'autres. Vous devriez l'utiliser lorsque cela est nécessaire afin d'écrire des expressions régulières moins gourmandes et plus précises.

Bon codage !