---
title: Comment configurer le débogueur pour l'extension Chrome dans Visual Studio
  Code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-30T21:38:53.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-the-debugger-for-chrome-extension-in-visual-studio-code-c0b3e5937c01
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XuUPNSTBAcqzuKXOABL-_w.png
tags:
- name: debugging
  slug: debugging
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment configurer le débogueur pour l'extension Chrome dans Visual Studio
  Code
seo_desc: 'By Victor A. Requena

  Debugging your web applications with Visual Studio Code makes you more efficient.
  It helps you save a lot of time and keeps your code cleaner. This is because you
  don’t have to write a bunch of console.logs and you can go through...'
---

Par Victor A. Requena

Déboguer vos applications web avec Visual Studio Code vous rend plus efficace. Cela vous fait gagner beaucoup de temps et garde votre code plus propre. En effet, vous n'avez pas à écrire une série de `console.log` et vous pouvez parcourir l'exécution de votre code ligne par ligne. Mais si vous êtes ici, vous connaissez probablement les avantages du débogage des applications web. Alors commençons...

### Installation

La première chose à faire est d'installer l'[extension Debugger for Chrome](https://marketplace.visualstudio.com/items?itemName=msjsdiag.debugger-for-chrome). Une fois installée, vous êtes presque prêt. La prochaine étape consiste à créer un fichier de lancement pour le débogueur de Visual Studio Code. Ce fichier contient les différentes configurations du débogueur pour votre projet.

Vous pouvez créer le fichier de lancement en allant dans la section de débogage de la barre d'activité et en cliquant sur l'icône d'engrenage.

![Image](https://cdn-media-1.freecodecamp.org/images/AUFWFZ8FQncLNTOIsD2at38qFq0GQOWErXm0)
_Cette icône d'engrenage._

Une liste d'options vous invitera à sélectionner celle de "Chrome".

![Image](https://cdn-media-1.freecodecamp.org/images/gV9J3xLjSklXcHaK4QdXWXzkkf1t84eh5OFO)
_Comme ceci._

Après avoir fait cela, vous aurez un répertoire `.vscode` avec un fichier `launch.json`.

### Configurations

Il existe deux types de configurations de débogage Chrome : `launch` et `attach`. Vous pouvez définir cela dans l'option `request` à l'intérieur de chaque objet de configuration.

#### Launch

La configuration de lancement _lance_ une instance de Chrome exécutant un fichier ou une URL spécifié. Si vous spécifiez une URL, vous devez définir `webRoot` sur le répertoire à partir duquel les fichiers sont servis. Cela peut être soit un chemin absolu, soit un chemin utilisant le résolveur `${workspaceFolder}`. Il s'agit du dossier ouvert dans votre espace de travail Visual Studio Code.

_Note : Soyez prudent lors de la définition de `webRoot`, cela est utilisé pour résoudre les URL en un fichier sur votre ordinateur._

Vous pouvez voir un exemple de deux configurations `launch` : l'une lancée contre un serveur local et l'autre contre un fichier local.

Si vous avez une instance de Chrome en cours d'exécution, celle lancée par le débogueur utilisera une session temporaire. Cela signifie que vous n'aurez pas vos extensions ou onglets ouverts. Si vous souhaitez lancer une instance de Chrome avec votre utilisateur et vos extensions, vous devez d'abord fermer toutes les instances en cours d'exécution.

_Note : Lorsque vous arrêtez le débogueur, cela fermera la fenêtre Chrome._

#### Attach

Je préfère personnellement utiliser celle-ci... Cette configuration attache le débogueur à une instance en cours d'exécution de Chrome. Mais pour que cette option fonctionne, vous devez lancer Chrome avec le débogage à distance activé. Le lancement d'une instance de Chrome avec le débogage à distance varie selon votre système d'exploitation.

#### Windows

Il existe deux façons de lancer Chrome avec le débogage à distance sous Windows. La plus simple consiste à faire un clic droit sur le raccourci de Google Chrome. Sélectionnez l'option propriétés et ajoutez la commande suivante dans le champ _cible_.

```
--remote-debugging-port=9222
```

_Note : Cela lancera Chrome avec le débogage à distance activé chaque fois que vous cliquerez sur le raccourci._

L'autre façon est d'ouvrir l'invite de commande et d'exécuter cette commande en remplaçant `<chrome_path>` par l'emplacement réel de votre installation de Chrome.

```
<chrome_path>\\chrome.exe --remote-debugging-port=9222
```

#### macOS

Ouvrez le terminal et exécutez la commande suivante :

```
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
```

#### Linux

Lancez votre terminal et exécutez cette commande :

```
google-chrome --remote-debugging-port=9222
```

Ce que cela fait — quel que soit le système d'exploitation — est d'ouvrir Chrome avec un indicateur, dans ce cas : `--remote-debugging-port`, et le définit sur `9222`. Vous pouvez en lire plus à ce sujet [ici](https://www.chromium.org/developers/how-tos/run-chromium-with-flags).

_Note : Si vous avez d'autres instances de Chrome en cours d'exécution sans débogage à distance, assurez-vous de les fermer avant d'en lancer une nouvelle._

Voici un exemple de configuration `attach`.

_Note : Si vous ne définissez pas l'option `"url"`, une liste sera affichée avec vos onglets ouverts._

Cette extension dispose de nombreuses options très utiles que vous pouvez utiliser pour adapter les configurations à votre projet. Vous pouvez lire la documentation de certaines d'entre elles [ici](https://github.com/Microsoft/vscode-chrome-debug#other-optional-launch-config-fields).

#### Résumé

Félicitations ! Vous avez appris comment installer et configurer le débogueur pour Chrome dans Visual Studio Code. Vous avez également appris comment lancer Google Chrome avec le débogage à distance activé. Maintenant, il est temps pour vous d'explorer et d'élargir vos nouvelles connaissances... Je vous recommande vivement de jeter un coup d'œil au [dépôt](https://github.com/Microsoft/vscode-chrome-debug) de l'extension.

J'espère que vous avez apprécié cet article. Vous pouvez me trouver sur Twitter [@_svictoreq](https://twitter.com/_svictoreq). ?