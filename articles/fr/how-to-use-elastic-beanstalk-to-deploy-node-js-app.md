---
title: Comment utiliser Elastic Beanstalk pour déployer une application Node.js
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2023-05-09T21:34:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-elastic-beanstalk-to-deploy-node-js-app
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/Elastic-Beanstalk
seo_title: Comment utiliser Elastic Beanstalk pour déployer une application Node.js
---

Banner.png
tags:
- name: AWS
  slug: aws
- name: Cloud Computing
  slug: cloud-computing
- name: node js
  slug: node-js
seo_title: null
seo_desc: "Construire et gérer des applications sur le cloud peut être une tâche ardue. \
  \ Cela est particulièrement vrai lorsqu'il s'agit de gérer différents environnements, la mise à l'échelle,\
  \ et le déploiement des mises à jour. \nMais il existe un service dans AWS qui peut simplifier cela.\
  \ AWS Elastic Beanst..."
---

Construire et gérer des applications sur le cloud peut être une tâche ardue. Cela est particulièrement vrai lorsqu'il s'agit de gérer différents environnements, la mise à l'échelle et le déploiement des mises à jour. 

Mais il existe un service dans AWS qui peut simplifier cela. AWS Elastic Beanstalk est là pour faciliter votre vie. Il fournit une plateforme facile à utiliser pour déployer, gérer et mettre à l'échelle vos applications dans le cloud AWS.

Dans ce tutoriel, nous allons plonger dans les bases d'Elastic Beanstalk, puis vous guider à travers le processus de déploiement d'une application NodeJS connectée à une base de données RDS. Commençons !

## Qu'est-ce qu'Elastic Beanstalk ?

AWS Elastic Beanstalk est un service entièrement géré qui vous aide à déployer, gérer et mettre à l'échelle des applications sur AWS. Il prend en charge la provision des ressources requises, telles que les instances EC2, les bases de données RDS et les équilibreurs de charge. 

Elastic Beanstalk gère également le déploiement des applications, la surveillance et les tâches de maintenance afin que vous puissiez vous concentrer sur l'écriture de code et la livraison de fonctionnalités.

Elastic Beanstalk utilise CloudFormation pour provisionner les ressources. Le bon point est que vous n'avez pas besoin d'écrire des modèles CloudFormation. Cela sera pris en charge automatiquement par Elastic Beanstalk.

Maintenant que nous avons une compréhension de base d'Elastic Beanstalk, plongeons dans le déploiement de notre application NodeJS avec une connexion RDS.

## Comment préparer le code source NodeJS

Nous ne pouvons pas déployer notre application directement sur Elastic Beanstalk (similaire au déploiement sur EC2). Nous devons suivre quelques étapes avant le déploiement. Cela m'a pris des heures à comprendre, mais je vais vous aider à la déployer en 5 minutes.

Dans cet article, nous allons déployer cette [application Node.js](https://github.com/5minslearn/eb-nodejs-rds). Mais pour déployer notre code, nous n'avons pas besoin d'un dépôt, mais plutôt d'un zip de notre code source. Vous pouvez télécharger le fichier zip du dépôt ci-dessus [ici](https://github.com/5minslearn/eb-nodejs-rds/blob/master/nodejs-rds-sample.zip).

Ajout des étapes ici si vous souhaitez déployer votre propre application. Mais si vous souhaitez simplement déployer le code ci-dessus, vous pouvez passer à la section suivante ([Comment créer l'application Elastic Beanstalk](#heading-comment-creer-lapplication-elastic-beanstalk)).

### Comment déployer votre propre application

Tout d'abord, assurez-vous que votre fichier `package.json` contient la commande `start` et que cette commande `start` doit être configurée pour exécuter votre application. Beanstalk exécutera `npm start` par défaut et générera une erreur s'il ne la trouve pas.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-20.png)
_fichier package.json avec la commande start_

Il y a une chose super importante concernant la configuration des variables d'environnement. AWS suit des variables d'environnement prédéfinies pour les connexions RDS. Assurez-vous d'utiliser les bons noms. Vous pouvez lire cet article d'[AWS](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.managing.db.html) pour plus d'informations. 

Un exemple rapide pour vous si vous ne comprenez pas ce point. Pour configurer le nom d'hôte pour le RDS, vous devez utiliser la variable d'environnement `RDS_HOSTNAME`. Votre application ne pourra pas se connecter si vous utilisez un autre nom de variable (par exemple `DB_HOSTNAME`).

Vous pouvez définir des variables d'environnement personnalisées dans la console AWS Elastic Beanstalk selon vos besoins.

Voici à quoi devrait ressembler votre configuration de connexion à la base de données :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/Screenshot-from-2023-05-06-23-39-39.png)
_configuration de la base de données Elastic Beanstalk_

Elastic Beanstalk (EBS) par défaut fonctionne sur le port 8080. Nous devons donc configurer notre application pour qu'elle s'exécute sur le port 8080. Il est toujours préférable d'ajouter le numéro de port dans les variables d'environnement et de le configurer dans la console EBS.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-22.png)
_port Elastic Beanstalk_

