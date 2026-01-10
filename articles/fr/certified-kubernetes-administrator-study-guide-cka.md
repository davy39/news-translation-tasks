---
title: Guide d'étude pour l'administrateur certifié Kubernetes – Préparez-vous à l'examen
  CKA
subtitle: ''
author: Nitheesh Poojary
co_authors: []
series: null
date: '2022-01-14T01:14:02.000Z'
originalURL: https://freecodecamp.org/news/certified-kubernetes-administrator-study-guide-cka
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/cka-article-image.png
tags:
- name: Certification
  slug: certification
- name: Kubernetes
  slug: kubernetes
seo_title: Guide d'étude pour l'administrateur certifié Kubernetes – Préparez-vous
  à l'examen CKA
seo_desc: "Kubernetes is a container orchestration platform that helps you manage\
  \ containers at scale. \nI recently passed my certified Kubernetes administrator\
  \ exam, and I would like to share my learning experience and resources with you.\
  \ \nShould You Get Kubern..."
---

Kubernetes est une plateforme d'orchestration de conteneurs qui vous aide à gérer des conteneurs à grande échelle.

J'ai récemment réussi mon examen d'administrateur certifié Kubernetes, et je souhaite partager mon expérience d'apprentissage et mes ressources avec vous.

## Devez-vous obtenir une certification Kubernetes ?

Il existe des opinions mitigées dans l'industrie technologique sur l'importance des certifications. Certaines personnes soutiennent que les certificats que vous possédez n'ont pas d'importance – tout est une question de connaissances pratiques.

Mais tout le monde n'a pas la chance de travailler sur des projets réels. Et les questions de certification sont basées sur des scénarios réels. Donc, si vous n'avez pas eu l'opportunité de travailler beaucoup avec Kubernetes en pratique, vous pouvez apprendre de cet examen et appliquer vos connaissances sur des projets réels.

D'un autre côté, si vous travaillez déjà avec Kubernetes, passer l'examen est une excellente occasion de tester vos connaissances et d'en apprendre davantage sur son fonctionnement interne.

Par exemple, vous avez peut-être travaillé avec AWS depuis un certain temps, mais vous n'avez pas touché à la tarification AWS, ou vous n'avez pas suivi les meilleures pratiques. La certification couvre tous les aspects de Kubernetes, vous apprendrez donc comment vous pouvez réduire vos coûts ou suivre les meilleures pratiques.

Dans ce guide d'étude, je ne vais pas expliquer en détail l'architecture Kubernetes ou les objets Kubernetes (Pods, Déploiements, Services, Config, Secrets, etc.). Si vous souhaitez approfondir ces sujets, voici quelques ressources d'apprentissage Kubernetes utiles :

