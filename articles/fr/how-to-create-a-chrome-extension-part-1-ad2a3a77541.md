---
title: Comment créer une extension Chrome
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-12T12:52:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-chrome-extension-part-1-ad2a3a77541
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7aJPlxn8gwhI7JjcBFr-tQ.jpeg
tags:
- name: Google Chrome
  slug: chrome
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment créer une extension Chrome
seo_desc: 'By Erika Tan

  In this article, I will be teaching you how to make a Chrome Extension of your own.
  I’m basing it off of lessons learned while creating TalkToMe, a Chrome Extension
  that helps the visually impaired by reading website content and navigati...'
---

Par Erika Tan

Dans cet article, je vais vous apprendre à [créer votre propre extension Chrome](https://developer.chrome.com/extensions/getstarted). Je m'appuie sur les leçons apprises lors de la création de [TalkToMe](https://github.com/PalashTanejaPro/BlindHelper), une extension Chrome qui aide les malvoyants en lisant le contenu des sites web et en naviguant vers d'autres pages web.

Je vais couvrir les bases de la configuration de votre extension, y compris :

* Configurer les fichiers pour l'installation
* La préparer pour la mettre sur le Chrome Store

> Je ne couvrirai pas la gestion des fonctionnalités audio, comme la gestion des permissions du micro. Cela a été couvert dans [cet article](https://medium.com/@tanejapalash/handling-mic-input-permissions-and-speech-recognition-in-chrome-extensions-ff7e3ca84cb0) par mon ami Palash et utilise également l'extension [TalkToMe](https://github.com/PalashTanejaPro/BlindHelper) comme exemple.

#### Configurer les fichiers pour l'installation

Tout d'abord, allez à **chrome://extensions** dans votre navigateur, ou cliquez simplement sur "Plus d'outils" et "Extensions" dans le menu Chrome. Cela devrait vous mener à la page de gestion des extensions, où vous pouvez **activer le mode développeur** (il devrait se trouver dans le coin supérieur droit).

Ensuite, vous devrez créer un fichier `manifest.json` dans un nouveau répertoire pour votre extension. Ce fichier fournit des informations importantes pour le fonctionnement de votre extension, telles que les permissions et les fichiers de script que vous allez lier à votre projet. Voici à quoi devrait ressembler le contenu de votre manifest :

```
{    "name": "Exemple d'extension Chrome",    "version": "1.0",    "description": "Construisez une extension !",    "manifest_version": 2}
```

Pour télécharger votre répertoire sur la page de gestion des extensions, cliquez sur le bouton "Charger l'extension décompressée" et sélectionnez votre répertoire. Cela liera vos fichiers à l'interface utilisateur basée sur le web.

Un autre fichier important que vous devrez configurer est `background.js`, qui est le script d'arrière-plan de votre projet.

Un script d'arrière-plan d'exemple a cette structure :

```
chrome.runtime.onInstalled.addListener(function() {    // ajoutez une action ici});
```

Il fonctionnera toujours lorsque votre extension sera activée et est utile pour écouter différents événements, comme les pressions sur le clavier, ou pour naviguer vers différentes pages.

Vous pouvez même avoir plusieurs scripts d'arrière-plan. Vous devez simplement les enregistrer tous dans votre fichier manifest. Pour ce faire, structurez simplement `manifest.js` comme ceci, ce à quoi ressemble le fichier manifest de notre extension :

```
{    "name": "Exemple d'extension Chrome",    ...
```

```
    "background": {        "scripts": [            "js/es6-promise.auto.min.js",            "js/defaults.js",            "js/speech.js",            "js/document.js",            "js/events.js",            "js/stt.js",            "js/listen.js"        ],        "persistent": false    }}
```

Maintenant, vous aurez besoin d'un fichier non seulement pour la fonction de votre extension, mais aussi pour l'interface utilisateur. Pour ce faire, créez un fichier appelé `popup.html`. La popup est une petite fenêtre qui apparaît une fois que l'icône de votre extension est cliquée. Par exemple, voici la popup pour l'extension Cookie Manager de Firefox.

![Image](https://cdn-media-1.freecodecamp.org/images/ZG-VIUmxMhxR8qzkGKdB7NOwtl598vzxmG7n)

Le fichier `popup.html` peut être assez simple. Ci-dessous, un code pour créer une popup avec un seul bouton. Il est aussi simple que d'ajouter des balises de bouton d'ouverture et de fermeture dans le corps du document et quelques règles de style.

```
<!DOCTYPE html>  <html>    <head>      <style>        button {          height: 30px;          width: 30px;          outline: none;        }      </style>    </head>;    <body>      <button></button>    </body>  </html>
```

Bien sûr, le code `popup.html` de notre extension a beaucoup plus de composants que cela. N'hésitez pas à ajouter plus de boutons, de feuilles de style et tout ce que vous jugez utile pour votre idée d'extension.

Il est temps de configurer le code de la popup et l'icône. Pour l'icône, cependant, vous devrez ajouter du code à deux endroits, "default_icon" et "icons". La propriété "default_icon" est utilisée pour les icônes de la barre d'outils, et "icons" est utilisée pour les images affichées sur la page de gestion des extensions.

Retournez à `manifest.json` et ajoutez les lignes de code suivantes, en remplaçant les chemins d'image pour l'icône par défaut par vos propres images. Vous pouvez également mettre les mêmes images pour "default_icon" et "icons". Et vous n'avez pas besoin de mettre des images des mêmes dimensions que celles spécifiées ci-dessous. Par exemple, si vous n'avez que des images de 16 x 16 et 48 x 48, n'hésitez pas à supprimer les deux autres lignes qui spécifient 32 et 128 pixels.

```
{   "name": "Exemple d'extension Chrome",    ...
```

```
    "page_action": {        "default_popup": "popup.html",        "default_icon": {            "16": "images/img16.png",            "32": "images/img32.png",            "48": "images/img48.png",            "128": "images/img128.png"        }    },    "icons": {        "16": "images/img16.png",        "32": "images/img32.png",        "48": "images/img48.png",        "128": "images/img128.png"    }}
```

Voici donc les fichiers essentiels pour construire une extension Chrome :

* un fichier manifest,
* des scripts d'arrière-plan, et
* un fichier popup

D'autres fichiers que vous pourriez vouloir configurer sont :

* `options.html` et
* `options.js`

`options.js` offrira à vos utilisateurs une plus grande variété d'options lorsqu'il s'agit d'utiliser votre extension. Il prendra en charge l'apparence de votre page d'options (elle est très similaire à `popup.html`), tandis que `options.js` gérera la fonctionnalité.

Ces fichiers sont optionnels, mais si vous décidez de les ajouter, n'oubliez pas de configurer `options.html` dans le manifest et de lier votre fichier `options.js` en ajoutant `<script src="options.js"></script>` juste avant votre balise HTML de fin.

```
{    "name": "Exemple d'extension Chrome",    ...    "options_page": "options.html"}
```

Pour voir votre extension en action, enregistrez tous vos fichiers et cliquez sur "Recharger" lorsque vous êtes sur la page de gestion des extensions. Vous devriez voir votre icône dans la barre d'outils. Pour afficher votre page d'options, vous pouvez également cliquer sur "Détails" sous votre extension et faire défiler jusqu'à l'endroit où il est écrit "Options de l'extension".

#### Publier votre projet sur le Web Store

Vous avez donc développé et testé votre extension. Maintenant, vous devez la distribuer !

Pour commencer à télécharger votre projet, convertissez-le d'abord en fichier .zip. Le fichier doit contenir, au minimum, le fichier `manifest.json`. Ensuite, assurez-vous d'avoir un compte développeur en visitant le [Tableau de bord des développeurs du Chrome Web Store](https://chrome.google.com/webstore/developer/dashboard).

Cliquez sur le bouton "Ajouter un nouvel élément" et cela devrait vous permettre de télécharger votre fichier `.zip`. À moins que vous ne souhaitiez enregistrer des paiements pour votre application, vous pouvez ignorer l'étape concernant la configuration d'un système de paiement. Vous devrez cependant payer des frais de développeur de 5 $ une seule fois lorsque vous mettrez votre projet sur le web store.

N'oubliez pas non plus d'inclure une description détaillée et des images de votre extension afin que les utilisateurs potentiels sachent exactement ce que fait votre projet !

Une fois tout cela terminé, vous recevrez un identifiant d'application et un jeton OAuth. L'identifiant d'application est utilisé pour faire des requêtes aux API Google, tandis que le jeton OAuth est utilisé pour effectuer des paiements sur le Web Store.

Félicitations, vous avez maintenant publié votre extension ! 🎉

Si vous avez aimé cet article, consultez [cet article suivant](https://medium.com/@tanejapalash/handling-mic-input-permissions-and-speech-recognition-in-chrome-extensions-ff7e3ca84cb0). Nous approfondirons la configuration des fonctionnalités audio dans votre extension Chrome, tout comme nous l'avons fait pour TalkToMe.