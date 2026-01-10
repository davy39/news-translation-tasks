---
title: Comment conteneuriser et déployer vos applications Node.js
subtitle: Apprenons à conteneuriser votre application avec Docker et à la déployer
  en production en quelques étapes seulement.
author: Manish Shivanandhan
co_authors: []
series: null
date: '2025-10-09T23:10:37.662Z'
originalURL: https://freecodecamp.org/news/how-to-containerize-and-deploy-your-nodejs-applications
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1760051426715/fd0f14cf-95dc-4191-b0fc-e5c916520097.png
tags:
- name: containers
  slug: containers
- name: Node.js
  slug: nodejs
- name: Docker
  slug: docker
seo_title: Comment conteneuriser et déployer vos applications Node.js
seo_desc: 'When you build a Node.js application, running it locally is simple. You
  type npm start, and it works.

  But when you need to run it on the cloud, things get complicated. You need to think
  about servers, environments, dependencies, and deployment pipeli...'
---

Lorsque vous créez une application Node.js, l'exécuter localement est simple. Vous tapez `npm start`, et cela fonctionne.

Mais lorsque vous devez l'exécuter sur le cloud, les choses se compliquent. Vous devez penser aux serveurs, aux environnements, aux dépendances et aux pipelines de déploiement. C'est là que la conteneurisation intervient.

Les conteneurs rendent votre application portable et prévisible. Vous pouvez exécuter le même code avec la même configuration n'importe où, de votre ordinateur portable au cloud.

Dans ce guide, nous allons voir comment conteneuriser une API Node.js simple et la déployer sur le cloud. À la fin, vous saurez comment configurer Docker pour votre application, la pousser vers un registre et voir votre application s'exécuter sur le cloud.

## **Table des matières**

