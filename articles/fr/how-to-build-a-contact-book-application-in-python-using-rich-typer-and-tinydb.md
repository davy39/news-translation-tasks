---
title: Comment créer une application de carnet de contacts en Python avec Rich, Typer
  et TinyDB
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
seo_title: Comment créer une application de carnet de contacts en Python avec Rich,
  Typer et TinyDB
seo_desc: "In this Python tutorial, we'll learn how to build a terminal application\
  \ (CLI app) to manage our contact book. \nWe'll use Typer for building the CLI app,\
  \ Rich for a colorized terminal output, and TinyDB for the database.\nGet your tools\
  \ ready\nWe'll be..."
---

Dans ce tutoriel Python, nous allons apprendre à créer une application de terminal (application CLI) pour gérer notre carnet de contacts. 

Nous utiliserons Typer pour créer l'application CLI, Rich pour une sortie colorée dans le terminal, et TinyDB pour la base de données.

# **Préparez vos outils**

Nous utiliserons quelques bibliothèques externes dans ce projet. Apprenons-en plus sur elles et installons-les une par une.

Mais avant de les installer, créons un environnement virtuel et activons-le.

Nous allons créer un environnement virtuel en utilisant `virtualenv`. Python est désormais livré avec une bibliothèque `virtualenv` préinstallée. Ainsi, pour créer un environnement virtuel, vous pouvez utiliser la commande ci-dessous :

```bash
$ python -m venv env
```

La commande ci-dessus créera un environnement virtuel nommé `env`. Maintenant, nous devons activer l'environnement en utilisant la commande :

```bash
$ . env/Scripts/activate
```

Pour vérifier si l'environnement a été activé ou non, vous pouvez voir `(env)` dans votre terminal. Maintenant, nous pouvons installer les bibliothèques.

<ol>
	<li><a href="https://rich.readthedocs.io/en/latest/"><strong>Rich</strong></a> : Rich est une bibliothèque Python pour écrire du texte <em>riche</em> (avec couleur et style) dans le terminal, et pour afficher du contenu avancé tel que des tableaux, du markdown et du code avec coloration syntaxique.<br />
	Pour installer Rich, utilisez la commande :
	<pre>
<code class="language-bash">$ pip install Rich
</code></pre>
	</li>
	<li><a href="https://typer.tiangolo.com/"><strong>Typer</strong></a> : Typer est une bibliothèque pour créer des applications CLI.<br />
	Pour installer Typer, utilisez la commande :
	<pre>
<code class="language-bash">$ pip install Typer
</code></pre>
	</li>
	<li><a href="https://tinydb.readthedocs.io/"><strong>TinyDB</strong></a> : TinyDB est une base de données orientée document écrite en pur Python sans dépendances externes.<br />
	Pour installer TinyDB, utilisez la commande :
	<pre>
<code class="language-bash">$ pip install TinyDB</code></pre>
	</li>
</ol>

# **Fonctionnalités du carnet de contacts**

Notre application de carnet de contacts sera une application basée sur le terminal. Semblable à une application de liste de tâches (Todo), nous pouvons y effectuer les opérations suivantes :

1. **Ajouter (ou Créer)** : Vous pouvez ajouter un nouveau contact dans le carnet de contacts.
2. **Afficher (ou Lire)** : Vous pouvez voir tous vos contacts enregistrés dans le carnet de contacts.
3. **Modifier (ou Mettre à jour)** : Vous pouvez modifier les contacts enregistrés dans le carnet de contacts.
4. **Supprimer (ou Effacer)** : Vous pouvez supprimer les contacts enregistrés dans le carnet de contacts.  


# **Comment créer un modèle de contact**

Tout d'abord, nous allons créer une classe personnalisée ou un modèle pour notre Contact. Pensez à tous les champs qu'un contact devrait avoir. 

Je pense à ces champs – nom (name) et numéro de contact (contact number). Si vous en voyez d'autres, vous pouvez les ajouter à votre modèle. Nous allons continuer avec ces deux-là pour le moment.

Créez un répertoire appelé `contact_book`. À l'intérieur, créez un fichier Python appelé `model.py`. Ajoutez ensuite le contenu suivant dans le fichier :

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

Nous avons créé une classe appelée Contact qui prend deux paramètres obligatoires, `name` et `contact_number`. 

En plus de ces deux-là, elle prend également trois paramètres optionnels : `position`, `date_created` et **`date_updated`**. Si ces trois paramètres optionnels ne sont pas transmis, ils prennent par défaut l'index actuel et l'heure actuelle, respectivement.

De plus, nous avons défini la méthode `__repr__` qui renvoie l'objet d'une manière plus lisible.

# **Comment créer une base de données avec TinyDB**

Maintenant, configurons TinyDB et créons une base de données. Si vous débutez avec TinyDB, n'oubliez pas de consulter [ce tutoriel](https://ireadblog.com/posts/109/getting-started-with-tinydb). 

