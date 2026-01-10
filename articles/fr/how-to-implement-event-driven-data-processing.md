---
title: Comment implémenter le traitement de données piloté par événements avec Traefik,
  Kafka et Docker
subtitle: ''
author: Abraham Dahunsi
co_authors: []
series: null
date: '2024-11-19T11:47:15.557Z'
originalURL: https://freecodecamp.org/news/how-to-implement-event-driven-data-processing
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1731772751529/58ee1304-a5d9-4be4-a709-1026de99ab3e.png
tags:
- name: Docker
  slug: docker
- name: Microservices
  slug: microservices
- name: containers
  slug: containers
seo_title: Comment implémenter le traitement de données piloté par événements avec
  Traefik, Kafka et Docker
seo_desc: In modern system design, Event-Driven Architecture (EDA) focuses on creating,
  detecting, using, and responding to events within a system. Events are significant
  occurrences that can affect a system’s hardware or software, such as user actions,
  state ...
---

Dans la conception des systèmes modernes, l'[Architecture Pilotée par Événements](https://en.wikipedia.org/wiki/Event-driven_programming) (EDA) se concentre sur la création, la détection, l'utilisation et la réponse aux événements au sein d'un système. Les événements sont des occurrences significatives qui peuvent affecter le matériel ou le logiciel d'un système, telles que les actions des utilisateurs, les changements d'état ou les mises à jour de données.

L'EDA permet à différentes parties d'une application d'interagir de manière découplée, leur permettant de communiquer via des événements plutôt que par des appels directs. Cette configuration permet aux composants de fonctionner indépendamment, de répondre aux événements de manière asynchrone et de s'adapter aux besoins commerciaux changeants sans nécessiter une reconfiguration majeure du système, favorisant ainsi l'agilité.

