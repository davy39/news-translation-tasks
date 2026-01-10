---
title: Comment construire de meilleures API dans Express avec OpenAPI
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-04-02T20:18:31.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-explicit-apis-with-openapi
coverImage: https://cdn-media-2.freecodecamp.org/w1280/6065d95e9618b008528ab4a6.jpg
tags:
- name: api
  slug: api
- name: Express
  slug: express
- name: node js
  slug: node-js
- name: REST API
  slug: rest-api
seo_title: Comment construire de meilleures API dans Express avec OpenAPI
seo_desc: 'By Alain Perkaz

  In this article, I will share how to build robust REST APIs in Express. First, I
  will present some of the challenges of building REST APIs and then propose a solution
  using open standards.

  This article won''t be an introduction to Node...'
---

Par Alain Perkaz

Dans cet article, je vais partager comment construire des API REST robustes dans Express. Tout d'abord, je vais présenter certains des défis de la construction d'API REST, puis proposer une solution utilisant des standards ouverts.

Cet article ne sera pas une introduction à [Node.js](https://nodejs.org/en/), [Express.js](https://expressjs.com/), ou aux [REST API](https://www.freecodecamp.org/news/rest-apis/). Assurez-vous de consulter les liens avant d'approfondir si vous avez besoin d'un rappel. 🧏

J'adore l'écosystème Node.js pour sa flexibilité et sa facilité d'utilisation. La communauté est dynamique, et en quelques minutes, vous pouvez configurer une API REST en utilisant le langage que vous connaissez déjà.

Il y a une grande valeur à partager le même langage de programmation entre le back-end et le front-end d'une application. Cela facilite la navigation dans le codebase d'une application avec moins de [changement de contexte](https://blog.rescuetime.com/context-switching/). Les développeurs full-stack peuvent se déplacer rapidement dans la stack, et le [partage de code](https://betterprogramming.pub/sharing-logic-components-between-frontend-and-backend-repositories-6fdc1f9cb850) devient un jeu d'enfant.

Cela dit, lorsque les MVPs deviennent des applications de production à part entière et que les équipes de développement grandissent, cette flexibilité crée également des défis.

## Défis de travail avec les API REST

Il y a de nombreux défis à relever lorsque les codebases et les équipes grandissent, peu importe la stack technologique utilisée.

Je vais réduire ces défis aux applications Express.js qui contiennent une logique métier exposée via une API REST.

Quelle que soit la nature des consommateurs de l'API (pages web, applications mobiles, backends tiers), ils sont susceptibles de rencontrer un (ou plusieurs) des défis suivants à mesure qu'ils grandissent :

### 1. ⚠️ Il est plus difficile de faire des changements

Lorsque le contrat n'est pas explicite, il devient plus difficile de faire des changements des deux côtés de l'API REST.

Par exemple, vous pouvez avoir un endpoint REST qui retourne le nom d'un utilisateur spécifique. Dans la prochaine fonctionnalité, vous pourriez avoir besoin de le modifier pour retourner également l'âge. Cela pourrait silencieusement casser l'application web et l'application mobile.

Vous pouvez mettre en place des tests d'intégration pour atténuer ce problème, mais vous dépendrez toujours fortement des développeurs pour couvrir manuellement tous les cas limites. Cela prend beaucoup de temps et d'efforts, et vous n'êtes jamais certain à 100% que les changements ne casseront pas l'application.

### 2. 📖 Manque de documentation (à jour)

La documentation est un autre sujet sensible lors de la construction d'API REST. Je suis un fervent croyant que, dans la plupart des cas, le code devrait servir de documentation suffisante.

Cela dit, les API REST peuvent devenir complexes, et vérifier la sécurité, les paramètres et les réponses possibles pour chaque endpoint dans le code devient fastidieux et chronophage. Cela ralentit la vitesse de développement, et des bugs s'immiscent dans le système.

Même si l'équipe s'engage à maintenir manuellement la documentation à jour dans un document séparé du code, il est difficile d'être certain à 100% qu'elle reflète le code.

### 3. 📩 API publiques

Cela ne s'appliquera pas à toutes les applications, mais une application peut avoir besoin d'exposer un ensemble de fonctionnalités à un tiers dans certains cas. En faisant cela, le tiers peut construire des fonctionnalités principales sur la base de nos API exposées.

Cela signifie que nous ne pouvons pas modifier ces API au même rythme que nous mettons à jour nos API privées. L'application tierce peut casser, et c'est quelque chose que nous devons éviter à tout prix.

Ce que les API publiques exposent doit être explicite et simple à développer, afin de limiter la quantité de communication aller-retour nécessaire entre les équipes de développeurs internes et externes.

### 4. ✏️ Tests d'intégration manuels

Lorsque les applications grandissent de manière organique sans un plan approfondi, il est probable que ce que l'API fournit et ce que le consommateur de l'API attend soit enfoui profondément dans le code.

Ce n'est pas un gros problème lorsque vous avez un petit nombre d'endpoints pour un usage interne. Mais à mesure que la surface de l'API grandit, la modification des endpoints existants nécessite de suivre des traces à travers tout le système pour s'assurer que ce que le consommateur s'attend à recevoir est égal à ce qui est fourni.

Cela peut être atténué en maintenant des tests d'intégration entre les parties du système qui communiquent avec l'API REST. Mais le faire manuellement est un travail énorme et, lorsqu'il est mal fait, fournit une fausse sécurité que le système fonctionnera correctement.

## Solution proposée

Nous avons vu certains des défis inhérents à la construction d'API REST. Dans la section suivante, nous allons construire un exemple de projet Express qui aborde ces défis en utilisant des standards ouverts.

### Spécification standard de l'API

Les défis décrits dans la section précédente existent depuis longtemps, il est donc avantageux de se pencher sur des solutions existantes, plutôt que de réinventer la roue.

Il y a eu plusieurs tentatives pour standardiser les définitions d'API REST ([RAML](https://raml.org/), [JsonAPI](https://jsonapi.org/), [OpenAPI](https://www.openapis.org/)...). Ces projets ont pour objectif commun de faciliter la définition par les développeurs du comportement de leurs API, afin que les serveurs et les clients dans plusieurs langages puissent "parler une langue commune".

Avoir une sorte de spécification formelle de l'API résout de nombreux défis, car dans de nombreux cas, les SDK clients, les tests, les serveurs mock et la documentation peuvent être générés automatiquement à partir de ces spécifications.

L'un de mes préférés est OpenAPI (anciennement Swagger). Il a une grande communauté et de nombreux outils pour Express. Cela peut ne pas être le meilleur outil pour chaque projet d'API REST, alors n'oubliez pas de faire des recherches supplémentaires pour vous assurer que les outils et le support autour de cette spécification ont du sens dans votre cas.

### Contexte pour notre exemple

Pour les besoins de cet exemple, supposons que nous construisons une application de gestion de liste de tâches. L'utilisateur a accès à une application web où il peut récupérer, créer, modifier et supprimer des tâches, qui sont persistées dans le backend.

Dans ce cas, le backend sera une application Express.js qui exposera via une API REST les fonctionnalités suivantes :

* Récupérer les tâches : **[GET] /todos**
* Créer une tâche : **[POST] /todos**
* Modifier une tâche : **[PUT] /todos/:id**
* Supprimer une tâche : **[DELETE] /todos/:id**

Ceci est une simplification excessive des fonctionnalités dont une application de gestion de tâches aura besoin, mais cela servira à montrer comment nous pouvons surmonter les défis présentés ci-dessus dans un contexte réel.

### Implémentation

Bien, maintenant que nous avons introduit les standards ouverts pour les définitions d'API et un contexte, implémentons une application de tâches Express en relevant les défis précédents.

Nous allons utiliser OpenAPI avec la bibliothèque Express [**express-openapi**](https://github.com/kogosoftwarellc/open-api/tree/master/packages/express-openapi). Notez que cette bibliothèque fournit des fonctionnalités avancées (validation des réponses, authentification, configuration des middlewares...) au-delà de la portée de cet article.

Le code complet est disponible dans **[ce dépôt](https://github.com/aperkaz/express-open-api)**.

1. Initialiser un squelette Express et initialiser un dépôt Git :

`npx express-generator --no-view --git todo-app`
`cd ./todo-app`
`git init`
`git add .; git commit -m "Initial commit";`


2. Ajouter la bibliothèque OpenAPI Express, **[express-openapi](https://github.com/kogosoftwarellc/open-api/tree/master/packages/express-openapi)** :

`npm i express-openapi -s`

```
// ./app.js

...

app.listen(3030);

...

// Routes OpenAPI
initialize({
  app,
  apiDoc: require("./api/api-doc"),
  paths: "./api/paths",
});

module.exports = app;
```

3. Ajouter le schéma de base OpenAPI.

Notez que le schéma définit le type d'un **Todo**, qui sera référencé dans les gestionnaires de routes.

```javascript
// ./api/api-doc.js

const apiDoc = {
  swagger: "2.0",
  basePath: "/",
  info: {
    title: "API de l'application de tâches.",
    version: "1.0.0",
  },
  definitions: {
    Todo: {
      type: "object",
      properties: {
        id: {
          type: "number",
        },
        message: {
          type: "string",
        },
      },
      required: ["id", "message"],
    },
  },
  paths: {},
};

module.exports = apiDoc;
```



4. Ajouter les [gestionnaires](https://github.com/kogosoftwarellc/open-api/tree/master/packages/express-openapi#getting-started) de routes.

Chaque gestionnaire déclare quelles opérations il supporte (GET, POST...), les callbacks pour chaque opération, et le schéma **apiDoc** OpenAPI pour ce gestionnaire.

```javascript
// ./api/paths/todos/index.js
module.exports = function () {
  let operations = {
    GET,
    POST,
    PUT,
    DELETE,
  };

  function GET(req, res, next) {
    res.status(200).json([
      { id: 0, message: "Première tâche" },
      { id: 1, message: "Deuxième tâche" },
    ]);
  }

  function POST(req, res, next) {
    console.log(`Sur le point de créer une tâche : ${JSON.stringify(req.body)}`);
    res.status(201).send();
  }

  function PUT(req, res, next) {
    console.log(`Sur le point de mettre à jour la tâche avec l'id : ${req.query.id}`);
    res.status(200).send();
  }

  function DELETE(req, res, next) {
    console.log(`Sur le point de supprimer la tâche avec l'id : ${req.query.id}`);
    res.status(200).send();
  }

  GET.apiDoc = {
    summary: "Récupérer les tâches.",
    operationId: "getTodos",
    responses: {
      200: {
        description: "Liste des tâches.",
        schema: {
          type: "array",
          items: {
            $ref: "#/definitions/Todo",
          },
        },
      },
    },
  };

  POST.apiDoc = {
    summary: "Créer une tâche.",
    operationId: "createTodo",
    consumes: ["application/json"],
    parameters: [
      {
        in: "body",
        name: "todo",
        schema: {
          $ref: "#/definitions/Todo",
        },
      },
    ],
    responses: {
      201: {
        description: "Créé",
      },
    },
  };

  PUT.apiDoc = {
    summary: "Mettre à jour une tâche.",
    operationId: "updateTodo",
    parameters: [
      {
        in: "query",
        name: "id",
        required: true,
        type: "string",
      },
      {
        in: "body",
        name: "todo",
        schema: {
          $ref: "#/definitions/Todo",
        },
      },
    ],
    responses: {
      200: {
        description: "Mis à jour avec succès",
      },
    },
  };

  DELETE.apiDoc = {
    summary: "Supprimer une tâche.",
    operationId: "deleteTodo",
    consumes: ["application/json"],
    parameters: [
      {
        in: "query",
        name: "id",
        required: true,
        type: "string",
      },
    ],
    responses: {
      200: {
        description: "Supprimé",
      },
    },
  };

  return operations;
};
```

5. Ajouter la documentation autogénérée, **[swagger-ui-express](https://github.com/scottie1984/swagger-ui-express)** :


```
npm i swagger-ui-express -s
```

```
// ./app.js

...

// UI OpenAPI
app.use(
  "/api-documentation",
  swaggerUi.serve,
  swaggerUi.setup(null, {
    swaggerOptions: {
      url: "http://localhost:3030/api-docs",
    },
  })
);

module.exports = app;
```

Et voici ce que nous obtiendrons :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-23.png)
_Documentation SwaggerUi autogénérée, à l'adresse http://localhost:3030/api-documentation_

🎉 **Félicitations !**

Si vous êtes arrivé jusqu'ici, vous devriez avoir une application Express entièrement fonctionnelle, entièrement intégrée avec OpenAPI.

En utilisant le schéma disponible à l'adresse _[http://localhost:3030/api-docs](http://localhost:3030/api-docs)_, nous pouvons maintenant facilement générer des [tests](https://nordicapis.com/generating-web-api-tests-from-an-openapi-specification/), un [serveur mock](https://github.com/stoplightio/prism), des [types](https://github.com/drwpow/openapi-typescript) ou même un [client](https://phrase.com/blog/posts/using-openapi-to-generate-api-client-code/) !

## Conclusion

Nous n'avons fait qu'effleurer la surface de ce qui est possible avec OpenAPI. Mais j'espère que cet article a éclairé comment un schéma de définition d'API standard peut aider à la visibilité, aux tests, à la documentation et à la confiance globale lors de la construction d'API REST.

Merci d'être resté jusqu'à la fin !

Je construis actuellement [_**taggr**_](https://taggr.ai/)_,_ une application desktop multiplateforme qui permet aux utilisateurs de **redécouvrir** leurs **souvenirs** numériques tout en préservant leur **vie privée**.

L'open-alpha arrive bientôt sur Linux, Windows et Mac OS. Assurez-vous de consulter la [page web](https://taggr.ai/) et de vous [inscrire](https://taggr.us18.list-manage.com/subscribe/post?u=482d473aa1e4dedadc89fb3e2&id=aa6a10c164) pour ne pas la manquer !