Pour qu'Elastic Beanstalk lise nos variables d'environnement, nous devons ajouter un fichier appelé `.ebextensions` dans le répertoire racine du projet avec le code suivant :

```
commands:
    setvars:
        command: /opt/elasticbeanstalk/bin/get-config environment | jq -r 'to_entries | .[] | "export \(.key)=\"\(.value)\""' > /etc/profile.d/sh.local
packages:
    yum:
        jq: []
```

Installez les dépendances en exécutant `npm install` et zippez votre code avec `node_modules` en exécutant la commande suivante :

```bash
zip [filename].zip -r ./
```

Rappelez-vous que le fichier zippé doit contenir tous les fichiers et sous-répertoires dans le dossier racine et ne doit pas être à l'intérieur d'autres dossiers. Cela est dû au fait qu'Elastic Beanstalk vérifiera la présence du fichier `package.json` dans le dossier racine et générera une erreur s'il ne le trouve pas.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/Screenshot-from-2023-05-07-00-04-50.png)
_un exemple de structure de dossier correcte pour Elastic Beanstalk nodejs_

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-21.png)
_structure de dossier incorrecte (tous les fichiers sont à l'intérieur du dossier appelé source-code)_

Maintenant que notre application est prête, créons l'application Elastic Beanstalk.

## Comment créer l'application Elastic Beanstalk

### **Étape 1 :** Configurer votre environnement

Tout d'abord, accédez à la console de gestion AWS et sélectionnez Elastic Beanstalk dans le menu Services. Cliquez sur le bouton "Créer une application".

Ensuite, sélectionnez l'environnement de serveur Web et fournissez un nom pour votre application.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-10.png)
_Démarrage avec AWS Elastic Beanstalk_

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-11.png)
_Donnez un nom à votre application_

Choisissez `Plateforme gérée` dans "Type de plateforme", et `Node.js` dans "Plateforme", et laissez le reste tel quel.

Ensuite, choisissez `Télécharger votre code` dans la section "Code de l'application" et téléchargez le fichier `zip`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-12.png)
_Capture d'écran montrant les sélections ci-dessus_

Ensuite, définissez l'étiquette de version sur `1` et choisissez `Instance unique` dans la section "Préréglages" et cliquez sur Suivant.

**Remarque :** Préférez `Haute disponibilité` pour un environnement de production.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-13.png)
_Plus de configuration de configuration_

### Étape 2 : Configurer l'accès au service

Dans cette section, nous devons configurer les rôles IAM. Nous devons créer deux rôles IAM, un pour Elastic Beanstalk et un pour EC2

Pour le rôle de service, sélectionnez `Créer et utiliser un nouveau rôle de service`. Il créera automatiquement et fournira les permissions requises

Si vous souhaitez vous connecter à votre instance EC2 via le terminal, créez une paire clé-valeur et sélectionnez-la. Ignorez cette étape si vous ne souhaitez pas vous connecter à EC2.

