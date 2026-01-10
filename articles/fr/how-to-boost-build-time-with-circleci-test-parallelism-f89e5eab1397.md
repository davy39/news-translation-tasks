---
title: Comment accélérer le temps de construction avec le parallélisme des tests CircleCI
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-03T17:21:59.000Z'
originalURL: https://freecodecamp.org/news/how-to-boost-build-time-with-circleci-test-parallelism-f89e5eab1397
coverImage: https://cdn-media-1.freecodecamp.org/images/0*Xw31bEh4xGoWbmx_.png
tags:
- name: Continuous Integration
  slug: continuous-integration
- name: gradle
  slug: gradle
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment accélérer le temps de construction avec le parallélisme des tests
  CircleCI
seo_desc: 'By Karel Rochelt

  Providing an error-free API for a heavily developed project is not an easy task.
  Likely, the first things that come to mind are tests. For a mid-sized API, you may
  write hundreds or even thousands of end-to-end tests. These tests sig...'
---

Par Karel Rochelt

Fournir une API sans erreur pour un projet en développement intensif n'est pas une tâche facile. Probablement, les premières choses qui viennent à l'esprit sont les tests. Pour une API de taille moyenne, vous pouvez écrire des centaines, voire des milliers de tests de bout en bout. Ces tests prolongent considérablement les temps de construction.

Dans cet article, nous allons expliquer comment nous avons résolu les longs temps de construction avec le parallélisme des tests CircleCI et Gradle/Grails pour le service principal d'[Amio](https://amio.io).

### Configuration de CircleCI

