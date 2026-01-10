---
title: How to manage multiple Python versions and virtual environments
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-10T15:19:39.000Z'
originalURL: https://freecodecamp.org/news/manage-multiple-python-versions-and-virtual-environments-venv-pyenv-pyvenv-a29fb00c296f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*X7729FJyghz1ADa5OGhrqg.png
tags:
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Dominic Fraser

  Addition January 2019: If you are coming back to this blog after upgrading to macOS
  Mojave please see this github issue for a solution to the common pyenv ‘zlib not
  available’ problem.

  Before we start, let’s briefly go over the term...'
---

By Dominic Fraser

_Addition January 2019: If you are coming back to this blog after upgrading to macOS Mojave please see [this github issue](https://github.com/pyenv/pyenv/issues/1219#issue-363576794) for a solution to the common pyenv ‘zlib not available’ problem._

Before we start, let’s briefly go over the terms used in the title:

* **Multiple Python versions**: Different installations of Python on the same machine, 2.7 and 3.4 for example.
* [**Virtual environments**](https://packaging.python.org/tutorials/installing-packages/#creating-virtual-environments): isolated independent environments that can have both a specific version of Python and of any project-specific packages installed within them, without affecting any other projects.

Here we’ll look at three different tools for working with these, and when you might need each one. Let’s explore the use cases for:

* `venv` / `pyvenv`
* `pyenv`
* `pyenv-virtualenv`

If you are using a **single version** of Python say version **3.3+**, and want to manage **different virtual environments,** then `venv` is all you need.

If you want to use **multiple versions** of Python at **3.3+**, **with or without virtual environments**, then continue to read about `pyenv`.

If you also want to work with **Python 2**, then `pyenv-virtualenv` is a tool to consider.

### venv

From Python 3.3+ the `venv` package is included. It is ideal for creating lightweight virtual environments.

Up until Python 3.6 a script called `pyvenv` was also included as a wrapper around `venv`, but this has been [deprecated](https://docs.python.org/3/library/venv.html). It will be completely removed in Python 3.8. The exact same functionality is available when using `venv`, and any existing documentation should be updated. For anyone interested you can read [the reasons behind depreciating `pyvenv`](https://bugs.python.org/issue25154).

`venv` is used to create a new environment via the terminal command:

```bash
$ python3 -m venv directory-name-to-create
```

activated with:

```bash
$ source name-given/bin/activate
```

and deactivated with simply:

```bash
$ deactivate
```

If you need to remove the environment completely after deactivating it, you can run:

```bash
$ rm -r name-given
```

By default, the environment it creates will be the current version of Python you are using. If you are writing documentation, and want the additional safety that the correct version of Python is being used by your reader you can specify the major and minor version number in the command, like so:

```bash
$ python3.6 -m venv example-three-six
```

If the reader is using a version other than 3.6 then the command will not be successful and will indicate in its error message. However, any patch version (for example 3.6.4) will work.

When the environment is active, any packages can be installed to it via `[pip](https://pip.pypa.io/en/stable/installing/#installation)` as normal. By default, the newly created environment will **not** include any packages already installed on the machine. As `pip` itself will not necessarily be installed on the machine. It is recommended to first upgrade `pip` to the latest version, using `pip install --upgrade pip`.

Projects will commonly have a `requirements.txt` file specifying its dependencies. This allows the shortcut command `pip install -r requirements.txt` command to quickly install all packages to the newly created virtual environment. They will only exist in the virtual environment. It will not be available when it is deactivated but will persist when it is reactivated.

If you do not need to use additional versions of Python itself, then this is all you need to create isolated, project specific, virtual environments.

### [pyenv](https://github.com/pyenv/pyenv)

If you wish to use multiple versions of Python on a single machine, then `pyenv` is a commonly used tool to install and switch between versions. This is not to be confused with the previously mentioned depreciated `pyvenv` script. It does not come bundled with Python and must be installed separately.

The `[pyenv](https://github.com/pyenv/pyenv)` [documentation](https://github.com/pyenv/pyenv) includes a great description of [how it works](https://github.com/pyenv/pyenv#how-it-works), so here we will look simply at how to use it.

Firstly we will need to install it. If using Mac OS X, we can do this using Homebrew, else consider [other installation options](https://github.com/pyenv/pyenv#installation).

```bash
$ brew update
$ brew install pyenv
```

Next, add the following towards the bottom of your shell scripts to allow `pyenv` to automatically change versions for you:

```bash
eval "$(pyenv init -)"
```

To do, open your [in use shell](https://askubuntu.com/questions/590899/how-to-check-which-shell-am-i-using) script, via `$ ~/.zshrc`, `$ ~/.bashrc` or `$ ~/.bash_profile` and copy and paste the above line in.

Running `pyenv versions` will show which Python versions are currently installed, with a `*` next to the one currently in use. `pyenv version` shows this directly, and `python --version` can be used to verify this.

To install an additional version, say `3.4.0`, simply use `pyenv install 3.4.0`.

`pyenv` looks in four places to decide which version of Python to use, in priority order:

1. The `PYENV_VERSION` environment variable (if specified). You can use the `[pyenv shell](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-shell)` command to set this environment variable in your current shell session.
2. The application-specific `.python-version` file in the current directory (if present). You can modify the current directory's `.python-version` file with the `[pyenv local](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-local)` command.
3. The first `.python-version` file found (if any) by searching each parent directory, until reaching the root of your filesystem.
4. The global version file. You can modify this file using the `[pyenv global](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-global)` command. If the global version file is not present, pyenv assumes you want to use the "system" Python. (In other words, whatever version would run if pyenv weren't in your `PATH`.)

When setting up a new project that is to use Python 3.6.4 then `pyenv local 3.6.4` would be ran in its root directory. This would both set the version, and create a `.python-version` file, so that other contributors’ machines would pick it up.

The [full description of `pyenv` commands](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md) is one to bookmark.

#### pyenv and venv

When working with Python 3.3+ we now know both how to install and switch between different versions of Python, and how to create new virtual environments.

As an example, let’s say we were setting up a project that was to use Python 3.4.

First we could set our local version using `pyenv local 3.4.0`.

If we then ran `python3 -m venv example-project` a new virtual environment would be set up under `example-project`, using our locally enabled Python 3.4.0.

We activate using `source example-project/bin/activate` and can start working.

Next we could _optionally_ document that a collaborator should use `python3.4 -m venv <name>`. This means even if a collaborator was not using pyenv the `python3.4` command would error if their Python version was not the same major and minor version (3 and 4), as we intended.

Alternatively, we could choose to simply specify that 3.4.0 was to be used, and instruct `python3 -m venv <name>`. If we believe that any ve_rsion g_reater than 3.4 is acceptable, then we also may choose to use `python3` over `python3.4`, as if the collaborator was using 3.6 then they would otherwise also receive an error. This is a project specific decision.

### pyenv-virtualenv

`pyenv` can be used to install both Python 2 and 3 versions. However, as we have seen, `venv` is limited to versions of Python greater than 3.3.

`pyenv-virtualenv` is a tool to create virtual environments integrated with `pyenv`, and works for all versions of Python. It is still recommended to use the official Python `venv` where possible. But if, for example, you’re creating a virtual environment based on `2.7.13`, then this compliments `pyenv`.

It also works well with [Anaconda and Miniconda](https://conda.io/docs/glossary.html#anaconda-glossary) `conda` environments if you are already using those. A tool called `virtualenv` also exists. It’s not covered here, but it’s linked at the end.

After installing `pyenv` it can next be installed using Homebrew ([or alternatives](https://github.com/pyenv/pyenv-virtualenv)) as so:

```bash
$ brew install pyenv-virtualenv
```

Next in your `.zshrc`, `.bashrc`, or `.bash_profile` (depending on which shell you use) add the following towards the bottom:

```bash
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

This allows `pyenv` to activate and deactivate environments automatically when moving directories.

To create a new virtual environment, use:

```bash
$ pyenv virtualenv <version> <name-to-give-it>

// for example

$ pyenv virtualenv 2.7.10 my-virtual-env-2.7.10
```

Existing environments can be listed with:

```bash
$ pyenv virtualenvs
```

Activated/ deactivated with:

```bash
$ pyenv activate <name>
$ pyenv deactivate
```

At the time of writing, when using `activate` the warning `prompt changing will be removed from future release` will be displayed. This is [expected](https://github.com/pyenv/pyenv-virtualenv/issues/135#issuecomment-386154344) and refers only to the `(env-name)` being displayed in your shell, not the use of the `activate` command itself.

Installing requirements works as described in `venv`. Unlike in `venv` a `rm -r` command is not needed to remove an environment, an `[uninstall](https://github.com/pyenv/pyenv-virtualenv#delete-existing-virtualenv)` [command](https://github.com/pyenv/pyenv-virtualenv#delete-existing-virtualenv) exists.

### Final thoughts

Between these three tools, we have the ability to collaborate on any project, no matter the version of Python or of the dependencies required. We also know how to document set up instructions for others to use for any project we work on.

We can also see the reasoning behind which set to use, as not all developers will require all three.

Hopefully this was helpful, and is a useful reference in combination with the documentation linked below.

Thanks for reading! ?

### Other things I’ve explored:

* [Mocking ES and CommonJS modules with jest.mock()](https://medium.com/codeclan/mocking-es-and-commonjs-modules-with-jest-mock-37bbb552da43)
* [A beginner’s guide to Amazon’s Elastic Container Service](https://www.freecodecamp.org/news/amazon-ecs-terms-and-architecture-807d8c4960fd/)

### Resources

* [Python Virtual Environments: A Primer](https://realpython.com/python-virtual-environments-a-primer/)
* [Depreciating `pyvenv`](https://bugs.python.org/issue25154)
* [Python `venv` documentation](https://docs.python.org/3/library/venv.html)
* `[venv](https://www.reddit.com/r/learnpython/comments/4hsudz/pyvenv_vs_virtualenv/)` [vs `virtualenv`](https://www.reddit.com/r/learnpython/comments/4hsudz/pyvenv_vs_virtualenv/)
* [What is the difference between venv, pyvenv, pyenv, virtualenv, virtualenvwrapper, pipenv, etc?](https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe)
* [Do I need to install `pip`?](https://pip.pypa.io/en/stable/installing/#installation)

