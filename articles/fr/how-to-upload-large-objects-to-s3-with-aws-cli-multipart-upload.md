---
title: Comment télécharger de grands objets sur S3 avec le téléchargement multipartite
  AWS CLI
subtitle: ''
author: Chisom Uma
co_authors: []
series: null
date: '2025-07-31T05:48:09.436Z'
originalURL: https://freecodecamp.org/news/how-to-upload-large-objects-to-s3-with-aws-cli-multipart-upload
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1753940874032/9dae199c-ff29-44c1-aff9-4dad02fdc26d.png
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: AWS
  slug: aws
seo_title: Comment télécharger de grands objets sur S3 avec le téléchargement multipartite
  AWS CLI
seo_desc: Uploading large files to S3 using traditional single-request methods can
  be quite challenging. If you’re transferring a 5GB database backup, and a network
  interruption happens, it forces you to restart the entire upload process. This wastes
  bandwidth...
---

Télécharger de grands fichiers sur S3 en utilisant des méthodes traditionnelles de requête unique peut être assez difficile. Si vous transférez une sauvegarde de base de données de 5 Go et qu'une interruption réseau se produit, cela vous oblige à redémarrer l'ensemble du processus de téléchargement. Cela gaspille la bande passante et le temps. Et cette approche devient de plus en plus peu fiable à mesure que la taille des fichiers augmente.

Avec une seule opération PUT, vous pouvez en fait télécharger un objet allant jusqu'à 5 Go. Mais, lorsqu'il s'agit de télécharger des objets plus grands (au-dessus de 5 Go), l'utilisation de la fonctionnalité [Téléchargement multipartite](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html) d'Amazon S3 est une meilleure approche.

Le téléchargement multipartite facilite le téléchargement de fichiers et d'objets plus grands en les segmentant en morceaux plus petits et indépendants qui sont téléchargés séparément et réassemblés sur S3.

Dans ce guide, vous apprendrez à implémenter des téléchargements multipartites en utilisant AWS CLI.

## Table des matières

