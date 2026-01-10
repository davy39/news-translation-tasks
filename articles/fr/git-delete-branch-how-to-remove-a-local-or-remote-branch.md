---
title: Git Supprimer une Branche – Comment Supprimer une Branche Locale ou Distante
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-08-26T17:00:36.000Z'
originalURL: https://freecodecamp.org/news/git-delete-branch-how-to-remove-a-local-or-remote-branch
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/elaine-alex-OFMEk4ar9RA-unsplash--1-.jpg
tags:
- name: clean code
  slug: clean-code
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: Git Supprimer une Branche – Comment Supprimer une Branche Locale ou Distante
seo_desc: 'Git is a popular version control system and an essential tool in a web
  developer''s toolkit.

  Branches are a powerful and integral part of working with Git.

  In this article, you will learn the basics about how to remove local and remote
  branches in Git...'
---

Git est un système de contrôle de version populaire et un outil essentiel dans la boîte à outils d'un développeur web.

Les branches sont une partie puissante et intégrale du travail avec Git.

Dans cet article, vous apprendrez les bases de la suppression des branches locales et distantes dans Git.

## Qu'est-ce que les Branches dans Git ?

Une branche est un pointeur vers un commit.

Les branches Git sont un instantané d'un projet et de ses modifications, à partir d'un point spécifique dans le temps.

Lorsqu'on travaille sur un grand projet, il y a le dépôt principal avec tout le code, souvent appelé `main` ou `master`.

Le branchement vous permet de créer de nouvelles versions indépendantes du projet de travail principal original. Vous pourriez créer une branche pour l'éditer afin d'apporter des modifications, d'ajouter une nouvelle fonctionnalité, ou d'écrire un test lorsque vous essayez de corriger un bug. Et une nouvelle branche vous permet de faire cela sans affecter le code principal de quelque manière que ce soit.

Donc, pour résumer, les branches vous permettent d'apporter des modifications à la base de code sans affecter le code principal jusqu'à ce que vous soyez absolument prêt à implémenter ces modifications. 

Cela vous aide à garder la base de code propre et organisée.

## Pourquoi Supprimer des Branches dans Git ?

Vous avez donc créé une branche pour contenir le code d'une modification que vous souhaitiez apporter à votre projet.

Vous avez ensuite intégré cette modification ou cette nouvelle fonctionnalité dans la version originale du projet.

Cela signifie que vous n'avez plus besoin de conserver et d'utiliser cette branche, il est donc une bonne pratique courante de la supprimer pour éviter d'encombrer votre code.


## Comment Supprimer une Branche Locale dans Git

Les branches locales sont des branches sur votre machine locale et n'affectent aucune branche distante.

La commande pour supprimer une branche locale dans Git est :

```
git branch -d  nom_de_la_branche_locale
```

- `git branch` est la commande pour supprimer une branche localement.
- `-d` est un drapeau, une option de la commande, et c'est un alias pour `--delete`. Il indique que vous souhaitez supprimer quelque chose, comme le suggère le nom.  - `nom_de_la_branche_locale` est le nom de la branche que vous souhaitez supprimer.

Examinons cela un peu plus en détail avec un exemple.

Pour lister toutes les branches locales, vous utilisez la commande suivante :

```
git branch
```

J'en ai deux, les branches `master` et `test2`. Je suis actuellement sur la branche `test2` comme le montre le `(*)` :

![Screenshot-2021-08-25-at-4.13.14-PM](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-25-at-4.13.14-PM.png)

Je veux supprimer la branche `test2`, mais il n'est pas possible de supprimer une branche dans laquelle vous vous trouvez actuellement.

Si vous essayez de le faire, vous obtiendrez une erreur qui ressemblera à ceci :

![Screenshot-2021-08-25-at-4.17.50-PM](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-25-at-4.17.50-PM.png)

Donc, avant de supprimer une branche locale, assurez-vous de basculer vers une autre branche que vous ne souhaitez PAS supprimer, avec la commande `git checkout` :

```
git checkout nom_de_la_branche

#où nom_de_la_branche est le nom de la branche vers laquelle vous souhaitez vous déplacer
#dans mon cas, l'autre branche que j'ai est master, donc je ferais :
#git checkout master
```

Voici le résultat :

