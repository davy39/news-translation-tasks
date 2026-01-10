---
title: How to Use TUI Applications with Click and Trogon – Linux Tutorial
subtitle: ''
author: Jose Vicente Nunez
co_authors: []
series: null
date: '2024-01-17T17:36:53.000Z'
originalURL: https://freecodecamp.org/news/tui-applications-with-click-and-trogon
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/mazinger_vampire.JPG
tags:
- name: cli
  slug: cli
- name: Linux
  slug: linux
seo_title: null
seo_desc: Linux and terminal applications are almost synonymous. If you have used
  applications like grep, cat, sed, and AWK, those are command line interfaces (CLI).
  And when they work together, they allow you to unleash the power of your computer
  by mixing an...
---

Linux and terminal applications are almost synonymous. If you have used applications like grep, cat, sed, and AWK, those are command line interfaces ([CLI](https://en.wikipedia.org/wiki/Command-line_interface)). And when they work together, they allow you to unleash the power of your computer by mixing and matching a few commands.

Sometimes the CLI gets too complex – and that's when you can complement it with more exploratory versions of the programs called text user interfaces ([TUI](https://en.wikipedia.org/wiki/Text-based_user_interface)).

TUIs like HTOP, Glances, Midnight Commander, and others allow you to mix in the power of the CLI without sacrificing the ease of use.

So what can you do when your Python CLI has too many options and becomes intimidating? Wouldn't be nice if you could have a way to 'self' discover the app, and then once you're familiar with it, perform your tasks quickly using the options supported by the script?

Python has a very [healthy ecosystem of GUI and TUI frameworks](https://github.com/josevnz/rpm_query/blob/main/Writting%20UI%20applications%20that%20can%20query%20the%20RPM%20database%20with%20Python.md) that you can use to write nice-looking and intuitive applications. In this tutorial we will talk about Trogon and what you can do to make your application more friendly yet powerful for new and seasoned users alike.

I'll show you two of them that can help you solve the following two problems:

1. Avoid becoming overwhelmed and having to use intimidating APIs when writing applications. Will use the [Click](https://palletsprojects.com/p/click/) Python package to solve that problem.
    
2. Allow discoverability. This is very important when you have an application that supports many options or that you haven't used in a while. That is where [Trogon](https://github.com/Textualize/trogon) comes handy.
    

We will reuse the source code of one of my Open Source applications, [rpm\_query](https://github.com/josevnz/rpm_query/tree/main) as a base. Rpm\_query is a collection of simple applications that can query your system [RPM database](https://en.wikipedia.org/wiki/RPM_Package_Manager#Local_operations) from the command line.

## What You'll Need for This Tutorial

1. Linux's distribution, preferably one that uses RPM (Like Fedora or RedHat enterprise Linux)
    
2. Python 3.8+
    
3. Git
    
4. Familiarity with Python virtual environments
    
5. An Internet connection so you can download dependencies, using pip.
    

I strongly suggest that you clone the repository and create a virtual environment so you can follow the tutorial:

```shell
git clone https://github.com/josevnz/CLIWithClickAndTrogon.git
cd CLIWithClickAndTrogon
python3 -m venv ~/virtualenv/CLIWithCLickAndTrogon 
. ~/virtualenv/CLIWithCLickAndTrogon/bin/activate
```

If you're all set, let's dive in.

## What a Typical CLI (Command Line Interface) Looks Like – Quick Refresher

This script uses a module inside the [reporter](https://github.com/josevnz/CLIWithClickAndTrogon/blob/3192bed33056985421feb7dbd40cb1922ad80e6c/reporter/rpm_query.py) Python package to query the RPM database.

```python
#!/usr/bin/env python
"""
# rpmq_simple.py - A simple CLI to query the sizes of RPM on your system
Author: Jose Vicente Nunez
"""
import argparse
import textwrap

from reporter import __is_valid_limit__
from reporter.rpm_query import QueryHelper

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=textwrap.dedent(__doc__))
    parser.add_argument(
        "--limit",
        type=__is_valid_limit__,  # Custom limit validator
        action="store",
        default=QueryHelper.MAX_NUMBER_OF_RESULTS,
        help="By default results are unlimited but you can cap the results"
    )
    parser.add_argument(
        "--name",
        type=str,
        action="store",
        help="You can filter by a package name."
    )
    parser.add_argument(
        "--sort",
        action="store_false",
        help="Sorted results are enabled bu default, but you fan turn it off"
    )
    args = parser.parse_args()

    with QueryHelper(
        name=args.name,
        limit=args.limit,
        sorted_val=args.sort
    ) as rpm_query:
        for package in rpm_query:
            print(f"{package['name']}-{package['version']}: {package['size']:,.0f}")
```

Let's install it, in editable mode:

```shell
. ~/virtualenv/CLIWithCLickAndTrogon/bin/activate
pip install --editable .
```

And see it in action:

```shell
(CLIWithClickAndTrogon) [josevnz@dmaf5 CLIWithClickAndTrogon]$ rpmq_simple.py --help
usage: rpmq_simple.py [-h] [--limit LIMIT] [--name NAME] [--sort]

# rpmq_simple.py - A simple CLI to query the sizes of RPM on your system Author: Jose Vicente Nunez

options:
  -h, --help     show this help message and exit
  --limit LIMIT  By default results are unlimited but you can cap the results
  --name NAME    You can filter by a package name.
  --sort         Sorted results are enabled bu default, but you fan turn it off
(CLIWithClickAndTrogon) [josevnz@dmaf5 CLIWithClickAndTrogon]$ rpmq_simple.py --name kernel --limit 5
kernel-6.2.11: 0
kernel-6.2.14: 0
kernel-6.2.15: 0
```

So it seems than most of the code on the [rpmq\_simple.py](https://github.com/josevnz/CLIWithClickAndTrogon/blob/main/scripts/rpmq_simple.py) script is boilerplate for the command line interface, using the standard '[ArgParse](https://docs.python.org/3/library/argparse.html)' library.

ArgParse is [powerful](https://docs.python.org/3/howto/argparse.html#argparse-tutorial), but it is also intimidating at first, specially when you have to support multiple use cases.

## A New Way to Process the CLI with Click

The Click framework promises to make it easier to parse out command line arguments. To demonstrate that, let's convert our script from ArgParse to [Click](https://click.palletsprojects.com/en/8.1.x/) (they both provide support for options but Click has a few interesting options we will use):

```python
#!/usr/bin/env python
"""
# rpmq_click.py - A simple CLI to query the sizes of RPM on your system
Author: Jose Vicente Nunez
"""
import click

from reporter.rpm_query import QueryHelper


@click.command()
@click.option('--limit', default=QueryHelper.MAX_NUMBER_OF_RESULTS,
              help="By default results are unlimited but you can cap the results")
@click.option('--name', help="You can filter by a package name.")
@click.option('--sort', default=True, help="Sorted results are enabled bu default, but you fan turn it off")
def command(
        name: str,
        limit: int,
        sort: bool
) -> None:
    with QueryHelper(
            name=name,
            limit=limit,
            sorted_val=sort
    ) as rpm_query:
        for package in rpm_query:
            click.echo(f"{package['name']}-{package['version']}: {package['size']:,.0f}")


if __name__ == "__main__":
    command()
```

So you will notice to big changes here:

1. Most of the boilerplate code from ArgParse is gone, replaced by annotations.
    
2. Click works by adding decorators to a new function called 'command', that takes arguments and executes the RPM query.
    

If you run the new script you will see that it works exactly as before:

```shell
(CLIWithClickAndTrogon) [josevnz@dmaf5 CLIWithClickAndTrogon]$ rpmq_click.py --help
Usage: rpmq_click.py [OPTIONS]

Options:
  --limit INTEGER  By default results are unlimited but you can cap the
                   results
  --name TEXT      You can filter by a package name.
  --sort BOOLEAN   Sorted results are enabled bu default, but you fan turn it
                   off
  --help           Show this message and exit.
(CLIWithClickAndTrogon) [josevnz@dmaf5 CLIWithClickAndTrogon]$ rpmq_click.py --name kernel --limit 5
kernel-6.2.11: 0
kernel-6.2.14: 0
kernel-6.2.15: 0
```

So what did we gain? Our code is slightly simpler but also is now supported by Trogon, a new framework we will discuss soon.

## How to Use setuptools and Click

The Click [documentation r](https://click.palletsprojects.com/en/8.1.x/setuptools/#setuptools-integration)ecommends that we should use [setuptools](https://setuptools.pypa.io/en/latest/setuptools.html) to create a wrapper for our tool, automatically. So we need to define a function where we handle all the command line options and logic and the wrapper creates a regular script for us on the right place during the package installation. It also points to the right version of Python, among other nice things.

The documentation has the deprecated syntax for setup.py, so we will use the more recent setup.cfg format instead:

```python
[metadata]
name = CLIWithClickAndTrogon
version = 0.0.1
author = Jose Vicente Nunez Zuleta
author-email = kodegeek.com@protonmail.com
license = Apache 2.0
summary = Simple TUI that queries the RPM database
home-page = https://github.com/josevnz/cliwithclickandtrogon
description = Simple TUI that queries the RPM database. A tutorial.
long_description = file: README.md
long_description_content_type = text/markdown

[options]
packages = reporter
setup_requires =
    setuptools
    wheel
    build
    pip
    twine
install_requires =
    importlib; python_version == "3.9"
    click
scripts =
    scripts/rpmq_simple.py
    scripts/rpmq_click.py
[options.entry_points]
console_scripts =
    rpmq = reporter.scripts:command
```

I created a package called '[scripts](https://github.com/josevnz/CLIWithClickAndTrogon/tree/main/scripts)' inside the package called 'reporter' with the CLI logic using click.

[setuptools will generate a script called 'rpmq'](https://setuptools.pypa.io/en/latest/userguide/entry_point.html) for us that behaves exactly as the previous script does – but again, we don't need any boilerplate code to pass arguments to Click:

```shell
CLIWithClickAndTrogon) [josevnz@dmaf5 CLIWithClickAndTrogon]$ pip install --editable .
(CLIWithClickAndTrogon) [josevnz@dmaf5 CLIWithClickAndTrogon]$ rpmq --help
Usage: rpmq [OPTIONS]

Options:
  --limit INTEGER  By default results are unlimited but you can cap the
                   results
  --name TEXT      You can filter by a package name.
  --sort BOOLEAN   Sorted results are enabled bu default, but you fan turn it
                   off
  --help           Show this message and exit.
(CLIWithClickAndTrogon) [josevnz@dmaf5 CLIWithClickAndTrogon]$ rpmq --name kernel --limit 5
kernel-6.2.11: 0
kernel-6.2.14: 0
kernel-6.2.15: 0
```

## How to Make Your CLI Discoverable with Trogon

Let's solve the problem of making your CLI discoverable with Trogon. Besides adding the new `trogon` library as part of the requirements ([requirements.txt](https://github.com/josevnz/CLIWithClickAndTrogon/blob/main/requirements.txt) and [setup.cfg](https://github.com/josevnz/CLIWithClickAndTrogon/blob/main/setup.cfg)), we need to add a new decorator to our CLI:

```python
#!/usr/bin/env python
"""
A simple CLI to query the sizes of RPM on your system
Author: Jose Vicente Nunez
"""
import click
from trogon import tui

from reporter.rpm_query import QueryHelper

@tui()
@click.command()
@click.option('--limit', default=QueryHelper.MAX_NUMBER_OF_RESULTS,
              help="By default results are unlimited but you can cap the results")
@click.option('--name', help="You can filter by a package name.")
@click.option('--sort', default=True, help="Sorted results are enabled bu default, but you fan turn it off")
def command(
        name: str,
        limit: int,
        sort: bool
) -> None:
    with QueryHelper(
            name=name,
            limit=limit,
            sorted_val=sort
    ) as rpm_query:
        for package in rpm_query:
            click.echo(f"{package['name']}-{package['version']}: {package['size']:,.0f}")


if __name__ == "__main__":
    command()
```

Just one annotation, `@tui`, and a new import.

Time to see it in action:

```shell
(CLIWithClickAndTrogon) [josevnz@dmaf5 CLIWithClickAndTrogon]$ rpmq_trogon.py --help
Usage: rpmq_trogon.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  command
  tui      Open Textual TUI.
```

Same results, but you'll notice two changes:

1. If you want to use the CLI options, you need to prepend 'command' before the switches.
    
2. There is a new `tui` command.
    

Wait a second...what happened with the other flags? No worries, if you ask for more help for 'command', you will see them there:

```shell
(CLIWithClickAndTrogon) [josevnz@dmaf5 CLIWithClickAndTrogon]$ rpmq_trogon.py command --help
Usage: rpmq_trogon.py command [OPTIONS]

Options:
  --limit INTEGER  By default results are unlimited but you can cap the
                   results
  --name TEXT      You can filter by a package name.
  --sort BOOLEAN   Sorted results are enabled bu default, but you fan turn it
                   off
  --help           Show this message and exit.
```

Ah, much better. Let's run the CLI similar to the way we did before:

```shell
(CLIWithClickAndTrogon) [josevnz@dmaf5 CLIWithClickAndTrogon]$ rpmq_trogon.py command --limit 5 --name kernel
kernel-6.2.11: 0
kernel-6.2.14: 0
kernel-6.2.15: 0
```

And what about support for setuptools? Just add the import and the annotation to the 'command function':

```python
import click
from trogon import tui

from reporter.rpm_query import QueryHelper
@tui()
@click.command()
@click.option('--limit', default=QueryHelper.MAX_NUMBER_OF_RESULTS,
              help="By default results are unlimited but you can cap the results")
@click.option('--name', help="You can filter by a package name.")
@click.option('--sort', default=True, help="Sorted results are enabled bu default, but you fan turn it off")
def command(
        name: str,
        limit: int,
        sort: bool
) -> None:
    # .... real code goes here
    pass
```

Allow me to demonstrate now with TUI mode how auto discoverable mode works:

[![asciicast](https://asciinema.org/a/590897.svg align="left")](https://asciinema.org/a/590897)

Nice! We got a TUI where some options are automatically populated for us. This gives us a clear idea how to use the programs without knowing too much about them.

## What's Next

1. Download the [source code](https://github.com/josevnz/CLIWithClickAndTrogon) for this tutorial and start experimenting.
    
2. Both [Click](https://click.palletsprojects.com/en/8.1.x/) and [Trogon](https://discord.com/invite/Enf6Z3qhVr) have great documentation and online support. Take advantage of them.
    
3. Click has many more complex examples, feel free to [check out their gallery](https://github.com/pallets/click/tree/main/examples).
