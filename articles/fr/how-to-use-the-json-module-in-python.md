---
title: Comment utiliser le module JSON en Python – Un guide pour débutants
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2023-06-05T22:51:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-the-json-module-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/json-module.png
tags:
- name: json
  slug: json
- name: Python
  slug: python
seo_title: Comment utiliser le module JSON en Python – Un guide pour débutants
seo_desc: "JSON (JavaScript Object Notation) is a popular, lightweight data interchange\
  \ standard. It represents data structures made up of key-value pairs that's quite\
  \ straightforward and human-readable. \nJSON has become the industry standard for\
  \ data interchan..."
---

JSON (JavaScript Object Notation) est un standard d'échange de données populaire et léger. Il représente des structures de données composées de paires clé-valeur qui sont assez simples et lisibles par les humains. 

JSON est devenu le standard industriel pour l'échange de données entre les services en ligne. Et il est largement utilisé dans les langages de programmation modernes, y compris Python.

Les données JSON sont fréquemment exprimées sous forme de dictionnaires imbriqués, de listes et de valeurs scalaires telles que des textes, des nombres, des booléens et null. Il est nommé JSON car il imite de près la syntaxe utilisée dans les objets JavaScript.

Dans ce tutoriel, vous explorerez le module JSON en Python et apprendrez à travailler efficacement avec les données JSON.

## Le module JSON intégré de Python

JSON joue un rôle important dans la programmation Python car il permet une sérialisation et une désérialisation efficaces des données. Il permet aux programmes Python de communiquer sans effort avec les services web, d'échanger des données et de stocker des informations structurées. 

Les développeurs peuvent utiliser JSON pour lier de manière transparente leurs programmes Python à une variété d'API, de bases de données et de systèmes externes qui utilisent JSON pour la représentation des données.

