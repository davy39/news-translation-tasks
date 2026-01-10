---
title: 'Git Fetch vs Pull : Quelle est la différence entre les commandes Git Fetch
  et Git Pull ?'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-27T21:34:00.000Z'
originalURL: https://freecodecamp.org/news/git-fetch-vs-pull
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e70740569d1a4ca3d14.jpg
tags:
- name: Git
  slug: git
seo_title: 'Git Fetch vs Pull : Quelle est la différence entre les commandes Git Fetch
  et Git Pull ?'
seo_desc: 'Git pull and fetch are two commands that are regularly used by Git users.
  Let’s see the difference between both commands.

  For the sake of context, it’s worth remembering that we’re probably working in a
  clone repo. What’s a clone? It''s simply a dupli...'
---

Les commandes `pull` et `fetch` de Git sont deux commandes régulièrement utilisées par les utilisateurs de Git. Voyons la différence entre ces deux commandes.

Pour le contexte, il est utile de rappeler que nous travaillons probablement dans un dépôt cloné. Qu'est-ce qu'un clone ? Il s'agit simplement d'une copie d'un autre dépôt. C'est essentiellement obtenir votre propre copie du code source de quelqu'un d'autre.

Cela dit, pour garder votre clone à jour avec les modifications qui ont pu être appliquées à l'original, vous devrez apporter ces modifications à votre clone.

C'est là que `fetch` et `pull` interviennent.

`git fetch` est la commande qui indique à votre git local de récupérer les dernières informations de métadonnées de l'original (mais ne transfère aucun fichier. C'est plus comme une simple vérification pour voir s'il y a des changements disponibles).

`git pull`, en revanche, fait cela ET apporte (copie) ces changements depuis le dépôt distant.

Par exemple :

```text
git pull origin ankur bugfix
```

L'essentiel à retenir est qu'il y a généralement au moins trois copies d'un projet sur votre poste de travail.

* Une copie est votre propre dépôt avec votre propre historique de commits (celui déjà sauvegardé, pour ainsi dire).
* La deuxième copie est votre copie de travail où vous éditez et construisez (pas encore validée dans votre dépôt).
* La troisième copie est votre copie locale "en cache" d'un dépôt distant (probablement l'original à partir duquel vous avez cloné le vôtre).

Vous pouvez utiliser `git fetch` pour connaître les changements effectués dans le dépôt/branche distant depuis votre dernier pull. Cela est utile pour permettre une vérification avant de faire un pull réel, qui pourrait changer des fichiers dans votre branche actuelle et votre copie de travail (et potentiellement perdre vos changements, etc.).

```text
git fetch    
git diff ...origin
```