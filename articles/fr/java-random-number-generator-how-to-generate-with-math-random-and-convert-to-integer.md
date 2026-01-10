---
title: Générateur de nombres aléatoires en Java – Comment générer des nombres avec
  Math.random() et les convertir en entiers
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-07-19T15:09:37.000Z'
originalURL: https://freecodecamp.org/news/java-random-number-generator-how-to-generate-with-math-random-and-convert-to-integer
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/java-number-generators.png
tags:
- name: Java
  slug: java
- name: Math
  slug: math
seo_title: Générateur de nombres aléatoires en Java – Comment générer des nombres
  avec Math.random() et les convertir en entiers
seo_desc: "By Sebastian Sigl\nIn many applications, you need random numbers. You might\
  \ need to throw dice in video games, create a private cryptography key, or create\
  \ a user’s temporary password. \nAll these applications depend on random number\
  \ creation. It’s som..."
---

Par Sebastian Sigl

Dans de nombreuses applications, vous avez besoin de nombres aléatoires. Vous pourriez avoir besoin de lancer des dés dans des jeux vidéo, créer une clé cryptographique privée ou générer un mot de passe temporaire pour un utilisateur. 

Toutes ces applications dépendent de la création de nombres aléatoires. Il est parfois difficile de différencier ce qu'il faut utiliser et quand, et la sécurité est un sujet complexe. Sans passer quelques années à l'étudier, il est difficile de comprendre rapidement la documentation sur les implémentations disponibles et de choisir la bonne méthode pour votre cas d'utilisation. 

Alors dans ce tutoriel, je vais résumer les cas d'utilisation les plus courants et comment choisir l'implémentation la plus performante en fonction de votre code Java.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/brainstorming---Frame-1--1-.jpg)

Dans cet article, vous apprendrez :

* Comment générer des entiers, des flottants et des booléens,
* Comment générer des nombres aléatoires pour des cas d'utilisation critiques en termes de performance,
* Comment générer des nombres aléatoires pour des cas d'utilisation critiques en termes de sécurité,
* Comment fonctionnent les générateurs de nombres,
* Les différences entre les générateurs de nombres pseudo-aléatoires et les générateurs de nombres véritablement aléatoires,
* Comment utiliser une graine à votre avantage.  


