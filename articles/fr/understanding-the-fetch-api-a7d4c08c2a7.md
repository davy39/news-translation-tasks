---
title: Comprendre l'API Fetch
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2018-03-15T02:58:01.000Z'
originalURL: https://freecodecamp.org/news/understanding-the-fetch-api-a7d4c08c2a7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2uRk3VpmBwXvnuRtfBReSQ.png
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
seo_title: Comprendre l'API Fetch
seo_desc: 'Interested in learning JavaScript? Get my ebook at jshandbook.com


  Since IE5 was released in 1998, we’ve had the option to make asynchronous network
  calls in the browser using XMLHttpRequest (XHR).

  Quite a few years after this, Gmail and other rich a...'
---

> Intéressé par l'apprentissage de JavaScript ? Obtenez mon ebook sur [jshandbook.com](https://jshandbook.com/)

Depuis la sortie d'IE5 en 1998, nous avons eu la possibilité de faire des appels réseau asynchrones dans le navigateur en utilisant [XMLHttpRequest (XHR)](https://flaviocopes.com/xhr/).

Quelques années après cela, Gmail et d'autres applications riches en ont fait un usage intensif, et ont rendu l'approche si populaire qu'elle devait avoir un nom : **AJAX**.

Travailler directement avec XMLHttpRequest a toujours été pénible, et il était presque toujours abstrait par une bibliothèque. En particulier, jQuery a ses propres fonctions d'assistance construites autour de celui-ci :

* `jQuery.ajax()`
* `jQuery.get()`
* `jQuery.post()`

et ainsi de suite.

Ils ont eu un impact énorme sur la simplification des appels asynchrones. En particulier, ils se sont concentrés sur les anciens navigateurs pour s'assurer que tout fonctionnait encore.

L'**API Fetch** a été standardisée comme une approche moderne des requêtes réseau asynchrones et utilise les [**Promesses**](https://flaviocopes.com/javascript-promises/) comme bloc de construction.

Fetch, au moment de l'écriture (septembre 2017), a un bon support parmi les principaux navigateurs, à l'exception d'IE.

