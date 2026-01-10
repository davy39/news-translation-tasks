---
title: Comment connecter votre instance AWS EC2 à VS Code
subtitle: ''
author: Ijeoma Igboagu
co_authors: []
series: null
date: '2025-03-25T17:48:02.797Z'
originalURL: https://freecodecamp.org/news/how-to-connect-your-aws-ec2-instance-to-vs-code
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1742397603245/c1ca0496-dbab-4570-8b6b-cb4bac5f72c1.png
tags:
- name: ec2
  slug: ec2
- name: AWS
  slug: aws
- name: software development
  slug: software-development
- name: ssh
  slug: ssh
- name: Cloud
  slug: cloud
- name: server
  slug: server
seo_title: Comment connecter votre instance AWS EC2 à VS Code
seo_desc: 'As a DevOps engineer, it is crucial to master at least one cloud provider.
  Cloud services simplify storage, data migration, and CI/CD workflows and help make
  these tasks easier and more efficient.

  If you need a basic introduction to cloud computing, ...'
---

En tant qu'ingénieur DevOps, il est crucial de maîtriser au moins un fournisseur de cloud. Les services cloud simplifient le stockage, la migration de données et les flux de travail CI/CD, et aident à rendre ces tâches plus faciles et plus efficaces.

Si vous avez besoin d'une introduction de base à l'informatique en cloud, voici un tutoriel pour débutants pour vous : [**Qu'est-ce que l'informatique en cloud ? Un guide pour débutants.**](https://www.freecodecamp.org/news/cloud-computing-guide-for-beginners/)

Dans ce guide, je vais vous montrer comment créer une instance AWS EC2. C'est l'un des principaux services d'AWS pour construire des applications. À la fin de ce guide, vous saurez comment lancer une instance AWS EC2 et la connecter à VS Code.

## **Table des matières**

* [Prérequis](#heading-prerequis)
    
* [Qu'est-ce qu'une instance AWS EC2 ?](#heading-quest-ce-quune-instance-aws-ec2)
    
* [Pourquoi connecter votre instance AWS EC2 à VS Code ?](#heading-pourquoi-connecter-votre-instance-aws-ec2-a-vs-code)
    
* [Comment lancer et connecter votre instance AWS EC2 à VS Code](#heading-comment-lancer-et-connecter-votre-instance-aws-ec2-a-vs-code)
    
    * [Étape 1 : Créer une instance AWS EC2](#heading-etape-1-creer-une-instance-aws-ec2)
        
    * [Étape 2 : Connecter l'instance AWS EC2 à votre éditeur de code](#heading-etape-2-connecter-linstance-aws-ec2-a-votre-editeur-de-code)
        
    * [Étape 3 : Installer le langage de programmation](#heading-etape-3-installer-le-langage-de-programmation)
        
    * [Étape 4 : Ouvrir une fenêtre distante](#heading-ouvrir-une-fenetre-distante)
        
    * [Étape 5 : Accéder à votre dossier de projet](#heading-etape-5-acceder-a-votre-dossier-de-projet)
        
* [Conclusion](#heading-conclusion)
    

## Prérequis

Avant de commencer, assurez-vous d'avoir :

* Un compte AWS. Si vous n'en avez pas, [inscrivez-vous ici](https://aws.amazon.com/free/?gclid=Cj0KCQiAvvO7BhC-ARIsAGFyToVguvjmSCa99VkB7XsHepginSELSYCCYnVzZXeZSKFpRRTC8DKyh98aAkZkEALw_wcB&trk=2d3e6bee-b4a1-42e0-8600-6f2bb4fcb10c&sc_channel=ps&ef_id=Cj0KCQiAvvO7BhC-ARIsAGFyToVguvjmSCa99VkB7XsHepginSELSYCCYnVzZXeZSKFpRRTC8DKyh98aAkZkEALw_wcB:G:s&s_kwcid=AL!4422!3!645125273261!e!!g!!aws!19574556887!145779846712&all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all).
    
* Un dépôt GitHub avec votre code source. Si vous n'avez pas de compte GitHub, [inscrivez-vous ici](https://github.com/).
    
* Des connaissances de base en développement web et en contrôle de version.
    
* Un éditeur de code. Pour ce tutoriel, j'utilise VS Code.
    

Commençons sans plus tarder !

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1735997217784/fdb3b399-7a07-4cf2-8577-10859bf5542d.gif align="center")

## Qu'est-ce qu'une instance AWS EC2 ?

AWS EC2 (Elastic Compute Cloud) vous permet d'exécuter des machines virtuelles dans le cloud. Ces ordinateurs vous permettent d'exécuter vos applications sans avoir besoin de matériel physique.

Il y a un certain nombre de choses que vous pouvez faire avec AWS EC2, comme l'hébergement de sites web ou d'applications, l'exécution de tâches de big data ou d'apprentissage automatique, la création d'environnements de test, et la gestion de tâches qui nécessitent une puissance de calcul flexible et évolutive.

## Pourquoi connecter votre instance AWS EC2 à VS Code ?

Connecter votre instance AWS EC2 à VS Code est utile pour plusieurs raisons. Avant de commencer le processus de configuration, il est important de comprendre pourquoi c'est bénéfique.

1. L'utilisation de VS Code offre un espace de développement familier et efficace. Cela donne l'impression de coder sur votre propre machine.
    
2. Vous n'avez pas besoin de vous connecter à votre instance AWS EC2 à chaque fois. Vous pouvez éditer des fichiers, exécuter des commandes et déboguer du code à distance.
    
3. Vous pouvez rationaliser votre flux de travail avec un accès intégré au terminal et des extensions. Ainsi, vous n'aurez pas à basculer entre les clients SSH tout le temps.
    
4. Vous pouvez pousser les modifications vers GitHub. Cela rend la collaboration et le déploiement beaucoup plus fluides.
    
5. VS Code fonctionne bien avec Java, Node.js et Python. Il prend en charge de nombreux langages et frameworks, ce qui en fait un excellent choix pour le développement cloud.
    

Maintenant que vous comprenez les avantages, passons à la configuration de la connexion.

## **Comment lancer et connecter votre instance AWS EC2 à VS Code**

Pour lancer une instance EC2 sur AWS, suivez simplement ces étapes :

### **Étape 1 : Créer une instance AWS EC2**

Tout d'abord, connectez-vous à votre compte AWS. Ensuite, utilisez la barre de recherche pour trouver EC2 et sélectionnez-le.

![Recherche d'EC2 sur la console AWS](https://cdn.hashnode.com/res/hashnode/image/upload/v1736016609765/f784db8e-46cc-4e03-abc0-7bdea9b1c668.png align="center")

Cliquez sur EC2 et suivez les instructions à l'écran pour créer une nouvelle instance.

1. **Choisissez une AMI (Amazon Machine Image) :** Il s'agit d'un modèle préconfiguré qui inclut un système d'exploitation et peut être livré avec des logiciels supplémentaires.
    
2. **Sélectionnez un type d'instance :** Choisissez la taille adaptée à vos besoins. Par exemple, `t2.micro` est une bonne option pour les débutants et les petites charges de travail.
    
3. **Configurez votre instance EC2 :** Configurez le réseau, le stockage, les groupes de sécurité et d'autres options en fonction de vos exigences.
    
4. **Lancez votre instance :** Démarrez votre serveur virtuel et accédez-y à distance pour commencer à l'utiliser.
    

![création d'une instance EC2](https://cdn.hashnode.com/res/hashnode/image/upload/v1736174305817/e8d9d8dd-f09d-4bca-a838-42ee55607fa5.gif align="center")

Instance lancée en cours d'exécution :

![Instance lancée](https://cdn.hashnode.com/res/hashnode/image/upload/v1736174700999/b729de98-bd8f-496f-9486-3079d87fb4de.png align="center")

Alors, que se passe-t-il dans l'étape 1 ?

En lançant une instance AWS EC2, vous configurez un serveur distant dans le cloud. AWS propose différentes AMI qui servent d'environnements préconfigurés.

### Étape 2 : **Connecter l'instance AWS EC2 à votre éditeur de code**

Pour connecter votre instance EC2 créée dans AWS à votre VS Code, vous avez besoin de SSH.

#### Qu'est-ce que SSH ?

SSH (Secure Shell) est un moyen sécurisé de se connecter et de communiquer avec d'autres appareils. Il maintient votre connexion sécurisée. Cela est important lorsque vous accédez à des serveurs ou à des dépôts. Dans Git, vous pouvez utiliser SSH au lieu de HTTPS pour cloner des dépôts avec une connexion sécurisée.

#### Pourquoi SSH est-il important ici ?

Avec SSH, vous pouvez lier votre éditeur de code local (comme VS Code) à votre instance AWS EC2. Cela vous permet de travailler sur les fichiers stockés sur l'instance EC2 directement depuis votre éditeur comme si vous étiez sur votre ordinateur local.

**Pour connecter votre instance AWS EC2 à votre éditeur local en utilisant SSH, suivez ces étapes :**

* Ouvrez votre terminal.
    
* Allez dans le dossier où se trouve votre fichier de clé `.pem`. Le fichier de clé (.pem) se télécharge automatiquement lorsque vous créez votre instance EC2 (généralement dans le dossier Téléchargements).
    
* Mettez à jour les permissions du fichier pour garder votre clé sécurisée et assurer une authentification correcte.
    

Pour les utilisateurs Linux, utilisez cette commande pour mettre à jour les permissions du fichier :

```bash
chmod 400 codebuild-keypair.pem
```

Pour les utilisateurs Windows, vous devrez d'abord trouver le nom d'utilisateur de votre ordinateur portable, car vous en aurez besoin pour mettre à jour les permissions du fichier.

Pour ce faire, ouvrez votre terminal et tapez :

```powershell
whoami
```

Cela affichera votre nom d'utilisateur actuel.

Une fois que vous avez votre nom d'utilisateur, utilisez la commande suivante pour mettre à jour les permissions du fichier :

```powershell
icacls "codebuild-keypair.pem" /reset
icacls "codbuild-keypair.pem" /grant:r "%USERNAME%:R"
icacls "codebuld-keypair.pem" /inheritance:r
```

Voici ce que je veux dire : Mon nom d'utilisateur est **ijeon**, donc vous devriez le remplacer par **le nom d'utilisateur de votre ordinateur portable** et **votre propre** clé, qui se termine par l'extension `.pem`.

![collage de la commande sur le terminal](https://cdn.hashnode.com/res/hashnode/image/upload/v1736021541861/048a9411-2348-48dc-8a6e-04d51dbd347d.png align="center")

L'exécution de cette commande ci-dessus met à jour les permissions du fichier. Ainsi, avec cela, vous pouvez travailler avec votre serveur distant.

![le résultat de la commande collée](https://cdn.hashnode.com/res/hashnode/image/upload/v1736021649692/118c75cf-30b4-474c-b726-142c2b4326e9.png align="left")

Maintenant que vous avez défini les permissions de fichier correctes, vous pouvez utiliser la commande SSH avec l'adresse IPv4 pour vous connecter à notre instance EC2. Tapez la commande suivante :

```powershell
ssh -i [CHEMIN VERS VOTRE FICHIER .PEM] ec2-user@[VOTRE DNS PUBLIC IPV4]
```

Exemple :

```powershell
ssh -i "C:\Users\ijeon\OneDrive\Desktop\devops-series-nextwork\codebuild-keypair.pem" ec2-user@ec2-35-178-142-201.eu-west-2.compute.amazonaws.
```

Décomposition :

1. `ssh` : Cela démarre une connexion distante sécurisée.
    
2. `-i "C:\Users\ijeon\...\codebuild-keypair.pem"` : Cela indique à SSH d'utiliser le fichier de clé `.pem` pour un accès sécurisé.
    
3. [`ec2-user@ec2-35-178-142-201.eu-west-2.compute.amazonaws.com`](mailto:ec2-user@ec2-35-178-142-201.eu-west-2.compute.amazonaws.com) :
    
    * `ec2-user` est le nom d'utilisateur par défaut pour les instances EC2.
        
    * `@ec2-35-178-142-201...` est l'adresse publique de votre instance EC2.
        

Cette commande vous connecte à votre instance EC2 à distance depuis votre ordinateur. Elle utilise ensuite la clé (fichier `.pem`) au lieu d'un mot de passe pour la sécurité. Elle vous permet également de contrôler l'instance EC2 depuis votre terminal comme si vous l'utilisiez directement.

Si tout est configuré correctement, un message de "succès" apparaîtra. Cela confirme que vous êtes connecté et que vous pouvez accéder au serveur distant.

![connexion via ssh](https://cdn.hashnode.com/res/hashnode/image/upload/v1742153348953/a68f32fc-7578-4904-9b2e-e63a353e84a0.gif align="center")

### **Étape 3 : Installer le langage de programmation**

Maintenant que vous avez lié votre instance à l'éditeur, vous pouvez installer les packages nécessaires pour construire votre application web. Vous pouvez utiliser n'importe quel langage de programmation avec lequel vous êtes à l'aise, mais nous utiliserons Java pour ce tutoriel. Il s'agira d'une application web simple – nous n'avons pas besoin d'entrer dans les détails avancés.

#### **1. Installer Java**

Dans votre terminal, exécutez les commandes suivantes pour installer **Java** :

```powershell
sudo dnf install -y java-1.8.0-amazon-corretto-devel

export JAVA_HOME=/usr/lib/jvm/java-1.8.0-amazon-corretto.x86_64

export PATH=/usr/lib/jvm/java-1.8.0-amazon-corretto.x86_64/jre/bin/:$PATH
```

Cela installe Java sur votre système. Vous avez également besoin de Maven. Il aide à gérer les projets Java et à créer des modèles pour les applications web.

#### **2. Installer Maven**

Maven vous aide à organiser les projets Java. Il vous permet également de créer des modèles pour les applications web. Exécutez ces commandes pour installer Maven :

```powershell
wget https://archive.apache.org/dist/maven/maven-3/3.5.2/binaries/apache-maven-3.5.2-bin.tar.gz

sudo tar -xzf apache-maven-3.5.2-bin.tar.gz -C /opt

echo "export PATH=/opt/apache-maven-3.5.2/bin:$PATH" >> ~/.bashrc

source ~/.bashrc
```

Pour confirmer l'installation correcte de Maven, exécutez cette commande :

```powershell
mvn -v
```

Exécutez également la commande suivante pour vérifier si vous avez Java installé :

```powershell
java -version
```

Maintenant que vous avez installé Maven, vous pouvez l'utiliser pour créer une application web Java avec la commande suivante :

```powershell
mvn archetype:generate \
  -DgroupId=com.nextwork.app \
  -DartifactId=nextwork-web-project \
  -Dpackage=com.nextwork.app \
  -DarchetypeArtifactId=maven-archetype-webapp \
  -DarchetypeVersion=1.4 \
  -DinteractiveMode=false
```

L'exécution de la commande ci-dessus génère un modèle pour votre application. Dans le terminal, il devrait afficher un message "Build Success". Cela signifie que la configuration a fonctionné.

![Installation du modèle](https://cdn.hashnode.com/res/hashnode/image/upload/v1742122446716/7c51b3a2-6a8c-463d-817c-9630488a803d.png align="center")

### **Étape 4 :** Ouvrir une fenêtre distante

Maintenant que vous avez installé les packages nécessaires et configuré votre modèle d'application, vous devez ouvrir votre IDE ou éditeur de code. Cela vous permettra d'accéder aux dossiers sur votre serveur distant.

Dans votre terminal, cliquez sur l'icône de double flèche en bas à gauche.

![double flèche à gauche](https://cdn.hashnode.com/res/hashnode/image/upload/v1736073016500/cb3a4d44-3ae5-4ccb-9006-c592c0be30f7.png align="center")

Lorsque vous cliquez dessus, cela ouvre une fenêtre modale pour vous.

![se connecter à l'hôte](https://cdn.hashnode.com/res/hashnode/image/upload/v1736073334686/a24d115c-9da3-4b46-80be-a75d73a189ab.gif align="center")

Une fenêtre apparaîtra. Cliquez sur "Connect to Host", ce qui ouvrira une autre fenêtre.

Ensuite, choisissez "Add New SSH Host" pour ouvrir le terminal de connexion SSH.

![ajout d'un hôte SSH](https://cdn.hashnode.com/res/hashnode/image/upload/v1736073802080/45dbc209-0b4c-41a2-83eb-3fa05a8eff20.gif align="center")

Entrez votre commande SSH pour configurer l'hôte.

![image de la commande de connexion SSH](https://cdn.hashnode.com/res/hashnode/image/upload/v1736078262849/b09d017e-cbd3-476e-9641-63dc41e34d83.png align="center")

Après avoir appuyé sur "Enter", un fichier de configuration s'ouvrira. Dans ce fichier, assurez-vous que le fichier `.pem` et les adresses `IP4v DNS` de votre instance EC2 sont correctes.

![emplacement pour appuyer pour le fichier de configuration](https://cdn.hashnode.com/res/hashnode/image/upload/v1736083806867/e158ee79-67d3-41c8-bb63-870caab0033b.png align="center")

Voici une vue GIF de l'image ci-dessus :

![une vue gif de la façon d'ouvrir votre fichier de configuration](https://cdn.hashnode.com/res/hashnode/image/upload/v1736083586490/7520a325-376d-42a8-905d-2e22770498de.gif align="center")

Voici le fichier de configuration :

![fichier de configuration](https://cdn.hashnode.com/res/hashnode/image/upload/v1736084278100/6e71324f-6b47-4a2a-b7a1-89c1be10c39b.png align="center")

Retournez à votre éditeur et cliquez à nouveau sur cette double flèche. Cela ouvrira automatiquement une nouvelle fenêtre.

![Réouverture d'une nouvelle fenêtre](https://cdn.hashnode.com/res/hashnode/image/upload/v1736086002267/53e4edd8-afe2-4652-90ab-56bc90f80405.gif align="center")

Si votre éditeur affiche l'adresse DNS IPv4, votre VS Code est connecté avec succès à l'instance EC2.

![connexion au serveur distant](https://cdn.hashnode.com/res/hashnode/image/upload/v1736086479299/e399f86c-e236-4efc-8d4d-a7055139d01e.png align="left")

Maintenant que vous êtes connecté et qu'une nouvelle fenêtre est ouverte, accédons au dossier stocké dans le cloud.

### Étape 5 : Accéder à votre dossier de projet

Dans l'étape 3, vous vous souvenez quand vous avez installé Maven ? Il a créé un modèle pour votre application web. Maintenant, vous allez accéder au dossier où vous l'avez créé.

1. Allez dans le panneau de l'explorateur dans la fenêtre.
    
2. Cliquez sur le bouton **"Ouvrir le dossier"**.
    

![accéder au dossier distant](https://cdn.hashnode.com/res/hashnode/image/upload/v1736087503207/7fb21fcb-939e-4f17-83d2-93a6e0e3ee68.png align="center")

En cliquant sur ce bouton, une boîte modale s'ouvre pour que vous sélectionniez votre dossier, qui a été créé par le modèle Maven :

![accéder au dossier](https://cdn.hashnode.com/res/hashnode/image/upload/v1742134089654/77104e69-4c7a-4b59-812d-423167079f24.gif align="center")

Pour accéder au fichier modèle, cliquez sur le dossier "src". Cela vous mène au fichier `index.jsp`.

![modèle automatiquement créé pour vous](https://cdn.hashnode.com/res/hashnode/image/upload/v1742135158716/4cfedc15-1c2e-4d60-b9f6-fe04c300dfa0.png align="left")

Avec ce modèle créé, vous pouvez décider de le modifier et de l'envoyer à votre dépôt Git pour le stockage.

## Conclusion

Excellent travail ! Vous avez configuré une instance AWS EC2, l'avez liée à votre éditeur de code et installé les outils nécessaires pour votre application web. Dans ce tutoriel, nous avons utilisé Java, mais vous pouvez également choisir d'autres langages comme Node.js ou Python.

Si vous avez trouvé cet article utile, veuillez le partager avec d'autres personnes qui pourraient le trouver intéressant.

Restez informé de mes projets en me suivant sur [Twitter](https://twitter.com/ijaydimples), [LinkedIn](https://twitter.com/ijaydimples) et [GitHub](https://github.com/ijayhub).

Merci d'avoir lu.