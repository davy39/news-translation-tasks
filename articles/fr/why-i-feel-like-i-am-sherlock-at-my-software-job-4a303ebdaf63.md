---
title: Je me sens comme Sherlock, s'il était développeur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-10-30T08:16:07.000Z'
originalURL: https://freecodecamp.org/news/why-i-feel-like-i-am-sherlock-at-my-software-job-4a303ebdaf63
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-CNoGje_a2x2Nziq0pru-w.jpeg
tags:
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Je me sens comme Sherlock, s'il était développeur
seo_desc: 'By DHARA DOSHI

  It’s a normal day at work. My boss assigned me an issue that I know nothing about.
  And I’m supposed to solve it as fast as possible.

  Somewhere in a massive project is a piece of code that keeps crashing. To me, it
  feels as electrifying...'
---

Par DHARA DOSHI

C'est une journée de travail normale. Mon patron m'a assigné un problème dont je ne sais rien. Et je suis censé le résoudre le plus rapidement possible.

Quelque part dans un projet massif se trouve un morceau de code qui continue de planter. Pour moi, c'est aussi électrisant qu'un mystère de meurtre.

Heureusement pour moi, le débogage et l'investigation vont de pair.

Bienvenue sur la scène de crime !

Il y a des indices. Certains soupçons évidents. Certaines empreintes digitales.

Mais rien de définitif.

Je traque les suspects habituels, mais ils ne mènent à rien.

> « Il n'y a rien de plus trompeur qu'un fait évident. »
> – [**Arthur Conan Doyle**](https://www.goodreads.com/author/show/2448.Arthur_Conan_Doyle) **dans [The Boscombe Valley Mystery](https://www.goodreads.com/work/quotes/1214700)**

Je fais appel à l'aide de mon équivalent du Dr. Watson : mon [IDE](https://en.wikipedia.org/wiki/Integrated_development_environment).

Je place quelques points d'arrêt. J'ajoute quelques moniteurs.

Je fais un peu plus de brainstorming.

Je rejoue la scène de crime encore et encore, en investiguant les faits.

En parcourant la trace de la pile, j'ai un éclair de compréhension qui m'aide à affiner ma recherche.

Je ressens une bouffée d'enthousiasme en entrant dans une fonction et en ajoutant un point d'arrêt spécifique.

Et quelques instants plus tard, je sors de mon état de concentration, ayant résolu le bug.

Vous voulez savoir quel était le problème ?

Si vous connaissez un peu le C, jetez un coup d'œil à ce bloc de code et voyez si vous pouvez trouver un indice sur ce qui a mal tourné :

```
FILE *fd;char *filename="models/";strcat(filename,"bullet");strcat(filename,".h3d");if( (fd = fopen(filename,"r"))==NULL ){    printf("\nFile or Directory not found");    return;}
```

D'accord, roulement de tambour… voici la cause du problème :

C'était une [erreur de segmentation](https://en.wikipedia.org/wiki/Segmentation_fault). Simple et clair.

```
char *filename="models/"; // Il s'agit d'une chaîne littérale stockée en mémoire en lecture seule
```

```
Lorsque nous utilisons strcat pour ajouter à "filename", c'est un comportement indéfini car nous n'avons pas le droit d'écrire dans cette mémoire en lecture seule.
```

Alors, comment ai-je résolu le problème ?

J'ai alloué un tampon mémoire suffisamment grand pour stocker le chemin complet du fichier.

```
char filename[256]; // Alternativement, vous pouvez allouer dynamiquement strcpy(filename, "models/");strcat(filename,"bullet");strcat(filename,".h3d");
```

Maintenant, vous voyez comment je ne peux m'empêcher d'être Sherlock-isé.

Restez à l'écoute pour le prochain mystère !

[**Abonnez-vous à mes publications Medium**](https://powered.by.rabbut.com/p/Ntce?c=0)  
[_Entrez votre email pour recevoir des mises à jour de ma part._powered.by.rabbut.com](https://powered.by.rabbut.com/p/Ntce?c=0)