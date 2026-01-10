---
title: 8 astuces npm que vous pouvez utiliser pour impressionner vos collègues
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-05-13T18:43:08.000Z'
originalURL: https://freecodecamp.org/news/8-npm-tricks-you-can-use-to-impress-your-colleagues-dbdae1ef5f9e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*r04YgvldF8rsv-sfttkvnA.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: 8 astuces npm que vous pouvez utiliser pour impressionner vos collègues
seo_desc: 'By Adir Amsalem

  You watch a colleague coding, there’s a shorthand or trick being applied, somehow
  you’re not familiar with it and your mind blows away. Happens to all of us all the
  time.

  In this short post we will unveil some very useful npm tricks. ...'
---

Par Adir Amsalem

Vous regardez un collègue coder, il utilise un raccourci ou une astuce, et pour une raison quelconque, vous ne la connaissez pas et votre esprit est soufflé. Cela nous arrive à tous tout le temps.

Dans ce court article, nous allons révéler quelques astuces npm très utiles. Il y en a beaucoup plus que ce que nous pouvons couvrir ici, alors j'ai choisi de me concentrer sur celles qui sont les plus pertinentes et utiles pour notre flux de travail quotidien en tant que développeurs.

### Raccourcis de base avant de commencer

Pour aligner tout le monde, surtout les nouveaux parmi nous, faisons un rapide aperçu des raccourcis de base et assurons-nous que personne ne manque rien de trivial.

#### Installer un package :

Normal : `npm install pkg`, Raccourci : `npm i pkg`.

#### Installer un package globalement :

Normal : `npm i --global pkg`, Raccourci : `npm i -g pkg`.

#### Installer un package et l'enregistrer comme une dépendance :

Normal : `npm i --save pkg`, Raccourci : `npm i -S pkg`.

#### Installer un package et l'enregistrer comme une devDependency :

Normal : `npm i --save-dev pkg`, Raccourci : `npm i -D pkg`.

