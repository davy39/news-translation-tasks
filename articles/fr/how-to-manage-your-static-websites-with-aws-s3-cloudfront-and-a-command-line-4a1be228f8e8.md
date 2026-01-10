---
title: Comment gérer vos sites statiques avec AWS S3, CloudFront et une ligne de commande
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-09-14T00:17:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-manage-your-static-websites-with-aws-s3-cloudfront-and-a-command-line-4a1be228f8e8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*zxIISvYq2_dz4R3THj17pA.jpeg
tags:
- name: AWS
  slug: aws
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment gérer vos sites statiques avec AWS S3, CloudFront et une ligne
  de commande
seo_desc: 'By Ben Cheng

  Here’s a short list of things you shouldn’t need to worry about when setting up
  a static website:


  scaling up your servers for surges in traffic

  logging into the AWS Management Console just to upload a new index.html file

  spending US$5 t...'
---

Par Ben Cheng

Voici une courte liste de choses dont vous ne devriez pas avoir à vous soucier lors de la configuration d'un site statique :

* mettre à l'échelle vos serveurs pour les pics de trafic
* vous connecter à la console de gestion AWS juste pour télécharger un nouveau fichier index.html
* dépenser 5 USD pour héberger un seul site statique

J'en avais assez de m'inquiéter de ces choses. J'ai donc appris un peu de Go, développé un petit outil en ligne de commande pendant le week-end, et je l'ai open-sourcé.

[AWS S3](https://aws.amazon.com/s3) est une option abordable pour l'hébergement (et gratuit pour les nouveaux utilisateurs), et AWS [CloudFront](https://aws.amazon.com/cloudfront/) est bon pour le CDN. Mais configurer les deux est fastidieux. La liste de contrôle est assez longue :

1. configurer correctement S3
2. configurer CloudFront
3. s'assurer que vous avez suivi les meilleures pratiques telles que la redirection HTTP -> HTTPS
4. synchroniser les fichiers
5. invalider CloudFront pour les mises à jour.

Heureusement, mon outil open source [AWS-site-manager](https://github.com/oursky/aws-site-manager) rend l'hébergement et la mise à jour d'un site statique aussi simple qu'une seule ligne de commande.

AWS Site Manager est un outil simple en ligne de commande qui facilite l'hébergement d'un site web statique avec AWS S3 et CloudFront, sans enfreindre les meilleures pratiques.

Si c'est la première fois que vous hébergez un site, créez un compte AWS et enregistrez votre nom de domaine avec un service tel que [Namecheap](https://www.namecheap.com/) (assurez-vous d'utiliser leur coupon de réduction mensuel).

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZcHHO4Em6dZ7FA87kM4j3g.png)

### Pourquoi utiliser S3 et CloudFront pour les sites statiques ?

Étant donné tous les tracas, pourquoi s'embêter avec S3 et CloudFront ? Les deux principales raisons sont :

1. Abordabilité des fonctionnalités (par rapport au dyno gratuit Heroku — qui s'arrête lorsque vous atteignez leur limite d'inactivité — ou Github.io — qui ne supporte pas HTTPS avec des domaines personnalisés)
2. Vitesse (CloudFront est un CDN bon marché, mais acceptable)

Étant donné les avantages, le seul obstacle était la configuration, nous avons donc créé un outil en ligne de commande pour une utilisation future pratique. Ci-dessous, je vais vous guider à travers la configuration de ce gestionnaire de site open source.

### [AWS-site-manager](https://github.com/oursky/aws-site-manager) fait 2 choses :

#### 1. Configurer S3 et CloudFront avec une configuration opinionnée :

* Créer des buckets S3
* Configurer la distribution CloudFront et configurer le CNAME
* Télécharger et configurer des certificats HTTPS personnalisés
* Rediriger www vers des domaines nus pour un meilleur SEO
* Rediriger HTTP vers HTTPS pour un meilleur SEO (si HTTPS est activé)
* _Configurer IAM / certificat let's encrypt automatiquement (bientôt disponible)_

