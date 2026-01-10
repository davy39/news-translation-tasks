---
title: Comment construire un système back-end complet avec Serverless
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-27T09:33:44.000Z'
originalURL: https://freecodecamp.org/news/complete-back-end-system-with-serverless
coverImage: https://www.freecodecamp.org/news/content/images/2019/12/thumbnail.png
tags:
- name: api
  slug: api
- name: AWS
  slug: aws
- name: Backend Development
  slug: backend-development
- name: serverless
  slug: serverless
- name: serverless framework
  slug: serverless-framework
seo_title: Comment construire un système back-end complet avec Serverless
seo_desc: 'By Sam Williams

  This article will teach you how to build and deploy everything you need to be able
  to build a back-end for your application. We''ll be using AWS to host all of this
  and deploying it all using the Serverless Framework.

  By the end of thi...'
---

Par Sam Williams

Cet article vous apprendra à construire et déployer tout ce dont vous avez besoin pour créer un back-end pour votre application. Nous utiliserons AWS pour héberger tout cela et le déployer en utilisant le Framework Serverless.

À la fin de cet article, vous saurez comment :

* [Configurer votre compte AWS pour travailler avec le Framework Serverless](#heading-installation)
* [Configurer un projet Serverless et déployer une Lambda](#)
* [Créer un stockage cloud privé avec un bucket S3 et téléverser des fichiers depuis votre ordinateur](#)
* [Déployer une API en utilisant API Gateway et AWS Lambda](#)
* [Créer une table de base de données serverless avec AWS DynamoDB](#)
* [Créer une API pour obtenir des données depuis votre table DynamoDB](#)
* [Créer une API pour ajouter des données à votre table DynamoDB](#)
* [Créer des APIs pour stocker des fichiers et obtenir des fichiers depuis votre bucket S3](#)
* [Sécuriser tous vos endpoints API avec des clés API](#)

Pouvoir faire toutes ces choses vous donne la capacité de créer toutes les fonctionnalités nécessaires pour la plupart des back-ends d'applications.

<a class="anchor" id="heading-installation"></a>

# **Installation Serverless avec AWS**

Le Framework Serverless est un outil que nous pouvons utiliser en tant que développeurs pour configurer et déployer des services depuis nos ordinateurs. Il y a un peu de configuration à faire pour permettre à tout cela de fonctionner ensemble et cette section vous montrera comment faire.

[Contenu intégré](https://www.youtube.com/embed/videoseries?list=PLmexTtcbIn_gP8bpsUsHfv-58KsKPsGEo)

Pour permettre à Serverless de travailler sur votre compte, vous devez configurer un utilisateur pour cela. Pour ce faire, naviguez dans AWS et recherchez "IAM" (Identity and Access Management).

Une fois sur la page IAM, cliquez sur _Utilisateurs_ dans la liste sur le côté gauche. Cela ouvrira la liste des utilisateurs de votre compte. À partir de là, nous cliquerons sur _Ajouter un utilisateur_.

Nous devons créer un utilisateur qui a un _accès programmatique_ et j'ai appelé mon utilisateur _ServerlessAccount_, mais le nom n'a pas trop d'importance.

![Image](https://completecoding.io/content/images/2019/08/createUser-1.png)

Ensuite, nous devons donner à l'utilisateur certaines autorisations. Sur l'écran des autorisations, sélectionnez _Joindre des stratégies existantes directement_ puis sélectionnez _AdministratorAccess_. Cela donnera au Framework Serverless l'autorisation de créer toutes les ressources dont il a besoin.

Nous n'avons pas besoin d'ajouter de tags, donc nous pouvons passer directement à _Revue_.

![Image](https://completecoding.io/content/images/2019/08/credential.png)

Sur la fenêtre de révision, vous verrez que l'utilisateur a reçu un _ID de clé d'accès_ et une _clé d'accès secrète_. Nous en aurons besoin dans la prochaine partie, alors gardez cette page ouverte.

### **Installation et configuration de Serverless**

Maintenant que nous avons créé notre utilisateur, nous devons installer le Framework Serverless sur notre machine.

Ouvrez un terminal et exécutez cette commande pour installer Serverless globalement sur votre ordinateur. Si vous n'avez pas NodeJS installé, consultez [cette page](https://nodejs.org/en/download/).

```
npm install -g serverless
```

Maintenant que nous avons installé Serverless, nous devons configurer les identifiants pour que Serverless les utilise. Exécutez cette commande, en mettant votre _ID de clé d'accès_ et votre _clé d'accès secrète_ aux endroits appropriés :

```js
serverless config credentials --provider aws --key ${Votre ID de clé d'accès} --secret ${Votre clé d'accès secrète} --profile serverlessUser
```

Une fois cela exécuté, vous êtes prêt à utiliser Serverless.

<a class="anchor" id="firstlambda"></a>

# **Déploiement de votre première AWS Lambda**

Avec notre serverlessUser configuré, nous voulons déployer quelque chose en utilisant le Framework Serverless. Nous pouvons utiliser des modèles Serverless pour configurer un projet de base que nous pouvons déployer. Ce sera la base de l'ensemble de ce projet Serverless.

[Contenu intégré](https://www.youtube.com/embed/sku9Rrci-tE?feature=oembed)

Dans votre terminal, nous pouvons créer un projet Serverless à partir d'un modèle. Cette commande créera un projet Serverless NodeJS dans le dossier `myServerlessProject` :

```
serverless create --template aws-nodejs --path myServerlessProject

```

Si vous ouvrez maintenant le dossier dans votre éditeur de code, nous pouvons voir ce que nous avons créé.

![Image](https://completecoding.io/content/images/2019/12/folderStruct.png)

Nous avons deux fichiers à discuter : `handler.js` et `serverless.yml`

### **handler.js**

Ce fichier est une fonction qui sera téléversée en tant que fonction Lambda sur votre compte AWS. Les fonctions Lambda sont géniales et nous en utiliserons beaucoup plus tard dans la série.

### **serverless.yml**

Ce fichier est très important pour nous. C'est ici que toute la configuration pour notre déploiement est définie. Il indique à Serverless quel runtime utiliser, quel compte déployer, et quoi déployer.

Nous devons apporter une modification à ce fichier pour que notre déploiement fonctionne correctement. Dans l'objet `provider`, nous devons ajouter une nouvelle ligne `profile: serverlessUser`. Cela indique à Serverless d'utiliser les identifiants AWS que nous avons créés dans la dernière section.

Nous pouvons faire défiler jusqu'à `functions` et voir que nous avons une fonction appelée `hello` qui pointe vers la fonction dans le fichier `handler.js`. Cela signifie que nous allons déployer cette fonction Lambda dans le cadre de ce projet.

Nous en apprendrons beaucoup plus sur ce fichier `serverless.yml` plus tard dans cet article.

## **Déploiement de notre projet**

Maintenant que nous avons examiné les fichiers, il est temps de faire notre premier déploiement. Ouvrez un terminal et naviguez jusqu'à notre dossier de projet. Le déploiement est aussi simple que de taper :

```
serverless deploy

```

Cela prend un certain temps, mais une fois terminé, nous pouvons vérifier que tout a été déployé avec succès.

Ouvrez votre navigateur et naviguez jusqu'à votre compte AWS. Recherchez `Lambda` et vous verrez une liste de toutes vos fonctions Lambda. (Si vous n'en voyez aucune, vérifiez que votre région est définie sur `N. Virginia`). Vous devriez voir la Lambda `myserverlessproject-dev-hello` qui contient le code exact du fichier `handler.js` dans votre dossier de projet.

<a class="anchor" id="s3"></a>

# **Déploiement d'un bucket S3 et téléversement de fichiers**

Dans cette section, nous allons apprendre comment déployer un bucket Amazon S3 puis synchroniser des fichiers depuis notre ordinateur. C'est ainsi que nous pouvons commencer à utiliser S3 comme stockage cloud pour nos fichiers.

[Contenu intégré](https://www.youtube.com/embed/8dc72i41r1A?feature=oembed)

Ouvrez le fichier `serverless.yml` et supprimez toutes les lignes commentées. Faites défiler jusqu'à la fin du fichier et ajoutez le code suivant pour inclure nos ressources S3 :

```
resources:
    Resources:
        DemoBucketUpload:
            Type: AWS::S3::Bucket
            Properties:
                BucketName: EnterAUniqueBucketNameHere

```

Changez le nom du bucket et nous sommes prêts à déployer à nouveau. Ouvrez à nouveau votre terminal et exécutez `serverless deploy`. Vous pouvez obtenir une erreur indiquant que le nom du bucket n'est pas unique, auquel cas vous devrez changer le nom du bucket, enregistrer le fichier et réexécuter la commande.

Si c'est un succès, nous pouvons alors voir notre nouveau bucket S3 dans notre console AWS via notre navigateur. Recherchez `S3` puis vous devriez voir votre bucket nouvellement créé.

## **Synchronisation de vos fichiers**

Avoir un bucket est génial, mais maintenant nous devons mettre des fichiers dans le bucket. Nous allons utiliser un plugin Serverless appelé S3 Sync pour faire cela pour nous. Pour ajouter ce plugin à notre projet, nous devons définir les plugins. Après votre objet provider, ajoutez ce code :

```
plugins:
    - serverless-s3-sync
```

Ce plugin nécessite également une configuration personnalisée, nous ajoutons donc un autre champ à notre fichier `serverless.yml`, en changeant le nom du bucket par le vôtre :

```
custom:
    s3Sync:
        - bucketName: YourUniqueBucketName
          localDir: UploadData

```

Cette section de code indique au plugin S3 Sync de téléverser le contenu du dossier `UploadData` vers notre bucket. Nous n'avons pas actuellement ce dossier, donc nous devons le créer et ajouter quelques fichiers. Vous pouvez ajouter un fichier texte, une image, ou ce que vous voulez téléverser, assurez-vous simplement qu'il y a au moins 1 fichier dans le dossier.

La dernière chose que nous devons faire est d'installer le plugin. Heureusement, tous les plugins Serverless sont également des packages npm, donc nous pouvons l'installer en exécutant `npm install --save-dev serverless-s3-sync` dans notre terminal.

Comme nous l'avons fait auparavant, nous pouvons maintenant exécuter `serverless deploy` et attendre que le déploiement soit terminé. Une fois terminé, nous pouvons retourner dans notre navigateur et dans notre bucket et nous devrions voir tous les fichiers que nous avons mis dans le dossier `UploadData` dans notre projet.

![Image](https://completecoding.io/content/images/2019/12/Screenshot-2019-12-10-at-07.12.07.png)

<a class="anchor" id="api"></a>

# **Création d'une API avec Lambda et API Gateway**

Dans cette section, nous apprendrons à faire l'une des choses les plus utiles avec Serverless : créer une API. Créer une API vous permet de faire tant de choses, de la récupération de données depuis des bases de données, du stockage S3, de l'appel d'autres APIs, et bien plus encore !

[Contenu intégré](https://www.youtube.com/embed/Jruqo0KVOWk?feature=oembed)

Pour créer l'API, nous devons d'abord créer une nouvelle fonction Lambda pour gérer la requête. Nous allons faire plusieurs Lambdas, donc nous allons créer un dossier `lambdas` dans notre projet avec deux sous-dossiers, `common` et `endpoints`.

![Image](https://completecoding.io/content/images/2019/12/Screenshot-2019-12-10-at-07.47.27.png)

À l'intérieur du dossier endpoints, nous pouvons ajouter un nouveau fichier appelé `getUser.js`. Cette API permettra à quelqu'un de faire une requête et de récupérer des données basées sur l'ID d'un utilisateur. Voici le code pour l'API :

```js
const Responses = require('../common/API_Responses');

exports.handler = async event => {
    console.log('event', event);

    if (!event.pathParameters || !event.pathParameters.ID) {
        // échoué sans ID
        return Responses._400({ message: 'ID manquant dans le chemin' });
    }

    let ID = event.pathParameters.ID;

    if (data[ID]) {
        // retourner les données
        return Responses._200(data[ID]);
    }

    // échoué car ID non présent dans les données
    return Responses._400({ message: 'aucun ID dans les données' });
};

const data = {
    1234: { name: 'Anna Jones', age: 25, job: 'journaliste' },
    7893: { name: 'Chris Smith', age: 52, job: 'enseignant' },
    5132: { name: 'Tom Hague', age: 23, job: 'plâtrier' },
};

```

Si la requête ne contient pas d'ID, nous retournons une réponse d'échec. Si des données existent pour cet ID, nous retournons ces données. Si aucune donnée n'existe pour cet ID utilisateur, nous retournons également une réponse d'échec.

Comme vous l'avez peut-être remarqué, nous importons l'objet `Responses` depuis `API_Responses`. Ces réponses seront communes à toutes les APIs que nous créerons, donc rendre ce code importable est une bonne idée. Créez un nouveau fichier appelé `API_Responses.js` dans le dossier `common` et ajoutez ce code :

```js
const Responses = {
    _200(data = {}) {
        return {
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Methods': '*',
                'Access-Control-Allow-Origin': '*',
            },
            statusCode: 200,
            body: JSON.stringify(data),
        };
    },

    _400(data = {}) {
        return {
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Methods': '*',
                'Access-Control-Allow-Origin': '*',
            },
            statusCode: 400,
            body: JSON.stringify(data),
        };
    },
};

module.exports = Responses;

```

Cet ensemble de fonctions est utilisé pour simplifier la création de la réponse correcte nécessaire lors de l'utilisation d'une Lambda avec API Gateway (que nous ferons dans un instant). Les méthodes ajoutent des en-têtes, un code de statut, et convertissent en chaîne toute donnée devant être retournée.

Maintenant que nous avons le code pour notre API, nous devons le configurer dans notre fichier `serverless.yml`. Faites défiler jusqu'à la section `functions` du fichier `serverless.yml`. Dans la dernière partie de ce guide, nous avons déployé la fonction `hello`, mais nous n'en avons plus besoin. Supprimez l'objet functions et remplacez-le par ceci :

```yml
functions:
    getUser:
        handler: lambdas/endpoints/getUser.handler
        events:
            - http:
                  path: get-user/{ID}
                  method: GET
                  cors: true

```

Ce code crée une nouvelle fonction Lambda appelée `getUser` qui se trouve dans le fichier `lambdas/getUser` avec la méthode `handler`. Nous définissons ensuite les événements qui peuvent déclencher l'exécution de cette fonction lambda.

Pour transformer une Lambda en API, nous pouvons ajouter un événement `http`. Cela indique à Serverless d'ajouter une API Gateway à ce compte, puis nous pouvons définir le point de terminaison de l'API en utilisant `path`. Dans ce cas, `get-user/{ID}` signifie que l'URL sera `https://${something-provided-by-API-Gateway}/get-user/{ID}`, où l'ID est passé à la Lambda en tant que paramètre de chemin. Nous définissons également la méthode sur `GET` et activons CORS afin que nous puissions accéder à ce point de terminaison depuis une application front-end si nous le souhaitons.

Nous pouvons maintenant déployer à nouveau, et cette fois nous pouvons utiliser la commande raccourcie `sls deploy`. Cela ne sauve que quelques caractères, mais aide à éviter beaucoup de fautes de frappe. Une fois cela terminé, nous obtiendrons une sortie qui inclut également une liste de points de terminaison. Nous pouvons copier notre point de terminaison et nous rendre sur un navigateur pour le tester.

![Image](https://completecoding.io/content/images/2019/12/Screenshot-2019-12-10-at-07.19.00.png)

Si nous collons l'URL de notre API dans notre navigateur et que nous ajoutons un ID à la fin de 5132, nous devrions obtenir une réponse de `{ name: 'Tom Hague', age: 23, job: 'plasterer' }`. Si nous entrons un ID différent comme 1234, nous obtiendrons des données différentes, mais entrer un ID de 7890 ou ne pas entrer d'ID retournera une erreur.

Si nous voulons ajouter plus de données à notre API, nous pouvons simplement ajouter une nouvelle ligne à l'objet data dans le fichier `getUser.js`. Nous pouvons ensuite exécuter une commande spéciale qui ne déploie qu'une seule fonction, `sls deploy -f ${functionName}`. Pour nous, cela donne :

```
sls deploy -f getUser

```

Si vous faites maintenant une requête en utilisant l'ID des nouvelles données, l'API retournera ces nouvelles données au lieu d'une erreur.

<a class="anchor" id="dynamo"></a>

# **Création d'une base de données sur AWS**

DynamoDB est une base de données non relationnelle, entièrement hébergée sur AWS. C'est la solution parfaite pour stocker des données que vous devez accéder et mettre à jour régulièrement. Dans cette section, nous allons apprendre comment créer une table DynamoDB avec Serverless.

[Contenu intégré](https://www.youtube.com/embed/1de8NkTseqM?feature=oembed)

Dans notre fichier `serverless.yml`, nous allons ajouter une configuration à la section `Resources` :

```
resources:
    Resources:
        DemoBucketUpload:
            Type: AWS::S3::Bucket
            Properties:
                BucketName: ${self:custom.bucketName}
        # Nouveau Code
        MyDynamoDbTable:
            Type: AWS::DynamoDB::Table
            Properties:
                TableName: ${self:custom.tableName}
                AttributeDefinitions:
                    - AttributeName: ID
                      AttributeType: S
                KeySchema:
                    - AttributeName: ID
                      KeyType: HASH
                BillingMode: PAY_PER_REQUEST

```

Dans ce code, nous pouvons voir que nous créons une nouvelle table DynamoDB avec un `TableName` de `${self:custom.tableName}`, en définissant un attribut `ID` et en définissant le mode de facturation à payer par requête.

C'est notre premier aperçu de l'utilisation de variables dans notre fichier `serverless.yml`. Nous pouvons utiliser des variables pour plusieurs raisons et elles peuvent faciliter notre travail. Dans ce cas, nous faisons référence à la variable `custom.tableName`. Nous pouvons ensuite faire référence à cette variable depuis plusieurs emplacements sans avoir à copier et coller le nom de la table. Pour que cela fonctionne, nous devons également ajouter `tableName` à la section personnalisée. Dans notre cas, nous allons ajouter la ligne `tableName: player-points` pour créer une table afin de stocker les points d'un joueur. Ce nom de table doit simplement être unique pour votre compte.

Lors de la définition d'une table, vous devez définir au moins l'un des champs qui sera votre champ d'identification unique. Comme DynamoDB est une base de données non relationnelle, vous n'avez pas besoin de définir le schéma complet. Dans notre cas, nous avons défini l'`ID`, en indiquant qu'il a un type d'attribut de chaîne et un type de clé de `HASH`.

La dernière partie de la définition est le mode de facturation. Il existe deux façons de payer pour DynamoDB :

* payer par requête
* ressources provisionnées.

Les ressources provisionnées vous permettent de définir la quantité de données que vous allez lire et écrire dans la table. Les problèmes avec cela sont que si vous commencez à utiliser davantage, vos requêtes sont limitées, et que vous payez pour la ressource même si personne ne l'utilise.

Payer par requête est beaucoup plus simple car vous payez simplement par requête. Cela signifie que si personne ne l'utilise, vous ne payez rien, et si vous avez des centaines de personnes qui l'utilisent en même temps, toutes les requêtes fonctionnent. Pour cette flexibilité supplémentaire, vous payez légèrement plus pour Payer par requête, mais à long terme, cela s'avère généralement moins cher.

Une fois que nous avons exécuté `sls deploy` à nouveau, nous pouvons ouvrir notre console AWS et rechercher DynamoDB. Nous devrions pouvoir voir notre nouvelle table et nous pouvons voir qu'il n'y a rien dedans.

Pour ajouter des données à la table, cliquez sur `Créer un élément`, donnez-lui un ID unique, cliquez sur le bouton plus et `ajoutez` un nouveau champ et sélectionnez le type de chaîne. Nous devons lui donner un champ `name` et une valeur `Jess`. Ajoutez un champ numérique `score` défini sur `12`. Cliquez sur enregistrer et vous avez maintenant des données dans votre table dynamo.

![Image](https://completecoding.io/content/images/2019/12/Screenshot-2019-12-10-at-07.57.54.png)

<a class="anchor" id="dynamoGet"></a>

# **Obtention de données depuis votre table DynamoDB**

Maintenant que nous avons créé notre table Dynamo, nous voulons pouvoir obtenir et ajouter des données à la table. Nous allons commencer par obtenir des données depuis la table avec un endpoint get.

[Contenu intégré](https://www.youtube.com/embed/CpDFfSXRG04?feature=oembed)

Nous allons créer un nouveau fichier dans notre dossier `endpoints` appelé `getPlayerScore.js`. Ce endpoint Lambda va gérer les requêtes pour un utilisateur et obtenir ces données depuis la table Dynamo.

```js
const Responses = require('../common/API_Responses');
const Dynamo = require('../common/Dynamo');

const tableName = process.env.tableName;

exports.handler = async event => {
    console.log('event', event);

    if (!event.pathParameters || !event.pathParameters.ID) {
        // échoué sans ID
        return Responses._400({ message: 'ID manquant dans le chemin' });
    }

    let ID = event.pathParameters.ID;

    const user = await Dynamo.get(ID, tableName).catch(err => {
        console.log('erreur dans Dynamo Get', err);
        return null;
    });

    if (!user) {
        return Responses._400({ message: 'Échec de la récupération de l\'utilisateur par ID' });
    }

    return Responses._200({ user });
};

```

Le code utilisé ici est très similaire au code à l'intérieur du fichier `getUser.js`. Nous vérifions qu'un paramètre de chemin ID existe, obtenons les données de l'utilisateur, puis retournons l'utilisateur. La principale différence est la manière dont nous obtenons l'utilisateur.

Nous avons importé l'objet de fonction `Dynamo` et appelons `Dynamo.get`. Nous passons l'ID et le nom de la table, puis capturons les erreurs. Nous devons maintenant créer cet objet de fonction `Dynamo` dans un nouveau fichier appelé `Dynamo.js` dans le dossier commun.

```js
const AWS = require('aws-sdk');

const documentClient = new AWS.DynamoDB.DocumentClient();

const Dynamo = {
    async get(ID, TableName) {
        const params = {
            TableName,
            Key: {
                ID,
            },
        };

        const data = await documentClient.get(params).promise();

        if (!data || !data.Item) {
            throw Error(`Il y a eu une erreur lors de la récupération des données pour l\'ID ${ID} depuis ${TableName}`);
        }
        console.log(data);

        return data.Item;
    },
};
module.exports = Dynamo;

```

La lecture et l'écriture dans Dynamo nécessitent une quantité raisonnable de code. Nous pourrions écrire ce code chaque fois que nous voulons utiliser Dynamo, mais il est beaucoup plus propre d'avoir des fonctions pour simplifier le processus pour nous.

Le fichier importe d'abord AWS, puis crée une instance du client de document DynamoDB. Le client de document est le moyen le plus simple pour nous de travailler avec Dynamo depuis nos Lambdas. Nous créons un objet `Dynamo` avec une fonction get asynchrone. Les seules choses dont nous avons besoin pour faire une requête sont un ID et un nom de table. Nous les formatons dans le format de paramètre correct pour le DocumentClient, attendons une requête `documentClient.get`, et nous assurons d'ajouter `.promise()` à la fin. Cela transforme la requête d'un rappel en une promesse qui est beaucoup plus facile à utiliser. Nous vérifions que nous avons réussi à obtenir un élément de Dynamo, puis nous retournons cet élément.

Nous avons maintenant tout le code dont nous avons besoin, nous devons également mettre à jour notre fichier `serverless.yml`. La première chose à faire est d'ajouter notre nouveau point de terminaison d'API en l'ajoutant à notre liste de fonctions.

```
    getPlayerScore:
        handler: lambdas/endpoints/getPlayerScore.handler
        events:
            - http:
                  path: get-player-score/{ID}
                  method: GET
                  cors: true

```

Il y a deux autres changements que nous devons apporter pour que notre point de terminaison fonctionne :

* variables d'environnement
* permissions

Vous avez peut-être remarqué dans le fichier `getPlayerScore.js` que nous avions une ligne de code comme celle-ci :

```js
const tableName = process.env.tableName;

```

C'est ici que nous obtenons le nom de la table à partir des variables d'environnement de la Lambda. Pour créer notre Lambda avec les bonnes variables d'environnement, nous devons définir un nouvel objet dans le fournisseur appelé `environment` avec un champ `tableName` et une valeur `${self:custom.tableName}`. Cela garantira que nous faisons la requête à la bonne table.

Nous devons également donner à nos Lambdas les permissions d'accéder à Dynamo. Nous devons ajouter un autre champ au fournisseur appelé `iamRoleStatements`. Celui-ci contient un tableau de politiques qui peuvent autoriser ou interdire l'accès à certains services ou ressources :

```
provider:
    name: aws
    runtime: nodejs10.x
    profile: serverlessUser
    region: eu-west-1
    environment:
        tableName: ${self:custom.tableName}
    iamRoleStatements:
        - Effect: Allow
          Action:
              - dynamodb:*
          Resource: '*'

```

Comme tout cela a été ajouté à l'objet fournisseur, il sera appliqué à toutes les Lambdas.

Nous pouvons maintenant exécuter `sls deploy` à nouveau pour déployer notre nouveau point de terminaison. Une fois cela fait, nous devrions obtenir une sortie avec un nouveau point de terminaison `https://${something-provided-by-API-Gateway}/get-player-score/{ID}`. Si nous copions cette URL dans un onglet du navigateur et ajoutons l'ID du joueur que nous avons créé dans la dernière section, nous devrions obtenir une réponse.

![Image](https://completecoding.io/content/images/2019/12/Screenshot-2019-12-10-at-07.59.02.png)

<a class="anchor" id="dynamoPut"></a>

# **Ajout de nouvelles données à DynamoDB**

Pouvoir obtenir des données depuis Dynamo est cool, mais c'est assez inutile si nous ne pouvons pas également ajouter de nouvelles données à la table. Nous allons créer un point de terminaison POST pour créer de nouvelles données dans notre table Dynamo.

[Contenu intégré](https://www.youtube.com/embed/AguTaMQGACE?feature=oembed)

Commencez par créer un nouveau fichier dans notre dossier endpoints appelé `createPlayerScore.js` et ajoutez ce code :

```js
const Responses = require('../common/API_Responses');
const Dynamo = require('../common/Dynamo');

const tableName = process.env.tableName;

exports.handler = async event => {
    console.log('event', event);

    if (!event.pathParameters || !event.pathParameters.ID) {
        // échoué sans ID
        return Responses._400({ message: 'ID manquant dans le chemin' });
    }

    let ID = event.pathParameters.ID;
    const user = JSON.parse(event.body);
    user.ID = ID;

    const newUser = await Dynamo.write(user, tableName).catch(err => {
        console.log('erreur dans l\'écriture dynamo', err);
        return null;
    });

    if (!newUser) {
        return Responses._400({ message: 'Échec de l\'écriture de l\'utilisateur par ID' });
    }

    return Responses._200({ newUser });
};

```

Ce code est très similaire au code `getPlayerScore` avec quelques modifications. Nous obtenons l'utilisateur depuis le corps de la requête, ajoutons l'ID à l'utilisateur, puis passons cela à une fonction `Dynamo.write`. Nous devons analyser le corps de l'événement car API Gateway le convertit en chaîne avant de le passer à la Lambda.

Nous devons maintenant modifier le fichier commun `Dynamo.js` pour ajouter la méthode `.write`. Cela effectue des étapes très similaires à la fonction `.get` et retourne les données nouvellement créées :

```js
    async write(data, TableName) {
        if (!data.ID) {
            throw Error('aucun ID sur les données');
        }

        const params = {
            TableName,
            Item: data,
        };

        const res = await documentClient.put(params).promise();

        if (!res) {
            throw Error(`Il y a eu une erreur lors de l\'insertion de l\'ID ${data.ID} dans la table ${TableName}`);
        }

        return data;
    }

```

Nous avons créé le point de terminaison et le code commun, donc la dernière chose que nous devons faire est de modifier le fichier `serverless.yml`. Comme nous avons ajouté la variable d'environnement et les permissions dans la dernière section, nous devons simplement ajouter la fonction et la configuration de l'API. Ce point de terminaison est différent des deux précédents car la méthode est `POST` au lieu de `GET` :

```
    createPlayerScore:
        handler: lambdas/endpoints/createPlayerScore.handler
        events:
            - http:
                  path: create-player-score/{ID}
                  method: POST
                  cors: true

```

Le déploiement de ceci avec `sls deploy` créera maintenant trois points de terminaison, y compris notre point de terminaison `create-player-score`. Tester un point de terminaison `POST` est plus complexe qu'une requête `GET`, mais heureusement, il existe des outils pour nous aider. J'utilise [Postman](https://www.getpostman.com/) pour tester tous mes points de terminaison car cela rend le processus rapide et facile.

Créez une nouvelle requête et collez votre URL `create-player-score`. Vous devez changer le type de requête en `POST` et définir l'ID à la fin de l'URL. Comme nous faisons une requête POST, nous pouvons envoyer des données dans le corps de la requête. Cliquez sur `body` puis `raw` et sélectionnez `JSON` comme type de corps. Vous pouvez ensuite ajouter les données que vous souhaitez mettre dans votre table. Lorsque vous cliquez sur `Send`, vous devriez obtenir une réponse réussie :

![Image](https://completecoding.io/content/images/2019/12/postman.png)

Pour valider que vos données ont été ajoutées à la table, vous pouvez faire une requête get-player-score avec l'ID des nouvelles données que vous venez de créer. Vous pouvez également aller dans la console Dynamo et regarder tous les éléments de la table.

<a class="anchor" id="s3API"></a>

# **Création de points de terminaison S3 GET et POST**

Dynamo est une solution de stockage de base de données brillante, mais parfois ce n'est pas la meilleure solution de stockage. Si vous avez des données qui ne vont pas changer et que vous voulez économiser de l'argent, ou si vous voulez stocker des fichiers autres que du JSON, alors vous pourriez vouloir considérer Amazon S3.

[Contenu intégré](https://www.youtube.com/embed/MlKpK0WqTSs?feature=oembed)

Créer des points de terminaison pour obtenir et créer des fichiers dans S3 est très similaire à DynamoDB. Nous devons créer deux fichiers de points de terminaison, un fichier S3 commun, et modifier le fichier `serverless.yml`.

Nous allons commencer par ajouter un fichier à S3. Créez un fichier `createFile.js` dans le dossier endpoints et ajoutez ce code :

```js
const Responses = require('../common/API_Responses');
const S3 = require('../common/S3');

const bucket = process.env.bucketName;

exports.handler = async event => {
    console.log('event', event);

    if (!event.pathParameters || !event.pathParameters.fileName) {
        // échoué sans fileName
        return Responses._400({ message: 'fileName manquant dans le chemin' });
    }

    let fileName = event.pathParameters.fileName;
    const data = JSON.parse(event.body);

    const newData = await S3.write(data, fileName, bucket).catch(err => {
        console.log('erreur dans l\'écriture S3', err);
        return null;
    });

    if (!newData) {
        return Responses._400({ message: 'Échec de l\'écriture des données par nom de fichier' });
    }

    return Responses._200({ newData });
};

```

Ce code est presque identique au code `createPlayerScore.js`, mais utilise un `fileName` au lieu d'un `ID` et `S3.write` au lieu de `Dynamo.write`.

Maintenant, nous devons créer notre code commun `S3` pour simplifier les requêtes faites à S3 :

```js
const AWS = require('aws-sdk');
const s3Client = new AWS.S3();

const S3 = {
    async write(data, fileName, bucket) {
        const params = {
            Bucket: bucket,
            Body: JSON.stringify(data),
            Key: fileName,
        };
        const newData = await s3Client.putObject(params).promise();
        if (!newData) {
            throw Error('il y a eu une erreur lors de l\'écriture du fichier');
        }
        return newData;
    },
};
module.exports = S3;

```

Encore une fois, le code dans ce fichier est très similaire au code dans `Dynamo.js`, avec quelques différences autour des paramètres pour la requête.

La dernière chose que nous devons faire pour écrire dans S3 est de changer le fichier `serverless.yml`. Nous devons faire quatre choses : ajouter des variables d'environnement, ajouter des permissions, ajouter la fonction, et ajouter un bucket S3.

Dans le fournisseur, nous pouvons ajouter une nouvelle variable d'environnement `bucketName: ${self:custom.s3UploadBucket}`.

Pour ajouter la permission de lire et écrire dans S3, nous pouvons ajouter une nouvelle permission à la stratégie existante. Juste après `- dynamodb:*`, nous pouvons ajouter la ligne `- s3:*`.

L'ajout de la fonction est le même que ce que nous avons fait avec toutes nos autres fonctions. Assurez-vous que le chemin a un paramètre `fileName` car c'est ce que vous vérifiez dans votre code de point de terminaison :

```
    createFile:
        handler: lambdas/endpoints/createFile.handler
        events:
            - http:
                  path: create-file/{fileName}
                  method: POST
                  cors: true

```

Enfin, nous devons créer un nouveau bucket pour téléverser ces fichiers. Dans la section `custom`, nous devons ajouter un nouveau champ `s3UploadBucket` et le définir sur un nom de bucket unique. Nous devons également configurer la ressource. Après la configuration de la table Dynamo, nous pouvons ajouter ceci pour créer un nouveau bucket pour nos téléversements de fichiers :

```
        s3UploadBucket:
            Type: AWS::S3::Bucket
            Properties:
                BucketName: ${self:custom.s3UploadBucket}

```

Avec cette configuration, il est temps de déployer à nouveau. L'exécution de `sls deploy` à nouveau déployera le nouveau bucket de téléversement ainsi que le point de terminaison d'écriture S3. Pour tester le point de terminaison d'écriture, nous devons retourner sur Postman.

Copiez l'URL `create-file` que vous obtenez lorsque Serverless a terminé le déploiement et collez-la dans Postman et changez le type de requête en `POST`. Ensuite, ce que nous devons faire est d'ajouter le nom de fichier que nous téléversons. Dans notre cas, nous allons téléverser `car.json`. La dernière chose que nous devons faire est d'ajouter les données à la requête. Sélectionnez `Body` puis `raw` avec un type `JSON`. Vous pouvez ajouter les données JSON que vous souhaitez, mais voici des données d'exemple :

```
{
	"model": "Ford Focus",
	"year": 2018,
	"colour": "red"
}
```

Lorsque vous postez ces données, vous devriez obtenir une réponse `200` avec une référence `ETag` au fichier. En allant dans la console et votre nouveau bucket S3, vous devriez pouvoir voir `car.json`.

## **Obtention de données depuis S3**

Maintenant que nous pouvons téléverser des données vers S3, nous voulons également pouvoir les récupérer. Nous commençons par créer un fichier `getFile.js` à l'intérieur du dossier endpoints :

```js
const Responses = require('../common/API_Responses');
const S3 = require('../common/S3');

const bucket = process.env.bucketName;

exports.handler = async event => {
    console.log('event', event);

    if (!event.pathParameters || !event.pathParameters.fileName) {
        // échoué sans fileName
        return Responses._400({ message: 'fileName manquant dans le chemin' });
    }

    const fileName = event.pathParameters.fileName;

    const file = await S3.get(fileName, bucket).catch(err => {
        console.log('erreur dans S3 get', err);
        return null;
    });

    if (!file) {
        return Responses._400({ message: 'Échec de la lecture des données par nom de fichier' });
    }

    return Responses._200({ file });
};
```

Cela devrait ressembler à des points de terminaison `GET` précédents que nous avons créés auparavant. Les différences sont l'utilisation du paramètre de chemin `fileName`, `S3.get`, et le retour du fichier.

À l'intérieur du fichier commun `s3.js`, nous devons ajouter la fonction `get`. La principale différence entre cela et l'obtention depuis Dynamo est que lorsque nous obtenons depuis S3, le résultat n'est pas une réponse JSON, mais un `Buffer`. Cela signifie que si nous téléversons un fichier JSON, il ne reviendra pas au format JSON, donc nous vérifions si nous obtenons un fichier JSON et le transformons à nouveau en JSON :

```js
    async get(fileName, bucket) {
        const params = {
            Bucket: bucket,
            Key: fileName,
        };
        let data = await s3Client.getObject(params).promise();
        if (!data) {
            throw Error(`Échec de l\'obtention du fichier ${fileName}, depuis ${bucket}`);
        }
        if (fileName.slice(fileName.length - 4, fileName.length) == 'json') {
            data = data.Body.toString();
        }
        return data;
    }

```

De retour dans notre fichier `serverless.yml`, nous pouvons ajouter une nouvelle fonction et un point de terminaison pour obtenir des fichiers. Nous avons déjà configuré les permissions et les variables d'environnement :

```
    getFile:
        handler: lambdas/endpoints/getFile.handler
        events:
            - http:
                  path: get-file/{fileName}
                  method: GET
                  cors: true
```

Comme nous créons un nouveau point de terminaison, nous devons faire un déploiement complet à nouveau avec `sls deploy`. Nous pouvons ensuite prendre le nouveau point de terminaison `get-file` et le coller dans un navigateur ou Postman. Si nous ajoutons `car.json` à la fin de la requête, nous recevrons les données JSON que nous avons téléversées plus tôt dans cette section.

<a class="anchor" id="l9apikey"></a>

# **Sécurisation de vos points de terminaison avec des clés API**

Pouvoir créer des points de terminaison d'API rapidement et facilement avec Serverless est génial pour démarrer un projet et créer une preuve de concept. Lorsque vous passez à la création d'une version de production de votre application, vous devez commencer à être plus prudent quant à qui peut accéder à vos points de terminaison. Vous ne voulez pas que n'importe qui puisse accéder à vos APIs.

[Contenu intégré](https://www.youtube.com/embed/n5aSq1L5nIw?feature=oembed)

Pour sécuriser vos APIs, il existe de nombreuses méthodes, et dans cette section, nous allons mettre en œuvre des clés API. Si vous ne passez pas la clé API avec la requête, elle échoue avec un message non autorisé. Vous pouvez ensuite contrôler à qui vous donnez les clés API, et donc qui a accès à vos APIs.

Vous pouvez également ajouter des politiques d'utilisation à vos clés API afin de pouvoir contrôler combien chaque personne utilise votre API. Cela vous permet de créer des plans d'utilisation échelonnés pour votre service.

Pour commencer, nous allons créer une clé API simple. Pour ce faire, nous devons aller dans notre fichier `serverless.yml` et ajouter une configuration au fournisseur.

```js
	apiKeys:
		myFirstAPIKey
```

Cela créera une nouvelle clé API. Maintenant, nous devons dire à Serverless quels points de terminaison d'API protéger avec la clé API. Cela a été fait de sorte que nous pouvons avoir certaines des APIs protégées, tandis que certaines restent publiques. Nous spécifions qu'un point de terminaison doit être protégé en ajoutant l'option `private: true` :

```js
    getUser:
        handler: lambdas/endpoints/getUser.handler
        events:
            - http:
                  path: get-user/{ID}
                  method: GET
                  cors: true
                  private: true
```

Vous pouvez ensuite ajouter ce champ à autant de vos APIs que vous le souhaitez. Pour déployer cela, nous pouvons exécuter `sls deploy` à nouveau. Une fois cela terminé, vous obtiendrez une clé API dans les valeurs de retour. Cela est très important et nous l'utiliserons très bientôt. Si vous essayez de faire une requête à votre API `get-user`, vous devriez obtenir une erreur 401 Non autorisé.

Pour que la requête réussisse, vous devez maintenant passer une clé API dans les en-têtes de la requête. Pour ce faire, nous devons utiliser Postman ou un autre outil de requête API et ajouter un en-tête à notre requête get. Nous faisons cela en sélectionnant `Authorisation` en utilisant le `type d'API`. La clé doit être `X-API-KEY` et la valeur est la clé que vous avez obtenue en sortie de votre déploiement Serverless :

![Image](https://completecoding.io/content/images/2019/12/Screenshot-2019-12-20-at-20.05.53.png)

Maintenant, lorsque nous faisons la requête, nous obtenons une réponse réussie. Cela signifie que seules les personnes à qui vous avez donné votre clé API peuvent accéder à votre API.

C'est génial, mais nous pouvons faire plus. Nous pouvons ajouter une politique d'utilisation à cette clé API. C'est ici que nous pouvons limiter le nombre de requêtes par mois ainsi que le taux auquel les requêtes peuvent être faites. C'est génial pour exécuter un produit SAAS car vous pouvez fournir une clé API qui donne aux utilisateurs un nombre défini d'appels API.

Pour créer un plan d'utilisation, nous devons ajouter un nouvel objet dans le fournisseur. La section `quota` définit combien de requêtes peuvent être faites en utilisant cette clé API. Vous pouvez changer la période en `DAY` ou `WEEK` si cela convient mieux à votre application.

La section `throttle` vous permet de contrôler la fréquence à laquelle vos points de terminaison d'API peuvent être atteints. L'ajout d'une limite de `rate limit` définit un nombre maximum de requêtes par seconde. Cela est très utile car cela empêche les gens de mettre en place une attaque par déni de service. La `burstLimit` permet à l'API d'être atteinte plus souvent que votre `rateLimit`, mais seulement pour une courte période de temps, généralement quelques secondes :

```
    usagePlan:
        quota:
            limit: 10
            period: MONTH
        throttle:
            burstLimit: 2
            rateLimit: 1
```

Si nous devions déployer cela à nouveau, le déploiement échouerait car nous essaierions de déployer la même clé API. Les clés API doivent être uniques, nous devons donc changer le nom de la clé API. Lorsque nous déployons cela et copions notre nouvelle clé API dans Postman, nous pourrons faire des requêtes comme nous le faisons normalement. Si nous essayons de faire trop de requêtes par seconde ou atteignons le nombre maximum de requêtes, nous obtiendrons une erreur 429 de

```
{
    "message": "Limite dépassée"
}
```

Cela signifie que vous ne pouvez plus utiliser cette clé API jusqu'au mois prochain.

Bien que la création d'un plan d'utilisation soit géniale, vous souhaitez souvent donner à différentes personnes différents niveaux d'accès à vos services. Vous pourriez donner aux utilisateurs gratuits 100 requêtes par mois et aux utilisateurs payants 1000. Vous pourriez vouloir différents plans de paiement qui donnent différents nombres de requêtes. Vous voudriez probablement aussi une clé API maître pour vous-même qui a des requêtes illimitées !

Pour ce faire, nous pouvons configurer plusieurs groupes de clés API, chacun ayant sa propre politique d'utilisation. Nous devons changer les sections `apiKeys` et `usagePlan` :

```
	apiKeys:
        - free:
              - MyAPIKey3
        - paid:
              - MyPaidKey3
    usagePlan:
        - free:
              quota:
                  limit: 10
                  period: MONTH
              throttle:
                  burstLimit: 2
                  rateLimit: 1
        - paid:
              quota:
                  period: MONTH
                  limit: 1000
              throttle:
                  burstLimit: 20
                  rateLimit: 10
```

Une fois que vous avez enregistré et déployé cela, vous obtiendrez deux nouvelles clés API, chacune avec un niveau d'accès différent à vos points de terminaison d'API.

<style> a.anchor {
    display: block;
    position: relative;
    top: -40px;
    visibility: hidden;
}
</style>

Merci d'avoir lu ce guide ! Si vous l'avez trouvé utile, veuillez vous abonner à ma [chaîne YouTube](https://www.youtube.com/channel/UC8uBP0Un18DJAnWjm1CPqBg) où je publie des vidéos hebdomadaires sur Serverless et le développement logiciel.