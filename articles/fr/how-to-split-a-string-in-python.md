---
title: Python .split() – Diviser une chaîne de caractères en Python
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-09-08T17:22:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-split-a-string-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/pexels-lukas-952354.jpg
tags:
- name: Python
  slug: python
seo_title: Python .split() – Diviser une chaîne de caractères en Python
seo_desc: 'In this article, you will learn how to split a string in Python.

  Firstly, I''ll introduce you to the syntax of the .split() method. After that, you
  will see how to use the .split() method with and without arguments, using code examples
  along the way.

  ...'
---

Dans cet article, vous apprendrez à diviser une chaîne de caractères en Python.

Tout d'abord, je vous présenterai la syntaxe de la méthode `.split()`. Ensuite, vous verrez comment utiliser la méthode `.split()` avec et sans arguments, avec des exemples de code tout au long.

Voici ce que nous allons couvrir :

1. [Syntaxe de la méthode `.split()`](#syntaxe)
	1. [Comment fonctionne la méthode `.split()` sans aucun argument ?](#sans-arguments)
	2. [Comment fonctionne la méthode `.split()` avec l'argument `separator` ?](#separateur)
	3. [Comment fonctionne la méthode `.split()` avec l'argument `maxsplit` ?](#maxsplit)


## Qu'est-ce que la méthode `.split()` en Python ? Analyse de la syntaxe de la méthode `.split()` <a name="syntaxe"></a>

Vous utilisez la méthode `.split()` pour diviser une chaîne de caractères en une liste.

La syntaxe générale de la méthode `.split()` ressemble à ceci :

```python
string.split(separator, maxsplit)
```

Décomposons cela :

- `string` est la chaîne de caractères que vous souhaitez diviser. C'est la chaîne sur laquelle vous appelez la méthode `.split()`.
- La méthode `.split()` accepte deux arguments.
- Le premier argument *optionnel* est `separator`, qui spécifie quel type de séparateur utiliser pour diviser la chaîne. Si cet argument n'est pas fourni, la valeur par défaut est tout espace blanc, ce qui signifie que la chaîne sera divisée chaque fois que `.split()` rencontre un espace blanc.
- Le deuxième argument *optionnel* est `maxsplit`, qui spécifie le nombre maximum de divisions que la méthode `.split()` doit effectuer. Si cet argument n'est pas fourni, la valeur par défaut est `-1`, ce qui signifie qu'il n'y a pas de limite au nombre de divisions, et `.split()` doit diviser la chaîne à chaque occurrence de `separator`.

La méthode `.split()` retourne une nouvelle liste de sous-chaînes, et la chaîne d'origine n'est pas modifiée.


### Comment fonctionne la méthode `.split()` sans aucun argument ? <a name="sans-arguments"></a>

Voici comment diviser une chaîne de caractères en une liste en utilisant la méthode `.split()` sans aucun argument :

```python
coding_journey = "J'apprends à coder gratuitement avec freeCodecamp !"

# diviser la chaîne en une liste et enregistrer le résultat dans une nouvelle variable
coding_journey_split = coding_journey.split()

print(coding_journey)
print(coding_journey_split)

# vérifier le type de données de coding_journey_split en utilisant la fonction type()
print(type(coding_journey_split))

# sortie
# J'apprends à coder gratuitement avec freeCodecamp !
# ['J'apprends', 'à', 'coder', 'gratuitement', 'avec', 'freeCodecamp!']
# <class 'list'>

```

La sortie montre que chaque mot qui compose la chaîne est maintenant un élément de liste, et la chaîne d'origine est préservée.

Lorsque vous ne passez aucun des deux arguments que la méthode `.split()` accepte, alors par défaut, elle divise la chaîne chaque fois qu'elle rencontre un espace blanc jusqu'à ce que la chaîne arrive à sa fin.

Que se passe-t-il lorsque vous ne passez aucun argument à la méthode `.split()`, et qu'elle rencontre des espaces blancs consécutifs au lieu d'un seul ?

```python
coding_journey = "J'adore   coder"

coding_journey_split = coding_journey.split()

print(coding_journey_split)

# sortie
# ['J'adore', 'coder']
```

Dans l'exemple ci-dessus, j'ai ajouté des espaces blancs consécutifs entre le mot `adore` et le mot `coder`. Dans ce cas, la méthode `.split()` traite tous les espaces consécutifs comme s'ils étaient un seul espace.


### Comment fonctionne la méthode `.split()` avec l'argument `separator` ? <a name="separateur"></a>

Comme vous l'avez vu précédemment, lorsqu'il n'y a pas d'argument `separator`, la valeur par défaut est un espace blanc. Cela dit, vous pouvez définir un `separator` différent.

Le `separator` divisera la chaîne chaque fois qu'il rencontrera le caractère que vous spécifiez et retournera une liste de sous-chaînes.

Par exemple, vous pourriez faire en sorte qu'une chaîne se divise chaque fois que la méthode `.split()` rencontre un point, `.` :

```python
fave_website = "www.freecodecamp.org"

fave_website_split = fave_website.split(".")

print(fave_website_split)

# sortie
# ['www', 'freecodecamp', 'org']
```

Dans l'exemple ci-dessus, la chaîne se divise chaque fois que `.split()` rencontre un `.`.

Gardez à l'esprit que je n'ai pas spécifié un point suivi d'un espace. Cela ne fonctionnerait pas puisque la chaîne ne contient pas un point suivi d'un espace :

```python
fave_website = "www.freecodecamp.org"

fave_website_split = fave_website.split(". ")

print(fave_website_split)

# sortie
# ['www.freecodecamp.org']
```

Maintenant, revisitons le dernier exemple de la section précédente.

Lorsque l'argument `separator` n'était pas spécifié, les espaces blancs consécutifs étaient traités comme s'ils étaient un seul espace.

Cependant, lorsque vous spécifiez un seul espace comme `separator`, alors la chaîne se divise chaque fois qu'elle rencontre un seul caractère d'espace :

```python
coding_journey = "J'adore   coder"

coding_journey_split = coding_journey.split(" ")

print(coding_journey_split)

# sortie
# ['J'adore', '', '', 'coder']
```

Dans l'exemple ci-dessus, chaque fois que `.split()` rencontrait un caractère d'espace, il divisait le mot et ajoutait l'espace vide comme un élément de liste.

### Comment fonctionne la méthode `.split()` avec l'argument `maxsplit` ? <a name="maxsplit"></a>

Lorsque l'argument `maxsplit` n'est pas spécifié, il n'y a pas de limite définie pour l'arrêt des divisions.

Dans le premier exemple de la section précédente, `.split()` a divisé la chaîne chaque fois qu'il rencontrait le `separator` jusqu'à ce qu'il atteigne la fin de la chaîne.

Cependant, vous pouvez spécifier quand vous souhaitez que la division s'arrête.

Par exemple, vous pourriez spécifier que la division s'arrête après avoir rencontré un point :

```python
fave_website = "www.freecodecamp.org"

fave_website_split = fave_website.split(".", 1)

print(fave_website_split)

# sortie
# ['www', 'freecodecamp.org']
```

Dans l'exemple ci-dessus, j'ai défini `maxsplit` à `1`, et une liste a été créée avec deux éléments.

J'ai spécifié que la liste devait se diviser lorsqu'elle rencontrait un point. Une fois qu'elle a rencontré un point, l'opération s'est arrêtée, et le reste de la chaîne est devenu un élément de liste à part entière.

## Conclusion

Et voilà ! Vous savez maintenant comment diviser une chaîne de caractères en Python en utilisant la méthode `.split()`.

J'espère que vous avez trouvé ce tutoriel utile.

Pour en savoir plus sur le langage de programmation Python, consultez la [certification Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/) de freeCodeCamp.

Vous commencerez par les bases et apprendrez de manière interactive et adaptée aux débutants. Vous construirez également cinq projets à la fin pour mettre en pratique et renforcer ce que vous avez appris.

Merci d'avoir lu, et bon codage !