---
title: Une introduction conviviale à Kubernetes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-09T16:48:43.000Z'
originalURL: https://freecodecamp.org/news/a-friendly-introduction-to-kubernetes-670c50ce4542
coverImage: https://cdn-media-1.freecodecamp.org/images/1*VZf19QtcEYsMaA912V0pkQ.jpeg
tags:
- name: containers
  slug: containers
- name: Docker
  slug: docker
- name: Kubernetes
  slug: kubernetes
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Une introduction conviviale à Kubernetes
seo_desc: 'By Faizan Bashir

  Kubernetes is one of the most exciting technologies in the world of DevOps these
  days. It has attracted a lot of attention over the last few years. The reason for
  its instantaneous fame is the mighty containers.

  Docker Inc. brought c...'
---

Par Faizan Bashir

Kubernetes est l'une des technologies les plus passionnantes dans le monde de DevOps ces jours-ci. Il a attiré beaucoup d'attention au cours des dernières années. La raison de sa renommée instantanée est due aux puissants **conteneurs**. 

Docker Inc. a mis en lumière les conteneurs avec leur marketing impeccable d'un produit incroyable. Docker a posé les bases de l'utilisation généralisée des conteneurs, bien que la technologie des conteneurs soit antérieure. Pourtant, grâce à Docker, l'utilisation des conteneurs Linux est devenue plus répandue, consolidant ainsi les bases des moteurs d'orchestration de conteneurs.

Entrez Kubernetes — développé par Google en utilisant des années d'expérience dans l'exécution d'une infrastructure de classe mondiale sur des milliards de conteneurs. Kubernetes a été un succès instantané, et à partir de cette année, Docker Inc. a intégré Kubernetes comme un moteur d'orchestration supplémentaire aux côtés de Docker Swarm.

Désormais, Kubernetes fera partie de la communauté Docker et de Docker Enterprise Edition. Cela semble plutôt cool, n'est-ce pas ? Le meilleur des deux mondes emballé ensemble dans un seul binaire.

### Vue d'ensemble

Kubernetes, k8s, ou kube, est une plateforme open source qui automatise les opérations de conteneurs. Elle élimine la plupart des processus manuels existants, qui impliquent le déploiement, la mise à l'échelle et la gestion des applications conteneurisées. Ouf ! C'est beaucoup de travail.

Avec Kubernetes, vous pouvez regrouper des hôtes exécutant des conteneurs ensemble. Kubernetes vous aide à gérer ces clusters. Ces clusters peuvent s'étendre sur les clouds publics, privés et hybrides — et qui sait, l'univers de Star Wars un jour.

Kubernetes a été développé et conçu par l'équipe d'ingénierie de Google. Google est depuis longtemps un contributeur à la technologie des conteneurs. En plus d'être vocal sur son utilisation de la technologie des conteneurs, Kubernetes est la technologie derrière les offres de services cloud de Google.

