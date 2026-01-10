---
title: Comment créer une application CRUD Full-Stack Serverless avec AWS et React
subtitle: ''
author: Chisom Uma
co_authors: []
series: null
date: '2025-10-21T16:37:30.728Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-full-stack-serverless-app
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1761064422167/c0a6b8ed-a500-43f2-820f-42fef5d73275.png
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: serverless
  slug: serverless
- name: AWS
  slug: aws
- name: React
  slug: reactjs
seo_title: Comment créer une application CRUD Full-Stack Serverless avec AWS et React
seo_desc: 'Imagine running a production application that automatically scales from
  zero to thousands of users without ever touching a server configuration. That''s
  the power of serverless architecture, and it''s easier to implement than you might
  think.

  If you''re...'
---

Imaginez exécuter une application de production qui passe automatiquement à l'échelle de zéro à des milliers d'utilisateurs sans jamais toucher à une configuration de serveur. C'est la puissance de l'architecture serverless, et c'est plus facile à mettre en œuvre que vous ne le pensez.

Si vous êtes un ingénieur cloud junior prêt à dépasser les concepts théoriques d'AWS pour construire quelque chose de concret, ce tutoriel vous guide dans la création d'un système complet de gestion de café serverless.

Vous apprendrez à concevoir, déployer et sécuriser une application prête pour la production en utilisant les services serverless les plus puissants d'AWS.

Sans plus attendre, commençons !

## Table des matières

