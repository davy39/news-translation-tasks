---
title: 'Comment comprendre Git : une introduction aux commandes de base, astuces et
  conseils'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-20T13:31:00.000Z'
originalURL: https://freecodecamp.org/news/understanding-git-basics-commands-tips-tricks
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/brandon-green-321795-unsplash.jpg
tags:
- name: Git
  slug: git
- name: General Programming
  slug: programming
- name: version control
  slug: version-control
seo_title: 'Comment comprendre Git : une introduction aux commandes de base, astuces
  et conseils'
seo_desc: 'By Goran Aviani

  Recently I’ve became a mentor to a colleague of mine. And my mentee has asked me
  about Git on several occasions. This is for you colleague! P.S. I should have written
  this article when we started but I hope it will help now!

  And remem...'
---

Par Goran Aviani

Récemment, je suis devenu mentor pour un collègue. Et mon mentoré m'a demandé plusieurs fois à propos de Git. C'est pour toi, collègue ! P.S. J'aurais dû écrire cet article quand nous avons commencé, mais j'espère qu'il aidera maintenant !

_Et n'oubliez pas : La meilleure façon d'apprendre quoi que ce soit est de le faire par vous-même ! Et comme mon mentor me le dit toujours : Udaraj !_

## Bases

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0-2GkM1pvDmnI2ksUM.png)

### Pourquoi Git est-il si important ?

Commençons par citer la première ligne de la page Wikipédia de Git :

