---
title: Comment configurer le déploiement continu vers AWS S3 en utilisant CircleCI
  en seulement 30 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-04-28T18:01:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-continuous-deployment-to-aws-s3-using-circleci-in-under-30-minutes-a8e268284098
coverImage: https://cdn-media-1.freecodecamp.org/images/1*iEPDwncshci0-coGQn96Cg.jpeg
tags:
- name: AWS
  slug: aws
- name: CircleCI
  slug: circleci
- name: Devops
  slug: devops
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Comment configurer le déploiement continu vers AWS S3 en utilisant CircleCI
  en seulement 30 minutes
seo_desc: 'By Adam Watt

  Continuous Deployment might seem complicated at first, but don’t be intimidated.
  In this tutorial, I’ll show you how to implement Continuous Deployment to AWS S3
  for a static website using CircleCI in less than 30 minutes.

  You’ll need bo...'
---

Par Adam Watt

Le déploiement continu peut sembler compliqué au premier abord, mais ne vous laissez pas intimider. Dans ce tutoriel, je vais vous montrer comment implémenter le déploiement continu vers AWS S3 pour un site web statique en utilisant CircleCI en moins de 30 minutes.

Vous aurez besoin d'un compte AWS et d'un compte CircleCI. Si vous n'avez pas encore ces comptes, commencez par ouvrir un compte gratuit pour AWS [ici](https://aws.amazon.com/free) et un compte gratuit CircleCI [ici](https://circleci.com/signup/). AWS et CircleCI ont tous deux un niveau gratuit qui est plus que suffisant pour ce dont vous aurez besoin pour ce tutoriel.

### Obtenir le code

Tout d'abord, vous allez commencer par forker et cloner le projet suivant sur Github : [S3ContinuousDeploy](https://github.com/AWattNY/S3ContinuousDeploy) ou, si vous préférez, vous pouvez essayer ce tutoriel avec l'un de vos propres dépôts, tant qu'il s'agit d'un site statique.

Ensuite, vous allez ajouter le projet à votre compte CircleCI.

