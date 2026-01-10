---
title: Comment utiliser Fetch pour faire des appels AJAX en JavaScript
subtitle: ''
author: Shruti Kapoor
co_authors: []
series: null
date: '2020-06-26T17:43:31.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-fetch-api
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a08740569d1a4ca231d.jpg
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: beginner
  slug: beginner
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
seo_title: Comment utiliser Fetch pour faire des appels AJAX en JavaScript
seo_desc: 'I will be sharing bite sized learnings about JavaScript regularly in this
  series. We''ll cover JS fundamentals, browsers, DOM, system design, domain architecture
  and frameworks.

  Fetch is an interface for making an AJAX request in JavaScript. It is imp...'
---

Je vais partager des apprentissages concis sur JavaScript régulièrement dans cette série. Nous aborderons les fondamentaux de JS, les navigateurs, le DOM, la conception système, l'architecture de domaine et les frameworks.


Fetch est une interface pour faire une requête AJAX en JavaScript. Elle est largement implémentée par les navigateurs modernes et est utilisée pour appeler une API.


````javascript
const promise = fetch(url, [options])

````

Appeler fetch retourne une promesse, avec un objet Response. La promesse est rejetée s'il y a une erreur réseau, et elle est résolue s'il n'y a pas de problème de connexion au serveur et que le serveur a répondu avec un code de statut. Ce code de statut peut être 200, 400 ou 500.

Un exemple de requête FETCH -
```javascript

fetch(url)
  .then(response => response.json())
  .catch(err => console.log(err))

```

La requête est envoyée en GET par défaut. Pour envoyer un POST / PATCH / DELETE / PUT, vous pouvez utiliser la propriété method dans le paramètre `options`. Voici quelques autres valeurs possibles pour `options` :

- `method` : comme GET, POST, PATCH
- `headers` : objet Headers
- `mode` : comme `cors`, `no-cors`, `same-origin`
- `cache` : mode de cache pour la requête
- `credentials`
- `body`

[Consultez la liste complète des options disponibles ici]('https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/fetch')


Exemple d'utilisation :
Cet exemple démontre l'utilisation de fetch pour appeler une API et obtenir une liste de dépôts git.
``` javascript
const url = 'https://api.github.com/users/shrutikapoor08/repos';

fetch(url)
  .then(response => response.json())
  .then(repos => {
    const reposList = repos.map(repo => repo.name);
    console.log(reposList);
  })
.catch(err => console.log(err))

```


Pour envoyer une requête POST, voici comment le paramètre method peut être utilisé avec la syntaxe async / await.

```javascript
const params = {
  id: 123
}

const response = await fetch('url', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(params)
});

const data = await response.json();
```

---
### Intéressé par plus de JSBytes ? [Inscrivez-vous à la newsletter](https://tinyletter.com/shrutikapoor)