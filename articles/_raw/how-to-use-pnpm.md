---
title: How to Use pnpm – Installation and Common Commands
subtitle: ''
author: Ashutosh Biswas
co_authors: []
series: null
date: '2024-01-09T15:31:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-pnpm
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/cover-pnpm-1.png
tags:
- name: node js
  slug: node-js
- name: npm
  slug: npm
- name: performance
  slug: performance
- name: pnpm
  slug: pnpm
seo_title: null
seo_desc: 'pnpm is like npm, but it''s way faster and more efficient. After all, the
  starting p stands for _p_erformant.

  According to its creator, Zoltan Kochan, pnpm "allows you to save gigabytes of disk
  space."

  Many popular projects including Next.js, Vite, Sv...'
---

_pnpm_ is like npm, but it's way faster and more efficient. After all, the starting _p_ stands for _p_erformant.

According to its creator, Zoltan Kochan, pnpm "allows you to save gigabytes of disk space."

Many popular projects including Next.js, Vite, Svelte, and even freeCodeCamp use pnpm. So now is a great time try out this tool if you haven't yet. I'm sure your time will not be wasted.

In this article, I won't go into details of why pnpm is faster and more efficient than npm. You can check out the [official documentation](https://pnpm.io/motivation) if you want to know more about that.

The goal of this article is to quickly get you started with pnpm so you can perform your day to day tasks that you previously did with npm or yarn. Grab your favorite cup of tea or coffee ☕️, and let's dive right in! 🚀

## How to Install pnpm

I assume you already have a modern version of Node.js installed on your machine. These modern versions come with a command called `corepack`. It let's you manage your Node package managers. 

Yes you read that right! It's an experimental feature of Node but it works pretty well. 

So to start using it, you first need to enable it by entering the following command from your terminal, which has the effect of installing pnpm (and also yarn) on your system:

```zsh
corepack enable
```

It's that simple. Now if you run `pnpm --version` you will see the version you have just installed. But this might not be the latest version of pnpm. If this is the case, you can install the latest version of pnpm using this command:

```zsh
corepack prepare pnpm@latest --activate
```

