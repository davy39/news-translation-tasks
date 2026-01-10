---
title: Comment tester l'architecture de votre projet Java avec ArchUnit
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-10T16:33:05.000Z'
originalURL: https://freecodecamp.org/news/java-archunit-testing-the-architecture-a09f089585be
coverImage: https://cdn-media-1.freecodecamp.org/images/1*T1255atSpmUxEhV_n4t9Yw.png
tags:
- name: coding
  slug: coding
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: unit testing
  slug: unit-testing
seo_title: Comment tester l'architecture de votre projet Java avec ArchUnit
seo_desc: 'By Emre Savcı

  In this post, I will show you an interesting library called ArchUnit that I met
  recently. It does not test your code flow or business logic. The library lets you
  test your “architecture” including class dependencies, cyclic dependencies...'
---

Par Emre Savcı

Dans cet article, je vais vous présenter une bibliothèque intéressante appelée ArchUnit que j'ai découverte récemment. Elle ne teste pas le flux de votre code ou la logique métier. La bibliothèque vous permet de tester votre « architecture » incluant les dépendances de classes, les dépendances cycliques, les accès aux couches, les conventions de nommage et la vérification de l'héritage.

Voici la liste des tests que nous allons écrire dans cet article :

* Test de dépendance cyclique
* Test d'accès aux couches
* Test de localisation de classe
* Test de type de retour de méthode
* Test de convention de nommage

Imaginons donc un projet avec la structure de packages présentée ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/eRqPRYi8fcrjbBal2M9vIqopIPnJcfOz6SX3)

Avant d'écrire des tests pour notre architecture, nous décidons en point de départ que nos contrôleurs ne doivent pas être accessibles depuis aucune autre classe ou package. Nous acceptons également conceptuellement que les noms des contrôleurs doivent se terminer par le suffixe « ...Controller ».

Il est maintenant temps de mettre les mains dans le cambouis. Ci-dessous, nous commençons à écrire notre premier test. Il nous permet de vérifier notre convention de nommage.

#### **Tests de convention de nommage**

```
@RunWith(ArchUnitRunner.class)@AnalyzeClasses(packages = "com.test.controllers")public class NamingConventionTests {    @ArchTest    ArchRule controllers_should_be_suffixed = classes()            .that().resideInAPackage("..controllers..")            .should().haveSimpleNameEndingWith("Controller");    }
```

Lorsque nous exécutons le test, nous voyons qu'il passe :

