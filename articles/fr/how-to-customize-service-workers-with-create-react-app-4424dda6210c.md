---
title: Comment personnaliser les service workers avec create-react-app
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-30T23:43:40.000Z'
originalURL: https://freecodecamp.org/news/how-to-customize-service-workers-with-create-react-app-4424dda6210c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8ZTUXbW0X2a2ck85dNxQtA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Comment personnaliser les service workers avec create-react-app
seo_desc: 'By Zaid Humayun

  This is a follow up to my previous post about building a PWA with create-react-app
  (CRA). In the linked post, I discussed how we could go about building a custom Service
  Worker (SW) while staying within the create-react-app shell.

  If ...'
---

Par Zaid Humayun

Ceci est un suivi de mon [précédent article](https://medium.freecodecamp.org/how-to-build-a-pwa-with-create-react-app-and-custom-service-workers-376bd1fdc6d3) sur la création d'une PWA avec create-react-app (CRA). Dans l'article lié, j'ai discuté de la manière dont nous pourrions créer un Service Worker (SW) personnalisé tout en restant dans l'environnement create-react-app.

Si vous avez suivi l'article (et espérons-le, l'avez fait fonctionner), vous aurez remarqué un défaut critique. Il est toujours extrêmement difficile de développer un SW dans un environnement de développement. Essentiellement, vous devriez modifier votre code SW, exécuter un processus de construction, le tester, corriger les bugs, actualiser et répéter. Parlant d'expérience, c'est un processus épuisant.

Allons-y et découvrons comment résoudre ce problème.

### **Travailler en mode développement**

D'accord, alors comment faire fonctionner un SW en mode développement, afin que nous puissions rapidement écrire du code, et déterminer ce qui fonctionne et ce qui ne fonctionne pas ?

Tout d'abord, découvrons pourquoi cela ne fonctionne pas en mode développement. Créez un nouveau projet CRA, et ouvrez le fichier `registerServiceWorker.js` sous le répertoire `src`.

Dans le gist ci-dessus, je n'ai que la partie pertinente du code. Vous remarquerez une vérification conditionnelle `process.env.NODE_ENV === 'production'`. Cela vérifie si vous exécutez une version de production. Si vous n'exécutez pas une version de production, le SW sera remplacé par un fichier no-op.

La raison derrière cette décision est fournie dans ce [problème GitHub](https://github.com/facebook/create-react-app/issues/2396).

Tout d'abord, essayez d'exécuter `yarn start` sur votre application et vérifiez la présence d'un fichier SW dans la fenêtre de la barre d'outils. Si vous cliquez sur le lien `service-worker.js` dans la barre d'outils, vous verrez le fichier suivant :

Heureusement, il existe une solution simple à ce problème. C'est un processus facile en deux étapes.

Tout d'abord, à l'intérieur du fichier `registerServiceWorker.js`, recherchez l'appel de fonction `window.addEventListener('load')`. La première ligne est une déclaration pour `swUrl` qui dit :

```
const swUrl = `${process.env.PUBLIC_URL}/service-worker.js`;
```

Renommez la partie `service-worker` avec autre chose. Je vais nommer le mien `service-worker-custom.js`.

Deuxièmement, créez un fichier à l'intérieur de votre répertoire public avec le **même nom exact** que le nom personnalisé que vous venez de choisir. Donc, je créerais un fichier appelé `service-worker-custom.js` à l'intérieur du répertoire public.

Maintenant, à l'intérieur du fichier `service-worker-custom.js`, placez une simple instruction de journalisation. Quelque chose comme : `console.log('Mon service worker personnalisé')`.

Maintenant, exécutez à nouveau votre application avec `yarn start` et vous devriez voir l'instruction de journalisation apparaître dans la console de votre navigateur. Vous devrez peut-être désenregistrer un service worker précédent si vous avez déjà exécuté yarn start auparavant.

Donc, vous y êtes. Un service worker personnalisé que vous pouvez exécuter en toute sécurité en mode développement.

**Note : Il est déconseillé de tester un service worker dans un environnement de développement en dehors du mode de navigation privée de votre navigateur. De plus, assurez-vous toujours que "Update On Reload" est coché dans votre fenêtre d'outils de développement lorsque vous testez en mode développement.**

### **Combiner Dev et Prod**

Maintenant, nous avons découvert comment tester un SW en mode développement. Cependant, nous devons également trouver un moyen d'injecter notre code personnalisé dans le SW généré par CRA dans une version de production.

Si vous gardez tout tel quel avec les configurations que nous avons faites jusqu'à présent et exécutez un processus de construction et vérifiez la construction dans votre navigateur, vous remarquerez que le fichier SW généré est celui que nous avons créé. C'est un problème, car nous voulons pouvoir combiner les avantages de ce que CRA a à nous offrir avec notre propre code.

Nous pouvons faire cela avec la bibliothèque `sw-precache`. J'ai introduit cette bibliothèque dans mon [précédent article](https://medium.freecodecamp.org/how-to-build-a-pwa-with-create-react-app-and-custom-service-workers-376bd1fdc6d3). Voici le [lien GitHub](https://github.com/GoogleChromeLabs/sw-precache) vers la bibliothèque `sw-precache`.

Installez la bibliothèque avec `yarn add sw-precache`. Une fois que vous avez fait cela, créez un fichier `sw-precache-config.js` dans votre répertoire racine. Voici mon fichier :

J'ai introduit la plupart de ce fichier dans le [précédent article](https://medium.freecodecamp.org/how-to-build-a-pwa-with-create-react-app-and-custom-service-workers-376bd1fdc6d3). La seule nouvelle partie est l'option `importScripts`. Cela est assez explicite, il importe simplement le fichier spécifié par le chemin, et nous essayons d'importer notre fichier SW personnalisé.

Vous remarquerez que le chemin du fichier manque du préfixe `./public`, malgré la présence du fichier dans notre répertoire `public`. Je vais expliquer cela dans un instant.

Maintenant, mettez à jour votre fichier `package.json` avec une modification de la commande `build`. Faites en sorte que votre commande `build` soit la suivante :

`react-scripts build && sw-precache --config=sw-precache-config.js`

Maintenant, revenons au chemin de fichier que nous avons fourni à l'option importScripts. Si vous remarquez, le `sw-precache` s'exécute essentiellement comme un processus post-construction. Maintenant, si vous exécutez simplement un processus de construction, et ouvrez le répertoire de construction qui est créé, vous remarquerez votre fichier de service worker personnalisé dans le dossier de construction. Lorsque nous fournissons un chemin à l'option `importScripts`, nous le fournissons par rapport au répertoire de construction !

Une fois que vous avez fait tout cela, allez-y et exécutez la version de construction de votre application, et vous remarquerez que l'instruction de journalisation apparaît une fois de plus dans la console de votre navigateur.

Eh bien, vous y êtes ! Vous pouvez maintenant injecter du code SW personnalisé dans le SW par défaut généré par CRA !