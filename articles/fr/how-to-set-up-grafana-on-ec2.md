---
title: Comment installer Grafana sur EC2
subtitle: ''
author: Onwubiko Emmanuel
co_authors: []
series: null
date: '2024-08-02T13:42:27.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-grafana-on-ec2
coverImage: https://www.freecodecamp.org/news/content/images/2024/08/pexels-kawserhamid-176342.jpg
tags:
- name: analytics
  slug: analytics
- name: Grafana
  slug: grafana
- name: monitoring
  slug: monitoring
seo_title: Comment installer Grafana sur EC2
seo_desc: "In today's data-driven world, it's important to monitor and visualize system\
  \ metrics to make sure everything works consistently and performs well. \nGrafana\
  \ is an open-source analytics and monitoring platform. It has gained widespread\
  \ recognition amon..."
---

Dans le monde actuel axé sur les données, il est important de surveiller et de visualiser les métriques système pour s'assurer que tout fonctionne de manière cohérente et performante. 

Grafana est une plateforme d'analyse et de surveillance open-source. Elle a gagné une reconnaissance généralisée parmi les développeurs et les entreprises cherchant à extraire plus d'informations des données produites par leurs systèmes. 

Grafana possède de nombreuses fonctionnalités de visualisation puissantes, et lorsqu'elle est combinée avec la scalabilité et la flexibilité d'Amazon EC2, elle crée un environnement stable pour une surveillance efficace. 

Cet article vous guidera à travers l'installation de Grafana sur Amazon EC2 et la création de tableaux de bord informatifs à partir de données brutes. 

## **À qui ce guide est-il destiné ?**

Ce tutoriel est destiné aux débutants dans le cloud ainsi qu'aux experts en DevOps. L'objectif de cet article est de simplifier le processus d'installation afin que vous puissiez utiliser Grafana sur AWS de manière optimale. Commençons maintenant. 

## **Comment configurer votre instance EC2**

Vous devez configurer la règle entrante pour votre instance EC2 afin d'accéder au port 3000, car Grafana fonctionne sur ce port. Mais d'abord, vous devez créer une instance EC2. Vous pouvez suivre ce guide sur la façon de configurer votre instance [AWS EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html). Cela prend moins de 5 minutes. 

Une fois que vous avez créé votre instance EC2, vous devrez configurer les règles entrantes du réseau. Rendez-vous donc sur la page de votre instance et cliquez dessus. Dans le widget de bouton, cliquez sur l'onglet **sécurité** et cliquez sur le lien du groupe de sécurité (il devrait ressembler à ceci : « **sg-547********************** »). 

Une fois que vous avez ouvert la page dans la section des règles entrantes, cliquez sur « **Modifier les règles entrantes** ». Cliquez sur Ajouter une nouvelle règle et ajoutez **3000** dans le champ de la plage de ports, et dans le champ source, sélectionnez **0.0.0.0/0**. Ensuite, enregistrez. 

