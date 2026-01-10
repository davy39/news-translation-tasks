---
title: How to Add ESLint to an Angular Application
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-11-15T16:39:58.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-eslint-to-an-angular-application
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/angular-eslint-cover-hashnode.png
tags:
- name: Angular
  slug: angular
- name: eslint
  slug: eslint
- name: JavaScript
  slug: javascript
- name: TypeScript
  slug: typescript
seo_title: null
seo_desc: 'By Rodrigo Kamada

  In this article, we''ll build a web application using the latest version of Angular.
  Then we''ll add ESLint which analyzes the JavaScript code statically to find any
  problems.

  Prerequisites

  Before you start, you need to install and co...'
---

By Rodrigo Kamada

In this article, we'll build a web application using the latest version of [Angular](https://angular.io/). Then we'll add [ESLint](https://eslint.org/) which analyzes the JavaScript code statically to find any problems.

## Prerequisites

Before you start, you need to install and configure the tools below (if you don't already have them installed) to create the Angular application:

* [Git](https://git-scm.com/): Git is a distributed version control system. We'll use it to sync the repository.
* [Node.js and npm](https://nodejs.org/): Node.js is a JavaScript code runtime software based on Google's V8 engine. npm is a package manager for Node.js (Node Package Manager). We'll use them to build and run the Angular application and install the libraries.
* [Angular CLI](https://angular.io/cli): Angular CLI is a command line utility tool for Angular. We'll use it to create the base structure of the Angular application.
* IDE (for example [Visual Studio Code](https://code.visualstudio.com/) or [WebStorm](https://www.jetbrains.com/webstorm/)): an Integrated Development Environment is a tool with a graphical interface to help in the development of applications. We'll use it to develop the Angular application.

## Getting Started

### Create the Angular application

Angular is a development platform for building web, mobile and desktop applications using HTML, CSS, and TypeScript (JavaScript). Currently, Angular is at version 14 and Google is the main maintainer of the project.

First, let's create the application with the Angular base structure using the `@angular/cli` with the route file and the SCSS style format.

```
ng new angular-eslint --routing true --style scss
CREATE angular-eslint/README.md (1067 bytes)
CREATE angular-eslint/.editorconfig (274 bytes)
CREATE angular-eslint/.gitignore (548 bytes)
CREATE angular-eslint/angular.json (3136 bytes)
CREATE angular-eslint/package.json (1045 bytes)
CREATE angular-eslint/tsconfig.json (863 bytes)
CREATE angular-eslint/.browserslistrc (600 bytes)
CREATE angular-eslint/karma.conf.js (1431 bytes)
CREATE angular-eslint/tsconfig.app.json (287 bytes)
CREATE angular-eslint/tsconfig.spec.json (333 bytes)
CREATE angular-eslint/.vscode/extensions.json (130 bytes)
CREATE angular-eslint/.vscode/launch.json (474 bytes)
CREATE angular-eslint/.vscode/tasks.json (938 bytes)
CREATE angular-eslint/src/favicon.ico (948 bytes)
CREATE angular-eslint/src/index.html (299 bytes)
CREATE angular-eslint/src/main.ts (372 bytes)
CREATE angular-eslint/src/polyfills.ts (2338 bytes)
CREATE angular-eslint/src/styles.scss (80 bytes)
CREATE angular-eslint/src/test.ts (749 bytes)
CREATE angular-eslint/src/assets/.gitkeep (0 bytes)
CREATE angular-eslint/src/environments/environment.prod.ts (51 bytes)
CREATE angular-eslint/src/environments/environment.ts (658 bytes)
CREATE angular-eslint/src/app/app-routing.module.ts (245 bytes)
CREATE angular-eslint/src/app/app.module.ts (393 bytes)
CREATE angular-eslint/src/app/app.component.scss (0 bytes)
CREATE angular-eslint/src/app/app.component.html (23364 bytes)
CREATE angular-eslint/src/app/app.component.spec.ts (1097 bytes)
CREATE angular-eslint/src/app/app.component.ts (219 bytes)
✔ Packages installed successfully.
    Successfully initialized git.
```

Now we will install the libraries and add the ESLint settings.

```
ng add @angular-eslint/schematics
ℹ Using package manager: npm
✔ Found compatible package version: @angular-eslint/schematics@14.2.5.
✔ Package information loaded.

The package @angular-eslint/schematics@14.2.5 will be installed and executed.
Would you like to proceed? Yes
✔ Packages successfully installed.

    All @angular-eslint dependencies have been successfully installed 🎉

    Please see https://github.com/angular-eslint/angular-eslint for how to add ESLint configuration to your project.

    We detected that you have a single project in your workspace and no existing linter wired up, so we are configuring ESLint for you automatically.

    Please see https://github.com/angular-eslint/angular-eslint for more information.

CREATE .eslintrc.json (984 bytes)
UPDATE package.json (1511 bytes)
UPDATE angular.json (3447 bytes)
✔ Packages installed successfully.
```

Next, we will run the command below to validate the ESLint installation and configuration:

```
npm run lint

> angular-eslint@1.0.0 lint /home/rodrigokamada/angular-eslint
> ng lint


Linting "angular-eslint"...

All files pass linting.
```

And you're all set! The message "_All files pass linting_" shows that no problems were found.

The application repository is [available here](https://github.com/rodrigokamada/angular-eslint.).

## Conclusion

This is what we covered in this article:

* We created an Angular application.
* We added ESLint to analyze and find problems with the code.

You can use this to check your application code before deploying to your environment.

Thank you for reading and I hope you enjoyed the article!

This tutorial was posted on my [blog](https://rodrigo.kamada.com.br/blog/adicionando-o-eslint-em-uma-aplicacao-angular) in Portuguese.

To stay updated whenever I post new articles, follow me on [Twitter](https://twitter.com/rodrigokamada) and [LinkedIn](https://www.linkedin.com/in/rodrigokamada).






