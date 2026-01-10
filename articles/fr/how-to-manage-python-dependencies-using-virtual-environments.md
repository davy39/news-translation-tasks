---
title: Comment gérer les dépendances Python à l'aide d'environnements virtuels
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-22T20:39:56.000Z'
originalURL: https://freecodecamp.org/news/how-to-manage-python-dependencies-using-virtual-environments
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/0_T4VpXQchm1Vr05bL.jpg
tags:
- name: Python
  slug: python
- name: virtualenv
  slug: virtualenv
seo_title: Comment gérer les dépendances Python à l'aide d'environnements virtuels
seo_desc: "By Saransh Kataria\nWhen we start building a Python project that goes beyond\
  \ simple scripts, we tend to start using third-party dependencies. \nWhen working\
  \ on a larger project, we need to think about managing these dependencies in an\
  \ efficient manner...."
---

Par Saransh Kataria

Lorsque nous commençons à construire un projet Python qui va au-delà de simples scripts, nous avons tendance à commencer à utiliser des dépendances tierces. 

Lorsque nous travaillons sur un projet plus important, nous devons penser à gérer ces dépendances de manière efficace. Et lors de l'installation des dépendances, nous voulons toujours être dans des environnements virtuels. Cela aide à garder les choses bien organisées. Cela aide également à éviter de désorganiser notre environnement Python.

# Pourquoi avons-nous besoin d'environnements virtuels Python ?

Nous pouvons utiliser Pip pour installer des packages dans notre projet Python. Et il est courant d'avoir plusieurs packages installés dans un seul projet Python. Cela peut entraîner certains problèmes concernant les versions des packages installés et leurs dépendances.

Lorsque nous utilisons `pip install <nom du package>` dans un projet, nous installons le package et ses dépendances dans l'espace de noms global Python. Et cela installera le package pour la version spécifique de Python que nous avons configurée pour Python. 

Nous pouvons découvrir où se trouve ce répertoire en utilisant

```shell
python3.7 -c "import sys; print('\n'.join(sys.path))"

/usr/lib/python27.zip
/usr/lib/python2.7
/usr/lib/python2.7/lib-dynload
/usr/lib/python2.7/site-packages
```

Et si nous installons le même package en utilisant `pip3 install <nom du package>`, il sera installé dans un répertoire séparé avec la version Python 3. Nous pouvons surmonter cela en utilisant la commande suivante :

```shell
 python2.7 -m pip install <nom du package>
```

Cela ne résout toujours pas notre problème de packages installés à l'échelle du système, ce qui peut entraîner les problèmes suivants :

* Différents projets ayant différentes versions du même package entreront en conflit les uns avec les autres
* Les dépendances d'un projet peuvent entrer en conflit avec les dépendances au niveau du système, ce qui peut casser le système entièrement
* Les projets multi-utilisateurs ne sont pas une possibilité
* Tester le code contre différentes versions de Python et de bibliothèques est une tâche difficile

Pour éviter ces problèmes, les développeurs Python utilisent des environnements virtuels. Ces environnements virtuels utilisent des contextes isolés (répertoires) pour installer des packages et des dépendances.

# Comment créer un environnement virtuel

Nous avons besoin d'un outil pour utiliser les environnements virtuels Python. L'outil que nous utilisons pour les créer est connu sous le nom de [venv](https://docs.python.org/3/library/venv.html). Il est intégré dans la bibliothèque standard Python pour Python 3.3+.

Si nous utilisions Python 2, nous aurions dû l'installer manuellement. C'est l'un des rares packages que nous voulons installer globalement.

```shell
python2 -m pip install virtualenv
```

Note : Nous parlerons davantage de venv dans cet article et de Python 3 puisque il y a quelques différences entre celui-ci et virtualenv. Les commandes sont un peu différentes et les outils fonctionnent différemment sous le capot.

Nous commencerons par créer un nouveau répertoire dans lequel nous voulons travailler avec notre projet.

```shell
mkdir my-python-project && cd my-python-project
```

Ensuite, nous créerons un nouvel environnement virtuel :

```shell
python3 -m venv virtualenv

# crée un environnement virtuel appelé virtualenv, le nom peut être n'importe quoi
```

Cela créera un répertoire appelé virtualenv dans le répertoire que nous venons de créer. Le répertoire contiendra un dossier bin, un dossier lib, un dossier include et un fichier de configuration d'environnement. 

Tous ces fichiers garantissent que tout le code Python est exécuté dans le contexte de l'environnement actuel. Cela nous aide à obtenir l'isolation des environnements globaux et évite les problèmes que nous avons discutés précédemment.

Pour commencer à utiliser cet environnement, nous devons l'activer. Ce faisant, cela changera également notre invite de commande au contexte actuel.

```shell
$ source env/bin/activate
(virtualenv) $
```

L'invite est également un indicateur que l'environnement virtuel est actif et que le code Python s'exécute sous cet environnement.

À l'intérieur de notre environnement, les packages système ne sont pas accessibles et tout package installé à l'intérieur de l'environnement n'est pas disponible à l'extérieur.

Seuls `pip` et `setuptools` sont installés par défaut dans un environnement virtuel.

Après avoir activé un environnement, la variable de chemin est modifiée pour réaliser le concept d'environnements virtuels.

Lorsque nous avons terminé et que nous voulons passer à l'environnement global, nous pouvons quitter en utilisant la commande deactivate :

```shell
(virtualenv) $ deactivate 
$
```

# Comment gérer les dépendances entre les environnements

Maintenant que nous avons configuré nos environnements virtuels, nous ne voulons pas continuer à partager les packages qui peuvent être installés en utilisant pip. Nous voulons exclure notre dossier d'environnement virtuel et pouvoir reproduire notre travail sur un système différent. 

Nous pouvons le faire en utilisant un fichier de requirements dans le répertoire racine de notre projet.

Supposons que nous avons installé Flask dans notre environnement virtuel. Après cela, si nous exécutons `pip freeze`, il listera les packages que nous avons installés et leurs numéros de version.

```shell
(virtualenv) $ pip freeze
Flask==1.1.2
```

Nous pouvons écrire cela dans un fichier requirements.txt pour le télécharger sur Git, ou le partager avec d'autres personnes sous une autre forme.

```shell
(virtualenv) $ pip freeze > requirements.txt
```

Cette commande peut également être utilisée pour mettre à jour le fichier.

Et ensuite, chaque fois que quelqu'un veut exécuter notre projet sur son ordinateur, tout ce qu'il a à faire est :

```shell
$ cd copied-project/
$ python3 -m venv virtualenv/
$ python3 -m pip install -r requirements.txt
```

Et tout fonctionnera comme sur notre système. 

## Conclusion

Maintenant, nous pouvons gérer les environnements virtuels Python et ainsi gérer les dépendances et les packages selon les besoins. Si vous avez des questions à ce sujet, n'hésitez pas à nous contacter.

_Vous pouvez trouver d'autres articles de moi à [_https://www.wisdomgeek.com_](https://www.wisdomgeek.com/development/web-development/python/managing-python-dependencies-using-virtual-environments/)._