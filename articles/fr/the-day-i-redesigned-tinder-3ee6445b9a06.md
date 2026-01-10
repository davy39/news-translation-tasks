---
title: J'ai repensé Tinder. Voici ce que j'ai appris dans le processus.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-27T22:56:43.000Z'
originalURL: https://freecodecamp.org/news/the-day-i-redesigned-tinder-3ee6445b9a06
coverImage: https://cdn-media-1.freecodecamp.org/images/1*SGoCQhxcIQhk8uqtvTHB7A.png
tags:
- name: Design
  slug: design
- name: design thinking
  slug: design-thinking
- name: Product Design
  slug: product-design
- name: UI
  slug: ui
- name: UX
  slug: ux
seo_title: J'ai repensé Tinder. Voici ce que j'ai appris dans le processus.
seo_desc: 'By Daniel Lopes

  The challenge

  I set out to see how far I could push myself creatively as a designer by rebuilding
  an App I frequently use.

  I chose Tinder because I’ve used it a few times, and realized a few modifications
  to the design would be helpfu...'
---

Par Daniel Lopes

### **Le défi**

Je me suis lancé pour voir jusqu'où je pouvais me pousser créativement en tant que designer en reconstruisant une application que j'utilise fréquemment.

J'ai choisi Tinder parce que je l'ai utilisé quelques fois et j'ai réalisé que quelques modifications de design seraient utiles. Bien sûr, je ne suggère pas que mon design devrait être utilisé à la place du design actuel de Tinder. C'est juste un point de vue différent du design actuel de l'application.

Mes objectifs :

* Créer une meilleure expérience utilisateur
* Faciliter l'utilisation de l'application
* En tant qu'objectif personnel, terminer mon premier projet de design

### Comprendre l'application

Tinder est une application sociale basée sur la localisation, principalement utilisée comme application de rencontre avec un public cible de 18 à 34 ans. Depuis son lancement en 2012, Tinder a connu une croissance rapide grâce à sa méthode d'utilisation extrêmement simple et à sa stratégie organique incroyable.

### La page d'accueil

