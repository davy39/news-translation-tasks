---
title: Comment j'ai remporté une bourse pour l'événement annuel d'Apple pour la deuxième
  fois
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-02T15:55:46.000Z'
originalURL: https://freecodecamp.org/news/how-i-won-a-scholarship-to-apples-yearly-event-for-the-second-time-f04f5f4636b1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*c3bEXoh-PxEi-XHYr6yeNw.png
tags:
- name: Design
  slug: design
- name: Life lessons
  slug: life-lessons
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment j'ai remporté une bourse pour l'événement annuel d'Apple pour la
  deuxième fois
seo_desc: 'By Renan Magagnin

  Introduction

  This article describes the process behind Mindblower, a game that was one of the
  selected submissions for the WWDC19 Scholarship. It is now available on the AppStore
  and GitHub.

  WWDC Scholarships reward students from al...'
---

Par Renan Magagnin

### Introduction

Cet article décrit le processus derrière _Mindblower_, un jeu qui a été l'une des soumissions sélectionnées pour la _Bourse WWDC19_. Il est maintenant disponible sur l'[AppStore](https://itunes.apple.com/us/app/mindblower-the-game/id1460079689) et [GitHub](https://github.com/RenanMagagnin/mindblower-wwdc19).

Les [_Bourses WWDC_](https://developer.apple.com/wwdc19/scholarships/) récompensent des étudiants du monde entier avec l'opportunité d'assister à l'événement annuel d'Apple. Les développeurs sélectionnés pour une bourse reçoivent un billet pour la WWDC, un hébergement pour la conférence et une année d'adhésion au _Programme Apple Developer_ gratuitement.

J'étais étudiant à l'Apple Developer Academy et c'était la deuxième fois que je remportais la bourse — mon projet de l'année dernière peut être trouvé [ici](https://github.com/renanmagagnin/orbs-wwdc18). J'étais incroyablement excité par la nouvelle et j'ai pensé partager le processus derrière le jeu qui m'a permis de recevoir cette opportunité une fois de plus.

Dans _Mindblower_, l'objectif est de souffler les esprits. Pour y parvenir, le joueur tire des grenades collantes qui sont affectées par des champs vectoriels. La boucle principale consiste à analyser chaque niveau, à élaborer un plan et à tirer avec précision.

### L'Idée

L'inspiration est venue de la combinaison d'être intrigué par les optimisations dans [_Frost_](https://www.youtube.com/watch?v=Ry7VFcDNUMA), l'un des gagnants des _Apple Design Awards 2018_, et des [vidéos sur les champs vectoriels par _3Blue1Brown_](https://www.youtube.com/watch?v=rB83DpBJQsE).

L'idée était d'optimiser le mouvement d'un grand nombre d'entités en utilisant des équations de champs vectoriels pour déterminer leur vitesse.

![Image](https://cdn-media-1.freecodecamp.org/images/JOyhTe5ksoTskTMY5XJ8uhSQikslIGUqQE0j)
_Un prototype précoce simulant un champ vectoriel vortex affectant de petites entités_

### Concept du Jeu

Le prototype montré ci-dessus a prouvé que cela pouvait, en effet, être la mécanique de base du jeu. Maintenant, il était temps de trouver les éléments principaux qui permettraient un gameplay intéressant :

* **Catapulte** : Permet au joueur de tirer des balles en déterminant leur vitesse initiale, étant donné la position fixe de la catapulte.
* **Objectif** : Au contact avec au moins une balle, enregistre que l'étape est complète.
* **Champs vectoriels obstacles** : Ceux-ci existent dans une tentative d'empêcher le joueur d'atteindre l'objectif.
* **Inverseurs** : Au contact avec une balle, font tourner l'orientation de chaque champ vectoriel dans l'étape de 180°.
* **Portails** : Existent en paires et toute balle qui entre par un portail, sort par l'autre.

![Image](https://cdn-media-1.freecodecamp.org/images/p6ZrWG2RbP4nVAPkcdTa9wMdA1S5ovLznkQM)
_Une version précoce du jeu avec une catapulte fonctionnelle, quelques champs vectoriels différents et l'objectif_

### Design des Niveaux

L'étape suivante était de créer des étapes qui, de manière intéressante, introduiraient progressivement les éléments du jeu et deviendraient de plus en plus difficiles.

Pour y parvenir, il y a eu beaucoup d'expérimentations avec les équations de champs vectoriels pour trouver celles qui conviendraient au jeu. Ensuite, des combinaisons de ces champs vectoriels et des autres éléments du jeu ont donné forme aux étapes dans la version finale du jeu.

![Image](https://cdn-media-1.freecodecamp.org/images/T6n0p35kWGg3cBW21bB7hIsi8FyhNhvaGDOk)
_Maquettes des étapes, qui introduisent progressivement tous les éléments du jeu avant de les combiner tous dans l'étape finale_

### Implémentation

À ce stade, l'idée était bien définie et les étapes étaient déjà planifiées, il était donc facile d'identifier les systèmes qui seraient nécessaires et ce qu'ils devraient supporter. Il est également devenu clair que la partie clé serait de faciliter la construction des étapes.

Avec cela en tête, les champs vectoriels ont été conçus pour supporter la personnalisation de leur équation d'accélération, de leur forme, de leur force, de leur couleur et de leur transparence.

Cela a permis de créer différentes étapes de manière plutôt élégante et facile — supportant même plusieurs catapultes ou objectifs. Cela a également évité la répétition de code et a atteint toutes les compositions présentes dans les étapes planifiées pour le jeu final.

### Design

Les graphismes ont été créés avec Sketch et des particules SpriteKit. L'intention était de suivre le thème néon de _WWDC19_ et de prendre littéralement la phrase d'Apple :

> _"Écrivez du code. Soufflez les esprits."_

La boucle principale composée d'une catapulte tirant des balles sur une plus grande balle représentant l'objectif a été améliorée. Maintenant, un arc néon tirait des grenades collantes sur un esprit à souffler. Cela n'était pas seulement plus visuellement attrayant, mais aussi plus intuitif.

![Image](https://cdn-media-1.freecodecamp.org/images/zyEC7uBvpM-iccPFxMebHlobcUjZMGMfjrAf)

Et, afin de rendre le succès plus satisfaisant, il était important de se concentrer sur sa partie centrale : l'explosion.

![Image](https://cdn-media-1.freecodecamp.org/images/jAbQA0hNX4mRqOtbAa1YHrBIKGOs1c9prddU)

Ce résultat a été obtenu en utilisant quatre particules différentes et plusieurs SKActions pour créer programmatiquement le rebond au contact et les morceaux de la tête volant partout (qui ont été exportés en 9 actifs différents).

En tant que touche finale, il était également important — avec des animations — de rendre les lumières néon réelles. Pour y parvenir, il a fallu beaucoup d'observation de références sur Internet et BEAUCOUP de fadeTo(alpha) et wait(forDuration) SKActions dans le code.

![Image](https://cdn-media-1.freecodecamp.org/images/aVnc2jMDXi7MeJZWqINkVRPlDWLBsI5MbKKd)

### Audio

L'audio a été réalisé à partir d'un mélange de sources en ligne et de certains effets sonores créés sur Garageband. Pour l'implémentation, des actions SpriteKit et le framework AVFoundation ont été utilisés.

La musique de fond utilisée est [Paradise by Juno Dreams](https://www.youtube.com/watch?v=Iedf8baVdDM) et a été trouvée dans l'awesome [mixtape by NewRetroWave](https://www.youtube.com/watch?v=yV_MsBiTVsc&t) sur YouTube. Elle correspondait simplement si bien au thème et au jeu.

### Adaptation au Format PlaygroundBook

Puisque le jeu a été entièrement réalisé avec SpriteKit, la transition a été presque sans stress, ne nécessitant que l'exigence classique de marquer presque tout dans le code comme _public_.

La dernière étape consistait à fournir une page d'instructions dans le livre de terrain de jeu. L'objectif était de n'y inclure que les instructions nécessaires, tout en la gardant aussi concise que possible, afin de garder l'accent sur le jeu.

### Conclusion

En rétrospective, je crois que ce qui a le plus contribué à la qualité du résultat final a été ce qui suit :

1. **Être curieux** : Les idées intéressantes peuvent venir de n'importe quoi. Pour moi, c'était lorsque je me suis demandé : "Comment les gens de [Frost](https://www.youtube.com/watch?v=Ry7VFcDNUMA) ont-ils fait cela ? Comment est-ce que _je_ le ferais ?"
2. **Élaborer un plan** : Valider l'idée avant même de penser à l'implémentation était crucial. Avoir une idée claire de l'objectif final a rendu l'identification des meilleures approches beaucoup plus facile.
3. **Créer pour les gens** : Faire de l'expérience du joueur/utilisateur votre priorité numéro un. Faites tourner chaque décision autour de cela.

Merci beaucoup d'avoir lu. Si vous avez des questions, des suggestions ou des commentaires, n'hésitez pas à les écrire dans la section des commentaires ci-dessous ou à me les envoyer directement, je serai ravi de répondre.