---
title: Comment contribuer à l'open source m'a rendu meilleur développeur — et comment
  vous pouvez le faire aussi
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-17T02:19:15.000Z'
originalURL: https://freecodecamp.org/news/how-contributing-to-open-source-made-me-a-better-developer-and-how-you-can-do-the-same-89929cd9f497
coverImage: https://cdn-media-1.freecodecamp.org/images/1*fu2BEgeHB_-QnlbIhJZfJg.jpeg
tags:
- name: GitHub
  slug: github
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Comment contribuer à l'open source m'a rendu meilleur développeur — et
  comment vous pouvez le faire aussi
seo_desc: 'By Luciano Strika

  So you’ve been learning how to code. You are studying Algorithms and Data Structures.
  You are getting up to date on the latest Frameworks and their quirks. You can already
  smell some code smells, or even design solutions to real pro...'
---

Par Luciano Strika

Donc, vous apprenez à coder. Vous étudiez les algorithmes et les structures de données. Vous vous tenez au courant des derniers frameworks et de leurs particularités. Vous pouvez déjà détecter certaines mauvaises pratiques de code, voire concevoir des solutions à des problèmes réels.

Mais vous n'avez pas encore travaillé dans l'industrie du logiciel. Ou vous êtes à votre premier emploi et vous voyez à quel point tout le monde est génial et plein d'expérience. Pourtant, vous avez l'impression d'être le plus novice des novices. Le syndrome de l'imposteur est une réalité, et nous y avons tous été confrontés.

Il existe un moyen d'acquérir de l'expérience en travaillant sur de vrais projets, en maîtrisant des compétences qu'un livre ne peut pas vous enseigner.

Voici quelques-unes des choses que nous pouvons apprendre grâce à l'Open Source :

* Lire le code des autres
* Comprendre des systèmes complexes, pièce par pièce
* Utiliser correctement les logiciels de versioning (comme git), avec des messages de commit clairs, des commits atomiques, et toutes ces bonnes pratiques.

Si vous avez lu le titre de cet article, vous savez où cela mène. En tant que lecteur de Medium, vous avez souvent lu que contribuer à l'Open Source est génial. Cela vous apprendra beaucoup, et pourrait même attirer l'attention d'un recruteur d'une grande entreprise. Je ne peux pas garantir tout cela, mais je peux certainement attester des deux premiers points.

#### Mon histoire

Laissez-moi vous raconter une histoire. Lorsque j'ai commencé mon premier emploi, les dépôts m'ont submergé. Ils contenaient des milliers de lignes de code, des conventions ou leur absence, et des styles en conflit. J'avais seulement travaillé sur de petits projets universitaires. Ces projets faisaient au maximum 10 000 lignes, écrites par des personnes que je connaissais, sur une période d'un mois.

Je n'avais jamais vu ce qu'un dépôt pouvait devenir (ou prospérer, s'il est bien maintenu, mais c'est l'industrie dont nous parlons ici) après quelques années de chaos et de `git reset --hard`.

Apprendre à naviguer dans cette base de code était une compétence en soi, que j'ai acquise après des mois de pratique. Mais ensuite, lorsque j'ai commencé à parcourir GitHub, à la recherche d'un endroit où contribuer (ou pousser), j'ai commencé à voir comment d'autres dépôts étaient organisés.

Maintenant, je ne suis en aucun cas un expert. Mon expérience sur GitHub jusqu'à présent a surtout été celle de ce que, dans certains cercles, on appellerait un lurker. Je lis le code, je vois ce qu'il fait, je lis les problèmes, et je pense « bon sang, j'aimerais avoir une idée de par où commencer ».

Mais ensuite, quelque chose d'awesome s'est produit : un gars sur Reddit a posté un petit projet sur lequel il travaillait. Pas tant de lignes de code, principalement en Python (mon langage préféré), et maintenu principalement par lui-même, avec l'aide de quelques autres personnes. J'ai vu ma chance et je l'ai saisie. J'ai étudié le code, j'ai vu que certains des scripts Python fonctionnaient parfaitement, mais qu'ils étaient un peu laids : mauvaises pratiques, répétitions, des trucs vraiment basiques que le genre de personne qui fait vraiment avancer les choses ne prend peut-être pas le temps de réfléchir en codant le premier jet, mais qui vous reviennent en pleine figure par la suite. Alors je me suis lancé dans le refactoring.

(En passant, ce projet était [cheat.sh](http://cheat.sh), une feuille de triche interactive sur le web pour les développeurs. Voici le projet [GitHub](https://github.com/chubin/cheat.sh). C'est un projet génial auquel contribuer, et je vous recommande de le vérifier.)

#### Un tutoriel

Avec cet article, j'ai créé un tutoriel pour que vous puissiez vous rafraîchir la mémoire sur git.
Je vais supposer que nous utilisons un dépôt GitHub, car c'est ce que la plupart d'entre vous pourriez utiliser dans vos emplois. Pour ce tutoriel, j'ai créé un [**petit dépôt d'exemple**](https://github.com/StrikingLoo/contributions-worktable) pour que vous puissiez suivre. Les instructions sont également présentes dans le fichier README.md.

Voici ce que vous devrez faire dans cette petite tâche :

* Visitez le lien du dépôt et cliquez sur le bouton **fork**. Cela créera une copie de l'historique du projet jusqu'à ce point sous votre propre profil.
* Créez un répertoire local sur votre ordinateur
* Ajoutez à la fois mon projet et celui que vous avez créé en tant que dépôts distants. Pour ce faire, ouvrez votre terminal dans le répertoire que vous avez créé et utilisez la commande suivante :

```
 git remote add *nom* *lien* 
```

Il est coutumier que le nom du lien de mon projet soit 'upstream', et le vôtre 'origin'.

* **Pull** mon projet :

```
git pull origin master
```

* Ajoutez votre nom à la liste des contributeurs dans le README.md en utilisant votre éditeur de texte préféré (j'aime Vim, par exemple). N'oubliez pas d'enregistrer vos modifications !
* **Commit** les changements :

```
git add . && git commit -m 'Votre message génial pour moi ici'
```

* Allez sur votre compte Github, visitez votre copie du projet et cliquez sur 'pull request', en choisissant de fusionner votre branche master avec la mienne.

Je promets d'accepter les demandes dès que possible, probablement le même jour... Et c'est tout ! Pas différent de ce que cela aurait été si vous faisiez une grande contribution !

#### **Appel à l'action**

Maintenant, vous n'avez plus d'excuse, trouvez un projet que vous aimez ou qui vous tient à cœur et ajoutez quelques lignes ! Peu importe si vos changements sont petits, tant que vous aidez et apprenez à travers eux. Ma première contribution était de corriger une faute de frappe dans un README.

J'essaie de nouvelles choses cette année, et écrire sur Medium était sur ma liste depuis un moment.

C'était mon tout premier article, et je serais ravi si vous me donniez des retours ou des opinions sur ce que vous avez lu.

Étant nouveau dans le logiciel Open Source, veuillez me dire s'il y a quelque chose d'important que vous pensez que j'ai manqué. Enfin, si vous avez déjà fait des contributions Open Source, j'aimerais entendre quelques histoires et opinions. Quels sont les meilleurs projets auxquels contribuer, et ceux que vous avez le plus/le moins aimés ? Ce serait bien si nous pouvions compiler une liste pour les débutants.

Merci d'avoir lu jusqu'ici, à bientôt !

_Suivez-moi pour plus d'articles sur la programmation et la Data Science, et découvrez mes derniers articles (probablement meilleurs).