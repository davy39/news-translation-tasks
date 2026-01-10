---
title: How to Easily Build Desktop Apps with HTML, CSS and Javascript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-04T21:53:22.000Z'
originalURL: https://freecodecamp.org/news/how-to-easily-build-desktop-apps-with-html-css-and-javascript-d3e3f03f95a5
coverImage: https://cdn-media-1.freecodecamp.org/images/0*mwIqsFZSbnweFQuv
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Aditya Sridhar

  Can HTML, CSS and Javascript really be used to build Desktop Applications?

  The answer is yes.

  In this Article we will be focussing mainly on how Electron can be used to create
  desktop applications with Web Technologies like HTML, CS...'
---

By Aditya Sridhar

Can HTML, CSS and Javascript really be used to build Desktop Applications?

The answer is yes.

In this Article we will be focussing mainly on how Electron can be used to create desktop applications with Web Technologies like HTML, CSS and Javascript.

### Electron

[Electron](https://electronjs.org/) can be used to build Desktop Apps with HTML, CSS and Javascript. Also these apps work for multiple platforms like Windows, Mac, Linux and so on.

Electron combines Chromium and NodeJS into a single runtime. This enables us to run the HTML, CSS and Javascript code as a desktop application.

### Electron Forge

If Electron is used directly, then some manual setup is needed before building your application. Also if you want to use Angular, React, Vue or any other framework or library, you will need to manually configure for that.

[Electron Forge](https://electronforge.io/) makes the above things much easier.

It provides template applications with Angular, React, Vue and other frameworks which avoids the extra manual setups.

Also it provides an easy way to build and package the application. It also provides many other features which can be found in their [documenation](https://docs.electronforge.io/).

### Pre-requisites

Ensure you have NodeJS installed. It can be installed from [here](https://nodejs.org/en/).

Install Electron Forge globally using the following command:

```bash
npm install -g electron-forge
```

### Let’s get started with the application

Use the following command to create your application:

```bash
electron-forge init simple-desktop-app-electronjs
```

**simple-desktop-app-electronjs** is the name of the application.

The above command will take some time to run.

Once it finishes running, start the application using the following commands:

```bash
cd simple-desktop-app-electronjsnpm start
```

This should open up a window like the one shown below:

![Image](https://cdn-media-1.freecodecamp.org/images/OWyV2vj2yK654YopDS5YsLUAwclQrpA0AX2u)

### Understanding the Existing Folder Structure and Code

The application has a particular folder structure. Here I will be mentioning some of the important things in this folder structure.

#### package.json

It has information about the application you are creating, all the dependencies needed for the app, and some scripts. Some of the scripts are already pre configured, and you can add new scripts as well.

The **config.forge** path has all the configurations which are specific to ElectronJS. For example **make-targets** is used to specify the target make files for various platforms like Windows, Mac or Linux.

Also package.json has `"main": "src/index.js"` which indicates that src/index.js is the starting point of the application

#### src/index.js

According to package.json, **index.js** is the main script. The process which runs the main script is known as the **main process**. So the main process runs the index.js script.

The main process is used to display GUI elements. It does this by creating web pages.

Each web page created runs in a process called the **renderer process.**

#### Main process and renderer process

The purpose of the **main process** is to create web pages using a `BrowserWindow` Instance.

The `BrowserWindow` Instance uses a **renderer process** to run each web page.

**Each app can have only one main process but can have many renderer processes.**

It is possible to communicate between the main and the renderer process as well. This, however, will not be covered in this article.

![Image](https://cdn-media-1.freecodecamp.org/images/0nGfmUyxp4rC0GmbnhQk9OuJFm5f5xgO-WGE)
_Electron Architecture showing main and renderer process. The file names can vary._

**abcd.html** is shown as a second webpage in the above architecture. But in our code we won’t be having a second web page.

#### src/index.html

index.js loads the index.html file into a new BrowerWindow Instance.

What this basically means is that index.js creates a new GUI Window, and loads it with index.html web page. The index.html web page runs in its own renderer process.

#### Code in index.js explained

Most of the code created in index.js has good comments explaining what it does. Here I will mention a few key points to note in index.js:

```js
mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
  });

  // and load the index.html of the app.
  mainWindow.loadURL(`file://${__dirname}/index.html`);
```

The above code snippet basically creates a **BrowserWindow** Instance and loads **index.html** into the BrowserWindow.

You will see **app** used often in the code. For example take the below code snippet:

```js
app.on('ready', createWindow);
```

**app** is used to control the application’s event life cycle.

The above code snippet says that when the application is ready, load the first window.

Similarly, **app** can be used to perform other actions on various events. For example it can be used to perform some action right before the application closes and so on.

### Let’s create a Temperature Converter Desktop Application

Let us use the same application we used before and modify it slightly to create a temperature converter application.

First let us install Bootstrap with the following command:

```bash
npm install bootstrap --save
```

Copy the following code into src/index.html:

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Temperature Converter</title>
    <link rel="stylesheet" type="text/css" href="../node_modules/bootstrap/dist/css/bootstrap.min.css">

  </head>
  <body>
    <h1>Temperature Converter</h1>
    <div class="form-group col-md-3">
      <label for="usr">Celcius:</label>
      <input type="text" class="form-control" id="celcius" onkeyup="celciusToFahrenheit()">
    </div>
    <div class="form-group col-md-3">
      <label for="pwd">Fahrenheit:</label>
      <input type="text" class="form-control" id="fahrenheit" onkeyup="fahrenheitToCelcius()">
    </div>
    <script src='./renderer.js'></script>
  </body>
  </body>
</html>
```

The above code does the following:

1. Creates a text box with id **Celcius**. Whenever anything is typed in this textbox, the **celciusToFahrenheit()** function is called.
2. Creates a text box with id **Fahrenheit**. Whenever anything is typed in this textbox, the **fahrenheitToCelcius()** function is called.
3. Whenever a new value is typed in the Celcius text box, the value in the Fahrenheit text box displays the same temperature in Fahrenheit
4. Whenever a new value is typed in the Fahrenheit text box, the value in the Celcius text box displays the same temperature in Celcius

The 2 functions which do the temperature conversion are present in **renderer.js.**

Create a file called **renderer.js** inside **src**. Copy the following code into it:

```js
function celciusToFahrenheit(){
    let celcius = document.getElementById('celcius').value;
    let fahrenheit = (celcius* 9/5) + 32;
    document.getElementById('fahrenheit').value = fahrenheit;

}

function fahrenheitToCelcius(){
    let fahrenheit = document.getElementById('fahrenheit').value;
    let celcius = (fahrenheit - 32) * 5/9
    document.getElementById('celcius').value = celcius;
}
```

The **celciusToFahrenheit()** function reads the value in the **Celcius** text box, converts it to Fahrenheit, and writes the new temperature into the **Fahrenheit** text box.

The **fahrenheitToCelcius()** function does the exact opposite of this.

### Running the application

Run the application using the following command:

```bash
npm start
```

This should display the following window. Try it out with different values.

![Image](https://cdn-media-1.freecodecamp.org/images/RNlYkY-7y-zpWDFa6apV81oGv6E8cIsPX19B)

### Packaging the application

The command to package the application is:

```bash
npm run package
```

This command will take some time to run. Once it finishes check the **out** folder within the project folder.

I tested this in a Windows machine. This creates a folder called **simple-desktop-app-electronjs-win32-x64** inside the **out** folder

So in the **out/simple-desktop-app-electronjs-win32-x64** folder, the command creates an **.exe** file for this application. Clicking on the exe file automatically starts the desktop application.

The folder name **simple-desktop-app-electronjs-win32-x64** can be broken down as **appname-platform-architecture** where

* appname = simple-desktop-app-electronjs
* platform = win32
* architecture = x64

**When you run this command without any parameters, by default it packages for the platform which you are using for development.**

Let’s say you want to package for a different platform and architecture. Then you can use the following syntax:

```bash
npm run package -- --platform=<platform> arch=<architecture>
```

For example, in order to package for linux you can use the following command:

```bash
npm run package -- --platform=linux --arch=x64
```

This will create a folder called **simple-desktop-app-electronjs-linux-x64** inside the **out** folder.

### Creating a make File

In order to create a make file or an installer for the application, use the following command:

```bash
npm run make
```

This command will take some time to run. Once it finishes check the **out** folder within the project folder.

The **out/make** folder will have a Windows installer for the desktop application.

**When you run this command without any parameters, by default it creates the installer for the platform which you are using for development.**

### Code

The code for this desktop application is available in my GitHub repo:

[https://github.com/aditya-sridhar/simple-desktop-app-electronjs](https://github.com/aditya-sridhar/simple-desktop-app-electronjs)

### Congrats ?

You now know how to create desktop applications using HTML, CSS and Javascript.

This article covered very basic concepts of Electron and Electron-Forge.

To know more about them, you can check out their documentation.

### About the author

I love technology and follow the advancements in the field. I also like helping others with my technology knowledge.

Feel free to connect with me on my LinkedIn account [https://www.linkedin.com/in/aditya1811/](https://www.linkedin.com/in/aditya1811/)

You can also follow me on twitter [https://twitter.com/adityasridhar18](https://twitter.com/adityasridhar18)

My Website: [https://adityasridhar.com/](https://adityasridhar.com/)

Read more of my articles on my blog at [adityasridhar.com](https://adityasridhar.com/posts/desktop-apps-with-html-css-javascript).

