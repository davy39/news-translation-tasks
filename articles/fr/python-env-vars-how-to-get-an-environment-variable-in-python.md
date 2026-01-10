---
title: Variables d'environnement Python – Comment obtenir une variable d'environnement
  en Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-07-10T21:39:01.000Z'
originalURL: https://freecodecamp.org/news/python-env-vars-how-to-get-an-environment-variable-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/Shittu-Olumide-Python-Env-Vars
seo_title: Variables d'environnement Python – Comment obtenir une variable d'environnement
  en Python
---

How-to-get-an-Environment-Variable-in-Python.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "Par Shittu Olumide\nLes variables d'environnement jouent un rôle crucial en programmation Python.\n  \ Elles fournissent un moyen de stocker et d'accéder à des valeurs de configuration, des informations spécifiques au système,\n  \ et des données sensibles. \nDans cet article, nous explorerons diverses méthodes\n  \ pour récupérer..."
---

Par Shittu Olumide

Les variables d'environnement jouent un rôle crucial en programmation Python. Elles fournissent un moyen de stocker et d'accéder à des valeurs de configuration, des informations spécifiques au système et des données sensibles.

Dans cet article, nous explorerons diverses méthodes pour récupérer des variables d'environnement en Python et discuterons des meilleures pratiques pour les gérer et les manipuler efficacement.

## Qu'est-ce qu'une variable d'environnement ?

Une variable d'environnement est une valeur nommée qui peut affecter le comportement des processus s'exécutant sur un système informatique ou un système d'exploitation. Il s'agit d'une valeur dynamique stockée dans l'environnement et accessible par divers programmes ou scripts s'exécutant sur le système.

Les variables d'environnement sont généralement définies par le système d'exploitation ou par l'utilisateur et sont accessibles à tous les programmes et processus s'exécutant sur le système. Elles fournissent un moyen de stocker des paramètres de configuration, des informations spécifiques au système ou des données sensibles sans les coder en dur directement dans le code. Au lieu de cela, le code peut récupérer les valeurs à partir des variables d'environnement, permettant ainsi flexibilité, sécurité et portabilité.

Les variables d'environnement sont couramment utilisées dans le développement logiciel pour configurer des applications en fonction de l'environnement spécifique dans lequel elles sont déployées. Par exemple, une application peut utiliser des variables d'environnement pour stocker des chaînes de connexion à une base de données, des clés API, des chemins de fichiers ou d'autres paramètres pouvant varier selon les différents environnements (comme le développement, la préproduction ou la production).

En Python, vous pouvez accéder et manipuler des variables d'environnement en utilisant le module `os`. Ce module fournit des fonctions et des dictionnaires pour interagir avec le système d'exploitation, y compris la possibilité de récupérer les valeurs des variables d'environnement, de définir de nouvelles variables ou de modifier celles existantes.

## Comment accéder aux variables d'environnement :

Pour accéder aux variables d'environnement en Python, nous pouvons utiliser le module intégré `os`, qui fournit des fonctions pour interagir avec le système d'exploitation.

### Comment utiliser le module os :

Tout d'abord, nous devons importer le module `os` dans notre script Python :

```python
import os
```

Le dictionnaire `os.environ` nous permet d'accéder à toutes les variables d'environnement définies sur notre système. Nous pouvons récupérer la valeur d'une variable d'environnement spécifique en utilisant son nom comme clé :

```python
# Récupération de la valeur de la variable d'environnement "PATH"
path = os.environ["PATH"]
print(path)
```

### Comment récupérer des variables d'environnement spécifiques :

Pour récupérer une variable d'environnement sans provoquer d'erreur si elle n'existe pas, nous pouvons utiliser la méthode `os.environ.get()`. Cette méthode prend le nom de la variable comme argument et retourne sa valeur. Si la variable n'existe pas, elle retourne `None` ou une valeur par défaut spécifiée :

```python
# Récupération de la valeur d'une variable d'environnement avec une valeur par défaut
database_url = os.environ.get("DATABASE_URL", "localhost:5432")
print(database_url)
```

### Cas d'utilisation exemples :

Récupération d'informations spécifiques au système :

