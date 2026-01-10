---
title: Refactorisation avec une Architecture Orientée Événements sur AWS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2024-01-23T15:03:06.000Z'
originalURL: https://freecodecamp.org/news/deep-dive-into-event-driven-architecture-on-aws
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/eda-title-macguffin.png
tags:
- name: AWS
  slug: aws
- name: youtube
  slug: youtube
seo_title: Refactorisation avec une Architecture Orientée Événements sur AWS
seo_desc: "By Matt Morgan\nEvent-driven architecture is a software design pattern\
  \ where components or services perform actions in response to events, often asynchronously.\
  \  \nThis post serves as a companion to our video course, \"Deep Dive into Event-Driven\
  \ Archit..."
---

Par Matt Morgan

L'architecture orientée événements est un modèle de conception logicielle où les composants ou services effectuent des actions en réponse à des événements, souvent de manière asynchrone. 
  
Cet article sert de complément à notre cours vidéo, "Plongée Approfondie dans l'Architecture Orientée Événements sur AWS". Dans le cours, nous explorons en détail certains des fondamentaux de l'architecture orientée événements sur AWS.

Cet article de blog complète le cours vidéo en examinant de près un exemple pratique : la modernisation de notre application de gestion des stocks d'entrepôt (WIMS). En savoir plus sur Matt Martz et son travail sur [martz.codes](https://martz.codes) et explorer les perspectives de Matt Morgan sur [mattmorgan.cloud](https://mattmorgan.cloud).

