---
title: Comment construire et pousser des images Docker vers AWS ECR
subtitle: ''
author: Kaushal Joshi
co_authors: []
series: null
date: '2022-04-27T16:38:22.000Z'
originalURL: https://freecodecamp.org/news/build-and-push-docker-images-to-aws-ecr
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/How-to-Build-and-Push-Docker-Images-to-AWS-ECR.png
tags:
- name: AWS
  slug: aws
- name: containers
  slug: containers
- name: Docker
  slug: docker
seo_title: Comment construire et pousser des images Docker vers AWS ECR
seo_desc: "Docker is a platform that helps you build, run, and ship applications in\
  \ a seamless and error-free way. \nYou've likely come across a scenario where the\
  \ code is running on your machine, but is somehow throwing errors on someone else's\
  \ machine. \nWell, ..."
---

Docker est une plateforme qui vous aide à construire, exécuter et livrer des applications de manière transparente et sans erreur. 

Vous avez probablement rencontré un scénario où le code s'exécute sur votre machine, mais génère des erreurs sur la machine de quelqu'un d'autre. 

Eh bien, Docker a été créé pour résoudre ce problème précis.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-166.png)
_source de l'image : internet_

Dans cet article, nous allons couvrir quatre concepts majeurs :

1. Comment installer, configurer et paramétrer Docker
2. Comment ajouter Docker à votre projet
3. Comment installer et configurer AWS CLI sur votre système
4. Comment utiliser AWS ECR pour héberger une image Docker dans un emplacement distant

## Prérequis

Voici ce dont vous aurez besoin pour suivre ce tutoriel :

1. Un compte Docker
2. Connaissance de base de Docker : cas d'utilisation, commandes
3. Un compte AWS
4. Connaissance de base d'AWS : console, IAM, utilisateurs, ECS, ECR
5. Une simple application web que nous pouvons utiliser pour ce projet

Si vous n'avez pas d'application web ou si vous souhaitez simplement essayer, vous pouvez cloner ce projet :

%[https://github.com/joshi-kaushal/members-only]

L'application ci-dessus est une application Express.js avec MongoDB Compass comme base de données. Nous allons créer une image Docker du projet, la pousser vers AWS ECR et y accéder via AWS ECS. 

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-183.png)

## Installation de Docker

La seule chose que vous devez faire si vous utilisez Windows ou Mac est d'installer l'application Docker Desktop. Elle installe tout ce dont vous avez besoin et offre une belle interface graphique pour l'interaction.

