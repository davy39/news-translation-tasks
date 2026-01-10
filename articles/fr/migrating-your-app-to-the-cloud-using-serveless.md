---
title: Comment migrer votre application vers le cloud en utilisant le Serverless
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-08T11:15:56.000Z'
originalURL: https://freecodecamp.org/news/migrating-your-app-to-the-cloud-using-serveless
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/ultimateGuideToMigrating1.91.png
tags:
- name: AWS
  slug: aws
- name: Cloud Computing
  slug: cloud-computing
- name: serverless
  slug: serverless
seo_title: Comment migrer votre application vers le cloud en utilisant le Serverless
seo_desc: 'By Sam Williams

  A step by step guide to migrating an existing software product to run serverlessly
  in the cloud

  You’ve got an app that you run and you''ve heard loads about serverless and the
  benefits. You may have even tried deploying some things wit...'
---

Par Sam Williams

### Un guide étape par étape pour migrer un produit logiciel existant afin qu'il s'exécute sans serveur dans le cloud

Vous avez une application que vous exécutez et vous avez entendu parler du serverless et de ses avantages. Vous avez peut-être même essayé de déployer certaines choses avec le serverless, mais vous souhaitez migrer toute votre application vers le serverless.

Comment faire cela ? Par où commencer ? Devez-vous tout faire en même temps ?

Cet article vous guidera à travers les étapes que vous pouvez suivre pour migrer votre application ou service vers le cloud avec le Serverless.

### 1. APIs simples

Lorsque vous commencez le processus de migration de votre service, il est préférable de commencer par les tâches les plus simples. Cela vous donnera de l'expérience avec le serverless et AWS tout en apportant de la valeur à l'application.

Les APIs simples sont des endpoints qui n'ont pas besoin d'accéder à vos bases de données pour effectuer leurs actions. Cela pourrait être une API pour envoyer des emails, interagir avec des APIs externes et combiner les données, ou pour exécuter une logique sur les entrées.

Un avantage secondaire à créer ces APIs est qu'elles réduisent la charge sur les serveurs existants. Chez MissionLabs, nous avons constaté que cette suppression de fonctionnalités et de complexité nous a permis de réduire le code sur nos serveurs de plus de 50 %. Cela a abouti à un code beaucoup plus lisible et à des corrections de bugs plus rapides.

**Comment migrer**

