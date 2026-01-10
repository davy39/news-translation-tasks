---
title: Améliorez le flux de développement de votre équipe avec les Githooks
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-15T16:06:01.000Z'
originalURL: https://freecodecamp.org/news/improve-development-workflow-of-your-team-with-githooks-9cda15377c3b
coverImage: https://cdn-media-1.freecodecamp.org/images/0*fzif-QPdioernqbi
tags:
- name: Git
  slug: git
- name: project management
  slug: project-management
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: workflow
  slug: workflow
seo_title: Améliorez le flux de développement de votre équipe avec les Githooks
seo_desc: 'By Daniel Deutsch

  Every product that is developed by more than one programmer needs to have some guidelines
  to harmonize the workflow.

  A standardized software development workflow between programmers allows, for example:


  faster engineering, since ea...'
---

Par Daniel Deutsch

Chaque produit développé par plus d'un programmeur doit avoir des directives pour harmoniser le flux de travail.

Un flux de travail standardisé pour le développement logiciel entre les programmeurs permet, par exemple :

* un développement plus rapide, car chaque développeur peut s'appuyer sur une activité habituelle
* moins d'erreurs, car le flux de travail lui-même doit être structuré de manière à éviter certaines erreurs
* une intégration facile des nouveaux membres
* un historique amélioré

Une fonctionnalité très facile à utiliser est celle des « [Githooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) » (si vous utilisez Git pour le contrôle de version).

Dans cet article, je souhaite montrer à quel point il est facile de mettre en place quelques directives de flux de travail avec les Githooks. Cela permettra à votre équipe d'être sur la même longueur d'onde lors du développement de logiciels.

### Table des matières

* [Pourquoi les Githooks ?](https://github.com/Createdd/Writing/blob/master/2018/articles/Githooks.md#pourquoi-les-githooks)
* [GitFlow et Checkout, Commit, Push](https://github.com/Createdd/Writing/blob/master/2018/articles/Githooks.md#gitflow-et-checkout-commit-push)
* [Post-checkout](https://github.com/Createdd/Writing/blob/master/2018/articles/Githooks.md#post-checkout)
* [Commit-msg](https://github.com/Createdd/Writing/blob/master/2018/articles/Githooks.md#commit-msg)
* [Pre-push](https://github.com/Createdd/Writing/blob/master/2018/articles/Githooks.md#pre-push)
* [« Appliquer » les hooks](https://github.com/Createdd/Writing/blob/master/2018/articles/Githooks.md#appliquer-les-hooks)
* [Résoudre un problème courant](https://github.com/Createdd/Writing/blob/master/2018/articles/Githooks.md#resoudre-un-probleme-courant)
* [Remerciements](https://github.com/Createdd/Writing/blob/master/2018/articles/Githooks.md#remerciements)

### Pourquoi les Githooks ?

Les Githooks sont, comme le suggère le mot, un hook pour les commandes [Git](https://git-scm.com/). Intuitivement, cela a du sens. Avec Git, vous gérez essentiellement le flux de travail d'un logiciel. Chaque branche fait partie de l'ensemble. Chaque commit est un bloc de construction d'une branche.

Ainsi, pour standardiser la qualité dans le développement logiciel, il faut standardiser les actions dans le processus de construction du produit.

Il existe de nombreuses commandes Git qui peuvent être hookées pour définir des standards. Rappelez-vous, il y en a assez :

* applypatch-msg
* pre-applypatch
* post-applypatch
* pre-commit
* prepare-commit-msg
* commit-msg
* post-commit
* pre-rebase
* post-checkout
* post-merge
* pre-receive
* pre-push
* update
* post-update
* pre-auto-gc
* post-rewrite

Pour établir un flux de travail amélioré, vous n'avez pas besoin d'utiliser toutes ces commandes. Concentrez-vous sur les quelques-unes importantes. Selon mon expérience jusqu'à présent, ce sont :

* commit-msg/pre-commit
* post-checkout
* pre-push

Permettez-moi d'expliquer pourquoi.

### GitFlow et Checkout, Commit, Push

L'utilisation de Git comme système de contrôle de version permet de définir un flux de travail. Je le fais en utilisant la [méthode GitFlow](https://datasift.github.io/gitflow/IntroducingGitFlow.html).

![Image](https://cdn-media-1.freecodecamp.org/images/0*f-3vMJcoDjKLJ3RJ)

Il s'agit essentiellement de développer un logiciel où chaque fonctionnalité est représentée par une branche.

Dans les exemples suivants, je vérifierai toujours la nomenclature avec des tests Regex ou j'exécuterai un autre script.

### Post-checkout

L'importance accrue d'une branche permet le premier hook sur « post-checkout ». Il est déclenché après la création d'une nouvelle branche avec Git.

Souvent, une convention de nommage est appliquée pour rendre les branches comparables et comprendre leur utilisation pour l'ensemble du produit.

Vous pouvez créer un simple script shell comme celui-ci pour garantir la nomenclature :

### Commit-msg

Dans le développement web, il existe plusieurs bibliothèques qui aident à configurer un hook pour les commits. Souvent, elles ne sont pas nécessaires, car des scripts simples peuvent également être écrits par vous-même.

Voir la validation d'un message git par exemple :

### Pre-push

« Git push » est le processus de « partage » de votre branche avec l'équipe. C'est souvent la dernière étape avant l'ouverture d'une pull-request pour une fusion avec la branche principale.

C'est un bon moment pour vérifier d'autres directives comme le « linting » du code, ou si tous les tests passent.

Un exemple d'exécution d'un autre script pourrait être :

### « Appliquer » les hooks

Une autre étape consiste à appliquer réellement ces hooks.

Dans JavaScript et les gestionnaires de paquets NPM/Yarn, il existe déjà un script « postinstall » intégré. Il permet l'exécution d'un script après le processus d'installation. Mais quoi exactement devrait être exécuté ?

Créez votre propre script d'installation ! Comme :

### Résoudre un problème courant

Un problème qui m'a laissé perplexe pendant un certain temps était que les hooks Git ne sont PAS exécutables par défaut. Cela signifie qu'ils doivent être rendus exécutables avec

`chmod +x <pathToHook>`

Voir la discussion StackOverflow [ici](https://stackoverflow.com/questions/8598639/why-is-my-git-pre-commit-hook-not-executable-by-default).

### Remerciements

J'espère que cela aidera certains d'entre vous à aligner le flux de travail de votre équipe de développement et à rendre la vie de chacun beaucoup plus facile. :-)

Merci d'avoir lu mon article ! N'hésitez pas à laisser vos commentaires !

Daniel est un développeur de logiciels, un étudiant en LL.M. en droit des affaires et organisateur d'événements liés à la technologie à Vienne. Ses efforts d'apprentissage personnel actuels se concentrent sur le machine learning.

Connectez-vous sur :

* [LinkedIn](https://www.linkedin.com/in/createdd)
* [Github](https://github.com/Createdd)
* [Medium](https://medium.com/@ddcreationstudi)
* [Twitter](https://twitter.com/_createdd)
* [Steemit](https://steemit.com/@createdd)
* [Hashnode](https://hashnode.com/@DDCreationStudio)