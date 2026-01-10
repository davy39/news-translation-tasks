---
title: Alternatives to Prettier – Popular Code Linting and Formatting Tools
subtitle: ''
author: Kamaldeen Lawal
co_authors: []
series: null
date: '2023-03-15T17:43:50.000Z'
originalURL: https://freecodecamp.org/news/alternatives-to-prettier
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Alternatives-to-Prettier.png
tags:
- name: clean code
  slug: clean-code
- name: eslint
  slug: eslint
- name: Prettier
  slug: prettier
seo_title: null
seo_desc: "Many programmers hate code formatting because it is tedious and time-consuming.\
  \ You can spend hours making sure everything is perfect and well-indented. \nThis\
  \ is why code formatters are so useful.\nA code formatter is a tool that formats\
  \ code accordin..."
---

Many programmers hate code formatting because it is tedious and time-consuming. You can spend hours making sure everything is perfect and well-indented. 

This is why code formatters are so useful.

A code formatter is a tool that formats code according to certain standards. It makes it so you don't have to worry as much about code formatting. Instead, you can focus on writing good code. This save time and also reduces your stress.

In this guide, we will talk about the Prettier code formatter. We will also talk about alternatives to Prettier like JsFmt, StandardJS, EsLint + EditorConfig, and Beautifier. Hopefully you’ll take away something that you can use to improve your code formatting.

## Brief Overview of Prettier

