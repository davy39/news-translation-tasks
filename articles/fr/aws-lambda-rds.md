---
title: Comment se connecter à AWS RDS depuis AWS Lambda
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-11-09T23:22:38.000Z'
originalURL: https://freecodecamp.org/news/aws-lambda-rds
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/AWS-Lambda-RDS-Proxy-1.png
tags:
- name: AWS
  slug: aws
- name: aws lambda
  slug: aws-lambda
- name: database
  slug: database
seo_title: Comment se connecter à AWS RDS depuis AWS Lambda
seo_desc: "By Mugilan Ragupathi\nIn this article, we're going to learn about how to\
  \ communicate with AWS RDS from AWS Lambda. \nIn this tutorial, we'll be using AWS\
  \ CDK. It's an open source software development framework that lets you define cloud\
  \ infrastructure...."
---

Par Mugilan Ragupathi

Dans cet article, nous allons apprendre comment communiquer avec AWS RDS depuis AWS Lambda. 

Dans ce tutoriel, nous allons utiliser `AWS CDK`. C'est un framework de développement logiciel open source qui vous permet de définir l'infrastructure cloud. 

`AWS CDK` supporte de nombreux langages, y compris TypeScript, Python, C#, Java et d'autres. Nous allons utiliser TypeScript dans ce tutoriel. 

Lors du déploiement (en utilisant la commande `cdk deploy`), votre code est converti en modèles Cloudformation, et toutes les ressources AWS correspondantes sont créées. Seules des connaissances de base en CDK et TypeScript sont requises pour essayer ce tutoriel. Bien sûr, vous devez avoir un compte AWS pour créer des ressources AWS.

Vous pouvez en apprendre davantage sur AWS CDK à partir de la documentation [ici](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html), et j'ai écrit un guide pour débutants à ce sujet sur mon blog [ici](https://www.cloudtechsimplified.com/the-beginners-guide-to-aws-cdk/).

## Introduction à AWS Lambda et RDS

AWS Lambda est un service de calcul sans serveur, piloté par événements, qui vous permet d'exécuter votre code sans avoir à provisionner de serveurs.

AWS RDS est un service de base de données relationnelle gérée par AWS et supporte divers SGBDR tels que MySQL, Postgres, Oracle, SQL Server et bien d'autres. AWS s'occupe de la configuration, de la mise à jour et de la maintenance de ces serveurs de bases de données.

### Pourquoi utiliser RDS avec Lambda ?

AWS Lambda est simplement un service de calcul et il n'a aucune recommandation concernant les magasins de données. En fait, certaines de vos fonctions lambda n'interagiront même pas avec des magasins de données de quelque nature que ce soit. Même si vous souhaitez utiliser un magasin de données, vous pourriez utiliser n'importe quel type de base de données en fonction de vos besoins.

Cependant, la plupart des architectures sans serveur utilisent DynamoDB comme magasin de données pour réduire les coûts et éliminer le besoin de maintenir des serveurs de bases de données.   
  
DynamoDB est excellent et a ses cas d'utilisation. Mais utiliser DynamoDB pour tous les projets impliquant lambda n'est pas possible pour les raisons suivantes :

**Modèles d'accès dynamiques :** Si vous utilisez DynamoDB, vous devrez concevoir vos modèles de requête à l'avance. Ce n'est pas toujours possible, car votre produit (et ses exigences associées) peut évoluer en fonction des retours des clients. 

**Modèles d'accès limités :** DynamoDB ne fournit pas de flexibilité dans l'écriture de vos requêtes. Vous ne pouvez pas effectuer de fonctionnalité `group by` comme vous le faites dans les SGBDR. Vous devez exporter les données et avoir un autre système pour fournir cette fonctionnalité.

**Base de données existante :** Si vous avez une base de données SGBDR existante, vous ne voudrez pas migrer vers DynamoDB à moins qu'il n'y ait une raison impérieuse de le faire. Même si vous souhaitez utiliser DynamoDB, vous devrez peut-être réécrire toute votre couche d'accès aux données pour utiliser DynamoDB au lieu d'un SGBDR régulier. 

### Avantages de l'utilisation des SGBDR :

