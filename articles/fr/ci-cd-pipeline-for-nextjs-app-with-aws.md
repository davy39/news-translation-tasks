---
title: Comment mettre en place un pipeline CI/CD pour une application Next.js avec
  AWS
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2023-03-27T21:53:46.000Z'
originalURL: https://freecodecamp.org/news/ci-cd-pipeline-for-nextjs-app-with-aws
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Deploy-Next.js-using-AWS--1.png
tags:
- name: AWS
  slug: aws
- name: continuous deployment
  slug: continuous-deployment
- name: Continuous Integration
  slug: continuous-integration
- name: Next.js
  slug: nextjs
seo_title: Comment mettre en place un pipeline CI/CD pour une application Next.js
  avec AWS
seo_desc: "Hello Everyone! Deploying a web application is a challenging task (at least\
  \ for me), especially when it comes to keeping it updated. It can take up a lot\
  \ of time and energy if it has to be deployed manually every time you make a change.\
  \ \nBut I recent..."
---

Bonjour à tous ! Déployer une application web est une tâche difficile (du moins pour moi), surtout lorsqu'il s'agit de la maintenir à jour. Cela peut prendre beaucoup de temps et d'énergie si elle doit être déployée manuellement à chaque fois que vous effectuez une modification.

Mais j'ai récemment découvert un moyen d'automatiser le processus de déploiement pour les applications Next.js en utilisant AWS CodeDeploy et CodePipeline. Cela m'a rendu la vie tellement plus facile, et je suis ravi de le partager avec vous.

Dans ce tutoriel, je vais vous guider à travers le processus de configuration du déploiement automatique pour votre application Next.js à l'aide des services AWS CodePipeline et CodeDeploy. À la fin de celui-ci, vous serez en mesure de gagner beaucoup de temps en déployant votre application automatiquement à chaque fois que vous pushez le code.

C'est parti !

## Table des matières :

