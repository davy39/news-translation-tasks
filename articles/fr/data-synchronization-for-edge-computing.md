---
title: Synchronisation des données pour l'informatique de périphérie avec SymmetricDS
subtitle: ''
author: Divya Valsala Saratchandran
co_authors: []
series: null
date: '2025-03-13T12:16:03.365Z'
originalURL: https://freecodecamp.org/news/data-synchronization-for-edge-computing
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1741798507678/d66ed2f3-4116-49ce-a4eb-06fcb7c36dc7.png
tags:
- name: symmetricds
  slug: symmetricds
- name: edgecomputing
  slug: edgecomputing
- name: data synchronization
  slug: data-synchronization
- name: Cloud Computing
  slug: cloud-computing
- name: POS System
  slug: pos-system
seo_title: Synchronisation des données pour l'informatique de périphérie avec SymmetricDS
seo_desc: Edge computing is a distributed system design that moves computation and
  data storage to where it’s most required – at the ‘edge’ of the network. Moving
  these tasks to the edge of the network enables computing in real time, which reduces
  the cost of ...
---

L'informatique de périphérie est une conception de système distribué qui déplace le calcul et le stockage des données là où ils sont le plus nécessaires – à la "périphérie" du réseau. Le déplacement de ces tâches à la périphérie du réseau permet un calcul en temps réel, ce qui réduit considérablement le coût de la bande passante et de la latence.

Mais les environnements d'informatique de périphérie sont confrontés à divers problèmes, tels que la synchronisation des données entre les nœuds de périphérie (comme les appareils locaux) et les systèmes centraux (qui sont généralement des clouds ou des centres de données).

Heureusement, il existe des outils qui peuvent aider à cela. Dans cet article, je vais vous apprendre à utiliser l'outil open source de synchronisation de données et de réplication de base de données SymmetricDS. Vous apprendrez comment l'utiliser au mieux dans les environnements d'informatique de périphérie dans n'importe quel domaine d'activité.

Je vais vous guider à travers les concepts clés derrière SymmetricDS, et discuter de la manière dont il vous aide à optimiser les performances pour l'informatique de périphérie. Nous examinerons également un cas d'utilisation de la synchronisation des données dans l'industrie de la vente au détail.

## Qu'est-ce que SymmetricDS ?