**Relation entre les entités :** Les SGBDR permettent des relations entre les entités. Vous pouvez définir des clés étrangères pour restreindre toute donnée invalide d'être stockée dans la base de données.

**Modèles d'accès :** Les SGBDR vous permettent d'utiliser des modèles d'accès dynamiques. Une nouvelle entité peut être introduite sans beaucoup de changement dans les modèles existants. Et il dispose de nombreuses fonctionnalités telles que `group by` – de sorte que vous n'avez pas besoin d'avoir un système externe pour effectuer de telles fonctionnalités.

**Familiarité avec SQL :** La plupart des développeurs sont familiers avec SQL pour interroger les bases de données, et vous avez un large éventail de bases de données parmi lesquelles choisir, y compris Oracle, Postgres et MySQL.

Vous pourriez choisir les SGBDR si vous avez les exigences suivantes :

* Vous avez une base de données SGBDR existante et vous souhaitez adopter le calcul sans serveur fourni par AWS Lambda
* Vous avez des modèles d'accès dynamiques et vous ne souhaitez pas changer beaucoup de vos modèles existants

Cela étant dit, discutons de la manière dont nous allons nous connecter à RDS depuis Lambda.

## Architecture du projet

Dans presque tous les cas, votre base de données SGBDR sera dans un sous-réseau privé du Virtual Private Cloud (VPC) afin que personne en dehors du VPC ne puisse y accéder. Comme votre fonction lambda contiendra la logique métier, cette lambda pourrait également être dans un sous-réseau privé.  
  
Nous allons utiliser Postgres comme base de données dans ce tutoriel. Mais le processus ici est applicable pour toute base de données (MySQL, Oracle, MS SQL et ainsi de suite) que vous souhaitez utiliser. L'architecture restera la même.

Voici l'architecture de ce projet :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/AWS-Lambda-RDS-Latest.png)

Nous allons utiliser `AWS CDK` comme outil d'Infrastructure as Code (IaC) pour créer les ressources AWS

### Comment créer un Virtual Private Cloud pour héberger notre Lambda et SGBDR

Nous allons créer 2 sous-réseaux – un sous-réseau privé et un sous-réseau public. Dans le sous-réseau privé, nous aurons notre base de données Postgres.

```typescript
const vpc = new ec2.Vpc(this, 'VpcLambda', {
      maxAzs: 2,
      subnetConfiguration: [
        {
          cidrMask: 24,
          name: 'privatelambda',
          subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS,
        },
        {
          cidrMask: 24,
          name: 'public',
          subnetType: ec2.SubnetType.PUBLIC,
        },
      ],
    });
```

Lorsque vous créez un sous-réseau de type `PRIVATE_WITH_EGRESS` dans AWS CDK, il créera également une passerelle NAT et placera cette passerelle NAT dans le sous-réseau public. 

Le but de la passerelle NAT est de permettre uniquement les connexions sortantes de votre sous-réseau privé vers Internet. Personne ne peut initier des connexions à votre sous-réseau privé depuis Internet public.

### Pourquoi utilisons-nous une passerelle NAT pour la connectivité Internet ?

Vous vous demandez peut-être pourquoi vous avez besoin d'une connexion Internet, car nous avons à la fois lambda et la base de données RDS dans le même sous-réseau privé.

`Secrets Manager` est un service d'AWS pour stocker et gérer des secrets tels que les mots de passe de base de données, les certificats, etc. Le mot de passe pour se connecter à la base de données est stocké dans `secrets manager` qui est accessible par un point de terminaison public.   
  
Soit vous pouvez utiliser `NAT Gateway` pour accéder au point de terminaison public du service `secrets manager`, soit vous pouvez créer un point de terminaison d'interface pour vous connecter à `secrets manager` en utilisant le réseau AWS sans passer par Internet public.

Les deux coûteront de l'argent, mais la passerelle NAT peut être réutilisée pour établir des connexions Internet depuis la lambda également (par exemple, si vous appelez une API externe publique), alors que dans un point de terminaison d'interface, vous ne pourriez pas faire cela.

### Comment créer une instance de base de données RDS pour stocker nos données :

