---
title: How to Build a Real-Time Chat App With Go, Fiber and HTMX
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
seo_title: null
seo_desc: "In this tutorial, you'll build a simple real-time chat app using Go, Fiber\
  \ and HTMX. \nYou will learn how to leverage the versatility of Fiber by making\
  \ use of a WebSocket. You'll also learn how to create a reactive frontend without\
  \ the use of JavaScr..."
---

In this tutorial, you'll build a simple real-time chat app using Go, Fiber and HTMX. 

You will learn how to leverage the versatility of Fiber by making use of a WebSocket. You'll also learn how to create a reactive frontend without the use of JavaScript.

## Prerequisites

* A good understanding of Go and HTTP servers.
* Go must be installed (Go version 1.22 will be used in this project).

## Table of Contents

* [Getting Started](#heading-getting-started)
* [How to Install Dependencies](#heading-how-to-install-dependencies)
* [main.go File](#heading-maingo-file)
* [Static Files](#heading-static-files)
* [How to Configure Static Files](#heading-how-to-configure-static-files)
* [How to Create Handlers](#heading-how-to-create-handlers)
* [messages.go File](#heading-messagesgo-file)
* [websocket.go File](#heading-websocketgo-file)
* [How to Add a WebSocket to Routes and HTMX](#heading-how-to-add-a-websocket-to-routes-and-htmx)
* [Conclusion](#heading-conclusion)  


## Getting Started

First, create a new folder named **go-chat**. Initiate Go in your project by running `go mod init pakacage_name`, as can seen below:

```
go mod init github.com/steelthedev/go-chat
```

### How to Install Dependencies

You need to install some libraries which are very vital. This can be done in the terminal by running the following commands:

```
go get -u github.com/gofiber/fiber/v2
go get -u github.com/gofiber/websocket/v2
go get -u github.com/gofiber/template/html/v2
```

These will install Fiber and other components such as WebSocket and HTML templating library.

### main.go File

In the root directory, create a **main.go** file. This file will be the entry point to the application. Inside the file we are going to create a simple web server:

```go
package main

import "github.com/gofiber/fiber/v2"


func main() {
	
    // Start new fiber instance
	app := fiber.New()

	// Create a "ping" handler to test the server
	app.Get("/ping", func(ctx *fiber.Ctx) error{
    	return ctx.SendString("Welcome to fiber")
    })

	// Start the http server
	app.Listen(":3000")
}

```

Save the file and run `go run main.go` in the terminal to start the web server. 

![Image](https://www.freecodecamp.org/news/content/images/2024/06/tuts1-cropped.png)
_`go run` command starting the web server_

If you head over to the browser and test the `/ping` route, there should be a response like this:

![Image](https://www.freecodecamp.org/news/content/images/2024/06/welcome-to-fiber-cropped.png)
_/ping route in the browser_

## Static Files 

We'll need static files such as CSS and HTML files for the application to function. Create two folders with named **static** and **views**. Inside the **views** folder, create two html files: **index.html** and **messages.html**.

Here's what the **index.html** file should look like:

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
    <!-- HTMX Websockets extension https://htmx.org/extensions/web-sockets/ -->
    <script src="https://unpkg.com/htmx.org/dist/ext/ws.js"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <link rel="stylesheet" href="/static/style.css">
</head>

<body>
    <div class="container">
        <div class="chat-window">
            <div class="messages" id="messages" >
                <!-- Messages will be appended here -->
            </div>
            <form id="form">
                <div class="input-area">
                    <input type="text" name="text" min="1" id="messageInput" placeholder="Type a message...">
                    <button type="submit">Send</button>
                </div>
            </form>

        </div>
    </div>

</body>

</html>
```

In the **index.html** above, we have linked the necessary plugins such as our **style.css** which will soon be created, HTMX and bootstrap 5.

Here's what the **message.html** file should look like:

```
<div id="messages" hx-swap-oob="beforeend">
    <p class="text-small">{{ .Text }}</p>
</div>
```

This message will be the response from the server, it will be swapped into our **index.html** code automatically in the browser with the help of HTMX.

Now, create a new folder named **static**. Inside it, create a new file **style.css**:

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

## How to Configure Static Files 

In your **main.g**o file, you need to tell Fiber how to handle your static files, most especially the folder to check for HTML rendering. Update **main.go** as follow:

```
package main

import (
	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/template/html/v2"
)

func main() {

	
    // Create views engine
    viewsEngine := html.New("./views", ".html")


    // Start new fiber instance
	app := fiber.New(fiber.Config{
		Views: viewsEngine,
	})
    
    // Static route and directory
    app.Static("/static/", "./static")
    
	// Create a "ping" handler to test the server
	app.Get("/ping", func(ctx *fiber.Ctx) error{
    	return ctx.SendString("Welcome to fiber")
    })

	// Start the http server
	app.Listen(":3000")

}

```

As seen above, a configuration was added to the app instance and also configured the static route to be `/static/`.

## How to Create Handlers

Create a new file named **handlers.go**:

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

In the code above, we created a handler which received the `AppHandler` struct. This helps with abstractions in case the code gets bigger. The `HandleGetIndex` function takes in a pointer to the Fiber context and renders the **index.html** file.

In **main.go**:

```
package main

import (
	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/template/html/v2"
	"github.com/steelthedev/go-chat/handlers"
)

func main() {
	
    // Start new fiber instance
	app := fiber.New()

	// Create a "ping" handler to test the server
	app.Get("/ping", func(ctx *fiber.Ctx) error{
    	return ctx.SendString("Welcome to fiber")
    })
    
    // create new App Handler
    appHandler := NewAppHandler()
    
    // Add appHandler routes
    app.Get("/, appHandler.HandleGetIndex)

	// Start the http server
	app.Listen(":3000")
}

```

Above, we created a new app handler and added the `HandleGetIndex` function in the routes. Run the `go run main.go` command. On `localhost:3000`, you should have a screen similar to this:

![Image](https://www.freecodecamp.org/news/content/images/2024/06/chat-room-cropped.png)
_input box, send button, and chat display area on localhost:3000_

### messages.go File

Create a new file in the project directly and name it **message.go**. This file will host the message struct.

```
package main

type Message struct {
	Text       string `json:"text"`
}

```

### websocket.go File

Create a new file in the project directory and name it **websocket.go**. This will house the main function creating the WebSocket server, reading through it and writing to all channels:

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

	// Register a new Client
	s.clients[ctx] = true
	defer func() {
		delete(s.clients, ctx)
		ctx.Close()
	}()

	for {
		_, msg, err := ctx.ReadMessage()
		if err != nil {
			log.Println("Read Error:", err)
			break
		}

		// send the message to the broadcast channel
		var message Message
		if err := json.Unmarshal(msg, &message); err != nil {
			log.Fatalf("Error Unmarshalling")
		}
		s.broadcast <- &message
	}
}

func (s *WebSocketServer) HandleMessages() {
	for {
		msg := <-s.broadcast

		// Send the message to all Clients

		for client := range s.clients {
			err := client.WriteMessage(websocket.TextMessage, getMessageTemplate(msg))
			if err != nil {
				log.Printf("Write  Error: %v ", err)
				client.Close()
				delete(s.clients, client)
			}

		}

	}
}

func getMessageTemplate(msg *Message) []byte {
	tmpl, err := template.ParseFiles("views/message.html")
	if err != nil {
		log.Fatalf("template parsing: %s", err)
	}

	// Render the template with the message as data.
	var renderedMessage bytes.Buffer
	err = tmpl.Execute(&renderedMessage, msg)
	if err != nil {
		log.Fatalf("template execution: %s", err)
	}

	return renderedMessage.Bytes()
}

```

The `HandleWebSocket` function adds the client, processes the messages into JSON and then adds the message into a channel for distribution to all clients by `HandleMessage`. 

It also keeps the connection alive. `getMessageTemplate` basically process the message into the **message.html**, and then converts it to a byte. This byte can then be sent to the client as a response. 

### How to Add a WebSocket to Routes and HTMX

We need to add the WebSocket to our routes **main.go**:

```
package main

import (
	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/template/html/v2"
    "github.com/gofiber/websocket/v2"
	"github.com/steelthedev/go-chat/handlers"
)

func main() {
	
    // Start new fiber instance
	app := fiber.New()

	// Create a "ping" handler to test the server
	app.Get("/ping", func(ctx *fiber.Ctx) error{
    	return ctx.SendString("Welcome to fiber")
    })
    
    // create new App Handler
    appHandler := NewAppHandler()
    
    // Add appHandler routes
    app.Get("/, appHandler.HandleGetIndex)
    
    // create new webscoket
    server := NewWebSocket()
    app.Get("/ws", websocket.New(func(ctx *websocket.Conn) {
		server.HandleWebSocket(ctx)
	}))

	go server.HandleMessages()
    

	// Start the http server
	app.Listen(":3000")
}

```

The WebSocket and its route has been added. The final step is to add the HTMX tags on the **index.html** file:

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
    <!-- HTMX Websockets extension https://htmx.org/extensions/web-sockets/ -->
    <script src="https://unpkg.com/htmx.org/dist/ext/ws.js"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <link rel="stylesheet" href="/static/style.css">
</head>

<body>
    <div class="container">
        <div class="chat-window" hx-ext="ws" ws-connect="/ws">
            <div class="messages" id="messages" hx-swap="beforeend" hx-swap-oob="beforeend">
                <!-- Messages will be appended here -->
            </div>
            <form id="form" ws-send hx ">
                <div class="input-area">
                    <input type="text" name="text" min="1" id="messageInput" placeholder="Type a message...">
                    <button type="submit">Send</button>
                </div>
            </form>

        </div>
    </div>

</body>

</html>
```

The `hx-ext` tag and `ws-connect` tag point to the WebSocket URL `/ws`. The `hx-swap` tag was used to perform DOM manipulations which adds our messages into the `#messages` div.

After saving this, run `go run main.go`. You can open two different browser windows at `localhost:3000`

![Image](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-from-2024-06-02-04-23-06.png)
_two browser windows used for sending and receiving messages_

If the WebSocket is running perfectly, you should be able to send and receive messages from the two browsers in real-time as displayed in the picture.

### Conclusion

In this tutorial, we have showcased how to create a simple WebSocket server using Go, Fiber and HTMX. 

You can go on and improve this project by adding extra features such as ClientID, authentication and user management. You can visit the project repo here: [github.com/steelthedev/go-chat](https://github.com/steelthedev/go-chat)

