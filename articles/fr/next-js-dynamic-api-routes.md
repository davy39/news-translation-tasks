---
title: Comment créer des routes API dynamiques dans Next.js
subtitle: ''
author: Musab Habeeb
co_authors: []
series: null
date: '2023-11-14T18:30:04.000Z'
originalURL: https://freecodecamp.org/news/next-js-dynamic-api-routes
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/Next.js-Dynamic-API-Routes.png
tags:
- name: api
  slug: api
- name: Next.js
  slug: nextjs
- name: React
  slug: react
seo_title: Comment créer des routes API dynamiques dans Next.js
seo_desc: 'Next.js is a React-based framework that enables developers to create full-stack
  web applications by extending the latest React features.

  Next helps you add additional features and optimizations to your React apps like
  static site generation (SSG), se...'
---

Next.js est un framework basé sur React qui permet aux développeurs de créer des applications web full-stack en étendant les dernières fonctionnalités de React.

Next vous aide à ajouter des fonctionnalités et optimisations supplémentaires à vos applications React comme la génération de site statique (SSG), le rendu côté serveur (SSR), le fractionnement et le bundling automatique du code, et les routes API dynamiques.

Dans cet article, vous apprendrez à propos des routes API dynamiques dans Next.js : ce qu'elles sont, comment les créer, et comment étendre leurs fonctionnalités.

## Qu'est-ce que les routes API ?

Avant de savoir ce qu'est une route API, vous devriez savoir ce qu'est une route et ce qu'est une API.

Une route est un chemin unique de dossiers imbriqués. Next.js utilise un routeur de pages pour naviguer vers les différentes pages d'une application web. Chaque fichier dans le répertoire pages d'une application Next.js représente une page sur l'application web.

Par exemple, si vous créez un fichier checkout.js dans votre dossier pages et que vous visitez l'URL : "le-nom-de-domaine-de-votre-app/checkout" sur votre navigateur, vous verrez le contenu du fichier checkout.js rendu.

