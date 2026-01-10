---
title: Comment travailler avec les fichiers TOML en Python
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2025-10-24T19:50:44.361Z'
originalURL: https://freecodecamp.org/news/how-to-work-with-toml-files-in-python
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1761335431619/2d4fefec-cdbb-4146-ae9c-24468b483278.png
tags:
- name: Python
  slug: python
seo_title: Comment travailler avec les fichiers TOML en Python
seo_desc: 'TOML (Tom''s Obvious Minimal Language) has become the modern standard for
  configuration files in Python projects. It''s more expressive than INI files and
  cleaner than JSON or YAML.

  Since Python 3.11, the standard library includes the tomllib module fo...'
---

TOML (Tom's Obvious Minimal Language) est devenu le standard moderne pour les fichiers de configuration dans les projets Python. Il est plus expressif que les fichiers INI et plus propre que JSON ou YAML.

Depuis Python 3.11, la bibliothèque standard inclut le module [tomllib](https://docs.python.org/3/library/tomllib.html) pour lire et analyser les fichiers TOML. TOML offre plusieurs avantages par rapport aux autres formats de configuration. Il supporte des types de données complexes comme les tableaux et les tables imbriquées tout en restant lisible par l'homme. De nombreux projets Python, dont [Poetry](https://python-poetry.org/) et [setuptools](https://pypi.org/project/setuptools/), utilisent `pyproject.toml` pour la configuration.

Dans ce tutoriel, nous allons apprendre à analyser les fichiers TOML en Python.

🔗 [**Voici le code sur GitHub**](https://github.com/balapriyac/python-basics/tree/main/config-management-basics/parsing-toml-files).

## Prérequis

Pour suivre ce tutoriel, vous aurez besoin de :

* **Python 3.11 ou supérieur** : Le module `tomllib` fait partie de la bibliothèque standard à partir de Python 3.11
    
* **Connaissances de base en Python** : Familiarité avec les dictionnaires, les file I/O et la syntaxe de base
    
* **Un éditeur de texte ou un IDE** : N'importe quel éditeur pour créer et modifier des fichiers TOML et Python
    

## Table des matières

1. [Comprendre le format TOML](#heading-comprendre-le-format-toml)
    
2. [Comment lire des fichiers TOML avec tomllib](#heading-comment-lire-des-fichiers-toml-avec-tomllib)
    
3. [Comment travailler avec les types de données TOML](#heading-comment-travailler-avec-les-types-de-donnees-toml)
    
4. [Comment construire un gestionnaire de configuration TOML](#heading-comment-construire-un-gestionnaire-de-configuration-toml)
    
5. [Comment gérer les valeurs manquantes en toute sécurité](#heading-comment-gerer-les-valeurs-manquantes-en-toute-securite)
    

## Comprendre le format TOML

Les fichiers TOML organisent les données en tables (similaires aux sections INI) mais avec des fonctionnalités plus puissantes. Créons un exemple de configuration pour comprendre la syntaxe.

Créez `config.toml` :

```plaintext
# Application configuration
title = "My Application"
version = "1.0.0"

[database]
host = "localhost"
port = 5432
username = "app_user"
password = "secure_password"
databases = ["myapp_db", "myapp_cache"]
pool_size = 10
ssl_enabled = true

[server]
host = "0.0.0.0"
port = 8000
debug = false
allowed_hosts = ["localhost", "127.0.0.1", "example.com"]

[logging]
level = "INFO"
format = "%(asctime)s - %(levelname)s - %(message)s"
handlers = ["console", "file"]

[cache]
enabled = true
ttl = 3600
max_size = 1000

[features]
enable_api = true
enable_webhooks = false
rate_limit = 100
```

Ce fichier TOML présente des caractéristiques clés : des paires clé-valeur simples, des tables (sections entre crochets), des tableaux (crochets avec des valeurs séparées par des virgules) et différents types de données, notamment des chaînes de caractères, des entiers, des booléens et des tableaux.

## Comment lire des fichiers TOML avec `tomllib`

Le module `tomllib` fait partie de la bibliothèque standard de Python à partir de la version 3.11. Il fournit une interface simple pour charger des fichiers TOML comme ceci :

```python
import tomllib

with open('config.toml', 'rb') as f:
    config = tomllib.load(f)

# Access values
app_title = config['title']
db_host = config['database']['host']
db_port = config['database']['port']

print(f"Application: {app_title}")
print(f"Database: {db_host}:{db_port}")
print(f"Config keys: {config.keys()}")
```

Sortie :

```plaintext
Application: My Application
Database: localhost:5432
Config keys: dict_keys(['title', 'version', 'database', 'server', 'logging', 'cache', 'features'])
```

Notez que `tomllib` nécessite l'ouverture des fichiers en mode binaire (`'rb'`). La fonction `load()` analyse le fichier TOML et renvoie un dictionnaire Python classique.

Les valeurs sont automatiquement converties dans les types Python appropriés : les chaînes restent des chaînes, les entiers deviennent des `int`, les booléens deviennent `True`/`False`, et les tableaux deviennent des listes. Ensuite, examinons de plus près le travail avec différents types de données.

## Comment travailler avec les types de données TOML

Le système de types de TOML se mappe proprement aux types intégrés de Python. Voici comment travailler avec différents types de valeurs :

```python
import tomllib

with open('config.toml', 'rb') as f:
    config = tomllib.load(f)

# Strings
app_title = config['title']

# Integers
db_port = config['database']['port']
cache_ttl = config['cache']['ttl']

# Booleans
debug_mode = config['server']['debug']
cache_enabled = config['cache']['enabled']

# Arrays (become Python lists)
databases = config['database']['databases']
allowed_hosts = config['server']['allowed_hosts']

print(f"Databases: {databases}")
print(f"Type of databases: {type(databases)}")
print(f"Debug mode: {debug_mode}, type: {type(debug_mode)}")
```

Avec `tomllib`, vous n'avez pas besoin de méthodes getter spéciales comme avec `ConfigParser`. Le dictionnaire renvoyé contient des objets Python correctement typés et prêts à l'emploi, comme illustré :

```plaintext
Databases: ['myapp_db', 'myapp_cache']
Type of databases: <class 'list'>
Debug mode: False, type: <class 'bool'>
```

## Comment construire un gestionnaire de configuration TOML

Pour les applications en production, envelopper le chargement TOML dans une classe de configuration offre une meilleure gestion des erreurs et une meilleure validation. Voici comment vous pouvez le faire :

```python
import tomllib
from pathlib import Path

class TOMLConfig:
    def __init__(self, config_file='config.toml'):
        self.config_file = Path(config_file)
        
        if not self.config_file.exists():
            raise FileNotFoundError(f"Config file not found: {config_file}")
        
        with open(self.config_file, 'rb') as f:
            self.config = tomllib.load(f)
    
    def get(self, key, default=None):
        """Get a top-level configuration value"""
        return self.config.get(key, default)
    
    def get_section(self, section):
        """Get an entire configuration section"""
        if section not in self.config:
            raise ValueError(f"Section '{section}' not found")
        return self.config[section]
```

Vous pouvez utiliser la classe `TOMLConfig` comme ceci :

```python
config = TOMLConfig('config.toml')

# Get top-level values
app_title = config.get('title')
version = config.get('version')

# Get entire sections
db_config = config.get_section('database')
server_config = config.get_section('server')

print(f"{app_title} v{version}")
print(f"Database config: {db_config}")
```

Cette classe de configuration fournit une interface propre pour votre fichier TOML. Elle valide que le fichier existe avant d'essayer de l'analyser et fournit des méthodes pour accéder en toute sécurité aux valeurs de configuration.

L'exécution du code ci-dessus donne ce résultat :

```plaintext
My Application v1.0.0
Database config: {'host': 'localhost', 'port': 5432, 'username': 'app_user', 'password': 'secure_password', 'databases': ['myapp_db', 'myapp_cache'], 'pool_size': 10, 'ssl_enabled': True}
```

## Comment gérer les valeurs manquantes en toute sécurité

Votre code doit gérer l'absence de configuration avec élégance. Voici comment fournir des valeurs par défaut et valider les valeurs requises :

```python
import tomllib

def load_config_safe(config_file='config.toml'):
    try:
        with open(config_file, 'rb') as f:
            return tomllib.load(f)
    except FileNotFoundError:
        print(f"Config file {config_file} not found, using defaults")
        return {}
    except tomllib.TOMLDecodeError as e:
        print(f"Error parsing TOML: {e}")
        raise

config = load_config_safe('config.toml')

# Get with defaults
db_host = config.get('database', {}).get('host', 'localhost')
db_port = config.get('database', {}).get('port', 5432)
debug = config.get('server', {}).get('debug', False)

print(f"Database: {db_host}:{db_port}")
print(f"Debug: {debug}")
```

Sortie :

```plaintext
Database: localhost:5432
Debug: False
```

Ce modèle utilise des appels `.get()` en chaîne avec des valeurs par défaut. Si une section ou une clé n'existe pas, vous obtenez la valeur par défaut au lieu d'une `KeyError`.

## Conclusion

Lorsque vous travaillez avec des fichiers TOML en Python, suivez ces directives :

* Ouvrez toujours en mode binaire : Le module `tomllib` nécessite le mode binaire (`'rb'`) lors de l'ouverture des fichiers.
    
* Utilisez des tables imbriquées pour l'organisation : Profitez de la capacité de TOML à imbriquer des tables pour les configurations complexes.
    
* Fournissez des valeurs par défaut pour les paramètres optionnels : Utilisez `.get()` avec des valeurs par défaut pour rendre votre application plus flexible.
    

Envisagez d'utiliser TOML pour vos nouveaux projets. Si vous partez de zéro, TOML est un excellent choix pour la configuration en Python. Bon codage !