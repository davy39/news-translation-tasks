---
title: Vérifier la version de Python – Comment vérifier Py sur Mac, Windows et Linux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-07-07T22:31:51.000Z'
originalURL: https://freecodecamp.org/news/check-python-version-how-to-check-py-in-mac-windows-and-linux
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/Shittu-Olumide-Check-Python-Version
seo_title: Vérifier la version de Python – Comment vérifier Py sur Mac, Windows et
  Linux
---

How-to-Check-Py-in-Mac--Windows--and-Linux.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "Par Shittu Olumide\nPython est un langage de programmation polyvalent et largement utilisé\n  \ connu pour sa simplicité et sa lisibilité. \nAvec sa nature en constante évolution, différentes\n  \ versions de Python sont souvent publiées, chacune offrant de nouvelles fonctionnalités, des améliorations,\
  \ et des corrections de bugs ..."
---

Par Shittu Olumide

Python est un langage de programmation polyvalent et largement utilisé, connu pour sa simplicité et sa lisibilité. 

Avec sa nature en constante évolution, différentes versions de Python sont souvent publiées, chacune offrant de nouvelles fonctionnalités, des améliorations et des corrections de bugs. 

En tant que développeur Python, il est crucial de connaître la version de Python que vous utilisez, car cela détermine la compatibilité des bibliothèques, de la syntaxe et des fonctionnalités.

Dans cet article, nous allons explorer diverses méthodes pour vérifier la version de Python installée sur votre système. Que vous soyez un débutant commençant votre parcours Python ou un développeur expérimenté travaillant sur un projet, connaître votre version de Python est la première étape pour garantir une exécution fluide et une compatibilité.

Nous allons plonger dans les approches en ligne de commande pour déterminer la version de Python. À la fin de cet article, vous serez équipé des connaissances pour vérifier facilement votre version de Python et prendre des décisions éclairées concernant les outils et les bibliothèques que vous pouvez utiliser.

## Comment vérifier la version de Python sur Mac

Pour vérifier la version de Python sur un Mac, vous pouvez suivre ces étapes :

### Ouvrez l'application Terminal sur votre Mac :

Vous pouvez trouver le terminal en naviguant vers "**Applications**" -> "**Utilitaires**" -> "**Terminal**", ou en utilisant la recherche Spotlight (Cmd + Espace) et en tapant "**Terminal**".

Une fois le Terminal ouvert, vous verrez un prompt de commande où vous pouvez entrer des commandes. Tapez la commande suivante et appuyez sur Entrée :

```bash
python --version
```

Cette commande affichera la version de Python installée sur votre Mac. Par exemple, si vous avez Python 3.9.2 installé, elle affichera quelque chose comme :

```bash
Python 3.9.2
```

Le numéro de version variera en fonction de l'installation spécifique de Python sur votre système.

### Méthodes alternatives pour Mac

Si la commande `python --version` ne fonctionne pas, essayez d'utiliser la commande `python3` à la place. Python 3 est la dernière version majeure de Python, et certains systèmes ont à la fois Python 2 et Python 3 installés. 

Pour vérifier la version de Python 3, entrez la commande suivante et appuyez sur Entrée :

```bash
python3 --version
```

Cette commande affichera la version de Python 3 installée sur votre Mac.

Une autre façon de vérifier la version de Python consiste à utiliser le module `sys` dans l'interpréteur Python. Dans le Terminal, tapez la commande suivante et appuyez sur Entrée pour démarrer l'interpréteur Python :

```bash
python
```

Cela lancera l'interpréteur Python, et vous verrez un nouveau prompt (`>>>`) indiquant que vous pouvez entrer des commandes Python.

Dans l'interpréteur Python, tapez la commande suivante et appuyez sur Entrée :

```bash
import sys
print(sys.version)
```

Cela imprimera les informations détaillées sur la version de Python, y compris le numéro de version et des détails supplémentaires tels que le numéro de build et la date de l'installation de Python.

Après avoir vérifié la version de Python, vous pouvez quitter l'interpréteur Python en tapant `exit()` et en appuyant sur Entrée, ou en appuyant sur Ctrl + Z suivi de Entrée.

En suivant ces étapes, vous pourrez vérifier la version de Python installée sur votre Mac en utilisant l'application Terminal.

## Comment vérifier la version de Python sous Windows

Pour vérifier la version de Python sur un système d'exploitation Windows, vous pouvez suivre ces étapes détaillées :

### Ouvrir l'invite de commandes :

* Appuyez sur la touche Windows de votre clavier.
* Tapez "**cmd**" (sans les guillemets) dans la barre de recherche.
* Cliquez sur l'application "**Invite de commandes**" dans les résultats de recherche. Cela ouvrira la fenêtre de l'invite de commandes.

### Vérifier si Python est installé :

Dans la fenêtre de l'invite de commandes, tapez la commande suivante et appuyez sur Entrée :

```bash
python --version
```

Si Python est installé sur votre système, il affichera le numéro de version. Par exemple, "**Python 3.9.2**".