Vous pouvez regarder le [cours vidéo complet sur la chaîne YouTube de freeCodeCamp.org](https://youtu.be/Zr6fnhvJKlw) (1,5 heure de visionnage).

%[https://youtu.be/Zr6fnhvJKlw]

## Pourquoi refactoriser ?

La plupart des développeurs comprennent que rien ne vaut la rapidité de mise sur le marché. Nous pouvons tous penser à des applications qui ont trouvé le succès en dépit, et non grâce à, leurs architectures système. Une fois que le système prend de l'ampleur et attire des utilisateurs, les imperfections peuvent vraiment se démarquer, et c'est alors le moment de refactoriser. Parfois, le système est replatformé vers quelque chose de plus scalable et performant. Parfois, il est reconstruit à partir de zéro. Cet article de blog démontrera comment adopter l'architecture orientée événements, les problèmes qu'elle peut résoudre, et certains des excellents outils qu'AWS propose dans ce domaine. Commençons !

## WIMS v1

Notre application métier fictive gère un entrepôt rempli de MacGuffins. Nous allons nous concentrer sur une partie du système qui gère la réception des commandes. Elle peut être représentée par ce diagramme d'architecture :

![Image](https://lh7-us.googleusercontent.com/yUWou0B9NJZsrVu8-Ra0EPHnAvalZjatdHvV2zdnwfFFHpf9j1o2yBpFaeq_K3qEIXHahfMRoMnuNKfeUQyUtRPVw9hwWf_o3IXAGmYGkcyiWYUeul4ics3qpn_DISwwdSYMXIJAlSXoPe1pHDAf4Iu5Ig=s2048)
_Diagramme d'architecture de la version 1 de WIMS_

Ce système a été construit avec des technologies serverless d'AWS, mais se concentre principalement sur API Gateway, Lambda et DynamoDB. Ces services sont excellents, mais se limiter à eux apporte également des défis techniques que nous découvrirons bientôt.

Notre flux principal est que nous recevons la commande via notre API Gateway qui déclenche une fonction Lambda pour gérer la création de la commande. La fonction Lambda effectuera trois choses :

1. Enregistrer la commande dans notre base de données.
2. Réduire le niveau de stock actuel du nombre d'unités dans la commande.
3. Notifier de manière RESTful notre API de Paiements pour gérer le paiement.

Une fonction Lambda est certainement capable d'effectuer ces tâches, mais à mesure que notre entreprise se développe, nous découvrons certaines faiblesses dans notre architecture :

### Limitation des paiements

Notre API de Paiements semble malheureusement être limitée pendant les périodes chargées. Parce que notre architecture nécessite que la fonction Lambda CreateOrder se termine avant le délai d'attente de 29 secondes de l'API Gateway, cela ne nous laisse qu'un temps limité pour réessayer les requêtes.

Notre traitement des paiements est déjà asynchrone, donc il n'y a pas de préoccupation si ce traitement est retardé, mais nous n'avons pas un bon moyen de nous auto-limiter et d'éviter de submerger l'API de Paiements avec des requêtes pendant les périodes chargées.

Nous nous en sortons avec un processus manuel pour l'instant, mais nous avons besoin d'une solution technique pour gérer notre entreprise en croissance !

### Notifications de faible stock

Les MacGuffins se vendent comme des petits pains, au point que nous avons manqué quelques opportunités en étant en rupture de stock à quelques reprises et en voyant ensuite un ralentissement de notre activité pendant que nous réapprovisionnons.

Nous voulons ajouter une notification de stock faible qui nous avertira qu'il est temps de réapprovisionner. Nous avons pensé à créer un sujet SNS avec un abonnement par e-mail. Nous pourrions vérifier le stock et déclencher l'événement immédiatement après avoir effectué l'ajustement du stock.

Cela pourrait fonctionner, mais est-ce la meilleure solution ? Notre fonction Lambda effectue maintenant cinq choses au lieu de trois, donc il y a plus de choses qui pourraient mal tourner. Mais pire encore, que se passe-t-il si un autre processus ajuste le stock en dessous du niveau d'avertissement ? Si cette logique n'existe que dans notre fonction Lambda CreateOrder, alors nous n'enverrions jamais la notification.

### Opérations de livraison

Notre processus de livraison est largement manuel, piloté par un tableau de bord qui interroge les commandes en attente. Nous avons un plan pour automatiser davantage, mais comment savons-nous qu'il est temps de lancer le processus de livraison ? Nous devons avoir un moyen d'attendre et de confirmer que le paiement a été effectué avec succès et que nous avons le stock souhaité en main. Pour ce faire, il est clair que nous avons besoin d'un système orienté événements.

## Considérations de conception

La plupart d'entre nous sont conscients des défis associés à la refactorisation. Pour commencer, il y a toujours un compromis entre la refactorisation et la construction de nouvelles fonctionnalités. Nous pouvons soutenir que la refactorisation est nécessaire pour supporter de nouvelles fonctionnalités, mais le fait est que nous allons faire un travail qui est invisible pour les clients et les parties prenantes. Afin d'avoir une chance de succès et de répondre aux attentes, nous devons être clairs sur nos considérations de conception et les résultats souhaités de la refactorisation.

### Scalabilité et cohérence éventuelle

WIMS v1 fonctionne bien dans notre environnement de test et sous une charge légère, mais il se dégrade sous des charges lourdes. Nous savons que cela est dû au fait que nous essayons de faire trop de travail dans une requête orientée client. Pour résoudre ce problème, nous voulons concevoir WIMS v2 pour simplement enregistrer l'intention du client : "Nous avons reçu votre commande !" Notre système traitera cette intention de manière éventuellement cohérente et notifiera le client par e-mail s'il y a un problème avec le paiement ou si un article est en rupture de stock.

La cohérence éventuelle fait partie de l'histoire de la scalabilité. Nous devons nous demander "Que se passe-t-il si nous avons une journée 10x ou 100x ?" Construire avec du serverless est un bon début, mais la version v1 de notre système était déjà serverless et avait pourtant des problèmes de scalabilité. En rendant notre système éventuellement cohérent, nous pouvons contrôler le débit de nos événements pour protéger les services en aval. Nous savons que certains événements (comme l'enregistrement de l'intention du client) doivent être immédiatement cohérents. Nous voulons rendre ceux-ci aussi réactifs et légers que possible et délesguer le travail lourd à d'autres services.

### Idempotence, tolérance aux pannes et relecture

Aucun système ne peut espérer être exempt d'erreurs à 100 %. Nous pouvons introduire un bug. Nous pouvons découvrir un cas limite ou atteindre une limite de service. Nos clients feront des choses que nous n'avons pas anticipées ! Les services gérés que nous utilisons peuvent avoir leurs propres bugs et problèmes opérationnels. Pour atténuer ces risques, nous avons besoin d'un système capable de relire les événements et nous avons besoin que le système soit tolérant à la redélivraison des événements ainsi que de gérer le cas où les événements sont livrés dans un ordre différent de celui que nous attendons.

Oui, il est possible d'utiliser des files d'attente [FIFO](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-understanding-logic.html), et les flux DynamoDB [garantissent l'ordre et ne contiendront pas d'événements en double](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/streamsmain.html), mais ces garanties peuvent être trompeuses lorsque d'autres parties du système peuvent utiliser un modèle de livraison [au moins une fois](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-delivery-level). Concevoir pour l'idempotence nous permet non seulement de mitiger le risque que les événements puissent être redélivrés, mais aussi de relire les événements en cas de défaillance du système. Nous pouvons avoir la confiance de relire tous les événements qui auraient dû être envoyés pendant un incident, plutôt que de devoir déterminer exactement quels événements doivent être relus.

### Modularisation

Nous savons par expérience que peu de temps après la livraison de WIMS v2, nous trouverons une nouvelle exigence qui n'a pas été considérée lors de notre conception. Par exemple, nous pourrions constater que nous avons des exigences de notification qui ne peuvent pas être satisfaites avec un abonnement par e-mail SNS. Si notre implémentation de notification réside dans la fonction Lambda CreateOrder, il pourrait être difficile d'ajouter une nouvelle implémentation plus complexe à sa place, mais puisque nous adoptons l'architecture orientée événements, nous pouvons simplement acheminer l'événement ailleurs.

### Observabilité

De nombreux développeurs estiment que les systèmes distribués peuvent être plus difficiles à observer. Cela est définitivement vrai pour les systèmes qui dépendent des plaintes des clients, des métriques du serveur et des codes de statut HTTP pour déterminer l'état du système. Si WIMS v1 répond 200 OK, nous sommes raisonnablement confiants en pensant que tout s'est bien passé. Cela ne sera pas vrai pour WIMS 2. Alors, comment savons-nous que le système a fait ce que nous voulions qu'il fasse ?

Tout d'abord, nous devons déconstruire cette réponse HTTP 200 OK. Un code de statut 200 signifie-t-il que nous avons reçu le paiement et que le client a reçu un MacGuffin ? Non, bien sûr que non. Nous utilisons vraiment ce code de statut comme un proxy pour un résultat métier. 

Une meilleure solution consiste à émettre des événements métiers à la fin (qu'il s'agisse d'un succès ou d'un échec) des opérations critiques. Ces événements peuvent alerter l'équipe sur les choses qui doivent être traitées (comme un faible stock) et peuvent également être utilisés pour suivre des choses comme un paiement réussi, la livraison d'un article et l'état actuel d'une commande.

### Capture des Données Modifiées (CDC)

Lever les événements CDC peut être l'un des meilleurs moyens d'ajouter des événements à un système. Par exemple, nous pourrions attendre qu'un champ de statut change et déclencher un événement basé sur cela. Au lieu d'écrire du code comme :

```typescript
updateStatus('PENDING');
sendEvent('PENDING', order);
```

Nous mettons simplement à jour le statut et laissons notre système CDC gérer le reste. Ce sera un système beaucoup plus fiable et cohérent. Et si nous devions faire une mise à jour de statut en masse pour corriger un bug ? Si nous dépendons d'un code impératif pour envoyer cet événement, il pourrait être manqué dans la mise à jour en masse. L'utilisation de CDC garantira que l'étape suivante de notre système est invoquée.

### Coût

Lors de l'AWS re:Invent 2023, le CTO d'Amazon, Dr. Werner Vogels, a utilisé sa [keynote](https://www.youtube.com/watch?v=UTRBVPvzt9w) pour faire un point intéressant sur l'utilisation du coût comme proxy pour une bonne architecture et a lancé un [site web](https://thefrugalarchitect.com/) en soutien à cette idée. Même si notre entreprise de MacGuffin se développe bien, nous voulons toujours maintenir les coûts opérationnels et nous savons que le gaspillage affectera non seulement notre résultat net, mais aussi l'opérabilité de ce système. Nous allons effectuer quelques projections de coûts pour nous assurer que nous exerçons la frugalité dans notre architecture.

## WIMS version 2

Étant donné nos considérations de conception et ce que nous avons appris sur l'architecture orientée événements, notre nouveau diagramme de système ressemble à ceci. Nous allons tirer parti des événements CDC des flux DynamoDB pour activer les notifications de faible stock et pour gérer le traitement asynchrone des commandes. Nous utiliserons SQS pour mettre en file d'attente les paiements, en utilisant des mécanismes de redélivraison et une file d'attente de lettres mortes pour gérer les exceptions.

![Image](https://lh7-us.googleusercontent.com/y6mBcKye93AWbTihybXMF5RWfsJPaAkMR7sz1C12nAAgARvkp94D56OxpjTXbF7-58KGBPYZnBdV_A3S-7wDos1MIq6ubfRqmTvx14NgIlRklyQ3_BZVdffAH5_9wag_I9uWWJaxD0B6LfAHKypXYWGEeA=s2048)
_Diagramme d'architecture de la version 2 de WIMS_

## Refactorisation CDK

Alors que nous commençons à refactoriser, nous devrions réfléchir à la manière dont nous allons construire notre code. Il est possible d'écrire des applications CDK sous la forme d'un seul fichier "my-stack.ts", mais cela peut entraîner des problèmes de lisibilité. Puisqu'une application CDK est une collection de ressources, la création d'une très grande classe pour toutes vos ressources peut créer des problèmes de maintenabilité. Il est considéré comme une bonne pratique de donner une organisation logique à vos ressources. Si nous pensons aux domaines sur lesquels nous voulons nous concentrer ici, ils incluent :

* Commandes
* Stock
* Paiements

De plus, il y a certaines considérations techniques qui doivent être incluses dans l'application. Ce ne sont pas des domaines métiers, mais ce sont des fonctionnalités importantes qui doivent être incluses dans la nouvelle architecture :

* Capture des Données Modifiées (CDC)
* Observabilité

Parce que les applications CDK utilisent du code impératif, il existe de nombreuses façons différentes d'atteindre cette organisation logique. Un tel outil est le [construct L3 de CDK](https://docs.aws.amazon.com/cdk/v2/guide/constructs.html#constructs_author). Les construct L3 (également appelés "patterns") sont souvent utilisés pour créer, partager et publier de nouveaux constructs, mais ils peuvent également être de simples outils d'organisation au sein d'une application, permettant aux développeurs d'interagir avec une partie de l'application en tant qu'API plutôt qu'en tant que collection de ressources.

Dans cet exemple, nous allons créer plusieurs construct L3 pour organiser notre application :

* CDC (ou Capture des Données Modifiées), pour capturer et router les événements de changement
* InventoryMonitor, pour vérifier les niveaux de stock et envoyer des notifications appropriées
* Observabilité, pour ajouter des journaux supplémentaires et configurer un registre de schémas EventBridge
* OrdersAPI, pour regrouper notre API existante pour les commandes
* OrdersProcessor, pour traiter une commande une fois qu'elle est créée
* PaymentsAPI, représentant notre système de paiement problématique
* PaymentsProcessor, où nous tentons de résoudre notre problème de débit

Notez que bien que nous pensions aux domaines métiers critiques, ces construct L3 n'ont pas une correspondance 1:1 avec nos domaines. Au lieu de cela, nos constructs correspondent aux capacités dont notre application a besoin pour implémenter ces domaines. La conception pilotée par le domaine et la manière dont cela se rapporte à l'architecture orientée événements est un sujet qui dépasse le cadre de cet article de blog.

Nous pouvons créer des construct L3 en créant un nouveau fichier TypeScript avec le nom de notre construct. Nous les mettrons dans un dossier sous ./src/constructs, mais ils pourraient aller n'importe où, car TypeScript peut les importer à partir de n'importe quelle structure de répertoire qui a du sens pour notre équipe. Nous définissons le construct comme une classe qui implémente `Construct`.

```typescript
import { TableV2 } from 'aws-cdk-lib/aws-dynamodb';
import { Construct } from 'constructs';

export interface CDCProps {
  table: TableV2;
}

export class CDC extends Construct {
  constructor(scope: Construct, id: string, props: CDCProps) {
    super(scope, id);

    // create resources
    // Do something with the table prop
  }
}

```

Nous pouvons exposer des ressources et les passer d'un construct à un autre en utilisant la syntaxe de classe TypeScript standard. Pour obtenir une référence à notre construct RestAPI de l'API de Paiements, nous pouvons créer un accesseur appelé `getApi()`.

```typescript
import { Stack } from 'aws-cdk-lib';
import {
  RestApi,
  MockIntegration,
  PassthroughBehavior,
} from 'aws-cdk-lib/aws-apigateway';
import { Construct } from 'constructs';

export class PaymentsApi extends Construct {
  private api: RestApi;
  constructor(scope: Stack, id: string) {
    super(scope, id);

    // Payments is an external system so mocked here.
    this.api = new RestApi(this, 'WIMSPayments', {
      deployOptions: { throttlingBurstLimit: 5, throttlingRateLimit: 5 },
    });
  }

  getApi() {
    return this.api;
  }
}
```

Cela peut ensuite être utilisé pour passer l'API d'un construct L3 à un autre.

```typescript
    const paymentsApi = new PaymentsApi(this, 'PaymentsApi');
    const paymentsProcessor = new PaymentsProcessor(this, 'PaymentsProcessor', {
      api: paymentsApi.getApi(),
    });
```

Vous pouvez trouver l'original [wims-stack.ts](https://github.com/elthrasher/wims/blob/legacy/src/stacks/wims-stack.ts) dans le [dépôt GitHub](https://github.com/elthrasher/wims) du projet sur la branche [legacy](https://github.com/elthrasher/wims/tree/legacy). Il fait juste un peu plus de 100 lignes de code, donc ce n'est pas trop terrible. Cependant, une fois que nous aurons terminé la refactorisation et déplacé toutes nos ressources vers des construct L3, nous réduirons cela de moitié. Notre pile crée maintenant la même table DynamoDB et ajoute ensuite nos nouveaux construct L3.

```typescript
import { CfnOutput, RemovalPolicy, Stack, StackProps } from 'aws-cdk-lib';
import {
  AttributeType,
  StreamViewType,
  TableV2,
} from 'aws-cdk-lib/aws-dynamodb';
import { Construct } from 'constructs';

import { TABLE_PK, TABLE_SK } from '../constants';
import { CDC } from '../constructs/cdc';
import { InventoryMonitor } from '../constructs/inventory-monitor';
import { ObservabilityConstruct } from '../constructs/observability';
import { OrdersApi } from '../constructs/orders-api';
import { OrdersProcessor } from '../constructs/orders-processor';
import { PaymentsApi } from '../constructs/payments-api';
import { PaymentsProcessor } from '../constructs/payments-processor';

export class WimsStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const table = new TableV2(this, 'WIMSTable', {
      dynamoStream: StreamViewType.NEW_AND_OLD_IMAGES,
      partitionKey: { name: TABLE_PK, type: AttributeType.STRING },
      removalPolicy: RemovalPolicy.DESTROY,
      sortKey: { name: TABLE_SK, type: AttributeType.STRING },
      tableName: 'WIMS',
    });

    new CDC(this, 'CDC', { table });
    new InventoryMonitor(this, 'InventoryMonitor');
    new ObservabilityConstruct(this, 'Observability');
    const paymentsApi = new PaymentsApi(this, 'PaymentsApi');
    const paymentsProcessor = new PaymentsProcessor(this, 'PaymentsProcessor', {
      api: paymentsApi.getApi(),
    });
    const ordersApi = new OrdersApi(this, 'OrdersApi', { table });
    new OrdersProcessor(this, 'OrdersProcessor', {
      queue: paymentsProcessor.getQueue(),
      table,
    });

    new CfnOutput(this, 'InventoryUrl', {
      value: ordersApi.getApi().deploymentStage.urlForPath('/inventory'),
    });
    new CfnOutput(this, 'OrdersUrl', {
      value: ordersApi.getApi().deploymentStage.urlForPath('/orders'),
    });
  }
}

```

Maintenant, examinons les capacités de ces construct L3 et comment ils répondront à nos besoins métiers et techniques.

## OrdersApi

Cela existait dans la V1 de notre application, mais avait l'inconvénient de tenter de faire trop de choses. `create-order.ts` aurait peut-être dû s'appeler `create-order-then-update-inventory-and-finally-call-payments-api.ts`. Plutôt que de lui donner un nom plus descriptif, simplifions-le à la capacité principale qui nous intéresse le plus - créer une commande. Ce construct L3 fera cette chose simple et différera le reste à d'autres constructs. Nous pourrions atteindre cet objectif en supprimant du code de notre fonction Lambda.

```typescript
import { DynamoDBClient } from '@aws-sdk/client-dynamodb';
import { DynamoDBDocumentClient, PutCommand } from '@aws-sdk/lib-dynamodb';
import { APIGatewayProxyEvent, APIGatewayProxyResult } from 'aws-lambda';

import { TABLE_PK, TABLE_SK } from '../constants';

const client = DynamoDBDocumentClient.from(new DynamoDBClient({}));

const api = process.env.API_URL;
const table = process.env.TABLE_NAME;

if (!api || !table) {
  throw new Error('Missing required env var!');
}

export const handler = async (
  event: APIGatewayProxyEvent
): Promise<APIGatewayProxyResult> => {
  if (!event.body) {
    throw new Error('Missing event body!');
  }

  const order = JSON.parse(event.body);

  if (!order.customerId || !order.quantity) {
    throw new Error('Invalid order!');
  }

  const timestamp = new Date().getTime();

  // First create the order
  const createOrderCommand = new PutCommand({
    Item: {
      ...order,
      status: 'PENDING',
      timestamp,
      [TABLE_PK]: `CUSTOMER#${order.customerId}`,
      [TABLE_SK]: `TIMESTAMP#${timestamp}`,
    },
    TableName: table,
  });
  await client.send(createOrderCommand);

  return {
    body: 'Order created!',
    statusCode: 200,
  };
};

```

Nous avons supprimé un tas de code et maintenant nous avons une belle fonction Lambda à usage unique ! Mais à ce stade, nous n'avons pas vraiment beaucoup de code ou de logique personnalisée. API Gateway a la capacité de s'intégrer directement avec DynamoDB. Faire cela présente certains avantages :

* Pas de démarrages à froid.
* Pas de fonctions Lambda à maintenir, bundler, déployer, mettre à niveau, ignorer les avertissements de dépréciation, etc.
* Pas de frais Lambda ou d'utilisation de concurrency.
* Nous force à garder cela simple car VTL n'est pas un bon endroit pour une logique complexe.

D'un autre côté, il y a quelques inconvénients à considérer :

* Il peut y avoir une courbe d'apprentissage ou un défi à adopter ce modèle.
* Nous changeons quelque chose qui n'a pas nécessairement besoin d'être changé (notre problème énoncé est que la fonction Lambda essaie de faire trop de choses, pas qu'elle existe).
* À mesure que notre entreprise se développe, la complexité peut être inévitable et nous pouvons devoir revenir à Lambda, donc nous ferions face à plus de retravail.

Tout cela considéré, essayons l'intégration directe. Pour ce faire, nous allons supprimer la fonction Lambda create-orders et remplacer notre `LambdaIntegration` par `AwsIntegration`.

```typescript
    orders.addMethod(
      'POST',
      new AwsIntegration({
        action: 'PutItem',
        options: {
          credentialsRole: role,
          integrationResponses: [
            {
              responseTemplates: {
                'application/json': JSON.stringify({
                  message: 'Order created!',
                }),
              },
              statusCode: '200',
            },
          ],
          requestTemplates: {
            'application/json': JSON.stringify({
              Item: {
                [TABLE_PK]: {
                  S: "CUSTOMER#$input.path('$.customerId')",
                },
                [TABLE_SK]: {
                  S: 'TIMESTAMP#$context.requestTimeEpoch',
                },
                customerId: {
                  S: "$input.path('$.customerId')",
                },
                quantity: {
                  N: "$input.path('$.quantity')",
                },
                status: {
                  S: 'PENDING',
                },
                timestamp: {
                  N: '$context.requestTimeEpoch',
                },
              },
              TableName: table.tableName,
            }),
          },
        },
        service: 'dynamodb',
      }),
      {
        methodResponses: [{ statusCode: '200' }],
      }
    );
```

Parce que notre OrdersApi crée une commande et répond immédiatement au client, c'est un exemple d'événement synchrone. Voir le construct dans notre [dépôt](https://github.com/elthrasher/wims/blob/main/src/constructs/orders-api.ts).

## CDC

Bien qu'il soit possible de mettre en œuvre des modèles CDC sur n'importe quel type de base de données, DynamoDB est un choix de premier plan pour ce modèle en raison de ses capacités de streaming. Le guide du développeur DynamoDB contient même une section sur la [capture des données modifiées](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html).

Pour utiliser les flux DynamoDB pour la CDC, nous devons d'abord activer les flux sur notre table. Cela est très simple à faire en utilisant AWS CDK.

```typescript
    const table = new TableV2(this, 'WIMSTable', {
      dynamoStream: StreamViewType.NEW_AND_OLD_IMAGES,
      partitionKey: { name: TABLE_PK, type: AttributeType.STRING },
      removalPolicy: RemovalPolicy.DESTROY,
      sortKey: { name: TABLE_SK, type: AttributeType.STRING },
      tableName: 'WIMS',
    });
```

L'ajout d'une clé `dynamoStream` avec la valeur `NEW_AND_OLD_IMAGES` nous donnera toutes les informations nécessaires pour commencer à capturer les événements de création, de mise à jour et de suppression et les router vers les gestionnaires appropriés.

Nous pouvons abonner une ou plusieurs fonctions Lambda au flux, mais il n'est pas recommandé d'avoir plus de deux abonnés à un flux car cela peut entraîner une [limitation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html#Streams.Processing).

Au lieu d'utiliser des gestionnaires Lambda pour le flux, nous utiliserons un EventBridge Pipe. Le Pipe nous permettra de nous abonner au flux, d'enrichir et de transformer les données du flux, puis d'envoyer l'événement à notre bus d'événements où nous pouvons définir des règles pour router les événements vers les gestionnaires appropriés.

Au moment de la rédaction de cet article, le construct L2 EventBridge Pipes est toujours en [statut RFC](https://github.com/aws/aws-cdk-rfcs/blob/main/text/0473-eventbridge-pipes.md). Il est possible d'utiliser le [construct proposé](https://github.com/RaphaelManke/aws-cdk-pipes-rfc-473), mais il est instable et sujet à changement. Nous allons nous en tenir au construct L1 [CfnPipe](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_pipes.CfnPipe.html) pour l'instant et espérons passer à L2 lorsque cela sera prêt.

Notre Pipe va lire à partir du flux DynamoDB, utiliser une fonction Lambda pour désérialiser l'enregistrement DynamoDB en JSON simple, puis envoyer l'événement à notre bus d'événements par défaut.

Parce que ce construct est un L1, nous devrons définir explicitement un rôle ainsi que des autorisations.

```typescript
    const cdcPipeRole = new Role(this, 'CDCPipeRole', {
      assumedBy: new ServicePrincipal('pipes.amazonaws.com'),
    });
    
    table.grantStreamRead(cdcPipeRole);
```

Maintenant, nous pouvons définir le Pipe.

```typescript
    new CfnPipe(this, 'CDCStreamPipe', {
      name: 'CDCStreamPipe',
      roleArn: cdcPipeRole.roleArn,
      source: table.tableStreamArn!,
      sourceParameters: {
        dynamoDbStreamParameters: { batchSize: 10, startingPosition: 'LATEST' },
      },
      target: bus.eventBusArn,
      targetParameters: {
        eventBridgeEventBusParameters: {
          source: PROJECT_SOURCE,
          detailType: CDC_EVENT,
        },
      },
    });
```

Pour cibler notre bus d'événements par défaut, nous devons obtenir une référence à celui-ci et accorder à notre rôle l'accès pour envoyer des événements à celui-ci.

```typescript
const bus = EventBus.fromEventBusName(this, 'DefaultBus', 'default');

bus.grantPutEventsTo(cdcPipeRole);
```

Enfin, nous définirons une fonction Lambda pour enrichir et transformer nos données et accorder l'invocation `cdcEnrichmentFn.grantInvoke(cdcPipeRole);` à notre rôle.

Notre fonction Lambda d'enrichissement CDC utilise la fonction unmarshall de `@aws-sdk/lib-dynamodb` pour transformer les enregistrements DynamoDB en objets JavaScript qui peuvent ensuite être consommés sous forme de JSON. Nous ajoutons également des clés `data` et `meta` à notre charge utile et étiquetons clairement le type d'événement pour faciliter la consommation en aval. Nous pourrions effectuer n'importe quel type de transformation qui a du sens pour notre entreprise ici. Le but de cette fonction est de préparer nos données pour les nombreux consommateurs de notre système.

```typescript
import { unmarshall } from '@aws-sdk/util-dynamodb';

import type { AttributeValue } from '@aws-sdk/client-dynamodb';
import type { DynamoDBRecord } from 'aws-lambda';
import { TABLE_PK, TABLE_SK } from '../constants';

export const handler = async (records: DynamoDBRecord[]) => {
  return records.map((r) => {
    const oldImage = r.dynamodb?.OldImage
      ? unmarshall(r.dynamodb?.OldImage as Record<string, AttributeValue>)
      : undefined;
    const newImage = r.dynamodb?.NewImage
      ? unmarshall(r.dynamodb?.NewImage as Record<string, AttributeValue>)
      : undefined;
    const result: {
      meta: Record<string, string>;
      data: {
        pk: string;
        sk: string;
        eventName: string;
        eventType: string;
        NewImage?: Record<string, unknown>;
        OldImage?: Record<string, unknown>;
      }
    } = {
      meta: {
        fn: process.env.AWS_LAMBDA_FUNCTION_NAME!,
      },
      data: {
        pk: oldImage?.[TABLE_PK] || newImage?.[TABLE_PK] || '',
        sk: oldImage?.[TABLE_SK] || newImage?.[TABLE_SK] || '',
        eventName: r.eventName || 'UNKNOWN',
        eventType:
          oldImage && newImage ? 'UPDATE' : oldImage ? 'REMOVE' : 'INSERT',
      },
    };
    if (newImage) result.data.NewImage = newImage;
    if (oldImage) result.data.OldImage = oldImage;
    return result;
  });
};
```

Notre [construct complet](https://github.com/elthrasher/wims/blob/main/src/constructs/cdc.ts) inclut l'enrichissement ainsi qu'une journalisation supplémentaire qui peut être utile pour comprendre comment notre Pipe fonctionne.

## OrdersProcessor

Ce construct L3 consistera en une règle EventBridge qui déclenche une fonction Step Function chaque fois qu'une nouvelle commande est créée. La fonction Step Function effectuera des ajustements de stock en fonction de la commande et mettra en file d'attente des messages pour SQS à envoyer à notre système de paiements.

La fonction Step Function se compose de deux étapes exécutées en parallèle. Pour effectuer des ajustements de stock, nous pourrions utiliser une fonction Lambda ou nous pouvons utiliser l'[intégration directe](https://docs.aws.amazon.com/step-functions/latest/dg/connect-ddb.html).

```typescript
    const adjustInventory = new DynamoUpdateItem(this, 'AdjustInventory', {
      expressionAttributeNames: { '#quantity': 'quantity' },
      expressionAttributeValues: {
        ':quantity': DynamoAttributeValue.numberFromString(
          JsonPath.format(
            '{}',
            JsonPath.stringAt('$.detail.data.NewImage.quantity')
          )
        ),
      },
      conditionExpression: '#quantity >= :quantity',
      key: {
        [TABLE_PK]: DynamoAttributeValue.fromString('INVENTORY#MACGUFFIN'),
        [TABLE_SK]: DynamoAttributeValue.fromString('MODEL#LX'),
      },
      resultPath: JsonPath.DISCARD,
      table,
      updateExpression: 'set #quantity = #quantity - :quantity',
    });
```

Cette instruction contient une `conditionExpression` qui garantira que nous ne décrémentons pas le stock en dessous de zéro. Cela devrait déclencher un autre événement qui pourrait alors notifier le client qu'il devra attendre que nous réapprovisionnions.

Une autre intégration directe avec SQS transmet ces messages pour être mis en file d'attente pour le paiement.

```typescript
    const enqueuePayment = new SqsSendMessage(this, 'EnqueuePayment', {
      messageBody: TaskInput.fromJsonPathAt('$.detail.data.NewImage'),
      queue,
    });
```

Nous enveloppons tout cela dans un workflow Express car nous savons qu'il s'exécutera très rapidement et que les workflows Express sont plus économiques pour les workflows courts. Une implémentation alternative de ce workflow pourrait impliquer l'envoi d'un [jeton de tâche](https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-wait-token) au système de paiement et la pause jusqu'à ce qu'il soit retourné. Dans ce cas, un workflow Standard est requis car nous savons que notre système de paiement n'est pas rapide.

```typescript
    const sm = new StateMachine(this, 'OrdersStateMachine', {
      definitionBody: DefinitionBody.fromChainable(parallel),
      logs: {
        destination: new LogGroup(this, 'SMLogs', {
          logGroupName: '/aws/vendedlogs/states/OrdersSMLogs',
          removalPolicy: RemovalPolicy.DESTROY,
          retention: RetentionDays.ONE_DAY,
        }),
        includeExecutionData: true,
        level: LogLevel.ALL,
      },
      stateMachineName: 'orders-state-machine',
      stateMachineType: StateMachineType.EXPRESS,
      tracingEnabled: true,
    });
```

Contrairement aux workflows Standard, les workflows Express nécessitent que la journalisation soit configurée afin d'avoir une visibilité sur le tableau de bord. Si nous omettons la journalisation, nous pourrions avoir un temps frustrant à observer la machine à états.

Notre règle EventBridge inclut certains filtres afin que nous ne déclenchions le workflow que sur un événement de création de commande.

```typescript
    new Rule(this, 'OrderStateMachineRule', {
      eventBus: bus,
      eventPattern: {
        source: [PROJECT_SOURCE],
        detailType: [CDC_EVENT],
        detail: {
          data: {
            eventType: ['INSERT'],
            pk: [{ prefix: 'CUSTOMER#' }],
          },
        },
      },
      ruleName: 'OrdersStateMachine',
      targets: [new SfnStateMachine(sm)],
    });
  }
