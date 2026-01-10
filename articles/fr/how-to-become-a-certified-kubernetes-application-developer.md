---
title: Comment devenir un développeur d'applications certifié Kubernetes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-04-14T15:57:28.000Z'
originalURL: https://freecodecamp.org/news/how-to-become-a-certified-kubernetes-application-developer
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/kubernetes-ckad-color-1024x1003.png
tags:
- name: containers
  slug: containers
- name: Kubernetes
  slug: kubernetes
seo_title: Comment devenir un développeur d'applications certifié Kubernetes
seo_desc: "By Sergio Fuentes Navarro\nThis guide is a summary of my study notes for\
  \ the Certified Kubernetes Application Developer (CKAD) exam that I recently passed.\
  \ \nEven if you're not interested in the certification, consider this as your one-stop\
  \ shop for Ku..."
---

Par Sergio Fuentes Navarro

Ce guide est un résumé de mes notes d'étude pour l'examen Certified Kubernetes Application Developer (CKAD) que j'ai récemment réussi. 

Même si vous n'êtes pas intéressé par la certification, considérez ceci comme votre **guichet unique** pour Kubernetes : vous avez tous les principaux concepts techniques expliqués ainsi qu'une myriade d'exemples en un seul endroit.

De plus, il contient quelques **extras qui proviennent de mon expérience de préparation et de passage de l'examen**.

