---
title: Terraform Certified Associate (003) – Comment étudier pour l'examen
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-09-11T19:17:49.000Z'
originalURL: https://freecodecamp.org/news/terraform-certified-associate-003-study-notes
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/terraform-course.png
tags:
- name: Certification
  slug: certification
- name: Cloud Computing
  slug: cloud-computing
- name: Terraform
  slug: terraform
seo_title: Terraform Certified Associate (003) – Comment étudier pour l'examen
seo_desc: "By Chris Williams\nI've been meaning to get my Terraform associates certification\
  \ for some time now, but something always got in the way. \nFinally I was able to\
  \ sit down and work my way through the study materials.\nCurrently Andrew Brown\
  \ and I are cre..."
---

Par Chris Williams

J'avais l'intention d'obtenir ma certification Terraform Associates depuis un certain temps, mais quelque chose m'en a toujours empêché.

Finalement, j'ai pu m'asseoir et travailler sur les matériaux d'étude.

Actuellement, Andrew Brown et moi créons deux Terraform Bootcamps : [un pour débutants](https://terraform.cloudprojectbootcamp.com/) et l'autre pour les praticiens intermédiaires. Ces bootcamps seront similaires au [AWS Cloud Project Bootcamp](https://aws.cloudprojectbootcamp.com/) d'Andrew (Playlist YouTube [ici](https://youtube.com/playlist?list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv)).

Dans ce guide, j'ai compilé mes notes d'étude en direct que j'ai utilisées pour me préparer à passer l'examen Terraform Certified Associate afin de vous aider à savoir quoi étudier.

Voici ce que je vais couvrir :

* [Matériaux de préparation](#heading-materiaux-de-preparation)
* [Comment utiliser ce guide](#heading-comment-utiliser-ce-guide)
* [Comprendre les concepts d'Infrastructure as Code (IaC)](#heading-comprendre-les-concepts-dinfrastructure-as-code-iac)
* [Comprendre le but de Terraform (vs autres outils IaC)](#heading-comprendre-le-but-de-terraform-vs-autres-outils-iac)
* [Comprendre les bases de Terraform](#heading-comprendre-les-bases-de-terraform)
* [Utiliser Terraform en dehors du flux de travail principal](#heading-utiliser-terraform-en-dehors-du-flux-de-travail-principal)
* [Interagir avec les modules Terraform](#heading-interagir-avec-les-modules-terraform)
* [Utiliser le flux de travail principal de Terraform](#heading-utiliser-le-flux-de-travail-principal-de-terraform)
* [Implémenter et maintenir l'état](#heading-implementer-et-maintenir-letat)
* [Lire, générer et modifier la configuration](#heading-lire-generer-et-modifier-la-configuration)
* [Comprendre les capacités de Terraform Cloud](#heading-comprendre-les-capacites-de-terraform-cloud)

## Matériaux de préparation

Pour se préparer à un examen, j'aime lister à l'avance les matériaux d'étude et les ressources de référence que je vais utiliser. Cela me permet de planifier mon temps d'étude avec un peu plus de discipline.

Voici les matériaux que j'ai utilisés :

1. [Certifications HashiCorp Cloud Engineer](https://developer.hashicorp.com/certifications) (Gratuit)

Ce site contient une mine d'informations :

![Image](https://mistwire.com/wp-content/uploads/2023/05/CleanShot-2023-05-30-at-13.48.29-2-1024x548.png)
_https://developer.hashicorp.com/certifications_

2. Les [Tutoriels de préparation Terraform Associate](https://developer.hashicorp.com/terraform/tutorials/certification-003) (Gratuit)

![Image](https://mistwire.com/wp-content/uploads/2023/06/CleanShot-2023-06-05-at-12.22.00-1024x683.png)
_https://developer.hashicorp.com/terraform/tutorials/certification-003_

3. Le cours [freeCodeCamp](https://youtu.be/SPcwo0Gq9T8) nouvellement mis à jour par Andrew Brown (Gratuit) 😀

4. [Jumppad.dev](https://jumppad.dev/) et leur dépôt [Terraform-workshop](https://github.com/jumppad-labs/terraform-workshop) (Gratuit)

5. Le cours Udemy [The Terraform Hands On Labs](https://www.udemy.com/course/terraform-hands-on-labs/) par Bryan Krausen (Payant)

## Comment utiliser ce guide

Chacune des sections ci-dessous couvrira l'un des neuf domaines spécifiés dans le [Guide de révision Terraform](https://developer.hashicorp.com/terraform/tutorials/certification-003/associate-review-003). Lisez la documentation, complétez les tutoriels et plongez dans les liens supplémentaires que j'ai fournis.

Les sections ci-dessous sont les grandes parties importantes d'informations que j'ai rassemblées pour chaque domaine, mais ce guide d'étude n'est pas exhaustif. Selon votre niveau de confort avec les connaissances spécifiques à un domaine, vous devrez plonger dans les liens fournis dans chaque section pour compléter votre compréhension du matériel.

## Comprendre les concepts d'Infrastructure as Code (IaC)

Le domaine 1 couvre les concepts généraux de l'IaC. Pourquoi voulons-nous l'utiliser ? À quoi est-il bon ? Y a-t-il des domaines où vous ne voudriez PAS l'utiliser ? Quels sont les différents types de langages qui peuvent être utilisés pour l'IaC et comment les approches diffèrent-elles ?

### Expliquer ce qu'est l'IaC :

Configurer manuellement votre infrastructure est bien pour le prototypage, mais est sujet à l'erreur humaine à grande échelle (ou lorsque vous devez provisionner le même environnement à plusieurs reprises). L'IaC est un plan de votre infrastructure et vous permet de partager/versionner/inventorier/documenter votre infrastructure.

Il existe deux types principaux d'infrastructure :

**Déclaratif** = Ce que vous voyez est ce que vous obtenez. C'est explicite avec 0 chance de mauvaise configuration :

* Azure uniquement -> Modèles ARM, Azure Blueprints
* AWS uniquement -> CloudFormation
* GCP uniquement -> Cloud Deployment Manager
* Tous les ci-dessus (& beaucoup d'autres) -> Terraform

**Impératif** = Utilise des langages de programmation existants comme Python, JS ou Ruby :

* AWS uniquement -> AWS CDK
* AWS, Azure, GCP, K8s -> Pulumi

Terraform supporte les boucles For, les blocs dynamiques, les structures de données complexes – donc c'est déclaratif avec certains avantages impératifs.

Le cycle de vie de l'infrastructure consiste à avoir des phases de travail clairement définies pour la planification, la conception, la construction, les tests, la maintenance et la mise hors service de votre infrastructure.

**Idempotent** : une propriété de certaines opérations telle que, peu importe le nombre de fois que vous les exécutez, vous obtenez le même résultat. Terraform est idempotent car, peu importe le nombre de fois que vous exécutez le même fichier de configuration, vous obtiendrez le même état attendu.

**Dérive de configuration** : un changement de configuration inattendu par rapport à ce qui est indiqué dans le fichier de configuration. Peut être dû à un ajustement manuel (accès à la console en production = MAUVAIS 😂), des pirates, etc... Comment le corriger ?

- Détecter : utiliser un outil de conformité comme AWS Config, ou un support intégré, par exemple, AWS CF Drift Detection, les fichiers d'état TF

- Corriger :
    - Commandes TF refresh & plan
    - Corriger manuellement (essayez de ne pas faire cela)
    - Reprovisionner (comporte ses propres risques)

- Prévenir :
    - utiliser une infrastructure immutable
    - toujours créer & détruire, jamais réutiliser
    - utiliser GitOps pour le contrôle de version IaC :
        - Créer un fichier tf
        - commit
        - Pull Request
        - révision par les pairs
        - commit vers main
    - L'action GitHub déclenche la construction

### Mutable vs Immutable infrastructure

Pensez à l'infrastructure mutable comme (1) construire une image de base (2) Déployer cette image de base puis (3) configurer le logiciel après le déploiement.

Pensez à l'infrastructure immutable comme (1) construire une image de base entièrement installée (2) déployer puis (3) si un changement doit être apporté, détruire cette infrastructure et la reconstruire avec une nouvelle image de base entièrement installée

* Mutable = Développer -> Déployer (VM) -> Configurer (par exemple, cloud-init)
* Immutable = Développer -> Configurer (Packer) -> Déployer

### Décrire les avantages des modèles IaC :

Pourquoi l'Infrastructure as Code est-elle importante ? Elle vous permet de :

* Construire & gérer votre infrastructure de manière (relativement 😅) sûre, cohérente et répétable
* Partager & réutiliser vos configurations plus facilement
* Gérer l'infrastructure sur plusieurs plateformes cloud
* Suivre les changements de ressources
* Utiliser le contrôle de version (Git, GitHub, etc..) pour collaborer avec les membres de l'équipe

## Comprendre le but de Terraform (vs autres outils IaC)

Le domaine 2 explique les différences entre Terraform et les autres offres IaC disponibles sur le marché. Les outils IaC agnostiques vs spécifiques au cloud ont chacun leur place sur le marché et vous choisirez entre eux en fonction de vos besoins (et ceux de votre entreprise).

### Expliquer les avantages multi-cloud et agnostiques des fournisseurs :

* Augmente la tolérance aux pannes
* Permet une récupération plus élégante des pannes des fournisseurs de cloud
* Réduit la complexité car chaque fournisseur a ses propres interfaces, outils et flux de travail que Terraform abstrait pour vous
* Utilisez le même flux de travail pour gérer plusieurs fournisseurs et gérer les dépendances inter-cloud
* Vue unifiée des ressources
* Une approche/flux de travail agnostique technologique

### Expliquer les avantages de l'état

- L'état (un fichier d'état) est nécessaire pour que Terraform fonctionne
- C'est une carte référençant une ressource dans le fichier tf à une ressource réelle qui est déployée
    - Par exemple, la ressource `"aws_instance" "webserver" {}` mappée à l'instance connue `"i-0dfcf96cceba9bc77"`
- Suivi des métadonnées
    - dépendances des ressources
    - suivi de l'ordre de construction/suppression
    - Ordonnancement au sein d'un fournisseur et entre plusieurs fournisseurs -> la complexité augmente rapidement
- Pour les environnements plus grands, utilisez les flags `-refresh=false` et `-target`
    - interroger chaque ressource peut prendre trop de temps
    - l'état mis en cache est traité comme un enregistrement de vérité
- Utilisez l'état distant lorsque vous travaillez en équipe
    - le verrouillage distant empêche 2 administrateurs de faire des changements simultanés

## Comprendre les bases de Terraform

Le domaine 3 aborde les commandes et processus que vous devez comprendre pour utiliser Terraform. Il couvre l'installation de Terraform lui-même, les fournisseurs, ce que sont les modules, et le flux de travail de base que vous ferez lors de la construction d'environnements IaC.

Quelques codes de triche utiles pour la CLI Terraform : `terraform -help` et `terraform (command) -help`.

### Cycle de vie de Terraform :

* code - créer ou éditer votre fichier de configuration terraform
* `terraform init` - Initialiser l'espace de travail, télécharger les fournisseurs et les modules
* `terraform plan` - voir quels changements seront apportés (ou générer un plan d'exécution) également connu sous le nom de "dry-run"
* `terraform validate` - s'assurer que les types, les valeurs et les attributs requis sont valides et présents
* `terraform apply` - créer les choses !
* `terraform destroy` - détruire les choses ! 😱

![Image](https://mistwire.com/wp-content/uploads/2023/06/CleanShot-2023-06-05-at-11.53.35.png)
_Diagramme montrant un flux de travail Terraform de base_

### Syntaxe HCL :

La syntaxe du langage Terraform se compose de quelques éléments standard :

![Image](https://mistwire.com/wp-content/uploads/2023/07/image-2.png)
_Éléments standard de HCL_

Par exemple, voici un bloc de ressource de base qui lancera une instance EC2 :

![Image](https://mistwire.com/wp-content/uploads/2023/07/image-1-1024x380.png)
_Exemple HCL avec les éléments standard mis en évidence_

```hcl
resource "aws_instance" "terraform_101_server"{
  ami            = "ami-0b5eea76982371e91"
  instance_type  = "t2.micro" 
```

- Les blocs sont des conteneurs pour d'autres contenus et représentent généralement la configuration d'un certain type d'objet (comme une ressource). Les blocs ont un type de bloc, peuvent avoir zéro ou plusieurs étiquettes, et ont un corps qui contient un nombre quelconque d'arguments et de blocs imbriqués. Il existe plusieurs types de blocs :
    - Bloc Terraform - paramètres pour l'environnement d'exécution de Terraform lui-même (version requise de terraform, paramètres de backend, etc.)
    - Bloc Fournisseur - détails du ou des fournisseurs utilisés. Inclut des informations comme les mécanismes d'accès, les options régionales, le profil à utiliser, etc...
    - Bloc Ressource - spécifie une ressource nommée de manière unique gérée par terraform. Inclut le type de ressource, le nom et les options de configuration
    - Bloc Données - sources de données qui peuvent être interrogées (fournisseur cloud, liste locale, etc.)
    - Bloc Module - ensemble réutilisable de ressources qui peuvent être exploitées dans plusieurs configurations terraform
    - Bloc Sortie - Les ressources gérées par Terraform exportent chacune des attributs dont les valeurs peuvent être utilisées ailleurs dans la configuration. Les valeurs de sortie sont un moyen d'exposer certaines de ces informations à l'utilisateur de votre module. (Par exemple, l'adresse IP d'une instance EC2).
    - Bloc Variable - Définit les variables à utiliser dans la configuration Terraform. Les variables d'entrée vous permettent de personnaliser des aspects des modules Terraform sans altérer le code source du module lui-même. Cette fonctionnalité vous permet de partager des modules entre différentes configurations Terraform, rendant votre module composable et réutilisable. Les noms de variables doivent être uniques 😉
        - ordre de priorité : défauts < variables d'environnement < fichier terraform.tfvars < fichier terraform.tfvars.json < .auto.tfvars < ligne de commande (-var & -var-file)
    - Bloc Locals - Une valeur locale attribue un nom à une [expression](https://developer.hashicorp.com/terraform/language/expressions), afin que vous puissiez utiliser le nom plusieurs fois dans un module au lieu de répéter l'expression.

### Installer et versionner les fournisseurs Terraform

Terraform s'appuie sur des [Fournisseurs](https://registry.terraform.io/browse/providers) pour permettre à Terraform d'interagir avec des systèmes distants (CSP, SaaS, API, etc.).

Certains fournisseurs nécessitent des informations de configuration supplémentaires (points de terminaison, régions utilisées, etc..) pour fonctionner.

Vous devez déclarer quels fournisseurs sont nécessaires dans vos configurations Terraform. Ils vont dans le module racine (les modules enfants obtiennent leurs configurations de fournisseur à partir du module racine) dans un bloc required_providers (voir [Exigences des fournisseurs](https://developer.hashicorp.com/terraform/language/providers/requirements) pour plus de détails)

Utilisez l'argument alias meta pour définir plusieurs configurations pour le même fournisseur (c'est-à-dire, pour supporter plusieurs régions pour une plateforme cloud)

Le bloc required_providers définit tous les fournisseurs nécessaires au module actuel

Pour vous assurer que plusieurs utilisateurs exécutent la même configuration Terraform (avec les mêmes versions de fournisseurs), vous :

- Spécifiez les contraintes de version des fournisseurs
- Utilisez le [fichier de verrouillage des dépendances](https://developer.hashicorp.com/terraform/language/files/dependency-lock) :
    - nommé .terraform.lock.hcl
    - mis à jour lorsque vous exécutez la commande `terraform init`
    - doit être inclus dans le dépôt de contrôle de version !
    - si un fournisseur est dans le fichier de verrouillage, TF utilisera toujours cette version sauf si vous exécutez `terraform init -upgrade`
- Si une mise à jour est effectuée, examinez les changements 😉 :

![Image](https://mistwire.com/wp-content/uploads/2023/07/CleanShot-2023-07-10-at-14.49.18-1024x684.png)
_Exemple de changement de version du fournisseur AWS dans le fichier de verrouillage_

### Décrire l'architecture basée sur les plugins

Terraform est divisé en 2 parties principales :
- **Noyau Terraform** : un binaire compilé statiquement (écrit en Go). Lorsque vous tapez `terraform` dans le CLI, vous invoquez la fonctionnalité principale :
    - lecture et interpolation des fichiers et modules de configuration
    - gestion de l'état
    - construction d'un graphe de ressources
    - exécution du plan
    - communication avec les plugins

[**Plugins Terraform**](https://developer.hashicorp.com/terraform/plugin/how-terraform-works) : binaires exécutables invoqués par le noyau Terraform via RPC.
- Chaque plugin est conçu pour un service spécifique (comme AWS).
- Tous les fournisseurs et provisionneurs utilisés dans les configurations Terraform sont des plugins
- Les plugins de fournisseurs sont responsables de :
    - Initialisation des bibliothèques pour effectuer des appels API
    - Authentification avec le fournisseur d'infrastructure
    - Définition des mappages de ressources vers des services spécifiques

### Écrire une configuration Terraform utilisant plusieurs fournisseurs

Parfois, vous devrez référencer le même fournisseur pour plusieurs raisons. Dans l'exemple ci-dessous, nous utilisons plusieurs régions au sein d'AWS, donc nous avons besoin d'un mécanisme pour distinguer les deux fournisseurs. Voici l'argument `alias`. Avec lui, vous pouvez attribuer des ressources à des environnements spécifiques :

![Image](https://mistwire.com/wp-content/uploads/2023/07/image.png)
_Exemple d'utilisation de plusieurs fournisseurs avec l'argument alias_

```hcl
provider "aws" {
  profile = "prod"
  region  = "us-east-1"
 }
 
 provider "aws" {
  profile = "prod"
  region  = "us-west-2"
  alias   = "west"
 }
```

### Décrire comment Terraform trouve et récupère les fournisseurs

Les fournisseurs requis sont spécifiés dans le bloc (surprise !) **`required_providers`** imbriqué dans le bloc de niveau supérieur **`terraform`** :

![Image](https://mistwire.com/wp-content/uploads/2023/07/image-3.png)
_Exemple d'utilisation du bloc des fournisseurs requis_

```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.8.0"
    }
  }
}
```

La valeur [source](https://developer.hashicorp.com/terraform/language/providers/requirements#source-addresses) spécifie l'emplacement principal où Terraform peut le télécharger (voir le lien pour les détails sur la syntaxe).

Utilisez les commandes **`terraform version`** (quelle version du noyau et quels plugins sont installés) et **`terraform providers`** (quels fournisseurs sont requis par la configuration) pour obtenir plus d'informations sur les exigences de configuration :

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-185.png)
_Sortie de la commande terraform version_

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-184.png)
_Sortie de la commande terraform providers_

## Utiliser Terraform en dehors du flux de travail principal

Maintenant que nous avons appris les bases de Terraform, le domaine 4 aborde d'autres flux de travail que vous verrez très souvent dans le monde réel.

Ce domaine répond à des questions comme "Si vous avez construit un environnement sans utiliser Terraform, comment transféreriez-vous ces ressources vers un état géré par Terraform ?" et "Que se passe-t-il lorsque tout se casse ?"

### Décrire quand utiliser [terraform import](https://developer.hashicorp.com/terraform/cli/commands/import) pour importer une infrastructure existante dans votre état Terraform (note : ne peut importer qu'une ressource à la fois)

1. Écrivez un bloc de ressource pour cela dans votre configuration
    - le nom de la ressource doit être unique (comme tout bloc de ressource régulier)
2. Exécutez terraform import avec la syntaxe `terraform import [options] <address id>`
    - address id est l'id de la ressource du fournisseur
    - chaque objet distant doit être lié à un seul bloc de ressource dans la configuration terraform
3. Exécutez terraform plan & examinez comment la configuration se compare à la ressource importée
4. Apportez des ajustements à la configuration pour atteindre l'état souhaité

### Utiliser terraform state pour voir l'état de Terraform

- **Utilisez ceci au lieu de modifier directement le fichier d'état**
    - Ne modifiez jamais directement le fichier d'état, jamais, jamais, JAMAIS
- Utilisé pour la gestion avancée de l'état
- Fonctionne avec les fichiers d'état locaux et distants
- Crée une sauvegarde qui ne peut pas être désactivée
- `terraform state -help` pour commencer
- `terraform state list` pour obtenir une vue moins encombrée des ressources sous gestion
- `terraform state list [resource]` pour obtenir des données granulaires sur les ressources (très pratique) :

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-74.png)
_Sortie de la commande terraform state_

### Décrire quand activer la journalisation détaillée et quel est le résultat/la valeur

Vous pouvez générer des journaux pour Terraform Core et les fournisseurs séparément.

- niveaux de journalisation = `TRACE` > `DEBUG` > `INFO` > `WARN` > `ERROR`
- Pour activer la journalisation du noyau, définissez la variable d'environnement `TF_LOG_CORE`=(niveau de journalisation)
    - exemple linux `export TF_LOG_CORE=TRACE`
    - exemple powershell `$env:TF_LOG_CORE=TRACE`
- Pour activer la journalisation du fournisseur, définissez la variable d'environnement `TF_LOG_PROVIDER`=(niveau de journalisation)
    - exemple linux `export TF_LOG_PROVIDER=TRACE`
    - exemple powershell `$env:TF_LOG_PROVIDER=TRACE`
- Pour conserver les journaux, définissez la variable d'environnement :
    - linux `export TF_LOG_PATH=logs.txt`
    - powershell `$env:TF_LOG_PATH=logs.txt`
- Pour annuler la variable d'environnement, réinitialisez les valeurs à null :
    - `export TF_LOG_CORE=""`
    - `export TF_LOG_PROVIDER=""`
    - `export TF_LOG_PATH=""`

![Image](https://www.freecodecamp.org/news/content/images/2023/08/CleanShot-2023-08-01-at-09.29.46-1.png)
_Sortie de la commande terraform refresh_

## Interagir avec les modules Terraform

Le domaine 5 étend vos connaissances de Terraform en introduisant le concept de modules. Beaucoup de gens utilisent Terraform et créent des modules pour faciliter le provisionnement des ressources pour tout le monde. Ne réinventez pas la roue, utilisez des modules !

### Comparer et utiliser différentes options de source de module, y compris le registre public Terraform

![Image](https://www.freecodecamp.org/news/content/images/2023/08/CleanShot-2023-08-02-at-15.07.13.png)
_Section de navigation des modules du registre Terraform_

Un module Terraform est simplement un ensemble de fichiers de configuration Terraform à l'intérieur d'un dossier – rien à craindre. 😊

Chaque configuration Terraform a au moins un module, le *module racine*. Si vous avez des *modules enfants*, le module racine peut faire appel à eux.

Les modules enfants sont simplement des fichiers en dehors du répertoire de travail. Ils peuvent être un dossier sur votre système, dans un dépôt GitHub, un bucket S3, etc. Consultez toutes les [options ici](https://developer.hashicorp.com/terraform/language/modules/sources)

L'argument `source` dans le bloc module indique à Terraform où trouver le code source du module. La syntaxe pour les modules de registre nécessite l'argument `source` est `<namespace>/<name>/<provider>`
- exemple : `terraform-aws-modules/vpc/aws`

Utilisez le [Registre Terraform](https://registry.terraform.io/) pour trouver et utiliser des modules 'publics'
- `terraform init` téléchargera et mettra en cache les modules référencés dans une configuration
- Par défaut, seuls les modules vérifiés sont affichés dans le registre Terraform. Vous pouvez changer cela avec des filtres.
- Les modules dans le registre sont versionnés en utilisant l'argument `version`
- Syntaxe des sources de modules de registre privé = `<hostname>/<namespace>/<name>/<provider>`

![Image](https://www.freecodecamp.org/news/content/images/2023/08/CleanShot-2023-08-02-at-15.40.36.png)
_Exemple d'utilisation d'un module Terraform_

```hcl
module "ec2_instance" {
  source  = "terraform-aws-modules/ec2-instance/aws"
  version = "3.5.0"
  count   = 2

  name = "my-ec2-cluster"

  instance_type          = "t2.micro"
  vpc_security_group_ids = ["sg-12345678"]
  subnet_id              = module.vpc.public_subnets[0]

  tags = {
    Terraform   = "true"
    Environment = "dev"
  }
}
```

### Interagir avec les entrées et sorties de module

Les variables d'entrée vous permettent de personnaliser des aspects des modules Terraform sans altérer le code source du module lui-même
- Chaque variable d'entrée acceptée par un module doit être déclarée en utilisant un bloc `variable`. Comme toujours, les noms de variables doivent être uniques dans le module
- Si une variable n'a pas de valeur par défaut qui lui est assignée, elle est requise

Les blocs de sortie fournissent des informations en retour à partir des ressources générées par le module.

- pour utiliser les informations de sortie dans le 'module appelant' (normalement le module racine), utilisez la syntaxe d'interpolation du bloc de sortie dans le 'module envoyant'

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-75.png)
_sortie du module enfant appelée par le module appelant_

### Décrire la portée des variables dans les modules/modules enfants

Décider ce qui est dans et hors de la portée d'un module peut être difficile. Ne surutilisez pas un module en mettant trop de ressources dans un seul.

Une bonne règle est de le limiter à un type de ressource offert par un fournisseur.

Vous pouvez regrouper l'infrastructure qui est toujours déployée ensemble. Vous pouvez également regrouper les ressources avec le même ensemble de privilèges lorsque cela est possible pour minimiser le rayon d'explosion.

Essayez de séparer les ressources de longue durée des ressources de courte durée : ne mettez pas votre base de données de production dans le même module que vos lambdas de développement. 😂

Les variables sont déclarées dans le module enfant. Si vous voulez des informations du module enfant, vous devez créer un bloc de sortie pour ces informations dans le module enfant & puis l'appeler en utilisant la syntaxe d'interpolation. Vous ne pouvez pas accéder aux informations des ressources du module enfant autrement.

Si vous construisez un module, il est bon de créer des blocs de sortie pour toutes les informations de ressources disponibles, même si vous ne voyez pas une utilisation immédiate pour cela :

![Image](https://www.freecodecamp.org/news/content/images/2023/08/CleanShot-2023-08-07-at-14.19.52.png)
_Disposition exemple des modules racine et enfant_

### Définir la version du module

![Image](https://www.freecodecamp.org/news/content/images/2023/08/CleanShot-2023-08-07-at-16.23.19-1.png)
_Où vérifier les versions des modules_

Tout comme d'autres blocs, les modules peuvent être versionnés. Si vous changez la version du module, vous devrez exécuter `terraform init` à nouveau.
- Il est recommandé de contraindre la version de votre module pour éviter les changements inattendus
- Le versionnement est supporté pour le registre public Terraform & le registre de modules privé de TFC
- Les modules de fichiers locaux ne supportent pas le versionnement

## Utiliser le flux de travail principal de Terraform

Le domaine 6 entre beaucoup plus dans le détail du flux de travail principal de Terraform. Dans le monde réel, c'est le processus que vous ferez encore et encore (et encore !), il est donc important que vous compreniez tous les petits détails.

Faites particulièrement attention à la manière dont les processus interagissent les uns avec les autres et exactement à ce qui se passe lorsque vous utilisez une commande particulière.

### Décrire le [flux de travail Terraform](https://developer.hashicorp.com/terraform/intro/core-workflow) (écrire -> planifier -> créer)

**Écrire** :
- Rédigez votre IaC dans l'éditeur de votre choix (comme VS Code 😉)
- Écrit en Hashicorp Configuration Language (HCL)
- Stockez votre travail dans VCS (comme Git + GitHub)

**Planifier** :
- Initialisez le répertoire de travail avec `terraform init`
- Prévoyez les changements avant de les appliquer avec `terraform plan`
- Faites cela de manière répétée pendant que vous construisez votre configuration pour corriger les erreurs et avoir une boucle de feedback serrée
- Peut sortir et sauvegarder pour plus tard avec `terraform plan -out [nom du plan]`

**Créer** :
- `terraform apply` pour déployer l'infrastructure que vous avez écrite
- Peut appliquer un plan précédemment sauvegardé avec `terraform apply [nom du plan]`
- Recommandé : poussez votre configuration vers un dépôt distant pour la redondance/la sauvegarde

### Initialiser un répertoire Terraform (`terraform init`)

- `init`ialise (vous comprenez ?) un répertoire de travail contenant des fichiers .tf
- C'est la première commande qui doit être exécutée après avoir écrit/cloné une nouvelle configuration. Vous pouvez trouver [les options de commande ici](https://developer.hashicorp.com/terraform/cli/commands/init#general-options)
- Le répertoire de configuration racine est vérifié pour les données de configuration du backend
    - pour mettre à jour le backend, utilisez `-reconfigure` ou `-migrate-state`
- Sources et télécharge les fournisseurs et modules utilisés dans la configuration
- Crée un fichier de verrouillage .terraform.lock.hcl pour fixer les versions des fournisseurs
- Raisons de réinitialiser une configuration :
    - ajout d'un nouveau fournisseur
    - mise à niveau/downgrade de la version d'un fournisseur avec `terraform init -upgrade`
    - ajout d'un nouveau module
    - mise à niveau/downgrade de la version d'un module avec `terraform init -upgrade`
    - changement de l'emplacement du backend (fichier d'état)

### Valider une configuration Terraform (`terraform validate`)

Connaître les limitations ! Cela fait :
- Valide les fichiers de configuration locaux
- Vérifie la validité syntaxique
- Vérifie la cohérence interne
- Vérifie la correction des noms d'attributs, des types de valeurs et des types d'arguments attendus

Cela ne fait PAS :
- Accéder aux services distants (état distant, API des fournisseurs, dépendances en amont, etc...)
- Vérifier avec le fournisseur de backend pour assurer la cohérence externe

### Générer et examiner un plan d'exécution (`[terraform plan](https://developer.hashicorp.com/terraform/cli/commands/plan)`)

Cela crée un plan d'exécution pour prévisualiser les changements que Terraform souhaite apporter à votre environnement.

Voici les étapes :
- Lit l'état actuel (le cas échéant) des objets distants sous gestion pour s'assurer que l'état est à jour
- Compare la configuration actuelle à l'état précédent et note les changements
- Propose des changements qui feront correspondre l'environnement distant à la configuration

Vous pouvez utiliser `terraform plan -help` pour voir toutes les options, et `terraform plan -out [nom du plan]` pour créer un fichier à examiner/utiliser plus tard.

- Utilisez `terraform plan -refresh-only` pour détecter la dérive entre votre configuration et l'environnement réel
- Ne change pas l'environnement, vous pouvez l'exécuter plusieurs fois
- <span style="color: green;">+</span> la ressource sera créée
- <span style="color: red;">-</span> la ressource sera détruite
- <span style="color: GoldenRod;">~</span> la ressource sera mise à jour sur place
- <span style="color: GoldenRod;">-/+</span> la ressource sera détruite & recréée


![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-127.png)
_création de 30 nouvelles ressources_

### Exécuter les changements d'infrastructure (`terraform apply`)

- Provisions, modifie et détruit (recrée) les ressources dans un environnement
- Exécute les actions proposées d'un `terraform plan`
- N'affectera que les ressources sous gestion
- L'exécuter sans un plan le fait exécuter automatiquement un plan, puis l'exécuter
- Vous pouvez passer un plan précédemment généré avec `terraform apply -out=[nom du plan]`
- `terraform apply -auto-approve` contourne la vérification manuelle 'yes' post-plan
- `terrafrom apply [nom du plan]` pour exécuter un plan précédemment sauvegardé

### Détruire l'infrastructure gérée par Terraform (`terraform destroy`)

- Vous ne devinerez jamais ce que fait cette commande 😂
- Détruit toute l'infrastructure **sous gestion** par Terraform (rien d'autre)
- Le nettoyage automatisé est meilleur car vous *oubliez toujours* de supprimer quelque chose lorsque vous le construisez manuellement
- Soyez prudent avec `terraform destroy -auto-approve`
- `terraform apply -destroy` fait également la même chose

![Image](https://www.freecodecamp.org/news/content/images/2023/08/CleanShot-2023-08-16-at-13.07.22.png)
_Êtes-vous vraiment, vraiment sûr ?!?!_

### Appliquer la mise en forme et les ajustements de style à une configuration (terraform fmt)

- Formate et style votre code pour une meilleure lisibilité
- Ne corrige PAS vos erreurs
- Liste les fichiers qu'il met à jour
- Très utile 😀

![Image](https://www.freecodecamp.org/news/content/images/2023/08/CleanShot-2023-08-16-at-14.19.16.png)
_Comment fonctionne terraform fmt_

## Implémenter et maintenir l'état

L'état est LA CHOSE LA PLUS IMPORTANTE dans tout environnement géré par Terraform. Sans votre fichier d'état, vous allez passer une mauvaise journée.

Le domaine 7 passe en revue les différents types d'état, comment le déplacer et comment le protéger.

### Décrire le backend [`local` par défaut](https://developer.hashicorp.com/terraform/language/v1.1.x/settings/backends/local)

Terraform stocke et référence l'*état* de tous les environnements gérés par Terraform.

Le fichier de configuration est ce que nous voulons que l'environnement ressemble, le *fichier d'état* est un mappage un à un des ressources provisionnées au fichier de configuration.

- Le backend `local` :
    - stocke l'état sur le système de fichiers local
    - verrouille cet état en utilisant les API système
    - effectue les opérations localement

Le fichier d'état par défaut est nommé `terraform.tfstate` et réside dans le répertoire de travail. Si vous ne spécifiez pas de backend, Terraform utilise le backend local par défaut.

Vous POUVEZ spécifier explicitement le backend local si vous souhaitez avoir un meilleur contrôle sur l'emplacement du fichier d'état, les considérations de migration d'état futures, etc.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/CleanShot-2023-08-17-at-11.01.06.png)
_État local par défaut défini explicitement_

```hcl
terraform {
  backend "local" {
    path = "terraform.tfstate"
  }
}
```

### Décrire le [verrouillage d'état](https://developer.hashicorp.com/terraform/language/state/locking)

Les données d'état (le fichier d'état) sont la source de vérité pour Terraform et sont donc *très* importantes. À ce titre, elles doivent être protégées contre plusieurs scénarios de corruption de fichiers et de perte de données.

Les backends sont responsables du stockage de l'état et de la fourniture d'une API pour le verrouillage de l'état. Le verrouillage de l'état est *facultatif* mais fortement recommandé dans les environnements multi-utilisateurs.
- Vous pouvez récupérer manuellement l'état distant avec `terraform state pull`
- Vous pouvez écrire manuellement l'état avec `terraform state push`.... mais ne le faites jamais sans une supervision et un guidage appropriés et des sauvegardes.

Le verrouillage de l'état empêche plusieurs utilisateurs d'apporter des modifications à un environnement géré simultanément (potentiellement en corrompant l'état). Le verrouillage se produit automatiquement sur toutes les opérations d'écriture d'état potentielles.

- Vous *pouvez* ignorer le verrouillage de l'état avec `-force` mais ne le faites pas 😅
- Vous pouvez également `terraform force-unlock [LOCK_ID]` si le déverrouillage échoue, mais c'est un cas d'utilisation d'urgence en cas de bris de verre

Tous les backends ne supportent pas le verrouillage ! Local, TFC, AWS S3 (avec quelques ajustements), et plusieurs autres le font ([voir la documentation pour savoir lesquels le font/ne le font pas](https://developer.hashicorp.com/terraform/language/settings/backends/configuration)).

### Gérer les méthodes d'authentification backend et d'intégration cloud

Lorsque vous avez un backend d'état stocké ailleurs que `local`, vous devrez avoir une forme d'authentification - ce sont des informations très sensibles qui doivent être protégées !

Chaque backend a son propre mécanisme d'authentification (par exemple, des clés d'accès pour AWS).

Quelques autres choses à garder à l'esprit :

- Les arguments utilisés dans le corps du bloc sont spécifiques au type de backend choisi
- Si vous souhaitez changer l'emplacement du backend, vous devrez commencer par `terraform init -reconfigure`
- `terraform login [hostname]` est utilisé pour obtenir et sauvegarder un jeton API de TFC, TFE, ou un autre hôte qui offre des services Terraform
- Si vous ne fournissez pas explicitement un nom d'hôte, la commande utilise par défaut TFC à `app.terraform.io`
- Par défaut, Terraform extrait & sauvegarde le jeton API en texte brut dans `credentials.tfrc.json` - cela peut être modifié pour d'autres systèmes de gestion des secrets
- Pour configurer un bloc backend, ajoutez un `backend` imbriqué dans le bloc de niveau supérieur `terraform` :

![Image](https://www.freecodecamp.org/news/content/images/2023/08/CleanShot-2023-08-19-at-15.15.46.png)
_État distant défini_

```hcl
terraform {
  backend "remote" {
    organization = "example_corp"
    
    workspaces {
      name = "my-app-prod"
    }
  }
}
```

### Différencier les options de backend d'état distant

Terraform dispose d'une sélection intégrée de backends et le backend configuré doit être disponible dans la version de Terraform que vous utilisez. C'est pourquoi il est important de versionner tout dans vos configurations !

Vous n'avez pas besoin de configurer un backend lorsque vous utilisez TFC car il gère automatiquement l'état dans les espaces de travail associés à la configuration. Si votre configuration inclut un bloc `cloud`, elle ne peut pas avoir de bloc `backend`.

### Gérer la dérive des ressources et l'état de Terraform

`terraform plan -refresh-only`
- Crée un plan qui met à jour l'état pour correspondre aux changements apportés en dehors de terraform
- Bon pour la détection de dérive
- Ne propose aucune action pour annuler les changements

`terraform apply -refresh-only`
- Met à jour le fichier d'état pour accepter les changements apportés manuellement dans l'environnement
- Ne modifie **PAS** le fichier de configuration ! Si vous ne mettez pas à jour la configuration avec les nouveaux changements, alors le prochain `terraform apply` de cette configuration rétablira l'environnement à l'état d'origine

### Décrire la configuration du bloc [`backend`](https://developer.hashicorp.com/terraform/language/settings/backends/configuration) et de l'[intégration cloud](https://developer.hashicorp.com/terraform/language/settings/terraform-cloud)

- Définit où terraform stocke le fichier d'état pour un répertoire de travail
- Le fichier d'état est la source de vérité pour les ressources sous gestion terraform et est donc extrêmement important (je l'ai peut-être déjà dit 😉)
- Par défaut, terraform utilise `local` qui stocke le fichier d'état sur le disque local
- `remote` est l'autre type de backend qui couvre tout le reste (TFC, S3, etc...)
- Limites :
    - 1 config, 1 bloc `backend`
    - Impossible d'utiliser l'interpolation (donc nous ne pouvons pas utiliser de variables)
- Configurations partielles
    - Omettre certains arguments à fournir à l'exécution
    - Utile pour les scripts d'automatisation & les scénarios CI
- Lorsque vous utilisez Terraform Cloud, vous n'avez pas besoin de configurer un backend car TFC gère l'état dans l'espace de travail associé à la configuration
- Le bloc `cloud` est imbriqué dans le bloc `terraform`
- Limites :
    - 1 config, 1 bloc `cloud`
    - Si la configuration inclut un bloc `cloud`, elle ne peut pas avoir également un bloc `backend`
    - Impossible d'utiliser l'interpolation
    - Voir [paramètres cloud](https://developer.hashicorp.com/terraform/cli/cloud/settings) pour plus d'informations

### Comprendre la gestion des secrets dans les fichiers d'état

- Le fichier d'état peut contenir beaucoup de secrets !!!
    - identifiants de ressource
    - noms d'utilisateur/mots de passe de la base de données
    - clés privées
    - numéro de téléphone personnel d'Andrew Brown

Vous devez donc le traiter comme vous le feriez pour les mots de passe de votre entreprise. Par défaut, l'état local est stocké en texte brut sous forme de JSON. Vous pouvez marquer les informations sensibles dans vos fichiers de configuration comme telles avec l'argument `sensitive = true`.
- masqué dans la sortie CLI, mais toujours dans le fichier d'état en texte brut (c'est pourquoi il est important de verrouiller le fichier d'état)

Utilisez un backend qui chiffre et protège votre fichier d'état contre les accès non autorisés.

- TFC chiffre l'état au repos & en transit
- Activez le chiffrement si vous utilisez S3 (& utilisez le verrouillage d'état !)
- Terraform ne persiste pas l'état sur le disque local lorsque l'état distant est utilisé

## Lire, générer et modifier la configuration

Le domaine 8 vous enseigne davantage sur les fichiers de configuration et comment exploiter pleinement HCL. Comme tout langage de programmation, HCL peut être refactorisé pour faciliter la compréhension et garder votre code DRY (Don't Repeat Yourself).

### Démontrer l'utilisation des [variables](https://developer.hashicorp.com/terraform/language/values/variables) et des [sorties](https://developer.hashicorp.com/terraform/language/values/outputs)

- Analogies de programmation :
    - [Variables d'entrée](https://developer.hashicorp.com/terraform/language/values/variables) = arguments de fonction
    - [Valeurs de sortie](https://developer.hashicorp.com/terraform/language/values/outputs)   = valeurs de retour de fonction
    - [Valeurs locales](https://developer.hashicorp.com/terraform/language/values/locals)    = variables locales de fonction
- Chaque variable d'entrée acceptée par un module doit être déclarée en utilisant un bloc `variable` :
![Picture1](https://www.freecodecamp.org/news/content/images/2023/08/Picture1.png)
![Picture2](https://www.freecodecamp.org/news/content/images/2023/08/Picture2.png)
![Picture3](https://www.freecodecamp.org/news/content/images/2023/08/Picture3.png)
    - Les noms de variables peuvent être n'importe quel nom valide _sauf_ `source`, `version`, `providers`, `count`, `for_each`, `lifecycle`, `depends_on`, ou `locals`
    - Ordre de priorité des entrées : défauts < variables d'environnement < fichier terraform.tfvars < fichier terraform.tfvars.json < .auto.tfvars < ligne de commande (-var & -var-file)
        - note de côté : terraform.tfvars est la manière la plus populaire de manipuler les variables utilisées dans la nature
- De la même manière, chaque valeur de sortie doit être déclarée en utilisant un bloc `output`
    - Dans le module racine, la sortie est affichée à l'utilisateur
    - Dans un module enfant, la sortie peut être utilisée pour accéder à une valeur par le module racine (`module.<NOM_DU_MODULE>.<NOM_DE_LA_SORTIE>`)
    - Les sorties ne s'affichent que sur `terraform apply`, pas sur `terraform plan`
    - `terraform output` affichera vos sorties sans exécuter un `apply`
    - `terraform output <NOM>` pour extraire une valeur spécifique
    - marquer une valeur de sortie comme sensible supprime la valeur dans le CLI pendant un `terraform apply`, mais PAS dans le fichier d'état ou un `terraform output <NOM>`
    - si vous marquez une variable comme `sensitive` mais PAS une sortie pour cette variable, elle générera une erreur
![CleanShot-2023-08-29-at-19.44.57](https://www.freecodecamp.org/news/content/images/2023/08/CleanShot-2023-08-29-at-19.44.57.png)

### Décrire les meilleures pratiques pour l'injection sécurisée de secrets

- Marquer les valeurs sensibles comme `sensitive`
- Ne mettez jamais de valeurs de secrets réelles dans un fichier .tf car elles seraient enregistrées dans le contrôle de source
    - Les mots de passe, jetons API, jetons d'accès, etc... doivent être obfuscés
- Ne vérifiez jamais votre fichier d'état dans le contrôle de source (même raison que ci-dessus)
- Utilisez des variables d'environnement en définissant `TF_VAR_<NOM>`
![CleanShot-2023-08-29-at-20.04.06](https://www.freecodecamp.org/news/content/images/2023/08/CleanShot-2023-08-29-at-20.04.06.png)
- Si vous utilisez Terraform Cloud, utilisez les variables d'environnement pour l'espace de travail approprié :
![CleanShot-2023-08-29-at-20.08.55](https://www.freecodecamp.org/news/content/images/2023/08/CleanShot-2023-08-29-at-20.08.55.png)
- Utilisez une solution de gestion des secrets comme Vault
    - Suivez [ce tutoriel](https://developer.hashicorp.com/terraform/tutorials/secrets/secrets-vault) pour avoir une idée de l'injection de secrets dans Terraform en utilisant Vault

### Comprendre l'utilisation des [types de collection et structurels](https://developer.hashicorp.com/terraform/language/v1.1.x/expressions/type-constraints#complex-types)

- Les types de collection sont une collection d'_un type_ de regroupement
    - Tous les éléments d'une collection doivent être du même type `list(string)` est différent de `list(number)`
    - 3 types de collections :
        - `list(...)` séquence d'éléments ordonnés (en commençant par 0)
![CleanShot-2023-08-30-at-15.43.39](https://www.freecodecamp.org/news/content/images/2023/08/CleanShot-2023-08-30-at-15.43.39.png)
        - `map(...)` séquence de paires clé/valeur séparées par une virgule. Peut utiliser de manière déroutante à la fois = ou : comme séparateur k/v
![CleanShot-2023-08-30-at-15.42.37](https://www.freecodecamp.org/news/content/images/2023/08/CleanShot-2023-08-30-at-15.42.37.png)
        - `set(...)` une collection de valeurs uniques, non ordonnées, non répétitives
- Les types structurels permettent de regrouper des éléments de _plusieurs types_
    - 2 types de types structurels :
        - `object({<KEY> = <TYPE>, ...})` attributs nommés où chacun a son propre type
        - `tuple([<TYPE>, <TYPE>, ...])` séquence d'éléments ordonnés (en commençant par 0)
![CleanShot-2023-08-30-at-16.18.32](https://www.freecodecamp.org/news/content/images/2023/08/CleanShot-2023-08-30-at-16.18.32.png)

### Créer et différencier les configurations `resource` et `data`

- Les fournisseurs peuvent accéder à la fois aux ressources et aux sources de données (exemples du fournisseur AWS :
![CleanShot-2023-08-31-at-14.29.32](https://www.freecodecamp.org/news/content/images/2023/08/CleanShot-2023-08-31-at-14.29.32.png)
- Vous pouvez interroger les ressources que vous avez créées dans Terraform (via l'exportation des références d'attributs) :
![CleanShot-2023-08-31-at-14.31.19](https://www.freecodecamp.org/news/content/images/2023/08/CleanShot-2023-08-31-at-14.31.19.png)
- Et également effectuer des recherches de données pour les ressources existantes qui n'ont pas été créées avec Terraform
![CleanShot-2023-08-31-at-14.33.19](https://www.freecodecamp.org/news/content/images/2023/08/CleanShot-2023-08-31-at-14.33.19.png)
- Faites le tutoriel [Query data sources](https://developer.hashicorp.com/terraform/tutorials/configuration-language/data-sources?variants=terraform-workflow%3Atfc)

### Utiliser l'adressage des ressources et les paramètres des ressources pour connecter les ressources ensemble

- Syntaxe du chemin de la ressource
    - `[module path][resource info]`
- Syntaxe du chemin du module
    - `module.<NOM_DU_MODULE>[index du module optionnel]`
- Syntaxe de la spécification de la ressource
    - `resource_type.user_defined_name[index optionnel]`
- Types de valeurs nommées :
    - Ressources `<TYPE_DE_RESSOURCE>.<NOM>`
        - si `count` est utilisé, la référence est une liste accessible avec [N]
        - si `for_each` est utilisé, la référence est une carte accessible avec ["clé"]
    - Variables d'entrée `var.<NOM>`
    - Locales `local.<NOM>`
    - Sorties des modules enfants `module.<NOM_DU_MODULE>`
        - mêmes règles `count` et `for_each` que les ressources
    - Blocs de données `data.<TYPE_DE_DONNÉES>.<NOM>`
        - mêmes règles `count` et `for_each` que les ressources
    - Informations sur le système de fichiers/espace de travail
        - `path.module` emplacement de l'expression (ne pas utiliser dans les opérations d'écriture)
        - `path.root` emplacement du module racine
        - `terraform.workspace` espace de travail actuellement sélectionné
    - Valeurs 'locales' du bloc
        - `count.index`
        - `each.key`/`each.value`
        - `self`

### Utiliser HCL et les fonctions Terraform pour écrire la configuration

- Terraform dispose d'un certain nombre de fonctions intégrées pour manipuler les valeurs, les chaînes, etc...
![CleanShot-2023-08-31-at-15.21.35](https://www.freecodecamp.org/news/content/images/2023/08/CleanShot-2023-08-31-at-15.21.35.png)
    - [Passez-les en revue ici](https://developer.hashicorp.com/terraform/language/functions)
    - Pas nécessaire pour l'examen (je ne pense pas ?) mais elles faciliteront votre vie lorsque vous utiliserez réellement HCL
- Faites les tutoriels [dynamic operations with functions](https://developer.hashicorp.com/terraform/tutorials/configuration-language/functions) et [create dynamic expressions](https://developer.hashicorp.com/terraform/tutorials/configuration-language/expressions)

### Décrire la gestion des dépendances intégrée (basée sur l'ordre d'exécution)

- Terraform génère un graphe de dépendances pour déterminer quelles ressources doivent être construites en 1er, 2ème, 3ème, etc...
    - `depends_on` peut être utilisé pour modifier les dépendances
    - Le bloc `lifecycle` ainsi que `create_before_destroy` et `prevent_destroy` sont des outils supplémentaires dans la boîte à outils du cycle de vie
- Les éléments sans dépendances sont construits en parallèle pour accélérer le processus de provisionnement
    - Par défaut, jusqu'à 10 opérations simultanées peuvent être exécutées en même temps
    - Cela peut être changé avec le flag `-parallelism` sur les commandes `plan`, `apply`, & `destroy`
- Vous pouvez voir cette carte de dépendances en utilisant la commande `terraform graph` et un visualiseur comme [Graphviz](https://www.graphviz.org/) (ou http://www.webgraphviz.com/ si vous êtes paresseux comme moi)

## Comprendre les capacités de Terraform Cloud

Le domaine 9 (le dernier domaine !) est entièrement consacré à Terraform Cloud. Il s'agit du backend distant géré par HashiCorp et offre un niveau gratuit (jusqu'à 500 ressources gérées au moment où j'ai écrit cet article).

Tout environnement de niveau production utilisera un backend distant avec verrouillage d'état, donc connaître le fonctionnement de Terraform Cloud est excellent non seulement pour l'examen, mais aussi pour l'expérience professionnelle dans le monde réel.

### Expliquer comment Terraform Cloud aide à gérer l'infrastructure

Terraform Cloud - est une offre SaaS qui :
- Gère les exécutions Terraform dans un environnement cohérent et fiable
- Inclut un accès facile à l'état partagé et aux données secrètes
- Contrôles d'accès pour approuver les changements d'infrastructure
- Un registre privé pour partager les modules Terraform
- Contrôles de politique détaillés pour régir le contenu des configurations Terraform
- Stockage d'état distant
- Intégrations de contrôle de version
- Autorisations personnalisées pour les espaces de travail
- Flux de travail flexibles - CLI, UI, VCS, ou l'API
- Collaboration - révision/commentaire des plans avant d'exécuter les changements d'infrastructure
- Journaux d'audit - qui l'a cassé

Terraform Enterprise est une distribution auto-hébergée de Terraform Cloud. Ce n'est pas au programme de l'examen, mais [ici](https://developer.hashicorp.com/terraform/enterprise) se trouvent les documents pour les exigences, les architectures de référence et les guides d'installation.

### Décrire comment Terraform Cloud permet la collaboration et la gouvernance

Terraform Cloud utilise les **Équipes** comme paradigme de regroupement. Les équipes sont composées d'utilisateurs dans une organisation donnée. Chaque équipe peut avoir un jeton API qui n'est pas associé à un utilisateur spécifique.

L'organisation accorde des autorisations d'espace de travail aux utilisateurs et aux équipes. L'équipe des propriétaires :
- Est la 1ère équipe créée
- Ne peut pas être supprimée ou laissée vide
- Peut créer/supprimer d'autres équipes
- Gère les autorisations au niveau de l'organisation pour les autres équipes
- Peut voir la liste complète des équipes (Visibles et Secrètes)

Terraform Cloud applique des **Politiques** aux exécutions en utilisant le _Langage de Politique Sentinel_. Après avoir défini une politique, elles sont ajoutées à des ensembles de politiques que Terraform Cloud peut ensuite appliquer.
- Faites le tutoriel [Enforce a policy with Sentinel](https://developer.hashicorp.com/terraform/tutorials/cloud-get-started/policy-quickstart).

## Conclusion

C'est tout ! 😂 Je suis confiant que si vous révisez tout le matériel ici, faites les tutoriels spécifiés dans la préparation à l'examen, et assistez à notre [Terraform Beginner Bootcamp](https://terraform.cloudprojectbootcamp.com/), vous serez bien préparé pour passer et réussir l'examen Terraform Associate.

Bonne chance !