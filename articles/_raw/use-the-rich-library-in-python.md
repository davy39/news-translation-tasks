---
title: How to Use the Rich Library with Python
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2022-02-08T16:15:49.000Z'
originalURL: https://freecodecamp.org/news/use-the-rich-library-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/Beige-Illustrated-Top-High-Paid-Jobs-Blog-Banner.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'In this article, we''ll learn about a powerful library for Python called
  Rich.

  Rich is a Python library for writing rich text (with color and style) to the terminal.
  It lets you display advanced content such as tables, markdown, and syntax-highlighted...'
---

In this article, we'll learn about a powerful library for Python called [Rich](https://rich.readthedocs.io/en/stable/introduction.html).

Rich is a Python library for writing _rich_ text (with color and style) to the terminal. It lets you display advanced content such as tables, markdown, and syntax-highlighted code.

So, why is this useful? Well, if you're not using a tool like Rich, the output of your code on the terminal can be a little boring and difficult to understand. If you want to make it clearer and prettier, you probably want to use Rich – and you've come to the right place to learn how to do it.

## How to Install Rich

You can install Rich with _pip_ as:

```bash
pip install Rich
```

To know what all Rich can do, you can type the following command in the terminal:

```bash
python -m rich
```

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-06-103528.png)

Now you can see that we can do quite a lot of things with Rich. Let's try a few of them out to see how they work.

## How to Rich print in Python

Rich has the capability to highlight the output according to the datatype. We'll import the alternative `print` function from the Rich library which takes the same arguments as the built-in `print`. 

To avoid confusion with the built-in `print` function, we'll import `print` from the `rich` library as `rprint`.

```python
from rich import print as rprint

nums_list = [1, 2, 3, 4]
rprint(nums_list)

nums_tuple = (1, 2, 3, 4)
rprint(nums_tuple)

nums_dict = {'nums_list': nums_list, 'nums_tuple': nums_tuple}
rprint(nums_dict)

bool_list = [True, False]
rprint(bool_list)

```

Output:

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-06-104950.png)

Do you see how the different data types are highlighted with different colors? This can help us a lot while debugging.

## How to Rich inspect in Python

If you use the built-in **`help`** function for viewing the documentation of a library, you'll see a boring output.

```python
import rich

print(help(rich))
```

Output:

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-06-110118.png)

Rich has an [`**inspect()**`](https://rich.readthedocs.io/en/stable/reference/init.html#rich.inspect) function which can generate a report on any Python object. It is a fantastic debug aid, and a good example of the output that Rich can generate.

```python
from rich import inspect
import rich

inspect(rich)

```

Output:

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-06-105936.png)

## How to style your console with Rich

For complete control over terminal formatting, Rich offers a [`**Console**`](https://rich.readthedocs.io/en/stable/reference/console.html#rich.console.Console) class. 

Let's write a function to [merge Python dictionaries](https://ireadblog.com/posts/76/how-to-merge-dictionaries-in-python).

```python
from rich.console import Console

console = Console()


def merge_dict(dict_one, dict_two):
    merged_dict = dict_one | dict_two
    console.log(merged_dict, log_locals=True)


merge_dict({'id': 1}, {'name': 'Ashutosh'})

```

Output:

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-06-115032.png)

In the above example, we have used the `**[log](https://rich.readthedocs.io/en/stable/console.html#logging)**` method that offers the same capabilities as print, but adds some features useful for debugging a running application. 

