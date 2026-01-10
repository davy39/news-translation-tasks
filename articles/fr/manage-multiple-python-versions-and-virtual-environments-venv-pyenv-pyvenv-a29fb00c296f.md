---
title: Comment gérer plusieurs versions de Python et des environnements virtuels
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-10T15:19:39.000Z'
originalURL: https://freecodecamp.org/news/manage-multiple-python-versions-and-virtual-environments-venv-pyenv-pyvenv-a29fb00c296f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*X7729FJyghz1ADa5OGhrqg.png
tags:
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: Comment gérer plusieurs versions de Python et des environnements virtuels
seo_desc: 'By Dominic Fraser

  Addition January 2019: If you are coming back to this blog after upgrading to macOS
  Mojave please see this github issue for a solution to the common pyenv ‘zlib not
  available’ problem.

  Before we start, let’s briefly go over the term...'
---

Par Dominic Fraser

_Mise à jour janvier 2019 : Si vous revenez sur ce blog après avoir mis à niveau vers macOS Mojave, veuillez consulter [ce problème github](https://github.com/pyenv/pyenv/issues/1219#issue-363576794) pour une solution au problème courant de pyenv « zlib not available »._

Avant de commencer, passons brièvement en revue les termes utilisés dans le titre :

* **Plusieurs versions de Python** : Différentes installations de Python sur la même machine, par exemple 2.7 et 3.4.
* [**Environnements virtuels**](https://packaging.python.org/tutorials/installing-packages/#creating-virtual-environments) : environnements isolés et indépendants qui peuvent avoir à la fois une version spécifique de Python et des packages spécifiques au projet installés à l'intérieur, sans affecter d'autres projets.

Ici, nous examinerons trois outils différents pour travailler avec ceux-ci, et quand vous pourriez avoir besoin de chacun. Explorons les cas d'utilisation pour :

* `venv` / `pyvenv`
* `pyenv`
* `pyenv-virtualenv`

Si vous utilisez une **seule version** de Python, par exemple la version **3.3+**, et que vous souhaitez gérer **différents environnements virtuels**, alors `venv` est tout ce dont vous avez besoin.

Si vous souhaitez utiliser **plusieurs versions** de Python à partir de **3.3+**, **avec ou sans environnements virtuels**, alors continuez à lire sur `pyenv`.

Si vous souhaitez également travailler avec **Python 2**, alors `pyenv-virtualenv` est un outil à considérer.

### venv

À partir de Python 3.3+, le package `venv` est inclus. Il est idéal pour créer des environnements virtuels légers.

Jusqu'à Python 3.6, un script appelé `pyvenv` était également inclus comme enveloppe autour de `venv`, mais celui-ci a été [déprécié](https://docs.python.org/3/library/venv.html). Il sera complètement supprimé dans Python 3.8. La même fonctionnalité est disponible lors de l'utilisation de `venv`, et toute documentation existante doit être mise à jour. Pour ceux qui sont intéressés, vous pouvez lire [les raisons derrière la dépréciation de `pyvenv`](https://bugs.python.org/issue25154).

`venv` est utilisé pour créer un nouvel environnement via la commande terminal :

```bash
$ python3 -m venv directory-name-to-create
```

activé avec :

```bash
$ source name-given/bin/activate
```

et désactivé simplement avec :

```bash
$ deactivate
```

Si vous devez supprimer complètement l'environnement après l'avoir désactivé, vous pouvez exécuter :

```bash
$ rm -r name-given
```

Par défaut, l'environnement créé sera la version actuelle de Python que vous utilisez. Si vous écrivez de la documentation et souhaitez la sécurité supplémentaire que la bonne version de Python est utilisée par votre lecteur, vous pouvez spécifier les numéros de version majeure et mineure dans la commande, comme suit :

```bash
$ python3.6 -m venv example-three-six
```

Si le lecteur utilise une version autre que 3.6, la commande ne sera pas réussie et indiquera dans son message d'erreur. Cependant, toute version de correctif (par exemple 3.6.4) fonctionnera.

Lorsque l'environnement est actif, tout package peut être installé via `[pip](https://pip.pypa.io/en/stable/installing/#installation)` comme d'habitude. Par défaut, le nouvel environnement créé **ne** contiendra aucun package déjà installé sur la machine. Comme `pip` lui-même ne sera pas nécessairement installé sur la machine, il est recommandé de d'abord mettre à niveau `pip` vers la dernière version, en utilisant `pip install --upgrade pip`.

Les projets auront couramment un fichier `requirements.txt` spécifiant ses dépendances. Cela permet la commande raccourcie `pip install -r requirements.txt` pour installer rapidement tous les packages dans le nouvel environnement virtuel créé. Ils n'existeront que dans l'environnement virtuel. Il ne sera pas disponible lorsqu'il est désactivé mais persistera lorsqu'il est réactivé.

Si vous n'avez pas besoin d'utiliser des versions supplémentaires de Python lui-même, alors c'est tout ce dont vous avez besoin pour créer des environnements virtuels isolés et spécifiques au projet.

### [pyenv](https://github.com/pyenv/pyenv)

Si vous souhaitez utiliser plusieurs versions de Python sur une seule machine, alors `pyenv` est un outil couramment utilisé pour installer et basculer entre les versions. Cela ne doit pas être confondu avec le script `pyvenv` précédemment mentionné et déprécié. Il n'est pas fourni avec Python et doit être installé séparément.

La [documentation](https://github.com/pyenv/pyenv) de `[pyenv](https://github.com/pyenv/pyenv)` inclut une excellente description de [son fonctionnement](https://github.com/pyenv/pyenv#how-it-works), donc ici nous allons simplement voir comment l'utiliser.

Tout d'abord, nous devons l'installer. Si vous utilisez Mac OS X, nous pouvons le faire en utilisant Homebrew, sinon envisagez [d'autres options d'installation](https://github.com/pyenv/pyenv#installation).

```bash
$ brew update
$ brew install pyenv
```

Ensuite, ajoutez ce qui suit vers le bas de vos scripts shell pour permettre à `pyenv` de changer automatiquement les versions pour vous :

```bash
eval "$(pyenv init -)"
```

Pour ce faire, ouvrez votre script shell [en cours d'utilisation](https://askubuntu.com/questions/590899/how-to-check-which-shell-am-i-using) via `$ ~/.zshrc`, `$ ~/.bashrc` ou `$ ~/.bash_profile` et copiez et collez la ligne ci-dessus.

L'exécution de `pyenv versions` affichera les versions de Python actuellement installées, avec un `*` à côté de celle actuellement utilisée. `pyenv version` montre cela directement, et `python --version` peut être utilisé pour vérifier cela.

Pour installer une version supplémentaire, par exemple `3.4.0`, utilisez simplement `pyenv install 3.4.0`.

`pyenv` recherche dans quatre endroits pour décider quelle version de Python utiliser, par ordre de priorité :

1. La variable d'environnement `PYENV_VERSION` (si spécifiée). Vous pouvez utiliser la commande `[pyenv shell](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-shell)` pour définir cette variable d'environnement dans votre session shell actuelle.
2. Le fichier `.python-version` spécifique à l'application dans le répertoire actuel (si présent). Vous pouvez modifier le fichier `.python-version` du répertoire actuel avec la commande `[pyenv local](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-local)`.
3. Le premier fichier `.python-version` trouvé (le cas échéant) en recherchant dans chaque répertoire parent, jusqu'à atteindre la racine de votre système de fichiers.
4. Le fichier de version global. Vous pouvez modifier ce fichier en utilisant la commande `[pyenv global](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-global)`. Si le fichier de version global n'est pas présent, pyenv suppose que vous souhaitez utiliser le Python « système ». (En d'autres termes, quelle que soit la version qui s'exécuterait si pyenv n'était pas dans votre `PATH`.)

Lors de la configuration d'un nouveau projet qui doit utiliser Python 3.6.4, alors `pyenv local 3.6.4` serait exécuté dans son répertoire racine. Cela définirait à la fois la version et créerait un fichier `.python-version`, de sorte que les machines des autres contributeurs le prendraient en compte.

La [description complète des commandes `pyenv`](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md) est une à marquer.

#### pyenv et venv

Lors de l'utilisation de Python 3.3+, nous savons maintenant comment installer et basculer entre différentes versions de Python, et comment créer de nouveaux environnements virtuels.

Par exemple, supposons que nous configurions un projet qui devait utiliser Python 3.4.

Tout d'abord, nous pourrions définir notre version locale en utilisant `pyenv local 3.4.0`.

Si nous exécutions ensuite `python3 -m venv example-project`, un nouvel environnement virtuel serait configuré sous `example-project`, en utilisant notre Python 3.4.0 activé localement.

Nous activons en utilisant `source example-project/bin/activate` et pouvons commencer à travailler.

Ensuite, nous pourrions _optionnellement_ documenter qu'un collaborateur devrait utiliser `python3.4 -m venv <name>`. Cela signifie que même si un collaborateur n'utilisait pas pyenv, la commande `python3.4` générerait une erreur si sa version de Python n'était pas la même version majeure et mineure (3 et 4), comme nous l'avions prévu.

Alternativement, nous pourrions choisir de simplement spécifier que 3.4.0 devait être utilisé, et instruire `python3 -m venv <name>`. Si nous pensons que toute version supérieure à 3.4 est acceptable, alors nous pourrions également choisir d'utiliser `python3` plutôt que `python3.4`, car si le collaborateur utilisait 3.6, il recevrait sinon également une erreur. Cela relève d'une décision spécifique au projet.

### pyenv-virtualenv

`pyenv` peut être utilisé pour installer à la fois les versions Python 2 et 3. Cependant, comme nous l'avons vu, `venv` est limité aux versions de Python supérieures à 3.3.

`pyenv-virtualenv` est un outil pour créer des environnements virtuels intégrés avec `pyenv`, et fonctionne pour toutes les versions de Python. Il est toujours recommandé d'utiliser le `venv` officiel de Python lorsque cela est possible. Mais si, par exemple, vous créez un environnement virtuel basé sur `2.7.13`, alors cela complète `pyenv`.

Il fonctionne également bien avec les environnements [Anaconda et Miniconda](https://conda.io/docs/glossary.html#anaconda-glossary) `conda` si vous les utilisez déjà. Un outil appelé `virtualenv` existe également. Il n'est pas couvert ici, mais il est lié à la fin.

Après avoir installé `pyenv`, il peut ensuite être installé en utilisant Homebrew ([ou des alternatives](https://github.com/pyenv/pyenv-virtualenv)) comme suit :

```bash
$ brew install pyenv-virtualenv
```

Ensuite, dans votre `.zshrc`, `.bashrc`, ou `.bash_profile` (selon le shell que vous utilisez), ajoutez ce qui suit vers le bas :

```bash
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

Cela permet à `pyenv` d'activer et de désactiver les environnements automatiquement lors du déplacement des répertoires.

Pour créer un nouvel environnement virtuel, utilisez :

```bash
$ pyenv virtualenv <version> <name-to-give-it>

// par exemple

$ pyenv virtualenv 2.7.10 my-virtual-env-2.7.10
```

Les environnements existants peuvent être listés avec :

```bash
$ pyenv virtualenvs
```

Activés/désactivés avec :

```bash
$ pyenv activate <name>
$ pyenv deactivate
```

Au moment de la rédaction, lors de l'utilisation de `activate`, l'avertissement `prompt changing will be removed from future release` sera affiché. Cela est [attendu](https://github.com/pyenv/pyenv-virtualenv/issues/135#issuecomment-386154344) et ne fait référence qu'à l'affichage de `(env-name)` dans votre shell, et non à l'utilisation de la commande `activate` elle-même.

L'installation des dépendances fonctionne comme décrit dans `venv`. Contrairement à `venv`, une commande `rm -r` n'est pas nécessaire pour supprimer un environnement, une commande `[uninstall](https://github.com/pyenv/pyenv-virtualenv#delete-existing-virtualenv)` [existe](https://github.com/pyenv/pyenv-virtualenv#delete-existing-virtualenv).

### Réflexions finales

Avec ces trois outils, nous avons la capacité de collaborer sur n'importe quel projet, quelle que soit la version de Python ou des dépendances requises. Nous savons également comment documenter les instructions de configuration pour que d'autres les utilisent pour tout projet sur lequel nous travaillons.

Nous pouvons également voir la logique derrière l'utilisation de chaque ensemble, car tous les développeurs n'auront pas besoin des trois.

J'espère que cela a été utile et constitue une référence utile en combinaison avec la documentation liée ci-dessous.

Merci d'avoir lu ! 😊

### Autres sujets que j'ai explorés :

* [Mocking ES et CommonJS modules avec jest.mock()](https://medium.com/codeclan/mocking-es-and-commonjs-modules-with-jest-mock-37bbb552da43)
* [Un guide pour débutants sur le service Amazon Elastic Container Service](https://www.freecodecamp.org/news/amazon-ecs-terms-and-architecture-807d8c4960fd/)

### Ressources

* [Python Virtual Environments: A Primer](https://realpython.com/python-virtual-environments-a-primer/)
* [Dépréciation de `pyvenv`](https://bugs.python.org/issue25154)
* [Documentation Python `venv`](https://docs.python.org/3/library/venv.html)
* [`venv`](https://www.reddit.com/r/learnpython/comments/4hsudz/pyvenv_vs_virtualenv/) [vs `virtualenv`](https://www.reddit.com/r/learnpython/comments/4hsudz/pyvenv_vs_virtualenv/)
* [Quelle est la différence entre venv, pyvenv, pyenv, virtualenv, virtualenvwrapper, pipenv, etc. ?](https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe)
* [Dois-je installer `pip` ?](https://pip.pypa.io/en/stable/installing/#installation)