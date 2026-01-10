---
title: Comment utiliser TypeScript avec GraphQL en utilisant TypeGraphQL
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-04-13T00:18:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-typescript-with-graphql
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/pexels-reagan-787642.jpg
tags:
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: TypeScript
  slug: typescript
- name: Web Development
  slug: web-development
seo_title: Comment utiliser TypeScript avec GraphQL en utilisant TypeGraphQL
seo_desc: 'By Dillion Megida

  In this tutorial, I''ll explain what TypeScript and GraphQL are, and the benefits
  of using them.

  Then I''ll show you how you can use them together using TypeGrapQL, and why you''d
  want to do this.

  What is TypeScript?

  TypeScript is a su...'
---

Par Dillion Megida

Dans ce tutoriel, je vais expliquer ce que sont TypeScript et GraphQL, et les avantages de les utiliser.

Ensuite, je vais vous montrer comment les utiliser ensemble avec TypeGraphQL, et pourquoi vous voudriez le faire.

## Qu'est-ce que TypeScript ?

TypeScript est un sur-ensemble de JavaScript qui compile en JavaScript pour la production. C'est comme JavaScript, mais avec des pouvoirs – des pouvoirs de typage.

TypeScript vous aide à construire des applications typées qui vous aident à éviter les erreurs de type statique dans ces applications et à rendre le code prévisible.

Sans TypeScript, une fonction déclarée pour recevoir un argument de type chaîne peut recevoir un argument de type nombre pendant l'exécution, et vous pouvez obtenir une erreur d'exécution. Cela peut être mauvais pour le code de production.

Avec TypeScript, une telle fonction entraînera une erreur de compilation à moins que le type approprié ne soit passé.

TypeScript peut gérer plus que des types primitifs. Il peut également garantir que des objets structurés corrects et attendus sont typés. Cela signifie qu'une propriété d'objet manquante peut également entraîner une erreur.

TypeScript nous aide à construire un code JavaScript plus prévisible pendant le développement grâce à la vérification de type. Il est également intégré dans des éditeurs comme VSCode, ce qui facilite la détection des erreurs de type lors de l'écriture de code.

TypeScript prend une étape supplémentaire pour compiler en JavaScript pour l'utilisation. Alors que certaines bibliothèques comme React le font interne pour vous, vous devrez peut-être le configurer vous-même si vous construisez sans de tels outils. Mais je dirais que cela en vaut la peine.

## Qu'est-ce que GraphQL ?

GraphQL est une autre méthode pour gérer les API. C'est une alternative aux API Rest qui vous permet de demander "uniquement les données dont vous avez besoin". Cela aide à réduire la quantité de données qui doivent être envoyées au client depuis le serveur.

Par exemple, avec une API Rest, un endpoint peut retourner toutes les données des utilisateurs alors que seuls leur email et leur numéro de téléphone sont nécessaires à ce moment-là. Cela est appelé "sur-récupération". Avec GraphQL, le client peut demander des données spécifiques.

GraphQL vient également avec des définitions de type, qui existent dans les objets de schéma. GraphQL utilise des objets de schéma pour savoir quelles propriétés sont interrogeables, et essentiellement, le type de requêtes qui sont acceptées. Il génère également une erreur lorsqu'une requête non acceptée est exécutée.

Cependant, ces définitions de type sont limitées aux objets de schéma. Elles ne vous donnent pas un typage statique global dans votre application. Et c'est pourquoi TypeScript est un excellent ajout, comme nous le verrons dans le reste de cet article.

## Avantages de l'utilisation de TypeScript et GraphQL

L'utilisation de TypeScript et GraphQL garantit que le typage statique existe dans toute votre application.

Sans TypeScript, vous pouvez toujours créer des types de requête avec GraphQL. Mais il y a une limitation à cela.

Les types GraphQL n'existent que dans le schéma GraphQL. La fonction `buildSchema` de la bibliothèque GraphQL est utilisée pour créer l'objet de schéma :

```js
const schema = buildSchema(`
    type Query {
        name(firstname: String!, lastname: String!): String
    }
`)
```

Nous avons créé l'objet de schéma, et maintenant nous avons besoin d'un resolver :

```js
const root = {
    name: variables => {
        return `My name is ${firstname} ${lastname}!`
    },
}
```

En exécutant la requête avec des variables de type incorrect dans un playground GraphQL, nous obtiendrions des erreurs :


![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-4.png)
_Playground GraphQL montrant une erreur pour un type incorrect fourni à la requête_

