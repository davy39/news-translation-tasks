---
title: Guide du débutant sur Terraform – Infrastructure-as-Code en pratique
subtitle: ''
author: Oluwatobi
co_authors: []
series: null
date: '2025-01-03T18:21:03.282Z'
originalURL: https://freecodecamp.org/news/a-beginners-guide-to-terraform-infrastructure-as-code-in-practice
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1735900327439/09832fb8-8cc0-4182-b70a-5f54ee6fce7d.jpeg
tags:
- name: Terraform
  slug: terraform
- name: Infrastructure as code
  slug: infrastructure-as-code
- name: Beginner Developers
  slug: beginners
- name: Terraweekchallenge
  slug: terraweekchallenge
seo_title: Guide du débutant sur Terraform – Infrastructure-as-Code en pratique
seo_desc: A beginner's guide to learning Terraform
---

Au fil des années, le développement cloud a connu un changement de paradigme majeur. De nouvelles applications plus complexes sont déployées rapidement dans le cloud pour minimiser les temps d'arrêt. Et à travers tout cela, le concept d'Infrastructure-as-Code et divers outils ont émergé pour simplifier le processus de développement d'applications.

Vous vous demandez peut-être : qu'est-ce que l'Infrastructure-as-Code ? Comment améliore-t-il le processus et l'expérience de développement, et où Terraform intervient-il ? Eh bien, nous explorerons tout cela et plus encore dans ce guide. Mais avant de commencer, voici quelques prérequis :

* Connaissance de base du cloud et des terminologies cloud

* Accès à un PC pour implémenter des exemples de code

* Un compte GCP

Avec cela, commençons.

### Voici ce que nous allons couvrir :

