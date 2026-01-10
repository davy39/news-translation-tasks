---
title: Vous pouvez enfin déclarer des variables locales de type inféré en Java avec
  var — voici pourquoi c'est génial
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-27T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/you-can-finally-declare-local-variables-in-java-with-var-heres-why-that-s-awesome-4418cb7e2da3
coverImage: https://cdn-media-1.freecodecamp.org/images/0*sJnvQ7q-_Vd6XVUa
tags:
- name: coding
  slug: coding
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: Vous pouvez enfin déclarer des variables locales de type inféré en Java
  avec var — voici pourquoi c'est génial
seo_desc: 'By javinpaul

  Hello everyone! In this article, I’ll discuss new features of Java 10. Specifically,
  I am going to talk about probably the most popular and most useful: the introduction
  of the var keyword in Java. Well, it’s not really a keyword — but I...'
---

Par javinpaul

Bonjour à tous ! Dans cet article, je vais discuter des nouvelles fonctionnalités de **Java 10**. Plus précisément, je vais parler de la fonctionnalité probablement la plus populaire et la plus utile : l'**introduction du mot-clé var en Java**. Eh bien, ce n'est pas vraiment un mot-clé — mais je vous en parlerai plus tard.

### Enfin...

Enfin, Java a obtenu le mot-clé **var** pour déclarer des **variables locales**. Cela vous permet de déclarer une variable sans son type. Par exemple, au lieu de faire ceci :

`String str = "Java"`

vous pouvez maintenant simplement dire ceci :

`var str = "Java".`

Cela peut ne pas sembler beaucoup lorsque vous déclarez une variable String ou int, mais pensez aux types complexes avec des génériques, par exemple. Cela permettra certainement d'économiser beaucoup de frappe et améliorera également la lisibilité du code.

#### Un peu de contexte

Les développeurs Java se plaignent depuis longtemps du code boilerplate et des cérémonies impliquées lors de l'écriture de code. De nombreuses choses qui prennent seulement 5 minutes dans des langages comme [Python](http://javarevisited.blogspot.sg/2018/03/top-5-courses-to-learn-python-in-2018.html), [Groovy](http://javarevisited.blogspot.sg/2017/08/top-5-books-to-learn-groovy-for-java.html), ou [JavaScript](http://javarevisited.blogspot.sg/2017/02/top-5-javascript-books-to-learn-best-of-lot-must-read.html) peuvent prendre plus de 30 minutes en Java en raison de sa verbosité.

Si vous avez codé en Scala, Kotlin, Go, C# ou tout autre [langage JVM](https://javarevisited.blogspot.com/2018/02/top-3-jvm-languages-java-programmer-learn.html), alors vous savez qu'ils ont tous une sorte d'inférence de type de variable locale déjà intégrée dans le langage.