![Image](https://www.freecodecamp.org/news/content/images/2019/08/lambda-gateway.png)

Heureusement, migrer des APIs simples vers le cloud en utilisant le serverless est vraiment facile avec AWS Lambda et API Gateway.

AWS Lambda est un service de fonctions cloud où vous pouvez exécuter des fonctions de code et ne payer que lorsque la fonction est en cours d'exécution. Vous pouvez écrire votre code en Ruby, Python, Node, Java, Go ou .Net et, via le SDK AWS, vous pouvez facilement accéder à d'autres services AWS (tels que l'email, les SMS, Kinesis, les bases de données).

Pour créer une API en utilisant AWS Lambda et API Gateway, vous devez écrire une fonction qui exécute la logique. Ensuite, vous devez exporter la fonction en tant que `exports.handler`.

```js
exports.handler = async (event, context) => {    
    // votre code de fonction va ici
}
```

Pour déployer votre code avec une API en utilisant le serverless, nous devons ajouter cette nouvelle fonction à notre fichier serverless.yml sous la déclaration de fonction. Vous devez définir l'emplacement du code ainsi que les méthodes et le chemin pour l'endpoint de l'API.

```yml
functions:    
    myFirstApi:
    	handler: src/myFirstApi/index.handler        
        events:            
           - http:
              path: getFromMyAPI                  
              method: GET
              cors: true
```

Cela déployera votre code de fonction à `${random-api-subdomain}.execute-api.${region}.amazonaws.com/${stage}/getFromMyApi`. Voici un exemple d'un endpoint.

[https://ic5hwq6j0a.execute-api.eu-west-1.amazonaws.com/live/item](https://ic5hwq6j0a.execute-api.eu-west-1.amazonaws.com/live/item)

Si vous souhaitez créer une adresse d'API plus lisible, vous pouvez utiliser Route 53 pour rediriger le trafic afin que votre endpoint puisse être quelque chose comme :

https://api.completecoding.io/v1/item (non actif)

### 2. Bases de données et APIs connectées

Maintenant que vous avez migré certaines de vos APIs, vous êtes familier avec l'écriture de fonctions Lambda et leur déploiement avec Serverless.

L'étape suivante consiste à migrer vos bases de données vers le serverless et à créer le reste de vos APIs.

#### 2.1 Bases de données

Les bases de données sont évidemment une partie massive de tout produit logiciel, mais leur création, gestion et mise à l'échelle peuvent être fastidieuses. La provision de shards et la synchronisation des instances peuvent être difficiles même dans les meilleures conditions.

Avec le Serverless, vous pouvez utiliser DynamoDB, où la mise à l'échelle et les performances sont gérées par AWS, vous laissant travailler sur les parties précieuses du produit.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/mongoToDynamo.png)

**Comment migrer**

La création de tables DynamoDB dans serverless est relativement simple. Tout ce que nous devons faire est de créer une nouvelle ressource et de fournir les détails de la table.

```yml
Resources:  
    OrderTable:
    	Type: AWS::DynamoDB::Table
        Properties:
        	TableName: order-table
            AttributeDefinitions:
            	- AttributeName: userID
                  AttributeType: S
                - AttributeName: orderId
                  AttributeType: S
            KeySchema:
            	- AttributeName: userId
                  KeyType: HASH
                - AttributeName: orderId
                  KeyType: HASH      
```

Les choses peuvent devenir un peu plus complexes lorsqu'il s'agit de l'auto-scaling et des index secondaires.

Pour ajouter l'auto-scaling à notre table, nous avons deux options. Nous pouvons soit configurer la facturation PayPerRequest, soit provisionner l'auto-scaling sur la table.

PayPerRequest est meilleur si vous avez un trafic plus irrégulier qui arrive par pics et creux. Pour le provisionner, vous pouvez supprimer ces lignes :

```
ProvisionedThroughput:
    ReadCapacityUnits: 5
    WriteCapacityUnits: 5
```

et les remplacer par cette ligne :

```
BillingMode: PAY_PER_REQUEST
```

L'autre option est d'ajouter l'auto-scaling. Cela n'était pas une fonctionnalité lorsque Dynamo a été lancé pour la première fois, donc la configuration est plus complexe. Pour réduire la complexité, nous pouvons utiliser le plugin `serverless-dynamodb-autoscaling`. Pour installer ce plugin, exécutez `npm install serverless-dynamodb-autoscaling` et ajoutez ensuite quelques champs personnalisés à notre fichier serverless.yml.

```yml
plugins:  
    - serverless-dynamodb-autoscaling
custom:  
    capacities:    
        - table: order-table  # Ressource DynamoDB      
          read:
              minimum: 5        # Capacité de lecture minimale
              maximum: 1000     # Capacité de lecture maximale        
              usage: 0.75       # Pourcentage d'utilisation ciblé      
          write:        
              minimum: 40       # Capacité d'écriture minimale
              maximum: 200      # Capacité d'écriture maximale	
              usage: 0.5        # Pourcentage d'utilisation ciblé
```

Vous devriez utiliser la méthode la plus applicable à la manière dont chacune de vos tables est utilisée. Il n'y a aucune raison pour que certaines tables ne soient pas en PayPerRequest et d'autres utilisant l'auto-scaling normal.

Il y a aussi la question de migrer toutes vos données de vos tables existantes vers vos nouvelles tables Dynamo. Heureusement, il y a un [article brillant](https://aws.amazon.com/dynamodb/migrations/) sur la façon de réaliser ces types de migrations, que ce soit depuis MongoDB, Cassandra, mySQL ou RDBMS.

#### 2.2 APIs connectées

Maintenant que nous avons créé nos bases de données, nous devrions être en mesure de convertir la plupart de nos APIs restantes en serverless. Cela pourrait être des recherches d'utilisateurs, des connexions, des recherches de produits, des mises à jour de statut de commande ou tout autre type de requête qui lit ou écrit dans l'une de vos tables.

**Comment migrer**

Le processus pour créer ces fonctions sera exactement le même que celui que vous avez fait dans l'étape 1, mais maintenant nous avons des bases de données auxquelles accéder.

Pour accéder à vos données dans DynamoDB, vous pouvez utiliser le SDK AWS et le client de document DynamoDB. Cette interface a la fonctionnalité pour effectuer toutes les méthodes REST ainsi que quelques méthodes supplémentaires telles que _scan, query, batchGet_ et _batchWrite_.

Bien que cela semble parfait pour intégrer dans votre code Lambda, je suggérerais de créer votre propre classe qui utilise ces méthodes. Cela est dû au fait que le format de la requête faite au client de document est souvent excessivement compliqué. Voici mon exemple de méthode simplifiée pour obtenir des données depuis Dynamo.

```js
get(ID, table) {
    if (!table)
        throw 'table nécessaire';
    if (typeof ID !== 'string')
        throw `ID n'était pas une chaîne et était ${ID} sur la table ${table}`;
    return new Promise((resolve, reject) => {
        let params = {
            TableName: table,
            Key: {
                ID: ID,
            },
        };
        documentClient.get(params, function (err, data) {
            if (err) {
                console.log(`Il y a eu une erreur lors de la récupération des données pour l'ID ${ID} sur la table ${table}`, err);
                return reject(err);
            }
            return resolve(data.Item);
        });
    });
}
```

Si vous devez maintenant effectuer une recherche dans l'une de vos APIs, vous pouvez simplement utiliser

```js
let user = await DB.get('123-f342-3ca', 'user-table')
```

Vous pouvez faire de même pour write, update, delete, scan et query.

Avec ces méthodes, vous devriez être en mesure de porter presque toutes vos APIs vers le serverless. Cela peut être un travail important, mais il y a beaucoup d'avantages, notamment l'auto-scaling, le paiement à l'usage, la redondance, la séparation des préoccupations et bien plus encore.

### 3. Stockage

Le stockage cloud était le premier service jamais fourni par AWS - Amazon S3. Ce service vous permet d'héberger des fichiers dans le cloud, de définir les politiques d'accès et d'utiliser facilement ces fichiers dans d'autres services AWS.

Les éléments stockés dans S3 sont placés dans des buckets, qui sont des conteneurs isolés utilisés pour regrouper des éléments (similaires aux dossiers sur votre machine). Vous pouvez stocker les fichiers que vous souhaitez dans S3, des images de produits aux factures, des données au format JSON à des sites web entiers.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/amazon-s3_preview.png)

**Comment migrer**

Il y a deux étapes pour migrer vers le stockage cloud serverless : créer les buckets et déployer les ressources.

Pour créer un bucket dans serverless, vous définissez une nouvelle ressource. Une chose à retenir est que le nom du bucket doit être globalement unique. Cela signifie que vous ne pouvez pas avoir le même nom de bucket sur deux comptes ou dans deux régions.

```
resources:
  Resources:
    UploadBucket:
      Type: AWS::S3::Bucket
      Properties:
        BucketName: my-bucket-name-is-unique
```

Lorsque vous exécutez `sls deploy` maintenant, vous constaterez que vous avez créé un bucket sur votre compte. Vous pouvez maintenant télécharger manuellement des fichiers dans ce bucket en utilisant l'interface utilisateur, ou l'utiliser comme emplacement pour mettre les fichiers téléchargés, mais nous allons également apprendre à synchroniser les fichiers locaux avec le bucket.

Pour télécharger automatiquement des fichiers vers notre nouveau bucket, nous allons utiliser le plugin `serverless-s3-sync`. Ce plugin nous permet de télécharger tout le contenu d'un dossier sur notre ordinateur vers un bucket S3 dans le cadre du processus de déploiement.

Pour commencer à utiliser le plugin, nous devons l'installer en utilisant `npm install --save serverless-s3-sync` et ensuite ajouter le plugin à notre fichier serverless. Avec notre plugin DynamoDB autoscaling, nous aurons maintenant ceci :

```yml
plugins:  
    - serverless-dynamodb-autoscaling
    - serverless-s3-sync
```

Pour configurer le téléchargement, nous devons ajouter un autre champ à notre section `custom`.

```yml
custom:
  s3Sync:
    - bucketName: my-bucket-name-is-unique # requis 
      bucketPrefix: assets/ # optionnel 
      localDir: dist/assets # requis 
```

Le `bucketName` doit correspondre au nom du bucket que vous avez créé. Le `localDir` est le dossier que vous souhaitez télécharger vers le bucket. Vous pouvez également utiliser `bucketPrefix` si vous souhaitez ajouter un préfixe au début des fichiers (les mettre dans un dossier au sein du bucket).

Avec tout cela configuré, l'exécution de `sls deploy` créera maintenant un nouveau bucket et téléchargera les fichiers que vous avez dans `dist/assets`.

### 4. Hébergement de site web

Jusqu'à présent, vous avez dû apporter plusieurs modifications d'URL à votre site web pour toutes les modifications d'API que vous avez déjà implémentées. Maintenant, ne serait-il pas génial si vous pouviez également héberger ce site web entièrement sans serveur et le déployer avec toutes vos APIs, bases de données et tout le reste.

**Comment migrer**

Nous allons héberger et déployer notre site web de manière très similaire à la façon dont nous hébergeons notre stockage d'actifs dans la dernière section : serverless-s3-sync.

Il y a quelques éléments supplémentaires dont nous devons nous occuper lorsque nous hébergeons un site web. Pour commencer, nous téléchargeons toujours un dossier (contenant notre site statique) vers un bucket S3. Nous pouvons ajouter un nouveau bucket (MyWebsiteBucket) et une nouvelle configuration S3Sync. Nous définissons une variable personnalisée appelée `siteName` et l'utilisons ensuite pour définir le nom du bucket.

```
resources:
  Resources:
    UploadBucket:
      Type: AWS::S3::Bucket
      Properties:
        BucketName: my-bucket-name-is-unique
    MyWebsiteBucket:
      Type: AWS::S3::Bucket
      Properties:
        BucketName: ${self:custom.siteName} 
```

```yml
custom:
  s3Sync:
    - bucketName: my-bucket-name-is-unique 
      bucketPrefix: assets/
      localDir: dist/assets
    - bucketName: ${self:custom.siteName}  
      localDir: myWebsiteFolder
  siteName: serverlessfullstack.com
```

Mais cette fois, nous devons ajouter quelques éléments supplémentaires à notre configuration de bucket S3. Nous devons définir le contrôle d'accès et indiquer à S3 qu'il s'agit d'un site web que nous hébergeons dans le bucket.

```
    MyWebsiteBucket:
      Type: AWS::S3::Bucket
      Properties:
        BucketName: ${self:custom.siteName}
        WebsiteConfiguration:
          IndexDocument: index.html
        AccessControl: PublicRead
```

Nous devons également créer un document de politique pour le bucket dans nos ressources

```yml
   WebsiteS3BucketPolicy:
      Type: AWS::S3::BucketPolicy
      Properties:
        Bucket:
          Ref: MyWebsiteBucket
        PolicyDocument:
          Statement:
            - Sid: PublicReadGetObject
              Effect: Allow
              Principal: "*"
              Action:
              - s3:GetObject
              Resource:
              	Fn::Join: ["", [
                  "arn:aws:s3:::",
                  {"Ref": "StaticSite"},
                  "/*"
                ]]

```

Lorsque nous exécutons maintenant `sls deploy`, nous obtiendrons le contenu de notre site web téléchargé vers S3 et toutes les permissions correctes définies sur le bucket.

Vous pourrez maintenant visualiser votre site à l'adresse suivante : [`http://serverlessfullstack.com.s3-website-us-east-1.amazonaws.com/`](http://serverlessfullstack.com.s3-website-us-east-1.amazonaws.com/)

C'est bien, mais ce serait mieux si nous hébergions sur notre propre URL, c'est donc ce que nous allons faire maintenant. Nous devons créer un enregistrement DNS qui pointe le domaine demandé vers notre bucket S3.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/s3Via53-1.png)

Dans Route 53, assurez-vous d'avoir configuré votre nom de zone hébergée, puis nous pouvons ajouter l'enregistrement DNS aux ressources.

```
    DnsRecord:
        Type: 'AWS::Route53::RecordSet'
        Properties:
            AliasTarget:
                DNSName: ${self:custom.aliasDNSName}
                HostedZoneId: ${self:custom.aliasHostedZoneId}
            HostedZoneName: ${self:custom.siteName}.
            Name:
                Ref: MyWebsiteBucket
            Type: 'A'
```

Avec cela, nous devons également définir quelques champs personnalisés supplémentaires : `hostedZoneName`, `aliasHostedZoneId` et `aliasDNSName`.

```
custom:
    s3Sync:
        - bucketName: ${self:custom.siteName}
          localDir: myWebsiteFolder
    siteName: serverlessfullstack.com
    hostedZoneName: ${self:custom.siteName}
    aliasHostedZoneId: Z3AQBSTGFYJSTF # us-east-1
    aliasDNSName: s3-website-us-east-1.amazonaws.com
```

Si vous avez configuré cela dans une région qui n'est pas `us-east-1`, vous pouvez trouver votre `aliasHostedZoneId` [ici](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region).

Avec tout cela configuré, vous devriez maintenant pouvoir exécuter `sls deploy` à nouveau. Cela ajoutera l'enregistrement DNS à votre compte et vous pourrez maintenant visiter serverlessfullstack.com et voir la page live hébergée depuis S3.

Si vous avez suivi, les seules différences entre notre code devraient être : `custom.siteName` et le nom de votre bucket d'actifs, et vous devriez avoir votre propre application hébergée sans serveur !

---

Si vous avez trouvé cet article utile et souhaitez commencer à travailler avec le Serverless, consultez mon [COURS GRATUIT](https://courses.completecoding.io/p/build-a-serverless-api/) sur la création et le déploiement d'une API Serverless. Vous apprendrez à :

* Créer un utilisateur et obtenir des identifiants sur AWS et configurer Serverless
* Créer une Lambda et un endpoint d'API pour gérer les requêtes API
* Déployer, tester et mettre à jour votre API

![Image](https://www.freecodecamp.org/news/content/images/2024/04/build-your-own-serverless-app.png)