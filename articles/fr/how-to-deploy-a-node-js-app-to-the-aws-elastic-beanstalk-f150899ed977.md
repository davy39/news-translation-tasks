---
title: Comment déployer une application Node.js sur AWS Elastic Beanstalk
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-16T08:02:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-a-node-js-app-to-the-aws-elastic-beanstalk-f150899ed977
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_qUFovbRz-UBf4GAEwgnlw.jpeg
tags:
- name: AWS
  slug: aws
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment déployer une application Node.js sur AWS Elastic Beanstalk
seo_desc: 'By Jared Nutt

  It took me the better part of a month to figure out how to setup an Amazon Web Services
  (AWS) account, configure a Node.js app for deploying, and then actually deploy it.

  A lot of that was trying to decipher Amazon’s documentation. Hope...'
---

Par Jared Nutt

Il m'a fallu près d'un mois pour comprendre comment configurer un compte Amazon Web Services (AWS), configurer une application Node.js pour le déploiement, puis la déployer réellement.

Une grande partie de cela consistait à essayer de déchiffrer la documentation d'Amazon. Espérons que ce guide vous mettra sur la voie du déploiement de local à live sans trop de maux de tête.

Je suis situé à Los Angeles, donc lorsque vous configurez votre configuration, les valeurs par défaut peuvent ne pas être exactement les mêmes.

### Prérequis

1. Connaissances de base de la ligne de commande  
Je suis sûr que vous pouvez faire cela sans la ligne de commande, mais c'est beaucoup plus facile d'utiliser le CLI
2. Un compte AWS
3. L'interface de ligne de commande Elastic Beanstalk (EB CLI)  
Instructions d'installation ci-dessous
4. Connaissances de base de Git

### Configuration d'un compte AWS

La première chose à faire est de configurer un compte AWS. Si vous avez déjà un compte, assurez-vous d'avoir un utilisateur IAM qui dispose de clés API et de l'accès approprié.

#### **Créer un compte**

Assez simple. Créez un compte. Le processus d'inscription devrait vous guider à travers tout assez facilement. Lorsque vous configurez pour la première fois un compte AWS, vous obtiendrez un accès root. Cependant, il est recommandé de créer un utilisateur séparé que vous utiliserez pour vous connecter régulièrement.

#### **Configurer votre IAM**

**NOTE :** Je ne suis pas un expert en AWS Identity and Access Management (IAM). Les actions que j'ai entreprises étaient pour mon propre cas d'utilisation personnel et peuvent ne pas être adaptées à vos besoins. Passez en revue les permissions de manière approfondie avant de donner accès aux utilisateurs.

