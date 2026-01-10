---
title: Python Print Sans Nouvelle Ligne [RÉSOLU]
subtitle: ''
author: Farhan Hasin Chowdhury
co_authors: []
series: null
date: '2022-05-10T16:18:38.000Z'
originalURL: https://freecodecamp.org/news/python-print-without-newline-solved
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/Python-Print-Without-Newline--SOLVED-.png
tags:
- name: Python
  slug: python
seo_title: Python Print Sans Nouvelle Ligne [RÉSOLU]
seo_desc: "If you're familiar with Python, you may have noticed that the built-in\
  \ function print() doesn't need an explicit \\n character at the end of each line.\
  \ \nThis means that the output from the following snippet of code\nprint('freeCodeCamp\
  \ Curriculum')\npri..."
---

Si vous êtes familier avec Python, vous avez peut-être remarqué que la fonction intégrée `print()` n'a pas besoin d'un caractère `\n` explicite à la fin de chaque ligne. 

Cela signifie que la sortie du code suivant

```python
print('freeCodeCamp Curriculum')
print('freeCodeCamp News')
print('freeCodeCamp YouTube Channel')
```

sera :

```shell
freeCodeCamp Curriculum
freeCodeCamp News
freeCodeCamp YouTube Channel
```

Cela se produit parce que la fonction `print()` ajoute le caractère `\n` à la fin de chaque ligne imprimée. Bien que cela soit généralement pratique, vous pouvez parfois vouloir imprimer des lignes sans le caractère `\n`.

Dans cet article, vous apprendrez comment changer la fin de chaque instruction print. Et vous apprendrez également plusieurs autres façons de modifier le comportement par défaut de la fonction intégrée.

## Comment Imprimer Sans Nouvelle Ligne en Python

Selon la [documentation officielle](https://docs.python.org/3/library/functions.html#print) pour la fonction `print()`, la signature de la fonction est la suivante :

```
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

Comme vous pouvez le voir, la fonction prend cinq arguments au total. Le premier est l'objet ou les objets que vous souhaitez imprimer sur le terminal. Ensuite, il y a le séparateur (que vous apprendrez dans une section ultérieure), et le paramètre `end`.

La valeur par défaut du paramètre `end` est `\n`, ce qui signifie qu'un caractère de nouvelle ligne sera ajouté à chaque ligne imprimée sur le terminal. 

Pour changer ce comportement, vous pouvez simplement remplacer ce paramètre comme suit :

```python
print('freeCodeCamp Curriculum', end=', ')
print('freeCodeCamp News', end=', ')
print('freeCodeCamp YouTube Channel')
```

Puisque j'ai changé la valeur de `end` en une virgule, la sortie sera `freeCodeCamp Curriculum, freeCodeCamp News, freeCodeCamp YouTube Channel` au lieu des trois lignes séparées. 

Vous pouvez utiliser n'importe quel caractère comme valeur de `end`. Si vous ne voulez rien à la fin des lignes, utilisez simplement une chaîne vide.

## Comment Imprimer Avec un Séparateur en Python

Vous souvenez-vous de l'argument `sep` dans la signature de la fonction ? Dans cette section, vous apprendrez son utilisation. 

Vous savez peut-être déjà que la fonction `print()` peut prendre plusieurs objets à la fois pour les imprimer comme suit :

```python
print('freeCodeCamp Curriculum', 'freeCodeCamp News', 'freeCodeCamp YouTube Channel')
```

La sortie de ce code sera :

```shell
freeCodeCamp Curriculum, freeCodeCamp News, freeCodeCamp YouTube Channel
```

Comme vous pouvez le voir, la fonction a imprimé les trois chaînes sur une seule ligne séparées par des virgules. Si vous voulez utiliser autre chose comme un tiret comme séparateur, vous pouvez le faire comme suit :

```python
print('freeCodeCamp Curriculum', 'freeCodeCamp News', 'freeCodeCamp YouTube Channel', sep=' - ')
```

La sortie de ce code sera :

```shell
freeCodeCamp Curriculum - freeCodeCamp News - freeCodeCamp YouTube Channel
```

J'espère que vous avez compris l'idée. Comme l'argument `end`, vous pouvez utiliser plus ou moins n'importe quelle chaîne valide comme valeur de l'argument `sep`.

## Comment Imprimer Dans un Fichier en Python

Au lieu d'imprimer des choses sur le terminal, vous pouvez également utiliser la fonction `print()` pour imprimer directement dans un fichier. 

La fonction `print()` prend un autre argument `file` qui par défaut est `sys.stdout` ou la sortie standard. C'est le descripteur de fichier par défaut où un processus peut écrire la sortie.

Vous pouvez remplacer cela pour écrire dans un fichier comme suit :

```python
with open('output.txt', 'w') as f:
    print('freeCodeCamp', file=f)
```

Tout d'abord, vous ouvrez un fichier appelé `output.txt` en tant que `f` et vous le passez comme valeur de l'argument `file`. Si vous exécutez le code, un nouveau fichier sera créé et à l'intérieur de ce fichier se trouvera votre sortie.

## Conclusion

La fonction `print()` est l'une des fonctions les plus couramment utilisées en Python. Avoir une bonne compréhension des différentes utilisations de cette fonction intégrée peut donc augmenter votre productivité. 

Il y a également un autre argument, `flush`, dans la fonction. C'est un booléen et le définir sur `True` videra la sortie à chaque exécution.

J'ai également un blog personnel où j'écris sur des sujets technologiques variés, donc si vous êtes intéressé par ce genre de choses, consultez [https://farhan.dev](https://farhan.dev). Si vous avez des questions ou si quelque chose vous semble confus — ou si vous voulez simplement entrer en contact — je suis disponible sur [Twitter](https://twitter.com/frhnhsin) et [LinkedIn](https://www.linkedin.com/in/farhanhasin/).