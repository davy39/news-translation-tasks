---
title: Commandes Git de base – Comment utiliser Git dans un projet réel
subtitle: ''
author: Okoro Emmanuel Nzube
co_authors: []
series: null
date: '2022-07-20T16:39:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-basic-git-and-github-commands
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/git-and-github.png
tags:
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: version control
  slug: version-control
seo_title: Commandes Git de base – Comment utiliser Git dans un projet réel
seo_desc: 'In my previous tutorial we talked about what version control is, how Git
  and GitHub work, and how to setup an account with GitHub.

  Today we will be looking at how to use some basic Git commands in a real project.

  I created a simple project that we''ll...'
---

Dans mon [tutoriel précédent](https://www.freecodecamp.org/news/git-and-github-the-basics/), nous avons parlé de ce qu'est le contrôle de version, du fonctionnement de Git et GitHub, et de la manière de configurer un compte avec GitHub.

Aujourd'hui, nous allons voir comment utiliser certaines commandes Git de base dans un projet réel.

J'ai créé un projet simple que nous utiliserons dans ce tutoriel.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/Document---Google-Chrome-7_18_2022-6_54_37-AM.png align="left")

*Interface du projet*

En suivant ce tutoriel, vous apprendrez comment :

* Créer un dépôt dans GitHub

* Initialiser Git dans votre projet

* Ajouter et commiter votre projet

* Pousser votre projet vers GitHub

* Ajouter et supprimer un fichier d'un dépôt

## Comment créer un dépôt dans GitHub

J'ai construit le projet exemple ci-dessus en utilisant HTML et CSS. Pour initialiser Git dans le projet, je dois créer un nouveau dépôt dans mon compte GitHub.

Je peux faire cela en me connectant à mon compte, puis en cliquant sur le bouton `new` situé en haut à droite de l'écran. Une fois ouvert, je vais saisir le nom de mon dépôt, la description, puis choisir si je veux que mon projet soit accessible publiquement ou privément. Ensuite, je cliquerai sur "Create repository."

![Image](https://www.freecodecamp.org/news/content/images/2022/07/Create-a-New-Repository---Google-Chrome-7_18_2022-7_43_32-AM.png align="left")

## Comment initialiser Git

Nous ne pouvons pas utiliser Git dans notre projet si nous ne l'initialisons/démarrons pas d'abord avec la commande `git init`.

Ainsi, après avoir créé le dépôt dans GitHub, j'ouvrirai le projet dans mon éditeur VS Code, j'irai dans mon terminal, puis j'utiliserai la commande `git init` pour initialiser/démarrer.

Lorsque vous exécutez cette commande dans votre terminal, vous remarquerez certains changements de couleur dans votre projet. Vous verrez également un symbole `U` qui signifie que vos fichiers ne sont pas suivis.

De plus, lorsque vous ouvrez le dossier où votre projet est stocké/situé, vous verrez un autre dossier nommé `.git` qui a été automatiquement créé lorsque vous avez exécuté la commande `git init`.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/git-add.jpg align="left")

*git add*

![Image](https://www.freecodecamp.org/news/content/images/2022/07/bandicam-2022-07-18-02-40-08-007.jpg align="left")

*.git folder*

## Comment ajouter et commiter votre projet

### Comment utiliser la commande `git add`

Ajouter le projet à la zone de staging aide Git à suivre votre projet et à voir les changements que vous avez apportés.

Pour ajouter votre projet à la zone de staging, exécutez la commande `git add .`. Lorsque vous exécutez cette commande, vous verrez que le symbole `U` change automatiquement en `A`. Cela signifie que vos fichiers ont été ajoutés à la zone de staging et sont maintenant suivis par Git, en attente d'être commités.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/git-add-1.jpg align="left")

*git add*

### Comment utiliser la commande `git commit`

En exécutant la commande `git commit`, vous sauvegardez cette étape particulière et les changements apportés à votre projet de manière permanente dans le dépôt Git. Et bien que vous puissiez apporter quelques modifications au projet à l'avenir et les commiter également, ce commit particulier que vous avez fait maintenant sera toujours sauvegardé dans le dépôt Git et pourra être accessible à tout moment.

Ainsi, après que votre projet a été ajouté à la zone de staging, la prochaine chose que vous voudrez faire est de le commiter en utilisant la commande `git commit –m "first commit"`.

Lorsque vous exécutez cette commande, vous devriez remarquer que le symbole `A` dans le projet n'est plus là, et le projet semble à nouveau comme vous vous y attendiez.

## Comment pousser votre projet vers GitHub

Pousser votre projet vers GitHub aide à prévenir la corruption/perte de votre projet dans le stockage local. Cela vous permet également d'accéder librement au dépôt GitHub depuis n'importe quel endroit, avec n'importe quel ordinateur (pas nécessairement votre ordinateur personnel).

Pour pouvoir pousser votre projet vers le dépôt GitHub, vous devrez ajouter le dépôt distant que vous avez créé initialement dans GitHub.

Pour ce faire, vous utiliserez la commande `git remote add origin (nom du dépôt)`. Dans mon cas, le nom de mon dépôt est [`https://github.com/Derekvibe/FoodResturant.git`](https://github.com/Derekvibe/FoodResturant.git). L'écrire dans le terminal devrait ressembler à ceci :

`git remote add origin [https://github.com/Derekvibe/FoodResturant.git](https://github.com/Derekvibe/FoodResturant.git)`

![Image](https://www.freecodecamp.org/news/content/images/2022/07/bandicam-2022-07-19-20-32-00-790.jpg align="left")

Si vous n'êtes pas sûr de la branche actuelle sur laquelle vous travaillez, utilisez la commande `git branch`. Si elle affiche la branche comme `master`, nous la changerons en branche `main` en exécutant la commande `git branch –M main`.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/git-branch.jpg align="left")

*(ma branche git)*

Dans mon cas, j'avais déjà configuré ma branche par défaut pour qu'elle soit `branch main` lorsque j'ai installé Git sur mon ordinateur en exécutant la commande `git config –global init.default branch main`. Je n'ai donc pas besoin d'exécuter à nouveau la commande `git branch –M main`.

Enfin, après avoir ajouté le dépôt distant où vous souhaitez télécharger le projet et avoir changé la branche en `main`, vous voudrez pousser votre projet vers GitHub.

Pour y parvenir, exécutez la commande `git push –u origin main` et attendez qu'elle se charge complètement.

Lorsque cela est fait, allez dans le dépôt Git que vous avez créé dans GitHub et actualisez la page. Vous verrez que tous vos projets dans le dépôt local ont été téléchargés vers le dépôt GitHub.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/git-push-image.jpg align="left")

À partir de ce moment, après avoir apporté des modifications au projet, vous devez simplement ajouter les modifications à la zone de staging en exécutant la commande `git add .`. Ensuite, vous pouvez les commiter en utilisant `git commit –m "(nom du commit)"` et les pousser vers le dépôt Git en utilisant `git push –u origin main`.

## Comment ajouter et supprimer un fichier d'un dépôt

À ce stade, je vais vous montrer comment ajouter et supprimer un nouveau fichier d'un dépôt GitHub.

### Comment ajouter un nouveau fichier à un dépôt existant

Pour résumer : j'ai ajouté un nouveau fichier à mon projet avec le nom `newfile.txt`. Je l'ai ajouté à la zone de staging en exécutant `git add newfile.txt`, puis je l'ai commité en utilisant `git commit –m "new commit"` et je l'ai poussé vers GitHub, tout comme nous l'avons fait lorsque nous voulions télécharger l'ensemble du projet vers GitHub.

Lorsque j'ai actualisé ma page GitHub, j'ai dû voir le nouveau fichier que j'ai créé s'afficher.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/bandicam-2022-07-18-07-14-54-352-1.jpg align="left")

### Comment supprimer un fichier d'un dépôt existant

Si je veux supprimer/retirer le fichier que je viens de créer de mon projet dans GitHub, je peux le faire en exécutant la commande `git rm newfile.txt` dans le terminal.

Lorsque j'exécute cette commande dans mon terminal, j'ajouterai les modifications à la zone de staging en utilisant `git add .`, puis je commiterai et pousserai les modifications vers le dépôt GitHub.

Lorsque j'actualise ma page GitHub, le fichier sera supprimé de mon dépôt GitHub. De plus, lorsque je vais dans mon stockage local, le fichier devrait également être supprimé de là.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/bandicam-2022-07-18-07-02-35-474.jpg align="left")

![Image](https://www.freecodecamp.org/news/content/images/2022/07/bandicam-2022-07-18-07-10-12-196.jpg align="left")

## Conclusion

Dans ce tutoriel, vous avez appris comment utiliser les commandes Git de base pour gérer vos projets.

[Cliquez ici](https://github.com/Derekvibe/FoodResturant) pour accéder à mon dépôt GitHub pour ce projet afin de pouvoir l'essayer par vous-même.

J'espère que ce tutoriel vous a été utile.

**Amusez-vous bien à coder !**