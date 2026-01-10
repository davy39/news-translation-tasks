---
title: Apprendre l'Infrastructure as Code en créant une Image Machine Personnalisée
  dans AWS
subtitle: ''
author: Destiny Erhabor
co_authors: []
series: null
date: '2022-07-15T17:15:48.000Z'
originalURL: https://freecodecamp.org/news/learn-instructure-as-a-code-by-building-custom-machine-image-in-aws
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/Understand-Infrastructure-as-a-code--4-.png
tags:
- name: AWS
  slug: aws
- name: Infrastructure as code
  slug: infrastructure-as-code
seo_title: Apprendre l'Infrastructure as Code en créant une Image Machine Personnalisée
  dans AWS
seo_desc: "Hey everyone! If you're wondering what infrastructure-as-code means, then\
  \ you've come to the right place. \nIn this article I will explain the concepts\
  \ behind Infrastructure-As-Code (IaC) at a high level and dive into a category of\
  \ IaC known as server..."
---

Salut à tous ! Si vous vous demandez ce que signifie l'infrastructure-as-code, alors vous êtes au bon endroit. 

Dans cet article, je vais expliquer les concepts derrière l'Infrastructure-As-Code (**IaC**) à un niveau élevé et plonger dans une catégorie de l'IaC connue sous le nom de **server templating**. 

Pour les besoins de cet article, nous allons utiliser un outil de templating de serveur appelé **Packer** pour créer une image machine Amazon personnalisée (AMI) et l'utiliser pour lancer une instance AWS EC2.

# Qu'est-ce que l'Infrastructure-As-Code ?

L'Infrastructure-As-Code (**IaC**) fait référence au processus de gestion et de fourniture d'infrastructure en utilisant du code plutôt que des méthodes manuelles. 

Le concept de base est que vous définissez, déployez, mettez à jour et détruisez votre infrastructure (serveurs, bases de données, réseaux, configuration, etc.) en écrivant et en exécutant du code.

# Types d'Infrastructure

## Qu'est-ce que l'Infrastructure Mutable ?

Vous pouvez changer et configurer l'infrastructure qui est mutable en fonction de vos besoins. Vous pouvez vous connecter aux serveurs, appliquer des correctifs, mettre à jour des configurations, et plus encore.

Disons que nous avons une application web que nous voulons déployer dans le cloud ou sur un serveur sur site. 

Nous configurons le programme pour installer toutes les instructions et configurations nécessaires après le déploiement afin qu'il soit prêt pour la production. Nous modifions manuellement ou automatiquement le serveur chaque fois qu'une nouvelle mise à jour/configuration de l'application est requise. 

C'est fantastique pour quelques serveurs, mais pour de nombreux serveurs, cela peut entraîner des incohérences d'application à moins d'utiliser des outils de configuration comme Ansible. Cela est appelé infrastructure mutable. Elle suit le modèle **BUILD, DEPLOY, CONFIGURE**.

### Avantages de l'Infrastructure Mutable

* Résoudre les problèmes plus rapidement. Plutôt que de devoir construire un nouveau serveur à partir de zéro, le personnel informatique apprend à connaître chaque serveur à un niveau "personnel", ce qui leur permet de diagnostiquer les problèmes plus rapidement.
* Les mises à jour sont généralement plus rapides et peuvent être adaptées à chaque serveur individuellement.
* L'infrastructure peut être adaptée aux exigences exactes des applications côté serveur.

### Défis de l'Infrastructure Mutable

* Parce que chaque serveur a une configuration unique, ce qui est connu sous le nom de dérive de configuration, les difficultés techniques sont difficiles à diagnostiquer ou à reproduire.
* Parce que vous devez configurer manuellement les serveurs, la fourniture de serveurs est souvent une procédure longue.
* Les changements de serveur ne sont pas toujours enregistrés, ce qui rend le suivi des versions plus complexe.
* Les échecs de mise à jour se produisent plus souvent en raison d'une série de facteurs imprévus tels que la connectivité réseau, les dépôts non réactifs, les temps d'arrêt DNS, etc.
* Si les mises à jour ne sont pas appliquées correctement, il y a un danger et une complexité plus élevés dans les charges de travail de production. En raison de ces situations imprévues, le débogage est difficile.

