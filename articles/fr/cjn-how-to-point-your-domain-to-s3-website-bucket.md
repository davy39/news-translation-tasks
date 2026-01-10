---
title: Comment pointer votre domaine vers un bucket S3 Website
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-21T00:08:34.000Z'
originalURL: https://freecodecamp.org/news/cjn-how-to-point-your-domain-to-s3-website-bucket
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/domain_name_point_to_s3_bucket.png
tags:
- name: dns
  slug: dns
- name: S3
  slug: s3
- name: Web Hosting
  slug: web-hosting
- name: website development,
  slug: website-development
seo_title: Comment pointer votre domaine vers un bucket S3 Website
seo_desc: 'By Clark Jason Ngo

  If you''re hosting a static website in an S3 bucket and it''s your first time buying
  a domain name, this simple guide is for you.

  Summary - What You Need

  Amazon S3


  Have an S3 bucket with the same name as your domain name

  Upload your...'
---

Par Clark Jason Ngo

Si vous hébergez un site web statique dans un bucket S3 et que c'est la première fois que vous achetez un nom de domaine, ce guide simple est fait pour vous.

## Résumé - Ce dont vous avez besoin

### Amazon S3

* Avoir un bucket S3 avec le même nom que votre nom de domaine
* Télécharger le code de votre site web
* Autoriser l'accès public
* Ajouter une politique pour activer S3 GetObject
* Activer l'hébergement de site web statique

### Fournisseur de nom de domaine

* Dans les paramètres de la zone DNS de votre nom de domaine, supprimez tous les enregistrements **A**
* Dans les paramètres de la zone DNS, ajoutez _www_ au **sous-domaine** et l'endpoint S3 dans le nom d'hôte pour les enregistrements **CNAME**

Passons en revue ces étapes une par une.

## Étape 1 : Créer un bucket S3

Créez un bucket S3 pour héberger vos fichiers pour votre site web

Tout d'abord, vous devez créer un bucket pour votre site web. Le nom de votre bucket doit être le même que votre nom de domaine. Supposons que nous ayons acheté le nom de domaine **www.clarkngo.net**. Alors le nom de mon bucket S3 doit être **www.clarkngo.net** également.

Après configuration, mon endpoint devrait ressembler à ceci :

http://www.clarkngo.net.s3-website-us-west-2.amazonaws.com

Allez dans votre console AWS et connectez-vous. Choisissez S3.

1. Cliquez sur **Buckets**
2. Cliquez sur **Créer un bucket**

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-119.png)

3. Ajoutez votre nom de domaine dans le **nom du bucket**

4. Vous pouvez choisir n'importe quelle **Région**

### Création du bucket S3 et configuration générale

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-118.png)

Suivez les cases à cocher ci-dessous et cliquez sur **Créer un bucket**.

Cochez uniquement les éléments suivants :

* **Bloquer l'accès public au bucket et aux objets accordé via les _nouvelles_ listes de contrôle d'accès (ACL)**
* **Bloquer l'accès public au bucket et aux objets accordé via _toutes_ les listes de contrôle d'accès (ACL)**

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-120.png)

### Téléchargement de fichiers vers le bucket S3

1. Cliquez sur **Vue d'ensemble** et **Télécharger**.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-121.png)

2. Téléchargez vos fichiers de site web dans **Sélectionner des fichiers**

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-122.png)

3. Pour **Définir les permissions**, cliquez sur **Suivant**.

4. Pour **Définir les propriétés**, cliquez sur **Suivant**. (Le standard est S3 par défaut.)

5. Pour **Révision**, cliquez sur **Télécharger**.

### Édition de la politique du bucket

1. Cliquez sur **Permissions**, puis **Politique du bucket**.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-123.png)

2. Ajoutez la politique. (Note : Pour votre site web, vous changerez **arn:aws::s3:::www.clarkngo.net/***)

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-124.png)

```
{
    "Version": "2012-10-17",
    "Id": "Policy1548223592786",
    "Statement": [
        {
            "Sid": "Stmt1548223591553",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::www.clarkngo.net/*"
        }
    ]
}
```

3. Cliquez sur **Enregistrer**.

### Hébergement de site web statique

1. Cliquez sur **Propriétés**, puis **Hébergement de site web statique**.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-125.png)

2. Choisissez **Utiliser ce bucket pour héberger un site web**.

3. Pour le document d'index, tapez _index.html_.

4. Pour le document d'erreur, tapez _index.html_.

5. Cliquez sur **Enregistrer**.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-126.png)

## Étape 2 : Ajouter l'endpoint S3 à votre domaine

### Édition de votre zone DNS

1. Connectez-vous à votre fournisseur de domaine.
2. Dans cet exemple, choisissez **Serveurs de noms/DNS**, puis **Modifier la zone DNS** (ou l'équivalent).

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-127.png)

3. Supprimez tous les enregistrements **A** de votre domaine. Habituellement, il y aura une adresse IP par défaut pour une page 404 Not Found.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-128.png)

4. Ajoutez un **CNAME** pour pointer vers le bucket S3 :

* ajoutez **www** pour le sous-domaine.
* ajoutez **www.clarkngo.net.s3-website-us-west-2.amazonaws.com** (l'endpoint S3) à l'hôte.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-129.png)

Et c'est tout ! Notez qu'il peut falloir un certain temps pour que vos nouveaux paramètres prennent effet.

Connectez-vous avec moi sur LinkedIn [ici](https://www.linkedin.com/in/clarkngo/).

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-133.png)