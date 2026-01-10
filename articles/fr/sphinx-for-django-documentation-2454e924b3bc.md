---
title: Comment documenter votre projet Django à l'aide de l'outil Sphinx
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-08T06:26:25.000Z'
originalURL: https://freecodecamp.org/news/sphinx-for-django-documentation-2454e924b3bc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*aBjEUaDShrMB9RFqbl_saQ.jpeg
tags:
- name: Django
  slug: django
- name: documentation
  slug: documentation
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: Comment documenter votre projet Django à l'aide de l'outil Sphinx
seo_desc: 'By Goran Aviani

  I recently visited a company where I had a nice talk with one of its employees.
  We talked about technology and programming. Then we touched the subject of project
  documentation. Specifically how React does it automatically but Django ...'
---

Par Goran Aviani

J'ai récemment visité une entreprise où j'ai eu une conversation intéressante avec l'un de ses employés. Nous avons parlé de technologie et de programmation. Ensuite, nous avons abordé le sujet de la documentation des projets. Plus précisément, comment React le fait automatiquement, mais pas Django. Cela m'a fait réfléchir à la nécessité de faire de la documentation automatique pour mes projets Django.

Je n'ai pas trouvé de documentation pertinente sur la manière de procéder, donc cela m'a pris un peu plus de temps que prévu. Non pas parce que c'était difficile, mais parce que j'ai trouvé que la documentation officielle de Sphinx et d'autres ressources étaient obsolètes ou obscures.

Aujourd'hui, j'ai donc créé un tutoriel simple mais complet qui explique comment faire de la documentation Django en utilisant l'outil de documentation Sphinx sous Ubuntu.

#### **Installer Sphinx**

Tout d'abord, vous devez entrer dans l'environnement virtuel de votre projet Django.

L'installation de Sphinx est assez simple avec pip3 (pip pour Python 3) :

```bash
pip3 install sphinx
```

#### Créer un répertoire de documentation

Une fois que vous avez installé Sphinx, vous devrez créer le dossier racine des documents. Ce dossier contiendra votre documentation et d'autres fichiers dont vous aurez besoin (images, pages "à propos", etc.).

Créez votre dossier racine de documents dans le dossier principal de votre projet et nommez-le /docs.

Pour démarrer Sphinx, exécutez cette commande à l'intérieur de votre dossier /docs :

```bash
sphinx-quickstart
```

Vous aurez maintenant beaucoup d'options. Dans la plupart des cas, vous pouvez simplement retaper l'option par défaut, mais il y a quelques options auxquelles vous devez prêter attention.

Voici comment j'ai répondu :

```
Bienvenue dans l'utilitaire de démarrage rapide de Sphinx 1.7.5.

Veuillez entrer les valeurs pour les paramètres suivants (appuyez simplement sur Entrée pour
accepter une valeur par défaut, si elle est donnée entre crochets).

Chemin racine sélectionné : .

Vous avez deux options pour placer le répertoire de construction pour la sortie de Sphinx.
Soit vous utilisez un répertoire "_build" dans le chemin racine, soit vous séparez
les répertoires "source" et "build" dans le chemin racine.

> Séparer les répertoires source et build (o/n) [n] : n

Dans le répertoire racine, deux autres répertoires seront créés ; "_templates"
pour les modèles HTML personnalisés et "_static" pour les feuilles de style personnalisées et autres fichiers statiques. Vous pouvez entrer un autre préfixe (tel que ".") pour remplacer le tiret bas.

> Préfixe de nom pour les répertoires templates et static [_] : _

Le nom du projet apparaîtra à plusieurs endroits dans la documentation générée.
> Nom du projet : Votre_nom_de_projet
> Nom de l'auteur(s) : Goran Aviani
> Version du projet [] : 1.0

Si les documents doivent être écrits dans une langue autre que l'anglais,
vous pouvez sélectionner une langue ici par son code de langue. Sphinx traduira alors
le texte qu'il génère dans cette langue.

Pour une liste des codes pris en charge, voir
http://sphinx-doc.org/config.html#confval-language.

> Langue du projet [en] : en

Le suffixe de nom de fichier pour les fichiers source. Communément, il s'agit soit de "txt"
soit de "rst". Seuls les fichiers avec ce suffixe sont considérés comme des documents.

> Suffix des fichiers source [.rst] : .rst

Un document est spécial en ce sens qu'il est considéré comme le nœud supérieur de l'
"arbre des contenus", c'est-à-dire qu'il est la racine de la structure hiérarchique
des documents. Normalement, il s'agit de "index", mais si votre document "index"
est un modèle personnalisé, vous pouvez également le définir sur un autre nom de fichier.

> Nom de votre document principal (sans suffixe) [index] : index

Sphinx peut également ajouter une configuration pour la sortie epub :

> Voulez-vous utiliser le générateur epub (o/n) [n] : n

Indiquez quelles extensions Sphinx suivantes doivent être activées :

> autodoc : insérer automatiquement les docstrings des modules (o/n) [n] : y
> doctest : tester automatiquement les extraits de code dans les blocs doctest (o/n) [n] : y
> intersphinx : lier la documentation Sphinx de différents projets (o/n) [n] : n
> todo : écrire des entrées "todo" qui peuvent être affichées ou masquées lors de la construction (o/n) [n] : y
> coverage : vérifie la couverture de la documentation (o/n) [n] : y
> imgmath : inclure des maths, rendues en images PNG ou SVG (o/n) [n] : y
> mathjax : inclure des maths, rendues dans le navigateur par MathJax (o/n) [n] : n
> ifconfig : inclusion conditionnelle de contenu basée sur les valeurs de configuration (o/n) [n] : n
> viewcode : inclure des liens vers le code source des objets Python documentés (o/n) [n] : n
> githubpages : créer un fichier .nojekyll pour publier le document sur GitHub pages (o/n) [n] : n
Un Makefile et un fichier de commande Windows peuvent être générés pour vous afin que vous
n'ayez qu'à exécuter par exemple `make html` au lieu d'invoquer directement sphinx-build.
> Créer un Makefile ? (o/n) [y] : y
> Créer un fichier de commande Windows ? (o/n) [y] : y

Création du fichier ./conf.py.
Création du fichier ./index.rst.
Création du fichier ./Makefile.
Création du fichier ./make.bat.

Terminé : Une structure de répertoire initiale a été créée.

Vous devriez maintenant remplir votre fichier principal ./index.rst et créer d'autres fichiers sources de documentation. Utilisez le Makefile pour construire les docs, comme ceci :

make builder

où "builder" est l'un des générateurs pris en charge, par exemple html, latex ou linkcheck.
```

