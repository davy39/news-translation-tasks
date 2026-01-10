---
title: Comment créer une application web avec Go, Gin et React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-08T18:56:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-web-app-with-go-gin-and-react-cffdc473576
coverImage: https://cdn-media-1.freecodecamp.org/images/1*zGDYRCxNPHUPcTowYotCdQ.png
tags:
- name: Apps
  slug: apps-tag
- name: golang
  slug: golang
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment créer une application web avec Go, Gin et React
seo_desc: 'By Francis Sunday


  This article was originally posted on My Blog


  TL;DR: In this tutorial, I’ll show you how easy it is to build a web application
  with Go and the Gin framework and add authentication to it. Check out the Github
  repo for the code we’r...'
---

Par Francis Sunday

> _Cet article a été initialement publié sur [Mon Blog](https://hakaselogs.me/2018-04-20/building-a-web-app-with-go-gin-and-react)_

**TL;DR :** Dans ce tutoriel, je vais vous montrer à quel point il est facile de créer une application web avec Go et le framework Gin, et d'y ajouter une authentification. Consultez le dépôt Github [repo](https://github.com/codehakase/golang-gin) pour le code que nous allons écrire.

**Gin** est un micro-framework haute performance. Il offre un framework très minimaliste qui ne contient que les fonctionnalités, bibliothèques et fonctionnalités essentielles nécessaires pour construire des applications web et des microservices. Il simplifie la création d'un pipeline de gestion des requêtes à partir de pièces modulaires et réutilisables. Il le fait en vous permettant d'écrire des middlewares qui peuvent être intégrés à un ou plusieurs gestionnaires de requêtes ou groupes de gestionnaires de requêtes.

### Fonctionnalités de Gin

Gin est un framework web rapide, simple mais complet et très efficace pour Go. Découvrez quelques-unes des fonctionnalités ci-dessous qui en font un framework digne d'être considéré pour votre prochain projet Golang.

* **Vitesse :** Gin est conçu pour la vitesse. Le framework offre un routage basé sur un arbre Radix et une faible empreinte mémoire. Pas de réflexion. Performances API prévisibles.
* **Sans plantage :** Gin a la capacité de capturer les plantages ou les paniques pendant l'exécution et peut s'en remettre. Ainsi, votre application sera toujours disponible.
* **Routage :** Gin fournit une interface de routage pour vous permettre d'exprimer comment les routes de votre application web ou API doivent être définies.
* **Validation JSON :** Gin peut analyser et valider facilement les requêtes JSON, en vérifiant l'existence des valeurs requises.
* **Gestion des erreurs :** Gin fournit un moyen pratique de collecter toutes les erreurs survenues lors d'une requête HTTP. Finalement, un middleware peut les écrire dans un fichier journal ou dans une base de données et les envoyer via le réseau.
* **Rendu intégré :** Gin fournit une API facile à utiliser pour le rendu JSON, XML et HTML.

### Prérequis

Pour suivre ce tutoriel, vous devrez avoir Go installé sur votre machine, un navigateur web pour visualiser l'application et une ligne de commande pour exécuter les commandes de construction.

**Go**, ou comme on l'appelle normalement **Golang**, est un langage de programmation développé par Google pour construire des logiciels modernes. Go est un langage conçu pour accomplir les tâches efficacement et rapidement. Les principaux avantages de Go incluent :

* Typage fort et garbage collection
* Temps de compilation ultra-rapides
* Concurrence intégrée
* Bibliothèque standard étendue

Rendez-vous sur la [section des téléchargements](https://golang.org/dl/) du site Go pour faire fonctionner Go sur votre machine.

### Construire une application avec Gin

Nous allons construire une application simple de liste de blagues avec **Gin**. Notre application listera quelques blagues de papa idiotes. Nous allons y ajouter une authentification, de sorte que tous les utilisateurs connectés auront le privilège d'aimer et de visualiser les blagues.

Cela nous permettra d'illustrer comment **Gin** peut être utilisé pour développer des applications web et/ou des API.

![Image](https://cdn-media-1.freecodecamp.org/images/7Nra6OXJG7Xclu5Gj2wPu2Kw2-vzbeKmLi4t)

Nous allons utiliser les fonctionnalités suivantes offertes par Gin :

* Middleware
* Routage
* Groupement de routes

### Prêt, à vos marques, Go

Nous allons écrire toute notre application Go dans un fichier `main.go`. Puisqu'il s'agit d'une petite application, il sera facile de construire l'application avec simplement `go run` depuis le terminal.

Nous allons créer un nouveau répertoire `golang-gin` dans notre espace de travail Go, puis un fichier `main.go` dedans :

```bash
$ mkdir -p $GOPATH/src/github.com/user/golang-gin
$ cd $GOPATH/src/github.com/user/golang-gin
$ touch main.go
```

Le contenu du fichier `main.go` :

```go
package main

import (
  "net/http"
  
  "github.com/gin-gonic/contrib/static"
  "github.com/gin-gonic/gin"
)

func main() {
  // Définir le routeur comme celui par défaut fourni avec Gin
  router := gin.Default()
  
  // Servir les fichiers statiques du frontend
  router.Use(static.Serve("/", static.LocalFile("./views", true)))
  
  // Configurer le groupe de routes pour l'API
  api := router.Group("/api")
  {
    api.GET("/", func(c *gin.Context) {
      c.JSON(http.StatusOK, gin.H {
        "message": "pong",
      })
    })
  }
  
  // Démarrer et exécuter le serveur
  router.Run(":3000")
}
```

Nous allons devoir créer quelques répertoires supplémentaires pour nos fichiers statiques. Dans le même répertoire que le fichier `main.go`, créons un dossier `views`. Dans le dossier `views`, créons un dossier `js` et un fichier `index.html` dedans.

Le fichier `index.html` sera très simple pour l'instant :

```html
<!DOCTYPE html>
<html>
<head>
  <title>Application Jokeish</title>
</head>

<body>
  <h1>Bienvenue sur l'application Jokeish</h1>
</body>
</html>
```

Avant de tester ce que nous avons jusqu'à présent, installons les dépendances ajoutées :

```bash
$ go get -u github.com/gin-gonic/gin
$ go get -u github.com/gin-gonic/contrib/static
```

Pour voir ce qui fonctionne, nous allons devoir démarrer notre serveur en exécutant `go run main.go`.

![Image](https://cdn-media-1.freecodecamp.org/images/YAkgbEcEk3EtY88NG37K3HbT3RRmlOxVFZCO)

Une fois l'application en cours d'exécution, naviguez vers `http://localhost:3000` dans votre navigateur. Si tout s'est bien passé, vous devriez voir le texte d'en-tête de niveau 1 **Bienvenue sur l'application Jokeish** affiché.

![Image](https://cdn-media-1.freecodecamp.org/images/9qq45GU1MjZoqb1qEQ9mw67ENOS8df55zuzW)

### Définition de l'API

Ajoutons un peu plus de code dans notre fichier `main.go` pour nos définitions d'API. Nous allons mettre à jour notre fonction `main` avec deux routes `/jokes/` et `/jokes/like/:jokeID` dans le groupe de routes `/api/`.

```go
func main() {
  // ... laissez le code ci-dessus intact...
  
  // Notre API consistera en seulement deux routes
  // /jokes - qui récupérera une liste de blagues qu'un utilisateur peut voir
  // /jokes/like/:jokeID - qui capturera les likes envoyés à une blague particulière
  api.GET("/jokes", JokeHandler)
  api.POST("/jokes/like/:jokeID", LikeJoke)
}

// JokeHandler récupère une liste de blagues disponibles
func JokeHandler(c *gin.Context) {
  c.Header("Content-Type", "application/json")
  c.JSON(http.StatusOK, gin.H {
    "message":"Gestionnaire de blagues non implémenté",
  })
}

// LikeJoke incrémente les likes d'une blague particulière
func LikeJoke(c *gin.Context) {
  c.Header("Content-Type", "application/json")
  c.JSON(http.StatusOK, gin.H {
    "message":"Gestionnaire LikeJoke non implémenté",
  })
}
```

Le contenu du fichier `main.go` devrait ressembler à ceci :

```go
package main

import (
  "net/http"
  
  "github.com/gin-gonic/contrib/static"
  "github.com/gin-gonic/gin"
)

func main() {
  // Définir le routeur comme celui par défaut fourni avec Gin
  router := gin.Default()
  
  // Servir les fichiers statiques du frontend
  router.Use(static.Serve("/", static.LocalFile("./views", true)))
  
  // Configurer le groupe de routes pour l'API
  api := router.Group("/api")
  {
    api.GET("/", func(c *gin.Context) {
      c.JSON(http.StatusOK, gin.H {
        "message": "pong",
      })
    })
  }
  // Notre API consistera en seulement deux routes
  // /jokes - qui récupérera une liste de blagues qu'un utilisateur peut voir
  // /jokes/like/:jokeID - qui capturera les likes envoyés à une blague particulière
  api.GET("/jokes", JokeHandler)
  api.POST("/jokes/like/:jokeID", LikeJoke)
  
  // Démarrer et exécuter le serveur
  router.Run(":3000")
}

// JokeHandler récupère une liste de blagues disponibles
func JokeHandler(c *gin.Context) {
  c.Header("Content-Type", "application/json")
  c.JSON(http.StatusOK, gin.H {
    "message":"Gestionnaire de blagues non implémenté",
  })
}

// LikeJoke incrémente les likes d'une blague particulière
func LikeJoke(c *gin.Context) {
  c.Header("Content-Type", "application/json")
  c.JSON(http.StatusOK, gin.H {
    "message":"Gestionnaire LikeJoke non implémenté",
  })
}
```

Exécutons notre application à nouveau `go run main.go`, et accédons à nos routes. `http://localhost:3000/api/jokes` retournera une réponse d'en-tête `200 OK`, avec le message `gestionnaire de blagues non implémenté`. Une requête POST à `http://localhost:3000/api/jokes/like/1` retourne un en-tête `200 OK`, et le message `gestionnaire LikeJoke non implémenté`.

### Données des blagues

Puisque nous avons déjà notre définition de routes en place, qui ne fait qu'une seule chose (retourner une réponse JSON), nous allons enrichir notre base de code en y ajoutant un peu plus de code.

```go
// ... laissez le code ci-dessus intact...

// Créons notre structure Jokes. Cela contiendra des informations sur une blague

// Joke contient des informations sur une seule blague
type Joke struct {
  ID     int     `json:"id" binding:"required"`
  Likes  int     `json:"likes"`
  Joke   string  `json:"joke" binding:"required"`
}

// Nous allons créer une liste de blagues
var jokes = []Joke{
  Joke{1, 0, "Did you hear about the restaurant on the moon? Great food, no atmosphere."},
  Joke{2, 0, "What do you call a fake noodle? An Impasta."},
  Joke{3, 0, "How many apples grow on a tree? All of them."},
  Joke{4, 0, "Want to hear a joke about paper? Nevermind it's tearable."},
  Joke{5, 0, "I just watched a program about beavers. It was the best dam program I've ever seen."},
  Joke{6, 0, "Why did the coffee file a police report? It got mugged."},
  Joke{7, 0, "How does a penguin build it's house? Igloos it together."},
}

func main() {
  // ... laissez ce bloc intact...
}

// JokeHandler récupère une liste de blagues disponibles
func JokeHandler(c *gin.Context) {
  c.Header("Content-Type", "application/json")
  c.JSON(http.StatusOK, jokes)
}

// LikeJoke incrémente les likes d'une blague particulière
func LikeJoke(c *gin.Context) {
  // confirmer que l'ID de la blague envoyé est valide
  // n'oubliez pas d'importer le package `strconv`
  if jokeid, err := strconv.Atoi(c.Param("jokeID")); err == nil {
    // trouver la blague et incrémenter les likes
    for i := 0; i < len(jokes); i++ {
      if jokes[i].ID == jokeid {
        jokes[i].Likes += 1
      }
    }
    // retourner un pointeur vers la liste de blagues mise à jour
    c.JSON(http.StatusOK, &jokes)
  } else {
    // L'ID de la blague est invalide
    c.AbortWithStatus(http.StatusNotFound)
  }
}

// NB: Remplacez les fonctions JokeHandler et LikeJoke dans la version précédente par celles ci-dessus
```

Avec notre code qui a l'air bien, allons-y et testons notre API. Nous pouvons tester avec `cURL` ou `postman`, puis envoyer une requête `GET` à `http://localhost:3000/jokes` pour obtenir la liste complète des blagues, et une requête `POST` à `http://localhost:3000/jokes/like/{jokeid}` pour incrémenter les likes d'une blague.

```bash
$ curl http://localhost:3000/api/jokes

$ curl -X POST http://localhost:3000/api/jokes/like/4
```

### Construction de l'interface utilisateur (React)

Nous avons notre API en place, alors construisons un frontend pour présenter les données de notre API. Pour cela, nous allons utiliser React. Nous n'irons pas trop loin dans React, car cela serait hors du cadre de ce tutoriel. Si vous devez en apprendre plus sur React, consultez le tutoriel officiel [tutoriel](https://facebook.github.io/react/docs/tutorial.html). Vous pouvez implémenter l'interface utilisateur avec n'importe quel framework frontend avec lequel vous êtes à l'aise.

### Configuration

Nous allons modifier le fichier `index.html` pour ajouter les bibliothèques externes nécessaires à l'exécution de React. Ensuite, nous devrons créer un fichier `app.jsx` dans le répertoire `views/js`, qui contiendra notre code React.

Notre fichier `index.html` devrait ressembler à ceci :

```html
<!DOCTYPE html>
<html>

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
  <title>Application Jokeish</title>
  <script src="http://code.jquery.com/jquery-2.1.4.min.js"></script>
  <script src="https://cdn.auth0.com/js/auth0/9.0/auth0.min.js"></script>
  <script type="application/javascript" src="https://unpkg.com/react@16.0.0/umd/react.production.min.js"></script>
  <script type="application/javascript" src="https://unpkg.com/react-dom@16.0.0/umd/react-dom.production.min.js"></script>
  <script type="application/javascript" src="https://unpkg.com/babel-standalone@6.26.0/babel.js"></script>
  <script type="text/babel" src="js/app.jsx"></script>
  <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet">
</head>

<body>
  <div id="app"></div>
</body>

</html>
```

### Construction de nos composants

Dans React, les vues sont décomposées en composants. Nous allons devoir construire quelques composants :

* un composant `App` comme point d'entrée principal qui lance l'application
* un composant `Home` qui fera face aux utilisateurs non connectés
* un composant `LoggedIn` avec du contenu visible uniquement par les utilisateurs authentifiés
* et un composant `Joke` pour afficher une liste de blagues.

Nous allons écrire tous ces composants dans le fichier `app.jsx`.

### Le composant App

Ce composant initialise toute notre application React. Il décide quel composant afficher en fonction de si un utilisateur est authentifié ou non. Nous allons commencer par sa base, et le mettre à jour plus tard avec plus de fonctionnalités.

```js
class App extends React.Component {
  render() {
    if (this.loggedIn) {
      return (<LoggedIn />);
    } else {
      return (<Home />);
    }
  }
}
```

### Le composant Home

Ce composant est affiché aux utilisateurs non connectés, avec un bouton qui ouvre un écran de verrouillage hébergé où ils peuvent s'inscrire ou se connecter. Nous ajouterons cette fonctionnalité plus tard.

```js
class Home extends React.Component {
  render() {
    return (
      <div className="container">
        <div className="col-xs-8 col-xs-offset-2 jumbotron text-center">
          <h1>Jokeish</h1>
          <p>Une charge de blagues de papa XD</p>
          <p>Connectez-vous pour obtenir l'accès</p>
          <a onClick={this.authenticate} className="btn btn-primary btn-lg btn-login btn-block">Se connecter</a>
        </div>
      </div>
    )
  }
}
```

### Composant LoggedIn

Ce composant est affiché lorsqu'un utilisateur est authentifié. Il stocke dans son `state` un tableau de blagues qui est peuplé lorsque le composant est monté.

```js
class LoggedIn extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      jokes: []
    }
  }
    
  render() {
    return (
      <div className="container">
        <div className="col-lg-12">
          <br />
          <span className="pull-right"><a onClick={this.logout}>Se déconnecter</a></span>
          <h2>Jokeish</h2>
          <p>Laissez-nous vous nourrir avec quelques blagues drôles !!!</p>
          <div className="row">
            {this.state.jokes.map(function(joke, i){
              return (<Joke key={i} joke={joke} />);
            })}
          </div>
        </div>
      </div>
    )
  }
}
```

### Le composant Joke

Le composant `Joke` contiendra des informations sur chaque élément de la réponse des blagues à afficher.

```js
class Joke extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      liked: ""
    }
    this.like = this.like.bind(this);
  }
    
  like() {
    // ... nous ajouterons ce bloc plus tard
  }
    
  render() {
    return (
      <div className="col-xs-4">
        <div className="panel panel-default">
          <div className="panel-heading">#{this.props.joke.id} <span className="pull-right">{this.state.liked}</span></div>
          <div className="panel-body">
            {this.props.joke.joke}
          </div>
          <div className="panel-footer">
            {this.props.joke.likes} Likes &nbsp;
            <a onClick={this.like} className="btn btn-default">
              <span className="glyphicon glyphicon-thumbs-up"></span>
            </a>
          </div>
        </div>
      </div>
    )
  }
}
```

Nous avons écrit nos composants, alors maintenant disons à React où rendre l'application. Nous allons ajouter le bloc de code ci-dessous au bas de notre fichier `app.jsx`.

```jsx
ReactDOM.render(<App />, document.getElementById('app'));
```

Redémarrons notre serveur Go `go run main.go`, et dirigeons-nous vers l'URL de notre application `http://localhost:3000/`. Vous verrez que le composant `Home` est rendu.

![Image](https://cdn-media-1.freecodecamp.org/images/P7w0V1mvGnYEMn4zyg8gUVjo-VEwt0o3Aizk)

### Sécuriser notre application de blagues avec Auth0

**Auth0** émet des [JSON Web Tokens](https://jwt.io/) à chaque connexion pour vos utilisateurs. Cela signifie que vous pouvez avoir une infrastructure d'identité solide, incluant [single sign-on](https://auth0.com/docs/sso/single-sign-on), la gestion des utilisateurs, la prise en charge des fournisseurs d'identité sociaux (Facebook, Github, Twitter, etc.), des fournisseurs d'identité d'entreprise (Active Directory, LDAP, SAML, etc.) et votre propre base de données d'utilisateurs, avec seulement quelques lignes de code.

Nous pouvons facilement configurer l'authentification dans notre application GIN en utilisant Auth0. Vous aurez besoin d'un compte pour suivre cette partie. Si vous n'avez pas déjà un compte Auth0, [inscrivez-vous](https://auth0.com/signup) pour en obtenir un maintenant.

> _Avis de non-responsabilité : Ce n'est pas du contenu sponsorisé._

### Création du client API

Nos jetons seront générés avec Auth0, nous devons donc créer une API et un Client depuis notre tableau de bord Auth0. Encore une fois, si vous ne l'avez pas déjà fait, [inscrivez-vous](https://auth0.com/signup) pour un compte Auth0.

Pour créer une nouvelle API, naviguez vers la [section APIs](https://manage.auth0.com/#/apis) dans votre tableau de bord, et cliquez sur le bouton **Créer une API**.

![Image](https://cdn-media-1.freecodecamp.org/images/zXJ6LA97EnrucoDyHBaSuib1wmQIFSx2nxEd)

Choisissez un **nom** d'API et un **identifiant**. L'identifiant sera l'**audience** pour le middleware. L'**algorithme de signature** doit être **RS256**.

Pour créer un nouveau Client, naviguez vers la [section clients](https://dev.to/codehakase/building-a-web-app-with-go-gin-and-react-5ke) dans votre tableau de bord, et cliquez sur le bouton **Créer un Client**. Sélectionnez le type `Applications Web Régulières`.

![Image](https://cdn-media-1.freecodecamp.org/images/mZD-PjRnzz7HiNiTTHZS2DaunCn4tYGsqBBE)

Une fois le client créé, notez le `client_id` et le `client_secret`, car nous en aurons besoin plus tard.

![Image](https://cdn-media-1.freecodecamp.org/images/otrwgdfP2KzrLo6lqndrcJdijYnVmffmtWfJ)

Nous devons ajouter les informations d'identification nécessaires pour notre API à une variable d'environnement. Dans le répertoire racine, créez un nouveau fichier `.env` et ajoutez-y ce qui suit, avec les détails du tableau de bord Auth0 :

```
export AUTH0_API_CLIENT_SECRET=""
export AUTH0_CLIENT_ID=""
export AUTH0_DOMAIN="votredomaine.auth0.com"
export AUTH0_API_AUDIENCE=""
```

### Sécurisation de nos points de terminaison API

Actuellement, notre API est ouverte au monde. Nous devons sécuriser nos points de terminaison, de sorte que seuls les utilisateurs autorisés puissent y accéder.

Nous allons utiliser un **JWT Middleware** pour vérifier la présence d'un **JSON Web Token** valide pour chaque requête atteignant nos points de terminaison.

Créons notre middleware :

```js
// ...

var jwtMiddleWare *jwtmiddleware.JWTMiddleware

func main() {
  jwtMiddleware := jwtmiddleware.New(jwtmiddleware.Options{
    ValidationKeyGetter: func(token *jwt.Token) (interface{}, error) {
      aud := os.Getenv("AUTH0_API_AUDIENCE")
      checkAudience := token.Claims.(jwt.MapClaims).VerifyAudience(aud, false)
      if !checkAudience {
        return token, errors.New("Audience invalide.")
      }
      // vérifier la revendication iss
      iss := os.Getenv("AUTH0_DOMAIN")
      checkIss := token.Claims.(jwt.MapClaims).VerifyIssuer(iss, false)
      if !checkIss {
        return token, errors.New("Émetteur invalide.")
      }
      
      cert, err := getPemCert(token)
      if err != nil {
        log.Fatalf("impossible d'obtenir le certificat : %+v", err)
      }
      
      result, _ := jwt.ParseRSAPublicKeyFromPEM([]byte(cert))
      return result, nil
    },
    SigningMethod: jwt.SigningMethodRS256,
  })
  
  // enregistrer notre jwtMiddleware réel
  jwtMiddleWare = jwtMiddleware

  // ... le reste du code sous cette fonction ne change pas encore
}

// authMiddleware intercepte les requêtes et vérifie la présence d'un jeton jwt valide
func authMiddleware() gin.HandlerFunc {
  return func(c *gin.Context) {
    // Obtenir la clé secrète du client
    err := jwtMiddleWare.CheckJWT(c.Writer, c.Request)
    if err != nil {
      // Jeton non trouvé
      fmt.Println(err)
      c.Abort()
      c.Writer.WriteHeader(http.StatusUnauthorized)
      c.Writer.Write([]byte("Non autorisé"))
      return
    }
  }
}
```

Dans le code ci-dessus, nous avons une nouvelle variable `jwtMiddleWare` qui est initialisée dans la fonction `main`. Elle est utilisée dans la fonction intermédiaire `authMiddleware`.

Comme vous pouvez le constater, nous récupérons nos informations d'identification côté serveur à partir d'une variable d'environnement (l'un des principes d'une **application 12-factor**). Notre middleware vérifie et reçoit un jeton d'une requête et appelle la méthode `jwtMiddleWare.CheckJWT` pour valider le jeton envoyé.

Écrivons également la fonction pour retourner les clés web JSON :

```js
// ... le code ci-dessus est intact...

// Jwks stocke une tranche de clés web JSON
type Jwks struct {
  Keys []JSONWebKeys `json:"keys"`
}

type JSONWebKeys struct {
  Kty string   `json:"kty"`
  Kid string   `json:"kid"`
  Use string   `json:"use"`
  N   string   `json:"n"`
  E   string   `json:"e"`
  X5c []string `json:"x5c"`
}

func main() {
  // ... le code dans cette méthode est intact...
}

func getPemCert(token *jwt.Token) (string, error) {
  cert := ""
  resp, err := http.Get(os.Getenv("AUTH0_DOMAIN") + ".well-known/jwks.json")
  if err != nil {
    return cert, err
  }
  defer resp.Body.Close()
    
  var jwks = Jwks{}
  err = json.NewDecoder(resp.Body).Decode(&jwks)
    
  if err != nil {
    return cert, err
  }
    
  x5c := jwks.Keys[0].X5c
  for k, v := range x5c {
    if token.Header["kid"] == jwks.Keys[k].Kid {
      cert = "-----BEGIN CERTIFICATE-----\n" + v + "\n-----END CERTIFICATE-----"
    }
  }
    
  if cert == "" {
    return cert, errors.New("impossible de trouver la clé appropriée.")
  }
    
  return cert, nil
}
```

### Utilisation du middleware JWT

L'utilisation du middleware est très simple. Nous le passons simplement en tant que paramètre à notre définition de routes.

```js
...

api.GET("/jokes", authMiddleware(), JokeHandler)
api.POST("/jokes/like/:jokeID", authMiddleware(), LikeJoke)

...
```

Notre fichier `main.go` devrait ressembler à ceci :

```
package main

import (
  "encoding/json"
  "errors"
  "fmt"
  "log"
  "net/http"
  "os"
  "strconv"
  
  jwtmiddleware "github.com/auth0/go-jwt-middleware"
  jwt "github.com/dgrijalva/jwt-go"
  "github.com/gin-gonic/contrib/static"
  "github.com/gin-gonic/gin"
)

type Response struct {
  Message string `json:"message"`
}

type Jwks struct {
  Keys []JSONWebKeys `json:"keys"`
}

type JSONWebKeys struct {
  Kty string   `json:"kty"`
  Kid string   `json:"kid"`
  Use string   `json:"use"`
  N   string   `json:"n"`
  E   string   `json:"e"`
  X5c []string `json:"x5c"`
}

type Joke struct {
  ID    int    `json:"id" binding:"required"`
  Likes int    `json:"likes"`
  Joke  string `json:"joke" binding:"required"`
}

/** nous allons créer une liste de blagues */
var jokes = []Joke{
  Joke{1, 0, "Did you hear about the restaurant on the moon? Great food, no atmosphere."},
  Joke{2, 0, "What do you call a fake noodle? An Impasta."},
  Joke{3, 0, "How many apples grow on a tree? All of them."},
  Joke{4, 0, "Want to hear a joke about paper? Nevermind it's tearable."},
  Joke{5, 0, "I just watched a program about beavers. It was the best dam program I've ever seen."},
  Joke{6, 0, "Why did the coffee file a police report? It got mugged."},
  Joke{7, 0, "How does a penguin build it's house? Igloos it together."},
}

var jwtMiddleWare *jwtmiddleware.JWTMiddleware

func main() {
  jwtMiddleware := jwtmiddleware.New(jwtmiddleware.Options{
    ValidationKeyGetter: func(token *jwt.Token) (interface{}, error) {
      aud := os.Getenv("AUTH0_API_AUDIENCE")
      checkAudience := token.Claims.(jwt.MapClaims).VerifyAudience(aud, false)
      if !checkAudience {
        return token, errors.New("Audience invalide.")
      }
      // vérifier la revendication iss
      iss := os.Getenv("AUTH0_DOMAIN")
      checkIss := token.Claims.(jwt.MapClaims).VerifyIssuer(iss, false)
      if !checkIss {
        return token, errors.New("Émetteur invalide.")
      }
      
      cert, err := getPemCert(token)
      if err != nil {
        log.Fatalf("impossible d'obtenir le certificat : %+v", err)
      }
      
      result, _ := jwt.ParseRSAPublicKeyFromPEM([]byte(cert))
      return result, nil
    },  
    SigningMethod: jwt.SigningMethodRS256,
  })
  
  jwtMiddleWare = jwtMiddleware
  // Définir le routeur comme celui par défaut fourni avec Gin
  router := gin.Default()
  
  // Servir le frontend
  router.Use(static.Serve("/", static.LocalFile("./views", true)))
  
  api := router.Group("/api")
  {
    api.GET("/", func(c *gin.Context) {
      c.JSON(http.StatusOK, gin.H{
        "message": "pong",
      })
    })
    api.GET("/jokes", authMiddleware(), JokeHandler)
    api.POST("/jokes/like/:jokeID", authMiddleware(), LikeJoke)
  }
  // Démarrer l'application
  router.Run(":3000")
}

func getPemCert(token *jwt.Token) (string, error) {
  cert := ""
  resp, err := http.Get(os.Getenv("AUTH0_DOMAIN") + ".well-known/jwks.json")
  if err != nil {
    return cert, err
  }
  defer resp.Body.Close()
  
  var jwks = Jwks{}
  err = json.NewDecoder(resp.Body).Decode(&jwks)
  
  if err != nil {
    return cert, err
  }
  
  x5c := jwks.Keys[0].X5c
  for k, v := range x5c {
    if token.Header["kid"] == jwks.Keys[k].Kid {
      cert = "-----BEGIN CERTIFICATE-----\n" + v + "\n-----END CERTIFICATE-----"
    }
  }
  
  if cert == "" {
    return cert, errors.New("impossible de trouver la clé appropriée")
  }
  
  return cert, nil
}

// authMiddleware intercepte les requêtes et vérifie la présence d'un jeton jwt valide
func authMiddleware() gin.HandlerFunc {
  return func(c *gin.Context) {
    // Obtenir la clé secrète du client
    err := jwtMiddleWare.CheckJWT(c.Writer, c.Request)
    if err != nil {
      // Jeton non trouvé
      fmt.Println(err)
      c.Abort()
      c.Writer.WriteHeader(http.StatusUnauthorized)
      c.Writer.Write([]byte("Non autorisé"))
      return
    }
  }
}

// JokeHandler retourne une liste de blagues disponibles (en mémoire)
func JokeHandler(c *gin.Context) {
  c.Header("Content-Type", "application/json")
  
  c.JSON(http.StatusOK, jokes)
}

func LikeJoke(c *gin.Context) {
  // Vérifier que l'ID de la blague est valide
  if jokeid, err := strconv.Atoi(c.Param("jokeID")); err == nil {
    // trouver la blague et incrémenter les likes
    for i := 0; i < len(jokes); i++ {
      if jokes[i].ID == jokeid {
        jokes[i].Likes = jokes[i].Likes + 1
      }
    }
    c.JSON(http.StatusOK, &jokes)
  } else {
    // l'ID de la blague est invalide
    c.AbortWithStatus(http.StatusNotFound)
  }
}
```

Installons les bibliothèques `jwtmiddleware` :

```bash
$ go get -u github.com/auth0/go-jwt-middleware
$ go get -u github.com/dgrijalva/jwt-go
```

Sourçons notre fichier d'environnement et redémarrons notre serveur d'application :

```bash
$ source .env
$ go run main.go
```

Maintenant, si nous essayons d'accéder à l'un des points de terminaison, nous serons confrontés à une erreur `401 Non autorisé`. C'est parce que nous devons envoyer un jeton avec la requête.

### Connexion avec Auth0 et React

Implémentons un système de connexion afin que les utilisateurs puissent se connecter ou créer des comptes et accéder à nos blagues. Nous ajouterons à notre fichier `app.jsx` les informations d'identification Auth0 suivantes :

* `AUTH0_CLIENT_ID`
* `AUTH0_DOMAIN`
* `AUTH0_CALLBACK_URL` - L'URL de votre application
* `AUTH0_API_AUDIENCE`

> _Vous pouvez trouver les données `AUTH0_CLIENT_ID`, `AUTH0_DOMAIN` et `AUTH0_API_AUDIENCE` depuis votre tableau de bord de gestion Auth0 [management dashboard](https://manage.auth0.com/)._

Nous devons définir un `callback` vers lequel Auth0 redirige. Naviguez vers la section Clients dans votre tableau de bord. Dans les paramètres, définissons le callback à `[http://localhost:3000](http://localhost:3000:)`[:](http://localhost:3000:)

![Image](https://cdn-media-1.freecodecamp.org/images/ITYOAqNxMw9pynQ8PpO6MZFfXSkf0AzH0qwy)

Avec les informations d'identification en place, mettons à jour nos composants React.

#### Composant APP

```js
const AUTH0_CLIENT_ID = "aIAOt9fkMZKrNsSsFqbKj5KTI0ObTDPP";
const AUTH0_DOMAIN = "hakaselabs.auth0.com";
const AUTH0_CALLBACK_URL = location.href;
const AUTH0_API_AUDIENCE = "golang-gin";

class App extends React.Component {
  parseHash() {
    this.auth0 = new auth0.WebAuth({
      domain: AUTH0_DOMAIN,
      clientID: AUTH0_CLIENT_ID
    });
    this.auth0.parseHash(window.location.hash, (err, authResult) => {
      if (err) {
        return console.log(err);
      }
      if (
        authResult !== null &&
        authResult.accessToken !== null &&
        authResult.idToken !== null
      ) {
        localStorage.setItem("access_token", authResult.accessToken);
        localStorage.setItem("id_token", authResult.idToken);
        localStorage.setItem(
          "profile",
          JSON.stringify(authResult.idTokenPayload)
        );
        window.location = window.location.href.substr(
          0,
          window.location.href.indexOf("#")
        );
      }
    });
  }
    
  setup() {
    $.ajaxSetup({
      beforeSend: (r) => {
        if (localStorage.getItem("access_token")) {
          r.setRequestHeader(
            "Authorization",
            "Bearer " + localStorage.getItem("access_token")
          );
        }
      }
    });
  }
  setState() {
    let idToken = localStorage.getItem("id_token");
    if (idToken) {
      this.loggedIn = true;
    } else {
      this.loggedIn = false;
    }
  }
    
  componentWillMount() {
    this.setup();
    this.parseHash();
    this.setState();
  }
    
  render() {
    if (this.loggedIn) {
      return <LoggedIn />;
    }
    return <Home />;
  }
}
```

Nous avons mis à jour le composant App avec trois méthodes de composant (`setup`, `parseHash`, et `setState`), et une méthode de cycle de vie `componentWillMount`. La méthode `parseHash` initialise le client `auth0` `webAuth` et analyse le hash dans un format plus lisible, les sauvegardant dans localSt. Pour afficher l'écran de verrouillage, capturer et stocker le jeton utilisateur et ajouter l'en-tête d'autorisation correct aux requêtes vers notre API

#### Composant Home

Notre composant Home sera mis à jour. Nous allons ajouter la fonctionnalité pour la méthode `authenticate`, qui déclenchera l'écran de verrouillage hébergé pour s'afficher et permettre à nos utilisateurs de se connecter ou de s'inscrire.

```js
class Home extends React.Component {
  constructor(props) {
    super(props);
    this.authenticate = this.authenticate.bind(this);
  }
  authenticate() {
    this.WebAuth = new auth0.WebAuth({
      domain: AUTH0_DOMAIN,
      clientID: AUTH0_CLIENT_ID,
      scope: "openid profile",
      audience: AUTH0_API_AUDIENCE,
      responseType: "token id_token",
      redirectUri: AUTH0_CALLBACK_URL
    });
    this.WebAuth.authorize();
  }
    
  render() {
    return (
      <div className="container">
        <div className="row">
          <div className="col-xs-8 col-xs-offset-2 jumbotron text-center">
            <h1>Jokeish</h1>
            <p>Une charge de blagues de papa XD</p>
            <p>Connectez-vous pour obtenir l'accès</p>
            <a
              onClick={this.authenticate}
              className="btn btn-primary btn-lg btn-login btn-block"
            >
              Se connecter
            </a>
          </div>
        </div>
      </div>
    );
  }
}
```

#### Composant LoggedIn

Nous allons mettre à jour le composant `LoggedIn` pour communiquer avec notre API et récupérer toutes les blagues. Il passera chaque blague en tant que `prop` au composant `Joke`, qui rend un panneau bootstrap. Écrivons ceux-ci :

```js
class LoggedIn extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      jokes: []
    };
    
    this.serverRequest = this.serverRequest.bind(this);
    this.logout = this.logout.bind(this);
  }
  
  logout() {
    localStorage.removeItem("id_token");
    localStorage.removeItem("access_token");
    localStorage.removeItem("profile");
    location.reload();
  }
  
  serverRequest() {
    $.get("http://localhost:3000/api/jokes", res => {
      this.setState({
        jokes: res
      });
    });
  }
  
  componentDidMount() {
    this.serverRequest();
  }
  
  render() {
    return (
      <div className="container">
        <br />
        <span className="pull-right">
          <a onClick={this.logout}>Se déconnecter</a>
        </span>
        <h2>Jokeish</h2>
        <p>Laissez-nous vous nourrir avec quelques blagues drôles !!!</p>
        <div className="row">
          <div className="container">
            {this.state.jokes.map(function(joke, i) {
              return <Joke key={i} joke={joke} />;
            })}
          </div>
        </div>
      </div>
    );
  }
}
```

#### Composant Joke

Nous allons également mettre à jour le composant `Joke` pour formater chaque élément de blague qui lui est passé depuis le composant parent (`LoggedIn`). Nous allons également ajouter une méthode `like`, qui incrémentera les likes d'une blague.

```js
class Joke extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      liked: "",
      jokes: []
    };
    this.like = this.like.bind(this);
    this.serverRequest = this.serverRequest.bind(this);
  }
    
  like() {
    let joke = this.props.joke;
    this.serverRequest(joke);
  }
  serverRequest(joke) {
    $.post(
      "http://localhost:3000/api/jokes/like/" + joke.id,
      { like: 1 },
      res => {
        console.log("res... ", res);
        this.setState({ liked: "Aimé !", jokes: res });
        this.props.jokes = res;
      }
    );
  }
    
  render() {
    return (
      <div className="col-xs-4">
        <div className="panel panel-default">
          <div className="panel-heading">
            #{this.props.joke.id}{" "}
            <span className="pull-right">{this.state.liked}</span>
          </div>
          <div className="panel-body">{this.props.joke.joke}</div>
          <div className="panel-footer">
            {this.props.joke.likes} Likes &nbsp;
            <a onClick={this.like} className="btn btn-default">
              <span className="glyphicon glyphicon-thumbs-up" />
            </a>
          </div>
        </div>
      </div>
    )
  }
}
```

### Mettre tout ensemble

Avec l'interface utilisateur et l'API complètes, nous pouvons tester notre application. Nous allons commencer par démarrer notre serveur `source .env && go run main.go`, puis nous allons naviguer vers `http://localhost:3000` depuis n'importe quel navigateur. Vous devriez voir le composant `Home` avec un bouton de connexion. En cliquant sur le bouton de connexion, vous serez redirigé vers une page Lock hébergée (créer un compte ou se connecter) pour continuer à utiliser l'application.

**Accueil :**

![Image](https://cdn-media-1.freecodecamp.org/images/W9d1bgk2u64ER9SQob5mTU4w9Dlf4s1V6T0h)

**Écran de verrouillage hébergé par Auth0 :**

![Image](https://cdn-media-1.freecodecamp.org/images/FkPbFFEsEotY0XeARHkvtbBkdg5BL3vF3iWy)

**Vue de l'application connectée :**

![Image](https://cdn-media-1.freecodecamp.org/images/zK62YBWYnLVgsDR3DHJWEvWI3owTElvFHJmM)

### Conclusion

Félicitations ! Vous avez appris à créer une application et une API avec Go et le framework Gin.

Ai-je oublié quelque chose d'important ? Faites-le moi savoir dans les commentaires.

Vous pouvez me dire bonjour sur Twitter [@codehakase](https://twitter.com/codehakase)