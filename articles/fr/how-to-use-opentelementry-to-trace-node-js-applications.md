---
title: Comment utiliser OpenTelemetry pour tracer les applications Node.js
subtitle: ''
author: Abraham Dahunsi
co_authors: []
series: null
date: '2024-02-03T00:21:14.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-opentelementry-to-trace-node-js-applications
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/feature-image-1.png
tags:
- name: data
  slug: data
- name: node js
  slug: node-js
- name: performance
  slug: performance
seo_title: Comment utiliser OpenTelemetry pour tracer les applications Node.js
seo_desc: 'Observability refers to our ability to "see" and understand what''s happening
  inside a system by looking at its external signals (like logs, metrics, and traces).

  Observability involves collecting and analyzing data from sources within a system
  to mon...'
---

L'observabilité fait référence à notre capacité à "voir" et comprendre ce qui se passe à l'intérieur d'un système en examinant ses signaux externes (comme les logs, les métriques et les traces).

L'observabilité implique la collecte et l'analyse de données provenant de sources au sein d'un système pour surveiller ses performances et résoudre les problèmes efficacement.

## Pourquoi l'observabilité est-elle utile ?

1. **Détection et résolution des problèmes** : L'observabilité joue un rôle dans l'identification et le diagnostic des problèmes au sein d'un système. Lorsque quelque chose ne va pas, avoir accès aux données aide à identifier la cause et à résoudre les problèmes plus rapidement.

2. **Optimisation des performances** : Grâce à la surveillance des métriques et des indicateurs de performance, l'observabilité aide à optimiser les performances de votre système. Cela inclut l'identification des goulots d'étranglement, l'amélioration de l'utilisation des ressources et la garantie de l'opération.

3. **Planification de la capacité future** : Comprendre comment votre système se comporte au fil du temps est vital pour planifier les besoins en capacité. Les données d'observabilité peuvent révéler des tendances, des périodes de pointe d'utilisation et des besoins en ressources, aidant vos décisions concernant la mise à l'échelle.

4. **Amélioration de l'expérience utilisateur** : En observant les interactions des utilisateurs avec votre système à travers les logs et les métriques, vous pouvez améliorer l'expérience utilisateur. Cela aide à reconnaître les modèles, les préférences et les domaines potentiels qui peuvent être améliorés pour la satisfaction des utilisateurs.

## Pourquoi devrais-je utiliser OpenTelemetry ?

L'observabilité est essentielle pour garantir la fiabilité et la disponibilité de vos applications Node.js. Mais l'instrumentation manuelle de votre code pour collecter et exporter des données de télémétrie, telles que les traces, les métriques et les logs, peut devenir très stressante.

L'instrumentation manuelle est très fastidieuse, sujette aux erreurs et inconsistante. Elle peut également introduire une surcharge supplémentaire et une complexité à votre logique d'application.

Dans ce guide, vous apprendrez à utiliser l'auto-instrumentation d'OpenTelemetry pour vous aider à atteindre une surveillance sans effort de Node.js.

## Prérequis

Avant de suivre ce guide, assurez-vous d'avoir les éléments suivants :

* Une application Node.js

* Un compte Datadog et une clé API. Si vous n'en avez pas, vous pouvez [vous inscrire ici pour en obtenir une](https://us5.datadoghq.com/signup).

* Un service backend. Vous pouvez utiliser un service backend comme Zepkin ou Jaeger pour stocker et analyser les données de trace. Pour ce guide, nous utiliserons Jaeger.

