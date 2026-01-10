---
title: Comment activer le rechargement en direct sur les applications basées sur Docker
  avec les volumes Docker
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-25T17:16:31.000Z'
originalURL: https://freecodecamp.org/news/how-to-enable-live-reload-on-docker-based-applications
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a0f740569d1a4ca233c.jpg
tags:
- name: Docker
  slug: docker
- name: Docker compose
  slug: docker-compose
- name: Docker Containers
  slug: docker-containers
- name: node
  slug: node
seo_title: Comment activer le rechargement en direct sur les applications basées sur
  Docker avec les volumes Docker
seo_desc: 'By Erick Wendel

  In this post you''ll learn how to configure a development environment with live-reload
  enabled. This will allow you to convert a legacy application so it uses Docker,
  Docker volumes, and docker-compose.

  Some developers turn up their no...'
---

Par Erick Wendel

Dans cet article, vous apprendrez à configurer un environnement de développement avec le rechargement en direct activé. Cela vous permettra de convertir une application héritée pour qu'elle utilise Docker, les volumes Docker et docker-compose.

Certains développeurs lèvent les yeux au ciel lorsqu'on parle d'utiliser Docker pour leur environnement de développement. Ils disent que Docker n'est pas bon pour le développement car il doit toujours reconstruire l'intégralité de l'image pour refléter toutes les nouvelles modifications. Cela le rend improductif et lent. 

Dans cet article, notre objectif est de lutter contre cette mentalité en démontrant comment des configurations simples peuvent entraîner de nombreux avantages tels qu'un environnement fiable sur les environnements de production et de développement.

À la fin de cet article, vous aurez appris à :

* Convertir une application héritée pour qu'elle s'exécute dans un conteneur Docker ;
* Activer la mise en cache des dépendances sur les modules Node.js ;
* Activer le rechargement en direct en utilisant les volumes Docker ;
* Agrégat tous les services dans docker-compose.

## **Conditions préalables**

Dans les prochaines étapes, vous allez cloner un projet existant pour exécuter tous les exemples de cet article. Avant de commencer à coder, assurez-vous d'avoir les outils suivants installés sur votre machine :

