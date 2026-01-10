---
title: Comment pousser vers un dépôt Git distant
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2018-08-28T14:44:21.000Z'
originalURL: https://freecodecamp.org/news/how-to-push-to-a-git-remote-repository-570d2712b62f
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9caaa9740569d1a4ca8c63.jpg
tags:
- name: Git
  slug: git
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
seo_title: Comment pousser vers un dépôt Git distant
seo_desc: 'Note: This the third video in the Git for beginners series. Watch the first
  video here.

  In Git terminology, we call the Git repository on your computer a local repository.

  A Git remote is the same repository stored somewhere else on the internet. It ...'
---

Note : Il s'agit de la troisième vidéo de la série Git pour débutants. [Regardez la première vidéo ici](https://zellwk.com/blog/setting-up-git).

En terminologie Git, nous appelons le dépôt Git sur votre ordinateur un dépôt local.

Un dépôt distant Git est le même dépôt stocké ailleurs sur Internet. Il peut servir de sauvegarde. Si votre ordinateur tombe en panne, vous pouvez toujours récupérer la dernière version du dépôt distant sur votre ordinateur.

Avant de parler des dépôts distants Git, nous devons parler des différents services qui vous fournissent des dépôts distants Git. Examinons quelques exemples.

### Différences entre les services Git

Il n'y a pas de différences entre ces trois services en ce qui concerne Git lui-même.

Les seules différences entre les services sont leur popularité, leur interface web et leur tarification.

De nombreuses personnes aiment utiliser Github car Github est le plus populaire des trois. C'est aussi pourquoi la plupart des projets open source sont hébergés sur Github. (Note : les projets open source peuvent également être hébergés sur Bitbucket et Gitlab).

Parfois, vous pouvez vouloir créer des dépôts privés. Un dépôt privé est un dépôt Git qui ne peut être lu que par vous et les personnes à qui vous donnez la permission.

Si vous souhaitez créer des dépôts privés, vous pouvez envisager Bitbucket ou Gitlab. Ils vous permettent de créer des dépôts privés gratuitement.

Si vous souhaitez créer un dépôt privé sur Github, vous devez payer 7 $ par mois.

Cet article vous montre comment configurer un dépôt distant sur Github. Les autres services suivent les mêmes instructions.

### Création d'un dépôt sur Github

Connectez-vous à Github. Créez un compte si vous n'en avez pas déjà un.

Une fois connecté, vous verrez un bouton plus (+) dans le coin supérieur droit de la page. Cliquez sur ce bouton plus et sélectionnez "nouveau dépôt".

