---
title: Qu'est-ce qu'une branche dans Git et comment l'utiliser ?
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2018-09-26T06:00:03.000Z'
originalURL: https://freecodecamp.org/news/what-is-a-branch-in-git-9bcd1a760ed3
coverImage: https://cdn-media-1.freecodecamp.org/images/0*75JvMnZTqmxkoVyw.png
tags:
- name: Git
  slug: git
- name: General Programming
  slug: programming
- name: remote-working
  slug: remote-working
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Qu'est-ce qu'une branche dans Git et comment l'utiliser ?
seo_desc: 'Note: This the seventh video in the Git for beginners series. Watch the
  first video here.

  Imagine there are parallel worlds. We have:


  a world where I have created this video, and you’re watching it

  a world where I have created this video, but you’re...'
---

Note : Il s'agit de la septième vidéo de la série Git pour débutants. [Regardez la première vidéo ici](https://zellwk.com/blog/setting-up-git).

Imaginez qu'il existe des mondes parallèles. Nous avons :

1. un monde où j'ai créé cette vidéo et vous la regardez
2. un monde où j'ai créé cette vidéo mais vous ne la regardez pas
3. un monde où je n'ai pas créé cette vidéo.

Dans ce concept de mondes parallèles, une branche Git est un monde parallèle.

Vous pouvez avoir une branche qui reste la même dans un monde. Ensuite, vous pouvez créer une nouvelle branche dans un autre monde. Une fois que vous avez terminé votre code, vous pouvez compléter le monde initial en fusionnant les changements.

### Comment créer une branche

Ouvrez votre client Git. Recherchez la branche à partir de laquelle vous souhaitez créer une nouvelle branche. Faites un clic droit dessus et sélectionnez "Créer une nouvelle branche".