```

Consultez la source complète de [OrdersProcessor](https://github.com/elthrasher/wims/blob/main/src/constructs/orders-processor.ts). Ce construct utilise une règle EventBridge pour implémenter un modèle de bus asynchrone en tant que consommateur d'un événement qui pourrait potentiellement avoir d'autres consommateurs.

## PaymentsQueue

Notre construct PaymentsQueue se compose d'une file d'attente SQS, d'une [file d'attente de lettres mortes](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html) correspondante, et d'une autre ressource Pipe qui route nos événements vers l'API de Paiements. L'utilisation de SQS de cette manière nous donne la capacité de stocker et de redélivrer des événements lorsque nous sommes confrontés à des limitations. Nous pouvons configurer notre file d'attente pour permettre autant de nouvelles tentatives que nécessaire pour notre système avant de finalement livrer à notre file d'attente de lettres mortes.

```typescript
    const dlq = new Queue(this, 'PaymentsDlq', { queueName: 'payments-dlq' });
    
    new Queue(this, 'PaymentsQueue', {
      deadLetterQueue: { maxReceiveCount: 10, queue: dlq },
      queueName: 'payments-queue',
    });
```

Notre construct CfnPipe utilise notre file d'attente comme source et route ces événements vers l'API de Paiements en utilisant un ARN (Amazon Resource Name) composé de l'ID de RestAPI, du stage, de la méthode HTTP et de la ressource.

```typescript
    new CfnPipe(this, 'PaymentsPipe', {
      name: 'PaymentsPipe',
      roleArn: paymentsPipeRole.roleArn,
      source: this.paymentsQueue.queueArn,
      target: Arn.format(
        {
          service: 'execute-api',
          resource: `${api.restApiId}/prod/POST/payments`,
        },
        Stack.of(this)
      ),
      targetParameters: {
        inputTemplate: `{
          "body": <$.body>
        }`,
      },
    });