Heureusement, vous pouvez utiliser une **infrastructure immutable** pour éviter les problèmes que l'infrastructure mutable peut causer.

## Qu'est-ce que l'Infrastructure Immutable ?

Dans l'infrastructure immutable, les composants sont recréés et remplacés plutôt que mis à jour après leur formation. Cela rend votre produit plus cohérent et fiable.

Rendre votre infrastructure immutable est le meilleur moyen de garantir la scalabilité dans le domaine de l'IaC.

Maintenant, à partir du cas d'utilisation dans l'infrastructure mutable, au lieu de **configurer le serveur après le déploiement**, que diriez-vous de **le configurer avant le déploiement**, comme dans l'infrastructure mutable ci-dessus ? 

L'infrastructure immutable est basée sur ce concept, que vous pouvez mettre en œuvre avec l'aide de technologies comme Packer.

### Avantages de l'Infrastructure Immutable

* Il n'y a pas de dérive de configuration car il n'y a pas de modifications à apporter.
* Le suivi et les retours en arrière sont considérablement plus faciles avec un versionnage discret. Chaque nouveau serveur ou machine virtuelle peut être suivi par le département informatique lors de son déploiement.
* Les tests sont facilités par l'uniformité des configurations sur plusieurs serveurs.
* État prévisible en raison du fait que l'infrastructure n'est jamais modifiée, ce qui réduit la complexité.
* Dans un contexte multithread, le code de thread sécurisé signifie que la mutation est presque inexistante.

### Défis de l'Infrastructure Immutable

* L'infrastructure ne peut pas être modifiée pendant qu'elle est en place. Par exemple, si une vulnérabilité zero-day est découverte, tous les serveurs avec la même configuration doivent être mis à jour.
* L'agilité et le dynamisme accrus de l'infrastructure immutable peuvent parfois entrer en conflit avec les mesures de sécurité informatique standard.
* La copie des données de tableau d'un emplacement à un autre entraîne des frais généraux. Au lieu d'écrire des données sur le disque local, les données sont externalisées.

# Types d'outils d'Infrastructure-As-Code

Il existe cinq grandes catégories d'outils IAC :

* **Scripts ad hoc**
* **Outils de gestion de configuration**
* **Outils d'orchestration**
* **Outils de provisionnement**
* **Outils de templating de serveur**

## Qu'est-ce que les scripts ad hoc ?

Une technique ad hoc consiste à créer un script dans votre langage de programmation préféré (comme Bash ou Python) pour automatiser une tâche, configurer un outil et l'exécuter sur le serveur.

## Qu'est-ce que les outils de gestion de configuration ?

De grandes quantités de logiciels sont installées et gérées à l'aide d'outils de provisionnement sur des serveurs existants. 

Lors du clustering d'ordinateurs, il est idéal de garder le matériel et les logiciels aussi homogènes que possible. Cela aide à garantir que les performances sont cohérentes et que les nœuds séparés s'entendent les uns avec les autres. 

Les outils de gestion de configuration simplifient la gestion du côté logiciel des clusters. Certains de ces outils incluent :

* **Chef**
* **Puppet**
* **Ansible**
* **SaltStack**

## Qu'est-ce que les outils d'orchestration ?

Comment gérez-vous les VM et les conteneurs une fois qu'ils ont été créés ? Vous devez déployer des mises à jour, surveiller la santé de vos VM et distribuer le trafic entre les VM et les conteneurs dans le monde réel. Même la communication entre eux via Internet est possible (découverte de serveur). 

Les outils d'orchestration sont conçus pour traiter ces problèmes. L'orchestration est l'automatisation simultanée de nombreuses opérations afin de réduire les difficultés de production et le temps de mise sur le marché. 

Certains de ces outils incluent :

* **Kubernetes**
* **Marathon/Mesos**
* **Amazon Elastic Container Service**
* **Docker Swarm**
* **Normad**

## Qu'est-ce que les outils de provisionnement ?

Le code qui s'exécute sur chaque serveur est défini par les outils de gestion de configuration, les outils de templating de serveur et les outils d'orchestration. 

