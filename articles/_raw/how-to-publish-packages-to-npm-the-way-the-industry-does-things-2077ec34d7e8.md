---
title: How to publish packages to npm (the way the industry does things)
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2019-04-09T15:17:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-publish-packages-to-npm-the-way-the-industry-does-things-2077ec34d7e8
coverImage: https://cdn-media-1.freecodecamp.org/images/0*Nhf9jeZDYfGdX6N6.png
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: npm
  slug: npm
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'It’s simple to publish a package onto npm. There are two steps:


  Create your package.

  Publish the package.


  But publishing packages the way the industry does it? Not so simple. There are more
  steps. We’ll go through what steps are required, and I’ll ...'
---

It’s simple to publish a package onto npm. There are two steps:

1. Create your package.
2. Publish the package.

But publishing packages the way the industry does it? Not so simple. There are more steps. We’ll go through what steps are required, and I’ll show you an easy way to publish and update your package.

### Creating your first package

This section is for you if you haven’t published a package to npm before. Feel free to skip to the next section if you published one before.

To publish your first package to npm, you need to go through these steps:

**First, you need to have an npm account**. Create one [here](https://www.npmjs.com/signup) if you don’t have one yet.

**Second, you need to login to your npm account through the command line**. (You need to have Node and npm installed on your system before you perform this step. Install them [here](https://nodejs.org/en/)).

To sign in, you use `npm login`.

```
npm login
```

You’ll be prompted to enter your username, password, and email address.

![Image](https://cdn-media-1.freecodecamp.org/images/JHhisobcBkv-CepU3oB0sjvuGJ3lpkQbqixh)

**Third, you need to create a package**. To do so, create a folder somewhere on your computer and navigate to it. The command line version is:

```
# Creating a folder named how-to-publish-to-npm mkdir how-to-publish-to-npm # Navigating into the folder cd how-to-publish-to-npm
```

Next, you want to begin the project with the `npm init` command.

```
npm init
```

This command runs you through a few questions and creates a `package.json` file for you at the end. This `package.json` file contains the bare necessities you need to publish your project. (Feel free to skip questions that don’t make sense).

![Image](https://cdn-media-1.freecodecamp.org/images/zkzI4ZMLfqEMMIfD2aFF6zfpxKpT54w5gU1Z)

**The final step is to publish your package** with the `npm publish` command.

```
npm publish
```

If the package already exists on npm (because your package has the same name as another package on npm), you won’t be able to publish it. You’ll get an error.

![Image](https://cdn-media-1.freecodecamp.org/images/q8cTyrCM2nFMivMgtaW2Gi9Jcno1zquqViBU)

You’ll need to change your package name.

To change your package name, you change the `name` property in the `package.json` file. Here, I changed it to `publishing-to-npm`.

(You can check for naming collisions by doing a search on npm, or through the `npm search` command).

![Image](https://cdn-media-1.freecodecamp.org/images/Gp-SPyfzY0nyDVKNJXa3GpFEahjKVuAfV8PD)

It’s also a good idea to update the folder name as well for consistency. Here’s the command line equivalent.

```
# Command to change folder names by moving everything mv how-to-publish-to-npm publishing-to-npm
```

Try the `publish` command again. You should get a success message now.

![Image](https://cdn-media-1.freecodecamp.org/images/ASGCDDVtEEjdKoPqzdvA2Ux32pgXsdcE98xE)

### What to do if every name you came up with is taken already

This is a common problem since many people create packages on npm. It’s difficult to get the package name you desire sometimes. (It’s like how I can _never_ find a good `.com` domain).

To combat this problem, npm lets you publish to a scope. This means you can publish the package under your own username (or npm organization), so you’re free from naming problems.

To publish to a scope, you can either:

1. Change the `name` to `@username/package-name` manually in `package.json`
2. Run `npm init --scope=username` instead of `npm init`

If your repository has a scope, you need to adjust the publish command slightly:

```
npm publish --access public
```

That’s all you need to do to publish a package to npm.

Now, let’s move on to how the industry publishes packages.

Consider a popular framework like React. If you dig around React, you’ll notice a few things:

First, React has a [Github repository](https://github.com/facebook/react).

Second, React is [published on](https://www.npmjs.com/package/react) npm.

Third, React follows [Semantic versioning](https://zellwk.com/blog/semantic-versioning/) (Semver for short).

![Image](https://cdn-media-1.freecodecamp.org/images/uwwUruPCdcFdhAmArNB-nBtUYcL7yb3x2J6R)

Fourth, each update to React has a git tag associated with it. This git tag follows Semver as well.

![Image](https://cdn-media-1.freecodecamp.org/images/wZuV9GG8e9pkllgcdjrVIGmjK84bDs-atDeU)

Fifth, there are [release notes](https://github.com/facebook/react/releases) for every React update.

This means publishing a package involves many steps. At the very least, you need to:

1. Run tests (if there are any)
2. Update `version` in `package.json` according to Semver
3. Create a git tag according to Semver
4. Push the package to Github
5. Push the package to npm
6. Create release notes for every update

It’s common to forget one of these things when we’re ready to push. Sometimes we `npm publish` and we enjoy a break. When we’re back, we screw ourselves for forgetting.

There’s an easier way. It’s with a tool called `np`.

### np

[np](https://github.com/sindresorhus/np) (created by [Sindre Sorhus](https://github.com/sindresorhus)) makes it easier for us to publish packages without missing any of the steps I detailed above.

### Installing np

To install `np`, you can run the following command:

```
npm install np
```

This works. But I prefer installing `np` globally on my computer so I can run the `np` command anywhere.

```
sudo npm install --global np
```

### Before using np

Before you use `np` you need to make sure:

1. Your project is a Git repository
2. It needs to have a remote
3. You must have pushed to the remote at least once.
4. You also need to make sure your working directory is clean.

```
# Initialize Git git init # Adds a remote repository git remote add origin some-url # Commit changes git add . git commit -m "Initial Commit"
```

If your project is not a Git repository, you’ll get this error:

![Image](https://cdn-media-1.freecodecamp.org/images/7NrM2CyehgdU8hCtwioMAAIjFY1XD8yKfYYz)

If your project doesn’t have remote, you’ll get this error (at a later part of the checks).

![Image](https://cdn-media-1.freecodecamp.org/images/3Pb4qxEzdXr-Uu8xk6o84aTg1CbhPKff1aBT)

If your working directory is dirty, you’ll get this error:

![Image](https://cdn-media-1.freecodecamp.org/images/OS9Wo5PaEyUDlmWh7ZWtig0Joik0GwRgnh6s)

If you haven’t pushed to the Git remote at least once, `np` will just hang and do nothing.

### Using npm

To use `np`, you run the `np` command.

```
np
```

`np` will prompt you to enter a Semver number.

![Image](https://cdn-media-1.freecodecamp.org/images/RD-MA-FOfYfODX9M8CemmsQRfNfGzoJfykQt)

Choose a number and `np` will ask you to confirm your choice.

![Image](https://cdn-media-1.freecodecamp.org/images/Kli5Ll2K9rNaLOQ1OokDMpEGoEoqxJ-kzDSZ)

`np` then does the rest of the publishing stuff for you.

### Error with running tests

`np` runs the `npm test` command as part of its checks.

If you followed the tutorial up to this point, you would get an error that looks like this:

![Image](https://cdn-media-1.freecodecamp.org/images/sORwnhnEitrpcWBx9JBa5zfkwk3jdx3eIhQE)

This happens because our `npm test` command results in an error. You can try it yourself:

```
npm test
```

![Image](https://cdn-media-1.freecodecamp.org/images/QQ28caWQvveRLIwk3jwcUkBhbLFDUMSy3Qe1)

To fix this error, we need to change the `test` script in `package.json` file.

Right now it looks like this:

```
"scripts": {     "test": "echo \"Error: no test specified\" && exit 1"},
```

Change it to this:

```
"scripts": {     "test": "echo \"No test specified\""},
```

This change works because `exit 1` creates an error.

With this change, `np` should complete the publishing process. (Remember to commit the change before running `np`).

![Image](https://cdn-media-1.freecodecamp.org/images/NFPTeC5esUzD1vLJczEy-meWcFJb1qPCEi8o)

At the end of the process, `np` launches a browser window for you to write your release notes.

![Image](https://cdn-media-1.freecodecamp.org/images/Erm2uLF-N8B4b6jCa5C0AkgwqMfD5sbqZIjf)

In short, `np` makes publishing packages much simpler!

Thanks for reading. Did this article help you out? If it did, I hope you consider [sharing it](https://twitter.com/share?text=How%20to%20publish%20packages%20to%20npm%20(the%20way%20the%20industry%20does%20things)%20by%20@zellwk%20?%20&url=https://zellwk.com/blog/publish-to-npm/). You might help someone else out. Thanks so much!

This article was originally posted at [_my blog_](https://zellwk.com/blog/publish-to-npm).  
Sign up for my [newsletter](https://zellwk.com/) if you want more articles to help you become a better frontend developer.

