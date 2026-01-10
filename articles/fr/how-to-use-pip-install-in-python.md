---
title: Comment utiliser pip install en Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-19T21:49:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-pip-install-in-python
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9dba740569d1a4ca3953.jpg
tags:
- name: Python
  slug: python
- name: toothbrush
  slug: toothbrush
seo_title: Comment utiliser pip install en Python
seo_desc: 'Python comes with several built-in modules, but the Python community has
  more to offer. It’s the modules that makes python so powerful!

  Third party modules add so much more functionality to Python. So it''s time to learn
  how to install these modules s...'
---

Python est livré avec plusieurs modules intégrés, mais la communauté Python a plus à offrir. Ce sont les modules qui rendent Python si puissant !

Les modules tiers ajoutent beaucoup plus de fonctionnalités à Python. Il est donc temps d'apprendre à installer ces modules afin de pouvoir les utiliser dans nos programmes.

La manière la plus simple est d'utiliser `pip`

```text
pip install <module_name>
```

Si vous avez utilisé `npm`, vous pouvez le considérer comme le _npm_ de Python.

Note : La différence est qu'avec npm, `npm install` installe par défaut les packages localement dans un projet, alors que `pip install` installe par défaut globalement. 

Pour installer des modules localement, vous devez créer et activer ce qu'on appelle un [environnement virtuel](https://docs.python-guide.org/dev/virtualenvs/), afin que `pip install` installe dans le dossier où se trouve cet environnement virtuel, plutôt que globalement (ce qui peut nécessiter des privilèges d'administrateur).

La dernière fois, dans le wiki `import-statements`, nous avons utilisé le module `requests` comme exemple. Comme il s'agit d'un module tiers, nous devons l'installer séparément après avoir installé Python.

L'installer serait aussi simple que `pip install requests`. Vous pouvez même passer divers arguments avec. Celui que vous rencontrerez plus souvent est `--upgrade`. Vous pouvez mettre à jour un module Python avec :

```text
pip install <module_name> --upgrade
```

Par exemple, pour mettre à jour le module requests à sa dernière version, ce serait aussi simple que `pip install requests --upgrade`.

Avant d'utiliser `pip`, vous devrez l'installer (c'est assez simple). Vous pouvez l'installer depuis [ici](https://packaging.python.org/en/latest/tutorials/installing-packages/).

Il suffit de cliquer sur le lien. Et d'enregistrer le fichier sous `get-pip.py`. *Veuillez ne pas oublier l'extension `.py`.* Et de l'exécuter.

Une alternative à l'utilisation de pip serait d'essayer [`easy_install`](https://bootstrap.pypa.io/ez_setup.py).

Utiliser `easy_install` est également simple. La syntaxe est :

```text
easy_install <module_name>
```

Cependant, `pip` est plus populaire que l'utilisation de `easy_install`.

**Note :** Sur certains systèmes où Python 2 et Python 3 sont installés, `pip` et `pip3` feront des choses différentes. `pip` installe la version Python 2 du package, et `pip3` installera la version Python 3 du package. 

Pour plus d'informations sur la différence entre Python 2 et 3, voir [ce](https://www.freecodecamp.org/news/how-to-learn-python/#heading-python-2-vs-python-3-whats-the-difference) guide. Vous pouvez vérifier la version de `pip` en faisant `pip --version` et/ou `pip3 --version` :

```text
pip3 --version
pip 18.0 from /usr/local/lib/python3.5/dist-packages/pip (python 3.5)
```

Nous pouvons également créer un fichier txt contenant une liste de modules qui doivent être installés en utilisant pip. Par exemple, nous pourrions créer le fichier `requirements.txt` et son contenu :

```text
Kivy-Garden==0.1.4
macholib==1.5.1
idna==2.6
geoip2nation==0.1.2
docutils>=0.14
Cython
```

Dans ce fichier, nous pourrions également définir une version pour l'installation. Après cela, en invoquant pip avec :

```text
 pip install -r <FILE CONTAINING MODULES>
 
          OU DANS NOTRE CAS
 
 pip install -r requirements.txt
 
```

il devrait installer tous les modules listés dans le fichier.