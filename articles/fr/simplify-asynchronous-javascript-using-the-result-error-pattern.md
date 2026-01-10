---
title: Comment simplifier le JavaScript asynchrone en utilisant le motif Résultat-Erreur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-18T22:08:11.000Z'
originalURL: https://freecodecamp.org/news/simplify-asynchronous-javascript-using-the-result-error-pattern
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/locomotive-gfe169d971_1920-1.jpg
tags:
- name: asynchronous
  slug: asynchronous
- name: asynchronous programming
  slug: asynchronous-programming
- name: JavaScript
  slug: javascript
seo_title: Comment simplifier le JavaScript asynchrone en utilisant le motif Résultat-Erreur
seo_desc: "By Ken Snyder\nOver the last 18 years of programming, I've had to deal\
  \ with asynchronous behavior in virtually every project. \nSince the adoption of\
  \ async-await in JavaScript, we've learned that async-await makes a lot of code\
  \ more pleasant and easier..."
---

Par Ken Snyder

Au cours des 18 dernières années de programmation, j'ai dû gérer le comportement asynchrone dans pratiquement tous les projets. 

Depuis l'adoption de async-await en JavaScript, nous avons appris que async-await rend beaucoup de code plus agréable et plus facile à comprendre.

Récemment, j'ai remarqué que lorsque je travaille avec une ressource qui doit se connecter et se déconnecter de manière asynchrone, j'en viens à écrire du code comme ceci :

```js
// PAS MON MOTIF PRÉFÉRÉ
router.get('/users/:id', async (req, res) => {
  const client = new Client();
  let user;
  try {
    await client.connect();
    user = await client.find('users').where('id', req.path.id);
  } catch(error) {
    res.status(500);
    user = { error };
  } finally {
    await client.close();
  }
  res.json(user);
});
```

Cela devient verbeux car nous devons utiliser try/catch pour gérer les erreurs.

Des exemples de telles ressources incluent les bases de données, ElasticSearch, les lignes de commande et ssh.

Dans ces cas d'utilisation, j'ai adopté un motif de code que j'appelle le motif Résultat-Erreur.

Considérez la réécriture du code ci-dessus comme ceci :

```js
// JE PRÉFÈRE CE MOTIF
router.get('/users/:id', async (req, res) => {
  const { result: user, error } = await withDbClient(client => {
    return client.find('users').where('id', req.path.id);
  });
  if (error) {
    res.status(500);
  }
  res.json({ user, error });
});

```

Remarquez quelques points :

1. Le client de base de données est créé pour nous et notre callback peut simplement l'utiliser.
2. Au lieu de capturer les erreurs dans un bloc try-catch, nous nous reposons sur `withDbClient` pour retourner les erreurs.
3. Le résultat est toujours appelé `result` car notre callback peut retourner n'importe quel type de données.
4. Nous n'avons pas à fermer la ressource.

Alors, que fait `withDbClient` ?

1. Il gère la création de la ressource, la connexion et la fermeture.
2. Il gère try, catch et finally.
3. Il garantit qu'il n'y aura pas d'exceptions non capturées lancées depuis `withDbClient`.
4. Il garantit que toute exception lancée dans le gestionnaire est également capturée à l'intérieur de `withDbClient`.
5. Il garantit que `{ result, error }` sera toujours retourné.

Voici un exemple d'implémentation :

```js
// EXEMPLE D'IMPLÉMENTATION
async function withDbClient(handler) {
  const client = new DbClient();
  let result = null;
  let error = null;
  try {
    await client.connect();
    result = await handler(client);
  } catch (e) {
    error = e;
  } finally {
    await client.close();
  }
  return { result, error };
}

```

## Un pas plus loin

