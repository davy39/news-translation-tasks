---
title: Erreur Python SyntaxError Unexpected EOF While Parsing [Résolu]
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-03-21T13:47:24.000Z'
originalURL: https://freecodecamp.org/news/syntaxerror-unexpected-eof-while-parsing-python-error-solved
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/solve.jpg
tags:
- name: error handling
  slug: error-handling
- name: Python
  slug: python
seo_title: Erreur Python SyntaxError Unexpected EOF While Parsing [Résolu]
seo_desc: "Error messages help us solve/fix problems in our code. But some error messages,\
  \ when you first see them, may confuse you because they seem unclear. \nOne of these\
  \ errors is the \"SyntaxError: unexpected EOF while parsing\" error you might get\
  \ in Python...."
---

Les messages d'erreur nous aident à résoudre/corriger les problèmes dans notre code. Mais certains messages d'erreur, quand vous les voyez pour la première fois, peuvent vous troubler car ils semblent flous. 

L'une de ces erreurs est l'erreur « SyntaxError: unexpected EOF while parsing » que vous pourriez rencontrer en Python.

Dans cet article, nous verrons pourquoi cette erreur se produit et comment la corriger avec quelques exemples. 

## Comment corriger l'erreur « SyntaxError: Unexpected EOF While Parsing »

Avant d'examiner quelques exemples, nous devrions d'abord comprendre pourquoi nous pourrions rencontrer cette erreur.

La première chose à comprendre est la signification du message d'erreur. EOF signifie **End of File** (fin de fichier) en Python. Un EOF inattendu implique que l'interprète a atteint la fin de notre programme avant d'exécuter tout le code.

Cette erreur est susceptible de se produire lorsque :

* nous ne déclarons pas d'instruction pour une boucle (`while`/`for`)
* nous oublions la parenthèse fermante ou l'accolade dans un bloc de code. 

Jetez un œil à cet exemple :

```python
student = {
  "name": "John",
  "level": "400",
  "faculty": "Engineering and Technology"

```

Dans le code ci-dessus, nous avons créé un dictionnaire mais avons oublié d'ajouter **`}`** (l'accolade fermante) – cela va donc certainement générer l'erreur « SyntaxError: unexpected EOF while parsing ».

Après avoir ajouté l'accolade fermante, le code devrait ressembler à ceci :

```python
student = {
  "name": "John",
  "level": "400",
  "faculty": "Engineering and Technology"
}
```

Cela devrait éliminer l'erreur.

Regardons un autre exemple.

```python
i = 1
while i < 11:
```

Dans la boucle `while` ci-dessus, nous avons déclaré notre variable et une condition mais avons omis l'instruction qui devrait s'exécuter jusqu'à ce que la condition soit remplie. Cela provoquera une erreur.

Voici la correction :

```python
i = 1
while i < 11:
  print(i)
  i += 1
  

```

Maintenant, notre code s'exécutera comme prévu et affichera les valeurs de `i` de 1 jusqu'à la dernière valeur de `i` inférieure à 11. 

C'est essentiellement tout ce qu'il faut pour corriger cette erreur. Pas si difficile, n'est-ce pas ? 

Pour plus de sécurité, fermez toujours chaque parenthèse et accolade dès qu'elles sont créées avant d'écrire la logique imbriquée (la plupart des éditeurs de code/IDE les fermeront automatiquement pour nous).

De même, déclarez toujours des instructions pour vos boucles avant d'exécuter le code.

## Conclusion

Dans cet article, nous avons compris pourquoi l'erreur « SyntaxError: unexpected EOF while parsing » se produit lorsque nous exécutons notre code. Nous avons également vu quelques exemples montrant comment corriger cette erreur.

Bon codage !