---
title: How to Jazz Up Your Bash Terminal — A Step By Step Guide With Pictures
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-02T17:41:49.000Z'
originalURL: https://freecodecamp.org/news/jazz-up-your-bash-terminal-a-step-by-step-guide-with-pictures-80267554cb22
coverImage: https://cdn-media-1.freecodecamp.org/images/1*QRJ9_60oCmcwRGfYqCbqSw.png
tags:
- name: Bash
  slug: bash
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
seo_title: null
seo_desc: 'By rajaraodv

  In this blog I’ll go over the steps to add Themes, Powerline, fonts, and powerline-gitstatus
  to make your regular Bash Terminal look beautiful and useful as shown in the picture
  above.

  It turns out, if you are using Mac, you’ll need to j...'
---

By rajaraodv

In this blog I’ll go over the steps to add Themes, Powerline, fonts, and powerline-gitstatus to make your regular Bash Terminal look beautiful and useful as shown in the picture above.

It turns out, if you are using Mac, you’ll need to jump through a lot of hoops to get this working as many instructions are for linux, or are out of date. So I thought I'd blog about it - hopefully it'll help you.

> Notes:  
>   
> 1. Follow the steps carefully as any mistake will cause a lot of headaches.  
>   
> 2. This is for MacOS and for regular bash in the Terminal.app. I’m not using ZSH or Hyper in this blog — I plan to write different blogs for them.  
>   
> 3. My Versions: Mac High Sierra; git version 2.14.3 (Apple Git-98); Python 2.7.10

OK, by default, when you have a new mac, your Terminal.app will look something like below. Let’s go ahead and add Themes, fonts, and so on.

