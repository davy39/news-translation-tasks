---
title: Apprendre la syntaxe de base de Terraform en 20 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-05-26T18:00:52.000Z'
originalURL: https://freecodecamp.org/news/terraform-syntax-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/terraform-article-cover-image.jpg
tags:
- name: Infrastructure as code
  slug: infrastructure-as-code
- name: Terraform
  slug: terraform
seo_title: Apprendre la syntaxe de base de Terraform en 20 minutes
seo_desc: "By Sumeet Ninawe\nIn this article, I'll give you a brief overview of the\
  \ configuration syntax of Terraform. \nTerraform's docs provide the most comprehensive\
  \ look at its syntax. But this article should serve as a condensed quick start introduction\
  \ that..."
---

Par Sumeet Ninawe

Dans cet article, je vais vous donner un bref aperçu de la syntaxe de configuration de Terraform.

[La documentation de Terraform](https://www.terraform.io/docs/index.html) offre le regard le plus complet sur sa syntaxe. Mais cet article devrait servir d'introduction rapide et condensée qui donnera aux nouveaux utilisateurs un aperçu simplifié. Nous nous concentrerons sur les structures de base sans trop entrer dans les détails.

Pour vous aider à apprendre la syntaxe, nous allons passer en revue un exemple et je vous enseignerai les parties les plus importantes du langage de configuration Terraform (appelé HCL - le HashiCorp Configuration Language). Ensuite, nous construirons une infrastructure en tant que code (IaC) pour la voir en action.

Avant de commencer, vous devriez avoir Terraform installé sur votre système local. Vous devriez également avoir accès à la console de gestion AWS, et avoir configuré un utilisateur IAM pour Terraform.

## Arguments et blocs dans Terraform

Le premier exemple ci-dessous crée une instance EC2 :

```
provider “aws” {
    region = “us-west-1”
}
 
resource “aws_instance” “myec2” {
    ami = “ami-12345qwert”
    instance_type = “t2.micro”
}
```

Le code se compose de deux blocs entourés d'accolades ( {} ), et chacun de ces blocs a certains **arguments** définis.

Comme dans la plupart des langages de programmation, vous utilisez des arguments pour assigner des valeurs à des variables. Dans Terraform, ces variables sont des attributs associés à un type particulier de bloc.

Le bloc provider “aws” a un argument – `region = “us-west-1”`, où la région est un attribut associé au bloc, et une valeur “us-west-1” lui est assignée. La valeur est de type chaîne de caractères (string), elle est donc entourée d'une paire de guillemets doubles ( “” ).

De même, le bloc resource possède deux arguments qui définissent les valeurs des attributs associés.

Terraform utilise différents types de **blocs**. Selon le type, les blocs représentent et englobent un ensemble d'attributs et de fonctions. Dans l'exemple donné, nous avons un bloc de type provider et un autre de type resource, et chaque bloc possède un identifiant et un ensemble de labels d'entrée.

Le bloc provider prend un label d'entrée – le nom du provider. Dans ce cas, “aws”. Il indique également à Terraform d'installer le plugin du provider AWS pendant la phase d'initialisation (init).

Le bloc resource prend 2 labels d'entrée – le type de ressource et le nom de la ressource. Dans ce cas, le type est “aws_instance” et le nom est “myec2”. Ce qui suit est le corps du bloc entouré d'accolades.

## Comment créer une instance EC2 sur AWS

Alors, comment commencer à exprimer notre infrastructure en tant que code et à l'utiliser ? Prenons l'exemple de la création d'une simple instance EC2 sur AWS.

Commencez par créer un répertoire de votre choix où vous placerez tout le code de configuration nécessaire pour créer une instance EC2.

Par défaut, Terraform suppose que tous les fichiers avec des extensions `.tf*` dans un répertoire font partie de la configuration, quels que soient les noms de fichiers. Créez un fichier nommé `main.tf` dans ce répertoire.

La première chose que nous devons décider est quels providers nous allons utiliser. Puisque nous allons lancer une instance EC2 sur AWS, we devons déclarer les providers requis comme vous pouvez le voir dans l'extrait ci-dessous :

```
terraform {
 required_providers {
   aws = {
     source  = "hashicorp/aws"
     version = "~> 3.0"
   }
 }
}

provider "aws" {
 region = “us-west-1”
}
```

Nous avons déclaré deux blocs – `terraform` et `provider`. `terraform` est un bloc de niveau supérieur, mais il est également optionnel. C'est une bonne pratique de le spécifier, surtout lorsque vous travaillez avec la gestion d'état à distance (remote state management).

Le bloc `terraform` contient un bloc imbriqué qui spécifie les `required_providers`. Nous avons besoin du provider `aws`. `aws` à l'intérieur de `required_providers` est une map, qui spécifie la source (`source`) et la version (`version`) du provider.

Ensuite, we avons un bloc provider pour `aws`, qui spécifie la région (`region`) souhaitée.

Généralement, c'est ainsi que tout code Terraform commence. Bien sûr, il peut y avoir des variations, et la meilleure façon d'en être sûr est de se référer au [Terraform registry](https://registry.terraform.io/) pour les versions spécifiques de Terraform ainsi que pour le plugin du provider lui-même.

Pour les besoins de cet exemple, nous nous référons à la [documentation du plugin AWS](https://registry.terraform.io/providers/hashicorp/aws/latest/docs).

Le registre Terraform documente l'utilisation de toutes les ressources des différents fournisseurs de cloud avec des exemples. C'est une excellente référence lorsque vous travaillez avec Terraform.

### Providers Terraform

Installer Terraform sur le système ne suffit pas. Terraform fonctionne sur une architecture basée sur des plugins, où le binaire Terraform constitue le cœur et chaque fournisseur de cloud est un plugin.

Pour que les configurations fonctionnent, ces plugins sont installés lors de la phase d'initialisation.

Les plugins de provider viennent avec leur propre ensemble de configurations, de types de ressources et de sources de données. Le registre Terraform documente tous les détails pour un provider donné.

### Ressources Terraform

Chaque provider vient avec un ensemble de ressources. `resource`, comme son nom l'indique, représente la ressource cloud réelle à créer dans le langage de configuration.

Les providers activent les ressources. Dans l'exemple donné, `aws` est un provider et `aws_instance` est une ressource fournie par le provider AWS.

La ressource a ses attributs. Ces attributs sont documentés dans le registre Terraform. Parmi tous les attributs, certains sont obligatoires. Les ressources sont les constructions exactes qui sont exécutées par Terraform.

En continuant avec l'exemple, définissons une ressource d'instance AWS EC2 en ajoutant le code ci-dessous dans notre fichier [`main.tf`](http://main.tf/).

```
resource "aws_instance" "demo" {
 ami = “ami-00831fc7c1e3ddc60”
 instance_type = “t2.micro”

 tags = {
   name = "Demo System"
 }
}
```

Nous commençons par un bloc resource nommé “aws_instance” et nous passons un label et le nommons “demo”. Le label est le nom de votre choix.

Ensuite, ouvrez le bloc à l'aide d'accolades et spécifiez les attributs requis utilisés par la ressource `aws_instance`. Le premier attribut est `ami` qui spécifie l'ID de l'Amazon machine image pour l'instance EC2.

Le deuxième attribut est `instance_type` qui spécifie la taille de la machine à créer.

Nous passons également des tags, ce qui est un argument optionnel. En tant que tag, nous passons “name” comme clé et “Demo System” comme valeur. C'est tout – nous avons défini notre ressource.

Nous sommes maintenant techniquement prêts avec la configuration. Nous pouvons continuer et initialiser Terraform dans ce répertoire afin qu'il installe le plugin du provider pour AWS. Nous pourrons ensuite planifier (`plan`) et appliquer (`apply`) cette configuration.

Enregistrez le fichier, puis lancez `terraform init` et voyez s'il installe le plugin du provider AWS. Une fois que c'est fait avec succès, lancez `terraform plan` et observez la sortie.

Mettons tout en perspective. Les `providers` permettent à Terraform de savoir quels plugins doivent être installés pour exécuter la configuration. Les `resources` représentent les ressources cloud réelles à créer.

Généralement, chaque ressource a un nom ( “aws_instance” ). La partie initiale du nom de la ressource est l'identifiant du provider ( “aws” ) qui est séparé par un underscore.

### Variables Terraform

Terraform est un langage déclaratif. Dans l'exemple, nous avons déclaré l'état final de la machine virtuelle sur le cloud souhaité.

C'est maintenant à Terraform de prendre cette configuration et de l'exécuter pour créer la ressource virtuelle. Cela dit, Terraform nous donne la possibilité de spécifier des **variables d'entrée** à sa configuration.

Les variables d'entrée sont comme des paramètres pour une fonction donnée, tout comme dans n'importe quel langage de programmation.

Elles sont particulièrement utiles lorsque vous devez spécifier la même valeur à plusieurs endroits de votre code. À mesure que le projet grandit, il devient plus facile de modifier certaines valeurs qui pourraient être utilisées à plusieurs endroits en utilisant des variables.

Terraform prend en charge les types de variables primitifs tels que string, number, boolean, et plusieurs types complexes tels que list, set, map, object et tuple.

Définissons quelques variables dans notre code comme ci-dessous :

```
variable "region" {
 default = "us-west-1"
 description = "AWS Region"
}

variable "ami" {
 default = "ami-00831fc7c1e3ddc60"
 description = "Amazon Machine Image ID for Ubuntu Server 20.04"
}

variable "type" {
 default = "t2.micro"
 description = "Size of VM"
}
```

Comme vous pouvez le voir, nous avons introduit trois nouvelles variables pour la région (`region`), l'AMI (`ami`) et le type (`type`). Nous utiliserons cela dans notre configuration jusqu'à présent. Les valeurs des variables peuvent être référencées en utilisant `var.<nom de la variable>`.

La configuration Terraform nous donne également la possibilité de retourner des valeurs. Ces valeurs sont connues sous le nom de **valeurs de sortie** (output values).

Lorsque Terraform termine l'exécution de la configuration, il rend les valeurs de sortie disponibles. Elles peuvent ensuite être utilisées comme entrées pour d'autres interfaces.

Nous avons défini une variable de sortie “instance_id” dans notre code. La valeur de cette variable de sortie est définie à l'aide de la référence d'attribut de “aws_instance.demo”. De même, nous pouvons nous référer à d'autres variables de sortie disponibles à partir de n'importe quelle ressource de la configuration.

Voici le code mis à jour de notre `main.tf`. Nous avons utilisé trois variables ici :

```
terraform {
 required_providers {
   aws = {
     source  = "hashicorp/aws"
     version = "~> 3.0"
   }
 }
}
 
provider "aws" {
 region = var.region
}
 
variable "region" {
 default = "us-west-1"
 description = "AWS Region"
}
 
variable "ami" {
 default = "ami-00831fc7c1e3ddc60"
 description = "Amazon Machine Image ID for Ubuntu Server 20.04"
}
 
variable "type" {
 default = "t2.micro"
 description = "Size of VM"
}
 
resource "aws_instance" "demo" {
 ami = var.ami
 instance_type = var.type
 
 tags = {
   name = "Demo System"
 }
}
 
output "instance_id" {
 instance = aws_instance.demo.id
}
```

Enregistrez le fichier et lancez `terraform plan`. Notez que Terraform prend en compte la variable de sortie cette fois. Il indique que la sortie est connue “after apply” (après application) :

```
Plan: 1 to add, 0 to change, 0 to destroy.
 
Changes to Outputs:
  + instance_id = (known after apply)
```

Allez-y et faites `terraform apply`, puis vérifiez la sortie. N'oubliez pas de lancer `terraform destroy` après chaque `apply` réussi.

Enfin, Terraform prend également en charge les **variables locales**, qui sont des valeurs temporaires utilisées localement par des fonctions et des blocs.

### Provisioners Terraform

Le provisionnement signifie installer, mettre à jour et maintenir les logiciels requis une fois que le matériel ou la machine virtuelle est prêt à l'emploi.

Terraform peut déclencher des processus de provisionnement logiciel une fois qu'une machine virtuelle est prête, mais cela ne signifie pas qu'il s'agit d'un outil de provisionnement à plein temps.

Vous pouvez utiliser cet outil pour préparer l'infrastructure à la gestion en installant les composants logiciels initiaux et essentiels.

Il existe des outils comme Salt Stack, Ansible, Chef et d'autres, et la plupart d'entre eux sont basés sur des agents. Terraform peut exécuter des scripts initiaux pour installer des mises à jour de correctifs, des logiciels agents, ou même définir des politiques d'accès utilisateur pour s'assurer que les machines sont prêtes à l'emploi.

Terraform est livré avec des provisioners génériques et prend également en charge des provisioners spécifiques aux fournisseurs.

## Comment gérer le code dans Terraform

Avant de continuer, organisons d'abord notre code en plusieurs fichiers. En pratique générale, la base de code Terraform est divisée en plusieurs fichiers basés sur les providers, les ressources et les variables. Créons trois fichiers comme ci-dessous :

1. `variables.tf` – Ce fichier contient toutes les variables d'entrée déclarées. Dans notre exemple, nous avons des variables d'entrée définies pour `region`, `ami` et `type` et une variable de sortie `instance_id`.
2. `provider.tf` – Ce fichier contient les déclarations des providers que vous utilisez. Dans notre cas, nous avons les blocs `terraform` et le provider `aws`.
3. `main.tf` – Ce fichier contient les déclarations des ressources réelles à créer.

Par défaut, Terraform suppose que tout le code placé dans un répertoire particulier fait partie de la même configuration.

Donc techniquement, cela ne change pas grand-chose que vous mettiez le code dans un seul fichier ou que vous le divisiez en plusieurs fichiers et sous-répertoires. Du point de vue de la maintenabilité, cela a beaucoup de sens de le faire.

### Méta-arguments dans Terraform

Avant d'entrer dans le vif du sujet, assurez-vous que lorsque vous travaillez sur les exemples, vous lancez toujours `terraform destroy` après chaque exécution de `terraform apply`.

Les méta-arguments sont des constructions spéciales fournies pour les ressources. Nous avons vu que les blocs de ressources sont les ressources cloud réelles que Terraform crée.

Souvent, il est délicat de déclarer des ressources d'une manière qui satisfait certaines exigences.

Les méta-arguments sont utiles dans des situations comme la création de ressources chez le même fournisseur de cloud mais dans des régions différentes. Ils sont également utiles lorsque nous créons plusieurs ressources identiques avec des noms différents, ou lorsque nous devons déclarer des dépendances implicites à des endroits où Terraform n'est pas capable d'identifier la dépendance lui-même.

Les sections ci-dessous décrivent certains méta-arguments en action.

#### Le méta-argument Provider

Vous utiliserez le méta-argument `provider` lorsque vous avez plusieurs configurations de provider dans une configuration Terraform donnée. Terraform mappe automatiquement la ressource donnée au provider par défaut identifié par l'identifiant de la ressource.

Par exemple, le provider par défaut pour `aws_instance` est `aws`. Ce provider `aws` est actuellement configuré pour déployer une ressource dans une région particulière.

Cependant, si nous voulons avoir un autre provider `aws` pour une autre région, ou avec un paramètre de configuration différent, nous pouvons écrire un autre bloc provider.

Même s'il est possible d'écrire plusieurs configurations de provider, Terraform choisit par défaut le même provider pour `aws` pour créer des ressources.

C'est là que les **alias** entrent en jeu. Chaque configuration de provider peut être marquée avec un alias, et la valeur de cet alias est utilisée dans notre méta-argument **provider** dans le bloc resource pour spécifier différentes configurations de provider pour des ressources identiques.

Dans notre exemple, dupliquons le provider `aws` et donnons-leur des alias appropriés. Les providers modifiés avec un alias devraient ressembler à ce qui suit dans le fichier `provider.tf` :

```
provider "aws" {
  alias  = "aws_west"
  region = var.region_west
}

provider "aws" {
  alias  = "aws_east"
  region = var.region_east
}
```

Notez que nous avons également modifié les variables de la région pour représenter deux régions différentes, l'ouest (west) et l'est (east). Apportez les modifications correspondantes au fichier `variables.tf` comme ci-dessous :

```
variable "region_west" {
  default     = "us-west-1"
  description = "AWS West Region"
}

variable "region_east" {
  default     = "us-east-1"
  description = "AWS East Region"
}
```

Un dernier changement que nous devons faire est dans le fichier `main.tf`. Là, nous pouvons maintenant utiliser le méta-argument provider pour spécifier l'alias d'un provider spécifique.

Nous pouvons mentionner la configuration du provider que nous voulons en spécifiant `<provider>.<alias>` dans le méta-argument. Reportez-vous au fichier `main.tf` modifié ci-dessous :

```
resource "aws_instance" "demo" {
  provider      = aws.aws_west
  ami           = var.ami
  instance_type = var.type

  tags = {
    name = "Demo System"
  }
}
```

Validez la configuration finale en lançant `terraform validate`, et il devrait afficher “`Success!`”

#### Le méta-argument Lifecycle

Le méta-argument `lifecycle` spécifie les paramètres liés au cycle de vie des ressources gérées par Terraform. Par défaut, chaque fois qu'une configuration est modifiée et appliquée, Terraform opère selon cette séquence :

1. Créer de nouvelles ressources.
2. Détruire les ressources qui n'existent plus dans la configuration.
3. Mettre à jour les ressources qui peuvent être mises à jour sans destruction.
4. Détruire et recréer les ressources modifiées qui ne peuvent pas être changées à la volée.

Vous pouvez utiliser un méta-argument `lifecycle` si vous souhaitez modifier ce comportement par défaut. Ces méta-arguments sont utilisés dans les blocs de ressources de la même manière que les méta-arguments provider.

Il existe trois paramètres de méta-argument lifecycle :

1. `create_before_destroy` : Utilisé lorsque vous voulez éviter la perte accidentelle d'infrastructure lorsqu'une configuration modifiée est appliquée. Lorsque cela est défini sur true, Terraform créera d'abord la nouvelle ressource avant de détruire l'ancienne.
2. `prevent_destroy` : Lorsqu'il est défini sur true, toute tentative de destruction de ceci dans la configuration entraînera une erreur. C'est souvent utile dans le cas de ressources dont la reproduction peut s'avérer coûteuse.
3. `ignore_changes` : Il s'agit d'un méta-argument de type liste qui spécifie les attributs d'une certaine ressource sous forme de liste. Lors des opérations de mise à jour, il arrive souvent que vous souhaitiez empêcher des modifications causées par des facteurs externes. Dans ces cas, vous devez déclarer la liste des attributs qui ne doivent pas être modifiés sans être examinés.

Les méta-arguments `lifecycle` sont utiles lorsque nous sommes en train de mettre en place une infrastructure complexe.

En modifiant le comportement par défaut de Terraform, nous pouvons mettre en place une certaine protection sous la forme de méta-arguments `lifecycle` pour les blocs de ressources confirmés et finalisés.

Dans notre exemple, nous n'utiliserons aucun méta-argument lifecycle.

#### Le méta-argument depends_on

Généralement, Terraform est conscient des dépendances lors de la création ou de la modification des ressources et s'occupe lui-même de la séquence.

Cependant, dans certains cas, Terraform ne peut pas détecter les dépendances implicites et continue simplement à créer des ressources en parallèle s'il ne voit aucune dépendance.

Prenez, par exemple, une configuration Terraform pour deux instances EC2 enfermées dans un VPC.

Lorsque vous avez cette configuration, Terraform sait automatiquement qu'il doit créer le VPC avant de lancer les instances EC2.

C'est une connaissance générale et Terraform le sait très bien. Dans les situations où les dépendances ne sont pas si évidentes, le méta-argument `depends_on` vient à la rescousse.

Il s'agit d'un argument de type liste qui prend la liste des identifiants de ressources déclarés dans la configuration.

#### Le méta-argument count

Imaginez une situation où vous aimeriez créer plusieurs ressources similaires. Par défaut, Terraform crée une ressource réelle pour un seul bloc de ressource.

Mais dans le cas de ressources multiples, Terraform fournit un méta-argument nommé `count`. Comme son nom l'indique, le `count` peut se voir attribuer un nombre entier pour représenter plusieurs ressources.

Dans notre exemple, créons trois instances EC2 similaires. Dans votre fichier `main.tf`, ajoutez un attribut count à la ressource `aws_instance.demo`, et attribuez-lui une valeur de `3`. Cela devrait ressembler à ce qui suit :

```
resource "aws_instance" "demo" {
  count         = 3
  provider      = aws.aws_west
  ami           = var.ami
  instance_type = var.type

  tags = {
    name = "Demo System"
  }
}
```

En faisant cela, nous faisons savoir à Terraform que nous devons créer trois instances EC2 avec la même configuration.

Enregistrez le fichier et exécutez `terraform validate`. Il renvoie une erreur disant “`Missing resource instance key`”.

Rappelez-vous que dans notre fichier `variables.tf`, nous avons mentionné une variable de sortie pour afficher l'`id` de la ressource créée. Puisque nous avons demandé à Terraform de créer trois instances, il n'est pas très clair quel ID il doit imprimer.

Pour contourner ce problème, nous utilisons une expression spéciale appelée expression `splat`.

Le cas idéal ici est d'exécuter une boucle for sur l'instance et d'imprimer la propriété ID. L'expression splat est un meilleur moyen d'effectuer la même tâche avec moins de lignes de code.

Tout ce que vous avez à faire est, dans le fichier `variables.tf`, de remplacer le code de la valeur de sortie par celui-ci :

```
output "instance_id" {
  value = aws_instance.demo[*].id
}
```

Enregistrez ce fichier et lancez `terraform validate` pour voir si tout est correct.

Une fois réussi, continuez et lancez `terraform plan` et `apply` et vérifiez votre console de gestion AWS dans la région us-west-1, c'est-à-dire `aws_west`. Faites-moi savoir les ID également.

Splat est unique en son genre et nous examinerons de plus près les expressions dans les sections à venir.

#### Le méta-argument for_each

`for_each`, comme son nom l'indique, est essentiellement une boucle “for each”. Le méta-argument `for_each` est utilisé pour créer/boucler à travers plusieurs ressources cloud similaires. Oui, cela ressemble au méta-argument `count` mais il y a une différence.

Premièrement, `for_each` et `count` ne peuvent pas être utilisés ensemble.

Deuxièmement, on peut dire qu'il s'agit d'une version améliorée du count. Le méta-argument count est de type nombre. Terraform crée simplement ce nombre de ressources.

Cependant, si vous souhaitez créer ces ressources avec certaines personnalisations dans la sortie, ou si vous avez déjà un objet de type map ou list sur la base duquel vous voulez créer des ressources, alors le méta-argument `for_each` est la solution.

Comme mentionné précédemment, vous pouvez attribuer des valeurs de type map et list à `for_each`. Une map est une collection de paires clé-valeur, tandis qu'une liste est une collection de valeurs (dans ce cas, des chaînes de caractères).

`for_each` est accompagné d'un objet spécial `each`. Il s'agit de l'itérateur dans la boucle que vous pouvez utiliser pour vous référer à la clé (`key`) ou à la valeur (`value`), ou seulement à la clé dans le cas d'une liste.

Jetons un coup d'œil à notre exemple. Nous aimerions créer des instances EC2 pour la map donnée. La map est assignée au méta-argument `for_each` et Terraform crée une instance EC2 pour chaque paire clé-valeur de la map.

Enfin, nous utilisons les informations `key` et `value` à l'aide de l'objet `each` pour définir l'attribut de nom dans le `tag`.

Le bloc resource dans `main.tf` ressemble maintenant à quelque chose comme ceci :

```
resource "aws_instance" "demo" {
  for_each = {
    fruit = "apple"
    vehicle = "car"
    continent = "Europe"
  }
  provider      = aws.aws_west
  ami           = var.ami
  instance_type = var.type

  tags = {
    name = "${each.key}: ${each.value}"
  }
}
```

Exécutez `terraform validate` et observez la sortie. Il renvoie une erreur pour la variable de sortie – “`This object does not have an attribute named id`”.

Une petite note ici : les expressions `splat` fonctionnent pour les variables de type liste. Comme nous avons utilisé une map lors de la définition de notre méta-argument `for_each`, nous devons changer l'expression de la valeur de retour pour un for each, comme ci-dessous :

```
output "instance_id" {
  //valeur = aws_instance.demo[*].id
  value = [for b in aws_instance.demo : b.id]
}
```

Exécutez à nouveau `terraform validate`. Si c'est réussi, continuez et appliquez (`apply`) la configuration. Vérifiez la console de gestion AWS pour les machines créées et les noms qui leur ont été attribués.

### Expressions Terraform

Les expressions sont des moyens de rendre votre code Terraform dynamique.

Les expressions se présentent sous deux formes – simples et complexes. Jusqu'à présent dans nos exemples, nous avons principalement traité des expressions simples.

Une expression simple est n'importe quel argument utilisé dans le cadre d'un bloc. Écrire un argument avec une valeur primitive assignée est une forme d'expression.

Nous avons utilisé une expression complexe appelée splat ( `*` ) dans notre exemple tout en travaillant avec des méta-arguments.

Cependant, il existe des expressions encore plus complexes que vous pouvez utiliser pour rendre votre code Terraform plus dynamique, lisible et flexible. Il existe différents types d'expressions que vous pouvez consulter dans la [documentation de Terraform](https://www.terraform.io/docs/configuration/expressions/index.html).

### Fonctions Terraform

Terraform possède des fonctions intégrées que vous pouvez utiliser avec des expressions. Ce sont des fonctions utilitaires qui sont utiles pour les manipulations de nombres et de chaînes de caractères.

Il existe des fonctions pour travailler avec les systèmes de fichiers, la date et l'heure, le réseau, la conversion de type, et plus encore.

Les fonctions associées aux expressions permettent d'écrire très facilement une IaC réellement dynamique. Vous pouvez consulter la liste des fonctions [ici](https://www.terraform.io/docs/configuration/functions.html).

## Conclusion

Dans cet article, nous avons pu manipuler des instances AWS EC2 en utilisant Terraform. J'espère que cela vous aidera à vous sentir plus à l'aise avec Terraform.

Si vous aimez ce contenu, n'hésitez pas à vous abonner, à suivre et à partager cet article de blog ! [Let'sDoTech](https://letsdotech.dev/), [Instagram](https://www.instagram.com/letsdotech/), [Twitter](https://twitter.com/letsdotech_dev), [LinkedIn](https://www.linkedin.com/company/letsdotech).