Rendez-vous sur le [site officiel](https://www.docker.com/get-started/) et installez le setup. Vous devez également créer un compte Docker pour une utilisation ultérieure. Si vous êtes sous Linux, [cette page](https://hub.docker.com/search?q=&type=edition&offering=community&operating_system=linux&utm_source=docker&utm_medium=webreferral&utm_campaign=dd-smartbutton&utm_location=module) ou une simple recherche sur [YouTube](https://www.youtube.com/results?search_query=install+docker+on+linux) vous aidera à le faire.

Pour vérifier si l'installation est réussie, exécutez `docker --version` dans le terminal. Il devrait afficher la version et le build installés dans votre système.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-151.png)
_Vérification de la réussite de l'installation de Docker_

### Connexion à Docker

Rendez-vous sur [hub.docker.com/signup](https://hub.docker.com/signup) et créez votre compte. Pour connecter votre système à votre compte Docker, exécutez `docker login` dans le terminal. 

Vous verrez **Login succeeded** s'afficher dans le terminal. 

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-149.png)
_Vérification de la réussite de la connexion à Docker_

Une fois Docker installé et configuré dans votre système, passons à la section suivante.

## Comment Dockeriser Votre Projet

Par **Dockeriser**, j'entends configurer votre projet existant avec Docker et le containeriser. 

Créez un fichier nommé `Dockerfile` sans aucune extension à la racine de votre répertoire de projet. Il contient le code nécessaire pour construire une image Docker et exécuter l'application dockerisée en tant que conteneur. 

Si vous utilisez VS Code, l'extension [Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker) sera très utile.

### Comment Configurer le Dockerfile

En tant que configuration minimale, collez le code suivant dans le `Dockerfile`.

```
FROM node:12.17.0

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

ENV PORT=3000

EXPOSE 3000

CMD [ "npm", "start" ]
```

Avant de comprendre ces instructions, créez un fichier `.dockerignore` et ajoutez `node_modules` dedans. Il fonctionne de la même manière que `.gitignore`. 

Passons maintenant en revue ce code :

* `FROM` : Définit l'image de base pour les instructions suivantes. Pour simplifier, nous utiliserons une image Node.js officiellement supportée. J'utilise la version exacte mentionnée dans mon `package.json`, alors changez-la en conséquence si vous utilisez une version différente de Node. 
* `WORKDIR` : Ajoute le code source de notre répertoire de travail actuel à l'image.
* `COPY` : Copie les fichiers et dossiers de la source vers la destination dans le système de fichiers de l'image. Nous copions `package.json` et `package-lock.json`. Cette commande garantit que nous avons une liste de dépendances à installer dans notre conteneur Docker.
* `RUN` : Exécute la commande donnée. Comme nous avons `package.json` de l'étape précédente, nous pouvons installer les dépendances dans notre conteneur. 
* `COPY` : Maintenant, nous copions tout du répertoire du projet vers notre conteneur. Comme les deux sont dans le même répertoire, nous utilisons `.` qui indique le répertoire de travail actuel. `node_modules` n'est pas copié puisque nous l'avons ajouté dans `.dockerignore`.
* `ENV` : Définit une variable d'environnement pour le conteneur Docker.
* `EXPOSE` : Lorsque nous exécutons ce conteneur, nous voulons écouter notre application sur un port particulier. `EXPOSE` nous permet d'accéder à l'application containerisée publiquement. Il n'a pas besoin d'être le même que `ENV`, mais cela réduit la complexité :)
* `CMD` : Il ne peut y avoir qu'une seule commande `CMD` dans une image, qui indique au conteneur comment démarrer l'application. Remarquez que nous avons passé un tableau et la commande nécessaire en tant qu'éléments. Cela s'appelle la **forme exec** et cela nous permet d'exécuter la commande sans démarrer une session shell. 

Nous avons configuré tout ce dont nous avons besoin pour créer un fichier Docker. Créons maintenant une image Docker !

### Comment Créer une Image Docker

Vous utilisez la commande `docker build` pour créer une build d'image Docker. Il existe plusieurs paramètres que nous pouvons passer avec la commande. Mais celui que nous allons utiliser ici est `-t`. Cela donne à votre image une étiquette de nom qui la rend facile à retenir ainsi qu'à accéder. 

Il n'y a pas de manière standardisée de nommer votre image, mais normalement vous verriez ceci : nom d'utilisateur Docker suivi d'une barre oblique (`/`) et ensuite le numéro de version séparé par un deux-points (`:`). 

```
docker build -t <nom-étiquette> .
```

Le deuxième argument est l'emplacement du Dockerfile. Comme le nôtre est dans le même répertoire, nous pouvons mettre un point (.).

Lorsque vous exécutez la commande, vous verrez que les étapes sont exécutées dans le même ordre que celui dans lequel elles sont écrites dans le `Dockerfile`. Une fois terminé, il affichera **Successfully built <baseID>** dans le terminal.

Vous pouvez utiliser `baseID` pour accéder à l'image Docker particulière au lieu d'utiliser son étiquette de nom.

Vous pouvez vérifier cela en regardant la section _Images_ dans l'application Docker. Vous pouvez également voir le conteneur local dans la section `Containers/ Apps`.

Pour l'instant, exécutons notre image Docker dans notre système local.

```
docker run -p 3000:3000 <nom-étiquette>
```

Rappelez-vous, vous pouvez également utiliser `<baseID>` au lieu de `<nom-étiquette>`.

### Redirection de Port

Si vous exécutez la commande ci-dessus sans `-p 3000:3000`, vous ne verrez rien sur le port 3000. Cela est dû au fait que même si nous avons exposé le port 3000 dans le Dockerfile, si nous ne l'avons pas rendu accessible au monde extérieur,

Le drapeau `-p` nous permet de faire une redirection de port du conteneur vers notre machine locale.

La redirection de port est en fait un concept énorme, mais c'est tout ce que nous devons savoir pour l'instant. 

