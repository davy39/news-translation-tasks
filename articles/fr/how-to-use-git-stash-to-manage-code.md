---
title: Comment utiliser Git Stash pour gérer efficacement votre code
subtitle: ''
author: Okoro Emmanuel Nzube
co_authors: []
series: null
date: '2024-10-11T13:40:01.235Z'
originalURL: https://freecodecamp.org/news/how-to-use-git-stash-to-manage-code
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1728563160215/147e5b8d-960d-4a90-ad2f-6d71337ac0ce.jpeg
tags:
- name: gitpop
  slug: gitpop
- name: gitapply
  slug: gitapply
- name: git stash
  slug: git-stash
- name: Git
  slug: git
- name: code management
  slug: code-management
seo_title: Comment utiliser Git Stash pour gérer efficacement votre code
seo_desc: 'Sometimes when you’re coding, you need to leave a particular task incomplete
  to focus on another task – but you don''t want to lose your progress. So what do
  you do? Fortunately, git stash comes to the rescue.

  In this article, you’ll learn all about t...'
---

Parfois, lorsque vous codez, vous devez laisser une tâche particulière incomplète pour vous concentrer sur une autre tâche, mais vous ne voulez pas perdre votre progression. Alors, que faites-vous ? Heureusement, `git stash` vient à la rescousse.

