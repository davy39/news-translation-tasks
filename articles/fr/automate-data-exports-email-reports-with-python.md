---
title: Comment automatiser les exportations de données et les rapports par e-mail
  avec Python – un guide étape par étape
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2023-10-30T16:08:37.000Z'
originalURL: https://freecodecamp.org/news/automate-data-exports-email-reports-with-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/report-automation.png
tags:
- name: automation
  slug: automation
- name: excel
  slug: excel
- name: postgres
  slug: postgres
- name: Python
  slug: python
seo_title: Comment automatiser les exportations de données et les rapports par e-mail
  avec Python – un guide étape par étape
seo_desc: In today's data-driven world, automation is key to streamlining tasks and
  saving time. In this beginner-friendly tutorial, I'll walk you through the process
  of automating data exports from a PostgreSQL database and sending them as an email
  attachment...
---

Dans le monde actuel axé sur les données, l'automatisation est la clé pour rationaliser les tâches et gagner du temps. Dans ce tutoriel adapté aux débutants, je vais vous guider à travers le processus d'automatisation des exportations de données à partir d'une base de données PostgreSQL et de leur envoi en tant que pièce jointe par e-mail en utilisant Python.

Ce guide étape par étape vous aidera à comprendre les fondamentaux de la manipulation des bases de données, de la manipulation des données et de la communication par e-mail, tout en automatisant ces processus avec un script Python.

## Contexte commercial

Imaginez que vous faites partie d'une organisation où vos managers attendent un rapport hebdomadaire rempli d'informations précieuses. Mais la création de ce rapport est loin d'être une tâche simple.

Pour obtenir les informations dont vous avez besoin, vous devez exécuter manuellement dix requêtes de base de données différentes, rassembler les résultats, puis les compiler méticuleusement dans une feuille de calcul Excel. C'est un processus chronophage et sujet aux erreurs qui peut vous laisser épuisé.

Dans ce scénario, ne serait-ce pas un changement radical si Python pouvait prendre les rênes et gérer l'ensemble de ce processus pour vous ?

Imaginez ceci : chaque semaine, sans aucune intervention manuelle, Python extrait les données requises, les compile dans une feuille Excel bien organisée, et les envoie même à vos managers comme une horloge.

Ce tutoriel vous aidera à apprendre comment faire cela. Je vais vous guider à travers les étapes pour automatiser ce processus, rendant vos rapports hebdomadaires ou mensuels un jeu d'enfant, et vous libérant pour vous concentrer sur des tâches plus critiques.

## Table des matières

