---
title: Comment utiliser la bibliothèque Rich avec Python
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
seo_title: Comment utiliser la bibliothèque Rich avec Python
seo_desc: 'In this article, we''ll learn about a powerful library for Python called
  Rich.

  Rich is a Python library for writing rich text (with color and style) to the terminal.
  It lets you display advanced content such as tables, markdown, and syntax-highlighted...'
---

Dans cet article, nous allons apprendre à propos d'une bibliothèque puissante pour Python appelée [Rich](https://rich.readthedocs.io/en/stable/introduction.html).

Rich est une bibliothèque Python pour écrire du texte _rich_ (avec couleur et style) dans le terminal. Elle vous permet d'afficher du contenu avancé tel que des tableaux, du markdown et du code avec surlignage syntaxique.

Alors, pourquoi est-ce utile ? Eh bien, si vous n'utilisez pas un outil comme Rich, la sortie de votre code dans le terminal peut être un peu ennuyeuse et difficile à comprendre. Si vous voulez la rendre plus claire et plus joli, vous voulez probablement utiliser Rich – et vous êtes au bon endroit pour apprendre comment le faire.

## Comment installer Rich

Vous pouvez installer Rich avec _pip_ comme suit :

```bash
pip install Rich
```

Pour savoir tout ce que Rich peut faire, vous pouvez taper la commande suivante dans le terminal :

```bash
python -m rich
```

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-06-103528.png)

Maintenant, vous pouvez voir que nous pouvons faire beaucoup de choses avec Rich. Essayons quelques-unes pour voir comment elles fonctionnent.

## Comment utiliser Rich print en Python

Rich a la capacité de surligner la sortie selon le type de données. Nous allons importer la fonction alternative `print` de la bibliothèque Rich qui prend les mêmes arguments que la fonction intégrée `print`.

Pour éviter la confusion avec la fonction intégrée `print`, nous allons importer `print` de la bibliothèque `rich` comme `rprint`.

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

Sortie :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-06-104950.png)

Voyez-vous comment les différents types de données sont surlignés avec différentes couleurs ? Cela peut nous aider beaucoup lors du débogage.

## Comment utiliser Rich inspect en Python

Si vous utilisez la fonction intégrée **`help`** pour voir la documentation d'une bibliothèque, vous verrez une sortie ennuyeuse.

```python
import rich

print(help(rich))
```

Sortie :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-06-110118.png)

Rich a une fonction [`**inspect()**`](https://rich.readthedocs.io/en/stable/reference/init.html#rich.inspect) qui peut générer un rapport sur n'importe quel objet Python. C'est un excellent outil de débogage et un bon exemple de la sortie que Rich peut générer.

```python
from rich import inspect
import rich

inspect(rich)

```

Sortie :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-06-105936.png)

## Comment styliser votre console avec Rich

