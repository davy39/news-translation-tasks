---
title: How to work with unpublished Node dependencies
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-25T20:58:22.000Z'
originalURL: https://freecodecamp.org/news/working-with-unpublished-node-dependencies-f396ea1a363a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0n0NX3rgHf2bzldy1uvmiQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: npm
  slug: npm
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Santhosh Reddy

  If you are a Node.js developer, you have definitely ended up in a situation where
  you want to use an unfinished feature from another Node dependency.

  Let’s elaborate on this a bit. For example, your entire project is broken logicall...'
---

By Santhosh Reddy

If you are a Node.js developer, you have definitely ended up in a situation where you want to use an unfinished feature from another Node dependency.

Let’s elaborate on this a bit. For example, your entire project is broken logically into 4 npm modules. One module, which is the main one, depends on the other 3 modules. With this setup, you might have to change the code in sub-modules and check if it works well with your main Node module.

The simplest way is to publish the modules to npm. Use the new versions in your main node module. Well, the downside with this approach is if you have made a mistake in your submodules, you have to re-publish and use them accordingly. But, things don’t stop there. You will have to repeat this until your main node module is stable. A headache. Right? I know.

So, how do we get around this problem?

#### Using npm link

With this approach, you can work with any Node dependencies if they are checked out at some location in your local machine. All you have to do is run the below command in the root folder of the package, which is a dependency for your main node module.

So what does this do? If you have worked on Node-based projects, you know there is a **node_modules** folder which has your installed dependencies. Similarly, there is a global folder for the dependencies. The above command creates a symbolic link for the package in which this command is run. You have to run this command again in the package where you want to use the dependency code with the name in `package.json`.

With this, any changes you make to your dependency Node module can be used directly without having to re-install. The above 2 steps can be made short with the below command.

```
npm link <relative-path-to-the-dependency>
```

#### Getting the source from github

Now, let’s discuss another use case where you are not the one working on your dependency, but a colleague of yours. And they don’t want to publish the code until they make sure the feature is complete to some extent.

But you need this person’s code to test any early stage integration issues. I am assuming you both use the Git version control system for managing your code. You can get the changes your colleague has pushed to git with the link to the repository code as below in your file.

package.json

```
'package-name': git@github.com:<repository-name>.git#<branch-name>
```

Once you’ve placed the above path in `package.json` file, you need to run a clean `npm install` to get the latest code from git.

Hope you enjoyed the article. If you liked it, please do clap and share with others.

Comment down below if you’ve another way of working with Node dependencies.

_Originally published at [humbleposts.com](http://humbleposts.com/working-with-unpublished-node-dependencies)._

