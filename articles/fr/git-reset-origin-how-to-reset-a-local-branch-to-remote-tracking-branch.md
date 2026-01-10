---
title: Git Reset Origin – Comment réinitialiser une branche locale à une branche de
  suivi à distance
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-06-22T18:03:49.000Z'
originalURL: https://freecodecamp.org/news/git-reset-origin-how-to-reset-a-local-branch-to-remote-tracking-branch
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/tanner-van-dera-oaQ2mTeaP7o-unsplash.jpg
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: Git Reset Origin – Comment réinitialiser une branche locale à une branche
  de suivi à distance
seo_desc: 'Git is a free and open-source version control system. It is the most popular
  version control system in use today.

  Git keeps track of the changes made to a project over time. This allows multiple
  developers to collaborate and work on the same project ...'
---

Git est un système de contrôle de version gratuit et open-source. C'est le système de contrôle de version le plus populaire utilisé aujourd'hui.

Git suit les changements apportés à un projet au fil du temps. Cela permet à plusieurs développeurs de collaborer et de travailler sur le même projet en parallèle, peu importe où ils se trouvent dans le monde.

Il permet aux développeurs de consulter l'historique du projet et de voir qui a fait quels changements et pourquoi ces changements ont été faits en premier lieu. De plus, avec Git, vous pouvez revenir à une version plus ancienne du code si nécessaire.

Essentiellement, Git garantit que les développeurs sont tous sur la même page et savent ce qui se passe dans le projet.

Lorsqu'on travaille sur un projet, l'un des défis auxquels vous pourriez être confronté est d'essayer de synchroniser votre travail - spécifiquement, synchroniser les branches locales et distantes.

Dans cet article, vous apprendrez comment réinitialiser et faire correspondre exactement une branche locale Git à une branche distante.

Voici ce que nous allons couvrir :

