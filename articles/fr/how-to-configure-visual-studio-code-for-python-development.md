---
title: Comment configurer Visual Studio Code pour le développement Python
subtitle: ''
author: Farhan Hasin Chowdhury
co_authors: []
series: null
date: '2023-07-17T17:13:01.000Z'
originalURL: https://freecodecamp.org/news/how-to-configure-visual-studio-code-for-python-development
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/visual-studio-code-for-python.png
tags:
- name: Python
  slug: python
- name: Visual Studio Code
  slug: visual-studio-code
- name: Visual Studio Code
  slug: vscode
seo_title: Comment configurer Visual Studio Code pour le développement Python
seo_desc: 'Visual Studio Code is one of the most versatile code editors out there.
  Even though it''s a code editor, the sheer extensibility of the program makes it
  almost as capable as some of the JetBrains products out there.

  In this article, I''ll walk you thro...'
---

Visual Studio Code est l'un des éditeurs de code les plus polyvalents disponibles. Bien qu'il s'agisse d'un éditeur de code, l'extensibilité du programme le rend presque aussi performant que certains produits JetBrains.

Dans cet article, je vais vous guider à travers le processus complet de configuration de Visual Studio Code pour le développement Python. Ce n'est pas une configuration universelle, mais c'est quelque chose que j'utilise personnellement et que j'ai trouvé très confortable.

La première étape consiste à installer Visual Studio Code sur votre ordinateur. Je suis actuellement sur Debian 12 et j'ai l'éditeur prêt à l'emploi. Des instructions d'installation spécifiques à la plateforme sont disponibles dans la [documentation](https://code.visualstudio.com/docs/setup/setup-overview).

En supposant que vous avez passé l'étape d'installation, je vais maintenant vous présenter un ensemble d'extensions essentielles qui amélioreront votre expérience de développement Python.

## Extension Python

La première extension que vous devez installer est l'[Extension Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) de Microsoft.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-86.png)
_https://marketplace.visualstudio.com/items?itemName=ms-python.python_

Il s'agit en fait d'un pack d'extensions contenant deux extensions. La première extension est l'extension Python. Elle pose les bases du développement Python dans Visual Studio Code.

L'autre est [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance), qui est un serveur de langage très performant pour Python.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-88.png)
_https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance_

Cette extension fournit un riche support d'intellisense et est alimentée par [Pyright](https://github.com/microsoft/pyright), le vérificateur de types statiques de Microsoft. La prochaine chose à laquelle vous devez penser est le linting.

## Ruff Linter

Un linter est un programme qui analyse votre code statiquement et fournit des informations précieuses sur les erreurs possibles.

L'extension Pylance fait un excellent travail pour détecter les erreurs fatales dans votre code, mais il y a plus à faire.

Lorsqu'on travaille sur un grand projet, il est assez courant de laisser des désordres indésirables dans votre base de code. Des choses comme des imports et des variables inutilisés, de mauvaises pratiques de codage, etc.

Un bon linter peut pointer des odeurs de code comme celles-ci et rendre votre code plus propre. Maintenant, le choix de prédilection en matière de linters Python est Pylint.

Pylint existe depuis des années et fonctionne assez bien, mais je pense qu'il existe une meilleure alternative.

Ruff est un linter Python extrêmement rapide écrit en Rust qui impose des règles de linting plus strictes que Pylint. L'outil dispose également d'une [extension officielle](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff).

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-89.png)
_https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff_

Il s'agit d'une extension plug and play qui ne nécessite aucune configuration supplémentaire. Une fois installée, vous êtes prêt à l'utiliser.

## Isort