* [Prérequis](#heading-prerequis)
    
* [Outils que nous utiliserons](#heading-outils-que-nous-utiliserons)
    
* [Ce que nous construisons](#heading-ce-que-nous-construisons)
    
* [Pourquoi le Serverless ?](#heading-pourquoi-le-serverless)
    
* [Aperçu de l'architecture](#heading-apercu-de-larchitecture)
    
* [Créer une application Full-Stack Serverless](#heading-creer-une-application-full-stack-serverless)
    
    * [Étape 1 : Créer une table DynamoDB](#heading-etape-1-creer-une-table-dynamodb)
        
    * [Étape 2 : Créer un rôle IAM pour la fonction Lambda](#heading-etape-2-creer-un-role-iam-pour-la-fonction-lambda)
        
    * [Étape 3 : Créer une Lambda Layer et des fonctions Lambda](#heading-etape-3-creer-une-lambda-layer-et-des-fonctions-lambda)
        
    * [Étape 4 : Créer une API Gateway pour exposer les fonctions Lambda](#heading-etape-4-creer-une-api-gateway-pour-exposer-les-fonctions-lambda)
        
    * [Étape 5 : Configurer l'application React et téléverser le build vers un bucket S3](#heading-etape-5-configurer-lapplication-react-et-televerser-le-build-vers-un-bucket-s3)
        
    * [Étape 6 : Configurer un Authorizer Amazon API Gateway](#heading-etape-6-configurer-un-authorizer-amazon-api-gateway)
        
    * [Étape 7 : Créer une distribution CloudFront avec des comportements pour S3 et API Gateway](#heading-etape-7-creer-une-distribution-cloudfront-avec-des-comportements-pour-s3-et-api-gateway)
        
    * [Étape 8 : Configurer l'application React et téléverser le build vers un bucket S3](#heading-etape-8-configurer-lapplication-react-et-televerser-le-build-vers-un-bucket-s3)
        
* [Dépannage de l'erreur Access Denied](#heading-depannage-de-lerreur-access-denied)
    
    * [Étape 1 : Configurer l'Origin Access Control (OAC)](#heading-etape-1-configurer-lorigin-access-control-oac)
        
    * [Étape 2 : Mettre à jour la politique du bucket S3](#heading-etape-2-mettre-a-jour-la-politique-du-bucket-s3)
        
    * [Étape 3 : Définir l'objet racine par défaut](#heading-etape-3-definir-lobjet-racine-par-defaut)
        
* [Conclusion](#heading-conclusion)
    

## Prérequis

* Connaissances de base d'AWS.
    
* Connaissances de base des services serverless AWS.
    
* Connaissance de React (non requise).
    
* Connaissances de base de Postman ou d'autres outils de test d'API.
    

## Outils que nous utiliserons

* [React.js](https://react.dev/)
    
* [AWS Lambda](https://aws.amazon.com/lambda/)
    
* [DynamoDB](https://aws.amazon.com/dynamodb/)
    
* [API Gateway](https://aws.amazon.com/api-gateway/)
    
* [Cognito](https://aws.amazon.com/pm/cognito/)
    
* [CloudFront](https://aws.amazon.com/cloudfront/)
    

## Ce que nous construisons

Nous allons construire un système complet de gestion de café serverless en utilisant les services cloud AWS. Les propriétaires de café se connecteront en toute sécurité via l'authentification AWS Cognito et auront un contrôle total sur leur inventaire : ajout de nouveaux produits, mise à jour des niveaux de stock, consultation de l'inventaire actuel et suppression des articles abandonnés. Pour suivre ce tutoriel, vous pouvez cloner le dépôt [ici](https://github.com/ChisomUma/aws-serverless-arch-project).

Voici à quoi ressemble notre interface utilisateur (UI) :

![image du tableau de bord du projet serverless](https://cdn.hashnode.com/res/hashnode/image/upload/v1760784475691/8d9ba162-74dd-447d-b627-3e67b8a944ae.png align="center")

## Pourquoi le Serverless ?

Les services serverless d'AWS comme Lambda, Cognito et API Gateway passent automatiquement à zéro pendant les périodes calmes et montent instantanément en charge lors des pics de trafic. Bien que « serverless » puisse laisser croire qu'il n'y a pas de serveurs du tout, ce n'est pas le cas. Cela signifie qu'AWS gère tout le travail complexe, le provisionnement, la gestion et la mise à l'échelle de l'infrastructure en coulisses. Vous ne payez que pour ce que vous utilisez.

## Aperçu de l'architecture

Notre architecture utilise DynamoDB comme magasin de données, avec des fonctions Lambda (enrichies par des Lambda Layers) gérant toutes les requêtes API Gateway. Cognito sécurise l'API Gateway, tandis que le CDN CloudFront distribue le tout mondialement. Le frontend React se connecte directement au UserPool Cognito et est hébergé sur S3 avec une distribution CloudFront. Pour les déploiements en production, vous pouvez ajouter un domaine personnalisé via CloudFlare et AWS Certificate Manager.

## Créer une application Full-Stack Serverless

Dans cette section, vous allez construire une architecture serverless full-stack.

### Étape 1 : Créer une table DynamoDB

Pour créer une table DynamoDB, accédez à votre console AWS et sélectionnez la section DynamoDB. Vous pouvez le faire rapidement en tapant « DynamoDB » dans la barre de recherche AWS. Ensuite, suivez les étapes ci-dessous pour terminer la création de votre table :

1. Cliquez sur **Créer une table**.
    
2. Saisissez le nom de la table : « CoffeeShop ».
    
3. Saisissez la clé de partition : « coffeeId ».
    
4. Cliquez sur **Créer une table**.
    

**Étape 1.1 : Créer des éléments**

Vous devez créer des éléments dans la table. Cela aide à tester la connectivité à votre table DynamoDB.

Pour notre cas d'utilisation, nous allons créer un élément nommé « coffee » et saisir des attributs tels que coffeeId, name, price et availability. Pour créer un élément :

1. Cliquez sur **Explorer les éléments** dans le volet de navigation de gauche.
    
2. Cliquez sur **Créer un élément**.
    
3. Sélectionnez le bouton radio *CoffeeShop*, puis cliquez sur **Créer un élément**.
    

![image de la page dynamodb](https://cdn.hashnode.com/res/hashnode/image/upload/v1760785698166/ee1f5e2d-feef-41de-80d8-eb2c4cad4d04.png align="center")

4. Cliquez sur **Ajouter un nouvel attribut**. Cela vous permet d'ajouter différents types de données comme des chaînes de caractères et des booléens. La structure JSON ci-dessous montre les attributs créés.
    

```json

{
    "coffeeId": "c123",
    "name": "new cold coffee",
    "price": 456,
    "available": true
}
```

### Étape 2 : Créer un rôle IAM pour la fonction Lambda

Ensuite, créez une fonction Lambda qui interagit avec la table DynamoDB en utilisant un rôle IAM attaché à la fonction. Nous allons configurer un rôle IAM nommé « CoffeeShopRole » qui servira de rôle d'exécution partagé pour toutes les fonctions Lambda de l'application.

Ce rôle inclut les permissions suivantes :

* **CloudWatch Logs** : Capacités de journalisation complètes (création, écriture et gestion des flux de journaux).
    
* **Accès DynamoDB** : Opérations complètes de lecture, écriture, mise à jour et suppression sur la table « CoffeeShop ».
    

Pour ce faire :

1. Accédez à la console AWS IAM.
    
2. Allez dans **Rôles**.
    
3. Cliquez sur **Créer un rôle**.
    
4. Sélectionnez le service Lambda.
    
5. Recherchez « AWSLambdaBasicExecutionRole ».
    
6. Nommez votre rôle et cliquez sur **Créer un rôle**.
    

Voici à quoi ressemble le rôle :

```json

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "dynamodb:PutItem",
                "dynamodb:DeleteItem",
                "dynamodb:GetItem",
                "dynamodb:Scan",
                "dynamodb:UpdateItem"
            ],
            "Resource": "arn:aws:dynamodb::<DYNAMODB_TABLE_NAME>"
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "*"
        }
    ]
}
```

Cette politique nous permet de créer des journaux CloudWatch. Ensuite, créez une **politique en ligne** pour permettre les communications vers DynamoDB. Sélectionnez les actions suivantes pour la table :

* Get
    
* Put
    
* Update
    
* Scan
    
* Delete
    

Ensuite, connectez l'ARN de votre table à la politique en accédant à la table créée et en copiant l'ARN dans la politique.

### Étape 3 : Créer une Lambda Layer et des fonctions Lambda

Maintenant, nous devons connecter notre fonction Lambda à la table DynamoDB. Pour cela, nous aurons besoin du SDK JavaScript DynamoDB. Pour commencer, créez deux dossiers : `lambda` > `get` dans votre IDE, de préférence VS Code. Accédez à ces dossiers dans votre terminal et exécutez la commande `npm init` pour initialiser votre projet. Mettez à jour votre fichier `package.json` avec ceci :

```json

{
  "name": "get",
  "type": "module",
  "version": "1.0.0",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC",
  "description": ""
}
```

**Note :** nous utiliserons [ECMAScript](https://developer.mozilla.org/en-US/docs/Glossary/ECMAScript) tout au long de ce tutoriel.

Ensuite, nous devons créer une Lambda Layer Node.js réutilisable contenant le [SDK JavaScript DynamoDB](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_dynamodb_code_examples.html) et des fonctions utilitaires partagées. Cette couche agit comme une bibliothèque commune qui peut être attachée à plusieurs fonctions Lambda, éliminant ainsi le besoin de regrouper les mêmes dépendances à plusieurs reprises dans chaque package de déploiement.

Pour utiliser le SDK, créez un nouveau fichier dans votre répertoire intitulé `index.mjs` et collez le code ci-dessous :

```typescript

// fonction getCoffee
import { DynamoDBClient, GetItemCommand } from "@aws-sdk/client-dynamodb"; // Import ESM
const config = {
    region: "us-east-1",
};
const client = new DynamoDBClient(config);
export const getCoffee = async (event) => {
    const coffeeId = "c123";
    const input = {
        TableName: "CoffeShop",
        Key: {
            coffeeId: {
                S: coffeeId,
            },
        },
    };
    const command = new GetItemCommand(input);
    const response = await client.send(command);
    console.log(response);
    return response;
}
```

Le code ci-dessus est la fonction `getCoffee` qui se connecte à la table DynamoDB nommée `CoffeShop`, recherche le café avec l'ID `c123` et affiche ses détails.

Remplacez `region` par votre région spécifique.

Ensuite, installez les dépendances Lambda pour le SDK en utilisant la commande ci-dessous :

```bash

npm i @aws-sdk/client-dynamodb @aws-sdk/lib-dynamodb
```

Ensuite, créez un fichier zip pour tous les fichiers actuels avec la commande suivante :

```bash
zip -r get.zip ./*
```

Cela crée un fichier zip dans votre répertoire de projet. Maintenant, accédez à la page des fonctions Lambda sur votre console AWS et téléversez ce fichier zip.

Cliquez sur **Test** pour tester votre application. Si vous rencontrez une erreur, modifiez les paramètres d'exécution (Runtime settings) et changez le nom du gestionnaire (handler) en `index.getCoffee`. Déployez et exécutez à nouveau le code, vous devriez obtenir une réponse réussie de DynamoDB comme indiqué ci-dessous :

Réponse :

```bash

{
  "$metadata": {
    "httpStatusCode": 200,
    "requestId": "R14Q5UMTP3K9P9NAF1OGG0IB57VV4KQNSO5AEMVJF66Q9ASUAAJG",
    "attempts": 1,
    "totalRetryDelay": 0
  },
  "Item": {
    "available": {
      "BOOL": true
    },
    "price": {
      "N": "34"
    },
    "name": {
      "S": "My New Coffee"
    },
    "coffeeId": {
      "S": "c123"
    }
  }
}
```

Maintenant, apportons les modifications nécessaires pour préparer notre fonction à recevoir des requêtes de l'API Gateway. Lorsqu'une personne demande un café via le point de terminaison `/coffee`, nous voulons que l'application renvoie une liste de tous les cafés. Mais si la requête est faite vers `/coffee/c123` ou `/coffee/id`, l'application ne doit renvoyer que les détails de ce café spécifique.

Pour ce faire, retournez dans votre fichier `index.mjs` et collez le code ci-dessous :

```typescript

import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import { DynamoDBDocumentClient, GetCommand, ScanCommand } from "@aws-sdk/lib-dynamodb";
const client = new DynamoDBClient({});
const docClient = DynamoDBDocumentClient.from(client);
const tableName = process.env.tableName || "CoffeShop";
const createResponse = (statusCode, body) => {
    const responseBody = JSON.stringify(body);
    return {
        statusCode,
        headers: { "Content-Type": "application/json" },
        body: responseBody,
    };
};
export const getCoffee = async (event) => {
    const { pathParameters } = event;
    const { id } = pathParameters || {};
    try {
        let command;
        if (id) {
            command = new GetCommand({
                TableName: tableName,
                Key: {
                    "coffeeId": id,
                },
            });
        }
        else {
            command = new ScanCommand({
                TableName: tableName,
            });
        }
        const response = await docClient.send(command);
        return createResponse(200, response);
    }
    catch (err) {
        console.error("Error fetching data from DynamoDB:", err);
        return createResponse(500, { error: err.message });
    }
}
```

Exécutez à nouveau la commande `zip -r get.zip ./*` et téléversez à nouveau le fichier zip dans votre page de fonction Lambda.

Cette fonction AWS Lambda implémente un point de terminaison d'API serverless pour récupérer des données de café à partir d'une table DynamoDB, en utilisant le [SDK AWS v3](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/dynamodb/command/GetItemCommand/) pour créer un client de document capable soit de récupérer un article de café spécifique par ID, soit de renvoyer tous les articles de la table.

La fonction extrait l'ID du café des paramètres de chemin de l'événement entrant, construit la commande DynamoDB appropriée (`GetCommand` pour les articles uniques ou `ScanCommand` pour tous les articles), exécute l'opération de base de données et renvoie une réponse HTTP correctement formatée avec des en-têtes JSON et les codes d'état appropriés.

Répétez les étapes ci-dessus pour les fonctions `create`, `update` et `delete`. Vous pouvez trouver ces fonctions dans votre [dépôt de projet](https://github.com/ChisomUma/aws-serverless-arch-project) cloné.

### Étape 4 : Créer une API Gateway pour exposer les fonctions Lambda

Pour créer une API qui pointe vers la fonction Lambda :

1. Accédez à **API Gateway** > **Routes** et cliquez sur **Créer**.
    
2. Créez les points de terminaison suivants.
    

```bash

GET /coffee  -> fonction lambda getCoffee
GET /coffee/{id}  -> fonction lambda getCoffee
POST /coffee  -> fonction lambda createCoffee
PUT /coffee/{id}  -> fonction lambda updateCoffee
DELETE /coffee/{id}  -> fonction lambda deleteCoffee
```

3. Accédez à **Integrations** et créez des intégrations pour ces points de terminaison. Pour ce faire, allez dans l'onglet **Manage integrations**, cliquez sur **Create** et sélectionnez Lambda comme cible d'intégration.
    

Maintenant, dans votre portail API Gateway, cliquez sur `API: CoffeeShop...(numéros aléatoires)` et copiez l'URL d'appel (invoke URL) pour les tests, comme indiqué dans l'image ci-dessous :

![image de l'interface postman pendant les tests](https://cdn.hashnode.com/res/hashnode/image/upload/v1760792772732/1d453e97-ce05-4be2-ae6d-d7eb55f86820.png align="center")

La requête `get` avec un `id` renvoie une réponse `200 OK` avec les éléments créés dans DynamoDB. Vous pouvez tester le reste des points de terminaison sur Postman :)

**Ajout d'une Lambda Layer pour résoudre le problème de dépendance**

Toutes les fonctions utilisent la même dépendance, mais pour chaque fonction, nous devions maintenir des dossiers `node_modules` et des fichiers `package.json` séparés. Pour corriger cela, nous utiliserons une [Lambda Layer](https://docs.aws.amazon.com/lambda/latest/dg/chapter-layers.html). La Layer contient toutes les dépendances, tandis que les fonctions ne contiennent que votre code.

Pour commencer :

1. Créez un nouveau dossier dans votre IDE appelé `LambdaWithLayer`.
    
2. Créez deux dossiers supplémentaires sous `LambdaWithLayer` nommés `LambdaFunctionsWithLayer` et `nodejs`.
    

**Note :** Vous *devez* utiliser le nom `nodejs` pour que cela fonctionne.

3. Accédez au dossier `nodejs` et initialisez-le avec la commande `npm init`.
    
4. Installez les dépendances avec la commande suivante :
    

```bash
npm i @aws-sdk/client-dynamodb @aws-sdk/lib-dynamodb
```

5. Créez un nouveau fichier appelé `utils.js` sous le dossier `nodejs` et collez le code ci-dessous :
    

```typescript

import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import {
    DynamoDBDocumentClient,
    ScanCommand,
    GetCommand,
    PutCommand,
    UpdateCommand,
    DeleteCommand
} from "@aws-sdk/lib-dynamodb";
const client = new DynamoDBClient({});
const docClient = DynamoDBDocumentClient.from(client);
const createResponse = (statusCode, body) => {
    return {
        statusCode,
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body),
    };
};
export {
    docClient,
    createResponse,
    ScanCommand,
    GetCommand,
    PutCommand,
    UpdateCommand,
    DeleteCommand
};
```

Ici, nous avons importé toutes les commandes pour nos opérations d'API. Maintenant, nous pouvons créer des fonctions Lambda sans installer les dépendances du SDK pour chacune. Par exemple, pour la fonction `get`, créez un fichier `index.mjs` et collez le code ci-dessous :

```typescript

import { docClient, GetCommand, ScanCommand, createResponse } from '/opt/nodejs/utils.mjs'; // Importation depuis la Layer
const tableName = process.env.tableName || "CoffeShop";
export const getCoffee = async (event) => {
    const { pathParameters } = event;
    const { id } = pathParameters || {};
    try {
        let command;
        if (id) {
            command = new GetCommand({
                TableName: tableName,
                Key: {
                    "coffeeId": id,
                },
            });
        }
        else {
            command = new ScanCommand({
                TableName: tableName,
            });
        }
        const response = await docClient.send(command);
        return createResponse(200, response);
    }
    catch (err) {
        console.error("Error fetching data from DynamoDB:", err);
        return createResponse(500, { error: err.message });
    }
}
```

Répétez les étapes ci-dessus pour les autres fonctions.

6. Créez un dossier zip pour chaque fonction. Vous pouvez utiliser un script `create_zip.sh` pour automatiser cela.
    

```bash

echo "Creating zip for layer"
zip -r layer.zip nodejs
echo "Creating zip for GET Function"
cd LambdaFunctionsWithLayer/get
zip -r get.zip index.mjs
mv get.zip ../../
cd ../..
# ... répéter pour les autres fonctions
echo "Success!"
```

7. Dans votre page de fonction AWS Lambda, accédez à **Layers** et téléversez le fichier `layer.zip`.
    
8. Mettez à jour les fonctions en téléversant les nouveaux fichiers zip.
    
9. Ajoutez la couche à la fonction en cliquant sur **Layers** dans la vue de la fonction.
    

### Étape 5 : Configurer l'application React et téléverser le build vers un bucket S3

Pour configurer notre application React, accédez au dossier `frontend` du dépôt cloné et exécutez `npm install`. Ensuite, lancez `npm run dev` pour démarrer votre environnement de développement. Vous devriez voir l'aperçu dans votre navigateur à l'adresse : [`http://localhost:5173/`](http://localhost:5173/).

Si vous inspectez la page avec les [Chrome DevTools](https://developer.chrome.com/docs/devtools), vous verrez une erreur [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS).

Pour corriger cela :

1. Accédez à votre page API Gateway.
    
2. Cliquez sur **CORS** dans le volet de navigation de gauche.
    
3. Cliquez sur **Configure**.
    
4. Copiez votre URL [localhost](http://localhost) et collez-la dans le champ **Access-Control-Allow-Origin**.
    
5. Ajoutez `GET`, `POST`, `OPTIONS`, `PUT` et `DELETE` dans **Access-Control-Allow-Methods**.
    
6. Cliquez sur **Save**.
    

### Étape 6 : Configurer un Authorizer Amazon API Gateway

AWS Cognito vous aide à sécuriser votre API Gateway. La passerelle valide le jeton d'accès avec Amazon Cognito pour s'assurer qu'il est valide et n'a pas expiré.

1. Accédez à **Amazon Cognito > User pools**.
    
2. Cliquez sur **Create user pool**.
    
3. Sélectionnez **Single-page application (SPA)**.
    
4. Configurez l'authentification et récupérez le Client ID.
    
5. Dans API Gateway, créez un Authorizer de type JWT pointant vers votre pool Cognito.
    
6. Appliquez cet Authorizer à vos routes.
    

### Étape 7 : Créer une distribution CloudFront avec des comportements pour S3 et API Gateway

1. Accédez à **CloudFront**.
    
2. Cliquez sur **Create distribution**.
    
3. Sélectionnez votre bucket S3 comme origine.
    
4. Définissez le chemin d'origine sur `/dist`.
    
5. Activez l'**Origin access control (OAC)**.
    

### Étape 8 : Configurer l'application React et téléverser le build vers un bucket S3

1. Créez un bucket S3 avec un nom unique.
    
2. Dans le dossier frontend, lancez `npm run build`. Cela crée un dossier `dist`.
    
3. Téléversez le contenu du dossier `dist` dans votre bucket S3.
    

## Dépannage de l'erreur Access Denied

Si vous rencontrez une erreur « Access Denied » dans le navigateur, cela est probablement dû à une erreur de configuration S3 + CloudFront.

### Étape 1 : Configurer l'Origin Access Control (OAC)

1. Allez dans **CloudFront > Votre Distribution > Onglet Origins.**
    
2. Modifiez votre origine S3 et sélectionnez **Origin access control settings (recommended)**.
    

### Étape 2 : Mettre à jour la politique du bucket S3

Copiez la politique fournie par CloudFront et collez-la dans l'onglet **Permissions > Bucket policy** de votre bucket S3.

```json

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowCloudFrontServicePrincipal",
            "Effect": "Allow",
            "Principal": {
                "Service": "cloudfront.amazonaws.com"
            },
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::VOTRE-NOM-DE-BUCKET/*",
            "Condition": {
                "StringEquals": {
                    "AWS:SourceArn": "arn:aws:cloudfront::VOTRE-ID-COMPTE:distribution/VOTRE-ID-DISTRIBUTION"
                }
            }
        }
    ]
}
```

### Étape 3 : Définir l'objet racine par défaut

Dans l'onglet **General** de votre distribution CloudFront, définissez l'**Objet racine par défaut** sur `index.html`.

## Conclusion

Félicitations ! Vous venez de construire une application serverless prête pour la production en partant de zéro. Vous avez conçu avec succès un système CRUD complet qui s'adapte automatiquement, reste sécurisé avec l'authentification Cognito et ne vous coûte que ce que vous utilisez réellement.