---
title: Comment héberger et déployer un site web statique ou une application JAMstack
  sur AWS S3 et CloudFront
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-03-11T13:16:31.000Z'
originalURL: https://freecodecamp.org/news/how-to-host-and-deploy-a-static-website-or-jamstack-app-to-s3-and-cloudfront
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/static-website-in-aws-s3.jpg
tags:
- name: AWS
  slug: aws
- name: beginners guide
  slug: beginners-guide
- name: Cloud
  slug: cloud
- name: Cloud Services
  slug: cloud-services
- name: Cloud Solutions
  slug: cloud-solutions
- name: cloudfront
  slug: cloudfront
- name: HTML
  slug: html
- name: JAMstack
  slug: jamstack
- name: General Programming
  slug: programming
- name: S3
  slug: s3
- name: software development
  slug: software-development
- name: Static Site Generators
  slug: static-site-generators
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
- name: Web Development
  slug: web-development
seo_title: Comment héberger et déployer un site web statique ou une application JAMstack
  sur AWS S3 et CloudFront
seo_desc: 'S3 and CloudFront are AWS cloud services that make serving static assets
  powerful and cheap. How can we host a simple static website or JAMstack app on it?


  A little about AWS

  What are the benefits of serving from S3 and CloudFront?

  Before we start, ...'
---

S3 et CloudFront sont des services cloud AWS qui rendent le service des actifs statiques puissant et économique. Comment pouvons-nous héberger un simple site web statique ou une application JAMstack dessus ?