![Image](https://cdn-media-1.freecodecamp.org/images/0*69uxqvddbs9i7NRH.png)

Pour créer un nouveau dépôt, vous devez donner un nom à votre dépôt.

La description fournit des détails afin que d'autres personnes puissent comprendre votre projet. Elle est facultative. Vous pouvez la laisser de côté pour l'instant.

Définissez le projet comme public ou privé, selon ce que vous souhaitez.

Ensuite, ignorez le reste et cliquez sur le bouton créer un dépôt.

![Image](https://cdn-media-1.freecodecamp.org/images/0*01aK5RZDJYbGiclh.png)

Une fois que vous avez cliqué sur créer un dépôt, vous arriverez à une page avec quelques instructions Git.

![Image](https://cdn-media-1.freecodecamp.org/images/0*uZUYNOhWjfjWCfM_.png)

Ignorez ces instructions pour l'instant. Ces connaissances nécessitent l'utilisation de la ligne de commande Git. Vous allez apprendre à le faire dans quelques leçons.

Pour l'instant, nous voulons lier notre dépôt local dans Fork au dépôt distant que nous venons de créer.

Copiez l'URL que vous voyez sur la page.

Assurez-vous de sélectionner SSH (pas HTTPS !).

SSH vous permet de pousser (mettre des choses dans le dépôt distant) et de tirer (copier le dépôt distant vers votre local) sans entrer votre nom d'utilisateur et votre mot de passe Github à chaque fois. Cela facilite grandement les choses.

![Image](https://cdn-media-1.freecodecamp.org/images/0*SC3lXiMa9UMmyAHB.png)

Ensuite, ouvrez le projet dans Fork et cliquez sur le bouton Push.

Il s'agit du quatrième bouton à partir de la gauche. Il ressemble à une flèche qui monte.

![Image](https://cdn-media-1.freecodecamp.org/images/0*oljToA_B91hbkmx2.png)

Une fois que vous avez cliqué sur le bouton push, Fork vous demandera de sélectionner une branche et un dépôt distant vers lequel pousser.

Dans ce cas, notre branche sera master (parce que nous n'avons qu'une seule branche).

Nous devons ajouter le dépôt distant que nous venons de créer. Pour ajouter le dépôt distant, cliquez sur la boîte de sélection et sélectionnez ajouter un dépôt distant.

![Image](https://cdn-media-1.freecodecamp.org/images/0*cr0qHfqqCMkdzrEy.png)

Ensuite, vous devez nommer votre dépôt distant.

Le nom par défaut pour la plupart des dépôts distants sera origin. Si vous avez plusieurs dépôts distants, vous voudrez renommer le dépôt distant en fonction de leur provenance (comme Github, Heroku et Bitbucket).

L'URL du dépôt doit être l'URL que vous avez copiée depuis Github.

Sélectionnez Ajouter un nouveau dépôt distant lorsque vous avez terminé.

![Image](https://cdn-media-1.freecodecamp.org/images/0*vHRFPogrNQyrse9B.png)

### Pousser vers le dépôt distant pour la première fois

Lorsque vous poussez vos fichiers vers le dépôt distant pour la première fois, assurez-vous que la case à cocher créer une référence de suivi est cochée.

![Image](https://cdn-media-1.freecodecamp.org/images/0*AMl2y-GbAIyidZf6.png)

Une référence de suivi indique à Git de suivre la branche actuelle (master dans ce cas) et de pousser ou tirer vers la même branche sur le dépôt distant.

Si vous ne créez pas de référence de suivi, vous devrez spécifier quelle branche pousser (ou tirer) à chaque fois.

Note : si le concept de branche vous semble étranger pour l'instant, ne vous en souciez pas. Nous parlerons des branches dans une leçon ultérieure. Pour l'instant, rappelez-vous simplement que vous devez créer une référence de suivi.

Une fois que cela est coché, vous pouvez cliquer sur push et Fork poussera votre projet sur Github.

Une fois qu'il est poussé, vous pouvez regarder la section All Commits. (Dans d'autres clients Git, ce sera Git History).

Dans tous les commits, vous verrez deux tags. L'un s'appelle `master` (la branche master sur notre ordinateur). Et l'autre s'appelle `origin/master` (la branche master sur le dépôt distant nommé origin). Dans ce cas, notre origin est Github, donc `origin/master` fait référence à la branche master sur Github.

![Image](https://cdn-media-1.freecodecamp.org/images/0*0S0Dsq457t6SlO-9.png)

Lorsque ces deux tags sont sur le même commit, cela signifie que les fichiers que nous avons sur notre branche master locale sont les mêmes que les fichiers que nous avons sur la branche master de Github.

Vous pouvez vérifier que cela est vrai si vous retournez à la page où vous avez obtenu l'URL du dépôt distant Git. Actualisez cette page et vous verrez ce que vous voyez habituellement sur Github (une page de projet).

![Image](https://cdn-media-1.freecodecamp.org/images/0*kiR9rIjqnxBBq4hg.png)

Si vous regardez les fichiers, vous remarquerez que les fichiers sont exactement les mêmes que les fichiers que vous avez sur votre ordinateur.

### Pousser pour la deuxième fois

Les poussées suivantes sont beaucoup plus faciles.

Supposons que nous apportons une modification à notre dépôt. Cette fois, nous voulons créer un fichier `README.md`. Un fichier `README.md` apparaît sur la page du projet Git et aide les gens à comprendre de quoi il s'agit.

Vous voulez créer un fichier `README.md` pour chaque dépôt que vous créez.

Une fois que nous avons créé le fichier, nous verrons les changements dans Fork si nous cliquons sur l'onglet des changements.

[Comme avant](https://zellwk.com/blog/your-first-commit), nous voulons indexer le fichier et commiter le fichier. Dans ce cas, le message de commit peut être "Créer Readme.md".

Lorsque vous créez un nouveau commit, regardez la barre latérale à gauche. Vous verrez un nombre, un, et une flèche qui pointe vers le haut à côté de la branche master.

![Image](https://cdn-media-1.freecodecamp.org/images/0*wZztYXfAnZM1KITC.png)

Cela nous indique que notre branche master est d'un commit en avance sur la branche distante. Cela signifie que notre branche master est plus à jour par rapport à la branche distante.

Si vous regardez l'historique Git, vous pouvez voir le commit "Créer readme.md" sur la branche locale, mais ce commit n'a pas encore atteint le dépôt distant.

![Image](https://cdn-media-1.freecodecamp.org/images/0*B0ZYzQJcGSoDMaNo.png)

Pour pousser le nouveau commit vers le dépôt distant, vous devez cliquer à nouveau sur le bouton push.

Ensuite, cliquez à nouveau sur push.

C'est tout.

![Image](https://cdn-media-1.freecodecamp.org/images/0*EK2x4xVrKuKBODdO.png)

Une fois le commit poussé vers la branche distante, vous pouvez voir que le tag `origin/master` est déplacé vers le même commit que le tag `master`.

![Image](https://cdn-media-1.freecodecamp.org/images/0*PtvF1NJoo_nk48DN.png)

Pour prouver que cela fonctionne, vous pouvez actualiser la page du dépôt Github et vous pourrez voir votre nouveau fichier `README.md` !

### Conclusion

Un dépôt distant Git est une sorte de sauvegarde qui est stockée sur l'ordinateur de quelqu'un d'autre. Pour créer un dépôt distant Git, vous pouvez utiliser l'un des services populaires comme Github, Bitbucket et Gitlab.

Créez un dépôt distant, puis liez votre dépôt local au dépôt distant. Lorsque vous les liez, vous pouvez pousser vers le dépôt distant.

Merci d'avoir lu. Cet article vous a-t-il aidé d'une manière ou d'une autre ? Si c'est le cas, [j'espère que vous envisagerez de le partager](http://twitter.com/share?text=Pushing%20to%20a%20Git%20remote%20by%20@zellwk%20?%20&url=https://zellwk.com/blog/pushing-to-a-git-remote/&hashtags=); vous pourriez aider quelqu'un qui se sentait comme vous avant de lire l'article. Merci.

Cet article a été initialement publié sur [mon blog](https://zellwk.com/blog/pushing-to-a-git-remote/).
Inscrivez-vous à ma [newsletter](https://zellwk.com/) si vous voulez plus d'articles pour vous aider à devenir un meilleur développeur front-end.