---
title: How to setup a nested HTML template in the Go Echo web framework
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-05T23:01:58.000Z'
originalURL: https://freecodecamp.org/news/how-to-setup-a-nested-html-template-in-the-go-echo-web-framework-670f16244bb4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*i1ZfgPCFQ95TeWWMiLa8wA.png
tags:
- name: পিএইচপি ভেরিয়েবল Echo এবং প্রিন্ট স্ট্যাটমেন্ট
  slug: echo
- name: golang
  slug: golang
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Ying Kit Yuen

  Echo is a lightweight but complete web framework in Go for building RESTful APIs.
  It is fast and includes a bunch of middleware for handling the whole HTTP request-response
  cycle. For the rendering part, it works with any template en...'
---

By Ying Kit Yuen

[Echo](https://echo.labstack.com/) is a lightweight but complete web framework in [Go](https://golang.org/) for building RESTful APIs. It is fast and includes a bunch of middleware for handling the whole HTTP request-response cycle. For the rendering part, it works with any template engine, but I use the standard [html/template](https://godoc.org/html/template) package for the purpose of simplicity. By the end of this article, we will have a nested template [Echo](https://echo.labstack.com/) project setup.

If you already have an idea on how [Echo](https://echo.labstack.com/) works, jump to the [Using a nested template section](#b8ff).

### A basic Echo project setup

#### Create the project folder under the proper $GOPATH

The complete project code is hosted on [Gitlab](https://gitlab.com/ykyuen/golang-echo-template-example). First we’ll create the project folder here: _$GOPATH/src/gitlab.com/ykyuen/golang-echo-template-example_.

#### Create the main.go

Inside the newly created folder, let’s just copy the hello world example from the [Echo](https://echo.labstack.com/) official site and create the _main.go_.

**main.go**

#### Download the Echo package using dep

Simply run **dep init** if [dep](https://github.com/golang/dep) is installed. You can refer to this post for more information about dep: [Manage Go dependencies using dep](https://blog.boatswain.io/post/manage-go-dependencies-using-dep/).

Or run **go get github.com/labstack/echo** to download the [Echo](https://echo.labstack.com/) package in _$GOPATH_.

#### Run the hello world

Start the application by typing **go run main.go** and then visit [http://localhost:1323](http://localhost:1323) through the browser or the **curl** command.

![Image](https://cdn-media-1.freecodecamp.org/images/1*aExSnI6KPWva_VRT2-2wGg.jpeg)
_Start the Echo server._

![Image](https://cdn-media-1.freecodecamp.org/images/1*j-u3NXp7_u7PTVUiYVGwFA.jpeg)
_Send a request and get the hello world._

### Return a JSON response

When building a RESTful API, it is more likely that the client wants to receive a JSON response instead of a string. Let’s write some [Go](https://golang.org/) code in _main.go_.

**main.go**

### Return an HTML

Similar to returning a JSON object, we just need to call another method in the **return** statement.

**main.go**

The above are just two simple examples. [Echo](https://echo.labstack.com/) has a few more convenient ways to return JSON and HTML. For details please refer to the [documentation](https://echo.labstack.com/guide/response).

#### Render HTML using template engine

As mentioned at the very beginning, we could implement a template engine when returning the HTTP response. But before that, let’s restructure the project as follows:

**main.go**

In this _main.go_, we define a type called **TemplateRegistry** and implement the **Renderer** interface. A **Renderer** is a simple interface which wraps the **Render()** function. Inside a **TemplateRegistry** instance, it has a **templates** field containing all the templates needed for the [Echo](https://echo.labstack.com/) server to render the html response, and this is configured in the **main()** flow.

On the other hand, we define the **HomeHandler** in order to keep the logic in a separate file.

**handler/home_handler.go**

When the **c.Render()** is invoked, it executes the template which is already set in our **TemplateRegistry** instance as stated in **main.go**. The three parameters are:

1. HTTP response code
2. The template name
3. The data object which could be used in the template

**view/home.html**

This above template is named **home.html** as stated in the **define** statement. It can read the **name** and **msg** strings from **c.Render()** for the **<tit**le>**; an**d <h1> tags.

#### Using nested template

In the above setup, every HTML template has a complete set of HTML code and many of them are duplicated. Using nested templates makes it easier to maintain the project.

Originally the **templates** field in the **TemplateRegistry** contained all the templates files. In the new setup, we made it into an array field and each array item is a single set of template files for a particular HTML page.

We add a few files to the project and it should look like this:

The code below is based on this [gist](https://gist.github.com/rand99/808e6e9702c00ce64803d94abff65678) created by [rand99](https://gist.github.com/rand99).

**main.go**

We add a new route **/about** which is handled by an **AboutHandler.** As you can see from the above lines [34-36](https://gist.github.com/ykyuen/a8bcf35a338f398ddfe61275ac91e439#file-main-go-L34-L36), the **templates** array contains different sets of template files for different HTML pages. The **Render()** takes the **name** parameter as the **templates** array key so it can execute the correct template set.

**view/base.html**

The **template** statement tells the template engine that it should look for the **{{title}}** and **{{body}}** definitions in the template set, and they are defined in the **home.html** as well as **about.html**.

**view/about.html**

And here is the **AboutHanlder** which has no big difference from the **HomeHandler**.

**handler/about_handler.go**

### Summary

This is just a basic example implementing nested templates using the [Go](https://golang.org/) standard [html/template](https://godoc.org/html/template) library in [Echo](https://echo.labstack.com/). With proper setup, we could develop a more customized and convenient pattern for [Echo](https://echo.labstack.com/) or even make it work with any other template engines.

The complete example can be found on [gitlab.com](https://gitlab.com/ykyuen/golang-echo-template-example).

— Originally posted on [Boatswain Blog](https://blog.boatswain.io/post/setup-nested-html-template-in-go-echo-web-framework/).

