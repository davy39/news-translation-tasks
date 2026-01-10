---
title: Popular Front End Development Tools You Should Know
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-03T02:35:19.000Z'
originalURL: https://freecodecamp.org/news/front-end-development-tools-you-should-know
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/frontend-dev-tools.png
tags:
- name: Babel
  slug: babel
- name: CircleCI
  slug: circleci
- name: eslint
  slug: eslint
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: npm
  slug: npm
- name: webpack
  slug: webpack
seo_title: null
seo_desc: 'By Yiğit Kemal Erinç

  If you are just getting started with JavaScript, the number of tools and technologies
  you''ll hear about may be overwhelming. And you might have a hard time deciding
  which tools you actually need.

  Or maybe you''re familiar with the...'
---

By Yiğit Kemal Erinç

If you are just getting started with JavaScript, the number of tools and technologies you'll hear about may be overwhelming. And you might have a hard time deciding which tools you actually need.

Or maybe you're familiar with the tools, but you haven't given much thought to what problems they solve and how miserable your life would be without their help.

I believe it is important for Software Engineers and Developers to understand the purpose of the tools we use every day. 

That's why, in this article, I look at NPM, Babel, Webpack, ESLint, and CircleCI and I try to clarify the problems they solve and how they solve them. 

## NPM

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-1.png)

NPM is the default package manager for JavaScript development. It helps you find and install packages (programs) that you can use in your programs.

You can add npm to a project simply by using the "**npm init**" command. When you run this command it creates a "**package.json**" file in the current directory. This is the file where your dependencies are listed, and npm views it as the ID card of the project. 

You can add a dependency with the "**npm install (package_name)**" command. 

When you run this command, npm goes to the remote registry and checks if there is a package identified by this package name. If it finds it, a new dependency entry is added to your **package.json** and the package, with it's internal dependencies, is downloaded from the registry.

You can find downloaded packages or dependencies under the **"node_modules"** folder. Just keep in mind that it usually gets pretty big – so make sure to add it to **.gitignore**.

![How to keep your JavaScript libraries up to date - LogRocket Blog](https://i2.wp.com/blog.logrocket.com/wp-content/uploads/2020/06/node-modules-meme.jpeg?resize=730%2C525&ssl=1)

NPM does not only ease the process of finding and downloading packages but also makes it easier to work collaboratively on a project. 

Without NPM, it would be hard to manage external dependencies. You would need to download the correct versions of every dependency by hand when you join an existing project. And that would be a real hassle. 

With the help of npm, you can just run **"npm install"** and it will install all external dependencies for you. Then you can just run it again anytime someone on your team adds a new one.

## Babel

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-2.png)

Babel is a JavaScript compiler or transpiler which translates the ECMAScript 2015+ code into code that can be understood by older JavaScript engines.

Babel is the most popular Javascript compiler, and frameworks like Vue and React use it by default. That said, concepts we will talk about here are not only related to Babel and will apply to any JavaScript compiler.

### Why do you need a compiler?

"Why do we need a compiler, isn't JavaScript an interpreted language?" you may ask if you are familiar with the concepts of compiled and interpreted languages. 

It's true that we usually call something a "compiler" if it translates our human-readable code to an executable binary that can be understood by the CPU. But that is not the case here. 

The term transpiler may be more appropriate since it is a subset of a compiler: Transpilers are compilers that translate the code from a programming language to another language (in this example, from modern JS to an older version).

JavaScript is the language of browsers. But there is a problem with browsers: Cross compatibility. JavaScript tools and the language itself are evolving rapidly and many browsers fail to match that pace. This results in compatibility issues.

You probably want to write code in the most recent versions of JavaScript so you can use its new features. But if the browser that your code is running has not implemented some of the new features in its JavaScript engine, the code will not execute properly on that browser.

This is a complex problem because every browser implements the features at a different speed. And even if they do implement those new features, there will always be people who use an older version of their browser. 

So what if you want to be able to use the recent features but also want your users to view those pages without any problems?

Before Babel, we used polyfills to run older versions of certain code if the browser did not support the modern features. And when you use Babel, it uses polyfills behind the scenes and does not require you to do anything.

### How do transpilers/compilers work?

Babel works similar to other compilers. It has parsing, transformation, and code generation stages. 

We won't go in-depth here into how it works, since compilers are complicated things. But to understand the basics of how compilers work, you can check out the [the-super-tiny-compiler project](https://github.com/jamiebuilds/the-super-tiny-compiler). It is also mentioned in Babel's official documentation as being helpful in understanding how Babel works.

