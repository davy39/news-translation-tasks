---
title: Comment utiliser les variables d'environnement en Python
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2025-10-08T16:08:11.766Z'
originalURL: https://freecodecamp.org/news/how-to-work-with-environment-variables-in-python
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1759939671494/fa0f31c9-99e4-43d6-94df-894e0da263f5.png
tags:
- name: Python
  slug: python
seo_title: Comment utiliser les variables d'environnement en Python
seo_desc: 'Environment variables let you configure applications without hardcoding
  sensitive information directly into your source code.

  They''re particularly useful for storing API keys, database credentials, and configuration
  settings that change between devel...'
---

Les variables d'environnement vous permettent de configurer des applications sans coder en dur des informations sensibles directement dans votre code source.

Elles sont particulièrement utiles pour stocker des clés API, des identifiants de base de données et des paramètres de configuration qui changent entre les environnements de développement, de pré-production et de production.

Dans ce tutoriel, vous apprendrez à manipuler les variables d'environnement en Python.

🔗 [**Voici le code sur GitHub**](https://github.com/balapriyac/python-basics/tree/main/config-management-basics/env-vars)**.**

## Table des matières

* [Pourquoi utiliser des variables d'environnement ?](#heading-pourquoi-utiliser-des-variables-denvironnement)
    
* [Prérequis](#heading-prerequis)
    
* [Comment lire les variables d'environnement avec os.environ](#heading-comment-lire-les-variables-denvironnement-avec-osenviron)
    
* [Comment définir des variables d'environnement](#heading-comment-definir-des-variables-denvironnement)
    
* [Comment construire une classe de configuration pour gérer les variables d'environnement](#heading-comment-construire-une-classe-de-configuration-pour-gerer-les-variables-denvironnement)
    
* [Conclusion](#heading-conclusion)
    

## Pourquoi utiliser des variables d'environnement ?

Avant de plonger dans le code, comprenons pourquoi les variables d'environnement sont importantes.

Lorsque vous codez en dur un mot de passe de base de données ou une clé API dans votre script Python, vous risquez d'exposer des informations sensibles si votre code est partagé ou envoyé vers un système de contrôle de version (Commit).

Les variables d'environnement résolvent ce problème en stockant la configuration à l'extérieur de votre base de code, rendant votre application plus sécurisée et portable à travers différents environnements.

## Prérequis

Avant de commencer ce tutoriel, vous devriez avoir :

* Python installé sur votre système, de préférence une version récente comme Python 3.11 ou ultérieure
    
* Une familiarité de base avec la syntaxe Python et la manipulation des dictionnaires
    
* Un éditeur de texte ou un IDE pour écrire du code Python
    

## Comment lire les variables d'environnement avec `os.environ`

Le module intégré `os` de Python fournit l'interface principale pour travailler avec les variables d'environnement. L'objet `os.environ` se comporte comme un dictionnaire contenant toutes les variables d'environnement disponibles pour votre processus Python.

Ce code montre deux approches pour lire les variables d'environnement :

```python
import os

# Récupérer une variable d'environnement (lève une KeyError si non trouvée)
api_key = os.environ['API_KEY']

# Approche plus sûre : récupérer avec une valeur par défaut
database_host = os.environ.get('DATABASE_HOST', 'localhost')
database_port = os.environ.get('DATABASE_PORT', '5432')

print(f"Connexion à {database_host}:{database_port}")
```

Dans la première approche, `os.environ['API_KEY']` lèvera une `KeyError` si la variable n'existe pas, ce qui peut faire planter votre programme.

```plaintext
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
/tmp/ipython-input-2466845533.py in <cell line: 0>()
      2 
      3 # Récupérer une variable d'environnement (lève une KeyError si non trouvée)
----> 4 api_key = os.environ['API_KEY']
      5 
      6 # Approche plus sûre : récupérer avec une valeur par défaut

/usr/lib/python3.12/os.py in __getitem__(self, key)

KeyError: 'API_KEY'
```

L'approche la plus sûre utilise `os.environ.get()`, qui renvoie `None` ou une valeur par défaut spécifiée lorsque la variable est manquante. Cela vous donne le contrôle sur la gestion des configurations manquantes.

### Comprendre la conversion de type

Une chose importante à retenir est que les variables d'environnement sont toujours stockées sous forme de chaînes de caractères (strings). Lorsque vous récupérez une valeur comme `'5432'` pour un numéro de port, c'est une chaîne, pas un entier. Cela signifie que vous devrez convertir les variables d'environnement vers le type approprié pour votre application.

Par exemple, si vous devez utiliser le port de la base de données dans une opération numérique, vous devrez le convertir :

```python
database_port = int(os.environ.get('DATABASE_PORT', '5432'))
max_connections = int(os.environ.get('MAX_CONNECTIONS', '10'))

total_capacity = database_port + max_connections  # Maintenant, cela fonctionne avec des entiers
```

Pour les valeurs booléennes, vous devrez vérifier par rapport aux représentations sous forme de chaîne :

```python
debug_mode = os.environ.get('DEBUG', 'False').lower() in ('true', '1', 'yes')
```

Sans une conversion de type appropriée, vous pourriez rencontrer des comportements inattendus ou des erreurs lorsque votre code attend un nombre mais reçoit une chaîne.

## Comment définir des variables d'environnement

Vous pouvez définir des variables d'environnement par programmation dans votre script Python.

⚠️ Gardez simplement à l'esprit que ces modifications n'affectent que le processus actuel et ses processus enfants.

Ce code montre comment créer, accéder et supprimer des variables d'environnement pendant l'exécution :

```python
import os

# Définir une variable d'environnement
os.environ['APP_ENV'] = 'development'
os.environ['MAX_CONNECTIONS'] = '100'

# Vérifier qu'elle a été définie
print(f"Environnement : {os.environ['APP_ENV']}")

# Supprimer une variable d'environnement
if 'TEMP_VAR' in os.environ:
    del os.environ['TEMP_VAR']
```

La clé est de se rappeler que ces changements sont temporaires et n'existent que pendant la durée de vie de votre processus Python. Lorsque votre script se termine, ces modifications disparaissent.

## Comment construire une classe de configuration pour gérer les variables d'environnement

En pratique, vous pouvez gérer les variables d'environnement en créant une classe de configuration qui centralise tous les accès aux variables d'environnement et fournit une validation. Cette approche rend vos informations de configuration plus faciles à mettre à jour et à maintenir.

Voici un exemple de classe de configuration qui encapsule toute la gestion des variables d'environnement en un seul endroit :

```python
import os

class AppConfig:
    """Configuration de l'application chargée à partir des variables d'environnement"""
    
    def __init__(self):
        # Paramètres requis (échouera rapidement s'ils sont manquants)
        self.api_key = self._get_required('API_KEY')
        self.database_url = self._get_required('DATABASE_URL')
        
        # Paramètres optionnels avec valeurs par défaut
        self.debug = self._get_bool('DEBUG', False)
        self.port = self._get_int('PORT', 8000)
        self.log_level = os.environ.get('LOG_LEVEL', 'INFO')
        self.max_workers = self._get_int('MAX_WORKERS', 4)
        
    def _get_required(self, key):
        """Récupère une variable d'environnement requise ou lève une erreur"""
        value = os.environ.get(key)
        if value is None:
            raise ValueError(f"La variable d'environnement requise '{key}' n'est pas définie")
        return value
    
    def _get_bool(self, key, default):
        """Convertit une variable d'environnement en booléen"""
        value = os.environ.get(key)
        if value is None:
            return default
        return value.lower() in ('true', '1', 'yes', 'on')
    
    def _get_int(self, key, default):
        """Convertit une variable d'environnement en entier"""
        value = os.environ.get(key)
        if value is None:
            return default
        try:
            return int(value)
        except ValueError:
            raise ValueError(f"La variable d'environnement '{key}' doit être un entier, reçu '{value}'")
    
    def __repr__(self):
        """Représentation sous forme de chaîne sécurisée (masque les données sensibles)"""
        return (f"AppConfig(debug={self.debug}, port={self.port}, "
                f"log_level={self.log_level}, api_key={'*' * 8})")
```

Les méthodes d'assistance `_get_required()`, `_get_bool()` et `_get_int()` gèrent la conversion de type et la validation, rendant votre code plus robuste. La méthode `__repr__()` fournit un moyen sûr d'afficher la configuration sans exposer de valeurs sensibles comme les clés API.

Assurez-vous de définir les variables d'environnement requises :

```python
# Définir la variable d'environnement API_KEY
os.environ['API_KEY'] = 'votre_cle_api_ici' # Remplacez par votre véritable clé API
os.environ['DATABASE_URL'] = 'votre_url_bdd_ici' # Remplacez par l'URL de votre base de données
```

Vous pouvez maintenant instancier un objet `AppConfig` et l'utiliser ainsi :

```python
config = AppConfig()
print(config)
print(f"Exécution sur le port {config.port}")
```

Cela devrait vous donner une sortie d'exemple comme celle-ci :

```plaintext
AppConfig(debug=False, port=8000, log_level=INFO, api_key=********)
Running on port 8000
```

## Conclusion

J'espère que vous avez trouvé cet article utile ! Les variables d'environnement vous offrent un moyen simple et sécurisé de configurer des applications Python qui fonctionnent de manière cohérente dans différents environnements tout en gardant les informations sensibles hors de votre code source.

Lorsque vous travaillez avec des variables d'environnement, gardez à l'esprit les points suivants :

* Ne committez jamais de secrets dans le contrôle de version. Ajoutez toujours `.env` à votre fichier `.gitignore`. Fournissez un fichier `.env.example` avec des valeurs fictives pour montrer aux autres développeurs quelles variables sont nécessaires.
    
* Échouez rapidement (fail-fast) en cas de configuration requise manquante. Si votre application ne peut pas fonctionner sans certaines variables d'environnement, vérifiez-les au démarrage et levez des erreurs claires plutôt que d'échouer plus tard.
    
* Utilisez la conversion de type au besoin. Les variables d'environnement sont toujours des chaînes de caractères, convertissez-les donc au type approprié et gérez les erreurs de conversion avec élégance.
    
* Fournissez des valeurs par défaut raisonnables. Pour les configurations non sensibles comme les numéros de port ou les drapeaux de fonctionnalités (feature flags), les valeurs par défaut facilitent l'exécution de votre application pendant le développement.
    

En plus de ce qui précède, essayez également de documenter vos variables d'environnement. Maintenez une liste de toutes les variables d'environnement utilisées par votre application, ce qu'elles contrôlent et lesquelles sont obligatoires.

Dans mon prochain article, vous apprendrez comment analyser des fichiers de configuration en Python. D'ici là, bon codage !