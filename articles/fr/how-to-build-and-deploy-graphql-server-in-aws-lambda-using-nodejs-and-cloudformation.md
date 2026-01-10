---
title: Comment construire et déployer un serveur GraphQL dans AWS Lambda en utilisant
  Node.js et CloudFormation
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-19T20:42:16.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-and-deploy-graphql-server-in-aws-lambda-using-nodejs-and-cloudformation
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/banner.png
tags:
- name: aws lambda
  slug: aws-lambda
- name: cloudformation
  slug: cloudformation
- name: GraphQL
  slug: graphql
- name: node
  slug: node
seo_title: Comment construire et déployer un serveur GraphQL dans AWS Lambda en utilisant
  Node.js et CloudFormation
seo_desc: 'By subash adhikari

  Introduction

  I have been building GraphQL APIs in a Serverless environment for over 3 years now.
  I can''t even imagine working with RESTful APIs anymore. Combine the power of GraphQL
  with the scalability of AWS Lambda, and you have ...'
---

Par subash adhikari

# Introduction

Je construis des API GraphQL dans un environnement Serverless depuis plus de 3 ans maintenant. Je ne peux même plus imaginer travailler avec des API RESTful. Combinez la puissance de GraphQL avec la scalabilité d'AWS Lambda, et vous avez un serveur capable de gérer des quantités infinies de trafic.

Dans ce tutoriel, nous allons construire et déployer un serveur GraphQL sur AWS Lambda et y accéder via un point de terminaison API Gateway. Nous utiliserons CloudFormation et l'AWS CLI pour déployer toutes nos ressources AWS et notre code d'application.

## Ce que nous allons couvrir

1. Construire un serveur GraphQL en utilisant Apollo
2. Déployer ce serveur GraphQL sur Lambda
3. Utiliser API Gateway pour proxyfier les requêtes vers Lambda
4. Utiliser CloudFormation pour déployer la pile d'application sur AWS
5. Configurer Lambda pour le développement local.

TL;DR – Vous pouvez obtenir le code source complet de l'application depuis [Github](https://github.com/adikari/apollo-server-lambda-nodejs/tree/server-setup).

# Qu'est-ce que GraphQL ?

[GraphQL](https://graphql.org/) est un langage de requête pour décrire les API en utilisant un système de schéma fortement typé. Un serveur GraphQL remplit ces requêtes en utilisant des données existantes. Voici quelques-uns des principaux avantages de l'utilisation de GraphQL.

## Requêter uniquement ce dont votre application a besoin

Contrairement aux API REST, GraphQL permet aux clients de requêter précisément et uniquement ce dont ils ont besoin. Le serveur répond à la demande du client en retournant uniquement ce que le client demande.

## GraphQL utilise un système fortement typé

Le système fortement typé de GraphQL permet aux utilisateurs d'introspecter l'ensemble du schéma. Et l'API GraphQL sert de documentation claire sur les capacités du serveur et vous notifie des erreurs pendant le développement.

## Vous pouvez composer vos requêtes en une seule demande

Avec GraphQL, vous pouvez requêter plusieurs ressources et obtenir des réponses combinées avec une seule requête. Avec moins de requêtes, les applications utilisant GraphQL fonctionnent beaucoup plus rapidement.

# Qu'est-ce qu'AWS Lambda ?

AWS Lambda est un service de calcul offert par AWS qui vous permet d'exécuter votre code d'application sans avoir à gérer de serveurs. AWS gère toutes les tâches de gestion comme l'infrastructure, la sécurité, les ressources, le système d'exploitation et les correctifs afin que les développeurs puissent se concentrer uniquement sur la construction de l'application.

Commençons...

# Configuration du projet

Commençons par créer un dossier de projet. Ensuite, changez de répertoire et initialisez un projet Node. J'utilise `node 10.x` dans les exemples. Vous pouvez installer la version de Node de votre choix en utilisant [asdf](https://github.com/asdf-vm/asdf).

```bash
mkdir apollo-server-lambda-nodejs 
cd apollo-server-lambda-nodejs 
yarn init
```

Ensuite, créez un dossier qui contiendra tout notre code source.

```bash
mkdir src
```

Enfin, créez un fichier index à l'intérieur du répertoire `src` qui servira de gestionnaire lambda.

```bash
cd src
touch index.js
```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/initialize.png)
_Initialiser le projet node_

Remplissez le fichier index avec le code suivant.

