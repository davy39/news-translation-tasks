---
title: Python if __name__ == __main__ Expliqué avec des Exemples de Code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-03T19:48:00.000Z'
originalURL: https://freecodecamp.org/news/if-name-main-python-example
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c99de740569d1a4ca2229.jpg
tags:
- name: Python
  slug: python
seo_title: Python if __name__ == __main__ Expliqué avec des Exemples de Code
seo_desc: "By Goran Aviani\nWhen a Python interpreter reads a Python file, it first\
  \ sets a few special variables. Then it executes the code from the file. \nOne of\
  \ those variables is called __name__.\nIf you follow this article step-by-step and\
  \ read its code snipp..."
---

Par Goran Aviani

Lorsque l'interpréteur Python lit un fichier Python, il définit d'abord quelques variables spéciales. Ensuite, il exécute le code du fichier.

L'une de ces variables s'appelle `__name__`.

Si vous suivez cet article étape par étape et lisez ses extraits de code, vous apprendrez comment utiliser `if __name__ == "__main__"`, et pourquoi c'est si important.

## Modules Python Expliqués

Les fichiers Python sont appelés modules et sont identifiés par l'extension de fichier `.py`. Un module peut définir des fonctions, des classes et des variables.

Ainsi, lorsque l'interpréteur exécute un module, la variable `__name__` sera définie comme `__main__` si le module qui est exécuté est le programme principal.

Mais si le code importe le module depuis un autre module, alors la variable `__name__` sera définie comme le nom de ce module.

Prenons un exemple. Créez un module Python nommé `file_one.py` et collez ce code de niveau supérieur à l'intérieur :

```python
# Module un fichier Python

print("File one __name__ is set to: {}" .format(__name__))
```

En exécutant ce fichier, vous verrez exactement ce dont nous parlions. La variable `__name__` pour ce module est définie comme `__main__` :

```
File one __name__ is set to: __main__
```

Ajoutez maintenant un autre fichier nommé `file_two.py` et collez ce code à l'intérieur :

```python
# Module Python à importer

print("File two __name__ is set to: {}" .format(__name__))

```

Modifiez également le code dans `file_one.py` comme ceci pour importer le module `file_two` :

```python
# Module Python à exécuter
import file_two

print("File one __name__ is set to: {}" .format(__name__))

```

Exécuter notre code `file_one` une fois de plus montrera que la variable `__name__` dans `file_one` n'a pas changé et reste définie comme `__main__`. Mais maintenant, la variable `__name__` dans `file_two` est définie comme son nom de module, donc `file_two`.

Le résultat devrait ressembler à ceci :

```
File two __name__ is set to: file_two
File one __name__ is set to: __main__

```

Mais exécutez `file_two` directement et vous verrez que son nom est défini comme `__main__` :

```
File two __name__ is set to: __main__


```

La variable `__name__` pour le fichier/module qui est exécuté sera toujours `__main__`. Mais la variable `__name__` pour tous les autres modules qui sont importés sera définie comme le nom de leur module.

## Conventions de Nommage des Fichiers Python

La manière habituelle d'utiliser `__name__` et `__main__` ressemble à ceci :

```python
if __name__ == "__main__":
   Faire quelque chose ici


```

Voyons comment cela fonctionne dans la vie réelle, et comment utiliser réellement ces variables.

Modifiez `file_one` et `file_two` pour qu'ils ressemblent à ceci :

`file_one` :

```python
# Module Python à exécuter
import file_two

print("File one __name__ is set to: {}" .format(__name__))

if __name__ == "__main__":
   print("File one executed when ran directly")
else:
   print("File one executed when imported")

```

`file_two` :

```python
# Module Python à importer

print("File two __name__ is set to: {}" .format(__name__))

if __name__ == "__main__":
   print("File two executed when ran directly")
else:
   print("File two executed when imported")

```

Encore une fois, lorsque vous exécutez `file_one`, vous verrez que le programme a reconnu lequel de ces deux modules est `__main__` et a exécuté le code selon nos premières instructions `if else`.

Le résultat devrait ressembler à ceci :

```
File two __name__ is set to: file_two
File two executed when imported
File one __name__ is set to: __main__
File one executed when ran directly

```

