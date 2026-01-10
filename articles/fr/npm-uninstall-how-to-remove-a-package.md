---
title: npm Uninstall – Comment supprimer un package
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-03-01T20:46:50.000Z'
originalURL: https://freecodecamp.org/news/npm-uninstall-how-to-remove-a-package
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/shut-down-g5ad24366d_1280.jpg
tags:
- name: Node.js
  slug: nodejs
- name: npm
  slug: npm
seo_title: npm Uninstall – Comment supprimer un package
seo_desc: 'The Node Package Manager (NPM) provides various commands that let you work
  with packages.

  And just as you can install a package from the npm library, you can uninstall it.

  To uninstall a package, you can use the command provided by npm for the purpos...'
---

Le gestionnaire de packages Node (NPM) fournit diverses commandes qui vous permettent de travailler avec des packages.

Et tout comme vous pouvez installer un package depuis la bibliothèque npm, vous pouvez le désinstaller.

Pour désinstaller un package, vous pouvez utiliser la commande fournie par npm à cet effet – `npm uninstall`.

La manière de désinstaller un package régulier ou une dépendance n'est pas la même que pour désinstaller un package global et une dépendance de développement.

Dans cet article, je vais vous montrer comment désinstaller un package régulier, un package global et une dépendance de développement.

## Comment supprimer un package avec npm Uninstall

Pour supprimer un package avec la commande `npm uninstall`, vous pouvez utiliser la syntaxe `npm uninstall package-name` dans le répertoire où se trouve le package.

Le package que je vais utiliser pour démontrer comment un package est désinstallé est Express – un framework NodeJS.

Dans la capture d'écran ci-dessous, vous pouvez voir qu'Express est listé comme une dépendance dans le fichier `package.json`.
![ss-1](https://www.freecodecamp.org/news/content/images/2022/03/ss-1.png)

Mais après avoir exécuté `npm uninstall express`, vous ne verrez plus Express listé comme une dépendance :

![ss-2](https://www.freecodecamp.org/news/content/images/2022/03/ss-2.png)

Vous pouvez voir qu'il n'y a plus d'Express. Il n'y a même plus de clé de dépendance car il n'y a plus de dépendance.

## Comment supprimer une dépendance de développement avec npm Uninstall

Une dépendance de développement est un package utilisé uniquement pendant le développement.

Pour supprimer une dépendance de développement, vous devez ajouter le flag `-D` ou `--save-dev` à la commande npm uninstall, puis spécifier le nom du package.

La syntaxe de base pour cela est `npm uninstall -D package-name` ou `npm uninstall --save-dev package-name`.

Vous devez exécuter la commande dans le répertoire (dossier) où se trouve la dépendance.

Je vais utiliser Nodemon pour démontrer comment supprimer une dépendance de développement.

Nodemon permet à votre application NodeJS de se recharger automatiquement chaque fois qu'elle détecte un changement dans un fichier ou un dossier pendant le développement.

Dans la capture d'écran ci-dessous, vous pouvez voir que Nodemon est listé comme une dépendance de développement.
![ss-3](https://www.freecodecamp.org/news/content/images/2022/03/ss-3.png)

Pour le supprimer, je vais exécuter `npm uninstall –D nodemon`.
![ss-4](https://www.freecodecamp.org/news/content/images/2022/03/ss-4.png)

Vous pouvez voir qu'il n'y a plus de Nodemon dans le fichier `package.json`.

## Comment supprimer un package global avec npm Uninstall

Un package global est un package installé globalement sur votre machine, vous n'avez donc pas besoin de le réinstaller chaque fois que vous en avez besoin.

Pour supprimer un package global, vous devez ajouter le flag `-g` à la commande npm uninstall, puis spécifier le nom du package.

La syntaxe de base pour cela est `npm uninstall -g package-name`.

Pour vous montrer comment supprimer un package global, je vais utiliser un package appelé CORS (Cross-origin Resource Sharing).

CORS bloque la politique Same Origin Policy (SOP) des navigateurs afin que vous puissiez faire des requêtes d'un navigateur à un autre.

Dans la capture d'écran ci-dessous, vous pouvez voir que CORS n'est pas listé comme un package dans le fichier `package.json` :
![ss-5](https://www.freecodecamp.org/news/content/images/2022/03/ss-5.png)

CORS n'est pas listé car il est installé globalement sur ma machine, et non dans le répertoire d'un projet.

Si vous installez un package globalement et que vous souhaitez le voir, exécutez `npm list -g`.
![ss-6](https://www.freecodecamp.org/news/content/images/2022/03/ss-6.png)

Vous pouvez voir que CORS est maintenant listé comme un package global.

Pour désinstaller CORS globalement, je vais maintenant exécuter `npm uninstall -g cors`.

Après avoir exécuté la commande, vous pouvez voir qu'il n'y a plus de CORS lorsque j'exécute `npm list –g` :

![ss-7](https://www.freecodecamp.org/news/content/images/2022/03/ss-7.png)

## Conclusion

Dans cet article, vous avez appris les différentes manières de désinstaller divers types de packages NPM, afin de mieux contrôler votre base de code et de supprimer les packages inutiles.

Merci d'avoir lu.

Si vous trouvez cet article utile, partagez-le pour que d'autres puissent le voir.