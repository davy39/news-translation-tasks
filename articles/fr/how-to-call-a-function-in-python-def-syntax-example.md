---
title: Comment Appeler une Fonction en Python – Exemple de Syntaxe Def
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-07-20T16:17:26.000Z'
originalURL: https://freecodecamp.org/news/how-to-call-a-function-in-python-def-syntax-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/callFunction.png
tags:
- name: Python
  slug: python
seo_title: Comment Appeler une Fonction en Python – Exemple de Syntaxe Def
seo_desc: "In Python and other programming languages, you can use functions to avoid\
  \ repeting yourself and to reuse pieces of code.\nTo make functions work, you don’t\
  \ just write them and say goodbye – you have to call them too. \nBefore you call\
  \ a function, you n..."
---

En Python et dans d'autres langages de programmation, vous pouvez utiliser des fonctions pour éviter de vous répéter et pour réutiliser des morceaux de code.

Pour que les fonctions fonctionnent, vous ne les écrivez pas et ne dites pas au revoir – vous devez aussi les appeler.

Avant d'appeler une fonction, vous devez l'écrire avec le mot-clé def. Donc dans cet article, je ne vais pas seulement vous montrer comment appeler une fonction, je vais aussi vous montrer comment la créer.

## Ce que nous allons couvrir
- [Comment Définir une Fonction avec le Mot-Clé `def`](#heading-comment-definir-une-fonction-avec-le-mot-cle-def)
- [Comment Appeler une Fonction en Python](#heading-comment-appeler-une-fonction-en-python)
- [Comment Appeler une Fonction Imbriquée en Python](#heading-comment-appeler-une-fonction-imbriquee-en-python)
- [Réflexions Finales](#heading-reflexions-finales)


## Comment Définir une Fonction avec le Mot-Clé `def`

Pour définir une fonction en Python, vous tapez d'abord le mot-clé def, puis le nom de la fonction et les parenthèses.

Pour indiquer à Python que la fonction est un bloc de code, vous spécifiez un deux-points devant le nom de la fonction. Ce qui suit est ce que vous voulez que la fonction fasse.

La syntaxe de base d'une fonction ressemble à ceci :
```py
def nom_de_la_fonction():
    # Ce que vous voulez que la fonction fasse
```

Un exemple de fonction ressemble à ceci :
```py
def apprendre_a_coder():
    print("Vous pouvez apprendre à coder gratuitement sur freeCodeCamp")

```
Ce que nous voulons que cette fonction fasse, c'est d'imprimer le texte `Vous pouvez apprendre à coder gratuitement sur freeCodeCamp` dans le terminal.

Pour faire fonctionner cette fonction, vous devez l'appeler. C'est ce que nous allons faire ensuite.

## Comment Appeler une Fonction en Python

Pour appeler une fonction, utilisez simplement son nom suivi des arguments entre parenthèses.

La syntaxe pour appeler une fonction ressemble à ceci :
```py
nom_de_la_fonction()
```

Pour appeler une fonction que nous avons définie précédemment, nous devons écrire `apprendre_a_coder()` :

```py
def apprendre_a_coder():
    print("Vous pouvez apprendre à coder gratuitement sur freeCodeCamp")

apprendre_a_coder()
# Sortie : Vous pouvez apprendre à coder gratuitement sur freeCodeCamp
```

**N.B** : Assurez-vous de ne pas spécifier l'appel de la fonction à l'intérieur du bloc de la fonction. Cela ne fonctionnera pas car l'appel sera traité comme une partie de la fonction à exécuter.

![ss1-3](https://www.freecodecamp.org/news/content/images/2022/07/ss1-3.png)

Vous pouvez voir que la fonction n'a pas imprimé le texte dans le terminal car j'ai tenté de l'appeler à l'intérieur du bloc de la fonction.

![ss2-4](https://www.freecodecamp.org/news/content/images/2022/07/ss2-4.png)

Et ici, vous pouvez voir que la fonction s'exécute car je l'ai appelée en dehors du bloc de la fonction.


## Comment Appeler une Fonction Imbriquée en Python

Il peut être confus d'appeler une fonction imbriquée, donc je veux vous montrer comment faire.

Voici la fonction imbriquée :
```py
def apprendre_a_coder():
    print("Vous pouvez apprendre à coder gratuitement sur freeCodeCamp")

    def apprendre_quel_langage():
        print("Vous pouvez apprendre n'importe quel langage de programmation sur la chaîne YouTube de freeCodeCamp")
  
```

La fonction `apprendre_quel_langage` fait partie de la fonction `apprendre_a_coder` car elle est imbriquée à l'intérieur.

Si vous tapez `apprendre_a_coder()` et exécutez le code, seule la fonction externe (apprendre_a_coder) est appelée :

![ss3-3](https://www.freecodecamp.org/news/content/images/2022/07/ss3-3.png)
Vous pouvez voir que seule la fonction externe est appelée et que la fonction interne est grisée.

Pour appeler également la fonction interne, vous devez taper `apprendre_quel_langage()` précisément. Mais où ?

Vous devez regarder juste sous le mot-clé def de la fonction interne et taper l'appel de la fonction là.

Mais si vous faites seulement cela, cela ne fonctionnera toujours pas car vous devez également appeler la fonction externe.

![ss4-3](https://www.freecodecamp.org/news/content/images/2022/07/ss4-3.png)
Vous pouvez voir que la fonction interne (`apprendre_quel_langage`) n'a toujours pas fait ce que nous voulons qu'elle fasse.

Pour que cela fonctionne, vous devez appeler les deux fonctions où nécessaire :
```py
def apprendre_a_coder():
    print("Vous pouvez apprendre à coder gratuitement sur freeCodeCamp")

    def apprendre_quel_langage():
        print("Vous pouvez apprendre n'importe quel langage de programmation sur la chaîne YouTube de freeCodeCamp")
    
    apprendre_quel_langage()

apprendre_a_coder()

"""
Sortie :
Vous pouvez apprendre à coder gratuitement sur freeCodeCamp
Vous pouvez apprendre n'importe quel langage de programmation sur la chaîne YouTube de freeCodeCamp
"""
 ```

![ss5-4](https://www.freecodecamp.org/news/content/images/2022/07/ss5-4.png)
Vous pouvez voir que tout fonctionne comme prévu.

## Réflexions Finales

J'espère que cet article vous aide à apprendre comment appeler correctement une fonction en Python.

Si vous voulez apprendre davantage sur Python, vous pouvez consulter le [programme Python de freeCodeCamp](https://www.freecodecamp.org/learn/scientific-computing-with-python/). C'est gratuit.

Continuez à coder :)