* [Prérequis](#heading-prerequisites)
    
* [Comment fonctionnent les téléchargements multipartites](#heading-how-multipart-uploads-work)
    
* [Getting started](#heading-getting-started)
    
    * [Étape 1 : Télécharger AWS CLI](#heading-step-1-download-the-aws-cli)
        
    * [Étape 2 : Configurer les informations d'identification AWS IAM](#heading-step-2-configure-aws-iam-credentials)
        
* [Étape 1 : Diviser l'objet](#heading-step-1-split-object)
    
* [Étape 2 : Créer un bucket Amazon S3](#heading-step-2-create-an-amazon-s3-bucket)
    
* [Étape 3 : Initiation du téléchargement multipartite](#heading-step-3-initiate-multipart-upload)
    
* [Étape 4 : Télécharger les fichiers divisés vers le bucket S3](#heading-step-4-upload-split-files-to-s3-bucket)
    
* [Étape 5 : Créer un fichier JSON pour compiler les valeurs ETag](#heading-step-5-create-a-json-file-to-compile-etag-values)
    
* [Étape 6 : Terminer le téléchargement multipartite vers S3](#heading-step-6-complete-mulitipart-upload-to-s3)
    
* [Conclusion](#heading-conclusion)
    

## Prérequis

Pour suivre ce guide, vous devez avoir :

* Un compte AWS.
    
* Des connaissances sur AWS et le service S3.
    
* AWS CLI installé sur votre machine locale.
    

## Comment fonctionnent les téléchargements multipartites

Dans un téléchargement multipartite, les transferts de grands fichiers sont segmentés en morceaux plus petits qui sont téléchargés séparément vers Amazon S3. Une fois que tous les segments ont terminé leur processus de téléchargement, S3 les réassemble en l'objet complet.

Par exemple, un fichier de 160 Go divisé en segments de 1 Go génère 160 opérations de téléchargement individuelles vers S3. Chaque segment reçoit un identifiant distinct tout en préservant les informations de séquence pour garantir une reconstruction correcte du fichier.

Le système prend en charge une logique de nouvelle tentative configurable pour les segments échoués et permet la suspension/reprise des fonctionnalités de téléchargement. Voici un diagramme qui montre à quoi ressemble le processus de téléchargement multipartite :

![Processus de téléchargement multipartite AWS](https://cdn.hashnode.com/res/hashnode/image/upload/v1753729484012/63a68bcc-8c2d-4110-a007-bd67a3b4b2e4.png align="center")

## Getting Started

Avant de commencer avec ce guide, assurez-vous d'avoir AWS CLI installé sur votre machine. Si vous ne l'avez pas déjà installé, suivez les étapes ci-dessous.

### **Étape 1 : Télécharger AWS CLI**

Pour télécharger le CLI, visitez la [documentation de téléchargement du CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html). Ensuite, téléchargez le CLI en fonction de votre système d'exploitation (Windows, Linux, macOS). Une fois le CLI installé, l'étape suivante consiste à configurer vos informations d'identification AWS IAM dans votre terminal.

### **Étape 2 : Configurer les informations d'identification AWS IAM**

Pour configurer vos informations d'identification AWS, accédez à votre terminal et exécutez la commande suivante :

```bash
aws configure
```

Cette commande vous invite à coller certaines informations d'identification, telles que l'ID de clé d'accès AWS et l'ID secret. Pour obtenir ces informations d'identification, créez un nouvel utilisateur IAM dans votre compte AWS. Pour ce faire, suivez les étapes ci-dessous. (Vous pouvez ignorer ces étapes si vous avez déjà un utilisateur IAM et des informations d'identification de sécurité.)

1. [Connectez-vous](https://eu-north-1.signin.aws.amazon.com/oauth?client_id=arn%3Aaws%3Asignin%3A%3A%3Aconsole%2Fcanvas&code_challenge=gHNgZ4aX7afSDOY05TLWJNFrXDRnWRy-Mn3_TqW2p9o&code_challenge_method=SHA-256&response_type=code&redirect_uri=https%3A%2F%2Fconsole.aws.amazon.com%2Fconsole%2Fhome%3FhashArgs%3D%2523%26isauthcode%3Dtrue%26nc2%3Dh_si%3Aaws%3Asignin%3A%3A%3Aconsole%2Fcanvas&code_challenge=gHNgZ4aX7afSDOY05TLWJNFrXDRnWRy-Mn3_TqW2p9o&code_challenge_method=SHA-256&response_type=code&redirect_uri=https%3A%2F%2Fconsole.aws.amazon.com%2Fconsole%2Fhome%3FhashArgs%3D%2523%26isauthcode%3Dtrue%26nc2%3Dh_si%26src%3Dheader-signin%26state%3DhashArgsFromTB_eu-north-1_bcd5b75451c14744) à votre tableau de bord AWS.
    
2. Cliquez sur la barre de recherche au-dessus de votre tableau de bord et recherchez "IAM".
    
3. Cliquez sur IAM.
    
4. Dans le volet de navigation de gauche, accédez à **Gestion des accès** > **Utilisateurs**.
    
5. Cliquez sur **Créer un utilisateur**.
    
6. Pendant la création de l'utilisateur IAM, attachez une politique directement en sélectionnant **Attacher des politiques directement** à l'étape 2 : Définir les permissions.
    
7. Donnez à l'utilisateur un accès administrateur en recherchant "admin" dans la barre de recherche des politiques de permission et en sélectionnant AdministratorAccess.
    
8. Sur la page suivante, cliquez sur **Créer un utilisateur**.
    
9. Cliquez sur l'utilisateur créé dans la section **Utilisateurs** et accédez à **Informations d'identification de sécurité**.
    
10. Faites défiler vers le bas et cliquez sur **Créer une clé d'accès**.
    
11. Sélectionnez l'utilisation de l'interface de ligne de commande (CLI).
    
12. Sur la page suivante, cliquez sur **Créer une clé d'accès**.
    

Vous verrez maintenant vos clés d'accès. **Veuillez les garder en sécurité** et ne les exposez pas publiquement ou ne les partagez avec personne.

Vous pouvez maintenant copier ces clés d'accès dans votre terminal après avoir exécuté la commande `aws configure`.

Vous serez invité à inclure les détails suivants :

* `AWS Access Key ID` : obtenu à partir des informations d'identification de l'utilisateur IAM créé. Voir les étapes ci-dessus.
    
* `AWS Secret Access Key` : obtenu à partir des informations d'identification de l'utilisateur IAM créé. Voir les étapes ci-dessus.
    
* `Default region name` : nom de la région AWS par défaut, par exemple, `us-east-1`.
    
* `Default output format` : Aucun.
    

Maintenant, nous avons terminé la configuration du CLI.

Pour confirmer que vous avez installé le CLI avec succès, exécutez la commande suivante :

```bash
aws --version
```

Vous devriez voir la version du CLI dans votre terminal comme montré ci-dessous :

![Image de la version AWS CLI](https://cdn.hashnode.com/res/hashnode/image/upload/v1753730059205/5164dd17-5f66-40ba-b044-f1bca46a22a0.png align="center")

Maintenant, vous êtes prêt pour les étapes principales suivantes pour les téléchargements multipartites :)

## Étape 1 : Diviser l'objet

La première étape consiste à diviser l'objet que vous avez l'intention de télécharger. Pour ce guide, nous allons diviser un fichier vidéo de **188 Mo** en morceaux plus petits.

![Image de la taille de l'objet](https://cdn.hashnode.com/res/hashnode/image/upload/v1753730190692/bd22598d-0267-4507-864d-f3f7397faf19.png align="center")

Notez que ce processus fonctionne également pour des fichiers beaucoup plus grands.

Ensuite, localisez l'objet que vous avez l'intention de télécharger dans votre système. Vous pouvez utiliser la commande `cd` pour localiser l'objet dans son dossier stocké en utilisant votre terminal.

Ensuite, exécutez la commande de division suivante :

```bash
split -b <SIZE>mb <filename>
```

Remplacez `<SIZE>` par la taille de morceau souhaitée en mégaoctets (par exemple, 150, 100, 200).

Pour ce cas d'utilisation, nous allons diviser notre fichier vidéo de 188 Mo en octets. Voici la commande :

```bash

split -b 31457280 videoplayback.mp4
```

Ensuite, exécutez la commande `ls -lh` sur votre terminal. Vous devriez obtenir la sortie suivante :

![Image de l'objet divisé](https://cdn.hashnode.com/res/hashnode/image/upload/v1753730408994/33ef3552-9a92-46e9-9c2a-686e73d23c65.png align="center")

Ici, vous pouvez voir que le fichier de 188 Mo a été divisé en plusieurs parties (30 Mo et 7,9 Mo). Lorsque vous allez dans le dossier où l'objet est enregistré dans vos fichiers système, vous verrez des fichiers supplémentaires avec des noms qui ressemblent à ceci :

* `xaa`
    
* `xab`
    
* `xac`
    

et ainsi de suite. Ces fichiers représentent les différentes parties de votre objet. Par exemple, `xaa` est la première partie de votre fichier, qui sera téléchargée en premier vers S3. Plus d'informations à ce sujet plus tard dans le guide.

## Étape 2 : Créer un bucket Amazon S3

Si vous n'avez pas déjà créé de bucket S3, suivez les étapes de la documentation AWS [Prise en main d'Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html) pour en créer un.

## Étape 3 : Initiation du téléchargement multipartite

L'étape suivante consiste à initier un téléchargement multipartite. Pour ce faire, exécutez la commande suivante :

```bash

aws s3api create-multipart-upload --bucket DOC-EXAMPLE-BUCKET --key large_test_file
```

Dans cette commande :

* `DOC-EXAMPLE-BUCKET` est le nom de votre bucket S3.
    
* `large_test_file` est le nom du fichier, par exemple, videoplayback.mp4.
    

Vous obtiendrez une réponse JSON dans votre terminal, vous fournissant l'`UploadId`. La réponse ressemble à ceci :

```json

{
    "ServerSideEncryption": "AES345",
    "Bucket": "s3-multipart-uploads",
    "Key": "videoplayback.mp4",
    "UploadId": "************************************"
}
```

Gardez l'`UploadId` quelque part en sécurité sur votre machine locale, car vous en aurez besoin pour les étapes ultérieures.

## Étape 4 : Télécharger les fichiers divisés vers le bucket S3

Vous souvenez-vous de ces fichiers supplémentaires enregistrés sous xaa, xab, etc. ? Eh bien, il est maintenant temps de les télécharger vers votre bucket S3. Pour ce faire, exécutez la commande suivante :

```bash
aws s3api upload-part --bucket DOC-EXAMPLE-BUCKET --key large_test_file --part-number 1 --body large_test_file.001 --upload-id exampleTUVGeKAk3Ob7qMynRKqe3ROcavPRwg92eA6JPD4ybIGRxJx9R0VbgkrnOVphZFK59KCYJAO1PXlrBSW7vcH7ANHZwTTf0ovqe6XPYHwsSp7eTRnXB1qjx40Tk
```

* `DOC-EXAMPLE-BUCKET` est le nom de votre bucket S3.
    
* `large_test_file` est le nom du fichier, par exemple, videoplayback.mp4
    
* `large_test_file.001` est le nom de la partie du fichier, par exemple, xaa.
    
* `upload-id` remplace l'ID d'exemple par votre `UploadId` enregistré.
    

La commande retourne une réponse qui contient une valeur **ETag** pour la partie du fichier que vous avez téléchargée.

```json

{
    "ServerSideEncryption": "aws:kms",
    "ETag": "\"7f9b8c3e2a1d5f4e8c9b2a6d4e8f1c3a\"",
    "ChecksumCRC64NVME": "mK9xQpD2WnE="
}
```

Copiez la valeur **ETag** et enregistrez-la quelque part sur votre machine locale, car vous en aurez besoin plus tard comme référence.

Continuez à télécharger les parties de fichier restantes en répétant la commande ci-dessus, en incrémentant à la fois le numéro de partie et le nom de fichier pour chaque téléchargement ultérieur. Par exemple : `xaa` devient `xab`, et `--part-number 1` devient `--part-number 2`, et ainsi de suite.

Notez que la vitesse de téléchargement dépend de la taille de l'objet et de la qualité de votre vitesse Internet.

Pour confirmer que toutes les parties de fichier ont été téléchargées avec succès, exécutez la commande suivante :

```bash
aws s3api list-parts --bucket s3-multipart-uploads --key videoplayback.mp4 --upload-id p0NU3agC3C2tOi4oBmT8lHLebUYqYXmWhEYYt8gc8jXlCStEZYe1_kSx1GjON2ExY_0T.4N4E6pjzPlNcji7VDT6UomtNYUhFkyzpQ7IFKrtA5Dov8YdC20c7UE20Qf0
```

Remplacez l'ID de téléchargement d'exemple par votre ID de téléchargement réel.

Vous devriez obtenir une réponse JSON comme ceci :

```json

{
    "Parts": [
        {
            "PartNumber": 1,
            "LastModified": "2025-07-27T14:22:18+00:00",
            "ETag": "\"f7b9c8e4d3a2f6e8c9b5a4d7e6f8c2b1\"",
            "Size": 26214400
        },
        {
            "PartNumber": 2,
            "LastModified": "2025-07-27T14:25:42+00:00",
            "ETag": "\"a8e5d2c7f9b4e6a3c8d5f2e9b7c4a6d3\"",
            "Size": 26214400
        },
        {
            "PartNumber": 3,
            "LastModified": "2025-07-27T14:28:15+00:00",
            "ETag": "\"c4f8e2b6d9a3c7e5f8b2d6a9c3e7f4b8\"",
            "Size": 26214400
        },
        {
            "PartNumber": 4,
            "LastModified": "2025-07-27T14:31:03+00:00",
            "ETag": "\"e9c3f7a5d8b4e6c9f2a7d4b8c6e3f9a2\"",
            "Size": 26214400
        },
        {
            "PartNumber": 5,
            "LastModified": "2025-07-27T14:33:47+00:00",
            "ETag": "\"b6d4a8c7f5e9b3d6a2c8f4e7b9c5d8a6\"",
            "Size": 26214400
        },
        {
            "PartNumber": 6,
            "LastModified": "2025-07-27T14:36:29+00:00",
            "ETag": "\"d7e3c9f6a4b8d2e5c7f9a3b6d4e8c2f5\"",
            "Size": 26214400
        },
        {
            "PartNumber": 7,
            "LastModified": "2025-07-27T14:38:52+00:00",
            "ETag": "\"f2a6d8c4e7b3f6a9c2d5e8b4c7f3a6d9\"",
            "Size": 15728640
        }
    ]
}
```

C'est ainsi que vous vérifiez que toutes les parties ont été téléchargées.

## Étape 5 : Créer un fichier JSON pour compiler les valeurs ETag

Le document que nous allons créer aide AWS à comprendre quelles parties les ETags représentent. Rassemblez les valeurs **ETag** de chaque partie de fichier téléchargée et organisez-les dans une structure JSON.

Format JSON d'exemple :

```json

{
    "Parts": [{
        "ETag": "example8be9a0268ebfb8b115d4c1fd3",
        "PartNumber":1
    },

    ....

    {
        "ETag": "example246e31ab807da6f62802c1ae8",
        "PartNumber":4
    }]
}
```

Enregistrez le fichier JSON créé dans le même dossier que votre objet et nommez-le `multipart.json`. Vous pouvez utiliser n'importe quel IDE de votre choix pour créer et enregistrer ce document.

## Étape 6 : Terminer le téléchargement multipartite vers S3

Pour terminer le téléchargement multipartite, exécutez la commande suivante :

```bash
aws s3api complete-multipart-upload --multipart-upload file://fileparts.json --bucket DOC-EXAMPLE-BUCKET --key large_test_file --upload-id exampleTUVGeKAk3Ob7qMynRKqe3ROcavPRwg92eA6JPD4ybIGRxJx9R0VbgkrnOVphZFK59KCYJAO1PXlrBSW7vcH7ANHZwTTf0ovqe6XPYHwsSp7eTRnXB1qjx40Tk
```

Remplacez `fileparts.json` par `multipart.json`.

Vous devriez obtenir une sortie comme ceci :

```json

{
    "ServerSideEncryption": "AES256",
    "Location": "https://s3-multipart-uploads.s3.eu-west-1.amazonaws.com/videoplayback.mp4",
    "Bucket": "s3-multipart-uploads",
    "Key": "videoplayback.mp4",
    "ETag": "\"78298db673a369adf33dd8054bb6bab7-7\"",
    "ChecksumCRC64NVME": "d1UPkm73mAE=",
    "ChecksumType": "FULL_OBJECT"
}
```

Maintenant, lorsque vous allez dans votre bucket S3 et que vous actualisez, vous devriez voir l'objet téléchargé.

![Image de l'objet téléchargé avec succès sur AWS en utilisant le téléchargement multipartite](https://cdn.hashnode.com/res/hashnode/image/upload/v1753731196794/c7e121d4-f3a7-4d23-95c5-26b1b5e3b699.png align="center")

Ici, vous pouvez voir le fichier complet, le nom du fichier, le type et la taille.

## Conclusion

Les téléchargements multipartites transforment les transferts de grands fichiers vers Amazon S3, passant d'opérations fragiles et tout ou rien à des processus robustes et reprenables. En segmentant les fichiers en morceaux gérables, vous obtenez des capacités de nouvelle tentative, de meilleures performances et la possibilité de gérer des objets dépassant la limite de téléchargement unique de 5 Go de S3.

Cette approche est essentielle pour les environnements de production traitant des sauvegardes de bases de données, des fichiers vidéo ou de tout autre actif volumineux. Avec les techniques AWS CLI couvertes dans ce guide, vous êtes maintenant équipé pour gérer les transferts S3 en toute confiance, quelle que soit la taille des fichiers ou les conditions réseau.

Consultez cette [documentation du centre de connaissances AWS](https://repost.aws/knowledge-center/s3-multipart-upload-cli) pour en savoir plus sur les téléchargements multipartites en utilisant AWS CLI.