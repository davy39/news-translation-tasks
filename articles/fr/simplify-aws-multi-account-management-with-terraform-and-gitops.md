---
title: Comment simplifier la gestion multi-compte AWS avec Terraform et GitOps
subtitle: ''
author: Nitheesh Poojary
co_authors: []
series: null
date: '2024-11-26T14:56:18.081Z'
originalURL: https://freecodecamp.org/news/simplify-aws-multi-account-management-with-terraform-and-gitops
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1730239127065/317aa4dd-aba9-4a9e-8abb-7cacfbd0e672.png
tags:
- name: AWS
  slug: aws
- name: Terraform
  slug: terraform
- name: gitops
  slug: gitops
seo_title: Comment simplifier la gestion multi-compte AWS avec Terraform et GitOps
seo_desc: 'In the past, in the world of cloud computing, a company''s journey often
  began with a single AWS account. In this unified space, development and testing
  environments coexisted, while the production environment lived in a separate account.

  This arrange...'
---

Dans le passé, dans le monde de l'informatique en nuage, le parcours d'une entreprise commençait souvent par un seul compte AWS. Dans cet espace unifié, les environnements de développement et de test coexistaient, tandis que l'environnement de production vivait dans un compte séparé.

Cet arrangement pouvait bien fonctionner dans les premiers jours, mais à mesure qu'une entreprise grandit et que ses besoins deviennent plus spécialisés, la simplicité d'un seul compte peut commencer à montrer ses limites. La demande d'environnements dédiés va commencer à augmenter, et bientôt, cette entreprise peut avoir besoin de créer de nouveaux comptes AWS pour des fonctions spécifiques comme la sécurité, DevOps et la facturation.

Avec chaque nouveau compte, la complexité de la gestion des politiques de sécurité et de la journalisation dans toute l'infrastructure croît de manière exponentielle. Les architectes cloud de ces entreprises réaliseront alors qu'ils ont besoin d'une approche plus centralisée et rationalisée pour gérer cette présence numérique en expansion.

### Présentation d'AWS Organizations

AWS Organizations est un service conçu pour rationaliser la gestion des comptes AWS. Cet outil puissant vous permet de regrouper plusieurs comptes AWS sous une seule bannière. Avec AWS Organizations, vous pouvez facilement créer des unités organisationnelles, appliquer des politiques de contrôle de service et gérer les autorisations dans tous les comptes. Cela simplifie non seulement le processus, mais améliore également la sécurité et la conformité.

Les processus de facturation d'AWS Organizations ont également été optimisés grâce à la centralisation des paiements et à la génération de rapports de dépenses complets pour chaque compte. Cette clarté améliorée dans la gestion financière facilite l'allocation des ressources de manière plus efficace et la stratégie pour l'expansion future.

AWS Organizations peut aider votre équipe à appliquer de manière cohérente les politiques de sécurité, à activer la journalisation dans tous les comptes et à rationaliser les tâches administratives. L'infrastructure cloud est désormais une machine bien organisée, sécurisée et efficace, prête à soutenir les ambitions d'une entreprise pour les années à venir.

Dans cet article, nous discuterons de ce que signifie avoir une configuration multi-compte et de son fonctionnement. Je vous guiderai à travers tout, de l'architecture de déploiement à la création d'une unité organisationnelle et au-delà.

## Table des matières