#### 2. Synchroniser un dossier local avec S3

* Compresser les fichiers en Gzip pour une meilleure vitesse du site _(sera remplacé par le paramètre Gzip de CloudFront)_
* Paramètres par défaut sensés pour l'en-tête HTTP (type MIME correct, max-age=900, etag, etc.)
* Invalider la distribution CloudFront pour les fichiers synchronisés

### Pour commencer : Installation

Téléchargez le binaire pour Linux / Mac / Windows [ici](https://github.com/oursky/aws-site-manager/releases/).

Ou compilez à partir des sources : Si vous avez [Go 1.6 ou supérieur installé](https://golang.org/dl/), exécutez la commande suivante :

### **Comment utiliser AWS Site Manager**

#### 1. Configurer les identifiants AWS et la configuration.

Si vous n'avez pas encore configuré les identifiants AWS sur votre environnement, vous pouvez le faire en ajoutant les lignes suivantes dans `~/.aws/credentials`.

Et dans `~/.aws/config`

Vous devez également définir la variable d'environnement AWS_SDK_LOAD_CONFIG  
 Si vous êtes sous Linux / Mac et utilisez bash, ajoutez la ligne suivante dans `~/.bashrc`

Vous pouvez en savoir plus sur la configuration de l'AWS CLI dans sa [documentation officielle](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html).

#### 2. Utilisez-le !

En supposant que vous allez configurer un site web example.com et [www.example.com](http://www.example.com), vous pouvez :

Les commandes ci-dessus vont :

* configurer un bucket S3 example.com et [www.example.com](http://www.example.com)
* synchroniser tous les fichiers dans le dossier local
* rediriger [www.example.com](http://www.example.com) vers example.com

Si vous souhaitez utiliser https et avez le certificat au format PEM prêt, exécutez les commandes suivantes pour configurer HTTPS. (si votre registre SSL vous a envoyé des fichiers `.key` / `.crt`, [lisez ceci](http://stackoverflow.com/questions/991758/how-to-get-an-openssl-pem-file-from-key-and-crt-files))

Enfin, vous devez configurer la correspondance DNS avec le point de terminaison de votre distribution CloudFront. Pensez à utiliser AWS [Route-53](https://aws.amazon.com/route53/) pour cela.

Vous devez configurer un enregistrement CNAME pour pointer votre nom de domaine vers la distribution CloudFront. Vous pouvez obtenir le nom de domaine CloudFront depuis la console de gestion AWS, puis configurer le CNAME de votre domaine vers ce nom de domaine.

![Image](https://cdn-media-1.freecodecamp.org/images/1*TGXROtf37r5f-_ysbdornQ.png)

Si vous devez mettre à jour le site, exécutez simplement `aws-site-manager sync --domain example.com` dans le dossier et la commande comparera les changements de fichiers, téléchargera les nouveaux fichiers vers S3 et invalidera le cache CloudFront pour vous.

### Allez-y et lancez

Ce projet a résolu un problème récurrent pour moi et mon équipe chez [Oursky](https://github.com/oursky). En plus de construire des applications mobiles et web, nous créons souvent des sites statiques ponctuels que nous voulons pouvoir mettre à jour facilement de temps en temps.

[AWS-site-manager](https://github.com/oursky/aws-site-manager) est open source et en phase préliminaire. Si vous souhaitez contribuer, vous pouvez créer des issues ou soumettre une pull request.

Si vous avez des questions sur ce projet ou sur les solutions serverless en général, vous pouvez me contacter ici ou sur [Twitter](https://twitter.com/chpapa). Ou, si vous passez un jour par Hong Kong, venez visiter mon bureau pour discuter !

Bonne chance !

PS : Mon entreprise travaille également sur un autre projet open source appelé [Skygear.io](http://www.skygear.io/), qui est un BaaS gratuit incluant des fonctionnalités telles que le chat, les réseaux sociaux, les bots, les connexions sociales, la synchronisation de données en temps réel et hors ligne, le CMS pour mobile, la gestion des utilisateurs, etc.