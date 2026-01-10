---
title: Comment déployer une infrastructure AWS avec Terraform et GitHub Actions –
  Un guide CI/CD multi-environnement
subtitle: ''
author: Nitheesh Poojary
co_authors: []
series: null
date: '2022-02-11T19:09:46.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-aws-infrastructure-with-terraform-and-github-actions-a-practical-multi-environment-ci-cd-guide
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/pexels-pixabay-163235.jpg
tags:
- name: AWS
  slug: aws
- name: Cloud
  slug: cloud
- name: GitHub
  slug: github
- name: Terraform
  slug: terraform
seo_title: Comment déployer une infrastructure AWS avec Terraform et GitHub Actions
  – Un guide CI/CD multi-environnement
seo_desc: "Recently, I've been considering developing a complete end-to-end greenfield\
  \ DevOps personal lab project. \nThe term \"greenfield software project\" refers\
  \ to the development of a system for a new product that requires development from\
  \ scratch with no le..."
---

Récemment, j'ai envisagé de développer un projet de laboratoire DevOps personnel complet de bout en bout sur un terrain vierge. 

Le terme "projet logiciel sur terrain vierge" fait référence au développement d'un système pour un nouveau produit qui nécessite un développement à partir de zéro sans code hérité. 

C'est une méthode que vous utilisez lorsque vous commencez à partir de zéro et que vous n'avez aucune contrainte ou dépendance. Vous avez une opportunité fantastique de construire une solution à partir de zéro. Le projet est ouvert à de nouveaux outils et architectures.

J'ai cherché sur Internet des idées sur la manière de mettre en place un pipeline CI/CD pour le déploiement Terraform. Mais je n'ai pas trouvé d'instructions complètes de bout en bout pour le déploiement Terraform. 

La majorité des guides et des articles de blog que j'ai découverts discutent du pipeline de déploiement pour des environnements uniques (Prod). J'ai donc choisi de construire mon projet de laboratoire personnel et d'en faire un article de blog. 

Dans cet article, je vais discuter de l'ensemble du flux de travail de déploiement Terraform, des environnements de développement à ceux de production. Je vais également présenter les sujets et les techniques que je vais utiliser dans mon projet de laboratoire.

Il y a deux raisons pour lesquelles j'ai choisi Terraform comme outil d'infrastructure en tant que code. La première est que j'ai utilisé CloudFormation depuis longtemps et que j'ai beaucoup d'expérience avec celui-ci, donc je voulais acquérir de l'expérience avec Terraform. 

La deuxième raison pour laquelle j'ai choisi Terraform est que ce projet est un projet DevOps sur terrain vierge, donc je peux choisir une technologie moderne et jouer avec. 

Je vais passer en revue certaines des fonctionnalités de Terraform dans cet article. Commençons.

## Outils de déploiement

Avant d'aborder les modèles de déploiement, je voudrais passer en revue les outils que je vais utiliser.

### Terraform

Terraform est un framework de provisionnement open-source. C'est une application multiplateforme qui peut fonctionner sur Windows, Linux et macOS. 

Vous pouvez utiliser Terraform de trois manières.

* Terraform OSS (Gratuit)
* Terraform Cloud (Payant - Modèle SaaS)
* Terraform Enterprise (Payant - Auto-hébergé)

