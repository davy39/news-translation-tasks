---
title: Comment déployer votre propre instance CockroachDB sur Kubernetes [Livre complet
  pour les développeurs]
subtitle: ''
author: Prince Onukwili
co_authors: []
series: null
date: '2025-11-25T17:16:50.119Z'
originalURL: https://freecodecamp.org/news/deploy-your-own-cockroach-db-instance-on-kubernetes-full-book-for-devs
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1764088553942/496bf5f4-f059-4873-b6c1-419a86e594ef.png
tags:
- name: cockroachdb
  slug: cockroachdb
- name: Databases
  slug: databases
- name: google cloud
  slug: google-cloud
- name: Kubernetes
  slug: kubernetes
seo_title: Comment déployer votre propre instance CockroachDB sur Kubernetes [Livre
  complet pour les développeurs]
seo_desc: 'Developers are smart, wonderful people, and they’re some of the most logical
  thinkers you’ll ever meet. But we’re pretty terrible at naming things 😂

  Like, what in the world – out of every other possible name, they decided to name
  a database after a ...'
---


Les développeurs sont des gens intelligents et merveilleux, et ils comptent parmi les penseurs les plus logiques que vous rencontrerez jamais. Mais nous sommes assez nuls pour nommer les choses 😂

Sérieusement, de tous les noms possibles, ils ont décidé de nommer une base de données d'après un *littéral cafard* ? 🤣

Je veux dire, je comprends : les cafards sont connus pour être résilients, et les développeurs essayaient probablement de dire « notre base de données ne meurt jamais »… mais quand même… un cafard ?

Le nom mis à part, parmi toutes les bases de données existantes, vous vous demandez peut-être pourquoi choisir CockroachDB ? Et si vous la choisissiez, par où commencer pour l'héberger et la déployer ? Opteriez-vous pour un service cloud managé ? Ou pourriez-vous réellement l'auto-gérer ?

Si vous avez déjà pensé à le faire vous-même – peut-être dans un environnement de développement, ou même en l'introduisant dans votre entreprise – comment vous y prendriez-vous ?

Eh bien, calmez vos nerfs 😄

Dans ce livre, nous explorerons tout ce que vous devez savoir sur le **déploiement et la gestion de CockroachDB sur Kubernetes**. Nous approfondirons :

* La compréhension du fonctionnement réel de l'architecture sans maître (multi-primaire) de CockroachDB
    
* La configuration et le déploiement de CockroachDB sur un cluster Kubernetes
    
* L'automatisation des sauvegardes vers Google Cloud Storage en utilisant seulement quelques requêtes dans le cluster CockroachDB
    
* La gestion sécurisée des comptes de service et de l'authentification
    
* Le réglage des paramètres de mémoire de CockroachDB pour des performances stables
    
* La mise à l'échelle horizontale et verticale du cluster sans interruption de service
    
* La surveillance et la maintenance de la base de données comme un pro
    

À la fin, vous comprendrez non seulement comment fonctionne CockroachDB, mais vous serez assez confiant pour déployer et gérer votre propre instance résiliente et prête pour la production. 🚀

## Table des matières

