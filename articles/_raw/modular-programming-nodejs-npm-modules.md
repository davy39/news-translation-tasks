---
title: How Modular Programming Works in Node.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-17T14:00:00.000Z'
originalURL: https://freecodecamp.org/news/modular-programming-nodejs-npm-modules
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/alternateimg.png
tags:
- name: backend
  slug: backend
- name: JavaScript
  slug: javascript
- name: node
  slug: node
- name: node js
  slug: node-js
- name: npm
  slug: npm
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Sarvesh Kadam

  Modules are one of the fundamental features of Node.js.

  When you''re building an application, as the code becomes more and more complex
  you cannot put your entire code in one single file.

  As this becomes unmanageable, you can use Node...'
---

By Sarvesh Kadam

Modules are one of the fundamental features of Node.js.

When you're building an application, as the code becomes more and more complex you cannot put your entire code in one single file.

As this becomes unmanageable, you can use Node's module pattern to write different files and export them (including functions, objects, and methods) to the main file.

Now you might ask – what exactly is a `module`?

In simple terms, a `module` is nothing but a JavaScript file. That's It.

With Node's modular functionality, we can import our own external files, core (Native) node modules, and NPM modules. In this article, we'll discuss each one of these in detail.

## **How to import your own files**

In this article, we are going to discuss how we can export and import our own files.

Basically, there are two files: `calculate.js`, from where we will export, and `main.js` to where we will import that file.

![mduleexport.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1603082860893/xGgR903x4.png)

We have both files in the same folder to keep it simple.

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1603015526076/cwIgq_IuU.png)

### How to import a function

```js
//---- Exported file [calculate.js] ----
const add = (a,b)=>{
    return a + b
}

module.exports = add

```

Here we export a function called `add` using `module.exports`. Then this function gets imported to a different file using the `require` method.

In Node, each file is referred to as a `module`, and `exports` is a property of the module Object.

We can now invoke the function in the different file, that is `main.js`, by passing the arguments as shown below.

```js
//------ Main File[main.js] ----

const add = require('./calculate') //name of the desired file
const result = add(2,4)
console.log(result); //Output : 6


```

### How to import an object 

We can also export an entire object and access the different methods in it.

```js
//---- Exported file [calculate.js]  ----
const add = {
    result : (a,b)=>{
        return a + b
    }
}
module.exports = add


```

We exported the object `add` and imported it to our main file using the `require` method.

We can now access the `result` method of the `add` object using the `.` dot operator:

```javascript
//---- Main file[main.js] ----
const add = require('./calculate')

const result = add.result(5,8)

console.log(result) //Output : 13


```

Another way we can export the above object is by only exporting the method which we require rather than the entire object.

```js
//---- Exported file [calculate.js]  ----
const add = {
    result : (a,b)=>{
        return a + b
    }
}

module.exports = add.result

```

As you can see, we are importing the `result` method in the `add` object. So this method can be directly invoked in the main file.

This is good practice if you don't need the entire object but only require some methods/functions of it. It also makes our code more secure.

```javascript
//---- Main file[main.js] ----

const add = require('./calculate')
const result = add(5,8)
console.log(result) //Output : 13


```

### How to import a Function Constructor: 

A function constructor is basically used to create a new instance of an object which possesses the same properties as that of the main object/function.

In the below case, we create a new instance of the 'Add' object using the `new` keyword. This process where we create an instance of an object is called 'instantiation'.

Then we export this instance using `module.exports`:

```js
//---- Exported file [calculate.js]  ----

function Add (){
    this.result = (a,b)=>{
        return a + b
    }
}

module.exports = new Add()


```

Now we can import it into our main file and access the 'result' method inside it, to get our calculated value.

```js
//---- Main file[main.js] ----

const add = require('./calculate2')
const result = add.result(1,3)
console.log(result); //Output : 4


```

This way we can export and import a function constructor.

There is another way we can do this, which is by creating our new instance in the main file rather than in the exported file as shown above `module.exports = new Add()`.

