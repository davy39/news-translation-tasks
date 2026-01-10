---
title: 'How to Install Angular on Windows: A Guide to Angular CLI, Node.js, and Build
  Tools'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-21T23:39:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-angular-on-windows-a-guide-to-angular-cli-node-js-and-build-tools
coverImage: https://www.freecodecamp.org/news/content/images/2019/12/angular-cli-install.png
tags:
- name: Angular
  slug: angular
- name: Node.js
  slug: nodejs
- name: Windows
  slug: windows
seo_title: null
seo_desc: 'By Ahmed Bouchefra


  In this tutorial, we''ll learn how to install Angular CLI in Windows and use it
  to create an Angular project.

  What is Angular CLI?

  Angular CLI is the official tool for initializing and working with Angular projects.
  It saves you fr...'
---

By Ahmed Bouchefra

![Image](https://www.freecodecamp.org/news/content/images/2019/12/angular-cli-install-1.png)

In this tutorial, we'll learn how to install Angular CLI in Windows and use it to create an Angular project.

## What is Angular CLI?

Angular CLI is the official tool for initializing and working with Angular projects. It saves you from the hassle of complex configurations and build tools like TypeScript, Webpack, and so on.

After installing Angular CLI, you'll need to run one command to generate a project and another to serve it using a local development server to play with your application.

Like most modern frontend tools these days, Angular CLI is built on top of Node.js.

Node.js is a server technology that allows you to run JavaScript on the server and build server-side web applications. However, Angular is a front end technology, so even if you need to install Node.js on your development machine, it is only for running the CLI. 

Once you build your app for production you won't need Node.js because the final bundles are just static HTML, CSS, and JavaScript that can be served by any server or a CDN.

That being said, if you are building a full-stack [web application with Angular](https://shabang.dev/question/how-to-create-a-new-angular-9-project-using-npm/), you may need Node.js for creating the back end part if you like to use JavaScript for the front end and back end. 

Check out the MEAN stack – it's an architecture that includes MongoDB, Express (a web server and REST API framework built on top of Node.js) and Angular. You can read this [article](https://www.techiediaries.com/angular-9-8-mean-stack-authentication-tutorial-and-example-with-node-and-mongodb/) if you'd like a step by step tutorial to get started.

In this case, Node.js is used to build the back end part of your app and can be replaced with any server-side technology that you want such as PHP, Ruby, or Python. But Angular doesn't depend on Node.js except for its CLI tool and for installing packages from npm.

NPM stands for Node Package Manager. It's a registry for hosting Node packages. In recent years it's also been used to publish front end packages and libraries like Angular, React, Vue.js and even Bootstrap.

**Note**: you can download our **[Angular 8 Book: Build your first web apps with Angular 8](https://www.techiediaries.com/angular-book-build-your-first-web-apps/)** for free.

## Installing Angular CLI on Windows

First, you need to have Node and npm installed on your development machine. There are many ways to do that, such as:

* using NVM (Node Version Manager) for installing and working with multiple versions of node in your system
* using the official package manager of your operating system
* installing it from the official website.

Let's keep it simple and use the official website. Simply visit the [download page](https://nodejs.org/en/download/) and grab the binaries for Windows, then follow the setup wizard.

You can make sure Node is installed on your system by running the following command in a command prompt which should display the installed version of Node:

```bash
$ node -v

```

Next, run the following command to install Angular CLI:

```bash
$ npm install @angular/cli

```

After the command finishes successfully, you should have Angular CLI installed.

## A Quick Guide for Angular CLI

After installing Angular CLI, you can run many commands. Let’s start by checking the version of the installed CLI:

```bash
$ ng version

```

A second command that you might need to run is the `help` command for getting a complete usage help:

```bash
$ ng help

```

The CLI provides the following commands:

`add`: Adds support for an external library to your project.

`build (b)`: Compiles an Angular app into an output directory named  `dist/`  at the given output path. Must be executed from within a workspace directory.

`config`: Retrieves or sets Angular configuration values.

`doc (d)`: Opens the official Angular documentation ([angular.io](https://angular.io/)) in a browser, and searches for a given keyword.

`e2e (e)`: Builds and serves an Angular app, then runs end-to-end tests using Protractor.

`generate (g)`: Generates and/or modifies files based on a schematic.

`help`: Lists available commands and their short descriptions.

`lint (l)`: Runs linting tools on Angular app code in a given project folder.

`new (n)`: Creates a new workspace and an initial Angular app.

`run`: Runs a custom target defined in your project.

`serve (s)`: Builds and serves your app, rebuilding on file changes.

`test (t)`: Runs unit tests in a project.

`update`: Updates your application and its dependencies. See  [https://update.angular.io/](https://update.angular.io/)

`version (v)`: Outputs Angular CLI version.

`xi18n`: Extracts i18n messages from source code.

## Generating a Project

You can use Angular CLI to quickly generate your Angular project by running the following command in your command line interface:

```bash
$ ng new frontend


```

_Note:_ **frontend** _is the name of the project. You can , of course, choose any valid name for your project. Since we’ll create a full-stack application I’m using_  frontend _as a name for the front-end application._

As mentioned earlier, the CLI will ask you _Would you like to add Angular routing?_, and you can answer by entering `y` (Yes) or `n` (No), which is the default option. It will also ask you about the stylesheet format you want to use (such as CSS). Choose your options and hit  `Enter`  to continue.

![Angular 8 project structure](https://www.techiediaries.com/ezoimgfmt/i.imgur.com/vQaSm5I.png?ezimgfmt=rs:316x265/rscb1/ng:webp/ngcb1)

After that you'll have your project created with a directory structure and a bunch of configurations and code files. It'll be mostly in TypeScript and JSON formats. Let's see the role of each file:

* `/e2e/`: contains end-to-end (simulating user behavior) tests of the website
* `/node_modules/`: All 3rd party libraries are installed to this folder using  `npm install`
* `/src/`: contains the source code of the application. Most work will be done here
* `/app/`: contains modules and components
* `/assets/`: contains static assets like images, icons and styles
* `/environments/`: contains environment (production and development) specific configuration files
* `browserslist`: needed by autoprefixer for CSS support
* `favicon.ico`: the favicon
* `index.html`: the main HTML file
* `karma.conf.js`: the configuration file for Karma (a testing tool)
* `main.ts`: the main starting file from where the _AppModule_ is bootstrapped
* `polyfills.ts`: polyfills needed by Angular
* `styles.css`: the global stylesheet file for the project
* `test.ts`: this is a configuration file for Karma
* `tsconfig.*.json`: the configuration files for TypeScript
* `angular.json`: contains the configurations for CLI
* `package.json`: contains the basic information of the project (name, description and dependencies)
* `README.md`: a markdown file that contains a description of the project
* `tsconfig.json`: the configuration file for TypeScript
* `tslint.json`: the configuration file for TSlint (a static analysis tool)

## Serving your Project

Angular CLI provides a complete tool-chain for developing front-end apps on your local machine. As such, you don’t need to install a local server to serve your project — you can simply, use the  `ng serve` command from your terminal to serve your project locally. 

First navigate inside your project's folder and run the following commands:

```bash
$ cd frontend
$ ng serve


```

You can now navigate to the [http://localhost:4200/](http://localhost:4200/) address to start playing with your front end application. The page will automatically live-reload if you change any source file.

## Generating Angular Artifacts

Angular CLI provides an `ng generate` command which helps developers generate basic Angular artifacts such as modules, components, directives, pipes, and services:

```bash
$ ng generate component my-component

```

`my-component` is the name of the component. The Angular CLI will automatically add a reference to `components`, `directives` and `pipes` in the `src/app.module.ts` file.

If you want to add your component, directive or pipe to another module  (other than the main application module, `app.module.ts`), you can simply prefix the name of the component with the module name and a slash :

```bash
$ ng g component my-module/my-component

```

`my-module` is the name of an existing module.

## Conclusion

In this tutorial, we've seen how to install Angular CLI on our Windows machine and we used it to initialize a new Angular project from scratch. 

We have also seen various commands that you can use throughout the development of your project for generating Angular artifacts such as modules, components, and services.

Check out our other [Angular tutorials](https://www.techiediaries.com/angular/).

You can reach out to or follow the author via his [personal website](https://www.ahmedbouchefra.com/contact), [Twitter](https://twitter.com/ahmedbouchefra), [LinkedIn](https://www.linkedin.com/in/mr-ahmed/) and [Github](https://github.com/techiediaries).


