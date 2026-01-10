---
title: Que signifie K8s ? Comment installer Kubernetes et gérer des clusters
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-06-06T19:46:37.000Z'
originalURL: https://freecodecamp.org/news/what-does-k8s-mean-kubernetes-setup-guide
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/what-does-k8s-mean.png
tags:
- name: containers
  slug: containers
- name: Docker Containers
  slug: docker-containers
- name: Kubernetes
  slug: kubernetes
seo_title: Que signifie K8s ? Comment installer Kubernetes et gérer des clusters
seo_desc: "By Sebastian Sigl\nYou might've seen the term k8s in different sources,\
  \ and wondered what it means. Well, it means Kubernetes. The abbreviation consists\
  \ of:    \n\n\"k\" which is the first letter of Kubernetes,\n\"8\" which is the\
  \ number of letters between t..."
---

Par Sebastian Sigl

Vous avez peut-être vu le terme k8s dans différentes sources et vous êtes demandé ce qu'il signifie. Eh bien, cela signifie Kubernetes. L'abréviation se compose de :

* "**k**" qui est la première lettre de Kubernetes,
* "**8**" qui est le nombre de lettres entre la première et la dernière dans le mot, et
* "**s**" qui est la dernière lettre.

Maintenant, examinons à quoi sert Kubernetes pour comprendre sa force principale et ses domaines d'utilisation.