AWS publie régulièrement les meilleures pratiques, obtenez-en une de 2016 [ici](https://aws.amazon.com/blogs/security/adhere-to-iam-best-practices-in-2016/).

#### **Configurer un groupe**

Avant de configurer un utilisateur pour vous connecter, créez un groupe qui gérera les permissions. Dans mon cas, j'ai configuré un groupe **SuperAdmin** dans lequel je vais me mettre pour avoir accès à tout.

Pour ce groupe, puisque c'est essentiellement pour me connecter et avoir accès à tout, j'ai choisi AdministratorAccess comme permission.

![Image](https://cdn-media-1.freecodecamp.org/images/sbLmYlWNmFCX0afmNBLEicn6XUr0YDXZfXOY)

Pour plus d'informations sur les groupes IAM, allez [ici](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups.html).

#### **Configurer un utilisateur IAM**

La configuration d'un utilisateur est assez simple, mais si vous êtes bloqué, consultez la [page IAM](https://aws.amazon.com/iam/getting-started/) pour AWS. Ils ont beaucoup de vidéos utiles.

N'oubliez pas de :

1. Leur donner des permissions de clé d'accès  
(voir l'image ci-dessous)
2. Les assigner au groupe IAM approprié

![Image](https://cdn-media-1.freecodecamp.org/images/ymH6gZep9rfUud9YYBYcy548UK1RKAOdmW4D)

Une fois que vous avez configuré votre propre utilisateur, déconnectez-vous du root et reconnectez-vous en tant que votre nouvel utilisateur IAM.

### Configuration de l'environnement local

Maintenant que nous avons nos clés de compte prêtes, commençons avec le déploiement.

#### Qu'est-ce qu'Elastic Beanstalk ?

Elastic Beanstalk (EB) est un moyen assez simple de configurer des applications scalables. Il utilise des instances Amazon Elastic Compute Cloud (EC2), des buckets Amazon Simple Storage Service (S3) et des équilibreurs de charge pour gérer l'architecture de votre application pour vous.

Si vous devez rapidement monter en puissance en raison de la demande du réseau, il le fera. Il est également vraiment amazing pour pousser les mises à jour car il peut faire des "mises à jour en continu", qui permettent à l'application de rester en ligne pendant que vous mettez à jour. Sympa.

#### Comment éviter qu'Elastic Beanstalk ne vous coûte une fortune

Cela ne s'applique qu'aux nouveaux utilisateurs qui qualifient encore pour le plan gratuit :

1. Vous obtenez 750 heures de temps EC2 t2.micro par mois. Cela vous donnera assez pour faire fonctionner un seul serveur à plein temps.   
Cependant, si vous ajoutez un autre serveur, vous allez payer pour celui-ci.
2. Vous pourriez basculer toute votre logique de serveur vers des fonctions Lambda, mais c'est un sujet pour un autre jour (et il y a aussi quelques inconvénients).  
Si vous êtes intéressé, consultez cet [article](https://medium.freecodecamp.org/how-i-cut-my-aws-bill-by-90-35c937596f0c).

#### Combien cela va-t-il coûter ?

Bonne question. Voici un exemple de ma facture. Cela inclut l'application Node.js en cours d'exécution dont je parle dans cet article (EB, Cloudfront, S3 Buckets).

![Image](https://cdn-media-1.freecodecamp.org/images/dyjdFxzZRhLzbphtHPsoXroWDc33l2Z-V1Jy)

Si vous vous demandez combien cela coûtera après la fin du plan gratuit, consultez [ceci](https://calculator.s3.amazonaws.com/index.html#key=calc-BeanstalkDefault-140324).

### Création d'un environnement EB dans votre application

Ce n'est pas un tutoriel Node.js, car cela dépasse le cadre de cet article. Mais si vous avez besoin d'une application pour vous amuser, consultez le [générateur d'applications Express](https://expressjs.com/en/starter/generator.html). Il vous donnera au moins un "Hello World". C'est ce que j'ai utilisé comme `init` pour mon projet.

En continuant, il est supposé que vous avez déjà une application Node.js qui fonctionne localement sans problème.

#### Configuration de l'EB CLI

La première chose à faire est de faire fonctionner le CLI AWS/EB, ce qui consiste simplement à installer quelques outils et à configurer la configuration.

Les documents AWS font un meilleur travail pour l'expliquer que je ne pourrais jamais le faire, alors consultez-les [ici](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install.html).

**Note :** Si vous avez des problèmes avec les clés API, vous pouvez les vérifier/modifier en éditant le fichier de configuration.

```
open ~/.aws/config
```

### Déploiement initial

Maintenant que nous avons tous nos outils en ligne, que faire ensuite ?

```
eb init
```

Lorsque vous exécutez cette commande, elle va vous poser un tas de questions :

1. On vous demandera de choisir une région.  
Par défaut, c'est us-west-2 : US West (Oregon)
2. Elle vous demandera quelle application utiliser ou en créer une nouvelle.  
La première option devrait être d'en créer une nouvelle.
3. Elle vous demandera si vous voulez utiliser AWS CodeCommit.  
Je n'ai aucune expérience avec cela, mais j'utilise simplement GitHub, alors j'ai dit non.

#### Configurer vos variables d'environnement

Cela a probablement été mon plus gros point de douleur. Je ne sais pas si mon cerveau a survolé la documentation, ou quoi. Une fois que j'ai compris, c'est en fait vraiment simple. Et les fichiers de configuration sont écrits en YAML 💜.

![Image](https://cdn-media-1.freecodecamp.org/images/lYhTPxs5niNKQy2zmNaprrN6SZkdzBFz-x1t)
_YAML > JSON_

Lorsque vous exécutez `eb init`, il créera un dossier `**.elasticbeanstalk**` dans votre répertoire racine. Vous n'avez pas vraiment besoin de toucher à quoi que ce soit ici, car il devrait être configuré automatiquement lorsque vous exécutez la commande pour la première fois.

Cependant, afin d'avoir vos variables d'environnement, et toute autre configuration que vous devez exécuter au moment du démarrage, créez un nouveau dossier : `**.ebextensions**`

La structure du dossier devrait ressembler à ceci :

```
- .ebextensions
-- 01_votreconfig.config
- .elasticbeanstalk
-- config.yml
```

Les fichiers de configuration sont écrits en YAML, comme mentionné précédemment. Pour vous donner une idée de ce à quoi ils devraient ressembler, voici quelques exemples :

Fichier des variables d'environnement :

```
# 01_envar.config
option_settings:
  aws:elasticbeanstalk:application:environment:
    PORT: 8081
    NODE_ENV: production
```

Un fichier pour configurer Node.js :  
Vous n'avez pas **vraiment** besoin de spécifier la `NodeVersion` car il vous donnera la dernière disponible sur les instances EC2. Mais c'est ici au cas où.

```
# 02_nodecommand.config
option_settings:
  aws:elasticbeanstalk:container:nodejs:
    NodeCommand: "npm run start"
    NodeVersion: 8.8.1
```

C'est le moyen le plus facile pour moi de gérer les paramètres de configuration, mais ils peuvent être ajustés dans le tableau de bord EB sous configuration.

Si vous voulez en savoir plus, [ici](https://medium.com/trisfera/getting-to-know-and-love-aws-elastic-beanstalk-configuration-files-ebextensions-9a4502a26e3c) se trouve un article amazing sur ce sujet.

#### Créer un environnement

```
eb create <nom-env>
```

**puis déployer**

```
eb deploy
```

En supposant que tout s'est bien passé, votre application est maintenant déployée dans le "cloud".

Vérifiez-la avec `eb open`

### Déployer des changements

Une fois que vous avez tout configuré, pousser des changements est super facile.

**NOTE :** Les changements doivent être validés dans Git avant de les pousser vers l'environnement.

Je ne m'en suis pas rendu compte la première fois, et cela m'a pris une éternité pour comprendre. Ne faites pas la même erreur — validez ces changements !

Donc, une fois que vous avez validé les changements, tapez simplement la commande ci-dessous et attendez qu'elle s'exécute.

```
eb deploy <nom-env>
```

### Autres commandes EBCLI pratiques

Pour ouvrir l'instance dans le terminal, ce qui est considérablement plus facile que d'essayer de se souvenir du dictionnaire d'une URL que AWS vous donne au début :

```
eb open
```

Pour ouvrir la console :

```
eb console
```

Pour obtenir les fichiers de log directement dans votre terminal :

```
eb logs
```

### Qu'est-ce qui suit ?

#### Nom de domaine personnalisé

Si vous exécutez `eb open`, vous remarquerez que l'URL est une URL très longue. Si vous le souhaitez, vous pouvez le connecter à votre domaine en utilisant Route 53. Pour la plupart, il s'agit de la gestion standard des enregistrements DNS. Vous pouvez laisser la gestion DNS là où vous avez enregistré votre domaine, mais je trouve simplement plus facile de tout avoir au même endroit.

#### Certificat SSL

Obtenir un certificat SSL pour votre instance est également assez facile. Visitez le gestionnaire de certificats et créez un nouveau certificat pour votre domaine. C'est un processus simple, aussi.

**Note :** Si vous prévoyez d'utiliser un certificat SSL pour Cloudfront, vous **devez** initier le processus depuis la zone N. Virginie. Vous pouvez changer votre zone en haut à droite de l'écran.

![Image](https://cdn-media-1.freecodecamp.org/images/T-YIuFvgWNeI0yf4pHkA0rqzKF7YAymSJ3MO)

Une fois qu'il est vérifié et prêt à être utilisé, ajoutez-le à votre configuration EB. Le moyen le plus facile est d'aller dans la console et de le sélectionner.

1. Allez dans votre tableau de bord EB
2. Choisissez votre application
3. Choisissez votre environnement
4. Cliquez sur "configuration" et choisissez le certificat SSL.

![Image](https://cdn-media-1.freecodecamp.org/images/4pnMX2NO3EITPMpimgMCAz32S1piyVuRwR5d)

**Une autre note :** Parfois, vous pourriez avoir des problèmes avec le gestionnaire de certificats si vous avez un compte tout nouveau. Si on vous dit de contacter le support client lorsque vous essayez de créer un certificat, faites-le et ils le corrigeront.

### Conclusion

Wow. Quelle aventure. Espérons que vous avez réussi et que vous n'avez pas eu à consulter les documents AWS trop souvent. Mais, si je suis honnête avec moi-même, je suis sûr que vous avez dû le faire au moins une fois. AWS est un service monstrueux et il ne fait que grandir de jour en jour.

![Image](https://cdn-media-1.freecodecamp.org/images/hjlbhz1DU8melTrm8Sm-QimQXggcqMVg6Hit)
_Maintenant, vous aussi, pouvez crier contre le Cloud_

### Support

Avez-vous apprécié cet article ? Souhaitez-vous en voir plus ? Avez-vous quelques dollars à dépenser ? Consultez le lien ci-dessous. Chaque tasse de café est transformée en quelques centaines de lignes de code supplémentaires :)

[**Offrez un café à Jared Nutt - BuyMeACoffee.com**](http://buymeacoff.ee/AXwyIxz1C)  
[_Développeur Web basé à Los Angeles qui fait de son mieux pour contribuer aux logiciels open source et écrire des tutoriels géniaux._buymeacoff.ee](http://buymeacoff.ee/AXwyIxz1C)

### Ressources

[AWS en anglais simple](https://www.expeditedssl.com/aws-in-plain-english)

[Découvrir et aimer les fichiers de configuration AWS Elastic Beanstalk (.ebextensions)](https://medium.com/trisfera/getting-to-know-and-love-aws-elastic-beanstalk-configuration-files-ebextensions-9a4502a26e3c)

[Commencer avec AWS](https://www.taniarascia.com/getting-started-with-aws-setting-up-a-virtual-server/)

[acloudguru](https://acloud.guru/) (Ce n'est pas un service gratuit, cependant ils ont un cours d'introduction qui est gratuit et très informatif)