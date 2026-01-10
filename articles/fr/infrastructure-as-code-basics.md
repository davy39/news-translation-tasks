---
title: Qu'est-ce que l'Infrastructure as Code ? Expliqué pour les débutants
subtitle: ''
author: Daniel Adetunji
co_authors: []
series: null
date: '2023-06-15T14:32:46.000Z'
originalURL: https://freecodecamp.org/news/infrastructure-as-code-basics
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/cover-5.png
tags:
- name: Infrastructure as code
  slug: infrastructure-as-code
- name: Terraform
  slug: terraform
seo_title: Qu'est-ce que l'Infrastructure as Code ? Expliqué pour les débutants
seo_desc: Infrastructure as Code (IaC) is a way of managing your infrastructure like
  it was code. This gives you all the benefits of using code to create your infrastructure,
  like version control, faster and safer infrastructure deployments across different
  en...
---

L'Infrastructure as Code (IaC) est une méthode de gestion de votre infrastructure comme si c'était du code. Cela vous offre tous les avantages de l'utilisation de code pour créer votre infrastructure, comme le contrôle de version, des déploiements d'infrastructure plus rapides et plus sûrs dans différents environnements, et une documentation à jour de votre infrastructure.

L'article expliquera comment fonctionne l'infrastructure as code en utilisant une analogie. Nous aborderons les différents outils d'infrastructure as code disponibles ainsi que le code déclaratif vs impératif.

Je vous présenterai également Terraform, qui est un outil open source d'infrastructure as code que vous pouvez utiliser pour créer une infrastructure sur plusieurs fournisseurs de cloud comme AWS, GCP, Azure et autres.

## Infrastructure as Code en pratique

Imaginez que vous essayez de créer une application web à trois niveaux sur AWS comme vous pouvez le voir dans l'image ci-dessous :

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6f739c67-e79c-4995-b58d-71d695cccd47_1018x1682.png align="left")

*Exemple d'application web à trois niveaux*

Le niveau de présentation est responsable de la présentation de l'interface utilisateur à l'utilisateur. Il comprend les composants de l'interface utilisateur tels que HTML, CSS et JavaScript s'exécutant sur des instances EC2.

Le niveau logique est responsable du traitement des requêtes utilisateur et de la génération de réponses, en communiquant avec la couche de base de données pour récupérer ou stocker des données. Cela est également déployé sur des instances EC2.

Le niveau de base de données est responsable du stockage et de la gestion des données de l'application et permet l'accès à ses données via le niveau logique. La base de données s'exécute sur AWS RDS.

Chacune des instances se trouve dans un groupe de [mise à l'échelle automatique](https://lightcloud.substack.com/i/102200211/auto-scaling-explained) avec un [équilibreur de charge](https://lightcloud.substack.com/i/102200211/load-balancing-explained) devant (sauf pour le niveau de base de données).

Si vous souhaitez créer cette infrastructure via la console AWS, vous devrez cliquer manuellement à travers divers écrans pour lancer l'infrastructure. Cela est acceptable si c'est une activité ponctuelle.

Mais si vous devez répéter cela dans différents environnements comme le développement et les tests, ou si vous devez ajouter une infrastructure supplémentaire comme des caches, des files d'attente, des règles de pare-feu, [IAM](https://lightcloud.substack.com/p/aws-iam-identity-and-access-management) ou des certificats SSL, alors il devient de plus en plus complexe de gérer cela via la console AWS.

La gestion d'une infrastructure complexe via la console introduit également la possibilité d'erreurs humaines.

L'infrastructure as code exprime votre infrastructure souhaitée dans le langage du code. Cela apporte tous les avantages du code à la gestion de votre infrastructure comme :

1. Contrôle de version – permet de stocker l'historique de votre infrastructure et de revenir à une version précédente si nécessaire.

2. Déploiements plus rapides et plus sûrs – peut recréer une infrastructure dans de nouveaux environnements rapidement et avec moins d'erreurs puisque chaque partie de l'infrastructure est clairement définie dans le code.

3. Documentation – l'état actuel de votre infrastructure est documenté et maintenu à jour automatiquement chaque fois que vous apportez une modification. Cela maintient votre documentation d'infrastructure détaillée et précise, par rapport à une infrastructure écrite dans un document ou sur une page Confluence qui peut ne pas être mise à jour chaque fois qu'il y a un changement.

## Comment fonctionne l'Infrastructure as Code – Expliqué avec une analogie

L'infrastructure as code vous permet de créer un plan détaillé de votre infrastructure. Ce plan donne des instructions à votre fournisseur de cloud sur l'infrastructure que vous souhaitez créer.

Cela est similaire à la manière dont un plan architectural fonctionne. Il décrit la disposition, les dimensions, les matériaux et les divers composants de la structure. Le plan sert de référence pour les architectes et les ingénieurs afin de comprendre la construction souhaitée.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4d1aacbf-34c7-43ae-8384-2f912072cc00_2728x1514.png align="left")