We'll see how this works when we export ES6 Classes which works similar to Function constructors.

### How to import ES6 Classes

`class` is a special type of function where the `class` keyword helps initialize it. It uses the `constructor` method to store the properties. 

Now we are going to export the entire `class` using `module.exports`:

```js
//---- Exported file [calculate.js]  ----

const Add = class{
    constructor(a,b){
        this.a = a;
        this.b = b;
    }

    result(){
        return this.a + this.b
    }
}

module.exports = Add;


```

Now in our main file, we create a new instance using the `new` keyword and access the `result` method to get our calculated value.

```js

//---- Main file[main.js] ----

const add = require('./calculate')

const result = new add(2,5)

console.log(result.result()); //Output : 7


```

## How to Import Node Core (Native) Modules

Rather than creating our own custom modules every time, Node provides a set of modules to make our lives easier.

We are going to discuss some of the modules, but you can find the entire list in the official node API document [here](https://nodejs.org/dist/latest-v15.x/docs/api/).

Importing Node modules is similar to how you import your own modules. You use the same `require()` function to access it in your own file.

But there are some modules which you may have used unknowingly which do not need to be imported. For example `console.log()` – we have used the `console` module many times without fetching it in our own local file as these methods are available **globally**.

Let's look at one of the Core Native Modules which is **File System** (`fs`).  
There are n number of operations we can perform with the file system module such as reading a file, writing a file, and updating it, to name a few.

We are going to use the `fs` module to read a file. Even in this method, there are two ways we can perform this action: one by using the synchronous function `fs.readFileSync()`, and the other by asynchronous function `fs.readFile()`.

We'll discuss synchronous-asynchronous Node functions in future posts.

Today, we'll use the asynchronous version, that is `fs.readFile()`.

For this example, we have created two files: `main.js`, where we are going to perform the file reading operation, and `file.txt` which is the file we are going to read.

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1603442034534/DRk8tK6B8.png)

The`file.txt` contains some text in it.

```txt
Hello World!
```

Now, we use the `fs` module to read the file, without importing it, as shown below:

```js
fs.readFile('./file.txt','utf-8',(err,data)=>{
    if (err) throw err
    console.log(data);
})
```

It will throw an error as `fs` is not defined. That is because the file system `fs` module is not available globally like the `console` module is.

```powershell
ReferenceError: fs is not defined
    at Object.<anonymous> (C:\Users\Sarvesh Kadam\Desktop\Training\blog\code snippets\Node Modular Pattern\main.js:3:1)
    at Module._compile (internal/modules/cjs/loader.js:1256:30)
    at Object.Module._extensions..js (internal/modules/cjs/loader.js:1277:10)
    at Module.load (internal/modules/cjs/loader.js:1105:32)
    at Function.Module._load (internal/modules/cjs/loader.js:967:14)
    at Function.executeUserEntryPoint [as runMain] (internal/modules/run_main.js:60:12)
    at internal/main/run_main_module.js:17:47

```

Therefore, we need to import all the data from the file system module using the `require()` function and store all that data in a variable `fs`.

```js
const fs = require('fs')

fs.readFile('./file.txt','utf-8',(err,data)=>{
    if (err) throw err
    console.log(data);
})
```

Now you can name that variable anything. I named it `fs` for readability and it's the standard which most developers follow.

Using the `fs` variable we can access the `readFile()` method where we passed three arguments Those arguments are file path, character encoding `utf-8`, and the callback function to give an output.

You might ask why we're passing `utf-8` as our argument in the `readFile()`?

Because it encodes the value and gives the text as an output rather than giving a buffer as shown below:

`<Buffer 48 65 6c 6c 6f 20 57 6f 72 6c 64 21 21>`

The callback function, in turn, has two arguments: an error (`err`) and the actual content in the file (`data`). Then we print that `data` in the console.

```powershell
//Output:
Hello World!


```

## **How to Import NPM Modules** 