Keep in mind that there are many ways to install pnpm on your system, and you can read about all of them in the [installation docs](https://pnpm.io/installation). My favorite is the `corepack` formula I've shown above.

## How to Configure your Shell for Efficiency (Optional)

Well, you now have pnpm installed. But the default command line experience can be improved to save you some effort. 

Note that this section is optional. If you want you can skip to the next section. But if you are serious about setting it up so that the CLI experience is pleasant, let's learn how to do it.

### `pnpm` is Hard to Type – So Set Up an Alias

If you find `pnpm` hard to type like I do, you can set up an alias to to save you some effort. If you're on Linux or MacOS, just put the following in your shell config (`.bashrc`, `.zshrc`, or `config.fish`):

```
alias pn=pnpm

```

If you want to set up your alias in Powershell (Windows) you can [see this doc](https://pnpm.io/installation#adding-a-permanent-alias-in-powershell-windows).

### How to Setup Tab-Completion

There are two ways you can do this in pnpm. Both have their pros and cons.

First I will share with you my favorite method. It's a shell plugin called `pnpm-shell-completion` and is available for zsh, fish shell, and Powershell core. It only covers the most commonly used commands. If you are Arch Linux and zsh user, you can install it with any AUR helper. For example, if you use `yay`, run the following command to install it:

```zsh
yay -S pnpm-shell-completion
```

Then add the following line in your `.zshrc` file to load it:

```zsh
source /usr/share/zsh/plugins/pnpm-shell-completion/pnpm-shell-completion.zsh
```

Now it should work. If you use any other supported shell, follow the plugin's [doc](https://github.com/g-plane/pnpm-shell-completion) to learn how to install it.

The second method comes built-in with pnpm. To setup this style of auto-completion, run the following command:

```shell
pnpm install-completion

```

And then follow the steps it gives you. This method covers more commands than the first approach. But it has some limitations – for example it can't auto-complete your `package.json` scripts. It also, for example, can't auto complete any dependency name that you want to uninstall.

## How to Use `pnpm`

Now, you should have pnpm installed with an alias and tab-completion. No more delay – let's see how to use pnpm.

### How to Initialize a New Project using `pnpm`

To get the default `package.json` in the current directory, run the following command:

```zsh
pnpm init

```

Unlike npm, it will not create it interactively and you don't need to specify the `-y` flag for this.

### How to Install a Package

To install a package as a dependency, the syntax is:

```
pnpm add <pkg>

```

To install a package as a dev dependency, you have pass the `-D` (or `--save-dev`) flag:

```
pnpm add -D <pkg>

```

To install a package globally, use the `-g` flag:

```
pnpm add -g <pkg>

```

### How to Install All Dependencies

Suppose you cloned a project from GitHub. It does have a `package.json` file but no `node_modules` (you should not track `node_modules` with Git). Now to install all the dependencies in that `package.json`, the command is very similar to `npm`:

```
pnpm install

```

or

```
pnpm i

```

### How to Run a `package.json` Script

This process is also very similar to `npm`. The explicit way to do it is to use the `run` command. If you have a script named `build`, you can execute it with this command:

```
pnpm run build

```

You can also use `pnpm build` to do the same thing. This is a shorthand format that can do other things as well. We'll learn more about shorthand very soon in this article.

### How to Run Commands that Come with Dependencies

You can run commands that come with dependencies using `pnpm exec`.

When you install a package, if it has commands specified by the `bin` field in its `package.json`, you will get an executable of the same name in your `node_modules/.bin` directory. Its purpose to execute the corresponding file.

`pnpm exec` prepends `./node_modules/.bin` to the `PATH` (that is, `PATH=./node_modules/.bin:$PATH`) and then executes the given command.

The following is an example that shows installing `typescript` as a dev dependency and then running the `tsc` command to create a `tsconfig.json` file:

```
pnpm add -D typescript
pnpm exec tsc --init

```

Similar to the `pnpm run` command, you can also omit `exec` and just use `pnpm tsc` to do the same thing. This works when you don't have a conflicting `tsc` script in your `package.json`. In the next section we will take a close look at this shorthand syntax.

Note that since `pnpm exec` has access to all commands resolved by the paths specified in `PATH`, you may have access to many system commands for example `rm`, `ls`, and so on.

### How `pnpm <command>` Works

`pnpm <command>` works like this:

* If `<command>` is a pnpm command (that is `add`, `install` and so on), execute that command.
* Else if `<command>` is a script found in `package.json`, execute `pnpm run <command>`.
* Else execute `pnpm exec <command>`.

So `pnpm <command>` serves as a convenient shortcut where `pnpm exec` and `pnpm run` are explicit commands without fallback.

### How to Update Packages

To update packages to their latest versions based on the specified range in `package.json`, run this command:

```
pnpm up

```

To update all dependencies to their latest versions, ignoring ranges specified in `package.json`, run this:

```
pnpm up --latest

```

### How to Remove a Package

To remove a package from both `node_modules` and your `package.json`, you can use `pnpm rm`. For example if you installed `express`, you can remove it using:

```
pnpm rm express

```

To remove a globally installed package, use the `-g` flag. Below is an example of removing the globally installed package `nodemon`:

```
pnpm rm -g nodemon

```

## Is There an `npx` Alternative?

Yes – it's the `pnpm dlx` command. It's very similar to npx. It downloads the specified package from the registry without installing it as a dependency and then runs whatever default command binary it exposes.

For example, you can run the command that `cowsay` package exposes like below to print ASCII art of a cow saying a string that you pass:

```
pnpm dlx cowsay hi freeCodeCamp

```

Now you might be wondering, if a package exposes multiple command binaries, what command `pnpm dlx` chooses as the default? Or how can you explicitly specify a command binary?

Let's see how the default command binary is determined first:

* If the `bin` field of `package.json` has only one entry, then that is used.
* Else if there is a command name in the `bin` field of `package.json` that matches the package name, ignoring the scope part if any, then that command is used.
* Else pnpm can't determine the default command and throws an error with a helpful error message that most likely will answer the second question.

To explicitly specify a particular command, you will need to install the package first using the `--package` option and specify that command after `dlx`. 

For example the package `typescript` exposes to command binaries `tsc` and `tsserver`. Now if you want to run `tsc --init` to create a `tsconfig.json` file without having `typescript` in your `node_modules` or `package.json`, you can use `pnpm dlx` like below:

```
pnpm --package=typescript dlx tsc --init

```

## Conclusion

In this tutorial, you've learned what pnpm is and how to install it. We've also covered several common pnpm commands that you will most likely need on a daily basis. 

I hope this article helped you get up and running with pnpm. Check out the [documentation of pnpm](https://pnpm.io/motivation) to learn more about it.

If you want you can follow me on [LinkedIn](https://www.linkedin.com/in/ashutosh-biswas/) and [Twitter](https://twitter.com/ashutoshbw) where I share useful coding related things.

Happy coding!