Par exemple, JavaScript a **let** et **var**, [Scala](http://javarevisited.blogspot.sg/2018/01/10-reasons-to-learn-scala-programming.html#axzz550Ppgfxg) et [Kotlin](http://www.java67.com/2017/12/10-programming-languages-to-learn-in.html) ont **var** et **val**, C++ a **auto**, C# a **var**, et Go supporte cela par déclaration avec l'opérateur **:=**.

Jusqu'à [Java 10](http://javarevisited.blogspot.sg/2018/03/java-10-released-10-new-features-java.html), Java était le seul langage qui n'avait pas d'inférence de type de variable locale ou de support pour le mot-clé var.

Bien que l'inférence de type ait été grandement améliorée dans Java 8 avec l'introduction des expressions lambda, des références de méthode et des Streams, les variables locales devaient encore être déclarées avec un type approprié. Mais cela appartient désormais au passé ! [Java 10](http://javarevisited.blogspot.sg/2018/03/java-10-released-10-new-features-java.html#axzz5ALJyiIAt) dispose d'une fonctionnalité, [**JEP 286 : Local-Variable Type Inference**](http://openjdk.java.net/jeps/286), qui permettra de déclarer des variables locales sans information de type et en utilisant simplement le mot-clé var.

Examinons cela de plus près.

### Exemples du mot-clé var de Java 10

Voici quelques exemples du mot-clé var de Java 10 :

```
var str = "Java 10"; // infère String
```

```
var list = new ArrayList<String>(); // infère ArrayList<String>
```

```
var stream = list.stream(); // infère Stream<String>
```

Comme je l'ai dit, à ce stade, vous ne pouvez peut-être pas pleinement apprécier ce que var fait pour vous. Mais regardez l'exemple suivant :

```
var list = List.of(1, 2.0, "3")
```

Ici, la liste sera inférée en **List<? extends Serializable & Comparable<?>>** qui est un type d'intersection, mais vous n'aurez pas à taper les informations de type complètes. var rend le code beaucoup plus facile à écrire et à lire dans ce cas.

Dans la section suivante, nous verrons d'autres exemples qui vous aideront à apprendre comment écrire du code concis en utilisant var dans Java 10.

### Écrire du code concis en utilisant le mot-clé var en Java

L'utilisation du mot réservé var rend également votre code concis en réduisant la duplication — par exemple, le nom de la classe qui apparaît à la fois à droite et à gauche des affectations comme montré dans l'exemple suivant :

```
ByteArrayOutputStream bos = new ByteArrayOutputStream();
```

Ici, [ByteArrayOutputStream](https://docs.oracle.com/javase/10/docs/api/java/io/ByteArrayOutputStream.html) se répète deux fois, et nous pouvons éliminer cela en utilisant la fonctionnalité var de Java 10 comme montré ci-dessous :

```
var bos = new ByteArrayOutputStream();
```

Nous pouvons faire des choses similaires lors de l'utilisation des instructions [try-with-resource](https://javarevisited.blogspot.com/2011/09/arm-automatic-resource-management-in.html) en Java, par exemple ceci

```
try (Stream<Book> data = dbconn.executeQuery(sql)) {    return data.map(...) .filter(...) .findAny(); }
```

peut être écrit comme suit :

```
try (var books = dbconn.executeQuery(query)) {   return books.map(...) .filter(...) .findAny(); }
```

Ce ne sont que quelques exemples. Il y a beaucoup d'endroits où vous pouvez utiliser var pour rendre votre code plus concis et lisible, dont beaucoup peuvent être vus dans le cours Pluarlsight de Sander [**Quoi de neuf dans Java 10**](https://pluralsight.pxf.io/c/1193463/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Fwhats-new-java-10-local-variable-type-inference).

C'est un cours payant, mais vous pouvez essayer cet [essai gratuit de 10 jours](http://pluralsight.pxf.io/c/1193463/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Flearn).

![Image](https://cdn-media-1.freecodecamp.org/images/unYRUbTTXMNdA-id-rw25UbXpaksermD2GOc)

Pour les programmeurs qui ont utilisé [Groovy](http://javarevisited.blogspot.sg/2016/09/10-basic-differences-between-java-and-groovy-programming.html#axzz5ArdIFI7y) ou [Scala](http://javarevisited.blogspot.sg/2017/12/top-5-courses-to-learn-big-data-and.html#axzz5ArdIFI7y), l'introduction de var donne l'impression que Java prend la direction de Scala... mais seul le temps nous le dira.

Pour l'instant, nous pouvons simplement être heureux que **var facilite la déclaration d'une variable locale complexe en Java 10.**

Et notez bien : l'inférence de type de variable locale du mot-clé var de Java 10 ne peut être utilisée que pour déclarer des [variables locales](http://javarevisited.blogspot.sg/2012/02/difference-between-instance-class-and.html#axzz5ArdIFI7y) (par exemple, toute variable à l'intérieur du corps de la méthode ou du bloc de code).

### Peut-on utiliser var pour déclarer des variables membres en Java ?

Vous **ne pouvez pas** utiliser var pour déclarer des variables membres à l'intérieur de la classe, des paramètres formels de méthode ou du type de retour des méthodes.

Par exemple, cet exemple de var est correct :

```
public void aMethod(){ var name = "Java 10"; } 
```

Mais l'exemple suivant n'est **pas correct** :

```
class aClass{   var list; // erreur de compilation }
```

Ainsi, même si cette [nouvelle fonctionnalité de Java 10](https://pluralsight.pxf.io/c/1193463/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Fwhats-new-java-10-local-variable-type-inference) est accrocheuse et semble bien, elle a encore un long chemin à parcourir. Néanmoins, vous pouvez commencer à l'utiliser pour simplifier davantage votre code. Moins de code boilerplate signifie toujours un meilleur code et plus lisible.

### Points importants concernant ce nouveau mot-clé var

Maintenant que vous savez que vous pouvez déclarer des variables locales sans déclarer le type dans Java 10, il est temps d'apprendre quelques choses importantes sur cette fonctionnalité avant de commencer à l'utiliser dans votre code de production :

1. Cette fonctionnalité est construite sous **JEP 286 : Local-Variable Type Inference** et a été écrite par nul autre que [Brian Goetz](https://www.freecodecamp.org/news/you-can-finally-declare-local-variables-in-java-with-var-heres-why-that-s-awesome-4418cb7e2da3/undefined). Il est l'auteur de [Java Concurrency in Practice](http://www.amazon.com/dp/0321349601/?tag=javamysqlanta-20), l'un des livres les plus populaires pour les développeurs Java.

2. Le mot-clé var permet l'inférence de type de variable locale, ce qui signifie que le type de la [variable locale](https://javarevisited.blogspot.com/2012/02/difference-between-instance-class-and.html) sera inféré par le compilateur. Maintenant, vous n'avez plus besoin de le déclarer.

3. L'inférence de type de variable locale ou le mot-clé var de Java 10 ne peut être utilisé que pour déclarer des **variables locales**, par exemple à l'intérieur des méthodes, dans les blocs de code d'initialisation, les index dans la [boucle for améliorée](http://javarevisited.blogspot.sg/2017/01/difference-between-for-loop-and-enhanced-forlop-in-java.html#axzz4pp42TeHu), les [expressions lambda](http://www.java67.com/2017/06/10-points-about-lambda-expressions-in-java-8.html), et les variables locales déclarées dans une boucle for traditionnelle.

Vous ne pouvez pas l'utiliser pour déclarer des variables formelles et des types de retour de méthodes, pour déclarer des variables membres ou des champs, sur des variables formelles de constructeur, et tout autre type de déclaration de variable.

4. Malgré l'introduction de var, Java reste un langage typé statiquement et il doit y avoir suffisamment d'informations pour inférer le type de la variable locale. Sinon, le compilateur générera une erreur.

5. Le mot-clé var est similaire au mot-clé auto de C++, var de C#, [JavaScript](http://javarevisited.blogspot.sg/2018/01/top-10-udemy-courses-for-java-and-web-developers.html), [Scala](http://javarevisited.blogspot.sg/2017/03/top-30-scala-and-functional-programming.html), [Kotlin](http://javarevisited.blogspot.sg/2018/02/5-courses-to-learn-kotlin-programming-java-android.html), def de [Groovy](http://javarevisited.blogspot.sg/2018/02/top-3-jvm-languages-java-programmer-learn.html#axzz56WXxxAC0) et [Python](http://www.java67.com/2018/02/5-free-python-online-courses-for-beginners.html) (dans une certaine mesure), et l'opérateur := du langage de programmation Go.

6. Une chose importante à savoir est que, même si var ressemble à un mot-clé, ce n'est pas vraiment un mot-clé. Au lieu de cela, c'est un nom de type réservé. Cela signifie que le code qui utilise var comme variable, méthode ou nom de package ne sera pas affecté.

7. Une autre chose à noter est que le code qui utilise var comme nom de classe ou d'interface sera affecté par ce changement de Java 10. Mais comme le dit JEP, ces noms sont rares en pratique, car ils violent les conventions de nommage habituelles.

8. L'équivalent [immutable](http://javarevisited.blogspot.sg/2018/02/java-9-example-factory-methods-for-collections-immutable-list-set-map.html) des variables locales ou des variables finales val et let n'est pas encore supporté dans Java 10.

### Conclusion

C'est tout sur **var dans Java 10 !** C'est une fonctionnalité intéressante de Java 10, qui vous permet de déclarer des variables locales sans déclarer leur type. Cela aidera également les développeurs Java à apprendre rapidement d'autres langages, comme [Python](https://javarevisited.blogspot.com/2018/05/10-reasons-to-learn-python-programming.html), [Scala](https://javarevisited.blogspot.com/2018/01/10-reasons-to-learn-scala-programming.html#axzz550Ppgfxg), ou [Kotlin](https://hackernoon.com/should-android-developers-learn-kotlin-or-java-ee391902736f), car ils utilisent largement var pour déclarer des variables mutables et val pour déclarer des variables locales immutables.

Bien que **JEP 286 : Local-Variable Type Inference** ne supporte que **var** et non **val**, il est toujours utile et donne l'impression de coder en Scala dans Java.

#### **Pour aller plus loin**

[Quoi de neuf dans Java 10 par Sander Mak](https://pluralsight.pxf.io/c/1193463/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Fwhats-new-java-10-local-variable-type-inference)
[Guide de style pour l'inférence de type de variable locale en Java](http://openjdk.java.net/projects/amber/LVTIstyle.html)
[JEP 286 : Local-Variable Type Inference](http://openjdk.java.net/jeps/286)
[10 choses que les développeurs Java devraient apprendre en 2018](http://javarevisited.blogspot.sg/2017/12/10-things-java-programmers-should-learn.html#axzz53ENLS1RB)
[The Complete Java MasterClass pour mieux apprendre Java](https://click.linksynergy.com/fs-bin/click?id=JVFxdTr9V80&subid=0&offerid=323058.1&type=10&tmpid=14538&RD_PARM1=https%3A%2F%2Fwww.udemy.com%2Fjava-the-complete-java-developer-course%2F)

Merci d'avoir lu cet article. Si vous aimez cette **nouvelle fonctionnalité de Java 10**, alors veuillez la partager avec vos amis et collègues.

Si vous avez des questions ou des commentaires, n'hésitez pas à laisser un message et restez à l'écoute pour plus de tutoriels et d'articles sur Java 10 ici.

_Publié à l'origine sur [javarevisited.blogspot.com](https://javarevisited.blogspot.com/2018/03/finally-java-10-has-var-to-declare-local-variables.html) le 27 mars 2018._