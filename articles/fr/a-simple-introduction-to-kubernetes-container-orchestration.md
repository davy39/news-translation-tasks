---
title: Une introduction simple à l'orchestration de conteneurs Kubernetes
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2019-10-30T13:00:00.000Z'
originalURL: https://freecodecamp.org/news/a-simple-introduction-to-kubernetes-container-orchestration
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/adult-audience-band-2102568.jpg
tags:
- name: Kubernetes
  slug: kubernetes
- name: virtualization
  slug: virtualization
seo_title: Une introduction simple à l'orchestration de conteneurs Kubernetes
seo_desc: In the beginning there was the FreeBSD - and later Linux - chroot jail.
  Chroot was a way to bring an unmounted file system to life so you could execute
  commands as though it was actually running on its own host. Then came the Linux
  Containers project...
---

Au début, il y avait le chroot de FreeBSD - et plus tard Linux. Chroot était un moyen de donner vie à un système de fichiers non monté afin que vous puissiez exécuter des commandes comme s'il fonctionnait réellement sur son propre hôte. Ensuite est venu le projet Linux Containers (LXC et LXD) qui a ajouté des configurations réseau et de stockage pour exécuter des jails (maintenant plus couramment appelés conteneurs) dans des environnements appropriément isolés et optimisés.

Et puis il y a eu Docker. Les conteneurs Docker ont rationalisé les opérations de conteneurs afin que les ressources logicielles utilisées par plusieurs conteneurs puissent être partagées efficacement. Ils ont également ajouté des dépôts publics en ligne peuplés de vastes collections d'outils logiciels. Mais la vraie valeur de Docker résidait dans la facilité avec laquelle il permettait de déployer des environnements d'applications fiables et prévisibles.

### Ce que Kubernetes apporte

Puis, sortant des brumes du temps, est apparu Kubernetes. Bien que développé à l'origine au sein de Google, Kubernetes a depuis été publié en tant que logiciel open source sous le contrôle de la Cloud Native Computing Foundation.

Au cœur de Kubernetes, il gère les conteneurs de la même manière que Docker. Mais Kubernetes ajoute un vaste écosystème d'outils de mise à l'échelle, d'équilibrage de charge, de proxy réseau et d'administration multi-nœuds. Docker Swarm vient avec une suite d'outils comparable, mais Kubernetes s'est, jusqu'à présent au moins, avéré bien plus populaire.

Kubernetes est bien plus un outil natif à l'échelle de l'entreprise que Docker Swarm. Ce n'est pas que Docker Swarm ne peut pas être utilisé dans l'entreprise - il le peut certainement - c'est que Kubernetes n'est pas nécessairement si bien adapté à un environnement de développement local rapide et sale. La principale raison est que, à ce stade en tout cas, vous avez besoin d'un cluster existant avant de pouvoir faire quoi que ce soit, et la création d'un cluster local nécessite un hyperviseur en cours d'exécution d'une saveur ou d'une autre. Ainsi, avoir un cloud public comme AWS où vous pouvez librement provisionner tous les éléments qui composent un cluster sans avoir à vous soucier de l'infrastructure, compte plus pour Kubernetes que pour Docker en général.

L'empreinte de ressources plus grande de Kubernetes et sa courbe d'apprentissage plus raide peuvent être compensées par une intégration impressionnante : travailler avec des volumes de stockage persistants est simple. Et des solutions de surveillance de déploiement robustes sont facilement disponibles.

### Un coup d'œil rapide au cluster Kubernetes

