---
title: How to Install Python 3 on Mac and Update the Version with Pyenv – MacOS Homebrew
  Command Guide
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-03-04T18:44:30.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-python-3-on-mac-and-update-the-python-version-macos-homebrew-command-guide
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/pexels-christina-morillo-1181359--2-.jpg
tags:
- name: macOS
  slug: macos
- name: Python
  slug: python
- name: Python 3
  slug: python3
seo_title: null
seo_desc: 'By Dillion Megida

  When using Python, you may install different version variations for different projects.
  But sometimes this can affect how your code executes, as it may not use the correct
  version.

  In this article, we''ll learn how to install new Pyt...'
---

By Dillion Megida

When using Python, you may install different version variations for different projects. But sometimes this can affect how your code executes, as it may not use the correct version.

In this article, we'll learn how to install new Python versions (Python 3 in our case) and how to set this version as the active version for code execution.

## Install Pyenv

%[https://github.com/pyenv/pyenv]

If you're familiar with NodeJS, you'll know that `nvm` is used for managing versions of Node in different environments. `pyenv` does the same thing for Python – it's a version management tool.

This tool helps you to work on different environments which require different versions of Python.

Install `pyenv` using [Homebrew](https://brew.sh/) with the following command:

Here's the command to install Python 3 on Mac:

```bash
brew install pyenv
```

Make sure you follow the [rest of the steps for installing pyenv in the documentation](https://github.com/pyenv/pyenv#homebrew-in-macos).

## Install Python 3

With `pyenv` installed, you don't need to install Python with Homebrew anymore (as you may already be doing). You can install Python using `pyenv` with the following syntax:

```bash
pyenv install [version]
```

The version argument follows semantic versioning which is "major.minor.patch".

For Python 3, let's say we want to install `3.10.2`. Then we'll use this command:

```bash
pyenv install 3.10.2
```

To see the list of the Python versions we have, we use the following command:

```bash
pyenv versions
```

In my case, I have:

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-6.png)
_Currently installed python versions on my system_

From the screenshot above, the asterisk shows the currently active Python version, which is the default system version:

```shell
python --version
# Python 2.7.18
```

To set the newly installed version as the default, here's how to do it ([among many other ways](https://github.com/pyenv/pyenv#choosing-the-python-version)):

```bash
pyenv global 3.10.2

python --version
# Python 3.10.2
```

If your python version remains the same, you have to make sure that you add the required init command as you can see in the documentation: [Basic GitHub Checkout – 2. Configure your shell's environment for Pyenv](https://github.com/pyenv/pyenv#basic-github-checkout)

With all that in place, you can now use Python 3.

## Update Python Version

With more versions being released, you may want to update your version. You can update your version by installing a new version, making it your global default, and optionally uninstalling the old version.

Here are the commands for that:

```bash
pyenv install new.python.version

pyenv global new.python.version

pyenv uninstall old.python.version
```

Thank you for reading! I hope you now have the version of Python installed that's most useful to you.

