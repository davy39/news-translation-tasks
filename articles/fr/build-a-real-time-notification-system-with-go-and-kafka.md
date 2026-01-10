---
title: Comment construire un système de notifications en temps réel avec Go et Kafka
date: '2023-08-25T21:41:27.000Z'
authorURL: ''
originalURL: https://freecodecamp.org/news/build-a-real-time-notification-system-with-go-and-kafka
posteditor: ''
proofreader: ''
author: freeCodeCamp
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/Go_Kafka_Vert_Rev2.svg
tags:
- name: Apache Kafka
  slug: apache-kafka
- name: golang
  slug: golang
- name: message broker
  slug: message-broker
seo_desc: 'By Hermann Rösch

  These days, applications need to have instant data access and processing capabilities.
  Whether it''s updating real-time stock trades for financial institutions or navigating
  through live traffic data, the ability to process and react ...'
---


Par Hermann Rösch

<!-- more -->

De nos jours, les applications ont besoin d'un accès aux données et de capacités de traitement instantanés. Qu'il s'agisse de mettre à jour des transactions boursières en temps réel pour des institutions financières ou de naviguer à travers des données de trafic en direct, la capacité à traiter et à réagir aux données en temps réel est cruciale.

Dans ce tutoriel, vous allez explorer les mécanismes de **Kafka**, puis l'intégrer avec **Go** pour développer un système de notifications en temps réel.

Afin de comprendre pleinement cet article, vous devriez avoir des connaissances préalables sur les [**Goroutines**][1], le [**framework**][2] [**Gin**][2] et les outils de conteneurisation comme [**Docker**][3].

## Table des matières

