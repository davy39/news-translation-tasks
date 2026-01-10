---
title: Comment créer un fil de photos avec Go et Vue.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-26T18:15:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-photo-feed-with-go-and-vue-js-9d7f7f39c1b4
coverImage: https://cdn-media-1.freecodecamp.org/images/0*2vn4torHBYhCLmTr
tags:
- name: golang
  slug: golang
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Vue.js
  slug: vuejs
- name: Web Development
  slug: web-development
seo_title: Comment créer un fil de photos avec Go et Vue.js
seo_desc: 'By Neo Ighodaro

  Many social media applications allow users to upload photos and display them in
  a timeline for their followers to see.

  In the past, you would have had to refresh your feed manually to see new photos
  uploaded to the timeline. However, ...'
---

Par Neo Ighodaro

De nombreuses applications de médias sociaux permettent aux utilisateurs de télécharger des photos et de les afficher dans une timeline pour que leurs abonnés puissent les voir.

Auparavant, vous deviez actualiser manuellement votre fil pour voir les nouvelles photos téléchargées dans la timeline. Cependant, avec les technologies web modernes, vous pouvez voir les mises à jour en temps réel sans avoir à actualiser manuellement la page.

Dans cet article, nous allons voir comment vous pouvez créer un fil de photos en temps réel en utilisant Pusher Channels, GO et un peu de Vue.js. [Pusher Channels](https://pusher.com) vous aide à « créer facilement des notifications dans l'application, des chats, des graphiques en temps réel, du géotracking et plus encore dans vos applications web et mobiles avec notre API de messagerie pub/sub hébergée ».

Voici un aperçu de ce que nous allons créer :

![Image](https://cdn-media-1.freecodecamp.org/images/X-mAaSoJFNOVaFhrAyuiZ1kMxVOGcfpjrLjw)

### Prérequis

Avant de commencer à créer notre application, assurez-vous d'avoir :

* Une connaissance de base du langage de programmation [Go](https://golang.org/).
* Une connaissance de base de JavaScript (Vue.js).
* Go (version >= 0.10.x) installé sur votre machine. Consultez le [guide d'installation](https://golang.org/doc/install).
* SQLite (version >= 3.x) installé sur votre machine. Consultez un [guide d'installation](http://www.sqlitetutorial.net/download-install-sqlite/).

Commençons.

### Obtenir une application Pusher Channels

La première étape consiste à obtenir une application Pusher Channels. Nous aurons besoin des identifiants de l'application pour que nos fonctionnalités en temps réel fonctionnent.

Allez sur le site web de Pusher et créez un compte. Après avoir créé un compte, vous devez créer une nouvelle application. Suivez l'assistant de création d'application, puis vous devriez recevoir vos identifiants d'application, que nous utiliserons plus tard dans l'article.

![Image](https://cdn-media-1.freecodecamp.org/images/E13lsvCh5cph8zugQfGSNdbgbfaVWZ5CpzX5)

Maintenant que nous avons notre application, passons à l'étape suivante.

### Créer notre application Go

La prochaine chose que nous voulons faire est de créer l'application Go. Dans votre terminal, utilisez la commande `cd` pour accéder à votre `$GOPATH` et créez un nouveau répertoire.

```
$ cd $GOPATH/src
$ mkdir gofoto
$ cd gofoto
```

❓ Il est recommandé de placer le code source de votre projet dans le sous-répertoire `src` (par exemple, `$GOPATH/src/votre_projet` ou `$GOPATH/src/github.com/votre_nom_utilisateur_github/votre_projet`.

Ensuite, nous allons créer quelques répertoires pour organiser un peu notre application :

```
$ mkdir database
$ mkdir public
$ mkdir public/uploads
```

Cela créera un répertoire `database` et un répertoire `public`, ainsi qu'un répertoire `uploads` à l'intérieur du répertoire public. Nous stockerons notre fichier de base de données dans le répertoire `database`. Nous garderons nos fichiers publics (HTML et images) dans les répertoires `public` et `uploads`.

Créez un nouveau fichier `index.html` dans le répertoire `public` qui a été créé.

Maintenant, créons notre premier (et unique) fichier Go pour cet article. Nous garderons tout simple en plaçant tout notre code source dans un seul fichier. Créez un fichier `main.go` à la racine du projet.

Dans le fichier, collez ce qui suit :

```
package main
```

```
import (
    "database/sql"
    "io"
    "net/http"
    "os"
```

```
    "github.com/labstack/echo"
    "github.com/labstack/echo/middleware"
```

```
    _ "github.com/mattn/go-sqlite3"
    pusher "github.com/pusher/pusher-http-go"
)
```

Cela importe certains packages dont nous aurons besoin pour travailler sur notre fil de photos. Nous avons besoin de `database/sql` pour exécuter des requêtes SQL. Les packages `io` et `os` sont pour le processus de téléchargement de fichiers, et le package `net/http` est pour nos codes de statut HTTP.

Nous avons quelques autres packages externes que nous avons importés.

Le package `labstack/echo` est le [Framework Echo](https://github.com/labstack/echo) que nous allons utiliser. Nous avons également le package `mattn/go-sqlite3` pour SQLite. Enfin, nous avons importé le package `pusher/pusher-http-go` que nous utiliserons pour déclencher des événements vers Pusher Channels.

### Importation de packages Go externes

Avant de continuer, tirons ces packages en utilisant notre terminal. Exécutez les commandes suivantes pour tirer les packages :

```
$ go get github.com/labstack/echo
$ go get github.com/labstack/echo/middleware
$ go get github.com/mattn/go-sqlite3
$ go get github.com/pusher/pusher-http-go
```

Notez que les commandes ci-dessus ne retourneront aucune sortie de confirmation une fois l'installation des packages terminée. Si vous souhaitez confirmer que les packages ont bien été installés, vous pouvez simplement vérifier le répertoire `$GOPATH/src/github.com`.

Maintenant que nous avons tiré nos packages, créons la fonction `main`. C'est la fonction qui sera le point d'entrée de notre application. Dans cette fonction, nous allons configurer la base de données de notre application, le middleware et les routes.

Ouvrez le fichier `main.go` et collez le code suivant :

```
func main() {
    db := initialiseDatabase("database/database.sqlite")
```

```
    migrateDatabase(db)
```

```
    e := echo.New()
```

```
    e.Use(middleware.Logger())
    e.Use(middleware.Recover())
```

```
    e.File("/", "public/index.html")
    e.GET("/photos", getPhotos(db))
    e.POST("/photos", uploadPhoto(db))
    e.Static("/uploads", "public/uploads")
```

```
    e.Logger.Fatal(e.Start(":9000"))
}
```

Dans le code ci-dessus, nous avons instancié notre base de données en utilisant le chemin du fichier de la base de données. Cela créera le fichier SQLite s'il n'existait pas déjà. Nous exécutons ensuite la fonction `migrateDatabase` qui migre la base de données.

Ensuite, nous instancions Echo et enregistrons quelques middlewares.

Le [middleware logger](https://echo.labstack.com/middleware/logger) est utile pour logger les informations sur la requête HTTP. Le [middleware recover](https://echo.labstack.com/middleware/recover) « récupère les paniques n'importe où dans la chaîne, imprime la trace de la pile et gère le contrôle au [HTTPErrorHandler](https://echo.labstack.com/guide/customization#http-error-handler) centralisé ».

Nous avons ensuite configuré quelques routes pour gérer nos requêtes. Le premier gestionnaire est le gestionnaire `File`. Nous l'utilisons pour servir le fichier `index.html`. Ce sera le point d'entrée de l'application depuis le front-end.

Nous avons également la route `/photos` qui accepte une requête `POST` et `GET`. Nous avons besoin de ces routes pour agir comme des endpoints API qui sont utilisés pour télécharger et afficher les photos.

Le dernier gestionnaire est `Static`. Nous l'utilisons pour retourner des fichiers statiques qui sont stockés dans le répertoire `/uploads`.

Nous utilisons enfin `e.Start` pour démarrer notre serveur web Go sur le port 9000. Le port n'est pas figé et vous pouvez choisir n'importe quel port disponible et inutilisé que vous souhaitez.

À ce stade, nous n'avons pas créé la plupart des fonctions que nous avons référencées dans la fonction `main`, alors faisons-le maintenant.

### Création de nos fonctions de gestion de base de données

Dans la fonction `main`, nous avons référencé une fonction `initialiseDatabase` et `migrateDatabase`. Créons-les maintenant. Dans le fichier `main.go`, collez les fonctions suivantes au-dessus de la fonction `main` :

```
func initialiseDatabase(filepath string) *sql.DB {
    db, err := sql.Open("sqlite3", filepath)
```

```
    if err != nil || db == nil {
        panic("Erreur de connexion à la base de données")
    }
```

```
    return db
}
```

```
func migrateDatabase(db *sql.DB) {
    sql := `
        CREATE TABLE IF NOT EXISTS photos(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                src VARCHAR NOT NULL
        );
    `
```

```
    _, err := db.Exec(sql)
```

```
    if err != nil {
        panic(err)
    }
}
```

Dans la fonction `initialiseDatabase`, nous créons une instance de la base de données SQLite en utilisant le fichier de base de données et retournons cette instance. Dans la fonction `migrateDatabase`, nous utilisons l'instance de la base de données retournée dans la fonction précédente pour exécuter la migration SQL.

Créons la structure de données pour notre photo et notre collection de photos.

### Création de nos structures de données

La prochaine chose que nous allons faire est de créer la structure de données pour nos types d'objets. Nous allons créer une structure `Photo` et une structure `PhotoCollection`. La structure `Photo` définira comment une photo typique sera représentée tandis que la `PhotoCollection` définira comment une collection de photos sera représentée.

Ouvrez le fichier `main.go` et collez le code suivant au-dessus de la fonction `initialiseDatabase` :

```
type Photo struct {
    ID  int64  `json:"id"`
    Src string `json:"src"`
}
```

```
type PhotoCollection struct {
    Photos []Photo `json:"items"`
}
```

### Création de nos fonctions de gestion de routes

Ensuite, créons les fonctions pour nos routes. Ouvrez le fichier `main.go` et collez le fichier suivant à l'intérieur :

```
func getPhotos(db *sql.DB) echo.HandlerFunc {
    return func(c echo.Context) error {
        rows, err := db.Query("SELECT * FROM photos")
```

```
        if err != nil {
            panic(err)
        }
```

```
        defer rows.Close()
```

```
        result := PhotoCollection{}
```

```
        for rows.Next() {
            photo := Photo{}
```

```
            err2 := rows.Scan(&photo.ID, &photo.Src)
```

```
            if err2 != nil {
                panic(err2)
            }
```

```
            result.Photos = append(result.Photos, photo)
        }
```

```
        return c.JSON(http.StatusOK, result)
    }
}
```

```
func uploadPhoto(db *sql.DB) echo.HandlerFunc {
    return func(c echo.Context) error {
        file, err := c.FormFile("file")
```

```
        if err != nil {
            return err
        }
```

```
        src, err := file.Open()
```

```
        if err != nil {
            return err
        }
```

```
        defer src.Close()
```

```
        filePath := "./public/uploads/" + file.Filename
```

```
        fileSrc := "http://127.0.0.1:9000/uploads/" + file.Filename
```

```
        dst, err := os.Create(filePath)
```

```
        if err != nil {
            panic(err)
        }
```

```
        defer dst.Close()
```

```
        if _, err = io.Copy(dst, src); err != nil {
            panic(err)
        }
```

```
        stmt, err := db.Prepare("INSERT INTO photos (src) VALUES(?)")
```

```
        if err != nil {
            panic(err)
        }
```

```
        defer stmt.Close()
```

```
        result, err := stmt.Exec(fileSrc)
```

```
        if err != nil {
            panic(err)
        }
```

```
        insertedId, err := result.LastInsertId()
```

```
        if err != nil {
            panic(err)
        }
```

```
        photo := Photo{
            Src: fileSrc,
            ID:  insertedId,
        }
```

```
        return c.JSON(http.StatusOK, photo)
    }
}
```

Dans la méthode `getPhotos`, nous exécutons simplement la requête pour récupérer toutes les photos de la base de données et les retournons en tant que réponse JSON au client.

Dans la méthode `uploadPhoto`, nous récupérons d'abord le fichier à télécharger, puis nous le téléchargeons sur le serveur et exécutons la requête pour insérer un nouvel enregistrement dans la table `photos` avec la photo nouvellement téléchargée. Nous retournons également une réponse JSON à partir de cette fonction.

### Ajout du support en temps réel à notre application Go

La prochaine chose que nous voulons faire est de déclencher un événement lorsqu'une nouvelle photo est téléchargée sur le serveur. Pour cela, nous utiliserons la [bibliothèque HTTP Go de Pusher](https://github.com/pusher/pusher-http-go).

Dans le fichier `main.go`, collez ce qui suit au-dessus des définitions de type pour `Photo` et `PhotoCollection` :

```
var client = pusher.Client{
    AppId:   "PUSHER_APP_ID",
    Key:     "PUSHER_APP_KEY",
    Secret:  "PUSHER_APP_SECRET",
    Cluster: "PUSHER_APP_CLUSTER",
    Secure:  true,
}
```

Cela créera une nouvelle instance du client Pusher. Nous pouvons ensuite utiliser cette instance pour déclencher des notifications vers les différents canaux que nous voulons. N'oubliez pas de remplacer les clés `PUSHER_APP_*` par les clés fournies lors de la création de votre application Pusher.

Ensuite, allez à la fonction `uploadPhoto` dans le fichier `main.go` et juste avant l'instruction `return` en bas de la fonction, collez le code suivant :

```
client.Trigger("photo-stream", "new-photo", photo)
```

C'est le code qui déclenche un nouvel événement lorsqu'une nouvelle photo est téléchargée dans notre application.

Cela sera tout pour notre application Go. À ce stade, vous pouvez construire votre application et la compiler en un binaire en utilisant la commande `go build`. Cependant, pour ce tutoriel, nous allons simplement exécuter le binaire temporairement :

```
$ go run main.go
```

![Image](https://cdn-media-1.freecodecamp.org/images/hcsYY3wwFoA6QA4dxvxgL2MDxX7OwJVAiV9p)

### Construction de notre front-end

La prochaine chose que nous voulons faire est de construire notre front-end. Nous allons utiliser le [framework Vue.js](https://vuejs.org/) et la [bibliothèque Axios](https://github.com/axios/axios) pour envoyer des requêtes.

Ouvrez le fichier `index.html` et collez le code suivant :

```
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css">
    <title>Photo Feed</title>
    <style type="text/css">
        #photoFile { display: none; }
        #app img { max-width: 100%; }
        .image-row { margin: 20px 0; }
        .image-row .thumbnail { padding: 2px; border: 1px solid #d9d9d9; }
    </style>
</head>
<body>
    <div id="app">
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <a class="navbar-brand" href="#">GoFoto</a>
            <div>
                <ul class="navbar-nav mr-auto">
                    <li class="nav-item active">
                        <a class="nav-link" v-on:click="filePicker" href="#">Upload</a>
                        <input type="file" id="photoFile" ref="myFiles" @change="upload" name="file" />
                    </li>
                </ul>
            </div>
        </nav>
        <div class="container">
            <div class="row justify-content-md-center" id="loading" v-if="loading">
                <div class="col-xs-12">
                    Loading photos...
                </div>
            </div>
            <div class="row justify-content-md-center image-row" v-for="photo in photos">
                <div class="col col-lg-4 col-md-6 col-xs-12">
                    <img class="thumbnail" :src="photo.src" alt="" />
                </div>
            </div>
        </div>
    </div>
    <script src="//js.pusher.com/4.0/pusher.min.js"></script>
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/vue@2.5.16/dist/vue.js"></script>
</body>
</html>
```

Dans le fichier HTML ci-dessus, nous avons défini le design pour notre photostream. Nous utilisons Bootstrap 4 et nous avons inclus le CSS dans le HTML ci-dessus.

Nous utilisons également la bibliothèque Axios, la bibliothèque Pusher et le framework Vue. Nous avons inclus les liens vers les scripts en bas du document HTML.

Ensuite, ajoutons le code Vue.js. Dans le fichier HTML, ajoutez le code suivant juste avant la balise de fermeture `body` :

```
<script type="text/javascript">
    new Vue({
        el: '#app',
        data: {
            photos: [],
            loading: true,
        },
        mounted() {
            const pusher = new Pusher('PUSHER_APP_KEY', {
                cluster: 'PUSHER_APP_CLUSTER',
                encrypted: true
            });
```

```
            let channel = pusher.subscribe('photo-stream')
```

```
            channel.bind('new-photo', data => this.photos.unshift(data));
```

```
            axios.get('/photos').then(res => {
                this.loading = false
                this.photos = res.data.items ? res.data.items : []
            })
        },
        methods: {
            filePicker: function () {
                let elem = document.getElementById('photoFile');
```

```
                if (elem && document.createEvent) {
                    let evt = document.createEvent("MouseEvents");
                    evt.initEvent("click", true, false);
                    elem.dispatchEvent(evt);
                }
            },
            upload: function () {
                let data = new FormData();
```

```
                data.append('file', this.$refs.myFiles.files[0]);
                axios.post('/photos', data).then(res => console.log(res))
            }
        }
    });
</script>
```

Ci-dessus, nous avons créé une instance Vue et stocké les propriétés `photos` et `loading`. La propriété `photos` stocke la liste des photos et `loading` contient simplement un booléen qui indique si les photos sont en cours de chargement ou non.

Dans la méthode `mounted`, nous créons une instance de notre bibliothèque Pusher. Nous écoutons ensuite le canal `photo-stream` pour l'événement `new-photo`. Lorsque l'événement est déclenché, nous ajoutons la nouvelle photo de l'événement à la liste `photos`. Nous envoyons également une requête GET à `/photos` pour récupérer toutes les photos de l'API. Remplacez les clés `PUSHER_APP_*` par celles de votre tableau de bord Pusher.

Dans la propriété `methods`, nous avons ajouté quelques méthodes. La méthode `filePicker` est déclenchée lorsque le bouton « Upload » est pressé sur l'interface utilisateur. Elle déclenche un sélecteur de fichiers qui permet à l'utilisateur de télécharger des photos. La méthode `upload` prend le fichier téléchargé et envoie une requête POST avec le fichier à l'API pour traitement.

C'est tout pour le front-end. Vous pouvez enregistrer le fichier et vous rendre sur votre navigateur web. Visitez [http://127.0.0.1:9000](http://127.0.0.1:9000) pour voir votre application en action.

Voici à quoi cela ressemblera à nouveau :

![Image](https://cdn-media-1.freecodecamp.org/images/LQr7LmqE1dMa4c8BcFqutTdILkUnbI9Y0ZIr)

### Conclusion

Dans cet article, nous avons pu démontrer comment vous pouvez utiliser Pusher Channels dans votre application Go pour fournir des fonctionnalités en temps réel à votre application.

Comme on peut le voir à partir des exemples de code ci-dessus, il est très facile de commencer avec Pusher Channels. Consultez la [documentation](https://pusher.com/docs) pour voir d'autres façons dont vous pouvez utiliser Pusher Channels pour fournir des fonctionnalités en temps réel à vos utilisateurs.

Le code source de cette application est disponible sur [GitHub](https://github.com/neoighodaro/realtime-photofeed-pusher-go).

Cet article a été publié pour la première fois sur [Pusher](https://pusher.com/tutorials/photo-feed-go-vuejs).