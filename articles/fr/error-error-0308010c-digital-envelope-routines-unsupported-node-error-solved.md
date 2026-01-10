---
title: 'Erreur : error:0308010c:digital envelope routines::unsupported [Erreur Node
  résolue]'
date: '2022-11-10T18:39:19.000Z'
author: Kolade Chris
authorURL: https://www.freecodecamp.org/news/author/koladechris/
originalURL: https://freecodecamp.org/news/error-error-0308010c-digital-envelope-routines-unsupported-node-error-solved
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/envelope-1829509_1280.jpg
tags:
- name: error
  slug: error
- name: error handling
  slug: error-handling
- name: node
  slug: node
- name: node js
  slug: node-js
- name: React
  slug: react
seo_desc: "If you work with Node.js and command line interface solutions like Webpack,\
  \ create-react-app, or vue-cli-service, you might have encountered the error, Error:\
  \ error:0308010c:digital envelope routines::unsupported. \nYou’re not alone, because\
  \ I’m curre..."
---


Si vous travaillez avec Node.js et des solutions d'interface en ligne de commande (CLI) comme Webpack, `create-react-app` ou `vue-cli-service`, vous avez peut-être déjà rencontré l'erreur : `Error: error:0308010c:digital envelope routines::unsupported`.

<!-- more -->

Vous n'êtes pas seul, car je la rencontre également en ce moment :

![ss1-1](https://www.freecodecamp.org/news/content/images/2022/11/ss1-1.png)

L'application React a effectivement échoué à démarrer :

![ss2-1](https://www.freecodecamp.org/news/content/images/2022/11/ss2-1.png)

Dans cet article, vous apprendrez comment corriger cette erreur de 3 manières différentes. Mais d'abord, analysons les causes de cette erreur.

## Quelles sont les causes de l'erreur « 0308010c:digital envelope routines::unsupported » ?

Il est probable que vous obteniez cette erreur pour deux raisons principales :

-   Vous n'utilisez pas la version LTS (*long term support*) de Node.js. Vous pouvez voir que j'utilise Node 17.0.0, qui n'est pas une version LTS.
-   Vous utilisez `react-scripts` avec une version inférieure à 5.

L'erreur peut également survenir simplement du fait de l'utilisation de Node 17.

## Comment corriger l'erreur « 0308010c:digital envelope routines::unsupported »

Il existe au moins 3 façons de corriger cette erreur. Nous allons les examiner une par une. L'une d'entre elles devrait fonctionner pour vous.

### Passer `--openssl-legacy-provider` à Webpack ou à l'outil CLI

Dans une application React, par exemple, vous pouvez passer `--openssl-legacy-provider` au script de démarrage comme ceci : `"react-scripts --openssl-legacy-provider start"`.

Cela devrait suffire. Mais si cela ne corrige pas l'erreur, passez à la solution suivante. Dans de nombreux cas, cette méthode fonctionne.

### Utiliser une version LTS de Node JS

Envisagez de rétrograder votre version de Node vers la 16.16.0 ou d'autres versions LTS.

Actuellement, la version 18.12.1 est la dernière version LTS de Node. Vous pouvez la télécharger sur le site officiel de Node JS ou utiliser NVM pour l'installer.

### Mettre à jour react-scripts vers la version 5+

Si vous travaillez avec React et que les solutions précédentes n'ont pas fonctionné, il s'agit probablement d'un problème avec votre script React.

Si vous utilisez une version de `react-scripts` inférieure à 5, vous devriez la mettre à jour vers la version 5 ou supérieure.

Dans mon cas, j'utilise actuellement `react-scripts` 3.4.3 :

![ss3](https://www.freecodecamp.org/news/content/images/2022/11/ss3.png)

Pour mettre à jour `react-scripts` vers la version 5+, vous pouvez procéder de deux manières :

-   Désinstaller et réinstaller `react-scripts`
    
    -   Ouvrez le terminal et exécutez `npm uninstall react-scripts`
    -   Exécutez `npm install react-scripts`
-   Modifier manuellement la version du script React
    
    -   Allez dans votre fichier `package.json` et changez la version de `react-scripts` pour `5.0.2`
    -   Supprimez le dossier `node_modules` en exécutant `rm –rf node_modules`
    -   Supprimez le fichier `package-lock.json` en exécutant `rm –rf package-lock.json`
    -   Exécutez `npm install` ou `yarn add`, selon le gestionnaire de paquets que vous utilisez

Après avoir mis à jour la version de `react-scripts` vers la 5+, mon application React fonctionne désormais correctement :

![ss4](https://www.freecodecamp.org/news/content/images/2022/11/ss4.png)

![ss5](https://www.freecodecamp.org/news/content/images/2022/11/ss5.png)

## Conclusion

Comme nous l'avons souligné dans cet article, si vous obtenez l'erreur « 0308010c:digital envelope routines::unsupported », cela peut être dû au fait que vous n'utilisez pas une version LTS de Node JS, ou que vous utilisez une version de `react-scripts` inférieure à 5.

Nous espérons que les correctifs abordés dans ce tutoriel vous aideront à résoudre cette erreur. Si l'une des solutions ne fonctionne pas, essayez les autres. Dans mon cas, c'est la mise à jour de `react-scripts` vers la version 5+ qui a fonctionné.

Merci de votre lecture.