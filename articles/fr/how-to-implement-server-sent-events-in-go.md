---
title: Comment implémenter les Server-Sent Events en Go
subtitle: ''
author: Alex Pliutau
co_authors: []
series: null
date: '2024-08-28T14:07:51.466Z'
originalURL: https://freecodecamp.org/news/how-to-implement-server-sent-events-in-go
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1724762290560/de9c7afd-2a81-4bd6-aa12-da92a759ebdb.png
tags:
- name: Go Language
  slug: go
- name: APIs
  slug: apis
- name: websockets
  slug: websockets
seo_title: Comment implémenter les Server-Sent Events en Go
seo_desc: 'Server-Sent Events (SSE) is a powerful technology that enables real-time,
  unidirectional communication from servers to clients.

  In this article, we''ll explore how to implement SSE in Go, discussing its benefits,
  use cases, and providing practical exa...'
---

Les Server-Sent Events (SSE) sont une technologie puissante qui permet une communication unidirectionnelle en temps réel des serveurs vers les clients.

Dans cet article, nous explorerons comment implémenter SSE en Go, en discutant de ses avantages, de ses cas d'utilisation et en fournissant des exemples pratiques. À la fin, vous devriez connaître les bases de la construction d'applications en temps réel avec une communication unidirectionnelle efficace.

## Qu'est-ce que les Server-Sent Events ?

SSE est une technologie web qui permet aux serveurs de pousser des données vers les clients via une seule connexion HTTP.

Contrairement aux WebSockets, SSE est unidirectionnel, ce qui le rend plus simple à implémenter et idéal pour les scénarios où des mises à jour en temps réel du serveur sont nécessaires, mais où la communication du client vers le serveur n'est pas indispensable.

Développer une application web qui utilise SSE est simple. Vous aurez besoin d'un peu de code sur le serveur pour diffuser les événements vers le front-end, mais le code côté client fonctionne presque de la même manière que les WebSockets lorsqu'il s'agit de gérer les événements entrants. Il s'agit d'une connexion unidirectionnelle, vous ne pouvez donc pas envoyer d'événements d'un client vers un serveur.

### Avantages de SSE

1. **Simplicité** : SSE est plus facile à implémenter par rapport aux WebSockets.
    
2. **Support natif du navigateur** : La plupart des navigateurs modernes supportent SSE nativement.
    
3. **Reconnexion automatique** : Les clients tentent automatiquement de se reconnecter si la connexion est perdue.
    
4. **Efficace** : Utilise une seule connexion HTTP, réduisant la surcharge (overhead).
    

## Comment implémenter SSE en Go

Pour notre exemple ici, nous allons créer un serveur SSE simple en Go qui envoie simplement les données au client chaque seconde avec un horodatage actuel. Le client peut ensuite se connecter à notre serveur sur le port 8080 et recevoir ces messages.

Un exemple réel pourrait être quelque chose de plus sophistiqué comme l'envoi de notifications, l'affichage des mises à jour d'une barre de progression, et ainsi de suite.

```go
package main

import (
    "fmt"
    "net/http"
    "time"
)

func sseHandler(w http.ResponseWriter, r *http.Request) {
    // Définir les en-têtes HTTP requis pour SSE
    w.Header().Set("Content-Type", "text/event-stream")
    w.Header().Set("Cache-Control", "no-cache")
    w.Header().Set("Connection", "keep-alive")

    // Vous pourriez en avoir besoin localement pour les requêtes CORS
    w.Header().Set("Access-Control-Allow-Origin", "*")

    // Créer un canal pour la déconnexion du client
    clientGone := r.Context().Done()

    rc := http.NewResponseController(w)
    t := time.NewTicker(time.Second)
    defer t.Stop()
    for {
        select {
        case <-clientGone:
            fmt.Println("Client déconnecté")
            return
        case <-t.C:
            // Envoyer un événement au client
            // Ici, nous n'envoyons que le champ "data", mais il en existe d'autres
            _, err := fmt.Fprintf(w, "data: L'heure est %s\\n\\n", time.Now().Format(time.UnixDate))
            if err != nil {
                return
            }
            err = rc.Flush()
            if err != nil {
                return
            }
        }
    }
}

func main() {
    http.HandleFunc("/events", sseHandler)
    fmt.Println("le serveur tourne sur :8080")
    if err := http.ListenAndServe(":8080", nil); err != nil {
        fmt.Println(err.Error())
    }
}
```

### **Composants clés de l'implémentation SSE**

