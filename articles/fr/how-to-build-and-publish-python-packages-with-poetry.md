---
title: Comment créer et publier des packages Python avec Poetry
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2023-04-05T18:04:44.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-and-publish-python-packages-with-poetry
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/phone-number-validator.png
tags:
- name: Python
  slug: python
seo_title: Comment créer et publier des packages Python avec Poetry
seo_desc: "A Python package is a collection of Python modules that can be easily distributed\
  \ and installed. It allows developers to reuse code across multiple projects and\
  \ share it with others. \nPython packages typically include a set of functions,\
  \ classes, or ..."
---

Un package Python est une collection de modules Python qui peuvent être facilement distribués et installés. Il permet aux développeurs de réutiliser du code dans plusieurs projets et de le partager avec d'autres.

Les packages Python incluent généralement un ensemble de fonctions, de classes ou d'autres composants qui servent un objectif spécifique, tel que l'analyse de données, le développement web ou l'apprentissage automatique.

Vous avez peut-être utilisé des packages Python intégrés tels que `os`, `sys` ou `math`, ou des dépendances externes telles que `requests`, `pandas` ou `numpy` dans vos projets Python.

Ce tutoriel vous guidera à travers le processus de création et de publication d'un package Python avec [Poetry](https://python-poetry.org/). Vous allez créer un package de validation de numéros de téléphone pour vérifier si un numéro de téléphone donné est valide. En cours de route, vous apprendrez à utiliser Poetry pour gérer les dépendances, définir les configurations de package et écrire des tests pour le package.

À la fin de ce tutoriel, vous devriez avoir une bonne compréhension de l'utilisation de Poetry pour créer et publier vos propres packages Python.

## Qu'est-ce que Poetry ?

Poetry est un outil moderne pour la gestion de packages en Python qui simplifie le processus de création, de gestion et de publication de packages Python.

