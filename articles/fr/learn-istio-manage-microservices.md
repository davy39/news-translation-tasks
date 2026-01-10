---
title: Apprendre Istio – Comment gérer, surveiller et sécuriser les microservices
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-05-23T14:00:55.000Z'
originalURL: https://freecodecamp.org/news/learn-istio-manage-microservices
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/how-traces-are-generated-1.png
tags:
- name: Microservices
  slug: microservices
seo_title: Apprendre Istio – Comment gérer, surveiller et sécuriser les microservices
seo_desc: "By Rinor Maloku\nThree years ago, I wrote an article titled \"Back to Microservices\
  \ with Istio\" for Google Cloud Community. I published it there to reach people\
  \ interested in the latest technologies built on top of Kubernetes. \nAt that point,\
  \ Istio was..."
---

Par Rinor Maloku

Il y a trois ans, j'ai écrit un article intitulé ["Back to Microservices with Istio"](https://medium.com/google-cloud/back-to-microservices-with-istio-p1-827c872daa53) pour la Google Cloud Community. Je l'ai publié là-bas pour toucher les personnes intéressées par les dernières technologies construites au-dessus de Kubernetes.

À ce moment-là, Istio était une technologie de niche. Mais trois ans plus tard :

* J'ai co-écrit le livre "[Istio in Action](https://www.manning.com/books/istio-in-action?utm_source=rinor&utm_medium=affiliate&utm_campaign=book_posta2_istio_9_30_18&a_aid=rinor&a_bid=9f6a70f3)" avec Christian Posta ([@christianposta](https://twitter.com/christianposta)), qui a été récemment publié par Manning.
* J'ai rejoint [Solo.io](https://www.solo.io/), où je collabore quotidiennement avec des clients pour utiliser au mieux les capacités de Service Mesh d'Istio. Que ce soit pour améliorer la résilience, réduire les risques liés au déploiement de nouveaux logiciels, améliorer la posture de sécurité ou l'une des innombrables capacités qu'il permet.

Kubernetes, qui atteignait déjà une large adoption à l'époque, est maintenant devenu une [technologie mondiale grand public](https://www.cncf.io/reports/cncf-annual-survey-2021/#:~:text=Kubernetes%20has%20crossed%20the%20adoption%20chasm%20to%20become%20a%20mainstream%20global%20technology%C2%A0). Et à mesure que le nombre de services fonctionnant sur cette plateforme augmente, le nombre d'organisations adoptant Istio augmentera également.

De plus, **Istio n'est plus une technologie de niche !** Après de nombreuses améliorations de l'expérience utilisateur — par exemple, l'installation et les opérations de jour 2 sont devenues beaucoup plus faciles — Istio a été adopté par des organisations de différentes tailles et industries.

En même temps, il continue d'étendre son ensemble d'outils en ajoutant le support des machines virtuelles, en permettant au maillage de s'étendre sur plusieurs clusters, et bien plus encore.

La dernière chose que vous devez savoir est que le marché manque de personnes possédant ce genre de connaissances. Nous avons besoin de *vous !* C'est pourquoi j'ai entièrement réécrit cet article pour en faire une introduction approfondie à Istio et montrer ce qu'il fait sous le capot – car je ne veux pas seulement que vous sachiez "ce qu'il fait", mais aussi "comment" il le fait.

Voici le contenu que nous allons couvrir dans ce guide :

