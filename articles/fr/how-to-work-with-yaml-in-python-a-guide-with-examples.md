---
title: Comment travailler avec YAML en Python – Un guide avec exemples
author: Bala Priya C
date: '2025-12-10T22:58:47.038Z'
originalURL: https://freecodecamp.org/news/how-to-work-with-yaml-in-python-a-guide-with-examples
description: 'Si vous avez déjà travaillé avec des fichiers de configuration, Docker
  Compose, Kubernetes ou des pipelines CI/CD, vous avez probablement utilisé YAML.
  C''est omniprésent dans le développement moderne, et pour une bonne raison : c''est
  lisible par l''humain, simple et puissant. Dans ce guide, vous apprendrez...'
co_authors: []
series: null
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1765407508788/61769835-bd12-486e-8f8e-ba0f3a7af83c.png
tags:
- name: Python
  slug: python
- name: YAML
  slug: yaml
seo_desc: 'If you''ve ever worked with configuration files, Docker Compose, Kubernetes,
  or CI/CD pipelines, you''ve probably used YAML. It''s everywhere in modern development,
  and for good reason: it’s human-readable, simple, and powerful.

  In this guide, you''ll le...'
---


Si vous avez déjà travaillé avec des fichiers de configuration, Docker Compose, Kubernetes ou des pipelines CI/CD, vous avez probablement utilisé YAML. C'est omniprésent dans le développement moderne, et pour une bonne raison : c'est lisible par l'humain, simple et puissant.

Dans ce guide, vous apprendrez à manipuler des fichiers YAML en Python. Nous aborderons la lecture, l'écriture et la manipulation de données YAML en pratique.

