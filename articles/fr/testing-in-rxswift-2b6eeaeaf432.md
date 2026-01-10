---
title: Comment exécuter des tests dans RxSwift
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-19T04:15:05.000Z'
originalURL: https://freecodecamp.org/news/testing-in-rxswift-2b6eeaeaf432
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ASJBAG5pLUIdEpVU4_RM2A.png
tags:
- name: coding
  slug: coding
- name: iOS
  slug: ios
- name: Reactive Programming
  slug: reactive-programming
- name: RxSwift
  slug: rxswift
- name: technology
  slug: technology
seo_title: Comment exécuter des tests dans RxSwift
seo_desc: 'By Navdeep Singh

  RxTest and RxBlocking are part of the RxSwift repository. They are made available
  via separate pods, however, and so require separate imports.

  RxTest provides useful additions for testing Rx code. It includes TestScheduler,
  which is ...'
---

Par Navdeep Singh

**RxTest** et **RxBlocking** font partie du dépôt RxSwift. Ils sont disponibles via des pods séparés, cependant, et nécessitent donc des imports séparés.

**RxTest** fournit des ajouts utiles pour tester le code Rx. Il inclut **TestScheduler**, qui est un planificateur de temps virtuel, et fournit des méthodes pour ajouter des événements à des intervalles de temps précis.

**RxBlocking**, en revanche, vous permet de convertir une séquence Observable régulière en un observable bloquant, qui bloque le thread sur lequel il s'exécute jusqu'à ce que la séquence observable soit terminée ou qu'un délai d'attente spécifié soit atteint. Cela rend les tests des opérations asynchrones beaucoup plus faciles.

Examinons chacun d'eux maintenant.

### RxTest

Comme décrit ci-dessus, **RxTest** fait partie du même dépôt que **RxSwift**. Il y a une autre chose à savoir sur **RxTest** avant de plonger dans quelques tests Rx : RxTest expose deux types d'Observables à des fins de test.

* HotObservables
* ColdObservables

HotObservables rejouent les événements à des heures spécifiées en utilisant un planificateur de test, indépendamment du fait qu'il y ait des abonnés.

ColdObservables fonctionnent plus comme des Observables réguliers, rejouant leurs éléments à leurs nouveaux abonnés lors de l'abonnement.

### RxBlocking

Si vous êtes familier avec les attentes dans **XCTest**, vous saurez que c'est une autre façon de tester les opérations asynchrones. Utiliser RxBlocking est simplement beaucoup plus facile. Commençons par une petite implémentation afin que nous puissions voir comment tirer parti de cette bibliothèque lors du test d'opérations asynchrones.

### Test avec RxBlocking

Nous allons commencer un nouveau test et créer un Observable de 10, 20 et 30, comme suit :

```
func testBlocking(){        let observableToTest = Observable.of(10, 20, 30)    }
```

Maintenant, nous allons définir le résultat comme étant égal à l'appel de toBlocking() sur l'observable que nous avons créé :

```
let result = observableToTest.toBlocking()
```

**toBlocking()** retourne un Observable bloquant vers un tableau simple, comme vous pouvez le voir ici :

![Image](https://cdn-media-1.freecodecamp.org/images/1F4TF7RZ2FlBgcynP9tWUi9UqQBtLCCy6YSg)

Nous devrons utiliser la première méthode si nous voulons découvrir laquelle est une méthode de lancement. Nous allons donc l'envelopper dans une instruction do catch, puis nous ajouterons une instruction **AssertEquals** si elle réussit, comme suit :

```
func testBlocking(){        let observableToTest = Observable.of(10, 20, 30)        do{            let result = try observableToTest.toBlocking().first()            XCTAssertEqual(result, 10)        } catch {        }    }
```

Alternativement, un Assert échoue si ce n'est pas cela :

```
do{            let result = try observableToTest.toBlocking().first()            XCTAssertEqual(result, 10)        } catch {            XCTFail(error.localizedDescription)        }
```

C'est tout ! Exécutons le test, et vous verrez que le test passe. Nous pouvons simplifier ce test avec seulement deux lignes de code en forçant le try.

Encore une fois, cela est plus acceptable dans les tests que dans le code de production. Nous allons commenter l'instruction do catch et ensuite écrire l'assert equals en une seule ligne, comme suit :

```
XCTAssertEqual(try! observableToTest.toBlocking().first(), 10)
```

Relancez le test, et vous verrez que le test passe une fois de plus. Le code global avec les commentaires ressemble à ceci :

```
func testBlocking(){        let observableToTest = Observable.of(10, 20, 30)//        do{//            let result = try observableToTest.toBlocking().first()//            XCTAssertEqual(result, 10)//        } catch {//            XCTFail(error.localizedDescription)//        }        XCTAssertEqual(try! observableToTest.toBlocking().first(), 10)    }
```

**Qu'en est-il de la concision ?** À vrai dire, cette séquence Observable serait en fait déjà synchrone si nous imprimions les éléments émis dans un abonnement suivi d'un marqueur. Le marqueur sera imprimé après l'événement terminé de l'abonnement.

Pour tester une opération réellement asynchrone, nous allons écrire un test de plus. Cette fois, nous allons utiliser un planificateur concurrent sur un thread d'arrière-plan, comme suit :

```
func testAsynchronousToArry(){        let scheduler = ConcurrentDispatchQueueScheduler(qos: .background)    }
```

Maintenant, nous allons créer un Observable de la séquence simple d'entiers. Nous allons utiliser map pour doubler chaque valeur, comme suit :

```
let intObservbale = Observable.of(10, 20, 30)            .map{ $0 * 2 }
```

Ensuite, nous allons nous abonner sur le planificateur :

```
let intObservbale = Observable.of(10, 20, 30)            .map{ $0 * 2 }            .subscribeOn(scheduler)
```

Maintenant, nous allons écrire une instruction do catch similaire au dernier test et appeler toBlocking sur l'Observable, qui devrait être observé sur le planificateur principal, comme suit :

```
do{   let result = try intObservbale.observeOn(MainScheduler.instance).toBlocking().toArray()   } catch {   }
```

Ensuite, nous ajouterons les mêmes assertions que dans l'exemple précédent :

```
do{   let result = try intObservbale.observeOn(MainScheduler.instance).toBlocking().toArray()            XCTAssertEqual(result, [20, 40, 60])        } catch {            XCTFail(error.localizedDescription)        }
```

Maintenant, nous allons exécuter le test, et vous noterez qu'il passe avec la coche verte dans la gouttière.

Notez que le marqueur est imprimé avant les éléments émis dans la console, comme montré :

![Image](https://cdn-media-1.freecodecamp.org/images/699d2sSCtcHgNblX68UK9VKzUBF-f1aTW8r0)

C'est parce que ces opérations ont été exécutées de manière asynchrone.

Pour d'autres mises à jour, vous pouvez me suivre sur Twitter sur mon compte twitter @NavRudraSambyal

Pour travailler avec des exemples d'observables chauds et froids, vous pouvez trouver le lien vers mon livre [Reactive programming in Swift 4](https://www.amazon.com/Reactive-Programming-Swift-easy-maintain-ebook/dp/B078MHNSL1/ref=asap_bc?ie=UTF8)

Merci d'avoir lu, veuillez le partager si vous l'avez trouvé utile :)