Voici - basé sur le contenu de [mon cours Pluralsight, « Utiliser Docker sur AWS »](https://pluralsight.pxf.io/nZgKx) - comment fonctionne Kubernetes. Un cluster est composé des ressources de réseau, de stockage et de calcul que vos charges de travail utiliseront. Les ordinateurs physiques ou virtuels du cluster - appelés nœuds - servent soit de primaires, soit de répliques. Un primaire exécute les services qui gèrent toutes les opérations du cluster. Le primaire lui-même est géré via le service kube-apiserver qui répond aux instructions que vous lui envoyez en utilisant le logiciel client kubectl. Le primaire héberge également :

> • Une base de données de configuration de cluster connue sous le nom de etcd
> • kube-controller-manager, qui mesure l'état actuel d'un cluster par rapport à son état souhaité
> • kube-scheduler, qui équilibre les spécifications de configuration par rapport aux ressources disponibles
> • Le cloud-controller-manager qui fournit une intégration critique avec les fournisseurs de cloud public comme AWS

Les nœuds sont contrôlés par des agents logiciels appelés kubelets et maintiennent une connectivité réseau fiable et sécurisée via le service kube-proxy. Le contenu important - votre charge de travail d'application réelle - se produit sur les nœuds au sein des pods, qui sont des structures d'organisation au sein desquelles les conteneurs d'application eux-mêmes s'exécutent. Plusieurs conteneurs peuvent s'exécuter sur un pod, partageant tous une seule adresse IP et des ressources de calcul - fournissant une seule instance de votre application.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/cluster.jpg)
_Les composants d'un environnement Kubernetes typique_

La bonne nouvelle est que le logiciel kubectl est suffisamment intelligent pour simplement lire votre document de configuration YAML et l'utiliser pour donner vie à tous les détails sans votre aide. Si vous souhaitez devenir un administrateur Kubernetes performant, vous devez vraiment comprendre tous ces détails. Mais vous pouvez être pardonné de vous détendre un peu à ce sujet en attendant : la plupart de l'action se déroule de manière invisible, cachée par l'ensemble de commandes relativement simple que nous verrons bientôt.

### Une installation rapide de Kubernetes

Juste pour que vous ne puissiez pas dire que je ne vous ai rien montré de pratique ici, installons la version légère de Kubernetes, MicroK8s, sur une machine Linux. Tout ce dont vous aurez besoin pour cet exercice rapide est une copie fonctionnelle du gestionnaire de paquets Snaps. Cette seule commande installera tous les services principaux, bibliothèques et binaires nécessaires pour des démonstrations de preuve de concept.

```
snap install microk8s --classic
```

Juste pour prouver que l'installation a réussi, demandez au service de lister tous les nœuds qui sont actuellement en cours d'exécution. Bien sûr, il n'y en aura aucun pour l'instant.

```
$ sudo microk8s.kubectl get nodes
No resources found.
```

Il y aura, cependant, un seul service avec une adresse IP privée associée à celui-ci :

```
$ sudo microk8s.kubectl get services
NAME         TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.152.183.1   <none>        443/TCP   80s
```

Enfin, vous pouvez activer le tableau de bord d'administration Kubernetes basé sur le navigateur en utilisant cette commande microk8s.enable. La sortie que vous obtiendrez inclura des instructions supplémentaires pour afficher et utiliser le jeton d'authentification dont vous aurez besoin pour vous connecter.

```
$ sudo microk8s.enable dns dashboard
Enabling DNS
Applying manifest
serviceaccount/coredns created
configmap/coredns created
[...]
If RBAC is not enabled access the dashboard using the default token retrieved with:

token=$(microk8s.kubectl -n kube-system get secret | grep default-token | cut -d " " -f1)
microk8s.kubectl -n kube-system describe secret $token
```

Dans une configuration avec RBAC activé (microk8s.enable RBAC), vous devez créer un utilisateur avec des permissions restreintes comme indiqué dans [https://github.com/kubernetes/dashboard/wiki/Creating-sample-user](https://github.com/kubernetes/dashboard/wiki/Creating-sample-user)

_Cet article est basé sur le contenu de [mon cours Pluralsight, "Utiliser Docker sur AWS"](https://pluralsight.pxf.io/nZgKx). Il y a beaucoup plus de bonnes pratiques d'administration sous forme de livres, de cours et d'articles disponibles sur [bootstrap-it.com](https://bootstrap-it.com).