1. [Prérequis](#heading-prerequis)
2. [Comment déployer l'application Next.js sur AWS EC2](#heading-comment-deployer-lapplication-nextjs-sur-aws-ec2)
3. [Comment lancer l'application Next.js en mode production](#heading-comment-lancer-lapplication-nextjs-en-mode-production)
4. [Comment faire tourner une application Next.js en permanence quand la console est fermée](#heading-comment-faire-tourner-une-application-nextjs-en-permanence-quand-la-console-est-fermee)
5. [Qu'est-ce que CodeDeploy ?](#heading-questce-que-codedeploy)
6. [Comment configurer le déploiement automatique avec CodePipeline et CodeDeploy](#heading-comment-configurer-le-deploiement-automatique-avec-codepipeline-et-codedeploy)
7. [Comment attacher le rôle IAM à EC2](#heading-comment-attacher-le-role-iam-a-ec2)
8. [Comment créer le CodePipeline](#heading-comment-creer-le-codepipeline)
9. [Conclusion](#heading-conclusion)

## Prérequis

1. Machine EC2 tournant sous Ubuntu
2. Connaissances très basiques des services AWS EC2 et IAM

## Comment déployer l'application Next.js sur AWS EC2

Pour commencer simplement, déployons manuellement l'application Next.js de base "hello-world" sur EC2. Les étapes sont pratiquement les mêmes pour toutes les applications Next.js.

### Connexion à EC2

Connectez-vous à la machine EC2 que vous avez créée à l'aide de la commande ci-dessous :

```
ssh -i /path/key-pair-name.pem instance-user-name@instance-IP-address
```

Lorsque vous essayez de vous connecter à EC2, voici l'erreur courante que la plupart des gens rencontrent (je l'ai eue aussi) :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-216.png)
_Erreur : Les permissions 0664 pour le fichier .pem sont trop ouvertes_

Cette erreur indique que le fichier `.pem` doit être protégé en lecture. Seul l'utilisateur root doit pouvoir le lire. Vous devez donc définir la permission du fichier sur `400`. Exécutez la commande suivante pour y parvenir :

```
chmod 400 key-pair-name.pem
```

EC2 est livré par défaut sans logiciel installé. Une fois connecté à EC2, installez NodeJS. Il existe un excellent [article](https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-20-04) publié par Digital Ocean et je l'utilise à chaque fois que je dois installer Node sur le serveur.

J'ai téléchargé le [dépôt boilerplate](https://github.com/5minslearn/deploy_nextjs_app) sur Github. Vous pouvez cloner le dépôt en exécutant la commande suivante :

```bash
git clone https://github.com/5minslearn/deploy_nextjs_app.git
```

Naviguez vers le projet et installez les dépendances en exécutant les commandes ci-dessous.

Une petite note ici. Je suis un grand fan de yarn pour sa gestion ultra-rapide des dépendances. Mais je vois que la plupart des gens utilisent `npm` pour gérer leurs dépendances. Si vous préférez utiliser `npm`, vous pouvez remplacer `yarn install` par `npm install` dans les commandes ci-dessous.

Si vous préférez utiliser `yarn`, installez d'abord yarn en suivant ce [tutoriel](https://classic.yarnpkg.com/lang/en/docs/install/#debian-stable).

```
cd deploy_nextjs_app
yarn install
```

Lançons l'application :

```
yarn dev
```

Allez sur "http://ec2-public-ip-address:3000/" dans votre navigateur et vous devriez voir la page suivante :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-217.png)
_Application Next.js Hello World_

Il y a un autre problème courant que la plupart des gens rencontrent ici et que nous allons examiner ensuite.

### Comment corriger l'erreur de timeout (EC2)

"Oh mon Dieu ! Mon site charge pendant longtemps et finit par afficher une erreur de timeout. Quel pourrait être le problème ? Où ai-je fait une erreur ?"

Si cela vous arrive, vous pouvez suivre les étapes ci-dessous pour le corriger.

Ce problème survient essentiellement si votre serveur n'expose pas le port 3000. Rappelez-vous, par défaut, les applications Next s'exécutent sur le port 3000. Mais vous devez autoriser le port 3000 dans le Security Group de votre console EC2 pour y accéder depuis votre navigateur.

Connectez-vous à votre console AWS, sélectionnez votre instance EC2, puis sélectionnez l'option Security Group. Cliquez sur le bouton "Edit inbound rules". Ajoutez le port 3000 à la liste comme indiqué dans la capture d'écran ci-dessous. Cliquez ensuite sur le bouton "Save rules".

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-218.png)
_Ajout du port 3000 à un groupe de sécurité_

Visitez le lien "http://ec2-public-ip-address:3000/", et vous serez étonné de voir que votre page se charge comme par magie.

Jusqu'à présent, nous avons simplement lancé notre application en mode développement et vérifié qu'elle fonctionne.

## Comment lancer l'application Next.js en mode production

Pour déployer l'application en mode production, vous devez d'abord builder votre application. Exécutez `yarn build` pour builder l'application et `yarn start` pour démarrer l'application en mode production.

```
yarn build
yarn start
```

Allez à nouveau sur "http://ec2-public-ip-address:3000/" et cette fois vous verrez que votre application se charge plus rapidement qu'auparavant.

Les applications fonctionnant en mode Production seront toujours plus rapides par rapport à celles fonctionnant en mode Développement. C'est parce que les applications de Production sont optimisées pour la performance.

## Comment faire tourner une application Next.js en permanence quand la console est fermée

Ainsi, votre application fonctionne maintenant. Mais vous remarquerez peut-être qu'elle vous empêche de fermer votre terminal et de quitter la connexion au serveur. Si vous le faites, votre site sera hors ligne. C'est là que PM2 entre en jeu.

Fondamentalement, PM2 est un gestionnaire de processus qui aide à maintenir les applications Node actives tout le temps. Il s'exécute en arrière-plan en gérant les applications Node pour vous.

Installez PM2 à l'aide de la commande suivante :

```
sudo yarn global add pm2
```

Après l'installation de PM2, exécutez la commande ci-dessous pour lancer et gérer votre application en arrière-plan :

```
pm2 start yarn --name [nom-de-votre-app] -- start -p [numero-de-port]
```

Remplacez `[nom-de-votre-app]` par le nom de votre application et `[numero-de-port]` par 3000. Voici un exemple de commande :

```
pm2 start yarn --name next_hello_world_app -- start -p 3000
```

Allez sur "http://ec2-public-ip-address:3000/" et vous serez à nouveau étonné de voir votre application opérationnelle.

C'est toujours une bonne pratique de sauvegarder le processus PM2. Lorsque vous redémarrez votre instance, vos instances PM2 seront perdues. Afin de les restaurer dans leur état précédent, vous devez sauvegarder le processus PM2. Voici la commande pour cela :

```
pm2 save
```

Voici la commande pour restaurer vos instances PM2 au redémarrage (ne l'exécutez pas maintenant, nous y reviendrons plus tard) :

```
pm2 resurrect
```

Nous avons réussi à déployer l'application Next.js manuellement. Mais rappelez-vous, à chaque fois que vous modifiez le code et que vous voulez voir les changements sur votre site, vous devez vous connecter à EC2, récupérer les derniers changements, builder l'application et redémarrer l'application.

Cela consommera beaucoup de temps et je suis trop paresseux pour le faire. Alors automatisons cela à l'étape suivante !

Avant de configurer le déploiement automatique, vous devez savoir comment fonctionne CodeDeploy.

## Qu'est-ce que CodeDeploy ?

CodeDeploy vous permet de déployer votre application automatiquement sur n'importe quel nombre d'instances EC2. Nous devons préparer deux éléments avant de commencer ce processus :

1. L'agent CodeDeploy doit être installé dans l'instance EC2. Nous l'utilisons pour interroger continuellement CodeDeploy et déployer si de nouveaux changements sont disponibles.
2. Un fichier nommé `appspec.yml` doit être présent dans le dossier racine. Ce fichier décrit les étapes à suivre pour le déploiement.

Il existe une excellente [documentation](https://docs.aws.amazon.com/codedeploy/latest/userguide/codedeploy-agent-operations-install-ubuntu.html) d'AWS pour vous aider à installer l'agent CodeDeploy. Veuillez suivre chaque étape pour installer l'agent CodeDeploy sur votre machine EC2.

Pour vérifier que l'agent CodeDeploy est installé, exécutez la commande ci-dessous. Si vous voyez _active (running),_ félicitations ! CodeDeploy a été installé avec succès.

```
sudo service codedeploy-agent status
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-219.png)
_Statut d'exécution de l'agent CodeDeploy_

Maintenant, créons le fichier `appspec.yml`. J'ai écrit les instructions de déploiement dans le fichier `deploy.sh`. Il suffit d'exécuter ce fichier dans le fichier `appspec.yml`. Si vous voulez en savoir plus sur `appspec.yml`, consultez la [documentation](https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-appspec-file-structure.html) officielle d'AWS.

Créez un fichier nommé `appspec.yml` et ajoutez le contenu suivant :

```
version: 0.0
os: linux
hooks:
  ApplicationStart:
    - location: deploy.sh
      timeout: 300
      runas: ubuntu
```

J'espère que vous comprenez les instructions du fichier ci-dessus. Sinon, voici une explication super simple. J'indique à l'agent CodeDeploy que j'utilise un OS Linux dans mon instance et je lui demande d'exécuter le fichier `deploy.sh` en tant qu'utilisateur `ubuntu` avec un timeout fixé à 300 secondes.

Voici mon fichier `deploy.sh` :

```
#!/bin/bash
cd /path/to/project/on/EC2 
git pull origin master
yarn install &&
yarn build &&
pm2 restart [name] 
```

Ce fichier contient les instructions pour naviguer vers le dossier du projet sur EC2, récupérer le dernier code depuis le contrôle de source, installer les dépendances, builder le projet et redémarrer l'instance du projet.

Ce fichier est déjà disponible dans le dépôt. Aucune action de votre part ici. Il est maintenant temps de configurer le déploiement automatique.

## Comment configurer le déploiement automatique avec CodePipeline et CodeDeploy

Deux rôles IAM doivent être créés pour configurer le déploiement automatique. Quelques complications vont commencer ici. Pour simplifier les choses, j'ai joint des captures d'écran avec les éléments appropriés mis en évidence par des cadres rouges.

### Créer un rôle IAM pour CodeDeploy

Vous devez créer ce rôle pour déployer le code à chaque fois que vous pushez.

Naviguez vers IAM dans la console AWS en recherchant "IAM" dans la barre de recherche en haut. Cliquez sur Roles dans le panneau de gauche et cliquez sur le bouton "Create role" en haut à droite.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-220.png)
_Créer un rôle IAM_

Choisissez AWS service dans Trusted entity types et choisissez CodeDeploy dans la section Use cases et passez à l'étape suivante.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-221.png)
_Rôle IAM pour CodeDeploy_

Maintenant, vous pouvez voir que la politique AWSCodeDeployRole est la seule politique disponible, et elle sera choisie par défaut dans cette étape (Permissions). Passons à la section suivante. Aucune action de votre part ici.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-222.png)
_Permission AWSCodeDeploy_

Entrez un nom pour votre rôle IAM. Vous devriez choisir un nom significatif pour l'identifier à l'avenir. Je l'appelle _service-role-for-code-deploy_. Vérifiez la permission dans le JSON et cliquez sur le bouton Create role en bas.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-223.png)
_Révision de la permission AWSCodeDeploy_

### Créer un rôle IAM pour EC2

Créons le rôle suivant. Ce rôle est pour EC2. Choisissez AWS service dans Trusted entity type, EC2 dans la section Common use cases, et choisissez CodeDeploy dans Use cases for other AWS services. Cliquez sur Next pour passer à la section suivante.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-224.png)
_Rôle IAM pour EC2_

Il existe de nombreuses politiques disponibles pour EC2 et CodeDeploy. Dans la section Add permissions, recherchez _codedeploy_ (pas d'espace entre code et deploy) et sélectionnez "AmazonEC2RoleForCodeDeploy" puis passez à l'étape suivante.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-225.png)
_Ajout de la permission AmazonEC2RoleForCodeDeploy_

Aucun changement dans cette étape. Révisez et donnez un nom significatif (je le nomme "code-deploy-role-for-ec2") à votre rôle et cliquez sur le bouton "Create role".

## Comment attacher le rôle IAM à EC2

Une fois le rôle IAM pour EC2 créé, nous devons l'attacher à l'instance EC2.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-226.png)
_Instance EC2 avant d'attacher le rôle IAM_

Pour attacher le rôle IAM à l'instance EC2, ouvrez votre instance EC2, cliquez sur le bouton "Actions" en haut à droite, et sélectionnez "Security" dans le menu déroulant. Ensuite, sélectionnez "Modify IAM role".

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-227.png)
_Modifier le rôle IAM pour l'instance EC2_

Sélectionnez le rôle IAM que vous avez créé en dernier (code-deploy-role-for-ec2) et cliquez sur le bouton "Update IAM role". Redémarrez l'EC2 pour que les changements prennent effet.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-228.png)
_Mettre à jour le rôle IAM pour l'instance EC2_

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-229.png)
_Instance EC2 après avoir attaché le rôle IAM_

Après avoir redémarré l'EC2, connectez-vous à EC2 avec SSH et exécutez la commande `pm2 resurrect` pour restaurer les processus PM2. Ne pas le faire pourrait vous mener à une erreur "PM2 Process or Namespace not found" lors de l'exécution du déploiement automatique.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-230.png)
_Restauration du processus PM2_

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-231.png)
_Erreur processus ou namespace PM2 non trouvé_

### Comment créer l'application CodeDeploy

Dans la console AWS, recherchez "CodeDeploy" dans la barre de recherche en haut. Sélectionnez "Applications" dans le panneau de gauche. Cliquez sur le bouton "Create application" en haut à droite.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-232.png)
_Naviguer vers CodeDeploy dans la console AWS_

Entrez le nom de l'application, choisissez la plateforme de calcul "EC2/On-premises", et cliquez sur le bouton "Create application".

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-233.png)
_Créer l'application CodeDeploy_

Une fois cela fait, vous serez automatiquement redirigé vers la section Deployment groups. Nous devons créer un groupe de déploiement. Cliquez sur le bouton "Create deployment group".

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-234.png)
_Créer le groupe de déploiement CodeDeploy_

Entrez le nom du groupe de déploiement, sélectionnez le rôle de service (le 1er rôle créé) que vous avez créé, et sélectionnez le type de déploiement comme in-place :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-235.png)
_Créer le groupe de déploiement CodeDeploy_

Dans la section Environment configuration, sélectionnez "Amazon EC2 instances" et sélectionnez la clé comme Name. Entrez le nom de votre instance EC2 dans la valeur.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-236.png)
_Configuration de l'environnement du groupe de déploiement Code_

Dans la section Agent configuration, sélectionnez Never, car nous avons déjà installé l'agent CodeDeploy. Sélectionnez "CodeDeployDefault.AllAtOnce" dans la section Deployment settings. Laissez la case "Enable load balancing" décochée. Enfin, cliquez sur le bouton "Create a deployment group".

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-237.png)
_Configurations du groupe de déploiement CodeDeploy_

## Comment créer le CodePipeline

AWS CodePipeline vous aide à automatiser vos pipelines de release pour des mises à jour d'applications et d'infrastructure rapides et fiables. Il est maintenant temps de créer notre CodePipeline. Dans la console AWS, recherchez "CodePipeline" dans la barre de recherche.

Sélectionnez "Pipelines" dans le panneau de gauche et cliquez sur le bouton "Create pipeline".

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-238.png)
_Créer le CodePipeline_

Entrez le nom du pipeline et le nom du rôle. Rappelez-vous, nous avons créé des rôles pour EC2 et CodeDeploy, mais pas pour CodePipeline. AWS le crée par défaut à partir d'ici.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-239.png)
_Paramètres CodePipeline_

### Ajouter l'étape Source

Dans cette étape, nous devons connecter notre dépôt avec CodePipeline pour déployer les changements immédiatement après que le code soit pushé.

Nous utiliserons GitHub comme source. Choisissez GitHub (version 2) comme fournisseur source, et cliquez sur le bouton "Connect to GitHub". Cela ouvrira une nouvelle fenêtre contextuelle. Cliquez sur le bouton "Connect to GitHub".

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-240.png)
_CodePipeline ajout de l'étape source_

Cela vous mènera à la page d'autorisation GitHub où vous devrez vous connecter à votre compte GitHub. Cliquez sur le bouton "Install a new app".

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-241.png)
_Autorisation Github CodePipeline_

Choisissez "Only select repositories" et choisissez votre dépôt en dessous.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-242.png)
_Installation du connecteur AWS pour GitHub_

Une fois installé, il vous demandera votre mot de passe. Cliquez sur le bouton "Connect" une fois l'authentification terminée.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-243.png)
_Connexion de GitHub à AWS_

Après vous être connecté à GitHub, sélectionnez le nom du dépôt et le nom de la branche. Pour démarrer le CodePipeline lors d'un changement de code, il est important de cocher la case "Start the pipeline on source code change" – sinon le déploiement automatique ne se produira pas. Pour "Output and artifact format", sélectionnez "CodePipeline default" et cliquez sur le bouton "Next".

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-244.png)
_CodePipeline - Sélection du dépôt de code source_

L'étape suivante consiste à ajouter l'étape de build, mais comme nous déployons une application simple, nous n'en avons pas besoin. Les grandes entreprises préfèrent builder leur application à l'aide du service AWS CodeBuild. Gardons les choses simples et sautons l'étape de build.

Si vous voulez que j'écrive sur CodeBuild, faites-le moi savoir, j'essaierai de le couvrir dans mes prochains tutoriels.

### Ajouter l'étape de déploiement

À l'étape de déploiement, choisissez "AWS CodeDeploy" pour le "Deploy provider" et sélectionnez la région où vous avez créé l'application CodeDeploy ci-dessus. Ensuite, sélectionnez le "Application name" et le "Deployment group" que nous avons créés dans les étapes précédentes et cliquez sur le bouton "Next".

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-245.png)
_CodePipeline - Ajout de l'étape de déploiement_

La dernière étape est "Review". Vérifiez tout attentivement et cliquez sur le bouton "Create pipeline". Une fois le pipeline créé, il lancera le processus de déploiement. Si vous avez suivi toutes les étapes ci-dessus, le pipeline devrait indiquer "Succeeded" dès votre premier build.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-246.png)
_Pipeline réussi_

### Comment vérifier le déploiement automatique

Maintenant, vérifions si le déploiement automatique fonctionne correctement. Voici la page d'accueil de notre projet :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-247.png)
_Application Next.js Hello World_

Changeons le texte de "Hello World" à "Welcome to 5minslearn" et pushez le code sur GitHub.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-248.png)
_Différence de code Git_

Et voilà ! Le CodePipeline s'est déclenché automatiquement et les modifications ont été déployées avec succès.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-249.png)
_CodeDeploy déclenché automatiquement lors des changements de code dans Git_

Maintenant, allez sur "http://ec2-public-ip-address:3000/", vous verrez la page suivante :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-250.png)
_Application Next.js après déploiement automatique_

Félicitations ! 🥳 Nous avons terminé avec succès la configuration du déploiement automatique pour une application Next.js.

## Conclusion

Dans cet article, nous avons appris comment déployer Next.js manuellement sur EC2 et configurer le déploiement automatique à l'aide des services AWS tels que CodeDeploy et CodePipeline.

J'espère que vous avez apprécié la lecture de cet article ! Si vous êtes bloqué à n'importe quel moment, n'hésitez pas à envoyer vos questions à mon [e-mail](mailto:arun@gogosoon.com). Je serai ravi de vous aider !

Si vous souhaitez en savoir plus sur AWS, abonnez-vous à ma [newsletter](https://5minslearn.gogosoon.com/?ref=fcc_nextjs_deployment) ([https://5minslearn.gogosoon.com/](https://5minslearn.gogosoon.com/?ref=fcc_nextjs_deployment)) et suivez-moi sur les réseaux sociaux.