```javascript
exports.handler = async () => {  
    return { 
        body: 'Hello from Lambda' 
    };
};
```

Le code ci-dessus est un gestionnaire Lambda très simple qui retournera `Hello from Lambda` lorsqu'il sera invoqué. Déployons d'abord notre code sur AWS Lambda.

# Emballer le code de l'application

Avant de pouvoir déployer notre code sur Lambda, nous devons créer une archive zip de notre application et la télécharger dans un bucket S3. Nous utilisons AWS CLI pour créer le bucket. Configurez AWS CLI maintenant en suivant [ce guide](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) si vous ne l'avez pas déjà fait.

Créez un bucket S3 à utiliser pour déployer notre code sur Lambda. Choisissez un nom unique pour votre bucket S3. Les noms de bucket sont uniques globalement dans toutes les régions AWS.

```bash
aws s3 mb s3://lambda-deploy-asln
```

Créez une archive de l'application en utilisant la commande zip et vérifiez les fichiers à l'intérieur de l'archive.

```bash
zip -rq dist-latest.zip src package.json 
zipinfo dist-latest.zip
```

Copiez le fichier zip vers S3 en utilisant la commande AWS CLI.

```bash
aws s3 cp dist-latest.zip s3://lambda-deploy-asln/dist-latest.zip
```

Enfin, utilisez la commande suivante pour vérifier que le fichier existe dans S3.

```bash
aws s3 ls s3://lambda-deploy-asln
```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/2-1.png)
_Copier le package de l'application vers S3_

Maintenant que nous avons déployé l'application emballée sur S3, nous devons ensuite configurer notre Lambda et API Gateway dans AWS. Dans la section suivante, nous utiliserons CloudFormation pour configurer toutes les ressources AWS nécessaires.

# Configurer AWS Lambda avec l'intégration proxy API Gateway

CloudFormation est un service AWS qui nous aide à écrire l'infrastructure en tant que code. CloudFormation rend très simple la création et la gestion de nos ressources d'application. Utilisons CloudFormation pour définir notre pile.

Créez un fichier nommé `cloudformation.yml` à la racine du projet.

```bash
touch cloudformation.yml
```

Ajoutez le code suivant au fichier `cloudformation.yml`

```yaml
---
Description: Serveur GraphQL sur AWS Lambda

Parameters:
  Version:
    Description: Numéro de version de l'application
    Type: String

  BucketName:
    Description: Nom du bucket S3 où se trouve le code source
    Type: String

Resources:
  LambdaFunction:
    Type: AWS::Lambda::Function
    Properties:
      Code:
        S3Bucket: !Ref BucketName
        S3Key: !Sub dist-${Version}.zip
      Handler: src/index.handler
      Description: Serveur GraphQL Apollo
      Role: !GetAtt LambdaExecutionRole.Arn
      Runtime: nodejs10.x
      Timeout: 10

  LambdaExecutionRole:
    Type: "AWS::IAM::Role"
    Properties:
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: "Allow"
            Principal:
              Service:
                - "lambda.amazonaws.com"
            Action:
              - "sts:AssumeRole"
      Policies:
        - PolicyName: "LambdaFunctionPolicy"
          PolicyDocument:
            Version: '2012-10-17'
            Statement:
            - Effect: Allow
              Action:
              - logs:CreateLogGroup
              - logs:CreateLogStream
              - logs:PutLogEvents
              Resource: "*"

  GraphQLApi:
    Type: 'AWS::ApiGateway::RestApi'
    Properties:
      Name: apollo-graphql-api

  GraphQLApiResource:
    Type: 'AWS::ApiGateway::Resource'
    Properties:
      ParentId: !GetAtt GraphQLApi.RootResourceId
      RestApiId: !Ref GraphQLApi
      PathPart: 'graphql'

  GraphQLApiMethod:
    Type: 'AWS::ApiGateway::Method'
    Properties:
      RestApiId: !Ref GraphQLApi
      ResourceId: !Ref GraphQLApiResource
      AuthorizationType: None
      HttpMethod: POST
      Integration:
        Type: AWS_PROXY
        IntegrationHttpMethod: POST
        Uri: !Sub arn:aws:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${LambdaFunction.Arn}/invocations

  GraphQLApiDeployment:
    Type: 'AWS::ApiGateway::Deployment'
    Properties:
      RestApiId: !Ref GraphQLApi
      StageName: v1
    DependsOn:
      - GraphQLApiResource
      - GraphQLApiMethod

  GraphQLApiPermission:
    Type: 'AWS::Lambda::Permission'
    Properties:
      Action: lambda:invokeFunction
      FunctionName: !GetAtt LambdaFunction.Arn
      Principal: apigateway.amazonaws.com
      SourceArn: !Sub arn:aws:execute-api:${AWS::Region}:${AWS::AccountId}:${GraphQLApi}/*

Outputs:
  ApiUrl:
    Description: URL d'invocation du point de terminaison API Gateway
    Value: !Sub https://${GraphQLApi}.execute-api.${AWS::Region}.amazonaws.com/v1/graphql
```

