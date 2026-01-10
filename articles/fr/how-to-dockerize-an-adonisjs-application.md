---
title: Comment Dockeriser une Application AdonisJS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-01-31T00:00:41.000Z'
originalURL: https://freecodecamp.org/news/how-to-dockerize-an-adonisjs-application
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/pexels-pixabay-163726--1-.jpg
tags:
- name: containers
  slug: containers
- name: Docker
  slug: docker
seo_title: Comment Dockeriser une Application AdonisJS
seo_desc: 'By Solomon Eseme

  Creating software is hard. So you want to build it once and run it everywhere without
  adjusting configurations for different operating systems and machines every time.

  Well, this is one problem that dockerizing your application can h...'
---

Par Solomon Eseme

Créer des logiciels est difficile. Vous voulez donc le construire une fois et l'exécuter partout sans ajuster les configurations pour différents systèmes d'exploitation et machines à chaque fois.

Eh bien, c'est un problème que la dockerisation de votre application peut aider à résoudre.

Voici ce que nous allons couvrir dans ce tutoriel :

* Qu'est-ce que Docker ?
    * Avantages de la Dockerisation d'une Application AdonisJS
* Prérequis
* Comment Créer une Application AdonisJS
    * Comment Installer AdonisJS
    * Comment Configurer la Base de Données
    * Comment Configurer les Variables d'Environnement
    * Créer l'Application AdonisJS
* Comment Configurer Docker
    * Comment Installer Docker
    * Comment Créer le Dockerfile
    * Comment Construire l'Image Docker
    * Comment Exécuter le Conteneur Docker
* Conclusion

## Qu'est-ce que Docker ?

Docker est une plateforme pour les développeurs et les administrateurs système qui vous aide à construire, livrer et exécuter des applications distribuées. C'est un outil conçu pour faciliter la création, le déploiement et l'exécution d'applications en utilisant des conteneurs.

Les conteneurs permettent aux développeurs d'empaqueter une application avec toutes les parties dont elle a besoin, telles que les bibliothèques et autres dépendances, et de tout livrer en un seul package.

En faisant cela, vous pouvez être assuré que l'application s'exécutera sur n'importe quelle autre machine Linux (peu importe les paramètres personnalisés que la machine pourrait avoir et qui diffèrent de la machine utilisée pour écrire et tester le code).

### Avantages de la Dockerisation d'une Application AdonisJS

Voici quelques-uns des avantages de la dockerisation de vos applications AdonisJS :

#### Performance Améliorée

La dockerisation d'une application AdonisJS peut aider à améliorer ses performances globales. Cela est dû au fait que les conteneurs Docker sont légers et efficaces, et ils peuvent être rapidement déployés et mis à l'échelle.

#### Déploiement Facile

La dockerisation d'une application AdonisJS facilite son déploiement et sa gestion. Les conteneurs Docker peuvent être rapidement déployés dans n'importe quel environnement, ce qui facilite la gestion et la maintenance de l'application.

#### Coûts Réduits

La dockerisation d'une application AdonisJS peut aider à réduire les coûts associés à l'hébergement et à la maintenance. Cela est dû au fait que les conteneurs Docker sont légers et nécessitent moins de ressources que les machines virtuelles traditionnelles.

#### Sécurité Améliorée

La dockerisation d'une application AdonisJS peut aider à améliorer sa sécurité. Les conteneurs Docker sont isolés les uns des autres.

Dans la section suivante, nous allons explorer davantage la dockerisation d'une application AdonisJS réelle. Mais avant de continuer, examinons quelques-uns des prérequis.

## Prérequis

Avant de plonger dans la création de l'application AdonisJS et sa dockerisation, vous devez avoir [Node.js, NPM](https://nodejs.org/en/) et [Docker installé](https://www.docker.com/).

