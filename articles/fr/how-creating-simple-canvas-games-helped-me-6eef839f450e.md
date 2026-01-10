---
title: Comment la création de jeux HTML5 canvas m'a aidé à apprendre la programmation
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-05-25T04:54:08.000Z'
originalURL: https://freecodecamp.org/news/how-creating-simple-canvas-games-helped-me-6eef839f450e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*bm6Nb2cCdNWKFZh1TKDnAw.jpeg
tags:
- name: GameDev
  slug: gamedev
- name: Games
  slug: games
- name: gaming
  slug: gaming
- name: General Programming
  slug: programming
- name: women in tech
  slug: women-in-tech
seo_title: Comment la création de jeux HTML5 canvas m'a aidé à apprendre la programmation
seo_desc: 'By Surbhi Oberoi

  Like many 9 year-olds, the first thing I did when our family got a computer was
  install games on it. My brother and I would tussle after school over who got to
  play before mom or dad got home and booted us off of it.

  As I grew up, my...'
---

Par Surbhi Oberoi

Comme beaucoup d'enfants de 9 ans, la première chose que j'ai faite lorsque ma famille a eu un ordinateur a été d'y installer des jeux. Mon frère et moi nous disputions après l'école pour savoir qui pouvait jouer avant que maman ou papa ne rentrent et nous éjectent de l'ordinateur.

En grandissant, mes intérêts se sont éloignés des jeux vidéo et se sont tournés vers la lecture. Puis, il y a quelques jours, mon ami m'a montré Super Mario sur son téléphone. Et juste comme ça, j'ai été de nouveau accro aux jeux.

