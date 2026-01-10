---
title: Tutoriel Git Checkout Remote Branch
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-01-12T20:14:30.000Z'
originalURL: https://freecodecamp.org/news/git-checkout-remote-branch-tutorial
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5ffda02d75d5f706921cc25f.jpg
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: Tutoriel Git Checkout Remote Branch
seo_desc: 'By Dillion Megida

  Git is a version control tool that allows you to maintain and view different versions
  of your application. When a new update breaks your app, Git lets you revert those
  changes to the previous version.

  In addition to versioning, Git ...'
---

Par Dillion Megida

Git est un outil de contrôle de version qui vous permet de maintenir et de visualiser différentes versions de votre application. Lorsqu'une nouvelle mise à jour casse votre application, Git vous permet de revenir à la version précédente.

En plus de la gestion des versions, Git vous permet de travailler dans plusieurs environnements en même temps. Plusieurs environnements dans ce contexte signifie **branches**.

## Pourquoi vous avez besoin de branches

Lorsque vous travaillez avec Git, vous aurez un environnement principal (également appelé main) (branche). Cette branche particulière contient le code source qui est déployé lorsque votre application est prête pour la production. 

Lorsque vous souhaitez mettre à jour votre application, vous pouvez également ajouter plus de commits (changements) à cette branche. Pour des changements mineurs, cela peut ne pas être un gros problème, mais pour des changements majeurs, faire cela n'est pas idéal. Et c'est pourquoi d'autres branches existent.

Pour créer et utiliser une nouvelle branche, vous utilisez la commande suivante dans votre terminal dans le répertoire du projet :

```shell
# créer une nouvelle branche
git branch nom-de-la-branche
# changer d'environnement pour la nouvelle branche
git checkout nom-de-la-branche
```

Sur cette nouvelle branche, vous pouvez créer les nouveaux changements. Ensuite, lorsque vous avez terminé, vous pouvez les fusionner avec la branche principale.

Un autre avantage des branches est qu'elles permettent à plusieurs développeurs de travailler sur le même projet simultanément. Si vous avez plusieurs développeurs travaillant sur la même branche principale, cela peut être désastreux. Vous avez trop de changements entre le code de chaque développeur, et cela se termine généralement par des conflits de fusion.

Avec Git, vous pouvez sauter sur une autre branche (un autre environnement) et y apporter des modifications, tandis que le travail se poursuit dans d'autres branches.


## Que signifie Git Checkout Remote Branch ?

Lorsque vous commencez un projet avec Git, vous obtenez deux environnements : la branche principale locale (qui existe dans votre ordinateur) et la branche principale distante (qui existe sur une plateforme prise en charge par Git comme GitHub). 

Vous pouvez pousser les changements de la branche principale locale vers la branche principale distante et également tirer les changements de la branche distante.

Lorsque vous créez une branche localement, elle n'existe qu'en local jusqu'à ce qu'elle soit poussée vers GitHub où elle devient la branche distante. Cela est montré dans l'exemple suivant :

```shell
# créer une nouvelle branche
git branch nouvelle-branche
# changer d'environnement pour la nouvelle branche
git checkout nouvelle-branche
# créer un changement
touch nouveau-fichier.js
# commiter le changement
git add .
git commit -m "ajouter un nouveau fichier"
# pousser vers une nouvelle branche
git push --set-upstream origin nouvelle-branche
```

Dans l'exemple ci-dessus, `origin nouvelle-branche` devient la branche distante. Comme vous l'avez peut-être remarqué, nous avons créé une nouvelle branche et commité un changement dessus avant de pousser vers la nouvelle branche distante. 

Mais que se passe-t-il si la branche distante existait déjà, et que nous voulions tirer la branche et tous ses changements vers notre environnement local ?

C'est là que nous utilisons "Git Checkout Remote Branch".

## Comment faire un Git Checkout Remote Branch

Supposons qu'il y ait une branche distante créée par un autre développeur, et que vous souhaitiez tirer cette branche. Voici comment procéder :

### 1. Récupérer toutes les branches distantes

```shell
git fetch origin
```

Cela récupère toutes les branches distantes du dépôt. `origin` est le nom de la branche distante que vous ciblez. Donc, si vous aviez un nom de branche distante `upstream`, vous pouvez appeler `git fetch upstream`.

### 2. Lister les branches disponibles pour le checkout

Pour voir les branches disponibles pour le checkout, exécutez la commande suivante :

```shell
git branch -a
```

Le résultat de cette commande est la liste des branches disponibles pour le checkout. Pour les branches distantes, vous les trouverez préfixées par `remotes/origin`.

### 3. Tirer les changements d'une branche distante

Notez que vous ne pouvez pas apporter de modifications directement sur une branche distante. Par conséquent, vous avez besoin d'une copie de cette branche. Supposons que vous souhaitiez copier la branche distante `fix-failing-tests`, voici comment vous procéderiez :

```shell
git checkout -b fix-failing-tests origin/fix-failing-tests
```

Ce que cela fait est :

- il crée une nouvelle branche appelée `fix-failing-tests`
- il `checkout` cette branche
- il tire les changements de `origin/fix-failing-tests` vers cette branche

Et maintenant vous avez une copie de cette branche distante. De plus, vous pouvez pousser des commits vers cette branche distante. Par exemple, vous pouvez pousser un nouveau commit comme suit :

```shell
touch nouveau-fichier.js
git add .
git commit -m "ajouter un nouveau fichier"
git push
```

Cela poussera les changements commités vers `origin/fix-failing-tests`. Si vous avez remarqué, nous n'avons pas eu à spécifier où nous poussions les changements (comme `git push origin fix-failing-tests`). C'est parce que Git configure automatiquement la branche locale pour suivre la branche distante.

## Conclusion

Le branchement Git rend la collaboration très facile lors du développement d'applications. 

Avec les branches, différents développeurs peuvent facilement travailler sur différentes parties de l'application simultanément. 

Avec le checkout de branche distante, la collaboration devient encore plus fluide car les développeurs peuvent également copier des branches distantes localement sur leurs systèmes, apporter des modifications et pousser vers les branches distantes.