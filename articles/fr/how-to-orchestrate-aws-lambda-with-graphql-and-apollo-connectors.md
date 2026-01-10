---
title: Orchestration d'AWS Lambda avec GraphQL et Apollo Connectors
subtitle: ''
author: Rob Walters
co_authors: []
series: null
date: '2025-03-25T16:12:16.340Z'
originalURL: https://freecodecamp.org/news/how-to-orchestrate-aws-lambda-with-graphql-and-apollo-connectors
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1742917115054/07184be6-5384-4861-a676-b72c06ff7c65.png
tags:
- name: GraphQL
  slug: graphql
- name: aws lambda
  slug: aws-lambda
- name: Microservices
  slug: microservices
- name: Apollo GraphQL
  slug: apollo
seo_title: Orchestration d'AWS Lambda avec GraphQL et Apollo Connectors
seo_desc: AWS Lambda is a computing service that enables you to run arbitrary code
  functions without needing to provision, manage, or scale servers. It’s often used
  in the logic tier of a multi-tier architecture to handle tasks such as processing
  files in S3 o...
---

AWS Lambda est un service de calcul qui permet d'exécuter des fonctions de code arbitraires sans avoir besoin de provisionner, gérer ou mettre à l'échelle des serveurs. Il est souvent utilisé dans la couche logique d'une architecture multi-niveaux pour gérer des tâches telles que le traitement de fichiers dans S3 ou l'exécution d'opérations CRUD sur une base de données.

AWS propose également une API Gateway, permettant aux développeurs d'invoquer des fonctions AWS Lambda, ce qui offre des fonctionnalités de sécurité et de performance améliorées comme la limitation de débit. Mais même avec l'API Gateway, vous devez coordonner ces microservices, car vos applications client ont probablement chacune des besoins de données uniques. Les données peuvent avoir besoin d'être transformées, filtrées ou combinées avant d'être retournées au client.

Ces tâches d'orchestration peuvent réduire votre productivité et prendre du temps et des efforts loin de la résolution du problème métier que votre application essaie de résoudre.

Apollo GraphQL est une couche d'orchestration d'API qui aide les équipes à livrer de nouvelles fonctionnalités plus rapidement et de manière plus indépendante en composant n'importe quel nombre de services et sources de données sous-jacents en un seul point de terminaison. Cela permet aux clients d'accéder à la demande à précisément ce dont l'expérience a besoin, indépendamment de la source de ces données.

Cet article vous apprendra à orchestrer des fonctions AWS Lambda en utilisant Apollo GraphQL. Plus précisément, voici ce que nous allons couvrir :