* [Composants de la configuration multi-compte](#heading-composants-de-la-configuration-multi-compte)
    
* [Comment automatiser une stratégie multi-compte](#heading-comment-automatiser-une-strategie-multi-compte)
    
* [Structure de l'organisation AWS](#heading-structure-de-lorganisation-aws)
    
* [Architecture de déploiement](#heading-architecture-de-deploiement)
    
* [Aperçu des composants CI/CD](#heading-apercu-des-composants-cicd)
    
* [Processus de déploiement CI/CD expliqué](#heading-processus-de-deploiement-cicd-explique)
    
* [Comment automatiser la création de la zone d'atterrissage](#heading-comment-automatiser-la-creation-de-la-zone-datterrissage)
    
* [Comment créer une unité organisationnelle](#heading-comment-creer-une-unite-organisationnelle)
    
* [Comment automatiser l'attachement du contrôle de Control Tower à l'OU](#heading-comment-automatiser-lattachement-du-controle-de-control-tower-a-lou)
    
* [Conclusion](#heading-conclusion)
    

## **Composants de la configuration multi-compte**

Tout d'abord, examinons en détail les différents composants qui constituent une stratégie multi-compte AWS :

* **AWS Control Tower**
    
* **Zone d'atterrissage**
    
* **Unité organisationnelle AWS**
    
* **AWS SSO**
    
* **Contrôles de Control Tower**
    
* **Politiques de contrôle de service (SCP)**
    

### **Qu'est-ce qu'AWS Control Tower ?**

AWS Control Tower est un service complet qui vous permet de configurer et de gérer efficacement un environnement AWS multi-compte. Il est conçu sur la base des meilleures pratiques des experts AWS et respecte les normes et exigences de l'industrie.

En utilisant AWS Control Tower, vous pouvez vous assurer que votre environnement AWS est sécurisé, conforme et bien organisé, facilitant ainsi la gestion et la scalabilité.

#### Fonctionnalités d'AWS Control Tower :

* L'informatique cloud peut être sûre que tous les comptes sont conformes aux réglementations de l'entreprise, et les équipes distribuées peuvent créer rapidement de nouveaux comptes AWS.
    
* Vous pouvez appliquer les meilleures pratiques, les normes et les exigences réglementaires avec des contrôles préconfigurés.
    
* Vous pouvez automatiser la configuration de votre environnement AWS avec des plans conformes aux meilleures pratiques. Ces plans couvrent divers aspects tels que la structure multi-compte, la gestion de l'identité et des accès, ainsi que le flux de travail de provisionnement de compte.
    
* Il vous permet de gérer les configurations de nouveaux comptes ou existants, d'obtenir une visibilité sur l'état de conformité et d'appliquer des contrôles à grande échelle.
    

### **Qu'est-ce qu'une zone d'atterrissage dans AWS ?**

Une zone d'atterrissage vous aide à configurer rapidement un environnement cloud en utilisant l'automatisation, y compris des paramètres préconfigurés qui suivent les meilleures pratiques de l'industrie pour assurer la sécurité de vos comptes AWS.

Le point de départ sert de base à votre entreprise pour initier et mettre en œuvre efficacement des charges de travail et des applications, garantissant un environnement d'infrastructure sécurisé et fiable.

Il existe deux choix pour créer une zone d'atterrissage. Tout d'abord, vous pouvez utiliser le tableau de bord AWS Control Tower. Ensuite, vous pouvez créer une zone d'atterrissage personnalisée. Si vous êtes nouveau dans AWS, je recommande d'utiliser AWS Control Tower pour créer une zone d'atterrissage.

![AWS Landing Zone](https://cdn.hashnode.com/res/hashnode/image/upload/v1732137800622/f72dbf02-fa34-4004-999d-71a2af33f90b.png align="center")

Si vous optez pour la création d'une zone d'atterrissage via le tableau de bord Control Tower, les éléments suivants seront mis en œuvre dans votre zone d'atterrissage :

* Un environnement multi-compte avec des organisations AWS.
    
* La gestion de l'identité via le répertoire par défaut dans AWS IAM Identity Center.
    
* L'accès fédéré aux comptes en utilisant IAM Identity Center.
    
* La journalisation centralisée à partir d'AWS CloudTrail et AWS Config stockée dans Amazon Simple Storage Service (Amazon S3).
    
* Les audits de sécurité inter-comptes activés en utilisant IAM Identity Center.
    

### **Qu'est-ce qu'une unité organisationnelle AWS ?**

L'utilisation de plusieurs comptes vous permet de mieux soutenir vos objectifs de sécurité et les opérations de votre entreprise.

AWS Organizations permet la gestion basée sur les politiques de plusieurs comptes AWS. Lorsque vous créez de nouveaux comptes, vous pouvez les organiser en unités organisationnelles (OU), qui sont des regroupements de comptes fournissant la même application ou service.

![AWS Organizational Units](https://cdn.hashnode.com/res/hashnode/image/upload/v1732137833615/6eebb3ab-94d0-4286-8dc4-9d3ae297e186.png align="center")

#### Avantages de l'utilisation des OU :

* Les comptes sont des unités de protection de la sécurité. Les dangers potentiels et les menaces de sécurité peuvent être contenus dans un compte sans affecter les autres.
    
* Les équipes ont différentes missions et besoins en ressources. La configuration de différents comptes empêche les équipes de s'interférer les unes avec les autres, comme elles pourraient le faire si elles utilisaient le même compte.
    
* L'isolement des magasins de données à un compte réduit le nombre de personnes qui ont accès et peuvent gérer le magasin de données.
    
* Le concept multi-compte vous permet de générer des éléments facturables séparés pour les divisions commerciales, les équipes fonctionnelles ou les utilisateurs individuels.
    
* Les quotas AWS sont configurés par compte. La séparation des charges de travail en différents comptes donne à chaque compte un quota individuel.
    

### **Qu'est-ce qu'AWS IAM Identity Center ?**

AWS IAM Identity Center fournit une solution centralisée pour gérer l'accès à plusieurs comptes AWS et applications métiers.

![AWS identity center](https://cdn.hashnode.com/res/hashnode/image/upload/v1732137875918/349673f8-1a09-4bcc-b1db-6a898d3d06b5.png align="center")

Cette méthode offre une fonctionnalité de connexion unique qui permet aux employés d'accéder à tous les comptes et applications assignés à partir d'une seule identité.

Le portail utilisateur web personnalisé fournit une vue centralisée des rôles assignés de l'utilisateur dans les comptes AWS.

Pour une expérience d'authentification uniforme, les utilisateurs peuvent se connecter en utilisant l'interface de ligne de commande AWS, les SDK AWS ou l'application mobile AWS Console avec leurs identifiants de répertoire.

Vous pouvez également configurer et superviser les identifiants utilisateur dans le magasin d'identités d'IAM Identity Center, ou vous pouvez vous connecter à votre fournisseur d'identité existant, tel que Microsoft Active Directory, Okta, etc.

### **Contrôles de Control Tower (Guardrails)**

Les contrôles sont des règles de gouvernance prédéfinies pour la sécurité, les opérations et la conformité. Vous pouvez les sélectionner et les appliquer à l'échelle de l'entreprise ou à des groupes spécifiques de comptes.

![ControlTowerControls](https://cdn.hashnode.com/res/hashnode/image/upload/v1732137911519/5dac3db6-15e6-476b-9b50-a1597a02fe84.png align="center")

Les contrôles peuvent être détectifs, préventifs ou proactifs et peuvent être obligatoires ou facultatifs.

* Tout d'abord, nous avons des contrôles détectifs (par exemple, détecter si l'accès en lecture publique aux compartiments Amazon S3 est autorisé).
    
* Ensuite, les contrôles préventifs établissent l'intention et empêchent le déploiement de ressources qui ne sont pas conformes à vos politiques (par exemple, activer AWS CloudTrail dans tous les comptes).
    
* Enfin, les capacités de contrôle proactif utilisent les [hooks AWS CloudFormation](https://aws.amazon.com/blogs/mt/proactively-keep-resources-secure-and-compliant-with-aws-cloudformation-hooks/) pour identifier et bloquer proactivement le déploiement CloudFormation de ressources qui ne sont pas conformes aux contrôles que vous avez activés. Par exemple, les développeurs ne peuvent pas créer de compartiments S3 capables de stocker des données dans un état non chiffré au repos.
    

### **Politiques de contrôle de service (SCP)**

Les SCP sont une fonctionnalité de l'organisation qui vous permet de définir les autorisations maximales pour les comptes membres au sein de l'organisation.

![Service Control Policies](https://cdn.hashnode.com/res/hashnode/image/upload/v1732137972306/80d0782c-0801-4548-9c0c-d4a11d43ecbe.png align="center")

Il existe de nombreuses fonctions et caractéristiques d'une SCP :

* Si une SCP refuse une action sur un compte, aucune entité dans le compte ne peut effectuer cette action, même si ses autorisations IAM le permettent.
    
* Empêche l'arrêt ou la suppression de la journalisation CloudTrail.
    
* Empêche la suppression des journaux de flux VPC.
    
* Interdit aux comptes AWS de quitter l'organisation.
    
* Empêche les modifications d'AWS GuardDuty.
    
* Empêche le partage de ressources en utilisant AWS Resource Access Manager (RAM) soit en externe soit entre environnements.
    
* Empêche la désactivation du chiffrement par défaut d'Amazon EBS.
    
* Empêche les téléchargements d'objets non chiffrés Amazon S3.
    
* Et empêche les utilisateurs et rôles IAM dans les comptes concernés de créer certains types de ressources si la demande n'inclut pas les balises spécifiées.
    

## **Comment automatiser une stratégie multi-compte**

Maintenant que vous êtes familiarisé avec les concepts clés d'une stratégie multi-compte dans AWS, plongeons plus profondément dans les parties pratiques.

Dans les sous-sections à venir, nous couvrirons comment vous pouvez configurer une AWS Control Tower, créer une zone d'atterrissage et créer automatiquement des unités organisationnelles (OU). Je vous guiderai également à travers la configuration des contrôles de Control Tower, souvent appelés garde-fous, pour maintenir la sécurité, la conformité et la gouvernance de votre environnement AWS.

Une fois ce déploiement terminé, nous aurons une solution qui inclut les composants suivants :

* Crée une OU AWS Organizations nommée Core dans la structure racine de l'organisation.
    
* Crée et ajoute deux comptes partagés à l'OU Security : le compte Log Archive et le compte Audit.
    
* Crée un répertoire natif cloud dans IAM Identity Center, avec des groupes prêts à l'emploi et un accès unique.
    
* Applique tous les contrôles préventifs requis pour faire respecter les politiques.
    
* Applique les contrôles détectifs requis pour identifier les violations de configuration.
    

## **Structure de l'organisation AWS**

Nous allons créer et mettre en œuvre la structure organisationnelle suivante. Vous pouvez ajouter ou modifier des OU selon vos besoins.

![AWS Organization Structure](https://cdn.hashnode.com/res/hashnode/image/upload/v1732138006995/423e54cd-bf74-4aef-a2a3-d52294482ca0.png align="center")

## **Architecture de déploiement**

J'utiliserai Terraform Cloud et GitHub Actions pour automatiser l'ensemble du processus. Cette architecture s'applique à tous les trois composants, y compris les comptes principaux, les zones d'atterrissage et la création d'unités organisationnelles (OU) et les contrôles.

![Deployment Architecture](https://cdn.hashnode.com/res/hashnode/image/upload/v1732138041912/0cba5af0-69ea-4ae9-986e-c1608d3d5c21.avif align="left")

### Aperçu des composants CI/CD

#### **1. GitHub Actions**

GitHub Actions est une plateforme CI/CD qui vous permet d'automatiser votre pipeline de construction, de test et de déploiement. Vous pouvez créer des flux de travail qui construisent et testent automatiquement chaque demande de tirage vers votre dépôt, garantissant que les modifications de code sont vérifiées avant la fusion.

GitHub Actions vous permet également de déployer les demandes de tirage fusionnées en production, rationalisant le processus de publication et réduisant les erreurs.

L'utilisation de GitHub Actions améliore votre flux de travail de développement, améliore la qualité du code et accélère la livraison de nouvelles fonctionnalités et mises à jour.

#### **2. Terraform Cloud**

Terraform Cloud est une plateforme de HashiCorp pour gérer et exécuter votre code Terraform. Elle offre des outils et des fonctionnalités qui améliorent la collaboration entre les développeurs et les ingénieurs DevOps, rendant le travail d'équipe plus efficace.

Avec Terraform Cloud, vous pouvez simplifier et rationaliser votre flux de travail, facilitant la gestion des tâches d'infrastructure complexes et des déploiements. La plateforme offre également des fonctionnalités de sécurité robustes pour protéger votre code et votre infrastructure, gardant votre produit sécurisé tout au long de son cycle de vie.

### **Processus de déploiement CI/CD expliqué**

Les ingénieurs DevOps sont responsables de l'écriture du code Terraform, puis de la création d'une demande de tirage. J'ai ajouté plusieurs cas de test pour mon code Terraform dans le fichier `terraform-plan.yml`, qui s'exécute uniquement sur la branche de fonctionnalité.

* **Vérifier les variables d'environnement** : Assure que toutes les variables d'environnement requises sont définies.
    
* **Vérifier le code** : Utilise l'action `actions/checkout` pour vérifier le dépôt.
    
* **Vérifier la validation** : Vérifie que la validation a réussi.
    
* **Validation** : Vérifie le code Terraform pour toute erreur de syntaxe. Les demandes de tirage contiennent des modifications proposées dans le code, permettant aux membres de l'équipe de les examiner et de les fusionner dans la branche principale. Une fois les demandes de tirage fusionnées avec la branche principale, tous les cas de test sont relancés et la zone d'atterrissage est créée via Terraform Cloud.
    

## **Ce qu'il faut savoir avant de configurer Control Tower**

Avant de commencer le processus de configuration pour AWS Control Tower, il est important de bien comprendre les limitations associées à Control Tower et de considérer certains points clés.

* Lors de la configuration d'une zone d'atterrissage, il est important de choisir votre région principale. Une fois que vous avez fait une sélection, vous ne pourrez pas changer votre région principale.
    
* Si vous avez l'intention d'établir une tour de contrôle sur un compte AWS existant qui fait déjà partie d'une unité organisationnelle (OU) existante, vous ne pourrez pas l'utiliser. Pour continuer, vous devrez créer un nouveau compte AWS qui n'est associé à aucune unité organisationnelle (OU).
    
* Dans le cadre du processus de création de Control Tower, vous devrez créer des comptes obligatoires tels que le compte Log Archive et les comptes Audit. Des e-mails spécifiques aux comptes sont requis.
    
* Afin de configurer la zone d'atterrissage dans le compte de gestion, il est essentiel de s'assurer que vous avez souscrit aux services suivants dans le compte de gestion :
    
    * S3, EC2, SNS, VPC, CloudFormation, CloudTrail, CloudWatch, AWS Config, IAM, AWS Lambda
        
* La configuration de base d'AWS Control Tower ne couvre que quelques services avec des options de personnalisation limitées : IAM Identity Center, CloudTrail, Config, certaines règles de configuration et certains SCP dans AWS Organizations.
    
* La mise en œuvre d'IAM Identity Center est limitée au compte de gestion d'une organisation.
    
* AWS Control Tower met en œuvre des limitations de concourance, permettant uniquement une opération à la fois.
    
* Notez que certaines régions AWS ne prennent pas en charge le fonctionnement de certains contrôles dans AWS Control Tower. Cela est dû au fait que les régions spécifiées manquent de la fonctionnalité sous-jacente nécessaire pour prendre en charge les opérations requises.
    

### **Comment créer une Control Tower**

Créer une Control Tower signifie configurer une zone d'atterrissage. La zone d'atterrissage AWS nécessite la création de deux nouveaux comptes membres : le compte Audit et le compte Log Archive. Vous aurez besoin de deux adresses e-mail uniques pour ces comptes.

Nous allons gérer ce processus en utilisant des modules Terraform. Pour garder les choses simples et claires, nous allons diviser le projet en plusieurs modules. Un module créera les deux comptes principaux. Un autre module gérera la configuration de la zone d'atterrissage. Le module final créera des unités organisationnelles (OU) et appliquera des contrôles de Control Tower pour assurer la gouvernance et la conformité.

## **Comment automatiser la création de la zone d'atterrissage**

Lorsque vous exécutez ce code, l'OU Core et deux comptes sont créés sous l'OU Core. J'ai mentionné deux dépôts pour chaque composant : un pour déployer les ressources AWS comme la zone d'atterrissage, l'OU et les contrôles de Control Tower, et un autre pour le module Terraform.

Un *module Terraform* est un ensemble de fichiers de configuration standard dans un répertoire spécifique. Les modules Terraform regroupent des ressources pour une tâche spécifique, ce qui réduit la quantité de code nécessaire pour des composants d'infrastructure similaires.

J'ai importé les modules de création de compte principal et de création de zone d'atterrissage dans le même fichier [`main.tf`](https://github.com/nitheeshp-irl/aws-landing-zone/blob/main/main.tf). Cela est nécessaire car la création de la zone d'atterrissage dépend du module de compte principal. Les inclure ensemble garantit que toutes les dépendances sont gérées correctement et que le processus de déploiement est efficace.

Cette méthode simplifie également la structure du projet et aide à éviter les problèmes potentiels liés à la gestion de ces composants séparément.

L'API AWS Control Tower [`CreateLandingZone`](https://docs.aws.amazon.com/controltower/latest/APIReference/API_CreateLandingZone.html) nécessite une version de zone d'atterrissage et un fichier manifeste en tant que paramètres d'entrée. Voici un exemple de manifeste **LandingZoneManifest.json**.

```json
{
   "governedRegions": ["us-west-2","us-west-1"],
   "organizationStructure": {
       "security": {
           "name": "CORE"
       },
       "sandbox": {
           "name": "Sandbox"
       }
   },
   "centralizedLogging": {
        "accountId": "222222222222",
        "configurations": {
            "loggingBucket": {
                "retentionDays": 60
            },
            "accessLoggingBucket": {
                "retentionDays": 60
            },
            "kmsKeyArn": "arn:aws:kms:us-west-1:123456789123:key/e84XXXXX-6bXX-49XX-9eXX-ecfXXXXXXXXX"
        },
        "enabled": true
   },
   "securityRoles": {
        "accountId": "333333333333"
   },
   "accessManagement": {
        "enabled": true
   }
}
```

Ce module configure la zone d'atterrissage AWS en utilisant `landingzone_manifest_template`. La version de la zone d'atterrissage et l'ID du compte administrateur sont donnés via des variables. Ce module crée également plusieurs rôles IAM requis pour la configuration de la zone d'atterrissage.

J'ai défini une variable locale `landingzone_manifest_template`, qui est un modèle JSON pour configurer la zone d'atterrissage. Ce modèle JSON a plusieurs paramètres importants :

```yaml
provider "aws" {
  region = var.region
}

locals {
  landingzone_manifest_template = <<EOF
{
    "governedRegions": ${jsonencode(var.governed_regions)},
    "organizationStructure": {
        "security": {
            "name": "Core"
        }
    },
    "centralizedLogging": {
         "accountId": "${module.aws_core_accounts.log_account_id}",
         "configurations": {
             "loggingBucket": {
                 "retentionDays": ${var.retention_days}
             },
             "accessLoggingBucket": {
                 "retentionDays": ${var.retention_days}
             }
         },
         "enabled": true
    },
    "securityRoles": {
         "accountId": "${module.aws_core_accounts.security_account_id}"
    },
    "accessManagement": {
         "enabled": true
    }
}
EOF
}

module "aws_core_accounts" {
  source = "https://github.com/nitheeshp-irl/terraform_modules/aws_core_accounts_module"

  logging_account_email  = var.logging_account_email
  logging_account_name   = var.logging_account_name
  security_account_email = var.security_account_email
  security_account_name  = var.security_account_name
}

module "aws_landingzone" {
  source                  = "https://github.com/nitheeshp-irl/blog_terraform_modules/aws_landingzone_module"
  manifest_json           = local.landingzone_manifest_template
  landingzone_version     = var.landingzone_version
  administrator_account_id = var.administrator_account_id
}
```

* **Régions gouvernées** : Spécifie les régions gouvernées par la zone d'atterrissage.
    
* **Structure de l'organisation** : Définit la structure de sécurité avec un compte de sécurité dédié.
    
* **Journalisation centralisée** : Configure la journalisation, en spécifiant l'ID du compte et les politiques de conservation des journaux.
    
* **Rôles de sécurité** : Spécifie l'ID du compte pour les rôles de sécurité.
    
* **Gestion des accès** : Active la gestion des accès.
    
* **Comptes principaux** : Le code des comptes principaux, également défini dans le même fichier, est ce qui configure les comptes AWS essentiels pour la journalisation et la sécurité.
    

Vous pouvez trouver le code complet ici : [https://github.com/nitheeshp-irl/aws-landing-zone](https://github.com/nitheeshp-irl/aws-landing-zone).

## **Comment créer une unité organisationnelle**

Lorsque vous exécutez ce code, différentes unités organisationnelles (OU) sont créées selon les spécifications dans le fichier [variable](https://github.com/nitheeshp-irl/aws-orgunits/blob/main/variables.auto.tfvars).

Une fois la configuration de la zone d'atterrissage terminée, nous pouvons créer une OU selon nos besoins métiers. Cela prendra le nom de l'OU à partir du fichier de variables et créera l'OU.

```json
aws_region = "us-east-2"

organizational_units = [
  {
    unit_name = "apps"
  },
  {
    unit_name = "infra"
  },
  {
    unit_name = "stagingpolicy"
  },
  {
    unit_name = "sandbox"
  },
  {
    unit_name = "security"
  }
]
```

Vous pouvez voir le code ici :

* [AWS Organizational Units (OUs) Terraform Repo](https://github.com/nitheeshp-irl/aws-orgunits)
    
* [AWS Organizational Units Terraform Module Path](https://github.com/nitheeshp-irl/blog-terraform-modules/tree/main/aws_org_module)
    

## **Comment automatiser l'attachement du contrôle de Control Tower à l'OU**

Une fois que vous avez créé les unités OU en utilisant le dépôt ci-dessus, ce dépôt appliquera les contrôles de Control Tower aux OU.

Après avoir créé les objets requis, vous pouvez attacher des contrôles à l'OU si vous en avez besoin. Voici le fichier [`main.tf`](https://github.com/nitheeshp-irl/controltower_controls/blob/main/main.tf) :

```yaml
provider "aws" {
  region = var.region
}

module "aws_controls" {
  source = "https://github.com/nitheeshp-irl/blog_terraform_modules/awscontroltower-controls_module"

  aws_region = var.aws_region
  controls   = var.controls
}
```

Nous avons utilisé des modules Terraform pour créer des ressources AWS.

Voici les variables de contrôle :

```json
aws_region = "us-east-2"


controls = [
  {
    control_names = [
      "AWS-GR_ENCRYPTED_VOLUMES",
      "AWS-GR_EBS_OPTIMIZED_INSTANCE",
      "AWS-GR_EC2_VOLUME_INUSE_CHECK",
      "AWS-GR_RDS_INSTANCE_PUBLIC_ACCESS_CHECK",
      "AWS-GR_RDS_SNAPSHOTS_PUBLIC_PROHIBITED",
      "AWS-GR_RDS_STORAGE_ENCRYPTED",
      "AWS-GR_RESTRICTED_COMMON_PORTS",
      "AWS-GR_RESTRICTED_SSH",
      "AWS-GR_RESTRICT_ROOT_USER",
      "AWS-GR_RESTRICT_ROOT_USER_ACCESS_KEYS",
      "AWS-GR_ROOT_ACCOUNT_MFA_ENABLED",
      "AWS-GR_S3_BUCKET_PUBLIC_READ_PROHIBITED",
      "AWS-GR_S3_BUCKET_PUBLIC_WRITE_PROHIBITED",
    ],
    organizational_unit_names = ["infra", "apps"]
  }
]
```

Vous pouvez voir le code ici :

* [Terraform Repo pour créer des contrôles de Control Tower](https://github.com/nitheeshp-irl/controltower_controls)
    
* [Module Terraform pour créer des contrôles de Control Tower](https://github.com/nitheeshp-irl/blog-terraform-modules/tree/main/awscontroltower-controls_module)
    

## **Conclusion**

Naviguer dans une stratégie multi-compte dans AWS peut être difficile, mais avec AWS Control Tower et une approche structurée, cela devient gérable.

En utilisant AWS Control Tower, votre équipe peut s'assurer que leurs environnements AWS sont sécurisés, conformes et bien organisés. La configuration automatisée, la gouvernance à grande échelle et la gestion centralisée via AWS Organizations fournissent une base solide pour l'infrastructure cloud.

La mise en œuvre d'une zone d'atterrissage via AWS Control Tower offre un point de départ sécurisé et standardisé, permettant un déploiement plus rapide et une meilleure gouvernance. L'utilisation d'unités organisationnelles (OU) sépare les comptes en fonction des besoins métiers, améliorant la sécurité et l'efficacité opérationnelle. AWS IAM Identity Center simplifie la gestion des accès, offrant une expérience d'authentification unifiée sur plusieurs comptes et applications.

Les politiques de contrôle de service (SCP) aident à maintenir la sécurité et la conformité en veillant à ce que toutes les ressources suivent les règles de l'organisation. Terraform Cloud et GitHub Actions facilitent le déploiement des ressources, offrant un pipeline CI/CD fluide pour gérer les modifications de l'infrastructure.