#### Connexion Django

Dans le dossier de votre projet, trouvez /docs/conf.py et, à l'intérieur, quelque part près du haut du fichier, trouvez "#import os". Juste en dessous, écrivez ceci :

```py
import os
import sys
import django
sys.path.insert(0, os.path.abspath('..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'Votre_nom_de_projet.settings'
django.setup()
```

**Il y a maintenant deux façons de procéder :**

1. Vous pouvez utiliser _sphinx-apidoc_ pour générer une documentation complètement automatique, ou
2. Vous pouvez construire vos propres modules qui seront affichés dans la documentation.

Dans ce tutoriel, je vais vous montrer comment faire les deux.

#### 1. Sphinx-apidoc

Il s'agit de la méthode la plus simple où vous devez simplement naviguer jusqu'à votre dossier /docs et exécuter :

```bash
sphinx-apidoc -o . ..
```

Maintenant, vous devez construire votre documentation en exécutant la commande :

```bash
make html
```

Naviguez jusqu'à _Votre_dossier_de_projet/docs/_build/html_ et ouvrez _index.html_. Il s'agit de la page d'index de votre documentation.

#### 2. Construire vos propres modules

Il s'agit de la méthode un peu plus compliquée, mais elle vous donnera beaucoup plus de liberté pour organiser votre documentation.

Maintenant, vous allez vouloir faire de la documentation sur vos vues, modules, etc. Mais d'abord, laissez-moi vous montrer un exemple simple, juste pour que vous compreniez la logique de cette partie :

Allez dans votre dossier /docs et créez un nouveau dossier nommé "modules". À l'intérieur, créez un fichier nommé all-about-me.rst :

```bash
mkdir modules
touch modules/all-about-me.rst
```

À l'intérieur de all-about-me.rst, écrivez quelque chose comme ceci :

```rest
############
Tout sur moi
############

Je suis Goran Aviani, un développeur Django.
```

Maintenant, vous avez créé quelque chose à afficher dans votre documentation, mais vous n'avez toujours pas d'endroit pour l'afficher. Retournez dans le dossier /docs et ouvrez index.rst et juste en dessous de ce code :

```rest
.. toctree::
   :maxdepth: 2
   :caption: Contenu :
```

Ajoutez ceci :

```rest
modules/all-about-me.rst
```

Faites en sorte qu'il y ait une ligne vide entre le code supérieur et la ligne ajoutée :

```rest
.. toctree::
   :maxdepth: 2
   :caption: Contenu :

   modules/all-about-me.rst
```

Maintenant, vous devez construire votre documentation. Changez l'emplacement pour le dossier qui contient le Makefile (c'est-à-dire le dossier /docs). Ensuite, exécutez dans le terminal :

```bash
make html
```

Vous trouverez votre documentation dans

> Votre_dossier_de_projet/docs/_build/html et ouvrez index.html

Vous pouvez faire de même pour vos vues Django :

À l'intérieur du dossier /modules, créez le fichier views.rst.

```bash
touch views.rst
```

À l'intérieur du fichier views.rst, écrivez ceci :

```rest
Vues
======

.. automodule:: yourapp.views
   :members:
   :undoc-members:
```

À l'intérieur de index.rst, juste sous modules/all-about-me.rst, ajoutez ceci :

```rest
modules/views.rst
```

Maintenant, vous devez à nouveau construire votre documentation en exécutant "make html" à l'intérieur de votre dossier /docs :

```bash
make html
```

Vous avez compris l'idée ? D'abord, vous créez le fichier .rst, puis vous le placez à l'intérieur de index.rst pour qu'il puisse être affiché sur la page index.html.

Vous pouvez faire de même pour vos modèles. Allez dans votre dossier /modules et créez le fichier models.rst.

```bash
touch models.rst
```

Vous pouvez ajouter quelque chose comme ceci dans votre fichier models.rst :

```rest
Modèles
=======

.. automodule:: yourapp.models
   :members:
   :undoc-members:
```

À l'intérieur de index.rst, juste sous modules/views.rst, collez :

```rest
modules/models.rst
```

À l'intérieur de votre dossier /docs, exécutez :

```bash
make html
```

#### Test de la documentation

Vous pouvez tester votre documentation en exécutant ce code à l'intérieur de votre dossier /docs :

```bash
make linkcheck
```

Voilà ! Vous avez terminé !

Il s'agit de mon premier tutoriel public, alors donnez-moi quelques applaudissements si vous l'aimez :)

Merci d'avoir lu ! Consultez d'autres articles comme celui-ci sur mon profil freeCodeCamp : [https://www.freecodecamp.org/news/author/goran/](https://www.freecodecamp.org/news/author/goran/) et d'autres choses amusantes que je construis sur ma page GitHub : [https://github.com/GoranAviani](https://github.com/GoranAviani)