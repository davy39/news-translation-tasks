---
title: Comment utiliser Azure Kubernetes Service pour l'orchestration de conteneurs
subtitle: ''
author: valentine Gatwiri
co_authors: []
series: null
date: '2023-09-06T13:56:05.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-azure-kubernetes-service-for-container-orchestration
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/Screenshot-from-2023-09-04-11-21-32.png
tags:
- name: Azure
  slug: azure
- name: containers
  slug: containers
- name: Kubernetes
  slug: kubernetes
seo_title: Comment utiliser Azure Kubernetes Service pour l'orchestration de conteneurs
seo_desc: "Containerization has transformed the way applications are built, deployed,\
  \ and scaled. Containers provide a lightweight, portable, and uniform environment\
  \ for developers to bundle their programs as well as their dependencies into a single\
  \ unit. \nBut ..."
---

La conteneurisation a transformé la manière dont les applications sont construites, déployées et mises à l'échelle. Les conteneurs offrent un environnement léger, portable et uniforme pour que les développeurs puissent regrouper leurs programmes ainsi que leurs dépendances en une seule unité.

Mais lorsque le nombre de conteneurs d'un système augmente, les contrôler et les coordonner devient plus difficile. Heureusement, Kubernetes est une solution puissante d'orchestration de conteneurs.

Ce tutoriel vous apprend à utiliser Azure Kubernetes Service (AKS) pour l'orchestration de conteneurs dans l'environnement cloud Azure.

## **Terminologies clés**

Avant de plonger dans le guide, définissons quelques terminologies essentielles :

1. Conteneurisation : Le processus d'emballage de votre code d'application avec tous les fichiers et bibliothèques ensemble dans un seul conteneur pour assurer la cohérence et la portabilité à travers différents environnements.
2. Kubernetes : Une plateforme open-source d'orchestration de conteneurs qui automatise le déploiement, la mise à l'échelle et la gestion des applications conteneurisées.
3. Azure Kubernetes Service (AKS) : Un service Kubernetes géré fourni par Microsoft Azure qui simplifie le déploiement et la gestion des clusters Kubernetes dans l'environnement cloud Azure.
4. Pod : La plus petite unité déployable dans Kubernetes, représentant un ou plusieurs conteneurs fonctionnant ensemble sur un nœud.
5. Déploiement : Une ressource Kubernetes qui définit combien de réplicas d'un Pod doivent fonctionner et le modèle pour les créer.
6. Nœud : Une machine virtuelle ou physique dans un cluster Kubernetes sur laquelle les conteneurs sont déployés.
7. kubectl : L'outil en ligne de commande utilisé pour interagir avec les clusters Kubernetes.

## Comment utiliser Azure Kubernetes Service (AKS)

### **Créer un groupe de ressources Azure**

