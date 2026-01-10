---
title: Ce que la musique peut nous apprendre sur la façon dont nous partageons du
  code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-19T19:04:36.000Z'
originalURL: https://freecodecamp.org/news/what-music-can-teach-us-about-the-way-we-share-code-a69c30ebded8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*viBEEx_KTOQfLsV63PJM9w.png
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: Ce que la musique peut nous apprendre sur la façon dont nous partageons
  du code
seo_desc: 'By Jonathan Saring

  Not that long ago, many of us were carrying a suspicious-looking suitcase in the
  back of our cars, or had one hidden under our beds. Some of us had Ikea-made towers
  with multiple storage spaces standing proud in our living rooms. I...'
---

Par Jonathan Saring

Il n'y a pas si longtemps, beaucoup d'entre nous transportions une valise suspecte à l'arrière de notre voiture, ou en avions une cachée sous notre lit. Certains d'entre nous avions des tours fabriquées par Ikea avec plusieurs espaces de stockage debout fièrement dans nos salons. Dans les deux cas, cela était le résultat de notre impressionnante collection de CD-Roms de musique. Aujourd'hui, il y a des chances qu'ils soient stockés de manière nostalgique dans notre garage.

Après un règne court, les CD-Roms de musique ont été remplacés par iTunes et YouTube, avec des lecteurs MP3 entre les deux. Cette révolution s'est produite principalement à cause de 5 inconvénients majeurs que les CD avaient dès le premier jour :

1. Ils étaient encombrants à utiliser, à transporter et à manipuler.
2. Ils demandaient trop d'efforts pour être achetés/créés.
3. Ils étaient très difficiles à changer et à modifier. Personne ne voulait vraiment graver un nouveau CD chaque fois qu'une nouvelle chanson de Bieber sortait (ne me jugez pas).
4. Ils nous forçaient à transporter un tas de chansons que nous n'écoutions pas et à zapper à travers elles juste pour écouter une seule chanson que nous voulions vraiment écouter.
5. Qui se souvenait de quelles chansons étaient sur quel CD ? 90 % de mes CD gravés contenaient de toute façon les mêmes 10 chansons.

Étonnamment, cela n'est pas si différent de la façon dont nous partageons le code aujourd'hui, entre les projets et entre les personnes. Voyons comment.

### En quoi cela ressemble-t-il au partage de code ?

