---
title: La sécurité comme norme dans le monde de Kubernetes.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-05T17:39:17.000Z'
originalURL: https://freecodecamp.org/news/security-as-standard-in-the-land-of-kubernetes-50bfad74ca16
coverImage: https://cdn-media-1.freecodecamp.org/images/1*PJxP2dKTiFWRnfG5p0tKGA.jpeg
tags:
- name: Docker
  slug: docker
- name: '#infosec'
  slug: infosec
- name: Kubernetes
  slug: kubernetes
- name: Security
  slug: security
- name: 'tech '
  slug: tech
seo_title: La sécurité comme norme dans le monde de Kubernetes.
seo_desc: 'By Chris Cooney

  Security in Kubernetes needs some work, but there are some clear steps a team can
  take to make sure their information is safe.

  I have been writing about Kubernetes for a while. I use it every day in my place
  of work. Our mission over ...'
---

Par Chris Cooney

La sécurité dans Kubernetes nécessite quelques efforts, mais il existe des étapes claires qu'une équipe peut suivre pour s'assurer que ses informations sont protégées.

J'écris sur Kubernetes depuis un certain temps. Je l'utilise tous les jours dans mon lieu de travail. Notre mission au cours des derniers mois a été de créer le Fort Knox des clusters Kubernetes. Si un attaquant parvient à traverser les couches de réseau, les pare-feu et les WAF, il se retrouvera avec très peu d'options. Cela est né d'un seul conseil que j'ai reçu des gentlemen de [LearnK8s](https://twitter.com/learnk8s).

> Kubernetes gérera automatiquement la haute disponibilité, les déploiements, la configuration et les secrets pour vous, mais il n'imposera pas la sécurité de lui-même. Cela nécessite quelques efforts.

Cela ne signifie pas que Kubernetes est _insecure_, c'est simplement une manière différente d'aborder le logiciel. Une manière qui favorise la livraison continue, les déploiements sans temps d'arrêt et la haute disponibilité. Kubernetes fera ces choses pour vous, avec un effort minimal. La sécurité, en revanche, nécessite un effort volontaire. Cela a été mon travail au cours des derniers mois et j'ai pensé partager les leçons que j'ai apprises. D'abord, l'idéal global que nous avions en tête.

### La sécurité comme norme

C'est simple. Il ne devrait pas être de la responsabilité de chaque ingénieur de s'assurer que chaque couche de son application, de son déploiement et de sa configuration est sécurisée. Pensez à la quantité de retravail impliquée dans cela.

* Le simple potentiel de dérive, la complexité introduite pour le support.
* Le silo que cela crée et l'architecture disjointée avec laquelle vous vous retrouvez, parce que tout le monde a une méthode légèrement différente basée sur son expérience.

L'objectif est de nécessiter _un effort minimal des développeurs_ et _une sécurité automatique maximale_.

### Alors, comment y parvenir ?

Cela constituera le cœur de cet article. J'ai compilé une liste d'outils et de pratiques que l'on peut utiliser pour aider à créer un écosystème technique qui offre un environnement sûr et sécurisé pour les ingénieurs.

Ce n'est en aucun cas une liste exhaustive. Plus un kit de démarrage. Il y a des idées fondamentales et d'autres plus expérimentales. Le truc est de trouver ce qui fonctionne pour vous, mais gardez à l'esprit les deux métriques — effort minimal des développeurs, sécurité automatique maximale.

### La NetworkPolicy de Kubernetes

Je n'ai aucun doute que la majorité des personnes lisant cet article connaissent déjà la `[NetworkPolicy](https://kubernetes.io/docs/concepts/services-networking/network-policies/)` dans Kubernetes. Lorsque vous commencez avec la sécurité dans un cluster Kubernetes, c'est l'or. En bref, elle permet à l'ingénieur de verrouiller quels autres services peuvent communiquer avec ce pod. Par exemple, vous pouvez créer une `NetworkPolicy` comme ceci :

```
kind: NetworkPolicyapiVersion: networking.k8s.io/v1metadata:  name: api-allowspec:  podSelector:    matchLabels:      app: my-app  ingress:  - from:      - podSelector:          matchLabels:            app: my-other-app
```