[SymmetricDS](https://symmetricds.org/about/) est un outil logiciel open source utilisé pour la réplication, la synchronisation et l'intégration des données entre les bases de données dans des environnements distribués. Contrairement aux méthodes traditionnelles, où les outils de synchronisation de données sont adaptés à des plateformes spécifiques ou limités à la même base de données, SymmetricDS est conçu et adapté pour synchroniser les données entre les bases de données fonctionnant sur différentes plateformes.

Si vous travaillez dans un environnement qui nécessite uniquement un type de base de données, et qu'une synchronisation unidirectionnelle est suffisante, les méthodes traditionnelles comme la réplication de base de données ou la planification de travaux ETL peuvent être une approche plus facile. Mais pour les environnements complexes qui nécessitent plus de flexibilité et une intégration en temps réel (en particulier avec des appareils de périphérie comme les systèmes POS et les machines industrielles), SymmetricDS peut vous offrir une solution plus adaptable.

## Prérequis

Voici les prérequis dont vous aurez besoin avant d'installer SymmetricDS :

1. **Java Runtime Environment (JRE)** : Java 8.0 ou supérieur installé sur votre système.

2. **Base de données** : Instance en cours d'exécution d'une base de données prise en charge comme MySQL, PostgreSQL, Oracle, SQL Server, etc., et savoir comment la configurer.

3. **Configuration système** : 2 Go de RAM sont recommandés, et les exigences d'espace disque varient en fonction du volume de données et des nœuds impliqués dans la réplication.

## Comprendre l'architecture de SymmetricDS

SymmetricDS fournit une architecture flexible d'informatique de périphérie pour la synchronisation des données sur plusieurs systèmes, y compris les appareils de périphérie. Considérez cet outil comme un réseau flexible qui est configuré en topologie hub-and-spoke ou peer-to-peer.

Une topologie hub-and-spoke possède un hub central (serveur cloud ou sur site) qui est connecté aux nœuds de périphérie (spoke). Le hub central gère la configuration, l'orchestration et la surveillance de la synchronisation des données, tandis que ces nœuds de périphérie capturent et traitent les données localement.

Dans une topologie peer-to-peer, il n'y a pas de hub central et chaque nœud de périphérie agit à la fois comme client et serveur, partageant des données avec ses pairs (nœuds de périphérie).

Chaque nœud de périphérie exécute son propre moteur SymmetricDS, qui gère la synchronisation des données pour sa base de données locale. Le processus de synchronisation utilise un modèle pull-push, où les modifications des données sont capturées et mises en file d'attente à la périphérie, puis transmises au serveur central ou à d'autres nœuds en fonction d'événements planifiés ou déclenchés par des conditions spécifiques.

Un avantage clé de l'utilisation de SymmetricDS dans un environnement de périphérie est la capacité à gérer efficacement les transactions hors ligne. Les nœuds de périphérie peuvent fonctionner de manière autonome pendant les interruptions du réseau et synchroniser les données une fois qu'une connexion réseau est disponible. Cela le rend idéal pour les systèmes POS de vente au détail, la surveillance à distance et les déploiements IoT.

SymmetricDS se compose de :

* **Nœuds** : Instances de base de données individuelles participant à la synchronisation.

* **Canaux** : Groupements logiques de tables pour un routage efficace des données.

* **Déclencheurs** : Capturent les modifications des données (INSERT, UPDATE, DELETE).

* **Routeurs** : Déterminent où les mises à jour des données doivent être envoyées.

* **Lots** : Les données sont regroupées en lots avant la synchronisation.

* **Résolution des conflits** : Gère les conflits de données en cas de mises à jour concurrentes

## Installation et configuration

### Étape 1 : Télécharger et installer SymmetricDS

Pour commencer avec SymmetricDS, téléchargez et extrayez le fichier de l'**Édition Communautaire** (open-source) depuis [SourceForge.net](https://sourceforge.net/projects/symmetricds/files/latest/download) ou de l'**Édition Pro** (sous licence) depuis [Jumpmind Inc](https://jumpmind.com). Assurez-vous que JAVA_HOME est défini dans votre machine.

### Étape 2 : Créer une base de données

Installez une base de données prise en charge (par exemple, MySQL, PostgreSQL, Oracle, SQL Server, etc.). Créez un schéma de base de données et des tables.

### Étape 3 : Configurer un nœud

Chaque base de données participante est un nœud. Vous définissez les nœuds dans `symmetric-ds.properties`. Voici un exemple de configuration :

```sql
engine.name=my-node
db.driver=com.mysql.cj.jdbc.Driver
db.url=jdbc:mysql://localhost:3306/mydb
db.user=root
db.password=root
sync.url=http://localhost:31415/sync/my-node
registration.url=http://localhost:31415/sync/hub
```

Et voici ce qui se passe dans le SQL ci-dessus :

* [`engine.name`](http://engine.name)`=my-node` attribue un nom à l'instance SymmetricDS.

* `db.driver=com.mysql.cj.jdbc.Driver` spécifie le pilote JDBC pour MySQL.

* `db.url=jdbc:mysql://`[`localhost:3306/mydb`](http://localhost:3306/mydb) pointe vers l'URL de la base de données.

* `db.user=root` & `db.password=root` sont les identifiants pour l'accès à la base de données.

* `sync.url` définit l'URL pour la synchronisation (où ce nœud envoie les données).

* `registration.url` spécifie l'URL du nœud hub qui gère les inscriptions.

### Étape 4 : Démarrer SymmetricDS

Pour démarrer SymmetricDS, exécutez la commande suivante depuis le dossier extrait :

```sql
./sym_service start  # Sur Linux/macOS
sym_service.bat start  # Sur Windows
```

Cela lance le moteur SymmetricDS, qui commence à surveiller la base de données configurée pour les modifications.

## Définir les règles de synchronisation

L'un des composants clés de SymmetricDS est ses règles de synchronisation, qui déterminent quelles modifications de données doivent être capturées et routées à travers les nœuds de périphérie. Ces règles sont configurables et définissent comment et quand les données sont transférées entre les bases de données.

Voici quelques étapes à considérer lors de la configuration de vos règles de synchronisation :

### Étape 1 : Définir un groupe de nœuds

Dans SymmetricDS, les règles de configuration sont appliquées à des groupes de nœuds. Cela aide à contrôler comment les données circulent entre différents nœuds dans un environnement distribué.

```sql
INSERT INTO SYM_NODE_GROUP (node_group_id, description)
VALUES ('Store', 'Store Node');
INSERT INTO SYM_NODE_GROUP (node_group_id, description)
VALUES ('Corp', 'Corp Node');
```

Dans ce code,

* Le groupe `Store` représente les nœuds de périphérie (par exemple, les bases de données des magasins).

* Le groupe `Corp` représente le nœud hub central.

### Étape 2 : Définir les liens de groupe

Les liens de groupe définissent quel groupe de nœuds initiéra la synchronisation pour l'échange de données. Ils aident à définir la relation entre deux groupes de nœuds ou plus, spécifiant comment et quand les données circuleront entre les groupes.

```sql
INSERT INTO SYM_NODE_GROUP_LINK (source_node_group_id, target_node_group_id, data_event_action)
VALUES ('Store', 'Corp', 'P'); // 'P' représente 'Push'
INSERT INTO SYM_NODE_GROUP_LINK (source_node_group_id, target_node_group_id, data_event_action)
VALUES ('Corp', 'Store', 'W'); // 'W' représente 'Wait for Pull'
```

Ici,

* Les magasins poussent les données (`'P'`) vers le nœud Corp (par exemple, en envoyant les données de vente au siège).

* Les magasins attendent de tirer (`'W'`) les données de Corp (par exemple, en recevant les mises à jour d'inventaire).

### Étape 3 : Définir le routeur et le routeur de déclenchement pour le flux de données

Les routeurs aident à filtrer les données qui doivent être synchronisées en fonction de règles spécifiques, telles que le type d'opération (insertion, mise à jour, suppression, etc.). Ils aident à garantir que seules les données nécessaires sont routées vers la destination correcte en éliminant les transferts de données inutiles.

```sql
INSERT INTO SYM_ROUTER (router_id, source_node_group_id, target_node_group_id, router_type, 
sync_on_update, sync_on_insert, sync_on_delete)
VALUES('corp to store', 'corp', 'store', 'default ', 1, 1, 1);
INSERT INTO SYM_TRIGGER_ROUTER (trigger_id, router_id, initial_load_order)
VALUES('user', 'corp to store', '1');
```

Ce code fait ce qui suit :

* Définit un routeur nommé `'corp to store'`, qui synchronise les données de Corp vers Store.

* Le type de routeur `'default'` est utilisé.

* `sync_on_update = 1` les mises à jour dans Corp seront synchronisées avec Store.

* `sync_on_insert = 1` les insertions dans Corp seront synchronisées avec Store.

* `sync_on_delete = 1` les suppressions dans Corp seront synchronisées avec Store.

Maintenant, nous lions ce routeur à un déclencheur :

```sql
INSERT INTO SYM_TRIGGER_ROUTER (trigger_id, router_id, initial_load_order)
VALUES ('user', 'corp to store', '1');
```

Cela garantit que le déclencheur (modifications de la table utilisateur) est routé selon la règle `'corp to store'`.

### Étape 4 : Définir les canaux pour la synchronisation

Les canaux définissent le regroupement logique des données dans les tables qui aident à organiser et à séparer les flux de données pour rendre la synchronisation plus efficace et évolutive.

```sql
INSERT INTO SYM_CHANNEL (channel_id, max_batch_size, max_batch_to_send, max_data_to_route, 
enabled, batch_algorithm, description)
VALUES ('users', '10000', '100', '500000', '1', 'default', 'user data');
```

Ce code :

* Définit un canal nommé `'users'`.

* Regroupe les données en morceaux de `10 000` lignes par synchronisation.

* Assure l'efficacité en limitant `100` lots par synchronisation et `500 000` enregistrements par route.

### Étape 5 : Définir les déclencheurs de table

La définition des déclencheurs de table aide à détecter et à gérer les modifications dans la table de la base de données. Ils servent d'écouteurs d'événements qui suivent les modifications dans votre base de données source. Sans déclencheurs de table, le système ne saurait pas quand commencer à synchroniser les modifications ou quelles données doivent être synchronisées.

```sql
INSERT INTO SYM_TRIGGER (trigger_id, source_table_name, channel_id)
VALUES ('user', 'user', 'user');
```

Ce code suit les modifications dans la table `user`. Les modifications sont routées via le canal `users`.

### Étape 6 : Tester la synchronisation des données

Pour tester la synchronisation, insérez quelques données de test dans la base de données source :

```sql
INSERT INTO user (id, name, email) VALUES (1, 'Alice', 'alice@example.com');
```

Ensuite, exécutez la synchronisation SymmetricDS et vérifiez si l'enregistrement apparaît dans la base de données cible.

### Étape 7 : Surveillance et dépannage

Vérifiez les logs dans le fichier `logs/wrapper.log`. Si un lot échoue, vérifiez l'erreur en exécutant la requête SQL suivante :

```sql
SELECT * FROM SYM_OUTGOING_BATCH WHERE ERROR_FLAG = 1;
```

En résultat de l'exécution de la requête ci-dessus, elle récupérera le BATCH_ID erroné. Exécutez le SQL suivant pour obtenir les données exactes du lot échoué :

```sql
SELECT * FROM SYM_DATA WHERE data_id in (select failed_data_id from sym_outgoing_batch 
WHERE batch_id='XXXXX' and node_id='YYYY');
```

## Avantages de SymmetricDS dans l'informatique de périphérie

Dans le contexte de l'informatique de périphérie, où les données sont traitées plus près de la source (par exemple, les systèmes POS, les appareils IoT, les capteurs, etc.), SymmetricDS offre plusieurs avantages pour en faire un outil robuste pour la synchronisation des données :

1. **Latence réduite** : SymmetricDS permet le traitement local des données et la synchronisation avec le serveur central à intervalles réguliers, réduisant la latence impliquée dans le traitement en temps réel dans les environnements cloud.

2. **Optimisation de la bande passante** : il transmet les modifications incrémentielles plutôt que des ensembles de données complets, ce qui réduit le besoin de transfert de données continu. Cela aide à économiser la bande passante.

3. **Tolérance aux pannes** : il assure la réplication des données dans des environnements déconnectés, une fonction clé pour l'informatique de périphérie où la connectivité peut être peu fiable ou intermittente. Il aide également au traitement hors ligne.

4. **Évolutivité** : il s'adapte à de nombreux nœuds de périphérie et prend en charge des architectures complexes, garantissant que les performances s'améliorent même lorsque davantage de fonctionnalités système sont ajoutées.

## Cas d'utilisation : Comment SymmetricDS résout les défis de données en temps réel pour les détaillants

Imaginez une chaîne de magasins de détail avec plusieurs points de vente dans un pays, un état ou une région. Chaque magasin est indépendant avec son propre système local de Point de Vente (POS), son système d'inventaire et ses bases de données d'interaction client.

Mais le siège social dépend des informations en temps réel de tous les magasins pour des décisions clés, telles que les modifications d'inventaire, la génération de rapports de ventes, la surveillance de l'activité client et les promotions. L'objectif est donc de synchroniser toutes ces données provenant de nombreux emplacements de magasins avec une faible latence de manière à ce que les niveaux d'inventaire soient précis, les transactions correctement enregistrées et les opérations de magasin synchronisées.

L'un des problèmes les plus courants dans le commerce de détail est les incohérences d'inventaire entre les magasins. Si un article se vend dans un magasin, le système d'inventaire doit rattraper cela immédiatement pour éviter la survente ou le sous-stockage ailleurs. Les approches traditionnelles de synchronisation des données entraîneront des retards ou des erreurs, conduisant à des situations de rupture de stock ou de surstock dans certains magasins.

SymmetricDS offre une solution plus fiable pour la synchronisation des données en temps réel dans tous les magasins et le système central. Chaque fois qu'un produit est vendu dans un magasin, SymmetricDS met immédiatement à jour les données d'inventaire dans le système local du magasin et la base de données centrale. Cela permet aux autres magasins de maintenir les niveaux d'inventaire actuels et d'éviter les incohérences dans le réseau.

## Conclusion

SymmetricDS possède un ensemble de fonctionnalités robustes pour rationaliser les environnements d'informatique de périphérie. Grâce à son accent sur la synchronisation incrémentielle des données, la compression des données et la réplication asynchrone, SymmetricDS rationalise les performances en termes de latence, d'utilisation de la bande passante et de tolérance aux pannes.

Dans une application pratique, l'utilisation de SymmetricDS dans un environnement d'informatique de périphérie peut grandement améliorer l'efficacité des applications distribuées, permettant une plus grande évolutivité, une prise de décision plus rapide et une moindre dépendance aux serveurs centraux.

En utilisant les méthodes que nous avons discutées ici, les appareils de périphérie peuvent encore fonctionner de manière autonome, se synchroniser avec succès avec le serveur principal et maintenir une sortie de haute performance même dans des conditions de pointe.