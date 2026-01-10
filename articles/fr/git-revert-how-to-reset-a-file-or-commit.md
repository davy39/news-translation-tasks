---
title: Git Revert – Comment réinitialiser un fichier ou un commit
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-02-28T00:21:11.000Z'
originalURL: https://freecodecamp.org/news/git-revert-how-to-reset-a-file-or-commit
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/roman-synkevych-wX2L8L-fGeA-unsplash--1-.jpg
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: Git Revert – Comment réinitialiser un fichier ou un commit
seo_desc: "When working on a project with a team or by yourself, it's important to\
  \ track changes in the code base through version control. \nGit provides you with\
  \ different commands for tracking file changes. These commands will enable you to\
  \ collaborate with ot..."
---

Lorsque vous travaillez sur un projet avec une équipe ou seul, il est important de suivre les changements dans la base de code grâce au contrôle de version. 

Git vous fournit différentes commandes pour suivre les changements de fichiers. Ces commandes vous permettront de collaborer avec d'autres développeurs, d'accéder à l'historique des fichiers, de gérer le code, et plus encore. 

Dans cet article, vous apprendrez comment réinitialiser un fichier ou un commit à un commit précédent. 

Nous utiliserons un simple code HTML pour démontrer comment vous pouvez réinitialiser à un commit précédent en utilisant Git. 

Commençons !

## Comment réinitialiser un fichier ou un commit

Dans cette section, vous apprendrez comment réinitialiser un fichier ou un commit en utilisant les commandes suivantes : 

* `git revert`.
* `git reset`.

### Comment réinitialiser un fichier ou un commit en utilisant la commande `git revert`

Voici à quoi ressemble la syntaxe de la commande `git revert` :

```txt
git revert [ID du commit]
```

Voici le code avec lequel nous allons travailler :

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Document</title>
  </head>
  <body>
    <h1>Hello World!</h1>
  </body>
</html>

```

Supposons que le fichier ci-dessus est l'état actuel de la base de code pour tous les développeurs travaillant sur le projet. 

Nous allons apporter quelques modifications au fichier, puis ajouter, commiter et pousser les changements. C'est-à-dire : 

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Document</title>
  </head>
  <body>
    <h1>Hello World!</h1>

    <ul>
        <li>Red</li>
        <li>Yellow</li>
        <li>Orange</li>
    </ul>
    
  </body>
</html>

```

Nous avons ajouté une liste de couleurs au code. Poussons les changements en utilisant la commande ci-dessous :

```bash
git add .
git commit -m "added colors to the HTML file"
git push -u origin main
```

À ce stade, les nouveaux changements ont été mis à jour pour tous ceux qui travaillent sur cette branche particulière du code. 

Mais que faire si les couleurs ajoutées font partie de fonctionnalités qui doivent être publiées pour les utilisateurs dans le futur ? Vous avez fait une erreur en publiant cette fonctionnalité avant le temps prévu. 

Pour revenir à un commit précédent, vous aurez besoin de l'ID de ce commit particulier. Pour obtenir l'ID du commit, exécutez la commande suivante :

```bash
git log
```

La commande vous montre l'ID du commit, l'auteur et la date de chaque commit. Cela devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/git-log.PNG)
_git log_

Dans notre cas, l'ID du commit est 785dd5a6dd0f1ebd9e06045df787d8d28fd38285.

Pour réinitialiser le fichier, vous utilisez `git revert [ID du commit]`. C'est-à-dire :

```bash
git revert 785dd5a6dd0f1ebd9e06045df787d8d28fd38285
```

La commande ci-dessus réinitialisera toutes les modifications apportées au fichier avant que ce commit particulier ne soit effectué. Voici à quoi ressemblera le fichier HTML maintenant :

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Document</title>
  </head>
  <body>
    <h1>Hello World!</h1>
  </body>
</html>
```

Maintenant, vous pouvez pousser cet nouvel état. 

Notez que la commande `git revert` ne supprime pas le commit réinitialisé du dépôt distant. Au lieu de cela, elle crée un nouveau commit pour les changements réinitialisés. 

Cela signifie que vous aurez l'historique du commit qui a été réinitialisé et un nouveau commit pour le fichier contenant les changements réinitialisés. 

### Comment réinitialiser un fichier ou un commit en utilisant la commande `git reset`

La commande `git reset` peut également être utilisée pour réinitialiser les changements. Considérez l'historique des commits ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/git-log-1.PNG)

L'image ci-dessus montre tout l'historique des commits — du premier commit au commit réinitialisé dans la dernière section. 

Si nous utilisons `git reset [ID du commit]` pour revenir à un commit particulier, tous les autres commits après celui-ci seront supprimés de l'historique des commits. 

Voici un exemple :

```bash
git reset c1e4962a9b355f023c250609cfa9303a67b3063e
```

En utilisant l'ID du premier commit, nous revenons à l'état du premier commit. 

En exécutant la commande `git log`, vous aurez un historique des commits comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/git-log-2.PNG)

Bien que vous ayez réussi à revenir au premier commit, l'historique des autres commits dans le code a été effacé. Cela peut avoir un effet très négatif lors de la collaboration avec d'autres développeurs. 

## Résumé

Dans cet article, nous avons parlé de deux commandes Git importantes pour annuler les changements dans un dépôt Git — `git revert` et `git reset`. 

Les deux commandes vous ramènent à un état précédent spécifié dans la base de code, mais avec des effets différents. 

La commande `git revert` revient à un commit spécifié mais conserve l'historique de chaque autre commit effectué sur la base de code, et crée un nouveau commit pour les changements réinitialisés. C'est une manière plus efficace d'annuler les changements lors de la collaboration avec d'autres. 

Alternativement, la commande `git reset` reviendra à un commit spécifié, puis supprimera chaque commit qui vient après le commit spécifié. 

Pour être du bon côté, utilisez `git revert` lorsque vous annulez des changements dans un dépôt sur lequel d'autres développeurs travaillent. 

Vous pouvez utiliser `git reset` dans les cas où vous souhaitez vous débarrasser complètement des commits après avoir annulé les changements.

Bon codage !