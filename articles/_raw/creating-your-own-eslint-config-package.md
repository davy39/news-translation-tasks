---
title: How to Create Your Own ESLint Config Package
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-17T13:00:00.000Z'
originalURL: https://freecodecamp.org/news/creating-your-own-eslint-config-package
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/susan-holt-simpson-2nSdQEd-Exc-unsplash.jpg
tags:
- name: eslint
  slug: eslint
- name: JavaScript
  slug: javascript
- name: npm
  slug: npm
seo_title: null
seo_desc: "By Leonardo Faria\nESLint is a powerful tool that helps you enforce consistent\
  \ coding conventions and ensure quality in your JavaScript codebase. \nCoding conventions\
  \ are sometimes difficult to decide on, and having a tool that automates their enforcem..."
---

By Leonardo Faria

ESLint is a powerful tool that helps you enforce consistent coding conventions and ensure quality in your JavaScript codebase. 

Coding conventions are sometimes difficult to decide on, and having a tool that automates their enforcement helps avoid unnecessary discussions. Ensuring quality is also a welcome feature: linters are excellent tools for catching bugs, such as those related to variable scope.

ESLint is designed to be completely configurable, giving you the option of enabling/disabling each rule, or mixing the rules to match your needs.  

With this in mind, the JavaScript community and companies who use JavaScript can extend the original ESLint config. There are [several examples](https://www.npmjs.com/search?q=eslint-config) in the npm registry: [eslint-config-airbnb](https://www.npmjs.com/package/eslint-config-airbnb) is one of the most well-known.

In your daily routine, you will probably combine more than one config, since there is no one-config-fits-all. This post will show how to create your own repository of configurations, giving you the option to centralize all your rule definitions.

## Create the project

First you'll need to create a new folder and npm project. [By convention](https://eslint.org/docs/developer-guide/shareable-configs), the module name begins with `eslint-config-`, such as `eslint-config-test`.

```bash
mkdir eslint-config-test
cd eslint-config-test
npm init

```

You will have a package.json file that will look like the following snippet:

```json
{
  "name": "eslint-config-test",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC"
}

```

Next, it's time to add your ESLint dependencies:

```bash
npm install -D eslint eslint-config-airbnb eslint-config-prettier eslint-plugin-import eslint-plugin-jsx eslint-plugin-prettier eslint-plugin-react eslint-plugin-react-hooks prettier

```

The packages will change according to your needs. In this case, I work with React codebases and I use [Prettier](https://prettier.io/) to format my code. The [documentation](https://eslint.org/docs/developer-guide/shareable-configs#publishing-a-shareable-config) mentions that if your shareable config depends on a plugin, you should also specify it as a `peerDependency`.

Next, I will create a `.eslintrc.js` with my configuration - this is similar to what you already do in your apps:

```js
module.exports = {
  extends: [
    'airbnb',
    'eslint:recommended',
    'plugin:import/errors',
    'plugin:react/recommended',
    'plugin:jsx-a11y/recommended',
    'plugin:prettier/recommended',
    'prettier/react',
  ],
  plugins: [
    'react-hooks',
  ],
  rules: {
  },
};

```

The `rules` object stores any rule that you want to override. In the snippet above `rules` is empty but feel free to check [my overrides](https://github.com/leonardofaria/eslint-config-leozera/blob/master/.eslintrc.js#L14:L58). In the Airbnb/JavaScript repository you can [find a list of overridden rules](https://github.com/airbnb/javascript/issues/1089) by the community.

### Create custom rules

Time to create a `.prettierrc` with your custom rules - this is a tricky part since Prettier and ESLint can conflict on a few rules:

```json
{
  "tabWidth": 2
}

```

It is important to mention that the `.prettierrc` file should live in the root of the project that is using your package. Right now, I am manually copying it. 

The next step is to export your config in the `index.js` file:

```js
const eslintrc = require('./.eslintrc.js');

module.exports = eslintrc;

```

It is technically possible to create all configurations in the `index.js` file. But if you do this, you won't get the config object linted (insert your [Inception](https://www.imdb.com/title/tt1375666/) joke here).

### You're done!

_Voilà!_ That’s all you need to start your own package of configurations. You can test locally your config package by running the following in a JavaScript project:

```bash
npm install /Users/leonardo/path/to/eslint-config-test

```

Keep in mind that the dependencies of your configuration package may also be installed.

If everything looks fine, you can publish to the npm registry:

```bash
npm publish

```

## Full example

I have a functional GitHub project showing the setup of this post: [eslint-config-leozera](https://github.com/leonardofaria/eslint-config-leozera). You can also see it below:

%[https://codesandbox.io/embed/github/leonardofaria/eslint-config-leozera/tree/master/?fontsize=14&theme=dark]

## More about the project

* [Configuring ESLint](https://eslint.org/docs/user-guide/configuring): official ESLint docs. You know, _read the docs_
* [How to publish your first NPM package](https://medium.com/@bretcameron/how-to-publish-your-first-npm-package-b224296fc57b): quoting the post subtitle – "everything you need to know to create a NPM package."
* [eslint-config-wesbos](https://github.com/wesbos/eslint-config-wesbos): a project by [Wes Bos](https://www.wesbos.com/) that helped me while doing this work

Also posted on [my blog](https://bit.ly/2AKW42t). If you like this content, follow me on [Twitter](https://twitter.com/leozera) and [GitHub](https://github.com/leonardofaria). Cover photo by [Susan Holt Simpson/Unsplash](https://unsplash.com/photos/2nSdQEd-Exc).

