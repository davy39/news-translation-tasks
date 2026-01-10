---
title: Comment renommer une branche locale et distante dans Git
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-05T17:19:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-rename-local-and-remote-git-branch
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/Rename-Git-Branch.png
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: Comment renommer une branche locale et distante dans Git
seo_desc: 'By Chaitanya Prabuddha

  Have you ever needed to rename a Git branch? If so, this article will assist you
  in resolving the problem.

  Git makes it simple to rename a git branch both locally and remotely. Let''s take
  a look at the solution.

  Why would you n...'
---

Par Chaitanya Prabuddha

Avez-vous déjà eu besoin de renommer une branche Git ? Si oui, cet article vous aidera à résoudre le problème.

Git simplifie le renommage d'une branche git, que ce soit en local ou à distance. Examinons la solution.

## Pourquoi auriez-vous besoin de renommer une branche dans Git ?

Les branches Git sont des étapes distinctes dans le développement de votre projet. Elles vous offrent un moyen de travailler parallèlement à votre branche principale tout en la gardant exempt de désordre et de code inachevé.

Dans la précipitation, vous pourriez nommer une branche qui ne décrit pas précisément le code, ou vous pourriez vouloir la renommer. La plupart des gens veulent changer les noms de leurs branches dans ces situations.

## Comment renommer une branche git locale

Vous pouvez utiliser cette commande si vous êtes déjà dans la branche locale que vous souhaitez renommer.

```
git branch -m <nouveau_nom>
```

Si vous êtes sur une autre branche et que vous souhaitez la renommer, utilisez la commande suivante :

```
git branch -m <ancien_nom> <nouveau_nom>
```

Utilisez la commande suivante pour déterminer le nom de votre branche actuelle :

```
git status
```

## Comment renommer une branche git distante

Si vous souhaitez renommer une branche qui a déjà été poussée vers un dépôt distant, utilisez la commande suivante :

```
git push origin -u <nouveau_nom>
```

Et maintenant, vous devrez supprimer l'ancien nom. Pour ce faire, utilisez cette commande :

```
git push origin --delete <ancien_nom>
```

Pour vérifier les modifications que vous venez d'effectuer, connectez-vous à votre portail client et vérifiez le dépôt que vous venez de modifier.

**C'est tout ! N'est-ce pas si simple ? 🤳**

J'écris également régulièrement dans ma newsletter. Vous pouvez vous inscrire directement ici. **👋👋**

<iframe src="https://thelearners.substack.com/embed" height="100"></iframe>