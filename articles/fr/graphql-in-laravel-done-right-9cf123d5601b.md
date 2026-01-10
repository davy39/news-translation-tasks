---
title: 'GraphQL dans Laravel fait correctement : comment configurer Lighthouse dans
  un blog simple'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-01T09:17:09.000Z'
originalURL: https://freecodecamp.org/news/graphql-in-laravel-done-right-9cf123d5601b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*y_uXqbzjq767fB9TrY1vzw.png
tags:
- name: GraphQL
  slug: graphql
- name: Laravel
  slug: laravel
- name: Lighthouse
  slug: lighthouse
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: 'GraphQL dans Laravel fait correctement : comment configurer Lighthouse
  dans un blog simple'
seo_desc: 'By Oliver Nybroe

  Recently a new package has revolutionized the creation of a GraphQL API in Laravel.
  This package makes it so simple and easy to set up a GraphQL server, that it gives
  you the same feeling you had the first time you worked with Larave...'
---

Par Oliver Nybroe

Récemment, un nouveau package a révolutionné la création d'une API GraphQL dans Laravel. Ce package rend la configuration d'un serveur GraphQL si simple et facile qu'il vous donne la même sensation que vous avez eue la première fois que vous avez travaillé avec Laravel, « *Quelle magie est-ce !* ». Ce package est, bien sûr, [Lighthouse](https://lighthouse-php.netlify.com/).

Dans cet article, je vais expliquer comment configurer Lighthouse avec un exemple de blog simple. Je supposerai que vous êtes déjà familiarisé avec les bases de GraphQL. L'exemple vous permettra d'obtenir et de créer des articles via GraphQL. Lighthouse utilise une approche de schéma. Vous définissez votre API en créant un schéma GraphQL, puis utilisez des directives pour ajouter des liaisons avec Laravel.

### Installation

Pour commencer, ajoutez simplement le package via composer et publiez le fichier de configuration. (Le package `laravel-graphql-playground` est un client navigateur GraphQL qui est optionnel.)

```
$ composer require nuwave/lighthouse
$ php artisan vendor:publish --provider="Nuwave\Lighthouse\Providers\LighthouseServiceProvider"
$ composer require mll-lab/laravel-graphql-playground
$ php artisan vendor:publish --provider="MLL\GraphQLPlayground\GraphQLPlaygroundServiceProvider"
```

### Création du schéma

Maintenant, la partie intéressante : lors de la configuration de ce package, nous devons simplement créer le fichier suivant `routes/graphql/schema.graphql`. Ce fichier est celui qui contient tout notre schéma pour le serveur graphql.

Pour commencer, nous allons ajouter un endpoint simple pour obtenir tous les articles dans notre base de données. Pour cela, nous devons d'abord créer notre type Article dans le fichier de schéma.

```
...type Article {
    id: ID!
    title: String!
    body: String!
    author: User!
}
```

#### Définition de la requête de schéma

Nous avons maintenant deux types, un type pour les articles et un pour les utilisateurs, afin que nous puissions obtenir l'auteur de l'article. Cependant, nous n'avons toujours pas d'endpoints pour les articles, alors ajoutons-en un dans le fichier de schéma.

```
type Query {
  ...
  articles: [Article]! @paginate(type: "paginator" model: "Article")
}
```

Maintenant, un peu plus de magie se produit. Nous ajoutons une directive personnalisée appelée `paginate`. Cette directive ajoute une pagination pour le modèle fourni (dans ce cas, Article). Nous disons également qu'il doit utiliser le type `paginator`, ce qui entraînera la création d'un type compatible avec la pagination pour nous.

Pour parcourir les endpoints, ouvrons le client GraphQL que nous avons installé en allant sur `your-url.test/graphql-playground`. Dans le schéma, nous pouvons maintenant voir qu'un nouveau type appelé `ArticlePaginator` est ajouté. L'endpoint `articles` retourne une instance de `ArticlePaginator`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*IAcFIeIGTk-9qMrdh0i0ng.png)
*Capture d'écran de graphql-playground*

#### Exécution de la requête

Alors, créons une requête simple pour obtenir 10 articles avec leur titre et le nom de l'auteur.

```
query {
  articles(count: 10) {
    data {
      title
      author {
        name
      }
    }
  }
}
```

Lorsque nous exécutons cette requête, cela entraîne une erreur indiquant qu'il n'a pas pu trouver une classe appelée `Article`. Cela a du sens car nous n'avons pas encore créé le modèle. Ce message de débogage n'est visible que parce que nous ne sommes pas en environnement de production.

