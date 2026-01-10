---
title: Comment analyser les fichiers de configuration INI en Python avec Configparser
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2025-10-17T15:10:37.893Z'
originalURL: https://freecodecamp.org/news/how-to-parse-ini-config-files-in-python-with-configparser
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1760712555277/4eabf2d7-fa9d-445b-8e0a-6ebdee53790c.png
tags:
- name: Python
  slug: python
seo_title: Comment analyser les fichiers de configuration INI en Python avec Configparser
seo_desc: 'Configuration files provide a structured way to manage application settings
  that''s more organized than environment variables alone.

  INI files, short for initialization files, with their simple section-based format,
  are both easy to read and parse. Py...'
---

Les fichiers de configuration offrent un moyen structuré de gérer les paramètres d'application, plus organisé que les seules variables d'environnement.

Les fichiers INI, abréviation de fichiers d'initialisation, avec leur format simple basé sur des sections, sont à la fois faciles à lire et à analyser. Le module intégré de Python [configparser](https://docs.python.org/3/library/configparser.html) rend le travail avec ces fichiers simple et puissant.

Ce tutoriel vous apprendra comment lire et analyser de tels fichiers de configuration `.ini` en utilisant le module `configparser`.

🔗 [**Voici le code sur GitHub**](https://github.com/balapriyac/python-basics/tree/main/config-management-basics/parsing-ini-files).

## Prérequis

Pour suivre ce tutoriel, vous devriez avoir :

* Python 3.7 ou version ultérieure installé sur votre système
    
* Une compréhension de base de la syntaxe Python et des structures de données (dictionnaires, chaînes de caractères)
    
* Une familiarité avec les opérations sur les fichiers en Python
    
* Un éditeur de texte ou un IDE pour écrire du code Python
    
* Des connaissances de base sur les fichiers de configuration et pourquoi ils sont utilisés dans les applications
    

Aucun package externe n'est requis, car nous utiliserons le module intégré `configparser` de Python.

## Table des matières

1. [Comprendre le format de fichier INI](#heading-comprendre-le-format-de-fichier-ini)
    
2. [Utilisation de base de ConfigParser](#heading-utilisation-de-base-de-configparser)
    
3. [Conversion de type et valeurs par défaut](#heading-conversion-de-type-et-valeurs-par-defaut)
    
4. [Comment créer un gestionnaire de configuration simple](#heading-comment-creer-un-gestionnaire-de-configuration-simple)
    
5. [Comment travailler avec plusieurs sections dans les fichiers INI](#heading-comment-travailler-avec-plusieurs-sections-dans-les-fichiers-ini)
    
6. [Comment écrire des fichiers de configuration](#heading-comment-ecrire-des-fichiers-de-configuration)
    

## Comprendre le format de fichier INI

Les fichiers INI organisent la configuration en sections, où chaque section contient des paires clé-valeur. Cette structure est utile pour les applications comportant plusieurs composants ou environnements. Voyons à quoi ressemble un fichier INI avant de l'analyser.

Créez un fichier nommé `app.ini` :

```plaintext
[database]
host = localhost
port = 5432
username = app_user
password = secure_password
pool_size = 10
ssl_enabled = true

[server]
host = 0.0.0.0
port = 8000
debug = false

[logging]
level = INFO
file = app.log
```

Ce fichier contient trois sections : database, server et logging. Chaque section regroupe les paramètres associés, ce qui rend la configuration facile à comprendre et à maintenir.

## Utilisation de base de ConfigParser

Le module `configparser` fournit la classe `ConfigParser`, qui gère tout le travail d'analyse. Voici comment lire et accéder aux valeurs de configuration :

```python
import configparser

config = configparser.ConfigParser()
config.read('app.ini')

# Access values from sections
db_host = config['database']['host']
db_port = config['database']['port']

print(f"Database: {db_host}:{db_port}")
print(f"Sections: {config.sections()}")
```

Ce code montre le flux de travail de base :

* créer un objet `ConfigParser`,
    
* lire votre fichier INI,
    
* puis accéder aux valeurs en utilisant une syntaxe de type dictionnaire.
    

Le premier crochet contient le nom de la section, et le second contient la clé.

Créez le fichier `app.ini` et exécutez le code ci-dessus. Vous devriez voir la sortie suivante :

```plaintext
Database: localhost:5432
Sections: ['database', 'server', 'logging']
```

## Conversion de type et valeurs par défaut

Les valeurs de configuration dans les fichiers INI sont stockées sous forme de chaînes de caractères, mais vous en avez souvent besoin sous forme d'entiers, de booléens ou de flottants. `ConfigParser` fournit des méthodes pratiques pour la conversion de type, comme illustré ici :

```python
import configparser

config = configparser.ConfigParser()
config.read('app.ini')

# Automatic type conversion
db_port = config.getint('database', 'port')
ssl_enabled = config.getboolean('database', 'ssl_enabled')

# With fallback defaults
max_retries = config.getint('database', 'max_retries', fallback=3)
timeout = config.getfloat('database', 'timeout', fallback=30.0)

print(f"Port: {db_port}, SSL: {ssl_enabled}")
```

Dans ce code, les méthodes `getint()`, `getboolean()` et `getfloat()` convertissent les valeurs de type chaîne vers le type approprié. Le paramètre `fallback` fournit une valeur par défaut lorsque la clé n'existe pas, évitant ainsi les erreurs.

Lorsque vous exécutez le code ci-dessus, vous obtiendrez :

```plaintext
Port: 5432, SSL: True
```

## Comment créer un gestionnaire de configuration simple

Une approche pratique consiste à envelopper `ConfigParser` dans une classe qui valide la configuration et offre un accès facile aux paramètres :

```python
import configparser
from pathlib import Path

class ConfigManager:
    def __init__(self, config_file='app.ini'):
        self.config = configparser.ConfigParser()
        
        if not Path(config_file).exists():
            raise FileNotFoundError(f"Config file not found: {config_file}")
        
        self.config.read(config_file)
    
    def get_database_config(self):
        db = self.config['database']
        return {
            'host': db.get('host'),
            'port': db.getint('port'),
            'username': db.get('username'),
            'password': db.get('password'),
            'pool_size': db.getint('pool_size', fallback=5)
        }
```

Cette classe de gestionnaire valide que le fichier existe et fournit des méthodes propres pour accéder à la configuration. Elle renvoie des dictionnaires avec des valeurs correctement typées.

Et vous pouvez l'utiliser comme ceci :

```python
config = ConfigManager('app.ini')
db_config = config.get_database_config()
print(db_config)
```

Cela affiche :

```plaintext
{'host': 'localhost', 'port': 5432, 'username': 'app_user', 'password': 'secure_password', 'pool_size': 10}
```

## Comment travailler avec plusieurs sections dans les fichiers INI

Vous pouvez organiser différentes parties de votre application dans des sections séparées et y accéder indépendamment :

```python
import configparser

config = configparser.ConfigParser()
config.read('app.ini')

# Get all options in a section as a dictionary
db_settings = dict(config['database'])
server_settings = dict(config['server'])

# Check if a section exists
if config.has_section('cache'):
    cache_enabled = config.getboolean('cache', 'enabled')
else:
    cache_enabled = False

print(f"Database settings: {db_settings}")
print(f"Caching enabled: {cache_enabled}")
```

La conversion `dict()` vous donne toutes les paires clé-valeur d'une section en une seule fois. La méthode `has_section()` vous permet de gérer conditionnellement les sections de configuration optionnelles.

L'exécution du code ci-dessus devrait vous donner la sortie suivante :

```plaintext
Database settings: {'host': 'localhost', 'port': '5432', 'username': 'app_user', 'password': 'secure_password', 'pool_size': '10', 'ssl_enabled': 'true'}
Caching enabled: False
```

## Comment écrire des fichiers de configuration

`ConfigParser` peut également créer et modifier des fichiers INI, ce qui est utile pour enregistrer les préférences de l'utilisateur ou générer des modèles de configuration :

```python
import configparser

config = configparser.ConfigParser()

# Add sections and values
config['database'] = {
    'host': 'localhost',
    'port': '5432',
    'username': 'myapp'
}

config['server'] = {
    'host': '0.0.0.0',
    'port': '8000',
    'debug': 'false'
}

# Write to file
with open('generated.ini', 'w') as configfile:
    config.write(configfile)

print("Configuration file created!")
```

Ce code crée un nouveau fichier INI à partir de zéro. La méthode write() enregistre la configuration au format INI approprié avec des sections et des paires clé-valeur.

## Conclusion

Lorsque les variables d'environnement ne suffisent pas et que vous avez besoin de paramètres groupés pour différents composants, les fichiers INI sont votre solution.

Le format est lisible par l'homme, `ConfigParser` gère automatiquement la conversion de type, et il est intégré à la bibliothèque standard de Python. Enveloppez-le dans une classe de configuration pour la validation et des modèles d'accès propres.

Rappelez-vous également :

* Organisez par composant. Utilisez des sections pour regrouper les paramètres associés.
    
* Utilisez les méthodes de conversion de type. Utilisez toujours `getint()`, `getboolean()` et `getfloat()` plutôt qu'une conversion manuelle. Elles gèrent mieux les cas particuliers.
    
* Fournissez des valeurs par défaut judicieuses. Utilisez le paramètre `fallback` pour les paramètres optionnels afin que votre application fonctionne avec une configuration minimale.
    
* Validez tôt. Vérifiez que les sections et les clés requises existent au démarrage avant de tenter de les utiliser.
    
* Gardez les secrets séparés. Ne faites pas de Commit de fichiers INI contenant des mots de passe dans le contrôle de version. Utilisez des fichiers `.ini.example` avec des valeurs fictives comme modèles.
    

Dans le prochain article, vous apprendrez à travailler avec les fichiers TOML en Python. D'ici là, continuez à coder !