---
title: DynamoDB Cheatsheet – Tout ce que vous devez savoir sur Amazon DynamoDB pour
  la certification AWS Certified Developer Associate 2020
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-28T23:36:40.000Z'
originalURL: https://freecodecamp.org/news/ultimate-dynamodb-2020-cheatsheet
coverImage: https://www.freecodecamp.org/news/content/images/2020/02/DynamoDB-Cheatsheet.png
tags:
- name: AWS
  slug: aws
- name: 'AWSCertified  '
  slug: awscertified
seo_title: DynamoDB Cheatsheet – Tout ce que vous devez savoir sur Amazon DynamoDB
  pour la certification AWS Certified Developer Associate 2020
seo_desc: "By Andrew Brown\nThe emergence of cloud services has changed the way we\
  \ build web-applications. This in turn has changed the responsibilities of a Web\
  \ Developer. \nWe used to build everything into a single web-application on a single\
  \ server. This encom..."
---

Par Andrew Brown

L'émergence des services cloud a changé la façon dont nous construisons des applications web. Cela a à son tour changé les responsabilités d'un développeur web. 

Nous avions l'habitude de tout construire dans une seule application web sur un seul serveur. Cela englobait plusieurs responsabilités telles que le stockage, les bases de données, l'authentification, les tâches en arrière-plan, la mise en cache, et plus encore.

Les services cloud nous permettent de réduire la complexité de notre application web et de nos serveurs web en transférant les responsabilités à ces services cloud hautement disponibles, scalables et durables.

Un développeur web qui sait comment déployer et intégrer des services cloud avec une application web est ce que nous appelons un **ingénieur cloud.**

Si vous voulez accélérer votre carrière en tant que développeur web en 2020, alors la **certification AWS Developer Associate** peut vous aider à atteindre cet objectif final.

Le service AWS le plus important que vous devez étudier pour passer l'examen AWS Developer Associate est DynamoDB. J'ai donc publié ce que j'appelle **The _Ultimate_ DynamoDB Cheatsheet** gratuitement. Vous pouvez l'imprimer le jour de votre examen pour augmenter vos chances de réussite.

C'est [Nader](https://twitter.com/dabit3), l'AWS Developer Advocate pour AWS Amplify, qui a suggéré que je publie ma feuille de triche complète gratuitement. Vous n'auriez pas cette ressource sans lui.

C'est [Kirk](https://twitter.com/NoSQLKnowHow), le technologue senior AWS spécialisé dans DynamoDB, qui a consacré son temps pour garantir l'exactitude de cette feuille de triche. Cela l'a fait passer de 5 pages à 8 pages ! ????????

