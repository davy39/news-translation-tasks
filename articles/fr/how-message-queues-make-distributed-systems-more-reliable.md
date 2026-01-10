---
title: Comment les files d'attente de messages aident à rendre les systèmes distribués
  plus fiables
subtitle: ''
author: Anant Chowdhary
co_authors: []
series: null
date: '2024-10-28T13:41:21.714Z'
originalURL: https://freecodecamp.org/news/how-message-queues-make-distributed-systems-more-reliable
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1729895479626/5d476c5d-9749-4c2a-977b-bcdd8b2b8199.jpeg
tags:
- name: AWS
  slug: aws
- name: AWS SQS
  slug: aws-sqs
- name: distributed system
  slug: distributed-system
- name: message queue
  slug: message-queue
seo_title: Comment les files d'attente de messages aident à rendre les systèmes distribués
  plus fiables
seo_desc: 'Reliable systems consistently perform their intended functions under various
  conditions while minimizing downtime and failures.

  As internet users, we tend to take for granted that the systems that we use daily
  will operate reliably. In this article, ...'
---

Les systèmes fiables exécutent de manière cohérente leurs fonctions prévues dans diverses conditions tout en minimisant les temps d'arrêt et les pannes.

En tant qu'utilisateurs d'Internet, nous avons tendance à tenir pour acquis que les systèmes que nous utilisons quotidiennement fonctionneront de manière fiable. Dans cet article, nous explorerons comment les files d'attente de messages améliorent la flexibilité et la tolérance aux pannes. Nous discuterons également de certains défis que nous pouvons rencontrer lors de leur utilisation.

Après avoir lu cet article, vous saurez comment implémenter des systèmes fiables et quels facteurs de performance clés garder à l'esprit.

### **Prérequis**

Avant de plonger dans cet article, vous devriez avoir une compréhension fondamentale de l'informatique en nuage. Voici les concepts clés :

1. Principes de base de l'informatique en nuage

2. Disponibilité dans les systèmes distribués

3. Une compréhension du théorème CAP.

### **Table des matières**

