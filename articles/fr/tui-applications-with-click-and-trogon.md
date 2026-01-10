---
title: Comment utiliser les applications TUI avec Click et Trogon – Tutoriel Linux
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
seo_title: Comment utiliser les applications TUI avec Click et Trogon – Tutoriel Linux
seo_desc: Linux and terminal applications are almost synonymous. If you have used
  applications like grep, cat, sed, and AWK, those are command line interfaces (CLI).
  And when they work together, they allow you to unleash the power of your computer
  by mixing an...
---

Linux et les applications terminal sont presque synonymes. Si vous avez utilisé des applications comme grep, cat, sed et AWK, ce sont des interfaces en ligne de commande ([CLI](https://en.wikipedia.org/wiki/Command-line_interface)). Et lorsqu'elles fonctionnent ensemble, elles vous permettent de libérer la puissance de votre ordinateur en mélangeant et en associant quelques commandes.

Parfois, la CLI devient trop complexe – et c'est là que vous pouvez la compléter avec des versions plus exploratoires des programmes appelées interfaces utilisateur en mode texte ([TUI](https://en.wikipedia.org/wiki/Text-based_user_interface)).

Les TUI comme HTOP, Glances, Midnight Commander et autres vous permettent de combiner la puissance de la CLI sans sacrifier la facilité d'utilisation.

Alors, que pouvez-vous faire lorsque votre CLI Python a trop d'options et devient intimidante ? Ne serait-il pas agréable de pouvoir découvrir l'application par vous-même, puis, une fois que vous êtes familiarisé avec elle, effectuer vos tâches rapidement en utilisant les options prises en charge par le script ?

Python dispose d'un écosystème très sain de frameworks GUI et TUI que vous pouvez utiliser pour écrire des applications esthétiques et intuitives. Dans ce tutoriel, nous parlerons de Trogon et de ce que vous pouvez faire pour rendre votre application plus conviviale tout en restant puissante pour les nouveaux utilisateurs comme pour les utilisateurs expérimentés.

Je vais vous montrer deux d'entre eux qui peuvent vous aider à résoudre les deux problèmes suivants :

1. Éviter d'être submergé et de devoir utiliser des API intimidantes lors de l'écriture d'applications. Nous utiliserons le package Python [Click](https://palletsprojects.com/p/click/) pour résoudre ce problème.

2. Permettre la découvrabilité. Cela est très important lorsque vous avez une application qui prend en charge de nombreuses options ou que vous n'avez pas utilisée depuis un certain temps. C'est là que [Trogon](https://github.com/Textualize/trogon) devient utile.

Nous réutiliserons le code source de l'une de mes applications Open Source, [rpm\_query](https://github.com/josevnz/rpm_query/tree/main), comme base. Rpm\_query est une collection d'applications simples qui peuvent interroger la base de données [RPM](https://en.wikipedia.org/wiki/RPM_Package_Manager#Local_operations) de votre système à partir de la ligne de commande.

## Ce dont vous aurez besoin pour ce tutoriel

1. Une distribution Linux, de préférence une qui utilise RPM (comme Fedora ou RedHat Enterprise Linux)

2. Python 3.8+

3. Git

4. Familiarité avec les environnements virtuels Python

5. Une connexion Internet pour télécharger les dépendances, en utilisant pip.

Je vous recommande fortement de cloner le dépôt et de créer un environnement virtuel pour suivre le tutoriel :

```shell
git clone https://github.com/josevnz/CLIWithClickAndTrogon.git
cd CLIWithClickAndTrogon
python3 -m venv ~/virtualenv/CLIWithCLickAndTrogon
. ~/virtualenv/CLIWithCLickAndTrogon/bin/activate
```

Si vous êtes prêt, plongeons dans le vif du sujet.

## À quoi ressemble une CLI (Command Line Interface) typique – Rappel rapide

Ce script utilise un module à l'intérieur du package Python [reporter](https://github.com/josevnz/CLIWithClickAndTrogon/blob/3192bed33056985421feb7dbd40cb1922ad80e6c/reporter/rpm_query.py) pour interroger la base de données RPM.

```python
#!/usr/bin/env python
"""
# rpmq_simple.py - Une CLI simple pour interroger les tailles des RPM sur votre système
Auteur : Jose Vicente Nunez
"""
import argparse
import textwrap

from reporter import __is_valid_limit__
from reporter.rpm_query import QueryHelper

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=textwrap.dedent(__doc__))
    parser.add_argument(
        "--limit",
        type=__is_valid_limit__,  # Validateur de limite personnalisé
        action="store",
        default=QueryHelper.MAX_NUMBER_OF_RESULTS,
        help="Par défaut, les résultats sont illimités, mais vous pouvez les limiter"
    )
    parser.add_argument(
        "--name",
        type=str,
        action="store",
        help="Vous pouvez filtrer par un nom de package."
    )
    parser.add_argument(
        "--sort",
        action="store_false",
        help="Les résultats triés sont activés par défaut, mais vous pouvez les désactiver"
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

Installons-le en mode éditable :

```shell
. ~/virtualenv/CLIWithCLickAndTrogon/bin/activate
pip install --editable .
```

Et voyons-le en action :

```shell
(CLIWithClickAndTrogon) [josevnz@dmaf5 CLIWithClickAndTrogon]$ rpmq_simple.py --help
usage: rpmq_simple.py [-h] [--limit LIMIT] [--name NAME] [--sort]

# rpmq_simple.py - Une CLI simple pour interroger les tailles des RPM sur votre système Auteur : Jose Vicente Nunez

options:
  -h, --help     show this help message and exit
  --limit LIMIT  Par défaut, les résultats sont illimités, mais vous pouvez les limiter
  --name NAME    Vous pouvez filtrer par un nom de package.
  --sort         Les résultats triés sont activés par défaut, mais vous pouvez les désactiver
(CLIWithClickAndTrogon) [josevnz@dmaf5 CLIWithClickAndTrogon]$ rpmq_simple.py --name kernel --limit 5
kernel-6.2.11: 0
kernel-6.2.14: 0
kernel-6.2.15: 0
```

Il semble donc que la plupart du code du script [rpmq\_simple.py](https://github.com/josevnz/CLIWithClickAndTrogon/blob/main/scripts/rpmq_simple.py) soit du code standard pour l'interface de ligne de commande, utilisant la bibliothèque standard '[ArgParse](https://docs.python.org/3/library/argparse.html)'.

ArgParse est [puissant](https://docs.python.org/3/howto/argparse.html#argparse-tutorial), mais il est aussi intimidant au début, surtout lorsque vous devez prendre en charge plusieurs cas d'utilisation.

## Une nouvelle façon de traiter la CLI avec Click

Le framework Click promet de faciliter l'analyse des arguments de ligne de commande. Pour démontrer cela, convertissons notre script d'ArgParse à [Click](https://click.palletsprojects.com/en/8.1.x/) (ils prennent tous deux en charge les options, mais Click a quelques options intéressantes que nous utiliserons) :

```python
#!/usr/bin/env python
"""
# rpmq_click.py - Une CLI simple pour interroger les tailles des RPM sur votre système
Auteur : Jose Vicente Nunez
"""
import click

from reporter.rpm_query import QueryHelper


@click.command()
@click.option('--limit', default=QueryHelper.MAX_NUMBER_OF_RESULTS,
              help="Par défaut, les résultats sont illimités, mais vous pouvez les limiter")
@click.option('--name', help="Vous pouvez filtrer par un nom de package.")
@click.option('--sort', default=True, help="Les résultats triés sont activés par défaut, mais vous pouvez les désactiver")
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

Vous remarquerez deux grands changements ici :

1. La plupart du code standard d'ArgParse a disparu, remplacé par des annotations.

2. Click fonctionne en ajoutant des décorateurs à une nouvelle fonction appelée 'command', qui prend des arguments et exécute la requête RPM.

Si vous exécutez le nouveau script, vous verrez qu'il fonctionne exactement comme avant :

```shell
(CLIWithClickAndTrogon) [josevnz@dmaf5 CLIWithClickAndTrogon]$ rpmq_click.py --help
Usage: rpmq_click.py [OPTIONS]

Options:
  --limit INTEGER  Par défaut, les résultats sont illimités, mais vous pouvez les limiter
  --name TEXT      Vous pouvez filtrer par un nom de package.
  --sort BOOLEAN   Les résultats triés sont activés par défaut, mais vous pouvez les désactiver
  --help           Show this message and exit.
(CLIWithClickAndTrogon) [josevnz@dmaf5 CLIWithClickAndTrogon]$ rpmq_click.py --name kernel --limit 5
kernel-6.2.11: 0
kernel-6.2.14: 0
kernel-6.2.15: 0
```

Alors, qu'avons-nous gagné ? Notre code est légèrement plus simple, mais il est maintenant pris en charge par Trogon, un nouveau framework que nous discuterons bientôt.

## Comment utiliser setuptools et Click

La documentation de Click [documentation r](https://click.palletsprojects.com/en/8.1.x/setuptools/#setuptools-integration)ecommande que nous devrions utiliser [setuptools](https://setuptools.pypa.io/en/latest/setuptools.html) pour créer un wrapper pour notre outil, automatiquement. Nous devons donc définir une fonction où nous gérons toutes les options et la logique de la ligne de commande, et le wrapper crée un script régulier pour nous au bon endroit lors de l'installation du package. Il pointe également vers la bonne version de Python, entre autres choses.

La documentation a la syntaxe obsolète pour setup.py, nous utiliserons donc le format plus récent setup.cfg à la place :

```python
[metadata]
name = CLIWithClickAndTrogon
version = 0.0.1
author = Jose Vicente Nunez Zuleta
author-email = kodegeek.com@protonmail.com
license = Apache 2.0
summary = Simple TUI qui interroge la base de données RPM
home-page = https://github.com/josevnz/cliwithclickandtrogon
description = Simple TUI qui interroge la base de données RPM. Un tutoriel.
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

J'ai créé un package appelé '[scripts](https://github.com/josevnz/CLIWithClickAndTrogon/tree/main/scripts)' à l'intérieur du package appelé 'reporter' avec la logique CLI utilisant click.

[setuptools générera un script appelé 'rpmq'](https://setuptools.pypa.io/en/latest/userguide/entry_point.html) pour nous qui se comporte exactement comme le script précédent – mais encore une fois, nous n'avons pas besoin de code standard pour passer des arguments à Click :

```shell
CLIWithClickAndTrogon) [josevnz@dmaf5 CLIWithClickAndTrogon]$ pip install --editable .
(CLIWithClickAndTrogon) [josevnz@dmaf5 CLIWithClickAndTrogon]$ rpmq --help
Usage: rpmq [OPTIONS]

Options:
  --limit INTEGER  Par défaut, les résultats sont illimités, mais vous pouvez les limiter
  --name TEXT      Vous pouvez filtrer par un nom de package.
  --sort BOOLEAN   Les résultats triés sont activés par défaut, mais vous pouvez les désactiver
  --help           Show this message and exit.
(CLIWithClickAndTrogon) [josevnz@dmaf5 CLIWithClickAndTrogon]$ rpmq --name kernel --limit 5
kernel-6.2.11: 0
kernel-6.2.14: 0
kernel-6.2.15: 0
```

## Comment rendre votre CLI découvrable avec Trogon

Résolvons le problème de rendre votre CLI découvrable avec Trogon. En plus d'ajouter la nouvelle bibliothèque `trogon` comme partie des exigences ([requirements.txt](https://github.com/josevnz/CLIWithClickAndTrogon/blob/main/requirements.txt) et [setup.cfg](https://github.com/josevnz/CLIWithClickAndTrogon/blob/main/setup.cfg)), nous devons ajouter un nouveau décorateur à notre CLI :

```python
#!/usr/bin/env python
"""
Une CLI simple pour interroger les tailles des RPM sur votre système
Auteur : Jose Vicente Nunez
"""
import click
from trogon import tui

from reporter.rpm_query import QueryHelper

@tui()
@click.command()
@click.option('--limit', default=QueryHelper.MAX_NUMBER_OF_RESULTS,
              help="Par défaut, les résultats sont illimités, mais vous pouvez les limiter")
@click.option('--name', help="Vous pouvez filtrer par un nom de package.")
@click.option('--sort', default=True, help="Les résultats triés sont activés par défaut, mais vous pouvez les désactiver")
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

Une seule annotation, `@tui`, et une nouvelle importation.

Il est temps de voir cela en action :

```shell
(CLIWithClickAndTrogon) [josevnz@dmaf5 CLIWithClickAndTrogon]$ rpmq_trogon.py --help
Usage: rpmq_trogon.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  command
  tui      Open Textual TUI.
```

Mêmes résultats, mais vous remarquerez deux changements :

1. Si vous souhaitez utiliser les options CLI, vous devez préfixer 'command' avant les commutateurs.

2. Il y a une nouvelle commande `tui`.

Attendez une seconde... qu'est-il arrivé aux autres drapeaux ? Ne vous inquiétez pas, si vous demandez plus d'aide pour 'command', vous les verrez là :

```shell
(CLIWithClickAndTrogon) [josevnz@dmaf5 CLIWithClickAndTrogon]$ rpmq_trogon.py command --help
Usage: rpmq_trogon.py command [OPTIONS]

Options:
  --limit INTEGER  Par défaut, les résultats sont illimités, mais vous pouvez les limiter
  --name TEXT      Vous pouvez filtrer par un nom de package.
  --sort BOOLEAN   Les résultats triés sont activés par défaut, mais vous pouvez les désactiver
  --help           Show this message and exit.
```

Ah, beaucoup mieux. Exécutons la CLI de manière similaire à ce que nous avons fait auparavant :

```shell
(CLIWithClickAndTrogon) [josevnz@dmaf5 CLIWithClickAndTrogon]$ rpmq_trogon.py command --limit 5 --name kernel
kernel-6.2.11: 0
kernel-6.2.14: 0
kernel-6.2.15: 0
```

Et qu'en est-il de la prise en charge de setuptools ? Il suffit d'ajouter l'importation et l'annotation à la fonction 'command' :

```python
import click
from trogon import tui

from reporter.rpm_query import QueryHelper
@tui()
@click.command()
@click.option('--limit', default=QueryHelper.MAX_NUMBER_OF_RESULTS,
              help="Par défaut, les résultats sont illimités, mais vous pouvez les limiter")
@click.option('--name', help="Vous pouvez filtrer par un nom de package.")
@click.option('--sort', default=True, help="Les résultats triés sont activés par défaut, mais vous pouvez les désactiver")
def command(
        name: str,
        limit: int,
        sort: bool
) -> None:
    # .... le code réel va ici
    pass
```

Permettez-moi de démontrer maintenant avec le mode TUI comment fonctionne le mode auto-découvrable :

[![asciicast](https://asciinema.org/a/590897.svg align="left")](https://asciinema.org/a/590897)

Bien ! Nous avons obtenu une TUI où certaines options sont automatiquement remplies pour nous. Cela nous donne une idée claire de la manière d'utiliser les programmes sans en savoir trop sur eux.

## Qu'est-ce qui suit

1. Téléchargez le [code source](https://github.com/josevnz/CLIWithClickAndTrogon) de ce tutoriel et commencez à expérimenter.

2. [Click](https://click.palletsprojects.com/en/8.1.x/) et [Trogon](https://discord.com/invite/Enf6Z3qhVr) disposent d'une excellente documentation et d'un support en ligne. Profitez-en.

3. Click propose de nombreux exemples plus complexes, n'hésitez pas à [consulter leur galerie](https://github.com/pallets/click/tree/main/examples).