*comment un plan architectural est analogue à l'infrastructure as code*

Le plan laisse peu de place à l'erreur. Il sera interprété de la même manière par tout architecte ou ingénieur. Si vous vouliez construire des copies exactes de cette maison, tout ce dont vous avez besoin est le plan architectural.

L'infrastructure as code, à un niveau de base, fonctionne de la même manière qu'un plan architectural. Il détaille l'infrastructure que vous souhaitez créer en tant que code dans un certain nombre de langages possibles (JSON, YAML, HCL, Python, Ruby, JavaScript, etc.), instruisant le fournisseur de cloud de créer votre infrastructure exactement comme spécifié.

## Outils d'Infrastructure as Code Déclaratif et Impératif

Il existe de nombreuses options IaC parmi lesquelles choisir, et tous les principaux fournisseurs de cloud ont leurs propres outils dédiés :

* AWS a CloudFormation

* GCP a Deployment Manager

* Azure a Resource Manager

Une limitation de ces outils spécifiques aux fournisseurs de cloud est qu'ils ne peuvent créer une infrastructure que dans leurs clouds respectifs. Ainsi, CloudFormation ne fonctionne que dans AWS et Deployment Manager ne fonctionne que dans GCP. L'IaC utilisant ces fournisseurs est généralement écrit au format JSON ou YAML.

Terraform, en revanche, est open source et vous pouvez l'utiliser pour créer une infrastructure sur tous les principaux fournisseurs de cloud. Il utilise HCL (HashiCorp Configuration Language).

L'infrastructure as code peut également être écrite en utilisant des langages populaires comme Python et JavaScript.

Ces langages de script/programmation se situent sur un spectre de code déclaratif et impératif comme montré ci-dessous.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdaba03dc-13eb-4f45-873f-6f00dd648ffb_2508x870.png align="left")

*Un spectre de langages déclaratifs et impératifs et où se situe Terraform HCL*

La principale différence entre un langage impératif et déclaratif est que les langages impératifs définissent explicitement le *flux de contrôle*. Cela est simplement l'ordre dans lequel les instructions sont exécutées dans un programme. Le flux de contrôle détermine le chemin que le programme prend et comment il répond à différentes conditions ou événements.

Dans les langages impératifs, le flux de contrôle est explicitement défini en utilisant des structures de contrôle telles que les boucles, les conditionnelles et les appels de fonction. Les langages impératifs vous donnent plus de flexibilité dans la configuration de votre infrastructure. Ce n'est pas nécessairement un point positif, car plus de flexibilité signifie plus d'opportunités d'introduire des erreurs dans votre infrastructure.

Un langage déclaratif se concentre sur la description du résultat souhaité sans donner d'instructions spécifiques sur la manière de l'atteindre.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5fe4d2ce-6449-4597-beca-5a46f2aa6ee8_2620x1468.png align="left")

*Une illustration démontrant la différence entre les langages déclaratifs et impératifs*

Un exemple JSON est montré ci-dessous, utilisé dans AWS CloudFormation pour créer une instance EC2 :

```python
"Type": "AWS::EC2::Instance",
      "Properties": {
        "ImageId": "ami-0123456789",
        "InstanceType": "t2.micro",
        "KeyName": "my-key-pair",
        "SecurityGroupIds": ["sg-0123456789"],
        "SubnetId": "subnet-0123456789",
        "Tags": [
          {
            "Key": "Name",
            "Value": "MyEC2Instance"
          }
        ]
      }
```

