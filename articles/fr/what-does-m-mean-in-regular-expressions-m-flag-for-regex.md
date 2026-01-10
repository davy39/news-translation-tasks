---
title: Que signifie M dans les expressions régulières ? Le drapeau M pour RegEx
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-04-26T14:31:31.000Z'
originalURL: https://freecodecamp.org/news/what-does-m-mean-in-regular-expressions-m-flag-for-regex
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/mFlagRegex.png
tags:
- name: Regex
  slug: regex
seo_title: Que signifie M dans les expressions régulières ? Le drapeau M pour RegEx
seo_desc: 'In regular expressions, "m" is a flag that signifies multiple lines. So,
  it is popularly called the "multiline flag".

  In this article, I will show you what the "m" flag does and how you can use it in
  both regex engines and JavaScript.

  What Does the "...'
---

Dans les expressions régulières, "m" est un drapeau qui signifie plusieurs lignes. Il est donc populairement appelé le "drapeau multiline".

Dans cet article, je vais vous montrer ce que fait le drapeau "m" et comment vous pouvez l'utiliser dans les moteurs regex et en JavaScript.


## Que fait le drapeau "m" ?
Parfois, vous voulez que vos correspondances ne se produisent pas seulement sur une seule ligne, mais aussi sur d'autres lignes en dessous de la première. C'est là que le drapeau multiline est influent. 

Presque tous les moteurs regex populaires ont un moyen d'activer et de désactiver le drapeau multiline.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-26-at-12.48.37.png)
_RegEx 101_

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-26-at-12.49.25.png)
_RegExr_

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-26-at-12.48.50.png)
_RegEx Tester from Dan's Tools_

## Comment utiliser le drapeau "m" dans les moteurs RegEx
Si vous voulez que vos correspondances ne soient pas limitées à la première ligne lors de l'utilisation d'un moteur regex, tout ce que vous avez à faire est d'activer le drapeau "m".

![Screenshot-2023-04-26-at-13.04.45](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-26-at-13.04.45.png)

J'ai activé le drapeau multiline et il ne correspond pas à toutes les lignes. Pourquoi cela ?

C'est parce que souvent, vous devez également utiliser le drapeau global ["g"] avec le drapeau "m" pour obtenir toutes les correspondances :
![Screenshot-2023-04-26-at-13.06.23](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-26-at-13.06.23.png)


## Comment utiliser le drapeau "m" dans les expressions régulières JavaScript
Rappelez-vous que pour utiliser le drapeau des expressions régulières en JavaScript, vous devez le spécifier comme deuxième argument d'un constructeur `RegExp()`. Et si vous créez votre Regex avec des barres obliques, les drapeaux doivent être à l'extérieur des barres obliques.

```js
// un drapeau est le deuxième argument d'un constructeur RegExp
const regex1 = new RegExp('line', 'gm');

// un drapeau est la lettre à l'extérieur lorsque vous créez une regex avec deux barres obliques
const regex2 = /line/gm;
```

Voici comment j'utilise le "m" en conjonction avec le drapeau "g" pour correspondre à plusieurs lignes en JavaScript :

```js
const regex2 = /line/gim;

const multiLineStr = `Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7`;

console.log(regex2.test(multiLineStr)); // true

if (regex2.test(multiLineStr)) {
  console.log('There are multiple matches'); // Il y a plusieurs correspondances
} else {
  console.log('Found no match');
}
``` 


## Conclusion
Vous pouvez maintenant voir à quel point le drapeau multiline est utile pour obtenir des correspondances sur toutes les lignes de texte. 

Si vous avez trouvé l'article utile, n'hésitez pas à le partager avec vos amis et votre famille.

Bon codage !