---
title: Questions et réponses d'entretien sur AWS Lambda
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-12-07T20:54:49.000Z'
originalURL: https://freecodecamp.org/news/aws-lambda-interview-questions
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/AWS-Lambda-Interview-Questions.png
tags:
- name: aws lambda
  slug: aws-lambda
- name: coding interview
  slug: coding-interview
- name: interview questions
  slug: interview-questions
seo_title: Questions et réponses d'entretien sur AWS Lambda
seo_desc: "By Mugilan Ragupathi\nIn this article, I'll go over some of the most commonly\
  \ asked questions that come up in interviews about AWS Lambda. \nNote that this\
  \ is not an exhaustive list – but you can use this guide as a reference to refresh\
  \ your knowledge ..."
---

Par Mugilan Ragupathi

Dans cet article, je vais passer en revue certaines des questions les plus fréquemment posées lors des entretiens sur AWS Lambda. 

Notez que cette liste n'est pas exhaustive, mais vous pouvez utiliser ce guide comme référence pour rafraîchir vos connaissances et obtenir des conseils pour des études plus approfondies.

La plupart des questions seront basées sur votre expérience ou sur certains scénarios. Les questions sont dans les titres et vous trouverez les notes expliquant la raison derrière ces questions juste en dessous.

## Expliquez votre dernier projet impliquant AWS Lambda

_L'intervieweur veut connaître votre expérience réelle avec AWS Lambda. Ne bluffez pas ici, car l'intervieweur pourrait poser des questions supplémentaires basées sur vos réponses._ 

Vous avez peut-être construit une API serverless, des systèmes impliquant des microservices, la conversion d'images/vidéos, l'analyse de logs, et bien plus encore. Expliquez simplement votre projet en détail et parlez des avantages commerciaux de ce projet afin que l'intervieweur sache que vous voyez le tableau d'ensemble.

## Quels services avez-vous intégrés avec AWS Lambda ?

_Ceci est une extension de la question précédente. Il ne s'agit pas d'une liste exhaustive de toutes les sources d'événements qui peuvent se connecter à AWS Lambda. Parlez uniquement des services que vous avez réellement utilisés._ 

Vous avez peut-être utilisé S3, SNS, SQS, Kinesis, DynamoDB, SES, ou d'autres. Tous les projets ne seront pas complètement serverless. 

Si vous avez utilisé un composant non-serverless avec AWS Lambda, mentionnez-les également. Par exemple, vous avez peut-être utilisé AWS Lambda avec RDS. Si vous avez utilisé une telle configuration, vous pouvez l'expliquer ainsi que votre raisonnement.

## Expliquez le concept de démarrages à froid et à chaud dans AWS Lambda

_Il y a deux raisons pour poser cette question. Ils veulent connaître les environnements d'exécution que vous avez utilisés, et ils veulent savoir si vous connaissez les autres environnements d'exécution qui pourraient causer un démarrage à froid._

Les services Lambda reçoivent une demande pour exécuter une fonction lambda. Le service prépare l'environnement d'exécution en téléchargeant le code de la fonction de gestion et en allouant de la mémoire ainsi que d'autres configurations. 

Même si vous n'êtes pas facturé pour ce temps de préparation de l'« environnement d'exécution », vous devrez faire face au délai d'invocation de votre fonction lambda. Ce délai est appelé un « démarrage à froid ».

Le temps de démarrage à froid est moins significatif pour les environnements d'exécution TypeScript et Python, alors qu'il est un peu plus élevé pour les environnements d'exécution Java ou C#.

