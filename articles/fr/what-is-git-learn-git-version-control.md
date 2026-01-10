---
title: Qu'est-ce que Git ? Un guide pour débutants sur le contrôle de version avec
  Git
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-17T17:07:46.000Z'
originalURL: https://freecodecamp.org/news/what-is-git-learn-git-version-control
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/Artboard-2.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: version control
  slug: version-control
seo_title: Qu'est-ce que Git ? Un guide pour débutants sur le contrôle de version
  avec Git
seo_desc: 'By Anna Skoulikari

  Git is a version control system that developers use all over the world. It helps
  you track different versions of your code and collaborate with other developers.

  If you are working on a project over time, you may want to keep track...'
---

Par Anna Skoulikari

Git est un système de contrôle de version utilisé par les développeurs du monde entier. Il vous aide à suivre les différentes versions de votre code et à collaborer avec d'autres développeurs.

Si vous travaillez sur un projet sur une période donnée, vous voudrez peut-être garder une trace des modifications apportées, par qui et quand ces modifications ont été faites. Cela devient de plus en plus important si vous avez un bug dans votre code ! Git peut vous aider avec cela.

Mais Git peut aussi être un peu effrayant et déroutant lorsque vous commencez à l'apprendre, alors dans cet article, je vais présenter Git de manière compréhensible. Nous aborderons des sujets tels que les dépôts, les commits, les branches et bien plus encore, alors commençons !

Voici ce que nous allons couvrir dans cet article :

* Qu'est-ce que Git ?
* Qu'est-ce que GitHub ?
* Comment commencer à utiliser Git
* Comment Git suit-il les changements ?
* Un flux de travail typique avec Git
* Cours en ligne pour apprendre le contrôle de version avec Git

## Qu'est-ce que Git ?

**Git** est un système de contrôle de version que vous téléchargez sur votre ordinateur. Il est essentiel d'utiliser Git si vous souhaitez collaborer avec d'autres développeurs sur un projet de codage ou travailler sur votre propre projet.

Pour vérifier si vous avez déjà Git installé sur votre ordinateur, vous pouvez taper la commande `git --version` dans le terminal.

Si vous avez déjà Git installé, vous verrez quelle version vous avez. Si vous n'avez pas Git installé, vous pouvez visiter le [site web de Git](https://git-scm.com/) et suivre facilement les instructions de téléchargement pour installer la version correcte pour votre système d'exploitation.

## Qu'est-ce que GitHub ?

**GitHub** est un produit qui vous permet d'héberger vos projets Git sur un serveur distant (ou en d'autres termes, dans le cloud).

Il est important de se rappeler que GitHub n'est pas Git. GitHub est simplement un service d'hébergement. Il existe d'autres entreprises qui offrent des services d'hébergement qui font la même chose que GitHub, comme Bitbucket et GitLab.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/1_JL0fpMQTlDNbyQ5GlLdA_g.png)
_La différence entre GitHub et Git_

## Comment commencer avec Git

### Terminal vs GUI

Vous pouvez utiliser Git soit en tapant des commandes dans le terminal, soit en utilisant une interface graphique (GUI) telle que Sourcetree ou GitKraken.

Si vous choisissez le terminal, vous devrez rechercher les commandes Git dont vous aurez besoin.

Heureusement, vous n'avez pas à les apprendre par cœur. En plus d'une poignée de commandes que vous utiliserez le plus souvent, vous pouvez rechercher le reste chaque fois que vous en avez besoin (c'est ce que font la plupart des développeurs, même ceux avec des décennies d'expérience). Git offre une [documentation approfondie sur leur site web](https://git-scm.com/docs).

Si vous choisissez d'utiliser une GUI, alors les différentes actions que vous devez entreprendre seront affichées de manière plus visuelle.

Que vous choisissiez d'utiliser le terminal ou une GUI, vous devrez comprendre les bases du fonctionnement de Git pour l'utiliser en toute confiance.

Pour le reste de cet article, nous partagerons des exemples en utilisant Git dans le terminal. Mais les étapes que nous partageons sont très similaires si vous utilisez une GUI.

### Comment préparer votre dossier de projet dans Git

Pour utiliser Git, nous devons avoir un projet que nous voulons versionner. Cela peut être un nouveau projet ou un projet existant.

Si c'est un nouveau projet, alors nous devons créer un nouveau dossier de projet (indice : nous pouvons utiliser la commande `mkdir`) et ensuite naviguer dans ce dossier de projet dans le terminal.

Si nous choisissons un projet existant, nous naviguons simplement dans ce dossier de projet dans le terminal.

Dans notre exemple, nous allons créer un nouveau dossier de projet appelé `novel`.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/1_GwzrUZNrMWv_MfZaoudhIg.png)
_Création de notre dossier de projet_

