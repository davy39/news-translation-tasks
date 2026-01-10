---
title: Comment optimiser votre Jupyter Notebook
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-19T07:44:05.000Z'
originalURL: https://freecodecamp.org/news/optimize-your-jupyter-notebook
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/1_m87_Htb_9Pstq0UcvNJ49w.png
tags:
- name: Data Science
  slug: data-science
- name: 'Jupyter Notebook '
  slug: jupyter-notebook
- name: Machine Learning
  slug: machine-learning
seo_title: Comment optimiser votre Jupyter Notebook
seo_desc: "By Pier Paolo Ippolito\nIntroduction\nJupyter Notebook is nowadays probably\
  \ the most used environment for solving Machine Learning/Data Science tasks in Python.\
  \ \nJupyter Notebook is a client-server application used for running notebook documents\
  \ in the..."
---

Par Pier Paolo Ippolito

## Introduction

Jupyter Notebook est probablement l'environnement le plus utilisé aujourd'hui pour résoudre des tâches de Machine Learning/Data Science en Python. 

Jupyter Notebook est une application client-serveur utilisée pour exécuter des documents notebook dans le navigateur. Les documents notebook sont des documents capables de contenir à la fois du code et des éléments de texte riche tels que des paragraphes, des équations, etc.

Dans cet article, je vais vous guider à travers quelques astuces simples pour améliorer votre expérience avec Jupyter Notebook. Nous commencerons par des raccourcis utiles et nous finirons par ajouter des thèmes, des tables des matières générées automatiquement, et plus encore.

## Raccourcis

Les raccourcis peuvent être vraiment utiles pour accélérer l'écriture de votre code. Je vais maintenant vous montrer quelques-uns des raccourcis que j'ai trouvés les plus utiles à utiliser dans Jupyter.

Il existe deux façons possibles d'interagir avec Jupyter Notebook : le Mode Commande et le Mode Édition. Certains raccourcis ne fonctionnent que dans un mode ou l'autre, tandis que d'autres sont communs aux deux modes.

Certains raccourcis qui sont communs aux deux modes sont :

* **Ctrl + Entrée** : pour exécuter toutes les cellules sélectionnées
* **Maj + Entrée** : exécuter la cellule actuelle et passer à la suivante
* **Ctrl + s** : sauvegarder le notebook

Pour entrer en mode commande Jupyter, nous devons appuyer sur Échap puis sur l'une des commandes suivantes :

* **H** : afficher tous les raccourcis disponibles dans Jupyter Notebook
* **Maj + Flèche Haut/Bas** : pour sélectionner plusieurs cellules de notebook en même temps (appuyer sur entrée après avoir sélectionné plusieurs cellules les exécutera toutes !)
* **A** : insérer une nouvelle cellule au-dessus
* **B** : insérer une nouvelle cellule en dessous
* **X** : couper les cellules sélectionnées
* **Z** : annuler la suppression d'une cellule
* **Y** : changer le type de cellule en Code
* **M** : changer le type de cellule en Markdown
* **Espace** : faire défiler le notebook vers le bas
* **Maj + Espace** : faire défiler le notebook vers le haut

Pour entrer en mode édition Jupyter, nous devons appuyer sur Entrée puis sur l'une des commandes suivantes :

* **Tab** : suggestions de complétion de code
* **Ctrl + ]** : indenter le code
* **Ctrl + [** : désindenter le code
* **Ctrl + z** : annuler
* **Ctrl + y** : rétablir
* **Ctrl + a** : tout sélectionner
* **Ctrl + Origine** : déplacer le curseur au début de la cellule
* **Ctrl + Fin** : déplacer le curseur à la fin de la cellule
* **Ctrl + Gauche** : déplacer le curseur d'un mot vers la gauche
* **Ctrl + Droite** : déplacer le curseur d'un mot vers la droite

## Commandes Shell et installation de packages

Peu d'utilisateurs sont conscients de cela, mais il est possible d'exécuter des commandes shell dans une cellule Jupyter notebook en ajoutant un point d'exclamation au début de la cellule. Par exemple, exécuter une cellule avec **!ls** retournera tous les éléments dans le répertoire de travail actuel. Exécuter une cellule avec **!pwd** imprimera le chemin du fichier du répertoire actuel.

Cette même astuce peut également être appliquée pour installer des packages Python dans Jupyter notebook.

```py
!pip install numpy
```

## Thèmes Jupyter

Si vous êtes intéressé par le changement de l'apparence de votre Jupyter notebook, il est possible d'installer un package avec une collection de différents thèmes. Le thème Jupyter par défaut ressemble à celui de la Figure 1. Dans la Figure 2, vous verrez comment nous pourrons personnaliser son aspect.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/2-2.PNG)
_Figure 1 : Thème par défaut de Jupyter Notebook_



Nous pouvons installer notre package directement dans le notebook en utilisant l'astuce que je vous ai montrée dans la section précédente :

```py
!pip install jupyterthemes
```

Nous pouvons exécuter la commande suivante pour lister les noms de tous les thèmes disponibles :

```py
!jt -l

# Sortie de la cellule :
# Thèmes disponibles : 
#   chesterish
#   grade3
#   gruvboxd
#   gruvboxl
#   monokai
#   oceans16
#   onedork
#   solarizedd
#   solarizedl
```

Enfin, nous pouvons choisir un thème en utilisant la commande suivante (dans cet exemple, j'ai décidé d'utiliser le thème solarized1) :

