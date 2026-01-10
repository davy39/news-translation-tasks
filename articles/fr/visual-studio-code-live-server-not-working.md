---
title: Visual Studio Code Live Server ne fonctionne pas
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-14T09:28:00.000Z'
originalURL: https://freecodecamp.org/news/visual-studio-code-live-server-not-working
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9941740569d1a4ca1eab.jpg
tags:
- name: Browsers
  slug: browsers
- name: Google Chrome
  slug: chrome
- name: Visual Studio Code
  slug: visual-studio-code
- name: Visual Studio Code
  slug: vscode
seo_title: Visual Studio Code Live Server ne fonctionne pas
seo_desc: "VSCode has a lot of great extensions, and Live Server is one of the best.\
  \ \nWith just a couple of clicks, Live Server lets you see your page live in an\
  \ actual browser. Better yet, it features live reloading, so if you update your\
  \ code, the changes are..."
---

VSCode dispose de nombreuses extensions géniales, et [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) est l'une des meilleures. 

En quelques clics, Live Server vous permet de voir votre page en direct dans un navigateur réel. Mieux encore, il offre un rechargement en direct, donc si vous mettez à jour votre code, les modifications sont également reflétées dans le navigateur.

Tout ce que vous avez à faire est de faire un clic droit dans le fichier HTML que vous souhaitez visualiser, puis de sélectionner "Open with Live Server" :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/live-server-ex.gif)
_Live Server en action_

Mais que faire si Live Server n'ouvre pas votre navigateur et n'affiche pas votre page comme vous le souhaitez ? Si cela vous arrive, voici quelques solutions à essayer.

## Redémarrer VSCode

Parfois, la meilleure solution est de redémarrer VSCode.

Tout d'abord, sauvegardez tout votre travail. Ensuite, fermez VSCode, ce qui arrêtera également toutes les extensions que vous avez installées.

Puis, rouvrez VSCode et essayez à nouveau – allez dans le fichier HTML que vous souhaitez visualiser, faites un clic droit et sélectionnez "Open with Live Server".

## Définir le navigateur pour Live Server

Il est possible que l'extension fonctionne, mais que votre système n'ait pas de navigateur par défaut.

Même si vous avez défini le navigateur par défaut pour votre système, il ne serait pas inutile de laisser Live Server savoir quel navigateur vous souhaitez utiliser explicitement.

Tout d'abord, ouvrez la palette de commandes avec F1, puis tapez `Preferences: Open Settings (JSON)` et sélectionnez cette option.

Cela ouvrira votre fichier `settings.json` de VSCode.

Faites défiler jusqu'en bas du fichier, ajoutez une virgule après le dernier paramètre, puis collez `"liveServer.settings.CustomBrowser": "chrome"` :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/settings-json.gif)

Notez que vous pouvez également utiliser `"firefox"`, `"safari"`, ou tout autre navigateur comme valeur pour le paramètre `"liveServer.settings.CustomBrowser"`.

Enfin, sauvegardez le fichier `settings.json` et essayez de relancer Live Server.

## Définir le navigateur par défaut pour votre système d'exploitation

Même après avoir indiqué à Live Server quel navigateur vous souhaitez utiliser, il est possible qu'il n'ouvre toujours pas votre page dans ce navigateur correctement.

La prochaine chose à essayer est de définir le navigateur par défaut pour votre système d'exploitation lui-même.

La méthode exacte pour faire cela peut varier en fonction de votre système d'exploitation, il est donc préférable de rechercher comment faire si vous n'êtes pas sûr.

Voici à quoi ressemble la page des paramètres dans Windows :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-56.png)
_Crédit : [Advitya-sharma](https://forum.freecodecamp.org/u/Advitya-sharma)_

## Accéder à la page live vous-même

Si pour une raison quelconque Live Server n'ouvre toujours pas la page dans votre navigateur automatiquement, pas de souci. Vous pouvez toujours ouvrir le navigateur de votre choix et visualiser la page directement.

Ouvrez simplement votre navigateur préféré et allez à `http://127.0.0.1:5500/<votre_nom_de_fichier>`.

Par exemple, si votre fichier s'appelle `index.html`, allez simplement à `http://127.0.0.1:5500/index.html`.

Tant que Live Server est en cours d'exécution, vous devriez voir votre page.

## En conclusion

Voici quelques solutions courantes à essayer si Live Server ne fonctionne pas comme vous le souhaitez.

Restez en sécurité et bon codage (en direct).