* **Accéder à la variable d'environnement `PATH`** : La variable `PATH` contient une liste de répertoires que le système d'exploitation recherche lors de l'exécution d'une commande. Récupérer sa valeur nous permet de localiser facilement des exécutables ou des scripts.
* **Récupérer le répertoire personnel de l'utilisateur actuel** : Les variables d'environnement `HOME` ou `USERPROFILE` stockent le chemin vers le répertoire personnel de l'utilisateur actuel, ce qui est utile pour accéder à des fichiers et répertoires spécifiques à l'utilisateur.

Gestion des informations sensibles :

* **Utiliser des variables d'environnement pour les clés API et les mots de passe** : Stocker des données sensibles, telles que les clés API et les mots de passe, sous forme de variables d'environnement au lieu de les coder en dur dans le code améliore la sécurité. Nous pouvons récupérer ces valeurs dans nos scripts Python en utilisant les méthodes mentionnées précédemment.
* **Sécuriser les données sensibles en dehors du code** : En stockant des informations sensibles sous forme de variables d'environnement, nous pouvons séparer la configuration du code. Cela nous permet de partager le code publiquement tout en gardant les données sensibles privées.

## Comment définir des variables d'environnement :

Nous pouvons également définir des variables d'environnement en utilisant le dictionnaire `os.environ`.

### Comment utiliser `os.environ` :

Pour définir une nouvelle variable d'environnement, nous attribuons une valeur à une clé dans le dictionnaire `os.environ` :

```python
# Définition d'une nouvelle variable d'environnement
os.environ["API_KEY"] = "YOUR_API_KEY"
```

Pour modifier une variable d'environnement existante, nous pouvons simplement réattribuer une nouvelle valeur à la clé :

```python
# Modification d'une variable d'environnement existante
os.environ["DATABASE_URL"] = "new_database_url"
```

## Bonnes pratiques et conseils pour utiliser les variables d'environnement :

* **Conventions de nommage pour les variables d'environnement** : Il est bon de pratique d'utiliser des lettres majuscules et des traits de soulignement pour nommer les variables d'environnement, les rendant ainsi facilement distinguables des variables régulières.
* **Gestion des différences spécifiques à la plateforme** : Gardez à l'esprit que les noms des variables d'environnement peuvent différer selon les plateformes. Par exemple, la variable `HOME` est utilisée dans les systèmes de type Unix, tandis que `USERPROFILE` est utilisée dans Windows. Tenez compte de ces différences lors de la récupération des variables d'environnement.
* **Documentation et gestion des variables d'environnement** : Maintenez une documentation listant toutes les variables d'environnement requises pour votre application, y compris leur objectif et leurs valeurs par défaut. Utilisez des outils comme les fichiers `.env` pour gérer les variables d'environnement pendant le développement local.
* **Utilisation d'un fichier .env pour le développement local** : Pendant le développement local, il est souvent pratique d'utiliser un fichier `.env` pour stocker les variables d'environnement. Ce fichier contient des paires clé-valeur au format `KEY=VALUE`, chaque variable étant sur une nouvelle ligne. Nous pouvons utiliser des bibliothèques comme `python-dotenv` pour charger automatiquement les variables du fichier dans notre script Python.

## Conclusion

Dans cet article, nous avons exploré différentes méthodes pour récupérer des variables d'environnement en Python. Nous avons appris comment y accéder en utilisant le dictionnaire `os.environ` et récupérer des variables spécifiques avec des valeurs par défaut. Nous avons également discuté de cas d'utilisation exemples, tels que la récupération d'informations spécifiques au système et la gestion sécurisée des données sensibles.

Nous avons vu comment définir des variables d'environnement en utilisant le dictionnaire `os.environ`, à la fois pour créer de nouvelles variables et modifier celles existantes. Suivre les meilleures pratiques, telles que l'utilisation de conventions de nommage, la gestion des différences spécifiques à la plateforme et la documentation des variables, est crucial pour une gestion efficace.

En utilisant des variables d'environnement en Python, nous pouvons améliorer la flexibilité, la sécurité et la portabilité de nos applications. N'oubliez pas de suivre les meilleures pratiques et d'incorporer les variables d'environnement comme une partie fondamentale de votre flux de travail de développement Python.

Connectons-nous sur [Twitter](https://www.twitter.com/Shittu_Olumide_) et sur [LinkedIn](https://www.linkedin.com/in/olumide-shittu). Vous pouvez également vous abonner à ma chaîne [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A).

Bon codage !