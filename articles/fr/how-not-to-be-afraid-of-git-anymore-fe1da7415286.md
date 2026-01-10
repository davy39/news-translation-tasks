---
title: Comment ne plus avoir peur de GIT
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-13T17:24:43.000Z'
originalURL: https://freecodecamp.org/news/how-not-to-be-afraid-of-git-anymore-fe1da7415286
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca86e740569d1a4ca7de8.jpg
tags:
- name: Git
  slug: git
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment ne plus avoir peur de GIT
seo_desc: 'By Neil Kakkar

  Understanding the machinery to whittle away the uncertainty


  _Been here before? ([web comic by XKCD](https://imgs.xkcd.com/comics/git.png" rel="noopener"
  target="blank" title="))

  What is Git anyway?

  “It’s a version control system.”

  Why...'
---

Par Neil Kakkar

#### Comprendre la mécanique pour réduire l'incertitude

![Image](https://cdn-media-1.freecodecamp.org/images/2GCBfaz1YnEnmhZzKldeQe4hvhk0OnUXOOSU)
_Ça vous dit quelque chose ? ([bande dessinée web par XKCD](https://imgs.xkcd.com/comics/git.png" rel="noopener" target="_blank" title="))_

#### Qu'est-ce que Git, au fait ?

« C'est un système de contrôle de version. »

#### Pourquoi en ai-je besoin ?

« Pour le contrôle de version, bien sûr. »

D'accord, d'accord, je ne suis pas très utile pour l'instant. Voici l'idée de base : À mesure que les projets deviennent trop grands, avec trop de contributeurs, il devient impossible de suivre qui a fait quoi et quand. Quelqu'un a-t-il introduit un changement qui a tout cassé ? Comment savoir quel était ce changement ? Comment revenir à l'état précédent ? Retourner au pays des merveilles non cassé ?

Je vais aller plus loin — disons pas un projet avec de nombreux contributeurs, juste un petit projet où vous êtes le créateur, le mainteneur et le distributeur : Vous créez une nouvelle fonctionnalité pour ce projet, qui introduit des bugs subtils que vous découvrez plus tard. Vous ne vous souvenez pas des changements que vous avez apportés au code existant pour créer cette nouvelle fonctionnalité. Problème ?

La réponse à tous ces problèmes est le versioning ! Avoir des versions pour tout ce que vous avez codé vous assure de savoir qui a fait les changements, quels changements et exactement où, depuis le début du projet !

Et maintenant, je vous invite à cesser de penser à (g)it comme une boîte noire, ouvrez-la et découvrez quels trésors vous attendent. Comprenez comment Git fonctionne, et vous n'aurez plus jamais de problème à faire fonctionner les choses. Une fois que vous aurez terminé cela, je vous promets que vous réaliserez la folie de faire ce que dit la bande dessinée XKCD ci-dessus. C'est exactement ce que le versioning essaie d'empêcher.

### Comment utiliser Git ?

Je suppose que vous connaissez les commandes de base dans Git, ou que vous en avez entendu parler et que vous les avez utilisées au moins une fois. Sinon, voici un vocabulaire de base pour vous aider à commencer.

**Repository** : un endroit pour stocker des choses. Avec Git, cela signifie votre dossier de code.

**head** : Un « pointeur » vers le dernier code sur lequel vous travailliez.

**add** : Une action pour demander à Git de suivre un fichier.

**commit** : Une action pour sauvegarder l'état actuel — de sorte que l'on puisse revenir à cet état si nécessaire.

**remote** : Un repository qui n'est pas local. Peut être dans un autre dossier ou dans le cloud (par exemple : Github) : aide les autres personnes à collaborer facilement, car elles n'ont pas à obtenir une copie de votre système — elles peuvent simplement l'obtenir depuis le cloud. Assure également que vous avez une sauvegarde au cas où vous casseriez votre ordinateur portable.

**pull** : Une action pour obtenir le code mis à jour depuis le remote.

**push** : Une action pour envoyer le code mis à jour vers le remote.

**merge** : Une action pour combiner deux versions différentes de code.

**status** : Affiche des informations sur l'état actuel du repository.

#### Où utiliser Git ?

Présentation de la magie contrôlée par un dossier caché : `.git/`

Dans chaque repository git, vous verrez quelque chose comme ceci :

```
$ tree .git/
.git/
├── HEAD
├── config
├── description
├── hooks
│   ├── applypatch-msg.sample
│   ├── commit-msg.sample
│   ├── post-update.sample
│   ├── pre-applypatch.sample
│   ├── pre-commit.sample
│   ├── pre-push.sample
│   ├── pre-rebase.sample
│   ├── pre-receive.sample
│   ├── prepare-commit-msg.sample
│   └── update.sample
├── info
│   └── exclude
├── objects
│   ├── info
│   └── pack
└── refs
    ├── heads
    └── tags
8 directories, 14 files
```

C'est ainsi que Git contrôle et gère l'ensemble de votre projet. Nous allons passer en revue toutes les parties importantes, une par une.

Git se compose de 3 parties : le stockage d'objets, l'index et le répertoire de travail.

#### Le stockage d'objets

C'est ainsi que Git stocke tout en interne. Pour chaque fichier dans votre projet que vous `add`, Git génère un hash pour le fichier et stocke le fichier sous ce hash. Par exemple, si je crée maintenant un fichier `helloworld` et que je fais `git add helloworld` (ce qui indique à Git d'ajouter le fichier appelé `helloworld` au stockage d'objets git), j'obtiens quelque chose comme ceci :

```
$ tree .git/
.git/
├── HEAD
├── config
├── description
├── hooks
│   ├── applypatch-msg.sample
│   ├── commit-msg.sample
│   ├── post-update.sample
│   ├── pre-applypatch.sample
│   ├── pre-commit.sample
│   ├── pre-push.sample
│   ├── pre-rebase.sample
│   ├── pre-receive.sample
│   ├── prepare-commit-msg.sample
│   └── update.sample
├── index
├── info
│   └── exclude
├── objects
│   ├── a0
│   │   └── 423896973644771497bdc03eb99d5281615b51
│   ├── info
│   └── pack
└── refs
    ├── heads
    └── tags
9 directories, 16 files
```

Un nouvel objet a été généré ! Pour ceux qui sont intéressés à regarder sous le capot, Git utilise en interne la commande [hash-object](https://git-scm.com/docs/git-hash-object) comme ceci :

```
$ git hash-object helloworld
a0423896973644771497bdc03eb99d5281615b51
```

Oui, c'est le même hash que nous voyons sous le dossier objects. Pourquoi le sous-répertoire avec les deux premiers caractères du hash ? **Cela rend la recherche plus rapide.**

Ensuite, Git crée un objet avec le nom comme le hash ci-dessus, compresse notre fichier donné et le stocke là. Par conséquent, vous pouvez également voir le contenu de l'objet !

```
$ git cat-file a0423896973644771497bdc03eb99d5281615b51 -p
hello world!
```

C'est tout ce qui se passe sous le capot. Vous n'utiliserez jamais [cat-file](https://git-scm.com/docs/git-cat-file) dans les ajouts quotidiens. Vous ferez simplement `add`, et laisserez Git gérer le reste.

C'est notre première commande Git, faite et terminée.

`**git add**` **crée un hash, compresse le fichier et ajoute l'objet compressé au stockage d'objets.**

#### Le répertoire de travail

Comme le suggère le nom, c'est là que vous travaillez. Tous les fichiers que vous créez et modifiez sont dans le répertoire de travail. J'ai créé un nouveau fichier, `byeworld` et j'ai exécuté `git status` :

```
$ git status
On branch master
No commits yet
Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
new file:   helloworld
Untracked files:
  (use "git add <file>..." to include in what will be committed)
byeworld
```

Les fichiers non suivis sont des fichiers dans le répertoire de travail que nous n'avons pas demandés à git de gérer.

Si nous n'avions rien fait dans le répertoire de travail, nous obtiendrions le message suivant :

```
$ git status
On branch master
nothing to commit, working tree clean
```

ce que je suis sûr que vous comprenez maintenant. Ignorez la branche et le commit pour l'instant. L'essentiel est que le working tree (répertoire) est propre.

#### L'Index

C'est le cœur de Git. Également connu sous le nom de zone de staging. L'index stocke la correspondance des fichiers avec les objets dans le stockage d'objets. C'est là que les `commits` interviennent. La meilleure façon de voir cela est de l'essayer !

Faisons un commit de notre ajout du fichier `helloworld`

```
$ git commit -m "Add helloworld"
[master (root-commit) a39b9fd] Add helloworld
 1 file changed, 1 insertion(+)
 create mode 100644 helloworld
```

Retour à notre arbre :

```
$ tree .git/
.git/
├── COMMIT_EDITMSG
├── HEAD
├── config
├── description
├── hooks
│   ├── applypatch-msg.sample
│   ├── commit-msg.sample
│   ├── post-update.sample
│   ├── pre-applypatch.sample
│   ├── pre-commit.sample
│   ├── pre-push.sample
│   ├── pre-rebase.sample
│   ├── pre-receive.sample
│   ├── prepare-commit-msg.sample
│   └── update.sample
├── index
├── info
│   └── exclude
├── logs
│   ├── HEAD
│   └── refs
│       └── heads
│           └── master
├── objects
│   ├── a0
│   │   └── 423896973644771497bdc03eb99d5281615b51
│   ├── a3
│   │   └── 9b9fdd624c35eee08a36077f411e009da68c2f
│   ├── fb
│   │   └── 26ca0289762a454db2ef783c322fedfc566d38
│   ├── info
│   └── pack
└── refs
    ├── heads
    │   └── master
    └── tags
14 directories, 22 files
```

Ah, intéressant ! Nous avons 2 nouveaux objets dans notre stockage d'objets, et quelques trucs que nous ne comprenons pas encore dans les logs et refs. Retour à notre ami `cat-file` :

```
$ git cat-file a39b9fdd624c35eee08a36077f411e009da68c2f -p
tree fb26ca0289762a454db2ef783c322fedfc566d38
author = <=> 1537700068 +0100
committer = <=> 1537700068 +0100
Add helloworld
$ git cat-file fb26ca0289762a454db2ef783c322fedfc566d38 -p
100644 blob a0423896973644771497bdc03eb99d5281615b51 helloworld
```

Comme vous pouvez le deviner, le premier objet est les métadonnées du commit : qui a fait quoi et pourquoi, avec un arbre. Le deuxième objet est l'arbre réel. Si vous comprenez le système de fichiers unix, vous saurez exactement ce que c'est.

L'`arbre` dans Git correspond au système de fichiers Git. Tout est soit un arbre (répertoire) soit un blob (fichier) et avec chaque commit, Git stocke également les informations de l'arbre, pour se dire : voici à quoi devrait ressembler le répertoire de travail à ce stade. Notez que l'arbre pointe vers un objet spécifique de chaque fichier qu'il contient (le hash).

Il est temps de parler des **branches** ! Notre premier commit a également ajouté d'autres trucs à `.git/`. Notre intérêt se porte maintenant sur `.git/refs/heads/master` :

```
$ cat .git/refs/heads/master 
a39b9fdd624c35eee08a36077f411e009da68c2f
```

Voici ce que vous devez savoir sur les branches :

> Une branche dans Git est un pointeur mobile léger vers l'un de ces commits. Le nom de branche par défaut dans Git est master.

Eh, quoi ? J'aime penser aux branches comme une fourche dans votre code. Vous voulez apporter des changements, mais vous ne voulez pas tout casser. Vous décidez d'avoir une démarcation plus forte que le journal des commits, et c'est là que les branches interviennent. `master` est la branche par défaut, également utilisée comme branche de production de facto. D'où la création du fichier ci-dessus. Comme vous pouvez le deviner par le contenu du fichier, il pointe vers notre premier commit. Donc, c'est un pointeur vers un commit.

Explorons cela plus avant. Disons que je crée une nouvelle branche :

```
$ git branch the-ending
$ git branch
* master
  the-ending
```

Nous y voilà, une nouvelle branche ! Comme vous pouvez le deviner, une nouvelle entrée doit avoir été ajoutée à `.git/refs/heads/` et puisque il n'y a pas de commit supplémentaire, elle devrait pointer vers notre premier commit également, tout comme `master`.

```
$ cat .git/refs/heads/the-ending

a39b9fdd624c35eee08a36077f411e009da68c2f
```

Oui, exactement ! Maintenant, vous vous souvenez de `byeworld` ? Ce fichier était toujours non suivi, donc peu importe la branche vers laquelle vous basculez, ce fichier serait toujours là. Disons que je veux basculer vers cette branche maintenant, donc je vais `checkout` la branche, comme un [smokeshow.](https://www.urbandictionary.com/define.php?term=smokeshow)

```
$ git checkout the-ending
Switched to branch 'the-ending'
$ git branch
  master
* the-ending
```

Maintenant, sous le capot, Git changerait tout le contenu du répertoire de travail pour correspondre au contenu pointé par le commit de la branche. Pour l'instant, comme c'est exactement la même chose que master, cela ressemble à la même chose.

J'`add` et je `commit` le fichier `byeworld`.

À quoi vous attendez-vous à changer dans le dossier `objects` ?

À quoi vous attendez-vous à changer dans le dossier `refs/heads` ?

Réfléchissez à cela avant de continuer.

```
$ tree .git/
.git/
├── COMMIT_EDITMSG
├── HEAD
├── config
├── description
├── hooks
│   ├── applypatch-msg.sample
│   ├── commit-msg.sample
│   ├── post-update.sample
│   ├── pre-applypatch.sample
│   ├── pre-commit.sample
│   ├── pre-push.sample
│   ├── pre-rebase.sample
│   ├── pre-receive.sample
│   ├── prepare-commit-msg.sample
│   └── update.sample
├── index
├── info
│   └── exclude
├── logs
│   ├── HEAD
│   └── refs
│       └── heads
│           ├── master
│           └── the-ending
├── objects
│   ├── 0b
│   │   └── 17be9dbc34c5a5fbb0b94d57680968efd035ca
│   ├── a0
│   │   └── 423896973644771497bdc03eb99d5281615b51
│   ├── a3
│   │   └── 9b9fdd624c35eee08a36077f411e009da68c2f
│   ├── b3
│   │   └── 00387d818adbbd6e7cc14945fdf4c895de6376
│   ├── d1
│   │   └── 8affe001488123b496ceb34d8b13b120ab4cb6
│   ├── fb
│   │   └── 26ca0289762a454db2ef783c322fedfc566d38
│   ├── info
│   └── pack
└── refs
    ├── heads
    │   ├── master
    │   └── the-ending
    └── tags
17 directories, 27 files
```

3 nouveaux objets — 1 pour add, 2 pour commit ! Cela a-t-il du sens ? Que pensez-vous que les objets contiennent ?

* Métadonnées du commit
* Contenu de l'objet `add`
* Description de l'arbre

La dernière partie de l'image est : comment ces métadonnées de commit fonctionnent-elles avec les métadonnées de commit précédentes. Eh bien, `cat-file` !

```
$ git cat-file 0b17be9dbc34c5a5fbb0b94d57680968efd035ca -p
100644 blob d18affe001488123b496ceb34d8b13b120ab4cb6 byeworld
100644 blob a0423896973644771497bdc03eb99d5281615b51 helloworld
$ git cat-file b300387d818adbbd6e7cc14945fdf4c895de6376 -p
tree 0b17be9dbc34c5a5fbb0b94d57680968efd035ca
parent a39b9fdd624c35eee08a36077f411e009da68c2f
author = <=> 1537770989 +0100
committer = <=> 1537770989 +0100
add byeworld
$ git cat-file d18affe001488123b496ceb34d8b13b120ab4cb6 -p
Bye world!
$ cat .git/refs/heads/the-ending 
b300387d818adbbd6e7cc14945fdf4c895de6376
```

Le voyez-vous en gras ? Le pointeur parent ! Et c'est exactement comme vous y pensiez — une liste liée, reliant les commits ensemble !

Et voyez-vous l'implémentation de la branche ? Elle pointe vers un commit, le dernier que nous avons fait après le checkout ! Bien sûr, le master devrait toujours pointer vers le commit helloworld, n'est-ce pas ?

```
$ cat .git/refs/heads/master

a39b9fdd624c35eee08a36077f411e009da68c2f
```

D'accord, nous avons parcouru beaucoup de choses, résumons jusqu'ici.

### TL;DR

Git fonctionne avec des objets — des versions compressées des fichiers que vous demandez à Git de suivre.

Chaque objet a un ID (un hash généré par Git basé sur le contenu du fichier).

Chaque fois que vous `add` un fichier, Git ajoute un nouvel objet au stockage d'objets. **C'est exactement pourquoi vous ne pouvez pas gérer de très grands fichiers dans Git** — il stocke le fichier entier chaque fois que vous `add` des changements, pas le diff (contrairement à la croyance populaire).

Chaque commit crée 2 objets :

1. **L'arbre** : Un ID pour l'arbre, qui agit exactement comme un répertoire unix : il pointe vers d'autres arbres (répertoires) ou blobs (fichiers) : Cela construit toute la structure de répertoire basée sur les objets présents à ce moment-là. Les blobs sont représentés par les objets actuels créés par `add`.
2. **Les métadonnées du commit** : Un ID pour le commit, qui a fait le commit, un arbre qui représente le commit, le message du commit et le commit parent. Forme une structure de liste liée reliant les commits ensemble.

Les branches sont des pointeurs vers des objets de métadonnées de commit, tous stockés dans `.git/refs/heads`

C'est tout pour la compréhension des coulisses ! [Dans la prochaine partie](https://medium.freecodecamp.org/now-that-youre-not-afraid-of-git-anymore-here-s-how-to-leverage-what-you-know-11e710c7f37b), nous passerons en revue certaines des actions Git qui donnent des cauchemars aux gens :

`reset, merge, pull, push, fetch` et comment elles modifient la structure interne dans `.git/`.

Autres histoires de cette série :

* [Comment ne plus avoir peur de Vim](https://medium.freecodecamp.org/how-not-to-be-afraid-of-vim-anymore-ec0b7264b0ae)
* [Comment ne plus avoir peur de Python](https://medium.freecodecamp.org/how-not-to-be-afraid-of-python-anymore-b37b58871795)

Vous avez aimé cela ? [Ne manquez plus un article — abonnez-vous à ma liste de diffusion !](http://neilkakkar.com/subscribe/)