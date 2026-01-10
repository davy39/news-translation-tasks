---
title: Tutoriel sur les Tables de Vérité de l'Algèbre Booléenne – XOR, NOR, et Symboles
  Logiques Expliqués
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-04T21:31:31.000Z'
originalURL: https://freecodecamp.org/news/boolean-algebra
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b45740569d1a4ca2aca.jpg
tags:
- name: Advanced Mathematics
  slug: advanced-mathematics
- name: Boolean
  slug: boolean
- name: Math
  slug: math
seo_title: Tutoriel sur les Tables de Vérité de l'Algèbre Booléenne – XOR, NOR, et
  Symboles Logiques Expliqués
seo_desc: "By Aditya\nWe all love computers. They can do so many amazing things. Within\
  \ a couple of decades computers have completely revolutionized almost all the aspects\
  \ of human life. \nThey can do tasks of varying degrees of sophistication, all by\
  \ just flippi..."
---

Par Aditya

Nous aimons tous les ordinateurs. Ils peuvent faire tant de choses incroyables. En quelques décennies, les ordinateurs ont complètement révolutionné presque tous les aspects de la vie humaine. 

Ils peuvent effectuer des tâches de degrés de sophistication variés, simplement en basculant des zéros et des uns. Il est remarquable de voir comment une action aussi simple peut conduire à tant de complexité.

Mais je suis sûr que vous savez tous que cette complexité ne peut pas être atteinte (pratiquement) simplement en basculant les nombres de manière aléatoire. Il y a effectivement une certaine logique derrière cela. Il existe des règles qui régissent la manière dont cela doit être fait. Dans cet article, nous allons discuter de ces règles et nous verrons comment elles régissent la manière dont les ordinateurs "pensent".

## Qu'est-ce que l'Algèbre Booléenne ?

Les règles que j'ai mentionnées ci-dessus sont décrites par un domaine des mathématiques appelé Algèbre Booléenne. 

Dans son livre de 1854, le mathématicien britannique George Boole a proposé un ensemble systématique de règles pour la manipulation des valeurs de vérité. Ces règles ont fourni une fondation mathématique pour traiter les propositions logiques. Ces ensembles de fondations ont conduit au développement de l'Algèbre Booléenne. 

Pour bien comprendre l'Algèbre Booléenne, nous devons d'abord comprendre les similitudes et les différences entre l'Algèbre Booléenne et les autres formes d'algèbre. 

L'algèbre, en général, traite de l'étude des symboles mathématiques et des opérations qui peuvent être effectuées sur ces symboles.

Ces symboles n'ont pas de signification propre. Ils représentent une autre quantité. C'est cette quantité qui donne une certaine valeur à ces symboles et c'est cette quantité sur laquelle les opérations sont réellement effectuées. 

L'Algèbre Booléenne traite également des symboles et des règles qui régissent les opérations sur ces symboles, mais la différence réside dans _ce que ces symboles représentent_. 

Dans le cas de l'algèbre ordinaire, les symboles représentent les nombres réels, tandis que dans l'Algèbre Booléenne, ils représentent les valeurs de vérité.

L'image ci-dessous montre l'ensemble complet des nombres réels. L'ensemble des nombres réels inclut les nombres naturels (1, 2, 3, 4....), les nombres entiers (tous les nombres naturels et 0), les entiers (.....-2, -1, 0, 1, 2, 3 ...) et ainsi de suite. L'algèbre ordinaire traite de cet ensemble complet de nombres. 

