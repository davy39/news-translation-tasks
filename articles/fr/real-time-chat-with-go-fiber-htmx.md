---
title: Comment créer une application de chat en temps réel avec Go, Fiber et HTMX
subtitle: ''
author: Akinwumi Iyanuoluwa Ayomiposi
co_authors: []
series: null
date: '2024-06-06T18:06:35.000Z'
originalURL: https://freecodecamp.org/news/real-time-chat-with-go-fiber-htmx
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/websocket.png
tags:
- name: Chat
  slug: chat
- name: Go Language
  slug: go
seo_title: Comment créer une application de chat en temps réel avec Go, Fiber et HTMX
seo_desc: "In this tutorial, you'll build a simple real-time chat app using Go, Fiber\
  \ and HTMX. \nYou will learn how to leverage the versatility of Fiber by making\
  \ use of a WebSocket. You'll also learn how to create a reactive frontend without\
  \ the use of JavaScr..."
---

Dans ce tutoriel, vous allez créer une application de chat en temps réel simple en utilisant Go, Fiber et HTMX.

Vous apprendrez à tirer parti de la polyvalence de Fiber en utilisant une WebSocket. Vous apprendrez également à créer un frontend réactif sans utiliser JavaScript.

## Prérequis

* Une bonne compréhension de Go et des serveurs HTTP.
* Go doit être installé (la version Go 1.22 sera utilisée dans ce projet).

## Table des matières