> « **Git** (_[/ɡɪt/](https://en.wikipedia.org/wiki/Help:IPA/English)_) est un système de _[contrôle de version](https://en.wikipedia.org/wiki/Version-control)_ pour suivre les modifications dans les _[fichiers informatiques](https://en.wikipedia.org/wiki/Computer_file)_ et coordonner le travail sur ces fichiers entre plusieurs personnes. »

Ainsi, la fonction la plus basique et importante de Git est de permettre aux équipes d'ajouter (et de fusionner) du code en même temps sur le même projet. En ajoutant cette capacité aux projets, cela rend les équipes plus efficaces et leur donne la possibilité de travailler sur des projets plus grands et des problèmes plus complexes.

Il y a aussi beaucoup d'autres choses que Git fait très bien : il nous permet de revenir en arrière sur les changements, de créer de nouvelles branches pour ajouter de nouvelles fonctionnalités, de résoudre les conflits de fusion, et ainsi de suite.

### Comment fonctionne Git

Git stocke les projets dans des **dépôts**. Les **commits** sont faits sur le projet et ils indiquent à Git que vous êtes satisfait du nouveau code ou des modifications que vous avez créées.

Le nouveau code/les modifications sont validés sur des branches. La plupart du travail est validé sur d'autres branches puis fusionné avec la branche principale. Tout cela est stocké dans le même répertoire que le projet mais dans un sous-dossier appelé **.git**. 

Pour partager le code avec vos collègues, vous **poussez** les modifications vers le dépôt. Pour obtenir le nouveau code de vos collègues, vous **tirez** les modifications du dépôt.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0-SBz94SjR2tbvFY6n.jpg)

### Alors, qu'est-ce que GitHub, GitLab et Bitbucket ?

Je suis content que vous ayez posé la question ! Ces types d'applications sont appelés services de gestion de dépôts. Ils jouent un rôle crucial dans le développement logiciel moderne.

Bien que Git et GitHub soient les solutions de contrôle de version de choix pour la plupart des entreprises, GitHub a des concurrents sérieux comme GitLab et Bitbucket. Cependant, si vous savez utiliser GitHub, vous n'aurez aucun problème à travailler avec GitLab ou Bitbucket.

_Pour être clair : Git est l'outil, et GitHub est le service pour les projets qui utilisent Git._

#### Où puis-je découvrir des projets intéressants et me connecter à d'autres développeurs ?

GitHub, GitLab et Bitbucket ont des options de recherche de dépôts publics et la possibilité de suivre facilement d'autres utilisateurs.

Pouvez-vous maintenant voir pourquoi il est important de connaître Git et GitHub (GitLab/Bitbucket) ? La seule chose restante avant de parler des commandes est de vous donner quelques règles simples à toujours suivre lorsque vous utilisez Git :

* **Règle 1 :** Créez un dépôt Git pour chaque nouveau projet
* **Règle 2 :** Créez une nouvelle branche pour chaque nouvelle fonctionnalité

## Commandes

Pour commencer avec Git, vous devez l'avoir sur votre ordinateur. Si vous ne l'avez pas déjà, vous pouvez aller [ici](https://git-scm.com/) et suivre les instructions.

### Initialiser un nouveau dépôt Git : Git init

Tout ce que vous codez est suivi dans le dépôt. Pour initialiser un dépôt git, utilisez cette commande lorsque vous êtes dans le dossier du projet. Cela créera un dossier .git.

```
git init
```

### Git add

Cette commande ajoute un ou tous les fichiers modifiés à la zone de staging.

Pour ajouter simplement un fichier spécifique au staging :

```
git add filename.py
```

Pour mettre en staging les nouveaux fichiers, modifiés ou supprimés :

```
git add -A
```

Pour mettre en staging les nouveaux fichiers et ceux modifiés :

```
git add .
```

Pour mettre en staging les fichiers modifiés et supprimés :

```
git add -u
```

### Git commit

Cette commande enregistre le fichier dans l'historique des versions. Le -m signifie qu'un message de commit suit. Ce message est personnalisé et vous devriez l'utiliser pour informer vos collègues ou votre futur vous-même de ce qui a été ajouté dans ce commit.

```
git commit -m "votre texte"
```

### Git status

Cette commande listera les fichiers en couleurs vertes ou rouges. Les fichiers verts ont été ajoutés à la zone de staging mais pas encore validés. Les fichiers marqués en rouge sont ceux qui ne sont pas encore ajoutés à la zone de staging.

```
git status
```

## Travailler avec les branches

### Git branch branch_name

Cela créera une nouvelle branche :

```
git branch branch_name
```

### Git checkout branch_name

Pour passer d'une branche à une autre :

```
git checkout branch_name
```

#### Git checkout -b branch_name

Pour créer une nouvelle branche et y basculer automatiquement :

```
git checkout -b branch_name
```

Cela est l'équivalent de :

```
git branch branch_name
git checkout branch_name
```

### Git branch

Pour lister toutes les branches et voir sur quelle branche vous vous trouvez actuellement :

```
git branch
```

### Git log

Cette commande listera l'historique des versions pour la branche actuelle :

```
git log
```

---

## Push & Pull

### Git push

Cette commande envoie les modifications validées à un dépôt distant :

```
git push
```

### Git pull

Pour tirer les modifications du serveur distant vers votre ordinateur local :

```
git pull
```

Pour plus de commandes et une explication détaillée de celles listées, je vous recommande de consulter la documentation officielle de [Git](https://git-scm.com/docs/).

## Astuces & Conseils

### Abandonner toutes vos modifications non validées

Comme son nom l'indique, cette commande abandonnera toutes vos modifications non validées :

```
git reset --hard
```

### Supprimer un fichier de git sans le supprimer de votre ordinateur

Parfois, lors de l'utilisation de la commande « git add », vous pourriez ajouter des fichiers que vous ne vouliez pas ajouter.

Si vous n'êtes pas prudent lors d'un « git add », vous pourriez ajouter des fichiers que vous ne vouliez pas valider. Vous devriez supprimer la version mise en staging du fichier, puis ajouter le fichier à .gitignore pour éviter de faire la même erreur une seconde fois :

```
git reset file_name
echo filename >> .gitignore
```

### Modifier un message de commit

Il est très facile de corriger un message de commit :

```
git commit --amend -m "Nouveau message"
```

Merci d'avoir lu ! Consultez d'autres articles comme celui-ci sur mon profil freeCodeCamp : [https://www.freecodecamp.org/news/author/goran/](https://www.freecodecamp.org/news/author/goran/) et d'autres choses amusantes que je construis sur ma page GitHub : [https://github.com/GoranAviani](https://github.com/GoranAviani)