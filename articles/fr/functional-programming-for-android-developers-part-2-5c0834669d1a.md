---
title: Programmation Fonctionnelle pour les Développeurs Android — Partie 2
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-27T07:20:27.000Z'
originalURL: https://freecodecamp.org/news/functional-programming-for-android-developers-part-2-5c0834669d1a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1-2UBc_3rxKqKn89iMN2nQ.jpeg
tags:
- name: Android
  slug: android
- name: Functional Programming
  slug: functional-programming
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
seo_title: Programmation Fonctionnelle pour les Développeurs Android — Partie 2
seo_desc: 'By Anup Cowkur

  In the last post, we learned about Purity, Side effects and Ordering. In this part,
  let’s talk about immutability and concurrency.

  If you haven’t read part 1, please read it here:

  Functional Programming for Android developers — Part 1_...'
---

Par Anup Cowkur

Dans le dernier article, nous avons appris la _Pureté_, les _Effets de bord_ et l'_Ordre_. Dans cette partie, parlons de l'_immutabilité_ et de la _concurence_.

Si vous n'avez pas lu la partie 1, veuillez la lire ici :

[**Programmation Fonctionnelle pour les Développeurs Android — Partie 1**](https://medium.com/@anupcowkur/functional-programming-for-android-developers-part-1-a58d40d6e742)  
[_Récemment, j'ai passé beaucoup de temps à apprendre Elixir — Un langage de programmation fonctionnelle génial qui est convivial..._medium.com](https://medium.com/@anupcowkur/functional-programming-for-android-developers-part-1-a58d40d6e742)

### Immutabilité

L'immutabilité est l'idée qu'une valeur, une fois créée, ne peut jamais être modifiée.

Supposons que j'ai une classe _Car_ comme ceci :

**Java**

```
public final class Car {    private String name;    public Car(final String name) {        this.name = name;    }    public void setName(final String name) {        this.name = name;    }    public String getName() {        return name;    }}
```

**Kotlin**

```
class Car(var name: String?)
```

Puisqu'elle a un setter en Java et est une propriété mutable en Kotlin, je peux modifier le nom de la voiture après l'avoir construite :

**Java**

```
Car car = new Car("BMW");car.setName("Audi");
```

**Kotlin**

```
val car = Car("BMW")car.name = "Audi"
```

Cette classe n'est _pas_ immutable. Elle peut être modifiée après sa création.

Rendons-la immutable. Pour ce faire en Java, nous devons :

* Rendre la variable name _final_.
* Supprimer le setter.
* Rendre la classe _final_ également afin qu'une autre classe ne puisse pas l'étendre et modifier ses internes.

**Java**

```
public final class Car {    private final String name;    public Car(final String name) {        this.name = name;    }    public String getName() {        return name;    }}
```

En Kotlin, nous devons simplement rendre le nom une valeur immutable.

**Kotlin**

```
class Car(val name: String)
```

Maintenant, si quelqu'un veut créer une nouvelle voiture, il doit initialiser un nouvel objet. Personne ne peut modifier notre voiture une fois qu'elle est créée. Cette classe est maintenant _immutable_.

Mais qu'en est-il du getter _getName()_ en Java ou de l'accesseur _name_ en Kotlin ? Il retourne notre variable name au monde extérieur, non ? Et si quelqu'un modifiait la valeur _name_ après avoir obtenu une référence à celle-ci à partir de ce getter ?

En Java, [les chaînes sont immutables par défaut](http://stackoverflow.com/questions/1552301/immutability-of-strings-in-java). Même si quelqu'un obtenait une référence à notre chaîne _name_ et voulait la modifier, il obtiendrait une copie de la chaîne _name_ et la chaîne originale resterait intacte.

Mais qu'en est-il des choses qui ne sont pas immutables ? Une liste peut-être ? Modifions la classe _Car_ pour qu'elle ait une liste de personnes qui la conduisent.

**Java**

```
public final class Car {    private final List<String> listOfDrivers;    public Car(final List<String> listOfDrivers) {        this.listOfDrivers = listOfDrivers;    }    public List<String> getListOfDrivers() {        return listOfDrivers;    }}
```

Dans ce cas, quelqu'un peut utiliser la méthode _getListOfDrivers()_ pour obtenir une référence à notre liste interne et la modifier, rendant ainsi notre classe _mutable_.

Pour la rendre immutable, nous devons passer une copie profonde de la liste dans le getter qui est séparée de notre liste afin que la nouvelle liste puisse être modifiée en toute sécurité par l'appelant. Nous devons également faire une copie profonde de la liste qui est passée dans notre constructeur afin que personne ne puisse la modifier externement après la construction de la voiture.

Une copie profonde signifie que nous copions toutes les données dépendantes de manière récursive. Par exemple, si la liste était une liste d'objets _Driver_ au lieu de simples chaînes, nous devrions copier chacun des objets _Driver_ également. Sinon, nous créerions une nouvelle liste avec des références aux objets _Driver_ originaux qui pourraient être mutés. Dans notre classe, puisque la liste est composée de chaînes immutables, nous pouvons faire une copie profonde comme ceci :

**Java**

```
public final class Car {    private final List<String> listOfDrivers;    public Car(final List<String> listOfDrivers) {        this.listOfDrivers = deepCopy(listOfDrivers);    }    public List<String> getListOfDrivers() {        return deepCopy(listOfDrivers);    }    private List<String> deepCopy(List<String> oldList) {        List<String> newList = new ArrayList<>();        for (String driver : oldList) {            newList.add(driver);        }        return newList;    }}
```

Maintenant, cette classe est vraiment _immutable_.

En Kotlin, nous pouvons simplement déclarer la liste immutable dans notre définition de classe et elle est sûre à utiliser (sauf si vous l'appelez depuis Java et d'autres cas particuliers comme celui-ci)

**Kotlin**

```
class Car(val listOfDrivers: List<String>)
```

### Concurrence

D'accord, donc l'_immutabilité_ est cool et tout, mais pourquoi s'en soucier ? Comme nous en avons parlé dans la partie 1, les fonctions pures nous permettent une concurrence facile et si un objet est immutable, il est très facile à utiliser dans des fonctions pures puisque vous ne pouvez pas le modifier et causer des effets de bord.

Prenons un exemple. Supposons que nous ajoutons une méthode _getNoOfDrivers()_ dans notre classe _Car_ en Java et que nous la rendons également _mutable_ en Kotlin et en Java en permettant à un appelant externe de modifier la variable du nombre de conducteurs comme ceci :

**Java**

```
public class Car {    private int noOfDrivers;    public Car(final int noOfDrivers) {        this.noOfDrivers = noOfDrivers;    }    public int getNoOfDrivers() {        return noOfDrivers;    }    public void setNoOfDrivers(final int noOfDrivers) {        this.noOfDrivers = noOfDrivers;    }}
```

**Kotlin**

```
class Car(var noOfDrivers: Int)
```

Supposons que nous partageons une instance de cette classe _Car_ entre 2 threads : _Thread_1_ et _Thread_2. _Thread_1_ veut faire un calcul basé sur le nombre de conducteurs, il appelle donc _getNoOfDrivers()_ en Java ou accède à la propriété _noOfDrivers_ en Kotlin. Pendant ce temps, _Thread_2_ intervient et modifie la variable _noOfDrivers_. _Thread_1_ ne connaît pas ce changement et continue joyeusement ses calculs. Ces calculs seraient incorrects puisque l'état du monde a été modifié par _Thread_2_ sans que _Thread_1_ en soit informé.

Le diagramme de séquence suivant illustre le problème :

![Image](https://cdn-media-1.freecodecamp.org/images/1*PXDu-vgwZ6hmh96lc5TYOg.png)

Il s'agit d'une condition de course classique connue sous le nom de problème de lecture-modification-écriture. La manière traditionnelle de résoudre cela est d'utiliser des [verrous et mutex](https://en.wikipedia.org/wiki/Mutual_exclusion) afin qu'un seul thread puisse opérer sur des données partagées à la fois et libérer le verrou une fois l'opération terminée (dans notre cas, _Thread_1_ maintiendrait un verrou sur _Car_ jusqu'à ce qu'il termine son calcul).

Ce type de gestion des ressources basée sur les verrous est notoirement difficile à faire de manière sûre et conduit à des bugs de concurrence qui sont extrêmement difficiles à analyser. De nombreux programmeurs ont perdu leur santé mentale à cause de [deadlocks et livelocks](https://en.wikipedia.org/wiki/Deadlock).

Comment l'immutabilité pourrait-elle résoudre cela, dites-vous ? Rendons _Car_ immutable à nouveau :

**Java**

```
public final class Car {    private final int noOfDrivers;    public Car(final int noOfDrivers) {        this.noOfDrivers = noOfDrivers;    }    public int getNoOfDrivers() {        return noOfDrivers;    }}
```

**Kotlin**

```
class Car(val noOfDrivers: Int)
```

Maintenant, _Thread_1_ peut effectuer ses calculs sans souci puisqu'il est garanti que _Thread_2_ ne peut pas modifier l'objet voiture. Si _Thread_2_ veut modifier _Car_, il créera sa propre copie pour le faire et _Thread_1_ ne sera pas du tout affecté par cela. Aucun verrou nécessaire.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EyBmNH__K0QlOfapgib_rg.png)

L'immutabilité garantit que les données partagées sont thread-safe par défaut. Les choses qui _ne devraient pas_ être modifiées _ne peuvent pas_ être modifiées.

#### Et si nous devons avoir un état global modifiable ?

Pour écrire des applications réelles, nous avons besoin d'un état partagé modifiable dans de nombreux cas. Il peut y avoir une véritable exigence de mettre à jour _noOfDrivers_ et de le refléter dans tout le système. Nous traiterons de situations comme celle-ci en utilisant l'isolement d'état et en repoussant les effets de bord aux limites de notre système lorsque nous parlerons des _architectures fonctionnelles_ dans un prochain chapitre.

### Structures de données persistantes

Les objets immutables peuvent être géniaux, mais si nous les utilisons sans retenue, ils surchargeront le garbage collector et causeront des problèmes de performance. La programmation fonctionnelle nous fournit également des structures de données spécialisées pour utiliser l'immutabilité tout en minimisant la création d'objets. Ces structures de données spécialisées sont connues sous le nom de _Structures de Données Persistantes_.

Une structure de données persistante préserve toujours la version précédente d'elle-même lorsqu'elle est modifiée. De telles structures de données sont effectivement immutables, car leurs opérations ne mettent pas à jour la structure en place, mais retournent toujours une nouvelle structure mise à jour.

Supposons que nous avons les chaînes suivantes que nous voulons stocker en mémoire : **reborn, rebate, realize, realizes, relief, red, redder.**

Nous pouvons les stocker toutes séparément, mais cela prendrait plus de mémoire que nécessaire. Si nous regardons de près, nous pouvons voir que ces chaînes ont de nombreux caractères en commun et nous pourrions les représenter dans une seule structure de données [_trie_](https://en.wikipedia.org/wiki/Trie) comme ceci (tous les tries ne sont pas persistants, mais les tries sont l'un des outils que nous pouvons utiliser pour implémenter des structures de données persistantes) :

![Image](https://cdn-media-1.freecodecamp.org/images/1*5_7HbxMEMGRmpPkxlUnIHA.png)
_source : [http://merrigrove.blogspot.in/2010/05/dictionary-trie.html](http://merrigrove.blogspot.in/2010/05/dictionary-trie.html" rel="noopener" target="_blank" title=")_

C'est l'idée de base derrière le fonctionnement des structures de données persistantes. Lorsqu'une nouvelle chaîne doit être ajoutée, nous créons simplement un nouveau nœud et le lions à l'endroit approprié. Si un objet utilisant cette structure doit supprimer un nœud, nous arrêtons simplement de le référencer à partir de cet objet, mais le nœud réel n'est pas supprimé de la mémoire, évitant ainsi les effets de bord. Cela garantit que d'autres objets référençant cette structure peuvent continuer à l'utiliser.

Lorsque aucun autre objet ne la référence, nous pouvons GC toute la structure pour récupérer de la mémoire.

Les structures de données persistantes en Java ne sont pas une idée radicale. [Clojure](https://clojure.org/) est un langage fonctionnel qui s'exécute sur la JVM et dispose d'une bibliothèque standard entière de structures de données persistantes. Vous pourriez utiliser directement la bibliothèque standard de Clojure dans le code Android, mais elle a une taille et un nombre de méthodes significatifs. Une meilleure alternative que j'ai trouvée est une bibliothèque appelée [PCollections](https://pcollections.org/). Elle a [427 méthodes et une taille dex de 48 Ko](http://www.methodscount.com/?lib=org.pcollections%3Apcollections%3A2.1.2), ce qui la rend idéale pour nos besoins.

Par exemple, voici comment nous créerions et utiliserions une liste liée persistante en utilisant PCollections :

**Java**

```
ConsPStack<String> list = ConsPStack.empty();System.out.println(list);  // []ConsPStack<String> list2 = list.plus("hello");System.out.println(list);  // []System.out.println(list2); // [hello]ConsPStack<String> list3 = list2.plus("hi");System.out.println(list);  // []System.out.println(list2); // [hello]System.out.println(list3); // [hi, hello]ConsPStack<String> list4 = list3.minus("hello");System.out.println(list);  // []System.out.println(list2); // [hello]System.out.println(list3); // [hi, hello]System.out.println(list4); // [hi]
```

Comme nous pouvons le voir, aucune des listes n'est modifiée en place, mais une nouvelle copie est retournée à chaque fois qu'une modification est nécessaire.

PCollections dispose d'un ensemble de structures de données persistantes standard implémentées pour divers cas d'utilisation et vaut la peine d'être exploré. Elles s'intègrent également bien avec la bibliothèque de collections standard de Java, ce qui est assez pratique.

Kotlin est livré avec une bibliothèque standard qui contient déjà des collections immutables, donc si vous utilisez Kotlin, vous êtes prêt à partir.

Les structures de données persistantes sont un sujet vaste et cette section ne fait qu'effleurer la surface. Si vous êtes intéressé à en apprendre davantage sur elles, [Purely Functional Data Structures de Chris Okasaki](https://www.amazon.com/Purely-Functional-Structures-Chris-Okasaki/dp/0521663504) est fortement recommandé.

### Résumé

L'_Immutabilité_ et la _Pureté_ sont une combinaison puissante nous permettant d'écrire des programmes sûrs et concurrents. Dans la prochaine partie, nous apprendrons les fonctions d'ordre supérieur et les fermetures.

#### Lire la suite

[**Programmation Fonctionnelle pour les Développeurs Android — Partie 3**](https://medium.com/@anupcowkur/functional-programming-for-android-developers-part-3-f9e521e96788)  
[_Dans le dernier article, nous avons appris l'immutabilité et la concurrence. Dans celui-ci, nous examinerons les fonctions d'ordre supérieur et..._medium.com](https://medium.com/@anupcowkur/functional-programming-for-android-developers-part-3-f9e521e96788)

#### **Crédit supplémentaire**

J'ai fait une conférence entière sur l'immutabilité et la concurrence à Droidcon India. Profitez-en !

_Si vous avez aimé cela, cliquez sur le ? ci-dessous. Je remarque chacun d'eux et je suis reconnaissant pour chacun d'eux._

_Pour plus de réflexions sur la programmation, suivez-moi pour être informé lorsque j'écris de nouveaux articles._