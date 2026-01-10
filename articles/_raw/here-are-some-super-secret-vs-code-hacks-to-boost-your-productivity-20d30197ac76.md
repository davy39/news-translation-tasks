---
title: Here are some super secret VS Code hacks to boost your productivity
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-08T22:17:21.000Z'
originalURL: https://freecodecamp.org/news/here-are-some-super-secret-vs-code-hacks-to-boost-your-productivity-20d30197ac76
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Cda3VjoZXXl2KjDWhL-a-g.jpeg
tags:
- name: coding
  slug: coding
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Dylan Tientcheu

  Coding as a hobbyist, professional or even a once-in-a-month developer, you must
  know that having smart and sharp tools is vital to anyone willing to put in maximum
  productive hours while working.

  I’ve curated a little collection o...'
---

By Dylan Tientcheu

Coding as a hobbyist, professional or even a once-in-a-month developer, you must know that having smart and sharp tools is vital to anyone willing to put in maximum productive hours while working.

I’ve curated a little collection of tips, tricks and extensions, and filtered them to keep only both the most rare and most useful ones to a modern web developer. As we know the JavaScript ecosystem is very big and still growing bigger. For this reason, I’ll try to be unbiased as much as possible.

The following Visual Studio Code tips will help you walk out of all your coding sessions looking like this:

### Making it beautiful and friendly

> If it really looks good and friendly, you’ll love the time spent with it.

#### [1. Material Theme](https://marketplace.visualstudio.com/items?itemName=Equinusocio.vsc-material-theme) & [Icons](https://marketplace.visualstudio.com/items?itemName=PKief.material-icon-theme)

This is straight up the beast in VS Code themes. I think the material theme is the closest thing to writing with a pen and a paper within the editor (especially when using the **no contrast variant** theme). Your editor almost looks flat and seamless, going from the integrated tools to the text editor.

