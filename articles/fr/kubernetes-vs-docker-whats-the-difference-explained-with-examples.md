---
title: 'Kubernetes VS Docker : Quelles sont les différences ? Expliqué avec des exemples'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-12-10T18:03:22.000Z'
originalURL: https://freecodecamp.org/news/kubernetes-vs-docker-whats-the-difference-explained-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2020/12/docker-vs-kubernetes-2.jpg
tags:
- name: containers
  slug: containers
- name: Docker
  slug: docker
- name: Kubernetes
  slug: kubernetes
seo_title: 'Kubernetes VS Docker : Quelles sont les différences ? Expliqué avec des
  exemples'
seo_desc: "By Sebastian Sigl\nNowadays, two of the essential tools in a developer's\
  \ toolbox are Docker and Kubernetes. Both let developers to package applications\
  \ into containers to run them in different environments. \nAlthough you can achieve\
  \ similar things usi..."
---

Par Sebastian Sigl

De nos jours, deux des outils essentiels dans la boîte à outils d'un développeur sont Docker et Kubernetes. Tous deux permettent aux développeurs d'empaqueter des applications dans des conteneurs pour les exécuter dans différents environnements. 

Bien que vous puissiez atteindre des objectifs similaires avec les deux, en pratique, ils diffèrent dans leur utilisation.

Dans cet article, vous obtiendrez une explication sur Docker et Kubernetes, et vous construirez une exemple d'application web NodeJS et la déployerez en utilisant les deux technologies.

## Qu'est-ce que Docker ?

Voici comment les gens définissent Docker sur Wikipedia :

> "Docker peut empaqueter une application et ses dépendances dans un conteneur virtuel qui s'exécute sur n'importe quel serveur Linux. Cela permet aux applications de s'exécuter dans une variété d'endroits, tels que sur site, dans un cloud public et/ou dans un cloud privé. Docker utilise les fonctionnalités d'isolation des ressources du noyau Linux (telles que les cgroups et les espaces de noms du noyau) et un système de fichiers capable d'union (tel que OverlayFS) pour permettre aux conteneurs de s'exécuter au sein d'une seule instance Linux, évitant ainsi la surcharge de démarrage et de maintenance des machines virtuelles." — Wikipedia

En bref, Docker est une plateforme pour exécuter des conteneurs immuables encapsulés avec des performances proches du natif sur une machine souhaitée. 

Il existe des alternatives à Docker qui ont des propriétés similaires comme LC, rkt ou containerd. Docker est simplement le plus populaire.

## Qu'est-ce que Kubernetes ?

Voici comment les gens définissent Kubernetes sur Wikipedia :

> Kubernetes définit un ensemble de blocs de construction ("primitives"), qui fournissent collectivement des mécanismes pour déployer, maintenir et mettre à l'échelle des applications basées sur le CPU, la mémoire ou des métriques personnalisées. Kubernetes est faiblement couplé et extensible pour répondre à différentes charges de travail. Cette extensibilité est fournie en grande partie par l'API Kubernetes, qui est utilisée par les composants internes ainsi que par les extensions et les conteneurs qui s'exécutent sur Kubernetes. La plateforme exerce son contrôle sur les ressources de calcul et de stockage en définissant les ressources comme des objets, qui peuvent ensuite être gérés comme tels. — Wikipedia

En bref, Kubernetes gère plusieurs hôtes et déploie des conteneurs sur eux. La technologie de conteneur la plus utilisée pour exécuter des conteneurs sur ces hôtes est Docker.

Assez parlé, mettons les mains dans le cambouis et expérimentons les différences par nous-mêmes.

## Comment construire et déployer une application web NodeJS en utilisant Docker et Kubernetes.

Si vous n'avez pas encore installé Docker, vous devriez le faire. Consultez et installez Docker depuis [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/).

```shell
$ docker --version

Docker version 19.03.13, build 4484c46d9d
```

