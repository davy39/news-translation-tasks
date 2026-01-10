---
title: Pourquoi vous avez besoin d'environnements Python et comment les gérer avec
  Conda
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-21T15:09:43.000Z'
originalURL: https://freecodecamp.org/news/why-you-need-python-environments-and-how-to-manage-them-with-conda-85f155f4353c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KhP3BJNqy4MC8GPfUz4r-Q.jpeg
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Pourquoi vous avez besoin d'environnements Python et comment les gérer
  avec Conda
seo_desc: 'By Gergely Szerovay

  I have over two decades of professional experience as a developer, I know a wide
  variety of frameworks and programming languages, and one of my favorites is Python.
  I’ve been teaching it for quite some time now, and according to m...'
---

Par Gergely Szerovay

Je possède plus de deux décennies d'expérience professionnelle en tant que développeur, je connais une grande variété de frameworks et de langages de programmation, et l'un de mes préférés est Python. J'enseigne ce langage depuis un certain temps maintenant, et selon mon expérience, **la configuration des environnements Python** est un **sujet complexe**.

Ainsi, ma principale motivation pour écrire cet article était d'aider les utilisateurs actuels et potentiels de Python à mieux comprendre comment gérer ces environnements.

Si vous avez ouvert cet article, il est probable que vous sachiez déjà ce qu'est Python, pourquoi c'est un outil formidable, et que vous avez même une version de Python installée sur votre ordinateur.

Alors **pourquoi exactement avez-vous besoin d'environnements Python** ? Vous pourriez demander : ne devrais-je pas simplement installer la dernière version de Python ?

### Pourquoi vous avez besoin de plusieurs environnements Python

