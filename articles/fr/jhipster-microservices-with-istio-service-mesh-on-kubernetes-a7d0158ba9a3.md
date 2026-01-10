---
title: Comment configurer des microservices JHipster avec le service mesh Istio sur
  Kubernetes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-17T16:01:37.000Z'
originalURL: https://freecodecamp.org/news/jhipster-microservices-with-istio-service-mesh-on-kubernetes-a7d0158ba9a3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*sed7vszGYvi40oa1F7iVzg.png
tags:
- name: Azure
  slug: azure
- name: Google Cloud Platform
  slug: google-cloud-platform
- name: Kubernetes
  slug: kubernetes
- name: Productivity
  slug: productivity
- name: 'tech '
  slug: tech
seo_title: Comment configurer des microservices JHipster avec le service mesh Istio
  sur Kubernetes
seo_desc: 'By Deepu K Sasidharan

  You can find a more up to date version of this post that uses JHipster 6 and latest
  Istio & Kubernetes versions here.


  Istio is the coolest kid on the DevOps and Cloud block now. For those of you who
  aren’t following close enoug...'
---

Par Deepu K Sasidharan

Vous pouvez trouver une version plus à jour de cet article qui utilise JHipster 6 et les dernières versions d'Istio et Kubernetes [ici](https://dev.to/deepu105/how-to-set-up-java-microservices-with-istio-service-mesh-on-kubernetes-5bkn).

---

