---
title: Apprendre Terraform en déployant un serveur Jenkins sur AWS
subtitle: ''
author: Destiny Erhabor
co_authors: []
series: null
date: '2022-07-26T18:03:50.000Z'
originalURL: https://freecodecamp.org/news/learn-terraform-by-deploying-jenkins-server-on-aws
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/pexels-pok-rie-2003885.jpg
tags:
- name: AWS
  slug: aws
- name: deployment
  slug: deployment
- name: Devops
  slug: devops
- name: Jenkins
  slug: jenkins
- name: Terraform
  slug: terraform
seo_title: Apprendre Terraform en déployant un serveur Jenkins sur AWS
seo_desc: 'Hello, everyone! Today we''re going to learn about Terraform by building
  a project.

  Terraform is more than just a tool to boost the productivity of operations teams.
  You have the chance to transform your developers into operators by implementing
  Terra...'
---

Bonjour à tous ! Aujourd'hui, nous allons apprendre Terraform en construisant un projet.

Terraform est bien plus qu'un simple outil pour booster la productivité des équipes opérationnelles. Vous avez l'opportunité de transformer vos développeurs en opérateurs en implémentant Terraform.

Cela peut aider à augmenter l'efficacité de toute votre équipe d'ingénierie et améliorer la communication entre les développeurs et les opérateurs.

Dans cet article, je vais vous montrer comment automatiser entièrement le déploiement de vos services Jenkins sur le cloud AWS en utilisant Terraform avec une image personnalisée.

## Table des matières

