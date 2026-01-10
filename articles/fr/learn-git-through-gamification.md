---
title: Apprendre Git à travers la Gamification – Un Guide Visuel des Concepts Clés
  de Contrôle de Version
subtitle: ''
author: Jacob Stopak
co_authors: []
series: null
date: '2025-03-02T06:00:00.000Z'
originalURL: https://freecodecamp.org/news/learn-git-through-gamification
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1740686401633/ffd9ac3c-668a-47bf-b2ba-f7cee14e74a8.webp
tags:
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: 'gamification '
  slug: gamification
- name: coding
  slug: coding
- name: learn coding
  slug: learn-coding
- name: Python
  slug: python
- name: visualization
  slug: visualization
- name: version control
  slug: version-control
seo_title: Apprendre Git à travers la Gamification – Un Guide Visuel des Concepts
  Clés de Contrôle de Version
seo_desc: Git has many concepts and commands that you’ll need to understand before
  you feel confident using it. Some of these concepts may sound trivial, especially
  to someone who has worked with Git before. But like most Git and coding concepts,
  even the “sim...
---

Git possède de nombreux concepts et commandes que vous devrez comprendre avant de vous sentir à l'aise avec son utilisation. Certains de ces concepts peuvent sembler triviaux, surtout pour quelqu'un qui a déjà travaillé avec Git. Mais comme la plupart des concepts Git et de codage, même les plus "simples" ont tendance à être abstraits.

Les trois concepts qui se démarquent pour moi comme les plus fondamentaux pour pouvoir travailler efficacement avec Git à un niveau basique sont :

1. Le **répertoire de travail**
    
2. La **zone de staging**
    
3. L'**historique des commits**
    

Dans cet article, nous allons adopter une nouvelle approche pour représenter ces trois concepts : en *les visualisant dans un monde de jeu immersif en 3D !*

Je vais fournir une représentation visuelle et tangible de ces concepts clés de Git, qui sont presque toujours décrits de manière abstraite et confuse. J'espère que cela les rendra beaucoup plus intuitifs pour vous.

## Table des Matières

