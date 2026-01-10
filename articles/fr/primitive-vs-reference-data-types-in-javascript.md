---
title: Types de données primitifs vs types de données par référence en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-18T19:24:33.000Z'
originalURL: https://freecodecamp.org/news/primitive-vs-reference-data-types-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/Purple-Minimal-We-Are-Hiring-Twitter-Post-1.gif
tags:
- name: JavaScript
  slug: javascript
seo_title: Types de données primitifs vs types de données par référence en JavaScript
seo_desc: "By Njong Emy\nData types can be a bit of a mind boggling concept. But as\
  \ programmers, we use data types everyday – so they're something we should understand.\
  \ \nQuestion is, how does the computer store these data types? It can't possibly\
  \ treat every dat..."
---

Par Njong Emy

Les types de données peuvent être un concept un peu déroutant. Mais en tant que programmeurs, nous utilisons des types de données tous les jours – il est donc important de les comprendre. 

La question est, comment l'ordinateur stocke-t-il ces types de données ? Il ne peut pas traiter tous les types de données de la même manière.

En JavaScript, les types de données sont divisés en deux catégories, et l'ordinateur traite chacune différemment. Nous avons les types de données primitifs et les types de données par référence. Mais qu'est-ce que c'est ? Et pourquoi est-il important de connaître la différence ? C'est ce que nous allons apprendre dans cet article.

# Types de données primitifs en JavaScript

Ces types de données sont assez simples et sont parfois considérés comme le niveau le plus bas de l'implémentation d'un langage de programmation. Ils ne sont pas des objets et n'ont pas de méthodes. 

Des exemples de tels types de données sont les nombres, les chaînes de caractères, les booléens, null et undefined. 

![Types de données primitifs](https://www.freecodecamp.org/news/content/images/2022/01/Purple-Minimal-We-Are-Hiring-Twitter-Post--1-.png)

Mais vous pourriez vous demander à propos des chaînes de caractères, car elles ont des méthodes. En fait, JavaScript convertit les chaînes de caractères primitives en objets chaîne de caractères, afin qu'il soit possible d'utiliser les méthodes des objets chaîne de caractères.

# Comment les types de données primitifs sont-ils traités en JavaScript ?

Lorsque vous déclarez un type de données primitif en JavaScript, il est stocké dans une pile. Une pile est une structure de données simple que l'ordinateur utilise pour stocker et récupérer des données rapidement. 

Un type de données primitif dans la pile est identifié par le nom de variable que vous avez utilisé pour la déclaration dans votre programme. Avec chaque type de données primitif que vous créez, des données sont ajoutées à la pile. 

Pour illustrer cela, disons que nous déclarons une variable, `numOne`, et lui donnons une valeur de 50. Nous créons ensuite une autre variable, `numTwo`, et lui attribuons la même valeur de 50. Ainsi, les deux variables ont la même valeur. 

Ce qui se passe dans la pile, c'est que l'ordinateur crée de l'espace pour `numOne` et stocke sa valeur assignée dans la pile. Lorsque `numTwo` est créé, l'ordinateur crée à nouveau de l'espace et stocke 50 dans la pile. Peu importe que les deux variables se voient attribuer la même valeur.

![Stocker des données dans la pile](https://www.freecodecamp.org/news/content/images/2022/01/Purple-Minimal-We-Are-Hiring-Twitter-Post--3-.png)

Et si, pendant le processus de codage, nous décidions de mettre à jour la valeur de `numOne` à, disons, 100 ? Est-ce que cela signifie que `numTwo` changera aussi ? La réponse est non. 

Puisque `numOne` et `numTwo` étaient stockés différemment dans la pile, la mise à jour de l'un d'eux n'affectera pas l'autre. Et nous pouvons expérimenter cela en l'essayant réellement dans notre éditeur de code. 

Enregistrer `numOne` dans la console affichera 100, et enregistrer `numTwo` affichera 50. Ainsi, en effet, les deux variables n'ont aucun lien entre elles.

```javascript
let numOne = 50;
let numTwo = numOne; //numTwo=numOne=50
numOne = 100;
console.log(numOne); //affiche 100
console.log(numTwo); //affiche 50
```

![Pile mise à jour](https://www.freecodecamp.org/news/content/images/2022/01/Purple-Minimal-We-Are-Hiring-Twitter-Post--4-.png)

Maintenant que nous avons vu à quel point il est facile de manipuler les types de données primitifs, voyons comment les types de données par référence fonctionnent de manière similaire.

# Types de données par référence en JavaScript

Les types de données par référence, contrairement aux types de données primitifs, sont dynamiques par nature. C'est-à-dire qu'ils n'ont pas une taille fixe. 

La plupart d'entre eux sont considérés comme des objets et ont donc des méthodes. Des exemples de tels types de données incluent les tableaux, les fonctions, les collections et tous les autres types d'objets.

![Types de données par référence](https://www.freecodecamp.org/news/content/images/2022/01/Purple-Minimal-We-Are-Hiring-Twitter-Post--2-.png)

# Quelle est la différence entre les types de données primitifs et les types de données par référence ?

La différence apparaît lorsque l'ordinateur doit stocker un type de données par référence. Lorsque vous créez une variable et lui attribuez une valeur qui est un type de données par référence, l'ordinateur ne stocke pas directement ce type de données dans cette variable (comme c'est le cas avec les types primitifs). 

Ce que vous avez attribué à cette variable est un pointeur qui pointe vers l'emplacement de ce type de données en mémoire. Confus ? Je sais.

![Types de données par référence](https://www.freecodecamp.org/news/content/images/2022/01/Purple-Minimal-We-Are-Hiring-Twitter-Post--5-.png)

Comme vous pouvez le voir sur l'image ci-dessus, nous avons maintenant deux structures de données. Une pile et un tas. Supposons que nous avons déclaré un objet, par exemple. L'objet lui-même est stocké dans un tas, et son pointeur est stocké dans une pile. Le pointeur est identifié par le nom de variable de l'objet et pointe vers cet objet.

Maintenant, nous pourrions créer une variable, `object1`, et lui attribuer un objet. Et si, comme avant, nous créons une autre variable `object2`, et lui attribuons `object1`. Est-ce que cela signifie qu'un autre objet sera créé dans le tas ? La réponse est non. 

Puisque l'objet existe déjà dans le tas, `object2` et `object1` pointeront tous deux vers le même objet.

Une autre différence apparaît lorsque nous mettons à jour `object1`. Si nous enregistrons les deux variables dans la console, nous voyons que le changement les a affectées toutes les deux. Cela est dû au fait qu'elles pointent toutes les deux vers le même objet dans le tas – et la mise à jour d'une variable affecte bien sûr l'autre.

```javascript
let object1 = {
name:'Bingeh',
age:18
};
let object2 = object1;

//mise à jour de object1,
object1.age = 20;

console.log(object2); //nous voyons que object2 met également à jour l'attribut age
```

![Mise à jour dans le tas](https://www.freecodecamp.org/news/content/images/2022/01/Purple-Minimal-We-Are-Hiring-Twitter-Post--6-.png)

# Conclusion

Maintenant, vous connaissez la différence entre les types de données primitifs et les types de données par référence. Il est important de connaître ces différences – surtout lorsque vous obtenez des erreurs comme 'null pointer reference' – afin de pouvoir comprendre pourquoi elles se produisent. 

Cela arrive parfois aux développeurs Java, donc j'espère que cet article vous aide à clarifier tout doute.