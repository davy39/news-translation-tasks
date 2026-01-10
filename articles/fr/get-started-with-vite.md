---
title: Tutoriel Vite.js – Comment installer et utiliser Vite dans vos projets web
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-04-26T21:41:58.000Z'
originalURL: https://freecodecamp.org/news/get-started-with-vite
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/getting-started-with-vite.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: Web Development
  slug: web-development
seo_title: Tutoriel Vite.js – Comment installer et utiliser Vite dans vos projets
  web
seo_desc: 'By Popoola Temitope

  Vite.js is a rapid development tool for modern web projects. It focuses on speed
  and performance by improving the development experience.

  Vite uses native browser ES imports to enable support for modern browsers without
  a build pr...'
---

Par Popoola Temitope

[Vite.js](https://www.freecodecamp.org/news/p/e534a679-ce3c-4cf1-842b-96087d30944d/Vite.js) est un outil de développement rapide pour les projets web modernes. Il se concentre sur la vitesse et la performance en améliorant l'expérience de développement.

Vite utilise les imports ES natifs du navigateur pour permettre la prise en charge des navigateurs modernes sans processus de construction.

Vite se compose de deux parties principales :

* Le serveur de développement fournit une prise en charge du Hot Module Replacement (HMR) pour la mise à jour des modules pendant l'exécution de l'application. Lorsque des modifications sont apportées au code source d'une application, seules les modifications sont mises à jour, plutôt que de recharger l'ensemble de l'application. Cette fonctionnalité aide à accélérer le temps de développement.
* La commande de construction permet aux développeurs de bundler leur code avec Rollup, pré-configuré pour produire des actifs statiques hautement optimisés pour la production.

## Comment fonctionne Vite.js

Lorsque les modules ES ont été introduits dans ES2015, de nombreux navigateurs avaient un faible support pour les modules ES6. Pour remédier à cela, les navigateurs modernes supportent désormais les modules ES natifs. Cela permet aux développeurs d'utiliser les instructions `import` et `export` de manière native.

Dans ES natif, l'import doit obtenir soit une URL relative ou absolue car il ne supporte pas les imports de modules nus tels que :

```js
import { someMethod } from 'my-dep'
```

Le code ci-dessus générera une erreur dans le navigateur car de nombreux navigateurs ne supportent pas les modules ES6. La question est donc de savoir comment Vite gère cela ?

Vite détectera automatiquement les imports de modules nus depuis vos fichiers sources et effectuera les deux actions suivantes sur eux :

* Vite pré-bundlera les fichiers sources pour accélérer le chargement des pages et convertir les modules CommonJS / UMD en ESM.
* Pour permettre aux navigateurs d'importer des modules sans générer d'erreurs, Vite réécrira les imports en URLs valides comme ceci

```
/node_modules/.vite/my-dep.js?v=f3sf2ebb
```

# Pourquoi utiliser Vite ?

Maintenant que nous savons ce qu'est Vite et comment il fonctionne, vous vous demandez peut-être pourquoi vous devriez utiliser Vite.

Il y a de nombreuses raisons pour lesquelles vous devriez utiliser Vite pour votre projet. Jetons un bref coup d'œil à certaines d'entre elles.

## Performance

Le pré-bundling avec ESbuild de Vite le rend 10 à 100 fois plus rapide que l'utilisation de tout autre bundler JS. Cela est dû au fait qu'il aide à améliorer la vitesse des pages et à convertir les modules CommonJS / UMD en ESM.

Selon la documentation de Vite,

> "L'étape de pré-bundling est effectuée avec esbuild et rend le temps de démarrage à froid de Vite significativement plus rapide que tout bundler basé sur JavaScript."

## Hot Module Replacement (HMR)

Vite utilise les fonctionnalités HMR pour suivre les changements dans votre application sans recharger la page complète. Avec l'API HMR, le navigateur ne chargera que la section modifiée de la page et conservera l'état de l'application.

Il n'est pas nécessaire de configurer manuellement l'API HMR dans votre application. Elle est automatiquement ajoutée à votre projet lors de l'installation de l'application.

Avec les performances HMR, vous pouvez concevoir des applications plus légères et plus rapides, quel que soit le nombre de modules ou la taille de votre application.

## Options de configuration

Vite vous permet d'avoir plus de contrôle sur la configuration de votre projet en étendant la configuration par défaut avec `vite.config.js` ou `vite.config.ts`. Ces fichiers sont situés dans le répertoire racine de base du projet.

Vous pouvez également spécifier différents fichiers de configuration avec l'option CLI `--config`, comme montré ci-dessous :

```bash
vite --config my-config.js
```

# Ce dont vous aurez besoin

Vous devez avoir les logiciels suivants installés sur votre ordinateur avant de pouvoir créer un projet Vite :

* [Node.js version 12.2.0](https://nodejs.org/en/download/) ou supérieure (pour vérifier si vous avez Node installé sur votre ordinateur, exécutez **`node -v`** dans le terminal)
* [Npm](https://www.npmjs.com/get-npm) / [Yarn](https://classic.yarnpkg.com/en/)

Une fois que vous avez installé ces logiciels sur votre ordinateur, vous pouvez maintenant créer un projet Vite.

# Comment créer un projet Vite

Pour créer une application Vite, ouvrez votre terminal et naviguez vers le dossier où vous souhaitez enregistrer le programme Vite. Ensuite, exécutez cette commande :

```bash
npm create @vitejs/app my-vite-app
```

**Note :** **`my_vite_app`** est le nom de l'application Vite que nous voulons créer. Vous pouvez le changer pour le nom que vous préférez.

Après avoir exécuté la commande ci-dessus, vous serez invité à sélectionner un `framework` et le `template` (variante). Pour les besoins de ce tutoriel, nous utiliserons React, mais vous pouvez sélectionner n'importe quel framework et template avec lesquels vous êtes familier.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/v-edit-1.jpg)

Ensuite, exécutez les commandes suivantes pour terminer l'installation :

```bash
cd vite_application
npm install
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/v-edit-1.png)

L'installation peut prendre quelques minutes, alors attendez simplement qu'elle soit terminée.

# Comment exécuter une application Vite

Pour exécuter votre application Vite dans le terminal, naviguez vers le dossier de l'application (`vite_application`) puis exécutez la commande dev ci-dessous pour démarrer le serveur de développement :

```bash
npm run dev
```

L'exécution de la commande ci-dessus démarrera le serveur de développement. Ensuite, ouvrez votre terminal et entrez [`http://localhost:3000`](http://localhost:3000).

Vous devriez voir quelque chose comme ceci dans le navigateur :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/vite-4.PNG)
_Application React_

# Structure des dossiers Vite

Examinons comment les dossiers des applications Vite sont organisés. Nous examinerons également quelques-uns des dossiers et fichiers en détail.

Note : si vous utilisez un framework et un template différents, le nom du fichier ne sera pas le même.


![Image](https://lh5.googleusercontent.com/Fgo6venfe73MifwcmqHXjOtatI5uix9yksTqNDoUpGXGQoyEiIozkcQ1sqrSOr1LQWBQuVWn3keKoY71aqFY91vjpOgFY2hpHV_7RfmuoV5hGerJqBzBLCfiA6FsjTmnMS-dcf-E)
_Structure des dossiers Vite_

### **Dossier node_modules**

Le dossier node_modules contient toutes les dépendances nécessaires pour l'application, qui sont spécifiées dans le fichier package.json.

Toutes les dépendances configurées dans package.json seront téléchargées dans le dossier node_modules une fois la commande `npm install` exécutée.

Lorsque vous poussez votre code source vers GitHub, vous n'avez pas besoin de pousser le dossier node_modules car les utilisateurs peuvent installer toutes les dépendances nécessaires utilisées dans votre application via le package.json.

Vous pouvez trouver le fichier package.json dans le répertoire racine parent de l'application.

### **Dossier src**

Le dossier src est l'un des dossiers avec lesquels nous interagissons le plus lors du développement d'applications Vite. Ce dossier contient app.jsx, main.jsx, app.css et index.js.

Tous les actifs de votre application, tels que les images, les vidéos et autres fichiers, doivent être stockés dans le dossier src car Vite rebases automatiquement toutes les URLs à l'intérieur de index.html.

### App.jsx et main.jsx

Le fichier app.jsx est le composant de base qui sert de conteneur pour tous les autres composants utilisés dans l'application.

Le fichier main.jsx est l'endroit où vous ciblez l'ID racine depuis le index.html et rendez tous les composants utilisés dans l'application.

### index.css et app.css

Ces fichiers contiennent tous les styles CSS utilisés dans le programme. Vous pouvez ajouter votre propre fichier CSS ou changer le style.

# Conclusion

Nous avons examiné ce qu'est Vite, comment il fonctionne et certaines de ses fonctionnalités. Nous avons également appris comment créer des applications Vite.

Afin d'améliorer votre flux de travail de développement et d'être plus productif en créant des applications plus légères et plus rapides, vous pouvez en apprendre davantage sur [Vite dans sa documentation](https://vitejs.dev/).