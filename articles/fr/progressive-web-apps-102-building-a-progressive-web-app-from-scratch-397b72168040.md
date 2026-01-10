---
title: 'Applications Web Progressives 102 : Construire une Application Web Progressive
  à partir de zéro'
subtitle: ''
author: Shruti Kapoor
co_authors: []
series: null
date: '2018-09-13T00:19:37.000Z'
originalURL: https://freecodecamp.org/news/progressive-web-apps-102-building-a-progressive-web-app-from-scratch-397b72168040
coverImage: https://cdn-media-1.freecodecamp.org/images/0*q57QiIkbThi9Mqvl
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: progressive web app
  slug: progressive-web-app
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: 'Applications Web Progressives 102 : Construire une Application Web Progressive
  à partir de zéro'
seo_desc: 'We learnt about what is a Progressive Web App (PWA) in part 1. In this
  part, we are going to build a progressive web app using no frameworks but just DOM
  manipulation.

  Let’s do a quick recap of what we have learnt so far. For an app to be progressive...'
---

Nous avons appris [ce qu'est une Application Web Progressive (PWA)](https://medium.freecodecamp.org/progressive-web-apps-101-the-what-why-and-how-4aa5e9065ac2) dans la partie 1. Dans cette partie, nous allons construire une application web progressive sans utiliser de frameworks, mais uniquement avec la manipulation du DOM.

Faisons un rapide récapitulatif de ce que nous avons appris jusqu'à présent. Pour qu'une application soit progressive, elle doit répondre aux exigences suivantes :

1. un fichier manifest — `manifest.json`
2. un service worker avec au moins un événement fetch — `serviceworker.js`
3. une icône — `icon.jpeg`
4. servie via HTTPS — `https://www.monsitegenial.com`

Dans ce tutoriel, je vais parler des exigences 1 et 2 — créer un fichier manifest et enregistrer un service worker.

### Objectif

Pour cet exemple, nous allons créer une application web progressive simple. La complexité est intentionnellement gardée simple afin que nous puissions nous concentrer sur les concepts d'une application web progressive. Vous devriez être en mesure de prendre ces concepts et de les appliquer dans votre propre application Angular, React, Vue ou vanilla JavaScript.

Nous allons créer un moteur de memes. Nous allons récupérer les derniers memes tendance de `giphy.com` et les afficher dans notre application. Un utilisateur devrait pouvoir voir les images même si la connexion est coupée. Ainsi, nous fournissons une expérience hors ligne transparente.

Super ! Alors maintenant, passons aux choses importantes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6EJH5wIYnR3sHy6yI4bm7w.gif)

### Étape 0 : Construire l'application

Commençons par un squelette index.html :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Tous les memes !</title>
    <link rel="stylesheet" href="/styles.css">
</head>
<body>
<header>
    <h1 class="center">Top des memes tendance aujourd'hui</h1>
</header>
<main>
    <div class="container"></div>
</main>
<script src="app.js"></script>

</body>
</html>
```

Comme vous pouvez le voir, il s'agit d'un simple `index.html` qui n'affiche que le texte `Top des memes tendance aujourd'hui`. Rien de sophistiqué.

Ensuite, ajoutons la capacité de récupérer les memes tendance de `giphy.com`. Voici à quoi ressemble la fonction fetch :

```js
async function fetchTrending() {
    const res = await fetch(`https://api.giphy.com/v1/gifs/trending?api_key=${apiKey}&limit=25`);
    const json = await res.json();

    main.innerHTML = json.data.map(createMeme).join('\n');
}
```

### Rendre l'application progressive

#### Étape 1 : Fichier Manifest

Comme vous vous en souvenez peut-être de la partie 1, le fichier manifest est un fichier `json`. Il contient des métadonnées sur l'application comme le nom de l'icône, la couleur de fond, le nom de l'application, etc. Voici un fichier `manifest.json` avec ces paramètres :

```json
{
  "name": "Meme",
  "short_name": "Meme",
  "icons": [{
    "src": "images/icons/icon-128x128.png",
      "sizes": "128x128",
      "type": "image/png"
    }, {
      "src": "images/icons/icon-144x144.png",
      "sizes": "144x144",
      "type": "image/png"
    }, {
      "src": "images/icons/icon-152x152.png",
      "sizes": "152x152",
      "type": "image/png"
    }, {
      "src": "images/icons/icon-192x192.png",
      "sizes": "192x192",
      "type": "image/png"
    }, {
      "src": "images/icons/icon-256x256.png",
      "sizes": "256x256",
      "type": "image/png"
    }],
  "start_url": "/index.html",
  "display": "standalone",
  "background_color": "#3E4EB8",
  "theme_color": "#2F3BA2"
}
```

Vous pouvez également utiliser un outil pour générer ceci. [Voici un outil](https://app-manifest.firebaseapp.com/) que j'ai trouvé utile :

![Image](https://cdn-media-1.freecodecamp.org/images/1*EeVAMTLF9yowvPPJuOHpqw.png)
_Générateur de manifest pour applications web_

L'ajouter à notre application est simple. Ajoutez la ligne suivante à `index.html` :

```html
<link rel="manifest" href="/manifest.json">
```

#### **Étape 2 : Service Worker**

Créons le fichier `serviceworker.js`. Tout d'abord, nous allons enregistrer le service worker lors de l'installation. Ensuite, nous allons mettre en cache certains actifs statiques tels que `styles.css` et `app.js`. Ensuite, nous devons fournir une capacité hors ligne en utilisant `fetch`. Voici à quoi ressemble le `serviceWorker.js` :

```js
const staticAssets = [
    './',
    './styles.css',
    './app.js'
];

