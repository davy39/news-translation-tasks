---
title: Apprenez à utiliser Git et GitHub – Un guide pour débutants
author: Sumit Saha
date: '2025-12-12T21:14:03.949Z'
originalURL: https://freecodecamp.org/news/learn-how-to-use-git-and-github-a-beginner-friendly-handbook
description: 'Dans ce guide, vous allez plonger dans un sujet passionnant : Git et
  GitHub. Pour commencer, clarifions une chose : Git et GitHub ne sont pas la même
  chose. En résumé, Git est l''outil qui s''exécute sur votre propre ordinateur et
  suit les modifications de vos fichiers...'
co_authors: []
series: null
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1765495440352/0eadf330-7a89-4328-aed1-3c851d279a5d.png
tags:
- name: GitHub
  slug: github
- name: Git
  slug: git
- name: Gitcommands
  slug: gitcommands
seo_desc: 'In this handbook, you’re going to dive into something really exciting:
  Git and GitHub.

  To start, let’s clear one thing up: Git and GitHub are not the same thing.

  In short, Git is the tool that runs on your own computer and keeps track of changes
  in y...'
---


Dans ce guide, vous allez plonger dans un sujet vraiment passionnant : Git et GitHub.

Pour commencer, clarifions une chose : Git et GitHub ne sont pas la même chose.

En résumé, Git est l'outil qui s'exécute sur votre propre ordinateur et suit les modifications de vos fichiers, tandis que GitHub est une plateforme en ligne qui vous permet de stocker ces projets Git dans le cloud et de collaborer avec d'autres personnes. Git fonctionne parfaitement seul, mais GitHub facilite grandement le travail d'équipe, le partage et la sauvegarde. Ils sont connectés, certes, mais complètement différents.

Voyez les choses ainsi : Git est le « café », et GitHub est le « café-restaurant » où ce café est servi. Analogie amusante, n'est-ce pas ? Ne vous inquiétez pas, vous verrez exactement ce que cela signifie dans un instant.

## Que fait Git ?

Commençons donc par comprendre ce qu'est réellement Git et comment il fonctionne. Pour faire simple, Git est un outil puissant qui suit constamment chaque modification que vous apportez à vos fichiers - et je veux dire *littéralement* tout le temps. Jour et nuit, 365 jours par an, Git enregistre ce qui a changé, quand cela a changé, qui l'a changé et même où cela s'est produit.

Maintenant, de quel type de fichiers parlons-nous ? De presque n'importe quel type – pas seulement du code. Il peut s'agir d'une image, d'un fichier texte, de JavaScript, PHP, Python ou même d'une vidéo. Peu importe ce sur quoi vous travaillez, Git suit chaque modification. C'est assez incroyable, n'est-ce pas ?

Mais voici la meilleure partie : la magie de Git ne s'arrête pas là. La chose la plus cool à propos de Git est qu'il enregistre différentes versions de vos fichiers. Imaginez que vous ayez écrit du code, puis que vous y ayez apporté quelques modifications après quelques jours. Vous voulez vous assurer que l'ancienne version ne soit pas perdue. C'est exactement là que Git vient à la rescousse. Il vous permet de conserver plusieurs versions du même fichier sans effort, et quand vous le souhaitez, vous pouvez revenir à n'importe quelle version précédente en un instant.

À la fin de ce guide, vous comprendrez non seulement ce que sont Git et GitHub, mais vous serez également capable de les utiliser en toute confiance dans des projets réels. Vous apprendrez comment Git suit les modifications localement, comment fonctionnent les dépôts (repositories), comment faire progresser les modifications dans le flux de travail de Git et comment collaborer avec d'autres en utilisant GitHub.

Nous partirons des bases fondamentales pour passer progressivement à des concepts plus avancés comme les branches, la fusion (merging), la résolution de conflits et l'annulation sécurisée d'erreurs – le tout avec des exemples pratiques que vous pourrez suivre.

## Voici ce que nous allons aborder :

