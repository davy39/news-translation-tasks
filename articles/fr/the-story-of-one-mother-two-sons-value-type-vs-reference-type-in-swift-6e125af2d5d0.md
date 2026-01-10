---
title: 'L''histoire d''une mère et de deux fils : type valeur vs type référence en
  Swift'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-21T16:47:32.000Z'
originalURL: https://freecodecamp.org/news/the-story-of-one-mother-two-sons-value-type-vs-reference-type-in-swift-6e125af2d5d0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Ri49w8TcHeXrnmO5dD4_aQ.jpeg
tags:
- name: iOS
  slug: ios
- name: mobile
  slug: mobile
- name: General Programming
  slug: programming
- name: Swift
  slug: swift
- name: technology
  slug: technology
seo_title: 'L''histoire d''une mère et de deux fils : type valeur vs type référence
  en Swift'
seo_desc: 'By Boudhayan Biswas

  Swift is a mother?and it has two sons ?-


  Value Type ??‍♀️

  Reference Type ?‍♂️


  But what are their characteristics??‍♂️

  Do they behave the same or opposite to each other? ?‍♂️

  Swift is a multi-paradigm programming language develop...'
---

Par Boudhayan Biswas

Swift est une mère ? et elle a deux fils ?

* Type Valeur ??‍♀️
* Type Référence ?‍♂️

Mais quelles sont leurs caractéristiques ??‍♂️

Se comportent-ils de la même manière ou de manière opposée ? ?‍♂️

Swift est un langage de programmation multi-paradigme développé par Apple pour iOS, macOS, watchOS, tvOS, Linux et z/OS. ?

Tout comme les autres langages de programmation orientés objet, Swift utilise des classes comme blocs de construction qui peuvent définir des méthodes, des propriétés, des initialisateurs, et peuvent se conformer à des protocoles, supporter l'héritage et le polymorphisme. ?

Mais, attendez attendez attendez… ???

Swift a aussi des structs et ils peuvent définir des méthodes, des propriétés, des initialisateurs et peuvent se conformer à des protocoles avec une seule exception : l'héritage. ?

Quoi ? Maintenant je suis confus !!! ???

Maintenant, ajoutons à votre confusion : les structs ne sont pas les seuls types valeur en Swift. Les tuples et les énumérations sont aussi des types valeur. Les classes ne sont pas non plus les seuls types utilisés comme type référence. Les fonctions et les fermetures sont aussi des types référence. Mais pour nous soulager, nous savons au moins l'utilisation principale et la spécialisation de ces types. ?

Jusqu'à ce point, nous sommes laissés avec une grande confusion concernant l'utilisation des structs et des classes. ?

Alors, allons-y et clarifions les confusions qui tournent autour. ?‍♂️

### Emplacements de stockage

Il y a trois types de stockage disponibles :

* Registre ?
* Pile ⛅️
* Tas ?

Les objets qui ont une durée de vie plus courte sont stockés dans les registres ou la pile et ceux qui ont une durée de vie plus longue sont stockés dans le tas. ?

Un type valeur stocke son contenu dans la mémoire allouée dans la pile, donc nous pouvons dire que les types valeur sont alloués dans la pile en Swift. ?

Mais il y a une idée fausse courante sur les types valeur, l'avez-vous entendue ??‍♂️

L'idée fausse est que la plupart des gens pensent que les types valeur sont toujours stockés dans la pile.

❌❌ Attendez une minute — ce n'est pas toujours le cas. ❌❌

Les types valeur peuvent être stockés dans la pile lorsqu'ils sont des variables temporaires ou locales. Mais que se passe-t-il si un type valeur est contenu dans un type référence ?

Dans cette situation, il peut être stocké dans la mémoire du tas. ?

Wow… c'est cool !!! ?

Ainsi, les types valeur peuvent être stockés dans le registre, la pile ou le tas en fonction de leur durée de vie, qu'ils soient de courte ou de longue durée. Si c'est une variable locale, elle peut vivre dans la pile et si elle fait partie d'une classe, elle peut vivre dans la mémoire du tas. ✅

D'autre part, le type référence stocke son contenu dans la mémoire allouée dans la mémoire du tas et la variable ne contient qu'une référence à cet emplacement mémoire où les données réelles ont été stockées. ??

Comment cela fonctionne-t-il pour le type référence ??

Pour le type référence, il est assez courant que plusieurs variables contiennent la référence au même emplacement mémoire. ⚙️

Lorsque qu'une instance de type valeur est assignée à une variable ou passée à une fonction, l'instance est copiée et assignée à cette variable. Mais avec le type référence, seule la référence est copiée et la nouvelle variable contient la même référence au même emplacement mémoire. ?

### Différences en termes de mutabilité

Il peut y avoir deux états pour une variable :

* ?‍♀️ Mutable ?‍♀️
* ?‍♂️ Immutable ?‍♂️

Si une instance de type valeur est assignée à une variable immutable, alors l'instance devient également immutable. Par conséquent, nous ne pouvons pas apporter de modifications à cette instance. ?‍♂️

Si une instance de type valeur est assignée à une variable mutable, alors seulement elle rend l'instance mutable. ?‍♂️

Mais les choses sont totalement différentes pour les types référence. La variable et l'instance à laquelle elle est assignée sont totalement différentes. Si nous déclarons une variable immutable contenant une référence à une classe, cela signifie que la référence qu'elle contient ne changera jamais. Nous ne pouvons pas changer la référence et elle pointera toujours vers la même référence. ?

### Types structurels

