---
title: Comment Dockeriser une Application React – Un Tutoriel Pas à Pas
subtitle: ''
author: Kunal Nalawade
co_authors: []
series: null
date: '2023-07-18T14:54:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-dockerize-a-react-application
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/pexels-pixabay-39656--1-.jpg
tags:
- name: Docker
  slug: docker
- name: React
  slug: react
seo_title: Comment Dockeriser une Application React – Un Tutoriel Pas à Pas
seo_desc: 'Picture this: you have developed an application that is ready to be deployed.
  You have worked really hard on it, so you want to make sure it gets deployed seamlessly
  and the final product is both fast and reliable. Enter images and containers.

  Images...'
---

Imaginez ceci : vous avez développé une application prête à être déployée. Vous avez travaillé très dur dessus, donc vous voulez vous assurer qu'elle soit déployée de manière transparente et que le produit final soit à la fois rapide et fiable. Entrez les images et les conteneurs.

Les images et les conteneurs vous aident à empaqueter votre application et à l'exécuter dans un environnement léger et isolé. Les conteneurs permettent des déploiements plus rapides et scalables. Et ce n'est pas si difficile de commencer à les utiliser. Tout ce que vous avez à faire est d'écrire quelques scripts et d'exécuter quelques commandes pour avoir un conteneur opérationnel. N'est-ce pas génial ?

Dans ce tutoriel, je vais prendre une application React et vous montrer, étape par étape, comment construire une image, la pousser vers un registre distant et utiliser cette image pour exécuter votre application dans un conteneur.

Pour suivre ce tutoriel, je suppose que vous êtes déjà familiarisé avec les bases des images et des conteneurs. Je vais commencer par expliquer ce qu'est Docker, puis plonger dans le processus.

## Qu'est-ce que Docker ?

