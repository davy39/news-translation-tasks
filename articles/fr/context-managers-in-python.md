---
title: Qu'est-ce que les gestionnaires de contexte en Python ?
subtitle: ''
author: Farhan Hasin Chowdhury
co_authors: []
series: null
date: '2023-10-02T13:49:54.000Z'
originalURL: https://freecodecamp.org/news/context-managers-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/python-context-managers-1.jpg
tags:
- name: Python
  slug: python
seo_title: Qu'est-ce que les gestionnaires de contexte en Python ?
seo_desc: 'One of the most common tasks that you''ll have to perform in your programs
  is working with external resources. These resources can be files on your computer''s
  storage or an open connection to third-party service on the internet.

  For the sake of simpli...'
---

L'une des tâches les plus courantes que vous devrez effectuer dans vos programmes est de travailler avec des ressources externes. Ces ressources peuvent être des fichiers sur le stockage de votre ordinateur ou une connexion ouverte à un service tiers sur Internet.

Pour simplifier, imaginez un programme qui ouvre un fichier, écrit quelque chose dedans, puis ferme le fichier.

Une façon d'implémenter ce programme en Python serait comme suit :

```python
def main():
    my_file = open('books.txt', 'w')
    my_file.write('Si demain vient de Sidney Sheldon')
    my_file.close()


if __name__ == '__main__':
    main()

```

Étant donné que vous exécutez ce programme avec les bonnes permissions sur votre ordinateur, il créera un fichier appelé `books.txt` et y écrira `Si demain vient de Sidney Sheldon`.

La fonction `open()` est l'une des fonctions intégrées de Python. Elle peut ouvrir un fichier à partir d'un chemin donné et retourner un objet fichier correspondant.

Un objet fichier ou un objet de type fichier, comme on l'appelle souvent, est un moyen utile d'encapsuler des méthodes comme `read()`, `write()`, ou `close()`.

La méthode `write()` peut être utilisée pour écrire/envoyer un objet de type bytes à un flux ouvert, comme un fichier.

Chaque fois que vous ouvrez une ressource externe, vous devez la fermer lorsqu'elle n'est plus nécessaire, et la méthode `close()` fait exactement cela.

Ce programme est fonctionnel, mais il présente un grand défaut. Si le programme ne parvient pas à fermer le fichier, il restera ouvert jusqu'à ce que le programme lui-même se ferme.

Vous voyez, chaque programme que vous exécutez sur votre ordinateur obtient une quantité finie de mémoire allouée. Toutes les variables que vous créez ou les ressources externes que vous ouvrez à partir d'un programme restent dans la mémoire qui lui est allouée par votre ordinateur.

Si un programme comme celui-ci continue à ouvrir de nouveaux fichiers sans fermer les précédents, la mémoire allouée continuera à diminuer.

À un moment donné, le programme manquera inévitablement de mémoire et plantera de manière peu élégante. Ce problème est appelé une fuite de mémoire.

Une façon d'empêcher cela en Python est d'utiliser une instruction `try...except...finally`.

```python
def main():
    my_file = open('books.txt', 'w')

    try:
        my_file.write('Si demain vient de Sidney Sheldon')
    except Exception as e:
        print(f'L\'écriture dans le fichier a échoué : {e}')
    finally:
        my_file.close()


if __name__ == '__main__':
    main()

```

Le code à l'intérieur du bloc `finally` s'exécutera quoi qu'il arrive. Donc, même si le programme échoue lors de l'action principale, il sera toujours exécuté.

Cela résout donc le problème, mais imaginez écrire ces lignes de code chaque fois que vous voulez écrire quelque chose dans un fichier.

Ce n'est pas très réutilisable. Vous devrez vous répéter beaucoup et les chances de sauter une partie de l'échelle `if...except...finally` sont également possibles.

C'est là que les gestionnaires de contexte interviennent.

## Qu'est-ce qu'un gestionnaire de contexte en Python ?

