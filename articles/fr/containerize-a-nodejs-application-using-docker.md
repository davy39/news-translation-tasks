---
title: Comment conteneuriser une application Node.js avec Docker – Un guide pour débutants
subtitle: ''
author: Oluwatobi
co_authors: []
series: null
date: '2025-01-24T14:45:09.830Z'
originalURL: https://freecodecamp.org/news/containerize-a-nodejs-application-using-docker
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1737681497302/0540f730-f1c3-496c-bd47-912fdc95d468.png
tags:
- name: Docker
  slug: docker
- name: Node.js
  slug: nodejs
- name: Dockerfile
  slug: dockerfile
- name: containers
  slug: containers
seo_title: Comment conteneuriser une application Node.js avec Docker – Un guide pour
  débutants
seo_desc: Over the years, applications and tools have become more complex to keep
  up with people’s changing requirements and expectations. But this can create issues
  of code compatibility and remote access. For example, a codebase that functions
  properly on Wi...
---

Au fil des années, les applications et les outils sont devenus plus complexes pour répondre aux exigences et aux attentes changeantes des utilisateurs. Mais cela peut créer des problèmes de compatibilité du code et d'accès à distance. Par exemple, une base de code qui fonctionne correctement sur Windows peut développer des erreurs de compatibilité lorsqu'elle est installée sur Linux.

Heureusement, Docker vient à la rescousse. Mais vous vous demandez peut-être – qu'est-ce que Docker, et comment cela aide-t-il ? Vous apprendrez tout cela et plus encore dans ce tutoriel.

Mais avant de commencer, voici quelques prérequis :

* Connaissance des commandes Linux
  
* Connaissance de l'utilisation du terminal
  
* Connaissance de Node.js et Express.js
  

## Table des matières