Si vous avez Twitter, faites-moi la faveur de les remercier en tweettant à [@dabit3](https://twitter.com/dabit3) et [@NoSQLKnowHow](https://twitter.com/NoSQLKnowHow) avec le hashtag #AWSCertified.

Alors passons à la feuille de triche :

## Les bases de DynamoDB

**DynamoDB** est une base de données NoSQL entièrement gérée, de type clé/valeur et document.

DynamoDB est adapté aux charges de travail avec n'importe quelle quantité de données qui **nécessitent des performances de lecture et d'écriture prévisibles** et une mise à l'échelle automatique, de grande à petite et partout entre les deux.

DynamoDB monte et descend en échelle pour supporter quelle que soit la **capacité de lecture et d'écriture que vous spécifiez** par seconde en mode capacité provisionnée. Ou vous pouvez le régler en mode À la demande et il y a peu ou pas de planification de capacité.

* DynamoDB stocke **3 copies des données** sur des disques SSD **à travers 3 AZ** dans une région.
* Les types de données les plus courants de DynamoDB sont **B** (Binaire), **N** (Nombre) et **S** (Chaîne)
* Les tables se composent d'**éléments** (lignes) et les éléments se composent d'**attributs** (colonnes)

## Cohérence des lectures et des écritures

DynamoDB peut être configuré pour supporter des **lectures éventuellement cohérentes** (par défaut) et des **lectures fortement cohérentes** sur une base par appel.

Les **lectures éventuellement cohérentes** renvoient les données immédiatement, mais les données peuvent être incohérentes. Les copies des données seront généralement cohérentes en 1 seconde.

Les **lectures fortement cohérentes** liront toujours à partir de la partition leader, car elle dispose toujours d'une copie à jour. Les données ne seront jamais incohérentes, mais la latence peut être plus élevée. Les copies des données seront cohérentes avec une garantie de 1 seconde.

## Partitions

Une **partition** est lorsque DynamoDB divise votre table en morceaux plus petits de données. Cela accélère les lectures pour les très grandes tables.

DynamoDB crée automatiquement des partitions pour :

* Chaque 10 Go de données ou
* Lorsque vous dépassez les limites de RCU (3000) ou de WCU (1000) pour une seule partition
* Lorsque DynamoDB détecte un schéma de partition chaude, il divise cette partition dans une tentative de résoudre le problème.

DynamoDB essaiera de **répartir uniformément** les RCU et les WCU entre les partitions.

### Conception de la clé primaire

Les clés primaires définissent **où et comment** vos données seront stockées dans les partitions.

Le schéma de clé peut être composé de deux clés :

* La clé de partition (PK) est également connue sous le nom de **HASH**
* La clé de tri (SK) est également connue sous le nom de **RANGE**

> Lorsque vous utilisez l'API AWS DynamoDB, par exemple CLI, SDK, ils font référence à la PK et à la SK par leurs noms alternatifs pour des raisons de compatibilité.

La clé primaire se présente sous deux types :

* Clé primaire **simple** (utilisant uniquement une clé de partition)
* Clé primaire **composite** (utilisant à la fois une clé de partition et une clé de tri)

L'unicité des clés est la suivante :

* Lors de la création d'une clé primaire simple, la **valeur de la PK peut être unique**
* Lors de la création d'une clé primaire composite, **la combinaison de la PK et de la SK doit être unique**

Lorsque vous utilisez une clé de tri, les enregistrements de la partition sont logiquement regroupés ensemble dans l'ordre ascendant.

## Index secondaires

DynamoDB dispose de deux types d'index :

* **LSI** - Index secondaire local
* **GSI** - Index secondaire global

### LSI - Index secondaire local

* Prend en charge les lectures **fortement** ou éventuellement cohérentes
* Ne peut être créé qu'avec la table initiale (ne peut pas être modifié et ne peut pas être supprimé sauf si vous supprimez également la table)
* Uniquement composite
* 10 Go ou moins par partition
* Partage les unités de capacité avec la table de base
* Doit partager la clé de partition (PK) avec la table de base.

### GSI - Index secondaire global

* **Uniquement les lectures éventuellement cohérentes** (ne peut pas fournir une forte cohérence)
* Peut être créé, modifié ou supprimé à tout moment
* Simple et composite
* Peut avoir n'importe quels attributs comme clé primaire (PK) ou clé secondaire (SK)
* Aucune restriction de taille par partition
* A ses propres paramètres de capacité (ne partage pas avec la table de base)

## Scan

Vos tables doivent être conçues de manière à ce que les motifs d'accès principaux de votre charge de travail n'utilisent pas de scans. Globalement, les scans doivent être utilisés avec parcimonie, par exemple pour un rapport peu fréquent.

* Parcourt tous les éléments d'une table puis renvoie un ou plusieurs éléments via des filtres
* Par défaut, renvoie tous les attributs pour chaque élément (utilisez **ProjectExpression** pour limiter)
* Les scans sont séquentiels, et vous pouvez accélérer un scan via des scans parallèles en utilisant **Segments** et **Total Segments**
* Les scans peuvent être lents, surtout avec des tables très grandes et peuvent facilement consommer votre débit provisionné.
* Les scans sont l'une des méthodes les plus coûteuses pour accéder aux données dans DynamoDB.

## Query

* Trouve des éléments basés sur les valeurs de la clé primaire
* La table doit avoir une clé composite afin de pouvoir être interrogée
* Par défaut, les requêtes sont éventuellement cohérentes (utilisez **ConsistentRead True** pour changer en fortement cohérente)
* Par défaut, renvoie tous les attributs pour chaque élément trouvé par une requête (utilisez **ProjectExpression** pour limiter)
* Par défaut, est trié par ordre ascendant (utilisez **ScanIndexForward** à False pour inverser l'ordre en descendant)

## Modes de capacité

DynamoDB dispose de deux modes de capacité, **Provisionné** et **À la demande**. Vous pouvez basculer entre ces modes **une fois toutes les 24 heures**.

### Provisionné

La **capacité de débit provisionnée** est la quantité maximale de capacité que votre application est autorisée **à lire ou à écrire par seconde** depuis une table ou un index.

* **Provisionné** est adapté aux charges de travail prévisibles ou stables
* **RCU** est l'unité de capacité de lecture
* **WCU** est l'unité de capacité d'écriture

**Vous devriez activer l'auto-scaling avec le mode de capacité provisionnée**. Dans ce mode, vous définissez un plancher et un plafond pour la capacité que vous souhaitez que la table supporte. DynamoDB ajoutera et supprimera automatiquement la capacité entre ces valeurs en votre nom et limitera les appels qui dépassent le plafond trop longtemps.

Si vous dépassez votre capacité provisionnée, vous obtiendrez une exception : **ProvisionedThroughputExceededException** (limitation)

La **limitation** est lorsque **les requêtes sont bloquées** en raison d'une fréquence de lecture ou d'écriture supérieure aux seuils définis. Par exemple, dépassement de la capacité provisionnée définie, division des partitions, inadéquation de la capacité de la table/index.

### À la demande

La **capacité à la demande** est payée par requête. Vous ne payez donc que pour ce que vous utilisez.

* À la demande est adapté aux charges de travail **nouvelles** ou **imprévisibles**
* Le débit est uniquement limité par les limites supérieures par défaut pour une table (40K RCU et 40K WCU)
* La **limitation peut se produire** si vous dépassez le double de votre capacité de pointe précédente (marque de haut niveau) en 30 minutes. Par exemple, si vous avez précédemment atteint un maximum de 30 000 opérations/sec, vous ne pourriez pas atteindre immédiatement 90 000 opérations/sec, mais vous pourriez atteindre 60 000 opérations/sec.
* Comme il n'y a pas de limite stricte, **À la demande pourrait devenir très coûteux** en fonction des scénarios émergents

## Calcul des lectures et des écritures

### Calcul des lectures (RCU)

**Une unité de capacité de lecture** représente :

* une lecture fortement cohérente par seconde, 
* ou deux lectures éventuellement cohérentes par seconde,
* pour un élément jusqu'à 4 Ko.

Comment calculer les RCU pour les lectures **fortement cohérentes**

1. Arrondir les données au multiple de 4 le plus proche.
2. Diviser les données par 4
3. Multiplier par le nombre de lectures

Voici un exemple :

* 50 lectures à 40 Ko par élément. (40/4) x 50 = 500 RCU
* 10 lectures à 6 Ko par élément. (8/4) x 10 = 20 RCU
* 33 lectures à 17 Ko par élément. (20/4) x 33 = 132 RCU

Comment calculer les RCU pour les lectures **éventuellement cohérentes**

1. Arrondir les données au multiple de 4 le plus proche.
2. Diviser les données par 4
3. Multiplier par le nombre de lectures
4. Diviser le nombre final par 2
5. Arrondir au nombre entier le plus proche

Voici un exemple :

* 50 lectures à 40 Ko par élément. (40/4) x 50 / 2 = 250 RCU
* 11 lectures à 9 Ko par élément. (12/4) x 11 / 2 = 17 RCU
* 14 lectures à 24 Ko par élément. (24/4) x 14 / 2 = 35 RCU

### Calcul des écritures (WCU)

**Une unité de capacité d'écriture** représente :

* une écriture par seconde, 
* pour un élément jusqu'à 1 Ko

Comment calculer les **écritures**

1. Arrondir les données au multiple de 1 le plus proche.
2. Multiplier par le nombre d'écritures

Voici un exemple :

* 50 écritures à 40 Ko par élément. 40 x 50 = 2000 WCU
* 11 écritures à 1 Ko par élément. 1 x 11 = 11 WCU
* 18 écritures à 500 octets par élément. 1 x 18 = 18 WCU

## DynamoDB Accelerator

DynamoDB Accelerator **(DAX)** est un **cache en mémoire entièrement géré avec écriture directe** pour DynamoDB qui fonctionne dans un cluster.

* Les lectures sont éventuellement cohérentes
* Les requêtes entrantes sont uniformément distribuées sur tous les nœuds du cluster.
* DAX peut réduire les temps de réponse des lectures à des **microsecondes**

### DAX est idéal pour :

* les temps de réponse les plus rapides possibles
* les applications qui lisent un petit nombre d'éléments plus fréquemment
* les applications qui sont **intensives en lecture**

### DAX n'est pas idéal pour :

* Les applications qui nécessitent des lectures fortement cohérentes
* Les applications qui ne nécessitent pas de temps de réponse de lecture en microsecondes
* Les applications qui sont **intensives en écriture**, ou qui ne réalisent pas beaucoup d'activité de lecture
* Si vous n'avez pas besoin de DAX, **envisagez d'utiliser ElastiCache**

## Transactions DynamoDB

DynamoDB prend en charge les transactions via les appels d'API **TransactWriteItems** et **TransactGetItems**.

Les **transactions** vous permettent d'interroger plusieurs tables à la fois et sont une approche tout ou rien (tous les appels d'API doivent réussir).

## Tables globales

Les tables globales DynamoDB fournissent une solution entièrement gérée pour déployer des **bases de données multi-régions, multi-maîtres**.

## Streams

**DynamoDB Streams** vous permet de configurer une fonction Lambda déclenchée chaque fois que des données sont modifiées dans une table pour réagir aux changements. **Les streams ne consomment pas de RCU.**

## API DynamoDB

Les commandes les plus notables de l'API DynamoDB via CLI : **aws dynamodb <command>**

**aws dynamodb _get-item_** renvoie un ensemble d'attributs pour l'élément avec la clé primaire donnée. Si aucun élément correspondant, il ne renvoie aucune donnée et il n'y aura aucun élément Item dans la réponse.

**aws dynamodb _put-item_** crée un nouvel élément, ou remplace un ancien élément par un nouvel élément. Si un élément ayant la même clé primaire que le nouvel élément existe déjà dans la table spécifiée, le nouvel élément remplace complètement l'élément existant.

**aws dynamodb _update-item_** modifie les attributs d'un élément existant, ou ajoute un nouvel élément à la table s'il n'existe pas déjà.

**aws dynamodb _batch-get-item_** renvoie les attributs d'un ou plusieurs éléments d'une ou plusieurs tables. Vous identifiez les éléments demandés par leur clé primaire. Une seule opération peut récupérer jusqu'à **16 Mo de données**, qui peuvent contenir jusqu'à **100 éléments**.

**aws dynamodb _batch-write-item_** met ou supprime plusieurs éléments dans une ou plusieurs tables. Peut écrire jusqu'à **16 Mo de données**, qui peuvent comprendre jusqu'à **25 requêtes de mise ou de suppression**. Les éléments individuels à écrire peuvent être **aussi grands que 400 Ko**.

**aws dynamodb _create-table_** ajoute une nouvelle table à votre compte. Les noms de table doivent être uniques dans chaque région.

**aws dynamodb _update-table_** modifie les paramètres de débit provisionné, les index secondaires globaux ou les paramètres de DynamoDB Streams pour une table donnée.

**aws dynamodb _delete-table_** supprime une table et tous ses éléments.

**aws dynamodb _transact-get-items_** est une opération synchrone qui récupère de manière atomique plusieurs éléments d'une ou plusieurs tables (mais pas d'index) dans un seul compte et une seule région. L'appel peut contenir jusqu'à **25 objets**. La taille totale des éléments dans la transaction **ne peut pas dépasser 4 Mo**.

