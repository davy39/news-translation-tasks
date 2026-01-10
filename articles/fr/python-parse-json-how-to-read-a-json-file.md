---
title: Python Parse JSON – Comment lire un fichier JSON
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2022-02-07T17:03:18.000Z'
originalURL: https://freecodecamp.org/news/python-parse-json-how-to-read-a-json-file
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/pexels-mike-1181776.jpg
tags:
- name: json
  slug: json
- name: Python
  slug: python
seo_title: Python Parse JSON – Comment lire un fichier JSON
seo_desc: 'JSON (JavaScript Object Notation) is a popular way to structure data. It''s
  used to exchange information between a web application and the server. But how do
  you read a JSON file in Python?

  In this article, I will show you how to use the json.loads() ...'
---

JSON (JavaScript Object Notation) est une manière populaire de structurer des données. Il est utilisé pour échanger des informations entre une application web et le serveur. Mais comment lire un fichier JSON en Python ?

Dans cet article, je vais vous montrer comment utiliser les méthodes `json.loads()` et `json.load()` pour analyser et lire des fichiers et des chaînes JSON. 

## Syntaxe JSON

Avant de nous pencher sur l'analyse et la lecture d'un fichier JSON, nous devons d'abord comprendre la syntaxe de base. La syntaxe JSON ressemble à un littéral d'objet JavaScript avec des paires clé-valeur.

Voici un exemple de données JSON pour [freeCodeCamp](https://www.freecodecamp.org/) :

```json
{
  "organization": "freeCodeCamp",
  "website": "https://www.freecodecamp.org/",
  "formed": 2014,
  "founder": "Quincy Larson",
  "certifications": [
    {
      "name": "Responsive Web Design",
      "courses": [
        "HTML",
        "CSS"
      ]
    },
    {
      "name": "JavaScript Algorithms and Data Structures",
      "courses": [
        "JavaScript"
      ]
    },
    {
      "name": "Front End Development Libraries",
      "courses": [
        "Bootstrap",
        "jQuery",
        "Sass",
        "React",
        "Redux"
      ]
    },
    {
      "name": "Data Visualization",
      "courses": [
        "D3"
      ]
    },
    {
      "name": "Relational Database Course",
      "courses": [
        "Linux",
        "SQL",
        "PostgreSQL",
        "Bash Scripting",
        "Git and GitHub",
        "Nano"
      ]
    },
    {
      "name": "Back End Development and APIs",
      "courses": [
        "MongoDB",
        "Express",
        "Node",
        "NPM"
      ]
    },
    {
      "name": "Quality Assurance",
      "courses": [
        "Testing with Chai",
        "Express",
        "Node"
      ]
    },
    {
      "name": "Scientific Computing with Python",
      "courses": [
        "Python"
      ]
    },
    {
      "name": "Data Analysis with Python",
      "courses": [
        "Numpy",
        "Pandas",
        "Matplotlib",
        "Seaborn"
      ]
    },
    {
      "name": "Information Security",
      "courses": [
        "HelmetJS"
      ]
    },
    {
      "name": "Machine Learning with Python",
      "courses": [
        "Machine Learning",
        "TensorFlow"
      ]
    }
  ]
}
```

## Comment analyser une chaîne JSON en Python

Python dispose d'un module intégré qui permet de travailler avec des données JSON. En haut de votre fichier, vous devrez importer le module `json`. 

```py
import json

```

Si vous devez analyser une chaîne JSON qui retourne un dictionnaire, vous pouvez utiliser la méthode `json.loads()`. 

```py
import json

# assigne une chaîne JSON à une variable appelée jess 
jess = '{"name": "Jessica Wilkins", "hobbies": ["music", "watching TV", "hanging out with friends"]}'

# analyse les données et les assigne à une variable appelée jess_dict
jess_dict = json.loads(jess)

# Sortie imprimée : {"name": "Jessica Wilkins", "hobbies": ["music", "watching TV", "hanging out with friends"]}
print(jess_dict)
```

## Comment analyser et lire un fichier JSON en Python

Dans cet exemple, nous avons un fichier JSON appelé `fcc.json` qui contient les mêmes données que précédemment concernant les cours proposés par freeCodeCamp. 

Si nous voulons lire ce fichier, nous devons d'abord utiliser la fonction intégrée `open()` de Python avec le mode de lecture. Nous utilisons le mot-clé `with` pour nous assurer que le fichier est correctement fermé. 

```py
with open('fcc.json', 'r') as fcc_file:

```

Si le fichier ne peut pas être ouvert, nous recevrons une erreur OSError. Voici un exemple d'une "FileNotFoundError" si je fais une faute de frappe dans le nom du fichier `fcc.json`. 

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-07-at-4.47.15-AM.png)

Nous pouvons ensuite analyser le fichier en utilisant la méthode `json.load()` et l'assigner à une variable appelée `fcc_data`. 

```py
 fcc_data = json.load(fcc_file)
```

La dernière étape consiste à imprimer les résultats.

```py
print(fcc_data)

```

Voici à quoi ressemblerait l'ensemble du code :

```py
import json

with open('fcc.json', 'r') as fcc_file:
    fcc_data = json.load(fcc_file)
    print(fcc_data)
```

## Comment afficher joliment les données JSON en Python

Si nous examinons les données imprimées, nous devrions voir que les données JSON s'affichent toutes sur une seule ligne.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-07-at-5.09.05-AM.png)

Mais cela peut être difficile à lire. Pour y remédier, nous pouvons utiliser la méthode `json.dumps()` avec le paramètre `indent`.

Dans cet exemple, nous allons avoir une indentation de 4 espaces et afficher les données dans un format plus facile à lire.

```py
 print(json.dumps(fcc_data, indent=4))

```

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-07-at-5.13.13-AM.png)

Nous pouvons également trier les clés par ordre alphabétique en utilisant le paramètre `sort_keys` et en le définissant sur `True`. 

```py
print(json.dumps(fcc_data, indent=4, sort_keys=True))

```

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-07-at-5.18.47-AM.png)

## Conclusion

JSON (JavaScript Object Notation) est une manière populaire de structurer des données et est utilisé pour échanger des informations entre une application web et le serveur. 

Si vous devez analyser une chaîne JSON qui retourne un dictionnaire, vous pouvez utiliser la méthode `json.loads()`. 

Si vous devez analyser un fichier JSON qui retourne un dictionnaire, vous pouvez utiliser la méthode `json.load()`.