---
title: Comment utiliser les fonctions Azure pour traiter des messages à haut débit
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-27T10:53:44.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-azure-functions-to-process-high-throughput-messages-996d05d4ab23
coverImage: https://cdn-media-1.freecodecamp.org/images/1*c37536mEXRF32zB3duPzTA.png
tags:
- name: Azure
  slug: azure
- name: Cloud Computing
  slug: cloud-computing
- name: General Programming
  slug: programming
- name: serverless
  slug: serverless
- name: 'tech '
  slug: tech
seo_title: Comment utiliser les fonctions Azure pour traiter des messages à haut débit
seo_desc: 'By Nadeem Ahamed

  Authored with Steef-Jan Wiggers, Azure MVP.

  With Microsoft Azure, customers will push all types of workloads to its services.
  Workloads are ranging from datasets for Machine Learning purposes to a large number
  of messages for the Ser...'
---

Par Nadeem Ahamed

Rédigé avec [Steef-Jan Wiggers, MVP Azure](https://www.serverless360.com/blog/author/steef?utm_source=medium-freecodecamp&utm_medium=author-name&utm_campaign=blog-resurfacing).

Avec Microsoft Azure, les clients pousseront tous types de charges de travail vers ses services. Les charges de travail vont des ensembles de données pour des fins d'apprentissage automatique à un grand nombre de messages pour le Service Bus. Dans tous les cas, Azure, comme tout fournisseur de cloud, est suffisamment élastique pour gérer toute taille de charge de travail. La scalabilité et la disponibilité sont des phrases courantes pour le cloud computing. De plus, vous exploitez le cloud pour cela et payez pour son utilisation.

### Scénario de messagerie

Dans cet article de blog, nous examinerons un scénario de messagerie spécifique. Supposons que nous avons un grand nombre de messages poussés vers un sujet de bus de service à partir d'une application LOB. De plus, plusieurs écouteurs sont attachés à des abonnements sur un sujet. Le nombre de messages par abonnement est de 50 à cent par seconde — pour le bus de service, c'est facile à gérer. Le défi dans ce scénario est de savoir comment mettre à l'échelle un service Azure consommant ces messages au même rythme. Utiliseriez-vous des fonctions, un web job ou peut-être Service Fabric ?

Pour cet article de blog, nous choisissons une application cliente générant ~100 000 messages par minute ou environ 1 666 messages par seconde. Chaque message est envoyé à un sujet dans Azure avec cinq abonnements. Chaque abonnement a une fonction Azure correspondante consommant le message (déclencheur de sujet de bus de service) et l'insérant dans une collection de documents Cosmos DB.

![Image](https://cdn-media-1.freecodecamp.org/images/YRIPBCqQLxLvkEJvrSdu-a66VLIuxrHryPtX)

### Fonctions Azure

Les fonctions Azure font partie de la suite Azure Web + Mobile des services d'application. Elles sont conçues pour permettre la création de petites pièces de méthodes significatives et réutilisables. Ces méthodes sont facilement partagées entre les services. Ces méthodes sans serveur, pilotées par événements, sont souvent appelées _"nano-services"_ en raison de leur petite taille. Bien qu'une fonction Azure puisse contenir une quantité importante de code, elles sont généralement conçues pour servir un seul objectif et répondre aux événements dans les services connectés.

Dans notre scénario, les fonctions peuvent répondre aux messages dans une file d'attente ou un sujet (abonnement) de bus de service. Le défi pour le débit réside dans l'hébergement des fonctions. Les fonctions peuvent s'exécuter sur un plan de consommation ou un plan de service d'application. Ce dernier permet une dimensionnement à la hausse. Lorsque vous exécutez sur consommation, vous payez pour l'infrastructure sous-jacente soutenant votre fonction dans une application de fonction.

Nous choisissons de développer une fonction simple en utilisant la liaison de déclencheur de sujet et la liaison Cosmos DB pour la sortie. Le code de la fonction est le suivant :

```java
using System;
using System.Threading.Tasks;
public static void Run(string mySbMsg, ILogger log, out object outputDocument)
{
log.LogInformation($"C# ServiceBus topic trigger function processed message: {mySbMsg}");
outputDocument = new
{
mySbMsg
};
}
```

Le message entrant est envoyé en sortie (document) à une collection dans CosmosDB. Le facteur limitant potentiel du côté Cosmos DB est le nombre spécifié d'[unités de requête par seconde (RU/s)](https://docs.microsoft.com/en-us/azure/cosmos-db/request-units). Lorsque ce paramètre est trop bas, une limitation de débit se produira et vous verrez apparaître des messages HTTP 429.

De plus, la performance réservée est spécifiée en termes d'unités de requête (RU) par seconde. Par conséquent, chaque opération dans Azure Cosmos DB, y compris les écritures, les mises à jour, les lectures et les requêtes, et la mise à jour d'un document, consomme du CPU, de la mémoire et des IOPs. En spécifiant les unités de requête, vous bénéficiez de performances garanties et d'une élasticité à toute échelle. Pour notre configuration, nous choisissons 10000 RU/s.

### Test de la configuration avec les fonctions Azure

Une fois que nous exécutons le test, nous remarquons qu'il faut jusqu'à 90 secondes pour que notre générateur de messages envoie 100000 messages à un sujet de bus de service dans Azure (Europe de l'Ouest). Par conséquent, nous avons un flux sortant de plus de 1000 messages par seconde. Par la suite, il faut environ 180 secondes supplémentaires pour que cinq fonctions lisent les abonnements correspondants et écrivent dans la collection Cosmos DB. Les documents font environ ~ 1Ko chacun.

Une fois que nous démarrons le test, nous voyons le nombre de requêtes entrantes et sortantes augmenter à 100 par seconde et croître pendant l'essai jusqu'à 500 par seconde.

Pendant l'essai, nous voyons les abonnements se remplir de messages et ensuite diminuer au fil du temps jusqu'à zéro. À la fin, environ 180 secondes après que l'application envoyant les messages ait terminé. Ce comportement peut être observé lors de l'exécution du test pour la première fois.

![Image](https://cdn-media-1.freecodecamp.org/images/6C8hHxeTYI00zdL7vcXs4Ge6c6rCx4UTomWG)

Après que tous les abonnements aient été lus et que les fonctions aient terminé le traitement des requêtes entrantes et sortantes dans les métriques en direct des Application Insights chutent à zéro.

![Image](https://cdn-media-1.freecodecamp.org/images/xOuhKPd3c3ALsjaEWSVjpftD9jDNsSE0D6OQ)

### Après plusieurs tests, le résultat est le suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/S7FcJSV6VoGYRj6ac9cTlC8S7Vpt2-rclvx8)

L'expéditeur de messages envoie en 90 secondes 100000 messages à un sujet de Service Bus : > 1100 messages/seconde.

Les cinq fonctions consomment et traitent les 100000 messages en 270 secondes : > 350 messages/seconde. Après un test, les fonctions sont préchauffées. Tout test suivant le premier entraîne un débit de plus de 1000 messages/seconde. Cela correspond à la latence que Cosmos DB promet lors de l'écriture de messages d'environ 1 Ko.

Notez que lorsque vous exécutez des fonctions sur un plan de consommation, votre application peut s'endormir, entraînant des problèmes de démarrage à froid. Selon un article de Chris 'O Brien, MVP :

![Image](https://cdn-media-1.freecodecamp.org/images/D-UL-NiGG6RejKC1OLKmgj5OtJBPTjjutPop)

> _Actuellement, la période de délai d'attente pour les fonctions Azure est de 20 minutes — donc si des périodes où votre fonction ne s'exécutera pas, vous souffrirez de ce problème._

Ce comportement se manifeste lors du test du scénario, la première fois. Après que les fonctions soient préchauffées, le débit triple de ~ 350 à ~ 1150 msg/sec.

Nous réexécutons les tests avec une fonction dans une application de fonction utilisant un plan de service d'application B3 (Standard) et le nombre d'instances défini à trois. De plus, le nombre de fonctions et d'abonnements a été limité à trois.

Le test avec un plan de service d'application utilisant un B3 a conduit à un débit de ~ 1150 messages/sec à chaque fois sans aucun problème de préchauffage.

![Image](https://cdn-media-1.freecodecamp.org/images/AgyczAhS40Xt82W19bxbSZNU0f4M5EO0vxhM)

Les graphiques ci-dessus montrent que le nombre de requêtes entrantes et sortantes est autour du débit mesuré.

![Image](https://cdn-media-1.freecodecamp.org/images/-X1FHjnYrlqR-7wy9qFWKtCvHWkBO38h8Fe0)

Vous pourriez expérimenter davantage en utilisant un plan de service d'application premium ou isolé avec plus de ressources.

### Azure WebJobs

Un moyen utile d'automatiser des tâches dans le cloud est d'utiliser Azure WebJobs hébergés sur Azure App Service. Avec le service d'application, vous pouvez lire en continu des messages à partir d'un sujet (abonnement) ou d'une file d'attente de bus de service sans rencontrer de problèmes de préchauffage. Pour notre scénario, une fonction Azure sur un plan de consommation est suffisante, indépendamment des problèmes de préchauffage.

### Service Fabric

Avec Service Fabric, vous construisez des applications distribuées à l'échelle en exploitant l'infrastructure Azure. Le service est un projet open source et alimente les services principaux d'Azure tels qu'Azure Event Hubs, Cosmos DB et Dynamics 365. Vous pouvez utiliser Service Fabric pour développer des services qui s'auto-dimensionnent en fonction des besoins et donc de tout débit requis. Par conséquent, lorsque vous attendez une performance impossible à atteindre avec Web Jobs ou Azure Functions, vous pouvez opter pour une implémentation Service Fabric. Pour notre scénario, Azure Functions est suffisant pour répondre au débit de 50 à 100 messages par seconde.

### Conclusion

Dans cet article de blog, nous avons examiné un scénario de réalisation d'un débit donné de messages d'un sujet vers Cosmos DB. Avec une fonction, exploitant le bus de service et la liaison Cosmos DB, nous pouvons facilement consommer plus de 300 messages par seconde et insérer les messages dans une collection Cosmos DB. Dans le cas où nous excluons les problèmes de préchauffage, les fonctions peuvent traiter efficacement plus de 1000 messages par seconde.

> _Par conséquent, nous pouvons conclure que les fonctions Azure sont une bonne option pour gérer environ 1000 messages par seconde avec le plan de service approprié en place._

Notez que cet article de blog décrit une petite expérience et que plus d'options sont disponibles pour traiter un volume élevé de messages dans Azure.

### Gestion et surveillance

On peut avoir besoin d'une vision plus approfondie des entités Azure Serverless pour les exploiter. Avec l'outil tiers [Serverless360](https://www.serverless360.com/?utm_source=Freecodecamp-blog&utm_medium=&utm_campaign=), vous pouvez gérer votre solution composite cloud-native en un seul endroit. L'outil surveille vos services d'intégration Azure comme Logic Apps, Functions, Event Hubs, Service Bus et les points de terminaison API. De plus, vous pouvez :

* Dans vos files d'attente ou sujets de bus de service, accéder aux messages actifs pour en savoir plus, traiter les messages de lettres mortes pour les réparer, les renvoyer ou simplement les purger.
* Détecter et être alerté des violations survenant dans vos solutions d'intégration composites.
* Intégrer votre surveillance Azure serverless avec des outils de notification essentiels comme PagerDuty, Microsoft Teams, ServiceNow, Slack, SMTP et OMS.
* Avoir un contrôle total sur ce que vos collègues ou consultants peuvent voir et faire avec les ressources Azure dans votre environnement.
* Le rapport de gouvernance et d'audit fournit des informations détaillées sur les quatre W — QUI a accédé à QUOI, QUAND et POURQUOI. Serverless360 collecte, consolide et permet des filtres de recherche sur vos journaux de compte.

![Image](https://cdn-media-1.freecodecamp.org/images/ZaCZPn44t2r0OqM042dfC9jqf69Dcjix3y0U)
_Application composite Serverless360_

> _Publié à l'origine sur [www.serverless360.com](https://www.serverless360.com/blog/azure-functions-to-process-high-throughput-messages?utm_source=medium-freecodecamp&utm_medium=link&utm_campaign=blog-resurfacing) le 27 novembre 2018._