---
title: Comment automatiser l'installation d'Anaconda sur AWS EC2 avec CloudFormation
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-23T12:26:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-automate-installation-of-anaconda-on-aws-ec2-instances-e9db8aa0570d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*urq81shE8JyiAM7BMYN_tQ.jpeg
tags:
- name: AWS
  slug: aws
- name: Cloud Computing
  slug: cloud-computing
- name: Devops
  slug: devops
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment automatiser l'installation d'Anaconda sur AWS EC2 avec CloudFormation
seo_desc: 'By Daniel Barker

  TL;DR

  Are you struggling to automate the install of Anaconda on AWS (Amazon Web Services)
  EC2 instances and install necessary Python packages for your project? I was — so
  I wrote a simple bash script to handle it.

  Read on for a quick...'
---

Par Daniel Barker

#### **TL;DR**

*Vous avez du mal à automatiser l'installation d'Anaconda sur AWS (Amazon Web Services) EC2 et à installer les packages Python nécessaires pour votre projet ? C'était mon cas, alors j'ai écrit un simple script bash pour le gérer.*

*Lisez la suite pour un tutoriel rapide ou consultez le [dépôt Github](https://github.com/dcbark01/AnacondaInstallEC2) contenant le script et le modèle CloudFormation.*

Pour une raison que je ne comprends pas, Amazon insiste pour utiliser Python 2 sur ses instances EC2 Amazon Linux 2 standard. Bien sûr, sur un projet sur lequel j'ai récemment travaillé, j'avais besoin de Python 3. Comme d'habitude, les environnements virtuels sont venus à la rescousse.

Normalement, j'installerais simplement Anaconda et ce serait bon. Cependant, mon projet utilise également largement les outils CloudFormation d'AWS pour déployer automatiquement des piles de ressources à partir d'un modèle, donc j'avais besoin d'un moyen d'automatiser l'installation. Je voulais également que les instances EC2 fraîchement créées aient l'AWS CLI et le package Python Boto3 installés.

Heureusement, AWS fournit une clé 'UserData' lors de l'approvisionnement des instances EC2 qui peut exécuter des commandes bash définies par l'utilisateur et des scripts shell.

Comme c'est souvent le cas, quelque chose que je pensais être simple a fini par prendre plusieurs heures, mais espérons que ce script vous aidera à éviter le même casse-tête. Voici un tutoriel rapide sur la façon d'utiliser le script et le modèle, que vous pouvez obtenir à ce lien :

[** Lien vers le dépôt Github **](https://github.com/dcbark01/AnacondaInstallEC2)

#### **Étape 1 : Ouvrir le modèle CloudFormation dans la console AWS**

Obtenez le fichier de modèle à partir du lien du dépôt ci-dessus et ouvrez-le dans le concepteur CloudFormation.

![Image](https://cdn-media-1.freecodecamp.org/images/1R9-HVEE0hQiZFOeCjl9Op6Mj3aTt1PVNcGb)

Cliquez sur 'créer une pile' dans le coin supérieur gauche et entrez les paramètres nécessaires (votre clé/secrète AWS API, nom de la clé SSH, etc.)

![Image](https://cdn-media-1.freecodecamp.org/images/9oYgo6OW0m3E4mqdVIt5YuVv61bGETIEUc13)

Passez à travers le reste des invites avec 'suivant' puis créez la pile. Vous devriez obtenir un message 'CREATE_IN_PROGRESS' comme celui ci-dessous...

![Image](https://cdn-media-1.freecodecamp.org/images/MiDJzfDTTLXGaqAAwJcPP2zRSOArTHrAbHKP)

...Et ensuite un 'CREATE_COMPLETE' une fois terminé (cela peut prendre beaucoup de temps - souvent 10 minutes - Anaconda est une installation assez lourde) :

![Image](https://cdn-media-1.freecodecamp.org/images/djulPCKTa9rphsAof0nNJDZ2g4HLn4l87xZ0)

#### **Étape 2 : Se connecter en SSH à votre nouvelle instance pour vérifier l'installation**

En utilisant votre client SSH préféré, connectez-vous à votre nouvelle instance. Vous devriez pouvoir vérifier rapidement qu'Anaconda s'est installé avec succès en tapant :

```
conda activate python3
```

Vérifiez que l'invite sur le client SSH change pour montrer que l'activation de 'python3' est active. Vous pouvez également vérifier que l'AWS CLI s'est correctement installé en tapant :

```
cd ~/.awsls
```

Vous devriez voir le fichier 'credentials' créé dans ce répertoire.

Si vous répondez aux vérifications ci-dessus, vous devriez avoir terminé. Bonne chance pour la suite de votre projet !