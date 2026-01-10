---
title: Parlons de TOI — et du modèle de conception Singleton
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-04T10:42:44.000Z'
originalURL: https://freecodecamp.org/news/lets-talk-about-you-and-the-singleton-design-pattern-bb2e160fa952
coverImage: https://cdn-media-1.freecodecamp.org/images/1*dIc3a1EKWwu3dwB1sPtvRw.png
tags:
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: Ruby
  slug: ruby
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Parlons de TOI — et du modèle de conception Singleton
seo_desc: 'By Sihui Huang

  This might be the most important post in my Design patterns in life and Ruby series,
  because this one is about YOU.

  Before anything, you need to listen to this song:

  No, I’m serious.

  The song is less than 2 minutes.

  Listen to the song ...'
---

Par Sihui Huang

Ceci pourrait être l'article le plus important de ma série [Design patterns in life and Ruby](http://www.sihui.io/design-patterns/), car celui-ci parle de TOI.

Avant toute chose, tu dois écouter cette chanson :

Non, je suis sérieuse.

La chanson dure moins de 2 minutes.

Écoute la chanson avant de lire la suite.

Regardons les paroles de la chanson :

> Tiens-toi droit.

> **_Tu es dans une classe à part._**

> Sois fier.

> **_Tu n'es comme personne d'autre._**

> Sans aucun doute, tu es unique.

> **_Car tu es le seul et unique._**

> Relève le menton.

> **_Car tu es unique en ton genre._**

> Sors la poitrine.

> Nous savons que **_nous ne trouverons jamais personne comme toi sous le soleil._**

> **_Car tu es le seul et unique._**

> Si tout le monde était comme tout le monde, ce serait bien ennuyeux.

> Les choses qui me rendent différent sont les choses qui font que je suis moi.

**Tu es dans une classe à part, tu es unique en ton genre, et tu es le seul et unique !**

Cette unicité est exactement ce que représente le modèle Singleton !

Définition du modèle Singleton :

> Le modèle Singleton :

> - **garantit qu'une classe n'a qu'une seule instance**,

> - et fournit un point d'accès global à celle-ci.

La deuxième partie des critères est facile à satisfaire — en principe, n'importe quelle classe peut fournir un point d'accès global.

Mais une simple classe comme celle-ci ne garantit pas que la classe n'a qu'une seule instance :

![Image](https://cdn-media-1.freecodecamp.org/images/1*s3lXUeDR62XehFAku_FOpQ.png)

Nous pouvons facilement créer deux instances différentes de `you`.

C'est parce que la méthode `new`, la méthode de création d'instances pour la classe, est publique.

Pour éviter d'avoir plusieurs instances de la classe, nous pouvons essayer de marquer la méthode `new` comme privée, afin que personne en dehors de la classe n'ait accès à la méthode — à moins que tu ne fasses vraiment un effort et que tu utilises `You.send('new')`. Tu peux toujours appeler `.send(method_name)` pour invoquer une méthode privée en Ruby, si tu veux vraiment aller contre la volonté de l'auteur du code.

![Image](https://cdn-media-1.freecodecamp.org/images/1*qVaeV0F_M36Oy5w3wnIu7Q.png)

Mais alors nous ne pouvons pas créer d'instance de la classe du tout !

Pourquoi ne pas créer une instance depuis l'intérieur de la classe et ouvrir un point d'accès au monde extérieur ?

(En Ruby, @@ indique que la variable est une variable de classe.)

Maintenant, il y a un moyen d'accéder à l'instance créée dans la classe :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ldvn18SnL_RnPdKedqjcqQ.png)

Les deux critères de la définition du modèle Singleton ont été remplis :

> - garantit qu'une classe n'a qu'une seule instance,

> - et fournit un point d'accès global à celle-ci.

Nous venons d'écrire un exemple simple du modèle Singleton !

Il y a de nombreux avantages à utiliser le modèle Singleton. L'un d'eux est l'initialisation paresseuse :

> la tactique consistant à **retarder la création d'un objet**, le calcul d'une valeur, ou un autre processus coûteux **jusqu'à la première fois où il est nécessaire**.

Dans le code ci-dessus, nous n'initialisons pas l'instance jusqu'à la première fois où `LazyYou.instance` est appelé, c'est-à-dire la première fois où l'instance est nécessaire.

Maintenant, tu as une compréhension de base du modèle Singleton.

La prochaine fois que tu essaieras de t'assurer qu'une classe n'a qu'une seule instance, tu pourras considérer ce modèle.

Et quand tu es découragé, rappelle-toi que **tu es le seul et unique et les choses qui te rendent différent sont les choses qui font que tu es toi :)**

### Points à retenir

1. **Le modèle Singleton garantit qu'une classe n'a qu'une seule instance et fournit un point d'accès global à celle-ci.**
2. **Sois fier. Tu n'es comme personne d'autre.**

N'oublie pas de t'abonner pour ne pas manquer le prochain article !

La prochaine fois, nous parlerons de…

![Image](https://cdn-media-1.freecodecamp.org/images/1*9gP8bD5I_NpQFgRIAGtT7g.png)