Les outils de provisionnement, en revanche, sont responsables de la création de serveurs, de bases de données, d'équilibreurs de charge, de la surveillance, de certificats de couche de sockets sécurisés (SSL) et de nombreux autres aspects de votre infrastructure. 

Exemples d'outils de provisionnement :

* **Terraform**
* **CloudFormation**
* **OpenStack Heat**

## Qu'est-ce que les outils de templating de serveur ?

Le templating de serveur est une alternative populaire à la gestion de configuration qui a récemment gagné en traction. 

L'objectif derrière les outils de templating de serveur est de créer une image d'un serveur qui prend un "snapshot" entièrement autonome du système d'exploitation (OS), des logiciels, des fichiers et de toutes les autres caractéristiques essentielles, plutôt que de lancer un certain nombre de serveurs et de les configurer en exécutant le même code sur chacun d'eux. 

Vous pouvez ensuite installer cette image sur tous vos serveurs à l'aide d'un autre programme IaC.

Exemples d'outils de templating de serveur :

* **Packer**
* **Docker**
* **Vagrant.**

Dans cet article, je vais passer en revue comment générer une image personnalisée en utilisant les outils de templating de serveur Packer, et vous verrez comment déployer l'image personnalisée sur une instance AWS.

# Packer et l'Image Personnalisée

## Qu'est-ce que Packer ?

Packer vous aide à créer et personnaliser des images qui ont déjà des applications spécifiques installées, afin que vos programmes soient copiés, et ainsi de suite. 

Ces images sont connues sous le nom d'images machine, et chaque plateforme a son propre format d'image avec des applications préchargées. 

Par exemple, voici comment certaines plateformes identifient ces images :

* **AMAZON** (AMI)
* **VMWare** (VMDK/VMX)
* **VirtualBox** (OVF)

Packer vous permet de générer votre propre image machine personnalisée et d'y intégrer votre code et votre configuration avant de la déployer sur le serveur. C'est terminé. Il n'est pas nécessaire de modifier la configuration car elle est déjà intégrée dans l'image. 

Et pour toute mise à jour ultérieure, vous détruisez le serveur et lancez un nouveau serveur avec un équilibreur de charge pour aider à maintenir la destruction d'un serveur et le démarrage d'un autre.

## Blocs de Construction Principaux de Packer

Il y a trois blocs de construction principaux dans le fichier de configuration de Packer :

* builders
* provisioners
* post-processors

Les **builders** créent la machine et génèrent l'image sur différentes plateformes. C'est un composant très important. Le bloc builder peut prendre un tableau de différents builders de différentes plateformes.

Les **provisioners** vous aident à installer, personnaliser et configurer l'image machine, soit via des logiciels tiers, soit via des outils intégrés.

Et les **post-processors** s'exécutent après que l'image a été construite et personnalisée.

### Assez de théorie...

Maintenant, il est temps pour nous de construire un système immutable avec Packer, n'est-ce pas ?

## Prérequis et Installation

