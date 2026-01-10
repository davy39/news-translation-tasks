---
title: Comment héberger un site web statique sur AWS S3 et CloudFront
subtitle: ''
author: Oghenekparobo Stephen
co_authors: []
series: null
date: '2025-03-25T15:34:32.267Z'
originalURL: https://freecodecamp.org/news/host-a-static-website-on-aws-s3-and-cloudfront
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1742916792332/9dbf6a18-7260-434f-815d-e38a82c9e47e.png
tags:
- name: AWS
  slug: aws
- name: S3
  slug: s3
- name: cloudfront
  slug: cloudfront
- name: Cloud Computing
  slug: cloud-computing
seo_title: Comment héberger un site web statique sur AWS S3 et CloudFront
seo_desc: DevOps might seem like a complex field with various specializations and
  tools. In this article, I’ll simplify one key aspect by demonstrating how to host
  a static website using Amazon S3 (Simple Storage Service) and CloudFront, AWS’s
  Content Delivery...
---

DevOps peut sembler être un domaine complexe avec diverses spécialisations et outils. Dans cet article, je vais simplifier un aspect clé en démontrant comment héberger un site web statique en utilisant Amazon S3 (Simple Storage Service) et CloudFront, le réseau de diffusion de contenu (CDN) d'AWS qui met en cache et distribue le contenu efficacement pour un accès plus rapide.

Pour suivre ce guide, vous devez avoir :

