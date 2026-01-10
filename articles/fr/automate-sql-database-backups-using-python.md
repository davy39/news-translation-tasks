---
title: Comment automatiser les sauvegardes de bases de données SQL avec Python
subtitle: ''
author: Jeremiah Oluseye
co_authors: []
series: null
date: '2023-03-16T14:49:50.000Z'
originalURL: https://freecodecamp.org/news/automate-sql-database-backups-using-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/rere.JPG
tags:
- name: Backup
  slug: backup
- name: database
  slug: database
- name: Python
  slug: python
- name: SQL
  slug: sql
seo_title: Comment automatiser les sauvegardes de bases de données SQL avec Python
seo_desc: 'You should back up your SQL database on a regular basis. It''s a critical
  task that helps ensure that your data is always protected.

  But manually backing up a database can be time-consuming and error-prone, especially
  if you have multiple databases to...'
---

Vous devriez sauvegarder régulièrement votre base de données SQL. C'est une tâche cruciale qui permet de s'assurer que vos données sont toujours protégées.

Mais la sauvegarde manuelle d'une base de données peut être chronophage et sujette aux erreurs, surtout si vous avez plusieurs bases de données à sauvegarder.

Dans cet article, nous allons explorer comment automatiser les sauvegardes de bases de données SQL à l'aide de Python, rendant le processus plus rapide, plus facile et moins sujet aux erreurs.

## Prérequis

Avant de commencer, vous devrez avoir installé les éléments suivants :

* Python 3.x
    
* pip
    
* Le package `pyodbc` (pour se connecter aux bases de données SQL)
    
* Le package `pandas` (pour manipuler les données)
    
* Une base de données SQL à sauvegarder
    

## Étape 1 : Comment se connecter à la base de données SQL

La première étape de l'automatisation des sauvegardes de bases de données SQL consiste à se connecter à la base de données à l'aide de Python. Nous utiliserons le package `pyodbc` pour nous connecter à la base de données et exécuter des commandes SQL.

Voici un exemple de segment de code qui se connecte à une base de données SQL Server :

```python
import pyodbc

# Paramètres de connexion
server = 'localhost'
database = 'mydatabase'
username = 'myusername'
password = 'mypassword'

# Créer un objet de connexion
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

# Créer un objet curseur
cursor = conn.cursor()
```

Dans ce code, nous créons un objet de connexion à l'aide de la méthode `pyodbc.connect()` et passons les paramètres de connexion. Nous créons ensuite un objet curseur à l'aide de la méthode `conn.cursor()`, ce qui nous permet d'exécuter des commandes SQL sur la base de données.

## Étape 2 : Comment créer une sauvegarde

Une fois connectés à la base de données, nous pouvons créer une sauvegarde à l'aide de la commande SQL `BACKUP DATABASE`.

Voici un exemple de segment de code qui crée une sauvegarde complète d'une base de données SQL Server :

```python
import os

# Répertoire de sauvegarde
backup_dir = 'C:/backup'

# Nom du fichier de sauvegarde
backup_file = 'mydatabase_backup_' + str(datetime.now().strftime('%Y%m%d_%H%M%S')) + '.bak'

# Commande de sauvegarde
backup_command = 'BACKUP DATABASE mydatabase TO DISK=\'' + os.path.join(backup_dir, backup_file) + '\''

# Exécuter la commande de sauvegarde
cursor.execute(backup_command)
```

Dans ce code, nous spécifions le répertoire et le nom du fichier de sauvegarde et utilisons la méthode `os.path.join()` pour créer un chemin de fichier complet. Nous créons ensuite la commande de sauvegarde à l'aide de la commande SQL `BACKUP DATABASE` et l'exécutons via l'objet curseur.

## Étape 3 : Comment enregistrer les détails de la sauvegarde

Après avoir créé une sauvegarde, il est conseillé d'enregistrer certaines informations sur celle-ci, telles que le nom du fichier de sauvegarde, la date et l'heure de la sauvegarde, ainsi que le nom de la base de données. Nous pouvons enregistrer ces informations dans un fichier CSV à l'aide du package `pandas`.