Je sais qu'il se passe beaucoup de choses dans ce modèle. Examinons le code étape par étape.

## Paramètres du modèle

Tout d'abord, nous définissons quelques paramètres que nous utilisons dans le modèle. Nous pouvons passer ces variables en tant que substitutions de paramètres lors du déploiement de la pile CloudFormation.

```yaml
Description: Serveur GraphQL sur AWS Lambda

Parameters:
  Version:
    Description: Numéro de version de l'application
    Type: String

  BucketName:
    Description: Nom du bucket S3 où se trouve le code source
    Type: String
```

## Fonction Lambda

Nous définissons notre fonction lambda en spécifiant le chemin à partir duquel elle doit extraire le code de l'application. Ce bucket est le même que celui que nous avons créé précédemment.

```yaml
LambdaFunction:
    Type: AWS::Lambda::Function
    Properties:
      Code:
        S3Bucket: !Ref BucketName
        S3Key: !Sub dist-${Version}.zip
      Handler: src/index.handler
      Description: Serveur GraphQL Apollo
      Role: !GetAtt LambdaExecutionRole.Arn
      Runtime: nodejs10.x
      Timeout: 10
```

Nous voulons que notre fonction Lambda puisse envoyer des logs d'application à AWS CloudWatch. Lambda nécessite des permissions spéciales pour pouvoir écrire des logs dans CloudWatch. Nous créons donc un rôle qui permet d'écrire dans CloudWatch et l'assignons à la fonction Lambda.

```yaml
LambdaExecutionRole:
    Type: "AWS::IAM::Role"
    Properties:
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: "Allow"
            Principal:
              Service:
                - "lambda.amazonaws.com"
            Action:
              - "sts:AssumeRole"
      Policies:
        - PolicyName: "LambdaFunctionPolicy"
          PolicyDocument:
            Version: '2012-10-17'
            Statement:
            - Effect: Allow
              Action:
              - logs:CreateLogGroup
              - logs:CreateLogStream
              - logs:PutLogEvents
              Resource: "*"
```

## API Gateway

Nous voulons également un point de terminaison HTTP pour invoquer la fonction lambda. API Gateway peut être utilisé pour créer un point de terminaison HTTP. Nous pouvons ensuite configurer API Gateway pour proxyfier toutes les requêtes entrantes du client vers la fonction Lambda et envoyer la réponse de Lambda au client.

Tout d'abord, nous créons une API Gateway RestApi.

```yaml
GraphQLApi:
    Type: 'AWS::ApiGateway::RestApi'
    Properties:
      Name: apollo-graphql-api
```

Ensuite, nous créons une ressource API Gateway, qui accepte les requêtes à `/graphql`.

```yaml
GraphQLApiResource:
    Type: 'AWS::ApiGateway::Resource'
    Properties:
      ParentId: !GetAtt GraphQLApi.RootResourceId
      RestApiId: !Ref GraphQLApi
      PathPart: 'graphql'
```

Ensuite, nous configurons la ressource pour accepter les requêtes POST en créant une méthode API Gateway, puis nous l'intégrons avec Lambda.

```yaml
GraphQLApiMethod:
    Type: 'AWS::ApiGateway::Method'
    Properties:
      RestApiId: !Ref GraphQLApi
      ResourceId: !Ref GraphQLApiResource
      AuthorizationType: None
      HttpMethod: POST
      Integration:
        Type: AWS_PROXY
        IntegrationHttpMethod: POST
        Uri: !Sub arn:aws:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${LambdaFunction.Arn}/invocations
```

Enfin, nous créons un déploiement API Gateway qui déploie l'API à l'étape spécifiée.

```yaml
GraphQLApiDeployment:
    Type: 'AWS::ApiGateway::Deployment'
    Properties:
      RestApiId: !Ref GraphQLApi
      StageName: v1
    DependsOn:
      - GraphQLApiResource
      - GraphQLApiMethod
```

