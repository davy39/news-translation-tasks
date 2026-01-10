---
title: Comment résoudre les conflits Git
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2018-09-18T22:12:17.000Z'
originalURL: https://freecodecamp.org/news/resolving-git-conflicts-62bd357ed5f
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca9e5740569d1a4ca877a.jpg
tags:
- name: coding
  slug: coding
- name: Git
  slug: git
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Comment résoudre les conflits Git
seo_desc: 'Note: This the sixth video in the Git for beginners series. Watch the first
  video here.

  Let’s say a friend of made a change to your repository and pushed the changes to
  the Git remote. At the same time, you also made a change to the same line of code...'
---

Note : Il s'agit de la sixième vidéo de la série Git pour débutants. [Regardez la première vidéo ici](https://zellwk.com/blog/setting-up-git).

Disons qu'un ami a apporté une modification à votre dépôt et a poussé les changements vers le dépôt distant Git. En même temps, vous avez également modifié la même ligne de code.

Lorsque vous tirez leurs changements dans votre dépôt local, vous remarquerez qu'il y a un conflit.

Cela se produit parce que Git ne sait pas si la version de votre ami est la version mise à jour ou si votre version est la version mise à jour.

C'est ce que nous appelons un conflit Git.

Vous apprendrez aujourd'hui comment résoudre un conflit Git.

Tout d'abord, produisons un conflit Git pour que vous voyiez ce qui se passe.

### Produire un conflit

Pour produire un conflit Git, nous avons besoin de deux ensembles de code. Pour le premier ensemble, nous avons besoin de quelqu'un pour pousser du code dans le dépôt distant.

Dans notre cas, nous éditons les fichiers sur GitHub pour simuler un changement.

Disons que nous changeons le texte dans `README.md` de « Hello world, this is my first Github repo » à « Hello world, this is my second Github repo ».

