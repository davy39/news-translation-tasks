---
title: Comment utiliser PyScript – Un Framework Frontend Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-05-26T15:37:08.000Z'
originalURL: https://freecodecamp.org/news/pyscript-python-front-end-framework
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-26-at-13.28.49.png
tags:
- name: framework
  slug: framework
- name: front end
  slug: front-end
- name: HTML
  slug: html
- name: Python
  slug: python
seo_title: Comment utiliser PyScript – Un Framework Frontend Python
seo_desc: 'By Ifihanagbara Olusheye

  Python has grown in popularity immensely in recent years. It has a wide range of
  applications, from its most popular use in Artificial Intelligence, to Data Science,
  Robotics, and Scripting.

  In the web development field, Pyth...'
---

Par Ifihanagbara Olusheye

Python a connu une croissance immense en popularité ces dernières années. Il a une large gamme d'applications, de son utilisation la plus populaire en Intelligence Artificielle, à la Science des Données, la Robotique et le Scripting.

Dans le domaine du développement web, Python est principalement utilisé en backend avec des frameworks tels que Django et Flask.

Auparavant, Python n'avait pas beaucoup de support côté frontend comme d'autres langages tels que JavaScript. Mais heureusement, les développeurs Python ont construit certaines bibliothèques (comme [Brython](https://brython.info/)) pour supporter leur langage préféré sur le web.

Et cette année, lors de la [conférence PyCon 2022](https://youtube.com/playlist?list=PL2Uw4_HvXqvYeXy8ab7iRHjA-9HiYhRQl), Anaconda a annoncé un framework nommé PyScript qui permet d'utiliser Python sur le web en utilisant du HTML standard.

Vous pouvez consulter ce tweet sur le lancement :

%[https://twitter.com/anacondainc/status/1520447158603890691?s=20&t=K-hrRhY9RwRaIkD-45acTQ]

## Prérequis

Vous aurez besoin des outils et connaissances suivants pour coder avec cet article :

* Un éditeur de texte ou un IDE de votre choix.

* Des connaissances en Python.

* Des connaissances en HTML.

* Un navigateur (Google Chrome est le navigateur recommandé pour PyScript).

## Qu'est-ce que PyScript ?

![Image du site web de PyScript.](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-22-at-18.29.40.png align="left")

*Source :* [Site officiel de PyScript](https://pyscript.net/)

PyScript est un framework frontend Python qui permet aux utilisateurs de construire des programmes Python en utilisant une interface HTML dans le navigateur.

Il a été développé en utilisant la puissance d'[Emscripten](https://emscripten.org/), [Pyodide](https://pyodide.org/en/stable/), [WASM](https://webassembly.org/), et d'autres technologies web modernes pour fournir les capacités suivantes en ligne avec ses objectifs :

* Fournir une API simpliste et propre.

* Fournir un système de composants pluggables et extensibles.

* Supporter et étendre le HTML standard pour lire des composants personnalisés fiables et opinionnés afin d'atteindre la mission « Programmer pour les 99% ».

![Une image montrant sur quoi PyScript est construit.](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-26-at-11.27.01.png align="left")

*Source :* [Blog Anaconda](https://www.anaconda.com/blog/pyscript-python-in-the-browser)

Au cours des dernières décennies, Python et les langages d'UI avancés comme le HTML, CSS et JavaScript modernes n'ont pas travaillé en collaboration. Python manquait d'un mécanisme simple pour créer des UIs attrayantes pour simplement packager et déployer des applications, tandis que le HTML, CSS et JavaScript actuels peuvent avoir une courbe d'apprentissage abrupte.

Permettre à Python d'utiliser les conventions HTML, CSS et JavaScript résout non seulement ces deux problèmes, mais aussi ceux liés au développement, au packaging, à la distribution et au déploiement d'applications web.

PyScript n'est pas destiné à prendre le rôle de JavaScript dans le navigateur, mais plutôt à donner aux développeurs Python, en particulier aux scientifiques des données, plus de flexibilité et de puissance.

## Pourquoi PyScript ?

PyScript vous offre un langage de programmation avec des conventions de style cohérentes, plus d'expressivité et de facilité d'apprentissage en fournissant ce qui suit :

* **Support dans le navigateur :** PyScript permet le support de Python et l'hébergement sans besoin de serveurs ou de configuration.

* **Interopérabilité :** Les programmes peuvent communiquer de manière bidirectionnelle entre les objets et les espaces de noms Python et JavaScript.

* **Support de l'écosystème :** PyScript permet l'utilisation de packages Python populaires tels que Pandas, NumPy, et bien d'autres.

* **Flexibilité du framework :** PyScript est un framework flexible que les développeurs peuvent utiliser pour créer des composants extensibles directement en Python facilement.

* **Gestion de l'environnement :** PyScript permet aux développeurs de définir les fichiers et les packages à inclure dans leur code de page pour l'exécuter.

* **Développement UI :** Avec PyScript, les développeurs peuvent facilement construire avec des composants UI disponibles tels que des boutons et des conteneurs, et bien d'autres.

## Comment commencer avec PyScript

PyScript est assez facile et straightforward à apprendre. Pour commencer, vous pouvez soit suivre les instructions sur le [site web](https://pyscript.net/) ou télécharger le fichier [.zip](https://github.com/pyscript/pyscript/archive/refs/heads/main.zip).

Dans cet article, nous allons utiliser et apprendre à utiliser PyScript via le [site web](https://pyscript.net/). Vous pouvez le faire en liant les composants dans votre fichier HTML. Imprimons notre premier « Hello World » avec PyScript.

### Créer un fichier HTML

Pour commencer, vous devrez créer un fichier HTML pour afficher du texte sur votre navigateur en utilisant l'éditeur de texte/IDE de votre choix.

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Titre : PyScript</title>
</head>
<body>

</body>
</html>
```

### Lier PyScript

Après avoir créé le fichier HTML, nous devrons lier PyScript dans votre fichier HTML pour avoir accès à l'interface PyScript. Cela sera placé dans la balise `<head>`.

```HTML
<link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />
<script defer src="https://pyscript.net/alpha/pyscript.js"></script>
```

### Imprimer dans le navigateur

Maintenant que vous avez lié PyScript au fichier HTML, vous pouvez imprimer votre « Hello World ».

Vous pouvez le faire avec la balise `<py-script>`. La balise `<py-script>` vous permet d'exécuter des programmes Python multi-lignes et de les imprimer sur la page du navigateur. Placez la balise entre les balises `<body>`.

```HTML
<body> <py-script> print("Hello, World!") </py-script> </body>
```

Le code complet pour le fichier HTML est ci-dessous :

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Titre : PyScript</title>
</head>
<body>
    <py-script> print("Hello, World!") </py-script>
</body>
</html>
```

Sur votre navigateur, vous devriez voir ceci :

![Image du "Hello, World" sur le navigateur.](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-23-at-18.19.48.png align="left")

**Astuce :** Si vous utilisez l'éditeur VSCode, vous pouvez utiliser l'extension Live Server dans [VSCode](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) pour recharger la page à mesure que vous mettez à jour le fichier HTML.

## Plus d'opérations avec PyScript

Il y a plus d'opérations que vous pouvez effectuer avec le framework PyScript. Regardons quelques-unes d'entre elles maintenant.

### Attacher des labels aux éléments étiquetés

Lors de l'utilisation de PyScript, vous pourriez vouloir passer des variables de votre code Python à HTML. Vous pouvez le faire avec la méthode `write` du module `pyscript` dans la balise `<pyscript>`. En utilisant l'attribut `id`, vous pouvez passer des chaînes affichées comme du texte régulier.

La méthode write accepte deux variables : la valeur `id` et la variable qui sera fournie.

```HTML
<html>
    <head>
      <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />
      <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
    </head>

  <body>
    <b><p>Aujourd'hui nous sommes le <u><label id='today'></label></u></p></b>
    <py-script>
import datetime as dt
pyscript.write('today', dt.date.today().strftime('%A %B %d, %Y'))
    </py-script>
  </body>
</html>
```

Et le résultat devient :

![Image montrant la sortie d'une date.](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-24-at-11.07.18.png align="left")

### Exécuter REPL dans le navigateur

PyScript fournit une interface pour exécuter du code Python dans les navigateurs.

Pour pouvoir le faire, PyScript utilise la balise `<py-repl>`. La balise `<py-repl>` ajoute un composant REPL à la page, qui agit comme un éditeur de code et permet d'écrire du code exécutable en ligne.

```HTML
<html>
  <head>
    <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />
    <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
  </head>
  <py-repl id="my-repl" auto-generate=true> </py-repl>
</html>
```

En l'essayant dans le navigateur (de préférence Chrome), vous devriez obtenir ceci :

![REPL de Python dans le navigateur.](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-24-at-16.14.34.png align="left")

### Importer des fichiers, modules et bibliothèques

L'une des fonctions que PyScript fournit est la flexibilité. Dans PyScript, vous pouvez importer des fichiers locaux, des modules intégrés ou des bibliothèques tierces. Ce processus utilise la balise `<py-env>`. Cette balise est utilisée pour déclarer les dépendances nécessaires.

Pour les fichiers Python locaux sur votre système, vous pouvez placer le code dans un fichier `.py` et les chemins vers les modules locaux sont fournis dans la clé paths: de la balise `<py-env>`.

Créons un fichier Python `example.py` pour contenir quelques fonctions :

```python
from random import randint

def add_two_numbers(x, y):
    return x + y

def generate_random_number():
    x = randint(0, 10)
    return x
```

Ensuite, le fichier Python sera importé dans le HTML avec la balise `<py-env>`. Vous devez placer cette balise dans la balise `<head>`, au-dessus de la balise `<body>`.

```HTML
<html>
    <head>
      <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />
      <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
      <py-env>
        - paths:
          - /example.py
      </py-env>
    </head>

  <body>
    <h1>Imprimons des nombres aléatoires</h1>
    <b>Le nombre chanceux de Doe est <label id="lucky"></label></b>
    <py-script>
      from example import generate_random_number
      pyscript.write('lucky', generate_random_number())
    </py-script>
  </body>
</html>
```

Cela retournera :

![Impression de nombres aléatoires avec Python.](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-24-at-23.20.31.png align="left")

Pour les bibliothèques tierces qui ne font pas partie de la bibliothèque standard, PyScript les supporte.

```HTML
<html>
    <head>
      <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />
      <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
      <py-env>
            - numpy
            - requests
      </py-env>
    </head>

  <body>
    <py-script>
    import numpy as np
    import requests
    </py-script>
  </body>
</html>
```

### Configurer les métadonnées

Vous pouvez définir et configurer les métadonnées générales sur votre application PyScript au format YAML en utilisant la balise `<py-config>`. Vous pouvez utiliser cette balise dans ce format :

```HTML
<py-config>
  - autoclose_loader: false
  - runtimes:
    -
      src: "https://cdn.jsdelivr.net/pyodide/v0.20.0/full/pyodide.js"
      name: pyodide-0.20
      lang: python
</py-config>
```

Ce sont les valeurs optionnelles que la balise `<py-config>` fournit. Elles incluent :

* **autoclose\_loader (booléen) :** Si cela est défini sur false, PyScript ne fermera pas l'écran de chargement.

* **name (chaîne) :** Nom de l'application utilisateur.

* **version (chaîne) :** Version de l'application utilisateur.

* **runtimes (Liste des Runtimes) :** Liste des configurations d'exécution qui auraient les champs suivants : src, name et lang.

## Conclusion

Dans cet article, vous avez appris ce qu'est PyScript et comment l'utiliser dans des fichiers HTML pour exécuter du code Python dans le navigateur. Vous avez également appris les différentes opérations/fonctionnalités que vous pouvez faire avec PyScript.

Avec PyScript, il est plus facile d'exécuter et de réaliser des opérations Python sur le web, ce qui n'était pas facile auparavant. C'est un excellent outil pour quiconque souhaite utiliser Python sur le web.

PyScript est encore dans ses premiers stades et en développement intensif. Il est toujours en phase alpha et fait face à des problèmes connus comme le temps de chargement qui peut affecter l'utilisabilité (certaines autres opérations ne peuvent pas être montrées au moment de la rédaction de cet article en raison de problèmes de performance). Vous ne devriez donc pas encore l'utiliser en production car il y aura probablement beaucoup de changements majeurs.

## Références

* [Le site officiel de PyScript](https://pyscript.net/).

* [Blog Anaconda](https://www.anaconda.com/blog/pyscript-python-in-the-browser).

* [Code source de PyScript](https://github.com/pyscript/pyscript).

* [Guide pour commencer avec PyScript](https://github.com/pyscript/pyscript/blob/main/docs/tutorials/getting-started.md).