Les conteneurs sont partout. En utilisant des technologies de conteneurs comme [Docker](https://www.docker.com/), vous pouvez démarrer des applications dans un environnement complètement isolé avec une seule commande. Kubernetes est utilisé pour l'orchestration de conteneurs, combinant plusieurs machines en un cluster et distribuant des conteneurs stateful.

Dans cet article de blog, vous apprendrez :

* Comment utiliser Kubernetes sur votre appareil local,
* Comment lancer des applications dans un cluster Kubernetes,
* Les fournisseurs de Kubernetes gérés les plus populaires pour exécuter vos applications à grande échelle.

Ce tutoriel se concentrera principalement sur l'utilisation de la ligne de commande plutôt que de l'interface utilisateur, car cela vous permet d'utiliser tous les exemples dans un cluster Kubernetes local et distant.

## Comment installer Kubernetes sur votre appareil local

La manière la plus simple de commencer est d'[installer Docker](https://www.docker.com/get-started/). Après avoir démarré, vous pouvez ouvrir Docker, aller dans `Paramètres -> Kubernetes`, et activer Kubernetes localement. Après confirmation, votre cluster Kubernetes démarrera.

La manière la plus simple de communiquer avec un cluster Kubernetes est d'utiliser [kubectl](https://github.com/kubernetes/kubectl). Donc, si vous ne l'avez pas encore fait, [installez kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl).

En outre, je vous recommande de [configurer kubectx](https://github.com/ahmetb/kubectx), qui vous permet de basculer entre différents clusters. Pour simplifier les déploiements Kubernetes, vous devriez également [installer Helm](https://helm.sh/docs/intro/install/), qui vous permet de déployer des applications plus complexes, composées de plusieurs parties, avec une seule commande.

Maintenant, Docker indique que le cluster Kubernetes est prêt dans vos paramètres, vous pouvez alors démarrer certaines applications. Regardons tous les contextes Kubernetes disponibles :

```sh
# Afficher tous les contextes disponibles
kubectx

> development
> docker-desktop

# Sélectionner le contexte local docker desktop
kubectx docker-desktop
```

## Comment lancer des applications dans un cluster Kubernetes

Configurons un [JupyterHub](https://jupyterhub.readthedocs.io/en/stable/) qui permet à une équipe d'utiliser Jupyter Notebooks, l'une des plateformes les plus populaires pour le machine learning et Python.

```sh
# ajouter le dépôt helm
helm repo add jupyterhub https://jupyterhub.github.io/helm-chart/

# démarrer les conteneurs
helm install my-jupyterhub jupyterhub/jupyterhub --version 1.2.0

# après quelques minutes, obtenir des informations sur le service Kubernetes
kubectl --namespace=default get svc proxy-public

NAME           TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
proxy-public   LoadBalancer   10.109.132.29   localhost     80:31480/TCP   31m
```

Comme indiqué, l'IP externe est localhost et exposée sur le port 80. Une fois les conteneurs démarrés, vous pouvez ouvrir [http://localhost](http://localhost) et vous connecter avec le nom d'utilisateur "admin" et sans mot de passe.

Comme vous pouvez le voir, il est très facile d'exécuter une application plus complète avec quelques lignes de commande. Si vous souhaitez essayer plus d'exemples, consultez [mon article de blog sur Helm](https://www.freecodecamp.org/news/helm-charts-tutorial-the-kubernetes-package-manager-explained/).

Pour nettoyer les ressources, vous devez supprimer l'application en cours d'exécution :

```sh
helm uninstall my-jupyterhub

release "my-jupyterhub" uninstalled
```

## Clusters Kubernetes gérés les plus populaires

Une fois que vous souhaitez exécuter une application et la rendre disponible pour les autres, vous devez exécuter un cluster Kubernetes accessible au public. Vous ne devriez pas exécuter votre cluster à partir de zéro si vous n'êtes pas un expert.

Au lieu de cela, vous pouvez utiliser une version gérée d'un cluster Kubernetes, ce qui signifie que la plupart de la maintenance du cluster lui-même est effectuée par un fournisseur externe. Vous pouvez simplement déployer des conteneurs, et les choses devraient simplement fonctionner.

Ma recommandation est d'utiliser le [Google Kubernetes Cluster](https://cloud.google.com/kubernetes-engine/) (GKE), le cluster géré par Google. Google est le concepteur original de Kubernetes et est connu pour fournir une expérience Kubernetes solide. Ils proposent également une version plus extrême gérée appelée GKE Autopilot, qui vous permet de payer par heure de conteneur et par mémoire.

Cependant, en réalité, les équipes utilisent le cluster Kubernetes standard qui vient avec plus d'intégrations d'autres services gérés, qui ne sont pas encore disponibles si vous utilisez Autopilot. Par exemple, vous pouvez créer des comptes de service, des enregistrements DNS ou des certificats gérés en utilisant des ressources Kubernetes grâce à [Config Connector](https://cloud.google.com/config-connector/docs/overview).

Vous pouvez suivre un [tutoriel simple de Google pour configurer un cluster Kubernetes GCP et déployer une application exemple](https://cloud.google.com/kubernetes-engine/docs/deploy-app-cluster) en quelques minutes.

Il existe de nombreux autres clusters Kubernetes gérés comme [Elastic Kubernetes Service](https://aws.amazon.com/de/eks/) (EKS) d'Amazon et [Azure Kubernetes Service](https://azure.microsoft.com/en-us/services/kubernetes-service/) (AKS) de Microsoft. Quel que soit le cloud que vous préférez, il est généralement judicieux d'utiliser le cluster Kubernetes géré de votre fournisseur de cloud actuel.

J'ai [comparé l'intérêt pour Kubernetes chez trois fournisseurs populaires en utilisant Google Trends](https://trends.google.com/trends/explore?date=today%205-y&q=Google%20Kubernetes,AWS%20Kubernetes,Azure%20Kubernetes), ce qui montre qu'Azure et AWS (Amazon) sont les plus populaires.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screenshot-2022-06-05-at-11.01.31.png)

Ces chiffres ne montrent pas quel fournisseur offre la meilleure expérience. Mais ils montrent un intérêt significatif pour Kubernetes exécuté sur Azure. Intéressamment, Azure a pris la tête au cours des derniers mois.

## Résumé

Dans cet article de blog, vous avez appris ce que signifie k8s – c'est simplement une abréviation pour Kubernetes. C'est un système populaire d'orchestration de conteneurs pour automatiser le déploiement, la mise à l'échelle et la gestion des applications. Vous pouvez exécuter Kubernetes localement et à grande échelle dans différents clouds.

J'espère que vous avez apprécié l'article.

Si vous l'avez aimé et que vous avez envie de m'applaudir ou simplement de prendre contact, [suivez-moi sur Twitter](https://twitter.com/sesigl).

Je travaille chez eBay Kleinanzeigen, l'une des plus grandes entreprises de petites annonces au monde. Au fait, [nous recrutons](https://www.ebay-kleinanzeigen.de/careers) !

## Références

* [JupyterHub Helm Chart](https://artifacthub.io/packages/helm/jupyterhub/jupyterhub?modal=values)
* [Top Managed Kubernetes Service](https://techgenix.com/top-managed-kubernetes-services/)
* [Azure vs Google vs Amazon Kubernetes](https://www.linkedin.com/pulse/aks-vs-eks-gke-managed-kubernetes-services-compared-yarden-fayer/?trk=public_profile_article_view)