---
title: How the Model View Controller Architecture Works – MVC Explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-04T20:51:41.000Z'
originalURL: https://freecodecamp.org/news/model-view-architecture
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--15--1.png
tags:
- name: software architecture
  slug: software-architecture
seo_title: null
seo_desc: "By Nishant Kumar\nOver the last 20 years, websites have changed from simple\
  \ pages with a little CSS to become much more complex and powerful applications.\
  \ \nTo make these applications easier to develop, programmers use different patterns\
  \ and software a..."
---

By Nishant Kumar

Over the last 20 years, websites have changed from simple pages with a little CSS to become much more complex and powerful applications. 

To make these applications easier to develop, programmers use different patterns and software architectures to make the code less complicated.

## But first, what is software architecture?

An architecture is a systematic way in which software is described. It also refers to its relationship with other software, and how they interact with each other.

Software architecture also includes other factors such as business strategy, quality attributes, human dynamics, design, and the IT environment.

In other words, an architecture serves as a **blueprint for a system**.

## Model-View-Controller (MVC) Architecture

The most popular software architecture, by far, is the Model-View-Controller, or MVC.

MVC divides any large application into three parts:

1. The Model
2. The View
3. The Controller

Each of these components is built to handle a specific aspect of an application and has different purposes.

### The Model

The model contains all the data-related logic that the user works with, like the schemas and interfaces of a project, the databases, and their fields.

For example, a customer object will retrieve the customer information from the database, manipulate or update their record in the database, or use it to render data.

### The View

The view contains the UI and the presentation of an application.

For example, the customer view will include all the UI components such as text boxes, dropdowns, and other things that the user interacts with.

### The Controller

And finally, the controller contains all the business-related logic and handles incoming requests. It is the interface between the Model and the View.

For example, the customer controller will handle all the interactions and inputs from the customer view and update the database using the customer model. The same controller will be used to view the customer data.

Here's a diagram to help visualize the MVC architecture, and how everything works together:

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--15-.png)
_Flow diagram of the Model View Controller_

## How MVC Architecture works

First, the browser sends a request to the Controller. Then, the Controller interacts with the Model to send and receive data.

The Controller then interacts with the View to render the data. The View is only concerned about how to present the information and not the final presentation. It will be a dynamic HTML file that renders data based on what the Controller sends it.

Finally, the View will send its final presentation to the Controller and the Controller will send that final data to the user output.

The important thing is that the View and the Model never interact with each other. The only interaction that takes place between them is through the Controller.

This means the logic of the application and the interface never interacts with each other, which makes writing complex applications easier.

Let’s look at a simple example:

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--16-.png)

Let's see what's going on here. First, a user inputs that they want a list of movies through a web browser or a mobile application.

The browser will then send the request to the Controller to get the list of movies.

Next, the Controller will ask the Model to find the list of movies from the database. 

```express
router.get('/',ensureAuth, async (req,res)=>{ 
	try{ 
		const movies = await Movies.find() (*) 
		res.render('movies/index',{ movies }) 
    } 
    
	catch(err){ console.error(err) 
		res.render('error/500') } })     
```

Then the Model searches the database and returns the list of movies to the Controller.

```express
const mongoose = require('mongoose') 
const MovieSchema = new mongoose.Schema
({ 
	name:{ 
        type:String, 
        required:true 
    }, 
	description:{ 
    	type:String 
    } 
}) 

module.exports = mongoose.model('Movies',MovieSchema)
```

If the Controller gets the list of movies from the Model, the Controller will ask the View to present the list of movies.

```express
router.get('/',ensureAuth, async (req,res)=>{ 
	try{ const movies = await Movies.find() 
		res.render('movies/index', { movies (*) }) } 

	catch(err){ 
    console.error(err) res.render('error/500') } 
})
```

‌Then the View will receive the request and returns the rendered list of movies to the Controller in HTML.

```html
<div class="col" style="margin-top:20px;padding-bottom:20px">
    <div class="ui fluid card"> 
        <div class="content"> 
        <div class="header">{{movie.title}}</div> 
        	</div> <div class="extra content"> 
            <a href="/movies/{{movie._id}}" class="ui blue button"> More from {{movie.description}} </a> 
        </div> 
    </div>
</div>
```

Lastly, the Controller will take that HTML and return it back to the user, thus getting the list of Movies as the output.

## Wrapping Up

There are a lot of software architectures out there, but Model-View-Controller is the most popular and widely used. It reduces the code complexity and makes the software easily understandable. 

Now you know the concepts behind the Model-View-Controller.  

> That’s all folks! Happy Learning!