## Permission Lambda / API Gateway

À ce stade, nous avons à la fois la fonction Lambda et API Gateway configurées correctement. Cependant, API Gateway a besoin d'une permission spéciale pour invoquer une fonction Lambda. Nous permettons à API Gateway d'invoquer Lambda en créant une ressource de permission Lambda.

```yaml
GraphQLApiPermission:
    Type: 'AWS::Lambda::Permission'
    Properties:
      Action: lambda:invokeFunction
      FunctionName: !GetAtt LambdaFunction.Arn
      Principal: apigateway.amazonaws.com
      SourceArn: !Sub arn:aws:execute-api:${AWS::Region}:${AWS::AccountId}:${GraphQLApi}/*
```

Enfin, nous exportons l'URL de l'API à la fin du modèle. Nous pouvons utiliser cette URL pour invoquer des appels à Lambda.

```yaml
Outputs:
  ApiUrl:
    Description: URL d'invocation du point de terminaison API Gateway
    Value: !Sub https://${GraphQLApi}.execute-api.${AWS::Region}.amazonaws.com/v1/graphql
```

# Déployer la pile CloudFormation sur AWS

Maintenant que nous avons le modèle CloudFormation prêt, utilisons la commande AWS CLI pour le déployer sur AWS.

Exécutez la commande suivante dans votre console. Assurez-vous de mettre à jour le BucketName avec le nom du bucket que vous avez créé précédemment.

```bash
aws cloudformation deploy \
  --template-file ./cloudformation.yml \
  --stack-name apollo-server-lambda-nodejs \
  --parameter-overrides BucketName=lambda-deploy-asln Version=latest \
  --capabilities CAPABILITY_IAM
```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/3-1.png)
_Déployer la pile CloudFormation sur AWS_

Il peut prendre un certain temps pour déployer la pile. La fonction Lambda devrait être prête à commencer à traiter les requêtes lorsque le déploiement est terminé.

# Vérifier que API Gateway et Lambda fonctionnent comme prévu

Maintenant que nous avons déployé notre pile CloudFormation, vérifions si tout fonctionne comme prévu. Nous avons besoin de l'URL API Gateway pour envoyer une requête à notre fonction Lambda. L'URL de l'API que nous avons exportée dans le modèle CloudFormation est utile ici.

Exécutez la commande suivante pour imprimer l'URL de l'API dans la ligne de commande.

```bash
aws cloudformation describe-stacks \
--stack-name=apollo-server-lambda-nodejs \
--query "Stacks[0].Outputs[?OutputKey=='ApiUrl'].OutputValue" \
--output text

```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/4-1.png)
_Décrire la pile CloudFormation_

Maintenant, utilisez la commande `curl` pour invoquer l'URL de l'API. Vous devriez obtenir "Hello from Lambda" en retour du serveur.

```bash
curl -d '{}' https://o55ybz0sc5.execute-api.us-east-1.amazonaws.com/v1/graphql
```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/5.png)
_Invoquer AWS Lambda_

# Ajouter un script de déploiement pour un déploiement plus facile

Vous avez peut-être remarqué que nous avons exécuté un tas de commandes pour emballer et déployer notre application. Il serait très fastidieux de devoir exécuter ces commandes à chaque fois que nous déployons l'application. Ajoutons un script bash pour simplifier ce flux de travail.

Créez un répertoire appelé `bin` à la racine de l'application et ajoutez un fichier nommé `deploy`.

```bash
mkdir bin 
touch bin/deploy
```

Avant de pouvoir exécuter le script, nous devons définir les permissions correctes pour le fichier. Faisons cela en exécutant la commande suivante.

```bash
chmod +x bin/deploy
```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/6.png)
_Créer un script de déploiement_

À ce stade, notre structure de répertoire devrait ressembler à celle de la capture d'écran ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/7.png)
_Structure de répertoire actuelle_

Ajoutez le code suivant au fichier.