There are several other methods such as `[print](https://rich.readthedocs.io/en/stable/console.html#printing)`, `[print_json](https://rich.readthedocs.io/en/stable/console.html#printing-json)`, `[out](https://rich.readthedocs.io/en/stable/console.html#low-level-output)`, `[rule](https://rich.readthedocs.io/en/stable/console.html#rules)`, and so on. Learn more about them [here](https://rich.readthedocs.io/en/stable/console.html).

## How to use Tree in Rich

Rich has a [`**Tree**`](https://rich.readthedocs.io/en/stable/reference/tree.html#rich.tree.Tree) class which can generate a tree view in the terminal. A tree view is a great way of presenting the contents of a filesystem or any other hierarchical data. Each branch of the tree can have a label which may be text or any other Rich renderable.

Let's see an example by creating a family tree:

```python
from rich.tree import Tree
from rich import print as rprint


tree = Tree("Family Tree")
tree.add("Mom")
tree.add("Dad")
tree.add("Brother").add("Wife")
tree.add("[red]Sister").add("[green]Husband").add("[blue]Son")

rprint(tree)

```

Output:

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-06-120229.png)

Once we create an instance of the `**Tree**` class, we can use the `**add()**` method to add branches to it. To create a complex tree, you just use the `**add()**` method to add more branches to it. Notice the _Brother_ and _Sister_ branch in the above example.

In the official documentation, we have a [tree.py](https://github.com/Textualize/rich/blob/master/examples/tree.py) file that outputs the file structure using Tree. The output looks like this:

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-06-121033.png)

## How to display a progress bar using Rich

Rich can show continuously updated information about the status of long-running tasks, file copies, and so forth. You can customize this information, too. By default, it provides a description of the 'task,' a progress bar, percentage complete, and anticipated time left.

Multiple tasks are supported with a rich progress display, each with a bar and progress statistics. You can use this to keep track of several jobs that are being worked on in threads or processes.

Let's first try the `progress.track` method to create the progress bar.

```python
from rich.progress import track
from time import sleep


def process_data():
    sleep(0.02)


for _ in track(range(100), description='[green]Processing data'):
    process_data()

```

Output:

![Image](https://www.freecodecamp.org/news/content/images/2022/02/progress.gif)

If we want to record the time when a particular task is finished executing, we can use `console.status` instead.

```python
from rich.console import Console
from time import sleep

console = Console()

data = [1, 2, 3, 4, 5]
with console.status("[bold green]Fetching data...") as status:
    while data:
        num = data.pop(0)
        sleep(1)
        console.log(f"[green]Finish fetching data[/green] {num}")

    console.log(f'[bold][red]Done!')

```

![Image](https://www.freecodecamp.org/news/content/images/2022/02/progress-1.gif)

You can work directly with the Progress class if you need several tasks in the display or want to customize the columns in the progress display. After you've created a Progress object, use (`add_task()`) to add task(s) and (`update_progress()`) to update progress.

The Progress class is intended to be used as a context manager, automatically starting and stopping the progress display.

```python
import time

from rich.progress import Progress

with Progress() as progress:

    task1 = progress.add_task("[red]Downloading...", total=100)
    task2 = progress.add_task("[green]Processing...", total=100)
    task3 = progress.add_task("[cyan]Installing...", total=100)

    while not progress.finished:
        progress.update(task1, advance=0.9)
        progress.update(task2, advance=0.6)
        progress.update(task3, advance=0.3)
        time.sleep(0.02)

```

Output:

![Image](https://www.freecodecamp.org/news/content/images/2022/02/progress-2.gif)

## How to display Rich Columns in Python

Rich can render text or other Rich renderables in neat columns with the [`**Columns**`](https://rich.readthedocs.io/en/stable/reference/columns.html#rich.columns.Columns) class. To use, construct a Columns instance with an iterable of renderables and print it to the Console.

```python
import json
from urllib.request import urlopen

from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel


def get_content(user):
    """Extract text from user dict."""
    country = user["location"]["country"]
    name = f"{user['name']['first']} {user['name']['last']}"
    return f"[b]{name}[/b]\n[yellow]{country}"


console = Console()


users = json.loads(urlopen("https://randomuser.me/api/?results=30").read())["results"]
user_renderables = [Panel(get_content(user), expand=True) for user in users]
console.print(Columns(user_renderables))

```

Output:

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-06-124236.png)

## How to display Rich tables in Python

Rich’s [`**Table**`](https://rich.readthedocs.io/en/stable/reference/table.html#rich.table.Table) class offers a variety of ways to render tabular data to the terminal. This class has `**add_column()**` and `**add_row()**` methods to add column and row respectively to the table instance created from the `**Table**` class.

Let's create a table for our todo list. This table will have three columns – _S.No._, _Task,_ and _Status_.

```python
from rich.console import Console
from rich.table import Table

table = Table(title="Todo List")

table.add_column("S. No.", style="cyan", no_wrap=True)
table.add_column("Task", style="magenta")
table.add_column("Status", justify="right", style="green")

table.add_row("1", "Buy Milk", "✅")
table.add_row("2", "Buy Bread", "✅")
table.add_row("3", "Buy Jam", "❌")

console = Console()
console.print(table)

```

Output:

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-06-190131.png)

## Wrapping Up

In this tutorial, we learned how to use Rich to beautify the terminal. There are lots of other features that Rich supports. Learn more about them in the [official documentation](https://rich.readthedocs.io/en/stable/introduction.html).

Feel free to fork and play with the source code of this article [here](https://gitlab.com/ashutoshkrris/rich-tutorial).

Thanks for reading!

<a class="cta-button" href="https://www.getrevue.co/profile/ashutoshkrris" target="_blank">Subscribe to my newsletter</a>