![bj3ZlORR_](https://www.freecodecamp.org/news/content/images/2022/02/bj3ZlORR_.jpeg)

### Qu'est-ce que Terraform Cloud ?

Pour mon projet de laboratoire, j'utilise Terraform Cloud. Terraform OSS est fantastique pour les petites équipes, mais à mesure que votre équipe grandit, la difficulté d'administrer Terraform augmente également. Terraform Cloud de HashiCorp est une offre SaaS commerciale.

![LvbPPn6sH](https://www.freecodecamp.org/news/content/images/2022/02/LvbPPn6sH.jpeg)

**Offres Terraform Cloud**

* Flux de travail Terraform à distance pour les équipes.
* Connexion VCS (GitHub, GitLab, Bitbucket) Gestion de l'état (Stockage, Historique et Verrouillage)
* Authentification unique (SSO) intégrée à Okta avec une interface utilisateur complète
* Terraform Cloud sert de backend distant pour l'état de votre Terraform.
* Terraform Cloud intègre le framework de politique-as-code Sentinel, qui vous permet d'établir et de faire respecter des politiques spécifiques pour la manière dont votre entreprise provisionne l'infrastructure. Vous pouvez limiter le nombre de VM de calcul, restreindre les mises à jour importantes à des périodes de maintenance prédéfinies, et effectuer une variété d'autres tâches.
* Terraform Cloud peut afficher une estimation de son coût total ainsi que tout changement de coût causé par les modifications proposées.

### GitHub Actions (CI/CD)

Vous pouvez utiliser Terraform CLI ou la console Terraform pour déployer l'infrastructure depuis votre ordinateur portable. 

Si vous êtes un membre unique de l'équipe, cela peut fonctionner pendant un certain temps. Mais cette stratégie ne sera pas évolutive à mesure que votre équipe grandit. Vous devez déployer depuis un emplacement centralisé où tout le monde a une visibilité, un contrôle et des capacités de retour en arrière.

Il existe de nombreuses technologies disponibles pour le déploiement depuis un emplacement centralisé (CI/CD). J'avais l'intention d'essayer le déploiement du pipeline Terraform en utilisant la technique "GitOps". 

Un dépôt Git sert de source unique de vérité pour les définitions d'infrastructure dans GitOps. Pour toutes les modifications d'infrastructure, GitOps utilise les demandes de fusion comme méthode de changement. Lorsque du nouveau code est intégré, le pipeline CI/CD met à jour l'environnement. GitOps écrase automatiquement toute dérive de configuration, telle que les modifications manuelles ou les erreurs.

Pour mon déploiement, j'utiliserai GitHub Actions.

GitHub Actions vous permet d'automatiser des tâches tout au long du cycle de vie du développement logiciel. Les actions GitHub sont pilotées par des événements, ce qui signifie que vous pouvez exécuter une série de commandes en réponse à un événement spécifique. 

Par exemple, vous pouvez exécuter une commande qui exécute un script de test, un script de planification et un script d'application chaque fois que quelqu'un écrit une demande de pull pour un dépôt. Cela vous permet d'incorporer des capacités d'intégration continue (CI) et de déploiement continu (CD), ainsi qu'une variété d'autres fonctionnalités, directement dans votre dépôt.

![PC6GGaSwk](https://www.freecodecamp.org/news/content/images/2022/02/PC6GGaSwk.jpeg)

**Fonctionnalités des actions GitHub**

* Les actions GitHub sont entièrement intégrées à GitHub et peuvent être contrôlées aux côtés de vos autres fonctionnalités liées au dépôt, comme les demandes de pull et les problèmes.
* Elles disposent d'un support pour les conteneurs Docker
* Les actions GitHub sont disponibles gratuitement pour tous les dépôts et offrent 2000 minutes de build gratuites par mois pour tous les dépôts privés.

Consultez ce [lien](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions) pour obtenir plus d'informations sur les actions disponibles sur GitHub.

Jusqu'à présent, j'ai présenté les outils et services que je vais utiliser dans mon pipeline de déploiement. Maintenant, je vais examiner la structure du répertoire Terraform. 

Pour résumer, je vais utiliser Terraform Cloud et GitHub Actions. Une autre chose à noter est que je ne vais pas entrer dans les détails de l'écriture du code Terraform dans cet article. Je vais utiliser du code du registre Terraform. Merci beaucoup, Anton Babenko.

## Configuration du projet

Supposons que vous venez de commencer un nouvel emploi et que votre première tâche est de créer des VPC. Ils veulent que vous configuriez trois VPC pour eux (Dev→Stage→Prod VPC). Vous avez décidé d'utiliser Terraform pour déployer les VPC.

### Structure du répertoire Terraform

Votre première étape devrait être de créer la structure du répertoire Terraform. Vous n'avez pas besoin d'établir une structure de répertoire si vous avez précédemment utilisé cloud-formation car vous n'avez pas besoin de gérer les fichiers d'état ou les modules. Mais lors de l'utilisation de Terraform, il est crucial de définir la structure du répertoire. 

Tout d'abord, je vais fournir plusieurs exemples de structures de répertoires couramment utilisées, suivis d'informations sur le répertoire que je vais utiliser dans mon projet.

**Structure de répertoire de base**

![I-Yg30jok](https://www.freecodecamp.org/news/content/images/2022/02/I-Yg30jok.jpeg)

Dans cette disposition, vous aurez trois fichiers. Votre fichier principal est main.tf. C'est le fichier dans lequel toutes les ressources sont définies.

```
{
  resource "aws_vpc" "this" {

  cidr_block = var.cidr
 }
}
```

variables.tf est l'endroit où vous définissez vos variables d'entrée :

```
variable "cidr" {
 description = "Le bloc CIDR pour le VPC"
 type        = string
 default     = "10.0.0.0/16"
}
```

outputs.tf : les valeurs de sortie sont définies dans ce fichier :

```
output "vpc_id" {
  description = "L'ID du VPC"
  value       = concat(aws_vpc.this.*.id, [""])[0]
}

```

Si vous travaillez sur un projet modeste avec une petite équipe, cette structure fonctionnera bien. Mais à mesure que vous utilisez des modules et travaillez sur des projets plus grands, cette structure ne pourra pas évoluer aussi bien.

### Structure de répertoire complexe et évolutive

Vous ne pourrez pas faire évoluer votre projet ou votre équipe avec la structure de répertoire de base. 

Plusieurs habitats et zones seront nécessaires pour le projet plus large. Vous aurez besoin d'une bonne structure de répertoire pour transférer l'infrastructure des environnements de développement aux environnements de production en utilisant une solution CI/CD. Vous pouvez utiliser les modules Terraform dans cette structure.

> Les modules sont des configurations Terraform réutilisables qui peuvent être appelées et configurées par d'autres configurations.
> 

```

├── environments
│   ├── dev
│   │   ├── compute.tf
│   │   ├── dev.tfvars
│   │   ├── outputs.tf
│   │   ├── rds.tf
│   │   ├── s3.tf
│   │   ├── variables.tf
│   │   └── vpc.tf
│   ├── prod
│   │   ├── compute.tf
│   │   ├── outputs.tf
│   │   ├── prod.tfvars
│   │   ├── rds.tf
│   │   ├── s3.tf
│   │   ├── variables.tf
│   │   └── vpc.tf
│   └── stage
│       ├── compute.tf
│       ├── outputs.tf
│       ├── rds.tf
│       ├── s3.tf
│       ├── stage.tfvars
│       ├── variables.tf
│       └── vpc.tf
└── modules
    ├── compute
    │   ├── main.tf
    │   ├── outputs.tf
    │   └── variables.tf
    ├── rds
    │   ├── main.tf
    │   ├── outputs.tf
    │   └── variables.tf
    ├── s3
    │   ├── main.tf
    │   ├── outputs.tf
    │   └── variables.tf
    ├── security-group
    │   ├── main.tf
    │   ├── outputs.tf
    │   └── variables.tf
    └── vpc
        ├── main.tf
        ├── outputs.tf
        └── variables.tf
```

J'ai remarqué que beaucoup de projets utilisent cette structure. Dans ce cas, le contenu de chaque environnement sera presque identique. 

Mais à mon avis, le contenu devrait être le même dans tous les environnements. Pour tous les environnements, nous devrions utiliser le même fichier main.tf. Les variables peuvent être utilisées pour ajuster le nombre de serveurs ou le nombre de sous-réseaux.

```
variable "instance_count" {
  description = "Nombre de serveurs"
}

variable "instance_type" {
  description = "Taille de l'instance (t2.micro, t2.large"
}

```

**Structure de répertoire proposée**

Avoir un dossier séparé et un fichier de configuration séparé, comme je l'ai décrit dans la section précédente, a peu de sens. Vous pouvez me contacter si vous pensez qu'il y a un avantage à avoir un dossier différent pour chaque configuration. 

Par conséquent, voici ma structure de répertoire proposée pour le déploiement VPC.

VPC : github.com/nitheesh86/network-vpc

Groupe de sécurité : github.com/nitheesh86/network-sg

Compute-ASG : github.com/nitheesh86/compute-asg

Vous vous demandez peut-être comment vous allez référencer les ressources de plusieurs dépôts. C'est là que l'espace de travail Terraform cloud sera utile. Je vais aborder cela plus en détail plus tard dans l'article.

Si vous regardez le répertoire ci-dessus, vous pourriez supposer qu'il ressemble à une "Structure de répertoire de base". Vous pourriez également vous demander où se trouvent les répertoires de modules. Oui, les répertoires semblent identiques, mais la magie se produit à l'intérieur des fichiers de configuration.

```
terraform {
  required_version = "~> 0.12"
  backend "remote" {
    hostname     = "app.terraform.io"
    organization = "xxxxxxxx"
    workspaces { prefix = "vpc-" }
  }
}

provider "aws" {
  region = "ap-south-1"
}


module "vpc" {
  source = "github.com/nitheesh86/terraform-modules/modules/vpc"

  name = var.name
  cidr = "10.0.0.0/16"

  azs             = ["ap-south-1a", "ap-south-1b", "ap-south-1c"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]

  enable_nat_gateway = true
  enable_vpn_gateway = true

  tags = {
    Terraform   = "true"
    Environment = var.env
  }
}

```

J'ai maintenu les modules séparés des configurations. Tous mes modules sont placés dans un dépôt séparé. Je vais référencer ce module par son URL de dépôt Git.
> L'argument source dans un bloc de module indique à Terraform où trouver le code source pour le module enfant souhaité.
> 

Terraform prend en charge les sources dans les modules suivants :

* Chemins locaux
* Registre Terraform
* GitHub
* Bitbucket
* Dépôts Git, Mercurial génériques
* URLs HTTP
* Seaux S3
* Seaux GCS

Nous pouvons utiliser le registre Terraform comme source de module car nous utilisons Terraform Cloud. Cependant, chaque module a besoin de son propre dépôt git. Si vous publiez des modules vpc (terraform-aws-vpc), par exemple, vous ne pouvez fournir que du code pour ces ressources vpc qui sont pertinentes pour le module. Un autre dépôt est nécessaire pour le module de groupe de sécurité (terraform-aws-sg).

> Un module par dépôt. Le registre ne peut pas utiliser de dépôts combinés avec plusieurs modules.
> 

Cependant, il vaut la peine d'envisager cette structure si votre organisation dispose d'une équipe réseau, sécurité et informatique distincte. Chaque équipe peut gérer ses modules indépendamment.

## Composants de Terraform Cloud

### Organisations

Les organisations sont un espace partagé dans Terraform Cloud pour que les équipes collaborent sur des espaces de travail. Les configurations d'état distant peuvent être partagées entre les organisations. 

Vous pouvez, par exemple, créer des entreprises basées sur un projet ou un produit. Par exemple, si vous essayez de créer un produit Apple, vous pouvez le nommer "apple". "nitheeshp" est le nom que j'ai donné à mon projet.

![KR3DCPRWz](https://www.freecodecamp.org/news/content/images/2022/02/KR3DCPRWz.jpeg)

### Espaces de travail

Au lieu de répertoires, Terraform Cloud maintient des collections d'infrastructures à l'aide d'espaces de travail. Un espace de travail est lié à des contextes tels que dev, staging et prod. 

Les configurations Terraform, les valeurs de variables et les fichiers d'état associés à un environnement sont tous stockés dans l'espace de travail. Chaque espace de travail conserve des sauvegardes des fichiers d'état précédents.

Dans mon projet, j'ai configuré un espace de travail pour chaque service Amazon Web Services. Chaque espace de travail peut être lié à une branche Git ou à un dépôt Git.

![ncNrBPUb7](https://www.freecodecamp.org/news/content/images/2022/02/ncNrBPUb7.jpeg)

Lorsque vous créez un espace de travail, vous avez trois options pour concevoir votre flux de travail Terraform :

* Flux de travail de contrôle de version
* Flux de travail piloté par CLI
* Flux de travail piloté par API

![wsGudB1Pa](https://www.freecodecamp.org/news/content/images/2022/02/wsGudB1Pa.jpeg)

Si vous regardez ma structure de répertoire Terraform ci-dessous, vous remarquerez que je n'ai pas défini de valeurs par défaut pour mes variables. Les variables ont été liées dans les paramètres de l'espace de travail Terraform.

![GbQMtKo2F](https://www.freecodecamp.org/news/content/images/2022/02/GbQMtKo2F.jpeg)

Si vous regardez main.tf, vous remarquerez que tous les environnements utilisent la même configuration cloud Terraform. Vous pourriez être curieux de savoir comment je procède pour apporter des modifications à un espace de travail spécifique. C'est le préfixe de l'espace de travail que j'utilise.

```
terraform {
  required_version = "~> 0.12"
  backend "remote" {
    hostname     = "app.terraform.io"
    organization = "nitheeshp"
    workspaces { prefix = "vpc-" }
  }
}
```

Lorsque vous ajoutez un espace de travail à votre configuration, il vous demandera de choisir un espace de travail. Par exemple :

```
$ terraform init

Initialisation du backend...

Configuration réussie du backend "remote" ! Terraform utilisera automatiquement
ce backend à moins que la configuration du backend ne change.

L'espace de travail actuellement sélectionné (par défaut) n'existe pas.
  C'est un comportement attendu lorsque l'espace de travail sélectionné n'avait pas
  d'état non vide existant. Veuillez entrer un numéro pour sélectionner un espace de travail :

  1. dev
  2. stage
  3. prod

  Entrez une valeur :

```

Définissez la variable d'environnement TF_WORKSPACE sur le nom de l'espace de travail que vous souhaitez sélectionner lors de l'utilisation de Terraform dans CI/CD.

```
export TF_WORKSPACE="dev"
```

### Comment déployer des groupes de sécurité

Comme mentionné précédemment, je déploie des groupes de sécurité en utilisant un dépôt et un espace de travail séparés. Un identifiant VPC est nécessaire pour le déploiement des groupes de sécurité. C'est là que les sources de données Terraform interviennent.

> Les sources de données permettent de récupérer ou de calculer des données pour une utilisation ailleurs dans la configuration Terraform. L'utilisation de sources de données permet à une configuration Terraform de faire usage d'informations définies en dehors de Terraform, ou définies par une autre configuration Terraform distincte.
> 

```
data "terraform_remote_state" "vpc" {
  backend = "remote"

  config = {
    organization = "nitheeshp"
    workspaces = {
     name = "vpc-${var.env}"
    }
  }
}

provider "aws" {
  region = "ap-south-1"
}


module "elb_sg" {
  source = "terraform-aws-modules/security-group/aws"

  name        = "${var.env}-elb-sg"
  description = "groupe de sécurité elb."
  vpc_id      = data.terraform_remote_state.vpc.outputs.vpc_id

  egress_with_cidr_blocks = [
    {
      from_port   = 0
      to_port     = 65535
      protocol    = "all"
      description = "Internet ouvert"
      cidr_blocks = "0.0.0.0/0"
    }
  ]

```

Comme vous pouvez le voir, je récupère l'identifiant VPC depuis l'espace de travail vpc-dev.

```
vpc_id      = data.terraform_remote_state.vpc.outputs.vpc_id
```

### GitHub Actions

Comme nous l'avons discuté ci-dessus, nous allons également utiliser GitHub Actions dans notre pipeline de déploiement.

![3Xxi80ooR](https://www.freecodecamp.org/news/content/images/2022/02/3Xxi80ooR.png)

GitHub Actions simplifie l'automatisation de tous vos flux de travail CI/CD. Vous pouvez construire, tester et déployer du code directement depuis votre dépôt GitHub. Vous pouvez également effectuer des revues de code, la gestion des branches et le tri des problèmes de la manière dont vous souhaitez qu'ils fonctionnent. GitHub Actions offre des plans gratuits.

![eD4NRbeS-g](https://www.freecodecamp.org/news/content/images/2022/02/eD4NRbeS-g.jpeg)

## GitOps et flux de travail Terraform

![3Wg3lPnMu](https://www.freecodecamp.org/news/content/images/2022/02/3Wg3lPnMu.jpeg)

* Chaque service a son propre dépôt (Network-VPC, Network-Security Groups, Compute-ASG, Compute-EC2)
* J'ai créé trois branches (Develop, Stage et Prod). Chaque branche reflète l'un de nos environnements d'infrastructure réels ou les espaces de travail terraform.
* Le flux de travail commence lorsque l'ingénieur DevOps commence à apporter des modifications à l'infrastructure.
* Un ingénieur DevOps développe une branche de fonctionnalité à partir de la branche master (production)
* Apportez vos modifications et soumettez une demande de pull à l'équipe de développement de la branche.

J'ai créé un flux de travail séparé pour chaque branche (terraform-develop.yml, terraform-stage.yml, terraform-prod.yml). Le flux de travail est une procédure que vous ajoutez à votre dépôt. 

Les flux de travail se composent d'un ou plusieurs jobs qui peuvent être planifiés ou déclenchés par un événement. Vous pouvez utiliser le flux de travail pour créer, tester, packager, publier ou déployer un projet GitHub.

GitWorkFlow va :
* Vérifier le code de la branche de fonctionnalité.
* Vérifier la syntaxe.
* Initialiser Terraform.
* Générer un plan pour chaque demande de pull.
* Lorsque une demande de pull est fusionnée avec la branche de développement, elle déploie les ressources dans l'environnement de développement.
* Déployer les modifications de la branche de développement.
* Créer à nouveau des demandes de pull vers la branche de stage et de même vers la branche de production.

Voici les dépôts GitHub pour ce projet si vous souhaitez y jeter un coup d'œil :

* github.com/nitheesh86/network-vpc
* github.com/nitheesh86/network-sg
* github.com/nitheesh86/terraform-modules

J'adorerais en savoir plus sur vos méthodes de déploiement Terraform. N'hésitez pas à me contacter si vous souhaitez les partager et en discuter davantage.