Il fournit une interface en ligne de commande facile à utiliser pour gérer les dépendances, construire des packages et les publier sur [PyPI](https://pypi.org) (Python Package Index), le dépôt officiel des packages Python.

Il existe plusieurs avantages à utiliser Poetry pour la gestion de packages en Python :

* **Résolution des dépendances** : Il gère automatiquement les dépendances et garantit que votre package est compatible avec d'autres packages dans votre projet.
* **Environnements virtuels** : Il crée un environnement virtuel pour votre projet, ce qui vous permet d'isoler votre package et ses dépendances du reste de votre système.
* **Échafaudage de projet** : Il fournit une interface en ligne de commande simple pour créer de nouveaux projets Python et configurer leur structure de base.
* **Construction et packaging intégrés** : Il fournit des outils pour créer des packages distribuables dans une variété de formats, y compris les distributions de source, les distributions wheel et les distributions binaires.
* **Publication sur PyPI** : Il facilite la publication de votre package sur PyPI, permettant à d'autres développeurs d'installer et d'utiliser facilement votre package.

Dans l'ensemble, Poetry fournit une interface simple et intuitive pour gérer les dépendances, construire des packages et les publier sur PyPI. Si vous travaillez sur un projet Python qui nécessite une gestion de packages, Poetry vaut définitivement la peine d'être exploré.

## Prérequis

Pour suivre ce tutoriel, il est recommandé d'avoir les éléments suivants :

* Python 3.7+ installé
* Compréhension de base des [environnements virtuels, modules et packages](https://docs.python.org/3/tutorial/venv.html)
* Connaissance de base de [Requests](https://blog.ashutoshkrris.in/how-to-interact-with-web-services-using-python) et [PyTest](https://pytest.org/)

Vous pouvez trouver les exemples de code utilisés dans ce tutoriel dans [ce dépôt](https://github.com/ashutoshkrris/phone-number-validator).

## Comment configurer le projet

Avant de pouvoir commencer à construire votre package Python, vous devez configurer votre environnement de développement. Cela implique d'installer Poetry, de créer un nouveau projet et de configurer les dépendances du projet.

### Comment installer Poetry

Poetry est un gestionnaire de packages et un outil de construction multiplateforme qui peut être installé sur divers systèmes d'exploitation, y compris Linux, macOS et Windows.

Il dispose d'un installeur personnalisé qui crée un environnement virtuel dédié pour Poetry, ce qui garantit qu'il fonctionne indépendamment du reste du système. Cet environnement isolé empêche les mises à niveau ou suppressions accidentelles de dépendances, permettant à Poetry de gérer ses dépendances plus efficacement.

Pour installer Poetry, la première étape consiste à ouvrir le terminal ou l'invite de commande, selon le système d'exploitation que vous utilisez.

Pour les utilisateurs de Windows, ouvrez Windows Powershell et exécutez la commande suivante :

```ps1
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

Pour les utilisateurs de Linux, macOS et Windows Subsystem for Linux (WSL), ouvrez le terminal et exécutez la commande suivante :

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Notez que sur certains systèmes, la commande `python` peut faire référence à Python 2 au lieu de Python 3. Pour éviter toute ambiguïté, il est recommandé d'utiliser le binaire `python3` à la place.

Une fois le processus d'installation terminé, vous pouvez vérifier si Poetry est installé correctement en exécutant la commande suivante :

```bash
poetry --version
```

Si vous voyez une sortie similaire à `Poetry (version 1.4.1)`, votre installation est complète et prête à être utilisée.

### Comment créer un nouveau projet

Pour créer un nouveau projet Poetry, vous pouvez utiliser la commande `new` suivie du nom du projet. Par exemple, si vous souhaitez créer un package pour valider les numéros de téléphone, vous pouvez utiliser la commande suivante :

```bash
poetry new phone-number-validator
```

Cela créera un nouveau dossier appelé `phone-number-validator` avec la structure suivante :

```bash
phone-number-validator
├── pyproject.toml
├── README.md
├── phone_number_validator
│   └── __init__.py
└── tests
    └── __init__.py
```

Le dossier `phone-number-validator` contient deux fichiers : `pyproject.toml` et `README.md`, ainsi que deux packages : `phone_number_validator` pour stocker les fichiers de code source et `tests` pour stocker les fichiers de test.

#### Comprendre le fichier `pyproject.toml`

Le fichier `pyproject.toml` sert de fichier de configuration pour un projet Poetry, contenant des informations sur le projet et ses dépendances. Le fichier a trois tables par défaut – `tool.poetry`, `tool.poetry.dependencies`, et `build-system`.

```toml
[tool.poetry]
name = "phone-number-validator"
version = "0.1.0"
description = ""
authors = ["Ashutosh Krishna <ashutoshbritish@gmail.com>"]
readme = "README.md"
packages = [{include = "phone_number_validator"}]
```

La table `tool.poetry` dans le fichier `pyproject.toml` a plusieurs paires clé/valeur, avec `name`, `version`, `description`, et `authors` étant obligatoires tandis que les autres sont optionnels.

Poetry suppose qu'un package avec le même nom que `tool.poetry.name` spécifié dans le fichier `pyproject.toml` est situé à la racine du projet. Mais si l'emplacement du package est différent, les packages et leurs emplacements peuvent être spécifiés dans la clé `tool.poetry.packages`.

```toml
[tool.poetry.dependencies]
python = "^3.11"
```

Dans la table `tool.poetry.dependencies`, il est obligatoire de déclarer la version de Python pour laquelle le package est compatible.

```toml
[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

La dernière table, `build-system`, a deux clés – `requires` et `build-backend`. La clé `requires` est une liste de dépendances requises pour construire le package, tandis que la clé `build-backend` est l'objet Python utilisé pour effectuer le processus de construction.

TOML est le format de configuration préféré de Poetry, et à partir de la version 3.11, Python fournit le module `tomllib` pour analyser les fichiers TOML.

Pour l'instant, le fichier `pyproject.toml` ressemble à [celui-ci](https://github.com/ashutoshkrris/phone-number-validator/blob/c1b69d414437f857742a2009743d8a0d8dbf90b8/pyproject.toml).

### Comment créer un nouvel environnement virtuel

Poetry simplifie la création d'environnements virtuels pour vos projets. Pour créer un environnement virtuel pour votre bibliothèque `phone-number-validator`, naviguez jusqu'à votre répertoire de projet et exécutez la commande `env use` :

```bash
poetry env use /full/path/to/python
```

Le `/full/path/to/python` spécifie le chemin complet vers l'exécutable Python.

Par exemple, sur MacOS :

```bash
poetry env use /usr/local/bin/python3.11
```

Sur Windows :

```bash
poetry env use "C:\\Users\\ashut\\AppData\\Local\\Programs\\Python\\Python311\\python.exe"
```

### Comment configurer les dépendances du projet

Après avoir configuré votre projet Poetry, l'étape suivante consiste à installer les dépendances nécessaires.

Puisque vous allez [interagir avec un service web externe](https://blog.ashutoshkrris.in/how-to-interact-with-web-services-using-python), la première dépendance dont vous aurez besoin est `requests`. Pour installer cette dépendance, Poetry fournit une commande `add` qui s'occupe d'installer le package correctement, de définir les contraintes de version et de mettre à jour le fichier `pyproject.toml` avec les informations appropriées.

```bash
poetry add requests
```

Une fois la dépendance installée, vous verrez la dépendance ajoutée dans la table `tool.poetry.dependencies` dans votre fichier `pyproject.toml`.

```toml
[tool.poetry.dependencies]
python = "^3.11"
requests = "^2.28.2"
```

#### Le fichier `poetry.lock`

Le fichier `poetry.lock` sert d'enregistrement de toutes les versions exactes des dépendances utilisées dans un projet lors de l'installation, de la suppression ou de la mise à jour de toute dépendance. Il garantit que votre projet utilise les bonnes versions des dépendances en listant tous les packages, leurs versions exactes et les hachages de leurs fichiers sources.

Une fois que vous avez installé la bibliothèque `requests`, le fichier `[poetry.lock](https://github.com/ashutoshkrris/phone-number-validator/blob/main/poetry.lock)` sera mis à jour pour enregistrer la version exacte et le hachage de la dépendance installée. À mesure que vous ajoutez plus de dépendances dans votre projet, ce fichier suivra tous les changements.

Il est important de commiter le fichier `poetry.lock` dans votre contrôle de version lorsque vous partagez votre projet, car il garantit que les autres utiliseront les mêmes versions de dépendances que vous avez utilisées pour construire et tester votre projet.

Pour créer un fichier `requirements.txt` à partir du fichier `poetry.lock`, vous pouvez utiliser la commande suivante :

```bash
poetry export --output requirements.txt
```

## Comment développer le package

À ce stade, vous avez installé la bibliothèque requests mais votre application ne fait encore rien. Dans cette section, vous allez commencer à construire la fonctionnalité de votre application.

Pour commencer, créez un nouveau fichier appelé `validator.py` à l'intérieur du package `phone_number_validator` et suivez les instructions.

Dans ce tutoriel, vous allez utiliser les principes de la [Programmation Orientée Objet](https://blog.ashutoshkrris.in/object-oriented-programming-in-python) pour construire votre application. Pour commencer, créez une classe appelée `PhoneNumberValidator` :

```python
class PhoneNumberValidator:
    pass

```

Ensuite, vous devez créer un constructeur pour la classe. Par défaut, nous voulons que l'utilisateur fournisse sa propre clé API. Donc, le constructeur doit prendre un argument `api_key`. De plus, le constructeur doit initialiser l'attribut `api_url` à _https://api.numlookupapi.com/v1/validate/_ :

```python
class PhoneNumberValidator:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.api_url = "https://api.numlookupapi.com/v1/validate/"
```

Avec cela, vous avez une structure de classe de base en place. Vous pouvez maintenant commencer à ajouter plus de fonctionnalités à la classe `PhoneNumberValidator`.

Ensuite, vous devez définir une méthode que l'utilisateur peut utiliser pour valider un numéro de téléphone. Cette méthode sera appelée `validate()`.

```python
def validate(self, phone_number: str, country_code: str = None) -> bool:
    if not phone_number:
        raise ValueError("Le numéro de téléphone ne peut pas être vide !")
    response = self._make_api_call(phone_number, country_code)
    if response.ok:
       return response.json()["valid"]
   else:
       response.raise_for_status()
```

La méthode prend deux paramètres : `phone_number`, qui est un paramètre de chaîne requis, et `country_code`, qui est un paramètre de chaîne optionnel avec une valeur par défaut de `None`. La méthode retourne une valeur booléenne indiquant si le numéro de téléphone est valide ou non.

La méthode vérifie d'abord si le paramètre `phone_number` n'est pas vide. S'il est vide, une `ValueError` est levée. Ensuite, la méthode appelle une méthode `_make_api_call()` (définie plus tard) avec les paramètres `phone_number` et `country_code` pour faire un appel API afin de valider le numéro de téléphone.

Si l'appel API réussit, c'est-à-dire qu'il retourne un code de statut 200, la méthode retourne la valeur booléenne de la clé `valid` dans la réponse JSON. Si l'appel API échoue, une `HTTPError` est levée avec le code de statut et le message fournis par la réponse API.

Puisque la méthode ci-dessus utilise une méthode `_make_api_call()` pour faire l'appel API, définissons cette méthode :

```python
import requests

def _make_api_call(self, phone_number: str, country_code: str = None)
    params = {"apikey": self.api_key}
    if country_code:
        params["country_code"] = country_code
    response = requests.get(self.api_url + phone_number, params=params)
    return response
```

La méthode `_make_api_call()` est une méthode privée de la classe `PhoneNumberValidator`, qui fait un appel API à [NumLookupAPI](https://numlookupapi.com/) pour valider un numéro de téléphone.

La méthode prend deux arguments, `phone_number` (une chaîne représentant le numéro de téléphone à valider) et `country_code` (une chaîne optionnelle représentant le code pays ISO Alpha 2 pour le numéro de téléphone).

La méthode retourne un objet `requests.Response`, qui contient la réponse retournée par l'appel API. La variable `params` est un dictionnaire contenant la clé API et, si fourni, le code pays. La méthode `requests.get()` est utilisée pour envoyer une requête GET à l'API avec le numéro de téléphone et les paramètres.

Si l'appel API réussit, la méthode retourne l'objet de réponse, qui sera traité par la méthode `validate()`. Si l'appel API échoue, une exception sera levée avec le message d'erreur.

Votre classe `PhoneNumberValidator` ressemblera à [celle-ci](https://github.com/ashutoshkrris/phone-number-validator/blob/main/phone_number_validator/validator.py) à ce stade.

Note : vous pouvez en apprendre plus sur NumLookupAPI dans sa [documentation officielle](https://numlookupapi.com/docs/validate) ici.

### Exemple d'utilisation de la classe `PhoneNumberValidator` (Optionnel)

Vous avez maintenant terminé l'implémentation de la fonctionnalité de validation des numéros de téléphone. Pour tester votre application, vous pouvez créer un fichier nommé `main.py` dans le répertoire racine de votre projet. Notez que cette étape est optionnelle.

Dans `main.py`, vous pouvez utiliser la classe `PhoneNumberValidator` en l'important depuis le module `phone_number_validator.validator`. Ensuite, vous pouvez créer une instance de la classe en passant votre clé API comme argument au constructeur.

Pour obtenir la clé API, inscrivez-vous pour un compte gratuit sur [NumLookupAPI](https://app.numlookupapi.com/register) et copiez la clé depuis le tableau de bord :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-01-181245.png)

Après cela, vous pouvez appeler la méthode `validate` sur l'instance avec les numéros de téléphone que vous souhaitez valider. La méthode `validate` retourne une valeur booléenne indiquant si le numéro de téléphone est valide ou non.

Voici un exemple de code pour `main.py` :

```python
from phone_number_validator.validator import PhoneNumberValidator

validator = PhoneNumberValidator(api_key="votre-cle-api-ici")
is_valid1 = validator.validate("+15551234")
is_valid2= validator.validate("+12069220880")
is_valid3= validator.validate("2069220880", country_code="US")
print(is_valid1)
print(is_valid2)
print(is_valid3)
```

Sortie :

```bash
False
True
True
```

## Comment tester le package

Dans cette section, vous allez tester le package `phone_number_validator` en utilisant [Pytest](https://docs.pytest.org/en/7.2.x/). Les tests sont une partie essentielle du développement logiciel, car ils garantissent que notre code fonctionne comme prévu et aident à détecter les bugs ou problèmes potentiels avant qu'ils ne soient déployés en production. Vous allez écrire des cas de test pour vérifier la fonctionnalité de la classe `PhoneNumberValidator` et de ses méthodes.

### Comment installer les dépendances de test

Dans Poetry, un groupe de dépendances est un moyen de regrouper les dépendances ensemble. L'utilisation la plus courante des groupes de dépendances est de séparer les dépendances de développement et de production. Lors de l'installation des dépendances, vous pouvez choisir quel groupe de dépendances installer.

Pour installer les packages `pytest` et `requests-mock` dans un groupe appelé `test`, exécutez la commande suivante :

```bash
poetry add pytest requests-mock --group test
```

Dans la commande ci-dessus, vous avez utilisé l'option `--group` pour spécifier le nom du groupe, `test` dans ce cas. Après avoir installé les dépendances, votre fichier `pyproject.toml` ressemble à ceci :

```toml
[tool.poetry]
name = "phone-number-validator"
version = "0.1.0"
description = ""
authors = ["Ashutosh Krishna <ashutoshbritish@gmail.com>"]
readme = "README.md"
packages = [{include = "phone_number_validator"}]

[tool.poetry.dependencies]
python = "^3.11"
requests = "^2.28.2"


[tool.poetry.group.test.dependencies]
pytest = "^7.2.2"
requests-mock = "^1.10.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

```

### Comment écrire les tests

Pour rappel, vous avez précédemment créé une méthode `validate` pour valider les numéros de téléphone. Maintenant que vous avez installé les dépendances nécessaires à l'environnement de test, il est temps d'écrire le code pour tester la fonctionnalité de votre application.

Créez un fichier `test_validator.py` à l'intérieur de votre package `tests` et ajoutez le code suivant :

```python
import pytest
from phone_number_validator.validator import PhoneNumberValidator


VALID_PHONE_NUMBER="+12069220880"
INVALID_PHONE_NUMBER="+15551234"
PHONE_NUMBER_WITHOUT_COUNTRY_CODE="2069220880"


@pytest.fixture
def validator():
    return PhoneNumberValidator(api_key="test_api_key")
```

Le code importe les modules nécessaires pour écrire les cas de test. Le décorateur `@pytest.fixture` est utilisé pour définir une [fixture](https://docs.pytest.org/en/6.2.x/fixture.html#) `validator()` qui crée une nouvelle instance de la classe `PhoneNumberValidator` avec le paramètre `test_api_key`. Cette fixture peut être utilisée dans plusieurs tests pour créer une nouvelle instance de `PhoneNumberValidator`.

Ensuite, ajoutez les cas de test suivants après la fixture :

```python
def test_valid_phone_number(validator, requests_mock):
    requests_mock.get(validator.api_url + VALID_PHONE_NUMBER, json={"valid": True})
    assert validator.validate(VALID_PHONE_NUMBER) == True


def test_invalid_phone_number(validator, requests_mock):
    requests_mock.get(validator.api_url + INVALID_PHONE_NUMBER, json={"valid": False})
    assert validator.validate(INVALID_PHONE_NUMBER) == False


def test_api_call_failure(validator, requests_mock):
    requests_mock.get(validator.api_url, status_code=500)
    with pytest.raises(Exception):
        validator.validate(INVALID_PHONE_NUMBER)


def test_phone_number_without_country_code(validator, requests_mock):
    requests_mock.get(
        validator.api_url + PHONE_NUMBER_WITHOUT_COUNTRY_CODE, json={"valid": True, "country_code": "US"}
    )
    assert validator.validate(PHONE_NUMBER_WITHOUT_COUNTRY_CODE, country_code="US") == True


def test_phone_number_with_unsupported_country_code(validator, requests_mock):
    requests_mock.get(validator.api_url, status_code=400)
    with pytest.raises(Exception):
        validator.validate(VALID_PHONE_NUMBER, country_code="ZZ")


def test_invalid_api_key(validator, requests_mock):
    requests_mock.get(validator.api_url, status_code=401)
    with pytest.raises(Exception):
        validator.validate(VALID_PHONE_NUMBER)


def test_invalid_phone_number_type(validator):
    with pytest.raises(TypeError):
        validator.validate(5551234)


def test_empty_phone_number(validator):
    with pytest.raises(ValueError):
        validator.validate("")

```

Chaque fonction de test définit un scénario qui teste si la méthode `validate()` fonctionne correctement pour une entrée donnée. Les cas de test couvrent les scénarios suivants :

1. `test_valid_phone_number` : Ce cas de test vérifie si la méthode `validate` retourne `True` pour un numéro de téléphone valide. Le numéro de téléphone utilisé pour ce test est `+12069220880`, et la réponse de l'API est simulée pour retourner `{"valid": True}`.
2. `test_invalid_phone_number` : Ce cas de test vérifie si la méthode `validate` retourne `False` pour un numéro de téléphone invalide. Le numéro de téléphone utilisé pour ce test est `+15551234`, et la réponse de l'API est simulée pour retourner `{"valid": False}`.
3. `test_api_call_failure` : Ce cas de test vérifie si une exception est levée lorsqu'il y a une défaillance dans l'appel API. Le numéro de téléphone utilisé pour ce test est un numéro de téléphone invalide (`+15551234`), et l'appel API est simulé pour retourner un code de statut `500`.
4. `test_phone_number_without_country_code` : Ce cas de test vérifie si la méthode `validate` peut valider un numéro de téléphone sans code pays, en spécifiant le code pays comme argument. Le numéro de téléphone utilisé pour ce test est `2069220880`, et la réponse de l'API est simulée pour retourner `{"valid": True, "country_code": "US"}`.
5. `test_phone_number_with_unsupported_country_code` : Ce cas de test vérifie si une exception est levée lorsqu'un code pays non supporté est spécifié. Le numéro de téléphone utilisé pour ce test est un numéro de téléphone valide (`+12069220880`), et l'appel API est simulé pour retourner un code de statut `400`.
6. `test_invalid_api_key` : Ce cas de test vérifie si une exception est levée lorsqu'une clé API invalide est utilisée. Le numéro de téléphone utilisé pour ce test est un numéro de téléphone valide (`+12069220880`), et l'appel API est simulé pour retourner un code de statut `401`.
7. `test_invalid_phone_number_type` : Ce cas de test vérifie si une exception est levée lorsque le numéro de téléphone passé à la méthode `validate` n'est pas une chaîne.
8. `test_empty_phone_number` : Ce cas de test vérifie si une exception est levée lorsqu'une chaîne vide est passée comme numéro de téléphone à la méthode `validate`.

Votre fichier `test_validator.py` devrait ressembler à [celui-ci](https://github.com/ashutoshkrris/phone-number-validator/blob/main/tests/test_validator.py) à ce stade.

Pour exécuter les tests, il est important d'exécuter la commande `pytest` à l'intérieur de l'environnement virtuel. Poetry fournit une commande `run` pour exécuter la commande donnée à l'intérieur de l'environnement virtuel du projet. Exécutez donc la commande suivante pour exécuter les tests :

```bash
poetry run pytest -v
```

Sortie :

```bash
poetry run pytest -v
============================================== test session starts ===============================================
platform win32 -- Python 3.11.0, pytest-7.2.2, pluggy-1.0.0 -- C:\Users\ashut\AppData\Local\pypoetry\Cache\virtualenvs\phone-number-validator-j1Sa98gs-py3.11\Scripts\python.exe
cachedir: .pytest_cache
rootdir: D:\Blog-Codes\phone-number-validator
plugins: requests-mock-1.10.0
collected 8 items

tests/test_validator.py::test_valid_phone_number PASSED                                                     [ 12%] 
tests/test_validator.py::test_invalid_phone_number PASSED                                                   [ 25%] 
tests/test_validator.py::test_api_call_failure PASSED                                                       [ 37%] 
tests/test_validator.py::test_phone_number_without_country_code PASSED                                      [ 50%]
tests/test_validator.py::test_phone_number_with_unsupported_country_code PASSED                             [ 62%] 
tests/test_validator.py::test_invalid_api_key PASSED                                                        [ 75%] 
tests/test_validator.py::test_invalid_phone_number_type PASSED                                              [ 87%] 
tests/test_validator.py::test_empty_phone_number PASSED                                                     [100%] 

=============================================== 8 passed in 0.05s ================================================ 
```

## Comment publier le package

À ce stade de votre projet, vous avez créé une bibliothèque qui peut valider les numéros de téléphone et vous avez écrit des cas de test pour garantir sa fonctionnalité.

Si vous souhaitez rendre cette bibliothèque disponible pour les autres, vous pouvez la publier en ligne. Poetry fournit un moyen simple de publier un package en utilisant la commande publish.

Mais avant de pouvoir publier votre bibliothèque, vous devez la packager avec la commande build :

```bash
poetry build
```

Sortie :

```bash
Building phone-number-validator (0.1.0)
  - Building sdist
  - Built phone_number_validator-0.1.0.tar.gz
  - Building wheel
  - Built phone_number_validator-0.1.0-py3-none-any.whl
```

Packager un projet avant de le publier est une étape cruciale, car cela simplifie le processus de distribution, d'installation et d'utilisation pour les autres.

Poetry utilise les informations spécifiées dans le fichier `pyproject.toml` telles que le nom du projet, la version et les dépendances pour packager le projet dans deux formats différents – sdist et wheel. Les distributions wheel sont des packages précompilés qui peuvent être installés rapidement, tandis que les distributions de source contiennent le code source brut et nécessitent une compilation.

Pour publier votre bibliothèque, vous devrez [configurer correctement vos identifiants PyPI](https://python-poetry.org/docs/repositories/#configuring-credentials), car Poetry publiera la bibliothèque sur PyPI par défaut.

Une fois la bibliothèque packagée, vous pouvez utiliser la commande `publish` pour la publier.

```bash
poetry publish
```

Après avoir exécuté la commande `poetry publish`, votre package sera publié sur le Python Package Index (PyPI), ce qui le rend disponible pour l'installation via Poetry.

Sortie :

```bash
Publishing phone-number-validator (0.1.0) to PyPI
 - Uploading phone_number_validator-0.1.0-py3-none-any.whl 0%
 - Uploading phone_number_validator-0.1.0-py3-none-any.whl 100%
 - Uploading phone_number_validator-0.1.0.tar.gz 0%
 - Uploading phone_number_validator-0.1.0.tar.gz 100%
```

Une fois le package publié, il peut être recherché sur PyPI. Par exemple, vous pouvez rechercher la bibliothèque `[phone-number-validator](https://pypi.org/project/phone-number-validator/)` sur PyPI. Après l'avoir trouvée, vous pouvez l'installer sur votre système et essayer de l'utiliser.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-03-212242.png)

## Conclusion

Dans ce tutoriel, j'ai expliqué comment Poetry fonctionne et comment utiliser ses fonctionnalités. Vous avez appris à créer un nouveau projet Poetry, à gérer les dépendances et à gérer les versions. Vous avez également appris à écrire et exécuter des tests en utilisant Pytest, et à packager et publier votre bibliothèque Python sur PyPI en utilisant Poetry.

En suivant ce tutoriel, vous avez maintenant les compétences nécessaires pour créer, gérer et distribuer vos propres packages Python avec facilité. Avec une exploration et une pratique supplémentaires, vous pouvez élargir vos connaissances de Poetry et l'utiliser pour développer et partager vos propres bibliothèques Python pour que les autres les utilisent.

Si vous avez suivi ce tutoriel et construit votre propre package, je vous encourage à partager votre création avec le monde ! Prenez une capture d'écran ou enregistrez une vidéo de votre application en action, et partagez-la sur Twitter. N'oubliez pas de me taguer, [@ashutoshkrris](https://twitter.com/ashutoshkrris), afin que je puisse voir votre travail et le partager avec mes abonnés.

J'ai hâte de voir ce que vous avez créé ! Bon codage !

### Ressources supplémentaires

* [Dépôt Github](https://github.com/ashutoshkrris/phone-number-validator) pour le tutoriel
* [Comment interagir avec les services web en Python](https://blog.ashutoshkrris.in/how-to-interact-with-web-services-using-python)
* [Documentation de NumLookupAPI](https://numlookupapi.com/docs/)