![Image](https://cdn-media-1.freecodecamp.org/images/u740J5qArBLMtR08Bqlo-0Sl6m8E-xwV4WfQ)
_« J'aime généralement juste écouter mon sabre laser siffler d'avant en arrière... »_

La modularité a toujours été le saint graal du développement logiciel, et la clé d'une meilleure réutilisabilité, maintenabilité et testabilité.

Chaque jour, de plus en plus des applications que nous construisons sont conçues avec une plus grande modularité grâce à des composants de code plus petits. Les fonctionnalités réutilisables, les composants UI et Web (tels que React, Vue et Angular), les modules Node.js, les API GraphQL et même les fonctions serverless sont nos blocs de construction.

Maintenant, soyons honnêtes — qui sait exactement quels composants réutilisables ont été écrits dans leur base de code, les organise et les partage entre leurs projets à grande échelle ? Je sais que je ne le faisais pas. Ensuite, j'ai commencé à me demander pourquoi pas.

Permettez-moi de vous montrer. Voici une [application React de films](https://github.com/teambit/movie-app) hébergée sur GitHub. Comme vous pouvez le voir, elle contient un total de 49 fichiers et 14 répertoires. L'un de ces répertoires est le sous-répertoire `components`. À l'intérieur de ce sous-répertoire, il y a 8 composants React réutilisables (tels que `hero` et `navigation`).

```
├── src
```

```
│   ├── App.js
```

```
│   ├── App.scss
```

```
│   ├── App.test.js
```

```
│   ├── components
```

```
│   │   ├── hero
```

```
│   │   ├── hero-button
```

```
│   │   ├── item
```

```
│   │   ├── list-toggle
```

```
│   │   ├── logo
```

```
│   │   ├── navigation
```

```
│   │   ├── title-list
```

```
│   │   └── user-profile
```

```
│   ├── favicon.ico
```

```
│   ├── global.css
```

```
│   └── index.js
```

```
└── yarn.lock
```

Disons que j'ai une autre application React, et que je veux utiliser mon composant `hero` dans cette autre application également, et aussi le rendre découvrable pour mon équipe afin qu'ils l'utilisent dans leurs projets et le modifient facilement pour répondre à leurs besoins.

Copier-coller du code est une [très mauvaise idée](https://stackoverflow.com/questions/4226284/how-to-convince-a-colleague-that-code-duplication-is-bad). Cela peut sembler la solution rapide, mais ce n'est vraiment pas le cas. Ne le faites pas.

À ce jour, j'ai vraiment trois options :

1. **Publier neuf packages** : Créer huit nouveaux dépôts, du code boilerplate, et publier neuf packages et modifier le code source des deux projets pour les **requérir**. Lorsque je voudrai modifier un composant, je devrai travailler très dur pour apporter des modifications depuis différents dépôts. Imaginez maintenant en avoir 500.
2. **Je peux utiliser [Lerna](https://github.com/lerna/lerna)** pour garder plusieurs packages dans un seul dépôt, mais cela ne fonctionne que si je veux vraiment passer à un monorepo. Même alors, je devrai restructurer mon projet, configurer chaque package séparément, et définir leurs arbres de dépendances, et chaque changement devra encore passer par le dépôt original.
3. **Bibliothèque partagée** : Créer un nouveau dépôt, regrouper les composants ensemble, créer les configurations nécessaires pour un tel projet, le publier en tant que nouvelle bibliothèque, et modifier le code source des deux projets. Chaque application utilisant cette bibliothèque ajoutera du code redondant, du poids et de la complexité. Chaque modification nécessitera de republier toute la bibliothèque et de passer par le propriétaire.

Le problème, c'est que les packages sont **formidables** pour les grands projets. Pour les composants et modules plus petits, ces solutions partagent certains des mêmes problèmes que les CD-Roms de musique : un sérieux surcoût, les changements sont difficiles, et la découvrabilité est insuffisante.

D'une certaine manière, la configuration de 500 dépôts et packages pour partager de petits composants me rappelle l'utilisation d'un lecteur de mini-disques (pas mes 100 $ les mieux dépensés) : vous ne pouvez pas résoudre ce problème en l'optimisant. Vous devez innover.

### Donc... iTunes pour le code partagé ?

Évidemment, comparer les bibliothèques partagées aux CD-Roms n'est pas très techniquement précis. La complexité du partage de fonctionnalités entre des environnements et des contextes compliqués est différente de celle de l'écoute de Lady Gaga.

Pourtant, partager du code commun entre les projets ne devrait vraiment pas être si difficile. Ce que nous pouvons vraiment apprendre de la façon dont nous partageons et consommons de la musique aujourd'hui, c'est qu'un partage efficace nécessite une **meilleure** **expérience** : réduire les surcoûts, augmenter la découvrabilité et passer du statique au dynamique.

### Nous avons donc décidé de le construire

Un jour, début 2017, nous avions exactement ce rêve. L'une des meilleures choses à propos de l'open source, c'est qu'avoir une idée est une raison parfaitement valable pour la construire.

Nous avons décidé d'aller de l'avant et de construire [Bit](https://bitsrc.io) — un [projet open source](https://github.com/teambit/bit) conçu pour faire pour le partage de code ce qu'iTunes a fait pour le partage de musique — le rendre simple, dynamique et facilement accessible à tous. L'idée de [Bit](https://bitsrc.io) est simple : Éliminer le surcoût du partage de code.

#### Comment cela fonctionne

![Image](https://cdn-media-1.freecodecamp.org/images/U9MYoGOV4yiSkk3XYYreYkXfWnM9qUEv6MzJ)

Il a été construit pour fournir l'expérience la plus rapide possible pour le « copier-coller géré » et être 100 % compatible avec Git et NPM.

La clé réside dans la capacité de Bit à séparer la représentation du code partagé du système de fichiers de votre projet, et sa capacité à suivre le code partagé à travers les dépôts et les projets, qu'il soit installé ou réellement sourcé dans ces projets.

Il élimine le surcoût du partage de code en éliminant le besoin de diviser vos dépôts ou d'avoir à restructurer votre projet et à créer plusieurs packages boilerplate à l'intérieur.

Au lieu de cela, vous pouvez simplement pointer Bit vers n'importe quelle partie de votre dépôt que vous souhaitez partager, laisser Bit l'isoler automatiquement (y compris les dépendances), et le partager vers un emplacement partagé appelé Scope à partir duquel il peut être installé avec NPM.

Puisque Bit est capable de suivre le code source réel entre les projets, vous pouvez également l'utiliser pour importer le code lui-même dans n'importe quel dépôt, le modifier et laisser Bit synchroniser les changements à travers vos projets pour vous.

Lors du partage, vous pouvez même `ejecter` le code pour qu'il redevienne une dépendance de package pour votre projet.

En conséquence, il n'y a pratiquement aucun surcoût pour partager du code et le rendre disponible avec NPM, la découvrabilité est augmentée et la maintenance devient beaucoup plus simple. Les Scopes aident même à [construire](https://docs.bitsrc.io/docs/building-components.html) et tester votre code afin que vous n'ayez pas à configurer ces environnements pour chaque package.

Voici à quoi ressemble le [flux de travail de Bit](https://docs.bitsrc.io/) :

1. Installez Bit et initialisez-le pour votre projet.
2. Choisissez quels composants de code suivre à partir de votre projet et quels [environnements](https://docs.bitsrc.io/) ajouter pour les processus de construction et de test.
3. Partagez-les vers un Scope distant où ils sont hébergés, organisés et mis à disposition pour installation en utilisant votre gestionnaire de packages préféré.
4. Importez facilement leur code dans n'importe quel dépôt, modifiez-le selon les besoins et mettez à jour vos changements à travers votre base de code.

Regardons un exemple.

#### Retour à l'application React movie-app

Revenons à l'[application React movie-app](https://github.com/teambit/movie-app).

[Ajouter Bit](https://docs.bitsrc.io/) au projet m'a permis de suivre et d'isoler les composants réutilisables à l'intérieur, sans configurer de nouveaux dépôts ou modifier le code de mon projet. Ensuite, je les ai partagés vers cette [collection](https://bitsrc.io/bit/movie-app).

Le partage a pris très peu de temps et mon projet n'a pas été modifié du tout. Aucun nouveau fichier `package.json` n'a été créé et je n'ai pas eu à configurer plusieurs environnements ou à lutter contre mon arbre de dépendances.

![Image](https://cdn-media-1.freecodecamp.org/images/gAxTcRwrApKKUG1uju8B-q5IjsYr81O9Y0p8)
_Composants React avec Bit_

Comme vous pouvez le voir, chaque composant est maintenant disponible pour toute mon équipe pour être installé avec NPM ou pour être importé dans leurs propres projets pour des modifications ultérieures.

Ils peuvent le rechercher et voir des informations utiles — du rendu en direct aux résultats de construction et de test, aux docs et exemples auto-analysés — afin qu'ils puissent juger de son utilité.

Toute notre équipe peut maintenant organiser et partager nos composants de code communs sans avoir à travailler dur ou à réinventer la roue chaque jour.

Après l'avoir utilisé pendant plus de 10 mois, et après qu'il soit maintenant utilisé par des équipes et des communautés supplémentaires, je vous invite à rejoindre et à l'utiliser pour vos projets.

Vous pouvez voir une démonstration vidéo de ce projet [ici](https://www.youtube.com/watch?v=vm_oOghNEYs).

### Retour vers le futur

Jusqu'à il y a quelques années, nous devions graver un nouveau projet pour chaque chanson que nous voulions écouter. Nous devions stocker et maintenir plusieurs CD statiques et traîner un tas de choses juste pour écouter une seule chanson. Nous dupliquions des chansons entre les CD et avions du mal à découvrir les chansons que nous voulions vraiment.

iTunes nous a fourni l'expérience dynamique qui nous a aidés à composer et à partager des playlists, à trouver facilement les chansons que nous voulions et à mettre rapidement à jour nos playlists. Lorsque je suis à une fête, je peux facilement jouer ma playlist estivale à tempo soutenu, ou tout aussi facilement jouer mes chansons romantiques à mon chat pour l'endormir.

Nous pouvons apprendre énormément de la façon dont la musique est passée des CD-Roms aux playlists partagées. [Bit](https://bitsrc.io) vise à rendre le partage et la réutilisation de code simples et accessibles à tous, tout comme iTunes l'a fait pour la musique partagée. C'est encore un travail en cours, et à ce titre, il a encore beaucoup de place pour grandir et évoluer. Vous êtes les bienvenus pour [l'essayer](https://bitsrc.io), suggérer des [idées](https://gitter.im/bit-src/Bit) et des [retours](https://github.com/teambit/bit/issues), et nous aider à faire ce bond en avant.

> « Le secret pour construire efficacement des choses 'grandes' est généralement d'éviter de les construire en premier lieu. Au lieu de cela, composez votre grande chose à partir de morceaux plus petits et plus ciblés... »

> - A. Osmani