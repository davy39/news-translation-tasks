---
title: Qu'est-ce que le Fiasco de l'Ordre d'Initialisation Statique en C++ ? [Résolu]
subtitle: ''
author: Jayant Chowdhary
co_authors: []
series: null
date: '2023-12-06T23:11:52.000Z'
originalURL: https://freecodecamp.org/news/cpp-static-initialization-order-fiasco
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/StaticCover.jpg
tags:
- name: C++
  slug: c-2
seo_title: Qu'est-ce que le Fiasco de l'Ordre d'Initialisation Statique en C++ ? [Résolu]
seo_desc: "In this article, I'll be covering a subtle but egregious problem that can\
  \ occur in C++ programs. This problem is popularly called the 'Static Initialization\
  \ Order Fiasco'. \nI'll first go over what the problem is, then go onto some solutions\
  \ and explo..."
---

Dans cet article, je vais aborder un problème subtil mais grave qui peut survenir dans les programmes C++. Ce problème est populairement appelé le 'Fiasco de l'Ordre d'Initialisation Statique'.

Je vais d'abord expliquer en quoi consiste le problème, puis aborder certaines solutions et explorer leur fonctionnement. Commençons.

Voici ce que nous allons couvrir :

<ul>
    <li><a href="#prerequis">Prérequis</a></li>
    <li><a href="#questcequelefiascodelordredinitialisationstatiqueenc">Qu'est-ce que le 'Fiasco de l'Ordre d'Initialisation Statique' en C++ ?</a></li>
     <li><a href="#solutionsauproblemededinitialisationstatique">Solutions au problème de l'ordre de désinitialisation statique</a>
          <li><a href="#constructionapremiereutilisation">Construction à la première utilisation</a></li>
    <li><a href="#solutioncompteurnifty">Solution Compteur Nifty</a></li>
    </li>
	<li><a href="#resume">Résumé</a></li>
</ul>

## Prérequis