Le [flux d'événements](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#event_stream_format) est un simple flux de données textuelles qui doit être encodé en UTF-8. Les messages dans le flux d'événements sont séparés par une paire de caractères de saut de ligne – **\\n\\n**. Un deux-points comme premier caractère d'une ligne est par essence un commentaire et est ignoré.

Dans notre serveur, cela se fait ici :

```go
rc := http.NewResponseController(w)
fmt.Fprintf(w, "data: L'heure est %s\\n\\n", time.Now().Format(time.UnixDate))
// Pour s'assurer que les données sont envoyées immédiatement
rc.Flush()
```

Le serveur qui envoie les événements doit répondre en utilisant le type MIME **text/event-stream.** Nous le faisons en définissant l'en-tête de réponse ici :

```go
w.Header().Set("Content-Type", "text/event-stream")
```

Vous avez peut-être remarqué que nous avons également défini quelques autres en-têtes. L'un sert à maintenir la connexion HTTP ouverte, et l'autre à contourner CORS :

```go
w.Header().Set("Cache-Control", "no-cache")
w.Header().Set("Connection", "keep-alive")
w.Header().Set("Access-Control-Allow-Origin", "*")
```

Et la dernière pièce importante est de détecter la déconnexion. En Go, nous la recevrons sous forme de message dans un canal spécifié :

```go
clientGone := r.Context().Done()

for {
    select {
    case <-clientGone:
        fmt.Println("Client déconnecté")
        return
    }
}
```

Chaque message reçu contient une combinaison des champs suivants, un par ligne. Dans notre serveur, nous n'envoyons que le champ data, ce qui est suffisant car les autres champs sont optionnels. Plus de détails [ici](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events).

* **event** – une chaîne identifiant le type d'événement décrit.
    
* **data** – le champ de données pour le message.
    
* **id** – l'ID de l'événement pour définir la valeur du dernier ID d'événement de l'objet EventSource.
    
* **retry** – le délai de reconnexion.
    

### Comment recevoir les événements côté client

Sur le front-end ou côté client, vous devrez utiliser l'interface [EventSource](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#creating_an_eventsource_instance). C'est une API de navigateur encapsulant les Server-Sent Events. Dans l'exemple suivant, notre application de navigateur reçoit les événements du serveur et les affiche dans une liste.

```xml
<!doctype html>
<html>
    <body>
        <ul id="list"></ul>
    </body>

    <script type="text/javascript">
        const eventSrc = new EventSource("http://127.0.0.1:8080/events");

        const list = document.getElementById("list");

        eventSrc.onmessage = (event) => {
            const li = document.createElement("li");
            li.textContent = `message : ${event.data}`;

            list.appendChild(li);
        };
    </script>
</html>
```

Voici à quoi cela peut ressembler dans votre navigateur :

![logs](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe2cda643-36a6-4986-8100-76d1d7c3fb33_998x490.png align="left")

## **Bonnes pratiques pour SSE en Golang**

### **Formatage des événements**

Dans un projet réel, une simple chaîne de données peut ne pas suffire. Dans ces cas, l'utilisation d'un format structuré comme JSON peut être une bonne option pour envoyer plusieurs champs de données à la fois. Voici un exemple :

```json
{
  "status": "in_progress",
  "completion": 51.22
}
```

### **Stratégie de reconnexion et gestion des erreurs**

Quelque chose pourrait toujours mal se passer des deux côtés : le serveur pourrait rejeter la connexion pour une raison quelconque ou un client pourrait se déconnecter brusquement.

Dans chaque cas, vous devrez implémenter une stratégie de backoff pour des reconnexions fluides. Il vaut mieux manquer un message que de casser complètement la boucle d'événements.

En JavaScript, vous pouvez vérifier les erreurs dans EventSource puis agir en conséquence :

```javascript
eventSrc.onerror = (err) => {
  console.error("Échec de l'EventSource :", err);
};
```

### **Répartition de charge (Load Balancing)**

Pour les applications à fort trafic, vous pouvez envisager d'utiliser un répartiteur de charge (Load Balancer), par exemple NGINX. Si vous prévoyez d'avoir de nombreux clients se connectant à votre serveur, il est bon de le tester au préalable en simulant la charge des clients.

## **Cas d'utilisation de SSE**

1. Tableaux de bord en temps réel
    
2. Scores sportifs en direct
    
3. Flux de réseaux sociaux
    
4. Tickers boursiers
    
5. Indicateurs de progression pour les tâches de longue durée
    

## **Conclusion**

Les Server-Sent Events offrent un moyen efficace et simple d'implémenter une communication en temps réel de serveur à client dans les applications Golang. En tirant parti de SSE, les développeurs peuvent créer des applications web réactives et dynamiques avec une surcharge et une complexité minimales.

Lors de la création de vos applications exploitant SSE, n'oubliez pas de prendre en compte l'évolutivité, la gestion des erreurs et l'implémentation côté client pour garantir un système de communication en temps réel robuste et efficace.

[Découvrez d'autres articles sur packagemain.tech](https://packagemain.tech)