Créez un rôle IAM avec les permissions suivantes et ajoutez le rôle au "Profil d'instance EC2" et passez à Suivant.

* AWSElasticBeanstalkWebTier
* AWSElasticBeanstalkWorkerTier
* AWSElasticBeanstalkMulticontainerDocker

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-14.png)
_Écran de configuration de l'accès au service_

### Étape 3 : Configurer le réseau, la base de données et les balises

Maintenant, activez le basculeur `Activer la base de données` et choisissez le moteur `mysql`. Remplissez les autres champs en fonction de vos besoins.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-15.png)
_Remplir les autres options_

Soyez très prudent lors de la sélection de la "Politique de suppression de la base de données". Comme je crée l'application exemple, j'ai sélectionné l'option `Supprimer` qui supprimera la base de données lorsque l'application Elastic Beanstalk sera supprimée. 

Si vous travaillez sur une base de données de production, il est toujours préférable de choisir l'option `Créer un instantané` ou `Conserver`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-16.png)
_Politique de suppression de la base de données_

### Étape 4 : Configurer le trafic des instances et la mise à l'échelle

Vous n'avez pas besoin de changer quoi que ce soit ici sauf si vous en avez particulièrement besoin. Si vous construisez cette application exemple, laissez les champs avec les valeurs par défaut. Par défaut, Elastic Beanstalk créera une machine Amazon Linux.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-17.png)
_Vous pouvez laisser les valeurs par défaut sauf si vous avez besoin de quelque chose en particulier._

### Étape 5 : Configurer les mises à jour, la surveillance et la journalisation

Choisissez `Basique` dans "Rapport de santé" et décochez l'activation des mises à jour gérées.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-18.png)
_Plus de configuration_

Ajoutez vos variables d'environnement et cliquez sur Suivant.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-23.png)
_Ajouter des variables d'environnement_

Enfin, passez en revue toutes vos configurations et passez à l'étape suivante. Il faut du temps pour provisionner le RDS, alors asseyez-vous et prenez votre café

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-19.png)
_Passez en revue la configuration et passez à l'étape suivante lorsque vous êtes prêt._

À présent, vous comprenez peut-être pourquoi j'ai passé des heures sur ce processus la première fois 😀. Chaque fois que je faisais une erreur, je devais attendre environ 10 à 15 minutes pour vérifier le résultat et refaire toutes les étapes ci-dessus si quelque chose n'allait pas. Elastic Beanstalk testera définitivement votre patience, alors restez calme et détendez-vous.

Une fois tout terminé, vous devriez voir que la santé devient verte 🎉 et une URL de domaine sera générée 🤳

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-24.png)
_Succès !_

Si vous avez utilisé mon exemple de [dépôt](https://github.com/5minslearn/eb-nodejs-rds), vous verrez la page suivante en ouvrant l'URL.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-25.png)

Lorsque vous accédez à `domain-url/hikes`, vous pouvez voir la page ci-dessous. Saisissez quelques données et cliquez sur le bouton `Record Hike`, les données seront stockées dans la table `hikes` dans RDS MySQL.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-26.png)
_Site déployé_

## Conclusion

Dans cet article, nous avons déployé avec succès une application NodeJS avec une connexion RDS en utilisant AWS Elastic Beanstalk. Ce service puissant simplifie le processus de déploiement et de gestion, vous permettant de vous concentrer sur le développement et la mise à l'échelle de vos applications.

Si vous êtes bloqué à un moment donné, n'hésitez pas à me poser vos questions par email à [arun@gogosoon.com](mailto:arun@gogosoon.com). Je serai heureux de vous aider.

J'espère que vous avez apprécié la lecture de cet article !

Si vous souhaitez en savoir plus sur AWS, abonnez-vous à ma [newsletter](https://5minslearn.gogosoon.com/?ref=fcc_cloud_elastic_beanstalk) ([https://5minslearn.gogosoon.com/](https://5minslearn.gogosoon.com/?ref=fcc_cloud_elastic_beanstalk)) et suivez-moi sur les réseaux sociaux.