**aws dynamodb _transact-write-items_** est une opération d'écriture synchrone qui regroupe jusqu'à **25 requêtes d'action**. Ces actions peuvent cibler des éléments dans différentes tables, mais pas dans différents comptes ou régions AWS, et aucune des deux actions ne peut cibler le même élément.

**aws dynamodb _query_** trouve des éléments basés sur les valeurs de la clé primaire. Vous pouvez interroger une table ou un index secondaire qui a une clé primaire composite.

**aws dynamodb _scan_** renvoie un ou plusieurs éléments et attributs d'éléments en accédant à chaque élément d'une table ou d'un index secondaire.

## ? #rocketsToMars

Je veux vous aider à entrer dans l'industrie du web et du cloud. C'est pourquoi je publie mon cours **gratuit** **AWS Developer Associate Certification 2020** sur la chaîne YouTube freeCodeCamp avec plus de 10 heures de contenu supplémentaire que je n'ai jamais publié auparavant.

Ce cours gratuit sera publié dans quelques jours alors que j'applique les dernières touches. 

Je crois en rendant l'éducation technologique accessible au monde entier, car en retour, plus nous améliorons nos compétences, plus nous pouvons sortir les gens de la pauvreté, plus nous pouvons concevoir des solutions durables pour garder notre planète verte et saine, et plus nous pouvons lancer des fusées vers Mars.