1. [Aperçu de l'Infrastructure as Code](#heading-apercu-de-linfrastructure-as-code-iac)

2. [Qu'est-ce que Terraform ?](#heading-quest-ce-que-terraform)

3. [Avantages de Terraform](#heading-avantages-de-terraform)

4. [Termes courants utilisés dans Terraform](#heading-termes-courants-utilises-dans-terraform)

5. [Projet de démonstration : Comment écrire une configuration Terraform](#heading-projet-de-demonstration-comment-ecrire-une-configuration-terraform)

6. [Conclusion](#heading-conclusion)

## Aperçu de l'Infrastructure as Code (IaC)

L'Infrastructure as Code fait référence à la génération d'outils et d'applications d'infrastructure cloud avec un document de configuration basé sur du code. Ce processus, lorsqu'il est exécuté, automatise la séquence et le processus de création de bases de données, de machines virtuelles et de serveurs. Cela améliore l'expérience utilisateur en réduisant la fréquence des déploiements manuels de services cloud, surtout pour plusieurs services identiques.

Il existe deux approches distinctes pour l'Infrastructure as Code : l'approche `Impérative` et l'approche `Déclarative`.

Lorsque vous utilisez l'approche Déclarative pour la génération d'infrastructure, vous décrivez simplement les résultats attendus/souhaités pour l'infrastructure à générer, puis l'outil IaC que vous utilisez détermine comment produire ce résultat.

D'autre part, l'approche Impérative implique de spécifier les étapes exactes nécessaires pour atteindre l'état d'infrastructure souhaité. Bien que l'approche Impérative semble plus adaptée aux configurations d'infrastructure complexes, l'approche Déclarative peut fonctionner tout aussi bien.

Certains outils sont capables des deux approches, tandis que d'autres ne sont adaptés qu'à l'une ou l'autre. Parmi les outils IaC populaires utilisés dans le monde, on trouve [Terraform IaC](https://www.terraform.io/), [AWS Cloud Formation](https://aws.amazon.com/cloudformation/), [Ansible](https://www.redhat.com/en/ansible-collaborative), et [Pulumi](https://www.pulumi.com/), [Chef](https://www.chef.io/glossary/what-is-infrastructure-as-code), parmi d'autres.

Comme le nom l'indique – infrastructure as **code** – le code créant l'infrastructure est écrit dans divers langages de modèle dans l'espace IaC. Les langages de modèle populaires incluent JSON, YAML, ARM template, HCL, Heat Scripts, et ainsi de suite.

Vous pouvez également utiliser des outils de script pour exécuter l'infrastructure cloud. Certains des plus populaires incluent Bash et PowerShell. Ceux-ci sont parfois préinstallés sur la plupart des ordinateurs personnels.

Parmi tous ces outils, Terraform se distingue pour diverses raisons – et c'est celui que nous allons examiner dans cet article.

## Qu'est-ce que Terraform ?

Terraform est un outil open source développé par HashiCorp en 2014. Il a évolué au fil des années et sert désormais d'outil d'infrastructure agnostique du cloud qui vous permet de créer une infrastructure sur plusieurs fournisseurs de services cloud.

Terraform propose également [Terraform Cloud](https://app.terraform.io/session), un outil logiciel en tant que service basé sur le cloud. Il permet le déploiement basé sur le cloud d'outils cloud, au lieu d'utiliser les anciennes méthodes locales que nous avions dans l'outil CLI Terraform obsolète.

De plus, comme d'autres outils IaC qui utilisent des langages de modèle, le framework de modèle utilisé pour créer une infrastructure dans Terraform est le langage de modèle HashiCorp (HCL).

## Avantages de Terraform

Je vais maintenant souligner certains des avantages de l'utilisation de Terraform en tant qu'ingénieur cloud, ainsi que le rôle clé de l'outil dans l'écosystème cloud.

### **1. Approche Déclarative**

Cette approche de l'automatisation de l'infrastructure cloud garantit que toute l'infrastructure requise à déployer (bases de données, serveurs, etc.) est explicitement indiquée et exécutée en conséquence. Cela aide à éviter les conflits.

### **2. Gestion des conflits**

En plus de ses capacités efficaces d'automatisation des outils cloud, Terraform possède certaines propriétés robustes de détection et de gestion des conflits. L'une des façons dont il gère les conflits est via la fonction `Terraform plan`. Cette fonction met en évidence tout conflit perçu ou potentiel d'orchestration de l'infrastructure, ce qui permet une correction facile avant le déploiement. Je discuterai de cela plus en détail dans les sections suivantes.

### **3. Agnostique du cloud**

Terraform est un fournisseur de services d'automatisation multi-usage et multi-cloud avec des capacités efficaces d'automatisation de l'infrastructure sur les principaux fournisseurs de services cloud (AWS, GCP et Azure). Il permet également l'automatisation hybride et inter-fournisseurs.

### **4. Convivial**

Terraform est l'un des plus grands outils d'automatisation cloud avec les plus grandes communautés d'utilisateurs. Il dispose de nombreux tutoriels adaptés aux débutants qui vous aident à vous familiariser rapidement avec l'outil. Voici un lien vers sa [documentation](https://developer.hashicorp.com/terraform/docs) pour que vous puissiez approfondir.

### **5. Capacités de gestion de fichiers**

Terraform crée automatiquement une sauvegarde locale des états d'automatisation sur votre ordinateur local pour assurer un rappel immédiat et une gestion des fichiers en cas de problème. Il offre également des options de sauvegarde à distance vers des fournisseurs de services cloud à distance si nécessaire.

### **6. Contrôle de version**

Tout comme le système de contrôle de version Git, Terraform dispose d'un système de contrôle de version intégré qui vous permet de suivre les modifications apportées à un fichier Terraform. Il vous permet également de revenir à des versions précédentes de votre code si des erreurs sont présentes dans la version actuelle, par exemple.

### **7. Réutilisabilité du code**

Terraform offre une grande variété de modèles de code pour une réutilisation facile sur sa page de documentation pour les développeurs.

Maintenant que nous avons mis en évidence les avantages de Terraform, apprenons quelques terminologies courantes utilisées dans Terraform et ce qu'elles signifient.

## Termes courants utilisés dans Terraform

Avant de commencer à utiliser Terraform, vous devez être familiarisé avec certains termes clés qui reviennent souvent. Voici ce que vous devez savoir :

1. **Providers** : dans Terraform, un Provider est une interface de programmation qui permet à Terraform d'interagir avec diverses API et services cloud. Par exemple, vous utiliseriez un provider pour interfacer avec un fournisseur de services cloud comme GCP ou Azure.

2. **Modules** : Les modules sont spécifiquement créés dans le framework Terraform et servent de composants réutilisables qui vous permettent d'orchestrer facilement les services cloud. Vous pouvez également stocker des informations clés concernant les services cloud dans un module, puis les modifier pour garantir l'unicité en utilisant des variables de module.

3. **Resources** : Les ressources dans Terraform font référence aux composants d'infrastructure cloud à créer. Des exemples incluent les réseaux cloud, les machines virtuelles, les zones de disponibilité et d'autres infrastructures.

4. **State** : Le concept de state dans Terraform forme la base de son efficacité. State suit la configuration actuelle de vos ressources d'infrastructure et contient des détails sur chaque ressource que Terraform a créée, modifiée ou supprimée. Le système de contrôle de version de Terraform l'utilise pour suivre les modifications que vous apportez à un fichier de code et utilise ces informations pour détruire et provisionner l'infrastructure si nécessaire.

5. **Workspace** : un Workspace fonctionne de manière similaire à un système de contrôle de version, car il crée une sorte de contrainte autour d'un fichier de travail. Les Workspaces vous permettent de gérer plusieurs instances d'une seule configuration d'infrastructure de manière propre et isolée dans le même backend. Vous pouvez utiliser des workspaces pour séparer les environnements comme le développement, la mise en scène et la production tout en utilisant la même configuration Terraform.

## Projet de démonstration : Comment écrire une configuration Terraform

Dans cette section, nous allons approfondir l'écriture de notre premier fichier Terraform pour orchestrer une machine virtuelle de programme Google Cloud avec seulement quelques lignes de code. Mais avant de commencer, nous allons discuter des différentes commandes que vous devez comprendre avant d'implémenter le projet de démonstration.

### Commandes courantes de Terraform

* `Terraform init` : Cette commande initialise l'outil Terraform et télécharge les fichiers essentiels spécifiques au fournisseur de cloud. Elle établit également une connexion entre Terraform et le fournisseur de cloud en question. Dans notre cas, il s'agit de GCP et du fournisseur Terraform.

* `Terraform fmt` : Cette commande assure automatiquement un formatage et une indentation optimaux du code. Elle garantit une exécution ordonnée du code et minimise les erreurs.

* `Terraform plan` : Cette commande décrit les étapes d'exécution du code Terraform et détecte les erreurs qui peuvent survenir pendant le processus d'exécution. Elle met également en évidence les erreurs dans le code Terraform qui peuvent empêcher l'exécution. Enfin, elle fonctionne avec la gestion de l'état Terraform pour détecter tout changement d'état et désapprovisionner ou générer des services cloud supplémentaires si nécessaire.

* `Terraform apply` : Cette commande exécute l'état planifié de Terraform mis en œuvre par la commande `Terraform plan`.

* `Terraform destroy` : Cette commande est la dernière commande dans le schéma Terraform qui est utilisée pour désactiver ou détruire tous les services cloud créés en utilisant la commande Terraform apply. Il est important de noter que vous devez exécuter les commandes listées ci-dessus séquentiellement pour garantir que votre infrastructure soit créée correctement.

### Création d'une machine virtuelle GCP alimentée par IaC

Maintenant que vous avez appris ces commandes importantes, testons-les toutes en créant notre toute première machine virtuelle GCP alimentée par IaC.

Dans votre éditeur de code, tapez le code suivant :

```plaintext
provider "google" {
  project = "votre-id-de-projet-gcp"  # Remplacez par votre ID de projet GCP
  region  = "us-central1"          
  zone    = "us-central1-a"        
}
```

Ce code met en évidence le fournisseur de cloud que nous utilisons pour générer les ressources cloud dont nous avons besoin. Dans notre cas, il s'agit du programme Google Cloud. Le nom qui lui est attribué est simplement « google ». D'autres fournisseurs de cloud comme AWS et Azure sont « aws » et « azure » respectivement.

La deuxième ligne identifie l'identifiant d'abonnement GCP, qui est unique à chaque compte GCP (et aide à faciliter une intégration précise). **Vous devez utiliser le vôtre dans l'espace prévu.**

Vous devrez également inclure une région de ressource appropriée et une zone de disponibilité des ressources. Cela sert de base physique pour la machine virtuelle que nous allons créer afin de pouvoir l'exécuter. Dans ce scénario, j'ai choisi la région centrale des États-Unis et la zone de disponibilité 1-a, respectivement. Vous pouvez en lire plus [ici](https://cloud.google.com/compute/docs/regions-zones) sur les régions cloud et les zones de disponibilité.

```plaintext
resource "google_compute_instance" "vm_instance" {
  name         = "example-vm"      
  machine_type = "e2-medium"          

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11" 
    }
  }
```

L'extrait de code ci-dessus spécifie la ressource de calcul exacte qui sera orchestrée, qui dans notre cas est une instance de machine virtuelle codée comme « vm_instance ». `'example-vm'` est le nom que nous voulons attribuer à la machine virtuelle que nous allons créer pour ce projet. Il est important de noter que le nom de la machine virtuelle doit également être unique. Le type de machine virtuelle que nous avons choisi était le type VM E2 (usage général)-medium. Vous pouvez obtenir plus d'informations sur les types de machines virtuelles [ici](https://cloud.google.com/compute/docs/general-purpose-machines).

En allant plus loin, nous spécifions également le système d'exploitation amorcé attendu (« boot_disk »), qui est une image du système d'exploitation Debian Linux version 11 dans mon cas.

```plaintext
  network_interface {
    network = "default"  # Attacher au réseau VPC par défaut
    access_config {
      
    }
  }

output "instance_ip" {
  value = google_compute_instance.vm_instance.network_interface[0].access_config[0].nat_ip
}
```

Pour compléter la création de notre machine virtuelle, nous devons configurer un réseau virtuel pour permettre l'accès à distance à la VM. Le bloc d'interface réseau connecte la machine virtuelle au réseau VPC (Virtual Private Cloud) par défaut fourni par GCP. Nous ne pourrons pas interfacer avec notre machine virtuelle sans le réseau VPC. Le bloc de sortie affiche également l'adresse IP d'accès par défaut dans le terminal, que nous pouvons utiliser pour nous connecter à la machine virtuelle.

Voici le code final attendu :

```plaintext

provider "google" {
  project = "votre-id-de-projet-gcp"  # Remplacez par votre ID de projet GCP
  region  = "us-central1"          
  zone    = "us-central1-a"       
}

resource "google_compute_instance" "vm_instance" {
  name         = "example-vm"         
  machine_type = "e2-medium"          

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"  
    }
  }

  network_interface {
    network = "default"  # Attacher au réseau VPC par défaut
    access_config {
    
    }
  }

output "instance_ip" {
  value = google_compute_instance.vm_instance.network_interface[0].access_config[0].nat_ip
}
```

Ensuite, nous allons exécuter ce code en utilisant les commandes mises en évidence dans l'image ci-dessous :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1734796321588/29561c5c-3908-43d1-8579-53a3de33358a.png align="center")

La commande `terraform -v` confirme que Terraform a été installé avec succès sur le terminal. Le résultat attendu sera la version de l'outil Terraform installé.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1734796340539/149f5f24-90eb-4777-8ae3-18acdd3c758a.png align="center")

La commande suivante exécutée est la fonction `terraform init` qui initialise une communication avec le fournisseur de services cloud, qui dans notre cas est GCP. Toutes les dépendances nécessaires sont également installées.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1734796301342/bd886728-dfdb-49f7-bcbf-1e53ff203b35.png align="center")

La commande `terraform fmt` est également exécutée pour garantir un formatage et une indentation adéquats du code. Ensuite, la commande `terraform plan` est exécutée séquentiellement.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1734889731467/bb454ec4-47e4-40a4-84fc-91c580fb77bb.png align="center")

Sur l'image ci-dessus, vous pouvez voir les étapes que Terraform prévoit d'utiliser pour générer la machine virtuelle attendue.

En cas d'exécution réussie de Terraform plan, nous exécuterons ensuite la fonction `terraform apply` pour exécuter les étapes décrites par Terraform plan.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1734796355772/d1d8f9f9-98a9-4ab0-be00-60a9b2b993a9.png align="center")

Cela générera une invite demandant une confirmation de l'exécution de Terraform comme montré ci-dessus. Taper « Yes » permettra à l'opération de se poursuivre sans problème.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1734796361770/a08254b0-878a-4681-b6ce-f6b0a9a83bc6.png align="center")

En cas d'exécution réussie, un message de succès sera affiché comme montré ci-dessus. Avec cela, nous avons créé notre infrastructure cloud avec juste du code. La commande `terraform destroy` peut ensuite être appelée pour supprimer les machines virtuelles créées.

## Conclusion

Dans cet article, vous avez appris les bases de l'Infrastructure as Code. Nous avons discuté de Terraform, de ses avantages et de certaines de ses fonctionnalités et commandes clés. Nous avons également illustré son utilisation dans un projet de démonstration.

Pour approfondir vos connaissances, vous pouvez [consulter la documentation de Terraform](https://developer.hashicorp.com/terraform?product_intent=terraform) pour plus d'exemples de code. Je vous recommande également d'utiliser vos nouvelles connaissances pour automatiser un projet avec des utilisations réelles.

N'hésitez pas à me contacter pour tout commentaire ou question. Vous pouvez également consulter mes autres articles [ici](http://portfolio-oluwatobi.netlify.app). Jusqu'à la prochaine fois, continuez à coder !