### Comment créer un dépôt Git

Une fois que nous sommes dans notre dossier de projet, pour commencer à utiliser Git, nous devons créer (ou initialiser) un dépôt en utilisant la commande `git init`.

Une fois que nous exécutons la commande en la tapant dans le terminal et en appuyant sur entrée, il semblera probablement que rien ne s'est passé. Mais ne vous y trompez pas, Git peut être sournois parfois et il effectue beaucoup d'actions en arrière-plan.

Pour voir ce que Git a fait en arrière-plan, nous devons afficher nos fichiers cachés. Assurez-vous d'ouvrir votre dossier de projet dans votre système de fichiers. Ensuite, si vous êtes sur un mac, vous pouvez sélectionner **Command** + **Shift** + **Point** pour voir les fichiers cachés dans votre système de fichiers. Si vous êtes sur un système d'exploitation Windows, vous pouvez changer vos paramètres de vue pour afficher les fichiers cachés dans votre système de fichiers.

Pour afficher les fichiers cachés dans le terminal, nous pouvons utiliser la commande `ls -a`.

Ce que nous devrions voir maintenant est un dossier `.git` à l'intérieur de notre dossier de projet. C'est généralement ce qui représente notre dépôt.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/1_fUAS61mZR44MwNeWRpnm2w.png)
_Création de notre dépôt_

### Qu'est-ce qu'un dépôt Git ?

Le **dépôt** est le dossier `.git` à l'intérieur de notre dossier de projet. Il suivra toutes les modifications apportées aux fichiers de notre projet et enregistrera cet historique au fil du temps.

Le dépôt que nous avons sur notre ordinateur est appelé le **dépôt local**.

Plus tôt, nous avons mentionné des services d'hébergement tels que GitHub, GitLab et Bitbucket. Lorsque nous poussons (en d'autres termes, téléchargeons) notre dépôt local vers l'un de ces services, alors le dépôt qui réside dans ces services dans le cloud est appelé le **dépôt distant**.

Il est important d'utiliser un dépôt distant afin de pouvoir collaborer avec d'autres personnes ainsi que de sauvegarder nos projets au cas où quelque chose arriverait à notre ordinateur portable ou à notre ordinateur.

### Comment collaborer avec d'autres développeurs en utilisant Git

