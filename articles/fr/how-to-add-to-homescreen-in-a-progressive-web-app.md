---
title: Comment ajouter à l'écran d'accueil dans une Progressive Web App
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-to-homescreen-in-a-progressive-web-app
coverImage: https://www.freecodecamp.org/news/content/images/2020/02/daniel-korpai-beHREvNpn6k-unsplash.jpg
tags:
- name: progressive web app
  slug: progressive-web-app
- name: PWA
  slug: pwa
- name: toothbrush
  slug: toothbrush
seo_title: Comment ajouter à l'écran d'accueil dans une Progressive Web App
seo_desc: 'Add To Homescreen

  Here the web app install banner is focused on web app, with the feature of add to
  homescreen.

  Browser Support for Add To Homescreen

  Add to Homescreen functionality is currently supported by:


  Chrome

  iOS Safari


  You can see the lates...'
---

## **Ajouter à l'écran d'accueil**

Ici, la bannière d'installation de l'application web se concentre sur l'application web, avec la fonctionnalité d'ajout à l'écran d'accueil.

### **Support des navigateurs pour Ajouter à l'écran d'accueil**

La fonctionnalité Ajouter à l'écran d'accueil est actuellement supportée par :

* Chrome
* iOS Safari

Vous pouvez voir le dernier statut du support des navigateurs pour cette fonctionnalité [ici](https://caniuse.com/#feat=web-app-manifest).

### **Sur Android**

Sur Android, la bannière « ajouter à l'écran d'accueil » apparaît automatiquement si vous répondez à certaines exigences. Voici à quoi cela devrait ressembler sur Android :

Invite d'ajout à l'écran d'accueil lors du lancement de l'application

![prompt](https://user-images.githubusercontent.com/15358452/31663686-860779f0-b375-11e7-85c9-1387d9b3bfcf.png)

![launch](https://user-images.githubusercontent.com/15358452/31663690-89b0d998-b375-11e7-8a84-f3e33be9a2c2.png)

### Exigences

Inclure un fichier `manifest.json` avec les propriétés suivantes :

* `short_name`
* `name`
* icône `png` de taille `192x192`
* `start_url`
* inclure un service worker qui est à la fois enregistré et activé
* le site web servi via HTTPS (vous pouvez toujours essayer cela avec localhost sans HTTPS)
* le site web répond aux heuristiques d'engagement définies par Chrome

#### **manifest.json**

```json
{
  "name": "FreeCodeCamp",
  "short_name": "FreeCodeCamp",
  "theme_color": "#00FF00",
  "background_color": "#00FF00",
  "display": "standalone",
  "scope": "/",
  "start_url": "/",
  "icons": [
    {
      "src": "assets/images/icons/icon-72x72.png",
      "sizes": "72x72",
      "type": "image/png"
    },
    {
      "src": "assets/images/icons/icon-96x96.png",
      "sizes": "96x96",
      "type": "image/png"
    },
    {
      "src": "assets/images/icons/icon-128x128.png",
      "sizes": "128x128",
      "type": "image/png"
    },
    {
      "src": "assets/images/icons/icon-144x144.png",
      "sizes": "144x144",
      "type": "image/png"
    },
    {
      "src": "assets/images/icons/icon-152x152.png",
      "sizes": "152x152",
      "type": "image/png"
    },
    {
      "src": "assets/images/icons/icon-192x192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "assets/images/icons/icon-384x384.png",
      "sizes": "384x384",
      "type": "image/png"
    },
    {
      "src": "assets/images/icons/icon-512x512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ],
  "splash_pages": null
}
```

* `name` est le nom de l'application web. (Il sera affiché dans l'écran de lancement)
* `short_name` est le nom court de l'application web. (Il sera affiché sous l'icône du menu téléphone)
* `theme_color` est la couleur du haut du navigateur.
* `background_color` est la couleur de fond de l'écran de lancement.
* `display` est la manière dont l'application web doit s'afficher une fois lancée sur le téléphone.
* `start_url` définit l'URL de démarrage du site web.
* `icons` est un tableau qui stocke tous les emplacements, tailles et types d'images.

## Sur d'autres appareils

Bien que cette méthode ne fonctionne pas sur iOS et Windows, il existe une méthode de repli.

### iOS

Sur iOS, le bouton « ajouter à l'écran d'accueil » doit être ajouté manuellement. Ajoutez les balises meta suivantes à la section head de votre HTML pour supporter l'icône de l'application web iOS.

```html
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="green">
<meta name="apple-mobile-web-app-title" content="FreeCodeCamp">
<link rel="apple-touch-icon" href="/assets/images/icons/icon-72x72.png" sizes="72x72">
<link rel="apple-touch-icon" href="/assets/images/icons/icon-96x96.png" sizes="96x96">
<link rel="apple-touch-icon" href="/assets/images/icons/icon-128x128.png" sizes="128x128">
<link rel="apple-touch-icon" href="/assets/images/icons/icon-144x144.png" sizes="144x144">
<link rel="apple-touch-icon" href="/assets/images/icons/icon-152x152.png" sizes="152x152">
<link rel="apple-touch-icon" href="/assets/images/icons/icon-192x192.png" sizes="192x192">
<link rel="apple-touch-icon" href="/assets/images/icons/icon-384x384.png" sizes="384x384">
<link rel="apple-touch-icon" href="/assets/images/icons/icon-512x512.png" sizes="512x512">
```

### Windows

Sur les téléphones Windows, ajoutez les balises meta suivantes à la section head de votre HTML :

```html
<meta name="msapplication-TileImage" content="/assets/images/icons/icon-144x144.png">
<meta name="msapplication-TileColor" content="green">
```