1.  [Qu'est-ce que Kafka ?][4]
2.  [Comment configurer l'espace de travail du projet][5]
3.  [Comment créer les modèles User et Notification][6]
4.  [Comment configurer le Producer Kafka][7]
5.  [Comment configurer le Consumer Kafka][8]
6.  [Testons le système de notifications en temps réel][9]
7.  [Conclusion][10]

## Qu'est-ce que Kafka ? 🤔

[Kafka][11] est une plateforme de streaming d'événements distribuée. Initialement développé par LinkedIn, Kafka a ensuite été confié à la Apache Software Foundation et rendu open-source. Cette transition a marqué son rôle en tant qu'acteur clé du streaming de données en temps réel.

Plus qu'un simple outil de communication, Kafka est un « event broker » — un système qui contrôle et gère les événements ou les messages entre diverses applications ou services. Il peut gérer des volumes d'événements quotidiens massifs en tant que plateforme de streaming d'événements distribuée, garantissant que les données sont transportées et analysées de manière transparente en temps réel.

Outre son rôle fondamental de broker d'événements, Kafka offre des fonctionnalités de durabilité, de scalabilité et de tolérance aux pannes. Il permet également de s'assurer que les flux de données à grande échelle sont gérés de manière efficace et fiable avec une latence très faible.

### Les composants clés de Kafka ⚙️

Maintenant que vous avez fait connaissance avec Kafka, plongeons dans les principaux éléments qui composent son architecture :

#### Événements (Events)

Un événement enregistre le fait que « quelque chose s'est produit ». Il peut être considéré comme un message ou une donnée représentant un changement ou une action. Dans le contexte de notre système de notifications en temps réel, vous pourriez considérer un événement comme suit :

-   Clé de l'événement : `“1”` (représentant l'**ID** de l'utilisateur **Emma**)
-   Valeur de l'événement : `“Bruno a commencé à vous suivre.”`

#### Brokers

Un broker Kafka est un serveur qui exécute le logiciel Kafka et stocke les données. Bien que les configurations de production à grande échelle impliquent souvent plusieurs brokers sur plusieurs machines, vous utiliserez une configuration à broker unique pour ce tutoriel.

#### Topics

Les topics dans Kafka sont similaires aux dossiers dans un système de fichiers. Ils représentent des catégories sous lesquelles les données ou les événements sont stockés. Par exemple, un nom de topic pourrait être `"notifications"`.

#### Producers

Les producers sont des entités qui publient (écrivent) ou envoient des messages à Kafka, comme un programme Go ou un service. Lorsqu'un producer a un événement à envoyer, il choisit un topic auquel adresser l'événement.

#### Consumers

Les consumers lisent et traitent les événements ou les messages de Kafka. Une fois que les producers ont envoyé des messages aux topics, les consumers peuvent s'abonner à un ou plusieurs topics pour recevoir les messages.

#### Partitions

Chaque topic dans Kafka peut être divisé en partitions. Considérez les partitions comme des segments au sein d'un topic qui permettent à Kafka de gérer les données plus efficacement, en particulier dans les configurations avec plusieurs brokers.

Nous nous en tiendrons à une configuration de base sans approfondir les partitions multiples, mais vous devez comprendre leur rôle dans les déploiements Kafka plus importants.

#### Groupes de consumers (Consumer groups)

Alors que les consumers individuels gèrent les messages de partitions spécifiques, les groupes de consumers gèrent la coordination entre plusieurs consumers.

Un groupe de consumers se compose de plusieurs consumers traitant collaborativement des messages de différentes partitions d'un topic. Cela garantit que chaque message d'une partition n'est traité que par un seul consumer du groupe, permettant une consommation efficace et évolutive.

Considérez cela comme une équipe de consumers travaillant ensemble, chaque membre étant responsable des messages de partitions spécifiques, garantissant qu'aucun message n'est oublié.

#### Réplicas (Replicas)

La réplication garantit la sécurité des données. Dans les déploiements Kafka plus importants, le stockage de plusieurs réplicas de données est courant pour aider à la récupération après des défaillances inattendues.

Vous n'utiliserez pas de réplicas dans ce tutoriel, mais il est bénéfique de comprendre leur importance pour assurer la durabilité des données dans Kafka.

#### KRaft

[KRaft][12] est le propre protocole de consensus de Kafka introduit pour éliminer le besoin de [ZooKeeper][13]. En résumé, KRaft gère les métadonnées directement au sein de Kafka, offrant scalabilité, simplicité et une meilleure reprise sur panne, entre autres avantages.

Pour lier tous ces composants ensemble, voici une représentation visuelle de l'architecture de base de Kafka, illustrant un broker, des topics, des partitions et des groupes de consumers :

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Kafka_Architecture_Transparent_V2.png) _Visualisation de l'architecture de streaming d'événements de Kafka_

## Comment configurer l'espace de travail du projet 👨‍💻👩‍💻 {#heading-comment-configurer-l-espace-de-travail-du-projet}

Assez de théorie pour l'instant ! Mettons les mains dans le cambouis avec le projet réel.

En supposant que Docker et Go soient installés sur votre machine, créons un répertoire pour le projet nommé `kafka-notify`. Ensuite, vous allez récupérer [**l'image Docker Kafka de Bitnami**][14] pour la configuration de Kafka, offrant une installation sans tracas :

```
mkdir kafka-notify && cd kafka-notify

curl -sSL \
https://raw.githubusercontent.com/bitnami/containers/main/bitnami/kafka/docker-compose.yml > docker-compose.yml
```

Avant de démarrer le broker Kafka, une légère modification est requise dans le fichier `docker-compose.yml`. Trouvez la chaîne suivante :

```
KAFKA_CFG_ADVERTISED_LISTENERS=PLAINTEXT://:9092
```

Et remplacez-la par :

```
KAFKA_CFG_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092
```

Le changement ci-dessus garantit que Kafka annonce son listener sur `localhost`, ce qui permet à notre application Go locale de se connecter de manière transparente. Maintenant, vous pouvez démarrer le broker Kafka via la commande Docker suivante :

```
docker-compose up -d
```

Ensuite, vous devrez créer quelques répertoires pour organiser les fichiers du projet. Les répertoires `cmd/producer` et `cmd/consumer` contiendront les fichiers principaux de l'application, et le répertoire `pkg/models` stockera les déclarations de modèles :

```
mkdir -p cmd/producer cmd/consumer pkg/models
```

La dernière étape consiste à initialiser les modules Go et à installer les packages externes. Vous utiliserez `sarama` pour établir une connexion avec le broker Kafka et `gin` pour gérer les points de terminaison de l'API pour le système de notifications :

```
go mod init kafka-notify
go get github.com/IBM/sarama github.com/gin-gonic/gin
```

## Comment créer les modèles User et Notification {#heading-comment-creer-les-modeles-user-et-notification}

Une fois l'espace de travail configuré, la première étape consiste à créer les structs `User` et `Notification`. Allez dans le répertoire `pkg/models`, puis créez un nouveau fichier nommé `models.go` et déclarez ces structs à l'intérieur :

```
package models

type User struct {
    ID   int    `json:"id"`
    Name string `json:"name"`
}

type Notification struct {
    From    User   `json:"from"`
    To      User   `json:"to"`
    Message string `json:"message"`
}
```

## Comment configurer le Producer Kafka 📤 {#heading-comment-configurer-le-producer-kafka}

L'étape suivante consiste à écrire le code pour le producer. Vous allez créer une API web Gin simple où un utilisateur peut envoyer une notification à un autre utilisateur via une requête HTTP POST. Cette requête va ensuite « produire » (envoyer) un message vers un topic Kafka nommé `"notifications"`.

Naviguons vers le répertoire `cmd/producer` et créons un nouveau fichier nommé `producer.go`. À l'intérieur, vous allez configurer la logique du producer :

```
package main

import (
    "encoding/json"
    "errors"
    "fmt"
    "log"
    "net/http"
    "strconv"

    "kafka-notify/pkg/models"

    "github.com/IBM/sarama"
    "github.com/gin-gonic/gin"
)

const (
    ProducerPort       = ":8080"
    KafkaServerAddress = "localhost:9092"
    KafkaTopic         = "notifications"
)

// ============== HELPER FUNCTIONS ==============
var ErrUserNotFoundInProducer = errors.New("user not found")

func findUserByID(id int, users []models.User) (models.User, error) {
    for _, user := range users {
        if user.ID == id {
            return user, nil
        }
    }
    return models.User{}, ErrUserNotFoundInProducer
}

func getIDFromRequest(formValue string, ctx *gin.Context) (int, error) {
    id, err := strconv.Atoi(ctx.PostForm(formValue))
    if err != nil {
        return 0, fmt.Errorf(
            "failed to parse ID from form value %s: %w", formValue, err)
    }
    return id, nil
}

// ============== KAFKA RELATED FUNCTIONS ==============
func sendKafkaMessage(producer sarama.SyncProducer,
    users []models.User, ctx *gin.Context, fromID, toID int) error {
    message := ctx.PostForm("message")

    fromUser, err := findUserByID(fromID, users)
    if err != nil {
        return err
    }

    toUser, err := findUserByID(toID, users)
    if err != nil {
        return err
    }

    notification := models.Notification{
        From: fromUser,
        To:   toUser, Message: message,
    }

    notificationJSON, err := json.Marshal(notification)
    if err != nil {
        return fmt.Errorf("failed to marshal notification: %w", err)
    }

    msg := &sarama.ProducerMessage{
        Topic: KafkaTopic,
        Key:   sarama.StringEncoder(strconv.Itoa(toUser.ID)),
        Value: sarama.StringEncoder(notificationJSON),
    }

    _, _, err = producer.SendMessage(msg)
    return err
}

func sendMessageHandler(producer sarama.SyncProducer,
    users []models.User) gin.HandlerFunc {
    return func(ctx *gin.Context) {
        fromID, err := getIDFromRequest("fromID", ctx)
        if err != nil {
            ctx.JSON(http.StatusBadRequest, gin.H{"message": err.Error()})
            return
        }

        toID, err := getIDFromRequest("toID", ctx)
        if err != nil {
            ctx.JSON(http.StatusBadRequest, gin.H{"message": err.Error()})
            return
        }

        err = sendKafkaMessage(producer, users, ctx, fromID, toID)
        if errors.Is(err, ErrUserNotFoundInProducer) {
            ctx.JSON(http.StatusNotFound, gin.H{"message": "User not found"})
            return
        }
        if err != nil {
            ctx.JSON(http.StatusInternalServerError, gin.H{
                "message": err.Error(),
            })
            return
        }

        ctx.JSON(http.StatusOK, gin.H{
            "message": "Notification sent successfully!",
        })
    }
}

func setupProducer() (sarama.SyncProducer, error) {
    config := sarama.NewConfig()
    config.Producer.Return.Successes = true
    producer, err := sarama.NewSyncProducer([]string{KafkaServerAddress},
        config)
    if err != nil {
        return nil, fmt.Errorf("failed to setup producer: %w", err)
    }
    return producer, nil
}

func main() {
    users := []models.User{
        {ID: 1, Name: "Emma"},
        {ID: 2, Name: "Bruno"},
        {ID: 3, Name: "Rick"},
        {ID: 4, Name: "Lena"},
    }

    producer, err := setupProducer()
    if err != nil {
        log.Fatalf("failed to initialize producer: %v", err)
    }
    defer producer.Close()

    gin.SetMode(gin.ReleaseMode)
    router := gin.Default()
    router.POST("/send", sendMessageHandler(producer, users))

    fmt.Printf("Kafka PRODUCER 📨 started at http://localhost%s\n",
        ProducerPort)

    if err := router.Run(ProducerPort); err != nil {
        log.Printf("failed to run the server: %v", err)
    }
}
```

Analysons les composants liés à Kafka au sein de `producer.go` :

Dans la fonction `**setupProducer()**` :

-   `config := sarama.NewConfig()` : Initialise une nouvelle configuration par défaut pour Kafka. Considérez cela comme le réglage des paramètres avant de se connecter au broker.
-   `config.Producer.Return.Successes = true` : Garantit que le producer reçoit un acquittement une fois que le message est stocké avec succès dans le topic `"notifications"`.
-   `producer, err := sarama.NewSyncProducer(…)` : Initialise un producer Kafka synchrone qui se connecte au broker Kafka s'exécutant sur `localhost:9092`.

Dans la fonction `**sendKafkaMessage()**` :

-   Cette fonction commence par récupérer le `message` du contexte, puis tente de trouver à la fois l'expéditeur et le destinataire à l'aide de leurs IDs.
-   `notification := models.Notification{…}` : Initialise une struct `Notification` qui encapsule les informations sur l'expéditeur, le destinataire et le message réel.
-   `msg := &sarama.ProducerMessage{…}` : Construit un `ProducerMessage` pour le topic `"notifications"`, en définissant l'ID du destinataire comme `Key` et le contenu du message, qui est la forme sérialisée de la `Notification`, comme `Value`.
-   `producer.SendMessage(msg)` : Envoie le message construit au topic `"notifications"`.

Dans la fonction `**sendMessageHandler()**` :

-   Cette fonction sert de gestionnaire de point de terminaison (endpoint) pour la requête POST `/send`. Elle traite la requête entrante pour s'assurer que des IDs d'expéditeur et de destinataire valides sont fournis.
-   Après avoir récupéré les IDs, elle invoque la fonction `sendKafkaMessage()` pour envoyer le message Kafka. Selon le résultat, elle envoie les réponses HTTP appropriées : un `404 Not Found` pour les utilisateurs inexistants, un `400 Bad Request` pour les IDs invalides, et un `500 Internal Server Error` pour les autres échecs, accompagnés d'un message d'erreur spécifique.

Enfin, dans la fonction `**main()**` :

-   Vous initialisez un producer Kafka via la fonction `setupProducer()`.
-   Ensuite, vous créez un `router` Gin via `gin.Default()`, configurant un serveur web. Puis, vous définissez un endpoint POST `/send` pour gérer les notifications. Cet endpoint attend les IDs de l'expéditeur et du destinataire ainsi que le contenu du message.
-   La notification est traitée lors de la réception d'une requête POST via la fonction `sendMessageHandler()`, et une réponse HTTP appropriée est envoyée.

Cette configuration offre un moyen simple de simuler des utilisateurs s'envoyant des notifications et montre comment ces notifications sont produites dans le topic `"notifications"`.

## Comment configurer le Consumer Kafka 📥 {#heading-comment-configurer-le-consumer-kafka}

Après avoir créé le producer, l'étape suivante consiste à configurer un consumer qui écoute le topic `"notifications"` et fournit un point de terminaison pour lister les notifications d'un utilisateur spécifique.

Déplaçons-nous vers le répertoire `cmd/consumer` et créons un nouveau fichier nommé `consumer.go`. À l'intérieur, vous allez configurer la logique du consumer et l'API basée sur Gin :

```
package main

import (
    "context"
    "encoding/json"
    "errors"
    "fmt"
    "log"
    "net/http"
    "sync"

    "kafka-notify/pkg/models"

    "github.com/IBM/sarama"
    "github.com/gin-gonic/gin"
)

const (
    ConsumerGroup      = "notifications-group"
    ConsumerTopic      = "notifications"
    ConsumerPort       = ":8081"
    KafkaServerAddress = "localhost:9092"
)

// ============== HELPER FUNCTIONS ==============
var ErrNoMessagesFound = errors.New("no messages found")

func getUserIDFromRequest(ctx *gin.Context) (string, error) {
    userID := ctx.Param("userID")
    if userID == "" {
        return "", ErrNoMessagesFound
    }
    return userID, nil
}

// ====== NOTIFICATION STORAGE ======
type UserNotifications map[string][]models.Notification

type NotificationStore struct {
    data UserNotifications
    mu   sync.RWMutex
}

func (ns *NotificationStore) Add(userID string,
    notification models.Notification) {
    ns.mu.Lock()
    defer ns.mu.Unlock()
    ns.data[userID] = append(ns.data[userID], notification)
}

func (ns *NotificationStore) Get(userID string) []models.Notification {
    ns.mu.RLock()
    defer ns.mu.RUnlock()
    return ns.data[userID]
}

// ============== KAFKA RELATED FUNCTIONS ==============
type Consumer struct {
    store *NotificationStore
}

func (*Consumer) Setup(sarama.ConsumerGroupSession) error   { return nil }
func (*Consumer) Cleanup(sarama.ConsumerGroupSession) error { return nil }

func (consumer *Consumer) ConsumeClaim(
    sess sarama.ConsumerGroupSession, claim sarama.ConsumerGroupClaim) error {
    for msg := range claim.Messages() {
        userID := string(msg.Key)
        var notification models.Notification
        err := json.Unmarshal(msg.Value, &notification)
        if err != nil {
            log.Printf("failed to unmarshal notification: %v", err)
            continue
        }
        consumer.store.Add(userID, notification)
        sess.MarkMessage(msg, "")
    }
    return nil
}

func initializeConsumerGroup() (sarama.ConsumerGroup, error) {
    config := sarama.NewConfig()

    consumerGroup, err := sarama.NewConsumerGroup(
        []string{KafkaServerAddress}, ConsumerGroup, config)
    if err != nil {
        return nil, fmt.Errorf("failed to initialize consumer group: %w", err)
    }

    return consumerGroup, nil
}

func setupConsumerGroup(ctx context.Context, store *NotificationStore) {
    consumerGroup, err := initializeConsumerGroup()
    if err != nil {
        log.Printf("initialization error: %v", err)
    }
    defer consumerGroup.Close()

    consumer := &Consumer{
        store: store,
    }

    for {
        err = consumerGroup.Consume(ctx, []string{ConsumerTopic}, consumer)
        if err != nil {
            log.Printf("error from consumer: %v", err)
        }
        if ctx.Err() != nil {
            return
        }
    }
}

func handleNotifications(ctx *gin.Context, store *NotificationStore) {
    userID, err := getUserIDFromRequest(ctx)
    if err != nil {
        ctx.JSON(http.StatusNotFound, gin.H{"message": err.Error()})
        return
    }

    notes := store.Get(userID)
    if len(notes) == 0 {
        ctx.JSON(http.StatusOK,
            gin.H{
                "message":       "No notifications found for user",
                "notifications": []models.Notification{},
            })
        return
    }

    ctx.JSON(http.StatusOK, gin.H{"notifications": notes})
}

func main() {
    store := &NotificationStore{
        data: make(UserNotifications),
    }

    ctx, cancel := context.WithCancel(context.Background())
    go setupConsumerGroup(ctx, store)
    defer cancel()

    gin.SetMode(gin.ReleaseMode)
    router := gin.Default()
    router.GET("/notifications/:userID", func(ctx *gin.Context) {
        handleNotifications(ctx, store)
    })

    fmt.Printf("Kafka CONSUMER (Group: %s) 👥📥 "+
        "started at http://localhost%s\n", ConsumerGroup, ConsumerPort)

    if err := router.Run(ConsumerPort); err != nil {
        log.Printf("failed to run the server: %v", err)
    }
}
```

Examinons les opérations liées à Kafka au sein de `consumer.go` :

Dans la fonction `**initializeConsumerGroup()**` :

-   `config := sarama.NewConfig()` : Initialise une nouvelle configuration par défaut pour Kafka.
-   `consumerGroup, err := sarama.NewConsumerGroup(…)` : Crée un nouveau groupe de consumers Kafka qui se connecte au broker s'exécutant sur `localhost:9092`. Le nom du groupe est `"notifications-group"`.

À l'intérieur de la struct `**Consumer**` et de ses méthodes :

-   La struct `Consumer` possède un champ `store`, qui est une référence au `NotificationStore` pour garder une trace des notifications reçues.
-   Les méthodes `Setup()` et `Cleanup()` sont requises pour satisfaire l'interface `sarama.ConsumerGroupHandler`. Bien qu'elles ne soient PAS utilisées dans ce tutoriel, elles peuvent jouer des rôles potentiels pour l'initialisation et le nettoyage pendant la consommation de messages, mais agissent ici comme des points de réservation (placeholders).
-   Dans la méthode `ConsumeClaim()` : Le consumer écoute les nouveaux messages sur le topic. Pour chaque message, il récupère le `userID` (la `Key` du message), désérialise (unmarshal) le message dans une struct `Notification`, et ajoute la notification au `NotificationStore`.

Dans la fonction `**setupConsumerGroup()**` :

-   Cette fonction configure le groupe de consumers Kafka, écoute les messages entrants et les traite à l'aide des méthodes de la struct `Consumer`.
-   Elle exécute une boucle `for` indéfiniment, consommant les messages du topic `“notifications”` et traitant toutes les erreurs qui surviennent.

La fonction `**handleNotifications()**` :

-   Initialement, elle tente de récupérer le `userID` de la requête. S'il n'existe pas, elle renvoie un statut `404 Not Found`.
-   Ensuite, elle récupère les notifications pour l'ID utilisateur fourni à partir du `NotificationStore`. Selon que l'utilisateur a des notifications ou non, elle répond avec un statut `200 OK` et soit une tranche (slice) de notifications vide, soit les notifications actuelles.

Enfin, dans la fonction `**main()**` :

-   `store := &NotificationStore{…}` : Crée une instance de `NotificationStore` pour contenir les notifications.
-   `ctx, cancel := context.WithCancel(context.Background())` : Configure un contexte annulable qui peut être utilisé pour arrêter le groupe de consumers.
-   `go setupConsumerGroup(ctx, store)` : Démarre le groupe de consumers dans une Goroutine séparée, lui permettant de fonctionner de manière concurrente sans bloquer le thread principal.
-   La dernière étape consiste à créer un `router` Gin et à définir un endpoint GET `/notifications/:userID` qui récupérera les notifications pour un utilisateur spécifique via la fonction `handleNotifications()` lors de l'accès.

Cette configuration offre un moyen simple de consommer des messages du topic `"notifications"` et de les présenter aux utilisateurs via un point de terminaison web.

## Testons le système de notifications en temps réel👨‍🔬🖥️👩‍🔬 {#heading-testons-le-systeme-de-notifications-en-temps-reel}

Maintenant que le producer et le consumer sont prêts, il est temps de voir le système en action.

### 1. Démarrer le producer

Ouvrez un terminal, déplacez-vous dans le répertoire `kafka-notify`, et lancez le producer avec la commande suivante :

```
go run cmd/producer/producer.go
```

### 2. Démarrer le consumer

Ouvrez une deuxième fenêtre de terminal, naviguez vers le répertoire `kafka-notify`, et démarrez le consumer en exécutant :

```
go run cmd/consumer/consumer.go
```

### 3. Envoi de notifications

Avec le producer et le consumer en cours d'exécution, vous pouvez simuler l'envoi de notifications. Ouvrez un troisième terminal et utilisez les commandes `curl` ci-dessous pour envoyer des notifications :

**L'utilisateur 1 (Emma) reçoit une notification de l'utilisateur 2 (Bruno) :**

```
curl -X POST http://localhost:8080/send \
-d "fromID=2&toID=1&message=Bruno started following you."
```

**L'utilisateur 2 (Bruno) reçoit une notification de l'utilisateur 1 (Emma) :**

```
curl -X POST http://localhost:8080/send \
-d "fromID=1&toID=2&message=Emma mentioned you in a comment: 'Great seeing you yesterday, @Bruno!'"
```

**L'utilisateur 1 (Emma) reçoit une notification de l'utilisateur 4 (Lena) :**

```
curl -X POST http://localhost:8080/send \
-d "fromID=4&toID=1&message=Lena liked your post: 'My weekend getaway!'"
```

### 4. Récupération des notifications

Enfin, vous pouvez récupérer les notifications d'un utilisateur spécifique. Vous pouvez utiliser les commandes `curl` ci-dessous :

**Récupération des notifications pour l'utilisateur 1 (Emma) :**

```
curl http://localhost:8081/notifications/1
```

**Sortie :**

```
{"notifications": [{"from": {"id": 2, "name": "Bruno"}, "to": {"id": 1, "name": "Emma"}, "message": "Bruno started following you."}]}
{"notifications": [{"from": {"id": 4, "name": "Lena"}, "to": {"id": 1, "name": "Emma"}, "message": "Lena liked your post: 'My weekend getaway!'"}]}
```

Dans la sortie ci-dessus, vous voyez une réponse `JSON` listant toutes les notifications pour **Emma**. À mesure que vous envoyez plus de notifications, elles s'accumulent et vous pouvez les récupérer via l'API du consumer.

## Conclusion 📝 {#heading-conclusion}

Dans ce tutoriel, vous avez appris à configurer un système de notifications en temps réel de base en utilisant Kafka avec Go.

En simulant le processus d'envoi et de récupération de notifications par les utilisateurs, vous avez acquis une expérience pratique des composants de Kafka. Il s'agit d'une étape fondamentale pour comprendre comment Kafka peut être intégré dans des applications Go pour diverses tâches de traitement de données en temps réel.

Vous pouvez accéder à l'intégralité du code source de ce projet dans le dépôt GitHub suivant : [https://github.com/gutyoh/kafka-notify][15]

Si vous avez trouvé cet article utile et que vous souhaitez approfondir vos connaissances sur Golang 🐿️, Docker 🐳 et Gin 🍸, n'hésitez pas à consulter le parcours **[Introduction to Go][16]**, qui couvre les concepts de base de Golang.

Les utilisateurs enregistrés peuvent également consulter les parcours **[Go Developer][17]** et **[Introduction to Docker][18]** sur Hyperskill. J'ai été activement impliqué en tant qu'expert dans la création de ces parcours, en veillant à ce qu'ils fournissent un contenu éducatif de premier ordre.

Avant de conclure, je dois un grand merci à mon cher ami **Anton Illarionov**. Son expertise dans l'intégration de Go avec Kafka a inspiré l'idée de cet article. Vous pouvez explorer ses projets sur [GitHub][19].

Faites-moi savoir si vous avez des questions ou des commentaires concernant cet article.

Merci de m'avoir lu, et continuez à coder !

[1]: https://go.dev/tour/concurrency/1#:~:text=A%20goroutine%20is%20a%20lightweight,happens%20in%20the%20new%20goroutine.
[2]: https://gin-gonic.com/docs/introduction/
[3]: https://www.docker.com/
[4]: #heading-qu-est-ce-que-kafka
[5]: #heading-comment-configurer-l-espace-de-travail-du-projet
[6]: #heading-comment-creer-les-modeles-user-et-notification
[7]: #heading-comment-configurer-le-producer-kafka
[8]: #heading-comment-configurer-le-consumer-kafka
[9]: #heading-testons-le-systeme-de-notifications-en-temps-reel
[10]: #heading-conclusion
[11]: https://kafka.apache.org/intro
[12]: https://developer.confluent.io/learn/kraft/
[13]: https://kafka.apache.org/documentation/#zk_depr
[14]: https://hub.docker.com/r/bitnami/kafka/
[15]: https://github.com/gutyoh/kafka-notify
[16]: https://hyperskill.org/tracks/25?category=12&utm_source=fc_hs&utm_medium=social&utm_campaign=hermann
[17]: https://hyperskill.org/tracks/43?category=20&utm_source=fc_hs&utm_medium=social&utm_campaign=hermann
[18]: https://hyperskill.org/tracks/64?category=20&utm_source=fc_hs&utm_medium=social&utm_campaign=hermann
[19]: https://github.com/ant1k9