![Screenshot-2021-08-25-at-4.20.40-PM](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-25-at-4.20.40-PM.png)

Maintenant, je peux supprimer la branche :

![Screenshot-2021-08-25-at-5.10.13-PM](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-25-at-5.10.13-PM.png)

La commande pour supprimer une branche locale que nous venons d'utiliser ne fonctionne pas dans tous les cas.

Si la branche contient des modifications non fusionnées et des commits non poussés, le drapeau `-d` ne permettra pas la suppression de la branche locale.

C'est parce que les commits ne sont pas vus par d'autres branches et Git vous protège contre la perte accidentelle de données de commit.

Si vous essayez de le faire, Git vous montrera une erreur :

![Screenshot-2021-08-25-at-5.23.46-PM](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-25-at-5.23.46-PM.png)

Comme le suggère l'erreur, vous devrez utiliser le drapeau `-D` à la place :

```
git branch -D nom_de_la_branche_locale
```

Le drapeau `-D`, avec un D majuscule (qui est un alias pour `--delete --force`), supprime de force la branche locale, quel que soit son état de fusion.

Mais notez que **vous devez utiliser cette commande avec prudence**, car il n'y a pas de prompt vous demandant de confirmer vos actions. 

Utilisez-la uniquement lorsque vous êtes absolument sûr de vouloir supprimer une branche locale.

Si vous ne l'avez pas fusionnée dans une autre branche locale ou poussée vers une branche distante dans la base de code, vous risquez de perdre toutes les modifications que vous avez apportées.

![Screenshot-2021-08-25-at-5.33.41-PM](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-25-at-5.33.41-PM.png)


## Comment Supprimer une Branche Distante dans Git

Les branches distantes sont séparées des branches locales.

Ce sont des dépôts hébergés sur un serveur distant qui peuvent être accessibles depuis celui-ci. Cela est en comparaison avec les branches locales, qui sont des dépôts sur votre système local.

La commande pour supprimer une branche distante est :

```
git push nom_du_remote -d nom_de_la_branche_distante
```

- Au lieu d'utiliser la commande `git branch` que vous utilisez pour les branches locales, vous pouvez supprimer une branche distante avec la commande `git push`.
- Ensuite, vous spécifiez le nom du remote, qui dans la plupart des cas est `origin`.
- `-d` est le drapeau pour la suppression, un alias pour `--delete`.
- `nom_de_la_branche_distante` est la branche distante que vous souhaitez supprimer.

Maintenant, voyons un exemple de la manière de procéder pour supprimer une branche distante.

Pour afficher les branches distantes, vous utilisez cette commande :

```
git branch -a
```

Le drapeau `-a` (un alias pour `--all`) montre toutes les branches – locales et distantes.

![Screenshot-2021-08-25-at-7.35.31-PM](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-25-at-7.35.31-PM.png)

J'ai deux branches locales appelées `master` et `test` et deux branches distantes `origin/master` et `origin/test`.

Le `-r`, un alias pour `--remotes`, montre *uniquement* les dépôts distants.

![Screenshot-2021-08-25-at-7.37.12-PM](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-25-at-7.37.12-PM.png)

Je veux supprimer la branche distante `origin/test`, donc j'utilise la commande :

```
git push origin -d test
```

Résultat :

![Screenshot-2021-08-25-at-7.39.34-PM](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-25-at-7.39.34-PM.png)

Cela a supprimé la branche `test` dans le dépôt distant nommé `origin`.

Le dépôt distant `origin/test` n'est plus là :

![Screenshot-2021-08-25-at-7.42.01-PM](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-25-at-7.42.01-PM.png)

## Conclusion

Vous savez maintenant comment supprimer des branches locales et distantes dans Git.

Si vous souhaitez en savoir plus sur Git, vous pouvez regarder les cours suivants sur la chaîne YouTube de freeCodeCamp :

- Pour apprendre à vous configurer avec Git, et pour un aperçu des commandes Git importantes et du flux de travail git typique – [Git et GitHub pour débutants - Cours accéléré](https://www.youtube.com/watch?v=RGOj5yH7evk).
- Pour approfondir les branches et apprendre comment elles fonctionnent – [Tutoriel sur les Branches Git](https://www.youtube.com/watch?v=e2IbNHi4uCI&t=6s).

Merci d'avoir lu et bon apprentissage !