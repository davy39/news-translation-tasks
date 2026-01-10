---
title: Comment sécuriser et gérer les secrets à l'aide de Google Cloud KMS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-07T22:22:23.000Z'
originalURL: https://freecodecamp.org/news/securing-managing-secrets-using-google-cloud-kms-3fe08c69f499
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_Cf1p5h7nfoNfo4wNswuNw.jpeg
tags:
- name: Google Cloud Platform
  slug: google-cloud-platform
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Comment sécuriser et gérer les secrets à l'aide de Google Cloud KMS
seo_desc: 'By Ramesh Lingappa

  Let’s jump right in. We all know it’s a bad idea to store application secrets within
  our code. So why we are storing there it still? Let’s take an example.

  We could store those secrets in a file and add it to the gitignore so it’s ...'
---

Par Ramesh Lingappa

Entrons directement dans le vif du sujet. Nous savons tous que c'est une mauvaise idée de stocker les secrets d'application dans notre code. Alors pourquoi continuons-nous à les y stocker ? Prenons un exemple.

Nous pourrions stocker ces secrets dans un fichier et l'ajouter au **gitignore** afin qu'il ne soit pas ajouté au contrôle de version. Mais il y a quelques obstacles :

* Comment gérons-nous ces secrets ?
* Que se passe-t-il lorsque la copie locale est supprimée ?
* Comment les partager avec d'autres développeurs ?
* Comment gérer le versionnage de ces secrets lors des modifications et tenir un journal d'audit de qui a changé quoi ?

Beaucoup de questions ! Nous finissons donc par les stocker dans le code, car c'est trop complexe à gérer autrement.

