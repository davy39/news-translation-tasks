---
title: Qu'est-ce qu'un problème d'arithmétique à virgule flottante ?
subtitle: ''
author: Syeda Maham Fahim
co_authors: []
series: null
date: '2024-10-24T14:19:22.582Z'
originalURL: https://freecodecamp.org/news/what-is-a-floating-point-arithmetic-problem
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1729588035734/9824633d-727a-49ce-9080-0fa3a7b18ed6.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Maths
  slug: maths
- name: Mathematics
  slug: mathematics
- name: float
  slug: float
seo_title: Qu'est-ce qu'un problème d'arithmétique à virgule flottante ?
seo_desc: 'Have you ever worked with numbers like 1/3, where the result is 0.33333…
  and continues forever? As humans, we naturally round off such numbers, but have
  you ever wondered how computers handle them?

  In this article, you’ll explore how computers manage...'
---

Avez-vous déjà travaillé avec des nombres comme 1/3, où le résultat est 0,33333… et continue à l'infini ? En tant qu'êtres humains, nous arrondissons naturellement de tels nombres, mais vous êtes-vous déjà demandé comment les ordinateurs les gèrent ?

Dans cet article, vous explorerez comment les ordinateurs gèrent les valeurs continues, y compris le concept d'erreurs de précision. Nous examinerons le problème d'arithmétique à virgule flottante, un problème universel qui affecte de nombreux langages de programmation. Nous nous concentrerons spécifiquement sur la manière dont JavaScript aborde ce défi.

De plus, vous apprendrez comment les opérations binaires fonctionnent en coulisses, le seuil auquel JavaScript tronque les nombres selon la norme IEEE 754, et nous présenterons `BigInt` comme une solution pour gérer avec précision des nombres plus grands sans perte de précision.

Commençons par un exemple. Pouvez-vous deviner le résultat de cette opération ?

```javascript
console.log(0.1 + 0.2);
```

Vous pensez peut-être que la réponse est 0,3, n'est-ce pas ? Mais non, la sortie réelle est :

```javascript
Output: 0.30000000000000004
```

Vous devez vous demander pourquoi cela se produit. Pourquoi tant de zéros supplémentaires, et pourquoi se termine-t-il par un 4 ?

