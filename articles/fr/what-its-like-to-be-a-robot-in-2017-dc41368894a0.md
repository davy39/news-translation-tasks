---
title: À quoi ressemble la vie d'un robot
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-05T07:00:38.000Z'
originalURL: https://freecodecamp.org/news/what-its-like-to-be-a-robot-in-2017-dc41368894a0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1wfeIn-huOS_O8YkE2D2BA.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: General Programming
  slug: programming
- name: robotics
  slug: robotics
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: À quoi ressemble la vie d'un robot
seo_desc: 'By Ugo Cupcic

  Image credit: http://www.esa.int/images/DSC03062.JPG

  What it’s like to be a robot in 2017

  What will a state-of-the-art robot be able to do in 2017?

  There are many different types of robots out there, from humanoid robots to industrial
  a...'
---

Par Ugo Cupcic

*Crédit image :* [*http://www.esa.int/images/DSC03062.JPG*](http://www.esa.int/images/DSC03062.JPG)

À quoi ressemble la vie d'un robot en 2017

Que pourra faire un robot de pointe en 2017 ?

Il existe de nombreux types de robots différents, des robots humanoïdes aux bras industriels capables de se déplacer avec une précision et une vitesse incroyables.

Étant donné mon domaine d'expertise, je me concentrerai davantage sur la préhension et l'utilisation d'objets. Ce sont des compétences humaines essentielles que les robots doivent acquérir pour être véritablement utiles.

Mais pourquoi est-il si difficile pour un robot de reproduire ces compétences ?

Voici les capacités dont les robots ont besoin :

#### Pour un robot de préhension / manipulation

Sur le plan matériel, un robot de préhension ou de manipulation a besoin d'un bras, d'une main et d'un capteur 3D. Le bras possède généralement environ 6 degrés de liberté (pour référence, le bras humain en a 7). Cela permet d'atteindre n'importe quel point donné dans un espace de travail.

En plus d'un bon contrôle de position — être capable de diriger chaque articulation vers sa cible donnée rapidement et de manière fiable — le bras et la main ont également besoin d'un contrôle de couple fiable. Cela signifie que vous êtes capable d'appliquer un couple donné avec une articulation donnée.

Une main avancée aura également des capteurs tactiles, ce qui permet de manipuler les objets.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pZkMp3nu7Vy2AWrczT-Axw.png align="left")