* [Un peu sur AWS](#heading-un-peu-sur-aws)
* [Quels sont les avantages de servir depuis S3 et CloudFront ?](#heading-quels-sont-les-avantages-de-servir-depuis-s3-et-cloudfront)
* [Avant de commencer, vous aurez besoin d'un compte AWS](#heading-avant-de-commencer-vous-aurez-besoin-dun-compte-aws)
* [Stocker votre site web sur S3](#heading-stocker-votre-site-web-sur-s3)
* [Servir votre site web sur S3](#heading-servir-votre-site-web-sur-s3)
* [Distribuer votre site web sur CloudFront](#heading-distribuer-votre-site-web-sur-cloudfront)
* [Noms de domaine personnalisés](#heading-noms-de-domaine-personnalises)
* [Utilisation avancée d'AWS](#heading-utilisation-avancee-daws)
* [Ressources](#heading-ressources)

%[https://www.youtube.com/watch?v=1lDGDzmbQWg]

## Un peu sur AWS

Si vous n'êtes pas familier, [AWS](https://aws.amazon.com/) (Amazon Web Services) est un fournisseur de services cloud qui offre aux développeurs des opportunités de construire presque tout ce qu'ils peuvent imaginer dans le cloud.

Bien que leurs [services](https://aws.amazon.com/products/) s'étendent au-delà de l'apprentissage automatique et de l'intelligence artificielle, nous allons nous en tenir aux services de niveau d'entrée pour les besoins de ce guide qui nous permettront d'héberger facilement un site web HTML.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/aws-services-overview.jpg)
_Types de services AWS disponibles_

Construire un site avec S3 et CloudFront est une recette courante utilisée par les petites et grandes entreprises sur le web, mais décomposons ce que chaque service fait réellement.

### Stockage d'objets avec S3

[S3](https://aws.amazon.com/s3/) (Simple Storage Service) agit comme votre hébergement pour votre site web statique. Pensez-y comme un disque dur dans le cloud que nous ne pouvons pas utiliser à des fins de traitement, mais plutôt pour le stockage et l'accès à des fichiers simples.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/aws-s3-bucket-file-list.jpg)
_Liste de fichiers d'un site statique dans un bucket AWS S3_

Lorsque qu'une application ou un site web est compilé sous forme statique, c'est tout ce dont nous avons besoin pour le servir aux personnes visitant notre site. Le HTML est envoyé dans la requête initiale "tel quel" (sauf s'il y a un traitement avec votre fournisseur) et tout travail supplémentaire se produit après le chargement de la page dans le navigateur, généralement par JavaScript. Cela nous permet de prendre cette approche simple (et économique) en servant ces fichiers depuis S3.

### Réseau de diffusion de contenu avec CloudFront

[CloudFront](https://aws.amazon.com/cloudfront/) fonctionne comme un [CDN](https://en.wikipedia.org/wiki/Content_delivery_network) (Content Delivery Network) qui se place devant votre site web, mettant en cache les fichiers et les servant directement aux personnes visitant votre site.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/cdn-distribution-map.jpg)
_Diagramme CDN_

L'endroit où vous hébergez et servez votre site web, généralement appelé l'origine, est la source principale de vos fichiers et peut servir le site web lui-même. Mais mettre un CDN devant lui fournit aux personnes accédant à votre contenu un moyen plus court et plus rapide de faire leur requête.

## Quels sont les avantages de servir depuis S3 et CloudFront ?

Étant donné l'essor de l'ère [JAMstack](https://jamstack.org/), de nombreux services apparaissent qui fournissent des services similaires pour les sites statiques, rendant le déploiement très facile. Certains offrent même un niveau gratuit généreux comme [Netlify](https://www.netlify.com/) et [Zeit](https://zeit.co/) !

Mais parfois, les développeurs ont besoin d'un peu plus de contrôle sur leurs services ou ils doivent s'intégrer dans un pipeline cloud plus large qui est déjà à 99 % sur AWS, ce qui est exactement là où S3 excelle. De plus, il y a de fortes chances que, pendant votre première année, vous puissiez encore bénéficier du [niveau gratuit](https://aws.amazon.com/free/) d'AWS.

### Intégration au cadre bien architecturé d'AWS

En tant que principal fournisseur de services cloud, AWS a publié de nombreux guides pour aider les développeurs et les équipes à viser l'excellence dans leurs solutions en termes de performance, de coût et de sécurité.

Une directive particulière est leurs 5 piliers de ce qu'ils décrivent comme une infrastructure "bien architecturée".

![Image](https://www.freecodecamp.org/news/content/images/2020/03/aws-well-architected-framework.jpg)
_Cadre bien architecturé d'AWS_

Par défaut, nous cocherons toutes ces cases avec notre solution d'hébergement en utilisant S3 et CloudFront. Dès la sortie de la boîte, le HTML et les actifs que vous servez seront rapides, économiques, sécurisés et fiables.

### La beauté des sites statiques et JAMstack

En s'appuyant sur les piliers, ce que vous servez réellement est un fichier HTML statique et un groupe d'actifs qui ne nécessiteront aucun type de ressources de rendu lors de la requête initiale. Auparavant, un problème courant était de devoir s'inquiéter qu'un site plante en raison d'une charge élevée. Mais avec S3 et CloudFront, votre site web est infiniment scalable.

Sur une note similaire, lorsque ce serveur monte en charge alors qu'il essaie de servir des millions de visites sur votre publication devenue virale, vos coûts augmenteront également. Servir un site statique est économique et peut grandement réduire le coût associé à l'exécution d'un serveur web.

## Avant de commencer, vous aurez besoin d'un compte AWS

Pour suivre ce guide, vous aurez besoin d'un compte AWS. Heureusement, il est gratuit de créer un compte – vous ne paierez que pour les services utilisés.

En plus de cela, AWS propose un niveau gratuit généreux pour certains de ses services. Certains services offrent seulement 12 mois de niveau gratuit (comme S3) tandis que d'autres sont toujours éligibles pour le niveau gratuit (comme [Lambda](https://aws.amazon.com/lambda/)), alors assurez-vous de faire vos recherches pour ne pas accumuler une facture inattendue élevée.

Pour créer votre compte, rendez-vous sur le site web d'AWS puis continuez pour commencer : [https://aws.amazon.com/](https://aws.amazon.com/).

## Stocker votre site web sur S3

Pour commencer, nous allons commencer par un simple fichier HTML qui servira de site web. Cela nous permettra de nous concentrer davantage sur le processus d'hébergement plutôt que sur les intricacités du site web lui-même.

### Créer notre fichier de site web

Commencez par créer un nouveau dossier appelé `mon-site-statique`. À l'intérieur de ce dossier, créons un nouveau fichier appelé `index.html` et ajoutons ce qui suit au fichier :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mon Site Web Statique</title>
</head>
<body>
  <h1>Bonjour le Monde !</h1>
  <p>Ceci est mon site web statique. ?</p>
</body>
</html>

```

Si vous ouvrez ce fichier depuis votre ordinateur dans votre navigateur préféré, vous devriez maintenant voir ceci.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/hello-world-local-website-file-1.jpg)
_Bonjour le Monde ! Ouverture d'une page web locale_

### Créer un nouveau bucket

Rendez-vous sur votre compte AWS, connectez-vous et naviguez vers votre [console S3](https://s3.console.aws.amazon.com/s3/).

Une fois là-bas, créons notre bucket en cliquant sur le bouton bleu **Créer un bucket** :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/aws-s3-create-bucket.jpg)
_Création d'un bucket dans AWS S3_

La première chose qu'AWS veut que nous fassions est d'entrer un **Nom de bucket**. Le nom du bucket doit être globalement unique, ce qui signifie que le nom que vous utilisez peut être le seul au monde, alors essayons quelque chose comme `[votrenom]-site-statique`, où j'utiliserai `colbyfayock-site-statique`.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/aws-s3-bucket-name.jpg)
_Nommage d'un bucket dans AWS S3_

Ensuite, définissons la [**Région**](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/). Il s'agit de l'emplacement géographique où AWS hébergera le bucket et votre site web. Vous êtes probablement bien avec la valeur par défaut, mais si vous le souhaitez, vous pouvez sélectionner l'emplacement le plus proche de vous s'il est autorisé. Comme je suis en Virginie, je vais rester avec ma valeur par défaut **US East (N. Virginia)**.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/aws-s3-bucket-region.jpg)
_Définition de la région d'un bucket dans AWS S3_

Enfin, cliquez sur le bouton **Créer** en bas à gauche de la page.

_Note : même si vous utilisez le modèle `[votrenom]-site-statique`, il y a une chance que le nom soit déjà pris. Si c'est le cas, AWS affichera une erreur indiquant « Le nom du bucket existe déjà », auquel cas vous devrez essayer un nouveau nom de votre choix._

Alternativement, vous pouvez cliquer sur **Suivant** pour une utilisation avancée, mais pour ce guide, nous sommes satisfaits de toutes les valeurs par défaut fournies par S3.

Si tout se passe bien, vous devriez maintenant voir votre bucket dans la liste sur le tableau de bord de la console S3.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/aws-s3-bucket.jpg)
_Nouveau bucket dans AWS S3_

### Télécharger votre site web dans le bucket

Naviguons vers notre nouveau bucket en cliquant sur la ligne de notre bucket. Vous serez accueilli avec un message indiquant « Ce bucket est vide. Téléchargez de nouveaux objets pour commencer », alors c'est ce que nous allons faire.

Cliquez sur le bouton **Télécharger** pour commencer.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/aws-s3-bucket-upload.jpg)
_Téléchargement de fichiers vers AWS S3_

Vous verrez alors une fenêtre contextuelle qui vous demandera de télécharger un fichier. Cliquez sur le bouton **Ajouter des fichiers** et sélectionnez votre fichier `index.html` que nous avons créé précédemment.

Une fois sélectionné, cliquez sur le bouton **Télécharger** en bas à gauche.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/aws-s3-bucket-upload-files.jpg)
_Sélection des fichiers à télécharger dans AWS S3_

Et maintenant votre fichier est téléchargé sur S3 !

## Servir votre site web sur S3

Si vous essayez de naviguer vers votre fichier `index.html` et de l'ouvrir, vous remarquerez un grand message laid "Accès refusé".

![Image](https://www.freecodecamp.org/news/content/images/2020/03/aws-s3-access-denied.jpg)
_Accès refusé au fichier du bucket_

C'est parce que votre fichier n'a pas actuellement les permissions et les paramètres nécessaires pour servir le fichier au public, alors corrigeons cela.

### Configurer votre bucket comme un site web

Naviguez vers l'onglet **Propriétés** à l'intérieur de votre bucket, puis cliquez sur **Hébergement de site web statique**.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/aws-s3-properties-static-hosting.jpg)
_Configuration d'un bucket AWS S3 pour l'hébergement de site web statique_

Une fois là-bas, nous voulons faire quelques choses :

* Noter le **Point de terminaison** en haut du bloc. Nous l'utiliserons pour accéder à notre site plus tard (vous pouvez toujours le retrouver ici)
* Sélectionner l'option "Utiliser ce bucket pour héberger un site web"
* Entrer `index.html` dans le champ **Document d'index**
* Enfin, cliquer sur **Enregistrer**

![Image](https://www.freecodecamp.org/news/content/images/2020/03/aws-s3-static-website-configuration.jpg)
_Configuration d'un bucket AWS S3 pour l'hébergement de site web statique_

### Configurer la politique et les permissions de votre bucket

Ensuite, naviguez vers l'onglet **Permissions**. Ici, nous voulons faire 2 choses : débloquer tout l'accès public et ajouter une politique de bucket.

Tout d'abord, sur la page principale, cliquons sur **Modifier** pour débloquer tout l'accès.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/aws-s3-bucket-permissions.jpg)
_Configuration des permissions d'un bucket AWS S3_

Ensuite, décochez la case "Bloquer tout accès public" et cliquez sur **Enregistrer**.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/aws-s3-bucket-block-access.jpg)
_Autorisation de l'accès public à un bucket AWS S3_

AWS vous demandera de confirmer ces paramètres, car ce n'est pas toujours ce que vous voulez faire avec votre bucket. Mais pour les besoins de l'hébergement d'un site web, nous voulons que le monde entier le voie, alors tapez le mot "confirm" et cliquez sur le bouton **Confirmer**.

Après confirmation, cliquez sur le bouton **Politique de bucket** et vous serez redirigé vers un éditeur de texte.

Dans cette zone de texte, nous allons coller le snippet suivant. Dans ce snippet, assurez-vous de remplacer `[your-bucket-name]` par le nom de votre bucket, sinon vous ne pourrez pas enregistrer ce fichier.

```json
{
  "Version":"2012-10-17",
  "Statement":[{
	"Sid":"PublicReadGetObject",
        "Effect":"Allow",
	  "Principal": "*",
      "Action":["s3:GetObject"],
      "Resource":["arn:aws:s3:::[your-bucket-name]/*"]
      }]
}

```

[Cette politique](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteAccessPermissionsReqd.html#bucket-policy-static-site) indique qu'elle permet au public d'effectuer une requête GetObject sur la ressource S3, qui est votre bucket S3.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/aws-s3-static-website-bucket-policy.jpg)
_Configuration d'une politique publique pour un bucket AWS S3_

Après avoir ajouté la politique, cliquez sur le bouton **Enregistrer**. Vous devriez maintenant voir un message indiquant "Ce bucket a un accès public."

### Prévisualiser votre nouveau site web de bucket

Si vous avez noté le point de terminaison depuis votre page Propriétés, vous pouvez maintenant visiter cette adresse pour voir votre site web. Le point de terminaison devrait ressembler à ceci :

```plaintext
http://[your-bucket-name].s3-website-[region-id].amazonaws.com

```

Si vous ne l'avez pas fait, remontez de quelques étapes pour vous rappeler comment le trouver ou regardez sous l'onglet Propriétés.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/aws-s3-static-website.jpg)
_Bonjour le Monde ! Ouverture d'un site web AWS S3_

Félicitations, vous êtes à moitié là ! ?

## Distribuer votre site web sur CloudFront

Maintenant que nous avons notre site web statique servi depuis un bucket sur S3, prenons-le à un autre niveau et servons-le à travers le monde en utilisant CloudFront.

### Créer une distribution CloudFront

Naviguez vers votre [tableau de bord CloudFront](https://console.aws.amazon.com/cloudfront) et cliquez sur le bouton **Créer une distribution**.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/aws-cloudfront-create-distribution.jpg)
_Création d'une nouvelle distribution dans AWS CloudFront_

Ensuite, sélectionnez **Commencer** sous la méthode de livraison **Web**.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/aws-cloudfront-creating-web-distribution.jpg)
_Démarrage avec une distribution AWS CloudFront avec livraison Web_

Ici, nous allons entrer quelques paramètres personnalisés pour configurer notre distribution.

Cliquez dans le champ **Nom de domaine d'origine**. Une fois sélectionné, une liste déroulante devrait apparaître où vous pouvez sélectionner le bucket S3 que vous venez de créer. Allez-y et sélectionnez votre bucket S3.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/aws-cloudfront-distribution-origin-name-1.jpg)
_Définition du nom de domaine d'origine dans AWS CloudFront vers votre bucket_

Bien que vous puissiez [personnaliser la plupart des paramètres](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html) selon vos préférences, pour nos besoins, nous allons laisser toutes les valeurs par défaut sauf une.

Faites défiler vers le bas jusqu'au champ **Objet racine par défaut** et tapez `index.html`.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/aws-cloudfront-distribution-default-root-object-1.jpg)
_Définition de l'objet racine par défaut pour une distribution dans AWS CloudFront_

Après cela, faites défiler vers le bas et cliquez sur **Créer une distribution** en bas à droite.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/aws-cloudfront-setup-create-1.jpg)
_Création d'une distribution AWS CloudFront_

### Prévisualiser votre nouvelle distribution CloudFront

Après avoir cliqué sur le bouton **Créer**, il faudra un certain temps pour que votre distribution soit créée et configurée. Vous remarquerez sur la page de liste des **Distributions CloudFront** que le **Statut** de votre nouvelle distribution est **En cours**.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/aws-cloudfront-distribution-in-progress-1.jpg)
_Le déploiement de la distribution AWS CloudFront est en cours_

Une fois cela terminé, il indiquera **Déployé**. Vous pouvez alors trouver votre **Nom de domaine** dans la même ligne.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/aws-cloudfront-distribution-deployed.jpg)
_La distribution AWS CloudFront est déployée_

En utilisant la valeur dans la colonne Nom de domaine, ouvrez votre distribution dans votre navigateur et succès ! Vous visualisez maintenant votre bucket S3 à travers le réseau de distribution de CloudFront.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/aws-cloudfront-static-website-1.jpg)
_Bonjour le Monde ! Ouverture d'un site web AWS CloudFront_

## Noms de domaine personnalisés

Bien que la plupart d'entre nous voudront probablement utiliser un nom de domaine personnalisé avec notre site web, nous n'allons pas approfondir cela dans ce guide, car il existe de nombreuses façons de le configurer en fonction de l'endroit où vous achetez votre nom de domaine.

Cependant, voici quelques éléments à considérer.

### HTTPS / Certificat SSL

Si vous créez votre distribution CloudFront pour l'utiliser avec un nom de domaine personnalisé, vous voudrez probablement configurer votre distribution avec un [certificat SSL](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/) en utilisant le [Gestionnaire de certificats](https://aws.amazon.com/certificate-manager/) d'AWS. Alternativement, vous pouvez fournir votre propre certificat avec des outils comme [Let's Encrypt](https://letsencrypt.org/), mais en utilisant ACM, AWS facilite l'intégration des enregistrements pour une utilisation avec votre distribution.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/fay.io-ssl-certificate.jpg)

Une fois dans ACM, vous voudrez configurer le certificat, mapper les domaines et sous-domaines qui doivent correspondre (généralement `*.domain.com`), puis créer votre certificat à utiliser avec votre distribution.

Pour commencer, vous pouvez consulter le guide AWS pour [demander un certificat public](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-public.html).

### CNAMEs et Alias

Une approche courante pour configurer un domaine personnalisé est d'utiliser un CNAME. CloudFront rend cela assez indolore, car vous l'ajouterez comme option de configuration lorsque vous configurerez votre distribution.

Pour commencer à configurer un CNAME dans CloudFront, [voir le guide AWS](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/CNAMEs.html).

![Image](https://www.freecodecamp.org/news/content/images/2020/03/fay.io-route53-alias.jpg)

Si vous utilisez [Route53](https://aws.amazon.com/route53/) pour gérer votre [DNS](https://www.cloudflare.com/learning/dns/what-is-dns/), vous pouvez ensuite configurer un enregistrement A (alias) pour pointer vers votre distribution. Vous pouvez en savoir plus [en utilisant ce guide](https://aws.amazon.com/premiumsupport/knowledge-center/route-53-create-alias-records/).

## Utilisation avancée d'AWS

Pour ce guide, nous vous avons montré comment configurer un nouveau site web statique et une application en utilisant la console AWS. Mais que vous souhaitiez en apprendre davantage, améliorer l'efficacité de votre déploiement ou automatiser ce processus, vous voudrez aller plus loin avec l'AWS CLI ou CloudFormation.

Bien que nous ne vous montrerons pas comment utiliser ces outils ici, nous vous donnerons une petite idée de ce à quoi vous êtes confronté.

### AWS CLI

L'[AWS CLI](https://aws.amazon.com/cli/) permet à quelqu'un d'effectuer des opérations AWS depuis la ligne de commande. Cela peut être incroyablement puissant lorsque vous souhaitez scripter la création de vos ressources ou si vous préférez simplement faire tout votre travail depuis le terminal.

Une fois configuré localement, vous pourrez effectuer des actions comme créer un bucket en utilisant la commande suivante :

```shell
aws s3api create-bucket --bucket [your-bucket-name] --region [bucket-region]
```

Pour commencer, consultez la page [Github de l'AWS CLI](https://github.com/aws/aws-cli) ou le [Guide de l'utilisateur de l'AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html).

### AWS CloudFormation

AWS prêche l'infrastructure en tant que code. C'est l'idée que vous pouvez lancer votre infrastructure en utilisant quelque chose qui est écrit dans un fichier, où dans ce cas particulier, ce serait un modèle CloudFormation. Cela vous permet d'avoir un processus reproductible qui sera le même à chaque fois que vous effectuerez le déploiement.

[CloudFormation](https://aws.amazon.com/cloudformation/) vous permet de configurer un fichier de configuration qui déploiera les services et ressources de votre choix en pointant vers ce fichier avec le CLI ou en le téléchargeant dans la console.

Voici un [exemple d'AWS](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-s3.html#scenario-s3-bucket-website) de ce à quoi cela ressemble pour un bucket S3 statique qui pourrait servir de site web.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/aws-cloudformation-template-s3.jpg)
_Exemple de modèle AWS CloudFront_

Pour commencer, consultez les [modèles d'exemples](https://aws.amazon.com/cloudformation/resources/templates/) de CloudFormation d'AWS ou leur [guide de démarrage](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/GettingStarted.Walkthrough.html).

## Ressources

Si vous êtes intéressé à approfondir l'écosystème AWS, voici quelques ressources pour commencer :

* [Formation AWS Certified Cloud Practitioner 2019 - Un cours vidéo gratuit de 4 heures](https://www.freecodecamp.org/news/aws-certified-cloud-practitioner-training-2019-free-video-course/) (freeCodeCamp.org)
* [Présentation du défi #AWSCertified : Un chemin vers vos premières certifications AWS](https://www.freecodecamp.org/news/awscertified-challenge-free-path-aws-cloud-certifications/) (freeCodeCamp.org)
* [Tutoriels de 10 minutes](https://aws.amazon.com/getting-started/tutorials/) (AWS)
* [A Cloud Guru](https://acloud.guru/) (Cours payants)
* [Études de cas AWS](https://aws.amazon.com/solutions/case-studies/) (AWS)

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Follow Me On Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">?f3a5 Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;"> 2709 fe0f Sign Up For My Newsletter</a>
    </li>
  </ul>
</div>