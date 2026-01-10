---
title: Comment créer et téléverser votre premier paquet Python sur PyPI
subtitle: ''
author: Rochdi Khalid
co_authors: []
series: null
date: '2022-04-11T15:40:44.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-and-upload-your-first-python-package-to-pypi
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/cover-image-python-packaging-blog-1.jpg
tags:
- name: package
  slug: package
- name: Python
  slug: python
seo_title: Comment créer et téléverser votre premier paquet Python sur PyPI
seo_desc: "A few weeks ago, I wanted to learn how to build my first Python package,\
  \ and I was trying to figure out where to start. \nWell, I got confused and a bit\
  \ stressed trying to find a simple and easy tutorial I could use to get started.\
  \ For this reason, I ..."
---

Il y a quelques semaines, je voulais apprendre à créer mon premier paquet Python, et j'essayais de comprendre par où commencer. 

Eh bien, j'étais confus et un peu stressé en essayant de trouver un tutoriel simple et facile que je pourrais utiliser pour commencer. Pour cette raison, j'ai décidé d'écrire ce tutoriel documentant comment j'ai créé mon premier paquet Python.

## Qu'est-ce qu'un paquet en Python ?

Avant de commencer, nous devons savoir ce que signifie un paquet en Python.

Un paquet Python est un répertoire qui contient un ensemble de modules avec un fichier de dépendance appelé `__init__.py`. Ce fichier peut être complètement vide et vous l'utilisez pour marquer le répertoire sur un disque comme un paquet Python. 

L'exemple suivant montre un exemple de répertoire de paquet :

```
package
	__init__.py
	module_a.py
	module_b.py
	module_c.py

```

Le fichier `__init__.py` est un fichier de dépendance qui aide Python à rechercher les modules disponibles dans notre répertoire de paquet. Si nous supprimons ce fichier, Python ne pourra pas importer nos modules.

## Paquets vs modules en Python

Vous devriez maintenant comprendre que les paquets Python créent un répertoire structuré avec plusieurs modules, mais qu'en est-il des modules ? Assurons-nous de comprendre la différence entre un paquet et un module :

Un **Module** correspond toujours à un seul fichier Python _turtle.py_. Il contient la logique comme les classes, les fonctions et les constantes.

Un **Paquet** est essentiellement un module qui pourrait contenir de nombreux modules ou sous-paquets.

## Structure du paquet

Les paquets ne contiennent pas seulement des modules, cependant. Ils consistent également en des scripts de haut niveau, de la documentation et des tests. L'exemple suivant montre comment un paquet Python de base peut être structuré :

```
package_name/
	docs/
	scripts/
	src/
		package_a
			__init__.py
			module_a.py
		package_b
			__init__.py
			module_b.py
	tests/
    	__init__.py
		test_module_a.py
		test_module_b.py
	LICENSE.txt
	CHANGES.txt
	MANIFEST.in
	README.txt
	pyproject.toml
	setup.py
	setup.cfg

```

Comprenons à quoi sert chaque fichier dans l'arborescence ci-dessus :