Pour un contrôle complet sur le formatage du terminal, Rich offre une classe [`**Console**`](https://rich.readthedocs.io/en/stable/reference/console.html#rich.console.Console).

Écrivons une fonction pour [fusionner des dictionnaires Python](https://ireadblog.com/posts/76/how-to-merge-dictionaries-in-python).

```python
from rich.console import Console

console = Console()


def merge_dict(dict_one, dict_two):
    merged_dict = dict_one | dict_two
    console.log(merged_dict, log_locals=True)


merge_dict({'id': 1}, {'name': 'Ashutosh'})

```

Sortie :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-06-115032.png)

Dans l'exemple ci-dessus, nous avons utilisé la méthode `**[log](https://rich.readthedocs.io/en/stable/console.html#logging)**` qui offre les mêmes capacités que print, mais ajoute quelques fonctionnalités utiles pour déboguer une application en cours d'exécution.

Il existe plusieurs autres méthodes telles que `[print](https://rich.readthedocs.io/en/stable/console.html#printing)`, `[print_json](https://rich.readthedocs.io/en/stable/console.html#printing-json)`, `[out](https://rich.readthedocs.io/en/stable/console.html#low-level-output)`, `[rule](https://rich.readthedocs.io/en/stable/console.html#rules)`, et ainsi de suite. En savoir plus sur elles [ici](https://rich.readthedocs.io/en/stable/console.html).

## Comment utiliser Tree dans Rich

Rich a une classe [`**Tree**`](https://rich.readthedocs.io/en/stable/reference/tree.html#rich.tree.Tree) qui peut générer une vue en arbre dans le terminal. Une vue en arbre est un excellent moyen de présenter le contenu d'un système de fichiers ou toute autre donnée hiérarchique. Chaque branche de l'arbre peut avoir une étiquette qui peut être du texte ou tout autre élément renderable de Rich.

Voyons un exemple en créant un arbre généalogique :

```python
from rich.tree import Tree
from rich import print as rprint


tree = Tree("Arbre généalogique")
tree.add("Maman")
tree.add("Papa")
tree.add("Frère").add("Épouse")
tree.add("[red]Sœur").add("[green]Mari").add("[blue]Fils")

rprint(tree)

```

Sortie :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-06-120229.png)

Une fois que nous avons créé une instance de la classe `**Tree**`, nous pouvons utiliser la méthode `**add()**` pour ajouter des branches. Pour créer un arbre complexe, vous utilisez simplement la méthode `**add()**` pour ajouter plus de branches. Remarquez les branches _Frère_ et _Sœur_ dans l'exemple ci-dessus.

Dans la documentation officielle, nous avons un fichier [tree.py](https://github.com/Textualize/rich/blob/master/examples/tree.py) qui affiche la structure des fichiers en utilisant Tree. La sortie ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-06-121033.png)

## Comment afficher une barre de progression avec Rich

Rich peut afficher des informations continuellement mises à jour sur l'état des tâches longues, des copies de fichiers, et ainsi de suite. Vous pouvez également personnaliser ces informations. Par défaut, il fournit une description de la 'tâche', une barre de progression, un pourcentage d'achèvement et le temps restant estimé.

Plusieurs tâches sont prises en charge avec un affichage riche de progression, chacune avec une barre et des statistiques de progression. Vous pouvez utiliser cela pour suivre plusieurs travaux qui sont en cours dans des threads ou des processus.

Essayons d'abord la méthode `progress.track` pour créer la barre de progression.

```python
from rich.progress import track
from time import sleep


def process_data():
    sleep(0.02)


for _ in track(range(100), description='[green]Traitement des données'):
    process_data()

```

Sortie :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/progress.gif)

Si nous voulons enregistrer le temps lorsque une tâche particulière a terminé son exécution, nous pouvons utiliser `console.status` à la place.

```python
from rich.console import Console
from time import sleep

console = Console()

data = [1, 2, 3, 4, 5]
with console.status("[bold green]Récupération des données...") as status:
    while data:
        num = data.pop(0)
        sleep(1)
        console.log(f"[green]Fin de la récupération des données[/green] {num}")

    console.log(f'[bold][red]Terminé !')

```

![Image](https://www.freecodecamp.org/news/content/images/2022/02/progress-1.gif)

Vous pouvez travailler directement avec la classe Progress si vous avez besoin de plusieurs tâches dans l'affichage ou si vous souhaitez personnaliser les colonnes dans l'affichage de progression. Après avoir créé un objet Progress, utilisez (`add_task()`) pour ajouter des tâches et (`update_progress()`) pour mettre à jour la progression.

La classe Progress est destinée à être utilisée comme un gestionnaire de contexte, démarrant et arrêtant automatiquement l'affichage de progression.

```python
import time

from rich.progress import Progress

with Progress() as progress:

    task1 = progress.add_task("[red]Téléchargement...", total=100)
    task2 = progress.add_task("[green]Traitement...", total=100)
    task3 = progress.add_task("[cyan]Installation...", total=100)

    while not progress.finished:
        progress.update(task1, advance=0.9)
        progress.update(task2, advance=0.6)
        progress.update(task3, advance=0.3)
        time.sleep(0.02)

```

Sortie :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/progress-2.gif)

## Comment afficher des colonnes Rich en Python

Rich peut rendre du texte ou d'autres éléments renderables de Rich dans des colonnes soignées avec la classe [`**Columns**`](https://rich.readthedocs.io/en/stable/reference/columns.html#rich.columns.Columns). Pour l'utiliser, construisez une instance de Columns avec un itérable d'éléments renderables et imprimez-la dans la Console.

```python
import json
from urllib.request import urlopen

from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel


def get_content(user):
    """Extraire le texte du dictionnaire utilisateur."""
    country = user["location"]["country"]
    name = f"{user['name']['first']} {user['name']['last']}"
    return f"[b]{name}[/b]\n[yellow]{country}"


console = Console()


users = json.loads(urlopen("https://randomuser.me/api/?results=30").read())["results"]
user_renderables = [Panel(get_content(user), expand=True) for user in users]
console.print(Columns(user_renderables))

```

Sortie :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-06-124236.png)

## Comment afficher des tableaux Rich en Python

La classe [`**Table**`](https://rich.readthedocs.io/en/stable/reference/table.html#rich.table.Table) de Rich offre une variété de façons de rendre des données tabulaires dans le terminal. Cette classe a les méthodes `**add_column()**` et `**add_row()**` pour ajouter des colonnes et des lignes respectivement au tableau créé à partir de la classe `**Table**`.

Créons un tableau pour notre liste de tâches. Ce tableau aura trois colonnes – _N°_, _Tâche_ et _Statut_.

```python
from rich.console import Console
from rich.table import Table

table = Table(title="Liste de tâches")

table.add_column("N°", style="cyan", no_wrap=True)
table.add_column("Tâche", style="magenta")
table.add_column("Statut", justify="right", style="green")

table.add_row("1", "Acheter du lait", "✅")
table.add_row("2", "Acheter du pain", "✅")
table.add_row("3", "Acheter de la confiture", "❌")

console = Console()
console.print(table)

```

Sortie :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-06-190131.png)

## Conclusion

Dans ce tutoriel, nous avons appris comment utiliser Rich pour embellir le terminal. Il existe de nombreuses autres fonctionnalités que Rich prend en charge. En savoir plus sur elles dans la [documentation officielle](https://rich.readthedocs.io/en/stable/introduction.html).

N'hésitez pas à forker et à jouer avec le code source de cet article [ici](https://gitlab.com/ashutoshkrris/rich-tutorial).

Merci d'avoir lu !

<a class="cta-button" href="https://www.getrevue.co/profile/ashutoshkrris" target="_blank">S'abonner à ma newsletter</a>