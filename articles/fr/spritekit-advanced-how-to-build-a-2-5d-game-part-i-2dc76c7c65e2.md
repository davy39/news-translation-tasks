---
title: SpriteKit Avancé — Comment construire un jeu 2,5D (Partie I)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-01T20:04:38.000Z'
originalURL: https://freecodecamp.org/news/spritekit-advanced-how-to-build-a-2-5d-game-part-i-2dc76c7c65e2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*UfZWvFeWyuKgOIlkuU1log.png
tags:
- name: Game Development
  slug: game-development
- name: iOS
  slug: ios
- name: mobile app development
  slug: mobile-app-development
- name: SpriteKit
  slug: spritekit
- name: 'tech '
  slug: tech
seo_title: SpriteKit Avancé — Comment construire un jeu 2,5D (Partie I)
seo_desc: 'By Luke Konior

  Intro

  This article is about graphical evolution of Raft Challenge from the prototype to
  the final product. It’s AIM-ed for the people who are thinking about making their
  own game with graphics like Raft, but don’t know exactly how to s...'
---

Par Luke Konior

### Introduction

Cet article traite de l'évolution graphique de [Raft Challenge](https://itunes.apple.com/app/apple-store/id1073887270?pt=117756562&ct=Develop%20Articles&mt=8), du prototype au produit final. Il est destiné aux personnes qui envisagent de créer leur propre jeu avec des graphismes similaires à Raft, mais qui ne savent pas exactement comment commencer.

### Les tout débuts de Raft Challenge

Raft Challenge est né lors du premier hackathon organisé par [All In Mobile](https://www.allinmobile.co). L'idée était de créer un jeu où un joueur évite des obstacles. Nous voulions garder les choses aussi simples que possible.

Après le week-end, nous avions un prototype qui ressemblait à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/2IVkfJ6Zhe1RZbQhi-7d7ofu1jjmQwxdyjFD)

Raft Challenge a remporté le hackathon. L'entreprise a annoncé qu'elle allouerait des ressources pour améliorer le jeu.

### Faisons-en un jeu 2,5D !

Au début du projet, Raft avait les graphismes les plus simples possibles. Une vue était directement au-dessus d'une texture de sol plate, avec des cercles colorés indiquant le joueur et les ennemis. C'était beau et aussi simple que le code sous-jacent. Ensuite, notre [designer graphique](https://dribbble.com/allinmobile) est arrivé et a tout bouleversé. Il a dit : « Faisons-en un jeu 2,5D ! ». Le défi a été accepté et l'animation ci-dessus en a été le résultat.

Après le hackathon, il est réapparu une fois de plus. Cette fois, c'était plus qu'une simple phrase.

C'était un sourire malicieux et cette vidéo :

![Image](https://cdn-media-1.freecodecamp.org/images/EUGZnxZdfPYruZCbvOQYer-2Mg858pUe4RrA)

### Explication de la perspective

D'accord, arrêtons de jouer la comédie :-). J'ai voulu lui donner l'impression qu'il était aux commandes. Mais c'est moi le patron ici ! La perspective est facile à implémenter en code, quel que soit le moteur 2D que nous utilisons.

Tout d'abord, nous devons déterminer où nous voulons placer le [point de fuite](https://en.wikipedia.org/wiki/Perspective_%28graphical%29#One-point_perspective). L'exemple ci-dessous montre ce point au centre de la toile.

![Image](https://cdn-media-1.freecodecamp.org/images/7-ygj-gLXH3jM-z430XHGVEtxqgsvOqfMQXa)

Raft Challenge a ce point dans la moitié supérieure de l'écran, car le ciel et tout ce qui se trouve au-dessus n'est pas aussi important que les obstacles sur la rivière.

Comment les sprites eux-mêmes sont-ils créés ? Bien que cela puisse être évident pour quelqu'un avec un background artistique, ce n'est pas nécessairement clair pour une personne technique.

Il y a deux règles :

![Image](https://cdn-media-1.freecodecamp.org/images/W9bUzPWIZwFZdXJRvUm4swbWjMlOoXbrmMOR)

* Les parties mobiles doivent être dessinées le long des lignes d'aide comme montré ci-dessus
Tous ces lignes se croisent au point de fuite

**Note :** La partie côte n'atteint pas le point de fuite. Elle s'arrête quelque part au milieu, laissant une zone transparente derrière.

![Image](https://cdn-media-1.freecodecamp.org/images/8L66ks8EFml12WsVuZzyiA791N7pKWx0-cX6)

* Cette zone vide entre le graphique et le point de fuite a un but important
Elle contiendra des éléments qui sont plus éloignés.

Ces parties sont faites en appliquant une échelle deux fois plus petite à chaque étape. L'image résultante doit être sans couture si la texture est bien faite.

### Assemblage de la scène

![Image](https://cdn-media-1.freecodecamp.org/images/e2CuoGVjG4UBNTO1rKtcGs1ySZUw7lMwTwF3)

Après avoir préparé tous nos actifs, nous devons les mettre tous dans la scène.

Voyons à quoi cela ressemble dans Raft Challenge.

![Image](https://cdn-media-1.freecodecamp.org/images/BtVv7dU8oH3xX-xccye5FxzcIhMaC3wpAcf8)

En partant du bas :

1. Couches d'arrière-plan
   Arrière-plan
   Herbe
   Brouillard bas
   Soleil
   Montagnes
   Ligne d'horizon

* Ces couches sont toutes statiques, elles ne bougent pas
* L'arrière-plan fait office à la fois de ciel et d'eau
* L'arrière-plan est un simple dégradé
   Il est étiré pour remplir tout l'écran de l'appareil
   Le ratio d'aspect est ignoré
* Nous pouvons fusionner les couches autres que l'arrière-plan pour augmenter les performances, sauf si nous voulons changer certaines propriétés
* Nous pouvons déplacer le soleil pendant le gameplay
   ou remplacer les montagnes par quelque chose de différent

2. Couches de perspective
   Arbres avec reflets
   Côte
   Obstacles

* Pour la clarté de l'image ci-dessus, les couches avec un contenu similaire ont été regroupées
   Il y avait :
   2 couches d'obstacles
   8 couches de côte
   8 couches d'arbres avec reflets
* Ces couches sont agrandies par 2 lorsque le joueur avance
* L'ordre de ces couches dépend de
   la distance
   les plus proches sont en haut
   la priorité
   Obstacle > Côte > Arbres

3. Personnage

* Si un obstacle est dans la position la plus proche possible, il peut avoir une position z plus élevée que le personnage lui-même
   Dans ce cas, l'obstacle couvre le personnage, ce qui est souhaitable

4. GUI

* De bons graphismes doivent dépendre des illusions et des astuces plutôt que du matériel

![Image](https://cdn-media-1.freecodecamp.org/images/N9yKZLZ8BBoBIfjSzyLjf1sxUdx8h08DPUtT)

### Résumé

Cet article devrait nous donner une idée de la manière d'aborder le problème de la création d'actifs pour un jeu 2,5D et de leur organisation dans une scène.

Vous pouvez lire [la partie 2 de cette série ici](https://medium.freecodecamp.org/spritekit-advanced-how-to-build-a-2-5d-game-part-ii-30ddb613b568).

À propos de l'auteur : Kamil Ziętek est un développeur iOS chez [www.allinmobile.co](http://www.allinmobile.co)