---
title: Comment activer les crochets dans RegEx ?
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-04-27T12:31:45.000Z'
originalURL: https://freecodecamp.org/news/how-do-i-enable-square-brackets-in-regex
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/regexSquareBrackets.png
tags:
- name: Regex
  slug: regex
seo_title: Comment activer les crochets dans RegEx ?
seo_desc: 'In this article, you’ll learn about what square brackets do in regular
  expressions, how to use them for specifying ranges, and how to match them as a character.

  What Does Square Bracket Do in RegEx?

  In regular expressions, square brackets ([ ]) are c...'
---

Dans cet article, vous apprendrez ce que font les crochets dans les expressions régulières, comment les utiliser pour spécifier des plages et comment les faire correspondre en tant que caractère.


## Que font les crochets dans RegEx ?
Dans les expressions régulières, les crochets (`[ ]`) sont des caractères qui ont une signification spéciale. Puisqu'ils ont une signification spéciale, vous pouvez les appeler "metacaractère". Les crochets vous aident à définir un ensemble de caractères, qui est un ensemble de caractères que vous souhaitez faire correspondre.

Par exemple, `[aeiou]` correspondrait à toutes les voyelles

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-27-at-11.44.03.png)
_Correspondances de voyelles avec des crochets dans RegEx_

En plus de cela, certains caractères peuvent avoir des significations spéciales à l'intérieur des crochets.

Par exemple, si vous placez un circonflexe (`^`) avant tout autre caractère à l'intérieur des crochets, cela signifie que vous négociez les caractères qui suivent le circonflexe. C'est-à-dire, **vous dites au moteur regex ou à votre langage de programmation de ne pas faire correspondre ces caractères**.

Dans la capture d'écran ci-dessous, j'ai fait correspondre toutes les non-voyelles et les espaces en niant toutes les voyelles à l'intérieur d'un crochet.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-27-at-11.44.47.png)
_Négation de toutes les non-voyelles et espaces avec des crochets dans RegEx_

Dans un autre cas, si vous placez un trait d'union (`-`) entre deux caractères à l'intérieur des crochets, cela signifie **plage**.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-27-at-11.47.35.png)
_Spécification de la plage avec des crochets dans RegEx_

Mais il y a des situations où vous voulez faire correspondre les crochets en tant que caractère propre. Voyons comment faire cela ensuite – le but de cet article.


## Comment activer les crochets dans RegEx
Si vous vous trouvez dans une situation où vous voulez faire correspondre les crochets, par exemple, comme vous devez le faire lorsque vous faites correspondre des caractères spéciaux pour les mots de passe, **vous devez les échapper**.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-27-at-11.50.20.png)
_Correspondance des crochets dans RegEx_

## Comment utiliser les crochets et les activer en JavaScript
JavaScript fonctionne bien avec les crochets en tant que métacaractères et en tant que caractère propre.

```js
const text =
  'This is the opening square bracket [ and this is the closing square bracket ] Both [ and ] are everyday part of regex';

const regex = /\[|\]/g;

console.log(regex.test(text)); //true
```

Vous pouvez aller plus loin et parcourir les correspondances en utilisant la méthode `exec()` et une boucle `while` :

```js
const text =
  'This is the opening square bracket [ and this is the closing square bracket ] Both [ and ] are everyday part of regex';

const regex = /\[|\]/g;

let match;
while ((match = regex.exec(text)) !== null) {
  console.log('A match:', match[0], 'at Index:', match.index);
}
```
![Screenshot-2023-04-27-at-12.14.23](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-27-at-12.14.23.png)


## Conclusion
Cet article vous a montré comment utiliser les crochets en tant que métacaractères et en tant que caractère propre dans les moteurs RegEx et JavaScript.

Il est important de garder à l'esprit que certains langages de programmation ou moteurs regex peuvent avoir une syntaxe ou des règles légèrement différentes pour l'utilisation des crochets et autres métacaractères dans regex. Donc, si vous utilisez des crochets avec d'autres moteurs regex et langages de programmation autres que JavaScript, assurez-vous de comprendre comment ils fonctionnent avec les crochets.

Continuez à coder !