Docker est une plateforme open-source développée par [Docker, Inc.](https://www.docker.com/company/). Elle vous permet d'empaqueter votre application et ses dépendances et de tout exécuter dans un environnement isolé, appelé conteneur. Avec juste un petit ensemble d'instructions, vous pouvez facilement construire des images et les exécuter en tant que conteneurs.

Les conteneurs Docker sont extrêmement légers et efficaces. Grâce à l'isolement, chaque conteneur s'exécute différemment et les processus des conteneurs n'interfèrent pas les uns avec les autres. Docker dispose également de son propre système de contrôle de version, Docker Hub, dont nous parlerons plus tard dans le tutoriel.

Docker est largement utilisé par les technologies d'entreprise et les services cloud qui ont choisi d'adopter la conteneurisation pour des déploiements plus rapides. Enfin, Docker dispose d'une vaste communauté et d'un écosystème en constante expansion d'outils et de services. Pour plus d'informations, vous pouvez consulter la [documentation](https://docs.docker.com/get-started/).

D'accord, assez parlé de Docker (en fait, non). Vous êtes ici pour obtenir une pratique concrète et c'est ce que nous allons faire ici. Avant de commencer, vous devez d'abord installer Docker sur votre système. Référez-vous à [ce guide](https://docs.docker.com/get-docker/) pour installer Docker sur différents systèmes d'exploitation.

Exécutez la commande `docker --version` pour vérifier si Docker est installé.

## Comment Créer une Application React Simple

Utilisez la commande suivante pour configurer une application React simple.

```bash
create-react-app react-docker-example
```

Vous n'avez pas besoin d'ajouter d'autres dépendances au projet. Tout ce dont vous avez besoin est une application fonctionnelle. Exécutez `npm start` pour voir si l'application s'exécute correctement.

Une fois que l'application est en cours d'exécution et prête à être déployée, nous sommes prêts à commencer à la Dockeriser !

## Comment Écrire un Dockerfile

Pour construire une image de votre application, vous devez spécifier des instructions dans un Dockerfile. Les instructions de ce fichier seront exécutées les unes après les autres. Vous trouverez une référence à toutes les instructions [ici](https://docs.docker.com/engine/reference/builder/).

Une image Docker se compose de différentes couches empilées les unes sur les autres. Chaque instruction dans le Dockerfile ajoute une nouvelle couche par-dessus les existantes. Chaque couche de l'image est stockée sous forme de hachage SHA-256.

Notez que toutes les instructions ne créent pas de nouvelles couches. Certaines instructions comme `LABEL`, `ENV` et `ARG` ne sont définies que pour fournir des métadonnées pour l'image. Lisez [ceci](https://kodekloud.com/blog/docker-image-layers/) pour en savoir plus sur les couches d'image.

Passons en revue les instructions dont nous aurons besoin, une par une.

```python
FROM node:18-alpine
```

Cette instruction tire l'image de base d'un dépôt distant (dans ce cas, Docker Hub) et définit le point de départ pour les couches de l'image. La syntaxe pour spécifier l'image est

![](undefined align="left")

: où tag représente la version de l'image.

Puisque React est une application basée sur Node, nous allons tirer une image Node du dépôt. Spécifiez la version de l'image que vous souhaitez tirer. Vous pouvez obtenir une liste des versions [ici](https://hub.docker.com/_/node/tags).

Si vous spécifiez *latest*, il tirera la dernière version – c'est-à-dire que chaque fois que l'image est mise à niveau, elle récupérera toujours la dernière. Mais ce n'est pas une bonne pratique pour les applications déployées en production.

```python
WORKDIR /react-docker-example/
```

Cette commande définit le répertoire de travail pour toute commande que vous ajoutez dans le Dockerfile. Ainsi, lors de la construction de l'image, les commandes seront exécutées dans ce répertoire.

```python
COPY public/ /react-docker-example/public
COPY src/ /react-docker-example/src
COPY package.json /react-docker-example/
```

Ces instructions copieront les fichiers dont nous avons besoin dans le répertoire de travail. Nous n'avons besoin que des dossiers public et src (où se trouve votre code) et du fichier package.json pour exécuter l'application.

```python
RUN npm install
```

L'instruction `RUN` exécute toute commande en ajoutant une nouvelle couche par-dessus les couches actuelles, modifiant ainsi l'image. Cette image modifiée sera utilisée pour les étapes suivantes.

Dans ce cas, elle installe toutes les dépendances spécifiées dans le fichier `package.json`. C'est pourquoi nous n'avons pas copié le dossier `node_modules` dans le répertoire de travail. Le dossier sera créé après l'exécution de cette commande.

```python
CMD ["npm", "start"]
```

Cette instruction définit la commande qui sera exécutée lors du démarrage d'un conteneur à partir de l'image. Il ne peut y avoir qu'une seule instruction `CMD` dans le Dockerfile. S'il y en a plus d'une, seule la dernière sera prise en compte.

Puisque `npm start` est la commande utilisée pour démarrer une application React, nous spécifierons la même pour exécuter le conteneur.

## Comment Construire l'Image

Maintenant que nous avons écrit le Dockerfile, il est temps de construire l'image. Ouvrez votre terminal (ou cmd sous Windows) et exécutez la commande suivante.

```python
docker image build -t <image_name>:<tag> <path>
```

L'option `-t` spécifie le nom et le tag pour l'image. `<path>` représente le chemin dans lequel vous souhaitez exécuter la commande.

Nous nommerons l'image react-docker-example et lui donnerons le tag `latest`. Assurez-vous de changer de répertoire pour le répertoire racine du projet en utilisant `cd react-docker-example` avant d'exécuter la commande.

```python
docker image build -t react-example-image:latest .
```

Le `.` à la fin représente le répertoire courant.

Une fois que vous avez appuyé sur Entrée, cette commande exécutera chaque instruction dans le Dockerfile une par une.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-2023-07-13-at-6.08.46-PM.png align="left")

*Sortie de la commande docker build*

Dans l'image ci-dessus, vous pouvez voir que chaque instruction dans le Dockerfile est exécutée dans une nouvelle couche par-dessus les précédentes. À la fin, l'image est représentée par un seul hachage sha256 qui est l'identifiant de l'image.

Maintenant, exécutez `docker images` pour voir une liste des images dans votre système. Vous verrez les détails de l'image que vous venez de créer.

C'est tout ce qu'il faut pour construire une image Docker : quelques instructions dans un Dockerfile et une commande.

## Comment Pousser l'Image vers Docker Hub

Maintenant, l'image que vous avez créée réside dans votre système local. Mais que faire si vous souhaitez la rendre accessible à vos membres d'équipe ? Similaire à Git, vous devrez pousser l'image vers un dépôt distant.

Docker Hub est un dépôt (ou registre) où vous pouvez pousser votre image ainsi qu'accéder à d'autres images open source. Similaire à Node, il existe d'autres images de base telles que Ubuntu, Python, Redis, et ainsi de suite. Découvrez-les [ici](https://hub.docker.com/search).

Pour commencer à utiliser [Docker Hub](https://hub.docker.com/signup), vous devez d'abord créer un compte.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-2023-07-13-at-9.26.02-PM.png align="left")

*Inscription sur Docker Hub*

Ensuite, allez dans les dépôts et cliquez sur Créer un dépôt.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-2023-07-13-at-9.25.24-PM.png align="left")

*Dépôts*

Spécifiez un nom de dépôt et marquez-le public ou privé. Dans l'édition communautaire, vous n'êtes autorisé à avoir qu'un seul dépôt privé. Cliquez sur Créer.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-2023-07-13-at-9.37.41-PM.png align="left")

*Créer un Dépôt*

Maintenant, voici à quoi ressemble votre dépôt. Vous pouvez pousser votre image dans ce dépôt. Puisque c'est un dépôt public, n'importe qui peut tirer vos images. Mais seul vous avez la permission de pousser.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-2023-07-13-at-9.39.30-PM.png align="left")

Maintenant que vous avez créé votre dépôt distant, il est temps de pousser votre image. Tout d'abord, vous devez vous connecter en utilisant vos identifiants.

```python
docker login
```

Après cela, tagguez l'image avec votre nom d'utilisateur.

```python
docker image tag react-example-image <username>/react-example-image
```

Maintenant, exécutez cette commande pour pousser l'image.

```python
docker push kunalmac25/react-example-image
```

Puisque vous n'avez pas spécifié de tag d'image (c'est-à-dire une version), il utilisera celui par défaut – le dernier. Contrairement au tag de version, il est nécessaire de tagguer le nom de l'image avec votre nom d'utilisateur. Cela vous donne la pleine propriété de l'image et évite tout conflit de nommage potentiel.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-2023-07-13-at-9.49.48-PM.png align="left")

*Image poussée vers le dépôt*

La dernière version de votre image a été poussée dans le dépôt. Supposons que, dans le futur, vous avez apporté des modifications à votre application. Vous pouvez créer une version mise à niveau de la même image, la tagguer avec le nouveau nom de version et ensuite la pousser.

```python
docker image build -t react-example-image:upgrade .
```

```python
docker image tag react-example-image:upgrade <username>/react-example-image:upgrade
```

```python
docker push kunalmac25/react-example-image:upgrade
```

Maintenant, ouvrez votre dépôt et vérifiez les images.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-2023-07-13-at-10.58.50-PM.png align="left")