* [Docker](https://docs.docker.com/desktop/) et [Docker compose](https://docs.docker.com/compose/)
* [Node.js 1](https://nodejs.org/en/download/current/)0+
* [Git](https://code.visualstudio.com/download)

## **Pourquoi utiliser Docker ?**

De plus en plus de technologies de pointe sont publiées pour l'internet en permanence. Elles sont stables et amusantes à développer et à publier, mais elles ne sont pas prévisibles lorsqu'elles fonctionnent sur différents environnements. Les développeurs ont donc créé Docker pour aider à réduire les risques d'erreurs possibles.

Docker est l'un de mes outils préférés avec lesquels je travaille tous les jours sur des applications de bureau, web et IoT. Il m'a donné le pouvoir non seulement de déplacer des applications à travers différents environnements, mais aussi de garder mon environnement local aussi propre que possible. 

Les développeurs travaillant avec des technologies de pointe travaillent toujours avec quelque chose de nouveau. Mais qu'en est-il des applications héritées ? Devrions-nous tout réécrire avec de nouvelles technologies ? Je sais que ce n'est pas aussi simple qu'il y paraît. Nous devrions travailler sur de nouvelles choses, mais aussi apporter des améliorations aux applications existantes. 

Supposons que vous avez décidé de passer des serveurs Windows aux serveurs Unix. Comment feriez-vous ? Connaissez-vous toutes les dépendances dont votre application a besoin pour fonctionner ?

## À quoi devrait ressembler un environnement de développement ?

Les développeurs ont toujours essayé d'être plus productifs en ajoutant des plugins, des modèles de code et des bases de code sur leurs éditeurs/IDE/terminaux. Le meilleur environnement, à mon avis, devrait être :

1. Facile à exécuter et à tester ;
2. Agnostique de l'environnement ;
3. Rapide pour évaluer les modifications ;
4. Facile à répliquer sur n'importe quelle machine.

En suivant ces principes, nous allons configurer une application dans les prochaines sections de cet article. De plus, si vous n'avez jamais entendu parler du rechargement en direct (ou hot reload), il s'agit d'une fonctionnalité qui surveille les changements dans votre code et redémarre le serveur si nécessaire. Ainsi, vous n'avez pas besoin de revenir en arrière, de redémarrer votre application ou même de reconstruire le système.

## Commencer

Tout d'abord, vous aurez besoin d'un dossier vide appelé `post-docker-livereload` que vous utiliserez comme espace de travail. Allez sur le [dépôt Github](https://github.com/ErickWendel/nodejs-with-mongodb-api-example) et clonez-le dans votre dossier post-docker-live-reload.

Ensuite, analysons ce dont l'application a besoin. Si vous regardez le fichier README.md, il y a quelques instructions démontrant comment exécuter cette application comme montré dans l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screen-Shot-2020-06-24-at-18.10.43-1.png)

Il nécessite Node.js version 10 ou supérieure et MongoDB. Au lieu d'installer MongoDB sur votre machine locale, vous l'installerez en utilisant Docker. Vous l'exposerez également sur localhost:27017 afin que les applications qui ne s'exécutent pas via Docker puissent y accéder sans connaître l'adresse IP interne de Docker. 

Copiez la commande ci-dessous et collez-la dans votre terminal :

```bash
docker run --name mongodb -p 27017:27017 -d mongo:4
```

En utilisant la commande ci-dessus, elle téléchargera et exécutera l'instance MongoDB. Remarquez que si vous avez déjà une instance avec ce nom, elle générera une erreur concernant le nom invalide. 

Si vous voyez l'erreur, exécutez `docker rm mongodb` et elle supprimera toute instance précédente afin que vous puissiez exécuter à nouveau la commande docker run.

## Explorer l'application

Le fichier README.md indique que vous avez besoin d'une instance MongoDB en cours d'exécution avant de démarrer votre application, ainsi que Node.js. 

Si vous avez Node.js installé, allez dans le dossier `nodejs-with-mongodb-api-example` et exécutez les commandes suivantes :

```bash
npm i 
npm run build 
npm start
```

Après avoir exécuté ces commandes, vous pouvez aller dans un navigateur sur [http://localhost:3000](http://localhost:3000) et voir l'application en cours d'exécution comme montré dans l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/01-start.gif)

Gardez à l'esprit que l'application a déjà une commande pour activer le rechargement en direct qui est `npm run dev:watch`. Le pipeline devrait refléter les étapes suivantes :

1. Le développeur modifie les fichiers Typescript ;
2. Typescript transpile les fichiers en Javascript ;
3. Le serveur remarque les changements dans le Javascript et redémarre le serveur Node.js.

Ainsi, la mise en miroir des fichiers vers les conteneurs Docker reflétera toutes les modifications dans le conteneur. Le `npm run build:watch` de l'application attrapera les changements et générera des fichiers de sortie dans le dossier lib afin que le `npm run dev:run` redémarrera le serveur chaque fois qu'il aura été déclenché.

## Dockeriser les applications

Si Docker est un monde complètement nouveau pour vous, n'ayez pas peur ! Vous allez le configurer à partir de zéro. Vous devrez créer quelques fichiers pour commencer :

1. `Dockerfile` - un fichier de recette qui liste comment installer et exécuter votre application ;
2. `.dockerignore` - un fichier qui liste les fichiers qui n'iront pas dans l'instance du conteneur Docker.

### Créer le Dockerfile

Le Dockerfile est le concept clé ici. Vous y spécifiez les étapes et les dépendances pour préparer et exécuter l'application. Tant que vous avez lu le fichier README.md, il sera facile de mettre en œuvre le fichier de recette. 

Je vais mettre le fichier complet ci-dessous et l'analyser plus tard. Dans votre dossier `nodejs-with-mongodb-api-example`, créez un fichier `Dockerfile` et collez le code ci-dessous :

```dockerfile
FROM node:14-alpine

WORKDIR /src

ADD package.json /src 

RUN npm i --silent

ADD . /src 

RUN npm run build 

CMD npm start
```

Que se passe-t-il là ?

* À la ligne 1 - Il utilise comme image de base Node.js 14 - version alpine ;
* Des lignes 2 à 4 - Il copie et installe les dépendances Node.js de l'hôte vers le conteneur. Notez que l'ordre est important. Ajouter package.json au dossier src avant de restaurer les dépendances le mettra en cache et empêchera l'installation des packages à chaque fois que vous devez construire votre image ;
* Des lignes 6 à 7 - Il exécute les commandes pour le processus de compilation puis pour démarrer le programme comme mentionné dans le fichier README.md.

### Ignorer les fichiers inutiles avec .dockerignore

De plus, je travaille sur un système basé sur OSX et le conteneur Docker s'exécutera sur un système basé sur Linux Alpine. Lorsque vous exécutez `npm install`, il restaurera les dépendances pour des environnements spécifiques. 

Vous allez maintenant créer un fichier pour ignorer le code généré à partir de votre machine locale tel que node_modules et lib. Ainsi, lorsque vous copierez tous les fichiers du répertoire courant vers le conteneur, il n'obtiendra pas de versions de packages invalides. 

Dans le dossier `nodejs-with-mongodb-api-example`, créez un fichier `.dockerignore` et collez le code ci-dessous :

```txt
node_modules/
lib/
```

### Construire l'image Docker

Je préfère exécuter cette application à partir du dossier racine. Retournez dans le dossier `post-docker-live-reload` et exécutez les commandes suivantes pour préparer une image pour une utilisation ultérieure :

```shell
docker build -t app nodejs-with-mongodb-api-example
```

Remarquez que la commande ci-dessus utilise le drapeau `-t` pour vous indiquer le nom de l'image et, juste après, le dossier qui contient le fichier `Dockerfile`.

### Travailler avec les volumes

Avant d'exécuter l'application, faisons quelques astuces pour améliorer notre expérience dans les conteneurs Docker.

Les volumes Docker sont une fonctionnalité pour mettre en miroir les fichiers entre votre machine locale et l'environnement Docker. Vous pouvez également partager des volumes entre les conteneurs et les réutiliser pour mettre en cache les dépendances.

Votre objectif est de surveiller les changements sur les fichiers `.ts` locaux et de mettre en miroir ces changements dans le conteneur. Même si les fichiers et le dossier `node_modules` sont dans le même chemin. 

Vous vous souvenez quand j'ai dit que les dépendances dans chaque système d'exploitation seraient différentes ? Pour vous assurer que notre environnement local n'affectera pas l'environnement Docker lors de la mise en miroir des fichiers, nous isolerons le dossier `node_modules` du conteneur sur un volume distinct. 

Par conséquent, lors de la création du dossier `node_modules` sur le conteneur, il ne créera pas le dossier sur l'environnement de la machine locale. Exécutez la commande ci-dessous dans votre terminal pour le créer :

```
docker volume create --name nodemodules

```

### Exécuter et activer le rechargement en direct

Comme vous le savez, le `npm run dev:watch` spécifié dans le README.md montre comment activer le rechargement en direct. Le problème est que vous codez sur une machine locale et cela doit se refléter directement dans votre conteneur. 

En exécutant les commandes suivantes, vous lierez votre environnement local avec le conteneur Docker afin que tout changement dans `nodejs-with-mongodb-api-example` affectera le dossier `src` du conteneur.

```shell
docker run \
    --name app \
    --link mongodb \
    -e MONGO_URL=mongodb \
    -e PORT=4000 \
    -p 4000:4000 \
    -v `pwd`/nodejs-with-mongodb-api-example:/src \
    -v nodemodules:/src/node_modules \
    app npm run dev:watch
```

Analysons ce qui se passe là :

* `--link` donne la permission à l'application d'accéder à l'instance MongoDB ;
* `-e` - sont les variables d'environnement. Comme mentionné dans le fichier README.md, vous pouvez spécifier la chaîne de connexion MongoDB à laquelle vous souhaitez vous connecter en remplaçant la variable `MONGO_URL`. Remplacez la variable `PORT` si vous souhaitez l'exécuter sur un port différent. Notez que la valeur `mongodb` est le même nom que nous avons utilisé pour créer notre instance MongoDB dans les sections précédentes. Cette valeur est également un alias pour l'IP interne de l'instance MongoDB ;
*  `-v` - mappe le répertoire courant vers le conteneur Docker en utilisant un volume virtuel. En utilisant la commande `pwd`, vous pouvez obtenir le chemin absolu de votre répertoire de travail actuel, puis le dossier que vous souhaitez mettre en miroir dans le conteneur Docker. Il y a le `:/src`. Le chemin `src` est l'instruction `WORKDIR` définie dans le `Dockerfile`, donc nous mettons en miroir le dossier local vers le `src` du conteneur Docker ;
* `-v` - le deuxième volume mettra en miroir le volume individuel que nous avons créé dans le dossier `node_modules` du conteneur ;
* `app` - le nom de l'image ;
*  `npm run dev:watch` - cette dernière commande remplacera l'instruction `CMD` du `Dockerfile`.

Après avoir exécuté la commande ci-dessous, vous pouvez déclencher le navigateur après avoir modifié le fichier local `index.ts` pour voir les résultats. La vidéo ci-dessous démontre ces étapes en pratique :

%[https://youtu.be/O9vEQhU_JEM]

## Conclusion

Vous savez que travailler avec des commandes shell fonctionne. Mais ce n'est pas courant de les utiliser ici, et ce n'est pas productif pour exécuter toutes ces commandes, construire des images et gérer des instances à la main. Alors, composez-le !

Docker compose est un moyen de simplifier l'agrégation et la liaison des services. Vous pouvez spécifier les bases de données, les logs, l'application, les volumes, les réseaux, etc.

Tout d'abord, vous devez supprimer toutes les instances actives pour éviter les conflits sur les ports exposés. Exécutez les commandes suivantes dans votre terminal pour supprimer les volumes, les services et les conteneurs :

```bash
docker rm app 
docker volume rm nodemodules
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)
```

### Le fichier docker-compose

Créez un fichier `docker-compose.yml` dans votre dossier `post-docker-livereload` en utilisant les données ci-dessous :

```yaml
version: '3'
services:
    mongodb:
        image: mongo:4
        ports:
            - 27017:27017
    app:
        build: nodejs-with-mongodb-api-example
        command: npm run dev:watch
        ports:
            - 4000:4000
        environment: 
            MONGO_URL: mongodb
            PORT: 4000
        volumes:
            - ./nodejs-with-mongodb-api-example:/src/
            - nodemodules:/src/node_modules
        links:
            - mongodb
        depends_on: 
            - mongodb

volumes:
    nodemodules: {}
```

Le fichier ci-dessus spécifie les ressources par sections. Remarquez que vous avez les sections `links` et `depends_on`. Le champ links est le même drapeau que vous avez utilisé dans votre commande shell. Le `depends_on` s'assurera que MongoDB est une dépendance pour exécuter votre application. Il exécutera MongoDB avant votre application comme par magie ! 

Retournez dans votre terminal, pour démarrer tous les services et construire l'image Docker et créer des volumes et lier les services, exécutez la commande suivante :

```shell
docker-compose up --build
```

Si vous devez supprimer tous les services créés précédemment par ce `Dockerfile`, vous pouvez également exécuter `docker-compose down`.

## Docker est votre ami !

C'est vrai, mon ami. Docker peut vous aider à prévenir de nombreuses erreurs possibles avant qu'elles ne se produisent. Vous pouvez l'utiliser pour les applications frontales et dorsales. Même pour l'IoT lorsque vous devez contrôler le matériel, vous pouvez spécifier des politiques pour l'utiliser.

Pour vos prochaines étapes, je vous recommande vivement de jeter un coup d'œil aux orchestrateurs de conteneurs tels que Kubernetes et Docker swarm. Ils pourraient améliorer encore plus vos applications existantes et vous aider à passer au niveau supérieur.

## **Merci d'avoir lu**

J'apprécie vraiment le temps que nous avons passé ensemble. J'espère que ce contenu sera plus que du simple texte. J'espère qu'il vous aidera à devenir un meilleur penseur et aussi un meilleur programmeur. Suivez-moi sur [Twitter](https://twitter.com/erickwendel_) et consultez mon [blog personnel](https://erickwendel.com/) où je partage tout mon contenu précieux.

À bientôt ! ?