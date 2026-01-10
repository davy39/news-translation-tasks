---
title: Les boucles For en Python – Exemple de syntaxe de boucle For
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2023-01-18T17:25:16.000Z'
originalURL: https://freecodecamp.org/news/for-loops-in-python-with-example-code
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/pexels-pixabay-106155.jpg
tags:
- name: Python
  slug: python
seo_title: Les boucles For en Python – Exemple de syntaxe de boucle For
seo_desc: 'While coding in Python, you may need to repeat the same code several times.

  Writing the same lines of code again and again repeatedly throughout your program
  is considered a bad practice in programming – this is where loops come in handy.

  With loops,...'
---

Lors de la programmation en Python, vous pouvez avoir besoin de répéter le même code plusieurs fois.

Écrire les mêmes lignes de code encore et encore de manière répétée dans votre programme est considéré comme une mauvaise pratique en programmation – c'est là que les boucles deviennent utiles.

Avec les boucles, vous pouvez exécuter une séquence d'instructions encore et encore pour un nombre prédéterminé de fois jusqu'à ce qu'une condition spécifique soit remplie.

L'utilisation de boucles dans votre programme vous aidera à gagner du temps, à minimiser les erreurs et à éviter les répétitions.

Il existe deux types de boucles en Python :

- les boucles `for`
- les boucles `while`.

Dans cet article, vous apprendrez tout sur les boucles `for`.