1. [Qu'est-ce que CockroachDB au juste ? 🧐](#heading-qu-est-ce-que-cockroachdb)
    
    * [Définition simple](#heading-definition-simple)
        
    * [Qui a créé CockroachDB ? Quand a-t-il été lancé ?](#heading-qui-a-cree-cockroachdb-quand-a-t-il-ete-lance)
        
    * [Quels problèmes CockroachDB essaie-t-il de résoudre ?](#heading-quels-problemes-cockroachdb-essaie-t-il-de-resoudre)
        
    * [Termes clés à connaître (en langage clair) :](#heading-termes-cles-a-connaitre-en-langage-clair)
        
    * [Pourquoi le nom « CockroachDB » ? 😅](#heading-pourquoi-le-nom-cockroachdb)
        
2. [Pourquoi choisir CockroachDB plutôt que PostgreSQL ou MongoDB 🤷🏾‍♂️ ?](#heading-pourquoi-choisir-cockroachdb-plutot-que-postgresql-ou-mongodb)
    
    * [Comment la tolérance aux pannes est gérée dans PostgreSQL et MongoDB](#heading-comment-la-tolerance-aux-pannes-est-geree-dans-postgresql-et-mongodb)
        
    * [Comment CockroachDB gère cela différemment](#heading-comment-cockroachdb-gere-cela-differemment)
        
3. [Comment CockroachDB fonctionne en coulisses ⚙️](#heading-comment-cockroachdb-fonctionne-en-coulisses)
    
    * [Ranges : Les petits morceaux de données](#heading-ranges-les-petits-morceaux-de-donnees)
        
    * [Réplication : Plusieurs copies pour la sécurité](#heading-replication-plusieurs-copies-pour-la-securite)
        
    * [Consensus Raft : Comment toutes les copies s'accordent](#heading-consensus-raft-comment-toutes-les-copies-s-accordent)
        
    * [MultiRaft : Maintenir l'efficacité de Raft lors de la mise à l'échelle](#heading-multiraft-maintenir-l-efficacite-de-raft-lors-de-la-mise-a-l-echelle)
        
    * [Rééquilibrage : Le mouvement pour l'équilibre](#heading-reequilibrage-le-mouvement-pour-l-equilibre)
        
    * [Transactions distribuées : Travailler sur plusieurs Ranges](#heading-transactions-distribuees-travailler-sur-plusieurs-ranges)
        
    * [Comment tout s'imbrique : Flux de lecture + écriture (Ce qui se passe quand vous l'utilisez)](#heading-comment-tout-s-imbrique-flux-de-lecture-ecriture)
        
    * [Pourquoi tout cela est important (En langage clair)](#heading-pourquoi-tout-cela-est-important)
        
4. [Où (et comment) devriez-vous héberger CockroachDB ? ☁️](#heading-ou-et-comment-devriez-vous-heberger-cockroachdb)
    
    * [Option 1 : CockroachDB Cloud (entièrement managé par Cockroach Labs)](#heading-option-1-cockroachdb-cloud)
        
    * [Option 2 : Bring Your Own Cloud (BYOC)](#heading-option-2-bring-your-own-cloud-byoc)
        
    * [Option 3 : Utiliser les Marketplaces Cloud (AWS, GCP, Azure)](#heading-option-3-utiliser-les-marketplaces-cloud)
        
    * [Option 4 (Ma préférée 😁) : Auto-hébergement — Surtout avec Kubernetes](#heading-option-4-auto-hebergement-surtout-avec-kubernetes)
        
5. [Configuration de votre environnement local 🧑🏾‍💻](#heading-configuration-de-votre-environnement-local)
    
    * [Pourquoi ces outils ?](#heading-pourquoi-ces-outils)
        
    * [Étape 1 : Installer Minikube](#heading-etape-1-installer-minikube)
        
    * [Étape 2 : Installer kubectl](#heading-etape-2-installer-kubectl)
        
    * [Étape 3 : Installer Helm](#heading-etape-3-installer-helm)
        
6. [Déploiement de CockroachDB sur Minikube (La partie amusante commence 😁 !)](#heading-deploiement-de-cockroachdb-sur-minikube)
    
    * [Étape 1 : Visiter ArtifactHub](#heading-etape-1-visiter-artifacthub)
        
    * [Étape 2 : Explorer le Helm Chart](#heading-etape-2-explorer-le-helm-chart)
        
    * [Étape 3 : Copier les valeurs par défaut](#heading-etape-3-copier-les-valeurs-par-defaut)
        
    * [Étape 4 : Créer un dossier pour notre projet](#heading-etape-4-creer-un-dossier-pour-notre-projet)
        
    * [Étape 5 : Comprendre les configurations clés](#heading-etape-5-comprendre-les-configurations-cles)
        
    * [Étape 6 : Créer une configuration de valeurs simplifiée pour le Helm Chart CockroachDB](#heading-etape-6-creer-une-configuration-de-valeurs-simplifiee)
        
    * [Aperçu des valeurs YAML](#heading-apercu-des-valeurs-yaml)
        
    * [🚀 Étape 7 : Installer le cluster CockroachDB avec Helm](#heading-etape-7-installer-le-cluster-cockroachdb-avec-helm)
        
7. [Accéder à la console CockroachDB et visualiser les métriques](#heading-acceder-a-la-console-cockroachdb-et-visualiser-les-metriques)
    
    * [Étape 1 : Localiser le service public CockroachDB](#heading-etape-1-localiser-le-service-public-cockroachdb)
        
    * [Étape 2 : En savoir plus sur le service](#heading-etape-2-en-savoir-plus-sur-le-service)
        
    * [Étape 3 : Accéder au tableau de bord CockroachDB](#heading-etape-3-acceder-au-tableau-de-bord-cockroachdb)
        
    * [Étape 4 : Visiter le tableau de bord](#heading-etape-4-visiter-le-tableau-de-bord)
        
    * [Étape 5 : Explorer le tableau de bord des métriques](#heading-etape-5-explorer-le-tableau-de-bord-des-metriques)
        
    * [Étape 6 : Créer une petite charge sur le cluster CockroachDB](#heading-etape-6-creer-une-petite-charge-sur-le-cluster-cockroachdb)
        
    * [Étape 7 : Visualiser les métriques issues de la charge](#heading-etape-7-visualiser-les-metriques-issues-de-la-charge)
        
    * [Étape 8 : Voir la liste des éléments créés dans la base de données](#heading-etape-8-voir-la-liste-des-elements-crees)
        
8. [Sauvegarde de CockroachDB vers Google Cloud Storage ☁️](#heading-sauvegarde-de-cockroachdb-vers-google-cloud-storage)
    
    * [Pourquoi les sauvegardes sont absolument critiques](#heading-pourquoi-les-sauvegardes-sont-absolument-critiques)
        
    * [Connexion à notre DB – Installation de Beekeeper Studio](#heading-connexion-a-notre-db-installation-de-beekeeper-studio)
        
    * [Comment installer Beekeeper Studio](#heading-comment-installer-beekeeper-studio)
        
    * [Connecter Beekeeper Studio à CockroachDB](#heading-connecter-beekeeper-studio-a-cockroachdb)
        
    * [Exposer le cluster pour un accès local](#heading-exposer-le-cluster-pour-un-acces-local)
        
    * [🐝 Connexion via Beekeeper Studio](#heading-connexion-via-beekeeper-studio)
        
    * [Vérifier la connexion](#heading-verifier-la-connexion)
        
    * [Créer un compte Google Cloud](#heading-creer-un-compte-google-cloud)
        
    * [Créer un bucket Google Cloud Storage](#heading-creer-un-bucket-google-cloud-storage)
        
    * [Donner à CockroachDB l'accès au bucket](#heading-donner-a-cockroachdb-l-acces-au-bucket)
        
    * [Attacher la clé à notre cluster CockroachDB](#heading-attacher-la-cle-a-notre-cluster-cockroachdb)
        
    * [Tester notre sauvegarde — L'heure de la reprise après sinistre](#heading-tester-notre-sauvegarde-reprise-apres-sinistre)
        
9. [Gestion des ressources et optimisation de l'utilisation de la mémoire](#heading-gestion-des-ressources-et-optimisation-de-l-utilisation-de-la-memoire)
    
    * [Comment CockroachDB utilise la mémoire](#heading-comment-cockroachdb-utilise-la-memoire)
        
    * [La formule d'utilisation de la mémoire que vous devez suivre](#heading-la-formule-d-utilisation-de-la-memoire)
        
    * [Où trouver ces paramètres](#heading-ou-trouver-ces-parametres)
        
    * [Exemple concret (étape par étape)](#heading-exemple-concret-etape-par-etape)
        
    * [⚠️ À propos des Requests vs Limits dans Kubernetes](#heading-a-propos-des-requests-vs-limits-dans-kubernetes)
        
    * [Surcharger les fractions par défaut](#heading-surcharger-les-fractions-par-defaut)
        
10. [Mise à l'échelle de CockroachDB de la bonne manière](#heading-mise-a-l-echelle-de-cockroachdb-de-la-bonne-maniere)
    
    * [Métriques clés à comprendre](#heading-metriques-cles-a-comprendre)
        
    * [Quand (et quoi) mettre à l'échelle en fonction de vos métriques](#heading-quand-et-quoi-mettre-a-l-echelle)
        
    * [Situations liées au disque — Que faire quand votre disque est le facteur limitant](#heading-situations-liees-au-disque)
        
    * [Pression mémoire — Que faire quand votre base de données atteint la limite](#heading-pression-memoire)
        
    * [Quand les requêtes sont lentes mais que tout le reste (CPU, Mémoire & Disque) semble « correct »](#heading-quand-les-requetes-sont-lentes)
        
    * [Comprendre la vitesse du disque (IOPS & Débit) selon les fournisseurs Cloud](#heading-comprendre-la-vitesse-du-disque)
        
    * [Réduction de la taille du cluster (Réduction des réplicas)](#heading-reduction-de-la-taille-du-cluster)
        
    * [⚠️ La mauvaise façon de réduire l'échelle](#heading-la-mauvaise-facon-de-reduire-l-echelle)
        
    * [Déclassement d'un nœud avant de réduire la taille du cluster](#heading-declassement-d-un-noeud-avant-de-reduire-la-taille-du-cluster)
        
11. [Ce qu'il faut considérer lors du déploiement de CockroachDB sur Google Kubernetes Engine (GKE) ☁️](#heading-ce-qu-il-faut-considerer-sur-gke)
    
    * [Création de votre cluster GKE](#heading-creation-de-votre-cluster-gke)
        
    * [Connexion à votre cluster GKE](#heading-connexion-a-votre-cluster-gke)
        
    * [Déploiement de CockroachDB en production (sur GKE)](#heading-deploiement-de-cockroachdb-en-production-sur-gke)
        
    * [Comprendre la configuration](#heading-comprendre-la-configuration)
        
    * [Installer le cluster CockroachDB sur GKE](#heading-installer-le-cluster-cockroachdb-sur-gke)
        
    * [Connexion à notre cluster CockroachDB (Maintenant que TLS + mTLS sont activés)](#heading-connexion-a-notre-cluster-cockroachdb-tls-mtls)
        
    * [Connexion via Mutual TLS (mTLS) — Pourquoi nous avons besoin d'un certificat pour notre utilisateur root](#heading-connexion-via-mutual-tls-mtls)
        
    * [Explorons le certificat de notre cluster](#heading-explorons-le-certificat-de-notre-cluster)
        
    * [Comprendre les sections du certificat (Expliqué très simplement)](#heading-comprendre-les-sections-du-certificat)
        
    * [Création d'un certificat client (Pour pouvoir enfin se connecter à CockroachDB)](#heading-creation-d-un-certificat-client)
        
    * [Connexion sécurisée à notre cluster CockroachDB (Utilisation de mTLS)](#heading-connexion-securisee-a-notre-cluster-cockroachdb-mtls)
        
    * [Restauration de notre base de données précédente dans le nouveau cluster GKE (sans clés SA)](#heading-restauration-de-notre-base-de-donnees-precedente)
        
    * [Restauration de notre base de données précédente depuis Google Cloud Storage](#heading-restauration-depuis-google-cloud-storage)
        
    * [Maintenant, restaurons les données 🎉](#heading-maintenant-restaurons-les-donnees)
        
    * [Connexion à la base de données avec un nouvel utilisateur](#heading-connexion-a-la-base-de-donnees-avec-un-nouvel-utilisateur)
        
    * [Connexion avec authentification sans mot de passe (Mutual TLS)](#heading-connexion-avec-authentification-sans-mot-de-pass-mtls)
        
    * [Connexion via Mutual TLS (mTLS) depuis nos applications sur Kubernetes](#heading-connexion-via-mutual-tls-mtls-depuis-nos-apps)
        
12. [Comment obtenir une licence CockroachDB Enterprise GRATUITEMENT !](#heading-comment-obtenir-une-licence-cockroachdb-enterprise-gratuitement)
    
    * [Trois types de licences](#heading-trois-types-de-licences)
        
    * [Comment demander la licence Enterprise gratuite](#heading-comment-demander-la-licence-enterprise-gratuite)
        
    * [Ajout de votre licence au cluster CockroachDB](#heading-ajout-de-votre-licence-au-cluster-cockroachdb)
        
13. [Conclusion et prochaines étapes ✨](#heading-conclusion-et-prochaines-etapes)
    
    * [À propos de l'auteur 👨🏾‍💻](#heading-a-propos-de-l-auteur)
        

## Qu'est-ce que CockroachDB au juste ? 🧐

![Une image résumant ce qu'est CockroachDB](https://cdn.hashnode.com/res/hashnode/image/upload/v1760416037885/c67edcbb-be85-4614-bdf3-104942048eea.jpeg align="center")

Hé ! Avant de nous lancer dans la configuration de notre cluster Kubernetes et le déploiement de notre cluster CockroachDB, posons les bases de ce qu'est réellement CockroachDB. (Parce que si vous ne comprenez pas le pourquoi et le comment, l'implémentation et la session pratique ressembleront juste à de la magie 😅.)

### Définition simple

CockroachDB est une base de données SQL distribuée. Cela signifie qu'elle vous offre les fonctionnalités d'une base de données relationnelle (tables, requêtes SQL, JOINS, transactions) mais copie les données sur plusieurs réplicas (serveurs, nœuds, instances). Pas besoin de sharding manuel. 😃

Elle est conçue pour survivre aux pannes, évoluer facilement (comparée aux autres bases de données SQL) et maintenir la cohérence de vos données quoi qu'il arrive (sur toutes les instances).

### Qui a créé CockroachDB ? Quand a-t-il été lancé ?

CockroachDB a été créé par [**Cockroach Labs**](https://www.cockroachlabs.com/), fondé par Spencer Kimball, Peter Mattis et Ben Darnell. L'idée a commencé à prendre forme vers 2014, et Cockroach Labs a été formellement fondé en 2015.

Sa version 1.0 « prête pour la production » a été annoncée en 2017, marquant sa transition de la version bêta à une utilisation adaptée au monde réel.

### Quels problèmes CockroachDB essaie-t-il de résoudre ?

Les bases de données relationnelles traditionnelles sont excellentes, mais elles rencontrent de réels défis lorsque votre application grandit. CockroachDB a été conçu pour les résoudre. Voici les principaux points de friction et comment CockroachDB y répond :

| Point de friction | Ce qui se passe habituellement | Comment CockroachDB le résout |
| --- | --- | --- |
| **Goulot d'étranglement du primaire unique** | SEUL UN nœud « primaire » gère les écritures, mises à jour et suppressions. Ce nœud peut devenir difficile à mettre à l'échelle sans interruption. | CockroachDB est **multi-primaire**, ce qui signifie que chaque nœud peut accepter des lectures et des écritures. Pas de « primaire » unique pour tout le cluster. |
| **Complexité du sharding manuel** | Vous devez diviser les données (shard) à la main, décider où va chaque morceau et gérer les requêtes inter-shards, un vrai casse-tête 🤢. | CockroachDB partitionne automatiquement les données en petites unités (appelées *ranges*) et les déplace pour équilibrer la charge. |
| **Interruption lors du basculement (failover)** | Si le nœud primaire échoue, vous devez promouvoir un réplica et basculer. Pendant ce temps, votre application peut être hors service. | Comme il n'y a pas de primaire unique, si une instance échoue, les autres prennent le relais de manière transparente (via consensus) sans panne majeure. |
| **Mise à l'échelle géographique et latence** | Servir des utilisateurs dans différentes régions est difficile — soit les données sont loin (lent), soit vous devez construire une logique de réplication complexe. | CockroachDB vous permet de distribuer des nœuds à travers les régions. Vous pouvez servir des lectures/écritures locales tout en gardant une cohérence globale. |

Ainsi, au lieu de lutter contre votre base de données à mesure qu'elle grandit, CockroachDB gère une grande partie du travail difficile pour vous.

### Termes clés à connaître (en langage clair) :

* **Nœud (Node) :** Doublons ou copies de votre base de données. On les appelle aussi réplicas. Ils peuvent être en lecture seule (SELECT uniquement) OU en lecture-écriture (SELECT, INSERT, UPDATE, DELETE).
    
* **Réplication** : Faire des copies de données sur plusieurs nœuds. Si un nœud échoue, les autres ont toujours les données.
    
* **Raft (algorithme de consensus)** : Un système qui garantit que les copies (réplicas) s'accordent sur les changements de manière sûre et fiable. Par exemple, Raft s'assure que la majorité des copies sont d'accord avant qu'une écriture ne soit acceptée.
    
* **Sharding / Ranges** : Au lieu de mettre toutes vos données dans un seul gros bloc, CockroachDB les divise en plus petits morceaux appelés *ranges*. Chaque range est répliqué et peut se déplacer entre les nœuds.
    
* **Transaction distribuée** : Une transaction (série d'opérations) qui peut toucher des données stockées dans différents nœuds. CockroachDB gère cela pour que vous conserviez les propriétés ACID (atomique, cohérent, isolé, durable).
    

### Pourquoi le nom « CockroachDB » ? 😅

Vous vous demandez peut-être : *Pourquoi nommer une base de données d'après un cafard ?* Ça semble bizarre au début, mais il y a une raison :

Les cafards sont connus pour survivre à des conditions extrêmes : radiations, catastrophes naturelles, etc. Les fondateurs voulaient une base de données presque « impossible à tuer », capable de survivre aux pannes de nœuds, aux coupures de courant et aux scissions de réseau. Le nom est un clin d'œil humoristique à la résilience.

## Pourquoi choisir CockroachDB plutôt que PostgreSQL ou MongoDB 🤷🏾‍♂️ ?

Comparons la configuration classique (Postgres / MongoDB) à CockroachDB, en particulier pourquoi vous pourriez vouloir choisir CockroachDB et comment cela facilite la mise à l'échelle.

Dans de nombreuses configurations, avec Postgres ou MongoDB, vous avez souvent un nœud « primaire » qui gère toutes les écritures (inserts, updates, deletes).

Ensuite, vous avez plusieurs « réplicas de lecture » qui copient les données du primaire et servent les requêtes de lecture (selects). Cela fonctionne bien — les lectures peuvent être réparties — mais tout le trafic d'écriture va vers ce seul nœud primaire.

Habituellement, le primaire finit par être stressé lorsque le volume d'écriture augmente (par exemple, plus de clients créent des comptes).

Vous pouvez ajouter plus de réplicas de lecture (mise à l'échelle horizontale pour les lectures), mais mettre à l'échelle le primaire est beaucoup plus difficile.

Pour mettre à l'échelle le primaire, vous devez souvent augmenter ses ressources (CPU, RAM, disque) — c'est la mise à l'échelle verticale — ce qui nécessite souvent une interruption de service (arrêter la DB, augmenter les ressources, puis redémarrer).

Ou alors, vous devriez effectuer un sharding manuel (diviser vos données) sur plusieurs primaires, router le trafic avec soin et gérer la complexité.

### Comment la tolérance aux pannes est gérée dans PostgreSQL et MongoDB

Lorsque vous essayez de rendre Postgres (ou MongoDB) hautement disponible et tolérant aux pannes dans une configuration auto-gérée, vous avez souvent besoin de deux réplicas de lecture ou plus et d'un primaire.

La partie délicate est de gérer ce qui se passe quand le primaire échoue. Vous avez besoin de quelque chose qui peut promouvoir automatiquement un réplica en primaire.

Dans le monde Postgres, c'est souvent géré par [**Patroni**](https://github.com/patroni/patroni) ou [**repmgr**](https://www.repmgr.org/) (des outils qui gèrent la gestion de cluster, le failover, l'élection du leader, etc.).

Dans MongoDB, cette logique fait partie du comportement du **replica set** : il effectue des élections automatiques parmi les réplicas.

Voici quelques-uns des défis principaux de ce modèle classique :

* Chaque écriture doit aller vers un seul primaire. Si ce primaire échoue ou est surchargé, tout votre système en pâtit.
    
* Mettre à l'échelle les lectures est facile (ajouter des réplicas), mais mettre à l'échelle les écritures est difficile.
    
* La mise à l'échelle verticale a ses inconvénients. Si le nœud primaire a besoin de plus de ressources, vous pourriez subir une interruption.
    
* Le sharding manuel est complexe : vous décidez quelle donnée va sur quel shard, gérez les requêtes inter-shards et construisez la logique de routage.
    
* Un service (ou load balancer/proxy) pointe vers le primaire (pour TOUTES les écritures).
    
* Un autre service ou logique de routage gère les lectures et peut les répartir sur les réplicas.
    
* Vous pourriez utiliser **HAProxy**, **pgpool-II** ou **pgBouncer** pour Postgres afin de router le trafic ou gérer le pool de connexions. Ce sont des outils externes que vous devez configurer.
    

Ainsi, quand le primaire échoue, Patroni (ou repmgr, etc.) le détecte et promeut l'un des réplicas de lecture comme nouveau primaire.

Mais cette promotion, reconfiguration et redirection du trafic causent souvent une brève fenêtre d'interruption.

### Comment CockroachDB gère cela différemment

![Un bref aperçu des propriétés de CockroachDB](https://cdn.hashnode.com/res/hashnode/image/upload/v1760416070693/af1ade70-19bb-4e9f-82ec-9711c13d8079.jpeg align="center")

CockroachDB change les règles :

* **Tous les réplicas sont égaux** pour les lectures *et* les écritures. Vous n'avez pas de « primaire » spécial. Chaque nœud du cluster peut accepter des requêtes d'écriture.
    
* CockroachDB divise vos données en petits morceaux (ranges) et les réplique sur les nœuds. Si vous ajoutez un nouveau nœud, les données se déplacent automatiquement pour équilibrer la charge.
    
* Chaque écriture est automatiquement copiée sur d'autres réplicas, et la cohérence est gérée par un protocole (Raft), vous n'avez donc pas à construire cela vous-même.
    
* Pas de sharding manuel nécessaire. Comme la base de données gère la division et le déplacement des données, vous n'avez pas à décider comment sharder à la main.
    
* Vous **n'avez pas besoin d'un service spécial** pour router les écritures vs les lectures. N'importe quel nœud peut accepter les deux.
    
* Lors de la mise à l'échelle, vous n'avez pas à vous soucier de quel nœud est le primaire — car *il n'y a pas de primaire*.
    
* Vous pouvez mettre à l'échelle vos nœuds un par un (style rollout). Lorsqu'un nœud est mis à jour, les autres continuent de servir le trafic. Vous n'aurez pas d'interruption juste parce que vous mettez à l'échelle le « primaire ».
    
* Comme il n'y a pas de logique de promotion de réplica, il n'y a pas de moment où un réplica doit être « élevé » au rang de primaire — ce sont juste des nœuds qui continuent de servir.
    

## Comment CockroachDB fonctionne en coulisses ⚙️

Dans CockroachDB, il y a beaucoup de pièces mobiles en coulisses. Mais elles travaillent ensemble pour que vous n'ayez pas à les surveiller de trop près. Les idées centrales sont :

* Diviser les données en morceaux (**ranges**)
    
* Garder plusieurs copies de chaque morceau (**réplicas/réplication**)
    
* S'assurer que toutes les copies sont d'accord via le **consensus Raft**
    
* Déplacer les morceaux pour équilibrer la charge (**rééquilibrage/distribution automatique**)
    
* Coordonner les transactions qui peuvent toucher de nombreux morceaux
    

Passons-les en revue un par un.

### Ranges : Les petits morceaux de données

![Une petite illustration des ranges CockroachDB](https://cdn.hashnode.com/res/hashnode/image/upload/v1760413105037/984f8b5c-bd53-4850-9704-57ce1dcedb80.png align="center")

Imaginez que vous avez un géant livre de recettes. Si vous essayez de tout porter, c'est lourd. Alors vous divisez le livre en petits livrets, chacun couvrant une gamme de repas : petits-déjeuners, déjeuners, dîners, desserts.

Dans CockroachDB, les données sont divisées en ranges, qui sont comme ces petits livrets :

* Chaque range couvre un certain bloc de données (comme « tous les utilisateurs dont l'ID est 1-1000 »)
    
* Lorsqu'un range devient trop gros, il est coupé/divisé en deux plus petits. Cela rend chaque morceau plus facile à gérer.
    
* Si deux ranges voisins sont devenus très petits, ils peuvent être fusionnés.
    
* Ces divisions et fusions se produisent automatiquement en coulisses.
    

Ce découpage aide le système de plusieurs façons : déplacer les morceaux, les copier, équilibrer la charge et récupérer après une panne de nœud devient plus facile.

### Réplication : Plusieurs copies pour la sécurité

![Réplication des Ranges sur plusieurs Nœuds dans CockroachDB](https://cdn.hashnode.com/res/hashnode/image/upload/v1760413678362/a0066780-1360-4511-8fd0-466f54ea2135.jpeg align="center")

Personne n'aime perdre son travail, alors vous gardez des copies de sauvegarde. CockroachDB fait de même pour les données.

Pour chaque range, il y a généralement 3 copies (réplicas) stockées sur différentes machines (nœuds). Si une machine meurt, vous avez toujours les autres. Et ces copies sont toujours synchronisées : quand vous écrivez quelque chose, le changement est propagé aux autres copies.

La base de données tolère également les pannes. Si un nœud tombe, le système le détecte et finit par créer une nouvelle copie ailleurs pour le remplacer. Cela vous donne une tolérance aux pannes : vos données restent en sécurité même quand des parties de votre système échouent.

### Consensus Raft : Comment toutes les copies s'accordent

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1760415307117/79859a4b-4341-46eb-91d9-cccc3bde9a66.jpeg align="center")

Avoir des copies est utile, mais vous avez aussi besoin qu'elles soient d'accord entre elles. Le protocole Raft est un moyen de s'assurer que cela se produit de manière fiable.

Voici comment Raft fonctionne en termes simples :

* Chaque range a un groupe de réplicas. L'un d'eux agit comme le **leader**. Les autres sont des **followers**.
    
* Toutes les requêtes d'écriture pour ce range passent par le leader. Le leader reçoit la requête, puis dit aux followers d'enregistrer le même changement.
    
* Une fois que la majorité des copies disent « ok, on l'a », le changement est considéré comme final (committed). Ensuite, le leader répond au client : « Terminé ».
    
* Si le leader s'arrête de fonctionner, les followers le remarquent et organisent une élection pour choisir un nouveau leader.
    

Ainsi, Raft est le protocole d'accord qui maintient toutes les copies synchronisées et sûres.

### MultiRaft : Maintenir l'efficacité de Raft lors de la mise à l'échelle

Lorsque vous avez de nombreux ranges, chacun a son propre groupe Raft. Cela peut signifier beaucoup de messages « es-tu vivant ? » entre les nœuds. MultiRaft est l'astuce utilisée par CockroachDB pour rendre cela efficace.

MultiRaft regroupe le travail Raft pour de nombreux ranges qui partagent des nœuds, réduisant ainsi la surcharge réseau et le gaspillage de ressources.

### Rééquilibrage : Le mouvement pour l'équilibre

Lorsque vos ranges ne sont pas répartis uniformément sur les nœuds, certaines machines travaillent trop et d'autres presque pas. CockroachDB déplace automatiquement les morceaux pour équilibrer les choses.

* Le système surveille l'activité de chaque nœud.
    
* Si un nœud est surchargé, il déplacera certains ranges vers d'autres nœuds.
    
* Si un nœud meurt, le système s'assure que les ranges qui s'y trouvaient sont copiés ailleurs.
    
* Si vous ajoutez un nouveau nœud, le système commence à y déplacer des ranges pour utiliser ses ressources.
    

Cela se produit sans que vous ayez à décider manuellement quoi déplacer où.

### Transactions distribuées : Travailler sur plusieurs Ranges

Souvent, une opération touche plusieurs ranges. Par exemple, « transférer de l'argent du compte A (range 1) au compte B (range 2) ». Cela doit être géré avec soin pour que soit les deux parties réussissent, soit aucune.

CockroachDB prend en charge les **transactions distribuées**, garantissant les propriétés ACID même dans une configuration distribuée. Le système assure un comportement atomique : tout ou rien.

### Flux de lecture + écriture (Ce qui se passe quand vous l'utilisez)

Imaginons une écriture, étape par étape :

1. Votre application envoie une écriture à n'importe quel nœud du cluster CockroachDB.
2. Ce nœud identifie quel(s) range(s) sont impliqués.
3. Pour chaque range, l'écriture va au leader de ce range.
4. Le leader écrit le changement sur sa propre copie, puis demande aux followers de faire de même.
5. Une fois que la majorité confirme, le leader déclare l'écriture « validée » et répond à votre application.

Flux de lecture :

* Votre application envoie une lecture à n'importe quel nœud.
* Ce nœud vérifie ses copies. S'il a une copie fraîche, il répond. Sinon, il demande au nœud qui l'a.

### Pourquoi tout cela est important

Tous ces ajustements sont importants car, comme les données sont découpées en ranges et répliquées, aucun nœud unique n'est un goulot d'étranglement. De plus, Raft garantit le consensus, vous pouvez donc être sûr que les données sont cohérentes sur tous les réplicas fonctionnels.

## Où (et comment) devriez-vous héberger CockroachDB ? ☁️

Il n'y a pas qu'une seule « bonne » façon d'héberger CockroachDB. Votre choix dépend du coût, du contrôle, de la facilité d'utilisation et de votre tolérance au risque.

### Option 1 : CockroachDB Cloud (entièrement managé par Cockroach Labs)

C'est l'option la plus simple si vous voulez déléguer les opérations. Vous ne gérez pas les nœuds, les mises à jour ou les sauvegardes.

**Ce qu'il offre :**
* Inscription et clic sur « créer un cluster ».
* Mise à l'échelle automatique, mises à jour sans interruption et sauvegardes managées.
* Supporte plusieurs fournisseurs cloud.

**Compromis :**
* Moins de contrôle sur l'infrastructure sous-jacente.
* Vous payez un supplément pour le service managé.

### Option 2 : Bring Your Own Cloud (BYOC)

Un juste milieu : vous gardez votre environnement cloud, mais laissez Cockroach Labs gérer la base de données à l'intérieur de *votre* compte cloud.

### Option 3 : Utiliser les Marketplaces Cloud (AWS, GCP, Azure)

Si vous utilisez déjà un fournisseur cloud, le déploiement via leur marketplace peut être le plus simple pour la facturation et l'intégration.

### Option 4 (Ma préférée 😁) : Auto-hébergement — Surtout avec Kubernetes

Si vous auto-hébergez CockroachDB, vous avez le **contrôle total**. Vous êtes le patron de tout : machines, stockage, réseau, sauvegardes, etc.

L'utilisation de Kubernetes signifie que votre configuration n'est pas liée à un seul fournisseur cloud. Kubernetes offre une couche d'infrastructure portable.

#### Pourquoi Kubernetes bat des outils comme Docker Swarm ou Hashicorp Nomad pour les bases de données

Comme CockroachDB est un système **stateful** (avec état), vous avez besoin d'un support solide pour les données persistantes. Kubernetes est conçu avec de bonnes primitives pour cela.

* **StatefulSets :** Garantit que chaque réplica CockroachDB conserve son identité et son stockage même s'il redémarre.
* **Persistent Volumes :** Même si un pod se déplace ou crash, le disque (données) reste.
* **StorageClasses :** Vous pouvez choisir votre type de disque (HDD, SSD équilibré, SSD rapide).
* **Mises à jour roulantes et anti-affinité :** Permet de mettre à jour un réplica à la fois sans interruption. L'anti-affinité empêche de mettre deux réplicas sur la même machine physique.

## Configuration de votre environnement local 🧑🏾‍💻

Avant de déployer CockroachDB, nous avons besoin d'un « terrain de jeu » sécurisé.

### Pourquoi ces outils ?

* **Minikube** : Un outil qui fait tourner un petit cluster Kubernetes sur votre ordinateur.
* **Kubectl** : L'outil en ligne de commande pour parler à votre cluster.
* **Helm** : Le gestionnaire de paquets pour Kubernetes.

### Étape 1 : Installer Minikube

#### 🪟 Windows
```bash
choco install minikube
```
ou
```bash
winget install minikube
```

#### 🍎 macOS
```bash
brew install minikube
minikube start
```

#### 🐧 Linux
```bash
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
rm minikube-linux-amd64
minikube start
```

### Étape 2 : Installer kubectl

#### 🪟 Windows
```bash
choco install kubernetes-cli
```

#### 🍎 macOS
```bash
brew install kubectl
```

#### 🐧 Linux
```bash
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl
```

### Étape 3 : Installer Helm

#### 🪟 Windows
```bash
choco install kubernetes-helm
```

#### 🍎 macOS
```bash
brew install helm
```

#### 🐧 Linux
```bash
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh
```

## Déploiement de CockroachDB sur Minikube

### Étape 1 : Visiter ArtifactHub
Allez sur [https://artifacthub.io](https://artifacthub.io) et cherchez **CockroachDB**.

### Étape 2 : Explorer le Helm Chart
Regardez le README et les valeurs par défaut.

### Étape 3 : Copier les valeurs par défaut
Cliquez sur le bouton **Default Values** et copiez le contenu YAML.

### Étape 4 : Créer un dossier pour notre projet
```bash
mkdir cockroachdb-tutorial
cd cockroachdb-tutorial
nano cockroachdb-original-values.yml
# Collez le contenu et sauvegardez
```

### Étape 5 : Comprendre les configurations clés
* `statefulset.replicas` : Nombre de nœuds (3 par défaut).
* `resources.requests/limits` : CPU et mémoire alloués.
* `storage.persistentVolume.size` : Taille du disque par nœud.

### Étape 6 : Créer une configuration de valeurs simplifiée
Créez `cockroachdb-values.yml` :

```yaml
statefulset:
  replicas: 3
  podSecurityContext:
    fsGroup: 1000
    runAsUser: 1000
    runAsGroup: 1000
  resources:
    requests:
      memory: "1Gi"
      cpu: 1
    limits:
      memory: "1Gi"
      cpu: 1
  podAntiAffinity:
    type: ""
  nodeSelector:
    kubernetes.io/hostname: minikube

storage:
  persistentVolume:
    size: 5Gi
    storageClass: standard

tls:
  enabled: false

init:
  jobs:
    wait:
      enabled: true
```

### 🚀 Étape 7 : Installer le cluster CockroachDB avec Helm

```bash
helm install crdb cockroachdb/cockroachdb -f cockroachdb-values.yml
```

Vérifiez les pods :
```bash
kubectl get pods | grep -i crdb
```

## Accéder à la console CockroachDB et visualiser les métriques

### Étape 1 : Localiser le service public
```bash
kubectl get svc | grep -i crdb
```

### Étape 3 : Accéder au tableau de bord
```bash
kubectl port-forward svc/crdb-cockroachdb-public 8080:8080
```
Allez sur [http://localhost:8080](http://localhost:8080).

### Étape 6 : Créer une petite charge sur le cluster
Nous allons utiliser un script Python pour simuler une activité.

#### Étape 6.1 : Créer un ConfigMap pour les données
Créez `books.json` avec une liste de livres, puis :
```bash
kubectl create configmap books-json --from-file=books.json
```

#### Étape 6.2 : Créer le ConfigMap du script Python
Appliquez le fichier `books-script.yml` contenant le code Python de manipulation de données.

#### Étape 6.3 : Créer le Job pour exécuter le script
Appliquez `books-job.yml` pour lancer le container qui exécutera les requêtes SQL.

## Sauvegarde de CockroachDB vers Google Cloud Storage ☁️

### Pourquoi les sauvegardes sont absolument critiques
Les erreurs arrivent. Une sauvegarde quotidienne vers un bucket Google Cloud Storage vous permet de restaurer votre cluster en cas de sinistre.

### Connexion via Beekeeper Studio
1. Installez Beekeeper Studio.
2. Exposez le port de la DB :
```bash
kubectl port-forward svc/crdb-cockroachdb-public 26257
```
3. Connectez-vous à `localhost:26257` avec l'utilisateur `root`.

### Créer un bucket Google Cloud Storage
Créez un bucket unique dans votre console Google Cloud.

### Donner à CockroachDB l'accès au bucket
Créez un **Service Account** avec les rôles :
* Storage Object Creator
* Storage Object Viewer
* Storage Object User

Téléchargez la clé JSON.

### Attacher la clé à notre cluster CockroachDB
1. Créez un secret Kubernetes :
```bash
kubectl create secret generic gcs-key --from-file=key.json=<PATH_TO_KEY>
```
2. Mettez à jour `cockroachdb-values.yml` pour monter ce secret et définir `GOOGLE_APPLICATION_CREDENTIALS`.

### Création du planning de sauvegarde
Dans la console SQL :
```sql
CREATE SCHEDULE backup_cluster
FOR BACKUP INTO 'gs://<BUCKET_NAME>/cluster?AUTH=implicit'
WITH revision_history
RECURRING '@hourly'
FULL BACKUP '@daily'
WITH SCHEDULE OPTIONS first_run = 'now';
```

## Gestion des ressources et optimisation de l'utilisation de la mémoire

### La formule d'utilisation de la mémoire
```yaml
(2 × max-sql-memory) + cache ≤ 80% de la limite de mémoire du pod
```
Il est crucial de laisser environ 20% de mémoire libre pour les processus internes de CockroachDB.

## Mise à l'échelle de CockroachDB de la bonne manière

### Métriques clés à comprendre
* **IOPS** : Nombre d'opérations d'entrée/sortie par seconde.
* **Débit (Throughput)** : Volume de données transférées par seconde.
* **Latence SQL p99** : Temps de réponse pour les 1% de requêtes les plus lentes.

### Déclassement d'un nœud avant de réduire la taille du cluster
Ne réduisez pas simplement le nombre de réplicas. Vous devez d'abord **déclasser (decommission)** le nœud via la CLI Cockroach pour que les données soient déplacées en toute sécurité vers les nœuds restants.

## Ce qu'il faut considérer sur GKE ☁️

En production sur GKE, utilisez :
* **Workload Identity** au lieu de clés JSON statiques.
* **SSD Premium (premium-rwo)** pour de meilleures performances.
* **TLS/mTLS** activé pour sécuriser toutes les communications.

### Connexion via Mutual TLS (mTLS)
En mode sécurisé, CockroachDB exige que le client présente un certificat signé par la même Autorité de Certification (CA) que le cluster.

Utilisez **cert-manager** pour gérer automatiquement la création et le renouvellement de ces certificats.

## Comment obtenir une licence CockroachDB Enterprise GRATUITEMENT !

Si votre entreprise génère moins de 10 millions de dollars de revenus annuels, vous pouvez demander une licence **Enterprise Free**. Elle débloque toutes les fonctionnalités avancées sans frais, à condition d'activer la télémétrie.

## Conclusion et prochaines étapes ✨

Félicitations ! Vous avez parcouru tout le chemin, de la compréhension théorique au déploiement d'un cluster CockroachDB sécurisé, résilient et prêt pour la production sur Kubernetes. Vous maîtrisez maintenant la réplication, les sauvegardes cloud, la sécurité mTLS et la gestion des ressources.

### À propos de l'auteur 👨🏾‍💻

Salut, je suis Prince ! Je suis ingénieur DevOps et architecte Cloud, passionné par la construction et la gestion d'applications modernes. Retrouvez-moi sur [LinkedIn](https://www.linkedin.com/in/prince-onukwili-a82143233/) ou [Twitter (X)](https://x.com/POnukwili). Merci de m'avoir lu !