![Image](https://www.freecodecamp.org/news/content/images/2024/08/numbersys.png)

Les valeurs de vérité, en comparaison, consistent en un ensemble de seulement deux valeurs : Faux et Vrai. Ici, je voudrais souligner le fait que nous pouvons utiliser n'importe quel autre symbole pour représenter ces valeurs. 

Par exemple, en informatique, nous représentons principalement ces valeurs en utilisant 0 et 1. 0 est utilisé pour Faux et 1 pour Vrai. 

Vous pouvez également le faire de manière plus fantaisiste en représentant les valeurs de vérité avec d'autres symboles tels que Chats et Chiens ou Bananes et Oranges. 

Le point ici est que la signification interne de ces symboles restera la même, quel que soit le symbole que vous utilisez. Mais assurez-vous de ne pas changer les symboles lors de l'exécution des opérations. 

Maintenant, la question est que si (Vrai et Faux), (0 et 1) ne sont que des représentations, alors qu'est-ce qu'ils essaient de représenter ? 

La signification sous-jacente des valeurs de vérité provient du domaine de la logique où les valeurs de vérité sont utilisées pour dire si une proposition est "Vraie" ou "Fausse". Ici, les valeurs de vérité représentent la _relation d'une proposition à la vérité_, c'est-à-dire si la proposition est vraie ou fausse.

Une proposition est simplement une déclaration comme "Tous les chats sont mignons."

Si la proposition ci-dessus est vraie, alors nous lui attribuons la valeur de vérité "Vrai" ou "1", sinon nous lui attribuons "Faux" ou "0".

En électronique numérique, les valeurs de vérité sont utilisées pour représenter les états "Allumé" et "Éteint" des circuits électroniques. Nous en discuterons plus tard dans cet article. 

## Opérations Booléennes et Tables de Vérité

Tout comme l'Algèbre Ordinaire, l'Algèbre Booléenne possède également des opérations qui peuvent être appliquées aux valeurs pour obtenir des résultats. Bien que ces opérations ne soient pas similaires à celles de l'algèbre ordinaire, car, comme nous l'avons discuté précédemment, l'algèbre booléenne fonctionne sur des valeurs de vérité plutôt que sur des nombres réels.

### L'Algèbre Booléenne a trois opérations de base.

**OU** : Également connu sous le nom de _Disjonction_. Cette opération est effectuée sur deux variables booléennes. La sortie de l'opération OU sera 0 lorsque les deux opérandes sont 0, sinon elle sera 1. 

Pour avoir une image plus claire de ce que fait cette opération, nous pouvons la visualiser à l'aide d'une **Table de Vérité** ci-dessous.

```
Les tables de vérité nous donnent une représentation perspicace de ce que font les opérations booléennes et elles servent également d'outil pratique pour effectuer des opérations booléennes.

		Opération OU

Variable-1	Variable-2	Sortie
  0		0		0
  0		1		1
  1		0		1
  1		1		1
```

**ET** : Également connu sous le nom de _Conjonction_. Cette opération est effectuée sur deux variables booléennes. La sortie des opérations ET sera 1 lorsque les deux opérandes sont 1, sinon elle sera 0. La représentation de la table de vérité est la suivante.

```
		Opération ET

Variable-1	Variable-2	Sortie
  0		0		0
  0		1		0
  1		0		0
  1		1		1
```

**NON** : Également connu sous le nom de _Négation_. Cette opération est effectuée uniquement sur une variable. Si la valeur de la variable est 1, cette opération la convertit simplement en 0 et si la valeur de la variable est 0, elle la convertit en 1.

```
	Opération NON

Variable-1	Sortie
  0		1	
  1		0			
```

## Algèbre Booléenne et Circuits Numériques

Après son développement initial, l'Algèbre Booléenne, pendant très longtemps, est restée l'un de ces concepts en mathématiques qui n'avait aucune application pratique significative. 

Dans les années 1930, Claude Shannon, un mathématicien américain, a réalisé que l'Algèbre Booléenne pouvait être utilisée dans des circuits où les variables binaires pouvaient représenter les signaux de tension "bas" et "haut" ou les états "allumé" et "éteint".

Cette simple idée de fabriquer des circuits à l'aide de l'Algèbre Booléenne a conduit au développement de l'Électronique Numérique qui a grandement contribué au développement des circuits pour les ordinateurs. 

Les circuits numériques mettent en œuvre l'Algèbre Booléenne à l'aide de portes logiques. Les portes logiques sont les circuits qui représentent une opération booléenne. Par exemple, une porte OU représentera une opération OU. Il en va de même pour les portes NON et ET.

Outre les portes logiques de base, nous avons également des portes logiques qui peuvent être créées en combinant les portes logiques de base. 

**NAND** : La porte NAND est formée par une combinaison des portes NON et ET. La porte NAND donne une sortie de 0 si les deux entrées sont 1, sinon 1. 

La porte NAND possède la propriété de Complétude Fonctionnelle, ce qui signifie que toute fonction booléenne peut être implémentée simplement en utilisant une combinaison de portes NAND uniquement.

```
		Porte NAND

Variable-1	Variable-2	Sortie
  0		0		1
  0		1		1
  1		0		1
  1		1		0
```

**NOR** : La porte NOR est formée par une combinaison des portes NON et OU. La porte NOR donne une sortie de 1 si les deux entrées sont 0, sinon 0. 

La porte NOR, tout comme la porte NAND, possède la propriété de Complétude Fonctionnelle, ce qui signifie que toute fonction booléenne peut être implémentée simplement en utilisant une combinaison de portes NOR uniquement. 

```
		Porte NOR

Variable-1	Variable-2	Sortie
  0		0		1
  0		1		0
  1		0		0
  1		1		0
```

La plupart des circuits numériques sont construits en utilisant des portes NAND ou NOR en raison de leur propriété de complétude fonctionnelle et aussi parce qu'elles sont faciles à fabriquer. 

Outre les portes mentionnées ci-dessus, nous avons également certains types spéciaux de portes qui servent un but spécifique. Ce sont les suivantes :

**XOR** : La porte XOR ou porte OU-exclusif est un type spécial de porte logique qui donne 0 comme sortie si les deux entrées sont soit 0 soit 1, sinon elle donne 1. 

```
		Porte XOR

Variable-1	Variable-2	Sortie
  0		0		0
  0		1		1
  1		0		1
  1		1		0
```

**XNOR** : La porte XNOR ou porte NON-OU-exclusif est un type spécial de porte logique qui donne 1 comme sortie lorsque les deux entrées sont soit 0 soit 1, sinon elle donne 0.

```
		Porte XNOR

Variable-1	Variable-2	Sortie
  0		0		1
  0		1		0
  1		0		0
  1		1		1
```

## Conclusion

Ainsi, avec tout cela, nous pouvons maintenant conclure notre discussion sur l'Algèbre Booléenne ici. J'espère que maintenant vous avez une image décente de ce qu'est l'Algèbre Booléenne. 

Ce n'est définitivement pas tout ce que vous devez savoir sur l'Algèbre Booléenne. L'Algèbre Booléenne a beaucoup de concepts et de détails que nous n'avons pas pu discuter dans cet article.