Google déploie plus de 2 milliards de conteneurs par semaine. Tous alimentés par une plateforme interne appelée [Borg](http://blog.kubernetes.io/2015/04/borg-predecessor-to-kubernetes.html) (cela ressemble plus à un seigneur de guerre Orc de Mordor, mais non). Borg était le prédécesseur de Kubernetes. Les leçons apprises par Google en travaillant avec Borg au fil des ans sont devenues la force directrice derrière Kubernetes.

Kubernetes rend tout ce qui est associé au déploiement et à la gestion des applications conteneurisées un plaisir. Kubernetes automatise les déploiements, les retours en arrière et surveille la santé des services déployés. Cela empêche les mauvais déploiements avant que les choses ne tournent vraiment mal.

De plus, Kubernetes peut mettre à l'échelle les services en fonction de l'utilisation, garantissant que vous n'exécutez que ce dont vous avez besoin, quand vous en avez besoin, où vous en avez besoin. Comme les conteneurs, Kubernetes nous permet de gérer des clusters, permettant à la configuration d'être contrôlée par version et répliquée.

C'était une vue d'ensemble, mais ne vous arrêtez pas ici. Il y a plus à Kubernetes que ce que l'on voit (et c'est pourquoi j'écris cela en premier lieu).

### Comment fonctionne Kubernetes ?

![Image](https://cdn-media-1.freecodecamp.org/images/ZZ4KONLpSBCx5nzqsEcfr8FEiAb3bOBBhko6)
_Référence : [https://kubernetes.io/docs/concepts/architecture/cloud-controller/](https://kubernetes.io/docs/concepts/architecture/cloud-controller/" rel="noopener" target="_blank" title=")_

Kubernetes est un système très complexe par rapport à la solution d'orchestration de Docker, Docker Swarm. Pour comprendre comment Kubernetes fonctionne, nous devons comprendre ses concepts et principes sous-jacents.

### L'état souhaité

L'état souhaité est l'un des concepts fondamentaux de Kubernetes. Vous êtes libre de définir un état pour l'exécution des conteneurs à l'intérieur des Pods. Si, en raison d'une défaillance, le conteneur cesse de fonctionner, Kubernetes recrée le Pod en fonction des lignes de l'état souhaité.

Kubernetes garantit strictement que tous les conteneurs en cours d'exécution dans le cluster sont toujours dans l'état souhaité. Cela est imposé par le Kubernetes Master qui fait partie du plan de contrôle de Kubernetes. Vous pouvez utiliser la commande `**kubectl**` qui interagit directement avec le cluster pour définir ou modifier l'état souhaité via l'API Kubernetes.

### Objets Kubernetes

Comme défini dans la [Documentation Kubernetes](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) :

> Un objet Kubernetes est un « enregistrement d'intention » — une fois que vous créez l'objet, le système Kubernetes travaillera constamment pour garantir que l'objet existe. En créant un objet, vous dites effectivement au système Kubernetes à quoi vous voulez que la charge de travail de votre cluster ressemble ; c'est l'état souhaité de votre cluster.

L'état des entités dans le système à un moment donné est représenté par les objets Kubernetes. Les objets Kubernetes agissent également comme une couche d'abstraction supplémentaire sur l'interface des conteneurs. Vous pouvez maintenant interagir directement avec des instances d'objets Kubernetes au lieu d'interagir avec des conteneurs. Les objets Kubernetes de base sont les suivants :

* [**Pod**](https://kubernetes.io/docs/concepts/workloads/pods/pod-overview/) est la plus petite unité déployable sur un nœud. C'est un groupe de conteneurs qui doivent fonctionner ensemble. Souvent, mais pas nécessairement, un Pod contient généralement un conteneur.
* [**Service**](https://kubernetes.io/docs/concepts/services-networking/service/) est utilisé pour définir un ensemble logique de Pods et les politiques associées utilisées pour y accéder.
* [**Volume**](https://kubernetes.io/docs/concepts/storage/volumes/) est essentiellement un répertoire accessible à tous les conteneurs en cours d'exécution dans un Pod.
* [**Namespaces**](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) sont des clusters virtuels soutenus par le cluster physique.

Il existe un certain nombre de contrôleurs fournis par Kubernetes. Ces contrôleurs sont construits sur les objets Kubernetes de base et fournissent des fonctionnalités supplémentaires. Les contrôleurs Kubernetes incluent :

* [**ReplicaSet**](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/) garantit qu'un nombre spécifié de répliques de Pods sont en cours d'exécution à tout moment.
* [**Deployment**](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) est utilisé pour changer l'état actuel en l'état souhaité.
* [**StatefulSet**](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) est utilisé pour assurer le contrôle sur l'ordre de déploiement et l'accès aux volumes, etc.
* [**DaemonSet**](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/) est utilisé pour exécuter une copie d'un Pod sur tous les nœuds d'un cluster ou sur des nœuds spécifiés.
* [**Job**](https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/) est utilisé pour effectuer une tâche et quitter après avoir terminé leur travail avec succès ou après une période de temps donnée.

### Plan de contrôle Kubernetes

Le **plan de contrôle Kubernetes** travaille pour faire correspondre l'état actuel du cluster à votre état souhaité. Pour ce faire, Kubernetes effectue une variété de tâches automatiquement — par exemple, démarrer ou redémarrer des conteneurs, mettre à l'échelle le nombre de répliques d'une application donnée, et bien plus encore.

Comme défini dans la [Documentation Kubernetes](https://kubernetes.io/docs/concepts/#kubernetes-control-plane) :

> Les différentes parties du plan de contrôle Kubernetes, telles que le Kubernetes Master et les processus _kubelet_, régissent la manière dont Kubernetes communique avec votre cluster. Le plan de contrôle maintient un enregistrement de tous les objets Kubernetes dans le système et exécute des boucles de contrôle continues pour gérer l'état des objets. À tout moment, les boucles de contrôle du plan de contrôle répondront aux changements dans le cluster et travailleront pour faire correspondre l'état réel de tous les objets dans le système à l'état souhaité que vous avez défini.

Le plan de contrôle Kubernetes effectue la tâche de maintenir l'état souhaité dans le cluster. Il enregistre l'état de l'objet et exécute en continu une boucle de contrôle pour vérifier si l'état actuel de l'objet correspond à l'état souhaité. Vous pouvez le considérer comme le gouvernement qui dirige l'état.

### Kubernetes Master

En tant que partie du plan de contrôle Kubernetes, le Kubernetes Master travaille en continu pour maintenir l'état souhaité dans votre cluster. La commande `**kubectl**` est une interface pour communiquer avec le Kubernetes Master du cluster via l'API Kubernetes. Pensez-y comme la force de police responsable du maintien de la loi et de l'ordre.

Comme défini dans la [Documentation Kubernetes](https://kubernetes.io/docs/concepts/#kubernetes-master) :

> Le terme « master » fait référence à une collection de processus gérant l'état du cluster. Typiquement, ces processus sont tous exécutés sur un seul nœud dans le cluster, et ce nœud est également appelé le master. Le master peut également être répliqué pour la disponibilité et la redondance.

Le **Kubernetes Master** contrôle et coordonne tous les nœuds dans le cluster à l'aide de trois processus qui s'exécutent sur un ou plusieurs nœuds maîtres dans le cluster. Chaque Kubernetes Master dans votre cluster exécute ces trois processus :

1. [**kube-apiserver**](https://kubernetes.io/docs/admin/kube-apiserver/) : le point de gestion unique pour l'ensemble du cluster. Le serveur API implémente une interface RESTful pour la communication avec les outils et les bibliothèques. La commande `**kubectl**` interagit directement avec le serveur API.
2. [**kube-controller-manager**](https://kubernetes.io/docs/admin/kube-controller-manager/) : régule l'état du cluster en gérant les différents types de contrôleurs.
3. [**kube-scheduler**](https://kubernetes.io/docs/admin/kube-scheduler/) : planifie les charges de travail sur les nœuds disponibles dans le cluster.

### Nœuds Kubernetes

Les nœuds Kubernetes sont essentiellement des machines de travail (VM, serveurs physiques, serveurs bare metal, etc.) dans un cluster exécutant vos charges de travail. Les nœuds sont contrôlés par le Kubernetes Master et sont surveillés en continu pour maintenir l'état souhaité de l'application. Auparavant, ils étaient connus sous le nom de **minions** (pas la petite armée jaune hilarante et fidèle de Gru). Similaire au master, chaque nœud Kubernetes dans votre cluster exécute deux processus :

1. [**kubelet**](https://kubernetes.io/docs/admin/kubelet/) est une interface de communication entre le nœud et le Kubernetes Master.
2. [**kube-proxy**](https://kubernetes.io/docs/admin/kube-proxy/) est un proxy réseau qui reflète les services tels que définis dans l'API Kubernetes sur chaque nœud. Il peut également effectuer un simple transfert de flux TCP et UDP.

### L'application de vote

Mettons-vous à niveau en exécutant réellement une application sur Kubernetes. Mais, avant de pouvoir faire un pas de plus dans le monde incroyable de Kubernetes, vous devrez d'abord installer et exécuter Kubernetes localement. Alors, commençons par là. Passez cette étape si vous avez déjà installé Kubernetes et MiniKube.

#### Installation de Kubernetes

Kubernetes est maintenant intégré à Docker Community Edition pour la version 17.12+. Au cas où vous n'auriez pas la Community Edition installée, vous pouvez la télécharger [ici](https://www.docker.com/community-edition).

#### Installation de MiniKube

Pour exécuter Kubernetes localement, vous devrez installer [MiniKube](https://github.com/kubernetes/minikube). Il crée une VM locale et exécute un cluster à nœud unique. Ne pensez même pas à exécuter votre cluster de production dessus. Il est préférable de l'utiliser uniquement à des fins de développement et de test.

#### Le cluster à nœud unique

Pour exécuter un cluster à nœud unique, nous devons simplement exécuter la commande `**minikube start**`. Voilà, une VM, un cluster et Kubernetes sont en cours d'exécution.

```
$ minikube start
Starting local Kubernetes v1.10.0 cluster...
Starting VM...
Getting VM IP address...
Moving files into cluster...
Setting up certs...
Connecting to cluster...
Setting up kubeconfig...
Starting cluster components...
Kubectl is now configured to use the cluster.
Loading cached images from config file.
```

Pour vérifier que votre installation a réussi, exécutez `kubectl version` pour vérifier la version de Kubernetes en cours d'exécution sur votre machine.

```
$ kubectl version
Client Version: version.Info{Major:"1", Minor:"9", GitVersion:"v1.9.1", GitCommit:"3a1c9449a956b6026f075fa3134ff92f7d55f812", GitTreeState:"clean", BuildDate:"2018-01-04T20:00:41Z", GoVersion:"go1.9.2", Compiler:"gc", Platform:"darwin/amd64"}
Server Version: version.Info{Major:"1", Minor:"10", GitVersion:"v1.10.0", GitCommit:"fc32d2f3698e36b93322a3465f63a14e9f0eaead", GitTreeState:"clean", BuildDate:"2018-03-26T16:44:10Z", GoVersion:"go1.9.3", Compiler:"gc", Platform:"linux/amd64"}
```

#### L'application de vote enfin

Passons à l'application de vote maintenant que vous avez installé Kubernetes sur votre machine locale. Il s'agit d'une application simple basée sur l'architecture de micro-services, composée de 5 services simples.

![Image](https://cdn-media-1.freecodecamp.org/images/c21Fn5g6pbiinwVWPYSSjqpcAIhckn17Wg0Z)
_Architecture de l'application de vote [[https://github.com/docker/example-voting-app](https://github.com/docker/example-voting-app" rel="noopener" target="_blank" title=")]_

1. **Voting-App** : Frontend de l'application écrit en Python, utilisé par les utilisateurs pour voter.
2. **Redis** : Base de données en mémoire, utilisée comme stockage intermédiaire.
3. **Worker** : Service .Net, utilisé pour récupérer les votes de Redis et les stocker dans la base de données Postgres.
4. **DB** : Base de données PostgreSQL, utilisée comme base de données.
5. **Result-App** : Frontend de l'application écrit en Node.js, affiche les résultats des votes.

Git `clone` et `cd` dans le dépôt de l'application de vote.

[**dockersamples/example-voting-app**](https://github.com/dockersamples/example-voting-app)
[_example-voting-app — Exemple d'application Docker Compose_github.com](https://github.com/dockersamples/example-voting-app)

Le dossier "k8s-specifications" contient les spécifications yaml Kubernetes des services de l'application de vote. Pour chaque service, il contient deux fichiers yaml : un fichier de service et un fichier de déploiement. Le fichier de service définit un ensemble logique de pods et les politiques autour d'eux. Voici le fichier de service résultant de l'application de vote.

```
apiVersion: v1
kind: Service
metadata:
  name: result
spec:
  type: NodePort
  ports:
  - name: "result-service"
    port: 5001
    targetPort: 80
    nodePort: 31001
  selector:
    app: result
```

Un fichier de déploiement est utilisé pour définir l'état souhaité de votre application, tel que le nombre de répliques qui doivent être en cours d'exécution à tout moment. Voici le fichier de déploiement résultant de l'application de vote.

```
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: result
spec:
  replicas: 1
  template:
    metadata:
      labels:
        app: result
    spec:
      containers:
      - image: dockersamples/examplevotingapp_result:before
        name: result
```

Il est temps de créer les objets de service et de déploiement — un jeu d'enfant.

```
$ kubectl create -f k8s-specifications/
deployment "db" created
service "db" created
deployment "redis" created
service "redis" created
deployment "result" created
service "result" created
deployment "vote" created
service "vote" created
deployment "worker" created
```

Et voilà ! Votre application a été déployée avec succès sur le cluster à nœud unique, et vous pouvez lister les pods et services en cours d'exécution.

```
$ kubectl get pods
NAME                      READY     STATUS    RESTARTS   AGE
db-86b99d968f-s5pv7       1/1       Running   0          1m
redis-659469b86b-hrxqs    1/1       Running   0          1m
result-59f4f867b8-cthvc   1/1       Running   0          1m
vote-54f5f76b95-zgwrm     1/1       Running   0          1m
worker-56578c48f8-h7zvs   1/1       Running   0          1m
$ kubectl get svc
NAME         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
db           ClusterIP   10.109.241.59    <none>        5432/TCP         2m
kubernetes   ClusterIP   10.96.0.1        <none>        443/TCP          23m
redis        ClusterIP   10.102.242.148   <none>        6379/TCP         2m
result       NodePort    10.106.7.255     <none>        5001:31001/TCP   2m
vote         NodePort    10.103.28.96     <none>        5000:31000/TCP   2m
```

Voici la guerre des chats contre les chiens, que les chats gagnent toujours. Les chats sont mignons par nature et leur attitude IDC est un grand avantage. Mais c'est une discussion pour une autre fois.

Revenons au moment présent, votre application de vote est exposée sur le port **30001**, et l'application de résultats est exposée sur le port **31001**. Vous pouvez y accéder en utilisant localhost:port ou, en utilisant l'IP sur laquelle minikube est en cours d'exécution, vous pouvez l'obtenir en utilisant la commande `**minikube ip**`.

![Image](https://cdn-media-1.freecodecamp.org/images/3uE3JBORlH9LiSrlHpVhXZqIPMCpBTBITHfJ)

![Image](https://cdn-media-1.freecodecamp.org/images/JQ76935N09c4g1KTzbGXH6U5bZPd6luvYbL1)

### **Feuille de triche Kubernetes**

Puisque vous avez tous montré beaucoup de patience en parcourant ces blocs de texte, laissez-moi maintenant vous présenter la feuille de triche Kubernetes (qui aurait pu être un tout nouvel article en soi, mais peu importe !) :

Commande Minikube :

```
# Démarrer le serveur Minikube
$ minikube start
# Obtenir l'IP de Minikube
$ minikube ip
```

Informations sur la version :

```
$ kubectl version             #Obtenir la version de kubectl
$ kubectl cluster-info        #Obtenir les informations du cluster
```

Création d'objets :

```
$ kubectl create -f ./file.yml
$ kubectl create -f ./file1.yml -f ./file2.yaml
$ kubectl create -f ./dir
$ kubectl create -f http://www.fpaste.org/279276/48569091/raw/
```

Visualisation et recherche de ressources :

```
# Lister tous les services dans le namespace
$ kubectl get services
# Lister tous les pods dans tous les namespaces
$ kubectl get pods --all-namespaces
# Lister tous les pods dans le namespace, avec plus de détails
$ kubectl get pods -o wide
# Lister un contrôleur de réplication particulier
$ kubectl get rc <rc-name>
# Lister tous les pods avec une étiquette env=production
$ kubectl get pods -l env=production
```

Lister les services triés par nom :

```
$ kubectl get services --sort-by=.metadata.name
```

Modification et suppression de ressources :

```
$ kubectl label pods <pod-name> new-label=awesome
$ kubectl annotate pods <pod-name> icon-url=http://goo.gl/XXBTWq
$ kubectl delete pod pingredis-XXXXX
```

Mise à l'échelle :

```
$ kubectl scale --replicas=3 deployment nginx
```

Interaction avec les Pods en cours d'exécution :

```
$ kubectl logs <pod-name>
# Exécute une sortie de log tailf
$ kubectl logs -f <pod-name>
# Exécute le pod en tant que shell interactif
$ kubectl run -i --tty busybox --image=busybox -- sh
# Attacher à un conteneur en cours d'exécution
$ kubectl attach <podname> -i
# Transférer le port du Pod vers votre machine locale
$ kubectl port-forward <podname> <local-and-remote-port>
# Transférer le port vers le service
$ kubectl port-forward <servicename> <port>
# Exécuter une commande dans un pod existant (cas à 1 conteneur)
$ kubectl exec <pod-name> -- ls /
# Exécuter une commande dans un pod existant (cas multi-conteneurs)
$ kubectl exec <pod-name> -c <container-name> -- ls /
```

Recherches DNS :

```
$ kubectl exec busybox -- nslookup kubernetes
$ kubectl exec busybox -- nslookup kubernetes.default
$ kubectl exec busybox -- nslookup kubernetes.default.svc.cluster.local
```

Créer et exposer un déploiement :

```
$ kubectl run nginx --image=nginx:1.9.12
$ kubectl expose deployment nginx --port=80 --type=LoadBalancer
```

### Résumé

Kubernetes est super excitant, cool, et très probablement l'avenir de l'orchestration de conteneurs. La technologie est géniale, et cela vaut la peine d'investir votre temps si vous êtes intéressé par les conteneurs ou simplement un fan comme moi. Kubernetes est un moteur d'orchestration de conteneurs très puissant, il peut être utilisé pour amplifier la stratégie de conteneurisation cloud car il est conçu pour automatiser le déploiement, la mise à l'échelle et l'exploitation des conteneurs.

Le côté ensoleillé est que Kubernetes s'intègre facilement à tout portefeuille cloud, qu'il soit public, privé, hybride ou multi-cloud. Les fournisseurs de cloud comme AWS et Google proposent des services Kubernetes gérés comme [Elastic Container Service for Kubernetes (EKS)](https://aws.amazon.com/eks/) et [Google Kubernetes Engine (GKE)](https://cloud.google.com/kubernetes-engine/). Le côté obscur est que Kubernetes est significativement plus complexe que le propre moteur d'orchestration de conteneurs de Docker, Docker Swarm.

Toutes les informations ici n'étaient que pour mouiller vos pieds. Si vous avez envie de plonger dans l'océan incroyable de Kubernetes, voici :

[**ramitsurana/awesome-kubernetes**](https://github.com/ramitsurana/awesome-kubernetes)
[_awesome-kubernetes - Une liste sélectionnée pour des sources kubernetes incroyables :ship::tada:_github.com](https://github.com/ramitsurana/awesome-kubernetes)

Après être sorti de la plongée profonde, vous pourriez bien vouloir vous familiariser avec Kubernetes. Prenez Kubernetes pour une balade ou laissez-le vous emmener, dans les labs Play with Kubernetes.

[**Play with Kubernetes**](http://labs.play-with-k8s.com/)
[_Play with Kubernetes est un site de labs fourni par Docker et créé par Tutorius. Play with Kubernetes est un terrain de jeu..._labs.play-with-k8s.com](http://labs.play-with-k8s.com/)

J'espère que cet article a aidé à la compréhension de Kubernetes. J'adorerais entendre parler de la manière dont vous utilisez Kubernetes dans vos projets. Applaudissez si cela a augmenté vos connaissances, et aidez-le à atteindre plus de personnes.