Comme un linter, [isort](https://marketplace.visualstudio.com/items?itemName=ms-python.isort) est un autre utilitaire dont le seul but est de trier les instructions d'importation.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-95.png)
_https://marketplace.visualstudio.com/items?itemName=ms-python.isort_

L'utilitaire trie toutes les imports par ordre alphabétique, tout en les divisant en sections.

L'extension est très simple. Une fois que vous avez l'extension, elle rendra des lignes ondulées sous toute instruction d'importation qui semble hors de place.

Vous pouvez ensuite utiliser le menu d'action rapide pour les trier. Ou, vous pouvez également utiliser la palette de commandes pour accéder rapidement à la commande isort.

## Vérificateur de types Mypy

Avant de commencer à parler de cette extension, laissez-moi expliquer ce qu'est [mypy](https://mypy-lang.org/).

Selon les informations sur leur page d'accueil :

> Mypy est un vérificateur de types statiques optionnel pour Python qui vise à combiner les avantages du typage dynamique (ou "duck") et du typage statique. Mypy combine la puissance expressive et la commodité de Python avec un système de types puissant et une vérification des types au moment de la compilation.

En termes plus simples, mypy vous oblige à ajouter des annotations de type essentielles à vos programmes Python, les rendant ainsi plus faciles à comprendre.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-90.png)
_https://mypy-lang.org/_

Récemment, Microsoft a publié [une extension](https://marketplace.visualstudio.com/items?itemName=ms-python.mypy-type-checker) qui ajoute une fonctionnalité de vérification de type utilisant mypy à leur éditeur préféré.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-91.png)
_https://marketplace.visualstudio.com/items?itemName=ms-python.mypy-type-checker_

Une fois que vous avez installé l'extension, elle effectuera les vérifications nécessaires sur votre code et signalera toute annotation de type manquante comme des erreurs de compilation.

Bien que les annotations de type ne soient pas obligatoires, elles sont fortement recommandées.

## IntelliCode

[IntelliCode](https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode) fournit une complétion de code assistée par IA dans Visual Studio Code. Cela peut sembler similaire à GitHub Copilot, mais en réalité, c'est beaucoup plus petit que cela.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-93.png)
_https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode_

Alors que GitHub Copilot ou Tabnine fournit des blocs de code complets, IntelliCode complète les lignes de code de manière assez fluide.

Dans la plupart des cas, cette extension peut vous aider à taper moins de code en suggérant la bonne chose tout en restant discret.

## Error Lens

Bien que non spécifique à Python, [Error Lens](https://marketplace.visualstudio.com/items?itemName=usernamehw.errorlens) est une excellente extension qui intègre les erreurs directement à côté de la ligne de code.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-94.png)

Je travaille souvent sur mon Thinkpad de 14 pouces et j'aime désactiver le panneau du terminal. Error Lens élimine le besoin de regarder le terminal de temps en temps pour voir mes erreurs et avertissements.

Aussi utile que cela puisse être, parfois votre éditeur peut sembler encombré en raison de toutes les sorties d'avertissement et d'erreur, alors décidez en conséquence.

## Indent Rainbow

Contrairement à d'autres langages de programmation, un niveau d'indentation incorrect peut littéralement casser votre programme en Python.

Visual Studio Code fait déjà un bon travail de visualisation des niveaux d'indentation dans votre code, mais si vous voulez ajouter un peu de couleur, le package [indent-rainbow](https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow) est ce dont vous avez besoin.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-92.png)
_https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow_

Il ajoute différentes couleurs aux différents niveaux d'indentation. Personnellement, je ne l'utilise pas régulièrement, mais vous pourriez le trouver utile.

## Conclusion

Comme je l'ai dit, ces extensions et ma configuration personnelle ne sont pas une solution miracle. Mais cette configuration est quelque chose que j'utilise depuis un certain temps et j'espère qu'elle vous sera également utile.

J'installe souvent des extensions spécialisées en fonction des projets sur lesquels je travaille. Par exemple, j'utilise l'extension [Django](https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django) ou [Jinja](https://marketplace.visualstudio.com/items?itemName=wholroyd.jinja) lorsque je travaille sur un projet Django ou Flask.

Ou j'installe l'extension [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) lorsque je travaille sur un Jupyter Notebook. N'hésitez donc pas à installer ce dont vous avez besoin, mais ne faites pas trop.