---
title: Comment forcer l'utilisation de Yarn ou NPM
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-17T07:03:09.000Z'
originalURL: https://freecodecamp.org/news/how-to-force-use-yarn-or-npm
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/how-to-force-use-yarn-or-npm-facebook.jpg
tags:
- name: npm
  slug: npm
- name: Yarn
  slug: yarn
seo_title: Comment forcer l'utilisation de Yarn ou NPM
seo_desc: "By Carol-Theodor Pelu\nIn this short post, I’m going to show you how to\
  \ prevent the usage of npm or yarn, depending on your needs. \nThis comes in handy\
  \ when your team or organization has a preference for a specific package manager.\
  \ \nWith this method, ..."
---

Par Carol-Theodor Pelu

Dans ce court article, je vais vous montrer comment empêcher l'utilisation de _npm_ ou _yarn_, selon vos besoins. 

Cela s'avère utile lorsque votre équipe ou votre organisation a une préférence pour un gestionnaire de paquets spécifique. 

Avec cette méthode, vous vous assurez que tout le monde utilisera le même gestionnaire de paquets.

Commençons !

Vous voulez regarder une vidéo sur la façon de faire cela ? Consultez celle-ci :

%[https://www.youtube.com/watch?v=RmpVlaocd0M]

## Modifier .npmrc

Vous n'avez peut-être pas ce fichier dans votre base de code. Si c'est le cas, créez ce fichier dans le dossier racine de votre application.

Il nous permet de spécifier les configurations du gestionnaire de paquets et il est utilisé à la fois par _npm_ et _yarn_.

Votre fichier `.npmrc` doit avoir la propriété `engine-strict` définie sur `true`.

```config
//.npmrc file

engine-strict = true
```

Cette option indique au gestionnaire de paquets d'utiliser la version des moteurs que nous avons spécifiée dans le fichier `package.json`.

## Modifier package.json

À l'intérieur de votre fichier `package.json`, vous devez ajouter la section `engines` si vous ne l'avez pas déjà.

```json

//package.json
{ 
  ...
  "engines": {
    "npm": "please-use-yarn",
    "yarn": ">= 1.19.1"
  },
  ...
}
```

Dans le code ci-dessus, le fichier `package.json` utilise une version de `yarn` 1.19.1 ou supérieure.  
Mais pour `npm`, nous spécifions une version qui n'existe pas.

De cette manière, nous nous assurons que lorsque quelqu'un essaie d'utiliser `npm` au lieu de `yarn`, il recevra une erreur qui affiche '`please-use-yarn`'.

## Exécuter npm install

Une fois que vous avez apporté les modifications ci-dessus, essayez d'exécuter `npm install`.

Vous recevrez une erreur qui vous empêche d'utiliser `npm`.

```bash

npm ERR! code ENOTSUP
npm ERR! notsup Unsupported engine for my-app@0.1.0: wanted: {"npm":"please-use-yarn","yarn":">= 1.19.1"} (current:
 {"node":"12.16.3","npm":"6.14.4"})
npm ERR! notsup Not compatible with your version of node/npm: my-app@0.1.0
npm ERR! notsup Not compatible with your version of node/npm: my-app@0.1.0
npm ERR! notsup Required: {"npm":"please-use-yarn","yarn":">= 1.19.1"}
npm ERR! notsup Actual:   {"npm":"6.14.4","node":"12.16.3"}

npm ERR! A complete log of this run can be found in:
npm ERR!     C:\Users\YourUser\AppData\Roaming\npm-cache\_logs\2020-05-21T10_21_04_676Z-debug.log

```

Bien sûr, cela peut être fait dans l'autre sens si vous souhaitez empêcher l'utilisation de `yarn`.

## Conclusion

C'est assez simple et facile de s'assurer qu'un seul gestionnaire de paquets doit être utilisé dans votre projet.  
  
Cela réduira les risques d'erreurs causées par les développeurs utilisant différents gestionnaires de paquets et c'est une bonne pratique pour standardiser les règles de codage et de gestion du projet.

Vous pouvez me contacter et me poser des questions sur [Twitter](https://twitter.com/pelu_carol), [Facebook](https://www.facebook.com/neutrondevcom) et mon [site web](https://neutrondev.com/).