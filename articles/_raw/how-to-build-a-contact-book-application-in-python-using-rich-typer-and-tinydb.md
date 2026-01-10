---
title: How to Build a Contact Book Application in Python using Rich, Typer, and TinyDB
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2022-03-17T00:15:43.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-contact-book-application-in-python-using-rich-typer-and-tinydb
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/contact-book.png
tags:
- name: cli
  slug: cli
- name: Python
  slug: python
seo_title: null
seo_desc: "In this Python tutorial, we'll learn how to build a terminal application\
  \ (CLI app) to manage our contact book. \nWe'll use Typer for building the CLI app,\
  \ Rich for a colorized terminal output, and TinyDB for the database.\nGet your tools\
  \ ready\nWe'll be..."
---

In this Python tutorial, we'll learn how to build a terminal application (CLI app) to manage our contact book. 

We'll use Typer for building the CLI app, Rich for a colorized terminal output, and TinyDB for the database.

# **Get your tools ready**

We'll be using a few external libraries in this project. Let's learn more about them and install them one by one.

But before we install them, let's create a virtual environment and activate it.

We are going to create a virtual environment using `virtualenv`. Python now ships with a pre-installed `virtualenv` library. So, to create a virtual environment, you can use the below command:

```bash
$ python -m venv env
```

The above command will create a virtual environment named `env`. Now, we need to activate the environment using the command:

```bash
$ . env/Scripts/activate
```

To verify if the environment has been activated or not, you can see `(env)` in your terminal. Now, we can install the libraries.

<ol>
	<li><a href="https://rich.readthedocs.io/en/latest/"><strong>Rich</strong></a>: Rich is a Python library for writing <em>rich</em> text (with color and style) to the terminal, and for displaying advanced content such as tables, markdown, and syntax highlighted code.<br />
	To install Rich, use the command:
	<pre>
<code class="language-bash">$ pip install Rich
</code></pre>
	</li>
	<li><a href="https://typer.tiangolo.com/"><strong>Typer</strong></a>: Typer is a library for building CLI applications.<br />
	To install Typer, use the command:
	<pre>
<code class="language-bash">$ pip install Typer
</code></pre>
	</li>
	<li><a href="https://tinydb.readthedocs.io/"><strong>TinyDB</strong></a>: TinyDB is a document-oriented database written in pure Python with no external dependencies.<br />
	To install TinyDB, use the command:
	<pre>
<code class="language-bash">$ pip install TinyDB</code></pre>
	</li>
</ol>

# **Features of the Contact Book**

Our Contact Book application will be a terminal-based application. Similar to a Todo application, we can perform the following operations on it:

1. **Add (or Create)**: You can add a new contact in the contact book.
2. **Show (or Read)**: You can see all your contacts saved in the contact book.
3. **Edit (or Update)**: You can edit the contacts saved in the contact book.
4. **Remove (or Delete)**: You can delete the contacts saved in the contact book.  


# **How to Create a Contact Model**

First of all, we'll create a custom class or a model for our Contact. Think of all the fields that contact should have. 

I can think of these fields – name and contact number. If you can think of more, you can add them to your model. We'll be moving forward with these two for now.

Create a directory called `contact_book`. Inside that, create a Python file called `model.py`. Then add the following content in the file:

```py
import datetime

class Contact:
    def __init__ (self, name, contact_number, position=None, date_created=None, date_updated=None):
        self.name = name
        self.contact_number = contact_number
        self.position = position
        self.date_created = date_created if date_created is not None else datetime.datetime.now().isoformat()
        self.date_updated = date_updated if date_updated is not None else datetime.datetime.now().isoformat()

    def __repr__ (self) -> str:
        return f"({self.name}, {self.contact_number}, {self.position}, {self.date_created}, {self.date_updated})"

```

We have created a class called Contact which takes two mandatory parameters, `name` and `contact_number`. 