```

Dans cet exemple simple, nous transmettons simplement le même événement en tant que corps POST, mais il pourrait y avoir une bonne raison d'utiliser une autre fonction d'enrichissement ici.

Voir la [source complète](https://github.com/elthrasher/wims/blob/main/src/constructs/payments-queue.ts) de ce construct. Il implémente un modèle de file d'attente asynchrone où les événements sont mis en file d'attente jusqu'à ce qu'ils puissent être livrés avec succès.

## InventoryMonitor

Ce construct démontre vraiment la puissance de l'EDA. Nous allons définir un sujet SNS avec un abonnement par e-mail, puis une règle pour l'invoquer.

```typescript
    const inventoryStockTopic = new Topic(this, 'InventoryStockTopic');
    inventoryStockTopic.addSubscription(new EmailSubscription('theteam@ourcompany.com'));
```

Ces deux lignes de code sont tout ce dont nous avons besoin pour créer le sujet et y abonner notre équipe. Ensuite, nous définissons la règle EventBridge.

```typescript
    new Rule(this, 'InventoryStockRule', {
      eventBus: bus,
      eventPattern: {
        source: [PROJECT_SOURCE],
        detailType: [CDC_EVENT],
        detail: {
          data: {
            eventType: ['UPDATE'],
            pk: [{ prefix: 'INVENTORY#' }],
            NewImage: {
              quantity: [{ numeric: ['<=', 100] }],
            },
          },
        },
      },
      targets: [new SnsTopic(inventoryStockTopic)],
    });
