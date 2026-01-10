---
title: 'Workflow Terraform : Comment travailler individuellement et en équipe'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-16T08:08:29.000Z'
originalURL: https://freecodecamp.org/news/terraform-workflow-working-individually-and-in-a-team
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/tf-workflows.jpeg
tags:
- name: Devops
  slug: devops
- name: Infrastructure as code
  slug: infrastructure-as-code
- name: Terraform
  slug: terraform
- name: workflow
  slug: workflow
seo_title: 'Workflow Terraform : Comment travailler individuellement et en équipe'
seo_desc: "By Serhii Vasylenko\nA workflow, or a pattern of the work, gives you a\
  \ standardized way to do something. \nIt is extremely helpful in a team, and can\
  \ benefit you even if you work individually. A good workflow enables you to streamline\
  \ a process, organi..."
---

Par Serhii Vasylenko

Un workflow, ou un modèle de travail, vous donne une manière standardisée de faire quelque chose. 

C'est extrêmement utile en équipe, et peut vous être bénéfique même si vous travaillez individuellement. Un bon workflow vous permet de rationaliser un processus, de l'organiser et de le rendre moins sujet aux erreurs.

Cet article résume plusieurs approches lors de l'utilisation de Terraform, à la fois individuellement et en équipe. J'ai essayé de rassembler les plus courantes, mais vous pourriez aussi vouloir développer la vôtre.

L'exigence commune pour toutes est un système de contrôle de version (comme Git). C'est ainsi que vous vous assurez que rien n'est perdu et que toutes vos modifications de code sont correctement versionnées et suivies.

Table des matières :