Lorsque vous commencez à apprendre Python, il est bon de commencer par installer la dernière version de Python avec les dernières versions des packages dont vous avez besoin ou avec lesquels vous souhaitez jouer. Ensuite, très probablement, vous vous immergez dans ce monde et téléchargez des applications Python depuis [GitHub](https://github.com/search?l=Python&q=python&type=Repositories&utf8=%E2%9C%93), [Kaggle](https://www.kaggle.com/) ou d'autres sources. Ces applications peuvent nécessiter d'autres versions de Python/packages que celles que vous utilisez actuellement.

Dans ce cas, vous devez configurer différents environnements appelés **environnements**.

Outre cette situation, il existe d'autres cas d'utilisation où avoir des environnements supplémentaires peut s'avérer utile :

* Vous avez une **application** (développée par vous-même ou par quelqu'un d'autre) qui **fonctionnait** parfaitement. Mais maintenant, vous avez essayé de l'exécuter et elle ne fonctionne plus. Peut-être qu'un des packages n'est plus compatible avec les autres parties de votre programme (en raison des soi-disant **changements cassants**). Une solution possible est de configurer un nouvel environnement pour votre application, qui contient la version de Python et les packages qui sont entièrement compatibles avec votre application.
* Vous **collaborez avec quelqu'un d'autre**, et vous voulez vous assurer que votre application fonctionne sur l'ordinateur de votre collègue, et vice versa, vous pouvez donc également configurer un environnement pour les applications de votre collègue.
* Vous **livrez une application à votre client**, et encore une fois, vous voulez vous assurer qu'elle fonctionne sans problème sur l'ordinateur de votre client.

Un environnement se compose d'une certaine version de Python et de certains packages. Par conséquent, si vous souhaitez **développer ou utiliser des applications avec différentes versions de Python ou de packages**, vous devez configurer différents environnements.

Maintenant que nous avons discuté de l'utilité des environnements, plongeons-nous et parlons de certains des aspects les plus importants de leur gestion.

### Gestionnaires de packages et d'environnements

Les deux outils les plus populaires pour configurer des environnements sont :

* [**PIP**](https://pip.pypa.io/en/stable/) (un gestionnaire de packages Python ; ironiquement, cela signifie « Pip Installs Packages ») avec [**virtualenv**](https://virtualenv.pypa.io/en/stable/) (un outil pour créer des environnements isolés)
* **Conda** (un gestionnaire de packages et d'environnements)

Dans cet article, je couvre comment utiliser **Conda**. Je le préfère parce que :

1. **Structure claire** : Il est facile de comprendre sa structure de répertoires
2. **Gestion transparente des fichiers** : Il n'installe pas de fichiers en dehors de son répertoire
3. **Flexibilité** : Il contient de nombreux packages (les packages PIP sont également installables dans les environnements Conda)
4. **Multifonction** : Il ne sert pas seulement à gérer les environnements et les packages Python — vous pouvez également l'utiliser pour R (un langage de programmation pour le calcul statistique)

Au moment de la rédaction de cet article, j'utilise les versions 4.3.x de Conda, mais les nouvelles versions 4.4.x sont également disponibles.

_Dans le cas de Conda 4.4, il y a eu des changements récents affectant les utilisateurs de Linux/Mac OS X. Ils sont décrits dans cette [entrée du journal des modifications](https://github.com/conda/conda/blob/master/CHANGELOG.md#recommended-change-to-enable-conda-in-your-shell)._

### Comment choisir une option de téléchargement Conda appropriée

**Installer votre système Conda** est un peu plus compliqué que de télécharger une belle image depuis Unsplash ou d'acheter un nouvel ebook. Pourquoi cela ?

#### 1. Installateur

Actuellement, il existe **3 installateurs différents** :

* [Anaconda](https://www.anaconda.com/download/) (gratuit)
* [Miniconda](https://conda.io/miniconda.html) (gratuit)
* [Anaconda Enterprise platform](https://www.anaconda.com/enterprise/) (il s'agit d'un produit commercial qui permet aux organisations d'appliquer Python et R dans des environnements d'entreprise)

Examinons de plus près les outils gratuits, **Anaconda** et **Miniconda**. Maintenant, quelles sont les principales différences entre ces deux outils ?

Quelles sont les choses qu'ils ont en commun ? Ils configurent tous les deux sur votre ordinateur

* le **Conda** (le système de gestion des packages et des environnements) et
* le soi-disant **« environnement racine »** (plus d'informations à ce sujet un peu plus tard).

En ce qui concerne les principales différences, **Miniconda** nécessite environ 400 Mo d'espace disque et ne contient que quelques packages de base.

L'installateur **Anaconda** nécessite environ 3 Go d'espace disque et installe plus de 150 packages scientifiques (par exemple, des packages pour les statistiques et l'apprentissage automatique). Il configure également l'Anaconda Navigator, un outil GUI qui vous aide à gérer les environnements et les packages Conda.

**Je préfère Miniconda**, car je n'ai jamais utilisé la plupart des packages inclus par défaut dans Anaconda. Une autre raison est que l'utilisation de Miniconda permet une duplication plus fluide de l'environnement (par exemple, si je veux l'utiliser sur un autre ordinateur également), car je n'installe que les packages requis par mes applications sur les deux ordinateurs.

À partir de maintenant, je vais décrire comment fonctionne Miniconda (dans le cas de l'utilisation d'Anaconda, le processus est presque le même).

#### 2–3. Plateforme (système d'exploitation et nombre de bits)

En plus de ces 3 installateurs différents, il existe également des sous-types basés sur le nombre de bits : **32 et 64 bits**. Et bien sûr, ceux-ci ont également des sous-types pour les différents systèmes d'exploitation : **Windows, Linux et Mac OS X** (sauf que la version Mac OS X est uniquement en 64 bits).

Dans cet article, je me concentre sur la version **Windows** (les versions Linux et Mac OS X sont légèrement différentes. Par exemple, le chemin des dossiers d'installation et certaines commandes de ligne de commande diffèrent).

**Alors 32 bits ou 64 bits ?**

Si vous avez un système d'exploitation (OS) 64 bits avec 4 Go de RAM ou plus, vous devriez installer la version 64 bits. De plus, vous pourriez avoir besoin d'un installateur 64 bits si les packages que vous prévoyez d'appliquer nécessitent les versions 64 bits de Python. Par exemple, si vous souhaitez utiliser TensorFlow — plus précisément, les soi-disant binaires officiels — vous avez besoin d'un OS et d'une version de Python en 64 bits.

Si vous avez un OS 32 bits ou si vous prévoyez d'utiliser des packages qui n'ont que des versions 32 bits, la version 32 bits est la bonne option pour vous.

#### 4. Version de Python (pour l'environnement racine)

Si ces 3 dimensions ne suffisent pas (installateurs, 32/64 bits et systèmes d'exploitation), il y en a une 4ème basée sur les **différentes versions de Python** (incluses dans l'installateur — et par conséquent, dans l'environnement racine) !

Alors parlons un peu des différentes **versions de Python disponibles**.

Actuellement, vos options sont la **version 2.7** ou la **version 3.x** (au moment de la rédaction de cet article, c'est la 3.6) pour le Python qui se trouve dans l'environnement racine. Pour les environnements supplémentaires, vous pouvez choisir n'importe quelle version — finalement, c'est pourquoi vous créez des environnements en premier lieu : pour passer facilement d'un environnement à l'autre et d'une version à l'autre.

**Alors, la version 2.7 ou 3.x de Python pour mon environnement racine ?**

Laissez-moi vous aider à décider rapidement :

Puisque la **3.x est plus récente**, cela devrait être votre choix par défaut. (La version 2.7 est une version héritée, elle a été publiée en 2010, et il n'y aura pas de nouvelles versions majeures 2.7 pour celle-ci, seulement des correctifs.)

Cependant, si

* vous avez principalement du **code 2.7** (vous avez créé ou utilisez des applications utilisant les versions 2.7) ou
* vous devez utiliser des **packages qui n'ont pas de versions Python 3.x**,

vous devriez installer un environnement racine basé sur Python 2.7.

Vous pourriez demander : **pourquoi ne pas simplement créer deux environnements basés sur ces deux versions 2.7 et 3.x ?** Je suis content que vous ayez posé la question. La raison en est que votre environnement racine est celui qui est créé pendant le processus d'installation et il est **activé par défaut**.

J'expliquerai dans l'une des sections suivantes comment vous pouvez activer un environnement, mais en gros, cela signifie que l'environnement racine est celui le plus facilement accessible, donc **choisir soigneusement votre environnement racine** rendra votre flux de travail plus efficace.

Tout au long du processus d'installation, Miniconda vous permettra de modifier certaines **options définies par défaut** (par exemple, vous pouvez cocher/décocher certaines cases à cocher). Lorsque vous installez Conda pour la première fois, je vous recommande de laisser ces options intactes (sauf pour le chemin du répertoire d'installation).

![Image](https://cdn-media-1.freecodecamp.org/images/HPZ8sQsvMG0fGn008WGH1vb4avGImJOKIMi2)
_Choisir un installateur approprié pour Conda_

Je voudrais mentionner une chose de plus ici. Bien que vous puissiez avoir plusieurs environnements qui contiennent différentes versions de Python en même temps sur le même ordinateur, vous ne pouvez pas configurer des **environnements 32 et 64 bits** en utilisant le même système de gestion Conda. Il est possible de **les mélanger d'une certaine manière**, mais ce n'est pas si facile, donc je vais consacrer un article séparé à ce sujet.

### Environnements Python : racine et supplémentaires

Maintenant que vous avez choisi un installateur approprié pour vous, bien joué ! Examinons maintenant les différents types d'environnements et comment ils sont créés.

Miniconda configure deux choses pour vous : **Conda** et l'**environnement racine**.

Le processus ressemble à ceci : l'installateur installe d'abord Conda, qui est — comme je l'ai déjà mentionné — l'outil de gestion des packages et des environnements. Ensuite, Conda crée **un environnement racine qui contient deux choses** :

* une certaine version de Python et
* certains packages de base.

À côté de l'environnement racine, vous pouvez créer autant d'**environnements supplémentaires** que vous le souhaitez. Et tout l'intérêt est que ces environnements supplémentaires **peuvent contenir différentes versions de Python et d'autres packages**. Cela signifie que, par exemple, si votre petite application précieuse ne fonctionne plus dans le nouvel environnement dernier cri que vous venez de configurer, vous pouvez toujours revenir en arrière et utiliser d'autres versions de certains packages (y compris Python — Python lui-même est un package, plus d'informations à ce sujet plus tard).

Comme je l'ai déjà résumé au début de l'article, les **principaux cas d'utilisation** de l'application d'un environnement supplémentaire sont les suivants :

* Vous **développez des applications** avec différentes versions de Python ou de packages
* Vous **utilisez des applications** avec différentes versions de Python ou de packages
* Vous **collaborez** avec d'autres développeurs
* Vous créez des applications Python **pour des clients**

![Image](https://cdn-media-1.freecodecamp.org/images/z0aTVunjlzFF9lz9SaJNKna8L2z9lVVecu2q)
_Environnements racine et supplémentaires_

Avant de plonger dans les bases de la gestion des environnements, examinons la structure des répertoires de votre système Conda.

### Structure des répertoires

Comme je l'ai mentionné ci-dessus, le système Conda est installé dans un seul répertoire. Dans mon exemple, ce répertoire est : `D:\Miniconda3-64\`. Il contient l'environnement racine et deux répertoires importants (les autres répertoires sont sans importance pour l'instant) :

* `\pkgs` (il contient les packages mis en cache dans des formats compressés et non compressés)
* `\envs` (il contient les environnements — à l'exception de l'environnement racine — dans des sous-répertoires séparés)

Les **fichiers exécutables et répertoires** les plus significatifs à l'intérieur d'un environnement Conda (placés dans le répertoire `\envs\environmentname`) sont :

* `\python.exe` — l'exécutable Python pour les applications en ligne de commande. Donc, par exemple, si vous êtes dans le répertoire de l'`Example App`, vous pouvez l'exécuter par : `python.exe exampleapp.py`
* `\pythonw.exe` — l'exécutable Python pour les applications GUI, ou les applications complètement sans UI
* `\Scripts` — les exécutables qui font partie des packages installés. Lors de l'activation d'un environnement, ce répertoire est ajouté au chemin du système, de sorte que les exécutables deviennent disponibles sans leur chemin complet
* `\Scripts\activate.exe` — active l'environnement

Et si vous avez installé Jupyter, voici également un fichier important :

* `\Scripts\jupyter-notebook.exe` — lanceur de notebook Jupyter (faisant partie du package `jupyter`). En bref, Jupyter Notebook crée des documents appelés notebooks qui contiennent des parties exécutables (par exemple Python) et des parties lisibles par l'homme. Il faudrait un autre article pour entrer dans les détails.

Maintenant, vous devriez avoir au moins un environnement Python installé avec succès sur votre ordinateur. Mais comment pouvez-vous commencer à l'utiliser ? Examinons cela de plus près.

### GUI vs. Ligne de commande (Terminal)

Comme je l'ai mentionné ci-dessus, l'installateur Anaconda installe également un outil d'interface graphique (GUI) appelé Anaconda Navigator. J'ai également souligné que je préfère utiliser Miniconda, qui n'installe pas de GUI pour vous, vous devez donc utiliser des interfaces basées sur du texte (par exemple, des outils de ligne de commande ou le Terminal).

Dans cet article, je me concentre sur les **outils de ligne de commande** (Windows). Et bien que je me concentre sur la version Windows, ces exemples peuvent également être appliqués à Linux et Mac OS X, seul le chemin des dossiers d'installation et certaines commandes de ligne de commande diffèrent.

**Pour ouvrir la ligne de commande**, sélectionnez « Anaconda 32-bit » ou « Anaconda 64-bit » (selon votre installation) dans le menu Démarrer de Windows, puis choisissez « Anaconda Prompt ».

Je recommande de lire la feuille de triche officielle de [**Conda**](https://conda.io/docs/_downloads/conda-cheatsheet.pdf) (pdf), car elle contient également les différences de commandes entre Windows et Mac OS X/Linux.

Dans les sections suivantes, je vais vous donner quelques **exemples de commandes de base**, en indiquant également leurs résultats. Espérons que ceux-ci vous aideront à mieux gérer votre nouvel environnement.

### Gestion des environnements

#### Ajout d'un nouvel environnement

Pour créer un nouvel environnement nommé, par exemple `mynewenv` (vous pouvez le nommer comme vous le souhaitez), qui inclut, disons, une version Python 3.4, exécutez :

```bash
conda create --name mynewenv python=3.4
```

Vous pouvez changer la version Python d'un environnement en utilisant les commandes de gestion de packages que je décris dans la section suivante.

#### Activation et sortie (désactivation) d'un environnement

Dans une nouvelle installation Conda, l'environnement racine est activé par défaut, vous pouvez donc l'utiliser sans activation.

Dans les autres cas, si vous souhaitez utiliser un environnement (par exemple, gérer des packages ou exécuter des scripts Python à l'intérieur), vous devez d'abord l'**activer**.

Voici un **guide étape par étape** du processus d'activation :

Tout d'abord, ouvrez la ligne de commande (ou le Terminal sur Linux/Mac OS X). Pour activer l'environnement `mynewenv`, utilisez les commandes suivantes en fonction du système d'exploitation que vous avez :

* sur Windows :

```bash
activate mynewenv
```

* Sur Linux ou Mac OS X :

```bash
source activate mynewenv
```

L'**invite de commande change** lors de l'activation de l'environnement. Elle devient, par exemple, `(mynewenv) C:\>` ou `(root) D:\>`, de sorte qu'à la suite de l'activation, elle contient maintenant le nom de l'environnement actif.

Les répertoires des **fichiers exécutables** de l'environnement actif sont ajoutés au chemin du système (ce qui signifie que vous pouvez maintenant y accéder plus facilement). Vous pouvez quitter un environnement avec cette commande :

```bash
deactivate
```

Sur Linux ou Mac OS X, utilisez celle-ci :

```bash
source deactivate
```

Selon la documentation officielle de Conda, sous Windows, il est bon de désactiver un environnement avant d'en activer un autre.

Il faut mentionner que lors de la désactivation d'un environnement, l'environnement racine devient actif automatiquement.

Pour **lister les environnements disponibles** dans une installation Conda, exécutez :

```bash
conda env list 
```

Résultat d'exemple :

```bash
# conda environments:#mynewenv                 D:\Miniconda\envs\mynewenvtensorflow-cpu           D:\Miniconda\envs\tensorflow-cpuroot                  *  D:\Miniconda
```

Grâce à cette commande, vous pouvez lister tous vos environnements (le racine et tous les supplémentaires). L'environnement **actif** est marqué d'un **astérisque** (à chaque moment donné, il ne peut y avoir qu'un seul environnement actif).

#### Comment connaître la version de votre Conda ?

Il peut être utile de vérifier **quelle version de Conda vous utilisez**, ainsi que les autres paramètres de votre environnement. Je vais vous montrer ci-dessous comment lister facilement ces informations.

Pour **obtenir la version de Conda** de l'environnement actuellement actif, exécutez cette commande :

```bash
conda --version
```

Résultat d'exemple :

```bash
conda 4.3.33
```

Pour obtenir une **liste détaillée d'informations** sur l'environnement, par exemple :

* Version de Conda,
* Plateforme (système d'exploitation et nombre de bits — 32 ou 64 bits),
* Version de Python,
* Répertoires de l'environnement,

exécutez cette commande :

```bash
conda info
```

Résultat d'exemple :

```bash
Current conda install:
```

```
Current conda install:

platform : win-64
          conda version : 4.3.33
       conda is private : False
      conda-env version : 4.3.33
    conda-build version : not installed
         python version : 3.6.3.final.0
       requests version : 2.18.4
       root environment : D:\Miniconda  (writable)
    default environment : D:\Miniconda\envs\tensorflow-cpu
       envs directories : D:\Miniconda\envs
                          C:\Users\sg\AppData\Local\conda\conda\envs
                          C:\Users\sg\.conda\envs
          package cache : D:\Miniconda\pkgs
                          C:\Users\sg\AppData\Local\conda\conda\pkgs
           channel URLs : https://repo.continuum.io/pkgs/main/win-64
                          https://repo.continuum.io/pkgs/main/noarch
                          https://repo.continuum.io/pkgs/free/win-64
                          https://repo.continuum.io/pkgs/free/noarch
                          https://repo.continuum.io/pkgs/r/win-64
                          https://repo.continuum.io/pkgs/r/noarch
                          https://repo.continuum.io/pkgs/pro/win-64
                          https://repo.continuum.io/pkgs/pro/noarch
            config file : C:\Users\sg\.condarc
             netrc file : None
           offline mode : False
             user-agent : conda/4.3.33 requests/2.18.4 CPython/3.6.3 Windows/10 Windows/10.0.15063    
          administrator : False
```

Maintenant, vous connaissez quelques commandes de base pour gérer votre environnement. Examinons la gestion des packages à l'intérieur de l'environnement.

### Gestion des packages

Selon l'installateur que vous avez choisi, vous allez vous retrouver avec certains packages de base (dans le cas de l'utilisation de Miniconda) ou de nombreux packages (dans le cas de l'utilisation d'Anaconda) pour commencer. Mais que se passe-t-il si vous avez besoin

* d'un **nouveau package** ou
* d'**une autre version** d'un package déjà installé ?

Conda — votre outil de gestion des environnements et des packages — viendra à la rescousse. Examinons cela plus en détail.

#### Canaux de packages

**Les canaux sont les emplacements** des dépôts (sur l'illustration, je les appelle stockages) **où Conda recherche les packages**. Lors de l'installation de Conda, les canaux de Continuum (le développeur de Conda) sont définis par défaut, donc sans aucune modification supplémentaire, ce sont les emplacements où votre Conda commencera à rechercher les packages.

**Les canaux existent dans un ordre hiérarchique**. Le canal avec la priorité la plus élevée est le premier que Conda vérifie, à la recherche du package que vous avez demandé. Vous pouvez changer cet ordre et également ajouter des canaux à celui-ci (et définir leur priorité également).

Il est **bon de pratique d'ajouter un canal** à la liste des canaux comme **l'élément de priorité la plus faible**. De cette façon, vous pouvez inclure des packages « spéciaux » qui ne font pas partie de ceux qui sont définis par défaut (~canaux de Continuum). En conséquence, vous vous retrouverez avec tous les packages par défaut — sans le risque de les écraser par un canal de priorité inférieure — ET ce package « spécial » dont vous avez besoin.

![Image](https://cdn-media-1.freecodecamp.org/images/GZusvvaHx3GM-XtrwNg6i8uxlJbmptgUdwAD)
_C'est ainsi que fonctionnent les canaux_

Pour installer un certain package qui ne peut pas être trouvé dans ces canaux par défaut, vous pouvez rechercher ce package « spécial » sur ce [site web](https://anaconda.org/anaconda/repo). Tous les packages ne sont pas disponibles sur toutes les plateformes (=système d'exploitation et nombre de bits, par exemple Windows 64 bits), cependant, vous pouvez **affiner votre recherche** pour une plateforme spécifique. Si vous trouvez un canal qui contient le package que vous recherchez, vous pouvez l'ajouter à votre liste de canaux.

Pour **ajouter un canal** (nommé par exemple `newchannel`) avec la **priorité la plus faible**, exécutez :

```bash
conda config --append channels newchannel
```

Pour ajouter un canal (nommé `newchannel`) avec la **priorité la plus élevée**, exécutez :

```bash
conda config --prepend channels newchannel
```

Il faut mentionner qu'en pratique, vous définirez probablement des canaux avec la priorité la plus faible. Pour un débutant, ajouter un canal avec la priorité la plus élevée est un cas limite.

Pour **lister les canaux actifs et leurs priorités**, utilisez la commande suivante :

```bash
conda config --get channels
```

Résultat d'exemple :

```bash
--add channels 'conda-forge'   # lowest priority
--add channels 'rdonnelly'
--add channels 'defaults'   # highest priority
```

Il y a un autre aspect que je voudrais résumer ici. Si **plusieurs canaux contiennent un package**, et qu'un canal contient une version plus récente que l'autre, l'ordre hiérarchique des canaux détermine laquelle de ces deux versions sera installée, même si le canal de priorité supérieure contient la version la plus ancienne.

![Image](https://cdn-media-1.freecodecamp.org/images/l8CEpW7EsDPLTrfCUtcrfQc4aH55fyGq09hj)
_La version à l'intérieur du canal de priorité supérieure sera installée_

#### Recherche, installation et suppression de packages

Pour lister tous les **packages installés** dans l'environnement actuellement actif, exécutez :

```bash
conda list
```

La commande donne une liste des noms de packages correspondants, des versions et des canaux :

```bash
# packages in environment at D:\Miniconda:
#
asn1crypto                0.22.0           py36h8e79faa_1  
bleach                    1.5.0                     <pip>
ca-certificates           2017.08.26           h94faf87_0

...

wheel                     0.29.0           py36h6ce6cde_1  
win_inet_pton             1.0.1            py36he67d7fd_1  
wincertstore              0.2              py36h7fe50ca_0  
yaml                      0.1.7            vc14hb31d195_1  [vc14]
```

Pour **rechercher** toutes les **versions disponibles d'un certain package**, vous pouvez utiliser la commande `search`. Par exemple, pour lister toutes les versions du package `seaborn` (il s'agit d'un outil de visualisation de données), exécutez :

```
conda search -f seaborn
```

De manière similaire à la commande `conda list`, celle-ci donne une liste des noms de packages correspondants, des versions et des canaux :

```bash
Fetching package metadata .................
seaborn           0.7.1                    py27_0  conda-forge     
                  0.7.1                    py34_0  conda-forge     
                  0.7.1                    py35_0  conda-forge
                  
...
                  
                  0.8.1            py27hab56d54_0  defaults        
                  0.8.1            py35hc73483e_0  defaults        
                  0.8.1            py36h9b69545_0  defaults
```

Pour **installer** un package (par exemple `seaborn`) qui se trouve **dans un canal de votre liste de canaux**, exécutez cette commande (si vous ne spécifiez pas la version que vous souhaitez, il installera automatiquement la dernière version disponible depuis le canal de priorité la plus élevée) :

```bash
conda install seaborn
```

Vous pouvez également **spécifier la version du package** :

```bash
conda install seaborn=0.7.0
```

Pour installer un package (par exemple `yaml` — qui est, soit dit en passant, un analyseur et émetteur YAML) depuis un canal (par exemple un canal nommé `conda-forge`), qui se trouve **dans un canal qui n'est pas dans votre liste de canaux**, exécutez :

```bash
conda install -c conda-forge yaml
```

Pour **mettre à jour tous les packages installés** (cela n'affecte que l'environnement actif), utilisez cette commande :

```bash
conda update
```

Pour **mettre à jour un package spécifique**, par exemple le package `seaborn`, exécutez :

```bash
conda update seaborn
```

Pour **supprimer** le package `seaborn`, exécutez :

```bash
conda remove seaborn
```

Il y a un autre aspect de la gestion des packages que je voudrais couvrir dans cet article. Si vous ne voulez pas traiter les problèmes de compatibilité (changements cassants) causés par une nouvelle version de l'un des packages que vous utilisez, vous pouvez **empêcher ce package de se mettre à jour**. Comme je l'ai mentionné ci-dessus, si vous exécutez la commande `conda update`, tous vos packages installés vont être mis à jour, donc en gros, il s'agit de créer une « liste d'exceptions ». Alors, comment pouvez-vous faire cela ?

#### Empêcher les packages de se mettre à jour (épinglage)

Créez un fichier nommé `pinned` dans le répertoire `conda-meta` de l'environnement. Ajoutez la liste des packages que vous ne souhaitez pas voir mis à jour dans le fichier. Par exemple, pour forcer le package `seaborn` à la branche 0.7.x et verrouiller le package `yaml` à la version 0.1.7, ajoutez les lignes suivantes au fichier nommé `pinned` :

```bash
seaborn 0.7.*
yaml ==0.1.7
```

#### Changer la version de Python d'un environnement

Et comment pouvez-vous **changer la version de Python d'un environnement** ?

**Python est également un package**. Pourquoi est-ce pertinent pour vous ? Parce que vous allez utiliser la même commande pour remplacer la version actuellement installée de Python par une autre version que vous utilisez lorsque vous remplacez n'importe quel autre package par une autre version de ce même package.

Tout d'abord, vous devriez lister les versions disponibles de Python :

```bash
conda search -f python
```

Résultat d'exemple (la liste contient les versions et canaux disponibles) :

```bash
Fetching package metadata .................
python   2.7.12     0  conda-forge     
         2.7.12     1  conda-forge     
         2.7.12     2  conda-forge
         
...

3.6.3      h3b118a2_4  defaults        
         3.6.4      h6538335_0  defaults        
         3.6.4      h6538335_1  defaults
```

Pour **remplacer la version actuelle de Python** par, par exemple, 3.4.2, exécutez :

```bash
conda install python=3.4.2
```

Pour **mettre à jour la version de Python** vers la dernière version de sa branche (par exemple, mettre à jour la 3.4.2 vers la 3.4.5 de la branche 3.4), exécutez :

```bash
conda update python
```

#### Ajout de packages PIP

Vers le début de cet article, j'ai recommandé d'utiliser Conda comme gestionnaire de packages et d'environnements (et non PIP). Et comme je l'ai mentionné ci-dessus, **les packages PIP sont également installables dans les environnements Conda**.

Par conséquent, si un package n'est pas disponible via les canaux Conda, vous pouvez essayer de l'installer depuis l'[index des packages PyPI](https://pypi.python.org/pypi). Vous pouvez le faire en utilisant la commande `pip` (cette commande est mise à disposition par l'installateur Conda par défaut, vous pouvez donc l'appliquer dans n'importe quel environnement actif). Par exemple, si vous souhaitez installer le package `lightgbm` (il s'agit d'un framework de boosting de gradient), exécutez :

```bash
pip install lightgbm
```

### Résumé

Alors, résumons cela. Je sais que cela semble assez compliqué — et en fait, c'est compliqué. Cependant, **l'utilisation d'environnements vous évitera beaucoup de problèmes**.

Dans cet article, j'ai résumé comment vous pouvez :

* choisir un **installateur Conda** approprié pour vous
* créer des **environnements supplémentaires** (à côté de l'environnement racine)
* **ajouter ou remplacer des packages** (et j'explique également comment fonctionnent les **canaux**)
* gérer vos **versions de Python**

Il existe de nombreux autres aspects dans le domaine de la gestion des environnements Python, **alors s'il vous plaît, faites-moi savoir quels aspects vous trouvez les plus difficiles**. Faites-moi également savoir si vous avez de bonnes pratiques que je ne mentionne pas ici. Je suis curieux de connaître votre flux de travail, alors n'hésitez pas à partager dans la section des réponses ci-dessous si vous avez des **suggestions** !

### Articles recommandés

Si vous êtes intéressé par ce sujet, je vous encourage à consulter également ces articles. Merci pour ces excellentes ressources [Michael Galarnyk](https://www.freecodecamp.org/news/why-you-need-python-environments-and-how-to-manage-them-with-conda-85f155f4353c/undefined), [Dries Cronje](https://www.freecodecamp.org/news/why-you-need-python-environments-and-how-to-manage-them-with-conda-85f155f4353c/undefined), [Ryan Abernathey](https://www.freecodecamp.org/news/why-you-need-python-environments-and-how-to-manage-them-with-conda-85f155f4353c/undefined), [Sanyam Bhutani](https://www.freecodecamp.org/news/why-you-need-python-environments-and-how-to-manage-them-with-conda-85f155f4353c/undefined), [Jason Brownlee](https://www.freecodecamp.org/news/why-you-need-python-environments-and-how-to-manage-them-with-conda-85f155f4353c/undefined) et [Jake Vanderplas](https://github.com/jakevdp).

[**Gestion des environnements Python avec Conda (Python 2 + 3, Utilisation de plusieurs versions de Python)**](https://towardsdatascience.com/environment-management-with-conda-python-2-3-b9961a8a5097)  
[_Pourquoi avez-vous besoin d'environnements virtuels ? Supposons que vous avez plusieurs projets et qu'ils dépendent tous d'une bibliothèque (Pandas, Numpy…_towardsdatascience.com](https://towardsdatascience.com/environment-management-with-conda-python-2-3-b9961a8a5097)

[**Configurer votre machine Windows 10 pour le Machine Learning**](https://becominghuman.ai/how-to-setup-your-windows-10-machine-for-machine-learning-using-ubuntu-bash-shell-b32f01bd31ab)  
[_Comment configurer votre machine Windows 10 pour le Machine Learning en utilisant Ubuntu Bash shell et Conda_becominghuman.ai](https://becominghuman.ai/how-to-setup-your-windows-10-machine-for-machine-learning-using-ubuntu-bash-shell-b32f01bd31ab)

[**Environnements Conda personnalisés pour la Data Science sur les clusters HPC**](https://medium.com/@rabernat/custom-conda-environments-for-data-science-on-hpc-clusters-32d58c63aa95)  
[_Un problème auquel de nombreux scientifiques doivent faire face est comment exécuter notre code Python sur un cluster HPC (par exemple, un xsede…_medium.com](https://medium.com/@rabernat/custom-conda-environments-for-data-science-on-hpc-clusters-32d58c63aa95)

[**Tutoriels de base Partie 3**](https://medium.com/ai-saturdays/basic-tutorials-part-3-4962731e808e)  
[_Conda_medium.com](https://medium.com/ai-saturdays/basic-tutorials-part-3-4962731e808e)

[**Comment configurer un environnement Python pour le Machine Learning et le Deep Learning avec Anaconda - Machine…**](https://machinelearningmastery.com/setup-python-environment-machine-learning-deep-learning-anaconda/)  
[_Il peut être difficile d'installer un environnement Python pour le machine learning sur certaines plateformes. Python lui-même doit être installé…_machinelearningmastery.com](https://machinelearningmastery.com/setup-python-environment-machine-learning-deep-learning-anaconda/)

[**Conda : Mythes et idées fausses**](http://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions/)  
[_J'ai passé une grande partie de la dernière décennie à utiliser Python pour mes recherches, enseignant des outils Python à d'autres scientifiques et…_jakevdp.github.](http://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions/)

### Utilisation de Docker

Une petite **note de côté** basée sur une question de l'un de mes lecteurs (merci d'avoir soulevé ce point [Vikram Durai](https://www.freecodecamp.org/news/why-you-need-python-environments-and-how-to-manage-them-with-conda-85f155f4353c/undefined) !) :

Si votre application

* **utilise un serveur** (par exemple un serveur de base de données avec des données préchargées), ET
* vous souhaitez **distribuer** ce serveur et ses données avec votre application et son environnement Python à d'autres (par exemple à un autre développeur ou à un client),

vous pouvez **« conteneuriser »** l'ensemble avec **Docker**.

Dans ce cas, tous ces composants seront **encapsulés dans un conteneur Docker** :

* L'**application elle-même**,
* L'**environnement Conda** qui peut exécuter votre application (donc une version compatible de Python et des packages),
* Le **serveur ou service local** (par exemple : un serveur de base de données et un serveur web) requis pour exécuter l'application

Vous pouvez en savoir plus sur la façon dont Anaconda et Docker fonctionnent ensemble dans cet article de [Kristopher Overholt](https://www.anaconda.com/people/kristopher-overholt) :

[**Anaconda et Docker - Mieux ensemble pour la science des données reproductibles**](https://www.anaconda.com/blog/developer-blog/anaconda-and-docker-better-together-reproducible-data-science/)  
[_Anaconda s'intègre avec de nombreux fournisseurs et plateformes différents pour vous donner accès aux bibliothèques de science des données dont vous avez besoin…_www.anaconda.com](https://www.anaconda.com/blog/developer-blog/anaconda-and-docker-better-together-reproducible-data-science/)

Quelques articles supplémentaires sur les conteneurs Docker (par [Preethi Kasireddy](https://www.freecodecamp.org/news/why-you-need-python-environments-and-how-to-manage-them-with-conda-85f155f4353c/undefined) et [Alexander Ryabtsev](https://www.freecodecamp.org/news/why-you-need-python-environments-and-how-to-manage-them-with-conda-85f155f4353c/undefined)) :

[**Une introduction conviviale pour débutants aux conteneurs, aux VM et à Docker**  
_Si vous êtes programmeur ou technicien, il y a de fortes chances que vous ayez au moins entendu parler de Docker : un outil utile pour emballer, expédier…_](https://www.freecodecamp.org/news/a-beginner-friendly-introduction-to-containers-vms-and-docker-79a9e3e119b/)

[**Qu'est-ce que Docker et comment l'utiliser avec Python (Tutoriel)**](https://djangostars.com/blog/what-is-docker-and-how-to-use-it-with-python/)  
[_Il s'agit d'un tutoriel introductif sur les conteneurs Docker. À la fin de cet article, vous aurez une idée de la manière d'utiliser…_djangostars.com](https://djangostars.com/blog/what-is-docker-and-how-to-use-it-with-python/)

**Répondez ?** — s'il vous plaît, faites-moi savoir dans la section des réponses si vous avez des suggestions ou des questions !

Merci d'avoir lu ! ?

Et merci à ma femme [Krisztina Szerovay](https://www.freecodecamp.org/news/why-you-need-python-environments-and-how-to-manage-them-with-conda-85f155f4353c/undefined), qui m'a aidé à rendre cet article plus compréhensible et a créé les illustrations. Si vous êtes intéressé par le design UX (si vous êtes développeur, vous devriez l'être :) ), consultez ses croquis de base de connaissances UX ici :

[**Croquis de base de connaissances UX**](https://uxknowledgebase.com)  
[_La collection de croquis de la base de connaissances UX est destinée aux designers UX et à toute personne intéressée par le design UX ou le croquis._uxknowledgebase.com](https://uxknowledgebase.com)