Créons un fichier de package NodeJS et ajoutons une seule dépendance de serveur web appelée [Express](https://expressjs.com).

```javascript
// fichier : package.json

{
  "name": "docker-vs-k8s",
  "version": "1.0.0",
  "description": "",
  "main": "server.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "node server.js"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "express": "^4.17.1"
  }
}
```

De plus, nous devons démarrer le serveur web et définir un seul point de terminaison.

```javascript
// fichier : server.js

const express = require('express');

// Constantes
const PORT = 8080;
const HOST = '0.0.0.0';

// App
const app = express();
app.get('/', (req, res) => {
  res.send('Hello World');
});

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);
```

_FYI : Il est possible de sauter l'étape suivante si vous n'avez pas NodeJS installé. L'étape suivante utilisera une image Docker qui vient avec un environnement Node prêt à l'emploi._

Si vous avez NodeJS installé sur votre PC local, vous pouvez essayer d'exécuter l'application avec NodeJS seul. 

```shell
$ npm install
$ node server.js 

Running on http://0.0.0.0:8080
```

Ouvrez [http://localhost:8080](http://localhost:8080/), et vous verrez votre réponse hello world.

### Trouvons une image Docker de base pour exécuter notre application

Le [Docker Hub](https://hub.docker.com/) public est une excellente source. Si vous recherchez 'node', vous trouverez rapidement une [image qui a été utilisée plus d'un milliard de fois](https://hub.docker.com/_/node).

Un conteneur doit être assemblé à partir de sa fondation. Nous commençons par une image de base qui contient un environnement NodeJS prêt à l'emploi. Elle est généralement construite sur une simple image Linux. Nous copions tous les fichiers requis dans le conteneur. 

Ensuite, nous exécutons des commandes, par exemple, pour récupérer toutes les dépendances requises. La dernière étape consiste à indiquer au conteneur quelle commande exécuter lorsque le conteneur démarre. 

```dockerfile
# fichier : 'Dockerfile'

# lts-alpine signifie support à long terme et alpine est une très petite distribution Linux 
# qui est beaucoup plus petite que celle par défaut (node:lts).
# des images plus petites signifient des builds plus rapides et un temps de démarrage très pratique 
# lorsqu'il s'agit de mettre à l'échelle des conteneurs pour la production
FROM node:lts-alpine

# Créer un répertoire pour l'application
WORKDIR /usr/src/app

# Installer les dépendances de l'application
COPY package*.json ./

# Installer toutes les dépendances
RUN npm install

# Copier les sources
COPY server.js server.js

CMD [ "node", "server.js" ]
```

Maintenant, construisons l'image : 

```shell
docker build -t node-web-app .
```

Nous pouvons exécuter le conteneur Docker par :

```shell
$ docker run --name my_container -p 8080:8080 node-web-app

Running on http://0.0.0.0:8080
```

Ouvrez [http://localhost:8080](http://localhost:8080) dans votre navigateur et vous verrez la page hello world. Cette fois, elle s'exécute isolée dans un conteneur. 

Vous n'avez même pas besoin de NodeJS ou autre chose pour construire et exécuter ce conteneur. Tout est encapsulé, et grâce à la nature de Docker, il s'exécute avec des performances natives.

Arrêtons ce conteneur qui pourrait encore s'exécuter en arrière-plan :

```shell
$ docker rm -f my_container
```

_FYI : Des performances proches de 100 % du natif ne sont vraies que pour les hôtes Linux. Pour Mac OS et Windows, une certaine traduction et virtualisation sont nécessaires, ce qui entraîne une certaine dégradation des performances. Pour le développement, cela devrait être acceptable. Plus important encore, les serveurs de production exécutent généralement un Linux natif qui fonctionne bien avec Docker._

Ensuite, utilisons notre conteneur précédemment construit dans un cluster Kubernetes. Dans ce tutoriel, nous nous concentrerons sur un cluster local. Si vous allez à distance, c'est très similaire. 

Dans une configuration à distance, vous devez également pousser votre image vers un registre accessible au public, ce qui permet à votre cluster distant d'accéder à l'image. 

Je pourrais écrire un autre article de blog à ce sujet dans le futur si les gens le demandent.

### Exécutez votre application web dans Kubernetes

Votre Docker vient déjà avec une intégration Kubernetes. Ouvrez l'application Docker, allez dans _Paramètres -> Kubernetes_ et activez Kubernetes. 

L'application des modifications peut prendre un certain temps. Vous êtes prêt dès que le statut de votre Kubernetes dans la barre du bas de votre application Docker est vert. 

Si vous avez des problèmes, allez dans le dépannage (la petite icône de bug dans le coin supérieur droit), et appuyez sur réinitialiser aux paramètres d'usine. Ensuite, Docker devrait redémarrer et vous devez activer Kubernetes à nouveau.

Installons kubectl, l'un des outils les plus importants pour interagir avec votre cluster Kubernetes. Suivez ce guide pour l'installer : [https://kubernetes.io/docs/tasks/tools/install-kubectl/](https://kubernetes.io/docs/tasks/tools/install-kubectl/).

Maintenant, nous pouvons vérifier si tout est configuré correctement :

```shell
$ kubectl get services

NAME TYPE CLUSTER-IP EXTERNAL-IP PORT(S) AGE
kubernetes ClusterIP 10.96.0.1 <none> 443/TCP 3m14s
```

Déployons notre conteneur Docker dans notre cluster :

```yaml
# fichier 'application/deployment.yaml'

apiVersion: apps/v1
kind: Deployment
metadata:
  name: node-web-app
spec:
  selector:
    matchLabels:
      app: node-web-app
  replicas: 2 # indique au déploiement d'exécuter 2 pods correspondant au modèle
  template:
    metadata:
      labels:
        app: node-web-app
    spec:
      containers:
        - name: node-web-app
          image: node-web-app
          
          # n'utilisez ceci que pour le développement local
          # nous n'avons jamais poussé notre image vers un registre distant
          # et par défaut Kubernetes tire les images
          # cette propriété force Kubernetes à toujours utiliser 
          # l'image locale, ce qui n'est pas une bonne pratique en production
          imagePullPolicy: Never
          ports:
            - containerPort: 8080

```

Le fichier deployment.yaml est un fichier qui décrit le déploiement à effectuer. Nous pouvons l'exécuter par :

```shell
$ kubectl apply -f application/deployment.yaml

deployment.apps/node-web-app created
```

et vérifier si les conteneurs sont en cours d'exécution :

```shell
$ kubectl get pods

NAME READY STATUS RESTARTS AGE
node-web-app-6788cfd6cc-bcbb2 1/1 Running 0 3s
node-web-app-6788cfd6cc-t5t6w 1/1 Running 0 3s

```

Notre Kubernetes gère un cluster qui contient un seul hôte, qui est notre machine locale. Sur un cluster distant, il peut y avoir des centaines de nœuds qui hébergent différents déploiements. 

Il a déployé deux conteneurs dans notre environnement. Ces conteneurs s'exécutent dans un réseau isolé. Sinon, il ne serait pas possible d'exposer le même port deux fois. 

Alors, comment accéder au conteneur réel ? Vous pouvez accéder à un conteneur déployé en définissant un soi-disant service. Chaque application publique a besoin d'un service devant elle qui définit le port public exposé.

```yaml
# fichier 'application/service.yaml'

apiVersion: v1
kind: Service
metadata:
  name: my-service-for-my-webapp
spec:
  type: LoadBalancer
  selector:
    app: my-example-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080

```

Nous mappons le port du conteneur 8080 à un port public disponible 80. Le service agit comme un équilibreur de charge. Il distribue les requêtes parmi les conteneurs.

Déployons notre service :

```shell
$ kubectl apply -f ./application/service.yaml 

service/my-service-for-my-webapp created
```

nous pouvons vérifier si notre service est en cours d'exécution :

```shell
$ kubectl describe svc my-service-for-my-webapp

Name: my-service-for-my-webapp
Namespace: default
Labels: <none>
Annotations: Selector: app=my-example-app
Type: LoadBalancer
IP: 10.104.18.24
LoadBalancer Ingress: localhost
Port: <unset> 80/TCP
TargetPort: 8080/TCP
NodePort: <unset> 32114/TCP
Endpoints: 10.1.0.17:8080,10.1.0.18:8080
Session Affinity: None
External Traffic Policy: Cluster
Events: <none>

```

La sortie est très descriptive et confirme ce que nous voulons atteindre. Elle utilise des points de terminaison de deux conteneurs déployés (appelés pods dans Kubernetes).

Maintenant, vous pouvez ouvrir [http://localhost:80](http://localhost:80)

C'est tout ! Vous avez créé un conteneur Docker et l'avez utilisé dans votre cluster Kubernetes. Cette configuration est puissante et est la base de nombreux produits et entreprises scalables de nos jours.

## Finalisation

Nettoyons notre espace d'expérimentation :

```shell
$ kubectl delete -f ./application/service.yaml 

service "my-service-for-my-webapp" deleted

$ kubectl delete -f application/deployment.yaml

deployment.apps "node-web-app" deleted
```

Pour garder les ressources de notre appareil libres, nous devrions également arrêter la fonctionnalité Kubernetes de Docker.

J'espère que vous avez apprécié cet exemple pratique. Motivez-vous à chercher sur Google, à consulter d'autres exemples, à déployer des conteneurs, à les connecter et à les utiliser. 

Vous apprendrez de nombreuses fonctionnalités intéressantes à l'avenir qui vous permettront de déployer votre application en production de manière sans effort, réutilisable et scalable.

Comme toujours, j'apprécie tout commentaire et feedback. 

J'espère que vous avez apprécié l'article. Si vous l'aimez et ressentez le besoin d'une salve d'applaudissements, [suivez-moi sur Twitter](https://twitter.com/sesigl). Je travaille chez eBay Kleinanzeigen, l'une des plus grandes entreprises de petites annonces au monde. Au fait, [nous recrutons](https://jobs.ebayclassifiedsgroup.com/ebay-kleinanzeigen) !

Bon Docker !

## Références :

* [https://en.wikipedia.org/wiki/Kubernetes](https://en.wikipedia.org/wiki/Kubernetes)
* [https://en.wikipedia.org/wiki/Docker_(software)](https://en.wikipedia.org/wiki/Docker_(software))
* [https://labs.play-with-docker.com/](https://labs.play-with-docker.com/)
* [https://labs.play-with-k8s.com/](https://labs.play-with-k8s.com/)
* [https://nodejs.org/en/docs/guides/nodejs-docker-webapp/](https://nodejs.org/en/docs/guides/nodejs-docker-webapp/)