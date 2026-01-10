---
title: Comment configurer un projet réel avec Go et Vue
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-18T19:48:35.000Z'
originalURL: https://freecodecamp.org/news/how-i-set-up-a-real-world-project-with-go-and-vue
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/1_9uBiGMLNlBPoNm8kmBCeYw.png
tags:
- name: Go Language
  slug: go
- name: JavaScript
  slug: javascript
seo_title: Comment configurer un projet réel avec Go et Vue
seo_desc: 'By Dirk Hoekstra

  When I first started with Go programming I found it pretty hard to get my head around
  it. It was way more low-level than anything else I had ever coded in.

  Fast forward a few months and now I''m a total fan and use it for a lot of pro...'
---

Par Dirk Hoekstra

Lorsque j'ai commencé avec la programmation Go, j'ai trouvé cela assez difficile à comprendre. C'était bien plus bas niveau que tout ce que j'avais jamais codé auparavant.

Quelques mois plus tard, je suis devenu un vrai fan et je l'utilise pour beaucoup de projets.

Dans cet article, je vais vous montrer comment je configure une application web full-stack avec Go et Vue.

Commençons !

## Ce que nous allons créer

J'ai pensé qu'il serait cool de créer un générateur de miniatures de sites web. L'idée est que vous entrez une URL de site web et l'application génère une miniature de ce site web pour vous.

## Configuration d'un module Go

Tout d'abord, je crée un nouveau répertoire. Ensuite, je configure un module Go en exécutant la commande suivante.

```
go mod init github.com/Dirk94/website-thumbnail-generator
```

Cela créera un fichier `go.mod` qui suit toutes les dépendances du module. Cela est similaire au fichier `package.json` dans un projet node.

Ensuite, je crée un nouveau répertoire `main` dans lequel j'ajoute un fichier `server.go`. Ce sera le point d'entrée principal de l'application.

Pour l'instant, imprimons simplement un message "hello world".

```go
package main

import "fmt"

func main() {
	fmt.Println("Hello world")
}
```

Pour exécuter le programme, j'exécute la commande suivante depuis le répertoire du projet.

```
go run main/server.go
Hello world
```

Super, tout fonctionne jusqu'à présent ! 🎉

## Configuration d'un serveur web

Nous devons créer un serveur web qui écoutera les requêtes entrantes.

Mettons à jour la fonction principale.

```go
func main() {
	http.HandleFunc("/", homePageHandler)

	fmt.Println("Server listening on port 3000")
	log.Panic(
		http.ListenAndServe(":3000", nil),
	)
}
```

Cela démarrera un serveur web et écoutera sur le port 3000.

Toute requête entrante sera gérée par la fonction `homePageHandler`. Celle-ci n'existe pas encore, alors créons-la.

```go
func homePageHandler(w http.ResponseWriter, r *http.Request) {
	_, err := fmt.Fprintf(w, "hello world")
	checkError(err)
}

func checkError(err error) {
	if err != nil {
		log.Panic(err)
	}
}
```

Tout ce que fait cette fonction est d'écrire "hello world" dans le `http.ResponseWriter`.

La fonction `checkError` est simplement une fonction pratique qui arrêtera le programme et imprimera une trace de la pile si l'`error` n'est pas nil.

Lorsque vous exécutez le programme, le serveur web imprime correctement le message "hello world" !

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-14-at-17.02.19.png)

## Création du projet Vue

Pour créer un nouveau projet Vue, j'exécute la commande suivante depuis le répertoire du projet.

```
vue create frontend
```

Cela crée beaucoup de fichiers, mais ne soyez pas submergé. Commençons par exécuter le serveur de développement Vue.

```
yarn serve
```

En naviguant vers localhost:8081, vous pouvez voir que l'application Vue fonctionne !

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-15-at-19.11.06.png)

D'accord, nettoyons un peu le répertoire frontend.

Pour commencer, je supprime les répertoires `assets` et `components` car je ne les utiliserai pas.

Ensuite, je mets à jour le fichier `App.vue`.

```html
<template>
  <div id="app" class="container">
    <div class="row">
      <div class="col-md-6 offset-md-3 py-5">
        <h1>Générer une miniature d'un site web</h1>

        <form v-on:submit.prevent="makeWebsiteThumbnail">
          <div class="form-group">
            <input v-model="websiteUrl" type="text" id="website-input" placeholder="Entrez une URL de site web" class="form-control">
          </div>
          <div class="form-group">
            <button class="btn btn-primary">Générer !</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
```

J'utilise la balise `v-model` et j'appelle une fonction `makeWebsiteThumbnail` lorsque le formulaire est soumis. Pour l'instant, ceux-ci n'existent pas. Ajoutons-les.