* [Concepts de base](#heading-concepts-de-base)
* [Workflow individuel de base](#heading-workflow-individuel-de-base)
* [Workflow d'équipe de base](#heading-workflow-dequipe-de-base)
* [Workflow d'équipe avec automatisation](#heading-workflow-dequipe-avec-automatisation)
* [Workflow d'import](#heading-workflow-dimport)

## Concepts de base

Définissons d'abord les actions de base. 

Tous les workflows décrits sont construits sur trois étapes clés : Write, Plan et Apply. Néanmoins, leurs détails et actions varient entre les workflows.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-79.png)

**Write** – c'est là que vous apportez des modifications au code.

**Plan** – c'est là que vous passez en revue les modifications et décidez si vous les acceptez.

**Apply** – c'est là que vous acceptez les modifications et les appliquez à l'infrastructure réelle.

C'est une idée simple avec une variété de mises en œuvre possibles.

## Workflow individuel de base

C'est le workflow le plus simple si vous travaillez seul sur un projet TF relativement petit. Ce workflow convient bien aux backends locaux et distants.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-78.png)

### Write

Vous clonez le dépôt de code distant ou vous récupérez les dernières modifications, vous modifiez le code de configuration, puis vous exécutez les commandes `terraform validate` et `terraform fmt` pour vous assurer que votre code fonctionne bien.

### Plan

C'est là que vous exécutez la commande `terraform plan` pour vous assurer que vos modifications font ce dont vous avez besoin. C'est un bon moment pour valider vos modifications de code (ou vous pouvez le faire à l'étape suivante).

### Apply

C'est là que vous exécutez `terraform apply` et introduisez les modifications aux objets d'infrastructure réels. C'est aussi là que vous poussez les modifications validées vers le dépôt distant.

## Workflow d'équipe de base

Ce workflow est bon lorsque vous travaillez avec du code de configuration en équipe et que vous souhaitez utiliser des branches de fonctionnalités pour gérer les modifications de manière précise.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-80.png)

### Write

Commencez par créer une nouvelle branche, apportez vos modifications et exécutez les commandes `terraform validate` et `terraform fmt` pour vous assurer que votre code fonctionne bien.

Exécuter `terraform plan` à cette étape aidera à garantir que vous obtiendrez ce que vous attendez.

### Plan

C'est là que se déroulent les revues de code et de plan.

Ajoutez la sortie de la commande `terraform plan` à la Pull Request avec vos modifications. Il serait bon d'ajouter uniquement les parties modifiées de la sortie commune, c'est-à-dire la partie qui commence par la chaîne "_Terraform will perform the following actions_".

### Apply

Une fois la PR revue et fusionnée dans la branche amont, il est sûr de finalement tirer la branche amont localement et d'appliquer la configuration avec `terraform apply`.

## Workflow d'équipe avec automatisation

En résumé, ce workflow vous permet d'introduire une sorte de test de fumée pour votre code d'infrastructure (en utilisant `plan`) et également d'automatiser les retours dans le processus CI.

La partie automatisée de ce workflow consiste en un plan spéculatif sur commit et/ou Pull Request (PR), ainsi qu'à ajouter la sortie de `plan` au commentaire de la PR. Un plan spéculatif signifie simplement montrer les modifications, et ne pas les appliquer ensuite.



![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-81.png)

### Write

Cette étape est la même que dans le workflow précédent.

### Plan

C'est là que votre outil CI fait son travail. 

Passons en revue cela étape par étape :

1. Vous créez une PR avec les modifications de code que vous souhaitez implémenter.
2. Le pipeline CI est déclenché par un événement de votre dépôt de code (comme une poussée de webhook) et il exécute un plan spéculatif contre votre code.
3. La liste des modifications (un soi-disant "plan diff") est ajoutée à la PR pour revue par le CI.
4. Une fois fusionnée, le pipeline CI s'exécute à nouveau et vous obtenez le plan final prêt à être appliqué à l'infrastructure.

**Apply**

Maintenant que vous avez une branche (par exemple, main) avec le nouveau code à appliquer, vous devez la tirer localement et exécuter `terraform apply`.

Vous pouvez également ajouter l'application automatisée ici – étape 5 dans l'image ci-dessous. Cela peut être très utile pour les environnements jetables tels que les tests, la pré-production, le développement, etc.

L'outil CI exact à utiliser ici vous appartient : Jenkins, GitHub Actions et Travis CI fonctionnent tous bien. 

Une chose importante à noter est que le pipeline CI doit être configuré de manière bidirectionnelle avec votre dépôt pour obtenir le code et rapporter avec des commentaires à la PR.

En option, vous pouvez envisager d'utiliser Terraform Cloud qui offre de nombreuses fonctionnalités, y compris l'intégration de dépôt mentionnée ci-dessus, même avec l'abonnement gratuit.

Si vous n'avez jamais travaillé avec Terraform Cloud auparavant et que vous souhaitez des conseils pour commencer, je fournirai les liens à la fin de cet article.

## Workflow d'import

Ce workflow fait référence à une situation où vous avez déjà créé certains objets (c'est-à-dire, en cours d'exécution), et vous devez les gérer avec Terraform.

Supposons que nous avons déjà un bucket S3 dans AWS appelé "someassetsbucket" et que nous voulons l'inclure dans notre code de configuration.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-82.png)

### Prepare

Vous devez créer un bloc de ressource à utiliser plus tard pour l'objet réel que vous allez importer. 

Vous n'avez pas besoin de remplir les arguments au début, donc il peut s'agir simplement d'un bloc de ressource vide, par exemple :

```
resource "aws_s3_bucket" "assets" {

}
```

### Import

Maintenant, vous devez importer les informations sur l'objet réel dans votre fichier d'état Terraform existant.

Cela peut être fait avec la commande `terraform import`, par exemple :

```
terraform import aws_s3_bucket.assets "someassetsbucket"
```

### Write

Maintenant, vous devez écrire le code Terraform correspondant pour ce bucket.

Pour éviter de modifier votre objet réel lors de l'action `terraform apply`, vous devez spécifier tous les arguments nécessaires avec les valeurs exactes de la phase d'importation.

Vous pouvez voir les détails en exécutant la commande `terraform state show`, par exemple :

```
terraform state show aws_s3_bucket.assets
```

La sortie de cette commande sera très similaire au code de configuration. Mais elle contient à la fois les arguments et les attributs de la ressource, vous devez donc la nettoyer avant de l'appliquer.

Vous pouvez utiliser l'une des tactiques suivantes :

* soit copier/coller, puis exécuter `terraform validate` et `terraform plan` plusieurs fois pour vous assurer qu'il n'y a pas d'erreurs comme "_argument is not expected here_" ou "_this field cannot be set_"
* soit vous pouvez sélectionner et écrire uniquement les arguments nécessaires

Dans tous les cas, assurez-vous de vous référer à la documentation de la ressource pendant ce processus.

### Plan

Le but est d'avoir une sortie `terraform plan` montrant uniquement les modifications "_~ update in-place_".

Cependant, il n'est pas toujours clair si l'objet réel sera modifié ou si seul le fichier d'état sera mis à jour. C'est pourquoi vous devez comprendre comment fonctionne un objet réel et connaître son cycle de vie pour vous assurer qu'il est sûr d'appliquer le plan.

### Apply

C'est l'action habituelle `terraform apply`. 

Une fois appliqué, votre configuration et votre fichier d'état correspondront à la configuration de l'objet réel. 

## **Conclusion**

Voici un aperçu de Terraform Cloud pour ceux qui n'ont jamais travaillé avec auparavant : [Overview of Terraform Cloud Features](https://www.terraform.io/docs/cloud/overview.html)

Et voici un bon tutoriel pour commencer : [Get Started - Terraform Cloud](https://learn.hashicorp.com/collections/terraform/cloud-get-started)

De plus, voici un aperçu des workflows à grande échelle par le CTO de HashiCorp, qui pourrait être utile pour les utilisateurs plus expérimentés de Terraform : [Terraform Workflow Best Practices at Scale](https://www.hashicorp.com/resources/terraform-workflow-best-practices-at-scale)

Merci d'avoir lu. J'espère que vous essaierez l'un de ces workflows, ou que vous développerez le vôtre !

