---
title: Pourquoi nous aurons toujours besoin de nouveaux langages de programmation
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-25T15:40:40.000Z'
originalURL: https://freecodecamp.org/news/why-we-will-always-need-new-programming-languages-3415869ea37e
coverImage: https://cdn-media-1.freecodecamp.org/images/0*ngXgBNNdx6iiWP8q.png
tags:
- name: coding
  slug: coding
- name: Kotlin
  slug: kotlin
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Pourquoi nous aurons toujours besoin de nouveaux langages de programmation
seo_desc: 'By Marcin Moskala

  Structure and Interpretation of Computer Programs by Harold Abelson and Gerald Jay
  Sussman is one of the best books about programming ever written. It was ahead of
  its time for many years.

  The advantages of functional programming th...'
---

Par Marcin Moskala

[Structure et Interprétation des Programmes Informatiques](http://web.mit.edu/alexmv/6.037/sicp.pdf) par Harold Abelson et Gerald Jay Sussman est l'un des meilleurs livres sur la programmation jamais écrits. Il était en avance sur son temps pendant de nombreuses années.

Les avantages de la programmation fonctionnelle qui y étaient mis en avant sont encore une source constante d'inspiration pour les conférenciers, les enseignants et autres auteurs. Il a montré la puissance et les faiblesses de la programmation orientée objet alors qu'elle était encore jeune. Les puissances ont rapidement été mises en avant grâce aux fanatiques de la programmation orientée objet. En revanche, il a fallu des années à la communauté pour voir les faiblesses.

Le dernier chapitre était entièrement consacré à un autre concept qui est encore peu discuté dans le dialogue populaire : le besoin de nouveaux langages de programmation. Bien que le livre sympathisait avec [Lisp](https://en.wikipedia.org/wiki/Lisp_(programming_language)), il affirmait clairement qu'il ne s'agit pas du langage de programmation final. Aucun langage ne le sera jamais.

Nous aurons toujours besoin de nouveaux langages de programmation pour améliorer notre expressivité. Ce n'est pas une affirmation triviale, et pour comprendre ce qui se cache derrière, nous devons descendre de deux niveaux.

### Qu'est-ce qu'un langage de programmation ?

Voir la fonction suivante :

```
fun square(a: Int) = a * a
```

```
// Utilisationprint(square(10) + square(20))
```

Que signifie le fait que `square` soit défini ?

D'un point de vue technique, ce n'est qu'une simplification et le corps peut remplacer tous les appels :

```
// Kotlinprint(10 * 10 + 20 * 20)
```

Du point de vue du programmeur, `square` est bien plus. Le fait que nous puissions définir une telle fonction n'est pas seulement un moyen plus simple de réaliser une opération, mais cela nous permet également d'exprimer un concept de mise au carré. Cette fonction est une certaine abstraction.

Si elle était plus complexe, elle nous permettrait de cacher toute cette complexité derrière un simple appel de fonction. C'est ce qu'est la programmation : différentes fonctionnalités des langages de programmation nous permettent d'exprimer les choses de différentes manières.

### Évolution des langages de programmation

L'industrie de la programmation évolue, et les langages de programmation aussi. Pensez à la boucle for. Initialement, il n'y avait que la boucle when.

Bientôt, les programmeurs ont remarqué un motif commun :

```
// Cint i = 0;while(i < n) {    i++;    // ...} 
```

L'expression `while` était utilisée encore et encore pour itérer sur quelque chose — principalement des nombres, des adresses ou des itérateurs.

Nous avons donc introduit les boucles for :

```
// C++for (int i = 0; i < n; i++) {    // ...}
```

Bientôt, l'industrie a observé que la boucle for est principalement utilisée pour itérer sur les éléments d'une liste.

C'est pourquoi les langages ont introduit une nouvelle variante de la boucle for qui est conçue pour itérer sur `list` :

```
// Kotlinfor(e in list) {    // ...}
```

### Nous avons donc besoin de nouvelles fonctionnalités

#### Mais les langages évoluent, pourquoi ne pas rester avec eux ?

Il est vrai que les langages évoluent. Dans certains cas, il est vraiment impressionnant de voir comment des langages anciens comme C++, Java ou JavaScript peuvent avoir un bon support pour les éléments de programmation fonctionnelle pour lesquels ils n'étaient pas conçus. Mais le problème est que les nouvelles fonctionnalités ne remplacent pas les anciennes — elles sont ajoutées.

En termes de fonctionnalités des langages de programmation, plus n'est pas nécessairement mieux. C'est déroutant lorsque nous pouvons exprimer le même concept de nombreuses manières différentes.

Pensez à [Scala](https://www.scala-lang.org/). La plus grande objection avec Scala est que trop de fonctionnalités différentes le rendent extrêmement difficile à comprendre ce qui se passe dans le code d'un développeur avec un peu trop de créativité.

Le langage de programmation [Go](https://golang.org/) a bâti sa popularité sur la simplicité. Ce n'est pas une question de savoir combien de fonctionnalités certains langages ont, mais d'avoir l'ensemble parfait de fonctionnalités.

À mon avis, c'est pourquoi tout le monde aime tant [Kotlin](https://kotlinlang.org/). C'est le langage de programmation le mieux conçu que je connaisse.

Il y a de bonnes raisons à cela :

* Il était en version bêta pendant 6 ans et il a évolué de manière itérative pendant tout ce temps
* Il est conçu par [JetBrains](https://www.jetbrains.com/) qui maîtrisent leur compréhension des langages de programmation et de la manière dont les gens les utilisent depuis des années

Pendant la période bêta, certaines fonctionnalités importantes ont été entièrement implémentées, et pourtant elles ont été supprimées avant la version 1.0. Parmi elles, les tuples. Kotlin les supportait pleinement ! Pourtant, l'équipe Kotlin a supprimé le support des tuples avant Kotlin 1.0 parce que leurs analyses et expériences ont montré que les tuples font plus de mal que de bien, et que les gens devraient utiliser des classes de données à la place. Cela montre que JetBrains comprend l'importance d'un bon design.

Un autre langage bien conçu est [Swift](https://swift.org/). Il a été développé beaucoup plus rapidement, et les développeurs qui l'ont conçu ont fait beaucoup d'erreurs. Pourtant, Apple a simplement changé le design avec presque chaque version majeure. Ils ne se soucient pas vraiment du héritage.

Les développeurs râlent, mais du point de vue du design, c'est génial. Bien qu'ils ne puissent pas continuer à faire cela longtemps. Plus il y a de choses dans Swift, plus le coût du changement de design est élevé. De plus, je ne pense pas qu'ils soient capables de changer les fonctionnalités majeures.

![Image](https://cdn-media-1.freecodecamp.org/images/gyPeeyU3As2Bd4PHAt50byzZlibC2ResHNDd)
_Source : [https://getbadges.io/blog/12-gamification-platforms-that-help-learn-coding](https://getbadges.io/blog/12-gamification-platforms-that-help-learn-coding" rel="noopener" target="_blank" title=")_

### Donc, si nous avons de nouveaux langages bien conçus, sont-ils les langages finaux ?

Pas du tout. Les industries évoluent. Notre façon de penser évolue. Et donc les langages de programmation doivent évoluer également.

Une chose est que des idées pour de nouvelles fonctionnalités et de nouvelles façons de penser naîtront, et donc les langages parfaitement conçus ne seront plus parfaits.

La deuxième chose est que nous en apprenons davantage sur la programmation. Les classes et les méthodes sont ouvertes par défaut en Java. Kotlin les a rendues finales par défaut parce que les développeurs utilisaient excessivement l'héritage alors qu'ils n'auraient pas dû.

Les membres de classe Java étaient package-private par défaut. Ce modificateur était presque jamais utilisé. Kotlin ne l'autorise pas du tout, mais à la place, les membres de classe sont publics par défaut parce que c'est le modificateur le plus courant pour eux. Nous changeons nos habitudes et nous apprenons, donc les langages doivent aussi changer avec nous.

La troisième chose est que les paradigmes changent. Je vois une stagnation en termes de paradigmes de programmation, mais nous avons encore quelques-uns à introduire dans la pratique quotidienne.

Où est passée la programmation logique ? Remarquez que vous pouvez utiliser ce paradigme et simplement fournir un ensemble de contraintes pour un site web et vous attendre à ce que le site web soit construit automatiquement sur la base de celles-ci. Il est possible de l'implémenter. De plus, de nouveaux paradigmes naîtront tôt ou tard. Il ne peut pas en être que nous ayons tout exploré.

Enfin, de nouvelles technologies naissent et l'ancienne façon de penser représentée par les langages précédents peut ne pas être adéquate.

Pensez à la [blockchain](https://en.wikipedia.org/wiki/Blockchain). Lorsque je parle à des personnes qui envisagent de passer à la blockchain, elles veulent utiliser leurs langages préférés comme Java ou JavaScript. Bien que lorsque je parle à des développeurs de blockchain, ils affirment que la blockchain doit être développée dans des langages qui sont conçus pour elle.

Par exemple, un contrat est un concept qui n'a pas d'équivalent en programmation. Il peut être simulé par une classe, mais cela est nuisible à la façon dont les gens y pensent. C'est dommageable lorsque nous essayons d'exprimer de nouvelles choses en utilisant de vieux mots. C'est comme nommer une voiture "cheval d'acier" et essayer de faire des mécaniciens à partir de vétérinaires.

### Conclusion

Pensez aux mathématiques. L'équilibre peut être exprimé de manière descriptive :

**Deux plus trois égale cinq**

Bien que ce soit quelque chose de totalement différent que de l'exprimer en utilisant la notation mathématique :

**2 + 3 = 5**

Ce n'est pas seulement une optimisation pour la lisibilité et l'espace. Ces deux notations signifient la même chose, mais elles représentent des concepts totalement différents. C'est quelque chose qui n'est pas important du point de vue d'un ordinateur — qui peut facilement traduire la forme descriptive en mathématique — mais c'est la chose la plus importante pour nous en tant qu'êtres humains.

Si ce n'était pas important, nous utiliserions l'Assembleur au lieu de Java, JavaScript, Python ou Kotlin. Mais c'est important. C'est pourquoi nous avons besoin d'une meilleure et meilleure expression, et nous avons besoin de nouveaux langages de programmation.

![Image](https://cdn-media-1.freecodecamp.org/images/Vr01qrslh5N7yR1gf6L3OfIRGPg6r2ttP102)

### À propos de l'auteur

[Marcin Moskała](http://marcinmoskala.com/) ([@marcinmoskala](https://twitter.com/marcinmoskala)) est un formateur et consultant, se concentrant actuellement sur la formation Kotlin pour Android et les ateliers avancés Kotlin (pour plus de détails, [postulez ici](https://marcinmoskala.typeform.com/to/iwKnN9)). Il est également un [conférencier](https://www.youtube.com/results?search_query=Marcin+Moskała), auteur d'[articles](https://medium.com/@marcinmoskala) et d'[un livre](https://www.packtpub.com/application-development/android-development-kotlin) sur le développement Android en Kotlin.

![Image](https://cdn-media-1.freecodecamp.org/images/70Dz9UeSMUlQTowTe8t8N-QuMO2BZSD80C5b)