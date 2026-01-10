---
title: Comment afficher joliment du JSON en Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-04-14T15:38:01.000Z'
originalURL: https://freecodecamp.org/news/how-to-pretty-print-json-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/Shittu-Olumide-How-to-Pretty-Print-JSON-in-Python.png
tags:
- name: json
  slug: json
- name: Python
  slug: python
seo_title: Comment afficher joliment du JSON en Python
seo_desc: "By Shittu Olumide\nJSON (JavaScript Object Notation) is a popular data\
  \ interchange format that is widely used in web applications, APIs, and databases.\
  \ It is a lightweight and human-readable format that is easy to parse and generate.\
  \ \nBut when dealing..."
---

Par Shittu Olumide

JSON (JavaScript Object Notation) est un format d'échange de données populaire largement utilisé dans les applications web, les API et les bases de données. C'est un format léger et lisible par l'homme, facile à analyser et à générer. 

Mais lorsqu'on traite des données JSON volumineuses et complexes, il peut être difficile de lire et de comprendre la structure des données. C'est là que l'affichage joli entre en jeu. L'affichage joli est le processus de formatage des données JSON de manière à les rendre plus faciles à lire et à comprendre. 

Dans cet article, nous allons explorer comment afficher joliment du JSON en Python en utilisant des bibliothèques intégrées et tierces. Nous aborderons également les meilleures pratiques utilisées pour afficher joliment du JSON, et nous parlerons de ses cas d'utilisation.

## Que signifie Affichage Joli ?

En Python, "affichage joli" fait référence au formatage et à la présentation des structures de données telles que les listes, les dictionnaires et les tuples de manière plus lisible et organisée. 

Pour afficher joliment du JSON en Python, nous pouvons utiliser le module intégré `json`. Ce module fournit une fonction `dumps()` qui peut sérialiser des objets Python en une chaîne formatée JSON. 

Par défaut, cette fonction produit une chaîne JSON sans aucun formatage, mais nous pouvons utiliser le paramètre `indent` pour spécifier le nombre d'espaces à utiliser pour l'indentation.

Voici un exemple de la façon d'afficher joliment du JSON en Python :

```py
import json

# Exemple de données JSON
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Convertir les données en une chaîne formatée JSON avec 4 espaces d'indentation
json_str = json.dumps(data, indent=4)

# Afficher la chaîne JSON joliment imprimée
print(json_str)

```

Sortie :

```bash
{
    "name": "John",
    "age": 30,
    "city": "New York"
}

```

Comme vous pouvez le voir, le paramètre `indent` est défini sur `4`, ce qui produit une chaîne JSON avec chaque niveau de nesting indenté de quatre espaces. Nous pouvons ajuster ce paramètre pour contrôler la quantité d'indentation dans la sortie.

Notez que la fonction `json.dumps()` peut également prendre d'autres paramètres optionnels, tels que `sort_keys`, qui peut être utilisé pour trier les clés dans la sortie JSON. Pour plus d'informations, voir la documentation du module json.

## Meilleures Pratiques pour l'Affichage Joli de JSON 

### Utiliser le module `json`

Le module `json` est un module intégré en Python, qui fournit des méthodes pour travailler avec des données JSON. La méthode `json.dumps()` est utilisée pour sérialiser des objets Python en une chaîne formatée JSON. La méthode `json.dumps()` dispose également d'un paramètre optionnel `indent` qui peut être utilisé pour spécifier le nombre d'espaces à utiliser pour l'indentation. 

Voici un exemple :

```py
import json

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

json_str = json.dumps(data, indent=4)
print(json_str)

```

Sortie :

```bash
{
    "name": "John",
    "age": 30,
    "city": "New York"
}

```

### Utiliser le module `pprint`

Le module `pprint` est un module intégré en Python qui fournit un moyen d'afficher joliment les structures de données Python. Il fonctionne également avec les données JSON. La méthode `pprint.pprint()` est utilisée pour afficher joliment les données JSON. 

Voici un exemple :

```py
import json
import pprint

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

pprint.pprint(data)

```

Sortie :

```bash
{'age': 30, 'city': 'New York', 'name': 'John'}

```

### Utiliser des bibliothèques tierces

Il existe de nombreuses bibliothèques tierces disponibles en Python pour l'affichage joli des données JSON, telles que `simplejson`, `ujson`, et `json5`. Ces bibliothèques fournissent des fonctionnalités supplémentaires telles que la sérialisation et la désérialisation plus rapides, la prise en charge de types de données supplémentaires, et des options de formatage plus flexibles. 

Voici un exemple utilisant `simplejson` :

```py
import simplejson as json

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

json_str = json.dumps(data, indent=4, sort_keys=True)
print(json_str)

```

Sortie :

```bash
{
    "age": 30,
    "city": "New York",
    "name": "John"
}

```

## Cas d'Utilisation de l'Affichage Joli de JSON en Python

1. **Débogage des données JSON** : Lorsqu'on travaille avec des données JSON, il peut être difficile de lire et de comprendre la structure des données si elles ne sont pas bien formatées. L'affichage joli des données JSON en Python peut nous aider à identifier rapidement les problèmes avec les données et à déboguer notre code plus efficacement.
2. **Affichage des données JSON dans les interfaces utilisateur** : Si nous développons une application web ou une application mobile qui affiche des données JSON à l'utilisateur, l'affichage joli peut améliorer l'expérience utilisateur en rendant les données plus lisibles et présentables.
3. **Partage des données JSON avec les membres de l'équipe** : Si nous travaillons sur un projet avec d'autres membres de l'équipe et devons partager des données JSON avec eux, l'affichage joli des données peut faciliter leur compréhension et leur travail avec celles-ci.
4. **Journalisation des données JSON** : Si nous journalisons des données JSON dans notre application Python, l'affichage joli des données peut faciliter la lecture et l'analyse des journaux.

## Conclusion

L'affichage joli de JSON en Python est une compétence importante à avoir pour toute personne travaillant avec des données JSON. 

Dans ce tutoriel, nous avons appris comment utiliser le module `json` en Python pour afficher joliment du JSON ainsi que le module `pprint`. Avec seulement quelques lignes de code, nous pouvons générer une sortie JSON bien formatée qui est facile à lire et à naviguer. 

Connectons-nous sur [Twitter](https://www.twitter.com/Shittu_Olumide_) et sur [LinkedIn](https://www.linkedin.com/in/olumide-shittu). Vous pouvez également vous abonner à ma chaîne [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A).

Bon Codage !