La réponse est simple : les nombres 0,1 et 0,2 ne peuvent pas être représentés avec précision en JavaScript (c'est-à-dire "exactement" ou "avec précision").

Cela semble simple, n'est-ce pas ? Mais l'explication est un peu plus complexe.

Alors, selon vous, est-ce un bug ou une fonctionnalité ?

Eh bien, ce n'est pas un bug. C'est en fait un problème fondamental lié à la manière dont les ordinateurs gèrent les nombres, spécifiquement les nombres à virgule flottante.

## Pourquoi cela se produit-il ?

Comprenons cela avec des mathématiques de base.

La fraction 1/3 est représentée en décimal par 0,33333... et elle ne se termine jamais. Cela signifie que 3 se répète à l'infini. Nous ne pouvons pas l'écrire exactement, alors nous l'approximons à quelque chose comme 0,333 ou 0,333333 pour gagner du temps et de l'espace.

De même, dans un ordinateur, nous devons également approximer car 1/3 ou 0,3333... serait un nombre très grand et prendrait un espace infini (que nous n'avons pas).

Cela conduit à ce que nous appelons le problème d'arithmétique à virgule flottante.

## Problème d'arithmétique à virgule flottante

En termes simples, les nombres à virgule flottante sont des nombres qui ne peuvent pas être écrits exactement, alors nous les approximons. Dans un ordinateur, ce type d'approximation peut entraîner de petites erreurs de précision, que nous appelons le problème d'arithmétique à virgule flottante.

## Explication binaire

Maintenant que nous avons couvert l'explication simple, comprenons également cela en termes binaires. JavaScript gère tout en binaire en coulisses.

Le binaire est un système de numération qui n'utilise que deux chiffres : 0 et 1.

### Pourquoi 0,1 et 0,2 ne peuvent-ils pas être représentés exactement en binaire ?

Le problème central est que tous les nombres décimaux ne peuvent pas être parfaitement représentés comme des fractions binaires.

Prenons 0,1 comme exemple :

Lorsque vous essayez de représenter 0,1 en binaire, vous découvrirez qu'il ne peut pas être exprimé comme une fraction binaire finie. Au lieu de cela, il devient une fraction répétitive, un peu comme 1/3 en décimal devient 0,333..., se répétant à l'infini.

En binaire, 0,1 devient :

```plaintext
0.0001100110011001100110011001100110011... (se répétant à l'infini)
```

Puisque les ordinateurs ont une mémoire limitée, ils ne peuvent pas stocker cette séquence infinie exactement. Au lieu de cela, ils doivent couper le nombre à un certain point, ce qui introduit une petite erreur d'arrondi. C'est pourquoi 0,1 en binaire n'est qu'une approximation de la valeur réelle.

Comme 0,1, 0,2 ne peut pas être exactement représenté en binaire. Il devient :

```plaintext
0.00110011001100110011001100110011... (se répétant à l'infini)
```

Encore une fois, l'ordinateur tronque (couper une partie d'un nombre pour s'adapter à une limite ou supprimer des chiffres supplémentaires) cette séquence binaire infinie, ce qui conduit à une petite erreur de représentation.

Alors, que se passe-t-il lorsque nous additionnons 0,1 + 0,2 ? Lorsque vous additionnez 0,1 + 0,2 en JavaScript, les approximations binaires pour 0,1 et 0,2 sont additionnées ensemble. Mais puisque les deux valeurs ne sont que des approximations, le résultat est également une approximation.

Au lieu d'obtenir exactement 0,3, vous obtenez quelque chose de proche de ceci :

```javascript
console.log(0.1 + 0.2); // Output: 0.30000000000000004
```

Cette légère erreur se produit parce que ni 0,1 ni 0,2 ne peuvent être représentés exactement en binaire, donc le résultat final a une petite erreur d'arrondi.

## Comment JavaScript tronque-t-il le nombre ?

Maintenant, la question se pose : comment JavaScript sait-il quand tronquer la valeur ?

**( La troncation signifie couper ou raccourcir un nombre en supprimant des chiffres supplémentaires au-delà d'un certain point. **)**

Il existe une limite maximale et minimale pour cela.

Pour gérer cela dans le monde informatique, nous avons une norme qui définit comment les nombres à virgule flottante sont stockés et calculés.

## Norme IEEE 754

JavaScript utilise la norme IEEE 754 pour gérer l'arithmétique à virgule flottante.

La norme définit les limites d'entiers sûrs pour le type `Number` en JavaScript sans perte de précision :

* **Entier sûr maximum :** 2^53 - 1 ou 9007199254740991

* **Entier sûr minimum :** -(2^53 - 1) ou -9007199254740991

Au-delà de ces limites, JavaScript ne peut pas représenter avec précision les entiers en raison du fonctionnement de l'arithmétique à virgule flottante.

Pour cette raison, JavaScript fournit deux constantes pour représenter ces limites :

* `Number.MAX_SAFE_INTEGER`

* `Number.MIN_SAFE_INTEGER`

### Que faire si j'ai besoin d'un nombre plus grand ?

Si vous devez travailler avec des nombres plus grands que l'entier sûr maximum (comme ceux utilisés en cryptographie ou en finance), JavaScript a une solution : BigInt.

### Présentation de BigInt

`BigInt` est un objet intégré qui vous permet de travailler avec des nombres entiers au-delà de la limite d'entiers sûrs. Il vous permet de représenter des nombres plus grands que 9007199254740991, donc vous n'avez pas à vous soucier des erreurs de précision ici !

Pour utiliser `BigInt`, il suffit d'ajouter un `n` à la fin d'un littéral entier :

```javascript
const bigNumber = 1234567890123456789012345678901234567890n;
```

Alternativement, vous pouvez utiliser le constructeur `BigInt` :

```javascript
const bigNumber = BigInt("1234567890123456789012345678901234567890");
```

#### Opérations avec BigInt

Vous pouvez effectuer des opérations arithmétiques avec `BigInt`, comme l'addition, la soustraction, la multiplication et même l'exponentiation. Cependant, il y a un piège : vous ne pouvez pas mélanger `BigInt` avec des types `Number` réguliers dans des opérations arithmétiques sans conversion explicite entre eux.

Par exemple, cela ne fonctionnera pas :

```javascript
let result = bigNumber + 5; // Erreur : impossible de mélanger BigInt et d'autres types
```

Vous devriez d'abord convertir le `Number` en `BigInt` :

```javascript
let result = bigNumber + BigInt(5); // Maintenant, cela fonctionne !
```

### Où utilisons-nous BigInt ?

`BigInt` est particulièrement utile dans les domaines nécessitant de la précision, tels que :

* Algorithmes cryptographiques

* Gestion de grands ensembles de données

* Calculs financiers nécessitant une exactitude

### En résumé

* La limite d'entiers sûrs en JavaScript garantit une représentation exacte des nombres pour les entiers entre -(2^53 - 1) et 2^53 - 1.

* Les erreurs de précision se produisent en raison de l'arithmétique à virgule flottante lors de la manipulation de certains nombres (comme 0,1 + 0,2).

* Si vous avez besoin de nombres plus grands que la limite sûre, `BigInt` est votre ami. Mais n'oubliez pas, le mélange de `BigInt` et de types `Number` nécessite des conversions explicites.