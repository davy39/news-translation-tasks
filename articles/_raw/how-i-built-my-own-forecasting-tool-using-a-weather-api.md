---
title: How I Built My Own Forecasting Tool Using a Weather API
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-11T17:50:21.000Z'
originalURL: https://freecodecamp.org/news/how-i-built-my-own-forecasting-tool-using-a-weather-api
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b25740569d1a4ca29f2.jpg
tags:
- name: api
  slug: api
- name: forecasting
  slug: forecasting
- name: weather
  slug: weather
seo_title: null
seo_desc: "By Anton Lawrence\nAbrupt weather and climate change are things that everybody\
  \ is dealing with. In fact, the vast majority of the global population relies on\
  \ accurate, real-time weather data and forecasts to make informed decisions.   \n\
  This has increa..."
---

By Anton Lawrence

Abrupt weather and climate change are things that everybody is dealing with. In fact, the vast majority of the global population relies on accurate, real-time [weather data and forecasts to make informed decisions](https://www.climate.gov/maps-data/primer/processing-climate-data).   
  
This has increased the importance of reliable Android and iOS weather apps. In this article, we will show you how to create a simple forecasting tool using NodeJS and a weather API.  
  
But before that, let’s go over the importance of weather apps.

# Why Do We Need Weather Apps?

A feature-rich [weather forecasting](https://en.wikipedia.org/wiki/Weather_forecasting) app can provide great value to various industries. Some noteworthy benefits of weather applications include:

* Providing immediate access to local weather conditions and upcoming forecast, thus saving you time.
* Providing real-time notifications about prevailing and expected weather conditions.
* Helping governments and local administrations prepare for natural disasters and save lives.
* Helping farmers take preventive measures.
* Facilitating the global travel and tourism industry.
* Providing clear weather forecasts which are crucial in the aviation and logistics industry.

# What You Need to Build a Weather App

  
Here are some of the things you will need to build a weather app successfully:  


* Familiarity working with JavaScript (Node.js)
* A text editor such as Notepad or an IDE. My favorite is Visual Studio.
* Access to a reliable weather API such as ClimaCell
* Access to a map service
* Knowledge of HTML, CSS, and Bootstrap

Once you have these ready, you’re good to go.

# Overview of the ClimaCell Weather API

![Image](https://paper-attachments.dropbox.com/s_09D7754335BDD40A8ECD55F1187847147F5C3FBE3BBD081087C52D1E8CDCDF32_1589167731846_climacell+api+weather.jpg)

ClimaCell is a popular weather provider that offers hyper-accurate [historical weather data](https://www.climate.gov/maps-data/dataset/past-weather-zip-code-data-table) as well as forecasts through an easy to consume API.

# The Building Process

In this section, I will show you how I created a forecasting app where a user enters their city or any other location by name and fetches weather data from the ClimaCell API. The API responds to the request by returning data, which is then displayed to the user.

## Install NodeJS and Create a New Project

  
For this project, we will use Node.js — one of the most popular run-time environments for JavaScript. Node.js helps developers create quick web applications. It has a wide range of libraries and modules for creating advanced web applications.  
  
If you do not have Node.js on your device, you can install it from the [official website](https://nodejs.org/en/).  
Once installed, we use this command to initialize npm - the default packet manager used by Node.js.  
  
`$ npm init` 

This creates our project, so you will be prompted to enter a few details such as package name, description, Git repository, and more.  
  
Next, we install the modules required to run our project. To generate a Node.js app skeleton, we use express - a framework for building Node.js web applications.  
  
`$ npm install express`  
  
Installing the express framework helps you run the server, handle client requests, and connect the right HTML template with a response.    
  
Next, we will also install unirest - a simple yet powerful solution that allows you to request a library.   
  
It will help us make requests to the ClimaCell API and handle the responses.   
  
Use this command:  
  
`npm install unirest`  
  
At this point, we’ve installed the necessary modules, and the project is ready.  
Next, we generate a weather app using the express generator tool. On the command line, type this:  
  
`express --view=pug weather-app-nodejs`  
   
You should now have a view like this on the command line:

![Image](https://paper-attachments.dropbox.com/s_09D7754335BDD40A8ECD55F1187847147F5C3FBE3BBD081087C52D1E8CDCDF32_1589167675672_create+weather+app.png)

## Get the ClimaCell Weather API

To get access to the ClimaCell API, you will need to sign up for an account on their page. 

![Image](https://paper-attachments.dropbox.com/s_09D7754335BDD40A8ECD55F1187847147F5C3FBE3BBD081087C52D1E8CDCDF32_1589187768233_CLIMACELL+DASHBOARD.png)

Once you create an account, sign in to their Microweather API dashboard which looks like this:  


![Image](https://paper-attachments.dropbox.com/s_09D7754335BDD40A8ECD55F1187847147F5C3FBE3BBD081087C52D1E8CDCDF32_1589188690033_dashboard.png)

  
On the dashboard, click on references to check the API endpoints. As you can see, the ClimaCell API has a number of endpoints including the short term forecast, hourly forecast, real time data, and more.

![Image](https://paper-attachments.dropbox.com/s_09D7754335BDD40A8ECD55F1187847147F5C3FBE3BBD081087C52D1E8CDCDF32_1589191651855_API+endpoints.png)

Worth a mention is that each endpoint has its own code snippet. For example, here is the Node.js code snippet for getting real time weather data.

![Image](https://paper-attachments.dropbox.com/s_09D7754335BDD40A8ECD55F1187847147F5C3FBE3BBD081087C52D1E8CDCDF32_1589192780403_carbon.png)
_[Raw](https://carbon.now.sh/embed?bg=rgba(0%2C0%2C0%2C1)&amp;t=blackboard&amp;wt=none&amp;l=javascript&amp;ds=true&amp;dsyoff=20px&amp;dsblur=68px&amp;wc=true&amp;wa=true&amp;pv=56px&amp;ph=56px&amp;ln=false&amp;fl=1&amp;fm=Hack&amp;fs=14px&amp;lh=133%25&amp;si=false&amp;es=1x&amp;wm=false&amp;code=router.post(%27%252Fweather%27%252C%2520function(req%252C%2520res%252C%2520next)%257B%250A%250A%2520%2520let%2520city%2520%253D%2520req.body.city%253B%250A%250A%2520%2520url%2520%253D%2520url%252Bcity%252B%2522%2526%2522%252BappId%253B%250A%250A%2520request(url%252C%2520function%2520(error%252C%2520response%252C%2520body)%2520%257B%250A%250A%2520%2520%2520%2520%2520%2520body%2520%253D%2520JSON.parse(body)%253B%250A%250A%2520%2520%2520%2520%2520%2520if(error%2520%2526%2526%2520response.statusCode%2520!%253D%2520200)%257B%250A%250A%2520%2520%2520%2520%2520%2520%2520%2520throw%2520error%253B%250A%250A%2520%2520%2520%2520%2520%2520%257D%250A%250A%2520%2520%2520%2520let%2520country%2520%253D%2520(body.sys.country)%2520%253F%2520body.sys.country%2520%253A%2520%27%27%2520%253B%250A%250A%2520%2520%2520%2520let%2520var%2520request%2520%253D%2520require(%2522request%2522)%253B%250A%250Avar%2520options%2520%253D%2520%257B%250A%2520%2520method%253A%2520%27GET%27%252C%250A%2520%2520url%253A%2520%27https%253A%252F%252Fapi.climacell.co%252Fv3%252Fweather%252Frealtime%27%252C%250A%2520%2520qs%253A%2520%257Bapikey%253A%2520%279efRx8KrGKa6ME0ORWIJz7TaNjuRQAvb%27%257D%250A%257D%253B%250A%250Arequest(options%252C%2520function%2520(error%252C%2520response%252C%2520body)%2520%257B%250A%2520%2520if%2520(error)%2520throw%2520new%2520Error(error)%253B%250A%250A%2520%2520console.log(body)%253B%250A%257D)%253B%2520%253D%2520%2522For%2520city%2520%2522%252Bcity%252B%27%252C%2520country%2520%27%252Bcountry%253B%250A%250A%2520%2520%2520%2520res.render(%27index%27%252C%2520%257Bbody%2520%253A%2520body%252C%2520forecast%253A%2520forecast%257D)%253B%250A%250A%2520%2520%2520%257D)%253B%250A%250A%257D)%253B" rel="noreferrer nofollow noopener)_

## Modifying the application

To call the ClimaCell API, we need to first edit some files. Here, you can use Notepad or open the project directory in your IDE for easier editing. It should appear as shown:

![Image](https://paper-attachments.dropbox.com/s_09D7754335BDD40A8ECD55F1187847147F5C3FBE3BBD081087C52D1E8CDCDF32_1589180215929_repo.png)

We start modifying our files by adding bootstrap to layout.pug. Open the views directory and insert this snippet to the file.

![Image](https://paper-attachments.dropbox.com/s_09D7754335BDD40A8ECD55F1187847147F5C3FBE3BBD081087C52D1E8CDCDF32_1589170180082_carbon+1.png)
_[Raw](https://carbon.now.sh/embed?bg=rgba(0%2C0%2C0%2C1)&amp;t=blackboard&amp;wt=none&amp;l=javascript&amp;ds=true&amp;dsyoff=20px&amp;dsblur=68px&amp;wc=true&amp;wa=true&amp;pv=56px&amp;ph=56px&amp;ln=false&amp;fl=1&amp;fm=Hack&amp;fs=14px&amp;lh=133%25&amp;si=false&amp;es=1x&amp;wm=false&amp;code=doctype%2520html%250Ahtml(lang%253D%2522en%2522)%250A%2520%2520head%250A%2520%2520%2520%2520title%2520Weather%2520Forecast%2520Tool%2520using%2520Climacell%2520API%250A%2520%2520%2520%2520meta(charset%253D%2522utf-8%2522)%250A%2520%2520%2520%2520meta(name%253D%2522viewport%2522%2520content%253D%2522width%253Ddevice-width%252C%2520initial-scale%253D1%2522)%250A%2520%2520%2520%2520link(rel%253D%2522stylesheet%2522%2520href%253D%2522https%253A%252F%252Fmaxcdn.bootstrapcdn.com%252Fbootstrap%252F3.3.7%252Fcss%252Fbootstrap.min.css%2522)%250A%2520%2520%2520%2520script(src%253D%2522https%253A%252F%252Fajax.googleapis.com%252Fajax%252Flibs%252Fjquery%252F3.3.1%252Fjquery.min.js%2522)%250A%2520%2520%2520%2520script(src%253D%2522https%253A%252F%252Fmaxcdn.bootstrapcdn.com%252Fbootstrap%252F3.3.7%252Fjs%252Fbootstrap.min.js%2522)%250A%2520%2520body%250A%2520%2520%2520%2520block%2520content" rel="noreferrer nofollow noopener)_

Next, we create a form by adding the snippet below to index.pug file.  


![Image](https://paper-attachments.dropbox.com/s_09D7754335BDD40A8ECD55F1187847147F5C3FBE3BBD081087C52D1E8CDCDF32_1589170264156_carbon.png)

Notice how we use the [HTTP post method](https://en.wikipedia.org/wiki/POST_(HTTP)) to send data to the server. The code above also sets the action parameter to weather route and adds the text input as “city.”    
An input button to fetch the weather is also added.   
  
We now create an HTML table just below the form to display fetched weather records.

![Image](https://paper-attachments.dropbox.com/s_09D7754335BDD40A8ECD55F1187847147F5C3FBE3BBD081087C52D1E8CDCDF32_1589171285500_carbon+2.png)
_[Raw](https://carbon.now.sh/embed?bg=rgba(0%2C0%2C0%2C1)&amp;t=blackboard&amp;wt=none&amp;l=htmlmixed&amp;ds=true&amp;dsyoff=20px&amp;dsblur=68px&amp;wc=true&amp;wa=true&amp;pv=56px&amp;ph=56px&amp;ln=false&amp;fl=1&amp;fm=Hack&amp;fs=14px&amp;lh=133%25&amp;si=false&amp;es=1x&amp;wm=false&amp;code=.row%250A%2520%2520%2520%2520%2520%2520%2520.col-md-12%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520p%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520br%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520br%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520strong%2520Weather%2520Forecast%2520%2523%257Bforecast%257D%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520table.table%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520thead%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520tr%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520th%2520Longitude%2520%252F%2520Latitude%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520th%2520Pressure%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520th%2520Temprature%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520th%2520Humidty%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520tbody%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520if%2520body%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520tr%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520td%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2523%257Bbody.coord.lon%257D%2520%252F%2520%2523%257Bbody.coord.lon%257D%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520td%2520%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2523%257Bbody.main.pressure%257D%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520td%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2523%257Bbody.main.temp%257D%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520td%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2523%257Bbody.main.humidity%257D%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520else%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520tr%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520td(colspan%253D%25226%2522)%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%257C%2520Enter%2520city%2520name%2520and%2520click%2520Fetch%2520Weather%2520button" rel="noreferrer nofollow noopener)_

Inserting the code snippet above creates a table that looks like this:

![Image](https://paper-attachments.dropbox.com/s_09D7754335BDD40A8ECD55F1187847147F5C3FBE3BBD081087C52D1E8CDCDF32_1589196907929_Weather+1.png)

## Calling the ClimaCell API

To send requests to the ClimaCell API, we must install the [request module](https://nodejs.dev/making-http-requests-with-nodejs).  
  
`npm i request --save`  
  
Next, we add the ClimaCell API credentials in the index.js file. Open the file in your routes directory and add the API key you obtained on the ClimaCell dashboard:  


![Image](https://paper-attachments.dropbox.com/s_09D7754335BDD40A8ECD55F1187847147F5C3FBE3BBD081087C52D1E8CDCDF32_1589171891228_example+key.png)

  
Here is the code to add API credentials:  


![Image](https://paper-attachments.dropbox.com/s_09D7754335BDD40A8ECD55F1187847147F5C3FBE3BBD081087C52D1E8CDCDF32_1589172288863_carbon+4.png)
_[Raw](https://carbon.now.sh/embed?bg=rgba(0%2C0%2C0%2C1)&amp;t=blackboard&amp;wt=none&amp;l=javascript&amp;ds=true&amp;dsyoff=20px&amp;dsblur=68px&amp;wc=true&amp;wa=true&amp;pv=56px&amp;ph=56px&amp;ln=false&amp;fl=1&amp;fm=Hack&amp;fs=14px&amp;lh=133%25&amp;si=false&amp;es=1x&amp;wm=false&amp;code=let%2520url%2520%2520%2520%2520%253D%2520%27https%253A%252F%252Fclimacell-microweather-v1.p.rapidapi.com%252Fweather%252Frealtime%27%250Alet%2520appId%2520%2520%253D%2520%27appid%253DYOUR%2520API%2520KEY%27%253B%250Alet%2520units%2520%2520%253D%2520%27%2526units%253Dmetric%27%253B%2520%250Avar%2520request%2520%253D%2520require(%27request%27)%253B" rel="noreferrer nofollow noopener)_

  
After adding the API credentials, we update the index route. This is done by replacing the code section in **‘/’** route in index.js file.

![Image](https://paper-attachments.dropbox.com/s_09D7754335BDD40A8ECD55F1187847147F5C3FBE3BBD081087C52D1E8CDCDF32_1589172437273_carbon+5.png)
_[Raw](https://carbon.now.sh/embed?bg=rgba(0%2C0%2C0%2C1)&amp;t=blackboard&amp;wt=none&amp;l=javascript&amp;ds=true&amp;dsyoff=20px&amp;dsblur=68px&amp;wc=true&amp;wa=true&amp;pv=56px&amp;ph=56px&amp;ln=false&amp;fl=1&amp;fm=Hack&amp;fs=14px&amp;lh=133%25&amp;si=false&amp;es=1x&amp;wm=false&amp;code=%252F*%2520GET%2520home%2520page.%2520*%252F%250Arouter.get(%27%252F%27%252C%2520function(req%252C%2520res%252C%2520next)%2520%257B%250A%2520res.render(%27index%27%252C%2520%257B%27body%27%253A%27%27%252C%2520forecast%253A%2520%27%27%257D)%253B%250A%257D)%253B" rel="noreferrer nofollow noopener)_

We finish by creating the weather route in index.js.

![Image](https://paper-attachments.dropbox.com/s_09D7754335BDD40A8ECD55F1187847147F5C3FBE3BBD081087C52D1E8CDCDF32_1589172832852_carbon+6.png)
_[Raw](https://carbon.now.sh/embed?bg=rgba(0%2C0%2C0%2C1)&amp;t=blackboard&amp;wt=none&amp;l=javascript&amp;ds=true&amp;dsyoff=20px&amp;dsblur=68px&amp;wc=true&amp;wa=true&amp;pv=56px&amp;ph=56px&amp;ln=false&amp;fl=1&amp;fm=Hack&amp;fs=14px&amp;lh=133%25&amp;si=false&amp;es=1x&amp;wm=false&amp;code=router.post(%27%252Fweather%27%252C%2520function(req%252C%2520res%252C%2520next)%257B%250A%250A%2520%2520let%2520city%2520%253D%2520req.body.city%253B%250A%250A%2520%2520url%2520%253D%2520url%252Bcity%252B%2522%2526%2522%252BappId%253B%250A%250A%2520request(url%252C%2520function%2520(error%252C%2520response%252C%2520body)%2520%257B%250A%250A%2520%2520%2520%2520%2520%2520body%2520%253D%2520JSON.parse(body)%253B%250A%250A%2520%2520%2520%2520%2520%2520if(error%2520%2526%2526%2520response.statusCode%2520!%253D%2520200)%257B%250A%250A%2520%2520%2520%2520%2520%2520%2520%2520throw%2520error%253B%250A%250A%2520%2520%2520%2520%2520%2520%257D%250A%250A%2520%2520%2520%2520let%2520country%2520%253D%2520(body.sys.country)%2520%253F%2520body.sys.country%2520%253A%2520%27%27%2520%253B%250A%250A%2520%2520%2520%2520let%2520forecast%2520%253D%2520%2522For%2520city%2520%2522%252Bcity%252B%27%252C%2520country%2520%27%252Bcountry%253B%250A%250A%2520%2520%2520%2520res.render(%27index%27%252C%2520%257Bbody%2520%253A%2520body%252C%2520forecast%253A%2520forecast%257D)%253B%250A%250A%2520%2520%2520%257D)%253B%250A%250A%257D)%253B" rel="noreferrer nofollow noopener)_

  
This code snippet enables data in the input form to be posted to the index route. Once the user enters a city name, it is assigned to the city variable using the request object.   
  
The URL is then appended with the city name and ID and the request sent to ClimaCell API.  
  
The ClimaCell API server response is returned as a JSON file, which is then parsed and fed to the output template.  
  
For instance, if the user was looking for Boston weather forecasts, the app will return this:

![Image](https://paper-attachments.dropbox.com/s_09D7754335BDD40A8ECD55F1187847147F5C3FBE3BBD081087C52D1E8CDCDF32_1589196959089_WEATHER+2.png)

Note - The temperature in this example is shown in Kelvin and is equal to 50°F or 10°C.

## Add Maps to Visualize Your Data

You can integrate interactive maps into your forecasting application to enhance user experience. This can be achieved by using a third-party map service provider for web applications.  
  
Mapbox is one such tool that helps developers create awesome weather maps for their applications. It integrates seamlessly with any weather app.  
  
To use the Mapbox, sign up on their website and [check out their API](https://www.mapbox.com/install/). There are integrations for Android, iOS, Web, and Unity. In this case, we choose Web integration for our tool.  
  
We can either install the Mapbox CDN or use the module bundler. Let's use the module bundler.  
  
The first step would be installing the package  
  
`npm install Mapbox-gl –save`  
  
Next, we add the GL JS CSS file in the HTML file by including this snippet in the <head>  
  
`<link href='https://api.mapbox.com/mapbox-gl-js/v1.8.1/mapbox-gl.css' rel='stylesheet' />`  
  
We can now add the map to our application. To do this, use the code snippet below.

![Image](https://paper-attachments.dropbox.com/s_09D7754335BDD40A8ECD55F1187847147F5C3FBE3BBD081087C52D1E8CDCDF32_1589201956495_carbon+1.png)
_[Raw](https://carbon.now.sh/embed?bg=rgba(0%2C0%2C0%2C1)&amp;t=blackboard&amp;wt=none&amp;l=javascript&amp;ds=true&amp;dsyoff=20px&amp;dsblur=68px&amp;wc=true&amp;wa=true&amp;pv=56px&amp;ph=56px&amp;ln=false&amp;fl=1&amp;fm=Hack&amp;fs=14px&amp;lh=133%25&amp;si=false&amp;es=1x&amp;wm=false&amp;code=var%2520mapboxgl%2520%253D%2520require(%27mapbox-gl%252Fdist%252Fmapbox-gl.js%27)%253B%250A%2520%250Amapboxgl.accessToken%2520%253D%2520%27pk.eyJ1IjoiZGlja3Nvbi1tIiwiYSI6ImNrOXphd3MzZDBlMXYzbHFwM2kwbmlvbmkifQ.VE3RRbb8l78w9kxfmh_9ew%27%253B%250Avar%2520map%2520%253D%2520new%2520mapboxgl.Map(%257B%250Acontainer%253A%2520%27CONTAINER_ELEMENT_ID%27%252C%250Astyle%253A%2520%27mapbox%253A%252F%252Fstyles%252Fmapbox%252Fstreets-v11%27%250A%257D)%253B%250A" rel="noreferrer nofollow noopener)_

  
You can choose where to place the map by replacing the 

“CONTAINER_ELEMENT_ID’ .  
  
Here is a sample map generated using Mapbox:

![Image](https://paper-attachments.dropbox.com/s_09D7754335BDD40A8ECD55F1187847147F5C3FBE3BBD081087C52D1E8CDCDF32_1589202164225_map.png)

# What’s next?

At this point, much of the work is done, and your app can get weather forecasts for any city using the ClimaCell API. 

However, you can consider adding more interactive features to your application or extending its functionality. 

Here are some things you might want to do:

* Add a search function.
* Improve the look of your user interface.
* Query the application by ID or name.
* Display a list of target cities and their respective IDs.
* Add parameters to display additional weather data .
* Integrate real-time notifications and warning signals.

As you can see, the basic app building process is pretty simple and straightforward. By following the above process to leverage the power of a weather API, even beginner-level developers can get their weather application up and running in a matter of minutes.