* [Créer un compte AWS](https://aws.amazon.com/console/)
* [Créer un utilisateur IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console)
* [Créer et télécharger votre clé secrète et votre clé d'accès utilisateur](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey)
* [Télécharger et installer Packer](https://www.packer.io)

## Comment Construire Votre Première Image avec Packer

Tout d'abord, créez un dossier appelé **packer_custom_image**.

Ouvrez le dossier et créez les fichiers suivants : **packer.json, variable.json, setup.sh,** et **.gitignore**.

* **packer.json** contient tout le code nécessaire pour créer l'image machine personnalisée
* **variable.json** contient des informations sensibles que nous voulons garder à l'écart du public
* **setup.sh** contient des scripts shell dont nous aurons besoin pour exécuter des instructions sur notre image
* **.gitignore** contient des fichiers/dossiers cachés du serveur distant Git

Notez que les fichiers Packer utilisent l'extension .json et ont un format similaire au script JSON JavaScript.

### **Structure du Dossier/Fichier**

![Image](https://www.freecodecamp.org/news/content/images/2022/07/Capture-1.PNG)

**Commençons !**

Tout d'abord, définissons nos variables et les builders Packer à l'intérieur de variable.json comme ceci :

```json
 { 
 	"description" : "myWebServer", 
    "access_key" : "enter-aws-your-key", 
    "secret_key" : "enter-aws-your-secret", 
    "source_ami" : "enter-yours" 
   }
```

Alors, que se passe-t-il ici ?

* **descriptions** : Cette variable détecte le nom de l'image machine que nous créons
* **access_key** et **secret_key** : Vos identifiants d'utilisateur IAM que vous avez créés et téléchargés. Ceux-ci sont requis par Packer pour l'authentification et l'autorisation.
* **source_ami** : L'AMI source est l'AMI que vous souhaitez utiliser comme base pour votre AMI personnalisée. AWS dispose de nombreuses AMI telles que Amazon Linux, Ubuntu, Windows, Redhat, etc. Vous pouvez choisir parmi celles-ci comme image de base. Dans notre cas, nous utiliserons l'**Amazon Linux AMI.**

Maintenant, connectez-vous à votre console AWS. Cliquez sur services et recherchez EC2.

Cliquez sur le bouton **lancer l'instance** (nous ne lançons aucune instance, nous voulons simplement copier notre image de base).

![Image](https://paper-attachments.dropbox.com/s_27CF84DFB65AC89AFB11F73B9BBE903F909EE2F6D867768E80956C8C0E105718_1655555078518_ec2.PNG)

Ensuite, faites défiler jusqu'à **Application et OS Images (Amazon Machine Image)**. Cliquez et choisissez l'image Amazon, puis copiez votre AMI la plus récente.

![Image](https://paper-attachments.dropbox.com/s_27CF84DFB65AC89AFB11F73B9BBE903F909EE2F6D867768E80956C8C0E105718_1655555557189_base-ami.PNG)

Ensuite, fermez l'instance (**NE PAS CRÉER/LANCER**).

Ensuite, mettons à jour le fichier **packer.json** comme ceci :

```json
{ 
	"builders": [ 
    	{ 
        	"type": "amazon-ebs", 
            "access_key": "{{user `access_key` }}", 
            "secret_key": "{{user `secret_key` }}", 
            "region" : "us-east-1", 
            "ami_name" : "myfirstami", 
            "source_ami" : "{{user `source_ami` }}", 
            "instance_type" : "t2.micro", 
            "ssh_username" : "ec2-user" 
         } 
    ] 
 } 
```

Voyons ce qui se passe ici :

* **builder** : Comme mentionné précédemment, le builder crée l'image machine et peut produire des images identiques sur plusieurs plateformes, telles que AWS et Azure, d'où le tableau. Il nécessite le builder.
* **type** : Nom du type de builder
* **access et secret keys** : Pour l'authentification, il récupère les données du fichier variable.json que nous avons créé pour la sécurité, d'où le format **"{{user `variable-name` }}"**.
* **variable-name** : le nom que nous avons donné dans notre fichier variable.json (vous devriez utiliser ce format similaire pour les variables que vous ne souhaitez pas rendre publiques)
* **region** : identifie la région de l'AMI.
* **ami_name** : Nom personnalisé pour notre nom d'image machine personnalisée.
* **source ami** : Pour l'image machine que nous voulons personnaliser à partir de l'AMI AWS.
* **Instance type** : Pour l'instance temporaire requise par Packer pour créer notre image.
* **ssh username** : Pour les identifiants de création de l'instance temporaire en relation avec la plateforme du builder. **AWS** est le mot qui vient à l'esprit dans notre cas.

Ensuite, nous allons personnaliser l'image avec des provisioners. Nous allons personnaliser l'AMI source avec une instance Jenkins.

Mettez à jour le fichier packer.json et ajoutez ce qui suit après le bloc de tableau du builder :

```json
 {  ... 
 		"provisioners": 
        	[ 
            	{ 
                	"type": "shell", 
                    "script": "setup.sh" 
                 } 
             ] 
}  
```

Les provisioners viennent après les builders et prennent également un tableau. Nous pouvons utiliser de nombreux provisioners pour un ou plusieurs builders, ce qui nous donne plus de flexibilité.

* **type** : Le type shell est le provisioner le plus basique et le plus largement utilisé. Il peut accepter une propriété de script (fichier externe pour exécuter notre code), des propriétés en ligne pour s'exécuter sur la ligne de commande, ou des propriétés de fichier pour télécharger des fichiers, du code et d'autres éléments pour nos images.
* **scripts** : Prend une propriété de script externe pour exécuter nos configurations.

Configurons le fichier de scripts que nous avons créé précédemment.

**setup.sh**

```bash
sleep 30
sudo yum update -y
sudo wget -O /etc/yum.repos.d/jenkins.repo \
    https://pkg.jenkins.io/redhat-stable/jenkins.repo
sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key
sudo yum upgrade
sudo amazon-linux-extras install java-openjdk11 -y
sudo yum install jenkins -y
sudo systemctl enable jenkins
sudo systemctl start jenkins
sudo systemctl status jenkins
```

Le script installe Jenkins et ses dépendances dans notre image et démarre l'instance Jenkins.

Optionnellement, nous pouvons passer des post-processors et des variables sensibles. Il existe de nombreux post-processors que vous pouvez utiliser après qu'une image a été construite et modifiée.

**packer.json**

```json
{  ... 
		"post-processors": 
        	[ 
            	{ 
                	"type": "manifest", 
                    "output": "out.json" 
                  } 
             ] 
 } 
```

* **type** : Prend le type d'instance de post-processor, le type **manifest** définit la manière dont nous voulons que l'architecture de notre image soit imprimée après sa création.
* **output** : le nom du fichier à imprimer après les artefacts de l'image cuite
* **Sensitive-variables** : Packer nous permet de spécifier des variables sensibles à omettre du manifeste du post-processor. Ajoutons notre clé secrète et notre clé d'accès :

```json
{...
	"sensitive-variables": 
    	[     
        	"secret_key",    "access_key"  
         ]
 }
```

## Comment Exécuter et Tester le Code

Dans votre terminal, dans le répertoire racine, exécutez le code. Vous devriez voir **out.json** et **out.json.lock** créés à la racine de votre application. (Ces fichiers contiennent votre build et vos artefacts.)

`packer build -var-file="variable.json" packer.json`

![Image](https://paper-attachments.dropbox.com/s_27CF84DFB65AC89AFB11F73B9BBE903F909EE2F6D867768E80956C8C0E105718_1655557789760_firstami.PNG)

### AMI dans la Console AWS

Maintenant, connectons-nous à notre console AWS pour voir notre image personnalisée nouvellement créée. Nous devrons également lancer une instance EC2 pour vérifier si notre image a les configurations appropriées de l'instance Jenkins intégrées.

* Allez dans votre console AWS
* Cliquez sur service et recherchez EC2, puis faites défiler jusqu'à image
* Là, cliquez sur AMI et trouvez votre image personnalisée nouvellement créée

![Image](https://paper-attachments.dropbox.com/s_27CF84DFB65AC89AFB11F73B9BBE903F909EE2F6D867768E80956C8C0E105718_1655557986410_ami.PNG)

Hourra ! Notre image a été créée avec succès. Maintenant, il est temps de lancer une instance à partir de celle-ci. 

* À partir de la page AMI, sélectionnez l'AMI récemment créée et cliquez sur **Lancer une instance à partir de l'AMI** en haut à droite. Cela vous amène à la page de l'instance.
* **Nom et tags** – Donnez un nom à l'instance, par exemple ""My Jenkins Server"
* **Application et OS Images (Amazon Machine Image)** doit rester le même (c'est-à-dire, notre image)
* **Type d'instance** – Laissez par défaut "t2-micro". Cela nous permet d'utiliser le niveau gratuit d'AWS
* **Paire de clés** – Nous devrons créer une nouvelle paire de clés pour nous permettre de nous connecter (SSH) à l'instance à partir de notre terminal d'ordinateur. Cliquez sur le bouton **Créer une nouvelle clé** et la fenêtre suivante devrait s'afficher :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/key-par.PNG)
_créer une nouvelle paire de clés_

* Donnez un nom et un type à la paire de clés. Si vous utilisez Windows, vous pouvez choisir le format de fichier de clé privée .pem et utiliser votre PowerShell Windows pour vous connecter en SSH au serveur. Ou vous pouvez utiliser .ppk et vous devrez télécharger PuTTy, une application qui vous aide à obtenir SSH sur des serveurs distants. 
* Cliquez sur Créer une paire de clés une fois et la paire de clés est automatiquement téléchargée sur votre système local (**notez l'emplacement de téléchargement du fichier**)
* **Paramètres réseau** – Nous devrons configurer un peu de réseau pour permettre l'accès à notre instance Jenkins, et pour permettre SSH, HTTP et HTTPS. Cliquez donc sur modifier et faites défiler jusqu'à **règles de groupe de sécurité entrantes** pour ajouter la règle suivante (TCP personnalisé au port 8080) et permettre l'accès de n'importe où. Pour plus de sécurité, vous pouvez ajouter l'accès uniquement depuis votre IP ou personnaliser selon vos souhaits.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/network-sett.PNG)

![Image](https://www.freecodecamp.org/news/content/images/2022/07/customTCP.PNG)

Le TCP personnalisé au port 8080 nous permettra de voir notre instance Jenkins depuis notre navigateur après nous être connectés en SSH via l'IP publique ou le DNS.

Laissez **Configurer le stockage et les détails avancés** par défaut.

Ensuite, cliquez sur lancer et attendez un peu que l'instance se lance complètement. Une fois lancée, cliquez sur l'instance pour trouver toutes vos configurations (DNS, IP, etc.)

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-163.png)

Maintenant, pour l'étape finale, vous souvenez-vous de la paire de clés qui a été téléchargée dans notre système local ? Nous en aurons besoin maintenant pour nous connecter en SSH à cette instance qui contient notre serveur Jenkins.

Ouvrez votre terminal (PowerShell pour les utilisateurs Windows) et entrez ce qui suit avec votre DNS public correct ou (remplacez par l'IP publique) et le chemin de la paire de clés :

```
ssh -i /path/key-pair-name.pem ec2-user@instance-public-dns-name
```

Suivez et acceptez l'invite pour vous connecter avec succès.

Entrez **`sudo systemctl status jenkins`** pour vérifier l'état de l'instance Jenkins. Si elle ne s'exécute pas, démarrez-la en entrant **`sudo systemctl start jenkins`** dans le terminal.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/termnal-1.PNG)
_Démarrer l'instance jenkins_

Maintenant, lançons notre instance depuis le navigateur. Ouvrez votre navigateur préféré et entrez '**http://44.201.88.238:8080**' pour voir l'instance Jenkins :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/Jenkins-instance-1.PNG)

Entrez ce qui suit dans le terminal de l'instance EC2 pour voir le mot de passe et vous connecter.

```
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

Ensuite, déverrouillez et profitez de toutes les fonctionnalités de votre instance Jenkins nouvellement créée.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/get-started-1.PNG)

## Félicitations, vous avez réussi !

Vous pouvez voir le code complet de ce tutoriel ici :

* [packer.json](https://gist.github.com/Caesarsage/acd419178acec18010a2f5bc51996cec)
* [setup.sh](https://gist.github.com/Caesarsage/5da51fff02bb945c932029c4ba48d064)

## Nettoyage

Si vous souhaitez éviter des frais inutiles de la part d'AWS (basés sur l'utilisation des ressources) et puisque nous n'utilisons pas cela en production, nous devrions nettoyer nos ressources.

Pour terminer, vous pouvez vous connecter à votre console AWS et terminer le lancement de l'instance EC2 avec l'image personnalisée et supprimer l'image si vous ne l'utilisez pas.

## Résumé

Dans ce tutoriel, vous avez appris ce qu'est l'infrastructure as a code à un niveau élevé et comment elle s'applique dans la pratique mutable/immutable. 

Vous avez également appris comment créer une image personnalisée avec un outil puissant appelé Hashicorp Packer. Dans notre cas, nous avons personnalisé un serveur Jenkins dans l'image, mais vous pouvez l'étendre avec n'importe quelle configuration personnalisée. 

Et enfin, nous avons testé notre image en lançant une instance EC2.

J'espère que cet article vous aide à comprendre ce qu'est l'infrastructure as a code et comment vous pouvez utiliser ses outils dans vos applications. Bon apprentissage !