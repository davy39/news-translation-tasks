---
title: Examinons les avantages et les inconvénients du modèle de conception Singleton
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-24T13:33:45.000Z'
originalURL: https://freecodecamp.org/news/singleton-design-pattern-pros-and-cons-e10f98e23d63
coverImage: https://cdn-media-1.freecodecamp.org/images/1*GOAK3XdRvjrcpX9dq0fUrQ.png
tags:
- name: Functional Programming
  slug: functional-programming
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Examinons les avantages et les inconvénients du modèle de conception Singleton
seo_desc: 'By Navdeep Singh


  Design patterns are conceptual tools for solving complex software problems. These
  patterns are simple and elegant solutions that have evolved over time and may have
  become generally accepted as the best way to address certain design...'
---

Par Navdeep Singh

> Les modèles de conception sont des outils conceptuels pour résoudre des problèmes logiciels complexes. Ces modèles sont des solutions simples et élégantes qui ont évolué au fil du temps et peuvent être devenus généralement acceptés comme la meilleure façon d'aborder certains défis de conception. — _Moi, dans mon ebook_ Reactive Programming with Swift 4

### Modèle de conception Singleton

Le modèle Singleton encapsule une ressource partagée dans une instance de classe unique. Cette instance arbitre l'accès à la ressource et aux informations d'état liées au stockage. Une méthode de classe fournit la référence à cette instance, il n'est donc pas nécessaire de transmettre la référence. Tout objet ayant accès à l'en-tête de classe du Singleton peut utiliser le Singleton.

Ce modèle de conception définit la structure d'une classe qui ne peut avoir qu'une seule instance. **Un Singleton encapsule une ressource unique et la rend facilement disponible dans toute l'application**. La ressource peut être du matériel, un service réseau, un stockage persistant ou toute autre chose qui peut être modélisée comme un objet ou un service unique.

Un exemple de Cocoa Touch est un appareil physique exécutant une application iOS. Pour une application en cours d'exécution, il n'y a qu'un seul iPhone ou iPad avec une batterie et un écran. UIDevice est une classe Singleton ici, car elle fournit un canal pour interagir avec les fonctionnalités sous-jacentes. Dans le cas où la ressource unique a une configuration modifiable, ce type de divergence peut entraîner des problèmes tels que des conditions de course et des blocages. Étant uniques, **les Singletons agissent comme un contrôle, garantissant un accès ordonné à la ressource partagée**.

> Les Singletons peuvent souvent être modélisés comme un serveur au sein de l'application qui accepte les demandes d'envoi, de stockage ou de récupération de données et de configuration de l'état de la ressource.

### Implémentation

L'implémentation du modèle Singleton crée souvent un objet unique en utilisant la méthode de fabrique, et cette instance/objet est appelée une instance partagée dans la plupart des cas. Puisque l'accès à l'instance est transmis via une méthode de classe, le besoin de créer un objet est éliminé. Examinons l'implémentation du Singleton en code.

Pour cet exemple, nous avons utilisé le modèle d'outil **command line tool** d'Xcode pour créer un projet et le nommer Singleton. Notre classe Singleton s'appelle **SingletonObject**, que nous avons créée comme une classe Cocoa normale, et elle est une sous-classe de **NSObject**. La configuration du projet ressemble à ceci jusqu'à présent :

![Image](https://cdn-media-1.freecodecamp.org/images/DrYEzG5i3dVViHfhA5b7kxvwdpti2SZvtLAp)

Ensuite, nous avons ajouté une méthode de classe appelée **sharedInstance** comme discuté précédemment, car c'est ainsi que la classe rendra le Singleton disponible. Sa valeur de retour est de type **SingleObject**, comme suit :

```
func sharedInstance() -> SingletonObject {         }
```

La fonction stocke l'instance dans une référence locale statique appelée **localSharedInstance**. Les variables locales statiques sont très similaires aux objets globaux — elles conservent leur valeur pendant toute la durée de vie de l'application, mais leur portée est limitée. **Ces qualités les rendent idéales pour être un Singleton, car elles sont permanentes et garantissent que notre Singleton est uniquement disponible via sharedInstance_.**

C'est l'une des façons dont notre implémentation de Singleton garantit que le Singleton reste unique. La structure de base de l'instance partagée consiste en un bloc conditionnel qui teste si une instance Singleton a été allouée. Mais, de manière surprenante, c'est l'ancienne façon de faire les choses (ou peut-être la façon de procéder dans d'autres langages). En Swift, cependant, l'implémentation a changé pour se réduire à une seule ligne, et nous n'avons pas besoin d'une méthode. L'implémentation ressemble à ceci :

```
class SingletonObject: NSObject {    static let sharedInstance = SingletonObject()}
```

Simple, n'est-ce pas ?

#### Modèle de conception Singleton — Avantages et inconvénients

> Les Singletons ne sont pas la réponse à tous les problèmes. Comme tout outil, ils peuvent être en quantité insuffisante ou être surutilisés.

Certains développeurs critiquent les Singletons pour diverses raisons. Nous examinerons cette critique et discuterons brièvement des moyens de les résoudre. Les critiques, pour la plupart, se divisent en deux catégories :

* **Les Singletons entravent les tests unitaires** : Un Singleton peut causer des problèmes pour écrire du code testable si l'objet et les méthodes qui lui sont associées sont si étroitement couplés qu'il devient impossible de tester sans écrire une classe entièrement fonctionnelle dédiée au Singleton.
* **Les Singletons créent des dépendances cachées** : Comme le Singleton est facilement disponible dans toute la base de code, il peut être surutilisé. De plus, comme sa référence n'est pas complètement transparente lors du passage à différentes méthodes, il devient difficile à suivre.

Pour éviter ces complications, lors de la considération du modèle Singleton, vous devez vous assurer que la classe est un Singleton. De plus, lors de la conception du modèle de conception Singleton, gardez les tests à l'esprit et utilisez l'injection de dépendances chaque fois que possible — c'est-à-dire, essayez de passer le Singleton comme paramètre à l'initialiseur chaque fois que possible.

Pour d'autres mises à jour, vous pouvez me suivre sur Twitter sur mon compte @NavRudraSambyal

Pour en savoir plus sur divers autres modèles de conception et des exemples pratiques, vous pouvez suivre le lien vers mon livre [Reactive programming in Swift 4](https://www.amazon.com/Reactive-Programming-Swift-easy-maintain-ebook/dp/B078MHNSL1/ref=asap_bc?ie=UTF8)

Merci d'avoir lu, veuillez le partager si vous l'avez trouvé utile :)