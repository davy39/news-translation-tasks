---
title: Comment créer facilement des applications de bureau avec HTML, CSS et JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-04T21:53:22.000Z'
originalURL: https://freecodecamp.org/news/how-to-easily-build-desktop-apps-with-html-css-and-javascript-d3e3f03f95a5
coverImage: https://cdn-media-1.freecodecamp.org/images/0*mwIqsFZSbnweFQuv
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment créer facilement des applications de bureau avec HTML, CSS et JavaScript
seo_desc: 'By Aditya Sridhar

  Can HTML, CSS and Javascript really be used to build Desktop Applications?

  The answer is yes.

  In this Article we will be focussing mainly on how Electron can be used to create
  desktop applications with Web Technologies like HTML, CS...'
---

Par Aditya Sridhar

Peut-on vraiment utiliser HTML, CSS et JavaScript pour créer des applications de bureau ?

La réponse est oui.

Dans cet article, nous nous concentrerons principalement sur la manière dont Electron peut être utilisé pour créer des applications de bureau avec des technologies web comme HTML, CSS et JavaScript.

### Electron

[Electron](https://electronjs.org/) peut être utilisé pour créer des applications de bureau avec HTML, CSS et JavaScript. De plus, ces applications fonctionnent sur plusieurs plateformes comme Windows, Mac, Linux, etc.

Electron combine Chromium et NodeJS en un seul runtime. Cela nous permet d'exécuter le code HTML, CSS et JavaScript en tant qu'application de bureau.

### Electron Forge

Si Electron est utilisé directement, une configuration manuelle est nécessaire avant de construire votre application. De plus, si vous souhaitez utiliser Angular, React, Vue ou tout autre framework ou bibliothèque, vous devrez configurer manuellement pour cela.

[Electron Forge](https://electronforge.io/) rend les choses ci-dessus beaucoup plus faciles.

Il fournit des applications modèles avec Angular, React, Vue et d'autres frameworks, ce qui évite les configurations manuelles supplémentaires.

Il fournit également un moyen facile de construire et de packager l'application. Il offre également de nombreuses autres fonctionnalités que vous pouvez trouver dans leur [documentation](https://docs.electronforge.io/).

### Prérequis

Assurez-vous d'avoir NodeJS installé. Il peut être installé depuis [ici](https://nodejs.org/en/).

Installez Electron Forge globalement en utilisant la commande suivante :

```bash
npm install -g electron-forge
```

### Commençons avec l'application

Utilisez la commande suivante pour créer votre application :

```bash
electron-forge init simple-desktop-app-electronjs
```

**simple-desktop-app-electronjs** est le nom de l'application.

La commande ci-dessus prendra un certain temps pour s'exécuter.

Une fois qu'elle a fini de s'exécuter, démarrez l'application en utilisant les commandes suivantes :

```bash
cd simple-desktop-app-electronjs
npm start
```

Cela devrait ouvrir une fenêtre comme celle montrée ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/OWyV2vj2yK654YopDS5YsLUAwclQrpA0AX2u)

### Comprendre la structure de dossiers existante et le code

L'application a une structure de dossiers particulière. Ici, je vais mentionner certaines des choses importantes dans cette structure de dossiers.

#### package.json

Il contient des informations sur l'application que vous créez, toutes les dépendances nécessaires pour l'application, et quelques scripts. Certains des scripts sont déjà préconfigurés, et vous pouvez ajouter de nouveaux scripts également.

Le chemin **config.forge** contient toutes les configurations spécifiques à ElectronJS. Par exemple, **make-targets** est utilisé pour spécifier les fichiers de construction cibles pour diverses plateformes comme Windows, Mac ou Linux.

De plus, package.json contient `"main": "src/index.js"` qui indique que src/index.js est le point de départ de l'application.

#### src/index.js

Selon package.json, **index.js** est le script principal. Le processus qui exécute le script principal est connu sous le nom de **main process**. Donc, le main process exécute le script index.js.

Le main process est utilisé pour afficher les éléments de l'interface graphique. Il le fait en créant des pages web.

Chaque page web créée s'exécute dans un processus appelé **renderer process**.

#### Main process et renderer process

Le but du **main process** est de créer des pages web en utilisant une instance `BrowserWindow`.

L'instance `BrowserWindow` utilise un **renderer process** pour exécuter chaque page web.

**Chaque application ne peut avoir qu'un seul main process mais peut avoir plusieurs renderer processes.**

Il est possible de communiquer entre le main process et le renderer process. Cependant, cela ne sera pas couvert dans cet article.

![Image](https://cdn-media-1.freecodecamp.org/images/0nGfmUyxp4rC0GmbnhQk9OuJFm5f5xgO-WGE)
_Architecture d'Electron montrant le main process et le renderer process. Les noms de fichiers peuvent varier._

**abcd.html** est montré comme une deuxième page web dans l'architecture ci-dessus. Mais dans notre code, nous n'aurons pas de deuxième page web.

#### src/index.html

index.js charge le fichier index.html dans une nouvelle instance BrowserWindow.

Ce que cela signifie essentiellement, c'est que index.js crée une nouvelle fenêtre GUI et la charge avec la page web index.html. La page web index.html s'exécute dans son propre renderer process.

#### Code dans index.js expliqué

La plupart du code créé dans index.js a de bons commentaires expliquant ce qu'il fait. Ici, je vais mentionner quelques points clés à noter dans index.js :

```js
mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
  });

  // et charge l'index.html de l'application.
  mainWindow.loadURL(`file://${__dirname}/index.html`);
```

Le fragment de code ci-dessus crée essentiellement une instance **BrowserWindow** et charge **index.html** dans le BrowserWindow.

Vous verrez **app** souvent utilisé dans le code. Par exemple, prenez le fragment de code ci-dessous :

```js
app.on('ready', createWindow);
```

**app** est utilisé pour contrôler le cycle de vie des événements de l'application.

Le fragment de code ci-dessus dit que lorsque l'application est prête, chargez la première fenêtre.

De même, **app** peut être utilisé pour effectuer d'autres actions sur divers événements. Par exemple, il peut être utilisé pour effectuer une action juste avant la fermeture de l'application, etc.

### Créons une application de bureau de conversion de température

Utilisons la même application que nous avons utilisée auparavant et modifions-la légèrement pour créer une application de conversion de température.

Tout d'abord, installons Bootstrap avec la commande suivante :

```bash
npm install bootstrap --save
```

Copiez le code suivant dans src/index.html :

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Convertisseur de température</title>
    <link rel="stylesheet" type="text/css" href="../node_modules/bootstrap/dist/css/bootstrap.min.css">

  </head>
  <body>
    <h1>Convertisseur de température</h1>
    <div class="form-group col-md-3">
      <label for="usr">Celcius :</label>
      <input type="text" class="form-control" id="celcius" onkeyup="celciusToFahrenheit()">
    </div>
    <div class="form-group col-md-3">
      <label for="pwd">Fahrenheit :</label>
      <input type="text" class="form-control" id="fahrenheit" onkeyup="fahrenheitToCelcius()">
    </div>
    <script src='./renderer.js'></script>
  </body>
  </body>
</html>
```

Le code ci-dessus fait ce qui suit :

1. Crée une zone de texte avec l'id **Celcius**. Chaque fois que quelque chose est tapé dans cette zone de texte, la fonction **celciusToFahrenheit()** est appelée.
2. Crée une zone de texte avec l'id **Fahrenheit**. Chaque fois que quelque chose est tapé dans cette zone de texte, la fonction **fahrenheitToCelcius()** est appelée.
3. Chaque fois qu'une nouvelle valeur est tapée dans la zone de texte Celcius, la valeur dans la zone de texte Fahrenheit affiche la même température en Fahrenheit.
4. Chaque fois qu'une nouvelle valeur est tapée dans la zone de texte Fahrenheit, la valeur dans la zone de texte Celcius affiche la même température en Celcius.

Les 2 fonctions qui effectuent la conversion de température sont présentes dans **renderer.js.**

Créez un fichier appelé **renderer.js** à l'intérieur de **src**. Copiez le code suivant dedans :

```js
function celciusToFahrenheit(){
    let celcius = document.getElementById('celcius').value;
    let fahrenheit = (celcius* 9/5) + 32;
    document.getElementById('fahrenheit').value = fahrenheit;

}

function fahrenheitToCelcius(){
    let fahrenheit = document.getElementById('fahrenheit').value;
    let celcius = (fahrenheit - 32) * 5/9
    document.getElementById('celcius').value = celcius;
}
```

La fonction **celciusToFahrenheit()** lit la valeur dans la zone de texte **Celcius**, la convertit en Fahrenheit et écrit la nouvelle température dans la zone de texte **Fahrenheit**.

La fonction **fahrenheitToCelcius()** fait exactement l'inverse.

### Exécution de l'application

Exécutez l'application en utilisant la commande suivante :

```bash
npm start
```

Cela devrait afficher la fenêtre suivante. Essayez-la avec différentes valeurs.

![Image](https://cdn-media-1.freecodecamp.org/images/RNlYkY-7y-zpWDFa6apV81oGv6E8cIsPX19B)

### Packaging de l'application

La commande pour packager l'application est :

```bash
npm run package
```

Cette commande prendra un certain temps pour s'exécuter. Une fois qu'elle a fini, vérifiez le dossier **out** dans le dossier du projet.

J'ai testé cela sur une machine Windows. Cela crée un dossier appelé **simple-desktop-app-electronjs-win32-x64** à l'intérieur du dossier **out**.

Donc, dans le dossier **out/simple-desktop-app-electronjs-win32-x64**, la commande crée un fichier **.exe** pour cette application. En cliquant sur le fichier exe, l'application de bureau démarre automatiquement.

Le nom du dossier **simple-desktop-app-electronjs-win32-x64** peut être décomposé en **appname-platform-architecture** où :

* appname = simple-desktop-app-electronjs
* platform = win32
* architecture = x64

**Lorsque vous exécutez cette commande sans aucun paramètre, par défaut, elle package pour la plateforme que vous utilisez pour le développement.**

Supposons que vous souhaitiez packager pour une plateforme et une architecture différentes. Vous pouvez alors utiliser la syntaxe suivante :

```bash
npm run package -- --platform=<platform> arch=<architecture>
```

Par exemple, pour packager pour Linux, vous pouvez utiliser la commande suivante :

```bash
npm run package -- --platform=linux --arch=x64
```

Cela créera un dossier appelé **simple-desktop-app-electronjs-linux-x64** à l'intérieur du dossier **out**.

### Création d'un fichier make

Pour créer un fichier make ou un installeur pour l'application, utilisez la commande suivante :

```bash
npm run make
```

Cette commande prendra un certain temps pour s'exécuter. Une fois qu'elle a fini, vérifiez le dossier **out** dans le dossier du projet.

Le dossier **out/make** contiendra un installeur Windows pour l'application de bureau.

**Lorsque vous exécutez cette commande sans aucun paramètre, par défaut, elle crée l'installeur pour la plateforme que vous utilisez pour le développement.**

### Code

Le code de cette application de bureau est disponible dans mon dépôt GitHub :

[https://github.com/aditya-sridhar/simple-desktop-app-electronjs](https://github.com/aditya-sridhar/simple-desktop-app-electronjs)

### Félicitations 🎉

Vous savez maintenant comment créer des applications de bureau en utilisant HTML, CSS et JavaScript.

Cet article a couvert des concepts très basiques d'Electron et d'Electron-Forge.

Pour en savoir plus sur eux, vous pouvez consulter leur documentation.

### À propos de l'auteur

J'aime la technologie et je suis les avancées dans ce domaine. J'aime aussi aider les autres avec mes connaissances technologiques.

N'hésitez pas à me contacter sur mon compte LinkedIn [https://www.linkedin.com/in/aditya1811/](https://www.linkedin.com/in/aditya1811/)

Vous pouvez également me suivre sur Twitter [https://twitter.com/adityasridhar18](https://twitter.com/adityasridhar18)

Mon site web : [https://adityasridhar.com/](https://adityasridhar.com/)

Lisez plus de mes articles sur mon blog à l'adresse [adityasridhar.com](https://adityasridhar.com/posts/desktop-apps-with-html-css-javascript).