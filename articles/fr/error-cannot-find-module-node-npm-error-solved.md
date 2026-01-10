---
title: 'Erreur : impossible de trouver le module [Erreur Node npm Résolue]'
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-11-09T15:37:57.000Z'
originalURL: https://freecodecamp.org/news/error-cannot-find-module-node-npm-error-solved
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/factory-4757647_1280.jpg
tags:
- name: error
  slug: error
- name: node
  slug: node
- name: npm
  slug: npm
- name: Web Development
  slug: web-development
seo_title: 'Erreur : impossible de trouver le module [Erreur Node npm Résolue]'
seo_desc: 'If you’re a developer that works with Node JS and JavaScript libraries
  and frameworks like React, Vue, and Angular, then you might have encountered the
  "Error: cannot find module" error.

  In this article, I’m going to show you how to fix the error.

  Wh...'
---

Si vous êtes un développeur qui travaille avec Node JS et des bibliothèques et frameworks JavaScript comme React, Vue et Angular, vous avez peut-être rencontré l'erreur "Erreur : impossible de trouver le module".

Dans cet article, je vais vous montrer comment corriger cette erreur.

## Pourquoi l'erreur "Erreur : impossible de trouver le module" se produit
Cette erreur se produit pour les raisons suivantes : 
- vous essayez d'importer un élément d'un module que vous n'avez pas installé dans votre répertoire de projet
- vous importez des éléments d'un package obsolète
- vous pointez vers un fichier qui n'existe pas

Dans la capture d'écran ci-dessous, vous pouvez voir que j'obtiens l'erreur :

![ss1](https://www.freecodecamp.org/news/content/images/2022/11/ss1.png)

J'obtiens l'erreur parce que j'essaie d'importer l'icône freeCodeCamp du package react-icons, que je n'ai pas installé.

```js
import { FaFreeCodeCamp } from "react-icons/fa";
```

## Comment corriger l'erreur "impossible de trouver le module"
Si vous obtenez cette erreur, la solution est toujours dans l'erreur. Le module (package) non trouvé est toujours spécifié au format "Module non trouvé : Erreur : Impossible de résoudre 'nom du package' dans 'répertoire du projet'". 

Dans mon cas, je l'ai obtenu comme ceci "Module non trouvé : Erreur : Impossible de résoudre 'react-icons/fa' dans 'C:\Users\user\Desktop\Projects\Address Locator\address-locator\src'".

Pour corriger l'erreur, vous devez installer le package qui est absent dans votre répertoire de projet – `npm install nom-du-package` ou `yarn add nom-du-package`.

Dans mon cas, je dois installer le package `react-icons` pour que l'icône freeCodeCamp puisse être résolue. Je vais le faire en exécutant `yarn add react-icons`.

Une fois que j'ai installé le package et exécuté l'application, tout devrait compiler avec succès :

![ss2](https://www.freecodecamp.org/news/content/images/2022/11/ss2.png) 

Si vous installez le package mais que vous obtenez toujours l'erreur, suivez les étapes ci-dessous :
- supprimez le dossier node_modules en exécutant ` rm -rf node_modules`
- supprimez le fichier package-lock.json en exécutant ` rm -f package-lock.json`
- nettoyez le cache NPM en exécutant ` npm cache clean --force`
- installez tous les packages à nouveau en exécutant `npm install`

Cela devrait corriger l'erreur pour vous.

## Conclusion
Lorsque vous obtenez l'erreur "impossible de trouver le module" ou "module non trouvé", cela signifie que vous n'avez pas installé le package que vous essayez d'utiliser. 

Si l'erreur se produit même si vous avez installé le package, les correctifs suggérés dans cet article peuvent vous aider.

Merci d'avoir lu.