La [documentation](https://circleci.com/docs/2.0/parallelism-faster-jobs/) de CircleCI fait un bon travail pour expliquer comment leur outil [d'interface de ligne de commande](https://circleci.com/docs/2.0/local-cli/) (CLI) doit être utilisé pour activer le parallélisme des tests. Lorsque j'ai commencé à m'y intéresser pour la première fois, il n'était pas entièrement évident de savoir à quoi ressemblerait le résultat retourné. Je me demandais, « Donc, je vais exécuter cette commande et elle va magiquement commencer à diviser mes tests ? » Eh bien, bien sûr que non ! Le résultat est une liste de fichiers de test qui doivent être exécutés sur un conteneur particulier.

Cela semble compliqué ? Laissez-moi expliquer avec un exemple.

La première chose que nous devons faire est de définir la clé de parallélisme dans le fichier `.circleci/config.yml`. D'après la documentation de CircleCI :

> La clé `_parallelism_` spécifie combien d'exécuteurs indépendants seront configurés pour exécuter les étapes d'un travail.

Toute valeur supérieure à un permettra une exécution parallèle, mais pour les besoins de cet exemple, utilisons deux. De cette façon, chaque fois qu'un travail CircleCI est démarré, il créera deux conteneurs qui effectueront tous deux les mêmes tâches.

Si nous devions utiliser la clé de parallélisme sans configuration supplémentaire, elle exécuterait simplement tous nos tests deux fois. Ce n'est pas ce que nous voulons. Nous voulons diviser nos tests entre les conteneurs.

C'est là que l'interface de ligne de commande de CircleCI intervient. Elle offre deux commandes qui, lorsqu'elles sont utilisées ensemble, divisent nos tests en portions égales entre nos deux conteneurs.

Disons que ce sont les fichiers de test dans notre projet :

```
src/integration-test/groovy/com/package1/Test1.groovysrc/integration-test/groovy/com/package1/Test2.groovysrc/integration-test/groovy/com/package2/Test3.groovysrc/integration-test/groovy/com/package2/Test4.groovysrc/integration-test/groovy/com/package2/Test5.groovy
```

Naturellement, nous aurons d'autres fichiers sources dans notre projet ; pas seulement nos tests. Ils peuvent être situés dans le même répertoire `src/integration-test/...`. Pour atteindre notre objectif de division des tests, nous devons sélectionner uniquement les fichiers de test pour le projet. Cela se fait en utilisant la commande [glob](https://circleci.com/docs/2.0/parallelism-faster-jobs/#globbing-test-files) :

```
circleci tests glob "src/integration-test/**/*.groovy"
```

Cette commande affichera la liste de nos tests (tous les 5). Maintenant, nous utilisons la commande split pour, eh bien, les [diviser](https://circleci.com/docs/2.0/parallelism-faster-jobs/#splitting-test-files) entre les conteneurs :

```
circleci tests glob "src/integration-test/**/*.groovy" | circleci tests split --split-by=timings
```

La commande `split` offre plusieurs stratégies pour diviser les tests, mais `timings` est ma préférée. Elle utilise les données de timing qui sont collectées par CircleCI (cela doit être activé via la clé [store_test_results](https://circleci.com/docs/2.0/configuration-reference/#store_test_results)) pour diviser les tests en portions qui prennent un temps similaire à exécuter. L'indexation des conteneurs est automatique. Nous pouvons exécuter la même commande sur chaque conteneur. Dans notre exemple, l'exécution de la commande sur le Conteneur 0 pourrait afficher :

```
src/integration-test/groovy/com/package1/Test1.groovysrc/integration-test/groovy/com/package2/Test3.groovy
```

Et sur le Conteneur 1 :

```
src/integration-test/groovy/com/package1/Test2.groovysrc/integration-test/groovy/com/package2/Test4.groovysrc/integration-test/groovy/com/package2/Test5.groovy
```

Je dis « pourrait » parce que le résultat réel dépendrait des données de timing. Comme vous pouvez le voir, chaque conteneur a obtenu sa moitié des tests.

### Configuration de Gradle

Diviser les tests dans CircleCI était la partie facile. La partie difficile est de faire en sorte que Gradle exécute uniquement les tests qui sont dans le résultat de la commande split. Si nous utilisions JavaScript et Mocha, ce serait beaucoup plus facile. Mocha accepte une liste de fichiers qui doivent être exécutés. Avec Gradle 3, j'avais utilisé cette commande pour exécuter les tests : `./gradlew check -i`

La [documentation](https://docs.gradle.org/current/userguide/gradle_wrapper.html) de Gradle n'est pas vraiment utile. Juste comprendre ce que fait la tâche check est une douleur. Heureusement, il est possible de passer notre liste de tests en tant que paramètre à la tâche Gradle.

```
./gradlew check -i -PtestFilter="`circleci tests glob "src/integration-test/**/*.groovy" | circleci tests split --split-by=timings`"
```

Maintenant, lorsque la tâche `check` est démarrée, elle a accès au paramètre `testFilter`. Pour que tout fonctionne, nous devons également ajouter du code qui peut gérer le paramètre dans notre **build.gradle** :

```
integrationTest {  if (project.hasProperty("testFilter")) {    List<String> props = project.getProperties().get("testFilter").split("\\s+")    props.each {      include(it.replace("src/integration-test/groovy/com/", "**/").replace(".groovy", ".class"))    }  }}
```

Notez que le paramètre a été passé à la tâche sous forme de chaîne unique. Dans le bloc de code ci-dessus, la ligne 3 contient la logique pour le diviser à nouveau en lignes. L'appel à include indiquera à Gradle d'exécuter uniquement les tests que nous incluons. Maintenant, nous pouvons inclure toutes les lignes, et nous sommes bons, n'est-ce pas ?

Non. Gradle ne sait pas comment travailler avec les fichiers sources. Il ne comprend que les classes. Nous devons lui passer les fichiers de classe compilés.

Il y a deux problèmes avec cela. Premièrement, les classes compilées ne sont pas dans le même répertoire. Deuxièmement, le suffixe n'est pas .groovy mais .class.

Pour surmonter le premier problème, nous avons remplacé le préfixe commun par **/. Cela dit, « Regardez dans le répertoire racine et tous ses sous-répertoires. » Bien sûr, vous pourriez le remplacer par quelque chose comme `build/classes/integrationTest/com`. C'est plus propre, mais pas nécessaire. Cela devrait être sûr tant que les noms des classes de test sont uniques. La ligne 5 dans le bloc de code ci-dessus inclut la logique qui résout ces deux problèmes.

En fin de compte, votre `.circleci/config.yml` devrait ressembler à ceci (juste la partie pertinente) :

```
- run:    # Ceci est juste à des fins de débogage, vous pouvez omettre cette étape    name: test splitting output    command: circleci tests glob "src/integration-test/**/*.groovy" | circleci tests split --split-by=timings | xargs -n 1 echo
```

```
- run:    name: test    command: ./gradlew check -i -PtestFilter="`circleci tests glob "src/integration-test/**/*.groovy" | circleci tests split --split-by=timings`"
```

### Conclusion

Et c'est tout ! Facile, n'est-ce pas ? Eh bien, cela a été un peu plus de travail que cela n'aurait dû être. Avoir nos temps de test réduits de près de moitié en valait définitivement la peine ! En appliquant le parallélisme des tests, nous avons réduit le temps de construction d'environ 15 minutes à 9 minutes.

![Image](https://cdn-media-1.freecodecamp.org/images/5Pn6DOPH8BS02ki3faCRXcsui9ZE1x9jRnp4)