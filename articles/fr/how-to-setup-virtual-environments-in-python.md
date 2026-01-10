---
title: Comment configurer un environnement virtuel en Python – et pourquoi c'est utile
date: '2022-04-11T20:46:19.000Z'
author: freeCodeCamp
authorURL: https://www.freecodecamp.org/news/author/stephen-sanwo/
originalURL: https://freecodecamp.org/news/how-to-setup-virtual-environments-in-python
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/virtual-env-python.png
tags:
- name: Python
  slug: python
- name: virtualenv
  slug: virtualenv
seo_desc: 'By Stephen Sanwo

  When developing software with Python, a basic approach is to install Python on your
  machine, install all your required libraries via the terminal, write all your code
  in a single .py file or notebook, and run your Python program in t...'
---


Lors du développement de logiciels avec Python, une approche de base consiste à installer Python sur votre machine, à installer toutes les bibliothèques requises via le terminal, à écrire tout votre code dans un seul fichier .py ou notebook, et à exécuter votre programme Python dans le terminal.

<!-- more -->

C'est une approche courante pour beaucoup de débutants et de nombreuses personnes venant de l'analyse de données avec Python.

Cela fonctionne parfaitement pour des projets de scripting Python simples. Mais dans des projets de développement logiciel complexes, comme la création d'une bibliothèque Python, d'une API ou d'un kit de développement logiciel (SDK), vous travaillerez souvent avec plusieurs fichiers, plusieurs packages et des dépendances. Par conséquent, vous devrez isoler votre environnement de développement Python pour ce projet particulier.

Considérez ce scénario : vous travaillez sur l'application A en utilisant le Python installé sur votre système et vous faites un `pip install packageX` version 1.0 dans votre bibliothèque Python globale. Ensuite, vous passez au projet B sur votre machine locale et vous installez le même `packageX` mais en version 2.0, qui présente des changements de rupture (*breaking changes*) entre la version 1.0 et 2.0.

Lorsque vous revenez pour exécuter votre application A, vous obtenez toutes sortes d'erreurs et votre application ne se lance pas. C'est un scénario que l'on peut rencontrer lors de la création de logiciels avec Python. Pour contourner ce problème, nous pouvons utiliser des environnements virtuels.

Ce tutoriel couvrira tout ce que vous devez savoir sur les environnements virtuels et comment en configurer un avec **Virtualenv**.

## Qu'est-ce qu'un environnement virtuel ?

La documentation officielle de Python indique :

> "Un environnement virtuel est un environnement Python tel que l'interpréteur Python, les bibliothèques et les scripts qui y sont installés sont isolés de ceux installés dans d'autres environnements virtuels, et (par défaut) de toutes les bibliothèques installées dans un Python « système », c'est-à-dire celui qui est installé dans le cadre de votre système d'exploitation"

Pour simplifier, lorsque vous activez un environnement virtuel pour votre projet, votre projet devient une application autonome, indépendante du Python installé sur le système et de ses modules.

Votre nouvel environnement virtuel possède son propre `pip` pour installer des bibliothèques, son propre dossier de bibliothèques où les nouveaux packages sont ajoutés, et son propre interpréteur Python correspondant à la version utilisée pour activer l'environnement.

Avec ce nouvel environnement, votre application devient autonome et vous bénéficiez de certains avantages tels que :

-   Votre environnement de développement est contenu dans votre projet, devient isolé et n'interfère pas avec le Python installé sur votre système ou d'autres environnements virtuels.
-   Vous pouvez créer un nouvel environnement virtuel pour plusieurs versions de Python.
-   Vous pouvez télécharger des packages dans votre projet sans privilèges d'administrateur.
-   Vous pouvez facilement packager votre application et la partager avec d'autres développeurs pour qu'ils la reproduisent.
-   Vous pouvez facilement créer une liste de dépendances et de sous-dépendances dans un fichier pour votre projet, ce qui facilite la reproduction et l'installation de toutes les dépendances utilisées dans votre environnement par d'autres développeurs.

L'utilisation d'environnements virtuels est recommandée pour les projets de développement logiciel qui dépassent généralement le cadre d'un simple script Python, et Python propose plusieurs façons de créer et d'utiliser un environnement virtuel.

Dans les sections ci-dessous, nous allons voir comment configurer votre environnement virtuel en utilisant **venv**, qui vous offre un contrôle beaucoup plus précis de votre environnement.

Une autre façon courante de configurer votre environnement virtuel est d'utiliser **pipenv**, qui est une approche de plus haut niveau.

## Comment installer un environnement virtuel avec venv

**Virtualenv** est un outil pour configurer vos environnements Python. Depuis Python 3.3, un sous-ensemble de celui-ci a été intégré à la bibliothèque standard sous le module `venv`. Vous pouvez installer `venv` sur votre Python hôte en exécutant cette commande dans votre terminal :

```bash
pip install virtualenv
```

Pour utiliser `venv` dans votre projet, créez un nouveau dossier de projet dans votre terminal, déplacez-vous (`cd`) dans ce dossier et exécutez la commande suivante :