Les valeurs des types structurels sont comparées pour l'égalité en termes de leurs attributs ou éléments. Nous pouvons dire qu'un type valeur est égal à un autre si et seulement si tous les attributs correspondants sont égaux. ???

Umm… trop de mots forts… que voulez-vous dire ???

Disons que nous avons un type valeur **_Personne_** qui a des attributs comme **_prénom_** et **_nom._**

```
struct Personne {
   var prenom: String
   var nom: String
}

var personne1 = Personne(prenom: "foo", nom: "bar")

var personne2 = Personne(prenom: "foo", nom: "bar")
```

Ici, les instances **_personne1_** et **_personne2_** contiennent la même valeur pour **_prénom_ ("foo")** et **_nom ("bar")_**. Donc, selon notre compréhension, nous pouvons dire que les deux instances sont égales l'une à l'autre puisque leurs attributs (**_prénom_** et **_nom_**) contiennent les mêmes valeurs.

Mais ce n'est pas seulement limité à cela : à l'avenir, deux instances de personne contenant les mêmes valeurs pour **_prénom_** et **_nom_** seront égales l'une à l'autre.

Donc, selon notre compréhension jusqu'à ce point, nous pouvons dire que :

> _**Les types valeur n'ont pas d'identité, donc il ne peut y avoir aucune référence à eux. Les types valeur sont sans visage. ?**_

Quoi ? Comment pouvez-vous dire cela ????

```
var monAge: Int = 21
var ageAmi: Int = 21
```

**_monAge_** et **_ageAmi_** sont des variables de type entier avec la valeur 21.

**_Pouvons-nous les distinguer l'une de l'autre ? ?_**

Non, car elles contiennent la même valeur. ?

Une variable entière avec la valeur 21 ne peut pas être différente d'une autre variable entière qui a également la valeur 21. C'est aussi simple que cela. ???

Le fait de ne pas avoir d'identité donne aux types valeur un autre avantage : si vous pensez de manière pratique, vous pouvez imaginer que si vous n'avez pas d'identité, alors n'importe qui avec les mêmes caractéristiques peut vous remplacer ou vous substituer. ???

Nous pouvons penser de la même manière pour nous en tant qu'êtres humains. Si je n'ai pas d'identité, alors n'importe qui avec les mêmes caractéristiques peut me remplacer ???. C'est bien pour nous que nous ayons une identité, sinon ce serait un grand risque pour notre existence. ?

Mais pour les types valeur, ils n'ont pas d'identité et c'est un avantage pour eux. ?

### Quels sont les avantages de l'utilisation des types valeur ?

#### ? Pas de conditions de course et d'interblocages : ?

Pour les types valeur dans un environnement multithread, il est impossible pour un thread de muter l'état de l'instance alors qu'elle est utilisée par un autre thread. Nous pouvons donc dire qu'il n'y aura pas de conditions de course ou d'interblocages.

#### ⚙️ **Pas de cycles de rétention : ⚙️**

Lorsque deux instances de type référence se contiennent mutuellement des références fortes et empêchent chacune d'être désallouée de la mémoire, on parle de cycle de rétention. Comme les types valeur ne fonctionnent pas comme une référence, nous pouvons dire qu'il n'y aura pas de cycles de rétention pour les types valeur.

#### ?‍?‍?‍? Comptage automatique des références : ?‍?‍?‍?

Pour le type référence, Swift utilise le comptage automatique des références pour suivre tous les objets vivants ou actifs et désalloue l'instance uniquement lorsqu'il n'y a plus de références fortes à celle-ci. Si nous réfléchissons un peu, nous pouvons dire que c'est une opération assez lourde car le runtime Swift doit toujours suivre les objets. Mais comme les types valeur sont alloués dans la pile, ils n'ont pas besoin de l'ARC. C'est donc moins coûteux et plus rapide ??.

Mais attendez... Comment gère-t-il la mémoire pour Array, Dictionary et String ??

Puisque nous ne pouvons pas savoir quelle sera la taille réelle d'un tableau, d'un dictionnaire et d'une chaîne à la compilation, il n'y a pas de possibilité pour eux d'être alloués à la compilation. Bien qu'ils soient des types valeur en interne, ils ne peuvent pas être alloués dans la pile. Ils doivent être alloués dans la mémoire du tas, et pour gérer cela, Swift utilise le **_copie à l'écriture_**. ?

Mais qu'est-ce que c'est ??

Lorsque nous disons qu'une instance est une copie d'une autre instance, cela signifie vraiment qu'elles sont les mêmes, qu'elles contiennent les mêmes valeurs. Mais en Swift, pour ces types (Array, Dictionary, String, etc.), une copie réelle a été faite sur le tas uniquement lorsqu'une instance est mutée. Cela s'appelle une technique d'optimisation des performances pour les types valeur. ???

### Conclusion

Il n'y a pas de règle stricte qui définit quand utiliser le type valeur et quand utiliser le type référence. Les types valeur ont certains avantages uniques par rapport aux types référence et vice versa. Ils sont tous les deux uniques à leur manière. Cela dépend vraiment de vos exigences et de ce que vous essayez d'accomplir. Vous devriez connaître la sémantique de votre code car vous connaissez votre code mieux que quiconque, donc c'est à vous de choisir. Vous avez la pleine liberté.

Alors, au lieu de vous battre sur le type valeur vs le type référence, utilisez-les intelligemment.

**_??? Santé !!! Merci d'avoir lu !!_** _???_

**_   Vous pouvez me trouver sur_** [**_Twitter_**](https://twitter.com/_boudhayan_)**_.   _**