![Image](https://cdn-media-1.freecodecamp.org/images/ZTZudnYkwsXj7jUrXoEcNRjAyqKBjqoLalmx)

Le [polyfill](https://github.com/github/fetch) publié par GitHub nous permet d'utiliser `fetch` sur n'importe quel navigateur.

### Utilisation de Fetch

Commencer à utiliser Fetch pour les requêtes `GET` est très simple :

```
fetch('/file.json')
```

Vous l'utilisez déjà : fetch va faire une requête HTTP pour obtenir la ressource `file.json` sur le même domaine.

Comme vous pouvez le voir, la fonction `fetch` est disponible dans la portée globale `window`.

Maintenant, rendons cela un peu plus utile, voyons ce que contient le fichier :

```
fetch('./file.json') .then(response => response.json()).then(data => console.log(data))
```

Appeler `fetch()` retourne une promesse. Nous pouvons attendre que la promesse se résolve en passant un gestionnaire avec la méthode `then()` de la promesse.

Ce gestionnaire reçoit la valeur de retour de la promesse `fetch`, un objet Response.

Nous verrons cet objet plus en détail dans la section suivante.

### Capture des erreurs

Puisque `fetch()` retourne une promesse, nous pouvons utiliser la méthode `catch` de la promesse pour intercepter toute erreur survenant pendant l'exécution de la requête, et le traitement est fait dans les rappels `then` :

```
fetch('./file.json').then(response => {  //...}.catch(err => console.error(err))
```

### Objet Response

L'objet Response retourné par un appel `fetch()` contient toutes les informations sur la requête et la réponse de la requête réseau.

Accéder à la propriété `headers` sur l'objet `response` vous donne la possibilité de consulter les en-têtes HTTP retournés par la requête :

```
fetch('./file.json').then(response => {  console.log(response.headers.get('Content-Type'))  console.log(response.headers.get('Date'))})
```

![Image](https://cdn-media-1.freecodecamp.org/images/OJOg4dW3f2GWea2bcfnwa4MvECpCZ7WbwHxo)

#### status

Cette propriété est un nombre entier représentant le statut de la réponse HTTP.

* `101`, `204`, `205`, ou `304` est un statut `body null`
* `200` à `299`, inclus, est un statut `OK` (succès)
* `301`, `302`, `303`, `307`, ou `308` est une `redirection`

```
fetch('./file.json') .then((response) => {   console.log(response.status) })
```

#### statusText

`statusText` est une propriété représentant le message de statut de la réponse. Si la requête est réussie, le statut est `OK`.

```
fetch('./file.json') .then(response => console.log(response.statusText))
```

#### url

`url` représente l'URL complète de la propriété que nous avons récupérée.

```
fetch('./file.json') .then(response => console.log(response.url))
```

### Contenu du corps

Une réponse a un corps, accessible en utilisant les méthodes `text()` ou `json()`, qui retournent une promesse.

```
fetch('./file.json').then(response => response.text()).then(body => console.log(body))
```

```
fetch('./file.json').then(response => response.json()).then(body => console.log(body))
```

![Image](https://cdn-media-1.freecodecamp.org/images/bUd5fnaOF3fWarIFA7kr5j2cU-Y9LLvnE35F)

La même chose peut être écrite en utilisant les [fonctions asynchrones](https://flaviocopes.com/async-await/) [ES2017](https://flaviocopes.com/ecmascript/) :

```
(async () => {  const response = await fetch('./file.json')  const data = await response.json()  console.log(data)})()
```

### Objet Request

L'objet Request représente une requête de ressource, et il est généralement créé en utilisant l'API `new Request()`.

Exemple :

```
const req = new Request('/api/todos')
```

L'objet Request offre plusieurs propriétés en lecture seule pour inspecter les détails de la requête de ressource, y compris

* `method` : la méthode de la requête (GET, POST, etc.)
* `url` : l'URL de la requête.
* `headers` : l'objet Headers associé de la requête
* `referrer` : le référent de la requête
* `cache` : le mode cache de la requête (par exemple, default, reload, no-cache).

Et expose plusieurs méthodes incluant `json()`, `text()` et `formData()` pour traiter le corps de la requête.

L'API complète peut être trouvée [ici](https://developer.mozilla.org/docs/Web/API/Request).

Pouvoir définir l'en-tête de la requête HTTP est essentiel, et `fetch` nous donne la possibilité de le faire en utilisant l'objet Headers :

```
const headers = new Headers()headers.append('Content-Type', 'application/json')
```

ou, plus simplement :

```
const headers = new Headers({   'Content-Type': 'application/json' })
```

Pour attacher les en-têtes à la requête, nous utilisons l'objet Request, et le passons à `fetch()` au lieu de simplement passer l'URL.

Au lieu de :

```
fetch('./file.json')
```

nous faisons

```
const request = new Request('./file.json', {   headers: new Headers({ 'Content-Type': 'application/json' }) }) 
```

```
fetch(request)
```

L'objet Headers n'est pas limité à la définition de valeurs, mais nous pouvons également l'interroger :

```
headers.has('Content-Type') headers.get('Content-Type')
```

et nous pouvons supprimer un en-tête qui a été précédemment défini :

```
headers.delete('X-My-Custom-Header')
```

### Requêtes POST

Fetch permet également d'utiliser toute autre méthode HTTP dans votre requête : POST, PUT, DELETE ou OPTIONS.

Spécifiez la méthode dans la propriété method de la requête, et passez des paramètres supplémentaires dans l'en-tête et dans le corps de la requête :

Exemple d'une requête POST :

```
const options = {   method: 'post',   headers: {     "Content-type": "application/x-www-form-urlencoded; charset=UTF-8" },     body: 'foo=bar&test=1' } 
```

```
fetch(url, options) .catch((err) => {   console.error('Request failed', err) })
```

### **Comment annuler une requête fetch**

Pendant quelques années après l'introduction de `fetch`, il n'y avait aucun moyen d'annuler une requête une fois ouverte.

Maintenant, nous pouvons le faire, grâce à l'introduction de `AbortController` et `AbortSignal`, une API générique pour notifier les événements **abort**

Vous intégrez cette API en passant un signal comme paramètre de fetch :

```
const controller = new AbortController()const signal = controller.signalfetch('./file.json', { signal })
```

Vous pouvez définir un délai qui déclenche un événement d'annulation 5 secondes après le début de la requête fetch, pour l'annuler :

```
setTimeout(() => controller.abort(), 5 * 1000)
```

De manière pratique, si le fetch a déjà retourné, l'appel à `abort()` ne causera aucune erreur.

Lorsqu'un signal d'annulation se produit, fetch rejettera la promesse avec une `DOMException` nommée `AbortError` :

```
fetch('./file.json', { signal }).then(response => response.text()).then(text => console.log(text)).catch(err => {  if (err.name === 'AbortError') {    console.error('Fetch aborted')  } else {    console.error('Another error', err)  }})
```

> Intéressé par l'apprentissage de JavaScript ? Obtenez mon ebook sur [jshandbook.com](https://jshandbook.com/)