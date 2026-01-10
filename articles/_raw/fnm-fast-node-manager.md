---
title: How to Use fnm – Fast Node Manager
subtitle: ''
author: Ashutosh Biswas
co_authors: []
series: null
date: '2022-06-09T15:30:55.000Z'
originalURL: https://freecodecamp.org/news/fnm-fast-node-manager
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/rocket-fnm.jpg
tags:
- name: node
  slug: node
seo_title: null
seo_desc: "If you've been working with Node for a while, you will most likely discover\
  \ that your projects – or one you're working on – are written for an older version\
  \ of Node. That means they won't work as expected with the latest version. \nIn\
  \ that case, a Nod..."
---

If you've been working with Node for a while, you will most likely discover that your projects – or one you're working on – are written for an older version of Node. That means they won't work as expected with the latest version. 

In that case, a Node version manager can help you save precious time installing and switching back and forth between different Node versions. 

Today I will introduce you to `fnm`(Fast Node Manager), a Node version manager, written in Rust with simplicity and speed in mind. `fnm` also has cross platform support.

  <h2 id="toc-heading" style="border-bottom: 2px solid cornflowerblue; margin-bottom: 0px; font-weight: normal;">Table of contents</h2>
  <ul style="padding-left: 0px; padding-block: 0.5rem; list-style-type: none; margin: 0px;">
    <li>
      <span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">1</span>
      <a href="#installation-for-linux-system-and-zsh-shell">Installation for Linux system and <code>zsh</code> shell </a>
      <ul style="padding-left: 1.3em; list-style-type: none;">
        <li><span style="margin-right:.6rem;color:#66a62e;font-weight:700">1.1</span><a href="#shell-setup">Shell setup</a></li>
        <li>
          <span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">1.2</span>
          <a href="#how-to-install-the-completion-script">How to install  the completion script </a>
        </li>
      </ul>
    </li>
    <li>
      <span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">2</span>
      <a href="#common-usage-of-fnm">Common usage of <code>fnm</code>
      </a>
      <ul style="padding-left: 1.3em; list-style-type: none;">
        <li>
          <span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">2.1</span>
          <a href="#how-to-list-all-remote-node-versions">How to list all remote Node versions </a>
        </li>
        <li>
          <span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">2.2</span>
          <a href="#how-to-install-multiple-versions-of-node">How to install multiple versions of Node </a>
        </li>
        <li>
          <span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">2.3</span>
          <a href="#how-to-set-aliases-for-a-node-version">How to set aliases for a Node version </a>
        </li>
        <li>
          <span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">2.4</span>
          <a href="#how-to-use-a-particular-version-of-node">How to use a particular version of Node </a>
        </li>
        <li>
          <span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">2.5</span>
          <a href="#how-to-attach-a-node-version-to-a-project">How to attach a Node version to a project </a>
        </li>
        <li>
          <span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">2.6</span>
          <a href="#how-to-uninstall-a-version-of-node">How to uninstall a version of Node</a>
        </li>
      </ul>
    </li>
    <li>
      <span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">3</span>
        <a href="#how-to-remove-fnm">How to remove <code>fnm</code></a>
    </li>
    <li>
      <span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">4</span>
      <a href="#summary">Summary </a>
    </li>
  </ul>

<h2 id="installation-for-linux-system-and-zsh-shell"><span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">1</span>Installation for Linux system and zsh shell
<a href="#installation-for-linux-system-and-zsh-shell" aria-label="Anchor link for: &quot;Installation for Linux system and zsh shell
&quot;" style="text-decoration: none;">§</a></h2>

