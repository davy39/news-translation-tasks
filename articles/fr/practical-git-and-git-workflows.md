---
title: Comment utiliser Git et les workflows Git – un guide pratique
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-04-01T16:08:23.000Z'
originalURL: https://freecodecamp.org/news/practical-git-and-git-workflows
coverImage: https://cdn-media-2.freecodecamp.org/w1280/60635fd39618b008528a9920.jpg
tags:
- name: Collaboration
  slug: collaboration
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: teamwork
  slug: teamwork
- name: version control
  slug: version-control
seo_title: Comment utiliser Git et les workflows Git – un guide pratique
seo_desc: 'By John Mosesman

  Everyone says you should learn Git—and you should—but let''s be honest: Git is kind
  of hard.

  Even almost ten years into my software development career, I am still learning about
  the underlying Git fundamentals and how to use Git more ...'
---

Par John Mosesman

Tout le monde dit que vous devriez apprendre Git – et vous devriez – mais soyons honnêtes : Git est un peu difficile.

Même après presque dix ans de carrière en développement logiciel, j'apprends encore les fondamentaux sous-jacents de Git et comment l'utiliser plus efficacement.

Il n'y a pas si longtemps, je me suis rendu compte que [j'avais une incompréhension fondamentale](https://twitter.com/johnmosesman/status/1306255666718310401) d'une commande clé que j'avais utilisée d'innombrables fois.

Comme dans de nombreux autres domaines de la programmation, je crois que la meilleure façon d'apprendre est de simplement commencer à _faire_.

Commencez simplement à être productif avec l'outil – les fondamentaux et les cas particuliers se clarifieront avec le temps.

Alors dans ce tutoriel, c'est exactement ce que nous ferons. Nous travaillerons à travers une série d'exemples pour construire une compréhension depuis les bases de comment utiliser Git et finalement collaborer avec vos coéquipiers.

En faisant cela, nous utiliserons des commandes simples et expliquerons les concepts sous-jacents lorsqu'ils sont utiles – mais seulement dans la mesure où ils aident à la compréhension.

Il y a définitivement beaucoup plus à Git que ce qui est présenté ici, mais ce sont des choses que vous apprendrez en travaillant avec lui au fil du temps.

Je n'utiliserai également aucun diagramme d'arborescence (comme celui ci-dessous) car ils ne font que me confondre, et je n'ai jamais eu à penser à Git de cette manière pour être productif en tant que développeur logiciel.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/hero.svg)
_https://www.atlassian.com/git/tutorials/using-branches/git-checkout_

Voici ce que nous allons couvrir. Ne vous laissez pas intimider par cette liste, nous irons étape par étape.

* [Installer git et configurer un compte GitHub](#heading-installation-de-git-et-configuration-dun-compte-github)
* [Comment créer un nouveau dépôt dans GitHub](#heading-comment-creer-un-nouveau-depot-dans-github)
* [Cloner le dépôt](#heading-cloner-le-depot)
* [Branches Git](#heading-branches-git)
* [Comment vérifier l'état d'un projet Git](#heading-comment-verifier-letat-dun-projet-git)
* [Comment faire notre premier commit](#heading-comment-faire-notre-premier-commit)
* [Comment pousser notre premier commit vers GitHub](#heading-comment-pousser-notre-premier-commit-vers-github)
* [Comment ajouter un autre commit dans Git](#heading-comment-ajouter-un-autre-commit-dans-git)
* [Comment mettre en attente les changements dans Git](#heading-comment-mettre-en-attente-les-changements-dans-git)
* [Comment voir la différence Git](#heading-comment-voir-la-difference-git)
* [Comment collaborer avec d'autres dans Git](#heading-comment-collaborer-avec-dautres-dans-git)
* [Branches de fonctionnalités dans Git](#heading-branches-de-fonctionnalites-dans-git)
* [Workflows Git pour la collaboration](#heading-workflows-git-pour-la-collaboration)
* [Comment fusionner une branche dans Git](#heading-comment-fusionner-une-branche-dans-git)
* [Workflow de pull request](#heading-workflow-de-pull-request)
* [Comment mettre à jour notre local](#heading-comment-mettre-a-jour-notre-local)
* [Comment récupérer les données distantes](#heading-comment-recuperer-les-donnees-distantes)
* [Comment résoudre les conflits de fusion dans Git](#heading-comment-resoudre-les-conflits-de-fusion-dans-git)
* [Révision : comment démarrer un nouveau workflow de fonctionnalité](#heading-revision-comment-demarrer-un-nouveau-workflow-de-fonctionnalite)
* [Conclusion](#heading-conclusion)

Alors, avec tout cela dit, je vous encourage à suivre les exemples sur votre propre machine – commençons !

## Installation de Git et configuration d'un compte GitHub

D'abord, quelques choses ennuyeuses que nous devons faire pour commencer.

Si vous avez déjà installé Git, créé un compte GitHub (ou utilisez un autre fournisseur comme GitLab ou Bitbucket), et configuré une clé SSH, vous pouvez sauter cette section.

Sinon, vous devrez d'abord [installer Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

Deuxièmement, nous utiliserons GitHub dans ce tutoriel, alors inscrivez-vous pour un [compte GitHub ici](https://github.com/join).

Après avoir un compte GitHub, vous devrez créer une clé SSH pour pousser votre code de votre machine locale vers GitHub (cette clé prouve à GitHub lorsque vous poussez du code que vous êtes "vous").

Ce n'est pas difficile – suivez simplement [les étapes ici](https://docs.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).

## Comment créer un nouveau dépôt dans GitHub

La prochaine chose que nous ferons est de créer un nouveau dépôt dans GitHub.

C'est simple. Cliquez simplement sur le bouton "Nouveau" dépôt sur votre page d'accueil :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screen-Shot-2021-03-31-at-7.30.33-PM.png)
_Création d'un nouveau dépôt_

Ensuite, choisissez un nom pour le dépôt et si vous voulez que le dépôt soit public ou privé. Vous pouvez optionnellement ajouter un fichier README si vous le souhaitez, puis cliquez sur "Créer un dépôt".

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screen-Shot-2021-03-31-at-7.29.07-PM.png)
_Configuration du nouveau dépôt_

J'ai appelé mon dépôt [practical-git-tutorial](https://github.com/johnmosesman/practical-git-tutorial). Ce dépôt contient toutes les étapes terminées de ce tutoriel déjà dedans, donc si vous le souhaitez, vous pouvez toujours l'utiliser comme référence.

## Cloner le dépôt

Pour commencer, nous allons "cloner" le dépôt. Cloner un dépôt signifie télécharger tout le code et les métadonnées du projet à partir de la source – qui dans ce cas est GitHub.

Pour cloner un dépôt, nous utilisons `git clone <URL>`.

J'ai utilisé l'URL du dépôt que je viens de créer, mais vous devriez utiliser l'URL de votre propre dépôt :

```
$ git clone git@github.com:johnmosesman/practical-git-tutorial.git
Cloning into 'practical-git-tutorial'...
remote: Enumerating objects: 6, done.
remote: Counting objects: 100% (6/6), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 6 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (6/6), done.

```

> **Note :** les commandes à exécuter dans votre terminal seront précédées d'un `$`.

Nous entrerons dans plus de détails sur ce que fait `git clone` bientôt, mais pour l'instant, sachez simplement qu'il télécharge le projet et le place dans un dossier dans votre répertoire de travail actuel.

Ensuite, changeons de répertoire avec `cd` :

```
$ cd practical-git-tutorial/
/practical-git-tutorial (main)$

```

Nous avons changé de dossier (qui est comme n'importe quel autre dossier), et votre terminal peut vous montrer quelque chose à côté du nom du répertoire : `(main)`.

## Branches Git

Ce `(main)` signifie que nous sommes actuellement sur une **branche** appelée `main`. Vous pouvez penser à une branche Git comme une copie du projet _à un moment spécifique_ qui peut être modifiée indépendamment des autres branches.

Par exemple, si nous utilisions Git pour suivre l'écriture d'un livre, nous pourrions avoir des branches qui ressemblent à ceci :

* branche `main`
* branche `table-des-matieres`
* branche `chapitre-1`
* branche `chapitre-2`
* etc.

La branche `main` est, eh bien, la branche "main" – l'endroit où nous allons combiner tout le contenu du livre en un livre finalisé et terminé.

Nous pouvons créer d'autres branches pour séparer et suivre des morceaux spécifiques de travail.

Si je travaillais sur le Chapitre 1 et que vous travailliez sur le Chapitre 2, nous pourrions créer deux branches différentes, `chapitre-1` et `chapitre-2` – effectivement deux copies différentes de l'état actuel du livre.

Nous pourrions ensuite travailler tous les deux sur nos chapitres respectifs sans nous marcher sur les pieds ou changer le contenu sous les pieds de l'autre – nous avons tous les deux notre propre copie de travail qui sont séparées l'une de l'autre.

Lorsque l'un de nous a terminé son chapitre, nous pouvons ajouter le contenu de notre branche de chapitre dans la branche `main`. Lorsque nous avons tous les deux terminé, la branche `main` contiendra à la fois le Chapitre 1 et le Chapitre 2.

Cependant, il y a des moments où vous _allez_ écraser ou changer le même morceau de contenu que quelqu'un d'autre et nous devrons trouver comment régler ces différences – et nous verrons cela bientôt.

> **Note :** selon le projet [vous pourriez voir une branche](https://github.com/github/renaming) nommée `master` au lieu de `main`. Cela n'a aucune différence fonctionnelle, tapez simplement `master` ou `main` selon ce qui se trouve dans votre projet.

## Comment vérifier l'état d'un projet Git

Une chose que nous ferons souvent est de vérifier l'état de notre projet. Quels changements ont été faits et que voulons-nous faire avec eux ?

Pour voir l'état de notre projet, nous utilisons `git status` :

```
(main)$ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean

```

Il y a quelques choses dans le résultat de cette commande, alors décomposons-les.

La première chose que `git status` nous dit est que nous sommes sur la branche `main` :

```
 On branch main
```

La deuxième phrase est un peu plus intéressante :

```
Your branch is up to date with 'origin/main'.

```

Git nous dit que notre branche est "à jour" avec quelque chose appelé `origin/main`.

`origin` est un nouveau concept connu sous le nom de **remote**. Un remote est une "source distante" différente de votre machine locale.

Dans ce projet, nous avons notre copie locale du projet, mais nous pouvons également ajouter des sources distantes avec lesquelles nous pouvons collaborer. Après tout, c'est l'un des plus grands avantages de Git : la collaboration contrôlée avec d'autres.

En continuant avec notre exemple d'écriture de livre, si j'écris le Chapitre 1 sur ma machine et que vous écrivez le Chapitre 2 sur votre machine, nous pourrions tous les deux ajouter les machines de l'autre comme "remotes" et envoyer et recevoir des changements l'un de l'autre.

En pratique, la communauté de programmation dans son ensemble a décidé qu'il est préférable d'avoir une **source unique de vérité** pour le code. Un endroit qui est toujours "correct" sur l'état actuel de la base de code. Par convention, nous appelons cet endroit l'**origin**.

Dans ce cas, GitHub est notre "origin".

En fait, nous pouvons voir cela en exécutant la commande `git remote -v` (`-v` pour "verbose") :

```
(main)$ git remote -v
origin  git@github.com:johnmosesman/practical-git-tutorial.git (fetch)
origin  git@github.com:johnmosesman/practical-git-tutorial.git (push)

```

Cette commande liste tous nos remotes. À partir du résultat, nous pouvons voir que nous avons un remote nommé `origin`, et l'URL Git de ce remote pointe vers notre dépôt sur Github.com. Ce remote a été automatiquement configuré pour nous lorsque nous avons exécuté `git clone`.

Donc, en revenant à cette déclaration dans le résultat de `git status` :

`Your branch is up to date with 'origin/main'.`

Lorsque nous avons demandé l'état de notre projet, Git nous a dit que notre branche locale `main` est à jour avec la branche `main` de notre origin – qui est GitHub.

En fait, `git clone` a automatiquement créé une branche `main` pour nous localement parce qu'il a vu que l'origine que nous avons clonée avait une branche appelée `main` comme sa branche principale.

En gros, il n'y a pas de changements sur notre machine locale différents de GitHub ou vice versa – notre branche locale `main` et la branche `main` de GitHub sont identiques.

Au fur et à mesure que nous apportons des changements, nous verrons ce message changer pour refléter les différences dans notre dépôt local et le dépôt d'origine (GitHub).

Le message final de `git status` concerne l'état du projet local :

```
nothing to commit, working tree clean
```

Nous entrerons dans plus de détails ici au fur et à mesure que nous apportons des changements, mais ce message dit essentiellement que nous n'avons rien fait – donc aucun changement à signaler.

Pour résumer le résultat de `git status` :

* Nous sommes sur la branche `main`
* Notre branche locale `main` est identique à la branche `main` de l'`origin` (GitHub)
* Nous n'avons pas encore apporté de changements au projet

## Comment faire notre premier commit

Maintenant que nous comprenons l'état initial de notre projet, apportons quelques changements et regardons le résultat.

En continuant avec notre analogie de livre, créons un nouveau fichier appelé `chapitre-1.txt` et insérons une phrase dedans.

(Vous pouvez utiliser les commandes de terminal ci-dessous, ou créer et éditer le fichier dans n'importe quel éditeur de texte que vous choisissez – cela n'a pas d'importance.)

```
(main)$ touch chapitre-1.txt
(main)$ echo "Chapitre 1 - Le Début" >> chapitre-1.txt
(main)$ cat chapitre-1.txt
Chapitre 1 - Le Début

```

Les commandes ci-dessus créent un nouveau fichier appelé `chapitre-1.txt` en utilisant `touch`, insèrent la phrase "Chapitre 1 - Le Début" en utilisant `echo` et l'opérateur `>>`, et, pour double-vérifier notre travail, montrent le contenu du fichier en utilisant `cat`.

Le résultat est un simple fichier texte avec une phrase dedans.

Exécutons `git status` à nouveau et voyons la différence dans sa sortie :

```
(main)$ git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        chapitre-1.txt

nothing added to commit but untracked files present (use "git add" to track)

```

Ici, nous voyons une sortie différente de celle d'avant. Nous voyons une section décrivant "Untracked files", et notre nouveau fichier `chapitre-1.txt` est listé là.

Avant que Git ne commence à suivre les changements d'un fichier, nous devons d'abord dire à Git de le suivre – et comme le mentionne le bas du message – nous pouvons utiliser `git add` pour cela :

```
(main)$ git add chapitre-1.txt

```

(Au lieu de spécifier le nom du fichier pour `git add`, vous pouvez utiliser un point (`.`) pour ajouter tous les changements dans le répertoire.)

Vérifions le statut à nouveau :

```
(main)$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   chapitre-1.txt

john:~/code/practical-git-tutorial (main)$

```

Le message a changé à nouveau. Il dit maintenant que nous avons quelques changements qui sont prêts à être "committed".

Un **commit** dans Git est un morceau enregistré de travail, mais il est un peu différent de la même sauvegarde que vous utiliseriez pour sauvegarder un fichier texte dans un éditeur de texte.

Vous pouvez penser à un commit comme une _idée ou une unité de travail complétée_.

Par exemple, si nous continuions à écrire le contenu du Chapitre 1 dans le livre, cela pourrait ressembler à ceci :

* Écrire le titre du chapitre. _*cliquez sur sauvegarder dans notre éditeur*_
* Écrire le premier paragraphe du chapitre. _*cliquez sur sauvegarder dans notre éditeur*_
* Écrire le deuxième paragraphe du chapitre. _*cliquez sur sauvegarder à nouveau*_
* Écrire le paragraphe final du chapitre. _*cliquez sur sauvegarder à nouveau*_

Ici, nous avons "sauvegardé" le document quatre fois, mais à la fin de ces quatre sauvegardes, nous avons maintenant le premier brouillon de notre chapitre, et ce brouillon est une "unité de travail".

Nous voulons sauvegarder ce fichier sur notre ordinateur, mais nous voulons aussi signifier que c'est une unité de travail complétée – même si ce n'est qu'un brouillon. C'est un morceau de travail qui vaut la peine d'être conservé. Nous pourrions vouloir y revenir à l'avenir, revenir en arrière et l'éditer, ou fusionner ce brouillon dans le brouillon actuel de l'ensemble du livre.

Pour ce faire, nous créons un nouveau commit pour signifier cette étape. Chaque commit obtient son propre identifiant unique, et l'ordre des commits est préservé.

Pour commiter nos changements, ils doivent d'abord être ajoutés à la **zone de staging** en utilisant `git add`.

(Nous parlerons plus de la zone de staging bientôt.)

Ensuite, nous devons finaliser le commit en utilisant `git commit`.

Il est considéré comme une bonne pratique de fournir un message détaillé sur _quels changements_ vous avez faits – et plus important encore – _pourquoi_ vous commitez ces changements.

Une fois que l'historique des commits devient des centaines ou des milliers de commits de long, il devient presque impossible de comprendre _pourquoi_ un changement a été fait sans un bon message de commit. Git nous montrera quels fichiers ont changé et quels étaient les changements, mais la _signification de ces changements_ dépend de nous pour la fournir.

Faisons un commit du nouveau fichier que nous avons créé avec un message de commit en utilisant le flag `-m` ou "message" :

```
(main)$ git commit -m "Nouveau fichier chapitre 1 avec l'en-tête du chapitre"
[main a8f8b95] Nouveau fichier chapitre 1 avec l'en-tête du chapitre
 1 file changed, 1 insertion(+)
 create mode 100644 chapitre-1.txt

```

Nous avons maintenant commité ce morceau de travail, et nous pouvons le voir en regardant le journal Git via `git log` :

```
(main)$ git log
commit a8f8b95f19105fe10ed144fead9cab84520181e3 (HEAD -> main)
Author: John Mosesman <johnmosesman@gmail.com>
Date:   Fri Mar 19 12:27:35 2021 -0500

    Nouveau fichier chapitre 1 avec l'en-tête du chapitre

commit 2592324fae9c615a96f856a0d8b8fe1d2d8439f8 (origin/main, origin/HEAD)
Author: John Mosesman <johnmosesman@users.noreply.github.com>
Date:   Wed Mar 17 08:48:25 2021 -0500

    Mise à jour de README.md

commit 024ea223ee4055ae82ee31fc605bbd8a5a3673a0
Author: John Mosesman <johnmosesman@users.noreply.github.com>
Date:   Wed Mar 17 08:48:10 2021 -0500

    Commit initial

```

En regardant ce journal, nous voyons qu'il y a trois commits dans l'historique du projet.

Le dernier commit est celui que nous venons de faire. Nous pouvons voir le même message de commit que nous venons d'utiliser : _"Nouveau fichier chapitre 1..."._

Il y a aussi deux commits précédents : un lorsque j'ai initialisé le projet et un autre lorsque j'ai mis à jour le fichier `README.md` sur GitHub.

Remarquez que chaque commit a une longue chaîne de nombres et de caractères qui lui est associée :

```
commit a8f8b95f19105fe10ed144fead9cab84520181e3 (HEAD -> main)

```

Cette chaîne de caractères et de nombres est appelée [SHA](https://en.wikipedia.org/wiki/SHA-1) – c'est l'ID unique généré par un algorithme de hachage pour ce commit. Notez simplement ceux-ci pour l'instant – nous y reviendrons bientôt.

Nous voyons également deux autres choses intéressantes dans le journal après les SHA des commits :

* `(HEAD -> main)` à côté de notre dernier commit
* Et `(origin/main, origin/HEAD)` à côté du commit précédent.

Ces informations nous indiquent l'_état actuel de nos branches et de nos remotes_ (autant que nous le sachions – mais nous en parlerons plus tard).

Pour le dernier commit, nous voyons que le `HEAD` (aka "où nous sommes maintenant" dans l'historique du projet) pointe vers notre branche locale `main` – représenté par `HEAD -> main`.

Cela a du sens car nous venons de faire ce commit, et nous n'avons rien fait d'autre – nous sommes toujours au point dans le temps où nous avons fait ce commit.

Si nous regardons le commit précédent commençant par `25923`, nous voyons `(origin/main, origin/HEAD)`. Cela nous dit que, _sur l'origine (aka GitHub)_, le `HEAD` de GitHub ou "l'endroit actuel" est sur notre commit précédent.

En gros, notre machine locale pense que le dernier changement pour la branche locale `main` est le commit où nous avons ajouté le Chapitre 1, et notre machine locale pense également que _sur GitHub_ le dernier changement est le commit où j'ai mis à jour le README avant d'écrire ce post.

Et cela a du sens – nous n'avons pas dit à GitHub à propos du nouveau commit que nous avons fait. GitHub pense toujours que le dépôt est à jour avec ce qu'il a vu.

Maintenant, poussons notre nouveau commit vers GitHub.

## Comment pousser notre premier commit vers GitHub

Nous avons un nouveau commit sur notre machine locale et nous devons mettre à jour notre "source de vérité" – le remote `origin` – aka GitHub.

Nous sommes actuellement sur la branche `main` localement, donc nous devons dire à GitHub de mettre à jour son propre `main` avec le nouveau commit que nous avons fait.

Pour cela, nous utilisons la commande `git push` et nous pouvons spécifier _où nous voulons pousser_ et _quelle branche nous voulons pousser_.

```
(main)$ git push origin main
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 16 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 326 bytes | 326.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To github.com:johnmosesman/practical-git-tutorial.git
   2592324..a8f8b95  main -> main

```

Ici, nous avons poussé vers le remote `origin` (GitHub) et vers la branche `main`.

La sortie nous indique certaines opérations de fichiers que Git a effectuées pour cela, et la dernière ligne de la sortie nous indique quels commits il a poussés et où :

```
To github.com:johnmosesman/practical-git-tutorial.git
   2592324..a8f8b95  main -> main

```

Ici, il nous montre que nous avons poussé notre branche `main` vers la branche `main` de GitHub.

Si nous regardons à nouveau la sortie de `git log`, nous remarquerons que notre local et `origin` pointent maintenant vers le même commit :

```
(main)$ git log
commit f5b6e2f18f742e2b851e38f52a969dd921f72d2f (HEAD -> main, origin/main, origin/HEAD)
Author: John Mosesman <johnmosesman@gmail.com>
Date:   Mon Mar 22 10:07:35 2021 -0500

    Ajout de la ligne d'introduction au chapitre 1

```

En bref, sur `origin` (GitHub), la branche `main` (également écrite `origin/main`) a maintenant placé notre nouveau commit comme le dernier commit dans l'historique.

Si nous travaillions avec d'autres collaborateurs, ils pourraient maintenant tirer notre nouveau changement de GitHub et commencer à éditer le Chapitre 1 également.

## Comment ajouter un autre commit dans Git

Avant de commencer à collaborer avec d'autres, faisons un autre petit changement pour voir ce qui se passe lorsque nous éditons un fichier existant.

Ajoutons une autre ligne dans notre fichier du Chapitre 1 :

```
(main)$ echo "C'était le meilleur des temps, c'était le pire des temps" >> chapitre-1.txt
(main)$ cat chapitre-1.txt
Chapitre 1 - Le Début
C'était le meilleur des temps, c'était le pire des temps

```

En utilisant `cat`, nous pouvons voir que notre fichier contient maintenant deux lignes.

Regardons l'état de notre dépôt Git à nouveau :

```
(main)$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   chapitre-1.txt

no changes added to commit (use "git add" and/or "git commit -a")

```

En commençant par le haut, nous remarquerons que la sortie dit `Your branch is up to date with 'origin/main'.`

Cela peut vous sembler étrange puisque nous venons de changer un fichier, mais Git ne compare que _les commits_ que nous avons faits par rapport aux commits dans `origin/main`.

La section suivante de la sortie l'explique un peu plus :

```
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   chapitre-1.txt

```

Ici, Git nous dit que nous avons des "changements non mis en attente pour commit".

Avant de pouvoir commiter un ensemble de changements, nous devons d'abord les **mettre en attente**.

### Comment mettre en attente les changements dans Git

Pour illustrer l'utilité de la zone de staging, mettons d'abord en attente nos changements en utilisant `git add` :

```
(main)$ git add .
(main)$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   chapitre-1.txt

```

Ces changements sont maintenant prêts à être commités, mais avant de les commiter, ajoutons un autre changement dans notre fichier `chapitre-1.txt`.

Je vais remplacer entièrement le contenu de `chapitre-1.txt` par un nouveau texte :

> **Note :** J'utilise `>` ici au lieu de `>>` ce qui remplacera le contenu du fichier au lieu de l'ajouter.

```
(main)$ echo "Nouveau contenu du fichier" > chapitre-1.txt

(main)$ cat chapitre-1.txt
Nouveau contenu du fichier

(main)$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   chapitre-1.txt

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   chapitre-1.txt

```

À partir de la sortie, nous pouvons voir que nous avons maintenant des changements _mis en attente_, et des changements _non mis en attente_.

Bien que le fichier lui-même ne puisse contenir qu'une seule chose, Git suit les deux changements pour nous – même s'ils sont des changements sur les mêmes lignes !

Cependant, à partir de la sortie ci-dessus, nous ne pouvons pas vraiment dire quels étaient ces changements – nous savons simplement qu'ils existent.

Pour voir ces changements, nous regarderons d'abord la méthode en ligne de commande (que je n'utilise jamais), puis une méthode qui utilise une interface graphique (qui est 100 % plus agréable).

### Comment voir la différence Git

Pour voir les changements, nous devons regarder la **diff** Git.

Une _diff_ (abréviation de différence) est la différence entre deux ensembles de changements. Ces changements pourraient être n'importe quoi, des changements mis en attente aux changements non mis en attente en passant par les commits.

La méthode en ligne de commande pour faire cela est d'utiliser `git diff`.

Nous regarderons cette sortie dans notre cas simple ici juste pour l'exhaustivité. Mais, comme je l'ai mentionné auparavant, nous nous intéressons aux workflows Git efficaces, et une fois que vous arrivez à des changements de taille décente sur plusieurs fichiers, cette sortie en ligne de commande devient simplement inefficace.

Mais pour l'exhaustivité, la voici :

```
(main)$ git diff
diff --git a/chapitre-1.txt b/chapitre-1.txt
index 0450d87..4cbeaee 100644
--- a/chapitre-1.txt
+++ b/chapitre-1.txt
@@ -1,2 +1 @@
-Chapitre 1 - Le Début
-C'était le meilleur des temps, c'était le pire des temps
+Nouveau contenu du fichier

```

Mon terminal tente de coloriser cette sortie pour aider à la lisibilité, mais les parties importantes à noter ici sont qu'il nous dit quel fichier nous différencions, `chapitre-1.txt`, et en bas, il nous montre les différences réelles. Concentrons-nous sur ces lignes :

```
-Chapitre 1 - Le Début
-C'était le meilleur des temps, c'était le pire des temps
+Nouveau contenu du fichier

```

Les lignes commençant par un signe moins (`-`) sont des lignes que nous avons entièrement supprimées ou en partie, et les lignes commençant par un signe `+` représentent des lignes ajoutées entièrement ou en partie.

Maintenant, avec plusieurs fichiers et de nombreuses lignes modifiées, cette sortie devient ingérable – rapidement. Il existe une meilleure façon, et même après presque dix ans de carrière en programmation, j'utilise toujours un simple programme GUI pour m'aider à regarder et gérer les diffs.

Le programme que j'utilise s'appelle [GitX](http://gitx.frim.nl/), et c'est un vieux logiciel obsolète qui n'est même plus vraiment maintenu. Cependant, je l'utilise simplement pour visualiser et gérer les diffs de fichiers – donc cela fonctionne pour moi.

Je ne le recommanderais pas particulièrement, mais il est gratuit. Bien que je ne l'aie jamais utilisé, le [client GitHub Desktop](https://desktop.github.com/) est probablement un bon choix.

Maintenant, avec cette petite parenthèse terminée, voici à quoi ressemble la diff dans mon outil.

Pour commencer, les changements mis en attente sur le côté droit montrent notre ajout initial de la deuxième phrase :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/staged_changes.png)
_Changements mis en attente dans GitX_

Dans les changements non mis en attente sur le côté gauche, nous voyons la suppression de ces deux lignes entièrement et l'ajout d'une nouvelle ligne :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/unstaged_changes.png)
_Changements non mis en attente dans GitX_

Cela correspond à la commande de remplacement de fichier que nous avons exécutée.

Il est tellement plus facile de comprendre la diff dans un programme GUI. Ce programme me permet également de basculer rapidement entre la mise en attente et la non-mise en attente des fichiers en les faisant simplement glisser. Je peux même mettre en attente ou non des lignes individuelles dans un fichier.

Il n'y a pas de points bonus pour utiliser la ligne de commande par rapport à un programme GUI. Utilisez ce qui vous permet d'accomplir la tâche.

Maintenant que nous avons vu comment fonctionne la zone de staging et les diffs Git, abandonnons nos changements non mis en attente afin de pouvoir revenir à la validation de notre premier changement.

Dans mon programme GUI, je peux faire un clic droit sur le fichier et cliquer sur "Discard changes", mais je vais également montrer la version en ligne de commande ici.

La sortie de notre dernier `git status` nous a en fait montré comment faire cela en utilisant `git restore`. Nous pouvons passer le chemin du fichier ou simplement un `.` pour tout le répertoire :

```
(main)$ git restore .

```

Si nous vérifions le statut à nouveau, nous sommes de retour à nos changements mis en attente, et nous pouvons continuer.

> **Note :** Git ne valide que les changements qui sont mis en attente, donc nous aurions pu laisser ces changements non mis en attente dans notre répertoire de travail et cela n'aurait pas interféré avec le processus de validation.
>   
> Cependant, cela rendrait nos futurs changements plus fastidieux à gérer – il est donc logique d'abandonner ces changements pour garder notre répertoire de travail en bon état.

Maintenant, validons enfin ces changements avec un message sur ce que nous avons fait :

```
(main)$ git commit -m "Ajout de la ligne d'introduction au chapitre 1"
[main f5b6e2f] Ajout de la ligne d'introduction au chapitre 1
 1 file changed, 1 insertion(+)

```

Vérifier le statut une fois de plus nous montre que notre branche est "en avance de 1 commit sur 'origin/main'" :

```
(main)$ git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

```

Enfin, poussons notre changement :

```
(main)$ git push origin main

```

## Comment collaborer avec d'autres dans Git

Jusqu'à présent, nous avons examiné le cas d'utilisation le plus simple : travailler seul sur une branche.

En réalité, nous travaillerons généralement avec plusieurs personnes sur plusieurs branches différentes. C'est là que réside la véritable puissance de Git : un système pour collaborer et suivre les changements au fil du temps parmi de nombreux collaborateurs.

Pour l'instant, continuons à travailler comme si nous étions la seule personne sur le projet, mais ajustons un peu notre workflow pour nous préparer au moment où ce ne sera plus le cas.

En général, il est considéré comme une bonne pratique de _ne pas_ travailler directement sur la branche `main`.

La branche `main` est censée être la "source de vérité" pour le projet – les changements qui y sont apportés doivent être soigneusement examinés. Tout changement dans `origin/main` devient la nouvelle "source de vérité" pour toute autre personne travaillant sur le projet, donc nous ne devrions pas simplement la changer sans réflexion et sans examen par les autres.

Au lieu de travailler directement sur `main`, créons une **branche de fonctionnalité** à partir de `main`, puis **fusionnons** ces changements dans `main`.

C'est beaucoup de nouvelle terminologie, alors prenons cela étape par étape.

### Branches de fonctionnalités dans Git

Pour commencer, créons une branche à partir de `main` et créons notre propre branche de fonctionnalité sur laquelle travailler.

Lorsque vous créez une branche à partir d'une autre branche, vous créez une copie de cette branche _à ce moment précis_. Vous pouvez maintenant modifier cette nouvelle branche indépendamment de la branche originale.

Pour essayer cela, créons une nouvelle branche appelée `chapitre-2`. Pour cela, nous utilisons `git checkout` avec le flag `-b` et le nom que nous voulons donner à la nouvelle branche :

```
(main)$ git checkout -b chapitre-2
Switched to a new branch 'chapitre-2'
(chapitre-2)$

```

Remarquez que le terminal nous montre maintenant sur la branche `chapitre-2`. Les changements sur la branche `chapitre-2` n'affecteront pas du tout la branche `main`. Nous avons essentiellement un nouveau terrain de jeu pour faire tous les changements que nous voulons sans affecter `main`.

Il se passe des choses intéressantes sous le capot ici, mais pour les besoins de ce tutoriel, nous devons simplement savoir que pour "checkout" quelque chose dans Git signifie "changer mon projet local pour qu'il ressemble exactement au projet tel qu'il était _à un moment spécifique_." Vous pouvez penser à une branche comme un pointeur vers une timeline spécifique de l'historique Git.

Il se passe beaucoup plus de choses ici, mais cette définition devrait suffire pour l'instant.

Donc, nous avons une nouvelle branche, et pour l'instant, cette nouvelle branche est identique à `main` (nous n'avons pas encore fait de changements).

Ensuite, répétons ce que nous avons déjà fait auparavant et créons un nouveau fichier appelé `chapitre-2.txt`, donnons-lui un contenu, et validons-le :

```
(chapitre-2)$ touch chapitre-2.txt
(chapitre-2)$ echo "Chapitre 2 - Le chapitre suivant" >> chapitre-2.txt

(chapitre-2)$ git status
On branch chapitre-2
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        chapitre-2.txt

nothing added to commit but untracked files present (use "git add" to track)

(chapitre-2)$ git add .

(chapitre-2)$ git commit -m "Crée le chapitre 2 et ajoute la phrase de sujet"
[chapitre-2 741822a] Crée le chapitre 2 et ajoute la phrase de sujet
 1 file changed, 1 insertion(+)
 create mode 100644 chapitre-2.txt

```

Rien de nouveau là-dedans – juste la même chose que nous avons fait pour le Chapitre 1.

Maintenant que nous avons un nouveau commit sur notre branche `chapitre-2`, regardons le journal Git et comparons cette nouvelle branche à `main` :

```
(chapitre-2)$ git log
commit 741822a9fd7b15b6e3caf437dd0617fabf918449 (HEAD -> chapitre-2)
Author: John Mosesman <johnmosesman@gmail.com>
Date:   Mon Mar 22 10:33:26 2021 -0500

    Crée le chapitre 2 et ajoute la phrase de sujet

commit f5b6e2f18f742e2b851e38f52a969dd921f72d2f (origin/main, origin/HEAD, main)
Author: John Mosesman <johnmosesman@gmail.com>
Date:   Mon Mar 22 10:07:35 2021 -0500

    Ajout de la ligne d'introduction au chapitre 1

commit a8f8b95f19105fe10ed144fead9cab84520181e3
Author: John Mosesman <johnmosesman@gmail.com>
Date:   Fri Mar 19 12:27:35 2021 -0500

    Nouveau fichier chapitre 1 avec l'en-tête du chapitre
...

```

Nous remarquerons dans le journal que notre dernier commit est affiché en haut, et que notre `HEAD` est à nouveau différent de notre `origin`. Cela a à nouveau du sens – nous avons fait des changements localement qui ne sont pas sur GitHub.

Maintenant, nous devons intégrer nos nouveaux changements dans la branche `main`.

## Workflows Git pour la collaboration

Il existe plusieurs façons d'intégrer notre nouveau Chapitre 2 dans la branche `main` et dans GitHub, et la méthode que nous choisissons dépend du projet et du workflow que nous utilisons pour collaborer avec les autres.

Tout d'abord, parlons de quelques workflows différents que nous pourrions utiliser.

Le premier est le plus simple :

1. Fusionner les changements de `chapitre-2` dans notre branche locale `main`
2. Pousser la branche locale `main` vers `origin/main`

La deuxième méthode est un peu plus compliquée :

* Pousser notre branche locale `chapitre-2` vers origin (cela crée une nouvelle branche sur `origin` appelée `origin/chapitre-2`)
* Fusionner `origin/chapitre-2` dans `origin/main` sur GitHub
* Tirer les nouveaux changements de `origin/main` dans notre `main` local

Le premier workflow est définitivement plus facile, et c'est quelque chose que j'utiliserais si je travaillais sur ce projet seul sans aucun autre collaborateur.

Cependant, si j'avais des collaborateurs, je ne voudrais pas pousser directement vers la branche `main` depuis mon local. En faisant cela, je changerais et prendrais le contrôle de l'historique du projet uniquement sur mes propres changements – sans aucune contribution ou révision des collaborateurs.

Pour cette raison, si plusieurs personnes travaillaient sur le même projet, j'utiliserais le deuxième workflow car c'est un meilleur processus de collaboration pour l'équipe.

Cela dit, nous passerons en revue les deux workflows, et commençons par le premier qui est moins compliqué.

## Comment fusionner une branche dans Git

Lorsque vous souhaitez combiner le contenu de deux branches en une seule dans Git, il existe plusieurs méthodes pour le faire. La première et probablement la plus simple est de faire une **fusion**.

Une fusion, comme son nom l'indique, tente de prendre le contenu d'une branche et d'appliquer (ou "fusionner") ces changements dans une autre branche.

Dans notre scénario, nous voulons prendre le contenu de la branche `chapitre-2` et _les fusionner dans_ `main`. Autrement dit, nous voulons prendre l'état actuel de `main` et y ajouter nos changements de la branche `chapitre-2`.

Nous pouvons faire cela en utilisant `git merge`, et nous examinerons le résultat par la suite.

La première chose que nous devons faire est d'être sur la branche principale dans laquelle nous voulons fusionner les changements. Puisque nous voulons que `main` absorbe les changements de `chapitre-2`, nous devons d'abord être sur la branche `main`.

Pour revenir à la branche `main`, nous pouvons à nouveau utiliser `git checkout` et spécifier le nom de la branche `main`. Cette fois, nous n'utilisons pas le flag `-b` car nous voulons passer à une branche existante et non en créer une nouvelle :

```
(chapitre-2)$ git checkout main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
(main)$

```

Nous sommes maintenant de retour sur la branche `main`, et nous obtenons un message d'état rapide indiquant que nous sommes à jour avec `origin/main`.

Ensuite, fusionnons notre branche `chapitre-2` dans `main` :

```
(main)$ git merge chapitre-2
Updating f5b6e2f..741822a
Fast-forward
 chapitre-2.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 chapitre-2.txt

```

Regardons à nouveau le journal Git pour voir le résultat :

```
(main)$ git log
commit 741822a9fd7b15b6e3caf437dd0617fabf918449 (HEAD -> main, chapitre-2)
Author: John Mosesman <johnmosesman@gmail.com>
Date:   Mon Mar 22 10:33:26 2021 -0500

    Crée le chapitre 2 et ajoute la phrase de sujet

commit f5b6e2f18f742e2b851e38f52a969dd921f72d2f (origin/main, origin/HEAD)
Author: John Mosesman <johnmosesman@gmail.com>
Date:   Mon Mar 22 10:07:35 2021 -0500

    Ajout de la ligne d'introduction au chapitre 1
    
...

```

Nous pouvons voir que notre branche `main` contient maintenant le nouveau commit de `chapitre-2`, et que notre `origin` est toujours au commit précédent (car nous n'avons pas encore mis à jour `origin`).

Enfin, poussons nos changements vers `origin/main` :

```
(main)$ git push origin main
Total 0 (delta 0), reused 0 (delta 0)
To github.com:johnmosesman/practical-git-tutorial.git
   f5b6e2f..741822a  main -> main

```

Nous avons réussi à fusionner notre branche `chapitre-2`, et à pousser ce changement vers GitHub !

Comme étape finale de nettoyage, supprimons la branche de fonctionnalité `chapitre-2` car elle a déjà été fusionnée dans `main` :

```
(main)$ git branch -d chapitre-2
Deleted branch chapitre-2 (was 741822a).

```

> **Note :** la commande `git branch` sans argument de nom de branche liste toutes les branches que vous avez localement.
>   
> L'ajout du flag `-d` et d'un nom de branche supprime la branche passée en argument.

## Workflow de pull request

Pour travailler à travers notre workflow de collaboration, répétons la même chose que nous avons fait avec les chapitres 1 et 2 sur une nouvelle branche appelée `chapitre-3` :

(Maintenant serait un bon moment pour essayer cela par vous-même !)

```
(main)$ git checkout -b chapitre-3
(chapitre-3)$ touch chapitre-3.txt
(chapitre-3)$ echo "Chapitre 3 - La Fin ?" >> chapitre-3.txt
(chapitre-3)$ git add .
(chapitre-3)$ git commit -m "Ajoute le Chapitre 3"

```

Nous avons maintenant un nouveau commit sur une nouvelle branche appelée `chapitre-3`.

Récapitulons comment nous allons faire fusionner cette nouvelle branche dans `main` _sans agir directement sur `main` nous-mêmes_ :

* Pousser notre branche locale `chapitre-3` vers origin (cela crée une nouvelle branche sur `origin` appelée `origin/chapitre-3`)
* Fusionner `origin/chapitre-3` dans `origin/main` sur GitHub
* Tirer les nouveaux changements de `origin/main` dans notre `main` local

Quelques étapes de plus – mais aucune qui soit trop compliquée.

La première étape consiste à pousser notre nouvelle branche vers GitHub. Comme cette branche n'existe pas encore sur GitHub, GitHub créera une nouvelle branche pour nous qui est une copie de ce que nous avons poussé :

```
(chapitre-3)$ git push origin chapitre-3
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 16 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 299 bytes | 299.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
remote:
remote: Create a pull request for 'chapitre-3' on GitHub by visiting:
remote:      https://github.com/johnmosesman/practical-git-tutorial/pull/new/chapitre-3
remote:
To github.com:johnmosesman/practical-git-tutorial.git
 * [new branch]      chapitre-3 -> chapitre-3

```

Maintenant que nous avons notre branche sur GitHub, nous pouvons créer une **pull request** pour qu'elle soit examinée par nos coéquipiers.

GitHub nous fournit même l'URL à visiter dans notre sortie ci-dessus : `https://github.com/johnmosesman/practical-git-tutorial/pull/new/chapitre-3`

> **Quelques notes :** cette prochaine partie montre l'interface utilisateur et le processus de GitHub pour les pull requests, mais ce processus devrait être très similaire pour d'autres services (comme GitLab, Bitbucket, etc.).
>   
> Gardez également à l'esprit que j'utilise mon propre dépôt, donc certaines des URL que vous voyez ici seront différentes des vôtres.

En visitant l'URL ci-dessus, nous arrivons à une page pour ouvrir une nouvelle pull request.

Nous voyons quelques choses :

* Un endroit pour spécifier le nom de la pull request (une phrase d'accroche pour comprendre facilement de quoi parle cette PR)
* Une boîte pour une description expliquant les changements que nous avons faits et tout autre contexte que nous voulons fournir (vous pouvez également ajouter des images, des gifs ou des vidéos ici aussi)
* Et en dessous de tout cela se trouve la liste des fichiers que nous avons modifiés et les changements qu'ils contiennent (la diff).

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screen-Shot-2021-03-24-at-10.22.13-AM.png)
_Ouvrir une nouvelle pull request_

Remarquez que l'interface utilisateur montre `base: main <- compare: chapitre-3`. Cela signifie que GitHub nous indique que nous définissons la pull request pour fusionner `chapitre-3` _dans_ `main`.

En dessous de la description de la pull request se trouve la diff des changements que nous avons faits :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screen-Shot-2021-03-24-at-10.26.42-AM.png)
_La diff de la pull request_

Nous remarquerons que seul le fichier `chapitre-3.txt` est affiché, et cela est dû au fait que c'est le seul fichier que nous avons modifié.

Il y a d'autres fichiers actuellement dans notre projet (`chapitre-1.txt`, `chapitre-2.txt`), mais ces fichiers n'ont pas changé, donc il n'est pas nécessaire de les afficher.

Nous voyons la seule ligne que nous avons insérée dans `chapitre-3.txt` – signifiée par un signe `+` au début de la ligne et le fond vert qui signifie une addition au fichier.

Après avoir cliqué sur "Create Pull Request", nous sommes redirigés vers la nouvelle PR que nous venons de créer.

À ce stade, nous pourrions assigner un relecteur à la PR et avoir une discussion aller-retour autour du code en laissant des commentaires sur des lignes spécifiques dans la diff. Après que le code ait été révisé et que nous ayons fait les changements nécessaires, nous sommes prêts à fusionner.

Pour les besoins de ce tutoriel, nous sauterons le processus de révision et cliquerons simplement sur le gros bouton vert de fusion :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screen-Shot-2021-03-24-at-10.39.55-AM.png)
_Pull request fusionnée_

Et avec cela, notre pull request a été fusionnée dans `main` !

## Comment mettre à jour notre local

Nous avons maintenant apporté un changement à `origin/main` de manière sûre, contrôlée et révisée par les pairs.

Mais notre local ne sait rien de ce changement. Localement, Git pense toujours que nous sommes sur notre branche `chapitre-3` qui n'est pas fusionnée dans `main` :

```
(chapitre-3)$ git log
commit 085ca1ce2d0010fdaa1c0ffc23ff880091ce1692 (HEAD -> chapitre-3, origin/chapitre-3)
Author: John Mosesman <johnmosesman@gmail.com>
Date:   Tue Mar 23 09:19:14 2021 -0500

    Ajoute le Chapitre 3

commit 741822a9fd7b15b6e3caf437dd0617fabf918449 (origin/main, origin/HEAD, main)
Author: John Mosesman <johnmosesman@gmail.com>
Date:   Mon Mar 22 10:33:26 2021 -0500

    Crée le chapitre 2 et ajoute la phrase de sujet

...

```

Notre local montre `origin/main` sur le commit précédent commençant par `741822`. Nous devons récupérer les nouvelles informations de notre `origin` pour mettre à jour notre dépôt local.

### Comment récupérer les données distantes

Comme pour beaucoup d'autres choses avec Git, il existe plusieurs méthodes pour accomplir la même tâche.

Pour nos besoins, nous allons examiner une méthode simple qui fonctionnera dans la majorité des cas.

Pour commencer, revenons à notre branche `main` localement :

```
(chapitre-3)$ git checkout main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.

```

Notre local pense que nous sommes à jour avec `origin/main` parce que nous n'avons pas demandé au dépôt distant (`origin`) de nouvelles informations depuis que nous avons tiré le projet au début en utilisant `git clone`.

Les dépôts Git ne sont pas mis à jour en temps réel – ils ne sont qu'un instantané de l'historique à un moment donné. Pour recevoir de nouvelles informations sur le dépôt, nous devons les demander à nouveau.

Pour récupérer toutes les nouvelles informations qui ont changé sur le distant, nous utilisons `git fetch` :

```
(main)$ git fetch
From github.com:johnmosesman/practical-git-tutorial
   741822a..10630f2  main       -> origin/main

```

La sortie nous montre que `origin/main` pointe maintenant vers un commit commençant par `10630f2`. Ce préfixe de commit correspond au SHA du commit de fusion de notre pull request.

Il existe plusieurs façons de fusionner deux branches en une seule, et l'une de ces façons est de créer un **commit de fusion**. C'est ce qui s'est passé ici.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/commit.png)
_Le commit de fusion de notre PR_

Notre dépôt local connaît maintenant la présence de ces nouveaux commits, mais nous n'avons rien fait avec eux pour l'instant.

L'exécution de `git fetch` ne change pas réellement nos fichiers – elle télécharge simplement de nouvelles informations du distant sur l'état du dépôt.

Maintenant que notre dépôt local est conscient de l'état de chaque branche (mais n'a pas _changé ou mis à jour_ aucune des branches), vérifions à nouveau notre statut :

```
(main)$ git status
Your branch is behind 'origin/main' by 2 commits, and can be fast-forwarded.
  (use "git pull" to update your local branch)

```

Notre local sait maintenant que notre `main` local est en retard de 2 commits par rapport à `origin/main` (le commit de la branche `chapitre-3` et le commit de fusion de la PR).

Il nous donne également l'indice d'utiliser `git pull` pour mettre à jour notre branche locale :

```
john:~/code/practical-git-tutorial (main)$ git pull origin main
From github.com:johnmosesman/practical-git-tutorial
 * branch            main       -> FETCH_HEAD
Updating 741822a..10630f2
Fast-forward
 chapitre-3.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 chapitre-3.txt

```

La commande `git pull` est en fait un raccourci pour exécuter deux commandes : `git fetch` suivi d'un `git merge`.

Puisque `git fetch` n'applique aucun changement localement, il peut être utile d'utiliser `git fetch` pour voir si nos branches sont à jour avec le distant (peut-être que nous ne voulons pas encore fusionner les changements), ou pour tirer de nouvelles branches qui existent sur le distant et non sur notre machine locale.

La récupération d'une _nouvelle_ branche depuis un distant ira de l'avant et téléchargera également cette branche sur votre machine locale – puisque c'est une nouvelle branche, elle n'entrera pas en conflit avec quoi que ce soit dans votre configuration locale.

Nous aurions pu simplement faire un `git pull` initialement au lieu de faire d'abord un `git fetch`, mais je voulais expliquer `git fetch` car il est utile en soi.

Après avoir exécuté `git pull`, si nous exécutons `git status` une fois de plus, nous verrons que tout est à jour.

Et avec cela, nous avons récupéré les changements de notre distant et mis à jour notre local !

## Comment résoudre les conflits de fusion dans Git

Le dernier sujet que nous aborderons est la gestion des conflits.

Jusqu'à présent, Git a simplement géré automatiquement toutes les mises à jour de fichiers, et la plupart du temps Git peut simplement le gérer. Mais il y a des moments où Git ne sait pas comment combiner les changements ensemble, et cela crée un **conflit**.

Un conflit se produit lorsque l'on fusionne deux changements qui ont modifié la même ligne dans un fichier. Si deux commits ont modifié la même ligne dans un fichier, Git ne sait pas quels changements de commit utiliser, et il vous demandera de faire le choix.

Pour configurer ce scénario, j'ai créé une autre branche sur GitHub appelée `chapitre-3-collaboration`. Imaginons qu'un coéquipier a déjà commencé à travailler sur cette branche et qu'il vous a demandé de collaborer avec lui pour terminer le Chapitre 3.

Puisque c'est une nouvelle branche que nous n'avons pas localement, nous pouvons utiliser `git fetch` pour récupérer les nouvelles informations de la branche depuis le distant, puis basculer vers cette branche en utilisant `git checkout` :

```
(main)$ git fetch
From github.com:johnmosesman/practical-git-tutorial
 * [new branch]      chapitre-3-collaboration -> origin/chapitre-3-collaboration

(main)$ git checkout chapitre-3-collaboration
Branch 'chapitre-3-collaboration' set up to track remote branch 'chapitre-3-collaboration' from 'origin'.
Switched to a new branch 'chapitre-3-collaboration'
(chapitre-3-collaboration)$

```

Nous avons maintenant téléchargé la nouvelle branche vers notre dépôt local et basculé vers celle-ci. Voici le contenu de `chapitre-3.txt` sur cette nouvelle branche actuellement :

```
(chapitre-3-collaboration)$ cat chapitre-3.txt
Chapitre 3 - La Fin ?

Ceci est une phrase.

```

C'est un titre et une phrase. Changeons le titre en quelque chose de nouveau comme _"Chapitre 3 - La Fin N'est Que Le Début."_

Le contenu de `chapitre-3.txt` ressemble maintenant à ceci :

```
(chapitre-3-collaboration)$ cat chapitre-3.txt
Chapitre 3 - La Fin N'est Que Le Début

Ceci est une phrase.

```

Après avoir validé ce changement, si nous essayons de le pousser, nous obtenons ce message :

```
(chapitre-3-collaboration)$ git push origin chapitre-3-collaboration
To github.com:johnmosesman/practical-git-tutorial.git
 ! [rejected]        chapitre-3-collaboration -> chapitre-3-collaboration (non-fast-forward)
error: failed to push some refs to 'git@github.com:johnmosesman/practical-git-tutorial.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

```

Notre coéquipier a déjà fait quelques commits avant nous et les a poussés vers la branche distante. Notre branche locale est maintenant obsolète par rapport à la branche distante, et GitHub refuse notre push jusqu'à ce que nous fusionnions les changements de notre coéquipier :

```
... the tip of your current branch is behind its remote counterpart. Integrate the remote changes ... before pushing again.

```

Il nous donne également un indice sur la façon de le faire : `git pull`.

```
(chapitre-3-collaboration)$ git pull origin chapitre-3-collaboration
From github.com:johnmosesman/practical-git-tutorial
 * branch            chapitre-3-collaboration -> FETCH_HEAD
Auto-merging chapitre-3.txt
CONFLICT (content): Merge conflict in chapitre-3.txt
Automatic merge failed; fix conflicts and then commit the result.

```

Après avoir tiré – et comme nous aurions pu nous y attendre étant donné le sujet que nous discutons actuellement – nous avons un conflit de fusion.

Git a essayé de fusionner automatiquement les changements de notre coéquipier dans les nôtres, mais il y avait un endroit dans le fichier qu'il ne pouvait pas fusionner automatiquement – nous avons tous les deux changé la même ligne.

Git s'est arrêté "en cours de fusion" et nous dit que nous devons résoudre les conflits de fusion avant qu'il ne puisse terminer la fusion. Regardons notre `git status` actuel :

```
(chapitre-3-collaboration)$ git status
On branch chapitre-3-collaboration
Your branch and 'origin/chapitre-3-collaboration' have diverged,
and have 1 and 1 different commits each, respectively.
  (use "git pull" to merge the remote branch into yours)

You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   chapitre-3.txt

no changes added to commit (use "git add" and/or "git commit -a")

```

Git nous dit que notre branche et la branche distante ont 1 commit différent l'une de l'autre. Il nous dit également que nous avons des "chemins non fusionnés" – que nous sommes actuellement en cours de fusion et que nous devons résoudre les conflits.

Il nous montre que `chapitre-3.txt` est actuellement modifié, alors regardons le contenu de `chapitre-3.txt` :

```
(chapitre-3-collaboration)$ cat chapitre-3.txt
<<<<<<< HEAD
Chapitre 3 - La Fin N'est Que Le Début
=======
Chapitre 3 - La Fin Mais Pas La Fin
>>>>>>> 2f6874f650a6a9d2b7ccefa7c9618deb1d45541e

Ceci est une phrase.

```

Git a ajouté des marqueurs au fichier pour nous montrer où le conflit s'est produit. Nous et notre coéquipier avons tous les deux modifié la phrase de titre, donc elle est entourée des marqueurs de conflit de Git : des flèches `<<<` et `>>>` séparées par une ligne de `===`.

La ligne du haut, signifiée par `<<<<<<< HEAD` et suivie de _"Chapitre 3 - La Fin N'est Que Le Début"_, est le changement que nous venons de faire. Git nous dit que cette ligne est là où notre `HEAD` actuel se trouve – c'est-à-dire, c'est le changement à notre commit actuel.

La ligne en dessous, _"Chapitre 3 - La Fin Mais Pas La Fin"_ suivie de `>>>>>>> 2f6874f650a6a9d2b7ccefa7c9618deb1d45541e`, est la ligne et le commit de notre coéquipier.

En gros, Git nous dit : "Laquelle de ces lignes (ou une combinaison de ces lignes) voulez-vous garder ?"

Remarquez que la ligne en bas du fichier n'est pas enveloppée dans les conflits – elle n'a pas été modifiée par les deux commits.

Nous devons résoudre le conflit en supprimant l'une des lignes ou en combinant les deux lignes en une seule (et n'oubliez pas de supprimer tous les marqueurs supplémentaires que Git a mis là aussi).

Je vais prendre une combinaison de ces lignes, donc le fichier final ressemble à ceci :

```
(chapitre-3-collaboration)$ cat chapitre-3.txt
Chapitre 3 - La Fin N'est Pas La Fin--Mais Seulement Le Début

Ceci est une phrase.

```

Pour terminer la fusion, nous devons simplement valider notre résolution de conflit :

```
(chapitre-3-collaboration)$ git add .
(chapitre-3-collaboration)$ git commit -m "Fusion du nouveau titre du coéquipier"
[chapitre-3-collaboration bd621aa] Fusion du nouveau titre du coéquipier

(chapitre-3-collaboration)$ git status
On branch chapitre-3-collaboration
Your branch is ahead of 'origin/chapitre-3-collaboration' by 2 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

```

Le résultat de `git status` nous indique que notre branche locale est `en avance de 2 commits sur 'origin/chapitre-3-collaboration'`.

Regarder le `git log` confirme cela :

```
commit bd621aa0e491a291af409283f5fd1f68407b94e0 (HEAD -> chapitre-3-collaboration)
Merge: 74ed9b0 2f6874f
Author: John Mosesman <johnmosesman@gmail.com>
Date:   Thu Mar 25 09:20:42 2021 -0500

    Fusion du nouveau titre du coéquipier

commit 74ed9b0d0d9154c912e1f194f04dbd6abea602e6
Author: John Mosesman <johnmosesman@gmail.com>
Date:   Thu Mar 25 09:02:03 2021 -0500

    Nouveau titre

commit 2f6874f650a6a9d2b7ccefa7c9618deb1d45541e (origin/chapitre-3-collaboration)
Author: John Mosesman <johnmosesman@gmail.com>
Date:   Thu Mar 25 08:58:58 2021 -0500

    Mise à jour du titre

...

```

L'historique des commits résultant contient les deux commits de la branche et notre commit de fusion en haut.

À partir de là, nous devons simplement pousser nos changements vers le distant :

```
(chapitre-3-collaboration)$ git push origin chapitre-3-collaboration
Enumerating objects: 10, done.
Counting objects: 100% (10/10), done.
Delta compression using up to 16 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (6/6), 647 bytes | 647.00 KiB/s, done.
Total 6 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 1 local object.
To github.com:johnmosesman/practical-git-tutorial.git
   2f6874f..bd621aa  chapitre-3-collaboration -> chapitre-3-collaboration

```

Maintenant que nous avons modifié la branche distante, notre coéquipier devrait faire un `git pull` pour fusionner nos nouveaux changements fusionnés.

Et, idéalement, nous devrions dire à notre coéquipier que nous avons poussé un nouveau changement afin qu'il puisse le tirer avant de continuer à éditer – réduisant ainsi la probabilité qu'il doive résoudre un conflit de fusion à l'avenir, également.

### Branches à partir de branches

Nous aurions également pu créer notre propre branche à partir de la branche `chapitre-3-collaboration`. Cela nous aurait permis de travailler sans avoir à nous soucier des conflits de fusion jusqu'à la toute fin.

Une fois que nous aurions terminé notre travail dans notre propre branche séparée, nous aurions pu fusionner _notre_ branche de fonctionnalité dans la branche de fonctionnalité de _notre coéquipier_ – et ensuite dans `main`.

> `chapitre-3-collaboration-john` -> `chapitre-3-collaboration` -> `main`

Comme vous pouvez le voir, la structure des branches peut devenir assez compliquée à mesure que de plus en plus de branches se ramifient les unes des autres et deviennent en avance ou en retard les unes par rapport aux autres.

Pour cette raison, il est généralement bon de garder les branches **petites et isolées** et d'essayer de **les fusionner rapidement et souvent**.

Cela peut aider à éviter beaucoup de conflits de fusion douloureux.

## Révision : comment démarrer un nouveau workflow de fonctionnalité

Je terminerai par un rapide récapitulatif de la manière d'aborder le démarrage d'une nouvelle tâche et des commandes et flux pour le faire.

Supposons que vous avez reçu votre premier ticket dans un nouvel emploi : un petit bug à corriger dans le produit de votre équipe.

La première chose que vous devriez faire est de télécharger le dépôt en utilisant `git clone <URL>`.

Ensuite, vous voudrez créer une branche de fonctionnalité à partir de `main` en utilisant `git checkout -b <NOM_DE_BRANCHE>`. Après cela, vous corrigez le bug et validez les changement(s) en utilisant `git add` et `git commit`.

Peut-être que la résolution de ce problème prend plusieurs commits – ou peut-être que vous faites quelques commits dans une tentative de le résoudre avant d'arriver enfin à la solution. C'est bien aussi.

Après avoir validé, vous poussez votre nouvelle branche vers `origin` (`git push origin <NOM_DE_BRANCHE>`) et créez une pull request. Après une révision de code, votre branche est fusionnée (youpi !).

Vous avez maintenant terminé votre fonctionnalité, et il est temps de revenir à `main` (en utilisant `git checkout main`), d'utiliser `git pull` pour obtenir vos derniers changements plus tous les autres changements que les autres ont faits, et de recommencer avec une nouvelle branche.

## Conclusion

Comme mentionné au début, il existe de nombreuses façons d'aborder le travail avec Git et les workflows Git.

Il y a aussi beaucoup de "magie" sous-jacente de Git (c'est-à-dire du code qui s'exécute que vous ne comprenez pas encore), mais vous apprendrez et en comprendrez davantage avec le temps.

J'ai passé les premières années de ma carrière à utiliser simplement des commandes et des workflows mémorisés. Cela a fonctionné. Au fur et à mesure que je rencontrais des problèmes ou que je collaborais avec des coéquipiers, j'ai appris davantage et finalement mes compétences avec Git se sont élargies.

Au début, ne le rendez pas plus difficile qu'il ne l'est ! Vous apprendrez avec le temps.

Si vous avez aimé cet article, j'écris sur des sujets techniques comme celui-ci ainsi que sur des sujets non techniques [sur mon site](https://johnmosesman.com/).

J'écris également des choses similaires sur Twitter : [@johnmosesman](https://twitter.com/johnmosesman).

Dans tous les cas, n'hésitez pas à m'envoyer un message.

Merci d'avoir lu !

John