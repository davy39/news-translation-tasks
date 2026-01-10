---
title: How to Build a photo feed with Go and Vue.js
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
seo_title: null
seo_desc: 'By Neo Ighodaro

  Many social media applications allow users to upload photos and display them in
  a timeline for their followers to see.

  In the past, you would have had to refresh your feed manually to see new photos
  uploaded to the timeline. However, ...'
---

By Neo Ighodaro

Many social media applications allow users to upload photos and display them in a timeline for their followers to see.

In the past, you would have had to refresh your feed manually to see new photos uploaded to the timeline. However, with modern web technologies, you can see the updates in realtime without having to refresh the page manually.

In this article, we will consider how you can build a realtime photo feed using Pusher Channels, GO and a little Vue.js. [Pusher Channels](https://pusher.com) helps you “easily build scalable in-app notifications, chat, realtime graphs, geotracking and more in your web & mobile apps with our hosted pub/sub messaging API.”

This is a preview of what we will be building:

![Image](https://cdn-media-1.freecodecamp.org/images/X-mAaSoJFNOVaFhrAyuiZ1kMxVOGcfpjrLjw)

### Prerequisites

Before we start building our application, make sure you have:

* Basic knowledge of the [Go](https://golang.org/) programming language.
* Basic JavaScript (Vue.js) knowledge.
* Go (version >= 0.10.x) installed on your machine. Check out t[he installation gu](https://golang.org/doc/install)ide.
* SQLite (version >= 3.x) installed on your machine. Check out [an installation gu](http://www.sqlitetutorial.net/download-install-sqlite/)ide.

Let’s get started.

### Getting a Pusher Channels application

The first step will be to get a Pusher Channels application. We will need the application credentials for our realtime features to work.

Go to the Pusher website and create an account. After creating an account, you should create a new application. Follow the application creation wizard and then you should be given your application credentials, we will use this later in the article.

![Image](https://cdn-media-1.freecodecamp.org/images/E13lsvCh5cph8zugQfGSNdbgbfaVWZ5CpzX5)

Now that we have our application, let’s move on to the next step

### Creating our Go application

The next thing we want to do is create the Go application. In your terminal, `cd` to your `$GOPATH` and create a new directory there.

```
$ cd $GOPATH/src$ mkdir gofoto$ cd gofoto
```

? It is recommended that you place the source code for your project in the s`rc` subdirectory (e.g., $`GOPATH/src/your_project` or $`GOPATH/src/github.com/your_github_username/your_project.`

Next, we will create some directories to organize our application a little:

```
$ mkdir database$ mkdir public$ mkdir public/uploads
```

This will create a `database` and `public` directory, and also an `uploads` directory inside the public directory. We will store our database file inside the `database` directory. We will keep our public files (HTML and images) inside the `public` and `uploads` directory.

Create a new `index.html` file in the `public` directory that was created.

Now let’s create our first (and only) Go file for this article. We will keep everything simple by placing all our source code in a single file. Create a `main.go` file in the project root.

In the file paste the following:

```
package main
```

```
import (    "database/sql"    "io"    "net/http"    "os"
```

```
    "github.com/labstack/echo"    "github.com/labstack/echo/middleware"
```

```
    _ "github.com/mattn/go-sqlite3"    pusher "github.com/pusher/pusher-http-go")
```

This imports some packages we will be needing to work on our photo feed. We need the `database/sql` to run SQL queries. The `io` and `os` packages are for the file uploading process, and the `net/http` package is for our HTTP status codes.

We have some other external packages we imported.

The `labstack/echo` package is the [Echo framework](https://github.com/labstack/echo) that we will be using. We also have the `mattn/go-sqlite3` package for SQLite. Finally, we imported the `pusher/pusher-http-go` package which we will use to trigger events to Pusher Channels.

### Importing external Go packages

Before we continue, let’s pull in these packages using our terminal. Run the following commands below to pull the packages in:

```
$ go get github.com/labstack/echo$ go get github.com/labstack/echo/middleware$ go get github.com/mattn/go-sqlite3$ go get github.com/pusher/pusher-http-go
```

Note that the commands above will not return any confirmation output when it finishes installing the packages. If you want to confirm the packages were indeed installed you can just check the `$GOPATH/src/github.com` directory.

Now that we have pulled in our packages, let’s create the `main` function. This is the function that will be the entry point of our application. In this function, we will set up our applications database, middleware, and routes.

Open the `main,go` file and paste the following code:

```
func main() {    db := initialiseDatabase("database/database.sqlite")
```

```
    migrateDatabase(db)
```

```
    e := echo.New()
```

```
    e.Use(middleware.Logger())    e.Use(middleware.Recover())
```

```
    e.File("/", "public/index.html")    e.GET("/photos", getPhotos(db))    e.POST("/photos", uploadPhoto(db))    e.Static("/uploads", "public/uploads")
```

```
    e.Logger.Fatal(e.Start(":9000"))}
```

In the code above, we instantiated our database using the file path to the database file. This will create the SQLite file if it did not already exist. We then run the `migrateDatabase` function which migrates the database.

Next, we instantiate Echo and then register some middleware.

The [logger middleware](https://echo.labstack.com/middleware/logger) is helpful for logging information about the HTTP request. The [recover middleware](https://echo.labstack.com/middleware/recover) “recovers from panics anywhere in the chain, prints stack trace and handles the control to the centralized [HTTPErrorHandler](https://echo.labstack.com/guide/customization#http-error-handler).”

We then set up some routes to handle our requests. The first handler is the `File` handler. We use this to serve the `index.html` file. This will be the entry point to the application from the front end.

We also have the `/photos` route which accepts a `POST` and `GET` request. We need these routes to act like API endpoints that are used for uploading and displaying the photos.

The final handler is `Static`. We use this to return static files that are stored in the `/uploads` directory.

We finally use `e.Start` to start our Go web server running on port 9000. The port is not set in stone and you can choose any available and unused port you feel like.

At this point, we have not created most of the functions we referenced in the `main` function so let’s do so now.

### Creating our database management functions

In the `main` function we referenced an `initialiseDatabase` and `migrateDatabase` function. Let’s create them now. In the `main.go` file, paste the following functions above the `main` function:

```
func initialiseDatabase(filepath string) *sql.DB {    db, err := sql.Open("sqlite3", filepath)
```

```
    if err != nil || db == nil {        panic("Error connecting to database")    }
```

```
    return db}
```

```
func migrateDatabase(db *sql.DB) {    sql := `        CREATE TABLE IF NOT EXISTS photos(                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,                src VARCHAR NOT NULL        );    `
```

```
    _, err := db.Exec(sql)
```

```
    if err != nil {        panic(err)    }}
```

In the `initialiseDatabase` function, we create an instance of the SQLite database using the database file and return that instance. In the `migrateDatabase` function, we use the instance of the database returned in the previous function to execute the migration SQL.

Let’s create the data structure for our photo and photo collection.

### Creating our data structures

The next thing we will do is create the data structure for our object types. We will create a `Photo` structure and a `PhotoCollection` structure. The `Photo` struct will define how a typical photo will be represented while the `PhotoCollection` will define how a collection of photos will be represented.

Open the `main.go` file and paste the following code above the `initialiseDatabase` function:

```
type Photo struct {    ID  int64  `json:"id"`    Src string `json:"src"`}
```

```
type PhotoCollection struct {    Photos []Photo `json:"items"`}
```

### Creating our route handler functions

Next, let’s create the functions for our routes. Open the `main.go` file and paste the following file inside it:

```
func getPhotos(db *sql.DB) echo.HandlerFunc {    return func(c echo.Context) error {        rows, err := db.Query("SELECT * FROM photos")
```

```
        if err != nil {            panic(err)        }
```

```
        defer rows.Close()
```

```
        result := PhotoCollection{}
```

```
        for rows.Next() {            photo := Photo{}
```

```
            err2 := rows.Scan(&photo.ID, &photo.Src)
```

```
            if err2 != nil {                panic(err2)            }
```

```
            result.Photos = append(result.Photos, photo)        }
```

```
        return c.JSON(http.StatusOK, result)    }}
```

```
func uploadPhoto(db *sql.DB) echo.HandlerFunc {    return func(c echo.Context) error {        file, err := c.FormFile("file")
```

```
        if err != nil {            return err        }
```

```
        src, err := file.Open()
```

```
        if err != nil {            return err        }
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
        if err != nil {            panic(err)        }
```

```
        defer dst.Close()
```

```
        if _, err = io.Copy(dst, src); err != nil {            panic(err)        }
```

```
        stmt, err := db.Prepare("INSERT INTO photos (src) VALUES(?)")
```

```
        if err != nil {            panic(err)        }
```

```
        defer stmt.Close()
```

```
        result, err := stmt.Exec(fileSrc)
```

```
        if err != nil {            panic(err)        }
```

```
        insertedId, err := result.LastInsertId()
```

```
        if err != nil {            panic(err)        }
```

```
        photo := Photo{            Src: fileSrc,            ID:  insertedId,        }
```

```
        return c.JSON(http.StatusOK, photo)    }}
```

In the `getPhotos` method, we are simply running the query to fetch all the photos from the database and returning them as a JSON response to the client.

In the `uploadPhoto` method we first get the file to be uploaded then upload them to the server and then we run the query to insert a new record in the `photos` table with the newly uploaded photo. We also return a JSON response from that function.

### Adding realtime support to our Go application

The next thing we want to do is trigger an event when a new photo is uploaded to the server. For this, we will be using the [Pusher Go HTTP library](https://github.com/pusher/pusher-http-go).

In the `main.go` file paste the following above the type definitions for the `Photo` and `PhotoCollection`:

```
var client = pusher.Client{    AppId:   "PUSHER_APP_ID",    Key:     "PUSHER_APP_KEY",    Secret:  "PUSHER_APP_SECRET",    Cluster: "PUSHER_APP_CLUSTER",    Secure:  true,}
```

This will create a new Pusher client instance. We can then use this instance to trigger notifications to different channels we want. Remember to replace the `PUSHER_APP_*` keys with the keys provided when you created your Pusher application earlier.

Next, go to the `uploadPhoto` function in the `main.go` file and right before the `return` statement at the bottom of the function, paste the following code:

```
client.Trigger("photo-stream", "new-photo", photo)
```

This is the code that triggers a new event when a new photo is uploaded to our application.

That will be all for our Go application. At this point, you can build your application and compile it into a binary using the `go build` command. However, for this tutorial we will just run the binary temporarily:

```
$ go run main.go
```

![Image](https://cdn-media-1.freecodecamp.org/images/hcsYY3wwFoA6QA4dxvxgL2MDxX7OwJVAiV9p)

### Building our front end

The next thing we want to do is build out our front end. We will be using the [Vue.js framework](https://vuejs.org/) and the [Axios library](https://github.com/axios/axios) to send requests.

Open the `index.html` file and in there paste the following code:

```
<!doctype html><html lang="en"><head>    <meta charset="utf-8">    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css">    <title>Photo Feed</title>    <style type="text/css">        #photoFile { display: none; }        #app img { max-width: 100%; }        .image-row { margin: 20px 0; }        .image-row .thumbnail { padding: 2px; border: 1px solid #d9d9d9; }    </style></head><body>    <div id="app">        <nav class="navbar navbar-expand-lg navbar-light bg-light">            <a class="navbar-brand" href="#">GoFoto</a>            <div>                <ul class="navbar-nav mr-auto">                    <li class="nav-item active">                        <a class="nav-link" v-on:click="filePicker" href="#">Upload</a>                        <input type="file" id="photoFile" ref="myFiles" @change="upload" name="file" />                    </li>                </ul>            </div>        </nav>        <div class="container">            <div class="row justify-content-md-center" id="loading" v-if="loading">                <div class="col-xs-12">                    Loading photos...                </div>            </div>            <div class="row justify-content-md-center image-row" v-for="photo in photos">                <div class="col col-lg-4 col-md-6 col-xs-12">                    <img class="thumbnail" :src="photo.src" alt="" />                </div>            </div>        &lt;/div>    </div>    <script src="//js.pusher.com/4.0/pusher.min.js"></script>    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>    <script src="https://cdn.jsdelivr.net/npm/vue@2.5.16/dist/vue.js"></script></body></html>
```

In the HTML file above we have defined the design for our photostream. We are using Bootstrap 4 and we included the CSS in the HTML above.

We are also using the Axios library, Pusher library, and Vue framework. We included the links to the scripts at the bottom of the HTML document.

Next, let’s add the Vue.js code. In the HTML file, add the following code right before the closing `body` tag:

```
<script type="text/javascript">    new Vue({        el: '#app',        data: {            photos: [],            loading: true,        },        mounted() {            const pusher = new Pusher('PUSHER_APP_KEY', {                cluster: 'PUSHER_APP_CLUSTER',                encrypted: true            });
```

```
            let channel = pusher.subscribe('photo-stream')
```

```
            channel.bind('new-photo', data => this.photos.unshift(data));
```

```
            axios.get('/photos').then(res => {                this.loading = false                this.photos = res.data.items ? res.data.items : []            })        },        methods: {            filePicker: function () {                let elem = document.getElementById('photoFile');
```

```
                if (elem && document.createEvent) {                    let evt = document.createEvent("MouseEvents");                    evt.initEvent("click", true, false);                    elem.dispatchEvent(evt);                }            },            upload: function () {                let data = new FormData();
```

```
                data.append('file', this.$refs.myFiles.files[0]);                axios.post('/photos', data).then(res => console.log(res))            }        }    });</script>
```

Above we created a Vue instance and stored the properties `photos` and `loading`. The `photos` property stores the photo list and the `loading` just holds a boolean that indicates if the photos are loading or not.

In the `mounted` method we create an instance of our Pusher library. We then listen on the `photo-stream` channel for the `new-photo` event. When the event is triggered we append the new photo from the event to the `photos` list. We also send a GET request to `/photos` to fetch all the photos from the API. Replace the `PUSHER_APP_*` keys with the one from your Pusher dashboard.

In the `methods` property, we added a few methods. The `filePicker` is triggered when the ‘Upload’ button is pressed on the UI. It triggers a file picker that allows the user to upload photos. The `upload` method takes the uploaded file and sends a POST request with the file to the API for processing.

That’s all for the front end. You can save the file and head over to your web browser. Visit [http://127.0.0.1:9000](http://127.0.0.1:9000) to see your application in action.

Here’s how it will look again:

![Image](https://cdn-media-1.freecodecamp.org/images/LQr7LmqE1dMa4c8BcFqutTdILkUnbI9Y0ZIr)

### Conclusion

In this article, we have been able to demonstrate how you can use Pusher Channels in your Go application to provide realtime features for your application.

As seen from the code samples above, it is very easy to get started with Pusher Channels. Check the [documentation](https://pusher.com/docs) to see other ways you can use Pusher Channels to provide realtime features to your users.

The source code for this application is available on [GitHub](https://github.com/neoighodaro/realtime-photofeed-pusher-go).

This article was first published on [Pusher](https://pusher.com/tutorials/photo-feed-go-vuejs).

