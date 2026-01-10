---
title: How to Force Use Yarn or NPM
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-17T07:03:09.000Z'
originalURL: https://freecodecamp.org/news/how-to-force-use-yarn-or-npm
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/how-to-force-use-yarn-or-npm-facebook.jpg
tags:
- name: npm
  slug: npm
- name: Yarn
  slug: yarn
seo_title: null
seo_desc: "By Carol-Theodor Pelu\nIn this short post, I’m going to show you how to\
  \ prevent the usage of npm or yarn, depending on your needs. \nThis comes in handy\
  \ when your team or organization has a preference for a specific package manager.\
  \ \nWith this method, ..."
---

By Carol-Theodor Pelu

In this short post, I’m going to show you how to prevent the usage of _npm_ or _yarn,_ depending on your needs. 

This comes in handy when your team or organization has a preference for a specific package manager. 

With this method, you make sure everyone will be using the same package manager.

Let’s get started!

Want to watch a video about how to do this? Check this one out:

%[https://www.youtube.com/watch?v=RmpVlaocd0M]

## Edit .npmrc

You might not have this file in your codebase. If this is the case, create this file in the root folder of your application.

It allows us to specify package manager configurations and it is used by both _npm_ and _yarn_.

Your `.npmrc` file should have the `engine-strict` property marked as `true`.

```config
//.npmrc file

engine-strict = true
```

This option tells the package manager to use the version of the engines we have specified in the `package.json` file.

## Edit package.json

Inside your `package.json` file you should add the `engines` section if you don’t currently have it.

```json

//package.json
{ 
  ...
  "engines": {
    "npm": "please-use-yarn",
    "yarn": ">= 1.19.1"
  },
  ...
}
```

In the above code, the `package.json` file uses a version of `yarn` 1.19.1 or greater.  
But for `npm` we specify a version that doesn’t exist.

This way we make sure that when someone tries to use `npm` instead of `yarn`, they will receive an error that outputs ‘`please-use-yarn`‘.

## Running npm install

Once you’ve done the above changes, try to run `npm install`.

You will receive an error that prevents you from using `npm`.

```bash

npm ERR! code ENOTSUP
npm ERR! notsup Unsupported engine for my-app@0.1.0: wanted: {"npm":"please-use-yarn","yarn":">= 1.19.1"} (current:
 {"node":"12.16.3","npm":"6.14.4"})
npm ERR! notsup Not compatible with your version of node/npm: my-app@0.1.0
npm ERR! notsup Not compatible with your version of node/npm: my-app@0.1.0
npm ERR! notsup Required: {"npm":"please-use-yarn","yarn":">= 1.19.1"}
npm ERR! notsup Actual:   {"npm":"6.14.4","node":"12.16.3"}

npm ERR! A complete log of this run can be found in:
npm ERR!     C:\Users\YourUser\AppData\Roaming\npm-cache\_logs\2020-05-21T10_21_04_676Z-debug.log

```

This, of course, can be done the other way around if you want to prevent the usage of `yarn`.

## Conclusion

It is pretty straightforward and easy to ensure that only one package manager must be used inside your project.  
  
This will reduce the chance of errors caused by developers that are using different package managers and it is a good practice to standardize the project’s coding rules and management.

You can reach out and ask me anything on [Twitter](https://twitter.com/pelu_carol), [Facebook](https://www.facebook.com/neutrondevcom) and my [website](https://neutrondev.com/).

