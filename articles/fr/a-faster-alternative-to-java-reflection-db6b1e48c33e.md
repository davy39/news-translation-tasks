---
title: Une alternative plus rapide à la réflexion Java
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-11T15:38:23.000Z'
originalURL: https://freecodecamp.org/news/a-faster-alternative-to-java-reflection-db6b1e48c33e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*63rcvkvE5D5TUKmQ6q7I7A.jpeg
tags:
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
seo_title: Une alternative plus rapide à la réflexion Java
seo_desc: 'By Carlos Raphael

  In the article Specification Pattern, for the sake of sanity, I didn’t mention about
  an underlying component to nicely make that thing happen. Now, I’ll elaborate a
  little bit more around the JavaBeanUtil class, that I put in place ...'
---

Par Carlos Raphael

Dans l'article [Specification Pattern](https://medium.com/@carlosraphael/specification-design-pattern-in-java-8-bac6f5f943bc), pour des raisons de simplicité, je n'ai pas mentionné un composant sous-jacent qui permet de faire fonctionner cela de manière élégante. Maintenant, je vais élaborer un peu plus autour de la classe [JavaBeanUtil](https://github.com/carlosraphael/specification-pattern/blob/master/src/main/java/com/github/carlosraphael/specificationpattern/util/JavaBeanUtil.java), que j'ai mise en place pour lire la valeur d'un `fieldName` donné à partir d'un `javaBeanObject` particulier, qui dans cette occasion s'est avéré être [FxTransaction](https://github.com/carlosraphael/specification-pattern/blob/master/src/main/java/com/github/carlosraphael/specificationpattern/FxTransaction.java).

Vous pourriez facilement argumenter que j'aurais pu utiliser [Apache Commons BeanUtils](http://commons.apache.org/proper/commons-beanutils/) ou l'une de ses alternatives pour obtenir le même résultat. Mais je m'intéressais à mettre la main à la pâte avec quelque chose de différent que je savais être bien plus rapide que toute bibliothèque construite sur la très connue [Java Reflection](https://www.oracle.com/technetwork/articles/java/javareflection-1536171.html).

L'élément clé de la technique utilisée pour éviter la réflexion très lente est l'instruction de bytecode `invokedynamic`. En bref, `invokedynamic` (ou "indy") était la meilleure chose introduite dans Java 7 afin de préparer le terrain pour l'implémentation de langages dynamiques sur la JVM grâce à l'invocation dynamique de méthodes. Cela a également permis plus tard les [expressions lambda](https://docs.oracle.com/javase/tutorial/java/javaOO/lambdaexpressions.html) et les [références de méthode](https://docs.oracle.com/javase/tutorial/java/javaOO/methodreferences.html) dans Java 8 ainsi que la concaténation de chaînes dans Java 9 pour en bénéficier.

En résumé, la technique que je m'apprête à mieux décrire ci-dessous utilise [LambdaMetafactory](https://docs.oracle.com/javase/8/docs/api/java/lang/invoke/LambdaMetafactory.html) et [MethodHandle](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/invoke/MethodHandles.html) afin de créer dynamiquement une implémentation de [Function](https://docs.oracle.com/javase/8/docs/api/java/util/function/Function.html). Sa [méthode unique](https://docs.oracle.com/javase/8/docs/api/java/util/function/Function.html#apply-T-) délègue un appel à la méthode cible réelle avec un code défini à l'intérieur du corps de la lambda.

La méthode cible en question ici est la méthode getter réelle qui a un accès direct au champ que nous voulons lire. De plus, je devrais dire que si vous êtes assez familier avec les bonnes choses qui sont apparues dans Java 8, vous trouverez les extraits de code ci-dessous assez faciles à comprendre. Sinon, cela peut sembler délicat à première vue.

### Un aperçu de JavaBeanUtil fait maison

La méthode suivante est l'utilitaire utilisé pour lire une valeur à partir d'un champ JavaBean. Elle prend l'objet JavaBean et un seul `fieldA` ou même un champ imbriqué séparé par des points, par exemple, `nestedJavaBean.nestedJavaBean.fieldA`

Pour des performances optimales, je mets en cache la fonction créée dynamiquement qui est la manière réelle de lire le contenu d'un `fieldName` donné. Ainsi, à l'intérieur de la méthode `getCachedFunction`, comme vous pouvez le voir ci-dessus, il y a un chemin rapide utilisant [ClassValue](https://docs.oracle.com/javase/8/docs/api/java/lang/ClassValue.html) pour la mise en cache et il y a le chemin lent `createAndCacheFunction` exécuté uniquement si rien n'a été mis en cache jusqu'à présent.

Le chemin lent délèguera essentiellement à la méthode `createFunctions` qui retourne une liste de fonctions à réduire en les enchaînant à l'aide de `Function::andThen`. Lorsque les fonctions sont enchaînées, vous pouvez imaginer une sorte d'appels imbriqués comme `getNestedJavaBean().getNestedJavaBean().getFieldA()`. Enfin, après l'enchaînement, nous mettons simplement la fonction réduite en cache en appelant la méthode `cacheAndGetFunction`.

En approfondissant un peu plus le chemin lent de la création de fonction, nous devons naviguer individuellement à travers la variable de chemin `path` en la divisant comme suit :

La méthode `createFunctions` ci-dessus délègue le `fieldName` individuel et son type de classe de support à la méthode `createFunction`, qui localisera le getter nécessaire en fonction de `javaBeanClass.getDeclaredMethods()`. Une fois localisé, il le mappe à un objet Tuple (facilité de la bibliothèque [Vavr](http://www.vavr.io/)), qui contient le type de retour de la méthode getter et la fonction créée dynamiquement qui agira comme si elle était la méthode getter réelle elle-même.

Ce mappage de tuple est effectué par `createTupleWithReturnTypeAndGetter` en conjonction avec la méthode `createCallSite` comme suit :

Dans les deux méthodes ci-dessus, j'utilise une constante appelée `LOOKUP`, qui est simplement une référence à [MethodHandles.Lookup](https://docs.oracle.com/javase/8/docs/api/java/lang/invoke/MethodHandles.Lookup.html). Avec cela, je peux créer un [direct method handle](https://docs.oracle.com/javase/8/docs/api/java/lang/invoke/MethodHandleInfo.html#directmh) basé sur la méthode getter précédemment localisée. Et enfin, le [MethodHandle](https://docs.oracle.com/javase/8/docs/api/java/lang/invoke/MethodHandle.html) créé est passé à la méthode `createCallSite` où le corps de la lambda pour la fonction est produit en utilisant [LambdaMetafactory](https://docs.oracle.com/javase/8/docs/api/java/lang/invoke/LambdaMetafactory.html). À partir de là, nous pouvons finalement obtenir l'instance [CallSite](https://docs.oracle.com/javase/8/docs/api/java/lang/invoke/CallSite.html), qui est le support de la fonction.

Notez que si je voulais traiter avec des setters, je pourrais utiliser une approche similaire en utilisant [BiFunction](https://docs.oracle.com/javase/8/docs/api/java/util/function/BiFunction.html) au lieu de [Function](https://docs.oracle.com/javase/8/docs/api/java/util/function/Function.html).

### Benchmark

Afin de mesurer les gains de performance, j'ai utilisé le toujours génial JMH ([Java Microbenchmark Harness](https://openjdk.java.net/projects/code-tools/jmh/)), qui fera probablement partie du [JDK 12](https://openjdk.java.net/jeps/230). Comme vous le savez peut-être, les résultats sont liés à la plateforme, donc pour référence, j'utiliserai un seul `1x6 i5-8600K 3.6GHz` et `Linux x86_64` ainsi que `Oracle JDK 8u191` et `GraalVM EE 1.0.0-rc9`.

Pour la comparaison, j'ai utilisé [Apache Commons BeanUtils](http://commons.apache.org/proper/commons-beanutils/), une bibliothèque bien connue de la plupart des développeurs Java, et l'une de ses alternatives appelée [Jodd BeanUtil](https://jodd.org/beanutil/) qui prétend être [presque 20% plus rapide](https://jodd.org/beanutil/performance.html).

Le scénario de benchmark est défini comme suit :

Le benchmark est piloté par la profondeur à laquelle nous allons récupérer une valeur selon les quatre niveaux différents spécifiés ci-dessus. Pour chaque `fieldName`, JMH effectuera 5 itérations de 3 secondes chacune pour réchauffer les choses et ensuite 5 itérations de 1 seconde chacune pour mesurer réellement. Chaque scénario sera ensuite répété 3 fois pour recueillir raisonnablement les métriques.

### Résultats

Commençons par les résultats recueillis à partir de l'exécution de `JDK 8u191` :

![Image](https://cdn-media-1.freecodecamp.org/images/1*WABW6nwa_pciOdk6v8JXTA.png)
_Oracle JDK 8u191_

Le pire scénario utilisant l'approche `invokedynamic` est beaucoup plus rapide que le scénario le plus rapide des deux autres bibliothèques. C'est une énorme différence, et si vous doutez des résultats, vous pouvez toujours télécharger le [code source](https://github.com/carlosraphael/javabeanutil-benchmark) et jouer avec comme vous le souhaitez.

Maintenant, voyons comment le même benchmark se comporte avec `GraalVM EE 1.0.0-rc9`

![Image](https://cdn-media-1.freecodecamp.org/images/1*p5UY9s_c6H_b45LLVCUnOg.png)
_GraalVM EE 1.0.0-rc9_

Les résultats complets peuvent être consultés [ici](https://jmh.morethan.io/?gist=https://gist.githubusercontent.com/carlosraphael/27723493d2161ea078e29a1f7fc15dd2/raw/5975d3b609e1c0cb14c47f7ab76e38c053be64b3/JavaBeanUtilBenchmark_result.json) avec le visualiseur JMH.

### Observations

La grande différence est due au fait que le compilateur JIT connaît très bien `CallSite` et `MethodHandle` et sait comment les intégrer en ligne assez bien contrairement à l'approche par réflexion. De plus, vous pouvez voir à quel point [GraalVM](https://www.graalvm.org/) est prometteur. Son compilateur fait un travail vraiment impressionnant, capable d'une grande amélioration des performances pour l'approche par réflexion.

Si vous êtes curieux et souhaitez aller plus loin, je vous encourage à télécharger le code source depuis mon [Github](https://github.com/carlosraphael/javabeanutil-benchmark). Gardez à l'esprit que je ne vous encourage pas à faire votre propre `JavaBeanUtil` maison et à l'utiliser en production. Plutôt, mon objectif ici est simplement de présenter mon expérience et les possibilités que nous pouvons obtenir avec `invokedynamic`.