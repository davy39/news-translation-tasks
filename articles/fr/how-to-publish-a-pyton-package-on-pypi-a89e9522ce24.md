---
title: Comment publier votre propre package Python sur PyPi
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-09-19T02:09:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-publish-a-pyton-package-on-pypi-a89e9522ce24
coverImage: https://cdn-media-1.freecodecamp.org/images/1*OebmlFYpKPFJJ-qT2qSfiA.jpeg
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Comment publier votre propre package Python sur PyPi
seo_desc: 'By Marco Massenzio

  Want to share your Python code with other developers? Want to make your users’ lives
  easier when installing your package? Then you should publish your Python packages
  to PyPi.

  The good news is that it is now easier than ever. This ...'
---

Par Marco Massenzio

Vous souhaitez partager votre code Python avec d'autres développeurs ? Vous voulez faciliter la vie de vos utilisateurs lors de l'installation de votre package ? Alors vous devriez publier vos packages Python sur PyPi.

La bonne nouvelle, c'est que c'est maintenant plus facile que jamais. Voici un guide court qui vous guidera tout au long du processus et vous orientera vers la documentation pertinente en cours de route.

### Étape #1 : Créer un fichier setup.py

Les arguments pour _setup()_ sont documentés [ici](https://packaging.python.org/distributing/#setup-args) et ne sont pas triviaux. Un bon exemple à suivre est le fichier _setup.py_ de mon projet [filecrypt](https://github.com/massenz/filecrypt).

Voici un bref extrait. Encore une fois, assurez-vous de [lire la documentation](https://packaging.python.org/distributing/#setup-args) pour plus d'informations à ce sujet, car elle explique ce que signifient tous ces arguments bien mieux que je ne pourrais le faire, même avec un article complet de Medium pour le faire :

```
setup(name='crytto',      description='Un utilitaire de chiffrement et de déchiffrement de fichiers basé sur OpenSSL',      long_description=long_description,      version='0.2.0',      url='https://github.com/massenz/filecrypt',      author='M. Massenzio',      author_email='marco@alertavert.com',      license='Apache2',      classifiers=[          'Development Status :: 4 - Beta',          'Intended Audience :: System Administrators',          'License :: OSI Approved :: Apache Software License',          'Programming Language :: Python :: 3'      ],      packages=['crytto'],      install_requires=[          'PyYAML>=3.11',          'sh>=1.11'      ],      entry_points={          'console_scripts': [              'encrypt=crytto.main:run'          ]      })
```

**Note :** Ne confondez **pas** setuptools avec distutils — voici l'importation correcte pour setup.py :

```
from setuptools import setup
```

La partie la plus délicate consiste à déterminer les noms des packages et la configuration correcte pour vos _fichiers de script_. Il est probablement préférable de décider cela à l'avance, mais vous pouvez toujours rectifier cela lors de la création de votre setup.py.

Le plus grand défi est de trouver un nom de package de premier niveau qui n'entre pas en conflit avec un nom existant. Pour autant que je sache, c'est actuellement surtout un processus d'essais et d'erreurs.

Une fois que le setup.py est en bon état, vous pouvez essayer de construire une wheel :

```
python setup.py bdist_wheel
```

Après avoir fait cela, il est bon de créer un nouvel environnement virtuel et d'essayer d'installer le nouveau package dans celui-ci :

```
virtualenv test_env
./test_env/bin/activate
pip install dist/my-project.whl
```

Cela est particulièrement utile pour tester si les _console_scripts_ ont été correctement configurées.

Si vous utilisez des _classifiers_ comme dans :

```
classifiers=[     'Development Status :: 4 - Beta',     'Intended Audience :: System Administrators',     'License :: OSI Approved :: Apache Software License',    'Programming Language :: Python :: 3']
```

… alors assurez-vous de consulter la [liste des classifiers](https://pypi.python.org/pypi?%3Aaction=list_classifiers), car toute autre chose provoquera une erreur et empêchera l'enregistrement.

### Enregistrer votre projet

![Image](https://cdn-media-1.freecodecamp.org/images/0kPl1058z7-o9Hw-0VLNSkuHpuIjLTsx7R6i)

**Note :** La documentation m'a dit d'utiliser twine pour cette étape, mais cela n'a pas fonctionné pour moi. Votre expérience peut varier.

Sauf si vous avez déjà un compte sur PyPi, vous devrez [en créer un](https://pypi.python.org/pypi?%3Aaction=register_form), puis vous connecter.

Vous pouvez ensuite vous rendre sur le [formulaire d'enregistrement](https://pypi.python.org/pypi?%3Aaction=submit_form) et télécharger votre fichier **PKG_INFO**. Celui-ci a été créé dans un répertoire _[nom du projet].egg-info/_. Cela peut prendre un peu de va-et-vient, pendant que vous essayez d'apaiser les dieux de PyPi pour qu'ils acceptent vos choix de configuration.

En particulier, trouver un nom de package non conflictuel mais significatif peut prendre plus de tentatives que vous ne le pensez. Encore une fois, je vous recommande de planifier, car je n'ai pas trouvé de moyen facile de lister **tous** les noms de packages. Si vous en connaissez un, n'hésitez pas à laisser un commentaire. Vous noterez que, selon PyPi…

```
Il y a actuellement 88906 packages ici.
```

(« ici » étant PyPi, au 16 septembre 2016).

### Télécharger sur PyPi

Une fois l'enregistrement réussi, le téléchargement proprement dit est assez facile, en utilisant twine :

```
twine upload dist/*
```

À condition que vous ayez un ~/.pypirc valide, il vous demandera simplement votre mot de passe. Ensuite, vous devez simplement :

```
$ cat ~/.pypirc
[distutils]
index-servers=pypi
```

```
[pypi]
repository = https://upload.pypi.org/legacy/
username = [votre nom d'utilisateur]
```

C'est tout. Bonnes constructions et partage de vos packages Python !

_Je suis l'auteur original de cet article sur mon blog à l'adresse [codetrips.com](https://codetrips.com/2016/09/19/how-to-publish-a-pyton-package-on-pypi/).