* [Prérequis](#heading-prerequis)
    
* [Qu'est-ce que la conteneurisation ?](#heading-quest-ce-que-la-conteneurisation)
    
* [Configuration d'une application Node.js](#heading-configuration-dune-application-nodejs)
    
* [Écriture du Dockerfile](#heading-ecriture-du-dockerfile)
    
* [Construction et test du conteneur](#heading-construction-et-test-du-conteneur)
    
* [Préparation au déploiement](#heading-preparation-au-deploiement)
    
* [Déploiement sur le cloud](#heading-deploiement-sur-le-cloud)
    
* [Mise à l'échelle de votre application](#heading-mise-a-lechelle-de-votre-application)
    
* [Mise à jour de votre application](#heading-mise-a-jour-de-votre-application)
    
* [Avantages de l'utilisation des conteneurs](#heading-avantages-de-lutilisation-des-conteneurs)
    
* [Conclusion](#heading-conclusion)
    

## Prérequis

Avant de nous plonger dans la conteneurisation et le déploiement de votre application Node.js, assurez-vous d'avoir configuré les éléments suivants sur votre système. Ces bases vous aideront à suivre sans rencontrer d'erreurs.

**Node.js et npm**  
Vous devriez avoir [Node.js](https://nodejs.org/en) (v18 ou supérieur) et npm installés sur votre machine locale. Cela garantit que vous pouvez exécuter votre application localement avant de la conteneuriser.  
Pour vérifier vos versions, exécutez :

```python
node -v
npm -v
```

**Docker installé et en cours d'exécution**  
[Docker](https://www.docker.com/) est l'outil principal que nous utiliserons pour conteneuriser l'application. Installez Docker Desktop ou Docker Engine selon votre système. Une fois installé, confirmez qu'il fonctionne en tapant :

```python
docker --version
```

**Compte Docker Hub (ou tout autre registre de conteneurs)**  
Vous aurez besoin d'un compte Docker Hub pour pousser votre image de conteneur vers le cloud. Cela permet à votre plateforme de déploiement de récupérer et d'exécuter l'image. Vous pouvez en créer un gratuitement sur [hub.docker.com](http://hub.docker.com)[.](https://hub.docker.com/)

Une fois ces prérequis prêts, vous serez paré pour construire votre première application Node.js conteneurisée et la déployer sur le cloud.

## **Qu'est-ce que la conteneurisation ?**

La conteneurisation est un moyen d'empaqueter une application avec tout ce dont elle a besoin pour fonctionner. Cela inclut le code, les bibliothèques, les outils système et les paramètres. Ce paquet est appelé une image de conteneur.

Lorsque vous exécutez cette image, vous obtenez un conteneur qui se comporte exactement de la même manière sur n'importe quel système prenant en charge [Docker](https://www.freecodecamp.org/news/the-docker-handbook/).

Sans conteneurs, le déploiement peut être laborieux. Votre application peut fonctionner sur votre machine mais échouer en production en raison de bibliothèques manquantes ou de discordances de versions.

Les conteneurs résolvent ce problème en verrouillant l'environnement. Considérez-les comme des machines virtuelles légères qui ne contiennent que ce dont votre application a besoin.

## **Configuration d'une application Node.js**

Commençons par construire une API Node.js simple. Nous la garderons minimale afin de pouvoir nous concentrer sur les étapes de conteneurisation et de déploiement.

Créez un nouveau dossier et ajoutez un fichier nommé `server.js` :

```plaintext
const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

app.get('/', (req, res) => {
  res.json({ message: 'Hello from Container!' });
});
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

Ensuite, créez un fichier `package.json` avec le contenu suivant :

```plaintext
{
  "name": "container-node-app",
  "version": "1.0.0",
  "main": "server.js",
  "scripts": {
    "start": "node server.js"
  },
  "dependencies": {
    "express": "^5.1.0"
  }
}
```

Exécutez `npm install` pour installer la dépendance Express. Vous avez maintenant une API Node.js simple qui s'exécute localement. Vous pouvez la tester avec `npm start` et ouvrir `http://localhost:3000` dans votre navigateur.

## **Écriture du Dockerfile**

Pour exécuter cette application dans un conteneur, nous devons écrire un `Dockerfile`. Ce fichier définit comment construire l'image du conteneur. Créez un nouveau fichier nommé `Dockerfile` et ajoutez ceci :

```plaintext
FROM node:24

WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["npm", "start"]
```

Analysons cela. Nous commençons par l'image officielle Node.js 24. Nous définissons un répertoire de travail à l'intérieur du conteneur. Nous copions les fichiers package et installons les dépendances.

Ensuite, nous copions le reste du code. Nous exposons le port 3000 pour que l'application puisse accepter du trafic. Enfin, nous exécutons `npm start` comme commande par défaut.

## **Construction et test du conteneur**

Maintenant que nous avons le `Dockerfile`, nous pouvons construire l'image. Exécutez la commande suivante :

```plaintext
docker build -t container-node-app .
```

Cela construit une image nommée `container-node-app`. Pour la tester localement, exécutez :

```plaintext
docker run -p 3000:3000 container-node-app
```

Ouvrez `http://localhost:3000` dans votre navigateur, et vous devriez voir le message JSON `{"message":"Hello from Container!"}`. À ce stade, nous savons que notre application fonctionne dans un conteneur.

## **Préparation au déploiement**

Pour déployer sur n'importe quelle plateforme cloud, vous devez pousser votre image vers un registre de conteneurs. Un registre est un endroit où les images de conteneurs sont stockées et partagées. Votre fournisseur cloud peut récupérer des images depuis [Docker Hub](https://hub.docker.com/) ou d'autres registres.

Étiquetez (tag) votre image avec un chemin de registre. Pour Docker Hub, cela ressemble à ceci :

```plaintext
docker tag container-node-app votre-nom-utilisateur-dockerhub/container-node-app:latest
```

Ensuite, connectez-vous et poussez-la :

```plaintext
docker login
docker push votre-nom-utilisateur-dockerhub/container-node-app:latest
```

Votre image devrait maintenant être disponible dans le registre cloud et prête pour le déploiement.

Voici la mienne :

![Registre Docker](https://cdn.hashnode.com/res/hashnode/image/upload/v1759747825354/e217d7f1-6131-41a2-a8b1-76e8ad84399a.webp align="center")

## **Déploiement sur le cloud**

Dans ce tutoriel, j'utiliserai Sevalla car il propose un niveau gratuit, il n'y a donc aucun coût impliqué pour déployer ce conteneur sur le cloud. Vous pouvez utiliser d'autres fournisseurs comme [AWS](https://aws.amazon.com/) ou [Heroku](https://www.heroku.com/), mais notez que vous encourrez des frais pour la création de ressources.

[Sevalla](https://sevalla.com/) est un fournisseur moderne de plateforme en tant que service (PaaS) basé sur l'utilisation. Il propose l'hébergement d'applications, de bases de données, de stockage d'objets et l'hébergement de sites statiques pour vos projets.

Une fois votre compte configuré, vous pouvez créer une nouvelle application et lui indiquer quelle image de conteneur utiliser. Sevalla récupérera l'image du registre, créera un conteneur et gérera le réseau, la mise à l'échelle et les mises à jour pour vous.

Pour commencer, [connectez-vous](https://app.sevalla.com/login) à Sevalla. Dans le tableau de bord, choisissez de créer une nouvelle application. Donnez-lui un nom comme `node-api`. Fournissez le chemin du registre de votre image.

![Créer une application](https://cdn.hashnode.com/res/hashnode/image/upload/v1759747861994/4ad344d6-d8a5-4593-a85e-eb679bc600f5.webp align="center")

Choisissez un emplacement et utilisez le plan « Hobby ». Sevalla offre un crédit gratuit de 50 $, vous ne serez donc pas facturé pour le déploiement de cette image.

![Ressources de l'application](https://cdn.hashnode.com/res/hashnode/image/upload/v1759747920267/cf23401d-131e-4c51-a248-411d8624542c.webp align="center")

Cliquez sur « Create and Deploy ». Sevalla s'occupera du reste. Vous pouvez le regarder configurer l'application et exécuter le déploiement.

![Déploiement Sevalla](https://cdn.hashnode.com/res/hashnode/image/upload/v1759747953591/79db7997-88a3-48f7-ae09-65703ec2abab.webp align="center")

Une fois le déploiement terminé, cliquez sur « Visit app » pour obtenir l'URL en direct de votre application. Vous pouvez voir la réponse de l'API.

![Succès du déploiement Sevalla](https://cdn.hashnode.com/res/hashnode/image/upload/v1759747987239/b3a1de3a-3f3a-48d6-86e1-27137f6b41fd.webp align="center")

## **Mise à l'échelle de votre application**

L'un des principaux avantages de Sevalla est la facilité de mise à l'échelle. Si vous commencez à recevoir plus de trafic, vous pouvez augmenter le nombre de conteneurs exécutant votre application en quelques clics seulement. Sevalla équilibrera la charge du trafic entre eux. Cela signifie que votre application peut gérer plus de requêtes sans interruption de service.

La mise à l'échelle avec des conteneurs est efficace car chaque conteneur exécute exactement le même code. Il n'est pas nécessaire de configurer manuellement des serveurs supplémentaires. Sevalla s'occupe de l'orchestration, afin que vous puissiez vous concentrer sur l'écriture du code plutôt que sur la gestion de l'infrastructure.

## **Mise à jour de votre application**

Lorsque vous apportez des modifications à votre application Node.js, la mise à jour est simple. Vous reconstruisez l'image Docker, vous la poussez vers le registre et vous demandez à Sevalla de redéployer.

Comme les conteneurs sont immuables, chaque nouvelle construction crée un environnement frais. Cela garantit que vos mises à jour sont propres, cohérentes et exemptes d'anciennes dépendances.

Par exemple, si vous modifiez le message dans `server.js` et souhaitez le déployer, vous exécuteriez :

```plaintext
docker build -t votre-nom-utilisateur-dockerhub/container-node-app:latest .
docker push votre-nom-utilisateur-dockerhub/container-node-app:latest
```

Ensuite, déclenchez un redéploiement dans le tableau de bord Sevalla. En quelques minutes, vos utilisateurs verront la réponse mise à jour.

## **Avantages de l'utilisation des conteneurs**

Les [conteneurs](https://techcrunch.com/2016/10/16/wtf-is-a-container/) apportent de nombreux avantages lors du déploiement d'applications Node.js. Ils rendent votre application portable car le conteneur contient à la fois le code et ses dépendances, garantissant qu'elle fonctionne de la même manière partout.

Ils améliorent la cohérence, car chaque construction crée un environnement isolé sans fichiers restants ou versions incompatibles. La mise à l'échelle devient simple car vous pouvez lancer plus de conteneurs à mesure que le trafic augmente, et chacun se comporte de manière identique. Les mises à jour sont également plus propres, car vous remplacez les anciens conteneurs par de nouveaux construits à partir du code le plus récent.

Pour les développeurs, cela signifie moins de surprises et moins de temps passé à corriger des problèmes d'environnement. Les conteneurs fournissent une base fiable, vous permettant de vous concentrer sur la création de fonctionnalités plutôt que sur le dépannage des déploiements.

## **Conclusion**

La conteneurisation est l'un des changements les plus importants dans le développement logiciel moderne. En apprenant à mettre votre application Node.js dans un conteneur Docker, vous débloquez la possibilité de l'exécuter n'importe où.

Dans ce guide, nous avons construit une petite API Node.js, créé un Dockerfile, testé le conteneur localement, l'avons poussé vers un registre et l'avons déployé sur le cloud. Les étapes que vous avez suivies ici s'appliquent également à des applications beaucoup plus grandes et plus complexes. Une fois que vous maîtrisez les bases, vous pouvez adapter vos flux de travail à des projets de niveau production.

J'espère que vous avez apprécié cet article. Contactez-moi [sur LinkedIn](https://www.linkedin.com/in/manishmshiva/?originalSubdomain=in) ou [visitez mon site web](https://manishshivanandhan.com/).