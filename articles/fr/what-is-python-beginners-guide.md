---
title: Qu'est-ce que Python ? Comment fonctionne l'interpréteur et comment écrire
  "Hello World" en Python
subtitle: ''
author: Michael Para
co_authors: []
series: null
date: '2022-10-17T13:38:18.000Z'
originalURL: https://freecodecamp.org/news/what-is-python-beginners-guide
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/python-img.jpg
tags:
- name: beginner
  slug: beginner
- name: Python
  slug: python
seo_title: Qu'est-ce que Python ? Comment fonctionne l'interpréteur et comment écrire
  "Hello World" en Python
seo_desc: 'In this article, I am going to explain what Python is and how the Python
  interpreter works. Then you''ll write your first "Hello World" program.

  What is Python?

  Python is a high-level programming language designed to do many tasks. It''s based
  on the C...'
---

Dans cet article, je vais expliquer ce qu'est Python et comment fonctionne l'interpréteur Python. Ensuite, vous écrirez votre premier programme "Hello World".

## Qu'est-ce que Python ?

Python est un langage de programmation de haut niveau conçu pour effectuer de nombreuses tâches. Il est basé sur l'interpréteur CPython qui traduit le code Python en quelque chose que la machine peut lire.

Python nous donne la capacité d'utiliser de nombreux modules et packages avec notre code, qui sont des bibliothèques standard intégrées avec l'interpréteur.

Vous pouvez utiliser Python pour effectuer de nombreuses tâches telles que :

* Apprentissage automatique

* Intelligence artificielle

* Visualisation de données

* Applications de programmation

* Applications Web

* Développement de langages et de jeux

* Analyse de données

et plus encore.

De plus, la syntaxe de Python est assez simple et facile à apprendre – souvent, il semble que vous écrivez simplement un message à quelqu'un d'autre. Assurez-vous simplement de connaître les règles d'indentation :).

Nous pouvons comparer Python avec d'autres langages de programmation interprétés tels que Java, JavaScript, PHP, et autres. Mais vous vous demandez peut-être – qu'est-ce que CPython ?

Dans la section suivante, je vais me concentrer sur l'histoire de l'interpréteur Python en profondeur, puis je répondrai à cette question.

## Aperçu de l'histoire de Python

La première apparition du langage de programmation Python remonte à la fin des années 1980. Il a été créé par Guido van Rossum.

Python a été conçu pour remplacer le langage de programmation ABC qui fonctionnait avec le système d'exploitation Amoeba.

Rossum a commencé l'implémentation en 1989 et il a travaillé seul sur Python jusqu'en 2018.

Il l'a nommé Python parce que la première version était capable de lire le script comique de la BBC "Monty Python's Flying Circus".

La première version est sortie en 1994 sous la version 1.0 (Python 1.0) et la deuxième version est sortie en 2000, nommée version 2.0.

Dans la version 2.0, van Rossum a ajouté des fonctionnalités mineures telles que les systèmes de collection et les comprehensions.

La troisième version est sortie en 2008 et a corrigé un défaut de base du langage. Ils ont nommé cette version "Py3K", ou Python 3.0.

## Comment fonctionne l'interpréteur Python ?

L'interpréteur Python s'appelle "CPython" et il est écrit en langage de programmation C. C'est l'implémentation par défaut pour Python.

Dans les sections suivantes, vous comprendrez comment l'interpréteur Python fonctionne en coulisses.

### Analyse du code source

En fait, tout traducteur commence par l'analyse du code source. Ici, l'interpréteur Python reçoit le code source et initialise certaines instructions pour faire les choses suivantes :

Il suit la règle d'indentation et vérifie la syntaxe Python. Peut-être qu'il y a des lignes incorrectes, donc il arrêtera le programme de l'exécution pour afficher le message d'erreur.

