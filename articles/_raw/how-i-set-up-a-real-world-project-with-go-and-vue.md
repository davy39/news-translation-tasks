---
title: How to Set Up a Real-World Project with Go and Vue
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
seo_title: null
seo_desc: 'By Dirk Hoekstra

  When I first started with Go programming I found it pretty hard to get my head around
  it. It was way more low-level than anything else I had ever coded in.

  Fast forward a few months and now I''m a total fan and use it for a lot of pro...'
---

By Dirk Hoekstra

When I first started with Go programming I found it pretty hard to get my head around it. It was way more low-level than anything else I had ever coded in.

Fast forward a few months and now I'm a total fan and use it for a lot of projects.

In this article, I'll show you how I set up a full-stack web application with Go and Vue.

Let's dive in!

## What we're going to create

I thought it would be cool to create a website thumbnail generator. The idea is that you enter a website URL and the application will generate a thumbnail of that website for you.

## Setting up a Go module

First, I create a new directory. Then I set up a Go module by running the following command.

```
go mod init github.com/Dirk94/website-thumbnail-generator
```

This will create a `go.mod` file that keeps track of all the module dependencies. This is similar to the `package.json` file in a node project.

Next, I create a new directory `main` in which I add a `server.go` file. This will be the main entry point of the application.

For now, let's just print a "hello world" message.

```go
package main

import "fmt"

func main() {
	fmt.Println("Hello world")
}
```

 To run the program I run the following command from the project directory.

```
go run main/server.go
Hello world
```

Great, so far everything works! ?

## Setting up a web server

We should create a web server that will listen for incoming requests. 

Let's update the main function.

```go
func main() {
	http.HandleFunc("/", homePageHandler)

	fmt.Println("Server listening on port 3000")
	log.Panic(
		http.ListenAndServe(":3000", nil),
	)
}
```

This will start up a web server and listen on port 3000. 

Any request coming in will be handled by the `homePageHandler` function. This does not yet exist so let's create it.

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

All this function does is write "hello world" to the `http.ResponseWriter` 

The `checkError` function is simply a handy function that will stop the program and print a stack trace if the `error` is not nil.

When running the program the web server prints the "hello world" message correctly!

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-14-at-17.02.19.png)

## Creating the Vue project

To create a new Vue project I run the following command from the project directory.

```
vue create frontend
```

This creates a lot of files but don't be overwhelmed. Let's begin by running the Vue development server.

```
yarn serve
```

When navigating to localhost:8081 you can see that the Vue app works!

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-15-at-19.11.06.png)

Alright, let's clean up the frontend directory a bit.

For starters, I delete the `assets` and `components` directory as I won't use them.

Then I update the `App.vue` file.

```html
<template>
  <div id="app" class="container">
    <div class="row">
      <div class="col-md-6 offset-md-3 py-5">
        <h1>Generate a thumbnail of a website</h1>

        <form v-on:submit.prevent="makeWebsiteThumbnail">
          <div class="form-group">
            <input v-model="websiteUrl" type="text" id="website-input" placeholder="Enter a website" class="form-control">
          </div>
          <div class="form-group">
            <button class="btn btn-primary">Generate!</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
```

I use the `v-model` tag and I call a `makeWebsiteThumbnail` function when the form submits. Right now these don't exist. Let's add them.

```javascript
<script>
export default {
  name: 'App',

  data() { return {
    websiteUrl: '',
  } },

  methods: {
    makeWebsiteThumbnail() {
      console.log(`I should create a website thumbnail of ${this.websiteUrl}`);
    }
  }
}
</script>
```

I'm also using some Bootstrap 4 classes, so for that to work I must add the bootstrap CSS to the `public/index.html` file.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
      
      <!--- The other stuff in the head tag here... -->
  </head>
```

Alright, let's fire up the web server and check if we see the log message.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-15-at-18.36.31.png)

Nice, it works! ?

## Creating a website thumbnail

To create the website thumbnail I'm going to use [screenshotapi.net](https://screenshotapi.net). That way I only have to call an API to do the heavy lifting for me.

First I install axios.

```
yarn add axios
```

Then I import it in the `App.vue` file.

```javascript
<script>
  import axios from 'axios';
  
  export default {
    name: 'App', 
    
    // The rest here...
    
```

Next, I update the `makeWebsiteThumbnail` function to actually call the screenshot API.

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
    window.alert(`The API returned an error: ${error}`);
  })
}
```

Make sure to replace the `SCREENSHOTAPI_TOKEN` with your token.

I set the variable `thumbnailUrl` to the screenshot URL that is created by the API. To make this work I have to add 2 things.

First, I add the `thumbnailUrl` variable to the Vue `data` object.

```javascript
data: {
  websiteUrl: '',
  thumbnailUrl: '',
},
```

Second, I create an `img` tag that will display `thumbnailUrl` image.

```html
<img :src="thumbnailUrl"/>
```

Let's spin up the web server and see the result:

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-15-at-18.57.00.png)

It shows a thumbnail of freeCodeCamp, nice!

