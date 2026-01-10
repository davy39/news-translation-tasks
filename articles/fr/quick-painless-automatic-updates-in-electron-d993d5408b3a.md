---
title: Mises à jour rapides, indolores et automatiques dans Electron
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-28T16:43:32.000Z'
originalURL: https://freecodecamp.org/news/quick-painless-automatic-updates-in-electron-d993d5408b3a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*afd_KNE6oIHoqycO5GlDXA.jpeg
tags:
- name: development
  slug: development
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Mises à jour rapides, indolores et automatiques dans Electron
seo_desc: 'By Andrea Zanin

  Let’s face it: most users won’t go back to your site and download the updates for
  your brand new Electron app. Instead, you should put in place some kind of automatic
  update system.

  Unfortunately, the online documentation for this is ...'
---

Par Andrea Zanin

Admettons-le : la plupart des utilisateurs ne retourneront pas sur votre site pour télécharger les mises à jour de votre toute nouvelle application Electron. Au lieu de cela, vous devriez mettre en place un système de mise à jour automatique.

Malheureusement, la documentation en ligne pour cela n'est ni très facile à trouver ni à suivre. Ici, je vais vous guider à travers un processus rapide pour configurer un auto-updater, en utilisant GitHub comme hôte.

### Configuration du dépôt

Pour publier en votre nom, electron-builder a besoin d'un jeton d'accès GitHub. Si vous ne savez pas ce que c'est ou comment en créer un, consultez le [guide rapide](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/) de GitHub.

Electron-builder a besoin d'un jeton avec accès au scope du dépôt. Créez-en un comme décrit dans le lien, et copiez-le quelque part en sécurité (vous ne verrez le jeton qu'une seule fois !).

### Configuration de la bibliothèque

Nous allons utiliser [electron-builder](https://github.com/electron-userland/electron-builder) pour packager notre application, alors commençons par l'installer :

```
npm install electron-builder --save-dev
```

Installons aussi [electron-updater](https://github.com/electron-userland/electron-builder/tree/master/packages/electron-updater) pour gérer les mises à jour automatiques :

```
npm install electron-updater --save
```

Ensuite, nous devons configurer notre build. Dans le `package.json`, ajoutez ce snippet :

Analysons cela bit par bit :

* Le lien `repository` est assez explicite — n'oubliez pas de le remplacer par le vôtre !
* Le script `build` construira votre application localement, sans publier.
* Le script `ship` construira et publiera votre application.

**Note pour les développeurs React** : electron-builder et create-react-app ont quelques conflits par défaut. J'ai créé un générateur qui configure une application electron+react+electron-builder sans aucune configuration nécessaire. Vous pouvez le trouver [ici](https://www.npmjs.com/package/generator-react-electron).

Maintenant, créez un fichier appelé `electron-builder.yml` avec le contenu suivant :

* L'`appId` est le nom de votre application dans le registre du système d'exploitation. Vous pouvez le choisir librement.
* Le `provider` est la plateforme qui stockera l'installateur de votre application.
* Le `token` est le jeton d'accès GitHub. Remplacez-le par celui que vous avez créé précédemment.

N'oubliez pas d'ajouter ce fichier au `.gitignore` pour ne pas partager votre jeton avec le monde entier ! ;)

### Gestion de la logique de mise à jour

Maintenant, nous devons configurer la logique de mise à jour dans notre application Electron. Intégrez cela dans votre fichier d'entrée (généralement `index.js` ou `electron.js`). Si vous créez une toute nouvelle application, vous pouvez simplement copier-coller le code ci-dessous :

Les modules IPC sont le moyen standard d'envoyer des messages entre les processus dans Electron. Vous pouvez en apprendre plus à leur sujet [ici](https://github.com/electron/electron/blob/master/docs/api/ipc-main.md).

Le code est assez explicite et gère le côté Electron de la mise à jour. Maintenant, nous devons notifier l'utilisateur.

Voici un exemple de page HTML. Elle affiche un bouton dont la légende est soit « aucune mise à jour prête » soit « nouvelle version prête ! ». Lorsque le bouton est cliqué, une méthode est appelée qui indique à Electron de quitter et d'installer les nouvelles mises à jour.

### Et enfin, publier

Lorsque vous êtes prêt à publier, modifiez le champ `version` dans le `package.json` et exécutez la commande suivante :

```
npm run ship
```

Allez sur la page GitHub de votre dépôt et cliquez sur 'releases' (c'est sur la même ligne que 'commits' et 'branch'). Là, vous trouverez une version brouillon. Cliquez sur 'edit' puis sur 'publish release'.

Ne paniquez pas si le bouton affiche « aucune mise à jour prête » lorsque vous démarrez l'application. Cela ne changera qu'après avoir terminé le téléchargement de la nouvelle version.

Si vous souhaitez utiliser un projet fonctionnel pour en apprendre plus et commencer, vous pouvez cloner [ce dépôt d'exemple](https://github.com/ZaninAndrea/electron-autoupdate-example).

Si vous avez trouvé cet article utile, n'oubliez pas d'applaudir ?.