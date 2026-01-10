---
title: Comment choisir le bon outil IaC – Comparaison d'AWS CDK, CloudFormation et
  Terraform
subtitle: ''
author: Ifeanyi Otuonye
co_authors: []
series: null
date: '2024-06-03T21:27:31.000Z'
originalURL: https://freecodecamp.org/news/comparing-iac-tools-aws-cdk-cloudformation-terraform
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/Level-Up-Tech-Design-Portfolio.jpg
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: Infrastructure as code
  slug: infrastructure-as-code
seo_title: Comment choisir le bon outil IaC – Comparaison d'AWS CDK, CloudFormation
  et Terraform
seo_desc: "Infrastructure as Code (IaC) has become a cornerstone of modern cloud resource\
  \ management. It enables developers and engineers to manage their cloud resources\
  \ with the same level of control and precision as application code. \nWhen you're\
  \ working with..."
---

L'Infrastructure as Code (IaC) est devenue une pierre angulaire de la gestion moderne des ressources cloud. Elle permet aux développeurs et aux ingénieurs de gérer leurs ressources cloud avec le même niveau de contrôle et de précision que le code applicatif. 

Lorsque vous travaillez avec AWS, parmi les outils à l'avant-garde de l'utilisation de l'IaC, on trouve AWS CloudFormation, AWS Cloud Development Kit (CDK) et Terraform de HashiCorp. 

Chacun de ces outils IaC offre des fonctionnalités et des approches uniques pour la gestion de l'infrastructure. Cela les rend adaptés à différents scénarios et préférences, et ils peuvent vous aider à automatiser et à standardiser vos déploiements de ressources cloud ou ceux de votre équipe.

Cet article fournira une comparaison de haut niveau de ces trois outils, en se concentrant sur leurs capacités, leurs niveaux d'abstraction et leurs cas d'utilisation pratiques. Vous explorerez comment ces outils vous permettent de créer et de gérer programmatiquement des infrastructures cloud complexes. 

Plus précisément, l'accent sera mis sur le déploiement d'une infrastructure réseau d'architecture à trois niveaux. Cela inclura le déploiement d'un Virtual Private Cloud (VPC) configuré avec plusieurs sous-réseaux, des tables de routage, une passerelle Internet et des passerelles NAT pour mettre en avant les capacités et la syntaxe uniques de chaque outil IaC.

À la fin de cet article, vous aurez une compréhension approfondie des fonctionnalités de ces outils afin de pouvoir prendre une décision éclairée lors de la sélection de l'un d'eux pour construire des infrastructures cloud résilientes, évolutives et gérées efficacement.

Sans plus tarder, commençons !

## Ce que nous allons couvrir :

