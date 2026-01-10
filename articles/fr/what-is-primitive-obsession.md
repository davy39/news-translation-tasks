---
title: Qu'est-ce que l'Obsession des Primitifs ?
subtitle: ''
author: Daniel Asaboro
co_authors: []
series: null
date: '2024-07-23T22:03:40.000Z'
originalURL: https://freecodecamp.org/news/what-is-primitive-obsession
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-23-at-08.25.18.png
tags:
- name: clean code
  slug: clean-code
- name: software development
  slug: software-development
seo_title: Qu'est-ce que l'Obsession des Primitifs ?
seo_desc: 'In a statically-typed language like Java, C#, Go, Typescript, or even Dart,
  how do you represent an email address? Okay, what about a password? A phone number?
  Zip code? Home address? Alright, what about a unique ID?

  If your answer to all or most of ...'
---

Dans un langage à typage statique comme Java, C#, Go, Typescript, ou même Dart, comment représentez-vous une adresse e-mail ? D'accord, et un mot de passe ? Un numéro de téléphone ? Un code postal ? Une adresse postale ? Très bien, et un identifiant unique ?

Si votre réponse à toutes ou à la plupart de ces questions est une chaîne de caractères, alors vous souffrez de ce que les experts en développement logiciel appellent "**l'Obsession des Primitifs**".

Bien que les types primitifs comme `int`, `char`, `byte`, `short`, `long`, `float`, `double`, `boolean`, `string`, etc., soient les blocs de construction de base intégrés de tout langage de programmation, l'Obsession des Primitifs se produit lorsque votre code dépend trop d'eux pour représenter des concepts autrement plus complexes.

Les experts disent que c'est une mauvaise odeur de code. Cela est dû au fait que l'Obsession des Primitifs peut entraîner une série de problèmes, notamment un manque de validation, une mauvaise lisibilité, une duplication de code et des difficultés de refactorisation. Cet article vous aidera à résoudre ce problème.

## Ce que vous apprendrez dans cet article

Ce tutoriel, bien que assez court, est conçu pour vous aider à comprendre et à résoudre le problème de l'obsession des primitifs dans votre code. Ainsi, lorsque vous aurez terminé votre lecture, vous devriez être capable de :

1. Identifier ce qui est si mauvais dans l'Obsession des Primitifs et les inconvénients associés.
   
2. Concevoir de meilleurs logiciels et implémenter des structures de données qui améliorent la correction du code, la maintenabilité et la pérennité de votre logiciel contre les problèmes potentiels.
   
3. Améliorer la sécurité des données et réduire la probabilité d'erreurs d'exécution et de comportements inattendus en utilisant des représentations de données plus robustes.

## Prérequis : Ce que vous devez savoir

1. La familiarité avec les principes de la POO comme les classes, les objets, l'encapsulation, l'héritage et le polymorphisme sera bénéfique lors de la conception de structures de données personnalisées.
   
2. La maîtrise des langages à typage statique comme Java, C#, Go, TypeScript et Dart où les types de variables sont déclarés au moment de la compilation.

Ce n'est pas grave si vous n'êtes pas familier avec ces concepts – il existe de nombreuses ressources disponibles en ligne et dans les manuels pour vous aider à commencer. Mais ce tutoriel suppose une compréhension de base de ces fondements et s'appuie sur eux pour aborder le problème de l'obsession des primitifs.

## Qu'est-ce qui est mauvais dans l'Obsession des Primitifs ?

L'obsession des primitifs est problématique pour plusieurs raisons :

1. Vérification de type faible
   
2. Fonctionnalités intégrées limitées pour des types de données spécifiques
   
3. Maintenabilité réduite et perte de connaissances du domaine

Examinons chaque problème en détail :

### 1. Les primitifs offrent une vérification de type faible

Au-delà de l'allocation efficace de la mémoire, ou du temps de calcul gaspillé à déchiffrer quel type est une valeur, l'un des avantages des langages à typage statique est qu'ils permettent au compilateur de vous aider à attraper les incompatibilités de type potentielles au moment de la compilation. Cela peut aider à prévenir les erreurs d'exécution causées par l'utilisation du mauvais type de données.

Le compilateur vous crierait dessus si vous faisiez ceci :

```dart
String phoneNumber = "+1-555-229-1234";
int zipCode = 101257;

zipCode = phoneNumber; // lance une erreur
```

Et si vous faisiez ceci ?

```dart
String phoneNumber = "+1-555-229-1234";
String zipCode = "1000 AP"

zipCode = phoneNumber; // fonctionne bien
```

Cela va compiler et ne rien faire !

Pourquoi ?

**Parce qu'une chaîne de caractères sera toujours une chaîne de caractères.**

Le compilateur ne peut pas différencier si la valeur de la chaîne que vous passez représente un mot de passe utilisateur ou une adresse e-mail. Par conséquent, il ne peut pas vous empêcher d'assigner par erreur une variable au mauvais champ, ce qui conduit à des erreurs d'exécution et à des comportements inattendus.

### 2. Fonctionnalités intégrées limitées pour des types de données spécifiques.

