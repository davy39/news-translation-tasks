---
title: Comment j'ai rendu mon site web basé sur un CMS fonctionnel hors ligne
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2017-11-13T10:03:40.000Z'
originalURL: https://freecodecamp.org/news/how-i-made-my-cms-based-website-work-offline-f34afc393ca8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*AW_JMRH74Tu6yX0eWLltow.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment j'ai rendu mon site web basé sur un CMS fonctionnel hors ligne
seo_desc: 'Interested in learning JavaScript? Get my ebook at jshandbook.com


  This case study explains how I added the capability of working offline to the writesoftware.org
  website (which is based on Grav, a great PHP-based CMS for developers). I did this
  by i...'
---

> Intéressé par l'apprentissage de JavaScript ? Obtenez mon ebook sur [jshandbook.com](https://jshandbook.com/)

Cette étude de cas explique comment j'ai ajouté la capacité de fonctionner hors ligne au site web [writesoftware.org](https://writesoftware.org/) (qui est basé sur Grav, un excellent [CMS basé sur PHP pour les développeurs](https://getgrav.org/)). J'ai fait cela en introduisant un ensemble de technologies regroupées sous le nom d'**Applications Web Progressives** (en particulier les **Service Workers** et l'**Cache API**).

> Il y a beaucoup à apprendre sur ce sujet et les nouvelles API de navigateur. Je publie beaucoup de contenu lié sur mon [blog sur le développement frontend](https://flaviocopes.com), ne le manquez pas !

Je vais montrer les options que j'avais à ma disposition, et pourquoi j'ai choisi une approche plutôt que les autres.

Lorsque nous aurons terminé, nous pourrons utiliser notre site sur un appareil mobile ou sur un navigateur de bureau — même hors ligne — comme je l'ai montré ici :

![Image](https://cdn-media-1.freecodecamp.org/images/1*j2sFn6mO9JRmpCpmaymcBg.gif)
_Remarquez l'option « Hors ligne » dans les paramètres de limitation du réseau_

## Première approche : cache-first

J'ai d'abord abordé la tâche en utilisant une approche cache-first : lorsque nous interceptons une requête de récupération dans le Service Worker, nous **vérifions d'abord si nous l'avons déjà en cache**. Si ce n'est pas le cas, **nous la récupérons depuis le réseau**.

Cela présente l'avantage de rendre le site **extrêmement rapide** lors du chargement des pages déjà en cache, même en ligne — en particulier avec des réseaux lents et le [**lie-fi**](https://developers.google.com/web/fundamentals/performance/poor-connectivity/#what_is_lie-fi). Mais cela introduit également une certaine **complexité** dans la gestion des mises à jour du cache lorsque je publie du nouveau contenu.

_Ce ne sera pas la solution finale que j'adopte_, mais cela vaut la peine de la parcourir à des fins de démonstration.

Je vais passer par quelques phases :

1. J'**introduis un Service Worker** et le charge à l'aide d'un script JS
2. Lorsque j'installe le Service Worker, je **mets en cache le _squelette_ du site**
3. J'**intercepte les requêtes réseau** allant vers des liens supplémentaires et **les mets en cache**

### Introduction d'un Service Worker

J'ajoute le Service Worker dans un fichier `sw.js` à la racine du site. Cela lui donne suffisamment de portée pour fonctionner sur tous les sous-dossiers du site, ainsi que sur la page d'accueil du site ([plus d'informations sur la **portée des Service Workers**](https://www.writesoftware.org/topic/service-workers/lifecycle) ici). Le SW pour le moment est assez basique, car il se contente de journaliser toute requête réseau :

```js
self.addEventListener('fetch', (event) => {
  console.log(event.request)
})

```

Je dois enregistrer le Service Worker, et je fais cela à partir d'un script que j'inclus dans chaque page :

```js
window.addEventListener('load', () => {
  if (!navigator.serviceWorker) {
    return
  }

  navigator.serviceWorker.register('/sw.js', {
    scope: '/'
  }).then(() => {
    //...ok
  }).catch((err) => {
    console.log('registration failed', err)
  })
})

```

Si les Service Workers sont disponibles, nous enregistrons le fichier `sw.js`, et la prochaine fois que je rafraîchis la page, il devrait fonctionner correctement :

![Image](https://cdn-media-1.freecodecamp.org/images/1*tc-pueF9fW3lOJ0bev5plA.png)

À ce stade, je dois faire un peu de travail sur le site. Tout d'abord, je dois trouver un moyen de servir uniquement le **App Shell** : un ensemble de base de HTML + CSS et JS qui sera toujours disponible et montré aux utilisateurs, même hors ligne.

C'est essentiellement une version épurée du site web, avec un élément `<div class="wrapper row" id="content-wrapper"></div>` vide, que nous remplirons avec du contenu plus tard, disponible sous la route `/shell` :

![Image](https://cdn-media-1.freecodecamp.org/images/1*8g5q0wk7GidnA40JuepsvA.png)

Ainsi, la première fois que l'utilisateur charge le site, la version normale d'une page sera affichée (version HTML complète), et **le Service Worker est installé**.

Maintenant, toute autre page sur laquelle on clique est interceptée par notre Service Worker. Chaque fois qu'une page est chargée, nous chargeons d'abord le shell, puis nous chargeons une version épurée de la page, sans le shell, **juste le contenu**.

Comment ?

Nous écoutons l'événement `install`, qui se déclenche lorsque le Service Worker est installé ou mis à jour. Lorsque cela se produit, nous initialisons le cache avec le contenu de notre shell : la disposition HTML de base, plus un peu de CSS, JS, et quelques actifs externes :

```js
const cacheName = 'writesoftware-v1'

self.addEventListener('install', (event) => {
  event.waitUntil(caches.open(cacheName).then(cache => cache.addAll([
    '/shell',
    'user/themes/writesoftware/favicon.ico',
    'user/themes/writesoftware/css/style.css',
    'user/themes/writesoftware/js/script.js',
    'https://fonts.googleapis.com/css?family=Press+Start+2P',
    'https://fonts.googleapis.com/css?family=Inconsolata:400,700',
    'https://cdnjs.cloudflare.com/ajax/libs/prism/1.6.0/themes/prism.min.css',
    'https://cdnjs.cloudflare.com/ajax/libs/prism/1.6.0/prism.min.js',
    'https://cdn.jsdelivr.net/prism/1.6.0/components/prism-jsx.min.js'
  ])))
})
```

Ensuite, lorsque nous effectuons une récupération, nous interceptons les requêtes vers nos pages, et **nous récupérons le shell depuis le Cache au lieu d'aller sur le réseau**.

Si l'URL appartient à Google Analytics ou ConvertKit, j'évite d'utiliser le cache local, et je les récupère sans utiliser **CORS** (puisque je ne suis pas autorisé à y accéder par cette méthode).

Ensuite, si je demande un **partial local** (juste le contenu d'une page, pas la page complète), je fais simplement une requête de récupération pour l'obtenir.

Si ce n'est pas un partial, **nous retournons le shell**, qui est **déjà en cache** lorsque le Service Worker est installé pour la première fois.

Une fois la récupération terminée, je la mets en cache.

```js
self.addEventListener('fetch', (event) => {
  const requestUrl = new URL(event.request.url)

  if (requestUrl.href.startsWith('https://www.googletagmanager.com') ||
      requestUrl.href.startsWith('https://www.google-analytics.com') ||
      requestUrl.href.startsWith('https://assets.convertkit.com')) {
    // don't cache, and no cors
    event.respondWith(fetch(event.request.url, { mode: 'no-cors' }))
    return
  }

  event.respondWith(caches.match(event.request)
    .then((response) => {
      if (response) { return response }
      if (requestUrl.origin === location.origin) {
        if (requestUrl.pathname.endsWith('?partial=true')) {
          return fetch(requestUrl.pathname)
        } else {
          return caches.match('/shell')
        }

        return fetch(`${event.request.url}?partial=true`)
      }
      return fetch(event.request.url)
    })
    .then(response => caches.open(cacheName).then((cache) => {
      cache.put(event.request.url, response.clone())
      return response
    }))
    .catch((error) => {
      console.error(error)
    }))
})

```

Maintenant, j'édite le fichier `script.js` pour introduire une fonctionnalité importante : chaque fois qu'un lien est cliqué sur mes pages, je l'intercepte et j'envoie un message à un **Broadcast Channel**.

Puisque les Service Workers sont actuellement uniquement pris en charge dans Chrome, Firefox et Opera, je peux m'appuyer en toute sécurité sur l'[API BroadcastChannel](https://developers.google.com/web/updates/2016/09/broadcastchannel) pour cela.

![Image](https://cdn-media-1.freecodecamp.org/images/1*WGlDwfv4Seza_h-8AO1HRA.png)

Tout d'abord, je me connecte au canal `ws_navigation`, et j'attache un gestionnaire d'événements `onmessage` dessus. Chaque fois que je reçois un événement, c'est une communication du Service Worker avec un nouveau contenu à afficher à l'intérieur de l'App Shell. Je cherche simplement l'élément avec l'id `content-wrapper` et je mets le contenu de la page partielle dedans, changeant effectivement la page que l'utilisateur voit.

Dès que le Service Worker est enregistré, **j'envoie un message à ce canal** avec une tâche `fetchPartial` et une **URL de page partielle à récupérer**. C'est le contenu du chargement initial de la page.

**Le shell est chargé immédiatement** puisqu'il est toujours en cache. Peu après, le contenu réel est recherché, qui peut également être en cache.

```js
window.addEventListener('load', () => {
  if (!navigator.serviceWorker) { return }
  const channel = new BroadcastChannel('ws_navigation')

  channel.onmessage = (event) => {
    if (document.getElementById('content-wrapper')) {
      document.getElementById('content-wrapper').innerHTML = event.data.content
    }
  }

  navigator.serviceWorker.register('/sw.js', {
    scope: '/'
  }).then(() => {
    channel.postMessage({
      task: 'fetchPartial',
      url: `${window.location.pathname}?partial=true`
    })
  }).catch((err) => {
    console.log('SW registration failed', err)
  })
})

```

Le morceau manquant est **la gestion d'un clic sur la page**. Lorsqu'un lien est cliqué, j'intercepte l'événement, l'arrête, et envoie un message au Service Worker pour récupérer le partial avec cette URL.

Lors de la récupération d'un partial, j'ajoute une requête `?partial=true` pour indiquer à mon backend de ne servir que le contenu, pas le shell.

```js
window.addEventListener('load', () => {

  //...

  window.onclick = (e) => {
    let node = e.target
    while (node !== undefined && node !== null && node.localName !== 'a') {
      node = node.parentNode
    }
    if (node !== undefined && node !== null) {
      channel.postMessage({
        task: 'fetchPartial',
        url: `${node.href}?partial=true`
      })
      return false
    }
    return true
  }
})

```

Maintenant, il ne nous reste plus qu'à gérer cet événement. Du côté du Service Worker, je me connecte au canal `ws_navigation` et j'écoute un événement. J'écoute le nom de la tâche de message `fetchPartial`, bien que je puisse simplement éviter cette vérification de condition car c'est le seul événement qui est envoyé ici. Notez que les messages dans l'API Broadcast Channel **ne sont pas distribués à la même page qui les origine** — ils ne sont distribués qu'entre une page et un web worker.

**Je vérifie si l'URL est en cache**. Si c'est le cas, je l'envoie simplement en tant que message de réponse sur le canal et je retourne.

Si elle n'est pas en cache, je la récupère, l'envoie en retour en tant que message à la page, puis la mets en cache pour la prochaine fois qu'elle pourrait être visitée.

```js
const channel = new BroadcastChannel('ws_navigation')
channel.onmessage = (event) => {
  if (event.data.task === 'fetchPartial') {
    caches
      .match(event.data.url)
      .then((response) => {
        if (response) {
          response.text().then((body) => {
            channel.postMessage({ url: event.data.url, content: body })
          })
          return
        }

        fetch(event.data.url).then((fetchResponse) => {
          const fetchResponseClone = fetchResponse.clone()
          fetchResponse.text().then((body) => {
            channel.postMessage({ url: event.data.url, content: body })
          })

          caches.open(cacheName).then((cache) => {
            cache.put(event.data.url, fetchResponseClone)
          })
        })
      })
      .catch((error) => {
        console.error(error)
      })
  }
}

```

Nous avons presque terminé.

Maintenant, le Service Worker est installé sur le site dès qu'un utilisateur le visite. Les chargements de pages suivants sont gérés dynamiquement via l'[API Fetch](https://www.writesoftware.org/topic/fetch-api), ne nécessitant pas un chargement complet de la page. Après la première visite, les pages sont mises en cache et se chargent incroyablement rapidement, et — plus important encore — **elles se chargent même hors ligne** !

Et — tout cela est une **amélioration progressive**. Les anciens navigateurs, et les navigateurs qui ne supportent pas les Service Workers, fonctionnent simplement normalement.

Maintenant, détourner la navigation du navigateur pose quelques problèmes :

1. L'**URL doit changer** lorsqu'une nouvelle page est affichée. Le bouton de retour doit fonctionner normalement, ainsi que l'historique du navigateur.
2. Le **titre de la page doit changer** pour refléter le nouveau titre de la page.
3. Nous devons **notifier l'API Google Analytics** qu'une nouvelle page a été chargée pour éviter de manquer une métrique importante telle que les vues de page par visiteur.
4. Les **extraits de code ne sont plus mis en évidence** lors du chargement de nouveau contenu dynamiquement.

Résolvons ces défis.

### Corriger l'URL, le titre et le bouton de retour avec l'API History

En plus d'injecter le HTML du partial dans le gestionnaire de messages dans script.js, nous déclenchons la méthode `history.pushState()` :

```js
channel.onmessage = (event) => {
  if (document.getElementById('content-wrapper')) {
    document.getElementById('content-wrapper').innerHTML = event.data.content
    const url = event.data.url.replace('?partial=true', '')
    history.pushState(null, null, url)
  }
}

```

Cela fonctionne, mais le titre de la page ne change pas dans l'interface utilisateur du navigateur. Nous devons le récupérer d'une manière ou d'une autre depuis la page. J'ai décidé de mettre un span caché dans le contenu partiel de la page qui conserve le titre de la page. Ensuite, nous pouvons le récupérer depuis la page en utilisant l'API DOM, et définir la propriété `document.title` :

```js
channel.onmessage = (event) => {
  if (document.getElementById('content-wrapper')) {
    document.getElementById('content-wrapper').innerHTML = event.data.content
    const url = event.data.url.replace('?partial=true', '')
    if (document.getElementById('browser-page-title')) {
      document.title = document.getElementById('browser-page-title').innerHTML
    }
    history.pushState(null, null, url)
  }
}

```

### Corriger Google Analytics

Google Analytics fonctionne bien dès la sortie de la boîte, mais lors du chargement d'une page dynamiquement, il ne peut pas faire de miracles. Nous devons utiliser l'API qu'il fournit pour l'informer d'un nouveau chargement de page. Puisque j'utilise le suivi Global Site Tag (`gtag.js`), je dois appeler :

```js
gtag('config', 'UA-XXXXXX-XX', {'page_path': '/the-url'})

```

dans le code ci-dessus qui gère le changement de page :

```js
channel.onmessage = (event) => {
  if (document.getElementById('content-wrapper')) {
    document.getElementById('content-wrapper').innerHTML = event.data.content
    const url = event.data.url.replace('?partial=true', '')
    if (document.getElementById('browser-page-title')) {
      document.title = document.getElementById('browser-page-title').innerHTML
    }
    history.pushState(null, null, url)
    gtag('config', 'UA-XXXXXX-XX', {'page_path': url})
  }
}

```

Et si... l'utilisateur est hors ligne ? Idéalement, il devrait y avoir un écouteur d'événements `fetch` qui met en cache toute requête allant à Google Analytics et les rejoue dès que je suis à nouveau en ligne.

Heureusement [il existe une bibliothèque qui fait exactement cela](https://developers.google.com/web/updates/2016/07/offline-google-analytics), en s'appuyant sur IndexedDB pour stocker les données. Elle a été [déplacée dans Workbox](https://workboxjs.org/reference-docs/latest/module-workbox-google-analytics.html), si vous préférez utiliser cette bibliothèque pour gérer la mise en cache à un niveau supérieur.

### Corriger la mise en évidence de la syntaxe

La dernière chose que je dois corriger sur ma page est la mise en évidence de la connexion des extraits de code. J'utilise le surligneur de syntaxe Prism et ils le rendent très facile — je dois simplement ajouter un appel `Prism.highlightAll()` dans mon gestionnaire `onmessage` :

```js
channel.onmessage = (event) => {
  if (document.getElementById('content-wrapper')) {
    document.getElementById('content-wrapper').innerHTML = event.data.content
    const url = event.data.url.replace('?partial=true', '')
    if (document.getElementById('browser-page-title')) {
      document.title = document.getElementById('browser-page-title').innerHTML
    }
    history.pushState(null, null, url)
    gtag('config', 'UA-XXXXXX-XX', {'page_path': url})
    Prism.highlightAll()
  }
}

```

Le code complet de `script.js` est :

```js
window.addEventListener('load', () => {
  if (!navigator.serviceWorker) { return }
  const channel = new BroadcastChannel('ws_navigation')

  channel.onmessage = (event) => {
    if (document.getElementById('content-wrapper')) {
      document.getElementById('content-wrapper').innerHTML = event.data.content
      const url = event.data.url.replace('?partial=true', '')
      if (document.getElementById('browser-page-title')) {
        document.title = document.getElementById('browser-page-title').innerHTML
      }
      history.pushState(null, null, url)
      gtag('config', 'UA-1739509-49', {'page_path': url})
      Prism.highlightAll()
    }
  }

  navigator.serviceWorker.register('/sw.js', {
    scope: '/'
  }).then(() => {
    channel.postMessage({
      task: 'fetchPartial',
      url: `${window.location.pathname}?partial=true`
    })
  }).catch((err) => {
    console.log('SW registration failed', err)
  })

  window.onclick = (e) => {
    let node = e.target
    while (node !== undefined && node !== null && node.localName !== 'a') {
      node = node.parentNode
    }
    if (node !== undefined && node !== null) {
      channel.postMessage({
        task: 'fetchPartial',
        url: `${node.href}?partial=true`
      })
      return false
    }
    return true
  }
})

```

et `sw.js` :

```js
const cacheName = 'writesoftware-v1'

self.addEventListener('install', (event) => {
  event.waitUntil(caches.open(cacheName).then(cache => cache.addAll([
    '/shell',
    'user/themes/writesoftware/favicon.ico',
    'user/themes/writesoftware/css/style.css',
    'user/themes/writesoftware/js/script.js',
    'user/themes/writesoftware/img/offline.gif',
    'https://fonts.googleapis.com/css?family=Press+Start+2P',
    'https://fonts.googleapis.com/css?family=Inconsolata:400,700',
    'https://cdnjs.cloudflare.com/ajax/libs/prism/1.6.0/themes/prism.min.css',
    'https://cdnjs.cloudflare.com/ajax/libs/prism/1.6.0/prism.min.js',
    'https://cdn.jsdelivr.net/prism/1.6.0/components/prism-jsx.min.js'
  ])))
})

self.addEventListener('fetch', (event) => {
  const requestUrl = new URL(event.request.url)

  if (requestUrl.href.startsWith('https://www.googletagmanager.com') ||
      requestUrl.href.startsWith('https://www.google-analytics.com') ||
      requestUrl.href.startsWith('https://assets.convertkit.com')) {
    // don't cache, and no cors
    event.respondWith(fetch(event.request.url, { mode: 'no-cors' }))
    return
  }

  event.respondWith(caches.match(event.request)
    .then((response) => {
      if (response) { return response }
      if (requestUrl.origin === location.origin) {
        if (requestUrl.pathname.endsWith('?partial=true')) {
          return fetch(requestUrl.pathname)
        } else {
          return caches.match('/shell')
        }

        return fetch(`${event.request.url}?partial=true`)
      }
      return fetch(event.request.url)
    })
    .then(response => caches.open(cacheName).then((cache) => {
      if (response) {
        cache.put(event.request.url, response.clone())
      }
      return response
    }))
    .catch((error) => {
      console.error(error)
    }))
})

const channel = new BroadcastChannel('ws_navigation')
channel.onmessage = (event) => {
  if (event.data.task === 'fetchPartial') {
    caches
      .match(event.data.url)
      .then((response) => {
        if (response) {
          response.text().then((body) => {
            channel.postMessage({ url: event.data.url, content: body })
          })
          return
        }

        fetch(event.data.url).then((fetchResponse) => {
          const fetchResponseClone = fetchResponse.clone()
          fetchResponse.text().then((body) => {
            channel.postMessage({ url: event.data.url, content: body })
          })

          caches.open(cacheName).then((cache) => {
            cache.put(event.data.url, fetchResponseClone)
          })
        })
      })
      .catch((error) => {
        console.error(error)
      })
  }
}

```

## Deuxième approche : network-first, abandonner l'app shell

Bien que la première approche nous ait donné une application entièrement fonctionnelle, j'étais un peu sceptique et inquiet de avoir une copie d'une page mise en cache trop longtemps sur le client. J'ai donc décidé d'essayer une approche network-first : lorsque l'utilisateur charge une page, elle est d'abord récupérée depuis le réseau.

Si l'appel réseau échoue pour une raison quelconque, je recherche la page dans le cache pour voir si nous l'avons mise en cache. Sinon, je montre à l'utilisateur un GIF s'il est totalement hors ligne, ou un autre GIF si la page n'existe pas (je peux l'atteindre, mais j'ai obtenu une erreur 404).

Dès que nous obtenons une page, nous la mettons en cache (sans vérifier si nous l'avons mise en cache précédemment ou non, nous stockons simplement la dernière version).

En tant qu'expérience, j'ai également abandonné l'app shell, car dans mon cas, je n'avais pas l'intention de créer une application installable pour l'instant. Sans un appareil Android à jour, je ne pouvais pas vraiment le tester, et j'ai préféré éviter de jeter des choses sans un test approprié.

Pour ce faire, j'ai simplement supprimé l'app shell de l'événement `install` du Service Worker. Je me suis appuyé sur les Service Workers et l'API Cache pour livrer simplement les pages simples du site, sans gérer les mises à jour partielles. J'ai également abandonné le détournement de la récupération `/shell` lors du chargement d'une page complète. Lors du premier chargement de la page, il n'y a pas de retard, mais nous chargeons toujours des partials lors de la navigation vers d'autres pages plus tard.

J'utilise toujours `script.js` et `sw.js` pour héberger le code, avec `script.js` étant le fichier qui initialise le Service Worker, et intercepte également les clics côté client.

Voici `script.js` :

```js
const OFFLINE_GIF = '/user/themes/writesoftware/img/offline.gif'

const fetchPartial = (url) => {
  fetch(`${url}?partial=true`)
  .then((response) => {
    response.text().then((body) => {
      if (document.getElementById('content-wrapper')) {
        document.getElementById('content-wrapper').innerHTML = body
        if (document.getElementById('browser-page-title')) {
          document.title = document.getElementById('browser-page-title').innerHTML
        }
        history.pushState(null, null, url)
        gtag('config', 'UA-XXXXXX-XX', { page_path: url })
        Prism.highlightAll()
      }
    })
  })
  .catch(() => {
    if (document.getElementById('content-wrapper')) {
    document.getElementById('content-wrapper').innerHTML = `<center><h2>Offline</h2><img src="${OFFLINE_GIF}" /></center>`
    }
  })
}

window.addEventListener('load', () => {
  if (!navigator.serviceWorker) { return }

  navigator.serviceWorker.register('/sw.js', {
    scope: '/'
  }).then(() => {
    fetchPartial(window.location.pathname)
  }).catch((err) => {
    console.log('SW registration failed', err)
  })

  window.onclick = (e) => {
    let node = e.target
    while (node !== undefined && node !== null && node.localName !== 'a') {
      node = node.parentNode
    }
    if (node !== undefined && node !== null) {
      fetchPartial(node.href)
      return false
    }
    return true
  }
})

```

et voici `sw.js` :

```js
const CACHE_NAME = 'writesoftware-v1'
const OFFLINE_GIF = '/user/themes/writesoftware/img/offline.gif'
const PAGENOTFOUND_GIF = '/user/themes/writesoftware/img/pagenotfound.gif'

self.addEventListener('install', (event) => {
  event.waitUntil(caches.open(CACHE_NAME).then(cache => cache.addAll([
    '/user/themes/writesoftware/favicon.ico',
    '/user/themes/writesoftware/css/style.css',
    '/user/themes/writesoftware/js/script.js',
    '/user/themes/writesoftware/img/offline.gif',
    '/user/themes/writesoftware/img/pagenotfound.gif',
    'https://fonts.googleapis.com/css?family=Press+Start+2P',
    'https://fonts.googleapis.com/css?family=Inconsolata:400,700',
    'https://cdnjs.cloudflare.com/ajax/libs/prism/1.6.0/themes/prism.min.css',
    'https://cdnjs.cloudflare.com/ajax/libs/prism/1.6.0/prism.min.js',
    'https://cdn.jsdelivr.net/prism/1.6.0/components/prism-jsx.min.js'
  ])))
})

self.addEventListener('fetch', (event) => {
  if (event.request.method !== 'GET') return
  if (event.request.headers.get('accept').indexOf('text/html') === -1) return

  const requestUrl = new URL(event.request.url)
  let options = {}

  if (requestUrl.href.startsWith('https://www.googletagmanager.com') ||
      requestUrl.href.startsWith('https://www.google-analytics.com') ||
      requestUrl.href.startsWith('https://assets.convertkit.com')) {
    // no cors
    options = { mode: 'no-cors' }
  }

  event.respondWith(fetch(event.request, options)
    .then((response) => {
      if (response.status === 404) {
        return fetch(PAGENOTFOUND_GIF)
      }
      const resClone = response.clone()
      return caches.open(CACHE_NAME).then((cache) => {
        cache.put(event.request.url, response)
        return resClone
      })
    })
    .catch(() => caches.open(CACHE_NAME).then(cache => cache.match(event.request.url)
      .then((response) => {
        if (response) {
          return response
        }
        return fetch(OFFLINE_GIF)
      })
      .catch(() => fetch(OFFLINE_GIF)))))
```

### Troisième approche : simplifier sans partials du tout

En tant qu'expérience, j'ai abandonné l'intercepteur de clics qui récupère les partials, et je me suis appuyé sur les Service Workers et l'API Cache pour simplement livrer les pages simples du site, sans gérer les mises à jour partielles :

`script.js` :

```js
window.addEventListener('load', () => {
  if (!navigator.serviceWorker) { return }
  navigator.serviceWorker.register('/sw.js', {
    scope: '/'
  }).catch((err) => {
    console.log('SW registration failed', err)
  })
})

```

`sw.js` :

```js
const CACHE_NAME = 'writesoftware-v1'
const OFFLINE_GIF = '/user/themes/writesoftware/img/offline.gif'
const PAGENOTFOUND_GIF = '/user/themes/writesoftware/img/pagenotfound.gif'

self.addEventListener('install', (event) => {
  event.waitUntil(caches.open(CACHE_NAME).then(cache => cache.addAll([
    '/user/themes/writesoftware/favicon.ico',
    '/user/themes/writesoftware/css/style.css',
    '/user/themes/writesoftware/js/script.js',
    '/user/themes/writesoftware/img/offline.gif',
    '/user/themes/writesoftware/img/pagenotfound.gif',
    'https://fonts.googleapis.com/css?family=Press+Start+2P',
    'https://fonts.googleapis.com/css?family=Inconsolata:400,700',
    'https://cdnjs.cloudflare.com/ajax/libs/prism/1.6.0/themes/prism.min.css',
    'https://cdnjs.cloudflare.com/ajax/libs/prism/1.6.0/prism.min.js',
    'https://cdn.jsdelivr.net/prism/1.6.0/components/prism-jsx.min.js'
  ])))
})

self.addEventListener('fetch', (event) => {
  if (event.request.method !== 'GET') return
  if (event.request.headers.get('accept').indexOf('text/html') === -1) return

  const requestUrl = new URL(event.request.url)
  let options = {}

  if (requestUrl.href.startsWith('https://www.googletagmanager.com') ||
      requestUrl.href.startsWith('https://www.google-analytics.com') ||
      requestUrl.href.startsWith('https://assets.convertkit.com')) {
    // no cors
    options = { mode: 'no-cors' }
  }

  event.respondWith(fetch(event.request, options)
    .then((response) => {
      if (response.status === 404) {
        return fetch(PAGENOTFOUND_GIF)
      }
      const resClone = response.clone()
      return caches.open(CACHE_NAME).then((cache) => {
        cache.put(event.request.url, response)
        return resClone
      })
    })
    .catch(() => caches.open(CACHE_NAME).then(cache => cache.match(event.request.url)
      .then((response) => {
        return response || fetch(OFFLINE_GIF)
      })
      .catch(() => fetch(OFFLINE_GIF)))))
    
```

Je pense que c'est l'exemple minimal d'ajout de capacités hors ligne à un site web, tout en gardant les choses simples. Tout type de site web peut ajouter de tels Service Workers sans trop de complexité si cela vous suffit.

## Ce que j'ai fini par implémenter dans mon site web

En fin de compte, je n'ai pas pensé que cette dernière approche était suffisante pour être viable. Mais j'ai également fini par éviter l'App Shell, puisque je ne cherchais pas à créer une application installable, et dans mon cas spécifique, cela compliquait ma navigation. Je m'en suis sorti en faisant des mises à jour partielles avec fetch pour éviter d'avoir à recharger toute la page après la première depuis le serveur.

Tout cela avec une approche network-first, pour éviter d'avoir à gérer les mises à jour du cache et la version des actifs : après tout, cela repose toujours complètement sur les stratégies de mise en cache côté client qui chargent les pages mises en cache depuis le disque, donc je bénéficie toujours de la mise en cache sans compliquer mes déploiements.

> Intéressé par l'apprentissage de JavaScript ? Obtenez mon ebook sur [jshandbook.com](https://jshandbook.com/)