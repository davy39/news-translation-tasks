---
title: 'Tutoriel Google Cloud Platform : De Zéro à Héros avec GCP'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-10-09T15:24:46.000Z'
originalURL: https://freecodecamp.org/news/google-cloud-platform-from-zero-to-hero
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/gcp.png
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: google cloud
  slug: google-cloud
- name: Google Cloud Platform
  slug: google-cloud-platform
seo_title: 'Tutoriel Google Cloud Platform : De Zéro à Héros avec GCP'
seo_desc: 'By Sergio Fuentes Navarro

  Do you have the knowledge and skills to design a mobile gaming analytics platform
  that collects, stores, and analyzes large amounts of bulk and real-time data?

  Well, after reading this article, you will.

  I aim to take you fr...'
---

Par Sergio Fuentes Navarro

Avez-vous les connaissances et les compétences pour concevoir une plateforme d'analyse de jeux mobiles qui collecte, stocke et analyse de grandes quantités de données en masse et en temps réel ?

Eh bien, après avoir lu cet article, vous les aurez.

Je vise à vous emmener **de zéro à héros sur Google Cloud Platform (GCP) en un seul article**. Je vais vous montrer comment :

* Commencer avec un compte GCP gratuitement
* Réduire les coûts de votre infrastructure GCP
* Organiser vos ressources
* Automatiser la création et la configuration de vos ressources
* Gérer les opérations : journalisation, surveillance, traçage, etc.
* Stocker vos données
* Déployer vos applications et services
* Créer des réseaux dans GCP et les connecter avec vos réseaux sur site
* Travailler avec le Big Data, l'IA et le Machine Learning
* Sécuriser vos ressources

Une fois que j'aurai expliqué tous les sujets de cette liste, je partagerai avec vous une solution pour le système que j'ai décrit.

Si vous ne comprenez pas certaines parties, vous pouvez revenir aux sections pertinentes. Et si cela ne suffit pas, visitez les liens vers la documentation que j'ai fournis.

**Êtes-vous prêt pour un défi ?** J'ai sélectionné quelques questions d'anciens examens de certification professionnelle GCP. Elles testeront votre compréhension des concepts expliqués dans cet article.

Je recommande d'essayer de résoudre à la fois la conception et les questions _par vous-même_, en revenant au guide si nécessaire. Une fois que vous avez une réponse, comparez-la à la solution proposée.

Essayez d'aller au-delà de ce que vous lisez et demandez-vous ce qui se passerait si l'exigence X changeait :

* Données par lots vs données en streaming
* Solution régionale vs globale
* Un petit nombre d'utilisateurs vs un énorme volume d'utilisateurs
* La latence n'est pas un problème vs applications en temps réel

Et tout autre scénario auquel vous pouvez penser.

À la fin de la journée, vous n'êtes pas payé juste pour ce que vous savez, mais pour votre processus de réflexion et les décisions que vous prenez. C'est pourquoi il est vitalement important que vous exerciez cette compétence.

À la fin de l'article, je fournirai plus de ressources et les prochaines étapes si vous souhaitez continuer à apprendre sur GCP.

## **Comment commencer avec Google Cloud Platform gratuitement**

GCP offre actuellement un [essai gratuit de 3 mois](https://cloud.google.com/free) avec 300 dollars américains de crédit gratuit. Vous pouvez l'utiliser pour commencer, explorer GCP et effectuer des expériences pour décider si c'est la bonne option pour vous.

**Vous ne serez PAS facturé** à la fin de votre essai. Vous serez notifié et vos services cesseront de fonctionner sauf si vous décidez de mettre à niveau votre plan.

Je recommande fortement d'utiliser cet essai pour pratiquer. Pour apprendre, vous devez **essayer les choses par vous-même**, faire face à des problèmes, casser des choses et les réparer. Peu importe à quel point ce guide est bon (ou la documentation officielle d'ailleurs) si vous n'essayez pas les choses.

## **Pourquoi migreriez-vous vos services vers Google Cloud Platform ?**

Consommer des ressources de GCP, comme le stockage ou la puissance de calcul, offre les avantages suivants :

