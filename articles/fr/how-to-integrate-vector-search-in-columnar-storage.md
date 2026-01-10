---
title: Comment intégrer la recherche vectorielle dans le stockage colonnaire
subtitle: ''
author: Chirag Agrawal
co_authors: []
series: null
date: '2025-11-12T21:43:04.153Z'
originalURL: https://freecodecamp.org/news/how-to-integrate-vector-search-in-columnar-storage
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1762983768101/928331bd-3f97-4d05-92fb-2d8ea9af5dab.png
tags:
- name: vector database
  slug: vector-database
- name: semantic search
  slug: semantic-search
- name: Columnar Database
  slug: columnar-database
- name: google cloud
  slug: google-cloud
seo_title: Comment intégrer la recherche vectorielle dans le stockage colonnaire
seo_desc: Integrating vector search into traditional data platforms is becoming a
  common task in the current AI-driven landscape. When Google announced general availability
  for vector search in BigQuery in early 2024, it joined a growing list of established
  da...
---

L'intégration de la recherche vectorielle dans les plateformes de données traditionnelles devient une tâche courante dans le paysage actuel axé sur l'IA. Lorsque Google a annoncé la disponibilité générale (GA) de la recherche vectorielle dans BigQuery au début de l'année 2024, il a rejoint une liste croissante de bases de données établies ayant ajouté des capacités de recherche de similitude sur des embeddings de haute dimension.

Mais si vous examinez de plus près l'implémentation de BigQuery, vous découvrirez une approche qui va au-delà d'un simple ajout de fonctionnalité. Au lieu de greffer une bibliothèque vectorielle, Google a profondément intégré la recherche vectorielle dans son architecture distribuée et colonnaire existante.

Dans cet article, nous allons plonger techniquement dans les décisions d'ingénierie qui sous-tendent la recherche vectorielle de BigQuery. Nous explorerons comment les technologies fondamentales de Google telles que Dremel, Borg et Colossus, combinées à un format colonnaire propriétaire et à un nouvel algorithme d'indexation, créent une plateforme hautement évolutive et efficace pour les charges de travail d'IA.

Cette analyse vous donnera un aperçu des compromis architecturaux impliqués dans la construction d'une recherche vectorielle à grande échelle. Elle démontre également comment vous pouvez adapter un système conçu pour l'analyse à grande échelle afin qu'il excelle dans les tâches d'IA modernes.

## Table des matières

