---
title: Git sous le capot
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-07-25T19:25:49.000Z'
originalURL: https://freecodecamp.org/news/git-internals-for-curious-developers-a1e44e7ecafe
coverImage: https://cdn-media-1.freecodecamp.org/images/1*LvLuOinnwVDM5YsDMkMTIQ.jpeg
tags:
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Git sous le capot
seo_desc: 'By Wassim Chegham

  Let’s explore some common Git commands, and dive into its internals to see what
  Git does when you run them.

  But first, let’s talk about Git itself.

  What is Git?

  Put simply, Git is an open source distributed version control system. I...'
---

Par Wassim Chegham

Explorons quelques commandes Git courantes, et plongeons dans ses mécanismes internes pour voir ce que Git fait lorsque vous les exécutez.

Mais d'abord, parlons de Git lui-même.

### Qu'est-ce que Git ?

En termes simples, Git est un système de contrôle de version distribué open source. Il a été conçu par [Linus Torvalds](https://en.wikipedia.org/wiki/Linus_Torvalds), créateur du [noyau Linux](https://www.kernel.org/), pour gérer le code source du noyau. Ainsi, Git a été conçu dès le départ pour être aussi rapide et efficace que possible.

### Les principes de Git

Dans d'autres systèmes de contrôle de version tels que CVS, Subversion et ClearCase, le serveur est centralisé — il y a une séparation claire entre le serveur et les clients.

Lorsque les développeurs travaillent sur des projets utilisant ces systèmes, ils envoient d'abord une demande de "checkout" au serveur, puis récupèrent un "snapshot" de la version actuelle — généralement la plus récente. Tout le monde doit passer par le serveur central pour travailler sur le même projet, en envoyant des "commits" ou en créant des branches.

Avec Git, les choses sont différentes. Lorsque vous demandez un projet, vous le clonez localement sur votre machine.

En d'autres termes, Git copie tous les fichiers du projet sur votre disque dur, puis vous permet de travailler sur le projet de manière autonome. Toutes les opérations s'exécutent localement sur votre machine. Vous n'avez même pas besoin d'une connexion réseau, sauf pour vous synchroniser avec le code source en "poussant" ou en "tirant".

C'est ce qui rend Git si rapide.

Avec Git, vous pouvez :

* "commit" vos changements
* changer et créer des branches
* "fusionner" des branches
* récupérer un "diff" ou appliquer un "patch"
* récupérer différentes versions de n'importe quel fichier
* accéder à l'historique des changements de n'importe quel fichier

Et vous pouvez faire tout cela sans même être connecté à Internet. Incroyable, n'est-ce pas ?

### Un exemple de workflow

Prenons une application web générée avec [Yeoman](http://yeoman.io/) (ne vous inquiétez pas si vous n'êtes pas familier avec cet outil — cela n'a pas d'importance).

![Image](https://cdn-media-1.freecodecamp.org/images/j0DWw9UN8obAu6DakkUfLLVYdQIcXZEgCMI6)
_Yeoman en action_

Une fois que Yeoman a généré l'application, créant sa structure arborescente de fichiers, exécutez _git status_. Git répondra que le répertoire actuel n'est pas un dépôt Git :

![Image](https://cdn-media-1.freecodecamp.org/images/GybefwYV9he8FSMjirrh7Muhqaid081HsxBF)
_N'est pas un dépôt git_

Vous devez donc exécuter la commande _git init_ dans le répertoire racine afin d'initialiser un dépôt Git.

![Image](https://cdn-media-1.freecodecamp.org/images/OS8xRyAK3yeO6c6g9sVb7-jEEPB0gW04sw5I)
_git init_

Comme vous pouvez le voir sur la capture d'écran, nous avons créé un dépôt Git vide, et nous sommes actuellement sur sa branche principale — généralement appelée "master".

Vous pouvez également remarquer que Git crée un dossier _.git_ à la racine du dépôt. Ce répertoire caché est la base de données de Git. Si vous souhaitez faire une sauvegarde de votre projet, il vous suffit de faire un _tar.gz_ (ou _zip_) de ce répertoire.

Exécutons _git status_ pour voir notre statut :

![Image](https://cdn-media-1.freecodecamp.org/images/WQm8-07YIYWm0BsXdPaHDAePGdQ2yucxpfMS)
_git status_

Git nous dit que nous n'avons rien ajouté à notre commit pour l'instant. Ajoutons donc le contenu du répertoire actuel avec la commande _git add_ :

![Image](https://cdn-media-1.freecodecamp.org/images/AWlU5kabU439BpjN7wEskkW7lqH0mFm9OCKc)
_git add_

Avant de commiter vos changements, vous devriez vérifier ce que vous êtes sur le point de commiter. Pour cela, exécutez _git diff_ :

![Image](https://cdn-media-1.freecodecamp.org/images/g1elieXPk1VJXp1tqJ-Cq-pLn0oebGJm5hnP)
_git diff_

Git nous dit que nous avons des changements en attente de commit. Commitons-les en utilisant la commande _git commit -m "first commit"_ :

![Image](https://cdn-media-1.freecodecamp.org/images/8ofJt94-UpG-aBvhB-lK0KCoki65yHa8Xhbb)
_git commit_

Maintenant, voyons comment Git nous permet de travailler sur différentes fonctionnalités en même temps en utilisant plusieurs branches.

Pour illustrer cela, nous allons ouvrir un autre terminal dans le même répertoire, et exécuter notre application :

![Image](https://cdn-media-1.freecodecamp.org/images/WJligtsMG7jrhLklOBn20k1clbseMwZDPj0z)
_notre application web_

Pour créer une nouvelle branche dans Git, nous utilisons le verbe "checkout" (avec le flag -b) :

![Image](https://cdn-media-1.freecodecamp.org/images/9eodxsZTNS7XiOVPBxVTsvFvSjBbwUZrtNOj)
_git checkout -b branch_A_

Nous venons donc de créer une nouvelle branche appelée "branch_A" et avons changé le contexte de travail actuel de la branche "master" à la branche "branch_A".

Tout changement que nous apportons n'affectera que la branche actuelle. Apportons quelques modifications à la page d'accueil de notre application, comme changer la couleur de fond :

![Image](https://cdn-media-1.freecodecamp.org/images/0TEE9qlaPIEtClpF-ZVyXkZ5jFzia7A3Hs5V)
_changement de la couleur de fond de la page d'accueil_

En exécutant _git status_, nous remarquons que nous avons quelques changements en attente :

![Image](https://cdn-media-1.freecodecamp.org/images/zgonRQOs3oiAzfPqmXKunjLsPNaRUW-JvTnb)
_git status_

Ajoutons ce fichier modifié et commitons :

![Image](https://cdn-media-1.freecodecamp.org/images/gEK12hnmiTsnG-GTg-2EusjySrFR7Zj850mX)
_git add . && git commit -m "yellow bg"_

En utilisant la commande _git branch_, nous pouvons voir dans quelle branche nous nous trouvons. Pour revenir à la branche "master", nous pouvons taper _git checkout master_.

![Image](https://cdn-media-1.freecodecamp.org/images/Y5QOSGozW-CcTIFwWV4ObsjSUqXraIiS9PDj)
_git checkout master_

Après avoir changé de branche, nous pouvons voir que — dans le terminal où nous avons lancé notre application — que le contenu du fichier que nous avons modifié dans la branche "branch_A" a été rechargé et remplacé par celui du fichier de la branche "master" :

![Image](https://cdn-media-1.freecodecamp.org/images/CfSBmpGO5N1-yxxpGDFz4JA-ywWdHlohX-KJ)
_le fichier a été rechargé depuis la nouvelle branche_

Veuillez noter que Git ne vous permet pas de changer de branche si vous avez des changements en attente. Donc, si vous devez vraiment changer de branche avec des changements en attente, vous pouvez d'abord demander à Git de mettre de côté ces changements pour vous, en utilisant la commande _git stash_ :

![Image](https://cdn-media-1.freecodecamp.org/images/rPjN67L5ipQ6redC8igB-kBF4qMmfa-qWkgb)
_git stash_

Vous avez ensuite la possibilité d'appliquer ces changements plus tard en utilisant :

```
$ git stash apply stash@{0}
```

Cela appliquera la première sauvegarde — parce que vous avez spécifié {0}.

Lorsque vous travaillez avec plusieurs branches, à un moment donné, vous voudrez copier tous les changements d'une branche à une autre. Heureusement, Git dispose d'une commande _git merge_ qui peut faire exactement cela. Fusionnons branch_A dans notre branche de travail actuelle, master :

![Image](https://cdn-media-1.freecodecamp.org/images/gAcMCwoVeUMcQszG7wU7GgeqIC7gaD4cH4kb)
_git merge branch_A_

La bonne nouvelle : Git vous permet de fusionner la même branche plus d'une fois. Par exemple, imaginez que vous modifiez certains fichiers dans branch_A, puis les fusionnez dans "master". Ensuite, vous modifiez à nouveau branch_A. Git ne vous empêche pas de fusionner branch_A dans master une deuxième fois.

### Maintenant, voyons comment Git fait tout cela

Supposons que notre projet contient deux fichiers : _BlogFactory.js_ et _BlogController.js_.

Lorsque nous créons notre dépôt local avec _git clone_ ou _git init_, Git initialise sa base de données et la sauvegarde dans un répertoire caché appelé _.git_ :

![Image](https://cdn-media-1.freecodecamp.org/images/fp-4CG1grHzhDlFTXSbARbAMURDqTqV9UHkn)

Si nous examinons ce dossier, nous voyons la présence de plusieurs sous-répertoires et fichiers. Les plus intéressants sont :

* **HEAD** : ce fichier contient le chemin vers la référence qui indique la branche actuelle
* **config** : le fichier de configuration du dépôt
* **objects** : ce répertoire contient tous les fichiers du dépôt, leur contenu est encodé et compressé
* **refs / heads** : ce répertoire contient un fichier par branche. Chaque fichier porte le nom d'une branche, et son contenu est le SHA1 du dernier commit (comme expliqué ci-dessous)

Lorsque vous créez ou modifiez des fichiers, vous devez exécuter :

```
$ git add BlogFactory.js BlogController.js
```

Ou :

```
$ git add . # afin d'ajouter tous les fichiers non indexés
```

Cette commande indique à Git que vous souhaitez ajouter un snapshot de vos fichiers. Git récupère donc l'état actuel du contenu de vos fichiers, calcule leurs checksums en utilisant [SHA1](https://en.wikipedia.org/wiki/SHA-1), et crée une entrée dans sa base de données. La clé de cette entrée est le hash SHA1, et sa valeur est le contenu brut du fichier.

Oui, tout le contenu !

![Image](https://cdn-media-1.freecodecamp.org/images/fwCvzAHW1PGslQfTakxkMNz-HrZB4yh0UStm)

Ensuite, comme nous l'avons dit précédemment, vous devez commiter ces changements. Pour cela, vous exécutez la commande :

```
$ git commit -m "Un message de commit très utile"
```

À ce stade, Git enregistre une sorte de "manifest" représentant toute l'arborescence de la structure des fichiers, avec chaque nom de fichier et sa clé SHA1 dans sa base de données. Ensuite, il calcule le checksum de ce manifest, basé sur son contenu. Ensuite, il lie au nouveau commit.

![Image](https://cdn-media-1.freecodecamp.org/images/3HT-VNMHp9jeZGreN4eysJ4rpWgsGDeJ1hS-)

Maintenant, imaginez que vous avez modifié le fichier _BlogController.js_, et que vous refaites un _git add_. Git effectue le même processus que précédemment. Il crée une nouvelle entrée dans sa base de données, et parce que le contenu du fichier a changé, le checksum SHA1 a également changé.

Ensuite, lorsque vous faites un _git commit_, Git recrée un nouveau manifest avec le nouveau SHA1 de l'entrée :

![Image](https://cdn-media-1.freecodecamp.org/images/HaHcfQjG207wOPALb5XzvhNaElg-fIERZYNE)

Maintenant, supposons que vous renommez votre fichier en _MyBlogController.js_, par exemple, puis commitez à nouveau vos changements. Git ne crée pas de nouvelle entrée dans la base de données puisque le contenu — et le SHA1 — n'ont pas changé :

![Image](https://cdn-media-1.freecodecamp.org/images/l3vHl5EYxldwi91y6UnWVYE0zRYvxmDC2Tba)

Voici ce qui se passe réellement dans la base de données Git :

![Image](https://cdn-media-1.freecodecamp.org/images/Z3cvbavi49cSQcBSEAbcfEvETZOos8Y4s3tL)

Git a stocké le contenu des deux fichiers commités dans le répertoire **.git/objects**. À côté de ces fichiers commités, Git sauvegarde également un fichier contenant les détails du commit, et un fichier manifest comme décrit ci-dessus.

La commande Git _cat-file -p SHA1_ est utilisée pour lire le contenu des objets stockés. Le hash SHA1 est composé des deux premiers bits du répertoire **objects/XX/** avec 38 autres bits formant le nom de l'**object objects/XX/YY..YY**. Par exemple :

```
$ git cat-file -p 987451acde8030ef93abaaff87daa617316cc7c7
```

Vous pouvez également entrer les 8 premiers bits du SHA1 (ceux-ci suffisent) :

```
$ git cat-file -p 987451ac
```

![Image](https://cdn-media-1.freecodecamp.org/images/gYqiXyucx-FMeiwRJjzwnaEtZBh9pJrdQoc8)

De même, le contenu de l'objet stockant les informations du commit ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/vvDS8YUeSd2vJMgyCcSoUq-wbgdlflkYQufb)

Comme vous pouvez le voir, le fichier objet de commit contient certaines informations liées à ce commit, y compris le SHA1 du manifest (tree), qui ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/EuEiazAuI0qT9uEA8kTp29n2Xiu4ibpHpKPP)

Ainsi, comme vous l'avez peut-être deviné, Git ne se soucie pas vraiment des noms de fichiers. Il se soucie davantage de leur contenu. Même si vous copiez un fichier, Git ne créera pas de nouvelle entrée dans sa base de données. Il s'agit simplement de contenu et de hashs SHA1.

Et si vous vous demandez : lorsque je fais un _git push_, que fait vraiment Git ? Eh bien, Git calcule le delta entre les deux fichiers, le compresse, puis l'envoie au serveur. Git n'envoie pas le contenu entier du fichier.

### Ressources

Voici quelques liens qui vous aideront à continuer votre aventure avec Git :

* [http://try.github.io/levels/1/challenges/1](http://try.github.io/levels/1/challenges/1)
* [http://git-scm.com/documentation](http://git-scm.com/documentation)
* [http://gitref.org/](http://gitref.org/)

_Suivez [@manekinekko](https://twitter.com/manekinekko) pour en apprendre davantage sur la plateforme Web._