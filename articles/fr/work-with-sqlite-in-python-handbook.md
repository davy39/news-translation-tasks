---
title: Comment travailler avec SQLite en Python – Un guide pour débutants
date: '2024-10-02T09:44:37.000Z'
author: Ashutosh Krishna
authorURL: https://www.freecodecamp.org/news/author/ashutoshkrris/
originalURL: https://freecodecamp.org/news/work-with-sqlite-in-python-handbook
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1727862097228/24433377-ebb8-49b5-b0ee-5736f629399d.png
tags:
- name: SQLite
  slug: sqlite
- name: Python
  slug: python
- name: database
  slug: database
- name: handbook
  slug: handbook
seo_desc: SQLite is one of the most popular relational database management systems
  (RDBMS). It’s lightweight, meaning that it doesn’t take up much space on your system.
  One of its best features is that it’s serverless, so you don’t need to install or
  manage a ...
---


SQLite est l'un des systèmes de gestion de bases de données relationnelles (SGBDR) les plus populaires. Il est léger, ce qui signifie qu'il ne prend pas beaucoup de place sur votre système. L'une de ses meilleures caractéristiques est qu'il est sans serveur (serverless), vous n'avez donc pas besoin d'installer ou de gérer un serveur séparé pour l'utiliser.

<!-- more -->

Au lieu de cela, il stocke tout dans un simple fichier sur votre ordinateur. Il ne nécessite également aucune configuration, il n'y a donc pas de processus d'installation compliqué, ce qui le rend parfait pour les débutants et les petits projets.

SQLite est un excellent choix pour les applications de petite à moyenne taille car il est facile à utiliser, rapide et peut gérer la plupart des tâches que les bases de données plus importantes peuvent accomplir, mais sans les tracas de la gestion de logiciels supplémentaires. Que vous construisiez un projet personnel ou que vous prototypiez une nouvelle application, SQLite est une option solide pour démarrer rapidement.

Dans ce tutoriel, vous apprendrez à travailler avec SQLite en utilisant Python. Voici ce que nous allons couvrir :

-   [Configuration de votre environnement Python][1]
    