```py
!jt -t solarizedl
```

Une fois que nous avons exécuté cette commande et actualisé la page, notre notebook devrait ressembler à celui de la Figure 2.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/1-1.PNG)
_Figure 2 : Thème de notebook Solarized1_

Au cas où vous souhaiteriez revenir au thème original de Jupyter notebook, vous pouvez simplement exécuter la commande suivante et actualiser votre page.

```py
!jt -r
```

## Extensions Jupyter Notebook

Les extensions de notebook peuvent être utilisées pour améliorer l'expérience utilisateur et offrir une grande variété de techniques de personnalisation.

Dans cet exemple, j'utiliserai la bibliothèque _nbextensions_ afin d'installer tous les widgets nécessaires (cette fois, je vous suggère d'installer d'abord les packages via le terminal, puis d'ouvrir le Jupyter notebook). Cette bibliothèque utilise différents modèles Javascript afin d'enrichir le frontend du notebook.

```py
! pip install jupyter_contrib_nbextensions
! jupyter contrib nbextension install --system
```

Une fois que _nbextensions_ est installé, vous remarquerez qu'il y a un onglet supplémentaire sur la page d'accueil de votre Jupyter notebook (Figure 3).

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-128.png)
_Figure 3 : Ajout de nbextensions à Jupyter notebook_

En cliquant sur l'onglet Nbextensions, nous obtiendrons une liste des widgets disponibles. Dans mon cas, j'ai décidé d'activer ceux montrés dans la Figure 4.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-129.png)
_Figure 4 : Options des widgets nbextensions_

Certaines de mes extensions préférées sont :

1. **Table des matières**

Générer automatiquement une table des matières à partir des titres Markdown (Figure 5).

![Image](https://www.freecodecamp.org/news/content/images/2019/08/ezgif.com-optimize-1.gif)
_Figure 5 : Table des matières_

2. **Extraits de code**

Des codes exemples pour charger des bibliothèques courantes et créer des graphiques exemples que vous pouvez utiliser comme point de départ pour votre analyse de données (Figure 6).

![Image](https://www.freecodecamp.org/news/content/images/2019/08/snippets.gif)
_Figure 6 : Extraits de code_

3. **Hinterland**

Complétion automatique de code pour les Jupyter Notebooks (Figure 7).

![Image](https://www.freecodecamp.org/news/content/images/2019/08/completition.gif)
_Figure 7 : Complétion automatique de code_

La bibliothèque _nbextensions_ fournit de nombreuses autres extensions en plus de ces trois, donc je vous encourage à expérimenter et tester toute autre qui peut vous intéresser !

## Options Markdown

Par défaut, la dernière sortie dans une cellule Jupyter Notebook est la seule qui est imprimée. Si nous voulons plutôt imprimer automatiquement toutes les commandes sans avoir à utiliser _print()_, nous pouvons ajouter les lignes de code suivantes au début du notebook.

```py
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
```

De plus, il est possible d'écrire du LaTeX dans une cellule Markdown en enfermant le texte entre des signes dollar ($).

## Diapositives de Notebook

Il est possible de créer une présentation de diapositives d'un Jupyter Notebook en allant dans **Affichage -> Barre d'outils de cellule -> Diaporama** puis en sélectionnant la configuration des diapositives pour chaque cellule dans le notebook.

Enfin, en allant dans le terminal et en tapant les commandes suivantes, le diaporama sera créé.

```py
pip install jupyter_contrib_nbextensions

# puis successivement :

jupyter nbconvert my_notebook_name.ipynb --to slides --post serve
```

![Image](https://www.freecodecamp.org/news/content/images/2019/08/ezgif.com-optimize--1-.gif)

## Magie

Les commandes magiques sont des commandes qui peuvent être utilisées pour effectuer des commandes spécifiques. Quelques exemples sont : le traçage en ligne, l'impression du temps d'exécution d'une cellule, l'impression de la consommation mémoire de l'exécution d'une cellule, et ainsi de suite.

Les commandes magiques qui commencent par un seul _%_ appliquent leur fonctionnalité à une seule ligne d'une cellule (où la commande est placée). Les commandes magiques qui commencent par deux _%%_ sont appliquées à toute la cellule.

Il est possible d'imprimer toutes les commandes magiques disponibles en utilisant la commande suivante :

```py
%lsmagic
```

## Informations de contact

Si vous souhaitez rester informé de mes derniers articles et projets, [suivez-moi](https://medium.com/@pierpaoloippolito28?source=post_page---------------------------) et abonnez-vous à ma [liste de diffusion](http://eepurl.com/gwO-Dr?source=post_page---------------------------). Voici quelques-unes de mes coordonnées :

* [Linkedin](https://uk.linkedin.com/in/pier-paolo-ippolito-202917146?source=post_page---------------------------)
* [Blog Personnel](https://pierpaolo28.github.io/blog/?source=post_page---------------------------)
* [Site Web Personnel](https://pierpaolo28.github.io/?source=post_page---------------------------)
* [Profil Medium](https://towardsdatascience.com/@pierpaoloippolito28?source=post_page---------------------------)
* [GitHub](https://github.com/pierpaolo28?source=post_page---------------------------)
* [Kaggle](https://www.kaggle.com/pierpaolo28?source=post_page---------------------------)

Photo de couverture [de cet article](https://gdcoder.com/how-to-create-and-add-a-conda-environment-as-jupyter-kernel/).