* Pas besoin de dépenser beaucoup d'argent à l'avance pour le matériel
* Pas besoin de mettre à niveau votre matériel et de migrer vos données et services tous les quelques années
* Capacité à ajuster la demande, en payant uniquement pour les ressources que vous consommez
* Créer des preuves de concept rapidement puisque la provision de ressources peut être faite très rapidement
* Sécuriser et gérer vos [API](https://cloud.google.com/endpoints/docs)
* Pas seulement de l'infrastructure : des services d'analyse de données et de machine learning sont disponibles dans GCP

GCP facilite l'expérimentation et l'utilisation des ressources dont vous avez besoin de manière économique.

## Comment optimiser vos VM pour réduire les coûts dans GCP

En général, vous ne serez facturé que pour le temps pendant lequel vos instances sont en cours d'exécution. Google ne vous facturera pas pour les instances arrêtées. Cependant, si elles consomment des ressources, comme des disques ou des IP réservées, vous pourriez encourir des frais.

Voici quelques moyens d'optimiser le coût d'exécution de vos applications dans GCP.

### Types de machines personnalisés

GCP fournit différentes [familles de machines](https://cloud.google.com/compute/docs/machine-types) avec des quantités prédéfinies de RAM et de CPU :

* **Usage général**. Offre le meilleur rapport prix-performance pour une variété de charges de travail.
* **Optimisé pour la mémoire**. Idéal pour les charges de travail intensives en mémoire. Ils offrent plus de mémoire par cœur que les autres types de machines.
* **Optimisé pour le calcul**. Ils offrent la meilleure performance par cœur et sont optimisés pour les charges de travail intensives en calcul.
* **Cœur partagé**. Ces types de machines partagent un cœur physique. Cela peut être une méthode rentable pour exécuter de petites applications.

De plus, vous pouvez créer votre machine personnalisée avec la quantité de RAM et de CPU dont vous avez besoin.

### VM préemptibles

Vous pouvez utiliser des machines virtuelles préemptibles pour économiser jusqu'à 80 % de vos coûts. Elles sont idéales **pour les applications tolérantes aux pannes et non critiques**. Vous pouvez sauvegarder la progression de votre travail sur un disque persistant en utilisant un script d'arrêt pour continuer là où vous vous êtes arrêté.

Google peut arrêter vos instances à tout moment (avec un avertissement de 30 secondes) et les arrêtera toujours après 24 heures.

Pour réduire les chances que vos VM soient arrêtées, Google recommande :

* Utiliser **de nombreuses petites instances** et
* Exécuter vos travaux pendant les **heures creuses**.

**Note** : Les scripts de démarrage et d'arrêt s'appliquent également aux VM non préemptibles. Vous pouvez les utiliser pour contrôler le comportement de votre machine lorsqu'elle démarre ou s'arrête. Par exemple, pour installer des logiciels, télécharger des données ou sauvegarder des journaux.

Il existe deux options pour définir ces scripts :

* Lorsque vous créez votre instance dans la console Google, il y a un champ pour coller votre code.
* Utiliser l'URL du serveur de métadonnées pour pointer votre instance vers un script stocké dans Google Cloud Storage.

Cette dernière option est préférée car elle est plus facile à créer de nombreuses instances et à gérer le script.

### Remises pour utilisation prolongée

Plus vous utilisez vos machines virtuelles (et les instances Cloud SQL) longtemps, plus la remise est élevée - jusqu'à 30 %. Google le fait automatiquement pour vous.

### Remises pour engagement d'utilisation

Vous pouvez obtenir jusqu'à 57 % de remise si vous vous engagez à une certaine quantité de ressources CPU et RAM pour une période de 1 à 3 ans.

Pour estimer vos coûts, utilisez le [calculateur de prix](https://cloud.google.com/products/calculator). Cela aide à prévenir les surprises avec vos factures et à créer des [alertes budgétaires](https://cloud.google.com/billing/docs/how-to/budgets).

## **[Comment gérer les ressources dans GCP](https://cloud.google.com/resource-manager/docs)**

Dans cette section, je vais expliquer comment vous pouvez gérer et administrer vos ressources Google Cloud.

### **[Hiérarchie des ressources](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy)**

![Image](https://www.freecodecamp.org/news/content/images/2020/10/resource-manager.png)

Il existe quatre types de ressources qui peuvent être gérées via Resource Manager :

* **La ressource organisation**. Il s'agit du nœud racine dans la hiérarchie des ressources. Elle représente une organisation, par exemple, une entreprise.
* **La ressource projet**. Par exemple, pour séparer les projets pour les environnements de production et de développement. Ils sont **requis** pour créer des ressources.
* **La ressource dossier**. Ils fournissent un niveau supplémentaire d'isolation des projets. Par exemple, créer un dossier pour chaque département dans une entreprise.
* **Ressources**. Machines virtuelles, instances de base de données, équilibreurs de charge, etc.

Il existe des **quotas** qui limitent le nombre maximum de ressources que vous pouvez créer pour éviter les pics inattendus de facturation. Cependant, la plupart des quotas peuvent être augmentés en ouvrant un ticket de support.

Les ressources dans GCP suivent une **hiérarchie** via une relation parent/enfant, similaire à un système de fichiers traditionnel, où :

* **Les permissions sont héritées lorsque nous descendons la hiérarchie**. Par exemple, les permissions accordées au niveau de l'organisation seront propagées à tous les dossiers et projets.
* Les politiques parentales plus permissives annulent toujours les politiques enfant plus restrictives.

Cette organisation hiérarchique vous aide à gérer les aspects communs de vos ressources, tels que le contrôle d'accès et les paramètres de configuration.

Vous pouvez créer des comptes super administrateur qui ont accès à toutes les ressources de votre organisation. Comme ils sont très puissants, assurez-vous de suivre les [bonnes pratiques de Google](https://cloud.google.com/resource-manager/docs/super-admin-best-practices).

### Étiquettes

Les étiquettes sont des paires clé-valeur que vous pouvez utiliser pour organiser vos ressources dans GCP. Une fois que vous avez attaché une étiquette à une ressource (par exemple, à une machine virtuelle), vous pouvez filtrer en fonction de cette étiquette. Cela est également utile pour ventiler vos factures par étiquettes.

Quelques cas d'utilisation courants :

* Environnements : prod, test, etc.
* Équipe ou propriétaires de produits
* Composants : backend, frontend, etc.
* État de la ressource : actif, archive, etc.

### Étiquettes vs balises réseau

Ces deux concepts similaires semblent générer une certaine confusion. J'ai résumé les différences dans ce tableau :

| Étiquettes                      | Balises réseau                                                 |
| --------------------------- | ------------------------------------------------------------ |
| Appliquées à toute ressource GCP | Appliquées uniquement pour les ressources VPC                               |
| Organiser simplement les ressources     | Affectent le fonctionnement des ressources (ex : par l'application de règles de pare-feu) |

### **[Cloud IAM](https://cloud.google.com/iam/docs)**

En termes simples, Cloud IAM contrôle **qui peut faire quoi sur quelle ressource**. Une ressource peut être une machine virtuelle, une instance de base de données, un utilisateur, etc.

Il est important de noter que les permissions ne sont pas directement attribuées aux utilisateurs. Au lieu de cela, elles sont regroupées en _rôles_, qui sont attribués à des _membres_. Une _politique_ est une collection d'une ou plusieurs liaisons d'un ensemble de membres à un rôle.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/IAM.svg)

### Identités

Dans un projet GCP, les identités sont représentées par des comptes Google, créés en dehors de GCP, et définis par une adresse e-mail (pas nécessairement @gmail.com). Il existe différents types :

* **Comptes Google***. Pour représenter des personnes : ingénieurs, administrateurs, etc.
* **Comptes de service**. Utilisés pour identifier les utilisateurs non humains : applications, services, machines virtuelles, etc. Le processus d'authentification est défini par des _clés de compte_, qui peuvent être gérées par Google ou par les utilisateurs (uniquement pour les comptes de service créés par l'utilisateur).
* **Groupes Google** sont une collection de comptes Google et de comptes de service.
* **Domaine G Suite*** est le type de compte que vous pouvez utiliser pour identifier les organisations. Si votre organisation utilise déjà [Active Directory](https://en.wikipedia.org/wiki/Active_Directory), il peut être synchronisé avec Cloud IAM en utilisant [Cloud Identity](https://cloud.google.com/identity/docs).
* **allAuthenticatedUsers**. Pour représenter tout utilisateur authentifié dans GCP.
* **allUsers**. Pour représenter toute personne, authentifiée ou non.

En ce qui concerne les comptes de service, certaines des meilleures pratiques de Google incluent :

* Ne pas utiliser le compte de service par défaut
* Appliquer le [Principe du moindre privilège](https://en.wikipedia.org/wiki/Principle_of_least_privilege). Par exemple :
1. Restreindre qui peut agir en tant que compte de service
2. Accorder uniquement l'ensemble minimal de permissions dont le compte a besoin
3. Créer des comptes de service pour chaque service, uniquement avec les permissions dont le compte a besoin

### Rôles

Un rôle est une **collection de permissions**. Il existe trois types de rôles :

* **Primitif**. Rôles GCP originaux qui s'appliquent à l'ensemble du projet. Il existe trois rôles concentriques : **Viewer**, **Editor** et **Owner**. Editor contient Viewer et Owner contient Editor.
* **Prédéfini**. Fournit l'accès à des services spécifiques, par exemple storage.admin.
* **Personnalisé**. vous permet de créer vos propres rôles, en combinant les permissions spécifiques dont vous avez besoin.

Lors de l'attribution de rôles, suivez également le principe du moindre privilège. En général, **préférez les rôles prédéfinis aux rôles primitifs**.

### **[Cloud Deployment Manager](https://cloud.google.com/deployment-manager/docs)**

Cloud Deployment Manager automatise les tâches répétitives comme la provision, la configuration et les déploiements pour un nombre quelconque de machines.

C'est le service _Infrastructure as Code_ de Google, similaire à Terraform - bien que vous ne puissiez déployer que des ressources GCP. Il est utilisé par [GCP Marketplace](https://cloud.google.com/marketplace) pour créer des déploiements préconfigurés.

Vous définissez votre configuration dans des fichiers YAML, en listant les ressources (créées via des appels API) que vous souhaitez créer et leurs propriétés. Les ressources sont définies par leur **nom** (VM-1, disk-1), **type** (compute.v1.disk, compute.v1.instance) et **propriétés** (zone:europe-west4, boot:false).

Pour augmenter les performances, les ressources sont déployées en parallèle. Par conséquent, vous devez **spécifier les dépendances en utilisant des références**. Par exemple, ne créez pas de machine virtuelle VM-1 tant que le disque persistant disk-1 n'a pas été créé. En revanche, Terraform déterminerait les dépendances par lui-même.

Vous pouvez modulariser vos fichiers de configuration en utilisant des templates afin qu'ils puissent être mis à jour et partagés indépendamment. Les templates peuvent être définis en Python ou Jinja2. Le contenu de vos templates sera intégré dans le fichier de configuration qui les référence.

Deployment Manager créera un manifeste contenant votre configuration originale, les templates que vous avez importés et la liste étendue de toutes les ressources que vous souhaitez créer.

## **[Cloud Operations (anciennement Stackdriver)](https://cloud.google.com/stackdriver/docs)**

![Image](https://www.freecodecamp.org/news/content/images/2020/10/stackd.jpg)

Operations fournit un ensemble d'outils pour la surveillance, la journalisation, le débogage, la notification d'erreurs, le profilage et le traçage des ressources dans GCP (AWS et même sur site).

### **Cloud Logging**

Cloud Logging est la solution centralisée de GCP pour la gestion des journaux en temps réel. Pour chacun de vos projets, il vous permet de stocker, rechercher, analyser, surveiller et alerter sur les données de journalisation :

* Par défaut, les données seront stockées pendant une certaine période. La période de conservation varie en fonction du type de journal. Vous ne pouvez pas récupérer les journaux après qu'ils ont dépassé cette période de conservation.
* Les journaux peuvent être exportés à différentes fins. Pour ce faire, vous créez un **sink**, qui est composé d'un **filtre** (pour sélectionner ce que vous souhaitez journaliser) et d'une **destination** : Google Cloud Storage (GCS) pour une conservation à long terme, BigQuery pour l'analyse, ou Pub/Sub pour le diffuser dans d'autres applications.
* Vous pouvez créer des métriques basées sur les journaux dans Cloud Monitoring et même être alerté lorsque quelque chose ne va pas.

Les journaux sont une collection nommée d'**entrées de journal**. Les entrées de journal enregistrent l'état ou les événements et incluent le nom de leur journal, par exemple, compute.googleapis.com/activity. Il existe deux principaux types de journaux :

**Premièrement, les journaux utilisateur :**

* Ceux-ci sont générés par vos applications et services.
* Ils sont écrits dans Cloud Logging en utilisant l'API Cloud Logging, les bibliothèques clientes ou les [agents de journalisation](https://cloud.google.com/logging/docs/agent) installés sur vos machines virtuelles.
* Ils diffusent les journaux d'applications tierces courantes comme MySQL, MongoDB ou Tomcat.

**Deuxièmement, les journaux de sécurité, divisés en :**

* Journaux d'audit, pour les changements administratifs, les événements système et l'accès aux données de vos ressources. Par exemple, qui a créé une instance de base de données particulière ou pour journaliser une [migration en direct](https://cloud.google.com/compute/docs/instances/live-migration). Les journaux d'accès aux données doivent être explicitement activés et peuvent entraîner des frais supplémentaires. Les autres sont activés par défaut, ne peuvent pas être désactivés et sont gratuits.
* Journaux de transparence d'accès, pour les actions entreprises par le personnel de Google lorsqu'ils accèdent à vos ressources, par exemple pour enquêter sur un problème que vous avez signalé à l'équipe de support.

#### Journaux de flux VPC

Ils sont spécifiques aux réseaux VPC (que je présenterai plus tard). Les journaux de flux VPC enregistrent un **échantillon de flux réseau** envoyés et reçus par les instances de VM, qui peuvent être consultés ultérieurement dans Cloud Logging.

Ils peuvent être utilisés pour surveiller les performances du réseau, l'utilisation, la forensique, l'analyse de sécurité en temps réel et l'optimisation des coûts.

**Note** : vous pouvez souhaiter journaliser vos données de facturation pour analyse. Dans ce cas, vous ne créez _pas_ de sink. Vous pouvez directement exporter vos rapports vers BigQuery.

### **Cloud Monitoring**

Cloud Monitoring vous permet de surveiller les performances de vos applications et de votre infrastructure, de les visualiser dans des tableaux de bord, de créer des [vérifications de disponibilité](https://cloud.google.com/monitoring/uptime-checks) pour détecter les ressources qui sont hors service et de vous [alerter](https://cloud.google.com/monitoring/alerts) en fonction de ces vérifications afin que vous puissiez résoudre les problèmes dans votre environnement. Vous pouvez surveiller les ressources dans GCP, AWS et même sur site.

Il est recommandé de créer un projet séparé pour Cloud Monitoring, car il peut suivre les ressources de plusieurs projets.

De plus, il est recommandé d'installer un agent de surveillance dans vos machines virtuelles pour envoyer des métriques d'application (y compris de nombreuses applications tierces) à Cloud Monitoring. Sinon, Cloud Monitoring n'affichera que les métriques de CPU, de trafic de disque, de trafic réseau et de disponibilité.

#### Alertes

Pour recevoir des alertes, vous devez déclarer une **politique d'alerte**. Une politique d'alerte définit les **conditions** dans lesquelles un service est considéré comme non sain. Lorsque les conditions sont remplies, un nouvel incident sera créé et des notifications seront envoyées (par e-mail, Slack, SMS, PagerDuty, etc.).

Une politique appartient à un espace de travail individuel, qui peut contenir un maximum de 500 politiques.

#### Trace

Trace aide à **trouver les goulots d'étranglement dans vos services**. Vous pouvez utiliser ce service pour déterminer combien de temps il faut pour traiter une demande, quel microservice met le plus de temps à répondre, où concentrer vos efforts pour réduire la latence globale, etc.

Il est activé par défaut pour les applications exécutées sur Google App Engine (GAE) - Environnement standard - mais peut être utilisé pour les applications exécutées sur GCE, GKE et Google App Engine Flexible.

#### Rapport d'erreurs

Le rapport d'erreurs agrège et affiche les erreurs produites dans les services écrits en Go, Java, Node.js, PHP, Python, Ruby ou .NET, exécutés sur GCE, GKE, GAP, Cloud Functions ou Cloud Run.

#### Débogage

Le débogage vous permet d'inspecter l'état de l'application sans arrêter votre service. Actuellement pris en charge pour Java, Go, Node.js et Python. Il est automatiquement intégré avec GAE mais peut être utilisé sur GCE, GKE et Cloud Run.

#### Profilage

Profileur qui collecte en continu les informations d'utilisation du CPU et d'allocation de mémoire de vos applications. Pour l'utiliser, vous devez installer un agent de profilage.

## **Comment stocker des données dans GCP**

Dans cette section, je couvrirai à la fois Google Cloud Storage (pour tout type de données, y compris les fichiers, les images, les vidéos, etc.), les différents services de base de données disponibles dans GCP, et comment décider quelle option de stockage fonctionne le mieux pour vous.

### **[Google Cloud Storage (GCS)](https://cloud.google.com/storage/docs)**

![Image](https://www.freecodecamp.org/news/content/images/2020/10/gcs.jpg)

GCS est le **service de stockage de Google pour les données non structurées** : images, vidéos, fichiers, scripts, sauvegardes de bases de données, etc.

Les objets sont placés dans des **buckets**, dont ils héritent des permissions et des classes de stockage.

Les [classes de stockage](https://cloud.google.com/storage/docs/storage-classes) offrent différents SLA pour stocker vos données afin de minimiser les coûts pour votre cas d'utilisation. La classe de stockage d'un bucket peut être modifiée (sous certaines restrictions), mais cela n'affectera que les nouveaux objets ajoutés au bucket.

En plus de la console Google, vous pouvez interagir avec GCS depuis votre ligne de commande, en utilisant [gsutil](https://cloud.google.com/storage/docs/gsutil). Vous pouvez spécifier :

* **Mises à jour multithread** lorsque vous devez télécharger un grand nombre de petits fichiers. La commande ressemble à gsutil -m cp files gs://my-bucket)
* **Mises à jour parallèles** lorsque vous devez télécharger de grands fichiers. Pour plus de détails et de restrictions, visitez ce [lien](https://cloud.google.com/storage/docs/gsutil/commands/cp#parallel-composite-uploads).

Une autre option pour télécharger des fichiers vers GCS est [Storage Transfer Service (STS)](https://cloud.google.com/storage-transfer/docs), un service qui importe des données vers un bucket GCS à partir de :

* Un bucket AWS S3
* Une ressource accessible via HTTP(S)
* Un autre bucket Google Cloud Storage

Si vous devez télécharger d'énormes quantités de données (de centaines de téraoctets à un pétaoctet), envisagez [Data Transfer Appliance](https://cloud.google.com/transfer-appliance/docs/2.2) : expédiez vos données vers une installation Google. Une fois qu'ils ont téléchargé les données vers GCS, le processus de [réhydratation des données](https://cloud.google.com/transfer-appliance/docs/2.0/data-rehydration) reconstitue les fichiers afin qu'ils puissent être consultés à nouveau.

#### [Gestion du cycle de vie des objets](https://cloud.google.com/storage/docs/lifecycle)

Vous pouvez définir des règles qui déterminent ce qui arrivera à un objet (sera-t-il archivé ou supprimé) lorsqu'une certaine condition est remplie.

Par exemple, vous pourriez définir une politique pour changer automatiquement la classe de stockage d'un objet de Standard à Nearline après 30 jours et pour le supprimer après 180 jours.

Voici comment une règle peut être définie :

```js
{
   "lifecycle":{
      "rule":[
         {
            "action":{
               "type":"Delete"
            },
            "condition":{
               "age":30,
               "isLive":true
            }
         },
         {
            "action":{
               "type":"Delete"
            },
            "condition":{
               "numNewerVersions":2
            }
         },
         {
            "action":{
               "type":"Delete"
            },
            "condition":{
               "age":180,
               "isLive":false
            }
         }
      ]
   }
}
```

Elle sera appliquée via gsutils ou un appel d'API REST. Les règles peuvent également être créées via la console Google.

#### Permissions dans GCS

En plus des rôles IAM, vous pouvez utiliser des listes de contrôle d'accès (ACL) pour gérer l'accès aux ressources dans un bucket.

Utilisez les rôles IAM lorsque cela est possible, mais rappelez-vous que les **ACL** accordent l'accès aux buckets et aux **objets individuels**, tandis que les **rôles IAM sont des permissions au niveau du projet ou du bucket**. Les deux méthodes fonctionnent en tandem.

Pour accorder un accès temporaire aux utilisateurs en dehors de GCP, utilisez les [URL signées](https://cloud.google.com/storage/docs/access-control/signed-urls).

#### Verrouillage de bucket

Les verrous de bucket vous permettent d'imposer une **période de conservation minimale** pour les objets dans un bucket. Vous pourriez en avoir besoin pour des raisons d'audit ou légales.

**Une fois qu'un bucket est verrouillé, il ne peut pas être déverrouillé**. Pour le supprimer, vous devez d'abord supprimer tous les objets du bucket, ce que vous ne pouvez faire qu'après qu'ils ont tous atteint la période de conservation spécifiée par la politique de conservation. Ce n'est qu'alors que vous pourrez supprimer le bucket.

Vous pouvez inclure la politique de conservation lorsque vous créez le bucket ou ajouter une politique de conservation à un bucket existant (elle s'applique rétroactivement aux objets existants dans le bucket également).

Fait amusant : la période de conservation maximale est de 100 ans.

### **Bases de données relationnelles gérées dans GCP**

Cloud SQL et Cloud Spanner sont deux services de base de données gérés disponibles dans GCP. Si vous ne souhaitez pas gérer tout le travail nécessaire pour maintenir une base de données en ligne, ils sont une excellente option. Vous pouvez toujours lancer une machine virtuelle et gérer votre propre base de données.

#### [Cloud SQL](https://cloud.google.com/sql/docs)

Cloud SQL fournit l'accès à une instance de base de données MySQL ou PostgreSQL gérée dans GCP. Chaque instance est limitée à une **seule région** et a une **capacité maximale de 30 To**.

Google s'occupera de l'installation, des sauvegardes, de la mise à l'échelle, de la surveillance, du basculement et des réplicas de lecture. Pour des raisons de disponibilité, les réplicas doivent être définis dans la même région mais dans une zone différente de celle des instances principales.

Les données peuvent être facilement importées (d'abord en téléchargeant les données vers Google Cloud Storage puis vers l'instance) et exportées en utilisant des formats de fichiers SQL ou CSV. Les données peuvent être compressées pour réduire les coûts (vous pouvez directement importer des fichiers .gz). Pour les migrations "lift and shift", c'est une excellente option.

Si vous avez besoin d'une disponibilité mondiale ou de plus de capacité, envisagez d'utiliser Cloud Spanner.

#### [Cloud Spanner](https://cloud.google.com/spanner/docs)

Cloud Spanner est disponible mondialement et peut être mis à l'échelle (horizontalement) très facilement.

Ces deux caractéristiques le rendent capable de supporter différents cas d'utilisation que Cloud SQL et plus coûteux aussi. Cloud Spanner n'est pas une option pour les migrations lift and shift.

### **Bases de données NoSQL gérées dans GCP**

De même, GCP fournit deux bases de données NoSQL gérées, Bigtable et Datastore, ainsi qu'un service de base de données en mémoire, Memorystore.

#### [Datastore](https://cloud.google.com/datastore/docs)

Datastore est une base de données de documents entièrement sans opération, hautement évolutive, idéale pour les applications web et mobiles : états de jeu, catalogues de produits, inventaire en temps réel, etc. C'est idéal pour :

* Profils utilisateurs - applications mobiles
* États de sauvegarde de jeu

Par défaut, Datastore dispose d'un **index** intégré qui améliore les performances des requêtes simples. Vous pouvez créer vos propres index, appelés **index composites**, définis au format YAML.

Si vous avez besoin d'un débit extrême (nombre énorme de lectures/écritures par seconde), utilisez Bigtable à la place.

#### [Bigtable](https://cloud.google.com/bigtable/docs)

Bigtable est une base de données NoSQL idéale pour les charges de travail analytiques où vous pouvez vous attendre à un très grand volume d'écritures, des lectures en millisecondes et la capacité de stocker des téraoctets à des pétaoctets d'informations. C'est idéal pour :

* Analyse financière
* Données IoT
* Données marketing

Bigtable nécessite la création et la configuration de vos nœuds (contrairement à Datastore ou BigQuery entièrement gérés). Vous pouvez ajouter ou supprimer des nœuds de votre cluster sans temps d'arrêt. La manière la plus simple d'interagir avec Bigtable est l'outil en ligne de commande [cbt](https://cloud.google.com/bigtable/docs/cbt-overview).

Les performances de Bigtable dépendront de la conception de votre schéma de base de données.

* Vous ne pouvez définir qu'une seule clé par ligne et devez conserver toutes les informations associées à une entité dans la même ligne. Pensez-y comme une table de hachage.
* Les tables sont clairsemées : si aucune information n'est associée à une colonne, aucun espace n'est requis.
* Pour rendre les lectures plus efficaces, essayez de stocker les entités liées dans des lignes adjacentes.

Puisque ce sujet mérite un article à part entière, je vous recommande de lire la [documentation](https://cloud.google.com/bigtable/docs/performance).

#### [Memorystore](https://cloud.google.com/memorystore/docs)

Il fournit une version gérée de Redis et Memcache (bases de données en mémoire), résultant en des performances très rapides. Les instances sont régionales, comme Cloud SQL, et ont une capacité allant jusqu'à 300 Go.

### **Comment choisir votre base de données**

Google adore les arbres de décision. Celui-ci vous aidera à choisir la bonne base de données pour vos projets. Pour les données non structurées, envisagez GCS ou traitez-les en utilisant Dataflow (discuté plus tard).

![Image](https://www.freecodecamp.org/news/content/images/2020/10/choose-db.svg)

## **Comment fonctionne le réseau dans GCP ?**

### **Virtual Private Cloud (VPC) - [voir la documentation ici](https://cloud.google.com/vpc/docs/)**

Vous pouvez utiliser la même infrastructure réseau que Google utilise pour exécuter ses services : YouTube, Search, Maps, Gmail, Drive, etc.

L'infrastructure Google est divisée en :

* **Régions** : Zones géographiques indépendantes, distantes d'au moins 100 miles les unes des autres, où Google héberge des centres de données. Elle se compose de 3 zones ou plus. Par exemple, us-central1.
* **Zones** : Plusieurs centres de données individuels dans une région. Par exemple, us-central1-a.
* **Points de présence Edge** : points de connexion entre le réseau de Google et le reste d'Internet.

L'infrastructure GCP est conçue de manière à ce que tout le trafic entre les régions voyage à travers un réseau privé mondial, résultant en une meilleure sécurité et performance.

Sur le dessus de cette infrastructure, vous pouvez construire des réseaux pour vos ressources, des Virtual Private Clouds. Ce sont des **réseaux définis par logiciel**, où tous les concepts traditionnels de réseau s'appliquent :

* [Sous-réseaux](https://cloud.google.com/vpc/docs/vpc#subnets_vs_subnetworks). Partitions logiques d'un réseau définies en utilisant la [notation CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing). Ils appartiennent à une seule région mais peuvent s'étendre sur plusieurs zones. Si vous avez plusieurs sous-réseaux (y compris vos réseaux sur site s'ils sont connectés à GCP), assurez-vous que les plages CIDR ne se chevauchent pas.
* **Adresses IP**. Peuvent être internes (pour la communication privée au sein de GCP) ou externes (pour communiquer avec le reste d'Internet). Pour les adresses IP externes, vous pouvez utiliser une **IP éphémère** ou payer pour une **IP statique**. En général, vous avez besoin d'une adresse IP externe pour vous connecter aux services GCP. Cependant, dans certains cas, vous pouvez configurer un [accès privé](https://cloud.google.com/vpc/docs/private-access-options) pour les instances qui n'ont qu'une IP interne.
* [Règles de pare-feu](https://cloud.google.com/vpc/docs/firewalls), pour autoriser ou refuser le trafic vers vos machines virtuelles, à la fois entrant (ingress) et sortant (egress). Par défaut, tout le trafic ingress est refusé et tout le trafic egress est autorisé. Les règles de pare-feu sont définies au niveau du VPC mais elles **s'appliquent à des instances individuelles ou à des groupes d'instances** en utilisant des **balises réseau** ou des **plages d'IP**.
**Problème courant** : Si vous savez que vos VM fonctionnent correctement mais que vous ne pouvez pas y accéder via HTTP(s) ou ne pouvez pas vous y connecter via SSH, jetez un coup d'œil à vos règles de pare-feu.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/vpc.png)

Vous pouvez créer des **réseaux hybrides** en connectant votre infrastructure sur site à votre VPC.

Lorsque vous créez un projet, un **réseau par défaut** sera créé avec des sous-réseaux dans chaque région (mode auto). Vous pouvez supprimer ce réseau, mais vous devez créer au moins un réseau pour pouvoir créer des machines virtuelles.

Vous pouvez également créer vos **réseaux personnalisés**, où aucun sous-réseau n'est créé par défaut et vous avez un contrôle total sur la création de sous-réseaux (mode personnalisé).

Le principal objectif d'un VPC est la **séparation des ressources réseau**. Un projet GCP est un moyen d'organiser les ressources et de gérer les permissions.

Les utilisateurs du projet A ont besoin de permissions pour accéder aux ressources du projet B. Tous les utilisateurs peuvent accéder à tout VPC défini dans tout projet auquel ils appartiennent. Au sein du même VPC, les ressources du sous-réseau 1 doivent se voir accorder l'accès aux ressources du sous-réseau 2.

En termes de rôles IAM, il y a une distinction entre qui peut créer des ressources réseau (Administrateur réseau, pour créer des sous-réseaux, des machines virtuelles, etc.) et qui est responsable de la sécurité des ressources (Administrateur de sécurité, pour créer des règles de pare-feu, des certificats SSL, etc.).

Le rôle d'administrateur d'instance de calcul combine les deux rôles.

Comme d'habitude, il y a des quotas et des limites à ce que vous pouvez faire dans un VPC, parmi eux :

* Le nombre maximum de VPC dans un projet.
* Le nombre maximum de machines virtuelles par VPC.
* Pas de diffusion ou de multidiffusion.
* Les VPC ne peuvent pas utiliser IPv6 pour communiquer en interne, bien que les équilibreurs de charge globaux prennent en charge le trafic IPv6.

### **Comment partager des ressources entre plusieurs VPC**

#### [VPC partagé](https://cloud.google.com/vpc/docs/shared-vpc)

Les VPC partagés sont un moyen de partager des ressources entre différents projets au sein de la même organisation. Cela vous permet de contrôler la facturation et de gérer l'accès aux ressources dans différents projets, en suivant le principe du moindre privilège. Sinon, vous devriez mettre toutes les ressources dans un seul projet.

Pour concevoir un VPC partagé, les projets sont divisés en trois catégories :

* **Projet hôte**. Il s'agit du projet qui héberge les ressources communes. Il ne peut y avoir qu'un seul projet hôte.
* **Projet de service** : Projets qui peuvent accéder aux ressources du projet hôte. Un projet ne peut pas être à la fois hôte et service.
* **Projet autonome**. Tout projet qui n'utilise pas le VPC partagé.

Vous ne pourrez communiquer qu'entre les ressources créées **après** avoir défini vos projets hôte et de service. Toute ressource existante avant cela ne fera pas partie du VPC partagé.

#### [VPC Network Peering](https://cloud.google.com/vpc/docs/vpc-peering)

Les VPC partagés peuvent être utilisés lorsque tous les projets appartiennent à la même organisation. Cependant, si :

* Vous avez besoin d'une **communication privée** entre les VPC.
* Les VPC sont dans des projets qui peuvent appartenir à des **organisations différentes**.
* Vous voulez un contrôle **décentralisé**, c'est-à-dire, pas besoin de définir des projets hôte, des projets serveur, etc.
* Vous voulez réutiliser des ressources existantes.

Le peering de réseau VPC est la bonne solution.

Dans la section suivante, je vais discuter de la manière de connecter votre ou vos VPC avec des réseaux en dehors de GCP.

## Comment connecter les infrastructures sur site et GCP

![Image](https://www.freecodecamp.org/news/content/images/2020/10/interc.jpg)

Il existe trois options pour connecter votre infrastructure sur site à GCP :

* Cloud VPN
* Cloud Interconnect
* Cloud Peering

Chacune d'entre elles avec des capacités, des cas d'utilisation et des prix différents que je vais décrire dans les sections suivantes.

### [Cloud VPN](https://cloud.google.com/network-connectivity/docs/vpn)

Avec Cloud VPN, votre trafic voyage sur Internet public via un tunnel chiffré. Chaque tunnel a une capacité maximale de 3 Gb par seconde et vous pouvez en utiliser un maximum de 8 pour de meilleures performances. Ces deux caractéristiques font du VPN l'option la moins chère.

Vous pouvez définir deux types de routes entre votre VPC et vos réseaux sur site :

* **Routes statiques**. Vous devez les définir et les mettre à jour manuellement, par exemple lorsque vous ajoutez un nouveau sous-réseau. Ce n'est pas l'option préférée.
* **Routes dynamiques**. Les routes sont gérées automatiquement (définies et mises à jour) pour vous en utilisant [Cloud Router](https://cloud.google.com/network-connectivity/docs/router). C'est l'option préférée lorsque [BGP](https://en.wikipedia.org/wiki/Border_Gateway_Protocol) est disponible.

Votre trafic est chiffré et déchiffré par des passerelles VPN (dans GCP, ce sont des ressources régionales).

Pour avoir une connexion plus robuste, envisagez d'utiliser plusieurs passerelles VPN et tunnels. En cas de défaillance, cette redondance garantit que le trafic continuera de circuler.

### [Cloud Interconnect](https://cloud.google.com/network-connectivity/docs/interconnect)

Avec Cloud VPN, le trafic voyage sur Internet public. Avec Cloud Interconnect, il y a une **connexion physique directe** entre votre réseau sur site et votre VPC. Cette option sera plus chère mais offrira les meilleures performances.

Il existe deux types d'interconnexion disponibles, selon la manière dont vous souhaitez que votre connexion à GCP se matérialise :

* **Interconnexion dédiée**. Il y a "un câble direct" reliant votre infrastructure et GCP. C'est l'option la plus rapide, avec une capacité de 10 à 200 Gb par seconde. Cependant, elle n'est pas disponible partout : au moment de la rédaction de cet article, seulement dans 62 endroits dans le monde.
* **Interconnexion partenaire**. Vous vous connectez via un fournisseur de services. Cette option est plus disponible géographiquement, mais pas aussi rapide que les interconnexions dédiées : de 50 Mb par seconde à 10 Gb par seconde.

### [Cloud Peering](https://cloud.google.com/vpc/docs/using-vpc-peering)

Cloud peering n'est pas un service GCP, mais vous pouvez l'utiliser pour connecter votre réseau au réseau de Google et accéder à des services comme Youtube, Drive ou les services GCP.

Un cas d'utilisation courant est lorsque vous devez vous connecter à Google mais ne souhaitez pas le faire via Internet public.

### **Autres services réseau**

#### [Load Balancers (LB)](https://cloud.google.com/load-balancing/docs/load)

Dans GCP, les équilibreurs de charge sont des logiciels qui distribuent les requêtes des utilisateurs parmi un groupe d'instances.

Un équilibreur de charge peut avoir plusieurs backends associés, avec des règles pour décider du backend approprié pour une requête donnée.

Il existe différents types d'équilibreurs de charge. Ils diffèrent par le type de trafic (HTTP vs TCP/UDP - Couche 7 ou Couche 4), s'ils gèrent le trafic externe ou interne, et si leur portée est régionale ou mondiale :

* **HTTP(s)**. LB global qui gère les requêtes HTTP(s), distribuant le trafic vers plusieurs régions en fonction de l'emplacement de l'utilisateur (vers la région la plus proche avec des instances disponibles) ou des mappages d'URL (le LB peut être configuré pour transférer les requêtes vers _URL/news_ à un service backend et _URL/videos_ à un autre). Il peut recevoir à la fois du trafic IPv4 et IPv6 (mais celui-ci est terminé au niveau du LB et proxyfié en IPv4 vers les backends) et a une prise en charge native des WebSockets.
* **SSL Proxy LB**. **Global** LB qui gère le trafic TCP chiffré, gérant les certificats SSL pour vous.
* **TCP Proxy LB**. **Global** LB qui gère le trafic TCP non chiffré. Comme SSL Proxy LB, par défaut, il ne conservera pas l'IP du client, mais cela peut être changé.
* **Network Load Balancer**. LB régional qui gère le trafic TCP/UDP externe, basé sur l'adresse IP et le port.
* **Internal Load Balancer**. Comme un Network LB, mais pour le trafic interne.

Pour les apprenants visuels :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/lb.svg)

#### [Cloud DNS](https://cloud.google.com/dns/docs)

Cloud DNS est l'hôte géré de Google pour le [Domain Name System (DNS)](https://en.wikipedia.org/wiki/Domain_Name_System), à la fois pour le trafic interne et externe (public). Il mappera les URL comme [https://www.freecodecamp.org/](https://www.freecodecamp.org/) à une adresse IP. C'est le seul service dans GCP avec un SLA de 100 % - il est disponible 100 % du temps.

#### [Google Cloud CDN](https://cloud.google.com/cdn/docs)

Cloud DNS est le [Content Delivery Network](https://en.wikipedia.org/wiki/Content_delivery_network) de Google. Si vous avez des données qui ne changent pas souvent (images, vidéos, CSS, etc.), il est logique de les mettre en cache près de vos utilisateurs. Cloud CDN fournit 90 Points de Présence Edge (POP) pour mettre en cache les données près de vos utilisateurs finaux.

Après la première requête, les données statiques peuvent être stockées dans un POP, généralement beaucoup plus proche de votre utilisateur que vos serveurs principaux. Ainsi, dans les requêtes suivantes, vous pouvez récupérer les données plus rapidement depuis le POP et réduire la charge sur vos serveurs backend.

## **Où pouvez-vous exécuter vos applications dans GCP ?**

Je vais présenter 4 endroits où votre code peut s'exécuter dans GCP :

* Google Compute Engine
* Google Kubernetes Engine
* App Engine
* Cloud Functions

![Image](https://www.freecodecamp.org/news/content/images/2020/10/gce.png)

**Note** : il existe une 5ème option : Firebase est la plateforme mobile de Google qui vous aide à développer rapidement des applications.

### **[Compute Engine (GCE)](https://cloud.google.com/compute/docs)**

Compute Engine vous permet de lancer des machines virtuelles dans GCP. Cette section sera plus longue car GCE fournit l'infrastructure où GKE et GAE s'exécutent.

Dans l'introduction, j'ai parlé des différents types de VM que vous pouvez créer dans GCE. Maintenant, je vais couvrir où stocker les données, comment les sauvegarder et comment créer des instances avec toutes les données et la configuration dont vous avez besoin.

#### Où stocker les données de votre VM : disques

Vos données peuvent être stockées sur des **disques persistants**, des **SSD locaux** ou dans **Cloud Storage**.

##### **[Disque persistant](https://cloud.google.com/persistent-disk)**

Les disques persistants fournissent un stockage par blocs durable et fiable. Ils ne sont pas locaux à la machine. Ils sont plutôt attachés au réseau, ce qui a ses avantages et ses inconvénients :

* Les disques peuvent être redimensionnés, attachés ou détachés d'une VM même si l'instance est en cours d'utilisation.
* Ils ont une haute fiabilité.
* Les disques peuvent survivre à l'instance après sa suppression.
* Si vous avez besoin de plus d'espace, il suffit d'attacher plus de disques.
* Les disques plus grands offriront des performances plus élevées.
* Étant attachés au réseau, ils sont moins performants que les options locales. Les disques persistants SSD sont également disponibles pour les charges de travail plus exigeantes.

Chaque instance aura besoin d'un disque de démarrage et il doit être de ce type.

##### **[SSD local](https://cloud.google.com/local-ssd)**

Les SSD locaux sont attachés à une VM à laquelle ils fournissent un stockage éphemère haute performance. À l'heure actuelle, vous pouvez attacher jusqu'à huit SSD locaux de 375 Go à la même instance. Cependant, ces données seront perdues si la VM est tuée.

Les SSD locaux ne peuvent être attachés à une machine que lors de sa création, mais vous pouvez attacher à la fois des SSD locaux et des disques persistants à la même machine.

Les deux types de disques sont des ressources zonales.

##### **Cloud Storage**

Nous avons largement couvert GCS dans une section précédente. GCS n'est pas un système de fichiers, mais vous pouvez utiliser [GCS-Fuse](https://cloud.google.com/storage/docs/gcs-fuse) pour monter des buckets GCS en tant que systèmes de fichiers dans les systèmes Linux ou macOS. Vous pouvez également laisser les applications télécharger et téléverser des données vers GCS en utilisant la sémantique standard des systèmes de fichiers.

#### Comment sauvegarder les données de votre VM : Instantanés

Les instantanés sont des sauvegardes de vos disques. Pour réduire l'espace, ils sont créés de manière incrémentielle :

* La sauvegarde 1 contient tout le contenu de votre disque
* La sauvegarde 2 ne contient que les données qui ont changé depuis la sauvegarde 1
* La sauvegarde 3 ne contient que les données qui ont changé depuis la sauvegarde 2, et ainsi de suite

Cela suffit pour restaurer l'état de votre disque.

Bien que les instantanés puissent être pris sans arrêter l'instance, il est préférable de réduire son activité, d'arrêter d'écrire des données sur le disque et de vider les tampons. Cela vous aide à vous assurer que vous obtenez une représentation précise du contenu du disque.

#### [Images](https://cloud.google.com/compute/docs/images)

Les images font référence aux images du système d'exploitation nécessaires pour créer des disques de démarrage pour vos instances. Il existe deux types d'images :

* **Images publiques**. Elles sont fournies et maintenues par Google, les communautés open source et les vendeurs tiers. Prêtes à être utilisées dès que vous créez votre projet. Disponibles pour tous
* **Images personnalisées**. Images que vous avez créées.
* Elles sont liées au projet dans lequel vous les avez créées, mais vous pouvez les partager avec d'autres projets.
* Vous pouvez créer des images à partir de **disques persistants** et **d'autres images**, à la fois du même projet ou partagées depuis un autre projet.
* Les images liées peuvent être regroupées en **familles d'images** pour simplifier la gestion des différentes versions d'images.
* Pour les images basées sur Linux, vous pouvez également les partager en les exportant vers Cloud Storage sous forme de fichier tar.gz.

Vous vous demandez peut-être quelle est la différence entre une image et un instantané. Principalement, **leur but**. Les instantanés sont pris comme des sauvegardes incrémentielles d'un disque tandis que les images sont créées pour lancer de nouvelles machines virtuelles et configurer des modèles d'instances.

**Note sur les images vs les scripts de démarrage :**

Pour les configurations simples, les scripts de démarrage sont également une option. Ils peuvent être utilisés pour tester rapidement les changements, mais les VM mettront plus de temps à être prêtes par rapport à l'utilisation d'une image où tous les logiciels nécessaires sont installés, configurés, etc.

#### Groupes d'instances

Les groupes d'instances vous permettent de traiter un groupe d'instances comme une seule unité et ils se déclinent en deux versions :

* **Groupe d'instances non géré**. Formé par un groupe hétérogène d'instances nécessitant des paramètres de configuration individuels.
* **Groupe d'instances géré (MIG)**. C'est l'option préférée lorsque cela est possible. Toutes les machines se ressemblent, ce qui facilite leur configuration, leur création dans plusieurs zones (haute disponibilité), leur remplacement si elles deviennent non saines (auto-guérison), l'équilibrage du trafic entre elles et la création de nouvelles instances si le trafic augmente (mise à l'échelle horizontale).

Pour créer des MIG, vous devez définir un **modèle d'instance**, en spécifiant votre type de machine, votre zone, votre image OS, vos scripts de démarrage et d'arrêt, etc. Les modèles d'instances sont immuables.

Pour mettre à jour un MIG, vous devez créer un nouveau modèle et utiliser le **Managed Instance Group Updated** pour déployer la nouvelle version sur chaque machine du groupe.

Cette fonctionnalité peut être utilisée pour créer des [tests canari](https://martinfowler.com/bliki/CanaryRelease.html), en déployant vos changements sur une petite fraction de vos machines en premier.

Visitez ce [lien](https://cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups) pour en savoir plus sur les recommandations de Google pour garantir qu'une application déployée via un groupe d'instances géré peut gérer la charge même si une zone entière tombe en panne.

#### Bonnes pratiques de sécurité pour GCE

Pour augmenter la sécurité de votre infrastructure dans GCE, consultez :

* [VM blindées](https://cloud.google.com/security/shielded-cloud/shielded-vm)
* [Empêcher les instances d'être atteintes depuis Internet public](https://cloud.google.com/solutions/connecting-securely)
* [Images de confiance](https://cloud.google.com/compute/docs/images/restricting-image-access#:~:text=Use the Trusted image feature,images%2C disks%2C and snapshots.) pour vous assurer que vos utilisateurs ne peuvent créer des disques qu'à partir d'images dans des **projets spécifiques**

### **[App Engine](https://cloud.google.com/appengine/docs)**

App Engine est un excellent choix lorsque vous souhaitez vous concentrer sur le code et laisser Google gérer votre infrastructure. Vous devez simplement choisir la région où votre application sera déployée (ceci ne peut pas être changé une fois qu'il est défini). Parmi ses principaux cas d'utilisation figurent les sites web, les applications mobiles et les backends de jeux.

Vous pouvez facilement mettre à jour la version de votre application qui est en cours d'exécution via la ligne de commande ou la console Google.

De plus, si vous devez déployer une mise à jour risquée de votre application, vous pouvez diviser le trafic entre les anciennes et les nouvelles versions pour un déploiement canari. Une fois que vous êtes satisfait des résultats, vous pouvez router tout le trafic vers la nouvelle version.

Il existe deux environnements App Engine :

* **Standard**. Cette version peut rapidement monter ou descendre en puissance (même à zéro instance) pour s'adapter à la demande. Actuellement, seuls quelques langages de programmation sont pris en charge (Go, Java, PHP et Python) et vous n'avez pas accès à un VPC (y compris les connexions VPN). Il peut être réduit à zéro instance.
* **Flexible**. Votre code s'exécute dans des conteneurs Docker dans GCE, d'où une plus grande flexibilité que l'environnement Standard. Cependant, la création de nouvelles instances est plus lente et il ne peut pas être réduit à zéro instance. Il est adapté à un trafic plus constant.

Quelle que soit l'environnement, il n'y a pas de coûts initiaux et vous ne payez que pour ce que vous utilisez (facturé à la seconde).

**Memcache** est intégré à App Engine, vous donnant la possibilité de choisir entre un cache **partagé** (option par défaut, gratuite) ou un cache **dédié** pour de meilleures performances.

Visitez ce lien pour en savoir plus sur les [bonnes pratiques](https://cloud.google.com/appengine/docs/standard/java/memcache#best_practices) que vous devriez suivre pour maximiser les performances de votre application.

### **[Google Kubernetes Engine (GKE)](https://cloud.google.com/kubernetes-engine/docs)**

[Kubernetes](https://kubernetes.io/) est un système d'orchestration de conteneurs **open-source**, développé par Google.

Kubernetes est un sujet très vaste en soi et je ne le couvrirai pas ici. Vous devez simplement savoir que GKE facilite l'exécution et la gestion de vos clusters Kubernetes sur GCP.

Google fournit également [Container Registry](https://cloud.google.com/container-registry) pour stocker vos images de conteneurs - pensez-y comme votre Docker Hub privé.

**Note** : Vous pouvez utiliser [Cloud Build](https://cloud.google.com/cloud-build/docs) pour exécuter vos builds dans GCP et, entre autres, produire des images Docker et les stocker dans Container Registry. Cloud Build peut importer votre code depuis Google Cloud Storage, [Cloud Source Repository](https://cloud.google.com/source-repositories/docs), GitHub ou Bitbucket.

### **[Cloud Functions](https://cloud.google.com/functions/docs)**

Cloud Functions sont l'équivalent des fonctions Lambda dans AWS. Les fonctions Cloud sont **sans serveur**. Elles vous permettent de vous concentrer sur le code et de ne pas vous soucier de l'infrastructure sur laquelle il va s'exécuter.

Avec Cloud Functions, il est **facile de répondre aux événements** tels que les téléchargements vers un bucket GCS ou les messages dans un sujet Pub/Sub. Vous n'êtes facturé que pour le temps pendant lequel votre fonction s'exécute en réponse à un événement.

## **Comment travailler avec le Big Data dans GCP**

### **[BigQuery](https://cloud.google.com/bigquery/docs/)**

![Image](https://www.freecodecamp.org/news/content/images/2020/10/bigq.png)

BigQuery est l'entrepôt de données serverless de Google et fournit des capacités d'analyse pour les bases de données à l'échelle du pétaoctet.

BigQuery sauvegarde automatiquement vos tables, mais vous pouvez toujours les exporter vers GCS pour être du bon côté - en encourant des coûts supplémentaires.

Les données peuvent être ingérées par lots (par exemple, depuis un bucket GCS) ou depuis un flux dans plusieurs formats : CSV, JSON, Parquet ou Avro (le plus performant). De plus, vous pouvez interroger des données qui résident dans des sources externes, appelées sources fédérées, par exemple, des buckets GCS.

Vous pouvez interagir avec vos données dans BigQuery en utilisant SQL via

* La console Google.
* La [ligne de commande](https://cloud.google.com/bigquery/docs/bq-command-line-tool), en exécutant des commandes comme `bq query 'SELECT field FROM ....`
* L'API REST.
* Le code utilisant des bibliothèques clientes.

Les [fonctions définies par l'utilisateur](https://cloud.google.com/bigquery/docs/reference/standard-sql/user-defined-functions) vous permettent de combiner des requêtes SQL avec des fonctions JavaScript pour créer des opérations complexes.

BigQuery est un magasin de données colonnaire : les enregistrements sont stockés dans des colonnes. Les tables sont des collections de colonnes et les ensembles de données sont des collections de tables.

Les travaux sont des actions pour charger, exporter, interroger ou copier des données que BigQuery exécute pour vous.

Les vues sont des tables virtuelles définies par une requête SQL et sont utiles pour partager des données avec d'autres lorsque vous souhaitez contrôler exactement ce à quoi ils ont accès.

Deux concepts importants liés aux tables sont :

* **Tables partitionnées**. Pour limiter la quantité de données qui doivent être interrogées, les tables peuvent être divisées en partitions. Cela peut être fait en fonction du temps d'ingestion ou en incluant une colonne de timestamp ou de date ou une plage d'entiers. De cette manière, il est facile d'interroger certaines périodes sans interroger la table complète. Pour réduire les coûts, vous pouvez définir une période d'expiration après laquelle la partition sera supprimée.
* [**Tables clusterisées**](https://cloud.google.com/bigquery/docs/clustered-tables). Les données sont clusterisées par colonne (par exemple, order_id). Lorsque vous interrogez votre table, seules les lignes associées à cette colonne seront lues. BigQuery effectuera ce clustering automatiquement en fonction d'une ou plusieurs colonnes.

En utilisant les rôles IAM, vous pouvez contrôler l'accès au niveau du projet, de l'ensemble de données ou de la vue, mais _pas au niveau de la table_. Les rôles sont complexes pour BigQuery, donc je recommande de consulter la [documentation](https://cloud.google.com/bigquery/docs/access-control#predefined_roles_comparison_matrix).

Par exemple, le rôle jobUser ne vous permet que d'exécuter des travaux tandis que le rôle user vous permet d'exécuter des travaux et de créer des ensembles de données (mais pas des tables).

Vos coûts dépendent de la quantité de données que vous stockez et diffusez dans BigQuery et de la quantité de données que vous interrogez. Pour réduire les coûts, BigQuery met automatiquement en cache les requêtes précédentes (par utilisateur). Ce comportement peut être désactivé.

Lorsque vous ne modifiez pas les données pendant 90 jours, elles sont automatiquement déplacées vers une classe de stockage moins chère. Vous payez pour ce que vous utilisez, mais il est possible d'opter pour un tarif forfaitaire (uniquement si vous avez besoin de plus de 2000 [slots](https://cloud.google.com/bigquery/docs/slots) qui sont alloués par défaut).

Consultez ces liens pour voir comment [optimiser vos performances](https://cloud.google.com/bigquery/docs/best-practices-performance-overview) et [coûts](https://cloud.google.com/blog/products/data-analytics/cost-optimization-best-practices-for-bigquery).

### **[Cloud Pub/Sub](https://cloud.google.com/pubsub/docs)**

Pub/Sub est la **file d'attente de messages entièrement gérée** de Google, vous permettant de découpler les éditeurs (ajoutant des messages à la file d'attente) et les abonnés (consommant des messages de la file d'attente).

Bien qu'il soit similaire à [Kafka](https://kafka.apache.org/), Pub/Sub n'est pas un substitut direct. Ils peuvent être combinés dans le même pipeline (Kafka déployé sur site ou même dans GKE). Il existe des plugins open-source pour connecter Kafka à GCP, comme [Kafka Connect](https://www.confluent.io/hub/confluentinc/kafka-connect-gcp-pubsub).

Pub/Sub garantit que chaque message sera livré au moins une fois, mais il ne garantit pas que les messages seront traités dans l'ordre. Il est généralement connecté à Dataflow pour traiter les données, s'assurer que les messages sont traités dans l'ordre, etc.

Pub/Sub prend en charge les modes push et pull :

* **Push.** Les messages sont envoyés aux abonnés, ce qui entraîne une latence plus faible.
* **Pull.** Les abonnés tirent les messages des sujets, mieux adapté à un grand volume de messages.

### **Cloud Pub/Sub vs Cloud Task**

[Cloud Tasks](https://cloud.google.com/tasks/docs) est un autre service entièrement géré pour exécuter des tâches de manière asynchrone et gérer les messages entre les services. Cependant, il existe des différences entre Cloud Tasks et Pub/Sub :

* Dans Pub/Sub, les éditeurs et les abonnés sont découplés. Les éditeurs ne savent rien de leurs abonnés. Lorsqu'ils publient un message, ils provoquent implicitement une ou plusieurs réactions des abonnés à un événement de publication.
* Dans Cloud Tasks, l'éditeur reste en contrôle de l'exécution. De plus, Cloud Tasks fournit d'autres fonctionnalités non disponibles pour Pub/Sub comme la planification de temps de livraison spécifiques, les contrôles de taux de livraison, les nouvelles tentatives configurables, l'accès et la gestion des tâches individuelles dans une file d'attente, la déduplication de la création de tâches/messages.

Pour plus de détails, consultez ce [lien](https://cloud.google.com/tasks/docs/comp-pub-sub).

### **[Cloud Dataflow](https://cloud.google.com/dataflow/docs/)**

Cloud Dataflow est le service géré de Google pour le **traitement de données en flux continu et par lots**, basé sur [Apache Beam](https://beam.apache.org/documentation/).

Vous pouvez définir des pipelines qui transformeront vos données, par exemple avant qu'elles ne soient ingérées dans un autre service comme BigQuery, BigTable ou Cloud ML. Le même pipeline peut traiter à la fois des données en flux continu et par lots.

Un schéma courant consiste à diffuser des données dans Pub/Sub, disons depuis des [appareils IoT](https://cloud.google.com/solutions/iot), à les traiter dans Dataflow et à les stocker pour analyse dans BigQuery.

Mais Pub/Sub ne garantit pas que l'ordre dans lequel les messages sont poussés vers les sujets sera l'ordre dans lequel les messages sont consommés. Cependant, cela peut être fait avec Dataflow.

### **[Cloud Dataproc](https://cloud.google.com/dataproc/docs)**

Cloud Dataproc est l'écosystème Hadoop et Spark géré par Google. Il vous permet de créer et de gérer vos clusters facilement et de les éteindre lorsque vous ne les utilisez pas, pour réduire les coûts.

Dataproc ne peut être utilisé que pour traiter des données par lots, tandis que Dataflow peut gérer également des données en streaming.

Google recommande d'utiliser Dataproc pour une migration lift and leverage de vos clusters Hadoop sur site vers le cloud :

* Réduire les coûts en éteignant votre cluster lorsque vous ne l'utilisez pas.
* Tirer parti de l'infrastructure de Google
* Utiliser certaines machines virtuelles préemptibles pour réduire les coûts
* Ajouter des disques persistants plus grands (SSD) pour améliorer les performances
* BigQuery peut remplacer Hive et BigTable peut remplacer HBase
* Cloud Storage remplace HDFS. Il suffit de télécharger vos données vers GCS et de changer les préfixes hdfs:// en gs://

Sinon, vous devriez choisir Cloud Dataflow.

### **[Dataprep](https://cloud.google.com/dataprep/docs)**

Cloud Dataprep vous fournit une **interface basée sur le web pour nettoyer et préparer vos données** avant le traitement. Les formats d'entrée et de sortie incluent, entre autres, CSV, JSON et Avro.

Après avoir défini les transformations, un travail Dataflow s'exécutera. Les données transformées peuvent être exportées vers GCS, BigQuery, etc.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/proc.svg)

### **[Cloud Composer](https://cloud.google.com/composer/docs)**

Cloud Composer est le service entièrement géré d'Apache Airflow de Google pour créer, planifier, surveiller et gérer des flux de travail. Il gère toute l'infrastructure pour vous afin que vous puissiez vous concentrer sur la combinaison des services que j'ai décrits ci-dessus pour créer vos propres flux de travail.

Sous le capot, un cluster GKE sera créé avec Airflow et GCS sera utilisé pour stocker les fichiers.

### **[IA et Machine Learning dans GCP](https://cloud.google.com/products/ai)**

Couvrir les bases du machine learning prendrait un autre article. Donc ici, je suppose que vous êtes familier avec cela et je vais vous montrer comment entraîner et déployer vos modèles dans GCP.

Nous examinerons également quelles API sont disponibles pour tirer parti des capacités de machine learning de Google dans vos services, même si vous n'êtes pas un expert dans ce domaine.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/AI.jpg)

#### [AI Platform](https://cloud.google.com/ai-platform/docs)

AI Platform vous fournit une **plateforme entièrement gérée** pour utiliser des bibliothèques de machine learning comme [Tensorflow](https://www.tensorflow.org/). Vous devez simplement vous concentrer sur votre modèle et Google gérera toute l'infrastructure nécessaire pour l'entraîner.

Une fois votre modèle entraîné, vous pouvez l'utiliser pour obtenir des prédictions en ligne et par lots.

#### [Cloud AutoML](https://cloud.google.com/automl)

Google vous permet d'utiliser **vos données pour entraîner leurs modèles**. Vous pouvez exploiter des modèles pour construire des applications basées sur le traitement du langage naturel (par exemple, des applications de classification de documents ou d'analyse de sentiments), le traitement de la parole, la traduction automatique ou le traitement vidéo (classification vidéo ou détection d'objets).

## **Comment explorer et visualiser vos données dans GCP**

### **[Cloud Data Studio](https://cloud.google.com/bigquery/docs/visualize-data-studio)**

Data Studio vous permet de créer des **visualisations et des tableaux de bord** basés sur des données qui résident dans les services Google (YouTube Analytics, Sheets, AdWords, téléchargement local), Google Cloud Platform (BigQuery, Cloud SQL, GCS, Spanner) et de nombreux services tiers, en stockant vos rapports dans Google Drive.

Data Studio ne fait pas partie de GCP, mais de **G-Suite**, donc ses permissions ne sont pas gérées en utilisant IAM.

Il n'y a pas de coûts supplémentaires pour utiliser Data Studio, autres que le stockage des données, les requêtes dans BigQuery, etc. Le **cache** peut être utilisé pour améliorer les performances et réduire les coûts.

### **[Cloud Datalab](https://cloud.google.com/datalab/docs)**

Datalab vous permet d'**explorer, analyser et visualiser des données** dans BigQuery, ML Engine, Compute Engine, Cloud Storage et Stackdriver.

Il est basé sur des notebooks Jupyter et prend en charge le code Python, SQL et Javascript. Vos notebooks peuvent être partagés via le Cloud Source Repository.

Cloud Datalab lui-même est gratuit, mais il créera une machine virtuelle dans GCE pour laquelle vous serez facturé.

## **[Sécurité dans GCP](https://cloud.google.com/security/)**

![Image](https://www.freecodecamp.org/news/content/images/2020/10/sec.jpg)

### **Chiffrement sur Google Cloud Platform**

Google Cloud chiffre les données à la fois au repos (données stockées sur disque) et en transit (données voyageant dans le réseau), en utilisant [AES](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) implémenté via [Boring SSL](https://boringssl.googlesource.com/boringssl/).

Vous pouvez gérer les clés de chiffrement vous-même (en les stockant dans GCP ou sur site) ou laisser Google les gérer.

#### [Chiffrement au repos](https://cloud.google.com/security/encryption-at-rest/default-encryption)

GCP chiffre les données stockées au repos **par défaut**. Vos données seront divisées en morceaux. Chaque morceau est distribué sur différentes machines et chiffré avec une clé unique, appelée **clé de chiffrement de données (DEK)**.

Les clés sont générées et gérées par Google, mais vous pouvez également gérer les clés vous-même, comme nous le verrons plus tard dans ce guide.

#### [Chiffrement en transit](https://cloud.google.com/security/encryption-in-transit)

Pour ajouter une couche de sécurité supplémentaire, toutes les communications entre deux services GCP ou depuis votre infrastructure vers GCP sont chiffrées à une ou plusieurs couches réseau. Vos données ne seraient pas compromises si vos messages étaient interceptés.

### **[Cloud Key Management Service (KMS)](https://cloud.google.com/kms/docs)**

Comme je l'ai mentionné précédemment, vous pouvez laisser Google gérer les clés pour vous ou vous pouvez les gérer vous-même.

Google KMS est le service qui vous permet de **gérer vos clés de chiffrement**. Vous pouvez créer, faire tourner et détruire des clés de chiffrement symétriques. Toutes les activités liées aux clés sont enregistrées dans les journaux. Ces clés sont appelées **clés de chiffrement gérées par le client**.

Dans GCS, elles sont utilisées pour [chiffrer](https://cloud.google.com/storage/docs/encryption/customer-managed-keys#:~:text=Data%20Encryption%20Options.-,Overview,are%20stored%20within%20Cloud%20KMS.) :

* Les données de l'objet.
* La somme de contrôle CRC32C de l'objet.
* Le hachage MD5 de l'objet.

Et Google utilise des clés côté serveur pour gérer le reste des métadonnées, y compris le nom de l'objet.

Les DEK utilisés pour chiffrer vos données sont également chiffrés à l'aide de clés de chiffrement de clés (KEK), dans un processus appelé chiffrement d'enveloppe. Par défaut, les KEK sont tournés tous les 90 jours.

Il est important de noter que KMS ne stocke pas de secrets. KMS est un dépôt central pour les KEK. Seules les clés dont GCP a besoin pour chiffrer les secrets qui sont stockés ailleurs, par exemple dans [Gestion des secrets](https://cloud.google.com/solutions/secret-manager/).

**Note** : Pour GCE et GCS, vous avez la possibilité de garder vos clés sur site et de laisser Google les récupérer pour chiffrer et déchiffrer vos données. Celles-ci sont connues sous le nom de **clés fournies par le client**.

### **[Identity-Aware Proxy (IAP)](https://cloud.google.com/iap/docs)**

Identity-Aware Proxy vous permet de **contrôler l'accès** aux applications GCP via HTTPS sans installer de logiciel VPN ou ajouter de code supplémentaire dans votre application pour gérer la connexion.

Vos applications sont visibles sur l'Internet public, mais accessibles uniquement aux utilisateurs autorisés, mettant en œuvre un modèle d'accès de sécurité zéro confiance.

De plus, avec le transfert TCP, vous pouvez empêcher des services comme SSH d'être exposés sur l'Internet public.

### **[Cloud Armor](https://cloud.google.com/armor/docs)**

Cloud Armor protège votre infrastructure contre les attaques par [déni de service distribué (DDoS)](https://en.wikipedia.org/wiki/Denial-of-service_attack). Vous définissez des règles (par exemple, pour mettre sur liste blanche ou refuser certaines adresses IP ou plages CIDR) pour créer des politiques de sécurité, qui sont appliquées au niveau du Point de Présence (plus proche de la source de l'attaque).

Cloud Armor vous donne la possibilité de prévisualiser les effets de vos politiques avant de les activer.

### **[Cloud Data Loss Prevention](https://cloud.google.com/dlp/docs)**

Data Loss Prevention est un service entièrement géré conçu pour vous aider à découvrir, classer et protéger les données sensibles, comme :

* **Informations personnelles identifiables (PII)** : nom, numéro de sécurité sociale, numéro de permis de conduire, numéro de compte bancaire, numéro de passeport, adresse e-mail, etc.
* **Secrets**
* **Identifiants**

DLP est intégré avec GCS, BigQuery et Datastore. De plus, la source des données peut être en dehors de GCP.

Vous pouvez spécifier le type de données qui vous intéresse, appelé type d'info, définir vos propres types (basés sur des dictionnaires de mots et de phrases ou basés sur des expressions regex), ou laisser Google utiliser le type par défaut qui peut être chronophage pour de grandes quantités de données.

Pour chaque résultat, DLP retournera la probabilité que cette donnée corresponde à un certain type d'info : LIKELIHOOD_UNSPECIFIED, VERY_UNLIKELY, UNLIKELY, POSSIBLE, LIKELY, VERY_LIKELY.

Après avoir détecté une PII, DLP peut la transformer de sorte qu'elle ne puisse pas être mappée à l'utilisateur. DLP utilise plusieurs techniques pour désidentifier vos données sensibles comme la tokenisation, le bucketing et le décalage de date. DLP peut détecter et masquer les données sensibles dans les images également.

### **[VPC Service Control](https://cloud.google.com/vpc-service-controls/docs/overview)**

VPC Service Control aide à prévenir l'exfiltration de données. Il vous permet de définir un périmètre autour des ressources que vous souhaitez protéger. Vous pouvez définir quels services et depuis quels réseaux ces ressources peuvent être accessibles.

### **[Cloud Web Security Scanner](https://cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview)**

Cloud Web Security Scanner analyse les applications exécutées dans Compute Engine, GKE et App Engine pour détecter les vulnérabilités courantes telles que les mots de passe en texte clair, les en-têtes invalides, les bibliothèques obsolètes et les [attaques par script inter-sites](https://en.wikipedia.org/wiki/Cross-site_scripting). Il simule un utilisateur réel essayant de cliquer sur vos boutons, de saisir du texte dans vos champs de texte, etc.

Il fait partie du [Cloud Security Command Center](https://cloud.google.com/security-command-center/docs).

## **Plus de ressources GCP**

* [Google Cloud Solutions Architecture Reference](https://gcp.solutions/)
* [Solutions GCP par secteur](https://cloud.google.com/solutions/#section-1)
* [Chaîne YouTube GCP](https://www.youtube.com/user/googlecloudplatform)
* [Labs GCP](https://cloud.google.com/training/free-labs)

Si vous êtes intéressé à en apprendre davantage sur GCP, je recommande de consulter les examens pratiques gratuits pour les différentes certifications. Que vous vous prépariez à une certification GCP ou non, vous pouvez les utiliser pour trouver des lacunes dans vos connaissances :

* [Développeur Cloud Professionnel](https://cloud.google.com/certification/sample-questions/cloud-developer)
* [Ingénieur de données Cloud Professionnel](https://cloud.google.com/certification/sample-questions/clouddata-engineer)
* [Ingénieur réseau Cloud Professionnel](https://cloud.google.com/certification/sample-questions/cloud-network-engineer)
* [Ingénieur de sécurité Cloud Professionnel](https://cloud.google.com/certification/sample-questions/cloud-security-engineer)
* [Ingénieur DevOps Cloud Professionnel](https://cloud.google.com/certification/sample-questions/cloud-devops-engineer)
* [Ingénieur en machine learning Cloud Professionnel](https://cloud.google.com/certification/sample-questions/cloud-devops-engineer)
* [Architecte Cloud Professionnel](https://cloud.google.com/certification/sample-questions/cloud-architect)

**Note** : Certaines questions sont basées sur des études de cas. Les liens vers les études de cas seront fournis dans les examens afin que vous ayez le contexte complet pour bien comprendre et répondre à la question.

## **Il est temps de tester vos connaissances**

J'ai extrait 10 questions de certains des examens ci-dessus. Certaines d'entre elles sont assez simples. D'autres nécessitent une réflexion approfondie et de décider quelle est la meilleure solution lorsque plus d'une option est une solution viable.

### **Question 1**

Votre client déplace ses applications d'entreprise vers Google Cloud. L'équipe de sécurité souhaite avoir une visibilité détaillée de toutes les ressources de l'organisation. Vous utilisez le Resource Manager pour vous configurer en tant qu'administrateur de l'organisation.

Quels rôles Cloud Identity and Access Management (Cloud IAM) devez-vous attribuer à l'équipe de sécurité tout en suivant les pratiques recommandées de Google ?

A. Organisation viewer, Project owner

B. Organisation viewer, Project viewer

C. Organisation administrator, Project browser

D. Project owner, Network administrator

### **Question 2**

Votre entreprise souhaite essayer le cloud avec un risque faible. Ils souhaitent archiver environ 100 To de leurs données de journal dans le cloud et tester les fonctionnalités d'analyse serverless disponibles là-bas, tout en conservant ces données comme sauvegarde de récupération après sinistre à long terme.

Quelles sont les deux étapes qu'ils doivent suivre ? (Choisissez deux)

A. Charger les journaux dans BigQuery.

B. Charger les journaux dans Cloud SQL.

C. Importer les journaux dans Cloud Logging.

D. Insérer les journaux dans Cloud Bigtable.

E. Télécharger les fichiers de journal dans Cloud Storage.

### **Question 3**

Votre entreprise souhaite suivre si quelqu'un est présent dans une salle de réunion réservée pour une réunion planifiée.

Il y a 1000 salles de réunion réparties dans 5 bureaux sur 3 continents. Chaque salle est équipée d'un capteur de mouvement qui signale son état chaque seconde.

Vous souhaitez répondre aux besoins d'ingestion de données de ce réseau de capteurs. L'infrastructure de réception doit tenir compte de la possibilité que les appareils puissent avoir une connectivité incohérente.

Quelle solution devez-vous concevoir ?

A. Faire en sorte que chaque appareil crée une connexion persistante à une instance Compute Engine et écrive des messages à une application personnalisée.

B. Faire en sorte que les appareils sondent la connectivité à Cloud SQL et insèrent les derniers messages à intervalles réguliers dans une table spécifique à l'appareil.

C. Faire en sorte que les appareils sondent la connectivité à Cloud Pub/Sub et publient les derniers messages à intervalles réguliers dans un sujet partagé pour tous les appareils.

D. Faire en sorte que les appareils créent une connexion persistante à une application App Engine frontale par Cloud Endpoints, qui ingère les messages et les écrit dans Cloud Datastore.

### **Question 4**

Pour réduire les coûts, le Directeur de l'Ingénierie a exigé que tous les développeurs déplacent leurs ressources d'infrastructure de développement des machines virtuelles (VM) sur site vers Google Cloud.

Ces ressources subissent plusieurs événements de démarrage/arrêt au cours de la journée et nécessitent que l'état persiste.

On vous a demandé de concevoir le processus d'exécution d'un environnement de développement dans Google Cloud tout en fournissant une visibilité des coûts au département financier.

Quelles sont les deux étapes que vous devez suivre ? (Choisissez deux)

A. Utiliser des disques persistants pour stocker l'état. Démarrer et arrêter la VM selon les besoins.

B. Utiliser le drapeau --auto-delete sur tous les disques persistants avant d'arrêter la VM.

C. Appliquer l'étiquette d'utilisation du CPU de la VM et l'inclure dans l'exportation de facturation BigQuery.

D. Utiliser l'exportation de facturation BigQuery et les étiquettes pour relier les coûts aux groupes.

E. Stocker tout l'état dans un SSD local, prendre un instantané des disques persistants et terminer la VM.

### **Question 5**

L'équipe d'administration de la base de données vous a demandé de les aider à améliorer les performances de leur nouveau serveur de base de données exécuté sur Compute Engine.

La base de données est utilisée pour importer et normaliser les statistiques de performance de l'entreprise. Elle est construite avec MySQL exécuté sur Debian Linux. Ils ont une machine virtuelle n1-standard-8 avec 80 Go de disque persistant SSD zonal qu'ils ne peuvent pas redémarrer avant le prochain événement de maintenance.

Que doivent-ils changer pour obtenir de meilleures performances de ce système dès que possible et de manière rentable ?

A. Augmenter la mémoire de la machine virtuelle à 64 Go.

B. Créer une nouvelle machine virtuelle exécutant PostgreSQL.

C. Redimensionner dynamiquement le disque persistant SSD à 500 Go.

D. Migrer leur entrepôt de métriques de performance vers BigQuery.

### **Question 6**

Votre organisation a une application web à 3 niveaux déployée dans le même Virtual Private Cloud (VPC) de Google Cloud.

Chaque niveau (web, API et base de données) est mis à l'échelle indépendamment des autres. Le trafic réseau doit circuler du web vers le niveau API, puis vers le niveau de la base de données. Le trafic ne doit pas circuler entre le web et le niveau de la base de données.

Comment devez-vous configurer le réseau avec un minimum d'étapes ?

A. Ajouter chaque niveau à un sous-réseau différent.

B. Configurer des pare-feux basés sur des logiciels sur des VM individuelles.

C. Ajouter des balises à chaque niveau et configurer des routes pour permettre le flux de trafic souhaité.

D. Ajouter des balises à chaque niveau et configurer des règles de pare-feu pour permettre le flux de trafic souhaité.

### **Question 7**

Vous développez une application sur Google Cloud qui étiquettera les monuments célèbres dans les photos des utilisateurs. Vous êtes sous pression concurrentielle pour développer rapidement un modèle prédictif. Vous devez garder les coûts du service bas.

Que devez-vous faire ?

A. Construire une application qui appelle l'API Cloud Vision. Inspecter les valeurs MID générées pour fournir les étiquettes d'image.

B. Construire une application qui appelle l'API Cloud Vision. Passer les emplacements des images client sous forme de chaînes encodées en base64.

C. Construire et entraîner un modèle de classification avec TensorFlow. Déployer le modèle en utilisant AI Platform Prediction. Passer les emplacements des images client sous forme de chaînes encodées en base64.

D. Construire et entraîner un modèle de classification avec TensorFlow. Déployer le modèle en utilisant AI Platform Prediction. Inspecter les valeurs MID générées pour fournir les étiquettes d'image.

### **Question 8**

Vous avez configuré un groupe d'instances géré avec mise à l'échelle automatique pour servir le trafic web pour un lancement à venir.

Après avoir configuré le groupe d'instances comme service backend pour un équilibreur de charge HTTP(S), vous remarquez que les instances de machines virtuelles (VM) sont terminées et relancées chaque minute. Les instances n'ont pas d'adresse IP publique.

Vous avez vérifié que la réponse web appropriée provient de chaque instance en utilisant la commande curl. Vous souhaitez vous assurer que le backend est configuré correctement.

Que devez-vous faire ?

A. Vérifier qu'une règle de pare-feu existe pour permettre au trafic source sur HTTP/HTTPS d'atteindre l'équilibreur de charge.

B. Attribuer une IP publique à chaque instance et configurer une règle de pare-feu pour permettre à l'équilibreur de charge d'atteindre l'IP publique de l'instance.

C. Vérifier qu'une règle de pare-feu existe pour permettre aux vérifications de santé de l'équilibreur de charge d'atteindre les instances dans le groupe d'instances.

D. Créer une balise sur chaque instance avec le nom de l'équilibreur de charge. Configurer une règle de pare-feu avec le nom de l'équilibreur de charge comme source et la balise de l'instance comme destination.

### **Question 9**

Vous avez créé un travail qui s'exécute quotidiennement pour importer des données hautement sensibles depuis un emplacement sur site vers Cloud Storage. Vous avez également configuré une insertion de données en streaming dans Cloud Storage via un nœud Kafka qui s'exécute sur une instance Compute Engine.

Vous devez chiffrer les données au repos et fournir votre propre clé de chiffrement. Votre clé ne doit pas être stockée dans Google Cloud.

Que devez-vous faire ?

A. Créer un compte de service dédié et utiliser le chiffrement au repos pour référencer vos données stockées dans Cloud Storage et les données Compute Engine dans le cadre de vos appels de service API.

B. Télécharger votre propre clé de chiffrement vers Cloud Key Management Service et l'utiliser pour chiffrer vos données dans Cloud Storage. Utiliser votre clé de chiffrement téléchargée et la référencer dans le cadre de vos appels de service API pour chiffrer vos données dans le nœud Kafka hébergé sur Compute Engine.

C. Télécharger votre propre clé de chiffrement vers Cloud Key Management Service et l'utiliser pour chiffrer vos données dans votre nœud Kafka hébergé sur Compute Engine.

D. Fournir votre propre clé de chiffrement et la référencer dans le cadre de vos appels de service API pour chiffrer vos données dans Cloud Storage et votre nœud Kafka hébergé sur Compute Engine.

### **Question 10**

Vous concevez un dépôt de données relationnelles sur Google Cloud pour croître selon les besoins. Les données seront cohérentes transactionnellement et ajoutées depuis n'importe quel endroit dans le monde. Vous souhaitez surveiller et ajuster le nombre de nœuds pour le trafic d'entrée, qui peut augmenter de manière imprévisible.

Que devez-vous faire ?

A. Utiliser Cloud Spanner pour le stockage. Surveiller l'utilisation du stockage et augmenter le nombre de nœuds si plus de 70 % sont utilisés.

B. Utiliser Cloud Spanner pour le stockage. Surveiller l'utilisation du CPU et augmenter le nombre de nœuds si plus de 70 % sont utilisés pour votre période de temps.

C. Utiliser Cloud Bigtable pour le stockage. Surveiller les données stockées et augmenter le nombre de nœuds si plus de 70 % sont utilisés.

D. Utiliser Cloud Bigtable pour le stockage. Surveiller l'utilisation du CPU et augmenter le nombre de nœuds si plus de 70 % sont utilisés pour votre période de temps.

#### Réponses

1. B
2. A, E
3. C
4. A, D
5. C
6. D
7. B
8. C
9. D
10. B

## **Retour à la proposition initiale**

Au début de cet article, j'ai dit que vous apprendriez à concevoir une plateforme d'analyse de jeux mobiles qui collecte, stocke et analyse de vastes quantités de télémétrie des joueurs, à la fois à partir de lots de données et d'événements en temps réel.

Alors, pensez-vous pouvoir le faire ?

Prenez un stylo et une feuille de papier et essayez de trouver votre propre solution basée sur les services que j'ai décrits ici. Si vous êtes bloqué, les questions suivantes pourraient vous aider :

* La plateforme doit collecter des événements en temps réel depuis le jeu :
* Où le jeu pourrait-il s'exécuter ?
* Comment pouvez-vous ingérer des données en streaming depuis le jeu vers GCP ?
* Comment pouvez-vous les stocker ?
* Comment pouvez-vous collecter et stocker les téléchargements de lots de données ?
* Pouvez-vous analyser toutes les données ingérées au fur et à mesure qu'elles arrivent ? Doivent-elles être traitées ?
* Quels services pouvez-vous utiliser pour analyser les données ? Comment cela changerait-il si la faible latence était maintenant une nouvelle exigence ?

J'ai délibérément défini le problème de manière très vague. C'est ce à quoi vous pouvez vous attendre lorsque vous êtes confronté à ce type de défi : l'incertitude. C'est à vous de recueillir les exigences et de documenter vos hypothèses.

Ne vous inquiétez pas si votre solution ne ressemble pas à celle de [Google](https://cloud.google.com/solutions/mobile/mobile-gaming-analysis-telemetry). Ce n'est qu'une solution possible. Apprendre à concevoir des systèmes complexes est une compétence qui prend une vie entière à maîtriser. Heureusement, vous êtes sur la bonne voie.

## **Conclusion**

Ce guide vous aidera à commencer avec GCP et vous donnera une perspective large de ce que vous pouvez faire avec.

En aucun cas vous ne serez un expert après avoir terminé ce guide, ou tout autre guide d'ailleurs. La seule façon d'apprendre vraiment est par la pratique.

**Vous allez apprendre infiniment plus en faisant qu'en lisant ou en regardant**. Je recommande fortement d'utiliser votre essai gratuit et les Code Labs si vous êtes sérieux dans l'apprentissage.

Vous pouvez visiter mon blog [www.yourdevopsguy.com](https://www.yourdevopsguy.com/) et [me suivre sur Twitter](https://twitter.com/CodingLanguages) pour plus de contenu technique de haute qualité.

**Avis de non-responsabilité** : Au moment de la publication de cet article, je ne travaille pas et n'ai jamais travaillé pour Google. Je voulais organiser et résumer les connaissances que j'ai acquises en apprenant via la documentation Google, les vidéos YouTube, les cours que j'ai suivis et surtout par la pratique quotidienne de GCP dans mon travail.

Toutes ces informations sont gratuites. Les chiffres, les nombres et les versions que vous voyez ici proviennent de la documentation au moment où je publie cet article. Pour vous assurer que vous utilisez des données à jour, veuillez consulter la documentation officielle.