![Image](https://www.freecodecamp.org/news/content/images/2022/01/pexels-tom-fisk-1595104.jpg)
_Photo par [Tom Fisk](https://www.pexels.com/@tomfisk) de Pexels_

Et pour une ressource qui n'a pas besoin d'être fermée ? Eh bien, le motif Résultat-Erreur peut toujours être agréable !

Considérez l'utilisation suivante de `fetch` :

```js
// C'EST COURT ET AGRÉABLE
const { data, error, response } = await fetchJson('/users/123');

```

Son implémentation pourrait être la suivante :

```js
// EXEMPLE D'IMPLÉMENTATION
async function fetchJson(...args) {
  let data = null;
  let error = null;
  let response = null;
  try {
    const response = await fetch(...args);
    if (response.ok) {
      try {
        data = await response.json();
      } catch (e) {
        // pas du json
      }
    } else {
      // notez que statusText est toujours "" dans HTTP2
      error = `${response.status} ${response.statusText}`;
    }
  } catch(e) {
    error = e;  
  }
  return { data, error, response };
}

```

## Utilisation de haut niveau

![Image](https://www.freecodecamp.org/news/content/images/2022/01/aerial-g3ccde9887_1920.jpg)
_Photo par [16018388](https://pixabay.com/users/16018388-16018388/) de Pixabay_

Nous n'avons pas à nous arrêter à une utilisation de bas niveau. Qu'en est-il des autres fonctions qui peuvent se terminer par un résultat ou une erreur ?

Récemment, j'ai écrit une application avec beaucoup d'interactions ElasticSearch. J'ai décidé d'utiliser également le motif Résultat-Erreur sur des fonctions de haut niveau.

Par exemple, la recherche de posts produit un tableau de documents ElasticSearch et retourne le résultat et l'erreur comme ceci :

```js
const { result, error, details } = await findPosts(query);
```

Si vous avez travaillé avec ElasticSearch, vous savez que les réponses sont verbeuses et que les données sont imbriquées à plusieurs niveaux dans la réponse. Ici, `result` est un objet contenant :

1. `records` – Un tableau de documents
2. `total` – Le nombre total de documents si une limite n'a pas été appliquée
3. `aggregations` – Informations de recherche facettée d'ElasticSearch

Comme vous pouvez le deviner, `error` peut être un message d'erreur et `details` est la réponse complète d'ElasticSearch au cas où vous auriez besoin de choses comme les métadonnées d'erreur, les surlignages ou le temps de requête.

Mon implémentation pour interroger ElasticSearch avec un objet de requête ressemble à ceci :

```js
// Récupérer depuis le nom d'index donné avec la requête donnée
async function query(index, query) {
  // Notre motif Résultat-Erreur au niveau bas  
  const { result, error } = await withEsClient(client => {
    return client.search({
      index,
      body: query.getQuery(),
    });
  });
  // Retourner un objet similaire également avec résultat-erreur
  return {
    result: formatRecords(result),
    error,
    details: result || error?.meta,
  };
}
    
// Extraire les enregistrements des réponses 
function formatRecords(result) {
  // Remarquez à quel point ElasticSearch enterre les résultats ?
  if (result?.body?.hits?.hits) {
    const records = [];
    for (const hit of result.body.hits.hits) {
      records.push(hit._source);
    }
    return {
      records,
      total: result.body.hits.total?.value || 0,
      aggregations: result.aggregations,
    };
  } else {
    return { records: [], total: null, aggregations: null };
  }
}    
```

Et ensuite, la fonction `findPosts` devient quelque chose de simple comme ceci :

```js
function findPosts(query) {
  return query('posts', query);
}
```

## Résumé

Voici les aspects clés d'une fonction qui implémente le motif Résultat-Erreur :

1. Ne jamais lancer d'exceptions.
2. Toujours retourner un objet avec les résultats et l'erreur, où l'un peut être null.
3. Cacher toute création ou nettoyage de ressource asynchrone.

Et voici les avantages correspondants de l'appel de fonctions qui implémentent le motif Résultat-Erreur :

1. Vous n'avez pas besoin d'utiliser des blocs try-catch.
2. La gestion des cas d'erreur est aussi simple que `if (error)`.
3. Vous n'avez pas besoin de vous soucier des opérations de configuration ou de nettoyage.

Ne me croyez pas sur parole, essayez par vous-même !