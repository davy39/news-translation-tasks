---
title: Qu'est-ce que Terraform ? Apprendre Terraform et l'Infrastructure as Code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-04-15T23:38:22.000Z'
originalURL: https://freecodecamp.org/news/what-is-terraform-learn-infrastructure-as-code
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/terraform-article.jpeg
tags:
- name: Infrastructure as code
  slug: infrastructure-as-code
- name: Terraform
  slug: terraform
seo_title: Qu'est-ce que Terraform ? Apprendre Terraform et l'Infrastructure as Code
seo_desc: 'By Sumeet Ninawe

  Terraform is a tool that helps you manage various cloud infrastructure services
  in the form of code. You codify your infrastructure, and so it''s also known as
  Infrastructure as Code (IaC).

  The cloud has become important to more and m...'
---

Par Sumeet Ninawe

Terraform est un outil qui vous aide à gérer divers services d'infrastructure cloud sous forme de code. Vous codifiez votre infrastructure, et c'est pourquoi on l'appelle aussi Infrastructure as Code (IaC).

Le cloud est devenu important pour de plus en plus d'entreprises. Il aide non seulement à réduire le temps et les coûts, mais permet également aux clients de se concentrer sur leur activité principale.

## Pourquoi l'Infrastructure as Code ?

À mesure que le nombre de fournisseurs cloud augmente et que leurs services deviennent plus flexibles, il devient de plus en plus important de pouvoir gérer vos ressources d'infrastructure cloud.

Terraform fonctionne sur le concept d'Infrastructure as Code (IaC). En termes simples, l'IaC est la capacité de représenter votre infrastructure sous forme de code.

Prenons comme exemple une ressource de calcul sur un cloud donné, comme EC2 sur AWS. Demander une instance EC2 à AWS consiste à s'inscrire auprès d'AWS, à fournir un ensemble de valeurs et à cliquer sur le bouton "Lancer". La "ressource" sera prête en quelques minutes.

Tant que nous pouvons fournir ces valeurs à AWS, elles existeront sur ce fournisseur cloud. Bien sûr, c'est la manière traditionnelle de procéder.

Terraform fournit un moyen de prendre ces informations d'identification et ces entrées sous forme de _configurations_ et de les traiter pour créer une ressource dans le cloud cible.

Ces configurations décrivent la ressource dans un langage que Terraform comprend. Les configurations sont la manière dont vous pouvez déclarer l'état souhaité de votre infrastructure – essentiellement, une syntaxe "déclarative".

Terraform utilise les API des fournisseurs cloud pour créer la ressource.

## Avantages de Terraform