![Image](https://cdn-media-1.freecodecamp.org/images/0*oqp8X9DU4fbyuWD0.png)

Nous allons également créer un message de commit qui dit « Changed first to second » pour voir les effets dans notre historique Git plus tard.

![Image](https://cdn-media-1.freecodecamp.org/images/0*mqXHe049z2qbF5d_.png)

Pour le deuxième ensemble de code, vous pouvez changer le même fichier `README.md` dans votre dépôt local. Au lieu de « second Github repository », nous allons dire « third Github repository ».

```
Hello world! This is my third Github repo!
```

Nous allons commiter ce fichier et définir le message de commit à « Change first to third. »

![Image](https://cdn-media-1.freecodecamp.org/images/0*CzA0oV7JicsnHfgM.png)

Vous pouvez vérifier une mise à jour dans votre client Git avec le bouton « Fetch ». Une fois la récupération terminée, vous pouvez voir que `origin/master` est sur une fourche différente par rapport à `master`.

Cela se produit parce qu'il y a des changements sur le dépôt distant Git **et** sur notre dépôt local en même temps.

![Image](https://cdn-media-1.freecodecamp.org/images/0*Qa60g2Itzon51df_.png)

Si vous regardez la branche à gauche, vous pouvez voir que la branche master dit « one down one up ». Cela nous indique qu'il y a un commit dans le dépôt distant Git qui est **en avance** sur notre master. En même temps, notre branche master a un commit **en avance** sur le dépôt distant.

![Image](https://cdn-media-1.freecodecamp.org/images/0*1y5a6LCYSxr3XQJC.png)

Nous devons tirer nos changements sur notre branche locale pour consolider les changements. Lorsque vous tirez les changements, vous verrez un message d'erreur.

Ce message d'erreur peut être légèrement différent selon le client Git que vous utilisez. Dans Fork, il dit « Merging branch `origin/master` into `master`. Fix 1 conflict and then continue ».

![Image](https://cdn-media-1.freecodecamp.org/images/0*vBybWUmGNpYBu3Pt.png)

Ce que cela signifie, c'est que vous devez résoudre le conflit avant de continuer.

**Pour voir le conflit**, vous pouvez revenir à la section des changements. Ici, vous verrez les fichiers qui contiennent des conflits. Dans ce cas, il s'agit du fichier `README.md`.

![Image](https://cdn-media-1.freecodecamp.org/images/0*8nF6u__JbIqsDWET.png)

Tout d'abord, parlons de pourquoi vous devez fusionner.

### Pourquoi fusionner ?

Lorsque vous tirez des changements de la branche distante vers la branche locale, le changement de la branche distante est fusionné dans la branche locale.

Git nous aide à faire la fusion automatiquement s'il sait ce qui a été changé en premier, et ce qui a été changé plus tard, et s'il n'y a pas d'ambiguïtés.

Mais, lorsqu'il y a un conflit, Git ne sait pas quelle version est correcte — donc vous devez fusionner le code vous-même.

### Résoudre les conflits

La manière la plus simple de résoudre un conflit est de changer le fichier sur votre ordinateur. Si vous ouvrez `README.md` maintenant, vous verrez des lignes qui disent ceci :

```
<<<<<< HEAD Hello world! This is my third Github repo!====== Hello world! This is my second Github repo! >>>&gt;>> snt2h1s3n4tnthd9au8d3324
```

Le code entre `<<<`;<`<<`; HEAD et ======= est le code dans notre dépôt local (notre code).

Le code entre `======` et `>&g`t;>>>> est le code du dépôt distant (leur code).

Ces deux lignes de code sont en conflit. Nous devons choisir entre « second Github repo » ou « third Github repo ».

Pour résoudre le conflit, vous choisissez la ligne de code correcte. Ensuite, vous supprimez tout le reste.

Dans ce cas, disons que « third » est la version correcte. Ce que vous ferez, c'est supprimer tout le reste qui est incorrect.

```
Hello world! This is my third Github repo!
```

### Commiter la fusion

Lorsque vous retournez à Fork, vous verrez que les changements sont mis à jour. Dans notre cas, le changement est celui sur notre local, donc nous ne voyons aucun fichier qui doit être indexé.

Si le changement est différent, vous devrez indexer les fichiers.

Après l'indexation, vous devez commiter la fusion.

Si vous regardez la zone de message de commit, vous verrez que Fork a rempli un message de commit pour vous automatiquement. Vous pouvez utiliser le message de commit directement.

Cliquez sur commit pour commiter les changements.

![Image](https://cdn-media-1.freecodecamp.org/images/0*JW97OfT-V7rVz4PO.png)

Lorsque vous commitez les changements, vous verrez que la branche master dans la barre latérale dit « 2 up ». Cela signifie que notre branche locale est deux commits en avance sur le dépôt distant.

Si vous regardez l'historique Git, vous pouvez voir que la branche master distante a un lien vers la branche master locale. Cela montre une fusion.

![Image](https://cdn-media-1.freecodecamp.org/images/0*kUh2pvk7Xmi7nxzi.png)

Ce que vous devez faire ensuite, c'est pousser les changements vers le dépôt distant Git.

![Image](https://cdn-media-1.freecodecamp.org/images/0*RmOpKdzZHmVQ4YC9.png)

Et c'est **comment** vous résolvez un conflit Git.

### Empêcher les conflits de se produire

Les conflits se produisent lorsque deux personnes ou plus travaillent sur le même fichier en même temps.

Il y a deux façons d'empêcher les conflits.

La première façon est de réduire la taille de vos commits. Cela signifie que vous faites un commit pour chaque petite chose que vous faites. Les commits sont gratuits, alors faites simplement plus de commits.

Cela aide parce qu'il est facile de résoudre un petit conflit comme celui que nous venons de résoudre. Si vous rencontrez un conflit qui fait des centaines de lignes, il sera difficile à résoudre.

La deuxième façon implique des branches. Ici, différentes personnes travaillent sur le code dans différentes branches. Elles n'interagissent pas les unes avec les autres. Elles ne fusionnent le code dans la branche principale que lorsqu'elles sont prêtes.

Les branches sont légèrement plus avancées. Nous parlerons des branches et de la façon de les utiliser dans la prochaine vidéo.

Merci d'avoir lu. Cet article vous a-t-il aidé d'une manière ou d'une autre ? Si c'est le cas, [j'espère que vous envisagerez de le partager](http://twitter.com/share?text=Resolving%20Git%20conflicts%20by%20@zellwk%20?%20&url=https://zellwk.com/blog/resolving-git-conflicts/&hashtags=). Vous pourriez aider quelqu'un. Merci !

Cet article a été initialement publié sur [mon blog](https://zellwk.com/blog/resolving-git-conflicts). Inscrivez-vous à ma [newsletter](https://zellwk.com/) si vous voulez plus d'articles pour vous aider à devenir un meilleur développeur frontend.