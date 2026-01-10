---
title: Supprimer un Répertoire sous Linux – Comment Supprimer des Répertoires et leur
  Contenu depuis la Ligne de Commande
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2021-08-30T21:35:33.000Z'
originalURL: https://freecodecamp.org/news/remove-a-directory-in-linux-how-to-delete-directories-and-contents-from-the-command-line
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/pexels-any-lane-5945735.jpg
tags:
- name: command line
  slug: command-line
- name: Linux
  slug: linux
seo_title: Supprimer un Répertoire sous Linux – Comment Supprimer des Répertoires
  et leur Contenu depuis la Ligne de Commande
seo_desc: 'Linux is a popular open source operating system, and its features are often
  available in your development environment. If you can learn its basic commands,
  it''ll make your life as a developer much easier.

  In this guide you will learn how to delete di...'
---

Linux est un système d'exploitation open source populaire, et ses fonctionnalités sont souvent disponibles dans votre environnement de développement. Si vous pouvez apprendre ses commandes de base, cela rendra votre vie en tant que développeur beaucoup plus facile.

Dans ce guide, vous apprendrez à supprimer des répertoires et des fichiers depuis la ligne de commande Linux.

# La commande Linux `rm`

La commande `rm` (abréviation de remove) est assez utile. Apprenons sa syntaxe et regardons quelques exemples pour la voir en action.

## Syntaxe de la commande `rm`

La syntaxe est montrée ci-dessous, avec `args` étant n'importe quel nombre d'arguments (dossiers ou fichiers).

```
rm [options] args
```

Sans `options`, vous pouvez l'utiliser pour supprimer des fichiers. Mais pour supprimer des répertoires, vous devez utiliser les `options` pour cette commande.

Les options sont les suivantes :

* `-r`, "récursif" – cette option vous permet de supprimer des dossiers et de supprimer récursivement leur contenu en premier
* `-i`, "interactif" – avec cette option, il demandera une confirmation à chaque fois avant de supprimer quelque chose
* `-f`, "forcer" – il ignore les fichiers inexistants et supprime toute demande de confirmation (essentiellement, c'est l'opposé de `-i`). Il ne supprimera pas les fichiers d'un répertoire si le répertoire est protégé en écriture.
* `-v`, "verbose" – il affiche ce que la commande fait sur le terminal
* `-d`, "répertoire" – qui vous permet de supprimer un répertoire. Il fonctionne uniquement si le répertoire est vide.

## Exemple de la commande Linux `rm`

Prenons un répertoire `project_folder` comme exemple. Il contient ces fichiers et dossiers :

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-94.png)



Utilisons ce répertoire pour montrer comment fonctionnent les différentes options.

Vous pouvez ajouter l'option `-v` à toutes les commandes afin qu'elle écrive étape par étape ce qui se passe.

Commençons donc par la première option, `-r`. Vous venez d'apprendre que cela supprime les fichiers et dossiers de manière récursive. Vous pouvez l'utiliser comme ceci `rm -r project_folder` ou aussi `rm -rv project_folder` avec l'option verbose.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-98.png)

Il a supprimé le répertoire `project_folder` et tout ce qu'il contient, dans l'ordre indiqué.

Recréons le dossier et réessayons.

Que se passe-t-il si vous n'utilisez pas l'option `-r` et que vous essayez de supprimer le répertoire quand même ? Il ne le permettra pas et affichera une erreur :

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-99.png)

Pour supprimer des répertoires, vous pouvez utiliser l'option `-d`, mais si vous essayez de l'utiliser dans ce cas, il donnera une erreur car le dossier n'est pas vide.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-106.png)

L'option `-i` fait en sorte qu'il demande pour chaque action individuellement.

Et vous devez appuyer sur `y` ou `n` puis `Enter` après chaque requête.

Si vous sélectionnez `y` pour toutes les requêtes, il supprimera tout :

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-107.png)

Si, au contraire, vous décidez de ne pas supprimer certains fichiers ou dossiers, avec `n`, il conservera ces fichiers et continuera avec le reste :

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-109.png)

La dernière option que nous n'avons pas vue jusqu'à présent est `-f`, qui supprimera les erreurs.

Par exemple, en écrivant comme ci-dessous, vous essayeriez de supprimer deux fichiers inexistants – il n'y a pas de fichier `rat.png`, et `dog.pmg` contient une faute de frappe et cela donne deux erreurs. Avec l'option `-f`, vous ne verrez pas les erreurs.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-108.png)

# Conclusion

La ligne de commande Linux est assez utile si vous êtes développeur. Dans cet article, vous avez vu l'une de ses commandes possibles, `rm`, que vous pouvez utiliser pour supprimer des répertoires et des fichiers.

Profitez de cet nouvel outil dans votre arsenal !