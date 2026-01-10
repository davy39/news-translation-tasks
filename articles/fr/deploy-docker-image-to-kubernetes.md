---
title: Comment déployer une application sur un cluster Kubernetes
subtitle: ''
author: Kunal Nalawade
co_authors: []
series: null
date: '2023-08-22T16:34:30.000Z'
originalURL: https://freecodecamp.org/news/deploy-docker-image-to-kubernetes
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/deploy-app-to-k8s-cluster.jpeg
tags:
- name: containers
  slug: containers
- name: Docker
  slug: docker
- name: Kubernetes
  slug: kubernetes
seo_title: Comment déployer une application sur un cluster Kubernetes
seo_desc: 'In today''s ever-changing technology landscape, companies are looking for
  reliable and scalable ways to run and manage software. And containers have transformed
  the way we deliver software.

  Container orchestration platforms have made it possible to de...'
---

Dans le paysage technologique en constante évolution d'aujourd'hui, les entreprises recherchent des moyens fiables et évolutifs pour exécuter et gérer des logiciels. Et les conteneurs ont transformé la manière dont nous livrons des logiciels.

Les plateformes d'orchestration de conteneurs ont rendu possible le déploiement et la gestion d'applications conteneurisées. Kubernetes est l'une de ces plateformes qui a été un changement de jeu pour les développeurs qui font face aux défis des déploiements d'applications.

Kubernetes a grandement facilité la gestion et la mise à l'échelle des déploiements selon vos besoins. Dans ce tutoriel, je vais vous aider à comprendre la simplicité de Kubernetes, alors préparez-vous.

Nous allons d'abord prendre une application Node et la packager en utilisant Docker. Ensuite, je vous montrerai comment utiliser Kubernetes – de la configuration du cluster et la création de déploiements et de services à la mise à l'échelle de l'application. Assurez-vous de rester jusqu'à la fin pour obtenir le maximum de valeur. Ce sera génial.

Vous pouvez trouver le code complet [dans ce dépôt GitHub](https://github.com/KunalN25/sample-node-application).

Je vais commencer par une note sur l'orchestration de conteneurs.

## Orchestration de conteneurs

Les conteneurs offrent un environnement efficace et isolé pour votre application. Mais à mesure que votre application grandit, le nombre de conteneurs augmente également.

Gérer les conteneurs en production peut rapidement devenir un casse-tête, surtout si vous utilisez des microservices. Les déploiements plus rapides, la surveillance, la mise à l'échelle, la mise en réseau et l'équilibrage de charge deviennent soudainement des tâches redoutables.

C'est là que l'orchestration de conteneurs intervient. Elle automatise ces défis et garantit que les conteneurs fonctionnent sans problème. Elle simplifie les processus de déploiement et de mise à l'échelle, rationalisant ainsi votre flux de travail.

En outre, l'orchestration joue un rôle dans la mise en réseau et facilite la communication entre les conteneurs sur plusieurs hôtes. Vous souhaitez exposer vos conteneurs au monde extérieur ? L'orchestration le rend sans effort.

## Comment préparer une application packagée

Votre première tâche consiste à configurer une application Node et à la packager dans une image Docker. Pour cela, vous devez avoir Node.js installé dans votre système. Si ce n'est pas le cas, suivez [ce](https://radixweb.com/blog/installing-npm-and-nodejs-on-windows-and-mac) guide pour installer Node sur Mac et Windows.

Vous n'avez pas besoin d'être familier avec Node.js ou JavaScript pour suivre ce tutoriel. Suivez simplement les étapes mentionnées ci-dessous. L'objectif principal de cet article est Kubernetes.

### Configurer l'application Node

Pour configurer votre application Node, créez un dossier appelé `sample-node-application` et naviguez à l'intérieur. Exécutez la commande `npm init` et entrez chaque valeur de champ en conséquence avec le point d'entrée comme `server.js`.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Screenshot-2023-08-20-at-8.36.24-PM.png align="left")