-   [Création d'une base de données SQLite][2]
    
-   [Création de tables de base de données][3]
    
-   [Insertion de données dans une table][4]
    
-   [Interrogation des données][5]
    
-   [Mise à jour et suppression de données][6]
    
-   [Utilisation des transactions][7]
    
-   [Optimisation des performances des requêtes SQLite avec l'indexation][8]
    
-   [Gestion des erreurs et des exceptions][9]
    
-   [Exportation et importation de données [Section Bonus]][10]
    
-   [Conclusion][11]
    

Ce tutoriel est parfait pour tous ceux qui souhaitent s'initier aux bases de données sans se plonger dans des configurations complexes.

## Configuration de votre environnement Python

Avant de travailler avec SQLite, assurons-nous que votre environnement Python est prêt. Voici comment tout configurer.

### Installation de Python

Si vous n'avez pas encore installé Python sur votre système, vous pouvez le télécharger sur le [site officiel de Python][12]. Suivez les instructions d'installation pour votre système d'exploitation (Windows, macOS ou Linux).

Pour vérifier si Python est installé, ouvrez votre terminal (ou invite de commande) et tapez :

```
python --version
```

Cela devrait afficher la version actuelle de Python installée. S'il n'est pas installé, suivez les instructions sur le site Web de Python.

### Installation du module SQLite3

La bonne nouvelle est que SQLite3 est intégré à Python ! Vous n'avez pas besoin de l'installer séparément car il est inclus dans la bibliothèque standard de Python. Cela signifie que vous pouvez commencer à l'utiliser immédiatement sans aucune configuration supplémentaire.

### Création d'un environnement virtuel (Optionnel mais recommandé)

C'est une bonne idée de créer un environnement virtuel pour chaque projet afin de garder vos dépendances organisées. Un environnement virtuel est comme une page blanche où vous pouvez installer des packages sans affecter votre installation globale de Python.

Pour créer un environnement virtuel, suivez ces étapes :

1.  Tout d'abord, ouvrez votre terminal ou invite de commande et naviguez jusqu'au répertoire où vous souhaitez créer votre projet.
    
2.  Exécutez la commande suivante pour créer un environnement virtuel :
    

```
python -m venv env
```

Ici, `env` est le nom de l'environnement virtuel. Vous pouvez le nommer comme vous le souhaitez.

3.  Activez l'environnement virtuel :

```
# Use the command for Windows
env\Scripts\activate

# Use the command for macOS/Linux:
env/bin/activate
```

Après avoir activé l'environnement virtuel, vous remarquerez que l'invite de votre terminal change, affichant le nom de l'environnement virtuel. Cela signifie que vous travaillez maintenant à l'intérieur de celui-ci.

### Installation des bibliothèques nécessaires

Nous aurons besoin de quelques bibliothèques supplémentaires pour ce projet. Plus précisément, nous utiliserons :

-   `pandas` : Il s'agit d'une bibliothèque optionnelle pour manipuler et afficher des données au format tabulaire, utile pour les cas d'utilisation avancés.
    
-   `faker` : Cette bibliothèque nous aidera à générer des données factices, comme des noms et des adresses aléatoires, que nous pourrons insérer dans notre base de données pour les tests.
    

Pour installer `pandas` et `faker`, exécutez simplement les commandes suivantes :

```
pip install pandas faker
```

Cela installe à la fois `pandas` et `faker` dans votre environnement virtuel. Avec cela, votre environnement est configuré et vous êtes prêt à commencer à créer et à gérer votre base de données SQLite en Python !

## Création d'une base de données SQLite

Une base de données est un moyen structuré de stocker et de gérer des données afin qu'elles puissent être facilement consultées, mises à jour et organisées. C'est comme un système de classement numérique qui vous permet de stocker efficacement de grandes quantités de données, que ce soit pour une application simple ou un système plus complexe. Les bases de données utilisent des tables pour organiser les données, avec des lignes et des colonnes représentant les enregistrements individuels et leurs attributs.

### Fonctionnement des bases de données SQLite

Contrairement à la plupart des autres systèmes de bases de données, SQLite est une base de données sans serveur. Cela signifie qu'elle ne nécessite pas la configuration ou la gestion d'un serveur, ce qui la rend légère et facile à utiliser. Toutes les données sont stockées dans un seul fichier sur votre ordinateur, que vous pouvez facilement déplacer, partager ou sauvegarder. Malgré sa simplicité, SQLite est suffisamment puissant pour gérer de nombreuses tâches de base de données courantes et est largement utilisé dans les applications mobiles, les systèmes embarqués et les projets de petite à moyenne envergure.

### Création d'une nouvelle base de données SQLite

Créons une nouvelle base de données SQLite et apprenons à interagir avec elle en utilisant la bibliothèque `sqlite3` de Python.

#### Connexion à la base de données

Puisque `sqlite3` est pré-installé, il vous suffit de l'importer dans votre script Python. Pour créer une nouvelle base de données ou vous connecter à une base existante, nous utilisons la méthode `sqlite3.connect()`. Cette méthode prend le nom du fichier de base de données comme argument. Si le fichier n'existe pas, SQLite le créera automatiquement.

```
import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect('my_database.db')
```

Dans cet exemple, un fichier nommé `my_database.db` est créé dans le même répertoire que votre script. Si le fichier existe déjà, SQLite ouvrira simplement la connexion vers celui-ci.

#### Création d'un curseur

Une fois que vous avez une connexion, l'étape suivante consiste à créer un objet curseur (cursor). Le curseur est responsable de l'exécution des commandes SQL et des requêtes sur la base de données.

```
# Create a cursor object
cursor = connection.cursor()
```

#### Fermeture de la connexion

Après avoir fini de travailler avec la base de données, il est important de fermer la connexion pour libérer les ressources. Vous pouvez fermer la connexion avec la commande suivante :

```
# Close the database connection
connection.close()
```

Cependant, vous ne devez fermer la connexion qu'une fois que vous avez terminé toutes vos opérations.

Lorsque vous exécutez votre script Python, un fichier nommé `my_database.db` sera créé dans votre répertoire de travail actuel. Vous avez maintenant créé avec succès votre première base de données SQLite !

### Utilisation d'un gestionnaire de contexte pour ouvrir et fermer les connexions

Python offre un moyen plus efficace et plus propre de gérer les connexions aux bases de données en utilisant l'instruction `with`, également connue sous le nom de gestionnaire de contexte (context manager). L'instruction `with` ouvre et ferme automatiquement la connexion, garantissant que la connexion est correctement fermée même si une erreur survient pendant les opérations de base de données. Cela élimine le besoin d'appeler manuellement `connection.close()`.

Voici comment vous pouvez utiliser l'instruction `with` pour gérer les connexions aux bases de données :

```
import sqlite3

# Step 1: Use 'with' to connect to the database (or create one) and automatically close it when done
with sqlite3.connect('my_database.db') as connection:

    # Step 2: Create a cursor object to interact with the database
    cursor = connection.cursor()

    print("Database created and connected successfully!")

# No need to call connection.close(); it's done automatically!
```

À partir de maintenant, nous utiliserons l'instruction `with` dans nos prochains exemples de code pour gérer efficacement les connexions aux bases de données. Cela rendra le code plus concis et plus facile à maintenir.

## Création de tables de base de données

Maintenant que nous avons créé une base de données SQLite et que nous nous y sommes connectés, l'étape suivante consiste à créer des tables à l'intérieur de la base de données. Une table est l'endroit où nous stockerons nos données, organisées en lignes (enregistrements) et en colonnes (attributs). Pour cet exemple, nous allons créer une table appelée `Students` pour stocker des informations sur les étudiants, que nous réutiliserons dans les sections suivantes.

Pour créer une table, nous utilisons l'instruction SQL `CREATE TABLE`. Cette commande définit la structure de la table, y compris les noms des colonnes et les types de données pour chaque colonne.

Voici une commande SQL simple pour créer une table `Students` avec les champs suivants :

-   `id` : Un identifiant unique pour chaque étudiant (un entier).
    
-   **name** : Le nom de l'étudiant (texte).
    
-   **age** : L'âge de l'étudiant (un entier).
    
-   **email** : L'adresse e-mail de l'étudiant (texte).
    

La commande SQL pour créer cette table ressemblerait à ceci :

```
CREATE TABLE Students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT
);
```

Nous pouvons exécuter cette commande SQL `CREATE TABLE` en Python en utilisant la bibliothèque `sqlite3`. Voyons comment faire cela.

```
import sqlite3

# Use 'with' to connect to the SQLite database and automatically close the connection when done
with sqlite3.connect('my_database.db') as connection:

    # Create a cursor object
    cursor = connection.cursor()

    # Write the SQL command to create the Students table
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS Students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        email TEXT
    );
    '''

    # Execute the SQL command
    cursor.execute(create_table_query)

    # Commit the changes
    connection.commit()

    # Print a confirmation message
    print("Table 'Students' created successfully!")
```

-   `IF NOT EXISTS` : Cela garantit que la table n'est créée que si elle n'existe pas déjà, évitant ainsi des erreurs si la table a déjà été créée auparavant.
    
-   `connection.commit()` : Cela enregistre (valide) les modifications dans la base de données.
    

Lorsque vous exécutez le code Python ci-dessus, il créera la table `Students` dans le fichier de base de données `my_database.db`. Vous verrez également un message dans le terminal confirmant que la table a été créée avec succès.

Si vous utilisez Visual Studio Code, vous pouvez installer l'extension [SQLite Viewer][13] pour visualiser les bases de données SQLite.

![SQLite Viewer - VS Code Extension](https://cdn.hashnode.com/res/hashnode/image/upload/v1727514353100/522fc6f1-0363-41ca-a76a-b730470cb64a.png)

### Types de données dans SQLite et leur correspondance avec Python

SQLite prend en charge plusieurs types de données, que nous devons comprendre lors de la définition de nos tables. Voici un aperçu rapide des types de données SQLite courants et de leur correspondance avec les types Python :

| Type de données SQLite | Description | Équivalent Python |
| --- | --- | --- |
| **INTEGER** | Nombres entiers | `int` |
| **TEXT** | Chaînes de caractères | `str` |
| **REAL** | Nombres à virgule flottante | `float` |
| **BLOB** | Données binaires (ex: images, fichiers) | `bytes` |
| **NULL** | Représente une absence de valeur | `None` |

Dans notre table `Students` :

-   `id` est de type `INTEGER`, qui correspond au `int` de Python.
    
-   `name` et `email` sont de type `TEXT`, qui correspondent au `str` de Python.
    
-   `age` est également de type `INTEGER`, correspondant au `int` de Python.
    

## Insertion de données dans une table

Maintenant que notre table `Students` est créée, il est temps de commencer à insérer des données dans la base de données. Dans cette section, nous verrons comment insérer des enregistrements uniques et multiples en utilisant Python et SQLite, et comment éviter les problèmes de sécurité courants comme l'injection SQL en utilisant des requêtes paramétrées.

### Insertion d'un seul enregistrement

Pour insérer des données dans la base de données, nous utilisons la commande SQL `INSERT INTO`. Commençons par insérer un seul enregistrement dans notre table `Students`.

Voici la syntaxe SQL de base pour insérer un seul enregistrement :

```
INSERT INTO Students (name, age, email) 
VALUES ('John Doe', 20, 'johndoe@example.com');
```

Cependant, au lieu d'écrire du SQL directement dans notre script Python avec des valeurs codées en dur, nous utiliserons des requêtes paramétrées pour rendre notre code plus sûr et plus flexible. Les requêtes paramétrées aident à prévenir l'injection SQL, une attaque courante où des utilisateurs malveillants peuvent manipuler la requête SQL en transmettant des entrées nuisibles.

Voici comment nous pouvons insérer un seul enregistrement dans la table `Students` en utilisant une requête paramétrée :

```
import sqlite3

# Use 'with' to open and close the connection automatically
with sqlite3.connect('my_database.db') as connection:
    cursor = connection.cursor()

    # Insert a record into the Students table
    insert_query = '''
    INSERT INTO Students (name, age, email) 
    VALUES (?, ?, ?);
    '''
    student_data = ('Jane Doe', 23, 'jane@example.com')

    cursor.execute(insert_query, student_data)

    # Commit the changes automatically
    connection.commit()

    # No need to call connection.close(); it's done automatically!
    print("Record inserted successfully!")
```

Les espaces réservés `?` représentent les valeurs à insérer dans la table. Les valeurs réelles sont passées sous forme de tuple (`student_data`) dans la méthode `cursor.execute()`.

### Insertion de plusieurs enregistrements

Si vous souhaitez insérer plusieurs enregistrements à la fois, vous pouvez utiliser la méthode `executemany()` en Python. Cette méthode prend une liste de tuples, où chaque tuple représente un enregistrement.

Pour rendre notre exemple plus dynamique, nous pouvons utiliser la bibliothèque `Faker` pour générer des données d'étudiants aléatoires. C'est utile pour tester et simuler des scénarios du monde réel.

```
from faker import Faker
import sqlite3

# Initialize Faker
fake = Faker(['en_IN'])

# Use 'with' to open and close the connection automatically
with sqlite3.connect('my_database.db') as connection:
    cursor = connection.cursor()

    # Insert a record into the Students table
    insert_query = '''
    INSERT INTO Students (name, age, email) 
    VALUES (?, ?, ?);
    '''
    students_data = [(fake.name(), fake.random_int(
        min=18, max=25), fake.email()) for _ in range(5)]

    # Execute the query for multiple records
    cursor.executemany(insert_query, students_data)

    # Commit the changes
    connection.commit()

    # Print confirmation message
    print("Fake student records inserted successfully!")
```

Dans ce code :

-   `Faker()` génère des noms, des âges et des e-mails aléatoires pour les étudiants. Le passage de la locale (`[‘en_IN’]`) est optionnel.
    
-   `cursor.executemany()` : Cette méthode nous permet d'insérer plusieurs enregistrements à la fois, ce qui rend le code plus efficace.
    
-   `students_data` : Une liste de tuples où chaque tuple représente les données d'un étudiant.
    

### Gestion des problèmes courants : Injection SQL

L'injection SQL est une vulnérabilité de sécurité où des attaquants peuvent insérer ou manipuler des requêtes SQL en fournissant des entrées nuisibles. Par exemple, un attaquant pourrait essayer d'injecter un code comme `'; DROP TABLE Students; --` pour supprimer la table.

En utilisant des requêtes paramétrées (comme démontré ci-dessus), nous évitons ce problème. Les espaces réservés `?` dans les requêtes paramétrées garantissent que les valeurs d'entrée sont traitées comme des données, et non comme faisant partie de la commande SQL. Cela rend impossible l'exécution de code malveillant.

## Interrogation des données

Maintenant que nous avons inséré des données dans notre table `Students`, apprenons à récupérer ces données. Nous explorerons différentes méthodes pour récupérer des données en Python, notamment `fetchone()`, `fetchall()` et `fetchmany()`.

Pour interroger les données d'une table, nous utilisons l'instruction `SELECT`. Voici une commande SQL simple pour sélectionner toutes les colonnes de la table `Students` :

```
SELECT * FROM Students;
```

Cette commande récupère tous les enregistrements et toutes les colonnes de la table `Students`. Nous pouvons exécuter cette requête `SELECT` en Python et récupérer les résultats.

### Récupération de tous les enregistrements

Voici comment nous pouvons récupérer tous les enregistrements de la table `Students` :

```
import sqlite3

# Use 'with' to connect to the SQLite database
with sqlite3.connect('my_database.db') as connection:

    # Create a cursor object
    cursor = connection.cursor()

    # Write the SQL command to select all records from the Students table
    select_query = "SELECT * FROM Students;"

    # Execute the SQL command
    cursor.execute(select_query)

    # Fetch all records
    all_students = cursor.fetchall()

    # Display results in the terminal
    print("All Students:")
    for student in all_students:
        print(student)
```

Dans cet exemple, la méthode `fetchall()` récupère toutes les lignes renvoyées par la requête sous forme de liste de tuples.

```
All Students:
(1, 'Jane Doe', 23, 'jane@example.com')
(2, 'Bahadurjit Sabharwal', 18, 'tristanupadhyay@example.net')
(3, 'Zayyan Arya', 20, 'yashawinibhakta@example.org')
(4, 'Hemani Shukla', 18, 'gaurikanarula@example.com')
(5, 'Warda Kara', 20, 'npatil@example.net')
(6, 'Mitali Nazareth', 19, 'sparekh@example.org')
```

### Récupération d'un seul enregistrement

Si vous souhaitez ne récupérer qu'un seul enregistrement, vous pouvez utiliser la méthode `fetchone()` :

```
import sqlite3

# Use 'with' to connect to the SQLite database
with sqlite3.connect('my_database.db') as connection:

    # Create a cursor object
    cursor = connection.cursor()

    # Write the SQL command to select all records from the Students table
    select_query = "SELECT * FROM Students;"

    # Execute the SQL command
    cursor.execute(select_query)

    # Fetch one record
    student = cursor.fetchone()

    # Display the result
    print("First Student:")
    print(student)
```

Sortie :

```
First Student:
(1, 'Jane Doe', 23, 'jane@example.com')
```

### Récupération de plusieurs enregistrements

Pour récupérer un nombre spécifique d'enregistrements, vous pouvez utiliser `fetchmany(size)` :

```
import sqlite3

# Use 'with' to connect to the SQLite database
with sqlite3.connect('my_database.db') as connection:

    # Create a cursor object
    cursor = connection.cursor()

    # Write the SQL command to select all records from the Students table
    select_query = "SELECT * FROM Students;"

    # Execute the SQL command
    cursor.execute(select_query)

    # Fetch three records
    three_students = cursor.fetchmany(3)

    # Display results
    print("Three Students:")
    for student in three_students:
        print(student)
```

Sortie :

```
Three Students:
(1, 'Jane Doe', 23, 'jane@example.com')
(2, 'Bahadurjit Sabharwal', 18, 'tristanupadhyay@example.net')
(3, 'Zayyan Arya', 20, 'yashawinibhakta@example.org')
```

### Utilisation de `pandas` pour une meilleure présentation des données

Pour une meilleure présentation des données, nous pouvons utiliser la bibliothèque `pandas` pour créer un `DataFrame` à partir des résultats de notre requête. Cela facilite la manipulation et la visualisation des données.

Voici comment récupérer tous les enregistrements et les afficher sous forme de DataFrame pandas :

```
import sqlite3
import pandas as pd

# Use 'with' to connect to the SQLite database
with sqlite3.connect('my_database.db') as connection:
    # Write the SQL command to select all records from the Students table
    select_query = "SELECT * FROM Students;"

    # Use pandas to read SQL query directly into a DataFrame
    df = pd.read_sql_query(select_query, connection)

# Display the DataFrame
print("All Students as DataFrame:")
print(df)
```

Sortie :

```
All Students as DataFrame:
   id                  name  age                        email
0   1              Jane Doe   23             jane@example.com
1   2  Bahadurjit Sabharwal   18  tristanupadhyay@example.net
2   3           Zayyan Arya   20  yashawinibhakta@example.org
3   4         Hemani Shukla   18    gaurikanarula@example.com
4   5            Warda Kara   20           npatil@example.net
5   6       Mitali Nazareth   19          sparekh@example.org
```

La fonction `pd.read_sql_query()` exécute la requête SQL et renvoie directement les résultats sous forme de DataFrame pandas.

## Mise à jour et suppression de données

Dans cette section, nous apprendrons à mettre à jour des enregistrements existants et à supprimer des enregistrements de notre table `Students` en utilisant des commandes SQL en Python. C'est essentiel pour gérer et maintenir vos données efficacement.

### Mise à jour d'enregistrements existants

Pour modifier des enregistrements existants dans une base de données, nous utilisons la commande SQL `UPDATE`. Cette commande nous permet de changer les valeurs de colonnes spécifiques dans une ou plusieurs lignes en fonction d'une condition spécifiée.

Par exemple, si nous voulons mettre à jour l'âge d'un étudiant, la commande SQL ressemblerait à ceci :

```
UPDATE Students 
SET age = 21 
WHERE name = 'Jane Doe';
```

Maintenant, écrivons le code Python pour mettre à jour l'âge d'un étudiant spécifique dans notre table `Students`.

```
import sqlite3

# Use 'with' to connect to the SQLite database
with sqlite3.connect('my_database.db') as connection:
    cursor = connection.cursor()

    # SQL command to update a student's age
    update_query = '''
    UPDATE Students 
    SET age = ? 
    WHERE name = ?;
    '''

    # Data for the update
    new_age = 21
    student_name = 'Jane Doe'

    # Execute the SQL command with the data
    cursor.execute(update_query, (new_age, student_name))

    # Commit the changes to save the update
    connection.commit()

    # Print a confirmation message
    print(f"Updated age for {student_name} to {new_age}.")
```

Dans cet exemple, nous avons utilisé des requêtes paramétrées pour prévenir l'injection SQL.

### Suppression d'enregistrements de la table

Pour supprimer des enregistrements d'une base de données, nous utilisons la commande SQL `DELETE`. Cette commande nous permet de supprimer une ou plusieurs lignes en fonction d'une condition spécifiée.

Par exemple, si nous voulons supprimer un étudiant nommé 'Jane Doe', la commande SQL ressemblerait à ceci :

```
DELETE FROM Students 
WHERE name = 'Jane Doe';
```

Écrivons le code Python pour supprimer un étudiant spécifique de notre table `Students` en utilisant l'instruction `with`.

```
import sqlite3

# Use 'with' to connect to the SQLite database
with sqlite3.connect('my_database.db') as connection:
    cursor = connection.cursor()

    # SQL command to delete a student
    delete_query = '''
    DELETE FROM Students 
    WHERE name = ?;
    '''

    # Name of the student to be deleted
    student_name = 'Jane Doe'

    # Execute the SQL command with the data
    cursor.execute(delete_query, (student_name,))

    # Commit the changes to save the deletion
    connection.commit()

    # Print a confirmation message
    print(f"Deleted student record for {student_name}.")
```

#### Considérations importantes

-   **Conditions** : Utilisez toujours la clause `WHERE` lors de la mise à jour ou de la suppression d'enregistrements pour éviter de modifier ou de supprimer toutes les lignes de la table. Sans clause `WHERE`, la commande affecte chaque ligne de la table.
    
    ![Mème 357089 lignes affectées](https://cdn.hashnode.com/res/hashnode/image/upload/v1727519069500/f22be4cc-e75f-4492-af01-ed08f31361f3.jpeg)
    
-   **Sauvegarde** : C'est une bonne pratique de sauvegarder votre base de données avant d'effectuer des mises à jour ou des suppressions, surtout dans des environnements de production.
    

## Utilisation des transactions

Une transaction est une séquence d'une ou plusieurs opérations SQL qui sont traitées comme une seule unité de travail. Dans le contexte d'une base de données, une transaction vous permet d'effectuer plusieurs opérations qui soit réussissent toutes, soit échouent toutes. Cela garantit que votre base de données reste dans un état cohérent, même en cas d'erreurs ou de problèmes inattendus.

Par exemple, si vous transférez de l'argent entre deux comptes bancaires, vous voudriez que le débit d'un compte et le crédit sur l'autre réussissent ou échouent ensemble. Si une opération échoue, l'autre ne doit pas être exécutée pour maintenir la cohérence.

### Pourquoi utiliser les transactions ?

1.  **Atomicité** : Les transactions garantissent qu'une série d'opérations est traitée comme une seule unité. Si une opération échoue, aucune des opérations ne sera appliquée à la base de données.
    
2.  **Cohérence** : Les transactions aident à maintenir l'intégrité de la base de données en garantissant que toutes les règles et contraintes sont respectées.
    
3.  **Isolation** : Chaque transaction opère indépendamment des autres, évitant les interférences involontaires.
    
4.  **Durabilité** : Une fois qu'une transaction est validée (commit), les modifications sont permanentes, même en cas de défaillance du système.
    

### Quand utiliser les transactions ?

Vous devriez utiliser des transactions lorsque :

-   Vous effectuez plusieurs opérations liées qui doivent réussir ou échouer ensemble.
    
-   Vous modifiez des données critiques qui nécessitent cohérence et intégrité.
    
-   Vous travaillez avec des opérations qui peuvent potentiellement échouer, comme des transactions financières ou des migrations de données.
    

### Gestion des transactions en Python

Dans SQLite, les transactions sont gérées à l'aide des commandes `BEGIN`, `COMMIT` et `ROLLBACK`. Cependant, lors de l'utilisation du module `sqlite3` en Python, vous gérez généralement les transactions via l'objet de connexion.

##### Démarrer une transaction

Une transaction commence implicitement lorsque vous exécutez une instruction SQL. Pour démarrer une transaction explicitement, vous pouvez utiliser la commande `BEGIN` :

```
cursor.execute("BEGIN;")
```

Cependant, il est généralement inutile de démarrer une transaction manuellement, car SQLite démarre une transaction automatiquement lorsque vous exécutez une instruction SQL.

##### Comment valider (commit) une transaction

Pour enregistrer toutes les modifications effectuées pendant une transaction, vous utilisez la méthode `commit()`. Cela rend toutes les modifications permanentes dans la base de données.

```
connection.commit()
```

Nous avons déjà utilisé la méthode `commit()` dans les exemples fournis ci-dessus.

##### Annuler (rollback) une transaction

Si quelque chose ne va pas et que vous souhaitez annuler les modifications effectuées pendant une transaction, vous pouvez utiliser la méthode `rollback()`. Cela annulera toutes les modifications effectuées depuis le début de la transaction.

```
connection.rollback()
```

### Exemple d'utilisation des transactions en Python

Pour illustrer l'utilisation des transactions dans un scénario réel, nous allons créer une nouvelle table appelée `Customers` pour gérer les comptes clients. Dans cet exemple, nous supposerons que chaque client a un `balance` (solde). Nous ajouterons deux clients à cette table et effectuerons une opération de transfert de fonds entre eux.

Tout d'abord, créons la table `Customers` et insérons deux clients :

```
import sqlite3

# Create the Customers table and add two customers
with sqlite3.connect('my_database.db') as connection:
    cursor = connection.cursor()

    # Create Customers table
    create_customers_table = '''
    CREATE TABLE IF NOT EXISTS Customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        balance REAL NOT NULL
    );
    '''
    cursor.execute(create_customers_table)

    # Insert two customers
    cursor.execute(
        "INSERT INTO Customers (name, balance) VALUES (?, ?);", ('Ashutosh', 100.0))
    cursor.execute(
        "INSERT INTO Customers (name, balance) VALUES (?, ?);", ('Krishna', 50.0))

    connection.commit()
```

Maintenant, effectuons l'opération de transfert de fonds entre Ashutosh et Krishna :

```
import sqlite3


def transfer_funds(from_customer, to_customer, amount):
    with sqlite3.connect('my_database.db') as connection:
        cursor = connection.cursor()

        try:
            # Start a transaction
            cursor.execute("BEGIN;")

            # Deduct amount from the sender
            cursor.execute(
                "UPDATE Customers SET balance = balance - ? WHERE name = ?;", (amount, from_customer))
            # Add amount to the receiver
            cursor.execute(
                "UPDATE Customers SET balance = balance + ? WHERE name = ?;", (amount, to_customer))

            # Commit the changes
            connection.commit()
            print(
                f"Transferred {amount} from {from_customer} to {to_customer}.")

        except Exception as e:
            # If an error occurs, rollback the transaction
            connection.rollback()
            print(f"Transaction failed: {e}")


# Example usage
transfer_funds('Ashutosh', 'Krishna', 80.0)
```

Dans cet exemple, nous avons d'abord créé une table `Customers` et inséré deux clients, Ashutosh avec un solde de 100 € et Krishna avec un solde de 50 €. Nous avons ensuite effectué un transfert de fonds de 80 € d'Ashutosh vers Krishna. En utilisant des transactions, nous garantissons que le débit du compte d'Ashutosh et le crédit du compte de Krishna sont exécutés comme une seule opération atomique, maintenant l'intégrité des données en cas d'erreur. Si le transfert échoue (par exemple, en raison de fonds insuffisants), la transaction sera annulée, laissant les deux comptes inchangés.

## Optimisation des performances des requêtes SQLite avec l'indexation

L'indexation est une technique puissante utilisée dans les bases de données pour améliorer les performances des requêtes. Un index est essentiellement une structure de données qui stocke l'emplacement des lignes en fonction de valeurs de colonnes spécifiques, tout comme l'index à la fin d'un livre vous aide à localiser rapidement un sujet.

Sans index, SQLite doit parcourir toute la table ligne par ligne pour trouver les données pertinentes, ce qui devient inefficace à mesure que l'ensemble de données s'agrandit. En utilisant un index, SQLite peut sauter directement aux lignes dont vous avez besoin, accélérant considérablement l'exécution de la requête.

### Remplissage de la base de données avec des données factices

Pour tester efficacement l'impact de l'indexation, nous avons besoin d'un ensemble de données conséquent. Au lieu d'ajouter manuellement des enregistrements, nous pouvons utiliser la bibliothèque `faker` pour générer rapidement des données factices. Dans cette section, nous allons générer 10 000 enregistrements factices et les insérer dans notre table `Students`. Cela simulera un scénario réel où les bases de données deviennent volumineuses et où les performances des requêtes deviennent importantes.

Nous utiliserons la méthode `executemany()` pour insérer les enregistrements comme ci-dessous :

```
import sqlite3
from faker import Faker

# Initialize the Faker library
fake = Faker(['en_IN'])


def insert_fake_students(num_records):
    """Generate and insert fake student data into the Students table."""
    fake_data = [(fake.name(), fake.random_int(min=18, max=25),
                  fake.email()) for _ in range(num_records)]

    # Use 'with' to handle the database connection
    with sqlite3.connect('my_database.db') as connection:
        cursor = connection.cursor()

        # Insert fake data into the Students table
        cursor.executemany('''
        INSERT INTO Students (name, age, email) 
        VALUES (?, ?, ?);
        ''', fake_data)

        connection.commit()

    print(f"{num_records} fake student records inserted successfully.")


# Insert 10,000 fake records into the Students table
insert_fake_students(10000)
```

En exécutant ce script, 10 000 enregistrements d'étudiants factices seront ajoutés à la table `Students`. Dans la section suivante, nous interrogerons la base de données et comparerons les performances des requêtes avec et sans indexation.

### Interrogation sans index

Dans cette section, nous allons interroger la table `Students` sans aucun index pour observer comment SQLite se comporte lorsqu'aucune optimisation n'est en place. Cela servira de base de comparaison pour les performances lorsque nous ajouterons des index plus tard.

Sans index, SQLite effectue un balayage complet de la table (full table scan), ce qui signifie qu'il doit vérifier chaque ligne de la table pour trouver les résultats correspondants. Pour les petits ensembles de données, c'est gérable, mais à mesure que le nombre d'enregistrements augmente, le temps nécessaire à la recherche augmente considérablement. Voyons cela en action en exécutant une requête `SELECT` de base pour rechercher un étudiant spécifique par son nom et mesurer le temps que cela prend.

Tout d'abord, nous allons interroger la table `Students` en cherchant un étudiant avec un nom spécifique. Nous enregistrerons le temps mis pour exécuter la requête en utilisant le module `time` de Python pour mesurer la performance.

```
import sqlite3
import time


def query_without_index(search_name):
    """Query the Students table by name without an index and measure the time taken."""

    # Connect to the database using 'with'
    with sqlite3.connect('my_database.db') as connection:
        cursor = connection.cursor()

        # Measure the start time
        start_time = time.perf_counter_ns()

        # Perform a SELECT query to find a student by name
        cursor.execute('''
        SELECT * FROM Students WHERE name = ?;
        ''', (search_name,))

        # Fetch all results (there should be only one or a few in practice)
        results = cursor.fetchall()

        # Measure the end time
        end_time = time.perf_counter_ns()

        # Calculate the total time taken
        elapsed_time = (end_time - start_time) / 1000

        # Display the results and the time taken
        print(f"Query completed in {elapsed_time:.5f} microseconds.")
        print("Results:", results)


# Example: Searching for a student by name
query_without_index('Ojasvi Dhawan')
```

Voici le résultat :

```
Query completed in 1578.10000 microseconds.
Results: [(104, 'Ojasvi Dhawan', 21, 'lavanya26@example.com')]
```

En exécutant le script ci-dessus, vous verrez combien de temps il faut pour parcourir la table `Students` sans aucun index. Par exemple, s'il y a 10 000 enregistrements dans la table, la requête pourrait prendre entre 1 000 et 2 000 microsecondes selon la taille de la table et votre matériel. Cela peut ne pas sembler trop lent pour un petit ensemble de données, mais les performances se dégraderont à mesure que davantage d'enregistrements seront ajoutés.

Nous utilisons `time.perf_counter_ns()` pour mesurer le temps mis pour l'exécution de la requête en nanosecondes. Cette méthode est très précise pour comparer de petits intervalles de temps. Nous convertissons le temps en microsecondes (`us`) pour une meilleure lisibilité.

### Présentation du plan de requête

Lorsque vous travaillez avec des bases de données, comprendre comment les requêtes sont exécutées peut vous aider à identifier les goulots d'étranglement de performance et à optimiser votre code. SQLite fournit un outil utile pour cela appelé `EXPLAIN QUERY PLAN`, qui vous permet d'analyser les étapes que SQLite suit pour récupérer les données.

Dans cette section, nous allons introduire l'utilisation de `EXPLAIN QUERY PLAN` pour visualiser et comprendre le fonctionnement interne d'une requête — plus précisément, comment SQLite effectue un balayage complet de la table lorsqu'aucun index n'est présent.

Utilisons `EXPLAIN QUERY PLAN` pour voir comment SQLite récupère les données de la table `Students` sans aucun index. Nous chercherons un étudiant par son nom, et le plan de requête révélera les étapes que SQLite suit pour trouver les lignes correspondantes.

```
import sqlite3


def explain_query(search_name):
    """Explain the query execution plan for a SELECT query without an index."""

    with sqlite3.connect('my_database.db') as connection:
        cursor = connection.cursor()

        # Use EXPLAIN QUERY PLAN to analyze how the query is executed
        cursor.execute('''
        EXPLAIN QUERY PLAN
        SELECT * FROM Students WHERE name = ?;
        ''', (search_name,))

        # Fetch and display the query plan
        query_plan = cursor.fetchall()

        print("Query Plan:")
        for step in query_plan:
            print(step)


# Example: Analyzing the query plan for searching by name
explain_query('Ojasvi Dhawan')
```

Lorsque vous exécutez ce code, SQLite renverra une décomposition de la manière dont il prévoit d'exécuter la requête. Voici un exemple de ce à quoi pourrait ressembler la sortie :

```
Query Plan:
(2, 0, 0, 'SCAN Students')
```

Cela indique que SQLite scanne toute la table `Students` (un balayage complet de la table) pour trouver les lignes où la colonne `name` correspond à la valeur fournie (`Ojasvi Dhawan`). Puisqu'il n'y a pas d'index sur la colonne `name`, SQLite doit examiner chaque ligne de la table.

### Création d'un index

La création d'un index sur une colonne permet à SQLite de trouver les lignes plus rapidement lors des opérations de requête. Au lieu de scanner toute la table, SQLite peut utiliser l'index pour sauter directement aux lignes concernées, ce qui accélère considérablement les requêtes — en particulier celles impliquant de grands ensembles de données.

Pour créer un index, utilisez la commande SQL suivante :

```
CREATE INDEX IF NOT EXISTS index-name ON table (column(s));
```

Dans cet exemple, nous allons créer un index sur la colonne `name` de la table `Students`. Voici comment vous pouvez le faire en utilisant Python :

```
import sqlite3
import time


def create_index():
    """Create an index on the name column of the Students table."""
    with sqlite3.connect('my_database.db') as connection:
        cursor = connection.cursor()

        # SQL command to create an index on the name column
        create_index_query = '''
        CREATE INDEX IF NOT EXISTS idx_name ON Students (name);
        '''

        # Measure the start time
        start_time = time.perf_counter_ns()

        # Execute the SQL command to create the index
        cursor.execute(create_index_query)

        # Measure the start time
        end_time = time.perf_counter_ns()

        # Commit the changes
        connection.commit()

        print("Index on 'name' column created successfully!")

        # Calculate the total time taken
        elapsed_time = (end_time - start_time) / 1000

        # Display the results and the time taken
        print(f"Query completed in {elapsed_time:.5f} microseconds.")


# Call the function to create the index
create_index()
```

Sortie :

```
Index on 'name' column created successfully!
Query completed in 102768.60000 microseconds.
```

Même si la création de l'index prend ce temps (102 768,6 microsecondes), c'est une opération ponctuelle. Vous obtiendrez toujours un gain de vitesse substantiel lors de l'exécution de multiples requêtes. Dans les sections suivantes, nous interrogerons à nouveau la base de données pour observer les améliorations de performance rendues possibles par cet index.

### Interrogation avec des index

Dans cette section, nous allons effectuer la même requête `SELECT` que précédemment, mais cette fois nous profiterons de l'index que nous avons créé sur la colonne `name` de la table `Students`. Nous mesurerons et enregistrerons le temps d'exécution pour observer les améliorations de performance fournies par l'index.

```
import sqlite3
import time


def query_with_index(student_name):
    """Query the Students table using an index on the name column."""
    with sqlite3.connect('my_database.db') as connection:
        cursor = connection.cursor()

        # SQL command to select a student by name
        select_query = 'SELECT * FROM Students WHERE name = ?;'

        # Measure the execution time
        start_time = time.perf_counter_ns()  # Start the timer

        # Execute the query with the provided student name
        cursor.execute(select_query, (student_name,))
        result = cursor.fetchall()  # Fetch all results

        end_time = time.perf_counter_ns()  # End the timer

        # Calculate the elapsed time in microseconds
        execution_time = (end_time - start_time) / 1000

        # Display results and execution time
        print(f"Query result: {result}")
        print(f"Execution time with index: {execution_time:.5f} microseconds")


# Example: Searching for a student by name
query_with_index('Ojasvi Dhawan')
```

Voici ce que nous obtenons en sortie :

```
Query result: [(104, 'Ojasvi Dhawan', 21, 'lavanya26@example.com')]
Execution time with index: 390.70000 microseconds
```

Nous pouvons observer une réduction significative du temps d'exécution par rapport au moment où la requête était effectuée sans index.

Analysons le plan d'exécution de la requête pour la requête avec l'index sur la colonne `name` de la table `Students`. Si vous exécutez à nouveau le même script pour expliquer la requête, vous obtiendrez la sortie ci-dessous :

```
Query Plan:
(3, 0, 0, 'SEARCH Students USING INDEX idx_name (name=?)')
```

Le plan montre maintenant que la requête utilise l'index `idx_name`, réduisant considérablement le nombre de lignes à scanner, ce qui conduit à une exécution plus rapide de la requête.

### Comparaison des résultats de performance

Résumons maintenant les résultats de performance que nous avons obtenus lors de l'interrogation avec et sans index.

#### Comparaison du temps d'exécution

| Type de requête | Temps d'exécution (microsecondes) |
| --- | --- |
| Sans index | 1578.1 |
| Avec index | 390.7 |

#### Résumé de l'amélioration des performances

-   La requête avec l'index est environ 4,04 fois plus rapide que la requête sans l'index.
    
-   Le temps d'exécution s'est amélioré d'environ 75,24 % après l'ajout de l'index.
    

### Bonnes pratiques pour l'utilisation des index

Les index peuvent améliorer considérablement les performances de votre base de données SQLite, mais ils doivent être utilisés avec discernement. Voici quelques bonnes pratiques à considérer :

#### Quand et pourquoi utiliser des index

1.  **Colonnes fréquemment interrogées** : Utilisez des index sur les colonnes qui sont fréquemment utilisées dans les requêtes `SELECT`, en particulier celles utilisées dans les clauses `WHERE`, `JOIN` et `ORDER BY`. En effet, l'indexation de ces colonnes peut réduire considérablement le temps d'exécution des requêtes.
    
2.  **Contraintes d'unicité** : Lorsque vous avez des colonnes qui doivent contenir des valeurs uniques (comme des noms d'utilisateur ou des adresses e-mail), la création d'un index peut appliquer cette contrainte efficacement.
    
3.  **Grands ensembles de données** : Pour les tables avec un grand nombre d'enregistrements, les index deviennent de plus en plus bénéfiques. Ils permettent des recherches rapides, ce qui est essentiel pour maintenir les performances à mesure que vos données augmentent.
    
4.  **Index composites** : Envisagez de créer des index composites pour les requêtes qui filtrent ou trient par plusieurs colonnes. Par exemple, si vous recherchez souvent des étudiants par `name` et `age`, un index sur les deux colonnes peut optimiser ces requêtes.
    

#### Inconvénients potentiels des index

Bien que les index offrent des avantages significatifs, il existe certains inconvénients potentiels :

1.  **Opérations d'insertion/mise à jour plus lentes** : Lorsque vous insérez ou mettez à jour des enregistrements dans une table avec des index, SQLite doit également mettre à jour l'index, ce qui peut ralentir ces opérations. En effet, chaque insertion ou mise à jour nécessite une surcharge supplémentaire pour maintenir la structure de l'index.
    
2.  **Besoins de stockage accrus** : Les index consomment de l'espace disque supplémentaire. Pour les grandes tables, le coût de stockage peut être substantiel. Tenez-en compte lors de la conception de votre schéma de base de données, en particulier pour les systèmes aux ressources de stockage limitées.
    
3.  **Gestion complexe des index** : Avoir trop d'index peut compliquer la gestion de la base de données. Cela peut conduire à des situations où vous avez des index redondants, ce qui peut dégrader les performances plutôt que de les améliorer. Examiner et optimiser régulièrement vos index est une bonne pratique.
    

Les index sont des outils puissants pour optimiser les requêtes de base de données, mais ils nécessitent une réflexion approfondie. Trouver un équilibre entre l'amélioration des performances de lecture et la surcharge potentielle sur les opérations d'écriture est essentiel. Voici quelques stratégies pour atteindre cet équilibre :

-   **Surveiller les performances des requêtes** : Utilisez `EXPLAIN QUERY PLAN` de SQLite pour analyser comment vos requêtes se comportent avec et sans index. Cela peut aider à identifier quels index sont bénéfiques et lesquels peuvent être inutiles.
    
-   **Maintenance régulière** : Examinez périodiquement vos index et évaluez s'ils sont toujours nécessaires. Supprimez les index redondants ou rarement utilisés pour rationaliser les opérations de votre base de données.
    
-   **Tester et évaluer** : Avant d'implémenter des index dans un environnement de production, effectuez des tests approfondis pour comprendre leur impact sur les opérations de lecture et d'écriture.
    

En suivant ces bonnes pratiques, vous pouvez tirer parti des avantages de l'indexation tout en minimisant les inconvénients potentiels, améliorant ainsi les performances et l'efficacité de votre base de données SQLite.

## Gestion des erreurs et des exceptions

Dans cette section, nous verrons comment gérer les erreurs et les exceptions lors du travail avec SQLite en Python. Une gestion appropriée des erreurs est cruciale pour maintenir l'intégrité de votre base de données et garantir que votre application se comporte de manière prévisible.

### Erreurs courantes dans les opérations SQLite

Lors de l'interaction avec une base de données SQLite, plusieurs erreurs courantes peuvent survenir :

1.  **Violations de contraintes** : Cela se produit lorsque vous essayez d'insérer ou de mettre à jour des données qui violent une contrainte de base de données, telle que l'unicité de la clé primaire ou les contraintes de clé étrangère. Par exemple, essayer d'insérer une clé primaire en double déclenchera une erreur.
    
2.  **Incompatibilités de types de données** : Tenter d'insérer des données du mauvais type (par exemple, insérer une chaîne de caractères là où un nombre est attendu) peut entraîner une erreur.
    
3.  **Erreurs de base de données verrouillée** : Si une base de données est en cours d'écriture par un autre processus ou une autre connexion, essayer d'y accéder peut entraîner une erreur "database is locked".
    
4.  **Erreurs de syntaxe** : Des erreurs dans votre syntaxe SQL entraîneront des erreurs lorsque vous essaierez d'exécuter vos commandes.
    

### Utilisation de la gestion des exceptions de Python

Les mécanismes de [gestion des exceptions][14] intégrés à Python (`try` et `except`) sont essentiels pour gérer les erreurs dans les opérations SQLite. En utilisant ces constructions, vous pouvez intercepter les exceptions et répondre de manière appropriée sans faire planter votre programme.

Voici un exemple de base sur la façon de gérer les erreurs lors de l'insertion de données dans la base de données :

```
import sqlite3


def add_customer_with_error_handling(name, balance):
    """Add a new customer with error handling."""
    try:
        with sqlite3.connect('my_database.db') as connection:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO Customers (name, balance) VALUES (?, ?);", (name, balance))
            connection.commit()
            print(f"Added customer: {name} with balance: {balance}")

    except sqlite3.IntegrityError as e:
        print(f"Error: Integrity constraint violated - {e}")

    except sqlite3.OperationalError as e:
        print(f"Error: Operational issue - {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage
add_customer_with_error_handling('Vishakha', 100.0)  # Valid
add_customer_with_error_handling('Vishakha', 150.0)  # Duplicate entry
```

Dans cet exemple :

-   Nous interceptons `IntegrityError`, qui est levée pour des violations telles que les contraintes d'unicité.
    
-   Nous interceptons `OperationalError` pour les problèmes généraux liés à la base de données (comme les erreurs de base de données verrouillée).
    
-   Nous avons également un bloc `except` générique pour gérer toutes les exceptions inattendues.
    

Sortie :

```
Added customer: Vishakha with balance: 100.0
Error: Integrity constraint violated - UNIQUE constraint failed: Customers.name
```

### Bonnes pratiques pour garantir l'intégrité de la base de données

1.  **Utiliser des transactions** : Utilisez toujours des transactions (comme discuté dans la section précédente) lorsque vous effectuez plusieurs opérations liées. Cela permet de s'assurer que soit toutes les opérations réussissent, soit aucune ne réussit, maintenant ainsi la cohérence.
    
2.  **Valider les données d'entrée** : Avant d'exécuter des commandes SQL, validez les données d'entrée pour vous assurer qu'elles répondent aux critères attendus (par exemple, types corrects, plages autorisées).
    
3.  **Intercepter des exceptions spécifiques** : Interceptez toujours des exceptions spécifiques pour gérer différents types d'erreurs de manière appropriée. Cela permet une gestion des erreurs et un débogage plus clairs.
    
4.  **Journaliser les erreurs** : Au lieu de simplement imprimer les erreurs sur la console, envisagez de les consigner dans un fichier ou un système de surveillance. Cela vous aidera à suivre les problèmes en production.
    
5.  **Dégradation progressive** : Concevez votre application pour gérer les erreurs avec élégance. Si une opération échoue, fournissez un retour significatif à l'utilisateur plutôt que de faire planter l'application.
    
6.  **Sauvegarder régulièrement les données** : Sauvegardez régulièrement votre base de données pour éviter la perte de données en cas de défaillances critiques ou de corruption.
    
7.  **Utiliser des requêtes préparées** : Les requêtes préparées aident à prévenir les attaques par injection SQL et peuvent également offrir de meilleures performances pour les requêtes répétées.
    

## Exportation et importation de données [Section Bonus]

Dans cette section, nous apprendrons comment exporter des données d'une base de données SQLite vers des formats courants tels que CSV et JSON, ainsi que comment importer des données dans SQLite à partir de ces formats en utilisant Python. C'est utile pour le partage de données, la sauvegarde et l'intégration avec d'autres applications.

### Exportation de données de SQLite vers CSV

L'exportation de données vers un fichier CSV (Comma-Separated Values) est simple avec les bibliothèques intégrées de Python. Les fichiers CSV sont largement utilisés pour le stockage et l'échange de données, ce qui en fait un format pratique pour l'exportation.

Voici comment exporter des données d'une table SQLite vers un fichier CSV :

```
import sqlite3
import csv

def export_to_csv(file_name):
    """Export data from the Customers table to a CSV file."""
    with sqlite3.connect('my_database.db') as connection:
        cursor = connection.cursor()

        # Execute a query to fetch all customer data
        cursor.execute("SELECT * FROM Customers;")
        customers = cursor.fetchall()

        # Write data to CSV
        with open(file_name, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['ID', 'Name', 'Balance'])  # Writing header
            csv_writer.writerows(customers)  # Writing data rows

        print(f"Data exported successfully to {file_name}.")

# Example usage
export_to_csv('customers.csv')
```

### Exportation de données vers JSON

De même, vous pouvez exporter des données vers un fichier [JSON][15] (JavaScript Object Notation), qui est un format populaire pour l'échange de données, en particulier dans les applications Web.

Voici un exemple de la façon d'exporter des données vers JSON :

```
import json
import sqlite3


def export_to_json(file_name):
    """Export data from the Customers table to a JSON file."""
    with sqlite3.connect('my_database.db') as connection:
        cursor = connection.cursor()

        # Execute a query to fetch all customer data
        cursor.execute("SELECT * FROM Customers;")
        customers = cursor.fetchall()

        # Convert data to a list of dictionaries
        customers_list = [{'ID': customer[0], 'Name': customer[1],
                           'Balance': customer[2]} for customer in customers]

        # Write data to JSON
        with open(file_name, 'w') as json_file:
            json.dump(customers_list, json_file, indent=4)

        print(f"Data exported successfully to {file_name}.")


# Example usage
export_to_json('customers.json')
```

### Importation de données dans SQLite depuis CSV

Vous pouvez également importer des données d'un fichier CSV dans une base de données SQLite. C'est utile pour remplir votre base de données avec des ensembles de données existants.

Voici comment importer des données d'un fichier CSV :

```
import csv
import sqlite3


def import_from_csv(file_name):
    """Import data from a CSV file into the Customers table."""
    with sqlite3.connect('my_database.db') as connection:
        cursor = connection.cursor()

        # Open the CSV file for reading
        with open(file_name, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)  # Skip the header row

            # Insert each row into the Customers table
            for row in csv_reader:
                cursor.execute(
                    "INSERT INTO Customers (name, balance) VALUES (?, ?);", (row[1], row[2]))

        connection.commit()
        print(f"Data imported successfully from {file_name}.")


# Example usage
import_from_csv('customer_data.csv')
```

### Importation de données dans SQLite depuis JSON

De même, l'importation de données à partir d'un fichier JSON est simple. Vous pouvez lire le fichier JSON et insérer les données dans votre table SQLite.

Voici comment faire :

```
import json
import sqlite3


def import_from_json(file_name):
    """Import data from a JSON file into the Customers table."""
    with sqlite3.connect('my_database.db') as connection:
        cursor = connection.cursor()

        # Open the JSON file for reading
        with open(file_name, 'r') as json_file:
            customers_list = json.load(json_file)

            # Insert each customer into the Customers table
            for customer in customers_list:
                cursor.execute("INSERT INTO Customers (name, balance) VALUES (?, ?);", (customer['Name'], customer['Balance']))

        connection.commit()
        print(f"Data imported successfully from {file_name}.")


# Example usage
import_from_json('customer_data.json')
```

## Conclusion

Et voilà, c'est terminé ! Ce guide vous a présenté les bases du travail avec SQLite en Python, couvrant tout, de la configuration de votre environnement à l'interrogation et à la manipulation des données, ainsi qu'à l'exportation et à l'importation d'informations. J'espère que vous l'avez trouvé utile et qu'il a suscité votre intérêt pour l'utilisation de SQLite dans vos projets.

Il est maintenant temps de mettre vos nouvelles connaissances en pratique ! Je vous encourage à créer votre propre projet en utilisant SQLite et Python. Qu'il s'agisse d'une application simple pour gérer votre bibliothèque, d'un outil de budgétisation ou de quelque chose d'unique, les possibilités sont infinies.

Une fois votre projet terminé, partagez-le sur Twitter et taguez-moi ! J'adorerais voir ce que vous avez créé et célébrer vos réussites.

Vous pouvez trouver tout le code de ce tutoriel sur [GitHub][16]. Merci d'avoir suivi ce guide, et bon codage !

> Générez gratuitement une table des matières pour vos articles freeCodeCamp en utilisant l'outil [TOC Generator][17].

[1]: #heading-configuration-de-votre-environnement-python
[2]: #heading-creation-d-une-base-de-donnees-sqlite
[3]: #heading-creation-de-tables-de-base-de-donnees
[4]: #heading-insertion-de-donnees-dans-une-table
[5]: #heading-interrogation-des-donnees
[6]: #heading-mise-a-jour-et-suppression-de-donnees
[7]: #heading-utilisation-des-transactions
[8]: #heading-optimisation-des-performances-des-requetes-sqlite-avec-l-indexation
[9]: #heading-gestion-des-erreurs-et-des-exceptions
[10]: #heading-exportation-et-importation-de-donnees-section-bonus
[11]: #heading-conclusion
[12]: https://www.python.org/downloads/
[13]: https://marketplace.visualstudio.com/items?itemName=qwtel.sqlite-viewer
[14]: https://blog.ashutoshkrris.in/exception-handling-in-python
[15]: https://blog.ashutoshkrris.in/a-beginners-guide-to-the-json-module-in-python
[16]: https://github.com/ashutoshkrris/sqlite-tutorial
[17]: https://toc-generator.ashutoshkrris.in/freecodecamp