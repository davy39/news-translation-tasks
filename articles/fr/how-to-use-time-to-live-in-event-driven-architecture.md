---
title: Comment utiliser le Time To Live dans l'architecture pilotée par événements
  dans AWS
subtitle: ''
author: Anant Chowdhary
co_authors: []
series: null
date: '2024-06-19T18:08:45.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-time-to-live-in-event-driven-architecture
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/pexels-giallo-859895.jpg
tags:
- name: AWS
  slug: aws
- name: distributed systems
  slug: distributed-systems
- name: software architecture
  slug: software-architecture
seo_title: Comment utiliser le Time To Live dans l'architecture pilotée par événements
  dans AWS
seo_desc: "Distributed systems generally involve the storage and exchange of huge\
  \ amounts of data. Not all data is created the same, and some of it can even expire\
  \ – by design. \nAs the Buddha said, \"All conditioned things are impermanent.\"\
  \nIn this article, we'l..."
---

Les systèmes distribués impliquent généralement le stockage et l'échange de grandes quantités de données. Toutes les données ne sont pas créées de la même manière, et certaines peuvent même expirer - par conception.

Comme l'a dit Bouddha, "Toutes les choses conditionnées sont impermanentes."

Dans cet article, nous examinerons comment le concept de temps de vie peut nous aider avec ce type de données et quand il est judicieux de l'utiliser.

## Table des matières

