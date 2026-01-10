---
title: 'Erreur : src refspec master does not match any – Comment le corriger dans
  Git'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-08-01T13:58:44.000Z'
originalURL: https://freecodecamp.org/news/error-src-refspec-master-does-not-match-any-how-to-fix-in-git
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/refspec-master-error.png
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: 'Erreur : src refspec master does not match any – Comment le corriger dans
  Git'
seo_desc: "By Dillion Megida\nWhen working with Git, you may come across an error\
  \ that says \"src refspace master does not match any\". \nHere's what the error\
  \ means and how you can solve it.\nWhat Does src refspec master does not match any\
  \ Mean in Git?\nYou may get ..."
---

Par Dillion Megida

Lorsque vous travaillez avec Git, vous pouvez rencontrer une erreur indiquant « src refspace master does not match any ».

Voici ce que signifie cette erreur et comment vous pouvez la résoudre.

## Que signifie `src refspec master does not match any` dans Git ?

Vous pouvez obtenir cette erreur lorsque vous essayez de déclencher un push depuis un dépôt local vers un dépôt master comme ceci :

```bash
git push origin master
```

Cette erreur peut survenir pour différentes raisons.

La raison la plus probable pour laquelle cette erreur se produit est que la branche `master` n'existe pas.

Peut-être avez-vous cloné un nouveau dépôt et la branche par défaut est `main`, donc il n'y a pas de branche master lorsque vous essayez de pousser vers celle-ci.

Vous pouvez afficher les branches distantes connectées à un dépôt local en utilisant la commande `git branch -b` comme ceci :

```bash
git branch -b

# résultats
#  origin/main
#  origin/feat/authentication
#  origin/other branches ...
```

Avec les résultats ci-dessus, vous pouvez voir qu'il n'y a pas de dépôt `master` (`origin/master`). Donc, lorsque vous essayez de pousser vers ce dépôt, vous obtiendrez l'erreur "respec error".

Ce résultat s'applique également à toute autre branche qui n'existe pas. Supposons, par exemple, que je fasse des modifications et que je pousse vers une branche distante `hello` qui n'existe pas :

```bash
git add .
git commit -m "new changes"
git push origin hello
```

Cette commande produira l'erreur suivante :

```bash
error: src refspec hello does not match any
```

## Comment corriger l'erreur "src refspec master does not match any"

Maintenant, vous êtes conscient que la branche `master` n'existe pas. La solution à cette erreur est soit de créer une branche `master` locale et distante vers laquelle vous pouvez pousser le commit, soit de pousser le commit vers une branche existante – peut-être `main`.

Vous pouvez créer une branche distante `master` sur un site géré par Git (comme GitHub) ou vous pouvez le faire directement depuis votre terminal comme ceci :

```bash
git checkout -b master

# ajouter un commit

git push origin master
```

Ces commandes créeront une branche `master` localement. Et en poussant vers `origin master`, la branche `master` sera également créée à distance.

Mais si vous ne souhaitez pas créer une branche `master`, vous pouvez utiliser la branche par défaut existante (qui peut être `main`) à la place.

## Conclusion

Donc, si vous obtenez l'erreur `Error: src refspec master does not match any` lorsque vous essayez de pousser vers master, la raison la plus plausible est que la branche `master` n'existe pas.