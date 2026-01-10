---
title: Que signifie le B dans les expressions régulières ? Limites de mot et métacaractères
  de non-limite de mot
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-03-08T14:10:22.000Z'
originalURL: https://freecodecamp.org/news/what-does-b-in-regex-mean-word-boundary-and-non-word-boundary-metacharacters
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/start-graph--4-.png
tags:
- name: Regex
  slug: regex
seo_title: Que signifie le B dans les expressions régulières ? Limites de mot et métacaractères
  de non-limite de mot
seo_desc: 'In regular expressions, “B” is a metacharacter for specifying word boundary.
  It could be in two forms – the capital letter “B” and the small letter “b”.

  Since B (and b) is a metacharacter, you need to escape it to make it work (\b and
  \B). Otherwise,...'
---

Dans les expressions régulières, « B » est un métacaractère pour spécifier une limite de mot. Il peut se présenter sous deux formes – la lettre majuscule « B » et la lettre minuscule « b ».

Puisque `B` (et `b`) est un métacaractère, vous devez l'échapper pour qu'il fonctionne (`\b` et `\B`). Sinon, `b` ou `B` serait interprété comme une lettre de l'alphabet.

Dans cet article, je vais vous guider à travers ces deux variations du caractère « B » dans les expressions régulières. Nous examinerons ce qu'ils font et leur utilisation dans les moteurs d'expressions régulières et la programmation.

## Ce que nous allons couvrir
- [Que fait le métacaractère « S » ?](#heading-que-fait-le-metacaractere-s)
- [Comment utiliser le métacaractère « B » dans les expressions régulières](#heading-comment-utiliser-le-metacaractere-b-dans-les-expressions-regulieres)
  - [Comment utiliser le métacaractère de limite de mot (`\b`)](#heading-comment-utiliser-le-metacaractere-de-limite-de-mot-b)
  - [Comment utiliser le métacaractère de non-limite de mot (`\B`)](#heading-comment-utiliser-le-metacaractere-de-non-limite-de-mot-b)
- [Conclusion](#heading-conclusion)


## Que fait le métacaractère « S » ?
Le métacaractère de la lettre minuscule « b » représente une limite de mot, et la lettre majuscule « B » représente une non-limite de mot. C'est ainsi que fonctionne le modèle pour la plupart des métacaractères.

Par exemple, la lettre minuscule « s » est le métacaractère pour un espace (espace, tabulation, retour chariot, nouvelle ligne), et la lettre majuscule « S » est le métacaractère pour un non-espace.

Vous pouvez [en savoir plus sur le métacaractère `s` ici](https://www.freecodecamp.org/news/what-does-s-in-regex-mean-space-and-negated-space-metacharacters/).

La lettre minuscule `\b` de limite de mot indique qu'un motif est délimité par un caractère non-mot. Les caractères non-mot sont tous les caractères autres que les chiffres, les lettres et le soulignement (`_`). Ils sont désignés par un autre métacaractère (`\W`).

D'autre part, la lettre majuscule `\B` est une non-limite de mot qui indique qu'un motif est délimité par un caractère de mot. Les caractères de mot sont les lettres, les chiffres et le soulignement (`_`). Ils sont désignés par un autre métacaractère (`\w`).


## Comment utiliser le métacaractère « B » dans les expressions régulières
Le métacaractère `\b` spécifie une limite de mot et `\B` spécifie une non-limite de mot. Les deux font référence à des positions, pas aux caractères réels, mais ils correspondent à des choses différentes car ils sont opposés.


### Comment utiliser le métacaractère de limite de mot (`\b`)
Voici comment fonctionne le métacaractère de limite de mot (`\b`) :

Par exemple, dans la phrase « One should take care of oneself before takin care of others one by one », placer `\b` avant le mot « one » comme motif défini correspondrait à chaque occurrence du mot « one » précédé par un caractère non-mot (tout ce qui n'est pas une lettre, un chiffre et un soulignement `_`) :
![Screenshot-2023-03-08-at-11.00.42](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-08-at-11.00.42.png)

Si je place `\b` de l'autre côté du mot « one » à nouveau, alors il correspondrait uniquement au mot « one » mais pas à « oneself » :
![Screenshot-2023-03-08-at-11.04.17](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-08-at-11.04.17.png)

Et c'est ce que fait le métacaractère de limite de mot – il vous permet de correspondre à la partie exacte d'une chaîne que vous souhaitez.

**Note** : J'ai pu correspondre au mot « One » parce que j'ai activé le drapeau d'insensibilité à la casse.

Vous n'avez pas non plus à utiliser le métacaractère de limite de mot avec un seul mot :
![Screenshot-2023-03-08-at-11.07.57](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-08-at-11.07.57.png)


### Comment utiliser le métacaractère de non-limite de mot (`\B`)
Pour le métacaractère de non-limite de mot (`\B`), rappelez-vous qu'il correspond à tout ce qui est délimité par un caractère de mot.

Voici comment je l'ai utilisé pour correspondre à « for » à l'intérieur du mot « before » :
![Screenshot-2023-03-08-at-11.15.04](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-08-at-11.15.04.png)

Et voici comment je l'ai utilisé pour extraire « king » du mot « taking » :
![Screenshot-2023-03-08-at-11.15.54](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-08-at-11.15.54.png)

Maintenant, si vous souhaitez correspondre au mot « the » à l'intérieur de « others », vous devez simplement entourer le mot « the » avec `\B` dans votre motif.

Les métacaractères `\b` et `\B` fonctionneraient également bien dans un langage comme JavaScript :
```js
let str =
  'One should take care of oneself before taking care of others one by one';

let regex1 = /\Bking/;
let regex2 = /\bone/;

console.log(regex1.exec(str));
console.log(regex2.exec(str));
```

Voici le résultat dans la console :
![Screenshot-2023-03-08-at-11.22.05](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-08-at-11.22.05.png)


## Conclusion
Les métacaractères de limite de mot et de non-limite de mot vous aident à extraire le mot exact dont vous avez besoin dans une chaîne ou même dans un mot particulier, ce qui est utile lors de la mise en œuvre de plusieurs validations pour les entrées utilisateur.

Bon codage !