* [Primer GraphQL](#heading-primer-graphql)

* [Aperçu du tutoriel](#heading-aperçu-du-tutoriel)

* [Prérequis](#heading-prérequis)

* [Section 1 : Créer les ressources AWS](#heading-section-1-créer-les-ressources-aws)

* [Section 2 : Créer un connecteur Apollo](#heading-section-2-créer-un-connecteur-apollo)

* [Section 3 : Comment utiliser Apollo Sandbox](#heading-section-3-comment-utiliser-apollo-sandbox)

* [Résumé](#heading-résumé)

## Primer GraphQL

Pour ceux qui ne sont pas familiers avec GraphQL, voici un primer qui offre quelques informations sur les défis que GraphQL aborde et comment les données sont typiquement gérées via les API REST dans GraphQL avant l'émergence des Apollo Connectors. Si vous êtes familier avec GraphQL, vous pouvez sauter cette section.

GraphQL est un langage de requête pour les API. Ce langage de requête et son runtime correspondant permettent aux clients de spécifier exactement les données dont ils ont besoin, minimisant ainsi le sur-fetching et le sous-fetching.

Contrairement à REST, qui nécessite plusieurs endpoints pour diverses exigences de données, GraphQL rationalise les requêtes en une seule demande, améliorant les performances et réduisant la latence du réseau.

GraphQL utilise également un schéma fortement typé. Cela améliore la documentation de l'API et facilite la validation, la détection précoce des erreurs et les outils de développement immersifs.

Pour illustrer la différence entre les API REST et GraphQL, considérons l'appel d'API REST suivant : /user/123

Réponse :

```json
{
  "id": 123,
  "name": "Alice Johnson",
  "email": "alice@example.com",
  "phone": "555-1234",
  "address": {
    "street": "123 Main St",
    "city": "Springfield",
    "state": "IL",
    "zip": "62704"
  },
  "createdAt": "2022-01-01T12:00:00Z",
  "updatedAt": "2022-05-15T14:30:00Z",
  "isAdmin": false
}
```

Si vous n'étiez intéressé que par le nom et l'email, utiliser REST serait une perte de données retournées du réseau au client pour aucune raison. En utilisant GraphQL, la requête GraphQL pour retourner le nom et l'email serait la suivante :

```graphql
query {
  user(id: 123) {
    name
    email
  }
}
```

Le jeu de résultats est simplement les données dont le client a besoin :

```json
{
  "data": {
    "user": {
      "name": "Alice Johnson",
      "email": "alice@example.com"
    }
  }
}
```

Ceci est un exemple simple montrant l'avantage de ne pas sur-fetcher les données, mais GraphQL a de nombreux autres avantages. L'un d'eux est la séparation entre le client et le serveur. Puisque les deux parties utilisent et respectent le schéma de type GraphQL, les deux équipes peuvent opérer plus indépendamment avec le backend définissant où les données résident et le frontend ne demandant que les données dont il a besoin.

Alors, comment GraphQL sait-il comment remplir les données pour chaque champ de votre schéma ? Il le fait via des [resolvers](https://www.apollographql.com/docs/apollo-server/data/resolvers). Les resolvers peuvent récupérer des données à partir de bases de données backend ou d'API tierces telles que les API REST, gRPC, etc. Ces fonctions comprennent du code procédural compilé et maintenu pour chaque champ du schéma. Ainsi, un champ peut avoir un resolver qui interroge une API REST et un autre peut interroger un endpoint gRPC.

Pour illustrer les resolvers, considérons l'exemple ci-dessus. Ajoutons un champ, status, qui interroge une API REST pour déterminer si l'utilisateur est à temps plein, à temps partiel ou licencié.

Tout d'abord, nous avons défini notre schéma comme suit :

```graphql
type User {
  id: ID!
  name: String!
  email: String!
  status: String!  # Besoin de cela à partir d'une API REST externe
}

type Query {
  user(id: ID!): User
}
```

La requête user dans ce cas acceptera un id d'utilisateur et retournera un type User. La fonction resolver pour supporter la récupération des données ressemble à ce qui suit :

```javascript
const resolvers = {
  Query: {
    user: async (_, { id }) => {
      // Récupérer les détails de l'utilisateur à partir d'une API REST
      const userResponse = await fetch(`https://api.company.com/users/${id}`);
      const userData = await userResponse.json();

      // Récupérer le statut de l'employé à partir d'une autre API REST
      const statusResponse = await fetch(`https://api.company.com/employees/${id}/status`);
      const statusData = await statusResponse.json();

      return {
        id: userData.id,
        name: userData.name,
        email: userData.email,
        status: statusData.status, // par exemple, "Full-Time", "Part-Time", "Terminated"
      };
    },
  },
};
```

Remarquez que non seulement deux fetches sont nécessaires pour obtenir les informations que la requête nécessite, mais nous devons également écrire du code procédural et le déployer.

Une meilleure approche serait de spécifier de manière déclarative à GraphQL où se trouve l'API REST et quelles données retourner. Apollo Connectors est la solution à ce défi, simplifiant le processus et permettant d'intégrer les données de l'API REST de manière déclarative sans nécessiter de compilation et de maintenance de code.

Maintenant que vous avez une idée générale de GraphQL et des défis qu'il aborde, plongeons dans l'exemple que nous allons construire.

## Aperçu du tutoriel

Dans ce tutoriel, vous allez créer deux fonctions AWS Lambda qui retournent des informations sur les produits, décrites comme suit :

Requête de produits :

POST /2015-03-31/functions/products/invocations

Réponse :

```json
{
  "statusCode": 200,
  "body": [
    {
      "id": "RANQi6AZkUXCbZ",
      "name": "OG Olive Putter - Blade",
      "description": "The traditional Block in a blade shape is made from a solid block of Olive wood. The head weight is approximately 360 grams with the addition of pure tungsten weights. Paired with a walnut center-line and white accents colors.",
      "image": "https://keynote-strapi-production.up.railway.app/uploads/thumbnail_IMG_9102_3119483fac.png"
    },
    {
      "id": "RANYrWRy876AA5",
      "name": "Butter Knife Olive Putter- Blade",
      "description": "The traditional Block in a extremely thin blade shape (~1\") is made from a solid block of Olive wood. The head weight is approximately 330 grams with the addition of pure tungsten weights.",
      "image": "https://keynote-strapi-production.up.railway.app/uploads/thumbnail_IMG_9104_97c221e79c.png"
    },...
```

Requête de prix de produit :

POST: /2015-03-31/functions/product-price/invocations

Réponse :

```json
{
  "default_price": 49900,
  "is_active": true,
  "currency": "usd",
  "billing_schema": "per_unit",
  "recurring": {
    "interval": 0,
    "interval_count": 3
  }
}
```

Pour exposer ces deux microservices lambda, vous devez créer des déclencheurs API Gateway. Cela implique soit de configurer une API Gateway distincte pour chaque lambda, soit de les consolider sous une ou quelques instances API Gateway avec des routes spécifiées pour chaque lambda.

Créer un déclencheur peut sembler fastidieux et répétitif dans une configuration de microservices. Mais il existe une alternative disponible. Vous pourriez invoquer directement ces fonctions via REST en utilisant la permission InvokeFunction assignée à un utilisateur IAM. Cet article vous montrera cette méthode et vous guidera à travers la création de fonctions, les permissions AWS IAM nécessaires et la configuration du connecteur Apollo pour invoquer la fonction.

## Prérequis

Pour suivre ce tutoriel, vous devrez avoir une compréhension de base des fonctions AWS Lambda ainsi que de la sécurité AWS. Vous aurez également besoin d'un accès aux éléments suivants :

* Un compte AWS avec des permissions pour créer des utilisateurs et des politiques IAM

* Un compte Apollo GraphQL, vous pouvez [vous inscrire pour un plan gratuit ici](https://studio.apollographql.com/signup).

Nous utiliserons également les outils suivants :

* [VS Code](https://code.visualstudio.com/) : Microsoft VS Code est un éditeur de code source gratuit de Microsoft

* [Apollo Rover CLI](https://www.apollographql.com/docs/rover/getting-started?utm_campaign=2025-03-20_installing-rover-doc-march2025awareness&utm_medium=blog&utm_source=freecodecamp) : Rover est l'interface de ligne de commande pour gérer et maintenir les graphes

* [Apollo Studio](https://studio.apollographql.com/signup?utm_campaign=2025-03-19_studio-signup-march2025awareness&utm_medium=blog&utm_source=freecodecamp) : Un portail basé sur le web utilisé pour gérer tous les aspects de votre graphe

* [Apollo Connectors Mapping Playground](https://www.apollographql.com/connectors-mapping-playground?utm_campaign=2025-03-20_connectors-mapping-playground-march2025awareness&utm_medium=blog&utm_source=freecodecamp) : Un site web qui prend un document JSON et aide les développeurs à créer le mapping de sélection utilisé avec Apollo Connectors

## Section 1 : Créer les ressources AWS

Tout d'abord, configurons notre environnement AWS, en commençant par la sécurité. Dans notre scénario, nous allons créer un utilisateur IAM, "ConnectorUser", avec accès à une politique AWS, "ConnectorLambdaPolicy", avec les permissions minimales nécessaires pour accéder aux fonctions AWS Lambda.

Notez que vous pourriez créer des groupes d'utilisateurs et assigner des politiques de permission à ces groupes dans un environnement de production. Mais pour cet article, nous réduisons le nombre d'étapes administratives pour nous concentrer sur l'intégration principale avec GraphQL.

### Étape 1 : Créer une politique AWS

Pour créer une politique, naviguez vers IAM dans la console de gestion AWS, puis sélectionnez "Politiques" sous Gestion des accès. Cliquez sur "Créer une politique". Cela ouvrira la page de l'éditeur de politiques, comme montré ci-dessous :

![spécifier les permissions](https://cdn.hashnode.com/res/hashnode/image/upload/v1742755417676/1025d04f-a712-4311-9669-ac38bd2fee50.jpeg align="center")

Choisissez le service "Lambda" et sous le niveau d'accès, sélectionnez "InvokeFunction" dans le menu déroulant Write comme montré ci-dessous :

![InvokeFunction coché](https://cdn.hashnode.com/res/hashnode/image/upload/v1742755482285/1be204db-7b39-4c8f-ac7c-d461032f6887.jpeg align="center")

Sous le menu Ressources, vous pouvez choisir soit Tous les ARNs soit une option spécifique. Il est considéré comme une bonne pratique d'être aussi granulaire que possible lors de la définition des configurations de sécurité. Dans cet exemple, limitons notre sélection à la région "us-east-1" en cliquant sur l'option "Spécifique" puis sur "Ajouter des ARNs". Entrez "us-east-1" dans la région de la ressource et sélectionnez "N'importe quel nom de fonction".

![Dialogue spécifier ARN](https://cdn.hashnode.com/res/hashnode/image/upload/v1742755564740/99e47ac8-4ce9-4ff3-94b6-105308526f56.jpeg align="center")

Avec la politique créée, nous pouvons assigner un utilisateur IAM à cette politique.

### Étape 2 : Créer l'utilisateur IAM et attacher une politique

Cliquez sur Utilisateurs sous "Gestion des accès" puis Créer un utilisateur. Fournissez un nom pour l'utilisateur, "ConnectorUser".

![Politique de permission](https://cdn.hashnode.com/res/hashnode/image/upload/v1742755638499/ad782c39-a78f-4d68-b834-4e58dea9e35b.jpeg align="center")

Ensuite, sélectionnez "Attacher des politiques directement", choisissez la politique que nous venons de créer, "ConnectorLambdaPolicy", et cliquez sur "Créer un utilisateur".

### Étape 3 : Créer des fonctions AWS Lambda

Dans votre console AWS, créez une nouvelle fonction AWS Lambda NodeJS, "products".

![Dialogue de création de fonction AWS](https://cdn.hashnode.com/res/hashnode/image/upload/v1742754922858/b2a307c2-8b43-4417-b022-0113803a3b5d.jpeg align="center")

Sélectionnez "Node.JS" pour le runtime puis cliquez sur "Créer une fonction". Une fois créée, collez le code de la fonction [à partir de ce Gist](https://gist.github.com/RWaltersMA/25264ff22a5cbc26814a00dbb78a16e2).

![Fonction AWS montrant la source du code](https://cdn.hashnode.com/res/hashnode/image/upload/v1742755096066/90e96036-41cd-4b45-8841-0bb3acb5af6b.jpeg align="center")

Répétez ce processus, en créant une autre fonction pour "product-price" et utilisez le code de la fonction [à partir de ce Gist](https://gist.github.com/RWaltersMA/d75d9eb02264829c1392dbdf7f238bad).

## Section 2 : Créer un connecteur Apollo

Dans cette section, nous allons installer l'outil de ligne de commande Apollo Rover CLI, créer un compte Apollo Studio gratuit et cloner le dépôt Apollo Connectors. Si vous avez déjà un environnement Apollo disponible, vous pouvez sauter les étapes 1 et 2.

### Étape 1 : Installer Rover

Rover est l'interface de ligne de commande pour gérer et maintenir les graphes. Il fournit également une expérience moderne de rechargement à chaud pour développer et exécuter vos connecteurs localement. Si vous n'avez pas Rover installé, installez-le en [suivant les étapes ici](https://www.apollographql.com/docs/rover/getting-started?utm_campaign=2025-03-20_installing-rover-doc-march2025awareness&utm_medium=blog&utm_source=freecodecamp).

### Étape 2 : Créer un compte Apollo Studio gratuit

Apollo Studio est une plateforme de gestion basée sur le cloud conçue pour explorer, livrer et collaborer sur des graphes. Si vous n'avez pas de compte Apollo Studio, créez-en un sur un plan gratuit [en naviguant ici](https://studio.apollographql.com/signup?utm_campaign=2025-03-19_studio-signup-march2025awareness&utm_medium=blog&utm_source=freecodecamp).

![Apollo Studio](https://cdn.hashnode.com/res/hashnode/image/upload/v1742755870123/4b38b025-064c-4a9a-b836-53a563152e43.jpeg align="center")

### Étape 3 : Cloner le dépôt Apollo Connectors

Pour vous aider à démarrer votre premier connecteur Apollo, un dépôt GitHub fournit des connecteurs d'exemple et un script de modèle. Lorsque vous l'exécutez, ce script créera tous les fichiers et configurations nécessaires pour commencer.

Allez-y et [clonez le dépôt à partir d'ici](https://github.com/apollographql/connectors-community).

Note : Bien que ce ne soit pas obligatoire, je recommande d'utiliser VS Code, car ce dépôt utilise des fichiers de configuration spécifiques à VS Code.

### Étape 4 : Créer un fichier .env

Avant d'exécuter le script de modèle Create Connectors, créez un fichier .env localement avec une clé API utilisateur de votre Apollo Studio. Vous pouvez [créer et obtenir cette clé ici](https://studio.apollographql.com/user-settings/api-keys). Remplir ce fichier .env ajoutera cette clé API au modèle de connecteur que vous créez à l'étape suivante.

![fichier .env](https://cdn.hashnode.com/res/hashnode/image/upload/v1742755977271/860ef610-e802-4ec1-9cca-e881881a0968.jpeg align="center")

### Étape 5 : Créer votre nouveau connecteur à partir d'un modèle

Exécutez `npm start` et fournissez un emplacement pour créer le modèle de connecteur. Vous pouvez utiliser les valeurs par défaut pour les questions restantes.

![npmstart](https://cdn.hashnode.com/res/hashnode/image/upload/v1742756030015/e6c3b535-8657-4a77-b353-b8546cfa9ac5.jpeg align="center")

Ce script créera tous les fichiers nécessaires pour exécuter une instance locale Apollo GraphQL dans le répertoire spécifié. Chargez le connecteur nouvellement créé en utilisant VS Code ou votre éditeur de code préféré. Vous reviendrez à cet éditeur bientôt, mais d'abord, nous devons obtenir quelques clés d'accès d'AWS.

### Étape 6 : Créer une clé d'accès AWS

Puisque nous nous connectons à AWS en utilisant SigV4, nous devons créer une clé d'accès AWS et entrer les valeurs de la clé dans le fichier settings.json. Retournez à la console IAM AWS et sélectionnez l'utilisateur *ConnectorUser* que vous avez créé à l'étape 1. Créez une nouvelle clé d'accès en cliquant sur "Créer une clé d'accès".

Vous serez présenté avec plusieurs options quant à l'origine de l'utilisation de cette clé. Puisque nous exécutons d'abord localement, sélectionnez "Service tiers" puis continuez l'assistant jusqu'à ce que vous soyez présenté avec la clé et la clé secrète comme montré ci-dessous :

![dialogue de récupération de la clé d'accès](https://cdn.hashnode.com/res/hashnode/image/upload/v1742756092209/e7b33bd2-f6ca-4e78-bf83-8ed357860abd.jpeg align="center")

Ajoutez la clé d'accès et la clé d'accès secrète au fichier settings.json en tant que "AWS\_ACCESS\_KEY\_ID" et "AWS\_SECRET\_ACCESS\_KEY" respectivement.

![fichier de paramètres vscode](https://cdn.hashnode.com/res/hashnode/image/upload/v1742756152443/31906e19-625d-446f-adde-b9618e8df61a.jpeg align="center")

Vous devrez recharger la fenêtre puisque VS Code ne charge ces fichiers sous le répertoire .vscode qu'une seule fois.

![fenêtre de tâche vscode montrant l'option de rechargement](https://cdn.hashnode.com/res/hashnode/image/upload/v1742756203631/8fb467fc-e8de-4f16-8907-622a12017d4f.jpeg align="center")

Note : Dans cette étape, nous avons sauvegardé la clé dans le fichier settings.json. Bien que cela soit acceptable pour le développement, envisagez de sauvegarder les variables d'environnement dans des fichiers .env.

### Étape 7 : Configurer le graphe

Le fichier supergraph.yaml est utilisé pour définir tous les sous-graphes qui font partie de cette fédération. Modifiez le fichier **supergraph.yaml** comme suit :

```yaml
federation_version: =2.10.0
subgraphs:
  awsconnector:
    routing_url: http://lambda
    schema:
      file: connector.graphql
```

### Étape 8 : Configurer Apollo Router

Apollo Router prend en charge l'authentification AWS SigV4. Pour configurer le connecteur pour utiliser cela, modifiez le fichier **router.yaml** et ajoutez une section d'authentification comme suit :

```yaml
authentication:
  connector:
    sources:
      awsconnector.lambda:   # nom du sous-graphe . nom de la source du connecteur
        aws_sig_v4:
          default_chain:
            region: "us-east-1"
            service_name: "lambda"
```

Il existe d'autres options de configuration de sécurité AWS disponibles, y compris l'utilisation de l'assumption de rôle. La documentation complète pour l'authentification des sous-graphes [est disponible ici](https://www.apollographql.com/docs/graphos/routing/security/subgraph-authentication).

### Étape 9 : Construire le connecteur

Maintenant que nous avons configuré les variables d'environnement et les informations d'authentification, nous sommes prêts à construire le connecteur. Ouvrez le fichier `connector.graphql` et effacez le contenu. Ensuite, copiez le schéma d'extension suivant :

```graphql
extend schema
  @link(
    url: "https://specs.apollo.dev/federation/v2.10"
    import: ["@key"]
  )
  @link(
    url: "https://specs.apollo.dev/connect/v0.1"
    import: ["@source", "@connect"]
  )
  
  @source(
    name: "lambda"
    http: { baseURL: "https://lambda.us-east-1.amazonaws.com" }
  )
```

**Extend schema** est utilisé pour lier les directives Apollo Connectors dans le schéma actuel. Dans cet article, nous définissons l'URL de base de notre fonction lambda. Si votre API REST a des en-têtes HTTP qui s'appliquent à toutes les références de cette source, comme des restrictions de Content-Length, vous pouvez les ajouter ici dans la déclaration @source. Ensuite, définissons le schéma Product :

```graphql
type Product {
  id: ID!
  name: String
  description: String
  image: String
  price: Price
    @connect(
      source: "lambda"
      http: {
        POST: "/2015-03-31/functions/product-price/invocations"
        body: """
        product_id: $this.id
        """
      }
      selection: """
      amount: default_price
      isActive: is_active
      currency
      recurringInterval: recurring.interval -> match(
        [0,"ONE_TIME"],
        [1,"DAILY"],
        [2,"MONTHLY"],
        [3,"ANNUALLY"],
      )
      recurringCount: recurring.interval_count
      """
    )
}
```

Remarquez que notre requête Products a une directive @connect qui définit, au minimum, le nom de la source. Ici, vous pouvez ajouter la configuration spécifique HTTP dont vous avez besoin pour ce champ, comme les en-têtes d'autorisation. Dans ce scénario, puisque nous n'avons défini qu'une baseUrl dans la section extend schema, nous devons mettre l'URL spécifique pour InvokeFunction, qui est **/2015-03-31/functions/product-price/invocations**.

Le champ selection vous permet de transformer et mapper les valeurs retournées par l'API REST en utilisant la définition de mapping définie dans le champ selection. Bien qu'une discussion complète sur le mapping de sélection soit hors de portée de cet article, consultez la documentation pour un regard détaillé sur [Mapping GraphQL Responses](https://www.apollographql.com/docs/graphos/schema-design/connectors/responses?utm_campaign=2025-03-20_mapping-graphql-responses-doc-march2025awareness&utm_medium=blog&utm_source=freecodecamp). Apollo [fournit un outil en ligne gratuit](https://www.apollographql.com/connectors-mapping-playground?utm_campaign=2025-03-20_connectors-mapping-playground-march2025awareness&utm_medium=blog&utm_source=freecodecamp) qui rend la construction de mappings intuitive et rapide.

![connectors mapping playground](https://cdn.hashnode.com/res/hashnode/image/upload/v1742756290237/91d17c59-a2d0-4a22-8acf-1faec0c0f36f.jpeg align="center")

Ensuite, définissons le schéma Price et la requête products.

```graphql
type Price {
  amount: Float
  isActive: Boolean
  currency: String
  recurringInterval: RecurringInterval
  recurringCount: Int
}
enum RecurringInterval {
  ONE_TIME
  DAILY
  MONTHLY
  ANNUALLY
}

type Query {
  products: [Product]
    # https://docs.aws.amazon.com/lambda/latest/api/API_Invoke.html
    @connect(
      source: "lambda"
      http: { POST: "/2015-03-31/functions/products/invocations" }
      selection: """
      $.body {
        id
        name
        description
        image
      }
      """
    )
}
```

Maintenant, nous sommes prêts à exécuter notre connecteur et à émettre des requêtes à notre graphe ! Le script de configuration complet est disponible [à ce Gist](https://gist.github.com/RWaltersMA/e44813a89c748e175d6997f659162b33).

### Étape 10 : Exécuter le connecteur

Si vous utilisez VS Code, le dépôt inclut un fichier tasks.json qui ajoute une tâche "rover dev", qui lance Rover localement.

```json
{
    "version": "2.0.0",
    "tasks": [{
        "label": "rover dev",
        "command": "rover", // Peut être n'importe quelle autre commande shell
        "args": ["dev", "--supergraph-config","supergraph.yaml", "--router-config","router.yaml"],
        "type": "shell",
        "problemMatcher": [],
    }]
}
```

Si vous n'utilisez pas VS Code, vous pouvez démarrer votre graphe en exécutant `rover dev --supergraph-config supergraph.yaml --router-config router.yaml` à partir d'une fenêtre de terminal.

Si tout est configuré correctement, vous verrez ce qui suit :

![exécution de la commande rover dev](https://cdn.hashnode.com/res/hashnode/image/upload/v1742756354078/9fab875a-d064-4723-be91-8ca0d6243b59.jpeg align="center")

## Section 3 : Comment utiliser Apollo Sandbox

La commande `rover dev` que vous avez lancée à l'étape précédente configure une instance locale d'Apollo Router pour le [mode développement](https://www.apollographql.com/docs/graphos/reference/router/configuration?utm_campaign=2025-03-20_router-configuration-doc-march2025awareness&utm_medium=blog&utm_source=freecodecamp#-dev). Ce mode facilite la création, l'exécution et le débogage de requêtes GraphQL ad-hoc par les développeurs en utilisant le portail web Apollo Sandbox. Ce portail est situé à [http://localhost:4000](http://localhost:4000) par défaut.

Lancez le portail et cliquez sur le champ products. Cela remplira le panneau Operation avec tous les champs disponibles dans le schéma. Dans le panneau operation, vous pouvez modifier et construire votre requête GraphQL. Cliquer sur le bouton Run (qui affiche le nom de la requête, Products, dans notre exemple) exécutera la requête et affichera les résultats dans le panneau Response, comme illustré dans la figure ci-dessus.

Dans cet exemple, vous pouvez voir que les données ont été retournées par notre fonction AWS Lambda. Pour confirmer, vous pouvez afficher le plan de requête en sélectionnant "Query Plan" dans le menu déroulant Response.

![élément de menu du plan de requête](https://cdn.hashnode.com/res/hashnode/image/upload/v1742756499055/822467d7-0694-423e-baef-450a8d0dd64e.jpeg align="center")

Le plan de requête illustre l'orchestration de nos deux fonctions AWS Lambda qui récupèrent les données de produit et de prix de produit.

![plan de requête](https://cdn.hashnode.com/res/hashnode/image/upload/v1742756540147/af32d615-029a-4f6f-a489-96ee9950e630.jpeg align="center")

Une fonctionnalité de débogage utile est le débogueur de connecteurs, disponible dans le menu déroulant comme montré dans la figure précédente.

![débogueur montrant l'aperçu de la requête](https://cdn.hashnode.com/res/hashnode/image/upload/v1742756614481/c9b311e3-ab5d-4927-9457-e9a7d242fbdf.jpeg align="center")

Le débogueur de connexion fournit une vue complète de la requête HTTP, y compris les en-têtes, le corps, le code de réponse et le mapping de sélection utilisé dans la requête. Si vous rencontrez des difficultés à exécuter des requêtes, utilisez ce débogueur, il vous fera gagner beaucoup de temps.

## Résumé

Dans cet article, vous avez appris à :

* Configurer un utilisateur IAM AWS, des politiques et des fonctions Lambda

* Créer un connecteur Apollo pour obtenir des données à partir d'une fonction AWS Lambda

* Configurer le routeur Apollo

* Exécuter et déboguer des requêtes en utilisant Apollo Sandbox

L'intégration d'AWS Lambda avec Apollo Connectors offre une méthode simplifiée, sans resolver, pour incorporer des fonctions cloud dans votre API GraphQL. En utilisant Apollo Connectors, vous pouvez lier de manière déclarative des fonctions Lambda basées sur REST à votre supergraphe tout en assurant une authentification sécurisée avec AWS SigV4.

Vous pouvez en apprendre davantage sur Apollo Connectors à partir des ressources suivantes :

1. Tutoriel : [GraphQL rencontre REST, avec Apollo Connectors](https://www.apollographql.com/tutorials/connectors-intro-rest?utm_campaign=2025-03-20_connectors-intro-rest-odyssey-march2025awareness&utm_medium=blog&utm_source=freecodecamp)

2. Blog : Découvrez comment Apollo Connectors s'intègre avec Apollo Federation à travers les insights du fondateur et CTO d'Apollo : [Orchestration d'API REST avec GraphQL](https://www.apollographql.com/blog/api-orchestration-with-graphql?utm_campaign=2025-03-20_api-orchestration-with-graphql-march2025awareness&utm_medium=blog&utm_source=freecodecamp).

3. Blog : Plongez dans le voyage d'ingénierie derrière Apollo Connectors et le processus de leur création : [Notre voyage vers Apollo Connectors](https://www.apollographql.com/blog/our-journey-to-apollo-connectors?utm_campaign=2025-03-20_our-journey-to-apollo-connectors-march2025awareness&utm_medium=blog&utm_source=freecodecamp)

4. Webinaire : [Webinaire de lancement GA d'Apollo Connectors](https://www.apollographql.com/events/new-innovations-from-apollo-dont-miss-out?utm_campaign=2025-03-20_new-innovations-from-apollo-dont-miss-out-march2025awareness&utm_medium=blog&utm_source=freecodecamp)