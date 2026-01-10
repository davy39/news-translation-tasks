---
title: 'Comment déboguer les pipelines CI/CD : Un guide sur le dépannage avec les
  outils d''observabilité'
date: '2025-06-16T23:34:03.425Z'
author: Opaluwa Emidowojo
authorURL: https://www.freecodecamp.org/news/author/Tech-On-Diapers/
originalURL: https://freecodecamp.org/news/how-to-debug-cicd-pipelines-handbook
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1748620971355/d4893ec5-8016-491e-9626-15d971f0c885.png
tags:
- name: Devops
  slug: devops
- name: observability
  slug: observability
- name: '#prometheus'
  slug: prometheus
- name: Grafana
  slug: grafana
- name: promql
  slug: promql
- name: loki
  slug: loki
- name: handbook
  slug: handbook
seo_desc: Observability is a game-changer for CI/CD pipelines, and it’s one of the
  most exciting aspects of DevOps. When I started working with CI/CD systems, I assumed
  the hardest part would be building the pipeline. But with increasingly complex setups,
  the ...
---


L'observabilité change la donne pour les pipelines CI/CD, et c'est l'un des aspects les plus passionnants du DevOps. Quand j'ai commencé à travailler avec des systèmes CI/CD, je pensais que la partie la plus difficile serait de construire le pipeline. Mais avec des configurations de plus en plus complexes, le véritable défi est de déboguer les échecs, comme les builds qui plantent ou les tests qui échouent uniquement en production.

<!-- more -->

Les outils d'observabilité, tels que les logs, les métriques et les traces, offrent la visibilité nécessaire pour identifier rapidement les problèmes. Dans ce guide, nous explorerons des outils gratuits et open-source que vous pouvez utiliser pour rendre vos pipelines CI/CD plus fiables. Nous utiliserons des étapes pratiques pour dépanner comme un pro – aucune licence d'entreprise n'est requise.

## Table des matières

1.  [Prérequis][1]
    
