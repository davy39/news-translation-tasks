---
title: Comment construire votre propre casque VR pour 100 $
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-20T11:44:27.000Z'
originalURL: https://freecodecamp.org/news/build-your-own-vr-headset-for-100-13d6f2b06385
coverImage: https://cdn-media-1.freecodecamp.org/images/1*S7v2UiCN4mJV2Llk98tuCA.jpeg
tags:
- name: open source
  slug: open-source
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Virtual Reality
  slug: virtual-reality
seo_title: Comment construire votre propre casque VR pour 100 $
seo_desc: 'By Maxime Coutte

  My name is Maxime Peroumal. I’m 16 and I built my own VR headset with my best friends,
  Jonas Ceccon and Gabriel Combe. And it ended up costing us $100.

  I started programming when I was 13, thanks to my math teacher. Every Monday and
  ...'
---

Par Maxime Coutte

Je m'appelle Maxime Peroumal. J'ai 16 ans et j'ai construit mon propre casque VR avec mes meilleurs amis, Jonas Ceccon et Gabriel Combe. Et cela nous a coûté 100 $.

J'ai commencé à programmer à l'âge de 13 ans, grâce à mon professeur de maths. Chaque lundi et mardi, mes amis et moi allions dans sa classe pour apprendre et pratiquer au lieu de manger à la cafétéria.

J'ai passé un an à construire un OS 8 bits très basique à partir de zéro et à participer à des concours de robotique avec mes amis.

Je me suis ensuite intéressé à la VR et avec mes amis, nous avons convenu qu'il serait vraiment cool de créer notre propre monde en VR où nous pourrions passer du temps après l'école. Mais face au fait qu'un Oculus coûtait 700 $ à l'époque, nous avons décidé de construire notre propre casque.

![Image](https://cdn-media-1.freecodecamp.org/images/RVxl0N2jdbFhf7gESlIURUc0QYT3dPctNRaK)
_Pièces imprimées en 3D du casque_

### Rendre la VR accessible à tous ?

![Image](https://cdn-media-1.freecodecamp.org/images/F5NUB8PwLFyV9FIyG4IMAXNrju71nMZwbzmw)
_DARROW; J. R. EYERMAN/THE LIFE PICTURE COLLECTION/GETTY IMAGES_

C'est à cause d'un anime appelé _Sword Art Online_ où le personnage principal est dans un RPG de réalité virtuelle que je suis tombé amoureux de la VR. Je voulais comprendre chaque aspect de celle-ci.

J'ai acheté les composants les moins chers que j'ai pu trouver et nous avons commencé par apprendre les bases de la physique et des maths derrière la VR (accélération propre, antiderivatives, quaternions…). Et puis nous avons réinventé la VR. J'ai écrit [WRMHL](https://medium.freecodecamp.org/you-can-now-create-an-arduino-and-unity3d-interactive-experience-without-latency-2d7388dcc0c), puis [FastVR](https://github.com/relativty/fastVR-sdk) avec Gabriel. En mettant tout cela ensemble, nous avons obtenu un casque VR à 100 $.

![Image](https://cdn-media-1.freecodecamp.org/images/r7lT43yWgmgvO8r8GMeFRz1PSeZQEp2ABZPw)

### Un casque VR et un kit de développement entièrement modifiables

Pour accélérer le temps de développement VR, nous avons construit FastVR, un SDK open-source pour les développeurs qui est facile à comprendre et à personnaliser. Cela fonctionne comme suit :

* Le casque principal calcule la position du casque dans l'espace ;
* La position est envoyée du casque à [**WRMHL**](https://medium.freecodecamp.org/you-can-now-create-an-arduino-and-unity3d-interactive-experience-without-latency-2d7388dcc0c), et une partie de la puissance du CPU est dédiée à la lecture de ces messages ;
* Ensuite, [**FastVR**](https://github.com/relativty/fastVR-sdk) récupère les données et les utilise pour rendre le jeu VR.

Tout ce dont vous avez besoin pour construire le casque a été open-sourcé et peut être modifié.

![Image](https://cdn-media-1.freecodecamp.org/images/-2xejLIdyQa9BFuKKVnrnMsBOGPEaXcBJCgW)

### Pourquoi open source ?

![Image](https://cdn-media-1.freecodecamp.org/images/lEfatukim7bZsKDWueEyw77FPkqm3WOiWXtR)

Je veux rendre la VR grand public. J'ai donc contacté [Oussama Ammar](https://www.freecodecamp.org/news/build-your-own-vr-headset-for-100-13d6f2b06385/undefined), l'un des cofondateurs de The Family. Je lui ai parlé de la création d'une entreprise et du lancement d'un Kickstarter.

Mais il m'a convaincu que pour l'instant, il est préférable d'attendre pour démarrer une entreprise, de continuer à rencontrer d'autres personnes ayant les mêmes objectifs et de continuer à apprendre.

Nous avons fait un voyage dans la Silicon Valley et Oussama m'a présenté l'architecte en chef chez Oculus, Atman Brinstock. Et ils m'ont donné quelques conseils précieux : rendre tout cela open source.

### La prochaine étape ?

Il reste encore beaucoup de points techniques que nous voulons améliorer.

Notre grand objectif pour l'instant est un casque VR autonome, que nous avons déjà en version simple, et un suivi 3D moins cher.

Tout cela sera bientôt publié.

### Comment commencer ?

Si vous voulez en savoir plus sur le côté technique et construire votre casque, suivez simplement le guide en [**cliquant ici**](https://github.com/relativty/Relativ). Étoilez le dépôt si vous l'avez aimé ⭐

J'adorerais entendre parler de ce que vous avez vécu en construisant le casque, ou si vous avez besoin d'aide ou avez des questions. Contactez-moi à [**maxime@relativty.com**](mailto:maxime@relativty.com) ou [@MaximePeroumal](https://twitter.com/MaximePeroumal).