Au moment de la rédaction de ce guide, le programme CKAD (domaines d'étude et poids de chaque domaine) est le suivant :

* 13 % – Concepts de base
* 18 % – Configuration
* 10 % – Pods multi-conteneurs
* 18 % – Observabilité
* 20 % – Conception de pods
* 13 % – Services et mise en réseau
* 8 % – Persistance de l'état

Ce guide couvre le programme, mais dans un ordre différent.

Je vais supposer que vous connaissez déjà les bases de Kubernetes (principalement les conteneurs et les pods) et que vous cherchez à faire passer vos compétences au niveau supérieur. Réussir cet examen fera ressortir votre CV car il s'agit d'une certification très recherchée.

## Sommaire

* [Introduction à Kubernetes](#heading-installation)
* [Comment gérer les clusters dans Kubernetes](#heading-comment-gerer-les-clusters-dans-kubernetes)
* [Au-delà des pods et des déploiements](#heading-au-dela-des-pods-et-des-deploiements)
* [Comment configurer les pods et les conteneurs](#heading-comment-configurer-les-pods-et-les-conteneurs)
* [Comment planifier les pods dans Kubernetes](#heading-comment-planifier-les-pods-dans-kubernetes)
* [Stockage dans Kubernetes](#heading-stockage-dans-kubernetes)
* [Réseau et sécurité dans Kubernetes](#heading-reseau-et-securite-dans-kubernetes)
* [Observabilité et débogage dans Kubernetes](#heading-observabilite-et-debogage-dans-kubernetes)
* [Conseils et astuces](#heading-conseils-et-astuces)
* [Temps de pratique](#heading-temps-de-pratique)
* [Conclusions](#heading-conclusions)

## Introduction à Kubernetes

Kubernetes est une technologie qui permet le déploiement et la gestion faciles d'applications conteneurisées sur plusieurs nœuds. Certaines de ses fonctionnalités les plus marquantes sont :

* Configuration et déploiement de conteneurs
* Surveillance du système
* Stockage persistant
* Planification automatisée
* Auto-scaling et auto-healing

Et bien plus encore.

Kubernetes fonctionne de manière **déclarative** : vous définissez l'état que vous souhaitez pour votre cluster et Kubernetes travaille pour s'assurer que le cluster est toujours dans cet état. 

Pour définir ou modifier cet état, vous devez interagir avec le serveur API. Cela peut être fait via :

* Appels REST
* L'outil en ligne de commande `kubectl`. Vous pouvez trouver des instructions pour l'installer sur votre machine [ici](https://kubernetes.io/docs/tasks/tools/).

Si vous n'avez pas accès à un cluster Kubernetes, je vous suggère d'installer [minikube](https://minikube.sigs.k8s.io/docs/start/) sur votre machine locale pour suivre. Une fois installé et démarré, exécutez la commande suivante pour créer votre premier pod.

```yaml
kubectl run --image=busybox --restart=Never --rm -it -- echo "Bienvenue dans Kubernetes!!"

```

Ce pod sera supprimé automatiquement une fois qu'il aura imprimé son message de bienvenue.

## Comment gérer les clusters dans Kubernetes

La gestion des clusters ne fait pas partie du programme pour devenir CKAD. Pour les besoins de l'examen, vous n'avez pas besoin de savoir comment créer un cluster, gérer des nœuds, etc. 

Et à moins que vous ne prévoyiez de devenir administrateur de cluster, il est probable que vous serez simplement un utilisateur d'une version gérée de Kubernetes dans le cloud, comme GKE sur GCP ou EKS sur AWS.

Cependant, vous devez vous familiariser avec les concepts de namespace, labels et annotations.

### Namespaces

Les namespaces vous permettent de créer des _clusters virtuels_, c'est-à-dire de séparer les ressources dans différentes sections du même cluster physique. Par exemple :

* Pour séparer différents environnements comme le développement, la pré-production, la QA et la production
* Pour décomposer un système complexe en sous-systèmes plus petits. Vous pouvez créer un namespace pour les composants front-end, un autre pour les composants back-end, et ainsi de suite.
* Pour éviter les collisions de noms : la même ressource peut être créée avec le même nom dans différents namespaces. Cela facilite la création de différents environnements (pensez à la pré-production et à la production) qui semblent identiques.

Vous pouvez créer un namespace en exécutant la commande suivante :

```bash
kubectl create ns my-namespace

```

### Quotas de ressources

Si vous souhaitez limiter la quantité de ressources que les développeurs peuvent créer dans un namespace (à la fois les ressources physiques et les objets Kubernetes comme les pods), vous pouvez utiliser [Resource Quotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/).

Par exemple, vous pouvez limiter le nombre de _secrets_ Kubernetes que les utilisateurs peuvent créer sur votre cluster en définissant le `ResourceQuota` suivant :

```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: my-quota
spec:
  hard:
    secrets: "2"

```

dans un fichier – appelons-le `my-quota.yaml` – puis en exécutant `kubectl apply -f my-quota.yaml` ou simplement en exécutant

```bash
kubectl create quota my-quota --hard="secrets=2"

```

Plus d'informations sur les _secrets_ plus tard dans le guide.

### Labels

Les labels vous permettent d'organiser les ressources à l'intérieur de votre cluster Kubernetes. Un label est une paire clé-valeur que vous attachez à une ressource, soit lorsque vous la créez, soit en étiquetant une ressource existante. Vous pouvez ensuite utiliser les labels pour filtrer les ressources. 

Par exemple :

* Vous souhaitez afficher uniquement vos pods `backend`. Vous pouvez attacher le label `tier=backend` aux pods (la clé et la valeur sont arbitraires, vous pouvez utiliser ce que vous voulez) puis exécuter `kubectl get pods -l tier=backend` pour récupérer les pods souhaités.
* Vous souhaitez définir un déploiement ou un service associé à certains pods. La manière de dire au déploiement/service quels pods il doit surveiller est d'utiliser des labels pour les sélectionner.

Voici quelques actions courantes liées aux labels :

```bash
# Étiqueter un pod, mais syntaxe similaire pour les nœuds, etc
kubectl label pods pod-name key=value
# Supprimer un label par nom de pod
kubectl label pods pod-name label_key-

# Supprimer un pod en utilisant le label comme sélecteur
kubectl label po -l app app-

# Afficher les labels
kubectl get pods --show-labels

# Sélectionner des pods en fonction de leurs labels (supposons que nous les avons définis)
kubect get pods -l 'tier in (frontend,backend)'
kubect get pods -l tier=frontend,deployer=coolest-team

```

Les annotations sont similaires aux labels en ce sens qu'elles sont des paires clé-valeur, mais elles ne peuvent pas être utilisées pour sélectionner des ressources. Elles ont un but différent. 

Les annotations sont normalement ajoutées pour être traitées par d'autres outils. Par exemple, si vous exécutez Prometheus pour collecter des métriques, vous pourriez ajouter cette configuration à votre descripteur :

```yaml
metadata:
	labels:
		name: fluentd-elasticsearch
	annotations:
        prometheus.io/scrape: 'true'
        prometheus.io/port: '9102'

```

Cela indique à Prometheus de remplacer les valeurs par défaut pour _scrape_ et _port_ par `true` et `9102` respectivement.

## Au-delà des pods et des déploiements

Comme vous le savez maintenant, un **pod** est l'unité de base dans Kubernetes. Dans la plupart des cas, vous pouvez le considérer comme un conteneur, mais un pod peut être composé de plusieurs conteneurs. Puisque les pods sont éphémères par nature, nous avons besoin d'un mécanisme pour nous assurer que de nouveaux pods sont créés lorsque nos pods existants meurent.

Avec les déploiements, vous pouvez définir un état souhaité, par exemple avoir 3 réplicas de votre application toujours en cours d'exécution. Kubernetes travaillera pour atteindre et maintenir cet état dans le cluster à tout moment. 

Les déploiements peuvent également être utilisés pour gérer facilement le nombre de réplicas en cours d'exécution à tout moment, effectuer des mises à jour progressives, revenir à des versions précédentes, et ainsi de suite.

Cependant, il existe de nombreuses autres charges de travail.

### Pods multi-conteneurs

Un pod peut exécuter plus d'un conteneur. Les conteneurs peuvent communiquer entre eux de manière transparente, car ils sont sur le même réseau et peuvent utiliser des _volumes_ pour partager des données.

Pour l'instant, plongeons dans quelques modèles de conception courants pour les pods multi-conteneurs. Plus tard dans ce guide, nous verrons les volumes en détail et comment déployer certains de ces modèles.

#### Sidecar

Dans ce modèle, nous avons un conteneur qui exécute votre application principale ainsi qu'un autre conteneur qui **exécute des tâches secondaires pour améliorer votre conteneur principal**.

Un exemple classique est l'exécution d'un serveur web (conteneur principal) ainsi qu'un conteneur secondaire qui gère des tâches comme la journalisation, la surveillance, le rafraîchissement des données dans le volume du pod, la terminaison TLS, et ainsi de suite.

#### Adapter

De même, vous pouvez avoir votre conteneur principal et un conteneur secondaire qui **transforme la sortie du conteneur principal**.

Par exemple, imaginez que votre conteneur principal exécute un service qui génère beaucoup de logs complexes. Vous pouvez utiliser un conteneur adaptateur pour simplifier cette sortie avant qu'elle ne soit envoyée à votre service de journalisation, déchargeant ainsi le conteneur principal (et les développeurs du service) de cette tâche.

#### Ambassador

Une autre option courante est d'utiliser un conteneur secondaire **pour agir comme un proxy** entre votre conteneur principal et le monde extérieur.

Par exemple, vous avez probablement différentes bases de données pour différents environnements, comme le test et la production. Lorsque votre conteneur principal a besoin d'une connexion à une base de données, il peut décharger sur le conteneur ambassadeur la tâche de déterminer la base de données appropriée en fonction de l'environnement.

### Services

Les pods peuvent se connecter à d'autres pods en utilisant leurs adresses IP. Cependant, les pods sont éphémères par nature. Lorsqu'ils meurent, en supposant que vous avez un contrôleur de réplication, un nouveau pod sera créé avec une nouvelle adresse IP. Cela rend difficile l'utilisation des IP pour se connecter directement aux pods.

Kubernetes offre une abstraction appelée Service qui crée **une ressource avec une adresse IP fixe** et envoie les requêtes aux pods appropriés. 

Au lieu de se connecter directement aux pods, vous pouvez atteindre leur service via son adresse IP ou mieux encore en utilisant son nom complet grâce au service DNS. De plus, certains types de services exposent votre application en dehors du cluster également.

#### Types de Services

Les principaux types de services que vous pouvez créer sont :

* **ClusterIP** – Pour exposer votre application à l'intérieur du cluster. Il s'agit du service par défaut que Kubernetes crée si vous ne spécifiez pas de type.
* **NodePort** – Il ouvre un port sur chaque nœud du cluster pour exposer vos applications au monde.
* **LoadBalancer** – Expose un service de manière externe en utilisant un équilibreur de charge du fournisseur de cloud.

#### Comment exposer votre application à l'intérieur du cluster

Supposons que vous souhaitiez exposer votre application `my-app` à d'autres nœuds du cluster sur le port 80. Vous pourriez créer un _déploiement_ qui déploie votre application avec cette commande :

```bash
kubectl create deploy my-app --image=my-app --port=80

```

Cela créera des pods qui ne peuvent être accessibles que depuis d'autres ressources à l'intérieur du cluster par leur IP, qui changera si les pods redémarrent.

L'étape suivante consiste à créer un service ClusterIP pour ces pods. La commande suivante crée un service qui peut être atteint sur le port 80 et qui transférera les requêtes à votre application (également sur le port 80).

```bash
kubectl expose deploy my-app --port=80

```

#### Comment exposer votre application à l'extérieur du cluster

Si vous souhaitiez exposer votre application au monde à la place, vous pourriez utiliser cette configuration pour créer un service NodePort :

```yaml
kind: Service
apiVersion: v1
metadata:
	name: my-svc
spec:
    type: NodePort
    selector:
	    app: nginx
    ports:
    - protocol: TCP
    	port: 80 # Le port où vous pouvez atteindre ce service
    	targetPort: 80 # Le port que vous avez ouvert dans le pod

```

### [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/)

Les services ne sont pas le seul moyen d'exposer vos applications au monde. Vous pouvez également utiliser un **objet Ingress** comme point d'entrée pour votre cluster. 

En plus de cela, vous avez besoin d'un **Ingress Controller**, comme Nginx, pour implémenter les règles définies dans l'objet Ingress.

Puisque les ingresses ne font pas partie du programme CKAD, nous passerons à d'autres sujets.

### [Jobs](https://kubernetes.io/docs/concepts/workloads/controllers/job/)

Un Job créera un ou plusieurs pods qui **ne seront pas redémarrés s'ils se terminent avec succès**. Vous pouvez les utiliser pour effectuer des travaux par lots, c'est-à-dire des **tâches ponctuelles** comme effectuer un calcul, sauvegarder certains fichiers, transformer et exporter certaines données, et ainsi de suite.

Sauf indication contraire, le pod s'exécutera une fois. Vous pouvez spécifier combien de fois un job doit être exécuté pour être considéré comme COMPLETÉ, en utilisant le paramètre `completions`. Par défaut, les pods s'exécuteront séquentiellement, mais vous pouvez configurer le Job pour qu'ils s'exécutent en parallèle.

En cas de non-réalisation, vous pouvez les configurer pour qu'ils ne redémarrent **jamais** (réessayer) ou pour qu'ils redémarrent **OnFailure** jusqu'à `backoffLimit` fois avant que Kubernetes ne considère que le job a échoué.

Voici comment créer un job simple depuis la ligne de commande :

```bash
 kubectl create job my-job --image=busybox -- echo "Hello World"

```

Si le job s'est exécuté avec succès, son état sera COMPLETÉ et ses pods ne seront pas supprimés afin que vous puissiez accéder à leurs logs. Vous pouvez les voir en utilisant :

```bash
kubectll get pods --show-all

```

puisqu'ils ne seront pas visibles par défaut dans la liste des pods après 2 minutes.

### [Cronjobs](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/)

Kubernetes offre des Cronjobs pour créer des jobs qui doivent s'exécuter périodiquement ou à un moment spécifique dans le futur : tâches de nettoyage et de sauvegarde périodiques, renouvellement des certificats TLS, et ainsi de suite.

Kubernetes fera de son mieux pour exécuter un seul Job pour effectuer la tâche que vous avez spécifiée dans la configuration du Cronjob. Cependant, il existe 3 problèmes courants dont vous devez être conscient :

* Il n'est pas garanti que le job s'exécutera **exactement au moment souhaité**. Imaginez que vous avez besoin que votre job s'exécute à 09:00:00. Vous pouvez définir la propriété `startingDeadlineSeconds` à X secondes afin que, si le job n'a pas démarré à 09:00:00 + X secondes, il sera marqué comme échoué et ne s'exécutera pas.
* **2 Jobs peuvent être planifiés en même temps** pour effectuer la tâche. Dans ce cas, vous devez vous assurer que les tâches sont _idempotentes_, c'est-à-dire que le résultat de l'exécution de la tâche ne changera pas si la tâche est effectuée plusieurs fois.
* **Aucun job peut être planifié**. Pour surmonter ce problème, assurez-vous que le Cronjob récupère tout travail non fait par l'exécution précédente.

Voici comment créer un cronjob simple qui imprime "Hello World" chaque minute :

```bash
kubectl create cronjob my-job --image=busybox --schedule="*/1 * * * *" -- echo "Hello World"

```

Je recommande ce [site web](https://crontab.guru/) pour obtenir vos expressions de planification cron correctes.

Les 3 ressources suivantes ne font pas partie de l'examen CKAD, mais je pense que vous devriez avoir une compréhension de base d'elles au moins.

### [Daemon sets](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/)

Les Daemon sets garantissent qu'un pod est planifié sur chaque **nœud** de votre cluster. En plus de cela, le pod est toujours en cours d'exécution : s'il meurt ou si quelqu'un le supprime, le pod sera recréé.

Un cas d'utilisation courant pour les Daemon sets est de collecter les logs et les métriques qui proviennent de chaque nœud. Mais même si vous n'en créez aucun, il y a déjà des daemon sets en cours d'exécution dans votre cluster : Kubernetes crée un daemon set pour exécuter un composant appelé `kube-proxy` sur chaque nœud !

Si vous retirez un nœud du cluster, Kubernetes ne recréera pas son daemon sur un autre nœud, car ce nœud exécutera déjà le daemon set. Si vous ajoutez un nouveau nœud au cluster, il exécutera automatiquement le daemon set.

### [Stateful set](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)

Jusqu'à présent, nous avons vu des outils pour déployer des applications sans état ou des pods qui ont leur propre stockage persistant qui leur survivra. Pour déployer des applications avec état, vous pouvez utiliser des stateful sets.

Puisque cela ne fait pas partie de l'examen CKAD, nous n'entrerons pas dans plus de détails.

### [Static pods](https://kubernetes.io/docs/tasks/configure-pod-container/static-pod/)

Les pods statiques sont des pods gérés par `kubelet`, et non par l'API Kubernetes.

Pour les créer, vous devez simplement créer un fichier de configuration de pod régulier et configurer kubelet pour analyser ce répertoire. Après avoir redémarré `kubelet`, il créera le pod et le redémarrera s'il échoue.

Kubernetes créera un pod miroir, c'est-à-dire une copie du pod dans le serveur API Kubernetes. Vous pouvez voir que ce pod apparaît lorsque vous exécutez `kubectl get pods`, mais si vous essayez de le supprimer en utilisant `kubectl delete podName`, il apparaîtra immédiatement dans la liste des pods, créé par le `kubelet` qui s'exécute sur le nœud où vous avez créé le pod statique.

## Comment configurer les pods et les conteneurs

Nous venons de voir différentes charges de travail que vous pouvez déployer sur votre cluster Kubernetes. Passons maintenant un peu de temps à apprendre comment configurer les pods et les conteneurs qui exécutent ces charges de travail.

### [Init Containers](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-initialization/)

Vous pouvez utiliser des _init containers_ pour définir l'état initial de votre pod : en écrivant certaines données dans le volume du pod, en téléchargeant certains fichiers, et ainsi de suite.

Vous pouvez définir un ou plusieurs init containers pour le même pod. Ils seront exécutés séquentiellement et le pod ne commencera à s'exécuter qu'après que tous les conteneurs soient terminés. Par conséquent, les init containers peuvent également être utilisés pour faire attendre le pod jusqu'à ce qu'une certaine condition soit remplie avant qu'il ne soit exécuté. 

Par exemple, vous pouvez faire attendre un pod jusqu'à ce qu'un autre service soit opérationnel avant qu'il ne puisse démarrer.

Vous pouvez définir un init container en ajoutant quelque chose comme ceci sous la section `spec` de votre description de pod :

```yaml
spec:
  initContainers:
  - name: init-myservice
    image: busybox:1.28
    command: ['sh', '-c', "until nslookup myservice.$(cat /var/run/secrets/kubernetes.io/serviceaccount/namespace).svc.cluster.local; do echo waiting for myservice; sleep 2; done"]
 ...

```

### [ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/)

Garder la configuration de votre application séparée du code source est une pratique que vous devriez suivre. Les ConfigMaps vous permettent de faire cela dans Kubernetes.

Les ConfigMaps sont utilisés pour **stocker des paires clé-valeur de données non confidentielles**. Nous verrons comment stocker des données confidentielles (par exemple, des mots de passe) dans les _Secrets_ dans la section suivante.

Vous pouvez créer un ConfigMap depuis la ligne de commande :

```bash
# Passer les valeurs en tant qu'arguments
kubectl create configmap my-map --from-literal=db_url=my-url --from-literal=username=username

# Passer les valeurs depuis un fichier
kubectl create configmap another-map --from-file=my-file

```

Une fois créé, votre application peut l'utiliser dans un pod qui se trouve dans le même namespace de plusieurs manières :

* En tant qu'arguments de ligne de commande
* En tant que variables d'environnement
* Depuis un fichier dans un volume en lecture seule

Voyons une définition de pod qui lit des valeurs depuis un ConfigMap en utilisant ces approches :

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  restartPolicy: Never
  containers:
    - name: busybox
      image: busybox
      args:
        - /bin/sh
        - -c
        - "echo $MY_VARIABLE" # Cette valeur provient du configmap
      env:
      - name: MY_VARIABLE
        valueFrom:
          configMapKeyRef:
            name: another-map           
            key: my-key # Pour charger des clés individuelles depuis une map
      envFrom:
      - configMapRef:
          name: another-map # Pour importer toutes les valeurs d'une map en tant que variables d'environnement
      volumeMounts:
      - name: config
        mountPath: "/config" # Cela contiendra des fichiers avec les données stockées dans my-map
        readOnly: true
  volumes:
    # Nom pour faire référence à ce volume dans le pod
    - name: config
      configMap:
        # Nom du ConfigMap
        name: my-map

```

### [Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

Les Secrets sont très similaires aux ConfigMaps, mais vous les utilisez pour stocker des **données confidentielles**. La création et la gestion des secrets est un sujet sensible. Assurez-vous de lire la documentation. Ici, nous verrons les bases.

La manière la plus simple de créer un secret est :

```bash
#Pour créer un secret à partir d'un littéral
kubectl create secret generic secret-name --from-literal=password=password
#Pour créer un secret à partir du contenu d'un fichier
kubectl create secret generic secret-name --from-file=path-to-file

```

Ensuite, vous pouvez monter vos secrets dans le pod en tant que variables d'environnement ou fichiers :

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: another-pod
spec:
  restartPolicy: Never
  containers:
    - name: busybox
      image: busybox
      args:
        - /bin/sh
        - -c
        - "echo $MY_VARIABLE"
      env:
      - name: MY_VARIABLE
        valueFrom:
          secretKeyRef:
            name: my-secret2
            key: username # Pour charger des clés individuelles depuis une map
      envFrom:
      - secretRef:
          name: yet-another-secret # Pour importer toutes les valeurs d'une map en tant que variables d'environnement
      volumeMounts:
      - name: secret-volume
        mountPath: "/secrets" # Cela contiendra des fichiers avec les données stockées dans my-map
        readOnly: true
  volumes:
    # Nom pour faire référence à ce volume dans le pod
    - name: secret-volume
      secret:
        # Nom du Secret
        secretName: my-secret

```

### [Probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)

Les Probes vous permettent de définir des règles pour décider si un pod est en bonne santé, s'il est prêt à servir du trafic et s'il est prêt à démarrer. À la fin de cette section, je présenterai un descripteur d'exemple avec certaines de ces sondes.

#### Sondes de vivacité

Kubernetes redémarrera automatiquement les _conteneurs plantés_. Cependant, cela ne tiendra pas compte des situations comme les bugs (imaginez une boucle infinie dans votre application), les interblocages, et ainsi de suite. Vous pouvez définir des sondes de vivacité pour **détecter si votre application est en bonne santé**. Kubernetes utilise cette sonde pour décider s'il doit redémarrer le conteneur.

Il existe trois types de sondes de vivacité que vous pouvez définir :

* HTTP Get, où vous définissez un endpoint dans votre application (par exemple /health) que Kubernetes peut appeler pour déterminer si l'application est en bonne santé.
* Sonde de socket TCP, qui tente d'établir une connexion TCP à un port spécifique. Si la connexion ne peut pas être établie, l'application est redémarrée.
* Sonde Exec, qui exécute une commande à l'intérieur du conteneur et le redémarre si le code de statut de sortie est différent de 0.

#### Sondes de préparation

Imaginez un service qui doit charger un fichier de configuration volumineux lors du démarrage. Le conteneur lui-même peut être en bonne santé (ceci peut être vérifié en utilisant les sondes de vivacité décrites ci-dessus) mais pas prêt à commencer à accepter des requêtes. 

Kubernetes utilise des sondes de préparation pour déterminer si votre application est prête à commencer à servir du trafic.

De nombreuses idées discutées pour les sondes de vivacité s'appliquent également aux sondes de préparation :

* Elles peuvent être configurées avec un délai initial, un délai d'attente, un seuil, une période, etc.
* Elles peuvent être basées sur des appels HTTP get, des connexions de socket TCP, ou l'exécution de commandes à l'intérieur du conteneur

Cependant, tandis que les sondes de vivacité indiquent à Kubernetes de redémarrer le conteneur s'il n'est pas en bonne santé, les sondes de préparation sont utilisées pour retirer le conteneur du pool de conteneurs qui peuvent accepter des requêtes. Une fois que le conteneur est prêt, il peut commencer à servir des requêtes.

#### Sondes de démarrage

Les sondes de démarrage sont utilisées uniquement pendant le démarrage, par exemple pour les applications qui sont lentes à démarrer. Si la sonde de démarrage réussit, les sondes de vivacité et de préparation (si configurées) commenceront à s'exécuter périodiquement.

### Exemple

Ce pod va exécuter les commandes suivantes :

* sleep 20
* touch /tmp/healthy
* sleep 30
* rm -rf /tmp/healthy
* sleep 600

Les paramètres les plus basiques dont vous devez être conscient lors de la configuration de vos sondes sont :

* **initialDelaySeconds** avant de commencer à sonder
* **periodSeconds** pour définir la fréquence de la sonde
* **timeoutSeconds** après lequel la sonde expire
* **failureThreshold** pour déterminer le nombre d'essais après lequel Kubernetes abandonne

Avec notre configuration, les sondes commenceront 10 secondes après la création du pod. Pendant les 20 premières secondes, le fichier `/tmp/healthy` n'existe pas. Par conséquent, la sonde de préparation échouera. Nous créerons ensuite ce fichier et pendant les 30 secondes suivantes, la sonde de préparation réussira, jusqu'à ce que nous supprimions à nouveau le fichier.

La sonde de vivacité est une simple commande `echo "I'm healthy"`. Si elle peut être exécutée, le pod est en bonne santé. Sinon, il doit être redémarré.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
  - args:
    - /bin/sh
    - -c
    - "sleep 20; touch /tmp/healthy; sleep 30; rm -rf /tmp/healthy; sleep 600"
    image: busybox
    name: tmp
    livenessProbe:
     exec: # Si cette commande peut être exécutée, le pod est en bonne santé
       command:
       - echo
       - "I'm healthy"
     initialDelaySeconds: 5 # Ne commencer à sonder qu'après 5 secondes
     periodSeconds: 5 # Sonder toutes les 5 secondes
    readinessProbe:
     exec: # Si cette commande peut être exécutée, le pod est prêt à servir du trafic
       command:
       - cat
       - /tmp/healthy
     initialDelaySeconds: 5 # Ne commencer à sonder qu'après 5 secondes
     periodSeconds: 10 # Sonder toutes les 10 secondes
  dnsPolicy: ClusterFirst
  restartPolicy: Never
status: {}

```

Exécutez cette commande pour voir le pod passer par ces états :

```bash
kubectl get pods --watch

```

Voyez comment la colonne `Ready` passe de `0/1`, à `1/1` et retourne à `0/1` ?

Exécutez cette commande pour obtenir une liste d'événements et voir comment les sondes ont échoué, comme nous nous y attendions.

```bash
kubectl describe pods my-pod

```

### [Ressources des conteneurs](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)

Lorsque vous créez un pod, vous pouvez définir :

* La quantité minimale de ressources dont il a besoin pour fonctionner, connue sous le nom de _requests_.
* La quantité maximale de ressources que le pod doit utiliser, connue sous le nom de _limits_.

Kubernetes prendra en compte les ressources que vous avez demandées lorsqu'il essaiera de planifier le pod. Il ne planifiera pas le pod sur un nœud qui n'a pas assez de capacité, indépendamment de la consommation actuelle des ressources. 

Par exemple, si les pods A et B s'exécutent sur le nœud N, Kubernetes calculera si le nouveau pod C peut s'adapter à N en faisant quelque chose comme :

`Capacité totale de N - (ressources demandées par A + ressources demandées par B) <= ressources demandées par C`

Même si les pods A et B n'utilisent pas toutes les ressources qu'ils ont demandées, Kubernetes a **promis** qu'ils auraient ces ressources disponibles sur ce pod. C'est pourquoi l'utilisation actuelle des ressources ne fait pas partie de la formule précédente.

Si un pod dépasse ses limites de ressources, deux choses peuvent se produire :

* S'il dépasse ses limites de CPU, il sera limité
* S'il dépasse ses limites de mémoire, il sera redémarré

Créons maintenant un pod qui demande de la mémoire et du CPU et limite les ressources qu'il est autorisé à utiliser :

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: resource-limited-pod
spec:
  restartPolicy: Never
  containers:
    - name: busybox
      image: busybox
      args:
        - /bin/sh
        - -c
        - "echo Hello Kubernetes; sleep 3600"
      resources:
        requests:
          memory: "300Mi"
          cpu: 0.2
        limits:
          memory: "1Gi"
          cpu: 0.5

```

En tant qu'exercice, définissez des valeurs ridiculement élevées pour la mémoire demandée (et/ou le CPU) et _essayez_ de créer le pod. Vous verrez que le pod ne devient jamais prêt. La sortie de

```bash
kubectl describe pods resource-limited-pod

```

vous dira pourquoi.

## [Comment planifier les pods dans Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node) 

Cette section ne fait pas partie du programme de l'examen CKAD. Mais je pense que vous devriez avoir au moins une compréhension de base des concepts que je vais exposer ici car ils sont susceptibles de se poser lorsque vous travaillez avec Kubernetes.

Kubernetes vous permet de spécifier sur quels nœuds vous souhaitez que vos pods soient planifiés via plusieurs mécanismes. 

Le plus simple est d'utiliser le champ **nodeSelector** pour choisir un nœud en fonction d'un label. Cependant, d'autres fonctionnalités ont été introduites pour permettre des configurations plus complexes.

### [Taints et tolérations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/)

Vous pouvez **taint un nœud pour empêcher les pods d'être planifiés sur celui-ci**, sans modifier les pods eux-mêmes. Lorsque vous taint un nœud, les seuls pods que Kubernetes planifiera sur ce nœud seront les pods qui **tolèrent** ce taint.

Vous pouvez voir cela en action si vous exécutez :

```bash
kubectl describe node master.Kubernetes

```

Dans la sortie de la commande précédente, vous verrez la ligne :

```bash
Taints: node-role.kubernetes.io/master:NoSchedule

```

Ce taint empêche les pods d'être planifiés sur le nœud maître (sauf si les pods tolèrent ce taint).

Il existe trois types de taint :

* NoSchedule : Kubernetes ne planifiera pas les pods sur un nœud s'ils ne peuvent pas tolérer le taint.
* PreferNoSchedule : les pods qui ne tolèrent pas le taint ne seront pas planifiés sur un nœud sauf s'ils ne peuvent pas être planifiés ailleurs.
* NoExecute : si les pods _déjà en cours d'exécution sur le nœud_ ne peuvent pas tolérer le taint, les expulser du nœud.

**Les taints ne garantissent pas que les pods seront planifiés sur des nœuds spécifiques**. Pour y parvenir, vous avez besoin du concept de _Node affinity_ que nous allons explorer maintenant.

### Node affinity

Node affinity indique à Kubernetes de **planifier les pods sur des nœuds spécifiques**.

Imaginez que vous avez un service S qui nécessite un matériel spécial pour fonctionner. Vous souhaitez dédier le matériel à ce service et ne voulez que les pods de S s'exécutent sur celui-ci. Comment pouvez-vous y parvenir ?

Vous pouvez taint les nœuds qui ont ce type d'équipement afin que seuls les pods du service S puissent être planifiés sur ces nœuds. Cependant, Kubernetes peut toujours déployer ces pods sur d'autres nœuds qui n'ont pas le matériel requis.

Nous pouvons voir comment la combinaison de taints et de node affinity garantit que seuls les pods du service S s'exécutent dans nos nœuds spécialisés :

* Node affinity planifie les pods de S dans les nœuds spécialisés (et nulle part ailleurs).
* Les taints garantissent qu'aucun autre pod ne sera planifié dans les nœuds spécialisés, seuls les pods du service S.

## Stockage dans Kubernetes

Par défaut, lorsque le conteneur à l'intérieur d'un pod redémarre, toutes les données à l'intérieur du conteneur sont perdues. C'est par conception. 

Si vous souhaitez que les données survivent au conteneur, au pod, et même au nœud, vous devez utiliser des **volumes**. De plus, si un pod est composé de plusieurs conteneurs, alors les volumes du pod peuvent être utilisés par tous les conteneurs.

### [Volumes](https://kubernetes.io/docs/concepts/storage/volumes/)

Après avoir défini le volume, au niveau du pod, vous devez le monter dans chaque conteneur qui a besoin d'y accéder.

Il existe de nombreux types de volumes pour répondre à différents cas d'utilisation (généralement, en fonction de ce que vous voulez qu'il se passe lorsque le _pod_ est détruit). Certains types courants de volumes sont :

* emptyDir : crée un répertoire qui est initialement vide. Moyens faciles de partager des fichiers entre différents conteneurs dans un pod.
* hostPath : monte un fichier ou un répertoire du système de fichiers du nœud dans le pod. Après la suppression du pod, les fichiers resteront sur l'hôte.
* Volumes qui vivent sur les clouds AWS, GCP ou Azure.

Pour plus d'informations sur ces types de volumes et d'autres, consultez la documentation.

Pour monter un volume dans un conteneur, votre descripteur de pod (appelons ce fichier `with-mounted-volume.yaml`) devrait ressembler à ceci :

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: with-mounted-volume
spec:
  volumes: # Les volumes sont définis au niveau du pod
  - name: my-volume # Nous utiliserons ce nom pour monter le volume à l'intérieur du pod
    hostPath: # Ici nous définissons le type de volume que nous voulons
      path: /var/my-k8s-volume
  containers:
  - args:
    - /bin/sh
    - -c
    - "sleep 3600"
    image: busybox
    name: bb
    volumeMounts:
    - name: my-volume
      mountPath: /tmp/my-volume-path
  restartPolicy: Never

```

Puisque nous avons créé un volume `hostPath`, son contenu survivra au pod. Testons cela :

```bash
# Créer un pod
kubectl apply -f with-mounted-volume.yaml
# Créer un fichier à l'emplacement monté
kubectl exec -it with-mounted-volume -- sh -c "echo 'Inside the pod' > /tmp/my-volume-path/newfile"
# Essayer de lire le fichier
kubectl exec -it with-mounted-volume -- cat /tmp/my-volume-path/newfile
# Supprimer le pod
kubectl delete pods with-mounted-volume
# Créer un nouveau pod
kubectl apply -f with-mounted-volume.yaml
# Explorer le contenu de `/tmp/my-volume-path` pour voir s'il a persisté
kubectl exec -it with-mounted-volume -- cat /tmp/my-volume-path/newfile

```

#### Revisiter les pods multi-conteneurs

Maintenant que nous sommes familiers avec les volumes, créons un pod multi-conteneurs qui utilisera un volume monté pour partager des données entre les conteneurs.

* Notre descripteur de pod s'appellera `communicating-containers.yaml`
* Nous aurons un pod avec 2 conteneurs `busybox`.
* L'un d'eux ajoutera `Hello World` à un fichier chaque seconde.
* L'autre conteneur a accès au contenu de ce fichier (et à tout ce qui est placé dans ce volume partagé). Nous allons suivre le fichier partagé et voir comment l'autre conteneur ajoute `Hello World` à celui-ci.

Voici la définition de notre pod :

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: communicating-containers
spec:
  volumes:
  - name: vol
    emptyDir: {}
  containers:
  - args:
    - sh
    - -c
    - "while true;do echo 'Hello World' >> /etc/shared/log; sleep 1; done"
    image: busybox
    name: container-1
    volumeMounts:
    - name: vol
      mountPath: /etc/shared/ # Le conteneur peut accéder au volume ici
  - args:
    - sh
    - -c
    - "sleep 3600"
    image: busybox
    name: container-2
    volumeMounts:
    - name: vol
      mountPath: /etc/a-different-location # Le volume peut être monté à différents emplacements sur chaque conteneur
  restartPolicy: Never

```

Créons le pod :

```bash
kubectl apply -f communicating-containers.yaml

```

Une fois le pod en cours d'exécution, nous pouvons suivre le fichier depuis `container-2` :

```bash
kubectl exec -it communicating-containers -c container-2 -- tail -f /etc/a-different-location/log

```

Bien que ce soit `container-1` qui écrit dans `log`, puisque c'est dans un volume partagé, `container-2` peut voir ce fichier aussi.

### [Volumes persistants](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)

Les volumes persistants (PV) et les revendications de volumes persistants (PVC) découplent les pods de la technologie de stockage. Les PV sont créés par les administrateurs de cluster ou dynamiquement en fonction des [classes de stockage](https://kubernetes.io/docs/concepts/storage/storage-classes/). 

Contrairement aux volumes que nous avons créés précédemment, définis au niveau du pod, les PV ont leur propre cycle de vie, indépendant de tout pod.

Après avoir créé des PV, les _utilisateurs_ peuvent créer des revendications de volumes persistants pour obtenir le stockage dont ils ont besoin, _sans avoir besoin de se soucier de l'infrastructure réelle qui soutient leur stockage_.

#### Exemple

Tout d'abord, nous définissons un volume persistant dans pv.yaml :

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: myvolume
spec:
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce
    - ReadWriteMany
  storageClassName: normal
  hostPath:
    path: /etc/foo

```

Pour la revendication de volume persistant, voici le descripteur (dans pvc.yaml) :

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mypvc
spec:
  storageClassName: normal
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 4Gi

```

Maintenant, créons les ressources dans notre cluster

```bash
# D'abord, le volume persistant
kubectl apply -f pv.yaml
# Ensuite, la revendication de volume persistant
kubectl apply -f pvc.yaml

```

Nous pouvons prendre la définition de pod de l'exemple précédent et avec une petite modification commencer à utiliser ce volume persistant au lieu du hostPath que nous avions défini. C'est la seule chose que nous devons changer :

```yaml
volumes:
  - name: mypd # Pour faire référence à ce volume lorsque nous configurons le pod
    persistentVolumeClaim: # Au lieu de hostPath
      claimName: mypvc # Le nom de la pvc que nous venons de créer

```

## Réseau et sécurité dans Kubernetes

En ce qui concerne la sécurité, ces concepts sont le minimum que vous devriez connaître pour pouvoir réussir l'examen CKAD.

### [Politiques de réseau](https://kubernetes.io/docs/concepts/services-networking/network-policies/)

Par défaut, tout le trafic entrant (c'est-à-dire le trafic circulant vers votre application) et le trafic sortant (c'est-à-dire le trafic circulant depuis votre application) est autorisé. Tout pod peut se connecter à tout autre pod, même s'ils sont dans des namespaces différents.

Vous pouvez définir des politiques de réseau pour contrôler le trafic entrant et sortant en fonction de différents critères.

Pour illustrer cela, créons une politique de réseau qui permet le trafic vers notre base de données uniquement depuis les pods avec le label `access: allowed` :

```yaml
kind: NetworkPolicy
apiVersion: networking.k8s.io/v1
metadata:
  name: access-db-policy # choisissez un nom
spec:
  podSelector:
    matchLabels:
      app: db # sélecteur pour les pods de la base de données
  ingress: # autoriser le trafic entrant
  - from:
    - podSelector: 
        matchLabels: 
          access: allowed # Seuls les pods avec ce label pourront envoyer du trafic à la base de données

```

### [Contexte de sécurité](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)

Lors de la configuration d'un contexte de sécurité, vous pouvez activer des fonctionnalités de sécurité comme empêcher le conteneur de s'exécuter en tant que root, choisir en tant qu'utilisateur le pod s'exécute, et ainsi de suite. Voici un exemple :

```bash
spec:
  securityContext:
    runAsUser: 1000 # Cela définit l'utilisateur pour chaque conteneur dans ce pod, mais peut être remplacé
  containers:
  - name: my-container
     image: alpine
     securityContext:
     	runAsUser: 1001 # Cela remplace l'utilisateur défini au niveau du pod     	
  - name: another-container
	....

```

### [Comptes de service](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)

Vos applications peuvent se connecter au serveur API et interagir avec lui. Par exemple, pour récupérer des informations sur les pods dans un namespace. Les comptes de service permettent aux applications de s'_authentifier_ auprès du serveur API afin qu'elles puissent opérer sur celui-ci.

Il existe un _compte de service par défaut_, mais ce n'est pas une bonne pratique que tous les pods l'utilisent puisque toutes les applications n'ont pas besoin de pouvoir effectuer les mêmes opérations sur le serveur API.

La manière la plus simple de créer un compte de service est via la ligne de commande :

```bash
kubectl create serviceaccount my-sa

```

Une fois créé, vous pouvez l'assigner à un pod en utilisant le champ `serviceAccountName` dans le descripteur de pod :

```bash
spec:
  serviceAccountName: my-sa
  containers:
  - name: web-server
  ...

```

Une fois l'application authentifiée, l'étape suivante consiste à voir si elle dispose des autorisations appropriées pour l'action qu'elle tente d'accomplir, c'est-à-dire à voir si l'application est _autorisée_.

### [Contrôle d'accès basé sur les rôles](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)

Une méthode courante pour gérer l'autorisation est le **Contrôle d'accès basé sur les rôles (RBAC)**. Les comptes de service sont liés à un ou plusieurs rôles. Chaque rôle a des autorisations pour effectuer une action spécifique sur une certaine ressource.

L'autorisation RBAC est définie en deux étapes séparées :

* Création de rôle, en utilisant les ressources Role et ClusterRole, pour spécifier les actions qui peuvent être effectuées sur certaines ressources
* La liaison des rôles aux comptes, en utilisant les ressources RoleBinding et ClusterRoleBinding.

Comme vous pouvez l'imaginer, les ressources qui contiennent le préfixe Cluster sont disponibles dans tout le cluster, tandis que les autres ne sont définies que dans un namespace particulier.

Puisque cela ne fait pas partie de l'examen CKAD, nous n'entrerons pas dans les détails de la création et de la configuration de RBAC dans votre cluster.

## Observabilité et débogage dans Kubernetes

Une fois que vous avez déployé vos applications, comment savez-vous ce qui se passe dans votre cluster ?

Nous avons déjà introduit les Probes comme un mécanisme pour décider si les pods doivent être redémarrés et si les pods sont prêts à servir du trafic. Ici, nous verrons d'autres mécanismes pour mieux comprendre l'état de notre cluster et résoudre les problèmes.

#### Obtenir des informations de base sur les pods

Pour accéder à l'état actuel des pods, il y a deux options de base. En voici la première :

```bash
kubect get pods

```

Cela vous montrera le `STATUS`, l'`AGE`, le nombre de `RESTARTS` et combien de conteneurs à l'intérieur des pods sont `READY`. Vous pouvez passer des flags à cette commande pour qu'elle affiche l'adresse IP des pods, les labels, et plus encore.

La deuxième option fournit des informations plus détaillées :

```bash
kubectl describe pods my-pod

```

Tout en bas de la sortie de cette commande, vous trouverez une liste d'événements qui vous donneront des indices en cas de problème :

* Les sondes de vivacité/prêt à l'emploi échouent
* Il y a eu une erreur lors de la récupération d'une image
* Mémoire insuffisante pour planifier un pod

Et ainsi de suite.

### Comment obtenir les logs d'un conteneur

Si un pod est en cours d'exécution, vous pouvez accéder à ses logs en utilisant la commande suivante :

```bash
kubectl logs pod-name [-c container-name] [-n namespace]

```

Vous n'avez besoin de passer le nom du conteneur que s'il y a plus d'un conteneur dans votre pod. De même, le flag namespace n'est nécessaire que pour récupérer les logs des pods dans un namespace différent.

Vous pouvez même suivre les logs avec le flag `-f` :

```
kubectl logs -f pod-name [-c container-name] [-n namespace]

```

Cela sera suffisant pour la certification. Cependant, vérifier manuellement les logs est fastidieux et inefficace dans un environnement de production réel. Vous voudrez utiliser d'autres technologies pour gérer vos logs ou des services comme StackDriver si vous êtes sur GCP. Si vous souhaitez en savoir plus sur StackDriver et GCP en général, assurez-vous de consulter mon [guide GCP](https://www.freecodecamp.org/news/google-cloud-platform-from-zero-to-hero/).

### Conseils de dépannage

Bien qu'il n'existe pas de solutions universelles en matière de dépannage, il est généralement bon de commencer au niveau du pod pour avoir une idée de ce qui pourrait être la cause racine du problème.

Vos outils de base devraient être les commandes que nous avons couvertes ci-dessus. En plus de cela, vous pouvez toujours ouvrir un terminal à l'intérieur du pod :

```bash
# En supposant que votre image de conteneur utilise sh
kubectl exec -it my-pod -c container -n namespace -- sh

```

Il n'est **pas recommandé** de résoudre les problèmes à l'intérieur du pod de cette manière, car par conception les pods sont éphémères et après leur redémarrage, vos modifications seront perdues et le problème se manifestera à nouveau. Cependant, c'est une bonne idée de bien comprendre le problème.

Pour récupérer vos métriques de pod ou de nœud, vous pouvez exécuter la commande suivante :

```bash
kubectl top pod pod-name

```

Ces outils devraient vous aider à résoudre les problèmes les plus courants dans vos opérations quotidiennes. Il y a trop de choses qui peuvent mal tourner pour tout couvrir ici. Si vous êtes confronté à quelque chose que vous ne pouvez pas corriger, je vous recommande de visiter cette entrée pour obtenir de l'aide [déboguer vos applications.](https://kubernetes.io/docs/tasks/debug-application-cluster/debug-application/)

## Conseils et astuces

Ce sont quelques "astuces" que j'ai trouvées utiles dans mon travail quotidien avec Kubernetes et surtout pour passer l'examen CKAD. **L'examen est une question de vitesse et d'efficacité**. Avec cela à l'esprit, voyons ce que nous pouvons faire pour performer mieux.

### Définir des alias

Vous allez taper les mêmes commandes encore et encore. Dès que vous commencez l'examen, créez les alias suivants :

```bash
# Alias essentiels. Je recommande fortement de les définir
alias k='kubectl'
alias kg='k get'
alias kgpo='k get pods'
alias kdpo='k describe pod'
alias kd='k describe'

# J'ai également trouvé celui-ci très utile
alias kap='k apply -f'

# Je n'ai cela que pour le travail
alias kgpoa='kgpo --all-namespaces'
alias kgpol='kgpo --show-labels'
alias kgpow='kgpo -o wide'
alias kgd='kg deploy'
alias kgs='kg svc'
alias kdd='kd deploy'
alias kds='kd svc'

```

### Rechercher dans l'historique des commandes plus rapidement

J'ai vu beaucoup d'ingénieurs, dont beaucoup de seniors, frapper maladroitement la touche flèche vers le haut 20 fois pour trouver quelque chose dans leur historique de commandes.

Au lieu de cela, assurez-vous d'être à l'aise avec `Ctrl + r`. Il suffit de l'appuyer et de commencer à taper une partie de la commande que vous recherchez. Ensuite, continuez à appuyer sur `Ctrl + r` jusqu'à ce que vous la trouviez. Maintenant, vous pouvez appuyer sur `Entrée` pour l'exécuter ou simplement commencer à taper pour la modifier.

C'est un énorme gain de temps dont tout le monde n'est pas conscient.

### Familiarisez-vous avec la documentation

Vous pouvez consulter la documentation pendant l'examen. Cependant, ce n'est pas le moment d'apprendre de nouvelles choses. Visitez la documentation pour obtenir des modèles pour yaml, vérifier des paramètres spécifiques, et ainsi de suite.

Assurez-vous d'avoir une bonne idée de la **structure de la documentation** et de l'endroit où trouver les choses. Utilisez la **fonctionnalité de recherche** pour aller encore plus vite.

Enfin, cette [feuille de triche Kubectl](https://kubernetes.io/docs/reference/kubectl/cheatsheet/) est en or et **sera disponible pour vous pendant l'examen**.

### Vous n'avez pas besoin de tout mémoriser

En plus de la documentation, `kubectl` a un flag `--help` pour la plupart des commandes (`-h` est la version courte). La plupart du temps, vous trouverez la réponse à votre question là.

En fait, je recommande de faire cela avant d'aller à la documentation, car c'est beaucoup plus rapide.

Imaginez que vous souhaitez créer un objet quota de ressources. Vous ne vous souvenez pas du yaml que vous devez écrire ou de la commande pour le créer. Cependant, vous connaissez la `commande kubectl` et le flag `--help`. Ensuite, vous devriez essayer ceci avant d'aller à la documentation :

```bash
# À partir de cela, nous pouvons obtenir ce dont nous avons besoin pour créer notre objet quota de ressources
kubeclt create quota -h
# Par exemple
kubeclt create quota my-quota --hard="secrets=2"

```

Vous avez de nombreuses sources d'information et donc vous n'avez pas besoin de mémoriser de nombreuses commandes ou des descripteurs.

Cependant, étant donné que le temps est très limité pendant l'examen, je pense qu'il vaut la peine de connaître certaines des commandes suivantes par cœur et comment les utiliser.

### Générer une spécification de pod de base rapidement

**Ceci est extrêmement important**. Au lieu de copier et coller depuis la documentation chaque fois que vous avez besoin d'un pod, utilisez la commande suivante pour obtenir un descripteur que vous pouvez modifier plus tard pour répondre à vos exigences :

```bash
# Exécuter le pod nginx et écrire sa spécification dans un fichier appelé pod.yaml
kubectl run nginx --image=nginx --restart=Never --dry-run=client -o yaml > pod.yaml
# Certains de ces flags peuvent être utiles, selon le problème
kubectl run nginx --image=nginx --restart=Never  --port=80 --labels=key=val --dry-run=client -o yaml > pod.yaml

```

Autres paramètres utiles :

```bash
--rm # pour supprimer le pod dès qu'il est terminé
-it # Entrer dans le terminal interactif, pour exécuter des commandes directement à l'intérieur du pod

```

Par exemple, vous pouvez utiliser ceci pour créer un pod temporaire et l'utiliser pour vérifier votre travail :

```bash
kubectl run tmp --image=busybox --restart=Never --rm -it -- /bin/sh

```

Maintenant, vous pourriez faire `wget -O- svc:port` pour voir si votre service est en cours d'exécution, si les politiques de réseau fonctionnent, et ainsi de suite.

##### Remarque :

Le `--dry-run=client -o yaml` n'est pas seulement pour les pods, mais pour de nombreuses ressources. Si nous revenons à la section précédente où nous avons créé un quota de ressources, nous pourrions obtenir un descripteur comme ceci :

```bash
kubeclt create quota my-quota --hard="secrets=2" --dry-run=client -o yaml

```

### Utiliser grep

Vous n'avez pas besoin de connaître les expressions régulières en profondeur. Passez simplement des mots-clés. Par exemple, pour récupérer des informations rapidement depuis le long `kubectl describe pods my-pod` :

```bash
# -i rend la recherche insensible à la casse. C'est un peu plus lent mais pour des textes très courts, cela ne fera pas de différence
# -C 2 affichera la ligne correspondante ainsi que les 2 lignes avant et après la correspondance (le "contexte")
kubectl describe pods my-pod | grep -i -C 2 labels
kubectl describe pods my-pod | grep -i -C 2 ip
...

```

### Surveiller les pods lorsque leur statut change

Au lieu d'exécuter manuellement `kubeclt get pods` toutes les quelques secondes pour voir les changements, passez le flag `watch` pour voir comment vos pods se comportent :

```bash
kubectl get pods --watch

```

### Supprimer les pods rapidement

Faire des erreurs fait partie du processus d'apprentissage. Vous en ferez aussi pendant l'examen. Comme le temps presse, nous devons nous assurer de ne pas avoir à attendre longtemps lors de la suppression des ressources. Ajoutez ces flags pour supprimer les pods immédiatement :

```bash
k delete pods my-pod --force --grace-period=0

```

### Exécuter un pod avec une commande particulière

J'ai trouvé utile d'apprendre à passer des commandes aux pods, jobs, cronjobs, etc., depuis la ligne de commande, comme dans cet exemple :

```bash
kubectl run loop --image=busybox -o yaml --dry-run=client --restart=Never \
-- /bin/sh -c 'for i in {1..10}; do echo "Counting: $i"; done' \
> pod.yaml

```

Cela générerait le fichier pod.yaml :

```bash
apiVersion: v1
kind: Pod
metadata:
  creationTimestamp: null
  labels:
    run: loop
  name: loop
spec:
  containers:
  - args:
    - /bin/sh
    - -c
    - 'for i in {1..10}; do echo "Counting: $i"; done'
    image: busybox
    name: loop
    resources: {}
  dnsPolicy: ClusterFirst
  restartPolicy: Never
status: {}

```

Vous pouvez exécuter une seule commande ou enchaîner plusieurs commandes, comme un mini script bash :

```bash
# Exécuter un exécutable particulier
kubectl run busybox --image=busybox -it --restart=Never -- echo 'hello world'
# Exécuter des commandes à l'intérieur d'un shell (utile pour exécuter plusieurs commandes)
kubectl run busybox --image=busybox -it --restart=Never -- /bin/sh -c 'echo hello world'

```

Ce n'est pas une énorme différence, mais vous n'avez pas besoin de vous souvenir de la manière de l'écrire dans le descripteur de pod ou de perdre du temps à ouvrir la documentation. **Vous devez simplement utiliser ce que vous savez déjà.**

### Roll out

Familiarisez-vous avec la commande `rollout` pour obtenir des informations sur l'état de vos déploiements.

Je commence toujours par le flag `--help` pour me souvenir de la manière de faire ce que je voulais faire.

```bash
kubectl rollout -h

```

### Bonus

Ces derniers conseils ne sont pas pour la certification, mais pour le travail quotidien :

* Ce [module kube-ps1](https://github.com/jonmosco/kube-ps1) facilite la connaissance du cluster et du namespace dans lequel vous opérez, pour éviter des erreurs comme manipuler des ressources de production lorsque vous ne devriez pas.
* De plus, je recommande de jeter un coup d'œil à [Helm](https://helm.sh/). Helm est un gestionnaire de paquets qui peut être utilisé pour déployer des applications facilement (pensez à `npm`). Helm permet également d'écrire des templates que vous pouvez réutiliser pour créer des objets basés sur différentes valeurs (nom, demandes et limites de ressources, etc.).

## Temps de pratique

**Vous apprendrez toujours plus en faisant qu'en lisant.** J'ai donc laissé ici quelques problèmes que j'ai résolus pendant ma préparation pour que vous puissiez pratiquer. Consultez [ce dépôt](https://github.com/dgkanatsios/CKAD-exercises) et [cet article](https://medium.com/bb-tutorials-and-thoughts/practice-enough-with-these-questions-for-the-ckad-exam-2f42d1228552).

Je recommande de résoudre tous ces problèmes par vous-même avant de vérifier la solution proposée. De plus, vérifiez votre travail : consultez les logs, créez un pod pour vous connecter à vos services, etc. Cela vous aidera également à construire votre mémoire musculaire pour l'examen.

Essayez de suivre mes conseils et résolvez les exercices comme si vous étiez vraiment à l'examen : pas de distractions, un seul onglet ouvert - avec la documentation officielle de Kubernetes.

## Conclusions

Ce guide contient tout ce dont vous avez besoin pour faire passer vos compétences au niveau supérieur, pour réussir l'examen CKAD et pour devenir un développeur Kubernetes efficace. Tout est entre vos mains. Vous devez simplement faire un peu de travail. Bonne chance !

Vous pouvez visiter mon blog [www.yourdevopsguy.com](https://www.yourdevopsguy.com/) et [me suivre sur Twitter](https://twitter.com/CodingLanguages) pour plus de contenu technique de haute qualité.

Si vous avez aimé cet article, veuillez le partager car vous pourriez aider quelqu'un à réussir son examen ou à obtenir un emploi.