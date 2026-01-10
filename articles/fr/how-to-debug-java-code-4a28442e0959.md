---
title: Mes techniques de débogage Java préférées
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-06T11:18:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-debug-java-code-4a28442e0959
coverImage: https://cdn-media-1.freecodecamp.org/images/1*E5604TZJQHsu3Yn6jXYPFA.jpeg
tags:
- name: debugging
  slug: debugging
- name: Java
  slug: java
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Mes techniques de débogage Java préférées
seo_desc: 'By Bhuvan Gupta

  This article is about techniques which I have used to debug codeBases of various
  kinds, such as:


  CodeBase with high concurrent nature.

  CodeBase with a lot of proprietary (unsupported) libraries.

  CodeBase with a lot of deprecated/unwa...'
---

Par Bhuvan Gupta

Cet article traite des techniques que j'ai utilisées pour déboguer des bases de code de divers types, telles que :

1. Base de code avec une nature très concurrente.
2. Base de code avec beaucoup de bibliothèques propriétaires (non supportées).
3. Base de code avec beaucoup de code obsolète/indésirable.
4. Base de code avec des fuites de mémoire.
5. Base de code où chaque JVM peut communiquer avec chaque autre JVM.

Alors, examinons-les une par une.

#### **Base de code avec une nature très concurrente.**

Il peut arriver que pour servir une requête, la JVM utilise de nombreux threads, par exemple :

```
Req -> tomcatThread-1 -> executorThread-2 -> BizThread-3->…
```

Supposons que nous trouvons que l'exception provient de BizThread-3. En tant que débogueur, nous voulons comprendre le flux de la requête. Mais la stacktrace ne pourra pas fournir le flux complet de la requête (par exemple, ce qui s'est passé dans **executorThread-2** et ce qui s'est passé dans **tomcatThread-1**, etc.).

**Technique 1.1 :** Écrivez un [**agent Java personnalisé**](https://www.baeldung.com/java-instrumentation) qui sera utilisé pour ajouter efficacement `log.debug()` au début et à la fin de chaque méthode de certains packages Java. Cela nous donnera un aperçu de ce qui est appelé.

**Technique 1.2 :** Dans certains frameworks, si supporté, utilisez [**AOP**](https://www.journaldev.com/2583/spring-aop-example-tutorial-aspect-advice-pointcut-joinpoint-annotations) pour proxifier toutes les méthodes et ajouter efficacement `log.debug()`.

#### **Base de code avec beaucoup de bibliothèques propriétaires (non supportées).**

Parfois, nous nous retrouvons dans une situation où, après des heures de débogage, nous identifions que la bibliothèque _xyz-gov-secret_ se comporte mal et que cette bibliothèque n'est plus supportée.

**Technique 2.1 :** Retroussez vos manches et installez [**eclipse-decompiler**](https://marketplace.eclipse.org/content/enhanced-class-decompiler) et plongez dans la base de code.

#### **Base de code avec beaucoup de code obsolète/indésirable.**

C'est un classique : nous nous retrouvons parfois dans une méthode de 500+ lignes avec des tonnes de conditions if-else obsolètes. Maintenant, comment déterminer le flux de code pour un appel particulier, quelles conditions if-else vont être utilisées, et quel est le code mort ?

**Technique 3.1 :** Nous pouvons utiliser un outil appelé [**jacoco agent**](https://www.eclemma.org/jacoco/trunk/doc/agent.html). Il collecte les détails d'exécution pendant le runtime et peut colorier le code dans Eclipse. 
En gros, c'est le même outil, généralement utilisé pour analyser la couverture de code par les tests JUnit.

#### **Base de code avec des fuites de mémoire.**

Chaque développeur a un jour où, sur son système local, tout va bien, mais en production, OutOfMemory :(

**_Technique 4.1 :_** La JVM fournit des techniques pour capturer les dumps de heap en cas de OutOfMemory.

Ajoutez ce qui suit comme argument lors du démarrage de la JVM   
[_-XX:+HeapDumpOnOutOfMemoryError_](https://docs.oracle.com/javase/7/docs/webnotes/tsg/TSG-VM/html/clopts.html) _._ Cela capturera le dump de heap et le placera dans un fichier, qui pourra être utilisé pour analyser ce qui consomme la mémoire.

**Technique 4.2 :** Vous pouvez également capturer le dump de heap/thread d'une JVM en cours d'exécution en utilisant [jProfiler](https://www.ej-technologies.com/products/jprofiler/overview.html)/[Jvisualvm](https://visualvm.github.io/).

#### **Base de code où chaque JVM peut communiquer avec chaque autre JVM.**

Lorsque vous êtes plongé dans un environnement distribué spaghetti, il devient difficile de suivre le flux des requêtes.

**Technique 5.1 :** Vous pouvez utiliser des outils comme [**Wireshark**](https://www.wireshark.org/). Wireshark capture les données réseau et les représente dans une interface utilisateur agréable. Vous pouvez ensuite visualiser les requêtes/réponses HTTP circulant dans le système.

#### **Mentions honorables**

**Technique 6.1 :** Dans un environnement monothread, insérez intentionnellement   
`try catch` afin de connaître rapidement la stacktrace.

```java
try {
	throw new RuntimeException(); 
} catch(Exception e){
  e.printStackTrace();
}
```

**Technique 6.2 :** Utilisation de points d'arrêt Eclipse ou de points d'arrêt conditionnels.

**Technique 6.3 :** [https://en.wikipedia.org/wiki/Rubber_duck_debugging](https://en.wikipedia.org/wiki/Rubber_duck_debugging)

> Motivation de l'article : Apprentissage d'équipe/Partage des connaissances.