* Un [**compte AWS**](https://aws.amazon.com/free/)**.**

* Une compréhension de base de l'architecture AWS (Vous pouvez obtenir des informations [ici](https://youtu.be/NhDYbskXRgc?si=mZi-dN4AbdVZtWD5).)

* Des connaissances sur [**AWS IAM**](https://aws.amazon.com/iam/) (Identity and Access Management pour le contrôle d'accès sécurisé aux ressources)

* Une familiarité avec [**Git et GitHub**](https://youtu.be/RGOj5yH7evk?si=AXlPrk1czT9zm4ql)

Plongeons-nous et configurons notre hébergement de site statique étape par étape.

## Table des matières :

1. [Qu'est-ce qu'AWS S3 ?](#heading-questce-que-aws-s3)

* [Contrôles d'accès granulaires dans S3](#heading-controles-dacces-granulaires-dans-s3)

* [Chiffrement au repos dans S3](#heading-chiffrement-au-repos-dans-s3)

* [Comment téléverser un site web statique sur Amazon S3](#heading-comment-televerser-un-site-web-statique-sur-amazon-s3)

2. [Qu'est-ce qu'un bucket ?](#heading-questce-quun-bucket)

* [Comment créer un bucket](#heading-comment-creer-un-bucket)

* [Comment téléverser des fichiers et dossiers vers un bucket S3](#heading-comment-televerser-des-fichiers-et-dossiers-vers-un-bucket-s3)

* [Comment définir les permissions et propriétés dans AWS S3](#heading-comment-definir-les-permissions-et-proprietes-dans-aws-s3)

* [Qu'est-ce qu'une politique de bucket ?](#heading-questce-quune-politique-de-bucket)

* [Comment configurer une politique de bucket](#heading-comment-configurer-une-politique-de-bucket)

3. [Comment activer l'hébergement statique](#heading-comment-activer-lhebergement-statique)

4. [Amazon CloudFront](#heading-amazon-cloudfront)

* [Fonctionnalités clés d'Amazon CloudFront](#heading-fonctionnalites-cles-damazon-cloudfront)

* [Pourquoi Amazon S3 seul ne suffit pas](#heading-pourquoi-amazon-s3-seul-ne-suffit-pas)

* [Pourquoi vous devriez servir votre site web avec CloudFront](#heading-pourquoi-vous-devriez-servir-votre-site-web-avec-cloudfront)

* [Qu'est-ce qu'une distribution CloudFront ?](#heading-questce-quune-distribution-cloudfront)

* [Comprendre le nom de ressource Amazon (ARN)](#heading-comprendre-le-nom-de-ressource-amazon-arn)

* [Politique de bucket S3 mise à jour](#heading-politique-de-bucket-s3-mise-a-jour)

5. [Conclusion](#heading-conclusion)

## Qu'est-ce qu'AWS S3 ?

Amazon Simple Storage Service (Amazon S3) est un service de stockage d'objets conçu pour stocker et récupérer n'importe quelle quantité de données depuis n'importe où.

L'utilisation d'Amazon S3 est simple. Vous commencez par sélectionner une région, créer un conteneur de stockage appelé "bucket", puis téléverser vos données. Il n'y a pas de limite à la quantité de données que vous pouvez stocker, et vous pouvez les récupérer à tout moment.

Amazon S3 crée automatiquement des sauvegardes de vos données en stockant des copies sur plusieurs appareils. Il vous permet également de conserver différentes versions de vos fichiers, vous aidant à récupérer des données si elles sont accidentellement perdues. Si vous supprimez un fichier par erreur, vous pouvez le restaurer en utilisant la fonctionnalité de versioning d'Amazon S3.

Amazon S3 offre des politiques de cycle de vie configurables pour aider à gérer les données efficacement tout au long de leur cycle de vie. La sécurité est une priorité absolue pour AWS, garantissant que les téléversements et récupérations de données sont protégés en utilisant le chiffrement SSL pour une transmission sécurisée. AWS fournit également plusieurs fonctionnalités de sécurité pour protéger vos données, y compris des contrôles d'accès granulaires et le chiffrement au repos. Explorons ces deux fonctionnalités en un peu plus de détail.

### **Contrôles d'accès granulaires dans S3**

Amazon S3 fournit un contrôle d'accès granulaire, vous permettant de définir qui peut accéder à vos données et quelles actions ils peuvent effectuer. Cela est géré via :

1. **AWS Identity and Access Management (IAM)** : Contrôle les permissions des utilisateurs au niveau du compte AWS. Vous pouvez accorder à des utilisateurs ou rôles spécifiques des permissions pour accéder à S3.

2. **Politiques de bucket S3** : Politiques basées sur JSON appliquées au niveau du bucket pour contrôler l'accès à tous les objets dans un bucket.

3. **Listes de contrôle d'accès (ACL)** : Définit les permissions pour des objets individuels au sein d'un bucket (moins couramment utilisé depuis que les politiques de bucket sont plus puissantes).

4. **Paramètres de blocage de l'accès public** : Empêche l'exposition publique accidentelle des données S3 en restreignant l'accès ouvert.

### **Chiffrement au repos dans S3**

Le chiffrement au repos garantit que les données stockées restent sécurisées, même en cas d'accès non autorisé. S3 prend en charge plusieurs options de chiffrement :

1. **Chiffrement côté serveur (SSE)** :

* **SSE-S3** : AWS gère automatiquement les clés de chiffrement.

* **SSE-KMS** : Utilise AWS Key Management Service (KMS) pour un contrôle supplémentaire sur les clés de chiffrement.

* **SSE-C** : Les clients fournissent leurs propres clés de chiffrement.

2. **Chiffrement côté client** :

* Les données sont chiffrées **avant** d'être téléversées vers S3 en utilisant des clés de chiffrement gérées par le client.

Nous pourrions passer un temps infini à rechercher et explorer la théorie derrière Amazon S3, mais l'application pratique solidifie l'apprentissage. Maintenant, passons au téléversement d'un site web statique vers Amazon S3.

Comme mentionné précédemment, vous devez avoir une compréhension de base du fonctionnement d'AWS, y compris l'inscription, la connexion et la création d'utilisateurs IAM. Cela est crucial car nous utiliserons un utilisateur IAM pour effectuer des opérations de manière sécurisée. Comprendre Identity and Access Management est essentiel dans AWS, car il garantit un contrôle d'accès et une sécurité appropriés lors de la gestion des ressources.

## Comment téléverser un site web statique sur Amazon S3

Pour téléverser un site web statique, vous avez d'abord besoin d'un site statique. Si vous n'en avez pas, vous pouvez utiliser un modèle gratuit de [Free CSS](https://www.free-css.com/free-css-templates).

J'ai également fourni un modèle prêt à l'emploi que vous pouvez cloner depuis ce dépôt GitHub : [Mediplus Free Template](https://github.com/Oghenekparobo/Mediplus-free-template).

Maintenant que votre projet statique est prêt, allons sur AWS et téléversons-le vers un bucket Amazon S3.

Connectez-vous à votre compte AWS en utilisant vos identifiants d'utilisateur IAM. Une fois connecté, vous serez redirigé vers la Console de gestion AWS.

Votre tableau de bord AWS devrait ressembler à ceci :

![Tableau de bord de l'utilisateur AWS ou IAM](https://cdn.hashnode.com/res/hashnode/image/upload/v1742473569107/436e229b-f16d-4572-b26c-b2359d2ef738.jpeg align="center")

Accédez au service S3 en cliquant sur le lien S3 dans le tableau de bord AWS. Si vous ne le voyez pas, ce qui est peu probable, utilisez la barre de recherche en haut du tableau de bord. Tapez simplement "S3", et il apparaîtra dans les résultats. Cliquez dessus pour continuer.

Une fois que vous arrivez sur la page Amazon S3, vous verrez le bouton Créer un bucket.

Les buckets S3 sont la pierre angulaire de nombreuses applications, y compris la diffusion de contenu, la sauvegarde de données, l'archivage, l'hébergement de sites web statiques et le stockage de big data pour l'analyse.

## Qu'est-ce qu'un bucket ?

Les buckets Amazon S3 sont les conteneurs de stockage fondamentaux au sein du service Amazon Simple Storage Service qui fournissent des référentiels sécurisés et évolutifs pour les actifs numériques.

Chaque bucket possède un nom globalement unique, un déploiement régional et une architecture de stockage d'objets plate identifiée par des clés uniques.

Avec une durabilité de 99,999999999 % grâce à la redondance intégrée, les buckets S3 prennent en charge les besoins cruciaux de l'infrastructure, y compris la distribution de contenu, l'archivage de données et l'hébergement de sites web statiques. Les administrateurs peuvent mettre en œuvre une gouvernance complète des données grâce à des contrôles d'accès configurables (politiques, ACL, IAM), des capacités de gestion du cycle de vie, de versioning et des protocoles de chiffrement pour répondre aux exigences de sécurité organisationnelles.

### Comment créer un bucket

Pour créer un bucket, cliquez sur le bouton "Créer un bucket". Vous serez alors redirigé vers la page de création de bucket.

![page de création de bucket](https://cdn.hashnode.com/res/hashnode/image/upload/v1742476384065/3a7df14d-2c5c-4169-98e9-473e7d96590b.jpeg align="center")

Choisissez n'importe quel nom que vous aimez, tant qu'il suit les règles de nommage des buckets AWS.

Vous verrez également diverses options de configuration, mais pour l'instant, laissez-les par défaut. Nous apporterons les ajustements nécessaires plus tard dans le projet.

Enfin, cliquez sur "Créer un bucket", et voilà, votre bucket est créé ! Vous devriez maintenant voir votre bucket, qui agit comme un conteneur pour stocker vos fichiers ou données :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1742477392285/409692a6-7838-42d4-bc61-e691b0d41477.jpeg align="center")

### Comment téléverser des fichiers et dossiers vers un bucket S3

Maintenant, téléversons le site statique que nous avons créé ou [clonné](https://github.com/Oghenekparobo/Mediplus-free-template) vers notre bucket S3.

**1. Cliquez sur votre bucket :**

![surligner le bucket à cliquer](https://cdn.hashnode.com/res/hashnode/image/upload/v1742479043138/19d5ee6b-67b2-422e-a1d5-e021d0248ef3.jpeg align="center")

Après avoir cliqué sur votre bucket, vous serez redirigé vers la page des détails du bucket, où vous pouvez gérer divers paramètres et configurations. Cette page fournit des options pour ajuster les permissions et propriétés, surveiller les métriques, gérer les points d'accès et téléverser des fichiers en utilisant le bouton "Téléverser".

![page du bucket créé ou page d'informations du bucket](https://cdn.hashnode.com/res/hashnode/image/upload/v1742479342643/deec0a64-6c4b-4670-8c38-e9949c18a93e.jpeg align="center")

**2. Télécharger les fichiers du projet :**

Si votre projet de site statique est prêt, il devrait contenir les fichiers essentiels nécessaires pour le déploiement. Bien que la structure puisse varier, elle devrait inclure un fichier index.html, ainsi que les actifs nécessaires tels que des images (ou un dossier d'images), des fichiers CSS (ou un dossier CSS) et des fichiers JavaScript (ou un dossier JS) pour assurer un fonctionnement et un style appropriés.

![fichiers du projet ou du site statique](https://cdn.hashnode.com/res/hashnode/image/upload/v1742479661115/367b7346-3762-4405-a612-fd5cb0d59094.jpeg align="center")

Commençons par téléverser les fichiers nécessaires selon la structure de notre projet. Commencez par les fichiers de niveau racine tels que index.html, ainsi que tout autre fichier essentiel au niveau racine. Assurez-vous de suivre attentivement la structure de votre projet et téléversez d'abord tous les fichiers requis pour maintenir une structure appropriée.

Ensuite, cliquez sur le bouton de téléversement :

![page de téléversement](https://cdn.hashnode.com/res/hashnode/image/upload/v1742479955714/306058d9-1629-4185-b480-d9e1ca4a6e91.jpeg align="center")

Sur la page de téléversement, vous verrez les boutons "Ajouter des fichiers" et "Ajouter un dossier". Commençons par téléverser des fichiers individuels. Cliquez sur "Ajouter des fichiers" pour commencer à sélectionner et téléverser les fichiers nécessaires.

![ajout de fichiers](https://cdn.hashnode.com/res/hashnode/image/upload/v1742480188360/b4a5d67f-14ed-4675-b846-8e71cf9080d5.jpeg align="center")

Après avoir téléversé vos fichiers avec succès, assurez-vous de suivre la structure de votre projet. Si votre site statique ne nécessite que des fichiers individuels, procédez en conséquence. Mais si votre projet dépend de dossiers spécifiques pour des actifs comme des images et du CSS, vous devrez téléverser ceux-ci également. Dans mon cas, la structure de mon projet inclut des dossiers pour les images et le CSS, etc., donc je vais téléverser à la fois des fichiers et des dossiers.

#### 3. Télécharger les dossiers du projet

![dossiers du projet](https://cdn.hashnode.com/res/hashnode/image/upload/v1742483020056/6454b351-b962-4e71-845b-b6c90a3bd2db.jpeg align="center")

Pour téléverser vos dossiers, cliquez sur le bouton "Ajouter un dossier".

![surligner le bouton Ajouter un dossier dans la page du bucket](https://cdn.hashnode.com/res/hashnode/image/upload/v1742483175794/0f96e172-146a-4513-adda-4e7bfb5281ec.jpeg align="center")

Maintenant, téléversez vos dossiers en cliquant sur le bouton "Ajouter un dossier" et en sélectionnant les dossiers nécessaires, tels que ceux contenant des images, des fichiers CSS ou JavaScript, en fonction de la structure de votre projet.

![à quoi ressemble un téléversement de dossier réussi](https://cdn.hashnode.com/res/hashnode/image/upload/v1742483490417/254d6fc4-ca3c-427d-acb5-1ffab46ed15f.jpeg align="center")

Vous remarquerez que lorsque vous téléversez des dossiers, S3 extrait et structure automatiquement les fichiers par nom, type et taille. Cela peut parfois être déroutant pour les débutants, car les fichiers sont affichés dans un format structuré.

Une fois que vous avez téléversé vos fichiers et dossiers avec succès, faites défiler vers le bas et cliquez sur le bouton "Téléverser" pour terminer le processus.

![surligner où se trouve le bouton de téléversement](https://cdn.hashnode.com/res/hashnode/image/upload/v1742483726834/890c70db-e2e4-4b0f-aac3-29b215276f97.jpeg align="center")

Après avoir cliqué sur "Téléverser", AWS S3 commencera à téléverser vos fichiers. Vous verrez un indicateur de progression montrant l'état de chaque fichier en cours de téléversement en temps réel.

Une fois le téléversement terminé, vous verrez un message de confirmation indiquant "Téléversement réussi". AWS S3 générera alors une URL que vous pouvez trouver dans la section Résumé de la page des détails du bucket. (Voir l'image ci-dessous pour référence.)

![montrant le téléversement réussi](https://cdn.hashnode.com/res/hashnode/image/upload/v1742485405264/af04f296-e447-4747-b060-2f9b86d7a0e0.jpeg align="center")

Félicitations ! Vous avez téléversé votre projet dans AWS S3 avec succès. Maintenant, rendons cela accessible sur le web.

Cliquez sur le bouton "Fermer" pour quitter la page de téléversement. Maintenant, tout en restant dans votre bucket, configurons les paramètres et permissions nécessaires pour assurer un accès et un fonctionnement appropriés pour notre site web statique.

## **Comment définir les permissions et propriétés dans AWS S3**

Après avoir téléversé vos fichiers, l'étape suivante consiste à configurer les permissions et propriétés pour vous assurer que votre site web statique fonctionne correctement.

* **Permissions** : Par défaut, les objets S3 sont privés. Pour rendre votre site web accessible au public, vous devez ajuster la politique de bucket et les permissions des objets en conséquence.

* **Propriétés** : Vous pouvez configurer divers paramètres tels que le versioning, le chiffrement et l'hébergement de site web statique sous l'onglet Propriétés de votre bucket, mais nous n'irons pas trop loin car nous ne faisons que passer par les bases.

![page du bucket avec des fichiers](https://cdn.hashnode.com/res/hashnode/image/upload/v1742485786885/3290bf47-6d32-4956-957c-527ba30357ed.jpeg align="center")

Commençons par configurer les permissions :

### Permissions

Par défaut, l'accès public est bloqué dans S3 pour des raisons de sécurité. Mais pour ce tutoriel, nous allons activer l'accès public pour nous assurer que notre site web statique est accessible aux utilisateurs.

Sur l'image ci-dessous, vous pouvez voir que l'accès public est bloqué par défaut :

![accès public bloqué](https://cdn.hashnode.com/res/hashnode/image/upload/v1742486056880/5e5ae64d-ee88-4f7e-af4e-989f40850d21.jpeg align="center")

Pour activer l'accès public, cliquez sur le bouton "Modifier" dans le coin supérieur droit. Ensuite, décochez l'option "Bloquer tout accès public". Après cela, cliquez sur "Enregistrer les modifications" pour appliquer la mise à jour.

Vous pouvez maintenant voir que l'accès public a été bloqué :

![Accès public bloqué](https://cdn.hashnode.com/res/hashnode/image/upload/v1742486660352/50508b0d-0d51-4f48-8bf0-d2a6f01fc5c8.jpeg align="center")

L'accès public est maintenant activé. Cliquez sur "Enregistrer les modifications" pour confirmer et appliquer la mise à jour.

![L'accès public est maintenant activé, cliquez sur enregistrer les modifications pour valider les paramètres](https://cdn.hashnode.com/res/hashnode/image/upload/v1742486981885/6a9d687f-8fef-40a8-b585-de9c23126aa2.jpeg align="center")

#### Activation de l'accès public

AWS S3 vous demandera de saisir un texte de confirmation pour valider les paramètres. Saisissez le texte requis et confirmez, et l'accès public sera activé avec succès.

![prompt de confirmation](https://cdn.hashnode.com/res/hashnode/image/upload/v1742487256155/d3efe5d2-e42f-46d6-8052-4d6cb9a99ce8.jpeg align="center")

Maintenant que nous avons activé l'accès public, définissons une politique de bucket.

### **Qu'est-ce qu'une politique de bucket ?**

Une politique de bucket est une politique de contrôle d'accès basée sur JSON qui définit les permissions pour votre bucket S3. Elle vous permet de spécifier qui peut accéder à votre bucket et quelles actions ils peuvent effectuer.

Avec une politique de bucket, vous pouvez :

* Accorder ou restreindre l'accès public aux objets dans votre bucket.

* Autoriser des utilisateurs ou services AWS spécifiques à interagir avec votre bucket.

* Définir des permissions de lecture, d'écriture ou de suppression pour différents utilisateurs.

Dans cette prochaine section, nous allons configurer une politique de bucket pour rendre notre site web statique accessible au public.

## **Comment configurer une politique de bucket**

La configuration d'une politique de bucket est simple. Cliquez sur le bouton "Modifier" dans la section Politique de bucket et collez la politique JSON suivante dans l'éditeur :

```markdown
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::nom-de-votre-bucket/*"
    }
  ]
}
```

#### Comprendre les attributs de la politique :

* **Version** : Définit la version du langage de la politique. La version `"2012-10-17"` est la plus récente et la plus couramment utilisée pour les politiques S3.

* **Statement** : Une liste de règles qui définissent quelles actions sont autorisées ou refusées.

* **Sid (Statement ID)** : Un identifiant unique pour l'instruction de la politique (facultatif mais utile pour référence).

* **Effect** : Spécifie si la règle autorise ou refuse l'action spécifiée. Dans ce cas, c'est `"Allow"`.

* **Principal** : Définit qui a accès. Le `"*"` signifie n'importe qui (accès public).

* **Action** : Spécifie l'opération autorisée. `"s3:GetObject"` permet aux utilisateurs de récupérer (lire) des objets depuis le bucket.

* **Resource** : Définit le bucket spécifique et les objets auxquels la politique s'applique. Remplacez `"nom-de-votre-bucket"` par le nom réel de votre bucket. Le `"/*"` signifie tous les objets dans le bucket.

Cette politique rend tous les objets du bucket lisibles publiquement, permettant aux utilisateurs d'accéder aux fichiers de votre site web statique via un navigateur.

Si vous avez suivi de près, votre page de politique de bucket devrait ressembler à ceci :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1742489775324/07439366-6f64-401b-a48a-1ce20536df5c.jpeg align="center")

Maintenant, cliquez sur le bouton "Enregistrer les modifications", généralement situé en bas à droite de la page, pour appliquer vos modifications.

Après avoir suivi les étapes requises, la politique de bucket a été définie et l'accès public a été activé.

![La politique de bucket a été définie et l'accès public a été activé.](https://cdn.hashnode.com/res/hashnode/image/upload/v1742490328543/58488d6e-1bc0-4acc-86da-e137e8fc5180.jpeg align="center")

Félicitations ! Vous avez configuré avec succès votre politique de bucket et activé l'accès public, ce qui signifie que n'importe qui peut maintenant accéder à votre site web. Mais attendez, où est l'URL ?

Il reste une dernière étape : nous devons activer l'hébergement de site web statique. Pour ce faire, vous devrez naviguer vers l'onglet Propriétés et configurer l'hébergement de site web statique afin que votre site puisse être accessible sur le web. Je vais vous guider à travers le processus dans la section suivante.

![onglet permissions](https://cdn.hashnode.com/res/hashnode/image/upload/v1742490657866/e9bb25a9-7fc2-478b-a531-2da041d4b740.jpeg align="center")

## Comment activer l'hébergement statique

Activer l'hébergement de site web statique est simple. Faites défiler jusqu'en bas de l'onglet Propriétés, et vous trouverez la section Hébergement de site web statique. Par défaut, cette option est désactivée. Activons-la pour rendre notre site web accessible sur le web.

![section d'hébergement web statique dans l'onglet permissions](https://cdn.hashnode.com/res/hashnode/image/upload/v1742490851582/ffa1b0b1-82f4-40d4-951d-bc494681620e.jpeg align="center")

Cliquez sur le bouton "Modifier" sur le côté droit de la section Hébergement de site web statique. Par défaut, cette option est désactivée, changez-la donc en Activé. Une fois activé, vous verrez plusieurs options de configuration, dont la plupart sont facultatives pour ce tutoriel.

Le paramètre le plus important ici est le Document d'index, qui spécifie le fichier par défaut qui se charge lorsqu'une personne accède à votre site. Le texte de l'espace réservé indique qu'il attend un fichier `index.html`. Tapez simplement `index.html` dans le champ Document d'index pour continuer.

![configuration de l'hébergement statique](https://cdn.hashnode.com/res/hashnode/image/upload/v1742491006060/91ba5d52-acb4-42c8-802d-7cfd9a24e8c8.jpeg align="center")

Après avoir saisi `index.html` dans le champ Document d'index, faites défiler vers le bas et cliquez sur "Enregistrer les modifications" pour appliquer la configuration.

Après avoir appliqué les modifications avec succès, vous devriez trouver votre URL de site web statique en bas de la section Hébergement de site web statique dans l'onglet Propriétés de votre bucket.

![url du site web statique](https://cdn.hashnode.com/res/hashnode/image/upload/v1742491854680/8393bbf2-27e6-4d21-b41f-d48e8e03fb09.jpeg align="center")

Félicitations ! Vous venez d'héberger votre site web sur AWS S3. C'est une étape solide dans le monde de DevOps.

Votre URL devrait ressembler à ceci : [`http://nom-de-votre-bucket.s3-website.votre-région.amazonaws.com/`](http://nom-de-votre-bucket.s3-website.votre-région.amazonaws.com/).

Il vous suffit de copier et coller votre URL de site web statique dans votre navigateur pour voir votre site hébergé en direct.

Maintenant, vous avez les compétences pour héberger un site web statique pour un client et partager l'URL avec eux.

Alors, allez prendre un café et du pain aux bananes, vous l'avez mérité. Ensuite, nous passerons à la partie suivante du tutoriel.

## Amazon CloudFront

Amazon CloudFront est un réseau de diffusion de contenu (CDN) rapide, hautement sécurisé et programmable qui améliore les performances et la sécurité des sites web.

Notre site web statique est hébergé sur S3([`http://nom-de-votre-bucket.s3-website.votre-région.amazonaws.com/`](http://nom-de-votre-bucket.s3-website.votre-région.amazonaws.com/)) – mais vous pourriez remarquer que le site est accessible via HTTP mais manque de mesures de sécurité appropriées telles que le chiffrement SSL/TLS. CloudFront répond à ces limitations en fournissant un moyen sécurisé et évolutif de servir à la fois du contenu statique et dynamique à l'échelle mondiale.

Il livre le contenu aux utilisateurs avec une faible latence en mettant en cache des copies de votre site web dans des emplacements de périphérie à travers le monde. Lorsqu'un utilisateur demande une ressource, CloudFront la sert depuis l'emplacement de périphérie le plus proche, améliorant ainsi considérablement la vitesse et la disponibilité.

### Fonctionnalités clés d'Amazon CloudFront

1. **Livraison de contenu sécurisée** : CloudFront prend en charge le chiffrement SSL/TLS, garantissant que les données sont transférées de manière sécurisée entre les clients et les serveurs.

2. **Protection contre les attaques DDoS** : Intégré avec AWS Shield, CloudFront aide à atténuer les attaques par déni de service distribué (DDoS).

3. **Mise en cache de contenu mondiale** : CloudFront met en cache le contenu dans plusieurs emplacements de périphérie, réduisant la charge du serveur et la latence.

4. **Distribution personnalisable** : Les utilisateurs peuvent configurer le comportement du cache, les paramètres d'origine et les politiques de sécurité.

5. **Intégration transparente avec les outils AWS** : CloudFront s'intègre avec AWS Lambda@Edge, S3, EC2 et API Gateway, prenant en charge la diffusion de contenu statique et dynamique.

6. **Optimisation des coûts** : Réduit les coûts de transfert de données en mettant en cache et en servant le contenu depuis les emplacements de périphérie au lieu de directement depuis l'origine.

### Pourquoi Amazon S3 seul ne suffit pas

Amazon S3 est un service de stockage d'objets évolutif et durable, mais il manque de fonctionnalités clés nécessaires pour servir du contenu web de manière sécurisée.

Tout d'abord, il n'a pas HTTPS par défaut. Lorsqu'un site est hébergé sur S3, il n'est accessible qu'en HTTP sauf si des configurations supplémentaires sont effectuées.

Deuxièmement, il a une latence plus élevée. Les buckets S3 sont hébergés dans une région AWS spécifique, ce qui peut entraîner une livraison de contenu plus lente pour les utilisateurs dans différentes régions.

Il n'a pas non plus de mise en cache intégrée, ce qui signifie que chaque demande est servie depuis S3, augmentant le temps de réponse et les coûts potentiels.

Et enfin, il n'y a pas de protection contre les attaques DDoS – contrairement à CloudFront, S3 ne fournit pas de protection native contre les cyberattaques.

### Pourquoi vous devriez servir votre site web avec CloudFront

Bien qu'Amazon S3 soit une excellente solution de stockage, il manque des optimisations de sécurité et de performance nécessaires pour l'hébergement web. Amazon CloudFront améliore la sécurité avec le chiffrement SSL/TLS, améliore les performances avec la mise en cache mondiale et fournit des fonctionnalités de sécurité robustes comme la protection contre les attaques DDoS.

En tirant parti de CloudFront, vous pouvez vous assurer que votre site web est non seulement rapide mais aussi sécurisé, évolutif et rentable.

Pour commencer à héberger votre site sur CloudFront, accédez à la page du service CloudFront dans AWS. Vous pouvez le faire en allant sur la page d'accueil ou le tableau de bord de la console de gestion AWS et en recherchant "CloudFront" à l'aide de la barre de recherche en haut à gauche. Cliquez sur "CloudFront" dans les résultats de recherche pour continuer.

![CloudFront peut être navigué sur le tableau de bord](https://cdn.hashnode.com/res/hashnode/image/upload/v1742514549138/97c31675-81dc-4d6f-8f2c-28867bbb7ee2.jpeg align="center")

![vous pouvez rechercher CloudFront dans la barre de recherche](https://cdn.hashnode.com/res/hashnode/image/upload/v1742514582663/14f0b8b4-3556-4ed2-a309-643d5fcee263.jpeg align="center")

Une fois que vous avez accédé à la page AWS CloudFront, vous verrez un bouton Créer une distribution. Cliquez dessus pour commencer à configurer CloudFront pour votre site web.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1742515301740/ffe72934-b250-4adb-8cf7-e9cafd5c4ac2.jpeg align="center")

### **Qu'est-ce qu'une distribution CloudFront ?**

Une distribution CloudFront est la configuration qui définit comment CloudFront livre le contenu aux utilisateurs. Elle agit comme un lien entre votre serveur d'origine (tel qu'un bucket S3) et le réseau mondial d'emplacements de périphérie de CloudFront. Lorsqu'un utilisateur demande votre site, CloudFront récupère le contenu depuis l'emplacement de périphérie le plus proche au lieu de toujours le récupérer depuis l'origine, garantissant ainsi des temps de chargement plus rapides, une latence réduite et une sécurité améliorée.

Il existe deux types de distributions dans CloudFront :

1. **Distribution Web** : Utilisée pour les sites web, les API et le contenu dynamique ou statique.

2. **Distribution RTMP** (Dépréciée) : Auparavant utilisée pour le streaming multimédia (maintenant remplacée par des services de streaming modernes).

Pour notre site web hébergé sur S3, nous allons créer une Distribution Web pour servir le contenu de manière sécurisée via HTTPS tout en améliorant la vitesse et la fiabilité.

Après avoir cliqué sur le bouton Créer une distribution, vous serez redirigé vers la page Créer une distribution, où vous pouvez configurer divers paramètres. Dans ce tutoriel, nous nous concentrerons sur les options essentielles.

1. Dans la section Origine, sélectionnez votre bucket S3 comme domaine d'origine.

2. Si votre bucket S3 a l'hébergement de site web statique activé, AWS recommande d'utiliser le point de terminaison du site web S3 au lieu du point de terminaison du bucket par défaut.

3. Entrez le bon point de terminaison du site web S3 dans le champ Domaine d'origine. Par exemple :

```markdown
freecodecampbuckettutorial.s3-website.ca-central-1.amazonaws.com
```

4. Assurez-vous d'utiliser le point de terminaison du site web S3 plutôt que l'URL standard du bucket S3 pour éviter les problèmes d'accès à votre site.

En suivant ces étapes, vous garantissez que CloudFront sert correctement votre site web statique depuis le bucket S3.

Assurez-vous d'utiliser le point de terminaison du site web S3 plutôt que l'URL standard du bucket S3 pour éviter les problèmes d'accès à votre site. Cela vous sera suggéré de manière descriptive lors de la saisie du nom d'origine. Cliquez sur "Utiliser le point de terminaison du site web" et il remplira le champ avec le point de terminaison du site web du bucket S3 au lieu de l'URL du bucket.

![sélectionner la distribution](https://cdn.hashnode.com/res/hashnode/image/upload/v1742516012771/9c631915-1a1e-415d-a614-5aab854db6ed.jpeg align="center")

![sélectionner le bucket s3 sur le domaine d'origine](https://cdn.hashnode.com/res/hashnode/image/upload/v1742515900001/01d173b4-8f2d-4289-96e1-e688ebafa34e.jpeg align="center")

Ensuite, faites défiler jusqu'à la section Pare-feu d'application Web (WAF) en bas de la page et activez les protections de sécurité pour protéger votre site web contre les menaces web courantes. Sélectionnez "Créer une distribution" pour déployer votre distribution CloudFront.

![activer waf](https://cdn.hashnode.com/res/hashnode/image/upload/v1742516241133/c587b52a-9734-40bb-80cc-a882b9bbbd44.jpeg align="center")

Votre page Distributions CloudFront devrait maintenant afficher la nouvelle distribution créée. La page inclura des détails clés tels que :

* **ID de distribution** : Un identifiant unique pour votre distribution CloudFront.

* **Nom de domaine** : L'URL fournie par CloudFront (par exemple, [`d1234abcd.cloudfront.net`](http://d1234abcd.cloudfront.net)), que vous pouvez utiliser pour accéder à votre site.

Après avoir créé votre distribution CloudFront, accédez à votre page Distributions et vérifiez la section Dernière modification pour son statut. Si le statut indique Déploiement en cours, vous devrez attendre qu'il change, ce qui peut prendre plusieurs minutes.

Une fois le déploiement terminé, le statut se mettra généralement à jour avec un horodatage, indiquant que la distribution est prête à être utilisée. Assurez-vous que le statut a changé avant de procéder à d'autres configurations ou d'accéder à votre distribution CloudFront.

![page dernière modification](https://cdn.hashnode.com/res/hashnode/image/upload/v1742525346316/cd9d88a0-7c03-46d8-a794-f3ddd64ffdda.jpeg align="center")

Votre site web est maintenant hébergé avec succès sur CloudFront !

Nous avons maintenant notre nom de domaine CloudFront (par exemple, [`d1234abcd.cloudfront.net`](http://d1234abcd.cloudfront.net)), que vous pouvez trouver dans la section Détails de votre distribution. Avant d'apporter d'autres modifications, prévisualisons le site en copiant et collant le nom de domaine dans un navigateur web.

![distribution de contenu créée](https://cdn.hashnode.com/res/hashnode/image/upload/v1742516439826/0bfd3393-8ec0-45cc-a643-0e1d31c013cf.jpeg align="center")

À ce stade, lorsque vous essayez d'accéder à votre site web en utilisant le nom de domaine CloudFront, vous remarquerez que le site est inaccessible. Cela se produit parce que CloudFront n'a pas encore la permission de récupérer le contenu de votre bucket S3.

![page de domaine cloud front inaccessible](https://cdn.hashnode.com/res/hashnode/image/upload/v1742518594690/0808d92b-b8c5-45b3-a89c-f54452eec9a6.jpeg align="center")

Pour résoudre ce problème, vous devez mettre à jour votre politique de bucket S3 pour autoriser explicitement CloudFront à accéder à vos objets. Vous pouvez le faire en ajoutant une condition qui accorde l'accès aux requêtes provenant spécifiquement de votre distribution CloudFront.

### **Comprendre le nom de ressource Amazon (ARN)**

Un nom de ressource Amazon (ARN) est un identifiant unique attribué aux ressources AWS. Chaque distribution CloudFront a son propre ARN, que vous pouvez trouver en haut de la page des détails de la distribution CloudFront. Il ressemble à quelque chose comme ceci :

```markdown
arn:aws:cloudfront::123456789012:distribution/E2ABC3XYZ456
```

Cet ARN est crucial car nous l'utilisons dans notre politique de bucket pour restreindre l'accès uniquement à notre distribution CloudFront, garantissant ainsi qu'aucun autre service ou utilisateur ne peut récupérer des données directement depuis notre bucket S3.

### **Politique de bucket S3 mise à jour**

Pour permettre à CloudFront de servir du contenu depuis notre bucket S3, nous mettons à jour la politique de bucket S3 comme suit :

```markdown
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "cloudfront.amazonaws.com"
      },
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::nom-de-votre-bucket/*",
      "Condition": {
        "StringEquals": {
          "AWS:SourceArn": "arn:aws:cloudfront::[ID_DE_COMPTE]:distribution/[ID_DE_DISTRIBUTION]"
        }
      }
    },
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::nom-de-votre-bucket/*"
    }
  ]
}
```

Décomposons la politique de bucket :

1. **Première instruction qui accorde l'accès à CloudFront :**

* `"Effect" : "Allow"` : Cela permet l'accès à la ressource spécifiée.

* `"Principal" : { "Service" : "cloudfront.amazonaws.com" }` : Accorde l'accès spécifiquement à CloudFront.

* `"Action" : "s3:GetObject"` : Permet à CloudFront de récupérer des objets depuis le bucket S3.

* `"Resource" : "arn:aws:s3:::nom-de-votre-bucket/*"` : Accorde l'accès à tous les objets dans le bucket S3.

* `"Condition"` : Garantit que seules les requêtes provenant de notre distribution CloudFront sont autorisées en utilisant :

```markdown
"AWS:SourceArn" : "arn:aws:cloudfront::123456789012:distribution/E2ABC3XYZ456"
```

2. **Deuxième instruction (facultative, et accorde l'accès public)**

* Cette instruction permet à tous les utilisateurs (`Principal : "*"`) d'accéder aux objets S3.

* Si vous souhaitez restreindre l'accès uniquement à CloudFront, vous pouvez supprimer cette deuxième instruction.

Après avoir modifié et mis à jour votre politique de bucket S3 pour permettre l'accès à CloudFront, vous pouvez actualiser la page où vous prévisualisez votre nom de domaine CloudFront (par exemple, [`d1234abcd.cloudfront.net`](http://d1234abcd.cloudfront.net)). Ouvrez-le dans un navigateur, et si vous avez suivi toutes les instructions avec soin, vous avez hébergé avec succès un site statique sur S3 et CloudFront.

Votre site web est maintenant entièrement protégé, bien joué ! Félicitations, pro de DevOps !

**COUP DE POING !**

## Conclusion

Dans ce guide, nous n'avons fait qu'effleurer la surface de ce qu'AWS peut faire. S3 et CloudFront sont des services puissants, mais il y a encore tellement plus à explorer, des paramètres de sécurité avancés à l'automatisation et aux optimisations de performance.

Alors que vous continuez votre parcours AWS, vous pouvez approfondir des sujets comme les stratégies de mise en cache, les configurations de domaine personnalisé et l'intégration d'AWS Lambda@Edge pour du contenu dynamique. Les possibilités sont infinies.

Ce n'est que le début, et vous êtes bien parti. Continuez à expérimenter, continuez à apprendre, et bientôt nous maîtriserons des capacités AWS encore plus avancées. Bonne construction ! 🚀