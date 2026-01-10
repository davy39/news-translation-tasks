---
title: Comment déployer un service Web Restful sur Microsoft Azure App Service
subtitle: ''
author: Alaran Ayobami
co_authors: []
series: null
date: '2025-03-28T15:34:24.295Z'
originalURL: https://freecodecamp.org/news/deploy-a-restful-web-service-on-microsoft-azure-app-service
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1743176028047/61eba7a3-5505-4152-9df5-59a1cb8c61ac.png
tags:
- name: Azure
  slug: azure
- name: azure-devops
  slug: azure-devops
- name: Cloud Computing
  slug: cloud-computing
- name: Cloud
  slug: cloud
- name: REST API
  slug: rest-api
- name: deployment
  slug: deployment
- name: Azure App Service
  slug: azure-app-service
- name: azure-app-services
  slug: azure-app-services
seo_title: Comment déployer un service Web Restful sur Microsoft Azure App Service
seo_desc: 'Hey there! 👋, How’s it going?

  I hope you''re doing well. Whether you''re a seasoned coder, a curious learner,
  or just someone browsing through, welcome to my little corner of the internet.

  In this tutorial, we’ll dive into how you can deploy a web ser...'
---

Salut à tous ! \ud83d\udc4b, Comment ça va ?

J'espère que vous allez bien. Que vous soyez un codeur expérimenté, un apprenant curieux ou simplement quelqu'un qui navigue, bienvenue dans mon petit coin d'internet.

Dans ce tutoriel, nous allons plonger dans la manière de déployer un service web sur le service d'application Microsoft Azure. C'est un sujet que j'ai hâte d'explorer, et j'espère que vous le trouverez instructif et utile. Alors, prenez un café, installez-vous confortablement et commençons.

### Prérequis

* Compréhension de base des services web RESTful

* Connaissances en programmation

* Bases de Docker

* Compte Docker Hub

* Compétences en interface de ligne de commande (CLI)

### Ce que nous allons couvrir :

