---
title: Le modèle de conception Observer est un peu comme un podcast
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-25T03:55:11.000Z'
originalURL: https://freecodecamp.org/news/the-observer-design-pattern-is-kind-of-like-a-podcast-cdee5ef9f074
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_lV71Wek7B9MUmsOjS76gQ.png
tags:
- name: design patterns
  slug: design-patterns
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: Ruby
  slug: ruby
- name: Web Development
  slug: web-development
seo_title: Le modèle de conception Observer est un peu comme un podcast
seo_desc: 'By Sihui Huang

  If you listen to podcasts, you are already familiar with the Observer pattern. In
  fact, you are an “observer”.

  Here’s the definition for the Observer pattern:


  The Observer Pattern defines a one-to-many dependency between objects so th...'
---

Par Sihui Huang

Si vous écoutez des podcasts, vous êtes déjà familier avec le modèle Observer. En fait, vous êtes un « observateur ».

Voici la définition du modèle Observer :

> Le modèle Observer définit une dépendance un-à-plusieurs entre des objets de sorte que lorsqu'un objet change d'état, tous ses dépendants sont notifiés et mis à jour automatiquement.

### Examinons la définition en relation avec les podcasts.

J'ai trouvé un podcast intéressant nommé `developer tea`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-lQ8wA_1gNxtwimzoqKfGA.png)

Après avoir cliqué sur le bouton `S'ABONNER`, je suis maintenant sur leur liste d'abonnés.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GBO65Rn7VDroo7R5sbkfKw.png)

Lorsque `developer tea` publie un nouvel épisode, l'application me notifie ainsi que les autres abonnés. Elle télécharge le nouvel épisode pour nous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_bOkx12Vqyr9b7zBlDUVVg.png)

C'est exactement la définition du modèle Observer !

> Le modèle Observer définit une dépendance un-à-plusieurs entre des objets de sorte que lorsqu'un objet change d'état, tous ses dépendants sont notifiés et mis à jour automatiquement.

Il existe une relation un-à-plusieurs entre le podcast `developer tea` et les `abonnés`.

Lorsque `developer tea` change d'état, comme la publication d'un nouvel épisode, tous les `abonnés` de `developer tea` sont notifiés et mis à jour.

### Implémentons-le en Ruby.

Commençons par une version simple.

La classe `Podcast` contient une liste d'épisodes et possède une méthode pour `ajouter_episode` à la liste.

Ensuite, nous pouvons créer le podcast `developer_tea` et ajouter l'épisode #1 comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*79mOvT3PAVnOZKIzmkhAog.png)

Je veux recevoir une notification chaque fois qu'un nouvel épisode est publié.

Nous pouvons me mettre à jour après avoir ajouté un nouvel épisode à la liste :

Et chaque fois que je reçois une mise à jour de `developer_tea`, je peux télécharger le dernier épisode.

J'aime tellement écouter `developer_tea` que je le recommande à mon amie, Amber. Maintenant, Amber veut aussi s'y abonner.

![Image](https://cdn-media-1.freecodecamp.org/images/1*PKqEa9I2eoOKJAs_ajZUxA.png)

Nous devons nous assurer qu'Amber reçoit également une notification chaque fois qu'un nouvel épisode est publié :

Hmmm, ce code fait ce que nous voulons.

Mais il y a un problème.

Chaque fois que nous voulons ajouter un abonné, nous devons redéfinir la classe.

Y a-t-il un moyen de mettre à jour la liste des abonnés sans avoir à redéfinir la classe ????

### ??Nous pouvons garder une liste d'abonnés !??

La nouvelle classe `Podcast` conserve une liste d'abonnés avec l'aide de deux nouvelles méthodes : une pour ajouter des abonnés et une pour supprimer des abonnés. Lorsqu'un épisode est publié, nous mettons à jour chaque abonné.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xnCj4ij96f0MS6ioiOxk6w.png)

Malheureusement, Amber n'apprécie pas autant le podcast que moi et décide de se désabonner. Nous utilisons la méthode `supprimer_abonne` pour la retirer de la liste des abonnés.

![Image](https://cdn-media-1.freecodecamp.org/images/1*berwHCxfb4NDDv7XbcPjAw.png)

**??Hourra ! Vous venez d'apprendre le modèle Observer !??**

### **Principe de conception derrière le modèle Observer.**

**Le modèle Observer utilise le principe de conception de couplage lâche :**

> **Efforcez-vous de concevoir des objets faiblement couplés qui interagissent.**

**La classe `Podcast` ne sait pas grand-chose sur ses abonnés. Elle sait seulement que chaque abonné possède une méthode de mise à jour.**

**Ce couplage lâche minimise la dépendance entre Podcast et ses abonnés. Il maximise également la flexibilité. Tant qu'il possède une méthode de mise à jour, un abonné peut être n'importe quoi : un humain, un groupe de personnes, un animal, ou même une voiture.**

**Points clés :**

1. **Le modèle Observer définit une dépendance un-à-plusieurs entre des objets de sorte que lorsqu'un objet change d'état, tous ses dépendants sont notifiés et mis à jour automatiquement.**
2. **Principe de conception de couplage lâche : efforcez-vous de concevoir des objets faiblement couplés qui interagissent.**

**Merci d'avoir lu. Connaissez-vous d'autres exemples concrets du modèle Observer ? ?**

**Je publie sur [sihui.io](http://www.sihui.io/) chaque semaine.**

**Abonnez-vous pour ne pas manquer le prochain article de la série.**

**La prochaine fois, nous parlerons de…**

![Image](https://cdn-media-1.freecodecamp.org/images/1*dIc3a1EKWwu3dwB1sPtvRw.png)