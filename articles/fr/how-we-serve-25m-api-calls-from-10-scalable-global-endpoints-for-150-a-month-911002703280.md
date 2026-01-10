---
title: Comment nous servons 25 millions d'appels API à partir de 10 points de terminaison
  mondiaux évolutifs pour 150 $ par mois
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-18T13:31:19.000Z'
originalURL: https://freecodecamp.org/news/how-we-serve-25m-api-calls-from-10-scalable-global-endpoints-for-150-a-month-911002703280
coverImage: https://cdn-media-1.freecodecamp.org/images/1*I-GPwGqtRcyciHkXjIsMLw.jpeg
tags:
- name: api
  slug: api
- name: AWS
  slug: aws
- name: software
  slug: software
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
seo_title: Comment nous servons 25 millions d'appels API à partir de 10 points de
  terminaison mondiaux évolutifs pour 150 $ par mois
seo_desc: 'By Jonathan Kosgei

  I woke up on Black Friday last year to a barrage of emails from users reporting
  503 errors from the ipdata API.

  Our users typically call our API on each page request on their websites to geolocate
  their users and localize their con...'
---

Par Jonathan Kosgei

Je me suis réveillé le Black Friday de l'année dernière à une avalanche d'e-mails d'utilisateurs signalant des erreurs 503 de l'API [ipdata](https://ipdata.co/?utm_campaign=how-we-serve-25M-calls&utm_medium=freecodecamp-post&utm_source=medium).

Nos utilisateurs appellent généralement notre API à chaque requête de page sur leurs sites web pour géolocaliser leurs utilisateurs et localiser leur contenu. Ainsi, cette panne particulière impactait directement les sites web de nos utilisateurs lors du plus grand jour de ventes de l'année.

Je n'ai perdu qu'un seul utilisateur ce jour-là, mais j'ai failli en perdre beaucoup plus.

Cette séquence d'événements et leur nature inexplicable - le CPU, la mémoire et les E/S étaient loin d'être à capacité. Ainsi que les préoccupations concernant la manière dont nous allions évoluer (si tant est que nous le fassions), étant donné notre panne, ont été un grand signal d'alarme pour repenser notre infrastructure existante.

## Notre pile technologique à l'époque

![Image](https://cdn-media-1.freecodecamp.org/images/rqzWDcdQF8izmRhxYtIyeJF0PATKA2yddmv5)

* Framework Python Japronto
* Redis
* Nœuds AWS EC2
* Équilibreurs de charge AWS Elastic Loadbalancers
* Routage basé sur la latence Route53

J'avais effectué des tests sur plusieurs nouveaux micro-frameworks Python prometteurs.

En choisissant entre aiohttp, sanic et japronto, j'ai opté pour [Japronto](https://medium.freecodecamp.org/million-requests-per-second-with-python-95c137af319) après avoir benchmarké les 3 en utilisant [https://github.com/samuelcolvin/aiohttp-vs-sanic-vs-japronto](https://github.com/samuelcolvin/aiohttp-vs-sanic-vs-japronto) et en constatant qu'il avait le débit le plus élevé.

L'API fonctionnait sur 3 nœuds EC2 dans 3 régions derrière des équilibreurs de charge ELB avec un routage basé sur la latence Route53 pour diriger les requêtes vers la région la plus proche de l'utilisateur afin d'assurer une faible latence.

## Choix d'une nouvelle pile technologique

![Image](https://cdn-media-1.freecodecamp.org/images/diPMaejoDxpsKkQxbBsp8J5orTLZn6CIsawU)
_Un exemple d'API météo utilisant notre pile actuelle_

À cette époque, j'ai commencé à sérieusement envisager d'utiliser API Gateway avec AWS Lambda en raison de leurs :

1. Tarification avantageuse - environ 3,50 $ par million sur API Gateway et 0,20 $ par million pour AWS Lambda.
2. Évolutivité infinie et débit élevé - la limite de compte sur API Gateway est de 10 000 requêtes par seconde ou environ 864 millions d'appels par jour. Une limite qu'il est possible de lever en ouvrant une demande de support.

Cela a également rendu économiquement viable d'avoir des points de terminaison dans de nombreuses régions AWS pour offrir des latences faibles à tous nos utilisateurs dans le monde entier.

## Conception d'une API basée sur une passerelle API multi-régionale

Il y avait un certain nombre de défis architecturaux à résoudre pour rendre cela viable.

1. Chaque fonction Lambda dans chaque région devait pouvoir rechercher des données d'utilisation dans une base de données de la même région pour minimiser la latence.
2. Je devais trouver un moyen de déterminer le nombre d'appels API effectués par chaque adresse IP, référent et clé API.
3. Un moyen de synchroniser les données d'utilisation dans toutes les régions. Par exemple, si Route53 envoyait 10 000 requêtes à notre point de terminaison de Sydney, puis décidait d'envoyer les 50 000 suivantes à notre point de terminaison de Séoul (selon le point de terminaison ayant la latence réseau la plus faible à ce moment-là). Chaque fonction Lambda devrait savoir que l'utilisateur avait fait 60 000 requêtes au total pour gérer correctement la limitation de débit.
4. Autorisation - API Gateway fournit des plans d'utilisation et la génération de clés API et vous permet de lier une clé API à un plan d'utilisation. Avec l'avantage supplémentaire que vous n'êtes pas facturé pour les requêtes que les utilisateurs font au-delà de leurs quotas. Cependant, je ne pouvais pas utiliser cela car il était important pour moi de fournir un niveau gratuit sans inscription ni carte de crédit.

Avec beaucoup de travail, j'ai pu résoudre ces problèmes de manière créative.

## Accès aux données d'utilisation localement (pour chaque fonction Lambda)

La solution évidente pour cela était d'utiliser DynamoDB, qui était rentable à grande échelle, rapide et les 200 premiers millions de requêtes par mois étaient gratuits.

DynamoDB offrait également des latences de lecture constamment faibles de 1 à 2 ms.

![Image](https://cdn-media-1.freecodecamp.org/images/dwE0L8p8fjQekAXNod7CLuJ9bnFSOhnNmy7I)

Et cela peut être accéléré dans la plage des microsecondes avec [DynamoDB Accelerator](https://aws.amazon.com/dynamodb/dax/) (DAX).

> DAX porte la performance à un niveau supérieur avec des temps de réponse en microsecondes et fournit des millions de requêtes par seconde pour des charges de travail intensives en lecture.

## Collecte des données d'utilisation pour tous les identifiants

Le défi suivant était de compter en temps réel le nombre de requêtes faites par adresse IP, référent ou clé API.

La manière la plus simple et directe de faire cela serait de mettre à jour un compteur dans une table DynamoDB à chaque appel.

Cependant, cela introduirait des écritures de base de données à chaque appel de notre API, potentiellement introduisant une latence significative.

J'ai pu trouver une solution simple et élégante à cela :

1. Tout d'abord, imprimer un journal (un objet JSON) avec tous les identifiants de requête à chaque requête. C'est-à-dire l'adresse IP, le référent et la clé API si présente. Vraiment juste ;

```
print(event)
```

1. Ajouter un [filtre d'abonnement Cloudwatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Subscriptions.html) au flux de journal Cloudwatch de chaque fonction Lambda dans chaque région et pousser tous les journaux dans un flux Kinesis. Cela me permettrait de traiter les événements de journal de chaque région en un seul endroit central. J'ai choisi Kinesis plutôt que SQS (le service de file d'attente simple d'Amazon) en raison de la capacité à rejouer les événements. SQS supprime l'événement dès qu'un consommateur le lit. Et je voulais la capacité de pouvoir récupérer des pannes de nœud et des pertes de données.
2. Lire à partir du flux Kinesis et mettre à jour une instance [DynamoDB Local](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html) avec les données d'utilisation
3. Utiliser la [bibliothèque de réplication inter-régionale DynamoDB](https://github.com/awslabs/dynamodb-cross-region-library) pour diffuser tous les changements de mon instance DynamoDB locale vers toutes les tables dans toutes les régions en temps réel.

## Authentification des requêtes

Je gère cela en répliquant les clés dans chaque région à l'inscription, de sorte que, peu importe quel point de terminaison un utilisateur atteint, la fonction Lambda qu'il atteint peut vérifier sa clé en vérifiant la table DynamoDB locale dans la même région en quelques millisecondes. Cela stocke également le quota du plan de l'utilisateur et peut, en une seule lecture, vérifier la clé et, si elle existe, obtenir le quota du plan pour comparer l'utilisation et déterminer si la requête doit être acceptée ou rejetée.

## Comment cela s'est passé

Aujourd'hui, nous servons 25 millions d'appels API par mois, soit environ 1 million d'appels par jour.

La majorité d'entre eux en moins de 30 ms, offrant la recherche de géolocalisation IP la plus rapide sur SSL dans l'industrie.

#### [Hyperping.io](https://hyperping.io/)

![Image](https://cdn-media-1.freecodecamp.org/images/D4hfVJDYxsX8O2rz5B-67wN3QE-w-ExvS2eh)

### [Notre page de statut](https://status.ipdata.co)

![Image](https://cdn-media-1.freecodecamp.org/images/OqGMUdPHAQIKxH7SlYTFMu3g9yGCoTBrQ5yg)

La latence est pratiquement la principale raison pour laquelle les développeurs hésitent à utiliser des API tierces pour les recherches GeoIP.

Cependant, nos faibles latences et notre infrastructure mondiale redondante attirent lentement les grandes entreprises vers notre service.

## Coûts

![Image](https://cdn-media-1.freecodecamp.org/images/yqRZHcP929fjBeROjup4i1SIQbStNx3GQBNd)
_Une ventilation de nos coûts_

## Leçons

1. CloudWatch peut être surprenamment coûteux - et ce n'est pas le stockage des journaux. Nous ne stockons les journaux CloudWatch que pendant 24 heures. Les alarmes, les métriques et les requêtes CloudWatch peuvent vraiment s'accumuler.
2. Sur API Gateway, plus vous recevez de requêtes, plus vos latences seront faibles en raison de moins de démarrages à froid. Pour cette raison, j'ai vu des latences aussi basses que 17 ms dans notre région la plus occupée (Francfort) à 40 ms dans nos régions moins occupées comme Sydney.
3. DynamoDB est rapide et vous coûtera moins que vous ne le pensez (ou peut-être pas). Jetez un œil à [https://segment.com/blog/the-million-dollar-eng-problem/](https://segment.com/blog/the-million-dollar-eng-problem/). Au début, je pensais que je serais facturé en fonction du nombre d'unités de capacité de lecture (RCU) et d'unités de capacité d'écriture (WCU) que je provisionnerais. Cependant, la facturation semble être uniquement basée sur l'utilisation, donc si vous provisionnez 1000 RCU et 1000 WCU mais n'utilisez que 5 RCU et WCU, vous ne serez facturé que pour votre utilisation. Cet aspect de la tarification de DynamoDB était un peu difficile à comprendre au début.
4. Augmenter la RAM de votre Lambda peut réduire de moitié votre temps d'exécution et rendre les temps de réponse plus cohérents (ainsi que doubler vos coûts !)
5. Kinesis s'est avéré très fiable sous haute charge. Relayant tous nos événements de journal pour un traitement en temps quasi réel.
6. DynamoDB Local n'est limité que par les ressources de votre système, ce qui le rend idéal pour exécuter des analyses de table ou des requêtes (par exemple lors de la génération de rapports) qui seraient autrement coûteuses à effectuer sur DynamoDB d'AWS. Gardez à l'esprit que DynamoDB Local n'est vraiment qu'un enveloppement Dynamo autour de SQLite. C'est utile et pratique pour notre cas d'utilisation, mais cela pourrait ne pas être le cas pour vous.

## Notes

* AWS a annoncé les tables globales DynamoDB lors de Re:invent l'année dernière, qui synchronisent toutes les écritures dans toutes les tables - entre les régions. Nous ne passons pas à cela pour le moment, car cela n'est disponible que dans 5 régions.
* Amazon a également introduit des autorisateurs personnalisés de type `REQUEST` dans Amazon API Gateway. Cela pourrait potentiellement vous permettre de limiter le débit par adresse IP ainsi que par tout en-tête, paramètre de requête ou de chemin.

Lisez plus d'architectures de la vie réelle sur le blog [highscalability.com](http://highscalability.com).

#### **Mise à jour :**

Consultez notre analyse détaillée de 8 des [meilleures API de géolocalisation IP](https://medium.com/@ipdata_co/what-is-the-best-commercial-ip-geolocation-api-d8195cda7027).