```javascript
<script>
export default {
  name: 'App',

  data() { return {
    websiteUrl: '',
  } },

  methods: {
    makeWebsiteThumbnail() {
      console.log(`Je devrais créer une miniature du site web ${this.websiteUrl}`);
    }
  }
}
</script>
```

J'utilise également quelques classes Bootstrap 4, donc pour que cela fonctionne, je dois ajouter le CSS de Bootstrap au fichier `public/index.html`.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
      
      <!--- Le reste du contenu dans la balise head ici... -->
  </head>
```

D'accord, démarrons le serveur web et vérifions si nous voyons le message de log.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-15-at-18.36.31.png)

Super, cela fonctionne ! 🎉

## Création d'une miniature de site web

Pour créer la miniature de site web, je vais utiliser [screenshotapi.net](https://screenshotapi.net). Ainsi, je n'ai qu'à appeler une API pour faire le travail difficile pour moi.

Tout d'abord, j'installe axios.

```
yarn add axios
```

Ensuite, je l'importe dans le fichier `App.vue`.

```javascript
<script>
  import axios from 'axios';
  
  export default {
    name: 'App', 
    
    // Le reste ici...
    
```

Ensuite, je mets à jour la fonction `makeWebsiteThumbnail` pour appeler réellement l'API de capture d'écran.

```javascript
makeWebsiteThumbnail() {
  axios.post("https://screenshotapi.net/api/v1/screenshot", {
    token: "SCREENSHOTAPI_TOKEN",
    url: this.websiteUrl,
    width: 1920,
    height: 1080,
    output: 'json',
    thumbnail_width: 300
  })
  .then((response) => {
    this.thumbnailUrl = response.data.screenshot;
  })
  .catch((error) => {
    window.alert(`L'API a retourné une erreur : ${error}`);
  })
}
```

Assurez-vous de remplacer `SCREENSHOTAPI_TOKEN` par votre jeton.

Je définis la variable `thumbnailUrl` sur l'URL de la capture d'écran créée par l'API. Pour que cela fonctionne, je dois ajouter deux choses.

Tout d'abord, j'ajoute la variable `thumbnailUrl` à l'objet `data` de Vue.

```javascript
data: {
  websiteUrl: '',
  thumbnailUrl: '',
},
```

Ensuite, je crée une balise `img` qui affichera l'image `thumbnailUrl`.

```html
<img :src="thumbnailUrl"/>
```

Démarrons le serveur web et voyons le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-15-at-18.57.00.png)

Il montre une miniature de freeCodeCamp, super !

## Associer Go et Vue ensemble

Pour l'instant, nous avons utilisé le serveur de développement Vue pour démarrer le frontend. Cela fonctionne, mais le serveur de développement ne doit être utilisé que pour le développement local.

Lorsque nous hébergeons cette application dans un environnement de production, vous voudrez utiliser un serveur web "réel" pour gérer les requêtes entrantes.

Heureusement, nous avons juste ce qu'il faut : notre serveur Go.

La première chose que nous devons faire est de compiler notre frontend.

```
yarn run build
```

Cela crée un répertoire `dist` avec les assets compilés.

Nous devons mettre à jour le serveur Go pour servir les fichiers de ce répertoire.

Pour ce faire, je mets à jour la fonction `main` dans le fichier `main.go`.

```go
func main() {
	// Servir les fichiers statiques depuis le répertoire frontend/dist.
	fs := http.FileServer(http.Dir("./frontend/dist"))
	http.Handle("/", fs)

	// Démarrer le serveur.
	fmt.Println("Server listening on port 3000")
	log.Panic(
		http.ListenAndServe(":3000", nil),
	)
}
```

Comme vous pouvez le voir, nous passons simplement le répertoire `frontend/dist` au serveur de fichiers.

Lorsque vous exécutez le programme Go et naviguez vers `localhost:3000`, vous pouvez effectivement voir l'application !

## Rendre l'application plus sécurisée

Pour l'instant, nous avons une faille de sécurité majeure. Le jeton de l'API de capture d'écran est visible dans notre code frontend.

Cela signifie que n'importe qui inspectant la page web peut voler le jeton.

Corrigeons cela en utilisant notre serveur pour appeler l'API de capture d'écran. Ainsi, seul le serveur a besoin de connaître le jeton.

Dans le fichier `server.go`, je crée une nouvelle fonction qui écoutera toute requête vers le point de terminaison `/api/thumbnail`.

```go
type thumbnailRequest struct {
	Url string `json:"url"`
}

func thumbnailHandler(w http.ResponseWriter, r *http.Request) {
	var decoded thumbnailRequest

	// Essayer de décoder la requête dans la structure thumbnailRequest.
	err := json.NewDecoder(r.Body).Decode(&decoded)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	fmt.Printf("Got the following url: %s\n", decoded.Url)
}
```

Pour l'instant, nous extrayons et imprimons simplement le paramètre URL de la requête.

Pour que cela fonctionne, je mets à jour la fonction `main` pour utiliser notre fonction `thumbnailHandler`.

```go
func main() {
	// Utiliser la fonction thumbnailHandler 
	http.HandleFunc("/api/thumbnail", thumbnailHandler)

	fs := http.FileServer(http.Dir("./frontend/dist"))
	http.Handle("/", fs)

	fmt.Println("Server listening on port 3000")
	log.Panic(
		http.ListenAndServe(":3000", nil),
	)
}
```

Et enfin, je dois mettre à jour le fichier `App.vue` pour appeler le serveur Go au lieu de l'API de capture d'écran.

```javascript
makeWebsiteThumbnail() {
  // Appeler l'API Go, dans ce cas, nous avons seulement besoin du paramètre URL.
  axios.post("http://localhost:3000/api/thumbnail", {
    url: this.websiteUrl,
  })
  .then((response) => {
    this.thumbnailUrl = response.data.screenshot;
  })
  .catch((error) => {
    window.alert(`L'API a retourné une erreur : ${error}`);
  })
}
```

Lorsque je teste la nouvelle configuration, je vois effectivement un message de log dans le serveur Go.

```
go run main/server.go
Got the following url: freecodecamp.org
```

## Appeler l'API de capture d'écran depuis Go

Appelons réellement l'API de capture d'écran depuis notre serveur Go.

Pour commencer, je crée une `struct` qui contient tous les paramètres nécessaires pour appeler l'API de capture d'écran.

```go
type screenshotAPIRequest struct {
	Token          string `json:"token"`
	Url            string `json:"url"`
	Output         string `json:"output"`
	Width          int    `json:"width"`
	Height         int    `json:"height"`
	ThumbnailWidth int    `json:"thumbnail_width"`
}
```

Ensuite, je mets à jour la fonction `thumbnailHandler` pour créer une requête HTTP POST et appeler l'API.

```go
func thumbnailHandler(w http.ResponseWriter, r *http.Request) {
	var decoded thumbnailRequest

	// Essayer de décoder la requête dans la structure thumbnailRequest.
	err := json.NewDecoder(r.Body).Decode(&decoded)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	// Créer une structure avec les paramètres nécessaires pour appeler l'API de capture d'écran.
	apiRequest := screenshotAPIRequest{
		Token:          "SCREENSHOTAPI_TOKEN",
		Url:            decoded.Url,
		Output:         "json",
		Width:          1920,
		Height:         1080,
		ThumbnailWidth: 300,
	}

	// Convertir la structure en une chaîne JSON.
	jsonString, err := json.Marshal(apiRequest)
	checkError(err)

	// Créer une requête HTTP.
	req, err := http.NewRequest("POST", "https://screenshotapi.net/api/v1/screenshot", bytes.NewBuffer(jsonString))
	req.Header.Set("Content-Type", "application/json")

	// Exécuter la requête HTTP.
	client := &http.Client{}
	response, err := client.Do(req)
	checkError(err)

	// Dire à Go de fermer la réponse à la fin de la fonction.
	defer response.Body.Close();

	// Lire la réponse brute dans une structure Go.
	type screenshotAPIResponse struct {
		Screenshot string `json"screenshot"`
	}
	var apiResponse screenshotAPIResponse
	err = json.NewDecoder(response.Body).Decode(&apiResponse)
	checkError(err)

	// Renvoyer l'URL de la capture d'écran au frontend.
	_, err = fmt.Fprintf(w, `{ "screenshot": "%s" }`, apiResponse.Screenshot)
	checkError(err)
}
```

Et lorsque vous redémarrez le serveur Go, vous pouvez voir que le générateur de miniatures fonctionne toujours ! Et en bonus, personne ne peut voler notre jeton API maintenant.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-16-at-10.00.18.png)

## Conclusion

Nous avons configuré un générateur de miniatures de sites web full-stack en utilisant Go et Vue. Le frontend est séparé du backend et nous avons ajouté une API externe dans le mélange que nous appelons depuis le serveur Go.

Vous pouvez voir la [version live ici](https://coffeecoding.dev/website-thumbnail-generator) et le [code source Github ici](https://github.com/Dirk94/website-thumbnail-generator).

Bon codage !