Nous avons déclaré quelque chose de très spécifique ici. Nous avons dit qu'il n'y a qu'une seule chose qui devrait pouvoir communiquer avec notre application. C'est un pod étiqueté avec `my-other-app`. Si un conteneur malveillant est créé à l'intérieur de votre cluster, toute tentative de communication avec `my-app` sera contrecarrée. Cependant, nous pouvons aller plus loin.

Les Network Policies ne sont pas seulement liées aux applications, mais elles peuvent être accrochées à des espaces de noms entiers, créant ainsi des règles de base qui régissent toutes les applications qui s'y trouvent. Vous pouvez donc créer une règle `default-deny`. Cela va essentiellement blacklister tout le trafic et une autre `NetworkPolicy` devra être créée pour whitelister la communication.

Nous avons cependant un problème. Tout le monde ne va pas créer et utiliser une `NetworkPolicy`. Elles sont parfois gênantes et délicates, les gens vont opter pour la facilité et choisir un conteneur ouvert. Jusqu'à présent, nous avons un effort élevé des développeurs et une sécurité élevée. Cela pose une question. Comment faciliter la vie des ingénieurs tout en maintenant un haut niveau de sécurité ? La réponse est _helm_.

### Utiliser Helm pour la cohérence

[Helm](https://helm.sh/) vous permet de regrouper de nombreuses ressources Kubernetes dans un seul _chart_. Son cas d'utilisation le plus courant est de rendre le déploiement de logiciels tiers trivial — vous pouvez parcourir la grande collection de [stable helm charts](https://github.com/helm/charts/tree/master/stable) à votre guise. Tout le monde qui compte a un chart là-bas et cela devrait être votre premier point de contact lorsque vous souhaitez rendre un outil open source disponible dans votre cluster Kubernetes.

Les ampoules devraient s'allumer à peu près maintenant. Et si nous pouvons créer notre propre chart helm et inclure une `NetworkPolicy` comme norme ? Nous pouvons y mettre toutes sortes de choses — `PodDisruptionBudget` ou `HorizontalPodAutoscaler` par exemple. Si vous pouvez vous assurer que vos ingénieurs utilisent votre chart helm pour leurs déploiements, vous pouvez également vous assurer que les bonnes ressources sont en place avec un effort minimal de leur part. Vous venez de réduire l'effort des développeurs tout en maintenant le même niveau de sécurité. Score !

Donc maintenant vos applications limitent qui elles peuvent et ne peuvent pas parler, mais comment savez-vous que votre application ne peut pas exécuter un tas de commandes destructrices sur les autres applications autour d'elle ?

### Contrôle d'accès basé sur les rôles (RBAC) pour les services

RBAC est une fonctionnalité très courante dans les clusters Kubernetes. Je vous conseille fortement de l'activer. Nous l'utilisons généralement pour les applications tierces et l'accès des développeurs, mais nous pouvons également l'utiliser pour notre logiciel, sous la forme de ressources `ServiceAccount`. Nous pouvons les lier à un `Role` ou `ClusterRole` spécifique et hop, plus de risque que les applications deviennent malveillantes à l'intérieur de votre cluster.

La documentation Kubernetes fait un excellent travail pour vous guider à travers les mécanismes de cela. [Lisez-la et soyez éclairé.](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#service-account-permissions) Mon seul conseil serait, une fois que vous avez compris l'essence, intégrez cela dans votre chart helm. Ne forcez pas les ingénieurs à le faire car tôt ou tard, ils vont l'éviter. Ou vous détester. Ou les deux. Souvenez-vous, effort minimal des développeurs.

### Validez votre Yaml avant le déploiement en utilisant Kubescore

Donc vous avez un chart helm badass pour vos applications, mais tout n'est pas une application. Il y a beaucoup de choses, comme les serveurs Nexus et les outils CI, qui ne seront pas déployés par les moyens typiques. Souvent, ce sera une commande `kubectl` malicieuse depuis la machine d'un ingénieur qui ouvrira la vulnérabilité la plus large.

Un truc est d'utiliser un outil nommé [kube-score](https://github.com/zegl/kube-score) pour fournir une mesure facile, cohérente et objective de la qualité d'un service. Un élément de confiance est nécessaire ici — vous pourriez concocter quelque chose pour empêcher l'application de tout yaml qui échoue, mais dans un premier temps, simplement faire connaître cet outil à vos ingénieurs est suffisant pour vous lancer.

### Testez votre configuration de cluster avec kube-bench

Il existe un outil brillant appelé [kube-bench](https://github.com/aquasecurity/kube-bench) qui analysera la configuration de vos nœuds. Cela testera des choses comme, si vous avez désactivé les conteneurs privilégiés et que votre kubelet communique avec les nœuds maîtres en HTTPS.

Comme pour tout, il est peu probable que vous passiez chaque métrique — cet outil est rigoureux. Concentrez-vous sur les grandes, tout ce que l'outil met en évidence comme critique. C'est un travail que vous pouvez faire en coulisses, sans perturber l'ingénierie, qui vous bénéficiera à long terme, si votre cluster tombe en proie à une vulnérabilité ailleurs.

### Créez un ensemble standard d'images Docker de base

Un trou béant dans tout cela est les conteneurs d'application eux-mêmes. Les vulnérabilités s'y glissent tout le temps et cette quantité inconnue crée un petit cachette merveilleux pour les bugs et vulnérabilités difficiles à diagnostiquer.

Cependant, tout n'est pas perdu. Les gentils chez Google ont travaillé sur [Distroless](https://github.com/GoogleContainerTools/distroless), un ensemble d'images docker qui fait ressembler docker alpine à Windows 10. Ces choses sont très, très limitées et ne donnent pas beaucoup de marge de manœuvre à un intrus.

Cela dit, vous n'avez pas besoin d'utiliser des images Distroless. Vous pouvez empaqueter les vôtres si vous êtes confiant dans votre maîtrise des conteneurs. L'objectif ici est de limiter la portée et l'échelle des images docker personnalisées et de les ramener à un ensemble gérable d'outils connus, et de les rendre disponibles à tous ceux qui en ont besoin.

#### Et méfiez-vous de la dernière balise

Assurez-vous que toutes les images docker déployées dans le cluster sont _fixées à une version_. La balise `latest` est un jeu dangereux en effet — vous n'avez absolument aucune idée du logiciel qui s'exécute après chaque recyclage de pod.

### Istio Mutual TLS

Si vous avez regardé [Istio](https://istio.io/), vous savez qu'il a très récemment annoncé la v1.0.0. C'est tout, les gars, ils sont prêts pour la production. Istio offre une pléthore absolue de surveillance, de traçage et de résilience. Il a également une fonctionnalité géniale pour activer le mutual TLS entre les applications gérées par Istio. Si votre application a un proxy envoy, vous êtes dans la bonne voie.

#### Mais qu'est-ce que le Mutual TLS ?

Le Mutual TLS est un peu comme HTTPS. Il implique qu'une partie vérifie l'existence de l'autre et, par la suite, établit un canal de communication chiffré. Cependant, HTTPS est basé sur le client vérifiant le serveur. Dans le mutual TLS, _deux clients se vérifieront mutuellement_.

#### Cela impacte-t-il les applications ?

C'est le côté cool. Istio Mutual TLS se produit en dehors de l'application, à l'intérieur du proxy envoy qui est couplé avec vos applications. Vos applications peuvent envoyer une requête en HTTP et Istio vérifiera silencieusement la source et chiffrera le trafic pour vous. Effort des développeurs ? Absolument rien. Avantages de sécurité ? Un chiffrement cryptographique fort en transit dans le cluster et un énorme blocage des attaques de l'homme du milieu (MITM). Pas mal du tout.

### Controversé : Interdire les types de service `LoadBalancer` et `NodePort` — Restreindre à ClusterIP

Celui-ci tend à diviser un peu la pièce. Nous voyons le type de service `LoadBalancer` apparaître partout dans les services. Il est souvent la configuration par défaut pour de nombreux charts helm qui cherchent à permettre le trafic entrant de l'extérieur du cluster. Il y a quelques sérieux inconvénients à cela :

* Les Load Balancers coûtent de l'argent, à la fois pour les coûts de transfert et le temps d'exécution. Les ingénieurs utiliseront ce qui est le plus facile et vous pouvez être sûr, à toute échelle raisonnable, que ces charges vont s'accumuler. Cela ne serait pas si grave, mais c'est complètement évitable.
* Chaque Load Balancer va parler à vos nœuds sur un port différent. Plus vous avez de ports ouverts, plus la surface d'attaque est grande.
* Qui sait quelle configuration se passe entre ces load balancers et leurs nœuds cibles. C'est totalement à la discrétion du contrôleur que vous avez installé.

#### Alors, que pouvons-nous faire à la place ?

Créez une seule voie d'entrée. Un seul Load Balancer. Pour nous, nous utilisons un [AWS ALB](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html), mais vous pouvez utiliser un [NLB](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html) ou un classique [ELB](https://aws.amazon.com/elasticloadbalancing/) si l'envie vous en prend. Le but du jeu est de créer une seule route et un seul ensemble de ports par lesquels le trafic circule. Cela minimise votre surface d'attaque. Avec toutes vos applications fonctionnant comme des instances `ClusterIP`, aucune exposition de port supplémentaire n'est nécessaire et le routage est fait pour vous par Kubernetes. La seule chose restante à faire est de choisir un seul contrôleur d'entrée à exécuter comme un `NodePort`, peut-être [NGINX](https://github.com/nginxinc/kubernetes-ingress) ou [Traefik](https://github.com/helm/charts/tree/master/stable/traefik), et hop ! Vous avez un réseau simple avec une minuscule surface d'attaque.

### Très controversé : Prendre le contrôle du processus de build et de déploiement

J'ai inclus celui-ci comme une pièce d'opinion. C'est beaucoup plus controversé que les autres que j'ai discutés. Les équipes aiment souvent posséder leurs propres pipelines de livraison continue (CD). C'est quelque chose qu'elles devront utiliser au quotidien. Il y a des désaccords classiques parmi les ingénieurs sur quel outil CI/CD utiliser.

#### Et cela ouvre un vecteur d'attaque, un gros.

Jusqu'à ce que vous sachiez, pas penser ou deviner, mais sachiez que vos ingénieurs utilisent l'automatisation qui a été mise en place, tous ces efforts pourraient être annulés par une seule configuration douteuse. Votre chart helm pourrait envelopper les services dans de la laine d'acier et les vaporiser avec de l'eau bénite, mais cela ne sert à rien s'il n'est pas utilisé.

En créant un processus CI/CD unifié, vous pouvez vous assurer que les vérifications appropriées sont utilisées. Cela a quelques sérieux avantages. Si vous souhaitez introduire un nouvel outil, vous le construisez en un seul endroit et tout le monde l'obtient immédiatement. Retravail minimal, effort minimal, bénéfice de sécurité maximal. Couronné par la cohérence entre les équipes.

L'option que nous avons choisie était [Global Shared Libraries](https://jenkins.io/doc/book/pipeline/shared-libraries/) dans Jenkins. Cela nous a permis de créer une seule base de code qui définissait les pipelines que tous les services utilisent. J'ai écrit [un autre article](https://hackernoon.com/simplifying-jenkinsfiles-c97cfee13f83) sur ce sujet, si vous souhaitez un regard plus approfondi. (Avertissement, langage fort.)

#### Mais un mot d'avertissement...

Réfléchissez bien à celui-ci. Vous prenez un énorme fardeau de maintenance et de fiabilité. Si cet outil CI/CD que vous avez construit est défectueux, cela impacte chaque développeur, immédiatement. C'est un point de défaillance unique et votre vie sera passée à éteindre des incendies. Réfléchissez bien avant de vous charger de cela.

#### Souvent, la confiance et l'éducation sont la meilleure solution...

À défaut de prendre le contrôle du processus CI/CD, la meilleure chose que vous puissiez faire est d'être impliqué dans la création de l'ensemble d'outils de chaque équipe. Répondez aux questions, parlez des capacités. Rendez-vous disponible pour donner des conseils aux équipes. Donnez aux gens l'autonomie et la responsabilité de leur propre solution en leur montrant à quoi ressemble une bonne solution. Cette approche n'offre pas de garanties, mais elle présente une charge opérationnelle beaucoup plus gérable.

### D'accord, je suis à court.

J'ai évité de discuter des techniques de réseau spécifiques que nous avons employées et j'ai esquivé comment nous pouvons écrire nos applications de manière plus sécurisée. Le truc ici a été d'obtenir quelques victoires rapides qui réduiront sérieusement la surface d'attaque de tout cluster Kubernetes tout en nécessitant très peu d'efforts de la part de vos ingénieurs logiciels.

Amusez-vous bien dans votre voyage. Kubernetes est un outil brillant et avec un peu d'amour et d'attention, il peut former une plateforme incroyable pour vos équipes d'ingénierie.

Je suis pleinement dans le train Kubernetes et j'en parle tout le temps sur mon [twitter](https://twitter.com/chris_cooney).