Mais les resolvers ne sont pas conscients de la définition de type dans l'objet de schéma. Comme vous pouvez le voir, le resolver est une fonction JavaScript régulière. Cela signifie que nous n'avons pas de typage statique dans le resolver.

Par exemple, si nous fournissons les mauvais types d'arguments au resolver, ou si nous retournons un type différent du resolver que le schéma n'attendait pas. Nous pourrions introduire des bugs dans notre code sans le savoir.

Et c'est pourquoi TypeScript est bénéfique. Avec TypeScript, nous avons des définitions de type dans l'objet de schéma et dans les resolvers, synchronisant ainsi les deux et rendant notre code beaucoup plus prévisible.

## Comment utiliser TypeScript et GraphQL

Dans cette section, nous allons utiliser TypeScript et GraphQL pour créer une simple API GraphQL sur un serveur Express.

### Étape 1 : Créer un dossier de projet

Vous pouvez le nommer comme vous voulez, mais nous utiliserons le dossier `graphql-ts-example` pour ce tutoriel :

```bash
mkdir graphql-ts-example
cd graphql-ts-example
npm init -y
```

### Étape 2 : Installer les dépendances

Nous utiliserons les dépendances suivantes pour ce tutoriel :

- [graphql](https://www.npmjs.com/package/graphql) : la bibliothèque JavaScript pour GraphQL
- [express](https://www.npmjs.com/package/express) : un framework web pour Node qui nous permet de créer des API et un serveur backend
- [express-graphql](https://www.npmjs.com/package/express-graphql) : pour créer un serveur GraphQL pour les API
- [ts-node](https://www.npmjs.com/package/ts-node) : pour exécuter du code TypeScript dans Node
- [typescript](https://www.npmjs.com/package/typescript) : pour compiler du code TypeScript en JavaScript
- [@types/express](https://www.npmjs.com/package/@types/express) : pour utiliser Express dans TypeScript
- [nodemon](https://www.npmjs.com/package/nodemon) : pour redémarrer le serveur lorsque des modifications sont apportées

Dans votre terminal, exécutez :

```bash
npm install graphql express express-graphql
npm install -D nodemon ts-node @types/express typescript
```

Pour tester notre API, nous utiliserons le playground GraphQL fourni par express-graphql.

### Étape 3 : Configurer nos scripts

Dans `package.json`, mettez à jour l'objet `scripts` comme suit :

```json
"scripts": {
    "start": "nodemon --exec ts-node src/index.ts",
}
```

Ajoutez également un fichier de configuration pour TypeScript, `tsconfig.json` :

```json
{
    "compilerOptions": {
        "target": "es2018",
        "module": "commonjs",
        "jsx": "preserve",
        "strict": true,
        "esModuleInterop": true,
        "lib": ["es2018", "esnext.asynciterable"]
    },
    "exclude": ["node_modules"]
}
```

Avec cela, nous pouvons exécuter notre serveur avec `npm start`.

### Étape 4 : Écrire le code

Nous allons créer un serveur Express avec une API GraphQL qui nous permet de récupérer des utilisateurs, de créer un utilisateur et de mettre à jour les données d'un utilisateur.

Créez un nouveau répertoire appelé "src" et ajoutez le fichier `index.ts` dans celui-ci. Nous avons nos imports dans le fichier comme suit :

```js
import { buildSchema } from "graphql"
import express from "express"
import { graphqlHTTP } from "express-graphql"
```

Ensuite, nous avons besoin de notre liste d'utilisateurs. Idéalement, cela viendrait d'une base de données, mais nous allons le coder en dur ici :

```js
const users = [
    { id: 1, name: "John Doe", email: "johndoe@gmail.com" },
    { id: 2, name: "Jane Doe", email: "janedoe@gmail.com" },
    { id: 3, name: "Mike Doe", email: "mikedoe@gmail.com" },
]
```

Ensuite, nous construisons le schéma GraphQL :

```js
const schema = buildSchema(`
    input UserInput {
        email: String!
        name: String!

    }

    type User {
        id: Int!
        name: String!
        email: String!
    }

    type Mutation {
        createUser(input: UserInput): User
        updateUser(id: Int!, input: UserInput): User
    }

    type Query {
        getUser(id: String): User
        getUsers: [User]
    }
`)
```

À partir de notre schéma, nous avons défini :
* une entrée utilisateur avec deux propriétés requises, qui est requise lors de la création d'un utilisateur
* un type utilisateur avec trois propriétés requises
* une mutation GraphQL où nous créons des utilisateurs et mettons à jour des utilisateurs
* et une requête GraphQL pour obtenir un utilisateur particulier ou tous les utilisateurs.

Maintenant, nous devons définir nos types TypeScript pour le typage statique :

```ts

type User = {
    id: number
    name: string
    email: string
}

type UserInput = Pick<User, "email" | "name">
```

Ensuite, nos resolvers :

```ts
const getUser = (args: { id: number }): User | undefined =>
    users.find(u => u.id === args.id)

const getUsers = (): User[] => users

const createUser = (args: { input: UserInput }): User => {
    const user = {
        id: users.length + 1,
        ...args.input,
    }
    users.push(user)

    return user
}

const updateUser = (args: { user: User }): User => {
    const index = users.findIndex(u => u.id === args.user.id)
    const targetUser = users[index]

    if (targetUser) users[index] = args.user

    return targetUser
}

const root = {
    getUser,
    getUsers,
    createUser,
    updateUser,
}
```

Et enfin, notre route Express et serveur :

```ts
const app = express()

app.use(
    "/graphql",
    graphqlHTTP({
        schema: schema,
        rootValue: root,
        graphiql: true,
    })
)

const PORT = 8000

app.listen(PORT)

console.log(`Running a GraphQL API server at http://localhost:${PORT}/graphql`)
```

Avec ce que nous avons ci-dessus, nos resolvers sont typés suivant la définition du schéma. De cette façon, nos resolvers sont synchronisés. Sur `localhost:4000/graphql`, nous pouvons voir le playground GraphQL :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-5.png)
_Playground GraphQL montrant des requêtes fonctionnelles_

Bien que nous puissions voir à quel point TypeScript est bénéfique, nous ne pouvons pas non plus nier la difficulté de rédiger des définitions de type après avoir créé un objet de schéma.

Cette base de code est petite, donc cela peut être plus facile, mais imaginez quelque chose de grand, avec de nombreux resolvers et devant créer des définitions de type pour chacun 😩

Nous avons besoin d'une meilleure façon de faire cela. Nous avons besoin de quelque chose qui nous permet de créer des définitions de type en un seul endroit, comme la source principale de vérité, et de les utiliser dans nos resolvers et objets de schéma.

## Comment utiliser TypeGraphQL pour améliorer votre GraphQL typé

Le but de [TypeGraphQL](https://typegraphql.com/) est de rendre l'utilisation du typage statique dans vos resolvers et la création de vos schémas à partir d'un seul endroit transparente.

Il vient avec sa propre syntaxe, ce qui est un autre processus d'apprentissage. Mais ce n'est pas si difficile – c'est un pas dans la bonne direction.

Améliorons notre base de code en utilisant TypeGraphQL.

Nous aurons besoin de quelques dépendances :

* [class-validator](https://www.npmjs.com/package/class-validator) : permet l'utilisation de [décorateurs](https://www.typescriptlang.org/docs/handbook/decorators.html) pour la validation
* [type-graphql](https://www.npmjs.com/package/type-graphql) : la bibliothèque TypeGraphQL elle-même, qui vous permet de créer des schémas et des resolvers avec TypeScript, en utilisant des classes et des décorateurs
* [reflect-metadata](https://www.npmjs.com/package/reflect-metadata) : pour la réflexion des types à l'exécution (en savoir plus ici : [Metadata reflection in TypeScript](http://blog.wolksoftware.com/decorators-metadata-reflection-in-typescript-from-novice-to-expert-part-4))

Dans votre terminal, exécutez :

```bash
npm install class-validator type-graphql reflect-metadata
```

Dans votre `tsconfig.json`, ajoutez ce qui suit à l'objet `compilerOptions` :

```json
"compilerOptions": {
    // ...
    "emitDecoratorMetadata": true,
    "experimentalDecorators": true,
}
```

Celles-ci sont importantes pour que TypeScript ne se plaigne pas de l'utilisation des décorateurs. Ils sont encore en mode expérimental.

Maintenant, mettons à jour notre base de code en utilisant TypeGraphQL. Créez un nouveau répertoire appelé "users". Dans celui-ci, nous aurons le schéma et les resolvers.

Créez un nouveau fichier dans "users" appelé "users.schema.ts" :

```ts
// users.schema.ts

import { Field, ObjectType, InputType } from "type-graphql"

@ObjectType()
export class User {
    @Field()
    id!: number
    @Field()
    name!: string
    @Field()
    email!: string
}

@InputType()
export class UserInput implements Pick<User, "name" | "email"> {
    @Field()
    name!: string
    @Field()
    email!: string
}
```

Tout d'abord, nous avons la classe `User`, qui est décorée avec le décorateur `ObjectType`. Cela indique à GraphQL que cette classe est un type GraphQL. En GraphQL, cela est interprété comme :

```ts
buildSchema(`
    type User {
        id: Int!
        name: String!
        email: String!
    }

    input UserInput {
        name: String!
        email: String!
    }
`)
```

Ensuite, nos resolvers. Créez un fichier `users.resolvers.ts` dans le répertoire "users" :

```ts

// users.resolvers.ts

import { Query, Resolver, Mutation, Arg } from "type-graphql"
import { UserInput, User } from "./users.schema"

@Resolver(() => User)
export class UsersResolver {
    private users: User[] = [
        { id: 1, name: "John Doe", email: "johndoe@gmail.com" },
        { id: 2, name: "Jane Doe", email: "janedoe@gmail.com" },
        { id: 3, name: "Mike Doe", email: "mikedoe@gmail.com" },
    ]

    @Query(() => [User])
    async getUsers(): Promise<User[]> {
        return this.users
    }

    @Query(() => User)
    async getUser(@Arg("id") id: number): Promise<User | undefined> {
        const user = this.users.find(u => u.id === id)
        return user
    }

    @Mutation(() => User)
    async createUser(@Arg("input") input: UserInput): Promise<User> {
        const user = {
            id: this.users.length + 1,
            ...input,
        }
        
        this.users.push(user)
        return user
    }

    @Mutation(() => User)
    async updateUser(
        @Arg("id") id: number,
        @Arg("input") input: UserInput
    ): Promise<User> {
        const user = this.users.find(u => u.id === id)
        
        if (!user) {
            throw new Error("User not found")
        }

        const updatedUser = {
            ...user,
            ...input,
        }

        this.users = this.users.map(u => (u.id === id ? updatedUser : u))

        return updatedUser
    }
}
```

Il y a quelques décorateurs à noter ici :

* il y a le décorateur `Resolver`, qui décore la classe comme un objet avec de nombreuses méthodes de résolution de requêtes et de mutations. La beauté ici est que nous définissons les requêtes et les mutations et les méthodes de résolution dans la même classe.
* il y a le décorateur `Query`, qui indique à GraphQL que ceci est une requête et la méthode de résolution respective
* il y a le décorateur `Mutation`, qui indique à GraphQL que ceci est une mutation et la méthode de résolution respective
* il y a le décorateur `Arg`, qui indique à GraphQL que cet argument est un argument GraphQL pour le resolver.

Comme vous le remarquerez, sans créer de définition de type pour l'objet `User`, nous avons simplement pu utiliser la classe exportée depuis le fichier de schéma.

Le code ci-dessus sera interprété en GraphQL comme :

```ts
buildSchema(`
    type Query {
        getUsers: [User]
        getUser(id: Int!): User
    }

    type Mutation {
        createUser(input: UserInput): User
        updateUser(id: Int!, input: UserInput): User
    }
`)

// resolvers
```

De retour dans `src/index.ts`, voici à quoi ressemble le code :

```ts
import "reflect-metadata"
import { buildSchema } from "type-graphql"
import express from "express"
import { graphqlHTTP } from "express-graphql"

import { UsersResolver } from "./users/users.resolver"

async function main() {
    const schema = await buildSchema({
        resolvers: [UsersResolver],
        emitSchemaFile: true,
    })

    const app = express()

    app.use(
        "/graphql",
        graphqlHTTP({
            schema: schema,
            graphiql: true,
        })
    )

    app.listen(8000)

    console.log("Running a GraphQL API server at http://localhost:8000/graphql")
}

main()
```

La fonction `buildSchema` provient cette fois de la bibliothèque `type-graphql`. De retour dans le playground GraphQL, nos requêtes fonctionnent comme prévu :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-6.png)
_Playground GraphQL montrant la mutation GraphQL pour créer un utilisateur_

Voici le dépôt GitHub pour ce projet : [graphql-typescript-example](https://github.com/dillionmegida/graphql-typescript-example)

## Conclusion

Dans cet article, nous avons appris ce que sont GraphQL et TypeScript, et vu les limitations de l'utilisation de GraphQL sans TypeScript.

Nous avons également vu une belle façon d'utiliser GraphQL et TypeScript ensemble – TypeGraphQL.

Si vous avez trouvé cela utile, partagez-le avec d'autres : )