Nous allons utiliser un type d'instance `small` pour la base de données – juste pour les besoins de ce tutoriel. Mais dans les environnements de production, vous utiliserez probablement des instances de plus grande taille. 

Nous créons un nouveau groupe de sécurité pour la base de données afin que nous puissions contrôler qui peut accéder à l'instance de la base de données et par quel port.

```typescript
const dbSecurityGroup = new ec2.SecurityGroup(this, 'DbSecurityGroup', {
      vpc,
    });

    const databaseName = 'cloudtechsimplified';

    const dbInstance = new rds.DatabaseInstance(this, 'Instance', {
      engine: rds.DatabaseInstanceEngine.postgres({
        version: rds.PostgresEngineVersion.VER_13,
      }),
      // optionnel, par défaut m5.large
      instanceType: ec2.InstanceType.of(
        ec2.InstanceClass.BURSTABLE3,
        ec2.InstanceSize.SMALL
      ),
      vpc,
      vpcSubnets: vpc.selectSubnets({
        subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS,
      }),
      databaseName,
      securityGroups: [dbSecurityGroup],
      credentials: rds.Credentials.fromGeneratedSecret('postgres'),
      maxAllocatedStorage: 200,
    });
```

Le code `CDK` ci-dessus créera une instance de base de données et la placera dans le sous-réseau privé (selon la sélection de sous-réseau que nous avons faite).  
  
La méthode `fromGeneratedSecret` créera le secret dans le service de gestion des secrets avec le nom d'utilisateur passé en paramètre. Nous voulons que le nom d'utilisateur de la base de données soit `postgres`, donc nous passons cette valeur.  
  
Et enfin, nous allouons 200 Go d'espace de stockage pour la base de données.

### Comment configurer les propriétés de la fonction Lambda

Nous utilisons Node16 pour écrire notre fonction lambda, et voici les propriétés génériques pour la lambda. 

Nous voulons que le délai d'attente soit de 3 minutes au lieu des 3 secondes par défaut, et nous voulons allouer 256 Mo pour la fonction lambda. 

Comme `aws-sdk` est fourni par le runtime lambda lui-même, nous voulons exclure la bibliothèque `aws-sdk` lors de la création du bundle de la lambda. 

Nous avons installé le package npm `pg` pour communiquer avec la base de données Postgres et nous excluons le package `pg-native` car nous n'en avons pas besoin.

```typescript
 const nodeJsFunctionProps: NodejsFunctionProps = {
      bundling: {
        externalModules: [
          'aws-sdk', // Utilisez le 'aws-sdk' disponible dans le runtime Lambda
          'pg-native',
        ],
      },
      runtime: Runtime.NODEJS_16_X,
      timeout: Duration.minutes(3), // Par défaut 3 secondes
      memorySize: 256,
    };
```

Ensuite, nous allons créer un groupe de sécurité pour la fonction lambda. Notre fonction lambda doit avoir des informations sur le point de terminaison, le nom d'utilisateur et le mot de passe de la base de données afin que lambda puisse se connecter à la base de données. 

Nous allons passer ces valeurs comme variables d'environnement à la fonction lambda.

```typescript
 const lambdaSG = new ec2.SecurityGroup(this, 'LambdaSG', {
      vpc,
    });

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
      securityGroups: [lambdaSG],
    });
```