1. [Qu'est-ce que Docker ?](#heading-quest-ce-que-docker)
  
2. [Comment installer Docker](#heading-comment-installer-docker)
  
3. [Projet de démonstration : Comment conteneuriser une application Node.js](#heading-projet-de-demonstration-comment-conteneuriser-une-application-nodejs)
  
4. [Conclusion](#heading-conclusion)
  

## Qu'est-ce que Docker ?

Docker est un outil open-source qui facilite l'exécution de logiciels de manière cohérente, peu importe où vous vous trouvez. Il y parvient en plaçant votre application et tout ce dont elle a besoin (comme les bibliothèques et les paramètres) dans un conteneur (dont je parlerai plus en détail dans un instant).

Imaginez un conteneur comme une boîte : il contient votre application et toutes ses parties, de sorte qu'elle fonctionne exactement de la même manière sur votre ordinateur portable, un serveur ou dans le cloud. Docker aide les développeurs à éviter le problème "ça marche sur ma machine" en s'assurant que tout est emballé ensemble de manière fiable et portable.

Docker a été créé par Solomon Hykes en 2013. Au fil des années, il a évolué pour couvrir une large gamme d'outils. Il est devenu un outil incontournable pour améliorer les processus de déploiement et de mise en réseau des applications.

Avant de continuer, voici quelques termes clés que vous rencontrerez tout au long de ce tutoriel :

### **Moteur Docker**

Le moteur Docker, comme son nom l'indique, est le cœur des applications Docker. Il comporte un composant client et un composant serveur. Le client Docker, dans notre cas, est l'outil d'interface de ligne de commande ou le terminal Docker que nous utiliserons pour envoyer les commandes pertinentes pour l'exécution du projet. Le serveur Docker, populairement connu sous le nom de démon, est le serveur qui gère l'exécution des diverses images et conteneurs Docker.

### **Image Docker**

Les images Docker sont des modèles préconçus de logiciels et de systèmes exécutables. Docker offre une large gamme d'images allant des modèles de systèmes d'exploitation aux modèles de serveurs, aux modèles de logiciels, et ainsi de suite. Vous pouvez trouver toutes ces images sur le registre Docker Hub où ces images sont stockées.

Vous pouvez également créer une image spécifique et l'héberger soit publiquement sur le Docker Hub, soit dans un registre privé.

### **Conteneurs Docker**

Les conteneurs Docker sont des instances exécutables et compactes construites sur le modèle généré qui est l'image Docker. Ce sont des packages légers et portables qui incluent tout ce qui est nécessaire pour exécuter un logiciel – code, runtime, bibliothèques et outils système. Un conteneur garantit que l'application s'exécute de manière cohérente, indépendamment de l'environnement.

### Avantages de l'utilisation de Docker

Voici quelques-uns des avantages de l'utilisation de Docker en tant que développeur backend :

* Docker est un excellent outil pour créer une solide culture DevOps pour le développement d'applications, car il clarifie les fonctions des équipes de développement et d'exploitation.
  
* Il est également assez flexible, permettant un déploiement facile de microservices et d'applications backend monolithiques distribuées.
  
* Il minimise également les erreurs dues aux mauvaises configurations de dépendances lors des installations, car il porte l'application avec ses dépendances nécessaires en une seule fois.
  

Passons maintenant à la conteneurisation d'une application Node.JS Express. Mais avant cela, vous devrez installer Docker sur votre ordinateur. Vous pouvez sauter cette étape si vous l'avez déjà installé.

## Comment installer Docker

Docker est un outil multiplateforme qui peut être installé sur tous les systèmes d'exploitation populaires (Windows, Mac OS et distributions Linux). Pour ce tutoriel, je ne mettrai en évidence que la configuration de Docker sur Windows.

Si vous utilisez actuellement un système d'exploitation autre que Windows, vous pouvez facilement configurer Docker en suivant les étapes de la documentation Docker [ici](https://docs.docker.com/engine/install/).

Pour les utilisateurs de Windows, il est essentiel que votre PC réponde aux spécifications minimales – sinon l'installation ne sera pas réussie. Les exigences minimales sont les suivantes :

* Une version de Windows OS non inférieure à Windows 10 home
  
* Un PC avec WSL-2 installé ou Hyperviseur activé.
  

Avec cela, passons au téléchargement de l'exécutable d'installation de Docker. Vous pouvez télécharger le dernier installateur Docker depuis [ici](https://www.docker.com/products/docker-desktop/). Après avoir fait cela, exécutez le logiciel et acceptez les termes et conditions. Une fois l'installation terminée avec succès, lancez l'application. Voici ce que vous devriez voir :

![Interface graphique de Docker Desktop](https://cdn.hashnode.com/res/hashnode/image/upload/v1737154696376/dcbf3b23-10cc-452a-b206-46973163e8d6.png align="center")

Pour confirmer que vous avez installé l'application avec succès, accédez à l'invite de commande du terminal et exécutez `Docker --version`. Vous devriez voir la version exacte de l'outil du moteur Docker que vous avez installée si l'installation a réussi.

Nous allons maintenant passer au projet proprement dit.

## Projet de démonstration : Comment conteneuriser une application Node.js

Dans cette section, nous allons conteneuriser un simple service backend basé sur Node.js avec des dépendances minimales. Cela vous montrera comment conteneuriser et porter une application en utilisant une technique de conteneurisation d'application Docker connue sous le nom de **Dockerfile**. Gardez à l'esprit que si vous avez une application plus complexe, il peut être préférable d'utiliser l'outil YAML [**Docker compose**](https://www.freecodecamp.org/news/what-is-docker-compose-how-to-use-it/).

Pour commencer, nous allons configurer l'application Node.js de démonstration. Je fournirai l'ensemble de la configuration du code dans cet article, ci-dessous. Mais d'abord, comprenons ce qu'est un **Dockerfile**.

### Qu'est-ce qu'un Dockerfile ?

En gros, un Dockerfile est un système de modèle qui permet à l'utilisateur d'entrer des commandes qui, une fois exécutées, peuvent produire une image fonctionnelle de l'application. Cette image peut ensuite être convertie en un conteneur.

Voici quelques commandes incluses dans la structure de base d'un Dockerfile :

* `CMD`**:** définit la commande par défaut à exécuter si aucune commande n'est spécifiée lorsque le conteneur démarre. Elle peut être remplacée en fournissant une commande lors de l'exécution du conteneur (`docker run ...`).
  
* `ENTRYPOINT`**:** Spécifie la commande principale qui s'exécute toujours lorsque le conteneur démarre. Elle n'est pas facilement remplacée, mais des arguments peuvent être ajoutés.  
  **Notez** que `CMD` et `ENTRYPOINT` spécifient tous deux quelle commande ou quel processus le conteneur doit exécuter lorsqu'il démarre. Mais ils sont utilisés différemment et ont des objectifs distincts. Utilisez `CMD` pour un comportement par défaut qui peut être remplacé. Utilisez `ENTRYPOINT` pour une commande fixe qui définit le but principal du conteneur.
  
* `FROM`**:** Il s'agit généralement de l'instruction d'ouverture dans un Dockerfile. Cette commande récupère une image de base qui forme la fondation pour la construction de l'image de l'application en question. Par exemple, dans notre application, l'image de base pour une application Node.js est d'avoir le moteur Node.js de base installé.
  
* `WORKDIR`**:** Cette syntaxe définit le répertoire de travail actif où les fichiers de l'application résideront dans le conteneur défini. Un dossier automatique sera créé s'il n'est pas déjà disponible.
  
* `COPY`**:** Cette syntaxe est utilisée pour s'assurer que les fichiers nécessaires à la création de l'image Docker à partir du fichier de projet de la base de code sont copiés dans le nouveau conteneur Docker créé. Les répertoires de ces fichiers sont soigneusement mis en évidence.
  
* `RUN`**:** Cette syntaxe spécifie le script que vous souhaitez exécuter avant de finaliser la conteneurisation de l'application.
  
* `ENV`**:** Cette syntaxe est utilisée pour mettre en évidence les variables d'environnement et les secrets qui seront invoqués lors du processus d'exécution de l'application.
  
* `EXPOSE`**:** Cette syntaxe cartographie le port de navigation où l'application est utilisée pour communiquer avec l'internet externe. Par exemple, `EXPOSE: 3000` cartographie l'interface web de l'application à `localhost:3000`.
  

En approfondissant Docker, passons rapidement en revue quelques commandes Docker clés que nous utiliserons tout au long de ce tutoriel :

* `Docker ps`**:** Cette commande liste tous les conteneurs en cours d'exécution sur votre terminal Docker.
  
* `Docker run`**:** Cette commande exécute une image Docker pour déclencher une instance d'un conteneur.
  
* `Docker build`**:** Cette commande fonctionne en fonction du fichier Docker pour générer une image d'un service ou d'une application.
  
* `Docker rm`**:** cette commande peut être utilisée pour supprimer une image en utilisant les détails d'identification de l'image.
  

### Comment conteneuriser l'application

Maintenant, nous pouvons commencer à conteneuriser notre simple application Node/Express. Pour suivre ce tutoriel, vous pouvez obtenir le code de base depuis [ici](https://github.com/oluwatobi2001/Typescript_test).

En le testant localement, il retourne une API CRUD où vous pouvez créer, récupérer, mettre à jour et supprimer des produits lorsqu'il est exécuté. Nous allons emballer l'application pour un déploiement facile sur le cloud en utilisant notre moteur Docker. Nous pourrons le faire en utilisant l'outil Dockerfile dont nous avons parlé ci-dessus.

#### Étape 1 : Créer le Dockerfile

Dans votre dossier de projet, créez un fichier nommé `Dockerfile`. Assurez-vous que le nom est **exactement** "Dockerfile" (sans extension, et sensible à la casse dans certains systèmes – assurez-vous donc qu'il est en majuscules).

Si vous utilisez un éditeur de code, créez simplement un nouveau fichier nommé `Dockerfile`. Si vous utilisez un éditeur de texte basique, enregistrez le fichier avec le nom `Dockerfile` et assurez-vous qu'il ne s'enregistre pas accidentellement avec une extension comme `.txt`.

Ensuite, entrez la première ligne :

```dockerfile
FROM Node:18-alpine
```

Cette commande récupère l'image de base que nous utiliserons pour alimenter notre application Express, qui est le moteur Node lui-même.

Vous vous demandez peut-être à quoi sert `alpine`. Alpine est une version légère, beaucoup plus compressée d'une image Docker. Elle exclut l'incorporation de packages supplémentaires non directement essentiels au système d'exploitation de base. Il est recommandé comme bonne pratique de code standard d'utiliser des distros légères pour une exécution plus rapide et une utilisation facile.

#### Étape 2 : Définir le répertoire de travail

```dockerfile
WORKDIR /app
```

Cela définit le répertoire de travail de l'image sur le dossier `/app` du conteneur. Il garantit que toutes les actions sur les fichiers se produisent ici et que tous les fichiers sont copiés dans ce répertoire.

#### Étape 3 : Copier les fichiers nécessaires

```dockerfile
COPY package.json
```

Cette commande copie les fichiers `package.json` qui contiennent une liste de dépendances et de packages à installer pour alimenter notre application.

#### Étape 4 : Exécuter un script de configuration

```dockerfile
RUN npm install
```

Cette commande garantit que toutes les dépendances nécessaires pour alimenter nos applications Node.js sont installées sur le conteneur.

#### Étape 5 : Copier les fichiers de code

```dockerfile
COPY . .
```

Cette commande garantit que tous les fichiers du répertoire local sont copiés dans le système de fichiers du conteneur dans le répertoire de travail établi.

#### Étape 6 : Exposer le port du serveur

```dockerfile


EXPOSE 3000 
```

Cette commande expose le port du serveur que nous prévoyons d'utiliser pour accéder au conteneur. Dans ce cas, il s'agit du port 3000.

#### Étape 7 : Inclure la commande pour démarrer le conteneur

```dockerfile
CMD ["npm", "run", "dev"]4
```

Cette commande est exécutée à la fin afin de démarrer l'application Node.js. Elle exécute simplement la commande `npm run dev` qui est ce que vous utiliseriez pour un environnement de développement. Pour l'exécuter dans un environnement de production, vous utiliseriez la commande `npm start` à la place.

Ayant terminé ce processus, voici à quoi devrait ressembler la structure finale du Dockerfile :

```dockerfile
FROM Node:18-alpine
WORKDIR /app

COPY package.json

RUN npm install

COPY . .

CMD ["npm", "run", "dev"]
```

### Tester le conteneur Docker

Pour conclure, nous allons créer une image Docker de notre application Node.js. Pour ce faire, exécutez la commande `docker build -t nodeapp .`. La commande `docker build` construit l'image, tandis que `-t` permet de spécifier les détails de l'étiquette de l'image.

Dans notre cas, nous attribuons le nom `nodeapp` à l'image que nous allons créer et l'image sera créée dans le répertoire de travail.

![Cette image exécute la commande docker build](https://cdn.hashnode.com/res/hashnode/image/upload/v1737154702142/98e05981-bb05-41c6-919f-02b3261f3caa.png align="center")

Félicitations ! Vous avez réussi à créer votre première image Docker. Pour voir toutes les images de votre dépôt local, exécutez la commande `docker images`.

![Une image montrant la commande docker images en cours d'exécution et la liste de toutes les images disponibles localement](https://cdn.hashnode.com/res/hashnode/image/upload/v1737154714828/71f50b4f-8df5-4885-a5fc-6365dd903645.png align="center")

Pour créer une instance de travail de votre image pour les tests, exécutez la commande `docker run nodeapp`.

![Exécution d'une instance en cours de notre image docker](https://cdn.hashnode.com/res/hashnode/image/upload/v1737154708130/bb6968f2-829d-4107-be82-4bdd9c167d53.png align="center")

Nous utilisons MongoDB comme base de données pour ce tutoriel, nous devons donc passer l'URL MongoDB comme variable d'environnement au conteneur Docker. Les variables d'environnement vous aident à protéger certaines variables clés qui ne doivent pas être exposées au public. D'autres variables qui peuvent être passées comme variables d'environnement incluent les clés API et les codes de chiffrement.

Pour passer l'URL MongoDB au conteneur Docker, nous utilisons le tag `-e` pour nous assurer que Docker reconnaît la valeur correspondante entrée comme une variable d'environnement.

`docker run -e JWT_SECRETS={entrez la valeur de votre choix} -e MONGO_URL={L'URL mongo de votre choix} nodeapp`.

Pour utiliser également le conteneur en arrière-plan, il suffit d'attacher le tag `-d` qui représente l'option de détachement. Cette option permet au conteneur de s'exécuter en arrière-plan malgré la sortie du terminal de ligne de commande.

En cas d'absence d'erreurs, la navigation vers `localhost:5000` devrait également produire quelque chose de similaire à l'image ci-dessous.

![Postman testant le localhost:5000](https://cdn.hashnode.com/res/hashnode/image/upload/v1737506281699/54bb1d9b-0be7-42e3-b212-bb4bd27e019d.png align="center")

## Conclusion

Dans cet article, vous avez appris ce qu'est Docker et comment il fonctionne, ainsi que ses commandes courantes et comment l'utiliser pour conteneuriser une application backend. En allant au-delà des bases, vous pouvez également explorer d'autres utilisations de Docker dans l'intégration et le développement continus. Pour en savoir plus sur Docker, vous pouvez consulter sa documentation [ici](https://docs.docker.com/).

Je vous recommande également d'utiliser vos nouvelles connaissances pour déployer des projets avec des cas d'utilisation réels, ainsi que d'explorer la mise en réseau dans les applications Docker. Pour rendre votre application vivante, vous pouvez facilement déployer l'image Docker que vous avez créée sur l'un des fournisseurs de services cloud populaires comme AWS, GCP, Azure, et ainsi de suite.

N'hésitez pas à me poser des questions ! Vous pouvez également consulter mes autres articles [ici](http://portfolio-121.netlify.app). Jusqu'à la prochaine fois, continuez à coder !