* [Introduction](#heading-introduction)
* [Comment installer les dépendances](#heading-comment-installer-les-dependances)
* [Fichier main.go](#heading-fichier-maingo)
* [Fichiers statiques](#heading-fichiers-statiques)
* [Comment configurer les fichiers statiques](#heading-comment-configurer-les-fichiers-statiques)
* [Comment créer des gestionnaires](#heading-comment-creer-des-gestionnaires)
* [Fichier messages.go](#heading-fichier-messagesgo)
* [Fichier websocket.go](#heading-fichier-websocketgo)
* [Comment ajouter une WebSocket aux routes et HTMX](#heading-comment-ajouter-une-websocket-aux-routes-et-htmx)
* [Conclusion](#heading-conclusion)


## Introduction

Tout d'abord, créez un nouveau dossier nommé **go-chat**. Initialisez Go dans votre projet en exécutant `go mod init nom_du_paquet`, comme montré ci-dessous :

```
go mod init github.com/steelthedev/go-chat
```

### Comment installer les dépendances

Vous devez installer certaines bibliothèques qui sont très vitales. Cela peut être fait dans le terminal en exécutant les commandes suivantes :

```
go get -u github.com/gofiber/fiber/v2
go get -u github.com/gofiber/websocket/v2
go get -u github.com/gofiber/template/html/v2
```

Cela installera Fiber et d'autres composants tels que WebSocket et la bibliothèque de templating HTML.

### Fichier main.go

Dans le répertoire racine, créez un fichier **main.go**. Ce fichier sera le point d'entrée de l'application. À l'intérieur du fichier, nous allons créer un simple serveur web :

```go
package main

import "github.com/gofiber/fiber/v2"


func main() {
	
    // Démarrer une nouvelle instance fiber
	app := fiber.New()

	// Créer un gestionnaire "ping" pour tester le serveur
	app.Get("/ping", func(ctx *fiber.Ctx) error{
    	return ctx.SendString("Bienvenue sur fiber")
    })

	// Démarrer le serveur http
	app.Listen(":3000")
}

```

Enregistrez le fichier et exécutez `go run main.go` dans le terminal pour démarrer le serveur web.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/tuts1-cropped.png)
_Commande `go run` démarrant le serveur web_

Si vous allez dans le navigateur et testez la route `/ping`, vous devriez obtenir une réponse comme celle-ci :

![Image](https://www.freecodecamp.org/news/content/images/2024/06/welcome-to-fiber-cropped.png)
_Route `/ping` dans le navigateur_

## Fichiers statiques

Nous aurons besoin de fichiers statiques tels que des fichiers CSS et HTML pour que l'application fonctionne. Créez deux dossiers nommés **static** et **views**. À l'intérieur du dossier **views**, créez deux fichiers HTML : **index.html** et **messages.html**.

Voici à quoi devrait ressembler le fichier **index.html** :

```go
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chat Room</title>
    <script src="https://unpkg.com/htmx.org@1.9.10"
        integrity="sha384-D1Kt99CQMDuVetoL1lrYwg5t+9QdHe7NLX/SoJYkXDFfX37iInKRy5xLSi8nO7UC"
        crossorigin="anonymous"></script>
    <!-- Extension HTMX Websockets https://htmx.org/extensions/web-sockets/ -->
    <script src="https://unpkg.com/htmx.org/dist/ext/ws.js"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <link rel="stylesheet" href="/static/style.css">
</head>

<body>
    <div class="container">
        <div class="chat-window">
            <div class="messages" id="messages" >
                <!-- Les messages seront ajoutés ici -->
            </div>
            <form id="form">
                <div class="input-area">
                    <input type="text" name="text" min="1" id="messageInput" placeholder="Tapez un message...">
                    <button type="submit">Envoyer</button>
                </div>
            </form>

        </div>
    </div>

</body>

</html>
```

Dans le **index.html** ci-dessus, nous avons lié les plugins nécessaires tels que notre **style.css** qui sera bientôt créé, HTMX et Bootstrap 5.

Voici à quoi devrait ressembler le fichier **message.html** :

```
<div id="messages" hx-swap-oob="beforeend">
    <p class="text-small">{{ .Text }}</p>
</div>
```

Ce message sera la réponse du serveur, il sera inséré automatiquement dans notre code **index.html** dans le navigateur avec l'aide de HTMX.

Maintenant, créez un nouveau dossier nommé **static**. À l'intérieur, créez un nouveau fichier **style.css** :

```
body {
    margin: 0;
    padding: 0;
    font-family: Arial, sans-serif;
    background-color: #f2f2f2;
}

.container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

.chat-window {
    width: 400px;
    background-color: #fff;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.messages {
    padding: 10px;
    overflow-y: scroll;
    height: 300px;
}

.message {
    margin-bottom: 10px;
}

.message p {
    background-color: #f0f0f0;
    border-radius: 5px;
    padding: 5px 10px;
    display: inline-block;
    max-width: 80%;
}

.input-area {
    padding: 10px;
    display: flex;
}

.input-area input[type="text"] {
    flex: 1;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 5px;
    margin-right: 5px;
}

.input-area button {
    padding: 8px 15px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
}

.input-area button:hover {
    background-color: #45a049;
}

.input-area button:active {
    background-color: #3e8e41;
}
```

## Comment configurer les fichiers statiques

Dans votre fichier **main.go**, vous devez indiquer à Fiber comment gérer vos fichiers statiques, surtout le dossier à vérifier pour le rendu HTML. Mettez à jour **main.go** comme suit :

```
package main

import (
	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/template/html/v2"
)

func main() {

	
    // Créer le moteur de vues
    viewsEngine := html.New("./views", ".html")


    // Démarrer une nouvelle instance fiber
	app := fiber.New(fiber.Config{
		Views: viewsEngine,
	})
    
    // Route et répertoire statiques
    app.Static("/static/", "./static")
    
	// Créer un gestionnaire "ping" pour tester le serveur
	app.Get("/ping", func(ctx *fiber.Ctx) error{
    	return ctx.SendString("Bienvenue sur fiber")
    })

	// Démarrer le serveur http
	app.Listen(":3000")

}

```

Comme vu ci-dessus, une configuration a été ajoutée à l'instance de l'application et la route statique a été configurée pour être `/static/`.

## Comment créer des gestionnaires

Créez un nouveau fichier nommé **handlers.go** :

```
package handlers

import "github.com/gofiber/fiber/v2"

type AppHandler struct{}

func NewAppHandler() *AppHandler {
	return &AppHandler{}
}

func (a *AppHandler) HandleGetIndex(ctx *fiber.Ctx) error {
	context := fiber.Map{}
	return ctx.Render("index", context)
}

```

Dans le code ci-dessus, nous avons créé un gestionnaire qui reçoit la structure `AppHandler`. Cela aide à l'abstraction au cas où le code deviendrait plus volumineux. La fonction `HandleGetIndex` prend un pointeur vers le contexte Fiber et rend le fichier **index.html**.

Dans **main.go** :

```
package main

import (
	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/template/html/v2"
	"github.com/steelthedev/go-chat/handlers"
)

func main() {
	
    // Démarrer une nouvelle instance fiber
	app := fiber.New()

	// Créer un gestionnaire "ping" pour tester le serveur
	app.Get("/ping", func(ctx *fiber.Ctx) error{
    	return ctx.SendString("Bienvenue sur fiber")
    })
    
    // créer un nouveau gestionnaire d'application
    appHandler := NewAppHandler()
    
    // Ajouter les routes du gestionnaire d'application
    app.Get("/", appHandler.HandleGetIndex)

	// Démarrer le serveur http
	app.Listen(":3000")
}

```

Ci-dessus, nous avons créé un nouveau gestionnaire d'application et ajouté la fonction `HandleGetIndex` dans les routes. Exécutez la commande `go run main.go`. Sur `localhost:3000`, vous devriez avoir un écran similaire à celui-ci :

![Image](https://www.freecodecamp.org/news/content/images/2024/06/chat-room-cropped.png)
_zone de saisie, bouton d'envoi et zone d'affichage du chat sur localhost:3000_

### Fichier messages.go

Créez un nouveau fichier dans le projet et nommez-le **message.go**. Ce fichier hébergera la structure du message.

```
package main

type Message struct {
	Text       string `json:"text"`
}

```

### Fichier websocket.go

Créez un nouveau fichier dans le répertoire du projet et nommez-le **websocket.go**. Ce fichier contiendra la fonction principale créant le serveur WebSocket, lisant à travers celui-ci et écrivant sur tous les canaux :

```
package main

import (
	"bytes"
	"encoding/json"
	"html/template"
	"log"

	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/websocket/v2"
)

type WebSocketServer struct {
	clients   map[*websocket.Conn]bool
	broadcast chan *Message
}

func NewWebSocket() *WebSocketServer {
	return &WebSocketServer{
		clients:   make(map[*websocket.Conn]bool),
		broadcast: make(chan *Message),
	}
}


func (s *WebSocketServer) HandleWebSocket(ctx *websocket.Conn) {

	// Enregistrer un nouveau client
	s.clients[ctx] = true
	defer func() {
		delete(s.clients, ctx)
		ctx.Close()
	}()

	for {
		_, msg, err := ctx.ReadMessage()
		if err != nil {
			log.Println("Erreur de lecture :", err)
			break
		}

		// envoyer le message au canal de diffusion
		var message Message
		if err := json.Unmarshal(msg, &message); err != nil {
			log.Fatalf("Erreur de désérialisation")
		}
		s.broadcast <- &message
	}
}

func (s *WebSocketServer) HandleMessages() {
	for {
		msg := <-s.broadcast

		// Envoyer le message à tous les clients

		for client := range s.clients {
			err := client.WriteMessage(websocket.TextMessage, getMessageTemplate(msg))
			if err != nil {
				log.Printf("Erreur d'écriture : %v ", err)
				client.Close()
				delete(s.clients, client)
			}

		}

	}
}

func getMessageTemplate(msg *Message) []byte {
	tmpl, err := template.ParseFiles("views/message.html")
	if err != nil {
		log.Fatalf("analyse du template : %s", err)
	}

	// Rendre le template avec le message comme données.
	var renderedMessage bytes.Buffer
	err = tmpl.Execute(&renderedMessage, msg)
	if err != nil {
		log.Fatalf("exécution du template : %s", err)
	}

	return renderedMessage.Bytes()
}

```

La fonction `HandleWebSocket` ajoute le client, traite les messages en JSON et ajoute ensuite le message dans un canal pour distribution à tous les clients par `HandleMessage`.

Elle maintient également la connexion active. `getMessageTemplate` traite essentiellement le message dans le fichier **message.html**, puis le convertit en octets. Ces octets peuvent ensuite être envoyés au client en tant que réponse.

### Comment ajouter une WebSocket aux routes et HTMX

Nous devons ajouter la WebSocket à nos routes dans **main.go** :

```
package main

import (
	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/template/html/v2"
    "github.com/gofiber/websocket/v2"
	"github.com/steelthedev/go-chat/handlers"
)

func main() {
	
    // Démarrer une nouvelle instance fiber
	app := fiber.New()

	// Créer un gestionnaire "ping" pour tester le serveur
	app.Get("/ping", func(ctx *fiber.Ctx) error{
    	return ctx.SendString("Bienvenue sur fiber")
    })
    
    // créer un nouveau gestionnaire d'application
    appHandler := NewAppHandler()
    
    // Ajouter les routes du gestionnaire d'application
    app.Get("/", appHandler.HandleGetIndex)
    
    // créer un nouveau websocket
    server := NewWebSocket()
    app.Get("/ws", websocket.New(func(ctx *websocket.Conn) {
		server.HandleWebSocket(ctx)
	}))

	go server.HandleMessages()
    

	// Démarrer le serveur http
	app.Listen(":3000")
}

```

La WebSocket et sa route ont été ajoutées. La dernière étape consiste à ajouter les balises HTMX dans le fichier **index.html** :

```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chat Room</title>
    <script src="https://unpkg.com/htmx.org@1.9.10"
        integrity="sha384-D1Kt99CQMDuVetoL1lrYwg5t+9QdHe7NLX/SoJYkXDFfX37iInKRy5xLSi8nO7UC"
        crossorigin="anonymous"></script>
    <!-- Extension HTMX Websockets https://htmx.org/extensions/web-sockets/ -->
    <script src="https://unpkg.com/htmx.org/dist/ext/ws.js"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <link rel="stylesheet" href="/static/style.css">
</head>

<body>
    <div class="container">
        <div class="chat-window" hx-ext="ws" ws-connect="/ws">
            <div class="messages" id="messages" hx-swap="beforeend" hx-swap-oob="beforeend">
                <!-- Les messages seront ajoutés ici -->
            </div>
            <form id="form" ws-send>
                <div class="input-area">
                    <input type="text" name="text" min="1" id="messageInput" placeholder="Tapez un message...">
                    <button type="submit">Envoyer</button>
                </div>
            </form>

        </div>
    </div>

</body>

</html>
```

La balise `hx-ext` et la balise `ws-connect` pointent vers l'URL de la WebSocket `/ws`. La balise `hx-swap` a été utilisée pour effectuer des manipulations DOM qui ajoutent nos messages dans la div `#messages`.

Après avoir enregistré cela, exécutez `go run main.go`. Vous pouvez ouvrir deux fenêtres de navigateur différentes sur `localhost:3000`.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-from-2024-06-02-04-23-06.png)
_deux fenêtres de navigateur utilisées pour envoyer et recevoir des messages_

Si la WebSocket fonctionne parfaitement, vous devriez pouvoir envoyer et recevoir des messages entre les deux navigateurs en temps réel comme affiché dans l'image.

### Conclusion

Dans ce tutoriel, nous avons montré comment créer un simple serveur WebSocket en utilisant Go, Fiber et HTMX.

Vous pouvez continuer et améliorer ce projet en ajoutant des fonctionnalités supplémentaires telles que ClientID, l'authentification et la gestion des utilisateurs. Vous pouvez visiter le dépôt du projet ici : [github.com/steelthedev/go-chat](https://github.com/steelthedev/go-chat)