Tous les exemples de code sont minimaux, et vous pouvez trouver le code source complet sur [GitHub](https://github.com/sesigl/random-number-generators-java).

## Contraintes de Math.random()

`Math.random` existait même avant Java 6. Il est facile d'accès et toujours largement utilisé. Avec Java 17, une nouvelle interface commune appelée `RandomGenerator` est disponible, qui consolide toutes les implémentations de générateurs aléatoires dans le SDK Java actuel. 

`Math.random()` délègue simplement à `Random().nextFloat()`. Mais il ne retourne qu'un `double`. Il ne vous permet donc pas de demander différents types de nombres ou de générer des nombres dans des plages spécifiques. Il ne vous permet pas non plus de choisir parmi différentes implémentations. 

Dans les sections suivantes, vous apprendrez une génération de nombres plus flexible et comment générer des nombres optimisés pour l'efficacité ou la sécurité.

## Interface commune depuis Java 17

Avec Java 17, une interface commune est implémentée par les générateurs de nombres disponibles dans le SDK Java. Vous avez des méthodes disponibles pour tous les types de données essentiels, et vous pouvez définir la plage attendue pour laquelle vous souhaitez générer des nombres :

```java
RandomGenerator randomGenerator = new Random();

// générer un int entre 0 - 9
randomGenerator.nextInt(10);

// générer un int entre 1 - 9
randomGenerator.nextInt(1, 9);

// générer un long entre 1 - 9
randomGenerator.nextLong(1, 9);

// générer un float entre 1 - 9
randomGenerator.nextFloat(1, 9);

// générer un double entre 1 - 9
randomGenerator.nextDouble(1, 9);

// générer un booléen aléatoire
randomGenerator.nextBoolean();
```

## Génération de nombres aléatoires optimisée pour la performance dans un environnement monothread

Pour de nombreux cas non critiques en termes de sécurité, vous ne vous souciez pas de la prévisibilité de votre nombre aléatoire. Généralement, vous voulez simplement une distribution fiable. 

Des implémentations plus performantes que `Random` sont disponibles si votre application est monothread. Une alternative très efficace s'appelle `SplittableRandom` :

```java
new SplittableRandom().nextInt();
```

Le [benchmark exécuté sur un MacBook Pro comparant SplittableRandom et Random](https://github.com/sesigl/random-number-generators-java/blob/main/src/test/java/org/example/BenchmarkSingleThreadedTest.java) montre les résultats suivants :

```sh
SingleThreaded.Random  116528253,100 ops/s
SingleThreaded.SplittableRandom  619630768,299  ops/s
```

`SplittableRandom` est environ 5 fois plus rapide que `Random` dans un environnement monothread. 

Les avantages supplémentaires par rapport à `Random()` sont un comportement déterministe et une implémentation splittable fork/join. En résumé, vous devriez préférer utiliser `SplittableRandom` plutôt que `Random` dans les environnements monothread.

## Génération de nombres aléatoires optimisée pour la performance dans un environnement multithread

Les applications à haut débit utilisent plusieurs threads. Vous voulez donc utiliser un générateur de nombres conçu pour une utilisation parallèle. 

L'implémentation de `Random` est thread-safe mais relativement lente et ralentit encore plus à cause des verrous. Comme `SplittableRandom` n'est pas thread-safe, ce n'est pas une alternative ici. 

Cependant, vous obtenez de meilleures performances en utilisant `ThreadLocalRandom` dans un environnement multithread. Il utilise `SplittableRandom`, mais garantit une utilisation performante et sécurisée dans plusieurs threads :

```java
ThreadLocalRandom.current().nextInt();
```

Le [benchmark exécuté sur un MacBook Pro comparant ThreadLocalRandom et Random](https://github.com/sesigl/random-number-generators-java/blob/main/src/test/java/org/example/BenchmarkMultiThreadedTest.java) générant des nombres en parallèle en utilisant 10 threads montre les résultats suivants :

```sh
MultiThreaded   Random                      8308724,791         ops/s
MultiThreaded   ThreadLocalRandom  3537955530,922   ops/s
```

Comme vous pouvez le voir, l'utilisation de `ThreadLocalRandom` est 425 fois plus rapide. `ThreadLocalRandom` est sans verrou et, par conséquent, plus performant que la classe `Random` thread-safe.

## Génération de nombres aléatoires optimisée pour la sécurité

Les méthodes que nous venons de discuter sont rapides et suffisantes pour la plupart de vos applications. Mais elles créent ce que l'on appelle des nombres pseudo-aléatoires.

Au lieu de toujours créer un nombre véritablement aléatoire, elles prédisent un nouveau nombre basé sur le nombre précédemment prédit, ce qui implique un état et un sérieux problème de prévisibilité. 

Peut-être souhaitez-vous créer des secrets à longue durée de vie pour le chiffrement, et vous ne voulez pas que d'autres puissent, par hasard, prédire le prochain jeton généré. 

En Java, vous avez `SecureRandom` pour des cas d'utilisation plus critiques en termes de sécurité :

```java
SecureRandom.getInstanceStrong().nextInt();
```

`SecureRandom.getInstanceStrong()` vous donne un fournisseur qui crée des jetons sécurisés. Dans de nombreux systèmes Linux, vous utilisez `/dev/random`, générant des nombres basés sur le bruit aléatoire de dispositifs réels. 

Cependant, si vous n'avez pas assez de données aléatoires collectées, ce que l'on appelle l'[entropy](https://en.wikipedia.org/wiki/Entropy) manquante, l'exécution peut bloquer et prendre un temps inattendu. Surtout dans les machines avec beaucoup de conteneurs Docker, cela peut conduire à une exécution lente en pratique.

En alternative, `new SecureRandom()` ne bloque pas par défaut en cas d'absence d'entropie. Il utilise également une méthode moins sécurisée de génération de nombres comme solution de repli.

## Comment utiliser les graines à votre avantage

Par défaut, un générateur de nombres pseudo-aléatoires utilise une graine aléatoire, qui reflète les valeurs de départ utilisées pour générer des valeurs. Une graine est donc très pratique pour les tests, car elle vous donne le contrôle sur les prédictions et vous permet de réinitialiser la manière dont les nombres sont créés. 

Jusqu'à présent, nous n'avons pas parlé de quoi que ce soit en relation avec les graines.

```java
@Test
   public void splittableRandomWithSeedIsDeterministic() {
   assertEquals(new SplittableRandom(9999).nextInt(), -788346102);
}

@Test
   public void randomWithSeedIsDeterministic() {
   assertEquals(new Random(9999).nextInt(), -509091100);
}
```

Cela facilite grandement les tests. Sinon, vous devriez toujours [simuler les dépendances](https://site.mockito.org/). 

## Pourquoi la génération de nombres est difficile

Comprendre pourquoi la génération de nombres est difficile pour avoir un sentiment de sécurité est essentiel. 

Les ingénieurs écrivent du code, qui est finalement compilé en code lisible par machine exécuté dans une unité de traitement réelle (CPU). Une CPU est construite sur des circuits électroniques, qui consistent en des portes logiques. 

En résumé, il n'y a pas de véritable aléatoire que vous pouvez créer avec un ordinateur traditionnel car la sortie nécessite une certaine entrée et, par définition, cela ne peut pas être aléatoire. 

Cela signifie que vous avez besoin d'une sorte d'entrée véritablement aléatoire provenant du monde réel, comme le [bruit thermique](https://en.wikipedia.org/wiki/Johnson-Nyquist_noise) d'une [résistance](https://en.wikipedia.org/wiki/Resistor). Il existe des générateurs de nombres matériels coûteux qui utilisent la physique du monde réel pour vous offrir une grande capacité de création de nombres aléatoires.

## Risques de la génération de nombres aléatoires non sécurisée

Bien que de nombreux protocoles soient sécurisés par conception, ils ne le sont pas si un attaquant peut prédire les clés de chiffrement. 

De nos jours, de nombreuses applications nécessitent une génération de nombres véritablement aléatoires en arrière-plan. Sinon, les attaquants pourraient être capables de prédire les nombres générés et, ce faisant, infiltrer les applications. 

Par exemple, les avancées en matière de traitement de la sécurité basées sur l'informatique quantique peuvent représenter une réelle menace si soudainement les attaquants peuvent résoudre les chiffrements en un rien de temps.

## Résumé

Dans cet article de blog, vous avez appris comment générer des nombres en Java de manière efficace. Vous avez également appris comment optimiser pour la performance ou la sécurité, et vous avez appris ce qu'est une graine et comment elle peut être utilisée. 

De plus, vous devriez maintenant comprendre les différences clés entre les nombres pseudo-aléatoires et véritablement aléatoires, et vous devriez être capable de décrire pourquoi la génération de nombres aléatoires sécurisés est importante.

J'espère que vous avez apprécié l'article.

Si vous l'avez aimé et que vous avez envie de m'applaudir ou simplement de prendre contact, [suivez-moi sur Twitter](https://twitter.com/sesigl).

Au fait, [nous recrutons](https://www.ebay-kleinanzeigen.de/careers) !

### Références

* [https://betterprogramming.pub/generating-random-numbers-is-a-lot-harder-than-you-think-b121c3e75d08](https://betterprogramming.pub/generating-random-numbers-is-a-lot-harder-than-you-think-b121c3e75d08)
* [https://docs.oracle.com/javase/8/docs/api/java/security/SecureRandom.html](https://docs.oracle.com/javase/8/docs/api/java/security/SecureRandom.html)
* [https://www.happycoders.eu/java/random-number/](https://www.happycoders.eu/java/random-number/)
* [https://www.baeldung.com/java-17-random-number-generators](https://www.baeldung.com/java-17-random-number-generators)
* [https://programmer.ink/think/61db978dde30a.html](https://programmer.ink/think/61db978dde30a.html)
* [https://www.baeldung.com/java-secure-random](https://www.baeldung.com/java-secure-random)
* [https://tersesystems.com/blog/2015/12/17/the-right-way-to-use-securerandom/](https://tersesystems.com/blog/2015/12/17/the-right-way-to-use-securerandom/)
* [https://en.wikipedia.org/wiki//dev/random](https://en.wikipedia.org/wiki//dev/random)
* [https://www.schutzwerk.com/en/43/posts/attacking_a_random_number_generator/](https://www.schutzwerk.com/en/43/posts/attacking_a_random_number_generator/)
* [https://en.wikipedia.org/wiki/Random_number_generator_attack](https://en.wikipedia.org/wiki/Random_number_generator_attack)