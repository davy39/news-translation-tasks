---
title: Python Reverse String – Inversion de Chaîne en Python Expliquée avec des Exemples
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2021-11-10T16:40:09.000Z'
originalURL: https://freecodecamp.org/news/python-reverse-string-string-reversal-in-python-explained-with-code-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/designecologist-sYI_WSHEsXU-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: Python Reverse String – Inversion de Chaîne en Python Expliquée avec des
  Exemples
seo_desc: "When you're working with Python strings, there are times when you'll have\
  \ to reverse them, and work with their reversed copies instead. \nBut since Python\
  \ strings are immutable, you cannot modify or reverse them in place.\nIn Python,\
  \ there are a few di..."
---

Lorsque vous travaillez avec des chaînes de caractères en Python, il arrive que vous deviez les inverser et travailler avec leurs copies inversées.

Mais comme les chaînes de caractères Python sont _immuables_, vous ne pouvez pas les modifier ou les inverser sur place.

En Python, il existe plusieurs façons de procéder. Ce tutoriel vous apprendra à utiliser le slicing de chaînes, les méthodes intégrées et la récursivité pour inverser des chaînes.

### 🏁 Ce que vous allez apprendre

* [Utiliser la **Récursivité** pour inverser des chaînes](#heading-comment-inverser-des-chaines-en-python-en-utilisant-la-recursion) : Vous apprendrez comment fonctionne la récursivité et l'intuition derrière l'inversion de chaînes en utilisant la récursivité.
* [Utiliser le **Slicing de Chaînes** pour inverser des chaînes](#heading-comment-inverser-des-chaines-en-python-en-utilisant-le-slicing-de-chaines) : Vous apprendrez une méthode beaucoup plus simple pour inverser des chaînes en Python.
* [Utiliser les **Méthodes Intégrées**](#heading-comment-inverser-des-chaines-en-python-en-utilisant-les-methodes-reversed-et-join) : Vous apprendrez une autre méthode facile et intuitive pour inverser des chaînes en Python.

Alors, commençons.

## Comment inverser des chaînes en Python en utilisant la récursivité

Avant d'apprendre à utiliser la récursivité pour inverser des chaînes, commençons par comprendre comment fonctionne la récursivité.

> La récursivité est un paradigme de programmation puissant. Pour résoudre le problème d'intérêt, une fonction récursive **s'appelle elle-même** répétitivement, jusqu'à ce qu'un **cas de base** soit atteint.

Eh bien, c'est ce que vous aurez probablement lu sur la récursivité auparavant.

Reformulons cette définition en langage simple maintenant.

### La récursivité en langage simple

Supposons que vous avez créé une fonction pour résoudre un problème.

* La fonction est conçue de telle sorte que chaque fois qu'elle est appelée, elle **s'appelle elle-même** à nouveau.
* Ce sont ce qu'on appelle des appels de fonction **récursifs**. 
* Chaque appel de fonction récursive effectue la même petite quantité de travail.
* Et cela continue jusqu'à ce qu'il n'y ait plus de travail à faire. Et la fonction n'a plus besoin de s'appeler elle-même – c'est ce qu'on appelle le **cas de base**. 

### Comment utiliser la récursivité pour inverser des chaînes

Discutons maintenant de la motivation derrière l'inversion intuitive des chaînes. Pour ce faire, considérons la chaîne `"code"`.

**Problème :** Inverser la chaîne `"code"`.

![Image](https://lh5.googleusercontent.com/9EzNJgPbbGbmddk3f_t55PSDTr7cP5fgdXJjCX9B_hPkP1GHzOq58PR3wkZPRSdU5_O7SC4g8tZOQVjlNx6Ya9jc00aeqgXP-fvGHECpU7lF64AWYraIz25u-6JbmvTXQCkI1HY_)

Oublions la récursivité un instant et commençons par ce que vous savez.

> La première lettre de la chaîne originale sera la dernière lettre de la chaîne inversée, n'est-ce pas ?

* Donc, retirez la première lettre – `"c"` ici – et placez-la à la toute fin.
* Vous avez maintenant la chaîne `"ode"`. Et le problème se réduit à inverser cette sous-chaîne `"ode"` [car `"c"` est déjà à la bonne place]

![Image](https://lh4.googleusercontent.com/V4oyw-hYeZWzSzu0JULaKLzHynBWgQCAB-GJrEU6sb8j5u9OKY7DRIvDbYEw-2MrWY-rNcFmVYbkSQMfQyx6AjYG7j-flGQktEEwoZpO1H0Fl1Hkwq0MN2UpiPl3QYclrDWN91oU)

* Vous pouvez faire la même tâche de retirer la première lettre encore une fois, maintenant `"o"`. Et la placer dans le dernier emplacement disponible à droite.
* Maintenant que `"c"` et `"o"` ont été traités, il vous reste le problème d'inverser la sous-chaîne `"de"`.

![Image](https://lh3.googleusercontent.com/IfSSH94VWA90ZxOSGqKUYBRUqFwT_nLY3W7vFJ4_jYdTIbUIQ17FabArbDqVv9cZ2jVdKoJTh0IFhKnoACscgipWLpL3iwfoeRV8FuFIABVPriynIqJabAccqr-UJHpScXBmuJQ9)

* Faites-le encore quelques fois – retirez d'abord `"d"`, puis `"e"`.

![Image](https://lh5.googleusercontent.com/LDgbioxKdX1Mey1FpzF20KnWnCAVNIQZFWTczaB-IDiKhHOWudo5Wnx8qg5XyiBnA0r5UVwERxVYodPtcvSM39Irn7kJvMZ5X8UzdpVDwTfhKsr0uxNPadgMTCpmEy4qcgaQsiC2)

* Il vous reste maintenant à inverser `""` – une chaîne vide.

![Image](https://lh5.googleusercontent.com/sGHYP70tsai5P6CQdiJk5u8qOLEXNzq0Ab5q8r3mmO5HFJslYCSii17tw3khyo2SQuDBhdlpq05FZ7kvO2AOj65QGJdV_YK9E2aqN6VHx7E1YHETR-phtSJeTUchquxLpd-bCfjO)

* C'est lorsque vous avez placé `"e"`, `"d"`, `"o"` et `"c"` dans les positions correctes, et vous n'avez plus à le faire. Dans le contexte de la récursivité, vous avez atteint le **cas de base**.

**Qu'avez-vous fait ici ?**

1. À chaque étape, vous avez effectué la même tâche de retirer la première lettre de chaque sous-chaîne suivante.
2. Et vous avez réduit le problème à l'inversion d'une chaîne qui est plus courte d'une lettre que précédemment.

**Quand vous êtes-vous arrêté ?**

Lorsque la chaîne était _vide_ – vous n'aviez plus de lettres à retirer.

L'illustration ci-dessous résume ce que nous avons fait :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-30.png)
_Intuition derrière l'inversion de chaîne (Image par l'auteur)_

Maintenant que vous avez compris comment fonctionne réellement l'inversion de chaîne en utilisant la récursivité, écrivons un peu de code.

### Comprendre la pile d'appels récursifs

Voici la fonction Python `reverseString()` qui fait exactement ce que vous avez appris dans la section précédente.

La fonction `reverseString()` prend `any_string` et retourne une copie inversée de `any_string`.

```python
def reverseString(any_string):
  if any_string == "":
    return any_string
  else:
    return reverseString(any_string[1:]) + any_string[:1]
```

Vous devrez comprendre comment les appels récursifs sont poussés sur la pile lorsque vous appelez la fonction `reverseString()`.

```python
reverseString("code")

# Sortie
'edoc'
```

* Supposons que vous appelez la fonction `reverseString()` avec `"code"` comme argument. Cela fait à son tour un appel à `reverseString()` avec `"ode"` comme argument.
* Et cet appel fait un appel à `reverseString()` encore une fois avec `"de"` comme argument.
* Cela continue jusqu'à ce qu'un appel soit finalement fait à `reverseString()` avec une chaîne vide `""` comme argument.

Pour chaque appel de fonction, un enregistrement d'activation est créé dans la section de pile de la mémoire de votre ordinateur.

Et l'enregistrement d'activation de chaque appel de fonction suivant est poussé au sommet de la pile.

Cela est expliqué dans l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-28.png)
_Pile d'appels (Image par l'auteur)_

* Vous savez que lorsque l'appel est fait avec `""`, la fonction retourne `""` concaténée avec `"e"` qui est simplement `"e"`. Et son enregistrement d'activation est retiré de la pile.
* L'appel suivant retourne `"ed"`, et le suivant retourne `"edo"`. Et l'enregistrement d'activation qui est retiré de la pile retourne finalement `"edoc"` qui est la chaîne inversée.

Notez que l'enregistrement d'activation correspondant à chacun des appels récursifs est retiré de la pile une fois les valeurs retournées – comme montré dans l'appel qui a retourné `"e"`.

Pour des raisons de lisibilité, j'ai omis le ❌ dans l'illustration ci-dessous. Et les valeurs de retour de l'appel précédent ont été indiquées en _vert_ à l'intérieur de la pile d'appels.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-29.png)
_Valeurs de retour des appels récursifs (Image par l'auteur)_

Vous pouvez maintenant appeler `reverseString()` avec n'importe quelle chaîne Python valide. Voici quelques exemples supplémentaires.

```python
reverseString("Python")
```

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-17.png)

```python
reverseString("Python Reverse String")
```

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-16.png)

Eh bien, cela a demandé pas mal d'efforts. 😓 Mais j'espère que vous êtes maintenant capable de mieux comprendre les appels récursifs. 😊

Dans les deux sections suivantes, vous verrez des méthodes plus faciles pour inverser des chaînes. C'est parti. ✅

## Comment inverser des chaînes en Python en utilisant le slicing de chaînes

Vous pouvez également inverser des chaînes en Python en utilisant le **slicing de chaînes**. Et vous pouvez slicer des chaînes Python de la même manière que vous sliceriez des listes Python.

### Explication du slicing de chaînes Python

`<string>[start: stop: step]` retourne une tranche de la chaîne – commençant à l'index `start`, s'étendant jusqu'à `stop - 1`, par pas de `step`.

Voici quelques points sur les chaînes à rappeler :

* `<string>` est n'importe quelle chaîne Python valide.
* L'index `start` est _optionnel_. Si vous ne le spécifiez pas, par _défaut_, la tranche commence au début de `<string>` (à l'index `0`).
* L'index `stop` est également _optionnel_. Si vous ne le spécifiez pas, par _défaut_, la tranche s'étend jusqu'à la fin de `<string>`.
* L'argument _optionnel_ `step` donne le contexte sur la manière dont vous souhaitez slicer `<string>`.
* Définissons `step = 2`. Maintenant, la tranche commencerait à partir de `start` et irait jusqu'à `stop - 1`, en incluant chaque deuxième caractère de la chaîne.

En mettant tout ensemble, `<string>[:::]` retourne une copie de la chaîne entière.

Pouvez-vous voir pourquoi cela est correct ?🤔

Sans l'index `start`, la tranche commence à l'index `0`.

Sans l'index `end`, la tranche s'étend jusqu'au dernier caractère de la chaîne.

Sans l'argument `step`, la tranche inclut tous les caractères de la chaîne.

* Vous pouvez également définir des valeurs **négatives** pour `step`. Et les valeurs négatives retourneront des tranches de chaîne commençant à partir de la **fin** de la chaîne.
* Définissez `step = -1` : Cela retourne une tranche de la chaîne commençant **par** le **dernier** caractère, s'étendant **jusqu'au** **premier** caractère. Et cela inclut également chaque caractère.

Attendez, n'est-ce pas exactement la chaîne inversée ? 🤔 Oui, c'est le cas.

Donc `<string>[::-1]` retourne une copie inversée de la chaîne. ✅

```python
any_string = "Python"

rev_string = any_string[::-1]

print(rev_string)

# Sortie
nohtyP
```

Passez à la section suivante pour apprendre une autre façon d'inverser des chaînes.

## Comment inverser des chaînes en Python en utilisant les méthodes `reversed()` et `join()`

Commençons par examiner ce que fait la méthode `reversed()` de Python.

> La fonction intégrée `reversed()` de Python retourne un itérateur inversé sur les valeurs d'une séquence donnée.

```python
any_string = "Python"
```

Étant donné une chaîne comme `any_string`, vous pouvez utiliser la méthode `reversed()` pour obtenir les caractères dans l'ordre inversé.

Cela est montré ci-dessous :

```python
for char in reversed(any_string):
  print(char)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-13.png)

Maintenant que vous avez tous vos caractères dans l'ordre inversé, vous devez les rassembler dans une chaîne.

Et la méthode `join()` de Python vous permet de faire exactement cela.

`<sep>.join(<these>)` joint `<these>` dans une chaîne avec `<sep>` comme séparateur.

* Ici, `<these>` sont les caractères dans l'ordre inversé.
* Mais que devrait être `<sep>` ? Eh bien, vous n'avez besoin d'aucun séparateur – vous voulez simplement que tous les caractères aillent dans la chaîne aux bons indices.
* Alors, que devriez-vous faire ? Il suffit d'insérer un `""` dans le champ `<sep>`, comme montré :

```python
"".join(reversed(any_string))

```

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-19.png)

Faites simplement attention à **ne pas** insérer d'espace entre les guillemets ouvrants et fermants `"`.

Si vous faites ce qui suit :

```python
" ".join(reversed(any_string))

```

Vous obtiendrez une chaîne où les caractères sont séparés par un espace, et ce n'est pas ce que vous voulez.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-18.png)

Dans cette section, vous avez appris une autre méthode Pythonique pour inverser des chaînes en Python.

## Conclusion

Félicitations pour être arrivé jusqu'ici ! 🎉

Pour résumer, vous avez appris :

* comment inverser récursivement une chaîne – continuez jusqu'à ce que vous ayez une **chaîne vide** ou qu'il ne reste qu'un **seul caractère** (cela fonctionnerait aussi bien, car un caractère inversé est lui-même),
* comment utiliser `<string>[::-1]` pour obtenir une copie inversée de `<string>`, et
* comment utiliser `"".join(reversed(<string>))` pour obtenir une copie inversée de `<string>`.

J'espère que vous avez trouvé ce tutoriel utile et intéressant. Bon codage ! 😄