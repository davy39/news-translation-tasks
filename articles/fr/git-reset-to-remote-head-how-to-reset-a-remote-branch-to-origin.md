---
title: Git Reset to Remote Head – Comment réinitialiser une branche distante vers
  Origin
subtitle: ''
author: Bolaji Ayodeji
co_authors: []
series: null
date: '2021-03-08T20:14:39.000Z'
originalURL: https://freecodecamp.org/news/git-reset-to-remote-head-how-to-reset-a-remote-branch-to-origin
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/article-banner--1-.png
tags:
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: version control
  slug: version-control
seo_title: Git Reset to Remote Head – Comment réinitialiser une branche distante vers
  Origin
seo_desc: 'Branching is a core concept in Git. It can help you set up a distributed
  workflow for team collaboration and makes your development process more efficient.

  When you''re using version control and you''re distributing features across branches,
  there''s a ...'
---

Le branchement est un concept central dans Git. Il peut vous aider à configurer un flux de travail distribué pour la collaboration en équipe et rendre votre processus de développement plus efficace.

Lorsque vous utilisez le contrôle de version et que vous distribuez des fonctionnalités sur différentes branches, il y a beaucoup de communication entre votre ordinateur local et votre dépôt en ligne sur GitHub. Pendant ce processus, vous pourriez avoir besoin de réinitialiser votre copie locale à l'original du projet.

Si la réinitialisation d'une branche vous effraie, ne vous inquiétez pas – cet article vous présentera les branches distantes, le remote head, et comment vous pouvez facilement réinitialiser une branche distante vers le remote head.

## **Prérequis**

* Connaissance de base de l'utilisation du terminal.

* Git installé (Apprenez [comment installer Git ici](https://www.freecodecamp.org/news/git-clone-branch-how-to-clone-a-specific-branch/#how-to-install-git-on-windows) si ce n'est pas déjà fait).

* Connaissance de base de GitHub et des dépôts.

* Un sourire sur le visage. 😉

## Qu'est-ce qu'une branche dans Git ?

Une branche est un concept central dans Git et GitHub que vous utiliserez tout le temps. Les branches vous aident à gérer différentes versions d'un même projet.

La branche `main` est toujours la branche par défaut dans un dépôt et est considérée comme du « code de production et déployable ». Vous pouvez créer de nouvelles branches comme `prod-staging` ou `prod-current` à partir de la branche `main`.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-27-at-7.19.26-PM.png align="left")

*Toutes les branches dans https://github.com/freeCodeCamp/freeCodeCamp*

### Qu'est-ce qu'une branche distante dans Git ?

Une **branche distante** est une référence à l'état des branches dans un dépôt distant (une version de votre projet hébergée sur Internet ou sur un réseau comme GitHub).

Lorsque vous clonez un dépôt, vous récupérez des données depuis un dépôt sur Internet ou un serveur interne connu sous le nom de **distant** (cela ressemble à quelque chose comme `(distant)/(branche)`).

## Qu'est-ce qu'Origin (ou Remote Head) dans Git ?

Le mot origin est un alias que Git a créé pour remplacer l'URL distante d'un dépôt distant. Il représente la branche par défaut sur un dépôt distant et est une référence locale représentant une copie locale du HEAD dans le dépôt distant.

En résumé, origin/HEAD représente la branche par défaut sur le dépôt distant, qui est définie automatiquement lorsque vous clonez un dépôt depuis Internet.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-08-at-8.23.47-AM.png align="left")

## Comment réinitialiser une branche distante vers Origin dans Git

Maintenant que vous avez des connaissances de base sur le fonctionnement des dépôts distants et des branches, résolvons notre problème et réinitialisons une branche distante vers origin en utilisant la commande `git reset --hard`.

Avant de faire cela (si c'est votre première fois), assurez-vous de sauvegarder votre branche avant de la réinitialiser au cas où quelque chose se passerait mal. Vous pouvez la sauvegarder comme suit :

```bash
git commit -a -m "Sauvegarde de la branche"
git branch sauvegarde-branche
```

Exécutez maintenant la commande ci-dessous pour réinitialiser votre branche distante vers origin. Si vous avez un dépôt distant et un nom de branche par défaut différents (différents de `origin` ou `main`, respectivement), remplacez-les simplement par le nom approprié.

```bash
git fetch origin
git reset --hard origin/main
```

Si vous avez créé de nouveaux fichiers ou répertoires, ils peuvent subsister après la réinitialisation. Vous pouvez utiliser la commande ci-dessous pour nettoyer l'arborescence de travail en supprimant récursivement les fichiers de la branche précédente qui ne sont pas sous contrôle de version.

```python
git clean -xdf
```

* Le drapeau `-x` supprime tous les fichiers non suivis, y compris les répertoires de build ignorés.

* Le drapeau `-d` permet à Git de parcourir récursivement les répertoires non suivis lorsqu'aucun chemin n'est spécifié.

* Le drapeau `-f` écrase la configuration par défaut de Git clean et commence à nettoyer les fichiers et répertoires non suivis.

## Conclusion

Si le nom de votre dépôt distant n'est pas « origin » et que le nom de la branche n'est pas « main » dans le dépôt distant, n'oubliez pas de mettre à jour les commandes ci-dessus avec les noms appropriés. Vous pouvez toujours exécuter `git remote show origin` pour vérifier cela.

J'espère que cet article vous a rendu plus à l'aise pour travailler avec et réinitialiser des branches. Vous devriez également rejoindre le nouveau [serveur de chat freeCodeCamp](https://www.freecodecamp.org/news/introducing-freecodecamp-chat) pour échanger avec d'autres apprenants et poser des questions. Merci d'avoir lu ! 💙