🔗 [**Vous pouvez trouver le code sur GitHub**](https://github.com/balapriyac/python-basics/tree/main/config-management-basics/working-with-yaml).

## Prérequis

Avant de travailler avec YAML en Python, vous devriez avoir :

* Python 3.8 ou une version ultérieure installée
    
* **Connaissances de base en Python** : Variables, types de données, fonctions et structures de contrôle
    
* **Compréhension des structures de données** : Dictionnaires, listes et structures de données imbriquées
    
* **Bases de la manipulation de fichiers** : Lire et écrire dans des fichiers en Python
    
* **Familiarité avec la ligne de commande** : Exécuter des scripts Python et installer des packages avec `pip`
    

Vous devrez également installer la bibliothèque [PyYAML](https://pypi.org/project/PyYAML/) :

```bash
pip install pyyaml
```

## Table des matières

1. [Qu'est-ce que YAML et pourquoi s'y intéresser ?](#heading-qu-est-ce-que-yaml-et-pourquoi-s-y-interesser)
    
2. [Comment lire des fichiers YAML](#heading-comment-lire-des-fichiers-yaml)
    
3. [Comment écrire des fichiers YAML](#heading-comment-ecrire-des-fichiers-yaml)
    
4. [Comment travailler avec des listes en YAML](#heading-comment-travailler-avec-des-listes-en-yaml)
    
5. [Créer un gestionnaire de configuration YAML](#heading-creer-un-gestionnaire-de-configuration-yaml)
    

## Qu'est-ce que YAML et pourquoi s'y intéresser ?

YAML (YAML Ain't Markup Language) est un format de sérialisation de données conçu pour être facile à lire et à écrire. Considérez-le comme le cousin plus lisible du JSON. :)

Voici les mêmes données en JSON et en YAML :

JSON :

```json
{
  "database": {
    "host": "localhost",
    "port": 5432,
    "credentials": {
      "username": "admin",
      "password": "secret"
    }
  }
}
```

YAML :

```yaml
database:
  host: localhost
  port: 5432
  credentials:
    username: admin
    password: secret
```

La version YAML est plus épurée et plus facile à lire, en particulier pour les fichiers de configuration.

## Comment lire des fichiers YAML

Supposons que vous ayez un fichier de configuration pour une application web. Nous allons créer un fichier [`config.yaml`](https://github.com/balapriyac/python-basics/blob/main/config-management-basics/working-with-yaml/config.yaml) simple et apprendre à le lire en Python.

Tout d'abord, comprenons ce que nous essayons de faire. Vous avez des données de configuration stockées dans un fichier YAML, et vous voulez les charger dans Python pour pouvoir les utiliser dans votre application. Voici comment procéder :

```python
import yaml

# Open and read the YAML file
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Access the data
print(config['database']['host'])
```

Sortie :

```plaintext
localhost
```

Voici ce qui se passe dans ce code :

* Nous importons le module `yaml`.
    
* Ensuite, nous ouvrons le fichier à l'aide d'un gestionnaire de contexte (instruction `with`), qui ferme automatiquement le fichier lorsque nous avons terminé.
    
* Nous utilisons `yaml.safe_load()` pour analyser le contenu YAML en un dictionnaire Python afin de pouvoir accéder aux données comme n'importe quel dictionnaire Python.
    

⚠️ Notez que vous devriez **toujours utiliser** `yaml.safe_load()` **au lieu de** `yaml.load()`. La fonction `safe_load()` vous protège des vulnérabilités d'exécution de code arbitraire. À moins d'avoir une raison très spécifique (et c'est probablement peu probable), tenez-vous-en à `safe_load()`.

## Comment écrire des fichiers YAML

Passons maintenant à la direction opposée. Vous avez des structures de données Python et vous voulez les sauvegarder sous forme de fichiers YAML. C'est utile lorsque vous générez des fichiers de configuration ou que vous exportez des données.

```python
import yaml

# Your configuration data as Python dictionaries
config = {
    'database': {
        'host': 'localhost',
        'port': 5432,
        'name': 'myapp_db',
        'credentials': {
            'username': 'admin',
            'password': 'secret123'
        }
    },
    'server': {
        'host': '0.0.0.0',
        'port': 8000,
        'debug': True
    },
    'features': {
        'enable_cache': True,
        'cache_ttl': 3600
    }
}

# Write to a YAML file
with open('generated_config.yaml', 'w') as file:
    yaml.dump(config, file, default_flow_style=False)
```

Analysons ce qui se passe :

* Nous créons un dictionnaire Python imbriqué avec notre configuration.
    
* Nous ouvrons un fichier en mode écriture (`'w'`).
    
* Nous utilisons `yaml.dump()` pour convertir le dictionnaire Python au format YAML et l'écrire dans le fichier.
    
* Le paramètre `default_flow_style=False` garantit que la sortie utilise le style bloc (le format lisible et indenté) au lieu du style en ligne.
    

Le fichier `generated_config.yaml` résultant sera correctement formaté et prêt à l'emploi.

## Comment travailler avec des listes en YAML

YAML gère les listes avec élégance, et elles sont courantes dans les fichiers de configuration. Supposons que vous construisiez une application de microservices et que vous deviez configurer plusieurs points de terminaison de service. Voici comment vous travailleriez avec ces données :

```python
import yaml

# Configuration with lists
services_config = {
    'services': [
        {
            'name': 'auth-service',
            'url': 'http://auth.example.com',
            'timeout': 30
        },
        {
            'name': 'payment-service',
            'url': 'http://payment.example.com',
            'timeout': 60
        },
        {
            'name': 'notification-service',
            'url': 'http://notification.example.com',
            'timeout': 15
        }
    ],
    'retry_policy': {
        'max_attempts': 3,
        'backoff_seconds': 5
    }
}

# Write to file
with open('services.yaml', 'w') as file:
    yaml.dump(services_config, file, default_flow_style=False, sort_keys=False)

# Read it back
with open('services.yaml', 'r') as file:
    loaded_services = yaml.safe_load(file)

# Access list items
for service in loaded_services['services']:
    print(f"Service: {service['name']}, URL: {service['url']}")
```

Sortie :

```plaintext
Service: auth-service, URL: http://auth.example.com
Service: payment-service, URL: http://payment.example.com
Service: notification-service, URL: http://notification.example.com
```

Ce code nous aide à comprendre quelques concepts clés.

Nous pouvons imbriquer des listes et des dictionnaires librement dans nos structures de données Python. Le paramètre `sort_keys=False` préserve l'ordre des clés tel que nous les avons définies. Lorsque nous relisons le YAML, nous pouvons itérer sur les listes comme n'importe quelle liste Python. Les structures de données en Python correspondent aux structures en YAML.

## Créer un gestionnaire de configuration YAML

Mettons tout cela ensemble avec un exemple pratique. Nous allons construire une classe de gestionnaire de configuration simple qui gère les configurations spécifiques à l'environnement (un besoin courant dans les projets réels) :

```python
import yaml
import os

class ConfigManager:
    def __init__(self, config_dir='configs'):
        self.config_dir = config_dir
        self.config = {}
    
    def load_config(self, environment='development'):
        """Load configuration for a specific environment"""
        config_file = os.path.join(self.config_dir, f'{environment}.yaml')
        
        try:
            with open(config_file, 'r') as file:
                self.config = yaml.safe_load(file)
            print(f"✓ Loaded configuration for {environment}")
            return self.config
        except FileNotFoundError:
            print(f"✗ Configuration file not found: {config_file}")
            return None
        except yaml.YAMLError as e:
            print(f"✗ Error parsing YAML: {e}")
            return None
    
    def get(self, key_path, default=None):
        """Get a configuration value using dot notation"""
        keys = key_path.split('.')
        value = self.config
        
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return default
        
        return value
    
    def save_config(self, environment, config_data):
        """Save configuration to a file"""
        config_file = os.path.join(self.config_dir, f'{environment}.yaml')
        
        os.makedirs(self.config_dir, exist_ok=True)
        
        with open(config_file, 'w') as file:
            yaml.dump(config_data, file, default_flow_style=False)
        
        print(f"✓ Saved configuration for {environment}")
```

Cette classe `ConfigManager` vous montre comment construire un utilitaire pratique :

1. **Initialisation** : Nous configurons un répertoire pour les fichiers de configuration.
    
2. **Chargement** : La méthode `load_config()` lit les fichiers YAML spécifiques à l'environnement avec une gestion appropriée des erreurs.
    
3. **Accès aux données** : La méthode `get()` vous permet d'accéder aux valeurs imbriquées en utilisant la notation par points (comme `'database.host'`).
    
4. **Sauvegarde** : La méthode `save_config()` écrit les données de configuration dans des fichiers YAML.
    

C'est le genre de pattern que vous pourriez réellement utiliser dans vos projets. Vous pouvez l'étendre davantage en ajoutant de la validation, des surcharges par variables d'environnement ou la fusion de configurations. Voici comment vous pouvez utiliser la classe `ConfigManager` que nous avons codée :

```python
if __name__ == '__main__':
    # Create config manager
    config_mgr = ConfigManager()
    
    # Create a sample development config
    dev_config = {
        'database': {
            'host': 'localhost',
            'port': 5432,
            'name': 'dev_db'
        },
        'api': {
            'base_url': 'http://localhost:8000',
            'timeout': 30
        }
    }
    
    # Save it
    config_mgr.save_config('development', dev_config)
    
    # Load and use it
    config_mgr.load_config('development')
    print(f"Database host: {config_mgr.get('database.host')}")
    print(f"API timeout: {config_mgr.get('api.timeout')}")
```

L'exécution du code ci-dessus devrait vous donner la sortie suivante :

```plaintext
✓ Saved configuration for development
✓ Loaded configuration for development
Database host: localhost
API timeout: 30
```

## Conclusion

YAML est un outil puissant dans votre boîte à outils de développeur. Il s'avère très utile lorsque vous configurez des applications, définissez des pipelines CI/CD ou travaillez avec l'infrastructure as code.

Dans cet article, vous avez appris à travailler avec des fichiers YAML en Python. Vous pouvez lire des fichiers de configuration, écrire des données au format YAML, gérer des listes et des structures imbriquées, et construire des utilitaires pratiques comme le `ConfigManager` que nous avons codé.

Commencez petit. Essayez de remplacer un fichier de configuration JSON par du YAML dans l'un de vos projets. Vous apprécierez rapidement à quel point il est plus lisible, et vous serez à l'aise pour travailler avec YAML sur l'ensemble des outils et plateformes qui l'utilisent.

Bon code !