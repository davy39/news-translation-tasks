---
title: Comment implémenter l'Infrastructure as Code avec AWS
subtitle: ''
author: Kayode Adeniyi
co_authors: []
series: null
date: '2022-10-31T17:07:04.000Z'
originalURL: https://freecodecamp.org/news/how-to-implement-infrastructure-as-code-with-aws
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/network-g381392bcb_1280.jpg
tags:
- name: AWS
  slug: aws
- name: Cloud Computing
  slug: cloud-computing
- name: Infrastructure as code
  slug: infrastructure-as-code
seo_title: Comment implémenter l'Infrastructure as Code avec AWS
seo_desc: "Infrastructure as code is the process of provisioning and managing your\
  \ cloud resources by writing a template file that is both human-readable and machine\
  \ consumable. \nFor AWS cloud development, the built-in choice for infrastructure\
  \ as code is AWS C..."
---

L'infrastructure as code est le processus de provisionnement et de gestion de vos ressources cloud en écrivant un fichier de modèle qui est à la fois lisible par l'homme et consommable par la machine. 

Pour le développement cloud AWS, le choix intégré pour l'infrastructure as code est AWS CloudFormation.

En utilisant l'IaC, les développeurs peuvent gérer l'infrastructure d'un projet de manière efficace, leur permettant de configurer et de maintenir facilement les changements au sein de l'architecture et des ressources d'un projet.

Il existe de nombreux outils IaC disponibles tels qu'Ansible, Puppet, Chef et Terraform. 

Mais pour ce guide, nous utiliserons CloudFormation, qui a été conçu spécifiquement pour les ressources AWS.

## Ce que vous apprendrez dans ce tutoriel

Après avoir suivi ce tutoriel, vous comprendrez comment maintenir vos ressources dans un seul fichier logiciel. 

En plus de cela, vous apprendrez les avantages liés à la vitesse que l'Infrastructure as Code apporte. Sans IaC, le temps et le coût du déploiement manuel de diverses infrastructures peuvent être beaucoup plus élevés par rapport à la maintenance de l'infrastructure en tant que logiciel. 

Dans cet article, nous allons considérer un exemple. Il démontrera le provisionnement manuel des ressources par rapport au déploiement d'un script CloudFormation pour créer une fonction Lambda serverless et une API REST sur AWS.

### Services que nous utiliserons dans ce tutoriel

Nous utiliserons les services suivants pour implémenter l'Infrastructure as Code dans AWS : 

<table style="border:none;border-collapse:collapse;table-layout:fixed;width:468pt"><colgroup><col><col></colgroup><tbody><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;background-color:#cfe2f3;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;text-align: center;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Nom du service AWS</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;background-color:#cfe2f3;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;text-align: center;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Description</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">AWS API Gateway (API GW)</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Nous utiliserons ce service pour créer notre API REST. Il permet également de créer, publier et surveiller des API Socket et Restful sécurisées.</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">AWS Lambda</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Nous utiliserons ce service pour configurer une fonction serverless d'exemple sur le backend qui sera intégrée avec notre API REST.</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Identity Access and Management (IAM)</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Service qui permet de gérer l'accès à divers services AWS via des rôles et des permissions. Nous créerons un rôle pour notre fonction Lambda afin que nous puissions accéder à l'API gateway.</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">AWS CLI</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Pour travailler avec les services et ressources AWS, vous pouvez utiliser l'interface de ligne de commande plutôt que la console pour un accès facile.</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">AWS SAM</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Une abstraction de CloudFormation permet de développer des applications serverless.</span></p></td></tr></tbody></table>

