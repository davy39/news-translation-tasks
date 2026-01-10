---
title: How to set up VSCode to improve your productivity
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-22T17:03:20.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-vscode-to-improve-your-productivity-fb14c81d4991
coverImage: https://cdn-media-1.freecodecamp.org/images/1*cgkkTflpK9s3jL1yb1Jygw.png
tags:
- name: Productivity
  slug: productivity
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Chiamaka Ikeanyi

  Code editors have evolved over the years. A few years ago, there was no Visual Studio
  Code (VS Code). You were probably using Sublime Text, Atom, Bracket, etc. But with
  the release of VS Code, it has become the favourite code edit...'
---

By Chiamaka Ikeanyi

Code editors have evolved over the years. A few years ago, there was no Visual Studio Code (VS Code). You were probably using Sublime Text, Atom, Bracket, etc. But with the release of VS Code, it has become the favourite code editor of most developers.

### Why VS Code?

Developers love it because

* It’s customizable
* Easy Debugging
* Emmet
* Extensions
* Git Integration
* Integrated terminal
* Intellisense
* Theming and more…

Now that you’ve seen the advantages of using VS Code, this article will cover VS Code setup and extensions needed when using VS Code for maximum productivity.

### Terminal

You can [set up your terminal](https://chiamakaikeanyi.dev/how-to-configure-your-macos-terminal-with-zsh-like-a-pro/) to use iTerm2 and ZSh and have your VS Code terminal setup to use that.

After configuring Zsh, launch the VS Code integrated terminal `Terminal > New Termi`naland run the command

```
source ~/.zshrc
```

or

```
. ~/.zshrc
```

to execute the content of the .zshrc configuration file in the shell.

### Font

[FiraCode](https://github.com/tonsky/FiraCode) looks cool because of the support for ligatures. Download and install FiraCode, then add it to your `settings.json` file.

![Image](https://cdn-media-1.freecodecamp.org/images/vqdv5dokMCcD5yivbaPUBTtYsWBiUIMo6gZ6)

```
"editor.fontFamily": "Fira Code","editor.fontLigatures": true,
```

### Launching from the command line

Launching VS Code from the terminal looks cool. To do this, press CMD + SHIFT + P, type **shell command** and select **Install code command in path**. Afterwards, navigate to any project from the terminal and type `**code .**`from the directory to launch the project using VS Code.

### Configuration

VS Code configurations not specific to a workspace are housed within the settings.json. You can configure VS Code to suit your preferences.

To launch the settings.json, press

```
CMD + ,
```

Copy and paste the code below within the settings.json file:

```
{    "editor.multiCursorModifier": "ctrlCmd",    "editor.formatOnPaste": true,    "editor.wordWrap": "bounded",    "editor.trimAutoWhitespace": true,    "editor.fontFamily": "Fira Code",    "editor.fontLigatures": true,    "editor.fontSize": 14,    "editor.formatOnSave": true,    "files.autoSave": "onFocusChange",    "emmet.syntaxProfiles": {        "javascript": "jsx"    },    "eslint.autoFixOnSave": true,    "eslint.validate": [        "javascript",        "javascriptreact"    ],    "javascript.validate.enable": true,    "git.enableSmartCommit": true,    "files.trimTrailingWhitespace": true,    "editor.tabSize": 2,    "gitlens.historyExplorer.enabled": true,    "diffEditor.ignoreTrimWhitespace": false,    "workbench.sideBar.location": "right",    "explorer.confirmDelete": false,    "javascript.updateImportsOnFileMove.enabled": "always",}
```

### Extensions

Below are useful extensions that can improve your developer experience when working on a codebase.

To access these extensions,

* Go to `View -> Extensi`ons
* Search for extensions in the marketplace
* Click on Install

#### 1. Auto Import

With this extension, you don’t need to manually import files. If you are working on a component-based project, just go ahead and type the component name and it will be automatically imported.

![Image](https://cdn-media-1.freecodecamp.org/images/d88RTDvyIzGWYC5BuLcnIaFOjHiyDMaqE5Bh)

#### 2. Add jsdoc comments

This adds a comments block to the code. To use it, highlight the first line of the function, press `CMD + SHIFT + P` and select **_Add Doc Comments._**

![Image](https://cdn-media-1.freecodecamp.org/images/jlJk05MHt3HknnqZyKQB-8d1Oj7qgh7ZOBGL)

#### 3. ESDoc MDN

In certain scenarios, we tend to forget how a particular thing works. This is where this extension becomes useful. You don’t need to launch your web browser to find out the syntax. All you need is to type

```
//mdn [object].[method];
```

![Image](https://cdn-media-1.freecodecamp.org/images/r8pUHOgNQwAyNq0DU9VPcL5xb8zGgT1ybCZV)

#### 4. CSS Peek

As the name implies, this helps you peek on rules applied by a defined style within a codebase and its [specificity](https://chiamakaikeanyi.dev/css-specificity). It comes in handy when working on legacy codebases.

![Image](https://cdn-media-1.freecodecamp.org/images/7orGFqwr8mdQPOVPuQVMTlRO8XtPgnR0Ggmj)

#### 5. GitLens

GitLens boosts what you can achieve with Git. It helps you to do a lot more, such as seamlessly exploring Git repositories, peeking into code revisions, authorship and much more.

![Image](https://cdn-media-1.freecodecamp.org/images/Sf2hWdpXSF7CPBhmQ9sTf9zGPD-OiXQsf2aM)

#### 6. ESLint

This integrates ESLint into VS Code to lint your codes. The project you are working on needs to have ESLint installed either locally or globally to take advantage of the features this extension offers.

To install ESLint locally, run

```
npm install eslint
```

or globally using

```
npm install -g eslint
```

You would also need to create `.eslintrc` configuration file. If you installed ESLint locally, run

```
./node_modules/.bin/eslint --init
```

or

```
eslint --init
```

for global installation.

#### 7. Debugger for Chrome

This lets you debug your JavaScript code right from the Google Chrome browser

![Image](https://cdn-media-1.freecodecamp.org/images/O4SSLTXtEEdU3AjZODIdUKG7AYao27y6O7jq)

#### 8. Google Fonts

Adding Google fonts just got easier with this extension. You no longer need to search for fonts in the browser. To access a list of fonts, press`CMD + SHIFT + P` and search for **_Google fonts_** to proceed.

![Image](https://cdn-media-1.freecodecamp.org/images/sqVCRBo5mlEUjIFcSsp28oEo4ugo3LMXjKoS)

#### 9. TODO Highlight

With a lot to work on which needs to be prioritized, sometimes you may tend to forget tasks yet to be completed. TODO highlight makes these easily seen by highlighting them.

#### 10. Docker

You can create Dockerfiles on the fly with this extension. It also provides syntax highlighting, intellisense and much more.

Press CMD + SHIFT + P and search for _Add Docker files to workspace._

![Image](https://cdn-media-1.freecodecamp.org/images/Yv09L4W8lraVLXLr-aYpCHz8hfLC-tuORELa)

#### 11. Code Spellchecker

This comes in handy to identify typographical errors within the codebase.

#### 12. Import Cost

Import Cost shows the impact of imported packages within the code. It helps measure performance bottlenecks.

![Image](https://cdn-media-1.freecodecamp.org/images/4Xl2OdUzPmPFW54eqzrHz59Kg9qSFbCDxUWf)

#### 13. HTMLHint

This extension validates your HTML helping you to write [standards-compliant code](https://chiamakaikeanyi.dev/writing-standards-compliant-html/).

![Image](https://cdn-media-1.freecodecamp.org/images/ZJN4LadCSa6e1EVHlEMs7gB1f4AVINChBxaY)

#### **14. Peacock**

This extension gives you the ability to change the colour of your workspace. It is ideal when you have multiple VS Code instances and you want to quickly identify a particular instance.

![Image](https://cdn-media-1.freecodecamp.org/images/BRiUh7NQh1PdVW7aP5mZJcnbzZFaCQcblYpq)

After installing Peacock, click on the settings icon > settings, select workspace settings tab, click on {} and paste the code below.

```
{    "workbench.colorCustomizations": {        "activityBar.background": "#e90b8d",        "activityBar.foreground": "#fff",        "activityBar.inactiveForeground": "#b5b5b5",    },    "peacock.affectedElements": [        "activityBar",    ]}
```

You can also add `titleBar` and `statusBar` to the affectedElements and add color customizations for them within the colorCustomizations section.

To use one of the default colors, press CMD + SHIFT + P, type **peacock** and select your preferred theme. This overrides the color settings within the settings.json file defined for that workspace.

#### **15. Prettier**

Do you always press the spacebar or tab key when coding? Here comes Prettier to the rescue. It formats lines of code and makes it readable.

Check out [the awesome things you can do with Visual Studio Code](https://vscodecandothat.com/) here.

Feel free to drop what works for you in the comment section and share this article.

Also, check out [my blog](https://chiamakaikeanyi.dev) for more articles.

