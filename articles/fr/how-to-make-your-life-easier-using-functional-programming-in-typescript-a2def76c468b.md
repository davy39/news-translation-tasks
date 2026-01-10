---
title: Comment faciliter votre vie en utilisant la programmation fonctionnelle en
  TypeScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-22T11:21:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-your-life-easier-using-functional-programming-in-typescript-a2def76c468b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*HMvoDO2f0kCl49CLCdzMEQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment faciliter votre vie en utilisant la programmation fonctionnelle
  en TypeScript
seo_desc: 'By Mateusz Sokola

  Over the last two years, the JavaScript community has been talking about functional
  programming. Functional programming allows us to build better software without designing
  complex class trees. Today, I will explain how to use funct...'
---

Par Mateusz Sokola

Au cours des deux dernières années, la communauté JavaScript a beaucoup parlé de programmation fonctionnelle. La programmation fonctionnelle nous permet de construire de meilleurs logiciels sans concevoir des arbres de classes complexes. Aujourd'hui, je vais expliquer comment utiliser la composition de fonctions en [Typescript](https://www.typescriptlang.org/) et [Lodash](https://lodash.com/).

Le code peut être [trouvé sur Github](https://github.com/mateuszsokola/function-composition-typescript).

![Image](https://cdn-media-1.freecodecamp.org/images/1*HMvoDO2f0kCl49CLCdzMEQ.jpeg)

#### Qu'est-ce que la composition de fonctions ?

La composition de fonctions consiste à combiner deux fonctions ou plus pour en créer une plus complexe. Vous êtes confus ? Pas de souci, l'exemple suivant va tout éclaircir :

```
const f = function (a) { return a + 1 };const g = function (b) { return b * b };
```

```
const x = 2;const result = f(g(x)); // => 5
```

J'ai combiné deux fonctions ici — la fonction _f_ et la fonction _g_. La fonction f ajoute 1 au paramètre _a_, et la fonction _g_ multiplie le paramètre _b_ par _b_. Le résultat est 5.

Décomposons cela :

1. la constante _x_ est égale à 2
2. la constante _x_ devient un argument de la fonction _g_
3. la fonction _g_ retourne 4
4. la sortie de la fonction _g_ (4) devient un argument de la fonction _f_
5. la fonction _f_ retourne 5

Ce n'est pas de la science-fiction, mais cela ne semble pas particulièrement utile. En fait, cela semble même plus complexe que de tout garder dans une seule fonction. Cela peut être vrai, mais considérons quelques cas d'utilisation réalistes.

### Exemple concret : le formatage de l'argent

Je construisais une simple offre d'emploi pour développeurs. L'une des exigences était d'afficher les fourchettes de salaire à côté de chaque offre. Tous les salaires étaient stockés en cents et devaient ressembler à ceci :

```
from: 6000000 to:   60,000.00 USD
```

Cela semble facile, mais travailler avec du texte est difficile. Presque tous les développeurs détestent cela.

Nous passons tous des heures à écrire des expressions régulières et à gérer l'unicode. Lorsque je dois formater du texte, j'essaie toujours de chercher la solution sur Google. Après avoir éliminé toutes les bibliothèques (trop pour mes besoins) et tous les extraits de code qui ne sont pas bons, il ne reste pas grand-chose.

J'ai décidé de construire mon propre formateur.

#### **Comment le construire ?**

Avant de commencer à écrire du code, approfondissons une idée que j'ai trouvée :

1. Séparer les dollars et les cents.
2. Formater les dollars — ajouter des séparateurs de milliers n'est pas si facile.
3. Formater les cents — traiter les cents est facile, presque prêt à l'emploi.
4. Relier ensemble les dollars et les cents avec le séparateur.

Maintenant, cela semble clair. La dernière chose que nous devons considérer est comment ajouter des séparateurs de milliers aux dollars. Considérons l'algorithme suivant :

1. Inverser la chaîne.
2. Diviser la chaîne tous les 3 caractères en un tableau.
3. Joindre tous les éléments du tableau ensemble, en ajoutant le séparateur de milliers entre eux.
4. Inverser la chaîne.

Toutes ces étapes peuvent être traduites dans le pseudo-code suivant :

```
1. "60000"        => "00006"2. "00006"        => ["000", "06"]3. ["000", "06"]  => "000.06"4. "000.06"       => "60.000"
```

Et voici comment cet algorithme est traduit en fonctions composées :

Dans la première ligne, vous remarquerez que j'ai utilisé la bibliothèque [Lodash](https://lodash.com/docs/). Lodash contient de nombreuses utilités qui facilitent la programmation fonctionnelle. Analysons le code à partir de la ligne 22 :

```
return flow([  reverse,  splitCurry(match),  joinCurry(separator),  reverse]);
```

La fonction [flow](https://lodash.com/docs/4.17.4#flow) est un compositeur de fonctions. Elle transmet le résultat de la fonction _reverse_ à l'entrée de _splitCurry_, et ainsi de suite. Cela crée une fonction entièrement nouvelle. Vous vous souvenez de l'algorithme de séparation des milliers ci-dessus ? C'est ça !

Vous pouvez voir que j'ai suffixé les fonctions split et join avec « Curry » et que je les ai invoquées. Cette technique est appelée le currying.

#### Qu'est-ce que le Currying ?

Le [Currying](https://lodash.com/docs/4.17.4#curry) est le processus de traduction d'une fonction à plusieurs arguments en une fonction à un seul argument. La fonction à un seul argument retourne une autre fonction si des arguments sont encore nécessaires.

Cela semble difficile ? Considérons l'exemple suivant :

La fonction _split_ a besoin de deux arguments — une chaîne et un motif de séparation. La fonction doit savoir comment diviser le texte. Dans ce cas, nous ne pouvons pas composer cette fonction car elle a besoin d'arguments différents des autres. C'est là que le currying intervient.

```
import { curry } from "lodash";import split from "./split";
```

```
const splitCurry = curry(split);
```

```
splitCurry("000001")(/[0-9]{1,3}/g); // => ["000", "001"]
```

Maintenant, la fonction _splitCurry_ est cohérente avec la fonction _reverse_. Toutes deux ont besoin d'un argument. Malheureusement, nous n'avons pas encore invoqué la fonction _splitCurry_ avec un motif de séparation. Cela ne va pas fonctionner de cette manière.

Et si nous inversions l'ordre des arguments dans notre curry ?

```
import { curryRight } from "lodash";import split from "./split";
```

```
const splitCurry = curryRight(split);
```

```
splitCurry(/[0-9]{1,3}/g)("000001"); // => ["000", "001"]
```

Maintenant, notre code peut fonctionner car nous pouvons utiliser les curries comme des fonctions de fabrication. Regardons à nouveau le code :

```
return flow([  reverse,  splitCurry(match),  joinCurry(separator),  reverse]);
```

Toutes ces fonctions prennent un seul argument (chaîne), nous pouvons donc les composer ensemble. Et ensuite les utiliser comme une fonction autonome. Attendez une minute...

#### Que sont les fonctions de fabrication ?

Les fonctions de fabrication sont des fonctions qui créent un nouvel objet. Dans notre cas, une fonction. Considérons à nouveau notre séparateur de milliers. En théorie, nous pouvons utiliser la même fonction tout le temps. Malheureusement, certains pays séparent les milliers avec des virgules, d'autres avec des points. Bien sûr, j'aurais pu paramétrer le séparateur, mais j'ai décidé d'utiliser la fonction de fabrication.

```
const formatUS = thousandSeparator(',');const formatEU = thousandSeparator('.');
```

```
formatUS(10000); // 10,000formatEU(10000); // 10.000
```

### Résumé

L'année dernière, j'ai passé du temps à rafraîchir mes connaissances issues d'études précédentes afin de pouvoir les appliquer dans mon activité quotidienne. Dans cet article, je n'ai pas approfondi la loi des monades ou les monoïdes — je ne voulais pas rendre cela confus. Le sujet est vaste et profondément enraciné dans l'informatique. Je voulais vous donner une idée de la manière d'aborder la pensée fonctionnelle tout en décrivant tous les termes aussi brièvement que possible.

J'ai décidé de garder [**tout le code sur mon Github**](https://github.com/mateuszsokola/function-composition-typescript), afin que l'article soit plus facile à lire.

**Si vous avez des problèmes ou des suggestions, veuillez écrire un commentaire.**

—

PS. J'ai commencé [**une chaîne YouTube sur la programmation**](https://www.youtube.com/user/sookol18). Veuillez la consulter et vous abonner :)