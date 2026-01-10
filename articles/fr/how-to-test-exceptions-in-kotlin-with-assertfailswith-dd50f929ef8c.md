---
title: Comment tester les exceptions en Kotlin avec assertFailsWith
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-26T18:40:05.000Z'
originalURL: https://freecodecamp.org/news/how-to-test-exceptions-in-kotlin-with-assertfailswith-dd50f929ef8c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*97MX1nM7-TWatCX9pbU-Kw.png
tags:
- name: Kotlin
  slug: kotlin
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Testing
  slug: testing
seo_title: Comment tester les exceptions en Kotlin avec assertFailsWith
seo_desc: 'By Daniel Newton

  I wanted to write this short post to highlight the assertFailsWith function available
  to Kotlin. This function makes testing exceptions a bit easier. Testing exceptions
  isn’t something fancy or new to JVM languages (from now on I wil...'
---

Par Daniel Newton

Je voulais écrire ce court article pour mettre en avant la fonction `assertFailsWith` disponible en Kotlin. Cette fonction facilite un peu les tests d'exceptions. Tester les exceptions n'est pas quelque chose de sophistiqué ou de nouveau pour les langages JVM (désormais, j'utiliserai Java pour les comparaisons). Kotlin offre l'avantage supplémentaire de fournir cette fonctionnalité dans sa bibliothèque standard. En comparaison avec Java, vous seriez probablement amené à utiliser [AssertJ](http://joel-costigliola.github.io/assertj/) pour obtenir des résultats similaires.

Le principal objectif de cet article est de vous faire connaître la fonction `assertFailsWith`. Personnellement, je ne savais pas qu'elle existait pendant un certain temps et je dépendais par défaut d'AssertJ. Ce n'est pas que j'aie quelque chose contre AssertJ, bien au contraire. Il existe de nombreuses autres fonctionnalités que la bibliothèque fournit. Pour cette instance spécifique, il pourrait être possible de la supprimer (en supposant que vous ne l'utilisez pas pour autre chose).

Qu'est-ce qui est bien avec `assertFailsWith` et AssertJ en général ? Ils offrent de meilleurs tests d'exceptions que les simples constructions fournies par JUnit. Plus précisément, ils vous permettent de spécifier quelle partie de votre test vous attendez à ce qu'une exception soit levée, au lieu de déclarer qu'une exception se produira quelque part dans le code. Cela pourrait conduire à des exceptions étant incorrectement avalées par le test à un point incorrect et vous tromper en pensant qu'il fonctionne comme vous le pensez.

Maintenant que j'ai abordé ce point, passons au contenu principal de cet article. Voici à quoi ressemble `assertFailsWith` à l'intérieur d'un test :

Dans cet exemple, `hereIsAnException` est placé à l'intérieur du corps de `assertFailsWith`, qui vérifie qu'une `IllegalArgumentException` est levée. Si aucune n'est levée, alors l'assertion échouera. Si une exception se produit, alors l'assertion passera et l'exception sera capturée.

Capturer l'exception permet à l'exécution du code de test de continuer si nécessaire, ainsi que de vous permettre de faire des assertions supplémentaires sur l'état de l'exception.

Par exemple, est-ce un wrapper autour d'une autre exception (quel est le type de sa propriété `cause`) ?

Le message est-il celui que vous attendez (pas le plus solide des contrôles) ?

Seules les exceptions qui sont du même type ou sous-type que celui spécifié par `assertFailsWith` seront capturées. Les autres feront échouer le test. Puisqu'il capture les sous-types, veuillez ne pas spécifier simplement `Exception` ou `RuntimeException`. Essayez d'être précis pour que vos tests soient aussi utiles que possible.

Comme mentionné précédemment, `assertFailsWith` ne capturera qu'une exception qui est levée dans le corps de la fonction. Par conséquent, si cela était écrit à la place :

Le test échouerait. `hereIsAnException` a levé une exception, qui n'a pas été capturée et conduit à l'échec du test. Je crois que c'est la meilleure partie de ce type de fonction par rapport aux anciennes méthodes utilisées (par exemple, en assertant dans `@Test` qu'une exception se produirait).

Personnellement, je n'ai jamais vraiment utilisé la partie message d'une assertion. Peut-être que vous le faites, alors je pensais au moins vous le faire savoir.

Avant de conclure le peu de contenu de cet article, jetons un rapide coup d'œil à AssertJ afin que nous puissions établir une comparaison entre les deux. Encore une fois, ceci n'est que pour le cas de la capture des exceptions, ce qui n'est qu'une petite partie de ce qu'AssertJ fournit.

Cela est légèrement plus "verbeux" que la version `assertFailsWith`. Mais cela est compensé par la pléthore de fonctions qu'AssertJ fournit, ce qui rend toute vérification supplémentaire de l'exception retournée beaucoup plus facile. Plus précisément, lors de l'utilisation de `assertFailsWith`, j'ai dû écrire une autre assertion pour vérifier le message. Dans AssertJ, cela n'est qu'une fonction enchaînée à la fin de l'appel précédent.

En conclusion, `assertFailsWith` est une petite fonction agréable à utiliser dans les tests pour s'assurer qu'un morceau de code lève un type spécifique d'exception. Elle est intégrée dans la bibliothèque standard de Kotlin, ce qui élimine le besoin d'ajouter une dépendance supplémentaire à votre projet. Cela dit, c'est une fonction relativement simple et elle n'apporte pas le type de fonctionnalités qu'une bibliothèque comme AssertJ fournirait. Elle est susceptible de suffire jusqu'à ce que vous souhaitiez écrire des tests qui contiennent une large gamme d'assertions, car c'est à ce moment-là que cela peut devenir compliqué.

La documentation officielle pour `assertFailsWith` peut être trouvée ici si vous êtes intéressé [Kotlin Docs – assertFailsWith](https://kotlinlang.org/api/latest/kotlin.test/kotlin.test/assert-fails-with.html).

Si vous avez trouvé cet article utile, vous pouvez me suivre sur Twitter à [@LankyDanDev](https://twitter.com/LankyDanDev) pour rester informé de mes nouveaux articles.

[Voir tous les articles de Dan Newton](https://lankydanblog.com/author/danknewton/)

_Publié à l'origine sur [lankydanblog.com](https://lankydanblog.com/2019/01/26/testing-exceptions-in-kotlin-with-assertfailswith/) le 26 janvier 2019._