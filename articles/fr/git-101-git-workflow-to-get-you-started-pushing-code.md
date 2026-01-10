---
title: 'Git 101 : Un flux de travail Git pour commencer à pousser du code'
subtitle: ''
author: Shruti Kapoor
co_authors: []
series: null
date: '2019-07-29T15:59:00.000Z'
originalURL: https://freecodecamp.org/news/git-101-git-workflow-to-get-you-started-pushing-code
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/photo-1556075798-4825dfaaf498.jpeg
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: Front-end Development
  slug: front-end-development
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: learning to code
  slug: learning-to-code
- name: Web Development
  slug: web-development
seo_title: 'Git 101 : Un flux de travail Git pour commencer à pousser du code'
seo_desc: "I'm going to explain Git the way I wish someone had explained to me back\
  \ when I was first learning. \nI'll show how you can get started with just a few\
  \ commands, and the concepts at work behind those concepts.\nBasic concepts\nYour\
  \ local code\nThis is th..."
---

Je vais expliquer Git de la manière dont j'aurais aimé que quelqu'un me l'explique lorsque j'ai commencé à apprendre. 

Je vais montrer comment vous pouvez commencer avec juste quelques commandes, et les concepts derrière ces commandes.

## Concepts de base

#### Votre code local

Il s'agit du travail que vous effectuez sur votre ordinateur. Toute édition, format, fonctionnalité ou travail de développement que vous avez sur votre ordinateur est votre code local.

#### Site en staging

Une fois que vous êtes satisfait des modifications ou de la quantité de travail effectuée, vous pouvez le marquer comme prêt pour le staging. Cela signifie que vous déclarez que ces lignes de code sont prêtes à être validées (commit).

#### Le serveur

Une fois que vous êtes prêt avec les fichiers que vous avez mis en staging, vous pouvez les envoyer sur le serveur qui stocke tout votre code afin que d'autres personnes puissent également l'utiliser. Maintenant, vos fichiers peuvent être consultés par d'autres personnes et travaillés.

### L'objectif final

L'idée derrière Git est que votre code sur le serveur distant doit être synchronisé avec le code sur votre machine. Lorsque vous travaillez avec d'autres personnes, leur code doit être synchronisé avec votre code. Ainsi, si vos collègues ont poussé du nouveau code, vous devriez pouvoir mettre à jour facilement votre code pour refléter leurs modifications.

L'objectif final est que tout sur le serveur soit identique à tout sur votre machine locale. Vous devez envoyer les fichiers sur le serveur dès que possible afin que, lorsque d'autres personnes consultent votre code, elles aient la version la plus à jour.

### Flux de travail

Supposons que vous avez un dossier sur votre ordinateur où se trouve votre code. Vous souhaitez le mettre sur GitHub pour pouvoir le versionner.

Voici comment vous pouvez le faire.

### 1. Obtenir un dépôt.

Il existe deux façons d'obtenir un dépôt : soit vous pouvez en créer un vous-même, soit vous pouvez travailler à partir du dépôt de quelqu'un d'autre et contribuer à son dépôt. Le choix dépend du projet sur lequel vous travaillez. Si vous travaillez sur un projet seul, vous êtes plus susceptible de créer un dépôt à partir de zéro et de commencer à écrire du code. Lorsque vous travaillez sur du code open source ou en équipe, vous obtiendrez probablement un dépôt qui existe déjà. Parlons de la façon de faire les deux.

#### Créer un dépôt

Tout d'abord, vous devrez créer un compte [GitHub](https://github.com/) si vous n'en avez pas déjà un. Cliquez sur l'onglet Dépôts et cliquez sur "Nouveau".

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-77.png)
_Bouton Nouveau pour créer un nouveau dépôt_

Suivez les instructions pour créer votre nouveau dépôt. Supposons que nous nommions ce dépôt `test-repo`. Une fois que vous avez créé ce dépôt, GitHub donne des instructions sur la façon de le configurer sur votre ordinateur local.

Utilisez les instructions pour créer un nouveau dépôt sur la ligne de commande :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-78.png)

#### Cloner un dépôt

`git clone <repository>`

Supposons que vous souhaitez obtenir le code sur lequel je travaille afin de pouvoir travailler dessus sur votre ordinateur. Vous devrez trouver mon compte GitHub et cloner un dépôt qui vous intéresse. Aujourd'hui, nous allons travailler sur ce dépôt :

```
git clone git@github.com:shrutikapoor08/devjoke.git
```



![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-85.png)

###   
2. Créer une branche