[Prettier](https://prettier.io/) is a popular code formatter that can handle complex code structures and format your code in a readable way.

It operates on the principle of no configuration required and it's designed to produce readable, consistent code. 

Prettier is an opinionated tool that encourages programmers to follow its formatting rules. It also parses the code and reprints it uniformly.

## Why Explore Alternatives to Prettier?

There are many advantages of using Prettier. But like every other tool, exploring alternatives is sometimes a good idea. Here are some of the reasons for exploring alternatives to Prettier:

1. **Inflexible style guides**: Prettier adopts a strict set of formatting rules, and does not allow for much customization. Some programmers want a tool with a lot of configurations available.
2. **Speed**: Although Prettier is fast, you may need a tool that provides faster and better performance in large codebases or real-time formatting.
3. **Language support**: Prettier may not support (or might offer inadequate support) for the language you use.
4. **More features**: While Prettier is open source, you might prefer a paid code formatter that has more features and better integration with other tools.

In the guide, we will talk about four alternatives to Prettier. They are:

* JsFmt
* StandardJS
* ESLint+EditorConfig
* JS Beautifier

## JsFmt Overview

[JsFmt](https://rdio.github.io/jsfmt/) is a code formatter that uses esformatter as a formatting tool. It automatically reformats JavaScript code according to a set of predefined rules. It is available specifically to re-write, format, search, and validate JavaScript code.

To install JsFmt, run this command:

```
npm install -g jsfmt
```

A .jsfmtrc file, which can either be a JSON or INI formatted file, can overwrite any of the esformatter formatting options.

```json
{
  "indent": 4,
  "line_ending": "unix",
  "quote": "single"
}

```

In this example, we specified the spaces for indentation to be four, we chose line-ending to be unix, and we picked single as the quote style for strings.

You can use the jsfmt rewrite method to change values in your JavaScript code. Here's an example of how to do that:

```javascript
const x = 5;
const y = 10;
const z = x + y;
console.log(z);

//  The output will change to the below code after writing:  npx jsfmt --rewrite '5 -> 20' reduce.js

const x = 20;
const y = 10;
const z = x + y;
console.log(z);

```

To learn more about JsFmt, you can read its documentation [here](https://github.com/rdio/jsfmt).

### Features of JsFmt

1. Formating: JsFmt can format code according to a set of predefined rules.
2. Integrations: you can integrate JsFmt with popular code editors like Visual Studio Code, Sublime Text, and Atom, making it easy to format your code directly in your editor.
3. Command-line interface: JsFmt allows you to format your code as part of your build process or development workflow in the command line.

### JsFmt Formatting Rules

Some of the formatting rules adopted by JsFmt are as follows

1. Set indent: With the `--indent` option, JsFmt indents your code with two spaces per level.
2. Quotes: In JsFmt, single quotes are the default for strings, but you can change this with the `--double-quote` option.
3. Wrapping: you can use `--linene-width` to change the default wrap lines setting in JsFmt.
4. Semicolons: JsFmt adds semicolons at the end of each statement by default. You can disable this using the `--no-semi` option.

### Pros of JsFmt

1. Formatting, searching, and re-writing of JavaScript.
2. Customizable: JsFmt's flexibility makes it a popular choice for many development teams. It is a highly customizable tool that you can configure to match the specific requirements of a project.

### Con of JsFmt

1. Lack of flexibility: despite the fact that it's customizeable, certain parts of JsFmt may not always be configurable to match the needs of your project.

## StandardJS Overview

[StandardJS](https://standardjs.com/) is an open-source, no configuration linter, formatter, and JavaScript style guide. It checks the code for probable errors with the linter. It also formats code automatically, and helps you write code that is easy to read and understand.

It is the most popular option, coming in at 27,905 stars on GitHub clean code linter. It is also a powerful tool for ensuring the quality and consistency of your JavaScript code.

You can either install it globally or locally on your machine. To install globally, use the first command, while the second command is for installing locally. Note that to install it, you must have Node and npm installed on your computer.

To install globally: `$ npm install standard --global`

To install locally: `$ npm install standard --save-dev`

Alternatively, you can add StandardJS to the package JSON.

```json
{
  "name": "my-cool-package",
  "devDependencies": {
    "standard": "*"
  },
  "scripts": {
    "test": "standard && node my-tests.js"
  }
}

```

The styles are checked automatically when you run the command:

```
npm test
```

To illustrate how it works, check the JavaScript code below:

```javascript!
let number = 10;
if (number == 10) {
  alert("yes");
} else {
  alert("no");
}

// The Output after running the npm test in the terminal

> test
> standard && node my-tests.js

standard: Use JavaScript Standard Style (https://standardjs.com)
  C:\Users\hp\Desktop\pretier\Js\script.js:5:5: Parsing error: Unexpected token else (null)

```

StandardJS shows that the code has a parsing error.

To fix most issues, run the following code:

```
standard --fix
```

### Features of StandardJS

1. Community: A community of contributors guides the development of StandardJS by providing bug fixes and new features.
2. Linting: StandardJS linting catches style issues and programmer errors early.
3. Automatic code formatting: StandardJS get rid of messy and inconsistent code.
4. Command line integration: It has a command-line interface for running linter checks and auto-formatting code.

### StandardJS Formatting Rules

Some of the widely used StandardJS formatting rules are listed below:

1. Indentation: StandardJS enforces a consistent indentation level of 2 spaces by default. To strictly implement this, you need to add the `--fix` option.
2. Line wrap: StandardJS doesn't enforce the rule of line length, but it recommends keeping lines shorter than 80 characters. Use `$ myfile.js | standard --stdin` to manually check the file length.
3. Semicolons: StandardJS recommends using semicolons for clarity and to avoid potential issues. But the tool doesn't enforce this. To enforce the use of semicolons, use this:

```json
{
  "extends": "standard"
}

```

1. Spaces around operators: StandardJS recommends using spaces around operators, such as + and -, but it doesn't enforce this rule.

### Pros of StandardJS

1. Zero configuration: No decisions to make. StandardJS is the easiest way to enforce code quality in your project.
2. Easy installation: StandardJS is easy to install, and you can use it with most editors and IDEs.
3. Enhances Productivity: StandardJS saves developers time and increases productivity by formatting code according to its rules.
4. Wide support: Most editors and IDEs support StandardJS using plugins and integrations.
5. Consistency: StandardJS promote consistency across projects by enforcing a strict set of coding rules.

### Cons of StandardJS

1. Opinionated: Some developers may find the tool too opinionated. If that's the case, you might prefer to use other linting tools that allow for more customization.
2. Limited flexibility: StandardJS enforces a strict set of rules and conventions, which some developers may feel restricted by and prefer a more customizable approach.

## ESLint + EditConfig Overview

[ESlint](https://eslint.org/) provides configurable rules that you can tailor according to your specific project needs. It is one of the most popular JavaScript linter that analyzes programming errors, bugs, and suspicious constructs.

You can extend its functionality by adding plugins, which can provide custom parsers and extra rules.

You'll need Node installed on your before installing ESLint. To install it, use the command below:

```
npm init @eslint/config
```

Alternatively, you can create this manually on your machine:

```
npm install --save-dev eslint
```

For both installations, you need to have installed a package.json file. If not, run this command

```
npx eslint --init
```

The command will ask a series of questions about your project, coding style, and preferences to generate your configuration file.

You can run ESLint on any of your directories or files with this command:

```
npx eslint yourfile.js
```

Rules can be turned off and you can run the toolonly with basic syntax validation, as ESLint is configurable and flexible to your use case.

Once you have generated the configuration file, you can customize according to your needs. The configuration file is a JavaScript file that exports an object with the configuration settings.

For example, you can specify the rules you want, plugins to use, and environments for your code:

```json
{
  "rules": {
    "semi": ["error", "always"],
    "quotes": ["error", "double"],
    "indent": ["error", 4]
  }
}

```

The semi, quotes, and indent are the names of the rules in ESLint, while the error level of the rule is the first value. There are only three outputs for the first values. They are:

* "off" or 0 - turn the rule off
* "warn" or 1 - turn the rule on as a warning (doesn’t affect exit code)
* "error" or 2 - turn the rule on as an error (exit code will be 1).

```json
{
  "env": {
    "browser": true,
    "es2021": true
  },
  "extends": "eslint: recommended",
  "overrides": [],
  "parserOptions": {
    "ecmaVersion": "latest"
  },
  "rules": {
    "indent": ["error", 4],
    "quotes": ["error", "single"],
    "semi": ["error", "never"]
  }
}

```

In this example, you specify that your code should run in a browser environment. Enable ECMAScript 2018 syntax, and follow the ESLint rules. You've also enabled three specific rules: indent, quotes, and semi.

The indent rule determines that an alert error will be thrown if indentation is more than 4 spaces. Likewise if you use double-quotes instead of single, there will be an error. You also specified not to use semi-colons.

To fix most of the issues in ESLint, use this command:

```
npx eslint yourfile.js --fix
```

Here's an example:

```javascript
const numbers = [1, 3, 5, 2, 6, 78, 8];
let peoples = ["shola", "kamal"];
console.log(peoples);

// The output

 error  'numbers' is assigned a value but never used  no-unused-vars
   error  Extra semicolon                               semi

✖ 2 problems (2 errors, 0 warnings)
  1 error and 0 warnings potentially fixable with the `--fix` option.

```

### EditorConfig Overview

[EditorConfig](https://editorconfig.org/#file-format-details) is an open-source file format. It provides standard ways of defining and maintaining coding styles in a project.

It maintains consistent coding styles which is especially useful when you have many developers working on the same project across various editors and IDEs. The tool consists of a collection of text editor plugins that enable editors to read the file format and adhere to defined styles.

You'll need to create a file named .editorconfig in the directory. EditorConfig plugins will look for the file in the directory of the opened file and on every parent directory.

Files are read from top to bottom, and a search for .editorconfig files will stop if the root file path is reached.

Creating an EditorConfig file is straightforward. Open a new file, and save it with .editorconfig as shown below.

![editorconfig file](https://i.imgur.com/SHEafBl.png)

Inside the .editorconfig file, the following wildcard patterns are used:

```javascript
root = true

[*]
 
indent_size = 4
indent_style = space
end_of_line = lf
insert_final_newline = true

 // Set root to true: A search for .editorconfig files will stop if the root file path is reached or an EditorConfig file with root=true is found.
 
 //[*]: Except for path selectors, it matches any string of characters.
 
 //indent_size: Indent size is set to 4. 
 //Indent_style: set to space
 //end_of_line: Set to lf
//insert_final_newline: Set to true

```

To know more about the wildcards pattern, visit the [EditorConfig docs](https://editorconfig.org/#file-format-details).

Using ESLint and EditorConfig together can help to spot potential issues early. It also ensures that your code is consistent, maintainable, and of high quality.

The combination of ESLint and EDitorConfig saves you time on code maintenance and debugging.

### Features of ESLint

1. Configurable: ESLint allows you to customize and add your own rules to the configuration file.
2. Support ECMAScript: ESLint ensures your code is compatible with the latest language features.
3. Supports many file formats: ESLint can analyze JavaScript code in a variety of file formats, including but not limited to .js, .jsx, and .vue.
4. Integration: ESLint integrates seamlessly with Webpack and Gulp, which are popular build tools.

### ESLint Formatting Rules

Some of the popular formatting rules in ESLint are listed below:

1. Indentation: ESLint by default expects a four-space per level indent. But you can customize this using the popular `--fix` option.
2. Semicolons: ESLint enforces the use of semicolons at the end of each statement. This rule is set to "always" by default. Use the popular `--fix` option to reset it to "never".
3. Line wrap: Use the `max-len` rule to change the maximum line length from the default 80 to your preferred  value.
4. Quotes: The quotes rule can be changed from the default value of "single" to "double" using the `--fix` option.

### Pros of ESLint

1. Saves time: ESLint saves time by reducing the amount of time spent on manual code reviews and debugging.
2. Active Community: ESLint has a wide and active community base that contributes to the development of the tool and its ecosystem.
3. Code analyzer: ESLint analyze your code to quickly find problems.
4. Consistency: ESLint helps in maintaining clean and readable code by enforcing a consistent coding style.

### Cons of ESLint

1. Rule conflicts: With a large set of rules, ESLint rules can sometimes conflict with one another, resulting in more configuration and fine-tuning.
2. Steeper learning curve: ESLint has a pretty steep learning curve, as it has many rules and learning how to configure them can take time.
3. False positives: ESLint can sometimes flag code as problematic code even when it is correct, which can be frustrating for developers.

## Overview of JS Beautifier

[JavaScript Beautifier](https://beautifier.io/), also known as js-beautify, is an open-source, cross-platform command-line tool. It is a beautifier for re-formating and re-indenting bookmarklets, ugly JavaScript, and it partly deobfuscates scripts.

You can install JS beautifier both locally and globally.

Run `npm -g install js-beautify` to install globally, and `npm install js-beautify` to install locally.

You can configure it through the command line option.

After local installation, you can import and call the appropriate beautifier methods for JS, CSS, or HTML. An example of how to call the methods goes like this: beautify (`code`, `options`).

While `code` is the string of code to be beautified, `options` is an object with the settings you would like used to beautify the code. See the example below for a JavaScript script file:

```
npx beautify("script.js",{indent_size:4})

```

You can also configure it through a configuration file:

```json
{
  "indent_size": 4,
  "indent_char": " ",
  "indent_with_tabs": false,
  "brace_style": "collapse"
}

```

Create a file `.jsbeautifyrc` in the root directory of your project. This option will override the default option of JS beautifier. You can also use Beautifier on your web browser. Learn more about [JSbeautifer from its docs here](https://www.npmjs.com/package/js-beautify).

### Feature of JS Beautifier

1. Formatting: You can customize JS Beautifier to fit your personal preferences and coding style because it offers varieties of formatting options, such as indentation size and braces style.
2. Online version: You can beautify JavaScript using JS Beautifier in your web browser, just as you can on the command line.

### JS Beautifier Formatting Rules

1. Indentation: The default identation in JS Beautifier is 4 spaces, but you can change it to 2 or 8 spaces, or use tabs instead. Use the `indent_size` option to specify the number of spaces to use for indentation.
2. Semicolons: You can change your semicolon settings in JS Beautifier with the `semicolon` option. You change this by alternating the value of the semicolon option between "true" or "false".
3. Line wrap: Use the `max_char` option to limit each line to 80 characters. You can set the value of the max_char to 80 or any other preferred  number.

### Pros of JS Beautifier

1. Time-saving: JS Beautifier saves time. It automates the many steps of formatting and organizing code.
2. Online presence: JS Beautifier's online presence is a game changer, as a lot of non-developers will be able to use it.
3. Detects errors: JS Beautifier helps catch small errors that can be difficult to spot otherwise.
4. Integration: JS Beautifier's compatibility with varieties of code editors and IDEs makes it a versatile tool.

### Cons of JS Beautifier

1. Complexity: Despite having an online version, JS Beautifier is somewhat complex for beginners.
2. Potential for over-formatting: In some cases, JS Beautifier may make the code harder to read because of over-formatting.

## Results from all the Formatting Tools

We'll use the code sample below to test how these four popular tools format code:

```javascript
const numbers = [2,3,8,9,7]

          let peoples = ['kamal', 'lawal', "shola", "olaide"];


```

As you can see, this code isn't properly formatted. So let's try the tools to see how they help.

### Formatting example with JsFmt

Using the above code as a sample, the command `npx jsfmt --write "Your file"` will format the code to this:

```javascript
const numbers = [2, 3, 8, 9, 7]

let peoples = ['kamal', 'lawal', "shola", "olaide"];

```

As you can see, there is a noticeable change in the code, and you can configure this to your desired taste.

### Formatting example with StandardJS

By running the popular `npx standard--fix` command from the terminal, you will have the following result.

```javascript
const numbers = [2, 3, 8, 9, 7]

const peoples = ['kamal', 'lawal', 'shola', 'olaide']

```

Notice the code was properly formatted, most especially the elements with double quotes within the `peoples` array.

### Formatting example with ESLint

Using the same code as above, the `npx eslint "Your file name --fix"` command will quickly format to this:

```javascript
const numbers = [2,3,8,9,7]

let peoples = ['kamal','lawal','shola','olaide']

```

You can also change the configuration of the tool, by changing the elements of the `peoples` array so they're inside double quotes:

```javascript
const numbers = [2,3,8,9,7]

let peoples = ["kamal","lawal","shola","olaide"];

```

You can do this by going to the .eslintrc file and manipulating the rules like this:

```json
{
  "quotes": ["error", "double"],
  "semi": ["off", "always"]
}

```

### Formatting example with JS Beautifier

Here's the result from JS Beautifier for the same code:

```javascript
const numbers = [2, 3, 8, 9, 7]
let peoples = ['kamal', 'lawal', "shola", "olaide"];

```

You can configure it more from your JSON file if you wish.

Now you've seen these formatters in action!

## Conclusion

In this guide, we talked about some alternatives to using Prettier. We discussed Jsfmt, ESlint, StandardJS, and JS Beautifier, as well as their features, pros, and cons.

I hope you are now more equipped to choose the right linter/formatter for your coding projects.

