---
title: Comment se débarrasser de NullPointerException
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-25T14:38:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-rid-of-nullpointerexception-3cdf9199f9fb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Gq_k-Dj-b2hkTN_-kw5RaQ.png
tags:
- name: clean code
  slug: clean-code
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment se débarrasser de NullPointerException
seo_desc: 'By shani fedida

  OverOps, an Israeli company which helps developers understand what happens in production,
  carried out research on what the top Java exceptions were in production. Want to
  guess which one is in #1 place? NullPointerException.


  NullPoin...'
---

Par shani fedida

OverOps, une entreprise israélienne qui aide les développeurs à comprendre ce qui se passe en production, a mené une [recherche](https://blog.takipi.com/the-top-10-exceptions-types-in-production-java-applications-based-on-1b-events/) sur les principales exceptions Java en production. Devinez laquelle est en première place ? `NullPointerException`.

![Image](https://cdn-media-1.freecodecamp.org/images/0*Qhtt3vCy6mUF-z2X.png)
_NullPointerException, le monstre d'OverOps_

Pourquoi cette exception est-elle si fréquente ? Je soutiens (comme le fait Uncle Bob ?) que ce n'est **pas** parce que les développeurs oublient d'ajouter des vérifications de null.

La raison : **les développeurs utilisent trop souvent les nulls.**

### **D'où viennent tous ces NULL ?**

En C# et Java, tous les types de référence peuvent pointer vers `null`. Nous pouvons obtenir une référence pointant vers `null` de plusieurs manières :

* Variables de type référence "non initialisées" — variables initialisées avec des nulls et qui reçoivent leur valeur réelle par la suite. Un bug peut empêcher leur réaffectation.
* Membres de classe de type référence non initialisés.
* Affectation explicite à `null` ou retour de `null` depuis une fonction

Voici quelques schémas que j'ai remarqués dans les fonctions retournant `null` :

#### Gestion des erreurs

Retourner `null` lorsque l'entrée est invalide. C'est une façon de retourner des codes d'erreur. Je pense que c'est un style de programmation ancien, datant de l'époque où les exceptions n'existaient pas.

#### Données optionnelles manquantes pour les entités

Une propriété d'une entité peut être optionnelle. Lorsqu'il n'y a pas de données pour une propriété optionnelle, elle retourne `null`.

#### Modèles hiérarchiques

Dans les modèles hiérarchiques, nous pouvons généralement naviguer vers le haut et vers le bas. Lorsque nous sommes au sommet, nous devons avoir un moyen de l'indiquer, généralement en retournant `null`.

#### Fonctions de recherche

Lorsque nous voulons trouver une entité par critères dans une collection, nous retournons `null` pour indiquer que l'entité n'a pas été trouvée.

### Quels sont les problèmes liés à l'utilisation des nulls ?

#### Cela va exploser. Finalement...

Le code dans lequel l'exception `NullPointerException` est levée peut être très éloigné de l'endroit où se trouve le bug. **Cela rend le traçage du problème réel plus difficile.** Surtout si le code est ramifié.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2ULzFy6tmPqxYQKpuwWc3A.png)
_Je suis heureux maintenant mais je vais exploser finalement._

Dans l'exemple de code suivant, il y a un bug, quelque part dans la classe A, qui fait que `entity` est null. Mais l'exception `NullPointerException` est levée à l'intérieur d'une fonction de la classe B. Le code réel peut être beaucoup plus compliqué.

#### Erreurs cachées

Je rencontre des vérifications de `null` qui semblent indiquer que le développeur pensait :

* "Je sais que je devrais vérifier `null` mais je ne sais pas ce que cela signifie lorsque la fonction retourne `null` et je ne sais pas quoi en faire," ou
* "Je pense que cela ne peut pas être null mais juste pour être sûr, je ne veux pas que cela fasse exploser la production"

Cela ressemble généralement à ceci :

Ces types de vérifications de `null` font que certaines logiques de code ne se déclenchent pas, **sans la possibilité de le savoir**. Écrire ce type de code signifie qu'une partie de la logique d'un flux a échoué mais que le flux entier a réussi. Cela peut également causer un bug dans une autre fonctionnalité qui supposait que l'autre fonction avait fait son travail.

Imaginez que vous achetez un billet pour un spectacle en ligne. Vous avez reçu un message de succès ! Le jour du spectacle est enfin arrivé, vous quittez le travail plus tôt, organisez une babysitter et allez voir le spectacle. À votre arrivée, vous découvrez que vous n'avez pas de billets ! et qu'il n'y a pas de places vides. Vous rentrez chez vous, contrarié et confus ?. **Pouvez-vous voir comment ce type de vérification de null peut causer cette situation ?**

Cela rend également le code ramifié et laid ?

### Types de référence non nullables manquants en C# et Java

En C# et Java, **les types de référence peuvent toujours pointer vers `null`**. Cela conduit à une situation où nous ne pouvons pas savoir, en regardant la signature d'une fonction, si `null` est une entrée ou une sortie valide. Je crois que la plupart des fonctions ne retournent pas ou n'acceptent pas `null`.

Parce qu'il est difficile de savoir si une fonction retourne `null` ou non (sauf si documenté), les développeurs insèrent soit des vérifications de `null` lorsqu'elles ne sont pas nécessaires, soit ne vérifient pas les `nulls` lorsqu'elles sont nécessaires — et oui, parfois mettent des vérifications de null lorsqu'elles sont nécessaires ?.

Ce mauvais choix de conception cause les problèmes que j'ai décrits précédemment dans "Erreurs cachées" et beaucoup d'erreurs `NullPointerException`, bien sûr. Situation perdant-perdant. ?

Il existe des langages comme [Kotlin](https://kotlinlang.org/docs/reference/null-safety.html) qui visent à éliminer les erreurs `NullPointerException` en différenciant les références nullables et non nullables. Cela permet de détecter les `null` assignés à des références non-`null`, et de s'assurer que les développeurs vérifient les `null` avant de déréférencer les références nullables, **tout cela au moment de la compilation**.

Microsoft adopte la même approche en introduisant les [Nullable Reference Types](https://msdn.microsoft.com/en-us/magazine/mt829270.aspx) dans C#8.

### Que devons-nous faire ?

#### Écouter Uncle Bob

[Robert C. Martin](https://en.wikipedia.org/wiki/Robert_C._Martin), largement connu sous le nom d'« Uncle Bob », a écrit l'un des livres les plus célèbres sur le code propre, intitulé (sans surprise) [« Clean Code »](https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882). Dans ce livre, Uncle Bob affirme que **nous ne devrions pas retourner de `nulls` et ne devrions pas passer de `null` à une fonction.**

![Image](https://cdn-media-1.freecodecamp.org/images/0*HGcUEEzNp9mTmK5w.jpg)

#### Mais comment ?

Je veux proposer quelques **schémas techniques** pour éliminer l'utilisation de null. **Je ne dis pas que c'est la meilleure solution pour chaque scénario — juste des options**.

**Utiliser le type option**

Le [type option](https://en.m.wikipedia.org/wiki/Option_type?wprov=sfla1&fbclid=IwAR3Y-vZX-mrpINhipnr_tjyZ4P8KZH0yLCtvcJqbtaMxry2DO6HJWdSP3XA) est une autre façon de représenter une valeur optionnelle. Ce type demande si une valeur existe et, si oui, accède à la valeur. **Lorsqu'on essaie d'accéder à la valeur qui n'existe pas, cela lève une exception**. Cela résout le problème de `NullPointerException` levé dans des zones de code éloignées du bug. En Java, il y a la classe [Optional<T>](https://docs.oracle.com/javase/8/docs/api/java/util/Optional.html). En C# (jusqu'à C# 7), il y a le type [Nullable](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/nullable-types/) qui est uniquement pour les types valeur, mais vous pouvez créer le vôtre ou [utiliser une bibliothèque](https://github.com/nlkl/Optional).

Une approche directe consiste à remplacer une référence qui peut être `null` (par logique) par ce type :

**Diviser la fonction en deux**

Chaque fonction qui retourne `null` sera convertie en deux fonctions. Une fonction avec la même signature lève une exception au lieu de retourner `null`. La deuxième fonction retourne un booléen indiquant si c'est valide ou non d'appeler la première fonction. Voyons un exemple :

Si le code contenant une instance `IEmployee` suppose que cet employé a un manager, le code doit appeler `Manager`. Mais si cette supposition n'existe pas, le code doit appeler `HasManager` et gérer les deux sorties possibles.

Voyons un autre exemple :

La logique de `ContainsEmployeById` est essentiellement la même que `FindEmployeById` mais sans retourner l'employé. Supposons maintenant que ces fonctions atteignent la base de données, nous avons un problème de performance ici. Introduisons un schéma similaire mais différent : la fonction `boolean` lorsqu'elle retourne `true` retournera également les données que nous recherchons. Cela ressemble à ceci :

Une utilisation courante de ce schéma est `int.Parse` et `[int.TryParse](https://docs.microsoft.com/en-us/dotnet/api/system.int32.tryparse?view=netframework-4.7.2#System_Int32_TryParse_System_String_System_Int32__)`.

Le fait que je puisse séparer une fonction en deux fonctions et que chacune ait ses propres usages est un signe que retourner `null` est un **mauvais code pour violer le Principe de Responsabilité Unique**.

### Diviser l'interface

Une directive pratique que nous pouvons déduire du [principe de Liskov](https://en.wikipedia.org/wiki/Liskov_substitution_principle) est qu'une classe **doit implémenter toutes les fonctions** d'une interface qu'elle implémente. Retourner `null` ou lever une exception sont des moyens de ne pas implémenter une fonction. Donc retourner `null` est un **mauvais code pour violer le principe de Liskov**.

Si une classe ne peut pas implémenter une fonction spécifique d'une interface, **nous pouvons déplacer cette fonction vers une autre interface** et chaque classe implémentera uniquement l'interface qu'elle peut.

Maintenant, au lieu de demander `employee.HasManager` — ce que nous ferions si nous utilisions la première approche « Diviser la fonction en deux » — nous demandons si l'employé est `IManagedEmployee`.

### Je ne travaille pas seul et pas sur un projet greenfield. Que faire maintenant ?

Dans les bases de code existantes, il y a beaucoup de code retournant des types de référence. Nous ne pouvons pas savoir si `null` est une sortie valide ou non.

La première victoire rapide que je souhaite vous voir obtenir est de **changer vos conventions de codage** pour que `null` ne soit pas une entrée ou une sortie valide pour une fonction. Ou, au moins lorsque vous décidez que `null` est une sortie valide, utilisez **le type Option**.

Il existe des outils qui peuvent aider à faire respecter cette convention comme [ReSharper](https://www.jetbrains.com/help/resharper/Code_Analysis__Value_Analysis.html) et [NullGuard](https://github.com/Fody/NullGuard). Je suppose, bien que je ne l'aie pas encore essayé, que vous pouvez ajouter une [règle personnalisée à SonarQube](https://docs.sonarqube.org/display/DEV/Adding+Coding+Rules) qui alertera lorsque le mot `null` apparaît.

J'aimerais savoir ce que vous en pensez. Allez-vous adopter cette convention ? Et si non, pourquoi ? Qu'est-ce qui vous retient ?

Si vous rencontrez un scénario dans lequel vous pensez que retourner `null` est le bon choix de conception, ou que les schémas que j'ai suggérés ne sont pas bons, j'aimerais le savoir.

Merci à [Mark Kazakov](https://www.linkedin.com/in/mark-kazakov-98994197/) pour le mème drôle, [Alex Zhitnitsky](https://www.linkedin.com/in/alex-zhitnitsky-86567238/) d'OverOps pour avoir répondu à mes questions, [Baot](https://www.facebook.com/baot.tech/) pour avoir organisé un grand événement d'écriture pour les nouveaux blogueurs, [Itzik Saban](https://www.linkedin.com/in/itzik-saban-54b93829/), [Amitay Horwitz](https://www.linkedin.com/in/amitayhorwitz/) et [Max Ophius](https://www.facebook.com/max.ophius) pour m'avoir donné des retours.