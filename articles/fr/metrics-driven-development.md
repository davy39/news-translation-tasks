---
title: 'Introduction au développement piloté par les métriques : que sont les métriques
  et pourquoi les utiliser ?'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-12T16:47:37.000Z'
originalURL: https://freecodecamp.org/news/metrics-driven-development
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c2b740569d1a4ca3062.jpg
tags:
- name: Metrics driven development
  slug: metrics-driven-development
- name: agile development
  slug: agile-development
- name: Grafana
  slug: grafana
- name: MDD
  slug: mdd
- name: metrics
  slug: metrics
- name: '#prometheus'
  slug: prometheus
- name: TypeScript
  slug: typescript
seo_title: 'Introduction au développement piloté par les métriques : que sont les
  métriques et pourquoi les utiliser ?'
seo_desc: 'By dor sever

  One of the coolest things I have learned in the last year is how to constantly deliver
  value into production without causing too much chaos.

  In this post, I’ll explain the metrics-driven development approach and how it helped
  me to achie...'
---

Par dor sever

L'une des choses les plus cool que j'ai apprises l'année dernière est comment livrer constamment de la valeur en production sans causer **trop** de chaos.

Dans cet article, je vais expliquer l'approche de développement piloté par les métriques et comment elle m'a aidé à atteindre cet objectif. À la fin de cet article, vous serez en mesure de répondre aux questions suivantes :

* Qu'est-ce que les métriques et pourquoi devrais-je les utiliser
* Quels sont les différents types de métriques
* Quels outils pourrais-je utiliser pour stocker et afficher les métriques
* Quel est un exemple concret de développement piloté par les métriques

## Qu'est-ce que les métriques et pourquoi devrais-je les utiliser ?

Les métriques vous donnent la capacité de collecter des informations sur un système en cours d'exécution sans changer son code.

Cela vous permet d'obtenir des données précieuses sur le comportement de votre application pendant son exécution, afin que vous puissiez prendre des **[décisions basées sur les données](https://www.techopedia.com/definition/32877/data-driven-decision-making-dddm)** basées sur les retours réels des clients et l'utilisation en production.

## Quels sont les types de métriques disponibles ?

Voici les métriques les plus couramment utilisées aujourd'hui :

* Compteur

Représente une valeur qui augmente de manière monotone.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-5780-06-10-at-12.37.42-PM.png)
_Les compteurs sont vraiment utiles pour mesurer les taux !_

Dans cet exemple, une métrique de compteur est utilisée pour calculer le taux d'événements au fil du temps, en comptant les événements par seconde.

* Jauge

Représente une seule valeur qui peut monter ou descendre.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-5780-06-10-at-12.42.06-PM.png)
_Les jauges sont vraiment utiles pour mesurer l'utilisation du CPU !_

Dans cet exemple, une métrique de jauge est utilisée pour surveiller le [CPU utilisateur](https://blog.appsignal.com/2018/03/06/understanding-cpu-statistics.html) en pourcentages.

* Histogramme

Un comptage des observations (comme les durées ou les tailles des requêtes) dans des compartiments configurables.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-5780-06-10-at-12.44.12-PM.png)
_Les histogrammes sont vraiment utiles pour mesurer la durée des requêtes !_

Dans cet exemple, une métrique d'histogramme est utilisée pour calculer les 75e et 90e percentiles de la durée d'une requête HTTP.

