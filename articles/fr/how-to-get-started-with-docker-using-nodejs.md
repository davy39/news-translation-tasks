---
title: Comment débuter avec Docker en utilisant NodeJS
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2023-03-20T14:28:45.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-with-docker-using-nodejs
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/How-to-get-started-with-Docker-using-NodeJS.png
tags:
- name: container
  slug: container
- name: Docker
  slug: docker
- name: node
  slug: node
seo_title: Comment débuter avec Docker en utilisant NodeJS
seo_desc: "You might have seen a tool with the logo of a whale lifting some square\
  \ containers. Yes, I am talking about Docker. \nThe Docker logo actually symbolizes\
  \ software that brings together a huge amount of organized information, hinting\
  \ at its convenience...."
---

Vous avez peut-être déjà vu un outil avec le logo d'une baleine transportant des conteneurs carrés. Oui, je parle de Docker. 

Le logo de Docker symbolise en fait un logiciel qui rassemble une énorme quantité d'informations organisées, suggérant ainsi sa commodité.

De nombreuses applications d'entreprise utilisent aujourd'hui des déploiements basés sur Docker (également appelés déploiements conteneurisés). C'est donc une compétence précieuse à posséder en tant que développeur.

Ce tutoriel sera idéal pour ceux qui ne connaissent rien d'autre que le terme « Docker ».

Dans cet article, vous découvrirez les fondamentaux de Docker, vous construirez votre propre image Docker et vous la publierez sur le Docker Hub.

## Pourquoi avez-vous besoin de Docker ?

Comprenons pourquoi nous avons besoin de Docker à l'aide d'un exemple simple.

Supposons que vous rejoigniez une nouvelle entreprise et que vous soyez affecté à un projet extrêmement volumineux. Vous recevez un ordinateur portable tout neuf et vous êtes prêt à commencer à développer.

La première étape lors de l'intégration dans un projet est de configurer l'environnement de développement. Comme il s'agit d'un projet d'entreprise massif, la configuration de l'environnement de développement prend énormément de temps. Vous devrez peut-être installer des dépendances spécifiques au projet, des outils et bien plus encore.

En cours de route, vous pourriez rencontrer des erreurs que vous résoudrez la plupart du temps en suivant le guide README, mais certaines pourraient apparaître pour la première fois (en raison de la configuration de l'ordinateur) et vous devrez les résoudre par vous-même.

Imaginez si vous deviez suivre ce même processus pour de grandes équipes composées de nombreux membres. Ce serait horrible à gérer, n'est-ce pas ?

C'est là que Docker s'avère vraiment utile. Docker va créer des applications conteneurisées qui s'exécutent sur n'importe quel type d'environnement et qui contiennent toutes les dépendances nécessaires. Ainsi, la configuration de l'environnement de développement ne nécessite plus qu'une seule commande. Docker a de nombreux cas d'utilisation – ce scénario n'en est qu'un parmi d'autres.

En utilisant Docker, nous pouvons standardiser les opérations des applications, livrer le code plus rapidement et déployer de manière transparente en production.

## Comment fonctionne Docker ?

Docker offre un moyen standardisé de développer, tester et déployer du code.

Vous pouvez considérer Docker comme une machine virtuelle avancée et surpuissante. Apprenons-en plus à ce sujet avec un exemple.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-171.png)
_Comparaison entre une machine virtuelle et Docker_

Avant de commencer à travailler sur Docker, nous devons comprendre certains fondamentaux de son fonctionnement. Il s'agit de :

1. Docker Engine
2. Conteneur Docker
3. Image Docker

### Qu'est-ce que Docker Engine ?

Le moteur Docker (Docker Engine) est une technologie de conteneurisation open source que vous pouvez utiliser pour construire une application conteneurisée.

Nous pouvons utiliser Docker Engine sur diverses plateformes via Docker Desktop ou une installation binaire. Pour simplifier, le logiciel qui héberge les conteneurs est appelé Docker Engine.

### Qu'est-ce qu'un conteneur Docker ?