*Liste des Images*

Vous pouvez voir une liste de toutes les versions de vos images.

## Comment Créer un Conteneur à partir de l'Image

À ce stade, nous avons un package regroupé incluant tout ce qui est nécessaire pour exécuter l'application React. Maintenant, nous devons créer un conteneur pour exécuter votre application. Exécutez la commande suivante.

```python
docker run -dp 8000:3000 --name react-example-container react-docker-example:latest
```

* `-d` exécute le conteneur en mode détaché – c'est-à-dire qu'il s'exécutera en arrière-plan et n'affichera pas le processus en cours d'exécution sur votre terminal.

* `-p` mappe le port sous la forme `<host_port>:<container_port>`. Le port hôte représente le port sur la machine hôte qui est mappé au port à l'intérieur du conteneur. Puisqu'une application React est exposée via le port 3000, nous allons le mapper au port 8000 sur votre machine hôte.

* Le flag `--name` spécifie le nom pour le conteneur.

* Après cela, vous spécifiez le nom et le tag de l'image.

Si l'image n'existe pas sur votre système local, il essaiera de trouver l'image dans le registre Docker.

Pour vérifier cela, supprimez votre image locale en utilisant `docker image rm react-example-image` et exécutez la commande ci-dessus. Puisqu'il existe une image avec le même nom sur Docker Hub (celle que vous venez de pousser), il téléchargera l'image et créera un conteneur à partir de celle-ci.