Selon le glossaire Python, un gestionnaire de contexte est —

> Un objet qui contrôle l'environnement vu dans une instruction `with` en définissant les méthodes `__enter__()` et `__exit__()`.

Cela peut ne pas être très clair pour vous. Laissez-moi expliquer le concept avec un exemple.

L'instruction `with` en Python vous permet d'exécuter un bloc de code dans un contexte d'exécution défini par un objet gestionnaire de contexte.

Une fois que le bloc de code a fini de s'exécuter, l'objet gestionnaire de contexte se chargera de libérer les ressources externes qui ne sont plus nécessaires.

Vous pouvez réécrire le programme en utilisant l'instruction `with` comme suit :

```python
def main():
    with open('books.txt', 'w') as my_file:
        my_file.write('Si demain vient de Sidney Sheldon')


if __name__ == '__main__':
    main()

```

Puisque la fonction `open()` est associée à une instruction `with` dans cet exemple, la fonction créera un gestionnaire de contexte.

L'objet fichier sera accessible dans le contexte du bloc de code indenté, ce qui signifie que l'objet fichier n'existe pas en dehors de ce contexte.

Le mot-clé `as` est utile lorsque vous souhaitez assigner une variable cible à un objet retourné. Ici, la variable `my_file` est la cible et contiendra l'objet fichier.

Vous pouvez faire ce que vous voulez dans le bloc de code indenté et vous n'avez pas à vous soucier de fermer le fichier.

Car une fois que le bloc de code a fini de s'exécuter, le gestionnaire de contexte fermera le fichier automatiquement.

Ainsi, vous avez réécrit toute l'échelle `try...except...finally` en deux lignes de code en utilisant l'instruction `with` et un gestionnaire de contexte.

Mais comment cela se passe-t-il ? Comment un objet gestionnaire de contexte gère-t-il la tâche de configuration et de fermeture des ressources ?

Et où sont ces méthodes `__enter__()` et `__exit__()` dont vous avez lu dans le glossaire de la documentation Python ?

Eh bien, je suis si heureux que vous ayez demandé :-)

## Comment créer un gestionnaire de contexte personnalisé en Python

Le physicien théoricien américain, Richard Feynman, a dit un jour —

> Ce que je ne peux pas créer, je ne comprends pas.

Ainsi, pour comprendre les fonctionnalités d'un gestionnaire de contexte, vous devez en créer un vous-même et il existe deux façons distinctes de le faire.

La première est une approche basée sur un générateur et la seconde est une approche basée sur une classe. Dans cette section, je vous enseignerai les deux.

Mais avant cela, laissez-moi vous donner un exemple complexe qui fait plus que simplement ouvrir et fermer des fichiers en Python.

Imaginez une autre application Python qui doit communiquer avec une base de données SQLite pour lire et écrire des données.

Vous pouvez écrire ce programme comme suit :

```python
import sqlite3

create_table_sql_statement = 'CREATE TABLE IF NOT EXISTS books(title TEXT, author TEXT)'
insert_into_table_sql_statement = "INSERT INTO books VALUES ('Si demain vient', 'Sidney Sheldon'), ('The Lincoln Lawyer', 'Michael Connelly')"
select_from_table_sql_statement = 'SELECT * FROM books'


def main():
    database_path = ':memory:'

    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    try:
        cursor.execute(create_table_sql_statement)
        connection.commit()

        cursor.execute(insert_into_table_sql_statement)
        connection.commit()

        cursor.execute(select_from_table_sql_statement)

        print(cursor.fetchall())
    except Exception as e:
        print(f'L\'action de lecture ou d\'écriture dans la base de données a échoué : {e}')
    finally:
        connection.close()


if __name__ == '__main__':
    main()

# [('Si demain vient', 'Sidney Sheldon'), ('The Lincoln Lawyer', 'Michael Connelly')]

```

