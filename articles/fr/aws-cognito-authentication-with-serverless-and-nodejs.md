---
title: Comment configurer l'authentification AWS Cognito avec Serverless et NodeJS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-05T20:15:00.000Z'
originalURL: https://freecodecamp.org/news/aws-cognito-authentication-with-serverless-and-nodejs
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/feature-psd-1.png
tags:
- name: AWS
  slug: aws
- name: node js
  slug: node-js
- name: serverless
  slug: serverless
- name: Tutorial
  slug: tutorial
- name: Web Development
  slug: web-development
seo_title: Comment configurer l'authentification AWS Cognito avec Serverless et NodeJS
seo_desc: "By Shivang\nIn this post, we are going to see how we can create a REST\
  \ API application for authentication using AWS Cognito, AWS Serverless, and NodeJS.\
  \ \nWe are going to use Lambda functions, API Gateway, and the Serverless framework\
  \ to achieve this.\n..."
---

Par Shivang

Dans cet article, nous allons voir comment créer une application API REST pour l'authentification en utilisant AWS Cognito, AWS Serverless et NodeJS.

Nous allons utiliser des fonctions Lambda, API Gateway et le framework Serverless pour y parvenir.

Commençons par configurer le projet.

## **Installation du projet**

La structure de notre projet ressemblera à ceci :

