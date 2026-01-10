---
title: Simuler GraphQL avec graphql-tools+
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-03T23:15:48.000Z'
originalURL: https://freecodecamp.org/news/mocking-graphql-with-graphql-tools-42c2dd9d0364
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9cb38c740569d1a4cac9a0.jpg
tags:
- name: Apollo GraphQL
  slug: apollo
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: Mocking
  slug: mocking
- name: Testing
  slug: testing
seo_title: Simuler GraphQL avec graphql-tools+
seo_desc: 'By Jeff M Lowery

  How to mock up your GraphQL API with realistic values

  In my last article, I took the original Apollo LaunchPad Posts and Authors API and
  broke it down into domains and components. I wanted to illustrate how one could
  organize a large...'
---

Par Jeff M Lowery

#### Comment simuler votre API GraphQL avec des valeurs réalistes

Dans [mon dernier article,](https://medium.com/@jefflowery/declarative-graphql-with-graphql-tools-cd1645f94fc), j'ai pris l'API originale Apollo LaunchPad [Posts and Authors](https://launchpad.graphql.com/1jzxrj179) et l'ai décomposée en domaines et composants. Je voulais illustrer comment organiser un grand projet GraphQL en utilisant [graphql-tools](https://github.com/apollographql/graphql-tools).

Maintenant, j'aimerais que l'API retourne des données simulées lorsque je l'interroge. Comment ?

### La source originale

Dans l'exemple original Apollo Launchpad, nous avons utilisé des structures de données statiques et des résolveurs de mappage simples pour fournir une sortie pour les requêtes.

Par exemple, étant donné cette requête :

```graphql
# Bienvenue dans GraphiQL

query PostsForAuthor {
  author(id: 1) {
    firstName
    posts {
      title
      votes
    }
  }
}
```

La sortie serait :

```json
{
  "data": {
    "author": {
      "firstName": "Tom",
      "posts": [
        {
          "title": "Introduction à GraphQL",
          "votes": 2
        }
      ]
    }
  }
}
```

L'objet résolveurs contient des fonctions qui s'occupent de mapper les auteurs aux posts et vice-versa. Ce n'est pas vraiment une simulation, cependant.

Le problème est que plus les relations et les entités deviennent complexes, plus de code doit être ajouté aux résolveurs. Ensuite, plus de données doivent être fournies.

En ce qui concerne les tests, les tests sont susceptibles de révéler parfois des problèmes dans les données ou dans les résolveurs. Vous voulez vraiment vous concentrer sur les tests de l'API elle-même.

### Utilisation des simulations

Il existe trois modules Node.js qui rendent la simulation d'une API rapide et facile. Le premier fait partie du module `graphql-tools`. En utilisant ce module, une première étape consiste à importer la méthode `addMockFunctionsToSchema` depuis le module dans le fichier racine `schema.js` :

```js
import {
    makeExecutableSchema,
    addMockFunctionsToSchema
} from 'graphql-tools';
```

Ensuite, après avoir créé un schéma exécutable en appelant `createExecutableSchema`, vous ajoutez vos simulations comme suit :

```js
    addMockFunctionsToSchema({
        schema: executableSchema,
    })
```

Voici une liste complète du fichier racine `schema.js` :

```js
// Cet exemple démontre un serveur simple avec certaines données relationnelles : Posts et Authors. Vous pouvez obtenir les posts pour un auteur particulier,
// et vice-versa. Lisez la documentation complète pour graphql-tools ici : http://dev.apollodata.com/tools/graphql-tools/generate-schema.html

import {
    makeExecutableSchema,
    addMockFunctionsToSchema
} from 'graphql-tools';

import {
    schema as authorpostsSchema,
    resolvers as authorpostsResolvers
} from './authorposts';

import {
    schema as myLittleTypoSchema,
    resolvers as myLittleTypeResolvers
} from './myLittleDomain';

import {
    merge
} from 'lodash';

const baseSchema = [
    `
    type Query {
        domain: String
    }
    type Mutation {
        domain: String
    }
    schema {
        query: Query,
        mutation: Mutation
    }`
]

// Assembler le schéma en un seul tableau de chaînes de schéma et une seule carte de résolveurs, comme makeExecutableSchema l'attend
const schema = [...baseSchema, ...authorpostsSchema, ...myLittleTypoSchema]

const options = {
    typeDefs: schema,
    resolvers: merge(authorpostsResolvers, myLittleTypeResolvers)
}

const executableSchema = makeExecutableSchema(options);

addMockFunctionsToSchema({
    schema: executableSchema
})

export default executableSchema;
```

Alors, quelle est la sortie ? L'exécution de la même requête qu'avant donne :

```json
{
  "data": {
    "author": {
      "firstName": "Hello World",
      "posts": [
        {
          "title": "Hello World",
          "votes": -70
        },
        {
          "title": "Hello World",
          "votes": -77
        }
      ]
    }
  }
}
```

Eh bien, c'est un peu stupide. Chaque chaîne est « Hello World », les votes sont négatifs, et il y aura toujours exactement deux posts par auteur. Nous allons corriger cela, mais d'abord...

#### Pourquoi utiliser des simulations ?

Les simulations sont souvent utilisées dans les tests unitaires pour séparer la fonctionnalité testée des dépendances sur lesquelles ces fonctions reposent. Vous voulez tester la fonction (l'unité), pas un ensemble complexe de fonctions.

À ce stade précoce du développement, les simulations servent un autre but : tester les tests. Dans un test de base, vous voulez d'abord vous assurer que le test appelle correctement l'API, et que les résultats retournés ont la structure, les propriétés et les types attendus. Je pense que les enfants cool appellent cela la « forme ».

Cela offre un test plus limité qu'une structure de données interrogeable, car la sémantique de référence n'est pas appliquée. L'`id` est sans signification. Néanmoins, les simulations offrent quelque chose pour structurer vos tests.

### Simulation réaliste

Il existe un module appelé [casual](https://github.com/boo1ean/casual) que j'apprécie vraiment. Il fournit des valeurs raisonnables et variables pour de nombreux types de données courants. Si vous démontrez votre nouvelle API devant des collègues blasés, cela donne vraiment l'impression que vous avez fait quelque chose de spécial.

Voici une liste de souhaits pour les valeurs simulées à afficher :

1. Le prénom de l'auteur doit être **comme un prénom**
2. Les titres des posts doivent être des textes **lorem ipsum** variables de longueur limitée
3. Les votes doivent être positifs ou nuls
4. Le nombre de posts doit varier entre 1 et 7

La première chose à faire est de créer un dossier appelé `mocks`. Ensuite, nous ajouterons un fichier `index.js` à ce dossier avec les méthodes de simulation. Enfin, les simulations personnalisées seront ajoutées au schéma exécutable généré.

La bibliothèque **casual** peut générer des valeurs par type de données (`String, ID, Int, ...`) ou par nom de propriété. De plus, l'objet MockList de graphql-tools sera utilisé pour faire varier le nombre d'éléments dans une liste — dans ce cas, `posts`. Alors commençons.

Importez à la fois casual et MockList dans `/mocks/index.js` :

```js
import casual from 'casual';
import {
    MockList
} from 'graphql-tools';
```

Maintenant, créons une exportation par défaut avec les propriétés suivantes :

```js
export default {
    Int: () => casual.integer(0),
    
    Author: () => ({
        firstName: casual.first_name,
        posts: () => new MockList([1, 7])
    }),
    
    Post: () => ({
        title: casual.title
    })
}
```

La déclaration `Int` prend en charge tous les types entiers apparaissant dans notre schéma et garantira que `Post.votes` sera positif ou nul.

Ensuite, `Author.firstName` sera un prénom raisonnable. MockList est utilisé pour garantir que le nombre de posts associés à chaque auteur sera compris entre 1 et 7. Enfin, casual générera un titre **lorem ipsum** pour chaque `Post`.

Maintenant, la sortie générée varie à chaque exécution de la requête. Et cela semble crédible :

```json
{
  "data": {
    "author": {
      "firstName": "Eldon",
      "posts": [
        {
          "title": "Voluptatum quae laudantium",
          "votes": 581
        },
        {
          "title": "Vero quos",
          "votes": 85
        },
        {
          "title": "Doloribus labore corrupti",
          "votes": 771
        },
        {
          "title": "Qui nulla qui",
          "votes": 285
        }
      ]
    }
  }
}
```

### Génération de valeurs personnalisées

Je n'ai fait qu'effleurer la surface de ce que casual peut faire, mais il est bien documenté et il n'y a pas grand-chose à ajouter.

Parfois, cependant, il y a des valeurs qui doivent se conformer à un format standard. J'aimerais présenter un autre module : [randexp](https://www.npmjs.com/package/randexp).

Randexp vous permet de générer des valeurs conformes à l'expression régulière que vous lui fournissez. Par exemple, les numéros ISBN ont le format :

**/ISBN-\d-\d{3}-\d{5}-\d/**

Maintenant, je peux ajouter des livres au schéma, ajouter des livres à l'auteur, et générer un ISBN et un titre pour chaque `Book` :

```js
// book.js
export default `
  type Book {
    ISBN: String
    title: String
}
```

mocks.js :

```js
import casual from 'casual';
import RandExp from 'randexp';
import {
    MockList
} from 'graphql-tools';
import {
    startCase
} from 'lodash';

export default {
    Int: () => casual.integer(0),
    
Author: () => ({
        firstName: casual.first_name,
        posts: () => new MockList([1, 7]),
        books: () => new MockList([0, 5])
    }),
    
Post: () => ({
        title: casual.title
    }),
    
Book: () => ({
        ISBN: new RandExp(/ISBN-\d-\d{3}-\d{5}-\d/)
            .gen(),
        title: startCase(casual.title)
    })
}
```

Et voici une nouvelle requête :

```graphql
query PostsForAuthor {
  author(id: 1) {
    firstName
    posts {
      title
      votes
    }
    books {
      title
      ISBN
    }
  }
}
```

Exemple de réponse :

```json
{
  "data": {
    "author": {
      "firstName": "Rosemarie",
      "posts": [
        {
          "title": "Et ipsum quo",
          "votes": 248
        },
        {
          "title": "Deleniti nihil",
          "votes": 789
        },
        {
          "title": "Aut aut reprehenderit",
          "votes": 220
        },
        {
          "title": "Nesciunt debitis mollitia",
          "votes": 181
        }
      ],
      "books": [
        {
          "title": "Consequatur Veniam Voluptas",
          "ISBN": "ISBN-0-843-74186-9"
        },
        {
          "title": "Totam Et Iusto",
          "ISBN": "ISBN-6-532-70557-3"
        },
        {
          "title": "Voluptatem Est Sunt",
          "ISBN": "ISBN-2-323-13918-2"
        }
      ]
    }
  }
}
```

Voici donc les bases de la simulation en utilisant graphql-tools plus quelques autres modules utiles.

**Note** : J'utilise des extraits tout au long de cet article. Si vous souhaitez suivre dans un contexte plus large, le code exemple est [ici](https://github.com/JeffML/graphql_authors_mock).

La [source complète](https://github.com/JeffML/graphql_authors_mock) est sur GitHub pour votre consultation.

Donnez-moi un coup de main si vous avez trouvé cet article informatif.