```

Les règles EventBridge permettent une [correspondance numérique](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns-content-based-filtering.html#filtering-numeric-matching) sur les filtres, donc nous pouvons facilement implémenter notre logique métier ici afin que la règle ne soit déclenchée que lorsque notre niveau de stock tombe à 100 unités ou moins. Notez que ce construct n'a pas besoin de se soucier de l'envoi de l'événement. Cela est géré par le construct CDC.

La source est disponible [ici](https://github.com/elthrasher/wims/blob/main/src/constructs/inventory-monitor.ts). Ce construct est déclenché par un événement de bus asynchrone qui est converti en un événement de diffusion en utilisant SNS.

## Benchmarking v1 vs. v2

### v1

Nous pouvons utiliser un [script simple](https://github.com/elthrasher/wims/blob/legacy/benchmark.mjs) pour faire du benchmarking. Ce script tentera de déclencher 10 événements simultanés, attendra qu'ils se terminent, puis bouclera jusqu'à ce que nous ayons créé 1000 commandes. Un outil fonctionnant sur NodeJS ne nous donnera pas une véritable simultanéité (les requêtes sont initiées séquentiellement), mais c'est suffisant pour nos besoins.

L'exécution du script contre le système v1 plusieurs fois donne des résultats assez cohérents.

```bash
Time for 1000 orders.: 2:04.980 (m:ss.mmm)
{ '200': 613, '429': 387 }
```

Il a fallu plus de 2 minutes pour traiter 1000 commandes. Puisque nous en exécutions dix à la fois, cela signifie qu'il a fallu environ 1,25 seconde pour chaque itération. Ce n'est pas mal, mais nous avons un gros problème lorsque notre API de Paiements est limitée, cette erreur est renvoyée à l'utilisateur. Dans ce cas, la commande et l'ajustement de l'inventaire ont tous deux été capturés avec succès, mais le paiement a échoué. Un taux d'erreur de 38,7 % est beaucoup trop élevé ! Nous pourrions vouloir améliorer la latence, mais le taux d'erreur est un problème critique. Ce problème peut-il être résolu avec la nouvelle architecture ?

### v2

En exécutant le même script contre le système v2, nous voyons une amélioration immédiate !

```bash
Time for 1000 orders.: 39.588s
{ '200': 1000 }
```

Nos itérations prennent moins d'un tiers du temps et nous n'avons aucune erreur ! Mais ce n'est pas vraiment équitable, puisque le but de cette architecture est que nous faisons moins de travail au départ lorsque nous créons la commande. Est-ce que tout le reste se passe comme il se doit ? À quel point la cohérence est-elle éventuelle ?

Pour vérifier nos ajustements d'inventaire, nous pouvons interroger les niveaux d'inventaire avant et après l'exécution du script et voir si tous ont été effectués. Le script fait un nombre variable d'unités par commande, donc nous garderons un total cumulé et verrons s'ils se réconcilient tous.

```bash
Starting Inventory: 1000000
Inventory at next tick: 994536
Inventory reduced by: 5464 of sales total 5536.
Time for 1000 orders.: 39.396s
{ '200': 1000 }
```

En interrogeant immédiatement après avoir terminé nos commandes, nous pouvons voir que certains des ajustements sont encore en cours. Combien de temps faut-il pour qu'ils se stabilisent ?

L'ajout d'une attente supplémentaire de 500 ms produit le résultat souhaité.

```bash
Starting Inventory: 994464
Inventory at next tick: 988938
Inventory reduced by: 5526 of sales total 5628.
Time for 1000 orders.: 31.332s
{ '200': 1000 }
Inventory after 500ms: 988836
Inventory reduced by: 5628 of sales total 5628.
Waited 500 ms.
```

Tous nos ajustements ont été complétés en moins de temps que le système original pour le faire de manière synchrone !

Notez que les lectures DynamoDB peuvent être [éventuellement cohérentes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html) elles-mêmes, donc nous ne saurons pas si c'est la cause de la légère latence dans les mises à jour ou si nos événements sont encore en cours. En fin de compte, cela n'a pas d'importance si nous avons adopté l'idée de la cohérence éventuelle.

Une autre chose que nous ignorons est de savoir si tous les paiements ont été effectués avec succès. Puisque notre exemple d'API de Paiements est simplement une RestAPI avec une limite de débit et une réponse simulée, il ne sera pas possible pour elle de nous dire si elle a reçu tous les paiements comme ce serait le cas dans un système réel. Nous pouvons nous tourner vers notre architecture de mise en file d'attente pour déterminer si la livraison a été réussie ou non.

Nous avons configuré SQS pour tenter 10 livraisons après quoi il basculera vers notre file d'attente de lettres mortes. Lors de l'exécution du benchmark, nous pouvons utiliser la fonctionnalité "Poll for messages" sur la console AWS et voir les messages en cours d'attente de redélivraison.

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-31-at-1.08.16-PM.png)
_Console AWS SQS montrant les messages en file d'attente pour redélivraison_

Tant que le "Receive count" est inférieur à 10, nous pouvons nous attendre à ce que ces messages continuent d'essayer. Nous voudrons passer à notre file d'attente de lettres mortes pour vérifier les messages à la fin. S'il n'y en a aucun, alors tout a finalement été traité !

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-31-at-1.12.46-PM.png)
_Console AWS SQS montrant que la file d'attente de lettres mortes n'a pas de messages_

Notre API de Paiements a une limite de débit de 5 requêtes par seconde, donc cela devrait prendre au moins 200 secondes pour traiter 1000 requêtes.

### Les résultats sont là !

Le système v1 a traité 1000 commandes en environ 125 secondes avec un taux de réussite misérable de 61,3 %. Le système v2 répond en 30-40 secondes avec une latence supplémentaire de 500 ms pour compléter les ajustements d'inventaire. Les paiements prennent du retard pendant quelques minutes supplémentaires, mais ce n'est qu'une limitation du système de paiement. Nous avons résolu le problème du taux d'erreur et maintenant 100 % de nos requêtes réussissent !

## Coût

Calculons les coûts réels d'exploitation de ce système. Nous savons, d'après l'expérience, qu'il n'y a pas de coût pour l'exécution de 1000 commandes. Tout est bien dans la limite du niveau gratuit. Qu'en est-il d'un million de commandes ?

Voici une estimation avec le [calculateur de prix AWS](https://calculator.aws/#/estimate?id=7de8847e4b38ce17027a2b1cecba9ef2f58d4d15).

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-31-at-1.47.10-PM.png)
_Estimation des coûts pour 12 mois du système WIMS 2.0 montrant un total de 222,84 $_

Cela suppose que 1 million d'unités sont déplacées chaque mois. Espérons que nos marges sont suffisamment bonnes pour nous permettre de dépenser 222,84 $ sur 12 millions vendus. Bien sûr, il s'agit d'un système incomplet, il est donc facile d'imaginer que le système complet coûte 10x ou 100x ce montant, mais même à ces niveaux, cela reste assez abordable (en supposant à nouveau que nous avons des marges raisonnables par MacGuffin). Le meilleur aspect est que nos coûts augmenteront et diminueront avec les chiffres de vente, donc chaque fois que notre facture AWS sera plus élevée que la normale, cela devrait être accompagné de revenus exceptionnels et, de même, si les ventes sont en baisse, nous devrions pouvoir nous consoler avec des factures inférieures à la normale.

## Conclusion

Nous avons commencé avec un système piloté par API qui avait des problèmes d'échelle et d'ajout de nouvelles fonctionnalités, et nous avons décomposé certaines parties pour créer un système orienté événements, éventuellement cohérent, qui reste assez réactif, observable, extensible et économique à exploiter.

Nous avons exploré différents modèles d'événements, y compris les événements synchrones, la file d'attente asynchrone, le bus asynchrone et les événements de diffusion. Nous avons discuté des principes de conception tels que la cohérence éventuelle et l'idempotence, ainsi que des techniques qui peuvent conduire à des résultats déclarés.

J'espère que vous avez apprécié ce voyage et que vous êtes inspiré pour construire de meilleurs systèmes, plus scalables, plus observables et plus économiques en conséquence. J'adorerais avoir de vos nouvelles et bon développement !