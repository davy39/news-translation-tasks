---
title: Qu'est-ce qu'une branche distante dans Git ? Comment vérifier les branches
  distantes depuis GitHub
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2023-02-22T16:22:30.000Z'
originalURL: https://freecodecamp.org/news/remote-branches-in-git
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/pexels-antonio-borriello-1297611.jpg
tags:
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: version control
  slug: version-control
seo_title: Qu'est-ce qu'une branche distante dans Git ? Comment vérifier les branches
  distantes depuis GitHub
seo_desc: 'Git is a free and open-source tool. Specifically, it is the most popular
  version control system used in software development today.

  Git allows you to keep track of and maintain different versions of a coding project.

  With Git, developers and technica...'
---

Git est un outil gratuit et open-source. Plus précisément, c'est le système de contrôle de version le plus populaire utilisé dans le développement logiciel aujourd'hui.

Git vous permet de suivre et de maintenir différentes versions d'un projet de codage.

Avec Git, les développeurs et les équipes techniques peuvent collaborer et travailler ensemble sur un projet.

Plusieurs développeurs peuvent travailler sur les mêmes parties ou sur des parties différentes du projet en parallèle sans interférer les uns avec les autres, augmentant ainsi la productivité et l'efficacité.

Les développeurs peuvent collaborer simultanément et travailler dans leurs environnements grâce aux fonctionnalités et outils intégrés que Git fournit, dont l'un est les branches.

## Qu'est-ce qu'une branche dans Git ?

Une branche dans Git est une zone de développement séparée, sûre et isolée qui diverge du projet principal.

Les branches permettent aux développeurs de travailler sur de nouvelles fonctionnalités, de corriger des bugs, d'expérimenter de nouvelles idées et de réduire le risque de casser le code stable dans la base de code.

### Branches locales VS branches distantes – Quelle est la différence ?

Dans Git, il existe deux types de branches : les branches locales et les branches distantes.

Une branche locale n'existe que sur votre machine locale.

Toutes les modifications que vous introduisez et validez dans votre dépôt local sont stockées uniquement sur votre système local. Elles offrent un moyen d'expérimenter, de corriger des bugs et de développer de nouvelles fonctionnalités sans affecter la base de code principale.

Pour créer une branche locale, vous utilisez la commande `git branch <nom-de-la-branche>`, où `nom-de-la-branche` est le nom de votre nouvelle branche.

Par exemple, si vous souhaitez créer une nouvelle branche appelée `test`, vous utiliseriez la commande suivante :

```bash
git branch test
```

Vous pouvez utiliser la commande `git checkout` pour naviguer vers la nouvelle branche et créer les modifications que vous souhaitez :

```bash
git checkout test
```

Pour voir une liste de vos branches locales, utilisez la commande `git branch`.

Tout cela dit, vous ne pouvez pas collaborer avec d'autres développeurs sur une branche locale. C'est là que les branches distantes deviennent utiles.

Les branches distantes permettent aux développeurs de collaborer sur le même projet simultanément.

Une branche distante existe dans un dépôt distant (le plus souvent appelé `origin` par convention) et est hébergée sur une plateforme telle que [GitHub](https://github.com/).

Une fois que vous avez validé les modifications dans votre branche locale, vous pouvez pousser la branche locale vers le dépôt distant (`origin`) en utilisant la syntaxe `git push <remote> <local>`. Ensuite, les autres pourront voir votre code.

```bash
git push -u origin test
```

Git créera une copie de votre branche locale sur le dépôt distant. Cette copie est connue sous le nom de branche distante.

Pour voir une liste de toutes les branches distantes dans votre projet, utilisez la commande `git branch -r`.

## Comment vérifier une branche distante dans Git

Vous devrez peut-être accéder à une branche créée par un autre développeur à des fins de révision ou de collaboration.

Cette branche n'est pas sur votre système local – c'est une branche distante stockée sur le dépôt distant.

Le problème est que Git ne vous permet pas automatiquement de travailler sur les branches de quelqu'un d'autre.

Au lieu de cela, vous devez créer une copie locale qui reflète la branche distante avec laquelle vous souhaitez travailler, puis apporter des modifications localement.

Voyons les étapes que vous devez suivre dans les sections suivantes.

### Comment récupérer toutes les branches distantes

Tout d'abord, vous devez récupérer les données de branche nécessaires à l'aide de la commande `git fetch` et du nom du dépôt distant :

```bash
git fetch origin
```

Cette commande téléchargera les dernières modifications (y compris les branches distantes) depuis le dépôt distant vers votre machine locale.

Si vous avez un autre nom de dépôt distant, remplacez `origin` par celui-ci.

### Comment voir les branches disponibles pour le checkout

Ensuite, pour voir une liste des branches disponibles pour le checkout, utilisez la commande suivante :

```bash
git branch -r
```

L'option `-r` (pour distant) indique à Git de lister les branches distantes.

Le résultat de cette commande sera une liste de toutes les branches distantes disponibles pour le checkout. Vous verrez le préfixe `remotes/origin` avant le nom de la branche.

### Comment vérifier la branche distante

Vous ne pouvez pas apporter de modifications directement à la branche distante qui vous intéresse – vous avez besoin d'une copie locale.

Vous devez vérifier la branche qui vous intéresse afin de pouvoir commencer à travailler localement sur les modifications que vous souhaitez apporter.

Pour ce faire, utilisez la commande `git checkout` avec l'option `-b` (pour la branche). La syntaxe ressemble à quelque chose comme ceci :

```bash
git checkout -b <nouveau-nom-de-branche-locale> origin/<nom-de-branche-distante>
```

Ainsi, si vous vouliez une copie de la branche distante `new-feature`, vous feriez ce qui suit :

```bash
git checkout -b new-feature origin/new-feature
```

La commande ci-dessus crée une nouvelle copie locale sur votre machine qui est basée sur et connectée à la branche distante.

Elle crée une nouvelle branche appelée `new-feature`, vérifie cette branche et extrait les modifications de `origin/new-feature` vers la nouvelle branche.

Maintenant, vous pouvez pousser de nouveaux commits vers `origin/new-feature`.

### Merci d'avoir lu !

Maintenant, vous savez comment vérifier et travailler avec des branches distantes dans Git. Bon codage !