Here I will only cover the installation of `fnm` for Linux systems and the `zsh` shell. See the [documentation](https://github.com/Schniz/fnm) for installation instructions for other platforms and shells.

First make sure `curl` is installed on your system. Then run the following to install `fnm`:

```zsh
curl -fsSL https://fnm.vercel.app/install | bash -s -- --skip-shell
```

It will install `fnm` in your `$HOME/.fnm/` directory.

**Updating** `fnm` is the same as **installing it again** with the above command.

<h3 id="shell-setup">
  <span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">1.1</span>Shell setup <a href="#shell-setup" aria-label="Anchor link for: &quot;Shell setup
&quot;" style="text-decoration: none;">§</a>
</h3>

There is one more important step. Just add the following to your `.zshrc` file:

```zsh
# fnm
export PATH=/home/$USER/.fnm:$PATH
eval "$(fnm env --use-on-cd --version-file-strategy=recursive)"
```

<h3 id="how-to-install-the-completion-script"><span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">1.2</span>How to install the completion script
<a href="#how-to-install-the-completion-script" aria-label="Anchor link for: &quot;How to install the completion script
&quot;" style="text-decoration: none;">§</a></h3>

Installing the completion script is **optional**. If you're wondering about the role of this step, here is what it does: it tries to auto-complete the partial command that you type relating to fnm when you press the TAB key. For example if you type `fnm ls-` and press the TAB key it will auto-complete to `fnm ls-remote`.

`fnm` comes with all the completion codes for different shells with its binary. You will have to paste that code in a file named `_fnm` in a directory specified in the `FPATH` environment variable:

```zsh
fnm completions --shell zsh > <a_fpath_dir>/_fnm
```

See the output of `echo $FPATH` to get all the possible directories and replace `<a_fpath_dir>` with an actual directory. It is recommend to use a user local path. If there are no such path, you can set one in your `.zshrc` by adding this line:

```zsh
fpath=(/home/$USER/your/favorite/path/here $fpath)
```

<h2 id="common-usage-of-fnm"><span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">2</span>Common usage of <code>fnm</code>
<a href="#common-usage-of-fnm" aria-label="Anchor link for: &quot;Common usage of fnm
&quot;" style="text-decoration: none;">§</a></h2>

<h3 id="how-to-list-all-remote-node-versions"><span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">2.1</span>How to list all remote Node versions
<a href="#how-to-list-all-remote-node-versions" aria-label="Anchor link for: &quot;How to list all remote Node versions
&quot;" style="text-decoration: none;">§</a></h3>

To see all the different Node versions you can install, run:

```zsh
fnm ls-remote
```

It will print all the versions like below:

```
.
.
.
v16.15.0 (Gallium)
v16.15.1 (Gallium)
v17.0.0
v17.0.1
v17.1.0
v17.2.0
v17.3.0
v17.3.1
v17.4.0
v17.5.0
v17.6.0
v17.7.0
v17.7.1
v17.7.2
v17.8.0
v17.9.0
v17.9.1
v18.0.0
v18.1.0
v18.2.0
v18.3.0
```

<h3 id="how-to-install-multiple-versions-of-node"><span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">2.2</span>How to install multiple versions of Node
<a href="#how-to-install-multiple-versions-of-node" aria-label="Anchor link for: &quot;How to install multiple versions of Node
&quot;" style="text-decoration: none;">§</a></h3>

Let's install Node of version `v18.3.0`:

```zsh
fnm install v18.3.0
```

For installing Node of the latest LTS version, you can use the `--lts` option. So run the following to install it also:

```
fnm install --lts
```

`fnm` also supports partial version matching. `fnm` guesses the latest available version from your partial input. For example, if you just do:

```
fnm install 17
```

It will install the Node of version `v17.9.1` which is latest available version starting with `17`. So experiment with the above command.

Let's check your Node version by entering `node --version` in your terminal. Note that the first installed one is used by default.

Before seeing how to start using a different installed version of Node, let's see how you can set an alias(name) to a version so that you can refer to it easily.

<h3 id="how-to-set-aliases-for-a-node-version"><span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">2.3</span>How to set aliases for a Node version
<a href="#how-to-set-aliases-for-a-node-version" aria-label="Anchor link for: &quot;How to set aliases for a Node version
&quot;" style="text-decoration: none;">§</a></h3>

By default, the first version of Node that you install using `fnm` receives the `default` alias.

The syntax to set an alias for a version is:

```
fnm alias <version> <name>
```

If you want to set the alias `default`, there is a shorthand:

```
fnm default <version>
```

You can set multiple aliases for a version, too.

The syntax to remove an alias is:

```
fnm unalias <name>
```

<h3 id="how-to-use-a-particular-version-of-node"><span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">2.4</span>How to use a particular version of Node
<a href="#how-to-use-a-particular-version-of-node" aria-label="Anchor link for: &quot;How to use a particular version of Node
&quot;" style="text-decoration: none;">§</a></h3>

You can use a Node of a particular version using the `use` sub-command:

```zsh
fnm use 16

```

To check the current Node version, simply run:

```
fnm current

```

To list all the Node versions that you installed with `fnm`, run:

```
fnm ls

```

![Image](https://www.freecodecamp.org/news/content/images/2022/06/fnm-ls-1.png)

Note that you can bypass `fnm` and use the system wide installation of Node on your system (if any) by using the `system`:

```zsh
fnm use system
```

<h3 id="how-to-attach-a-node-version-to-a-project"><span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">2.5</span>How to attach a Node version to a project
<a href="#how-to-attach-a-node-version-to-a-project" aria-label="Anchor link for: &quot;How to attach a Node version to a project
&quot;" style="text-decoration: none;">§</a></h3>

You can create a [`.node-version`](https://github.com/shadowspawn/node-version-usage) file in the root of your project and just write the desired Node version of that project in that file like below to attach a Node version to it:

```zsh
echo 'v18.3.0' > .node-version

```

`fnm` respects this file. So if you are in that directory, you can just use `fnm install` or `fnm use` to install or use that version.

`fnm` also respects the `.nvmrc` file (it is similar to the `.node-version` file but came from `nvm` land). So if you used `nvm` earlier, you will have smooth transition to `fnm`.

`fnm` can use these dot files to detect Node version and even start using it automatically when using `cd`, which is really handy in most cases, so I've already enabled them in the shell setup by adding the following flags to the `fnm env` command:

* **`--use-on-cd`**: This flag tells `fnm` that when you `cd` into a project root directory, it should automatically use the Node of version specified in `.node-version`(or `.nvmrc`). Cool, isn't it?
* `**--version-file-strategy=recursive**`: This flag and the `recursive` value of it basically tells `fnm` to use the specified Node version in `.node-version`(or `.nvmrc`) even when you are in a nested directory and using the `use` or `install` sub-command without a version. It also tells `fnm` to use the Node version aliased to `default` when you are out of any such project directory and using the `use` sub-command without a version. Using this flag along with `--use-on-cd` allows you to have the magic of automatically using or installing the Node of the relevant version(as described here) when you go deeply in and out of such project directories. 

If these features interfere your workflow, you can remove these flag(s) anytime in your shell setup to turn them off.

<h3 id="how-to-uninstall-a-version-of-node"><span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">2.6</span>How to uninstall a version of Node
<a href="#how-to-uninstall-a-version-of-node" aria-label="Anchor link for: &quot;How to uninstall a version of Node
&quot;" style="text-decoration: none;">§</a></h3>

Uninstalling a version of node is very similar to installing it. You just need to use sub-command `uninstall` instead of `install`. That's it.

<h2 id="how-to-remove-fnm"><span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">3</span>How to remove <code>fnm</code>
<a href="#how-to-remove-fnm" aria-label="Anchor link for: &quot;How to remove fnm
&quot;" style="text-decoration: none;">§</a></h2>

Removing `fnm` is as simple as removing the `.fnm` directory from your `home` and removing its specific config that you added in your shell config file. Remember to also remove the completion script.

<h2 id="summary"><span style="margin-right: 0.6rem; color: rgb(102, 166, 46); font-weight: bold;">4</span>Summary
<a href="#summary" aria-label="Anchor link for: &quot;Summary
&quot;" style="text-decoration: none;">§</a></h2>

Below is a summary of all the commands we have discussed in this article:

```zsh
# Listing all remote versions
fnm ls-remote

# Listing all installed ones
fnm ls

# Installing
fnm install <version>

# Uninstalling
fnm uninstall <version>

# Installing node of the latest LTS version
fnm install --lts

# Setting an alias
fnm alias <version> <name>

# Shortcut for setting 'default' as an alias
fnm default <version>

# Removing an alias
fnm unalias <name>

# Using a Node of a particular version
fnm use <version>

# Displaying the version of currently used Node
fnm current

```

Also, if you need quick help, `fnm` has built in help that you can get at any time right from your terminal like below:

* Help for the `fnm` command: `fnm --help`
* Help for any sub command `fnm <sub-command> --help`

If you like `fnm` don't forget it give it a star on [GitHub](https://github.com/Schniz/fnm). I think it deserves more stars than it has now.

Thanks for reading! If you want you can checkout my [website](https://www.ashutoshbiswas.dev/) and follow me on [Twitter](https://twitter.com/ashutoshbw) and [LinkedIn](https://www.linkedin.com/in/ashutosh-biswas/).

Happy Coding 😄

