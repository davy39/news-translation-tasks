---
title: Comment éviter le problème des requêtes N+1 dans les API GraphQL et REST [avec
  benchmarks]
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-07-07T17:59:59.000Z'
originalURL: https://freecodecamp.org/news/n-plus-one-query-problem
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/N-1-Query-Problem.png
tags:
- name: api
  slug: api
- name: GraphQL
  slug: graphql
- name: performance
  slug: performance
- name: REST API
  slug: rest-api
- name: web performance
  slug: web-performance
seo_title: Comment éviter le problème des requêtes N+1 dans les API GraphQL et REST
  [avec benchmarks]
seo_desc: 'By Mohamed Mayallo

  The N+1 query problem is a performance issue you might face while building APIs,
  regardless of whether they''re GraphQL or REST APIs.

  In fact, this problem occurs when your application needs to return a set of data
  that includes rel...'
---

Par Mohamed Mayallo

Le problème des requêtes N+1 est un problème de performance que vous pourriez rencontrer lors de la création d'API, qu'il s'agisse d'API GraphQL ou REST.

En fait, ce problème se produit lorsque votre application doit retourner un ensemble de données qui inclut des données imbriquées liées – par exemple, un article qui inclut des commentaires.

Mais comment pouvez-vous résoudre ce problème ? Pour éviter ce problème, vous devez comprendre ce qu'il est et comment il se produit.

Ainsi, dans ce tutoriel, vous apprendrez ce qu'est le problème des requêtes N+1, pourquoi il est facile d'y tomber, et comment vous pouvez l'éviter.

Avant de commencer, il est bon de savoir :

* Les exemples dans cet article sont juste pour la simplicité.
* `SELECT *` est très mauvais, et vous devriez l'éviter.
* Vous devriez vous soucier de la pagination si vous travaillez avec de grands ensembles de données.

