---
title: Comment basculer entre les problèmes dans votre dépôt Git local
subtitle: ''
author: Sule-Balogun Olanrewaju
co_authors: []
series: null
date: '2020-06-08T17:59:37.000Z'
originalURL: https://freecodecamp.org/news/how-to-switch-between-issues-in-git
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a74740569d1a4ca25b6.jpg
tags:
- name: Git
  slug: git
- name: Productivity
  slug: productivity
- name: version control
  slug: version-control
seo_title: Comment basculer entre les problèmes dans votre dépôt Git local
seo_desc: 'On my journey to open source I ran into a simple (yet tricky) situation
  that can trip you up if you do it wrong. And that''s what we''ll discuss in this
  article.

  Participating in the open source community means you''re contributing to the development
  of...'
---

Sur mon parcours vers l'open source, je suis tombé sur une situation simple (mais délicate) qui peut vous piéger si vous la faites mal. Et c'est ce que nous allons discuter dans cet article.

Participer à la communauté open source signifie que vous contribuez au développement de logiciels libres ou open source. Il existe de nombreuses organisations qui accueillent toujours des contributeurs dans leurs bases de code.

Pour commencer avec l'open source, vous devez avoir une compréhension de base des outils de contrôle de version tels que [Git](https://git-scm.com/). Les contributeurs utilisent Git pour suivre les changements dans les fichiers de projet et cela aide également les gens à coordonner leur travail sur ces fichiers.

## Prérequis