1. [Prérequis](#heading-prerequis)
2. [Comment configurer votre environnement virtuel](#heading-comment-configurer-votre-environnement-virtuel)
3. [Comment configurer votre base de données d'exemple](#heading-comment-configurer-votre-base-de-donnees-d-exemple)
4. [Comment configurer la journalisation et les variables d'environnement](#heading-comment-configurer-la-journalisation-et-les-variables-d-environnement)
5. [Comment extraire les données de la base de données](#heading-comment-extraire-les-donnees-de-la-base-de-donnees)
6. [Comment structurer les données de réservation avec la classe `BookingInfo`](#heading-comment-structurer-les-donnees-de-reservation-avec-la-classe-bookinginfo)
7. [Comment convertir les données en une feuille Excel](#heading-comment-convertir-les-donnees-en-une-feuille-excel)
8. [Comment combiner les fonctionnalités](#heading-comment-combiner-les-fonctionnalites)
9. [Comment envoyer un e-mail avec le rapport de données de réservations](#heading-comment-envoyer-un-e-mail-avec-le-rapport-de-donnees-de-reservations)
10. [Comment tester le flux](#heading-comment-tester-le-flux)
11. [Comment planifier l'application](#heading-comment-planifier-l-application)
12. [Conclusion](#heading-conclusion)

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants :

1. Python installé sur votre ordinateur. Vous pouvez télécharger Python depuis [Python.org](https://www.python.org/downloads/).
2. Connaissance de base du langage de programmation Python
3. Familiarité avec [l'envoi d'e-mails en Python](https://blog.ashutoshkrris.in/how-to-send-emails-using-python)
4. PostgreSQL installé sur votre ordinateur. Vous pouvez télécharger PostgreSQL depuis [ici](https://www.postgresql.org/download/).

## Comment configurer votre environnement virtuel

Avant de commencer à coder, vous devrez vous assurer d'avoir tous les outils et bibliothèques nécessaires installés.

Pour garantir que vous avez un environnement propre et isolé, vous allez [créer un environnement virtuel](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/) en utilisant `venv`.

Créez un répertoire de projet et naviguez jusqu'à celui-ci dans le terminal :

```bash
mkdir report-automation
cd report-automation
```

Créez un environnement virtuel nommé `env` en utilisant la commande suivante :

```bash
python -m venv env
```

Python est maintenant livré avec la bibliothèque `venv` préinstallée pour créer des environnements virtuels.

Activez l'environnement virtuel comme ceci :

```bash
source env/bin/activate
```

Note : si vous êtes sur Windows, vous devrez utiliser `source env/Scripts/activate` pour activer l'environnement.

Vous devriez voir `(env)` dans votre prompt de terminal, indiquant que l'environnement virtuel a été activé.

### Comment installer les bibliothèques requises

Maintenant que vous avez créé l'environnement virtuel, vous pouvez installer les bibliothèques suivantes :

* `psycopg2` : Adaptateur Python pour PostgreSQL, permettant aux applications Python d'interagir avec les bases de données PostgreSQL.
* `pandas` : Une bibliothèque versatile de manipulation et d'analyse de données pour Python, idéale pour travailler avec des données structurées.
* `xlsxwriter` : Module Python pour créer et formater des fichiers Excel (XLSX), utile pour générer des rapports et des feuilles de calcul.

Pour installer les bibliothèques, exécutez la commande suivante :

```bash
pip install psycopg2 pandas xlsxwriter
```

## Comment configurer votre base de données d'exemple

Dans cette section, je vais vous guider à travers la configuration d'une base de données de démonstration nommée "airlines" que nous utiliserons tout au long de ce tutoriel. La base de données comprend trois tables : `bookings`, `flights`, et `airports_data`.

Je vais vous fournir un fichier de script SQL nommé `airlines_db.sql` qui crée la base de données et la remplit avec des données d'exemple. Pour configurer la base de données, vous aurez besoin de PostgreSQL installé sur votre système.

### Télécharger et installer la base de données

1. Téléchargez le fichier de script SQL "airlines_db.sql" depuis [ici](https://drive.google.com/file/d/1CPo4ZC8dmuyCetEwpyDa6pfKnpbiqyO3/view?usp=sharing).
2. Ouvrez votre terminal ou invite de commande.
3. Utilisez la commande suivante pour installer la base de données. Assurez-vous d'avoir les outils en ligne de commande PostgreSQL installés et que vous pouvez accéder à la commande `psql`. Remplacez `postgres` par votre nom d'utilisateur PostgreSQL s'il est différent.

```bash
psql -f airlines_db.sql -U postgres
```

Cette commande exécutera le script SQL et créera la base de données "airlines" avec les tables `bookings`, `flights`, et `airports_data`.

### Description du schéma

Le schéma principal de la base de données est `bookings`. Examinons de plus près les tables dans la base de données "airlines" :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-29-115228.png)
_Diagramme de schéma_

#### Table `bookings.bookings`

La table "bookings" est conçue pour stocker des informations cruciales sur les réservations faites pour les vols. Chaque réservation est identifiée de manière unique par le `book_ref`, qui est un champ `character(6)`. Le champ `total_amount` est de type `numeric(10,2)` et représente le coût total de la réservation.

Pour suivre la date et l'heure de la réservation, la table inclut un champ `book_date` de type `bigint`. Cette table sert de dépôt central pour les données de réservation et est essentielle pour suivre les réservations des passagers, les coûts et les dates de réservation.

#### Table `bookings.flights`

La table "flights" est dédiée à la capture de détails complets sur les vols, y compris des informations sur leurs statuts, les heures de départ et d'arrivée prévues et réelles, et d'autres données importantes liées aux vols.

La clé primaire de cette table est le `flight_id`, un identifiant `integer`. Chaque vol est associé à un numéro de vol spécifique désigné par le champ `flight_no`, de type `character(6)`.

Pour comprendre l'origine et la destination du vol, les champs `departure_airport` et `arrival_airport` stockent les codes d'aéroport de départ et d'arrivée en tant que types `character(3)`, respectivement.

Le champ `status` est un `character varying(20)` qui enregistre le statut du vol, qui doit être l'un des suivants : 'On Time', 'Delayed', 'Departed', 'Arrived', 'Scheduled', ou 'Cancelled'. La table inclut également des champs pour les heures de départ et d'arrivée prévues (`scheduled_departure` et `scheduled_arrival`) et les heures de départ et d'arrivée réelles (`actual_departure` et `actual_arrival`).

De plus, cette table établit deux clés étrangères essentielles : `flights_arrival_airport_fkey` et `flights_departure_airport_fkey`, qui lient au `airport_code` dans la table "airports_data". Cela établit des connexions entre les vols et leurs aéroports de départ et d'arrivée respectifs.

#### Table `bookings.airports_data`

La table "airports_data" sert de dépôt pour les données liées aux aéroports et à leurs emplacements géographiques. Chaque aéroport est identifié par un code unique `character(3)` stocké dans le champ `airport_code`, qui sert également de clé primaire.

Le champ `timezone`, de type `text`, enregistre le fuseau horaire spécifique de l'aéroport, fournissant des informations essentielles pour la planification et les opérations. Le champ `airport_name` est de type `character varying` et contient le nom de l'aéroport. De plus, la table inclut le champ `city` en tant que type `character varying`, indiquant la ville dans laquelle l'aéroport est situé.

Ces détails permettent à la table "airports_data" de fournir un aperçu complet des emplacements et des informations des aéroports. Cela sert de référence pour la table "flights" via les clés étrangères `flights_arrival_airport_fkey` et `flights_departure_airport_fkey`, facilitant l'association entre les vols et leurs aéroports de départ et d'arrivée respectifs.

## Comment configurer la journalisation et les variables d'environnement

Dans cette section, nous allons configurer la journalisation pour fournir des messages informatifs et gérer les erreurs tout au long du code. Nous allons également configurer les variables d'environnement pour stocker en toute sécurité les informations sensibles et les paramètres de configuration. Ces pratiques améliorent la lisibilité, la maintenabilité et la sécurité du code.

### Configuration de la journalisation

Nous allons utiliser le module `logging` intégré de Python pour configurer un système de journalisation. La journalisation est essentielle pour suivre le flux d'exécution du code et capturer des informations importantes ou des erreurs.

La méthode `logging.basicConfig` est appelée pour définir le format des messages de journalisation et régler le niveau de journalisation sur `INFO`.

```python
import logging

logging.basicConfig(
    format="%(asctime)s | %(levelname)s : %(message)s", level=logging.INFO
)
```

* **Format** : Le paramètre `format` spécifie le format des messages de journalisation. Dans ce cas, chaque entrée de journal inclut un horodatage, le niveau de journalisation (par exemple, INFO, ERROR) et le message de journalisation réel.
* **Niveaux de journalisation** : Nous définissons le niveau de journalisation sur `INFO`, ce qui signifie que le journal enregistrera les messages d'information. Vous pouvez également utiliser des niveaux de gravité plus élevés, tels que `WARNING` ou `ERROR`, pour des problèmes plus critiques.

Vous pouvez en apprendre davantage sur la journalisation en Python dans [ce tutoriel](https://earthly.dev/blog/logging-in-python/).

### Comment gérer les variables d'environnement

Nous allons créer un fichier `.env` pour gérer les variables d'environnement. Les variables d'environnement sont utilisées pour stocker des informations sensibles et des paramètres de configuration, nous permettant de garder ces données séparées du code.

Dans ce cas, nous définissons des variables d'environnement pour les identifiants de messagerie et les détails de connexion à la base de données.

```
export EMAIL=
export PASSWORD=
export EMAIL_PORT=587
export SMTP_SERVER=smtp.gmail.com
export DB_HOSTNAME=localhost
export DB_NAME=airlines
export DB_PORT=5432
export DB_USERNAME=postgres
export DB_PASSWORD=postgres
```

Voici une description des variables :

* **EMAIL** : L'adresse e-mail à utiliser pour envoyer des e-mails.
* **PASSWORD** : Le mot de passe associé au compte e-mail.
* **EMAIL_PORT** : Le port pour le serveur e-mail (par exemple, serveur SMTP). Le port par défaut est 587 pour la transmission sécurisée des e-mails (TLS/SSL).
* **SMTP_SERVER** : L'adresse du serveur SMTP, souvent spécifique au fournisseur de services e-mail.
* **DB_HOSTNAME** : Le nom d'hôte ou l'adresse IP du serveur de base de données PostgreSQL.
* **DB_NAME** : Le nom de la base de données PostgreSQL.
* **DB_PORT** : Le numéro de port pour se connecter à la base de données (par défaut 5432 pour PostgreSQL).
* **DB_USERNAME** : Le nom d'utilisateur pour l'authentification avec la base de données.
* **DB_PASSWORD** : Le mot de passe pour l'utilisateur de la base de données.

Assurez-vous d'exécuter `source .env` pour charger les variables d'environnement.

En utilisant des variables d'environnement, les données sensibles comme les mots de passe et les identifiants de messagerie peuvent être gardées séparées du code, réduisant le risque d'exposition accidentelle ou d'accès non autorisé. Le code peut accéder à ces variables à l'exécution, assurant la sécurité et la flexibilité de la configuration.

## Comment extraire les données de la base de données

Commençons par définir les configurations de la base de données.

```python
import logging
import os

logging.basicConfig(
    format="%(asctime)s | %(levelname)s : %(message)s", level=logging.INFO
)

DB_CONFIG = {
    "host": os.environ.get("DB_HOSTNAME"),
    "database": os.environ.get("DB_NAME"),
    "user": os.environ.get("DB_USERNAME"),
    "password": os.environ.get("DB_PASSWORD"),
}
```

Le dictionnaire `DB_CONFIG` est utilisé pour stocker les paramètres de configuration pour la connexion à la base de données PostgreSQL. Ces paramètres incluent l'hôte, le nom de la base de données, le nom d'utilisateur et le mot de passe. Ces valeurs peuvent être définies via des variables d'environnement.

### Comment se connecter à la base de données

Avant d'extraire les données de la base de données, nous devons nous connecter à notre base de données. Nous allons utiliser la bibliothèque `psycopg2` pour nous connecter à la base de données PostgreSQL.

Nous allons commencer par définir une classe `DataExporter` qui contiendra des méthodes pour extraire la base de données et générer la feuille Excel.

```python
class DataExporter:
    def __init__(self):
        """Initialiser le DataExporter avec la configuration de la base de données."""
        self.db_config = DB_CONFIG
```

Le constructeur de la classe initialise le `DataExporter` avec la configuration de la base de données stockée dans le dictionnaire `DB_CONFIG`.

Ensuite, définissons une méthode qui se connecte à la base de données.

```python
...
import psycopg2

...

class DataExporter:
    def __init__(self):
        """Initialiser le DataExporter avec la configuration de la base de données."""
        self.db_config = DB_CONFIG

    def __connect_to_database(self) -> None:
        """
        Établir une connexion à la base de données PostgreSQL.

        Lève:
            Exception: Si une connexion à la base de données ne peut pas être établie.
        """
        try:
            self.conn = psycopg2.connect(**self.db_config)
            self.cursor = self.conn.cursor()
            logging.info("Connecté à la base de données")
        except Exception as e:
            logging.error(
                "Échec de la connexion à la base de données avec l'erreur : %s", e)
            raise
```

La méthode privée `__connect_to_database` est responsable de l'établissement d'une connexion à la base de données PostgreSQL. Elle utilise la bibliothèque `psycopg2` pour créer une connexion et un curseur pour exécuter des requêtes SQL. Si la connexion échoue, elle enregistre une erreur et lève une exception.

Vous pouvez en apprendre davantage sur la gestion des exceptions en Python [ici](https://blog.ashutoshkrris.in/exception-handling-in-python).

### Comment récupérer les données de la base de données

Maintenant, nous allons définir une autre méthode privée qui se connecte à la base de données et récupère le nombre total de réservations et le montant total de la base de données.

```python
from datetime import datetime

class DataExporter:
    ...

    def __fetch_from_database(self, start_timestamp, end_timestamp) -> list | None:
        """
        Récupérer les données de réservation de la base de données pour une plage de temps donnée.

        Args:
            start_timestamp (datetime): Le début de la plage de temps.
            end_timestamp (datetime): La fin de la plage de temps.

        Returns:
            list: Une liste contenant les données de réservation (num_bookings, total_amount) ou None si une erreur se produit.
        """
        self.__connect_to_database()
        query = f"""
        SELECT COUNT(*) AS num_bookings, SUM(total_amount) AS total_amount
        FROM bookings
        WHERE book_date >= {int(start_timestamp.timestamp()) * 1000} AND book_date <= {int(end_timestamp.timestamp()) * 1000}
        """
        logging.info(
            "Extraction des données de réservation de la base de données pour start timestamp=%s et end_timestamp=%s",
            start_timestamp,
            end_timestamp,
        )
        result = None
        try:
            self.cursor.execute(query)
            result = list(self.cursor.fetchone())
            result.append(
                f'{start_timestamp.strftime("%d %b, %Y")} - {end_timestamp.strftime("%d %b, %Y")}'
            )
            logging.info(
                "Données de réservation extraites avec succès de la base de données pour start timestamp=%s et end_timestamp=%s",
                start_timestamp,
                end_timestamp,
            )
        except Exception as e:
            logging.error(
                "Erreur survenue lors de l'extraction des données de réservation de la base de données : %s", e
            )
        return result
```

Cette méthode privée récupère les données de réservation de la base de données pour une plage de temps spécifiée.

Elle prend deux objets `datetime` comme arguments, `start_timestamp` et `end_timestamp`. Elle construit également une requête SQL pour récupérer le nombre de réservations et le montant total des réservations pour cette plage de temps.

La requête est exécutée, et si elle réussit, la méthode retourne les données sous forme de tuple. Nous convertissons le tuple en une liste et ajoutons la période pour laquelle les données ont été extraites à la liste. Si une erreur se produit lors de l'interaction avec la base de données, elle enregistre une erreur et retourne `None`.

En utilisant la méthode ci-dessus, vous pouvez extraire les données de réservation pour diverses périodes, qu'il s'agisse d'une semaine, d'un mois, d'une année ou de toute autre période personnalisée de votre choix.

## Comment structurer les données de réservation avec la classe `BookingInfo`

Dans cette section, nous allons définir une classe `BookingInfo` dans `booking_info.py`, qui sert de conteneur structuré pour les données de réservation récupérées de la base de données. La classe encapsule les informations liées aux réservations, ce qui facilite leur manipulation et leur présentation.

```python
from decimal import Decimal


class BookingInfo:
    def __init__(self, data_list: list):
        """
        Initialiser BookingInfo avec les données de la base de données.

        Args:
            data_list (list): Une liste contenant les données de réservation (total_bookings, total_amount, timestamp).

        Note:
            Le total_amount est converti en type Decimal.

        """
        self.__total_bookings, self.__total_amount, self.__timestamp = data_list
        self.__total_amount = Decimal(self.__total_amount) if self.__total_amount else Decimal(0)

    def __str__(self) -> str:
        """
        Retourner une représentation sous forme de chaîne de BookingInfo.

        Returns:
            str: Une chaîne au format "Total Bookings: X, Total Amount: $Y".

        """
        return f"Total Bookings: {self.__total_bookings}, Total Amount: ${self.__total_amount}"

    def get_total_bookings(self) -> int:
        """
        Obtenir le nombre total de réservations.

        Returns:
            int: Le nombre total de réservations.

        """
        return self.__total_bookings

    def get_total_amount(self) -> Decimal:
        """
        Obtenir le montant total des réservations sous forme de Decimal.

        Returns:
            Decimal: Le montant total des réservations.

        """
        return self.__total_amount

    def get_timestamp(self) -> str:
        """
        Obtenir le timestamp associé aux données de réservation.

        Returns:
            str: Le timestamp sous forme de chaîne.

        """
        return self.__timestamp

```

La classe `BookingInfo` est conçue pour organiser et représenter les données de réservation retournées par la base de données. Elle reçoit une liste de valeurs contenant le nombre total de réservations, le montant total des réservations et un timestamp en entrée et convertit le montant total en type Decimal. La classe offre des méthodes pour accéder et présenter ces données de manière structurée.

Le constructeur de la classe `BookingInfo` prend une `data_list` en entrée, qui est censée être une liste contenant les éléments suivants :

* `total_bookings` : Un entier représentant le nombre total de réservations.
* `total_amount` : Une valeur à virgule flottante représentant le montant total des réservations.
* `timestamp` : Un timestamp associé aux données de réservation.

La méthode `__init__` initialise les variables d'instance privées (`__total_bookings`, `__total_amount`, et `__timestamp`) avec les valeurs de la `data_list`. Elle convertit également le `__total_amount` en type décimal pour une gestion précise des valeurs monétaires.

La méthode `__str__` est implémentée pour fournir une représentation sous forme de chaîne de l'objet `BookingInfo`. Elle retourne une chaîne au format "Total Bookings: X, Total Amount: $Y", où `X` est le nombre total de réservations et `Y` est le montant total des réservations formaté en dollars.

### Méthodes Getter

La classe fournit trois méthodes getter pour accéder aux données encapsulées :

* `get_total_bookings()` : Retourne le nombre total de réservations sous forme d'entier.
* `get_total_amount()` : Retourne le montant total des réservations sous forme de type Decimal.
* `get_timestamp()` : Retourne le timestamp associé aux données de réservation sous forme de chaîne.

En encapsulant les données de réservation au sein de la classe `BookingInfo`, le code est plus organisé, lisible et réutilisable. Cette approche structurée simplifie la manipulation des informations de réservation dans toute l'application, la rendant plus intuitive à utiliser et à présenter les données.

## Comment convertir les données en une feuille Excel

Maintenant que vous pouvez récupérer des données de la base de données pour une période spécifique, vous pouvez également générer une feuille Excel basée sur les données extraites.

Pour ce faire, définissons une autre méthode privée pour créer la feuille Excel.

```python
...
import pandas as pd

from booking_info import BookingInfo


...

class DataExporter:

	...

    def __convert_to_excelsheet(self, data: list, sheet_name: str):
        """
        Convertir les données récupérées en une feuille Excel.

        Args:
            data (list): Une liste contenant les données de réservation.
            sheet_name (str): Nom de la feuille Excel à créer.

        Lève:
            ValueError: Si une erreur se produit lors de la conversion des données en une feuille Excel.
        """
        try:
            booking_info = BookingInfo(data)
            data = {
                "": ["Total Bookings", "Total Amount ($)"],
                booking_info.get_timestamp(): [
                    booking_info.get_total_bookings(),
                    booking_info.get_total_amount(),
                ],
            }
            logging.info("Conversion des données en dataframe pandas")
            df = pd.DataFrame(data)
            logging.info("Insertion des données dans la feuille Excel")
            with pd.ExcelWriter(sheet_name, engine="xlsxwriter") as writer:
                df.to_excel(writer, sheet_name="Sheet1", index=False)
            logging.info("Données insérées avec succès dans la feuille Excel")
        except ValueError as e:
            logging.error("Erreur de conversion des données en Excel : %s", e)

```

La méthode `__convert_to_excelsheet` au sein de la classe `DataExporter` est responsable de la structuration et de la conversion des données de réservation extraites en une feuille Excel.

Elle accepte deux paramètres d'entrée. Le premier paramètre, `data`, est censé être une liste contenant des données de réservation spécifiques. Ces données incluent le nombre total de réservations, le montant total des réservations et un timestamp pour lequel les données ont été extraites. Le deuxième paramètre, `sheet_name`, représente le nom souhaité pour la feuille Excel qui contiendra les données formatées.

Un aspect clé de la méthode est la structuration des données. Pour y parvenir, la méthode initie la création d'un objet `BookingInfo`, appelé `booking_info`. L'objet `BookingInfo` fournit une représentation structurée des données de réservation, ce qui simplifie la mise en forme et la présentation ultérieures.

Suite à la création de l'objet `booking_info`, un nouveau dictionnaire appelé `data` est généré. Ce dictionnaire est conçu pour structurer les données dans un format adapté à la conversion en une feuille Excel.

Le dictionnaire se compose de deux paires clé-valeur :

* La première paire utilise une chaîne vide comme clé et contient une liste avec deux valeurs d'en-tête, "Total Bookings" et "Total Amount ($)".
* La deuxième paire utilise le timestamp obtenu de `booking_info.get_timestamp()` comme clé et inclut une liste avec deux éléments : le nombre total de réservations (`booking_info.get_total_bookings()`) et le montant total des réservations (`booking_info.get_total_amount()`).

Ce dictionnaire permet d'insérer les données dans la feuille Excel comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-29-135512.png)
_Feuille Excel d'exemple_

Ensuite, le dictionnaire `data` structuré est converti en un DataFrame pandas, appelé `df`. Les DataFrames sont des structures de données couramment utilisées pour manipuler des données tabulaires en Python. Cette étape rationalise la manipulation et l'exportation des données pour un traitement ou une visualisation ultérieure.

Pour créer la feuille Excel, le code utilise le gestionnaire de contexte `pd.ExcelWriter` avec le moteur "xlsxwriter". Ce gestionnaire de contexte garantit que le fichier Excel est correctement préparé pour l'insertion des données. Le paramètre `sheet_name` est fourni pour spécifier le nom de la feuille dans le fichier Excel.

Les données du DataFrame, `df`, sont ensuite écrites dans la feuille Excel. La méthode `to_excel` est utilisée en conjonction avec l'objet `writer`, et le paramètre `index` est défini sur `False`. Cette configuration spécifique exclut les numéros de ligne par défaut qui sont généralement inclus dans les feuilles Excel.

## Comment combiner les fonctionnalités

Maintenant, écrivons une méthode publique que les utilisateurs peuvent utiliser pour extraire les données de la base de données et convertir les données extraites en un fichier de feuille Excel.

```python
...


class DataExporter:
	
    ...
    
    def generate_excelsheet(
        self,
        start_timestamp: datetime,
        end_timestamp: datetime,
        sheet_name: str = "Bookings Data.xlsx",
    ) -> bool:
        """
        Générer une feuille Excel avec les données de réservation pour une plage de temps spécifiée.

        Args:
            start_timestamp (datetime): Le début de la plage de temps.
            end_timestamp (datetime): La fin de la plage de temps.
            sheet_name (str, optionnel): Nom de la feuille Excel à créer. Par défaut "Bookings Data.xlsx".

        Returns:
            bool: True si la feuille Excel a été générée avec succès, sinon False

        Note:
            Cette méthode journalise les erreurs mais ne lève pas d'exceptions pour éviter de rompre le flux de travail.
        """
        data = self.__fetch_from_database(start_timestamp, end_timestamp)
        if data is not None:
            self.__convert_to_excelsheet(data, sheet_name)
            return True
        else:
            logging.error("Aucune donnée à convertir pour générer la feuille Excel")
            return False

```

Cette méthode accepte plusieurs paramètres, y compris `start_timestamp` et `end_timestamp`, qui définissent le début et la fin de la période pour l'extraction des données. Il y a aussi un paramètre optionnel `sheet_name` qui permet à l'utilisateur de spécifier le nom de la feuille Excel. Par défaut, la feuille est nommée "Bookings Data.xlsx" pour fournir une option par défaut pratique.

Lors de l'exécution, la méthode initie le processus de récupération des données en appelant la méthode `__fetch_from_database`, une méthode privée interne de la classe, avec la plage de temps spécifiée.

Si la récupération des données est réussie et que des données sont disponibles, la méthode procède à l'appel de la méthode `__convert_to_excelsheet`. Cela structure et formate les données pour l'insertion dans la feuille Excel.

Si, en revanche, aucune donnée n'est disponible pour la plage de temps fournie, la méthode journalise un message d'erreur et retourne "False" pour indiquer que la génération de la feuille Excel a échoué.

## Comment envoyer un e-mail avec le rapport de données de réservations

Dans cette section, vous apprendrez comment [utiliser Python pour envoyer un e-mail](https://blog.ashutoshkrris.in/how-to-send-emails-using-python) avec un rapport de données de réservations en pièce jointe.

Créez un fichier `mailer.py` et ajoutez le contenu suivant :

```python
import logging
import os
import smtplib
import ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

logging.basicConfig(
    format="%(asctime)s | %(levelname)s : %(message)s", level=logging.INFO
)

SMTP_SERVER = os.environ.get("SMTP_SERVER")
PORT = os.environ.get("EMAIL_PORT")
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")


def send_email(to_email: str, subject: str, attachment_name: str):
    """
    Envoyer un e-mail avec une pièce jointe au destinataire spécifié.

    Args:
        to_email (str): L'adresse e-mail du destinataire.
        subject (str): Le sujet de l'e-mail.
        attachment_name (str): Le nom de fichier de la pièce jointe.

    Note:
        Cette fonction suppose que le serveur SMTP nécessite un chiffrement TLS.

    Lève:
        smtplib.SMTPException: Si un problème survient lors de l'envoi de l'e-mail.

    """
    message = MIMEMultipart()
    message["From"] = EMAIL
    message["To"] = to_email
    message["Subject"] = subject
    body = "Bonjour,\n\nVeuillez trouver ci-joint votre rapport.\n\nMerci"

    message.attach(MIMEText(body, "plain"))

    with open(attachment_name, "rb") as file:
        part = MIMEBase(
            "application", "vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        part.set_payload(file.read())

    encoders.encode_base64(part)

    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {attachment_name}",
    )

    logging.info(f"Joindre {attachment_name} à l'e-mail")
    message.attach(part)
    text = message.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP(SMTP_SERVER, PORT) as server:
        logging.info(f"Envoi de l'e-mail à {to_email}")
        server.starttls(context=context)
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL, to_email, text)
        logging.info(f"E-mail envoyé avec succès à {to_email}")

```

Comme d'habitude, nous avons configuré le logger et les variables d'environnement dans notre script.

La fonctionnalité principale est encapsulée dans la fonction `send_email`. Cette fonction prend trois paramètres :

1. `to_email` : L'adresse e-mail du destinataire.
2. `subject` : Le sujet de l'e-mail.
3. `attachment_name` : Le nom de fichier de la pièce jointe, qui devrait être le rapport de données de réservations dans ce contexte.

Au sein de la fonction, nous construisons un message e-mail en utilisant la classe `MIMEMultipart`. Ce message inclut l'adresse e-mail de l'expéditeur, l'adresse e-mail du destinataire, le sujet et un corps de texte brut avec un message simple.

Le script permet de joindre le rapport de données de réservations en tant que pièce jointe. Il lit le fichier de pièce jointe, l'encode et l'ajoute au message e-mail. Cela garantit que le destinataire peut facilement accéder et télécharger le rapport de données depuis l'e-mail.

Vous pouvez apprendre comment ajouter des pièces jointes lors de l'envoi d'e-mails en utilisant Python [ici](https://blog.ashutoshkrris.in/how-to-send-emails-using-python#heading-including-attachments).

La fonction `create_default_context` de la bibliothèque `ssl` crée un contexte SSL sécurisé pour la communication par e-mail. Enfin, le script se connecte au serveur SMTP, se connecte en utilisant l'adresse e-mail et le mot de passe de l'expéditeur, envoie l'e-mail et journalise un message de succès après une transmission réussie.

## Comment tester le flux

Testons enfin le flux de l'application.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/finally-about-time.gif)

Dans cette section, nous allons automatiser les rapports mensuels. Créez un fichier `main.py` et ajoutez le contenu suivant :

```python
from exporter import DataExporter
from datetime import datetime
from mailer import send_email

start_timestamp = datetime(2023, 5, 28, 00, 00, 00)  # 28 mai 2023 00:00:00
end_timestamp = datetime(2023, 8, 20, 23, 59, 59)  # 20 août 2023 23:59:59

exporter = DataExporter()
if exporter.generate_excelsheet(
        start_timestamp, end_timestamp, sheet_name="Bookings Data.xlsx"):
    send_email("monemail@gmail.com", "Votre Rapport", "Bookings Data.xlsx")

```

Dans le code ci-dessus, nous créons deux objets timestamp, `start_timestamp` et `end_timestamp`, pour spécifier une plage de temps. Nous avons la date de début définie au 28 mai 2023 à minuit et la date de fin définie au 20 août 2023 juste avant minuit.

Ensuite, nous créons une instance de la classe `DataExporter`, qui gère l'exportation des données et la génération de la feuille Excel. La méthode `generate_excelsheet` de cette instance est appelée avec les timestamps précédemment définis pour créer un rapport lié aux réservations.

Enfin, le code envoie un e-mail avec la feuille Excel générée en pièce jointe en utilisant la fonction `send_email`.

## Comment planifier l'application

Ensuite, notre objectif est d'automatiser le processus de planification des rapports. Nous visons à planifier les livraisons de rapports pour deux scénarios distincts : chaque lundi pour les données de la semaine précédente, et le 1er jour de chaque mois pour les informations du mois précédent.

Pour planifier l'exécution, vous devrez installer la bibliothèque `schedule` :

```bash
pip install schedule
```

Une fois la bibliothèque installée, voici comment vous pouvez automatiser les rapports mensuels et hebdomadaires :

```python
import schedule
from exporter import DataExporter
from datetime import datetime, timedelta
from mailer import send_email


def main():
    today = datetime.now()
    sheet_name = "Bookings Data.xlsx"

    if today.weekday() == 0:  # Vérifier si c'est lundi (0 signifie lundi)
        # C'est lundi, récupérer les données de la semaine précédente (lundi à dimanche)
        start_timestamp = (today - timedelta(days=7)
                           ).replace(hour=0, minute=0, second=0, microsecond=0)
        end_timestamp = (today - timedelta(days=1)
                         ).replace(hour=23, minute=59, second=59, microsecond=0)
        sheet_name = "Rapport Hebdomadaire.xlsx"
    elif today.day == 29:
        # C'est le 1er jour du mois, récupérer les données du mois dernier
        start_timestamp = (today.replace(day=1) - timedelta(days=1)
                           ).replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        end_timestamp = (today.replace(day=1) - timedelta(days=1)
                         ).replace(hour=23, minute=59, second=59, microsecond=0)
        sheet_name = "Rapport Mensuel.xlsx"

    exporter = DataExporter()
    exporter.generate_excelsheet(
        start_timestamp, end_timestamp, sheet_name)

    send_email("votreemail@gmail.com",
               "Votre Rapport", sheet_name)


schedule.every().day.at("00:00").do(main)

while True:
    schedule.run_pending()

```

Le script ci-dessus utilise la bibliothèque `schedule` pour exécuter la fonction `main` quotidiennement à minuit. La fonction `main` calcule les timestamps pour l'extraction des données et la génération de la feuille Excel. Après avoir généré la feuille Excel, le script l'envoie par e-mail à un destinataire spécifié.

Si le script s'exécute un lundi, il se configure pour générer un rapport hebdomadaire. Il calcule les `start_timestamp` et `end_timestamp` pour la semaine précédente. Le `start_timestamp` est défini au lundi précédent à minuit (00:00:00), et le `end_timestamp` est défini au dimanche précédent juste avant minuit (23:59:59). La feuille Excel est nommée "Rapport Hebdomadaire.xlsx".

Le 1er jour du mois, le script se concentre sur la génération d'un rapport mensuel. Il calcule les `start_timestamp` et `end_timestamp` pour couvrir l'ensemble du mois précédent. Le `start_timestamp` est défini au premier jour du mois précédent à minuit (00:00:00), tandis que le `end_timestamp` est défini au dernier jour du mois précédent juste avant minuit (23:59:59). La feuille Excel est nommée "Rapport Mensuel.xlsx".

## Conclusion

Dans ce tutoriel, vous avez appris comment utiliser Python pour automatiser la génération d'un rapport et son envoi aux destinataires par e-mail. J'espère que vous avez trouvé le tutoriel utile !

### Portée future

* Vous pouvez ajouter les destinataires des e-mails dans une base de données et récupérer leur liste à partir de là au lieu de les coder en dur dans le code lui-même. Cela rendra l'application plus configurable.
* Vous pouvez également utiliser des tâches Cron pour automatiser l'exécution du script chaque jour à minuit. Dans ce cas, vous n'aurez pas besoin de la bibliothèque `schedule`.

Voici un lien vers le [Dépôt de Code Github](https://github.com/ashutoshkrris/report-automation).