```bash
#!/bin/bash

set -euo pipefail

OUTPUT_DIR=dist
CURRENT_DIR=$(pwd)
ROOT_DIR="$( dirname "${BASH_SOURCE[0]}" )"/..
APP_VERSION=$(date +%s)
STACK_NAME=apollo-server-lambda-nodejs

cd $ROOT_DIR

echo "Nettoyage de l'ancienne build.."
[ -d $OUTPUT_DIR ] && rm -rf $OUTPUT_DIR

mkdir dist

echo "Compression du code source.."
zip -rq $OUTPUT_DIR/dist-$APP_VERSION.zip src node_modules package.json

echo "Téléchargement du code source vers s3.."
aws s3 cp $OUTPUT_DIR/dist-$APP_VERSION.zip s3://$S3_BUCKET/dist-$APP_VERSION.zip

echo "Déploiement de l'application.."
aws cloudformation deploy \
  --template-file $ROOT_DIR/cloudformation.yml \
  --stack-name $STACK_NAME \
  --parameter-overrides Version=$APP_VERSION BucketName=$S3_BUCKET \
  --capabilities CAPABILITY_IAM

# Obtenir l'URL de l'API à partir de la sortie de la pile cloudformation
API_URL=$(
  aws cloudformation describe-stacks \
  --stack-name=$STACK_NAME \
  --query "Stacks[0].Outputs[?OutputKey=='ApiUrl'].OutputValue" \
  --output text
)

echo -e "\n$API_URL"

cd $CURRENT_DIR
```

D'accord, décomposons ce qui se passe dans ce script.

Nous commençons par définir quelques variables. Nous générons le fichier d'archive à l'intérieur du répertoire `dist`. Nous définissons la version de l'application à l'horodatage actuel auquel le script s'exécute. En utilisant l'horodatage, nous pouvons nous assurer que le numéro de version est toujours unique et incrémental.

```bash
#!/bin/bash

set -euo pipefail

OUTPUT_DIR=dist
CURRENT_DIR=$(pwd)
ROOT_DIR="$( dirname "${BASH_SOURCE[0]}" )"/..
APP_VERSION=$(date +%s)
STACK_NAME=apollo-server-lambda-nodejs
```

Nous nettoyons ensuite les anciennes builds et créons un nouveau répertoire `dist`.

```bash
echo "Nettoyage de l'ancienne build.."
[ -d $OUTPUT_DIR ] && rm -rf $OUTPUT_DIR

mkdir dist
```

Ensuite, nous exécutons la commande zip pour archiver le code source et ses dépendances.

```bash
echo "Compression du code source.."
zip -rq $OUTPUT_DIR/dist-$APP_VERSION.zip src node_modules package.json
```

Ensuite, nous copions le fichier zip dans le bucket S3.

```bash
echo "Téléchargement du code source vers s3.."
aws s3 cp $OUTPUT_DIR/dist-$APP_VERSION.zip s3://$S3_BUCKET/dist-$APP_VERSION.zip
```

Ensuite, nous déployons la pile CloudFormation.

```bash
echo "Déploiement de l'application.."
aws cloudformation deploy \
  --template-file $ROOT_DIR/cloudformation.yml \
  --stack-name $STACK_NAME \
  --parameter-overrides Version=$APP_VERSION BucketName=$S3_BUCKET \
  --capabilities CAPABILITY_IAM
```

Enfin, nous interrogeons la pile CloudFormation pour obtenir l'URL de l'API à partir des sorties CloudFormation et l'imprimons dans la console.

```bash
# Obtenir l'URL de l'API à partir de la sortie de la pile cloudformation
API_URL=$(
  aws cloudformation describe-stacks \
  --stack-name=$STACK_NAME \
  --query "Stacks[0].Outputs[?OutputKey=='ApiUrl'].OutputValue" \
  --output text
)

echo -e "\n$API_URL"
```

# Déployer sur AWS en utilisant le script de déploiement

Essayons le déploiement en utilisant le script de déploiement. Le script s'attend à ce que la variable S3_Bucket soit présente dans l'environnement. Exécutez la commande suivante pour exécuter le déploiement. Lorsque le déploiement est réussi, le script sortira l'URL de l'API que nous pouvons utiliser pour invoquer la lambda.

```bash
S3_BUCKET=lambda-deploy-asln ./bin/deploy
```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/8.png)
_Exécuter le script de déploiement_

Pour simplifier encore plus cela, invoquons-le en utilisant yarn. Ajoutez ce qui suit dans votre `package.json`.

```json
"scripts": {
  "deploy": "S3_BUCKET=lambda-deploy-asln ./bin/deploy"
}
```

Désormais, nous pouvons simplement exécuter `yarn deploy` pour initier les déploiements.

# Améliorer le flux de travail avec Lambda local et API Gateway

Nous avons fréquemment modifié le code de l'application en travaillant sur notre application. Actuellement, le déploiement sur la région AWS us-east-1 me prend environ 10 secondes. Je suis sur une connexion internet avec une vitesse de téléchargement de 40 Mb/s.

