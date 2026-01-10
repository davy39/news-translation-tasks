---
title: What is deb-get? How to Install the Debian Package with the deb-get Command
subtitle: ''
author: Rajdeep Singh
co_authors: []
series: null
date: '2022-09-07T18:27:17.000Z'
originalURL: https://freecodecamp.org/news/what-is-deb-get-debian-package-manager
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/Debian-deb-get.png
tags:
- name: command line
  slug: command-line
- name: Linux
  slug: linux
- name: package
  slug: package
seo_title: null
seo_desc: "deb-get is a new command line utility built by Martin Wimpress, an active\
  \ contributor to the Linux community. \nYou can use this utility to install third-party\
  \ packages on your Debian machine. It only works with Debian or Debian-based distros\
  \ like Ubu..."
---

`deb-get` is a new command line utility built by [Martin Wimpress](https://twitter.com/m_wimpress), an active contributor to the Linux community. 

You can use this utility to install third-party packages on your Debian machine. It only works with Debian or Debian-based distros like Ubuntu, Linux mint, Kali Linux, and so on. 

## Why Should You Use `deb-get`?

This is a great question. I think `deb-get` is more secure and faster than other package managers. 

For example, the snap package is way slower, and flatpack takes a lot of space to install a single package in your Debian system. 

The `deb-get` manager only uses `.deb` files from an official source and installs them in your system.

### Advantages of the `deb-get` Command

I think the `deb-get` command has more advantages than other package managers like snap, Flatpak, and so on. 

1. The `deb-get` command is a lightweight and stable bash command utility.
2. You can easily contribute with the deb-get CLI tool. You can add your own package or other packages in deb-get. To add a package, you need three to four lines of code.
3. The `deb-get` command installs official packages from source. It does not support third-party build packages.

### Disadvantages of the `deb-get` Command

Again, the `deb-get` command has more advantages than disadvantages. But the main disadvantage is that `deb-get` is a new utility. For that reason, it supports fewer packages than snap or flatpack.

## How to Install the `deb-get` Command on a Debian Distro

You can install `deb-get` with a bash script. For installation, you need the `curl` command to install `deb-get` in your Debian distro. If you've already installed the `curl` command on your distro, then skip this step.

```
sudo apt install curl  // alredy install,then skip it.
curl -sL https://raw.githubusercontent.com/wimpysworld/deb-get/main/deb-get | sudo -E bash -s install deb-get
```

The command output looks like this:

![Install deb-get command in debian distro](https://www.freecodecamp.org/news/content/images/2022/09/Install-deb-get-command-by-linux.png)
_Your deb-get installation looks like this._

Confirm that `deb-get` has been installed on your machine, then run the `deb-get version` command on your terminal.

```
> deb-get version
0.3.5

```

## How to Use `deb-get`

### How to Install the Debian Package with `deb-get`

With the `deb-get install` command, you can install packages from `deb-get`.

```
❯ deb-get install    <package-name>

```

![Install github-cli with deb-get command](https://www.freecodecamp.org/news/content/images/2022/09/install-package-from-deb-get.png)
_Install github-cli with the deb-get command_

### How to Delete a Package with `deb-get`

With the `deb-get purge` or `deb-get remove` command, you can delete any package with `deb-get`. I prefer the `deb-get purge` command, but both flags (`purge` and `remove`) work the same. `purge` flags delete all config files which install or config with the package.

```
❯ deb-get purge   <package-name>

```

![Delete or uninstall the package with the deb-get command](https://www.freecodecamp.org/news/content/images/2022/09/Delete-github-cli.png)
_Delete or uninstall the package with the deb-get command_

### How to Check Which Packages Are Available in `deb-get`

You check package availability in two ways. First, you can visit the [deb-get official docs](https://github.com/wimpysworld/deb-get#supported-software) to find a list of available packages. 

The second way is a command line utility. deb-get provides a lot of flags or options. My favorite is the two flags that come with deb-get.

1. `deb-get list`
2. `deb-get search  <package-name>` 

### How to use deb-get list

The `deb-get list` flag provides a list of all the available packages in the terminal. 

![list of available package in deb-get command](https://www.freecodecamp.org/news/content/images/2022/09/deb-get-list.png)
_list of available package_

### How to use deb-get search  <package-name>

The `deb-get search  <package-name>` flag helps you find a package by its name. If the flag finds a package, then it returns the package. Otherwise, it returns an empty string.

![Search package with deb-get](https://www.freecodecamp.org/news/content/images/2022/09/deb-get-search-chrome.png)
_Search package with deb-get_

You can check all the available commands with `deb-get help`.

## Conclusion

I think the deb-get distributor or Debian package manager has more potential than the other package managers.

Every package manager has advantages and disadvantages. But I believe deb-get is a game-changer in the future. 

You can share and follow on [Twitter](https://twitter.com/Official_R_deep) and [Linkedin](https://www.linkedin.com/in/officalrajdeepsingh/). If you like my work, feel free to read more content on [officialrajdeepsingh.dev](https://officialrajdeepsingh.dev/) and [Medium](https://officialrajdeepsingh.medium.com/).

### References

%[https://github.com/wimpysworld/deb-get]

%[https://github.com/wimpysworld/deb-get/blob/main/CONTRIBUTING.md]


