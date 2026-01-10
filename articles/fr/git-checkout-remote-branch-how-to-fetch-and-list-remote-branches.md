---
title: Git Checkout Remote Branch – Comment récupérer et lister les branches distantes
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2024-04-30T16:53:44.733Z'
originalURL: https://freecodecamp.org/news/git-checkout-remote-branch-how-to-fetch-and-list-remote-branches
coverImage: https://cdn.hashnode.com/res/hashnode/image/stock/unsplash/UT8LMo-wlyk/upload/c907bdb799b1331e27dd68f35a2b2e25.jpeg
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: Git Checkout Remote Branch – Comment récupérer et lister les branches distantes
seo_desc: You can use branches in Git to work on different features without affecting
  your main codebase. For example, you can experiment with a new layout for your webpage
  on a different branch without affecting the main branch where your website is being
  dep...
---

Vous pouvez utiliser des branches dans Git pour travailler sur différentes fonctionnalités sans affecter votre base de code principale. Par exemple, vous pouvez expérimenter une nouvelle mise en page pour votre page web sur une branche différente sans affecter la branche principale à partir de laquelle votre site web est déployé.

Les branches sont utilisées à différentes fins comme le développement de fonctionnalités, les corrections de bugs, la gestion des versions, l'expérimentation, [la contribution à des projets open source](https://contribute.freecodecamp.org/#/), et ainsi de suite.

Dans cet article, vous apprendrez à utiliser différentes commandes Git pour interagir avec les branches distantes.

# Comment récupérer et lister les branches distantes

J'ai créé un dépôt (repo) pour cet article avec trois branches différentes : main, feat/create-hobbies-list, et feat/create-language-list. Vous pouvez télécharger le dépôt [ici](https://github.com/ihechikara/git-branches-article), ou le cloner sur votre ordinateur en utilisant cette commande :

```bash
git clone https://github.com/ihechikara/git-branches-article.git
```

La commande ci-dessus télécharge la branche principale du dépôt sur votre ordinateur.

N'hésitez pas à suivre avec votre propre base de code/dépôt Git.

## Comment lister les branches distantes

Lorsque vous regardez le dépôt que vous venez de cloner sur GitHub, vous remarquerez qu'il y a trois branches.

Mais lorsque vous exécutez la commande `git branch`, vous n'obtenez qu'une liste des branches dans le dépôt local. Dans notre cas, il s'agit de la branche main. Cela se produit pour plusieurs raisons :

* La commande `git branch` ne montre que les branches locales.

* Cloner une branche ne télécharge pas automatiquement toutes les autres branches du dépôt distant.

Alors, comment lister les branches distantes ? Vous pouvez le faire en utilisant la commande `git branch -r` :

```bash
git branch -r

origin/HEAD -> origin/main
origin/feat/create-hobbies-list
origin/feat/create-language-list
origin/main
```

À partir de la sortie de la commande ci-dessus, vous pouvez voir toutes les branches du dépôt distant. La branche main qui agit également comme la branche par défaut (origin/HEAD), et deux autres branches : feat/create-hobbies-list et feat/create-language-list.

Maintenant que vous savez comment lister les branches distantes, voyons comment les récupérer et travailler dessus localement.

## Comment récupérer les branches distantes

Vous pouvez récupérer des branches distantes pour différentes raisons comme la révision de code, la mise à jour de votre dépôt local avec les modifications apportées au dépôt distant, l'expérimentation, et ainsi de suite.

### Comment récupérer les branches distantes en utilisant `git fetch`

Vous pouvez utiliser la commande `git fetch` pour "récupérer" les modifications récentes apportées au dépôt distant sans les fusionner dans votre dépôt local.

Par exemple, supposons que de nouvelles modifications ont été poussées vers la branche feat/create-language-list. Lorsque vous exécutez la commande `git fetch`, Git récupère les nouvelles modifications dans le dépôt distant, mais vous ne les verrez pas dans votre branche/repo local.

Vous pouvez ensuite utiliser des commandes comme `git diff` et `git log` pour comparer les modifications.

Dans un cas où vous êtes satisfait des modifications, vous pouvez utiliser la commande `git merge` pour fusionner ces modifications dans votre branche locale. À ce stade, les modifications de la branche distante seront visibles/localement.

C'est-à-dire :

```bash
git checkout feat/create-language-list
```

La commande ci-dessus bascule vers la branche feat/create-language-list.

```bash
git fetch
```

La commande ci-dessus récupère les modifications actuelles apportées à la branche distante qui ne sont pas dans votre branche locale.

```bash
git diff feat/create-language-list origin/feat/create-language-list
```

La commande ci-dessus compare les modifications que vous venez de récupérer avec votre branche locale. Dans le terminal, les caractères rouges désignent l'état de votre branche locale tandis que les caractères verts désignent les nouvelles modifications de la branche distante. C'est-à-dire :

![git diff command showing changes retrieved from remote branch](https://cdn.hashnode.com/res/hashnode/image/upload/v1714451407216/fd2ec3a7-a20f-4c1f-94a1-d7e916f183d4.png align="center")

```bash
git merge
```

La commande ci-dessus fusionne les modifications dans votre branche locale. Dans ce cas, le fichier **languages.txt** sera mis à jour avec les nouvelles modifications.

En résumé, `git fetch` récupère les modifications tandis que `git merge` fusionne les modifications dans votre branche locale.

### Comment récupérer les branches distantes en utilisant `git pull`

La commande `git pull` est similaire à `git fetch` et `git merge`.

La différence est que `git pull` fusionne automatiquement les nouvelles modifications dans votre branche locale. C'est-à-dire que vous ne pouvez pas comparer les modifications avant de les fusionner (vous n'aurez pas la chance d'exécuter `git diff`).

`git pull` exécute à la fois `git fetch` et `git merge` en même temps.

Ainsi, une fois que vous exécutez la commande `git pull`, les modifications distantes apparaîtront localement s'il n'y a pas de conflits de fusion.

# Conclusion

Dans cet article, vous avez appris à lister les branches distantes en utilisant la commande `git branch -r`.

Vous avez également appris à récupérer les branches distantes. La commande `git fetch` récupère les modifications de la branche distante tandis que la commande `git merge` fusionne les modifications distantes dans votre branche locale. Ce processus vous donne l'opportunité de comparer les modifications avant de les fusionner.

D'autre part, la commande `git pull` récupère et fusionne automatiquement les modifications d'une branche distante tant qu'il n'y a pas de conflits de fusion.

Bon codage !