Ce programme Python établit une connexion avec une base de données SQLite. Ensuite, il crée une nouvelle table appelée books avec deux colonnes `TEXT` nommées `title` et `author`.

Le programme stocke ensuite des informations sur trois livres dans la table, les récupère de la base de données et imprime les données récupérées sur la console.

Comme le montre la sortie de l'instruction `print()`, le programme a réussi à sauvegarder et à récupérer les données données de la base de données.

Il y a trois requêtes SQL dans ce programme responsables des actions de la base de données que je viens de décrire.

```python
create_table_sql_statement = 'CREATE TABLE IF NOT EXISTS books(title TEXT, author TEXT)'
insert_into_table_sql_statement = "INSERT INTO books VALUES ('Si demain vient', 'Sidney Sheldon'), ('The Lincoln Lawyer', 'Michael Connelly')"
select_from_table_sql_statement = 'SELECT * FROM books'
```

J'ai gardé ces trois lignes de code en haut du fichier pour garder la fonction `main()` plus propre. Le reste du programme configure la base de données et exécute les requêtes.

Python offre un excellent support pour les bases de données SQLite, grâce au module `sqlite3` encapsulant des méthodes utiles telles que la méthode `sqlite3.connect()`.

Cette méthode prend le chemin vers une base de données sous forme de chaîne, tente d'établir une connexion et, en cas de succès, retourne un objet `Connection`.

Si vous passez `:memory:` au lieu d'un chemin de fichier, le programme créera une base de données temporaire dans la mémoire de votre ordinateur.

Une fois que vous avez une connexion, vous aurez besoin d'un objet `Cursor`. Un objet curseur est une couche d'abstraction nécessaire pour exécuter des requêtes SQL.

La méthode `cursor()` encapsulée dans l'objet `Connection` retourne un nouveau curseur vers la base de données connectée.

Dans un bloc `try`, vous pouvez tenter d'exécuter la requête que vous souhaitez en utilisant les méthodes `execute()` ou `executemany()`.

```python
    try:
        cursor.execute(create_table_sql_statement)
        connection.commit()

        cursor.execute(insert_into_table_sql_statement)
        connection.commit()

        cursor.execute(select_from_table_sql_statement)

        print(cursor.fetchall())
```

Vous devez appeler la méthode `connection.commit()` chaque fois que vous écrivez quelque chose dans la base de données. Sinon, les modifications seront perdues.

Les données retournées par une base de données restent dans l'objet `cursor` et vous pouvez y accéder en utilisant les méthodes `cursor.fetchone()` ou `cursor.fetchall()`.

En cas d'échec, le bloc `except` sera déclenché. Le bloc `finally` s'exécutera sans condition et fermera la connexion à la base de données à la fin.

Cela est bien et fonctionnel, mais comme je l'ai déjà dit, ce n'est pas très réutilisable et est sujet aux erreurs.

Malheureusement, ou dans notre cas heureusement, Python ne vient pas avec un gestionnaire de contexte intégré pour gérer les connexions avec les bases de données SQLite.

Alors, essayons de voir si nous pouvons en produire un nous-mêmes.

### Comment créer un gestionnaire de contexte basé sur une classe en Python

Pour écrire un gestionnaire de contexte basé sur une classe en Python, vous devez créer une classe vide avec trois méthodes spécifiques :

```python
class Database:
    def __init__(self):
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
```

La première est évidemment le constructeur de la classe qui n'accepte aucun paramètre pour l'instant. Il sera responsable d'accepter un chemin de base de données :

```python
import sqlite3

class Database:
    def __init__(self, path: str):
        self.path = path

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
```

La méthode `__enter__()` gère la tâche de configuration de la ressource. C'est ici que vous établissez la connexion et instanciez le curseur :

```python
import sqlite3

class Database:
    def __init__(self, path: str):
        self.path = path

    def __enter__(self):
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
```

Cependant, vous ne pouvez pas retourner deux objets à la fois, donc vous devez retourner l'instance de la classe elle-même.

