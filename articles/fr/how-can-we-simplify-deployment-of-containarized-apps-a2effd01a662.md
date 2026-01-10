---
title: Comment simplifier le déploiement des applications conteneurisées
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-16T05:11:19.000Z'
originalURL: https://freecodecamp.org/news/how-can-we-simplify-deployment-of-containarized-apps-a2effd01a662
coverImage: https://cdn-media-1.freecodecamp.org/images/1*QzKmrPtCm5SvCklDccppkQ.png
tags:
- name: continuous deployment
  slug: continuous-deployment
- name: Devops
  slug: devops
- name: Docker
  slug: docker
- name: Helm
  slug: helm
- name: Kubernetes
  slug: kubernetes
seo_title: Comment simplifier le déploiement des applications conteneurisées
seo_desc: 'By Omer Levi Hevroni

  I asked myself this question when I started to learn Kubernetes: how can we simplify
  the deployment of containerized apps? At first look, deploying containerized apps
  seems pretty simple. All you need is a bunch of YAML files, an...'
---

Par Omer Levi Hevroni

Je me suis posé cette question lorsque j'ai commencé à apprendre [Kubernetes](https://kubernetes.io/) : comment pouvons-nous simplifier le déploiement des applications conteneurisées ? À première vue, le déploiement d'applications conteneurisées semble assez simple. Tout ce dont vous avez besoin est un ensemble de fichiers YAML, et en utilisant `[kubectl](https://kubernetes.io/docs/reference/generated/kubectl/kubectl/)` (l'utilitaire en ligne de commande Kubernetes), vous aurez votre service opérationnel dans votre cluster Kubernetes.

Mais, bien que le déploiement d'une seule application soit une tâche facile, comment déployer des centaines d'applications ? Chez [Soluto](https://www.solutotlv.com), nous avons plus de 100 microservices en production et ce nombre ne cesse de croître. Ainsi, lorsque nous avons commencé à réfléchir au transfert de charge de travail vers notre cluster Kubernetes, nous avons été confrontés à quelques défis :

Premièrement, le déploiement Kubernetes est en réalité plus complexe. Il y a de nombreuses parties mobiles que vous devez configurer correctement : l'autoscaler de pods, les ressources de pods, l'ingress, et ainsi de suite. Ces parties nécessitent une certaine expérience de fonctionnement de Kubernetes, et une configuration incorrecte pourrait causer des problèmes en production. Idéalement, nous aimerions avoir un moyen de simplifier cela, afin que les développeurs puissent se concentrer sur l'écriture de leur code et se soucier moins du déploiement.

Deuxièmement, la sécurité est également un défi. Tous les services en production doivent avoir certaines choses, comme la sécurité de la couche de transport (TLS). Ces éléments ne sont pas nécessairement complexes, mais doivent néanmoins être pris en charge. Nous aimerions les pré-configurer afin que tout nouveau déploiement soit sécurisé par défaut.

### Trouver une solution

Pour résoudre ces défis et accélérer et faciliter le processus d'adoption, nous avons cherché un moyen de créer un modèle pour Kubernetes. Quelque chose que tout développeur pourrait utiliser, et qui nécessiterait seulement quelques paramètres (par exemple, l'image Docker du service) pour mettre le service en production.

D'un autre côté, nous devions être prudents pour ne pas cacher trop de choses — les développeurs doivent être capables de comprendre ce qui se passe afin de pouvoir gérer les problèmes de production. Nous devions trouver le bon niveau d'abstraction qui facilite le déploiement sur Kubernetes, sans cacher trop de détails.

Avec cela en tête, nous avons commencé à chercher une solution. Après avoir essayé quelques choses, nous avons trouvé [Helm](https://helm.sh/). Helm est un gestionnaire de paquets pour Kubernetes. Vous pouvez l'utiliser pour installer n'importe quelle application sur votre cluster, et Helm se chargera d'obtenir tous les fichiers de configuration requis et de les installer sur votre cluster. Helm prend également en charge la mise à jour des déploiements, les retours en arrière, et de nombreuses autres fonctionnalités intéressantes. Chaque paquet Helm est appelé un « Chart », et les charts sont stockés dans un dépôt. Avec Helm, l'installation de [Mongo](https://github.com/kubernetes/charts/tree/master/stable/mongodb), par exemple, est aussi simple que `helm install stable/mongodb`.

Cela semble être une excellente solution ! Nous pouvons définir un chart pour chaque type de service — comme un pour toutes nos API web, qui gérera des choses comme l'équilibreur de charge et le TLS — et le développeur doit simplement spécifier les paramètres requis en utilisant les fichiers de configuration de Helm.

![Image](https://cdn-media-1.freecodecamp.org/images/4P0D8IGfVHiObVNHgAdPTrrhcNFOZh2irhoj)
_Moi et mon coéquipier, lorsque nous avons trouvé Helm_

### Helm : voyons comment cela fonctionne

Pour utiliser Helm, nous devons d'abord l'[installer](https://docs.helm.sh/using_helm/#installing-helm). Helm a deux composants : le client Helm s'exécutant sur votre ordinateur, et Tiller, un composant côté serveur s'exécutant sur votre cluster. Ensuite, nous devons créer le chart en utilisant cette simple commande CLI de Helm : `helm create web-api`

Après avoir exécuté cette commande, vous remarquerez la création d'un nouveau dossier nommé « web-api ». Dans ce dossier, vous trouverez tous les fichiers de configuration Kubernetes familiers : déploiement, service, ingress, et ainsi de suite. Maintenant, il est temps de personnaliser un peu : nous pouvons ajouter un [autoscaler de pods horizontal](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/), définir les ressources par défaut dont le pod a besoin, et bien sûr, activer le TLS par défaut.

Tout est hautement personnalisable en fonction du [mécanisme de modélisation Go](https://docs.helm.sh/chart_template_guide/). Ainsi, tout ce que nous ajoutons peut être remplacé plus tard par le développeur, au cas où la configuration par défaut ne fonctionnerait pas comme prévu.

Nous avons donc maintenant un chart — mais comment pouvons-nous l'utiliser ? Le chart doit exister dans un [dépôt Helm](https://github.com/kubernetes/helm/blob/master/docs/chart_repository.md), qui est essentiellement un serveur avec quelques archives Zip (qui sont tous les charts du dépôt) et un fichier d'index qui est consommé par le CLI. Vous pouvez configurer manuellement votre dépôt en utilisant n'importe quel service de stockage comme Azure Blob ou AWS S3, mais l'option la plus simple est [Chart Museum](https://github.com/kubernetes-helm/chartmuseum).

Chart Museum est un dépôt Helm avec une API CRUD pour gérer vos charts. Il prend en charge l'authentification de base afin que vous puissiez restreindre qui peut pousser de nouveaux charts vers votre dépôt Helm. Helm ne fournit aucune solution de musée en tant que service, vous devrez donc créer la vôtre. Mais c'est très simple — [utilisez simplement son image Docker](https://hub.docker.com/r/chartmuseum/chartmuseum/).

Maintenant, nous pouvons construire un pipeline CI/CD pour notre chart web-api, afin de faciliter le processus de modification :

* Exécuter des tests pour s'assurer que la nouvelle version n'est pas cassée. Je vais discuter de la manière de procéder dans le paragraphe suivant.
* Emballer le nouveau chart, en utilisant le CLI Helm.
* Pousser le nouveau package vers notre instance Chart Museum, en utilisant l'API de Chart Museum.

### Le tester

Notre chart est maintenant prêt à être utilisé par les développeurs ! Mais attendez… comment pouvons-nous savoir que le chart fonctionne réellement ? Et comment pouvons-nous nous assurer qu'il continuera à fonctionner ? C'est pourquoi nous devons écrire des tests pour notre chart (comme nous le faisons pour autre chose).

![Image](https://cdn-media-1.freecodecamp.org/images/WGGYmgftYuRQOqzlognwNV8yF4IFx6etjAF2)

Il y a essentiellement deux choses que nous voulons tester.

1. Nous voulons tester notre modèle — par exemple, si un ingress est censé exister avec un TLS et des règles spécifiques (définies par le développeur), nous devons tester le modèle généré et nous assurer que l'ingress a été créé correctement.
2. Nous voulons tester que les fichiers sont des configurations Kubernetes valides et qu'ils fonctionnent comme prévu.

Tester la première chose est relativement simple — consultez ce [dépôt d'exemple](https://github.com/omerlh/helm-chart-tests-demo) pour voir à quel point c'est simple.

Cela nous permet de tester les fichiers Kubernetes générés, en utilisant `[kubetest](https://github.com/garethr/kubetest)`. C'est génial, mais peut être complexe et désordonné, surtout lorsque vous avez beaucoup de branches dans vos fichiers de modèle.

Une meilleure solution est nécessaire — une qui nous permettra de faire des tests unitaires pour les modèles, sans générer de fichiers Kubernetes. Cela n'était pas un problème jusqu'à récemment lorsque nous avons commencé à avoir beaucoup de branches dans nos modèles, et nous cherchons maintenant des options.

La deuxième chose — tester que les fichiers Kubernetes sont valides — est un peu plus délicate. Pour l'instant, chez Soluto, nous utilisons le mécanisme de version de Helm : chaque chart a une version, et tous nos services utiliseront la dernière version stable. Lorsqu'une nouvelle version de chart est poussée, nous pouvons tester cette version sur un service spécifique. Si elle fonctionne correctement, mettez à jour le reste des services. Une autre option est de tester cela en utilisant `minikube`, mais c'était trop complexe pour nos besoins.

### Enfin : le déploiement !

Nous avons donc maintenant un pipeline CI/CD pour nos charts Helm, et nous avons préparé un chart Helm que les développeurs peuvent utiliser. Maintenant, lorsqu'un nouveau développeur souhaite déployer un nouveau service en production, tout ce qu'il a à faire est :

1. Ajouter notre dépôt à leur Helm local en utilisant `helm repo add chartmuseum http://<chart-museum-url>`
2. Créer un nouveau fichier de configuration Helm et spécifier les paramètres requis (par exemple, l'image Docker du service)
3. Exécuter `helm upgrade --install <service-name> chartmuseum/web-api -f <path_to_config_file>` et c'est tout. Le service est en vie.

Et pour le rendre encore plus facile à comprendre, j'ai créé un dépôt d'exemple [repository](https://github.com/Soluto/kubernetes-deployment-demo). Le dépôt contient toutes les choses dont j'ai discuté dans cet article de blog : un chart générique pour une application web qui peut être déployée avec ce chart et chart museum. Consultez-le pour mieux comprendre ce qui se passe — et il y a même un guide pour vous aider à commencer.

Merci d'avoir suivi. Si vous avez des questions, ou si vous avez besoin d'aide pour commencer avec Helm, n'hésitez pas à demander soit via les commentaires ici, soit via [Twitter](https://twitter.com/intent/tweet?text=.%20%40omerlh%2C%20I%20have%20a%20question%20about%20%40Helm&via=SolutoEng).

Bon Helming !

Publié à l'origine sur [Soluto's Blog](https://blog.solutotlv.com/?utm_source=medium)