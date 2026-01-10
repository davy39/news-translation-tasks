---
title: Améliorez votre projet Django avec ces meilleures pratiques
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-28T13:04:20.000Z'
originalURL: https://freecodecamp.org/news/improve-your-django-project-with-these-best-practices-47fd60a7bff3
coverImage: https://cdn-media-1.freecodecamp.org/images/0*G-4pTI8lP3Q7qqan.png
tags:
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Améliorez votre projet Django avec ces meilleures pratiques
seo_desc: 'By Ofir Chakon

  Django is a robust, open-source, Python-based framework for building web applications.
  Its popularity has increased during the last couple of years, and it is already
  mature and widely-used with a large community behind it.

  Among other...'
---

Par Ofir Chakon

Django est un framework robuste, open-source et basé sur Python pour la création d'applications web. Sa popularité a augmenté au cours des dernières années, et il est déjà mature et largement utilisé avec une grande communauté derrière lui.

Parmi les autres frameworks basés sur Python pour créer des applications web (comme Flask et Pyramid), Django est de loin le plus populaire. Il supporte à la fois les versions Python 2.7 et Python 3.6. Mais au moment de la rédaction de cet article, Python 2.7 est toujours la version la plus accessible en termes de communauté, de paquets tiers et de documentation en ligne. Django est sécurisé lorsqu'il est utilisé correctement et offre une grande flexibilité. C'est la voie à suivre pour développer des applications côté serveur en utilisant Python.

