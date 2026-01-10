---
title: Angular - Comment récupérer le nom de fichier à partir d'une réponse Blob
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-02T02:16:00.000Z'
originalURL: https://freecodecamp.org/news/angular-how-to-retrieve-filename-from-a-blob-response
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9aa3740569d1a4ca26cc.jpg
tags:
- name: Angular
  slug: angular
- name: how-to
  slug: how-to
- name: toothbrush
  slug: toothbrush
seo_title: Angular - Comment récupérer le nom de fichier à partir d'une réponse Blob
seo_desc: "If you're new to Angular, you might be wondering how to retrieve a filename\
  \ from an API response.\nImagine you have a method that makes a POST request to\
  \ a remote API and receives a Blob containing a file:\npublic downloadExcel(data):\
  \ void {\n  const ur..."
---

Si vous êtes nouveau dans Angular, vous vous demandez peut-être comment récupérer un nom de fichier à partir d'une réponse d'API.

Imaginez que vous avez une méthode qui effectue une requête POST vers une API distante et reçoit un `Blob` contenant un fichier :

```ts
public downloadExcel(data): void {
  const url: string = '[api endpoint here ]';
  this.http.post(url, data.body, { responseType: 'blob' })
    .subscribe((response: Blob) => saveAs(response, data.fileName + '.xlsx'));
}
```

Selon MDN, les objets `Blob` ne contiennent qu'une taille et un type, vous aurez donc besoin d'une autre méthode pour obtenir le nom de fichier réel.

Mais comme `data` est passé en paramètre à votre fonction, il est possible qu'il inclue également la charge utile du serveur. Affichez-le dans la console et voyez quelles informations sont incluses.

## Lire les en-têtes de réponse

Une autre option possible est de lire les en-têtes de la réponse HTTP eux-mêmes.

Puisque vous récupérez des données à partir d'une API, il est probable que vous utilisiez `httpClient` pour faire la requête. Souvent, les réponses des API incluent des informations utiles dans l'en-tête.

Une chose à examiner est l'entrée `X-Token`. Mais gardez à l'esprit que tous les en-têtes ne peuvent pas être accessibles côté client, donc `access-control-expose-headers` devra être défini côté serveur.

Si `X-Token` est exposé, vous pouvez utiliser la méthode HTTP `{ observe: 'response' }` pour obtenir la réponse complète, puis afficher `X-Token` dans la console :

```ts
http
  .get<any>('url', { observe: 'response' })
  .subscribe(resp => {
    console.log(resp.headers.get('X-Token'));
  });
```

Il est également utile de lire la documentation sur les [en-têtes de réponse](https://developer.mozilla.org/en-US/docs/Web/API/Response/headers) en général.