1. Avoir [Git](https://git-scm.com/downloads) installé
2. Avoir une compréhension de base de Git

## Pourquoi les problèmes ? 

![Image](https://www.freecodecamp.org/news/content/images/2020/06/issue-scrrenshot-1.PNG)

Les problèmes dans un dépôt peuvent être utilisés pour suivre les tâches, les idées, les bugs ou les améliorations pour le projet sur lequel vous travaillez. Basiquement, ils vous fournissent une description de ce que la tâche implique. 

Pour prendre un problème, les administrateurs du projet doivent vous assigner ce problème particulier. De cette façon, les autres membres de l'équipe sauront que quelqu'un travaille sur le problème.

## Travailler sur un problème 

Pour commencer à travailler sur un problème, vous devez faire une copie ou un clone du dépôt cible en utilisant la commande Git clone sur votre machine locale. 

```git
git clone <url du dépôt>
```

Créez un upstream vous permettant de suivre les dernières modifications de l'upstream (c'est-à-dire le dépôt original). De cette façon, Git vous informe lorsqu'il y a des changements afin que vous puissiez mettre à jour le dépôt cloné.

```git
git remote add upstream <url du dépôt original>

```

Pour prévisualiser la liste des distants disponibles et les tâches qui peuvent être effectuées (fetch et push), tapez :

```git
git remote -v
```

Pour rester à jour avec les dernières modifications, vous devez toujours essayer de fetch depuis l'upstream. De cette façon, vous obtenez tous les commits de chaque membre de l'équipe qui a également travaillé sur diverses fonctionnalités.

```git
git fetch <upstream>/<master>
```

Ensuite, vous devrez fusionner les commits des autres contributeurs dans le dépôt local. 

```git
git merge <upstream>/<master>


```

Le but de Git merge est de faire correspondre la copie locale de la branche master exactement à la même que la copie upstream de la branche master.

Ensuite, créez une branche pour le problème qui vous a été assigné. Pourquoi devez-vous créer une branche ? Et à quoi sert une branche ? Approfondissons.

### Branche Git 

Une branche vous donne un instantané des modifications qui ont été apportées. Lorsqu'un commit est fait, Git stocke les informations du commit. Cela fournit un pointeur qui peut ensuite être utilisé pour référencer ou suivre les modifications qui ont été apportées. C'est pourquoi il est utile de créer une branche lorsque vous travaillez sur une nouvelle tâche, un correctif de bug ou toute autre fonctionnalité. 

Lorsque nous commençons, Git nous fournit une branche master. La branche master contient du code fonctionnel. Pour éviter de mélanger vos modifications avec le code de production, vous devez créer une nouvelle branche.

Pour créer une branche, vous devez entrer la commande Git suivante :

```git
git checkout -b <nom-de-branche-descriptif>
```

Cette commande crée une nouvelle branche basée sur la branche actuelle, bien que vous puissiez également spécifier la branche où vous souhaitez que votre nouvelle branche soit créée.

```git
git checkout -b <nom-de-branche-descriptif> <nom-de-branche-cible>

```

Pour lister toutes les branches disponibles dans votre dépôt, tapez :

```git
git branch
```

Lorsque la tâche sur laquelle vous travaillez est terminée, poussez les modifications sur le dépôt local pour révision. Après cela, créez une pull request pour notifier les administrateurs du projet de l'état actuel de la tâche assignée.

```git
git push -u origin <nom-de-branche-descriptif>

```

## Maintenant, comment basculer pour travailler sur le problème suivant ?  

Créez une branche différente avec un nom descriptif, comme ceci :

```git
git checkout -b <nom-de-branche-descriptif> <nom-de-branche-cible>

```

Une fois que nous avons notre branche, nous utiliserons une commande utilitaire de [hub](https://hub.github.com/). La commande nous aidera à récupérer le code de l'upstream et exécutera également la fusion (si vous installez [l'utilitaire hub](https://github.com/github/hub#installation)). 

```git
hub sync
```

La commande récupère les modifications de l'upstream et les fusionne avec la branche nouvellement créée. Vous pouvez toujours vérifier les modifications avec votre branche et l'upstream en utilisant la commande Git status :

```git
git status
```

Maintenant, vous pouvez procéder et travailler sur la nouvelle branche. N'oubliez pas de commiter vos modifications et de les pousser vers la branche distante comme nous l'avons fait ci-dessus. 

### Erreurs que vous pourriez faire.

Vous pourriez faire une erreur en travaillant sur plusieurs problèmes - ce qui peut conduire à supprimer des commits d'une branche. 

Voici un exemple de ce qui peut être fait pour effacer les commits indésirables d'une branche :

**Étape 1 :** Basculez dans la branche où vous souhaitez supprimer les commits indésirables :

```git
git checkout <nom-de-branche-descriptif>

```

**Étape 2 :** Exécutez les enregistrements des commits faits sur la branche. Cela vous aidera à décider quels commits vous souhaitez conserver en fonction du **Hash de Commit** unique (SHA1 40 caractères de checksum du contenu des commits) généralement sous cette forme : **da034f6ff3e856b5ba155bc01def0847a1c4ed7e**.

```git
git log
```

Il est également utile de noter que si vous cherchez à conserver le commit le plus récent (disons le dernier), vous pouvez simplement faire ceci :

```git
git log -n 1
```

**Étape 3 :** Puisque vous souhaitez supprimer tous les autres commits sur cette branche, appliquez simplement ce seul commit à la branche. Supprimer et appliquer sont deux étapes :

Premièrement, supprimez tous les commits sur la branche avec :

```git
git reset --hard <upstream>/<master>


```

En termes simples, la commande ci-dessus indique à Git de jeter toutes les modifications stagées et non stagées. Il oubliera tout sur la branche locale actuelle et la rendra exactement identique à la branche `upstream/master`.

Deuxièmement, appliquez ce seul commit à la branche avec la commande :

```git
git cherry-pick Hash

//où Hash est un hash de commit d'une autre branche
```

Cette commande sélectionne une seule référence (c'est-à-dire un commit) par défaut à partir d'une branche et l'applique à une autre. 

**Étape 4 :** Lorsque vous exécutez `git status`, il signalera que votre branche `<origin>/<nom-de-branche-descriptif>` a divergé. Puisque c'est attendu, nous devons forcer le distant à ne contenir que les modifications que nous avons cherry-pickées. 

Pour y parvenir, nous devons utiliser une commande pour aider à effacer l'historique distant et le remplacer par un autre historique :

```git
git push --force origin
```

Cette commande supprimera les commits supplémentaires sur le distant, tout comme nous avons supprimé les commits supplémentaires sur la copie locale. Cela est dangereux car c'est l'une des très rares commandes git qui supprimera quelque chose - soyez donc prudent lorsque vous l'utilisez.

Maintenant, lorsque vous exécutez `git status`, il signale que la branche est à jour avec `<origin>/<nom-de-branche-descriptif>`. Cela vous montre que l'opération a été réalisée avec succès.

Merci d'avoir lu ?! Un grand merci à [Mark Waite](https://github.com/markewaite)?  

Suivez-moi sur [twitter](https://twitter.com/devlarri).