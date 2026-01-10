---
title: npm Uninstall – How to Remove a Package
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-03-01T20:46:50.000Z'
originalURL: https://freecodecamp.org/news/npm-uninstall-how-to-remove-a-package
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/shut-down-g5ad24366d_1280.jpg
tags:
- name: Node.js
  slug: nodejs
- name: npm
  slug: npm
seo_title: null
seo_desc: 'The Node Package Manager (NPM) provides various commands that let you work
  with packages.

  And just as you can install a package from the npm library, you can uninstall it.

  To uninstall a package, you can use the command provided by npm for the purpos...'
---

The Node Package Manager (NPM) provides various commands that let you work with packages.

And just as you can install a package from the npm library, you can uninstall it.

To uninstall a package, you can use the command provided by npm for the purpose – `npm uninstall`.

The way you uninstall a regular package or dependency is not the way you should uninstall a global package and a dev dependency, though.

In this article, I will show you how to uninstall a regular package, a global package, and a dev dependency.

## How to Remove a Package with npm Uninstall

To remove a package with the `npm uninstall` command, you can use the syntax `npm uninstall package-name` in the directory where the package is located.

The package I will be using to demonstrate how a package is uninstalled is Express – a NodeJS framework.

In the screenshot below, you can see that Express is listed as a dependency in the `package.json` file. 
![ss-1](https://www.freecodecamp.org/news/content/images/2022/03/ss-1.png)

But after I run `npm uninstall express`, you won’t see Express listed as a dependency again:

![ss-2](https://www.freecodecamp.org/news/content/images/2022/03/ss-2.png)

You can see there’s no Express anymore. There’s even no dependency key anymore because there is no dependency.

## How to Remove a Dev Dependency with npm Uninstall

A dev dependency is a package used during development only.

To remove a dev dependency, you need to attach the `-D` or `--save-dev` flag to the npm uninstall, and then specify the name of the package.

The basic syntax for doing this is `npm uninstall -D package-name` or `npm uninstall --save-dev package-name`

You must run the command in the directory (folder) where the dependency is located.

I will be using Nodemon to demonstrate how to remove a dev dependency. 

Nodemon lets your NodeJS app reload automatically any time it detects a change in a file or folder during development.

In the screenshot below, you can see that Nodemon is listed as a dev dependency.
![ss-3](https://www.freecodecamp.org/news/content/images/2022/03/ss-3.png)

To remove it, I will run `npm uninstall –D nodemon`
![ss-4](https://www.freecodecamp.org/news/content/images/2022/03/ss-4.png)

You can see there’s no Nodemon anymore in the `package.json` file. 


## How to Remove a Global Package with npm Uninstall

A global package is a package that is installed globally on your machine, so you don't have to reinstall it every you need it.

To remove a global package, you need to attach the `-g` flag to npm uninstall, and then specify the name of the package.

The basic syntax for doing this is `npm uninstall -g package-name`.

To show you how to remove a global package, I will be using a package called CORS (Cross-origin Resource Sharing). 

CORS blocks the Same Origin Policy (SOP) of browsers so you can make requests from one browser to another.

In the screenshot below, you can see that CORS is not listed as a package in the `package.json` file:
![ss-5](https://www.freecodecamp.org/news/content/images/2022/03/ss-5.png)

CORS is not listed because it is installed globally on my machine, not in the directory of a project. 

If you install a package globally and you want to see it, run `npm list -g`
![ss-6](https://www.freecodecamp.org/news/content/images/2022/03/ss-6.png)

You can see that CORS is listed as a global package now.

To uninstall CORS globally, I will now run `npm uninstall -g cors`.

After running the command, you can see there’s no CORS anymore when I run `npm list –g`:

![ss-7](https://www.freecodecamp.org/news/content/images/2022/03/ss-7.png)

## Conclusion

In this article, you learned the various ways you can uninstall different kinds of NPM packages, so you can have more control over your codebase and remove unnecessary packages.

Thank you for reading.

If you find this article helpful, kindly share it so others can see it.