Si un autre développeur souhaite collaborer avec nous sur notre projet, il peut cloner (ou en d'autres termes, télécharger) le dépôt distant depuis le service d'hébergement où vous l'avez téléchargé sur son ordinateur.

Cela leur permet d'avoir le projet sur leur ordinateur également. Le projet sur leur ordinateur est alors également appelé un dépôt local.

Dans un projet avec plusieurs développeurs, chacun a un dépôt local sur son ordinateur. Et il y a un dépôt distant auquel ils contribuent tous et qu'ils utilisent pour partager leur travail.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/1_BdQ8MuiohcSVp20163pEig.png)
_Dépôt distant et dépôts locaux_

## Comment Git suit-il les changements ?

Pour sauvegarder différentes versions de notre projet dans Git, nous allons faire des commits.

### Qu'est-ce qu'un commit Git ?

Un **commit** est une version de votre projet. Il représente une version autonome de votre projet et a une référence à tous les fichiers et dossiers qui font partie de cette version.

### Comment faire un commit dans Git ?

Pour comprendre comment nous faisons un commit, nous devons apprendre trois espaces différents dans Git : le répertoire de travail, la zone de staging et l'historique des commits.

Le **répertoire de travail** est essentiellement représenté par le contenu de notre dossier de projet (indice : un répertoire est la même chose qu'un dossier). C'est un peu comme un banc de travail, où nous pouvons ajouter, modifier et supprimer des fichiers dans notre projet.

La zone de staging et l'historique des commits font partie de notre dépôt.

La **zone de staging** est un peu comme un espace de brouillon. C'est là que nous pouvons ajouter des versions mises à jour de fichiers ou supprimer des fichiers afin de choisir ce que nous voulons inclure dans notre prochain commit (version de notre projet). Dans le dossier `.git`, la zone de staging est représentée par un fichier appelé `index`.

Et enfin, l'**historique des commits** est essentiellement l'endroit où nos commits vivent après avoir été créés. Dans le dossier `.git`, l'historique des commits est représenté par un dossier appelé `objects`.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/1_V8i09C2Q9xK0u1y7531t3Q--1-.png)
_Répertoire de travail, dépôt, zone de staging et historique des commits_

## Un flux de travail typique avec Git

### Étape 1 — Modifier les fichiers

Si vous avez un nouveau projet, vous créerez le tout premier fichier dans votre nouveau projet. Dans notre dossier de projet `novel`, nous allons créer un simple fichier texte appelé `chapter1`. Nous pouvons le faire soit en utilisant un éditeur de texte, soit directement dans le terminal. Dans notre exemple, nous le faisons directement dans le terminal en tapant `touch chapter1.txt`.

Si vous avez un projet existant, vous modifierez certains de vos fichiers existants, ajouterez de nouveaux fichiers ou supprimerez des fichiers.

Ensuite, nous pouvons utiliser la commande `git status`. Cette commande nous indiquera l'état de notre répertoire de travail et de la zone de staging et nous indiquera s'il y a des différences entre les deux.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/1_jHl7OaAsZBBa-6fuyK8Esw.png)
_Ajout d'un fichier à notre projet_

Dans notre exemple, nous avons ajouté un seul nouveau fichier à notre nouveau projet. Lorsque nous utilisons la commande `git status`, Git nous indique que nous avons un fichier non suivi dans notre répertoire de travail et que nous devons utiliser la commande `git add` pour l'inclure dans ce qui sera commit. Ce qui nous amène à l'étape 2.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/1_r3tL0x5-6x60uycPkIQxbg.png)
_Notre fichier est dans le répertoire de travail_

### Étape 2 — Ajouter des fichiers à la zone de staging

Nous pouvons utiliser la commande `git add` pour ajouter de nouveaux fichiers ou des fichiers mis à jour à la zone de staging. Si nous décidons de ne pas inclure certains des fichiers que nous avons modifiés dans notre prochain commit, nous veillons simplement à ne pas ajouter ces fichiers particuliers à la zone de staging.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/updated.png)
_Ajout d'un fichier à la zone de staging_

Dans notre exemple, nous ajoutons le seul fichier que nous avons dans notre projet à la zone de staging en utilisant la commande `git add` et en passant le nom du fichier. Ensuite, si nous utilisons la commande `git status`, nous verrons que Git nous indique que nous avons ajouté notre fichier à la zone de staging.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/1_90QUPov6WsHjkokIzJw10g.png)
_Notre fichier est dans la zone de staging_

Il est également important de noter que les fichiers **ne se déplacent pas** du répertoire de travail vers la zone de staging. Les fichiers sont **copiés** du répertoire de travail vers la zone de staging.

### Étape 3 — Faire le commit

Enfin, pour faire le commit, nous utilisons la commande `git commit` avec l'option `-m` et passons un message de commit, par exemple `git commit -m "ceci est le premier commit"`.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/1_KoPfPCVxlsOI3qqQLfd9Dw.png)
_Faire notre premier commit_

Nous pouvons ensuite utiliser la commande `git log` pour lister tous les commits que nous avons dans notre projet dans l'ordre chronologique inverse. Dans notre exemple, nous n'avons qu'un seul commit.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/1_O8tbeMHOrjCGNajx2chxHQ.png)
_Nous avons fait notre premier commit_