Les nouvelles applications et les [applications modernes reposent désormais fortement sur le traitement de données en temps réel et la réactivité](https://en.wikipedia.org/wiki/Event-driven_architecture). L'importance de l'EDA ne peut être surestimée car elle fournit le cadre qui soutient ces exigences. En utilisant la communication asynchrone et les interactions pilotées par événements, les systèmes peuvent gérer efficacement de grands volumes de transactions et maintenir des performances sous des charges instables. Ces caractéristiques sont particulièrement appréciées dans les environnements où les changements sont très spontanés, comme les plateformes de commerce électronique ou les applications IoT.

Certains composants clés de l'EDA incluent :

* **Sources d'événements** : Ce sont les producteurs qui génèrent des événements lorsque des actions significatives se produisent au sein du système. Des exemples incluent les interactions des utilisateurs ou les changements de données.

* **Écouteurs** : Ce sont des entités qui s'abonnent à des événements spécifiques et répondent lorsque ces événements se produisent. Les écouteurs permettent au système de réagir dynamiquement aux changements.

* **Gestionnaires** : Ceux-ci sont responsables du traitement des événements une fois qu'ils sont détectés par les écouteurs, exécutant la logique métier nécessaire ou les flux de travail déclenchés par l'événement.

Dans cet article, vous apprendrez comment implémenter le traitement de données piloté par événements en utilisant Traefik, Kafka et Docker.

Voici une [application simple hébergée sur GitHub](https://github.com/Abraham12611/EventMesh) que vous pouvez exécuter rapidement pour avoir un aperçu de ce que vous allez construire aujourd'hui.

## Table des matières

Voici ce que nous allons couvrir :

* [Table des matières](#heading-table-des-matieres)

* [Prérequis](#heading-prerequis)

* [Comprendre les technologies](#heading-comprendre-les-technologies)

* [Comment installer l'environnement](#heading-comment-installer-lenvironnement)

* [Comment construire le système piloté par événements](#heading-comment-construire-le-systeme-pilote-par-evenements)

* [Comment intégrer Traefik avec Kafka](#heading-comment-integrer-traefik-avec-kafka)

* [Tester la configuration](#heading-tester-la-configuration)

* [Conclusion](#heading-conclusion)

Commençons !

## Prérequis

Avant de commencer :

* Déployez une instance Ubuntu 24.04 avec au moins 4 Go de RAM et un minimum de 20 Go d'espace disque libre pour accueillir les images Docker, les conteneurs et les données Kafka.

* Accédez à l'instance avec un utilisateur non-root disposant de privilèges sudo.

* Mettez à jour l'index des paquets.

```bash
sudo apt update
```

## Comprendre les technologies

### Apache Kafka

Apache Kafka est une plateforme de diffusion d'événements distribuée conçue pour les pipelines de données à haut débit et les applications de streaming en temps réel. Il sert de colonne vertébrale pour la mise en œuvre de l'EDA en gérant efficacement de grands volumes d'événements. Kafka utilise un modèle de publication-abonnement où les producteurs envoient des événements à des sujets, et les consommateurs s'abonnent à ces sujets pour recevoir les événements.

Certaines des principales caractéristiques de Kafka incluent :

* **Haut débit** : Kafka est capable de gérer des millions d'événements par seconde avec une faible latence, ce qui le rend adapté aux applications à haut volume.

* **Tolérance aux pannes** : L'architecture distribuée de Kafka garantit la durabilité et la disponibilité des données même en cas de défaillance des serveurs. Il réplique les données sur plusieurs brokers au sein d'un cluster.

* **Évolutivité** : Kafka peut facilement s'étendre horizontalement en ajoutant plus de brokers au cluster ou de partitions aux sujets, répondant ainsi aux besoins croissants en données sans nécessiter une reconfiguration majeure.

### Traefik

Traefik est un proxy inverse HTTP moderne et un équilibreur de charge conçu spécifiquement pour les architectures de microservices. Il découvre automatiquement les services en cours d'exécution dans votre infrastructure et achemine le trafic en conséquence. Traefik simplifie la gestion des microservices en fournissant des capacités de routage dynamique basées sur les métadonnées des services.

Certaines des principales caractéristiques de Traefik incluent :

* Configuration dynamique : Traefik met automatiquement à jour sa configuration de routage à mesure que des services sont ajoutés ou supprimés, éliminant ainsi l'intervention manuelle.

* Équilibrage de charge : Il distribue efficacement les requêtes entrantes sur plusieurs instances de service, améliorant ainsi les performances et la fiabilité.

* Tableau de bord intégré : Traefik fournit un tableau de bord convivial pour surveiller le trafic et la santé des services en temps réel.

En utilisant Kafka et Traefik dans une architecture pilotée par événements, vous pouvez construire des systèmes réactifs qui gèrent efficacement le traitement des données en temps réel tout en maintenant une haute disponibilité et une évolutivité.

## Comment installer l'environnement

### Comment installer Docker sur Ubuntu 24.04

1. Installez les paquets requis.

```bash
sudo apt install ca-certificates curl gnupg lsb-release
```

2. Ajoutez la clé GPG officielle de Docker.

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```

3. Ajoutez le dépôt Docker à vos sources APT.

```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

4. Mettez à jour l'index des paquets à nouveau et installez Docker Engine avec le plugin Docker Compose.

```bash
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```

5. Vérifiez l'installation.

```bash
sudo docker run hello-world
```

Sortie attendue :

```bash
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
c1ec31eb5944: Pull complete
Digest: sha256:305243c734571da2d100c8c8b3c3167a098cab6049c9a5b066b6021a60fcb966
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.
```

### Comment configurer Docker Compose

Docker Compose simplifie la gestion des applications multi-conteneurs, vous permettant de définir et d'exécuter des services dans un seul fichier.

1. Créez un répertoire de projet

```bash
mkdir ~/kafka-traefik-setup && cd ~/kafka-traefik-setup
```

2. Créez un fichier `docker-compose.yml`.

```bash
nano docker-compose.yml
```

3. Ajoutez la configuration suivante au fichier pour définir vos services.

```yaml
version: '3.8'

services:
  kafka:
    image: wurstmeister/kafka:latest
    ports:
      - "9092:9092"
    environment:
      KAFKA_ADVERTISED_LISTENERS: INSIDE://kafka:9092,OUTSIDE://localhost:9092
      KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: INSIDE:PLAINTEXT,OUTSIDE:PLAINTEXT
      KAFKA_LISTENERS: INSIDE://0.0.0.0:9092,OUTSIDE://0.0.0.0:9092
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181

  zookeeper:
    image: wurstmeister/zookeeper:latest
    ports:
      - "2181:2181"

  traefik:
    image: traefik:v2.9
    ports:
      - "80:80"       # Trafic HTTP
      - "8080:8080"   # Tableau de bord Traefik (non sécurisé)
    command:
      - "--api.insecure=true"
      - "--providers.docker=true"
    volumes:
      - "/var/run/docker.sock:/var/run/docker.sock"
```

Enregistrez vos modifications avec `ctrl + o`, puis quittez avec `ctrl + x`.

4. Démarrez vos services.

```bash
docker compose up -d
```

Sortie attendue :

```bash
[+] Running 4/4
 ✔ Network kafka-traefik-setup_default        Created                  0.2s
 ✔ Container kafka-traefik-setup-zookeeper-1  Started                  1.9s
 ✔ Container kafka-traefik-setup-traefik-1    Started                  1.9s
 ✔ Container kafka-traefik-setup-kafka-1      Started                  1.9s
```

## Comment construire le système piloté par événements

### Comment créer des producteurs d'événements

Pour produire des événements dans Kafka, vous devrez implémenter un producteur Kafka. Voici un exemple utilisant Java.

1. Créez un fichier [`kafka-producer.java`](http://kafka-producer.java).

```bash
nano kafka-producer.java
```

2. Ajoutez la configuration suivante pour un producteur Kafka.

```java
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.clients.producer.RecordMetadata;

import java.util.Properties;

public class SimpleProducer {
    public static void main(String[] args) {
        // Configurer les propriétés du producteur
        Properties props = new Properties();
        props.put("bootstrap.servers", "localhost:9092");
        props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");

        // Créer le producteur
        KafkaProducer<String, String> producer = new KafkaProducer<>(props);

        try {
            // Envoyer un message au sujet "my-topic"
            ProducerRecord<String, String> record = new ProducerRecord<>("my-topic", "key1", "Hello, Kafka!");
            RecordMetadata metadata = producer.send(record).get(); // Envoi synchrone
            System.out.printf("Message envoyé avec la clé %s à la partition %d avec l'offset %d%n", 
                              record.key(), metadata.partition(), metadata.offset());
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            // Fermer le producteur
            producer.close();
        }
    }
}
```

Enregistrez vos modifications avec `ctrl + o`, puis quittez avec `ctrl + x`.

Dans la configuration ci-dessus, le producteur envoie un message avec la clé "key1" et la valeur "Hello, Kafka!" au sujet "my-topic".

### Comment configurer les sujets Kafka

Avant de produire ou de consommer des messages, vous devez créer des sujets dans Kafka.

1. Utilisez le script [`kafka-topics.sh`](http://kafka-topics.sh) inclus avec votre installation Kafka pour créer un sujet.

```bash
kafka-topics.sh --bootstrap-server localhost:9092 --create --topic <TopicName> --partitions <NumberOfPartitions> --replication-factor <ReplicationFactor>
```

Par exemple, si vous souhaitez créer un sujet nommé `my-topic` avec 3 partitions et un facteur de réplication de 1, exécutez :

```bash
docker exec <Kafka Container ID> /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --create --topic my-topic --partitions 3 --replication-factor 1
```

Sortie attendue :

```bash
Created topic my-topic.
```

2. Vérifiez si le sujet a été créé avec succès.

```bash
docker exec -it kafka-traefik-setup-kafka-1 /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --list
```

Sortie attendue :

```bash
my-topic
```

### Comment créer des consommateurs d'événements

Après avoir créé vos producteurs et sujets, vous pouvez créer des consommateurs pour lire les messages de ces sujets.

1. Créez un fichier [`kafka-consumer.java`](http://kafka-consumer.java).

```bash
nano kafka-consumer.java
```

2. Ajoutez la configuration suivante pour un consommateur Kafka.

```java
import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.clients.consumer.ConsumerRecord;

import java.time.Duration;
import java.util.Collections;
import java.util.Properties;

public class SimpleConsumer {
    public static void main(String[] args) {
        // Configurer les propriétés du consommateur
        Properties props = new Properties();
        props.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        props.put(ConsumerConfig.GROUP_ID_CONFIG, "my-group");
        props.put(ConsumerConfig.KEY_SERIALIZER_CLASS_CONFIG, "org.apache.kafka.common.serialization.StringDeserializer");
        props.put(ConsumerConfig.VALUE_SERIALIZER_CLASS_CONFIG, "org.apache.kafka.common.serialization.StringDeserializer");

        // Créer le consommateur
        KafkaConsumer<String, String> consumer = new KafkaConsumer<>(props);
        
        // S'abonner au sujet
        consumer.subscribe(Collections.singletonList("my-topic"));

        try {
            while (true) {
                // Interroger pour de nouveaux enregistrements
                ConsumerRecords<String, String> records = consumer.poll(Duration.ofMillis(100));
                for (ConsumerRecord<String, String> record : records) {
                    System.out.printf("Message consommé avec la clé %s et la valeur %s de la partition %d à l'offset %d%n",
                                      record.key(), record.value(), record.partition(), record.offset());
                }
            }
        } finally {
            // Fermer le consommateur
            consumer.close();
        }
    }
}
```

Enregistrez vos modifications avec `ctrl + o`, puis quittez avec `ctrl + x`.

Dans la configuration ci-dessus, le consommateur s'abonne à `my-topic` et interroge en continu pour de nouveaux messages. Lorsque des messages sont reçus, il imprime leurs clés et valeurs ainsi que les informations de partition et d'offset.

## Comment intégrer Traefik avec Kafka

### Configurer Traefik comme proxy inverse.

L'intégration de Traefik comme proxy inverse pour Kafka vous permet de gérer efficacement le trafic entrant tout en fournissant des fonctionnalités telles que le routage dynamique et la terminaison SSL.

1. Mettez à jour le fichier `docker-compose.yml`.

```yaml
version: '3.8'

services:
  kafka:
    image: wurstmeister/kafka:latest
    ports:
      - "9092:9092"
    environment:
      KAFKA_ADVERTISED_LISTENERS: INSIDE://kafka:9092,OUTSIDE://localhost:9092
      KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: INSIDE:PLAINTEXT,OUTSIDE:PLAINTEXT
      KAFKA_LISTENERS: INSIDE://0.0.0.0:9092,OUTSIDE://0.0.0.0:9092
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.kafka.rule=Host(`kafka.example.com`)"
      - "traefik.http.services.kafka.loadbalancer.server.port=9092"

  zookeeper:
    image: wurstmeister/zookeeper:latest
    ports:
      - "2181:2181"

  traefik:
    image: traefik:v2.9
    ports:
      - "80:80"        # Trafic HTTP
      - "8080:8080"    # Tableau de bord Traefik (non sécurisé)
    command:
      - "--api.insecure=true"
      - "--providers.docker=true"
    volumes:
      - "/var/run/docker.sock:/var/run/docker.sock"
```

Dans cette configuration, remplacez [`kafka.example.com`](http://kafka.example.com) par votre nom de domaine réel. Les labels définissent les règles de routage que Traefik utilisera pour diriger le trafic vers le service Kafka.

2. Redémarrez vos services.

```bash
docker compose up -d
```

3. Accédez à votre tableau de bord Traefik en accédant à [`http://localhost:8080`](http://localhost:8080) sur votre navigateur web.

    ![Tableau de bord Traefik sur http://localhost:8080](https://cdn.hashnode.com/res/hashnode/image/upload/v1731753126986/fc124c80-1da2-43eb-9385-426bf6a12756.png align="center")

    ### Équilibrage de charge avec Traefik

    Traefik fournit des capacités d'équilibrage de charge intégrées qui peuvent aider à distribuer les requêtes sur plusieurs instances de vos producteurs et consommateurs Kafka.

    ### Stratégies pour l'équilibrage de charge des microservices pilotés par événements

    1. **Round Robin** :

    Par défaut, Traefik utilise une stratégie de round-robin pour distribuer les requêtes entrantes de manière égale sur toutes les instances disponibles d'un service. Cela est efficace pour équilibrer la charge lorsque plusieurs instances de producteurs ou de consommateurs Kafka sont en cours d'exécution.

    2. **Sessions persistantes** :

    Si vous nécessitez que les requêtes d'un client spécifique aillent toujours à la même instance (par exemple, pour maintenir l'état de la session), vous pouvez configurer des sessions persistantes dans Traefik en utilisant des cookies ou des en-têtes.

    3. **Vérifications de santé** :

    Configurez des vérifications de santé dans Traefik pour vous assurer que le trafic est uniquement acheminé vers les instances saines de vos services Kafka. Vous pouvez le faire en ajoutant des paramètres de vérification de santé dans les définitions de service au sein de votre fichier `docker-compose.yml` :

    ```yaml
    labels:
      - "traefik.http.services.kafka.loadbalancer.healthcheck.path=/health"
      - "traefik.http.services.kafka.loadbalancer.healthcheck.interval=10s"
      - "traefik.http.services.kafka.loadbalancer.healthcheck.timeout=3s"
    ```

    ## Tester la configuration

    ### Vérification de la production et de la consommation d'événements

    1. Kafka fournit des outils en ligne de commande intégrés pour les tests. Démarrez un producteur de console.

    ```bash
    docker exec -it kafka-traefik-setup-kafka-1 /opt/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic my-topic
    ```

    Après avoir exécuté cette commande, vous pouvez taper des messages dans le terminal, qui seront envoyés au sujet Kafka spécifié.

    2. Démarrez une autre session de terminal et lancez un consommateur de console.

    ```bash
    docker exec -it kafka-traefik-setup-kafka-1 /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic my-topic --from-beginning
    ```

    Cette commande affichera tous les messages dans `my-topic`, y compris ceux produits avant que le consommateur ne démarre.

    3. Pour voir comment vos consommateurs suivent les producteurs, vous pouvez exécuter la commande suivante pour vérifier le retard pour un groupe de consommateurs spécifique.

    ```bash
    docker exec -it kafka-traefik-setup-kafka-1 /opt/kafka/bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group <your-consumer-group>
    ```

    ### Surveillance et journalisation

    1. **Métriques Kafka** :

    Kafka expose de nombreuses métriques qui peuvent être surveillées à l'aide de JMX (Java Management Extensions). Vous pouvez configurer JMX pour exporter ces métriques vers des systèmes de surveillance comme Prometheus ou Grafana. Les métriques clés à surveiller incluent :

    * **Débit des messages** : Le taux de messages produits et consommés.

    * **Retard du consommateur** : La différence entre le dernier offset de message produit et le dernier offset de message consommé.

    * **Santé du broker** : Les métriques liées aux performances du broker, telles que les taux de requêtes et les taux d'erreurs.

    2. **Intégration de Prometheus et Grafana** :

    Pour visualiser les métriques Kafka, vous pouvez configurer Prometheus pour scraper les métriques de vos brokers Kafka. Suivez ces étapes :

    * Activez JMX Exporter sur vos brokers Kafka en l'ajoutant comme agent Java dans votre configuration de broker.

    * Configurez Prometheus en ajoutant un travail de scraping dans son fichier de configuration (`prometheus.yml`) qui pointe vers votre endpoint JMX Exporter.

    * Utilisez Grafana pour créer des tableaux de bord qui visualisent ces métriques en temps réel.

    ### Comment implémenter la surveillance pour Traefik

    1. **Endpoint des métriques Traefik**.

    Traefik fournit un support intégré pour l'exportation de métriques via Prometheus. Pour activer cette fonctionnalité, ajoutez la configuration suivante dans votre définition de service Traefik au sein de `docker-compose.yml` :

    ```yaml
    command:
      - "--metrics.prometheus=true"
      - "--metrics.prometheus.addservice=true"
    ```

    2. **Visualisation des métriques Traefik avec Grafana**.

    Une fois que Prometheus scrape les métriques Traefik, vous pouvez les visualiser à l'aide de Grafana :

    * Créez un nouveau tableau de bord dans Grafana et ajoutez des panneaux qui affichent les métriques clés de Traefik telles que :

    * **traefik\_entrypoint\_requests\_total** : Nombre total de requêtes reçues.

    * **traefik\_backend\_request\_duration\_seconds** : Temps de réponse des services backend.

    * **traefik\_service\_requests\_total** : Requêtes totales transférées aux services backend.

    3. **Configuration des alertes**.

    Configurez des alertes dans Prometheus ou Grafana en fonction de seuils spécifiques (par exemple, retard élevé du consommateur ou taux d'erreurs accru).

    ## Conclusion

    Dans ce guide, vous avez implémenté avec succès l'Architecture Pilotée par Événements (EDA) en utilisant Kafka et Traefik dans l'environnement Ubuntu 24.04.

    ### Ressources supplémentaires

    Pour en savoir plus, vous pouvez visiter :

    * La [Documentation officielle d'Apache Kafka](https://kafka.apache.org/documentation/)

    * La [Documentation officielle de Traefik](https://doc.traefik.io/traefik/)

    * La [Documentation officielle de Docker](https://docs.docker.com/)

    * Le guide Vultr pour [configurer Traefik Proxy sur Ubuntu 24.04](https://docs.vultr.com/set-up-traefik-proxy-as-a-reverse-proxy-for-docker-containers-on-ubuntu-24-04)