Visitez [`http://localhost:3000/`](http://localhost:3000/) dans votre navigateur. Eh bien, vous avez créé un conteneur Docker et l'exécutez sur votre machine locale. Félicitations !

Habituellement, vous poussez cette image vers un type de registre de conteneurs pour l'utiliser dans des scénarios réels. Cela pourrait être un Docker Hub ou autre chose. Nous utilisons Amazon Elastic Container Service fourni par AWS.

Pour une communication fluide entre l'image Docker locale et ECS, nous devons configurer AWS CLI dans notre système. Voyons comment faire.

## Comment Configurer AWS CLI 

L'interface de ligne de commande AWS est un outil en ligne de commande qui nous permet d'utiliser les ressources AWS via notre terminal. Tout ce que nous pouvons faire dans la console AWS ou l'interface graphique web peut également être fait avec CLI.

Nous devons configurer et paramétrer AWS CLI dans notre système afin d'utiliser les services ECS localement. Pour vérifier si vous avez déjà AWS CLI installé, exécutez cette commande dans le terminal :

```
aws cli
```

Si la commande ne répond avec rien, CLI n'est pas configuré. Si elle répond, n'hésitez pas à passer à la section suivante. 

### Comment Installer AWS CLI 

J'utilise Windows 10 avec WSL2. Mais la procédure est similaire pour Mac OS et Linux Debian.

Rendez-vous sur [ce site](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) et suivez les étapes pour votre distribution. Pour Windows, vous devez télécharger un MSI. Ensuite, une invite d'installation s'affichera. Suivez simplement les étapes et il sera installé en quelques minutes.

Maintenant, redémarrez le terminal et exécutez `aws cli` à nouveau. Configurons un utilisateur pour ce profil local.

### Comment Configurer un Utilisateur Local pour AWS CLI

Rendez-vous dans la section IAM de la console AWS sur le web. Suivez ce GIF pour créer un nouvel utilisateur :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/ecs-new-user.gif)
_créer un utilisateur avec les droits appropriés_

**À retenir :**

1. **Accès par clé - Accès programmatique** est coché lorsque vous entrez le nom du nouvel utilisateur.
2. Ajoutez une politique d'utilisateur qui donne un accès complet à ECS. Le nom de la politique est `AmazonECS_FullAccess`.
3. Notez l'`ID de la clé d'accès` et la `Clé d'accès secrète`, car nous devrons les utiliser plus tard.

Retournez à notre bon vieux terminal. Exécutez la commande de configuration dans le terminal et entrez votre clé d'accès, votre clé d'accès secrète et la région préférée. Passez le `format de sortie par défaut` pour l'instant.

```
aws configure
```

Vérifiez la configuration en exécutant la commande `aws configure list`.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-152.png)
_Vérification de la configuration AWS CLI_

Félicitations ! Nous avons configuré avec succès AWS CLI avec notre terminal local. Il est maintenant temps de pousser notre image Docker vers Amazon ECR.

## Services de Conteneurs Élastiques AWS

Cela fait longtemps que nous avons parlé de Docker. Nous avons créé une image et un conteneur Docker locaux. Nous devons la publier depuis notre dépôt Docker local vers AWS ECR. Cela se fait via ECS

Qu'est-ce que ECS ? Vous pourriez demander.

> Amazon Elastic Container Services, alias ECS, est un service d'orchestration de conteneurs entièrement géré qui facilite le déploiement, la gestion et la mise à l'échelle d'applications containerisées.

Et Elastic Container Registry ou ECR est le registre pour les conteneurs Docker stockés dans ECS. Nous utiliserons ECS pour pousser notre conteneur Docker vers ECR.

### Comment Créer un Dépôt dans ECR

Pour simplifier, je suggère de garder le même nom que votre projet.

```
aws ecr create-repository --repository-name <nom_dépôt> --region <nom_région>
```

Si vous n'êtes pas sûr de `nom_région`, mettez `us-east-1`. Cela créerait votre dépôt dans la région US EAST-1. Une fois terminé, il affichera un objet JSON comme réponse dans le terminal.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-153.png)

Pour plus de sécurité, vérifiez la console AWS et voyez si un dépôt est créé :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/aws-ecr-repo.gif)
_vérification si un dépôt est créé_