1. [Visualisez votre Répertoire de Travail](#heading-visualisez-votre-repertoire-de-travail)
    
2. [Démystifiez votre Zone de Staging](#heading-demystifiez-votre-zone-de-staging)
    
3. [Parcourez Littéralement votre Historique de Commits](#heading-parcourez-litteralement-votre-historique-de-commits)
    
4. [Résumé](#heading-resume)
    
5. [Essayez par Vous-même](#heading-essayez-par-vous-meme)
    

## Visualisez votre Répertoire de Travail

Que voit votre cerveau lorsque vous pensez au "répertoire de travail" ? Je suppose que c'est quelque chose comme une structure de dossiers commençant à la racine du projet, contenant les fichiers de code et les sous-dossiers qui composent le projet.

Bien que ce soit une description juste du répertoire de travail, c'est un peu difficile à imaginer et cela manque la segmentation que Git applique à votre projet. Bien que l'état actuel de votre projet entier, de la structure des dossiers et des fichiers de code réside dans le répertoire de travail, Git n'a pas vraiment besoin de faire grand-chose à ce sujet à moins que certains *changements* ne soient détectés dans ces fichiers.

Git détecte et signale les changements dans le répertoire de travail avec la [commande Git status](https://initialcommit.com/blog/git-status), qui montre une sortie comme ceci :

```bash
Jack@RAPTOR ~/my-project (main)> git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   main.py
        modified:   settings.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        one.py
        three.py
        two.py

no changes added to commit (use "git add" and/or "git commit -a")
```

Les deux sections pertinentes ici sont :

1. **Changes not staged for commit** : Liste les fichiers existants suivis par Git qui contiennent actuellement des changements de code. Dans l'exemple ci-dessus, nous voyons deux fichiers "modifiés" : `main.py` et `settings.py`.
    
2. **Untracked files** : Liste les nouveaux fichiers dans votre projet que Git ne connaît pas encore. Dans l'exemple ci-dessus, nous voyons trois nouveaux fichiers non suivis : `one.py`, `two.py` et `three.py`.
    

En ce qui concerne la compréhension de Git, penser au répertoire de travail comme les changements que Git voit dans ces deux sections – **Untracked files** et **Modified files** – est assez utile.

Mais la commande `git status` rapporte ces détails dans le terminal de manière purement textuelle, ce qui ne facilite pas la compréhension de Git pour les nouveaux utilisateurs.

Certaines interfaces graphiques de Git font un meilleur travail avec cela (elles fournissent une interface plus sûre de type point-and-click, après tout), mais selon mon expérience, aucune d'entre elles ne rend les choses *évidentes au premier coup d'œil*.

Au lieu de cela, imaginez que, en tant que nouvel utilisateur de Git, vous voyiez ceci :

[![Image capturée depuis Devlands, l'interface et le tutoriel gamifiés de Git, montrant les sections des fichiers non suivis et des fichiers modifiés du mur du répertoire de travail](https://cdn.hashnode.com/res/hashnode/image/upload/v1740587730262/375bef09-b8b8-43e3-a18c-5b1e589b6097.png align="center")](https://devlands.com)

Un grand mur avec des sections clairement délimitées pour les **fichiers non suivis** et les **fichiers modifiés**. Les fichiers correspondant à chaque section sont représentés comme des blocs sur le mur dans cette section, clairement étiquetés avec leur nom de fichier.

Plus spécifiquement, les blocs représentant les fichiers `one.py`, `two.py` et `three.py` sont tous bien rangés dans la section **fichiers non suivis**, et les blocs représentant les fichiers `main.py` et `settings.py` sont dans la section **fichiers modifiés**.

Cela rend parfaitement clair, même pour un novice complet, que Git interprète ces fichiers différemment et les catégorise de manière logique. Cela transforme le concept abstrait de Git du "répertoire de travail" en une forme que presque tout le monde peut comprendre au premier coup d'œil.

Mais quelque chose manque ici. Supposons que vous exécutiez la commande `git add one.py`. Cela met en stage le fichier non suivi `one.py` pour être inclus dans le prochain commit. Que se passe-t-il avec le bloc étiqueté `one.py` sur le mur ?

## Démystifiez votre Zone de Staging

Pour répondre à cela, passons à la mystérieuse [zone de "staging" de Git](https://initialcommit.com/blog/git-add). Mais d'abord, où se trouve exactement la zone de staging ?

Eh bien, techniquement, tout changement de fichier mis en stage est toujours dans le répertoire de travail, ce qui rend les choses un peu confuses.

Voici comment Git rapporte cela dans le terminal :

```bash
Jack@RAPTOR ~/D/git-worlds (main)> git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   one.py
```

Comme vous pouvez le voir à partir de la sortie de Git, elle inclut maintenant la section **Changes to be committed**, qui contient le fichier `one.py` qui a été mis en stage avec la commande `git add`.

Mais cela reste un peu flou. Les changements de fichier mis en stage dans `one.py` font-ils toujours partie du répertoire de travail ? Ou Git les stocke-t-il ailleurs ?

Eh bien, la réponse est... LES DEUX :

[![Image capturée depuis Devlands, l'interface et le tutoriel gamifiés de Git, ajoutant la section des fichiers mis en stage sur le mur du répertoire de travail](https://cdn.hashnode.com/res/hashnode/image/upload/v1740592262850/dc65c06d-0ec6-4de6-bbe9-53307d523e68.png align="center")](https://devlands.com)

Ici, vous pouvez voir que nous avons un peu zoomé par rapport à l'image précédente, pour révéler une troisième section du mur étiquetée **Fichiers mis en stage**.

Puisque nous avons exécuté la commande `git add one.py`, vous pouvez voir que le bloc correspondant représentant le fichier `one.py` s'est déplacé de la colonne des fichiers non suivis à la colonne des fichiers mis en stage.

Cela montre clairement qu'un fichier situé dans la zone de staging fait toujours partie du répertoire de travail (parce qu'il fait partie du mur global), tout en étant segmenté dans son propre espace désigné.

D'un point de vue technique, la zone de staging de Git est simplement un fichier nommé **index** qui réside dans le dossier `.git/`. Git construit les changements de code spécifiés par la commande `git add` dans ce fichier, qui est utilisé comme source pour ces changements la prochaine fois que la commande `git commit` est exécutée.

Mais d'un point de vue de flux de travail, représenter la zone de staging comme une section sur le "mur du répertoire de travail" comme dans l'image ci-dessus rend les choses plus intuitives à comprendre.

Ensuite, explorons comment nous pourrions visualiser les choses une fois que les changements mis en stage sont transformés en un nouveau commit Git et deviennent une partie de la branche active.

## Parcourez Littéralement votre Historique de Commits

Que voit votre œil mental lorsque vous pensez à l'"historique des commits" de Git ?

Eh bien, la plus belle façon dont Git le fait dans le terminal est en utilisant la [commande Git log](https://initialcommit.com/blog/git-log), comme `git log --graph --all`, qui fournit une sortie comme :

```bash
* commit 88085cff3e2d7657f26eb6479b308526df7d2bba (HEAD -> dev, origin/dev)
| Author: Jacob Stopak <jacob@initialcommit.io>
| Date:   Tue Apr 23 20:31:24 2024 -0700
|
|     Fix command as title clip, ellipses and arrow length in rebase subcommand
|
|     Signed-off-by: Jacob Stopak <jacob@initialcommit.io>
|
*   commit e264605ea26a808c34d4dc2fbc6dad65a8e28c5f
|\  Merge: cb3fa5f b8c071c
| | Author: Jacob Stopak <jacob@initialcommit.io>
| | Date:   Wed Mar 20 19:51:06 2024 -0700
| |
| |     Merge branch 'main' into dev
| |
* | commit cb3fa5f3bdbdcff3d9a8c844cda99d46bf64e337
| | Author: Jacob Stopak <jacob@initialcommit.io>
| | Date:   Sat Mar 9 22:00:49 2024 -0800
| |
| |     Add --staged flag to git restore subcommand
| |
| |     Signed-off-by: Jacob Stopak <jacob@initialcommit.io>
| |
| * commit b8c071cb9a1653748525aa01c2b6bafe06ed9100
|/  Author: Jacob Stopak <jacob@initialcommit.io>
|   Date:   Wed Mar 20 19:50:53 2024 -0700
|
|       Correct license specified in pyproject.toml from MIT to GNU GPLv2
|
|       Signed-off-by: Jacob Stopak <jacob@initialcommit.io>
|
* commit 32a3a3fca583f6c68225b974716e74b557a1a094
| Author: Jacob Stopak <49353917+initialcommit-io@users.noreply.github.com>
| Date:   Tue Aug 22 11:31:38 2023 -0700
|
|     Update README.md
```

Malheureusement, ce n'est pas très joli du tout. Cette longue liste embrouillée d'IDs de commit, de noms, de dates et de messages de commit n'est définitivement pas quelque chose que la plupart des gens considéreraient comme convivial.

L'option `--graph` fournie ci-dessus montre les relations entre les commits en dessinant de petites lignes reliant chaque commit dans le terminal, mais la nature purement textuelle de cela n'est tout simplement pas intuitive pour la plupart des gens au premier coup d'œil.

Maintenant, considérons la représentation gamifiée suivante de l'historique des commits de Git :

[![Image capturée depuis Devlands, l'interface et le tutoriel gamifiés de Git, montrant l'historique des commits et les branches du projet](https://cdn.hashnode.com/res/hashnode/image/upload/v1740594184258/8d5a33c8-ad60-4496-a50d-a27fc6b8e752.png align="center")](https://devlands.com)

Maintenant, nous parlons ! Dans cette image, chaque commit Git est représenté par un bloc blanc avec un ID de commit raccourci à 6 caractères.

Chaque bloc de commit blanc pointe vers son commit parent avec une flèche, formant des chaînes très claires de commits qui constituent les branches Git.

Vous avez peut-être remarqué que certains des blocs de commit blancs ont des blocs colorés posés dessus. Les blocs verts sont des [noms de branches](https://initialcommit.com/blog/git-branches), les blocs jaunes sont des [tags Git](https://initialcommit.com/blog/git-tag), le bloc bleu est le [pointeur HEAD de Git](https://initialcommit.com/blog/what-is-git-head), et les blocs rouges sont des branches de suivi à distance. Ceux-ci sont collectivement appelés [références Git](https://initialcommit.com/blog/what-is-git-head#git-refs-and-heads).

En plus de pouvoir facilement les distinguer, représenter les types de références comme des blocs de couleurs différentes clarifie un autre concept Git souvent confus. Dans Git, les branches (ainsi que d'autres types de références) ne sont que des "pointeurs" vers un commit spécifique. Il est tentant de penser à une branche comme une série de commits connectés qui partagent une histoire – et conceptuellement, cela est correct – mais dans Git, une branche est vraiment juste une étiquette glorifiée pointant vers un commit spécifique.

Dans ce monde gamifié, vous pouvez *littéralement parcourir votre historique de commits* pour voir, interagir avec et examiner les changements de code dans n'importe quel commit.

## Résumé

Dans cet article, nous avons exploré comment les concepts fondamentaux de Git – le répertoire de travail, la zone de staging et l'historique des commits – peuvent être difficiles à comprendre en raison de leur nature abstraite.

Pour rendre ces concepts plus accessibles, nous avons introduit une approche visuelle et gamifiée qui les transforme en quelque chose de tangible : un monde de jeu immersif où les fichiers et les commits sont représentés comme des blocs interactifs.

En présentant Git de cette manière, les codeurs débutants, les étudiants et les développeurs de tous niveaux d'expérience peuvent apprendre intuitivement les concepts et les commandes de Git, et les appliquer en toute confiance dans des projets professionnels.

## Essayez par Vous-même

Les images de cet article ont été capturées dans [Devlands](https://devlands.com), la première et seule *interface et tutoriel gamifiés de Git*, que je développe en Python.

Dans Devlands, non seulement vous pouvez parcourir votre base de code... Vous pouvez également apprendre les concepts et les commandes de Git avec un tutoriel guidé par un personnage, simuler et exécuter des commandes Git directement dans le jeu, voir leurs résultats appliqués dans le monde du jeu en temps réel, et utiliser l'IA pour expliquer le code que vous ne comprenez pas.

Si vous ou quelqu'un que vous connaissez êtes un apprenant visuel, un codeur débutant ou un nouvel utilisateur de Git, [pensez à le vérifier !](https://devlands.com)