Terraform est un produit de [Hashicorp](https://www.hashicorp.com/) et utilise la syntaxe [Hashicorp Configuration Language](https://github.com/hashicorp/hcl) (HCL) pour représenter les configurations.

Dans l'exemple ci-dessous, vous pouvez voir la représentation de l'instance EC2 dans sa forme la plus simple :

```
provider "aws" {
	region = "us-west-1"
}

resource "aws_instance" "myec2" {
	ami = "ami-12345qwert"
	instance_type = "t2.micro"
}
```

Cet exemple simple suffit pour comprendre les capacités de Terraform.

Le code contient deux blocs – le `provider` et le `resource`. Le bloc `provider` indique à Terraform que nous voulons utiliser le fournisseur `aws` dans la région "us-west-1".

Le bloc `resource` indique à Terraform que parmi toutes les ressources d'infrastructure offertes par AWS, nous voulons créer une ressource de type "instance" (EC2).

Le premier paramètre représente cela pour le bloc de ressource sous forme de "aws_instance". Le deuxième paramètre est le nom que nous avons donné à la ressource – dans ce cas, "myec2".

Le bloc de ressource a quelques arguments qui indiquent l'image machine AWS et le type d'instance utilisés pour créer cette ressource.

Ici, nous avons réussi à exprimer notre infrastructure sous forme de code. Passons en revue certains des avantages de l'IaC.

1. Puisque la création d'infrastructure est maintenant condensée dans des fichiers de configuration/code, il est **plus facile à maintenir** car nous pouvons désormais utiliser des systèmes de contrôle de version comme Git pour collaborer et le maintenir.
2. Le temps nécessaire pour la phase de planification de l'infrastructure est réduit car nous pouvons écrire les configurations en un **court laps de temps**. Ces configurations sont directement consommées par Terraform pour créer des ressources cloud en quelques minutes.
3. Les **changements** apportés à l'infrastructure **sont plus faciles** et sont comparables aux changements de code d'application.
4. Les avantages pour le cycle de vie de la gestion des applications dans le cas du développement logiciel sont également applicables à l'infrastructure. Cela la rend **plus efficace**.

## Fonctionnalités de Terraform

### Orchestration

Lors du déploiement de divers services de bout en bout, Terraform agit comme le cœur du processus d'orchestration lorsqu'il s'agit de créer des ressources cloud.

### Agnostique du cloud

Puisque Terraform prend en charge la plupart des clouds, y compris AWS, MS Azure et GCP, vous n'avez pas à vous soucier autant des problèmes de verrouillage par le fournisseur. Le registre Terraform fournit la documentation pour tous les fournisseurs cloud pris en charge.

Les modèles de syntaxe utilisés pour coder l'infrastructure sur divers clouds sont les mêmes, donc la courbe d'apprentissage liée aux API spécifiques aux fournisseurs est mise de côté, mais pas oubliée.

### Syntaxe déclarative

L'infrastructure exprimée dans les fichiers Terraform est déclarative – donc, en tant que développeurs, nous n'avons pas besoin de nous soucier de faire comprendre à Terraform les étapes nécessaires pour créer une ressource. Plutôt, tout ce que nous devons faire est de faire savoir à Terraform l'état souhaité et Terraform se charge des étapes en interne.

### Modules

Terraform fournit des modules qui nous aident à réutiliser notre code Terraform. Une infrastructure complexe est divisée en plusieurs modules et chaque module est réutilisable dans différents projets.

Il est très facile de convertir une configuration Terraform donnée en modules et Terraform dispose de son écosystème pour les modules préconstruits.

### Gestion de l'état

Pendant que Terraform crée et planifie l'infrastructure, l'état est maintenu. Cela peut être partagé avec d'autres membres de l'équipe à des fins de collaboration.

Terraform vous permet de gérer l'état à distance, ce qui aide à prévenir la confusion parmi les membres de l'équipe au cas où ils tenteraient de recréer l'infrastructure.

### Approvisionnement

Terraform n'est pas un outil d'approvisionnement complet, mais il aide avec les activités d'approvisionnement du premier jour. Les blocs _local-exec_ et _remote-exec_ de Terraform vous permettent d'exécuter des scripts en ligne. Les scripts en ligne aident à installer des composants logiciels après la création réussie de la ressource.

Cela est particulièrement utile lorsque vous aidez des outils de gestion de configuration comme Chef, Ansible et Salt Stack à installer leurs agents respectifs. Ils peuvent simplement envoyer un signal "UP" une fois qu'ils sont installés avec succès.

### Open Source

Terraform est disponible en tant que logiciel open source. Il dispose également d'une version Enterprise.

## Workflow Terraform [init - plan - apply - destroy]

Il y a quelques étapes simples que vous devez suivre pour exécuter votre code Terraform. Ces étapes sont étroitement liées au cycle de vie des ressources sur les plateformes cloud.

Encore une fois, ces étapes sont agnostiques du cloud, ce qui signifie que les mêmes étapes/commandes sont valides pour **créer, mettre à jour et détruire** des ressources sur n'importe quel fournisseur cloud donné.

**Note :** Cet article de blog ne couvre pas les étapes d'installation de Terraform, et je suppose que vous avez déjà installé le CLI Terraform sur votre système.

### Exécuter la commande `init`

Une fois que nous avons les fichiers de configuration prêts, la toute première commande que nous devons exécuter est `terraform init`. L'installation binaire de Terraform n'inclut pas le support de tous les fournisseurs cloud à la fois.

Au lieu de cela, en fonction du fournisseur, les **plugins appropriés sont téléchargés** avant que Terraform n'exécute le code. Dans notre exemple, l'exécution de `terraform init` téléchargerait le plugin du fournisseur `aws`. Cette commande aide à _initialiser_ le backend pour un répertoire Terraform donné.

### Générer un plan d'exécution

La commande `terraform plan` aide à **générer un plan d'exécution**. En fonction de la configuration que vous fournissez, Terraform génère un plan d'exécution. Dans cette phase, Terraform effectue des **vérifications de faisabilité** en termes d'erreurs de syntaxe, d'authentification API, de vérification d'état, et plus encore.

`plan` met en évidence toute correction dans le script Terraform avant l'exécution réelle. Si c'est réussi, il produit un **résumé des changements potentiels** dans l'infrastructure. Vous devriez exécuter cela avant _apply_, car cela vous informe des risques avant de modifier l'infrastructure.

### `Appliquer` les changements

`terraform apply` aide à **exécuter tout changement dans l'infrastructure**. Vous devriez exécuter la commande `plan` avant d'exécuter `terraform apply`, car la planification crée un fichier de plan qui est référencé pendant la phase d'application.

Cependant, si `terraform apply` est exécuté directement, un nouveau fichier de plan sera créé automatiquement.

### `Détruire` les ressources

Enfin, `terraform destroy` aide à détruire toute ressource qui fait partie de la configuration/état actuel.

## Terraform en action

D'accord, assez de théorie pour ce post. Essayons de mettre en pratique ce que nous avons appris jusqu'à présent en créant réellement une instance EC2 sur AWS.

Tout d'abord, installez le CLI Terraform si ce n'est pas déjà fait. L'installation est assez facile et vous pouvez trouver les étapes [ici](https://learn.hashicorp.com/tutorials/terraform/install-cli) pour le système d'exploitation de votre choix.

Créez un répertoire/dossier sur votre système et créez le premier fichier Terraform. Nommez-le `main.tf`. Idéalement, nous pouvons le nommer n'importe comment tant qu'il a l'extension `.tf`.

Le CLI Terraform reconnaît tous les fichiers avec une extension `.tf` enregistrés dans un répertoire particulier pour l'exécution.

Collez le code ci-dessus dans ce fichier et enregistrez-le. **Veuillez noter** que vous devez utiliser l'AMI correct en fonction de votre région préférée.

Puisque ce sera la première fois que nous exécutons le code Terraform, nous devons _initialiser_ Terraform dans ce répertoire. L'exécution de `terraform init` installera le plugin `aws` requis.

Lancez un terminal, naviguez jusqu'au répertoire où se trouve notre fichier Terraform et exécutez la commande ci-dessous.

`terraform init`

Cela devrait générer la sortie suivante. La sortie est très claire et nous pouvons voir que le plugin `aws` a été installé avec la version v3.22.0.

```
Initializing the backend...
Initializing provider plugins...
- Reusing previous version of hashicorp/aws from the dependency lock file
- Installing hashicorp/aws v3.22.0...
- Installed hashicorp/aws v3.22.0 (signed by HashiCorp)
Terraform has been successfully initialized!
You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.
If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
```

Ensuite, nous exécuterons la commande `terraform plan` pour voir un plan d'exécution provisoire. Cela valide également toute erreur syntaxique ou de référence. La commande `plan` vérifie la faisabilité des ressources déclarées dans le fichier `main.tf`. Exécutez cela dans le même terminal.

`terraform plan`

Si tout s'est bien passé, la sortie suivante est générée.

```
An execution plan has been generated and is shown below.
Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # aws_instance.example will be created
  + resource "aws_instance" "myec2" {
      + ami                          = "ami-12345qwert"
      + arn                          = (known after apply)
      + associate_public_ip_address  = (known after apply)
. . .
Plan: 1 to add, 0 to change, 0 to destroy.

------------------------------------------------------------------------

Note: You didn't specify an "-out" parameter to save this plan, so Terraform
can't guarantee that exactly these actions will be performed if
"terraform apply" is subsequently run.
```

La commande `plan` indique quelles ressources seront créées. Dans notre cas, elle prévoit de créer une instance `myec2` avec la configuration donnée. Elle montre l'ID AMI utilisé pour créer l'instance.

De plus, elle indique également que d'autres attributs comme `arn` et `associate_public_ip_address` sont connus après `apply`, c'est-à-dire lorsque l'instance sera créée.

La ligne du bas indique ici l'ensemble final des changements – ajouter 1 ressource et rien à changer ou détruire.

Donc, tout semble bon pour l'instant. Allons-y et appliquons la configuration. Exécutez la commande ci-dessous dans le terminal et observez la sortie.

`terraform apply`

Une fois confirmé, cela prend quelques secondes pour terminer la création de l'instance EC2 sur AWS, et cela est indiqué par la sortie générée par `terraform apply`.

Comme indiqué par la sortie ci-dessous, dans mon cas, cela a pris 51 secondes pour créer une instance EC2 et l'ID de l'instance est également mis à disposition.

Vérifiez la même chose en vous connectant à votre console AWS et en recherchant une instance EC2 avec l'ID ci-dessous. Si tout s'est bien passé, vous devriez pouvoir la trouver.

```
Plan: 1 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

aws_instance.myec2: Creating...
aws_instance.myec2: Still creating... [10s elapsed]
aws_instance.myec2: Still creating... [20s elapsed]
aws_instance.myec2: Still creating... [30s elapsed]
aws_instance.myec2: Still creating... [40s elapsed]
aws_instance.myec2: Still creating... [50s elapsed]
aws_instance.myec2: Creation complete after 51s [id=i-04ef3120a0006a153]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
```

Ainsi, nous avons réussi à utiliser l'IaC pour définir/déclarer et créer notre configuration de machine virtuelle sur AWS.

Si nous n'avons plus besoin de cette machine virtuelle, nous pouvons utiliser la même configuration pour la détruire.

Veuillez noter que si nous apportons des modifications à la configuration sans l'intention d'appliquer ces modifications – puis nous essayons de détruire la même chose – nous pouvons rencontrer des erreurs.

C'est parce que Terraform maintient la relation entre la configuration et les ressources du monde réel dans les fichiers d'état. Changer la configuration avec son application affectera l'alignement et Terraform traitera cela comme de nouvelles ressources à créer.

Les états Terraform est un sujet qui mérite son propre post, nous l'aborderons donc plus tard. Pour l'instant, pour détruire l'instance EC2, exécutez la commande ci-dessous dans le terminal.

`terraform destroy`

Avant de détruire la ressource, Terraform demande notre confirmation en fournissant une sortie de plan. Il indique que l'exécution de la commande de destruction supprimera 1 ressource, ce qui est exactement ce que nous attendons.

```
Terraform destroy
Plan: 0 to add, 0 to change, 1 to destroy.

Do you really want to destroy all resources?
  Terraform will destroy all your managed infrastructure, as shown above.
  There is no undo. Only 'yes' will be accepted to confirm.

  Enter a value: yes

aws_instance.myec2: Destroying... [id=i-04ef3120a0006a153]
aws_instance.myec2: Still destroying... [id=i-04ef3120a0006a153, 10s elapsed]
aws_instance.myec2: Still destroying... [id=i-04ef3120a0006a153, 20s elapsed]
aws_instance.myec2: Still destroying... [id=i-04ef3120a0006a153, 30s elapsed]
aws_instance.myec2: Still destroying... [id=i-04ef3120a0006a153, 40s elapsed]
aws_instance.myec2: Still destroying... [id=i-04ef3120a0006a153, 50s elapsed]
aws_instance.myec2: Still destroying... [id=i-04ef3120a0006a153, 1m0s elapsed]
aws_instance.myec2: Destruction complete after 1m5s

Destroy complete! Resources: 1 destroyed.
```

Encore une fois, cela prend quelques secondes pour détruire la ressource. Terraform ne vous laisse pas dans l'expectative car il met à jour le statut à intervalles de 10 secondes.

Une fois la ressource détruite, il confirme que c'est fait. N'hésitez pas à vous connecter à la console AWS et à vérifier si la ressource est terminée.

### Merci d'avoir lu !

J'espère que vous comprenez comment Terraform fonctionne à partir de cette introduction de base. J'écrirai d'autres articles couvrant des concepts plus approfondis comme les états, la syntaxe, le CLI, le backend, et ainsi de suite dans de futurs articles.

Si vous aimez ce contenu, envisagez de vous abonner, de suivre et de partager cet article de blog ! [Let'sDoTech](https://letsdotech.dev/), [Instagram](https://www.instagram.com/letsdotech/), [Twitter](https://twitter.com/letsdotech_dev), [LinkedIn](https://www.linkedin.com/company/letsdotech).