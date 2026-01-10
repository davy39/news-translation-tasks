---
title: AWS Serverless – Comment utiliser AWS Rekognition pour identifier des célébrités
  dans des images
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-13T16:47:45.000Z'
originalURL: https://freecodecamp.org/news/use-aws-rekognition-to-identify-celebrities-in-images
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/fe.png
tags:
- name: AWS
  slug: aws
- name: lambda
  slug: lambda
- name: Node.js
  slug: nodejs
- name: serverless
  slug: serverless
- name: Web Development
  slug: web-development
seo_title: AWS Serverless – Comment utiliser AWS Rekognition pour identifier des célébrités
  dans des images
seo_desc: 'By Shivang

  In this article we''re going to learn how to make an application using AWS Serverless
  that lets us identify images of celebrities. We''ll use AWS Rekognition for AI-based
  identification.

  We are going to attach an event to the S3 Bucket so th...'
---

Par Shivang

Dans cet article, nous allons apprendre à créer une application utilisant AWS Serverless qui nous permet d'identifier des images de célébrités. Nous utiliserons AWS Rekognition pour l'identification basée sur l'IA.

Nous allons attacher un événement au bucket S3 afin que, chaque fois qu'un fichier est téléchargé dans le bucket, il invoque une fonction Lambda qui traitera les informations de l'image et les enregistrera dans la table DynamoDB.

Avant d'utiliser DynamoDB, assurez-vous de consulter ce guide sur [AWS DynamoDB Pricing](https://devswisdom.com/aws-dynamodb-pricing-and-features/) pour ne dépenser que ce que vous souhaitez.

## **Spécifications techniques**

Nous allons utiliser des fonctions Lambda pour coder la logique de notre projet et AWS Rekognition pour l'identification d'images basée sur l'IA des célébrités.

Si nous obtenons des données valides de l'API AWS Rekognition, nous allons stocker ces données dans une table DynamoDB.

Toutes ces ressources, à l'exception du bucket S3, seront créées dans le fichier _serverless.yml_.

## **Installation du projet**

Nous allons configurer toutes les choses dont nous avons besoin dans ce projet étape par étape. Tout d'abord, nous passerons en revue le fichier _serverless.yml_. Pour en savoir plus sur ce fichier, consultez [cet article](https://devswisdom.com/use-websockets-with-aws-serverless/). Commençons par la première étape.