Un conteneur est une unité logicielle standard qui regroupe le code et toutes les dépendances requises pour exécuter une application sur différentes plateformes ou environnements informatiques.

Les conteneurs sont totalement isolés de l'environnement informatique, de sorte que les applications s'exécutent rapidement et de manière fiable d'un environnement à un autre.

Les conteneurs Docker sont construits à partir d'images de conteneurs.

### Qu'est-ce qu'une image Docker ?

Une image de conteneur Docker est un package logiciel léger, autonome et exécutable qui comprend tout ce qui est nécessaire pour exécuter une application. Elle inclut le code, le runtime, les outils système, les bibliothèques système et les paramètres.

Comme nous l'avons vu, les conteneurs sont construits à partir d'images. Les images deviennent des conteneurs lorsqu'elles commencent à s'exécuter sur un Docker Engine.

### Cas d'utilisation de Docker

Docker vous donne la possibilité d'exécuter une application dans n'importe quel type d'environnement, lequel est complètement isolé de l'environnement actuel. Cet environnement isolé est appelé un conteneur.

Cette isolation et cette sécurité nous permettent d'exécuter autant de conteneurs que nous le souhaitons sur un hôte. Docker aide les développeurs à travailler dans un environnement standardisé en utilisant des conteneurs locaux qui fournissent tous les packages et dépendances nécessaires pour exécuter une application.

Voyons quelques cas d'utilisation de Docker :

1. Les développeurs peuvent écrire du code localement et partager leur travail en utilisant des conteneurs Docker.
2. Vous pouvez utiliser Docker pour déployer vos applications dans un environnement de test/production et exécuter des tests automatisés et manuels.
3. Lorsque les développeurs doivent corriger quelque chose, ils peuvent facilement effectuer les changements et pousser l'image Docker vers l'environnement de test ou de production.

Tout comme Git, nous pouvons utiliser Docker lors de modifications apportées à nos projets. Si nous faisons des changements, nous pouvons simplement pousser les images Docker et les récupérer sur la machine hôte. Plus aucun changement n'est nécessaire sur le serveur hôte.

Voici les étapes de déploiement que vous suivriez si vous n'utilisiez pas Docker :

1. Récupérer/cloner le code depuis Git.
2. Installer les dépendances, exécuter les migrations, etc., sur la machine hôte.
3. Démarrer l'application.

Ces étapes doivent être répétées sur chaque serveur, qu'il s'agisse d'un environnement de test ou de production.

Voici les étapes de déploiement avec Docker :

1. Récupérer l'image Docker (`docker pull`).
2. Exécuter le conteneur sur la machine hôte (`docker run`).

### Qu'est-ce que Docker Hub ?

Docker Hub est la plus grande communauté d'images Docker. Il vous permet de partager les images de conteneurs avec votre équipe ou la communauté Docker. Docker Hub est un peu comme GitHub. Ici, ce sont les images Docker qui résident au lieu du code du projet.

Vous pouvez également récupérer des images Docker open source. Pour l'utiliser, vous devez créer un compte sur Docker [hub](https://hub.docker.com).

Maintenant que vous en savez un peu plus sur le fonctionnement de Docker et son utilité, apprenons à conteneuriser une application.

## **Comment conteneuriser une application NodeJS en utilisant Docker**

### Prérequis :

1. Une compréhension de base des applications NodeJS.
2. L'application Docker Desktop.

Vous pouvez installer l'application Docker Desktop en suivant leur [documentation](https://docs.docker.com/desktop/install/windows-install/) d'origine.

Vous pouvez vérifier si Docker est installé sur votre machine en interrogeant sa version comme ceci :

