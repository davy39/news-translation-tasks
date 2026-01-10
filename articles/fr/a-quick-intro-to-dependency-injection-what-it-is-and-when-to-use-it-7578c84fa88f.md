---
title: 'Une introduction rapide à l''injection de dépendances : qu''est-ce que c''est
  et quand l''utiliser'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-18T22:25:28.000Z'
originalURL: https://freecodecamp.org/news/a-quick-intro-to-dependency-injection-what-it-is-and-when-to-use-it-7578c84fa88f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*rU6KNs9KfdROiENL-UQTNA.jpeg
tags:
- name: Design
  slug: design
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: 'Une introduction rapide à l''injection de dépendances : qu''est-ce que
  c''est et quand l''utiliser'
seo_desc: 'By Bhavya Karia

  Introduction


  In software engineering, dependency injection is a technique whereby one object
  (or static method) supplies the dependencies of another object. A dependency is
  an object that can be used (a service).


  That’s the Wikipedi...'
---

Par Bhavya Karia

### Introduction

> En [ingénierie logicielle](https://en.wikipedia.org/wiki/Software_engineering), l'**injection de dépendances** est une technique par laquelle un objet (ou une méthode statique) fournit les dépendances d'un autre objet. Une dépendance est un objet qui peut être utilisé (un [service](https://en.wikipedia.org/wiki/Service_(systems_architecture))).

C'est la définition de Wikipedia, mais elle n'est pas particulièrement facile à comprendre. Alors, essayons de mieux la comprendre.

Avant de comprendre ce que cela signifie en programmation, voyons d'abord ce que cela signifie en général, car cela nous aidera à mieux comprendre le concept.

Une dépendance ou un dépendant signifie compter sur quelque chose pour obtenir du soutien. Par exemple, si je dis que nous dépendons trop des téléphones mobiles, cela signifie que nous sommes dépendants d'eux.

Alors, avant d'aborder l'[**injection de dépendances**](https://en.wikipedia.org/wiki/Dependency_injection), comprenons d'abord ce qu'est une dépendance en programmation.

Lorsque la classe A utilise certaines fonctionnalités de la classe B, on dit alors que la classe A a une dépendance à la classe B.

![Image](https://cdn-media-1.freecodecamp.org/images/1*0P-1JhnUaZeobDUAajIbhA.jpeg)
_Montrant les dépendances entre les classes_

En Java, avant de pouvoir utiliser les méthodes d'autres classes, nous devons d'abord créer l'objet de cette classe (c'est-à-dire que la classe A doit créer une instance de la classe B).

**Ainsi, transférer la tâche de création de l'objet à quelqu'un d'autre et utiliser directement la dépendance s'appelle l'injection de dépendances.**

![Image](https://cdn-media-1.freecodecamp.org/images/1*TF-VdAgPfcD497kAW77Ukg.png)
_Et si le code pouvait parler ?_

### Pourquoi devrais-je utiliser l'injection de dépendances ?

Supposons que nous avons une classe voiture qui contient divers objets tels que des roues, un moteur, etc.

Ici, la classe voiture est responsable de la création de tous les objets de dépendance. Maintenant, que se passe-t-il si nous décidons d'abandonner **MRFWheels** à l'avenir et que nous voulons utiliser des roues **Yokohama** ?

Nous devrons recréer l'objet voiture avec une nouvelle dépendance Yokohama. Mais en utilisant l'injection de dépendances (DI), nous pouvons changer les roues à l'exécution (car les dépendances peuvent être injectées à l'exécution plutôt qu'à la compilation).

Vous pouvez penser à DI comme l'intermédiaire dans notre code qui fait tout le travail de création de l'objet de roues préféré et le fournit à la classe Car.

Cela rend notre classe Car indépendante de la création des objets de roues, de batterie, etc.

#### Il existe essentiellement trois types d'injection de dépendances :

1. **injection par constructeur** : les dépendances sont fournies via un constructeur de classe.
2. **injection par setter** : le client expose une méthode setter que l'injecteur utilise pour injecter la dépendance.
3. **injection par interface** : la dépendance fournit une méthode d'injecteur qui injectera la dépendance dans tout client qui lui est passé. Les clients doivent implémenter une interface qui expose une [méthode setter](https://en.wikipedia.org/wiki/Setter_method) qui accepte la dépendance.

**Ainsi, c'est maintenant la responsabilité de l'injection de dépendances de :**

1. Créer les objets
2. Savoir quelles classes nécessitent ces objets
3. Et fournir tous ces objets

Si un objet change, alors DI s'en occupe et cela ne devrait pas concerner la classe utilisant ces objets. De cette manière, si les objets changent à l'avenir, c'est la responsabilité de DI de fournir les objets appropriés à la classe.

#### Inversion de contrôle — le concept derrière DI

Cela stipule qu'une classe ne doit pas configurer ses dépendances de manière statique, mais doit être configurée par une autre classe de l'extérieur.

C'est le cinquième principe de **S.O.L.I.D** — les cinq principes de base de la programmation et de la conception orientées objet par [**Uncle Bob**](https://en.wikipedia.org/wiki/Robert_C._Martin) — qui stipule qu'une classe doit dépendre de l'abstraction et non des concretions (en termes simples, du code en dur).

Selon les principes, une classe doit se concentrer sur l'accomplissement de ses responsabilités et non sur la création d'objets dont elle a besoin pour accomplir ces responsabilités. Et c'est là que l'**injection de dépendances** entre en jeu : elle fournit à la classe les objets requis.

_Note : Si vous souhaitez en savoir plus sur les principes **SOLID** d'Uncle Bob, vous pouvez vous rendre sur ce [lien](https://scotch.io/bar-talk/s-o-l-i-d-the-first-five-principles-of-object-oriented-design#toc-single-responsibility-principle)._

#### Avantages de l'utilisation de DI

1. Aide aux tests unitaires.
2. Réduit le code standard, car l'initialisation des dépendances est effectuée par le composant injecteur.
3. L'extension de l'application devient plus facile.
4. Aide à activer le couplage lâche, ce qui est important dans la programmation d'applications.

#### Inconvénients de DI

1. C'est un peu complexe à apprendre, et si elle est surutilisée, cela peut entraîner des problèmes de gestion et d'autres problèmes.
2. De nombreuses erreurs de compilation sont repoussées à l'exécution.
3. Les frameworks d'injection de dépendances sont implémentés avec réflexion ou programmation dynamique. Cela peut entraver l'utilisation de l'automatisation de l'IDE, telle que « trouver les références », « afficher la hiérarchie des appels » et le refactoring sécurisé.

Vous pouvez implémenter l'injection de dépendances par vous-même (Pure Vanilla) ou utiliser des bibliothèques ou frameworks tiers.

#### **Bibliothèques et frameworks qui implémentent DI**

* [Spring](https://www.tutorialspoint.com/spring/spring_dependency_injection.htm) (Java)
* [Google Guice](https://github.com/google/guice) (Java)
* [Dagger](http://square.github.io/dagger/) (Java et Android)
* [Castle Windsor](https://github.com/castleproject/Windsor) (.NET)
* [Unity](https://www.microsoft.com/en-us/download/details.aspx?id=39944)(.NET)

**Pour en savoir plus sur l'injection de dépendances, vous pouvez consulter les ressources suivantes :**

[**Java Dependency Injection — DI Design Pattern Example Tutorial — JournalDev**](https://www.journaldev.com/2394/java-dependency-injection-design-pattern-example-tutorial)

[**Using dependency injection in Java — Introduction — Tutorial — Vogella**](http://www.vogella.com/tutorials/DependencyInjection/article.html)

[**Inversion of Control Containers and the Dependency Injection pattern — Martin Fowler**](https://www.martinfowler.com/articles/injection.html)

J'espère que cela aide !

Si vous avez aimé l'article et souhaitez lire d'autres articles passionnants, alors suivez-moi ici ([Bhavya Karia](https://medium.com/@bhavyankaria)) et montrez votre soutien, car cela me motive à écrire davantage.

Si vous avez des questions ou des commentaires pour moi, connectons-nous sur [LinkedIn](https://www.linkedin.com/in/bhavya-karia-1b115a93/), [Twitter](https://twitter.com/thebhavyakaria), [Facebook](https://www.facebook.com/karia.bhavya).

#### Édition 1 :

**_Merci à [Sergey Ufocoder](https://www.freecodecamp.org/news/a-quick-intro-to-dependency-injection-what-it-is-and-when-to-use-it-7578c84fa88f/undefined), cet article a maintenant été traduit en russe. Mes amis russes et tous ceux qui peuvent lire le russe, n'hésitez pas à le lire._**

[Lien vers l'article](https://medium.com/@xufocoder/a-quick-intro-to-dependency-injection-what-it-is-and-when-to-use-it-de1367295ba8)

**_De plus, si vous souhaitez appliquer DI en JavaScript et cherchez une bibliothèque, [Jo Surikat](https://www.freecodecamp.org/news/a-quick-intro-to-dependency-injection-what-it-is-and-when-to-use-it-7578c84fa88f/undefined) suggère d'essayer sa bibliothèque._**

[Di-Ninja](https://di-ninja.github.io/di-ninja/)

**_Une autre bibliothèque DI géniale en JavaScript a été suggérée par [Nicolas Froidure](https://www.freecodecamp.org/news/a-quick-intro-to-dependency-injection-what-it-is-and-when-to-use-it-7578c84fa88f/undefined)._**

[knifecycle](https://github.com/nfroidure/knifecycle)

#### Édition 2 :

**_Si vous êtes un développeur PHP, ne vous inquiétez pas, je vous ai également couvert. [Gordon Forsythe](https://www.freecodecamp.org/news/a-quick-intro-to-dependency-injection-what-it-is-and-when-to-use-it-7578c84fa88f/undefined) a recommandé cette bibliothèque incroyable que vous pourriez tous vouloir essayer._**

[auryn](https://github.com/rdlowrey/auryn)

Merci pour tous les mots gentils que j'ai reçus. Partagez l'article afin que de plus en plus de personnes puissent en bénéficier.

Si vous avez appris une ou deux choses, veuillez partager cette histoire !