So what exactly is Node Package Manager?  
  
The package is a piece of code that is managed by the Package Manager. It is nothing but software that manages the installation and updating of packages.

NPM as per the official [documentation](https://docs.npmjs.com/):

> NPM is the world's largest software registry. Open-source developers from every continent use npm to share and borrow packages and many organizations use npm to manage private development as well.

So, in NPM we use somebody else's open-source code managed by NPM by importing it into our project.  
  
NPM usually comes with Node JS when you download it. You can check if NPM is installed on your machine by simply running the command `npm -v` on your command-prompt. If it returns some version number, that means NPM is successfully installed.

NPM has its registry at [npmjs.com](https://docs.npmjs.com/) where you can discover packages that you can use.

Let's look at one of the packages called [chalk](https://www.npmjs.com/package/chalk) which is basically used for terminal styling.

![chalknpm2.jpg](https://cdn.hashnode.com/res/hashnode/image/upload/v1603909979665/T6w4cd8qR.jpeg)

In the above figure, we can see the weekly downloads of the package which suggests how popular is it.  
  
Also, you can see that this package has dependencies in it. So this module which will serve as a dependency on our project is itself dependent on other modules.  
This entire management process is taken care of by the Package Manager.  
  
Even the source code is which is present on GitHub is given to us. We can navigate to it and verify if there are any open issues present.  
  
One more thing before moving forward: the NPM packages come in different versions. The pattern which the version follows is semantic versioning.  
  
As you can see, the latest version of the [chalk](https://www.npmjs.com/package/chalk) module when I wrote this article is **4.1.0.**

It follows the semantic versioning `Major_changes`**.**`Minor_changes`**.**`Patch` pattern.

`Major_changes`, as the name stands, are the significant changes made on the module which might affect your existing code.  
  
`Minor_changes` are new enhancements or features along with defect fixes that have been added which should not affect your existing code.  
  
`Patch` is the small bug fixes that will not crash your existing code.

You can learn more about semantic versioning on [semver.org](https://semver.org/).

#### How to Install NPM

Now to import any package from NPM, you first need to initialize NPM on your local project folder by running the command on the command prompt:

```powershell
npm init

```

Once you run the above command, it will ask you for some data as shown below such as package name, version, and so on.

Much of this data can be kept as default as mentioned in the Round brackets **()**.  
Also, the fields such as `author` and `license` are for the folks who created those NPM packages.

On the other hand, we are just importing and using them to create our own application.

```powershell
package name: (code_npm) code_npm
version: (1.0.0) 1.0.0
description: npm demo
entry point: (index.js) index.js
test command: test
git repository:
keywords: npm test
author: Sarvesh
license: (ISC)


```

Once you enter all the fields, it will create a JSON file with values that have the above properties, and it'll ask you for confirmation like this:

```powershell
Is this OK? (yes) yes

```

Once you've confirmed `yes` it will create a `package.json` file with all the data you entered as illustrated below:

```json
{
  "name": "code_npm",
  "version": "1.0.0",
  "description": "npm demo",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [
    "npm",
    "test"
  ],
  "author": "Sarvesh",
  "license": "ISC"
}


```

Also, you can see a `script` object that has a `test` property added. You can run it using the `npm test` command and it will give back the desired output like this:

```powershell
"Error: no test specified"

```

Now instead of doing this elongated method of initializing NPM and entering the custom properties values, you can simply run the command:

```powershell
npm init -y

```

Once you run this command, it will directly create a `package.json` file with the default values.

![pkgjson.PNG](https://cdn.hashnode.com/res/hashnode/image/upload/v1603968825440/3fcyAhRJG.png)

  
Now to install the latest version of the **chalk** package in your project, you need to execute the command:

```powershell
npm install chalk

```

You can also install any specific version you need of chalk by just adding `@version number` as shown below. Also instead of `install` you can simply put the short-hand `i` flag which stands for installation:

```
npm i chalk@4.0.0

```

This will install two things, a `node_modules` folder, and a `package-lock.json` file.

![folderdir.PNG](https://cdn.hashnode.com/res/hashnode/image/upload/v1603968346848/EAws9k06a.png)

  
Also, it will add a new property called `dependencies` to our `package.json` file which contains the name of the package installed and its version.

```json
"dependencies": {
    "chalk": "^4.0.0"
  }

```

The `node_module` folder contains the packages folder and its dependency's folders. It gets modifies as and when the npm package gets installed.  
  
The `package-lock.json` contains the code which makes NPM faster and more secure.

```json
"chalk": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/chalk/-/chalk-4.0.0.tgz",
      "integrity": "sha512-N9oWFcegS0sFr9oh1oz2d7Npos6vNoWW9HvtCg5N1KRFpUhaAhvTv5Y58g880fZaEYSNm3qDz8SU1UrGvp+n7A==",
      "requires": {
        "ansi-styles": "^4.1.0",
        "supports-color": "^7.1.0"
      }

```

It mainly contains properties such as `version`, which is the semantic version number.  
  
The `resolved` property is the directory or location from which the package was fetched. In this case it was fetched from [chalk](https://www.npmjs.com/package/chalk).  
  
The `integrity` property is to make sure that we get the same code if we install the dependency again.  
  
The `requires` object property represents the dependency of the `chalk` package.

**Note**: Do not make any changes to these two files `node_modules` and `package-lock.json`

#### How to Use NPM

Now once we've installed chalk to our project, we can import it to our root project file using the `require()` method. Then we can store that module in a variable called `chalk`.

```js
const chalk = require('chalk')

console.log(chalk.red("Hello World"))
```

Using the `red()` method of the `chalk` package, we have styled the "Hello World" text color in red.

On running the command `node index.js` we get the following output:

![chalkop.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1603966334203/3ulfhvZnz.png)

Now there are many ways you can style your command line output using the chalk package. For more information you can refer to the [Chalk official document](https://www.npmjs.com/package/chalk) on NPM.

Also, you can install the NPM packages globally (that is, on our operating system) rather than installing it in your local project by adding the `-g` flag on the command line (which stands for global, as mentioned below):

```powershell
npm i nodemon -g

```

This global package will not affect our `package.json` in any way since it is not installed locally.

We have installed the `nodemon` package globally which is used for automatic restart of a Node application when file changes in the directory are observed.  
You can refer to [nodemon](https://www.npmjs.com/package/nodemon) for more information.

We can use the nodemon package by running the application using this command:

```powershell
nodemon index.js

```

It works similarly to `node index.js`, except it keeps an eye on the file changes and it restarts the application once changes are detected.

```powershell
[nodemon] 2.0.6
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `node index.js`
Hello World

```

**Note**: The `chalk` styling will probably not work when you used `nodemon`.

Finally, we will go through the `dev dependencies`. There are some NPM packages or modules which we won't need in our project's production environment, but only for our development requirements.

We can install these modules in our project using the `dev` flag as shown below:

```powershell
 npm i nodemon --save-dev

```

It then creates a new property in the `package.json` called `devDependencies`:

```json
"devDependencies": {
    "nodemon": "^2.0.6"
  }

```

## Conclusion

Using Node's Module Pattern, we can import from our own files by exporting them in form of functions, objects, function constructors, and ES6 classes.

And Node has its own set of Core (Native) Modules which we can use. Some of them are available globally, while some of them need to be imported locally in your project/folder.

NPM is a package manager that manages 3rd party open source code which we can use in our project. Before using NPM modules, you need to initialize NPM locally using `npm init` on your command line in the root of your project folder.

You can install any NPM package by using the command `npm i <package name>`. And you can install the NPM package globally using the `-g` flag. Also the package can be made development dependent using the `--save-dev` flag.

Thank you for reading! If you like this article, do reach out to me on [Twitter](https://twitter.com/kadamsarvesh10) as I continue to document my learning.