```bash
docker -v
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-172.png)
_Trouver la version de Docker_

Commençons notre implémentation.

Au lieu de repartir de zéro, j'ai créé une API Express super simple qui n'expose qu'un seul point de terminaison (endpoint). J'ai poussé le code sur un dépôt public GitHub. Vous pouvez cloner le dépôt en exécutant la commande ci-dessous :

```bash
git clone https://github.com/5minslearn/node_with_docker.git
```

Voici la structure du projet :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-168.png)
_Structure simple d'un projet NodeJS_

J'ai créé un seul point de terminaison ("/") et l'appeler retournera "Greeting from 5minslearn". J'ai simplifié cela au maximum pour nous permettre de nous concentrer davantage sur Docker.

## Comment créer un Dockerfile

Maintenant, vous devrez créer un fichier nommé "Dockerfile" dans le répertoire racine. C'est le nom de fichier par défaut pour le moteur Docker. Collez le code suivant dans le fichier :

```dockerfile
FROM node:latest
WORKDIR /app
COPY . /app
RUN npm install
EXPOSE 8000
CMD ["npm","start"]
```

Comprenons ces commandes ligne par ligne.

Définir l'image parente est la première étape du moteur Docker. Vous devez définir l'image parente à partir de laquelle vous construisez le projet. Dans notre cas, c'est Node.

Il existe de nombreuses images parentes disponibles sur Docker Hub. Vous devez ensuite définir la variante de l'image (Image Variant). Je préfère toujours utiliser la dernière image node (latest).

```dockerfile
FROM node:latest
```

La deuxième étape consiste à définir le répertoire de travail dans Docker. Définissons notre répertoire de travail comme le répertoire `app`.

```dockerfile
WORKDIR /app
```

Copiez le projet dans le répertoire `app`. Assurez-vous d'exclure le répertoire `node_modules`. Nous verrons comment ignorer des fichiers/dossiers dans les étapes suivantes.

```dockerfile
COPY . /app
```

Dans la commande ci-dessus, le `.` indique que tous les fichiers et répertoires doivent être copiés dans le dossier `app`.

L'étape suivante consiste à installer les dépendances requises avec cette commande :

```dockerfile
RUN npm install
```

RUN est une étape de construction de l'image. L'état du conteneur après une commande RUN sera sauvegardé (Commit) dans l'image du conteneur. Un Dockerfile peut comporter de nombreuses étapes RUN qui peuvent se superposer les unes aux autres pour construire l'image.

Exposez le port sur lequel l'application doit s'exécuter.

```dockerfile
EXPOSE 8000
```

L'instruction EXPOSE informe Docker que le conteneur écoute sur les ports réseau spécifiés au moment de l'exécution.

Enfin, lancez la commande d'exécution :

```dockerfile
CMD ["npm", "start"]
```

CMD est la commande que le conteneur exécute par défaut lorsque nous lançons l'image construite.

**Conseil :** Je vous recommande d'installer l'extension `Docker` si vous utilisez VS Code. Elle vous aidera avec des suggestions pertinentes.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-174.png)
_Extension `Docker` pour VS Code_

## Comment ignorer des fichiers pour qu'ils ne soient pas copiés dans le conteneur Docker

Vous devez exclure les fichiers indésirables de la copie dans le conteneur. Le fichier `.dockerignore` vous aide à faire cela. Il fonctionne comme le `.gitignore` pour Git.

Vous pouvez y définir tous les fichiers que vous devez ignorer et que vous ne voulez pas copier.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-169.png)
_Utilisation de `.dockerignore` pour exclure les fichiers indésirables de la copie vers le conteneur_

Super ! Vous avez terminé la configuration de Docker. Lançons l'application.

## Comment construire des images Docker

Vous pouvez construire une image Docker en exécutant la commande `docker build`. Voici sa syntaxe :

```bash
docker build -t nom_image:numero_version .
```

`nom_image` indique le nom de l'image du conteneur et `numero_version` indique la version de l'image. Avez-vous remarqué le point (`.`) à la fin de la commande ? Il indique que l'image Docker doit être construite à partir du répertoire actuel.

J'ai décidé de nommer l'image `node_with_docker`. N'oubliez pas que le nom de l'image doit être préfixé par votre nom d'utilisateur Docker Hub. J'ai créé mon compte Docker Hub avec le nom d'utilisateur `aanandggs`. Ainsi, le nom de mon image est `aanandggs/node_with_docker`. Vous pouvez choisir d'entrer ce que vous voulez.

```bash
docker build -t aanandggs/node_with_docker:0.0.1 .
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-175.png)
_Exemple de sortie lors de la construction d'une image docker_

