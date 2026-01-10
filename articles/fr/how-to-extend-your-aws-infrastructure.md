---
title: Comment étendre votre infrastructure AWS avec Direct Connect en utilisant Terraform
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-27T21:36:32.000Z'
originalURL: https://freecodecamp.org/news/how-to-extend-your-aws-infrastructure
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/transit-vac-router-service-3-3.png
tags:
- name: AWS
  slug: aws
- name: Network Engineering
  slug: network-engineering
seo_title: Comment étendre votre infrastructure AWS avec Direct Connect en utilisant
  Terraform
seo_desc: "By Serhii Povisenko\nSometimes, when you face a challenge, you might be\
  \ able to solve it with routine processes. But other times you need to try something\
  \ completely new, something that you know nothing about. \nUsually in these scenarios\
  \ you should ap..."
---

Par Serhii Povisenko

Parfois, lorsque vous êtes confronté à un défi, vous pouvez le résoudre avec des processus de routine. Mais d'autres fois, vous devez essayer quelque chose de complètement nouveau, quelque chose que vous ne connaissez pas. 

Habituellement, dans ces scénarios, vous devriez appliquer une pensée d'ingénierie. Pour moi, ces moments sont les plus instructifs et je veux partager certains des miens avec la communauté.

Ici, je vais vous guider à travers les étapes que mon équipe et moi avons suivies lorsque nous avons connecté une infrastructure AWS existante à un grand réseau privé en utilisant [Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/WorkingWithConnections.html). 

