---
title: 'AWS CloudFormation : Où trouver de l''aide quand vous en avez besoin'
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2020-05-18T13:00:00.000Z'
originalURL: https://freecodecamp.org/news/aws-cloudformation-where-to-find-help
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/automation.jpg
tags:
- name: AWS
  slug: aws
- name: aws cli
  slug: aws-cli
- name: cloudformation
  slug: cloudformation
seo_title: 'AWS CloudFormation : Où trouver de l''aide quand vous en avez besoin'
seo_desc: "Staring at a plain, dumb command line prompt with no clue what to do with\
  \ the AWS CLI next can be a humbling experience. And, in my experience at least,\
  \ staring at the Management Console for AWS CloudFormation can be worse. \nSo let\
  \ me offer you some ..."
---

Rester face à une simple invite de commande sans savoir quoi faire ensuite avec l'AWS CLI peut être une expérience humiliante. Et, selon mon expérience, regarder la Console de Gestion pour AWS CloudFormation peut être pire. 

Alors, laissez-moi vous offrir une aide rapide pour "bien démarrer" basée sur une partie du contenu de [mon dernier cours Pluralsight](https://pluralsight.pxf.io/EMPE2). 

Tout d'abord, si vous prévoyez de gérer vos piles CloudFormation via l'AWS CLI plutôt que la Console de Gestion, je discute des bases dans [cet article](https://www.freecodecamp.org/news/aws-cli-tutorial-install-configure-understand-resource-environment/). Une fois que tout cela est réglé, vous serez prêt pour tout. 

Commencez simplement : 

```
$ aws s3 ls
2019-11-03 13:16:59 athena5905
2019-02-03 18:01:42 book-3939
2014-07-01 18:52:32 elasticbeanstalk-ap-northeast-1-426397493112
2014-08-28 16:57:49 elasticbeanstalk-us-east-1-426497493912
2019-05-04 22:17:50 ltest236
2018-07-15 15:52:30 mybucket99688223
2017-07-25 17:06:43 nextcloud3239027
```

"aws" dans cet exemple indique à votre shell que vous souhaitez que ce qui suit soit géré par l'AWS CLI. Le "s3" que je tape ensuite indique à la CLI que j'utiliserai le service S3 - c'est le service de stockage simple d'Amazon. Enfin, "ls" ou "list" est la commande que je souhaite exécuter contre ce service. 

La CLI, utilisant les variables d'authentification de compte que l'outil de configuration a ajoutées à mon environnement, va maintenant accéder à mon compte, dans ce cas, en récupérant les noms de tous mes buckets.

De manière prévisible, vous indiquez à AWS que vous souhaitez travailler avec CloudFormation en utilisant "cloudformation". Si je lance simplement cela sans spécifier de commande, j'obtiendrai un message d'erreur :

```
aws cloudformation
usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help
aws: error: the following arguments are required: operation

```

Mais c'est un message important, car il nous indique comment accéder à la documentation intégrée. Une aide contextuelle est disponible à chaque niveau. 

Voyez ce qui se passe si vous ajoutez "help" après "cloudformation". Vous obtiendrez une brève description suivie d'une liste de toutes les sous-commandes disponibles. 

```
$ aws cloudformation help

CLOUDFORMATION()                                              CLOUDFORMATION()
NAME
       cloudformation -
DESCRIPTION
AWS  CloudFormation  vous permet de créer et de gérer des déploiements d'infrastructure AWS de manière prévisible et répétée. Vous pouvez utiliser AWS  CloudFormation pour  exploiter des produits AWS, tels qu'Amazon Elastic Compute Cloud, Amazon Elastic Block Store, Amazon Simple Notification Service,  Elastic  Load Balancing,  et Auto Scaling pour construire des applications hautement fiables, hautement évolutives et rentables sans créer ni configurer l'  infrastructure AWS sous-jacente.
Avec  AWS  CloudFormation, vous déclarez toutes vos ressources et dépendances dans un fichier de modèle.  Le  modèle  définit  une  collection  de ressources  en tant qu'  unité unique appelée une pile. AWS CloudFormation crée et supprime toutes les ressources membres de la pile ensemble et gère  toutes les dépendances entre les ressources pour vous.
Pour  plus d'informations sur AWS CloudFormation, voir la page du produit AWS CloudFormation.
Amazon CloudFormation utilise d'autres  produits AWS.  Si  vous  avez besoin d'informations techniques supplémentaires sur un produit AWS spécifique, vous pouvez trouver la documentation technique du produit sur docs.aws.amazon.com.

COMMANDES DISPONIBLES
       o cancel-update-stack
       o continue-update-rollback
       o create-change-set
       o create-stack
       o create-stack-set
       o delete-change-set
       o delete-stack
       o delete-stack-instances
       o delete-stack-set
       o deploy
       o describe-account-limits
       o describe-change-set
       o describe-stack-events
       o describe-stack-instance
       o describe-stack-resource
       o describe-stack-resources
       o describe-stack-set
       o describe-stack-set-operation
       o describe-stacks
       o estimate-template-cost
       o execute-change-set
       o get-stack-policy
[...]
```

Maintenant, exécutez la commande "describe-stacks". Il n'y a probablement aucune pile active dans votre compte pour le moment, donc vous ne verrez aucune sortie. 

Mais faites cela à nouveau, cette fois en ajoutant "help". Cela vous montrera quelques options qui vous permettront de filtrer ou de manipuler les données que vous obtenez en retour. Vous pourriez, par exemple, pointer la CLI vers une pile spécifique en utilisant "--stack-name" suivi du nom d'une pile existante.

```
$ aws cloudformation describe-stacks
$ aws cloudformation describe-stacks help
NAME
       describe-stacks -
DESCRIPTION
       Retourne  la  description pour la pile spécifiée ; si aucun nom de pile n'a été spécifié, alors il retourne la description pour toutes les piles créées.
       NOTE:
          Si la pile n'existe pas,  une  AmazonCloudFormationException  est retournée.
       Voir aussi : Documentation de l'API AWS
       Voir 'aws help' pour les descriptions des paramètres globaux.
       describe-stacks  est  une  opération paginée. Plusieurs appels API peuvent être émis afin de récupérer l'ensemble complet des résultats.  Vous  pouvez désactiver la pagination en fournissant l'argument --no-paginate.  Lorsque vous utilisez --output text et l'argument --query sur  une  réponse paginée,  l'argument  --query  doit  extraire les données des résultats des expressions de requête suivantes : Stacks

SYNOPSIS
            describe-stacks
          [--stack-name <value>]
          [--cli-input-json <value>]
          [--starting-token <value>]
          [--max-items <value>]
          [--generate-cli-skeleton <value>]

OPTIONS
       --stack-name (string)
          Le nom ou l'ID de pile unique qui est associé à  la  pile,
          qui ne sont pas toujours interchangeables :
[...]

$ aws cloudformation describe-stacks --stack-name myname

```

Ce sont des outils qui vous aideront, peu importe quel service AWS vous utilisez. Mais en regardant spécifiquement CloudFormation, il y a quelques collections officielles de modèles d'exemples précieuses que vous devriez connaître. La syntaxe JSON ou YAML étant ce qu'elle est, vous ne voudrez probablement pas commencer à partir d'un document vide. 

Amazon lui-même a fait un excellent travail en créant des modèles pour que nous puissions travailler avec. Votre premier arrêt devrait être la [page des modèles AWS CloudFormation](https://aws.amazon.com/cloudformation/resources/templates/). Ici, vous trouverez des liens vers des extraits et des frameworks d'applications spécifiques, ainsi que du contenu plus innovant. 

Mais pour l'instant, j'aimerais attirer votre attention sur l'un des "modèles d'exemples" organisés par service AWS (ce code provient de l'un des [exemples Amazon EC2](https://s3.us-west-2.amazonaws.com/cloudformation-templates-us-west-2/EC2InstanceWithSecurityGroupSample.template)). 

Le modèle commence par une description libre qui nous indique utilement quel type de pile cela générera. On nous dit également que nous pourrions personnaliser le modèle en utilisant une adresse IP élastique existante au lieu d'une générée automatiquement. 

```
{
  "AWSTemplateFormatVersion" : "2010-09-09",

  "Description" : "Modèle AWS CloudFormation EC2InstanceWithSecurityGroupSample : Crée une instance Amazon EC2 exécutant l'AMI Amazon Linux. L'AMI est choisi en fonction de la région dans laquelle la pile est exécutée. Cet exemple crée un groupe de sécurité EC2 pour l'instance afin de vous donner un accès SSH. **ATTENTION** Ce modèle crée une instance Amazon EC2. Vous serez facturé pour les ressources AWS utilisées si vous créez une pile à partir de ce modèle.",

```

Vous devrez passer le nom d'une KeyPair existante de la région actuelle dans votre compte AWS afin de pouvoir ouvrir un accès SSH distant à l'instance Linux qui sera lancée. Vous pouvez également passer cette valeur depuis la ligne de commande.

La section Paramètres est également l'endroit où vous définissez le type d'instance EC2. Le type par défaut est t2.small, mais nous serions autorisés à remplacer cette valeur par l'une des autres valeurs autorisées dans ce document, ou à la remplacer depuis la ligne de commande. 

```
  "Parameters" : {
    "KeyName": {
      "Description" : "Nom d'une KeyPair EC2 existante pour activer l'accès SSH à l'instance",
      "Type": "AWS::EC2::KeyPair::KeyName",
      "ConstraintDescription" : "doit être le nom d'une KeyPair EC2 existante."
    },

    "InstanceType" : {
      "Description" : "Type d'instance EC2 du serveur Web",
      "Type" : "String",
      "Default" : "t2.small",

```

Si vous faites défiler la section Mappings, nous pouvons voir de longues listes d'architectures matérielles disponibles et d'identifiants d'images de machines Amazon pour chaque région. 

Il s'agit d'une section facultative où vous pouvez insérer vos propres valeurs non standard, par exemple, un type d'image serait lancé en fonction d'un ensemble particulier de paramètres - peut-être même une image AMI privée. Ces données sont organisées en paires clé/valeur. 

```
  "Mappings" : {
    "AWSInstanceType2Arch" : {
      "t1.micro"    : { "Arch" : "HVM64"  },
      "t2.nano"     : { "Arch" : "HVM64"  },
      "t2.micro"    : { "Arch" : "HVM64"  },

```

La section Ressources dans ce cas définit votre environnement d'instance. Le SecurityGroup, par exemple, est configuré pour ouvrir le port SSH 22 mais rien d'autre. L'adresse IP publique de l'instance est également associée à la nouvelle adresse IP élastique qui sera allouée. 

```
    "InstanceSecurityGroup" : {
      "Type" : "AWS::EC2::SecurityGroup",
      "Properties" : {
        "GroupDescription" : "Activer l'accès SSH via le port 22",
        "SecurityGroupIngress" : [ {
          "IpProtocol" : "tcp",
          "FromPort" : "22",
          "ToPort" : "22",
          "CidrIp" : { "Ref" : "SSHLocation"}
        } ]
      }
    }
  },

```

Une autre ressource importante d'Amazon : [Quick Starts](https://aws.amazon.com/quickstart/?quickstart-all.sort-by=item.additionalFields.updateDate&quickstart-all.sort-order=desc). Strictement parlant, les piles d'infrastructure pré-construites fournies ici pour vous aider à créer des déploiements cloud plus complexes ne sont pas directement liées à CloudFormation. Elles ont été fournies par des entreprises tierces pour simplifier le processus de construction de leur infrastructure au sein de la plateforme AWS. 

Mais le fait est que chacune commence par son propre modèle CloudFormation unique. En cliquant pour voir des exemples concrets, vous serez souvent dirigé vers les modèles de code source des piles dans un dépôt GitHub. [Cet exemple](https://github.com/aws-quickstart/quickstart-hashicorp-consul) nous montre les outils dont vous auriez besoin pour lancer une Console HashiCorp :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-from-2020-05-17-13-06-37.png)

Dans tous les cas, n'hésitez pas à utiliser ces modèles comme outils d'apprentissage - ou à parcourir la sélection pour voir s'il y a une pile qui correspond à vos besoins.

_Il y a beaucoup plus de bonnes pratiques d'administration sous forme de livres, de cours et d'articles disponibles sur mon site [bootstrap-it.com](https://bootstrap-it.com/)._