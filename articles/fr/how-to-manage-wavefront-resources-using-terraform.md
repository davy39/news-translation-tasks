---
title: Comment gérer les ressources Wavefront à l'aide de Terraform
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-01-04T16:46:06.000Z'
originalURL: https://freecodecamp.org/news/how-to-manage-wavefront-resources-using-terraform
coverImage: https://www.freecodecamp.org/news/content/images/2020/12/wavefront-terraform.png
tags:
- name: Infrastructure as code
  slug: infrastructure-as-code
- name: metrics
  slug: metrics
- name: Microservices
  slug: microservices
- name: performance
  slug: performance
- name: Terraform
  slug: terraform
seo_title: Comment gérer les ressources Wavefront à l'aide de Terraform
seo_desc: 'By Siben Nayak

  In my previous article, I wrote about metrics and how they help you gain visibility
  into the operational health of your hardware and software systems.

  Wavefront is a high-performance streaming analytics platform that supports 3D observ...'
---

Par Siben Nayak

Dans mon [article](https://www.freecodecamp.org/news/microservice-observability-metrics/) précédent, j'ai écrit sur les métriques et comment elles aident à obtenir une visibilité sur la santé opérationnelle de vos systèmes matériels et logiciels.

**Wavefront** est une plateforme d'analyse de streaming haute performance qui prend en charge l'observabilité 3D (métriques, histogrammes, traces/portées).

Elle peut évoluer pour supporter des taux d'ingestion de données et des charges de requêtes très élevés. Vous pouvez collecter des données à partir de nombreux services et sources dans l'ensemble de votre pile d'applications, et examiner les détails des données précédemment collectées par Wavefront.

**Terraform** est un outil open-source "Infrastructure as Code", créé par HashiCorp.

C'est un outil de codage _déclaratif_ et permet aux développeurs d'utiliser un langage de configuration de haut niveau appelé HCL (HashiCorp Configuration Language) pour décrire l'état final souhaité pour l'infrastructure.

Cette infrastructure peut être dans le cloud ou sur site. Il génère ensuite un plan pour atteindre cet état final et exécute le plan pour créer l'infrastructure.

Dans cet article, nous allons voir comment utiliser Terraform pour écrire du code qui construira automatiquement des tableaux de bord et des alertes dans Wavefront. Cela est vraiment utile pour maintenir une culture DevOps dans votre équipe, où toute l'infrastructure de surveillance est maintenue sous forme de code et vérifiée dans votre système de contrôle de version tel que GitHub.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-21.png)

## Comment installer Terraform

Selon votre système d'exploitation, les instructions d'installation de [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli) varieront. Cet article couvre les instructions pour l'installer sur macOS.

L'approche recommandée pour l'installer sur macOS est d'utiliser le gestionnaire de paquets Homebrew.

### Installer Terraform

Vérifiez que vous avez Homebrew installé, comme ceci :

```
$ brew --version

Homebrew/homebrew-core (git revision fe68a; last commit 2020-10-15)
Homebrew/homebrew-cask (git revision 4a2c25; last commit 2020-10-15)
```

Si ce n'est pas le cas, vous pouvez installer Homebrew avec la commande suivante :

```
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

Ensuite, installez Terraform avec les commandes suivantes :

```
$ brew tap hashicorp/tap
$ brew install hashicorp/tap/terraform
```

### Vérifier l'installation de Terraform

Pour vérifier que Terraform est correctement installé, ouvrez une autre session de terminal et essayez une commande Terraform.

```
$ terraform --help

Usage: terraform [global options] <subcommand> [args]

The available commands for execution are listed below.The primary workflow commands are given first, followed byless common or more advanced commands.
```

## Comment obtenir un jeton API

Pour permettre à Terraform d'accéder à votre installation Wavefront, vous devrez lui fournir un jeton d'accès. Ce jeton peut être trouvé dans la section des jetons API de votre compte.

Allez à _Icône d'engrenage > Nom du compte > Accès API_

![Image](https://www.freecodecamp.org/news/content/images/2020/12/Screenshot-2020-12-26-at-12.49.23-PM.png)
_Obtenir votre jeton API Wavefront_

## Comment configurer un projet Terraform

Tout d'abord, créez un nouveau dossier pour votre projet Terraform :

```
$ mkdir wavefront-terraform
```

Un projet Terraform habituel contient 3 fichiers principaux :

1. **versions.tf** – ce fichier contient la déclaration du fournisseur Terraform qui spécifie la version du plugin à utiliser
2. **variables.tf** – ce fichier contient les variables que vous pouvez référencer dans votre code principal Terraform
3. **main.tf** – comme son nom l'indique, ce fichier contient le code réel nécessaire pour construire les ressources

Créez un fichier **versions.tf** dans le dossier du projet et ajoutez le code suivant :

<script src="https://gist.github.com/theawesomenayak/f7e6599433e1e8caf0c4aa08171f5331.js"></script>

Ensuite, exécutez la commande `terraform init` pour initialiser le fournisseur Wavefront :

```
$ terraform init
```

Cela télécharge le fichier `terraform-wavefront-provider-<version>` et le place dans un dossier `.terraform` dans le dossier du projet actuel.

Ensuite, créez un fichier **main.tf** dans le dossier du projet et ajoutez le code suivant :

<script src="https://gist.github.com/theawesomenayak/ee05304d5dc2bb0674c112f232185a36.js"></script>

Avec la configuration terminée, nous sommes maintenant prêts à créer des tableaux de bord et des alertes.

## Comment créer des tableaux de bord Wavefront

Avant de nous lancer dans la création de tableaux de bord, comprenons d'abord l'anatomie d'un tableau de bord Wavefront.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/Wavefront_Dashboard.png)
_Anatomie d'un tableau de bord Wavefront_

Un tableau de bord dans Wavefront se compose de 5 types d'entités :

* **Dashboard** – C'est le tableau de bord principal et contient toutes les autres entités.
* **Section** – Un tableau de bord peut contenir une ou plusieurs sections. Une section est un groupe logique de graphiques. Par exemple, vous pouvez avoir une section pour afficher les graphiques liés à l'utilisation du matériel, et une autre section pour afficher les graphiques liés aux appels API.
* **Row** – Une ligne est une collection de graphiques. Vous pouvez définir le nombre de graphiques que vous souhaitez voir dans une ligne. Ma recommandation personnelle est d'avoir 3 graphiques dans une ligne. Plus que cela encombre le tableau de bord.
* **Chart** – C'est le graphique final qui affiche les métriques sur le tableau de bord. Il existe diverses options pour créer des graphiques comme des graphiques en ligne, des graphiques en barre, des graphiques en secteur, etc.
* **Source** – Un graphique peut contenir une ou plusieurs sources. Chaque source a une requête qui fonctionne sur une métrique sous-jacente pour créer une représentation visuelle sur le graphique.

Maintenant, nous sommes prêts à écrire du code pour créer un tableau de bord. Ajoutez le code suivant au fichier **main.tf** :

<script src="https://gist.github.com/theawesomenayak/d47b384deb92cb36f24e6864e646dfbe.js"></script>

Cela crée un tableau de bord avec une section pour les métriques EC2. Il y a une ligne dans cette section avec deux graphiques. Un graphique affiche l'utilisation du CPU et l'autre affiche l'utilisation de la mémoire. Les deux sont des graphiques en ligne et montrent le pourcentage d'utilisation.

## Comment créer des alertes

Le tableau de bord que nous avons créé est idéal pour visualiser l'utilisation du CPU et de la mémoire de nos instances EC2. Mais si nous voulons être avertis lorsque l'utilisation du CPU ou de la mémoire dépasse un certain seuil, nous devons configurer des alertes.

Pour créer une alerte sur l'utilisation du CPU, ajoutez le code suivant au fichier **main.tf** :

<script src="https://gist.github.com/theawesomenayak/249a5e2d1f49a15b3d9e8316da30d805.js"></script>

Cela crée deux ressources :

1. Une cible d'alerte qui envoie un email à l'adresse spécifiée chaque fois qu'une alerte est ouverte ou résolue.
2. Une alerte sur l'utilisation du CPU qui se déclenche lorsque l'utilisation du CPU dépasse le seuil donné (une alerte AVERTISSEMENT lorsqu'elle dépasse 60 % et une alerte GRAVE lorsqu'elle dépasse 80 %).

Wavefront surveille en continu l'utilisation du CPU et envoie une notification à l'adresse email lorsque le seuil est dépassé. De même, lorsque l'utilisation redevient normale, il envoie une autre notification indiquant que les choses sont revenues à la normale.

## Comment générer des ressources dans Wavefront

Le code pour créer nos ressources est prêt. Nous devons maintenant l'appliquer pour que les ressources réelles soient créées sur Wavefront.

Pour voir quels changements seront apportés à Wavefront par notre code, exécutez la commande suivante :

```
$ terraform plan
```

Cela vérifiera notre code et montrera la différence entre la configuration actuelle dans Wavefront et les changements qui se produiront en raison de votre code.

Enfin, pour créer les ressources sur Wavefront, exécutez la commande suivante :

```
$ terraform apply -auto-approve
```

Cela téléversera la configuration vers Wavefront et créera le tableau de bord et l'alerte réels. Vous pouvez maintenant aller sur Wavefront et vérifier ces ressources.

## Conclusion

Félicitations ! Vous venez de créer un nouveau tableau de bord et une alerte Wavefront via du code.

Vous pouvez maintenant apporter des modifications à votre code et exécuter `terraform apply -auto-approve` pour appliquer vos changements à Wavefront.

Terraform est un excellent moyen de maintenir vos ressources sous forme de code qui peut être vérifié dans votre système de contrôle de version. Cela permet à plusieurs développeurs de travailler sur vos ressources tout en gardant une trace des changements.

Le code source complet de ce tutoriel peut être trouvé [ici](https://github.com/theawesomenayak/wavefront-terraform).

Merci de m'avoir suivi jusqu'ici. J'espère que vous avez aimé l'article. Vous pouvez me contacter sur [LinkedIn](https://www.linkedin.com/in/theawesomenayak/) où je discute régulièrement de technologie et de vie. Jetez également un coup d'œil à certains de [mes autres articles](https://www.freecodecamp.org/news/author/theawesomenayak/). Bonne lecture. 👋