![Image](https://cdn-media-1.freecodecamp.org/images/1*rpHcpF4I7W0mDu1H0WvgUg.png)

Ensuite, sélectionnez le dépôt S3ContinuousDeploy que vous venez de cloner et cliquez sur "build project".

![Image](https://cdn-media-1.freecodecamp.org/images/1*_dnV50_unj8H9RODMVQQYg.png)
_Choisissez le dépôt S3ContinuousDeploy et cliquez sur "build project"_

À ce stade, la construction va s'exécuter, mais vous allez recevoir un message d'erreur vous avertissant que les paramètres de votre projet n'ont pas pu être détectés. Ce qui est normal puisque nous n'avons pas de fichier de configuration circle.yml en place, ce que vous allez faire ensuite.

![Image](https://cdn-media-1.freecodecamp.org/images/1*PDeB4RAPCc2_kmD3dBS92g.png)

En consultant la documentation de CircleCI, vous pouvez vous faire une idée de ce à quoi le fichier circle.yml devrait ressembler. Malheureusement, l'exemple de fichier circle.yml fourni ne fonctionnera pas tel quel et nécessitera quelques ajustements, alors faisons cela.

Voici le fichier circle.yml modifié que vous allez utiliser :

```yaml
machine:
  python:
    version: 2.7.12

dependencies:
  override:
    - pip install awscli
```

En gros, CircleCI crée la construction dans un conteneur Docker, et le remplacement sous la propriété des dépendances (ligne 3) que j'ai ajouté instructe CircleCI d'installer l'interface de ligne de commande AWS (awscli) qui sera utilisée dans ce cas pour aider à gérer et faciliter le déploiement vers AWS S3.

Assurez-vous donc d'ajouter le fichier et de le commiter dans votre dépôt. Enfin, assurez-vous de pousser ce commit et les autres commits que vous auriez pu faire avant de passer à l'étape suivante.

Selon la documentation de CircleCI, la commande pour le déploiement est :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZUGQqjk7ozjUk6pnXu-LOg.png)

Le chemin vers le fichier était un peu difficile à déterminer, mais en regardant les journaux d'erreurs, j'ai finalement réussi à le trouver : home\ubuntu\projectName. Il suffit de remplacer projectName par le nom de votre projet, dans mon cas, ce sera S3ContinuousDeploy.

L'URL du bucket S3://bucket-URL, en revanche, n'est pas correcte et devrait être S3://bucket-Name. Pour l'instant, nous n'avons pas de nom de bucket, alors obtenons-nous un bucket.

### Créer le bucket S3

Dans cette étape, nous allons nous rendre dans la console AWS pour créer le bucket S3 pour ce projet :

![Image](https://cdn-media-1.freecodecamp.org/images/1*09G_AT9IHbI6tNiLGew1Sg.png)
_Dans votre console, allez dans Stockage puis dans S3_

![Image](https://cdn-media-1.freecodecamp.org/images/1*R1EUamf6tJuw1mdjTOXAbg.png)
_Appuyez sur Créer un bucket_

Entrez le nom du bucket que vous souhaitez utiliser pour ce projet ainsi que la région. (La meilleure pratique est d'utiliser la région la plus proche de l'audience de votre site.)

![Image](https://cdn-media-1.freecodecamp.org/images/1*gs2tyd8N7P3N8LRAbfvzoQ.png)

Vous allez sauter les autres étapes pour l'instant, alors appuyez sur « Suivant » puis sur « Créer un bucket » sur l'écran de révision.

À ce stade, si vous retournez à CircleCI et essayez de relancer la construction, CircleCI retournera une erreur fatale : Impossible de localiser les identifiants. Alors pourquoi ne pas corriger cela ensuite.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vfzxm4Ob1NzwGbFLu9MNZg.png)

Nous devons d'abord obtenir les identifiants d'AWS, puis les fournir à CircleCI afin de permettre à l'interface de ligne de commande AWS d'accéder et de gérer le bucket S3. La meilleure pratique pour cela est de créer un nouvel utilisateur Identity and Access Management (IAM) spécifiquement pour CircleCI.

Dans la console AWS, allez dans Sécurité, Identité et Conformité et appuyez sur IAM puis sur Ajouter un utilisateur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5URhjWCf_Cva14j10iC9lQ.png)

Dans la fenêtre Ajouter un utilisateur, tapez CircleCI pour le nom d'utilisateur. J'ai déjà un utilisateur IAM nommé CircleCI configuré, donc pour les besoins de ce tutoriel et pour illustrer ces étapes, j'utiliserai CircleCI2. Assurez-vous de cocher Accès programmatique pour le type d'accès.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8E2Zq-4Rf6zayOnXlu0xiw.png)

Pour les permissions, choisissez Attacher des politiques existantes directement, et sous Nom de la politique, cochez 'AdministratorAccess' puis cliquez sur Créer une politique. Cela fournira à votre utilisateur IAM un accès complet à votre bucket AWS S3.

![Image](https://cdn-media-1.freecodecamp.org/images/1*mSW3jMhrBXujFE1RbfcdnA.png)

Après avoir créé l'utilisateur IAM, assurez-vous de conserver à la fois l'ID de la clé d'accès et la clé d'accès secrète, car nous en aurons besoin à l'étape suivante.

![Image](https://cdn-media-1.freecodecamp.org/images/1*N58N_nM1aeh2TV2K0nB1EA.png)

Maintenant, retournez à CircleCI, cliquez sur le bouton des paramètres à côté du nom de votre projet pour révéler le menu des paramètres du projet, puis cliquez sur AWS Permissions. C'est ici que vous allez coller l'ID et la clé de l'étape précédente, puis cliquez sur "Enregistrer les clés AWS".

![Image](https://cdn-media-1.freecodecamp.org/images/1*nL8EUSt2c0udyOdQQ-NC0A.png)

Maintenant, notre conteneur CircleCI dispose à la fois de l'outil d'interface de ligne de commande AWS et des identifiants pour accéder au bucket AWS S3. Les étapes suivantes vous montreront comment révéler votre site statique au monde.

Dans la console AWS, allez dans Stockage, puis cliquez sur S3, puis cliquez sur le bucket que nous avons créé plus tôt dans ce tutoriel.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2HqAqD8aNKhIrJlKuT25nw.png)

Vous remarquerez que le code du dépôt a déjà été déployé avec succès.

![Image](https://cdn-media-1.freecodecamp.org/images/1*IVZMtV4e7Txu4l6FFW0SOg.png)

Maintenant, avant de pouvoir accéder à ce site statique, vous devez configurer votre bucket S3 pour l'hébergement de site web.

Sur le même écran, cliquez sur Propriétés, puis sur Hébergement de site web statique.

![Image](https://cdn-media-1.freecodecamp.org/images/1*cdQFxfsKAfLu3pUqb-bUGw.png)

Dans l'écran suivant, sélectionnez Utiliser ce bucket pour héberger un site web et assurez-vous de taper index.html pour Document d'index.

![Image](https://cdn-media-1.freecodecamp.org/images/1*YbdCVHxvWBpxyA-Q6B8eTQ.png)

Au fait, l'adresse HTTP fournie ci-dessus est votre point de terminaison d'accès. Mais si vous l'essayez dans le navigateur, malheureusement, cela ne fonctionnera pas et vous obtiendrez un message d'erreur d'accès refusé. Mais c'est normal, il vous reste une étape à faire : Configurer votre politique de bucket.

Cette politique de bucket permettra l'accès au bucket AWS S3 à quiconque via un navigateur.

Vous pouvez lire [ici](http://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html) sur les politiques de bucket et des exemples si vous souhaitez en savoir plus.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CJ0YNFnZWV3WA4wrP-uwKQ.png)

Maintenant, vous pouvez copier l'extrait de code ci-dessus et le coller dans votre éditeur de politique de bucket et voilà !

![Image](https://cdn-media-1.freecodecamp.org/images/1*gD8DcazPynHucGTlBGu5dg.png)

Si vous voyez l'écran ci-dessus, alors félicitations ! Vous avez réussi à configurer le déploiement continu vers un bucket AWS S3 en utilisant CircleCI.

Maintenant, chaque fois que vous pousserez des modifications vers votre dépôt Github, CircleCI déployera automatiquement les modifications vers votre bucket AWS S3.

Vous avez peut-être remarqué que même si le déploiement a réussi, CircleCI vous montre un avertissement rouge NO TESTS.

![Image](https://cdn-media-1.freecodecamp.org/images/1*QPWUzhV3CetGhRarc2HEaQ.png)

Cela est normal car dans un environnement de développement piloté par les tests (TDD), vous écriviez d'abord les tests, et ensuite, avant de passer en production, votre code doit passer tous les tests. Un exemple avec des tests dépasse le cadre de ce tutoriel, mais il suffit de dire que si nous avions écrit des tests, CircleCI n'aurait déployé que si tous nos tests avaient réussi.

L'utilisation de votre propre nom de domaine pour accéder à ce site statique dépasse également le cadre de ce tutoriel, mais n'hésitez pas à consulter [ici](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/setting-up-route-53.html) pour des instructions sur la configuration d'Amazon Route 53 afin de router le trafic Internet vers votre nouveau site.

J'espère faire un tutoriel impliquant un exemple d'intégration/deploiement continu avec une batterie complète de tests parfois dans le futur. En attendant, si vous avez un moment, répondez à une courte enquête sur ce tutoriel [ici](https://goo.gl/forms/aJl610F4ltAvMDBv1), aimez-le sur [LinkedIn](https://www.linkedin.com/pulse/how-set-up-continuous-deployment-aws-s3-using-circleci-adam-watt) ou postez un commentaire dans la section des commentaires.

Merci d'avoir lu !