![Image](https://cdn-media-1.freecodecamp.org/images/1*QxpBku6o7YILTd7ruavSpA.png)
*Capture d'écran de graphql-playground montrant l'erreur de classe Article manquante*

### Création de notre modèle et migrations

Alors, créons nos modèles et migrations. Par défaut, Lighthouse recherche les modèles dans `app/models`. Pour simplifier, nous allons ajouter le modèle Article ici. Nous n'avons pas besoin de déplacer le modèle User car dans le fichier de schéma, le namespace pour User a été typé directement.

```
$ php artisan make:model Models\\Article -m
```

Ensuite, mettez à jour la migration et les modèles :

#### Requête des articles

Maintenant que nos modèles et migrations sont configurés, migrons la base de données et vérifions si cela échoue toujours.

![Image](https://cdn-media-1.freecodecamp.org/images/1*q5g3oVVj0N-2hl6xS2DBYg.png)
*Capture d'écran de graphql-playground montrant aucun résultat*

Nous pouvons voir maintenant que l'endpoint fonctionne, mais nous n'avons pas de données dans la base de données. Nous allons en ajouter manuellement et ensuite aborder comment faire cela via GraphQL.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8Ud6YZtAsMbj0ArK5v71Hw.png)
*Capture d'écran de graphql-playground montrant les articles*

Super ! Nous sommes maintenant capables de récupérer des articles via GraphQL. Ajoutons également la possibilité d'obtenir les articles d'un utilisateur. Pour cela, nous devons modifier notre type GraphQL `user` pour qu'il ait une relation avec les articles.

```
...type User {
  id: ID!
  name: String!
  email: String!
  created_at: DateTime!
  updated_at: DateTime!
  articles: [Article] @hasMany(relation:"articles" type:"paginator")
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*gBXB_T_1jbQ1arC76nPbyw.png)
*Capture d'écran de graphql-playground montrant les articles d'un utilisateur*

Comme il s'agit de GraphQL, nous pourrions continuer à enchaîner. Ainsi, nous pouvons obtenir l'auteur de l'article, puis les articles de cet auteur, et ainsi de suite (même si cela serait plutôt inutile).

![Image](https://cdn-media-1.freecodecamp.org/images/1*JrfHjTerwsuD6tLxD_cpnw.png)
*Capture d'écran de graphql-playground montrant une requête inutile*

### Création d'un mutateur

Maintenant, ajoutons un mutateur pour créer un nouvel article. Cet endpoint nécessitera également une authentification. Bien sûr, nous devons être un utilisateur dans le système avant de pouvoir créer un nouvel article. Pour cela, nous utiliserons le middleware `auth:api` de Laravel. Supprimez toutes les mutations précédentes, car nous n'en avons pas besoin, et ajoutez ce qui suit :

```
type Mutation @group(middleware: ["auth:api"]) {
    createArticle(title: String!, body: String!): Article
        @create(model: "Article")
        @inject(context: "user.id", name: "author_id")
}
```

#### Authentification du mutateur

Pour utiliser le middleware `auth:api`, nous devons configurer un `Guard`. Pour cet exemple, nous utiliserons simplement le `TokenGuard`. Pour utiliser le token guard, nous devons ajouter un champ à l'utilisateur appelé `api_token`, et la valeur là-bas est votre token.

```
Schema::create('users', function (Blueprint $table) {
    $table->increments('id');
    $table->string('name');
    $table->string('email')->unique();
    $table->timestamp('email_verified_at')->nullable();
    $table->string('password');
    $table->string('api_token'); // Le nouveau champ de token API
    $table->rememberToken();
    $table->timestamps();
});
```

Maintenant, nous ajoutons manuellement le token dans la base de données et le définissons sur `secret` (vous pouvez créer votre propre UI pour définir le token ou utiliser [Laravel Passport](https://laravel.com/docs/5.8/passport)). Nous ajoutons ensuite ce token à notre requête, afin d'être authentifiés.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MZJI3CzdGJn_UvWdXgWg_g.png)
*Capture d'écran de graphql-playground montrant les en-têtes*

#### Utilisation du mutateur

![Image](https://cdn-media-1.freecodecamp.org/images/1*HsC1fl7a8hNDkHBHAWPaGQ.png)
*Capture d'écran de graphql-playground montrant la mutation*

Nous avons maintenant un nouvel article, et nous pouvons voir que l'auteur qui l'a créé était notre utilisateur authentifié. Nous avons donc une API GraphQL très simple en fonctionnement, mais avec la possibilité d'obtenir nos articles et de les créer !

J'espère que vous avez apprécié cet article, et si vous souhaitez en savoir plus, visitez la [documentation de Lighthouse](https://lighthouse-php.com/). Vous pouvez également trouver l'exemple créé ci-dessus sur [Github](https://github.com/olivernybroe/lighthouse-intro-article).