1. [Qu'est-ce que l'Infrastructure as Code (IaC) ?](#heading-questce-que-linfrastructure-as-code-iac)
2. [Prérequis](#heading-prerequis)
3. [Scénario d'utilisation](#heading-scenario-dutilisation)
4. [Exemples de code d'outils IaC](#heading-exemples-de-code-doutils-iac)
5. [Analyse et comparaison](#heading-analyse-et-comparaison)
6. [Pourquoi choisir l'un plutôt que l'autre ?](#heading-pourquoi-choisir-lun-plutot-que-lautre)

## Qu'est-ce que l'Infrastructure as Code (IaC) ?

L'Infrastructure as Code est un principe clé du DevOps qui consiste à gérer et à provisionner les ressources d'infrastructure en les définissant comme du code dans des fichiers de configuration, au lieu d'utiliser des processus et des paramètres manuels.

Si vous souhaitez en savoir plus sur les bases de l'IaC, [voici un guide utile pour vous aider à démarrer](https://www.freecodecamp.org/news/infrastructure-as-code-basics/).

Maintenant, apprenons un peu plus sur les trois outils que nous allons comparer dans cet aperçu.

### Que fait AWS CloudFormation ?

AWS CloudFormation utilise YAML ou JSON pour décrire et provisionner automatiquement et en toute sécurité les ressources d'infrastructure nécessaires pour vos applications – dans toutes les régions et tous les comptes de votre environnement cloud AWS.

### Que fait AWS Cloud Development Kit (CDK) ?

AWS Cloud Development Kit est un framework de développement logiciel spécifiquement utilisé pour définir l'infrastructure cloud en code. Il provisionne finalement les ressources via AWS CloudFormation. 

AWS CDK utilise des langages de programmation familiers comme TypeScript, JavaScript, Python, Java et d'autres pour définir des composants cloud réutilisables connus sous le nom de constructs. Ceux-ci sont ensuite partagés et utilisés pour créer des architectures cloud complexes et évolutives.

#### Qu'est-ce qu'un construct ?

Dans le contexte d'AWS CDK, un construct représente un composant cloud qui encapsule certaines fonctionnalités et configurations sous une forme réutilisable.

### Que fait Terraform ?

Terraform est un outil multi-locataire créé par HashiCorp qui vous permet de définir à la fois des composants de bas niveau et de haut niveau de votre infrastructure cloud en utilisant un langage de configuration déclaratif. 

Il est agnostique du cloud et est capable de gérer des configurations multi-fournisseurs dans une seule configuration.

#### Que signifie cloud-agnostic ?

Cloud-agnostic fait référence à la capacité d'un outil ou d'un service à fonctionner sur différents fournisseurs de cloud sans modifications significatives de ses procédures opérationnelles ou de son architecture.

Très bien, maintenant que vous comprenez les outils que nous allons discuter, plongeons-nous dans le sujet.

## Prérequis

* Compte AWS avec un utilisateur IAM disposant de permissions admin
* Connaissance et utilisation de base d'AWS CloudFormation, AWS CDK et Terraform
* Compréhension de base de YAML, Python et du langage de configuration HashiCorp
* Expérience avec un environnement de développement interactif (IDE)

## Scénario d'utilisation

Vous êtes un ingénieur réseau cloud chez REXTECH Corp, une startup sur le point de lancer un nouveau service en ligne offrant du streaming de contenu numérique. Comme le service devrait attirer une base d'utilisateurs substantielle dès le départ, vous devez déployer une infrastructure cloud hautement évolutive, fiable et sécurisée capable de gérer le trafic de pointe et de fournir une disponibilité continue.

Votre manager a mandaté une solution de réseau cloud qui non seulement répond à ces exigences de performance, mais permet également un scaling rapide et une gestion efficace. 

En réponse à cela, vous êtes chargé d'automatiser le déploiement d'une infrastructure réseau d'architecture à trois niveaux. Elle doit comporter un Virtual Private Cloud (VPC) incluant plusieurs sous-réseaux dans plusieurs zones de disponibilité (AZ), des passerelles NAT et des tables de routage pour assurer la résilience et une configuration optimale.

Avec le besoin d'agilité et de maintenabilité de votre infrastructure, vous décidez d'évaluer et de choisir entre AWS CloudFormation, AWS CDK et Terraform pour ce projet. 

Avant d'évaluer l'application de chaque outil au scénario, décomposons les composants des ressources de déploiement.

Ce déploiement implique la configuration d'un VPC avec deux sous-réseaux publics pour les serveurs web frontaux, deux sous-réseaux privés pour les serveurs de la couche application, et deux autres sous-réseaux privés pour héberger une base de données multi-AZ. Tous les sous-réseaux seront déployés dans plusieurs AZ et incluront les configurations de connectivité entre les composants via des tables de routage et une passerelle Internet.

De plus, deux passerelles NAT dans les sous-réseaux publics garantiront que les ressources dans les sous-réseaux privés de la couche application peuvent accéder en toute sécurité à Internet pour les mises à jour et la communication inter-services sans exposition directe au monde extérieur.

Maintenant, apprenons comment vous pouvez automatiser la création de cette solution en utilisant les trois outils IaC : **AWS CloudFormation**, **AWS CDK** et **Terraform**.

## Exemples de code d'outils IaC

### Exemple AWS CloudFormation

AWS CloudFormation vous permet de définir votre infrastructure souhaitée en utilisant un fichier de configuration déclaratif JSON ou YAML. Mais vous devez définir les interdépendances et les connexions entre les ressources en utilisant des fonctions intrinsèques comme **!Ref**, en référençant d'autres ressources ou **!GetAtt**, pour aider à sélectionner dynamiquement les zones de disponibilité.

Voici comment vous définissez la solution de réseau à trois niveaux en utilisant AWS CloudFormation :

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  MyVPC:
    Type: 'AWS::EC2::VPC'
    Properties:
      CidrBlock: '10.0.0.0/16'
      EnableDnsSupport: true
      EnableDnsHostnames: true

  InternetGateway:
    Type: 'AWS::EC2::InternetGateway'

  AttachGateway:
    Type: 'AWS::EC2::VPCGatewayAttachment'
    Properties:
      VpcId: !Ref MyVPC
      InternetGatewayId: !Ref InternetGateway

  PublicSubnetOne:
    Type: 'AWS::EC2::Subnet'
    Properties:
      VpcId: !Ref MyVPC
      CidrBlock: '10.0.1.0/24'
      AvailabilityZone: !Select [0, !GetAZs '']
      MapPublicIpOnLaunch: true

  PublicSubnetTwo:
    Type: 'AWS::EC2::Subnet'
    Properties:
      VpcId: !Ref MyVPC
      CidrBlock: '10.0.2.0/24'
      AvailabilityZone: !Select [1, !GetAZs '']
      MapPublicIpOnLaunch: true

  PrivateSubnetAppOne:
    Type: 'AWS::EC2::Subnet'
    Properties:
      VpcId: !Ref MyVPC
      CidrBlock: '10.0.3.0/24'
      AvailabilityZone: !Select [0, !GetAZs '']

  PrivateSubnetAppTwo:
    Type: 'AWS::EC2::Subnet'
    Properties:
      VpcId: !Ref MyVPC
      CidrBlock: '10.0.4.0/24'
      AvailabilityZone: !Select [1, !GetAZs '']

  PrivateSubnetDBOne:
    Type: 'AWS::EC2::Subnet'
    Properties:
      VpcId: !Ref MyVPC
      CidrBlock: '10.0.5.0/24'
      AvailabilityZone: !Select [0, !GetAZs '']

  PrivateSubnetDBTwo:
    Type: 'AWS::EC2::Subnet'
    Properties:
      VpcId: !Ref MyVPC
      CidrBlock: '10.0.6.0/24'
      AvailabilityZone: !Select [1, !GetAZs '']

  EIPOne:
    Type: 'AWS::EC2::EIP'

  EIPTwo:
    Type: 'AWS::EC2::EIP'

  NATGatewayOne:
    Type: 'AWS::EC2::NatGateway'
    Properties:
      AllocationId: !GetAtt 'EIPOne.AllocationId'
      SubnetId: !Ref PublicSubnetOne

  NATGatewayTwo:
    Type: 'AWS::EC2::NatGateway'
    Properties:
      AllocationId: !GetAtt 'EIPTwo.AllocationId'
      SubnetId: !Ref PublicSubnetTwo

  PublicRouteTable:
    Type: 'AWS::EC2::RouteTable'
    Properties:
      VpcId: !Ref MyVPC

  PublicRoute:
    Type: 'AWS::EC2::Route'
    Properties:
      RouteTableId: !Ref PublicRouteTable
      DestinationCidrBlock: '0.0.0.0/0'
      GatewayId: !Ref InternetGateway

  PublicSubnetOneRouteTableAssociation:
    Type: 'AWS::EC2::SubnetRouteTableAssociation'
    Properties:
      SubnetId: !Ref PublicSubnetOne
      RouteTableId: !Ref PublicRouteTable

  PublicSubnetTwoRouteTableAssociation:
    Type: 'AWS::EC2::SubnetRouteTableAssociation'
    Properties:
      SubnetId: !Ref PublicSubnetTwo
      RouteTableId: !Ref PublicRouteTable

  PrivateAppRouteTableOne:
    Type: 'AWS::EC2::RouteTable'
    Properties:
      VpcId: !Ref MyVPC

  PrivateAppRouteTableTwo:
    Type: 'AWS::EC2::RouteTable'
    Properties:
      VpcId: !Ref MyVPC

  PrivateAppRouteOne:
    Type: 'AWS::EC2::Route'
    Properties:
      RouteTableId: !Ref PrivateAppRouteTableOne
      DestinationCidrBlock: '0.0.0.0/0'
      NatGatewayId: !Ref NATGatewayOne

  PrivateAppRouteTwo:
    Type: 'AWS::EC2::Route'
    Properties:
      RouteTableId: !Ref PrivateAppRouteTableTwo
      DestinationCidrBlock: '0.0.0.0/0'
      NatGatewayId: !Ref NATGatewayTwo

  PrivateSubnetAppOneRouteTableAssociation:
    Type: 'AWS::EC2::SubnetRouteTableAssociation'
    Properties:
      SubnetId: !Ref PrivateSubnetAppOne
      RouteTableId: !Ref PrivateAppRouteTableOne

  PrivateSubnetAppTwoRouteTableAssociation:
    Type: 'AWS::EC2::SubnetRouteTableAssociation'
    Properties:
      SubnetId: !Ref PrivateSubnetAppTwo
      RouteTableId: !Ref PrivateAppRouteTableTwo

  PrivateDBRouteTable:
    Type: 'AWS::EC2::RouteTable'
    Properties:
      VpcId: !Ref MyVPC

  PrivateSubnetDBOneRouteTableAssociation:
    Type: 'AWS::EC2::SubnetRouteTableAssociation'
    Properties:
      SubnetId: !Ref PrivateSubnetDBOne
      RouteTableId: !Ref PrivateDBRouteTable

  PrivateSubnetDBTwoRouteTableAssociation:
    Type: 'AWS::EC2::SubnetRouteTableAssociation'
    Properties:
      SubnetId: !Ref PrivateSubnetDBTwo
      RouteTableId: !Ref PrivateDBRouteTable
```

Ce script YAML crée le VPC souhaité, deux sous-réseaux publics, une passerelle Internet, deux adresses IP élastiques et deux passerelles NAT. Ici, vous exploitez également les capacités d'AWS CloudFormation pour lier les ressources et gérer explicitement les dépendances.

### Exemple AWS CDK

Lorsque vous utilisez AWS CDK, vous définissez les ressources cloud dans un style de programmation impératif. Il offre une abstraction sur AWS CloudFormation mais offre plus de flexibilité en utilisant des constructs, qui peuvent encapsuler plusieurs ressources en une seule unité logique. Il permet également d'utiliser des boucles, des conditionnelles et d'autres logiques de programmation pour générer dynamiquement vos ressources.

Lors de la configuration de ressources comme les sous-réseaux, cela est simplifié en les regroupant sous **subnet_configuration** dans un construct VPC. Cela gère automatiquement les associations de sous-réseaux pour vous.

Ci-dessous, vous utiliserez le langage de programmation Python pour définir la solution à trois niveaux avec AWS CDK :

```python
from constructs import Construct
from aws_cdk import (
	Stack,
	aws_ec2 as ec2
)

class MyVpcStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # Créer un VPC avec des configurations spécifiques
        vpc = ec2.Vpc(self, "MyVpc",
                      ip_addresses=ec2.IpAddresses.cidr("10.0.0.0/16"),
                      max_azs=2,
                      subnet_configuration=[
                          ec2.SubnetConfiguration(
                              name="PublicSubnet",
                              subnet_type=ec2.SubnetType.PUBLIC,
                              cidr_mask=24
                          ),
                          ec2.SubnetConfiguration(
                              subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,
                              name="PrivateSubnet1",
                              cidr_mask=24
                          ),
                          ec2.SubnetConfiguration(
                              subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,
                              name="PrivateSubnet2",
                              cidr_mask=24
                          )
                      ],
                      nat_gateways=2,  # Nombre de passerelles NAT
                      )
```

Comme vous pouvez le voir, ce script AWS CDK en Python est plus concis et vous permet de travailler avec un langage de programmation de haut niveau très familier, qui fournit des abstractions puissantes et tire parti de l'utilisation de constructs.

### Exemple Terraform

L'approche de Terraform implique de définir l'infrastructure en utilisant un langage de configuration déclaratif. Mais elle diffère de celle d'AWS CloudFormation dans sa gestion de l'état et des dépendances. Elle permet également une création, une mise à jour et une destruction plus contrôlées des ressources avec des constructs comme **resource**, **provider** et **variable**.

Voici comment vous définissez la même solution avec Terraform :

```hcl
provider "aws" {
  region = "us-east-1"
}

resource "aws_vpc" "my_vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true
}

# Sous-réseaux publics
resource "aws_subnet" "public_subnet_one" {
  vpc_id                  = aws_vpc.my_vpc.id
  cidr_block              = "10.0.1.0/24"
  map_public_ip_on_launch = true
  availability_zone       = "us-east-1a"
}

resource "aws_subnet" "public_subnet_two" {
  vpc_id                  = aws_vpc.my_vpc.id
  cidr_block              = "10.0.2.0/24"
  map_public_ip_on_launch = true
  availability_zone       = "us-east-1b"
}

# Sous-réseaux privés pour la couche application
resource "aws_subnet" "private_app_subnet_one" {
  vpc_id            = aws_vpc.my_vpc.id
  cidr_block        = "10.0.3.0/24"
  availability_zone = "us-east-1a"
}

resource "aws_subnet" "private_app_subnet_two" {
  vpc_id            = aws_vpc.my_vpc.id
  cidr_block        = "10.0.4.0/24"
  availability_zone = "us-east-1b"
}

# Sous-réseaux privés pour la couche base de données
resource "aws_subnet" "private_db_subnet_one" {
  vpc_id            = aws_vpc.my_vpc.id
  cidr_block        = "10.0.5.0/24"
  availability_zone = "us-east-1a"
}

resource "aws_subnet" "private_db_subnet_two" {
  vpc_id            = aws_vpc.my_vpc.id
  cidr_block        = "10.0.6.0/24"
  availability_zone = "us-east-1b"
}

resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.my_vpc.id
}

resource "aws_nat_gateway" "nat_gateway_one" {
  allocation_id = aws_eip.nat_one.id
  subnet_id     = aws_subnet.public_subnet_one.id
}

resource "aws_nat_gateway" "nat_gateway_two" {
  allocation_id = aws_eip.nat_two.id
  subnet_id     = aws_subnet.public_subnet_two.id
}

resource "aws_eip" "nat_one" {
  domain = "vpc"
}

resource "aws_eip" "nat_two" {
  domain = "vpc"
}

# Table de routage publique
resource "aws_route_table" "public_rt" {
  vpc_id = aws_vpc.my_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }
}

# Tables de routage privées pour la couche application
resource "aws_route_table" "private_app_rt_one" {
  vpc_id = aws_vpc.my_vpc.id

  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.nat_gateway_one.id
  }
}

resource "aws_route_table" "private_app_rt_two" {
  vpc_id = aws_vpc.my_vpc.id

  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.nat_gateway_two.id
  }
}

# Tables de routage privées pour la couche base de données
resource "aws_route_table" "private_db_rt" {
  vpc_id = aws_vpc.my_vpc.id
}

# Associations de tables de routage
resource "aws_route_table_association" "public_subnet_one_association" {
  subnet_id      = aws_subnet.public_subnet_one.id
  route_table_id = aws_route_table.public_rt.id
}

resource "aws_route_table_association" "public_subnet_two_association" {
  subnet_id      = aws_subnet.public_subnet_two.id
  route_table_id = aws_route_table.public_rt.id
}

resource "aws_route_table_association" "private_app_subnet_one_association" {
  subnet_id      = aws_subnet.private_app_subnet_one.id
  route_table_id = aws_route_table.private_app_rt_one.id
}

resource "aws_route_table_association" "private_app_subnet_two_association" {
  subnet_id      = aws_subnet.private_app_subnet_two.id
  route_table_id = aws_route_table.private_app_rt_two.id
}

resource "aws_route_table_association" "private_db_subnet_one_association" {
  subnet_id      = aws_subnet.private_db_subnet_one.id
  route_table_id = aws_route_table.private_db_rt.id
}

resource "aws_route_table_association" "private_db_subnet_two_association" {
  subnet_id      = aws_subnet.private_db_subnet_two.id
  route_table_id = aws_route_table.private_db_rt.id
}
```

Ce script montre comment Terraform permet une approche modulaire de l'infrastructure as code, avec des définitions explicites et une gestion des dépendances avec une syntaxe relativement facile à lire et à écrire.

## Analyse et comparaison

Lorsque vous choisissez entre AWS CloudFormation, AWS CDK et Terraform pour gérer l'infrastructure cloud, vous devez prendre en compte un certain nombre de facteurs. Mais dans cet article, nous nous concentrerons spécifiquement sur la **facilité d'utilisation**, la **flexibilité**, l'**évolutivité**, le **support des langages** et la **capacité à gérer des environnements complexes**. 

### Facilité d'utilisation et courbe d'apprentissage

AWS CloudFormation offre un format de modèle basé sur JSON ou YAML. Cela est simple pour définir l'infrastructure, mais peut devenir complexe à mesure que l'infrastructure grandit. Il nécessite une compréhension de la syntaxe spécifique et des définitions de ressources AWS, ce qui peut représenter une courbe d'apprentissage plus raide pour ceux qui ne sont pas familiers avec JSON ou YAML.

AWS CDK utilise des langages de programmation familiers comme Python, JavaScript, TypeScript et Java. Cela peut le rendre plus accessible pour les développeurs déjà familiers avec ces langages. 

De plus, comme AWS CDK permet de définir l'infrastructure via du code, il offre une logique, des conditions et des boucles plus intuitives, et il abstrait une grande partie du code standard nécessaire dans AWS CloudFormation. Cela simplifie le processus de développement.

Terraform utilise son propre langage spécifique de domaine, le HashiCorp Configuration Language (HCL), qui est conçu pour être facilement lisible et écrivable par les humains. Bien qu'il puisse être facile à apprendre, vous devrez vous familiariser avec un autre nouveau langage. Cependant, sa nature déclarative permet des définitions claires de **ce à quoi** l'infrastructure devrait ressembler sans avoir besoin de spécifier **comment** l'atteindre.

### Flexibilité et support des fournisseurs cloud

AWS CloudFormation est étroitement intégré à AWS et est mis à jour en tandem avec les services AWS. Mais il est intrinsèquement limité à AWS, ce qui le rend moins adapté aux possibilités d'environnements hybrides ou multi-cloud.

AWS CDK cible principalement les services AWS mais supporte l'utilisation de ressources personnalisées AWS CloudFormation pour gérer des ressources en dehors d'AWS. Cependant, il ne se prête pas naturellement à la gestion de ressources multi-cloud aussi directement que Terraform.

Terraform est conçu pour être agnostique du cloud, supportant plusieurs fournisseurs dont AWS, Microsoft Azure, Google Cloud Platform et d'autres. Cela en fait un choix idéal pour des déploiements complexes s'étendant sur plus d'un fournisseur cloud.

### Évolutivité et maintenabilité

Les modèles AWS CloudFormation peuvent devenir encombrants et difficiles à gérer à mesure que les projets grandissent. Mais AWS fournit des stacks imbriqués comme solution pour gérer de grandes infrastructures, mais même avec cette capacité, la gestion de nombreuses stacks peut devenir fastidieuse.

AWS CDK fournit des abstractions de haut niveau et des constructs modulaires, facilitant la gestion et l'évolutivité de grandes infrastructures en les décomposant en composants plus petits et réutilisables.

Terraform excelle dans la gestion d'infrastructures à grande échelle grâce à son approche modulaire. En utilisant des modules Terraform, vous pouvez réutiliser des configurations et assurer la cohérence des déploiements.

### Support communautaire et écosystème

AWS CloudFormation bénéficie d'une grande adoption et d'un support d'AWS avec une large base d'utilisateurs, mais ses contributions communautaires sont limitées au partage de modèles.

AWS CDK est open-source et dispose d'une communauté croissante, en particulier parmi les développeurs préférant utiliser des langages de programmation polyvalents pour la gestion de l'infrastructure. L'écosystème comprend un ensemble riche de constructs de haut niveau développés à la fois par AWS et la communauté.

Terraform bénéficie d'un fort engagement communautaire et d'un vaste écosystème de fournisseurs et de modules partagés publiquement dans le Terraform Registry. Son adoption large sur différentes plateformes aide également à favoriser une grande et active communauté.

### Longueur du code et complexité

Les scripts AWS CloudFormation tendent à être verbeux, nécessitant des spécifications détaillées de chaque propriété. Cela peut conduire à des modèles longs et complexes pour des infrastructures plus grandes.

Les scripts AWS CDK sont généralement plus courts et moins complexes grâce à l'utilisation de constructs de programmation qui abstraient une grande partie des spécifications détaillées requises dans AWS CloudFormation.

Les configurations Terraform trouvent un équilibre, étant plus concises qu'AWS CloudFormation mais généralement plus verbeuses qu'AWS CDK en raison de sa nature déclarative, qui nécessite des définitions explicites de ressources et de configurations.

## Pourquoi choisir l'un plutôt que l'autre ?

Lorsque vous choisissez entre AWS CloudFormation, AWS CDK et Terraform, prenez en compte les fonctionnalités uniques de chaque outil, leurs principes opérationnels et vos propres préférences personnelles.

Maintenant, je vais partager des recommandations basées sur les informations de cet article pour vous aider à déterminer quand il est préférable d'utiliser chacun de ces outils IaC.

* AWS CloudFormation est adapté lorsque vous recherchez un outil natif AWS stable et que vous n'avez pas nécessairement besoin de gérer des ressources en dehors d'AWS. Il est particulièrement adapté lorsque la conformité avec des configurations AWS spécifiques est requise.
* Choisissez AWS CDK lorsque vous préférez utiliser des langages de programmation standard et que vous appréciez les avantages des techniques orientées objet pour créer des composants cloud réutilisables et modulaires. Il est généralement plus attrayant pour les développeurs qui souhaitent appliquer les meilleures pratiques de développement logiciel à l'approvisionnement d'infrastructure.
* Terraform est le leader ultime pour les environnements multi-cloud, ou si vous avez besoin d'un outil à la fois puissant et flexible pour gérer des architectures complexes. C'est également le bon choix si vous prévoyez d'intégrer une variété de services cloud et avez besoin d'une approche unifiée pour les gérer.

Bien que ces recommandations soient basées sur les caractéristiques spécifiques de chacun de ces outils IaC, je vous conseille d'acquérir une certaine expérience avec chaque outil, afin de pouvoir décider de celui qui correspond le mieux aux compétences et aux besoins spécifiques de votre équipe et de vos projets.

Si vous êtes arrivé jusqu'ici, **merci beaucoup d'avoir lu !** J'espère que cela en valait la peine pour vous.

Si vous souhaitez en savoir plus sur moi et mon histoire de transition d'un athlète professionnel à un ingénieur cloud, connectez-vous avec moi **[ici sur LinkedIn](https://www.linkedin.com/in/ifeanyi-otuonye/)**.