[*Une scène 3D*](http://www.ros.org/news/assets_c/2015/06/pallet-thumb-480x375-1206.png) *acquise à partir d'un Kinect.*

Pour un robot moderne, comprendre son environnement est essentiel. Vous ne pouvez pas saisir ou utiliser un objet si vous ne pouvez pas le voir.

Le pipeline le plus souvent utilisé pour cette tâche est le suivant :

* Tout d'abord, le pipeline de vision exécutera un **algorithme de segmentation** pour isoler les différents objets dans la scène entrante, par exemple, un nuage de points 3D.

* Ensuite, il passera par quelques **étapes de reconnaissance**. Le but est d'identifier les objets si possible et d'aligner une maille connue de l'objet.

Les diagrammes ci-dessous sont assez simples par rapport au cas d'utilisation réel ci-dessus. Les avancées récentes en apprentissage profond montrent de grandes promesses dans ce domaine.

![Image](https://cdn-media-1.freecodecamp.org/images/1*aMZGwM0S39X80ClgQB-Knw.jpeg align="left")

![Image](https://cdn-media-1.freecodecamp.org/images/1*t0dA_wNPVGTj-Q_bElvr8Q.jpeg align="left")

![Image](https://cdn-media-1.freecodecamp.org/images/1*YqSI_SYz4xIeFcsEd7g8Gw.jpeg align="left")

*Scène complète / résultats segmentés : chaque objet est d'une couleur différente / chaque objet est reconnu, le modèle est aligné en bleu.*

Maintenant que le robot a une compréhension approximative de l'emplacement des objets dans la scène, il doit être capable de naviguer dans l'environnement en évitant les obstacles. C'est le domaine de la **planification de mouvement**. Il existe de nombreux algorithmes différents qui traitent de la planification de mouvement.

Maintenant que le robot a un moyen d'atteindre l'objet que vous voulez qu'il saisisse, vous devez savoir comment fermer la main autour de l'objet. Il existe différentes façons d'aborder ce problème, mais les deux approches principales les plus souvent utilisées sont la **planification de préhension** et l'**enseignement par démonstration**.

Dans l'approche de planification de préhension, l'algorithme utilise certaines heuristiques pour calculer différentes préhensions et évaluer les préhensions à l'aide d'une mesure de qualité de préhension. Dans l'approche d'enseignement par démonstration, un humain montre au robot comment effectuer l'action. L'algorithme extrait ensuite les informations pour rendre l'action fiable sur le robot.

![Image](https://cdn-media-1.freecodecamp.org/images/1*mzLe2WPFYwYjyNtpmX2aiw.jpeg align="left")

![Image](https://cdn-media-1.freecodecamp.org/images/1*D3tG6I1zahdxowE1MXOebw.jpeg align="left")

![Image](https://cdn-media-1.freecodecamp.org/images/1*ppexSOcsGhqdCQ-C8KSGPA.jpeg align="left")

*Enseignement par démonstration — ouvrir une bouteille à l'université de Bielefeld.*

Enfin, il est possible de fermer la boucle en utilisant les différents capteurs disponibles dans le robot pour accomplir une action, comme stabiliser une préhension lors de la détection d'un glissement, ou déplacer un doigt sur un objet sans le lâcher. Exécuter une boucle de contrôle serrée, puis utiliser ses données pour modifier la prochaine commande d'un robot est l'un des aspects les plus difficiles de la robotique.

# Comment pouvons-nous avancer

Il faudra beaucoup de travail pour développer toutes ces capacités et les faire fonctionner dans tous les environnements. Chaque individu et chaque département de robotique aura son propre domaine d'expertise spécifique. Par exemple, mon domaine d'expertise est la préhension et la manipulation, tandis que d'autres personnes se concentrent davantage sur les robots humanoïdes, les plateformes mobiles et la vision.

Nous sommes tous confrontés au même défi, cependant : résoudre des problèmes complexes avec des données peu fiables.

Les robots avancés sont encore trop souvent réservés aux spécialistes. Ils sont difficiles à programmer et nécessitent beaucoup de connaissances pour accomplir de nouvelles choses. Mais souvent, ce que vous voulez que votre robot fasse peut être décrit facilement. C'est une tâche que vous pourriez faire vous-même.

Pour résoudre ce problème, de plus en plus d'entreprises se tournent vers des interfaces de programmation visuelle en robotique : [Choregraphe de NAO](https://www.youtube.com/watch?v=q2ihy_mVpY8), [Robot Blockly](http://wiki.ros.org/blockly) (utilisé chez Shadow et Erle Robotics), et [Desk de Franka](https://www.franka.de/#chapter2).

![Image](https://cdn-media-1.freecodecamp.org/images/1*j-MZPZWl4KzmLNBWitthrg.png align="left")

*Interface Blockly de Shadow Robot.*

Mais pour pouvoir programmer des robots avancés de manière intuitive via ces interfaces, vous avez besoin de capacités avancées — et robustes.

Je suis personnellement convaincu que la voie à suivre est de construire de plus en plus d'intelligence à l'intérieur des outils eux-mêmes. De cette manière, chaque capacité peut être implémentée par des experts.

Cette approche de boîte noire facilite la combinaison de différentes capacités de haut niveau, en réutilisant les diverses techniques de pointe développées par différents experts. Les boîtes n'ont pas besoin d'être noires, mais le résultat devrait être que les utilisateurs finaux puissent se concentrer uniquement sur la fonctionnalité de cette boîte — ses entrées et ses sorties — au lieu d'être distraits par la manière dont cette fonctionnalité devrait être implémentée.

En tant que roboticien, si nous voulons que les robots avancés soient utiles aux non-spécialistes, nous devons simplifier l'interface. Mais pour cela, nous devons d'abord implémenter de plus en plus de capacités avancées, puis les intégrer à l'intérieur des outils eux-mêmes.

Si vous avez aimé cet article, pourquoi ne pas l'aimer et le partager ? De plus, si vous voulez discuter de robotique, connectons-nous sur [Twitter](http://twitter.com/ugocupcic).

![Image](https://cdn-media-1.freecodecamp.org/images/1*bYWLCSD5yxrMMlBV-nNaDA.gif align="left")