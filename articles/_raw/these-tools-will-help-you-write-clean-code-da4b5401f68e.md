---
title: These tools will help you write clean code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-24T00:27:37.000Z'
originalURL: https://freecodecamp.org/news/these-tools-will-help-you-write-clean-code-da4b5401f68e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3OpyAlDBIinyME_ro6wq3A.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Adeel Imran

  A look at Prettier, ESLint, Husky, Lint-Staged and EditorConfig

  Learning to write good code, but you don’t know where to start… Going through style-guides
  like Airbnb’s Javascript Style Guide… Trying to write code with best practices.....'
---

By Adeel Imran

#### A look at Prettier, ESLint, Husky, Lint-Staged and EditorConfig

Learning to write good code, but you don’t know where to start… Going through style-guides like [Airbnb’s Javascript Style Guide](https://github.com/airbnb/javascript)… Trying to write code with best practices...

Removing dead code? Finding unused variables in the code base? Trying to find problematic patterns in your code? Like, does it `return` or not?

Any of this sound familiar?

With so much to learn and do all at the same time, it is just so hectic.

Are you a Team Lead managing a diverse team? Do you have new developers on the team? Do you worry that they’ll write code not up to standards? Does it take all of your day in code reviews, where the review is more on the code standards rather then the actual logic implementation?

I have been there and done that, and it just is so tiring and hectic.

Let’s promise to never worry again about how the code should look or getting your entire team to write code in a certain way that is linted and formatted properly.

Throughout this tutorial, if you get stuck, here is the [code repository](https://github.com/adeelibr/react-starter-kit). Pull requests are welcome, if you have suggestions for improvements.

This tutorial is catered more towards React applications, but the same can be applied on any web project.

Also the editor I am using for this tutorial is [VS Code](https://code.visualstudio.com/). It’s by [Microsoft](https://www.microsoft.com/en-us/) and ever since they have been into open source, I have been in ❤ with this company (although there was a time when I wasn’t).

### Agenda

* Prettier
* ESLint
* Automate Format and Lint on Save
* Husky
* Lint-staged
* With Husky and Lint-staged Combined
* EditorConfig

### Let’s start with Prettier

#### **_What is Prettier?_**

[Prettier](https://prettier.io/) is an opinionated code formatter. It formats code for you in a specific way.

This GIF pretty much explains it:

![Image](https://cdn-media-1.freecodecamp.org/images/1*opcd-o83ElQvQNP84oDgyQ.gif)
_Prettier formatting my code, like a boss!_

#### **_Why do we need it?_**

* **Cleans up existing code base**: on a single command line. Imagine cleaning a code base with over 20,000 lines of code.
* **Easy to adopt**: Prettier uses the least controversial coding style while formatting your code. Since it’s open source, many folks have worked on several iterations of it in fixing some edge cases and polishing the experience.
* **Writing code**: What people don’t realize is that they spend a lot of time formatting code and wasting their mental energy doing so. Let Prettier handle it while _you_ focus on the core business logic. On a personal note, Prettier has increased my efficiency by 10%.
* **Helping Newbie Developers**: If you are a new developer working side by side with great engineers and you want to look _cool_ writing clean code, be smart! Use Prettier.

#### **_How do I set it up?_**

Create a folder called `app` and inside that folder type on the command line:

```
npm init -y
```

This will create a `package.json` file for you inside the `app` folder.

Now, I am going to use `yarn` throughout this tutorial, but you can use `npm` as well.

Let’s install our first dependency:

```
yarn add --dev prettier
```

This will install a dev dependency in your `package.json` which will look like this:

```json
{
  "name": "react-boiler-plate",
  "version": "1.0.0",
  "description": "A react boiler plate",
  "main": "src/index.js",
  "author": "Adeel Imran",
  "license": "MIT",
  "scripts": {
    "prettier": "prettier --write src/**/*.js"
  },
  "devDependencies": {
    "prettier": "^1.14.3"
  }
}
```

I’ll talk in a second what this `“prettier”: “prettier — write src/**/*.js”` does, but first let’s create a `src/` folder inside our `app` folder. And inside the `src/` folder let’s create a file called `index.js` — you can call it whatever you want.

In the `index.js` file, paste this code as it is:

```javascript
let person =                     {
  name: "Yoda",
                designation: 'Jedi Master '
                };


              function trainJedi (jediWarrion) {
if (jediWarrion.name === 'Yoda') {
  console.log('No need! already trained');
}
console.log(`Training ${jediWarrion.name} complete`)
              }

trainJedi(person)
              trainJedi({ name: 'Adeel',
              designation: 'padawan' 
  });
```

So up till now we have a `src/app/index.js` file with some ugly code written in it.

There are 3 things we can do about it:

* Manually indent and format this code
* Use an automated tool
* Let things go and move on (Please don’t choose this option)

I am going to go for the second option. So now we have a dependency installed and a Prettier script written in our `package.json`.

Let’s create a `prettier.config.js` file in our root `app` folder, and add some prettier rules to it:

```javascript
module.exports = {
  printWidth: 100,
  singleQuote: true,
  trailingComma: 'all',
  bracketSpacing: true,
  jsxBracketSameLine: false,
  tabWidth: 2,
  semi: true,
};
```

`printWidth` will ensure that your code does not exceed more then 100 characters.

`singleQuote` will convert all your double quotes into single quotes.   
Read more in the Airbnb JavaScript Style Guide [here](https://github.com/airbnb/javascript). This guide is my playbook for writing good code and impressing my colleagues.

`trailingComma` will ensure there is a dangling comma at the end of last object property. [Nik Graf](https://twitter.com/nikgraf) explains this in such a cool way [here](https://medium.com/@nikgraf/why-you-should-enforce-dangling-commas-for-multiline-statements-d034c98e36f8)_._

`bracketSpacing` prints spaces between object literals:

```
If bracketSpacing is true - Example: { foo: bar }If bracketSpacing is false - Example: {foo: bar}
```

`jsxBracketSameLine` will put `&`gt; of a multi line JSX element on the last line:

```javascript
// true example

<button
  className="prettier-class"
  id="prettier-id"
  onClick={this.handleClick}>
  Click Here
</button>

// false example

<button
  className="prettier-class"
  id="prettier-id"
  onClick={this.handleClick}
>
  Click Here
</button>
```

`tabWidth` specifies the number of spaces per indentation level.

`semi` if true will print `;` at the end statements.

Here is a list of all the [options](https://prettier.io/docs/en/options.html) that you can give Prettier.

Now that we have the configuration set up, let’s talk about this script:

```
“prettier”: “prettier  — write src/**/*.js”
```

In the script above, I am running `prettier` and telling it to find all `.js` files in my `src/` folder. The `--write` flag tells `prettier` to save the formatted files as it goes through each file and finds any anomaly in the code formation.

Let’s run this script in your terminal:

```
yarn prettier
```

This is what happens to my code when I run it:

![Image](https://cdn-media-1.freecodecamp.org/images/1*XLy2nZkWeQz7gghWtweGKA.gif)
_Cool, right?_

If you got stuck, feel free to have a look at the [repository](https://github.com/adeelibr/react-starter) for this.

This pretty much concludes our Prettier discussion. Let’s talk about linters.

### ESLint

#### **_What is a code linter?_**

> Code [linting](https://en.wikipedia.org/wiki/Lint_(software)) is a type of static analysis that is frequently used to find problematic patterns or code that doesn’t adhere to certain style guidelines. There are code linters for most programming languages, and compilers sometimes incorporate linting into the compilation process. — [ESLint](https://eslint.org/docs/about/)

#### **_Why do we need one for JavaScript?_**

Since JavaScript is dynamic and a loosely typed [language](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures), it is prone to developer errors. Without the benefit of a compilation process, `.js` files are typically executed in order to find syntax or other errors.

Linting tools like [ESLint](https://eslint.org/) allow developers to find problems with their JavaScript code without executing it.

#### **_What makes ESLint so special?_**

Good question! Everything in ESLint is pluggable. You can add rules on run time — the rules and formatter don’t have to be bundled to be used. Every linting rule you add is stand alone, any rule can be turned on or off. Each rule can be set to a warning or an error. Your choice.

Using ESLint, you get complete customization of how you want your style guide to look.

Now there are 2 popular style guides out there at the moment:

* [Google JavaScript Style Guide](https://google.github.io/styleguide/jsguide.html)
* [Airbnb JavaScript Style Guide](https://github.com/airbnb/javascript#table-of-contents)

I have personally been using Airbnb’s Style Guide. This was recommended to me by my head of engineering in my last firm when I was starting out in my professional career, and this has been the most valuable asset at my disposal.

This style guide is actively maintained — check out their [GitHub repo](https://github.com/airbnb/javascript). I’ll be using the rule sets inspired by Airbnb’s Style Guide throughout this tutorial. So let’s begin.

Let’s first update our `package.json` file:

```json
{
  "name": "react-boiler-plate",
  "version": "1.0.0",
  "description": "A react boiler plate",
  "main": "src/index.js",
  "author": "Adeel Imran",
  "license": "MIT",
  "scripts": {
    "lint": "eslint --debug src/",
    "lint:write": "eslint --debug src/ --fix",
    "prettier": "prettier --write src/**/*.js"
  },
  "husky": {
    "hooks": {
      "pre-commit": "lint-staged"
    }
  },
  "lint-staged": {
    "*.(js|jsx)": ["npm run lint:write", "git add"]
  },
  "devDependencies": {
    "babel-eslint": "^8.2.3",
    "eslint": "^4.19.1",
    "eslint-config-airbnb": "^17.0.0",
    "eslint-config-jest-enzyme": "^6.0.2",
    "eslint-plugin-babel": "^5.1.0",
    "eslint-plugin-import": "^2.12.0",
    "eslint-plugin-jest": "^21.18.0",
    "eslint-plugin-jsx-a11y": "^6.0.3",
    "eslint-plugin-prettier": "^2.6.0",
    "eslint-plugin-react": "^7.9.1",
    "husky": "^1.1.2",
    "lint-staged": "^7.3.0",
    "prettier": "^1.14.3"
  }
}
```

Before heading forward with the configuration, I strongly believe that people should know what goes into their dependencies. So let’s talk about what each of these package does and then we can move forward with the configurations.

`babel-eslint`: this package allows you to use lint on all [Babel](https://babeljs.io/) goodness easily. You don’t necessarily need this plugin if you are not using [Flow](https://flow.org/) or experimental features that are not yet supported by ESLint.

`eslint`: this is the main tool that is needed for linting your code.

`eslint-config-airbnb`: this package provides all the Airbnb’s ESLint configuration as an extensible shared configuration, which you can modify.

`eslint-plugin-babel`: An `eslint` plugin companion to `babel-eslint`.   
`babel-eslint` does a great job at adapting `eslint` for use with Babel.

`eslint-plugin-import`: This plugin intends to support linting of `ES2015+ (ES6+)` `import/export syntax,` and prevent issues with misspelling of file paths and import names. [Read more](https://github.com/benmosher/eslint-plugin-import)_._

`eslint-plugin-jsx-a11y`: linting rules in place for accessibility rules on JSX elements. Because **accessibility is important!**

`eslint-plugin-prettier`: This helps ESLint work smoothly with Prettier. So when Prettier formats code, it does it keeping our ESLint rules in mind.

`eslint-plugin-react`: React-specific linting rules for ESLint.

Now this tutorial doesn’t talk much about unit testing for [Jest/Enzyme](https://airbnb.io/enzyme/docs/guides/jest.html). But if you are using it, let’s add linting rules for them as well:

`eslint-config-jest-enzyme`: This helps with React- and Enzyme-specific variables which are globalized. This lint config lets ESLint know about those globals and not warn about them — like the assertions `it` and `describe`.

`eslint-plugin-jest`: ESLint plugin for Jest.

`husky`: More on this later when in the automation section.

`lint-staged:` More on this later when in the automation section.

Now that we have a basic understanding, let’s begin;

Create a `.eslintrc.js` file in your root `app/` folder:

```
module.exports = {
	env: {
		es6: true,
		browser: true,
		node: true,
	},
	extends: ['airbnb', 'plugin:jest/recommended', 'jest-enzyme'],
	plugins: [
		'babel',
		'import',
		'jsx-a11y',
		'react',
		'prettier',
	],
	parser: 'babel-eslint',
	parserOptions: {
		ecmaVersion: 6,
		sourceType: 'module',
		ecmaFeatures: {
			jsx: true
		}
	},
	rules: {
		'linebreak-style': 'off', // Don't play nicely with Windows.

		'arrow-parens': 'off', // Incompatible with prettier
		'object-curly-newline': 'off', // Incompatible with prettier
		'no-mixed-operators': 'off', // Incompatible with prettier
		'arrow-body-style': 'off', // Not our taste?
		'function-paren-newline': 'off', // Incompatible with prettier
		'no-plusplus': 'off',
		'space-before-function-paren': 0, // Incompatible with prettier

		'max-len': ['error', 100, 2, { ignoreUrls: true, }], // airbnb is allowing some edge cases
		'no-console': 'error', // airbnb is using warn
		'no-alert': 'error', // airbnb is using warn

		'no-param-reassign': 'off', // Not our taste?
		"radix": "off", // parseInt, parseFloat radix turned off. Not my taste.

		'react/require-default-props': 'off', // airbnb use error
		'react/forbid-prop-types': 'off', // airbnb use error
		'react/jsx-filename-extension': ['error', { extensions: ['.js'] }], // airbnb is using .jsx

		'prefer-destructuring': 'off',

		'react/no-find-dom-node': 'off', // I don't know
		'react/no-did-mount-set-state': 'off',
		'react/no-unused-prop-types': 'off', // Is still buggy
		'react/jsx-one-expression-per-line': 'off',

		"jsx-a11y/anchor-is-valid": ["error", { "components": ["Link"], "specialLink": ["to"] }],
		"jsx-a11y/label-has-for": [2, {
			"required": {
				"every": ["id"]
			}
		}], // for nested label htmlFor error

		'prettier/prettier': ['error'],
	},
};
```

Also add a `.eslintignore` file in your root `app/` directory:

```
/.git
/.vscode
node_modules
```

Let’s start by discussing what a `.eslintrc.js` file does.

Let’s break it down:

```javascript
module.exports = { 
   env:{}, 
   extends: {}, 
   plugin: {}, 
   parser: {}, 
   parserOptions: {}, 
   rules: {},
};
```

* `env:` An environment defines global variables that are predefined. The available environments — in our case it is `es6`, `browser` and `node`.   
`es6` will enable all ECMAScript 6 features except for modules (this automatically sets the `ecmaVersion` parser option to 6).   
`browser` will add all browser global variables such as `Windows`.  
 `node` will add Node global variables and Node scoping, such as `global`. You can [read more](https://eslint.org/docs/user-guide/configuring#specifying-environments) on specifying environments.
* `extends:` An array of strings — each additional configuration extends the preceding configurations.   
Right now we are using the linting rules by `airbnb` which are extended to `jest` and then extended to `jest-enzyme`.
* `plugins:` plugins are basically linting rules that we want to use.   
Right now we are using `babel, import, jsx-a11y, react, prettier`, all of which I have explained above.
* `parser:` By default ESLint uses [Espree](https://github.com/eslint/espree), but since we are using `babel`, we need to use [Babel-ESLint](https://www.npmjs.com/package/babel-eslint).
* `parserOptions:` When we change the default parser for `Espree` to `babel-eslint` , we need to specify `parserOptions` — it is required.   
In the options I tell ESLint that `ecmaVersion` is going to lint version `6`. Since we are writing our code in an EcmaScript `module` and not a `script` we specify `sourceType` as `module`.   
Since we are using React which brings in JSX, in `ecmaFeatures` I pass it an option of `jsx` and set it to `true`.
* `rules:` This is the part which I love the most about ESLint, the customization.   
All the rules that we have extended and added with our plugins, we can change or override. `rules` is the place where you do it. I have already put comments in the Gist against each rule and for your understanding.

Now that’s cleared up, let’s talk about `.eslintignore`

`.eslintignore` takes a list of paths that we want ESLint to not lint. Here I specify only three:

* `/.git` I don’t want my Git-related files to be linted.
* `/.vscode` Since I am using VS Code, this editor comes in with it’s own configuration that you can set for each project. I don’t want my configuration(s) to be linted. I use VS Code because it is lightweight and open source.
* `node_modules` I don’t want my dependencies to get linted. So I have added this to the list.

Now that we are done with that, let’s talk about the newly added scripts to our `package.json`

```
"lint": "eslint --debug src/"
"lint:write": "eslint --debug src/ --fix"
```

* `$ yarn lint` running this command, it will go through all of your files in `src/` and will give you a detail log in each file where it finds errors, which you can then go in manually and correct them out.

![Image](https://cdn-media-1.freecodecamp.org/images/1*yfvCg7YG_IpFFbZYzBv8IA.gif)
_running **yarn lint | npm run lint**_

* `$ yarn lint:write` running the command, it will do the same as what the above command does. The only addition is that if it can correct any of the errors it sees, it is going to correct them and try to remove as much code smell from your code as it can.

If you get stuck, feel free to have a look at the [**repository**](https://github.com/adeelibr/react-starter) for this.

That was a bit hectic and if you have followed along so far:

![Image](https://cdn-media-1.freecodecamp.org/images/1*pi2nGW17A7cFXX2hc6apPA.gif)
_Professor Snape is proud of you. Good job._

### Let’s Automate A Bit More

So far we have `prettier` and `eslint` setup, but every time we have to run a script. Let’s do something about it.

* Format and Lint Code on hitting `ctrl+s` in your editor.
* Every time you commit your code, execute a pre-command automatically that lints and formats your code.

#### Format and Lint Code On Save

For this you need to use an editor like [VS Code](https://code.visualstudio.com/):

* Install a plugin called ESLint extension.  
[Download here](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint) or press `ctrl+shift+x` in your VS Code editor. This will open up the extensions module. There, search type `eslint`. A list of plugins will appear. Install the one by `Dirk Baeumer`. Once that is installed hit the `reload` button to restart your editor.

Once you have this plugin installed, in your root `app/` folder create a folder called `.vscode/` — the (dot) is important in the filename.

Inside the folder create a `settings.json` file like below:

```json
{
  "editor.formatOnSave": false,
  "eslint.autoFixOnSave": true,
}
```

* `editor.formatOnSave` I have set the value to `false` here because I don’t want the default editor configuration for file format to conflict with ESLint and Prettier.
* `eslint.autoFixOnSave` I have set the value to `true` here because I want the installed plugin to work every time I hit save. Since ESLint is configured with Prettier configurations, every time you hit `save` it will format and lint your code.

Also important thing to note here is that when you run the script  
`yarn lint:write` now it will lint and prettify your code on the same go.

Just imagine if you where handed a code base of 20k lines of code to audit and improve. Now imagine doing it manually. Improving unknown code. Now imagine doing it with a single command. The manual approach might take 30 days...while the automatic approach will take you 30 seconds.

So the scripts are set up, and every time you hit `save` the editor will do the magic for you for that specific file. But not everyone in your team will opt for VS Code and that’s okay. So let’s automate a bit more.

### Husky

#### What is husky?

[Husky](https://github.com/typicode/husky) basically let’s you Git hook. That means you can perform some certain actions when you are about to commit or when you are about to push code to a branch.

All you have to do is install Husky:

```
yarn add --dev husky
```

and in your `package.json` file add the snippet:

```
"husky": {    
   "hooks": {      
     "pre-commit": "YOUR_COMMAND_HERE", 
     "pre-push": "YOUR_COMMAND_HERE"   
   }  
},
```

So every time you commit or push, it will execute a certain script or command — like run test cases or format your code.

You can read more on Husky [here](https://github.com/typicode/husky#install).

### Lint-staged

#### **_What is Lint-staged?_**

[Lint-staged](https://github.com/okonet/lint-staged) helps you run linters on staged files, so that bad code doesn’t get pushed to your branch.

#### **_Why Lint-staged?_**

Linting makes more sense when run before committing your code. By doing so you can ensure no errors go into the repository and enforce code style. But running a lint process on a whole project is slow and linting results can be irrelevant. Ultimately you only want to lint files that will be committed.

This project contains a script that will run arbitrary shell tasks with a list of staged files as an argument, filtered by a specified glob pattern. You can [read more here](https://github.com/okonet/lint-staged#why).

All you have to is install Lint-staged:

```
yarn add --dev lint-staged
```

then in your `package.json` file add this:

```
"lint-staged": {    
   "*.(js|jsx)": ["npm run lint:write", "git add"]  
},
```

What this command will do is run the `lint:write` command first and then add it in the staging area. It will run this command for only `.js` & `.jsx` files, but you can do the same for other files as well if you want.

#### With H`usky` and L`int-staged` combined

Every time your commit your code, before committing your code, it will run a script called `lint-staged` which will run `npm run lint:write` which will lint and format your code — then add it to the staging area and then commit. Cool right?!

Your final `package.json` file should look like this. This is the same snippet I shared above:

```json
{
  "name": "react-boiler-plate",
  "version": "1.0.0",
  "description": "A react boiler plate",
  "main": "src/index.js",
  "author": "Adeel Imran",
  "license": "MIT",
  "scripts": {
    "lint": "eslint --debug src/",
    "lint:write": "eslint --debug src/ --fix",
    "prettier": "prettier --write src/**/*.js"
  },
  "husky": {
    "hooks": {
      "pre-commit": "lint-staged"
    }
  },
  "lint-staged": {
    "*.(js|jsx)": ["npm run lint:write", "git add"]
  },
  "devDependencies": {
    "babel-eslint": "^8.2.3",
    "eslint": "^4.19.1",
    "eslint-config-airbnb": "^17.0.0",
    "eslint-config-jest-enzyme": "^6.0.2",
    "eslint-plugin-babel": "^5.1.0",
    "eslint-plugin-import": "^2.12.0",
    "eslint-plugin-jest": "^21.18.0",
    "eslint-plugin-jsx-a11y": "^6.0.3",
    "eslint-plugin-prettier": "^2.6.0",
    "eslint-plugin-react": "^7.9.1",
    "husky": "^1.1.2",
    "lint-staged": "^7.3.0",
    "prettier": "^1.14.3"
  }
}
```

Now every time you do this:

```
$ git add .$ git commit -m "some descriptive message here"
```

It will lint and format your code based on all the rules put in the  
`.eslintrc.js` file. With this you can be sure that no bad code ever gets pushed to production.

With this section concluded, you now have `prettier`, `eslint` and `husky` integrated in your code base.

### Let’s talk about EditorConfig

First create a `.editorconfig` file in your root `app/` folder, and in that file paste the code below:

```
# EditorConfig is awesome: http://EditorConfig.org

# top-most EditorConfig file
root = true

[*.md]
trim_trailing_whitespace = false

[*.js]
trim_trailing_whitespace = true

# Unix-style newlines with a newline ending every file
[*]
indent_style = space
indent_size = 2
end_of_line = lf
charset = utf-8
insert_final_newline = true
max_line_length = 100
```

#### **_So what is EditorConfig?_**

So not everyone is going to use VS Code — and you can’t enforce it, nor should you. In order to keep everyone on the same page in terms of what the defaults, such as `tab space` or `line ending` should be, we use  
`.editorconfig`. This actually helps enforce some certain rule sets.

Here is the list of all the editors that support [EditorConfig](https://editorconfig.org/). The list of editors includes Web storm, App code, Atom, eclipse, emacs, bbedit and so many more.

The above configuration will do the following:

* trim trailing white spaces from `.md` & `.js` files
* set indent style to `space` instead of `tab`
* indent size to `2`
* end of line to be `lf` so that everyone, irrespective of their OS, has the same end of line. [Read more here](https://stackoverflow.com/questions/1552749/difference-between-cr-lf-lf-and-cr-line-break-types).
* there should be a new line at end of file
* and the max line length should be `100` chars

With all this configuration done and in place, you are now ready. If you want to see the [**source code**](https://github.com/adeelibr/react-starter-kit/) here it is**.**

Also pull requests are welcome if you feel like you can improve anything in this repository.

If you liked my article, you should also check out my other article: [**How to combine Webpack 4 and Babel 7 to create a fantastic React app**](https://medium.freecodecamp.org/how-to-combine-webpack-4-and-babel-7-to-create-a-fantastic-react-app-845797e036ff) in which I talk about setting up Webpack and Babel for React.