* [Apprendre Kubernetes en 3 heures](https://www.freecodecamp.org/news/learn-kubernetes-in-under-3-hours-a-detailed-guide-to-orchestrating-containers-114ff420e882/)
* [Le manuel Kubernetes](https://www.freecodecamp.org/news/the-kubernetes-handbook/)

## Qu'est-ce que l'administrateur certifié Kubernetes ?

Le CKA est un produit de la Cloud Native Computing Foundation (CNCF). Il a lancé cette certification en collaboration avec la Linux Foundation. D'autres certifications proposées par CNCF sont :

* Kubernetes et Cloud Native Associate (KCNA)
* Développeur d'applications certifié Kubernetes (CKAD)
* Spécialiste de la sécurité certifié Kubernetes (CKS)

Selon la fondation CNCF,

> « Le but du programme Certified Kubernetes Administrator (CKA) est de garantir que les CKAs possèdent les compétences, les connaissances et la compétence nécessaires pour remplir les responsabilités des administrateurs Kubernetes. »

Voici ce que nous allons couvrir dans ce guide d'étude :

* Détails de l'examen
* Conseils pour l'examen
* Modules de l'examen
* Architecture du cluster, installation et configuration
* Charges de travail et planification
* Services et mise en réseau
* Stockage
* Dépannage

Très bien, plongeons-nous dans le sujet.

## Détails de l'examen d'administrateur certifié Kubernetes

Voici quelques informations utiles pour vous aider à commencer à vous préparer et à planifier l'examen.

Tout d'abord, gardez à l'esprit que cet examen est un examen en ligne surveillé, ce qui signifie que vous pouvez le passer depuis votre domicile ou votre bureau. Il n'y a pas de centres d'examen.

Les frais d'examen sont de 375 $, mais la Linux Foundation offre des bons de réduction de temps en temps. Continuez à [surveiller cet espace](https://training.linuxfoundation.org/promo-inactive/) pour les trouver.

L'examen CKA est un examen basé sur des problèmes, et vous allez résoudre ces problèmes directement en ligne de commande ou en écrivant des fichiers de manifeste.

C'est un examen de 2 heures, et vous devez résoudre 17 questions. Un score de réussite est de 66 %. Chaque question aura des poids différents, comme 4 %, 5 %, 7 %, 13 %, etc.

Certaines questions auront deux parties. Si vous obtenez seulement la première partie correcte, les points pour la partie correcte seront toujours ajoutés à votre score.

L'examen CKA est un examen ouvert. Vous avez accès aux ressources suivantes :

* https://kubernetes.io/docs/
* https://github.com/kubernetes
* https://kubernetes.io/blog/

Si vous ne réussissez pas du premier coup, vous avez droit à une nouvelle tentative.

La certification CKA est valable pour trois ans.

## Conseils pour l'examen d'administrateur certifié Kubernetes

Pour vous aider à commencer, [voici une feuille de triche pratique pour kubectl](https://kubernetes.io/docs/reference/kubectl/cheatsheet/) que vous pouvez utiliser pendant l'examen.

Vous pouvez créer un alias pour cela afin de ne pas avoir à taper la commande complète. Par exemple, si vous créez un alias comme "alias k=kubectl," vous pouvez taper "k" au lieu de "kubectl."

Pendant l'examen, évitez de créer des ressources Kubernetes en utilisant des fichiers YAML, car cela prend trop de temps. Utilisez plutôt une commande impérative pour créer des ressources.

Par exemple, pour créer un pod, utilisez cette commande :
```
kubectl run nginx --image=nginx
```

Si vous souhaitez toujours créer une ressource en utilisant des fichiers YAML, utilisez dry-run=client.

Assurez-vous d'étudier les bases de curl et systemctl, car ils apparaîtront à l'examen.

Enfin, il y a environ 6 ou 8 clusters différents configurés pour l'examen. Assurez-vous de changer de contexte avant de résoudre le problème. La commande de changement de contexte sera fournie au début de chaque question.

## Modules de l'examen d'administrateur certifié Kubernetes

Il y a cinq modules dans l'examen :

* Architecture du cluster, installation et configuration
* Charges de travail et planification
* Services et mise en réseau
* Stockage
* Dépannage

![Screenshot-2022-01-11-at-00.16.14](https://www.freecodecamp.org/news/content/images/2022/01/Screenshot-2022-01-11-at-00.16.14.png)

Nous allons examiner chacun d'eux un peu plus en détail, et couvrir quelques autres informations importantes et connexes en cours de route.

### Déclarations impératives vs déclaratives

Vous devez connaître la différence entre les déclarations impératives et déclaratives afin de pouvoir décider quand utiliser chacune d'elles.

Déployer la ressource Kubernetes de manière impérative signifie exécuter des commandes kubectl, par exemple, `kubectl run nginx --image=nginx`. Déployer de manière déclarative signifie écrire des manifestes en utilisant YAML, par exemple `kubectl apply -f https://k8s.io/examples/pods/pod-nginx-required-affinity.yaml`.

Déployer des ressources en utilisant la méthode impérative aide pendant l'examen et vous fait gagner du temps.

### Module Architecture du cluster, installation et configuration

Vous pouvez vous attendre à ce que 25 % des questions de l'examen proviennent de cette section. Si vous souhaitez obtenir un bon score dans cette section, assurez-vous de réviser ces sujets en profondeur.

Ce module se concentre principalement sur l'authentification, la mise à niveau de la version de votre cluster, la sauvegarde des données Kubernetes et la configuration d'un cluster en utilisant kubeadm.

### Contrôle d'accès basé sur les rôles (RBAC)

Comprendre le contrôle d'accès basé sur les rôles (RBAC) est essentiel. Le RBAC restreint l'accès aux ordinateurs ou aux réseaux en fonction du rôle de l'individu. Les rôles incluent des politiques ou des règles définissant qui peut faire quoi au sein du cluster Kubernetes.

Voici une section pertinente sur [ClusterRole et CluserRole Binding](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) que vous pouvez consulter.

Les questions d'exemple seront comme ceci :

> Créez un nouveau compte de service nommé "sa" dans l'espace de noms development. Créez un rôle de cluster appelé "pod-reader," ayant la permission d'obtenir des pods et de lister les pods. "sa" doit pouvoir obtenir des pods et lister les pods.

Alors, comment aborder une question comme celle-ci ?

Tout d'abord, vous devez créer un espace de noms appelé "development" et créer un service appelé "sa" dans l'espace de travail development :

```
kubectl create namespace development
kubecrl create serviceaccount sa -n development
kubectl create clusterrole pod-reader --verb=get,list,watch --resource=pods
kubectl create clusterrolebinding pod-reader --clusterrole=pod-reader --serviceaccount=development:sa
```

Vous pouvez tester si le sa est autorisé à lire les pods en utilisant la commande suivante :

```
kubectl auth can-i list pods --development target --as system:serviceaccount:development:sa
```

#### Comment installer et configurer un cluster Kubernetes en utilisant kubeadm

Kubeadm automatise l'installation et la configuration des composants Kubernetes comme Control Manager, API server, et KubeDNS.

Si vous avez le temps, je vous recommande vivement de construire un cluster Kubernetes en utilisant le [guide Kubernetes the Hard Way](https://github.com/kelseyhightower/kubernetes-the-hard-way) conçu par Kelsey Hightower.

Si vous n'avez pas le temps de parcourir le guide complet, du point de vue de l'examen, étudiez simplement l'emplacement de la certification et le chemin de configuration Kubernetes.

#### Comment mettre à niveau la version de votre cluster Kubernetes

Il est très probable que vous obteniez cette question, car elle est spécifiquement mentionnée dans le programme de l'examen.

Voici les étapes pour mettre à niveau la version du cluster de 1.22.21 à 1.22.22. Il se peut que vous soyez également invité à mettre à niveau les versions de Kubelet et Kube proxy.

* Vérifiez la version actuelle du cluster, kubeadm et kubelet :

```
kubectl get nodes -o wide
kubeadm version
kubectl version
```

* Mettez à niveau les nœuds du plan de contrôle en premier :

```
apt-get update && apt-get install -y kubeadm=1.2.22-00
```

* Vérifiez le plan de mise à niveau. Utilisez la commande suivante pour voir si le cluster peut être mis à niveau :

```
kubeadm upgrade plan
```

* Appliquez la version mise à niveau :

```
sudo kubeadm upgrade apply v1.22.0
```

Une fois la commande terminée, vous devriez pouvoir voir "upgrade/successful SUCCESS! Your cluster was upgraded to "v1.22.0". Enjoy!"

* Préparez le nœud pour la maintenance en le marquant comme non planifiable et en expulsant les charges de travail :

```
kubectl drain node01 --ignore-daemonsets
```

* Ensuite, mettez à niveau le kubelet et kubectl :

```
apt-get update && apt-get install -y kubelet=1.22.0-00 kubectl=1.22.0-00 
```

* Enfin, redémarrez le kubelet et vérifiez si la version souhaitée a été mise à niveau :

```
sudo systemctl daemon-reload
sudo systemctl restart kubelet
kubectl get nodes -o wide
kubeadm version
kubectl version
```

* Remettez le nœud en ligne en le marquant comme planifiable :
```
kubectl uncordon node01
```

#### Comment sauvegarder et restaurer un cluster ETCD

ETCD est un magasin de valeurs-clés cohérent et distribué qui fournit un moyen fiable de stocker des données auxquelles un système distribué ou un cluster de machines doit accéder.

Kubernetes utilise etcd pour conserver toutes ses configurations et données. Vous pouvez le considérer comme une base de données de Kubernetes. Lorsque vous exécutez "kubectl get pods", les résultats sont récupérés à partir d'etcd. Dans l'examen, le nom de la certification et le chemin sont fournis.

* Connectez-vous au nœud maître et exécutez la commande suivante pour sauvegarder etcd :

```
etcdctl snapshot save /tmp/etcd-backup.db  --cacert /etc/kubernetes/pki/etcd/ca.crt --cert /etc/kubernetes/pki/etcd/server.crt --key /etc/kubernetes/pki/etcd/server.key
```

* Testez votre fichier de sauvegarde :

```
ETCDCTL_API=3 etcdctl --write-out=table snapshot status snapshotdb
```

* Restaurez etcd à partir d'un fichier de sauvegarde :

```
ETCDCTL_API=3 etcdctl snapshot restore tmp/etcd-backup.db  --data-dir /var/lib/etcd-backup --cacert /etc/kubernetes/pki/etcd/ca.crt --cert /etc/kubernetes/pki/etcd/server.crt --key /etc/kubernetes/pki/etcd/server.key
```

### Module Charges de travail et planification

Dans cette section, vous obtiendrez des questions sur le déploiement d'une application Kubernetes, la création de daemonsets, la mise à l'échelle de l'application, la configuration des vérifications de santé, les pods multi-conteneurs et l'utilisation des config maps et des secrets dans un pod.

**Comment déployer une application et exposer l'application en utilisant un service**

Les questions d'exemple pour déployer une application et créer un service peuvent ressembler à ceci :

> Créez un déploiement comme suit :
Nom : nginx
Exposé via un service nginx en utilisant CluserIP
Assurez-vous que le service et le pod sont accessibles au sein du cluster

* Fichier de manifeste pour créer un déploiement :
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
```

Exécutez kubectl get deployments pour vérifier si le déploiement a été créé. Si le déploiement est réussi, "Ready" doit afficher 3/3. Ready affiche combien de réplicas de l'application sont disponibles pour vos utilisateurs.

Si vous devez exposer votre application en dehors du cluster ou à l'intérieur du cluster, vous devez créer un service. Différentes options sont disponibles pour exposer votre application selon vos besoins.

* ClusterIP : Expose l'application au sein du cluster. Par exemple, exposer une base de données à une application backend.
* NodePort : Expose l'application en dehors du cluster en utilisant l'IP du nœud. Par exemple, exposer votre application frontend au monde extérieur.
* LoadBalancer : Expose l'application en dehors du cluster en utilisant un équilibreur de charge.

Et si nous prenions un exemple d'exposition de votre application en utilisant ClusterIP (au sein du cluster). Vous pouvez créer un service en utilisant le fichier de manifeste suivant :

```
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  selector:
    app: nginx
  type: ClusterIP
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8080
```

Vous pouvez utiliser "kubectl get service" pour voir l'adresse IP du service.

Voici un exemple d'exposition de votre application en utilisant NodePort (en dehors du cluster). Vous pouvez créer un service en utilisant le fichier de manifeste suivant :

```
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  selector:
    app: nginx
  type: NodePort
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8080
```

Vous pouvez utiliser "kubectl get service" pour voir l'adresse IP du nœud.

Une autre question d'exemple sera comme ceci :

> Planifiez le pod sur un nœud étiqueté avec distype=ssd

Ici, vous pouvez utiliser node-selector comme ceci :

```
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels:
    env: test
spec:
  containers:
  - name: nginx
    image: nginx
  nodeSelector:
    disktype: ssd
```

#### Comment mettre à l'échelle et mettre à jour les déploiements

Si vous devez mettre à l'échelle le déploiement après l'avoir créé, vous pouvez utiliser la commande suivante.

```
kubectl scale deployment/nginx-deployment --replicas=6
```

Vous pouvez mettre à jour l'image du déploiement existant en utilisant la commande suivante :

```
kubectl set image deployment/nginx-deployment nginx=nginx:1.8
```

#### Comment configurer les vérifications de santé pour votre application

Une fois votre application déployée, vous devez vous assurer que l'application s'exécute avec succès. Si une application plante, vous devez savoir comment vous pouvez tuer le conteneur et en amener un nouveau.

Les vérifications de santé aident à atteindre ce cas d'utilisation. Il existe trois types différents de vérifications de santé que vous pouvez effectuer :

* Sonde de préparation : Kubernetes utilise les sondes de préparation pour savoir quand un conteneur est prêt à commencer à accepter le trafic.
* Sonde de vivacité : Kubernetes utilise les sondes de vivacité pour vérifier quand redémarrer un conteneur. Une fois l'application déployée avec succès, si elle plante entre-temps, une sonde de vivacité détectera et redémarrera l'application.
* Sonde de démarrage : Kubernetes utilise les sondes de démarrage pour savoir quand une application de conteneur a démarré.

Exemple de configuration d'une sonde de vivacité :

```
kubectl apply -f https://k8s.io/examples/pods/probe/exec-liveness.yaml
```

Exemple de configuration d'une sonde de préparation :

```
apiVersion: v1
kind: Pod
metadata:
  labels:
    test: liveness
  name: liveness-exec
spec:
  containers:
  - name: liveness
    image: k8s.gcr.io/busybox
    args:
    - /bin/sh
    - -c
    - touch /tmp/healthy; sleep 30; rm -rf /tmp/healthy; sleep 600
    livenessProbe:
      exec:
        command:
        - cat
        - /tmp/healthy
      initialDelaySeconds: 5
      periodSeconds: 5

```

#### Pod multi-conteneurs/conteneurs sidecar

Le but principal d'un pod multi-conteneurs est de soutenir un conteneur d'assistance co-localisé pour le programme principal.

La méthode de journalisation standard pour les applications conteneurisées est l'écriture dans les flux de sortie standard et d'erreur standard.

Il peut y avoir des cas d'utilisation où vous devez également accéder à ces journaux après qu'un conteneur a planté. Par exemple, votre NGINX conçu pour servir la page web n'est pas adapté pour envoyer les journaux à une solution de journalisation centralisée.

Vous pouvez configurer un conteneur sidecar qui se spécialise dans l'envoi des journaux. Le conteneur sidecar est conçu comme un agent de journalisation, qui est configuré pour récupérer les journaux d'un conteneur d'application.

![logging-with-node-agent-reference from https://kubernetes.io/](https://www.freecodecamp.org/news/content/images/2022/01/logging-with-streaming-sidecar.png)

Les questions d'exemple sur ce sujet seront comme ceci :

> Créez un Pod avec le conteneur principal NGINX, qui sortie les journaux vers un volume partagé, et configurez le conteneur sidecar pour diffuser ces journaux. Vérifiez que les deux conteneurs sont en cours d'exécution.

```
apiVersion: v1
kind: Pod
metadata:
  name: nginx-server
spec:
  volumes:
    - name: shared-logs
      emptyDir: {}

  containers:
    - name: nginx
      image: nginx
      volumeMounts:
        - name: shared-logs
          mountPath: /var/log/nginx

    - name: sidecar-container
      image: busybox
      command: ["sh","-c","while true; do cat /var/log/nginx/access.log /var/log/nginx/error.log; sleep 30; done"]
      volumeMounts:
        - name: shared-logs
          mountPath: /var/log/nginx
```

#### Comment configurer un pod pour utiliser un ConfigMap

Les ConfigMaps stockent les données au format clé-valeur. Un cas d'utilisation possible des ConfigMaps est de garder le code de l'application et la configuration séparés.

Les ConfigMaps sont conçus pour stocker des données non confidentielles telles que des variables d'environnement ou des propriétés d'un jeu ou d'une application. Si vous souhaitez stocker des données sensibles, utilisez des secrets.

Les ConfigMaps aident à créer des fichiers de configuration séparés pour chaque environnement (développement, staging, prod).

Vous pouvez créer des ConfigMaps à partir de fichiers, de répertoires et de valeurs littérales. Les pods peuvent consommer des ConfigMaps en tant que variables d'environnement, arguments de ligne de commande ou en tant que fichiers de configuration dans un volume.

Les questions d'exemple seront comme ceci :

> Créez un ConfigMap appelé cfg-data avec les valeurs var1=val1,var2=val2 et créez un pod busybox avec le volume config-volume, qui lit les données de ce ConfigMap cfg-volume et les place sur le chemin /etc/cfg

```
kubectl create configmap cfg-data --from-literal=key1=val1 --from-literal=key2=val2 --from-literal=key3=val3
kubectl create -f https://github.com/nitheesh86/cka/blob/main/deployments-services/configmap.yml
```

#### Comment configurer un pod pour utiliser des secrets

Les secrets dans Kubernetes peuvent être utilisés pour stocker des données sensibles telles que des mots de passe et des jetons. Les secrets sont similaires aux ConfigMaps mais sont spécifiquement conçus pour contenir des données sensibles. Les pods peuvent utiliser des secrets en tant que variable d'environnement ou en tant que fichiers dans un volume.

* Les questions d'exemple sur les secrets seront comme ceci :

> Créez un secret nommé "db-secret" dans l'espace de noms database. Le secret doit contenir db_user=root et pass=1234. Montez-le en lecture seule dans le pod nommé "mysql-db" en tant que variable d'environnement.

```
kubectl create namespace database
kubectl -n secret create secret generic db-secret --from-literal=username=db_user --from-literal=db_pass=1234 -n database
```

```
https://github.com/nitheesh86/cka/blob/main/deployments-services/mysql-secret.yml
```

### Module Services et mise en réseau

Dans cette section, vous obtiendrez des questions sur la création de politiques de réseau, la création de contrôleurs d'entrée et l'exposition d'applications via des services (déjà couvert ci-dessus).

#### Comment créer des politiques de réseau

Dans Kubernetes, par défaut, la communication entre tous les pods est autorisée. Si vous devez isoler des pods, vous devez appliquer une politique de réseau.

Les questions d'exemple sur les politiques de réseau seront comme ceci :

Autoriser le trafic uniquement depuis l'espace de noms production :

```
kind: NetworkPolicy
apiVersion: networking.k8s.io/v1
metadata:
  name: allow-traffic-from-namespace
spec:
  podSelector:
    matchLabels:
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          purpose: production
```

Cette politique permettra le trafic vers tous les pods depuis l'espace de noms production.

#### Comment créer une ressource d'entrée

Un contrôleur d'entrée est un type d'équilibreur de charge. Il accepte le trafic de l'extérieur du cluster et équilibre la charge vers les pods. Nous pouvons également configurer des règles comme des redirections.

![Screenshot-2022-01-12-at-20.53.03 - Référence du site kubernetes.io](https://www.freecodecamp.org/news/content/images/2022/01/Screenshot-2022-01-12-at-20.53.03.png)

* Comment créer une entrée en utilisant le contrôleur d'entrée NGINX :

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: nginx-ngress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
  - http:
      paths:
      - path: /example
        pathType: Prefix
        backend:
          service:
            name: nginx-service
            port:
              number: 80
```

### Module Stockage

Cette section traite de la création de volumes persistants, de réclamations de volumes persistants et de leur montage dans un pod. Il est utile d'étudier beaucoup sur la persistance et les volumes persistants.

Un PersistentVolume (PV) est un stockage dans le cluster qui a été provisionné par un administrateur de stockage ou provisionné dynamiquement en utilisant des classes de stockage comme AWSElasticBlockStore, AzureDisk, etc.

Une PersistentVolumeClaim (PVC) est une demande de stockage par un utilisateur ou un Pod.

Les questions d'exemple seront comme ceci :

> Créez un Pod NGINX et montez index.html en tant que PersistentVolume.

* Connectez-vous en SSH au nœud et créez un répertoire /mnt/data, puis créez un fichier index.html :

```
sudo mkdir /mnt/data
sudo sh -c "echo 'Hello from Kubernetes storage' > /mnt/data/index.htm
```

* Créez un PersistentVolume et une PersistentVolume Claim :

```
apiVersion: v1
kind: PersistentVolume
metadata:
  name: task-pv-volume
  labels:
    type: local
spec:
  storageClassName: manual
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: "/mnt/data"
```

```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: task-pv-claim
spec:
  storageClassName: manual
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 3Gi
```

* Maintenant, le pod de configuration utilise la PersistentVolume Claim

```
apiVersion: v1
kind: Pod
metadata:
  name: task-pv-pod
spec:
  volumes:
    - name: task-pv-storage
      persistentVolumeClaim:
        claimName: task-pv-claim
  containers:
    - name: task-pv-container
      image: nginx
      ports:
        - containerPort: 80
          name: "http-server"
      volumeMounts:
        - mountPath: "/usr/share/nginx/html"
          name: task-pv-storage

```

De plus, lors de l'examen, il se peut que vous soyez invité à étendre le PersistentVolume. Certaines classes de stockage prennent en charge le redimensionnement du volume, par exemple AWS-EBS, GCE-PD, Azure Disk, Azure File, Glusterfs.

Si la classe de stockage n'est pas activée, vous devez la définir sur "allowVolumeExpansion: true."

Obtenez le nom de la classe de stockage que vous souhaitez étendre avec "kubectl get storage classes". Ensuite, modifiez le fichier YAML.

```
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: standard
parameters:
  type: pd-standard
provisioner: kubernetes.io/gce-pd
allowVolumeExpansion: true
reclaimPolicy: Delete
```

* Ensuite, modifiez PVC pour demander plus d'espace :
```
kubectl edit pvc myclaim and update request parameter
```
![pvc-storageclass](https://www.freecodecamp.org/news/content/images/2022/01/pvc-storageclass.png)

* Une fois que PVC est mis à jour, vous devez remplacer le pod pour que le changement prenne effet. Vous pouvez vérifier la nouvelle taille avec "kubectl get pvc. myclaim".

### Module Dépannage

Cette partie couvre 30 % de l'examen. Vous pouvez vous attendre à des questions sur la façon de dépanner les nœuds.

Les questions d'exemple seront comme ceci :

> L'un des nœuds de travail du cluster n'est pas dans un état prêt. Dépannez le nœud et remettez-le en ligne.

Pour dépanner un nœud de travail, vous devez savoir quels composants sont en cours d'exécution. Les nœuds de travail se composent de kubelet et kube-proxy. Typiquement, l'un de ces services aura des problèmes.

Tout d'abord, vérifiez si le service est en cours d'exécution et essayez de le redémarrer. Si le redémarrage du service ne fonctionne pas, vérifiez les journaux.

* var/log/kubelet.log - Kubelet, responsable de l'exécution des conteneurs sur le nœud
* /var/log/kube-proxy.log - Kube Proxy, responsable de l'équilibrage de charge des services

Vous pouvez vous référer au lien ci-dessous pour un guide de dépannage détaillé :

https://kubernetes.io/docs/tasks/debug-application-cluster/debug-cluster/

## Comment vérifier vos réponses à l'examen

Il est très important de vérifier vos réponses aux questions de l'examen. Voici les moyens de vérifier vos réponses :

### Vérifiez vos pods

Après avoir créé un pod, assurez-vous qu'il est dans l'état prêt avec la commande `kubectl get pod nginx`.

Si vos pods ne sont pas dans un état prêt, exécutez `kubectl desribe pod nginx` pour voir les événements. Vous pouvez également vérifier les journaux du pod en exécutant `kubectllogs nginx`.

### Vérifiez l'état du déploiement

Une fois que vous avez créé un déploiement, vous pouvez obtenir l'état du déploiement en exécutant `kubectl get deployments nginx-deployment`.

Si votre déploiement est en état d'attente, vous pouvez afficher les événements en exécutant `kubectl deployment deployment nginx-deployment`.

### Vérifiez les services

Vous pouvez vérifier que vos points de terminaison de service fonctionnent en lançant des pods d'assistance avec l'image "busybox".

Vous pouvez vous connecter en SSH au pod d'assistance avec la commande `kubectl exec --stdin --tty busybox -- /bin/bash` puis interroger le point de terminaison curl http://ipaddress/. 

Vous pouvez obtenir le point de terminaison du service en exécutant `kubectl get svc my-service`. [Voici une référence](https://kubernetes.io/docs/tasks/debug-application-cluster/get-shell-running-container/) où vous pouvez étudier davantage sur la connexion au conteneur.

## Et c'est tout !

Bonne chance pour vos révisions à l'examen ! J'espère que ce guide vous aidera à vous préparer et à réussir.

Voici les principales sources et références que j'ai utilisées pour étudier et pour écrire cet article :

* https://kubernetes.io/
* https://www.cncf.io/
* https://github.com/ahmetb/kubernetes-network-policy-recipes
* https://www.katacoda.com/courses/kubernetes
* https://jenciso.github.io/personal/manage-tls-certificates-for-kubernetes-users


Merci d'avoir lu, et bon apprentissage.