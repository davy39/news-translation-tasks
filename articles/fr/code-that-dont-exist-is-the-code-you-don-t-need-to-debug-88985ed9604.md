---
title: Le code qui n'existe pas est le code que vous n'avez pas besoin de déboguer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-19T09:02:00.000Z'
originalURL: https://freecodecamp.org/news/code-that-dont-exist-is-the-code-you-don-t-need-to-debug-88985ed9604
coverImage: https://cdn-media-1.freecodecamp.org/images/1*wuV2gWnanM8JoG_8CS09tQ.jpeg
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Le code qui n'existe pas est le code que vous n'avez pas besoin de déboguer
seo_desc: 'By Fagner Brack

  As developers, we tend to write more code than necessary

  As a developer, you’re in the business of managing complexity. And code is inherently
  complex.

  By writing as little code as necessary to solve the task at hand, you’ll have fewe...'
---

Par Fagner Brack

#### En tant que développeurs, nous avons tendance à écrire plus de code que nécessaire

En tant que développeur, vous êtes dans le domaine de la gestion de la complexité. Et le code est intrinsèquement complexe.

En écrivant le moins de code possible pour résoudre la tâche à accomplir, vous aurez moins de soucis à l'avenir.

Moins de code, moins de complexité.

%[https://twitter.com/paulg/status/788803863381995520?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed&ref_url=https%3A%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Ftype%3Dtext%252Fhtml%26key%3Dd04bfffea46d4aeda930ec88cc64b87c%26schema%3Dtwitter%26url%3Dhttps%253A%2F%2Ftwitter.com%2Fpaulg%2Fstatus%2F788803863381995520%26image%3Dhttps%253A%2F%2Fi.embed.ly%2F1%2Fimage%253Furl%253Dhttps%25253A%25252F%25252Fpbs.twimg.com%25252Fprofile_images%25252F1824002576%25252Fpg-railsconf_bigger.jpg%2526key%253D4fce0568f2ce49e8b54624ef71a8a5bd]

Il existe de nombreux exemples qui peuvent illustrer ce principe. Pour les besoins de cet article, disons que vous souhaitez tester une fonction existante. Il s'agit d'une fonction héritée non testée qui exécute une requête réseau et fait quelque chose avec sa réponse. L'aspect important est que la réponse contient plus de données que ce que le code utilise réellement.

<script async src="//jsfiddle.net/fagnerbrack/gytawzt9/embed/"></script>

Le [code](https://jsfiddle.net/fagnerbrack/gytawzt9/) montrant une fonction qui nécessite uniquement les propriétés "street", "number" et "suburb" de "accountDetails". Voir la ligne 27.

Lors du test de cette fonction, vous souhaitez simuler la requête réseau et fournir un ensemble de données fixe qui simule l'original. Ainsi, vous pouvez vérifier si la fonction fonctionne comme prévu.

<script async src="//jsfiddle.net/fagnerbrack/pmgv0chw/embed/"></script>

Le [code](https://jsfiddle.net/fagnerbrack/pmgv0chw/) simulant la requête réseau avec le même ensemble de données. Voir les lignes 37 à 47.

Mais l'ensemble de données original est énorme et vous ne vous souciez pas vraiment du reste. Vous pouvez simplement fournir la réponse minimale nécessaire pour satisfaire les exigences de la fonction que vous testez.

<script async src="//jsfiddle.net/fagnerbrack/Lv6cd0v0/embed/"></script>

Le [code](https://jsfiddle.net/fagnerbrack/Lv6cd0v0/), simulant uniquement le nombre minimal de propriétés de l'ensemble de données. Voir les lignes 37 à 41.

Il y a plusieurs avantages avec le dernier exemple :

1. Il n'y a pas de réponse inutilisée dans le test
2. L'ensemble de données ne sera pas énorme, donc il est plus facile de raisonner à ce sujet (et cela rend également le test plus petit)
3. Si le code commence à nécessiter plus de données de la réponse en raison d'un autre test sur la même fonction, le test échouera et vous pourrez commencer à ajouter le reste de la réponse au cas par cas
4. Si vous modifiez toujours le code en modifiant d'abord les tests, lorsque le code commence à nécessiter moins de données, vous les supprimerez toujours d'abord des tests afin de conserver la quantité minimale de code nécessaire pour le tester

Le [Développement Piloté par les Tests](https://medium.com/@fagnerbrack/why-test-driven-development-4fb92d56487c) (TDD) vous oblige à écrire la quantité minimale de code qui satisfait un cas d'utilisation. Dans le dernier exemple, si vous aviez utilisé le TDD, il vous aurait obligé à écrire la quantité minimale de code dans l'ensemble de données jusqu'à ce que vous ayez besoin de plus de données (voir le point 3 ci-dessus).

Dans un excellent article intitulé [You Are Not Paid to Write Code](http://bravenewgeek.com/you-are-not-paid-to-write-code/), Tyler Treat dit :

> _Chaque fois que vous écrivez du code [...] vous introduisez la possibilité d'échec dans votre système._

Un système logiciel a tendance à devenir plus complexe avec le temps, augmentant l'[Entropie Logicielle](https://en.wikipedia.org/wiki/Software_entropy). L'acte de supprimer du code aide à faire évoluer le système vers un état où il n'y a que le code nécessaire — un état où il y a moins d'Entropie Logicielle. Mais les équipes de projet ont tendance à ignorer ce principe et à se concentrer principalement sur l'ajout de nouvelles fonctionnalités.

Pour éviter cela, je pense que les développeurs devraient être récompensés lorsqu'ils suppriment du code. Peut-être de la même manière (ou plus) que lorsqu'ils ajoutent de nouvelles fonctionnalités.

> Supprimer du code inutile devrait être récompensé.

Outre la complexité, le code inutile peut également représenter une partie d'une fonctionnalité qui ne fournit aucune valeur. Pour chaque fonctionnalité ou modification liée à cette fonctionnalité, vous avez plus de choses à tester, maintenir et supporter. C'est un coût inutile pour le projet, et un coût qui ne disparaît pas à moins d'être explicitement supprimé.

L'évolution a façonné nos esprits pour penser aux bénéfices à court terme. Ajouter des fonctionnalités ou corriger des bugs pour satisfaire l'objectif du projet conduit à un **bénéfice à court terme** dans le contexte de l'Entropie Logicielle. Cela est essentiel, mais ne devrait pas se faire au détriment de l'ajout ou de la conservation de code qui n'est pas nécessaire.

La caractéristique qui fait de nous des humains est notre capacité à penser à l'avenir. Notre capacité à réfléchir à ce qui compte vraiment pour un projet. Ce dont nous avons besoin, c'est de renforcer la culture de la suppression de code.

**Le code qui n'existe pas est le code dont vous n'avez pas à vous soucier**.

Après tout, pourquoi s'inquiéter de quelque chose dont vous n'avez pas besoin ?

Merci d'avoir lu. Si vous avez des commentaires, contactez-moi sur [Twitter](https://twitter.com/FagnerBrack), [Facebook](https://www.facebook.com/fagner.brack) ou [Github](http://github.com/FagnerMartinsBrack).