Imagine an epic theme coupled with epic icons. [**Material Theme Icons**](https://marketplace.visualstudio.com/items?itemName=PKief.material-icon-theme) are just an awesome alternative to replace the default VSCode icons. The big catalog of icons designed integrates smoothly with the theme making it more beautiful. This will help you find your files easily in the explorer.

![Image](https://cdn-media-1.freecodecamp.org/images/0*k5PE7vEkF_9KA7oS.jpg)
_[https://marketplace.visualstudio.com/items?itemName=Equinusocio.vsc-material-theme](https://marketplace.visualstudio.com/items?itemName=Equinusocio.vsc-material-theme" rel="noopener" target="_blank" title=")_

#### 2. Zen Mode with Centered Layout

You may already know the Zen Mode View, also known as Distraction Free View (for those coming from Sublime Text) where everything (except code) is removed to give you real intimacy with your code editor. Did you know you could center the layout to help you read your code as if you were in a PDF viewer? This will really help you focus on a function or study someone else’s code.

**Zen Mode**: _[View > Appearance > Toggle Zen_ Mode]

**Center Layout:** _[View > Appearance > Toggle Centered L_ayout]

![Image](https://cdn-media-1.freecodecamp.org/images/1*rOEqs2r32WNvXKRDRNw9qQ.gif)

#### **3. Fonts With Ligatures**

Writing style makes reading easy and convenient. You can make your editor look better with awesome fonts along with [ligatures](https://en.wikipedia.org/wiki/Typographic_ligature). Here are [6 of the best fonts that support ligatures](https://www.slant.co/topics/5611/~monospace-programming-fonts-with-ligatures) (according to [www.slant.co](http://www.slant.co/))

![Image](https://cdn-media-1.freecodecamp.org/images/1*marIy0tF9nshab3_ugN6VA.gif)
_Coding with Ligatures_

You can try [Fira Code](https://github.com/tonsky/FiraCode), it’s just awesome and open source. This is how you change font in VSCode after installing it.

```
"editor.fontFamily": "Fira Code","editor.fontLigatures": true
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*0qjQY2qb5rJVPRILebhkxg.png)
_Source: [https://github.com/tonsky/FiraCode/blob/master/showcases/all_ligatures.png](https://github.com/tonsky/FiraCode/blob/master/showcases/all_ligatures.png" rel="noopener" target="_blank" title=")_

_The well renowned font Operator Mono does not come with native support for ligatures. However, if you are a big fan of ligatures, you can add them using [this library](https://github.com/kiliman/operator-mono-lig)._

#### 4. [Rainbow Indent](https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow)

Indent with style. This extension colorizes the indentation in front of your text alternating four different colors on each step.

![Image](https://cdn-media-1.freecodecamp.org/images/1*dSKbn4xbVxEGPdIrnyApjA.png)
_**Rainbow Indent: [https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow](https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow" rel="noopener" target="_blank" title=""></a>**<a href="https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow" rel="noopener" target="_blank" title=")_

The default indentation setting colors the indentation following a rainbow scheme. I however customized my own to follow different shades of grey. If you wish yours to look like this example, copy and paste the following snippet in your `settings.json`

```
"indentRainbow.colors": [
```

```
"rgba(16,16,16,0.1)",
```

```
"rgba(16,16,16,0.2)",
```

```
"rgba(16,16,16,0.3)",
```

```
"rgba(16,16,16,0.4)",
```

```
"rgba(16,16,16,0.5)",
```

```
"rgba(16,16,16,0.6)",
```

```
"rgba(16,16,16,0.7)",
```

```
"rgba(16,16,16,0.8)",
```

```
"rgba(16,16,16,0.9)",
```

```
"rgba(16,16,16,1.0)"
```

```
],
```

#### 5. Title Bar Customization

This is a great visual tweak. I copied it from [Wes Bos](https://www.freecodecamp.org/news/here-are-some-super-secret-vs-code-hacks-to-boost-your-productivity-20d30197ac76/undefined) in one of his [React & GraphQL l](https://advancedreact.com/)essons. Basically he switched the title bar colors on different projects to recognize them easily and help the audience distinguish between them too. This is really useful if you work on apps that may have the same code or file names, for example, a react-native mobile app and a react web app.

![Image](https://cdn-media-1.freecodecamp.org/images/1*cG_nfe-R1aHDk-e_whFP7w.png)

This is done by editing Title Bar settings in the **Workspace Settings** for each project in which you want different title bar colors.

### Faster Coding

> _The very essence of getting it done in time_

#### 1. Tag Wrapping

If you do not know [Emmet](https://emmet.io/), then you are probably someone that likes typing it all. Emmet enables you to type an abbreviated code and get the returned corresponding tags. This is done by selecting a bunch of code and typing the command **Wrap with Abbreviated** which I keybinded to `shift+alt+.`

Watch it below.

![Image](https://cdn-media-1.freecodecamp.org/images/1*27AU7hj5uEkYaPofK_BAUQ.gif)
_Wrap it up with Emmet_

Imagine you want to wrap all of these but as individual lines. You’d use **_wrap with individual lines_** then insert * after the abbreviation e.g `div*`

In case you want to jump right into Emmeting, this is the [Emmet Cheatsheet](https://docs.emmet.io/cheat-sheet/)

#### 2. Balance Inwards and Outwards

This tip was taken from [https://vscodecandothat.com/](https://vscodecandothat.com/) which I really recommend.

You can select a whole tag in VS Code by using the `balance inward` and `balance outward` Emmet commands. It's helpful to bind these commands to keyboard shortcuts, like `Ctrl + Shift + Up Arrow` for Balance Outward and `Ctrl + Shift + Down Arrow` for Balance Inward.

![Image](https://cdn-media-1.freecodecamp.org/images/1*WdH9CosNx91ggCI9u246cA.gif)
_Balance Inwards/Outwards_

#### 3. [Turbo Console.log()](https://marketplace.visualstudio.com/items?itemName=ChakrounAnas.turbo-console-log)

No one likes typing very long statements like console.log(). It can be really irritating, mostly when you just want to output something really fast, view its value, then continue coding. What if I told you you could console log anything as fast as Lucky Luke?

This is done with an extension called [Turbo Console Log](https://marketplace.visualstudio.com/items?itemName=ChakrounAnas.turbo-console-log)**.** It enables the logging of any variable on the line below with an automatic prefixing following the code structure. You are also able to uncomment/comment `alt+shift+u/ alt+shift+c` all the console.log() added by this extension.

Moreover, you can also delete all of them with `alt+shift+d`:

![Image](https://cdn-media-1.freecodecamp.org/images/1*C7BQj-qOFfkuvWC4Cg94bQ.gif)
_Console logging like Lucky Luke_

#### 4. [Live server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)

This is an awesome extension that helps you launch a local development server with live reload feature for static and dynamic pages. It has a great support for major features like: HTTPS, CORS, custom localhost addresses and port.

[Download it here](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)

![Image](https://cdn-media-1.freecodecamp.org/images/1*CfYU3dAoc-39eAJf2hgb3A.gif)
_Source ([https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer" rel="noopener" target="_blank" title="))_

It can even enable you to share your localhost, if used with [VSCode LiveShare](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare).

#### 5. Copy/Paste with Multiple Cursors

One of the first _“Wows”_ I screamed when using VS Code happened when I edited multiple lines by adding cursors on different lines. Long after, I found a very good use to this feature. You are able to copy and paste the content selected by those cursors and they’ll be pasted exactly in the order in which they were copied.

Check out below.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NPW3X6Z5eugYHUp1AQ3-aw.gif)
_Copy and Paste with different cursors_

#### 6. Breadcrumbs and Outlines

The Breadcrumb shows the current location and allows you to quickly navigate between symbols and files. To start using breadcrumbs, enable it with the View > Toggle Breadcrumbs command or via t`he breadcrumbs.enab`led setting.

The Outline View is a separate section at the bottom of the File Explorer Tree. When expanded, it will show the symbol tree of the currently active editor.

The Outline view has different Sort by modes, optional cursor tracking. It also includes an input box which filters symbols as you type. Errors and warnings are also shown in the Outline view, letting you see at a glance a problem’s location.

![Image](https://cdn-media-1.freecodecamp.org/images/1*BPo_JXR94vivyMJLyI0TiQ.gif)
_Breadcrumb and Outline Relation_

### Miscellaneous

> _Those little tweaks that change everything_

#### 1. Code CLI

VS Code has a powerful command line interface that lets you control how you launch the editor. You can open files, install extensions, change the display language, and output diagnostics through command line options (switches).

![Image](https://cdn-media-1.freecodecamp.org/images/1*KhG5u8EYn-aMlqwomhZq_w.png)

Imagine you’ve just `git clone <repo-u`rl> a repository and you want to replace the current instance of VS Code you are u`sing. cod`e . -r will do the trick without you having to leave the CLI inter[face (Learn mor](https://code.visualstudio.com/docs/editor/command-line)e here).

#### 2. [Polacode](https://github.com/octref/polacode)

You often come upon appealing code screenshots with custom fonts and themes like the one below. This was taken in VS Code with [Polacode Extension](https://github.com/octref/polacode)

![Image](https://cdn-media-1.freecodecamp.org/images/1*AF2kH-Hc5cR_RdSpfKFrlg.png)

I know [Carbon](https://carbon.now.sh/) is also a good and more customizable alternative. However, Polacode enables you stay in your code editor and use any proprietary font you may have bought which is unusable in Carbon.

#### 3. [Quokka (JS/TS ScratchPad)](https://quokkajs.com/)

Quokka is a rapid prototyping playground for JavaScript and TypeScript. It runs your code immediately as you type and displays various execution results and console logs in your code editor.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Es15d1InicXO5JxBmVAskA.gif)

An awesome use case for Quokka is when you are studying for technical interviews, you are able to output each step without having the stress of setting breakpoints in debuggers.

It can also help you study a library’s functions like Lodash or MomentJS before actually using them. It even works for Async calls.

#### 5. [WakaTime](https://wakatime.com/)

Do your friends think you spend too much time coding? Record it and show them that 10hrs/day is not “too much”. [WakaTime](https://wakatime.com/) is an extension that helps to record and store metrics and analytics regarding your programming activity.

You can set goals, view coding languages you often use, you can even compare yourself to other ninjas in the world.

![Image](https://cdn-media-1.freecodecamp.org/images/1*bvNk2yHjrObBPeBP6otd5w.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*_GHqrHKRWUEmf33nIdzEVg.png)
_WakaTime Dashboard and Leaderboards_

#### 6. [VSCode Hacker Typer](https://marketplace.visualstudio.com/items?itemName=jevakallio.vscode-hacker-typer)

Have you ever been typing code in front of a crowd? You often type recklessly and talk while typing which confuses you a little bit. Imagine a pre-typed code that only comes up when you simulate typing like in [geektyper](http://geektyper.com/tegnio/).

[Jani Eväkallio](https://www.freecodecamp.org/news/here-are-some-super-secret-vs-code-hacks-to-boost-your-productivity-20d30197ac76/undefined) brought to VS Code [**this extension**](https://marketplace.visualstudio.com/items?itemName=jevakallio.vscode-hacker-typer). It will help you record and replay macros (code written in your editor) making you 100% more focused when typing to an audience.

#### 7. Exclude folders

I learned this trick [on a StackOverFlow post](https://stackoverflow.com/questions/33258543/how-can-i-exclude-a-directory-from-visual-studio-code-explore-tab/33277809#33277809).This one is a quick tweak for excluding folders like node_modules or any other from the explorer tree to help you focus only on what matters. As for me, I really hate opening the tedious node_module folder in my editor, so I decided to hide it.

For example to hide node_modules you can do this:

1. Go to **File > Preferences > Se**ttings (or o**n Mac Code > Preferences &**gt; Settings)
2. Search `files.exclude` in the settings
3. Select add pattern and type `**/node_modules`
4. Voila! node_modules disappeared from the explorer tree

#### 8. [Your Suggestions]

You can always comment some of your most secret tips on VSCode, I’ll be glad to append them to the list to help others. :)

I hope these tips will really boost your productivity with VS Code. Please clap and share the post if you liked it and comment if I missed any extension.

[**Dylan Tientcheu (@DylanTientcheu) | Twitter**](http://twitter.com/dylantientcheu)  
[_Dylan Tientcheu(@DylanTientcheu). Javascript 熱狂者 * #Developer & #Designer * Technical Writer *…_twitter.com](http://twitter.com/dylantientcheu)