Créer une branche aide à garder le travail en cours séparé d'un morceau de code fonctionnel. Cela vous aide également à modulariser votre code et à garder les fonctionnalités séparées pendant que vous travaillez encore dessus. Créons une nouvelle branche `joke-branch` en utilisant :

 `git checkout -b joke-branch`

Vous pouvez pousser cette branche vers le serveur (`origin`) en utilisant :

`git push origin joke-branch`

Maintenant, supposons que vous et moi sommes coéquipiers. Nous travaillons sur un projet ensemble. Parcourons le flux de travail.

### 3. Modifier le code

Une fois que vous comprenez ce que fait le code, vous êtes prêt à faire des modifications. Si vous travaillez sur le dépôt de quelqu'un d'autre, il est bon de faire un `fork` de son dépôt. "Forker" consiste à faire une copie d'un dépôt. C'est comme passer un dépôt dans une photocopieuse et obtenir votre propre copie. Vous pouvez faire ce que vous voulez avec votre copie, apporter des modifications, éditer des fichiers, supprimer des fichiers ou ajouter de nouveaux fichiers. Si vous le souhaitez, vous pouvez envoyer vos mises à jour au dépôt original et demander que votre code soit fusionné dans le dépôt original.

Nous allons modifier ce code en créant un fork de ce dépôt. Pour forker un dépôt, cliquez sur le bouton Fork en haut du dépôt.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-86.png)

Maintenant, si vous allez sur votre profil GitHub, vous pouvez voir votre nouveau dépôt fork dans votre profil. Woot Woot !

Maintenant, nous allons faire quelques modifications. Ouvrez le fichier `README.md`. Dans ce fichier, nous allons ajouter une DevJoke ! Pensez à une blague de programmation intelligente et ajoutez-la en haut de ce fichier. En voici une pour vous :

> Pourquoi les programmeurs Java portent-ils des lunettes ?  
> .  
> .  
> .  
> .  
> Parce qu'ils ne voient pas C#!

### 4. Valider le code

Maintenant, sauvegardons et validons ce fichier. Si vous validez un fichier nouvellement créé, vous devrez d'abord l'ajouter à votre staging. Vous pouvez le faire en utilisant :

`git add <filename>`

Une fois votre fichier en staging, vous pouvez le valider. Assurez-vous d'ajouter un message à votre validation qui vous aidera à vous souvenir dans le futur de ce dont il s'agit.

`git commit -m "Ajout d'une DevJoke sur C#`

### 5. Pousser le code

Rappelez-vous, lorsque vous travaillez sur un dépôt sur lequel d'autres personnes travaillent également, il est possible que, pendant que vous travailliez sur votre version locale, certaines personnes aient poussé du code. Ainsi, le serveur est maintenant "une étape en avance sur vous". Vous devez maintenant synchroniser votre ordinateur avec le serveur pour vous assurer que vous avez le code le plus à jour. Pour ce faire, vous pouvez tirer depuis le serveur :

`git pull origin <branch-name>`

Si vous n'avez jamais créé de branche, ne vous inquiétez pas. Git vous donne la branche `master` par défaut. Vous pouvez également créer une nouvelle branche en utilisant :

```
git checkout -b <branch-name>
```

Maintenant que vous avez validé votre code et que votre machine locale est mise à jour depuis le serveur, vous êtes prêt à pousser vos modifications pour que le monde les voie. Pour pousser vers la branche `master`, vous pouvez le faire en utilisant :

git push origin master

YAYY !!! Vous avez fait votre premier push ! Donnez-vous une tape dans le dos. C'était la partie difficile. Maintenant, vous êtes prêt à valider à tout va.

### 6. Créer une Pull Request

Maintenant, envoyez-moi cette merveilleuse #DevJoke en créant une pull request. Une pull request est une fonctionnalité par laquelle vous, le développeur, me demandez, le propriétaire du code, de fusionner votre code dans le dépôt. Créer une pull request est facile. Allez sur github.com et ouvrez le dépôt sur lequel vous avez travaillé.

Vous verrez un bouton Pull request comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-87.png)

Cliquez sur le bouton et suivez les instructions pour créer une pull request. Assurez-vous que vos modifications sont correctement reflétées sur l'écran "Comparaison des modifications".

Cliquez sur "Créer une pull request" et c'est tout ! Vous avez terminé ! Vous avez réussi à créer votre première Pull Request !

?????????????????????????????

Maintenant, allez-y et envoyez-moi cette DevJoke !

---

Avez-vous appris quelque chose de nouveau ? Avez-vous des commentaires ? Connaissez-vous une DevJoke ? [Tweetez-moi @shrutikapoor08](https://twitter.com/shrutikapoor08?source=post_page---------------------------)

%[https://twitter.com/shrutikapoor08/status/1145925236946161665?s=20]