---
title: Qu'est-ce que le Strangler Fig Pattern et comment il aide à gérer le code hérité
subtitle: ''
author: Kealan Parr
co_authors: []
series: null
date: '2021-06-15T17:43:43.000Z'
originalURL: https://freecodecamp.org/news/what-is-the-strangler-pattern-in-software-development
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/Strangler-Fig.png
tags:
- name: Productivity
  slug: productivity
- name: 'self-improvement '
  slug: self-improvement
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: Qu'est-ce que le Strangler Fig Pattern et comment il aide à gérer le code
  hérité
seo_desc: 'Any sufficiently old codebase eventually starts to contain legacy code.
  Architecture, performance, comments, and more begin to degrade the moment after
  they are written.

  Some parts of the codebase last longer than other parts, but inevitably new codi...'
---

Tout code suffisamment ancien finit par contenir du code hérité. L'architecture, les performances, les commentaires et plus encore commencent à se dégrader dès qu'ils sont écrits.

Certaines parties du code durent plus longtemps que d'autres, mais inévitablement, de nouvelles normes de codage émergent pour réduire la dette technique. Ensuite, vous devez retravailler une grande application, sans temps d'arrêt, en adoptant une "nouvelle façon" de travailler sans rien casser dans votre version ou développement.

Le **Strangler Fig Pattern** est une méthode efficace pour résoudre ce problème.

## Qu'est-ce qu'un Strangler Fig ?

Le nom **[Strangler Fig Pattern](https://en.wikipedia.org/wiki/Strangler_fig)** vient en réalité d'une collection de plantes qui poussent en "étranglant" leurs hôtes.

Elles poussent dans des zones où la compétition pour la lumière est intense, et elles ont évolué pour que leurs graines soient dispersées (normalement par des oiseaux) au sommet d'un arbre hôte où elles peuvent facilement obtenir de la lumière.

Leurs racines poussent vers le bas autour de l'arbre et les jeunes pousses poussent vers le haut pour consommer toute la lumière possible. Cela "étrangle" l'arbre et les jeunes pousses de figuier peuvent souvent tuer leur arbre hôte sur lequel elles ont atterri.

Voici une image d'un Strangler Fig, que j'ai trouvée sur Wikipedia.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-99.png)
_Une image d'un figuier étrangleur, où les racines poussent le long du tronc de l'arbre jusqu'au sol tandis que les jeunes pousses poussent au-dessus de la canopée des arbres. [Source](https://upload.wikimedia.org/wikipedia/commons/4/46/Ficus_watkinsiana_on_Syzygium_hemilampra-Iluka.jpg)._

Alors, comment cela s'applique-t-il au logiciel ? 🤔

# Qu'est-ce que le Strangler Fig Pattern ?

Réécrire complètement une grande base de code complexe avec de nombreuses interactions différentes, souvent avec différentes équipes, entraîne un cauchemar de planification.

Dans de grands projets **brown-field** compliqués comme celui-ci, le **big-bang** (où tout est publié en une fois) vous oblige généralement à :

* comprendre chaque interaction en profondeur pour vous assurer de ne rien casser lors de la publication
* avoir toutes les nouvelles corrections de bugs faites à la fois dans le nouveau et l'ancien code pendant que vous le réécrivez
* garder les deux fusionnés et à jour
* passer des semaines en test
* gérer des tonnes d'appels et de support en dehors des heures pour le déploiement de la nouvelle base de code

Pour couronner le tout, cela se termine généralement par des développeurs faisant beaucoup d'heures supplémentaires avec un afflux de bugs.

Une grande difficulté que nous essayons de supprimer lorsque nous utilisons le **Strangler Fig** est de faire prendre conscience à ceux qui utilisent votre logiciel de l'endroit où votre nouveau logiciel est maintenant accessible.

Lorsque vous réécrivez votre backend, par exemple, si vous mettez tout sur un nouveau point de terminaison et demandez gentiment à vos utilisateurs de pointer vers votre nouveau point de terminaison. Mais si quelque chose ne va pas, vous devrez peut-être leur demander à tous de pointer à nouveau vers l'ancien.

Vous pourriez finir par aller et venir entre ces deux points de terminaison si vous avez des bugs vraiment difficiles, ce qui pourrait frustrer vos utilisateurs.

Lorsque nous utilisons le **Strangler Fig pattern**, nous pouvons éviter tout ce qui précède.

## Pourquoi étrangler notre code

Le **Strangler Fig pattern** vise à réécrire progressivement de petites parties de votre base de code, jusqu'à ce qu'après quelques mois/années, vous ayez étranglé toute votre ancienne base de code et qu'elle puisse être totalement supprimée.