2.  [Pourquoi l'observabilité est importante][2]
    
3.  [Comment installer et configurer Grafana Loki sur une infrastructure à petit budget][3]
    
4.  [Comment implémenter une alternative à la stack ELK pour l'observabilité des pipelines][4]
    
5.  [Comment créer une stratégie de journalisation unifiée à travers les composants du pipeline][5]
    
6.  [Comment interroger et analyser les logs pour un dépannage efficace][6]
    
7.  [Comment configurer les métriques Prometheus aux côtés de vos logs][7]
    
8.  [Comment créer des tableaux de bord Grafana combinant métriques et logs][8]
    
9.  [Comment utiliser les exemplaires pour passer des métriques aux logs pertinents][9]
    
10.  [Comment diagnostiquer et corriger les problèmes CI/CD courants][10]
    
11.  [Comment implémenter des techniques de débogage avancées][11]
    
12.  [Comment mener des post-mortems efficaces en utilisant les logs][12]
    
13.  [Comment optimiser le stockage et la gestion des logs][13]
    
14.  [Conclusion][14]
    

### Prérequis

Il y a certains points que vous devriez connaître et posséder pour tirer le meilleur parti de ce guide :

#### Connaissances techniques :

-   Compréhension de base des [pipelines CI/CD][15] (par exemple, les étapes de build, de test et de déploiement).
    
-   Familiarité avec les [commandes Linux/Unix][16] (par exemple, `mkdir`, `grep`, `curl`).
    
-   Aisance avec les [bases de Docker][17] (par exemple, `docker run`, `docker-compose up`).
    
-   Optionnel : Connaissance des [concepts d'observabilité][18] (logs, métriques, traces) ou de la configuration YAML.
    

#### Logiciels et outils :

-   **Docker et Docker Compose** : Installés et fonctionnels (vérifiez avec `docker --version` et `docker-compose --version`).
    
-   **Plateforme CI/CD** : Accès à GitHub Actions, Jenkins ou GitLab CI avec un exemple de pipeline générant des logs.
    
-   **Éditeur de texte** : Pour éditer les fichiers YAML (par exemple, VS Code, Nano).
    
-   **Navigateur Web** : Pour accéder aux interfaces des outils (par exemple, Grafana sur le port 3000, Kibana sur le 5601).
    
-   Optionnel : `curl` pour tester le transfert de logs, Git pour le contrôle de version.
    

#### Matériel et infrastructure :

-   Machine avec :
    
    -   OS : Linux, Windows (avec WSL2) ou macOS.
        
    -   4 Go de RAM (8 Go recommandés), 20 Go d'espace disque libre.
        
    -   Internet stable et capacité à ouvrir des ports (par exemple, 3100 pour Loki, 9200 pour Elasticsearch).
        
-   Optionnel : Accès à un fournisseur cloud (par exemple, AWS, GCP) pour des configurations évolutives.
    

#### Accès et permissions :

-   Accès administrateur pour installer Docker et configurer les outils CI/CD.
    
-   Permissions pour modifier les configurations de pipeline (par exemple, `.github/workflows`, `.gitlab-ci.yml`).
    
-   Optionnel : Accès à un registre de conteneurs (par exemple, Docker Hub) pour des images personnalisées.
    

## **Pourquoi l'observabilité est importante**

Les pipelines CI/CD modernes ne sont plus de simples scripts linéaires – ce sont désormais des systèmes distribués complexes impliquant plusieurs outils, environnements et couches d'infrastructure. Une tâche s'exécute sur GitHub Actions, une autre se déploie via Jenkins, et une troisième construit des images Docker dans un cluster Kubernetes.

Ainsi, quand quelque chose casse, vous vous retrouvez à traquer les logs à travers les outils, à deviner l'origine du problème et à perdre des heures à essayer de le reproduire.

Pire encore, les outils de débogage traditionnels s'arrêtent souvent à la surface, montrant seulement les tâches échouées sans le contexte du *pourquoi* elles ont échoué ou de l'*endroit* où se situe réellement la faille dans le système.

L'observabilité inverse la tendance. Au lieu de chasser à travers des logs déconnectés ou de relancer aveuglément des builds échoués, l'observabilité vous donne de la **compréhension**, pas seulement des données. En combinant logs structurés, métriques et traces, vous pouvez :

-   Reconstruire exactement ce qui s'est passé lors d'un échec de pipeline.
    
-   Tracer un échec à travers les agents CI, les étapes de déploiement et les conteneurs.
    
-   Visualiser les schémas et les anomalies avant qu'ils ne deviennent des pannes.
    

Plus important encore, l'observabilité vous aide à **passer d'un débogage réactif à une prévention proactive**.

Voici ce que vous apprendrez et accomplirez dans ce guide :

-   Mettre en place une observabilité rentable en utilisant Grafana Loki, un ELK léger et OpenTelemetry.
    
-   Créer une stratégie de journalisation unifiée pour connecter votre pipeline.
    
-   Écrire des requêtes précises pour identifier rapidement les causes racines, corréler les logs, les métriques et les traces pour un débogage complet.
    
-   Dépanner les problèmes CI/CD tels que les échecs de build, les tests instables et les crashs de conteneurs.
    
-   Construire des tableaux de bord personnalisés et des outils de diagnostic automatisés.
    
-   Promouvoir l'observabilité par la documentation et les post-mortems.
    

Que vous soyez un développeur indépendant ou que vous fassiez partie d'une équipe DevOps, ce guide transformera vos pipelines CI/CD chaotiques en systèmes clairs, fiables et observables.

### **Comment choisir le bon outil d'observabilité pour la CI/CD**

Voici une comparaison rapide de Grafana Loki, de l'ELK léger et de Vector pour l'observabilité CI/CD :

| **Outil** | **Utilisation des ressources** | **Complexité de configuration** | **Idéal pour** | **Adéquation CI/CD** |
| --- | --- | --- | --- | --- |
| **Grafana Loki** | Faible (léger) | Facile (basé sur Docker) | Petites équipes, infra à petit budget | Pipelines simples, logs JSON, utilisateurs Grafana |
| **ELK léger** | Élevée (Elasticsearch gourmand) | Modérée (multi-conteneurs) | Équipes ayant besoin de recherche/visualisation avancées | Pipelines complexes, besoins de requêtes riches |
| **Vector** | Très faible | Facile (binaire unique) | Configurations aux ressources limitées | Configurations minimales, transfert de logs |

Comment choisir :

-   **Loki** : Idéal pour les startups ou les développeurs solos avec des ressources limitées. S'intègre bien avec Prometheus/Grafana.
    
-   **ELK** : Idéal pour les équipes ayant besoin des visualisations avancées de Kibana ou gérant de gros volumes de logs.
    
-   **Vector** : Excellent pour le transfert de logs léger dans les configurations CI/CD distribuées.
    

**Grafana Loki** est un système d'agrégation de logs comme ELK, mais il est plus léger et idéal pour les pipelines CI/CD avec une infrastructure limitée.

## Comment installer et configurer Grafana Loki sur une infrastructure à petit budget

### 🛠 Option A : Configuration Docker rapide (recommandée pour infra à petit budget)

1.  **Créer un répertoire pour la configuration :**
    
    ```
     mkdir -p ~/loki-setup && cd ~/loki-setup
    ```
    
2.  **Créer un** `docker-compose.yml` :
    
    ```
     # Defines a Docker Compose setup for Grafana Loki and Promtail to aggregate and scrape logs efficiently.
     version: "3"
    
     services:
       loki:
         image: grafana/loki:2.9.4  # Uses Loki version 2.9.4 for lightweight log aggregation.
         ports:
           - "3100:3100"  # Exposes Loki’s HTTP API port for log ingestion and queries.
         command: -config.file=/etc/loki/loki-config.yaml  # Specifies the configuration file for Loki.
         volumes:
           - ./loki-config.yaml:/etc/loki/loki-config.yaml  # Mounts the local config file into the container.
    
       promtail:
         image: grafana/promtail:2.9.4  # Uses Promtail version 2.9.4 to scrape and forward logs to Loki.
         volumes:
           - /var/log:/var/log  # Mounts the host’s log directory for Promtail to scrape.
           - ./promtail-config.yaml:/etc/promtail/promtail-config.yaml  # Mounts the Promtail config file.
         command: -config.file=/etc/promtail/promtail-config.yaml  # Specifies the configuration file for Promtail.
    ```
    
3.  **Créer un** `loki-config.yaml` de base :
    
    ```
     # Configures Grafana Loki for lightweight log storage and querying in a CI/CD environment.
     auth_enabled: false  # Disables authentication for simplicity (not recommended for production).
    
     server:
       http_listen_port: 3100  # Sets the port for Loki’s HTTP API.
    
     ingester:
       lifecycler:
         ring:
           kvstore:
             store: inmemory  # Uses in-memory storage for the ring, suitable for small setups.
           replication_factor: 1  # Sets single replica for minimal resource use.
       chunk_idle_period: 3m  # Flushes chunks to storage after 3 minutes of inactivity.
       max_chunk_age: 1h  # Retires chunks after 1 hour to balance storage and query performance.
    
     schema_config:
       configs:
         - from: 2023-01-01  # Defines the schema start date.
           store: boltdb-shipper  # Uses BoltDB for indexing logs.
           object_store: filesystem  # Stores logs on the local filesystem.
           schema: v11  # Specifies schema version for log storage.
           index:
             prefix: index_  # Prefix for index files.
             period: 24h  # Rotates indexes daily.
    
     storage_config:
       boltdb_shipper:
         active_index_directory: /tmp/loki/index  # Directory for active index files.
         cache_location: /tmp/loki/boltdb-cache  # Cache location for BoltDB.
       filesystem:
         directory: /tmp/loki/chunks  # Directory for storing log chunks.
    
     limits_config:
       enforce_metric_name: false  # Disables strict metric name enforcement for flexibility.
    ```
    
4.  **Créer un** `promtail-config.yaml` de base :
    
    ```
     # Configures Promtail to scrape system logs and forward them to Loki.
     server:
       http_listen_port: 9080  # Sets Promtail’s HTTP port for metrics and health checks.
       grpc_listen_port: 0  # Disables gRPC to reduce resource usage.
    
     positions:
       filename: /tmp/positions.yaml  # Stores the position of scraped logs to resume after restarts.
    
     clients:
       - url: http://loki:3100/loki/api/v1/push  # Specifies the Loki endpoint for log ingestion.
    
     scrape_configs:
       - job_name: system  # Defines a scraping job for system logs.
         static_configs:
           - targets:
               - localhost  # Targets the local host for log collection.
             labels:
               job: varlogs  # Labels logs for easy querying in Loki.
               __path__: /var/log/*.log  # Scrapes all log files in /var/log directory.
    ```
    
5.  **Lancer le tout :**
    
    ```
     # Starts the Loki and Promtail containers in detached mode for background operation.
     docker-compose up -d
    ```
    

✨ Cela lance Loki et Promtail avec un minimum de ressources, sans authentification, et avec la récupération des logs depuis `/var/log`.

#### Dépannage des problèmes d'installation de Loki

Si Loki ou Promtail ne parvient pas à démarrer, l'un des problèmes suivants peut en être la cause :

1.  **Crashs de conteneurs** : Vérifiez les logs avec `docker logs loki` ou `docker logs promtail`. Recherchez des erreurs comme *“out of memory”* ou *“port already in use.”*
    
    -   Solution : Augmentez la mémoire (par exemple, via les limites de ressources dans `docker-compose.yml`) ou changez les ports (ex: `3101:3100`).
2.  **Logs non ingérés** : Vérifiez que Promtail scrute le bon chemin (`/var/log/ci/*.log`) en utilisant `docker exec promtail cat /etc/promtail/promtail-config.yaml`
    
    -   Solution : Mettez à jour `__path__` dans `promtail-config.yaml` pour correspondre à votre répertoire de logs CI/CD.
3.  **Contraintes de ressources** : Surveillez l'utilisation des ressources avec `docker stats` ou `top` sur l'hôte.
    
    -   Solution : Assurez-vous que votre machine dispose d'au moins 4 Go de RAM et 20 Go d'espace disque, comme spécifié dans les prérequis.

### Configuration pour la journalisation CI/CD

Pour adapter l'outil aux logs CI/CD, vous devriez :

#### 1\. Configurer vos outils CI/CD pour écrire les logs sur le disque :

Par exemple, GitHub Actions avec un runner personnalisé peut écrire des logs dans `/var/log/gha/*.log`.

Mettre à jour Promtail :

```
# Configures Promtail to scrape logs from GitHub Actions runners for CI/CD observability.
scrape_configs:
  - job_name: github_actions  # Defines a scraping job for GitHub Actions logs.
    static_configs:
      - targets: ['localhost']  # Targets the local host where the runner writes logs.
        labels:
          job: gha  # Labels logs for identification in Loki queries.
          __path__: /var/log/gha/*.log  # Scrapes logs from the specified directory.
```

#### 2\. Utiliser la journalisation structurée (JSON) :

Assurez-vous que vos outils ou scripts CI/CD produisent des logs au format structuré :

Exemple :

```
# Example of a structured JSON log for CI/CD pipelines, enabling easy parsing and querying.
{
  "timestamp": "2025-05-10T13:00:00Z",  # UTC timestamp for log entry.
  "level": "error",  # Log level to indicate severity.
  "job": "deploy",  # Identifies the CI/CD job (e.g., deploy stage).
  "message": "Image pull failed"  # Descriptive message for the error.
}
```

Cela facilite les requêtes avec LogQL.

### Comment connecter les agents CI à Loki

Cette section explique trois manières différentes d'envoyer les logs de votre pipeline CI dans Loki pour la surveillance et l'analyse :

#### Option 1 – Configuration locale :

Vos agents CI écrivent des fichiers de logs sur le disque, et Promtail (s'exécutant sur la même machine) lit ces fichiers et les envoie à Loki.

#### Option 2 – Utilisation du driver de journalisation Docker (conteneurs Docker) :

Si vos agents CI s'exécutent dans des conteneurs Docker, vous installez un plugin Loki spécial qui capture automatiquement toute la sortie des conteneurs et l'envoie directement à Loki sans avoir besoin de fichiers de logs séparés.

```
# Installs the Loki Docker logging driver to send container logs directly to Loki.
docker plugin install grafana/loki-docker-driver:latest --alias loki --grant-all-permissions
```

Ensuite, lancez votre conteneur agent :

```
# Runs a CI agent container with the Loki logging driver to forward logs.
docker run --log-driver=loki \
  --log-opt loki-url="http://<your-loki-host>:3100/loki/api/v1/push" \
  my-ci-agent-image
```

#### Option 3 – Configuration à distance :

Si vous ne pouvez pas installer Promtail localement, vous pouvez utiliser un outil de transfert de logs comme [Fluent Bit][19] ou [Vector][20] pour collecter les logs et les pousser vers Loki via le réseau.

**L'objectif :** Quelle que soit l'option choisie, vous finirez par centraliser tous les logs de votre pipeline CI dans Loki, où vous pourrez effectuer des recherches, créer des tableaux de bord dans Grafana et configurer des alertes en cas de problème.

Cela vous offre essentiellement la flexibilité d'intégrer la collecte de logs en fonction de votre configuration d'infrastructure – que vous préfériez des agents locaux, des plugins Docker ou le transfert à distance.

## Comment implémenter une alternative à la stack ELK pour l'observabilité des pipelines

Lorsque la stack ELK complète (Elasticsearch, Logstash, Kibana) est trop lourde pour votre infrastructure, vous pouvez opter pour des configurations légères qui offrent une observabilité similaire à un coût et une utilisation des ressources moindres.

### Comment installer des versions légères d'Elasticsearch, Logstash et Kibana

Objectif : Mettre en place une stack ELK minimale mais fonctionnelle pour le débogage des pipelines CI/CD.

#### 1\. Utiliser Docker pour lancer des conteneurs légers

Créez un `docker-compose.yml` :

```
# Defines a Docker Compose setup for a lightweight ELK stack to aggregate and visualize CI/CD logs.
version: '3.7'

services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.17.0  # Uses Elasticsearch 7.17.0.
    container_name: elasticsearch
    environment:
      - discovery.type=single-node  # Runs Elasticsearch in single-node mode for simplicity.
      - xpack.security.enabled=false  # Disables security features for lightweight setup.
    ports:
      - "9200:9200"  # Exposes Elasticsearch’s HTTP API port.
    volumes:
      - esdata:/usr/share/elasticsearch/data  # Persists Elasticsearch data.

  logstash:
    image: docker.elastic.co/logstash/logstash:7.17.0  # Uses Logstash 7.17.0.
    container_name: logstash
    ports:
      - "5044:5044"  # Port for receiving logs from Beats.
      - "9600:9600"  # Port for Logstash monitoring.
    volumes:
      - ./logstash.conf:/usr/share/logstash/pipeline/logstash.conf  # Mounts Logstash config file.

  kibana:
    image: docker.elastic.co/kibana/kibana:7.17.0  # Uses Kibana 7.17.0 for visualization.
    container_name: kibana
    environment:
      - ELASTICSEARCH_HOSTS=http://elasticsearch:9200  # Links Kibana to Elasticsearch.
    ports:
      - "5601:5601"  # Exposes Kibana’s web UI port.

volumes:
  esdata:  # Defines a volume for persisting Elasticsearch data.
```

#### 2\. Configuration minimale du pipeline Logstash (logstash.conf)

```
// Configures Logstash to process and forward CI/CD logs to Elasticsearch.
input {
  beats {
    port => 5044  // Listens for logs from Filebeat on port 5044.
  }
}

filter {
  json {
    source => "message"  // Parses JSON-formatted log messages for structured data.
  }
}

output {
  elasticsearch {
    hosts => ["http://elasticsearch:9200"]  // Sends processed logs to Elasticsearch.
    index => "ci-logs-%{+YYYY.MM.dd}"  // Stores logs in daily indexes (e.g., ci-logs-2025.05.14).
  }
}
```

#### Dépannage des problèmes d'installation ELK

Si Elasticsearch, Logstash ou Kibana ne parvient pas à démarrer, l'un des problèmes suivants peut être en cause :

1.  **Crashs de conteneurs** : Vérifiez les logs avec `docker logs elasticsearch`, `docker logs logstash` ou `docker logs kibana`. Recherchez des erreurs comme *“insufficient disk space”* ou *“port conflict”* (par exemple, 9200, 5601).
    
    -   Solution : Libérez de l'espace disque (assurez-vous d'avoir au moins 20 Go disponibles) ou changez les ports dans `docker-compose.yml` (par exemple, `9201:9200`).
2.  **Logs non ingérés** : Vérifiez que Logstash reçoit des données de Filebeat ou Vector en utilisant `docker logs logstash`. Vérifiez le port d'entrée dans `logstash.conf` (par exemple, 5044).
    
    -   Solution : Assurez-vous que Filebeat ou Vector est configuré pour envoyer vers le bon point de terminaison Logstash (ex: `localhost:5044`) et mettez à jour si nécessaire.
3.  **Contraintes de ressources** : Surveillez l'utilisation des ressources avec Docker stats ou top sur l'hôte.
    
    -   Solution : Allouez au moins 8 Go de RAM et 30 Go d'espace disque, car Elasticsearch nécessite plus de ressources que Loki. Ajustez les limites de mémoire dans `docker-compose.yml` si nécessaire.

### Comment configurer les agents d'expédition de logs pour différents composants CI/CD

Objectif : Envoyer les logs de votre pipeline dans Logstash ou Elasticsearch.

#### Option 1 : Utiliser Filebeat (agent d'expédition léger)

Installez [Filebeat][21] sur vos hôtes CI/CD (runner GitHub, nœud Jenkins, runner GitLab, etc.).

Extrait de configuration Filebeat (filebeat.yml) :

```
# Configures Filebeat to collect CI/CD logs and forward them to Logstash.
filebeat.inputs:
  - type: log  # Specifies log file input.
    enabled: true  # Enables the input.
    paths:
      - /var/log/ci/*.log  # Scrapes logs from the specified CI log directory.

output.logstash:
  hosts: ["localhost:5044"]  # Forwards logs to Logstash on port 5044.
```

Ensuite, lancez :

```
# Runs Filebeat with the specified configuration file for log collection.
filebeat -e -c filebeat.yml
```

#### Option 2 : Utiliser Vector.dev comme alternative plus économe en ressources à Filebeat

Configuration Vector (vector.toml) :

```
# Configures Vector to collect, parse, and forward CI/CD logs to Elasticsearch efficiently.
[sources.ci_logs]
  type = "file"  # Specifies file-based log collection.
  include = ["/var/log/ci/*.log"]  # Targets CI log files.

[transforms.json_parser]
  type = "remap"  # Uses remap transform to parse logs.
  inputs = ["ci_logs"]  # Processes logs from the ci_logs source.
  source = '''
  . = parse_json!(.message)  # Parses JSON log messages into structured data.
  '''

[sinks.to_elasticsearch]
  type = "elasticsearch"  # Sends logs to Elasticsearch.
  inputs = ["json_parser"]  # Uses parsed logs from the json_parser transform.
  endpoint = "http://localhost:9200"  # Specifies the Elasticsearch endpoint.
  index = "ci-logs"  # Stores logs in the ci-logs index.
```

Lancez :

```
# Runs Vector with the specified configuration file for log processing.
vector -c vector.toml
```

### Comment configurer les index patterns et les visualisations de base

Objectif : Rendre les logs CI/CD interrogeables et visuels dans Kibana.

#### 1\. Ouvrir Kibana ([http://localhost:5601][22])

-   Allez dans **Stack Management → Index Patterns**
    
-   Créez un nouvel index pattern : `ci-logs-*`
    
-   Choisissez un champ temporel comme `@timestamp`
    

#### 2\. Visualisations pour les cas d'utilisation CI/CD courants

-   **Graphiques à barres** : Nombre de builds échoués vs réussis par jour.
    
-   **Graphique en secteurs** : Types d'erreurs principaux ou noms de tests échouant le plus fréquemment.
    
-   **Graphique linéaire** : Durée des builds au fil du temps (si la durée est journalisée).
    

#### 3\. Recherches sauvegardées et tableaux de bord

Vous pouvez sauvegarder une recherche comme celle-ci :

```
message: "error" AND job_name: "build"
```

Vous pouvez également combiner les visualisations dans un tableau de bord de santé CI/CD.

## Comment créer une stratégie de journalisation unifiée à travers les composants du pipeline

Créer une stratégie de journalisation unifiée à travers les composants de votre pipeline CI/CD garantit que les logs sont cohérents, traçables et faciles à corréler. Cela vous aide à déboguer rapidement les problèmes, à surveiller la santé du système et à tracer les requêtes à travers différents outils et services. Discutons de quelques pratiques clés pour y parvenir :

### Implémenter des formats de logs cohérents à travers différents outils

Des formats de logs cohérents sont importants pour diverses raisons. Tout d'abord, un format de log standardisé facilite les requêtes, la recherche et la visualisation. Il aide également à la corrélation des logs de différents services. Et la cohérence garantit également que tous les logs fournissent les détails nécessaires comme l'horodatage, le niveau de log et le contexte de la requête.

Il existe également des meilleures pratiques à suivre lors du formatage des logs :

Le **format JSON** est fortement recommandé car il est structuré, lisible par machine et compatible avec de nombreux outils d'observabilité (par exemple, Loki, Elasticsearch, Grafana).

Voici quelques champs clés à inclure :

-   `timestamp` : L'heure à laquelle l'entrée de log a été créée (de préférence en UTC).
    
-   `log_level` : Indique si le log est une `INFO`, une `ERROR`, un `DEBUG`, etc.
    
-   `service` : Le service ou composant générant le log.
    
-   `message` : Une description concise de l'événement ou de l'erreur.
    
-   `correlation_id` : Un identifiant unique pour les requêtes afin de tracer les logs à travers les systèmes.
    

Voici un exemple d'un log cohérent au format JSON :

```
{
  "timestamp": "2025-05-10T12:34:56Z",
  "log_level": "ERROR",
  "service": "ci_cd_pipeline",
  "message": "Build failed due to missing dependency",
  "correlation_id": "1234567890abcdef"
}
```

### Comment configurer le transfert de logs depuis GitHub Actions, Jenkins ou GitLab

Le transfert de logs consiste à envoyer les logs de vos pipelines CI/CD vers un point central pour un suivi facile. C'est utile car cela vous permet de repérer rapidement les problèmes et de déboguer sans fouiller dans des fichiers dispersés.

Pour GitHub Actions, vous pouvez configurer les workflows pour écrire les logs dans un fichier ou les envoyer directement à un outil d'agrégation de logs comme Loki. Dans Jenkins, vous pouvez utiliser des scripts de pipeline pour transférer les logs vers un serveur de logs ou un système de fichiers. De même, pour GitLab CI, vous pouvez ajouter des scripts dans `.gitlab-ci.yml` pour transférer les logs vers un point de terminaison centralisé.

**Utilisation des Actions pour la sortie des logs :**  
Vous pouvez stocker les logs dans des fichiers puis les transférer vers un système de journalisation (comme Loki ou Elasticsearch).  
Voici un exemple dans un workflow GitHub Action :

```
# Defines a GitHub Actions workflow to run tests and forward logs for observability.
jobs:
  build:
    runs-on: ubuntu-latest  # Uses an Ubuntu runner.
    steps:
      - name: Checkout repository  # Checks out the repository code.
        uses: actions/checkout@v2
      - name: Run tests and log output  # Runs tests and saves output to a log file.
        run: |
          echo "Starting tests..."
          npm test | tee test.log  # Captures test output to test.log.
          # Forwards the log file to a Loki endpoint via HTTP POST.
          curl -X POST -F 'file=@test.log' http://your-loki-endpoint
```

**Transfert de logs avec Promtail :**  
Si vous utilisez Grafana Loki pour l'agrégation de logs, configurez Promtail pour récupérer les logs du runner GitHub Actions.

#### Jenkins :

Les logs Jenkins peuvent être transférés vers des systèmes externes (comme Elasticsearch ou Loki) en utilisant des agents d'expédition de logs ou des plugins.

**Vous pouvez utiliser le plugin Logstash** pour transférer les logs Jenkins vers une stack ELK ou d'autres systèmes :

-   Installez le plugin Logstash sur Jenkins.
    
-   Configurez le plugin pour transférer les logs vers un serveur Elasticsearch ou un système de journalisation de votre choix.
    
-   Dans Jenkins, ajoutez les configurations de transfert de logs :
    

```
pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        script {
          // Example of forwarding logs to a log server
          sh 'echo "Build successful" | curl -X POST -d @- http://your-log-server'
        }
      }
    }
  }
}
```

**Transfert vers Loki :**  
Jenkins supporte le driver de journalisation `loki` pour les conteneurs si Jenkins s'exécute dans Docker. Vous pouvez envoyer les logs directement à Loki en utilisant ce driver :

```
# Runs a Jenkins container with the Loki logging driver to send logs directly to Loki.
docker run --log-driver=loki --log-opt loki-url=http://loki:3100 jenkins/jenkins:lts
```

#### GitLab :

GitLab CI permet de transférer les logs vers des systèmes externes pour une collecte et une analyse centralisées.

**Utiliser GitLab CI/CD pour sortir les logs** :  
Exemple dans `.gitlab-ci.yml` :

```
# Defines a GitLab CI/CD pipeline to run a build and forward logs to Loki.
stages:
  - build
build:
  script:
    - echo "Starting the build" | tee build.log  # Saves build output to build.log.
    - curl -X POST -d @build.log http://your-loki-endpoint  # Forwards the log to Loki.
```

**Runners GitLab** :  
Configurez les runners GitLab pour transférer les logs vers un service externe comme Loki ou Elasticsearch en utilisant les paramètres `log-driver` ou l'agent d'expédition `fluentd`.

### Comment ajouter des IDs de corrélation pour tracer les requêtes à travers le système

#### Pourquoi les IDs de corrélation sont importants :

Les IDs de corrélation vous permettent de tracer une seule requête alors qu'elle voyage à travers différents services et outils, offrant une visibilité de bout en bout et facilitant le dépannage.

Ils sont critiques pour déboguer les systèmes distribués, surtout quand différents services (par exemple, outil CI, outil de déploiement, service API) sont impliqués.

#### Comment ajouter des IDs de corrélation :

Vous pouvez utiliser un UUID (Universally Unique Identifier) ou un GUID (Globally Unique Identifier) pour générer un ID unique pour chaque requête.

Si vous utilisez des microservices ou plusieurs services dans le pipeline, assurez-vous simplement que le même ID est propagé à travers chaque service.

De nombreuses bibliothèques de journalisation (par exemple, `winston` pour Node.js, `log4j` pour Java) supportent la génération et la journalisation automatiques d'ID de corrélation.

Voici un exemple en Node.js (utilisant `winston`) :

```
// Sets up Winston for structured logging with correlation IDs in a CI/CD pipeline.
const { createLogger, transports, format } = require('winston');
const { printf } = format;

// Creates a logger with a custom format including correlation IDs.
const logger = createLogger({
  format: printf(({ level, message, timestamp }) => {
    return `${timestamp} [${level}] ${message} correlation_id=${generateCorrelationId()}`;
  }),
  transports: [
    new transports.Console(),  // Outputs logs to the console.
  ],
});

// Generates a random correlation ID for tracing requests.
function generateCorrelationId() {
  return Math.random().toString(36).substring(2, 15);
}

// Logs a sample message.
logger.info('Pipeline execution started');
```

#### Comment propager les IDs de corrélation entre les services :

Dans les outils CI/CD, vous pouvez configurer votre pipeline pour injecter l'ID de corrélation dans les logs. Par exemple, dans GitHub Actions, vous pouvez générer un ID de corrélation dans la section `env` et le propager dans chaque tâche :

```
# Defines a GitHub Actions workflow that includes a correlation ID for log tracing.
jobs:
  build:
    runs-on: ubuntu-latest  # Uses an Ubuntu runner.
    env:
      CORRELATION_ID: ${{ github.run_id }}  # Uses the GitHub run ID as a correlation ID.
    steps:
      - name: Checkout repository  # Checks out the repository code.
        uses: actions/checkout@v2
      - name: Log build start with correlation ID  # Logs the build start with the correlation ID.
        run: echo "Build started with Correlation ID: $CORRELATION_ID"
```

#### Inclure les IDs de corrélation dans tous les logs :

Vous voudrez vous assurer que les logs de tous les composants du pipeline (GitHub Actions, Jenkins, GitLab, outils de déploiement, etc.) incluent l'ID de corrélation dans le message de log. Cela vous permet de tracer les logs d'une seule requête ou d'une exécution de pipeline à travers différents services.

#### Visualiser votre flux de logs

Vous pouvez créer un diagramme montrant comment les logs se déplacent de votre outil CI/CD (par exemple, GitHub Actions) vers Promtail/Vector, puis vers Loki/Elasticsearch, et enfin vers Grafana/Kibana pour la visualisation. Utilisez des outils comme [Draw.io][23] pour cartographier le flux d'observabilité de votre pipeline.

## Comment interroger et analyser les logs pour un dépannage efficace

Dans cette section, vous apprendrez à utiliser LogQL (le langage de requête de Loki) pour filtrer le bruit et trouver les logs spécifiques qui comptent. Que vous traquiez un échec de build mystérieux ou des problèmes de déploiement à travers plusieurs services, ces schémas de requête vous aideront toujours.

![Graphique à barres montrant les résultats de build CI/CD du 20 au 26 mai 2025. Les barres bleues représentent les builds réussis allant de 39 à 52 par jour, tandis que les barres rouges montrent les builds échoués allant de 1 à 9 par jour. Le graphique démontre des taux de réussite constamment élevés avec de faibles taux d'échec tout au long de la semaine, le 23 mai montrant le nombre d'échecs le plus élevé avec 9 builds.](https://cdn.hashnode.com/res/hashnode/image/upload/v1748224707087/d348accc-0ef8-4ebb-9cb9-49995404b0ec.png)

Ce graphique à barres illustre la performance des builds CI/CD du 20 au 26 mai 2025. Il compare le nombre de builds réussis (en bleu) aux builds échoués (en rose) chaque jour. Les builds réussis se situent systématiquement entre 40 et 50, tandis que les builds échoués culminent à 10 le 23 mai, les autres jours affichant entre 2 et 8 échecs. Cela indique un pipeline généralement stable avec des problèmes occasionnels.

### Comment écrire des requêtes LogQL avancées pour identifier les problèmes CI/CD

LogQL est le langage de requête de Grafana Loki, conçu pour interroger les logs avec une syntaxe similaire au PromQL de Prometheus. Il permet des recherches de logs efficaces et est particulièrement utile pour dépanner les problèmes CI/CD.

#### Syntaxe LogQL de base :

**1. Flux de logs :**

```
{job="ci_cd", level="error"}
```

Cette requête récupère les logs où le label `job` est `ci_cd` et le label `level` est `error`.

**2. Filtres de logs :**

```
{job="ci_cd"} |= "build failed"
```

L'opérateur `|=` filtre les logs pour n'inclure que ceux qui contiennent la chaîne spécifiée, par exemple "build failed".

**3. Expressions régulières :**

```
{job="ci_cd"} |~ "error.*timeout"
```

Ceci utilise l'opérateur `|~` pour filtrer les logs à l'aide d'une expression régulière. Dans ce cas, il trouve les logs qui contiennent "error" suivi de "timeout".

#### Requêtes LogQL avancées pour les problèmes CI/CD :

**1. Filtrer les logs pour des échecs de build spécifiques :**

Si votre pipeline utilise un label spécifique pour les noms de build :

```
{job="ci_cd", build="build123"} |= "failure"
```

Ceci trouve les logs liés à la tâche `build123` qui contiennent le mot "failure".

**2. Utilisation de la plage temporelle et du regroupement :**

Pour trouver les logs d'erreur des 15 dernières minutes :

```
{job="ci_cd", level="error"} | "build failed" | range(start="15m")
```

Pour regrouper les logs par tâche et par type d'erreur :

```
sum by (job) (count_over_time({job="ci_cd", level="error"}[5m]))
```

Ceci renverra le nombre de logs d'erreur par tâche, regroupés par nom de tâche, sur les 5 dernières minutes.

### Comment créer des requêtes spécifiques au pipeline pour les schémas d'échec courants

#### Schémas d'échec courants dans les pipelines CI/CD :

**1. Échecs de build :**

Si les logs de votre système CI contiennent des erreurs de build, vous pouvez les identifier avec :

```
{job="ci_cd", level="error"} |= "build failed"
```

Vous pouvez étendre cela pour filtrer par étapes spécifiques, par exemple, "test failed" ou "compilation error".

**2. Échecs de tests :**

Les logs de votre lanceur de tests (par exemple, Jest, Mocha, JUnit) peuvent contenir des messages d'échec spécifiques :

```
{job="ci_cd", stage="test"} |= "test failed"
```

**3. Problèmes de dépendances :**

Si votre pipeline échoue à cause de dépendances manquantes ou conflictuelles, recherchez les erreurs liées à `npm`, `maven` ou `docker` :

```
{job="ci_cd", image="node"} |= "npm ERR!"
```

Ou pour les problèmes liés à Maven :

```
{job="ci_cd", image="maven"} |= "[ERROR]"
```

**4. Contraintes de ressources (par exemple, manque de mémoire) :**

Si vous rencontrez des contraintes de ressources, vous pourriez voir des logs comme "OutOfMemoryError" :

```
{job="ci_cd", level="error"} |= "OutOfMemoryError"
```

**Exemple de combinaison de filtres :**

```
{job="ci_cd", level="error"} |= "build failed" |~ "timeout|dependency" | range(start="1h")
```

Cette requête combine des filtres de logs pour "build failed", correspondant à tous les logs contenant les termes "timeout" ou "dependency", au cours de la dernière heure.

### Comment configurer des règles d'alerte basées sur les schémas de logs

Les alertes aident à détecter les problèmes récurrents de manière proactive. Elles vous informent lorsqu'un schéma spécifique apparaît dans vos logs, vous permettant de prendre des mesures rapides.

#### **Étapes pour configurer les alertes :**

**1. Créer une requête pour l'alerte :**

Tout d'abord, définissez le schéma de log que vous souhaitez surveiller. Par exemple, une alerte pour les échecs de build :

```
{job="ci_cd", level="error"} |= "build failed"
```

**2. Créer une alerte dans Grafana :**

Suivez ces étapes pour configurer les alertes Grafana :

-   Allez sur votre tableau de bord Grafana.
    
-   Choisissez le panneau sur lequel vous souhaitez configurer l'alerte (ou créez un nouveau panneau à cet effet).
    
-   Dans le panneau, cliquez sur l'onglet **Alert**.
    
-   Définissez le champ **Query** avec votre requête LogQL, comme celle ci-dessus.
    
-   Sous **Conditions**, définissez quand l'alerte doit se déclencher, par exemple, si l'erreur se produit plus de `3` fois en `5 minutes`.
    

**3. Paramètres d'alerte :**

Vous voudrez maintenant configurer l'intervalle d'évaluation de l'alerte et les conditions de déclenchement (par exemple, si la requête renvoie des résultats au-dessus d'un certain seuil).

**Voici un exemple :** Déclencher une alerte si le nombre d'erreurs dépasse 5 en 5 minutes :

```
count_over_time({job="ci_cd", level="error"} |= "build failed"[5m]) > 5
```

**4. Configurer les notifications d'alerte :**

Vous pouvez choisir où vous souhaitez que l'alerte soit envoyée (comme Slack, e-mail ou PagerDuty). Grafana peut être intégré à ces systèmes pour envoyer des alertes en temps réel aux membres de l'équipe concernés.

**Exemple de requête d'alerte pour les échecs de tests :**

```
count_over_time({job="ci_cd", stage="test"} |= "test failed"[5m]) > 3
```

Cette requête déclenche une alerte si plus de 3 échecs de tests sont journalisés au cours des 5 dernières minutes.

### Plongée au cœur du Kibana Query Language pour les contextes CI/CD

Le Kibana Query Language (KQL) est un outil puissant pour rechercher et filtrer les logs dans Elasticsearch, et il devient particulièrement utile pour déboguer les pipelines CI/CD.

#### Syntaxe de requête de base :

-   **Champ :**
    
    ```
      fieldname:value
    ```
    
    Exemple : `status: "failure"`
    
-   **Caractère générique :** Utilisez `*` pour correspondre à n'importe quel nombre de caractères :
    
    ```
      message: "test*"
    ```
    
-   **Requêtes de plage :** Pour rechercher des logs dans un intervalle de temps spécifique :
    
    ```
      timestamp:[2023-05-01 TO 2023-05-15]
    ```
    
-   **Requêtes booléennes :** Combinez des requêtes en utilisant `AND`, `OR` et `NOT` :
    
    ```
      status: "failure" AND build_id: "12345"
    ```
    

#### Requêtes basées sur le temps :

Comme les logs CI/CD sont souvent liés à des opérations sensibles au temps (builds, déploiements), KQL vous permet de filtrer les logs par temps :

```
@timestamp:[now-1d TO now]
```

#### Requêtes imbriquées (pour les pipelines complexes) :

Les logs CI/CD peuvent avoir des structures imbriquées ou à plusieurs niveaux (par exemple, des logs à l'intérieur de conteneurs). Vous pouvez interroger ces champs imbriqués :

```
pipeline.logs.message: "build failed"
```

#### Agrégations et regroupement :

Vous pouvez agréger les logs en fonction de certains champs pour identifier des tendances ou des problèmes récurrents :

```
terms aggregation on "status" field
```

Cela aide à identifier les statuts d'échec les plus courants dans votre pipeline.

#### Filtrage spécifique au champ :

Lors du débogage de composants spécifiques comme un outil de build ou une étape de déploiement, vous pouvez filtrer par ces champs spécifiques au composant :

```
build_tool: "Jenkins" AND status: "failure"
```

#### Créer des recherches sauvegardées pour les problèmes récurrents

Une fois que vous avez construit des requêtes qui vous aident à identifier les problèmes courants dans votre pipeline CI/CD, vous pouvez les sauvegarder dans Kibana pour une utilisation future.

**1. Créer une recherche sauvegardée :**

Exécutez votre requête souhaitée dans l'onglet Discover de Kibana. Cliquez sur le bouton "Save" et donnez-lui un nom significatif, tel que "Failed Builds - Last Week". Vous pouvez ajouter des filtres et personnaliser la plage horaire pour correspondre à vos schémas de problèmes typiques.

**2. Utiliser des filtres pour identifier les problèmes récurrents :**

Créez des recherches sauvegardées qui se concentrent sur des problèmes récurrents spécifiques comme :

-   Échecs de build basés sur un outil ou une version spécifique.
    
-   Échecs de tests dans un module ou un ensemble de tests particulier.
    

Exemple de recherche pour les "tests instables" :

```
test_status: "failed" AND error_message: "*timeout*"
```

**3. Sauvegarder plusieurs variations :**

Vous pouvez sauvegarder plusieurs variations de requêtes basées sur différents types d'erreurs ou outils CI/CD :

-   **Tâches échouées :** `status: "failure"`
    
-   **Échecs de tests dans le build :** `log_type: "test" AND status: "failure"`
    
-   **Contraintes de ressources :** `error_message: "*memory*"`
    

Ces recherches sauvegardées vous permettront de dépanner rapidement des problèmes spécifiques qui surviennent fréquemment.

#### Créer des visualisations pour repérer les schémas au fil du temps

Une fois que vous avez des recherches sauvegardées, Kibana vous permet de créer des visualisations à partir de vos données, facilitant ainsi le repérage des tendances, des anomalies ou des schémas au fil du temps.

**1. Créer une visualisation :**

Allez dans l'onglet **Visualize** de Kibana. Sélectionnez le type de visualisation approprié. Les visualisations courantes pour déboguer les pipelines CI/CD incluent :

-   **Graphique linéaire :** Suivre les taux d'échec des builds au fil du temps.
    
-   **Graphique à barres :** Afficher le nombre d'échecs par outil CI ou service.
    
-   **Graphique en secteurs :** Répartition des raisons d'échec (par exemple, erreurs de compilation, échecs de tests, contraintes de ressources).
    

**2. Suivre les tendances d'échec au fil du temps :**

Créez un graphique linéaire pour suivre les échecs de build sur une période donnée :

-   **Axe X :** Temps (par exemple, quotidien ou hebdomadaire).
    
-   **Axe Y :** Nombre d'échecs de build.
    
-   **Agrégation :** Histogramme de date avec le champ `@timestamp`.
    

Cela vous aidera à visualiser l'évolution des échecs de build, facilitant l'identification des problèmes récurrents ou des pics d'échecs.

**3. Surveiller les types d'échec par outil CI :**

Créez un graphique à barres qui montre le nombre d'échecs répartis par outil CI :

-   **Axe X :** Outil CI (Jenkins, GitHub Actions, GitLab, etc.).
    
-   **Axe Y :** Nombre d'échecs.
    
-   **Agrégation :** Agrégation de termes sur le champ `ci_tool`.
    

Cette visualisation aide à identifier quel outil CI rencontre le plus d'échecs et à concentrer les efforts de dépannage à cet endroit.

**4. Visualiser les messages d'erreur par fréquence :**

Vous pouvez visualiser quels messages d'erreur apparaissent le plus fréquemment, vous aidant à comprendre ce qui pourrait causer des problèmes récurrents :

-   **Axe X :** Type de message d'erreur.
    
-   **Axe Y :** Nombre d'occurrences.
    
-   **Agrégation :** Agrégation de termes sur le champ `error_message`.
    

**5. Tableau de bord pour une surveillance holistique :**

Créez un tableau de bord qui rassemble plusieurs visualisations. Vous pouvez avoir un graphique pour les tendances d'échec, un autre pour les types d'échec (graphique à barres) et un graphique en secteurs montrant le pourcentage d'échecs causés par différents problèmes. Ce tableau de bord vous donne une vue holistique de la santé de votre pipeline.

#### Techniques de visualisation avancées :

Il existe diverses techniques avancées que vous pouvez utiliser pour approfondir vos données.

-   **Cartes de chaleur (Heatmaps)** : Utilisez des cartes de chaleur pour repérer les anomalies temporelles dans les durées de build ou les échecs de tests.
    
-   **Détection d'anomalies** : Kibana dispose d'une détection d'anomalies intégrée qui peut être appliquée aux données de logs pour détecter automatiquement les schémas qui s'écartent de la norme. C'est particulièrement utile pour attraper des erreurs rares ou inattendues dans votre pipeline CI/CD.
    
    Exemple pour la détection d'anomalies :
    
    ```
      field: duration
      aggregation: average
      anomaly detection model: "baseline"
    ```
    

## Comment configurer les métriques Prometheus aux côtés de vos logs

Pour comprendre pleinement la santé et la performance de votre pipeline CI/CD, combiner métriques et logs est essentiel. Prometheus est un excellent outil pour capturer des métriques de séries temporelles, et il fonctionne parfaitement avec Grafana et Loki (ou tout autre système d'agrégation de logs).

### **Comment configurer Prometheus pour la collecte de métriques CI/CD :**

#### 1. Installer Prometheus :

Vous pouvez installer Prometheus en utilisant Docker ou Kubernetes pour un déploiement facile.

Pour une installation basée sur Docker :

```
docker run -d -p 9090:9090 --name prometheus prom/prometheus
```

#### **2. Configurer Prometheus pour récupérer les métriques :**

Prometheus doit être configuré pour récupérer les métriques de vos services CI/CD.

Éditez le fichier `prometheus.yml` :

```
scrape_configs:
  - job_name: 'ci_cd_metrics'
    static_configs:
      - targets: ['localhost:8080', 'localhost:9091']
```

#### 3. Instrumenter vos services CI/CD :

Pour exposer des métriques, vous devez intégrer les bibliothèques clientes Prometheus dans vos services CI/CD.

Par exemple, pour exposer les métriques de build d'une tâche Jenkins, utilisez le [plugin Prometheus pour Jenkins][24]. Dans GitHub Actions, vous pouvez utiliser [Prometheus][25] pour exposer les métriques des tâches.

#### **4. Exposer le point de terminaison des métriques :**

Vous voudrez vous assurer que vos services exposent un point de terminaison `/metrics` que Prometheus peut scruter. Par exemple, utilisez les bibliothèques clientes Prometheus dans votre application pour exposer ce point de terminaison.

#### Dépannage des problèmes d'installation de Prometheus

Si Prometheus ne parvient pas à démarrer ou à récupérer les métriques, voici quelques points qui pourraient poser problème :

1.  **Crashs de conteneurs** : Vérifiez les logs avec `docker logs prometheus`. Recherchez des erreurs comme “port already in use” (par exemple, 9090) ou des problèmes d'analyse de configuration.
    
    -   Solution : Changez le port dans `docker run` (par exemple, `-p 9091:9090`) ou corrigez la syntaxe du fichier `prometheus.yml`.
2.  **Métriques non récupérées** : Vérifiez que les cibles sont accessibles en utilisant `docker logs prometheus` ou testez avec curl `http://localhost:9090/targets`. Vérifiez les points de terminaison corrects dans `prometheus.yml`.
    
    -   Solution : Mettez à jour les `targets` dans `scrape_configs` (par exemple, `localhost:8080`) pour correspondre au point de terminaison des métriques de votre service CI/CD.
3.  **Contraintes de ressources** : Surveillez l'utilisation avec docker stats ou top sur l'hôte.
    
    -   Solution : Assurez-vous d'avoir au moins 4 Go de RAM et 10 Go d'espace disque. Augmentez la rétention de stockage ou réduisez la fréquence de récupération dans `prometheus.yml` si nécessaire.

## Comment créer des tableaux de bord Grafana combinant métriques et logs

Une fois que Prometheus collecte des métriques, l'étape suivante consiste à les visualiser et à les corréler dans Grafana.

### **Comment intégrer Prometheus avec Grafana :**

Tout d'abord, vous devrez installer Grafana. Vous pouvez utiliser Docker ou Kubernetes pour un déploiement rapide :

```
docker run -d -p 3000:3000 --name grafana grafana/grafana
```

Ensuite, configurez Grafana pour utiliser Prometheus comme source de données. Pour ce faire, connectez-vous à Grafana (`localhost:3000` par défaut). Allez dans `Configuration` > `Data Sources` > `Add Data Source` > Choisissez `Prometheus`. Entrez l'URL de votre serveur Prometheus (par exemple, `http://localhost:9090`) et cliquez sur `Save & Test`.

Il est maintenant temps de construire un tableau de bord unifié. Pour ce faire, créez un nouveau tableau de bord dans Grafana qui combine à la fois les logs (Loki) et les métriques (Prometheus).

Ajoutez un panneau avec des requêtes de données Prometheus pour visualiser les métriques du pipeline comme le taux de réussite des builds, la durée du déploiement et le nombre d'échecs. Utilisez le type de visualisation `Graph` pour les données de séries temporelles et `Stat` pour les métriques de résumé rapide.

Enfin, dans le même tableau de bord Grafana, ajoutez des panneaux pour les logs (provenant de Loki ou de tout autre système de journalisation). Utilisez le panneau `Logs` pour visualiser les données de logs et liez-les aux métriques Prometheus pertinentes en utilisant des corrélations basées sur le temps.

**Exemple** : Si un pic d'utilisation du CPU est détecté (métrique Prometheus), le panneau de logs pourrait montrer les logs associés, comme des erreurs ou des tâches de build échouées.

## Comment utiliser les exemplaires pour passer des métriques aux logs pertinents

Les exemplaires (exemplars) sont une fonctionnalité avancée de Prometheus qui permet de connecter les données de métriques aux logs et aux traces. Grafana supporte cette fonctionnalité, et elle peut être incroyablement utile lors de l'investigation de problèmes.

### Comment configurer les exemplaires dans Prometheus :

**1. Activer les exemplaires dans votre application :**

Les exemplaires sont essentiellement des traces intégrées dans vos métriques. Pour les utiliser, vous devrez vous assurer que votre application est instrumentée pour envoyer des données d'exemplaires en même temps que vos métriques.

De nombreuses bibliothèques supportent l'ajout d'exemplaires aux métriques Prometheus, telles que `prom-client` (Node.js) et `prometheus-net` (C#).

Voici un exemple en Node.js :

```
// Demonstrates adding an exemplar to a Prometheus metric for linking to logs or traces.
const promClient = require('prom-client');

// Creates a counter metric to track failed CI/CD builds.
const counter = new promClient.Counter({
  name: 'ci_cd_failed_builds_total',  // Metric name for failed builds.
  help: 'Total number of failed builds',  // Description of the metric.
});

// Increments the counter with an exemplar for tracing.
counter.inc({ exemplar: 'build_failed' });
```

**2. Activer les exemplaires dans la configuration Prometheus :**

Assurez-vous que votre serveur Prometheus est configuré pour stocker et exposer les exemplaires. Les exemplaires sont généralement inclus avec les métriques d'histogramme ou de résumé, assurez-vous donc de les avoir configurés correctement.

**3. Visualiser les exemplaires dans Grafana :**

Dans Grafana, lorsque vous interrogez Prometheus pour des métriques avec des exemplaires, Grafana affichera les logs ou traces liés lorsque vous survolerez une métrique.

Utilisez l'option `Exemplar` dans les panneaux Grafana pour accéder rapidement aux logs à partir de métriques spécifiques.

Par exemple, si vous avez une métrique `build_failure_total` et que vous détectez un échec dans votre pipeline, vous pouvez cliquer sur la métrique d'échec dans Grafana et visualiser instantanément les logs pertinents pour cet échec spécifique en utilisant les exemplaires.

## Comment diagnostiquer et corriger les problèmes CI/CD courants

Les pipelines CI/CD rencontrent souvent des problèmes tels que des échecs de build, des problèmes de dépendances et des tests instables qui peuvent perturber les workflows de développement. Cette section fournit des stratégies pratiques pour diagnostiquer et résoudre ces problèmes courants en utilisant l'analyse de logs et des techniques de débogage systématiques, vous aidant à restaurer rapidement la stabilité du pipeline.

### **Stratégie 1 : Déboguer systématiquement les échecs de build**

Les échecs de build sont un défi fréquent en CI/CD, provenant souvent d'erreurs dans le code, les tests ou les configurations. Le débogage systématique de ces problèmes implique l'analyse des logs pour identifier les causes racines, en utilisant les approches suivantes.

#### Identifier les schémas dans les sorties du compilateur et des tests

Lors du débogage des échecs de build, vous devez d'abord examiner les logs des sorties du compilateur et des tests. Passons en revue quelques stratégies clés.

#### 1. Rechercher des messages d'erreur spécifiques :

Il existe quelques types courants de messages d'erreur que vous pourriez recevoir. Ce sont :

-   **Erreurs de syntaxe** : Recherchez les lignes indiquant qu'il y a une erreur de syntaxe, comme des points-virgules manquants, des variables non déclarées ou des appels de fonction incorrects.
    
-   **Erreurs de l'éditeur de liens (Linker)** : Celles-ci se produisent souvent lorsque les bibliothèques ou dépendances requises ne sont pas trouvées. Vous verrez généralement des erreurs comme `undefined reference` ou `symbol not found`.
    
-   **Erreurs de l'outil de build** : Si vous utilisez des systèmes de build comme Maven, Gradle ou MSBuild, leurs logs donneront des codes d'erreur spécifiques ou des configurations manquantes.
    

#### 2. Rechercher des schémas d'erreur courants :

Souvent, les builds échoués répètent la même erreur ou le même schéma à travers plusieurs exécutions. Vérifiez les logs pour des termes récurrents ou des erreurs qui pointent vers des modules ou fonctions spécifiques. Et rappelez-vous que le regroupement de problèmes similaires peut vous aider à identifier la cause racine plus rapidement.

#### 3. Utiliser des expressions régulières pour le filtrage des logs :

Vous pouvez utiliser des expressions régulières pour rechercher des mots-clés dans les logs qui correspondent à des schémas d'échec courants (par exemple, "error", "failed", "exception", "out of memory"). Cela vous aidera à filtrer les messages non liés et à vous concentrer sur les échecs.

**À titre d'exemple :**

-   Si le build échoue avec une erreur "Out of Memory", recherchez tout problème d'allocation de mémoire ou des paramètres qui peuvent être augmentés.
    
-   Si les échecs de tests sont liés à des modules spécifiques, inspectez ces modules pour des changements récents ou des problèmes de dépendances.
    

### Stratégie 2 : Dépannage des problèmes de dépendances avec l'analyse de logs

Les problèmes de dépendances sont courants dans les échecs de build, en particulier dans les pipelines CI/CD complexes avec plusieurs modules ou services. Pour résoudre ces problèmes, considérez les points suivants :

**1. Vérifier les dépendances manquantes ou obsolètes** :

Commencez par examiner la sortie de l'outil de build pour vérifier les messages liés aux dépendances manquantes (par exemple, `dependency not found`, `version conflict`).

De nombreux outils de build (comme Maven, npm ou .NET) incluront des messages d'erreur spécifiques lorsqu'une dépendance est manquante ou incompatible.

**2. Inspecter les logs de résolution de dépendances** :

Certains outils de build fournissent des logs détaillés montrant comment les dépendances ont été résolues (par exemple, la version d'une bibliothèque qui a été utilisée). Ces logs peuvent vous montrer s'il y a une inadéquation de version.

Assurez-vous que vos fichiers `package.json` (pour les projets JavaScript), `pom.xml` (pour Java) ou `csproj` (pour C#) sont correctement définis avec des versions compatibles.

**3. Vérifier la connectivité réseau** :

Les outils CI/CD échouent parfois à récupérer les dépendances en raison de problèmes de réseau (par exemple, paramètres de proxy, accès au dépôt). Recherchez toute erreur indiquant qu'un dépôt n'a pas pu être atteint.

**4. Exemple de log :**

Si un projet Java échoue avec `Could not find artifact`, il s'agit probablement d'une dépendance manquante ou inaccessible. Vérifiez l'URL du dépôt ou si l'artefact existe dans votre dépôt Maven.

**5. Résoudre les conflits de versions** :

Les conflits de versions surviennent lorsque différentes dépendances nécessitent des versions incompatibles de la même bibliothèque. C'est particulièrement vrai dans les projets Java (avec Maven/Gradle) et .NET. Envisagez d'utiliser des outils pour résoudre les conflits de versions automatiquement ou définissez manuellement des versions compatibles.

### Corriger les tests instables basés sur les données historiques des logs

**Note :** Les problèmes tels que les crashs de conteneurs, les logs non ingérés ou les contraintes de ressources ici peuvent ressembler à ceux d'autres sections. Ils sont courants à travers les services et processus CI/CD, mais chaque section offre un contexte unique pour éviter la redondance.

Les tests instables (flaky tests) – c'est-à-dire ceux qui réussissent parfois et échouent d'autres fois – sont courants dans les pipelines CI/CD, et ils peuvent être frustrants. Discutons de quelques stratégies pour les aborder :

**1. Analyser les logs de tests au fil du temps** :

Examinez les logs historiques pour identifier les schémas de moment où le test échoue. Recherchez des problèmes de timing, des limites de ressources ou des dépendances externes qui pourraient affecter la fiabilité des tests.

Par exemple, si un test échoue par intermittence après un certain temps ou seulement pendant des étapes spécifiques du pipeline, cela pourrait indiquer un épuisement des ressources ou des conditions de concurrence (race conditions).

**2. Vérifier les dépendances des tests** :

Souvent, les tests instables dépendent de services ou de ressources externes (par exemple, bases de données, API, systèmes de fichiers). Vérifiez si ces services sont systématiquement disponibles et correctement simulés (mockés) pendant l'exécution des tests.

Les logs mentionnant des échecs de connexion à des services externes ou des environnements instables peuvent vous donner des indications sur les problèmes potentiels avec les dépendances.

**3. Exécuter les tests avec une journalisation accrue** :

Augmentez la verbosité des logs de tests pour capturer plus d'informations sur les échecs. Cela peut vous aider à détecter pourquoi les tests échouent dans certaines conditions.

Par exemple, l'ajout de logs de débogage à l'intérieur des tests peut fournir plus de contexte sur l'état de l'application lorsque l'échec se produit.

**4. Problèmes liés au moment de la journée** :

Certains tests instables peuvent échouer pendant les heures de pointe, surtout s'ils reposent sur des ressources partagées. Recherchez des schémas qui corrèlent avec la contention des ressources (par exemple, verrous de base de données, limites de débit d'API).

Les logs montrant une utilisation élevée du CPU ou de la mémoire peuvent indiquer que les contraintes de ressources affectent la stabilité de vos tests.

**5. Implémenter une logique de réessai pour les tests instables** :

Pour atténuer les effets des tests instables, implémentez des réessais automatiques pour les tests qui échouent par intermittence. Cela peut aider à réduire le bruit dans votre pipeline CI/CD pendant que vous enquêtez sur les causes racines.

Par exemple, si un test de connexion à une base de données échoue par intermittence, vous voudrez peut-être inspecter les logs de la base de données pour des signes de timeouts ou d'épuisement du pool de connexions.

### Comment résoudre les échecs des pipelines de déploiement

Les échecs des pipelines de déploiement peuvent provenir de plusieurs sources, et les diagnostiquer nécessite une approche systématique utilisant les logs et les outils d'observabilité disponibles. Ci-dessous, nous soulignerons les schémas courants dans les logs qui indiquent des contraintes de ressources, des problèmes de permission/authentification et une dérive de configuration entre les environnements.

**Schémas de logs indiquant des contraintes de ressources**

Les contraintes de ressources sont une cause fréquente d'échec de pipeline. Celles-ci peuvent inclure des limites de CPU, l'utilisation de la mémoire ou le manque d'espace disque. Voici comment reconnaître ces schémas :

#### Indicateurs clés dans les logs :

-   **Problèmes de mémoire** : Recherchez des messages comme *"out of memory"*, *"memory limit exceeded"* ou *"OOM killed"* dans vos logs. Voici un exemple dans les logs Kubernetes :

```
pod has been OOMKilled
```

-   **Limites de CPU** : Surveillez les logs montrant qu'un processus a dépassé les limites de CPU ou a été bridé (throttled). Voici un exemple :

```
process 'foo' hit CPU limit, throttling at 100%
```

-   **Espace disque** : Les logs peuvent montrer des erreurs d'écriture de fichiers ou des messages indiquant qu'un disque est plein. Voici un exemple :

```
Unable to write to file, disk space is full.
```

Vous pouvez résoudre les problèmes de mémoire en augmentant la mémoire allouée à vos conteneurs, VM ou instances cloud.

Vous pouvez résoudre les problèmes de CPU en ajustant les limites de CPU ou en faisant évoluer votre infrastructure pour ajouter plus de ressources.

Et enfin, vous pouvez résoudre les problèmes d'espace disque en nettoyant les fichiers inutilisés ou en augmentant la capacité du disque sur le serveur/conteneur.

**Identifier les problèmes de permission et d'authentification**

Les problèmes de permission et d'authentification entraînent souvent des échecs de pipeline en raison d'un manque d'accès aux ressources ou services nécessaires. Ces problèmes peuvent survenir lorsque vous essayez d'accéder à des bases de données, de déployer vers des services cloud ou de vous authentifier auprès d'API tierces.

Il existe des indicateurs clés dans les logs que vous pouvez surveiller :

#### 1. Échecs d'authentification :

Recherchez des messages liés à des échecs de connexion, des identifiants incorrects ou des jetons (tokens) invalides.

Voici un exemple :

```
Authentication failed for user 'admin'
```

```
Invalid API token provided.
```

#### 2. Permission refusée :

Les logs peuvent indiquer que le pipeline CI/CD manque de permissions pour effectuer une certaine action.

Voici un exemple :

```
Access denied for /path/to/deployment/target
```

```
Unauthorized request to cloud service.
```

**Comment résoudre ces erreurs** :

-   **Identifiants** : Assurez-vous que les identifiants (clés API, jetons d'accès, clés SSH) utilisés dans le pipeline sont à jour et correctement configurés.
    
-   **Permissions** : Examinez et mettez à jour les paramètres de contrôle d'accès basé sur les rôles (RBAC) pour le compte de service exécutant le pipeline afin de vous assurer qu'il dispose des permissions nécessaires.
    
-   **Gestion des secrets** : Utilisez des outils comme Vault, AWS Secrets Manager ou Azure Key Vault pour gérer en toute sécurité les secrets et les identifiants.
    

**Dépannage de la dérive de configuration entre les environnements**

La dérive de configuration se produit lorsque différents environnements (comme le développement, le staging, la production) ne sont pas synchronisés. Cela peut entraîner un comportement incohérent lors des déploiements et aboutit souvent à des échecs dans un environnement mais pas dans les autres.

Surveillez ces indicateurs clés dans les logs :

#### 1. Inadéquation des variables d'environnement :

Si vous utilisez des variables d'environnement, vérifiez les divergences entre les différentes étapes. Par exemple :

```
Environment variable DATABASE_URL not found in production
```

#### 2. Versions des dépendances :

Des versions de dépendances décalées entre les environnements peuvent causer des problèmes inattendus.

Voici un exemple :

```
Error: Dependency 'libxyz' version mismatch between environments
```

#### 3. Configuration du service :

Recherchez des erreurs liées à la configuration qui pourraient ne pas être présentes dans un environnement de développement mais se produisent en production.

Voici un exemple :

```
Error: Invalid config in 'production-config.yaml'
```

**Comment résoudre ces erreurs** :

-   **Utiliser l'Infrastructure as Code (IaC)** : Des outils comme Terraform, Ansible ou CloudFormation peuvent aider à garantir que les environnements sont provisionnés de manière cohérente.
    
-   **Gestion automatisée de la configuration** : Utilisez les étapes du pipeline CI/CD pour automatiser la configuration de l'environnement afin d'éviter les changements manuels qui peuvent causer une dérive.
    
-   **Vérifications de la cohérence de l'environnement** : Implémentez des vérifications pour comparer les configurations et les dépendances entre les environnements avant le déploiement.
    
    -   Exemple : Vous pouvez ajouter une étape de pré-déploiement pour exécuter un script qui compare les variables d'environnement, les configurations et les versions de dépendances entre le staging et la production.
-   **Outils de gestion de configuration** : Utilisez des outils de gestion de configuration comme Chef, Puppet ou SaltStack pour maintenir des configurations cohérentes à travers les environnements.
    

### Comment déboguer les problèmes de déploiement basés sur des conteneurs

Le débogage des problèmes de déploiement basés sur des conteneurs nécessite des outils et des techniques spécialisés pour tracer les erreurs dans les environnements conteneurisés. Voici des stratégies pour collecter efficacement les logs, diagnostiquer les échecs et utiliser des conteneurs éphémères pour l'investigation.

#### Collecter et analyser les logs de conteneurs efficacement

Les logs de conteneurs sont essentiels pour le dépannage, et une collecte et une analyse efficaces peuvent accélérer considérablement le processus de débogage.

Voici comment vous pouvez collecter les logs de conteneurs :

**1. Logs Docker :**

Vous pouvez utiliser la commande `logs` de Docker pour visualiser les logs d'un conteneur spécifique :

```
docker logs <container_name_or_id>
```

Si votre conteneur utilise un driver de journalisation (comme `json-file` ou `fluentd`), assurez-vous que les logs sont écrits dans un emplacement accessible.

**2. Logs Kubernetes :**

Pour les conteneurs gérés par Kubernetes, utilisez `kubectl` pour accéder aux logs des pods :

```
kubectl logs <pod_name>
```

Pour visualiser les logs de tous les conteneurs d'un pod :

```
kubectl logs <pod_name> --all-containers=true
```

**3. Agrégation de logs :**

Vous pouvez intégrer des systèmes de journalisation centralisés (comme **Grafana Loki**, **Elastic Stack**). Vous pouvez également utiliser Fluentd ou Logstash comme agents d'expédition de logs pour transférer les logs des conteneurs vers un backend de journalisation.

#### Analyser les logs :

**1. Filtrer et rechercher dans les logs :**

Utilisez `grep` pour filtrer les logs à la recherche de messages d'erreur ou de schémas spécifiques :

```
docker logs <container_name> | grep "ERROR"
```

Dans Kubernetes, vous pouvez combiner `kubectl` avec `grep` ou d'autres outils pour un filtrage avancé.

**2. Contextualisation des logs :**

Incluez des métadonnées dans vos logs (par exemple, ID du conteneur, environnement, horodatages) pour faciliter le débogage. Assurez-vous que les logs sont structurés dans des formats comme JSON pour permettre de meilleures requêtes et filtrages.

### Comment diagnostiquer les échecs de pull d'image et de réseau

Les échecs de déploiement de conteneurs proviennent souvent de problèmes liés au pull d'images ou à la connectivité réseau. Voici comment dépanner ces problèmes :

#### Échecs de pull d'image :

Il existe des problèmes courants que vous pourriez voir, tels que :

-   **Échecs d'authentification :** Si le registre de conteneurs nécessite une authentification, assurez-vous que vos identifiants (nom d'utilisateur/mot de passe ou jetons) sont corrects.
    
-   **Connectivité réseau :** Vérifiez si le conteneur peut accéder au point de terminaison du registre. Souvent, des pare-feu ou des problèmes de DNS bloquent le pull de l'image.
    
-   **Image non trouvée :** Vérifiez que le nom de l'image et le tag sont corrects. Utilisez `docker pull` pour tirer manuellement l'image afin de voir si le problème est spécifique au processus de déploiement.
    

Il existe plusieurs façons de les diagnostiquer :

Pour **Docker**, utilisez :

```
docker pull <image_name>
```

Cela affichera le message d'erreur spécifique si le pull de l'image échoue.

Pour **Kubernetes**, vérifiez les logs d'événements pour le pod :

```
kubectl describe pod <pod_name>
```

Recherchez le statut `Failed` sous "Events" pour obtenir des informations sur la raison de l'échec du pull de l'image (par exemple, mauvais identifiants ou tag). Si le problème vient de l'authentification au registre, configurez les **imagePullSecrets** de Kubernetes ou les identifiants de Docker pour garantir l'accès correct.

#### Échecs de réseau :

Certains problèmes courants que vous pouvez rencontrer sont :

-   **Problèmes de résolution DNS :** Les conteneurs peuvent échouer à résoudre les noms d'hôtes si les configurations DNS sont incorrectes.
    
-   **Politiques réseau et règles de pare-feu :** Des politiques réseau ou des pare-feu peuvent bloquer les ports nécessaires.
    
-   **Communication entre conteneurs :** Si des conteneurs doivent se parler, assurez-vous qu'ils sont sur le même réseau ou sous-réseau.
    

Encore une fois, il existe plusieurs façons de diagnostiquer ces problèmes :

**Pour le réseau Docker :**

Vous pouvez faire ceci pour voir tous les réseaux Docker :

```
docker network ls
```

Vous pouvez également inspecter le réseau de votre conteneur comme ceci :

```
docker network inspect <network_name>
```

Vérifiez si le conteneur est correctement attaché au réseau et si les ports nécessaires sont exposés.

**Pour le réseau Kubernetes :**

Vous pouvez utiliser `kubectl` pour vérifier les politiques réseau :

```
kubectl get networkpolicies
```

Vous pouvez également vérifier les paramètres réseau du pod comme ceci :

```
kubectl describe pod <pod_name> | grep -i "Network"
```

**Tester la connectivité à l'intérieur des conteneurs :**

Pour Docker, entrez dans le conteneur et testez :

```
docker exec -it <container_id> /bin/bash
ping <hostname_or_ip>
curl http://<service_address>:<port>
```

Dans Kubernetes, utilisez `kubectl exec` pour accéder au pod et tester la connectivité :

```
kubectl exec -it <pod_name> -- /bin/bash
```

### Comment utiliser des conteneurs de débogage éphémères pour l'investigation

Les conteneurs de débogage éphémères sont des conteneurs à courte durée de vie qui aident à investiguer les problèmes dans un environnement en cours d'exécution sans altérer le conteneur d'application principal.

#### Que sont les conteneurs de débogage éphémères ?

Les conteneurs de débogage éphémères vous permettent d'exécuter des commandes de diagnostic (comme l'accès au shell, `ping` ou `curl`) dans le même environnement réseau que le conteneur d'application défaillant, sans modifier l'application elle-même.

#### Comment configurer des conteneurs éphémères dans Docker :

**1. Utiliser la commande** `docker run` :

Vous pouvez créer un nouveau conteneur pour le débogage en lançant un conteneur avec les mêmes paramètres réseau que le conteneur défaillant :

```
docker run -it --network container:<container_name_or_id> --entrypoint /bin/bash <debug_image>
```

Cette commande lance un shell interactif à l'intérieur du conteneur de débogage en utilisant le même réseau que le conteneur cible.

#### Conteneurs éphémères dans Kubernetes :

Kubernetes vous permet d'injecter un conteneur de débogage éphémère dans un pod en cours d'exécution. Vous pouvez ajouter un conteneur de débogage temporaire à votre pod en utilisant la commande suivante :

```
kubectl debug <pod_name> -it --image=<debug_image> --target=<container_name>
```

Cette commande lancera un nouveau conteneur dans le même pod que le conteneur cible, vous permettant d'exécuter des commandes de diagnostic.

Les cas d'utilisation typiques sont l'investigation des systèmes de fichiers, l'exécution de diagnostics réseau, la vérification des fichiers de configuration, etc.

Ces conteneurs de débogage sont destinés à être temporaires et peuvent être supprimés une fois le problème résolu.

## Comment implémenter des techniques de débogage avancées

Cette section couvre des méthodes avancées pour diagnostiquer des problèmes complexes de pipeline CI/CD que l'analyse de logs standard pourrait manquer. Nous explorerons le tracing distribué pour suivre les requêtes à travers plusieurs services et combinerons les traces avec les logs et les métriques pour des informations plus approfondies.

Ces techniques sont conçues pour fonctionner avec des contraintes budgétaires, garantissant un débogage efficace pour vos workflows CI/CD.

### **Choisir un backend de tracing pour la CI/CD**

Le tracing distribué vous permet de surveiller le chemin d'une requête à travers divers services de votre pipeline CI/CD, par exemple d'une étape de build à un déploiement, en identifiant les retards ou les échecs. Choisir un backend de tracing implique de sélectionner un outil pour stocker et analyser ces données de trace. Ci-dessous, nous comparons Jaeger, Tempo et les solutions hébergées pour le tracing distribué.

| **Outil** | **Utilisation des ressources** | **Complexité de configuration** | **Idéal pour** | **Adéquation CI/CD** |
| --- | --- | --- | --- | --- |
| **Jaeger** | Faible | Facile (basé sur Docker) | Petites équipes, configurations locales | Pipelines simples, vues de traces rapides |
| **Tempo** | Faible | Modérée (intégration Grafana) | Utilisateurs Grafana, corrélation logs/métriques | Pipelines complexes, observabilité unifiée |
| **Hébergé (ex: Lightstep)** | Variable (basé sur le cloud) | Facile (géré) | Équipes ayant un budget pour les services cloud | Tracing évolutif de niveau production |

Quand choisir chacun :

-   **Jaeger** : Idéal pour des configurations de tracing locales et rapides avec un minimum de surcharge.
    
-   **Tempo** : Idéal pour les équipes utilisant déjà Grafana Loki/Prometheus pour une observabilité unifiée.
    
-   **Solutions hébergées** : Adaptées aux pipelines à grande échelle nécessitant une évolutivité gérée.
    

### Comment configurer le tracing distribué avec un petit budget

Le tracing distribué est crucial pour déboguer et observer des opérations complexes à plusieurs étapes à travers les services. Il permet de suivre les requêtes alors qu'elles se propagent à travers différents services et composants de votre pipeline. L'implémenter avec un petit budget peut tout de même fournir des informations précieuses.

#### Comment utiliser OpenTelemetry avec des backends gratuits

[OpenTelemetry][26] est un framework open-source qui vous permet de collecter, traiter et exporter des données de télémétrie comme les traces et les métriques. Il supporte plusieurs backends, et nous nous concentrerons sur l'utilisation de backends gratuits et économiques pour le stockage et l'analyse des traces.

**1. Installer l'OpenTelemetry Collector :**

OpenTelemetry fournit un agent (collector) qui collecte les traces et les métriques de votre application et les envoie à un backend.

Pour installer l'OpenTelemetry Collector, téléchargez le binaire pour votre OS ou utilisez Docker pour le déployer :

```
docker pull otel/opentelemetry-collector:latest
```

Ensuite, lancez l'OpenTelemetry Collector dans Docker avec un fichier de configuration :

```
docker run -d --name opentelemetry-collector -p 55680:55680 -p 14250:14250 otel/opentelemetry-collector
```

**2. Configurer OpenTelemetry pour exporter vers des backends gratuits :**

Il existe quelques backends gratuits populaires que vous pouvez utiliser pour le tracing distribué, comme Jaeger et Prometheus + Tempo. Voyons comment utiliser les deux ici.

Nous allons commencer par **Jaeger**, un backend de tracing open-source. Il est hautement évolutif et fonctionne bien avec OpenTelemetry.

Vous pouvez utiliser la version Docker pour un déploiement facile :

```
docker run -d --name jaeger -e COLLECTOR_ZIPKIN_HTTP_PORT=9411 -p 5775:5775 -p 6831:6831/udp -p 6832:6832/udp -p 5778:5778 -p 16686:16686 -p 14250:14250 -p 14268:14268 -p 14250:14250 -p 9431:9431 jaegertracing/all-in-one:1.30
```

Alternativement, vous pouvez utiliser des services hébergés comme **Lightstep**, **AWS X-Ray** ou **Honeycomb** pour les environnements cloud-native.

Voyons maintenant comment utiliser **Prometheus** + **Tempo** pour la corrélation des logs et des métriques.

Tempo est un backend de tracing distribué construit par Grafana qui s'intègre bien avec les autres outils Grafana (Loki et Prometheus).

Vous pouvez installer Tempo en utilisant Docker :

```
docker run -d --name tempo -p 14268:14268 grafana/tempo:latest
```

**3. Instrumenter votre code avec le SDK OpenTelemetry :**

Pour les applications Python/Node.js/Java/Go, vous pouvez installer le SDK OpenTelemetry approprié et commencer le tracing.

Voici un exemple Python :

```
pip install opentelemetry-api opentelemetry-sdk opentelemetry-instrumentation
```

Et un exemple Node.js :

```
npm install @opentelemetry/api @opentelemetry/sdk-node @opentelemetry/instrumentation
```

Et un en Java :

```
<dependency>
    <groupId>io.opentelemetry</groupId>
    <artifactId>opentelemetry-api</artifactId>
    <version>1.0.0</version>
</dependency>
```

Après l'installation, vous pouvez utiliser le SDK OpenTelemetry pour instrumenter l'application et commencer à collecter des traces pour les requêtes HTTP, les requêtes de base de données et d'autres interactions du pipeline.

**4. Envoyer les données au Collector :**

Vous pouvez configurer le SDK pour envoyer les données de trace à votre OpenTelemetry Collector, qui les transmettra ensuite à votre backend (Jaeger, Tempo, etc.). Voici un exemple pour Python :

```
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchExportSpanProcessor

trace.set_tracer_provider(TracerProvider())
exporter = OTLPSpanExporter(endpoint="http://localhost:55680")
processor = BatchExportSpanProcessor(exporter)
trace.get_tracer_provider().add_span_processor(processor)
```

Si les traces n'apparaissent pas, plusieurs problèmes peuvent survenir :

1.  **Le Collector ne démarre pas** : Vérifiez les logs avec `docker logs otel-collector`. Recherchez des erreurs comme “port conflict” ou “invalid config.”
    
    -   Solution : Changez les ports (par exemple, `55681:55680`) ou vérifiez le fichier de configuration.
2.  **Pas de traces dans Jaeger** : Assurez-vous que le collector envoie les données à Jaeger (`http://localhost:14250`). Testez avec `curl http://localhost:55680`.
    
    -   Solution : Mettez à jour le point de terminaison de l'exportateur dans la configuration de votre SDK.
3.  **Contraintes de ressources** : Surveillez l'utilisation avec `docker stats`.
    
    -   Solution : Allouez au moins 2 Go de RAM et 10 Go d'espace disque pour le collector et le backend.

#### Corréler les traces avec les logs et les métriques

Combiner les traces avec les logs et les métriques offre une vue holistique des opérations de votre pipeline, vous permettant d'identifier plus efficacement la cause racine des problèmes.

OpenTelemetry et Grafana vous permettent de lier traces, logs et métriques dans une vue unifiée.

Voyons comment vous pouvez faire cela maintenant.

**1. Lier les logs et les traces en utilisant des IDs de corrélation :**

Lors de la génération de logs, incluez les IDs de trace et de span dans les entrées de logs. Cela vous permet de corréler les logs avec des requêtes de trace spécifiques.

Voici un exemple :

```
{
  "timestamp": "2025-05-10T12:00:00Z",
  "level": "error",
  "message": "Build failure",
  "trace_id": "1234567890abcdef",
  "span_id": "0987654321abcdef"
}
```

**2. Intégrer les logs (Loki) avec les traces (Jaeger/Tempo) dans Grafana :**

Grafana peut intégrer les traces de Jaeger ou Tempo et les corréler avec les logs de Loki.

Pour ce faire :

1.  **Configurez Loki et Tempo dans Grafana.**
    
2.  Dans la vue Explore de Grafana, vous pouvez rechercher les logs et les traces côte à côte.
    
3.  Créez des tableaux de bord qui affichent les métriques, les logs et les traces pour une vue complète du flux d'une requête.
    

**3. Utiliser les métriques Prometheus avec les traces :**

Prometheus fournit des métriques qui peuvent être corrélées avec les traces. Par exemple, vous pouvez utiliser des **exemplaires** dans Prometheus pour lier des données de métriques spécifiques à des données de trace.

**Exemple :** Si vous avez un taux d'erreur élevé dans votre étape de build, vous pouvez corréler cela avec les données de trace pour identifier quelles requêtes ont échoué.

#### Créer des visualisations de traces pour les opérations complexes du pipeline

Vous pouvez visualiser les traces avec Jaeger ou Tempo.

**Pour faire cela dans Jaeger :**

Une fois que vos traces sont dans Jaeger, vous pouvez accéder à l'interface utilisateur de Jaeger ([`http://localhost:16686`][27] par défaut) et utiliser la fonctionnalité de recherche pour explorer les traces basées sur le nom du service, l'ID de trace ou des opérations spécifiques.

Jaeger vous permet de créer des tableaux de bord personnalisés pour visualiser la latence, le débit et les erreurs des requêtes à travers les services.

**Pour faire cela dans Tempo (intégration Grafana) :**

Tempo s'intègre à Grafana, où vous pouvez créer des tableaux de bord qui visualisent les données de trace de votre pipeline.

**Créer un tableau de bord Grafana :**

1.  Ajoutez Tempo comme source de données dans Grafana.
    
2.  Utilisez le panneau "Trace" pour interroger et visualiser les traces.
    
3.  Combinez les visualisations de traces avec les métriques (de Prometheus) et les logs (de Loki) pour obtenir une vue unifiée de votre pipeline.
    

Un tableau de bord de visualisation de trace typique pourrait montrer la durée de chaque étape de votre pipeline (build, test, déploiement) et mettre en évidence les endroits où des retards ou des erreurs se produisent, comme des requêtes de base de données lentes ou des tests instables.

**Dépannage des problèmes d'installation de Tempo**

Si Tempo ne parvient pas à collecter ou à afficher les traces :

1.  **Le conteneur ne démarre pas** : Vérifiez les logs avec `docker logs tempo`. Recherchez des erreurs comme “port already in use” (par exemple, 14268) ou “storage backend unavailable.”
    
    -   Solution : Changez les ports dans la commande Docker (par exemple, `-p 14269:14268`) ou assurez-vous que le répertoire de stockage (par exemple, `/tmp/tempo`) existe et est accessible en écriture.
2.  **Pas de traces dans Tempo** : Vérifiez que l'OpenTelemetry Collector envoie les traces au point de terminaison de Tempo (`http://localhost:14268`). Testez la connectivité avec `curl http://localhost:14268`.
    
    -   Solution : Mettez à jour la configuration de l'exportateur du collector pour pointer vers le bon point de terminaison Tempo, et assurez-vous qu'aucun pare-feu ne bloque la connexion.
3.  **Contraintes de ressources** : Surveillez l'utilisation avec `docker stats` ou `top` sur l'hôte.
    
    -   Solution : Allouez au moins 2 Go de RAM et 10 Go d'espace disque pour Tempo, car les données de tracing peuvent croître rapidement avec des pipelines à haut volume.

![Graphique à barres montrant la latence des traces du pipeline CI/CD pour mai 2025. Trois étapes du pipeline sont affichées : l'étape de Build (barre bleue) montre une latence d'environ 1 200 ms, l'étape de Test (barre jaune) montre une latence d'environ 800 ms, et l'étape de Déploiement (barre rouge) montre une latence d'environ 1 500 ms. L'étape de Déploiement a la latence la plus élevée, suivie du Build, puis du Test.](https://cdn.hashnode.com/res/hashnode/image/upload/v1748226837500/c9865f8c-f737-49a5-a346-a56f4fac37fd.png)

Ce graphique à barres affiche la latence moyenne (en millisecondes) pour les étapes clés d'un pipeline CI/CD en mai 2025. L'étape de Build affiche une moyenne d'environ 1 200 ms (bleu), l'étape de Test environ 800 ms (jaune), et l'étape de Déploiement environ 1 500 ms (rose), soulignant que le déploiement est l'étape la plus chronophage.

## Comment construire des tableaux de bord de débogage complets

Cette section explique comment créer des tableaux de bord Grafana pour dépanner efficacement les problèmes de pipeline CI/CD. Nous nous concentrerons sur la mise en place de visualisations pour les métriques clés, les logs et les ressources système afin d'identifier des problèmes tels que les échecs de build ou les goulots d'étranglement des ressources, en utilisant des outils économiques pour garder votre stack d'observabilité légère et exploitable.

### Concevoir des tableaux de bord Grafana spécifiquement pour le dépannage

#### Étape 1 : Comprendre les métriques et logs clés à surveiller

Lors de la conception d'un tableau de bord Grafana pour le débogage, vous devez vous concentrer sur les métriques et les logs qui aident à identifier les problèmes dans le pipeline. Ceux-ci pourraient inclure :

-   **Échecs de build** : Erreurs pendant les processus de build (compilation, échecs de tests).
    
-   **Échecs de déploiement** : Problèmes lors du déploiement, tels que des tâches échouées, des limitations de ressources ou des mauvaises configurations.
    
-   **Logs de conteneurs** : Informations sur le statut des conteneurs et les logs (si vous utilisez des conteneurs dans votre pipeline).
    
-   **Utilisation des ressources système** : Utilisation du CPU, de la mémoire et du disque pouvant mener à des goulots d'étranglement de performance.
    
-   **Métriques spécifiques au CI/CD** : Nombre d'exécutions de pipeline réussies vs échouées, durée des tâches, temps d'attente des tâches en file d'attente.
    

#### Étape 2 : Configurer les sources de données

Pour commencer à construire le tableau de bord, vous devrez configurer vos sources de données dans Grafana. Tout d'abord, connectez votre instance Prometheus pour collecter les métriques. Pour ce faire, allez dans `Configuration` > `Data Sources` dans Grafana. Ajoutez ensuite `Prometheus` comme source de données et entrez l'URL (par exemple, [`http://localhost:9090`][28]).

Ensuite, vous devez connecter votre instance Loki pour les logs. Allez-y et ajoutez `Loki` comme source de données en spécifiant l'URL (par exemple, [`http://localhost:3100`][29]).

Notez que si vous utilisez d'autres sources comme InfluxDB ou Elasticsearch, vous devrez vous assurer qu'elles sont correctement connectées en tant que sources de données.

#### Étape 3 : Créer des panneaux et des visualisations

Maintenant que vos sources de données sont connectées, vous pouvez commencer à construire votre tableau de bord avec les panneaux suivants :

-   **Panneau de statut de build :**
    
    -   Créez un **panneau de statistiques (stat panel)** ou un **panneau de jauge (gauge panel)** pour montrer le ratio réussite/échec des exécutions de pipeline.
        
    -   Interrogez Prometheus ou Loki pour obtenir des données telles que le statut du build (réussite ou échec), le nombre d'erreurs et la durée des tâches.
        
-   **Panneau de répartition des erreurs :**
    
    -   Utilisez un **graphique en secteurs** pour visualiser les types d'erreurs (par exemple, échecs de build, de déploiement ou de ressources système).
        
    -   Interrogez les logs dans Loki pour répartir les types d'erreurs en fonction de l'outil CI (par exemple, Jenkins, GitHub Actions).
        
-   **Panneau d'utilisation des ressources :**
    
    -   Utilisez des **graphiques de séries temporelles** pour surveiller l'utilisation du CPU, de la mémoire et du disque au fil du temps, en particulier pour les builds ou déploiements gourmands en ressources.
-   **Panneau de durée des tâches :**
    
    -   Utilisez des **graphiques à barres** ou des **graphiques linéaires** pour suivre la durée moyenne des tâches au fil du temps. Définissez des seuils pour les signes d'avertissement si une tâche prend plus de temps que prévu.

#### Dépannage des problèmes de tableau de bord Grafana

Si les tableaux de bord Grafana ne parviennent pas à afficher les données ou montrent des erreurs, vous pourriez avoir l'un de ces problèmes :

1.  **Sources de données manquantes** : Si les métriques, logs ou traces n'apparaissent pas, vérifiez les connexions des sources de données dans Grafana (par exemple, Prometheus, Loki, Tempo). Vérifiez sous Configuration > Data Sources.
    
    -   Solution : Assurez-vous que les URLs des sources de données sont correctes (par exemple, `http://localhost:9090` pour Prometheus) et testez la connexion. Rajoutez la source de données si nécessaire.
2.  **IDs de trace incorrects** : Si les visualisations de traces (par exemple, les panneaux Tempo) n'affichent aucune donnée, confirmez que les IDs de trace dans les logs correspondent à ceux dans Tempo. Utilisez une requête comme `{job="ci_cd"} | json | trace_id="1234567890abcdef"` dans Loki pour vérifier.
    
    -   Solution : Assurez-vous que les logs de votre application incluent les IDs de trace et de span, et vérifiez que le SDK OpenTelemetry est correctement instrumenté pour envoyer les traces à Tempo.
3.  **Contraintes de ressources** : Surveillez l'utilisation des ressources de Grafana avec `docker stats` s'il s'exécute dans un conteneur, ou `top` sur l'hôte.
    
    -   Solution : Allouez au moins 4 Go de RAM et 10 Go d'espace disque pour Grafana, en particulier lors du rendu de tableaux de bord complexes avec plusieurs sources de données.

### Comment configurer des chemins de drill-down des vues de haut niveau aux vues détaillées

#### Étape 1 : Créer un panneau d'aperçu de haut niveau

En haut du tableau de bord, incluez un panneau d'aperçu de haut niveau qui résume le statut global du pipeline. Cela pourrait être :

-   **Nombre de réussites/échecs** : Un simple panneau de statistiques montrant le nombre d'exécutions réussies vs échouées.
    
-   **Statut de santé du pipeline** : Affichez un bilan de santé global de votre pipeline en utilisant des indicateurs colorés (vert pour sain, rouge pour les problèmes).
    

#### Étape 2 : Configurer les liens de drill-down

Pour permettre aux utilisateurs de passer des informations de haut niveau aux vues détaillées :

**1. Lien vers les informations détaillées du build :**

Vous pouvez créer un graphique de séries temporelles qui montre la durée des tâches de build. Ajoutez un lien vers une vue de logs détaillée lors d'un clic sur une tâche échouée.

Par exemple, en cliquant sur un build échoué, vous pouvez lier vers un panneau détaillé ou un tableau de bord séparé qui affiche les logs et les messages d'erreur liés à cette exécution spécifique.

**2. Lien vers les logs dans Loki :**

Vous pouvez utiliser les requêtes **LogQL de Loki** pour configurer un chemin de drill-down. Lorsque les utilisateurs cliquent sur un type d'erreur ou un nom de tâche spécifique, cela devrait automatiquement filtrer les logs pour cette tâche ou ce type d'erreur.

Vous pouvez configurer des interactions de drill-down en utilisant les Dashboard Links dans Grafana. Dans les paramètres du panneau, sous `Links`, spécifiez le lien vers un autre tableau de bord qui affiche les logs détaillés filtrés par le nom de la tâche ou le type d'échec.

#### Étape 3 : Implémenter des filtres de plage temporelle

Pour améliorer la fonctionnalité de drill-down, vous pouvez ajouter un **filtre de plage temporelle** pour permettre aux utilisateurs d'ajuster la fenêtre de temps pour les logs et les métriques. Cela leur permet de zoomer sur un laps de temps spécifique où les échecs se sont produits.

### Comment créer des tableaux de bord partagés pour le dépannage en équipe

#### Étape 1 : Partager votre tableau de bord

Une fois votre tableau de bord conçu, vous pouvez le partager avec votre équipe pour un dépannage collaboratif :

Tout d'abord, vous voudrez vous assurer que les bonnes permissions sont configurées pour votre équipe. Vous pouvez définir des rôles spécifiques dans Grafana avec accès au tableau de bord. Allez dans `Dashboard Settings` > `Permissions`, et accordez un accès en lecture ou en édition aux utilisateurs ou aux équipes.

Ensuite, vous pouvez directement partager un lien vers le tableau de bord avec les membres de votre équipe. Utilisez l'option `Share` dans le coin supérieur droit du tableau de bord, qui fournit une URL directe ainsi que des options pour intégrer le tableau de bord dans d'autres outils (par exemple, Slack, e-mail).

Vous pouvez également utiliser des **variables de template** pour permettre aux utilisateurs de filtrer et d'ajuster le tableau de bord pour différentes exécutions de pipeline ou environnements. Par exemple, ajoutez une variable pour `build_id`, `job_name` ou `branch_name` qui permet aux utilisateurs de sélectionner des builds ou des branches spécifiques pour un dépannage plus granulaire.

#### Étape 2 : Configurer les alertes

Pour s'assurer que votre équipe est informée de tout échec de pipeline, vous pouvez configurer des **règles d'alerte**. Il y en a quelques-unes importantes que vous voudrez mettre en place.

Tout d'abord, créez des alertes pour les problèmes critiques, comme lorsqu'un pipeline échoue ou dépasse l'utilisation des ressources attendue. Cela pourrait concerner des choses comme le temps de build dépassant un seuil ou l'échec d'une étape de déploiement.

Grafana peut envoyer des alertes via divers canaux tels que Slack, e-mail ou webhook.

Vous pouvez également intégrer vos tableaux de bord avec des outils comme Slack ou Teams pour des notifications et une collaboration en temps réel. Configurez des messages automatisés pour votre équipe lorsque le tableau de bord indique un problème.

### **Comment créer des outils de diagnostic automatisés**

#### Building Scripts that Collect Relevant Logs During Failures

Pour automatiser la collecte de logs lors d'échecs, vous avez besoin de scripts capables de capturer les logs des différentes étapes et services CI/CD dès qu'un échec est détecté. Voici les étapes que vous pouvez suivre pour ce faire :

**1. Écrire un script de détection d'échec :**

Vous pouvez exploiter les codes de statut de sortie de vos outils CI/CD pour détecter les échecs. Par exemple, dans GitLab CI/CD ou GitHub Actions, vous pouvez vérifier si la dernière commande a échoué en inspectant `$?` sur les systèmes basés sur Unix.

```
# Example for GitLab CI/CD
if [ $? -ne 0 ]; then
    echo "Failure detected, collecting logs..."
    # Custom log collection script call
    ./collect_logs.sh
fi
```

**2. Script de collecte de logs (collect\_[logs.sh][30]) :**

Le script doit collecter les logs pertinents, les métriques système et les informations de trace. Par exemple :

```
#!/bin/bash
LOG_DIR="/path/to/logs"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="${LOG_DIR}/backup/${TIMESTAMP}"
mkdir -p $BACKUP_DIR

# Collect logs from CI/CD agents, containers, or system logs
cp /var/log/ci_cd/*.log $BACKUP_DIR/
cp /path/to/docker_logs/*.log $BACKUP_DIR/
# Collect metrics or traces from monitoring systems if needed
```

**3. Utiliser les artefacts CI/CD :**

Pour des plateformes comme GitLab, GitHub Actions ou Jenkins, vous pouvez télécharger les logs en tant qu'artefacts pour une investigation ultérieure. Configurez ces plateformes pour sauvegarder les logs en cas d'échec.

Voici un exemple pour GitHub Actions :

```
steps:
  - name: Run Tests
    run: |
      npm run test
  - name: Upload logs if test fails
    if: failure()
    uses: actions/upload-artifact@v2
    with:
      name: test-logs
      path: /path/to/test/logs
```

**4. Journalisation centralisée :**

Au lieu de collecter manuellement les logs, vous pouvez centraliser leur stockage en utilisant des systèmes de journalisation comme Grafana Loki, la stack ELK ou même des solutions basées sur le cloud. Cela garantira que les logs sont accessibles même s'ils sont écrasés ou perdus sur les systèmes individuels.

### Comment implémenter l'analyse automatique des schémas d'erreurs courants

Une fois les logs collectés, vous pouvez automatiser le processus d'analyse en définissant des schémas d'erreurs courants et en les recherchant automatiquement dans vos logs.

#### Étape 1 : Définir les schémas d'erreurs :

Établissez des signatures ou des schémas d'erreurs courants dans votre processus CI/CD, tels que des builds échoués en raison de dépendances manquantes, des problèmes de permission ou des timeouts réseau.

Vous pouvez utiliser des regex ou des expressions régulières pour capturer ces schémas. Voici un exemple – définir une regex pour les schémas d'échec de tests :

```
TEST_FAILURE_REGEX=".*FAILURE.*"
```

#### Étape 2 : Créer un script d'analyse de logs :

Ensuite, vous pouvez écrire un script qui scanne les logs à la recherche de ces schémas courants. Le script pourrait ensuite catégoriser ou signaler les erreurs.

Voici un exemple utilisant `grep` pour détecter les schémas d'échec :

```
#!/bin/bash
LOG_DIR="/path/to/logs"
ERROR_LOG="${LOG_DIR}/error_patterns.log"
touch $ERROR_LOG

# Define error patterns to search for
ERROR_PATTERNS=("FAILURE" "ERROR" "TIMEOUT")

for PATTERN in "${ERROR_PATTERNS[@]}"; do
    grep -i $PATTERN $LOG_DIR/*.log >> $ERROR_LOG
done

if [ -s $ERROR_LOG ]; then
    echo "Error patterns found, review the log file."
fi
```

#### Étape 3 : Automatiser l'alerte :

Une fois qu'un schéma d'erreur est détecté, vous pouvez intégrer le script d'analyse de logs à votre système d'alerte (par exemple, en envoyant un e-mail ou une notification Slack).

Voici un exemple d'envoi d'une notification Slack :

```
if [ -s $ERROR_LOG ]; then
    curl -X POST -H 'Content-type: application/json' \
         --data '{"text":"Error detected in CI pipeline. Check error log."}' \
         https://hooks.slack.com/services/YOUR_SLACK_WEBHOOK_URL
fi
```

#### Étape 4 : Utiliser des outils d'observabilité pour la reconnaissance de schémas :

Tirez parti des outils d'observabilité (Grafana Loki, Prometheus) qui supportent les requêtes de logs et la visualisation. Vous pouvez créer des tableaux de bord qui détectent automatiquement les anomalies comme les taux d'échec élevés ou les erreurs récurrentes.

Exemple : Configurez un tableau de bord Grafana avec des règles d'alerte basées sur la fréquence des logs.

### Comment créer des pipelines auto-réparateurs basés sur des problèmes connus

Les pipelines auto-réparateurs peuvent traiter automatiquement les problèmes lorsqu'ils sont détectés en exécutant des actions correctives prédéfinies. Voyons comment vous pouvez en mettre un en place.

#### Étape 1 : Définir les échecs courants et les solutions :

Identifiez les problèmes récurrents (par exemple, problèmes de dépendances, timeouts de build, tests instables) qui surviennent dans votre pipeline. Ensuite, définissez des actions d'auto-réparation pour atténuer ces problèmes.

Voici un exemple de réessai automatique d'une étape échouée s'il s'agit d'un test instable connu :

```
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Run Tests
        run: |
          npm run test
      - name: Retry Tests if Failed
        if: failure() && (steps.tests.outcome == 'failure')
        run: |
          echo "Retrying tests..."
          npm run test
```

#### Étape 2 : Rollbacks automatiques :

Mettez en place un processus de rollback pour les déploiements échoués. Par exemple, si un déploiement en production échoue, le pipeline peut automatiquement revenir au dernier build réussi.

Exemple dans GitLab CI/CD :

```
deploy_production:
  script:
    - ./deploy.sh
  when: on_failure
  retry: 3
```

#### Étape 3 : Construire une logique d'auto-réparation en utilisant des mécanismes de réessai :

Implémentez une logique de réessai pour les problèmes transitoires (comme les micro-coupures réseau) qui causent souvent des échecs.

Exemple de réessai d'une étape dans GitHub Actions :

```
steps:
  - name: Retry Deployment
    run: |
      attempts=0
      max_attempts=3
      until [ $attempts -ge $max_attempts ]
      do
        deploy_script && break
        attempts=$((attempts+1))
        echo "Attempt $attempts failed. Retrying..."
        sleep 5
      done
```

#### Étape 4 : Automatiser les actions correctives pour les problèmes de dépendances :

Configurez des correctifs automatiques pour les échecs liés aux dépendances, comme le nettoyage des caches ou la réinstallation des dépendances :

```
if [[ $(cat error.log) =~ "dependency not found" ]]; then
    echo "Dependency issue detected, reinstalling dependencies..."
    npm install
fi
```

#### Étape 5 : Intégrer avec des services d'auto-réparation :

Pour une auto-réparation plus complexe, vous pouvez intégrer des outils comme Ansible, Puppet, ou même créer des scripts personnalisés qui corrigent automatiquement les problèmes de configuration courants.

## Comment mener des post-mortems efficaces en utilisant les logs

Les logs sont souvent la ressource la plus précieuse pour reconstruire ce qui s'est mal passé dans un pipeline CI/CD. Mener des post-mortems efficaces avec les données de logs permet aux équipes d'extraire des chronologies claires, d'identifier les causes racines et de définir des étapes pour prévenir la récurrence – le tout basé sur des preuves concrètes.

### Extraire la chronologie et les événements clés des logs

Pour comprendre précisément ce qui s'est passé et quand, à partir des informations contenues dans vos logs, vous pouvez suivre un processus simple.

#### Étape 1 : Centraliser et structurer les logs :

Tout d'abord, assurez-vous que les logs de toutes les étapes du pipeline (build, test, déploiement) sont agrégés dans un endroit central comme Grafana Loki, ELK ou OpenSearch.

Et vous voudrez utiliser un format de log cohérent (comme le JSON structuré) qui inclut des horodatages, des niveaux de log, des identifiants d'étape de pipeline et des IDs de corrélation/requête.

#### Étape 2 : Construire une vue chronologique :

Vous pouvez utiliser des filtres d'horodatage dans l'interface de vos logs (par exemple, Kibana, Grafana Explore) pour isoler les logs de la période de l'incident.

Recherchez les événements clés du cycle de vie, tels que :

-   Début et fin des étapes du pipeline.
    
-   Changements de statut (par exemple, "test failed", "deployment started", "build queued").
    
-   Messages d'erreur et avertissements.
    
-   Événements de réessai ou redémarrages inattendus.
    

#### Étape 3 : Extraire les logs par programmation (optionnel) :

Utilisez des requêtes (LogQL, Elasticsearch DSL) pour exporter les logs pertinents pour l'analyse ou l'inclusion dans un document de post-mortem.

### Comment identifier les causes racines via l'analyse de logs

Pour aller au-delà des symptômes et trouver le véritable problème, vous pouvez prendre plusieurs mesures.

Commencez par **rechercher le premier échec**. Vous pouvez filtrer les logs par `level=error` ou utiliser la reconnaissance de schémas de logs pour identifier le *tout premier* signe de défaillance. Ensuite, remontez en arrière à partir de l'échec en utilisant les IDs de corrélation ou les identifiants d'étape du pipeline.

Deuxièmement, assurez-vous de **corréler les logs à travers les systèmes.** Faites correspondre les logs entre les outils CI/CD (par exemple, GitHub Actions → Logs Docker → Logs Kubernetes). Vous pouvez utiliser des IDs de corrélation partagés ou des IDs de tâches pour regrouper les logs d'événements liés.

Ensuite, **prêtez attention aux signaux intermittents.** Les avertissements, les réessais ou les performances dégradées précédant l'échec peuvent révéler des problèmes liés à l'environnement ou à la configuration.

Et enfin, **vérifiez les dépendances externes.** Recherchez des erreurs de timeout ou de connexion impliquant des services tiers, des API cloud ou des composants d'infrastructure internes.

### **How to Create Actionable Follow-Ups to Prevent Recurrence**

Il existe diverses choses que vous pouvez faire pour transformer vos conclusions en améliorations de processus significatives.

**1. Documenter les conclusions clairement :**

Créez un document de post-mortem structuré qui inclut :

-   Une chronologie des événements avec des extraits de logs.
    
-   Le déclencheur immédiat et la cause racine (basés sur les logs).
    
-   Un résumé de l'impact et des composants affectés.
    
-   Des captures d'écran ou des requêtes de logs sauvegardées pour référence.
    

**2. Définir des actions préventives :**

Les exemples incluent :

-   Ajouter des alertes manquantes ou des moniteurs basés sur les logs.
    
-   Améliorer la verbosité des logs ou ajouter des métadonnées manquantes.
    
-   Corriger les cas de tests fragiles ou les scripts de déploiement.
    
-   Mettre à jour les limites d'infrastructure ou les stratégies de réessai.
    

**3. Assigner la responsabilité et des échéances :**

Chaque élément d'action doit avoir un responsable et une date d'échéance. Si applicable, créez des tests automatisés ou des garde-fous pour attraper des problèmes similaires à l'avenir.

**4. Mettre à jour les runbooks et les guides d'incident :**

Ajoutez les schémas de logs, des exemples de requêtes et les résolutions à la documentation partagée. Cela garantit que la prochaine personne confrontée à un problème similaire pourra agir plus rapidement.

**Conseil de pro :** Automatisez une partie de votre processus de post-mortem en étiquetant les logs des exécutions CI échouées, en les exportant vers un emplacement partagé et en pré-générant des tableaux de bord ou des rapports d'incident. Cela réduit l'effort manuel et augmente la cohérence.

## **How to Optimize Log Storage and Management**

À mesure que votre système CI/CD grandit, les logs peuvent devenir massifs, consommant du stockage et impactant les performances. Optimiser le stockage des logs vous aide à vous assurer que vous conservez ce qui est précieux tout en restant efficace.

### Comment implémenter des politiques de rotation et de rétention des logs

Sans rotation ni rétention, les logs s'accumuleront sans fin, menant à l'épuisement de l'espace disque et à de mauvaises performances. Vous pouvez aider à prévenir cela avec la **rotation des logs**.

La rotation des logs consiste à créer de nouveaux fichiers de logs après un seuil de taille ou de temps et à archiver ou supprimer les anciens.

**Outil logrotate sous Linux** – Configurez `/etc/logrotate.d/<votre-app>` :

```
/var/log/ci_cd/*.log {
    daily
    rotate 7
    compress
    missingok
    notifempty
    create 0640 root adm
}
```

Cet exemple :

-   Effectue une rotation quotidienne.
    
-   Conserve 7 jours de logs.
    
-   Compresse les anciens logs pour gagner de l'espace.
    

**Rotation des logs Docker** – dans `daemon.json` :

```
{
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "50m",
    "max-file": "5"
  }
}
```

Les politiques de rétention garantissent que les anciens logs sont automatiquement supprimés en fonction de leur âge ou de l'utilisation du stockage.

Vous pouvez en configurer une dans Loki comme ceci :

```
table_manager:
  retention_deletes_enabled: true
  retention_period: 168h  # 7 days
```

Ou dans Elasticsearch, utilisez l'Index Lifecycle Management (ILM) :

```
{
  "policy": {
    "phases": {
      "hot": {
        "actions": {
          "rollover": { "max_age": "3d", "max_size": "1gb" }
        }
      },
      "delete": {
        "min_age": "7d",
        "actions": { "delete": {} }
      }
    }
  }
}
```

### Comment configurer la compaction des logs pour le stockage à long terme

La compaction réduit la redondance et ne conserve que les informations de logs critiques, ce qui est idéal pour les audits à long terme ou les analyses.

#### Techniques de compaction :

Il existe diverses techniques de compaction que vous pouvez essayer. En voici quelques-unes :

**1. Loki (mode boltdb-shipper)** :

-   Utilise la compaction pour fusionner les morceaux (chunks) de logs et réduire le stockage.
    
-   Configurez dans `loki-config.yaml` :
    
    ```
      schema_config:
        configs:
          - from: 2023-01-01
            store: boltdb-shipper
            object_store: filesystem
            schema: v11
    ```
    
-   Utilisez une stratégie de faible rétention et de haute compaction pour les logs archivés.
    

**2. Elasticsearch** :

-   Utilisez les **rollup jobs** pour réduire la résolution des anciennes données.
    
-   Stocke des logs résumés, par exemple, des décomptes horaires d'événements similaires.
    

**3. Archiver vers un stockage moins coûteux** :

-   Déplacez les logs consultés peu fréquemment vers S3 ou Azure Blob Storage en utilisant des règles de cycle de vie.

### Comment équilibrer l'observabilité avec les contraintes de ressources

Plus de logs = plus d'observabilité, mais aussi plus de coûts et de surcharge. Cela signifie que vous avez besoin d'un équilibre. Voici diverses stratégies qui peuvent vous aider à atteindre cet équilibre :

1.  **Journaliser aux niveaux appropriés** :
    
    -   Évitez les logs excessifs de type `debug` ou `trace` en production.
        
    -   Utilisez les niveaux `info` et `warn` avec discernement.
        
    -   Utilisez uniquement `error` ou `critical` pour les échecs nécessitant une action.
        
2.  **Échantillonner les logs** :
    
    -   Si des pipelines à haut volume génèrent des logs répétitifs, activez l'échantillonnage de logs pour réduire les doublons.
        
    -   Des outils comme Vector ou Fluent Bit supportent l'échantillonnage.
        
3.  **Filtrer le bruit** :
    
    -   Utilisez des filtres de logs pour exclure les logs non critiques avant qu'ils n'atteignent le système central.
4.  **Séparer les logs "chauds" vs "froids"** :
    
    -   **Logs chauds** : données récentes en temps réel pour le débogage actif.
        
    -   **Logs froids** : archivés pour la conformité, stockés avec une priorité de performance/stockage plus faible.
        
5.  **Tout compresser** :
    
    -   Utilisez la compression gzip/zstd pour les logs stockés et transmis.
        
    -   Loki, Elasticsearch et Vector supportent la compression nativement.
        

## **Conclusion**

En conclusion, vous avez construit une couche d'observabilité full-stack spécifiquement optimisée pour les pipelines CI/CD sans grever votre budget d'infrastructure. Vous disposez désormais des outils et du savoir-faire pour :

-   Déployer Grafana Loki ou une alternative ELK légère pour capturer des logs structurés de toutes les parties de votre pipeline.
    
-   Unifier et enrichir les logs à travers les outils CI/CD (par exemple, GitHub Actions, Jenkins, GitLab) en utilisant des formats cohérents et des IDs de corrélation.
    
-   Utiliser des requêtes de logs puissantes (LogQL, Kibana Query Language) pour diagnostiquer les échecs de build, les tests instables et les problèmes de déploiement avec précision.
    
-   Corréler les logs avec les métriques et les traces pour obtenir une visibilité contextuelle profonde sur le comportement du pipeline.
    
-   Concevoir des tableaux de bord de débogage réutilisables et une automatisation qui transforme les logs bruts en informations et en actions.
    
-   Construire une culture de partage des connaissances de dépannage via des post-mortems, des runbooks et des rétrospectives basées sur les logs.
    

Pour voir la couche d'observabilité full-stack en action, consultez le code complet et les configurations dans mon dépôt GitHub : [github.com/Emidowojo/CICDObservability][31]. Ce dépôt inclut toutes les configurations pour Grafana Loki, OpenTelemetry, Prometheus, et plus encore, afin que vous puissiez déployer et explorer l'intégralité de la stack d'observabilité du pipeline.

### Prochaines étapes pour l'implémentation d'une observabilité avancée

Voici comment vous pouvez pousser votre configuration encore plus loin :

1.  **Intégrer pleinement le tracing distribué** : Déployez des agents OpenTelemetry à travers vos étapes de build et de déploiement. Cela vous aidera à visualiser comment le code, les builds et les déploiements circulent à travers les systèmes en temps réel.
    
2.  **Automatiser les scripts de diagnostic et les alertes** : Construisez des scripts pour collecter automatiquement les logs et les métriques en cas d'échec, et déclenchez des alertes lorsque des schémas connus se reproduisent. Cela permet une détection plus rapide et même des pipelines auto-réparateurs.
    
3.  **Faire évoluer et renforcer votre infrastructure de logs** : À mesure que l'utilisation augmente, implémentez des politiques de rétention, de compaction et de stockage des logs. Explorez des backends évolutifs comme ClickHouse ou le stockage objet (ex: S3) pour l'archivage à long terme.
    
4.  **Former votre équipe aux meilleures pratiques d'observabilité** : Partagez les tableaux de bord, créez des documents d'accueil et planifiez des sessions d'analyse de logs pour familiariser l'équipe avec vos outils et pratiques.
    

### 📚 Ressources pour continuer à apprendre

**Docs officielles et outils :**

-   [Documentation Grafana Loki][32]
    
-   [Guide de configuration Promtail][33]
    
-   [OpenTelemetry][34]
    
-   [Syntaxe LogQL][35]
    
-   [Kibana Query Language][36]
    
-   [Vector (transfert de logs)][37]
    

**Communautés :**

-   [r/devops sur Reddit][38]
    
-   [CNCF Slack – canal #observability][39]
    
-   [Meilleures pratiques de gestion de logs sur Stack Overflow][40]
    

En investissant dans l'observabilité tôt et de manière réfléchie, vous réduisez non seulement le temps de détection et de résolution des problèmes, mais vous construisez également un processus de livraison plus résilient, prévisible et transparent pour toute votre équipe d'ingénierie.

J'espère que cela vous sera utile un jour. Si vous êtes arrivé à la fin de ce guide, merci de m'avoir lu ! Vous pouvez me contacter sur [LinkedIn][41] ou sur X [@Emidowojo][42] si vous souhaitez rester en contact.

[1]: #heading-prerequis
[2]: #heading-pourquoi-lobservabilite-est-importante
[3]: #heading-comment-installer-et-configurer-grafana-loki-sur-une-infrastructure-a-petit-budget
[4]: #heading-comment-implementer-une-alternative-a-la-stack-elk-pour-lobservabilite-des-pipelines
[5]: #heading-comment-creer-une-strategie-de-journalisation-unifiee-a-travers-les-composants-du-pipeline
[6]: #heading-comment-interroger-et-analyser-les-logs-pour-un-depannage-efficace
[7]: #heading-comment-configurer-les-metriques-prometheus-aux-cotes-de-vos-logs
[8]: #heading-comment-creer-des-tableaux-de-bord-grafana-combinant-metriques-et-logs
[9]: #heading-comment-utiliser-les-exemplaires-pour-passer-des-metriques-aux-logs-pertinents
[10]: #heading-comment-diagnostiquer-et-corriger-les-problemes-cicd-courants
[11]: #heading-comment-implementer-des-techniques-de-debogage-avancees
[12]: #heading-comment-mener-des-post-mortems-efficaces-en-utilisant-les-logs
[13]: #heading-comment-optimiser-le-stockage-et-la-gestion-des-logs
[14]: #heading-conclusion
[15]: https://www.freecodecamp.org/news/what-is-ci-cd/
[16]: https://www.freecodecamp.org/news/helpful-linux-commands-you-should-know/
[17]: https://www.freecodecamp.org/news/the-docker-handbook/
[18]: https://www.freecodecamp.org/news/observability-in-cloud-native-applications/
[19]: https://fluentbit.io/
[20]: https://vector.dev/
[21]: https://www.elastic.co/beats/filebeat
[22]: http://localhost:5601/
[23]: http://Draw.io
[24]: https://plugins.jenkins.io/prometheus/
[25]: https://github.com/prometheus/prometheus
[26]: https://www.freecodecamp.org/news/how-to-use-opentelementry-to-trace-node-js-applications/
[27]: http://localhost:16686
[28]: http://localhost:9090
[29]: http://localhost:3100
[30]: http://logs.sh
[31]: https://github.com/Emidowojo/CICDObservability.git
[32]: https://grafana.com/docs/loki/
[33]: https://grafana.com/docs/loki/latest/clients/promtail/
[34]: https://opentelemetry.io/docs/
[35]: https://grafana.com/docs/loki/latest/logql/
[36]: https://www.elastic.co/guide/en/kibana/current/kuery-query.html
[37]: https://vector.dev/docs/
[38]: https://www.reddit.com/r/devops/
[39]: https://slack.cncf.io/
[40]: https://stackoverflow.com/questions/tagged/logging
[41]: https://www.linkedin.com/in/emidowojo/
[42]: https://x.com/Emidowojo