Maintenant, exécutez `file_two` et vous verrez que la variable `__name__` est définie comme `__main__` :

```
File two __name__ is set to: __main__
File two executed when ran directly

```

Lorsque des modules comme celui-ci sont importés et exécutés, leurs fonctions seront importées et le code de niveau supérieur exécuté.

Pour voir ce processus en action, modifiez vos fichiers pour qu'ils ressemblent à ceci :

`file_one` :

```python
# Module Python à exécuter
import file_two

print("File one __name__ is set to: {}" .format(__name__))

def function_one():
   print("Function one is executed")

def function_two():
   print("Function two is executed")

if __name__ == "__main__":
   print("File one executed when ran directly")
else:
   print("File one executed when imported")

```

`file_two` :

```python
# Module Python à importer

print("File two __name__ is set to: {}" .format(__name__))

def function_three():
   print("Function three is executed")

if __name__ == "__main__":
   print("File two executed when ran directly")
else:
   print("File two executed when imported")

```

Maintenant, les fonctions sont chargées mais non exécutées.

Pour exécuter l'une de ces fonctions, modifiez la partie `if __name__ == "__main__"` de `file_one` pour qu'elle ressemble à ceci :

```python
if __name__ == "__main__":
   print("File one executed when ran directly")
   function_two()
else:
   print("File one executed when imported")

```

Lorsque vous exécutez `file_one`, vous devriez voir ce qui suit :

```
File two __name__ is set to: file_two
File two executed when imported
File one __name__ is set to: __main__
File one executed when ran directly
Function two is executed

```

De plus, vous pouvez exécuter des fonctions depuis des fichiers importés. Pour ce faire, modifiez la partie `if __name__ == "__main__"` de `file_one` pour qu'elle ressemble à ceci :

```python
if __name__ == "__main__":
   print("File one executed when ran directly")
   function_two()
   file_two.function_three()
else:
   print("File one executed when imported")

```

Et vous pouvez vous attendre à un résultat comme ceci :

```
File two __name__ is set to: file_two
File two executed when imported
File one __name__ is set to: __main__
File one executed when ran directly
Function two is executed
Function three is executed

```

Maintenant, supposons que le module `file_two` est vraiment grand avec beaucoup de fonctions (deux dans notre cas), et que vous ne voulez pas tout importer. Modifiez `file_two` pour qu'il ressemble à ceci :

```python
# Module Python à importer

print("File two __name__ is set to: {}" .format(__name__))

def function_three():
   print("Function three is executed")

def function_four():
   print("Function four is executed")

if __name__ == "__main__":
   print("File two executed when ran directly")
else:
   print("File two executed when imported")

```

Et pour importer des fonctions spécifiques depuis le module, utilisez le bloc d'importation `from` dans le fichier `file_one` :

```python
# Module Python à exécuter
from file_two import function_three

print("File one __name__ is set to: {}" .format(__name__))

def function_one():
   print("Function one is executed")

def function_two():
   print("Function two is executed")

if __name__ == "__main__":
   print("File one executed when ran directly")
   function_two()
   function_three()
else:
   print("File one executed when imported")
```

## Conclusion

Il y a un cas d'utilisation vraiment intéressant pour la variable `__name__`, que vous souhaitiez un fichier qui peut être exécuté comme programme principal ou importé par d'autres modules. Nous pouvons utiliser un bloc `if __name__ == "__main__"` pour permettre ou empêcher des parties de code d'être exécutées lorsque les modules sont importés.

Lorsque l'interpréteur Python lit un fichier, la variable `__name__` est définie comme `__main__` si le module est exécuté, ou comme le nom du module s'il est importé. La lecture du fichier exécute tout le code de niveau supérieur, mais pas les fonctions et les classes (puisqu'elles ne seront que importées).

Bra gjort ! (Cela signifie "Bien joué" en suédois !)

Consultez plus d'articles comme celui-ci sur mon [profil freeCodeCamp](https://www.freecodecamp.org/news/author/goran/), mon [profil Medium](https://medium.com/@goranaviani), et d'autres choses amusantes que je construis sur ma [page GitHub](https://github.com/GoranAviani).