* Une compréhension de base du C++ : Pour les lecteurs qui ne sont pas familiers avec le C++, [Learn C++ Programming for Beginners – Free 31-Hour Course](https://www.freecodecamp.org/news/learn-c-with-free-31-hour-course/) est une ressource utile.
* En particulier, une compréhension des [classes de stockage](https://learn.microsoft.com/en-us/cpp/cpp/storage-classes-cpp?view=msvc-170) en C++ sera utile.

## Qu'est-ce que le 'Fiasco de l'Ordre d'Initialisation Statique' en C++ ?

La norme C++ stipule :

> _"L'ordre dans lequel les objets statiques sont initialisés à travers différentes unités de traduction est [indéfini](https://en.cppreference.com/w/cpp/language/siof) ou ambigu."_

Une unité de traduction est simplement une manière de dire un fichier qui est alimenté dans le compilateur. C'est un fichier source C++ avec tout le code des en-têtes inclus dedans.

Une chose à noter, pour plus tard dans l'article : les objets statiques dans la même unité de traduction sont construits dans l'ordre de déclaration et détruits dans l'ordre inverse.

Alors, en quoi est-ce un problème ?

Cela peut être un problème dans la situation suivante :

Supposons qu'il y ait 2 objets statiques dans 2 fichiers différents. `File1.cpp` a un objet statique de type classe A – `aObj`. `File2.cpp` a un objet statique de type classe B – `bObj`. L'objet statique dans `File1.cpp` est visible pour `File2.cpp` puisqu'il déclare `aObj` comme `extern` dans `File1.h`.

```cpp

// Problème d'ordre d'initialisation statique
// File1.h
class A {
....
  void doSomething() {
    ...
  } 
}
extern A aObj;

//File1.cpp


static A aObj;

// File2.cpp

class B {
B() {
 aObj.doSomething();// Pas correct ! aObj peut ne pas avoir été construit
}
....
}

static B bObj;

```

Dans ce programme, il est possible que l'objet `aObj` dans File1.cpp soit initialisé avant `bObj` dans File2.cpp. Cela est correct puisque dans ce cas, le constructeur pour `bObj` s'exécute après que `aObj` ait été construit. Il est sûr d'appeler des méthodes sur `aObj`.

Mais il est également possible que l'objet `bObj` dans File2.cpp soit initialisé avant `aObj` dans File1.cpp. Dans ce cas, _le constructeur de_ `bObj` _appele_ `doSomething()` _sur_ `aObj` _qui n'a pas été construit !_ La mémoire a été allouée pour `aObj`, mais il n'a pas été construit. Cela pourrait conduire à un comportement non intentionnel / un programme corrompu.

Donc, c'est en quoi consiste le fiasco de l'ordre d'initialisation statique.

Mais nous n'avons pas terminé : l'autre problème est le **fiasco de l'ordre de désinitialisation statique** ! C'est pratiquement le même problème, juste appliqué à l'ordre de désinitialisation des objets statiques.

La norme C++ ne spécifie pas non plus l'ordre dans lequel les objets statiques sont désinitialisés. Il est donc possible que l'objet statique `aObj` soit détruit avant `bObj`. C'est un problème si le destructeur de `bObj` utilise ou référence `aObj`.

Cela est illustré dans l'extrait de code ci-dessous – c'est pratiquement la même chose que l'exemple ci-dessus, sauf que c'est l'ordre de désinitialisation qui est dangereux cette fois :

```cpp
// Problème d'ordre de désinitialisation statique
// File1.h
class A {
....
  void doSomething() {
    ...
  } 
}
extern A aObj;

//File1.cpp

static A aObj;

// File2.cpp

class B {
B() {}
~B() {
 aObj.doSomething(); // Pas correct ! aObj peut avoir déjà été détruit !
}
....
}

static B bObj;

```

**Note :** Ces problèmes ne s'appliquent qu'aux objets avec une portée de stockage _statique_. Ils ne se produiront pas si `bObj` était une variable avec une portée de stockage automatique. Dans ce cas, la norme C++ garantit que `aObj` est construit avant `bObj` et détruit après.

**Autre note :** Ces problèmes ne se produisent pas non plus dans les programmes C. Pourquoi ? Eh bien, en C, il n'y a pas de concept de constructeurs et de destructeurs. Les objets statiques sont complètement définis pendant le temps de compilation.

## Comment résoudre le problème de l'ordre de désinitialisation statique

Maintenant que le problème est clair, je vais discuter de certaines solutions. Il existe plusieurs façons de résoudre ce problème – chacune avec ses compromis. Examinons cela.

### Construction à la première utilisation :

Cette idiome tente de s'assurer qu'il y a toujours un objet entièrement construit chaque fois que l'objet statique en question est utilisé. En suivant les exemples de la section précédente, nous pouvons faire cela en remplaçant toutes les références à `aObj` par un appel de fonction `aObj()` qui retourne une référence à un objet de type `A`.

En code, cela ressemble à ceci :

```cpp
// Problème d'ordre d'initialisation statique
// File1.h
class A {
....
  void doSomething() {
    ...
  } 
};

A& aObj();

//File1.cpp

A& aObj() {
  static A *aObj = new A();
  return *aObj; 
}

// File2.cpp

class B {
 B() {
   /*
    * Correct puisque l'appel à aObj() garantit que
    * static A *aObj = new A(); a été exécuté
    */
   aObj().doSomething();  
  }
  ....
};

static B bObj;

```

`bObj` peut supposer en toute sécurité que l'appel à aObj() retourne un `aObj` entièrement construit puisque cette ligne :

```cpp
static A *aObj = new A();
```

aurait été exécutée lors de l'appel de la fonction et lui donnera un objet entièrement construit. De plus, puisque le programme n'appelle jamais delete sur `aObj`, il n'est jamais détruit, il est donc également sûr d'utiliser `aObj` dans le destructeur de `bObj`.

Mais cela signifie que la mémoire allouée pour `aObj` reste toujours vivante et valide tout au long de la durée de vie du programme. Et cela peut ou non être un problème (elle est bien sûr récupérée par le système d'exploitation après la fin du programme).

Alors, dans quelle situation cette solution n'est-elle pas idéale ? Dans le cas où le destructeur de `aObj` fait quelque chose de souhaitable. Par exemple : lorsque `aObj` est détruit – il écrit dans un fichier journal / fait autre chose qui a des effets secondaires.

Maintenant, vous pourriez demander, d'accord, pourquoi ne pas simplement remplacer le pointeur statique dans l'appel de fonction `aObj()` par un objet `aObj` statique ?

```cpp
A& aObj() {
  static A aObj;
  return aObj; 
}

```

Cela garantit toujours que `aObj` a été entièrement construit au moment où la fonction est appelée, n'est-ce pas ? Oui. Mais cela ne nous sauve pas du problème de l'ordre de désinitialisation statique. Il est toujours possible que le destructeur de `aObj` s'exécute avant le destructeur de `bObj`.

Il existe un truc intéressant qui résout ces deux problèmes : l'idiome du Compteur Nifty.

### Solution Compteur Nifty

Référence : cette ressource sur l'[idiome du compteur nifty](https://en.wikibooks.org/wiki/More_C%2B%2B_Idioms/Nifty_Counter#:~:text=The%20%22nifty%20counter%22%20or%20%22,the%20initialization%20of%20static%20objects.&text=The%20header%20file%20of%20the,called%20on%20the%20Stream%20object.) présente l'idée derrière cet idiome. Examinons-le.

L'idée est de s'assurer que :

1. L'objet statique utilisé est construit avant tout autre objet statique dans l'unité de traduction dans laquelle il est utilisé.
2. L'objet statique utilisé est détruit après tout autre objet statique dans l'unité de traduction dans laquelle il est utilisé.

```cpp
// File1.h
#pragma once

struct A {
  A();
  ~A();
};
extern A& aObj;

static struct AInitializer {
  AInitializer ();
  ~AInitializer ();
} aInitializer; // initialiseur statique pour chaque unité de traduction où aObj est utilisé

```

```cpp
// File1.cpp
#include "File1.h"

#include <new>         // Utilisé pour le placement new
#include <type_traits> // Utilisé pour aligned_storage

static int niftyCounter; // ceci est initialisé à zéro au moment du chargement

/*
 * Mémoire pour l'objet statique aObj - la mémoire elle-même est valide tout au long de
 * la durée de vie du programme.
 */
static typename std::aligned_storage<sizeof (A), alignof (A)>::type
  aObjBuf; 

A& aObj = reinterpret_cast<A&> (aObj);

A::A ()
{
  // Construire A
}
A::~A ()
{
  /*
   * Détruire A : avec des effets secondaires possibles
   * comme l'écriture dans un fichier.
   */
} 

AInitializer::AInitializer ()
{
  if (niftyCounter++ == 0) {
    new (&aObj) A (); // utiliser l'opérateur placement new
  }
}

AInitializer::~AInitializer ()
{
  if (--niftyCounter == 0) {
    (&aObj)->~A(); // exécuter le destructeur
  }
}

```

Essayons de comprendre ce que fait ce code.

Tout d'abord, dans le fichier d'en-tête, `File1.h` contient la définition de `class A`. Après cela, il y a la définition d'une classe appelée `AInitializer`.

Il y a également un objet statique **définis** dans le fichier d'en-tête de type `AInitializer`. Cela garantit que le constructeur pour `AInitializer` s'exécute avant le constructeur de tout autre objet statique dans l'unité de traduction où `File1.h` est inclus (bien sûr, vous devez inclure File1.h avant toute autre définition d'objet statique dans les fichiers source).

Rappel : _les objets statiques dans la même unité de traduction sont construits dans l'ordre de déclaration et détruits dans l'ordre inverse._

Maintenant que `AInitializer` est construit avant tout autre objet statique dans une unité de traduction, comment pouvons-nous utiliser cela à notre avantage ? `aObj` peut être construit dans le constructeur de `AInitializer` ! Ce qui est fait dans les lignes ci-dessous :

```cpp
AInitializer::AInitializer ()
{
  if (niftyCounter++ == 0) {
    new (&aObj) A (); // utiliser le placement new
  }
}

```

Notez que l'opérateur [placement new](https://en.cppreference.com/w/cpp/language/new) est utilisé ici au lieu de l'opérateur `new` pour construire `aObj`. Voyons ce qui se passerait si nous utilisions `new` à la place. Le code ressemblerait à ceci :

```cpp
A& aObj;
A *aObjp = nullptr;

AInitializer::AInitializer ()
{
  if (niftyCounter++ == 0) {
    aObjp = new A (); 
    aObj = *aObjp; // Pas correct ! Impossible de réassigner une référence
  }
}

```

Cela ne fonctionne pas car une référence doit être définie et déclarée en même temps. C'est précisément pourquoi l'opérateur placement `new` doit être utilisé.

```cpp
static typename std::aligned_storage<sizeof (A), alignof (A)>::type
  aObjBuf; 

A& aObj = reinterpret_cast<A&> (aObj)
```

Cela alloue de la mémoire pour contenir un objet de type `A` et l'assigne ensuite à la référence. Maintenant, tout ce qui reste à faire est de _construire_ réellement l'objet dans le constructeur de `AInitializer` – ce qui est fait avec l'opérateur placement new.

Une autre question qui peut surgir dans votre esprit : ici, il y a un objet statique `aObjBuf`. Mais n'est-il pas sujet au même problème d'ordre de désinitialisation dont nous avons parlé dans la deuxième partie de l'idiome de construction _à la première utilisation_ ?

La réponse est que la mémoire pour `aObjBuf` reste vivante et valide jusqu'à ce que le programme soit vivant. Rien ne se passe dans la construction de la mémoire. Donc c'est valide de faire cela.

Cette approche garantit également que le problème de l'ordre de désinitialisation statique n'est pas rencontré, puisque le dernier objet `AInitializer` détruit appellera le destructeur de `aObj`. Cela est garanti de s'exécuter après tout objet statique dans d'autres unités de traduction, puisque dans l'unité de traduction particulière, l'objet statique `aInitializer` est déclaré avant tout autre objet statique utilisant `aObj`. Cela signifie qu'il sera détruit dans l'ordre inverse – c'est-à-dire après que le destructeur de tout autre objet statique ait été exécuté.

Il y a quelques mises en garde ici : cette solution n'est pas la plus facile à comprendre et à mettre en œuvre. Elle n'est également pas thread-safe. Vous pouvez trouver plus d'informations dans l'article sur les compteurs Nifty présenté dans The C/C++ Users Journal, Mai, 1999 [ici](http://www.petebecker.com/js/js199905.html).

## Résumé

L'utilisation d'objets initialisés statiquement en C++ est délicate et doit être faite avec soin. Heureusement, il existe plusieurs solutions et moyens de contourner le problème.

Dans cet article, nous avons couvert certaines solutions courantes : l'idiome 'Construction à la première utilisation' et la 'Solution du compteur Nifty', ainsi que leurs mérites et défis.

J'espère que vous avez apprécié cet article !