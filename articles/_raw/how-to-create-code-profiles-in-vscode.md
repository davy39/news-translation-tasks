---
title: How to Create Code Profiles in VSCode
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-23T13:45:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-code-profiles-in-vscode
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/Screen-Shot-2019-07-06-at-1.52.10-PM-1.png
tags:
- name: Productivity
  slug: productivity
- name: teaching
  slug: teaching
- name: Visual Studio Code
  slug: vscode
seo_title: null
seo_desc: 'By JavaScript Joe

  This post piggybacks off of the work done by @avanslaars who is a fellow instructor
  at egghead.io. He shared this in the egghead Slack sometime ago and I never got
  around to setting this up myself.

  Now, I''m setting up a new laptop a...'
---

By JavaScript Joe

This post piggybacks off of the work done by [@avanslaars](https://twitter.com/avanslaars) who is a fellow instructor at [egghead.io](https://github.com/avanslaars/code-profiles). He shared this in the egghead Slack sometime ago and I never got around to setting this up myself.

Now, I'm setting up a new laptop and decided to give it shot. Following Andy's [repo here](https://github.com/avanslaars/code-profiles), I'm going to walk you through the process so you can follow along.

Before we begin, a "code profile" is essentially a different `settings.json` configuration. You can also customize which extensions load per code profile but that's beyond the scope of this article.

### 1. Create a `code_profiles` directory

The first thing we need to do is create a place to store our "profile settings". It doesn't have to be called `code_profiles`, but we're going to use that term since Andy does and it sounds nice.

He keeps his at the root of his computer so we'll do the same:

```shell
# From the root of your computer ~/
mkdir code_profiles

```

After your done, `cd` into that directory:

```shell
cd code_profiles

```

### 2. Create your first profile

Since I'm going to be using this for egghead recordings, I'm going to create a new directory called `egghead`:

```shell
# mkdir name-of-profile
mkdir egghead

```

Then `cd` into that directory:

```shell
cd egghead

```

### 3. Add your settings.json

VSCode is expecting a `data` directory with a `User` subdirectory. In there, we'll place our settings:

```shell
# -p will create parent directories as needed
mkdir -p data/User

```

After those are created, change into that new `User` subdirectory and create your `settings.json` file:

```shell
# Go into that directory
cd data/User

# Create your settings file
touch settings.json

```

Then open up your `settings.json` file and add in your settings. I'll add a modified version of what Andy [has in his](https://github.com/avanslaars/code-profiles/blob/master/egghead/data/User/settings.json):

```json
{
  "editor.tabSize": 2,
  "editor.quickSuggestions": false,
  "editor.parameterHints": false,
  "editor.suggestOnTriggerCharacters": false,
  "editor.hover": false,
  "editor.fontSize": 18,
  "editor.tabCompletion": true,
  "window.zoomLevel": 1,
  "workbench.colorTheme": "Night Owl",
  "editor.cursorBlinking": "solid",
  "editor.cursorStyle": "line",
  "editor.minimap.renderCharacters": false,
  "terminal.integrated.fontSize": 16,
  "explorer.openEditors.visible": 0
}

```

### 4. Test your new code profile

Now let's make sure we did everything right. Assuming you've already set up VSCode to [launch from the command line]([https://code.visualstudio.com/docs/setup/mac#_launching-from-the-command-line](https://code.visualstudio.com/docs/setup/mac#_launching-from-the-command-line), we can launch our new profile by running:

```shell
# replace CODE_PROFILE_NAME with the profile name used earlier
code --user-data-dir ~/code_profiles/CODE_PROFILE_NAME/data

```

And if it worked, you should see VSCode open with your settings:  


![screenshot of vscode with new settings](https://thepracticaldev.s3.amazonaws.com/i/8r277j7k5r0oi1b3axym.png)

### 5. Create an alias for your profile.

I don't know about you, but I don't want to have to remember `code --user-data-dir ...` so let's take Andy's advice and create an alias.

I'm using `zsh` so I'm going to add this alias to my `.zshrc` file like so using the keyword "teach":

```shell
# replace CODE_PROFILE_NAME with the profile name used earlier
alias teach="code --user-data-dir ~/code_profiles/CODE_PROFILE_NAME/data"

```

Now, when you want to use this code profile, all you have to do is type:

```shell
teach ~/projects/lesson

```

Woohoo! And that's it.

Special thanks to [@avanslaars](https://twitter.com/avanslaars) for sharing this. Here's a link to his [`code_profiles` repo](https://github.com/avanslaars/code-profiles) where I learned how to do this.

_NOTE_: If you are using VSCode in Portable mode, there is a [known bug](https://github.com/microsoft/vscode/issues/63657) where the flag `user-data-dir` does not currently work (special thanks to @myfonj for pointing this out).

###

_This post first appeared on [DEV](https://dev.to/jsjoeio/how-to-create-code-profiles-in-vscode-3ofo)._

? Shameless Plug: if you'd like to see more content like this, subscribe to my newsletter: [https://buttondown.email/jsjoeio](https://buttondown.email/jsjoeio) 