Si Python n'est pas installé, vous verrez un message d'erreur indiquant que la commande n'est pas reconnue. Dans ce cas, vous devez installer Python avant de continuer.

### Vérifier l'emplacement de l'installation de Python (facultatif) :

Dans l'invite de commandes, tapez la commande suivante et appuyez sur Entrée :

```bash
where python
```

Cette commande affichera le chemin du fichier exécutable de Python. Par défaut, Python est installé dans le répertoire "**C:\PythonXX**", où "**XX**" représente le numéro de version.

Si la commande ne retourne aucun résultat, cela signifie que Python n'est pas installé ou n'est pas ajouté à la variable d'environnement PATH du système.

### Vérifier la version de Python en utilisant l'interpréteur Python :

Dans l'invite de commandes, tapez la commande suivante et appuyez sur Entrée :

```bash
python
```

Cela lancera l'interpréteur Python, affichant les informations sur la version de Python en haut. Par exemple, "**Python 3.9.2 (tags/v3.9.2:1a79785, Feb 22 2021, 12:26:58)**".

Pour quitter l'interpréteur Python, vous pouvez taper `exit()` et appuyer sur Entrée.

#### Vérifier la version de Python en utilisant IDLE (facultatif) :

IDLE est un environnement de développement intégré qui est fourni avec Python.

Dans l'invite de commandes, tapez la commande suivante et appuyez sur Entrée :

```bash
idle
```

Cela lancera l'IDLE Python Shell, qui affichera les informations sur la version de Python en haut. Par exemple, "**Python 3.9.2 (tags/v3.9.2:1a79785, Feb 22 2021, 12:26:58)**".

Pour quitter l'IDLE Python Shell, vous pouvez aller dans le menu "**Fichier**" et choisir "**Quitter**" ou simplement fermer la fenêtre.

En suivant ces étapes, vous pouvez facilement vérifier la version de Python installée sur votre système Windows en utilisant l'invite de commandes ou l'interpréteur Python.

## Comment vérifier la version de Python sous Linux

### Ouvrir un terminal :

Lancez l'application terminal sur votre système Linux. Vous pouvez généralement la trouver dans le menu des applications ou en utilisant un raccourci clavier tel que Ctrl+Alt+T.

Dans le terminal, tapez la commande suivante et appuyez sur Entrée :

```bash
python --version
```

Cette commande affichera la version de Python installée sur votre système.

> **Note** : Certaines distributions Linux, comme Ubuntu, peuvent avoir à la fois Python 2 et Python 3 installés. Dans ce cas, la commande ci-dessus peut afficher la version de Python 2. Pour vérifier la version de Python 3, vous pouvez utiliser la commande suivante :

```bash
python3 --version
```

### Vérifier la sortie :

Après avoir exécuté la commande, le terminal affichera la version de Python installée sur votre système. Elle sera généralement au format "Python x.y.z", où x, y et z représentent respectivement les versions majeure, mineure et micro.

Par exemple, la sortie pourrait être :

```bash
Python  3.9.2


Cela signifie que la version Python 3.9.2 est installée sur votre système Linux.

### Vérifier l'installation :

Pour vérifier que la version de Python affichée est correcte, vous pouvez également entrer dans l'interpréteur Python interactif en tapant la commande suivante et en appuyant sur Entrée :

```bash
python
```

Cela ouvrira l'interpréteur Python, où vous pourrez exécuter des commandes Python de manière interactive.

### Vérifier la version depuis l'interpréteur Python :

Dans l'interpréteur Python, vous pouvez confirmer la version en tapant la commande suivante et en appuyant sur Entrée :

```python
import sys
print(sys.version)
```

La sortie affichera des informations détaillées sur la version de Python, y compris le numéro de version, les informations de build et des détails supplémentaires.

### Quitter l'interpréteur Python

Pour quitter l'interpréteur Python, vous pouvez taper `exit()` ou appuyer sur Ctrl+D.

En suivant ces étapes, vous pouvez facilement vérifier la version de Python installée sur votre système Linux. 

## Conclusion 

En suivant les instructions fournies dans cet article, vous pouvez facilement vérifier votre version de Python, que vous utilisiez Mac, Windows ou Linux. Cela vous aidera à écrire vos programmes Python en toute confiance. 

N'oubliez pas de consulter la documentation pertinente ou les ressources communautaires si vous rencontrez des problèmes ou si vous utilisez des distributions Python non standard ou des environnements virtuels.

Alors que Python continue d'évoluer, rester à jour avec la version installée de Python devient de plus en plus important. Cette connaissance vous permet de tirer parti des nouvelles fonctionnalités et améliorations introduites dans les nouvelles versions de Python tout en assurant la compatibilité avec les bases de code existantes.

Restons en contact sur [Twitter](https://www.twitter.com/Shittu_Olumide_) et sur [LinkedIn](https://www.linkedin.com/in/olumide-shittu). Vous pouvez également vous abonner à ma chaîne [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A).

Bon codage !