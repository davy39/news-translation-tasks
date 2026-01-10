---
title: Comment démarrer avec Istio
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-29T17:04:03.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-istio-up-and-running-1935dc7cfb90
coverImage: https://cdn-media-1.freecodecamp.org/images/1*bL7D9agHyer92fD2VLkd6g.jpeg
tags:
- name: Devops
  slug: devops
- name: '#istio'
  slug: istio
- name: Kubernetes
  slug: kubernetes
- name: service mesh
  slug: service-mesh
seo_title: Comment démarrer avec Istio
seo_desc: 'By Chris Cooney

  And the crazy stuff you can do once it is.


  An actual picture of me when Kiali started working

  The moment you get Istio working on your cluster, it feels like you’ve taken quite
  a serious leap forward. The level of monitoring, securit...'
---

Par Chris Cooney

#### Et les choses folles que vous pouvez faire une fois qu'il est opérationnel.

![Image](https://cdn-media-1.freecodecamp.org/images/mvyypII5oA3zu6KFPReosnlq95i6UhFHvSAs)
_Une vraie photo de moi quand Kiali a commencé à fonctionner_

Le moment où vous faites fonctionner [Istio](https://istio.io/) sur votre cluster, on a l'impression d'avoir fait un bond en avant sérieux. Le niveau de surveillance, de sécurité et de fonctionnalité que vous gagnez immédiatement est des années-lumière devant la concurrence. Il y a quelques mois, nous avons sauté le pas et installé Istio sur notre cluster Kubernetes et... wow. Nous commencerons par le début, avec l'installation et les pièges que nous avons trouvés, puis un aperçu des outils que nous avons trouvés les plus utiles.

### Faire démarrer le moteur.

La manière la plus facile et la plus efficace d'installer Istio est d'utiliser le chart Helm. Vous obtenez une installation prête pour la production dès la sortie de la boîte. Vous avez quelques options, mais Istio fournit une commande de téléchargement pratique pour que vous puissiez télécharger une version groupée du chart Helm d'Istio. La commande suivante vous permettra d'obtenir la version `1.0.6` du package Istio.

```
curl -L https://git.io/getLatestIstio | ISTIO_VERSION=1.0.6 sh -
```

Dans ce package téléchargé, se trouve un petit chart Helm pratique. Il est situé dans `install/kubernetes/helm/istio`. Une fois que vous êtes dans ce répertoire, c'est une simple installation Helm. Nous préférons utiliser `helm upgrade --install` plutôt qu'une installation directe afin que la même commande puisse être automatisée :

```
helm upgrade istio . -f values.yaml \
--namespace istio-system \
--install
```

Cela utilisera le fichier `values.yaml` par défaut fourni dans le dossier. Vous pouvez modifier ce fichier pour activer ou désactiver différentes fonctionnalités.

#### Une note sur la désinstallation d'Istio

Le bon sens dicterait qu'un `helm delete --purge istio` supprimerait toutes les ressources Istio, mais il ne supprime pas les types `CustomResourceDefinition`. Nous avons dû fouiller et supprimer les CRD manuellement. Nous avons fini par scripter cela. Juste quelque chose à garder à l'esprit.

Une fois installé, nous avons configuré quelques endpoints et commencé à examiner ce que notre nouveau cluster pouvait faire. Oh là là, nous n'avons pas été déçus.

### Configurer Istio

La dernière chose à faire est d'annoter un namespace pour indiquer qu'Istio peut effectuer une injection automatique de sidecar. C'est la manière la plus simple d'utiliser Istio. L'annotation est simple. Un exemple de fichier yaml de namespace que vous pourriez utiliser est le suivant :

```
apiVersion: v1
kind: Namespace
metadata:
  name: my-namespace
labels:
  istio-injection: enabled
```

Toutes les applications déployées dans ce namespace obtiendront un proxy envoy. Ce proxy analysera votre trafic réseau et publiera sur le serveur Prometheus d'Istio, où les systèmes en aval pourront en faire usage.

#### Comment savoir si j'ai un proxy Envoy ?

C'est simple, exécutez `kubectl get pods` dans votre namespace souhaité. Vous verrez quelque chose comme ceci :

```
my-application-pod   2/2     Running   0          2d
```

En supposant que vous ne déployez qu'un seul conteneur par pod, un deuxième conteneur apparaîtra maintenant. Ce deuxième conteneur est votre proxy envoy. S'il est là et qu'il est prêt, vous êtes prêt à partir.

### Kiali

Je commence directement avec mon préféré. [Kiali](https://www.kiali.io/) fournit des diagrammes de réseau en direct et des statistiques HTTP pour vos applications. C'est un vrai plaisir pour la foule et il vous donne un excellent tableau de bord "à première vue".

![Image](https://cdn-media-1.freecodecamp.org/images/BtfRZZ2N1UUo-acrrVgUwwuSxbzBJRvRNvG7)
_Kiali vous donne une visibilité sérieuse_

Regardez le côté droit de cette image. En plus du haut niveau de visibilité, vous obtenez des détails. Vous pourriez mettre l'aperçu du réseau sur un écran de télévision. Lorsque l'une de ces lignes devient rouge, vous pouvez creuser dans les détails HTTP sous le capot.

#### Particularités de Kiali

Vous pourriez voir du trafic provenant d'"inconnu" dans Kiali, comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/Xa4WzV7JZCdCz3FlU-jO5iJAXt2lyfG3FpoK)
_Est-ce un hacker !?_

Il s'agit en fait de la vérification de santé de Kubernetes. Ce n'est rien d'alarme. Vous pouvez cacher cela en faisant l'une des choses suivantes :

* Ajustez votre vérification de santé pour utiliser un exec local sur le conteneur Docker, plutôt qu'une vérification basée sur HTTP. C'est un peu bidouillé.
* Utilisez un port différent de celui de votre application principale pour votre vérification de santé. C'est la direction que nous avons prise, ce qui ouvre également une autre porte pour (plus sur cela plus tard)

Istio travaille sur ce problème et il y a une correction dans la toute nouvelle version v1.1.

### Grafana

Istio remplira immédiatement une instance [Grafana](https://grafana.com/) pour vous. Cette instance Grafana est absolument remplie de métriques d'application utiles, alimentées par les données publiées par le proxy envoy de chaque application.

Dès que vous déployez une nouvelle application avec un proxy envoy, vous obtenez des métriques qui prennent généralement des semaines aux équipes pour être rassemblées :

![Image](https://cdn-media-1.freecodecamp.org/images/WM8SF6YLawPNAkB2424r0qseKYNhXH9GKFjX)
_Oh oui._

Il est important de reconnaître, _je n'ai pas configuré tout cela_. Istio est suffisamment impliqué dans votre système pour extraire tout cela pour vous. Et pour couronner le tout, ceci est l'un des nombreux tableaux de bord. Il y en a des tonnes, plus que je pense jamais utiliser. Dans le cas de la surveillance, plus c'est mieux. Je préfère avoir trop de détails et les réduire, plutôt que de n'avoir aucune visibilité du tout.

### Prometheus

C'est le moteur derrière tout ce qui se passe. [Prometheus](https://prometheus.io/) scrape et agrège d'énormes quantités de données et les présente de manière pratique. Je n'ai pas eu à passer beaucoup de temps à jouer avec, pour vous dire la vérité. Les services Istio fournissent une fonctionnalité incroyablement utile, prête à l'emploi. Prometheus peut être utilisé pour écrire vos propres graphiques ou scraper des métriques personnalisées à partir de vos applications.

Sur la base de ces données, vous pouvez déclencher des alertes en utilisant Alert Manager, créant ainsi une plateforme de surveillance et d'alerte hautement sophistiquée pour vos applications.

### Le contrôle que vous gagnez

En plus de tout cela, Istio dispose de quelques utilitaires intégrés qui repoussent vraiment les limites. Vous pourrez déclencher des pannes, provoquer des interruptions, blackholer le trafic et bien plus encore. J'ai détaillé quelques-unes des fonctionnalités cool que j'ai eu l'occasion d'essayer, mais il y en a bien plus.

#### Injection de pannes

Avec Istio, vous pouvez injecter des échecs. Par exemple, le YAML suivant provoquera le retour d'un code d'état HTTP 500 pour 100 % des requêtes. Utile lorsque vous simulez une panne d'un tiers.

```
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: ratings
spec:
  hosts:
  - ratings
  http:
  - fault:
      abort:
        httpStatus: 500
        percent: 100
    match:
    - headers:
        end-user:
          exact: json
    route:
    - destination:
        host: ratings
        subset: v
```

La documentation est assez bonne et vous pouvez plonger dans toutes sortes de fonctionnalités. Ce que je fais ici, c'est simplement vous montrer la surface.

#### Politiques de résilience par défaut

À quelle fréquence avez-vous écrit une logique pour implémenter des nouvelles tentatives ? Charger tout cela à l'avance dans un produit rend difficile la concentration sur la valeur commerciale spécifique. Istio simplifie cela. Par exemple, en intégrant les nouvelles tentatives :

```
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
    name: ratings
spec:
    hosts:
    — ratings
    http:
    — route:
        — destination:
            host: ratings
            subset: v1
        retries:
            attempts: 3
            perTryTimeout: 2s
```

Cela garantira que les requêtes effectuées par votre service sont réessayées trois fois, avec un délai d'attente de deux secondes pour chacune. Plus de pollution de votre code d'application — chargez cela dans le service mesh et gardez vos services simples.

#### Mutual TLS

Le chiffrement de service à service peut être difficile. S'assurer que les certificats n'expirent pas est une opération sérieuse... mais pas avec Istio. Istio utilise le pod de gestion des certificats pour s'assurer que vos applications ont leur propre certificat, tout neuf.

Ensuite, avec la bonne `DestinationRule`, vous pouvez imposer que vos applications n'autorisent que le trafic chiffré TLS. Cela garantit que toute la communication inter-cluster est verrouillée. L'application n'en a aucune idée. Elle émet la requête en HTTP et le sidecar proxy Envoy la mettra transparemment à niveau vers Mutual TLS. La règle de destination suivante garantira que toutes les requêtes vers `v1` du service `productpage` **doivent** être chiffrées en utilisant Mutual TLS.

```
apiVersion: networking.istio.io/v1alpha3
kind: DestinationRule
metadata:
  name: productpage
spec:
  host: productpage
  trafficPolicy:
    tls:
      mode: ISTIO_MUTUAL
  subsets:
  - name: v1
    labels:
      version: v1
```

### Il n'y a pas de repas gratuit

Comme pour tout, il y a quelques dangers et compromis. Istio est brillant, je suis vraiment impressionné. Il est facile de dérailler et de se retrouver avec un mash de services, plutôt qu'un mesh de services.

#### Couches d'intégration désordonnées

Quiconque a travaillé dans une organisation suffisamment grande a vu cela. Des "couches d'intégration" initialement conçues pour lier deux applications ensemble. Ensuite, elles obtiennent un peu de logique supplémentaire, quelques fichiers ici et là, quelques règles de routage saupoudrées par-dessus et tout à coup, elles deviennent un nid de complexité.

Soyez prudent avec Istio à cet égard. Il est extrêmement puissant mais nécessite une réflexion minutieuse. Certaines fonctionnalités sont cool mais vous n'en avez peut-être pas réellement besoin. Et parfois, osez-je le dire, un peu de répétition dans les microservices est plus souhaitable qu'un service mesh avec plus de logique que vos applications réelles.

#### Complexité

Kubernetes offre beaucoup à apprendre. La courbe d'apprentissage est assez douce, surtout par rapport aux alternatives, mais le domaine est vaste. Lorsque vous introduisez Istio, vous introduisez également une série de nouveaux concepts, plus complexes. Les types `VirtualService` et `Gateway` de Custom Resource Definitions avec lesquels vous devrez vous familiariser.

C'est un compromis. Regardez votre cluster ou votre équipe et décidez. Notre surveillance fait-elle parfaitement le travail ? Nos applications sont-elles résilientes ? Les ingénieurs se plaignent-ils de la répétition de la logique ? Assurez-vous d'obtenir quelque chose en retour pour cette complexité et ce compromis est une évidence. Ne vous endormez simplement pas dans un cauchemar.

#### Cela change... rapidement

Istio a récemment annoncé qu'il était prêt pour la production et avec sa version `1.1`, il a abordé beaucoup des préoccupations existantes. Cela dit, il s'agit d'un nouveau produit. Si vous êtes le type d'organisation qui a du mal à suivre, le rythme auquel Istio évolue pourrait vous être préjudiciable. Prendre du retard pourrait être catastrophique, surtout si des vulnérabilités de sécurité et des bugs apparaissent.

Une fois de plus, c'est un fardeau avec lequel vous devez raisonner. Avez-vous la capacité de suivre ? Si ce n'est pas le cas, pourriez-vous ? Et même si vous le pouviez, cela en vaut-il la peine ? Avez-vous vraiment besoin de cette charge opérationnelle supplémentaire ?

### C'est tout pour aujourd'hui

J'ai donné les points forts de mon expérience avec Istio. J'ai personnellement utilisé toutes les fonctionnalités de cet article et cela a été exceptionnel. Nous avons vu quelques particularités, mais rien qui nous ait donné beaucoup à réfléchir. Dans l'ensemble, à condition que vous ayez une situation qui en a besoin, Istio fait passer votre cluster au niveau supérieur.

Je parle d'Istio, de Kubernetes et de DevOps régulièrement, sur mon [compte twitter](https://twitter.com/chris_cooney).