Si vous cherchez à apprendre comment interagir avec les services web en utilisant Python, consultez [mon tutoriel sur le module requests](https://blog.ashutoshkrris.in/how-to-interact-with-web-services-using-python).

Le module JSON intégré de Python fournit un ensemble puissant de méthodes et de classes qui rendent le travail avec les données JSON simple. Les développeurs peuvent l'utiliser pour encoder des objets Python en chaînes JSON et décoder des chaînes JSON en objets Python.

## Comment stocker des données JSON dans un fichier

Lorsque vous travaillez avec des données JSON en Python, vous devrez souvent sauvegarder les données ou les partager avec d'autres. Stocker des données JSON dans un fichier permet une récupération rapide et une persistance des données. 

Dans cette section, vous apprendrez à utiliser la fonction `json.dump()` de Python pour sauvegarder des données JSON dans un fichier. Ce processus implique la sérialisation des données JSON et leur sauvegarde dans un fichier, que vous pouvez ensuite lire et utiliser selon vos besoins.

### La fonction `json.dump()`

La fonction `json.dump()` en Python vous permet de stocker des données JSON directement dans un fichier. Cette fonction prend deux paramètres : les données à sérialiser et l'objet fichier où les données seront écrites.

Pour écrire des données JSON dans un fichier, vous devez suivre quelques étapes. Tout d'abord, vous devez ouvrir un fichier en mode écriture, en spécifiant le chemin du fichier. Ensuite, vous pouvez utiliser la fonction `json.dump()` pour sérialiser les données et les écrire dans le fichier. Enfin, vous devez fermer le fichier pour vous assurer que toutes les données sont correctement sauvegardées.

Apprenons comment stocker des données dans un fichier en utilisant la réponse de l'API d'horoscope comme exemple.

Supposons que vous avez fait une requête GET à l'URL suivante : [https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily?sign=capricorn&day=today](https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily?sign=capricorn&day=today), qui fournit l'horoscope quotidien pour le signe du Capricorne.

```python
import requests
import json

# Faire la requête GET à l'API d'horoscope
response = requests.get("https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily?sign=capricorn&day=today")
data = response.json()  # Convertir la réponse en JSON

# Stocker les données JSON dans un fichier
with open("horoscope_data.json", "w") as file:
    json.dump(data, file)

print("Données stockées avec succès !")
```

Dans le code ci-dessus, vous utilisez la bibliothèque `requests` pour faire une requête GET à l'[API d'horoscope](https://blog.ashutoshkrris.in/how-to-create-a-horoscope-api-with-beautiful-soup-and-flask). Vous extrayez ensuite les données JSON de la réponse en utilisant la méthode `.json()`. Enfin, vous ouvrez un fichier nommé `horoscope_data.json` en mode écriture en utilisant l'instruction `with`, et vous utilisez `json.dump()` pour stocker les données dans le fichier.

Consultez [ce tutoriel](https://blog.ashutoshkrris.in/how-to-know-your-horoscope-using-python) pour apprendre comment connaître votre horoscope en utilisant Python.

Si vous ouvrez le fichier `horoscope_data.json`, vous verrez un contenu similaire à celui-ci :

```json
{
  "data": {
    "date": "Jun 3, 2023",
    "horoscope_data": "The forecast today is stormy. You may have sensed that there was some tension clouding the conversation at home. Resentments were left unsaid and subtle power games were played without resolution. Today, Capricorn, it all becomes too unbearable for you. Regardless of the risks involved, you will take measures to clear things up."
  },
  "status": 200,
  "success": true
}
```

## Comment récupérer des données à partir d'un fichier JSON

Vous devrez souvent lire des données à partir d'un fichier JSON. Par exemple, vous devrez peut-être lire des paramètres de configuration à partir d'un fichier JSON. Le module JSON de Python fournit la fonction `json.load()`, qui vous permet de lire et de désérialiser des données JSON à partir d'un fichier. 

Dans cette section, vous apprendrez à utiliser la fonction `json.load()` pour récupérer des données JSON à partir d'un fichier et travailler avec elles dans vos programmes Python.

### La fonction `json.load()`

La fonction `json.load()` accepte un objet fichier comme argument et retourne des données JSON désérialisées sous la forme d'objets Python tels que des dictionnaires, des listes, des chaînes, des nombres, des booléens et des valeurs null.

Pour lire des données JSON à partir d'un fichier, vous devez ouvrir le fichier en mode lecture, extraire les données en utilisant la fonction `json.load()` et les stocker dans une variable pour un traitement ultérieur. Il est important de s'assurer que le fichier lu contient des données JSON valides – sinon, cela peut lever une exception.

Voyons comment vous pouvez récupérer les données du fichier `horoscope_data.json` créé précédemment :

```python
import json

# Récupérer les données JSON du fichier
with open("horoscope_data.json", "r") as file:
    data = json.load(file)

# Accéder et traiter les données JSON récupérées
date = data["data"]["date"]
horoscope_data = data["data"]["horoscope_data"]

# Afficher les données récupérées
print(f"Horoscope pour la date {date}: {horoscope_data}")
```

Dans le code ci-dessus, vous ouvrez le fichier `horoscope_data.json` en mode lecture en utilisant l'instruction `with`. Vous utilisez ensuite la fonction `json.load()` pour désérialiser les données JSON du fichier dans la variable data. Enfin, vous accédez à des champs spécifiques des données JSON (par exemple, "date" et "horoscope_data") et les traitez selon vos besoins.

## Comment formater la sortie JSON

Lorsque vous lisez des données à partir d'un fichier JSON et que vous les affichez, la sortie est affichée sur une seule ligne, ce qui peut ne pas ressembler au format structuré du JSON.

```python
import json

# Récupérer les données JSON du fichier
with open("horoscope_data.json", "r") as file:
    data = json.load(file)

print(data)
```

Sortie :

```bash
{'data': {'date': 'Jun 3, 2023', 'horoscope_data': 'The forecast today is stormy. You may have sensed that there was some tension clouding the conversation at home. Resentments were left unsaid and subtle power games were played without resolution. Today, Capricorn, it all becomes too unbearable for you. Regardless of the risks involved, you will take measures to clear things up.'}, 'status': 200, 'success': True}
```

### La fonction `json.dumps()`

Le module JSON vous fournit une fonction `json.dumps()` pour sérialiser des objets Python en une chaîne formatée JSON. Il offre diverses options de personnalisation, y compris le formatage de la sortie pour la rendre plus lisible.

La fonction `json.dumps()` fournit plusieurs [options](https://docs.python.org/3/library/json.html#json.dumps) pour personnaliser la sortie. La plus couramment utilisée est `indent` qui vous permet de spécifier le nombre d'espaces utilisés pour l'indentation.

```python
import json

# Récupérer les données JSON du fichier
with open("horoscope_data.json", "r") as file:
    data = json.load(file)

# Formater les données
formatted_data = json.dumps(data, indent=2)

print(formatted_data)
```

Sortie :

```bash
{
  "data": {
    "date": "Jun 3, 2023",
    "horoscope_data": "The forecast today is stormy. You may have sensed that there was some tension clouding the conversation at home. Resentments were left unsaid and subtle power games were played without resolution. Today, Capricorn, it all becomes too unbearable for you. Regardless of the risks involved, you will take measures to clear things up."
  },
  "status": 200,
  "success": true
}
```

Comme vous pouvez le voir, les données JSON sont maintenant formatées avec une indentation appropriée, améliorant leur lisibilité. Cette technique peut être appliquée à n'importe quelle donnée JSON, vous permettant de présenter la sortie JSON de manière plus organisée et visuellement attrayante.

## L'outil en ligne de commande `json.tool`

Le module JSON de Python fournit un outil en ligne de commande pratique appelé `json.tool` qui vous permet de formater et d'afficher joliment les données JSON directement à partir de la ligne de commande. C'est un utilitaire utile pour visualiser rapidement la structure et le contenu des données JSON dans un format plus lisible et organisé.

Pour utiliser `json.tool`, vous pouvez exécuter la commande suivante dans votre interface en ligne de commande :

```bash
python -m json.tool <input_file> <output_file>
```

où :

* `python -m json.tool` invoque le module `json.tool` en utilisant l'interpréteur Python.
* `<input_file>` représente le chemin vers le fichier JSON que vous souhaitez formater.
* `<output_file>` est un argument optionnel qui spécifie le fichier dans lequel vous souhaitez sauvegarder la sortie JSON formatée. Si non fourni, la sortie formatée sera affichée sur la console.

Supposons que vous avez un fichier `horoscope_data.json` avec le contenu suivant :

```json
{
  "data": {
    "date": "Jun 3, 2023",
    "horoscope_data": "The forecast today is stormy. You may have sensed that there was some tension clouding the conversation at home. Resentments were left unsaid and subtle power games were played without resolution. Today, Capricorn, it all becomes too unbearable for you. Regardless of the risks involved, you will take measures to clear things up."
  },
  "status": 200,
  "success": true
}
```

Remarquez que le fichier JSON ci-dessus a une indentation de deux espaces.

Pour afficher joliment ce fichier JSON en utilisant `json.tool`, vous pouvez exécuter la commande suivante :

```bash
python -m json.tool horoscope_data.json
```

La sortie sera :

```json
{
    "data": {
        "date": "Jun 3, 2023",
        "horoscope_data": "The forecast today is stormy. You may have sensed that there was some tension clouding the conversation at home. Resentments were left unsaid and subtle power games were played without resolution. Today, Capricorn, it all becomes too unbearable for you. Regardless of the risks involved, you will take measures to clear things up."
    },
    "status": 200,
    "success": true
}
```

Comme vous pouvez le voir dans l'exemple, l'exécution du module `json.tool` avec le chemin du fichier d'entrée formate les données JSON et affiche la sortie formatée sur la console.

Vous pouvez également rediriger la sortie formatée vers un fichier de sortie en spécifiant le nom du fichier de sortie comme deuxième argument :

```bash
python -m json.tool horoscope_data.json formatted_data.json
```

Cette commande formate les données JSON de `horoscope_data.json` et sauvegarde la sortie formatée dans `formatted_data.json`.

## Encodage JSON d'objets personnalisés

Le module JSON en Python vous permet d'encoder et de décoder des objets personnalisés en utilisant les classes d'encodeur et de décodeur JSON. Vous pouvez définir une logique de sérialisation et de désérialisation personnalisée pour vos objets en utilisant ces classes.

La classe `JSONEncoder` vous permet de personnaliser le processus d'encodage. Pour définir comment votre objet personnalisé doit être encodé au format JSON, vous pouvez étendre `JSONEncoder` et modifier sa méthode `default`.

Voici un exemple de la manière dont vous pouvez étendre la classe `JSONEncoder` et personnaliser le processus d'encodage pour un objet personnalisé :

```python
import json


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class PersonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return {"name": obj.name, "age": obj.age}
        return super().default(obj)


# Créer un objet personnalisé
person = Person("Ashutosh Krishna", 23)

# Encoder l'objet personnalisé en utilisant l'encodeur personnalisé
json_str = json.dumps(person, cls=PersonEncoder)

# Afficher la chaîne JSON encodée
print(json_str)
```

Dans cet exemple, vous définissez une classe personnalisée `Person` avec les attributs `name` et `age`. Vous créez ensuite une sous-classe de `JSONEncoder` appelée `PersonEncoder` et vous remplacez sa méthode `default`. Dans la méthode `default`, vous vérifiez si l'objet encodé est une instance de `Person`. Si c'est le cas, vous fournissez une représentation sérialisable en JSON de l'objet en retournant un dictionnaire contenant les attributs `name` et `age`. Si l'objet n'est pas de type `Person`, vous appelez la méthode `default` de la superclasse pour gérer les autres types.

En utilisant `json.dumps` et en spécifiant le paramètre `cls` comme votre classe d'encodeur personnalisée `PersonEncoder`, vous pouvez encoder l'objet `person` en une chaîne JSON. La sortie sera :

```bash
{"name": "Ashutosh Krishna", "age": 23}
```

De même, vous pouvez spécifier une logique de décodage personnalisée dans la classe de décodeur JSON, `JSONDecoder`. Pour définir comment les données JSON doivent être décodées en votre objet personnalisé, étendez `JSONDecoder` et remplacez sa fonction `object_hook`.

## Comment créer du JSON à partir d'un dictionnaire Python

Vous pouvez utiliser la fonction `json.dumps()` fournie par le module JSON pour créer du JSON à partir d'un [dictionnaire Python](https://blog.ashutoshkrris.in/everything-you-need-to-know-about-python-dictionaries). Cette fonction prend un objet Python, généralement un dictionnaire, et le convertit en une représentation de chaîne JSON.

```python
import json

# Dictionnaire Python
data = {
    "name": "Ashutosh Krishna",
    "age": 23,
    "email": "ashutosh@example.com"
}

# Convertir le dictionnaire en chaîne JSON
json_str = json.dumps(data)

# Afficher la chaîne JSON
print(json_str)
```

Dans cet exemple, vous avez un dictionnaire Python `data` représentant certaines données. En appelant `json.dumps(data)`, vous convertissez le dictionnaire en une chaîne JSON. La sortie sera :

```bash
{"name": "Ashutosh Krishna", "age": 23, "email": "ashutosh@example.com"}
```

## Comment créer un dictionnaire Python à partir de JSON

Pour créer un dictionnaire Python à partir de données JSON, vous pouvez utiliser la fonction `json.loads()` fournie par le module JSON. Cette fonction prend une chaîne JSON et la convertit en un objet Python correspondant, généralement un dictionnaire.

```python
import json

# Chaîne JSON
json_str = '{"name": "Ashutosh Krishna", "age": 23, "email": "ashutosh@example.com"}'

# Convertir la chaîne JSON en dictionnaire Python
data = json.loads(json_str)

# Accéder aux valeurs du dictionnaire
print(data["name"])
print(data["age"])
print(data["email"])
```

Dans cet exemple, vous avez une chaîne JSON `json_str` représentant certaines données. En appelant `json.loads(json_str)`, vous convertissez la chaîne JSON en un dictionnaire Python. Vous pouvez ensuite accéder aux valeurs du dictionnaire en utilisant leurs clés respectives.

La sortie sera :

```bash
Ashutosh Krishna
23
ashutosh@example.com
```

## Conclusion

Comprendre le module JSON de Python est nécessaire pour travailler avec des données JSON car il est largement utilisé pour l'échange et le stockage de données dans une variété d'applications. 

Vous pouvez gérer efficacement les données JSON, interagir avec des API et traiter des fichiers de configuration si vous apprenez à utiliser le module JSON.