* [Prérequis](#heading-prerequis)
    
* [Le défi unique de la recherche vectorielle](#heading-le-defi-unique-de-la-recherche-vectorielle)
    
* [L'architecture distribuée fondamentale de BigQuery](#heading-larchitecture-distribuee-fondamentale-de-bigquery)
    
    * [Dremel : le moteur de requête distribué](#heading-dremel-le-moteur-de-requete-distribue)
        
    * [Borg : gestion de cluster et orchestration des ressources](#heading-borg-gestion-de-cluster-et-orchestration-des-ressources)
        
    * [Colossus : la couche de stockage distribuée](#heading-colossus-la-couche-de-stockage-distribuee)
        
    * [Jupiter : la structure réseau à haute vitesse](#heading-jupiter-la-structure-reseau-a-haute-vitesse)
        
* [Le rôle du stockage colonnaire dans les opérations vectorielles](#heading-le-role-du-stockage-colonnaire-dans-les-operations-vectorielles)
    
    * [Accélérer les calculs avec SIMD](#heading-accelerer-les-calculs-avec-simd)
        
* [L'algorithme d'indexation TreeAH](#heading-lalgorithme-dindexation-treeah)
    
    * [1\. Structure arborescente hiérarchique](#heading-1-structure-arborescente-hierarchique)
        
    * [2\. Quantification de produit (PQ)](#heading-2-quantification-de-produit-pq)
        
    * [3\. Hachage asymétrique](#heading-3-hachage-asymetrique)
        
    * [Comparaison architecturale : TreeAH vs. HNSW](#heading-comparaison-architecturale-treeah-vs-hnsw)
        
* [Le flux de requête de recherche vectorielle de bout en bout](#heading-le-flux-de-requete-de-recherche-vectorielle-de-bout-en-bout)
    
* [Implications pratiques pour les équipes d'ingénierie](#heading-implications-pratiques-pour-les-equipes-dingenierie)
    
    * [1\. Latence de requête vs débit](#heading-1-latence-de-requete-vs-debit)
        
    * [2\. Considérations sur le modèle de coût](#heading-2-considerations-sur-le-modele-de-cout)
        
    * [3\. Compromis sur la gestion des index](#heading-3-compromis-sur-la-gestion-des-index)
        
    * [4\. Avantages de l'intégration qui comptent vraiment](#heading-4-avantages-de-lintegration-qui-comptent-vraiment)
        
* [Conclusion](#heading-conclusion)
    
* [Lectures complémentaires](#heading-lectures-complementaires)
    

## Prérequis

Cet article suppose que vous possédez des bases solides en systèmes distribués et en mécanismes internes des bases de données, notamment une familiarité avec des concepts tels que le stockage colonnaire, les plans d'exécution de requêtes et le traitement de requêtes distribuées.

You devriez comprendre les bases des embeddings vectoriels et de la recherche de similitude, bien que nous passerons brièvement en revue les fondamentaux. Une expérience avec au moins une base de données vectorielle ou un système de recherche (tel que pgvector, Pinecone ou Elasticsearch) aidera à contextualiser les comparaisons architecturales.

Bien qu'une connaissance approfondie de Google Cloud Platform ne soit pas requise, une familiarité de base avec les entrepôts de données cloud et leurs architectures typiques sera bénéfique. L'article comprend des discussions sur les opérations SIMD et les optimisations au niveau du processeur, donc une aisance avec les considérations de performance de bas niveau est utile, bien que non obligatoire.

Les exemples de code supposent une connaissance pratique du SQL, certaines sections faisant référence à des détails d'implémentation dans des langages comme Python ou Java. Plus important encore, vous devriez avoir de l'expérience dans la construction ou l'exploitation de systèmes de données de production à grande échelle, car de nombreux points de vue se concentrent sur les compromis pratiques d'ingénierie plutôt que sur des concepts théoriques.

## Le défi unique de la recherche vectorielle

La recherche vectorielle diffère fondamentalement des opérations de base de données traditionnelles d'une manière qui remet en question nos hypothèses d'infrastructure existantes. Là où les requêtes conventionnelles tirent parti de décennies d'optimisation autour de la correspondance exacte et des balayages de plages (range scans), la recherche de similitude vectorielle nécessite de calculer des distances entre des points de haute dimension à une échelle massive.

Considérez les chiffres. Les modèles d'embeddings modernes produisent des vecteurs de 768 dimensions ou plus. À raison de 4 octets par valeur float32, un seul embedding consomme environ 3 Ko. Un corpus modeste de 100 millions d'éléments se traduit par 300 Go de données vectorielles.

Mais le véritable défi n'est pas le stockage. Le point critique est le calcul. Trouver les plus proches voisins d'un vecteur de requête signifie calculer des métriques de distance à travers toutes ces dimensions. Pour 100 millions de vecteurs, une recherche par force brute nécessite 76,8 milliards d'opérations en virgule flottante par requête, rien que pour les calculs de distance. Même avec les instructions SIMD modernes traitant 16 flottants à la fois, on parle de milliards de cycles CPU par recherche.

Cette réalité computationnelle impose un compromis fondamental : nous abandonnons les solutions exactes pour des solutions approximatives. Les algorithmes de recherche des plus proches voisins approximatifs (ANN) troquent une précision parfaite contre des temps de requête pratiques. Ils fonctionnent en partitionnant intelligemment l'espace vectoriel, en construisant des graphes de plus proches voisins ou en utilisant des schémas de hachage pour éviter d'examiner chaque vecteur. Le défi d'ingénierie devient alors d'équilibrer la latence des requêtes, la précision du rappel et la consommation de ressources.

La plupart des bases de données vectorielles spécialisées répondent à ce problème par des index en mémoire spécialisés comme HNSW ou IVF. Ceux-ci fonctionnent bien pour des requêtes uniques mais nécessitent de conserver des index massifs en RAM. Si vous n'êtes pas familier avec ces index vectoriels, vous pouvez lire [cet article](https://medium.com/towards-artificial-intelligence/unlocking-the-power-of-efficient-vector-search-in-rag-applications-c2e3a0c551d5).

BigQuery a pris une voie différente. Plutôt que d'optimiser pour la latence d'une requête unique, ils se sont demandé à quoi ressemblerait la recherche vectorielle si elle était conçue pour des charges de travail analytiques à l'échelle d'un entrepôt de données. La réponse a nécessité de repenser les hypothèses de base sur la conception des index, la disposition du stockage et l'exécution des requêtes.

## L'architecture distribuée fondamentale de BigQuery

La recherche vectorielle de BigQuery fonctionne sur la même infrastructure qui traite les requêtes SQL depuis 2011. Pas de nouveau type de cluster. Pas de nœuds vectoriels spécialisés. Juste quatre technologies de base qui alimentent la majeure partie du traitement de données de Google, gérant désormais une charge de travail pour laquelle elles n'avaient pas été conçues à l'origine.

Ce n'est pas le choix le plus évident. La plupart des vector databases construisent une infrastructure spécialisée optimisée pour la recherche de similitude. Les index basés sur des graphes ont besoin d'un accès aléatoire rapide. Les systèmes en mémoire nécessitent une gestion rigoureuse de la mémoire. BigQuery a pris son moteur SQL distribué existant et s'est demandé : pouvons-nous faire fonctionner cela aussi pour les vecteurs ?

La réponse a nécessité de tirer parti de quatre systèmes fondamentaux de nouvelles manières :

* Dremel, le moteur de requête qui gère normalement le SQL, orchestre désormais les calculs de similitude vectorielle.
    
* Borg, qui alloue les ressources pour tout, de Search à YouTube, assigne dynamiquement des milliers de workers aux requêtes vectorielles.
    
* Colossus stocke les embeddings dans le même système de fichiers distribué qui contient des pétaoctets de données analytiques.
    
* Et le réseau de datacenter Jupiter, conçu pour le traitement de données en masse, fait désormais la navette pour les données vectorielles entre les nœuds de calcul.
    

Ce qui est surprenant, ce n'est pas que cela fonctionne, mais à quel point cela fonctionne bien. La même architecture qui exécute des requêtes d'agrégation sur des tables de mille milliards de lignes peut effectuer des recherches dans des collections de vecteurs à l'échelle du milliard. Comprendre comment nécessite d'examiner chaque composant et comment ils ont été adaptés à cette nouvelle charge de travail.

### Dremel : le moteur de requête distribué

À la base, BigQuery est propulsé par Dremel, un moteur d'exécution de requêtes distribué développé chez Google depuis 2006.

Dremel traite les requêtes SQL à l'aide d'un arbre de service hiérarchique. Un serveur racine reçoit la requête et orchestre l'exécution, tandis que des nœuds mélangeurs (mixers) décomposent le travail et le distribuent à des centaines ou des milliers de nœuds feuilles (leaf nodes). Ces nœuds feuilles effectuent les calculs réels en parallèle sur des segments de données.

Cette architecture permet à BigQuery d'allouer dynamiquement un nombre massif de threads d'exécution, appelés slots, à une seule requête, lui permettant de traiter des pétaoctets de données en quelques secondes.

### Borg : gestion de cluster et orchestration des ressources

La nature serverless de BigQuery est rendue possible par Borg, le système de gestion de cluster de Google qui a précédé et inspiré Kubernetes.

Lorsqu'une requête de recherche vectorielle est soumise, Borg est responsable de trouver des machines disponibles dans les centres de données mondiaux de Google, d'allouer la quantité précise de ressources CPU et mémoire nécessaires pour les slots Dremel de la requête, et de gérer la tolérance aux pannes en replanifiant automatiquement le travail si une machine tombe en panne. Cette allocation dynamique de ressources signifie que les utilisateurs n'ont pas besoin de provisionner ou de mettre à l'échelle l'infrastructure, qu'ils recherchent 1 000 vecteurs ou 10 milliards.

### Colossus : la couche de stockage distribuée

Les données dans BigQuery sont stockées dans Colossus, le système de fichiers distribué de nouvelle génération de Google. Colossus est conçu pour un stockage à l'échelle de l'exaoctet, offre une haute disponibilité grâce à la réplication automatique entre datacenters, et est optimisé pour les lectures parallèles à haut débit requises par les nœuds feuilles de Dremel.

Lors d'une recherche vectorielle, Colossus peut fournir des données à des milliers de nœuds simultanément sans créer de goulot d'étranglement au niveau du stockage.

### Jupiter : la structure réseau à haute vitesse

Ces systèmes de calcul et de stockage sont interconnectés par Jupiter, le réseau interne de datacenter de Google, qui présente une bande passante de bissection de l'ordre du pétabit par seconde. La conception du réseau garantit que les données peuvent circuler entre le stockage Colossus et les nœuds de calcul Dremel à des vitesses extrêmement élevées, ce qui rend efficaces les phases de brassage (shuffling) et d'agrégation des données d'une requête.

![L'architecture de recherche vectorielle de Big Query est alimentée par le moteur de requête Dremel, l'orchestrateur Borg pour l'allocation des ressources, Colossus pour le stockage de données à grande échelle et le réseau Jupiter pour le transfert de données à ultra-haute bande passante](https://cdn.hashnode.com/res/hashnode/image/upload/v1715164800000/8f8f8f8f-8f8f-8f8f-8f8f-8f8f8f8f8f8f.png)

## Le rôle du stockage colonnaire dans les opérations vectorielles

Stocker des vecteurs dans des colonnes semble contre-intuitif. Les vecteurs sont des tableaux. Ils vont ensemble. Pourquoi les diviser dans un stockage colonnaire ?

BigQuery le fait quand même, et cela fonctionne brillamment. Voici pourquoi.

Lorsque vous recherchez un million de vecteurs, vous avez besoin d'exactement une chose de chaque ligne : l'embedding. Pas le nom du produit, le prix ou la catégorie. Juste le vecteur. Le stockage orienté ligne vous oblige à lire des enregistrements entiers et à jeter 90 % des données. Le stockage colonnaire ne lit que ce dont vous avez besoin.

L'impact sur les performances est dramatique. Une table avec des embeddings de 768 dimensions plus 20 autres colonnes pourrait totaliser 3 To. Lire uniquement la colonne d'embedding ? 300 Go. C'est une **réduction de 10x des E/S** avant même d'avoir effectué le moindre calcul.

Mais la vraie magie opère au niveau du CPU. Le stockage colonnaire aligne naturellement les données vectorielles pour le traitement SIMD. Au lieu de sauter d'un emplacement mémoire à l'autre pour rassembler les composants vectoriels, le CPU les trouve disposés séquentiellement, prêts pour des opérations en masse. Les processeurs modernes peuvent charger 16 valeurs en virgule flottante dans un seul registre et les traiter simultanément.

La compression devient presque triviale également. Le format Capacitor de BigQuery applique des techniques comme la Quantification de Produit directement aux données de la colonne, réduisant les vecteurs de 3 Ko à moins de 300 octets. Essayez de faire cela avec un stockage orienté ligne où les vecteurs sont dispersés sur plusieurs pages.

La leçon ? Parfois, la "mauvaise" abstraction à un niveau permet les bonnes optimisations à un autre.

### Accélérer les calculs avec SIMD

Les instructions SIMD sont une forme de parallélisme au niveau matériel disponible dans les processeurs modernes qui permettent d'accélérer considérablement l'arithmétique vectorielle. Ceci est réalisé grâce à des jeux d'instructions spéciaux intégrés au processeur.

Par exemple, AVX-512 (Advanced Vector Extensions 512-bit) est un jeu d'instructions présent dans les processeurs haute performance modernes, tels que ceux d'Intel, qui permet à une seule instruction d'opérer sur 512 bits de données à la fois.

Comme un nombre standard en virgule flottante simple précision fait 32 bits, un CPU doté de l'AVX-512 peut traiter 16 nombres en virgule flottante en une seule opération. Cela conduit à des gains de performance spectaculaires.

La différence entre le traitement scalaire et SIMD pour les calculs de distance vectorielle est frappante :

* **Approche scalaire** : Boucler sur chaque dimension, multiplier les composants correspondants, accumuler les résultats. Pour 768 dimensions, cela représente 768 multiplications, 768 additions et des performances de cache médiocres car vous sautez entre deux emplacements mémoire différents à chaque itération.
    
* **Approche SIMD** : Charger 16 composants de chaque vecteur dans des registres de 512 bits. Exécuter une seule instruction de multiplication qui gère les 16 paires. Exécuter une seule addition horizontale. Répéter 48 fois. Le pipeline du CPU reste plein, le préchargeur de cache sait exactement de quelles données vous avez besoin ensuite, et vous avez transformé 1 536 opérations en 96.
    

Le stockage colonnaire porte ses fruits ici aussi. Les vecteurs stockés de manière contiguë en mémoire s'alignent parfaitement avec les chargements de registres SIMD. Pas d'opérations de regroupement (gather), pas de cycles perdus. Juste du débit pur.

![Les opérations TreeAH SIMD In-Register accélèrent les calculs de distance à l'aide d'une table de distance pré-calculée et d'opérations parallèles](https://cdn.hashnode.com/res/hashnode/image/upload/v1715164800000/9f9f9f9f-9f9f-9f9f-9f9f-9f9f9f9f9f9f.png)

Le moteur de requête de BigQuery est conçu pour exploiter intensivement le SIMD. Il détecte et utilise automatiquement le jeu d'instructions optimal disponible sur le matériel sous-jacent (par exemple, AVX-512 pour Intel, NEON pour ARM). Le format de stockage colonnaire garantit que les données vectorielles sont disposées en mémoire d'une manière adaptée aux registres SIMD, et le moteur traite les vecteurs de requête par grands lots pour maximiser l'utilisation de ces instructions parallèles.

## L'algorithme d'indexation TreeAH

Bien que la recherche par force brute puisse être efficace à petite échelle grâce au parallélisme massif de BigQuery, une recherche efficace sur des milliards de vecteurs nécessite un index. L'index vectoriel principal de BigQuery est TreeAH (Tree with Asymmetric Hashing), basé sur l'algorithme open-source ScaNN (Scalable Nearest Neighbors) de Google. TreeAH combine trois techniques pour obtenir des performances élevées et une efficacité mémoire.

### 1\. Structure arborescente hiérarchique

L'algorithme partitionne d'abord l'ensemble de l'espace vectoriel en milliers de listes plus petites. Vous pouvez voir cela comme l'organisation d'une bibliothèque massive. Au lieu d'avoir une seule pièce géante avec un million de livres, une bibliothèque a des étages, des sections et des étagères. Cette hiérarchie permet de trouver un livre sans les scanner tous un par un.

De même, TreeAH regroupe les vecteurs sémantiquement similaires dans des partitions et les organise dans un arbre. Lors d'une requête, la recherche parcourt cet arbre en comparant le vecteur de requête à des vecteurs "centroïdes" qui représentent le centre de chaque partition, suivant ainsi un chemin vers les partitions les plus pertinentes et éliminant les larges branches non pertinentes de l'espace de recherche.

### 2\. Quantification de produit (PQ)

Au sein de TreeAH, la PQ sert un objectif différent de la simple compression. L'index ne se contente pas de stocker des vecteurs plus petits – il modifie fondamentalement le fonctionnement des calculs de distance.

TreeAH apprend des livres de codes (codebooks) spécifiques à chaque partition qui capturent la structure locale des vecteurs dans chaque nœud de l'arbre. Cela signifie que les vecteurs qui se retrouvent dans la partition "chaussures" sont quantifiés différemment de ceux de la partition "électronique". La compression devient sensible à la sémantique.

Combiné à la structure arborescente, cela crée un effet puissant : non seulement vous recherchez moins de vecteurs (grâce à l'arbre), mais vous calculez les distances plus rapidement sur les vecteurs que vous recherchez (grâce à la PQ).

### 3\. Hachage asymétrique

L'aspect "asymétrique" fait référence au fait que le vecteur de requête est conservé dans sa forme de pleine précision, tandis que les vecteurs de la base de données sont comparés sous leur forme compressée et quantifiée.

Les vecteurs ne sont pas de dimensions différentes, mais de précisions différentes. La correspondance sémantique fonctionne parce que la comparaison n'est pas directe. Le vecteur compressé de la base de données est un code qui pointe vers une région de l'espace vectoriel d'origine. Le calcul de distance utilise le vecteur de requête en pleine précision pour rechercher une distance pré-calculée par rapport au centre de cette région. De cette façon, les informations riches du vecteur de requête sont utilisées pour estimer avec précision la distance, évitant ainsi la perte d'informations significative qui se produirait si les deux vecteurs étaient compressés.

### Comparaison architecturale : TreeAH vs. HNSW

Pour mieux comprendre la philosophie de conception de TreeAH, il est utile de le comparer à HNSW (Hierarchical Navigable Small World), un algorithme basé sur les graphes très populaire utilisé dans de nombreuses bases de données vectorielles dédiées.

HNSW construit un graphe multicouche où les vecteurs sont des nœuds et les arêtes les relient à leurs plus proches voisins. Il est réputé pour son excellente latence sur les requêtes uniques.

Mais cette performance s'accompagne d'une surcharge mémoire importante, car la structure du graphe doit être stockée en plus des vecteurs en pleine précision. La construction des index HNSW peut également être chronophage, et les mises à jour fréquentes des données peuvent entraîner une fragmentation de la mémoire et une dégradation des performances.

TreeAH, en revanche, fait des compromis architecturaux différents qui s'alignent sur la nature de BigQuery en tant que système d'analyse distribué.

La comparaison révèle un choix de conception fondamental : TreeAH donne la priorité au débit par lots, à l'efficacité mémoire et à l'évolutivité plutôt qu'à la latence absolue d'une requête unique. Cela le rend particulièrement adapté aux charges de travail analytiques où des milliers de recherches sont effectuées simultanément.

![Comparaison architecturale TreeAH vs HNSW](https://cdn.hashnode.com/res/hashnode/image/upload/v1715164800000/afafafaf-afaf-afaf-afaf-afafafafafaf.png)

## Le flux de requête de recherche vectorielle de bout en bout

La chronologie d'exécution d'une recherche vectorielle BigQuery démontre comment le traitement parallèle élimine les goulots d'étranglement traditionnels. Lorsqu'une requête VECTOR_SEARCH arrive, le système lance plusieurs opérations simultanément plutôt que de les exécuter séquentiellement.

Le serveur racine commence immédiatement la planification de la requête dès la réception de la demande. En parallèle, Borg commence à allouer des slots de calcul dans le cluster, ciblant 1 000 slots répartis sur 50 nœuds ou plus. Borg donne la priorité aux slots qui sont physiquement proches des données dans Colossus afin de minimiser les coûts de mouvement des données. Cette allocation se termine généralement en moins de 10 millisecondes.

La planification de la requête et l'allocation des ressources se chevauchent considérablement. Les nœuds mélangeurs reçoivent des plans d'exécution partiels et commencent à partitionner l'espace de recherche avant que Borg n'ait terminé toutes les allocations de slots. Lorsque les index TreeAH sont disponibles, les mélangeurs les utilisent pour assigner des partitions de vecteurs spécifiques aux nœuds feuilles. Cette approche en streaming garantit que les nœuds feuilles reçoivent leurs tâches dès qu'ils sont opérationnels.

La phase d'exécution parallèle illustre l'efficacité de l'architecture. Des centaines ou des milliers de nœuds feuilles lisent simultanément leurs partitions de vecteurs assignées depuis Colossus. Le réseau haute bande passante de Jupiter empêche la congestion des E/S même avec des milliers de lectures simultanées. Chaque nœud feuille fonctionne de manière indépendante : chargement des vecteurs compressés, exécution des opérations SIMD pour les calculs de distance et maintien des résultats top-k locaux.

L'agrégation commence avant que tous les nœuds feuilles n'aient terminé leurs recherches locales. Les mélangeurs implémentent un algorithme de fusion en streaming qui traite les résultats au fur et à mesure de leur arrivée. Cette approche signifie qu'au moment où le nœud feuille le plus lent transmet ses résultats, les mélangeurs ont déjà traité la majeure partie des données. Le top-k global final émerge de ce processus de fusion continue.

Le temps d'exécution mesuré de 40 millisecondes représente le chemin le plus long à travers le graphe d'exécution parallèle, et non la somme des opérations individuelles. La plupart des opérations se terminent beaucoup plus rapidement, mais la latence globale est limitée par le composant le plus lent. Cette conception privilégie le débit massif au détriment de la latence d'une requête unique, permettant à BigQuery de traiter des milliers de recherches vectorielles simultanément sur des milliards de vecteurs.

![Chronologie de la recherche vectorielle Big Query](https://cdn.hashnode.com/res/hashnode/image/upload/v1715164800000/bfbfbfbf-bfbf-bfbf-bfbf-bfbfbfbfbfbf.png)

## Implications pratiques pour les équipes d'ingénierie

Les choix architecturaux derrière la recherche vectorielle de BigQuery créent des compromis spécifiques que les équipes d'ingénierie doivent comprendre avant de s'engager dans cette approche.

### 1\. Latence de requête vs débit

Les recherches vectorielles BigQuery se terminent généralement en 1 à 10 secondes, loin de la latence inférieure à 100 ms des bases de données vectorielles spécialisées. Mais vous pouvez exécuter des milliers de recherches simultanément sans dégradation. Cela rend BigQuery idéal pour la génération de recommandations par lots, l'analyse de similitude sur des catalogues de produits ou les pipelines d'enrichissement de données basés sur les embeddings. C'est le mauvais choix pour les fonctionnalités d'autocomplétion ou la personnalisation en temps réel qui nécessite des réponses immédiates.

### 2\. Considérations sur le modèle de coût

BigQuery facture les données scannées, pas le temps d'exécution de la requête. Une recherche vectorielle qui scanne 1 To coûte la même chose qu'elle se termine en 2 secondes ou en 20 secondes. Ce modèle favorise les charges de travail où vous effectuez des recherches sur de grands ensembles de données de manière peu fréquente plutôt que sur de petits ensembles de données en continu. Exécuter une recherche vectorielle sur une table de 10 Go des milliers de fois par jour sera plus coûteux qu'une base de données vectorielle dédiée avec des coûts d'infrastructure fixes.

### 3\. Compromis sur la gestion des index

Les index TreeAH se mettent à jour automatiquement en arrière-plan lorsque de nouvelles données arrivent, généralement en 5 à 15 minutes. Vous ne pouvez pas forcer les mises à jour immédiates des index ni contrôler les paramètres d'indexation comme vous le feriez avec des index HNSW ou IVF. Cette simplicité réduit la charge opérationnelle mais limite les options d'optimisation. Si votre cas d'utilisation nécessite un réglage fin des compromis rappel/latence ou une cohérence immédiate après les mises à jour, vous aurez besoin d'une solution différente.

### 4\. Avantages de l'intégration qui comptent vraiment

La possibilité de joindre (JOIN) les résultats de la recherche vectorielle avec les données métier dans une seule requête est plus puissante qu'il n'y paraît au premier abord. Considérez ce modèle de requête :

```sql
WITH semantic_matches AS (

  SELECT item_id, distance

  FROM VECTOR_SEARCH(

    TABLE products,

    'embedding',

    (SELECT embedding FROM queries WHERE query_id = @query_id)

  )

)

SELECT p.*, s.distance

FROM semantic_matches s

JOIN products p USING (item_id)

WHERE p.in_stock = TRUE

  AND p.price BETWEEN 50 AND 200

  AND p.category_restrictions IS NULL

ORDER BY s.distance

LIMIT 20
```

Ceci combine la recherche sémantique avec la logique métier, l'état des stocks et les contrôles d'accès en une seule opération atomique. L'implémentation de ceci avec une base de données vectorielle séparée nécessite une synchronisation complexe entre les systèmes.

## Conclusion

L'implémentation de la recherche vectorielle par BigQuery remet en question nos certitudes sur ce qu'un entrepôt de données peut accomplir. Au lieu de construire une énième base de données vectorielle spécialisée, Google a poussé son infrastructure existante à gérer une charge de travail fondamentalement différente.

L'idée clé est de reconnaître que la recherche vectorielle à grande échelle est un problème de traitement de données. Et traiter des données à grande échelle est la raison d'être de BigQuery.

En tirant parti de son architecture colonnaire et d'algorithmes tenant compte du matériel comme TreeAH, BigQuery fait un compromis délibéré. Il échange la latence de l'ordre de la milliseconde des systèmes en mémoire contre un débit par lots massif et une efficacité incroyable des ressources. Un index qui utilise **10 fois moins de mémoire** que HNSW est un compromis que de nombreuses équipes construisant des systèmes d'IA analytiques accepteraient volontiers.

La véritable puissance émerge lorsque les vecteurs cohabitent avec les données métier. Des requêtes complexes qui nécessiteraient normalement plusieurs systèmes et des cauchemars de synchronisation deviennent du simple SQL. "Trouver des produits similaires, mais uniquement auprès de fournisseurs fiables, en stock localement, sans problème de qualité récent." Une seule requête, un seul système, pas de gymnastique architecturale.

Cette approche valide une tendance plus large : les capacités vectorielles deviennent un prérequis indispensable pour les plateformes de données. La question n'est plus de savoir si votre plateforme de données supportera les vecteurs, mais à quel point elle les intégrera dans les flux de travail existants.

Pour les équipes qui construisent des applications d'IA analytiques, BigQuery offre une voie pragmatique. Il ne gagnera pas les tests de latence face à des bases de données vectorielles dédiées. Mais pour le traitement par lots, l'analyse intégrée et la simplicité opérationnelle à l'échelle, il démontre que parfois, la meilleure base de données vectorielle n'est pas du tout une base de données vectorielle. C'est votre entrepôt de données, qui a évolué.

### Lectures complémentaires

* [BigQuery Under the Hood](https://cloud.google.com/blog/products/bigquery/bigquery-under-the-hood) : Plongée officielle dans l'architecture
    
* [ScaNN Algorithm Details](https://github.com/google-research/google-research/tree/master/scann/docs/algorithms.md) : Les mathématiques derrière TreeAH
    
* [Dremel: Interactive Analysis of Web-Scale Datasets](https://research.google/pubs/pub36632/) : L'article fondateur
    
* [Large-scale cluster management at Google with Borg](https://research.google/pubs/pub43438/) : Comprendre l'orchestration des ressources
    
* [Jupiter Rising: A Decade of Clos Topologies](https://research.google/pubs/pub43837/) : Le réseau de datacenter de Google
    
* [BigQuery Vector Search: A Practitioner's Guide](https://medium.com/google-cloud/bigquery-vector-search-a-practitioners-guide-0f85b0d988f0) : Stratégies d'optimisation