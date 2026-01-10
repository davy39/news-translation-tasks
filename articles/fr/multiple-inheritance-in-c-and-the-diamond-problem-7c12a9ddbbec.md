---
title: L'héritage multiple en C++ et le problème du diamant
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-21T18:03:55.000Z'
originalURL: https://freecodecamp.org/news/multiple-inheritance-in-c-and-the-diamond-problem-7c12a9ddbbec
coverImage: https://cdn-media-1.freecodecamp.org/images/1*QVZomxLNxnRYhm9gGIfYyw.png
tags:
- name: General Programming
  slug: programming
- name: programming languages
  slug: programming-languages
- name: software design
  slug: software-design
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
seo_title: L'héritage multiple en C++ et le problème du diamant
seo_desc: 'By Onur Tuna

  Unlike many other object-oriented programming languages, C++ allows multiple inheritance.

  Multiple inheritance allows a child class to inherit from more than one parent class.

  At the outset, it seems like a very useful feature. But a use...'
---

Par Onur Tuna

Contrairement à de nombreux autres langages de programmation orientés objet, le C++ permet l'héritage multiple.

L'héritage multiple permet à une classe enfant d'hériter de plus d'une classe parente.

À première vue, cela semble être une fonctionnalité très utile. Mais l'utilisateur doit faire attention à quelques _pièges_ lors de la mise en œuvre de cette fonctionnalité.

Dans les exemples ci-dessous, nous aborderons quelques scénarios auxquels il faut être attentif.

Nous allons commencer par un exemple simple pour expliquer ce concept en C++.

La sortie de ce code est la suivante :

```
Je respire comme un serpent.Je rampe comme un serpent.
```

Dans l'exemple ci-dessus, nous avons une classe de base nommée **LivingThing**. Les classes **Animal** et **Reptile** en héritent. Seule la classe **Animal** redéfinit la méthode `breathe()`. La classe **Snake** hérite des classes **Animal** et **Reptile**. Elle redéfinit leurs méthodes. Dans l'exemple ci-dessus, il n'y a pas de problème. Notre code fonctionne bien.

Maintenant, nous allons ajouter un peu de complexité.

Et si la classe **Reptile** redéfinissait la méthode `breathe()` ?

La classe **Snake** ne saurait pas quelle méthode `breathe()` appeler. C'est le « problème du diamant ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*cI0TQYv7yOgSsHhfES1Kaw.png)

#### Le problème du diamant

Regardez le code ci-dessous. Il est similaire au code de l'exemple précédent, sauf que nous avons redéfini la méthode `breathe()` dans la classe **Reptile**.

Si vous essayez de compiler le programme, il ne compilera pas. Vous ferez face à un message d'erreur comme celui ci-dessous.

```
member ‘breathe’ found in multiple base classes of different types
```

L'erreur est due au « problème du diamant » de l'héritage multiple. La classe **Snake** ne sait pas quelle méthode `breathe()` appeler.

Dans le premier exemple, seule la classe **Animal** avait redéfini la méthode `breathe()`. La classe **Reptile** ne l'avait pas fait. Par conséquent, il n'était pas très difficile pour la classe **Snake** de déterminer quelle méthode `breathe()` appeler. Et la classe **Snake** a fini par appeler la méthode `breathe()` de la classe **Animal**.

Dans le deuxième exemple, la classe Snake hérite de **deux** méthodes `breathe()`. La méthode `breathe()` des classes Animal et Reptile. Comme nous n'avons pas redéfini la méthode `breathe()` dans la classe Snake, il y a une ambiguïté.

Le C++ possède de nombreuses fonctionnalités puissantes telles que l'héritage multiple. Mais il n'est pas nécessaire d'utiliser toutes les fonctionnalités qu'il offre.

Je préfère ne pas utiliser l'héritage multiple et utiliser l'héritage _virtuel_ à la place.

L'héritage virtuel _résout_ le classique « problème du diamant ». Il garantit que la classe enfant n'obtienne qu'une seule instance de la classe de base commune.

En d'autres termes, la classe Snake n'aura qu'**une seule** instance de la classe LivingThing. Les classes Animal et Reptile partagent cette instance.

Cela résout l'erreur de compilation que nous avons reçue précédemment. Les classes dérivées de classes abstraites doivent redéfinir les fonctions virtuelles pures définies dans la classe de base.

J'espère que vous avez apprécié cet aperçu de l'héritage multiple et du « problème du diamant ».