Istio est le nouvel outil le plus en vogue dans le domaine du DevOps et du Cloud. Pour ceux qui ne suivent pas de près — [Istio est un service mesh](https://istio.io/docs/concepts/what-is-istio/) pour les architectures d'applications distribuées, en particulier celles que vous exécutez sur le cloud avec Kubernetes. Istio fonctionne extrêmement bien avec Kubernetes, au point que vous pourriez penser qu'il fait partie de Kubernetes.

Si vous vous demandez encore ce qu'est un service mesh ou Istio, voici un aperçu d'Istio.

Istio fournit les fonctionnalités suivantes dans une architecture d'application distribuée :

* Découverte de services — Traditionnellement fournie par des plateformes comme [Netflix Eureka](https://github.com/Netflix/eureka/wiki) ou [Consul](https://www.consul.io/).
* Équilibrage de charge automatique — Vous avez peut-être utilisé [Netflix Zuul](https://github.com/Netflix/zuul/wiki) pour cela.
* Routage, disjoncteur, nouvelles tentatives, basculements, injection de fautes — Pensez à [Netflix Ribbon](https://github.com/Netflix/ribbon/wiki), [Hytrix](https://github.com/Netflix/Hystrix) et ainsi de suite.
* Application des politiques pour le contrôle d'accès, la limitation de débit, les tests A/B, la division du trafic et les quotas — Encore une fois, vous avez peut-être utilisé Zuul pour faire certaines de ces choses.
* Métriques, journaux et traces — Pensez à [ELK](https://www.elastic.co/elk-stack) ou [Stack driver](https://cloud.google.com/stackdriver/)
* Communication sécurisée entre services

Ci-dessous se trouve l'architecture d'Istio.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_STCerKXb4L3Hutyn4P5Gw.png)
_Architecture d'Istio_

Elle peut être classée en 2 plans distincts.

**Plan de données** : Composé de proxys [Envoy](https://www.envoyproxy.io/) déployés en tant que sidecars pour les conteneurs d'application. Ils contrôlent tout le trafic entrant et sortant du conteneur.

**Plan de contrôle** : Il utilise Pilot pour gérer et configurer les proxys afin de router le trafic. Il configure également Mixer pour appliquer les politiques et collecter la télémétrie. Il comprend également d'autres composants comme Citadel, pour gérer la sécurité, et Galley, pour gérer les configurations.

Istio configure également une instance de [Grafana](https://grafana.com/), [Prometheus](https://prometheus.io/) et [Jaeger](https://www.jaegertracing.io/) pour la surveillance et l'observabilité. Vous pouvez utiliser ceux-ci ou utiliser votre propre pile de surveillance.

J'espère que cela donne un aperçu d'Istio, concentrons-nous maintenant sur l'objectif de cet article.

### Devoxx 2018

J'ai fait une présentation à [Devoxx 2018](https://dvbe18.confinabox.com/talk/XCM-6395/JHipster_5_-_What's_new_and_noteworthy) avec [Julien Dubois](https://www.julien-dubois.com/) faisant la même démonstration et j'ai promis que j'écrirais un article détaillé à ce sujet.

%[https://twitter.com/deepu105/status/1063010906777497600?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed&ref_url=https%3A%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Ftype%3Dtext%252Fhtml%26key%3Da19fcc184b9711e1b4764040d3dc5c07%26schema%3Dtwitter%26url%3Dhttps%253A%2F%2Ftwitter.com%2Fdeepu105%2Fstatus%2F1063010906777497600%26image%3Dhttps%253A%2F%2Fi.embed.ly%2F1%2Fimage%253Furl%253Dhttps%25253A%25252F%25252Fpbs.twimg.com%25252Fprofile_images%25252F1056590953132244993%25252F0FGRfVeQ_400x400.jpg%2526key%253Da19fcc184b9711e1b4764040d3dc5c07]

Vous pouvez regarder la vidéo pour voir JHipster + Istio en action.

%[https://www.youtube.com/watch?v=NPToZd0PxbI]

Vous pouvez également consulter les diapositives sur Speaker Deck.

%[https://speakerdeck.com/deepu105/jhipster-5-whats-new-and-noteworthy]

### Préparation du cluster Kubernetes

Tout d'abord, préparons un cluster Kubernetes pour déployer Istio et nos conteneurs d'application. Suivez les instructions pour l'une des plateformes que vous préférez.

#### Prérequis

[**kubectl**](https://kubernetes.io/docs/tasks/tools/install-kubectl/) : L'outil en ligne de commande pour interagir avec Kubernetes. Installez-le et configurez-le.

#### Créer un cluster sur Azure Kubernetes Service (AKS)

Si vous allez utiliser Azure, installez alors [**Azure CLI**](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest) pour interagir avec Azure. Installez-le et connectez-vous avec votre compte Azure (vous pouvez créer un [compte gratuit](https://azure.microsoft.com/en-us/free/) si vous n'en avez pas déjà un).

Tout d'abord, créons un groupe de ressources. Vous pouvez utiliser n'importe quelle région ici au lieu de East US.

```bash
$ az group create --name eCommerceCluster --location eastus
```

Créez le cluster Kubernetes :

```bash
$ az aks create \
--resource-group eCommerceCluster \
--name eCommerceCluster \
--node-count 4 \
--kubernetes-version 1.11.4 \
--enable-addons monitoring \
--generate-ssh-keys
```

Le drapeau `node-count` est important car la configuration nécessite au moins quatre nœuds avec le CPU par défaut pour exécuter tout. Vous pouvez essayer d'utiliser une version `kubernetes-version` plus élevée si elle est supportée, sinon restez sur 1.11.4

La création du cluster peut prendre un certain temps, alors asseyez-vous et détendez-vous. ?

Une fois le cluster créé, récupérez ses informations d'identification à utiliser depuis `kubectl` en exécutant la commande ci-dessous. Elle injecte automatiquement les informations d'identification dans votre configuration `kubectl` sous **_~/.kube/config_**

```bash
$ az aks get-credentials \
--resource-group eCommerceCluster \
--name eCommerceCluster
```

Vous pouvez voir le cluster créé dans le portail Azure :

![Image](https://cdn-media-1.freecodecamp.org/images/1*yfLnHHc_N7VCkEY9vjNciQ.png)
_Cluster Kubernetes dans AKS_

Exécutez `kubectl get nodes` pour le voir dans la ligne de commande et vérifier que kubectl peut se connecter à votre cluster.

![Image](https://cdn-media-1.freecodecamp.org/images/1*k8xsRqQsvnquUhGPAh9TsA.png)
_Nœuds du cluster_

Passez à la section **Installer et configurer Istio**.

#### Créer un cluster sur Google Kubernetes Engine (GKE)

Si vous allez utiliser Google Cloud Platform (GCP), installez alors [**Gcloud CLI**](https://cloud.google.com/sdk/docs/) pour interagir avec GCP. Installez-le et connectez-vous avec votre compte GCP (vous pouvez créer un [compte gratuit](https://console.cloud.google.com/freetrial) si vous n'en avez pas déjà un).

Tout d'abord, nous avons besoin d'un projet GCP, vous pouvez soit utiliser un projet existant que vous avez, soit en créer un nouveau en utilisant GCloud CLI avec la commande ci-dessous :

```bash
$ gcloud projects create jhipster-demo-deepu
```

Définissez le projet que vous souhaitez utiliser comme projet par défaut :

```bash
$ gcloud config set project jhipster-demo-deepu
```

Maintenant, créons un cluster pour notre application avec la commande ci-dessous :

```bash
$ gcloud container clusters create hello-hipster \

   --cluster-version 1.10 \
   
   --num-nodes 4 \
   
   --machine-type n1-standard-2
```

Les drapeaux `num-nodes` et `machine-type` sont importants car la configuration nécessite au moins quatre nœuds avec un CPU plus puissant pour exécuter tout. Vous pouvez essayer d'utiliser une version `cluster-version` plus élevée si elle est supportée, sinon restez sur 1.10.

La création du cluster peut prendre un certain temps, alors asseyez-vous et détendez-vous.

Une fois le cluster créé, récupérez ses informations d'identification à utiliser depuis `kubectl` en exécutant la commande ci-dessous. Elle injecte automatiquement les informations d'identification dans votre configuration `kubectl` sous **_~/.kube/config_**

```bash
$ gcloud container clusters get-credentials hello-hipster
```

Vous pouvez voir le cluster créé dans l'interface graphique de GCP.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZxNbIG4vqWJymTLweJpPyQ.png)
_Cluster Kubernetes sur GKE_

Exécutez `kubectl get nodes` pour le voir dans la ligne de commande et vérifier que kubectl peut se connecter à votre cluster.

![Image](https://cdn-media-1.freecodecamp.org/images/1*F5Qcd_GS_GSuA1PsJE7gvA.png)
_Nœuds du cluster_

### Installer et configurer Istio

Installez Istio sur votre machine en suivant ces étapes :

```bash
$ cd ~/

$ export ISTIO_VERSION=1.0.2

$ curl -L https://git.io/getLatestIstio | sh -

$ ln -sf istio-$ISTIO_VERSION istio

$ export PATH=~/istio/bin:$PATH
```

Assurez-vous d'utiliser la version **1.0.2** car la dernière version semble avoir des problèmes de connexion aux conteneurs de la base de données MySQL.

Maintenant, installons Istio sur notre cluster Kubernetes en appliquant les manifestes Kubernetes fournis et les modèles helm d'Istio.

```bash
$ kubectl apply -f ~/istio/install/kubernetes/helm/istio/templates/crds.yaml
$ kubectl apply -f ~/istio/install/kubernetes/istio-demo.yaml \
    --as=admin --as-group=system:masters
```

Attendez que les pods soient en cours d'exécution, ceux-ci seront déployés dans l'espace de noms `istio-system`.

```bash
$ watch kubectl get pods -n istio-system
```

Une fois que les pods sont en état d'exécution, quittez la boucle de surveillance et exécutez la commande ci-dessous pour obtenir les détails du service de la passerelle Ingress. C'est le seul service qui est exposé à une IP externe.

```bash
$ kubectl get svc istio-ingressgateway -n istio-system

NAME                   TYPE           CLUSTER-IP     EXTERNAL-IP
istio-ingressgateway   LoadBalancer   10.27.249.83   35.195.81.130
```

L'IP externe est très importante ici, sauvegardons-la dans une variable d'environnement afin de pouvoir l'utiliser dans les commandes suivantes.

```bash
$ export \
  INGRESS_IP=$(kubectl -n istio-system get svc \
  istio-ingressgateway \
  -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
```

Notre cluster Kubernetes est maintenant prêt pour Istio. ?

_Pour des options de configuration avancées d'Istio, consultez_ [_https://istio.io/docs/setup/kubernetes/_](https://istio.io/docs/setup/kubernetes/)

### Création de la pile d'applications microservices

Dans l'un de mes [articles précédents](https://medium.com/@deepu105/create-full-microservice-stack-using-jhipster-domain-language-under-30-minutes-ecc6e7fc3f77), j'ai présenté comment créer une architecture microservice complète en utilisant **JHipster** et **JDL**. Vous pouvez lire l'article [ici](https://medium.com/@deepu105/create-full-microservice-stack-using-jhipster-domain-language-under-30-minutes-ecc6e7fc3f77) si vous souhaitez en savoir plus. Pour cet exercice, nous utiliserons la même application mais nous n'utiliserons pas l'option de découverte de services Eureka que nous avons utilisée précédemment. Notez également que l'application de magasin est divisée en applications Gateway et Product.

#### Architecture

Voici l'architecture du microservice que nous allons créer et déployer aujourd'hui.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UmNJ-Ue362-OltPOxt-OFQ.png)
_Architecture de microservice avec Istio_

Elle comprend une application de passerelle et trois applications de microservices. Chacune d'entre elles a sa propre base de données. Vous pouvez voir que chaque application a un proxy Envoy attaché au pod en tant que sidecar. Les composants du plan de contrôle d'Istio sont également déployés dans le même cluster avec Prometheus, Grafana et Jaeger.

La passerelle Ingress d'Istio est le seul point d'entrée pour le trafic et elle route le trafic vers tous les microservices en conséquence. La télémétrie est collectée à partir de tous les conteneurs en cours d'exécution dans le cluster, y compris les applications, les bases de données et les composants Istio.

Comparé à l'architecture de l'application originale [ici](https://medium.com/@deepu105/deploying-jhipster-microservices-on-azure-kubernetes-service-aks-fb46991746ba), vous pouvez clairement voir que nous avons remplacé le registre JHipster et les composants Netflix OSS par Istio. La pile de surveillance ELK est remplacée par Prometheus, Grafana et Jaeger configurés par Istio. Voici le diagramme d'architecture original sans Istio pour une comparaison visuelle rapide.

![Image](https://cdn-media-1.freecodecamp.org/images/1*H-6_dz1-aYXQ-fzWEuJcRw.png)
_Architecture de microservice avec Netflix OSS_

#### Application JDL

Examinons la déclaration JDL modifiée. Vous pouvez voir que nous avons déclaré `serviceDiscoveryType no` ici puisque nous allons utiliser Istio pour cela.

```

application {
  config {
    baseName store
    applicationType gateway
    packageName com.jhipster.demo.store
    serviceDiscoveryType no
    authenticationType jwt
    prodDatabaseType mysql
    cacheProvider hazelcast
    buildTool gradle
    clientFramework react
    useSass true
    testFrameworks [protractor]
  }
  entities *
}


application {
  config {
    baseName product
    applicationType microservice
    packageName com.jhipster.demo.product
    serviceDiscoveryType no
    authenticationType jwt
    prodDatabaseType mysql
    cacheProvider hazelcast
    buildTool gradle
    serverPort 8081
  }
  entities Product, ProductCategory, ProductOrder, OrderItem
}

application {
  config {
    baseName invoice
    applicationType microservice
    packageName com.jhipster.demo.invoice
    serviceDiscoveryType no
    authenticationType jwt
    prodDatabaseType mysql
    buildTool gradle
    serverPort 8082
  }
  entities Invoice, Shipment
}

application {
  config {
    baseName notification
    applicationType microservice
    packageName com.jhipster.demo.notification
    serviceDiscoveryType no
    authenticationType jwt
    databaseType mongodb
    cacheProvider no
    enableHibernateCache false
    buildTool gradle
    serverPort 8083
  }
  entities Notification
}

/**
 * Entités pour la passerelle Store
 */

// Client pour le magasin
entity Customer {
    firstName String required
    lastName String required
    gender Gender required
    email String required pattern(/^[^@\s]+@[^@\s]+\.[^@\s]+$/)
    phone String required
    addressLine1 String required
    addressLine2 String
    city String required
    country String required
}

enum Gender {
    MALE, FEMALE, OTHER
}

relationship OneToOne {
    Customer{user(login) required} to User
}

service Customer with serviceClass
paginate Customer with pagination


/**
 * Entités pour le microservice de produit
 */


// Produit vendu par le magasin en ligne 
entity Product {
    name String required
    description String
    price BigDecimal required min(0)
    size Size required
    image ImageBlob
}

enum Size {
    S, M, L, XL, XXL
}

entity ProductCategory {
    name String required
    description String
}

entity ProductOrder {
    placedDate Instant required
    status OrderStatus required
    code String required
    invoiceId Long
    customer String required
}

enum OrderStatus {
    COMPLETED, PENDING, CANCELLED
}

entity OrderItem {
    quantity Integer required min(0)
    totalPrice BigDecimal required min(0)
    status OrderItemStatus required
}

enum OrderItemStatus {
    AVAILABLE, OUT_OF_STOCK, BACK_ORDER
}

relationship ManyToOne {
	OrderItem{product(name) required} to Product
}

relationship OneToMany {
   ProductOrder{orderItem} to OrderItem{order(code) required} ,
   ProductCategory{product} to Product{productCategory(name)}
}

service Product, ProductCategory, ProductOrder, OrderItem with serviceClass
paginate Product, ProductOrder, OrderItem with pagination
microservice Product, ProductOrder, ProductCategory, OrderItem with product


/**
 * Entités pour le microservice Invoice
 */


// Facture pour les ventes
entity Invoice {
    code String required
    date Instant required
    details String
    status InvoiceStatus required
    paymentMethod PaymentMethod required
    paymentDate Instant required
    paymentAmount BigDecimal required
}

enum InvoiceStatus {
    PAID, ISSUED, CANCELLED
}

entity Shipment {
    trackingCode String
    date Instant required
    details String
}

enum PaymentMethod {
    CREDIT_CARD, CASH_ON_DELIVERY, PAYPAL
}

relationship OneToMany {
    Invoice{shipment} to Shipment{invoice(code) required}
}

service Invoice, Shipment with serviceClass
paginate Invoice, Shipment with pagination
microservice Invoice, Shipment with invoice


/**
 * Entités pour le microservice de notification
 */


entity Notification {
    date Instant required
    details String
    sentDate Instant required
    format NotificationType required
    userId Long required
    productId Long required
}

enum NotificationType {
    EMAIL, SMS, PARCEL
}

microservice Notification with notification

/**
 * Déploiements
 */

deployment {
  deploymentType kubernetes
  appsFolders [store, invoice, notification, product]
  dockerRepositoryName "deepu105"
  serviceDiscoveryType no
  istio true
  kubernetesServiceType Ingress
  kubernetesNamespace jhipster
  ingressDomain "34.90.236.124.nip.io"
}
```

#### Déploiement JDL

La version 5.7.0 de JHipster a introduit la prise en charge de la déclaration de déploiement directement dans le JDL

%[https://twitter.com/deepu105/status/1056588722769195018?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed&ref_url=https%3A%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Ftype%3Dtext%252Fhtml%26key%3Da19fcc184b9711e1b4764040d3dc5c07%26schema%3Dtwitter%26url%3Dhttps%253A%2F%2Ftwitter.com%2Fdeepu105%2Fstatus%2F1056588722769195018%26image%3Dhttps%253A%2F%2Fi.embed.ly%2F1%2Fimage%253Furl%253Dhttps%25253A%25252F%25252Fpbs.twimg.com%25252Fprofile_images%25252F1056590953132244993%25252F0FGRfVeQ_400x400.jpg%2526key%253Da19fcc184b9711e1b4764040d3dc5c07]

Nous avons ce qui suit dans notre JDL qui déclare notre déploiement Kubernetes :

```
deployment {
  deploymentType kubernetes
  appsFolders [store, invoice, notification, product]
  dockerRepositoryName "deepu105"
  serviceDiscoveryType no
  istio autoInjection
  istioRoute true
  kubernetesServiceType Ingress
  kubernetesNamespace jhipster
  ingressDomain "35.195.81.130.nip.io"
}
```

Le `serviceDiscoveryType` est désactivé et nous avons activé Istio avec le support `autoInjection` — les sidecars Envoy sont injectés automatiquement pour les applications sélectionnées. Les routes Istio sont également générées pour les applications en activant l'option `istioRoute`.

Le `kubernetesServiceType` est défini comme `Ingress`, ce qui est très important car Istio ne peut fonctionner qu'avec un type de service de contrôleur Ingress. Pour Ingress, nous devons définir le DNS du domaine et c'est là que l'IP de la passerelle Ingress Istio est nécessaire. Maintenant, nous avons besoin d'un DNS pour notre IP. Pour des cas d'utilisation réels, vous devriez mapper un DNS pour l'IP, mais pour des fins de test et de démonstration, nous pouvons utiliser un service DNS générique comme [**nip.io**](http://nip.io/) pour résoudre notre IP. Il suffit d'ajouter `nip.io` à notre IP et d'utiliser cela comme domaine d'entrée.

#### Générer les applications et les manifestes de déploiement

Maintenant que notre JDL est prêt, générons nos applications et les manifestes Kubernetes. Créez un nouveau répertoire et sauvegardez le JDL ci-dessus dans le répertoire. Nommons-le **_app-istio.jdl_** puis exécutez la commande import-jdl.

```bash
$ mkdir istio-demo && cd istio-demo
$ jhipster import-jdl app-istio.jdl
```

Cela générera toutes les applications et installera les dépendances NPM requises dans chacune d'elles. Une fois les applications générées, les manifestes de déploiement seront générés et des instructions utiles seront imprimées dans la console.

![Image](https://cdn-media-1.freecodecamp.org/images/0*ROg2XrRkHVHA4Xib)
_Sortie de génération_

Ouvrez le code généré dans votre IDE/éditeur préféré et explorez le code.

### Déployer sur le cluster Kubernetes en utilisant Kubectl

Maintenant, construisons et déployons nos applications. Exécutez la commande `./gradlew bootWar -Pprod jibDockerBuild` dans les dossiers store, product, invoice et notification pour construire les images docker. Une fois les images construites, poussez-les vers le dépôt docker avec ces commandes :

```bash
$ docker image tag store deepu105/store

$ docker push deepu105/store

$ docker image tag invoice deepu105/invoice

$ docker push deepu105/invoice

$ docker image tag notification deepu105/notification

$ docker push deepu105/notification

$ docker image tag product deepu105/product

$ docker push deepu105/product
```

Une fois les images poussées, naviguez dans le répertoire Kubernetes généré et exécutez le script de démarrage fourni. (Si vous êtes sous Windows, vous pouvez exécuter les étapes dans **_kubectl-apply.sh_** manuellement une par une.)

```bash
$ cd kubernetes
$ ./kubectl-apply.sh
```

Exécutez `watch kubectl get pods -n jhipster` pour surveiller le statut.

### Applications déployées

Une fois que tous les pods sont en état d'exécution, nous pouvons explorer les applications déployées

#### Passerelle de l'application

L'application de passerelle store est le point d'entrée pour nos microservices. Obtenez l'URL pour l'application store en exécutant `echo store.$INGRESS_IP.nip.io`, nous avons déjà stocké l'INGRESS_IP dans les variables d'environnement lors de la création de la configuration Istio. Visitez l'URL dans votre navigateur préféré et explorez l'application. Essayez de créer quelques entités pour les microservices :

![Image](https://cdn-media-1.freecodecamp.org/images/0*Qd6y_H-ObCeorQkg)
_Application de passerelle store_

#### Surveillance

La configuration Istio inclut Grafana et Prometheus configurés pour collecter et afficher les métriques de nos conteneurs. Jetons un coup d'œil.

Par défaut, seule la passerelle Ingress est exposée à l'IP externe et nous allons donc utiliser le transfert de port kubectl pour établir un tunnel sécurisé vers les services requis

Créons un tunnel pour Grafana :

```bash
$ kubectl -n istio-system \
port-forward $(kubectl -n istio-system get pod \

-l app=grafana -o jsonpath='{.items[0].metadata.name}') 3000:3000
```

Ouvrez [localhost:3000](localhost:3000) pour voir le tableau de bord Grafana.

![Image](https://cdn-media-1.freecodecamp.org/images/0*zaX0S8relpT4q__T)
_Tableau de bord Grafana pour l'application Store_

Grafana utilise les métriques collectées par Prometheus. Nous pouvons regarder Prometheus directement en créant un tunnel pour celui-ci et en ouvrant [localhost:9090](localhost:9090) :

```bash
$ kubectl -n istio-system \
port-forward $(kubectl -n istio-system get pod -l \

app=prometheus -o jsonpath='{.items[0].metadata.name}') 9090:9090
```

![Image](https://cdn-media-1.freecodecamp.org/images/0*W4obHNne_wQJfAuU)
_Tableau de bord Prometheus_

#### Observabilité

Istio configure Jaeger pour le traçage distribué et le graphe de service pour l'observabilité des services. Jetons un coup d'œil à ceux-ci.

Créez un tunnel pour Jaeger et ouvrez [localhost:16686](localhost:16686)

```bash
$ kubectl -n istio-system \
port-forward $(kubectl -n istio-system get pod -l \

app=jaeger -o jsonpath='{.items[0].metadata.name}') 16686:16686
```

![Image](https://cdn-media-1.freecodecamp.org/images/0*cyhS1_B0LFO54e48)
_Tableau de bord de traçage Jaeger_

Vous pouvez faire quelques requêtes dans l'application et les trouver dans le tableau de bord de traçage en interrogeant le service. Cliquez sur la requête pour voir les détails de traçage :

![Image](https://cdn-media-1.freecodecamp.org/images/1*X4XtKtIeMapPEyt_nfvftA.png)
_Traçage pour la requête de liste de catégories de produits_

Créons maintenant un tunnel pour le graphe de service et ouvrons-le dans [localhost:8080/force/forcegraph.html](localhost:8080/force/forcegraph.html) :

```bash
$ kubectl -n istio-system \
port-forward $(kubectl -n istio-system get pod -l \

app=servicegraph -o jsonpath='{.items[0].metadata.name}') 8088:8088
```

![Image](https://cdn-media-1.freecodecamp.org/images/0*4nQUsagF6TVupK-5)
_Graphe de service Istio_

### Conclusion

Istio fournit des blocs de construction pour construire des microservices distribués de manière plus native à Kubernetes et prend en charge la complexité et la responsabilité de maintenir ces blocs loin de vous. Cela signifie que vous n'avez pas à vous soucier de maintenir le code ou les déploiements pour la découverte de services, le traçage, etc.

La documentation d'Istio indique

> Le déploiement d'une application basée sur des microservices dans un service mesh Istio permet de contrôler externement la surveillance et le traçage des services, le routage des requêtes (version), les tests de résilience, la sécurité et l'application des politiques, etc., de manière cohérente à travers les services, pour l'application dans son ensemble.

Werner Vogels (CTO d'AWS) a déclaré lors d'AWS Re:Invent

> « À l'avenir, tout le code que vous écrivez sera de la logique métier. »

Le service mesh Istio aide à réaliser cette déclaration. Cela vous permet de vous concentrer uniquement sur les applications que vous développez et avec JHipster, cet avenir est vraiment là et vous n'avez besoin de vous soucier que d'écrire votre logique métier.

Bien que cela soit formidable, ce n'est pas une solution miracle. Gardez à l'esprit qu'Istio est relativement nouveau par rapport à d'autres solutions stables et éprouvées comme JHipster Registry (Eureka) ou Consul.

De plus, une autre chose à garder à l'esprit est les exigences en matière de ressources. Les mêmes microservices avec JHipster Registry ou Consul peuvent être déployés sur un cluster de 2 nœuds avec 1 vCPU et 3,75 Go de mémoire par nœud dans GCP, tandis que vous avez besoin d'un cluster de 4 nœuds avec 2 vCPU et 7,5 Go de mémoire par nœud pour les déploiements avec Istio activé. Le manifeste Kubernetes par défaut d'Istio n'applique aucune limite de demande pour les ressources, et en ajoutant et en ajustant celles-ci, l'exigence minimale pourrait être réduite. Mais je ne pense toujours pas que vous puissiez l'obtenir aussi bas que ce qui est nécessaire pour l'option de registre JHipster.

Dans un cas d'utilisation réel, les avantages de ne pas avoir à maintenir les parties complexes de votre infrastructure par rapport au fait de devoir payer pour plus de ressources pourraient être une décision qui doit être prise en fonction de vos priorités et objectifs.

Un énorme merci à [Ray Tsang](https://twitter.com/saturnism) pour m'avoir aidé à déterminer une taille de cluster optimale pour cette application. De plus, un énorme merci de ma part et de la communauté à Ray et [Srinivasa Vasu](https://twitter.com/humourmind) pour avoir ajouté le support Istio à JHipster.

JHipster fournit une excellente configuration Kubernetes pour commencer, que vous pouvez ensuite ajuster selon vos besoins et votre plateforme. Le support Istio est récent et s'améliorera avec le temps, mais c'est toujours un excellent point de départ, surtout pour apprendre.

Pour en savoir plus sur JHipster et le développement full stack, consultez mon livre « Full Stack Development with JHipster » sur [Amazon](https://www.amazon.com/Stack-Development-JHipster-Deepu-Sasidharan/dp/178847631X) et [Packt](https://www.packtpub.com/application-development/full-stack-development-jhipster).

Il y a un excellent tutoriel Istio de Ray Tsang [ici](https://docs.google.com/document/d/1Qo8o5C4UpGwMF7Mg02kLTaU4-xCSfJjLcnIFNveMEEA).

Si vous aimez JHipster, n'oubliez pas de lui donner une étoile sur [Github](https://github.com/jhipster/generator-jhipster).

Si vous aimez cet article, n'hésitez pas à laisser quelques applaudissements (Saviez-vous que vous pouvez applaudir plusieurs fois sur Medium ? ?) J'espère écrire davantage sur Istio dans un proche avenir.

Vous pouvez me suivre sur [Twitter](https://twitter.com/deepu105) et [LinkedIn](https://www.linkedin.com/in/deepu05/).

Mes autres articles liés :

1. [Créer une pile Microservice complète en utilisant le langage de domaine JHipster en moins de 30 minutes](https://medium.com/@deepu105/create-full-microservice-stack-using-jhipster-domain-language-under-30-minutes-ecc6e7fc3f77)
2. [Déploiement de microservices JHipster sur Azure Kubernetes Service (AKS)](https://medium.com/@deepu105/deploying-jhipster-microservices-on-azure-kubernetes-service-aks-fb46991746ba)