Pour améliorer les performances, le service lambda conservera l'environnement d'exécution pendant un certain temps. Lorsque vous recevez la demande pour la même fonction lambda à nouveau pendant cette période, votre gestionnaire peut commencer à s'exécuter immédiatement. Ce type d'invocation est appelé un « _démarrage à chaud_ ».

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-18.png)
_[Source de l'image](https://aws.amazon.com/blogs/compute/operating-lambda-performance-optimization-part-1/)_

## Quelle est la différence entre l'invocation synchrone et asynchrone dans AWS Lambda ?

_Même si cette question semble simple, elle a de nombreuses implications pour votre conception et la gestion des erreurs._ 

Dans l'invocation synchrone, l'appelant attend que l'exécution se termine. Mais dans l'invocation asynchrone, l'appelant place l'événement dans une file d'attente interne qui sera traitée plus tard dans la fonction lambda.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-19.png)
_[Source de l'image](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html)_

Un point important à noter ici est que vous ne pouvez pas dicter le type d'invocation et cela dépend du service que vous utilisez avec AWS Lambda.

Par exemple, si vous construisez des API serverless en utilisant API Gateway, ce sera une invocation synchrone. Mais si vous utilisez S3, ce sera une invocation asynchrone.

## Comment implémentez-vous la gestion des erreurs et la logique de nouvelle tentative dans Lambda ?

_Tout composant dans un système piloté par événements qui peut échouer échouera. L'intervieweur veut donc savoir comment vous avez géré les erreurs et comment vous avez relancé dans vos projets précédents. Voici quelques exemples. Expliquez toujours avec des exemples concrets._

Cela dépend du service que vous utilisez avec AWS Lambda. Discutons-en avec quelques exemples.

Si vous construisez une API serverless, il est préférable de retourner cette erreur au client appelant (qui peut être une application front-end dans ce cas). Ensuite, vous laissez votre logique front-end décider ce qu'il faut afficher à l'utilisateur en fonction du type d'erreur.

Si vous utilisez Lambda avec SQS, il est préférable d'utiliser une file d'attente de lettres mortes (Dead Letter Queue) afin de savoir quels messages n'ont pas pu être traités. Pour cette même raison, de nombreux systèmes qui utilisent SNS peuvent également utiliser SQS.

Dans le code ci-dessous, nous utilisons une file d'attente de lettres mortes. Si un message échoue à être traité après un certain nombre de tentatives (comme spécifié par `maxReceiveCount`), il est envoyé à la file d'attente de lettres mortes. Ce comportement est spécifique à lambda lorsqu'il est utilisé avec des files d'attente.

```typescript
const queue = new sqs.Queue(this, 'AwsLambdaSqsQueue', {
      visibilityTimeout: cdk.Duration.seconds(300),
      receiveMessageWaitTime: cdk.Duration.seconds(20),
      deadLetterQueue: {
        queue: new sqs.Queue(this, 'AwsLambdaDlq'),
        maxReceiveCount: 5,
      },
    });
```

Lorsque lambda est invoqué avec d'autres services, vous pouvez configurer le nombre de nouvelles tentatives avec une valeur maximale de 2. Cela signifie que vous pouvez avoir un maximum de 2 nouvelles tentatives en plus de l'invocation initiale. Par exemple, vous voulez déclencher en fonction du téléchargement d'un objet S3 et votre lambda essaiera au maximum 3 fois.

## Expliquez vos flux de travail pour le développement et le déploiement de fonctions AWS Lambda

_Parlez des frameworks que vous avez utilisés. L'intervieweur peut s'attendre à ce que vous parliez également des tests des fonctions lambda._ 

Vous pouvez expliquer quel(s) framework(s) vous avez utilisé pour développer et déployer des fonctions lambda. Vous pouvez également parler de tout outil IaC (Infrastructure as Code) que vous avez utilisé. 

Voici une liste non exhaustive des frameworks les plus couramment utilisés :

* Serverless
* AWS CDK
* AWS SAM
* CloudFormation
* Pulumi

Si vous avez utilisé Terraform, vous pouvez en parler également.

## Peut-on invoquer Lambda lorsqu'un email est reçu à une adresse email de support particulière ? Si oui, concevez ce système. Si non, expliquez pourquoi.

Oui, vous pouvez. Vous pouvez créer un ensemble de règles de réception et ajouter une règle qui déclenche la fonction lambda.

Vous devez stocker l'email dans S3 et déclencher le lambda après cela afin de conserver une copie de l'email pour toute référence future.

Vous pouvez vous référer à [cet article](https://www.freecodecamp.org/news/how-to-receive-emails-via-your-sites-contact-us-form-with-aws-ses-lambda-api-gateway/) sur la façon de recevoir des emails à partir d'un formulaire de contact.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-20.png)
_[Source de l'image](https://www.freecodecamp.org/news/how-to-receive-emails-via-your-sites-contact-us-form-with-aws-ses-lambda-api-gateway/)_

## Une fonction lambda peut-elle appeler une autre fonction lambda ?

_L'intervieweur veut savoir si vous connaissez cet anti-pattern._

Vous pouvez le faire, mais ce n'est pas recommandé. Si vous voulez concevoir un flux de travail qui implique plusieurs fonctions lambda, vous pouvez utiliser des step functions. 

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-21.png)
_[Source de l'image](https://aws.amazon.com/step-functions/)_

Vous pouvez lire plus sur les step functions [ici](https://aws.amazon.com/step-functions/).

Une autre approche standard consiste à émettre un événement et à déclencher un lambda en fonction de l'événement. Vous pouvez utiliser SQS, SNS ou EventBridge comme intermédiaire pour ces événements.

## Peut-on exécuter des requêtes sur une instance RDS (dans un sous-réseau privé) en utilisant Lambda ?

Oui, vous pouvez exécuter la requête dans RDS en utilisant AWS Lambda. Pour cela, vous pouvez avoir votre lambda dans le même VPC. 

Il peut y avoir des implications de performance si vous utilisez AWS Lambda directement avec RDS en raison du temps de création de la connexion à la base de données. Pour éviter cela, vous pouvez utiliser un RDS Proxy.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-22.png)
_[Source de l'image](https://www.freecodecamp.org/news/aws-lambda-rds/)_

Voici un [guide détaillé étape par étape](https://www.freecodecamp.org/news/aws-lambda-rds/) qui vous montre comment faire cela.

## AWS Lambda offre de nombreux avantages. Quels sont les inconvénients de l'utilisation d'AWS Lambda ?

_L'intervieweur veut connaître votre processus de réflexion. Ne dites pas qu'AWS Lambda résout tous les problèmes :-)_ 

Oui, Lambda offre de nombreux avantages tels que le coût et la scalabilité sans avoir besoin de maintenir les serveurs. Mais ce n'est pas la réponse à tout – comme tout service, il a ses propres problèmes (et vous devriez être capable d'en discuter) :

* Débogage : Si vous utilisez des architectures serverless avec Lambda, vous devrez peut-être vous fier aux logs pour trouver la cause racine du problème. Cela est dû au fait que votre application sera distribuée sur de nombreux services/fonctions lambda. 
* Tests : Vous pouvez simuler les services AWS dans vos tests locaux. Mais il est préférable d'avoir un environnement séparé dans AWS pour tester vos lambdas. Cela rend les tests un peu complexes.
* Tâches en arrière-plan : Lambda a une limite de temps de 15 minutes. Si vous voulez qu'une tâche particulière prenne plus de 15 minutes, vous devrez peut-être passer à Fargate ou une autre solution.
* Coût : Si vous exécutez une application à fort trafic qui traite les requêtes 24/7, l'utilisation de lambda peut être coûteuse. Il est préférable d'utiliser Fargate, EC2 ou d'autres services, si vous avez un trafic élevé constant.

## Comment gérez-vous la concurrency et la scalabilité dans AWS Lambda ?

_Des points bonus si vous parlez des problèmes que vous avez rencontrés dans ces situations._

La concurrency est la capacité à exécuter plusieurs fonctions lambda en même temps. La scalabilité est le processus d'augmentation du nombre de copies de votre fonction lambda pour gérer les requêtes entrantes.

Vous pouvez contrôler la concurrency en définissant la valeur de la « concurrency réservée » afin que seul le nombre mentionné de fonctions lambda soit invoqué.

Voici le diagramme de haut niveau de la manière dont lambda scale en fonction du nombre de messages dans la file d'attente.

![AWS Lambda avec SQS](https://www.freecodecamp.org/news/content/images/2022/12/image-23.png)
_[Source de l'image](https://www.cloudtechsimplified.com/aws-lambda-sqs/)_

Note : Il y a un [comportement étrange](https://www.cloudtechsimplified.com/aws-lambda-sqs/#weird-behavior) si vous essayez de limiter AWS Lambda lorsqu'il est utilisé avec une file d'attente standard SQS. Vous pouvez utiliser une file d'attente FIFO pour résoudre ce problème.

## Comment passez-vous des variables d'environnement à AWS Lambda ?

_L'intervieweur pourrait vouloir savoir comment vous passez des informations sensibles, par exemple._

Il existe différentes manières de passer des variables d'environnement à AWS Lambda, et cela dépend du type de valeur qui est passée.

**Données non sensibles** : Si vous voulez passer des informations non sensibles, vous pouvez passer les valeurs directement aux variables d'environnement de votre fonction lambda. Mais ces valeurs seraient visibles dans la console AWS dans le service Lambda. 

Dans l'exemple de code ci-dessous, nous passons le nom de la table DynamoDB directement comme variable d'environnement, car il ne s'agit pas de données sensibles :

```
   const readDDBLambdaFn = new NodejsFunction(this, 'readDDBLambdaFn', {
      entry: path.join(__dirname, '../src/lambdas', 'read-ddb.ts'),
      ...nodeJsFunctionProps,
      functionName: 'readDDBLambdaFn',
      environment: {
        tableName: table.tableName,
      },
    });
```

**Données sensibles** : Si vous voulez passer des données sensibles telles que des mots de passe et des clés API, vous pouvez utiliser soit un Secret Manager soit un Parameter Store. Mais vous devez vous assurer de fournir les rôles nécessaires à Lambda pour accéder et déchiffrer les secrets des services respectifs.

Dans l'extrait de code ci-dessous, nous ne passons pas le secret réel. Au lieu de cela, nous passons simplement l'ARN (Amazon Resource Name) du secret. 

```typescript
const rdsLambdaFn = new NodejsFunction(this, 'rdsLambdaFn', {
      entry: path.join(__dirname, '../src/lambdas', 'rds-lambda.ts'),
      ...nodeJsFunctionProps,
      functionName: 'rdsLambdaFn',
      environment: {
        DB_ENDPOINT_ADDRESS: dbInstance.dbInstanceEndpointAddress,
        DB_NAME: databaseName,
        DB_SECRET_ARN: dbInstance.secret?.secretFullArn || '',
      },
      vpc,
      vpcSubnets: vpc.selectSubnets({
        subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS,
      }),
    });
```

Ensuite, dans lambda, vous pouvez obtenir le secret réel dynamiquement dans la fonction lambda comme montré ci-dessous :

```typescript
export const handler = async (event: any, context: any): Promise<any> => {
    const host = process.env.DB_ENDPOINT_ADDRESS || '';
    const database = process.env.DB_NAME || '';
    const dbSecretArn = process.env.DB_SECRET_ARN || '';
    const secretManager = new AWS.SecretsManager({
      region: 'us-east-1',
    });
    const secretParams: AWS.SecretsManager.GetSecretValueRequest = {
      SecretId: dbSecretArn,
    };
    const dbSecret = await secretManager.getSecretValue(secretParams).promise();
    const secretString = dbSecret.SecretString || '';

    const { password } = JSON.parse(secretString);

}
```

J'ai écrit un tutoriel détaillé [ici](https://www.cloudtechsimplified.com/environment-variables-secrets-database-password-aws-lambda/) sur le même sujet.

## Supposons que vous avez un exécutable dépendant de Windows, sometool.exe. Vous pouvez le télécharger dans un bucket S3. Pouvez-vous exécuter ce binaire avec certains paramètres en utilisant AWS Lambda ?

_Ceci est plus une question pour s'assurer que vous comprenez l'environnement d'exécution d'AWS Lambda, spécifiquement le système d'exploitation qu'il utilise._

Non, vous ne pourriez pas faire cela car AWS Lambda utilise Linux comme système d'exploitation. Linux ne pourrait pas exécuter un binaire dépendant de Windows.

## Comment réutilisez-vous du code entre les fonctions AWS Lambda ?

Il existe deux façons de réutiliser du code entre plusieurs fonctions AWS Lambda :

* Utilisez des couches Lambda : Vous pouvez stocker votre code ou votre logique dans des couches lambda, que vous pouvez réutiliser entre différentes fonctions lambda. 

Voici un exemple de code de haut niveau pour créer et consommer des couches lambda en utilisant `aws cdk` :

```
    const logicLayer = new lambda.LayerVersion(this, 'logic-layer', {
      compatibleRuntimes: [
        lambda.Runtime.NODEJS_14_X,
        lambda.Runtime.NODEJS_16_X,
      ],
      layerVersionName: 'business-logic-layer',
      code: lambda.Code.fromAsset('src/layers/business-logic'),
      description: 'Couche de logique métier',
    });


    const lambdaWithLayer = new NodejsFunction(this, 'lambdaWithLayer', {
      entry: path.join(__dirname, '../src/lambdas', 'lambda.ts'),
      ...nodeJsFnProps,
      functionName: 'lambdaWithLayer',
      handler: 'handler',
      layers: [logicLayer, utilsLayer],
    });
```

* Utilisez un `monorepo` : Vous pouvez utiliser un monorepo et construire dynamiquement des packages au moment du déploiement.

## Que se passe-t-il avec vos fonctions lambda si vous supprimez une couche Lambda ?

_Dans cette question, l'intervieweur veut voir à quel point vous comprenez les couches lambda._ 

Les fonctions lambda existantes qui utilisent cette couche supprimée continueront à fonctionner, car les couches lambda sont fusionnées avec les fonctions lambda au moment du déploiement. 

Mais vous ne pouvez pas créer une nouvelle fonction lambda en utilisant cette couche lambda supprimée.

Vous pouvez en apprendre plus sur les couches Lambda [ici](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html) et j'ai écrit un guide sur le même sujet [ici](https://www.cloudtechsimplified.com/aws-lambda-layers/).

## Peut-on augmenter la taille d'un package de déploiement si l'on utilise des couches Lambda ?

Non, vous ne pouvez pas augmenter la taille du package de déploiement si vous utilisez des couches Lambda. La taille maximale de déploiement de 50 Mo zippée inclut à la fois la taille de la fonction lambda et ses couches lambda associées.

Si vous avez une base de code volumineuse et que vous souhaitez augmenter le déploiement, vous pouvez exécuter des conteneurs dans AWS Lambda.

## Puis-je prendre mon application web dockerisée existante et l'exécuter en utilisant Lambda ?

Non. Vous ne pouvez pas prendre une application Express, Springboot ou .NET Core (ou toute autre application d'ailleurs) telle quelle et la mettre dans lambda. 

Mais cela dit, il existe quelques bibliothèques qui permettent de mettre des applications utilisant ces frameworks web dans AWS Lambda. En interne, ces bibliothèques convertissent ces applications web en API compatibles avec AWS lambda. Vous pouvez voir un exemple ici [ici](https://aws.amazon.com/blogs/aws/running-express-applications-on-aws-lambda-and-amazon-api-gateway/).

En utilisant ces frameworks, la taille de vos fonctions lambda sera plus grande et entraînera des temps de démarrage plus longs.

Rappelez-vous que même lorsque vous utilisez des conteneurs avec Lambda, l'API d'exécution existante de Lambda reste la même. Lambda sera toujours :

* une seule fonction 
* invoquée par un événement ou manuellement
* avoir un délai d'exécution de 15 minutes.

Comme vous pouvez le voir dans le code ci-dessous, il n'y aura aucun changement dans l'API lambda. L'avantage d'utiliser Docker est que vous pourrez utiliser de grands packages sans vous soucier de la taille.

```typescript
import { Context, APIGatewayProxyResult, APIGatewayEvent } from 'aws-lambda';

export const handler = async (
  event: APIGatewayEvent,
  context: Context
): Promise<APIGatewayProxyResult> => {
  console.log(`Event: ${JSON.stringify(event, null, 2)}`);
  console.log(`Context: ${JSON.stringify(context, null, 2)}`);
  return {
    statusCode: 200,
    body: JSON.stringify({
      message: 'Exécution de ce gestionnaire à partir de docker',
    }),
  };
};
```

Et voici comment vous l'utilisez :

```
 const repo = ecr.Repository.fromRepositoryName(
      this,
      'dockerLambda',
      'docker-lambda'
    );

    const dockerLambda = new lambda.DockerImageFunction(
      this,
      'DockerLambdaFunction',
      {
        code: lambda.DockerImageCode.fromEcr(repo),
      }
    );
```

J'ai écrit un tutoriel étape par étape sur l'exécution de conteneurs Docker pour votre application dans `aws lambda` [ici](https://www.cloudtechsimplified.com/run-docker-containers-images-from-ecr-in-aws-lambda-along-with-cicd/).

## Comment partagez-vous des fichiers volumineux entre les fonctions lambda ?

Vous pouvez utiliser le système de fichiers élastique (EFS) pour partager des fichiers volumineux entre différentes fonctions. 

Vous pouvez créer un `point d'accès` dans l'EFS créé avec les permissions appropriées et utiliser ce `point d'accès` dans votre `chemin de montage` dans votre lambda. 

Tout fichier écrit sur ce chemin de montage sera accessible à toutes les autres fonctions lambda, à condition qu'elles aient le chemin de montage avec les permissions appropriées.

Voici le diagramme logique de haut niveau sur la façon d'utiliser AWS Lambda avec le système de fichiers élastique (EFS) :

![Utilisation d'EFS avec Lambda](https://www.freecodecamp.org/news/content/images/2022/12/image-24.png)
_[Source de l'image](https://www.cloudtechsimplified.com/elastic-file-system-efs-aws-lambda/)_

Vous pouvez lire à ce sujet [ici](https://aws.amazon.com/blogs/compute/using-amazon-efs-for-aws-lambda-in-your-serverless-applications/) (un peu ancien). J'ai écrit un guide pratique plus récent étape par étape [ici](https://www.cloudtechsimplified.com/elastic-file-system-efs-aws-lambda/) sur EFS avec les fonctions Lambda.

## **Conclusion**

J'espère que cet article vous a aidé à vous préparer pour les entretiens impliquant AWS Lambda.

Merci d'avoir lu jusqu'à ce point. J'écris sur `aws` et les technologies serverless à l'adresse [https://www.cloudtechsimplified.com](https://www.cloudtechsimplified.com/). Si vous êtes intéressé, vous pouvez vous [abonner](https://www.cloudtechsimplified.com/) à mon blog.