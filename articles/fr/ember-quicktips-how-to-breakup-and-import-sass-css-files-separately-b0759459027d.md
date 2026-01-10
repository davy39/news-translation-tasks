---
title: 'Ember QuickTips : Comment diviser et importer des fichiers SASS/CSS séparément'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-11T17:50:43.000Z'
originalURL: https://freecodecamp.org/news/ember-quicktips-how-to-breakup-and-import-sass-css-files-separately-b0759459027d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ZVmLA6aPZFWbG6UDK5nEfw.png
tags:
- name: CSS
  slug: css
- name: ember
  slug: ember
- name: JavaScript
  slug: javascript
- name: Sass
  slug: sass
- name: technology
  slug: technology
seo_title: 'Ember QuickTips : Comment diviser et importer des fichiers SASS/CSS séparément'
seo_desc: 'By Michael Xavier

  There are times when it’s desirable to break up your stylesheets into multiple files
  and import them into your project separately. This came up in a side project I started
  recently, and I thought y’all might benefit from what I came...'
---

Par Michael Xavier

Il arrive que l'on souhaite **diviser ses feuilles de style en plusieurs fichiers et les importer séparément dans son projet**. Cela s'est présenté dans un projet parallèle que j'ai commencé récemment, et j'ai pensé que vous pourriez bénéficier de la solution que j'ai trouvée. C'est une méthode rapide et facile, alors commençons ?

Lorsque vous commencez une nouvelle application EmberJS, vous remarquerez que le fichier `index.html` importe la feuille de style principale dans l'application comme suit :

```html
<head>
 ...
 <link
  integrity=""
  rel="stylesheet"
  href="{{rootURL}}assets/test-app.css"
 >
 ...
</head>
```

`test-app.css` est compilé directement à partir de votre projet. Lorsque nous écrivons nos styles personnalisés dans `app/styles/app.css`, ils sont placés dans ce fichier.

Maintenant, que faire si nous ne voulons pas importer tous nos styles dans l'application en tant que feuille de style unique ? **Comment pouvons-nous diviser nos styles et importer plusieurs feuilles de style dans l'application ?** Quelque chose comme ceci :

```html
<head>
 ...
 <link
  integrity=""
  rel="stylesheet"
  href="{{rootURL}}assets/test-app.css"
 >
 <link
  integrity=""
  rel="stylesheet"
  href="{{rootURL}}assets/second-stylesheet.css"
 >
...
</head>
```

Cela peut être plus facile que vous ne le pensez ?

### Étape 1 : Écrire des styles en SCSS/SASS et les compiler en CSS

Tout d'abord, installez un préprocesseur SASS pour compiler les feuilles de style SCSS/SASS en feuilles de style CSS. Pour cet exemple, j'utiliserai `ember-cli-sass` :

```
ember install ember-cli-sass
```

Renommez maintenant `app/styles/app.css` en `app/styles/app.scss`. Le préprocesseur se chargera de traiter et de compiler automatiquement votre feuille de style.

Si vous exécutez l'application, la page de bienvenue d'Ember devrait s'afficher comme d'habitude :

![Image](https://cdn-media-1.freecodecamp.org/images/aYuzVPXdJ4BtKQenSZFHhS-C-GDrL2LS7Ryf)
_Rien n'a changé. C'est bien._

Commentez `{{welcome-page}}` dans `app/templates/application.hbs` avant de continuer. Nous avons maintenant un DOM vide avec lequel travailler.

### Étape 2 : Créer une nouvelle feuille de style

Créons une nouvelle feuille de style appelée `app/styles/second-stylesheet.scss` et ajoutons les styles suivants :

```css
body {
 width: 100vw;
 height: 100vh;
 background-color: red;
}
```

Un fond rouge criard serait très visible, mais lorsque vous exécutez le serveur, vous ne voyez qu'un océan de blanc. Pourquoi ?

Si votre instinct était de l'importer dans le projet comme spécifié ci-dessus, vous auriez raison :

```html
<head>
 ...
 <link
  integrity=""
  rel="stylesheet"
  href="{{rootURL}}assets/second-stylesheet.css"
 >
...
</head>
```

Pourtant, il ne s'affiche toujours pas. Pourquoi ? ? C'est parce que le pipeline de construction n'a pas encore été configuré pour construire ce fichier dans le bon dossier.

### Étape 3 : Configurer Ember-CLI-Build

La dernière étape consiste à indiquer à l'application Ember que vous avez un fichier `css` à inclure dans son pipeline de construction.

Dans `ember-cli-build.js`, ajoutez ce qui suit :

```js
...
module.exports = function(defaults) {
  let app = new EmberApp(defaults, {
    // Ajoutez des options ici
    outputPaths: {
      app: {
        css: {
          'second-stylesheet': '/assets/second-stylesheet.css'
        }
      }
    }
    
  });
  ...
};
```

**C'est tout !** ? Cela indique à Ember où sortir votre nouvelle feuille de style afin qu'elle puisse être correctement accessible dans votre `index.html` ?

![Image](https://cdn-media-1.freecodecamp.org/images/EY9F7DHJAzzfJqcwOS9Ft-TyL78cFd5nYfuE)
_Un océan de rouge. N'oubliez pas de redémarrer le serveur lorsque vous apportez des modifications de configuration, sinon vous ne verrez peut-être pas les changements._