Enfin, la méthode `__exit__()` gère la tâche de fermeture de la ressource externe en question.

```python
import sqlite3

class Database:
    def __init__(self, path: str):
        self.path = path

    def __enter__(self):
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
    	if exc_type is not None:
            print(f'une erreur s\'est produite : {exc_val}')

        self.connection.close()
```

Vous pouvez utiliser ce gestionnaire de contexte en conjonction avec l'instruction `with` dans votre code comme suit :

```python
import sqlite3

create_table_sql_statement = 'CREATE TABLE IF NOT EXISTS books(title TEXT, author TEXT)'
insert_into_table_sql_statement = "INSERT INTO books VALUES ('Si demain vient', 'Sidney Sheldon'), ('The Lincoln Lawyer', 'Michael Connelly')"
select_from_table_sql_statement = 'SELECT * FROM books'


class Database:
    def __init__(self, path: str):
        self.path = path

    def __enter__(self):
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
    	if exc_type is not None:
            print(f'une erreur s\'est produite : {exc_val}')


def main():
    with Database(':memory:') as db:
        db.cursor.execute(create_table_sql_statement)
        db.connection.commit()

        db.cursor.execute(insert_into_table_sql_statement)
        db.connection.commit()
        
        db.cursor.execute(select_from_table_sql_statement)
        
        print(db.cursor.fetchall())


if __name__ == '__main__':
    main()

# [('Si demain vient', 'Sidney Sheldon'), ('The Lincoln Lawyer', 'Michael Connelly')]

```

Comme le montre la sortie de l'appel de la fonction `print()`, le programme a réussi à stocker et à récupérer les données données de la base de données.

Sans l'instruction `with`, `Database` est juste une vieille classe ordinaire. Cependant, dès que vous mettez `with` devant, les trois méthodes se mettent en action.

La méthode `__init__()` est l'initialiseur et fonctionne de manière identique à la méthode d'initialisation de toute autre classe Python ordinaire. Elle prend le chemin vers la base de données.

La méthode `__enter__()` établit la connexion à la base de données et retourne l'instance de la classe du gestionnaire de contexte à la variable cible, `db` dans ce cas.

Cette variable cible encapsule maintenant à la fois les objets de connexion et de curseur. Vous pouvez y accéder respectivement en tant que `db.connection` et `db.cursor`.

Une fois que le code à l'intérieur du bloc `with` a fini de s'exécuter, la méthode `__exit__()` sera exécutée et fermera la connexion active à la base de données.

Vous pouvez gérer toute exception qui peut survenir pendant l'exécution à l'intérieur de la méthode `__exit__()`. Si une exception se produit, `exc_type` contient le type de l'exception, `exc_val` contient la valeur de l'exception, `exc_tb` contient la trace de la pile.

Si aucune exception ne se produit, les trois variables auront une valeur de `None`. Je ne vais pas entrer dans les détails de la gestion des exceptions dans cet article, car cela peut prendre de nombreuses formes en fonction de ce que vous traitez.

Pour rendre ce gestionnaire de contexte personnalisé accessible depuis n'importe quel endroit du programme, vous pouvez le mettre dans son propre module séparé ou même dans un package.

C'est une solution bien meilleure que l'échelle `try...except...finally` que vous avez vue précédemment. Vous n'avez pas à vous répéter et les chances d'une erreur humaine sont plus faibles.

### Comment créer un gestionnaire de contexte basé sur un générateur en Python

Comme le suggère le titre de cette section, cette approche utilise un générateur au lieu d'une classe pour implémenter un gestionnaire de contexte.

Syntactiquement, les générateurs sont presque identiques aux fonctions normales, sauf que vous devez utiliser `yield` au lieu de `return` dans un générateur.

Écrire un gestionnaire de contexte basé sur un générateur nécessite moins de code, mais il perd également une partie de sa lisibilité.

