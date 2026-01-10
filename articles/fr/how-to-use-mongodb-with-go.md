---
title: Comment utiliser MongoDB avec Go
subtitle: ''
author: Oluwadamilola Oshungboye
co_authors: []
series: null
date: '2025-07-31T05:49:27.396Z'
originalURL: https://freecodecamp.org/news/how-to-use-mongodb-with-go
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1753940956019/6551a007-b463-486f-8746-15c13a7a99a0.png
tags:
- name: Go Language
  slug: go
- name: MongoDB
  slug: mongodb
- name: Tutorial
  slug: tutorial
seo_title: Comment utiliser MongoDB avec Go
seo_desc: 'Working with databases is a fundamental part of backend development, particularly
  when you’re building applications that require persisting, querying, and updating
  data.

  In Go, the official MongoDB driver provides a robust way to connect to and inter...'
---

Travailler avec des bases de données est une partie fondamentale du développement backend, en particulier lorsque vous construisez des applications qui nécessitent de persister, d'interroger et de mettre à jour des données.

En Go, le [pilote officiel MongoDB](https://github.com/mongodb/mongo-go-driver) fournit un moyen robuste de se connecter à MongoDB et d'interagir avec lui, une base de données NoSQL flexible qui stocke les données dans des documents de type JSON.

Dans ce tutoriel, vous n'apprendrez pas seulement à connecter Go à MongoDB. Vous irez plus loin en construisant une simple application de blog. En cours de route, vous apprendrez à effectuer des opérations CRUD (Create, Read, Update, Delete) essentielles et à afficher vos résultats en utilisant le framework web Gin.

## **Table des matières**

* [Prérequis](#heading-prérequis)
    
* [Créer un nouveau projet Go](#heading-créer-un-nouveau-projet-go)
    
* [Opérations de base avec MongoDB](#heading-opérations-de-base-avec-mongodb)
    
    * [Insérer des données dans la collection](#heading-insérer-des-données-dans-la-collection)
        
    * [Trouver des documents dans MongoDB](#heading-trouver-des-documents-dans-mongodb)
        
    * [Mettre à jour des documents dans MongoDB](#heading-mettre-à-jour-des-documents-dans-mongodb)
        
    * [Supprimer des documents dans MongoDB](#heading-supprimer-des-documents-dans-mongodb)
        
* [Comment construire une application de blog avec go-mongodb-driver et Gin](#heading-comment-construire-une-application-de-blog-avec-go-mongodb-driver-et-gin)
    
    * [Initialiser l'application Gin](#heading-initialiser-l'application-gin)
        
    * [Créer les modèles HTML](#heading-créer-les-modèles-html)
        
    * [Créer les gestionnaires](#heading-créer-les-gestionnaires)
        
    * [Exécuter l'application](#heading-exécuter-l'application)
        
* [C'est ainsi qu'on utilise MongoDB avec Go](#heading-c'est-ainsi-qu'on-utilise-mongodb-avec-go)
    

## Prérequis

Avant de continuer, assurez-vous d'avoir les éléments suivants :

* Connaissance de base de [Go](https://go.dev/) et de ses concepts
    
* Go (version 1.24 ou supérieure) installé
    
* [MongoDB](https://www.mongodb.com/docs/manual/installation/) installé (en cours d'exécution localement sur le port 27017)
    
* Connaissance de base de NoSQL
    

## Créer un nouveau projet Go

Tout d'abord, créez un nouveau projet Go, accédez au nouveau répertoire du projet et initialisez un nouveau module Go en exécutant les commandes suivantes :

```bash
mkdir go-mongodb-integration
cd go-mongodb-integrationgo 
mod init go-mongodb
```

Ensuite, installez le pilote MongoDB Go en exécutant la commande suivante :

```bash
go get go.mongodb.org/mongo-driver/mongo
go get go.mongodb.org/mongo-driver/bson
```

La bibliothèque standard Go inclut le package `database/sql` pour travailler avec les bases de données SQL, mais elle ne supporte pas MongoDB directement. Pour travailler avec MongoDB en Go, vous utiliserez le pilote officiel MongoDB, qui fournit tout ce dont vous avez besoin pour vous connecter à une base de données MongoDB et interagir avec elle.

Avec la configuration de base terminée, examinons maintenant les opérations de base dans MongoDB.

## Opérations de base avec MongoDB

Dans MongoDB, les bases de données et les [collections](https://www.mongodb.com/docs/manual/reference/glossary/#std-term-collection) sont créées automatiquement lors de la première insertion de données, adoptant une approche de "création paresseuse". Plus précisément, une base de données est créée lorsque vous insérez votre premier document, et une collection est créée de la même manière lorsque des données sont insérées pour la première fois.

Il est important de noter que des fonctions comme `client.Database()` et `db.Collection()` ne génèrent que des références à ces structures - elles ne créent pas la base de données ou la collection réelle tant que des données ne sont pas insérées.

### Insérer des données dans la collection

Examinons comment insérer un document dans une collection dans MongoDB.

Tout d'abord, ouvrez votre projet dans un éditeur de code, créez un fichier `main.go` et ajoutez le code suivant :

```go
package main

import (
	"context"
	"log"
	"time"

	"go.mongodb.org/mongo-driver/bson/primitive"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

type User struct {
	ID   primitive.ObjectID `bson:"_id,omitempty"`
	Name string             `bson:"name"`
	Age  int                `bson:"age"`
}

func main() {
	clientOptions := options.Client().ApplyURI("mongodb://localhost:27017")

	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()

	client, err := mongo.Connect(ctx, clientOptions)
	if err != nil {
		log.Fatal(err)
	}
	defer client.Disconnect(ctx)

	err = client.Ping(ctx, nil)
	if err != nil {
		log.Fatal(err)
	}

	db := client.Database("test_db")
	usersCollection := db.Collection("users")

	newUser := User{
		Name: "John Doe",
		Age:  30,
	}

	result, err := usersCollection.InsertOne(ctx, newUser)
	if err != nil {
		log.Fatal(err)
	}

	log.Printf("Inserted user with ID: %v\n", result.InsertedID)
}
```

Dans le code ci-dessus, vous définissez une [struct](https://www.w3schools.com/go/go_struct.php) `User` qui représente la structure de votre document, puis vous insérez un nouveau document utilisateur dans la collection en utilisant la méthode `InsertOne`. Lorsque vous exécutez cette opération d'insertion, MongoDB crée automatiquement la base de données `test_db` et la collection `users` si elles n'existent pas déjà.

Exécutez le code en exécutant :

```bash
go run main.go
```

Vous devriez voir la réponse ci-dessous, indiquant qu'un utilisateur a été inséré avec succès.

![Une interface de ligne de commande montrant la commande `go run main.go` avec une sortie qui dit, "Inserted user with ID: ObjectID('6862f3112341b0492801633b')" le 30 juin 2025.](https://cdn.hashnode.com/res/hashnode/image/upload/v1753561045916/79c1f4f1-ebe1-41e8-b6dd-01a5e2c9d247.png align="center")

### Trouver des documents dans MongoDB

Maintenant que vous avez inséré des données, il est temps d'interroger la base de données et de récupérer des documents.

Mettez à jour votre fichier `main.go` avec le code suivant :

```go
package main

import (
	"context"
	"fmt"
	"log"
	"time"

	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/bson/primitive"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

type User struct {
	ID   primitive.ObjectID `bson:"_id,omitempty"`
	Name string             `bson:"name"`
	Age  int                `bson:"age"`
}

func main() {
	clientOptions := options.Client().ApplyURI("mongodb://localhost:27017")

	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()

	client, err := mongo.Connect(ctx, clientOptions)
	if err != nil {
		log.Fatal(err)
	}
	defer client.Disconnect(ctx)

	db := client.Database("test_db")
	usersCollection := db.Collection("users")

	cursor, err := usersCollection.Find(ctx, bson.M{})
	if err != nil {
		log.Fatal(err)
	}
	defer cursor.Close(ctx)

	var users []User
	if err = cursor.All(ctx, &users); err != nil {
		log.Fatal(err)
	}

	for _, user := range users {
		fmt.Printf("User: %s, Age: %d, ID: %s\n", user.Name, user.Age, user.ID.Hex())
	}
}
```

Dans le code ci-dessus, vous utilisez la méthode `Find` avec un filtre vide (`bson.M{}`) pour récupérer tous les documents de la collection `users`. Ensuite, vous utilisez `cursor.All` pour décoder tous les résultats dans une tranche de structs `User`.

Chaque document est imprimé dans le terminal, montrant le nom, l'âge et l'ID de chaque utilisateur dans la collection.

Pour exécuter le code, utilisez :

```bash
go run main.go
```

Vous devriez voir la réponse ci-dessous dans votre terminal.

![Capture d'écran d'un terminal montrant une exécution de commande Go et une sortie avec des informations utilisateur incluant le nom, l'âge et l'ID.](https://cdn.hashnode.com/res/hashnode/image/upload/v1753561158932/adc32e01-742e-4c5c-acf8-a83e1197a27c.png align="left")

### Mettre à jour des documents dans MongoDB

Pour mettre à jour un document dans votre collection, modifiez votre fichier `main.go` comme indiqué ci-dessous :

```go
package main

import (
	"context"
	"log"
	"time"

	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/bson/primitive"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

type User struct {
	ID   primitive.ObjectID `bson:"_id,omitempty"`
	Name string             `bson:"name"`
	Age  int                `bson:"age"`
}

func main() {
	clientOptions := options.Client().ApplyURI("mongodb://localhost:27017")
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()

	client, err := mongo.Connect(ctx, clientOptions)
	if err != nil {
		log.Fatal(err)
	}
	defer client.Disconnect(ctx)

	db := client.Database("test_db")
	usersCollection := db.Collection("users")

	var userToUpdate User
	err = usersCollection.FindOne(ctx, bson.M{"name": "John Doe"}).Decode(&userToUpdate)
	if err != nil {
		log.Println("No user found to update")
	} else {
		update := bson.M{
			"$set": bson.M{
				"name": "Jane Doe",
				"age":  25,
			},
		}
		result, err := usersCollection.UpdateOne(
			ctx,
			bson.M{"_id": userToUpdate.ID},
			update,
		)
		if err != nil {
			log.Fatal(err)
		}
		log.Printf("Updated %v document(s)\n", result.ModifiedCount)
	}
}
```

Dans le code ci-dessus, vous recherchez d'abord un utilisateur nommé "John Doe" en utilisant la méthode `FindOne`. Si une correspondance est trouvée, vous utilisez la méthode `UpdateOne` pour mettre à jour son nom et son âge. L'opérateur `$set` garantit que seuls les champs spécifiés sont mis à jour, laissant le reste du document inchangé.

Exécutez le code en exécutant :

```bash
go run main.go
```

Vous devriez voir une sortie dans votre terminal indiquant combien de documents ont été mis à jour.

![Interface de ligne de commande montrant "go run main.go" et la sortie "2025/06/30 21:34:36 Updated 1 document(s)".](https://cdn.hashnode.com/res/hashnode/image/upload/v1753561280040/73f7a859-5d7a-440a-a58b-b6105b8837ab.png align="left")

### Supprimer des documents dans MongoDB

Pour supprimer des documents d'une collection, vous pouvez utiliser la méthode `DeleteOne`. Mettez à jour votre fichier `main.go` avec le code suivant :

```go
package main

import (
	"context"
	"log"
	"time"

	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/bson/primitive"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

type User struct {
	ID   primitive.ObjectID `bson:"_id,omitempty"`
	Name string             `bson:"name"`
	Age  int                `bson:"age"`
}

func main() {
	clientOptions := options.Client().ApplyURI("mongodb://localhost:27017")
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()

	client, err := mongo.Connect(ctx, clientOptions)
	if err != nil {
		log.Fatal(err)
	}
	defer client.Disconnect(ctx)

	db := client.Database("test_db")
	usersCollection := db.Collection("users")

	result, err := usersCollection.DeleteOne(ctx, bson.M{"name": "Jane Doe"})
	if err != nil {
		log.Fatal(err)
	}
	log.Printf("Deleted %v document(s)\n", result.DeletedCount)
}
```

Dans le code ci-dessus, vous utilisez la méthode `DeleteOne` pour supprimer le premier document qui correspond au filtre `{ "name": "Jane Doe" }`.

Vous devriez voir le résultat ci-dessous dans votre terminal.

![Un terminal de ligne de commande montrant l'exécution de "go run main.go" et la sortie "2025/06/30 21:36:05 Deleted 1 document(s)".](https://cdn.hashnode.com/res/hashnode/image/upload/v1753561355070/ab8797ef-8a15-47e0-8502-9b120fbbd2b8.png align="left")

## Comment construire une application de blog avec go-mongodb-driver et Gin

Maintenant que vous comprenez comment effectuer des opérations CRUD de base avec MongoDB en Go, vous êtes prêt à construire une application plus complète.

Commencez par créer un nouveau répertoire pour votre projet et initialisez-le en tant que module Go. Accédez à votre répertoire choisi et exécutez :

```bash
mkdir go-blog
cd go-blog
go mod init blog
```

Ensuite, installez les dépendances requises :

```bash
go get github.com/gin-gonic/gin
go get go.mongodb.org/mongo-driver/mongo
go get go.mongodb.org/mongo-driver/bson
```

Votre projet aura la structure suivante :

```bash
go-blog/  
 main.go  
 handlers/  
    main.go  
 templates/  
     index.html  
     post.html  
     create.html  
     edit.html
```

### Initialiser l'application Gin

Pour initialiser une nouvelle application Gin, créez un nouveau fichier `main.go` et ajoutez le code suivant :

```go
package main

import (
	"context"
	"log"
	"time"

	"blog/handlers"

	"github.com/gin-gonic/gin"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

func main() {
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()

	clientOptions := options.Client().ApplyURI("mongodb://localhost:27017")
	client, err := mongo.Connect(ctx, clientOptions)
	if err != nil {
		log.Fatal(err)
	}
	defer client.Disconnect(ctx)

	err = client.Ping(ctx, nil)
	if err != nil {
		log.Fatal(err)
	}
	log.Println("Connected to MongoDB!")

	db := client.Database("blog_db")
	h := handlers.NewHandler(db)

	router := gin.Default()
	router.LoadHTMLGlob("templates/*")

	router.GET("/", h.HomePage)
	router.GET("/post/:id", h.ViewPost)
	router.GET("/create", h.CreatePost)
	router.GET("/edit/:id", h.EditPost)
	router.POST("/save", h.SavePost)
	router.GET("/delete/:id", h.DeletePost)

	log.Println("Server starting on :8080...")
	router.Run(":8080")
}
```

Le code ci-dessus configure la connexion MongoDB, initialise le routeur Gin et enregistre vos routes.

### Créer les modèles HTML

Maintenant, créez les modèles HTML pour afficher l'interface utilisateur du blog.

Tout d'abord, créez un répertoire `templates` et ajoutez les fichiers suivants :

#### index.html :

```xml
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <meta name="viewport" content="width=device-width, initial-scale=1.0">  
    <title>Go Blog avec MongoDB</title>  
    <script src="https://cdn.tailwindcss.com"></script>  
</head>  
<body class="bg-gray-100 min-h-screen">  
    <div class="container mx-auto px-4 py-8">  
        <header class="mb-8">  
            <h1 class="text-3xl font-bold text-center text-blue-600">Go Blog avec MongoDB</h1>  
            <div class="flex justify-center mt-4">  
                <a href="/create" class="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded">Créer un nouvel article</a>  
            </div>  
        </header>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">  
            {{range .}}  
            <div class="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow duration-300">  
                <div class="p-6">  
                    <h2 class="text-xl font-semibold mb-2 text-gray-800">{{.Title}}</h2>  
                    <p class="text-gray-600 mb-4 line-clamp-3">  
                        {{if gt (len .Content) 150}}  
                            {{slice .Content 0 150}}...  
                        {{else}}  
                            {{.Content}}  
                        {{end}}  
                    </p>  
                    <div class="flex justify-between items-center text-sm text-gray-500">  
                        <span>{{.CreatedAt.Format "Jan 02, 2006"}}</span>  
                        <a href="/post/{{.ID.Hex}}" class="text-blue-500 hover:text-blue-700">Lire la suite</a>  
                    </div>  
                </div>  
                <div class="flex border-t border-gray-200">  
                    <a href="/edit/{{.ID.Hex}}" class="w-1/2 py-2 text-center text-sm text-gray-600 hover:bg-gray-100 border-r border-gray-200">Modifier</a>  
                    <a href="/delete/{{.ID.Hex}}" class="w-1/2 py-2 text-center text-sm text-red-600 hover:bg-gray-100" onclick="return confirm('Êtes-vous sûr de vouloir supprimer cet article ?')">Supprimer</a>  
                </div>  
            </div>  
            {{else}}  
            <div class="col-span-3 text-center py-12">  
                <p class="text-gray-600 text-lg">Aucun article pour le moment. <a href="/create" class="text-blue-500 hover:underline">Créez-en un</a> !</p>  
            </div>  
            {{end}}  
        </div>  
    </div>  
</body>  
</html>  
```

Ce modèle liste tous les articles de blog et inclut des boutons pour créer, modifier ou supprimer des articles.

#### post.html :

```xml
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <meta name="viewport" content="width=device-width, initial-scale=1.0">  
    <title>{{.Title}} | Go Blog avec MongoDB</title>  
    <script src="https://cdn.tailwindcss.com"></script>  
</head>  
<body class="bg-gray-100 min-h-screen">  
    <div class="container mx-auto px-4 py-8">  
        <header class="mb-8">  
            <h1 class="text-3xl font-bold text-center text-blue-600">Go Blog avec MongoDB</h1>  
            <div class="flex justify-center mt-4">  
                <a href="/" class="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded">Retour à l'accueil</a>  
            </div>  
        </header>

        <div class="max-w-3xl mx-auto bg-white rounded-lg shadow-md overflow-hidden">  
            <div class="p-6">  
                <h2 class="text-2xl font-bold mb-4 text-gray-800">{{.Title}}</h2>  
                  
                <div class="flex items-center text-sm text-gray-500 mb-6">  
                    <span>Publié : {{.CreatedAt.Format "Jan 02, 2006"}}</span>  
                    {{if ne .CreatedAt .UpdatedAt}}  
                    <span class="mx-2"></span>  
                    <span>Mis à jour : {{.UpdatedAt.Format "Jan 02, 2006"}}</span>  
                    {{end}}  
                </div>  
                  
                <div class="prose max-w-none">  
                    <p class="text-gray-700 whitespace-pre-line">{{.Content}}</p>  
                </div>  
            </div>  
              
            <div class="flex border-t border-gray-200">  
                <a href="/edit/{{.ID.Hex}}" class="w-1/2 py-3 text-center text-blue-600 hover:bg-gray-100 border-r border-gray-200">Modifier l'article</a>  
                <a href="/delete/{{.ID.Hex}}" class="w-1/2 py-3 text-center text-red-600 hover:bg-gray-100" onclick="return confirm('Êtes-vous sûr de vouloir supprimer cet article ?')">Supprimer l'article</a>  
            </div>  
        </div>  
    </div>  
</body>  
</html> 
```

Ce modèle affiche un seul article.

#### create.html :

```xml
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <meta name="viewport" content="width=device-width, initial-scale=1.0">  
    <title>Créer un nouvel article | Go Blog avec MongoDB</title>  
    <script src="https://cdn.tailwindcss.com"></script>  
</head>  
<body class="bg-gray-100 min-h-screen">  
    <div class="container mx-auto px-4 py-8">  
        <header class="mb-8">  
            <h1 class="text-3xl font-bold text-center text-blue-600">Go Blog avec MongoDB</h1>  
            <div class="flex justify-center mt-4">  
                <a href="/" class="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded">Retour à l'accueil</a>  
            </div>  
        </header>

        <div class="max-w-2xl mx-auto bg-white rounded-lg shadow-md overflow-hidden">  
            <div class="p-6">  
                <h2 class="text-2xl font-bold mb-6 text-gray-800">Créer un nouvel article</h2>  
                  
                <form action="/save" method="POST">  
                    <div class="mb-4">  
                        <label for="title" class="block text-gray-700 font-medium mb-2">Titre</label>  
                        <input type="text" id="title" name="title" required  
                            class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500">  
                    </div>  
                      
                    <div class="mb-6">  
                        <label for="content" class="block text-gray-700 font-medium mb-2">Contenu</label>  
                        <textarea id="content" name="content" rows="10" required  
                            class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"></textarea>  
                    </div>  
                      
                    <div class="flex justify-end">  
                        <button type="submit" class="bg-blue-500 hover:bg-blue-600 text-white px-6 py-2 rounded-md">  
                            Enregistrer l'article  
                        </button>  
                    </div>  
                </form>  
            </div>  
        </div>  
    </div>  
</body>  
</html>  
```

Ce modèle vous permet de créer un nouvel article.

#### edit.html :

```xml
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <meta name="viewport" content="width=device-width, initial-scale=1.0">  
    <title>Modifier l'article | Go Blog avec MongoDB</title>  
    <script src="https://cdn.tailwindcss.com"></script>  
</head>  
<body class="bg-gray-100 min-h-screen">  
    <div class="container mx-auto px-4 py-8">  
        <header class="mb-8">  
            <h1 class="text-3xl font-bold text-center text-blue-600">Go Blog avec MongoDB</h1>  
            <div class="flex justify-center mt-4">  
                <a href="/" class="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded">Retour à l'accueil</a>  
            </div>  
        </header>

        <div class="max-w-2xl mx-auto bg-white rounded-lg shadow-md overflow-hidden">  
            <div class="p-6">  
                <h2 class="text-2xl font-bold mb-6 text-gray-800">Modifier l'article</h2>  
                  
                <form action="/save" method="POST">  
                    <input type="hidden" name="id" value="{{.ID.Hex}}">  
                      
                    <div class="mb-4">  
                        <label for="title" class="block text-gray-700 font-medium mb-2">Titre</label>  
                        <input type="text" id="title" name="title" value="{{.Title}}" required  
                            class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500">  
                    </div>  
                      
                    <div class="mb-6">  
                        <label for="content" class="block text-gray-700 font-medium mb-2">Contenu</label>  
                        <textarea id="content" name="content" rows="10" required  
                            class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500">{{.Content}}</textarea>  
                    </div>  
                      
                    <div class="flex justify-between">  
                        <a href="/post/{{.ID.Hex}}" class="text-gray-600 hover:text-gray-800">Annuler</a>  
                        <button type="submit" class="bg-blue-500 hover:bg-blue-600 text-white px-6 py-2 rounded-md">  
                            Mettre à jour l'article  
                        </button>  
                    </div>  
                </form>  
            </div>  
        </div>  
    </div>  
</body>  
</html>  
```

Ce modèle est utilisé pour modifier un article.

### Créer les gestionnaires

Ensuite, configurez les gestionnaires pour se connecter à MongoDB et rendre les modèles. Créez un nouveau dossier appelé `handlers` dans le répertoire racine de votre projet, puis ajoutez un fichier `main.go` à l'intérieur et insérez le code suivant :

```go
package handlers

import (
	"context"
	"log"
	"net/http"
	"time"

	"github.com/gin-gonic/gin"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/bson/primitive"
	"go.mongodb.org/mongo-driver/mongo"
)

type Post struct {
	ID        primitive.ObjectID `bson:"_id,omitempty" json:"id"`
	Title     string             `bson:"title" json:"title"`
	Content   string             `bson:"content" json:"content"`
	CreatedAt time.Time          `bson:"created_at" json:"created_at"`
	UpdatedAt time.Time          `bson:"updated_at" json:"updated_at"`
}

type Handler struct {
	db         *mongo.Database
	collection *mongo.Collection
}

func NewHandler(db *mongo.Database) *Handler {
	return &Handler{
		db:         db,
		collection: db.Collection("posts"),
	}
}

func (h *Handler) HomePage(c *gin.Context) {
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	cursor, err := h.collection.Find(ctx, bson.M{})
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	defer cursor.Close(ctx)

	var posts []Post
	if err = cursor.All(ctx, &posts); err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}

	c.HTML(http.StatusOK, "index.html", posts)
}

func (h *Handler) ViewPost(c *gin.Context) {
	id := c.Param("id")
	objID, err := primitive.ObjectIDFromHex(id)
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "Invalid post ID"})
		return
	}

	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	var post Post
	err = h.collection.FindOne(ctx, bson.M{"_id": objID}).Decode(&post)
	if err != nil {
		c.JSON(http.StatusNotFound, gin.H{"error": "Post not found"})
		return
	}

	c.HTML(http.StatusOK, "post.html", post)
}

func (h *Handler) CreatePost(c *gin.Context) {
	c.HTML(http.StatusOK, "create.html", nil)
}

func (h *Handler) EditPost(c *gin.Context) {
	id := c.Param("id")
	objID, err := primitive.ObjectIDFromHex(id)
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "Invalid post ID"})
		return
	}

	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	var post Post
	err = h.collection.FindOne(ctx, bson.M{"_id": objID}).Decode(&post)
	if err != nil {
		c.JSON(http.StatusNotFound, gin.H{"error": "Post not found"})
		return
	}

	c.HTML(http.StatusOK, "edit.html", post)
}

func (h *Handler) SavePost(c *gin.Context) {
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	id := c.PostForm("id")
	title := c.PostForm("title")
	content := c.PostForm("content")

	now := time.Now()

	if id == "" {
		post := Post{
			Title:     title,
			Content:   content,
			CreatedAt: now,
			UpdatedAt: now,
		}

		result, err := h.collection.InsertOne(ctx, post)
		if err != nil {
			c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
			return
		}

		log.Printf("Created post with ID: %v\n", result.InsertedID)
	} else {
		objID, err := primitive.ObjectIDFromHex(id)
		if err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": "Invalid post ID"})
			return
		}

		update := bson.M{
			"$set": bson.M{
				"title":      title,
				"content":    content,
				"updated_at": now,
			},
		}

		result, err := h.collection.UpdateOne(ctx, bson.M{"_id": objID}, update)
		if err != nil {
			c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
			return
		}

		log.Printf("Updated post with ID: %s (Modified %d documents)\n", id, result.ModifiedCount)
	}

	c.Redirect(http.StatusSeeOther, "/")
}

func (h *Handler) DeletePost(c *gin.Context) {
	id := c.Param("id")
	objID, err := primitive.ObjectIDFromHex(id)
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "Invalid post ID"})
		return
	}

	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	result, err := h.collection.DeleteOne(ctx, bson.M{"_id": objID})
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}

	log.Printf("Deleted %d document(s) with ID: %s\n", result.DeletedCount, id)
	c.Redirect(http.StatusSeeOther, "/")
}
```

Le code ci-dessus contient toute la logique pour gérer les articles de blog. Voici ce que fait chaque composant :

* **Struct Post :** Définit la structure d'un document d'article de blog avec des champs pour l'ID, le titre, le contenu et les horodatages. Les balises `bson` spécifient comment les champs sont stockés dans MongoDB, tandis que les balises `json` gèrent la sérialisation JSON.
    
* **Struct Handler :** Contient une référence à la base de données MongoDB et à la collection des articles, fournissant un moyen centralisé d'accéder à la base de données dans vos gestionnaires.
    
* **Fonction NewHandler :** Crée et initialise une nouvelle instance de gestionnaire avec la connexion à la base de données et configure la référence à la collection des articles.
    
* **HomePage :** Récupère tous les articles de blog de la base de données en utilisant `Find()` avec un filtre vide et les affiche en utilisant le modèle `index.html`.
    
* **ViewPost :** Récupère un seul article par son ObjectID en utilisant `FindOne()` et l'affiche avec le modèle `post.html`.
    
* **CreatePost & EditPost :** Affichent les formulaires respectifs pour créer de nouveaux articles ou modifier des articles existants.
    
* **SavePost :** Gère à la fois la création de nouveaux articles et la mise à jour d'articles existants. Il vérifie si un ID est fourni. Si ce n'est pas le cas, il crée un nouvel article en utilisant `InsertOne()`. Sinon, il met à jour l'article existant en utilisant `UpdateOne()` avec l'opérateur `$set` de MongoDB.
    
* **DeletePost :** Supprime un article de la base de données en utilisant `DeleteOne()` et redirige vers la page d'accueil.
    

### Exécuter l'application

Avec tout configuré, vous pouvez maintenant lancer votre blog. Ouvrez votre terminal et exécutez :

```bash
go mod tidy && go run main.go
```

Ensuite, visitez [http://localhost:8080](http://localhost:8080) dans votre navigateur pour voir votre blog en action.

![Interface de gestion de blog avec un en-tête "Go Blog avec MongoDB" et un bouton "Créer un nouvel article". Deux entrées d'articles de blog sont affichées avec des options pour modifier ou supprimer.](https://cdn.hashnode.com/res/hashnode/image/upload/v1753561817087/0e48d3d1-a6c0-4c5d-9245-cd6e86cd8596.png align="center")

## C'est ainsi qu'on utilise MongoDB avec Go

Dans ce tutoriel, vous avez construit une simple application de blog en utilisant Go et MongoDB. Vous avez appris à vous connecter à une base de données MongoDB en utilisant le pilote officiel Go, à effectuer des opérations CRUD et à afficher vos résultats avec le framework web Gin.

La structure flexible et basée sur les documents de MongoDB en fait un excellent choix pour les applications où les modèles de données doivent évoluer au fil du temps. Elle vous permet d'itérer rapidement et de vous adapter à mesure que votre application grandit.

Alors que vous développez ce projet, envisagez d'ajouter des fonctionnalités telles que l'authentification des utilisateurs, l'étiquetage ou la catégorisation, les commentaires, la pagination ou la fonctionnalité de recherche pour améliorer l'expérience utilisateur.

À la vôtre pour construire davantage avec Go et MongoDB !