Maintenant, exécutez `docker ps` ou `docker container ps` pour afficher une liste de tous les conteneurs en cours d'exécution.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-2023-07-14-at-9.14.41-PM.png align="left")

*Conteneurs en cours d'exécution*

Maintenant, ouvrez votre navigateur et allez sur `http://localhost:8000`. Vous pourrez accéder à votre application.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-2023-07-15-at-8.27.46-PM.png align="left")

*Application en cours d'exécution dans un Conteneur*

Pour arrêter un conteneur en cours d'exécution, utilisez la commande `docker stop` avec l'identifiant ou le nom du conteneur.

```python
docker stop <container_id>
```

Maintenant, si vous exécutez `docker ps`, il n'affichera pas le conteneur car il n'affiche que ceux en cours d'exécution. Si vous souhaitez voir tous les conteneurs, y compris ceux qui ne sont pas en cours d'exécution, utilisez `docker ps -a`.

De plus, naviguez vers la même URL et vous ne pourrez rien voir puisque le conteneur n'est pas en cours d'exécution. Pour redémarrer le conteneur, exécutez `docker start <container_id>`.

Pour supprimer le conteneur, utilisez la commande `docker rm` suivie de l'identifiant ou du nom du conteneur.

```python
docker rm <container_id>
```

Félicitations ! Vous venez d'exécuter l'application dans un environnement isolé où aucun autre processus ne va interférer avec elle. Cela rend votre application plus rapide et plus fiable. Les conteneurs sont extrêmement légers, donc vous pouvez facilement mettre à l'échelle l'application.

De plus, vous n'avez pas à vous soucier des dépendances manquantes ou des versions conflictuelles. Toutes les dépendances dont votre application a besoin sont regroupées à l'intérieur du conteneur. C'est la beauté des conteneurs !

## Prochaines Étapes

![Image](https://images.unsplash.com/photo-1505909487039-08022c92a8ab?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wxMTc3M3wwfDF8c2VhcmNofDEzfHxuZXh0JTIwc3RlcHN8ZW58MHx8fHwxNjg5NTgxMTUyfDA&ixlib=rb-4.0.3&q=80&w=2000 align="left")

*Photo par [Unsplash](https://unsplash.com/@createandbloom?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit)*

À ce stade, vous avez une application empaquetée s'exécutant dans son propre environnement isolé. Mais nous ne sommes qu'à moitié du chemin. Le conteneur s'exécute toujours sur votre machine locale. Une fois que votre application est testée et prête à être déployée, vous devrez envoyer ce conteneur.

Il existe plusieurs plateformes d'orchestration comme Kubernetes et Docker Swarm et des fournisseurs cloud comme Google, AWS, Azure, et autres qui le rendent possible. Ceux-ci sont très utiles lorsque vous souhaitez déployer votre application dans différents environnements (développement, test ou production). Nous discuterons de l'orchestration de conteneurs dans un futur article. C'est tout pour aujourd'hui.

## Conclusion

Dans cet article, j'ai expliqué ce qu'est Docker et pourquoi vous devriez l'utiliser. Ensuite, je vous ai montré comment construire une image en écrivant un Dockerfile, qui n'est qu'un ensemble d'instructions pour construire une image Docker. Après avoir construit une image dans votre système local, vous pouvez pousser cette image vers un registre distant, Docker Hub.

Une fois que votre application est entièrement empaquetée, il est temps d'exécuter l'application dans un conteneur, un environnement isolé avec tout ce dont votre application a besoin. Vous pouvez démarrer, arrêter et supprimer les conteneurs en utilisant des commandes Docker. Après cela, je vous ai donné un aperçu de ce que vous pourriez faire ensuite.

Les conteneurs offrent une solution très légère et plus rapide pour tous vos déploiements et Docker les rend très faciles et pratiques. Les conteneurs ont un avenir très prometteur avec de plus en plus d'entreprises adoptant la conteneurisation.

J'ai expliqué toutes les étapes en termes simples et avec un exemple direct. J'espère que vous avez pu bien comprendre le processus.

Si vous ne comprenez pas le contenu ou trouvez l'explication insatisfaisante, faites-le moi savoir. Les nouvelles idées sont toujours appréciées ! N'hésitez pas à me contacter sur Twitter. En attendant, au revoir !