Pour une grande application ou une application qui nécessite un niveau de sécurité élevé, nous pouvons utiliser des services de gestion de secrets de classe production comme [Hashicorp Vault](https://www.vaultproject.io/).

Dans cet article, nous allons examiner une approche décente pour traiter les secrets tout en atteignant une meilleure sécurité. Nous allons y parvenir en utilisant **Google KMS + Git + IAM + automatisation.**

L'idée n'est pas nouvelle. Voici ce que nous allons faire :

* Nous allons stocker la version chiffrée du texte en clair dans le contrôle de version à l'aide de Google KMS
* Nous utiliserons KMS IAM pour permettre aux utilisateurs appropriés de gérer les secrets pour chaque environnement en accordant des rôles de chiffrement/déchiffrement
* Nous déploierons l'application avec les fichiers de secrets chiffrés
* Nous autoriserons le serveur à déchiffrer les secrets pour chaque environnement
* Au moment de l'exécution, nous chargerons les fichiers chiffrés, les déchiffrerons à l'aide des API KMS et les utiliserons.

> [**_Cloud KMS_**](https://cloud.google.com/kms) _est un **service de gestion de clés hébergé dans le cloud** qui vous permet de gérer les clés cryptographiques pour vos services cloud. Vous pouvez générer, utiliser, faire pivoter et détruire des clés cryptographiques. Cloud KMS est intégré à Cloud IAM et Cloud Audit Logging afin que vous puissiez gérer les autorisations sur les clés individuelles et surveiller la façon dont elles sont utilisées._

Ainsi, Cloud KMS chiffrera et déchiffrera nos secrets afin que nous n'ayons pas à stocker les clés. Seul un **utilisateur** autorisé ou un **compte de service** peut effectuer des opérations de chiffrement ou de déchiffrement.

Commençons !

### Étape 1 : Préparation des secrets

Pour notre cas d'utilisation, nous allons avoir des secrets d'application pour chaque environnement, `prod`, `stag` et `dev`. Pour ce faire, nous créons un nouveau dossier appelé `credentials` sous le dossier racine du projet, puis nous créons un dossier pour chaque environnement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*19_SnZ3De1o9XGv34P-oQg.png)
_identifiants par environnement_

Assurez-vous que ce dossier n'est pas suivi par le contrôle de version en ajoutant la ligne suivante dans le fichier `.gitignore` :

```
/credentials/
```

Ici, j'utilise un fichier **properties**, mais cela pourrait être n'importe quoi comme du JSON, YAML, etc. Vous pouvez maintenant ajouter n'importe quelle information sensible dans ces fichiers. J'ai ajouté ce qui suit :

```
# dev credentialsoauth_client_id=1234oauth_client_secret=abcdapi_key=api_123# ...
```

D'accord, nos secrets sont prêts à être cachés.

### Étape 2 : Création de clés secrètes KMS

Nous devons créer des clés de chiffrement pour chaque environnement afin d'utiliser ce service. Pour nous, chaque environnement sera un projet Google Cloud différent (recommandé). C'est mieux ainsi car cela offre une isolation et un contrôle d'accès (plus de détails à ce sujet plus tard).

Allez-y et créez une clé pour chaque environnement en utilisant ce lien [**Création de clés symétriques (recommandé)**](https://cloud.google.com/kms/docs/creating-keys#kms-create-keyring-console). Il contient des instructions étape par étape (différentes méthodes) pour créer ces clés. Nous créons ces clés en utilisant la ligne de commande comme ci-dessous :

```
// créer le trousseau de clés (pensez-y comme à un regroupement)gcloud kms keyrings create [KEYRING_NAME] \
--location [LOCATION] \
--project live-project-id
```

```
// créer la clé de chiffrementgcloud kms keys create [KEY_NAME] \
--location [LOCATION] \
--keyring [KEYRING_NAME] \
--purpose encryption \
--project live-project-id
```

Ici, je crée une clé pour la production en utilisant l'ID du projet de production. Répétez ce processus pour chaque environnement en remplaçant le **Project ID** pour _stag et les autres environnements_.

**Note** : Vous devez disposer de quatre informations pour chaque clé : `location`, `keyring`, `cryptokey` et `project`. Ces informations ne sont pas sensibles, vous pouvez donc les stocker dans votre code ou vos scripts de build.

### Étape 3 : Attribution des permissions pour utiliser ces clés

C'est ici que réside la beauté du système KMS IAM : pour utiliser chaque clé, nous devons explicitement accorder l'accès à un utilisateur individuel ou à un compte de service. Cela le rend très puissant car nous pouvons désormais définir qui peut gérer les secrets, qui peut voir ces secrets, et plus encore.

Consultez [Utilisation d'IAM avec Cloud KMS](https://cloud.google.com/kms/docs/iam) pour plus d'informations. Grâce à cela, nous pouvons réaliser ce qui suit :

#### **Environnement de production :**

Personne ne devrait pouvoir voir les secrets, à l'exception des quelques personnes qui peuvent apporter des modifications aux secrets. Nous pouvons le faire en leur accordant le rôle :

```
cloudkms.cryptoKeyEncrypterDecrypter
```

Ainsi, même si les identifiants chiffrés sont stockés dans le contrôle de version, les autres développeurs ne pourront pas les utiliser. Notez que même ces développeurs peuvent effectuer des déploiements en direct sans jamais avoir besoin de connaître les secrets (plus de détails à ce sujet plus tard).

#### **Environnement de staging :**

Chaque développeur peut voir les secrets et les utiliser en développement, mais seules quelques personnes peuvent apporter des modifications aux secrets. Nous pouvons le faire en leur accordant le rôle :

```
// pour la lecture seulecloudkms.cryptoKeyDecrypter
```

```
// pour la gestioncloudkms.cryptoKeyEncrypterDecrypter
```

De même, vous pouvez accorder des rôles de clé pour différents environnements en fonction des besoins. Pour les commandes exactes, reportez-vous à [Accorder des autorisations](https://cloud.google.com/kms/docs/iam#granting_permissions_to_use_keys) dans la documentation.

### Étape 4 : Chiffrement des secrets

Nous en avons terminé avec le travail de préparation, et il est maintenant temps de cacher certains secrets. En supposant que vous ayez le rôle _encrypter_, vous pouvez chiffrer un fichier à l'aide de la commande suivante :

```
gcloud kms encrypt --location global \  --keyring secrets-key-ring --key quickstart \  --plaintext-file credentials/stag/credentials.properties \  --ciphertext-file credentials-encrypted/stag/credentials.properties.encrypted
```

Puisqu'il s'agit d'une commande shell gcloud, vous pouvez facilement l'intégrer à n'importe quel système de build pour chiffrer tous les fichiers sous le dossier **credentials**. Par exemple, j'utilise **gradle** pour cela :

Fondamentalement, il y a deux fonctions utilitaires :

* **kmsEncryptSecrets** prend le **dossier source** pour chiffrer chaque fichier qu'il contient et l'écrire dans le **dossier cible** avec l'extension **.enc** (chiffré), et
* **kmsDecryptSecrets** qui effectue le processus inverse.

Ainsi, chaque fois que nous modifions des secrets, vous pouvez appeler la méthode utilitaire de chiffrement avec une tâche simple :

Maintenant, le dossier chiffré ressemblera à ce qui suit :

![Image](https://cdn-media-1.freecodecamp.org/images/1*fNdCMqpw8-uVglH_mIfHHQ.png)
_fichiers d'identifiants chiffrés_

Ce dossier peut être ajouté au contrôle de version afin que chaque fois qu'un utilisateur autorisé modifie des secrets, un nouveau fichier chiffré soit généré et enregistre l'historique dans le contrôle de version.

De même, il existe une [Tâche de déchiffrement](https://gist.github.com/ramesh-dev/3ba47732591c4b9e1bae7b99ed2b67a9) pour le processus inverse.

### Étape 4 : Utilisation des secrets chiffrés lors du déploiement

Maintenant que nous avons fini de chiffrer les secrets et de les gérer correctement dans le contrôle de version, voyons comment ils peuvent être utilisés au moment de l'exécution, c'est-à-dire lorsque l'application s'exécute réellement en staging ou en production. Nous pouvons le faire de deux manières :

#### **1. Déchiffrement des secrets et transmission lors du déploiement :**

Ainsi, lors du déploiement, un utilisateur autorisé peut simplement déchiffrer ces secrets chiffrés et les ajouter au déploiement (par exemple : répertoire de build), les rendant ainsi disponibles pour le code au moment de l'exécution. Nous ne couvrirons pas cela en profondeur.

> _Cette approche est bonne lorsque le **déployeur** doit être très restrictif ou que le processus est automatisé à l'aide d'un pipeline CD._

#### **2. Transmission des secrets chiffrés lors du déploiement et déchiffrement au moment de l'exécution :**

Ici, nous n'allons pas déchiffrer et envoyer des secrets bruts lors du déploiement. Au lieu de cela, nous transmettons simplement des secrets chiffrés. Et pendant l'exécution, nous déchiffrerons ces secrets et les utiliserons.

**Note :** cela fonctionne mieux au sein de Google Cloud Platform. Sinon, vous devez générer un compte de service pour pouvoir utiliser cette approche avec des fournisseurs externes.

Cette approche est encore plus sécurisée puisque nous ne dépendons d'aucune action utilisateur intermédiaire ou d'un pipeline, mais uniquement de serveurs autorisés capables de déchiffrer le contenu au moment de l'exécution.

Par exemple, nous pouvons autoriser le serveur de staging (compte de service) à déchiffrer les secrets de staging et non les secrets de production.

> _Avec cette approche, même un développeur qui n'a pas accès au déchiffrement des secrets de production peut effectuer un déploiement en production et tout fonctionne toujours correctement._

### Étape 5 : Utilisation des secrets au moment de l'exécution

Nous allons utiliser la deuxième approche (transmission de secrets chiffrés).

Pour la démo, supposons que nous allons déployer sur **AppEngine** puisqu'il possède déjà un compte de service par défaut généré. Nous lui accorderons l'accès pour déchiffrer les secrets comme ci-dessous :

```
gcloud kms keys add-iam-policy-binding secrets-enc-key \ --project kms-demo \--location global \--keyring secrets-key-ring \--member serviceAccount:kms-demo@appspot.gserviceaccount.com \--project kms-demo \--role roles/cloudkms.cryptoKeyDecrypter
```

Ainsi, lorsque le serveur démarre, nous pourrions simplement charger le fichier chiffré et utiliser les [bibliothèques clientes KMS](https://cloud.google.com/kms/docs/reference/libraries) pour déchiffrer son contenu.

### Étape 6 : [Journaux d'audit KMS](https://cloud.google.com/kms/docs/logging)

Enfin, vous pouvez voir les journaux d'audit pour les opérations sur chaque clé en activant la journalisation d'audit KMS (non activée par défaut). Ainsi, nous pouvons désormais garder une trace de toutes les opérations effectuées pour de futurs audits.

Vous pouvez activer le journal d'audit à l'aide de gcloud, mais nous en avons assez vu de la ligne de commande. Alternativement, nous pouvons activer cette configuration à l'aide de l'interface utilisateur de la console Cloud. Dans le menu de gauche, choisissez **IAM & admin -> Audit Logs**.

Cliquez sur **Cloud Key Management Service** et activez **Data Read** et **Data Write**, puis cliquez sur Enregistrer.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8FblhXekEI-E0hmmKGQEqA.png)
_Console de journal d'audit Google IAM_

C'est tout ! Désormais, si un chiffrement, un déchiffrement ou tout autre type d'opération est effectué, un journal d'audit est généré et vous pouvez les consulter dans la section Logging sous **_Cloud KMS CryptoKey._**

![Image](https://cdn-media-1.freecodecamp.org/images/1*X2F511jz2h5VoX5v0N6SNg.png)
_Journaux d'audit pour les opérations IAM_

Comme vous pouvez le voir, il contient des journaux d'audit pour toutes sortes d'opérations, y compris les échecs tels que les autorisations non valides, ou les requêtes, etc. Il montre quel utilisateur a effectué quelle opération en utilisant quelle clé (ou si cela a été fait sous un compte de service). C'est une solution assez soignée. Pour plus d'informations, lisez [Utilisation de Cloud Audit Logging avec Cloud KMS](https://cloud.google.com/kms/docs/logging).

### Conclusion

Avec cette approche, nous pouvons stocker, gérer et utiliser les secrets d'application ou toute information sensible de manière sécurisée et également suivre les modifications à l'aide du contrôle de version. Les techniques abordées dans cet article peuvent être utilisées avec n'importe quel langage, et elles peuvent être utilisées totalement ou partiellement sur d'autres plateformes comme iOS, Android, des serveurs externes, etc.

Pour une liste des commandes kms, reportez-vous à [Commandes KMS](https://gist.github.com/ramesh-dev/5042ef29946f570c906a082ec67cb5dc). Consultez également l'exemple d'application pour le code complet :

[**ramesh-dev/gae-dynamic-config-demo**](https://github.com/ramesh-dev/gae-dynamic-config-demo/tree/kms_demo)  
[_Démo de configuration dynamique AppEngine. Contribuez au développement de ramesh-dev/gae-dynamic-config-demo en créant un…_github.com](https://github.com/ramesh-dev/gae-dynamic-config-demo/tree/kms_demo)

Voici quelques liens de référence :

* [Google Cloud KMS](https://cloud.google.com/kms/)
* [Création de clés symétriques dans KMS](https://cloud.google.com/kms/docs/creating-keys#kms-create-keyring-console)
* [Démarrage rapide de Google Cloud KMS](https://cloud.google.com/kms/docs/quickstart)
* [Utilisation d'IAM avec Cloud KMS](https://cloud.google.com/kms/docs/iam)
* [Configurations dynamiques AppEngine à l'aide de Gradle Partie 2](https://medium.com/swlh/dynamic-appengine-configurations-using-gradle-part-2-49a30eb87672)