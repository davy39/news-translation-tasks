---
title: Comment créer une branche locale dans Git
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-07-13T16:41:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-local-git-branch
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/cover-template.jpg
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: Comment créer une branche locale dans Git
seo_desc: 'When you''re making changes to a Git repository, it''s a best practice
  to push to a different branch first. This lets you compare changes before submitting
  a pull request and finally merging it.

  This is especially crucial when working with other develo...'
---

Lorsque vous apportez des modifications à un dépôt Git, il est considéré comme une bonne pratique de pousser d'abord vers une branche différente. Cela vous permet de comparer les changements avant de soumettre une demande de tirage (pull request) et de finalement les fusionner.

Cela est particulièrement crucial lorsque vous travaillez avec d'autres développeurs.

Votre dépôt contient par défaut une seule branche, la branche `main`, qui est considérée comme la branche de référence. Passons maintenant rapidement en revue comment créer des branches dans Git.

## Comment créer des branches dans Git

En essence, il existe deux méthodes dans Git pour créer des branches.

Vous pouvez utiliser une seule commande pour créer la branche et basculer vers celle-ci. Ou vous pouvez créer la branche d'abord avec une commande, puis basculer vers celle-ci plus tard avec une autre commande lorsque vous souhaitez travailler dessus.

Voici la version rapide du code :

```bash
// créer une branche et basculer vers la branche
$ git checkout -b <nom-de-la-branche>

// créer une branche uniquement
$ git branch <nom-de-la-branche>
```

### Comment créer une branche Git et basculer vers une nouvelle branche

Nous pouvons créer une nouvelle branche et basculer vers celle-ci en utilisant la commande `git checkout` avec l'option `-b` et `<nom-de-la-branche>`. Cela ressemble à ceci :

```bash
$ git checkout -b <nom-de-la-branche>
```

Supposons que nous voulons créer une nouvelle branche Git nommée "pagination" à partir de la branche main. Pour y parvenir, nous utiliserons la commande "git checkout" avec l'option "-b" et le nom de la branche "pagination".

![](https://paper-attachments.dropbox.com/s_E7E3F14C4905C4CE20AE3FDC33EFE78C3CAFED59288B605B89A9E40497700515_1657112003074_branch.gif align="left")

Comme vous pouvez le voir, nous avons créé une nouvelle branche, et la commande checkout a fait basculer automatiquement notre branche de "main" à "pagination".

Examinons maintenant comment créer une branche Git sans basculer vers celle-ci.

### Comment créer une branche Git sans basculer vers la nouvelle branche

Il s'agit de la méthode standard pour créer une branche en utilisant la commande `git branch` et en spécifiant le nom de la branche Git que vous souhaitez créer.

```bash
$ git branch <nom-de-la-branche>
```

Par exemple, comme nous l'avons fait précédemment, nous pouvons créer une branche pour "pagination" en remplaçant "" par "pagination". Voici à quoi cela ressemblerait :

![](https://paper-attachments.dropbox.com/s_E7E3F14C4905C4CE20AE3FDC33EFE78C3CAFED59288B605B89A9E40497700515_1657114781462_switch.gif align="left")

Comme nous pouvons le voir, la branche n'a pas changé, mais la nouvelle branche a été créée. Pour voir une liste de toutes les branches disponibles, vous pouvez utiliser cette commande :

```bash
$ git branch
```

Enfin, supposons que nous souhaitons plus tard basculer vers notre nouvelle branche Git ou toute autre branche que nous avons créée précédemment. Dans ce cas, nous pouvons utiliser la commande `git checkout`.

```bash
$ git checkout <nom-de-la-branche>
```

## Conclusion

Dans cet article, nous avons appris comment utiliser les commandes Git dans notre terminal pour créer une branche localement.

Si nous voulons ajouter cette branche à distance, tout ce que nous avons à faire est de la pousser vers notre fournisseur Git tel que GitHub en utilisant la commande suivante :

```bash
$ git push -u origin <nom-de-la-branche>
```

Apprenez comment [cloner une branche spécifique avec Git via cet article](https://joelolawanle.com/posts/how-to-clone-a-specific-branch-with-git).

Bon codage !

Vous pouvez accéder à plus de 200 de mes articles en [visitant mon site web](https://joelolawanle.com/contents). Vous pouvez également utiliser le champ de recherche pour voir si j'ai écrit un article spécifique.