Apart from these two, it also takes three optional parameters: `position`, `date_created` and **`date_updated`**. If these three optional parameters are not passed, they default to the current index and the current times, respectively.

Further, we have defined the `__repr__` method that returns the object in a more readable way.

# **How to Create a Database using TinyDB**

Now, let's set up TinyDB and create a database. If you're new to TinyDB, make sure you check out [this tutorial](https://ireadblog.com/posts/109/getting-started-with-tinydb). 

Inside the `contact_book` directory, create a `__init__.py` file and add the following content there:

```py
from tinydb import TinyDB, Query

db = TinyDB('contact-book.json')
db.default_table_name = 'contact-book'
ContactQuery = Query()

```

We have created an instance of the _TinyDB_ class and passed the filename to it. This will create a JSON file **`contact-book.json`** where our data will be stored. To retrieve data from this database, we'll require an instance of the _Query_ class from the **`tinydb`** library.

Now, let's define the different functions which we'll be using to interact with the database. Inside the `contact_book` directory, create a `database.py` file and add the following content there:

```py
from typing import List
import datetime
from contact_book.model import Contact
from contact_book import db, ContactQuery

def create(contact: Contact) -> None:
    contact.position = len(db)+1
    new_contact = {
        'name': contact.name,
        'contact_number': contact.contact_number,
        'position': contact.position,
        'date_created': contact.date_created,
        'date_updated': contact.date_updated
    }
    db.insert(new_contact)

def read() -> List[Contact]:
    results = db.all()
    contacts = []
    for result in results:
        new_contact = Contact(result['name'], result['contact_number'], result['position'],
                              result['date_created'], result['date_updated'])
        contacts.append(new_contact)
    return contacts

def update(position: int, name: str, contact_number: str) -> None:
    if name is not None and contact_number is not None:
        db.update({'name': name, 'contact_number': contact_number},
                  ContactQuery.position == position)
    elif name is not None:
        db.update({'name': name}, ContactQuery.position == position)

    elif contact_number is not None:
        db.update({'contact_number': contact_number},
                  ContactQuery.position == position)

def delete(position) -> None:
    count = len(db)
    db.remove(ContactQuery.position == position)
    for pos in range(position+1, count):
        change_position(pos, pos-1)

def change_position(old_position: int, new_position: int) -> None:
    db.update({'position': new_position},
              ContactQuery.position == old_position)

```

We have defined four different functions – `create()`, `read()`, `update()` and `delete()` for each of the operations mentioned above. We are using the `position` attribute to identify particular contact. The `change_position()` function is responsible for maintaining the position of the contact whenever a contact is deleted.

# **How to Create a CLI using Typer**

Now let's create our CLI using Typer. Outside the `contact_book` directory, create a **`main.py`** file and add the following content.

```py
import typer

app = typer.Typer()

@app.command(short_help='adds a contact')
def add(name: str, contact_number: str):
    typer.echo(f"Adding {name}, {contact_number}")

@app.command(short_help='shows all contacts')
def show():
    typer.echo(f"All Contacts")

@app.command(short_help='edits a contact')
def edit(position: int, name: str = None, contact_number: str = None):
    typer.echo(f"Editing {position}")

@app.command(short_help='removes a contact')
def remove(position: int):
    typer.echo(f"Removing {position}")

if __name__ == " __main__":
    app()

```

First of all, we create an instance of the _Typer_ class from the `typer` library. Then we create four separate functions for the four operations that we discussed above. We bind each of the functions with a command using the `@app.command()` decorator. We also add **`short_help`** just to help the user with the commands.

To add a contact, we require the `name` and `contact_number` parameters. To show the contacts, we need nothing. To edit the contact, we definitely need the **`position`** whereas the `name` and `contact_number` parameters are optional. To remove the contact, we just need the `position`.

For now, we are not doing any operation inside the methods. We are just printing using the `echo` method in the `typer` class. In the main method, we just need to call the `app()` object.

If you run the application, you will get a similar output:

![Image](https://www.freecodecamp.org/news/content/images/2022/03/screenshot-2022-03-04-203615_k9tltn.png)

# **How to Style the Terminal using Rich**

We want to display the contacts in a beautiful-looking table layout with different colors. Rich can help us with this. If you're new to Rich, make sure you check out [this tutorial](https://ireadblog.com/posts/108/getting-rich-with-python).

Now let's modify the **`show()`** function in `main.py` as it is responsible for printing the contacts on the terminal.

```py
from rich.console import Console
from rich.table import Table

console = Console()

@app.command(short_help='shows all contacts')
def show():
    contacts = [("Ashutosh Krishna", "+91 1234554321"),
                ("Bobby Kumar", "+91 9876556789")]

    console.print("[bold magenta]Contact Book[/bold magenta]", "📕")

    if len(contacts) == 0:
        console.print("[bold red]No contacts to show[/bold red]")
    else:
        table = Table(show_header=True, header_style="bold blue", show_lines=True)
        table.add_column("#", style="dim", width=3, justify="center")
        table.add_column("Name", min_width=20, justify="center")
        table.add_column("Contact Number", min_width=12, justify="center")

        for idx, contact in enumerate(contacts, start=1):
            table.add_row(str(idx), f'[cyan]{contact[0]}[/cyan]', f'[green]{contact[1]}[/green]')
        console.print(table)

```

We have first created an instance of the _Console_ class. Inside the `show()` method, we have a dummy list of contacts for now. Using the `console` object, we print the heading in a bold magenta color. 

Next, we create a table and add the columns. Now we iterate over the contacts and put them in the table as separate rows with different colors. Then at the end, we print the table.

# **How to Connect Database Operations with Typer Commands**

Now let's do the final step which is connecting the database operations with the commands. That is, when we run a command, it should interact with the database appropriately.

```py
import typer
from rich.console import Console
from rich.table import Table
from contact_book.model import Contact
from contact_book.database import create, read, update, delete

app = typer.Typer()
console = Console()

@app.command(short_help='adds a contact')
def add(name: str, contact_number: str):
    typer.echo(f"Adding {name}, {contact_number}")
    contact = Contact(name, contact_number)
    create(contact)
    show()

@app.command(short_help='shows all contacts')
def show():
    contacts = read()

    console.print("[bold magenta]Contact Book[/bold magenta]", "📕")

    if len(contacts) == 0:
        console.print("[bold red]No contacts to show[/bold red]")
    else:
        table = Table(show_header=True,
                      header_style="bold blue", show_lines=True)
        table.add_column("#", style="dim", width=3, justify="center")
        table.add_column("Name", min_width=20, justify="center")
        table.add_column("Contact Number", min_width=12, justify="center")

        for idx, contact in enumerate(contacts, start=1):
            table.add_row(str(
                idx), f'[cyan]{contact.name}[/cyan]', f'[green]{contact.contact_number}[/green]')
        console.print(table)

@app.command(short_help='edits a contact')
def edit(position: int, name: str = None, contact_number: str = None):
    typer.echo(f"Editing {position}")
    update(position, name, contact_number)
    show()

@app.command(short_help='removes a contact')
def remove(position: int):
    typer.echo(f"Removing {position}")
    delete(position)
    show()

if __name__ == " __main__":
    app()

```

In the above code, we have used `create()`, `read()`, `update()` and `delete()` that we created previously.

# **App Demo**

Here's the demo of the final application:

%[https://youtu.be/KnRG7cMbccE]

# **Conclusion**

Congratulations! Now you should have a fully functioning CLI app. Go ahead and try different commands to modify your own contact book.

The code is also available on [GitHub](https://github.com/ashutoshkrris/Contact-Book).

[Embedded content](https://github.com/ashutoshkrris/Contact-Book)

If you enjoyed this tutorial, please share it with your friends and subscribe to my newsletter.

[Embedded content](https://www.getrevue.co/profile/ashutoshkrris)