self.addEventListener('install', async event => {
    const cache = await caches.open('static-meme');
    cache.addAll(staticAssets);
});

self.addEventListener('fetch', event => {
    const {request} = event;
    const url = new URL(request.url);
    if(url.origin === location.origin) {
        event.respondWith(cacheData(request));
    } else {
        event.respondWith(networkFirst(request));
    }

});

async function cacheData(request) {
    const cachedResponse = await caches.match(request);
    return cachedResponse || fetch(request);
}

async function networkFirst(request) {
    const cache = await caches.open('dynamic-meme');

    try {
        const response = await fetch(request);
        cache.put(request, response.clone());
        return response;
    } catch (error){
        return await cache.match(request);

    }

}
```

Décomposons cela. Un service worker nous aidera à mettre en cache les données et à récupérer les ressources. Si nous avons des données dans notre cache, nous retournons les données du cache ou les récupérons du réseau. Pour votre propre application, réfléchissez aux fonctionnalités que vous devrez fournir pour un accès hors ligne. Ensuite, mettez en cache les ressources en conséquence. Pour mon cas, je veux afficher les images précédemment mises en cache lorsque le réseau est hors ligne.

Nous devrons ajouter ceci à notre index.html. Pour l'ajouter, nous allons enregistrer le service worker en utilisant la bibliothèque navigator du navigateur :

```js
window.addEventListener('load', async e => {
    await fetchTrending();

    if ('serviceWorker' in navigator) {
        try {
            navigator.serviceWorker.register('serviceWorker.js');
            console.log('SW enregistré');

        } catch (error) {
            console.log('SW échoué');

        }
    }
});
```

Vérifions qu'il a bien été enregistré. Cliquez sur l'onglet réseau dans le navigateur et allez dans les paramètres de l'application. Cet onglet est vraiment utile lors du développement d'une application web progressive. Rechargez la page, et vous pourrez voir un service worker dans cet onglet.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ayDNoz8Aw59BlVTfhrSU-w.png)
_Le Service Worker a été enregistré_

Maintenant, rafraîchissons le navigateur. Lors du premier chargement, les données seront mises en cache par le service worker. Essayez de couper la connexion. Nous pourrons toujours voir les images.

Notre application est maintenant disponible même hors ligne ! Si vous avez activé HTTPS et téléchargé une icône, félicitations, vous avez maintenant une Application Web Progressive !

### Prochaines étapes

Si vous êtes intéressé par le développement de votre propre application web progressive, je vous recommande vivement de consulter ce [codelabs](https://codelabs.developers.google.com/codelabs/your-first-pwapp/) de Google Developers.

Avez-vous appris quelque chose de nouveau ? Avez-vous des commentaires ? Connaissez-vous une DevJoke ? [Tweetez-moi @shrutikapoor08](https://twitter.com/shrutikapoor08)

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">// When I wrote this, only God and I understood what I was doing<br>// Now, only God knows<a href="https://twitter.com/hashtag/devjoke?src=hash&amp;ref_src=twsrc%5Etfw">#devjoke</a> <a href="https://twitter.com/hashtag/notajoke?src=hash&amp;ref_src=twsrc%5Etfw">#notajoke</a> <a href="https://twitter.com/hashtag/development?src=hash&amp;ref_src=twsrc%5Etfw">#development</a> <a href="https://twitter.com/hashtag/javascript?src=hash&amp;ref_src=twsrc%5Etfw">#javascript</a> <a href="https://t.co/4V6lMUdhdb">pic.twitter.com/4V6lMUdhdb</a></p>&mdash; Shruti Kapoor (@shrutikapoor08) <a href="https://twitter.com/shrutikapoor08/status/1027666190447955968?ref_src=twsrc%5Etfw">August 9, 2018</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>