![Image](https://cdn-media-1.freecodecamp.org/images/0fhElZZVnCaM3AzwCpOMncCGFoCrdwVr03xU)
_Tendances Google des 3 frameworks de développement web Python les plus populaires_

En tant que développeur Python et Django expérimenté, je vais partager avec vous quelques meilleures pratiques pour une configuration Django que j'ai apprises et collectées au fil des ans. Que vous ayez quelques projets Django à votre actif ou que vous soyez sur le point de commencer votre premier projet à partir de zéro, les meilleures pratiques décrites ici pourraient vous aider à créer de meilleures applications à l'avenir.

J'ai écrit cet article avec un état d'esprit très pratique afin que vous puissiez ajouter certains outils à votre boîte à outils de développement immédiatement. Vous pouvez même créer un modèle avancé personnalisé pour vos prochains projets.

Pour les besoins de cet article, je suppose que vous utilisez une machine Linux Ubuntu. Tout au long de l'article, certaines lignes de code commencent par un signe `$`. Ceux-ci sont utilisés pour souligner que cette ligne doit être insérée dans le terminal. Assurez-vous de copier la ligne **sans** le signe `$`.

### Environnement virtuel

Lors du développement d'applications basées sur Python, l'utilisation de paquets tiers est une chose courante. Ces paquets sont souvent mis à jour, il est donc essentiel de les organiser. Lors du développement de plus en plus de projets sur la même machine locale, il est difficile de suivre la version actuelle de chaque paquet. Il est impossible d'utiliser différentes versions du même paquet pour différents projets. De plus, la mise à jour d'un paquet sur un projet peut rompre la fonctionnalité sur un autre, et vice versa.

C'est là que l'environnement virtuel Python est utile. Pour installer un environnement virtuel, utilisez :

```bash
$ apt-get update
$ apt-get install python-pip python-dev build-essential

$ export LC_ALL="en_US.UTF-8" # peut être nécessaire en cas d'erreur de la ligne suivante

$ pip install --upgrade pip
$ pip install --upgrade virtualenv
$ mkdir ~/.virtualenvs
$ pip install virtualenvwrapper
$ export WORKON_HOME=~/.virtualenvs
$ nano ~/.bashrc
```

Ajoutez cette ligne à la fin du fichier :

```
. /usr/local/bin/virtualenvwrapper.sh
```

Puis exécutez :

```bash
$ . .bashrc
```

Après l'installation, créez un nouvel environnement virtuel pour votre projet en tapant :

```bash
$ mkvirtualenv project_name
```

Lorsque vous êtes dans le contexte de votre environnement virtuel, vous remarquerez qu'un préfixe est ajouté au terminal, comme :

```bash
(project_name) ofir@playground:~$
```

Pour désactiver (quitter) l'environnement virtuel et revenir au contexte principal de Python de votre machine locale, utilisez :

```bash
$ deactivate
```

Pour activer (démarrer) le contexte de l'environnement virtuel, utilisez :

```bash
$ workon project_name
```

Pour lister les environnements virtuels existants sur votre machine locale, utilisez :

```bash
$ lsvirtualenv
```

Maintenir les dépendances de votre projet (paquets) dans un environnement virtuel sur votre machine vous permet de les garder dans un environnement isolé. Vous ne les utilisez que pour un seul (ou plusieurs) projet(s). Lorsque vous créez un nouvel environnement virtuel, vous commencez avec un environnement frais sans paquets installés. Vous pouvez ensuite utiliser, par exemple :

```bash
(project_name) $ pip install Django
```

pour installer Django dans votre environnement virtuel, ou :

```bash
(project_name) $ pip install Django==1.11
```

pour installer la version 1.11 de Django accessible uniquement depuis l'environnement.

Ni votre interpréteur Python principal ni les autres environnements virtuels sur votre machine ne pourront accéder au nouveau paquet Django que vous venez d'installer.

Pour utiliser la commande runserver avec votre environnement virtuel, tout en étant dans le contexte de l'environnement virtuel, utilisez :

```bash
(project_name) $ cd /path/to/django/project
(project_name) $ ./manage.py runserver
```

De même, lorsque vous entrez dans l'interpréteur Python depuis l'environnement virtuel, tapez :

```bash
(project_name) $ python
```

Il aura accès aux paquets que vous avez déjà installés dans l'environnement.

![Image](https://cdn-media-1.freecodecamp.org/images/F2e5Os6yhtJWucJ5YGWQ-BFvDGrkxvbBSmPp)

### Exigences

Les exigences sont la liste des paquets Python (dépendances) que votre projet utilise lors de son exécution, y compris la version pour chaque paquet. Voici un exemple de fichier `requirements.txt` :

```
dicttoxml==1.7.4
Django==1.11.2
h5py==2.7.0
matplotlib==2.0.2
numpy==1.13.0
Pillow==4.1.1
psycopg2==2.7.1
pyparsing==2.2.0
python-dateutil==2.6.0
pytz==2017.2
six==1.10.0
xmltodict==0.11.0
```

Maintenir votre fichier `requirements.txt` à jour est essentiel pour collaborer correctement avec d'autres développeurs. C'est également important pour garder votre environnement de production correctement configuré. Ce fichier, lorsqu'il est inclus dans votre dépôt de code, vous permet de mettre à jour tous les paquets installés dans votre environnement virtuel en exécutant une seule ligne dans le terminal. Vous pouvez ainsi mettre de nouveaux développeurs en route en un rien de temps.

Pour générer un nouveau fichier `requirements.txt` ou pour mettre à jour un fichier existant, utilisez depuis votre environnement virtuel :

```bash
(project_name) $ pip freeze > requirements.txt
```

Pour votre commodité, assurez-vous d'exécuter cette commande dans un dossier qui est suivi par votre dépôt Git. Cela permet à d'autres instances du code d'avoir également accès au fichier `requirements.txt`.

Si un nouveau développeur rejoint l'équipe, ou si vous souhaitez configurer un nouvel environnement en utilisant les mêmes paquets listés dans le fichier `requirements.txt`, exécutez dans le contexte de l'environnement virtuel :

```bash
(project_name) $ cd /path/to/requirements/file
(project_name) $ pip install -r requirements.txt
```

Toutes les exigences listées dans le fichier seront immédiatement installées dans votre environnement virtuel. Les versions plus anciennes seront mises à jour et les versions plus récentes seront rétrogradées pour correspondre à la liste exacte de `requirements.txt`. Soyez prudent cependant, il peut y avoir des différences entre les environnements que vous souhaitez toujours respecter.

Je vous recommande vivement d'intégrer ces commandes à votre flux de travail. Mettez à jour le fichier requirements.txt avant de pousser le code vers le dépôt et installez le fichier requirements.txt après avoir tiré le code du dépôt.

![Image](https://cdn-media-1.freecodecamp.org/images/SPVepaHtCvW26vwKEhtRl4AvZMzcFgegQPd-)
_Crédit : [https://www.djangoproject.com/](https://www.djangoproject.com/" rel="noopener" target="_blank" title=")_

### Meilleure configuration de `settings.py`

Django est livré avec un fichier `settings.py` très basique mais utile. Cela définit les configurations principales et les plus utiles pour votre projet. Le fichier `settings.py` est très simple. Mais parfois, en tant que développeur travaillant en équipe, ou lors de la configuration d'un environnement de production, vous avez besoin de plus d'un fichier `settings.py` de base.

Plusieurs fichiers de configuration vous permettent de définir facilement des configurations sur mesure pour chaque environnement séparément, comme :

```py
ALLOWED_HOSTS # pour l'environnement de production
DEBUG
DATABASES # pour différents développeurs de la même équipe
```

Permettez-moi de vous présenter une approche étendue pour configurer votre fichier `settings.py`. Elle vous permet de maintenir différentes versions et d'utiliser celle que vous souhaitez à tout moment et dans n'importe quel environnement.

Tout d'abord, naviguez jusqu'au chemin de votre fichier `settings.py` :

```bash
(project_name) $ cd /path/to/settings/file
```

Ensuite, créez un nouveau module appelé settings (un module est un dossier contenant un fichier `__init__.py`) :

```bash
(project_name) $ mkdir settings
```

Maintenant, renommez votre fichier `settings.py` en base.py et placez-le à l'intérieur du nouveau module que vous avez créé :

```bash
(project_name) $ mv settings.py settings/base.py
```

Pour cet exemple, je suppose que vous souhaitez configurer un fichier de paramètres pour votre environnement de développement et un autre pour votre environnement de production. Différents développeurs de la même équipe peuvent utiliser la même approche pour définir différents fichiers de paramètres.

Pour votre environnement de développement, créez :

```bash
(project_name) $ nano settings/development.py
```

Puis tapez :

```py
from .base import *

DEBUG = True
```

et enregistrez le fichier en appuyant sur `Ctrl + O`, Entrée puis `Ctrl + X`.

Pour votre environnement de production, créez :

```bash
(project_name) $ nano settings/production.py
```

et tapez :

```py
from .base import *

DEBUG = False
ALLOWED_HOSTS = ['app.project_name.com', ]
```

Maintenant, chaque fois que vous souhaitez ajouter ou mettre à jour les paramètres d'un environnement spécifique, vous pouvez facilement le faire dans son propre fichier de paramètres.

Vous vous demandez peut-être comment Django sait quel fichier de paramètres charger dans chaque environnement ? C'est à cela que sert le fichier `__init__.py`. Lorsque Django recherche le fichier `settings.py` qu'il utilisait pour charger lors de l'exécution du serveur, par exemple, il trouve maintenant un module de paramètres plutôt qu'un fichier `settings.py`. Mais tant qu'il s'agit d'un module contenant un fichier `__init__.py`, pour Django, c'est exactement la même chose. Django chargera le fichier `__init__.py` et exécutera ce qui y est écrit.

Par conséquent, nous devons définir quel fichier de paramètres nous voulons charger à l'intérieur du fichier `__init__.py` en exécutant :

```bash
(project_name) $ settings/__init__.py
```

puis, pour un environnement de production, par exemple, en tapant :

```py
from .production import *
```

De cette façon, Django chargera tous les paramètres de base.py et production.py à chaque fois qu'il démarre. Magique ?

Maintenant, la seule configuration restante est de garder le fichier `__init__.py` dans votre fichier `.gitignore` afin qu'il ne soit pas inclus dans les pushes et pulls. Une fois que vous avez configuré un nouvel environnement, n'oubliez pas de créer un nouveau fichier `__init__.py` à l'intérieur du module de paramètres. Ensuite, importez le fichier de paramètres requis exactement comme nous l'avons fait précédemment.

Dans cet article, nous avons couvert trois meilleures pratiques pour mieux configurer votre projet Django :

* Travailler dans un environnement virtuel
* Garder le fichier `requirements.txt` à jour et l'utiliser continuellement dans votre flux de travail
* Configurer un meilleur tableau de paramètres de projet

Avez-vous suivi ces meilleures pratiques dans votre dernier projet ? Avez-vous des idées à partager ? Les commentaires sont grandement appréciés.

Avez-vous trouvé cela utile ? Si oui, donnez-moi quelques applaudissements pour que plus de gens voient l'article.

Ceci est la partie 1 de la série sur les meilleures pratiques pour le développement Django. Suivez-moi pour obtenir une mise à jour immédiate dès que les prochaines parties seront disponibles.

Trouvez plus de conseils pour les entrepreneurs technologiques sur [CodingStartups](https://codingstartups.com/choose-cloud-computing-technology-startup/).