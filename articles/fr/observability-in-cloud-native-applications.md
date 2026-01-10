---
title: Guide du débutant pour l'observabilité dans les applications cloud native
subtitle: ''
author: Victoria Nduka
co_authors: []
series: null
date: '2025-03-25T16:14:36.364Z'
originalURL: https://freecodecamp.org/news/observability-in-cloud-native-applications
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1742917070693/fa372981-fb20-4230-bd9f-43b7255b8ced.png
tags:
- name: otlp resource attributes
  slug: otlp-resource-attributes
- name: cloud native applications
  slug: cloud-native-applications
- name: observability
  slug: observability
- name: '#prometheus'
  slug: prometheus
- name: OpenTelemetry
  slug: opentelemetry
- name: Otel
  slug: otel
seo_title: Guide du débutant pour l'observabilité dans les applications cloud native
seo_desc: 'If you''re new to cloud native technologies, you may have heard the term
  ''observability'' before. But what exactly does it mean? Is it simply the ability
  to observe? And if so, what are we observing and why?

  I had the same questions when I started lear...'
---

Si vous êtes nouveau dans les technologies cloud native, vous avez peut-être déjà entendu le terme "observabilité". Mais que signifie-t-il exactement ? Est-ce simplement la capacité d'observer ? Et si oui, qu'observons-nous et pourquoi ?

J'avais les mêmes questions lorsque j'ai commencé à apprendre les technologies cloud native. Dans cet article, je vais partager ma compréhension des concepts clés de l'observabilité, présenter les outils essentiels et partager des informations sur un projet connexe sur lequel je travaille.

## Table des matières