Maintenant, nous avons fait notre premier commit dans notre projet ! En d'autres termes, nous avons sauvegardé la première version de notre projet.

Le commit a un hash de commit de 40 caractères. Un **hash de commit** est une série de 40 lettres et chiffres qui servent de nom au commit ou de moyen de s'y référer.

Nous pouvons également voir des informations telles que qui a fait le commit, quand le commit a été fait et le message de commit.

## Qu'est-ce qu'un historique de commits dans Git ?

Un dépôt se compose de plusieurs commits, et dans le cas le plus simple, chaque commit a un commit parent qui est le commit qui l'a précédé. C'est pourquoi un commit pointe vers le commit qui l'a précédé dans l'image ci-dessous.

Il existe des cas plus complexes lorsque nous entrons dans le domaine des multiples branches et fusions, mais cela dépasse le cadre de cet article.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/1_pZBMf1JSUf0feoe-fst0Lg.png)
_Un historique de commits simple_

## Enfin, qu'est-ce qu'une branche dans Git ?

Une **branche** est un pointeur vers un commit. La branche par défaut dans Git s'appelle **master** ou **main**.

Nous pouvons voir qu'une branche est un pointeur vers un commit en allant dans le dossier `.git`, puis en ouvrant le dossier `refs`, en ouvrant le dossier `heads` et enfin en ouvrant le fichier appelé `master`. À l'intérieur de ce fichier, nous trouverons qu'il y a un hash. C'est le hash du commit vers lequel notre branche master pointe.

Nous pouvons à nouveau utiliser la commande `git log` pour lister tous les commits dans notre dépôt et nous trouverons que ce hash correspond au commit qui a l'étiquette `master` à côté dans les parenthèses.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/1_4yV_t7acLQZBMwkpXkZyBg.png)
_Affichage de la branche master dans notre dossier .git_

Dans le terminal, nous pouvons voir une liste de toutes les branches en tapant la commande `git branch`.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/1_88nz0tfYI77kjBzQvCDF9Q.png)
_Affichage de la branche master pointant vers notre commit_

Les branches sont vraiment importantes car elles facilitent grandement la collaboration avec d'autres personnes et le travail sur plusieurs fonctionnalités ou différentes parties de votre projet en même temps.

À mesure que nous faisons plus de commits, la branche sur laquelle nous nous trouvons se mettra à jour pour pointer vers notre dernier commit.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/1_iBdgErtar3XDmVQGRyT_9A.png)
_Affichage de notre historique de commits et de la branche master pointant vers notre dernier commit_

## Conclusion

Si vous êtes arrivé jusqu'ici, félicitations ! Il y a beaucoup plus à apprendre sur Git, et dans cet article, nous n'avons fait qu'effleurer la surface. N'hésitez pas à consulter d'autres ressources pour apprendre Git ci-dessous !

### Cours en ligne pour apprendre le contrôle de version avec Git

Cet article est basé sur un [cours en ligne que j'ai créé qui enseigne le contrôle de version avec Git appelé Git Learning Journey](https://www.udemy.com/course/git-learning-journey/?referralCode=3FA102A7FD43300B5BC2). Il enseigne les bases du contrôle de version avec Git, couvrant tout ce qui précède en beaucoup plus de profondeur, et bien plus encore, y compris le travail avec des dépôts distants, la fusion et le rebasage.

Il est spécialement conçu pour les personnes en transition vers la technologie depuis des milieux non techniques et il est devenu un cours **le mieux noté** sur Udemy avec une note de 4,8 étoiles ✨ et plus de 600 étudiants satisfaits (consultez les avis des étudiants, ils parlent d'eux-mêmes). Et les huit premières leçons sont un aperçu gratuit, alors n'hésitez pas à y jeter un coup d'œil !

![Image](https://cdn-images-1.medium.com/max/1600/1*wc4fSBxpGKNX5kZZSMHFhA.png)
_Git Learning Journey, cours en ligne enseignant le contrôle de version avec Git par Anna Skoulikari_