Commençons par nous connecter au [portail Azure](https://portal.azure.com/), puis cliquons sur "Créer une ressource" et recherchons "Groupe de ressources". Cliquons sur "Groupe de ressources" puis sur "Créer".

![Image](https://www.freecodecamp.org/news/content/images/2023/09/Screenshot-from-2023-09-04-10-31-03.png)
_Groupe de ressources_

Ensuite, remplissons les informations requises, telles que le nom du groupe de ressources et la région, puis cliquons sur "Vérifier + créer" et ensuite sur "Créer" pour créer le groupe de ressources.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/Screenshot-from-2023-09-04-10-32-03.png)
_Fenêtre contextuelle pour le groupe de ressources créé_

### **Créer un cluster AKS**

Dans le portail Azure, cliquons sur "Créer" et recherchons "Azure Kubernetes Service". Cliquons maintenant sur "Azure Kubernetes Service" puis sur "Créer".

![Image](https://www.freecodecamp.org/news/content/images/2023/09/Screenshot-from-2023-09-04-10-33-37.png)
_Création d'un AKS_

Remplissons les informations requises, telles que le nom du cluster AKS, le groupe de ressources (utilisons celui créé à l'étape 1) et la région.

### **Détails du cluster**

Tout d'abord, choisissons notre plan et la ressource que nous avons créée précédemment :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/Screenshot-from-2023-09-04-10-34-41.png)
_Plan et groupe de ressources_

Assurons-nous que la configuration prédéfinie est Standard ($$). Pour plus de détails sur les configurations prédéfinies, voir la configuration prédéfinie du cluster dans le portail Azure. Entrons un nom de cluster Kubernetes, tel que `AKScluster`.

Sélectionnons une région pour le cluster AKS et laissons la valeur par défaut sélectionnée pour la version de Kubernetes.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/awww.png)
_Détails du cluster_

Laissons les valeurs par défaut telles qu'elles sont dans le "pool de nœuds principal" :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/Screenshot-from-2023-09-04-10-38-29.png)
_Pool de nœuds principal_

Dans les parties suivantes, laissons les options par défaut et sélectionnons Suivant : Vérifier + créer :

Lorsque nous allons à l'onglet `Vérifier + Créer`, Azure valide les paramètres que nous avons sélectionnés. Si la validation est réussie, nous pouvons établir le cluster AKS en cliquant sur `créer`. Si la validation échoue, elle informe des paramètres qui doivent être changés.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/a20-15-18-22-1.png)
_Démonstration de validation réussie_

Le cluster AKS est créé en quelques minutes. Lorsque notre déploiement est terminé, nous pouvons accéder à notre ressource soit en choisissant Aller à la ressource, soit en sélectionnant la ressource AKS à partir du groupe de ressources du cluster AKS.

### Configurer kubectl

Après la création réussie du cluster AKS, nous devons cliquer sur "Aller à la ressource".

Dans la page de vue d'ensemble du cluster AKS, cliquons sur "Se connecter" puis sur "Ouvrir dans Cloud Shell".

L'Azure Cloud Shell s'ouvrira en bas du portail. Si on vous le demande, choisissez "Bash" comme type de shell. Ensuite, "Créer un stockage".

![Image](https://www.freecodecamp.org/news/content/images/2023/09/a5-31-19.png)
_Azure Cloud Shell_

Exécutons la commande suivante dans le Cloud Shell pour configurer kubectl afin de se connecter à notre cluster AKS :

```bash
az aks get-credentials --resource-group <votre_nom_de_groupe_de_ressources> --name <votre_nom_de_cluster_aks>
```

Dans notre cas, notre nom de groupe de ressources est `Tutorial` et notre cluster AKS est `AKScluster` :

```bash
az aks get-credentials --resource-group Tutorial --name AKScluster
```

Cela produira la sortie suivante :

```
Fusionné "AKScluster" en tant que contexte actuel dans /home/valentine/.kube/config
```

Pour vérifier la connexion à notre cluster, utilisons `kubectl get` pour retourner une liste des nœuds du cluster comme montré ci-dessous :

```
NOM                               STATUT    RÔLES   ÂGE   VERSION
aks-agentpool-22140002-vmss000000   Prêt    agent   16m   v1.25.6

```

### **Déployer et gérer l'application**

Maintenant que kubectl est configuré pour se connecter à notre cluster AKS, nous pouvons déployer et gérer des applications sur celui-ci.

Créons un fichier manifeste de déploiement Kubernetes dans le Cloud Shell. Pour ce faire, ouvrons l'éditeur de texte nano et créons le fichier "nginx-deployment.yaml". Utilisons la commande suivante pour cela :

```
nano nginx-deployment.yaml
```

L'éditeur nano s'ouvrira, et nous pourrons commencer à taper le contenu du manifeste de déploiement. Pour déployer un simple serveur web NGINX, utilisons le contenu YAML suivant :

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
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
          image: nginx:latest
          ports:
            - containerPort: 80

```

Après avoir copié et collé notre code ci-dessus, nous appuierons sur `Ctrl + X` pour quitter `nano`. Cela nous demandera de sauvegarder les modifications. Appuyons sur `Y` pour confirmer, et lorsque demandé de sauvegarder le fichier, appuyons sur Entrée pour sauvegarder le fichier avec le nom par défaut (nginx-deployment.yaml).

Maintenant, nous avons créé le fichier `nginx-deployment.yaml`, qui contient la spécification YAML pour déployer un simple serveur web NGINX avec trois réplicas.

Déployons l'application NGINX sur notre cluster AKS en utilisant la commande suivante :

```
kubectl apply -f nginx-deployment.yaml

```

Cela produira la sortie suivante :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/Screenshot-from-2023-09-04-10-56-05-1.png)
_Sortie montrant que notre application a été déployée_

### Mettre à l'échelle l'application

Nous pouvons facilement mettre à l'échelle notre application déployée en fonction de la demande.

Pour mettre à l'échelle le déploiement NGINX à cinq réplicas, utilisons la commande suivante :

```
kubectl scale deployment nginx-deployment --replicas=5
```

### Tester l'application

Vérifions maintenant l'état de notre déploiement en utilisant la commande suivante :

```
kubectl get deployment nginx-deployment --watch
```

La commande ci-dessus montrera l'état du déploiement, y compris le nombre de réplicas souhaités, le nombre de réplicas disponibles et l'état actuel du déploiement comme montré ci-dessous :

```
NOM                     PRÊT   À JOUR   DISPONIBLE   ÂGE
nginx-deployment          3/3     3            3           13m
```

### Déploiement en tant que service

Pour exposer le déploiement en tant que service et y accéder externement, nous devons créer un manifeste de service Kubernetes et l'appliquer en utilisant `kubectl apply -f service-manifest.yaml`.

Par exemple, nous pouvons créer un fichier manifeste de service nommé `nginx-service.yaml` et ajouter le contenu suivant :

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  selector:
    app: nginx
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
  type: LoadBalancer

```

Sauvegardons le fichier, puis appliquons-le en utilisant la commande suivante :

```
kubectl apply -f nginx-service.yaml
```

Cela créera un service Kubernetes nommé `nginx-service` qui mappe aux pods déployés par le `nginx-deployment` basé sur le sélecteur de label `app: nginx`. Le service sera accessible externement via un `LoadBalancer`, et nous pouvons vérifier son statut en utilisant :

```
kubectl get service nginx-service --watch
```

Nous devrions pouvoir accéder à notre serveur web NGINX en utilisant l'adresse IP fournie.

```
NOM           TYPE       CLUSTER-IP    EXTERNAL-IP    PORT(S)        AGE
nginx-service LoadBalancer 10.0.61.228   20.87.237.92   80:32415/TCP   93s


```

Visons l'IP externe :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/Screenshot-from-2023-09-04-11-08-27.png)
_Sortie_

Félicitations ! Nous avons déployé avec succès une application web sur notre cluster AKS, l'avons exposée sur Internet et avons géré sa mise à l'échelle sans effort en utilisant Azure Kubernetes Service.

### Surveiller le cluster

AKS s'intègre parfaitement avec Azure Monitor, nous permettant de surveiller les performances et la santé de notre cluster Kubernetes et de nos applications.

Dans le portail Azure, naviguons vers notre cluster AKS et cliquons sur "Surveillance". Là, nous pouvons explorer les différentes options de surveillance, telles que la santé du cluster, les performances et les diagnostics.

## **Conclusion**

Dans ce tutoriel, nous avons profité de l'essai gratuit d'Azure pour apprendre les tenants et aboutissants d'AKS. Nous avons également utilisé le site Azure pour établir notre propre cluster AKS, avec la possibilité d'ajuster les paramètres selon les besoins. Cloud Shell a également été utilisé sans installer quoi que ce soit sur le PC.

Vous pouvez consulter mon blog personnel [ici](https://gatwirival.hashnode.dev/). Bon apprentissage.