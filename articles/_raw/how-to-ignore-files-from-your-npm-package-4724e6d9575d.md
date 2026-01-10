---
title: How to ignore files from your npm package
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2019-04-22T16:02:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-ignore-files-from-your-npm-package-4724e6d9575d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*F6R34rqTupBQxrVe7GS4fw.jpeg
tags:
- name: npm
  slug: npm
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'You can decide what files people get when they download your npm package
  in three ways:


  With the .gitignore file

  With the .npmignore file

  With the files property


  We’ll look at each method and discuss which methods you should (or shouldn’t) be
  using...'
---

You can decide what files people get when they download your npm package in three ways:

1. With the `.gitignore` file
2. With the `.npmignore` file
3. With the `files` property

We’ll look at each method and discuss which methods you should (or shouldn’t) be using.

### Excluding files with gitignore

First, npm will check your repository for a `.gitignore` file. If there is a `.gitignore` file, npm will ignore files according to what’s listed in the `.gitignore` file.

This is the most common way package authors prevent people from downloading extra files.

Let’s go through a simple example. Say you have the following directory structure.

```
- project-name/   |- index.js   |- package.json   |- node_modules/
```

Let’s say you don’t want people to download the `node_modules` folder. You also don’t want to save the `node_modules` in the Git repository.

What you’ll do is create a `.gitignore` file.

```
# .gitignore node_modules
```

In this case, both Git and npm ignore the `node_modules` folder.

### Blacklisting files with npmignore

A second way is to blacklist files with a `.npmignore` file. The `.npmignore` file works the same way as a `.gitignore` file. If a file is listed in the `.npmignore` file, the file will be excluded from the package.

**Important note:** If you have a `.npmignore` file, npm will use the `.npmignore` file. **npm will ignore the `.gitignore` file** altogether. (Many developers mistakenly believe npm will use both `.npmignore` and `.gitignore` files. Don’t make the same mistake!)

You can use this method if you want to exclude files from the package but still keep them in the Git repository.

Let’s walk through another example. Let’s say you’ve written tests for your package and you put them all in a `tests` folder. This is your directory structure:

```
- project-name/  |- index.js |- package.json |- node_modules/ |- tests/
```

You want to exclude `node_modules` from both your Git repository and your package.

You want to include `tests` in your Git repository, but exclude it from the package.

If you opt for the `npmignore` file method, you can write these in your `.gitignore` and `.npmignore` files:

```
# .gitignore node_modules
```

```
# .npmignore node_modules tests
```

### Whitelisting files with the files property

A third method is to **whitelist** files you want to be **included** in the `package.json` file, under the `files` property.

Note: npm will prioritize this method over other methods mentioned above. This is the easiest method to limit what files others download.

This approach is pretty simple. What you need is to create a `files` property in the `package.json` file. Then, provide a list of files you’d like to include.

Here’s an example:

```
{   "files": [      "index.js"   ] }
```

Note: Some files, like `package.json`, are [always included](https://docs.npmjs.com/files/package.json) in a package. You don’t have to write these files in the `files` property.

### Which method to use?

All three methods work. Pick the one you’re most comfortable with. For simple projects, the `.gitignore` file method should suffice.

If your project is more advanced, you might want to blacklist files with `.npmignore` or whitelist files with the `files` property. Pick one. There’s no need for both.

### A quick tip

You can use `npm pack` to generate a package. This package includes files other people will get.

```
npm pack
```

Try it!

Thanks for reading. Did this article help you out? If it did, I hope you consider [sharing it](https://twitter.com/share?text=How%20to%20ignore%20files%20from%20your%20npm%20package%20by%20@zellwk%20?%20&url=https://zellwk.com/blog/ignoring-files-from-npm-package/). You might help someone else out. Thanks so much!

This article was originally posted on [_my blog_](https://zellwk.com/blog/ignoring-files-from-npm-package/)_._  
Sign up for my [newsletter](https://zellwk.com/) if you want more articles to help you become a better front-end developer.

