---
title: Meilleure gestion des exceptions dans les flux Java 8 avec Vavr
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-07T18:42:01.000Z'
originalURL: https://freecodecamp.org/news/better-exception-handling-in-java-8-streams-using-vavr-6eda31285ce9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*NubsZjUhLLRtGA7SkIvtjQ.png
tags:
- name: Functional Programming
  slug: functional-programming
- name: Java
  slug: java
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Meilleure gestion des exceptions dans les flux Java 8 avec Vavr
seo_desc: 'By Rajasekar Elango

  In this post, I will provide tips for better exception handling in Java 8 streams
  using the Functional Java library Vavr.

  The problem

  To illustrate with an example, let’s say we want to print the day of the week for
  a given stream...'
---

Par Rajasekar Elango

Dans cet article, je vais fournir des conseils pour une meilleure gestion des exceptions dans les flux Java 8 en utilisant la bibliothèque Java fonctionnelle [Vavr](http://www.vavr.io/).

### Le problème

Pour illustrer avec un exemple, disons que nous voulons imprimer le jour de la semaine pour un flux donné de chaînes de dates au format `MM/dd/YYYY`.

### Solution initiale

Commençons par une solution initiale, comme montré ci-dessous, et améliorons-la itérativement.

Cela produira

_Huh_, si une chaîne de date est invalide, cela échoue au premier _DateTimeParseException_ sans continuer avec les dates valides.

### Java 8 Optional à la rescousse

Nous pouvons refactoriser `parseDate` pour retourner `Optional<LocalDate>` afin de le faire ignorer les invalides et continuer à traiter les dates valides.

Cela ignorera les erreurs et convertira toutes les dates valides.

```
WEDNESDAY Text '01-01-2015' could not be parsed at index 2 THURSDAY Text 'not a date' could not be parsed at index 0 FRIDAY
```

C'est une grande amélioration, mais l'exception doit être gérée dans la méthode `parseDate` et ne peut pas être renvoyée à la méthode principale pour la traiter. Nous ne pouvons pas faire en sorte que la méthode `parseDate` lance une exception vérifiée car l'API Streams ne fonctionne pas bien avec les méthodes qui lancent des exceptions.

### Une meilleure solution avec le Try Monad de Vavr

[Vavr](http://www.vavr.io/) est une bibliothèque fonctionnelle pour Java 8+. Nous allons utiliser l'objet `Try` de Vavr, qui peut être soit une instance de `Success` soit de `Failure`. Basiquement, [Try](http://www.javaslang.io/javaslang-docs/#_try) est un type de conteneur monadique qui représente un calcul qui peut soit entraîner une exception, soit retourner une valeur calculée avec succès. Voici le code modifié utilisant `Try` :

La sortie est

```
WEDNESDAY Failed due to Text '01-01-2015' could not be parsed at index 2 THURSDAYFailed due to Text 'not a date' could not be parsed at index 0 FRIDAY
```

Maintenant, l'exception est renvoyée à la méthode principale pour être traitée. Try dispose également d'API pour implémenter une logique de récupération ou retourner une valeur par défaut en cas d'erreur.

Pour démontrer cela, disons que nous voulons également prendre en charge `MM-dd-YYYY` comme format de chaîne alternatif pour les dates. L'exemple ci-dessous montre comment nous pouvons facilement implémenter une logique de récupération.

La sortie montre que maintenant la date `01-01-2015` est également convertie avec succès.

```
WEDNESDAY THURSDAY THURSDAY Failed due to Text 'not a date' could not be parsed at index 0 FRIDAY
```

Ainsi, le _Try Monad_ peut être utilisé pour gérer élégamment les exceptions et _échouer rapidement_ en cas d'erreurs.

**_Mise à jour le 12/03/2018 :_**

Les exemples de code ont été mis à jour pour utiliser [Doculet](https://doculet.net/).

_Publié à l'origine sur [http://erajasekar.com/posts/better-exception-handling-java8-streams-using-javaslang/](http://erajasekar.com/posts/better-exception-handling-java8-streams-using-javaslang/)._