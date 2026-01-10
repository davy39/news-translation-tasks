---
title: Comment utiliser une file d'attente de tâches concurrentes dans vos Redux-Sagas
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-18T21:33:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-a-concurrent-task-queue-in-your-redux-sagas-39e598c4fcae
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8HhqBBy6h6Ag7wO_mqCMug.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Redux
  slug: redux
- name: technology
  slug: technology
seo_title: Comment utiliser une file d'attente de tâches concurrentes dans vos Redux-Sagas
seo_desc: 'By Shy Alter

  In this guide, you will learn what a concurrent task queue is, some of the best
  use cases, and how to write one.

  The queue is one of the most used data structures. You probably use it every day
  when you shop for groceries (even online) o...'
---

Par Shy Alter

Dans ce guide, vous apprendrez ce qu'est une file d'attente de tâches concurrentes, certains des meilleurs cas d'utilisation, et comment en écrire une.

La file d'attente est l'une des structures de données les plus utilisées. Vous l'utilisez probablement tous les jours lorsque vous faites vos courses (même en ligne) ou lorsque vous envoyez un message texte à vos amis.

La file d'attente de tâches concurrentes est un modèle très puissant qui peut vraiment vous aider à gérer les tâches au fil du temps ou à améliorer vos performances.

**TL;DR en bas**

### Commençons par les bases

#### Qu'est-ce qu'une file d'attente ? ???

Une file d'attente est une structure linéaire dans laquelle les valeurs sont ajoutées à une extrémité et retirées de l'autre. Cette discipline donne lieu à un comportement premier entré/premier sorti (FIFO) qui est la caractéristique définissante des files d'attente. Les deux opérations fondamentales de la file d'attente sont enqueue (ajouter à l'arrière) et dequeue (retirer de l'avant) ([source](https://stanford.edu/~stepp/cppdoc/Queue-class.html)).

![Image](https://cdn-media-1.freecodecamp.org/images/1*Li-9xbwJWffXSSERtTX86g.png)
_Représentation d'une [wikipedia](https://en.wikipedia.org/wiki/FIFO_(computing_and_electronics)" rel="noopener" target="_blank" title="FIFO (computing and electronics)">FIFO</a> (first in, first out) queue (<a href="https://en.wikipedia.org/wiki/Queue_(abstract_data_type)" rel="noopener" target="_blank" title="))_

#### Ok, quand devons-nous l'utiliser ?

Utilisez une file d'attente lorsque vous devez maintenir l'ordre des événements et traiter la valeur selon cet ordre.

#### Super, vous m'avez convaincu ! Mais pourquoi ai-je besoin de la concurrency ?

Comme je l'ai mentionné ci-dessus, une file d'attente est capable de traiter une valeur à la fois. Mais parfois ce n'est pas assez rapide.

**Considérez le cas suivant** ?:

Vous êtes dans votre épicerie préférée et venez d'arriver à la caisse, mais malheureusement il y a beaucoup de monde qui attend. Pour accélérer le processus, le magasin a ouvert plusieurs autres caisses et chaque caissier supplémentaire a sa propre file d'attente. Vous devez donc simplement en choisir une. Si l'un des caissiers a un problème technique ou s'il est simplement lent, cette file d'attente sera retardée même si les autres caisses sont libres.

![Image](https://cdn-media-1.freecodecamp.org/images/1*R4Dvy6CM9tbCiALKvVrshA.png)
_([@andreagiuliaderba](http://twitter.com/andreagiuliaderba" rel="noopener" target="_blank" title="Twitter profile for @andreagiuliaderba))_

La file d'attente de tâches concurrentes à la rescousse ! ?

Nous allons utiliser une seule file d'attente pour nos besoins. De cette manière, chaque fois qu'une caisse devient libre, nous allons retirer une personne de la file d'attente et l'envoyer à la caisse libre.

![Image](https://cdn-media-1.freecodecamp.org/images/1*nidy8yr16nMUBA153rhwEQ.png)
_single concurrent queue ([@andreagiuliaderba](http://twitter.com/andreagiuliaderba" rel="noopener" target="_blank" title="Twitter profile for @andreagiuliaderba))_

**Hourra !** ?

### Examinons maintenant un cas d'utilisation

La semaine dernière, je travaillais sur une extension Google Chrome qui détecte et télécharge les flux HLS [streams](https://en.m.wikipedia.org/wiki/HTTP_Live_Streaming) (HTTP Live stream).

Les flux HLS sont combinés à partir de plusieurs morceaux qui sont récupérés un par un et diffusés dans votre navigateur sous forme de vidéo unique. Vous pouvez avoir des milliers de fichiers par flux, et vous devez tous les télécharger.

Nous allons utiliser notre **file d'attente** bien-aimée pour accélérer le processus et nous assurer qu'une récupération lente ne va pas bloquer les autres.

### **TL;DR : voici le code**

Maintenant, examinons-le pièce par pièce.

#### 1. Le gestionnaire

Ce gestionnaire simple obtient l'URI à partir de la charge utile et ensuite :

* récupère le morceau
* le transforme en blob
* émet un événement redux **chunk-ready**
* obtient le nombre actuel de morceaux prêts
* vérifie si c'est **"tout fait"**

#### 2. Créer la file d'attente

En utilisant le gestionnaire, nous créons une nouvelle file d'attente avec **5 travailleurs.** Nous obtenons la tâche **watcher** et un **queue channel.** Ensuite, nous allons exécuter (fork) la tâche watcher pour qu'elle commence à écouter les tâches.

#### 3. Pousser les tâches

Nous mappons tous les segments à une tâche de mise (dans le **queue channel** que nous avons obtenu), puis nous lançons toutes les tâches ensemble.

#### 4. Attendre que tous les morceaux soient prêts ou que l'action soit annulée

Maintenant, nous attendons que la première action soit appelée **all-done** ou soit **cancelled.** Après cela, nous pouvons annuler le watcher et agir selon l'action qui a été reçue.

### Et c'est tout !

Si vous voulez le voir en direct, visitez [https://github.com/puemos/hls-downloader-chrome-extension](https://github.com/puemos/hls-downloader-chrome-extension), et téléchargez l'extension Chrome.

J'espère que vous avez appris quelque chose de nouveau ! Si vous avez des questions, veuillez commenter ci-dessous pour que tout le monde puisse en bénéficier.