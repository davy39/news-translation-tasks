---
title: Comment tirer depuis un dépôt Git distant
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2018-09-03T23:37:18.000Z'
originalURL: https://freecodecamp.org/news/how-to-pull-from-a-git-remote-repository-b9fabb6b3c9d
coverImage: https://cdn-media-1.freecodecamp.org/images/0*3MKmgO4C_GLI_of0.png
tags:
- name: Git
  slug: git
- name: learning
  slug: learning
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Comment tirer depuis un dépôt Git distant
seo_desc: 'Note: This the fourth video in the Git for beginners series. Watch the
  first video here.

  When you make a change to a local repository, you can push a change to a Git remote
  repository. Likewise, when the remote gets changed, you can pull the changes ...'
---

Note : Il s'agit de la quatrième vidéo de la série Git pour débutants. [Regardez la première vidéo ici](https://zellwk.com/blog/setting-up-git).

Lorsque vous apportez une modification à un dépôt local, vous pouvez pousser une modification vers un dépôt Git distant. De même, lorsque le dépôt distant est modifié, vous pouvez tirer les modifications vers votre dépôt local.

Aujourd'hui, vous apprendrez à tirer depuis le dépôt distant vers votre dépôt.

### Apporter une modification au dépôt distant

Habituellement, une autre personne travaillant sur le même projet apporte une modification au dépôt distant. Elle modifie le code sur son ordinateur et le pousse vers le dépôt distant.

Une fois le dépôt distant modifié, vous pouvez tirer les modifications vers votre dépôt local pour obtenir la version mise à jour.

C'est le flux de travail standard.

Mais, puisque je travaille seul sur le projet, je vais vous montrer comment modifier directement le dépôt distant sur GitHub. Une fois terminé, nous tirerons depuis là-bas.

### Modifier directement le dépôt GitHub

Supposons que nous voulons modifier le texte du fichier `README.md`.

Pour ce faire, vous pouvez cliquer sur l'icône de crayon à côté du fichier Readme. Cela vous amène à un éditeur où vous pouvez modifier le texte.

![Image](https://cdn-media-1.freecodecamp.org/images/0*3MKmgO4C_GLI_of0.png)

Une fois terminé, faites défiler vers le bas et écrivez un message de commit. Vous pouvez cliquer sur le bouton vert pour commiter les modifications directement sur GitHub.

![Image](https://cdn-media-1.freecodecamp.org/images/0*M48tNNP5FvJvRUcE.png)

Le projet sera mis à jour.

### Récupération des modifications

Fork et d'autres clients Git peuvent vous montrer les modifications apportées à un dépôt distant. Ils le font via une commande appelée Git Fetch.

Vous pouvez effectuer un Fetch vous-même en cliquant sur la flèche vide pointant vers le bas. C'est le bouton de flèche le plus à gauche dans le coin supérieur gauche.

![Image](https://cdn-media-1.freecodecamp.org/images/0*b7PHmWflcH2u27tT.png)

Fetch vérifie le dépôt distant pour toute modification. C'est comme un client de messagerie qui vous dit que vous avez trois emails à lire.

Une fois le Fetch terminé, vous pouvez voir dans l'historique Git que `origin/master` est sur le commit `update README.md`. Le commit `update README.md` est un commit en avance sur notre branche locale master.

![Image](https://cdn-media-1.freecodecamp.org/images/0*ewPdamyyxzHQqcl8.png)

Dans la barre latérale, vous pouvez voir le nombre 1 à côté de notre branche master, et une flèche pointant vers le bas. Cela nous indique que notre branche est un commit derrière le dépôt distant.

### Tirer les modifications

Pour mettre à jour votre branche locale, vous pouvez cliquer sur le bouton de pull. Le bouton de pull est la flèche pointant vers le bas remplie dans le coin supérieur gauche. C'est celle entre Fetch et Push.

![Image](https://cdn-media-1.freecodecamp.org/images/0*d3YLHKVBJVh3OwQp.png)

Lorsque vous cliquez sur Pull, vous pourrez sélectionner la branche que vous souhaitez tirer. Puisque nous l'avons suivie précédemment, vous pouvez tirer la branche master directement en cliquant à nouveau sur pull.

Lorsque vous tirez la branche depuis le dépôt distant vers votre dépôt local, vous verrez que `master` se déplace vers le même commit que `origin/master`.

![Image](https://cdn-media-1.freecodecamp.org/images/0*O463L1K2aqiZ685A.png)

### Conclusion

Fetch vérifie s'il y a des modifications dans le dépôt distant.

Pull apporte les modifications du dépôt distant vers votre dépôt local.

Merci d'avoir lu. Cet article vous a-t-il aidé d'une manière ou d'une autre ? Si c'est le cas, [j'espère que vous envisagerez de le partager](http://twitter.com/share?text=Pulling%20from%20a%20Git%20remote%20by%20@zellwk%20?%20&url=https://zellwk.com/blog/pulling-from-a-git-remote/&hashtags=). Vous pourriez aider quelqu'un. Merci !

Cet article a été initialement publié sur [mon blog](https://zellwk.com/blog/pulling-from-a-git-remote/). Inscrivez-vous à ma [newsletter](https://zellwk.com/) si vous voulez plus d'articles pour vous aider à devenir un meilleur développeur front-end.