Une API (abréviation de interface de programmation d'applications) sert de moyen de communication entre deux ordinateurs ou morceaux de logiciel. Dans une application web, une API facilite la communication entre le client et le serveur.

Une route API est une URL qui dirige les requêtes entrantes du client vers la ressource serveur appropriée qui traitera les requêtes.

Les routes API dans Next.js vous permettent de créer des endpoints API en tant que fonctions serverless Node.js. Ces endpoints vous permettent de faire des requêtes HTTPS et également de communiquer avec une base de données.

## Comment créer une route API

Pour créer une route API, vous allez créer un dossier nommé API dans votre dossier pages. Tout fichier à l'intérieur du répertoire /pages/api sera traité comme une route API au lieu d'une page.

Par exemple, vous pouvez créer un dossier nommé API dans votre dossier pages puis créer un fichier nommé start.js à l'intérieur avec le code suivant :

```javascript
// pages/api/start.js

export default function handler(req, res) {
  res.status(200).json({ message: 'Requête réussie' });
}
```

Vous avez maintenant créé une route API. Vous pouvez accéder à cette route API via cette URL : /api/start. Vous pouvez l'utiliser pour traiter une requête HTTP et renvoyer la réponse au client.

L'argument request est une instance d'un message entrant HTTP plus quelques middlewares préconstruits. L'argument response est une instance d'une réponse serveur HTTP plus quelques fonctions d'assistance.

Vous pouvez créer une route API pour traiter une seule méthode HTTP. Pour ce faire, vous devrez créer un nouveau fichier nommé get.js. Ensuite, vous pouvez ajouter ce code au fichier :

```javascript
// pages/api/get.js

export default function handler(req, res) {
  if (req.method === 'GET') {
  	res.status(200).json({ message: 'Ceci est une requête GET' });
  } else {
  	res.status(405).json({ message: 'Méthode non autorisée' });
  }
}
```

Cette route API peut être accessible via cette URL : /api/get et elle ne traitera que les requêtes HTTP GET.

Vous pouvez également créer une route API pour traiter plus d'une méthode HTTP. Pour ce faire, créez un nouveau fichier nommé all.js et mettez ce code dedans :

```javascript
// pages/api/all.js

function handler(req, res) {
  if (req.method === 'GET') {
  	// Traiter la requête GET
  	res.status(200).json({ message: 'Ceci est une requête GET' });
  } else if (req.method === 'POST') {
  	// Traiter la requête POST
  	res.status(200).json({ message: 'Ceci est une requête POST' });
  } else if (req.method === 'PUT') {
  	// Traiter la requête PUT
  	res.status(200).json({ message: 'Ceci est une requête PUT' });
  } else (req.method === 'DELETE') {
  	// Traiter la requête DELETE
  	res.status(200).json({ message: 'Ceci est une requête DELETE' });
  }
}
```

Cette route API peut être accessible via cette URL : /api/all et peut traiter quatre méthodes HTTP (GET, POST, PUT et DELETE).

## Comment créer des routes API dynamiques

Next.js permet aux développeurs de créer des routes dynamiques. Les routes dynamiques sont des routes dont les noms de segments ne sont pas connus à l'avance. Elles sont créées à partir de données dynamiques.

Une route API dynamique est une forme de route dynamique qui vous permet de créer des endpoints API avec des segments dynamiques dans le chemin de la route.

Ces segments sont remplis au moment de la requête ou pré-rendus au moment de la construction. Ils peuvent également être mis en cache par le navigateur, ce qui peut améliorer les performances pour les pages fréquemment consultées. Cela en fait un bon choix pour les applications qui s'attendent à beaucoup de trafic.

### Syntaxe des routes dynamiques

Il existe une syntaxe particulière pour créer des routes API dynamiques dans Next.js. Next.js vous permet de créer des routes API dynamiques en enveloppant le nom du fichier dans des crochets.

Pour créer une route API dynamique pour une API de bibliothèque qui récupère les données d'auteur avec des IDs dynamiques, vous pouvez commencer par créer un nouveau dossier nommé `authors` puis créer un fichier nommé `[id].js` et ajouter le code suivant :

```javascript
// api/authors/[id].js

export default function handler(req, res) {
  const { id } = req.query;
  
  if (req.method === 'GET') {
  	res.status(200).json({ id, message: 'Données de l\'auteur récupérées avec succès' });
  }
}
```

La route API pour le code ci-dessus sera `/author/[id]`, et si elle reçoit ce paramètre `{ id: '234' }`, elle correspondra à l'URL : `/author/234`.

Vous pouvez faire en sorte que votre route API dynamique traite différentes méthodes HTTP. Pour ce faire, supprimez le code dans votre dossier `[id].js` et mettez ce code à la place :

```javascript
// api/authors/[id].js

export default function handler(req, res) {
  const { id } = req.query;
  
  if (req.method === 'GET') {
  	res.status(200).json({ id, message: 'Données de l\'auteur récupérées avec succès' });
  } else if (req.method === 'POST') {
  	res.status(200).json({ id, message: 'Données de l\'auteur envoyées avec succès' });
  } else if (req.method === 'PUT') {
  	res.status(200).json({ id, message: 'Données de l\'auteur mises à jour avec succès' });
  } else if (req.method === 'DELETE') {
  	res.status(200).json({ id, message: 'Données de l\'auteur supprimées avec succès' });
  }
}
```

### Segments catch-all

Vous pouvez également passer des sous-paramètres à vos routes API dynamiques. Pour ce faire, vous allez étendre votre route API dynamique pour qu'elle puisse capturer tous les segments suivants qui lui sont passés en ajoutant une ellipse avant le nom du fichier dans les crochets. Cela garantit que les routes API peuvent recevoir plus d'un sous-paramètre.

Pour créer une route API dynamique qui capture tous les segments, créez un dossier nommé store et créez un fichier dans votre dossier store nommé `[...gadgets].js`. Ensuite, ajoutez le code suivant :

```javascript
// api/store/[...gadgets].js

export default function handler(req, res) {
  const { gadget } = req.query;
  
  if (req.method === 'GET') {
  	res.status(200).json({ id, message: 'Données récupérées avec succès' });
  }
}
```

La route API pour le code ci-dessus sera `pages/api/store/[...gadgets].js`. Si elle reçoit ce paramètre `{ gadget: ['phones', 'iphones', 'iphone15'] }`, elle correspondra aux URLs : `/store/phones ou /store/phones/iphones ou /store/phones/iphones/iphone15`.

### Segments catch-all optionnels

Vous pouvez rendre les segments catch-all de la route API dynamique optionnels. Lorsque vous les rendez optionnels, ils pourront non seulement correspondre à tous les segments suivants du chemin de l'URL, mais aussi au chemin principal de l'URL.

Pour rendre les segments catch-all suivants de la route API dynamique que nous avons vue dans la section précédente optionnels, ajoutez un crochet au nom du fichier comme ceci : `[[...store]].js]`. Les segments catch-all optionnels pourront non seulement correspondre aux URLs : `/store/phones ou /store/phones/iphones ou /store/phones/iphones/iphone15` seules – ils pourront également correspondre aux URLs `/store`.

## Conclusion

Cet article vous a aidé à comprendre les routes API dynamiques dans Next.js, y compris ce qu'elles sont, leurs utilisations et comment les créer.