![Image](https://paper-attachments.dropboxusercontent.com/s_4B51535633ABB1D019D79F3934180D191EF4BB549B6DD5EF46643EA16E05EAAE_1721347239653_image.png)
_Règles entrantes_

## **Comment créer un rôle IAM**

Maintenant, vous devez créer un rôle **IAM (Identity Access Management)**. Vous créez un rôle d'identité afin de pouvoir générer des identifiants que vous utiliserez ensuite pour vous connecter à votre service Grafana. 

![Image](https://paper-attachments.dropboxusercontent.com/s_4B51535633ABB1D019D79F3934180D191EF4BB549B6DD5EF46643EA16E05EAAE_1721348061199_IAM+Dashboard.png)
_Tableau de bord IAM_

Dans le champ de recherche, tapez « **service IAM** » et cliquez dessus. Cliquez sur '**Créer un rôle**', et sélectionnez le service AWS comme type d'entité de confiance. 

![Image](https://paper-attachments.dropboxusercontent.com/s_4B51535633ABB1D019D79F3934180D191EF4BB549B6DD5EF46643EA16E05EAAE_1721348079999_IAM+Role+creation.png)
_Entité de confiance IAM_

Dans la section du cas d'utilisation, sélectionnez EC2, puis cliquez sur suivant. 

![Image](https://paper-attachments.dropboxusercontent.com/s_4B51535633ABB1D019D79F3934180D191EF4BB549B6DD5EF46643EA16E05EAAE_1721348098668_EC2+Use+Case.png)
_Cas d'utilisation du rôle IAM_

Sur la page Ajouter des permissions, cliquez sur la stratégie **AdministratorAccess**, puis cliquez sur suivant. Entrez un nom de rôle – dans ce cas, j'ai utilisé **Grafana-Server-Role**. 

![Image](https://paper-attachments.dropboxusercontent.com/s_4B51535633ABB1D019D79F3934180D191EF4BB549B6DD5EF46643EA16E05EAAE_1721348120427_IAM+role+modify+.png)
_Création de rôle_

## Comment télécharger Grafana

Maintenant que vous avez configuré votre règle entrante EC2 et également configuré le rôle IAM, installons Grafana sur votre instance EC2. 

Rendez-vous sur la [page de téléchargement de Grafana](https://grafana.com/grafana/download). Puisque nous allons télécharger la version pour Amazon Linux dans ce tutoriel, vous devez taper la commande suivante sur votre ligne de commande Linux. Remarque : Vous devez vous connecter à votre instance VM via SSH (Secure Shell). Dans ce cas, j'utilise EC2 Instance Connect. 

```bash
sudo yum install -y https://dl.grafana.com/enterprise/release/grafana-enterprise-11.1.0-1.x86_64.rpm
```

Maintenant, vous allez activer le service Grafana sur votre terminal en tapant la commande suivante :

```bash
systemctl enable grafana-server.service
```

Puis démarrez le service :

```bash
systemctl start grafana-server.service
```

Vérifiez l'état du service Grafana sur l'instance EC2 en exécutant cette commande :

```bash
systemctl status grafana-server.service
```

![Image](https://paper-attachments.dropboxusercontent.com/s_4B51535633ABB1D019D79F3934180D191EF4BB549B6DD5EF46643EA16E05EAAE_1721411484886_Grafana+Active+.png)
_État du service Grafana_

Maintenant que vous avez confirmé que le service est actuellement actif, vous devrez également vérifier si le service Grafana est actif sur le **port 3000**, car vous avez déjà créé une règle entrante pour cela. 

Vous pouvez le faire en tapant la commande suivante :

```bash
netstat -tunpl | grep grafana
```

![Image](https://paper-attachments.dropboxusercontent.com/s_4B51535633ABB1D019D79F3934180D191EF4BB549B6DD5EF46643EA16E05EAAE_1721411578753_3000+active.png)
_Confirmation du port 3000_

Maintenant que vous avez confirmé que le service fonctionne sur le port 3000, vous pouvez continuer et configurer votre tableau de bord Grafana. 

Vous pouvez accéder au tableau de bord Grafana en tapant l'IP publique de votre instance EC2 et en ajoutant le port 3000 dans votre navigateur web, quelque chose comme ceci : **34.239.101.172:3000**. 

![Image](https://paper-attachments.dropboxusercontent.com/s_4B51535633ABB1D019D79F3934180D191EF4BB549B6DD5EF46643EA16E05EAAE_1721411871355_Grafana.png)
_Connexion à Grafana_

Le nom d'utilisateur et le mot de passe par défaut pour Grafana sont admin, mais vous aurez la possibilité de changer votre mot de passe après vous être connecté avec les identifiants par défaut. Vous pouvez également ignorer le processus de changement de mot de passe si vous le souhaitez. 

![Image](https://paper-attachments.dropboxusercontent.com/s_4B51535633ABB1D019D79F3934180D191EF4BB549B6DD5EF46643EA16E05EAAE_1721412805910_Grafana+Password.png)
_Changer le mot de passe sur Grafana_

Après cette étape, allez à la page d'accueil. La prochaine chose à faire est de commencer à connecter votre tableau de bord Grafana à une source de données. Dans ce cas, vous allez le connecter au service AWS CloudWatch. 

![Image](https://paper-attachments.dropboxusercontent.com/s_4B51535633ABB1D019D79F3934180D191EF4BB549B6DD5EF46643EA16E05EAAE_1721413426627_Grafana+home.png)
_Grafana_

## **Comment connecter des sources de données au tableau de bord Grafana**

Cliquez sur l'onglet connexions dans le menu latéral et cliquez sur sources de données. Recherchez le service CloudWatch. 

![Image](https://paper-attachments.dropboxusercontent.com/s_4B51535633ABB1D019D79F3934180D191EF4BB549B6DD5EF46643EA16E05EAAE_1721413905866_image.png)
_Configuration de CloudWatch_

Maintenant, vous serez invité à entrer votre ID de clé d'accès et votre clé d'accès secrète. Vous devrez créer cela sur votre service IAM AWS. 

Retournez donc à votre tableau de bord de gestion IAM et allez dans l'onglet des utilisateurs. Si vous n'avez pas créé d'utilisateur IAM, vous pouvez le faire en consultant ce [tutoriel de création d'utilisateur IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html). 

Dans le tableau de bord IAM de l'utilisateur, faites défiler jusqu'à la section des clés d'accès et cliquez sur **Créer une clé d'accès**. 

![Image](https://paper-attachments.dropboxusercontent.com/s_4B51535633ABB1D019D79F3934180D191EF4BB549B6DD5EF46643EA16E05EAAE_1721414737862_Access+Key.png)
_Clé d'accès_

Sélectionnez le cas d'utilisation de l'interface de ligne de commande. 

![Image](https://paper-attachments.dropboxusercontent.com/s_4B51535633ABB1D019D79F3934180D191EF4BB549B6DD5EF46643EA16E05EAAE_1721414696820_Access+Key+2.png)
_Cas d'utilisation de la clé d'accès_

Définissez la balise de description. Cette étape est facultative. Ensuite, cliquez sur **Créer une clé d'accès**. 

![Image](https://paper-attachments.dropboxusercontent.com/s_4B51535633ABB1D019D79F3934180D191EF4BB549B6DD5EF46643EA16E05EAAE_1721414844084_Access+Key+3.png)
_Clés d'accès_

Maintenant, copiez l'ID de la clé d'accès et la clé d'accès secrète et collez-les dans la page de configuration de la source de données CloudWatch sur Grafana. Définissez votre région cloud par défaut – dans ce cas, la mienne est **us-east-1**

![Image](https://paper-attachments.dropboxusercontent.com/s_4B51535633ABB1D019D79F3934180D191EF4BB549B6DD5EF46643EA16E05EAAE_1721414955923_image.png)
_Paramètres supplémentaires_

Lorsque vous avez terminé, cliquez sur les boutons enregistrer et tester. Grafana interrogera les journaux CloudWatch, et si cela fonctionne correctement, il enregistrera la configuration. 

## **Comment créer un tableau de bord sur Grafana**

Maintenant que vous avez configuré avec succès votre service Grafana, commençons à créer des tableaux de bord. 

Cliquez sur l'onglet tableau de bord dans le menu latéral, cliquez sur **Nouveau** et sélectionnez nouveau tableau de bord. Vous devriez voir l'écran ci-dessous : 

![Image](https://paper-attachments.dropboxusercontent.com/s_4B51535633ABB1D019D79F3934180D191EF4BB549B6DD5EF46643EA16E05EAAE_1721416576260_dashboard.png)
_Créer un nouveau tableau de bord_

Ensuite, sélectionnez **Importer un tableau de bord**. 

![Image](https://paper-attachments.dropboxusercontent.com/s_4B51535633ABB1D019D79F3934180D191EF4BB549B6DD5EF46643EA16E05EAAE_1721417832804_image.png)
_Importer un tableau de bord_

Dans ce cas, vous allez importer un tableau de bord déjà créé depuis Grafana. Grafana dispose de nombreux tableaux de bord pour de nombreux cas d'utilisation et services. Mais dans ce cas, vous allez importer un tableau de bord EC2 ([Tableau de bord EC2 Grafana](https://grafana.com/grafana/dashboards/11265-amazon-ec2/)). 

Si vous souhaitez l'importer, vous pouvez facilement copier l'ID du tableau de bord que vous souhaitez importer. Il est toujours accompagné du tableau de bord. 

Copiez donc maintenant l'ID – dans ce cas, c'est **11265**. Ensuite, collez-le dans le champ d'importation sur l'importation du tableau de bord, et cliquez sur le bouton de chargement. 

![Image](https://paper-attachments.dropboxusercontent.com/s_4B51535633ABB1D019D79F3934180D191EF4BB549B6DD5EF46643EA16E05EAAE_1721418236847_Grafana+Dashboard.png)
_Tableau de bord Grafana_

Maintenant, vous avez créé avec succès un tableau de bord dans Grafana. Ce tableau de bord vous permet de surveiller les performances de votre instance EC2. Vous pouvez surveiller des métriques telles que l'utilisation du CPU, le crédit CPU, les opérations de disque, les octets de disque, le réseau, les paquets réseau, la vérification de l'état, etc. 

## Conclusion

Merci d'avoir lu ! J'espère que ce guide étape par étape vous a aidé à apprendre comment créer et configurer des tableaux de bord efficaces en utilisant Grafana.