## Gluing Go and Vue together

Right now we've used the Vue development server to spin up the front end. It works, but the development server should only be used for local development.

When we host this application in a production environment you will want to use a "real" web server to handle the incoming requests.

Luckily we have just such a thing: our Go server.

The first thing we have to do is compile our frontend.

```
yarn run build
```

This creates a `dist` directory with the compiled assets.

We should update the Go server to serve the files from this directory.

To do this I update the `main` function in the `main.go` file.

```go
func main() {
	// Serve static files from the frontend/dist directory.
	fs := http.FileServer(http.Dir("./frontend/dist"))
	http.Handle("/", fs)

	// Start the server.
	fmt.Println("Server listening on port 3000")
	log.Panic(
		http.ListenAndServe(":3000", nil),
	)
}
```

As you can see we simply pass the `frontend/dist` directory to the fileserver.

When running the go program and navigating to `localhost:3000` you can indeed see the application!

## Making the app more secure

Right now we have a major security flaw. The screenshot API token is visible in our frontend code.

This means that anybody that inspects the webpage can steal the token.

Let's fix that by using our server to call the screenshot API. That way only the server needs to know the token.

In the `server.go` I create a new function that will listen for any request to the `/api/thumbnail` endpoint. 

```go
type thumbnailRequest struct {
	Url string `json:"url"`
}

func thumbnailHandler(w http.ResponseWriter, r *http.Request) {
	var decoded thumbnailRequest

	// Try to decode the request into the thumbnailRequest struct.
	err := json.NewDecoder(r.Body).Decode(&decoded)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	fmt.Printf("Got the following url: %s\n", decoded.Url)
}
```

For now we just extract and print the URL parameter from the request.

To make this work I update the `main` function to use our `thumbnailHandler` function.

```go
func main() {
	// Use the thumbnailHandler function 
	http.HandleFunc("/api/thumbnail", thumbnailHandler)

	fs := http.FileServer(http.Dir("./frontend/dist"))
	http.Handle("/", fs)

	fmt.Println("Server listening on port 3000")
	log.Panic(
		http.ListenAndServe(":3000", nil),
	)
}
```

And finally, I should update the `App.vue` file to call the Go server instead of the screenshot API.

```javascript
makeWebsiteThumbnail() {
  // Call the Go API, in this case we only need the URL parameter.
  axios.post("http://localhost:3000/api/thumbnail", {
    url: this.websiteUrl,
  })
  .then((response) => {
    this.thumbnailUrl = response.data.screenshot;
  })
  .catch((error) => {
    window.alert(`The API returned an error: ${error}`);
  })
}
```

When testing the new setup I indeed see a log message in the go server.

```
go run main/server.go
Got the following url: freecodecamp.org
```

## Calling the screenshot API from Go

Let's actually call the Screenshot API from our Go server.

To begin I create a `struct` that holds all the parameters needed to call the Screenshot API.

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

Then, I update the `thumbnailHandler` function to create a http POST request and call the API.

```go
func thumbnailHandler(w http.ResponseWriter, r *http.Request) {
	var decoded thumbnailRequest

	// Try to decode the request into the thumbnailRequest struct.
	err := json.NewDecoder(r.Body).Decode(&decoded)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	// Create a struct with the parameters needed to call the ScreenshotAPI.
	apiRequest := screenshotAPIRequest{
		Token:          "SCREENSHOTAPI_TOKEN",
		Url:            decoded.Url,
		Output:         "json",
		Width:          1920,
		Height:         1080,
		ThumbnailWidth: 300,
	}

	// Convert the struct to a JSON string.
	jsonString, err := json.Marshal(apiRequest)
	checkError(err)

	// Create a HTTP request.
	req, err := http.NewRequest("POST", "https://screenshotapi.net/api/v1/screenshot", bytes.NewBuffer(jsonString))
	req.Header.Set("Content-Type", "application/json")

	// Execute the HTTP request.
	client := &http.Client{}
	response, err := client.Do(req)
	checkError(err)

	// Tell Go to close the response at the end of the function.
	defer response.Body.Close();

	// Read the raw response into a Go struct.
	type screenshotAPIResponse struct {
		Screenshot string `json"screenshot"`
	}
	var apiResponse screenshotAPIResponse
	err = json.NewDecoder(response.Body).Decode(&apiResponse)
	checkError(err)

	// Pass back the screenshot URL to the frontend.
	_, err = fmt.Fprintf(w, `{ "screenshot": "%s" }`, apiResponse.Screenshot)
	checkError(err)
}
```

And when restarting the Go server you can see that the thumbnail generator still works! And as a bonus, nobody can steal our API token now. 

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-16-at-10.00.18.png)

## Conclusion

We've set up a full-stack website thumbnail generator using Go and Vue. The frontend is separated from the backend and we've added an external API in the mix that we call from the Go server.

You can view the [live version here](https://coffeecoding.dev/website-thumbnail-generator) and the [Github source code here](https://github.com/Dirk94/website-thumbnail-generator).

Happy coding!