*commande npm init*

Un fichier `package.json` sera créé qui spécifie les dépendances nécessaires dont votre application a besoin. Créez un fichier `server.js`, celui-ci contiendra vos API.

```javascript
const express = require("express");
const data = require("./data.json")

const app = express();

app.get("/", (req, res) => {
    res.send("Bonjour, bienvenue dans l'application Node")
})

app.get("/data", (req, res) => {
    res.json(data)
})


app.listen(8000, () => {
    console.log("L'application est en cours d'exécution")
});
```

Créez un fichier `data.json` séparé et ajoutez-y des données fictives. Vous pouvez générer des données fictives à partir de [Mockaroo](https://www.mockaroo.com/).

Exécutez la commande `node server` pour vérifier si l'application est en cours d'exécution.

### Construire une image Docker

Avant de construire l'image, vérifiez si vous avez Docker installé dans votre système. Si ce n'est pas le cas, reportez-vous aux [guides d'installation](https://docs.docker.com/get-docker/) pour différents systèmes d'exploitation. Exécutez `docker --version` pour confirmer que Docker est installé.

Voici à quoi ressemblera notre Dockerfile :

```dockerfile
FROM node:18-alpine

WORKDIR /sample-node-app

COPY server.js /sample-node-app/
COPY package.json /sample-node-app/
COPY data.json /sample-node-app/

RUN npm install

CMD ["node", "server"]
```

Exécutez la commande suivante pour construire l'image Docker :

```python
docker build -t node-image .
```

Vérifiez si votre image a été créée avec la commande `docker images`. Maintenant, poussez cette image vers Docker Hub. Allez sur [Docker Hub](https://hub.docker.com/) et connectez-vous. Si vous n'avez pas de compte, allez-y et enregistrez-vous.

Une fois connecté, créez un dépôt nommé node-image et rendez-le public. Retournez à votre terminal, exécutez docker login et entrez votre nom d'utilisateur et votre mot de passe. Ensuite, étiquetez l'image avec votre nom d'utilisateur.

```python
docker image tag react-example-image <username>/node-image
```

Poussez cette image vers Docker Hub avec la commande suivante :

```python
docker push <username>/node-image
```

Votre image sera poussée vers Docker Hub.

Ici, j'ai expliqué brièvement les étapes de création de l'image. Si vous souhaitez une explication plus détaillée, vous pouvez lire mon tutoriel sur [Comment Dockeriser une Application React](https://www.freecodecamp.org/news/how-to-dockerize-a-react-application/).

Avant de plonger dans les prochaines étapes, comprenons d'abord ce qu'est Kubernetes, pourquoi il est nécessaire, et quelques concepts clés.

## Qu'est-ce que Kubernetes et pourquoi en avez-vous besoin ?

Kubernetes (abrévié en K8s) est une plateforme open-source d'orchestration de conteneurs. L'orchestration consiste à automatiser les déploiements, la mise à l'échelle et la gestion des conteneurs.

Kubernetes utilise une approche déclarative, où vous définissez l'état souhaité de vos applications dans un fichier YAML. Ensuite, Kubernetes travaillera pour atteindre cet état et s'assurera que l'état est maintenu.

Il permet une collaboration étroite entre les équipes de développement et d'exploitation, aidant également à mettre en place des pratiques [DevOps](https://medium.com/gitconnected/what-is-devops-and-how-to-adopt-its-practices-6a4a7742bb65) efficaces.

### Problèmes que Kubernetes aide à résoudre

Traditionnellement, plusieurs applications étaient déployées sur des serveurs physiques. Cela posait quelques problèmes.

Si une application finissait par prendre plus d'espace que prévu, les autres applications n'auraient pas assez de ressources. De plus, la mise à l'échelle était difficile et coûteuse pour les organisations.

Puis sont venues les machines virtuelles. Elles permettaient une meilleure utilisation des ressources que les systèmes physiques et rendaient également la scalabilité plus facile et moins chère. Mais les conteneurs fournissent une solution beaucoup plus légère que les machines virtuelles.

Pour exécuter et gérer ces conteneurs, nous avons besoin de Kubernetes pour fournir l'automatisation nécessaire avec les fonctionnalités suivantes :

* **Découverte de services et équilibrage de charge** permettent aux applications de communiquer entre elles, peu importe où elles s'exécutent.

* **Mise à l'échelle automatisée** permet à Kubernetes de mettre à l'échelle automatiquement le nombre de conteneurs en fonction des configurations fournies.

* Avec **l'auto-réparation**, Kubernetes peut redémarrer tout conteneur qui a cessé de s'exécuter ou qui a échoué à s'exécuter.

* Kubernetes permet le **montage d'un stockage** à votre déploiement automatiquement.

* **Déploiements automatisés** : Kubernetes suit un mécanisme déclaratif pour atteindre et maintenir l'état souhaité de l'application.

* **Gestion des secrets et des configurations** : Vous pouvez ajouter des configurations et des secrets aux déploiements afin que votre application puisse utiliser la configuration dont elle a besoin en fonction de l'environnement dans lequel elle est déployée (dev ou prod).

Si vous souhaitez en savoir plus sur Kubernetes et ses composants, visitez la [documentation](https://kubernetes.io/docs/concepts/overview/).

## Concepts clés de Kubernetes

Voici les concepts clés que vous devrez connaître pour utiliser efficacement Kubernetes dans vos projets.

### Qu'est-ce que les Pods ?

Un pod est une unité de déploiement unique dans Kubernetes contenant un ou plusieurs conteneurs. Les pods sont responsables de l'exécution des conteneurs de votre application dans le cluster Kubernetes. C'est une instance unique d'une application en cours d'exécution.

Vous pouvez créer un pod en utilisant une configuration YAML simple. Habituellement, vous n'avez pas besoin de les créer explicitement. Au lieu de cela, vous pouvez utiliser la configuration de déploiement pour créer un pod. Nous verrons comment faire cela sous peu.

Même si un pod peut exécuter plusieurs conteneurs, il est courant de n'exécuter qu'un seul conteneur dans un pod. Lisez plus sur les pods [ici](https://kubernetes.io/docs/concepts/workloads/pods/).

### Comment fonctionnent les déploiements ?

Kubernetes vise à maintenir l'état souhaité de l'application à tout moment. Un déploiement décrit l'état souhaité via une configuration YAML.

Une configuration de déploiement est utilisée pour décider du nombre de réplicas de vos pods, modifier la configuration du pod, revenir à un état précédent, mettre à l'échelle votre application et plus encore.

Lorsque vous créez un déploiement, il créera les pods qui exécutent les conteneurs que vous avez spécifiés. Une fois que vous avez créé une configuration de déploiement, vous n'avez pas besoin de créer un fichier de configuration séparé pour les pods. Vous comprendrez mieux dans la partie pratique.

Lisez plus sur les déploiements [ici](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/).

### Qu'est-ce que les services ?

Supposons que vous avez plusieurs applications déployées en tant que pods. Ces applications peuvent avoir besoin de communiquer entre elles. Chaque pod a sa propre adresse IP unique, donc elles peuvent simplement utiliser la même adresse IP pour communiquer, n'est-ce pas ? En fait, cela pose quelques problèmes.

Les pods ont une durée de vie relativement courte. Si un problème survient et que le pod est terminé, Kubernetes en démarre un nouveau car il doit maintenir l'état souhaité du déploiement.

Ce nouveau pod aurait une adresse IP différente. Mais les autres pods utilisent toujours l'ancienne adresse IP du pod pour communiquer. Donc, ce nouveau pod ne serait pas découvrable à moins que tous les autres pods ne mettent à jour l'IP à laquelle ils communiquent.

C'est là que les services interviennent. Les services aident à exposer des groupes de pods sur un réseau en ajoutant une couche d'abstraction. Cette abstraction fournit un point de terminaison stable pour que les pods communiquent entre eux.

Lisez plus sur les services [ici](https://kubernetes.io/docs/concepts/services-networking/service/).

Regardons un dernier concept, le cluster Kubernetes. Je sais que cela semble être beaucoup de théorie, mais ne vous inquiétez pas, la partie pratique arrive.

### Le cluster Kubernetes

Un cluster K8s est un groupe de machines (ou nœuds) qui exécutent et gèrent vos applications. Le cluster se compose de nœuds travailleurs et d'un plan de contrôle qui contrôle et gère ces travailleurs.

Le plan de contrôle prend plusieurs décisions comme la planification, le démarrage d'un nouveau pod, etc. Il se compose des composants suivants :

* **api-server** : Expose l'API Kubernetes

* **etcd** : Stockage clé-valeur pour les données du cluster

* **scheduler** : Surveille les nouveaux pods créés et attribue un nœud travailleur pour les exécuter.

* **controller-manager** : Exécute une boucle de contrôle qui surveille l'état du cluster via l'api-server et, si nécessaire, passe l'état actuel à l'état souhaité.

Les nœuds travailleurs sont responsables de l'exécution et de la maintenance des pods. Chaque nœud travailleur se compose des composants suivants :

* **kubelet** : S'assure que les conteneurs sont sains et en cours d'exécution dans le Pod.

* **kube-proxy** : Proxy réseau qui s'exécute sur chaque nœud et permet la communication avec le nœud travailleur depuis l'intérieur et l'extérieur du cluster.

* **container-runtime** : Responsable de l'exécution des conteneurs

C'est tout pour les concepts principaux – plongeons dans la partie pratique.

## Comment déployer sur un cluster Kubernetes

Jusqu'à présent, nous avons créé une image Docker de l'application Node et l'avons poussée vers Docker Hub. L'image peut être accessible depuis n'importe où.

Voyons maintenant comment vous pouvez prendre cette application et l'exécuter dans un cluster Kubernetes.

### Installation

Installons l'utilitaire de ligne de commande Kubernetes, *kubectl*. Vous trouverez les guides d'installation pour Linux, Mac et Windows [ici](https://kubernetes.io/docs/tasks/tools/#kubectl).

Après avoir suivi les étapes mentionnées, exécutez la commande suivante pour vérifier si *kubectl* a été installé :

```bash
kubectl version --client
```

### Configurer le cluster Kubernetes

Pour déployer votre application, vous devez configurer un cluster Kubernetes qui exécutera vos pods et services. Il existe de nombreux clusters fournis par plusieurs fournisseurs de cloud comme Google, Amazon et Microsoft. Pour cette application, nous utiliserons Minikube.

Minikube est un outil qui vous permet d'exécuter un cluster K8s à nœud unique sur votre ordinateur. C'est un terrain de jeu personnel pour essayer Kubernetes dans votre système.

Référez-vous à [ce](https://minikube.sigs.k8s.io/docs/start/) guide pour configurer minikube sur Mac ou Windows. Vérifiez si Minikube a été installé en exécutant la commande `minikube version`.

Exécutez la commande `minikube start` pour démarrer un cluster Kubernetes local.

### Écrire les configurations YAML

Maintenant, écrivons nos configurations de déploiement et de service dans des fichiers YAML.

Tout d'abord, voyons comment créer la configuration de déploiement, étape par étape.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: sample-node-app
  namespace: default
```

* `apiVersion` : Spécifie la version de l'API de la ressource,

* `kind` : Définit le type de ressource, qui est un déploiement.

* `metadata` : Contient des métadonnées sur le déploiement. Ici, nous avons spécifié le nom du déploiement et défini le namespace par défaut.

```yaml
spec:
  replicas: 2
  selector:
    matchLabels:
      app: sample-node-app
  template:
    metadata:
      labels:
        app: sample-node-app
    spec:
      containers:
      - name: sample-node-app
        image: kunalmac25/node-image
        imagePullPolicy: Always
        ports:
        - containerPort: 8000
```

* `spec` : Décrit l'état souhaité du déploiement.

* `replicas` : Spécifie le nombre souhaité de réplicas (instances) de l'application à exécuter, qui est 1 dans ce cas.

* Les champs `selector` et `matchLabels` spécifient les étiquettes que le déploiement peut identifier les pods avec.

* `template` : Définit un modèle pour votre pod. Vous pouvez spécifier certaines métadonnées sous le champ `metadata`. Mentionnez l'étiquette avec laquelle le pod doit être identifié.

* Le champ `spec` sous `template` décrit l'état souhaité du pod, y compris la liste des conteneurs.

* Pour chaque conteneur, vous pouvez spécifier le nom, l'image qu'il doit tirer, et le port auquel il est exposé. `imagePullPolicy` spécifie la [politique de tirage d'image](https://kubernetes.io/docs/concepts/containers/images/#image-pull-policy). Ici, j'ai utilisé `Always` (toujours tirer la dernière image du registre).

Ce sont les contenus du fichier `deployment.yaml`. Maintenant, écrivons notre `service.yaml`.

```python
apiVersion: v1
kind: Service
metadata:
  name: node-service
  namespace: default
```

Similaire au déploiement, commencez par la version de l'API et quelques métadonnées sur le service.

```python
spec:
  type: LoadBalancer
  selector:
    app: sample-node-app
  ports:
    - port: 80 
      targetPort: 8000
```

* Ici, le champ `spec` décrit l'état souhaité du Service qui est de type `LoadBalancer`.

* `selector` : Spécifie l'étiquette qui identifie le pod vers lequel le service doit diriger le trafic.

* `ports` : Spécifie la liste des ports que le service doit exposer.

* `port` : Spécifie le port sur lequel le service écoute. Le trafic externe viendra à ce port, tandis que le `targetPort` spécifie le port sur les pods vers lequel le service doit transférer le trafic. Dans notre cas, le trafic entrant sur le port 80 du service sera envoyé aux pods sur le port 8000.

### Créer le Pod, le Déploiement et le Service

Utilisez `kubectl apply` pour appliquer les configurations ci-dessus et créer les pods, le déploiement et le service.

```bash
kubectl apply -f deployment.yaml
```

```bash
kubectl apply -f service.yaml
```

Alternativement, vous pouvez également mettre ces deux configurations dans un seul fichier `manifest.yaml` et exécuter la commande apply une seule fois.

```bash
kubectl apply -f manifest.yaml
```

Vérifiez vos pods, déploiements et services en utilisant les commandes `kubectl get`.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Screenshot-2023-08-16-at-4.25.04-PM.png align="left")

*Pods, Déploiements et Services*

Assurez-vous d'avoir exécuté la commande `minikube start` avant d'appliquer des fichiers, car vous devez démarrer un cluster pour exécuter vos pods.

Vous pouvez voir à partir de la sortie ci-dessus que les deux réplicas du pod sont en cours d'exécution. Si cela montre 0/2 sous READY, cela signifie qu'il y a eu un problème lors de la création du conteneur. Vous devriez vérifier si votre application fonctionne correctement avant de la déployer à nouveau.

Vous pouvez également vérifier les journaux du pod avec la commande `kubectl logs`.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Screenshot-2023-08-16-at-4.27.47-PM.png align="left")

*Journaux du Pod*

Minikube fournit également un tableau de bord qui montre tous vos pods, déploiements et services sous forme d'interface utilisateur web. Exécutez la commande `minikube dashboard` et votre navigateur ouvrira le tableau de bord.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Screenshot-2023-08-16-at-4.29.20-PM.png align="left")

*Tableau de bord Minikube*

### Accéder à votre application

Pour accéder à votre service dans le cluster Minikube, exécutez la commande suivante pour obtenir le point de terminaison auquel votre service LoadBalancer est exposé :

```bash
minikube service <service-name> --url
```

Ouvrez le même point de terminaison dans un navigateur ou accédez-y via Postman.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Screenshot-2023-08-19-at-6.37.11-PM.png align="left")

*Point de terminaison accessible sur le navigateur*

Vous pouvez également utiliser localhost au lieu de l'adresse IP, car ils sont identiques.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Screenshot-2023-08-19-at-6.38.43-PM.png align="left")

*API accessible via Postman*

### Mettre à l'échelle votre application

Votre application est opérationnelle. Avec une demande croissante, vous devrez peut-être mettre à l'échelle votre application pour garantir des performances optimales.

Pour mettre à l'échelle votre application, augmentez le nombre de réplicas de votre déploiement en exécutant la commande suivante :

```python
kubectl scale deployment <deployment-name> --replicas=<desired-number>
```

Spécifiez le nombre souhaité de réplicas et il mettra à l'échelle vos pods.

```bash
kubectl scale deployment sample-node-app --replicas=4
```

Après avoir exécuté la commande ci-dessus, exécutez `kubectl get deployments` pour voir que le nombre de réplicas a augmenté.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Screenshot-2023-08-19-at-6.48.55-PM.png align="left")

*Nombre accru de réplicas*

Alternativement, vous pouvez modifier le fichier YAML de déploiement en changeant le nombre de réplicas et exécuter à nouveau la commande `kubectl apply`.

Si vous n'avez plus besoin d'un grand nombre de pods et souhaitez réduire votre application, exécutez simplement la même commande et spécifiez un nombre plus petit de réplicas.

```python
kubectl scale deployment sample-node-app --replicas=2
```

## Un mot sur les fournisseurs de cloud

Jusqu'à présent, vous avez créé une image Docker et l'avez déployée dans un cluster Kubernetes local. Nous avons utilisé Minikube à cette fin. Mais si vous souhaitez distribuer votre application au monde extérieur, vous devez utiliser des fournisseurs de cloud.

Il existe de nombreuses options disponibles telles que AWS, Azure, GCP, VMware Tanzu, et d'autres. Ces plateformes fournissent de nombreux services comme la gestion de clusters, la mise à l'échelle, la mise en réseau et le stockage, l'intégration CI/CD, et bien plus encore.

Ces plateformes combinent les capacités de Kubernetes avec les forces de leurs propres systèmes cloud. Chaque produit vient avec ses propres services et plans tarifaires, alors choisissez celui qui correspond à vos exigences et à votre budget.

Dans un paysage cloud en rapide évolution, il est important de comprendre ce que chaque fournisseur de cloud offre et de prendre des décisions éclairées qui s'alignent avec les exigences et les objectifs de votre organisation.

## Conclusion

Kubernetes est une plateforme populaire d'orchestration de conteneurs et est très facile à utiliser. Avoir une bonne maîtrise de ses concepts vous aide à tirer parti de cette plateforme pour votre application.

Dans ce tutoriel, mon objectif était de fournir un guide complet, étape par étape, sur le déploiement de votre application sur un cluster Kubernetes. J'ai également établi une base sur quelques concepts clés de Kubernetes qui incluent les pods, les déploiements, les services et le cluster lui-même.

J'ai commencé avec une simple application Node et l'ai packagée dans une image Docker. Une fois que vous étiez clair avec les concepts clés, j'ai donné des étapes détaillées, de l'installation et de la configuration du cluster Kubernetes au déploiement de votre application en tant que pods et à leur exposition via des services.

Kubernetes prend lentement le contrôle du paysage cloud et il est là pour rester. J'espère avoir réussi à rendre Kubernetes facile pour vous. Cela vous aidera certainement à déployer vos applications sur n'importe quel cluster Kubernetes, pas seulement ceux que j'ai mentionnés.

Si vous ne comprenez pas le contenu ou trouvez l'explication insatisfaisante, faites-le moi savoir. Les nouvelles idées sont toujours appréciées ! N'hésitez pas à me contacter sur Twitter. En attendant, au revoir !