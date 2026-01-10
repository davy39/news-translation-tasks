---
title: Python End Program – Comment quitter un programme Python dans le terminal
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-05-16T16:48:59.000Z'
originalURL: https://freecodecamp.org/news/python-end-program-how-to-exit-a-python-program-in-terminal
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/jake-walker-MPKQiDpMyqU-unsplash.jpg
tags:
- name: Python
  slug: python
- name: terminal
  slug: terminal
seo_title: Python End Program – Comment quitter un programme Python dans le terminal
seo_desc: "You can execute Python code in a terminal just like you would in an IDE\
  \ like VS Code, Atom, and so on. You can do this in both Windows and Unix operating\
  \ systems like Linux and macOS. \nIn this article, you'll learn how to exit a Python\
  \ program in the..."
---

Vous pouvez exécuter du code Python dans un terminal tout comme vous le feriez dans un IDE comme VS Code, Atom, et ainsi de suite. Vous pouvez le faire à la fois sur Windows et sur des systèmes d'exploitation Unix comme Linux et macOS.

Dans cet article, vous apprendrez comment quitter un programme Python dans le terminal en utilisant les méthodes suivantes :

* Les fonctions `exit()` et `quit()` dans Windows et macOS (et autres systèmes basés sur Unix – nous utiliserons macOS pour les représenter). 
* La commande `Ctrl + Z` dans Windows. 
* La commande `Ctrl + D` dans macOS. 

## Comment exécuter un programme Python dans le terminal

Pour exécuter Python dans le terminal, vous devez ouvrir votre terminal et exécuter la commande `python`.

Notez que la commande `Python` ne fonctionnera dans votre terminal que si vous avez Python installé sur votre ordinateur.

Après avoir exécuté la commande, vous devriez avoir quelque chose comme ceci dans le terminal :

```bash
C:\Users\USER>python
Python 3.10.8 (main, Nov  6 2022, 23:27:16)  [GCC 12.2.0 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
```

![Image](https://www.freecodecamp.org/news/content/images/2023/05/py-in-terminal.PNG)
_Commande Python dans le terminal_

J'utilise l'invite de commande pour Windows, mais cela devrait fonctionner de la même manière si vous utilisez macOS ou Linux.

Maintenant, vous pouvez exécuter du code Python dans le terminal :

```bash
>>> print("Welcome to Py in the terminal!")
Welcome to Py in the terminal!
```

## Comment quitter un programme Python dans le terminal en utilisant les fonctions `exit()` et `quit()`

Vous pouvez utiliser les fonctions `exit()` et `quit()` pour quitter un programme Python dans Windows et macOS.

```bash
>>> print("Welcome to Py in the terminal!")
Welcome to Py in the terminal!
>>> exit()

C:\Users\USER>
```

![Image](https://www.freecodecamp.org/news/content/images/2023/05/py-in-terminal-exit.PNG)
_Commande exit() dans le terminal Python_

Dans l'exemple ci-dessus, nous avons imprimé "Welcome to Py in the terminal!" avant de quitter le terminal en utilisant la fonction `exit()`.

Après l'exécution de la fonction, vous pourrez utiliser le terminal de manière normale (sans l'environnement Python).

Le processus est le même pour la fonction `quit()` :

```bash
>>> print("Welcome to Py in the terminal!")
Welcome to Py in the terminal!
>>> quit()

C:\Users\USER>
```

![Image](https://www.freecodecamp.org/news/content/images/2023/05/py-in-terminal-quit.PNG)
_Commande exit() dans le terminal Python_

## Comment quitter un programme Python dans le terminal en utilisant la commande `Ctrl +`

Vous pouvez quitter un programme Python en cours d'exécution dans un terminal Windows en utilisant la commande `Ctrl + Z` :

```bash
>>> print("Welcome to Py in the terminal!")
Welcome to Py in the terminal!
>>> ^Z


C:\Users\USER>
```

![Image](https://www.freecodecamp.org/news/content/images/2023/05/py-in-terminal-ctrl-z.PNG)
_Commande ctrl + z pour quitter le terminal Python dans Windows_

De même, vous pouvez utiliser la commande `Ctrl + D` dans macOS.

## Résumé

Dans cet article, nous avons parlé de l'exécution d'un programme Python dans le terminal.

Nous avons vu comment exécuter Python dans le terminal en utilisant la commande `Python`.

Nous avons également vu comment quitter un programme Python dans le terminal en utilisant plusieurs méthodes différentes.

Les fonctions `exit()` et `quit()` peuvent quitter un programme Python dans le terminal pour Windows et macOS.

Alternativement, vous pouvez utiliser la commande `Ctrl + Z` pour quitter un programme Python dans le terminal sous Windows et `Ctrl + D` sous macOS.

Bon codage ! Vous pouvez en apprendre plus sur Python sur [mon blog](https://ihechikara.com/).