* **package_name** : représente le paquet principal.
* **docs** : inclut les fichiers de documentation sur la façon d'utiliser le paquet.
* **scripts/** : vos scripts de haut niveau.
* **src** : où votre code est placé. Il contient des paquets, des modules, des sous-paquets, etc.
* **tests** : où vous pouvez mettre des tests unitaires.
* **LICENSE.txt** : contient le texte de la licence (par exemple, MIT).
* **CHANGES.txt** : rapporte les changements de chaque version.
* **MANIFEST.in** : où vous mettez les instructions sur les fichiers supplémentaires que vous souhaitez inclure (fichiers non-code).
* **README.txt** : contient la description du paquet (format markdown).
* **pyproject.toml** : pour enregistrer vos outils de construction.
* **setup.py** : contient le script de construction pour vos outils de construction.
* **setup.cfg** : le fichier de configuration de vos outils de construction.

Notez qu'il existe deux options pour inclure nos fichiers de test dans notre paquet principal. Nous pouvons le garder au niveau supérieur comme nous l'avons fait ci-dessus ou le mettre à l'intérieur du paquet comme suit :

```
package_name/
      __init__.py
      module_a.py
      module_b.py
      test/
          __init__.py
          test_module_a.py
          test_module_b.py

```

À mon avis, je pense que garder les tests au niveau supérieur peut beaucoup aider, surtout lorsque nos tests nécessitent la lecture et l'écriture d'autres fichiers externes.

## Devriez-vous utiliser setup.cfg ou setup.py ?

Les fichiers **setup.py** et **setup.cfg** sont les outils de packaging par défaut dans PyPI, setuptools, pip et la bibliothèque standard Python. 

Ici, ils représentent les scripts de configuration et de construction pour setuptools. Ils indiquent tous deux à setuptools comment le paquet peut être construit et installé. 

Le fichier mentionné contient des informations comme la version, les paquets et les fichiers à inclure, ainsi que toutes les exigences.

L'exemple suivant montre un exemple de `setup.py` qui utilise certains arguments `setup()`. Vous pouvez trouver plus d'arguments [ici](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#setup-args) :

```python
import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "package-name",
    version = "0.0.1",
    author = "author",
    author_email = "author@example.com",
    description = "short package description",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "package URL",
    project_urls = {
        "Bug Tracker": "package issues URL",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.6"
)

```

Le fichier `setup.cfg` est écrit dans un format différent par rapport à `setup.py`, et contient essentiellement deux clés essentielles, `command` et `options`. 

La clé `command` représente l'une des commandes **distutils**, tandis que la clé `options` définit les options que la commande peut prendre en charge.

```
[command]
option = value

```

L'exemple suivant montre un exemple de `setup.cfg` qui utilise certaines métadonnées et options. Vous pouvez trouver une variété de métadonnées et d'options [ici](https://setuptools.pypa.io/en/latest/userguide/declarative_config.html) :

```
[metadata]
name = package-name
version = 0.0.1
author = name of the author
author_email = author@example.com
description = short package description
long_description = file: README.md
long_description_content_type = text/markdown
url = package url
project_urls =
    Bug Tracker = package issues url
classifiers =
    Programming Language :: Python :: 3
    License :: OSI Approved :: MIT License
    Operating System :: OS Independent

[options]
package_dir =
    = src
packages = find:
python_requires = >=3.6

[options.packages.find]
where = src

```

Les fichiers `setup.py` et `setup.cfg` sont tous deux spécifiques à setuptools. De plus, le fichier `setup.cfg` peut être déplacé en toute sécurité vers `pyproject.toml`. 

Ici, l'idée est que peut-être un jour nous voudrons passer à d'autres systèmes de construction comme **flit** ou **poetry**. Dans ce cas, tout ce que nous devrons faire est de changer l'entrée build-system (setuptools par exemple) dans `pyproject.toml` en quelque chose comme flit ou poetry plutôt que de recommencer à zéro. 

[Ici](https://packaging.python.org/en/latest/key_projects/#build) vous pouvez trouver des informations sur d'autres outils qui construisent et distribuent des paquets Python.

Peu importe quel fichier de configuration nous choisissons, nous sommes "verrouillés" dans la maintenance de ce fichier de configuration particulier, soit pyproject.toml, setup.cfg, ou setup.py.

Selon le [Guide de l'utilisateur de l'emballage Python](https://packaging.python.org/en/latest/), `setup.cfg` est préféré car il est statique, propre, plus facile à lire et évite les erreurs d'encodage.

## Comment construire votre premier paquet Python

Maintenant, il est temps de commencer à construire un simple paquet Python. Nous utiliserons setuptools comme système de construction et nous configurerons notre projet en utilisant `setup.cfg` et `pyproject.toml`.

### Configurer les fichiers du paquet

Pour ce simple paquet, nous devons structurer notre répertoire en ajoutant les fichiers de dépendance nécessaires pour préparer le paquet à la distribution. Voici comment structurer notre paquet :

```
basicpkg/
	src/
		divide
			__init__.py
			divide_by_three.py
		multiply
			__init__.py
			multiply_by_three.py
	tests/
		__init__.py
		test_divide_by_three.py
		test_multiply_by_three.py
	LICENSE.txt
	README.txt
	pyproject.toml
	setup.cfg

```

Notre paquet principal se compose de deux paquets : le premier pour diviser les nombres par trois, et l'autre pour multiplier les nombres par trois. 

De plus, nous ignorons certains fichiers comme `CONTEXT.txt`, `MANIFEST.in`, et le répertoire `docs/` pour garder les choses simples pour l'instant. Mais nous avons besoin du répertoire `test/` pour inclure nos tests unitaires afin de tester les comportements du paquet.

### Ajouter de la logique à nos modules

Comme toujours, nous garderons le fichier `__init__.py` vide. Ensuite, nous devons mettre de la logique dans nos modules pour effectuer nos opérations. 

Pour le paquet de division, ajoutons le contenu suivant dans `divide_by_three.py` pour diviser n'importe quel nombre par trois :

```python
def divide_by_three(num):
	return num / 3

```

La même logique s'applique à `multiply_by_three.py` à l'intérieur du paquet de multiplication. Mais cette fois, il s'agit de multiplier n'importe quel nombre par trois :

```python
def multiply_by_three(num):
	return num * 3

```

N'hésitez pas à ajouter plus de paquets et de modules pour effectuer d'autres types d'opérations. Par exemple, vous pouvez ajouter des paquets pour effectuer des tâches d'addition et de soustraction.

### Tester nos modules

Il est bon de pratiquer l'ajout de tests automatisés à tout programme que nous créons. Nous utiliserons `unittest` pour tester nos modules et le comportement du paquet. 

À l'intérieur du répertoire `test/`, ajoutons le code suivant à `test_divide_by_three.py` :

```python
import unittest
from divide.by_three import divide_by_three 

class TestDivideByThree(unittest.TestCase):

	def test_divide_by_three(self):
		self.assertEqual(divide_by_three(12), 4)

unittest.main()

```

Nous avons importé TestCase de `unittest` pour effectuer nos tests automatisés. Ensuite, nous avons importé notre méthode de division `divide_by_three()` du module `by_three` qui est situé à l'intérieur du paquet de division. 

Si nous supprimons le fichier `__init__.py` ici, Python ne pourra plus trouver nos modules. 

La méthode `.assertEqual()` est utilisée pour vérifier l'égalité des deux valeurs ci-dessus (divide_by_three(12) et 4). La méthode `unittest.main()` est instanciée pour exécuter tous nos tests.

La même logique s'applique à `test_multiply_by_three.py` :

```python
import unittest
from multiply.by_three import multiply_by_three

class TestMultiplyByThree(unittest.TestCase):

	def test_multiply_by_three(self):
		self.assertEqual(multiply_by_three(3), 9)

unittest.main()

```

Pour exécuter les tests, tapez ce qui suit dans votre terminal/commande :

Pour Linux :

```
python3 tests/test_divide_by_three.py

```

Pour Windows :

```
py tests/test_divide_by_three.py

```

Faites de même pour tester le module de multiplication. Si nos tests s'exécutent avec succès, vous devriez obtenir ce qui suit :

```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

```

Si vous ajoutez des paquets et modules supplémentaires, essayez d'ajouter quelques méthodes `unittest` à ceux-ci. Ce sera un bon défi pour vous.

### Configurer les métadonnées en utilisant setup.cfg

Ensuite, nous devons ajouter un fichier de configuration pour setuptools. Comme mentionné précédemment, ce fichier de configuration indiquera à setuptools comment notre paquet peut être construit et installé. 

Nous devons donc ajouter les métadonnées et options suivantes à notre fichier `setup.cfg`. Ensuite, n'oubliez pas de choisir un nom différent car j'ai déjà téléversé ce paquet avec le nom ci-dessous sur [TestPyPi](https://test.pypi.org/project/basicpkg/). Changez également d'autres informations comme l'auteur, l'email et les URLs du projet pour distribuer le paquet avec vos informations.

```
[metadata]
name = basicpkg
version = 1.0.0
author = your name
author_email = your email
description = A simple Python package
long_description = file: README.md, LICENSE.txt
long_description_content_type = text/markdown
url = https://gitlab.com/codasteroid/basicpkg
project_urls =
    Bug Tracker = https://gitlab.com/codasteroid/basicpkg/-/issues
    repository = https://gitlab.com/codasteroid/basicpkg
classifiers =
    Programming Language :: Python :: 3
    License :: OSI Approved :: MIT License
    Operating System :: OS Independent

[options]
package_dir =
    = src
packages = find:
python_requires = >=3.6

[options.packages.find]
where = src

```

Vous devriez simplement garder tout par défaut dans la catégorie options. Le package_dir localise le paquet racine où vos paquets, modules et tous vos fichiers sources Python sont situés. 

Dans la clé packages, nous pouvons lister nos paquets manuellement comme ceci `[divide, multiply]`. Mais si nous voulons obtenir tous les paquets, nous pouvons utiliser `find:` et spécifier où nous devons trouver ces paquets en utilisant `[options.packages.find]` avec la clé `where` assignée au nom du paquet racine.

Assurez-vous toujours d'inclure la clé `classifiers` dans votre fichier de configuration pour ajouter des informations importantes comme la version de Python et le système d'exploitation pour lequel notre paquet est adapté. Vous pouvez trouver la liste complète des classificateurs [ici](https://pypi.org/classifiers/).

### Créer pyproject.toml

Nous utiliserons setuptools comme système de construction. Pour informer `pip` ou d'autres outils de construction de notre système de construction, nous avons besoin de deux variables, comme vu ci-dessous. 

Nous utilisons `build-system.require` pour inclure ce dont nous avons besoin pour construire notre paquet, tandis que `build-system.build-back-end` définit l'objet qui effectuera la construction. 

Ajoutons donc le contenu suivant dans `pyproject.toml` :

```
[build-system]
requires = ['setuptools>=42']
build-backend = 'setuptools.build_meta'

```

Notez que vous pouvez déplacer toutes les configurations de `setup.cfg` vers `pyproject.toml` si vous décidez de changer le système de construction pour flit ou poetry, par exemple. Cela vous fera gagner du temps.

### Créer le README.md

Créer un bon `README.md` est important. Ajoutons une description à notre paquet et incluons quelques instructions sur la façon de l'installer :

```markdown
# `basicpkg`

Le `basicpkg` est un exemple de test simple pour comprendre les bases du développement de votre premier paquet Python. 

```

Nous pouvons également ajouter comment utiliser notre paquet comme ceci :

```markdown
from multiply.by_three import multiply_by_three
from divide.by_three import divide_by_three

multiply_by_three(9)
divide_by_three(21)

```

N'hésitez pas à ajouter toute information qui peut aider d'autres développeurs à comprendre à quoi sert votre paquet et quelques instructions sur la façon de l'installer et de travailler correctement avec lui. 

Notez que notre fichier de configuration chargera le `README.md` et il sera inclus lorsque nous distribuerons notre paquet.

### Ajouter une licence

Il est très important d'ajouter une LICENCE à votre projet pour informer les utilisateurs de la manière dont ils peuvent utiliser votre code. Choisissons une licence MIT pour notre paquet Python et ajoutons le contenu suivant à `LICENSE.txt` :

```
MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

```

N'oubliez pas de remplacer [year] par l'année en cours et [full name] par votre nom ou les noms des titulaires du droit d'auteur.

### Générer les archives de distribution

Il reste une étape pour préparer notre paquet à la distribution : générer les archives de distribution pour notre paquet Python. Pour ce faire, nous devons d'abord mettre à jour notre construction PyPA, puis générer les archives sources et construites.

Dans le terminal/cmd, exécutez les commandes suivantes à partir du même répertoire où se trouve le fichier `pyproject.toml` :

Pour Linux :

```
python3 -m pip install --upgrade build
python3 -m build

```

Pour Windows :

```
py -m pip install --upgrade build
py -m build

```

Une fois le processus ci-dessus terminé, un nouveau répertoire est généré appelé `dist/` avec deux fichiers à l'intérieur. Le fichier `.tag.tz` est l'archive source et le fichier `.whl*` est l'archive construite. Ces fichiers représentent les archives de distribution de notre paquet Python qui seront téléversées sur l'index des paquets Python et installées par `pip` dans les sections suivantes.

## Comment téléverser un paquet en Python

L'index des paquets Python est l'endroit où nous devons téléverser notre projet. Puisque notre paquet Python est en test et que nous pourrions ajouter d'autres fonctionnalités pour expérimenter avec lui, nous devons utiliser une instance séparée de PyPI appelée TestPyPI. Cette instance est spécifiquement implémentée pour les tests et l'expérimentation. Ensuite, une fois que votre paquet est prêt et répond à vos attentes, vous pouvez le téléverser sur PyPI en tant que paquet réel.

Suivons les instructions ci-dessous pour préparer notre TestPyPI à téléverser notre paquet :

1. Allez sur [TestPyPI](https://test.pypi.org/) et créez un compte.
2. Vérifiez votre adresse e-mail afin de pouvoir téléverser des paquets.
3. Mettez à jour les paramètres de votre profil (ajoutez votre photo, etc.).
4. Allez sur [api-tokens](https://test.pypi.org/manage/account/#api-tokens) et créez votre jeton API pour téléverser vos paquets en toute sécurité.
5. Sur la même page, définissez la portée sur "entire account".
6. Copiez et sauvegardez votre jeton dans un endroit sûr sur votre disque.

Ensuite, nous devons téléverser nos archives de distribution. Pour ce faire, nous devons utiliser un outil de téléversement pour téléverser notre paquet. L'outil de téléversement officiel de PyPI est **twine**, alors installons twine et téléversons nos archives de distribution sous le répertoire `dist/`.

Dans le terminal/cmd, exécutez les commandes suivantes à partir du même répertoire où se trouve le fichier `pyproject.toml` :

Pour Linux :

```
python3 -m pip install --upgrade twine
python3 -m twine upload --repository testpypi dist/*

```

Pour Windows :

```
py -m pip install --upgrade twine
py -m twine upload --repository testpypi dist/*

```

Ensuite, entrez `__token__` comme nom d'utilisateur, et le jeton (avec le préfixe pypi-) que vous avez sauvegardé comme mot de passe. Appuyez sur Entrée pour téléverser les distributions.

## Comment installer le paquet Python téléversé

Maintenant, il est temps d'installer notre paquet. Vous pouvez créer un nouvel environnement virtuel et utiliser `pip` pour l'installer depuis TestPyPI :

Pour Linux :

```
python3 -m venv env
source env/bin/activate
(env) python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps basicpkg

```

Pour Windows :

```
py -m venv env
.\env\Scripts\activate
(env) py -m pip install --index-url https://test.pypi.org/simple/ --no-deps basicpkg

```

Assurez-vous que votre environnement virtuel est activé avant de vérifier si notre paquet fonctionne correctement. 

Dans le terminal/commande, exécutez `python3` pour les utilisateurs Linux ou exécutez `py` pour les utilisateurs Windows. Ensuite, tapez le code suivant pour vous assurer que les paquets multiply et divide fonctionnent comme prévu :

```
from multiply.by_three import multiply_by_three
from divide.by_three import divide_by_three

multiply_by_three(9)
divide_by_three(21)

# Output: 27
# Output: 7

```

N'oubliez pas que nous devons importer les méthodes de nos modules dont nous avons besoin pour effectuer les opérations souhaitées, comme nous l'avons fait ci-dessus.

Hourra ! Notre paquet fonctionne comme prévu.

Ainsi, une fois que vous avez testé et expérimenté avec votre paquet, suivez les instructions ci-dessous pour téléverser votre paquet sur le vrai PyPI :

1. Allez sur [PyPI](https://pypi.org/) et créez un compte.
2. Exécutez `twine upload dist/*` dans le terminal/ligne de commande.
3. Entrez les informations d'identification du compte que vous avez enregistré sur le vrai PyPI.
4. Ensuite, exécutez `pip install [package_name]` pour installer votre paquet.

Félicitations ! Votre paquet a été installé depuis le vrai PyPI.

## Qu'est-ce qui suit ?

Ce serait génial si vous veniez avec une idée simple et construisiez votre premier vrai paquet Python. Dans cet article de blog, je me suis concentré uniquement sur les bases dont vous avez besoin pour commencer, mais il y a beaucoup à apprendre dans le monde de l'emballage. 

Espérons que ma première expérience avec le développement de paquets Python vous aide à apprendre ce dont vous avez besoin pour commencer à construire. Si vous avez des questions, n'hésitez pas à me contacter à tout moment sur [LinkedIn](https://www.linkedin.com/in/rochdi-khalid/). De plus, vous pouvez vous abonner à ma [chaîne](https://www.youtube.com/channel/UCF8iZXSsjgc8kE8hITp5rdQ) sur YouTube où je partage des vidéos sur ce que j'apprends et construis avec du code.

À la prochaine et continuez à avancer !

### Références

Voici quelques références qui m'ont aidé à développer mon premier paquet Python :

* [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
* [Configuring metadata](https://packaging.python.org/en/latest/tutorials/packaging-projects/#configuring-metadata)
* [PEP 621 – Storing project metadata in pyproject.toml](https://peps.python.org/pep-0621/#example)
* [Glossary - Python Packaging User Guide](https://packaging.python.org/en/latest/glossary/#term-Source-Archive)