---
title: Comment parser du JSON en Python – Un guide complet avec exemples
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2025-10-29T21:54:41.737Z'
originalURL: https://freecodecamp.org/news/how-to-parse-json-in-python-with-examples
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1761774871223/d4b07c0a-d37e-4197-bb47-f1ee6f51dffd.png
tags:
- name: Python
  slug: python
- name: json
  slug: json
seo_title: Comment parser du JSON en Python – Un guide complet avec exemples
seo_desc: JSON has become the standard format for data exchange on the web. So you'll
  run into JSON all the time when working with REST APIs, configuration files, database
  exports, and more. As a developer, you should know how to parse, manipulate, and
  generat...
---

Le JSON est devenu le format standard pour l'échange de données sur le web. Vous rencontrerez donc du JSON en permanence lorsque vous travaillerez avec des API REST, des fichiers de configuration, des exports de bases de données, et bien plus encore. En tant que développeur, vous devez savoir comment parser, manipuler et générer du JSON efficacement.

Le [module json intégré de Python](https://docs.python.org/3/library/json.html) offre une interface simple pour travailler avec les données JSON. Vous l'utiliserez pour convertir des chaînes JSON en dictionnaires et listes Python que vous pourrez manipuler avec une syntaxe familière, puis reconvertir vos structures de données Python en JSON lorsque vous devrez envoyer des données à une API ou les sauvegarder dans un fichier.

Au-delà du parsing de base, vous devrez souvent gérer des structures imbriquées, valider l'intégrité des données, gérer et transformer les formats de données. Ce guide couvre les techniques pratiques de parsing JSON que vous pouvez utiliser immédiatement dans vos projets. Commençons !

🔗 [**Vous pouvez trouver les exemples de code sur GitHub**](https://github.com/balapriyac/python-basics/tree/main/parsing-json).

## Prérequis

Pour suivre ce tutoriel, vous devriez avoir :

* Python 3.7 ou une version ultérieure installée sur votre système
    
* Une compréhension de base des dictionnaires et des listes Python
    
* Une familiarité avec les opérations sur les fichiers en Python (ouverture et lecture de fichiers)
    
* Un éditeur de texte ou un IDE pour écrire du code Python
    

## Table des matières

1. [Comprendre la structure JSON et le parsing de base](#heading-comprendre-la-structure-json-et-le-parsing-de-base)
    
2. [Comment travailler avec des objets JSON imbriqués](#heading-comment-travailler-avec-des-objets-json-imbriques)
    
3. [Comment parser des tableaux JSON](#heading-comment-parser-des-tableaux-json)
    
4. [Comment lire du JSON à partir de fichiers](#heading-comment-lire-du-json-a-partir-de-fichiers)
    
5. [Comment gérer les erreurs de parsing JSON](#heading-comment-gerer-les-erreurs-de-parsing-json)
    

## Comprendre la structure JSON et le parsing de base

Le JSON représente les données à l'aide d'une syntaxe simple comprenant six types de données : **objets (paires clé-valeur), tableaux, chaînes de caractères, nombres, booléens** et **null**.

Lorsque Python parse du JSON, ces types correspondent directement aux équivalents Python :

* Les objets JSON deviennent des dictionnaires,
    
* les tableaux deviennent des listes,
    
* les chaînes restent des chaînes,
    
* les nombres deviennent `int` ou `float`,
    
* true et false deviennent `True` et `False`, et
    
* null devient `None`.
    

Cette correspondance directe rend le travail avec le JSON en Python intuitif une fois que vous avez compris ces équivalences.

Avant de commencer, importez le module `json` qui est intégré à la bibliothèque standard de Python.

L'opération de base dans le parsing JSON consiste à convertir une chaîne JSON en une structure de données Python avec laquelle vous pouvez travailler. Voici comment effectuer cette conversion de base :

```python
import json

json_string = '{"name": "Sarah Chen", "age": 28, "city": "Portland"}'
person = json.loads(json_string)

print(person["name"]) 
print(person["age"])   
print(type(person))
```

Sortie :

```plaintext
Sarah Chen
28
<class 'dict'>
```

Ici, la fonction `json.loads()` prend une chaîne contenant du JSON et renvoie un objet Python. Le 's' dans `loads` signifie 'string' (chaîne), indiquant qu'elle travaille avec des données textuelles. Après le parsing, vous disposez d'un dictionnaire Python classique auquel vous pouvez accéder avec la notation entre crochets en utilisant les clés JSON.

## Comment travailler avec des objets JSON imbriqués

Dans le monde réel, les données JSON se présentent rarement sous forme de structures plates. Les API renvoient généralement des objets profondément imbriqués contenant plusieurs niveaux de données. Comprendre comment naviguer dans ces structures est essentiel pour extraire les informations dont vous avez besoin.

Considérez cet exemple de parsing d'une réponse d'API météo contenant des objets imbriqués pour les données de localisation et les conditions actuelles :

```python
import json

weather_data = '''
{
    "location": {
        "city": "Seattle",
        "state": "WA",
        "coordinates": {
            "latitude": 47.6062,
            "longitude": -122.3321
        }
    },
    "current": {
        "temperature_f": 58,
        "conditions": "Partly Cloudy",
        "humidity": 72,
        "wind": {
            "speed_mph": 8,
            "direction": "NW"
        }
    }
}
'''

weather = json.loads(weather_data)
```

Après avoir parsé la chaîne JSON avec `json.loads()`, vous pouvez accéder aux valeurs imbriquées en enchaînant les clés du dictionnaire :

```python
city = weather["location"]["city"]
temp = weather["current"]["temperature_f"]
wind_speed = weather["current"]["wind"]["speed_mph"]

print(f"{city}: {temp}°F, Wind {wind_speed} mph")
```

Sortie :

```plaintext
Seattle: 58°F, Wind 8 mph
```

Dans cet exemple, chaque niveau d'imbrication nécessite une nouvelle paire de crochets. L'expression `weather["location"]["city"]` accède d'abord à l'objet `"location"`, puis récupère la valeur `"city"` à l'intérieur. Vous pouvez descendre d'autant de niveaux que nécessaire, comme `weather["current"]["wind"]["speed_mph"]` qui traverse trois niveaux de profondeur. Cette syntaxe en chaîne reflète la manière dont vous accéderiez aux données dans la structure JSON originale.

## Comment parser des tableaux JSON

Les tableaux JSON représentent des listes ordonnées de valeurs et apparaissent fréquemment dans les réponses d'API lors du renvoi de collections d'éléments. Python convertit les tableaux JSON en listes, que vous pouvez parcourir ou accéder par index.

Voici un exemple de parsing d'une liste de produits provenant d'un système d'inventaire :

```python
import json

products_json = '''
[
    {
        "id": "PROD-001",
        "name": "Wireless Mouse",
        "price": 24.99,
        "in_stock": true
    },
    {
        "id": "PROD-002",
        "name": "Mechanical Keyboard",
        "price": 89.99,
        "in_stock": false
    },
    {
        "id": "PROD-003",
        "name": "USB-C Hub",
        "price": 34.99,
        "in_stock": true
    }
]
'''

products = json.loads(products_json)
```

La chaîne JSON commence par un crochet ouvrant, indiquant un tableau au niveau racine. Après le parsing, `products` est une liste Python contenant trois dictionnaires.

Vous pouvez maintenant utiliser les opérations standard sur les listes Python sur les données parsées. La fonction `len()` renvoie le nombre d'éléments, et vous pouvez parcourir la liste avec une boucle `for`. Chaque itération vous donne un dictionnaire représentant un produit, auquel vous accédez en utilisant la syntaxe des dictionnaires.

```python
print(f"Total products: {len(products)}")

for product in products:
    status = "Available" if product["in_stock"] else "Out of stock"
    print(f"{product['name']}: ${product['price']} - {status}")
```

Sortie :

```plaintext
Total products: 3
Wireless Mouse: $24.99 - Available
Mechanical Keyboard: $89.99 - Out of stock
USB-C Hub: $34.99 - Available
```

Vous pouvez également accéder à des éléments spécifiques du tableau par index et filtrer les données. L'indexation des listes fonctionne exactement comme pour n'importe quelle liste Python, en commençant à zéro.

```python
first_product = products[0]
print(f"First product ID: {first_product['id']}")
```

Sortie :

```plaintext
First product ID: PROD-001
```

Vous pouvez également utiliser les compréhensions de liste pour filtrer les données parsées, créant ainsi une nouvelle liste contenant uniquement les produits dont la valeur "in_stock" est `True`.

```python
available_products = [p for p in products if p["in_stock"]]
print(f"Available: {len(available_products)} products")
```

Sortie :

```plaintext
Available: 2 products
```

## Comment lire du JSON à partir de fichiers

La plupart des applications lisent le JSON à partir de fichiers plutôt qu'à partir de chaînes codées en dur. Les fichiers de configuration, les exports de données et les réponses d'API mises en cache résident généralement dans des fichiers JSON que votre application doit charger au moment de l'exécution.

Le module `json` est fourni avec la fonction `load` pour lire des fichiers, ce qui permet de gérer l'ouverture et le parsing en une seule étape.

Ce code crée un exemple de fichier de configuration pour démontrer la lecture de fichier :

```python
import json

# First, let's create a sample config 
config_data = {
    "api_url": "https://api.example.com/v2",
    "timeout": 30,
    "retry_attempts": 3,
    "enable_logging": True
}

with open('config.json', 'w') as f:
    json.dump(config_data, f, indent=2)
```

La fonction `json.dump()` écrit les données Python dans un fichier, et le paramètre `indent=2` formate le JSON avec une indentation de 2 espaces pour le rendre lisible par l'homme. Le mode `'w'` ouvre le fichier en écriture, le créant s'il n'existe pas ou l'écrasant s'il existe déjà.

Vous pouvez maintenant relire ce fichier dans votre application. La fonction `json.load()` (sans le 's') lit à partir d'un objet fichier et parse le JSON en une seule opération.

```python
with open('config.json', 'r') as f:
    config = json.load(f)

print(f"API URL: {config['api_url']}")
print(f"Timeout: {config['timeout']} seconds")
print(f"Logging: {'Enabled' if config['enable_logging'] else 'Disabled'}")
```

**Notez la différence** : `json.loads()` parse des chaînes, tandis que `json.load()` lit à partir de fichiers.

L'instruction `with` garantit que le fichier est correctement fermé même si une erreur survient pendant la lecture. Une fois le bloc `with` terminé, vous disposez d'un dictionnaire Python contenant toutes les données de configuration parsées.

```plaintext
API URL: https://api.example.com/v2
Timeout: 30 seconds
Logging: Enabled
```

## Comment gérer les erreurs de parsing JSON

Le parsing JSON peut échouer pour de nombreuses raisons : syntaxe malformée, types de données inattendus, fichiers corrompus ou problèmes de réseau lors de la récupération via des API. Votre code doit gérer ces erreurs avec élégance plutôt que de planter.

Le module `json` lève une exception `JSONDecodeError` lorsqu'il rencontre du JSON invalide. Voici comment capturer et gérer ces erreurs de manière appropriée.

Le bloc `try-except` capture toutes les erreurs de parsing JSON :

* L'exception `JSONDecodeError` fournit des informations détaillées sur ce qui s'est mal passé : `e.msg` décrit l'erreur, `e.lineno` indique quelle ligne contient le problème, et `e.colno` montre la position du caractère. Ces informations vous aident à déboguer rapidement un JSON malformé.
    
* La fonction renvoie `None` lorsque le parsing échoue, permettant au code appelant de vérifier cela et de gérer l'erreur de manière appropriée.
    

Testons cela avec quelques exemples JSON :

```python
# Missing closing quote
bad_json1 = '{"name": "Sarah, "age": 28}'
result1 = parse_json_safely(bad_json1)
print(f"Result 1: {result1}\n")

# Missing closing brace
bad_json2 = '{"name": "Sarah", "age": 28'
result2 = parse_json_safely(bad_json2)
print(f"Result 2: {result2}\n")

# Extra comma
bad_json3 = '{"name": "Sarah", "age": 28,}'
result3 = parse_json_safely(bad_json3)
print(f"Result 3: {result3}\n")

# Valid JSON for comparison
good_json = '{"name": "Sarah", "age": 28}'
result4 = parse_json_safely(good_json)
print(f"Result 4: {result4}")
```

Chaque chaîne JSON malformée déclenche un message d'erreur différent indiquant le problème de syntaxe spécifique. Les messages d'erreur aident à localiser exactement où le JSON est invalide. Le dernier exemple montre qu'un JSON valide est parsé avec succès et renvoie un dictionnaire au lieu de `None`.

```plaintext
JSON parsing failed: Expecting ',' delimiter
Error at line 1, column 19
Result 1: None

JSON parsing failed: Expecting ',' delimiter
Error at line 1, column 28
Result 2: None

JSON parsing failed: Expecting property name enclosed in double quotes
Error at line 1, column 29
Result 3: None

Result 4: {'name': 'Sarah', 'age': 28}
```

Lors de la lecture de fichiers JSON, vous devriez également gérer les erreurs liées aux fichiers. La fonction suivante `load_json_file_safely` gère trois types d'erreurs :

* `FileNotFoundError` lorsque le fichier n'existe pas,
    
* `PermissionError` lorsque l'application ne peut pas lire le fichier, et
    
* `JSONDecodeError` lorsque le fichier contient du JSON invalide. Chaque type d'erreur reçoit son propre bloc `except` avec un message approprié.
    

Le code appelant vérifie si le résultat est `None` et se rabat sur des valeurs par défaut, garantissant que l'application continue de fonctionner même lorsque le fichier ne peut pas être chargé.

```python
import json

def load_json_file_safely(filepath):
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found")
        return None
    except PermissionError:
        print(f"Error: Permission denied reading '{filepath}'")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in '{filepath}'")
        print(f"  {e.msg} at line {e.lineno}")
        return None

data = load_json_file_safely('missing_file.json')
if data is None:
    print("Using default configuration")
    data = {"timeout": 30, "retries": 3}
```

Si vous exécutez le code ci-dessus, vous obtiendrez la sortie suivante :

```plaintext
Error: File 'missing_file.json' not found
Using default configuration
```

Et voilà ! Merci d'être allé aussi loin si vous avez suivi jusqu'au bout ! 🥳

## Conclusion

Le module `json` fournit tout ce dont vous avez besoin pour travailler avec des données JSON en Python. Voici un résumé de ce que nous avons couvert :

* Les fonctions principales gèrent les opérations les plus courantes : `json.loads()` parse les chaînes JSON en objets Python, et `json.load()` lit et parse le JSON à partir de fichiers.
    
* Le parsing JSON convertit automatiquement les types de données entre JSON et Python. Cette conversion vous permet de travailler avec le JSON parsé en utilisant la syntaxe Python standard.
    
* Vous pouvez naviguer dans le JSON imbriqué en enchaînant les clés de dictionnaire et les index de liste. Accédez aux valeurs imbriquées comme `data['section']['subsection']['field']` en suivant la structure à travers chaque niveau.
    
* Enveloppez toujours le parsing JSON dans des blocs `try-except` lorsque vous travaillez avec des données externes. L'exception `JSONDecodeError` fournit des informations spécifiques sur les échecs de parsing, y compris l'emplacement de l'erreur, vous aidant à déboguer les problèmes rapidement. Lors de la lecture de fichiers, capturez également `FileNotFoundError` et `PermissionError` pour gérer les problèmes courants d'accès aux fichiers avec élégance.
    

Familiarisez-vous avec ces fondamentaux et vous serez en mesure de gérer la plupart des tâches de parsing JSON dont vous aurez besoin pour vos projets Python. Bon code !