```bash
 python<version> -m venv <virtual-environment-name>
```

Comme ceci :

```bash
 mkdir projectA
 cd projectA
 python3.8 -m venv env
```

Lorsque vous vérifiez le nouveau dossier `projectA`, vous remarquerez qu'un nouveau dossier appelé **env** a été créé. `env` est le nom de notre environnement virtuel, mais il peut être nommé comme vous le souhaitez.

Si nous examinons un peu le contenu de `env`, sur un Mac, vous verrez un dossier `bin`. Vous verrez également des scripts qui sont généralement utilisés pour contrôler votre environnement virtuel, tels que `activate` et `pip` pour installer des bibliothèques, ainsi que l'interpréteur Python pour la version que vous avez installée, et ainsi de suite. (Ce dossier s'appellera `Scripts` sur Windows).

Le dossier `lib` contiendra la liste des bibliothèques que vous avez installées. Si vous y jetez un coup d'œil, vous verrez la liste des bibliothèques fournies par défaut avec l'environnement virtuel.

## Comment activer l'environnement virtuel

Maintenant que vous avez créé l'environnement virtuel, vous devrez l'activer avant de pouvoir l'utiliser dans votre projet. Sur un Mac, pour activer votre environnement virtuel, exécutez le code ci-dessous :

```bash
source env/bin/activate
```

Cela activera votre environnement virtuel. Immédiatement, vous remarquerez que le chemin de votre terminal inclut `env`, signifiant qu'un environnement virtuel est activé.

Notez que pour activer votre environnement virtuel sur Windows, vous devrez exécuter le code ci-dessous (consultez ce [lien][1] pour bien comprendre les différences entre les plateformes) :

```bash
 env/Scripts/activate.bat //Dans CMD
 env/Scripts/Activate.ps1 //Dans Powershell
```

## L'environnement virtuel fonctionne-t-il ?

Nous avons activé notre environnement virtuel, maintenant comment confirmer que notre projet est bien isolé de notre Python hôte ? Nous pouvons faire plusieurs choses.

Tout d'abord, nous vérifions la liste des packages installés dans notre environnement virtuel en exécutant le code ci-dessous dans l'environnement virtuel activé. Vous ne remarquerez que deux packages – `pip` et `setuptools`, qui sont les packages de base fournis par défaut avec un nouvel environnement virtuel.

```bash
pip list
```

Ensuite, vous pouvez exécuter le même code ci-dessus dans un nouveau terminal dans lequel vous n'avez pas activé l'environnement virtuel. Vous remarquerez beaucoup plus de bibliothèques dans votre Python hôte que vous avez pu installer par le passé. Ces bibliothèques ne font pas partie de votre environnement virtuel Python tant que vous ne les y installez pas.

## Comment installer des bibliothèques dans un environnement virtuel

Pour installer de nouvelles bibliothèques, il vous suffit d'utiliser `pip install`. L'environnement virtuel utilisera son propre `pip`, vous n'avez donc pas besoin d'utiliser `pip3`.

Après avoir installé les bibliothèques requises, vous pouvez visualiser toutes les bibliothèques installées en utilisant `pip list`, ou vous pouvez générer un fichier texte listant toutes les dépendances de votre projet en exécutant le code ci-dessous :

```bash
pip freeze > requirements.txt
```

Vous pouvez nommer ce fichier `requirements.txt` comme vous le souhaitez.

## Le fichier requirements

Pourquoi un fichier `requirements` est-il important pour votre projet ? Imaginez que vous compressiez votre projet dans un fichier zip (**sans le dossier env**) et que vous le partagiez avec un ami développeur.

Pour recréer votre environnement de développement, votre ami n'aura qu'à suivre les étapes ci-dessus pour activer un nouvel environnement virtuel.

Au lieu de devoir installer chaque dépendance une par une, il pourra simplement exécuter le code ci-dessous pour installer toutes vos dépendances dans sa propre copie du projet :

```bash
 ~ pip install -r requirements.txt
```

Notez qu'il n'est généralement pas conseillé de partager votre dossier `env`, car il doit pouvoir être facilement reproduit dans n'importe quel nouvel environnement.

Typiquement, votre répertoire `env` sera inclus dans un fichier `.gitignore` (lors de l'utilisation de plateformes de contrôle de version comme GitHub) pour s'assurer que le fichier d'environnement n'est pas poussé vers le dépôt du projet.

## Comment désactiver un environnement virtuel

Pour désactiver votre environnement virtuel, exécutez simplement le code suivant dans le terminal :

```bash
 ~ deactivate
```

## Conclusion

Les environnements virtuels Python vous donnent la possibilité d'isoler vos projets de développement Python du Python installé sur votre système et des autres environnements Python. Cela vous donne un contrôle total sur votre projet et le rend facilement reproductible.

Lors du développement d'applications qui dépassent généralement le cadre d'un simple script .py ou d'un notebook Jupyter, c'est une bonne idée d'utiliser un environnement virtuel – et vous savez maintenant comment en configurer un et commencer à l'utiliser.

[1]: https://docs.python.org/3/library/venv.html