---
title: Comment gérer vos projets Python avec Poetry
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2025-11-21T21:16:02.318Z'
originalURL: https://freecodecamp.org/news/how-to-manage-your-python-projects-with-poetry
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1763759433793/adc30f57-5174-4af5-9eb7-2da52c450b36.png
tags:
- name: Python
  slug: python
- name: package manager
  slug: package-manager
seo_title: Comment gérer vos projets Python avec Poetry
seo_desc: 'Python development looks simple from the outside. But managing real projects
  is rarely easy. You need to install packages, update them, avoid version conflicts,
  create virtual environments, and prepare your project for distribution.

  Many beginners th...'
---

Le développement Python semble simple de l'extérieur. Mais la gestion de projets réels est rarement facile. Vous devez installer des packages, les mettre à jour, éviter les conflits de versions, créer des environnements virtuels et préparer votre projet pour la distribution.

Beaucoup de débutants pensent qu'ils peuvent tout gérer avec pip et venv. Cela fonctionne pour de petits scripts, mais cela devient désordonné une fois que votre projet prend de l'ampleur.

[Poetry](https://python-poetry.org/) résout ce problème en vous offrant un flux de travail (workflow) propre pour gérer les projets Python du début à la fin. Poetry apporte de la structure à votre projet. Il automatise la gestion des packages, crée des environnements virtuels de manière indépendante et prépare votre projet pour la construction et la publication. Il remplace de nombreux outils dispersés, apportant clarté et fiabilité. Avec Poetry, vous vous concentrez sur l'écriture du code pendant qu'il s'occupe de la configuration.

Poetry est également très utile pour les projets d'IA. Il verrouille les versions exactes des dépendances, ce qui empêche les ruptures soudaines lorsque des bibliothèques comme transformers, torch ou [langchain](https://www.turingtalks.ai/p/langchain-vs-langgraph) publient des mises à jour pouvant modifier le comportement du modèle ou les sorties de l'API.

Cet article explique comment Poetry fonctionne, comment l'utiliser avec des exemples, et comment il se compare aux autres alternatives. L'objectif est de rendre Poetry simple à comprendre, même si vous débutez en Python.

## Ce que nous allons couvrir

* [Le problème que Poetry tente de résoudre](#heading-le-probleme-que-poetry-tente-de-resoudre)
    
* [Premiers pas avec Poetry](#heading-premiers-pas-avec-poetry)
    
* [Comprendre pyproject.toml](#heading-comprendre-pyprojecttoml)
    
* [Créer une application exemple](#heading-creer-une-application-exemple)
    
* [Le fichier Lock](#heading-le-fichier-lock)
    
* [Comparaison de Poetry avec d'autres outils](#heading-comparaison-de-poetry-avec-dautres-outils)
    
    * [Poetry vs Pip et les environnements virtuels](#heading-poetry-vs-pip-et-les-environnements-virtuels)
        
    * [Poetry vs Pipenv](#heading-poetry-vs-pipenv)
        
    * [Poetry vs Hatch](#heading-poetry-vs-hatch)
        
* [Pourquoi Poetry est agréable à utiliser](#heading-pourquoi-poetry-est-agreable-a-utiliser)
    
* [Quand Poetry pourrait ne pas être le meilleur choix](#heading-quand-poetry-pourrait-ne-pas-etre-le-meilleur-choix)
    
* [Conclusion](#heading-conclusion)
    

## Le problème que Poetry tente de résoudre

Les [projets Python](https://www.freecodecamp.org/news/learn-python-basics/) modernes nécessitent de nombreuses pièces mobiles. Vous installez des bibliothèques depuis [PyPI](http://pypi.org/), vous les mettez à jour au fil du temps, vous suivez les versions pour garder le projet stable et vous partagez ces versions avec votre équipe. Vous devez également packager votre projet si vous voulez que d'autres l'utilisent.

La méthode traditionnelle utilisant `requirements.txt` et `pip install` ne résout pas tout. Les dépendances peuvent casser lorsqu'une nouvelle version est publiée. Deux développeurs peuvent utiliser des versions différentes sans le savoir. Vous pouvez oublier quel environnement vous avez utilisé. Lorsque vous voulez packager le projet, vous avez souvent besoin d'outils comme setup tools et wheel.

Poetry rassemble toutes ces pièces. Il utilise un seul fichier, [pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/), pour tout définir. Il installe les packages dans un environnement virtuel propre. Il verrouille les versions pour éviter les surprises. Et il peut construire et publier votre package avec quelques commandes.

## Premiers pas avec Poetry

Poetry est facile à prendre en main. Vous l'installez une fois, et il fonctionne sur n'importe quel projet Python. Exécutez cette commande pour installer Poetry sur votre système :

```python
pipx install poetry
```

Une fois installé, vous pouvez démarrer un nouveau projet en utilisant :

```python
poetry new my_project
```

Cela crée un dossier avec une structure de base. Il inclut un fichier `pyproject.toml`. Ce fichier est le cœur de votre projet. Il comprend le nom de votre projet, sa version, sa description et ses dépendances.

```python
[tool.poetry]
name = "myapp"
version = "0.1.0"
description = ""
authors = ["Manish Shivanandhan <manish@example.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.12"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

Si vous souhaitez ajouter Poetry à un projet existant, utilisez :

```python
poetry init
```

Cela vous posera des questions simples sur votre projet et créera le fichier de configuration.

```python
This command will guide you through creating your pyproject.toml config.

Package name [myapp]:
Version [0.1.0]:
Description []:
Author [Manish Shivanandhan <manish@example.com>, n to skip]:
License []:
Compatible Python versions [^3.12]:

Would you like to define your main dependencies interactively? (yes/no) [yes]
You can specify a package in the following forms:
  - A single name (requests): this will search for matches on PyPI
  - A name and a constraint (requests@^2.23.0)
  - A git url (git+https://github.com/python-poetry/poetry.git)
  - A git url with a revision (git+https://github.com/python-poetry/poetry.git#develop)
  - A file path (../my-package/my-package.whl)
  - A directory (../my-package/)
  - A url (https://example.com/packages/my-package-0.1.0.tar.gz)

Package to add or search for (leave blank to skip):

Would you like to define your development dependencies interactively? (yes/no) [yes]
```

Maintenant, vous pouvez installer des packages en utilisant :

```python
poetry add <package_name>
```

Poetry installera le package à l'intérieur de son propre environnement virtuel. Vous n'avez pas besoin de lancer `venv` manuellement. Pour exécuter votre programme Python, utilisez :

```python
poetry run python main.py
```

Ou vous pouvez entrer dans l'environnement :

```python
poetry shell
```

Ce flux de travail simple devient naturel très rapidement.

## Comprendre `pyproject.toml`

Le fichier `pyproject.toml` contient les données qui définissent votre projet. Poetry remplit ce fichier lorsque vous ajoutez ou supprimez des dépendances. Voici un exemple de fichier simple :

```python
[tool.poetry]
name = "weather"
version = "0.1.0"
authors = ["Manish"]

[tool.poetry.dependencies]
python = "^3.10"
requests = "^2.32.0"
[tool.poetry.group.dev.dependencies]
pytest = "^8.2.0"
```

Ce fichier unique remplace `setup.py`, `requirements.txt` et de nombreuses étapes manuelles. Poetry agit comme un gestionnaire pour tout ce qui s'y trouve.

## Créer une application exemple

Imaginez que vous créez une application météo simple qui appelle une API. Après avoir créé un projet Poetry, vous ajoutez une dépendance :

```python
poetry add requests
```

Ensuite, vous écrivez un script Python :

```python
import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=3"
    response = requests.get(url)
    print(response.text)
get_weather("London")
```

Pour l'exécuter :

```python
poetry run python weather.py
```

Poetry verrouille la version de requests afin que votre application fonctionne de la même manière pour tout le monde. Si une nouvelle version est publiée et casse quelque chose, vous êtes en sécurité car Poetry conserve votre version verrouillée.

Lorsque vous souhaitez construire votre projet pour la publication, exécutez :

```python
poetry build
```

Cette commande crée un fichier que vous pouvez télécharger sur PyPI :

```python
poetry publish
```

Ce genre de simplicité est la raison pour laquelle Poetry est devenu un favori parmi les développeurs.

## Le fichier Lock

L'une des fonctionnalités discrètement puissantes de Poetry est le fichier lock. Lorsque vous ajoutez un package, Poetry écrit les versions exactes dans `poetry.lock`. Ce fichier garantit que votre projet se comporte de la même manière sur toutes les machines. Si quelqu'un clone votre projet, tout ce dont il a besoin est :

```python
poetry install
```

Poetry lit le fichier lock et installe exactement les mêmes versions que celles que vous avez utilisées. Cela aide au débogage car rien ne change silencieusement après l'installation.

## Comparaison de Poetry avec d'autres outils

Poetry n'est pas le seul outil pour gérer les projets Python. Pour comprendre pourquoi les développeurs choisissent Poetry, il est utile de le comparer à d'autres options populaires. Voici trois alternatives et leurs différences.

### **Poetry vs Pip et les environnements virtuels**

[Pip](https://pypi.org/project/pip/) est l'installateur de packages Python par défaut, et venv crée des environnements isolés. Ces deux outils sont utilisés ensemble depuis des années. Ils fonctionnent bien pour des scripts simples mais nécessitent des étapes manuelles pour les projets réels.

Vous créez un environnement virtuel manuellement :

```python
python -m venv env
```

Ensuite, vous l'activez, installez les packages, mettez à jour `requirements.txt` et gérez vous-même les conflits de versions. Le packaging du projet est un processus entièrement séparé.

Poetry automatise tout cela. Il crée l'environnement, suit les versions et construit les packages. Le flux de travail est plus propre et plus moderne. Pip et venv semblent manuels par rapport à l'approche automatisée de Poetry.

Si vous n'avez besoin que d'un script rapide, pip et venv suffisent. Mais pour des projets reproductibles et partageables, Poetry l'emporte largement.

### **Poetry vs Pipenv**

[Pipenv](https://pipenv.pypa.io/en/latest/) a été créé pour rendre pip plus facile à utiliser. Il combine pip et les environnements virtuels dans un flux de travail unique. Beaucoup pensaient que Pipenv deviendrait l'outil principal de Python, mais il a connu des problèmes de performance et de fiabilité.

Par exemple, l'installation de packages dans Pipenv peut être lente. Pipenv utilise également un Pipfile au lieu de pyproject.toml, ce qui le rend moins aligné avec les standards Python modernes.

Une commande Pipenv de base pour installer requests ressemble à :

```python
pipenv install requests
```

Poetry fait la même chose avec :

```python
poetry add requests
```

La plus grande différence est la stabilité. Poetry résout les dépendances plus rapidement et de manière plus fiable. Il fonctionne bien pour les grands projets. Pipenv est plus simple que pip brut mais reste moins poli que Poetry.

### **Poetry vs Hatch**

[Hatch](https://hatch.pypa.io/latest/) est un autre outil moderne pour gérer les projets Python. Il utilise également `pyproject.toml`, il suit donc les mêmes standards que Poetry.

Hatch est connu pour être flexible et rapide. Il est populaire parmi les utilisateurs qui gèrent le packaging, les tests et le versionnement.

Hatch peut créer des environnements en utilisant :

```python
hatch env create
```

Les dépendances sont gérées à l'aide de sections dans le fichier de configuration. Hatch peut sembler plus avancé et se concentre davantage sur le packaging que sur la gestion des dépendances.

La principale différence est que Poetry essaie d'être un outil tout-en-un pour la gestion des dépendances, les environnements, la construction et la publication. Hatch offre plus de contrôle mais une expérience moins guidée.

Pour les débutants et les équipes, Poetry semble plus fluide. Hatch est puissant pour les utilisateurs avancés qui souhaitent plus de personnalisation.

## Pourquoi Poetry est agréable à utiliser

L'une des raisons pour lesquelles les développeurs apprécient Poetry est le sentiment de clarté. Tout est propre, prévisible et organisé. Lorsque vous ouvrez un projet Poetry, vous savez toujours où regarder.

Vous savez que les dépendances sont gérées correctement. Vous savez que votre build fonctionnera. Cela réduit le stress et vous rend plus confiant.

Poetry gère des choses que vous pourriez oublier. Il crée des environnements, contrôle les versions et garde votre espace de travail propre. Il possède également une interface en ligne de commande conviviale qui vous guide avec des messages utiles.

Un autre avantage est la facilité avec laquelle vous pouvez partager votre projet. Quiconque souhaite exécuter votre projet n'a qu'à lancer :

```python
poetry install
```

Cela apporte de la stabilité aux équipes et évite de nombreux problèmes courants.

## Quand Poetry pourrait ne pas être le meilleur choix

Poetry est idéal pour la plupart des projets, mais il existe des cas où il n'est peut-être pas la meilleure solution.

Si votre projet est extrêmement petit, vous n'aurez peut-être pas besoin de cette structure supplémentaire. Si vous travaillez dans un environnement qui utilise déjà pip, conda ou un autre flux de travail strict, l'introduction de Poetry peut causer des frictions.

Poetry essaie également de gérer les environnements par lui-même. Certains utilisateurs préfèrent un contrôle manuel. Dans ces cas-là, des outils comme Hatch ou pip pur peuvent mieux convenir.

Mais pour la majorité des développeurs Python, Poetry apporte une valeur énorme avec très peu de configuration.

## Conclusion

Poetry est l'un des outils les plus clairs et les plus utiles de l'écosystème Python. Il vous aide à gérer les dépendances, créer des environnements, construire des packages et les publier en toute simplicité. Il apporte structure et fiabilité à vos projets, rendant votre code plus stable et plus facile à partager.

Si vous recherchez un meilleur flux de travail pour vos projets Python, Poetry est un excellent outil à utiliser. Il maintient votre configuration propre, prévient les problèmes de version et vous offre un chemin fluide du développement à la publication. Avec quelques commandes, vous pouvez construire des projets Python solides et reproductibles sans les maux de tête habituels.

*J'espère que vous avez apprécié cet article. Inscrivez-vous à ma newsletter gratuite* [***TuringTalks.ai***](https://www.turingtalks.ai/) *pour plus de tutoriels pratiques sur l'IA. Vous pouvez également* [***visiter mon site web***](https://manishshivanandhan.com/)*.*