---
title: Comment faire votre premier commit Git
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2018-08-18T16:23:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-your-first-git-commit-a0581cb774f7
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9caaf4740569d1a4ca8e54.jpg
tags:
- name: Git
  slug: git
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment faire votre premier commit Git
seo_desc: 'Note: This is the second video in my Git for beginners series. Watch the
  first video here.

  Today we’re going to talk about how to make your first Git commit.

  If you open up Fork from where we left off before, you’ll see the project screen.
  If you cli...'
---

Note : Il s'agit de la deuxième vidéo de ma série Git pour débutants. [Regardez la première vidéo ici](https://zellwk.com/blog/setting-up-git).

Aujourd'hui, nous allons parler de la façon de faire votre premier commit Git.

Si vous ouvrez Fork depuis [là où nous nous étions arrêtés](https://medium.freecodecamp.org/how-to-set-up-a-git-client-in-just-a-few-minutes-3d78b8d2264f), vous verrez l'écran du projet. Si vous cliquez sur les modifications, l'écran se divise en deux parties.

À gauche de l'écran, vous verrez une section intitulée fichiers non préparés. En dessous de cette section, vous verrez une autre section intitulée fichiers préparés.

À droite, vous verrez un espace réservé qui affiche l'icône de Fork. En bas, vous verrez quelques champs :

1. Un champ de message de commit
2. Un champ de description
3. Une case à cocher modifiée
4. Un bouton de commit

Cela s'appelle la **zone de préparation**. C'est ici que vous décidez quels fichiers vous voulez enregistrer dans Git.

![Image](https://cdn-media-1.freecodecamp.org/images/0*z0qu2lqJZwZ87_WP.png)

### Préparer un fichier

Avant d'enregistrer quoi que ce soit, vous devez apporter une modification dans le dépôt Git.

Ouvrez votre projet Git dans un éditeur de texte comme VS Code. Créez un fichier appelé `index.html` et donnez-lui un peu de HTML pour commencer.

Une fois que vous avez enregistré ce fichier, vous verrez ce fichier dans la zone de préparation. Il devrait apparaître dans la section des fichiers non préparés de la zone de préparation.

![Image](https://cdn-media-1.freecodecamp.org/images/0*_5EDE_vPmD2X9uaY.png)

**Un fichier non préparé est un fichier qui a été modifié depuis votre dernier commit dans le dépôt Git.**

Si vous voulez commiter un fichier (dans ce cas, le fichier `index.html`), vous pouvez cliquer sur le fichier et cliquer sur stage. Ce fichier sera déplacé de la section des fichiers non préparés vers la section des fichiers préparés.

![Image](https://cdn-media-1.freecodecamp.org/images/0*m6JbL6aElj11k9yl.png)

**Lorsque vous avez un fichier dans la section des fichiers préparés**, ce que vous dites, c'est **que vous voulez enregistrer ce fichier lorsque vous faites un commit**.

Si vous cliquez sur le fichier, vous verrez les lignes de code (en vert) qui seront enregistrées dans le dépôt.

### Créer un commit

Pour créer un commit, vous écrivez votre message de commit en bas à droite, puis vous cliquez sur le bouton "créer un commit".

![Image](https://cdn-media-1.freecodecamp.org/images/0*ZtPjvgZI42RK1Rwr.png)

Une fois que vous avez cliqué sur le bouton de commit, les fichiers préparés disparaîtront de la zone de préparation. Cela est dû au fait que les fichiers sont enregistrés — il n'y a plus de nouvelles modifications pour le fichier dans le dépôt.

### Commiter plusieurs fichiers

Vous pouvez commiter plusieurs fichiers en même temps. Pour ce faire, vous devez modifier plusieurs fichiers.

Dans cet exemple, j'ai ajouté un fichier CSS et un fichier JavaScript au dépôt. J'ai également ajouté du code au fichier `index.html` pour pointer vers les fichiers CSS et JavaScript.

Si vous retournez dans Fork maintenant, vous devriez voir les dossiers et fichiers qui ont été modifiés.

![Image](https://cdn-media-1.freecodecamp.org/images/0*o7IRLjIX4NW2xLZg.png)

Pour commiter les trois fichiers en une seule fois, vous sélectionnez les fichiers et cliquez sur le bouton de préparation. Ensuite, vous écrivez votre message de commit et vous commitez les fichiers.

![Image](https://cdn-media-1.freecodecamp.org/images/0*fLy8BmEjCBv0gsh8.png)

### Vérifier l'historique Git

Si vous cliquez sur Tous les commits dans la barre latérale, vous verrez les commits que vous avez faits jusqu'à présent. Dans certains clients Git, cela s'appelle l'historique Git.

### Exercice

Essayez de faire quelques commits dans votre dépôt Git avec Fork. Dans la prochaine vidéo, je vous montrerai comment pousser vers un dépôt distant et comment tirer depuis un dépôt distant.

Merci d'avoir lu. Cet article vous a-t-il aidé d'une manière ou d'une autre ? Si c'est le cas, [j'espère que vous envisagerez de le partager](http://twitter.com/share?text=Your%20first%20Git%20commit%20by%20@zellwk%20?%20&url=https://zellwk.com/blog/your-first-git-commit/&hashtags=). Vous pourriez aider quelqu'un qui se sentait de la même manière que vous avant de lire l'article. Merci.

Cet article a été publié à l'origine sur [mon blog](https://zellwk.com/blog/your-first-git-commit).

Inscrivez-vous à ma [newsletter](https://zellwk.com/) si vous voulez plus d'articles pour vous aider à devenir un meilleur développeur frontend.