1. [Prérequis](#heading-prerequis)
    
2. [Qu'est-ce que Git](#heading-qu-est-ce-que-git) ?
    
    * [Git vs GitHub](#heading-git-vs-github)
        
3. [Architecture Git – Locale et Distante](#heading-architecture-git-locale-et-distante)
    
4. [Comment installer Git sur votre ordinateur](#heading-comment-installer-git-sur-votre-ordinateur)
    
5. [Comment créer un projet et initialiser un dépôt local](#heading-comment-creer-un-projet-et-initialiser-un-depot-local)
    
6. [Comment créer un dépôt distant sur GitHub et le cloner](#heading-comment-creer-un-depot-distant-sur-github-et-le-cloner)
    
7. [Comment suivre les modifications avec `git status`](#heading-comment-suivre-les-modifications-avec-git-status)
    
8. [Comment déplacer les modifications vers la zone de transit avec `git add`](#heading-comment-deplacer-les-modifications-vers-la-zone-de-transit-staging-area-avec-git-add)
    
9. [Comment enregistrer le travail de manière permanente avec `git commit` (et configurer Git)](#heading-comment-enregistrer-le-travail-de-maniere-permanente-avec-git-commit-et-configurer-git)
    
10. [Comment supprimer et restaurer des fichiers avec `git rm` et `git reset`](#heading-comment-supprimer-et-restaurer-des-fichiers-avec-git-rm-et-git-reset)
    
11. [Comment consulter l'historique des commits avec `git log`](#heading-comment-consulter-l-historique-des-commits-avec-git-log)
    
12. [Branches et fusions dans Git](#heading-branches-et-fusions-merging-dans-git)
    
    * [Comprendre les conflits de fusion](#heading-comprendre-les-conflits-de-fusion-merge-conflicts)
        
13. [Comment naviguer dans l'historique avec `git checkout` et comparer les commits avec `git diff`](#heading-comment-naviguer-dans-l-historique-avec-git-checkout-et-comparer-les-commits-avec-git-diff)
    
14. [Comment travailler avec les dépôts distants : `git push`, `git fetch` et `git pull`](#heading-comment-travailler-avec-les-depots-distants-git-push-git-fetch-et-git-pull)
    
    * [Exemple – `git push`](#heading-exemple-git-push)
        
    * [Exemple – Pousser d'autres branches](#heading-exemple-pousser-d-autres-branches)
        
    * [Exemple – `git fetch`](#heading-exemple-git-fetch)
        
    * [Exemple – `git pull`](#heading-exemple-git-pull)
        
15. [Comment annuler les modifications locales avec `git restore`](#heading-comment-annuler-les-modifications-locales-avec-git-restore)
    
16. [Comment mettre temporairement le travail de côté avec `git stash`](#heading-comment-mettre-temporairement-le-travail-de-cote-avec-git-stash)
    
17. [Comment annuler des commits en toute sécurité avec `git revert`](#heading-comment-annuler-des-commits-en-toute-securite-avec-git-revert)
    
18. [Comment garder un historique propre avec `git rebase`](#heading-comment-garder-un-historique-propre-avec-git-rebase)
    
19. [Comment collaborer sur GitHub avec les Pull Requests](#heading-comment-collaborer-sur-github-avec-les-pull-requests)
    
20. [Git & GitHub – Résumé concis](#heading-git-github-resume-concis)
    
    * [Git vs GitHub](#heading-git-vs-github)
        
    * [Architecture et flux de travail Git de base](#heading-architecture-et-flux-de-travail-workflow-git-de-base)
        
    * [Pour commencer](#heading-pour-commencer)
        
    * [Visualiser et déplacer les modifications](#heading-visualiser-et-deplacer-les-modifications)
        
    * [Suppression, restauration et annulation](#heading-suppression-restauration-et-annulation)
        
    * [Branches, fusions et conflits](#heading-branches-fusions-et-conflits)
        
    * [Navigation et comparaison de l'historique](#heading-navigation-et-comparaison-de-l-historique)
        
    * [Travailler avec les dépôts distants (GitHub)](#heading-travailler-avec-les-depots-distants-github)
        
    * [Mettre temporairement le travail de côté avec git stash](#heading-mettre-temporairement-le-travail-de-cote-avec-git-stash-1)
        
    * [Garder un historique propre avec git rebase](#heading-garder-un-historique-propre-avec-git-rebase-1)
        
    * [Collaboration avec les Pull Requests (PR)](#heading-collaboration-avec-les-pull-requests-pr)
        
    * [Ce qu'il faut retenir](#heading-ce-qu-il-faut-retenir)
        
21. [Le mot de la fin](#heading-le-mot-de-la-fin)
    

## Prérequis

* **Navigation de base dans les fichiers et dossiers** – Utilisation du Finder / Explorateur de fichiers.
    
* **Utilisation de la CLI** – Exécution de commandes simples dans le Terminal ou l'Invite de commandes.
    
* **Éditeur de texte** – N'importe quel éditeur pour ouvrir et modifier des fichiers.
    

J'ai également créé une vidéo pour accompagner cet article. Si vous préférez apprendre par la vidéo autant que par le texte, vous pouvez la consulter ci-dessous :

%[https://www.youtube.com/watch?v=wNrbaAGE2PY] 

## Qu'est-ce que Git ?

Git est le plus souvent utilisé dans les projets de codage, mais sa puissance va bien au-delà du simple code. Vous pouvez utiliser Git pour suivre les modifications et maintenir différentes versions de presque n'importe quel fichier. Cela signifie que vous n'avez jamais à vous soucier de perdre un fichier ou d'écraser accidentellement quelque chose d'important.

Prenons un exemple concret. Supposons que vous travailliez sur un projet. Vous avez passé des heures à écrire du code, votre client l'adore et tout se passe bien. Puis, un mois plus tard, le client demande de nouvelles modifications. Vous effectuez les mises à jour demandées. Mais après quelques jours, le client revient et dit : « En fait, l'ancienne version était meilleure. » Vous voilà dans l'embarras, n'est-ce pas ? Parce que vous avez déjà écrasé le code original. Comment le récupérer ?

C'est exactement le genre de problème que Git résout. C'est pourquoi Git est connu sous le nom de Système de Contrôle de Version (Version Control System) – il conserve chaque version de vos fichiers ou de votre code stockée en toute sécurité, afin que vous puissiez revenir à n'importe quel état précédent dès que vous en avez besoin, sans rien perdre.

Git a été créé par Linus Torvalds – le même esprit brillant derrière Linux. Et honnêtement, ce qu'il a construit est tout simplement génial. La plupart des