Un langage déclaratif comme JSON [abstrait](https://lightcloud.substack.com/p/cloud-computing-abstractions-explained) la complexité sous-jacente qui détaille comment l'instance EC2 sera créée. Tout ce qui l'intéresse, c'est l'état final.

Terraform HCL est plus proche de l'extrémité déclarative du spectre. Terraform vous permet de décrire l'état final de l'infrastructure souhaitée sans spécifier les étapes exactes pour y parvenir. Terraform gère en interne l'ordre d'exécution, les dépendances des ressources et traite les changements d'infrastructure en fonction de la configuration souhaitée.

Mais Terraform prend en charge certaines fonctionnalités impératives comme les variables et les expressions, permettant un comportement dynamique basé sur les entrées. Ainsi, ce n'est pas un langage complètement déclaratif comme JSON.

## Comment fonctionne Terraform

Il y a deux concepts fondamentaux qui servent de fondation pour comprendre Terraform :

1. Le fichier de configuration – cela décrit l'infrastructure souhaitée

2. Le fichier d'état – cela décrit l'infrastructure actuelle telle qu'elle existe dans le monde réel

Le travail de Terraform est de créer, modifier ou supprimer l'infrastructure selon les besoins afin que la configuration d'infrastructure souhaitée soit respectée. Il le fait en exécutant les appels d'API nécessaires à votre ou vos fournisseurs de cloud pour créer, modifier ou détruire les ressources comme spécifié.

Une fois que l'infrastructure a été créée/modifiée/détruite pour correspondre au fichier de configuration, le fichier d'état est mis à jour pour refléter l'infrastructure actuelle.

La commande `terraform plan` crée un [plan d'exécution](https://developer.hashicorp.com/terraform/cli/commands/plan), qui vous permet de prévisualiser les changements que Terraform prévoit d'apporter à votre infrastructure.

Par défaut, lorsque Terraform crée un plan, il compare la configuration souhaitée telle que décrite dans le fichier de configuration, avec la configuration actuelle telle que décrite dans le fichier d'état. Terraform propose ensuite une liste de changements nécessaires pour garantir que la configuration actuelle correspond à la configuration souhaitée.

Si vous exécutez ensuite la commande `terraform apply`, Terraform modifiera l'infrastructure réelle pour qu'elle corresponde à la configuration souhaitée, et mettra à jour le fichier d'état pour montrer la nouvelle configuration de l'infrastructure.

À un niveau élevé, voici ce que fait Terraform :

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fba9f88a0-e8bb-4507-9fd9-a9576bb8fefe_2650x1380.png align="left")

*Ce qui se passe lorsque vous exécutez la commande* `terraform apply`

Revenons à l'analogie du plan architectural.

Le fichier de configuration est comme le plan architectural. Il détaille l'infrastructure qui doit être construite, c'est-à-dire la construction souhaitée. L'infrastructure du monde réel est la construction existante dans le monde physique et le fichier d'état est une représentation de ce qui existe actuellement – le plan actuel. Les ingénieurs travaillent pour s'assurer que la construction existante correspond au plan architectural.

Dans cette analogie, les ingénieurs font le travail de Terraform en s'assurant que la construction existante correspond au plan architectural. Vous n'avez pas besoin de spécifier les détails de la construction de la maison, vous devez simplement spécifier ce que vous voulez construire et les ingénieurs s'occupent du reste.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F973320df-191b-46b6-be0a-18cd43305288_2620x1468.png align="left")

*Une analogie architecturale à l'exécution de* `terraform apply`

Si vous souhaitez en savoir plus sur le fonctionnement de Terraform et comment vous pouvez l'utiliser dans vos projets, vous pouvez [consulter ce cours gratuit](https://www.freecodecamp.org/news/learn-terraform-and-aws-by-building-a-dev-environment/) sur la chaîne YouTube de freeCodeCamp.

## Mettre tout ensemble

L'infrastructure as code (IaC) est un excellent moyen de gérer la configuration complexe de l'infrastructure sous forme de code. Cela apporte naturellement tous les avantages du code à votre infrastructure comme le contrôle de version, des déploiements d'infrastructure plus rapides et plus sûrs dans différents environnements et une documentation à jour de votre infrastructure.

Terraform est un outil IaC open source qui vous permet de travailler avec plusieurs fournisseurs de cloud pour lancer une infrastructure comme défini dans vos fichiers de configuration.

Terraform HCL est un langage déclaratif qui vous permet de décrire votre configuration d'infrastructure souhaitée. Tout ce que vous avez à faire est de spécifier ce que vous voulez créer et Terraform gère la création en votre nom en effectuant des appels d'API à votre ou vos fournisseurs de cloud choisis.