Si vous souhaitez également apprendre les boucles `while`, vous pouvez consulter [cet autre article que j'ai écrit](https://www.freecodecamp.org/news/while-loops-in-python-while-true-loop-statement-example/) sur le sujet.

Commençons !

## Qu'est-ce qu'une boucle `for` en Python ?

Vous pouvez utiliser une boucle `for` pour itérer sur un objet itérable un certain nombre de fois.

Un objet itérable en Python est tout objet qui peut être utilisé comme une séquence et sur lequel on peut boucler.

Il existe de nombreux objets itérables en Python, parmi les plus courants :

- [les listes](https://www.freecodecamp.org/news/create-a-list-in-python-lists-in-python-syntax/)
- [les tuples](https://www.freecodecamp.org/news/python-tuple-vs-list-what-is-the-difference/)
- [les dictionnaires](https://www.freecodecamp.org/news/create-a-dictionary-in-python-python-dict-methods/)
- [les ensembles](https://www.freecodecamp.org/news/python-set-how-to-create-sets-in-python/)
- et [les chaînes de caractères](https://www.freecodecamp.org/news/python-string-manipulation-handbook/)

La boucle `for` itère sur chaque élément de la séquence dans l'ordre.

Et elle exécute le même bloc de code pour chaque élément.

Grâce à ce comportement, la boucle `for` est utile lorsque :

- Vous connaissez le nombre de fois où vous souhaitez exécuter un bloc de code.
- Vous souhaitez exécuter le même code pour chaque élément d'une séquence donnée.

La principale différence entre les boucles `for` et les boucles `while` est que :

- La boucle `for` exécute les instructions un nombre de fois déterminé.
- La boucle `while` exécute la même action plusieurs fois jusqu'à ce qu'une condition soit remplie.

### Analyse de la syntaxe d'une boucle `for` en Python

Si vous avez travaillé avec d'autres langages de programmation, vous remarquerez qu'une boucle `for` en Python est différente des boucles `for` dans d'autres langages.

Par exemple, en JavaScript, la syntaxe générale d'une boucle `for` ressemble à ceci :

```javascript
for (let i = 0; i < 5; i++) {
  console.log('Hello World');
}
```

- Il y a une initialisation, `i = 0`, qui sert de point de départ.
- Une condition qui doit être remplie, `i < 5`, pour que la boucle continue à s'exécuter.
- Un opérateur d'incrémentation, `i++`.
- Des accolades et le corps de la boucle `for` qui contient l'action à effectuer.

Une boucle `for` en Python a une syntaxe plus courte, plus lisible et plus intuitive.

La syntaxe générale pour une boucle `for` en Python ressemble à ceci :

```python
for variable_temporaire in sequence:
    # code qui fait quelque chose
```

Décomposons cela :

- Pour démarrer la boucle `for`, vous devez d'abord utiliser le mot-clé `for`.
- La `variable_temporaire` est une variable arbitraire. Elle itère sur la séquence et pointe vers chaque élément à chaque itération, l'un après l'autre. La variable pourrait avoir presque n'importe quel nom - elle n'a pas besoin d'avoir un nom spécifique.
- Après la `variable_temporaire`, vous utilisez ensuite le mot-clé `in`, qui indique à la `variable_temporaire` de boucler sur les éléments de la séquence.
- La `sequence` peut être une liste Python, un tuple, un dictionnaire, un ensemble, une chaîne de caractères, ou tout autre type d'itérateur. Assurez-vous de ne pas oublier d'ajouter le deux-points, `:` à la fin !
- Ensuite, vous ajoutez une nouvelle ligne et devez ajouter un niveau d'indentation. Un niveau d'indentation en Python est de `4` espaces avec la barre d'espace.
- Enfin, vous devez ajouter le corps de la boucle `for`. Ici, vous spécifiez l'action que vous souhaitez effectuer sur chaque élément de la séquence.

## Comment boucler sur une chaîne de caractères en utilisant une boucle `for` en Python

Comme mentionné précédemment, les chaînes de caractères sont itérables. Elles sont une séquence de caractères, ce qui signifie que vous pouvez itérer sur elles, caractère par caractère.

Prenons l'exemple suivant :

```python
for caractere in "Python":
  print(caractere)

# sortie

# P
# y
# t
# h
# o
# n
```

Dans l'exemple ci-dessus, j'ai bouclé sur la chaîne de caractères `Python` et j'ai imprimé ses lettres individuelles dans la console.

Vous obtiendriez le même résultat si vous stockiez la chaîne dans une variable comme suit :

```python
langage_prefere = "Python"

for caractere in langage_prefere:
  print(caractere)
  
# sortie

# P
# y
# t
# h
# o
# n
```

## Comment boucler sur une liste en utilisant une boucle `for` en Python

Supposons que vous avez une liste de langages de programmation et que vous souhaitez itérer à travers celle-ci et imprimer chaque élément de la séquence jusqu'à atteindre la fin :

```python
langages_de_programmation = ["Python", "JavaScript", "Java", "C++"]

# itérer sur chaque élément de la liste
for langage in langages_de_programmation:
  print(langage)


# sortie

# Python
# JavaScript
# Java
# C++
```

Comme mentionné précédemment, la `variable_iterative` peut être appelée presque n'importe quoi – dans ce cas, je l'ai nommée `langage`.

Cette variable `langage` fait référence à chaque entrée dans la séquence.

Le mot-clé `in`, lorsqu'il est utilisé avec une boucle `for`, indique qu'il itère sur chaque élément de la séquence.

Lors de la première itération de la boucle, `langage` pointe vers le premier élément de la liste, `Python`.

Les instructions de code à l'intérieur du corps de la boucle sont exécutées, donc `Python` est imprimé dans la console.

Lors de la deuxième itération, la variable est mise à jour et pointe vers le deuxième élément, `JavaScript`. Elle exécute les mêmes instructions de code dans le corps de la boucle.

La même procédure se produit pour tous les éléments de la liste jusqu'à ce que la boucle atteigne la fin et que chaque élément ait été itéré.

## Comment boucler sur un tuple en utilisant une boucle `for` en Python

Essayons d'itérer sur tous les éléments à l'intérieur d'un tuple.

```python
mes_infos = ("John", "Doe", 26, "Ingénieur Logiciel")

for donnee in mes_infos:
  print(donnee)
  
# sortie

# John
# Doe
# 26
# Ingénieur Logiciel
```

Comme vous le voyez, le processus d'utilisation d'une boucle `for` avec des tuples est le même que l'utilisation d'une boucle `for` avec des listes.

## Comment boucler sur un dictionnaire en utilisant une boucle `for` en Python

Maintenant, prenons un dictionnaire et itérons sur les paires clé-valeur :

```python
mes_infos = {
  'nom':'John Doe',
  'titre_emploi':'ingénieur logiciel',
  'pays':'USA'
}

for info in mes_infos:
  print(info)

# nom
# titre_emploi
# pays
```

Lorsque j'utilise la même syntaxe que pour les chaînes, les listes, les tuples et les ensembles avec un dictionnaire, je me retrouve avec seulement les clés.

Pour boucler sur les paires clé et valeur dans un dictionnaire, vous devez faire ce qu'on appelle le [déballage de tuple](https://forum.freecodecamp.org/t/the-ultimate-guide-to-python-tuples-python-data-structure-tutorial-with-code-examples/19165) en spécifiant deux variables.

Vous devrez également utiliser la méthode `.items()` pour boucler à la fois sur les clés et les valeurs :

```python
mes_infos = {
  'nom':'John Doe',
  'titre_emploi':'ingénieur logiciel',
  'pays':'USA'
}

for cle,valeur in mes_infos.items():
  print(cle,":",valeur)

# sortie

# nom : John Doe
# titre_emploi : ingénieur logiciel
# pays : USA
```

Mais que se passe-t-il lorsque vous n'utilisez pas la méthode `.items()` ?

```python
mes_infos = {
  'nom':'John Doe',
  'titre_emploi':'ingénieur logiciel',
  'pays':'USA'
}

for cle,valeur in mes_infos:
  print(cle,":",valeur)


# sortie

# Traceback (most recent call last):
#  File "main.py", line 7, in <module>
#    for cle,valeur in mes_infos:
# ValueError: too many values to unpack (expected 2)
```

Vous obtenez une `ValueError` car Python attend des paires clé et valeur. En Python, les clés et les valeurs ne sont pas séparées – elles vont de pair.

## Comment écrire une instruction `break` dans une boucle `for` en Python

Par défaut, une boucle `for` en Python bouclera à travers l'objet itérable entier jusqu'à ce qu'elle atteigne la fin.

Cependant, il peut y avoir des moments où vous souhaitez avoir plus de contrôle sur le flux de la boucle `for`.

Par exemple, vous pouvez vouloir sortir de la boucle prématurément si une condition spécifique est remplie.

Pour y parvenir, vous pouvez utiliser l'instruction `break`.

Prenons l'exemple suivant :

```python
langages_de_programmation = ["Python", "JavaScript", "Java", "C++"]

for langage in langages_de_programmation:
  print(langage)
  if langage == "Java":
    break

# sortie

# Python
# JavaScript
# Java
```

Dans l'exemple ci-dessus, je veux sortir de la boucle lorsque la variable `langage` pointe vers l'élément de la liste `"Java"`.

Lorsque Python voit le mot-clé `break`, il arrête d'exécuter la boucle, et tout code qui vient après l'instruction ne s'exécute pas.

Comme vous le voyez à partir de la sortie du code, `"Java"` est imprimé dans la console, et la boucle est terminée.

Si vous vouliez sortir de la boucle lorsque la variable `langage` pointe vers `"Java"` mais ne pas imprimer la valeur dans la console, alors vous écririez ce qui suit :

```python
langages_de_programmation = ["Python", "JavaScript", "Java", "C++"]

for langage in langages_de_programmation:
  if langage == "Java":
    break
  print(langage)
  
# sortie

# Python
# JavaScript
```

## Comment écrire une instruction `continue` dans une boucle `for` en Python

Que faire si vous souhaitez ignorer un élément particulier ?

L'instruction `continue` ignore l'exécution du corps de la boucle lorsqu'une condition est remplie.

Prenons l'exemple suivant :

```python
langages_de_programmation = ["Python", "JavaScript", "Java", "C++"]


for langage in langages_de_programmation:
  if langage == "Java":
    continue
  print(langage)

# sortie

# Python
# JavaScript
# C++
```

Dans l'exemple ci-dessus, je voulais ignorer `"Java"` de ma liste.

J'ai spécifié que si la variable `langage` pointe vers `"Java"`, Python devrait s'arrêter et ignorer l'exécution à ce point et continuer à l'élément suivant de la liste jusqu'à ce qu'il atteigne la fin.

La différence entre les instructions `break` et `continue` est que l'instruction `break` termine la boucle complètement.

D'un autre côté, l'instruction `continue` arrête l'itération actuelle à un point spécifique et passe à l'élément suivant de l'objet itérable – elle ne quitte pas complètement la boucle.

## Comment utiliser la fonction `range()` dans une boucle `for` en Python

Si vous souhaitez boucler à travers un ensemble de code un nombre de fois spécifié, vous pouvez utiliser la fonction intégrée `range()` de Python.

Par défaut, la fonction `range()` retourne une séquence de nombres commençant par `0`, incrémentant de un, et se terminant à un nombre que vous spécifiez.

La syntaxe pour cela ressemble à ceci :

```python
range(fin)
```

L'argument `fin` est requis.

Voyons l'exemple suivant :

```python
for i in range(4):
  print(i)

# sortie

# 0
# 1
# 2
# 3
```

Dans cet exemple, j'ai spécifié un `range(4)`.

Cela signifie que la fonction commencera à compter à partir de `0`, incrémentera de `1` à chaque itération, et se terminera à `3`.

Gardez à l'esprit que la plage que vous spécifiez n'est pas inclusive ! Donc, un `range(4)` se terminera à `3` et non à `4`.

Donc, il inclura les valeurs de `0` à `3` et non de `0` à `4`.

Que faire si vous souhaitez itérer à travers une plage de deux nombres que vous spécifiez et ne pas commencer à partir de `0` ?

Vous pouvez passer un deuxième argument optionnel `début` pour spécifier le nombre de départ.

La syntaxe pour cela ressemble à ceci :

```
range(début, fin)
```

Si vous souhaitez une plage de valeurs de `10` inclus à `20` inclus, vous écrivez une plage de `range(10,21)`, comme suit :

```python
for i in range(10,21):
  print(i)
  
# sortie

# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20
```

Encore une fois, `range(10,21)` n'inclut pas `21`.

Enfin, si vous ne souhaitez pas que l'incrément par défaut soit `1`, vous pouvez spécifier un troisième paramètre optionnel, le paramètre `pas`.

La syntaxe pour cela ressemble à ceci :

```
range(début, fin, pas)
```

Une chose à noter est que `pas` peut être soit un nombre négatif ou positif, mais il ne peut pas être `0`.

Prenons l'exemple suivant :

```python
for i in range(10,21,2):
  print(i)
  
# sortie

# 10
# 12
# 14
# 16
# 18
# 20
```

Dans cet exemple, je voulais inclure les valeurs de `10` à `20` et incrémenter de `2`.

J'ai réalisé cela en spécifiant une valeur d'incrément de `2`.

Prenons un autre exemple.

Supposons que vous avez une liste d'éléments et que vous souhaitez faire quelque chose avec les éléments qui dépendent de la longueur de la liste.

Pour cela, vous pourriez utiliser `range()` et passer la longueur de votre liste comme argument à la fonction.

Pour calculer la longueur d'une liste, utilisez la fonction `len()`.

```python
langages_de_programmation = ["Python", "JavaScript", "Java", "C++"]

longueur_langages_de_programmation = len(langages_de_programmation)

for langages in range(longueur_langages_de_programmation):
  print("Bonjour le Monde")
  
# sortie

# Bonjour le Monde
# Bonjour le Monde
# Bonjour le Monde
# Bonjour le Monde
```

## Conclusion

Espérons que cet article vous a aidé à comprendre comment utiliser les boucles `for` en Python.

Vous avez appris comment écrire une boucle `for` pour itérer sur des chaînes de caractères, des listes, des tuples et des dictionnaires.

Vous avez également vu comment utiliser les instructions `break` et `continue` pour contrôler le flux de la boucle `for`.

Enfin, vous avez vu comment spécifier une plage de nombres à utiliser dans votre boucle `for` avec la fonction `range()`.

Merci d'avoir lu, et bon codage !