Pour des raccourcis supplémentaires, lisez la [liste des raccourcis](https://docs.npmjs.com/misc/config#shorthands-and-other-cli-niceties) de npm.

Commençons maintenant avec les choses intéressantes.

#### 1. Initialiser un nouveau package

Nous connaissons tous `npm init`, c'est la première chose que nous faisons lors de la création d'un nouveau package.

![Image](https://cdn-media-1.freecodecamp.org/images/8atnoWYLUL7DJoL1Y6MPQKHGjtxLTMlWHE2Q)

Mais, toutes ces questions sont assez ennuyeuses et nous allons les modifier de toute façon, alors pourquoi ne pas simplement les éviter ?

`npm init -y` et `npm init -f` à la rescousse !

![Image](https://cdn-media-1.freecodecamp.org/images/PW1ehHF7TJY5445PiIzqKH17I1VEAAqbAffA)

#### 2. Exécuter des tests

Une autre commande que nous utilisons tous est `npm test`. La plupart d'entre nous l'utilisent tous les jours, plusieurs fois par jour.

![Image](https://cdn-media-1.freecodecamp.org/images/223EOKMiVqraBkOZaldXI3ZkrT20LPGkmyOj)

Que diriez-vous si je vous disais que vous pouvez faire la même chose avec ~40 % de caractères en moins ? Nous l'utilisons tellement, c'est une belle victoire.

Heureusement, il y a `npm t`, qui fait exactement cela !

![Image](https://cdn-media-1.freecodecamp.org/images/qBoBUCbrrSUwXqmgkobS8RSWo7DBikcSd8TN)

#### 3. Lister les scripts disponibles

Nous arrivons à un nouveau projet et nous nous demandons comment commencer. Nous nous posons généralement des questions comme : comment l'exécuter ? Quels scripts sont disponibles ?

Une façon de le découvrir est d'ouvrir le fichier package.json et de vérifier la section `scripts`.

![Image](https://cdn-media-1.freecodecamp.org/images/yeCx6ROfgZnv7DfJ-NQnYDvEsUPLODGWbHQ2)

Nous pouvons bien sûr faire mieux, alors nous exécutons simplement `npm run` et obtenons une liste de tous les scripts disponibles.

![Image](https://cdn-media-1.freecodecamp.org/images/AW6DbH7UEeZu5bDIhBTMpWDZtzNsVZqEghGj)

Une option supplémentaire est d'installer `ntl` (`npm i -g ntl`), puis d'exécuter `ntl` dans le dossier du projet. Cela permet également d'exécuter les scripts, ce qui le rend très pratique.

![Image](https://cdn-media-1.freecodecamp.org/images/pxg3xuyZ-EfD4j3yPpgYLH77haLQ7Dya-X4a)

#### 4. Lister les packages installés

Similaire aux scripts disponibles, parfois nous nous demandons quelles dépendances nous avons dans notre projet.

Nous pouvons une fois de plus ouvrir le fichier package.json et vérifier, mais nous savons déjà que nous pouvons faire mieux.

Voici `npm ls --depth 0`.

![Image](https://cdn-media-1.freecodecamp.org/images/uplcv8ZLtwCPnCFTDIF4JmiTDAqys-d0GgRw)

Pour lister les packages installés globalement, nous pouvons exécuter la même commande avec le drapeau `-g`, `npm ls -g --depth 0`.

![Image](https://cdn-media-1.freecodecamp.org/images/32Rx5M4pyEtYxh6qy-EmoVUIAg0Yua2coV5W)

#### 5. Exécuter des exécutables installés localement

Nous avons installé un package dans notre projet, il vient avec un exécutable, mais il ne fonctionne que lorsque nous l'exécutons via un script npm. Vous vous êtes demandé pourquoi, ou comment le surmonter ?

Tout d'abord, comprenons pourquoi — lorsque nous exécutons des commandes dans notre terminal, ce qui se passe réellement est qu'il recherche un exécutable avec le même nom dans tous les chemins qui sont listés dans notre variable d'environnement `PATH`. C'est ainsi qu'ils sont magiquement disponibles de n'importe où. Les packages installés localement enregistrent leurs exécutables localement, donc ils ne sont pas listés dans notre `PATH` et ne seront pas trouvés.

Comment cela fonctionne-t-il lorsque nous exécutons ces exécutables via un script npm, demandez-vous ? Bonne question ! C'est parce que lorsque nous exécutons de cette manière, npm fait un petit tour de magie et ajoute un dossier supplémentaire à notre `PATH`, `<project-directory>/node_modules/.bin`.

Vous pouvez le voir en exécutant `npm run env | grep "$PATH"`. Vous pouvez également exécuter simplement `npm run env` pour voir toutes les variables d'environnement disponibles, npm ajoute quelques autres choses intéressantes.

`node_modules/.bin`, si vous vous le demandiez, est exactement là où les packages installés localement placent leurs exécutables.

Exécutons `./node_modules/.bin/mocha` dans le répertoire de notre projet pour le voir en action.

![Image](https://cdn-media-1.freecodecamp.org/images/qwmAkkWrBqyDvqeEH0vy2-AIFRFf1YZ7rTSF)

Simple, n'est-ce pas ? Il suffit d'exécuter `./node_modules/.bin/<commande>` chaque fois que vous voulez exécuter un exécutable installé localement.

#### 6. Trouver votre package sur internet

Vous êtes peut-être tombé sur l'entrée `repository` dans le fichier package.json et vous êtes demandé : « À quoi cela sert-il ? ».

Pour y répondre, exécutez simplement `npm repo` et regardez-le s'ouvrir dans votre navigateur.

La même chose s'applique, d'ailleurs, pour la commande `npm home` et l'entrée `homepage`.

Si vous voulez ouvrir la page de votre package sur [npmjs.com](https://www.npmjs.com/), il y a aussi un raccourci pour cela, `npm docs`.

#### 7. Exécuter des scripts avant et après d'autres scripts

Vous êtes probablement familier avec des scripts tels que `pretest`, qui vous permet de définir du code qui s'exécutera avant le script `test`.

Ce qui pourrait vous surprendre, c'est que vous pouvez avoir des scripts pré et post pour chaque script, y compris vos propres scripts personnalisés !

![Image](https://cdn-media-1.freecodecamp.org/images/ei1rVwDYYd1qlgXsAlSK95Yb0BmYzCka9XMt)

C'est très utile pour les projets dans lesquels vous utilisez npm comme outil de build et avez de nombreux scripts à orchestrer.

#### 8. Incrémenter la version du package

Vous avez un package, vous utilisez [semver](http://semver.org/) pour la version, et vous devez incrémenter la version avant une nouvelle publication.

Une façon de faire cela est d'ouvrir le fichier package.json et de changer la version manuellement, mais nous ne sommes pas là pour cela.

Une manière plus facile est d'exécuter `npm version` avec `major`, `minor` ou `patch`.

![Image](https://cdn-media-1.freecodecamp.org/images/OS51ylDy5REYLrs0nhP6l7oKb-1DOKUGuyAu)

C'est tout pour maintenant.

J'espère que vous avez appris quelque chose de nouveau et trouvé au moins une de ces astuces utile pour votre flux de travail quotidien, et idéalement, vous connaissez aussi mieux npm maintenant et avez de nouvelles idées sur la façon dont vous pouvez mieux l'utiliser dans votre travail.

Impressionner vos collègues est génial, mais apprendre constamment de nouvelles choses et être plus professionnel est encore mieux !

Si vous connaissez d'autres astuces utiles, n'hésitez pas à les partager dans les commentaires !