En cours de route, je fournirai des [extraits de code Terraform](https://github.com/povisenko/terraform-aws-direct-connect) qui vous montreront comment implémenter tous ces composants en tant qu'"[infrastructure as code](https://en.wikipedia.org/wiki/Infrastructure_as_code)" avec des schémas de conception accompagnateurs.

## Ce que nous allons couvrir

1. Problèmes à résoudre
2. Qu'est-ce que Direct Connect ?
3. Comment l'intégrer
4. Transit VPC utilisant Terraform
5. Direct Connect utilisant Terraform 
6. Appairage entre les VPC principaux et de transit
7. Utilisez-vous OpenVPN (optionnel) ?
8. Service de routage
9. Réflexions finales

## Problèmes à résoudre

Nous avions des services dans notre [VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) qui devaient pouvoir communiquer avec d'autres services dans un réseau privé virtuel séparé.

Pour établir la connexion, nous devions accepter une connexion hébergée par AWS d'un fournisseur de réseau dans le cadre d'un contrat signé pour accorder l'accès au VPN en utilisant AWS Direct Connect.

Alors, comment devions-nous implémenter tout cela ? Comment allions-nous l'intégrer à une solution actuelle gérée avec Terraform ? Y avait-il des meilleures pratiques pour le faire ?

## Qu'est-ce que Direct Connect ?

> AWS Direct Connect facilite l'établissement d'une connexion réseau dédiée depuis vos locaux vers votre Amazon VPC ou entre les Amazon VPC. Cette option peut potentiellement réduire les coûts réseau, augmenter le débit de la bande passante et fournir une expérience réseau plus cohérente que les autres options de connectivité VPC à VPC. ([source](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect-network-to-amazon.html))

Essentiellement, vous avez un fournisseur de réseau qui dispose d'installations AWS dans un centre de données partagé. Ensuite, vous pouvez tous deux établir une connexion directe entre vos composants réseau AWS et le réseau en utilisant le matériel du fournisseur (littéralement un câble de brassage dans le nid) avec un accès ultérieur.

L'implémentation générique en termes d'AWS ressemble à ce qui suit :

* Vous configurez une ou deux (réservées) connexions Direct Connect dans la console, ce qui crée une passerelle Direct Connect. 
* Ensuite, vous attachez une VIF privée (une par connexion) à la passerelle. 
* Une fois que vous avez passé quelques appels avec les ingénieurs réseau du fournisseur et échangé des politiques de routage, c'est fait. 

Habituellement, toutes les instructions concernant l'activation de la connexion vous seront envoyées par le fournisseur.

## Comment l'intégrer

Notre première hypothèse était que nous activerions la connexion dans le VPC et créerions la configuration de routage pour diriger la passerelle de connexion directe pour les requêtes nécessaires (par exemple, nous les distinguerions par l'en-tête "Host" ou par les IP). 

À haut niveau, cela ressemblerait à quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/aws-direct-connect.png)
_AWS Direct Connect_

Lors d'un appel avec les ingénieurs réseau du fournisseur, ils nous ont demandé notre plage d'IP que nous avons annoncée au réseau. Nous nous sommes demandé pourquoi. C'était parce que le travail de Direct Connect est déclaré par un protocole appelé [BGP](https://fr.wikipedia.org/wiki/Border_Gateway_Protocol). Si vous voulez plus d'informations, il existe de nombreuses vidéos qui vous enseigneront l'un des principaux protocoles Internet qui fonctionnent sous le capot. 

Notre première pensée était qu'il devait s'agir d'un sous-réseau contenant des services auxquels nous voulions accéder au réseau. Après cela, on nous a demandé de configurer le sous-réseau `10.1.2.0/24` comme un [préfixe autorisé](https://docs.aws.amazon.com/directconnect/latest/UserGuide/allowed-to-prefixes.html) dans notre configuration Direct Connect. 

En bref, les "préfixes autorisés" ici représentent une plage d'IP que nous allions annoncer au fournisseur de réseau, qui l'enregistrerait dans les politiques de routage. 
  
Eh bien, après tout cela, cela n'a pas fonctionné. Le fournisseur ne "voyait" pas nos routes annoncées malgré le fait que nous pouvions les voir. 

Un peu d'[investigation et voilà](https://aws.amazon.com/directconnect/faqs/#V1,):

> AWS allouera des IP privées (/30) dans la plage 169.x.x.x pour la session BGP et annoncera le bloc CIDR VPC via BGP. Vous pouvez annoncer la route par défaut via BGP.

De plus, nous avons trouvé [d'autres personnes](https://forums.aws.amazon.com/thread.jspa?threadID=130577) qui semblaient confrontées au même problème :

> nous avons fini par créer un nouveau VPC avec un CIDR plus petit que notre partenaire voulait.

Donc, en gros, la plage d'IP que vous pouvez annoncer via Direct Connect est limitée à `/30`. De plus, vous ne pouvez pas annoncer de sous-réseaux – plutôt, vous devriez annoncer le CIDR VPC entier. 

Notre CIDR réseau était `10.1.0.0/16` et nous avions un problème avec cela - _il était trop grand pour être accepté par le fournisseur de réseau_. En plus de cela, lors de l'appel, nous avons découvert une autre chose que nous devions faire lors de la connexion au réseau : _nous devions contacter le département de gestion de l'accès IP du réseau (si le réseau était suffisamment grand, je suppose) pour leur demander de nous fournir une plage unique au sein du réseau. Par la suite, cela devrait être notre nouveau CIDR VPC._

Nous avons décidé de créer un VPC séparé. Pour obtenir quelques preuves de travail, nous avons trouvé quelques guides officiels d'AWS tels que [celui-ci](https://docs.aws.amazon.com/solutions/latest/cisco-based-transit-vpc/appendix-d.html). Peu de temps après cela, nous avons appris que la communauté AWS commencerait à utiliser des mots séparés pour ce VPC séparé - ils l'appelleraient un **transit VPC.**

![Image](https://www.freecodecamp.org/news/content/images/2020/05/integration-with-direct-connect.png)
_**Direct Connect utilisant transit VPC**_

Avant de recevoir une réponse à une demande de plage d'IP unique dans le réseau, nous avons demandé au fournisseur les plages d'IP actuellement inutilisées afin de pouvoir l'implémenter rapidement de notre côté. Cela nous donnerait la preuve de travail dont nous avions besoin pour une solution. Tout a fonctionné parfaitement. 

L'étape suivante était d'implémenter tout (configurations Direct Connect + appairage VPC) dans notre configuration Terraform existante. 

## Transit VPC utilisant Terraform

Tout d'abord, avant de commencer à creuser dans le code, je veux dire que vous pouvez trouver tout le code ci-dessous sur GitHub [ici](https://github.com/povisenko/terraform-aws-direct-connect).

Récapitulons d'abord ce que nous avons discuté. Nous avons des conditions où nous avions un VPC existant. Et nous voulions que certains services au sein de celui-ci puissent communiquer via le réseau auquel nous nous sommes connectés en utilisant Direct Connect. 

Nous avons obtenu deux connexions hébergées par AWS (primaire et secondaire, afin d'assurer la bascule de connexion). L'idée principale était d'étendre notre infrastructure existante d'une manière ou d'une autre. Cela signifiait [Transit VPC](https://docs.aws.amazon.com/solutions/latest/cisco-based-transit-vpc/appendix-d.html) – la solution qui nous a aidés à intégrer de telles connexions.

Maintenant, regardons un peu de code pour représenter ce que nous avons discuté. La première chose à définir sera notre VPC principal. Je veux le présenter à des fins d'illustration uniquement, afin que toutes les étapes suivantes semblent plus cohérentes.

```hashicorp configuration language
variable "main_vpc_name" {
  description = "Nom de votre VPC principal"
}
variable "main_vpc_cidr" {
  description = "CIDR de votre VPC principal, par exemple 10.1.0.0/16"
}
variable "public_subnet" {
  description = "Sous-réseau public de votre VPC principal (si vous en avez un), par exemple 10.1.1.0/24"
}
variable "private_app_subnet" {
  description = "Sous-réseau privé de votre VPC principal (si vous en avez un), par exemple 10.1.2.0/24"
}
variable "main_vpc_key_name" {
  default     = "main-vpc-key"
  description = "Nom de la clé SSH de votre VPC principal"
}
variable "aws_availability_zone" {
  description = "Votre zone de disponibilité AWS de votre VPC principal"
}

provider "aws" {
  profile = "votre-profil"
  region  = "votre-région"
}

terraform {
  backend "s3" {
    bucket  = "votre-seau-etats-terraform"
    key     = "terraform.tfstate"
    profile = "votre-profil"
    region  = "votre-région"
  }
}

module "vpc" {
  version = "~> v2.0"
  source  = "terraform-aws-modules/vpc/aws"
  name    = var.main_vpc_name
  cidr    = var.main_vpc_cidr

  azs = [
    var.aws_availability_zone,
  ]

  private_subnets = [
    var.private_app_subnet
  ]

  public_subnets = [
    var.public_subnet,
  ]

  single_nat_gateway     = true
  one_nat_gateway_per_az = false
  enable_nat_gateway     = true
  enable_vpn_gateway     = false

  tags = {
    Terraform = "true"
  }
}
/***********************************************************************
ci-dessous peuvent être définies d'autres ressources de votre infrastructure
ex. serveur OpenVPN, instances, configuration de sécurité, paires de clés, etc.

...
***********************************************************************/
```

Ensuite, certains des paramètres principaux du VPC vont être utilisés dans le VPC de transit. Définissons-les donc comme sortie :

```hashicorp configuration language
output "main_vpc_id" {
  value = module.vpc.vpc_id
}
output "main_vpc_range" {
  value = module.vpc.vpc_cidr_block
}
output "main_vpc_az" {
  value = module.vpc.azs.0
}
output "main_vpc_key_name" {
  value = var.main_vpc_key_name
}
output "main_public_routing_table_id" {
  value = module.vpc.public_route_table_ids.0
}
output "main_private_routing_table_id" {
  value = module.vpc.private_route_table_ids.0
}
```

Maintenant, nous pouvons commencer à configurer notre VPC de transit. Juste pour une bonne conception, nous avons décidé de le gérer dans un état séparé sous un dossier séparé (par exemple, _tranist-vpc/_). Importons d'abord les _sorties_ ci-dessus en tant que _locaux_ :

```hashicorp configuration language
locals {
  main_private_routing_table = data.terraform_remote_state.main.outputs.main_private_routing_table_id
  
  main_public_routing_table  = data.terraform_remote_state.main.outputs.main_public_routing_table_id
  
  main_vpc_id                = data.terraform_remote_state.main.outputs.main_vpc_id
 
 main_vpc_range              = data.terraform_remote_state.main.outputs.main_vpc_range
  
  main_vpc_az                = data.terraform_remote_state.main.outputs.main_vpc_az
  
  main_vpc_key_name          = data.terraform_remote_state.main.outputs.main_vpc_key_name
}
```

Ensuite, nous pouvons commencer à définir la configuration du VPC de transit. Tout d'abord, je veux lister toutes les variables dont nous avons besoin (_faites attention aux IP des serveurs DNS dans le réseau auquel nous voulons nous connecter. Vous devriez les connaître pour les spécifier en tant que serveurs DNS dans le VPC de transit_) :

```hashicorp configuration language
variable "transit_vpc_name" {
  default = "transit-vpc"
}
variable "transit_vpc_cidr" {
  description = "CIDR du VPC de transit. Votre plage d'IP unique dans le réseau, par exemple 10.10.14.0/24"
}
variable "transit_private_subnet" {
  description = "Sous-réseau privé du VPC de transit, par exemple 10.10.14.0/25"
}
variable "transit_public_subnet" {
  description = "Sous-réseau public du VPC de transit pour la passerelle NAT, par exemple 10.10.14.128/25"
}
variable "network_dns_server" {
  description = "IP de l'un des serveurs DNS dans le réseau. Distribué par le fournisseur"
}
variable "network_dns_server_2" {
  description = "IP de l'un des serveurs DNS dans le réseau. Distribué par le fournisseur"
}
variable "dhcp_options_domain_name" {
  description = "Nom de domaine de l'option DHCP selon votre région AWS, par exemple {votre_région}.compute.internal"
}
```

Et, deuxièmement, la configuration :

```hashicorp configuration language
module "transit-vpc" {
  version = "~> v2.0"
  source  = "terraform-aws-modules/vpc/aws"
  name    = var.transit_vpc_name
  cidr    = var.transit_vpc_cidr

  azs = [
    local.main_vpc_az,
  ]

  private_subnets = [
    var.transit_private_subnet,
  ]

  public_subnets = [
    var.transit_public_subnet,
  ]

  single_nat_gateway               = true
  one_nat_gateway_per_az           = false
  enable_nat_gateway               = true
  enable_vpn_gateway               = false
  enable_dhcp_options              = true
  dhcp_options_domain_name         = var.dhcp_options_domain_name
  dhcp_options_domain_name_servers = [var.network_dns_server, var.network_dns_server_2]


  tags = {
    Terraform = "true"
  }
}
```

## Direct Connect utilisant Terraform

Continuons avec la configuration de Direct Connect. Tout d'abord, définissons toutes les variables dont nous avons besoin pour continuer. Vous devriez obtenir toutes ces valeurs de votre fournisseur de réseau. Je suppose qu'elles vous seront envoyées (cela a fonctionné pour nous) dans un document séparé comme une feuille de calcul :

```hashicorp configuration language
variable "bgp_provider_asn" {
  description = "Numéro de système autonome BGP du fournisseur. Distribué par le fournisseur"
}
variable "provider_vln_id" {
  description = "ID VLAN BGP du fournisseur. Distribué par le fournisseur"
}
variable "primary_bgp_key" {
  description = "Clé d'authentification BGP pour l'interface virtuelle principale. Distribuée par le fournisseur"
}
variable "secondary_bgp_key" {
  description = "Clé d'authentification BGP pour l'interface virtuelle secondaire. Distribuée par le fournisseur"
}
variable "primary_connection_id" {
  description = "Clé d'authentification BGP pour l'interface virtuelle principale. Distribuée par le fournisseur"
}
variable "secondary_connection_id" {
  description = "Plage d'IP distribuée par le fournisseur"
}
variable "primary_amazon_address" {
  description = "Plage d'IP distribuée par le fournisseur"
}
variable "secondary_amazon_address" {
  description = "Plage d'IP distribuée par le fournisseur"
}
variable "primary_customer_address" {
  description = "Plage d'IP distribuée par le fournisseur"
}
variable "secondary_customer_address" {
  description = "Plage d'IP distribuée par le fournisseur"
}
```

Et maintenant nous pouvons faire le reste de la configuration :

```hashicorp configuration language
resource "aws_dx_gateway" "provider-gateway" {
  name            = "provider-dc-gateway"
  amazon_side_asn = "64512" // généralement c'est une valeur par défaut
}

resource "aws_dx_gateway_association" "transit" {
  dx_gateway_id         = aws_dx_gateway.provider-gateway.id
  associated_gateway_id = aws_vpn_gateway.transit_vpn_gw.id
  allowed_prefixes = [
    var.transit_vpc_cidr
  ]
}

resource "aws_dx_private_virtual_interface" "primary" {
  connection_id    = var.primary_connection_id
  name             = "provider-vif-primary"
  vlan             = var.provider_vln_id
  address_family   = "ipv4"
  bgp_asn          = var.bgp_provider_asn
  amazon_address   = var.primary_amazon_address
  customer_address = var.primary_customer_address
  dx_gateway_id    = aws_dx_gateway.provider-gateway.id
  bgp_auth_key     = var.primary_bgp_key

}

resource "aws_dx_private_virtual_interface" "secondary" {
  connection_id    = var.secondary_connection_id
  name             = "provider-vif-secondary"
  vlan             = var.provider_vln_id
  address_family   = "ipv4"
  bgp_asn          = var.bgp_provider_asn
  amazon_address   = var.secondary_amazon_address
  customer_address = var.secondary_customer_address
  dx_gateway_id    = aws_dx_gateway.provider-gateway.id
  bgp_auth_key     = var.secondary_bgp_key
}
```

Maintenant, si vous allez dans votre console AWS, à côté de Direct Connection, vous devriez voir quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/dc-connection.png)
_connexions directes configurées_

## Appairage entre les VPC principaux et de transit

Le dernier problème à résoudre est de configurer la connectivité entre nos services et le VPC de transit afin d'établir l'accès au réseau. 

Pour y parvenir, nous décidons d'utiliser l'[appairage VPC](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html). Ici, nous aurons besoin de certaines des variables _locales_ que nous avons importées précédemment :

```hashicorp configuration language
resource "aws_vpc_peering_connection" "main-to-transit" {
  peer_vpc_id = module.transit-vpc.vpc_id
  vpc_id      = local.main_vpc_id
  auto_accept = true

  tags = {
    Name = "Appairage VPC entre le VPC principal et le VPC de transit"
  }
}

resource "aws_route" "from-main-to-transit" {
  route_table_id            = local.main_private_routing_table
  destination_cidr_block    = var.transit_vpc_cidr
  vpc_peering_connection_id = aws_vpc_peering_connection.main-to-transit.id
}

resource "aws_route" "from-main-public-to-transit" {
  route_table_id            = local.main_public_routing_table
  destination_cidr_block    = var.transit_vpc_cidr
  vpc_peering_connection_id = aws_vpc_peering_connection.main-to-transit.id
}

resource "aws_route" "from-transit-to-main" {
  route_table_id            = module.transit-vpc.private_route_table_ids.0
  destination_cidr_block    = local.main_vpc_range
  vpc_peering_connection_id = aws_vpc_peering_connection.main-to-transit.id
}
```

Ensuite, nous devons autoriser le trafic HTTP entrant depuis le VPC principal. Cette configuration peut être faite comme suit :

```hashicorp configuration language
resource "aws_security_group" "transit_vpc_sg" {
  name        = "transit-vpc-sg"
  description = "Groupe de sécurité du VPC de transit"
  vpc_id      = module.transit-vpc.vpc_id

  ingress {
    description = "Autoriser HTTP depuis le VPC principal"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = [local.main_vpc_range]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "transit-vpc"
  }
}
```

Super. Maintenant, nous avons deux VPC qui sont appairés et coexistent ensemble.

## Utilisez-vous OpenVPN (optionnel) ?

Dans notre cas, nous avons un serveur OpenVPN pour gérer l'accès (SSH) aux ressources internes du VPC principal. Et nous voulions accéder aux ressources des VPC de transit de la même manière. Pour ce faire, nous devions créer quelques ressources supplémentaires au sein du VPC de transit :

```hashicorp configuration language
resource "aws_vpn_gateway" "transit_vpn_gw" {
  tags = {
    Name = "transit-vpn-gw"
  }
}

resource "aws_vpn_gateway_attachment" "vpn_attachment" {
  vpc_id         = module.transit-vpc.vpc_id
  vpn_gateway_id = aws_vpn_gateway.transit_vpn_gw.id
}

resource "aws_vpn_gateway_route_propagation" "transit" {
  vpn_gateway_id = aws_vpn_gateway.transit_vpn_gw.id
  route_table_id = module.transit-vpc.private_route_table_ids.0
}
```

Et ensuite ajouter une _règle d'entrée_ à `transit-vpc-SG` qui a été créée à l'étape précédente :

```hashicorp configuration language
ingress {
    description = "Autoriser SSH depuis le VPC principal"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = [local.main_vpc_range]
}
```

Pour faire fonctionner tout cela, vous devez spécifier le CIDR du VPC de transit ainsi que le CIDR du VPC principal dans le paramètre de routage du serveur OpenVPN sous la section Paramètres VPN :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/open-VPC-server-settings.png)
_Paramètres de routage du serveur OpenVPN_

Nous y sommes presque. La dernière chose à faire est de concevoir et configurer comment nos services au sein du VPC principal pourront accéder de manière programmatique au réseau.

## Service de routage

Pour résumer, la principale raison pour laquelle nous avons fait tout cela est que nous devons pouvoir accéder à d'autres services dans le réseau (par exemple, demander ou soumettre des données). Nous avons trouvé deux moyens possibles d'y parvenir ici :

* Migrer les services requis vers le VPC de transit et les utiliser là-bas, avec de nouvelles IP privées. Le routage interne du VPC principal doit être ajusté. En plus de cela, tout accès aux serveurs de base de données, au stockage des logs, etc., doit être géré également.
* Créer un service de routage (exécutant HAproxy ou NGingx) au sein du VPC de transit. Ajouter l'IP privée du routeur au fichier `hosts` de chaque service dans le VPC principal qui souhaite accéder au réseau afin que l'IP soit résolue derrière le nom de domaine requis.

Nous avons choisi la deuxième option car elle semblait être la plus alignée avec le [principe ouvert-fermé](https://fr.wikipedia.org/wiki/Principe_ouvert-fermé). Voici à quoi cela ressemble approximativement :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/transit-vac-router-service-3-2.png)
_service de routage du VPC de transit_

Configurons-le dans Terraform :

```hashicorp configuration language
variable "router_private_ip" {
  description = "IP privée de l'instance du routeur dans le VPC de transit pour router les requêtes en arrière et en avant, par exemple 10.10.14.90"
}

resource "aws_instance" "router" {
  ami               = "ami-0eb89db7593b5d434" // n'importe quelle AMI que vous préférez
  instance_type     = "t2.micro" // n'importe quel type que vous préférez
  availability_zone = local.main_vpc_az
  key_name          = local.main_vpc_key_name
  subnet_id         = module.transit-vpc.private_subnets.0
  private_ip        = var.router_private_ip


  vpc_security_group_ids = [
    aws_security_group.router_sg.id,
  ]

  user_data = file("router_init.sh")

  associate_public_ip_address = false
  tags = {
    Name    = "transit-vpc-router"
    Managed = "terraform"
  }
}

resource "aws_security_group" "router_sg" {
  name        = "router_security_group"
  description = "Groupe de sécurité du routeur"

  ingress {
    from_port = 80
    to_port   = 80
    protocol  = "tcp"

    cidr_blocks = [
      local.main_vpc_range,
      var.transit_private_subnet
    ]
  }

  ingress {
    from_port = 22
    to_port   = 22
    protocol  = "tcp"

    cidr_blocks = [
      local.main_vpc_az,
    ]
  }

  egress {
    from_port = 0
    to_port   = 0
    protocol  = "-1"

    cidr_blocks = [
      "0.0.0.0/0",
    ]
  }

  vpc_id = module.transit-vpc.vpc_id

  tags = {
    Managed = "terraform"
  }
}
```

Ici, `router_init.sh` contient un script pour configurer et lancer le service HAproxy dans un conteneur. À des fins d'illustration, supposons que nous voulons accéder à deux noms de domaine internes dans le réseau :

* `domain-name-1.internal.com` 
* `domain-name-2.internal.com`

```bash
#! /bin/bash

# Installer Docker
apt-get update

apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -

apt-key fingerprint 0EBFCD88

sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

apt-get update

apt-get install -y docker-ce

usermod -a -G docker ubuntu

chown -R ubuntu:ubuntu /home/ubuntu/.docker/

# Créer la configuration HAproxy
cat > /home/ubuntu/haproxy.cfg <<- "EOF"
       global
           log stdout local0
           daemon
           maxconn 4000

       defaults
           log               global
           mode              http
           option            httplog
           timeout connect   5s
           timeout check     5s
           timeout client    60s
           timeout server    60s
           timeout tunnel    3600s

       frontend http-in
           bind *:80

           #acls des hôtes
           acl domain1_acl             hdr(host) -i domain-name-1.internal.com
           acl domain2_acl             hdr(host) -i domain-name-2.internal.com


           use_backend domain1         if domain1_acl
           use_backend domain2         if domain2_acl

       backend domain1
           mode http
           option forwardfor
           http-request replace-header Host .* domain-name-1.internal.com
           server domain1 domain-name-1.internal.com:443 ssl verify none

       backend domain2
           mode http
           option forwardfor
           http-request replace-header Host .* domain-name-2.internal.com
           server domain2 domain-name-2.internal.com:443 ssl verify none
EOF

#Lancer le routeur
docker run -d --restart always --name haproxy --net=host -v /home/ubuntu:/usr/local/etc/haproxy:ro haproxy:2.1-alpine
```

La dernière étape consiste à vérifier que nos domaines ont été ajoutés au fichier `hosts` sur les instances dans le VPC principal et à commencer à faire des requêtes via HTTP.

## Réflexions finales

Dans cet article, je vous ai montré comment intégrer Direct Connect à votre infrastructure AWS existante. J'ai également parlé de la manière dont vous pouvez la gérer efficacement en utilisant Terraform. 

Ensuite, j'ai discuté de l'approche qui serait appropriée pour une configuration de routage réseau qui rendrait la solution transparente et facile à maintenir autant que possible. 

Le Transit VPC, qui est recommandé par AWS pour résoudre de tels défis, était effectivement facile à configurer. Et l'approche que nous avons essayée avec le service de routage au sein du VPC de transit pour accéder au réseau privé a montré sa preuve de travail. Mais cela ne semblait pas être meilleur que d'autres alternatives. 

Enfin, j'ai introduit des extraits de code Terraform qui, je l'espère, seront utiles pour quiconque souhaite faire quelque chose de similaire.

J'espère que vous avez apprécié cet article et que vous l'avez trouvé utile !