* [Que fait Istio ?](#heading-que-fait-istio)
* [Introduction à Istio](#heading-introduction-a-istio)
* [Architecture d'Istio](#heading-architecture-distio)
* [Comment utiliser Istio en pratique](#heading-comment-utiliser-istio-en-pratique)
* [Comment exécuter les services sur le maillage](#heading-comment-executer-les-services-sur-le-maillage)
* [Ingress Gateway – Comment autoriser le trafic dans le maillage](#heading-ingress-gateway-comment-autoriser-le-trafic-dans-le-maillage)
* [Observabilité](#heading-observabilite)
* [Gestion du trafic – Déploiements Canary](#heading-gestion-du-trafic-deploiements-canary)
* [Sécurité Istio](#heading-securite-istio)

## Que fait Istio ?

**Istio** est un projet open-source qui a débuté par un partenariat entre des équipes de Google, IBM et Lyft. Aujourd'hui, le nombre de contributeurs s'est élargi pour inclure de nombreuses autres organisations telles que Solo.io, Tetrate, Aspen Mesh, et plus encore.

Il résout de nombreuses préoccupations liées aux microservices, telles que :

* **Gestion du trafic :** Résoudre le manque de fiabilité du réseau avec des timeouts, des tentatives (retries) et de l'équilibrage de charge (load balancing).
* **Sécurité :** Chiffrer le trafic en transit, authentification et autorisation des utilisateurs finaux et des services.
* **Observabilité :** Rendre le système observable avec des traces, des métriques et des journaux (logs).

Ces complexités ou préoccupations peuvent être résolues dans la couche applicative, mais vos services deviennent alors surchargés de bibliothèques qui gèrent la gestion du trafic, la découverte de services, l'authentification, l'instrumentation et tout ce qui n'est pas au cœur de votre métier.

Illustrons cela par une conversation entre un chef de produit (PM) et un développeur :

> **PM :** Combien de temps faudra-t-il pour ajouter une fonctionnalité de feedback à l'application ?
>
> **Dev :** Deux sprints.
>
> **PM :** Quoi... ?! C'est juste un CRUD !
>
> **Dev :** Créer le CRUD est facile, mais nous devons authentifier et autoriser les utilisateurs et les services. Et comme le réseau n'est pas fiable, nous devons implémenter des retries et des circuit breakers. Nous avons besoin de timeouts et de cloisons (bulkheads) pour nous assurer de ne pas faire tomber tout le système. De plus, pour détecter les problèmes, nous avons besoin de monitoring et de tracing [...]

Vous voyez l'idée. Toute la cérémonie et l'effort nécessaires pour ajouter un simple service sont énormes.

La figure ci-dessous visualise toutes les couches implémentées dans votre code applicatif qui épuisent les ressources de votre équipe. Des ressources qui seraient mieux dépensées en se concentrant sur les fonctionnalités métier de base.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/layers-of-a-microservices.png)
*Les couches d'un microservice en plus de la fonctionnalité métier de base*

Istio supprime toutes les préoccupations transversales mentionnées ci-dessus de vos services et les implémente au niveau de la couche plateforme. Voyons comment cela se passe.

**NOTE :** Cet article suppose que vous avez une connaissance pratique de Kubernetes. Si ce n'est pas le cas, je vous recommande de lire [mon introduction à Kubernetes](https://www.freecodecamp.org/news/learn-kubernetes-in-under-3-hours-a-detailed-guide-to-orchestrating-containers-114ff420e882/) puis de poursuivre avec cet article.

## Introduction à Istio

Dans un monde sans Istio, un service fait des requêtes directes à un autre et, en cas d'échec, le service est responsable de la gestion de ces échecs. Il peut le faire en réessayant, en abandonnant les requêtes qui prennent trop de temps, en ouvrant le circuit breaker pour protéger les services de la surcharge, et ainsi de suite.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/service-to-service-traffic.png)
*Trafic de service à service*

C'est pourquoi nous avons tant de bibliothèques pour la découverte de services, la résilience, l'instrumentation, etc. Étant donné que chaque service doit répondre à ces préoccupations, il est logique de les résoudre sur la couche plateforme plutôt que dans le code applicatif.

Istio a conçu une solution ingénieuse. Il intercepte toutes les communications réseau et les redirige vers un proxy sidecar capable qui s'exécute aux côtés de chaque service. **Et c'est la responsabilité des proxys de résoudre toutes les préoccupations mentionnées ci-dessus.**

L'animation ci-dessous montre comment les proxys sidecar servent d'intermédiaires au trafic et implémentent les retries et les basculements (failovers) pour les requêtes échouées.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/services-in-istio.gif)
*Trafic de service à service dans Istio*

Le proxy sidecar fait plus que cela. Nous détaillerons bon nombre de ses fonctionnalités dans cet article. Mais ce qu'il est essentiel de noter, c'est que l'application elle-même ignore totalement l'existence du proxy de service ou même de l'ensemble du maillage. Si on l'interrogeait sur le Service Mesh, votre application répondrait : "C'est quoi un Service Mesh ?!"

![Image](https://www.freecodecamp.org/news/content/images/2022/05/fish-in-water.png)
*Dessin par Victoria Dimitrakopoulos*

### Le proxy sidecar

Pour que le proxy sidecar puisse discerner si la requête a échoué ou non, il doit comprendre les protocoles de la couche applicative, tels que HTTP. Les proxys qui agissent à cette couche sont des *proxys de couche applicative* ou *proxys de couche 7*. J'utiliserai ces termes de manière interchangeable dans la suite de l'article.

En interceptant tout le trafic de service à service, les proxys de couche applicative peuvent implémenter les éléments suivants :

* **Tolérance aux pannes** — En utilisant les codes d'état de réponse, le proxy comprend quand une requête échoue et la réessaie.
* **Gestion fine du trafic** — Router les requêtes avec des en-têtes spécifiques vers les services prévus. Par exemple, envoyer uniquement les utilisateurs bêta vers une nouvelle version bêta d'une application.
* **Métriques** — Le nombre de réponses réussies et échouées, le temps mis par un service pour répondre, et ainsi de suite.
* **Traçage (Tracing)** — Ajoute des en-têtes spéciaux dans chaque requête et les suit à travers les services du cluster.
* **Sécurité** — Authentifie les services et les utilisateurs finaux à l'aide de certificats et de jetons JWT, respectivement.

Ce ne sont là que quelques-unes des capacités offertes par la gestion du trafic au niveau de la couche réseau applicative.

## Architecture d'Istio

Istio est composé du *plan de données (data plane)* et du *plan de contrôle (control plane)*.

### Le plan de données

Le plan de données comprend tous les pods dans lesquels le proxy sidecar a été injecté. Dans la communauté Istio, nous les appelons fréquemment workloads du maillage ou simplement *workloads*.

Pendant ce temps, nous appelons les workloads sans sidecar des *workloads hérités (legacy workloads)* parce qu'ils sont mauvais et dangereux, comme vous le verrez plus tard dans la section sécurité.

**NOTE :** *"Pourquoi ne pas simplement les appeler des pods ?"* — Parce que les workloads du maillage ne sont pas liés à un cluster et peuvent s'exécuter dans différents clusters, ou sur des machines virtuelles, et en fait partout où vous pouvez exécuter et configurer le proxy sidecar.

#### Zoom sur un workload

Chaque workload possède les quatre composants suivants :

* **Le conteneur init** – vous n'avez pas à vous en soucier. Il suffit de savoir qu'il configure la redirection du trafic vers le proxy sidecar.
* **Le pilot-agent** – vous n'avez pas non plus à vous en soucier. Il suffit de savoir qu'il effectue l'amorçage (bootstrapping) initial du proxy sidecar.
* **Le proxy sidecar** – vous n'avez pas non plus besoin de vous en soucier. Il suffit de savoir que c'est le composant concret qui implémente les fonctionnalités de gestion du trafic, de sécurité et d'observabilité.
* **L'application elle-même**

Istio utilise Envoy comme proxy sidecar. Envoy est un proxy de couche 7 polyvalent, hautement extensible et soutenu par une communauté dynamique.

Envoy se différencie des autres proxys en étant configurable dynamiquement via une API qu'il expose.

Vous pourriez demander : "**Pourquoi est-ce important ?**" Parce qu'Envoy doit être tenu à jour des changements qui surviennent dans l'environnement.

Par exemple, dans Kubernetes, les workloads ont une durée de vie courte. De nouveaux services sont constamment déployés, les workloads sont replanifiés et les utilisateurs peuvent définir de nouvelles règles de routage ou politiques. Par conséquent, nous avons besoin de *"quelque chose"* qui met continuellement à jour la configuration du proxy.

Ce "quelque chose" est le *plan de contrôle*, qui utilise l'API Envoy pour synchroniser le proxy avec les changements survenant dans la plateforme sous-jacente.

### Le plan de contrôle Istio

Le plan de contrôle d'Istio est un contrôleur Kubernetes qui surveille le serveur API Kubernetes pour en savoir plus sur les workloads s'exécutant dans la plateforme et génère la configuration Envoy sur la façon de router le trafic vers et depuis ces workloads.

De plus, Istio expose une API au format Custom Resource Definitions (CRDs) Kubernetes avec laquelle les opérateurs de services (*vous*) peuvent configurer le plan de données.

Par *configuration du plan de données*, on entend que vous configurez les workloads avec des politiques, des règles de routage, des retries, etc.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/istio-control-plane.png)
*Le plan de contrôle configure le plan de données*

Nous avons appris pas mal de choses sur l'architecture d'Istio. À partir de maintenant, nous allons réduire la théorie au strict minimum et passer à des exemples pratiques qui vous aideront à comprendre et à mémoriser le contenu.

## Comment utiliser Istio en pratique

### Prérequis : Comment configurer un cluster Kubernetes

Avant d'apprendre Istio et comment l'utiliser, vous devez disposer d'un cluster Kubernetes avec un accès administrateur.

Naturellement, vous aurez besoin de `kubectl` pour interagir avec le cluster. Pour installer `kubectl`, rendez-vous sur [la documentation officielle et suivez les instructions pour votre système d'exploitation](https://kubernetes.io/docs/tasks/tools/install-kubectl/).

Cet article utilise *Kubernetes In Docker*, également connu sous le nom de `kind`. Vous pouvez utiliser toute autre distribution Kubernetes locale telle que Docker-Desktop ([comment l'installer](https://docs.docker.com/desktop/) et [l'utiliser](https://docs.docker.com/desktop/kubernetes/)), [Rancher Desktop](https://rancherdesktop.io/), ou [Minikube](https://minikube.sigs.k8s.io/docs/start/). Assurez-vous simplement d'être au moins sur la version 1.23 de Kubernetes.

Pour installer `kind`, suivez les instructions d'installation sur [https://kind.sigs.k8s.io/docs/user/quick-start/](https://kind.sigs.k8s.io/docs/user/quick-start/).

### Comment créer un cluster avec `kind`

Après avoir installé `kind`, créez un cluster Kubernetes avec la commande ci-dessous :

`kind create cluster --image=kindest/node:v1.23.1`

Cette commande télécharge une image de conteneur avec la version 1.23.1 de Kubernetes et l'exécute sur votre moteur de conteneur. Par exemple, si votre moteur est `docker`, vous pouvez voir le conteneur en cours d'exécution en exécutant `docker ps`.

Votre sortie affichera un nouveau conteneur en cours d'exécution :

```
CONTAINER ID   IMAGE                  COMMAND        NAMES
2974301ffa31   kindest/node:v1.23.1   "/usr/loca…"   kind-control-plane
```

**NOTE :** Istio 1.13 est compatible avec les versions 1.20 et ultérieures de Kubernetes. Pour en savoir plus sur les versions de Kubernetes prises en charge, consultez la documentation officielle sur [Istio: Supported Kubernetes releases.](https://istio.io/latest/docs/releases/supported-releases/)

### Comment installer Istio sur le cluster

Vous pouvez installer Istio soit avec l'utilitaire `istioctl`, soit avec le gestionnaire de paquets `helm`. Pour obtenir `istioctl`, téléchargez les artefacts de la version d'Istio, comme indiqué ci-dessous.

```bash
curl -L https://istio.io/downloadIstio | \
  ISTIO_VERSION=1.13.2 TARGET_ARCH=x86_64 sh -
```

Dans le répertoire téléchargé, vous trouverez l'outil CLI `istioctl` sous `istio-1.13.2/bin/istioctl`. Ensuite, déplacez le binaire dans votre variable d'environnement PATH afin de pouvoir exécuter les commandes `istioctl` depuis n'importe quel répertoire.

Après cela, installez Istio avec la commande ci-dessous :

```bash
istioctl install --set profile=demo -y
```

L'exécution de cette commande peut prendre plusieurs minutes car elle attend que tous les Pods soient opérationnels. Une fois terminée, affichez les Pods déployés dans l'espace de noms d'installation d'Istio.

```bash
kubectl get pods -n istio-system
```

Vous devriez voir la sortie ci-dessous.

```
NAME                                   READY   STATUS    RESTARTS
istio-egressgateway-6cf5fb4756-r569f   1/1     Running   0
istio-ingressgateway-dc9c8f588-cn2z4   1/1     Running   0
istiod-7586c7dfd8-2nbsk                1/1     Running   0
```

Les composants installés sont :

* **Istio egress gateway** – utilisé pour sécuriser le trafic sortant.
* **Istio ingress gateway** – le point d'entrée du trafic arrivant dans votre cluster.
* **Istiod** – le plan de contrôle d'Istio qui configure les proxys de service.

### Comment installer les add-ons Istio

Les artefacts Istio téléchargés précédemment contiennent des exemples d'outils pour visualiser la télémétrie générée. Pour les déployer dans votre cluster, exécutez la commande ci-dessous :

```bash
kubectl apply -f istio-1.13.2/samples/addons/
```

Ceci installe les outils suivants : Prometheus, Grafana, Kiali et Jaeger. Nous y jetterons un œil plus tard. Mais d'abord, nous avons besoin de services.

### L'application exemple : Analyse de sentiment

Nous allons exécuter l'application de microservices utilisée dans mon [article d'introduction à Kubernetes](https://www.freecodecamp.org/news/learn-kubernetes-in-under-3-hours-a-detailed-guide-to-orchestrating-containers-114ff420e882). Elle est suffisamment complexe pour présenter les fonctionnalités d'Istio en pratique.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/sentiment-analysis-app.png)
*Les services d'analyse de sentiment*

La figure ci-dessus montre les services qui composent l'application :

* Le service **SA-Frontend** — sert le frontend ; une application React JavaScript.
* Le service **SA-WebApp** — gère les requêtes pour analyser le sentiment des phrases.
* Le service **SA-Logic** — effectue l'analyse de sentiment.
* Le service **SA-Feedback** — enregistre les commentaires des utilisateurs sur la précision de l'analyse.

De plus, la figure montre un proxy de couche 7 qui effectue un reverse-proxy du trafic en fonction du chemin de la requête. Dans le maillage d'Istio, l'*Ingress Gateway* est le point d'entrée du trafic et le route vers les services.

## Comment exécuter les services sur le maillage

Pour intégrer des services au maillage, vous devez injecter le proxy sidecar dans leurs pods applicatifs. Vous pouvez le faire manuellement ou automatiquement.

Pour l'injection automatique de sidecar, vous étiquetez les espaces de noms avec `istio-injection: enabled`. Après cela, tous les pods déployés dans ces espaces de noms auront le sidecar injecté (en utilisant une fonctionnalité de Kubernetes appelée mutating webhooks qui modifie la définition du pod).

Créez un espace de noms et étiquetez-le pour l'injection automatique.

```bash
kubectl create ns demo
kubectl label ns demo istio-injection=enabled
```

Basculez le contexte kubectl vers l'espace de noms `demo` pour y appliquer les commandes suivantes.

```bash
kubectl config set-context --current --namespace=demo
```

Ensuite, clonez le dépôt contenant les services et la configuration dont nous avons besoin tout au long de l'article :

```bash
git clone https://github.com/rinormaloku/master-istio.git 
cd master-istio
```

Procédez au déploiement des services :

```
kubectl apply -f ./kube
```

Ensuite, vérifiez que le sidecar a été injecté dans chacun des pods de service avec la commande suivante :

```bash
$ kubectl get pods -n demo

NAME                           READY     STATUS    RESTARTS   AGE
sa-feedback-55f5dc4d9c-c9wfv   2/2       Running   0          12m
sa-frontend-558f8986-hhkj9     2/2       Running   0          12m
sa-logic-568498cb4d-2sjwj      2/2       Running   0          12m
sa-logic-568498cb4d-p4f8c      2/2       Running   0          12m
sa-web-app-599cf47c7c-s7cvd    2/2       Running   0          12m
```

Assurez-vous que sous la colonne `READY`, vous voyez la valeur "2/2". Cela montre que les deux conteneurs sont en cours d'exécution : le conteneur de l'application et le proxy sidecar. Visualisé dans la figure ci-dessous, où nous zoomons sur un Pod.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/zoom-into-workload.png)
*Figure 7. Zoom sur un Pod : Le conteneur sidecar est injecté dans le pod*

Nos services sont prêts à recevoir le trafic des utilisateurs finaux. Pour cela, nous devons les exposer ensuite.

## Ingress Gateway – Comment autoriser le trafic dans le maillage

L'Ingress Gateway d'Istio est un proxy spécial à la périphérie du maillage qui autorise le trafic provenant du réseau public et le route vers les services au sein du cluster.

Plus tôt, lorsque nous avons listé les pods dans l'espace de noms d'installation d'Istio, nous l'avons vu à l'état `Running`. Cette passerelle est exposée par un service Kubernetes de type `LoadBalancer`. Nous pouvons l'interroger comme suit :

```bash
$ kubectl get svc -n istio-system -l istio=ingressgateway

NAME                   TYPE           CLUSTER-IP     EXTERNAL-IP
istio-ingressgateway   LoadBalancer   10.96.176.88   <pending>
```

Si vous utilisez `kind`, l'adresse IP externe sera à l'état `Pending`. Cependant, dans les clusters Kubernetes managés, le fournisseur de cloud fournirait un équilibreur de charge avec une adresse IP statique que vous pouvez utiliser pour router le trafic vers la passerelle.

Comme solution de contournement, nous pouvons effectuer une redirection de port vers notre environnement local. Ouvrez un deuxième terminal, exécutez la commande suivante et laissez-la s'exécuter pendant toute la durée de l'article.

```bash
kubectl port-forward -n istio-system svc/istio-ingressgateway 8080:80
```

Désormais, le trafic vers `localhost:8080` sera transféré vers l'Ingress Gateway. Si vous ouvrez le navigateur, tapez cette adresse et appuyez sur entrée, vous découvrirez que la passerelle rejette votre requête. C'est le comportement par défaut de la passerelle.

### API Gateway : autoriser le trafic

Istio définit la ressource personnalisée `Gateway` avec laquelle vous pouvez configurer le type de trafic à autoriser dans le maillage. Par exemple, pour accepter le trafic HTTP sur le port 80, nous utiliserons la configuration ci-dessous :

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
  name: http-gateway
spec:
  selector:
    istio: ingressgateway
  servers:
  - port:
      number: 80
      name: http
      protocol: HTTP
    hosts:
    - "*"
```

La majeure partie de la configuration ci-dessus est explicite, mais ce qui peut ressortir est le sélecteur `istio: ingressgateway`.

La question est : *"Pourquoi en avons-nous besoin ?"*

Un Service Mesh peut avoir plusieurs Ingress Gateways. Habituellement, vous utiliseriez cela dans des environnements multi-tenants. Dans notre cas, nous appliquerons la configuration `Gateway` à l'Ingress Gateway par défaut, qui est étiquetée avec `istio=ingressgateway`.

Appliquez la `Gateway` au cluster :

```bash
kubectl apply -f istio/http-gateway.yaml
```

Après avoir appliqué la configuration `Gateway`, le trafic sur le port 80 sera admis pour tous les hôtes (comme indiqué par l'hôte générique "*").

Ensuite, nous devons configurer ce qu'il faut faire avec le trafic admis.

### API VirtualService : Router le trafic

La ressource `VirtualService` configure le routage du trafic au sein du maillage pour tous les proxys et passerelles. Dans notre cas, nous voulons router le trafic de l'Ingress Gateway vers un ensemble de workloads, comme indiqué ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/istio-ingress-gateway-routing.png)
*L'Ingress Gateway d'Istio route le trafic en fonction de l'en-tête de localisation HTTP*

Décomposons les requêtes qui doivent être routées vers SA-Frontend :

* **Les chemins correspondant exactement à** `/` doivent être routés vers SA-Frontend pour obtenir le fichier Index.html.
* **Les chemins préfixés par** `/static/*` doivent être routés vers SA-Frontend pour obtenir tous les fichiers statiques nécessaires au frontend, comme les feuilles de style en cascade (CSS) et les fichiers JavaScript.
* **Les chemins qui correspondent à l'expression régulière** `'^.*\.(ico|png|jpg)$'` doivent être routés vers SA-Frontend.

Ceci est réalisé avec la configuration suivante :

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: sa-external-services
spec:
  hosts:
  - "*"
  gateways:
  - http-gateway                      # 1
  http:
  - match:
    - uri:
        exact: /
    - uri:
        prefix: /static
    - uri:
        regex: '^.*\.(ico|png|jpg)$'
    route:
    - destination:
        host: sa-frontend             # 2
        port:
          number: 80
```

1. Ce `VirtualService` s'applique aux requêtes arrivant via la `http-gateway` que nous avons définie dans la section précédente.
2. Destination définit le service vers lequel router le trafic.

**NOTE :** La configuration ci-dessus se trouve dans le fichier `vs-route-ingress.yaml`. Elle contient également les règles de routage pour le trafic vers SA-WebApp et SA-Feedback. Elle est omise par souci de brièveté dans la liste ci-dessus.

Appliquez le `VirtualService` au cluster.

```bash
kubectl apply -f istio/vs-route-ingress.yaml
```

Le plan de contrôle propage la configuration à la passerelle en quelques secondes. Après cela, vous pouvez accéder à l'application à l'adresse [http://localhost:8080/](http://localhost:8080/), à condition de toujours effectuer la redirection de port de l'Ingress Gateway d'Istio vers votre environnement local.

Ouvrez le navigateur à cette adresse. Vous verrez l'application, comme le montre l'image ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/sentiment-analysis.gif)

La figure ci-dessous montre comment ces deux ressources configurent l'Ingress Gateway. La ressource `Gateway` la configure pour autoriser le trafic et le `VirtualService` configure l'endroit où router le trafic admis.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/gateway-vs-in-context.png)
*Configuration de l'Ingress Gateway d'Istio pour autoriser et router le trafic*

Hourra ! Nous avons réussi à faire fonctionner les services. Nous avons injecté le sidecar et routé le trafic des utilisateurs finaux vers ceux-ci.

Vous pourriez vous demander : *"Pourquoi tout ce foin autour de l'exécution de workloads dans le maillage ? Après tout, le routage du trafic vers les workloads à l'aide d'un routage basé sur le chemin peut être effectué avec n'importe quel contrôleur d'ingress de couche 7."*

Nous y répondrons ensuite, lorsque nous montrerons les avantages en matière de sécurité et d'observabilité que vous avez acquis. Alors, commençons.

## Observabilité

Le proxy sidecar d'Istio — à savoir le proxy Envoy — génère des journaux d'accès, des métriques et des traces pour tout le trafic entrant et sortant. Les métriques fournissent des informations sur le fonctionnement du système et aident à répondre à des questions telles que : Le système est-il sain ? Quel est le taux de réussite d'un service ? Et ainsi de suite.

Générer les métriques n'est que la moitié de l'histoire. L'autre moitié consiste à collecter et à visualiser les informations d'une manière qui incite à l'action. Nous allons utiliser les add-ons Istio que nous avons installés plus tôt :

* **Prometheus** pour collecter les métriques.
* **Grafana** pour les visualiser.
* **Jaeger** pour dénicher les traces.
* **Kiali** rassemble toutes les données de télémétrie.

Mais que se passe-t-il si vous avez déjà des outils d'observabilité dans votre organisation ? Encore mieux, vous pouvez intégrer Istio avec ceux-ci :)

### Grafana : Visualiser les métriques

Grafana visualise les métriques collectées par Prometheus. Ouvrez le tableau de bord Grafana et voyons ce que nous obtenons par défaut.

```bash
istioctl dashboard grafana
```

La commande ci-dessus effectuera une redirection de port de Grafana vers votre environnement local et l'ouvrira dans votre navigateur par défaut. Ensuite, naviguez vers "Istio" > "Istio Service Dashboard" et filtrez la sortie en utilisant le menu déroulant "Service" et sélectionnez le service "sa-webapp".

Si les graphiques de votre côté semblent un peu vides, générez du trafic en exécutant la commande ci-dessous :

```bash
while true; do \
  curl -i http://localhost:8080/sentiment \
  -H "Content-type: application/json" \
  -d '{"sentence": "I love yogobella"}'; \
  sleep .$RANDOM; done
```

Laissez cette commande s'exécuter pour le reste de l'article, car nous aurons également besoin de l'afflux de trafic par la suite.

Ci-dessous, nous visualisons les métriques du service `sa-webapp`.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/grafana-dashboard.png)
*Grafana : Visualisation des métriques pour le service sa-webapp*

Prometheus et Grafana nous permettent de comprendre la santé, les performances et les améliorations ou dégradations de nos services au fil du temps. C'est à vous d'approfondir l'étude des graphiques et des informations qu'ils visualisent.

Ensuite, nous allons examiner le traçage des requêtes lorsqu'elles passent à travers les services.

### Jaeger : Dénicher les traces d'une requête

Il est raisonnable de se demander : "Pourquoi traçons-nous les requêtes *de nos jours* ? Nous ne le faisions pas pour les monolithes ?" — passer aux microservices résout certaines difficultés, bien que par inadvertance, cela apporte certaines des propriétés inhérentes aux systèmes distribués qui nécessitent d'autres solutions.

Par exemple, la propriété d'être distribué rend la localisation des pannes relativement délicate.

Imaginez qu'un utilisateur final reçoive une requête échouée — "quelle en était la cause ?" Pour localiser la panne, vous devriez vérifier tous les services qui ont participé au traitement de la requête.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/localizing-failures-is-hard.png)

Sans outils appropriés, la seule option disponible est d'enlever votre chapeau d'*Ingénieur* et de mettre votre chapeau de *Détective*. Ensuite, vous devriez reconstituer l'histoire de la "*requête échouée*" en interrogeant tous les journaux de service, en filtrant par horodatage et en essayant de donner un sens à toutes les données. Ensuite, vous arriveriez lentement mais sûrement au fond des choses et trouveriez le coupable !

Jouer au détective peut être une activité amusante la première fois — mais cela deviendra vite rébarbatif car les pannes sont monnaie courante. Nous avons besoin d'outils efficaces pour les localiser dans les systèmes distribués.

**Jaeger est un tel outil.**

Jaeger vient du mot allemand signifiant "chasseur" (écrit Jäger). Cela implique de "chasser les pannes". Cependant, je préfère de loin mon analogie avec le détective. Ainsi, rayez Jaeger ❌ et remplacez-le par **Inspecteur Gadget** ✅

Pour tracer des requêtes sans Istio, vous devriez instrumenter tous vos services pour générer des traces et les envoyer à **Inspecteur Gadget**. *(ouais… je continue sur ma lancée* 🤣)

Au contraire, avec Istio, les proxys sidecar génèrent des en-têtes de trace (sous forme d'en-têtes HTTP) et les envoient à Inspecteur Gadget (*c'est la dernière fois, je le promets* 😜). Ceci est fait par chaque service qui possède le proxy sidecar.

Vous n'avez qu'à **mettre à jour vos services pour propager les en-têtes de trace générés aux services amont**. Sinon, chaque proxy génère à nouveau les en-têtes. Et lorsque les traces sont assemblées, cela ne nous donnerait pas une image complète de la requête.

Le diagramme ci-dessous visualise le processus.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/how-traces-are-generated.png)
*Comment les informations de traçage sont générées et envoyées aux serveurs de traces*

Faites attention à l'étape 4 du diagramme. Il est de la responsabilité de l'application de transmettre les en-têtes de traçage à l'amont.

La transmission des en-têtes de traçage est critique, car le proxy suivant récupérera les en-têtes existants et comprendra qu'il s'agit de la suite d'une requête déjà tracée. Ainsi, il réutilisera les en-têtes de traçage (tels que le `x-request-id`), puis il ajoutera les données supplémentaires qu'il enregistre. Les en-têtes de trace sont utilisés pour combiner toutes les informations d'une requête dans Jaeger.

Ouvrez le tableau de bord Jaeger et voyez comment les traces montrent toute l'étendue d'une requête.

```bash
istioctl dashboard jaeger
```

La commande ci-dessus effectuera une redirection de port de Jaeger vers votre environnement local et l'ouvrira dans votre navigateur par défaut.

Explorez l'interface utilisateur de Jaeger et examinez les requêtes individuelles. Par exemple, l'image ci-dessous montre les traces d'une requête pour analyser le sentiment d'une phrase.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/jaeger-request-trace.png)
*Le flux complet de la requête à travers le maillage*

L'image montre comment la requête a commencé à l'Ingress Gateway (c'est le premier contact avec un workload du Service Mesh). Ensuite, la requête a été routée vers `sa-webapp` et `sa-logic`, respectivement.

**NOTE :** Pour en savoir plus sur les en-têtes que votre application doit propager et les bibliothèques clientes pour cela, consultez la [FAQ sur le traçage distribué d'Istio](https://istio.io/latest/about/faq/distributed-tracing) et lisez la réponse à ["What is required for distributed tracing with Istio"](https://istio.io/latest/about/faq/distributed-tracing/#how-to-support-tracing)?"

Les traces clarifient l'endroit où la requête a échoué et quel service a renvoyé l'erreur, et ainsi de suite. Mais nous en apprenons davantage sur l'échec en utilisant les journaux d'accès du proxy et les journaux de l'application.

### Journaux d'accès (Access logs)

Envoy enregistre chaque requête individuelle sous forme de journaux d'accès. Imprimons une entrée de journal du service `sa-webapp` pour voir les données enregistrées.

```bash
$ kubectl logs deploy/sa-webapp -c istio-proxy | tail -n 1

[2022-04-18T12:09:44.091Z] "POST /sentiment HTTP/1.1" 200 - via_upstream - "-" 32 46 5 5 "10.244.0.6" "curl/7.74.0" "bfb9e6e5-2968-9b25-b256-f0917aa6b0bb" "localhost:8080" "10.244.0.16:8080" inbound|8080|| 127.0.0.6:51819 10.244.0.16:8080 10.244.0.6:0 outbound_.80_._.sa-webapp.demo.svc.cluster.local default
```

Cela ressemble beaucoup à du charabia, n'est-ce pas ? C'est le format TEXTE, où chaque information est séparée par un espace. Vous pouvez apprendre ce que signifie chaque champ séparé par un espace en affichant le format du journal d'accès — obtenu avec la commande ci-dessous :

```bash
$ istioctl pc all deploy/sa-webapp -o json | \
    grep log_format -A 2 | tail -n 2

"text_format_source": {
  "inline_string": "[%START_TIME%] \"%REQ(:METHOD)% %REQ(X-ENVOY-ORIGINAL-PATH?:PATH)% %PROTOCOL%\" %RESPONSE_CODE% %RESPONSE_FLAGS% %RESPONSE_CODE_DETAILS% %CONNECTION_TERMINATION_DETAILS% \"%UPSTREAM_TRANSPORT_FAILURE_REASON%\" %BYTES_RECEIVED% %BYTES_SENT% %DURATION% %RESP(X-ENVOY-UPSTREAM-SERVICE-TIME)% \"%REQ(X-FORWARDED-FOR)%\" \"%REQ(USER-AGENT)%\" \"%REQ(X-REQUEST-ID)%\" \"%REQ(:AUTHORITY)%\" \"%UPSTREAM_HOST%\" %UPSTREAM_CLUSTER% %UPSTREAM_LOCAL_ADDRESS% %DOWNSTREAM_LOCAL_ADDRESS% %DOWNSTREAM_REMOTE_ADDRESS% %REQUESTED_SERVER_NAME% %ROUTE_NAME%\n"
```

Ainsi, la première entrée est `[%START_TIME%]` qui, d'après le journal listé précédemment, est la valeur `[2022-04-18T12:09:44.091Z]`, et ainsi de suite. Vous pouvez en savoir plus sur les journaux d'accès dans ce document Istio : "[Envoy Access Logs](https://istio.io/latest/docs/tasks/observability/logs/access-log/#default-access-log-format)".

### Comment personnaliser le format du journal d'accès

Vous pouvez personnaliser le format du journal d'accès. Par exemple, la commande suivante met à jour l'installation d'Istio pour imprimer les journaux au format JSON.

```bash
istioctl install --set profile=demo \
    --set meshConfig.accessLogEncoding="JSON"
```

Au format JSON, les données du journal ont des valeurs associées à des clés qui expliquent la signification de la valeur.

### Kiali – La console pour le Service Mesh d'Istio

Kiali est une console puissante pour Istio. Elle utilise les données de télémétrie pour visualiser le trafic de service à service. Elle corrèle les informations de télémétrie collectées, telles que les métriques, les traces, ainsi que les journaux d'accès et d'application. Ainsi, le débogage des problèmes d'application devient un jeu d'enfant.

**NOTE :** Kiali dispose d'une liste de validateurs qui découvrent également les mauvaises configurations au sein du maillage. Ceci, cependant, dépasse le cadre de cet article. En savoir plus sur les [validateurs Kiali](https://kiali.io/docs/features/validations/).

Ouvrez le tableau de bord Kiali avec la commande suivante :

```bash
istioctl dashboard kiali
```

La figure ci-dessous montre les informations visualisées dans le tableau de bord.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/kiali-dashboard-annotated.png)

Et ensuite, nous passons à ma fonctionnalité préférée : la corrélation des métriques et des traces, comme indiqué ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/correlation-requests-and-traces.png)

La corrélation des métriques et des traces permet aux équipes applicatives de trouver facilement la requête la plus lente et le chemin qu'elle a emprunté à travers les services. De cette façon, il est facile de découvrir les goulots d'étranglement sur lesquels les équipes peuvent se concentrer pour améliorer les performances de leur application.

**CONSEIL :** Consultez la documentation officielle pour en savoir plus sur la [corrélation des métriques](https://kiali.io/docs/features/tracing/#metric-correlation).

C'est ainsi que nous concluons la section sur l'observabilité de cet article. Bien sûr, tous les outils présentés ont plus d'ampleur et de profondeur. Cependant, la couverture ici est suffisante pour vous donner une idée de l'observabilité que vous gagnez sur le système lors de l'adoption de Service Meshes.

## Gestion du trafic – Déploiements Canary

Le fait que le trafic de service à service soit intermédié par des proxys de couche 7 permet des capacités complexes de gestion du trafic. À titre d'exemple, nous l'utilisons déjà lorsque nous routons les requêtes en fonction de l'en-tête de chemin dans l'Ingress Gateway.

Nous pouvons baser les décisions de routage sur n'importe quelle autre information HTTP. Voyons ensuite comment les capacités de gestion du trafic nous permettent de sécuriser les déploiements.

### Comment sécuriser la livraison continue (Continuous Delivery)

Dans toute l'industrie technologique, nous avons appris de manière empirique que les pannes de service les plus fréquentes surviennent pendant les jours ouvrables — et rarement le week-end. C'est parce que, pendant la semaine, des changements sont introduits dans le système. Nous ne pouvons pas éviter les changements, mais nous devons trouver des moyens de rendre leur livraison plus sûre.

La livraison continue peut être pensée en deux phases :

1. **Phase de déploiement** : Déployer l'application.
2. **Phase de publication (Release)** : Envoyer le trafic des utilisateurs finaux vers l'application.

#### Modèles de livraison

La "Phase de déploiement" est gérée par la plateforme. Par exemple, c'est ce pour quoi nous utilisons les Deployments Kubernetes.

La "Phase de publication" est celle où les capacités de gestion du trafic d'Istio s'avèrent utiles et permettent la mise en œuvre des modèles de livraison suivants :

* **Déploiements Canary** — Valider le nouveau déploiement en ne routant qu'une fraction du trafic vers la dernière version. Valider ensuite les changements et ne le publier à tous les utilisateurs qu'après cela.
* **Déploiements progressifs** — Une variante des déploiements canary où vous augmentez progressivement le pourcentage de trafic envoyé vers la nouvelle version.
* **Dark launch** — Pas précisément pour publier des logiciels en toute sécurité, mais pour les publier à un sous-ensemble d'utilisateurs (tels que des utilisateurs bêta) et vérifier comment les changements sont reçus.
* **Mise en miroir du trafic (Traffic mirroring)** — Reproduit le trafic réel des utilisateurs vers la nouvelle version de l'application et ignore les réponses.

Dans cet article, nous allons montrer le modèle de déploiement canary pour valider la nouvelle version de l'application avant de la publier au trafic réel. Nous couvrons plus de modèles de déploiement dans le livre [Istio in Action.](https://livebook.manning.com/book/istio-in-action/chapter-5/73#:~:text=v1%20of%20catalog-,5.2.5%20Routing%20specific%20requests%20to%20v2,-Maybe%20we%20wish)

### Déploiements Canary avec Istio

Lors du déploiement d'une autre version d'une application dans Kubernetes, elle reçoit immédiatement du trafic, ce qui signifie que nos utilisateurs sont routés vers le nouveau service. Ce n'est pas ce que nous voulons !

Nous voulons en fait que le trafic ne soit routé que vers la première version, même après le déploiement de la deuxième version de l'application (et plus tard, nous décidons de publier la deuxième version au trafic des utilisateurs finaux).

Dans Istio, la distinction entre les versions se fait à l'aide de l'API DestinationRule. Avec la règle de destination ci-dessous, nous définissons les sous-ensembles (subsets) suivants :

* Sous-ensemble `v1` — cible les pods avec l'étiquette `version: v1`.
* Sous-ensemble `v2` — cible les pods avec l'étiquette `version: v2`.

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: DestinationRule
metadata:
  name: sa-logic
spec:
  host: sa-logic
  subsets:
  - name: v1
    labels:
      version: v1
  - name: v2
    labels:
      version: v2
```

Appliquons-le au cluster pour que cette distinction existe.

```bash
kubectl apply -f istio/sa-logic-dr.yaml
```

Ensuite, créons un VirtualService qui configure les proxys de service pour router le trafic uniquement vers le sous-ensemble `v1` pour tout trafic ciblant le service `sa-logic` :

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: sa-logic
spec:
  hosts:
  - sa-logic
  http:
  - route:
    - destination:
        host: sa-logic
        subset: v1
      weight: 100
```

Appliquez au cluster en exécutant la commande suivante :

```bash
kubectl apply -f istio/sa-logic-vs.yaml
```

Désormais, le déploiement de la deuxième version du service ne la publiera pas au trafic des utilisateurs finaux.

```bash
kubectl apply -f kube/canary/sa-logic-v2.yaml
```

Vérifiez que tout le trafic est routé vers le sous-ensemble `v1` à l'aide du tableau de bord Kiali Graph (voir figure ci-dessous).

![Image](https://www.freecodecamp.org/news/content/images/2022/05/sa-logic-v1-only-kiali.png)
*Taux de réussite du sous-ensemble v1*

Ensuite, envoyons seulement 10 % du trafic des utilisateurs finaux vers la nouvelle version de `sa-logic`, comme visualisé dans l'image ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/subsets-istio-config.png)
*Comment Istio configure le routage vers les sous-ensembles*

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: sa-logic
spec:
  hosts:
  - sa-logic
  http:
  - route:
    - destination:
        host: sa-logic
        subset: v1
      weight: 90
    - destination:
        host: sa-logic
        subset: v2
      weight: 10
```

Appliquez-le au cluster.

```bash
kubectl apply -f istio/sa-logic-vs-canary.yaml
```

Après avoir publié la nouvelle version au trafic des utilisateurs finaux, vous pouvez la surveiller et la valider. Utilisez les outils d'observabilité que nous avons explorés plus tôt.

Par exemple, après avoir appliqué le changement, nous pouvons observer dans le graphique Kiali le taux de réussite et d'erreur des sous-ensembles.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/sa-logic-v2-errors-kiali.png)

Saperlipopette ! Nous avons une augmentation du taux d'erreur. Mettons à jour le VirtualService pour rediriger tout le trafic vers `v1`, qui n'avait aucune erreur.

```bash
kubectl apply -f istio/sa-logic-vs.yaml
```

Si vous vérifiez à nouveau les graphiques Kiali, vous constaterez que 100 % du trafic est routé vers la version 1, qui n'avait aucune erreur.

**Résumé :** Les publications dans Kubernetes sont toujours des "big bangs". Vous avez un changement que vous voulez expédier, et s'il contient des bugs, il impacte tous vos utilisateurs.

Mais Istio utilise les proxys de service pour prendre des décisions de routage fines qui, lorsqu'elles sont utilisées, sécurisent les publications.

Ensuite, examinons les fonctionnalités de sécurité d'Istio — ça devient passionnant !

## Sécurité Istio

Je n'aurais jamais (au grand jamais) cru que la sécurité serait un sujet qui m'enthousiasmerait. Que pourrait bien faire Istio sur le spectre technologique pour rendre ce sujet divertissant ? Et plus important encore, pourquoi devriez-vous être enthousiaste vous aussi ?

**La réponse est simple :** Istio décharge les responsabilités de sécurité de notre code applicatif vers la plateforme (plus précisément, les proxys Envoy). Ainsi, lorsque le trafic atteint nos applications, il est déjà authentifié et autorisé.

Dans les sections suivantes, nous montrerons comment authentifier et autoriser à la fois le trafic de service à service et le trafic des utilisateurs finaux à l'aide d'Istio.

Mais d'abord, assurons-nous d'avoir une compréhension commune de l'authentification et de l'autorisation :

* **L'authentification** se produit lorsqu'un client ou un serveur prouve son identité (c'est-à-dire répond à la question "qui" il est) en utilisant quelque chose qu'il possède, comme un certificat et/ou un JWT.
* **L'autorisation** est le processus consistant à autoriser ou à rejeter les actions des utilisateurs authentifiés.

### Auto mTLS : authentification de service à service

Istio utilise le *Secure Production Identity Framework for Everyone* — également connu sous le nom de SPIFFE — pour délivrer une identité aux workloads.

L'explication du fonctionnement de SPIFFE dépasse le cadre de cet article. Mais il suffit de savoir qu'Istio forge l'identité du workload sous la forme d'un certificat x509.

Istio utilise le `serviceaccount` Kubernetes attribué au Pod Kubernetes par Kubernetes lui-même comme source d'identité. Si votre déploiement ne spécifie pas de compte de service, le compte de service `default` lui est attribué.

**NOTE :** Pour ceux qui souhaitent en savoir plus sur SPIFFE, nous lui avons dédié l'["appendix C. Istio security: SPIFFE"](https://livebook.manning.com/book/istio-in-action/appendix-c/).

Le certificat forgé contient des métadonnées de workload encodées, telles que l'espace de noms, le compte de service, etc. Les proxys utilisent ce certificat pour initier des connexions mutuellement authentifiées (mTLS). Vous pouvez trouver le certificat dans la configuration d'Envoy.

La commande suivante interroge la configuration d'Envoy, la filtre pour obtenir la sortie dont nous avons besoin et décode le certificat. Vous devez installer [step-cli](https://smallstep.com/docs/step-cli/installation) et [jq](https://stedolan.github.io/jq/download/) pour l'exécuter.

```bash
istioctl proxy-config all deploy/sa-webapp -o json | \
  jq -r '.. |."secret"? | select(.name == "default")' | \
  jq -r '.tls_certificate.certificate_chain.inline_bytes' | \
  base64 -d - | step certificate inspect
```

Ma sortie est présentée ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/SVID.png)

Nous avons mentionné que les certificats sont utilisés pour chiffrer le trafic et le protéger contre les attaques de l'homme du milieu (man-in-the-middle). Vérifions cela ensuite.

#### Le trafic de service à service est chiffré

Pour savoir si le trafic est chiffré, nous devons capturer le trafic passant par le pod. Pour cela, nous allons exécuter un conteneur de débogage au sein du pod avec l'image suivante `nicolaka/netshoot` (l'exécution de conteneurs de débogage nécessite la version 1.23 de Kubernetes).

L'image `netshoot` contient de nombreux utilitaires réseau, dont `tcpdump`, un utilitaire de capture réseau que nous allons utiliser.

Exécutez le conteneur de débogage avec la commande suivante :

```bash
# Interroger le nom du pod sa-webapp
POD_NAME=$(kubectl get pods -l app=sa-webapp -o jsonpath={.items..metadata.name} | cut -d ' ' -f1)

# Exécuter un conteneur de débogage avec l'utilitaire tcpdump
kubectl debug -q -i $POD_NAME --image=nicolaka/netshoot -- \
  tcpdump -l --immediate-mode -vv -s 0 '(((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12]&0xf0)>>2)) != 0)'
```

Cela peut prendre une minute ou deux (*voire plus*) jusqu'à ce que le conteneur de débogage soit téléchargé et exécuté. Si vous exécutez toujours des requêtes continues vers `sa-webapp`, vous verrez beaucoup de trafic capturé. Cependant, vous ne pourrez en tirer aucune information. Ce qui est une bonne chose, car **c'est l'idée même — c'est chiffré. Tada !** 🥳

Sachez que cet avantage ne s'étend pas aux workloads hérités, comme nous le verrons ensuite.

#### Le trafic provenant des workloads hérités est en clair

Commencez par exécuter un workload hérité qui s'exécute indéfiniment. Nous allons créer un nouvel espace de noms et nous ne l'étiquetterons pas pour l'injection automatique de sidecar. Ainsi, le workload n'aura pas de sidecar injecté, il n'aura pas d'identité et il ne pourra pas s'authentifier mutuellement.

```bash
kubectl create ns legacy
kubectl -n legacy run workload --image=radial/busyboxplus:curl -- tail -f /dev/null
```

Lorsque le Pod est en cours d'exécution, exécutez une requête cURL depuis le workload hérité vers le workload `sa-web-app`.

```bash
kubectl -n legacy exec workload -- \
  curl -i http://sa-webapp.demo/sentiment \
  -H "Content-type: application/json" \
  -d '{"sentence": "I love yogobella"}'
```

En regardant la sortie de la commande `tcpdump` s'exécutant dans le pod `sa-webapp`, vous verrez la réponse en clair, comme indiqué ci-dessous.

```bash
HTTP/1.1 200 OK
content-type: application/json;charset=UTF-8
date: Mon, 25 Apr 2022 12:14:02 GMT
x-envoy-upstream-service-time: 13
server: istio-envoy
x-envoy-decorator-operation: sa-web-app.demo.svc.cluster.local:80/*
transfer-encoding: chunked

2e
{"sentence":"I love yogobella","polarity":0.5}
```

Supposons que les données soient sensibles, telles que des mots de passe, des JWT (qui peuvent être utilisés dans des attaques par rejeu), etc. Cela représente un vecteur d'attaque dangereux et un risque pour votre organisation.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/mtls-and-non-mtls-traffic.png)

Istio nous donne les outils pour empêcher les workloads du maillage de recevoir du trafic en clair.

### PeerAuthentication – comment améliorer les paramètres de sécurité par défaut

Par défaut, Istio configure les proxys de service pour utiliser le mode *mTLS permissive*, ce qui signifie que le trafic non authentifié est autorisé.

C'est un paramètre par défaut raisonnable, car il permet une migration progressive des services dans le maillage sans causer d'interruption de service.

Une fois que les workloads ont été migrés dans le maillage, il est recommandé de basculer le mode mTLS pour exiger strictement un trafic mutuellement authentifié. Vous pouvez le faire avec la configuration `PeerAuthentication` suivante.

```yaml
apiVersion: "security.istio.io/v1beta1"
kind: "PeerAuthentication"
metadata:
  name: "default"
  namespace: "istio-system"
spec:
  mtls:
    mode: STRICT
```

Cette configuration s'applique à tous les workloads, car Istio utilise une convention selon laquelle la configuration dans l'espace de noms d'installation d'Istio (dans notre cas `istio-system`) s'applique globalement. Cependant, elle peut être écrasée par une configuration *à l'échelle de l'espace de noms* ou une configuration *spécifique au sidecar*.

En savoir plus sur la ["Portée, héritage et surcharges"](https://istio.io/latest/docs/tasks/observability/telemetry/#scope-inheritance-and-overrides) de la configuration d'Istio. L'explication concerne l'API Telemetry mais s'applique de la même manière à `PeerAuthentication` et aux autres API d'Istio.

Appliquez la configuration d'authentification des pairs au cluster.

```bash
kubectl apply -f istio/security/peer-authentication.yaml
```

Vérifiez que le trafic provenant des workloads hérités est rejeté.

```bash
$ kubectl -n legacy exec workload -- \
    curl -i -Ss http://sa-webapp.demo/sentiment \
    -H "Content-type: application/json" \
    -d '{"sentence": "I love yogobella"}'

curl: (56) Recv failure: Connection reset by peer
command terminated with exit code 56
```

La commande cURL échoue avec l'erreur `Recv failure: Connection reset by peer` car le proxy de service n'accepte pas la connexion non authentifiée.

### Comment autoriser le trafic de service à service

L'authentification mutuelle des services et le chiffrement du trafic entre eux protègent nos données en transit.

*Mais que se passe-t-il lorsqu'un utilisateur malveillant s'empare de l'identité de l'un des workloads ?*

**L'utilisateur malveillant pourrait s'authentifier auprès de chaque service et interroger des données sensibles.**

Cependant, si nous adhérons au principe du moindre privilège, nous réduisons l'accès de chaque workload à ce qui est uniquement nécessaire à ses fonctions. Ainsi, nous réduisons la portée des dommages lorsqu'une identité est volée à ce qu'elle était autorisée à consulter.

Dans Istio, nous contrôlons l'accès à l'aide de politiques d'autorisation (authorization policies). Fondamentalement, une fois que les workloads s'authentifient mutuellement et que nous connaissons leur identité, à savoir "qui" c'est, nous pouvons alors appliquer des politiques, c'est-à-dire spécifier quelles actions l'identité est autorisée à effectuer.

Je vous laisse cela comme exercice facultatif. Vous devriez implémenter des politiques d'autorisation afin que le maillage adhère au principe du moindre privilège.

Istio propose un [exemple rapide](https://istio.io/latest/docs/tasks/security/authorization/authz-http/) pour vous mettre sur la bonne voie, et vous trouverez utiles les descriptions détaillées de la [référence de l'API AuthorizationPolicy](https://istio.io/latest/docs/reference/config/security/authorization-policy/).

*Résumé des accès dont chaque service a besoin :*

* L'`istio-ingressgateway` peut accéder à `sa-frontend`, `sa-feedback` et `sa-web-app`.
* Le `sa-web-app` peut accéder au service `sa-logic`.
* Tout autre accès doit être interdit.

### Authentification de l'utilisateur final

Istio authentifie les requêtes des utilisateurs finaux en utilisant des JWT comme moyen d'authentification.

Pour que les utilisateurs finaux reçoivent un jeton Web JSON, nous avons besoin d'un fournisseur d'identité (IdP). Nous utiliserons Keycloak comme IdP. Cependant, toute solution implémentant la norme OpenID Connect Discovery (OIDC) fonctionnera de la même manière.

#### Exécuter Keycloak dans le cluster

Commencez par créer un espace de noms et y déployer `keycloak`.

```bash
kubectl create ns keycloak
kubectl -n keycloak apply -f kube/idp/keycloak.yaml

# attendre le déploiement
kubectl -n keycloak rollout status deploy/keycloak
```

Attendez que *keycloak* soit opérationnel. Ensuite, créez une application cliente pour représenter l'application monopage `sa-frontend`. De plus, ajoutez les utilisateurs listés dans le tableau ci-dessous.

<table style="box-sizing: border-box; border-spacing: 0px; border-collapse: collapse; margin-top: 0px; margin-bottom: 16px; display: block; width: max-content; max-width: 100%; overflow: auto;"><thead style="box-sizing: border-box;"><tr style="box-sizing: border-box; background-color: var(--color-canvas-default); border-top: 1px solid var(--color-border-muted);"><th style="box-sizing: border-box; padding: 6px 13px; font-weight: 600; border: 1px solid var(--color-border-default);">Nom d'utilisateur</th><th style="box-sizing: border-box; padding: 6px 13px; font-weight: 600; border: 1px solid var(--color-border-default);">Mot de passe</th><th style="box-sizing: border-box; padding: 6px 13px; font-weight: 600; border: 1px solid var(--color-border-default);">Groupe</th><th style="box-sizing: border-box; padding: 6px 13px; font-weight: 600; border: 1px solid var(--color-border-default);">Type d'utilisateur</th></tr></thead><tbody style="box-sizing: border-box;"><tr style="box-sizing: border-box; background-color: var(--color-canvas-default); border-top: 1px solid var(--color-border-muted);"><td style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-border-default);"><p dir="auto" style="box-sizing: border-box; margin-top: 0px; margin-bottom: 16px;">user</p></td><td style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-border-default);"><p dir="auto" style="box-sizing: border-box; margin-top: 0px; margin-bottom: 16px;">password</p></td><td style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-border-default);"><p dir="auto" style="box-sizing: border-box; margin-top: 0px; margin-bottom: 16px;">users</p></td><td style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-border-default);"><p dir="auto" style="box-sizing: border-box; margin-top: 0px; margin-bottom: 16px;">regular</p></td></tr><tr style="box-sizing: border-box; background-color: var(--color-canvas-subtle); border-top: 1px solid var(--color-border-muted);"><td style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-border-default);"><p dir="auto" style="box-sizing: border-box; margin-top: 0px; margin-bottom: 16px;">beta</p></td><td style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-border-default);"><p dir="auto" style="box-sizing: border-box; margin-top: 0px; margin-bottom: 16px;">password</p></td><td style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-border-default);"><p dir="auto" style="box-sizing: border-box; margin-top: 0px; margin-bottom: 16px;">users</p></td><td style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-border-default);"><p dir="auto" style="box-sizing: border-box; margin-top: 0px; margin-bottom: 16px;">beta</p></td></tr><tr style="box-sizing: border-box; background-color: var(--color-canvas-default); border-top: 1px solid var(--color-border-muted);"><td style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-border-default);"><p dir="auto" style="box-sizing: border-box; margin-top: 0px; margin-bottom: 16px;">moderator</p></td><td style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-border-default);"><p dir="auto" style="box-sizing: border-box; margin-top: 0px; margin-bottom: 16px;">password</p></td><td style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-border-default);"><p dir="auto" style="box-sizing: border-box; margin-top: 0px; margin-bottom: 16px;">moderator</p></td><td style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-border-default);"><p dir="auto" style="box-sizing: border-box; margin-top: 0px; margin-bottom: 16px;">regular</p></td></tr></tbody></table>

> NOTE : Les attributs `group` et `usertype` sont ajoutés en tant que revendications (claims) dans le JWT après l'authentification.

La création de l'application cliente et des utilisateurs est automatisée avec le script ci-dessous. Cela vous évite de passer par l'interface utilisateur de Keycloak et de les créer manuellement.

```bash
# 1. Redirection de port vers l'environnement local
kubectl port-forward svc/keycloak -n keycloak  8081:8080 &
PID=$!
sleep 2

# 2. Créer le client et les utilisateurs
export KEYCLOAK_URL=http://localhost:8081/auth

export KEYCLOAK_TOKEN=$(curl -d "client_id=admin-cli" -d "username=admin" -d "password=admin" -d "grant_type=password" "$KEYCLOAK_URL/realms/master/protocol/openid-connect/token" | jq -r .access_token)
echo $KEYCLOAK_TOKEN

# Créer le jeton initial pour enregistrer le client
read -r client token <<<$(curl -H "Authorization: Bearer ${KEYCLOAK_TOKEN}" -X POST -H "Content-Type: application/json" -d '{"expiration": 0, "count": 1}' $KEYCLOAK_URL/admin/realms/master/clients-initial-access | jq -r '[.id, .token] | @tsv')

# Enregistrer le client
read -r id secret <<<$(curl -X POST -d "{ \"clientId\": \"sa-frontend\", \"implicitFlowEnabled\": true }" -H "Content-Type:application/json" -H "Authorization: bearer ${token}" ${KEYCLOAK_URL}/realms/master/clients-registrations/default| jq -r '[.id, .secret] | @tsv')

# Ajouter les URI de redirection autorisées
curl -H "Authorization: Bearer ${KEYCLOAK_TOKEN}" -X PUT \
  -H "Content-Type: application/json" -d "{\"serviceAccountsEnabled\": true, \"directAccessGrantsEnabled\": true, \"authorizationServicesEnabled\": true, \"redirectUris\": [\"http://localhost:8080/\"]}" $KEYCLOAK_URL/admin/realms/master/clients/${id}

# Ajouter l'attribut de groupe dans le JWT renvoyé par Keycloak
curl -H "Authorization: Bearer ${KEYCLOAK_TOKEN}" -X POST -H "Content-Type: application/json" -d '{"name": "group", "protocol": "openid-connect", "protocolMapper": "oidc-usermodel-attribute-mapper", "config": {"claim.name": "group", "jsonType.label": "String", "user.attribute": "group", "id.token.claim": "true", "access.token.claim": "true"}}' $KEYCLOAK_URL/admin/realms/master/clients/${id}/protocol-mappers/models

# Ajouter l'attribut de type d'utilisateur dans le JWT renvoyé par Keycloak
curl -H "Authorization: Bearer ${KEYCLOAK_TOKEN}" -X POST -H "Content-Type: application/json" -d '{"name": "usertype", "protocol": "openid-connect", "protocolMapper": "oidc-usermodel-attribute-mapper", "config": {"claim.name": "usertype", "jsonType.label": "String", "user.attribute": "usertype", "id.token.claim": "true", "access.token.claim": "true"}}' $KEYCLOAK_URL/admin/realms/master/clients/${id}/protocol-mappers/models

# Créer l'utilisateur régulier
curl -H "Authorization: Bearer ${KEYCLOAK_TOKEN}" -X POST -H "Content-Type: application/json" -d '{"username": "user", "email": "user@acme.com", "enabled": true, "attributes": {"group": "users", "usertype": "regular"}, "credentials": [{"type": "password", "value": "password", "temporary": false}]}' $KEYCLOAK_URL/admin/realms/master/users

# Créer l'utilisateur bêta
curl -H "Authorization: Bearer ${KEYCLOAK_TOKEN}" -X POST -H "Content-Type: application/json" -d '{"username": "beta", "email": "beta@acme.com", "enabled": true, "attributes": {"group": "users", "usertype": "beta"}, "credentials": [{"type": "password", "value": "password", "temporary": false}]}' $KEYCLOAK_URL/admin/realms/master/users

# Créer l'utilisateur modérateur
curl -H "Authorization: Bearer ${KEYCLOAK_TOKEN}" -X POST -H "Content-Type: application/json" -d '{"username": "moderator", "email": "moderator@acme.com", "enabled": true, "attributes": {"group": "moderator", "usertype": "regular"}, "credentials": [{"type": "password", "value": "password", "temporary": false}]}' $KEYCLOAK_URL/admin/realms/master/users

# 3. Arrêter la redirection de port
kill $PID
```

Une fois que cela est terminé avec succès, vous pourrez passer à la section suivante.

### Comment exposer le service Keycloak

La norme OIDC permet aux applications clientes d'identifier les utilisateurs finaux. L'application cliente commence le processus en redirigeant les utilisateurs vers le serveur d'authentification. Tout d'abord, les utilisateurs s'authentifient, puis le serveur d'authentification renvoie l'utilisateur à l'application cliente avec un jeton représentant son identité.

Le serveur d'authentification doit être accessible aux utilisateurs finaux. C'est pourquoi nous devons également exposer `keycloak` via l'Ingress Gateway d'Istio.

Le VirtualService mis à jour qui configure le routage du trafic vers Keycloak peut être appliqué avec la commande ci-dessous. N'hésitez pas à consulter le fichier pour en savoir plus sur les changements.

```bash
kubectl apply -f istio/vs-route-ingress-keycloak.yaml
```

Ensuite, nous devons mettre à jour l'application cliente — `sa-frontend` — pour rediriger l'utilisateur vers le frontend. Vous pouvez en savoir plus sur le code [ici](https://github.com/rinormaloku/master-istio/blob/main/services/sa-frontend/src/App.js#L80-L83). Cependant, vous pouvez vous épargner les détails et simplement appliquer l'image pré-construite avec ces changements.

```bash
kubectl set image deployment/sa-frontend \
    sa-frontend=rinormaloku/sentiment-analysis-frontend:keycloak
```

Attendez que le Pod soit en cours d'exécution, puis rafraîchissez la page `sa-frontend`.

La nouvelle version vous redirige vers `Keycloak` pour l'authentification. Utilisez les identifiants `user / password` pour vous connecter. Une fois la connexion réussie, vous recevrez un JWT et serez redirigé vers le client.

Par conséquent, les requêtes ultérieures pour l'analyse de phrases contiendront le JWT sur la base duquel nous pourrons authentifier et autoriser l'utilisateur final.

### RequestAuthentication – comment authentifier les requêtes des utilisateurs finaux

L'approche recommandée pour authentifier le trafic des utilisateurs finaux se situe au niveau de l'Ingress Gateway. Cela réduit la quantité de traitement car le trafic non authentifié et non autorisé est rejeté dès le début. Mais si vous souhaitez propager le JWT à travers les services, vous devez mettre à jour vos services pour le transmettre.

La figure ci-dessous montre les rôles et leurs accès à nos services que nous allons implémenter ensuite.

Voici un résumé des niveaux d'accès :

* Tous les utilisateurs peuvent accéder au service `sa-frontend` (ce qui est important pour initier le flux d'authentification).
* Les utilisateurs authentifiés peuvent accéder à `sa-webapp` en plus de l'accès à `sa-frontend`.
* Les modérateurs peuvent accéder à tous les services.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/different-access-levels.png)

L'API `RequestAuthentication` est utilisée pour configurer l'authentification des JWT des utilisateurs finaux. Par exemple, avec la configuration ci-dessous, nous authentifions les JWT émis par `keycloak`.

```
apiVersion: "security.istio.io/v1beta1"
kind: "RequestAuthentication"
metadata:
  name: "keycloak-request-authn"
  namespace: istio-system
spec:
  selector:
    matchLabels:
      app: istio-ingressgateway
  jwtRules:
  - issuer: "http://localhost:8080/auth/realms/master" (1)
    jwksUri: http://keycloak.keycloak.svc:8080/auth/realms/master/protocol/openid-connect/certs (2)
```

Explication des attributs de la règle JWT vus dans la liste ci-dessus :

1. Les jetons qui correspondent à cet émetteur (issuer) sont authentifiés avec cette règle JWT.
2. Les jetons correspondants sont validés par rapport aux JSON Web Key Sets (JWKS) trouvés à cette URI.

Appliquez-le au cluster.

```bash
kubectl apply -f istio/security/request-authentication.yaml
```

Vous pourriez vous attendre à ce que les requêtes sans JWT soient rejetées à partir de maintenant, mais ce n'est pas correct. La ressource `RequestAuthentication` authentifie uniquement les requêtes contenant le JWT. Les autres requêtes sont transmises telles quelles.

Vérifiez cela en déclenchant une requête sans jeton, elle est admise et servie, comme indiqué ci-dessous :

```bash
$ curl -S http://localhost:8080/sentiment \
    -H "Content-type: application/json" \
    -d '{"sentence": "I love yogobella"}'

{"sentence":"I love yogobella","polarity":0.5}
```

Cependant, il existe une différence entre les requêtes qui contiennent un JWT et celles qui n'en ont pas.

Les premières auront les données d'identité stockées dans les métadonnées de connexion. En revanche, les secondes n'ont pas de données d'identité dans les métadonnées de connexion. Les métadonnées de connexion sont appelées identité de connexion ou identité de requête.

**NOTE :** L'identité de la requête est composée des données authentifiées via `RequestAuthentication` et `PeerAuthentication`. Ainsi, vous pouvez contrôler l'accès en fonction à la fois de l'utilisateur final et du service effectuant la requête.

Les politiques prennent des décisions pour autoriser ou rejeter le trafic en fonction de l'identité de la requête.

### AuthorizationPolicy – Comment autoriser et rejeter les requêtes

En utilisant l'API `AuthorizationPolicy`, vous pouvez configurer les proxys pour accepter ou rejeter le trafic.

Nous voulons que *tous les utilisateurs*, même non authentifiés, accèdent aux services `sa-frontend` et `keycloak` (afin que les utilisateurs puissent s'authentifier en premier lieu). Et ce n'est qu'après cela que nous savons "qui" est l'utilisateur, et nous pouvons appliquer des politiques pour déterminer "quelles" actions il est autorisé à effectuer.

Nous y parvenons avec la politique ci-dessous. Elle autorise tout trafic vers les chemins listés (les chemins concernent les services `sa-frontend` et `keycloak`).

```yaml
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: allow-view
  namespace: istio-system
spec:
  selector:
    matchLabels:
      app: istio-ingressgateway
  action: ALLOW
  rules:
  - to:
    - operation:
        paths: ["/", "/static*", "/auth*"]
```

Appliquez-le au cluster.

```bash
kubectl apply -f istio/security/allow-view.yaml
```

Désormais, les utilisateurs peuvent s'authentifier et recevoir un JWT, qui est utilisé dans les requêtes ultérieures vers les services du cluster. La configuration `RequestAuthentication` authentifie le JWT et, par conséquent, les revendications du jeton sont stockées en tant que métadonnées de connexion.

La métadonnée clé que nous utilisons dans la section suivante est `requestPrincipals`, qu'Istio construit en combinant les revendications `iss` et `sub` du JWT.

#### Comment autoriser les requêtes en fonction des métadonnées de connexion

Avec la politique ci-dessous, nous autorisons les requêtes de n'importe quel `requestPrincipals` correspondant pour tous les chemins préfixés par `/sentiment`.

```yaml
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: allow-analysis
  namespace: istio-system
spec:
  selector:
    matchLabels:
      app: istio-ingressgateway
  action: ALLOW
  rules:
  - from:
    - source:
        requestPrincipals: ["*"]
    to:
    - operation:
        paths: ["/sentiment*"]
```

Pour qu'une politique s'applique au trafic entrant, elle doit correspondre à la fois à la source (`source`) et à l'opération (`operation`). Par exemple, la politique ci-dessus s'appliquera et autorisera le trafic uniquement si :

* **source** correspond à tous les requestPrincipals en raison du caractère générique. Cependant, elle ne correspondra pas si la requête n'a pas de principal de requête. Le principal de requête pour une requête n'est attribué qu'après qu'une `RequestAuthentication` a validé le JWT.
* **operation** correspond à toutes les requêtes dont les chemins sont préfixés par `/sentiment`.

Appliquez-le au cluster.

```bash
kubectl apply -f istio/security/allow-analysis.yaml
```

Vérifiez que vous pouvez analyser des phrases. Si tout va bien, passez à la section suivante.

#### Différents niveaux d'accès

Le `sa-frontend` permet aux utilisateurs d'envoyer un feedback après avoir analysé une phrase. Mais actuellement, si vous essayez d'envoyer un feedback, la requête échouera avec "Not authorized."

![Image](https://www.freecodecamp.org/news/content/images/2022/05/frontend-unauthorized-1.png)

Cela se produit car aucune politique n'a explicitement autorisé la requête. Elle sera donc refusée par défaut. Ensuite, nous voulons autoriser cette action uniquement pour les modérateurs.

Nous faisons la distinction entre les modérateurs et les utilisateurs à l'aide de la revendication `group`. Nous pouvons y parvenir avec la politique suivante :

```yaml
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: allow-feedback-for-mods
  namespace: istio-system
spec:
  selector:
    matchLabels:
      app: istio-ingressgateway
  action: ALLOW
  rules:
  - from:
    - source:
        requestPrincipals: ["*"]
    when:
    - key: request.auth.claims[group]
      values: ["moderator"]
```

Appliquez-le au cluster.

```bash
kubectl apply -f istio/security/allow-feedback.yaml
```

Pour vérifier que les modérateurs peuvent envoyer des feedbacks, suivez ces étapes : ouvrez une fenêtre de navigation privée, connectez-vous avec les identifiants `moderator / password`, tapez une phrase et soumettez un feedback. Cela réussira !

Dans la section sécurité, nous avons appris trois ressources personnalisées :

* `PeerAuthentication` — pour l'authentification des pairs.
* `RequestAuthentication` — pour l'authentification des utilisateurs finaux.
* `AuthorizationPolicy` — pour autoriser ou rejeter les requêtes en fonction des données authentifiées.

## Résumé

Hé ! Vous êtes arrivé au bout de cet article. Félicitations et bravo ! C'était un article plutôt long, mais après y avoir investi quelques heures — et sur vous-même — vous avez une idée claire de ce qu'est `Istio` et de ce qu'il peut faire pour vous et votre entreprise.

Un résumé de ce que nous avons couvert :

* Les Service Meshes sont implémentés en ajoutant un proxy aux côtés de l'application et en interceptant tout le trafic réseau vers et depuis celle-ci.
* Le proxy permet :
  * **Gestion avancée du trafic**
    * En utilisant les `Gateways`, nous définissons le trafic qui est accepté dans un proxy de service (y compris l'Ingress Gateway).
    * En utilisant les `VirtualServices`, nous définissons comment router le trafic vers une destination.
    * En utilisant les `DestinationRules`, nous définissons des politiques après le routage. Dans notre cas, nous ne l'avons utilisé que pour définir des sous-ensembles.
  * **Rendre un système observable en générant de la télémétrie**
    * Les journaux d'accès enregistrent les résultats des requêtes individuelles.
    * Les traces montrent le flux d'une requête à travers les services. Visualisé par Inspecteur Gadget (*je n'ai pas pu résister, mais vous savez que je veux dire Jaeger ;P*) et Kiali.
    * Les métriques mesurent les propriétés du système, le taux de réussite, les opérations par seconde, et ainsi de suite.
  * **Sécurité**
    * La ressource `PeerAuthentication` impose uniquement un trafic mutuellement authentifié, garantissant que tout le trafic de service à service est chiffré et que le trafic en clair est rejeté.
    * La ressource `RequestAuthentication` authentifie les JWT par rapport aux JWKS configurés.
    * La ressource `AuthorizationPolicy` nous permet de prendre des décisions sur l'acceptation ou le rejet du trafic.

### Lectures complémentaires

Après avoir lu jusqu'ici, vous en savez plus sur Istio que beaucoup de gens, même certains qui font tourner des services en production avec. 

Cependant, certaines particularités d'Istio pourraient vous surprendre. Parfois, votre application et le proxy peuvent mal se comporter. Et vous aurez d'autres questions telles que :

* Comment dépanner le proxy de service ou l'Ingress Gateway ?
* Comment donner un sens à la configuration Envoy appliquée ?
* Comment utiliser l'injection de fautes (fault injection) ?
* Sécuriser le trafic à la périphérie (edge).
* Comment configurer des Service Meshes multi-clusters ? Que se passe-t-il dans les coulisses ?
* L'intégration de workloads basés sur des machines est-elle possible ? Si oui, comment ?
* Comment utiliser des serveurs d'autorisation externes ?
* Opérations de jour 2.

Nous répondons à ces questions et à bien d'autres dans le livre ["Istio in Action."](https://www.manning.com/books/istio-in-action?utm_source=rinor&utm_medium=affiliate&utm_campaign=book_posta2_istio_9_30_18&a_aid=rinor&a_bid=9f6a70f3) Ce qui me rend vraiment fier de ce livre — en plus d'être l'élaboration la plus approfondie d'Istio — c'est sa valeur de référence.

C'est fou. Je me surprends, ainsi que d'autres ingénieurs de terrain ici chez Solo, à y revenir chaque fois que nous résolvons un problème délicat, tel que la résolution DNS, le dépannage du trafic inter-clusters, et ainsi de suite.

Voici d'autres ressources utiles :

* [Référence de configuration Istio](https://istio.io/latest/docs/reference/config/)
* [Blog d'Istio](https://istio.io/latest/blog/)
* Le [blog](https://www.solo.io/blog/) et la [chaîne YouTube](https://www.youtube.com/channel/UCuketWAG3WqYjjxtQ9Q8ApQ) de Solo
* [Blog de Christian Posta](https://blog.christianposta.com/)
* [Blog de Karl Stoney](https://karlstoney.com/tag/istio/)

Je saisis l'occasion pour vous remercier de m'avoir rejoint dans ce voyage. Ce n'était pas facile, et vous êtes incroyable d'avoir tenu bon.

J'aimerais beaucoup connaître votre avis, alors n'hésitez pas à me contacter sur Twitter ([@rinormaloku](https://twitter.com/rinormaloku)) ou sur ma page [rinormaloku.com](https://rinormaloku.com/).