---
title: 'Créez votre propre serveur web avec Go : Un guide rapide'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-04T19:58:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-your-own-web-server-with-go
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e35740569d1a4ca3be7.jpg
tags:
- name: Go Language
  slug: go
- name: servers
  slug: servers
seo_title: 'Créez votre propre serveur web avec Go : Un guide rapide'
seo_desc: 'The Go programming language is well-known for having a built-in web server.
  In this article you will learn how you can easily make your own web server with
  Go. You won’t need any other packages beside the ones that are already built in!

  First, hop in...'
---

Le langage de programmation Go est bien connu pour avoir un serveur web intégré. Dans cet article, vous apprendrez comment créer facilement votre propre serveur web avec Go. Vous n'aurez besoin d'aucun autre package en plus de ceux déjà intégrés !

Tout d'abord, ouvrez votre éditeur de texte. Ensuite, créez un fichier appelé `webserver.go` et entrez le code suivant :

```go
package main

import (
  "net/http"
  "io"
)

func main() {
  http.HandleFunc("/", servePage)
	http.ListenAndServe(":8080", nil)
}

func servePage(writer http.ResponseWriter, reqest *http.Request) {
  io.WriteString(writer, "Hello world!")
}
```

Décortiquons le bloc de code ci-dessus. Nous importons le package `net/http` : ce package contient le serveur web lui-même. Ensuite, nous importons également le package `io`, que nous utiliserons plus tard pour servir quelque chose au client.

Dans la fonction `main`, nous faisons deux choses. Tout d'abord, nous instruisons le serveur de laisser la fonction appelée `servePage` gérer tout le trafic entrant vers `/` - dans ce cas, cela signifie qu'elle gère les requêtes vers _n'importe quelle_ `URL`.

La deuxième chose que nous faisons est d'activer le serveur. Nous le faisons en utilisant une fonction nommée `ListenAndServe`. Cette fonction nécessite deux paramètres : le `port` (en tant que `string`), dans ce cas, c'est `8080`, et le `handler` (en tant que `Handler`) - cependant, ce dernier n'est pas important pour l'instant. Nous allons simplement le mettre à `nil` et tout fonctionnera très bien.

Dans la fonction `servePage`, nous faisons une chose simple, pour l'instant. En utilisant le package `io` et la fonction `WriteString` qu'il contient, nous pouvons répondre à la requête du client avec le texte `Hello world!` (ou toute autre chaîne de caractères, bien sûr).

Vous avez peut-être également remarqué que la fonction `servePage` a deux arguments : le `writer` et le `request`. Avec le writer, vous pouvez répondre à une requête `HTTP` et avec le `request`, vous pouvez obtenir plus d'informations sur la requête elle-même.

Félicitations ! Vous venez de créer votre premier serveur web ! Si vous voulez le tester : exécutez simplement `go run webserver.go`, lancez un navigateur et accédez à `http://localhost:8080` !