* [Qu'est-ce que Terraform ?](#heading-qu-est-ce-que-terraform)
* [Pourquoi devriez-vous utiliser Terraform ?](#heading-pourquoi-devriez-vous-utiliser-terraform)
* [Comment fonctionne Terraform](#heading-comment-fonctionne-terraform)
* [Qu'est-ce qu'un langage procédural vs un langage déclaratif ?](#heading-qu-est-ce-qu-un-langage-procedural-vs-un-langage-declaratif)
* [Prérequis et installation](#heading-prerequis-et-installation)
* [Structure des fichiers/dossiers de notre projet](#heading-structure-des-fichiersdossiers-de-notre-projet)
* [Comment initialiser l'état de Terraform pour la première fois](#heading-comment-initialiser-l-etat-de-terraform-pour-la-premiere-fois)
* [Comment approvisionner un cloud privé virtuel AWS](#heading-comment-approvisionner-un-cloud-prive-virtuel-aws)
* [Comment travailler avec les modules Terraform](#heading-comment-travailler-avec-les-modules-terraform)
* [Comment créer un sous-réseau VPC](#heading-comment-creer-un-sous-reseau-vpc)
* [Comment configurer les tables de routage VPC](#heading-comment-configurer-les-tables-de-routage-vpc)
* [Comment créer une table de routage publique](#heading-comment-creer-une-table-de-routage-publique)
* [Comment créer une table de routage privée](#heading-comment-creer-une-table-de-routage-privee)
* [Comment configurer un hôte bastion VPC](#heading-comment-configurer-un-hote-bastion-vpc)
* [Comment approvisionner notre service de calcul](#heading-comment-approvisionner-notre-service-de-calcul)
* [Instance maître Jenkins](#heading-instance-maitre-jenkins)
* [Comment créer le load balancer](#heading-comment-creer-le-load-balancer)
* [Nettoyage](#heading-nettoyage)
* [Résumé](#heading-resume)

# Qu'est-ce que Terraform ?

Terraform par HashiCorp est une solution d'infrastructure en tant que code. Il vous permet de spécifier les ressources cloud et sur site dans des fichiers de configuration lisibles par l'homme que vous pouvez réutiliser et partager. C'est un outil puissant de provisionnement DevOps.

# Pourquoi devriez-vous utiliser Terraform ?

Terraform a un certain nombre de cas d'utilisation, y compris la capacité de :

* Spécifier l'infrastructure dans la configuration/code et reconstruire/modifier facilement et suivre les modifications de l'infrastructure.
* Prendre en charge différentes plateformes cloud
* Effectuer des modifications incrémentielles des ressources
* Prendre en charge le réseau défini par logiciel

# Comment fonctionne Terraform

Examinons comment Terraform fonctionne à un niveau élevé.

Terraform est développé dans le langage de programmation Go. Le code Go est compilé en **terraform**, un seul binaire. Vous pouvez utiliser ce binaire pour déployer l'infrastructure à partir de votre ordinateur portable, d'un serveur de build, ou de presque tout autre ordinateur, et vous n'aurez pas besoin d'exécuter une infrastructure supplémentaire pour ce faire.

C'est parce que le binaire Terraform effectue des appels d'API en votre nom à un ou plusieurs fournisseurs, qui incluent Azure, AWS, Google Cloud, DigitalOcean, et d'autres. Cela permet à Terraform de tirer parti de l'infrastructure que ces fournisseurs ont déjà mise en place pour leurs serveurs API, ainsi que des processus d'authentification qu'ils nécessitent.

**Mais Terraform ne sait pas quelles requêtes API faire – alors comment le sait-il ?** Les configurations Terraform, qui sont des fichiers texte en **langage déclaratif** qui spécifient quelle infrastructure vous souhaitez générer, sont la réponse. Le "code" dans "infrastructure en tant que code" est ces configurations.

Vous avez un contrôle complet sur votre infrastructure, y compris les serveurs, les bases de données, les équilibreurs de charge, la topologie du réseau, et plus encore. En votre nom, le binaire Terraform analyse votre code et le convertit en une série d'appels d'API aussi rapidement que possible.

# Qu'est-ce qu'un langage procédural vs un langage déclaratif ?

Un langage procédural vous permet de spécifier l'ensemble du processus et de lister les étapes nécessaires pour le compléter. Vous donnez simplement des instructions et spécifiez comment le processus sera exécuté. Chef et Ansible encouragent cette méthode.

Les langages déclaratifs, en revanche, vous permettent de simplement définir la commande ou l'ordre et de laisser le système l'exécuter. Vous n'avez pas besoin d'entrer dans le processus ; vous avez juste besoin du résultat. Des exemples sont Terraform, CloudFormation, et Puppeteer.

Assez de théorie...

Maintenant est le moment de mettre en action la haute disponibilité, la sécurité, la performance et la fiabilité de Terraform.

Ici, nous parlons d'un serveur Jenkins basé sur Terraform sur Amazon Web Services. Nous configurons le réseau à partir de zéro, alors commençons.

## Prérequis et installation

Il y a quelques choses que vous devrez avoir configurées et installées pour suivre ce tutoriel :

* [Créer un compte AWS](https://aws.amazon.com/console/)
* [Créer un utilisateur IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console)
* [Créer et télécharger votre clé secrète et d'accès utilisateur](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey)
* [Installer Terraform depuis la page Learn de Terraform - HashiCorp](https://learn.hashicorp.com/tutorials/terraform/install-cli)

## Structure des fichiers/dossiers de notre projet

Nous utiliserons une stratégie de développement modulaire pour séparer le déploiement de notre cluster Jenkins en plusieurs fichiers de modèle (plutôt que de développer un seul grand fichier de modèle).

Chaque fichier est responsable de l'exécution d'un composant d'infrastructure cible ou d'une ressource AWS.

Pour créer et appliquer les paramètres d'infrastructure, Terraform utilise la syntaxe d'un langage de configuration similaire à JSON appelé HCL (HashiCorp Configuration Language).

![structure des fichiers/dossiers](https://www.freecodecamp.org/news/content/images/2022/07/structure.PNG)
_structure des fichiers/dossiers_

## Comment initialiser l'état de Terraform pour la première fois

Pour suivre les meilleures pratiques, nous stockerons nos fichiers d'état Terraform dans notre stockage cloud. Cela est essentiel, surtout pour la collaboration en équipe.

Les fichiers d'état Terraform sont des fichiers qui contiennent les ressources Terraform des projets.

À l'intérieur du fichier main.tf dans le dossier backend-state, ajoutez le code suivant :

```json
variable "aws_region" { 
	default = "us-east-1" 
} 
variable "aws_secret_key" {} 
variable "aws_access_key" {} 

provider "aws" { 
	region = var.aws_region 
    access_key = var.aws_access_key 
    secret_key = var.aws_secret_key 
} 

resource "aws_s3_bucket" "terraform_state" { 
	bucket = "terraform-state-caesar-tutorial-jenkins" 
    
    lifecycle { 
    	prevent_destroy = true 
    } 
    
    versioning { 
    	enabled = true 
   } 
   
   server_side_encryption_configuration { 
   		rule { 
        	apply_server_side_encryption_by_default { 
            	sse_algorithm = "AES256" 
            } 
        } 
   } 
}
```

Assurons-nous de savoir ce qui se passe dans le code ci-dessus.

Nous utilisons des **variables** pour stocker des données, et dans Terraform, vous déclarez une variable avec le mot-clé variable suivi du nom. Le bloc variable peut prendre certaines propriétés telles que default, description, type, etc., ou aucune. Vous verrez cela souvent.

Maintenant, nous déclarons les variables comme `variable "variable_name"{}` et **les utilisons dans n'importe quel bloc de ressources/données comme** `var.variable_name`. Plus tard, vous verrez comment nous attribuerons des valeurs à ces variables dans notre fichier secrets.tfvars.

Pour utiliser Terraform, vous devez lui indiquer le **fournisseur** avec lequel il communiquera et passer ses propriétés requises pour l'authentification. Ici, nous avons la région AWS, l'accès et la clé secrète (vous devriez avoir téléchargé ceux-ci sur votre système à partir des prérequis).

Dans Terraform, chaque **ressource** dont nous avons besoin est définie dans le bloc de ressources. Les ressources sont l'infrastructure sous-jacente qui crée notre service cloud. Il suit la syntaxe `resource "terraform-resource-name" "custom-name" {}`.

Terraform a beaucoup de ressources pour des fournisseurs particuliers dans la documentation Terraform (référez-vous toujours à la documentation si vous avez des questions).

Ensuite, nous créons le aws_s3_bucket. Cela stockera notre état distant. Il prend les propriétés suivantes :

* **bucket** → Cela doit être globalement unique
* **lifecycle** → Si vous devez détruire vos ressources Terraform, vous pourriez vouloir empêcher la destruction de l'état car il est partagé entre les équipes
* **versioning** → Aide à fournir un certain contrôle de version sur les états
* **server_side_encryption_configuration** → Fournit un chiffrement.

Notre backend d'état est prêt. Mais avant de l'initialiser, de le planifier et de l'appliquer avec Terraform, **attribuons nos variables à leurs valeurs**.

Dans secrets.tfvars, ajoutez les informations suivantes de votre compte AWS :

```json
  aws_region = "us-east-1"
  aws_secret_key = "enter-your-secret"
  aws_access_key = "enter-your-access"
```

Dans votre terminal, dans le même dossier backend-state, exécutez `terraform init`.

![terraform state on terminal](https://paper-attachments.dropbox.com/s_0475B692F95FDEC0A6E8498B95C86079E0E8D8D5196F9F4DEAA5AA6D3B79CB44_1655827434318_terminal-state-1.PNG)
_terraform state on terminal_

Ensuite, `terraform apply -var-file=secrets.tfvars` :

![terraform state on terminal](https://paper-attachments.dropbox.com/s_0475B692F95FDEC0A6E8498B95C86079E0E8D8D5196F9F4DEAA5AA6D3B79CB44_1655827520492_terminal-state-2.PNG)
_terraform state on terminal_

Dans votre **console AWS**, voici ce que vous verrez :

![terraform state on aws s3 bucket](https://paper-attachments.dropbox.com/s_0475B692F95FDEC0A6E8498B95C86079E0E8D8D5196F9F4DEAA5AA6D3B79CB44_1655827945123_aws-console.PNG)
_terraform state on aws s3 bucket_

Maintenant que notre état est prêt, passons à la partie suivante.

## Comment approvisionner un cloud privé virtuel AWS

Pour sécuriser notre cluster Jenkins, nous allons déployer l'architecture au sein d'un cloud privé virtuel (VPC) et d'un sous-réseau privé. Vous pouvez déployer le cluster dans le VPC par défaut d'AWS.

Pour avoir un contrôle complet sur la topologie du réseau, nous allons créer un VPC à partir de zéro.

```json
 variable "cidr_block" {} 
 variable "aws_access_key" {} 
 variable "aws_secret_key" {} 
 variable "aws_region" {} 
 
 provider "aws" { 
 	region = var.aws_region 
    access_key = var.aws_access_key 
    secret_key = var.aws_secret_key 
} 

terraform { 
	backend "s3" { 
    	bucket     = "terraform-state-caesar-tutorial-jenkins" 
        key        = "tutorial-jenkins/development/network/terraform.tfstate" 
        region     = "us-east-1" 
        encrypt    = true 
   }
} 

resource "aws_vpc" "main_vpc" { 
	cidr_block           = var.cidr_block 
    enable_dns_support   = true 
    enable_dns_hostnames = true 
    
    tags = { 
    	Name        = "jenkins-instance-main_vpc" 
    } 
}
```

```json
output "vpc_id" { 
	value = aws_vpc.main_vpc.id 
} 

output "vpc_cidr_block" { 
	value = aws_vpc.main_vpc.cidr_block 
}  
```

```json
cidr_block            = "172.0.0.0/16" 
aws_region = "us-east-1" 
aws_secret_key = "enter-your-secret" 
aws_access_key = "enter-your-access"
```

* **cidr_block →** Le routage inter-domaine sans classe est appelé CIDR. Un bloc CIDR est une plage d'adresses IP, pour faire simple. Cela définit la plage dans laquelle nous travaillons.
* **output →** Le bloc de sortie dans Terraform est utilisé pour exporter les valeurs des ressources vers d'autres modules. C'est un autre terme important lors du transfert de données de ressources dans un module vers une autre ressource dans un module séparé. (Vous apprendrez ce que sont les modules bientôt) Voici sa syntaxe : `output "custom_output_name" {  value = "resource-name"}`. Il prend une **valeur** qui prend la ressource passée. Ici, nous sortons vpc_id et cidr_block.

Maintenant, dans le terminal, exécutez `terraform init` et `terraform apply` pour créer les ressources. Vous pouvez exécuter `terraform plan` avant pour voir quelles ressources vous créez réellement. Voici la commande : `terraform apply -var-file=secrets.tfvars`, et la sortie :

![Image](https://paper-attachments.dropbox.com/s_0475B692F95FDEC0A6E8498B95C86079E0E8D8D5196F9F4DEAA5AA6D3B79CB44_1655907973370_vpc.PNG)

Vous devriez voir votre **vpc_id et vpc_cidr_block** dans votre **console AWS** :

![vpc resource on aws](https://paper-attachments.dropbox.com/s_0475B692F95FDEC0A6E8498B95C86079E0E8D8D5196F9F4DEAA5AA6D3B79CB44_1656907111688_vpc-aws.PNG)
_vpc on aws_

Maintenant que notre état est prêt, passons à la partie suivante.

## Comment travailler avec les modules Terraform

Un groupe de fichiers de configuration typiques dans un répertoire spécifique constitue un module Terraform. Les modules Terraform rassemblent des ressources utilisées pour une seule opération. Cela réduit la quantité de code dont vous avez besoin pour créer des composants d'infrastructure identiques.

En utilisant la syntaxe ci-dessous, vous pouvez transférer une ressource de module Terraform à une autre pour être utilisée.

```json
module "custom-module-name" { 
	source     = "path-to-modules-resources" 
}
```

Et pour utiliser la sortie de la ressource du module à l'intérieur d'une autre ressource du module, voici la commande : `module.custom-module-name.resource-output-value`.

## Comment créer un sous-réseau VPC

Créer un VPC n'est pas suffisant – nous avons également besoin d'un sous-réseau pour pouvoir installer des instances Jenkins sur ce réseau isolé. Nous devons passer l'ID VPC que nous avons sorti auparavant, puisque ce sous-réseau appartient à un VPC précédemment construit.

Pour la résilience, nous utiliserons deux sous-réseaux publics et deux sous-réseaux privés dans des zones de disponibilité distinctes. Chaque sous-réseau a son propre bloc CIDR, qui est un sous-ensemble du bloc CIDR VPC, que nous avons obtenu de la ressource VPC.

```json
resource "aws_subnet" "public_subnets" { 
	vpc_id         = var.vpc_id 
    cidr_block     = cidrsubnet(var.vpc_cidr_block, 8, 2 + count.index)  
   	availability_zone   = element(var.availability_zones, count.index)  	
    map_public_ip_on_launch = true 
    count                   = var.public_subnets_count 
    
    tags = { 
    	Name        = "jenkins-instance-public-subnet" 
   } 
} 

resource "aws_subnet" "private_subnets" { 
	vpc_id     = var.vpc_id 
    cidr_block = cidrsubnet(var.vpc_cidr_block, 8, count.index)  			
    availability_zone    = element(var.availability_zones, count.index)  
    map_public_ip_on_launch = false 
    count                   = var.private_subnets_count 
    
    tags = { 
    	Name        = "jenkins-instance-private-subnet" 
    } 
 }
```

D'accord, que se passe-t-il dans ce code ?

* [**count**](https://www.terraform.io/language/meta-arguments/count) **→** L'argument méta count accepte un nombre entier, et crée autant d'instances de la ressource ou du module. Ici, nous spécifions 2 chacun pour les variables private_subnets_count et public_subnets_count.
* **map_public_ip_on_launch →** Spécifiez true pour indiquer que les instances lancées dans le sous-réseau doivent se voir attribuer une adresse IP publique.
* [**cidrsubnet()**](https://www.terraform.io/language/functions/cidrsubnet) **→** cidrsubnet calcule une adresse de sous-réseau dans un préfixe d'adresse de réseau IP donné.
* [**element()**](https://www.terraform.io/language/functions/element) **→** element récupère un seul élément d'une liste.

Maintenant, mettons à jour nos variables de modules :

```json
variable "vpc_id" {} 
variable "vpc_cidr_block" {} 
variable "private_subnets_count" {} 
variable "public_subnets_count" {} 
variable "availability_zones" {} 
```

Mettez à jour le fichier secrets.tfvars comme ceci :

```json
private_subnets_count = 2 
public_subnets_count  = 2
```

Vous devez établir des tables de routage privées et publiques pour spécifier la méthode de routage du trafic dans les sous-réseaux VPC. Faisons cela avant d'exécuter **terraform apply** sur nos ressources.

## Comment configurer les tables de routage VPC

Nous développerons des tables de routage privées et publiques pour une gestion fine du trafic. Cela permettra aux instances déployées dans les sous-réseaux privés d'accéder à Internet sans être exposées au grand public.

### Comment créer une table de routage publique

Tout d'abord, nous devons établir une **ressource de passerelle Internet** et la lier au VPC que nous avons généré précédemment. Ensuite, nous devons définir une **table de routage publique** et une route qui pointe tout le trafic (0.0.0.0/0) vers la passerelle Internet. Et enfin, nous devons la lier avec les sous-réseaux publics dans notre VPC afin que le trafic provenant de ces sous-réseaux soit routé vers la passerelle Internet en créant une **association de table de routage**.

```json
/*** Internet Gateway - Fournit une connexion entre le VPC et l'internet public, permettant au trafic d'entrer et de sortir du VPC et de traduire les adresses IP en adresses publiques.*/ 
resource "aws_internet_gateway" "igw" { 
	vpc_id = var.vpc_id 
    
    tags = { 
    	Name = "igw_jenkins" 
   } 
} 

/*** Une route de la table de routage publique vers l'internet via la passerelle internet.*/ 
resource "aws_route_table" "public_rt" { 
	vpc_id = var.vpc_id 
    
    route { 
    	cidr_block = "0.0.0.0/0" 
        gateway_id = aws_internet_gateway.igw.id 
   } 
   
   tags = { 
   		Name = "public_rt_jenkins" 
   } 
} 
/*** Associer la table de routage publique aux sous-réseaux publics.*/ 
resource "aws_route_table_association" "public" { 
	count     = var.public_subnets_count 
    subnet_id = element(var.public_subnets.*.id, count.index) 
    route_table_id = aws_route_table.public_rt.id 
}
```

### Comment créer une table de routage privée

Maintenant que notre table de routage publique est terminée, créons la table de routage privée.

Pour permettre à nos instances Jenkins de se connecter à Internet car elles sont déployées sur le sous-réseau privé, nous allons construire une **ressource de passerelle NAT** à l'intérieur d'un sous-réseau public.

Ajoutez une **adresse IP élastique** à la passerelle NAT après cela et une table de routage privée avec une route (0.0.0.0/0) qui dirige tout le trafic vers l'ID de la passerelle NAT que vous avez établie. Ensuite, nous attachons les sous-réseaux privés à la table de routage privée en créant l'**association de table de routage**.

```json
 /*** Une adresse IP élastique à utiliser par la passerelle NAT définie ci-dessous.  La passerelle NAT agit comme une passerelle entre nos sous-réseaux privés et l'internet public, fournissant un accès à l'internet depuis ces sous-réseaux, tout en refusant l'accès à ceux-ci depuis l'internet public.  Cette adresse IP agit comme l'adresse IP à partir de laquelle tout le trafic sortant des sous-réseaux privés prendra son origine.*/ 
 
 resource "aws_eip" "eip_for_the_nat_gateway" { 
 	vpc = true 
    
    tags = { 
    	Name = "jenkins-tutoral-eip_for_the_nat_gateway" 
    } 
} 

/*** Une passerelle NAT qui réside dans notre sous-réseau public et fournit une interface entre nos sous-réseaux privés et l'internet public.  Elle permet au trafic de sortir de nos sous-réseaux privés, mais empêche le trafic d'y entrer.*/ 

resource "aws_nat_gateway" "nat_gateway" { 
	allocation_id = aws_eip.eip_for_the_nat_gateway.id 
    subnet_id     = element(var.public_subnets.*.id, 0) 
    
    tags = { 
    	Name = "jenkins-tutorial-nat_gateway" 
	} 
} 
/*** Une route de la table de routage privée vers l'internet via la passerelle NAT.*/ 

resource "aws_route_table" "private_rt" { 
	vpc_id = var.vpc_id 
    
    route { 
    	cidr_block     = "0.0.0.0/0" 
        nat_gateway_id = aws_nat_gateway.nat_gateway.id } 
        
        tags = { 
        	Name   = "private_rt_${var.vpc_name}" 
            Author = var.author 
        } 
} 
/*** Associer la table de routage privée au sous-réseau privé.*/ 
resource "aws_route_table_association" "private" { 
	count = var.private_subnets_count 
    subnet_id = element(aws_subnet.private_subnets.*.id, count.index) 
    route_table_id = aws_route_table.private_rt.id 
}
```

Maintenant, exécutons `terraform apply`. Mais nous devons **mettre à jour nos fichiers main.tf** (car c'est notre fichier terraform d'entrée) pour qu'ils soient conscients de nos sous-réseaux et des variables de module et **secrets.tfvars** (pour nos variables).

```json
variable "vpc_id" {} 
variable "vpc_cidr_block" {} 
variable "private_subnets_count" {} 
variable "public_subnets_count" {} 
variable "availability_zones" {} 
variable "public_subnets" {}
```

```json
variable "private_subnets_count" {} 
variable "public_subnets_count" {} 
variable "availability_zones" {} 

module "subnet_module" { 
	source     = "./modules" 
    vpc_id     = aws_vpc.main_vpc.id 
    vpc_cidr_block = aws_vpc.main_vpc.cidr_block 
    availability_zones = var.availability_zones 
    public_subnets_count = var.public_subnets_count 
    private_subnets_count = var.private_subnets_count 
 }
```

```json
 availability_zones    = ["us-east-1a", "us-east-1b", "us-east-1c", "us-east-1d", "us-east-1e"]
```

Nos sous-réseaux et leurs sécurités respectives sont prêts. Maintenant, nous pouvons l'initialiser, le planifier et l'appliquer avec Terraform.

Nous allons exécuter **terraform apply** pour créer les ressources. Vous pouvez exécuter terraform plan avant pour voir quelles ressources vous créez réellement.

Dans le terminal, exécutez `terraform apply -var-file=secrets.tfvars`.

![Image](https://paper-attachments.dropbox.com/s_0475B692F95FDEC0A6E8498B95C86079E0E8D8D5196F9F4DEAA5AA6D3B79CB44_1656906570979_terminal-state-3.PNG)

Gardez simplement à l'esprit que le nombre de ressources ajoutées ici peut différer du vôtre.

Voici la console AWS (sous-réseaux, adresse élastique, route_tables) :

![subnets](https://paper-attachments.dropbox.com/s_0475B692F95FDEC0A6E8498B95C86079E0E8D8D5196F9F4DEAA5AA6D3B79CB44_1656907223081_image.png)
_subnets_

![elastic ip](https://paper-attachments.dropbox.com/s_0475B692F95FDEC0A6E8498B95C86079E0E8D8D5196F9F4DEAA5AA6D3B79CB44_1656907210658_elastic-ip.PNG)
_elastic ip_

![route tables](https://paper-attachments.dropbox.com/s_0475B692F95FDEC0A6E8498B95C86079E0E8D8D5196F9F4DEAA5AA6D3B79CB44_1656907210672_rt.PNG)
_route tables_

## Comment configurer un hôte bastion VPC

Nous avons déployé notre cluster Jenkins à l'intérieur des sous-réseaux privés. Comme le cluster n'a pas d'IP publique, les instances ne seront pas accessibles publiquement via Internet. Pour remédier à cela, nous allons configurer un hôte bastion afin que nous puissions accéder aux instances Jenkins en toute sécurité.

Ajoutez les ressources suivantes et le groupe de sécurité dans le fichier bastion.tf :

```json
/*** Un groupe de sécurité pour permettre l'accès SSH à notre instance bastion.*/ 
resource "aws_security_group" "bastion" { 
	name   = "bastion-security-group" 
    vpc_id = var.vpc_id 
    
    ingress { 
    	protocol    = "tcp" 
        from_port   = 22 
        to_port     = 22 
        cidr_blocks = ["0.0.0.0/0"] 
    } 
    egress { 
    	protocol    = -1 
        from_port   = 0 
        to_port     = 0 
        cidr_blocks = ["0.0.0.0/0"] 
   } 
   
   tags = { 
   		Name = "aws_security_group.bastion_jenkins" 
   } 
} 

/*** La clé publique pour la paire de clés que nous utiliserons pour nous connecter en SSH à notre instance bastion.*/ 

resource "aws_key_pair" "bastion" { 
	key_name   = "bastion-key-jenkins" 
    public_key = var.public_key 
 } 
 
 /*** Ce paramètre contient l'ID AMI pour l'AMI Amazon Linux 2 la plus récente, gérée par AWS.*/ 
 
 data "aws_ssm_parameter" "linux2_ami" { 
 	name = "/aws/service/ami-amazon-linux-latest/amzn-ami-hvm-x86_64-ebs" 
} 

/*** Lancer une instance bastion que nous pouvons utiliser pour accéder aux sous-réseaux privés de cette zone de disponibilité.*/ 

resource "aws_instance" "bastion" { 
	ami           = data.aws_ssm_parameter.linux2_ami.value 
    key_name      = aws_key_pair.bastion.key_name 
    instance_type = "t2.large" 
    associate_public_ip_address = true 
    subnet_id                   = element(aws_subnet.public_subnets, 0).id 
    vpc_security_group_ids      = [aws_security_group.bastion.id] 
    
    tags = { 
    	Name        = "jenkins-bastion" 
    } 
} 

output "bastion" { value = aws_instance.bastion.public_ip }
```

Voyons ce qui se passe dans le code ici :

* **ressource de groupe de sécurité bastion** – Les nouvelles instances EC2 générées ne permettent pas l'accès SSH.
* Nous lierons un groupe de sécurité à l'instance active afin de permettre l'accès SSH aux hôtes bastion. Le groupe de sécurité permettra tout trafic entrant (ingress) sur le port 22 (SSH) de n'importe où (0.0.0.0/0). Pour améliorer la sécurité et prévenir les violations de sécurité, vous pouvez substituer votre propre adresse IP publique/32 ou adresse réseau pour le bloc source CIDR.
* **aws_key_pair** – Pour pouvoir se connecter à l'hôte bastion en utilisant SSH et la clé privée, nous avons ajouté une paire de clés SSH lors de la création de l'EC2. Notre clé SSH publique est utilisée dans la paire de clés. Vous pouvez également en créer une nouvelle en utilisant la commande **sshkeygen**.
* **aws_ssm_parameter** – L'image de la machine Amazon 2 Linux est utilisée par l'instance EC2. L'ID AMI est obtenu à partir du marketplace AWS en utilisant la source de données AMI AWS
* **aws_instance** – Enfin, nous déployons notre instance bastion EC2 avec ses configurations définies et son accès
* **output** – En spécifiant une sortie, nous utilisons la fonctionnalité de sorties Terraform pour afficher l'adresse IP dans la session de terminal.

Maintenant, mettons à jour notre variable dans les modules et le main.tf avec la nouvelle **public_key** que nous passons en tant que variable :

```json
variable "public_key"{} 
```

```json
varable "public_key" {} 
module "subnet_module" { 
	source     = "./modules" 
    ... 
    publc_key = var.public_key 
}
```

```json
public_key = "enter-your-public-key"
```

Nous allons exécuter **terraform apply** pour créer les ressources. Vous pouvez exécuter terraform plan avant pour voir quelles ressources vous créez réellement.

Dans le terminal, exécutons `terraform apply -var-file=secrets.tfvars` :

![terminal resources](https://paper-attachments.dropbox.com/s_0475B692F95FDEC0A6E8498B95C86079E0E8D8D5196F9F4DEAA5AA6D3B79CB44_1656907792871_terminal-state-4.PNG)
_terminal resources_

Voici la sortie dans la console AWS :

![aws-console instances](https://paper-attachments.dropbox.com/s_0475B692F95FDEC0A6E8498B95C86079E0E8D8D5196F9F4DEAA5AA6D3B79CB44_1656907897195_bastion.PNG)
_aws-console instances_

## Comment approvisionner notre service de calcul

### Instance maître Jenkins

Jusqu'à présent, nous avons réussi à configurer notre VPC et la topologie du réseau. Enfin, nous allons créer notre instance EC2 Jenkins qui utilisera une AMI maître Jenkins cuite par Packer.

Vous pouvez consulter mon article précédent sur la façon dont elle a été cuite : [Apprendre l'infrastructure en tant que code en construisant une image machine personnalisée dans AWS sur freecodecamp.org](https://www.freecodecamp.org/news/learn-instructure-as-a-code-by-building-custom-machine-image-in-aws/). Quoi qu'il en soit, vous pouvez utiliser l'une de vos images personnalisées si vous en avez une.

```json
 /*** Ce paramètre contient notre ID AMI cuite récupérée de la console Amazon*/ data "aws_ami" "jenkins-master" { 
 	most_recent = true owners      = ["self"] 
} 

resource "aws_security_group" "jenkins_master_sg" { 
	name        = "jenkins_master_sg" 
    description = "Autoriser le trafic sur le port 8080 et activer SSH" 
    vpc_id      = var.vpc_id 
    
    ingress { 
    	from_port       = "22" 
        to_port         = "22" 
        protocol        = "tcp" 
        security_groups = [aws_security_group.bastion.id] 
   } 
   ingress { 
   		from_port       = "8080" 
        to_port         = "8080" 
        protocol        = "tcp" 
        security_groups = [aws_security_group.lb.id] 
   } 
   ingress { 
   		from_port   = "8080" 
        to_port     = "8080" 
        protocol    = "tcp" 
        cidr_blocks = ["0.0.0.0/0"] 
  } 
  egress { 
  		from_port   = "0" 
        to_port     = "0" 
        protocol    = "-1" 
        cidr_blocks = ["0.0.0.0/0"] 
  } 
  
  tags = { 
  	Name = "jenkins_master_sg" 
  }
} 
```

L'attachement d'un groupe de sécurité à l'instance permettra le trafic entrant sur le port 8080 (le tableau de bord web Jenkins) et SSH uniquement depuis le serveur bastion et le bloc CIDR VPC.

```json
resource "aws_key_pair" "jenkins" { 
	key_name   = "key-jenkins" 
    public_key = var.public_key 
} 

resource "aws_instance" "jenkins_master" { 
	ami       = data.aws_ami.jenkins-master.id 
    instance_type  = "t2.large" 
    key_name       = aws_key_pair.jenkins.key_name 
    vpc_security_group_ids = [aws_security_group.jenkins_master_sg.id]
    subnet_id              = element(aws_subnet.private_subnets, 0).id
    root_block_device { 
    	volume_type           = "gp3" 
        volume_size           = 30 
        delete_on_termination = false 
    } 
    
    tags = { 
    	Name = "jenkins_master" 
     } 
 }
```

Ensuite, nous créons une variable et définissons le type d'instance que nous avons utilisé pour déployer l'instance EC2. Nous n'allouerons pas d'exécuteurs ou de workers sur le maître, donc t2.large (8 Go de mémoire et 2 vCPU) devrait être adéquat pour des raisons de simplicité.

Ainsi, les travaux de construction ne feront pas surcharger le maître Jenkins. Mais les exigences de mémoire de Jenkins varient en fonction des besoins de construction de votre projet et des outils utilisés dans ces constructions. Il nécessitera deux à trois threads, ou au moins 2 Mo de mémoire, pour se connecter à chaque nœud de construction.

Juste une note : envisagez d'installer des workers Jenkins pour éviter de surcharger le maître. Par conséquent, une instance à usage général peut héberger un maître Jenkins et offrir un équilibre entre les ressources de calcul et de mémoire. Afin de maintenir la simplicité de l'article, nous ne ferons pas cela.

## Comment créer le Load Balancer

Pour accéder au tableau de bord Jenkins, nous allons créer un load balancer public devant l'instance EC2.

Ce load balancer élastique acceptera le trafic HTTP sur le port 80 et le transférera à l'instance EC2 sur le port 8080. De plus, il vérifie automatiquement l'état de santé de l'instance EC2 enregistrée sur le port 8080. Si l'Elastic Load Balancing (ELB) trouve l'instance non saine, il arrête d'envoyer du trafic à l'instance Jenkins.

```json
 /*** Un groupe de sécurité pour permettre l'accès SSH à notre load balancer*/ resource "aws_security_group" "lb" { 
 	name   = "ecs-alb-security-group" 
    vpc_id = var.vpc_id 
    
    ingress { 
    	protocol    = "tcp" 
        from_port   = 80 
        to_port     = 80 
        cidr_blocks = ["0.0.0.0/0"] 
     } 
     egress { 
     	from_port   = 0 
        to_port     = 0 
        protocol    = "-1" 
        cidr_blocks = ["0.0.0.0/0"] 
     } 
     
     tags = { 
     	Name = "jenkins-lb-sg" 
      } 
 } 
 
 /***Load Balancer à attacher au cluster ECS pour distribuer la charge parmi les instances*/ 
 
 resource "aws_elb" "jenkins_elb" { 
 	subnets    = [for subnet in aws_subnet.public_subnets : subnet.id]
    cross_zone_load_balancing = true 
    security_groups       = [aws_security_group.lb.id] 
    instances             = [aws_instance.jenkins_master.id] 
    
    listener { 
    	instance_port     = 8080 
        instance_protocol = "http" 
        lb_port           = 80 
        lb_protocol       = "http" 
     } 
     
     health_check { 
     	healthy_threshold   = 2 
        unhealthy_threshold = 2 
        timeout             = 3 
        target              = "TCP:8080"    
        interval            = 5 
    } 
    
    tags = { 
    	Name = "jenkins_elb" 
    } 
 } 
 
 output "load-balancer-ip" { 
 	value = aws_elb.jenkins_elb.dns_name 
 }
```

Avant de faire notre terraform apply, mettons à jour notre dossier development/output.tf pour sortir le DNS du load balancer :

```json
 output "load-balancer-ip" { 
 	value = module.subnet_module.load-balancer-ip
 }
```

Dans le terminal, exécutez la commande suivante : `terraform apply -var-file="secrets.tfvars"`. Ce qui vous donnera ceci :

![load balancer output](https://paper-attachments.dropbox.com/s_0475B692F95FDEC0A6E8498B95C86079E0E8D8D5196F9F4DEAA5AA6D3B79CB44_1657669467370_load-balancer.PNG)
_load balancer output_

Après avoir appliqué les modifications avec Terraform, l'URL du load balancer maître Jenkins devrait s'afficher dans votre session de terminal.

Pointez votre navigateur préféré vers l'URL, et vous devriez avoir accès au tableau de bord web Jenkins.

![jenkins-instances](https://paper-attachments.dropbox.com/s_0475B692F95FDEC0A6E8498B95C86079E0E8D8D5196F9F4DEAA5AA6D3B79CB44_1657669441393_jenkns.PNG)
_jenkins-instances_

Ensuite, suivez simplement les instructions à l'écran pour DÉVERROUILLER.

![unlock jenkins](https://www.freecodecamp.org/news/content/images/2022/07/screencapture-ec2-3-87-146-72-compute-1-amazonaws-8080-2022-05-25-05_38_35-1.png)
_unlock jenkins_

Vous pouvez trouver le [code complet dans ce dépôt GitHub.](https://github.com/Caesarsage/terraform-jenkins-instance)

## Nettoyage

Pour éviter les coûts inutiles d'exécution des services AWS, vous devrez exécuter la commande suivante pour détruire toutes les ressources créées et en cours d'exécution : `terraform destroy -var-file="secrets.tfvars"` ce qui devrait donner cette sortie :

![destroy resources](https://paper-attachments.dropbox.com/s_0475B692F95FDEC0A6E8498B95C86079E0E8D8D5196F9F4DEAA5AA6D3B79CB44_1657669741091_destroy.PNG)
_destroy resources_

Comment c'est intéressant, n'est-ce pas ? Avec seulement quelques lignes de code, nous pouvons détruire et lancer nos ressources.

## Résumé

Dans ce tutoriel, vous avez appris comment utiliser Terraform à un niveau élevé. Vous avez également appris l'une de ses applications en approvisionnant un serveur Jenkins sur la plateforme cloud AWS.

Vous avez également appris les meilleures pratiques des états backend Terraform et des modules.

Pour en savoir plus sur Terraform et ses nombreux cas d'utilisation, vous pouvez consulter la documentation officielle [Terraform docs ici](https://registry.terraform.io/providers/hashicorp/aws/latest/docs).

Bon apprentissage !