Voici un exemple de segment de code qui enregistre les détails de la sauvegarde dans un fichier CSV :

```python
import pandas as pd

# Détails de la sauvegarde
backup_details = {'database': [database], 'backup_file': [backup_file], 'backup_datetime': [datetime.now()]}

# Créer un objet DataFrame à partir des détails de la sauvegarde
backup_df = pd.DataFrame(data=backup_details)

# Fichier des détails de la sauvegarde
backup_details_file = os.path.join(backup_dir, 'backup_details.csv')

# Écrire les détails de la sauvegarde dans un fichier CSV
backup_df.to_csv(backup_details_file, index=False)
```

Dans ce code, nous créons un objet dictionnaire contenant les détails de la sauvegarde et créons un objet DataFrame à partir de celui-ci à l'aide de la méthode `pd.DataFrame()`.

Nous spécifions ensuite le fichier des détails de la sauvegarde à l'aide de la méthode `os.path.join()` et écrivons les détails de la sauvegarde dans un fichier CSV à l'aide de la méthode `to_csv()`.

## Étape 4 : Comment automatiser le processus de sauvegarde

Maintenant que nous avons créé une sauvegarde et enregistré ses détails, nous pouvons automatiser le processus de sauvegarde à l'aide d'un script Python. Nous pouvons planifier l'exécution du script à intervalles réguliers à l'aide du Planificateur de tâches Windows intégré ou d'un outil de planification tiers comme CronTab (pour Linux) ou le Planificateur de tâches (pour Mac).

Voici un exemple de script Python qui automatise les sauvegardes de bases de données SQL :

```python
import pyodbc
import os
import pandas as pd
from datetime import datetime

# Paramètres de connexion
server = 'localhost'
database = 'mydatabase'
username = 'myusername'
password = 'mypassword'

# Répertoire de sauvegarde
backup_dir = 'C:/backup'

# Créer un objet de connexion
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

# Créer un objet curseur
cursor = conn.cursor()

# Nom du fichier de sauvegarde
backup_file = 'mydatabase_backup_' + str(datetime.now().strftime('%Y%m%d_%H%M%S')) + '.bak'

# Commande de sauvegarde
backup_command = 'BACKUP DATABASE mydatabase TO DISK=\'' + os.path.join(backup_dir, backup_file) + '\''

# Exécuter la commande de sauvegarde
cursor.execute(backup_command)

# Détails de la sauvegarde
backup_details = {'database': [database], 'backup_file': [backup_file], 'backup_datetime': [datetime.now()]}

# Créer un objet DataFrame à partir des détails de la sauvegarde
backup_df = pd.DataFrame(data=backup_details)

# Fichier des détails de la sauvegarde
backup_details_file = os.path.join(backup_dir, 'backup_details.csv')

# Écrire les détails de la sauvegarde dans un fichier CSV
backup_df.to_csv(backup_details_file, index=False)
```

Dans ce script, nous avons combiné les segments de code précédents en un seul script, ce qui facilite l'automatisation du processus de sauvegarde.

Nous nous connectons d'abord à la base de données, créons une sauvegarde, enregistrons les détails de la sauvegarde dans un fichier CSV, puis nous nous déconnectons de la base de données.

## Conclusion

Automatiser les sauvegardes de bases de données SQL à l'aide de Python est un excellent moyen de gagner du temps, de réduire les risques d'erreurs et de s'assurer que les données sont toujours protégées.

En suivant les étapes décrites dans cet article, vous pouvez facilement automatiser les sauvegardes de bases de données SQL et les planifier pour qu'elles s'exécutent à intervalles réguliers.

N'oubliez pas de tester régulièrement vos sauvegardes pour vous assurer qu'elles fonctionnent correctement et que vous pouvez restaurer les données si nécessaire.

Connectons-nous sur [Twitter](https://twitter.com/Olujerry19) et [Linkedin](https://www.linkedin.com/in/jeremiah-oluseye-58457719a/)