Vous pouvez écrire l'équivalent basé sur un générateur du gestionnaire de contexte `Database` basé sur une classe comme suit :

```python
import sqlite3
from contextlib import contextmanager

@contextmanager
def database(path: str):
    connection = sqlite3.connect(path)
    try:
        cursor = connection.cursor()
        yield {'connection': connection, 'cursor': cursor}
    except Exception as e:
        print(f'une erreur s\'est produite : {e}') 
    finally:
        connection.close()
```

Au lieu d'une classe, vous avez ici une fonction génératrice, donc il n'y a pas d'initialiseur. Au lieu de cela, la fonction elle-même peut accepter le chemin vers la base de données en tant que paramètre.

Dans un bloc `try`, vous pouvez établir une connexion à la base de données, instancier le curseur et retourner les deux objets à l'utilisateur.

Vous pouvez écrire `yield connection, cursor` pour retourner les deux objets, mais dans ce cas, le générateur les retournera sous forme de tuple.

Je préfère utiliser des chaînes de caractères plutôt que des nombres comme accesseurs, c'est pourquoi j'ai placé les deux objets dans un dictionnaire avec des clés descriptives.

Le bloc `except` s'exécutera en cas d'exception. N'hésitez pas à implémenter toute stratégie de gestion des exceptions que vous jugez appropriée.

Le bloc `finally` s'exécutera sans condition et fermera la connexion ouverte à la fin du bloc `with`.

Puisqu'il n'y a pas de méthodes `__enter__()` ou `__exit__()`, vous devez décorer le générateur avec le décorateur `@contextmanager`.

Ce décorateur définit une fonction d'usine pour les gestionnaires de contexte d'instruction `with`, sans avoir besoin de créer une classe ou des méthodes `__enter__()` et `__exit__()` séparées.

L'utilisation de ce gestionnaire de contexte est identique à celle de son homologue basé sur une classe, à l'exception de la capitalisation de son nom.

```python
import sqlite3
from contextlib import contextmanager

create_table_sql_statement = 'CREATE TABLE IF NOT EXISTS books(title TEXT, author TEXT)'
insert_into_table_sql_statement = "INSERT INTO books VALUES ('Si demain vient', 'Sidney Sheldon'), ('The Lincoln Lawyer', 'Michael Connelly')"
select_from_table_sql_statement = 'SELECT * FROM books'


@contextmanager
def database(path: str):
    connection = sqlite3.connect(path)
    try:
        cursor = connection.cursor()
        yield {'connection': connection, 'cursor': cursor}
    except Exception as e:
        print(f'une erreur s\'est produite : {e}') 
    finally:
        connection.close()


def main():
    database_path = ':memory:'

    with database(database_path) as db:
        db.get('cursor').execute(create_table_sql_statement)
        db.get('connection').commit()

        db.get('cursor').execute(insert_into_table_sql_statement)
        db.get('connection').commit()

        db.get('cursor').execute(select_from_table_sql_statement)

        print(db.get('cursor').fetchall())


if __name__ == '__main__':
    main()

# [('Si demain vient', 'Sidney Sheldon'), ('The Lincoln Lawyer', 'Michael Connelly')]

```

Puisque `db` est un dictionnaire au lieu d'un objet dans ce cas, vous devrez utiliser des crochets ou la méthode `get()` pour accéder à l'objet de connexion ou de curseur.

## Conclusion

Les gestionnaires de contexte en Python sont l'un de ces sujets que beaucoup de programmeurs ont utilisés mais ne comprennent pas clairement.

J'espère que cet article a clarifié certaines de vos confusions.

Si vous souhaitez me contacter, je suis toujours disponible sur [LinkedIn](https://www.linkedin.com/in/farhanhasin/). N'hésitez pas à envoyer un message et je serai heureux de répondre. De plus, si vous pensez que cela a été utile, envisagez d'approuver mes compétences pertinentes sur la plateforme.

Jusqu'à la prochaine, prenez soin de vous et continuez à explorer.