---
title: Comment créer un scraper web simple et personnalisable en utilisant RxJS et
  Node
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-27T02:10:34.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-simple-customizable-web-scraper-using-rxjs-and-node-6858cfe82a39
coverImage: https://cdn-media-1.freecodecamp.org/images/0*zqqImyUXrCGM9nA-.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: RxJS
  slug: rxjs
- name: 'tech '
  slug: tech
- name: web scraping
  slug: web-scraping
seo_title: Comment créer un scraper web simple et personnalisable en utilisant RxJS
  et Node
seo_desc: 'By Jacob Goh

  Introduction

  After getting to know RxJS (thanks to Angular!), I realized that it’s surprisingly
  a good fit for handling web scraping operations.

  I tried it out in a side project and I would like to share my experience with you.
  Hopefully...'
---

Par Jacob Goh

### Introduction

Après avoir découvert RxJS (grâce à Angular !), j'ai réalisé qu'il était surprenamment bien adapté pour gérer les opérations de web scraping.

Je l'ai essayé dans un projet parallèle et je souhaiterais partager mon expérience avec vous. J'espère que cela vous ouvrira les yeux sur la manière dont la programmation réactive peut simplifier votre vie.

Les codes peuvent être trouvés sur [https://github.com/jacobgoh101/web-scraping-with-rxjs](https://github.com/jacobgoh101/web-scraping-with-rxjs)

### Prérequis

* Node
* RxJS et une compréhension intermédiaire de celui-ci
* [cheerio](https://www.npmjs.com/package/cheerio) : il permet d'utiliser une syntaxe similaire à jQuery pour extraire des informations du code HTML
* [request-promise-native](https://www.npmjs.com/package/request-promise-native) : pour envoyer des requêtes HTTP

### Objectif hypothétique

Tout le monde aime un bon film comique.

Faisons de notre objectif de scraper une liste de bons films comiques depuis IMDB.

Il y a seulement 3 exigences que les données cibles doivent remplir :

* il s'agit d'un film (pas de séries TV, de clips musicaux, etc.)
* il s'agit d'une comédie
* il a une note de 7 ou plus

### Commencer

Définissons notre URL de base et définissons un BehaviorSubject `allUrl$` qui utilise l'URL de base comme valeur initiale.

(Un BehaviorSubject est un [subject](https://www.youtube.com/watch?v=rdK92pf3abs) avec une valeur initiale.)

```
const { BehaviorSubject } = require('rxjs');
const baseUrl = `https://imdb.com`;
const allUrl$ = new BehaviorSubject(baseUrl);
```

`allUrl$` va être le point de départ de toutes les opérations de crawling. Chaque URL sera passée dans `allUrl$` et sera traitée plus tard.

#### Assurer que nous scrapons chaque URL une seule fois

Avec l'aide des opérateurs [distinct](https://rxjs-dev.firebaseapp.com/api/operators/distinct) et [normalize-url](https://www.npmjs.com/package/normalize-url), nous pouvons facilement nous assurer de ne jamais scraper la même URL deux fois.

```
// ...
const { map, distinct, filter } = require('rxjs/operators');
const normalizeUrl = require('normalize-url');
```

```
// ...
```

```
const uniqueUrl$ = allUrl$.pipe(
  // ne crawler que les URLs IMDB
  filter(url => url.includes(baseUrl)),
  // normaliser l'URL pour la comparaison
  map(url => normalizeUrl(url, { removeQueryParameters: ['ref', 'ref_'] })),
  // distinct est un opérateur RxJS qui filtre les valeurs dupliquées
  distinct());
```

#### Il est temps de commencer à scraper

Nous allons faire une requête à chaque URL unique et mapper le contenu de chaque URL dans un autre observable.

Pour cela, nous utilisons [mergeMap](https://www.learnrxjs.io/operators/transformation/mergemap.html) pour mapper le résultat de la requête à un autre observable.

```
const { BehaviorSubject, from } = require('rxjs');
const { map, distinct, filter, mergeMap } = require('rxjs/operators');
const rp = require('request-promise-native');
const cheerio = require('cheerio');
```

```
//...
const urlAndDOM$ = uniqueUrl$.pipe(
  mergeMap(url => {
    return from(rp(url)).pipe(
      // obtenir la fonction cheerio $
      map(html => cheerio.load(html)),
      // ajouter l'URL au résultat. Elle sera utilisée plus tard pour le crawling
      map($ => ({
        $,
        url
      }))
    );
  }));
```

`urlAndDOM$` émettra un objet composé de 2 propriétés, qui sont `$` et `url`. `$` est une fonction Cheerio où vous pouvez utiliser quelque chose comme `$('div').text()` pour extraire des informations du code HTML brut.

#### Crawler toutes les URLs

```
const { resolve } = require('url');
//...
```

```
// obtenir toutes les URLs suivantes crawlables
urlAndDOM$.subscribe(({ url, $ }) => {
  $('a').each(function(i, elem) {
    const href = $(this).attr('href');
    if (!href) return;
```

```
// construire l'URL absolue
    const absoluteUrl = resolve(url, href);
    allUrl$.next(absoluteUrl);
  });
});
```

Dans le code ci-dessus, nous scrapons tous les liens à l'intérieur de la page et les envoyons à `allUrl$` pour qu'ils soient crawlés plus tard.

#### Scraper et sauvegarder les films que nous voulons !

```
const fs = require('fs');
//...
```

```
const isMovie = $ => $(`[property='og:type']`).attr('content') === 'video.movie';
const isComedy = $ => $(`.title_wrapper .subtext`)
  .text()
  .includes('Comedy');
const isHighlyRated = $ => +$(`[itemprop="ratingValue"]`).text() > 7;
```

```
urlAndDOM$
  .pipe(
    filter(({ $ }) => isMovie($)),
    filter(({ $ }) => isComedy($)),
    filter(({ $ }) => isHighlyRated($))
  )
  .subscribe(({ url, $ }) => {
    // ajouter les données que nous voulons à un fichier nommé "comedy.txt"
    fs.appendFile('comedy.txt', `${url}, ${$('title').text()}\n`);
  });
```

### Oui, nous venons de créer un scraper web

En environ 70 lignes de code, nous avons créé un scraper web qui

* crawle automatiquement les URLs sans doublons inutiles
* scrape et sauvegarde automatiquement les informations que nous voulons dans un fichier texte

Vous pouvez voir le code jusqu'à ce point dans [https://github.com/jacobgoh101/web-scraping-with-rxjs/blob/86ff05e893dec5f1b39647350cb0f74efe258c86/index.js](https://github.com/jacobgoh101/web-scraping-with-rxjs/blob/86ff05e893dec5f1b39647350cb0f74efe258c86/index.js)

Si vous avez déjà essayé d'écrire un scraper web à partir de zéro, vous devriez maintenant voir à quel point il est élégant d'en écrire un avec RxJS.

### Mais nous n'avons pas encore terminé...

Dans un monde idéal, le code ci-dessus devrait fonctionner pour toujours sans aucun problème.

Mais en réalité, des erreurs stupides se produisent.

### Gestion des erreurs

#### Limiter le nombre de connexions concurrentes actives

Si nous envoyons trop de requêtes à un serveur en peu de temps, il est probable que notre IP soit temporairement bloquée pour faire d'autres requêtes, surtout pour un site établi comme IMDB.

C'est aussi considéré comme **impoli/non éthique** d'envoyer autant de requêtes à la fois car cela créerait une charge plus lourde sur le serveur et, dans certains cas, **faire planter le serveur**.

[mergeMap](https://www.learnrxjs.io/operators/transformation/mergemap.html) a une fonctionnalité intégrée pour contrôler la concurrence. Il suffit d'ajouter un nombre au 3ème argument de la fonction et il limitera automatiquement la connexion concurrente active. Élégant !

```
const maxConcurrentReq = 10;
//...
const urlAndDOM$ = uniqueUrl$.pipe(
  mergeMap(
    //...
    null,
    maxConcurrentReq
  ));
```

Différence de code : [https://github.com/jacobgoh101/web-scraping-with-rxjs/commit/6aaed6dae230d2dde1493f1b6d78282ce2e8f316](https://github.com/jacobgoh101/web-scraping-with-rxjs/commit/6aaed6dae230d2dde1493f1b6d78282ce2e8f316)

#### Gérer et relancer les requêtes échouées

Les requêtes peuvent échouer aléatoirement en raison de liens morts ou de limitations de débit côté serveur. Cela est crucial pour les scrapers web.

Nous pouvons utiliser les opérateurs [catchError](https://www.learnrxjs.io/operators/error_handling/catch.html), [retry](https://www.learnrxjs.io/operators/error_handling/retry.html) pour gérer cela.

```
const { BehaviorSubject, from, of } = require('rxjs');
const {  // ...  retry,  catchError} = require('rxjs/operators');
//...
```

```
const maxRetries = 5;
// ...
```

```
const urlAndDOM$ = uniqueUrl$.pipe(
  mergeMap(
    url => {
      return from(rp(url)).pipe(
        retry(maxRetries),
        catchError(error => {
          const { uri } = error.options;
          console.log(`Error requesting ${uri} after ${maxRetries} retries.`);
          // retourner null en cas d'erreur
          return of(null);
        }),
        // filtrer les erreurs
        filter(v => v),
        // ...
      );
    },
```

Différence de code : [https://github.com/jacobgoh101/web-scraping-with-rxjs/commit/3098b48ca91a59aa5171bc2aa9c17801e769fcbb](https://github.com/jacobgoh101/web-scraping-with-rxjs/commit/3098b48ca91a59aa5171bc2aa9c17801e769fcbb)

#### Amélioration de la relance des requêtes échouées

En utilisant l'opérateur retry, la relance se ferait immédiatement après l'échec de la requête. Ce n'est pas idéal.

Il est préférable de relancer après une certaine période de délai.

Nous pouvons utiliser la stratégie `genericRetryStrategy` suggérée dans [learnrxjs](https://www.learnrxjs.io/operators/error_handling/retrywhen.html) pour y parvenir.

Différence de code : [https://github.com/jacobgoh101/web-scraping-with-rxjs/commit/e194f4ff128a573241055ffc0d1969d54ca8c270](https://github.com/jacobgoh101/web-scraping-with-rxjs/commit/e194f4ff128a573241055ffc0d1969d54ca8c270)

### Conclusion

Pour résumer, dans cet article, nous avons discuté :

* comment crawler une page web en utilisant Cheerio
* comment éviter les doublons de crawling en utilisant les opérateurs RxJS comme filter, distinct
* comment utiliser mergeMap pour créer un observable de la réponse de la requête
* comment limiter la concurrence dans mergeMap
* comment gérer les erreurs
* comment gérer les relances

J'espère que cela vous a été utile et a approfondi votre compréhension de RxJs et du web scraping.

_Publié à l'origine sur [dev.to](https://dev.to/jacobgoh101/simple--customizable-web-scraper-using-rxjs-and-node-1on7)._