![Image](https://cdn-media-1.freecodecamp.org/images/Hlm4H50oYkWS4fgNVADR84qy7YyPl-3tT8fb)
_Ancien écran et ma refonte_

#### **Problème 1 : Boutons du bas et balayage des cartes**

Dès qu'un utilisateur ouvre l'application, les utilisateurs de Tinder ont deux fonctionnalités principales pour indiquer s'ils aiment un profil ou non :

* les boutons du bas
* le balayage des cartes

Alors, laquelle de ces options doivent-ils utiliser ?

Les deux options sont très bonnes, mais le balayage des cartes offre une expérience beaucoup plus fluide. Si vous le comparez à d'autres applications qui implémentent de plus en plus la fonctionnalité de balayage des cartes, Tinder est bien en avance. Nous devrions en tirer 100 % avantage.

Après avoir analysé le design existant, les boutons « super like », « like » et « nope » ont été supprimés, remplacés par les gestes de balayage des cartes pour ces actions.

Les nouveaux boutons suivants ont été ajoutés.

![Image](https://cdn-media-1.freecodecamp.org/images/KdEPMH3mZ-wNdtEyRJcRLKFgx3LnfRY1B-2O)
_Bouton Ignorer le profil_

#### **Ignorer le profil**

Disons que vous tombez sur un profil qui vous intéresse et en même temps ne vous intéresse pas, vous pouvez l'ignorer et passer au suivant.

![Image](https://cdn-media-1.freecodecamp.org/images/NjUJEUGGPxkqVaylt8hPsspd8WLvGhVf7Lyx)
_Bouton Message_

#### **Message**

Fonctionnalité pour Tinder Gold qui permettrait d'envoyer un message à n'importe quel profil, même s'ils ne vous ont pas encore aimé.

#### **Nouvelle carte de balayage - Amis**

![Image](https://cdn-media-1.freecodecamp.org/images/7HlXjOqILUz2V7ZVJ4-WPrPnpKqZOR0gIP5k)

Tinder est répertorié sous « Mode de vie » dans l'App Store. Bien que Tinder ne soit pas commercialisé comme une application de rencontre, la plupart des gens le voient comme tel. En parcourant les profils, j'ai vu de nombreuses biographies avec quelque chose comme « Je cherche juste des amis ! ».

Ainsi, balayer vers le bas sur les nouvelles cartes de balayage permet de devenir ami avec quelqu'un.

### **Problème 2 : Changer de pages pour voir un profil**

Cette modification était quelque chose de plus personnel. Je n'aimais pas la façon dont un utilisateur naviguait vers le profil d'une personne. Je n'ai pas considéré le processus fluide aux yeux de l'utilisateur, car nous changeons constamment de pages et cela ne devient pas très intuitif ou pratique si nous voulons revenir en arrière après avoir vu le profil.

J'ai donc décidé d'implémenter la fonction permettant de voir le profil de l'utilisateur sans quitter la page principale. Balayer **vers le haut** afficherait le profil de l'utilisateur et balayer **vers le bas** ramènerait l'utilisateur à la page principale.

![Image](https://cdn-media-1.freecodecamp.org/images/X4KR8o6KUdpj5Z6cy2yPbwBeTS3WBoS1xRgl)

### **Repenser le fil d'actualité de Tinder**

Tinder a introduit la fonctionnalité de fil d'actualité qui montre les mises à jour en temps réel de vos correspondances, le tout au même endroit. C'est une très bonne idée qui vous emmènera au-delà de « C'est un match ! » et vous aidera à établir une véritable connexion.

Mais pour accéder à cette nouvelle fonctionnalité, vous devez aller dans les messages. Comme je pense que nous devrions en tirer parti, j'ai décidé de la retirer des messages et de la placer sur l'écran principal.

Un utilisateur devrait simplement cliquer sur le bouton de fil d'actualité sur l'écran principal pour accéder à toutes les nouvelles de ses correspondances.

![Image](https://cdn-media-1.freecodecamp.org/images/53CoOUKDc8o6XVFIMi-wou32Qy963zUDPKXD)

Pour naviguer dans le fil d'actualité, j'ai décidé d'implémenter deux boutons :

* **Nouveau** - Cliquer sur « Nouveau » en bas de l'écran à droite créerait une nouvelle publication.
* **Ancien** - Cliquer sur « Ancien » en bas de l'écran à gauche naviguerait vers la publication la plus ancienne jusqu'à atteindre la dernière.

Les boutons :

* **Message** - Message instantané à la connexion sans quitter le fil d'actualité.
* **Partager** - Partage sur les réseaux sociaux.

### **Nouvelle fonctionnalité : Expériences Tinder**

La plupart des gens voient Tinder comme une application de rencontre. Mais c'est bien plus, l'expérience peut être plus puissante. J'ai implémenté une nouvelle fonctionnalité appelée « Expériences Tinder », une façon de porter les rendez-vous et les rencontres avec des amis à un autre niveau.

Découvrez des lieux de la ville où vous vous trouvez, rencontrez des personnes qui partagent vos passions, ouvrez-vous à de nouvelles expériences.

![Image](https://cdn-media-1.freecodecamp.org/images/ncJhBnZYUrfBLS93oErDtCaFJoFkxDejApOv)

### **Statut**

![Image](https://cdn-media-1.freecodecamp.org/images/ZjRZ8tTmS3yAnUrY-uobMUgHz5nnEQcyekke)

Il y a quelques autres choses qui peuvent être implémentées pour améliorer considérablement l'expérience utilisateur. L'une d'entre elles est de connaître le statut de l'utilisateur. Ainsi, de manière simple et minimaliste, j'ai inséré le statut des utilisateurs dans les messages. Cette amélioration nous permet de savoir si un utilisateur est en ligne, hors ligne ou inactif.

Une autre fonctionnalité possible est de filtrer les utilisateurs en fonction de leur dernière activité. Cela permettrait à un utilisateur de définir une plage dans vos « Préférences de découverte », par exemple, afficher les utilisateurs qui ont été actifs au cours des 30 dernières minutes.

### **Conclusion**

En me lançant dans ce projet, je savais que ce serait l'occasion parfaite pour moi d'améliorer mes compétences en design et de me pousser créativement. J'étudie l'ingénierie informatique et en même temps j'étudie le design seul à la maison, car je souhaite poursuivre une carrière dans le design de produits. J'ai compris que la meilleure façon pour moi d'apprendre serait de me lancer dans un projet.

Ainsi, pour moi, ce n'est pas la fin de la refonte d'une application mobile, mais seulement le début.

Merci d'avoir lu. J'espère que cela vous a plu. 😊

J'apprécierais vos commentaires.