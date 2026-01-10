---
title: Comment déployer une application Node.js sur Amazon Web Services en utilisant
  Docker
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-02T00:51:05.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-a-node-js-application-to-amazon-web-services-using-docker-81c2a2d7225b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KqO5C0953HQzafpnBYaTSg.jpeg
tags:
- name: AWS
  slug: aws
- name: Docker
  slug: docker
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Comment déployer une application Node.js sur Amazon Web Services en utilisant
  Docker
seo_desc: 'By Emmanuel Yusufu


  Plug: Originally published at Zeolearn magazine.

  For many more useful developer content like this article, visit the Zeolearn blog.
  The blog features articles centered on web/software development: AngularJS, ReactJS,
  NodeJS, Djang...'
---

Par Emmanuel Yusufu

> Plug: Originalement publié chez Zeolearn [magazine](https://www.zeolearn.com/magazine/how-to-deploy-a-node.js-application-to-amazon-web-services-using-docker).

> Pour beaucoup plus de contenu utile pour les développeurs comme cet article, visitez le [blog Zeolearn](https://www.zeolearn.com/magazine/how-to-deploy-a-node.js-application-to-amazon-web-services-using-docker). Le blog propose des articles centrés sur le développement web/logiciel : AngularJS, ReactJS, NodeJS, Django et Data Science (y compris l'apprentissage automatique, la science des données, Python et l'apprentissage profond).

#### Table des matières

1. Introduction  
2. Prérequis  
3. Un rapide aperçu de Docker et AWS  
4. Ce que nous allons déployer   
5. Création d'un Dockerfile  
6. Construction d'une image Docker  
7. Exécution d'un conteneur Docker  
8. Création du registre (ECR) et téléchargement de l'image de l'application  
9. Création d'une nouvelle définition de tâche  
10. Création d'un cluster  
11. Création d'un service pour l'exécuter  
12. Conclusion

### 1. Introduction

Écrire du code qui fait des choses est quelque chose que la plupart des développeurs connaissent. Parfois, nous devons prendre la responsabilité d'un administrateur système ou d'un ingénieur DevOps et déployer notre base de code en production où elle aidera une entreprise à résoudre des problèmes pour les clients.

Dans ce tutoriel, je vais vous montrer comment dockeriser une application Node.js et la déployer sur Amazon Web Service (AWS) en utilisant Amazon ECR (Elastic Container Registry) et ECS (Elastic Container Service).

### 2. Prérequis

Pour suivre ce tutoriel, vous aurez besoin des éléments suivants :

1. **Node et Npm** : [Suivez ce lien](https://nodejs.org/en/) pour installer les dernières versions.
2. Connaissance de base de Node.js.
3. **Docker** : L'installation fournit Docker Engine, Docker CLI client et d'autres choses intéressantes. Suivez les [instructions](https://docs.docker.com/install/) pour votre système d'exploitation. Pour vérifier si l'installation a fonctionné, exécutez ceci dans le terminal :

```
docker --version
```

La commande ci-dessus devrait afficher le numéro de version. Si ce n'est pas le cas, l'installation ne s'est pas terminée correctement.

4. **Compte AWS** : Inscrivez-vous pour un niveau gratuit. Il y a une période d'attente pour vérifier votre numéro de téléphone et votre carte bancaire. Après cela, vous aurez accès à la console.

5. **AWS CLI** : Suivez les [instructions](https://aws.amazon.com/cli/) pour votre système d'exploitation. Vous devez avoir Python installé.

### 3. Un rapide aperçu de Docker et AWS

**Docker** est un logiciel open source qui vous permet d'emballer une application avec les dépendances et l'environnement requis dans un « conteneur » que vous pouvez expédier et exécuter n'importe où. Il est indépendant des plateformes ou du matériel, et donc l'application conteneurisée peut s'exécuter dans n'importe quel environnement de manière isolée.

Les conteneurs Docker résolvent de nombreux problèmes, comme lorsqu'une application fonctionne sur l'ordinateur d'un collègue mais ne s'exécute pas sur le vôtre, ou qu'elle fonctionne dans l'environnement de développement local mais ne fonctionne pas lorsque vous la déployez sur un serveur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*E0SsYen436st84JVeBz4dQ.png)

**Amazon Web Services (AWS)** offre un service de cloud computing fiable, évolutif et peu coûteux pour les entreprises. Comme je l'ai mentionné précédemment, ce tutoriel se concentrera sur l'utilisation des services ECR et ECS.

### 4. Ce que nous allons déployer

Construisons rapidement une application d'exemple que nous utiliserons pour ce tutoriel. Ce sera une application Node.js très simple.

Entrez les commandes suivantes dans votre terminal :

```
// créer un nouveau répertoire
mkdir sample-nodejs-app

// changer de répertoire
cd sample-nodejs-app

// Initialiser npm
npm init -y

// installer express
npm install express

// créer un fichier server.js
touch server.js
```

Ouvrez `server.js` et collez le code ci-dessous :

```js
// server.js

const express = require('express')
const app = express()

app.get('/', (req, res) => {
    res.send('Bonjour le monde depuis une application Node.js !')
})

app.listen(3000, () => {
    console.log('Le serveur est démarré sur le port 3000')
})
```

Démarrez l'application avec :

```
node server.js
```

Accédez-y sur [http://localhost:3000](http://localhost:3000). Vous devriez voir `Bonjour le monde depuis une application Node.js !` s'afficher dans votre navigateur. Le code complet est disponible sur GitHub.

Maintenant, prenons notre application très importante en production ?.

### 5. Création d'un Dockerfile

Nous allons commencer à dockeriser l'application en créant un seul fichier appelé `Dockerfile` à la base de notre répertoire de projet.

Le Dockerfile est le plan à partir duquel nos images sont construites. Ensuite, les images deviennent des conteneurs dans lesquels nous exécutons nos applications.

Chaque Dockerfile commence avec une image de base comme fondation. Il existe deux façons d'aborder la création de votre Dockerfile :

1. Utiliser une **image de base d'OS simple** (par exemple, Ubuntu OS, Debian, CentOS, etc.) et installer un environnement d'application tel que Node.js OU
2. Utiliser une **image de base prête pour l'environnement** pour obtenir une image OS avec un environnement d'application déjà installé.

Nous allons procéder avec la deuxième approche. Nous pouvons utiliser l'[image officielle Node.js](https://hub.docker.com/_/node/) hébergée sur Dockerhub qui est basée sur Alpine Linux.

Écrivez ceci dans le Dockerfile :

```
FROM node:8-alpine
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . .
RUN npm install
EXPOSE 3000
CMD [ "node", "server.js" ]
```

Passons en revue ceci ligne par ligne pour voir ce qui se passe ici, et pourquoi.

```
FROM node:8-alpine
```

Ici, nous construisons notre image Docker en utilisant l'image officielle Node.js de [Dockerhub](https://hub.docker.com/_/node/) (un dépôt pour les images de base).

* Commencez votre Dockerfile avec une instruction `[**FROM**](https://docs.docker.com/reference/builder/#from)`. C'est là que vous spécifiez votre image de base.
* L'instruction `[**RUN**](https://docs.docker.com/reference/builder/#run)` nous permettra d'exécuter une commande pour tout ce que vous voulez faire. Nous avons créé un sous-répertoire `/usr/src/app` qui contiendra notre code d'application dans l'image Docker.
* L'instruction `[**WORKDIR**](https://docs.docker.com/engine/reference/builder/#workdir)` établit le sous-répertoire que nous avons créé comme répertoire de travail pour toute instruction `RUN`, `CMD`, `ENTRYPOINT`, `COPY` et `ADD` qui le suit dans le `Dockerfile`. `/usr/src/app` est notre répertoire de travail.
* `[**COPY**](https://docs.docker.com/engine/reference/builder/#copy)` nous permet de copier des fichiers d'une source vers une destination. Nous avons copié le contenu de notre code d'application Node ( `server.js` et `package.json`) de notre répertoire actuel vers le répertoire de travail dans notre image Docker.
* L'instruction `[**EXPOSE**](https://docs.docker.com/engine/reference/builder/#expose)` informe Docker que le conteneur écoute sur les ports réseau spécifiés au moment de l'exécution. Nous avons spécifié le port 3000.
* Enfin, l'instruction `[**CMD**](https://docs.docker.com/reference/builder/#cmd)` spécifie la commande pour démarrer notre application. Cela indique à Docker comment exécuter votre application. Ici, nous utilisons `node server.js` qui est typiquement comment les fichiers sont exécutés dans Node.js.

Avec ce fichier complété, nous sommes maintenant prêts à construire une nouvelle image Docker.

### 6. Construction d'une image Docker

Assurez-vous que Docker est en cours d'exécution. Maintenant que nous avons défini notre Dockerfile, construisons l'image avec un titre en utilisant `-t` :

```
docker build -t sample-nodejs-app .
```

Cela affichera des hachages et des chaînes alphanumériques qui identifient les conteneurs et les images en disant « Successfully built » sur la dernière ligne :

```
Sending build context to Docker daemon  1.966MB
Step 1/7 : FROM node:6-alpine
 ---> 998971a692ca
Step 2/7 : RUN mkdir -p /usr/src/app
 ---> Using cache
 ---> f1aa1c112188
Step 3/7 : WORKDIR /usr/src/app
 ---> Using cache
 ---> b4421b83357b
Step 4/7 : COPY . .
 ---> 836112e1d526
Step 5/7 : RUN npm install
 ---> Running in 1c6b36b5381c
npm WARN sample-nodejs-app@1.0.0 No description
npm WARN sample-nodejs-app@1.0.0 No repository field.
Removing intermediate container 1c6b36b5381c
 ---> 93999e6c807f
Step 6/7 : EXPOSE 3000
 ---> Running in 7419020927f1
Removing intermediate container 7419020927f1
 ---> ed4ac8a31f83
Step 7/7 : CMD [ "node", "server.js" ]
 ---> Running in c77d34f4c873
Removing intermediate container c77d34f4c873
 ---> eaf97859f909
Successfully built eaf97859f909

// ne vous attendez pas aux mêmes valeurs dans votre terminal.
```

### **7. Exécution d'un conteneur Docker**

Nous avons construit l'image Docker. Pour voir les images précédemment créées, exécutez :

```
docker images
```

Vous devriez voir l'image que nous venons de créer comme la plus récente basée sur le temps :

![Image](https://cdn-media-1.freecodecamp.org/images/1*sQv-4uSIWP645Pp6MQu7Nw.png)

Copiez l'ID de l'image. Pour exécuter le conteneur, écrivez dans le terminal :

```
docker run -p 80:3000 {image-id}

// remplissez avec votre image-id
```

Par défaut, les conteneurs Docker peuvent établir des connexions vers l'extérieur, mais le monde extérieur ne peut pas se connecter aux conteneurs. `-p` publie tous les **ports exposés** vers les interfaces hôte. Ici, nous publions l'application sur le port 80:3000. Comme nous exécutons Docker localement, allez sur [http://localhost](http://localhost) pour voir.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ODVwlP_G5oIEWlYAxn1bXg.png)

À tout moment, vous pouvez vérifier les conteneurs Docker en cours d'exécution en tapant :

```
docker container ls
```

Enfin, vous pouvez arrêter le conteneur en cours d'exécution avec :

```
docker stop {image-id}
```

Laissez le démon Docker en cours d'exécution.

### 8. Créer un registre (ECR) et télécharger l'image de l'application

Amazon Elastic Container Registry (ECR) est un registre de conteneurs Docker entièrement géré qui facilite le stockage, la gestion et le déploiement des images de conteneurs Docker pour les développeurs. Amazon ECR est intégré à [Amazon Elastic Container Service (ECS)](https://aws.amazon.com/ecs/), simplifiant ainsi votre flux de travail de développement à production.

Le mot « Elastic » signifie que vous pouvez augmenter ou réduire la capacité selon vos besoins.

#### **Étapes** :

1. Allez sur la [console AWS](https://aws.amazon.com/) et connectez-vous.
2. Sélectionnez le service de conteneur EC2 et commencez

![Image](https://cdn-media-1.freecodecamp.org/images/1*QTkFrTPFM9PfMGLUgpBR_g.png)

3. La page de premier démarrage s'affiche, faites défiler vers le bas et cliquez sur annuler > entrer dans le tableau de bord ECS.

4. Pour vous assurer que votre CLI peut se connecter à votre compte AWS, exécutez dans le terminal :

```
aws configure
```

Si votre AWS CLI a été correctement installée, [**aws configure**](https://docs.aws.amazon.com/cli/latest/reference/configure/) demandera les informations suivantes :

```
$ aws configure
AWS Access Key ID [None]: accesskey
AWS Secret Access Key [None]: secretkey
Default region name [None]: us-west-2
Default output format [None]:
```

Obtenez les informations d'identification de sécurité de votre compte AWS sous votre nom d'utilisateur > Clés d'accès. Exécutez `aws configure` à nouveau et remplissez correctement.

4. Créez un nouveau dépôt et entrez un nom (**de préférence avec le même nom de conteneur que dans votre environnement de développement local pour la cohérence**).

Par exemple, utilisez `sample-nodejs-app`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*edZ_NxhuQUADW8KGUupAfA.png)

Suivez les 5 instructions de la console AWS pour construire, taguer et pousser les images Docker :

**Note : Les arguments des commandes suivantes sont les miens et seront différents des vôtres, alors suivez simplement les étapes décrites sur votre console.**

1. Récupérez la commande de connexion Docker que vous pouvez utiliser pour authentifier votre client Docker à votre registre :   
**Note** : Si vous recevez une erreur « Unknown options: - no-include-email », installez la dernière version de l'AWS CLI. [En savoir plus ici](https://docs.aws.amazon.com/cli/latest/userguide/installing.html).

```
aws ecr get-login --no-include-email --region us-east-2
```

2. Exécutez la commande `docker login` **qui a été retournée à l'étape précédente (il suffit de copier et coller)**. **Note** : Si vous utilisez Windows PowerShell, exécutez la commande suivante à la place :

```
Invoke-Expression -Command (aws ecr get-login --no-include-email --region us-east-2)
```

Cela devrait afficher : **Login Succeeded**.

3. Construisez votre image Docker en utilisant la commande suivante. Pour des informations sur la construction d'un fichier Docker à partir de zéro, voir les instructions [ici](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-basics.html). Vous pouvez sauter cette étape puisque notre image est déjà construite :

```
docker build -t sample-nodejs-app .
```

4. Avec une construction terminée, tagguez votre image avec un mot-clé (par exemple, **latest**) afin de pouvoir pousser l'image vers ce dépôt :

```
docker tag sample-nodejs-app:latest 559908478199.dkr.ecr.us-east-2.amazonaws.com/sample-nodejs-app:latest
```

5. Exécutez la commande suivante pour pousser cette image vers votre nouveau dépôt AWS :

```
docker push 559908478199.dkr.ecr.us-east-2.amazonaws.com/sample-nodejs-app:latest
```

### 9. Créer une nouvelle définition de tâche

Les tâches fonctionnent comme la commande `docker run` de l'interface de ligne de commande Docker mais pour plusieurs conteneurs. Elles définissent :

* Images de conteneurs (à utiliser)
* Volumes (le cas échéant)
* Réseaux Variables d'environnement
* Mappages de ports

À partir des **Définitions de tâches** dans le tableau de bord ECS, appuyez sur le bouton Créer une nouvelle définition de tâche (ECS) :

![Image](https://cdn-media-1.freecodecamp.org/images/1*BVt43mgwmiTAQF9CS0MClg.png)

Définissez un nom de tâche et utilisez les étapes suivantes :

* Ajouter un conteneur : sample-nodejs-app (celui que nous avons poussé).
* Image : l'URL de votre conteneur. La mienne est `559908478199.dkr.ecr.us-east-2.amazonaws.com/sample-nodejs-app`
* Limite souple : 512
* Mapper 80 (hôte) à 3000 (conteneur) pour sample-nodejs-app
* Variables d'environnement :

`NODE_ENV` : `production`

### 10. Créer un cluster

Un cluster est l'endroit où les conteneurs AWS s'exécutent. Ils utilisent des configurations similaires aux instances EC2. Définissez les éléments suivants :

* Nom du cluster : demo-nodejs-app-cluster
* Type d'instance EC2 : t2.micro

_(**Note** : vous sélectionnez les instances en fonction de la taille de votre application. Ici, nous avons sélectionné la plus petite. Votre sélection affecte le montant que vous serez facturé à la fin du mois. [Visitez ici](https://aws.amazon.com/ec2/pricing/on-demand/) pour plus d'informations). Merci à [Nicholas Kolatsis](https://www.freecodecamp.org/news/how-to-deploy-a-node-js-application-to-amazon-web-services-using-docker-81c2a2d7225b/undefined) pour avoir souligné que la sélection précédente de m4.large était coûteuse pour ce tutoriel._

* Nombre d'instances : 1
* Stockage EBS : 22
* Paire de clés : Aucune
* VPC : Nouveau

Lorsque le processus est terminé, vous pouvez choisir de cliquer sur « View cluster ».

### 11. Créer un service pour l'exécuter

Allez dans **Définition de tâche** > cliquez sur demo-nodejs-app > cliquez sur la dernière révision.

![Image](https://cdn-media-1.freecodecamp.org/images/1*LYPvdqq6UrE1IcaHsfIlcg.png)

À l'intérieur de la définition de tâche, cliquez sur le menu déroulant des actions et sélectionnez Créer un service

Utilisez les éléments suivants :

* Type de lancement : EC2
* Nom du service : demo-nodejs-app-service
* Nombre de tâches : 1

Passez les options et cliquez sur **Créer un service** et **Voir le service**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CLAS96g9wI9cjcZsG8VXIA.png)

Vous verrez son statut comme **EN ATTENTE**. Donnez-lui un peu de temps et il indiquera **EN COURS D'EXÉCUTION**.

Allez dans Cluster (via un lien depuis le service que nous venons de créer) > Instances EC2 > Cliquez sur l'instance de conteneur pour révéler le DNS public.

![Image](https://cdn-media-1.freecodecamp.org/images/1*G-gaEgSVdKpQNTBYw8517A.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*3nBfFGvKDCP7035goXXpMg.png)

Visitez le DNS public pour voir notre application ! Le mien est `[ec2-18-219-113-111.us-east-2.compute.amazonaws.com](http://ec2-18-219-113-111.us-east-2.compute.amazonaws.com/)`

![Image](https://cdn-media-1.freecodecamp.org/images/1*6P86otsleHPu9xy8w7cYzA.png)

### 12. Conclusion.

Félicitations pour avoir terminé cet article ! Récupérez le code pour la partie Docker depuis [Github](https://github.com/emmyyusufu/sample-nodejs-app).

N'hésitez pas à me soutenir ([devapparel.co](http://www.devapparel.co)) et à avoir l'air bien en le faisant. De plus, commentez ou partagez cet article. Merci pour la lecture !

> Plug: Encore une fois, pour beaucoup plus de contenu de qualité comme celui-ci, visitez le [blog Zeolearn](https://www.zeolearn.com/magazine/how-to-deploy-a-node.js-application-to-amazon-web-services-using-docker).