---
title: How to conquer Webpack 4 and build a sweet React app
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-03T05:27:03.000Z'
originalURL: https://freecodecamp.org/news/how-to-conquer-webpack-4-and-build-a-sweet-react-app-236d721e6745
coverImage: https://cdn-media-1.freecodecamp.org/images/1*VuWmde9oMOIIIHjaRj1vDA.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Adeel Imran


  This article has been outdated with the new release for babel, kindly check the
  updated article “How to combine Webpack 4 and Babel 7 to create a fantastic React
  app”, last updated October 13th, 2018


  In this article, I’ll go through ...'
---

By Adeel Imran

> This article has been outdated with the new release for babel, kindly check the updated article “[How to combine Webpack 4 and Babel 7 to create a fantastic React app](https://www.freecodecamp.org/news/how-to-combine-webpack-4-and-babel-7-to-create-a-fantastic-react-app-845797e036ff/)”, last updated October 13th, 2018

In this article, I’ll go through how to set up a React application using Webpack 4. By the end of this tutorial, you’ll know on how to hot reload your application every time you press `**ctrl + s**` in your editor of choice.

I use [Visual Studio Code](https://code.visualstudio.com/) (VS Code), and I love it. It is light weight, flexible, and the best part is it’s free. I love free. If you haven’t tried it out, give it a try.

### Our Goal

Our goal for this tutorial is to create a [React](https://reactjs.org/) app, with some cool features like async/await. I won’t be using [react-router version 4](https://reacttraining.com/react-router/web) in this tutorial, because I mainly want to focus on how to play with Webpack.

So by the end of this article, you will be good at:

* Setting up a development environment, with hot reloading using [webpack-dev-server](https://github.com/webpack/webpack-dev-server)
* Adding SCSS and HTML support in your code with webpack
* Adding support for features like try/catch, async/await and rest operator
* Creating a production build — optimized and ready for deployment
* Setting up different environments in your code like stage, demo and production

Guys I am telling you that if Webpack seems a bit hard, after this that won’t be the case anymore.

### Development Environment

#### Make the Folder

Make a folder called `tutorial` in your directory.

#### Create package.json

Open up your terminal, and go into the `tutorial` folder.

Type:

```
npm init -y
```

This will create a `**package.json**` file in your `tutorial` folder.

The file will look something like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*wZFOOk5M8Hm-Jal__d_tzA.png)
_This is what your package.json file will look like initially. I am using VS Code for the purpose of this tutorial_

#### Create the index.js file

I’ll create a folder called `**src**` in my `**tutorial**` folder.

In the `**src**` folder, I’ll create a file called `**index.js**`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Xf-2jlOilNxVpftvnh8ltg.png)
_and yeah, i’ll use star trek quotes a lot during this tutorial because IT’S AWESOME :D_

#### Bundle the code

I know this isn’t much, but bear with me. Things will get interesting pretty soon.

Now in order to bundle our code, we need to set up some configurations so that Webpack can know where to bundle the code from. For that we need to install some dependencies.

So let’s start by typing:

```
npm i --save-dev webpack webpack-cli webpack-dev-server @babel/core @babel/preset-env @babel/preset-react @babel/preset-stage-2 babel-loader@^8.0.0-beta
```

WOW! I know that was a lot of dependencies. Let’s recap why we needed these in the first place.

[webpack](http://webpack.js.org): We need Webpack to bundle our code.

[webpack-cli](https://github.com/webpack/webpack-cli): We will be using some CLI features for Webpack to make our life easier while writing some scripts.

[webpack-dev-server](https://github.com/webpack/webpack-dev-server): I will create a server using the webpack-dev-server package. This is only meant to be used in the development environment, and not for production. This means while developing and working on my code, I don’t need a separate server like Node.js.

[@babel/preset-env](https://github.com/babel/babel/tree/master/packages/babel-preset-env): This package behaves exactly the same as @babel/preset-latest (or @babel/preset-es2015, @babel/preset-es2016, and @babel/preset-es2017 together). Cool right?

[@babel/preset-react](https://github.com/babel/babel/tree/master/packages/babel-preset-react): The name of the package sounds clear — this will add support for react while we bundle our code.

[@babel/preset-stage-2](https://babeljs.io/docs/plugins/preset-stage-2/): This will add stage-2 feature of the [Ecma TC39](https://github.com/tc39) proposal. You can read more about it [here](https://babeljs.io/docs/plugins/preset-stage-2/).

[@babel/loader](https://github.com/babel/babel-loader): This is a dependency of Webpack. It allows transpiling Babel using Webpack.

[@babel/core](https://github.com/babel/babel/tree/master/packages/babel-core)**:** This is a dependency for the @babel/loader itself.

So now you know a little bit about what we installed and why.

Your `package.json` file should be looking something like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*zABxZp43O89ynHf2Goesgg.png)
_This is what your package.json file should be looking like right now._

#### Create a Babel file

We also need to add a new file called `.babelrc` **,** so let’s create it as well.

In your main folder directory, create a file `.babelrc` and the following code snippet. This will help Webpack when bundling your code and converting those Sassy codes that we will write.

#### Set up Webpack 4

Okay so the boring part has been done. Let’s move onto the main part of this tutorial: setting up Webpack 4.

To quote from Star Trek:

> He tasks me. He [_tasks_](http://www.youtube.com/watch?v=s0gk3AXEKUE) me; and I shall have him. I’ll chase him ’round the moons of Nibia and ’round the Antares maelstrom and ’round Perdition’s _flames_ before I give him up.

So let’s create a new folder called `**config**` and inside that folder let’s create a file called `**webpack.base.config.js**`.

The reason I call this file `.base` is because this contains all the common features we will use in our development and different production environments. Changes in this one file will reflect in all environments. Again if this doesn’t make sense now, guys, bear with me for a couple more minutes. It will start making sense.

Without further waiting, in your `config/webpack.base.config.js` file write these lines of code:

The `module.rules` define the set of rules that Webpack will apply to certain file extensions.

In our `rules` array, we define a `test` that tells Webpack what extension to use. Here I am telling Webpack to apply a certain rule to only `.js` based files.

Next comes `exclude`. While bundling, I don’t want Webpack to transpile everything. This will become very slow, especially when I include my node_modules folder as well.

So I will exclude it using the `exclude` property in the rule set. The last one, which is the most important one, is the `use.loader` property. Here I give it the value of `babel-loader`. What babel-loader does is use our defined presets that we defined in our `**.babelrc**` file to transpile all files with a `.js` extension.

**So far so good, yeah? We are more then halfway there…**

![Image](https://cdn-media-1.freecodecamp.org/images/1*9BpWHDblN_zsH-9ri_SpHA.gif)
_Even Professor Snape Applauds You. Awesome work guys, we are almost there._

Also one more thing: Webpack 4 sets the `**src**` folder as the default entry point and the `**dist**` folder as the default output point of your bundled result. Cool, right?

Go into your `**tutorial**` folder and run this script. This will bundle all your code and run that code in the browser:

```
Adeel@Frodo MINGW64 ~/Desktop/article/tutorial$ node_modules/.bin/webpack-dev-server --mode development --config config/webpack.base.config.js --open --hot --history-api-fallback
```

The basis for this script is that it will combine all of our code in the `**src**` directory and run it on the browser at this address:

```
http://localhost:8080/
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*hw2Qx290aHjl2nOeJob6Hw.png)
_Hmm! That’s different. This gives an error: Cannot GET /_

#### HTML

So when we ran the script it compiled and opened up the browser. Now it had the code that we wrote in our `**index.js**` file, but it didn’t have an .html file in which it could run it.

We need to add an html-webpack-plugin inside our `**webpack.base.config.js**` file, and an `**index.html**` file in our `**src**` directory.

First install the dependency for transpiling HTML with Webpack:

```
npm i --save-dev html-webpack-plugin
```

Your `**package.json**` file should look like this:

Now let’s add an HTML file in our `**src**` directory and name it `**index.html**`:

Our project directory should look like this now:

![Image](https://cdn-media-1.freecodecamp.org/images/1*BjLpopHXvTvhPr77imROIQ.png)
_Our project directory, should look something like this_

While we are at it, let’s add that `html-webpack-plugin` in our `**webpack.base.config.js**` file.

So we added something new to our webpack config file — did you notice? I am just messing with you. I know you did.

![Image](https://cdn-media-1.freecodecamp.org/images/1*lnDyP4-9zwP7oVJ0DnoLsg.gif)
_Good job guys, we’re almost done._

Now what does this plugin do? Well, it’s very simple. Plugins, put simply, add abilities to your Webpack. You can read more about them [here](https://webpack.js.org/plugins/).

Now I have added just this one plugin called [html-webpack-plugin](https://webpack.js.org/plugins/html-webpack-plugin/). The purpose of this plugin is very simple: it creates HTML files to serve your bundle file(s).

Ok so let’s run that script again (fingers crossed). “I hope no errors this time,” said every developer once.

```
Adeel@Frodo MINGW64 ~/Desktop/article/tutorial$ node_modules/.bin/webpack-dev-server --mode development --config config/webpack.base.config.js --open --hot --history-api-fallback
```

This will compile and open up your browser in the available default port. Mine is:

```
http://localhost:8080/
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*Fq9Cg3TFY-fUi1tjJkCtEA.png)
_I simply clicked **ctrl + shift + i** this opened up the inspect element in my chrome browser_

**Blue part:** The blue part is simply where I put in my meta tags and defined a title for the app.

**Yellow part:** The yellow part highlighted is the hard coded part that we wrote in our `**index.html**` file. This is where our future React app will reside.

**Red Part:** The part where I underlined in red is the most interesting part. We never wrote this in our index.html file, so where did it come from?

Webpack is very smart. It took that file in your `**index.js**` , bundled it all up nicely, and added it up all neatly in the file called `**main.js**` . Then it injected it in our `**index.html**` file. Super Cool!

#### Add React

Let’s add React and get the party going. For that, we need to install some dependencies.

Let’s start with:

```
npm i react react-dom --save
```

Now go in your `**index.js**` file and write:

Let’s run that script again:

```
Adeel@Frodo MINGW64 ~/Desktop/article/tutorial$ node_modules/.bin/webpack-dev-server --mode development --config config/webpack.base.config.js --open --hot --history-api-fallback
```

This will compile and open up your browser in the default port. Mine is:

```
http://localhost:8080/
```

Wow, did you see what opened in your browser? Yes! You did! Your first Webpack configured React app.

Now there is still loads of stuff to do. But man oh man. Good job!

![Image](https://cdn-media-1.freecodecamp.org/images/1*ghb2bSQb0lxi_zQY1L7L3A.png)
_This is our react app, running Yayyyy! :)_

Now here is the fun part. Go in your `**index.js**` file and change the title to anything of your choice. Hit `**ctrl + s**` and check your browser. It automatically updated your content.

Cool, right?

#### Let’s Recap

We have added a development environment. We added hot module reloading. We added support for **.js** files with React code. In the next part, we’ll add SCSS support in our Webpack.

#### SCSS

For SCSS support, we need to add some more dependencies in our `**package.json file**.`

Install the following packages:

```
npm i --save-dev style-loader css-loader sass-loader node-sass extract-text-webpack-plugin@^4.0.0-beta.0
```

[sass-loader](https://github.com/webpack-contrib/sass-loader): This plugin will help us compile SCSS to CSS.

[node-sass](https://github.com/sass/node-sass): The sass-loader required node-sass as a peer dependency.

[css-loader](https://github.com/webpack-contrib/css-loader): The CSS loader interprets `@import` and `url()` like `import/require()` and will resolve them.

[style-loader](https://github.com/webpack-contrib/style-loader): Adds CSS to the DOM by injecting style tag.

[extract-text-webpack-plugin](https://webpack.js.org/plugins/extract-text-webpack-plugin/): It moves all the required `**.css**` modules into a separate CSS file.

So your styles are no longer in-lined into the JavaScript bundle, but are in a separate CSS file (`**styles.css**`). If your total stylesheet volume is big, it will be faster because the CSS bundle is loaded in parallel to the JavaScript bundle.

Now that our dependencies have been installed, let’s make some changes to our Webpack config file.

Let’s understand what we did here first. In our `module.rules` we have added a new rule. What that rule does is apply some bundling to all `**.scss**` files. I hope that made sense. Inside our `use` **,** we tell it extract some information.

Let’s get a bit deeper, and I’ll try to make it as simple as I can.

```javascript
{ fallback: "style-loader", use: "css-loader!sass-loader" }
```

Try reading this piece of code from bottom-to-top.

Get all SASS code — .scss — using `sass-loader` and then convert it into CSS code using `css-loader.` Then take all that CSS code and inject it into our DOM with the <style> tag by `using style-`loader.

Now this entire object is surrounded by:

```
use: ExtractTextPlugin.extract({ ... })
```

This `ExtractTextPlugin.extract({ })` will take all of our CSS code that was suppose to be injected in our DOM and combine all of the CSS code and bundle it in a single file called `**style.css**`.

The huge benefit of this approach is that if our total style sheet volume is big while loading it up from the browser, it will load it in parallel with our JavaScript code. This will make our site download faster.

In the second part, we had to add a new entry in our `plugins` array which was:

```
new ExtractTextPlugin('style.css')
```

This basically tells the plugin to combine all our CSS code and put it in a file called `**style.css**`.

Let’s create a new file called `**styles.scss**` in our root folder and play with some styling.

Now in your `**index.js**` file add the `**styles.scss**`. Webpack allows you to import CSS in JavaScript. It’s awesome, I know.

In your code, simply add this line:

```
import './styles.scss';
```

Now run this script again, and check your browser:

```
Adeel@Frodo MINGW64 ~/Desktop/article/tutorial$ node_modules/.bin/webpack-dev-server --mode development --config config/webpack.base.config.js --open --hot --history-api-fallback
```

This is the last time we write it manually. Coming up we’ll make a script. And yeah, I remember — I still haven’t explained what this script does. I will. I promise.

Anyways, check your browser…ok cool.

![Image](https://cdn-media-1.freecodecamp.org/images/1*v8yRCnYtcJG63gvRPJXpSA.png)
_Our React app with some .scss code. We are rocking it guys,_

#### Make the Script

Let’s write some script, and make our lives a bit easier. The reason I kept on asking you to write that script again and again is so that you would actually memorize it and not just copy and paste it off the internet.

Let’s jump into our `**package.json**` file.

In your `scripts` section, add the following code:

Now in your terminal, type:

```
Adeel@Frodo MINGW64 ~/Desktop/article/tutorial$ npm run start:dev
```

**Note**: in the script we no longer have to write this:

```
node_modules/.bin/webpack
```

More details about in the webpack-dev-server usage docs [**here**](https://github.com/webpack/webpack-dev-server#usage)**.**

The script for `start:dev` looks something like this now:

```
webpack-dev-server --mode development --config config/webpack.base.config.js --open --hot --history-api-fallback
```

Let’s break down what this script does:

`webpack-dev-server --mode development`

The flag `--mode development` sets the build that’s the most optimized for development purposes. It has fast incremental compilation for the development cycle and useful error messages at runtime.

You can read more about modes in this amazing article: [Webpack 4: Mode and Optimization](https://medium.com/webpack/webpack-4-mode-and-optimization-5423a6bc597a).

The flag `--config config/webpack.base.config.js` tells Webpack where all our configuration is placed for our Webpack bundling.

The flag `--open` tells the `webpack-dev-server` to open up the browser.

The flag `--hot` tells the `webpack-dev-server` to enable Webpack’s hot module replacement feature. This updates the browser every time you hit `**ctrl + s**`

The flag `— -history-api-fallback` tells `webpack-dev-server` to fallback to `**index.html**` in the event that a requested resource cannot be found. You can read more about [history-api-fallback](https://github.com/webpack/webpack-dev-server/tree/master/examples/cli/history-api-fallback) here.

### Production Environment

Now that we are done with our development environment, let’s get our hands dirty and get our code ready for production.

Let’s create a new file `**webpack.opt.config.js**`. This file will contain all our production optimizations that we will need.

The plan is to do something like merge our `**webpack.base.config.js**` file with the `**webpack.opt.config.js**` file to create a production configuration for our single page application.

So let’s begin. In your `**config**` directory create a new file called `**webpack.opt.config.js**`. `opt` is short for optimization. If someone can came up with a cooler name, let me know.

We need to install some dependencies to help with our optimizations:

```
$ npm i --save-dev optimize-css-assets-webpack-plugin uglifyjs-webpack-plugin
```

Although the `--mode production` comes up with some pretty cool optimizations itself. You can read more about it [here](https://webpack.js.org/concepts/mode/#mode-production). But I’d still like to add a couple more.

The code is as follows:

Let’s recap what we did here. I added to new modules in dev-dependency.

[uglifyjs-webpack-plugin](https://github.com/webpack-contrib/uglifyjs-webpack-plugin): As the name sounds, this will uglify and minimize all our code to reduce the bundle size.

[optimize-css-assets-webpack-plugin](https://github.com/NMFR/optimize-css-assets-webpack-plugin): This plugin will minimize and optimize your CSS code.

**So far so good everybody — we are almost done.**

![Image](https://cdn-media-1.freecodecamp.org/images/1*H7nnE1npF6MtGTxGBxUPEg.gif)
_Just a little bit more, and you have reached the finish line._

Remember when I talked about a way where we wouldn’t have to repeat our code again and again? One for development, the other for production…and don’t even get me started on managing those environments stage, demo and live! Well that ends today. No more code repetitions.

I introduce to you our savior, the white knight [Webpack Merge](https://github.com/survivejs/webpack-merge). This plugin is amazing, as the name sounds.

What this will do is combine our configuration for `**.base**` and `**.opt**` files in a smart way. It provides a `merge` function that concatenates arrays and merges objects to create a new object.

So without further ado, let’s install this amazing plugin as well:

```
$ npm i --save-dev webpack-merge
```

Let’s create our final `**webpack.prod.config.js**` file:

We pass a parameter to our function called `productionConfiguration` and used `env` . This is how we pass information in Webpack through our CLI (I’ll explain how we do that in a minute).

I am passing something called `NODE_ENV` . It’s the value in which I will tell my webpack that what environment I will be running — such as demo, test, live or whatever.

Next, whatever I get in my `env.NODE_ENV` I set in my `process.env.NODE_ENV` using the Webpack builtin plugin called `DefinePlugin` . We just need to make sure that whatever value we pass is always stringified.

Then, in the last line, we do this:

```
module.exports = merge.smart(baseConfig, optimizationConfig, productionConfiguration);
```

What is happening here is we use `webpack-merge's` method called `smart` to smartly merge all three of our configurations. That way we don’t repeat the same code everywhere. This is coolest feature.

I remember a time before I found this plugin. It was a lot of mess doing the same thing in all of my Webpack configuration files. Now it’s just a breeze.

Anyways, moving forward, since now our Webpack configurations are finally done. Let’s make our production ready build script in our `**package.json**` file.

In your scripts section, add the following lines:

I’ll start with the `prestart:prod` command:

```
"prestart:prod": "webpack --mode production --config config/webpack.prod.config.js --env.NODE_ENV=production --progress",
```

We’ll break this command down.

`webpack --mode production` . As we discussed earlier, when discussing `development mode` , production mode will run some really cool optimization processes on our bundled file(s) to make the size smaller.

Next flag is `--config config/webpack.prod.config.js`. This tells Webpack where our production configuration lies in the directory.

The `env` flag specifies the environment variable that we pass through our `**webpack-cli**`. It goes like this: `--env.NOVE_ENV=production` passes an object in our `**webpack.prod.config.js**` with the key `NODE_ENV` which has the value called `production` .

You can pass as many environment variables as you want, like `--env.X=foo --env.Y=bar` . Then in your configuration you would get these values the same way you accesses `NODE_ENV` value.

The last flag is `--progess` . It simply tells the progress/status of the bundle, like what percentage the bundle has completed while making the bundled files in your `**dist**` folder.

#### A quick reminder

Webpack 4 by default sets the `**src**` folder as the default entry point and the `**dist**` folder as the default output point of your bundled result. Cool, right? I know I am repeating this — I told you earlier — but that’s why I said reminder.

#### Back to our Tutorial

We discussed `prestart:prod` script, now we will talk about the final script called `start:prod`.

With npm, any time you want to run scripts one after the other, you sequence them with `preCOMMAND` `COMMAND` `postCOMMAND.`

Like we did here:

```
$ prestart:prod
```

```
$ start:prod
```

So we will always run the script `npm run start:prod` before executing the script called `npm run prestart:prod.`

Let’s discuss `start:prod.`

```
$ node server => {This is equivalent to} =&gt; $ node server/index.js
```

Let’s create a folder called `**server**`. Inside the folder, create a file called `**index.js**`. But before we do that, we need to add one last dependency.

This is going to be Express, our back-end Node.js framework:

```
npm i --save express
```

Let’s discuss this code before we proceed further.

We instantiate our app with `express()` and then set up a static public folder called `**dist**`**.** This is the same folder created by Webpack when we run our production command.

We include our `**routes**` file — we will create that in a second — and set the `**routes**` file to the `/` directory.

Next we set up a port. If none is provided to set via the node CLI, we use port `3000`. After that, we create an HTTP server and listen on that server via the port. At the very last, we console to our terminal that we are running the server on that certain port.

Let’s create our last file called `**routes/index.js**:`

Here we check that whatever the user comes on, the path redirects the user to the `**dist/index.html**` where our React application lives.

And that’s it. We are done.

Now go in your terminal and type:

```
npm run start:prod
```

This will take a moment. It will show you the progress while it transpiles. After that, it consoles a message that it is `listening to port 3000` if none is provided.

Now go to your browser `http:localhost:3000/` and your application is alive.

![Image](https://cdn-media-1.freecodecamp.org/images/1*zzUTJ889aALPnm_KVmbmeA.gif)
_Congrats!_

See the code on [GitHub](https://github.com/adeelibr/react-starter).

A shout out to my good friend [Ahmed Abbasi](https://twitter.com/ehmadabbasi) for helping me proof read this article.

You can follow me on [Twitter](http://twitter.com/adeelibr), I would love to talk and hear you guys out.