**Note importante :** Nous ne passons pas le mot de passe de la base de données comme variable d'environnement à la lambda. Au lieu de cela, nous passons l'`ARN` (Amazon Resource Name) à la lambda et nous récupérerons le mot de passe réel (dynamiquement au moment de l'exécution) depuis le gestionnaire de secrets dans la lambda pour une meilleure sécurité.

### Autorisations pour Lambda pour accéder au mot de passe de la base de données

Même si nous passons l'`arn secret` à lambda comme variable d'environnement, lambda doit avoir les autorisations nécessaires pour récupérer le secret (mot de passe de la base de données, dans notre cas) depuis le service `secrets manager`. 

La ligne de code suivante fournit ces autorisations :

```typescript
dbInstance.secret?.grantRead(rdsLambdaFn);
```

La ligne `cdk` ci-dessus créera un rôle pour la lambda avec 2 autorisations `DescribeSecret` et `GetSecretValue` du gestionnaire de secrets afin que notre lambda ait les autorisations pour obtenir la valeur secrète (mot de passe de la base de données, dans notre cas) avant de parler à la base de données.  
  
Vous pouvez voir la même chose dans la console AWS dans le service Lambda.

![Autorisations AWS Lambda pour Secrets Manager](https://www.freecodecamp.org/news/content/images/2022/11/image-23.png)
_Autorisations AWS Lambda pour Secrets Manager_

### Groupe de sécurité pour l'instance de base de données RDS

Nous ne voulons pas permettre la connexion à la base de données ouverte à tous et nous voulons que les connexions à la base de données soient autorisées depuis lambda. 

Le code `cdk` ci-dessous ajoute une règle d'entrée pour permettre la connectivité de notre fonction lambda à l'instance RDS via le port `5432` (port pour la base de données Postgres) :

```typescript
  dbSecurityGroup.addIngressRule(
      lambdaSG,
      ec2.Port.tcp(5432),
      'Lambda vers la base de données Postgres'
    );
```

### Code de la fonction Lambda pour communiquer avec la base de données

Le code réel de la fonction lambda où elle communique avec la base de données est assez simple. Comme nous utilisons une base de données Postgres, nous utilisons le package `pg` pour communiquer avec Postgres depuis l'environnement `nodejs`.  
  
Avant d'initier la connexion à la base de données, nous récupérons la chaîne secrète depuis le service `secrets manager`. Cette chaîne secrète est une chaîne JSON qui contient à la fois le nom d'utilisateur et le mot de passe. Il suffit de parser la chaîne JSON et de prendre uniquement le mot de passe.

```
import * as AWS from 'aws-sdk';
import { Client } from 'pg';

export const handler = async (event: any, context: any): Promise<any> => {
  try {
    const host = process.env.DB_ENDPOINT_ADDRESS || '';
    console.log(`host:${host}`);
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

    if (!secretString) {
      throw new Error('secret string is empty');
    }

    const { password } = JSON.parse(secretString);

    const client = new Client({
      user: 'postgres',
      host,
      database,
      password,
      port: 5432,
    });
    await client.connect();
    const res = await client.query('SELECT $1::text as message', [
      'Hello world!',
    ]);
    console.log(res.rows[0].message); // Hello world!
    await client.end();
  } catch (err) {
    console.log('error while trying to connect to db');
  }
};

```

Et enfin, nous exécutons une simple requête de sélection dans notre base de données.

### Comment tester le projet

Maintenant, vous pouvez vous connecter à votre console AWS pour tester. Sélectionnez le service `Lambda` et sélectionnez votre fonction lambda – dans notre cas, ce serait `rdsLambdaFn`. 

Vous n'avez pas besoin de vous soucier de la propriété `event` de lambda pour ce tutoriel, car nous ne l'utilisons pas dans notre code de fonction lambda. Cliquez sur le bouton Test, et vous pourrez voir les logs.

![Test de la fonction Lambda](https://www.freecodecamp.org/news/content/images/2022/11/Lambda-perf-without-proxy.png)
_Test de la fonction Lambda_

### Le problème de performance

Lambda est bien adapté pour les fonctions qui ne prennent pas beaucoup de temps. En fait, la limite de délai d'attente maximale d'une fonction lambda est de 15 minutes. 

Comme vous pouvez le voir à partir du code lambda, nous établissons la connexion à la base de données chaque fois que la fonction lambda est invoquée. 

Selon la source de l'événement pour la lambda (file d'attente SQS, par exemple), cela créerait des connexions à un rythme plus élevé et se déconnecterait à la fin de la fonction lambda.  
  
Cela augmente considérablement la charge sur le serveur RDS, ce qui réduit les performances. Alors, comment résoudre ce problème ?

## Comment utiliser RDS Proxy

Au lieu de créer directement des connexions de lambda à la base de données, nous pouvons avoir un RDS Proxy situé entre la lambda et la base de données RDS. 

Le but de RDS proxy est de maintenir un pool de connexions afin que tout consommateur puisse se connecter au proxy et obtenir la connexion à la base de données. Notez que nous ne créons PAS de connexion ici – nous obtenons simplement des connexions qui ont déjà été créées.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/AWS-RDS-Proxy-Logical-1.png)
_Utilisation de RDS Proxy avec Lambda_

Il y a 2 avantages à suivre cette approche :

1. **Charge réduite sur le serveur de base de données :** Comme nous n'avons pas besoin de créer une connexion pour chaque invocation de lambda sur le serveur de base de données, la charge sur le serveur est considérablement réduite.
2. **Amélioration des performances de lambda :** Depuis lambda, nous obtenons simplement une connexion depuis le proxy RDS et nous ne créons pas de nouvelle connexion. Cela améliore les performances de la fonction lambda.

### Modifications nécessaires pour utiliser le RDS Proxy

Nous n'avons pas besoin d'apporter de nombreuses modifications à notre architecture ou à notre code. Nous devons simplement faire quelques choses :

* Créer le proxy RDS et associer le groupe de sécurité de la base de données que nous avons créé précédemment
* Mettre à jour la variable d'environnement du point de terminaison de la lambda afin que la lambda puisse se connecter au proxy RDS au lieu de RDS directement

Vous n'avez pas besoin de modifier votre code lambda.

### Architecture mise à jour

Voici le diagramme d'architecture mis à jour

![RDS Proxy avec Lambda - Architecture](https://www.freecodecamp.org/news/content/images/2022/11/AWS-Lambda-RDS-Proxy.png)
_RDS Proxy avec Lambda - Architecture_

### Comment créer le RDS Proxy

Nous devons créer le RDS Proxy et ajouter l'instance de base de données comme cible du proxy.

```typescript
const dbProxy = new rds.DatabaseProxy(this, 'Proxy', {
      proxyTarget: rds.ProxyTarget.fromInstance(dbInstance),
      secrets: [dbInstance.secret!],
      securityGroups: [dbSecurityGroup],
      vpc,
      requireTLS: false,
      vpcSubnets: vpc.selectSubnets({
        subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS,
      }),
    });
```

Notez que nous passons également le secret de la base de données à ce proxy, car il est responsable de la maintenance des connexions. Nous utilisons le même groupe de sécurité de la base de données que nous avons utilisé pour ouvrir le port 5432.

### Comment mettre à jour le point de terminaison pour Lambda

Nous n'avons pas besoin de modifier le code lambda. Nous devons simplement mettre à jour le point de terminaison qui est passé comme variable d'environnement.

```
 environment: {
        DB_ENDPOINT_ADDRESS: dbProxy.endpoint,
        DB_NAME: databaseName,
        DB_SECRET_ARN: dbInstance.secret?.secretFullArn || '',
      },
```

Il n'y aura aucun changement dans le reste du code.

### Améliorations des performances

Lorsque vous testez la fonction lambda, vous pouvez voir que la lambda se connecte au proxy au lieu de l'instance de la base de données (comme nous imprimons les informations de point de terminaison en tant que `host`). 

Vous devriez également remarquer que les performances sont considérablement améliorées. Auparavant, il fallait environ 500 ms pour se connecter. Maintenant, cela prend environ 50 ms.

![Performance de lambda avec RDS Proxy](https://www.freecodecamp.org/news/content/images/2022/11/image-22.png)
_Performance de lambda avec RDS Proxy_

Notez qu'il peut prendre un temps supplémentaire lorsque vous obtenez la connexion initiale depuis RDS proxy. Et l'obtention de toute connexion supplémentaire sera rapide, comme montré ci-dessus.

## Conclusion

J'espère que ce tutoriel vous a aidé à apprendre comment se connecter à RDS depuis AWS Lambda.

Merci d'avoir lu jusqu'à ce point. J'écris sur [aws lambda](https://www.cloudtechsimplified.com/tag/aws-lambda/), [fargate,](https://www.cloudtechsimplified.com/tag/fargate/) [pipeline ci/cd](https://www.cloudtechsimplified.com/tag/ci-cd-pipeline/) et les technologies sans serveur sur [https://www.cloudtechsimplified.com](https://www.cloudtechsimplified.com). Si vous êtes intéressé, vous pouvez vous abonner [ici](https://www.cloudtechsimplified.com/subscribe/).