![structure des dossiers du projet aws cognito](https://devswisdom.com/wp-content/uploads/2021/12/folder-structure.png)

Comme vous pouvez le voir, nous stockons tous nos fichiers de fonctions lambda dans un dossier nommé _user_ et toutes nos fonctions utilitaires dans un dossier séparé appelé _functions_. En plus de cela, il y a un fichier _serverless.yml_ qui est un fichier central pour tout projet basé sur serverless.

Si vous souhaitez en savoir plus sur ce fichier, consultez [cet](https://devswisdom.com/use-websockets-with-aws-serverless/) article.

## **Fichier Serverless.yml**

Commençons à coder notre fichier _serverless.yml_ où nous allons définir toutes nos fonctions lambda. Il contiendra notre logique pour l'inscription, la connexion, et ainsi de suite.

Nous allons également définir notre groupe d'utilisateurs AWS Cognito et le client du groupe d'utilisateurs avec différents paramètres et permissions.

Découpons ce fichier en différentes parties afin de comprendre chaque partie séparément.

### **Comment définir les permissions et paramètres AWS IAM**

Nous allons commencer par définir des éléments tels que les variables d'environnement, la configuration du projet serverless, les paramètres et les permissions AWS IAM.

```yaml
service: serverless-cognito-auth

provider:
  name: aws
  runtime: nodejs14.x
  environment:
    user_pool_id: { Ref: UserPool }
    client_id: { Ref: UserClient }
  iamRoleStatements:
    - Effect: Allow
      Action:
        - cognito-idp:AdminInitiateAuth
        - cognito-idp:AdminCreateUser
        - cognito-idp:AdminSetUserPassword
      Resource: "*"
```

Dans le bloc `provider`, nous définissons plusieurs configurations et paramètres. Discutons de chaque partie brièvement.

#### `environment`

Dans ce bloc, nous définissons toutes nos variables d'environnement que nous voulons utiliser dans notre projet, comme dans nos fonctions lambda, etc.

Nous définissons l'identifiant du groupe d'utilisateurs et l'identifiant du client de notre groupe d'utilisateurs et client AWS Cognito.

Et nous faisons également référence aux ressources que nous allons définir plus tard dans ce fichier, donc ne vous inquiétez pas de cela. Comprenez simplement que ces références vont nous donner l'identifiant pour le groupe d'utilisateurs et le client créés.

#### `iamRoleStatements`

Dans ce bloc, nous définissons toutes les permissions AWS IAM que nous voulons donner à nos ressources. Dans notre cas, ces permissions sont requises par nos fonctions lambda qui vont utiliser l'API AWS Cognito.

Pour en savoir plus sur AWS IAM, consultez la [documentation officielle](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html).

### **Comment définir les fonctions lambda**

Ensuite, nous allons définir nos fonctions lambda. Nous allons en avoir besoin de trois : une pour l'inscription des utilisateurs, une pour la connexion des utilisateurs et la dernière pour tester une route privée.

```yaml
functions:
  loginUser:
    handler: user/login.handler
    events:
      - http:
          path: user/login
          method: post
          cors: true

  signupUser:
    handler: user/signup.handler
    events:
      - http:
          path: user/signup
          method: post
          cors: true

  privateAPI:
    handler: user/private.handler
    events:
      - http:
          path: user/private
          method: post
          cors: true
          authorizer:
            name: PrivateAuthorizer
            type: COGNITO_USER_POOLS
            arn:
              Fn::GetAtt:
                - UserPool
                - Arn
            claims:
              - email
```

Dans le bloc `events`, nous définissons l'événement sur lequel notre fonction lambda sera invoquée. Dans notre cas, nous ajoutons un événement HTTP ici, qui sera notre appel AWS API Gateway.

**`authorizer`** – Ici, nous définissons notre autorisateur qui sera appelé avant que notre fonction lambda principale ne soit invoquée. Nous utilisons donc ici l'autorisateur AWS Cognito pour notre API Gateway qui vérifie à chaque requête si le jeton d'accès valide est passé avec celle-ci. Et seulement alors, il permet à notre fonction lambda principale d'être invoquée.

Nous devons passer l'ARN de notre groupe d'utilisateurs AWS Cognito, donc nous faisons référence à cette ressource et obtenons l'ARN de celle-ci en utilisant la fonction `:GetAtt`.

Nous utilisons également le bloc `claims` pour avoir les champs spécifiques disponibles à partir de l'objet de jeton d'accès décodé dans notre fonction lambda principale dans l'objet d'événement.

### **Comment définir les ressources**

Enfin, nous allons définir toutes les ressources dont nous avons besoin dans notre fichier _serverless.yml_.

```yaml
resources:
  Resources:
    UserPool:
      Type: AWS::Cognito::UserPool
      Properties:
        UserPoolName: serverless-auth-pool
        Schema:
          - Name: email
            Required: true
            Mutable: true
        Policies:
          PasswordPolicy:
            MinimumLength: 6
        AutoVerifiedAttributes: ["email"]

    UserClient:
      Type: AWS::Cognito::UserPoolClient
      Properties:
        ClientName: user-pool-ui
        GenerateSecret: false
        UserPoolId: { Ref: UserPool }
        AccessTokenValidity: 5
        IdTokenValidity: 5
        ExplicitAuthFlows:
          - "ADMIN_NO_SRP_AUTH"
```

Ici, nous créons notre groupe d'utilisateurs et client AWS Cognito. Passons en revue certaines des options maintenant. Si vous souhaitez voir toutes les options que vous pouvez utiliser, consultez cette [documentation officielle](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html) et [celle-ci](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html) également pour le client du groupe d'utilisateurs.

**`Schema`** – Ici, nous définissons le schéma des données utilisateur qui seront créées dans notre groupe d'utilisateurs. Nous pouvons définir différents attributs comme l'email, l'âge, le genre, etc.

**`Policies`** – Dans ce bloc, nous définissons notre politique de validation du mot de passe – donc essentiellement tous les paramètres de la façon dont le mot de passe doit être avant de pouvoir être enregistré dans notre groupe d'utilisateurs.

**`AutoVerifiedAttributes`** – Ici, nous pouvons définir les champs que nous voulons être automatiquement vérifiés comme l'email et le numéro de téléphone. Généralement, lorsqu'un nouvel utilisateur est créé dans le groupe d'utilisateurs AWS Cognito, cet utilisateur doit passer par un processus de vérification pour vérifier son email ou son numéro de téléphone. Mais définir ce champ ici va sauter ce processus de vérification pour l'utilisateur créé.

**`AccessTokenValidity`** – Cela définit le nombre d'heures pendant lesquelles le jeton d'accès sera valide.

**`ExplicitAuthFlows`** – Cela définit tous les flux d'authentification qui seront autorisés par le client du groupe d'utilisateurs. Nous allons utiliser `ADMIN_NO_SRP_AUTH` qui peut être utilisé pour autoriser les utilisateurs avec un nom d'utilisateur et un mot de passe – c'est pourquoi nous le passons ici comme valeur.

Je vous encourage également à consulter la [documentation officielle](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html) d'AWS Cognito.

## **Comment coder les fonctions lambda**

Il est maintenant temps de commencer à coder la logique de notre API REST en créant des fonctions lambda pour l'inscription des utilisateurs, la connexion des utilisateurs et notre route privée pour tout tester.

### **Inscription de l'utilisateur**

Tout d'abord, nous allons créer un nouveau fichier dans le dossier _user_ et le nommer _signup.js_. Ce fichier contiendra toute la logique liée à l'inscription des utilisateurs. Voyons à quoi ressemblera le code dans ce fichier en le découpant en parties.

#### **Imports**

```javascript
const AWS = require('aws-sdk')
const { sendResponse, validateInput } = require("../functions");

const cognito = new AWS.CognitoIdentityServiceProvider()
```

Nous allons utiliser `aws-sdk` NPM pour interagir avec l'API AWS Cognito. Nous importons également deux fonctions utilitaires (consultez le code) : `sendResponse` pour envoyer la réponse de la requête HTTP, et `validateInput` pour valider les données du corps de la requête.

Nous obtenons également l'instance du fournisseur d'identité Cognito pour interagir avec l'API du groupe d'utilisateurs.

#### **Comment valider les données du corps de la requête**

```javascript
const isValid = validateInput(event.body)
if (!isValid)
return sendResponse(400, { message: 'Entrée invalide' })
```

Ici, nous validons les données du corps de la requête et vérifions si les données sont valides ou non. Si elles ne sont pas valides, nous retournons la réponse et envoyons un message approprié.

#### **Comment créer un utilisateur dans le groupe d'utilisateurs AWS Cognito**

```javascript
const {
 email,
 password
 } = JSON.parse(event.body)
const {
 user_pool_id
 } = process.env

const params = {
  UserPoolId: user_pool_id,
  Username: email,
  UserAttributes: [{
      Name: 'email',
      Value: email
    },
    {
      Name: 'email_verified',
      Value: 'true'
    }
  ],
  MessageAction: 'SUPPRESS'
}
const response = await cognito.adminCreateUser(params).promise();
```

Ici, nous obtenons l'email et le mot de passe du corps de la requête et également l'identifiant du groupe d'utilisateurs de l'objet des variables d'environnement.

Après cela, nous créons un objet de paramètres pour l'API `adminCreateUser`. `MessageAction` est défini comme 'SUPPRESS' car nous ne voulons pas envoyer l'email par défaut envoyé par AWS Cognito lorsqu'un nouvel utilisateur est créé dans le groupe d'utilisateurs.

#### **Comment définir le mot de passe pour l'utilisateur créé**

```javascript
if (response.User) {
  const paramsForSetPass = {
    Password: password,
    UserPoolId: user_pool_id,
    Username: email,
    Permanent: true
  };
  await cognito.adminSetUserPassword(paramsForSetPass).promise()
}
return sendResponse(200, {
  message: 'Inscription de l\'utilisateur réussie'
})
```

Lorsque notre utilisateur est créé dans le groupe d'utilisateurs, nous devons définir le mot de passe pour cet utilisateur. Nous faisons cela car nous ne voulons pas que les utilisateurs créent un mot de passe lorsqu'ils se connectent puisqu'ils envoient déjà leur mot de passe dans la requête HTTP.

Cela changera également le statut de l'utilisateur en CONFIRMÉ dans le groupe d'utilisateurs Cognito.

Nous devons également passer `Permanent` comme `true` car sinon un mot de passe temporaire sera généré pour l'utilisateur.

### **Connexion de l'utilisateur**

Maintenant, nous allons commencer avec la connexion de l'utilisateur en créant un fichier dans le dossier _user_ nommé _login.js_. Cette API de connexion démarrera le processus d'authentification et enverra le jeton d'identité à l'utilisateur qui pourra l'utiliser pour accéder aux routes autorisées.

_login.js_ ressemblera beaucoup à _signup.js_. La seule différence sera les paramètres et l'appel de l'API.

#### **Comment démarrer le processus d'authentification**

```javascript
const {
  email,
  password
} = JSON.parse(event.body)
const {
  user_pool_id,
  client_id
} = process.env

const params = {
  AuthFlow: "ADMIN_NO_SRP_AUTH",
  UserPoolId: user_pool_id,
  ClientId: client_id,
  AuthParameters: {
    USERNAME: email,
    PASSWORD: password
  }
}
const response = await cognito.adminInitiateAuth(params).promise();
return sendResponse(200, {
  message: 'Succès',
  token: response.AuthenticationResult.IdToken
})
```

La chose principale à comprendre dans ce code est que nous utilisons `AuthFlow` comme ADMIN_NO_SRP_AUTH qui est utilisé pour authentifier l'utilisateur en fonction du nom d'utilisateur et du mot de passe. Après cela, nous appelons simplement l'API `adminInitiateAuth` et envoyons le jeton d'identité à l'utilisateur.

### **Route privée**

Nous allons ajouter une fonction lambda supplémentaire qui agira comme une route privée. Pour accéder à ce point de terminaison API, nous devrons envoyer un jeton d'identité valide dans l'en-tête de la requête avec la clé 'Authorization'.

Commencez par créer un nouveau fichier dans le dossier _user_ et nommez-le _private.js_.

```javascript
module.exports.handler = async (event) => {
  return sendResponse(200, {
    message: `Email ${event.requestContext.authorizer.claims.email} a été autorisé`
  })
}
```

Ici, nous obtenons simplement l'email de la requête et envoyons une réponse simple. Cette fonction lambda ne sera invoquée que si la requête passe la couche d'autorisation ajoutée dans la configuration de l'API Gateway.

Pour consulter toutes les API offertes par le SDK Nodejs, consultez [ces docs](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/CognitoIdentityServiceProvider.html).

Consultez également comment le [tarif AWS Cognito](https://devswisdom.com/aws-cognito-pricing-and-features-2021/) est calculé par AWS afin de ne dépenser que ce que vous souhaitez.

## **Conclusion**

Vous avez maintenant l'API REST pour l'authentification en utilisant AWS Cognito, AWS Serverless et Nodejs. Félicitations !

Assurez-vous de consulter le code GitHub donné à la fin de cet article. Il y a beaucoup de choses que vous pouvez ajouter ou améliorer dans le code actuel – la validation des données peut être augmentée, la fonctionnalité de mot de passe oublié peut être ajoutée, etc. Je vous laisse faire cela.

Nous pouvons également faire cela avec DynamoDB, consultez [AWS DynamoDB Pricing](https://devswisdom.com/aws-dynamodb-pricing-and-features/) pour en savoir plus.

## **Obtenez le code**

Vous pouvez trouver le [code source sur Github](https://github.com/shivangchauhan7/serverless-auth).

_Vous pouvez [consulter plus d'articles comme celui-ci](https://devswisdom.com/) sur mon site._