1. [Qu'est-ce que le Time to Live (TTL) dans les systèmes distribués ?](#heading-quest-ce-que-le-time-to-live-ttl-dans-les-systemes-distribues)
2. [Comment utiliser le TTL dans les files d'attente de messages (AWS SQS)](#heading-comment-utiliser-le-ttl-dans-les-files-dattente-de-messages-aws-sqs)
3. [Comment utiliser le TTL dans les systèmes de stockage d'objets (AWS S3)](#heading-comment-utiliser-le-ttl-dans-les-systemes-de-stockage-dobjets-aws-s3)
4. [Comment utiliser le TTL dans les bases de données (AWS DynamoDB)](#heading-comment-utiliser-le-ttl-dans-les-bases-de-donnees-aws-dynamodb)
5. [Comment utiliser le TTL dans l'architecture basée sur les événements](#heading-comment-utiliser-le-ttl-dans-larchitecture-basee-sur-les-evenements)
6. [Résumé](#heading-resume)

## Qu'est-ce que le Time to Live (TTL) dans les systèmes distribués ?

Le TTL, comme son nom l'indique, est la durée pendant laquelle une donnée reste pertinente ou stockée dans un système distribué ou un composant d'un système distribué. Un TTL peut être défini sur toute donnée qui n'est pas nécessaire indéfiniment.

Savoir quand et quand ne pas utiliser un TTL peut parfois être délicat. Cela peut également affecter la manière dont un système est conçu, ainsi que les considérations de coût et de mise à l'échelle. Dans les sections suivantes, nous apprenons quand et quand ne pas utiliser le TTL.

### Où le TTL a-t-il du sens ?

Comme mentionné ci-dessus, il est judicieux d'utiliser le TTL pour toute donnée éphémère. Voici quelques exemples courants de cas d'utilisation où vous pouvez définir un TTL sur les données :

1. **Données mises en cache** : Les données mises en cache sont omniprésentes dans les systèmes distribués. Par exemple, les ressources d'un post très populaire sur les réseaux sociaux (image, vidéo, audio) peuvent être mises en cache sur les serveurs d'un CDN (Content Delivery Network). Vous ne voulez pas que ces données restent indéfiniment sur le serveur, donc dans certains cas, il peut être judicieux d'ajouter un TTL à ces données, afin qu'elles soient automatiquement supprimées après une certaine période.
2. **Données d'analyse** : La plupart, sinon tous les systèmes à grande échelle, stockent une forme de métriques qui aident à analyser des éléments tels que la latence, la santé du système et les métriques produit, entre autres. Dans un grand nombre de cas, vous ne voudriez pas que ces métriques soient stockées dans les systèmes indéfiniment. Seules les données récentes (par exemple 60 jours ou 180 jours) peuvent être utiles dans la plupart des cas. Un TTL sur les données dans ce cas a du sens, surtout si vous avez des contraintes de mémoire.
3. **Données indexées** : La recherche est une fonctionnalité omniprésente dans les produits. Qu'il s'agisse d'applications de réseaux sociaux, de courriels ou de moteurs de recherche, les données indexées sont vitales pour des recherches ultra-rapides. Les données indexées, cependant, peuvent devenir obsolètes après un certain temps, il est donc judicieux que l'index expire après un certain temps. Par conséquent, un TTL ici peut être utile.
4. **Applications de réseaux sociaux avec contenu éphémère** : Les applications de réseaux sociaux avec contenu éphémère sont extrêmement populaires et les images/vidéos publiées sont souvent éphémères. Si ces images n'ont pas besoin d'être stockées pour la postérité, elles peuvent bénéficier d'un TTL défini sur elles. En plus d'être efficaces en mémoire, cela aide également à la confidentialité.

### Où le TTL n'a-t-il pas de sens ?

Dans la section ci-dessus, nous avons examiné quelques cas où le TTL a du sens. Qu'en est-il des cas où le TTL n'est pas courant et n'est pas utile ? Examinons quelques exemples :

1. **Médias stockés pour les plateformes de streaming** : Les plateformes de streaming utilisent souvent des solutions de stockage cloud telles qu'Amazon AWS S3 pour stocker des objets qui correspondent aux médias qu'elles diffusent aux clients. Ces formes de médias ne sont généralement pas éphémères et sont censées rester sur les plateformes pendant des années, voire des décennies. Comme ces données ne sont pas censées expirer de sitôt, le TTL n'a pas de sens ici.
2. **Transactions bancaires** : Les transactions bancaires produisent certaines des données les plus sensibles stockées dans des systèmes cloud et distribués. À des fins d'audit et de tenue de livres, ces données sont généralement stockées pendant des décennies. Ainsi, puisque ces données n'expirent apparemment jamais, il n'y a généralement pas d'utilité pour un TTL ici. Cela ne signifie pas que cette forme de données ne peut pas être déplacée de bases de données/caches à accès rapide vers des formes de stockage de données plus lentes et moins chères, cependant.

## Comment utiliser le TTL dans les files d'attente de messages (AWS SQS)

AWS SQS est une solution de mise en file d'attente de messages distribués qui est l'épine dorsale de nombreux systèmes distribués polyvalents à travers le monde. Les files d'attente de messages peuvent traiter des milliards de messages et sont utilisées presque universellement dans les systèmes distribués à travers le monde.

Dans cette section, nous examinerons comment les TTL peuvent être utiles lorsque nous considérons les options de conception concernant les files d'attente de messages.

Que se passe-t-il si les consommateurs d'une file d'attente de messages ont été en retard pendant plusieurs jours, ou si les messages n'ont tout simplement pas été consommés depuis un certain temps ? Nous avons la possibilité de définir un Time To Live personnalisé sur les messages SQS.

[Par défaut, la période de conservation est de 4 jours](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-basic-architecture.html#). Le TTL maximum au moment de la rédaction est de 14 jours. Il est donc important d'être conscient des contraintes telles que celles-ci lors de l'utilisation d'AWS SQS pour concevoir des systèmes.

Notez qu'avec AWS SQS, une période de conservation est définie sur la file d'attente elle-même, et non individuellement pour chaque message.

Boto est un SDK AWS pour Python qui permet aux développeurs de créer, configurer et gérer des services et ressources AWS de manière programmatique. Boto est largement utilisé pour le prototypage, les systèmes de production, et offre en général une interface conviviale pour accéder à des services comme S3, EC2 et DynamoDB.

Voici un extrait de code utilisant [Boto](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) qui vous aidera à définir l'attribut `MessageRetentionPeriod` qui est le nom formel pour TTL dans ce contexte.

```python
sqs = boto3.client('sqs', 
aws_access_key_id=votre_aws_access_key_id, 
aws_secret_access_key=aws_secret_access_key, 
region_name='votre_region')

# Définir la période de conservation souhaitée en secondes
retention_period_seconds = 86400  # Exemple : 1 jour

# Définir les attributs de la file d'attente
response = sqs.set_queue_attributes(
    QueueUrl=votre_queue_url,
    Attributes={
        'MessageRetentionPeriod': str(retention_period_seconds)
    }
)
```

### Délai de visibilité dans les files d'attente de messages (AWS SQS)

Notez que bien qu'il soit tentant de penser au [Délai de visibilité dans SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html) comme au Time To Live, ceux-ci ne sont pas les mêmes. Le Time To Live ou la Période de conservation est différent du Délai de visibilité.

Le délai de visibilité fait plutôt référence à une période de temps généralement plus courte pendant laquelle un message doit être traité (une fois pris en charge par un consommateur). Si ce n'est pas le cas, il est de nouveau dans la file d'attente SQS et visible pour les consommateurs, avec son compteur de réception ayant été augmenté de un.

## Comment utiliser le TTL dans les systèmes de stockage d'objets (AWS S3)

Le très polyvalent AWS S3, qui est une solution de stockage d'objets, donne aux utilisateurs la possibilité de définir un Time To Live sur les objets stockés dans les buckets S3.

S3 est extrêmement flexible avec la manière dont les TTL sont définis sur les objets / buckets. Vous pouvez définir des règles de cycle de vie pour spécifier quels objets ou quelles versions d'un objet vous souhaitez supprimer.

[Gérer votre cycle de vie de stockage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) est une excellente lecture sur le site de documentation AWS.

## Comment utiliser le TTL dans les bases de données (AWS DynamoDB)

Certains types de données dans les bases de données sont des candidats idéaux pour avoir un TTL défini sur eux. Des morceaux de données tels que les journaux et les données d'analyse peuvent devenir obsolètes très rapidement, et/ou ils peuvent perdre leur utilité avec le temps.

Le TTL dans DynamoDB offre une approche rentable qui vous permet de supprimer automatiquement les éléments qui ne sont plus pertinents. Il est supporté nativement et peut être défini sur toute la table DynamoDB.

Voici un extrait de code qui vous permet de définir le TTL sur une table DynamoDB (à nouveau, en utilisant Boto) :

```python
ddb_client = boto3.client('dynamodb')

# Activer le Time To Live (TTL) sur une table DynamoDB existante
ttl_response = ddb_client.update_time_to_live(
    TableName=votre_nom_de_table,
    TimeToLiveSpecification={
        'Enabled': True,
        'AttributeName': votre_nom_dattribut_ttl
    }
)

# Vérifier un code de statut réussi dans la réponse
if ttl_response['ResponseMetadata']['HTTPStatusCode'] == 200:
    print("Le Time To Live (TTL) a été activé avec succès.")
else:
    print(f"Échec de l'activation du Time To Live (TTL)")
```

Ici, l'attribut `votre_nom_dattribut_ttl` est l'attribut que DynamoDB examine pour déterminer si l'élément doit être supprimé ou non. L'attribut est généralement défini sur un horodatage dans le futur. Lorsque cet horodatage est atteint, DynamoDB supprime l'élément de la table.

## Comment utiliser le TTL dans l'architecture basée sur les événements

Jusqu'à présent, nous avons discuté du Time To Live et de son utilité. Qu'en est-il de ses implications ? De nombreuses solutions basées sur le cloud fournissent des notifications qui peuvent indiquer qu'une donnée a effectivement atteint son expiration, et vous permettent de prendre des actions en fonction de l'expiration de cette donnée.

Examinons un cas d'utilisation courant. Supposons que vous construisez une application de réseau social qui permet aux utilisateurs de s'envoyer des messages éphémères. Bien que le contenu de ces messages soit éphémère, vous pouvez toujours vouloir conserver un journal des utilisateurs avec lesquels un utilisateur particulier a échangé des messages, même si le contenu du message (audio/vidéo/image) a expiré.

Le diagramme ci-dessous explique une architecture possible en détail :

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1706250152880/7c0d7b46-df5f-4d22-996f-4ea75889630e.png)
_Exemple d'architecture d'application de réseau social_

Supposons qu'un utilisateur échange des messages avec un autre utilisateur. Une entrée correspondant à un message est stockée dans _ActiveMessageDB_ que nous supposerons, pour simplifier, être une base de données NoSQL qui stocke les messages.

Si l'application permet ici l'expiration des messages, vous pourriez définir un TTL sur l'entrée. Bien que l'entrée du message elle-même soit supprimée après que le TTL soit atteint, un événement peut être déclenché pour informer un système que le message est en cours de suppression.

Dans le diagramme ci-dessus, l'événement est capté par une instance AWS Lambda et une quantité de données beaucoup plus petite est écrite dans une autre base de données _MessageLogDB_ qui n'est pas aussi fréquemment accessible que _ActiveMessageDB_. Ce que nous venons de voir est une instance d'architecture basée sur les événements couplée avec le TTL.

## Résumé

1. Le TTL est la durée pendant laquelle une donnée reste pertinente ou stockée dans un système distribué ou un composant d'un système distribué.
2. Le TTL a du sens dans les cas d'utilisation où les données peuvent être supprimées, peuvent expirer, ou leur forme peut changer après une certaine période.
3. Le TTL est populaire et généralement facile à définir sur de nombreuses offres de systèmes distribués.
4. Le TTL peut être couplé avec une architecture pilotée par événements pour transformer les données.