Cette phase est appelée [analyse lexicale](https://codedtag.com/php/what-is-php-how-to-write-php-program/#the-lexical-analysis), ce qui signifie diviser les fichiers de code source en une liste de jetons.

À l'étape suivante, l'interpréteur générera des codes d'octets. Voyons comment cela fonctionne.

### Génération de bytecode

Une fois que l'analyseur de l'interpréteur Python reçoit les jetons, il commence à manipuler les jetons lexicaux. Il génère une grande structure appelée AST (Abstract Syntax Tree).

L'interpréteur convertit cet AST en bytecode, ce qui signifie le langage machine. En Python, le bytecode peut être enregistré dans un fichier se terminant par l'extension ".pyc".

Dans la section suivante, vous verrez comment l'interpréteur Python exécute ces codes d'octets.

### La machine virtuelle Python (PVM)

L'interpréteur Python initialise son moteur d'exécution appelé PVM qui est la machine virtuelle Python.

L'interpréteur charge le langage machine avec les modules de bibliothèque et l'entre dans le PVM. Cela convertit le bytecode en code exécutable tel que des 0 et des 1 (binaire).

Et ensuite, il imprime les résultats.

Notez que si une erreur se produit pendant le processus PVM, l'exécuteur mettra fin à l'opération immédiatement pour afficher l'erreur.

Maintenant, vous allez apprendre comment installer Python sur votre système d'exploitation.

Si vous n'avez pas de logiciel Python ou si vous utilisez un appareil mobile, vous pouvez utiliser n'importe quel [compilateur Python en ligne](https://codedtag.com/python/free-online-python-compiler-interpreter/).

## Comment installer Python

Pour installer Python sur votre système d'exploitation Ubuntu Linux, suivez ces instructions :

Ouvrez votre terminal et exécutez la commande suivante pour mettre à jour le dépôt du système local d'Ubuntu :

```xml
sudo apt update
```

Installez la dernière version de Python en utilisant la commande suivante :

```xml
sudo apt install python3
```

Si vous utilisez Windows OS, vous devez suivre ces étapes pour installer Python sur votre machine.

1. Accédez à la [page officielle de Python](https://www.python.org/downloads/windows/) et téléchargez le dernier installateur.

2. Une fois que vous avez choisi la dernière version via le lien ci-dessus, vous devez sélectionner le système de bits selon votre système d'exploitation Windows.

3. Exécutez l'installateur et suivez les instructions écrites sur l'installateur.

Une fois que vous avez installé le programme, vous devez vérifier la version actuelle de Python sur votre système d'exploitation en utilisant la commande suivante via le terminal ou CMD selon votre système d'exploitation.

Tapez simplement `python` et appuyez sur Entrée – il vous montrera le résultat comme dans l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-67.png align="left")

*Vérification de la version de Python via CMD*

Dans la section suivante, vous apprendrez comment écrire votre premier programme avec Python.

## Comment écrire votre premier programme Python

Dans ce programme, vous allez imprimer le message classique "Hello World" en utilisant le langage de programmation Python.

Tout d'abord, créez un dossier et nommez-le "CodedTag", puis créez un fichier à l'intérieur et nommez-le "page.py".

Ensuite, copiez et collez le code Python suivant :

```python
# sortie: Hello World
print("Hello World")
```

Ensuite, ouvrez le terminal et naviguez jusqu'au répertoire du projet et exécutez la commande suivante :

```xml
python page.py
```

La sortie sera comme l'image suivante :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-68.png align="left")

*Exécuter le message Python*

Félicitations – vous venez d'écrire votre premier programme Python.

## Conclusion

Dans cet article, vous avez appris ce qu'est Python et un peu de son histoire. Vous avez également appris comment fonctionne l'interpréteur Python.

Résumons cela en quelques points :

1. L'interpréteur vérifie et recherche les erreurs de syntaxe et vérifie les règles d'indentation. Ensuite, il convertit le code source via la tokenisation.

2. L'analyseur reçoit les jetons lexicaux et génère un arbre syntaxique abstrait.

3. L'interpréteur convertit l'AST en bytecode et initialise la machine virtuelle Python pour exécuter le bytecode et renvoyer le résultat final.

Merci d'avoir lu, si vous souhaitez lire plus de mes articles, vous pouvez les trouver sur [FlatCoding](https://flatcoding.com/). Restez à l'écoute pour mes prochains articles.