Pour ceux qui sont nouveaux sur AWS, il est bon d'avoir quelques connaissances à ce sujet pour comprendre l'article. Vous pouvez donc me suivre en créant un compte sur AWS [ici](https://aws.amazon.com/console/) et en vous assurant d'avoir installé [AWS CLI](https://aws.amazon.com/cli/) pour travailler avec l'exemple.

### Aperçu de l'exemple

Pour l'article, nous allons implémenter une API REST avec une API gateway. Elle sera intégrée avec une fonction backend Lambda serverless qui gère les requêtes POST et GET faites par notre API.

La première étape vous montrera comment construire et déployer manuellement ces ressources en utilisant la console AWS. La deuxième étape vous montrera comment automatiser le processus en utilisant CloudFormation.

## Comment déployer manuellement

Dans le déploiement manuel, nous travaillerons à l'intérieur de la console AWS. Il est un peu difficile de suivre les changements en travaillant en dehors de l'IDE local, surtout pour les projets à grande échelle. 

Dans la première étape, nous allons créer une fonction Lambda.

![Image](https://lh5.googleusercontent.com/dA4vn3WDgKdVRCf9dJyZjGG5CxtHGVrB-EuGs3EW9P0KkIGxMf64fWg-NXNhFGaVPios3ryNb4OpUfNCMEYvWE1rOtk1QfE_FjSF01E4DVUUlouuUY4KdzCt8J68_OnTz72x6PmousW5auYLYMZF_lYP69T-VljKBwD39ssmU2R-463xL7UQQCM9kg)

Si vous voulez que votre fonction Lambda fonctionne avec un autre service comme Comprehend, vous devez donner des permissions pour ce service. Assurez-vous donc de créer un rôle avec ces permissions.

Voici notre fonction Lambda qui retournera « Hello World » lorsqu'elle sera intégrée avec l'API gateway. 

```py
import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello World!')
    }
```

Maintenant que nous avons configuré notre fonction Lambda, l'étape suivante consiste à créer une API REST pour interagir avec la fonction Lambda. 

Pour cela, allez dans Amazon API Gateway, cliquez sur créer une API et sélectionnez REST API parmi les options fournies.

![Image](https://lh4.googleusercontent.com/DZDV8mRaosjWYOyeQgPpI2jI8U73bAYAJ-Y_FIEVZMYD_KjjSatXTNcUiv9rgpoBUg-tOL7Kc4-nXthNR8MsUcW8NtrbD7Sg6fx8VQHHG98DqBZDGvAC2alCjHunqu1W9OynLD83NcVu-kKE1jq4nu5byTcq6cLxjmeaAdI05l0MTfi37sxcIRcfSQ)

Maintenant, nous allons intégrer Lambda avec l'API. Pour cela, créez une méthode GET à partir du menu des actions et pointez notre API REST vers la fonction Lambda.

![Image](https://lh4.googleusercontent.com/H8Aw6L3o8xpkEPJQI2X0Hw7O2hAmyYuUKeEY2Q8SH0DOR7R_uCAJc94Z4lnJCsT-ZIYkrky3GWqroyrhSgUr2Hr8kiN8Ye3jOyTJdO_3WZSqTdC9shRDOju9oNIHx_ijkj2B3ig7xf83l2emLGVZei7Obj9twWhQifWMnR256HAFdUrc26fq52-70Q)

Nous sommes en mesure de déployer et de tester notre API pour son intégration correcte avec Lambda. Sélectionnez le nom de l'étape que vous souhaitez - pour cet exemple, j'utilise « prod ».

![Image](https://lh6.googleusercontent.com/YYKoUxe7L76Mcy6dJSK8rGo5b2KL3tru7D4pwGDqdREoHuPxNICkjGYvVT6KVDe_TrRDsfFj3wfu9TysVLDaJ9kb-fTyQoyc2DAYQ9y42Wtf1S4TGVAAmvdkQvgTVtxfwkU97_XRIAt4ge5HaDtnoroKS_uMPanS2GhC9Tk2mNhgyr1DAp5r9WG8tA)

Après avoir déployé l'API, vous pouvez voir une URL sur l'étape « prod ». En appelant cette URL, vous déclencherez la fonction Lambda. Comme nous avons retourné « Hello World » depuis notre fonction Lambda, vous devriez pouvoir voir le résultat souhaité.

![Image](https://lh6.googleusercontent.com/TY4GfBhk2V2RARNKYvD894FxeFKOZd4csJvj-aori2Ct524F1jOpx43CQpWEP-2irtjJTGIXgf6fhI4JZej_DgjEFM0UL0mzPoe7L2BQBHrMY5mv8mMbW6MbPKE-Qv7CC95VUPjqKeJ43L7iUea2qj4HMixEhm3p79Dma3cNxt4PanqJ49Hi6YJgrA)

## Comment déployer avec CloudFormation

Jusqu'à présent, nous avons vu comment fonctionne le déploiement manuel, ce qui prend généralement quelques minutes. 

Mais imaginons que nous avons plus d'une API, méthode, et plus d'un développeur travaillant dessus. Dans ce scénario, suivre toutes les ressources et les changements serait un défi. 

Donc, dans cette section, nous utiliserons AWS CloudFormation à la place. Cela donnera de la flexibilité aux développeurs, leur permettant d'ajuster leur infrastructure avec un simple script.

### Comment fonctionne CloudFormation ?

Nous utiliserons le fichier YAML pour provisionner et déclarer ces ressources et les déployer sur AWS pour créer une pile CloudFormation. CloudFormation est une pile qui contient toutes les ressources nécessaires pour le projet. 

Nous utiliserons le modèle SAM comme décrit ci-dessus dans la section des services. Il s'agit d'une abstraction de CloudFormation pour construire des applications serverless avec moins de code YAML. 

Pour ceux qui ne connaissent pas YAML, vous pouvez le considérer comme du JSON. Mais CloudFormation utilise ces deux formats de fichiers.

**Dans la première étape**, nous nous dirigeons vers notre IDE local et écrivons la même fonction Lambda que nous avons faite dans la console AWS.

**helloworld.py** :

```py
import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello World!')
    }
```

Ensuite, nous allons créer un fichier **template**.yaml contenant notre infrastructure. Nous allons définir notre fonction Lambda et API Gateway dans ce fichier. 

Pour construire ce fichier, nous devons ajouter quelques informations qui sont communes à tous les modèles SAM.

**template.yaml** :

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Description: Premier modèle CloudFormation
```

Maintenant, nous devons ajouter « Globals » à ce fichier template.yaml de CloudFormation. **Globals** sont les configurations communes pour les ressources que vous allez déployer. Globals vous permettent de déclarer des informations globalement pour un type de ressource spécifique plutôt que de le spécifier à nouveau pour différentes ressources.

**template.yaml** :

```yaml
Globals:
    #Commun à toutes les fonctions Lambda que vous créez
    Function:
      MemorySize: 128
      Runtime: python3.6
      Timeout: 5
```

Nous devons définir la balise Resources dans notre fichier template.yaml. La fonction Lambda et l'API REST viendront sous cette balise. 

**template.yaml** :

```yaml
Resources:

    ##Lambda et API GW intégrés
    helloworld:
        Type: AWS::Serverless::Function
        Properties:
          #filename.functionname
          Handler: helloworld.lambda_handler

          #REST API créée
          Events:
            PostAdd:
              Type: Api
              Properties:
                Path: /helloworld
                Method: get
```

Dans le code ci-dessus, nous définissons des paramètres pour créer la fonction Lambda. Pour l'événement, nous créons une API REST qui déclenche la fonction Lambda. 

**Note :** Il existe un tableau de paramètres comme CodeURI et description que vous pouvez spécifier pour votre fonction serverless. La meilleure façon de créer un fichier de modèle est de consulter la documentation CloudFormation et de voir les paramètres disponibles pour votre ressource/service spécifié.

## Comment déployer le fichier de modèle

Nous pouvons déployer notre fichier **template**.yaml en utilisant les deux commandes AWS CLI suivantes :

```yaml
##s3 bucket stocke notre modèle sam que nous devons déployer
aws cloudformation package --template-file template.yaml --output-template-file sam-template.yaml --s3-bucket helloworld-sam
```

Après avoir exécuté la commande ci-dessus, vous pourrez voir un fichier de modèle SAM. Nous utiliserons ce fichier dans la deuxième commande ci-dessous. 

Dans cette commande, donnez votre chemin approprié vers le fichier sam-template.yaml :

```yaml
#Déployer la pile
#pointez vers le fichier de modèle créé par une commande précédente et un nom de pile ainsi que votre région où vous déployez

aws cloudformation deploy --template-file /chemin vers le fichier sam-template.yaml --stack-name test-stack --capabilities CAPABILITY_IAM --region us-east-1
```

Après avoir exécuté ces deux commandes, vous verrez la pile créée dans le CLI. Vous pouvez la vérifier en utilisant CloudFormation dans la console. 

Ici, vous verrez toutes les ressources provisionnées via le code créé et déployé en utilisant le fichier template.yaml. 

![Image](https://lh5.googleusercontent.com/h9wcmfT3Kx-jSIMEeCqZv-0qFTs05puZ6ox5CuRBywubpqdiPRpnYiCZZTaYFBaSDEuQmi5HtXCPNPpZcuKCs_jtBTc6WZP5pUceHxR-jRWmRLycxFwESMYkdYpN5Qi5c3_TACNRjpqfwpRdDf5qV6Wee5-uAMhtvVoAWUtJvIA4h4no_fk-NPT7Sw)

Vous pouvez cliquer sur API et accéder à l'URL pour vérifier la sortie comme nous l'avons fait pour le déploiement manuel. 

## Conclusion

C'est tout - vous avez implémenté avec succès l'infrastructure as code dans AWS en utilisant CloudFormation.

J'espère que cet article a été utile pour quiconque souhaitant comprendre l'implémentation de l'infrastructure as code dans AWS.

Connectez-vous avec moi sur [LinkedIn](https://www.linkedin.com/in/kadeniyi/) et [Twitter](https://twitter.com/mkbadeniyi)

Hasta la vista!