![Image](https://cdn-media-1.freecodecamp.org/images/0*erKqmaDSa5ITj3Ev.png)

Vous pouvez nommer votre branche comme vous le souhaitez.

Généralement, la première branche que nous, les développeurs, utilisons est la branche de développement.

Une fois que vous avez nommé votre branche, cliquez sur "Créer et basculer". Basculer, dans ce cas, signifie passer à la branche de développement.

![Image](https://cdn-media-1.freecodecamp.org/images/0*mnhkSlA2Vv6VJKi9.png)

Une fois que vous avez créé la branche de développement, vous pouvez voir deux branches dans votre section de branches — master et development.

![Image](https://cdn-media-1.freecodecamp.org/images/0*75JvMnZTqmxkoVyw.png)

Dans l'historique Git, vous pouvez également voir une nouvelle étiquette appelée `development`. Cette étiquette `development` est sur le même commit que `master` et `origin/master`.

![Image](https://cdn-media-1.freecodecamp.org/images/0*SkdqylHFVPzfUvQy.png)

### Pourquoi créer une branche de développement ?

Supposons que vous avez un site web prêt à être vu par les gens. Ce site web est sur la branche master.

Si vous commitez du code sur la branche master, cela signifie que vous modifiez directement le site web. Si vous introduisez des bugs, d'autres personnes peuvent voir vos bugs immédiatement.

Nous sommes humains. Nous faisons des erreurs. Nous ne voulons pas montrer nos erreurs aux gens.

Nous créons donc une nouvelle branche et travaillons dessus. Lorsque nous avons terminé et que nous sommes sûrs qu'il n'y a plus de bugs — au moins nous essayons de nous en assurer ! — nous poussons les changements vers la branche master pour mettre à jour le site web.

C'est pourquoi nous utilisons une branche de développement.

Dans ce cas, la branche master peut également être appelée une branche de production.

### Comment coder sur une nouvelle branche

Lorsque vous créez une nouvelle branche, vous pouvez coder directement sur la branche elle-même. Tout code que vous modifiez ne sera reflété que sur cette branche.

Supposons que nous voulons créer un nouveau fichier appelé `development.md`. Dans ce fichier, nous écrivons "Bonjour ! Ceci est commit depuis la branche de développement !".

```
# development.md Bonjour ! Ceci est commit depuis la branche de développement !
```

Si vous retournez à votre client Git, vous pouvez commiter ce changement sur la branche de développement.

Assurez-vous d'être sur la branche de développement lorsque vous créez le commit. Dans Fork, vous pouvez savoir sur quelle branche vous vous trouvez en regardant la **branche en gras**.

![Image](https://cdn-media-1.freecodecamp.org/images/0*-7t_HDNPrLgU0Q9A.png)

Commitez votre code sur la branche de développement.

Maintenant, si vous regardez l'historique Git, vous pouvez voir que la branche de développement est d'un commit en avance sur la branche `origin/master` et la branche locale `master`.

Cela montre que nous pouvons coder autant que nous le souhaitons sur la branche `development` sans affecter les autres branches.

![Image](https://cdn-media-1.freecodecamp.org/images/0*ANi2i1wEVkn5uN4v.png)

### Pousser la branche de développement vers le dépôt distant Git

Vous pouvez pousser la branche de développement vers le dépôt distant Git en cliquant sur le bouton de poussée. Les étapes seront [similaires à celles lorsque vous avez poussé la branche master pour la première fois](https://zellwk.com/blog/pushing-to-a-git-remote).

Une fois la poussée terminée, vous pouvez voir l'étiquette `origin/development` sur le même commit que l'étiquette `development`.

![Image](https://cdn-media-1.freecodecamp.org/images/0*Hj5uSJjsHF2K0piB.png)

### Basculer entre les branches

Pour basculer entre les branches, vous pouvez double-cliquer sur la branche souhaitée dans la barre latérale. Si vous double-cliquez sur master, vous basculerez vers master.

**Basculer** signifie passer à la branche que vous avez choisie.

![Image](https://cdn-media-1.freecodecamp.org/images/0*Sh3g1YpxaAKssUSz.png)

Si vous regardez votre projet maintenant, vous remarquerez que le fichier `development.md` est manquant. Cela prouve, une fois de plus, que vous pouvez faire autant de commits que nécessaire sur votre branche `development` sans affecter les autres branches.

### Fusionner les branches

Vous avez terminé le processus de développement et vous êtes prêt à fusionner la branche dans `master`.

Pour fusionner, vous devez d'abord basculer vers la branche dans laquelle vous souhaitez fusionner. Cela devrait être `master`.

Ensuite, pour fusionner la branche `development` dans la branche `master`, vous faites un clic droit sur la branche `development` dans votre client Git et sélectionnez "Fusionner dans 'master'".

![Image](https://cdn-media-1.freecodecamp.org/images/0*THzXij82TmuqZjjO.png)

Fork vous demandera si vous souhaitez créer un commit de fusion. Certains clients le font automatiquement pour vous.

![Image](https://cdn-media-1.freecodecamp.org/images/0*wHSnEBBUyGHy39mp.png)

Sélectionnez "Fusionner" et la fusion sera terminée.

Si vous regardez l'historique Git maintenant, vous verrez que la branche `master` est en avance sur les branches `development` et `origin/development`.

C'est parce que nous avons fait un commit de fusion.

![Image](https://cdn-media-1.freecodecamp.org/images/0*bOjQredUMUFU1v9v.png)

En même temps, `master` est de deux commits en avance sur la branche `origin/master`. C'est pourquoi nous voyons 2 up dans la barre latérale.

![Image](https://cdn-media-1.freecodecamp.org/images/0*qhRL2gS-kyG5EtpJ.png)

Lorsque vous avez terminé la fusion, vous pouvez mettre à jour le dépôt distant Git en cliquant sur le bouton Pousser.

![Image](https://cdn-media-1.freecodecamp.org/images/0*sYeFkUaexUEhi9aM.png)

### Supprimer une branche

Pour supprimer une branche, vous faites un clic droit sur la branche que vous souhaitez supprimer et sélectionnez "Supprimer '[nom-de-la-branche]'".

![Image](https://cdn-media-1.freecodecamp.org/images/0*FLrlNZj77MnT2nhN.png)

Dans Fork, vous pouvez également choisir de supprimer la branche du dépôt distant.

![Image](https://cdn-media-1.freecodecamp.org/images/0*jOh1ZHYKpeVNwxaj.png)

Cliquez sur "Supprimer" et Fork supprimera les deux branches.

Une fois la suppression terminée, vous pouvez regarder l'historique Git. Vous remarquerez que les étiquettes `origin/development` et `development` ont toutes deux disparu de l'historique.

![Image](https://cdn-media-1.freecodecamp.org/images/0*Yg8dO6nZQkaVyo0J.png)

### Conclusion

Une branche est comme un monde parallèle où vous pouvez créer des commits sans introduire de bugs dans le code de production. Vous pouvez toujours corriger les bugs avant de fusionner votre branche dans le code de production.

Merci d'avoir lu. Cet article vous a-t-il aidé d'une manière ou d'une autre ? Si c'est le cas, [j'espère que vous envisagerez de le partager](http://twitter.com/share?text=Qu'est-ce%20qu'une%20branche%20dans%20Git%3F%20par%20@zellwk%20?%20&url=https://zellwk.com/blog/git-branch/&hashtags=). Vous pourriez aider quelqu'un. Merci !

Cet article a été initialement publié sur [mon blog](https://zellwk.com/blog/git-branch).

Inscrivez-vous à ma [newsletter](https://zellwk.com/) si vous voulez plus d'articles pour vous aider à devenir un meilleur développeur frontend.