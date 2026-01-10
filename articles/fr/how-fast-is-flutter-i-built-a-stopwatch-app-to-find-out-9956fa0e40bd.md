---
title: À quelle vitesse est Flutter ? J'ai construit une application chronomètre pour
  le découvrir.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-18T21:56:16.000Z'
originalURL: https://freecodecamp.org/news/how-fast-is-flutter-i-built-a-stopwatch-app-to-find-out-9956fa0e40bd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*270WC2lY8lFF6jfPpca0WQ.jpeg
tags:
- name: Android
  slug: android
- name: iOS
  slug: ios
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: À quelle vitesse est Flutter ? J'ai construit une application chronomètre
  pour le découvrir.
seo_desc: 'By Andrea Bizzotto

  This weekend I had some time to play with the new Flutter UI framework by Google.

  On paper it sounds great!


  Hot reloading? Yes, please.

  Declarative state-driven UI programming? I’m all in!


  According to the docs, high performance ...'
---

Par Andrea Bizzotto

Ce week-end, j'ai eu un peu de temps pour jouer avec le nouveau [Flutter](https://flutter.io/) UI framework de Google.

Sur le papier, cela semble génial !

* [Rechargement à chaud](https://flutter.io/hot-reload/) ? Oui, s'il vous plaît.
* Programmation UI [basée sur l'état](https://flutter.io/tutorials/interactive/) déclarative ? Je suis entièrement d'accord !

Selon [la documentation](https://flutter.io/faq/#what-kind-of-app-performance-can-i-expect), des performances élevées sont à prévoir :

> Flutter est conçu pour aider les développeurs à atteindre facilement un 60fps constant.

Mais qu'en est-il de l'utilisation du CPU ?

**TL;DR** : Pas aussi bon que le natif. Et vous devez le faire correctement :

* Les redessins fréquents de l'UI sont coûteux
* Si vous appelez souvent `setState()`, assurez-vous qu'il redessine aussi peu d'UI que possible.

J'ai construit une simple application chronomètre en Flutter et je l'ai profilée pour analyser l'utilisation du CPU et de la mémoire.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Bo0l0BjIRcInHZo2ACvjsA.png)
_**Gauche** : application chronomètre iOS. **Droite** : Ma version en Flutter. Belle, n'est-ce pas ?_

### Implémentation

L'UI est pilotée par deux objets : un [chronomètre](https://docs.flutter.io/flutter/dart-core/Stopwatch-class.html) et un [timer](https://docs.flutter.io/flutter/dart-async/Timer-class.html).

* L'utilisateur peut démarrer, arrêter et réinitialiser le chronomètre en appuyant sur deux boutons.
* Chaque fois que le chronomètre est démarré, un timer périodique est créé avec un callback qui se déclenche toutes les 30ms et met à jour l'UI.

L'UI principale est construite comme ceci :

Comment cela fonctionne-t-il ?

* Deux boutons gèrent l'état de l'objet chronomètre.
* Lorsque le chronomètre est mis à jour, `setState()` est appelé, déclenchant la méthode `build()`.
* Dans le cadre de la méthode `build()`, un nouveau `TimerText` est créé.

La classe `TimerText` ressemble à ceci :

Quelques notes :

* Le timer est créé avec l'objet `TimerTextState`. Chaque fois que le callback est déclenché, `setState()` est appelé **si le chronomètre est en cours d'exécution**.
* Cela provoque l'appel de la méthode `build()`, qui dessine un nouvel objet `Text` avec le temps mis à jour.

### Faire les choses correctement

Lorsque j'ai construit cette application pour la première fois, je gérais tout l'état et l'UI dans la classe `TimerPage`, qui comprenait à la fois le chronomètre et le timer.

Cela signifiait que chaque fois que le callback du timer était déclenché, toute l'UI était reconstruite. Cela est redondant et inefficace : seul l'objet `Text` contenant le temps écoulé devrait être redessiné — surtout si le timer se déclenche toutes les 30ms.

Cela devient apparent si nous considérons les hiérarchies d'arbres de widgets non optimisées et optimisées :

![Image](https://cdn-media-1.freecodecamp.org/images/1*YrJV5E7jWzr3K0kjPBs1Mg.png)

Créer une classe `TimerText` séparée pour encapsuler la logique du timer est moins intensif en CPU.

En d'autres termes :

* Les redessins fréquents de l'UI sont coûteux
* Si vous appelez souvent `setState()`, assurez-vous qu'il redessine aussi peu d'UI que possible.

La documentation de Flutter indique que la plateforme est optimisée pour une [allocation rapide](https://flutter.io/faq/#why-did-flutter-choose-to-use-dart) :

> Le framework Flutter utilise un flux de style fonctionnel qui dépend fortement de l'allocateur de mémoire sous-jacent gérant efficacement les petites allocations de courte durée.

Peut-être que la reconstruction d'un arbre de widgets ne compte pas comme une "petite allocation de courte durée". En pratique, mes optimisations de code ont abouti à une utilisation plus faible du CPU et de la mémoire (voir ci-dessous).

#### Mise à jour 19–03–2018

Depuis la publication de cet article, certains ingénieurs de Google ont pris note et ont aimablement contribué avec quelques optimisations supplémentaires.

Le code mis à jour réduit encore plus le redessin de l'UI en divisant `TimerText` en deux widgets `MinutesAndSeconds` et `Hundredths` :

![Image](https://cdn-media-1.freecodecamp.org/images/1*NQxSNVJDSnZnC3DohLBTAA.png)
_Optimisations supplémentaires de l'UI (crédit : Google)_

Ces widgets s'enregistrent eux-mêmes comme écouteurs du callback du timer, et ne se redessinent que lorsque leur état change. Cela optimise encore plus les performances, car seul le widget `Hundredths` se rend maintenant toutes les 30ms.

### Résultats de benchmarking

J'ai exécuté l'application en mode release (`flutter run --release`) :

* Appareil : **iPhone 6** sous **iOS 11.2**
* Version de Flutter : [0.1.5](https://github.com/flutter/flutter/releases/tag/v0.1.5) (22 févr. 2018).
* Xcode 9.2

J'ai surveillé l'utilisation du CPU et de la mémoire dans Xcode pendant trois minutes, et j'ai mesuré les performances des trois modes différents.

#### Code non optimisé

* Utilisation du CPU : 28%
* Utilisation de la mémoire : 32 Mo (à partir d'une base de 17 Mo après le démarrage de l'application)

![Image](https://cdn-media-1.freecodecamp.org/images/1*F1GR6mVtVEwRjaJptEuEwQ.png)

#### Passe d'optimisation 1 (widget de texte de timer séparé)

* Utilisation du CPU : 25%
* Utilisation de la mémoire : 25 Mo (à partir d'une base de 17 Mo après le démarrage de l'application)

![Image](https://cdn-media-1.freecodecamp.org/images/1*dTO3vThMfGx0LYrLqAIlAQ.png)

#### Passe d'optimisation 2 (minutes, secondes, centièmes séparés)

* Utilisation du CPU : 15% à 25%
* Utilisation de la mémoire : 26 Mo (à partir d'une base de 17 Mo après le démarrage de l'application)

![Image](https://cdn-media-1.freecodecamp.org/images/1*JFnMDRT8utbB9C4ETPklOg.png)

Dans ce dernier test, le graphique d'utilisation du CPU suit de près le thread GPU, tandis que le thread UI reste assez constant.

**NOTE** : l'exécution du même benchmark en [**mode lent**](https://flutter.io/faq/#my-app-has-a-slow-mode-bannerribbon-in-the-upper-right-why-am-i-seeing-that) donne une utilisation du CPU supérieure à 50%, et **une utilisation de la mémoire augmentant régulièrement** au fil du temps.

Cela peut indiquer que la mémoire n'est pas désallouée en mode développement.

Point clé à retenir : **assurez-vous de profiler vos applications en mode release**.

Notez que Xcode signale un **très haut** impact énergétique lorsque l'utilisation du CPU dépasse 20%.

### Creuser plus profond

Les résultats m'ont fait réfléchir. Un timer qui se déclenche ~30 fois par seconde et qui ré-affiche une étiquette de texte ne devrait pas utiliser jusqu'à 25% d'un [CPU dual core 1.4GHz](https://en.wikipedia.org/wiki/Apple_A8).

L'arbre des widgets dans une application Flutter est construit avec un **paradigme déclaratif**, plutôt que le modèle de programmation **impératif** utilisé dans iOS / Android.

Mais le modèle impératif est-il plus performant ?

Pour le découvrir, j'ai construit la même application chronomètre sur iOS.

Voici le code Swift pour configurer un timer et mettre à jour une étiquette de texte toutes les 30ms :

Pour être complet, voici le code de formatage du temps que j'ai utilisé en Dart (passe d'optimisation 1) :

Les résultats finaux ?

**Flutter.** CPU : 25%, Mémoire : 22 Mo

**iOS.** CPU : 7%, Mémoire : 8 Mo

L'implémentation Flutter est plus de 3x plus lourde en CPU, et utilise 3x plus de mémoire.

Lorsque le timer ne fonctionne pas, l'utilisation du CPU redescend à 1%. Cela confirme que tout le travail du CPU va dans la gestion des callbacks du timer et le redessin de l'UI.

Cela n'est pas entièrement surprenant.

* Dans l'application Flutter, je construis et je rends un nouveau widget `Text` à chaque fois.
* Sur iOS, je mets simplement à jour le texte d'un `UILabel`.

"Hey !" — je vous entends dire. "Mais le code de formatage du temps est différent ! Comment savez-vous que la différence d'utilisation du CPU n'est pas due à cela ?"

Eh bien, modifions les deux exemples pour ne faire aucun formatage du tout :

Swift :

Dart :

Résultats mis à jour :

**Flutter.** CPU : 15%, Mémoire : 22 Mo

**iOS.** CPU : 8%, Mémoire : 8 Mo

L'implémentation Flutter est toujours deux fois plus intensive en CPU. De plus, elle semble faire pas mal de choses sur plusieurs threads (GPU, travail d'I/O). Sur iOS, un seul thread est actif.

### Conclusion

J'ai comparé les performances de Flutter/Dart vs iOS/Swift sur un cas d'utilisation très spécifique.

Les chiffres ne mentent pas. En ce qui concerne les mises à jour fréquentes de l'UI, **vous ne pouvez pas avoir le beurre et l'argent du beurre**. 🍰

Flutter permet aux développeurs de créer des applications pour iOS et Android avec la même base de code. Et des fonctionnalités telles que le rechargement à chaud accélèrent encore plus la productivité. Flutter est encore dans ses premiers jours. J'espère que Google et la communauté pourront améliorer le profil d'exécution, afin que ces avantages soient reportés aux utilisateurs finaux.

Quant à vos applications, envisagez d'affiner votre code pour minimiser les redessins de l'UI. Cela en vaut vraiment la peine.

J'ai ajouté tout le code de ce projet sur [ce dépôt GitHub](https://github.com/bizz84/stopwatch-flutter), afin que vous puissiez jouer avec vous-même.

Je vous en prie ! 😊

Ce projet d'exemple était ma première expérience avec Flutter. Si vous savez comment écrire un code plus performant, j'adorerais entendre vos commentaires.

#### Pour plus d'articles et de tutoriels vidéo, consultez [Coding With Flutter](https://codingwithflutter.com/).

![Image](https://cdn-media-1.freecodecamp.org/images/1*TZ8Z0EnBGBugOs8mh19mHA.png)

**À propos de moi** : Je suis un développeur iOS & Flutter, jonglant entre le travail contractuel, l'open source, les projets parallèles et le blogging.

Je suis [@biz84](https://twitter.com/biz84) sur Twitter. Vous pouvez également voir ma page [GitHub](https://github.com/bizz84). Feedback, tweets, gifs drôles, tout est bienvenu ! Mon préféré ? Beaucoup de 🍌. Oh, et du pain aux bananes.