Les détails des types : compteur, histogramme et jauge peuvent être assez confus. Essayez de lire davantage à ce sujet [ici](https://prometheus.io/docs/concepts/metric_types/).

## Quels outils puis-je utiliser pour stocker et afficher les métriques ?

La plupart des systèmes de surveillance se composent de quelques parties :

1. Base de données de séries temporelles

Un logiciel de base de données qui optimise le stockage et la fourniture de données de [séries temporelles](https://en.wikipedia.org/wiki/Time_series). Deux exemples de ce type de base de données sont [Whisper](https://graphite.readthedocs.io/en/latest/whisper.html) et [Prometheus](https://prometheus.io/).
2. Moteur de requête (avec un langage de requête)

Deux exemples de moteurs de requête courants sont : [Graphite](https://graphiteapp.org/) et [PromQL](https://prometheus.io/docs/prometheus/latest/querying/basics/)
3. Système d'alerte

Le mécanisme qui vous permet de configurer des alertes basées sur des graphiques créés par le langage de requête. Le système peut envoyer ces alertes par Mail, Slack, PagerDuty. Deux exemples de systèmes d'alerte courants sont : [Grafana](https://grafana.com/) et [Prometheus](https://prometheus.io/).
4. UI

Permet de visualiser les graphiques générés par les données entrantes et de configurer des requêtes et des alertes. Deux exemples de systèmes d'UI courants sont : [Graphite](https://graphiteapp.org/) et [Grafana](https://grafana.com/)

La configuration que nous utilisons aujourd'hui chez [BigPanda Engineering](https://medium.com/@bigpanda_engineering) est :

* [Telegraf](https://www.influxdata.com/time-series-platform/telegraf/)

Utilisé comme serveur StatsD.
* [Prometheus](https://prometheus.io/)

Utilisé comme notre moteur de scraping, base de données de séries temporelles et moteur de requête.
* [Grafana](https://grafana.com/)

Utilisé pour les alertes et l'UI

Et les contraintes que nous avions à l'esprit lors du choix de cette pile étaient :

* Nous voulons un scraping de métriques scalable et élastique
* Nous voulons un moteur de requête performant
* Nous voulons la capacité de requêter nos métriques en utilisant des tags personnalisés (comme les noms de services, les hôtes, etc.)

## Un exemple concret de développement piloté par les métriques d'un service d'analyse de sentiment

Développons un nouveau service de pipeline qui calcule les sentiments basés sur des entrées textuelles et le faisons de manière pilotée par les métriques !

Disons que je dois développer ce service de pipeline :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/1_bj6DWm4987CuedEclpyvVw.png)
_Architecture du pipeline d'analyse de sentiment_

Et voici mon processus de développement habituel :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-5780-06-16-at-7.31.52-AM.png)
_Processus de développement habituel - Tester, coder et déployer. Oh là là !_

Je vais donc écrire l'implémentation suivante :

```typescript
let senService: SentimentAnalysisService = new SentimentAnalysisService();
while (true) {
    let tweetInformation = kafkaConsumer.consume()
    let deserializedTweet: { msg: string } = deSerialize(tweetInformation)
    let sentimentResult = senService.calculateSentiment(deserializedTweet.msg)
    let serializedSentimentResult = serialize(sentimentResult)
    sentimentStore.store(sentimentResult);
    kafkaProducer.produce(serializedSentimentResult, 'sentiment_topic', 0);
}
```

Le gist complet peut être trouvé [ici](https://gist.github.com/dorsev/387800acee8d1b8e6af29c86101fedb8).

**Et cette méthode fonctionne parfaitement bien.**

**Mais que se passe-t-il quand ça ne fonctionne pas ?**

![Image](https://www.freecodecamp.org/news/content/images/2020/03/but-.gif)

La réalité est que, pendant que nous travaillons (dans un processus de développement agile), nous faisons des erreurs. C'est un fait de la vie.

Je crois que le vrai défi avec les erreurs n'est pas de les éviter, mais plutôt d'optimiser la rapidité avec laquelle nous les détectons et les réparons. Nous devons donc acquérir la capacité de **découvrir rapidement** nos erreurs.

Il est temps pour la méthode MDD.

## La méthode de développement piloté par les métriques (MDD)

![Image](https://www.freecodecamp.org/news/content/images/2020/03/commandments.gif)
_Admirez ! **Les Trois Commandements de la Production !**_

L'approche MDD est fortement inspirée par les **Trois Commandements de la Production** (que j'ai appris à la dure).

**Les Trois Commandements de la Production sont :**

1. Il y a des erreurs et des bugs dans le code que vous écrivez et déployez.
2. Les données circulant en production sont imprévisibles et **uniques !**
3. Perfectionnez votre code à partir des **retours réels des clients et de l'utilisation en production**.

Et puisque nous connaissons maintenant les **Commandements**, il est temps de passer au plan en 4 étapes du processus de développement piloté par les métriques.

## Le plan en 4 étapes pour un MDD réussi

![Image](https://www.freecodecamp.org/news/content/images/2020/03/MDD---oh-wow.png)
_Développement piloté par les métriques ? Oh wow !_

### Développer le code

J'écris le code, et chaque fois que possible, je l'enveloppe avec un feature flag qui me permet de l'ouvrir progressivement aux utilisateurs.

### Métriques

Cela se compose de deux parties :

**Ajouter des métriques sur les parties pertinentes**

Dans cette partie, je me demande quelles sont les métriques de succès ou d'échec que je peux définir pour m'assurer que ma fonctionnalité fonctionne ? Dans ce cas, mon nouvelle application de pipeline effectue-t-elle sa logique correctement ?

**Ajouter des alertes sur le dessus afin que je sois alerté lorsqu'un bug se produit**

Dans cette partie, je me demande quelle métrique pourrait m'alerter si j'ai oublié quelque chose ou ne l'ai pas implémenté correctement ?

### Déploiement

Je déploie le code et le surveille immédiatement pour vérifier qu'il se comporte comme je l'ai anticipé.

### Itérer ce processus jusqu'à la perfection

Et c'est tout ! Maintenant que nous avons appris le processus, abordons une tâche importante à l'intérieur.

## Métriques à rapporter

Que devons-nous surveiller ?

L'une des questions les plus difficiles pour moi, lorsque je fais du MDD, est : "que devrais-je surveiller ?"

![Image](https://www.freecodecamp.org/news/content/images/2020/03/MALLTHINGZ.jpeg)
_C'est un joli gif. mais irréaliste dans la plupart des cas._

Pour répondre à la question, essayons de zoomer et de regarder le tableau d'ensemble.

Toutes les informations possibles disponibles pour la surveillance peuvent être divisées en deux parties :

1. **Informations applicatives**

Informations qui ont un contexte et une signification applicatifs. Un exemple de cela serait

"Combien de tweets avons-nous classés comme positifs dans la dernière heure ?"
2. **Informations opérationnelles**

Informations liées à l'infrastructure qui entoure notre application

Données cloud, utilisation du CPU et du disque, utilisation du réseau, etc.

Maintenant, puisque nous ne pouvons pas tout surveiller, nous devons choisir quelles informations applicatives et opérationnelles nous voulons surveiller.

* La partie opérationnelle dépend vraiment de votre pile ops et dispose de solutions intégrées pour (presque) tous vos besoins de surveillance.
* La partie applicative est plus unique à vos besoins, et j'essaierai d'expliquer comment j'y pense plus tard dans cet article.

Après cela, nous pouvons nous poser la question : quelles alertes voulons-nous configurer sur les métriques que nous venons de définir ?

Le diagramme (d'informations, de métriques, d'alertes) peut être dessiné comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/world-of.png)
_Le monde de l'information, des métriques et des alertes._

### Métriques applicatives

J'ajoute généralement des métriques applicatives pour deux besoins :

#### Pour répondre aux questions

Une question est quelque chose comme, "Lorsque mon service se comporte mal, quelles informations seraient utiles à connaître ?"

Certaines réponses à cette question peuvent être

les latences de tous les appels IO, le taux de traitement, le débit, etc...

La plupart de ces questions seront utiles pendant que vous cherchez la réponse. Mais une fois que vous l'avez trouvée, il est probable que vous ne la regarderez plus (puisque vous connaissez déjà la réponse).

Ces questions sont généralement motivées par la R&D et sont (généralement) utilisées pour recueillir des informations en interne.

#### Pour ajouter des alertes

Cela peut sembler rétrograde, mais j'ajoute généralement des métriques applicatives afin de définir des alertes sur le dessus. Cela signifie que nous définissons la liste des alertes et en déduisons ensuite les métriques applicatives à rapporter.

Ces alertes sont dérivées du SLA du produit et sont généralement traitées avec une importance critique pour la mission.

## Types courants d'alertes

Les alertes peuvent être divisées en trois parties :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/alert-types.png)
_Types d'alertes vers la liste des métriques_

### Alertes SLA

![Image](https://www.freecodecamp.org/news/content/images/2020/03/sla-breach.jpeg)
_Alertes SLA en réalité_

Les alertes [SLA](https://en.wikipedia.org/wiki/Service-level_agreement) entourent les endroits de notre système où un SLA est spécifié pour répondre à des exigences explicites des clients ou internes (c'est-à-dire disponibilité, débit, latence, etc.). Les violations de SLA impliquent de paginer la R&D et de réveiller les gens, alors essayez de garder les alertes de cette liste au minimum.

De plus, nous pouvons définir des alertes de **Dégradation** en plus des alertes SLA.
Les alertes de dégradation sont définies avec des seuils inférieurs à ceux des alertes SLA, et sont donc utiles pour réduire le nombre de violations de SLA

en vous donnant un avertissement approprié avant qu'elles ne se produisent.

Un exemple d'alerte SLA serait : "Toutes les requêtes de sentiment doivent se terminer en moins de 500 ms."

Un exemple d'alerte de dégradation serait : "Toutes les requêtes de sentiment doivent se terminer en moins de 400 ms."

Voici les alertes que j'ai définies :

1. Latence

Je m'attends à ce que le 90e percentile de la durée d'une seule requête ne dépasse pas 300 ms.
2. Ratio succès/échec des requêtes

Je m'attends à ce que le nombre d'échecs par seconde, de succès par seconde, reste inférieur à 0,01.
3. Débit

Je m'attends à ce que le nombre d'opérations par seconde (ops) que l'application gère soit > 200
4. Taille des données

Je m'attends à ce que la quantité de données que nous stockons en une seule journée ne dépasse pas 2 Go.

> _200 ops * 60 octets (Taille du Résultat de Sentiment) * 86400 sec dans une journée = 1 Go < 2 Go_

### Alertes de violation de référence

Ces alertes impliquent généralement la mesure et la définition d'une référence et s'assurent qu'elle ne change pas (de manière dramatique) au fil du temps avec des alertes.

Par exemple, la latence de traitement du 99e percentile pour un événement doit rester relativement la même au fil du temps, sauf si nous avons apporté des changements dramatiques à la logique.

Voici les alertes que j'ai définies :

1. Quantité de tweets de sentiment positif, neutre ou négatif

Si, pour une raison quelconque, la somme des tweets positifs a augmenté ou diminué de manière dramatique, il se peut que j'ai un bug quelque part dans mon application.
2. Toutes les latences \ Ratio de succès des requêtes \ Débit \ La taille des données ne doit pas augmenter\diminuer de manière dramatique au fil du temps.

### Alertes de propriétés d'exécution

J'ai donné une conférence sur les [tests basés sur les propriétés](https://www.youtube.com/watch?v=Xtuv_aduYjM) et leur force incroyable. Il s'avère que la collecte de métriques nous permet d'exécuter des tests basés sur les propriétés sur notre système **en production** !

Certaines propriétés de notre système :

1. Puisque nous consommons des messages d'un sujet Kafka, le décalage traité doit augmenter de manière monotone au fil du temps.
2. 1 

1 

 score de sentiment 

 0
3. Un tweet doit être classé comme soit Négatif \ Positif \ Neutre.
4. Une classification de tweet doit être unique.

Ces alertes m'ont aidé à valider que :

1. Nous lisons avec le même group-id. Changer les identifiants de groupe de consommateurs par erreur lors du déploiement est une erreur courante lors de l'utilisation de Kafka. Cela cause beaucoup de chaos en production.
2. Le score de sentiment est constamment entre 0 et 1.
3. La longueur de la catégorie de tweet doit toujours être 1.

Pour définir ces alertes, vous devez soumettre des métriques depuis votre application. Allez [ici](https://gist.github.com/dorsev/181e84e091ae545cb7825b782faf9d20) pour la liste complète des métriques.

En utilisant ces métriques, je peux créer des **alertes** qui m'enverront une notification chaque fois que l'une de ces propriétés ne sera plus respectée en production.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/processing-latency-alert.png)
_La latence de traitement a violé le SLA configuré ! Oh là là ! ?_

Regardons une implémentation possible de toutes ces métriques

```typescript
import SDC = require("statsd-client");
let sdc = new SDC({ host: 'localhost' });
let senService: SentimentAnalysisService; //...
while (true) {
    let tweetInformation = kafkaConsumer.consume()
    sdc.increment('incoming_requests_count')
    let deserializedTweet: { msg: string } = deSerialize(tweetInformation)
    sdc.histogram('request_size_chars', deserializedTweet.msg.length);
    let sentimentResult = senService.calculateSentiment(deserializedTweet.msg)
    if (sentimentResult !== undefined) {
        let serializedSentimentResult = serialize(sentimentResult)
        sdc.histogram('outgoing_event_size_chars', serializedSentimentResult.length);
        sentimentStore.store(sentimentResult)
        kafkaProducer.produce(serializedSentimentResult, 'sentiment_topic', 0);
    }

}

```

Le code complet peut être trouvé [ici](https://gist.github.com/dorsev/d7737ed6a866cf98b026d47f4f7faae8)

**Quelques réflexions sur l'exemple de code ci-dessus :**

1. Il y a eu une quantité impressionnante de métriques ajoutées à cette base de code.
2. Les métriques ajoutent de la complexité à la base de code, donc, comme toutes les bonnes choses, ajoutez-les de manière responsable et avec modération.
3. Choisir des noms de métriques corrects est difficile. Prenez votre temps pour sélectionner des noms appropriés. [Voici](https://prometheus.io/docs/practices/naming/) un excellent article à ce sujet.
4. Vous devez toujours collecter ces métriques et les afficher dans un système de surveillance (comme Grafana), plus ajouter des alertes sur le dessus, mais c'est un sujet pour un autre article.

## Avons-nous atteint l'objectif initial d'identifier les problèmes et de les résoudre plus rapidement ?

![Image](https://www.freecodecamp.org/news/content/images/2020/03/yes-it-was-.gif)
_OUI, c'était le cas !_

Nous pouvons maintenant nous assurer que la latence et le débit de l'application ne se dégradent pas au fil du temps. De plus, l'ajout d'alertes sur ces métriques permet une découverte et une résolution des problèmes beaucoup plus rapides.

## Conclusion

Le développement piloté par les métriques va de pair avec l'intégration continue/déploiement continu (CI/CD), le DevOps et le processus de développement agile. Si vous utilisez l'un des mots-clés ci-dessus, alors vous êtes au bon endroit.

Lorsque cela est fait correctement, les métriques vous donnent plus de confiance dans votre déploiement, de la même manière que voir des tests unitaires réussis dans votre build vous donne confiance dans le code que vous écrivez.

L'ajout de métriques vous permet de déployer du code et de vous sentir confiant que votre environnement de production est stable et que votre application se comporte comme prévu au fil du temps. Je vous encourage donc à essayer !

#### Quelques références

1. Voici un [lien](https://github.com/dorsev/MetricsSentimentAnalysis) vers le code montré dans cet article, et [ici](https://gist.github.com/dorsev/181e84e091ae545cb7825b782faf9d20) se trouve la liste complète des métriques décrites.
2. Si vous êtes impatient d'essayer d'écrire quelques métriques et de les connecter à un système de surveillance, consultez [Prometheus](https://prometheus.io/docs/introduction/first_steps/), [Grafana](https://grafana.com/docs/grafana/latest/guides/getting_started/) et éventuellement cet [article](https://dev.to/kirklewis/metrics-with-prometheus-statsd-exporter-and-grafana-5145)
3. Ce gars a écrit un article [délicieux](https://sookocheff.com/post/mdd/mdd/) sur le développement piloté par les métriques. Allez le lire.