Le flux approximatif est : ajouter une nouvelle partie à votre système qui n'est pas encore utilisée, activer la nouvelle partie du code - normalement avec un feature flag pour qu'elle coexiste avec l'ancien code - et enfin supprimer l'ancien code.

### Avantages du Strangler Fig pattern

En plus de vous aider à éviter tous les problèmes que nous avons déjà discutés, il permet également :

* de réduire votre risque lorsque vous devez mettre à jour des choses
* de commencer à vous donner immédiatement un certain avantage pièce par pièce
* de pousser vos changements en petites pièces modulaires, plus faciles à publier
* d'assurer un temps d'arrêt zéro
* d'être généralement plus agile
* de rendre vos retours en arrière plus faciles
* de vous permettre de répartir votre développement sur la base de code sur une période plus longue si vous avez plusieurs priorités.

Il existe plusieurs façons de mettre en œuvre le **Strangler Fig pattern** et cela dépend du système que vous supprimez, etc. Alors, devenons concrets et couvrons un exemple.

## Exemple de fournisseur de paiement façade

Supposons, par exemple, que vous avez une énorme base de code back-end monolithique pour gérer les paiements. Elle est **énorme**. Quelques millions de lignes de code, avec plusieurs points de terminaison, que vous souhaitez réécrire en quelque chose de nouveau pour votre entreprise, pour une multitude de raisons.

Les performances sont maintenant médiocres, l'architecture est trop confuse pour intégrer de nouveaux développeurs, et il y a beaucoup de [code mort](https://www.freecodecamp.org/news/antipatterns-to-avoid-in-code/) que vous devez supprimer mais sans rien casser.

Casser une énorme base de code impliquant des paiements clients pourrait bien faire perdre son emploi au développeur malchanceux qui a poussé en dernier !

D'accord. Comment étranglez-vous lentement cette ancienne base de code ? Encore plus délicat, vous ne voulez pas simplement mettre un nouveau point de terminaison et forcer tout le monde à se déplacer. Vous avez des centaines de clients utilisant ce logiciel, ils ne peuvent pas simplement basculer entre vos points de terminaison si vous avez des bugs et devez revenir en arrière.

Pour ajouter un dernier défi, vous ne voulez pas non plus changer vos interfaces vers ces points de terminaison. Tout ce qui est passé en arguments ou retourné doit rester le même.

## Solution basée sur le Strangler Fig Pattern

Nous pouvons créer une façade qui intercepte les requêtes allant vers les points de terminaison hérités.

La nouvelle façade transmettra à la nouvelle API que vous avez écrite, ou transmettra à l'API héritée si vous n'avez pas encore réécrit cette partie de la base de code.

Cette façade est essentiellement un [shim](https://en.wikipedia.org/wiki/Shim_(computing)) pour intercepter les requêtes réseau et les transmettre au bon endroit.

Vous pouvez ensuite migrer progressivement vers la nouvelle API pièce par pièce, et vos utilisateurs ne seront pas conscients des changements apportés à votre code sous-jacent car vous l'aurez correctement abstrait.

Si vous faites cela correctement, vous ferez généralement :

* Avoir uniquement la méthode héritée au début
* Créer la nouvelle API
* La faire coexister avec l'API héritée, où vous pouvez l'activer et la désactiver avec des feature flags
* Transférer de plus en plus vers la nouvelle API
* Supprimer l'ancienne méthode une fois entièrement migrée

La partie "étranglement" se produit pièce par pièce où vous retirez de plus en plus de responsabilités de l'API héritée vers la nouvelle API.

## **Conclusion**

J'espère que cela a expliqué ce qu'est le **Strangler Fig Pattern** ainsi que certains de ses avantages.

J'ai vu ce modèle utilisé dans des projets logiciels réels et il fonctionne _vraiment efficacement_. C'était facilement l'un des projets les plus compliqués sur lesquels j'ai travaillé et le **Strangler Fig** l'a rendu beaucoup plus facile.

Il vous empêche d'écrire des projets logiciels pendant des mois, puis de croiser les doigts et de les envoyer en production en espérant n'avoir rien oublié.

Il y avait deux ressources inestimables qui ont été très utiles lorsque j'écrivais cela :

* _Strangler Fig Application_ par Martin Fowler [ici](https://martinfowler.com/bliki/StranglerFigApplication.html), et
* _Avoid rewriting a legacy system from scratch, by strangling it_ trouvé [ici](https://understandlegacycode.com/blog/avoid-rewriting-a-legacy-system-from-scratch-by-strangling-it/).

Je partage mes écrits sur [Twitter](https://twitter.com/kealanparr) si vous avez aimé cet article et souhaitez en voir plus.