* Certaines connaissances de base des [commandes Linux](https://www.freecodecamp.org/news/helpful-linux-commands-you-should-know/). Vous devriez être familier avec l'utilisation de la ligne de commande et l'édition de fichiers de configuration.

## Préparer votre application

Dans ce guide, vous utiliserez une application Node.js qui possède deux services qui transfèrent des données entre eux. Vous utiliserez la bibliothèque cliente Node.js d'OpenTelemetry pour envoyer des données de trace à un collecteur OpenTelemetry.

Tout d'abord, clonez le dépôt localement :

```bash
$ git clone https://github.com/<github-account>/nodejs-example.git
```

Ensuite, exécutez l'application :

```bash
npm install
```

Allez dans le répertoire du premier service en utilisant cette commande :

```bash
$ cd <ServiceA>
```

Et démarrez le premier service.

```bash
$ node index.js
```

Ensuite, allez dans le répertoire du second service

```bash
$ cd <ServiceB>
```

Et démarrez le second service.

```bash
$ node index.js
```

Ouvrez le Service A, dans ce cas le port `5555`, et entrez quelques informations. Ensuite, répétez la même opération pour le Service B.

![ServiceASshot](https://www.freecodecamp.org/news/content/images/2024/01/ServiceASshot.png align="left")

## Comment configurer OpenTelemetry

Après avoir démarré les services, il est temps d'installer les modules OpenTelemetry dont vous aurez besoin pour l'auto-instrumentation.

Voici ce que nous devons installer :

```bash
$ npm install --save @opentelemetry/api

$ npm install --save @opentelemetry/instrumentation

$ npm install --save @opentelemetry/tracing

$ npm install --save @opentelemetry/exporter-trace-otlp-http

$ npm install --save @opentelemetry/resources

$ npm install --save @opentelemetry/semantic-conventions

$ npm install --save @opentelemetry/auto-instrumentations-node

$ npm install --save @opentelemetry/sdk-node

$ npm install --save @opentelemetry/exporter-jaeger
```

Voici une explication de ce que fait chaque module :

* `@opentelemetry/api` : Ce module fournit l'API OpenTelemetry pour Node.js.

* `@opentelemetry/instrumentation` : Les bibliothèques d'instrumentation fournissent une instrumentation automatique pour votre application Node.js. Elles capturent automatiquement les données de télémétrie sans nécessiter de modifications manuelles du code.

* `@opentelemetry/tracing` : Ce module contient la fonctionnalité de base de traçage pour OpenTelemetry dans votre application Node.js. Il inclut les interfaces Tracer et Span, qui sont importantes pour capturer et représenter les traces distribuées au sein de vos applications.

* `@opentelemetry/exporter-trace-otlp-http` : Ce module exporteur permet d'envoyer des données de trace à un backend compatible avec le protocole OpenTelemetry (OTLP) via HTTP.

* `@opentelemetry/resources` : Ce module fournit un moyen de définir et de gérer les ressources associées aux traces.

* `@opentelemetry/semantic-conventions` : Ce module définit un ensemble de conventions sémantiques pour le traçage. Il établit un ensemble commun de clés d'attributs et de formats de valeurs pour garantir la cohérence dans la représentation et l'interprétation des données de télémétrie.

* `@opentelemetry/auto-instrumentations-node` : Ce module simplifie le processus d'instrumentation de votre application en appliquant automatiquement l'instrumentation aux bibliothèques supportées.

* `@opentelemetry/sdk-node` : Le Kit de Développement Logiciel (SDK) pour Node.js fournit l'implémentation de l'API OpenTelemetry.

* `@opentelemetry/exporter-jaeger` : Ce module exporteur permet d'exporter les données de trace vers Jaeger. Jaeger fournit une interface conviviale pour surveiller et analyser les données de trace.

## Configurer l'application Node.js

Ensuite, ajoutez un traceur SDK Node.js pour gérer l'instanciation et l'arrêt du traçage.

Pour ajouter le traceur, créez un fichier `tracer.js` :

```bash
$ nano tracer.js
```

Ensuite, ajoutez le code suivant au fichier :

```javascript

"use strict";

const {
    BasicTracerProvider,
    SimpleSpanProcessor,
} = require("@opentelemetry/tracing");
// Importer JaegerExporter
const { JaegerExporter } = require("@opentelemetry/exporter-jaeger");
const { Resource } = require("@opentelemetry/resources");
const {
    SemanticResourceAttributes,
} = require("@opentelemetry/semantic-conventions");

const opentelemetry = require("@opentelemetry/sdk-node");
const {
    getNodeAutoInstrumentations,
} = require("@opentelemetry/auto-instrumentations-node");

// Créer une nouvelle instance de JaegerExporter avec les options
const exporter = new JaegerExporter({
    serviceName: "YOUR-SERVICE-NAME",
    host: "localhost", // optionnel, peut être défini par OTEL_EXPORTER_JAEGER_AGENT_HOST
    port: 16686 // optionnel
});

const provider = new BasicTracerProvider({
    resource: new Resource({
        [SemanticResourceAttributes.SERVICE_NAME]:
            "YOUR-SERVICE-NAME",
    }),
});
// Ajouter JaegerExporter au processeur de spans
provider.addSpanProcessor(new SimpleSpanProcessor(exporter));

provider.register();
const sdk = new opentelemetry.NodeSDK({
    traceExporter: exporter,
    instrumentations: [getNodeAutoInstrumentations()],
});

sdk
    .start()
    .then(() => {
        console.log("Tracing initialisé");
    })
    .catch((error) => console.log("Erreur lors de l'initialisation du tracing", error));

process.on("SIGTERM", () => {
    sdk
        .shutdown()
        .then(() => console.log("Tracing terminé"))
        .catch((error) => console.log("Erreur lors de la terminaison du tracing", error))
        .finally(() => process.exit(0));
```

Voici une explication simple du code :

* Le code commence par importer les modules `BasicTracerProvider` et `SimpleSpanProcessor` pour configurer le traçage à partir de la bibliothèque OpenTelemetry.

* Il importe ensuite le module JaegerExporter pour exporter les données de trace vers Jaeger.

* Le code crée une nouvelle instance de JaegerExporter, en spécifiant le nom du service, l'hôte et le port.

* Il crée ensuite un `BasicTracerProvider` et ajoute le JaegerExporter au processeur de spans en utilisant `SimpleSpanProcessor`.

* Le fournisseur est enregistré, le définissant comme le fournisseur par défaut pour l'application.

* Une instance du SDK OpenTelemetry est créée, configurée avec le JaegerExporter et activant les auto-instrumentations pour Node.js.

* Le SDK OpenTelemetry est démarré, initialisant le traçage.

* Un gestionnaire pour le signal SIGTERM est configuré pour arrêter le traçage lorsque l'application est terminée.

* Le code configure ensuite le fournisseur de traces avec un exporteur de traces. Pour vérifier l'instrumentation, `ConsoleSpanExporter` est utilisé pour imprimer une partie de la sortie du traceur dans la console.

## Comment configurer OpenTelemetry pour exporter les traces

Ensuite, vous devrez écrire les configurations pour collecter et exporter les données dans le collecteur OpenTelemetry.

Créez un fichier `config.yaml` :

```yaml

receivers:
  otlp:
    protocols:
      grpc:
      http:

exporters:
  datadog:
    api: # Remplacez par votre clé API Datadog
      key: "<YOUR_DATADOG_API_KEY>"
    # Optionnel:
    #   - endpoint: https://app.datadoghq.eu  # Pour la région UE

processors:
  batch:

extensions:
  pprof:
    endpoint: :1777
  zpages:
    endpoint: :55679
  health_check:

service:
  extensions: [health_check, pprof, zpages]
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch]
      exporters: [datadog]
```

La configuration configure OpenTelemetry avec le récepteur OTLP (OpenTelemetry Protocol) et l'exporteur Datadog. Voici une explication du code :

* `receivers` : Spécifie les composants qui reçoivent les données de télémétrie. Dans ce cas, il inclut le récepteur OTLP, qui prend en charge les protocoles gRPC et HTTP.

* `exporters` : Définit les composants responsables de l'exportation des données de télémétrie. Ici, il configure l'exporteur Datadog, fournissant la clé API Datadog. De plus, un `endpoint` optionnel est fourni pour utiliser la région UE de Datadog.

* `processors` : Spécifie les composants de traitement des données. Dans ce cas, le processeur `batch` est utilisé pour regrouper et envoyer les données en plus grands morceaux pour plus d'efficacité.

* `extensions` : Définit des composants supplémentaires qui étendent la fonctionnalité. Ici, il inclut des extensions pour pprof (données de profilage), zpages (pages de débogage) et une extension de vérification de santé.

* `service` : Configure le comportement global du service, y compris les extensions et les pipelines. La section `extensions` liste les extensions à utiliser, et la section `pipelines` configure le pipeline de données de télémétrie. Ici, le pipeline de traces inclut le récepteur OTLP, le processeur batch et l'exporteur Datadog.

Ce code est configuré par le collecteur avec l'exporteur Datadog pour envoyer les traces aux services de traçage distribué de Datadog. Cependant, il existe d'autres services de traçage distribué que vous pouvez utiliser comme New Relic, Logzio et Zipkin.

## Comment démarrer l'application

Après avoir correctement configuré l'auto-instrumentation, démarrez à nouveau l'application pour tester et vérifier la configuration de traçage.

Commencez par démarrer le collecteur OpenTelemetry :

```bash
./otelcontribcol_darwin_amd64 --config ./config.yaml
```

Le collecteur démarrera sur le port 4317.

Ensuite, allez dans le répertoire du premier service :

```bash
$ cd <ServiceA>
```

Puis démarrez le premier service avec le paramètre "--require './tracer.js'" pour activer l'instrumentation de l'application.

```bash
$ node --require './tracer.js' index.js
```

Répétez cela pour démarrer le second service.

En utilisant un navigateur comme Chrome, allez aux endpoints des services de vos deux applications, ajoutez quelques données et envoyez quelques requêtes pour tester la configuration de traçage.

Une fois les requêtes effectuées, ces traces sont captées par le collecteur, qui les envoie ensuite au backend de traçage distribué spécifié par la configuration de l'exporteur dans le fichier de configuration du collecteur.

Il est intéressant de noter que notre traceur facilite non seulement la transmission des traces au backend désigné, mais les exporte également vers la console en même temps.

Cette double fonctionnalité permet une visibilité en temps réel des traces générées et envoyées, nous aidant dans les processus de surveillance et de débogage.

Maintenant, utilisons l'interface utilisateur de Jaeger pour surveiller les traces :

Démarrez Jaeger avec la commande suivante :

```bash
docker run -d --name jaeger \
  -e COLLECTOR_ZIPKIN_HOST_PORT=:9411 \
  -p 5775:5775/udp \
  -p 6831:6831/udp \
  -p 6832:6832/udp \
  -p 5778:5778 \
  -p 16686:16686 \
  -p 14250:14250 \
  -p 14268:14268 \
  -p 14269:14269 \
  -p 9411:9411 \
  jaegertracing/all-in-one:1.32
```

En utilisant un navigateur, démarrez l'interface utilisateur de Jaeger à l'endpoint http://localhost:16686/.

![image4-1024x508](https://www.freecodecamp.org/news/content/images/2024/01/image4-1024x508.png align="left")

Voilà ! L'initiation de la trace commençant à partir du point de départ d'un service, naviguant à travers une séquence d'opérations.

Ce chemin est créé lorsque le service commence ses opérations, entraînant la configuration de l'autre service pour répondre à la demande initiale que vous avez initiée précédemment.

La trace fournit un récit visuel de ce qui se passe entre ces services, offrant des informations sur chaque étape du processus.

## Comment pouvez-vous utiliser les données d'observabilité ?

1. **Surveillance des métriques** : Surveillez les métriques clés telles que les temps de réponse, les taux d'erreur et l'utilisation des ressources. Les pics soudains ou les anomalies peuvent indiquer des problèmes nécessitant une attention.

2. **Journalisation** : Les données de journalisation fournissent des informations détaillées sur les événements et les actions au sein d'un système. L'analyse des logs aide à comprendre la séquence des activités et à retracer les étapes menant à un problème.

3. **Traçage** : Le traçage implique le suivi du flux des requêtes ou des transactions à travers différents composants d'un système. Cela aide à comprendre le parcours d'une requête et à identifier les goulots d'étranglement ou les retards.

4. **Alerte** : Configurez des alertes basées sur des conditions ou des seuils spécifiques. Lorsque certaines métriques dépassent les limites prédéfinies, les alertes peuvent vous notifier en temps réel, permettant une action immédiate.

5. **Visualisation** : Utilisez des représentations graphiques et des tableaux de bord pour visualiser des données complexes. Cela facilite l'identification des modèles, des tendances et des corrélations dans les données d'observabilité.

L'observabilité, lorsqu'elle est mise en œuvre efficacement, permet aux équipes de gérer et d'améliorer de manière proactive les performances, la fiabilité et l'expérience utilisateur de leurs systèmes. C'est un aspect crucial du développement logiciel moderne et des opérations.

## Conclusion

Dans ce guide, vous avez appris à auto-instrumenter des applications Node.js avec peu de code en :

* Installant et configurant le SDK OpenTelemetry Node.js et le package d'auto-instrumentation

* Activant le traçage automatique et la collecte de métriques pour vos applications Node.js et leurs dépendances

* Exportant pour visualiser vos données de télémétrie sur un backend, Jaeger.

L'utilisation de l'auto-instrumentation d'OpenTelemetry peut vous aider à obtenir des informations précieuses sur les performances et le comportement de vos applications Node.js sans avoir à instrumenter manuellement chaque bibliothèque ou framework.