Dans cet article, vous apprendrez tout sur la commande [git stash](https://git-scm.com/docs/git-stash) et pourquoi il est important de stasher votre code. À la fin de cet article, vous aurez une connaissance pratique de l'utilisation de la commande `git stash` dans vos projets.

### Voici ce que nous allons couvrir :

1. [Pourquoi stasher ?](#heading-pourquoi-stasher)

2. [Avantages et inconvénients de l'utilisation de git stash](#heading-avantages-et-inconvenients-de-lutilisation-de-git-stash)

3. [Comment créer un stash dans Git (guide étape par étape)](#heading-comment-creer-un-stash-dans-git-guide-etape-par-etape)

4. [Autres commandes git stash comme list, apply et pop](#heading-autres-commandes-git-stash-comme-list-apply-et-pop)

5. [Comment gérer plusieurs stashes dans votre projet](#heading-comment-gerer-plusieurs-stashes-dans-votre-projet)

6. [Cas d'utilisation réels pour git stash](#heading-cas-dutilisation-reels-pour-git-stash)

7. [Conclusion](#heading-conclusion)

## Pourquoi stasher ?

[Git](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F) nous a fourni la commande stash, qui facilite notre vie. La commande `git stash` vous aide à sauvegarder un brouillon de votre tâche actuelle, vous donnant temporairement le temps de vous occuper de votre nouvelle tâche sans perdre votre progression sur la tâche précédente.

Il y a de nombreuses raisons pour lesquelles le stashing est important. En voici quelques-unes :

* **Résolution des conflits dans un projet** : Dans un environnement de collaboration, en tant que développeur, vous travaillez avec d'autres développeurs sur un projet particulier. Un conflit de fusion peut survenir, ce qui peut vous obliger à interrompre votre tâche actuelle pour gérer le conflit. Vous pouvez facilement stasher votre tâche actuelle et vous concentrer pleinement sur la résolution du conflit de fusion sans avoir à vous soucier de perdre votre progression.

* **Environnement de travail propre** : Vous pouvez vouloir démarrer une nouvelle tâche ou tirer un dépôt dans votre environnement de travail. Avec le stashing, vous pouvez nettoyer temporairement votre environnement de travail actuel, rendant votre environnement de travail propre et prêt à effectuer une autre tâche.

* **Changement de branches** : `Git stash` est très utile dans cette situation. Vous pouvez être en train de faire quelque chose et ce n'est pas prêt à être validé, mais à ce moment-là, vous devez changer de branche. Avec `git stash`, vous pouvez facilement passer à une autre branche et effectuer vos autres tâches.

## Avantages et inconvénients du stashing

Voici quelques-uns des avantages de l'utilisation du stash :

* Il est facile à utiliser et à comprendre

* Il vous aide à sauvegarder un brouillon de votre tâche actuelle et à vous concentrer sur une autre tâche.

* Il est utile lorsque vous essayez de résoudre des conflits comme les conflits de fusion, `git fork`, etc., lorsque vous travaillez avec d'autres collaborateurs dans un projet.

* Vous pouvez réappliquer votre fichier brouillon non seulement sur la branche à partir de laquelle vous l'avez stashé, mais aussi sur d'autres branches.

Comme le dit le proverbe, "Tout ce qui a un avantage a aussi un inconvénient". Voici quelques-uns des inconvénients de l'utilisation du stash :

* Le stashing peut entraîner un conflit de fusion : Un conflit de fusion peut survenir lors de la réapplication de votre brouillon stashé à une branche qui contient déjà un contenu similaire au brouillon, et vous devrez résoudre cela manuellement.

* Cluster et confusion : Dans une situation où vous travaillez sur un projet énorme avec plusieurs sous-tâches, l'application de la commande stash à divers points peut entraîner un cluster de brouillons sauvegardés. Cela peut entraîner une confusion sur le brouillon sauvegardé particulier que vous souhaitez continuer à travailler.

Maintenant que nous avons vu quelques-uns des avantages et inconvénients de l'utilisation de `git stash`, voyons comment `git stash` fonctionne et comment l'appliquer à notre projet.

## Comment fonctionne Git Stash

Comme nous venons de le discuter, `git stash` vous aide à sauvegarder un brouillon de vos modifications non validées actuelles. Voyons maintenant comment cela se passe en utilisant l'analogie ci-dessous.

Lorsque vous exécutez la commande `git stash`, elle place votre fichier suivi dans une boîte, puis supprime/masque cette boîte, rendant l'environnement/branche propre et libre d'être utilisé pour une autre tâche. Lorsque vous appliquez la commande stash à la branche actuelle sur laquelle vous travaillez, elle sauvegarde un brouillon de tous les fichiers suivis dans cette branche et rétablit cette branche à un état propre.

Pour mieux expliquer, voici un exemple :

![Image de comment fonctionne Git Stash](https://hackmd.io/_uploads/S1x5zSPhR.gif align="left")

À partir de l'image ci-dessus, nous avons créé un nouveau projet et avons déjà initialisé `git` dedans. Nous sommes actuellement sur la branche "main" qui est la branche par défaut.

Si nous modifions un fichier dans la branche `main` et appliquons la commande `git stash`, le fichier modifié sera sauvegardé en tant que brouillon et votre environnement de travail sera rétabli au dernier commit que vous avez fait (faisant en sorte qu'il semble qu'il n'y ait eu aucune modification en premier lieu).

Note : Par défaut, vous ne pouvez appliquer la commande stash qu'aux fichiers suivis dans `git`.

### Comment créer un stash

Voici comment vous pouvez créer un stash dans votre projet.

Créez un fichier sur lequel vous souhaitez travailler, peut-être un fichier `index.html` ou un fichier `style.css`. Initialisez `git` dans votre projet en exécutant la commande `git init`. Ajoutez le fichier à l'étape de suivi de Git en exécutant `git add .`. Ensuite, à ce stade, si vous faites des modifications et souhaitez revenir plus tard pour les compléter, vous pouvez exécuter :

```bash
git stash
```

Voici une représentation visuelle du processus ci-dessus :

![Représentation visuelle de comment créer un stash](https://hackmd.io/_uploads/HJg8cHDh0.gif align="left")

Il existe d'autres commandes de stash que vous devez connaître afin de contrôler votre projet stashé. Elles incluent [List](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt-listltlog-optionsgt), [Pop](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt-pop--index-q--quietltstashgt), [Clear](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt-clear), [Apply](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt-apply--index-q--quietltstashgt), [Show](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt-show-u--include-untracked--only-untrackedltdiff-optionsgtltstashgt), et quelques autres.

* **List** : La commande list est principalement utilisée pour afficher le nombre de stashes effectués dans un projet particulier. Tout comme un tableau, le brouillon stashé est numéroté à partir de 0 et plus. Pour utiliser cette commande, exécutez `git stash list`. Note : La commande stash est organisée de telle sorte que lorsqu'un changement est stashé, il prend la première position, c'est-à-dire "stash@{0}" tandis que les autres changements sont repoussés vers le bas.

* **Pop** : Cette commande est utilisée pour récupérer un brouillon déjà stashé dans votre projet. Lorsque vous appliquez la commande pop, elle récupère automatiquement le dernier brouillon stashé dans votre projet de travail et le supprime de la liste de stash. Exécutez la commande suivante pour pop un stash : `git stash pop`.

* **Clear** : Lorsque cette commande est appliquée, elle est utilisée pour supprimer/tous les entrées de stash. Il est important de noter que, lorsque vous utilisez la commande clear, vous ne pouvez pas récupérer le stash effacé. Vous pouvez l'utiliser en exécutant cette commande : `git stash clear`.

* **Apply** : Cette commande fonctionne exactement comme la commande pop, mais la seule différence est que le brouillon stashé n'est pas supprimé de la liste après avoir été récupéré. Cela signifie que lorsque vous utilisez la commande apply, elle récupère le dernier brouillon stashé dans votre projet mais ne le supprime pas de la liste de stash. Exécutez la commande suivante pour utiliser la commande apply : `git stash apply`.

* **Show** : Cette commande est importante car elle vous aide à montrer les changements que vous avez apportés dans le brouillon stashé. Utilisez la commande suivante pour montrer un stash : `git stash show`.

## Comment gérer plusieurs stashes dans votre projet

Savoir comment gérer plusieurs stashes dans votre projet est important, car il peut y avoir des moments où vous avez plus de 3-4 brouillons stashés dans votre projet.

Voici comment gérer plusieurs stashes :

### Étape une : Personnalisez chaque stash avec un message spécifique

Cette étape est très importante si vous souhaitez éviter d'être confus dans des situations où vous avez plusieurs stashes.

![Plusieurs stashes avec les mêmes messages](https://hackmd.io/_uploads/BkVtICNIA.png align="left")

À partir de l'image ci-dessus, nous avons un total de quatre stashes (c'est-à-dire "stash@{0}" à "stash@{3}") et chaque stash porte le même message de "first commit". Cela peut être confus lorsque nous pourrions vouloir pop ou appliquer l'un de ces stashes plus tard dans le futur.

Pour résoudre ce problème, tout ce que nous avons à faire est d'assigner un message de stash spécifique au prochain stash. Nous pouvons faire cela en exécutant la commande suivante :

```bash
git stash save "Nouveau message/nom ici"
```

Voici à quoi cela ressemble :

![Plusieurs stashes avec des messages différents](https://hackmd.io/_uploads/HJH3IRNLA.png align="left")

À partir de l'image ci-dessus, vous pouvez clairement voir la différence entre les deux derniers stashes (c'est-à-dire "stash@{0}" et "stash@{1}") et les autres. Les deux premiers stashes ont leur propre message spécifique, ce qui les rend très faciles à différencier des autres.

### Étape deux : Récupérez un stash spécifique au lieu du dernier stash

Il y a des situations où vous pouvez vouloir récupérer un brouillon stashé spécifique plutôt que le dernier brouillon stashé que vous venez de faire. Vous pouvez faire cela en utilisant soit :

```bash
git stash pop stash@{n}
```

ou

```bash
git stash apply stash@{n}
```

Où `n` indique l'ID de stash que vous souhaitez récupérer. Cela fonctionne également lorsque vous souhaitez supprimer ou effacer un brouillon stashé spécifique.

### Étape trois : Prévisualisez votre brouillon stashé avant de le récupérer.

Avant de restaurer un brouillon stashé, il est important de le prévisualiser pour vous assurer qu'il s'agit du brouillon exact que vous souhaitez restaurer. La commande `show` vous aide à examiner les changements dans le brouillon avant de le restaurer. Pour ce faire, exécutez la commande suivante :

```bash
git stash show stash@{n}
```

## Cas d'utilisation réels pour `git stash`

Voici quelques scénarios de cas réels où la commande git stash est importante.

* **Lors du débogage** : Cela arrive souvent lorsque vous êtes dans un environnement de collaboration. Supposons que vous travaillez avec deux autres développeurs sur un projet et que l'un d'eux rencontre une erreur qui nécessite votre attention urgente. L'utilisation de la commande `git stash` est idéale dans cette situation.

* **Lorsque vous n'êtes pas prêt à valider** : Cela se produit souvent. Il y a des situations où vous n'êtes pas prêt à valider vos changements dans le dépôt. Stasher ces changements est la meilleure prochaine étape.

* **Rétablir le répertoire à son état d'origine** : Rétablir le répertoire à son état d'origine signifie simplement nettoyer toutes les modifications apportées au répertoire et le faire paraître comme si rien n'avait été fait. La commande `git stash` vous aide à atteindre cet objectif.

## Conclusion

La commande `git stash` vous aide à gérer votre projet correctement, que vous travailliez seul ou en collaboration.

Cet outil est vital pour chaque développeur qui souhaite travailler librement et sans effort sur un projet.

À ce stade, je crois que vous savez ce qu'est `git stash`, pourquoi il est important et comment l'utiliser dans votre projet.

Merci d'avoir lu.