Lorsque vous dépendez fortement des primitifs, vous devez souvent écrire du code supplémentaire pour effectuer des tâches telles que la validation d'adresse e-mail ou la mise en forme de numéro de téléphone. Et ce n'est pas vraiment un problème.

Le vrai problème est la nature répétitive et dispersée de ces implémentations. Cela n'augmente pas seulement le risque d'erreurs, mais cela rend également le code plus difficile à maintenir et à refactoriser.

### 3. Maintenabilité réduite et perte de connaissances du domaine

La dispersion des règles et de la logique métier dans la base de code rend plus difficile la maintenance et l'évolution du logiciel. Lorsque les primitifs sont utilisés de manière extensive, il peut être difficile de comprendre le but et les contraintes des données qu'ils représentent.

L'encapsulation de cette logique dans des types dédiés aide à préserver les connaissances du domaine et rend le code plus intuitif pour les développeurs futurs.

Par exemple, vous pourriez avoir besoin de bloquer certaines adresses e-mail en raison de fraudes ou de restreindre des codes postaux, des zones ou des entreprises spécifiques. Lorsque vous utilisez des primitifs, ce contexte important n'est pas évident, ce qui conduit à des erreurs potentielles et à une charge de maintenance accrue.

## Comment se libérer de l'Obsession des Primitifs

### 1. Méfiez-vous des variables avec une logique de validation spéciale.

Prenons les numéros de téléphone, par exemple. Au Nigeria, d'où je viens, tous les numéros de téléphone ont onze chiffres et commencent par un zéro. Le deuxième chiffre est généralement un "*7*", "*8*", ou "9" qui aide à identifier l'opérateur de télécommunications. Tout autre numéro est invalide.

Il en va de même pour une URL de site web. Elle pourrait très bien être représentée par une chaîne de caractères. Mais une URL contient plus d'informations et des propriétés spécifiques par rapport à une chaîne de caractères (par exemple, le schéma, les paramètres de requête et le protocole). Et chaque partie a une méthode de validation différente.

### 2. Méfiez-vous des variables avec des règles de comparaison spéciales

Au-delà des simples vérifications d'égalité (==), si vous vous retrouvez à implémenter une logique de comparaison personnalisée pour une variable sans l'encapsuler dans une classe, c'est un signal d'alarme.

Par exemple, la comparaison des adresses e-mail implique souvent plus qu'une simple vérification d'égalité. Vous pourriez avoir besoin d'effectuer une correspondance insensible à la casse, de supprimer les espaces blancs ou de gérer les variations de formatage pour identifier avec précision les e-mails correspondants, comme le signe + dans les adresses e-mail pour les personnes qui veulent tromper votre système.

daniel@example.com est la même adresse e-mail que daniel+dev@example.com. Les e-mails envoyés à cette dernière seront reçus sur la première.

### 3. Méfiez-vous des variables avec des règles de formatage spéciales

Toute variable qui nécessite un formatage ou un analyse spécifique pour extraire des informations significatives est un candidat pour une représentation plus riche.

Les **valeurs de devise** en sont un bon exemple. Différentes régions utilisent différentes règles de formatage – certaines utilisent des virgules et d'autres des points décimaux. Il en va de même pour une date de naissance ou tout ce qui nécessite des données.

L'identification et la résolution de l'obsession des primitifs est un processus continu.

Vous ne pourrez pas attraper toutes les instances en une seule fois, surtout celles qui sont peu communes et uniques à votre domaine métier. C'est parfaitement normal – c'est ainsi que cela devrait être.

Au lieu de paniquer ou d'abandonner, refactorisez progressivement votre code pour incorporer ces changements. Cette approche est la clé pour rendre votre code pérenne et maintenable.

## Vous ne le voyez pas jusqu'à ce qu'on vous le montre

L'obsession des primitifs se cache en pleine vue. Et c'est un problème significatif car, contrairement aux erreurs statiques, les linters ne les signaleront pas et votre programme ne plantera pas à cause d'eux.

Il faut souvent un mentor, une revue de code, ou un moment "aha" pour réaliser que ces vérifications et règles répétitives dispersées dans votre base de code peuvent être centralisées dans leurs propres types dédiés. Cette reconnaissance est la première étape vers un code plus robuste, lisible et maintenable.

Alors restez ouvert d'esprit, engagez-vous avec les autres, lisez du code de différentes sources et contribuez à des projets open-source. C'est ainsi que vous apprenez. En fin de compte, tout est une question d'encapsulation – regrouper les données et les méthodes qui opèrent sur elles en un seul endroit pour la maintenabilité.

## Crédits et ressources :

1. [A Code Smell that Hurts People the Most](https://medium.com/the-sixt-india-blog/primitive-obsession-code-smell-that-hurt-people-the-most-5cbdd70496e9) par Arpit Jain.
   
2. [Signs and Symptoms of Primitive Obsession](https://refactoring.guru/smells/primitive-obsession) par Refactoring Guru.
   
3. [How to Fix Primitive Obsession](https://hackernoon.com/what-is-primitive-obsession-and-how-can-we-fix-it-wh2f33ki) par Sam Walpole sur Hackernoon.