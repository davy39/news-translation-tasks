---
title: Comment rendre votre application fonctionnelle hors ligne avec la puissance
  de JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-23T22:53:06.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-your-app-work-offline-with-the-power-of-javascript-685d968bcfbb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*jRhKpS-07YTKIH6g-xJnbQ.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Comment rendre votre application fonctionnelle hors ligne avec la puissance
  de JavaScript
seo_desc: 'By Adrien Zaganelli

  In today’s world, connectivity has made us more mobile than ever which (paradoxically)
  cause us to be offline sometimes: when we’re in airplane mode, have a bad connection,
  have no more data, are on the subway…and so on.

  A second ...'
---

Par Adrien Zaganelli

Dans le monde d'aujourd'hui, la connectivité nous a rendus plus mobiles que jamais, ce qui (paradoxalement) nous amène parfois à être hors ligne : lorsque nous sommes en mode avion, avons une mauvaise connexion, n'avons plus de données, sommes dans le métro… et ainsi de suite.

Un deuxième effet de cette mobilité est le chargement lent des sites web lourds : Amazon a découvert que seulement [100 millisecondes de temps de chargement supplémentaire leur coûtaient 1% de ventes](https://www.forbes.com/sites/steveolenski/2016/11/10/why-brands-are-fighting-over-milliseconds/).

Dans ces situations, nous aimerions avoir un accès hors ligne à notre contenu. C'est pourquoi des outils comme [Instapaper](https://www.instapaper.com) et [Pocket](https://getpocket.com) existent. [Spotify](https://support.spotify.com/us/listen_everywhere/on_phone_tablet_desktop/listen-offline/) et [Netflix](https://techcrunch.com/2016/11/30/netflix-adds-offline-viewing-for-smartphones-and-tablets/) permettent également de télécharger des médias pour une utilisation hors ligne.

Nous pouvons facilement voir qu'il y a une demande pour cette fonctionnalité et comment elle peut bénéficier à votre entreprise.

**Il est temps pour le web de passer hors ligne.**

Heureusement, nous n'avons plus besoin de construire des applications natives pour atteindre cet objectif. Nous pouvons créer un site web hors ligne avec la puissance de JavaScript grâce aux nouvelles fonctionnalités des **service workers** et de l'**Cache API**.

### Qu'est-ce qu'un Service Worker (SW) ?

Les service workers sont du code JavaScript qui s'exécute en arrière-plan de votre site web, même lorsque la page est fermée. Pour une utilisation hors ligne, l'un de leurs objectifs est de stocker les requêtes réseau ou les images dans le cache du navigateur.

L'agence BETC a créé un site de démonstration appelé [whentheinternetisdown.com](https://whentheinternetisdown.com/) pour l'entreprise de télécommunications française Bouygues. Il ne fonctionne que hors ligne et semble magique. Allez l'essayer :)

> _C'est le cache qui fait la magie du site : vous pouvez revenir dans 3 semaines, 1 mois, 1 an, toujours sans connexion, et accéder à tout le contenu. — Maxime Huygue, Directeur du Studio Digital BETC_

**D'accord, c'est cool, dis-moi comment faire alors.**

D'accord, commençons par quelques prérequis :

* Pour utiliser les SWs, vous devez activer le https sur votre site web.
* Vous devez avoir une compréhension décente du fonctionnement des [promesses JavaScript](https://scotch.io/tutorials/javascript-promises-for-dummies).
* Les SWs fonctionnent dans tous les [navigateurs modernes](https://caniuse.com/#feat=serviceworkers) sauf notre ami IE.
* Même si c'est du JavaScript, ils s'exécutent dans le contexte des [web workers](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API). Ce qui signifie : pas de DOM, et s'exécutent en dehors du thread principal.
* Comprendre comment fonctionnent les bases de données.
* Le code de votre service worker doit être dans un fichier JavaScript séparé. Exemple : service-worker.js

### Cycle de vie des service workers

![Image](https://cdn-media-1.freecodecamp.org/images/0*kwQX495DA0fAv3QZ.png)

Pour pouvoir fonctionner, les SWs doivent être enregistrés dans votre application, puis installés. Vous devez vérifier si les SWs sont compatibles avec votre client avant de le faire.

#### **1) Enregistrement**

Si disponible, enregistrez votre fichier SW. Il retournera une promesse, donc vous pouvez gérer les erreurs. Vous pouvez également spécifier une portée d'URLs dans les [options d'enregistrement](https://developer.mozilla.org/en-US/docs/Web/API/ServiceWorkerContainer/register).

#### **2) Installation**

**Les service workers sont basés sur des événements.** Brièvement, vous devez attacher des rappels aux événements, comme vous le feriez avec un [element.addEventListener](https://developer.mozilla.org/fr/docs/Web/API/EventTarget/addEventListener). Le premier événement que vous devez utiliser est l'événement d'installation. C'est un bon moment pour mettre en cache toutes vos ressources vitales comme JavaScript, CSS, HTML, Images… C'est là que l'[Cache API](https://developer.mozilla.org/fr/docs/Web/API/Cache) rejoint la fête !

Ensuite, ouvrez la méthode ou créez un cache lié à un nom souhaité. La promesse retournée doit être enveloppée dans event.waitUntil(), ce qui retardera l'installation du service worker jusqu'à ce que la promesse soit résolue. Sinon, l'événement d'installation échoue et le service worker sera rejeté.

Veuillez être prudent avec la mise en cache : le stockage de votre utilisateur est précieux, alors n'en abusez pas. De plus, soyez prudent : l'événement d'installation ne peut être appelé qu'une seule fois, et vous devrez mettre à jour votre SW pour le modifier.

#### **3) Activation**

Celui-ci est un peu subtil.

Une fois l'installation terminée, le service worker n'est pas encore actif : nous sommes dans l'état installé.

Dans cet état, il attend de prendre le contrôle de la page. Il passe ensuite à la phase suivante du cycle de vie, qui est la phase d'activation.

La phase d'activation est utile lorsque vous mettez à jour un SW. Le cas le plus courant est de vider le cache du SW précédent installé.

Veuillez noter que, une fois installé avec succès, le worker mis à jour attendra jusqu'à ce que le worker existant contrôle zéro clients (les clients se chevauchent pendant un rafraîchissement).

self.skipWaiting() empêche l'attente, ce qui signifie que le service worker s'active dès qu'il a terminé son installation. L'avantage de cette méthode est que vous pouvez recevoir des événements de récupération plus rapidement.

Il n'est pas vraiment important de savoir quand vous appelez skipWaiting(), tant que c'est pendant ou avant l'attente. Il est assez courant de l'appeler dans l'événement d'installation.

**Ouf ! Prenons une pause et résumons ce que nous avons vu :**

* Les service workers sont des morceaux de JavaScript qui permettent des fonctionnalités hors ligne telles que la mise en cache.
* Nous avons exploré le cycle de vie des SW : enregistrement, installation, activation
* Nous avons appris comment implémenter des cas d'utilisation courants tels que : la mise en cache des ressources et le vidage des caches avec l'API Cache.
* Nous avons vu que self.skipWaiting et self.clients.claim nous permettent d'activer les SW plus rapidement afin de capturer les événements plus rapidement.

D'accord, continuons…

#### **4) Récupération**

L'événement de récupération nous permet d'intercepter les requêtes réseau et de stocker les réponses ou de les personnaliser.

L'avantage principal de ce hook est de retourner les ressources mises en cache au lieu de faire un appel de requête. Vous devriez jeter un coup d'œil à l'[API Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) pour gérer vos appels de requête.

Nous ne pouvons pas couvrir toutes les possibilités offertes par les service workers dans un seul article. Cependant, je vous encourage à explorer ce qui est possible : [404 personnalisé](https://gohugohq.com/howto/go-offline-with-service-worker/), [API de synchronisation en arrière-plan pour l'analyse hors ligne](https://developers.google.com/web/updates/2016/07/offline-google-analytics), [modélisation côté ServiceWorker](https://developers.google.com/web/fundamentals/instant-and-offline/offline-cookbook/#serviceworker-side-templating)… l'avenir semble passionnant !

Jusqu'à présent, nous avons vu ce qu'est un service worker, comment il fonctionne à travers son cycle de vie, et les cas d'utilisation les plus courants en jouant avec les API Cache et Fetch. Ces deux API nous offrent une toute nouvelle façon de gérer les **ressources adressables par URL** dans le navigateur. Pour compléter ce guide, voyons comment nous pouvons stocker d'autres types de données, par exemple le [JSON](https://en.wikipedia.org/wiki/JSON) d'un utilisateur de votre base de données.

### Stocker des données personnalisées avec IndexedDB

*Une directive générale pour le stockage des données est que les ressources adressables par URL doivent être stockées avec l'interface [Cache](https://developer.mozilla.org/en-US/docs/Web/API/Cache), et les autres données doivent être stockées avec [IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API). Par exemple, les fichiers HTML, CSS et JS doivent être stockés dans le cache, tandis que les données JSON doivent être stockées dans IndexedDB. Notez que ceci n'est qu'une directive, pas une règle ferme. ([source](https://developers.google.com/web/ilt/pwa/live-data-in-the-service-worker))*

En bref, nous verrons **quand vous ne devriez pas utiliser l'API Cache** mais [IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API/Using_IndexedDB) à la place. Les deux sont asynchrones et accessibles dans les service workers, les web workers et l'[interface window](https://developer.mozilla.org/fr/docs/Web/API/Window). La bonne nouvelle est que [c'est bien supporté](https://caniuse.com/#feat=indexeddb), même dans les versions récentes d'IE.

IndexedDB est une base de données NoSQL. Les données IndexedDB sont stockées sous forme de paires clé-valeur dans des **magasins d'objets** plutôt que dans des tables. Une seule base de données peut contenir n'importe quel nombre de magasins d'objets. Chaque fois qu'une valeur est stockée dans un magasin d'objets, elle est associée à une clé. Cela ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*6ES2yg8KcJaEpi_nAv31yA.png)

Assez classique, n'est-ce pas ? La chose principale à comprendre est le concept de [chemin de clé](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API/Basic_Concepts_Behind_IndexedDB#gloss_keypath). Il indique au navigateur quelle clé utiliser pour extraire les données du magasin d'objets ou de l'index.

Dans cet exemple, nous pouvons voir que notre chemin de clé est la propriété id, et il est défini à la ligne 10. Ensuite, nous retournons tous les éléments de la base de données. C'est un cas d'utilisation très basique, donc si vous voulez en savoir plus sur le fonctionnement d'IndexedDB, je vous conseille de lire cet excellent [article](https://itnext.io/getting-started-with-persistent-offline-storage-with-indexeddb-1af66727246c).

### Conclusion

Profiter du web hors ligne est excellent pour l'expérience utilisateur, et certaines entreprises ont commencé à s'y intéresser. Cela repose principalement sur les service workers, des scripts JavaScript qui s'exécutent en arrière-plan de votre site web.

Nous avons vu comment les utiliser à travers le cycle de vie des service workers et ce que vous pouvez faire en utilisant les API Cache et Fetch. Les possibilités sont presque illimitées, alors soyez créatif et pas trop gourmand en stockage de l'appareil.

Vous pouvez même utiliser des bases de données hors ligne : c'est pour cela qu'IndexedDB est fait. Ces capacités hors ligne font certainement partie de l'avenir du web, donc cela s'intègre bien avec le nouveau type de sites web que Google crée : les Progressive Web Apps.

### Lectures complémentaires :

* Le guide hors ligne : [https://developers.google.com/web/fundamentals/instant-and-offline/offline-cookbook/](https://developers.google.com/web/fundamentals/instant-and-offline/offline-cookbook/)
* PWA et hors ligne : [https://developers.google.com/web/ilt/pwa/lab-offline-quickstart](https://developers.google.com/web/ilt/pwa/lab-offline-quickstart)
* Lab : Mise en cache de fichiers avec Service Worker : [https://developers.google.com/web/ilt/pwa/lab-caching-files-with-service-worker](https://developers.google.com/web/ilt/pwa/lab-caching-files-with-service-worker)
* Le cycle de vie des Service Workers : [https://developers.google.com/web/fundamentals/primers/service-workers/lifecycle](https://developers.google.com/web/fundamentals/primers/service-workers/lifecycle)
* Démystifier le cycle de vie des Service Workers : [https://scotch.io/tutorials/demystifying-the-service-worker-lifecycle](https://scotch.io/tutorials/demystifying-the-service-worker-lifecycle)
* Activer les Service Workers plus rapidement : [https://davidwalsh.name/service-worker-claim](https://davidwalsh.name/service-worker-claim)
* Données en direct dans le Service Worker : [https://developers.google.com/web/ilt/pwa/live-data-in-the-service-worker](https://developers.google.com/web/ilt/pwa/live-data-in-the-service-worker)
* Concepts de base d'IndexedDB : [https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API/Basic_Concepts_Behind_IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API/Basic_Concepts_Behind_IndexedDB)
* Commencer avec le stockage hors ligne persistant avec IndexedDB : [https://itnext.io/getting-started-with-persistent-offline-storage-with-indexeddb-1af66727246c](https://itnext.io/getting-started-with-persistent-offline-storage-with-indexeddb-1af66727246c)