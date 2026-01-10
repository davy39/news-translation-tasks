---
title: Tests unitaires AppEngine simplifiés avec JUnit Rules
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-26T11:50:44.000Z'
originalURL: https://freecodecamp.org/news/appengine-unit-testing-made-easy-with-junit-rules-97c2127a161a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*V2EDFPlZSdQQSVyKn6I68w.png
tags:
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Testing
  slug: testing
seo_title: Tests unitaires AppEngine simplifiés avec JUnit Rules
seo_desc: 'By Ramesh Lingappa

  Hello there! If you are using AppEngine for hosting your application, then you will
  be using one or more of their services like Datastore, Memcache, TaskQueues, UserService,
  etc.

  And you will be needing to write unit tests to make ...'
---

Par Ramesh Lingappa

Bonjour ! Si vous utilisez AppEngine pour héberger votre application, alors vous utiliserez un ou plusieurs de leurs services comme Datastore, Memcache, TaskQueues, UserService, etc.

Et vous aurez besoin d'écrire des tests unitaires pour vous assurer que la fonctionnalité de votre application fonctionne comme prévu avec ces services. Pour cela, vous devez configurer certaines configurations pour tester ces services dans votre environnement local.

Si vous êtes nouveau dans les tests de services AppEngine, Google propose une excellente documentation sur la façon de configurer cette configuration avec des codes d'exemple. Jetez un œil à [Local Unit Testing for Java](https://cloud.google.com/appengine/docs/standard/java/tools/localunittesting).

Par exemple, voici un exemple de code de Google pour effectuer des tests de datastore :

C'est génial. La plupart du temps, nos services utiliseront plusieurs services AppEngine comme Memcache pour les entités (Objectify), la mise en file d'attente des tâches après avoir sauvegardé une entité. Le vrai point de douleur vient lorsque nous essayons de configurer plusieurs configurations.

D'accord, c'est beaucoup de configuration, mais devinez quoi — ce n'est pas tout. Que se passe-t-il si vous devez changer des paramètres spécifiques pour certains tests comme _High Replication_, _Queue XML Path_, ou _Current User_ ? Alors votre configuration sera encore plus complexe. Et vous devez répéter tout cela pour chaque classe de test unitaire.

Oh, au fait, avez-vous oublié la configuration de test [Objectify](https://github.com/objectify/objectify) ? Jetez un œil à [Objectify Unit Testing](https://stackoverflow.com/questions/32628124/how-to-use-objectifyservice-in-junit-testing).

Vous pourriez penser,

> « Configurons toutes ces configurations dans la classe parente et chaque classe de test unitaire étendra celle-ci »

Nous pouvons faire cela, mais il y a un autre problème avec cela :

**Chacun de ces services est coûteux à créer. Vous devez configurer l'environnement en utilisant uniquement les services dont vous avez besoin.**

Ainsi, configurer inutilement tous les services ralentira probablement le temps d'exécution des tests.

#### D'accord, y a-t-il un sauveur ?

Oui, [Junit Rules](https://github.com/junit-team/junit4/wiki/rules) vient à la rescousse !

> « Les règles permettent une addition ou une redéfinition très flexible du comportement de chaque méthode de test dans une classe de test. Les testeurs peuvent réutiliser ou étendre l'une des règles fournies ci-dessous, ou écrire les leurs »

Il existe de nombreux articles sur Junit Rules — veuillez les consulter.

Ainsi, avec les règles JUnit, nous sommes en mesure de configurer les dépendances externes avant l'exécution des tests de manière simple. Avec quelques ajustements, nous pouvons configurer les services liés à AppEngine par classe de la manière souhaitée. Voici un exemple :

Ici, **AppEngineRule** est une classe simple qui étend **ExternalResource** et a été créée en utilisant un modèle de construction. Nous pouvons configurer les services dont nous avons besoin, et si vous regardez dans **_SampleTestClass_**, nous pouvons faire toute la configuration en une seule ligne.

```
@Rule    public final AppEngineRule rule = AppEngineRule.builder()             .withDatastore()             .withQueue()             .build();
```

Et la classe _AppEngineRule_ remplace les méthodes `before` et `after` pour configurer les fonctionnalités de configuration et de nettoyage d'AppEngine. Vous pouvez également configurer de manière similaire pour chaque classe de test avec uniquement les services requis.

#### Est-ce tout ? Peut-on faire mieux ?

Bien sûr que nous pouvons ! Pour rendre cette configuration facile, vous devez écrire quelque chose de similaire à la classe _AppEngineRule_ avec tout le code de configuration standard.

Voici une bonne nouvelle : vous n'avez pas besoin d'écrire quoi que ce soit. J'ai créé une petite bibliothèque avec toutes les implémentations de configuration nécessaires pour tous les services et avec encore plus d'options configurables.

[**ramesh-dev/gae-test-util-java**](https://github.com/ramesh-dev/gae-test-util-java)  
[_Google AppEngine Java Utility Library. Contribute to ramesh-dev/gae-test-util-java development by creating an account…github.com](https://github.com/ramesh-dev/gae-test-util-java)

Dans votre script de construction, ajoutez simplement la dépendance, par exemple dans gradle :

```
testCompile 'com.github.ramesh-dev:gae-test-util-java:0.3'
```

Avec cela, nous pouvons avoir des configurations flexibles comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/1*PEm-JvZu6NKFKq_AY7VoPA.png)
_Image téléchargée depuis internet_

### Conclusion

Ainsi, Junit Rules est une option pratique pour configurer facilement nos dépendances externes, même pour des services complexes comme AppEngine. Vous pouvez également avoir d'autres règles et les enchaîner dans un ordre spécifique en utilisant [Rule Chain](https://github.com/junit-team/junit4/wiki/rules#rulechain)

Merci d'avoir lu et cette fois, **Bon Tests…**

#### Références

* [https://github.com/junit-team/junit4/wiki/rules](https://github.com/junit-team/junit4/wiki/rules)
* [https://cloud.google.com/appengine/docs/standard/java/tools/localunittesting](https://cloud.google.com/appengine/docs/standard/java/tools/localunittesting)
* [https://github.com/ramesh-dev/gae-test-util-java](https://github.com/ramesh-dev/gae-test-util-java)