1. [Fiabilité dans les systèmes distribués](#heading-quest-ce-que-la-fiabilite-signifie-dans-le-contexte-des-systemes-distribues)

2. [Qu'est-ce qui rend un logiciel fiable ?](#heading-quest-ce-qui-rend-un-logiciel-fiable)

3. [Qu'est-ce qu'une file d'attente de messages ?](#heading-quest-ce-quune-file-dattente-de-messages)

4. [Comment les files d'attente de messages aident à rendre les systèmes distribués plus fiables](#heading-comment-les-files-dattente-de-messages-aident-a-rendre-les-systemes-distribues-plus-fiables)

5. [Défis avec les files d'attente de messages](#heading-defis-avec-les-files-dattente-de-messages)

6. [Résumé](#heading-resume)

## **Qu'est-ce que la fiabilité signifie dans le contexte des systèmes distribués ?**

La fiabilité, selon l'OED, est « la qualité d'être digne de confiance ou de fonctionner de manière cohérente ». Nous pouvons traduire cette définition dans le contexte des systèmes distribués comme suit :

1. La capacité d'un système technologique, d'un appareil ou d'un composant à exécuter de manière cohérente et fiable ses fonctions prévues dans diverses conditions au fil du temps. Par exemple, dans le contexte de la banque en ligne, la fiabilité fait référence au traitement cohérent et sécurisé des transactions. Les utilisateurs s'attendent à effectuer des transferts et à accéder à leurs comptes sans erreurs ni pannes.

2. Le système est résilient face aux interactions inattendues ou erronées des utilisateurs ou d'autres systèmes interagissant avec lui. Par exemple, si un utilisateur tente d'accéder à un fichier supprimé sur un système de stockage en nuage, le système peut le notifier de manière élégante et suggérer des alternatives, plutôt que de planter.

3. Le système fonctionne de manière satisfaisante dans ses conditions d'exploitation prévues, ainsi qu'en cas de charge inattendue et/ou de perturbations. Un exemple de cela est un service de streaming vidéo lors d'un grand événement sportif. Le système est conçu pour fonctionner correctement sous un trafic normal, mais doit également gérer les pics soudains d'utilisateurs lorsque commence un jeu populaire.

Ceci est une vue assez générale de ce qu'est la fiabilité, et la définition change avec le temps, à mesure que les systèmes évoluent avec la technologie.

## **Qu'est-ce qui rend un logiciel fiable ?**

Il existe divers composants clés utilisés à l'échelle de l'industrie pour rendre les logiciels distribués fiables, comme utilisé dans les systèmes à grande échelle.

### **Réplication des données**

La réplication des données est un concept fondamental dans la conception des systèmes où les données sont intentionnellement dupliquées et stockées dans plusieurs emplacements ou serveurs.

Cette redondance sert plusieurs objectifs critiques, notamment l'amélioration de la disponibilité des données, l'amélioration de la tolérance aux pannes et la possibilité d'équilibrage de charge.

En répliquant les données sur différents nœuds ou centres de données, nous pouvons nous assurer que, en cas de défaillance matérielle ou de problème réseau, les données restent accessibles. Cela réduit les temps d'arrêt et améliore la fiabilité du système.

Il est essentiel de mettre en œuvre des stratégies de réplication avec soin, en tenant compte de facteurs tels que la cohérence, la synchronisation et la résolution des conflits pour maintenir l'intégrité des données et la fiabilité dans les systèmes distribués.

Examinons un exemple concret. Avec un modèle de base de données primaire-secondaire tel que celui utilisé avec les sites web de commerce électronique, nous pouvons avoir ce qui suit :

1. Réplication : La base de données primaire gère toutes les opérations d'écriture, tandis que la ou les bases de données secondaires gèrent toutes les lectures. Cela garantit que les lectures sont réparties sur plusieurs bases de données, améliorant les performances et réduisant la probabilité d'un crash.

2. Cohérence : Le système peut utiliser la cohérence éventuelle pour maintenir l'intégrité, garantissant que toutes les répliques reflètent éventuellement les mêmes données. Mais pendant les périodes de trafic élevé, le site web peut temporairement permettre de légères incohérences, comme l'affichage de niveaux de stock obsolètes.

3. Résolution des conflits : Si deux utilisateurs tentent d'acheter un seul article disponible en même temps, une stratégie de résolution des conflits peut être utilisée. Par exemple, le système pourrait utiliser des horodatages pour déterminer le client qui obtient l'article, et cela peut dicter les mises à jour de la base de données éventuellement.

### **Distribution de la charge sur les machines**

La distribution de la charge implique la répartition des tâches de calcul et du trafic réseau sur plusieurs serveurs ou ressources pour optimiser les performances et assurer la scalabilité du système.

En répartissant intelligemment les charges de travail, la distribution de la charge empêche qu'un seul serveur ne soit surchargé, réduisant ainsi le risque de goulots d'étranglement et de temps d'arrêt.

Certains mécanismes de distribution de charge très couramment utilisés sont :

1. Utilisation d'équilibreurs de charge : Un équilibreur de charge peut répartir uniformément le trafic entrant sur plusieurs serveurs, empêchant qu'un seul serveur ne devienne un goulot d'étranglement.

2. Mise à l'échelle dynamique : La mise à l'échelle dynamique ou automatique peut être utilisée pour ajuster automatiquement le nombre de serveurs actifs en fonction de la demande actuelle, en ajoutant plus de ressources pendant les périodes de pointe et en réduisant l'échelle pendant les périodes de faible trafic.

3. Mise en cache : Des couches de cache peuvent être utilisées pour stocker les données fréquemment consultées, réduisant ainsi la charge sur les serveurs backend en servant les requêtes directement à partir du cache.

### **Planification de la capacité**

La planification de la capacité implique l'analyse de facteurs tels que la croissance prévue des utilisateurs, les exigences de stockage des données et les capacités de traitement pour garantir que le système peut gérer des charges accrues sans dégradation des performances ou temps d'arrêt.

En prévisionnant avec précision les besoins en ressources et en mettant à l'échelle l'infrastructure en conséquence, une telle planification aide à optimiser les coûts, à maintenir la fiabilité et à offrir une expérience utilisateur fluide. Être proactif peut aider à garantir qu'un système est bien préparé à s'adapter aux exigences changeantes et reste robuste et efficace tout au long de son cycle de vie.

De nombreux systèmes modernes peuvent se mettre à l'échelle automatiquement avec les charges projetées. Lorsque le trafic ou les exigences de traitement augmentent, une telle mise à l'échelle automatique provisionne automatiquement des ressources supplémentaires pour gérer la charge. Inversement, lorsque la demande diminue, elle réduit les ressources pour optimiser l'efficacité des coûts.

### **Métriques et alertes automatisées**

Les métriques impliquent la collecte et l'analyse de points de données qui fournissent des informations sur divers aspects du comportement du système, tels que l'utilisation des ressources, les temps de réponse, les taux d'erreur, etc.

Les alertes automatisées complètent les métriques en permettant une surveillance proactive. Cela implique de définir des seuils ou des conditions prédéfinis basés sur les métriques. Lorsqu'une métrique dépasse ou dépasse ces seuils, des alertes automatisées sont déclenchées. Ces alertes peuvent notifier les administrateurs ou les opérateurs du système, leur permettant de prendre des mesures immédiates pour résoudre les problèmes potentiels avant qu'ils n'impactent le système ou les utilisateurs.

Lorsque elles sont utilisées ensemble, les métriques et les alertes automatisées créent un système robuste de surveillance et de dépannage, aidant à garantir que les anomalies ou les problèmes sont rapidement détectés et résolus.

Maintenant que vous savez un peu ce que signifie la fiabilité dans le contexte des systèmes distribués, nous pouvons passer aux files d'attente de messages.

## **Qu'est-ce qu'une file d'attente de messages ?**

Une file d'attente de messages est un mécanisme de communication utilisé dans les systèmes distribués pour permettre une communication asynchrone entre différents composants ou services. Elle agit comme un intermédiaire qui permet à un composant d'envoyer un message à un autre sans avoir besoin de communication directe et synchrone.

![Plusieurs producteurs ajoutant des messages à une file d'attente de messages qui sont à leur tour consommés par un consommateur.](https://cdn.hashnode.com/res/hashnode/image/upload/v1701696280571/8697cb07-c765-4f9e-b709-a7a03adf3e11.png?auto=compress,format&format=webp align="center")

Ci-dessus, vous pouvez voir qu'il y a plusieurs nœuds (appelés Producteurs) qui créent des messages envoyés à une file d'attente de messages. Ces messages sont traités par un nœud appelé le Nœud Consommateur, qui peut effectuer une série d'actions (par exemple, des lectures ou des écritures dans la base de données) dans le cadre du traitement de chaque message.

Examinons maintenant un exemple concret où une file d'attente de messages peut être utile. Supposons que nous avons un site web de commerce électronique qui permet de traiter des millions de commandes.

Le traitement d'une commande peut se dérouler en plusieurs étapes :

1. Un utilisateur crée une commande. Cela déclenche une requête à un serveur web, qui à son tour crée un message placé dans la file d'attente des commandes.

2. Un consommateur lit le message et appelle différents services lors du traitement du message (par exemple, les vérifications d'inventaire, le service de paiement, le service d'expédition).

3. Une fois toutes les étapes de traitement terminées, le consommateur supprime le message de la file d'attente.

Notez que dans le cas où certaines parties du système tombent en panne, le message peut être laissé dans la file d'attente pour être retraité.

Même dans les cas où il y a une panne totale du côté du traitement, les messages peuvent simplement s'accumuler dans la file d'attente et être consommés une fois que les services sont à nouveau fonctionnels. C'est un exemple de l'utilité d'une file d'attente dans plusieurs scénarios de défaillance.

Examinons un peu de code pour ce scénario en utilisant AWS SQS, qui est un service de file d'attente de messages populaire permettant aux utilisateurs de créer des files d'attente, d'envoyer des messages à la file d'attente et également de consommer des messages des files d'attente pour le traitement.

L'exemple ci-dessous utilise [Boto3](http://boto3.amazonaws.com), qui est un client Python pour AWS SQS.

Tout d'abord, nous allons passer une commande, en supposant que nous avons déjà une file d'attente SQS appelée OrderQueue en place.

```python
import boto3
import json

# Créer un client SQS
sqs = boto3.client('sqs')

# Supposons que la file d'attente s'appelle OrderQueue
# C'est la file d'attente dans laquelle les commandes sont placées
queue_url = 'https://sqs.us-east-1.amazonaws.com/2233334/OrderQueue'

# Fonction pour envoyer un message de commande
# Cela place une commande dans la file d'attente, qui peut à tout moment être
# récupérée par un consommateur et ensuite traitée
def send_order(order_details):
    message_body = json.dumps(order_details)
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=message_body
    )
    print(f'Commande envoyée avec l\'ID : {response["MessageId"]}')

# Utilisation de la file d'attente pour passer une commande
# Définition d'une commande exemple

order = {
    'order_id': '12345',
    'customer_id': '67890',
    'items': [
        {'product_id': 'abc123', 'quantity': 2},
        {'product_id': 'xyz456', 'quantity': 1}
    ],
    'total_price': 59.99
}

# Envoi de la commande à la file d'attente qui est censée être récupérée
# par un consommateur et traitée éventuellement.
send_order(order)
```

Une fois la commande passée, voici un exemple de code illustrant comment elle sera récupérée pour traitement :

```python
import boto3
import json

# Créer un client SQS
sqs = boto3.client('sqs')

# Traitement des commandes de la même file d'attente définie ci-dessus
queue_url = 'https://sqs.us-east-1.amazonaws.com/2233334/OrderQueue'

# Fonction pour recevoir et traiter les commandes
# Récupération d'un maximum de 10 messages à la fois pour traitement
def receive_orders():
    response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=10,  # Jusqu'à 10 messages
        WaitTimeSeconds=10
    )
    
    messages = response.get('Messages', [])
    
    for message in messages:
        order_details = json.loads(message['Body'])
        print(f'Traitement de la commande : {order_details}')
        
        # Traitement de la commande avec des détails tels que
        # le traitement des paiements, la mise à jour des niveaux de stock,
        # le traitement de l'expédition, etc.

        # Suppression du message après traitement
        # Cela est important puisque nous ne voulons pas qu'une
        # commande soit traitée plusieurs fois.
        sqs.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=message['ReceiptHandle']
        )
        
# Recevoir un lot de commandes
receive_orders()
```

### **Qu'est-ce qu'un intermédiaire dans un système distribué ?**

Dans le contexte de ce que nous discutons ici, une file d'attente de messages est un intermédiaire. En citant la définition d'Amazon AWS d'une file d'attente de messages :

> « [***Amazon Simple Queue Service (Amazon SQS)***](https://aws.amazon.com/sqs/) *vous permet d'envoyer, de stocker et de recevoir des messages entre les composants logiciels à tout volume, sans perdre de messages ou nécessiter que d'autres services soient disponibles*. »

Ceci est une description succincte et précise de l'importance d'une file d'attente de messages (un intermédiaire).

Dans une file d'attente de messages, les messages sont placés dans une structure de données de file d'attente, que vous pouvez considérer comme une zone de stockage temporaire. Le producteur place les messages dans la file d'attente, et le consommateur les récupère et les traite à son propre rythme. Ce découplage des producteurs et des consommateurs permet une plus grande flexibilité, une meilleure scalabilité et une meilleure tolérance aux pannes dans les systèmes distribués.

## Comment les files d'attente de messages aident à rendre les systèmes distribués plus fiables

Maintenant, discutons de la manière dont les files d'attente de messages aident à rendre les systèmes distribués plus fiables.

### **1. Les files d'attente de messages offrent de la flexibilité**

Les files d'attente de messages permettent une [communication asynchrone](https://en.wikipedia.org/wiki/Asynchrony_(computer_programming)) entre les composants. Cela signifie que les producteurs peuvent envoyer des messages à la file d'attente sans attendre un traitement immédiat par les consommateurs. Cela permet aux composants de travailler de manière indépendante et à leur propre rythme, offrant ainsi de la flexibilité en termes de temps de traitement. C'est donc un excellent moyen de rendre les conceptions flexibles et aussi autonomes que possible.

### **2. Les files d'attente de messages rendent les systèmes scalables**

Les files d'attente de messages sont souvent le pain et le beurre des systèmes distribués scalables pour les raisons suivantes :

1. Plusieurs producteurs peuvent ajouter des messages à une file d'attente de messages. Cela élève le plafond et nous permet de mettre à l'échelle horizontalement les applications facilement.

2. Plusieurs consommateurs peuvent lire à partir d'une file d'attente de messages. Cela nous permet à nouveau de mettre à l'échelle le débit si nécessaire dans de nombreux scénarios.

### **3. Les files d'attente de messages rendent les systèmes tolérants aux pannes**

Que se passe-t-il si un système distribué est submergé ? Nous devons parfois avoir la capacité de « couper le cordon » afin de ramener le système à un état de fonctionnement. Idéalement, nous aimerions avoir la capacité de traiter les requêtes qui n'ont pas été traitées lorsque le système était hors ligne.

C'est exactement ce qu'une file d'attente de messages peut nous aider à faire. Nous pouvons avoir des centaines de milliers de requêtes qui n'ont pas été traitées, mais qui sont encore dans la file d'attente. Celles-ci peuvent être traitées une fois que notre système est à nouveau en ligne.

## **Défis avec les files d'attente de messages**

Comme dans la vie, l'utilisation de files d'attente de messages dans les systèmes distribués n'est pas une solution miracle aux problèmes de mise à l'échelle.

Voici quelques situations où les files d'attente de messages peuvent être utiles :

1. Traitement asynchrone : Les files d'attente de messages sont généralement un excellent choix dans les infrastructures où un traitement asynchrone est requis. Dans les flux de travail tels que l'envoi d'e-mails de confirmation ou la génération de rapports après qu'une commande a été passée, les files d'attente de messages peuvent découpler ces tâches du flux principal de l'application.

2. Équilibrage de charge : Comme nous l'avons vu dans notre exemple pour les files d'attente de messages, dans les scénarios où des pics de trafic se produisent, les files d'attente de messages peuvent tamponner les requêtes entrantes, permettant à plusieurs consommateurs de traiter les messages simultanément. Cela aide à distribuer la charge uniformément sur les ressources disponibles.

3. Tolérance aux pannes : Dans les systèmes où la fiabilité est cruciale, les files d'attente de messages fournissent un mécanisme pour gérer les pannes. Si un service est temporairement hors ligne, les messages peuvent être conservés dans la file d'attente jusqu'à ce que le service soit à nouveau disponible, garantissant qu'aucune donnée n'est perdue sauf si cela est intentionnel.

Voici quelques situations où les files d'attente de messages peuvent ne pas être utiles :

1. Les files d'attente de messages peuvent être excellentes dans les scénarios où l'ordre des messages n'a pas d'importance. Mais dans les situations où l'ordre est important, elles peuvent parfois être lentes et plus coûteuses à utiliser.

2. Concevoir des systèmes avec des files d'attente qui ont plusieurs consommateurs n'est pas trivial. Que se passe-t-il si un message est traité deux fois ? L'[idempotence](https://en.wikipedia.org/wiki/Idempotence) est-elle une exigence ? Ou cela brise-t-il notre cas d'utilisation ? Ces complexités peuvent souvent nous amener à des situations où les files d'attente de messages peuvent ne pas être la meilleure solution.

## **Résumé**

Dans cet article, vous avez appris la fiabilité dans les systèmes distribués et comment les files d'attente de messages peuvent aider à rendre ces systèmes plus fiables. Voici un résumé des points clés à retenir :

1. La fiabilité est centrale pour les systèmes distribués et il existe quelques moyens courants de gérer cela dans l'industrie technologique. La réplication des données, la distribution de charge et la planification de la capacité sont quelques moyens qui peuvent améliorer la fiabilité d'un système.

2. Les files d'attente de messages sont des intermédiaires qui peuvent stocker des messages provenant de producteurs. Elles peuvent être récupérées par des consommateurs à un rythme généralement indépendant du rythme de production.

3. Les files d'attente sont flexibles, nous permettant d'arrêter immédiatement le flux de traitement d'événements indésirables en cas d'événement imprévu.

4. Malgré la polyvalence des files d'attente de messages, elles ne sont pas une panacée pour les problèmes de fiabilité. Il y a souvent plusieurs considérations à garder à l'esprit lors du traitement des messages dans une file d'attente de messages.