Vous pouvez trouver les exemples de cet article dans ce [dépôt](https://github.com/Mohamed-Mayallo/n_plus_one_problem_benchmarks). Plongeons-nous dans le sujet.

## Comprendre le problème des requêtes N+1

Le problème N+1 se produit lorsque votre application doit retourner un ensemble de données qui inclut des données liées existant dans :

* Une autre table.
* Une autre base de données (dans le cas de microservices, par exemple)
* Ou même un autre service tiers.

En d'autres termes, vous devez exécuter des requêtes de base de données supplémentaires ou des requêtes externes pour retourner les données imbriquées.

Si vous vous demandez ce que signifie le nom (N+1), suivez l'exemple ci-dessous, qui utilise une seule base de données :

![Tables Post et Comment | Par l'auteur](https://www.freecodecamp.org/news/content/images/2023/07/related-data.drawio.png)
_Illustration du problème N+1_

Comme vous pouvez le voir, la relation entre `Post` et `Comment` est respectivement de un à plusieurs.

Ainsi, si votre application doit retourner une liste d'articles et leurs commentaires associés, vous pourriez finir avec ce code :

```js
const posts = await rawSql('SELECT * FROM "Post"'); // Obtenir tous les articles (1 requête de base de données)
for (const post in posts) {
	// Bien sûr, vous pouvez remplacer la requête suivante par une requête externe si vous devez récupérer les commentaires de l'article depuis un autre service
	const comments = await rawSql(`SELECT * FROM "Comment" WHERE "post_id" = ${post.id}`); // Obtenir tous les commentaires pour chaque article (n requêtes de base de données pour n articles)
	post.comments = comments;
}

```

Ainsi, vous avez exécuté **N** requêtes pour récupérer les commentaires de chaque article et **1** requête pour récupérer tous les articles **(N requêtes de commentaires + 1 requête d'articles).**

Mais pourquoi devriez-vous être conscient de ce problème ?

## Pourquoi le problème des requêtes N+1 est-il un problème sérieux ?

Voici quelques raisons pour lesquelles le problème des requêtes N+1 peut causer de sérieux problèmes de performance dans votre application :

1. Votre application effectue de nombreuses requêtes de base de données ou requêtes externes pour récupérer une liste de données comme des articles.
2. Plus votre application récupère de données, plus votre requête sera lente et plus votre application consommera de ressources.
3. Un grand ensemble de données pourrait entraîner une latence réseau notable.
4. Il sera difficile de mettre à l'échelle l'application pour gérer de plus grands ensembles de données.

En plus de cela, vous allez voir l'impact sur la performance en chiffres dans la section des benchmarks plus tard dans cet article.

Maintenant que vous comprenez le problème des requêtes N+1 et son impact sur votre application, introduisons quelques moyens efficaces pour éviter ce problème.

## Stratégies pour éviter le problème des requêtes N+1

Heureusement, il existe quelques stratégies simples que vous pouvez suivre pour éviter le problème des requêtes N+1.

Appliquons-les à notre exemple précédent.

### 1) Chargement anticipé (en utilisant des jointures SQL, par exemple)

Dans cette stratégie, au lieu de retourner les commentaires de l'article séparément pour chaque article, vous pouvez utiliser des **jointures SQL**.

```js
const postsAndComments = await rawSql(`
	SELECT * 
	FROM "Post"
	JOIN "Comment"
	ON "Comment"."post_id" = "Post"."post_id"
`);

```

Lorsque vous utilisez cette stratégie, il est bon de savoir que :

* Il n'y a qu'une seule requête de base de données pour retourner tous les articles et leurs commentaires imbriqués.
* Vous ne pouvez pas appliquer cette stratégie si vous consommez vos ensembles de données à partir d'une base de données ou d'un service différent.

### 2) Chargement par lots

Dans cette stratégie, votre code doit suivre les étapes suivantes :

* Exécuter une requête pour récupérer tous les articles.
* Exécuter une autre requête pour charger un lot de commentaires d'articles au lieu de charger les commentaires de chaque article séparément.
* Associer chaque commentaire à son article parent correspondant.

Passons à un exemple :

```js
const posts = await rawSql('SELECT * FROM "Post"'), // 1- Récupérer tous les articles en une requête
	postsIds = posts.map(post => post.id),
	postsComments = await rawSql(`SELECT * FROM "Comment" WHERE "post_id" IN (${postsIds})`); // 2- récupérer tous les commentaires des articles en une autre requête

for (const post in posts) { // 3- Associer chaque commentaire à son article parent
	const comments = postsComments.filter(comment => comment.post_id === post.id);
	post.comments = comments;
}

```

Comme vous pouvez le voir, dans cette stratégie, il n'y a que deux requêtes : une pour récupérer tous les articles et une autre pour récupérer leurs commentaires.

### 3) Mise en cache

Vous êtes peut-être familier avec la mise en cache et son impact sur les performances de toute application.

Vous pouvez implémenter la mise en cache côté client ou côté serveur en utilisant [Redis](https://redis.io/), [Memcached](https://memcached.org/), ou tout autre outil similaire. Où que vous puissiez utiliser correctement la mise en cache, elle améliore considérablement les performances de votre application.

Revenons à notre exemple et mettons en cache les commentaires des articles dans un stockage Redis.

```js
	const posts = await rawSql('SELECT * FROM "Post"'),
		postsIds = posts.map(post => post.id),
		cachedPostsComments = getPostsCommentsFromRedis(postsIds);

for (const post in posts) {
	const comments = cachedPostsComments.filter(comment => comment.post_id === post.id);
	post.comments = comments;
}

```

Comme vous pouvez le deviner, vous pouvez mettre en cache les commentaires des articles ou même les articles eux-mêmes, ce qui minimise considérablement la charge sur les bases de données.

### 4) Chargement paresseux

Dans cette stratégie, vous répartissez la responsabilité entre le côté serveur et le côté client.

Vous ne devez pas retourner toutes les données en une seule fois depuis le côté serveur. Au lieu de cela, vous préparez deux endpoints pour le côté client comme ceci :

* `GET /api/posts` : Récupère tous les articles.
* `GET /api/comments/:postId` : Récupère les commentaires d'un article à la demande.

Et maintenant, la récupération des données dépend du côté client.

Cette stratégie est très utile car :

* Elle permet au côté client de charger d'abord l'article parent et d'afficher son contenu, puis de charger ses commentaires associés de manière paresseuse. Ainsi, les utilisateurs n'ont pas à attendre que l'ensemble des données soit retourné depuis le côté serveur.
* Vous avez un contrôle total sur le tri, le filtrage, la pagination et ainsi de suite sur chaque endpoint.

Le point clé de cette stratégie est qu'elle se débarrasse des données imbriquées comme les commentaires et aplatit tous les ensembles de données dans leur propre endpoint.

### 5) GraphQL Dataloader

Comme vous pouvez le deviner, cette stratégie fonctionne avec les API GraphQL.

Dataloader est un utilitaire GraphQL qui fonctionne en regroupant plusieurs requêtes de base de données en une seule requête. Ainsi, il utilise la stratégie de chargement par lots sous le capot.

Passons à notre exemple :

```js
const DataLoader = require('dataloader');

// 1- Définition du schéma GraphQL
const typeDefs = gql`
  type Post {
    post_id: ID!
		comments: [Comment]
  }

	type Comment {
		comment_id: ID!
    post_id: ID!
  }

  type Query {
    posts: [Post]
  }
`;

// 2- Résolution du schéma GraphQL
const resolvers = {
  Query: {
    posts: async () => {
      const posts = await rawSql('SELECT * FROM "Post"');
			return posts;
    }
  },

  Post: {
    comments: (post, args, { dataLoaders }) => {
      return dataLoaders.commentsLoader.load(post.id);
    }
  }
};

// 3- Définir les Dataloaders
const commentsBatchFunction = async postsIds => {
	  const comments = await rawSql(`SELECT * FROM "Comment" WHERE "post_id" IN (${postsIds})`);
		const groupedComments = comments.reduce((tot, cur) => {
      if (!tot[cur.post_id]) {
        tot[cur.post_id] = [cur];
      } else {
        tot[cur.post_id].push(cur);
      }
      return tot;
    }, {});
		return postsIds.map((postId) => groupedComments[postId]);
	},
	createCommentsLoader = new DataLoader(commentsBatchFunction),
	createDataloaders = () => ({
		commentsLoader: createCommentsLoader()
	});

// 4- Injecter les Dataloaders dans le contexte GraphQL
const server = new ApolloServer({
	typeDefs,
	resolvers,
	context: () => {
    return {
      dataLoaders: createDataloaders(),
    }
  }
});

```

Alors, comment cela fonctionne-t-il ? Pour obtenir des informations plus détaillées, vous pouvez consulter la [documentation](https://github.com/graphql/dataloader). Mais nous allons passer en revue les bases ici.

Le point clé du Dataloader est la [Fonction de lot](https://github.com/graphql/dataloader#batch-function). Ici, la fonction de lot `commentsBatchFunction` prend un tableau de clés `postsIds` et retourne une [Promesse qui se résout](https://mayallo.com/asynchronous-javascript/) en un tableau de valeurs `comments`, `[ [post1comment1, post1comment2], [post2comment1], ... ]`.

En plus de cela, la fonction de lot a deux contraintes :

* La taille du tableau de clés `postsIds` doit être égale à celle du tableau de valeurs `comments`. En d'autres termes, cette expression doit être vraie : `postsIds.length === comments.length`.
* Chaque index dans le tableau de clés `postsIds` doit correspondre au tableau de valeurs `comments`. Ainsi, vous pourriez noter que j'ai parcouru les `postsIds` pour mapper chaque commentaire correspondant.

En conséquence, vous pouvez voir que GraphQL Dataloader utilise la deuxième stratégie (Chargement par lots) sous le capot.

Revenons à notre exemple pour parcourir son implémentation :

1. Tout d'abord, nous avons défini le schéma GraphQL.
2. Ensuite, nous avons résolu le schéma GraphQL. Gardez à l'esprit, si vous avez résolu les commentaires dans le type `Post` en utilisant cette requête `await rawSql('SELECT * FROM "Comment" WHERE "post_id" = ' + post.id);`, vous allez tomber dans le problème des requêtes N+1.
3. Ensuite, nous avons défini la fonction de lot des commentaires puis créé le dataloader des commentaires.
4. Enfin, nous avons injecté les dataloaders dans le [Contexte GraphQL](https://www.apollographql.com/docs/apollo-server/data/context/) pour pouvoir les utiliser dans les résolveurs.

Ainsi, en utilisant GraphQL Dataloader, si vous avez 10 articles et que chaque article a 5 commentaires, vous finirez avec deux requêtes – une pour récupérer les 10 articles et une autre pour récupérer leurs commentaires.

Jetez un coup d'œil à la capture d'écran suivante :

![Requêtes de base de données avec et sans GraphQL Dataloader](https://www.freecodecamp.org/news/content/images/2023/07/Code_1K9XMH0CHB.png)
_Illustration du processus avec et sans Dataloader_

## Benchmarks sur le problème des requêtes N+1

Dans cette section, comparons chaque stratégie en termes de performance.

<table>
<thead>
<tr>
<th>N+1 dans l'API REST</th>
<th>Stratégie de chargement anticipé</th>
<th>Stratégie de chargement par lots</th>
<th>Stratégie de mise en cache</th>
<th>N+1 dans l'API GraphQL</th>
<th>GraphQL Dataloader</th>
</tr>
</thead>
<tbody>
<tr>
<td>2.139</td>
<td>0.065</td>
<td>0.048</td>
<td>0.019</td>
<td>2.44</td>
<td>0.397</td>
</tr>
<tr>
<td>2.147</td>
<td>0.081</td>
<td>0.068</td>
<td>0.024</td>
<td>2.38</td>
<td>0.483</td>
</tr>
<tr>
<td>2.152</td>
<td>0.062</td>
<td>0.065</td>
<td>0.035</td>
<td>2.67</td>
<td>0.372</td>
</tr>
<tr>
<td>2.17</td>
<td>0.053</td>
<td>0.047</td>
<td>0.031</td>
<td>2.71</td>
<td>0.377</td>
</tr>
<tr>
<td>2.181</td>
<td>0.052</td>
<td>0.069</td>
<td>0.031</td>
<td>2.38</td>
<td>0.364</td>
</tr>
<tr>
<td>2.14</td>
<td>0.076</td>
<td>0.043</td>
<td>0.017</td>
<td>2.53</td>
<td>0.346</td>
</tr>
<tr>
<td>2.321</td>
<td>0.073</td>
<td>0.045</td>
<td>0.018</td>
<td>2.60</td>
<td>0.451</td>
</tr>
<tr>
<td>2.13</td>
<td>0.061</td>
<td>0.06</td>
<td>0.015</td>
<td>2.35</td>
<td>0.369</td>
</tr>
<tr>
<td>2.149</td>
<td>0.064</td>
<td>0.04</td>
<td>0.015</td>
<td>2.65</td>
<td>0.368</td>
</tr>
<tr>
<td>2.361</td>
<td>0.065</td>
<td>0.045</td>
<td>0.016</td>
<td>2.54</td>
<td>0.424</td>
</tr>
<tr>
<td style="font-weight: bold; background-color: #eee;">2.190</td>
<td style="font-weight: bold; background-color: #eee;">0.065</td>
<td style="font-weight: bold; background-color: #eee;">0.053</td>
<td style="font-weight: bold; background-color: #eee;">0.022</td>
<td style="font-weight: bold; background-color: #eee;">2.525</td>
<td style="font-weight: bold; background-color: #eee;">0.395</td>
</tr>
</tbody>
</table>

_Notez que les résultats de la stratégie de mise en cache arrivent juste après la mise en cache de l'ensemble de données. La première requête est ignorée car la mise en cache est manquante._

Ces résultats ont été générés à partir de l'environnement suivant :

* Données ensemencées : 1000 articles et 50 commentaires pour chaque article.
* CPU : AMD Ryzen 5 3600 6-Core Processor 3.60 GHz.
* RAM : 32.0 GB.
* OS : Windows 10 Pro.

Pour pouvoir retester ces stratégies dans votre environnement, suivez ces étapes :

* Clonez ce [dépôt](https://github.com/Mohamed-Mayallo/n_plus_one_problem_benchmarks).
* Ensuite, exécutez `docker-compose up`.
* Pour GraphQL, ouvrez `http://localhost:3000/graphql`.
* **Une requête souffre du problème N+1** : interrogez uniquement **`commentsWithNPlusOne`** dans le type `Post`.
* **Stratégie Dataloader** : interrogez uniquement `commentsWithDataloader` dans le type `Post`.
* Pour REST, suivez ces endpoints :
* **Une requête souffre du problème N+1** : `http://localhost:3000/api/postsWithNPlusOne`.
* **Stratégie de chargement anticipé** : `http://localhost:3000/api/postsWithEagerLoading`.
* **Stratégie de chargement par lots** : `http://localhost:3000/api/postsWithBatchLoading`.
* **Stratégie de mise en cache** : `http://localhost:3000/api/postsWithCache`.

Mes notes sur ces benchmarks :

* Ces stratégies sont beaucoup trop efficaces.
* Vous pourriez remarquer que la stratégie la plus lente dans REST, la stratégie de chargement anticipé, est **environ 34 fois plus rapide** que la requête N+1 dans l'API REST.
* La stratégie Dataloader est **environ 6.4 fois plus rapide** que la requête N+1 dans l'API GraphQL.
* Si vous avez comparé les résultats des API REST et GraphQL, vous pourriez remarquer que REST est plus rapide que GraphQL. Je pense que cela est dû aux implémentations internes de GraphQL, ce qui est logique.

## Conclusion

Dans cet article, vous avez appris que le problème des requêtes N+1 est un problème de performance que vous pourriez rencontrer lors de la création d'API.

Vous avez ensuite appris quelques stratégies que vous pouvez suivre pour éviter ce problème comme :

* Le chargement anticipé en utilisant des jointures SQL
* Le chargement par lots en exécutant moins de requêtes puis en mappant chaque élément correspondant à son parent.
* La mise en cache en utilisant Redis
* Le Dataloader dans le monde GraphQL.

Enfin, nous avons créé quelques benchmarks sur le problème des requêtes N+1 afin de voir à quel point ces stratégies améliorent efficacement les performances de notre API.

## Avant de partir

Si vous avez trouvé cet article utile, vous pouvez [consulter certains de mes autres articles sur mon blog personnel](https://mayallo.com/blog/).

Merci beaucoup de m'avoir suivi jusqu'à ce point. J'espère que vous avez apprécié la lecture de cet article.