---
title: Comment déployer une application Kubernetes sur AWS EKS
subtitle: ''
author: Ijeoma Igboagu
co_authors: []
series: null
date: '2025-08-22T11:55:41.512Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-a-kubernetes-app-on-aws-eks
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1755863277691/28937c4d-5862-464d-84a1-dfab01a577bb.png
tags:
- name: Devops
  slug: devops
- name: AWS
  slug: aws
- name: Cloud
  slug: cloud
- name: Kubernetes
  slug: kubernetes
- name: deployment
  slug: deployment
seo_title: Comment déployer une application Kubernetes sur AWS EKS
seo_desc: 'AWS makes it much easier to deploy containerized applications, and running
  Kubernetes in the cloud is a powerful way to scale and manage these applications.

  Among the many managed Kubernetes services AWS offers, Amazon EKS (Elastic Kubernetes
  Service...'
---

AWS facilite grandement le déploiement d'applications conteneurisées, et l'exécution de Kubernetes dans le cloud est un moyen puissant de mettre à l'échelle et de gérer ces applications.

Parmi les nombreux services Kubernetes gérés proposés par AWS, Amazon EKS (Elastic Kubernetes Service) se distingue par son intégration transparente avec l'écosystème AWS, sa grande fiabilité et son excellent support.

Si vous êtes prêt à dépasser les configurations locales et que vous souhaitez déployer une application Kubernetes réelle sur AWS EKS, ce guide vous accompagnera tout au long du processus. Que vous travailliez sur un microservice, une application full-stack ou que vous expérimentiez simplement Kubernetes dans un environnement qui imite la production, vous trouverez ce tutoriel utile.

Dans cet article, je vous guiderai étape par étape à travers le processus de création de votre cluster EKS, le déploiement de votre application et sa mise à disposition sur Internet.

## Au programme :

* [Prérequis](#heading-prerequis)
    
* [Qu'est-ce qu'un cluster Kubernetes ?](#heading-qu-est-ce-qu-un-cluster-kubernetes)
    
* [Qu'est-ce qu'Amazon Elastic Kubernetes Service ?](#heading-qu-est-ce-qu-amazon-elastic-kubernetes-service)
    
* [Pourquoi utiliser Amazon EKS pour Kubernetes ?](#heading-pourquoi-utiliser-amazon-eks-pour-kubernetes)
    
* [Comment créer un cluster Kubernetes avec AWS](#heading-comment-creer-un-cluster-kubernetes-avec-aws)
    
* [Conclusion](#heading-conclusion)
    
* [Ressources](#heading-ressources)
    

## Prérequis

Pour commencer, assurez-vous d'avoir installé les éléments suivants sur votre machine locale :

*   Avoir une compréhension de base des services cloud.
    
*   Avoir une compréhension de base de la ligne de commande Linux.
    
*   Avoir un [compte AWS](https://aws.amazon.com/free/).
    
*   Installer eksctl, un outil CLI simple pour créer et gérer des clusters EKS.
    
*   Installer kubectl, l'outil de ligne de commande standard de Kubernetes.
    
*   Installer Docker pour construire et packager votre application dans un conteneur.
    

Avant de configurer un cluster Kubernetes pour notre application, il est essentiel de comprendre quelques concepts de base.

## **Qu'est-ce qu'un cluster Kubernetes ?**

Un cluster Kubernetes (également appelé K8S) est composé de machines (appelées nœuds) qui exécutent des applications conteneurisées. Il fonctionne aux côtés de moteurs de conteneurs comme [**CRI-O**](https://cri-o.io/#what-is-cri-o) ou [**containerd**](https://containerd.io/) pour vous aider à déployer et gérer vos applications plus efficacement.

Les nœuds Kubernetes se déclinent en deux types principaux :

*   **Nœuds maîtres (plan de contrôle) :** Ils gèrent le travail intellectuel, tel que la planification, la mise à l'échelle et la gestion de l'état global du cluster.
    
*   **Nœuds de travail (plan de données) :** Ils exécutent les applications réelles à l'intérieur des conteneurs.
    

Si vous débutez avec Kubernetes ou si vous souhaitez vous rafraîchir la mémoire, consultez le cours gratuit [**Introduction to Kubernetes (LFS158)**](https://training.linuxfoundation.org/training/introduction-to-kubernetes/?lid=axmt8lvbjbl8) de la Linux Foundation.

## Qu'est-ce qu'Amazon Elastic Kubernetes Service ?

Amazon Elastic Kubernetes Service (EKS) est un service géré qui permet un déploiement facile de Kubernetes sur AWS, éliminant ainsi le besoin de configurer et de maintenir votre propre nœud de plan de contrôle Kubernetes.

AWS EKS s'occupe des tâches complexes en gérant le plan de contrôle, en gérant les mises à niveau et en installant les composants de base, tels que le runtime de conteneur et les processus Kubernetes essentiels. Il offre également des outils intégrés pour la mise à l'échelle, la haute disponibilité et la sauvegarde.

Avec EKS, vous ou votre équipe pouvez vous concentrer sur la création et l'exécution d'applications, tandis qu'AWS gère l'infrastructure sous-jacente.

## **Pourquoi utiliser Amazon EKS pour Kubernetes ?**

Voici quelques avantages clés de l'utilisation d'AWS EKS :

*   EKS gère les mises à niveau, les correctifs et la haute disponibilité pour vous, vous offrant un plan de contrôle entièrement géré avec un effort manuel minimal.
    
*   Vous pouvez facilement mettre à l'échelle vos applications, et l'infrastructure se développe à mesure que vos besoins évoluent.
    
*   Il dispose d'un support intégré pour les rôles IAM, la mise en réseau privée et le chiffrement.
    
*   AWS EKS fonctionne sur une infrastructure hautement disponible à travers plusieurs zones de disponibilité AWS, rendant votre application disponible mondialement.
    
*   Avec Amazon EKS, vous bénéficiez de la puissance de Kubernetes sans gérer la configuration sous-jacente. Ainsi, vous pouvez rester concentré sur la création et l'exécution de vos applications.
    

## **Comment créer un cluster Kubernetes avec AWS**

Voyons maintenant le processus de mise en service d'un cluster Kubernetes.

![c'est parti](https://cdn.hashnode.com/res/hashnode/image/upload/v1754818871609/8b0f622a-af82-4a29-bb22-fbdb1a6279bb.png align="center")

### **Étape 1 : Comment installer les outils nécessaires pour créer un cluster**

Le moyen le plus simple et le plus convivial pour les développeurs de lancer un Elastic Kubernetes Service utilisable en production est d'utiliser **eksctl**. Il s'occupe de la configuration manuelle et provisionne automatiquement les ressources AWS nécessaires.

Avant de commencer, nous devons installer deux outils essentiels :

*   **eksctl** – Utilisé pour créer et gérer votre cluster EKS.
    
*   **kubectl** – Permet d'interagir avec votre cluster, de déployer des applications et de gérer les ressources Kubernetes.
    

Ces outils faciliteront la configuration de votre cluster Kubernetes et vous permettront de travailler avec lui directement depuis votre terminal.

#### Comment installer eksctl

Ouvrez votre navigateur et accédez à la documentation officielle de [eksctl](https://eksctl.io/). Faites défiler jusqu'à la section **Installation**.

Allez aux instructions **Unix** si vous utilisez Ubuntu ou un système similaire. Copiez ensuite la commande d'installation et collez-la dans votre terminal.

![Installation de l'outil eksctl](https://cdn.hashnode.com/res/hashnode/image/upload/v1754819104540/48310ddc-89fb-49b9-990b-ca425ac81e55.gif align="center")

Une fois l'opération terminée, exécutez `eksctl version` pour confirmer que l'installation a réussi.

![vérification de la version](https://cdn.hashnode.com/res/hashnode/image/upload/v1754819269922/69d18189-f3ea-421b-9666-e37c43d7c077.gif align="center")

#### Comment installer kubectl

L'étape suivante consiste à installer [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/). Vous trouverez les instructions d'installation dans la documentation officielle de Kubernetes, qui propose des étapes basées sur votre système d'exploitation.

![Installation de kubectl](https://cdn.hashnode.com/res/hashnode/image/upload/v1754819717619/028418cb-424a-4514-a7a7-dfd17c2c03ce.gif align="center")

### **Étape 2 : Comment créer le cluster Elastic Kubernetes Service (EKS)**

Maintenant que vous avez installé les outils nécessaires, il est temps de lancer le cluster.

Pour commencer, ouvrez votre terminal et exécutez la commande suivante :

```bash
# Créer un cluster EKS nommé "k8s-example" dans eu-west-2 (Londres)
eksctl create cluster --name k8s-example --region eu-west-2
```

![Création d'un terminal dans votre cluster](https://cdn.hashnode.com/res/hashnode/image/upload/v1754820013644/a763f4f1-4b5f-47c2-9c09-3148cb77f579.gif align="center")

L'un des grands avantages d'utiliser AWS EKS est qu'une fois votre cluster Kubernetes créé, il met automatiquement à jour votre fichier `~/.kube/config`. Cela signifie que vous pouvez commencer à interagir avec votre cluster immédiatement, en utilisant `kubectl`, sans configuration supplémentaire.

![Cluster prêt sur AWS](https://cdn.hashnode.com/res/hashnode/image/upload/v1754825286662/7b7f68a9-72c1-4306-bc09-a0d5c528b900.png align="left")

Après avoir exécuté la commande (comme indiqué dans le GIF ci-dessus), votre cluster Kubernetes est créé avec succès.

![Cluster Kubernetes créé](https://cdn.hashnode.com/res/hashnode/image/upload/v1754825194425/a6c611d4-837f-4106-955f-99bdcbb9cf5d.gif align="left")

Rendez-vous sur la console AWS, et vous verrez votre nouveau cluster listé avec un statut **Active**.

Votre cluster étant opérationnel, il est temps de tester la connexion. Vous pouvez le faire en exécutant quelques commandes `kubectl` dans votre terminal pour lister les nœuds, les pods et les espaces de noms (namespaces) de votre cluster.

**Pour tester la connexion :**

```bash
kubectl get nodes
```

Cette commande liste tous les nœuds de votre cluster.

```bash
kubectl get pods 
```

Cette commande liste tous les pods en cours d'exécution.

```bash
kubectl get namespaces
```

Cette commande liste tous les espaces de noms actuellement actifs.

![test du cluster](https://cdn.hashnode.com/res/hashnode/image/upload/v1754825006032/4d2e72ff-8eb9-48be-bd90-efffbb840241.png align="left")

Si chaque commande renvoie une liste de ressources, félicitations ! Votre connexion au cluster Kubernetes est réussie.

### **Étape 3 : Comment créer des manifestes Kubernetes**

Définissons l'application à l'aide d'un fichier YAML. Dans ce fichier, vous allez créer deux ressources clés : un **Deployment** et un **Service**.

*   Le **Deployment** garantit que votre application s'exécute de manière fiable en spécifiant le nombre de réplicas à exécuter, l'image du conteneur à utiliser et la manière de gérer les mises à jour.
    
*   Le **Service** rend votre application accessible — à la fois au sein du cluster Kubernetes et, si nécessaire, depuis Internet, même si les pods sous-jacents changent ou redémarrent.
    

Ensemble, ces ressources orchestrent votre application afin qu'elle puisse s'exécuter de manière cohérente dans différents environnements.

```yaml
#deployment-example.yaml

apiVersion: apps/v1
kind: Deployment
metadata:
  name: amazon-deployment
  namespace: default
  labels:
    app: amazon-app
spec:
  replicas: 5
  selector:
    matchLabels:
      app: amazon-app
      tier: frontend
      version: 1.0.0
  template:
    metadata:
      labels:
        app: amazon-app
        tier: frontend
        version: 1.0.0
    spec:
      containers:
        - name: amazon-container
          image: ooghenekaro/amazon:2
          ports:
            - containerPort: 3000
---
apiVersion: v1
kind: Service
metadata:
  name: amazon-service
  labels:
    app: amazon-app
spec:
  type: LoadBalancer
  ports:
    - port: 80
      targetPort: 3000
  selector:
    app: amazon-app
```

Le service utilise un type **LoadBalancer**, ce qui indique à AWS de provisionner un **Elastic Load Balancer** (ELB) et d'acheminer le trafic vers les pods.

### **Étape 4 : Comment déployer l'application sur EKS**

Maintenant que votre fichier YAML est défini et que le cluster Kubernetes sur AWS EKS est prêt, il est temps de déployer votre application.

Pour ce faire, exécutez la commande suivante dans votre terminal pour appliquer la configuration définie dans votre fichier manifeste :

```bash
kubectl apply -f deployment-example.yaml
```

Cette commande indique à Kubernetes de créer les pods et services nécessaires selon les spécifications du manifeste.

Ensuite, vous pouvez vérifier le statut de vos pods et services :

```bash
kubectl get pods
kubectl get svc or service
kubectl get all
```

![vérification du bon déploiement de l'application](https://cdn.hashnode.com/res/hashnode/image/upload/v1754824866347/8b48e580-d25f-4965-9c29-3609778365f0.png align="left")

### **Étape 5 : Comment accéder à votre application**

Pour voir votre application dans le navigateur, exécutez la commande suivante pour lister vos services :

```yaml
kubectl get svc
```

Cherchez l'**EXTERNAL-IP** de votre service.

![Affichage de l'IP externe sur le navigateur](https://cdn.hashnode.com/res/hashnode/image/upload/v1754824764125/b78b8feb-e5da-4d3c-b467-6ccb88d00373.png align="left")

Copiez l'adresse IP et collez-la dans votre navigateur. Votre application devrait maintenant être en ligne !

![site en ligne](https://cdn.hashnode.com/res/hashnode/image/upload/v1754824488894/821522c0-186f-48fd-8c64-ed29a2ba4447.png align="left")

## **Conclusion**

Déployer une application Kubernetes sur AWS EKS peut sembler complexe au début, mais avec des outils comme eksctl et kubectl, le processus est étonnamment accessible.

Que vous soyez un développeur expérimentant Kubernetes ou une équipe cherchant à mettre à l'échelle des charges de travail de production, EKS offre une base solide et évolutive qui soutient vos applications au fur et à mesure de leur croissance.

## Ressources

* [Play with Kubernetes](https://labs.play-with-k8s.com/)
    
* [Tutoriel Docker 101](https://www.docker.com/101-tutorial/)
    
* [Comment créer un pipeline CI/CD avec AWS Elastic Beanstalk](https://dev.to/ijay/how-to-create-a-cicd-using-aws-elastic-beanstalk-15nh)
    

Merci de m'avoir lu !