1. [Qu'est-ce qu'une branche dans Git ?](#intro)
    1. [Quelle est la différence entre les branches locales, distantes et de suivi à distance ?](#difference)
2. [Comment réinitialiser une branche locale Git à une branche distante ?](#reset)
    1. [Sauvegarder l'état actuel de votre branche locale](#save)
    2. [Faire un `git checkout`](#checkout)
    3. [Récupérer l'origine](#fetch)
    4. [Réinitialiser le dépôt local](#reset-local)
    5. [Nettoyer les changements non suivis](#clean)
3. [Conclusion](#conclusion)

## Qu'est-ce qu'une branche dans Git ? Les branches Git en bref pour les débutants <a name="intro"></a>

Le branchement est un aspect central du contrôle de version et un concept important à apprendre.

Grâce au branchement, les développeurs sont capables de collaborer de manière plus flexible. Le branchement rend le processus de développement quotidien plus fluide et plus efficace.

Le branchement est un moyen de gérer différentes versions de votre code et agit comme un pointeur vers un instantané de vos changements.

Lorsque vous créez pour la première fois un dépôt Git pour votre projet, au même moment, la **branche principale** est également créée.

La branche principale est la branche primaire et par défaut pour votre projet. Elle représente la version stable, sans bug et utilisable de votre code, prête à être publiée et partagée avec le public. C'est la base de code principale.

Mais que se passe-t-il lorsque vous voulez ajouter une nouvelle fonctionnalité à votre projet ?

Avant de l'ajouter, vous devez la tester et vous assurer qu'elle n'introduit pas de nouveaux bugs ou n'interfère pas avec le code existant.

Il doit y avoir un moyen de travailler sur la nouvelle fonctionnalité sans affecter la base de code.

Et c'est là que le branchement devient pratique.

Les branches sont des espaces isolés pour expérimenter et tester du nouveau code sans affecter le code de la branche principale.

Vous pouvez créer une nouvelle branche et apporter les modifications que vous souhaitez. Si vous êtes satisfait des modifications, vous pouvez les ajouter à la branche principale en les *fusionnant*. Si vous ne l'êtes pas, vous pouvez supprimer cette branche sans toucher au code principal du projet.

Les branches permettent également aux développeurs de travailler sur différentes fonctionnalités en même temps sans interférer avec le travail des autres.

Pour en savoir plus sur les branches dans Git, consultez [cette vidéo](https://www.youtube.com/watch?v=e2IbNHi4uCI) qui explique comment elles fonctionnent, et marquez [cet article](https://www.freecodecamp.org/news/how-to-use-branches-in-git/) qui fournit une feuille de triche sur la façon de les utiliser.

### Branches locales VS distantes VS de suivi à distance dans Git - Quelle est la différence ? <a name="difference"></a>

Une **branche locale** est une branche qui est accessible uniquement sur votre machine locale et existe là en isolation. À partir de là, vous pouvez ajouter des fichiers et valider les modifications que vous apportez. Ces modifications seront enregistrées localement et ne seront visibles que par vous et disponibles sur votre machine physique locale.

Les autres développeurs ne pourront pas voir votre travail et les modifications que vous avez apportées.

Vous pouvez créer une branche locale nommée `my_branch` en utilisant la commande suivante :

```bash
git branch my_branch
```

Et pour lister toutes vos branches locales, vous utilisez la commande `git branch`.

Pour collaborer avec d'autres développeurs sur le même projet et pour qu'ils voient les modifications que vous apportez, vous devez pousser les modifications de votre branche locale vers un dépôt distant.

Cela nous amène aux **branches distantes**.

Une branche distante fait référence à une branche qui existe dans un dépôt distant.

Un dépôt distant, également appelé distant, sera généralement un dépôt hébergé quelque part sur Internet, dans un emplacement distant tel que sur les serveurs GitHub. Le nom par défaut d'un dépôt distant est `origin`.

Maintenant, une **branche de suivi à distance** fait référence à une référence locale de l'état de la branche distante. Par défaut, les branches n'ont pas de connexion entre elles. Cela dit, vous pouvez dire à une branche locale de suivre une branche distante.

## Comment réinitialiser une branche locale Git à une branche distante ? <a name="reset"></a>

Vous avez peut-être travaillé sur votre branche locale, apportant diverses modifications à un projet, et vous avez conclu que ces modifications que vous avez apportées ne sont plus nécessaires.

Vous voulez les supprimer et réinitialiser la branche à la branche distante.

En plus de cela, un autre développeur a peut-être apporté des modifications et les a poussées vers la branche distante, donc vous devez récupérer ces dernières modifications du dépôt distant pour être à jour.

Les étapes que vous devez suivre pour y parvenir sont les suivantes :

- Sauvegarder l'état actuel de votre branche locale (facultatif).
- Récupérer la dernière version du code depuis le dépôt distant.
- Réinitialiser la branche locale.
- Nettoyer les fichiers (facultatif).

### Sauvegarder l'état actuel de votre branche locale <a name="save"></a>

Avant de commencer, vous pouvez vouloir sauvegarder l'état de votre branche actuelle dans une autre branche.

Lors de la réinitialisation d'une branche locale Git à une branche distante, vous perdrez les modifications que vous avez apportées localement.

Cette étape est facultative, et vous pouvez choisir de la faire au cas où quelque chose se passerait mal ou si vous souhaitez revenir à ce travail à l'avenir.

Pour sauvegarder le travail, utilisez les commandes suivantes :

```bash
git commit -a -m "Je sauvegarde mon travail"
git branch backup_work
```

Votre travail est maintenant sauvegardé dans la branche nommée `backup_work`.

### Faire un `git checkout` <a name="checkout"></a>

Typiquement, il y aura une branche de suivi à distance locale avec le même nom que la branche distante à laquelle vous voulez réinitialiser, comme `main`.

Utilisez la commande suivante pour basculer vers la branche principale de suivi à distance locale :

```bash
git checkout main
```

Si vous utilisez un nom différent pour cette branche, remplacez `main` par le nom que vous utilisez.

### Récupérer l'origine <a name="fetch"></a>

Pour récupérer le dépôt distant, et le dernier état et version du code dans le dépôt distant, entrez la commande suivante :

```bash
git fetch origin
```

`origin` est un alias créé par Git et spécifie l'URL distante du dépôt distant. Habituellement, Git suppose automatiquement que le nom du dépôt distant est `origin`.

Si vous avez un nom de dépôt distant différent, remplacez `origin` par le nom que vous utilisez.

### Réinitialiser le dépôt local <a name="reset-local"></a>

Maintenant, réinitialisez la branche locale `main` au dépôt distant en utilisant la commande suivante :

```bash
git reset --hard origin/main
```

### Nettoyer les changements non suivis <a name="clean"></a>

Cette étape est facultative.

Après avoir utilisé les commandes ci-dessus, vous pouvez vous retrouver avec certains fichiers non suivis.

Utilisez la commande suivante pour nettoyer les changements non suivis :

```bash
git clean -xdf
```

Décomposons le drapeau `-xdf` et expliquons ce que fait chaque partie :

- Le drapeau `-x` supprime les fichiers ignorés.
- Le drapeau `-d` supprime les dossiers non suivis.
- Le drapeau `-f` supprime les fichiers non suivis.

## Conclusion <a name="conclusion"></a>

Et voilà – vous avez maintenant réinitialisé votre branche locale à la branche distante.

Espérons que vous avez trouvé cet article utile.

Pour en savoir plus sur Git, consultez les ressources gratuites suivantes :

- [Git et GitHub pour les débutants - Cours accéléré](https://www.youtube.com/watch?v=RGOj5yH7evk)
- [Tutoriel Git pour les professionnels - Outils et concepts pour maîtriser le contrôle de version avec Git](https://www.youtube.com/watch?v=Uszj_k0DGsg)
- [Tutoriel avancé Git - Rebase interactif, Cherry-Picking, Reflog, Sous-modules et plus](https://www.youtube.com/watch?v=qsTthZi23VE)

Merci d'avoir lu et bon codage 😊