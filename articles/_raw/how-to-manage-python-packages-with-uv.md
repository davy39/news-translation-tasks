---
title: How to Manage Python Packages with uv
subtitle: ''
author: Hew Hahn
co_authors: []
series: null
date: '2025-11-03T12:12:43.880Z'
originalURL: https://freecodecamp.org/news/how-to-manage-python-packages-with-uv
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1762169941014/9e66858d-3ba4-434e-a9f1-84d42a316192.png
tags:
- name: Python
  slug: python
- name: package
  slug: package
- name: terminal
  slug: terminal
seo_title: null
seo_desc: 'Python package managers let you install and manage dependencies—like NumPy,
  pandas, and so on—right from your terminal.

  In this article, you will learn how to use uv—an extremely fast Python package manager.

  Prerequisites

  To get the most out of this ...'
---

Python package managers let you install and manage dependencies—like NumPy, pandas, and so on—right from your terminal.

In this article, you will learn how to use `uv`—an extremely fast Python package manager.

## Prerequisites

To get the most out of this tutorial, you will need to:

* Know how to execute commands in your terminal,
    
* Be familiar with basic Python development/scripting.
    

## Table of Contents

* [Prerequisites](#heading-prerequisites)
    
* [Why Should You Use uv?](#heading-why-should-you-use-uv)
    
* [How to Install uv](#heading-how-to-install-uv)
    
* [How to Set up a Project with uv](#heading-how-to-set-up-a-project-with-uv)
    
* [Commonly Used uv Commands](#heading-commonly-used-uv-commands)
    
    * [How to Add a Dependency](#heading-how-to-add-a-dependency)
        
    * [How to Remove a Dependency](#heading-how-to-remove-a-dependency)
        
    * [How to Run Python Code](#heading-how-to-run-python-code)
        
    * [How to Move Your Project](#heading-how-to-move-your-project)
        
    * [How to Add and Run Tools](#heading-how-to-add-and-run-tools)
        
    * [How to Run Tools Without Adding Them to Your Project](#heading-how-to-run-tools-without-adding-them-to-your-project)
        
    * [How to Manage Multiple Python Versions](#heading-how-to-manage-multiple-python-versions)
        
    * [How to Migrate from pip to uv](#heading-how-to-migrate-from-pip-to-uv)
        
* [Conclusion](#heading-conclusion)
    

## Why Should You Use uv?

`uv` is a free and open-source Python project management tool. Written in Rust, `uv` is fast and easy-to-use. It has become a standard package manager for modern Python development. You can also use it to manage your virtual environments, making it a good alternative for `pip` and `venv`.

[Speed tests](https://docs.astral.sh/uv/) have shown that `uv` is faster than other popular package managers when it comes to installing dependencies.

## How to Install uv

To install `uv`, simply execute the following command in your terminal:

For Linux/macOS:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

For Windows:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## How to Set up a Project with uv

To start a new project with `uv`, run the following command:

```bash
uv init freecodecamp-project
```

This creates the folder `/freecodecamp-project` in your working directory with the following structure:

```bash
├── .gitignore # hidden text file that lists files to be ignored by git
├── .python-version # hidden text file that keeps record of your Python's version number
├── README.md
├── main.py
└── pyproject.toml
```

`README.md` is a markdown file, which you can use to communicate information about your project (just as a repository README file on GitHub). `pyproject.toml` is the configuration file for your project. You can edit it to change your project’s name, version and description. It also keeps track of dependencies you add to project. Last but not least, `main.py` is where you put your Python code.

## Commonly Used uv Commands

Before you can run any `uv` commands, move your terminal into your project folder:

```bash
cd freecodecamp-project
```

### How to Add a Dependency

To add a dependency (for example, NumPy), run:

```bash
uv add numpy
# or if you need a specific version
uv add 'numpy==2.3.0'
```

This automatically adds a virtual environment and a `.lock` file with a new entry:

```bash
├── .venv # hidden folder inside of which your required packages will be installed
└── uv.lock
```

The `.lock` file keeps record of the exact versions of your dependencies and their required packages. You should never modify it directly.

### How to Remove a Dependency

To remove a dependency, run:

```bash
uv remove numpy
```

This will also remove the corresponding entry from the `.lock` file.

### How to Run Python Code

To run your Python script, execute:

```bash
uv run main.py
```

This will run the code inside the created virtual environment with the installed dependencies in one step! That is, you don’t need to explicitly activate the virtual environment and then run your code.

### How to Move Your Project

Sometimes you may want to move your project to another machine. Maybe you want to share it with colleagues, or set it up on a production server. Getting to run your code on another machine has never been easier than with `uv`. You can simply copy your project folder to the destination environment and run the following command in the destination terminal:

```bash
uv sync --locked
```

This installs the exact versions of your project dependencies!

### How to Add and Run Tools

Sometimes you may need tools like `ruff`, a Python linter (code formatter), which you can add just like any other dependency to your project:

```bash
uv add ruff
```

To run an installed tool, execute:

```bash
uv run ruff check
```

### How to Run Tools Without Adding Them to Your Project

Sometimes you may not want to add tools to your dependencies. For example, because you just want to make one-off checks. `uv` has got you covered with `tool run`. Simply run:

```bash
uv tool run ruff check
# or equivalently 
uvx ruff check
```

This will run the tool in an isolated environment independent.

### How to Manage Multiple Python Versions

If your system has Python installed, `uv` will use it. Otherwise, it will automatically install the latest Python version when you execute Python code or create a virtual environment with `uv`. However, you can also use it to manage multiple Python versions:

```bash
# install the latest Python version
uv python install
# install multiple Python versions
uv python install 3.11 3.12
# list all installed Python versions
uv python list
# set the version to be used in the current project (.python-version)
uv python pin 3.11
```

### How to Migrate from pip to uv

`uv` works as drop-in replacement for `pip`, meaning that you can use common `pip` commands with `uv`. Let’s say you received a `requirements.txt` file. To install the listed dependencies, you can run:

```bash
uv pip install -r requirements.txt
```

## Conclusion

You just learned how to use `uv`! Before `uv`, managing dependencies, virtual environments and Python versions had been notoriously cumbersome. As an ML engineer at [MLjobs.io](https://mljobs.io), I can safely say that `uv` has been a game changer. Check out `uv`'s [documentation](https://docs.astral.sh/uv/) to learn more.