Le temps de déploiement devient plus significatif à mesure que la taille de l'application grandit. Attendre 10 secondes ou plus pour réaliser que j'ai fait une erreur de syntaxe n'est pas productif du tout.

Corrigeons cela en configurant la fonction lambda localement et en l'invoquant en utilisant un point de terminaison API local. AWS SAM CLI nous permet de faire exactement cela. Suivez les instructions sur [cette page](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) pour l'installer.

Une fois terminé, depuis la racine du projet, exécutez la commande suivante.

```bash
sam local start-api --template-file cloudformation.yml
```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/9.png)
_Démarrer le serveur de développement local_

Le point de terminaison local est maintenant disponible à l'adresse [http://localhost:3000](http://localhost:3000/). Nous pouvons utiliser ce point de terminaison pour envoyer des requêtes à notre Lambda local.

Ouvrez un autre terminal et exécutez la commande suivante pour envoyer une requête. Vous devriez voir la réponse de notre fonction Lambda locale.

```bash
curl -d '{}' http://localhost:3000/graphql
```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/10.png)
_Invoquer la fonction lambda locale_

Enfin, ajoutez les lignes suivantes dans la section `scripts` du `package.json`.

```json
"dev": "sam local start-api --template-file cloudformation.yml"
```

Désormais, nous pouvons exécuter la commande `yarn dev` pour démarrer le serveur de développement.

# Configurer le serveur GraphQL dans Lambda

Sans plus attendre, plongeons directement dans le code et construisons le serveur GraphQL.

Commencez par installer les dépendances. Nous utilisons [Apollo Server](https://www.apollographql.com/docs/apollo-server/) pour construire notre serveur GraphQL. Apollo Server est une implémentation open-source de GraphQL Server.

```bash
yarn add apollo-server-lambda graphql
```

Remplacez le contenu de `src/index.js` par le code suivant.

```javascript
const { ApolloServer, gql } = require('apollo-server-lambda');

const typeDefs = gql`
  type Query {
    user: User
  }

  type User {
    id: ID
    name: String
  }
`;

const resolvers = {
  Query: {
    user: () => ({ id: 123, name: 'John Doe' })
  }
};

const server = new ApolloServer({ typeDefs, resolvers });

exports.handler = server.createHandler();
```

Ici, nous définissons un schéma qui se compose d'un type User et d'une requête user. Nous définissons ensuite un resolver pour la requête user. Pour simplifier, le resolver retourne un utilisateur codé en dur. Enfin, nous créons un gestionnaire GraphQL et l'exportons.

Pour effectuer des requêtes sur notre serveur GraphQL, nous avons besoin d'un client GraphQL. [Insomnia](https://insomnia.rest/download/core/) est mon client préféré. Cependant, tout autre client GraphQL devrait convenir.

Maintenant, exécutons une requête pour nous assurer que notre serveur fonctionne comme prévu.

Créez une nouvelle requête GraphQL dans Insomnia.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/a.png)
_Créer une nouvelle requête GraphQL_

![Image](https://www.freecodecamp.org/news/content/images/2020/05/b.png)
_Configurer la requête GraphQL_

Ajoutez la requête suivante dans le corps et soumettez la requête à `http://localhost:3000`. En supposant que votre serveur de développement est toujours en cours d'exécution, vous devriez voir la réponse suivante du serveur GraphQL.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/c.png)
_Effectuer une requête GraphQL vers le serveur local_

Maintenant que nous avons vérifié que tout fonctionne bien sur le serveur local, exécutons la commande suivante pour déployer le serveur GraphQL sur AWS.

```bash
yarn deploy
```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/d-1.png)
_Déployer le serveur sur AWS_

L'URL de l'API est affichée dans la console une fois le déploiement terminé. Remplacez l'URL dans Insomnia par celle de l'API Gateway. Réexécutez la requête pour voir sa résolution.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/e-1.png)
_Effectuer une requête GraphQL vers AWS Lambda_

# Résumé

Félicitations, vous avez déployé avec succès un serveur GraphQL dans AWS Lambda en utilisant uniquement CloudFormation. Le serveur peut recevoir des requêtes GraphQL du client et retourner la réponse en conséquence.

Nous avons également configuré l'environnement de développement pour le développement local sans ajouter de nombreuses dépendances.

Si vous avez aimé ce tutoriel, veuillez le partager avec votre réseau.