* [Mon introduction aux technologies cloud native](#heading-mon-introduction-aux-technologies-cloud-native)

* [Qu'est-ce que l'observabilité ?](#heading-quest-ce-que-lobservabilite)

* [Types de données d'observabilité](#heading-types-de-donnees-dobservabilite)

    * [1. Métriques](#heading-1-metriques)

    * [2. Journaux](#heading-2-journaux)

    * [3. Traces](#heading-3-traces)

* [Outils d'observabilité](#heading-outils-dobservabilite)

    * [Prometheus](#heading-prometheus)

    * [OpenTelemetry](#heading-opentelemetry)

* [Qu'est-ce que les attributs de ressource OTLP ?](#heading-quest-ce-que-les-attributs-de-ressource-otlp)

* [Importance des attributs de ressource OTLP](#heading-importance-des-attributs-de-ressource-otlp)

* [Comment mon projet s'intègre dans tout cela](#heading-comment-mon-projet-sintegre-dans-tout-cela)

* [Conclusion](#heading-conclusion)

* [Ressources supplémentaires](#heading-ressources-supplementaires)

## Mon introduction aux technologies cloud native

J'ai récemment été sélectionné comme mentoré pour le programme de mentorat de la Linux Foundation afin de travailler sur le [projet CNCF - Prometheus](https://mentorship.lfx.linuxfoundation.org/project/36e3f336-ce78-4074-b833-012015eb59be). Le projet est axé sur l'UX, et au cours des prochains mois, je travaillerai avec mes mentors pour comprendre comment les utilisateurs s'attendent à utiliser les attributs de ressource OTLP (OpenTelemetry Line Protocol) dans Prometheus.

C'est un peu compliqué, je sais. J'étais submergé au début, et honnêtement, je suis encore en train de comprendre. Nous sommes dans ma troisième semaine, et bien que j'aie encore beaucoup à apprendre—sachant que je n'avais aucune connaissance des technologies cloud native lorsque j'ai postulé pour ce stage—j'ai déjà appris beaucoup.

Comme je le fais souvent, j'ai l'intention de documenter ce que j'apprends à travers des articles pour aider à renforcer les concepts dans ma mémoire et servir de ressource pour d'autres nouveaux venus qui pourraient se retrouver aux prises avec ces termes techniques à l'avenir. Vous savez ce qu'on dit : on ne peut pas dire qu'on a compris quelque chose tant qu'on n'est pas capable de l'expliquer à quelqu'un d'autre qui est aussi nouveau sur le sujet.

## Qu'est-ce que l'observabilité ?

Tout d'abord, j'ai dû apprendre ce que signifiaient les termes inconnus—et il y en avait beaucoup. OpenTelemetry. Prometheus. Attributs de ressource. J'ai fini par comprendre que ces termes relèvent d'un même domaine : l'observabilité. Commençons par là.

Prenons l'exemple d'une application de livraison de nourriture pour illustrer. Lorsque quelqu'un commande de la nourriture, beaucoup de choses se passent en coulisses :

* L'application se connecte à différents services (restaurants, paiements, livraison)

* Les données circulent entre différents systèmes pour traiter la commande, attribuer un livreur et suivre la livraison

Les ingénieurs doivent surveiller tous les processus pour s'assurer que tout fonctionne correctement. Les commandes prennent-elles trop de temps à être traitées ? Le système de paiement est-il en panne ? L'application plante-t-elle soudainement sous charge ? Quelle partie du système cause des retards ?

Pour répondre à ces questions, les ingénieurs **instrumentent** leur code. Cela signifie qu'ils le configurent pour renvoyer des données en temps réel sur l'état, les performances et le comportement de l'application. Cette pratique de compréhension de ce qui se passe à l'intérieur d'un système complexe en fonction des données qu'il génère est connue sous le nom d'**observabilité**.

Vous pouvez voir le processus illustré dans l'image ci-dessous :

![Un diagramme de flux intitulé "Flux visuel des données d'observabilité" montrant comment les données circulent à travers un système d'application de livraison de nourriture. Le flux commence avec un utilisateur qui commande de la nourriture à partir d'une application de nourriture. L'application de nourriture se connecte à trois services (Restaurant, Paiement et Livraison). Tous ces composants envoient des données à OpenTelemetry, qui collecte trois types de données : Métriques, Journaux et Traces. OpenTelemetry transmet ensuite uniquement les données de métriques à Prometheus, qui stocke les métriques.](https://cdn.hashnode.com/res/hashnode/image/upload/v1742335445056/5fe7bb0b-bdf9-4f52-a2c1-7f2977411c6c.png align="center")

Dans le diagramme de flux ci-dessus, vous pouvez voir comment les données pourraient circuler à travers un système d'application de livraison de nourriture. Le flux commence avec un utilisateur qui commande de la nourriture à partir d'une application de nourriture. L'application de nourriture se connecte à trois services (Restaurant, Paiement et Livraison). Tous ces composants envoient des données à OpenTelemetry, qui collecte trois types de données : Métriques, Journaux et Traces. OpenTelemetry transmet ensuite uniquement les données de métriques à Prometheus, qui stocke les métriques.

## Types de données d'observabilité

Il existe trois types clés de données que les systèmes génèrent pour l'observabilité :

### **1. Métriques**

Les métriques sont des mesures numériques collectées au fil du temps qui représentent l'état ou les performances de votre système. Des exemples dans une application de livraison de nourriture seraient le nombre de commandes traitées par minute, le temps moyen de traitement des commandes en millisecondes, le nombre d'utilisateurs actifs ou de livreurs, et ainsi de suite.

### **2. Journaux**

Les journaux sont des enregistrements textuels d'événements discrets qui se produisent dans votre application. Les journaux pour notre application de livraison de nourriture pourraient ressembler à ceci :

```http
ERREUR : Paiement échoué pour la commande #12345 - Carte de crédit refusée
INFO : Livreur #789 attribué à la commande #12345
```

### **3. Traces**

Les traces suivent l'ensemble du cycle de vie d'une requête lorsqu'elle passe par différents services dans un système. Elles aident les ingénieurs à voir comment différents composants interagissent et à identifier les goulots d'étranglement dans des systèmes complexes et distribués.

Par exemple, dans notre application de livraison de nourriture, une seule requête de commande pourrait passer par les étapes suivantes :
`L'utilisateur passe une commande` → `Requête envoyée au système de restaurant` → `Processeur de paiement vérifie le paiement` → `Système de livraison attribue un livreur` → `L'utilisateur reçoit une confirmation`.

Chaque étape de ce parcours est enregistrée dans le cadre d'une trace. Cela aide les ingénieurs à identifier où se produisent les retards et à optimiser le système pour de meilleures performances.

L'observabilité repose sur les métriques, les journaux et les traces travaillant ensemble pour fournir une visibilité complète du système. Les métriques vous indiquent qu'il y a un problème (« Le taux d'erreur a augmenté de 5 % »). Les journaux vous indiquent pourquoi cela s'est produit (« Paiement échoué en raison de détails de carte invalides »). Les traces montrent exactement où cela s'est produit (« Retard dans la réponse du service de restaurant »).

## **Outils d'observabilité**

Les outils d'observabilité vous donnent une visibilité sur ce qui se passe dans votre application. Il en existe beaucoup, mais pour les besoins de cet article, nous parlerons de deux d'entre eux : Prometheus et OpenTelemetry.

### **Prometheus**

[Prometheus](https://prometheus.io/) est un kit d'outils de surveillance et d'alerte open source. Il fait deux choses :

* Collecte des données à partir d'applications, spécifiquement des métriques (rappel des types de données dont nous avons parlé précédemment)

* et les stocke dans une base de données de séries temporelles.

Une base de données de séries temporelles est une base de données spécialement conçue pour gérer des mesures ou des événements qui se produisent au fil du temps.

Prometheus utilise ce qu'on appelle un **modèle basé sur la récupération** pour collecter des métriques à partir d'applications. Basé sur la récupération signifie que Prometheus demande activement (récupère) des données auprès des services à intervalles réguliers. Pensez à cela comme à l'actualisation d'une page web pour obtenir le dernier contenu.

### **OpenTelemetry**

[OpenTelemetry (OTel)](https://opentelemetry.io/) collecte, traite et exporte des données d'observabilité. Contrairement à Prometheus, qui se concentre principalement sur les métriques, OpenTelemetry fournit une manière standardisée d'instrumenter des applications pour les trois types de données d'observabilité : journaux, métriques et traces.

OpenTelemetry est conçu pour être agnostique aux fournisseurs. Cela signifie que vous pouvez instrumenter vos applications une fois avec OpenTelemetry, puis envoyer ces données de télémétrie à n'importe quel backend d'observabilité pris en charge, qui pourrait être une solution open source comme Jaeger ou Prometheus, ou des plateformes commerciales comme Datadog, New Relic, Dynatrace ou Honeycomb.

Ainsi, par exemple, vous pouvez utiliser OpenTelemetry pour instrumenter votre application, puis Prometheus peut récupérer les métriques à partir d'OpenTelemetry tandis que d'autres outils gèrent les journaux et les traces.

## **Qu'est-ce que les attributs de ressource OTLP ?**

Lorsque OpenTelemetry collecte des données à partir d'applications, il fait plus que simplement rassembler des données de télémétrie brutes. Il fournit également un contexte sur ces données. Ce contexte se présente sous la forme d'**attributs de ressource**, qui décrivent d'où proviennent les données et à quoi elles se rapportent.

La "ressource" est le composant (ou l'entité) produisant les données, tandis que les "attributs" sont des détails spécifiques sur cette ressource.

Les attributs de ressource sont structurés sous forme de paires d'informations :

* La "clé" est le nom ou l'identifiant de l'attribut (comme `service.name` ou `host.id`)

* La "valeur" est l'information spécifique pour cet attribut (comme `payment-service` ou `server-123`)

Ensemble, ces paires clé-valeur identifient et décrivent le composant spécifique qui génère les données d'observabilité.

Par exemple, si un service de traitement des paiements envoie des métriques sur les temps de transaction, les attributs de ressource pourraient inclure :

* `service.name: "payment-service"`

* `service.version: "1.2.3"`

* `deployment.environment: "production"`

Ces attributs vous indiquent exactement quel service, quelle version et dans quel environnement les données proviennent, fournissant un contexte pour interpréter les métriques, les journaux ou les traces.

Les attributs de ressource ne sont pas arbitraires. OpenTelemetry fournit un ensemble standardisé de noms d'attributs et de formats que tout le monde devrait suivre, similaire à avoir une langue convenue pour décrire les services et leurs propriétés.

Par exemple, OpenTelemetry spécifie que vous devez utiliser `service.name` (et non `app_name` ou `service_id`) pour identifier votre service. Ils ont créé ces conventions de nommage standardisées (appelées [conventions sémantiques](https://opentelemetry.io/docs/concepts/semantic-conventions/)) afin que :

1. Tous les outils de l'écosystème puissent comprendre les mêmes attributs

2. Les ingénieurs de différentes entreprises utilisent une terminologie cohérente

3. Les données d'observabilité puissent être facilement partagées entre différents systèmes

Vous pouvez toujours créer vos propres attributs personnalisés lorsque vous avez besoin de quelque chose de spécifique (comme `payment.provider` pour un service de paiement), mais l'utilisation des attributs standard chaque fois que possible signifie que vos données de télémétrie fonctionneront mieux avec les outils existants et seront plus facilement comprises par d'autres ingénieurs.

## Importance des attributs de ressource OTLP

Supposons que les ingénieurs veulent surveiller combien de temps prennent les livraisons de nourriture et s'il y a des retards dans des lieux spécifiques. Sans attributs de ressource, OpenTelemetry pourrait simplement collecter et rapporter cette métrique comme ceci :

```yaml
delivery_time_seconds: 1800
```

Cela nous indique qu'une livraison a pris 1 800 secondes, soit 30 minutes, mais rien d'autre. C'est utile, mais cela manque de contexte. Où cela s'est-il produit ? Quel service l'a géré ? S'il y avait un retard dans la livraison et que les ingénieurs voulaient enquêter sur la cause, cela seul ne les aiderait pas.

Avec les attributs de ressource d'OpenTelemetry, la métrique devient plus significative :

```yaml
delivery_time_seconds: 1800
resource:
  service.name: "delivery-service"
  service.instance.id: "instance-456"
  cloud.region: "ng-west-2"
  deployment.environment: "production"
  customer.city: "Lagos"
  restaurant.id: "rest-789"
```

Cela nous indique :

* Les données proviennent du service de livraison.

* L'instance traitant la demande est "instance-456".

* Elle s'exécute dans la région cloud ng-west-2.

* L'environnement est Production (et non test ou staging), et ainsi de suite.

Maintenant, les ingénieurs peuvent répondre à des questions plus spécifiques :

* Les livraisons sont-elles plus lentes dans certaines villes ? (Filtrer par `customer.city`)

* Certains restaurants prennent-ils plus de temps à préparer la nourriture ? (Filtrer par `restaurant.id`)

* Les retards ne se produisent-ils que dans une région cloud spécifique ? (Filtrer par `cloud.region`)

* Les problèmes ne se produisent-ils qu'en production ou aussi en staging ? (Filtrer par `deployment.environment`)

Lorsque des problèmes surviennent, les attributs de ressource permettent aux ingénieurs de réduire rapidement la source des problèmes. Plutôt que d'enquêter sur chaque service, ils peuvent filtrer par des attributs spécifiques pour concentrer leurs efforts.

## **Comment mon projet s'intègre dans tout cela**

De nombreux ingénieurs utilisent OpenTelemetry pour la collecte de données, puis envoient les métriques à Prometheus pour le stockage, les requêtes et l'analyse.

Mais Prometheus ne prend pas en charge nativement les attributs de ressource de la même manière qu'OpenTelemetry. Au lieu de cela, il repose sur des labels pour organiser les métriques. Comme Prometheus a traditionnellement son propre système de labellisation pour les métriques, l'intégration des attributs de ressource d'OpenTelemetry crée des défis UX intéressants.

Un défi clé est l'**explosion de cardinalité**. La cardinalité fait référence au nombre de combinaisons uniques de valeurs de labels (ou dimensions) qu'une métrique peut avoir. Une "explosion de cardinalité" se produit lorsque vous ajoutez des labels avec de nombreuses valeurs possibles. OpenTelemetry inclut souvent de nombreux attributs détaillés qui, s'ils sont directement convertis en labels Prometheus, créeraient un nombre écrasant de séries temporelles. Cela peut ralentir considérablement Prometheus ou même le faire planter.

La solution existante consiste à regrouper tous les attributs de ressource dans un seul label Prometheus encodé en JSON. Bien que cela empêche l'explosion de cardinalité, cela rend les requêtes extrêmement fastidieuses. Les utilisateurs doivent utiliser des opérations de jointure complexes et une syntaxe de requête spécialisée pour filtrer ou agréger en fonction de ces attributs.

Cette approche est techniquement fonctionnelle mais crée une mauvaise expérience utilisateur. Ma recherche vise à comprendre comment les utilisateurs modélisent mentalement la transition du système d'attributs riche d'OpenTelemetry vers le système de labels plus contraint de Prometheus.

Les objectifs de la recherche sont de :

1. Comprendre comment les ingénieurs utilisent actuellement les attributs de ressource OpenTelemetry avec Prometheus

2. Identifier les points de douleur dans l'intégration actuelle entre ces systèmes

3. Découvrir les attentes des utilisateurs quant à la manière dont les attributs de ressource devraient être représentés dans Prometheus

Ce travail est particulièrement important alors que de plus en plus d'organisations adoptent OpenTelemetry comme norme d'instrumentation tout en continuant à utiliser Prometheus pour la surveillance des métriques. Créer une expérience transparente entre ces deux projets open source populaires aidera à améliorer l'écosystème global de l'observabilité.

## Conclusion

L'observabilité dans les applications cloud native est clairement un sujet intéressant et important pour construire des systèmes fiables et performants. Les outils et concepts que nous avons explorés—métriques, journaux, traces, Prometheus et OpenTelemetry—constituent la base des pratiques modernes d'observabilité.

Alors que je continue mon programme de mentorat, je partagerai plus d'informations sur le fonctionnement de ces technologies et essayerai de les décomposer du point de vue d'un apprenant débutant.

## Ressources supplémentaires

En savoir plus sur :

1. [OpenTelemetry](https://opentelemetry.io/docs/)

2. [Prometheus](https://prometheus.io/docs/introduction/overview/)

3. [Mon projet de recherche UX](https://github.com/prometheus/prometheus/issues/15909)