Dans le répertoire `contact_book`, créez un fichier `__init__.py` et ajoutez-y le contenu suivant :

```py
from tinydb import TinyDB, Query

db = TinyDB('contact-book.json')
db.default_table_name = 'contact-book'
ContactQuery = Query()

```

Nous avons créé une instance de la classe _TinyDB_ et lui avons passé le nom du fichier. Cela créera un fichier JSON **`contact-book.json`** où nos données seront stockées. Pour récupérer des données de cette base de données, nous aurons besoin d'une instance de la classe _Query_ de la bibliothèque **`tinydb`**.

Maintenant, définissons les différentes fonctions que nous utiliserons pour interagir avec la base de données. Dans le répertoire `contact_book`, créez un fichier `database.py` et ajoutez-y le contenu suivant :

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

Nous avons défini quatre fonctions différentes – `create()`, `read()`, `update()` et `delete()` pour chacune des opérations mentionnées ci-dessus. Nous utilisons l'attribut `position` pour identifier un contact particulier. La fonction `change_position()` est responsable du maintien de la position du contact chaque fois qu'un contact est supprimé.

# **Comment créer une CLI avec Typer**

Maintenant, créons notre CLI en utilisant Typer. À l'extérieur du répertoire `contact_book`, créez un fichier **`main.py`** et ajoutez le contenu suivant.

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

Tout d'abord, nous créons une instance de la classe _Typer_ de la bibliothèque `typer`. Ensuite, nous créons quatre fonctions distinctes pour les quatre opérations dont nous avons discuté ci-dessus. Nous lions chacune des fonctions à une commande en utilisant le décorateur `@app.command()`. Nous ajoutons également **`short_help`** juste pour aider l'utilisateur avec les commandes.

Pour ajouter un contact, nous avons besoin des paramètres `name` et `contact_number`. Pour afficher les contacts, nous n'avons besoin de rien. Pour modifier le contact, nous avons impérativement besoin de la **`position`**, tandis que les paramètres `name` et `contact_number` sont facultatifs. Pour supprimer le contact, nous avons juste besoin de la `position`.

Pour l'instant, nous n'effectuons aucune opération à l'intérieur des méthodes. Nous affichons simplement du texte en utilisant la méthode `echo` de la classe `typer`. Dans la méthode principale, nous avons juste besoin d'appeler l'objet `app()`.

Si vous lancez l'application, vous obtiendrez une sortie similaire :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/screenshot-2022-03-04-203615_k9tltn.png)

# **Comment styliser le terminal avec Rich**

Nous voulons afficher les contacts dans une belle mise en page de tableau avec différentes couleurs. Rich peut nous y aider. Si vous débutez avec Rich, n'oubliez pas de consulter [ce tutoriel](https://ireadblog.com/posts/108/getting-rich-with-python).

Modifions maintenant la fonction **`show()`** dans `main.py` car elle est responsable de l'affichage des contacts sur le terminal.

```py
from rich.console import Console
from rich.table import Table

console = Console()

@app.command(short_help='shows all contacts')
def show():
    contacts = [("Ashutosh Krishna", "+91 1234554321"),
                ("Bobby Kumar", "+91 9876556789")]

    console.print("[bold magenta]Contact Book[/bold magenta]", "📙")

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

Nous avons d'abord créé une instance de la classe _Console_. À l'intérieur de la méthode `show()`, nous avons une liste factice de contacts pour le moment. En utilisant l'objet `console`, nous affichons le titre dans une couleur magenta audacieuse. 

Ensuite, nous créons un tableau et ajoutons les colonnes. Maintenant, nous itérons sur les contacts et les plaçons dans le tableau sous forme de lignes distinctes avec différentes couleurs. Puis, à la fin, nous affichons le tableau.

# **Comment connecter les opérations de base de données aux commandes Typer**

Passons maintenant à la dernière étape qui consiste à connecter les opérations de la base de données aux commandes. C'est-à-dire que lorsque nous lançons une commande, elle doit interagir avec la base de données de manière appropriée.

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

    console.print("[bold magenta]Contact Book[/bold magenta]", "📙")

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

Dans le code ci-dessus, nous avons utilisé `create()`, `read()`, `update()` et `delete()` que nous avons créés précédemment.

# **Démo de l'application**

Voici la démo de l'application finale :

%[https://youtu.be/KnRG7cMbccE]

# **Conclusion**

Félicitations ! Vous devriez maintenant avoir une application CLI pleinement fonctionnelle. Allez-y et essayez différentes commandes pour modifier votre propre carnet de contacts.

Le code est également disponible sur [GitHub](https://github.com/ashutoshkrris/Contact-Book).

[Contenu intégré](https://github.com/ashutoshkrris/Contact-Book)

Si vous avez apprécié ce tutoriel, n'hésitez pas à le partager avec vos amis et à vous abonner à ma newsletter.

[Contenu intégré](https://www.getrevue.co/profile/ashutoshkrris)