![Image](https://cdn-media-1.freecodecamp.org/images/1*A2RjRAGXHeUQtIIy5XIBwQ.png)

### Step 1 — Add A New Theme

The first obvious step is to enhance the Theme. Terminal doesn’t provide all the cool and fancy themes that you see other developers use. Let’s download a Theme and add it to the Terminal.

In this blog, I’ll add Solarized-Dark theme to our Terminal.

> Note: You can download various Themes (.terminal files) from [this git repo](https://github.com/lysyi3m/osx-terminal-themes/tree/master/schemes). Simply open the `_*.terminal_` file to install it, i.e. `_right-click on the *.terminal file > “open with" > Te_`rminal

1. Go to [http://ethanschoonover.com/solarized](http://ethanschoonover.com/solarized)
2. Scroll down and download the Theme (solarized.zip)
3. Extract the solarized.zip file
4. Open the **osx-terminal.app-colors-solarized** folder. This folder contains Theme for the terminal.
5. Double click **_“Solarized Dark ansi.terminal”_** file **—** This is the specific Theme file for Terminal.app. _Note: If you get a warning that this is from an unidentified developer, Right-click on the file and select “Open with” > Terminal opti_on.
6. At this point, you have the Theme installed into your Terminal. We just need to make it a default Theme.
7. Open Terminal > Preferences > Text and select the “Solarized Dark …” theme and click on “Default”.

![Image](https://cdn-media-1.freecodecamp.org/images/1*0hPqERUbwhdAXVQfdQih1A.png)

From now on, your Terminal should like below.

![Image](https://cdn-media-1.freecodecamp.org/images/1*hvkwX_GZIXHQxuYY2987GQ.png)

### Step 2 — Install Powerline

Powerline is a Python app and is a status line plugin for vim, and provides status lines and prompts for several other applications, including zsh, bash, tmux, IPython, Awesome and Qtile.

It makes the Terminal prompt look like below.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7SLVI9-_IBwEcmZpGaDvmw.png)

#### 2.1 Install Python

Because Powerline is a Python app, we need to have Python and that too a proper version of Python.

* MacOS comes with Python installed already. **Ensure Python’s version is 2.7.x by typing** `python -V` in the Terminal.
* If it’s not 2.7, install [Homebrew](https://brew.sh/) that allows us to install various software from the CLI, by running:`/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
* Run `brew install python` to install the latest Python via Homebrew

#### 2.2 Install pip — A package manager for Python (similar to npm)

Install pip by running the following command

`$ sudo easy_install pip`

#### 2.3 Install XCode Developer CLI tools

XCode Developer CLI tools are used by Powerline and other apps that manipulate core OSX features. So make sure to install the XCode CLI tools by running the following command.

`$ xcode-select —-install`

> Note: The above command opens up Mac’s installer and installs the XCode Developer CLI tools. If it doesn’t work, try `_xcode-select -r_` to reset.

#### 2.4 Install Powerline

Finally, install the Powerline (stable version) via pip by running the following command.

```bash
$ pip install --user powerline-status
```

If you want to install the latest development branch, then use:

```bash
$ pip install --user git+git://github.com/powerline/powerline  //dev
```

#### 2.5 Add the Powerline daemon to bash

We now need to add the Powerline daemon to bash so that it can monitor the Terminal prompt and make changes.

**2.5.1 Copy the Powerline’s installation location**

You can figure out the location of Powerline by running the following: `pip show powerline-status` Copy the value from the `Location` field.

![Image](https://cdn-media-1.freecodecamp.org/images/1*1Hi5bB475XFf-Iu43tAFvA.png)

**2.5.2 Add the daemon with a proper location to .bash_profile**

1. Make sure you have `.bash_profile` file in your root directory. If not following create one by doing: `cd ~ && touch ~/.bash_profile`

2. Open `.bash_profile` and add the following:

```bash
export PATH=$PATH:$HOME/Library/Python/2.7/bin
powerline-daemon -q
POWERLINE_BASH_CONTINUATION=1
POWERLINE_BASH_SELECT=1
. /Users/rupa/Library/Python/2.7/lib/python/site-packages/powerline/bindings/bash/powerline.sh
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*QY-1dEQtAn6SUOpgOTQcsg.png)
_Some details about bash_profile_

> _Note: The location /Users/rupa/Library/Python/2.7/lib/python/site-packages/ is from the previous step (2.5.1). Change it to match your computer’s location._

**2.5.3. Restart the Terminal**

Completely quit the Terminal if it’s open (Terminal > Quit Terminal). And open it again.

> You should be able to simply use `_$ source ~/.bash_profile_` to update the settings. But I got some odd `_powerline-config_` file is missing! Typically you get this error if you don’t have $HOME/Library/Python/2.7/bin in your PATH.

**2.5.4 Your new Terminal**

Your new Terminal should look like below. It should be using “Solarized Dark ansi” theme and should show Powerline in the command prompt. But also notice that there are “?” characters! This is because Powerline uses various icons and fonts that are not available by default. So we need to install the fonts.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fVqgdIqo7AIw7EJdcHZZxw.png)

### Step 3 — Install Powerline fonts

To install Powerline fonts, simply go to [https://github.com/powerline/fonts](https://github.com/powerline/fonts). There you’ll see a whole bunch of folders. Each one is a font, aka “Patched fonts”.

> It is called “Patched fonts” because people have taken regular fonts and have added/patched additional Powerline specific icons and fonts to them.

![Image](https://cdn-media-1.freecodecamp.org/images/1*sYBQZYzxe37bkmtBUw_Oww.png)

#### 3.1 Download the whole repo and unzip it

* Click on the “Clone or download” button and download the whole repo so you try various fonts.
* Unzip the fonts-master.zip

#### 3.2 Install some fonts

Let’s open **Meslo dotted** fonts folder. It will look like below. You’ll see a whole bunch of .ttf file. Each one of them is a font but some are “bold” version of the font, some are “regular” version and so on.

Simply double-click on the .ttf file and press “Install font” to install the font on your computer.

For our case, let’s install “Meslo LG L DZ Regular for Powerline.ttf” and “Meslo LG L DZ Italic for Powerline.ttf”. This will add a **_regular_** and an **_Italic_** version of the **_Meslo_** font.

![Image](https://cdn-media-1.freecodecamp.org/images/1*zmoF1ksmDJfRH0lGK00GKg.png)

#### 3.3 Select the font in the Terminal’s Theme

Remember we added “Solarized Dark” theme in Step 1? That didn’t have any fonts in it and MacOS had some default font. All we need to do is to set our **Meslo dotted** font for this theme and we are done!

1. Open Terminal > Preferences > Text
2. Select **Solarized Dark ansi** Theme
3. Click on the “Font” button — This opens up “Fonts” dialog
4. In the “Fonts” dialog, select “Meslo LG L DZ for Powerline” in the Family and also select font size 14 (so it’s easier to read).

![Image](https://cdn-media-1.freecodecamp.org/images/1*SbKUVJxHJ_PR8yh2cbSESw.png)

#### 3.4 Restart Terminal

Completely quit the Terminal (Terminal > Quit Terminal) and then reopen it.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5pfC372U2Uz9Q5SQJSqKzA.png)

### Step 4 — Adding Git information to the prompt

In order to display various Git status at the prompt, we need to install [powerline-gitstatus](https://github.com/jaspernbrouwer/powerline-gitstatus). It is a simple add-on to Powerline and adds multiple colors and Themes to display various git status information.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NKRx9-fVCZIiWKW_Tb0lhA.png)
_PS: We will be dealing with files in the “color schemes” and “themes” folders_

#### 4.1 Install powerline-gitstatus

```bash
pip install --user powerline-gitstatus
```

> Note: “ — user” command is required to install it in the user’s profile.

#### 4.2 Add powerline-gitstatus color schemes to Powerline

4.2.1 Open the following `colorschemes/shell/default.json` folder

```bash
${powerline-install-directory}/powerline/config_files/colorschemes/shell/default.json

//For example:
/Users/rupa/Library/Python/2.7/lib/python/site-packages/powerline/config_files/colorschemes/shell/default.json
```

4.2.2 Add the following colors:

As mentioned in the powerline-gitstatus [readme](https://github.com/jaspernbrouwer/powerline-gitstatus#installation). PS: Just copy the colors inside “groups” and then append it to the default.json as shown below.

![Image](https://cdn-media-1.freecodecamp.org/images/1*shKgrO87LFrjoGMb2uOEVg.png)
_Click to zoom_

Here is my color schemes default.json (you may copy and paste this instead):

```json
{
	"name": "Default color scheme for shell prompts",
	"groups": {
		"hostname": {
			"fg": "brightyellow",
			"bg": "mediumorange",
			"attrs": []
		},
		"environment": {
			"fg": "white",
			"bg": "darkestgreen",
			"attrs": []
		},
		"mode": {
			"fg": "darkestgreen",
			"bg": "brightgreen",
			"attrs": ["bold"]
		},
		"attached_clients": {
			"fg": "white",
			"bg": "darkestgreen",
			"attrs": []
		},

		"gitstatus": {
			"fg": "gray8",
			"bg": "gray2",
			"attrs": []
		},
		"gitstatus_branch": {
			"fg": "gray8",
			"bg": "gray2",
			"attrs": []
		},
		"gitstatus_branch_clean": {
			"fg": "green",
			"bg": "gray2",
			"attrs": []
		},
		"gitstatus_branch_dirty": {
			"fg": "gray8",
			"bg": "gray2",
			"attrs": []
		},
		"gitstatus_branch_detached": {
			"fg": "mediumpurple",
			"bg": "gray2",
			"attrs": []
		},
		"gitstatus_tag": {
			"fg": "darkcyan",
			"bg": "gray2",
			"attrs": []
		},
		"gitstatus_behind": {
			"fg": "gray10",
			"bg": "gray2",
			"attrs": []
		},
		"gitstatus_ahead": {
			"fg": "gray10",
			"bg": "gray2",
			"attrs": []
		},
		"gitstatus_staged": {
			"fg": "green",
			"bg": "gray2",
			"attrs": []
		},
		"gitstatus_unmerged": {
			"fg": "brightred",
			"bg": "gray2",
			"attrs": []
		},
		"gitstatus_changed": {
			"fg": "mediumorange",
			"bg": "gray2",
			"attrs": []
		},
		"gitstatus_untracked": {
			"fg": "brightestorange",
			"bg": "gray2",
			"attrs": []
		},
		"gitstatus_stashed": {
			"fg": "darkblue",
			"bg": "gray2",
			"attrs": []
		},
		"gitstatus:divider": {
			"fg": "gray8",
			"bg": "gray2",
			"attrs": []
		}
	},
	"mode_translations": {
		"vicmd": {
			"groups": {
				"mode": {
					"fg": "darkestcyan",
					"bg": "white",
					"attrs": ["bold"]
				}
			}
		}
	}
}
```

#### 4.3 Activate The Theme

4.3.1 Open Theme’s default.json file

```bash
${powerline-install-directory}/powerline/config_files/themes/shell/default.json

//For example:
/Users/rupa/Library/Python/2.7/lib/python/site-packages/powerline/config_files/themes/shell/default.json
```

4.3.2 Add the following to the default.json

```json
{
    "function": "powerline_gitstatus.gitstatus",
    "priority": 40
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*QJIvX5hfNpUWZgoHTQ_nbQ.png)

Below is my Powerline’s Theme default.json(you may copy and paste this instead):

> Note: I have removed everything from the “right” section and also removed “job number” (“jobnum”) to keep things clean. Otherwise, you’ll see a little artifact on the right-hand side edge of the prompt.

```json
{
	"segments": {
		"left": [{
				"function": "powerline.segments.shell.mode"
			},
			{
				"function": "powerline.segments.common.net.hostname",
				"priority": 10
			},
			{
				"function": "powerline.segments.common.env.user",
				"priority": 30
			},
			{
				"function": "powerline.segments.shell.cwd",
				"priority": 10
			}, {
				"function": "powerline_gitstatus.gitstatus",
				"priority": 40
			}
		],
		"right": []
	}
}
```

#### 4.4 Restart the Daemon

Save the file and run the following: `_powerline-daemon —-replace_` _in the Terminal._

> **Important Note:** Every time you make changes to Powerline’s config, in addition to restarting the Terminal, you’ll also need to **restart** **the daemon to see the changes reflected** by running: `_powerline-daemon —-replace_`.

#### 4.5 Restart The Terminal

Quit the Terminal (Terminal > Quit Terminal) and open it again.

At this point, we are all done! whew! If you open the Terminal, and navigate to any git repo, and play around, it should look like the following.

![Image](https://cdn-media-1.freecodecamp.org/images/1*QRJ9_60oCmcwRGfYqCbqSw.png)

Here is how it looks in Solarized-Light Theme:

![Image](https://cdn-media-1.freecodecamp.org/images/1*8yii2h-RBMX3j5dtMagr2Q.png)

Here is how it looks in [Cobalt2 Theme](https://raw.githubusercontent.com/lysyi3m/osx-terminal-themes/master/schemes/Cobalt2.terminal):

![Image](https://cdn-media-1.freecodecamp.org/images/1*hYHwy__bxYoA8cji8E3plQ.png)

?? Thank you!

If you have questions, please feel free to ask me on Twitter: [https://twitter.com/rajaraodv](https://twitter.com/rajaraodv)

#### If this was useful, please click the clap ? button down below a few times to show your support! ⬇⬇⬇ ??

### My Other Posts

[_https://medium.com/@rajaraodv/latest_](https://medium.com/@rajaraodv/latest)

#### ECMAScript 2015+

1. _[Check out these useful ECMAScript 2015 (ES6) tips and tricks](https://www.freecodecamp.org/news/check-out-these-useful-ecmascript-2015-es6-tips-and-tricks-6db105590377/)_
2. [_5 JavaScript “Bad” Parts That Are Fixed In ES6_](https://medium.com/@rajaraodv/5-javascript-bad-parts-that-are-fixed-in-es6-c7c45d44fd81#.7e2s6cghy)
3. [_Is “Class” In ES6 The New “Bad” Part?_](https://medium.com/@rajaraodv/is-class-in-es6-the-new-bad-part-6c4e6fe1ee65#.4hqgpj2uv)

#### Terminal Improvements

1. _[How to Jazz Up Your Terminal — A Step By Step Guide With Pictures](https://www.freecodecamp.org/news/jazz-up-your-bash-terminal-a-step-by-step-guide-with-pictures-80267554cb22/)_
2. _[Jazz Up Your “ZSH” Terminal In Seven Steps — A Visual Guide](https://www.freecodecamp.org/news/jazz-up-your-zsh-terminal-in-seven-steps-a-visual-guide-e81a8fd59a38/)_

#### WWW

1. _[A Fascinating And Messy History Of The Web And JavaScript](https://www.freecodecamp.org/news/a-fascinating-and-messy-history-of-the-web-and-javascript-video-8978dc7bda75/)_

#### Virtual DOM

1. [_Inner Workings Of The Virtual DOM_](https://medium.com/@rajaraodv/the-inner-workings-of-virtual-dom-666ee7ad47cf)

#### React Performance

1. [_Two Quick Ways To Reduce React App’s Size In Production_](https://medium.com/@rajaraodv/two-quick-ways-to-reduce-react-apps-size-in-production-82226605771a#.6lepbl7ae)
2. [_Using Preact Instead Of React_](https://medium.com/@rajaraodv/using-preact-instead-of-react-70f40f53107c#.7fzp0lyo3)

#### Functional Programming

1. [_JavaScript Is Turing Complete — Explained_](https://medium.com/@rajaraodv/javascript-is-turing-complete-explained-41a34287d263#.6t0b2w66p)
2. [_Functional Programming In JS — With Practical Examples (Part 1)_](https://medium.com/@rajaraodv/functional-programming-in-js-with-practical-examples-part-1-87c2b0dbc276#.fbgrmoa7g)
3. _[Functional Programming In JS — With Practical Examples (Part 2)](https://www.freecodecamp.org/news/functional-programming-in-js-with-practical-examples-part-2-429d2e8ccc9e/)_
4. [_Why Redux Need Reducers To Be “Pure Functions”_](https://medium.com/@rajaraodv/why-redux-needs-reducers-to-be-pure-functions-d438c58ae468#.bntrywxrf)

#### WebPack

1. [_Webpack — The Confusing Parts_](https://medium.com/@rajaraodv/webpack-the-confusing-parts-58712f8fcad9#.6ot6deo2b)
2. [_Webpack & Hot Module Replacement [HMR]_](https://medium.com/@rajaraodv/webpack-hot-module-replacement-hmr-e756a726a07#.y667mx4lg) _(under-the-hood)_
3. [_Webpack’s HMR And React-Hot-Loader — The Missing Manual_](https://medium.com/@rajaraodv/webpacks-hmr-react-hot-loader-the-missing-manual-232336dc0d96#.fbb1e7ehl)

#### Draft.js

1. [_Why Draft.js And Why You Should Contribute_](https://medium.com/@rajaraodv/why-draft-js-and-why-you-should-contribute-460c4a69e6c8#.jp1tsvsqc)
2. [_How Draft.js Represents Rich Text Data_](https://medium.com/@rajaraodv/how-draft-js-represents-rich-text-data-eeabb5f25cf2#.hh0ue85lo)

#### React And Redux :

1. [_Step by Step Guide To Building React Redux Apps_](https://medium.com/@rajaraodv/step-by-step-guide-to-building-react-redux-apps-using-mocks-48ca0f47f9a#.s7zsgq3u1)
2. [_A Guide For Building A React Redux CRUD App_](https://medium.com/@rajaraodv/a-guide-for-building-a-react-redux-crud-app-7fe0b8943d0f#.g99gruhdz) _(3-page app)_
3. [_Using Middlewares In React Redux Apps_](https://medium.com/@rajaraodv/using-middlewares-in-react-redux-apps-f7c9652610c6#.oentrjqpj)
4. [_Adding A Robust Form Validation To React Redux Apps_](https://medium.com/@rajaraodv/adding-a-robust-form-validation-to-react-redux-apps-616ca240c124#.jq013tkr1)
5. [_Securing React Redux Apps With JWT Tokens_](https://medium.com/@rajaraodv/securing-react-redux-apps-with-jwt-tokens-fcfe81356ea0#.xci6o9s6w)
6. [_Handling Transactional Emails In React Redux Apps_](https://medium.com/@rajaraodv/handling-transactional-emails-in-react-redux-apps-8b1134748f76#.a24nenmnt)
7. [_The Anatomy Of A React Redux App_](https://medium.com/@rajaraodv/the-anatomy-of-a-react-redux-app-759282368c5a#.7wwjs8eqo)
8. [_Why Redux Need Reducers To Be “Pure Functions”_](https://medium.com/@rajaraodv/why-redux-needs-reducers-to-be-pure-functions-d438c58ae468#.bntrywxrf)
9. [_Two Quick Ways To Reduce React App’s Size In Production_](https://medium.com/@rajaraodv/two-quick-ways-to-reduce-react-apps-size-in-production-82226605771a#.6lepbl7ae)

#### If this was useful, please share it! Thank you! ??

