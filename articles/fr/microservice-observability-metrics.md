---
title: Comment utiliser les métriques pour surveiller vos microservices
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-12-30T16:49:38.000Z'
originalURL: https://freecodecamp.org/news/microservice-observability-metrics
coverImage: https://www.freecodecamp.org/news/content/images/2020/12/Microservice-Observability
seo_title: Comment utiliser les métriques pour surveiller vos microservices
---

Metrics.png
étiquettes:
- name: gestion des erreurs
  slug: gestion-des-erreurs
- name: journalisation
  slug: journalisation
- name: métriques
  slug: metriques
- name: Microservices
  slug: microservices
seo_title: null
seo_desc: "Par Siben Nayak\nDans mon article précédent, j'ai parlé de l'importance des\
  \ journaux et des différences entre la journalisation structurée et non structurée. \nLes journaux sont\
  \ faciles à intégrer dans votre application, et ils vous donnent la possibilité de représenter\
  \ n'importe quel type de données sous forme de chaînes de caractères."
---

Par Siben Nayak

Dans mon [article](https://www.freecodecamp.org/news/how-to-handle-logs-in-microservices/) précédent, j'ai parlé de l'importance des journaux et des différences entre la journalisation structurée et non structurée.

Les journaux sont faciles à intégrer dans votre application, et ils vous donnent la possibilité de représenter n'importe quel type de données sous forme de chaînes de caractères.

Les métriques, en revanche, sont des représentations numériques de données. Elles sont souvent utilisées pour compter ou mesurer une valeur et sont agrégées sur une période de temps.

Les métriques nous donnent des informations sur l'état historique et actuel d'un système. Comme ce ne sont que des nombres, nous pouvons également les utiliser pour effectuer des analyses statistiques et des prédictions sur le comportement futur du système.

Vous pouvez également utiliser les métriques pour déclencher des alertes et vous informer des problèmes dans le comportement du système.

# Journaux vs. Métriques

## Comment les journaux et les métriques sont formatés

Les journaux sont représentés sous forme de chaînes de caractères. Ils peuvent être du texte simple, des charges utiles JSON ou des paires clé-valeur (comme nous l'avons discuté dans la journalisation structurée).

Une entrée de journal typique ressemble à ceci :

```
[2020-09-27T18:54:41,500+0530]-[ERROR]-[InventoryValidator]-[13] Exception lors de la récupération des informations sur le produit - Produit Non Disponible
```

Les métriques sont représentées sous forme de nombres. Elles mesurent quelque chose (comme l'utilisation du CPU, le nombre d'erreurs, etc.) et sont de nature numérique.

Une métrique typique ressemble à ceci :

```
{class=InventoryValidator, exception=Produit Non Disponible, timestamp=1609306200}
```

## La résolution des journaux et des métriques

Les journaux contiennent des données à haute résolution. Cela inclut des informations complètes sur un événement et peut être utilisé pour corrélér les flux (ou chemins) que l'événement a pris à travers le système.

En cas d'erreurs, les journaux contiennent l'intégralité de la trace de la pile de l'exception, ce qui nous permet de visualiser et de déboguer les problèmes provenant des systèmes en aval.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/android-stack-trace-error-2.png)
_Une entrée de journal montrant la trace de la pile d'une erreur_

En bref, les journaux peuvent vous dire _ce qui s'est passé_ dans le système à un certain moment.

Les métriques contiennent des données à basse résolution. Cela peut inclure un compte de paramètres (tels que les requêtes, les erreurs, etc.) et des mesures de ressources (telles que l'utilisation du CPU et de la mémoire).

![Image](https://www.freecodecamp.org/news/content/images/2020/12/tracing_aggregated_red_metrics.png)
_Une métrique montrant le nombre de hits vers un service_

En bref, les métriques peuvent vous donner _un compte de quelque chose qui s'est passé_ dans le système à un certain moment.

## Le coût des journaux et des métriques

Les journaux sont coûteux à stocker. Le surcoût de stockage des journaux augmente également avec le temps et est directement proportionnel à l'augmentation du trafic.

Les métriques ont un surcoût de stockage constant. Le coût de stockage et de récupération des métriques n'augmente pas trop avec l'augmentation du trafic. Il dépend cependant du nombre de variables que nous émettons avec chaque métrique.

# Cardinalité des métriques

Les métriques sont identifiées par deux éléments clés d'information :

* Un nom de métrique
* Un ensemble de paires clé-valeur appelées tags ou labels

Une permutation de ces valeurs fournit à la métrique sa cardinalité. Par exemple, si nous mesurons l'utilisation du CPU d'un système avec trois hôtes, la métrique a une valeur de cardinalité de 3 et peut avoir les trois valeurs suivantes :

```
(name=pod.cpu.utilization, host=A)
(name=pod.cpu.utilization, host=B)
(name=pod.cpu.utilization, host=C)
```

De même, si nous introduisions un autre tag dans la métrique qui détermine la région AWS des hôtes (par exemple, `us-west-1` et `us-west-2`), nous aurions maintenant une métrique avec une valeur de cardinalité de 6.

# Types de métriques

## Signaux dorés

Les signaux dorés sont un moyen efficace de surveiller l'état général du système et d'identifier les problèmes.

* **Disponibilité** : État de votre système mesuré du point de vue des clients (par exemple, le pourcentage d'erreurs sur le nombre total de requêtes).
* **Santé** : État de votre système mesuré à l'aide de pings périodiques.
* **Taux de requêtes** : Taux de requêtes entrantes dans le système.
* **Saturation** : Degré de liberté ou de charge du système (par exemple, la profondeur de la file d'attente ou la mémoire disponible).
* **Utilisation** : Degré d'occupation du système (par exemple, la charge du CPU ou l'utilisation de la mémoire). Cela est représenté sous forme de pourcentage.
* **Taux d'erreurs** : Taux d'erreurs produites dans le système.
* **Latence** : Temps de réponse du système, généralement mesuré dans le 95e ou 99e percentile.

## Métriques de ressources

Les métriques de ressources sont presque toujours disponibles par défaut depuis le fournisseur d'infrastructure (AWS CloudWatch ou Kubernetes metrics) et sont utilisées pour surveiller la santé de l'infrastructure.

* **Utilisation du CPU/Mémoire** : Utilisation des ressources principales du système.
* **Nombre d'hôtes** : Nombre d'hôtes/pods qui exécutent votre système (utilisé pour détecter les problèmes de disponibilité dus aux plantages de pods).
* **Threads actifs** : Threads générés dans votre service (utilisé pour détecter les problèmes de multithreading).
* **Utilisation du tas** : Statistiques d'utilisation de la mémoire heap (peut aider à déboguer les fuites de mémoire).

## Métriques commerciales

Les métriques commerciales peuvent être utilisées pour surveiller les interactions granulaires avec les API principales ou les fonctionnalités de vos services.

* **Taux de requêtes** : Taux de requêtes vers les API.
* **Taux d'erreurs** : Taux d'erreurs générées par les API.
* **Latence** : Temps pris pour traiter les requêtes par les API.

# Tableaux de bord et alertes pour les métriques

Puisque les métriques sont stockées dans une base de données de séries temporelles, il est plus efficace et fiable d'exécuter des requêtes contre elles pour mesurer l'état du système.

Vous pouvez utiliser ces requêtes pour construire des tableaux de bord représentant l'état historique du système.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/Screenshot-2020-10-03-at-3.20.16-PM.png)
_Un tableau de bord Wavefront avec quelques métriques importantes_

Elles peuvent également être utilisées pour déclencher des alertes lorsqu'il y a un problème avec le système (comme une augmentation du nombre d'erreurs observées ou une augmentation soudaine de l'utilisation du CPU).

En raison de leur nature numérique, nous pouvons également créer des requêtes mathématiques complexes (comme X% d'erreurs dans les dernières Y minutes) pour surveiller la santé du système.

Le plus grand défi, cependant, dans la gestion des métriques est de décider la bonne quantité de cardinalité qui rend la métrique utile tout en gardant ses coûts sous contrôle.

Émettre trop de métriques, ou des métriques avec trop de dimensions, peut entraîner une augmentation des coûts de stockage et de traitement. Vous devez choisir la cardinalité minimale qui est juste suffisante pour donner une vue d'ensemble du système.

# Comment utiliser les journaux et les métriques

Les journaux et les métriques ont chacun leurs propres avantages et inconvénients. Cependant, dans tout système de production, nous devons utiliser à la fois les journaux et les métriques ensemble pour surveiller efficacement le système et déboguer les problèmes.

Les métriques sont souvent la première ligne de vue sur la santé d'un système. Prenons l'exemple d'une application de commerce électronique comme Amazon. La métrique la plus importante pour un tel cas d'utilisation est le nombre total de commandes réussies et échouées.

Un jour normal, la métrique du nombre de commandes échouées resterait à zéro ou à un nombre très faible. Si un problème dans le système provoque une augmentation soudaine des échecs de commandes, cette métrique montrera une augmentation du compte.

Vous pouvez créer une _alerte_ sur une combinaison de deux métriques - commandes totales et commandes échouées. Cela vous permettra d'envoyer une notification lorsque le pourcentage de commandes échouées dépasse un certain seuil (par exemple 5%).

Une fois que vous êtes informé des commandes échouées, vous pouvez ensuite vous référer aux journaux pour trouver la cause des échecs. Les journaux contiendraient les messages d'erreur menant à l'échec, ainsi que la trace de la pile détaillée qui peut identifier la cause racine de l'échec.

# Conclusion

Dans cet article, nous avons vu les différences entre les métriques et les journaux, et comment les métriques peuvent nous aider à surveiller la santé de notre système plus efficacement. Les métriques peuvent également être utilisées pour créer des tableaux de bord et des alertes à l'aide de logiciels de surveillance comme Wavefront et Grafana.

Il est également nécessaire d'utiliser à la fois les métriques et les journaux en coordination pour détecter et déboguer précisément les problèmes.

Merci de m'avoir suivi jusqu'ici. J'espère que vous avez aimé l'article. Vous pouvez me contacter sur [LinkedIn](https://www.linkedin.com/in/theawesomenayak/) où je discute régulièrement de la technologie et de la vie. Jetez également un coup d'œil à certains de mes autres articles sur [Medium](https://medium.com/@theawesomenayak). Bonne lecture 📊