* [Terminologies clés](#heading-terminologies-cles)

* [Comment installer Docker et Docker Compose](#heading-comment-installer-docker-et-docker-compose)

* [Comment créer un service Web simple Get Client Info](#heading-comment-creer-un-service-web-simple-get-client-info)

* [Comment construire l'image Docker de l'application](#heading-comment-construire-limage-docker-de-lapplication)

* [Comment exécuter l'application dans le conteneur](#heading-comment-executer-lapplication-dans-le-conteneur)

* [Comment créer un groupe de ressources Azure sur le portail Azure.](#heading-comment-creer-un-groupe-de-ressources-azure-sur-le-portail-azure)

* [Comment déployer sur Azure App Service](#heading-comment-deployer-sur-azure-app-service)

* [Conclusion](#heading-conclusion)

Avant de commencer, j'aimerais passer en revue quelques terminologies clés que j'utiliserai tout au long de ce tutoriel. Comprendre ces termes facilitera le suivi et vous permettra de tirer le meilleur parti de ce que nous discutons. Plongeons-nous !

## Terminologies clés

### **1. Docker**

Docker est une plateforme open-source qui simplifie le développement, le transport et le déploiement d'applications en utilisant des conteneurs. Avec Docker, il y a trois choses clés que vous pouvez faire :

* construire une fois et exécuter n'importe où

* garder l'environnement cohérent, et

* facilement mettre à l'échelle votre application avec des outils d'orchestration de conteneurs comme Kubernetes.

### **2. Docker Hub**

Docker Hub est un dépôt basé sur le cloud où les développeurs peuvent stocker, partager et gérer des images Docker. Vous pouvez le considérer comme le GitHub pour les images Docker \ud83d\ude09.

### **3. Image Docker**

Une image Docker est un package léger, autonome et exécutable qui inclut tout ce qui est nécessaire pour exécuter un logiciel. Vous pouvez également le considérer comme un plan pour créer et exécuter un conteneur.

Une fois construite, une image est immuable, ce qui signifie qu'elle ne peut pas changer après sa création. Au lieu de cela, vous créez une nouvelle version lorsque des mises à jour sont nécessaires. Cela signifie que vous devrez reconstruire si vous mettez à jour le code qui est exécuté dans le conteneur.

### **4. Conteneur**

Un conteneur est une instance en cours d'exécution d'une image Docker. Il fournit un environnement isolé où une application s'exécute avec toutes ses dépendances, sans interférer avec le système hôte ou d'autres conteneurs.

Attendez, quoi ?! **\ud83d\ude15** Eh bien, simplement, un conteneur est comme une petite machine virtuelle qui exécute l'image Docker construite. Mais contrairement aux machines virtuelles traditionnelles, il n'a pas de processus d'initialisation (PID 1), ce qui signifie qu'il s'exécute toujours sur un système hôte plutôt que d'être entièrement indépendant. À présent, vous devriez comprendre l'idée : pas d'image, pas de conteneur. Un conteneur dépend d'une image pour exister. Vous devez cuisiner avant de servir, n'est-ce pas ? \ud83c\udf7d\ufe0f

### **5. Groupe de ressources Azure**

Un groupe de ressources Azure fait référence à un magasin ou un dossier contenant toutes les ressources liées à une application que vous souhaitez déployer en production en utilisant le cloud MS Azure. Par exemple, si je veux déployer une application web eCommerce avec MS Azure, je pourrais créer un groupe de ressources appelé EcommWebAppRG. Je l'utiliserais pour créer toutes les ressources dont j'ai besoin pour que l'application web soit mise en ligne et accessible – comme des machines virtuelles, des bases de données, des caches et d'autres services.

Très bien, maintenant que tous les termes sont clarifiés, commençons le tutoriel pour que vous puissiez apprendre à déployer un service web sur Azure App Service.

Puisque nous déployons une application, commençons par créer une simple application API REST. J'utiliserai Golang pour le développement de l'API, mais vous pouvez utiliser n'importe quel langage de programmation ou framework de votre choix. Si vous souhaitez suivre avec l'application de ce tutoriel, j'ai fourni le code source [ici](https://github.com/Ayobami6/client_info_webservice).

## Comment installer Docker et Docker Compose

Pour installer Docker et Docker Compose sur votre PC, pour Mac et Windows, vous devrez télécharger Docker Desktop pour votre système d'exploitation [ici](https://hub.docker.com/welcome).

Pour Linux, vous pouvez exécuter la commande suivante :

```bash
sudo apt update # mettre à jour le registre apt
sudo apt install docker.io # pour le moteur docker
sudo apt install docker-compose-plugin
```

Après avoir téléchargé Docker Desktop pour votre application, ouvrez votre terminal et entrez la commande suivante pour vérifier que Docker et Docker Compose ont été installés avec succès sur votre machine :

```bash
docker-compose -v # cela devrait afficher la version de l'interface de ligne de commande docker compose que vous avez sur votre PC
```

Ma version de Docker Compose est :

```bash
Docker Compose version v2.31.0-desktop.2
```

```bash
docker -v
```

Vous devriez voir quelque chose de similaire si Docker a été installé avec succès sur votre machine :

```bash
Docker version 27.4.0, build bde2b89
```

## Comment créer un service Web simple Get Client Info

D'accord, j'utiliserai cet outil pratique appelé `sparky_generate` pour générer le modèle de code de l'application. `sparky_generate` est un outil de ligne de commande utilisé pour générer du code de base pour le développement backend en utilisant divers langages et frameworks backend.

Utilisez cette commande pour installer et configurer l'outil sur votre machine Mac ou Linux. Si vous êtes sous Windows, vous pouvez utiliser WSL.

```bash
wget https://raw.githubusercontent.com/Ayobami6/sparky_generate/refs/heads/main/install.sh
```

```bash
chmod 711 install.sh
./install.sh # exécutez la commande d'installation comme suit
```

```bash
sparky # exécutez la commande sparky comme suit
```

Vous devriez voir quelque chose de similaire à ce qui suit. Sélectionnez le framework que vous souhaitez utiliser pour votre service backend.

![Choisir un type de projet dans sparky](https://cdn.hashnode.com/res/hashnode/image/upload/v1741520002226/b696a376-527b-412a-a8c7-967aca35217a.png align="center")

Je vais sélectionner Go, car j'utilise Go pour ce tutoriel. Vous devriez avoir votre modèle de projet prêt une fois que vous avez sélectionné votre framework. Je ne vais pas expliquer comment coder le service web car cela est hors du cadre de ce tutoriel. Le but ici est de déployer sur Azure en utilisant Azure App Service.

## Comment construire l'image Docker de l'application

Pour construire l'image Docker de notre application, nous devons d'abord créer un fichier Docker qui inclura toutes les étapes nécessaires pour construire l'image.

```bash
touch Dockerfile
```

Nous allons utiliser une construction Docker multi-étapes pour réduire la taille de notre image Docker. Nous avons besoin de quelque chose d'aussi léger que possible.

La construction Docker multi-étapes aide à réduire la taille car nous utilisons différentes étapes pour différentes préoccupations. Cela aide à garantir que seule ce qui est nécessaire pour exécuter l'application dans l'étape finale est utilisé. Par exemple, nous pourrions avoir besoin de certains artefacts pour construire l'application, mais nous n'en avons pas besoin pour exécuter l'application. C'est pourquoi nous avons les étapes de construction et d'exécution dans le fichier Docker ci-dessous.

Notre première étape (build) est concernée par la construction et le regroupement de l'application. La deuxième étape (runner) est simplement utilisée pour exécuter l'exécutable que nous avons construit dans la première étape. Donc, en gros, tous les fichiers, modules, etc., utilisés dans le processus de construction seront jetés dans le runner puisqu'ils ont déjà servi leurs objectifs.

```dockerfile
# utiliser la première étape comme build
FROM golang:1.23-alpine AS build # utiliser l'image de base alpine pour réduire la taille

# installer git sur la machine
RUN apk add --no-cache git

# définir le répertoire de travail actuel sur la vm à /app
WORKDIR /app

# Copier tous les fichiers de dépendance go dans le répertoire de travail
COPY go.mod go.sum ./

# Installer les dépendances go
RUN go mod download

# copier tous les fichiers restants dans le répertoire de travail
COPY . .
# construire l'exécutable

# construire le programme go
RUN go build -o api cmd/main.go

# étape 2 AKA le runner
FROM alpine:3.18

RUN  apk add --no-cache ca-certificates

# copier l'exécutable go dans le répertoire de travail
COPY --from=build /app/api .

# exposer le port de service en cours d'exécution
EXPOSE 6080

```

Ce Dockerfile décrit toutes les étapes pour construire une image Docker pour notre application. Passons en revue toutes ces étapes ligne par ligne. Parce que nous utilisons une construction multi-étapes ici, nos étapes sont `build` et `runner`.

* La première étape de construction commence par le premier `FROM golang:1.23-alpine AS build`. Elle initialise une étape avec toutes les étapes de l'étape. Elle indique que l'image de base à utiliser pour toutes les étapes de cette étape doit utiliser une image golang:1.23 préexistante utilisant une distribution Alpine Linux pour exécuter toutes les étapes de l'étape.

* Ensuite, nous avons `RUN`, qui est utilisé pour exécuter la commande `apk add git`, suivi de la définition du répertoire de travail sur le dossier /app.

* Ensuite, nous avons la commande `COPY` qui copie toutes les dépendances Go qui exécuteront le programme Go.

* Ensuite, `RUN go mod download` qui est utilisé pour installer toutes les dépendances.

* Nous avons ensuite la commande `COPY . .` pour copier tous les fichiers dans le répertoire de travail /app de l'image

* Ensuite, la dernière étape de l'étape de construction, `RUN go build -o api cmd/main.go`, construit le code principal de l'application main.go en un exécutable API. La deuxième étape "runner" utilise une image de base `alpine:3.18`, et utilise également la directive `RUN` pour ajouter des certificats ca à l'image de base Alpine. La commande `COPY` est utilisée ici pour copier uniquement le fichier exécutable construit de l'image de construction à l'image d'exécution.

* Nous exposons ensuite le port 6080 afin que notre conteneur construit puisse accepter une connexion HTTP à partir du port 6080.

Maintenant, écrivons notre fichier `docker-compose.yml` pour définir et exécuter notre service conteneurisé :

```yaml
services:

  client_info_app:
    build: 
      context: .
      dockerfile: Dockerfile
    container_name: info_app

    ports:
      - "6080:6080"

    command: "./api"
```

### Comprendre la structure YAML

YAML suit une structure clé-valeur similaire à un dictionnaire ou une table de hachage. Dans notre fichier, la clé de premier niveau est `services`, qui agit comme la clé parente. Dans `services`, nous définissons les configurations de service individuelles.

Dans ce cas, nous avons un seul service nommé `client_info_app`, qui contient les propriétés nécessaires pour que Docker le construise et l'exécute.

* `build` : Cela spécifie comment construire l'image Docker pour le service. Le `context: .` indique à Docker de rechercher le `Dockerfile` dans le même répertoire que le fichier `docker-compose.yml`.

* `container_name` : Cela attribue un nom personnalisé (`info_app`) au conteneur en cours d'exécution, ce qui facilite la référence.

* `ports` : Définit les mappages de ports entre l'hôte et le conteneur. Le `-` avant `"6080:6080"` indique que plusieurs mappages pourraient être listés. Ici, le port `6080` sur l'hôte est mappé au port `6080` à l'intérieur du conteneur.

* `command` : Spécifie la commande à exécuter à l'intérieur du conteneur une fois qu'il démarre. Dans ce cas, il exécute `./api`.

Cette structure nous permet de définir et de configurer plusieurs services dans la clé `services` si nécessaire, mais pour l'instant, nous ne définissons que `client_info_app`.

## Comment exécuter l'application dans le conteneur

Vous pouvez utiliser cette commande pour démarrer le conteneur :

```bash
docker-compose up client_info_app
```

La commande ci-dessus construira d'abord l'image si elle n'existe pas. Ensuite, elle l'exécute, car rappelez-vous : **pas d'image, pas de conteneur.**

Si tout semble bon, vous devriez avoir quelque chose de similaire à ceci, selon le framework de votre application :

![Serveur web Go en cours d'exécution](https://cdn.hashnode.com/res/hashnode/image/upload/v1741708248802/0c0e25a0-fa8c-4eea-adaa-5f4986b5fda6.png align="center")

Vous devriez également vérifier que votre image Docker a été construite. Pour ce faire, exécutez la commande suivante :

```bash
docker images
```

![Vérifier que Docker est construit avec succès](https://cdn.hashnode.com/res/hashnode/image/upload/v1741708480967/dbb033eb-d336-4f22-934b-8d50333b6344.png align="center")

Voilà ! Vous avez maintenant votre image Docker construite et prête pour le déploiement sur Azure App Service.

Passons au portail Azure pour déployer l'application.

**Remarque :** si vous n'avez pas d'abonnement Azure actif, ce n'est pas grave – vous pouvez toujours suivre. Si vous souhaitez obtenir un compte d'essai, vous pouvez [en obtenir un ici](https://azure.microsoft.com/en-us/pricing/purchase-options/azure-account).

## Comment créer un groupe de ressources Azure sur le portail Azure.

Pour rappel, un groupe de ressources Azure fait référence à un magasin ou un dossier contenant toutes les ressources liées à une application que vous souhaitez déployer en production en utilisant le cloud MS Azure. Maintenant, créons-en un.

Lorsque vous vous connectez au portail Azure, vous devriez voir quelque chose comme ceci, le tableau de bord :

![Tableau de bord Azure](https://cdn.hashnode.com/res/hashnode/image/upload/v1741709173044/1ab78dd4-97ac-43da-8599-d7b1d790eb13.png align="center")

Recherchez le groupe de ressources en utilisant la barre de recherche :

![Rechercher un groupe de ressources](https://cdn.hashnode.com/res/hashnode/image/upload/v1741709263175/7946270b-11c6-4fef-9abc-996b1efc6f52.png align="center")

![Panneau de contrôle du groupe de ressources](https://cdn.hashnode.com/res/hashnode/image/upload/v1741709619363/5cfce825-0af6-4d64-ae4e-e929ba03d919.png align="center")

Cliquez sur Créer pour créer un nouveau groupe de ressources :

![Créer un groupe de ressources](https://cdn.hashnode.com/res/hashnode/image/upload/v1741709715096/e519fe55-0ac3-4e9f-8b98-3f34cecfcd43.png align="center")

Donnez un nom à votre groupe de ressources et sélectionnez une région pour celui-ci. Ici, j'utiliserai l'Est des États-Unis 2 par défaut, mais vous pouvez utiliser celle que vous voulez. Ensuite, cliquez sur Vérifier + créer.

![Vérifier la création du groupe de ressources](https://cdn.hashnode.com/res/hashnode/image/upload/v1741770354937/253c33d2-d7b2-44b5-84df-9cb4977aec3b.png align="center")

![Aperçu du groupe de ressources](https://cdn.hashnode.com/res/hashnode/image/upload/v1741770386424/0a97c949-5c31-466b-be7f-a43f0783e125.png align="center")

Vous devriez voir quelque chose de similaire à ce qui précède après avoir créé le groupe de ressources.

## Comment déployer sur Azure App Service

D'accord, maintenant que nous avons créé le groupe de ressources, passons à la création du service Azure App Service. Pour ce faire, revenez au tableau de bord et cliquez sur Créer une ressource.

![Tableau de bord Azure](https://cdn.hashnode.com/res/hashnode/image/upload/v1741772709338/2c353749-7e0a-42b0-894e-25b1f08cad15.png align="center")

![Vue des ressources Azure](https://cdn.hashnode.com/res/hashnode/image/upload/v1741773327784/536358ff-241b-4ea1-876d-575abf12a27b.png align="center")

Vous pouvez rechercher Web App si vous ne la voyez pas dans la liste. Ensuite, cliquez sur l'option Créer une application Web :

![Créer une application web](https://cdn.hashnode.com/res/hashnode/image/upload/v1741855971071/8c120d54-1df1-41f3-85b2-c03d9fd709f1.png align="center")

Ici, sélectionnez le groupe de ressources que vous avez créé précédemment, donnez un nom à l'application, puis sélectionnez Conteneur pour l'option Publier.

![Configuration de la création de l'application web](https://cdn.hashnode.com/res/hashnode/image/upload/v1741882867790/bed19e70-726d-4696-b88f-754e36511f0a.png align="center")

Avant de cliquer sur Créer, retournez à votre espace de travail de développement (VS Code ou tout autre IDE que vous utilisez) pour pousser votre image Docker vers Docker Hub afin de pouvoir l'ajouter avant de passer aux étapes suivantes.

Mais pourquoi avez-vous besoin de pousser vers Docker Hub ? Eh bien, tout d'abord, pour l'accessibilité – afin que nous puissions facilement la partager avec d'autres ou permettre à d'autres services d'y accéder (ce dont nous avons besoin ici).

Vous vous souvenez comment j'ai comparé Docker Hub avec GitHub plus tôt ? Docker Hub vous aide à héberger votre image Docker sur Internet et à la rendre disponible pour d'autres ou pour divers services sur Internet pour y accéder si vous la rendez publique. Sinon, elle est limitée aux seuls services autorisés.

Pour pousser l'image Docker vers Docker Hub, vous devez d'abord taguer l'image Docker avec votre nom d'utilisateur Docker Hub. Allez sur Docker [Docker Hub](https://hub.docker.com/) pour vous inscrire et obtenir votre nom d'utilisateur si vous n'en avez pas.

Exécutez ce qui suit :

```bash
docker tag client_info_webservice-client_info_app:latest ayobami6/client_info_webservice-client_info_app:latest
# cela ajoute le tag latest à votre image docker
```

Cela montre que vous avez tagué votre image avec le tag latest.

![Images Docker taguées](https://cdn.hashnode.com/res/hashnode/image/upload/v1741941521765/f624e0d1-2380-41cc-8bbf-f05e55d0b0ad.png align="center")

Avant de pousser l'image vers Docker Hub, connectez-vous avec l'interface de ligne de commande Docker.

```bash
docker login # cela demandera une authentification via le navigateur, pour l'invite et connectez votre compte avec votre nom d'utilisateur et mot de passe
```

Poussez l'image vers Docker Hub comme ceci :

```bash
docker push ayobami6/client_info_webservice-client_info_app:latest
```

![Pousser l'image Docker vers Docker Hub](https://cdn.hashnode.com/res/hashnode/image/upload/v1741941723747/5947d1eb-82fe-4bf3-a0d7-e20bbc9d7de4.png align="center")

Vous devriez voir quelque chose comme ceci une fois que vous avez entré la commande de poussée sur Docker Hub.

![Vérifier l'image Docker sur Docker Hub](https://cdn.hashnode.com/res/hashnode/image/upload/v1741941947561/7050ed8b-b7bf-4e07-91a6-765549b5d715.png align="center")

Très bien, maintenant que vous avez l'image Docker sur Docker Hub, vous pouvez procéder au déploiement en utilisant Microsoft Azure App Service.

![Sélection du conteneur de création web pour la publication](https://cdn.hashnode.com/res/hashnode/image/upload/v1741944017329/32080357-e214-4864-b5cb-0fc8ad77a71f.png align="right")

Cliquez sur le conteneur dans la barre de menu supérieure pour configurer les paramètres du conteneur.

![Section du conteneur de l'application web Azure](https://cdn.hashnode.com/res/hashnode/image/upload/v1741944418747/6f9092e9-e6fc-4098-86d0-ba79eda37a58.png align="center")

Ici, sélectionnez Autres registres de conteneurs.

![Autre sélection de registre pour l'application web Azure](https://cdn.hashnode.com/res/hashnode/image/upload/v1741944507676/d4c3d17e-e3fa-4c43-99b5-b768fd900309.png align="center")

Sélectionnez public, car votre image poussée est publique (ce qui signifie qu'elle est accessible publiquement sur Internet).

![Sélection du type d'accès à l'image Docker](https://cdn.hashnode.com/res/hashnode/image/upload/v1743071959687/48cc5a78-4b72-4c8f-9ffb-d32c065e1a63.jpeg align="center")

Ajoutez votre image Docker et son tag. Vous pouvez obtenir cela lorsque vous exécutez la commande `docker images`.

![Sélection de l'image et du tag](https://cdn.hashnode.com/res/hashnode/image/upload/v1743072606918/d17f7a31-bee3-41b9-a685-d7de0c0f6b39.jpeg align="center")

```bash
 MACs-MacBook-Pro ~  docker images
REPOSITORY                                        TAG         IMAGE ID       CREATED         SIZE
ayobami6/client_info_webservice-client_info_app   latest      a14f2a5b3bd4   2 weeks ago     30.8MB
postgres                                          13-alpine   236985828131   4 weeks ago     383MB
glint_pm_frontend-nextjs                          latest      424233ceaa4b   4 weeks ago     1.72GB
flask_app-flask_app                               latest      ff6ecfc4ba5a   5 weeks ago     203MB
nginx                                             latest      124b44bfc9cc   7 weeks ago     279MB
encoredotdev/postgres                             15          58b55b0e1fc7   10 months ago   878MB
 MACs-MacBook-Pro ~  
```

Copiez le nom du dépôt et le tag – dans mon cas, j'ai `ayobami6/client_info_webservice-client_info_app` et le tag `latest` → `ayobami6/client_info_webservice-client_info_app:latest`.

Ensuite, ajoutez votre commande de démarrage. Si vous n'utilisez pas Go pour le développement comme moi, votre commande de démarrage sera différente – utilisez simplement la commande que vous avez ajoutée à la clé de commande de votre Docker compose, comme ceci `command: "./api"`. Copiez simplement la valeur (la mienne est `./api`) sans ajouter les guillemets doubles, et ajoutez-la à la commande de démarrage.

![Ajouter la commande de démarrage à la configuration du conteneur de l'application web](https://cdn.hashnode.com/res/hashnode/image/upload/v1743072910308/a208c0a1-718b-4725-99b5-47bf33691fca.jpeg align="center")

Cette commande de démarrage est la commande qui démarrera l'application à partir du conteneur et fera fonctionner le conteneur.

Cliquez sur vérifier et créer pour créer le service.

Une fois le déploiement terminé, vous serez redirigé ici :

![Aperçu de l'application web](https://cdn.hashnode.com/res/hashnode/image/upload/v1741944994364/31e051a6-2da1-46fa-a748-c2bdd20528be.png align="center")

Félicitations ! Vous avez déployé avec succès votre service web sur Azure App Service. Vous pouvez visiter votre application en utilisant le domaine par défaut de l'aperçu. Le mien est [ici](http://clientinfoapp-hdgcdmgjdyd5ecfy.canadacentral-01.azurewebsites.net).

![Test du service déployé sur Postman](https://cdn.hashnode.com/res/hashnode/image/upload/v1741945313388/19c73507-0b48-49ef-9885-515784cb0f9b.png align="center")

![Test du service déployé sur le navigateur web](https://cdn.hashnode.com/res/hashnode/image/upload/v1741945461019/30a668c7-0552-4905-bbb0-c9db0b587387.png align="center")

## Conclusion

Déployer un service web RESTful sur Microsoft Azure App Service est un moyen puissant de tirer parti de la technologie cloud pour un hébergement d'applications scalable et efficace.

Comprendre des termes clés comme Docker, Docker Hub et les groupes de ressources Azure vous aidera à rationaliser le processus de déploiement.

Ce guide vous a accompagné dans la création d'un simple service web, la construction d'une image Docker et son déploiement sur Azure. En suivant ces étapes, vous pouvez déployer vos applications en toute confiance, en garantissant qu'elles sont accessibles et performantes.

Merci d'avoir suivi ce tutoriel, et j'espère qu'il a été instructif et utile dans votre parcours de déploiement cloud. Si vous l'avez trouvé utile, n'hésitez pas à le partager avec d'autres qui pourraient en bénéficier. Bon codage et bon déploiement !

Restez à l'écoute pour plus de contenu instructif, et continuons à apprendre et à grandir ensemble. À la construction de solutions plus intelligentes et plus efficaces avec Azure.