---
title: Comment intégrer Tailwind avec Electron – Avec des exemples de code
subtitle: ''
author: Abhijeet Dave
co_authors: []
series: null
date: '2025-08-13T17:22:22.821Z'
originalURL: https://freecodecamp.org/news/integrate-tailwind-with-electron
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1755102784797/0a2d19f0-3539-47c6-a29d-68fab3d430ba.png
tags:
- name: Tailwind CSS
  slug: tailwind-css
- name: Electron
  slug: electron
seo_title: Comment intégrer Tailwind avec Electron – Avec des exemples de code
seo_desc: 'In this article, you’ll learn how to integrate Tailwind CSS with Electron
  to build stylish, responsive desktop applications.

  You’ll set up Tailwind in an Electron project, configure your project, style the
  components, and optimize the development wor...'
---

Dans cet article, vous apprendrez à intégrer Tailwind CSS avec Electron pour créer des applications de bureau élégantes et réactives.

Vous installerez Tailwind dans un projet Electron, configurerez votre projet, styliserez les composants et optimiserez le flux de travail de développement. Ce guide est parfait pour les développeurs qui cherchent à combiner le Framework CSS utility-first de Tailwind avec les capacités multiplateformes d'Electron.

## Table des matières

* [Un aperçu rapide d'Electron](#heading-un-aperçu-rapide-delectron)
    
* [Qu'est-ce que Tailwind CSS ?](#heading-quest-ce-que-tailwind-css)
    
* [Pourquoi Electron et Tailwind fonctionnent si bien ensemble](#heading-pourquoi-electron-et-tailwind-fonctionnent-si-bien-ensemble)
    
* [Que allons-nous construire ?](#heading-que-allons-nous-construire)
    
* [Prérequis](#heading-prérequis)
    
* [Comment initialiser un projet Electron](#heading-comment-initialiser-un-projet-electron)
    
* [Comment intégrer Tailwind CSS avec Electron ?](#heading-comment-intégrer-tailwind-css-avec-electron)
    
* [Comment utiliser une bibliothèque de composants Tailwind – un exemple pratique](#heading-comment-utiliser-une-bibliothèque-de-composants-tailwind-un-exemple-pratique)
    
* [Testons les composants JS de FlyonUI](#heading-testons-les-composants-js-de-flyonui)
    
* [Conclusion](#heading-conclusion)
    

## Un aperçu rapide d'Electron

[**Electron**](https://www.electronjs.org/) est un Framework qui permet aux développeurs de créer des applications de bureau pour Windows, macOS et Linux en utilisant des technologies web familières telles que HTML, CSS et JavaScript, ainsi que Node.js pour les fonctionnalités backend.

Il est open-source, sous licence MIT et totalement gratuit à utiliser – que vous construisiez des projets personnels ou des applications commerciales.

Dans ce guide, nous verrons pourquoi tant de développeurs et d'entreprises choisissent Electron pour créer des applications de bureau modernes.

## **Qu'est-ce que Tailwind CSS ?**

[**Tailwind CSS**](https://tailwindcss.com/) est essentiellement un Framework utility-first pour styliser les interfaces web. Contrairement aux Frameworks qui fournissent des composants UI complets et pré-conçus, Tailwind propose un ensemble complet de classes utilitaires à usage unique. Vous appliquez ces classes directement à vos éléments HTML, ce qui signifie que vous pouvez rapidement construire des mises en page et des designs personnalisés sans avoir à plonger dans des fichiers CSS séparés.

Le grand avantage ? La précision et la flexibilité – vous pouvez assembler des interfaces uniques et réactives en combinant ces classes comme bon vous semble, tout en gardant votre balisage léger et maintenable.

## **Pourquoi Electron et Tailwind fonctionnent si bien ensemble**

Electron utilise HTML, CSS et JavaScript pour construire des applications de bureau. Essentiellement, il exécute une application web dans un shell de bureau. Cela facilite l'intégration d'outils frontend modernes comme Tailwind CSS.

L'approche utility-first de Tailwind vous permet de styliser les interfaces directement dans votre HTML, ce qui peut accélérer le développement de l'UI. Au lieu d'écrire des styles personnalisés ou de gérer des fichiers CSS volumineux, vous appliquez des classes prédéfinies directement aux éléments. Cela s'aligne bien avec la structure d'Electron, où la mise en page et les styles sont étroitement liés dans le même environnement HTML.

Tailwind fournit également des valeurs par défaut judicieuses et un système de conception cohérent dès le départ. Cela vous aide à prototyper et à créer plus rapidement des applications de bureau visuellement cohérentes. Bien qu'une certaine familiarité avec le CSS soit toujours utile, l'approche de Tailwind peut réduire la charge de travail liée à la configuration et à la gestion des styles, en particulier dans les projets de petite taille ou peu axés sur le design.

Ensemble, Electron et Tailwind offrent une voie simple pour construire des applications de bureau.

## Que allons-nous construire ?

Dans ce tutoriel, nous allons créer une application de bureau Electron de base stylisée avec Tailwind CSS et améliorée avec les composants FlyonUI. Vous n'avez besoin d'aucune expérience préalable avec Electron ou Tailwind.

À la fin de ce guide, vous aurez :

* Une fenêtre de bureau fonctionnelle (Electron)
    
* Une UI stylisée avec Tailwind CSS
    
* Un composant bouton réutilisable
    
* Une boîte de dialogue modale entièrement fonctionnelle propulsée par FlyonUI
    

Cela constituera une base solide pour construire des applications plus complexes à l'avenir.

## **Prérequis**

Avant de commencer, assurez-vous d'avoir les éléments suivants :

* **Connaissances de base en HTML, CSS et JavaScript**. Vous n'avez pas besoin d'être un expert, mais comprendre comment structurer le HTML et utiliser le JavaScript de base vous aidera à suivre.
    
* **Familiarité avec Node.js et npm**. Nous utiliserons npm (Node Package Manager) pour installer les dépendances et exécuter les commandes de build.
    
* **Node.js installé sur votre machine**. Vous pouvez le télécharger sur [nodejs.org](http://nodejs.org).
    
* **Un éditeur de code**. Je recommande [Visual Studio Code.](https://code.visualstudio.com/)
    
* **Accès au Terminal / Ligne de commande**. Vous devrez exécuter des commandes dans le terminal pour configurer les choses.
    

## **How to Initialize an Electron Project**

Configurons une application Electron de base à partir de zéro. Cela lancera une simple fenêtre de bureau qui charge un fichier HTML, servant de fondation pour votre UI.

### 1\. **Créez votre dossier de projet**

Tout d'abord, ouvrez votre terminal et créez un nouveau dossier de projet :

```bash
mkdir my-electron-app
cd my-electron-app
```

Cela crée un nouveau dossier appelé `my-electron-app` et change de répertoire pour y accéder. Ce dossier sera votre espace de travail de projet.

### 2\. **Installez Electron**

Ensuite, installez Electron en tant que dépendance de développement :

```bash
npm install electron --save-dev
```

Cela ajoutera Electron au dossier `node_modules` de votre projet et mettra à jour votre fichier `package.json`.

Cette commande installe Electron en tant que dépendance de développement. Electron vous permet de construire des applications de bureau sur différentes plateformes en utilisant des technologies web.

### 3\. **Configurez** `package.json`

Mettez à jour votre `package.json` pour pointer vers un fichier nommé `main.js`, et ajoutez un script pour démarrer facilement l'application.

**Modifiez votre** `package.json` comme ceci :

```json
"main": "main.js",
"scripts": {
  "start": "electron ."
}
```

* `"main"` définit le point d'entrée de votre application Electron (le processus principal).
    
* `"start"` est un raccourci pour lancer l'application en utilisant `npm start`.
    

### 4\. **Créez** `main.js`

Créez un fichier nommé `main.js` dans votre dossier racine et ajoutez le code suivant :

```javascript
const { app, BrowserWindow } = require("electron/main");

const createWindow = () => {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
  });

  win.loadFile("index.html");
};

app.whenReady().then(() => {
  createWindow();

  app.on("activate", () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
    }
  });
});

app.on("window-all-closed", () => {
  if (process.platform !== "darwin") {
    app.quit();
  }
});
```

C'est votre **processus principal**. Il crée et gère la fenêtre de l'application tout en chargeant votre fichier HTML.

### 5\. **Créez** `index.html` **(Processus Renderer)**

```xml
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'" />
    <title>Hello from Electron renderer!</title>
  </head>
  <body>
    <h1>Hello from Electron renderer!</h1>
    <p></p>
    <p id="info"></p>
    <script src="./renderer.js"></script>
  </body>
</html>
```

C'est le **frontend (renderer)** de votre application Electron. Vous pouvez utiliser du HTML, CSS et JavaScript standard ici, comme dans un navigateur.

> Facultatif : Créez un fichier renderer.js si vous souhaitez ajouter de l'interactivité JavaScript.

### 6\. **Exécutez l'application Electron**

Maintenant, exécutez votre application Electron avec la commande suivante :

```bash
npm start
```

Cette commande lance l'application en utilisant le script que vous avez configuré dans `package.json`. Une fenêtre de bureau devrait s'ouvrir, affichant votre contenu HTML.

![hello form electron renderer](https://cdn.hashnode.com/res/hashnode/image/upload/v1754292319523/58168908-40ed-4aca-920f-fbab7435b580.webp align="center")

## **Comment intégrer Tailwind CSS avec Electron ?**

Pour ce guide, nous utiliserons l'approche [Tailwind CLI](https://tailwindcss.com/docs/installation/tailwind-cli).

Le CLI Tailwind est un outil en ligne de commande qui vous permet de générer et de compiler les classes utilitaires Tailwind directement dans un fichier CSS. Vous n'avez pas besoin d'outils de build complexes comme Webpack ou PostCSS. Cela le rend parfait pour des projets simples comme les applications Electron, où vous voulez une configuration minimale et un stylisage rapide. Le CLI dispose également d'un mode `--watch` qui recompile automatiquement le CSS lorsque les fichiers changent.

### 1\. **Installez Tailwind CSS**

Tout d'abord, installez Tailwind CSS. Assurez-vous que Node.js est également installé, puis exécutez :

```bash
npm install tailwindcss @tailwindcss/cli
```

Cette commande installe Tailwind et son outil CLI en tant que dépendance de développement dans votre projet.

### 2\. **Configurez Tailwind CSS**

Créez un fichier `input.css` avec le contenu suivant pour configurer Tailwind :

```css
@import "tailwindcss";
```

Cette ligne indique à Tailwind de générer toutes ses classes utilitaires dans un fichier de sortie, que nous compilerons ensuite.

### 3\. **Ajoutez un script de Build**

Ensuite, mettez à jour votre `package.json` pour inclure un script de build :

```json
"scripts": {  
 "watch:css":"npx @tailwindcss/cli -i ./input.css -o ./output.css --watch",
}
```

Cette commande surveille votre fichier `input.css` et génère en continu un fichier CSS compilé (`output.css`) chaque fois qu'elle détecte des changements. Vous inclurez ce fichier dans votre HTML.

### 4\. **Liez** `output.css` **dans** `index.html`

Ouvrez votre fichier `index.html` et ajoutez ceci à l'intérieur de la balise `<head>` :

```html
<link href="./output.css" rel="stylesheet">
```

Ensuite, compilez Tailwind CSS avec cette commande :

```bash
npm run watch:css
```

Cette étape inclut les styles Tailwind compilés dans l'UI de votre application Electron.

### 5\. **Compilez Tailwind CSS**

Exécutez ce script pour commencer à surveiller les changements et générer votre CSS :

```bash
npm run watch:css
```

Gardez ce processus en cours d'exécution dans une fenêtre de terminal. Il met à jour `output.css` en direct pendant que vous travaillez.

### 6\. **Mettez à jour l'UI avec les classes Tailwind**

Remplacez le contenu de votre `<body>` par cet exemple de mise en page :

```xml
<body class="flex items-center justify-center h-screen bg-gray-100">
  <button type="button"
    class="py-3 px-4 inline-flex items-center gap-x-2 text-sm font-medium rounded-lg border border-transparent bg-purple-600 text-white hover:bg-purple-700 focus:outline-hidden cursor-pointer focus:bg-purple-700 disabled:opacity-50 disabled:pointer-events-none">
    Hello Tailwindcss
  </button>
</body>
```

### 7\. **Exécutez l'application Electron**

Lancez le serveur Electron avec cette commande :

```bash
npm start
```

Votre fenêtre Electron devrait maintenant s'ouvrir avec un bouton bien stylisé au centre, grâce à Tailwind CSS.

![run electron server](https://cdn.hashnode.com/res/hashnode/image/upload/v1754374369750/f79a6c6d-bc59-4a2b-a6eb-f3b63f8bccc4.png align="center")

## Comment utiliser une bibliothèque de composants Tailwind – un exemple pratique

Nous allons utiliser [FlyonUI](https://flyonui.com/), une bibliothèque de composants Tailwind open source. Elle comprend un mélange de classes utilitaires en plus de plugins JavaScript. FlyonUI s'inspire de daisyUI mais aussi de Preline, et combine flexibilité et simplicité.

### 1\. **Installez FlyonUI**

Vous pouvez installer FlyonUI avec la commande ci-dessous :

```bash
npm install -D flyonui@latest
```

Cela installe FlyonUI dans votre projet en tant que dépendance de développement, rendant ses fonctionnalités CSS et JS disponibles pour l'intégration.

### 2\. Ajoutez FlyonUI comme plugin dans le `input.css` :

```css
@import "tailwindcss";
@plugin "flyonui";
@import "./node_modules/flyonui/variants.css"; /* Nécessaire pour les composants JS */
@source "./node_modules/flyonui/dist/index.js"; /* Nécessaire pour les composants JS */
```

* `@plugin "flyonui"` injecte les classes sémantiques de FlyonUI dans votre build.
    
* Le `@import` inclut les variantes personnalisées créées pour les composants JS.
    
* La ligne `@source` est requise pour que les classes utilisées dans le JS soient générées.
    

### 3\. **Incluez le JavaScript de FlyonUI pour l'interactivité**

Juste avant de fermer la balise `</body>` dans votre HTML, incluez :

```html
<script src="../node_modules/flyonui/flyonui.js"></script>
```

Ce script active les comportements interactifs pour les composants FlyonUI, tels que les overlays, les modales et les listes déroulantes.

### 4\. **Utilisez un composant FlyonUI**

Par exemple, mettez à jour votre UI avec :

```xml
<body class="flex items-center justify-center h-screen bg-gray-100">
  <button type="button" class="btn btn-primary">
    Hello FlyonUI
  </button>
</body>

```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1754374843709/41f9d3e3-d0be-4a32-a569-ce0618bea0e9.png align="center")

* Les classes `.btn` et `.btn-primary` proviennent de FlyonUI — vous offrant des composants stylisés et sémantiques sans avoir à créer de CSS personnalisé.
    

### **Pourquoi c'est important**

* **Code plus propre** : Les classes sémantiques de FlyonUI rendent vos templates plus lisibles et maintenables par rapport aux classes utilitaires verbeuses.
    
* **Interactif sans surcharge** : Ajoutez facilement des fonctionnalités dynamiques comme des modales ou des accordéons grâce aux plugins JS de FlyonUI.
    
* **Stylisage sans effort** : FlyonUI s'appuie sur l'approche utilitaire de Tailwind, vous pouvez donc personnaliser les composants instantanément.
    

## Testons les composants JS de FlyonUI

Pour montrer comment FlyonUI fonctionne, nous allons tester l'un de ses composants UI alimentés par JavaScript, la **Modale**. Les modales sont des éléments d'interface courants qui attirent l'attention de l'utilisateur pour des alertes ou des confirmations.

### Pourquoi tester la Modale ?

Tester la modale vous aide à :

* Vérifier que les composants JavaScript de FlyonUI se chargent et fonctionnent correctement dans votre configuration Electron et Tailwind.
    
* Voir à quel point il est simple d'ajouter des fonctionnalités interactives en utilisant les classes intégrées et les attributs de données de FlyonUI.
    
* Comprendre comment la modale réagit aux différentes tailles d'écran.

### Comment tester la Modale

Copiez le code d'exemple suivant dans votre fichier `index.html`. Ce bouton ouvrira une boîte de dialogue modale avec un contenu fictif :

Nous utiliserons cet [**exemple de Modale**](https://flyonui.com/docs/overlays/modal/) pour le test. Copiez le code suivant dans votre `index.html` :

```html
<button type="button" class="btn btn-primary" aria-haspopup="dialog" aria-expanded="false" aria-controls="basic-modal" data-overlay="#basic-modal">Open modal</button>

<div id="basic-modal" class="overlay modal overlay-open:opacity-100 hidden overlay-open:duration-300" role="dialog" tabindex="-1">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">Titre du dialogue</h3>
        <button type="button" class="btn btn-text btn-circle btn-sm absolute end-3 top-3" aria-label="Close" data-overlay="#basic-modal">
          <span class="icon-[tabler--x] size-4"></span>
        </button>
      </div>
      <div class="modal-body">
        Ceci est un exemple de contenu pour montrer le comportement de défilement des modales. Au lieu de répéter le texte,
        nous utilisons un style en ligne pour définir une hauteur minimale, prolongeant ainsi la longueur de la modale
        et démontrant le défilement. Lorsque le contenu devient plus long que la hauteur de la fenêtre, le défilement
        déplacera la modale selon les besoins.
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-soft btn-secondary" data-overlay="#basic-modal">Fermer</button>
        <button type="button" class="btn btn-primary">Enregistrer</button>
      </div>
    </div>
  </div>
</div>
```

Après avoir mis à jour le fichier, redémarrez votre application Electron :

```bash
npm start
```

Voici le résultat :

![final result](https://cdn.hashnode.com/res/hashnode/image/upload/v1754374899394/4f153f2b-ca41-495f-b27e-18a2424a1952.png align="center")

## **Conclusion**

Vous pouvez utiliser Tailwind CSS et Electron pour créer des applications de bureau esthétiques et performantes sur différents appareils. Cela s'ajoute aux nombreuses fonctions d'Electron et au système de stylisage efficace de Tailwind, vous permettant de rester productif et d'utiliser des méthodes de conception propres.

Le code complet et plus de détails sont disponibles dans le dépôt ici : [ts-electron-tailwindcss](https://github.com/themeselection/ts-electron-tailwind).

J'ai écrit ce tutoriel avec l'aide de [Pruthvi Prajapati](https://github.com/PruthviPraj00), un développeur Tailwind CSS expérimenté.