![Structure du projet](https://www.freecodecamp.org/news/content/images/2022/01/pt-1.PNG)

La structure de notre dossier de projet devrait ressembler à ceci à la fin de ce tutoriel.

### **Comment configurer le fichier serverless.yml**

Nous allons décomposer le fichier _serverless.yml_ en différentes parties pour le rendre plus facile à comprendre.

#### **Comment configurer les permissions et le projet**

```yaml
service: meta-data-serverless

provider:
  name: aws
  runtime: nodejs12.x
  environment:
    DYNAMO_TABLE_NAME: MetaData
    BUCKET_NAME: new-bucket-caps2
  iamRoleStatements:
    - Effect: Allow
      Action:
        - dynamodb:PutItem
        - rekognition:RecognizeCelebrities
        - s3:Get*
        - s3:List*
      Resource: "*"
```

Dans ce bloc de code, nous définissons différentes variables d'environnement et permissions AWS IAM qui seront accordées à nos fonctions Lambda. Pour notre utilisation, nous devons écrire un élément dans la table DynamoDB, utiliser l'API AWS Rekognition pour faire de l'identification d'images sur l'image, et obtenir le fichier depuis S3 (tout ce que nous avons fait dans le code ci-dessus).

Notez que vous devrez créer un nouveau bucket S3 public et définir le nom de ce bucket ici à la place de "new-bucket-caps2" comme propriété BUCKET_NAME. Pour en savoir plus sur les rôles IAM, consultez la documentation officielle [AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html).

#### **Comment ajouter une fonction lambda**

```yaml
functions:
  processImg:
    handler: src/index.handler
    events:
      - s3:
          bucket: ${self:provider.environment.BUCKET_NAME}
          event: s3:ObjectCreated:*
          existing: true
```

Dans le bloc des fonctions, nous définissons une seule fonction lambda qui sera invoquée lorsqu'un fichier est téléchargé dans le bucket S3.

Comme vous pouvez le voir, nous attachons un événement à cette fonction lambda sur lequel elle sera invoquée. `s3:ObjectCreated` est l'événement lorsqu'un fichier est téléchargé dans le bucket S3.

Nous déclarons également que ce bucket existe déjà en définissant l'option `existing` sur `true`. Assurez-vous donc de créer ce bucket avant de déployer le projet.

Nous faisons également référence à la variable d'environnement pour le nom du bucket que nous avons créée dans la section précédente.

#### **Comment ajouter la configuration de la table DynamoDB**

```javascript
resources:
  Resources:
    UsersDynamoDbTable:
      Type: AWS::DynamoDB::Table
      DeletionPolicy: Retain
      Properties:
        AttributeDefinitions:
          - AttributeName: id
            AttributeType: S
        KeySchema:
          - AttributeName: id
            KeyType: HASH
        ProvisionedThroughput:
          ReadCapacityUnits: 1
          WriteCapacityUnits: 1
        TableName: ${self:provider.environment.DYNAMO_TABLE_NAME}
```

Dans ce bloc, nous définissons notre table DynamoDB et sa configuration. Toute ressource que nous voulons créer sur notre compte AWS est définie sous le bloc des ressources dans le fichier _serverless.yml_. Ici, nous définissons des choses comme les attributs de la table, le schéma de clé et la capacité de débit provisionnée que nous voulons donner à notre table.

Pour les attributs de la table, tous les autres attributs seront ajoutés dynamiquement à la table sauf l'id. Nous allons générer l'id dans le code en utilisant un module appelé UUID.

### **Comment configurer la fonction lambda**

Après avoir créé le fichier _serverless.yml_, il est maintenant temps de créer notre fonction lambda que nous avons définie à l'intérieur du fichier yml. Alors, commençons.

Nous allons à nouveau voir différentes parties de la fonction lambda pour que vous puissiez mieux la comprendre.

#### Importations

```javascript
const AWS = require("aws-sdk");
const {
    v4: uuidv4
} = require('uuid');
const rekognition = new AWS.Rekognition();
const dynamoDb = new AWS.DynamoDB.DocumentClient();
```

Nous importons deux packages, aws-sdk et UUID, pour appeler les API pour DynamoDB et AWS Rekognition. Nous initialisons également des instances de ceux-ci.

#### **Définir les paramètres**

```javascript
const Bucket = event.Records[0].s3.bucket.name;
const Name = decodeURIComponent(event.Records[0].s3.object.key.replace(/\+/g, " "));

const params = {
    Image: {
        S3Object: {
            Bucket,
            Name
        }
    }
};
```

Lorsque notre lambda est appelée par un événement S3, elle reçoit des données sur l'objet qui a été téléchargé dans le bucket S3. Nous obtenons simplement ces données d'objet comme le nom du bucket dans lequel il a été téléchargé et le nom du fichier également.

Après cela, nous passons ces données dans l'objet de paramètres que nous allons passer à l'appel de l'API AWS Rekognition.

#### **Appeler l'API AWS Rekognition**

```javascript
const celebrityData = await rekognition.recognizeCelebrities(params).promise();
if (celebrityData.CelebrityFaces && celebrityData.CelebrityFaces.length) {

    const {
        Name,
        Urls,
        KnownGender,
        Face
    } = celebrityData.CelebrityFaces[0];
    const closelyMatchedEmotion = Face.Emotions.reduce((prev, current) => (prev.Confidence > current.Confidence) ? prev : current)

    const params = {
        TableName: process.env.DYNAMO_TABLE_NAME,
        Item: {
            id: uuidv4(),
            Name,
            readMore: Urls,
            KnownGender,
            closelyMatchedEmotion
        },
        ConditionExpression: "attribute_not_exists(id)"
    };
    await dynamoDb.put(params).promise();
```

Enfin, nous appelons l'API AWS Rekognition avec les paramètres que nous avons déclarés à l'étape précédente. Après avoir obtenu la réponse de l'API, nous vérifions si elle a pu identifier la célébrité ou non.

Si elle a trouvé des données de célébrité, alors nous récupérons des données comme le Nom, le Genre, l'Émotion dans l'image, etc., à partir des données de célébrité identifiées.

Ensuite, nous générons un id en utilisant le package UUID que nous avons importé précédemment. La dernière chose que nous faisons est d'insérer ces données dans la table DynamoDB.

Notez que pour interroger ces données enregistrées avec des attributs non-clés, vous devrez créer un index si vous ne souhaitez pas scanner toute la table. Consultez cet article pour apprendre à créer un [DynamoDB Global Secondary Index](https://devswisdom.com/dynamodb-global-secondary-index-detailed-guide/) en utilisant AWS Serverless.

## **Conclusion**

Si vous êtes arrivé à ce point, alors félicitations ! Vous avez maintenant une application qui identifiera les données de célébrités à partir d'une image.

Vous pouvez maintenant simplement aller dans votre bucket S3 créé et télécharger n'importe quelle image de célébrité, puis attendre quelques secondes, puis vérifier la table DynamoDB pour voir les résultats enregistrés là.

Vous pouvez améliorer cette application de nombreuses manières. Par exemple, vous pouvez ajouter des API comme GET pour obtenir les données et voir les données qui ont été ajoutées à la table DynamoDB. Vous pouvez également utiliser MongoDB à la place de DynamoDB. Pour en savoir plus sur les différences entre ces deux, consultez [DynamoDB Vs MongoDB](https://devswisdom.com/dynamodb-vs-mongodb-detailed-comparison/).

## **Obtenez le code source**

Cliquez [ici](https://github.com/shivangchauhan7/celebrity-recoknition) pour obtenir le code source de cette application.

_Vous pouvez [consulter plus d'articles comme celui-ci](https://devswisdom.com/) sur mon site._