**À retenir :**

1. Vous ne verrez aucune image sous le dépôt. Parce que nous n'avons encore poussé aucune image.
2. Notez l'`URI` de votre dépôt. Nous devrons l'utiliser bientôt.

### Comment Pousser une Image Docker vers ECR

Chaque pièce a été créée individuellement jusqu'à présent. Il est temps de joindre chaque pièce et de compléter le puzzle. 

Pour que Docker pousse l'image vers ECR, nous devons d'abord authentifier nos identifiants Docker avec AWS. Nous utilisons la commande `get-login-password` qui récupère et affiche un jeton d'authentification en utilisant l'API _GetAuthorizationToken_ que nous pouvons utiliser pour nous authentifier auprès d'un registre Amazon ECR.

```
aws ecr get-login-password --region <nom_région>
```

Utilisez le même `nom_région` que celui que vous avez utilisé lors de la création d'un dépôt. Stockez le jeton chiffré quelque part pour un instant.

Prenez une profonde inspiration maintenant. Nous avons besoin de deux choses que je vous ai dit de sauvegarder quelque part. La première est le jeton que je viens de mentionner et la seconde est l'URI du dépôt de l'étape précédente. 

Vous avez compris ? Allons-y !

```
 aws ecr --region <région> | docker login -u AWS -p <jeton_chiffré> <uri_dépôt>
```

Inutile de dire, mettez la même région où se trouve votre dépôt.

Nous interrogeons l'API ECR fournie par AWS CLI. Plus tard, nous faisons le pipeline de la connexion Docker.

* `-u AWS` : Utilisateur par défaut fourni par AWS.
* `-p <jeton_chiffré>` : Mot de passe que nous avons récupéré à l'étape précédente.
* `uri_dépôt` : URI de notre dépôt.

Si la connexion est réussie, **Login Succeeded** s'affichera dans le terminal. 

### Comment Étiqueter une Image Docker Locale

Cette commande étiquette une image Docker locale avec le dépôt ECR.

```
docker tag <étiquette_image_source> <uri_dépôt_ecr_cible>
```

* `étiquette_image_source` : Le nom que vous avez donné pour la commande `docker build`. Si vous suivez ce guide, c'est `nom_utilisateur/nom_image:étiquette`.
* `uri_dépôt_ecr_cible` : URI du dépôt ECR.

### Comment Pousser l'Image Docker vers ECR

L'étape finale – la dernière pièce du puzzle !

La commande suivante pousse le fichier Docker local vers le dépôt ECR distant. Selon la taille de l'image, cela prendra un certain temps pour se terminer.

```bash
docker push <uri-dépôt-ecr>
```

Hourra ! Nous avons réussi 🎉

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-182.png)

Vous pouvez voir l'image téléchargée dans la console AWS. Allez dans ECR, cliquez sur les dépôts et ouvrez le dépôt ECR que nous avons téléchargé il y a quelques minutes. Copiez l'`URI de l'image` si vous souhaitez l'utiliser davantage. 

## Conclusion

Dans cet article, nous avons couvert comment déployer une image Docker sur AWS ECS. Vous pouvez utiliser ce conteneur Docker reposant dans ECR pour héberger votre application sur le serveur. Cela pourrait être AWS EC2 ou autre chose. 

Docker et AWS sont largement utilisés pour développer des applications à grande échelle. Avoir une idée de la manière dont ces choses fonctionnent ensemble devrait vous aider à construire des applications à grande échelle à l'avenir.

Cela dit, j'espère que cet article vous a aidé dans votre travail, vos études ou vos apprentissages. Si c'est le cas, vous pourriez également trouver mes autres articles utiles. 

Je écrite principalement sur mon [blog personnel](https://clumsycoder.hashnode.dev/) et [freeCodeCamp](https://www.freecodecamp.org/news/author/clumsycoder/). Si vous voulez dire bonjour, je suis le plus actif sur [Twitter](https://twitter.com/clumsy_coder), [LinkedIn](https://www.linkedin.com/in/7JKaushal) et [Showwcase](https://www.showwcase.com/clumsycoder).

Bon déploiement ! 🐳⛴️