Une fois votre image Docker construite, vous pourrez la voir dans votre Docker Desktop.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-178.png)
_Image Docker dans Docker Desktop_

## Comment exécuter l'image Docker

Après avoir construit l'image Docker, l'étape suivante consiste à l'exécuter. Lorsqu'une image commence à s'exécuter sur un moteur Docker, elle devient un conteneur.

Exécutons notre image construite à l'étape précédente :

```bash
docker container run -d --name <nom_de_lapp> -p <port_local>:<port_docker> <nom_image>:<version>
```

```bash
docker container run -d --name docker_with_node -p 8000:8000 aanandggs/node_with_docker:0.0.1
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-179.png)
_Commande Docker pour créer et exécuter un conteneur_

Comprenons la commande ci-dessus.

Nous utilisons la commande `docker container run` pour créer et exécuter un nouveau conteneur à partir d'une image.

Le drapeau `-d` demande au conteneur de s'exécuter en arrière-plan (detach). Il affiche l'ID du conteneur.

Le paramètre `--name` donne un nom à notre conteneur.

Nous utilisons le paramètre `-p` pour publier le port d'un conteneur sur l'hôte. Cela liera le port `8000` de votre machine locale au port `8000` du conteneur Docker.

`nom_image:version` indique l'image et sa version que ce conteneur doit exécuter.

Vous pouvez consulter les conteneurs en cours d'exécution dans l'application Docker Desktop.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-180.png)
_Conteneur en cours d'exécution dans Docker Desktop_

Le tableau de bord montre que notre application est en cours d'exécution. Vérifions le résultat sur le navigateur en essayant d'accéder au point de terminaison "/". Tapez `localhost:8000/` dans votre navigateur. Vous devriez voir un message similaire à celui de la capture d'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-181.png)
_Résultat de l'exécution de l'application NodeJS_

Vous avez réussi à exécuter une application avec un conteneur Docker.

**Note :** Vous pouvez lier n'importe quel port local au port Docker. Assurez-vous que votre port local n'est utilisé par aucun autre processus.

## Comment pousser l'image sur le Docker Hub

Créez votre profil sur Docker Hub. Revenez au terminal et exécutez la commande ci-dessous pour vous connecter à la CLI Docker :

```bash
docker login
```

Si vous rencontrez des problèmes lors de la connexion, suivez ce [document](https://docs.docker.com/desktop/get-started/#credentials-management-for-linux-users) pour vous connecter à Docker Hub sur votre machine.

Après une connexion réussie, vous pouvez pousser l'image vers Docker Hub.

```bash
docker push <image_docker>:<version_image>
```

```bash
docker push aanandggs/node_with_docker:0.0.1
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-182.png)
_Exemple de sortie lors de la poussée de l'image vers docker_

Hourra ! Les images Docker sont téléchargées sur Docker Hub.

Vous pourrez les voir dans la console Docker Hub.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-184.png)
_Image Docker poussée dans Docker Hub_

Comme notre image est publique, n'importe qui sur Internet peut la récupérer (pull) et l'exécuter sur sa machine sans aucune installation tierce.

## Conclusion

Dans cet article, nous avons appris les bases fondamentales de Docker. Docker est un océan d'informations. Pour l'apprendre pleinement, vous devrez faire plus que simplement lire – vous devrez pratiquer en l'utilisant.

J'espère que vous avez apprécié cette lecture. On se retrouve dans un autre tutoriel intéressant. N'hésitez pas à me contacter sur LinkedIn si vous avez des questions.

Pour en savoir plus sur Docker, abonnez-vous à ma newsletter par e-mail sur mon [site](https://5minslearn.gogosoon.com/?ref=fcc_docker_getting_started) ([https://5minslearn.gogosoon.com](https://5minslearn.gogosoon.com/?ref=fcc_docker_getting_started)) et suivez-moi sur les réseaux sociaux.