Vous devez également avoir une compréhension de base du [framework AdonisJS](https://masteringbackend.com/posts/adonisjs-tutorial-the-ultimate-guide) et une compréhension de base de [Docker](https://masteringbackend.com/posts/docker-tutorial) et de ses composants.

## Comment Créer l'Application AdonisJS

Pour créer l'API AdonisJS, vous pouvez suivre cet article sur la [création d'une API Restful avec AdonisJs](https://www.freecodecamp.org/news/build-a-restful-api-with-adonisjs/). Mais nous allons tout de même construire une simple application AdonisJS pour démontrer.

### Comment Installer AdonisJS

Assurez-vous d'installer la version requise de Node.js qui installera également la bonne version de NPM. AdonisJS 5 nécessite Node.js version 12 et NPM version 6 et supérieure.

Si vous avez installé et configuré Node.js et NPM correctement sur votre machine locale en suivant les étapes de la documentation, vous pouvez créer un nouveau projet AdonisJS 5 en exécutant cette commande :

```bash
npm init adonis-ts-app@latest adonisjs-test-app
```

La commande demandera la structure du projet. Sélectionnez simplement API Server et continuez avec les autres options par défaut comme montré ci-dessous :

![api_select](https://www.freecodecamp.org/news/content/images/2022/11/api_select.png)
_Installation d'AdonisJS et sélection de la structure du projet_

Enfin, après une installation réussie, ouvrez le dossier avec n'importe quel éditeur de texte et exécutez la commande suivante pour démarrer et inspecter le projet pour les nouveaux changements :

```bash
cd <NOM_DU_PROJET>

node ace serve --watch
```

Après avoir installé et ouvert votre instance AdonisJS dans l'éditeur de code et le navigateur, nous allons maintenant configurer une base de données et la connecter à notre application.

### Comment Configurer la Base de Données

Nous allons commencer par créer et peupler la base de données avec des schémas et structures de base de données appropriés qui représenteront le stockage de données de notre application.

Tout d'abord, nous devons créer une nouvelle base de données MySQL. Vous pouvez utiliser l'un de ces clients de base de données pour créer et gérer votre base de données.

Ensuite, nous allons installer et configurer AdonisJS Lucid. C'est un ORM puissant pour AdonisJS que vous utilisez pour accéder et manipuler les bases de données sans écrire une seule requête SQL.

Installons Lucid en utilisant cette commande :

```bash
npm install @adonisjs/lucid       
```

Pour configurer le package nouvellement installé avec le projet et la nouvelle base de données créée, exécutez cette commande :

```bash
node ace invoke @adonisjs/lucid
```

La commande présentera différentes options de base de données. Sélectionnez MySQL/MariaDB, et enfin, sélectionnez `In the Terminal` pour les instructions.

### Comment Configurer les Variables d'Environnement

Lisez les instructions et mettez à jour votre fichier `.env` en conséquence avec les bonnes informations d'identification de la base de données comme montré ci-dessous :

```bash
DB_CONNECTION=mysql
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER= //UTILISATEUR_DB
MYSQL_PASSWORD= //MOT_DE_PASSE_DB
MYSQL_DB_NAME= //NOM_DB       
```

### Créer l'Application AdonisJS

Ensuite, vous pouvez suivre l'article sur la [création d'une API Restful](https://www.freecodecamp.org/news/build-a-restful-api-with-adonisjs/) pour construire votre première API avec AdonisJS si vous débutez.

Cependant, si vous avez déjà créé votre application AdonisJS, plongeons dans sa dockerisation.

## Comment Configurer Docker

La configuration d'un conteneur Docker est un processus simple qui nécessite quelques étapes.

### Comment Installer Docker

Docker dispose d'une documentation et d'un processus d'installation très clairs en fonction de votre système d'exploitation. Vous pouvez suivre les [guides étape par étape](https://docs.docker.com/get-docker/) listés dans la documentation officielle pour installer Docker.

### Comment Créer un Dockerfile

Après avoir installé Docker dans votre système, vous pouvez dockeriser chacune de vos applications en créant un simple Dockerfile dans l'un de vos projets.

Un Dockerfile est un document texte qui contient toutes les commandes qu'un utilisateur pourrait appeler sur la ligne de commande pour assembler une image. Vous l'utilisez pour créer une image Docker, que vous pouvez ensuite utiliser pour créer des conteneurs Docker.

Un Dockerfile est écrit en utilisant une syntaxe spécifique et contient des instructions sur la façon de construire l'image.

Pour dockeriser l'application AdonisJS, nous devons créer un Dockerfile et inclure toutes les étapes nécessaires pour exécuter l'application sous forme de commandes.

### Comment Utiliser le Modèle Builder

Voici comment dockeriser notre application AdonisJs en utilisant le Builder Pattern. C'est la manière la plus simple et par défaut de dockeriser des applications.

```bash
FROM node:16.17.0-alpine

# Définir le répertoire de travail
WORKDIR /usr/src/app

# Installer les dépendances
COPY package*.json ./
RUN npm ci --production

# Copier le code source de l'application
COPY . .

# Construire l'application
RUN npm run build --production

COPY ./.env ./build

# Exposer le port
EXPOSE 3333

# Démarrer l'application
CMD ["node", "./build/server.js"]
```

Le Dockerfile est auto-explicatif grâce aux commentaires inclus dans le fichier. Approfondir les commandes Docker est hors du cadre de cet article.

Mais nous allons brièvement passer en revue certaines des commandes populaires utilisées ci-dessus :

1. **FROM** : spécifie quelle image est utilisée pour construire cette nouvelle image Docker
2. **RUN** : utilisé pour exécuter une commande lors de la construction de l'image Docker
3. **WORKDIR** : Il crée un nouveau dossier à l'intérieur de l'image Docker
4. **COPY** : utilisé pour copier les codes sources et autres fichiers dans un dossier spécifié à l'intérieur de l'image Docker.
5. **EXPOSE** : utilisé pour exposer le numéro de port de l'image Docker à la machine extérieure (client).
6. **CMD** : utilisé pour définir la commande par défaut à exécuter lorsqu'un conteneur est exécuté. Il est généralement utilisé en conjonction avec la commande ENTRYPOINT pour fournir une application par défaut à exécuter lorsque le conteneur est démarré.

Dans la section suivante, voyons comment dockeriser notre application en utilisant le modèle de construction multi-étapes de Docker.

### Comment Utiliser le Modèle de Construction Multi-Stage

Maintenant, je vais vous montrer comment dockeriser notre application AdonisJs en utilisant la construction [multi-stage](https://docs.docker.com/build/building/multi-stage/) de Docker. C'est la meilleure pratique pour dockeriser des applications.

```bash
################## Première Étape - Création de la base #########################

# Création d'une variable pour contenir notre image de base node
ARG NODE_IMAGE=node:16.13.1-alpine

# Utilisation de la variable pour créer notre image de base
FROM $NODE_IMAGE AS base

# Exécution d'une commande pour installer dumb-init pour gérer les processus
RUN apk --no-cache add dumb-init

# Création de dossiers et changement de propriétaires
RUN mkdir -p /home/node/app && chown node:node /home/node/app

# Définition du répertoire de travail
WORKDIR /home/node/app

# Changement de l'utilisateur actif actuel en "node"
USER node

# Création d'un nouveau dossier "tmp"
RUN mkdir tmp

################## Deuxième Étape - Installation des dépendances ##########

# Dans cette étape, nous allons commencer à installer les dépendances
FROM base AS dependencies

# Nous copions tous les fichiers package.* dans le répertoire de travail
COPY --chown=node:node ./package*.json ./

# Nous exécutons NPM CI pour installer les versions exactes des dépendances
RUN npm ci

# Enfin, nous copions tous les fichiers avec l'utilisateur actif
COPY --chown=node:node . .

################## Troisième Étape - Étape de Construction #####################

# Dans cette étape, nous allons commencer à construire les dépendances
FROM dependencies AS build

# Nous exécutons "node ace build" pour construire l'application pour la production
RUN node ace build --production


################## Étape Finale - Production #########################

# Dans cette étape finale, nous allons commencer à exécuter l'application
FROM base AS production

# Ici, nous incluons toutes les variables d'environnement requises
ENV NODE_ENV=production
ENV PORT=$PORT
ENV HOST=0.0.0.0

# Copier package.* dans le répertoire de travail avec l'utilisateur actif
COPY --chown=node:node ./package*.json ./

# Nous exécutons NPM CI pour installer les versions exactes des dépendances
RUN npm ci --production

# Copier les fichiers dans le répertoire de travail à partir du dossier de construction de l'utilisateur
COPY --chown=node:node --from=build /home/node/app/build .

# Exposer le port
EXPOSE $PORT

# Exécuter la commande pour démarrer le serveur en utilisant "dumb-init"
CMD [ "dumb-init", "node", "server.js" ]
```

Nous avons rendu le Dockerfile auto-explicatif en ajoutant des commentaires expliquant ce que fait chaque commande.

Dans la section suivante, nous allons explorer comment construire et exécuter le Dockerfile que nous venons de créer.

### Comment Construire l'Image Docker

Une fois que vous avez créé un Dockerfile, vous pouvez construire l'image en utilisant la commande `docker build` où `my-adonisjs-image` est le nom défini par l'utilisateur de l'image.

```bash
docker build -t my-adonisjs-image .
```

Il existe différentes options que vous pouvez passer à la commande `build` en fonction de votre cas d'utilisation. Vous pouvez [explorer la liste des options ici](https://docs.docker.com/engine/reference/commandline/build/).

![Image](https://www.freecodecamp.org/news/content/images/2023/01/docker-build.png)
_Une capture d'écran d'une commande de construction Docker réussie_

### Comment Exécuter l'Image Docker

Exécuter votre application AdonisJS dockerisée est l'étape suivante si vous avez construit votre image avec succès sans erreurs. Il existe plusieurs façons d'exécuter votre image en utilisant la commande Docker Run.

Ci-dessous, nous allons explorer quelques façons d'exécuter votre image Docker : Exécuter l'Image Docker :

```bash
docker run my-adonisjs-image
```

Vous pouvez exécuter l'Image Docker avec des paramètres spécifiques. Par exemple, pour exécuter l'Image Docker avec des paramètres tels que le port avec `-p`, le nom avec `--name`, le mode interactif avec `-it`, utilisez la commande suivante :

```bash
docker run --name adonis-app -it -p 3333:3333 my-adonisjs-image
```

Il existe différentes options que vous pouvez passer à la commande `run` en fonction de votre cas d'utilisation. Vous pouvez [explorer la liste des options ici](https://docs.docker.com/engine/reference/commandline/run/).

![Image](https://www.freecodecamp.org/news/content/images/2023/01/docker-run.png)
_Une capture d'écran d'une commande d'exécution Docker réussie_

### Comment Prévisualiser Votre Application

Vous pouvez prévisualiser votre application AdonisJS dockerisée en visitant http://localhost:3333, où 3333 est le numéro de port que nous avons exposé, comme montré ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Preivew.png)
_Un aperçu de l'application AdonisJS dockerisée_

## Conclusion

Dockeriser une application AdonisJS est un excellent moyen de simplifier le processus de développement et de s'assurer que l'application s'exécute sans problème en production.

En utilisant Docker, les développeurs peuvent facilement empaqueter leur application dans un conteneur et la déployer dans n'importe quel environnement avec un effort minimal.

Docker fournit également un moyen sûr et fiable de gérer les dépendances et les variables d'environnement de l'application. Avec l'aide de Docker, vous pouvez facilement créer, déployer et maintenir vos applications AdonisJS.