---
title: Comment créer une PWA à partir de zéro avec HTML, CSS et JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-03T23:27:42.000Z'
originalURL: https://freecodecamp.org/news/build-a-pwa-from-scratch-with-html-css-and-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/Group-1.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: PWA
  slug: pwa
seo_title: Comment créer une PWA à partir de zéro avec HTML, CSS et JavaScript
seo_desc: 'By Ibrahima Ndaw

  Progressive web apps are a way to bring that native app feeling to a traditional
  web app. With PWAs we can enhance our website with mobile app features which increase
  usability and offer a great user experience.

  In this article, we a...'
---

Par Ibrahima Ndaw

Les applications web progressives sont un moyen d'apporter cette sensation d'application native à une application web traditionnelle. Avec les PWA, nous pouvons améliorer notre site web avec des fonctionnalités d'application mobile qui augmentent l'utilisabilité et offrent une excellente expérience utilisateur.

Dans cet article, nous allons créer une PWA à partir de zéro avec HTML, CSS et JavaScript. Voici les sujets que nous allons aborder :

* [Qu'est-ce qu'une Progressive Web App ?](#heading-questce-quune-progressive-web-app)
* [Balisage](#heading-balisage)
* [Stylisation](#heading-stylisation)
* [Afficher les données avec JavaScript](#heading-afficher-les-donnees-avec-javascript)
* [Manifest de l'application web](#heading-manifest-de-lapplication-web)
* [Qu'est-ce qu'un Service Worker ?](#heading-questce-quun-service-worker)
* [Mettre en cache les ressources](#heading-mettre-en-cache-les-ressources)
* [Récupérer les ressources](#heading-recuperer-les-ressources)
* [Enregistrer le Service Worker](#heading-enregistrer-le-service-worker)
* [Réflexions finales](#heading-reflexions-finales)
* [Prochaines étapes](#heading-prochaines-etapes)

Alors, commençons par une question importante : Qu'est-ce qu'une PWA ?

## Qu'est-ce qu'une Progressive Web App ?

Une Progressive Web App est une application web qui offre une expérience similaire à une application aux utilisateurs en utilisant les capacités modernes du web. En fin de compte, ce n'est que votre site web habituel qui s'exécute dans un navigateur avec quelques améliorations. Elle vous donne la capacité :

* De l'installer sur l'écran d'accueil d'un mobile
* D'y accéder lorsqu'on est hors ligne
* D'accéder à la caméra
* De recevoir des notifications push
* De faire de la synchronisation en arrière-plan

Et bien plus encore.

Cependant, pour pouvoir transformer notre application web traditionnelle en PWA, nous devons l'ajuster un peu en ajoutant un fichier manifest d'application web et un service worker.

Ne vous inquiétez pas de ces nouveaux termes – nous les aborderons ci-dessous.

Tout d'abord, nous devons construire notre application web traditionnelle. Alors commençons par le balisage.

## Balisage

Le fichier HTML est relativement simple. Nous enveloppons tout dans la balise `main`.

* Dans `index.html`

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <link rel="stylesheet" href="css/style.css" />
    <title>Dev'Coffee PWA</title>
  </head>
  <body>
    <main>
      <nav>
        <h1>Dev'Coffee</h1>
        <ul>
          <li>Accueil</li>
          <li>À propos</li>
          <li>Blog</li>
        </ul>
      </nav>
      <div class="container"></div>
    </main>
    <script src="js/app.js"></script>
  </body>
</html>

```

Et créer une barre de navigation avec la balise `nav`. Ensuite, la `div` avec la classe `.container` contiendra nos cartes que nous ajouterons plus tard avec JavaScript.

Maintenant que nous avons fait cela, stylisons-le avec CSS.

## Stylisation

Ici, comme d'habitude, nous commençons par importer les polices dont nous avons besoin. Ensuite, nous ferons quelques réinitialisations pour empêcher le comportement par défaut.

* Dans `css/style.css`

```css
@import url("https://fonts.googleapis.com/css?family=Nunito:400,700&display=swap");
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
body {
  background: #fdfdfd;
  font-family: "Nunito", sans-serif;
  font-size: 1rem;
}
main {
  max-width: 900px;
  margin: auto;
  padding: 0.5rem;
  text-align: center;
}
nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
ul {
  list-style: none;
  display: flex;
}

li {
  margin-right: 1rem;
}
h1 {
  color: #e74c3c;
  margin-bottom: 0.5rem;
}

```

Ensuite, nous limitons la largeur maximale de l'élément `main` à `900px` pour qu'il ait une belle apparence sur un grand écran.

Pour la barre de navigation, je veux que le logo soit à gauche et les liens à droite. Donc pour la balise `nav`, après en avoir fait un conteneur flex, nous utilisons `justify-content: space-between;` pour les aligner.

* Dans `css/style.css`

```css
.container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(15rem, 1fr));
  grid-gap: 1rem;
  justify-content: center;
  align-items: center;
  margin: auto;
  padding: 1rem 0;
}
.card {
  display: flex;
  align-items: center;
  flex-direction: column;
  width: 15rem auto;
  height: 15rem;
  background: #fff;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.19), 0 6px 6px rgba(0, 0, 0, 0.23);
  border-radius: 10px;
  margin: auto;
  overflow: hidden;
}
.card--avatar {
  width: 100%;
  height: 10rem;
  object-fit: cover;
}
.card--title {
  color: #222;
  font-weight: 700;
  text-transform: capitalize;
  font-size: 1.1rem;
  margin-top: 0.5rem;
}
.card--link {
  text-decoration: none;
  background: #db4938;
  color: #fff;
  padding: 0.3rem 1rem;
  border-radius: 20px;
}

```

Nous aurons plusieurs cartes, donc pour l'élément conteneur, il sera affiché sous forme de grille. Et, avec `grid-template-columns: repeat(auto-fit, minmax(15rem, 1fr))`, nous pouvons maintenant rendre nos cartes réactives afin qu'elles utilisent au moins `15rem` de largeur si il y a assez d'espace (et `1fr` si ce n'est pas le cas).

Et pour les rendre belles, nous doublons l'effet d'ombre sur la classe `.card` et utilisons `object-fit: cover` sur `.card--avatar` pour empêcher l'image de s'étirer.

Maintenant, cela a l'air beaucoup mieux – mais nous n'avons toujours pas de données à afficher.

Corrigeons cela dans la section suivante.

## Afficher les données avec JavaScript

Remarquez que j'ai utilisé de grandes images qui prennent un certain temps à charger. Cela vous montrera de la meilleure façon la puissance des service workers.

Comme je l'ai dit plus tôt, la classe `.container` contiendra nos cartes. Par conséquent, nous devons la sélectionner.

* Dans `js/app.js`

```javascript
const container = document.querySelector(".container")
const coffees = [
  { name: "Perspiciatis", image: "images/coffee1.jpg" },
  { name: "Voluptatem", image: "images/coffee2.jpg" },
  { name: "Explicabo", image: "images/coffee3.jpg" },
  { name: "Rchitecto", image: "images/coffee4.jpg" },
  { name: " Beatae", image: "images/coffee5.jpg" },
  { name: " Vitae", image: "images/coffee6.jpg" },
  { name: "Inventore", image: "images/coffee7.jpg" },
  { name: "Veritatis", image: "images/coffee8.jpg" },
  { name: "Accusantium", image: "images/coffee9.jpg" },
]

```

Ensuite, nous créons un tableau de cartes avec des noms et des images.

* Dans `js/app.js`

```javascript
const showCoffees = () => {
  let output = ""
  coffees.forEach(
    ({ name, image }) =>
      (output += `
              <div class="card">
                <img class="card--avatar" src=${image} />
                <h1 class="card--title">${name}</h1>
                <a class="card--link" href="#">Goûter</a>
              </div>
              `)
  )
  container.innerHTML = output
}

document.addEventListener("DOMContentLoaded", showCoffees)

```

Avec ce code ci-dessus, nous pouvons maintenant parcourir le tableau et les afficher dans le fichier HTML. Et pour que tout fonctionne, nous attendons que le contenu du DOM (Document Object Model) finisse de charger pour exécuter la méthode `showCoffees`.

Nous avons fait beaucoup de choses, mais pour l'instant, nous n'avons qu'une application web traditionnelle. Alors, changeons cela dans la section suivante en introduisant quelques fonctionnalités de PWA.

![super-excité](https://media.giphy.com/media/l3V0dy1zzyjbYTQQM/source.gif)

## Manifest de l'application web

Le manifest de l'application web est un simple fichier JSON qui informe le navigateur à propos de votre application web. Il indique comment elle doit se comporter lorsqu'elle est installée sur le mobile ou le bureau de l'utilisateur. Et pour afficher l'invite Ajouter à l'écran d'accueil, le manifest de l'application web est requis.

Maintenant que nous savons ce qu'est un manifest web, créons un nouveau fichier nommé `manifest.json` (vous devez le nommer ainsi) dans le répertoire racine. Ensuite, ajoutez ce bloc de code ci-dessous.

* Dans `manifest.json`

```javascript
{
  "name": "Dev'Coffee",
  "short_name": "DevCoffee",
  "start_url": "index.html",
  "display": "standalone",
  "background_color": "#fdfdfd",
  "theme_color": "#db4938",
  "orientation": "portrait-primary",
  "icons": [
    {
      "src": "/images/icons/icon-72x72.png",
      "type": "image/png", "sizes": "72x72"
    },
    {
      "src": "/images/icons/icon-96x96.png",
      "type": "image/png", "sizes": "96x96"
    },
    {
      "src": "/images/icons/icon-128x128.png",
      "type": "image/png","sizes": "128x128"
    },
    {
      "src": "/images/icons/icon-144x144.png",
      "type": "image/png", "sizes": "144x144"
    },
    {
      "src": "/images/icons/icon-152x152.png",
      "type": "image/png", "sizes": "152x152"
    },
    {
      "src": "/images/icons/icon-192x192.png",
      "type": "image/png", "sizes": "192x192"
    },
    {
      "src": "/images/icons/icon-384x384.png",
      "type": "image/png", "sizes": "384x384"
    },
    {
      "src": "/images/icons/icon-512x512.png",
      "type": "image/png", "sizes": "512x512"
    }
  ]
}

```

En fin de compte, ce n'est qu'un fichier JSON avec certaines propriétés obligatoires et facultatives.

name: Lorsque le navigateur lance l'écran de démarrage, ce sera le nom affiché à l'écran.

short_name: Ce sera le nom affiché sous votre raccourci d'application sur l'écran d'accueil.

start_url: Ce sera la page montrée à l'utilisateur lorsque votre application est ouverte.

display: Il indique au navigateur comment afficher l'application. Il existe plusieurs modes comme `minimal-ui`, `fullscreen`, `browser` etc. Ici, nous utilisons le mode `standalone` pour masquer tout ce qui est lié au navigateur.

background_color: Lorsque le navigateur lance l'écran de démarrage, ce sera l'arrière-plan de l'écran.

theme_color: Ce sera la couleur d'arrière-plan de la barre d'état lorsque nous ouvrons l'application.

orientation: Il indique au navigateur l'orientation à avoir lors de l'affichage de l'application.

icons: Lorsque le navigateur lance l'écran de démarrage, ce sera l'icône affichée à l'écran. Ici, j'ai utilisé toutes les tailles pour correspondre à l'icône préférée de tout appareil. Mais vous pouvez simplement utiliser une ou deux. C'est à vous de voir.

Maintenant que nous avons un manifest d'application web, ajoutons-le au fichier HTML.

* Dans `index.html` (balise head)

```html
<link rel="manifest" href="manifest.json" />
<!-- support ios -->
<link rel="apple-touch-icon" href="images/icons/icon-72x72.png" />
<link rel="apple-touch-icon" href="images/icons/icon-96x96.png" />
<link rel="apple-touch-icon" href="images/icons/icon-128x128.png" />
<link rel="apple-touch-icon" href="images/icons/icon-144x144.png" />
<link rel="apple-touch-icon" href="images/icons/icon-152x152.png" />
<link rel="apple-touch-icon" href="images/icons/icon-192x192.png" />
<link rel="apple-touch-icon" href="images/icons/icon-384x384.png" />
<link rel="apple-touch-icon" href="images/icons/icon-512x512.png" />
<meta name="apple-mobile-web-app-status-bar" content="#db4938" />
<meta name="theme-color" content="#db4938" />

```

Comme vous pouvez le voir, nous avons lié notre fichier `manifest.json` à la balise head. Et nous avons ajouté quelques autres liens qui gèrent la prise en charge d'iOS pour afficher les icônes et colorer la barre d'état avec notre couleur de thème.

Avec cela, nous pouvons maintenant plonger dans la partie finale et introduire le service worker.

## Qu'est-ce qu'un Service Worker ?

Remarquez que les PWA ne s'exécutent que sur https car le service worker peut accéder à la requête et la gérer. Par conséquent, la sécurité est requise.

Un service worker est un script que votre navigateur exécute en arrière-plan dans un thread séparé. Cela signifie qu'il s'exécute dans un endroit différent et est complètement séparé de votre page web. C'est la raison pour laquelle il ne peut pas manipuler votre élément DOM.

Cependant, il est super puissant. Le service worker peut intercepter et gérer les requêtes réseau, gérer le cache pour activer la prise en charge hors ligne ou envoyer des notifications push à vos utilisateurs.

![wow](https://media.giphy.com/media/5VKbvrjxpVJCM/source.gif)

Alors créons notre tout premier service worker dans le dossier racine et nommons-le `serviceWorker.js` (le nom est à vous). Mais vous devez le mettre dans la racine afin de ne pas limiter sa portée à un seul dossier.

### Mettre en cache les ressources

* Dans `serviceWorker.js`

```javascript
const staticDevCoffee = "dev-coffee-site-v1"
const assets = [
  "/",
  "/index.html",
  "/css/style.css",
  "/js/app.js",
  "/images/coffee1.jpg",
  "/images/coffee2.jpg",
  "/images/coffee3.jpg",
  "/images/coffee4.jpg",
  "/images/coffee5.jpg",
  "/images/coffee6.jpg",
  "/images/coffee7.jpg",
  "/images/coffee8.jpg",
  "/images/coffee9.jpg",
]

self.addEventListener("install", installEvent => {
  installEvent.waitUntil(
    caches.open(staticDevCoffee).then(cache => {
      cache.addAll(assets)
    })
  )
})

```

Ce code semble intimidant au premier abord, mais ce n'est que du JavaScript (donc ne vous inquiétez pas).

Nous déclarons le nom de notre cache `staticDevCoffee` et les ressources à stocker dans le cache. Et pour effectuer cette action, nous devons attacher un écouteur à `self`.

`self` est le service worker lui-même. Il nous permet d'écouter les événements du cycle de vie et de faire quelque chose en retour.

Le service worker a plusieurs cycles de vie, et l'un d'eux est l'événement `install`. Il s'exécute lorsqu'un service worker est installé. Il est déclenché dès que le worker s'exécute, et il n'est appelé qu'une seule fois par service worker.

Lorsque l'événement `install` est déclenché, nous exécutons le callback qui nous donne accès à l'objet `event`.

La mise en cache de quelque chose sur le navigateur peut prendre un certain temps à terminer car c'est asynchrone.

Pour le gérer, nous devons utiliser `waitUntil()` qui, comme vous pouvez le deviner, attend que l'action se termine.

Une fois que l'API de cache est prête, nous pouvons exécuter la méthode `open()` et créer notre cache en passant son nom comme argument à `caches.open(staticDevCoffee)`.

Ensuite, il retourne une promesse, qui nous aide à stocker nos ressources dans le cache avec `cache.addAll(assets)`.

![Images de café mises en cache](https://www.freecodecamp.org/news/content/images/2021/10/cached-images.png)

Espérons que vous êtes toujours avec moi.

![désespéré](https://media.giphy.com/media/OQEcw90jACeU8/source.gif)

Maintenant, nous avons mis en cache nos ressources dans le navigateur avec succès. Et la prochaine fois que nous chargerons la page, le service worker gérera la requête et récupérera le cache si nous sommes hors ligne.

Alors, récupérons notre cache.

### Récupérer les ressources

* Dans `serviceWorker.js`

```javascript
self.addEventListener("fetch", fetchEvent => {
  fetchEvent.respondWith(
    caches.match(fetchEvent.request).then(res => {
      return res || fetch(fetchEvent.request)
    })
  )
})

```

Ici, nous utilisons l'événement `fetch` pour, eh bien, récupérer nos données. Le callback nous donne accès à `fetchEvent`. Ensuite, nous attachons `respondWith()` pour empêcher la réponse par défaut du navigateur. Au lieu de cela, il retourne une promesse car l'action de récupération peut prendre du temps à se terminer.

Et une fois le cache prêt, nous appliquons `caches.match(fetchEvent.request)`. Il vérifiera si quelque chose dans le cache correspond à `fetchEvent.request`. Au fait, `fetchEvent.request` est simplement notre tableau de ressources.

Ensuite, il retourne une promesse. Et enfin, nous pouvons retourner le résultat s'il existe ou la récupération initiale si ce n'est pas le cas.

Maintenant, nos ressources peuvent être mises en cache et récupérées par le service worker, ce qui augmente considérablement le temps de chargement de nos images.

Et surtout, cela rend notre application disponible en mode hors ligne.

Mais un service worker seul ne peut pas faire le travail. Nous devons l'enregistrer dans notre projet.

![faisons-le](https://media.giphy.com/media/Z9EvIRmLEOS3JNFeVb/source.gif)

## Enregistrer le Service Worker

* Dans `js/app.js`

```javascript
if ("serviceWorker" in navigator) {
  window.addEventListener("load", function() {
    navigator.serviceWorker
      .register("/serviceWorker.js")
      .then(res => console.log("service worker enregistré"))
      .catch(err => console.log("service worker non enregistré", err))
  })
}

```

Ici, nous commençons par vérifier si `serviceWorker` est pris en charge par le navigateur actuel (car il n'est toujours pas pris en charge par tous les navigateurs).

Ensuite, nous écoutons l'événement de chargement de la page pour enregistrer notre service worker en passant le nom de notre fichier `serviceWorker.js` à `navigator.serviceWorker.register()` en tant que paramètre pour enregistrer notre worker.

Avec cette mise à jour, nous avons maintenant transformé notre application web régulière en une PWA.

![nous-lavons-fait](https://media.giphy.com/media/3o6ZtlGkjeschymLNm/source.gif)

## Réflexions finales

Tout au long de cet article, nous avons vu à quel point les PWA peuvent être incroyables. En ajoutant un fichier manifest d'application web et un service worker, cela améliore vraiment l'expérience utilisateur de notre application web traditionnelle. Cela est dû au fait que les PWA sont rapides, sécurisées, fiables et – surtout – elles prennent en charge le mode hors ligne.

De nombreux frameworks disponibles aujourd'hui viennent avec un fichier de service worker déjà configuré pour nous. Mais savoir comment l'implémenter avec Vanilla JavaScript peut vous aider à comprendre les PWA.

Et vous pouvez aller encore plus loin avec les service workers en mettant en cache des ressources dynamiquement ou en limitant la taille de votre cache, etc.

Merci d'avoir lu cet article.

Vous pouvez le consulter en direct [ici](https://devcoffee-pwa.netlify.com/) et le code source est [ici](https://github.com/ibrahima92/pwa-with-vanilla-js).

Lisez plus de mes articles sur [mon blog](https://www.ibrahima-ndaw.com/blog/how-to-build-pwa-with-javascript/)

## Prochaines étapes

[Documentation sur le Manifest Web](https://developers.google.com/web/fundamentals/web-app-manifest)

[Documentation sur les Service Workers](https://developers.google.com/web/fundamentals/primers/service-workers)

[Générateur de Manifest Web](https://app-manifest.firebaseapp.com/)

[Prise en charge des navigateurs](https://caniuse.com/#search=service%20worker)