Une pensée m'est venue à ce moment-là : pourquoi ne pas créer un jeu ? Maintenant que j'apprends à coder avec [Free Code Camp](http://www.freecodecamp.com), je pourrais peut-être créer un jeu basique. Mais je n'avais aucune idée par où commencer. Alors j'ai commencé à chercher sur Google.

J'ai découvert l'API canvas et comment elle pouvait être utilisée pour créer des jeux basiques. J'ai suivi le cours HTML5 Canvas d'Udacity. Il m'a fallu trois jours pour enfin comprendre les concepts du canvas.

Après le cours, j'ai toujours senti que j'avais besoin d'un tutoriel pour m'apprendre à construire un jeu à partir de zéro, étape par étape, alors j'en ai suivi un. Cela m'a révélé que je manquais encore certaines bases de la programmation orientée objet, alors j'ai trouvé un autre cours sur Udacity pour le JavaScript orienté objet.

C'était assez dense et cela a pris un certain temps à digérer. J'ai dû regarder certaines vidéos deux fois pour les comprendre. Mais finalement, j'ai terminé de regarder toutes les vidéos et je suis arrivé au dernier chapitre où l'on crée enfin un jeu. Le bon côté de ce cours était qu'ils fournissaient déjà un framework de jeu.

Le jeu s'appelait "Frogger", où un sprite devait traverser un chemin rempli d'insectes sans entrer en collision avec aucun d'eux. Le sprite pouvait également collecter des gemmes pour marquer des points supplémentaires.

Pour commencer, j'ai forké leur dépôt GitHub. Il y avait déjà des fichiers créés — comme lorsque l'on utilise un générateur comme Yeoman — et le JavaScript était divisé en trois fichiers : app.js, engine.js et resources.js. Tout ce que j'avais à faire était de remplir les fonctions pré-écrites. Comme ces fonctions étaient déjà nommées, j'ai eu une bonne idée des arguments à passer et des boucles à créer.

Il y a trois aspects importants à tout jeu :

1. **La boucle de jeu** — elle répète un processus, de sorte que le jeu ne s'arrête pas à moins que vous n'appeliez la fonction pour l'arrêter.
2. **Le rendu** — prendre des indices des travaux back-end et afficher des sprites sur le front-end (en utilisant canvas, dans ce cas).
3. **La mise à jour** — mettre à jour les positions des sprites selon les mouvements spécifiés.

Cela peut sembler facile pour quelqu'un qui code depuis des années, mais commencer à partir de zéro nécessite beaucoup de patience.

Après pas mal de réflexion et de correction de bugs, le jeu a fonctionné. Même s'il était assez basique, la joie immense que j'ai ressentie en ayant créé un jeu était énorme.

Voici à quoi ressemble mon jeu :

![Image](https://cdn-media-1.freecodecamp.org/images/3j42Ds26BjFQWgjh2otYaOt2T93hmi30t5Bf)

Et voici mon code sur GitHub :

[**surbhioberoi/frontend-nanodegree-arcade-game**](https://github.com/surbhioberoi/frontend-nanodegree-arcade-game)  
[_Contribute to frontend-nanodegree-arcade-game development by creating an account on GitHub._github.com](https://github.com/surbhioberoi/frontend-nanodegree-arcade-game)

Ce jeu peut être amélioré de plusieurs manières, par exemple en utilisant des entrées aléatoires. Ici, j'ai codé en dur les positions, ce qui n'est pas une bonne pratique. J'apprends à faire les choses de manière plus efficace, et la première étape est de reconnaître qu'une meilleure méthode existe.

Pendant le week-end, j'ai pratiqué Canvas un peu plus, et c'était amusant ! J'ai créé des choses simples sur [JSfiddle](https://jsfiddle.net/) — tout ce qui me passait par la tête et qui pouvait utiliser canvas.

Je voulais créer quelque chose de plus maintenant. J'avais entendu parler du Jeu de la Vie de Conway. Au début, je pensais que ce serait vraiment difficile à créer. Malgré mon scepticisme quant à ma capacité à le réaliser, j'ai simplement commencé à y réfléchir.

Il y a deux choses très importantes sur le codage que j'ai apprises après avoir fait beaucoup d'erreurs stupides : **Ne paniquez jamais !** Tout est réalisable — il suffit de trouver comment. Et **ne commencez jamais à écrire du code tout de suite.** Prenez votre temps, réfléchissez, esquissez vos données et fonctionnalités sur une feuille de papier. Essayez de résoudre le problème manuellement d'abord, comme vous le feriez sans ordinateur. Si vous suivez cette approche, l'écriture de code devrait toujours être la dernière étape, car il est important de savoir quoi coder en premier.

Dans mon carnet, j'ai écrit mes fonctions, mes données et ce que je pensais être mes entrées. J'ai créé le canvas en premier, puis j'ai procédé à la création de la grille pour le Jeu de la Vie.

Honnêtement, c'est frustrant quand quelque chose ne fonctionne pas comme prévu, mais quand ça marche enfin, toute l'irritation en valait la peine. C'est bien de créer des choses, et encore mieux quand ces choses sont des jeux jouables.

La partie difficile de la création de ce jeu était de comprendre comment rendre la zone de la grille cliquable. Cela m'a vraiment stressée, mais j'ai finalement trouvé une solution : utiliser les coordonnées de décalage.

Voici à quoi ressemble le Jeu de la Vie :

![Image](https://cdn-media-1.freecodecamp.org/images/Mvdb7d2QjbiX1vySvmA00otSioq8-bllnKEJ)

Et voici mon code sur GitHub :

[**surbhioberoi/GameOfLife**](https://github.com/surbhioberoi/GameOfLife)  
[_GameOfLife - Conway's game of life_github.com](https://github.com/surbhioberoi/GameOfLife)

Les problèmes auxquels j'étais souvent confrontée lorsque je créais quelque chose de nouveau étaient la peur de ne pas pouvoir le faire. J'ai quelque peu surmonté cette peur en apprenant à créer des jeux.

De plus, je pensais que le rendu du back-end sur le front-end était la partie la plus difficile, et cela me faisait vraiment peur. Mais maintenant, je surmonte également ce défi.

J'ai trouvé que créer des jeux était la manière la plus amusante de pratiquer la programmation, car j'ai toujours aimé y jouer. Les jeux m'ont aidé à apprendre la programmation de manière divertissante, et je pense que c'est la meilleure façon d'apprendre quelque chose de nouveau.

HTML5 Canvas est vraiment génial, et une fois que vous en avez le coup, il est pratique à utiliser. C'est assez fascinant de voir comment vous pouvez créer tant de choses avec juste cet élément.

Maintenant, je ne sais pas si vous aimez jouer à des jeux. S'il y a quelque chose que vous aimez plus, essayez simplement de créer cela. Lorsque vous créez quelque chose que vous aimez vraiment, vous pouvez surmonter la peur de ne pas pouvoir le créer. Ce sera toujours difficile, mais vous aurez l'avantage de bénéfices agréables en cours de route, comme avoir un nouveau jeu auquel jouer ensuite. Et la meilleure partie — le sentiment d'accomplissement — sera toujours là pour vous, peu importe combien de temps le processus créatif prend.

_Publié à l'origine sur [surbhioberoi.com](http://surbhioberoi.com/how-creating-simple-canvas-games-helped-me/)._