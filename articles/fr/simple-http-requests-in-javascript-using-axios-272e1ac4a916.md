---
title: Requêtes HTTP simples en JavaScript avec Axios
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2018-04-11T11:27:52.000Z'
originalURL: https://freecodecamp.org/news/simple-http-requests-in-javascript-using-axios-272e1ac4a916
coverImage: https://cdn-media-1.freecodecamp.org/images/1*AIVLX97Nn6e3NfKOkvWTEQ.png
tags:
- name: Browsers
  slug: browsers
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Requêtes HTTP simples en JavaScript avec Axios
seo_desc: 'Interested in learning JavaScript? Get my ebook at jshandbook.com


  Introduction

  Axios is a very popular JavaScript library you can use to perform HTTP requests.
  It works in both Browser and Node.js platforms.

  Is supports all modern browsers, includin...'
---

> Intéressé par l'apprentissage de JavaScript ? Obtenez mon ebook sur [jshandbook.com](https://jshandbook.com/)

### Introduction

Axios est une bibliothèque JavaScript très populaire que vous pouvez utiliser pour effectuer des requêtes HTTP. Elle fonctionne à la fois sur les plateformes navigateur et [Node.js](https://flaviocopes.com/nodejs/).

Elle supporte tous les navigateurs modernes, y compris IE8 et versions supérieures.

Elle est basée sur les promesses, ce qui nous permet d'écrire du code async/await pour effectuer des requêtes [XHR](https://flaviocopes.com/xhr/) très facilement.

L'utilisation d'Axios présente plusieurs avantages par rapport à l'API native [Fetch](https://flaviocopes.com/fetch-api/) :

* supporte les anciens navigateurs (Fetch nécessite un polyfill)
* offre un moyen d'annuler une requête
* offre un moyen de définir un délai d'expiration pour la réponse
* dispose d'une protection CSRF intégrée
* supporte la progression du téléchargement
* effectue une transformation automatique des données JSON
* fonctionne dans Node.js

### Installation

Axios peut être installé en utilisant [npm](https://flaviocopes.com/npm/) :

```
npm install axios
```

ou [yarn](https://flaviocopes.com/yarn/) :

```
yarn add axios
```

ou simplement l'inclure dans votre page en utilisant unpkg.com :

```
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
```

### L'API Axios

Vous pouvez démarrer une requête HTTP à partir de l'objet `axios` :

```
axios({  url: 'https://dog.ceo/api/breeds/list/all',  method: 'get',  data: {    foo: 'bar'  }})
```

mais pour plus de commodité, vous utiliserez généralement

* `axios.get()`
* `axios.post()`

(comme dans jQuery, vous utiliseriez `$.get()` et `$.post()` au lieu de `$.ajax()`)

Axios offre des méthodes pour tous les verbes HTTP, qui sont moins populaires mais toujours utilisés :

* `axios.delete()`
* `axios.put()`
* `axios.patch()`
* `axios.options()`

Il offre également une méthode pour obtenir les en-têtes HTTP d'une requête, en ignorant le corps.

### Requêtes GET

Une façon pratique d'utiliser Axios est d'utiliser la syntaxe moderne (ES2017) async/await.

Cet exemple Node.js interroge l'[API Dog](https://dog.ceo/) pour récupérer une liste de toutes les races de chiens, en utilisant `axios.get()`, et les compte :

```
const axios = require('axios')const getBreeds = async () => {  try {    return await axios.get('https://dog.ceo/api/breeds/list/all')  } catch (error) {    console.error(error)  }}const countBreeds = async () => {  const breeds = await getBreeds()  if (breeds.data.message) {    console.log(`Got ${Object.entries(breeds.data.message).length} breeds`)  }}countBreeds()
```

Si vous ne souhaitez pas utiliser async/await, vous pouvez utiliser la syntaxe des [Promesses](https://flaviocopes.com/javascript-promises/) :

```
const axios = require('axios')const getBreeds = () => {  try {    return axios.get('https://dog.ceo/api/breeds/list/all')  } catch (error) {    console.error(error)  }}const countBreeds = async () => {  const breeds = getBreeds()    .then(response => {      if (response.data.message) {        console.log(          `Got ${Object.entries(response.data.message).length} breeds`        )      }    })    .catch(error => {      console.log(error)    })}countBreeds()
```

### Ajouter des paramètres aux requêtes GET

Une réponse GET peut contenir des paramètres dans l'URL, comme ceci : `[https://site.com/?foo=bar](https://site.com/?foo=bar.)`[.](https://site.com/?foo=bar.)

Avec Axios, vous pouvez le faire en utilisant simplement cette URL :

```
axios.get('https://site.com/?foo=bar')
```

ou vous pouvez utiliser une propriété `params` dans les options :

```
axios.get('https://site.com/', {  params: {    foo: 'bar'  }})
```

### Requêtes POST

Effectuer une requête POST est similaire à une requête GET, mais au lieu de `axios.get`, vous utilisez `axios.post` :

```
axios.post('https://site.com/')
```

Un objet contenant les paramètres POST est le deuxième argument :

```
axios.post('https://site.com/', { foo: 'bar' })
```

> Intéressé par l'apprentissage de JavaScript ? Obtenez mon ebook sur [jshandbook.com](https://jshandbook.com/)