We can usually get away with knowing about Babel plugins and presets. Plugins are the snippets that Babel uses behind the scenes to compile your code to older versions of JavaScript. You can think of each modern feature as a plugin. You can go to [this](https://babeljs.io/docs/en/plugins/) link to check out the full list of plugins.

![Image](https://erinc.io/wp-content/uploads/2020/10/image.png)
_List of plugins for ES5_

Presets are collections of plugins. If you want to use Babel for a React project you can use the pre-made **@babel/preset-react** which contains the necessary plugins.

![Image](https://erinc.io/wp-content/uploads/2020/10/image-1.png)
_React Preset Plugins_

You can add plugins by editing the Babel config file.

### Do you need Babel for your React App?

For React, you need a compiler because React code generally uses JSX and JSX needs to be compiled. Also the library is built on the concept of using ES6 syntax. 

Luckily, when you create a project with **create-react-app**, it comes with Babel already configured and you usually do not need to modify the config.

### Examples of a compiler in action

Babel's website has an online compiler and it is really helpful to understand how it works. Just plug in some code and analyze the output.

![Image](https://erinc.io/wp-content/uploads/2020/10/image-4.png)

![Image](https://erinc.io/wp-content/uploads/2020/10/image-5.png)

## Webpack

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image.png)

Webpack is a static module bundler. When you create a new project, most JavaScript frameworks/libraries use it out of the box nowadays. 

If the phrase "static module bundler" sounds confusing, keep reading because I have some great examples to help you understand.

### Why do you need a bundler?

In web apps you're going to have a lot of files. This is especially the case for Single Page Applications (React, Vue, Angular), with each having their own dependencies. 

What I mean by a dependency is an import statement – if file A needs to import file B to run properly, then we say A depends on B. 

In small projects, you can handle the module dependencies with `<script>` tags. But when the project gets larger, the dependencies rapidly become hard to manage. 

Maybe, more importantly, dividing the code into multiple files makes your website load more slowly. This is because the browser needs to send more requests compared to one large file, and your website starts to consume a ton of bandwidth, because of HTTP headers.

We, as developers want our code to be modular. We divide it into multiple files because we do not want to work with one file with thousands of lines. Still, we also want our websites to be performant, to use less bandwidth, and to load fast. 

So now, we'll see how Webpack solves this issue.

### How Webpack works

When we were talking about Babel, we mentioned that JavaScript code needs to be transpiled before the deployment. 

But compiling with Babel is not the only operation you need before deploying your project. 

You usually need to uglify it, transpile it, compile the SASS or SCSS to CSS if you are using any preprocessors, compile the TypeScript if you are using it...and as you can see, this list can get long easily. 

You do not want to deal with all those commands and operations before every deployment. It would be great if there was a tool that did all that for you in the correct order and correct way. 

The good news – there is: Webpack.

Webpack also provides features like a local server with hot reload (they call it hot module replacement) to make your development experience better. 

So what's hot reloading? It means that whenever you save your code, it gets compiled and deployed to the local HTTP server running on your machine. And whenever a file changes, it sends a message to your browser so you do not even need to refresh the page. 

If you have ever used "npm run serve", "npm start" or "npm run dev", those commands also start Webpack's dev server behind the scenes.

Webpack starts from the entry point of your project (index) and generates the Abstract Syntax Tree of the file. You can think of it as parsing the code. This operation is also done in compilers, which then look for import statements recursively to generate a graph of dependencies.

It then converts the files into [IIFEs](https://developer.mozilla.org/en-US/docs/Glossary/IIFE#:~:text=An%20IIFE%20(Immediately%20Invoked%20Function,soon%20as%20it%20is%20defined.) to modularize them (remember, putting code inside a function restricts its scope). By doing this, they modularize the files and make sure the variables and functions are not accessible to other files. 

Without this operation, it would be like copying and pasting the code of the imported file and that file would have the same scope.

Webpack does many other advanced things behind the scenes, but this is enough to understand the basics.

## Bonus – ESLint

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-3.png)

Code quality is important and helps keep your projects maintainable and easily extendable. While most of us developers recognize the significance of clean coding, we sometimes tend to ignore the long term consequences under the pressure of deadlines.

Many companies decide on coding standards and encourage developers to obey those standards. But how can you make sure that your code meets the standards? 

Well, you can use a tool like ESLint to enforce rules in the code. For example, you can create a rule to enforce or disallow the usage of semicolons in your JavaScript code. If you break a rule, ESLint shows an error and the code does not even get compiled – so it is not possible to ignore that unless you disable the rule.

Linters can be used to enforce standards by writing custom rules. But you can also use the pre-made ESLint configs established by big tech companies to help devs get into the habit of writing clean code. 

You can take a look at Google's ESLint config [here](https://github.com/google/eslint-config-google) – it is the one I prefer.

ESLint helps you get used to best practices, but that's not its only benefit. ESLint also warns you about possible bugs/errors in your code so you can avoid common mistakes.

![Image](https://erinc.io/wp-content/uploads/2020/11/image-1024x717.png)

## Bonus – CI/CD (CircleCI)

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-4.png)

Continuous Integration/Development has gained a lot of popularity in recent years as many companies have adopted Agile principles. 

Tools like Jenkins and CircleCI allow you to automate the deployment and testing of your software so you can deploy more often and reliably without going through difficult and error-prone build processes by yourselves. 

I mention CircleCI as the product here because it is free and used frequently in JavaScript projects. It's also quite easy to use.

Let's go over an example: Say you have a deployment/QA server and your Git repository. You want to deploy your changes to your deployment/QA server, so here is an example process:

1. Push the changes to Git
2. Connect to the server
3. Create a Docker container and run it
4. Pull the changes to the server, download all the dependencies (npm install)
5. Run the tests to make sure nothing is broken
6. Use a tool like ESLint/Sonar to ensure code quality
7. Merge the code if everything is fine

With the help of CircleCI, you can automatically do all these operations. You can set it up and configure to do all of the above operations whenever you push a change to Git. It will reject the push if anything goes wrong, for example a failing test.

I will not get into the details of how to configure CircleCI because this article is more about the "Why?" of each tool. But if you are interested in learning more and seeing it in action, you can check out [this tutorial series](https://www.youtube.com/watch?v=CB7vnoXI0pE&ab_channel=TheCodingTrain).

## Conclusion

The world of JavaScript is evolving rapidly and new tools are gaining popularity every year. 

It's easy to react to this change by just learning how to use the tool – we are often too busy to take our time and think about the reason why that tool became popular or what problem it solves.

In this article, I picked the tools I think are most popular and shared my thoughts on their significance. I also wanted to make you think about the problems they solve rather than just the details of how to use them.

If you liked the article you can check out and subscribe to my [blog](https://erinc.io/) where I try to write frequently. Also, let me know what you think by commenting so we can brainstorm or you can tell me what other tools you love to use :)