![Image](https://cdn-media-1.freecodecamp.org/images/FVYRmI5KiWe5B5VFE53v4F3x0tsoi2Q5dceD)

Il existe deux types de tests avec ArchUnit. L'un d'eux est similaire à celui montré ci-dessus. Si nous le souhaitons, nous pouvons écrire des tests en utilisant l'annotation `Test` de JUnit. Changez le paramètre `RunWith` en `JUnit4.class` et retirez l'annotation `AnalyzeClasses`.

De cette manière, nous spécifions les packages à importer en utilisant `ClassFileImporter` dans ArcUnit.

```
@RunWith(JUnit4.class)public class NamingConventionTests {    @Test    public void controllers_should_be_suffixed() {        JavaClasses importedClasses = new ClassFileImporter().importPackages("com.test.controllers");        ArchRule rule = classes()                .that().resideInAPackage("..controllers..")                .should().haveSimpleNameEndingWith("Controller");        rule.check(importedClasses);    }}
```

Maintenant, voyons ce qui se passe si nous avons un suffixe différent. Changez `("Controller")` en `("Ctrl")` et exécutez :

![Image](https://cdn-media-1.freecodecamp.org/images/bpiNudC8z7TTx19wNbeoEauM3s00fGstkKuL)

L'exception indique que : « java.lang.**AssertionError**: **Violation d'architecture** [Priorité : MOYENNE] — La règle 'les classes qui résident dans un package '..controllers..' doivent avoir un nom simple se terminant par 'Ctrl'' a été violée (1 fois) :  
le nom simple de com.test.controllers.**FirstController ne se termine pas par 'Ctrl'** dans (FirstController.java:0) »

Jusqu'à présent, tout va bien. Nous avons écrit notre premier test et il s'exécute correctement. Il est maintenant temps de passer à d'autres tests.

#### **Tests de localisation de classe**

Écrivons une autre règle qui garantit que les classes ayant l'annotation **repositories** doivent être situées dans le package **infrastructure**.

```
@RunWith(ArchUnitRunner.class)@AnalyzeClasses(packages = "com.test")public class RepositoryPackageTest {    @ArchTest    public ArchRule repositories_should_located_in_infrastructure = classes()            .that().areAnnotatedWith(Repository.class)            .should().resideInAPackage("..infrastructure..");}
```

Si nous annotons d'autres classes que les packages d'infrastructure, le test lève une AssertionError.

#### **Tests de type de retour de méthode**

Écrivons quelques vérifications de méthodes. Supposons que nous décidons que nos méthodes de contrôleur doivent retourner un type BaseResponse.

```
@RunWith(ArchUnitRunner.class)@AnalyzeClasses(packages = "com.test.controllers")public class ControllerMethodReturnTypeTest {    @ArchTest    public ArchRule controller_public_methods_should_return = methods()            .that().areDeclaredInClassesThat().resideInAPackage("..controllers..")            .and().arePublic()            .should().haveRawReturnType(BaseResponse.class)            .because("ici se trouve l'explication");}
```

#### **Tests de dépendance cyclique**

De nos jours, les problèmes de dépendance cyclique sont gérés par la plupart des conteneurs IOC. Il est bon d'avoir un outil qui teste cela pour nous.

Créez d'abord des classes qui ont une complexité cyclique :

![Image](https://cdn-media-1.freecodecamp.org/images/vRxbd6lmK0eHHl4s4UKELLZs1ldF4ir9yMV9)

```
package com.test.services.slice1;import com.test.services.slice2.SecondService;public class FirstService {    private SecondService secondService;    public FirstService() {        this.secondService = new SecondService();    }}
```

```
package com.test.services.slice2;import com.test.services.slice1.FirstService;public class SecondService {    private FirstService firstService;    public SecondService() {        this.firstService = new FirstService();    }}
```

FirstService et SecondService dépendent l'un de l'autre, ce qui crée le cycle.

Écrivons maintenant un test pour cela :

```
@RunWith(ArchUnitRunner.class)@AnalyzeClasses(packages = "com.test")public class CyclicDependencyTest {    @ArchTest    public static final ArchRule rule = slices().matching("..services.(*)..")            .should().beFreeOfCycles();}
```

L'exécution de ce test donne le résultat suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/ltAIwJP2j1vgpYj79u9GtZIIi-rJWmJSvnpW)

De plus, le résultat est le même avec l'injection par constructeur.

#### **Tests de couches**

Il est maintenant temps d'écrire un test de couche qui couvre nos couches.

```
@RunWith(JUnit4.class)public class LayeredArchitectureTests {    @Test    public void layer_dependencies_are_respected() {        JavaClasses importedClasses = new ClassFileImporter().importPackages("..com.test..");        ArchRule myRule = layeredArchitecture()                .layer("Controllers").definedBy("..com.test.controllers..")                .layer("Services").definedBy("..com.test.services..")                .layer("Infrastructure").definedBy("..com.test.infrastructure..")                .whereLayer("Controllers").mayNotBeAccessedByAnyLayer()                .whereLayer("Services").mayOnlyBeAccessedByLayers("Controllers")                .whereLayer("Infrastructure").mayOnlyBeAccessedByLayers("Services");        myRule.check(importedClasses);    }}
```

Nous violons les règles ci-dessus pour voir que notre test échoue — nous injectons un service dans le repository.

```
package com.test.infrastructure;import com.test.services.SecondService;public class FirstRepository {    SecondService secondService;    public FirstRepository(SecondService secondService) {        this.secondService = secondService;    }}
```

Lorsque nous exécutons le test, nous verrons que notre repository viole les règles :

![Image](https://cdn-media-1.freecodecamp.org/images/ThVQipnz3IR6On5lGpClwNOZ0kTgnzg3q6WP)

#### Conclusion

ArchUnit, comme vous le voyez, garantit que votre projet a la bonne architecture. Il vous aide à maintenir la structure du projet propre et empêche les développeurs de faire des changements cassants.

Nous avons fait un bref aperçu de la bibliothèque. En plus de toutes ses fonctionnalités, je pense qu'il serait formidable qu'ArchUnit ait des règles pour tester l'[architecture hexagonale](https://blog.octo.com/en/hexagonal-architecture-three-principles-and-an-implementation-example/), le [cqrs](https://docs.microsoft.com/tr-tr/azure/architecture/guide/architecture-styles/cqrs) et certains concepts DDD comme les agrégats, les objets de valeur, etc.

Pour les curieux, voici le code sur Github :

[**mstrYoda/java-archunit-examples**](https://github.com/mstrYoda/java-archunit-examples)  
[_Contribute to mstrYoda/java-archunit-examples development by creating an account on GitHub._github.com](https://github.com/mstrYoda/java-archunit-examples)[**TNG/ArchUnit**](https://github.com/TNG/ArchUnit)  
[_A Java architecture test library, to specify and assert architecture rules in plain Java - TNG/ArchUnit_github.com](https://github.com/TNG/ArchUnit)[**Unit test your Java architecture**](https://www.archunit.org/)  
[_Start enforcing your architecture within 30 minutes using the test setup you already have._www.archunit.org](https://www.archunit.org/)