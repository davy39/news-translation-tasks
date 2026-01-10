---
title: Expressions Lambda en Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-04T23:41:00.000Z'
originalURL: https://freecodecamp.org/news/lambda-expressions-in-python
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e32740569d1a4ca3bd6.jpg
tags:
- name: Lambda Expressions
  slug: lambda-expressions
- name: Python
  slug: python
seo_title: Expressions Lambda en Python
seo_desc: 'Lambda Expressions

  Lambda Expressions are ideally used when we need to do something simple and are
  more interested in getting the job done quickly rather than formally naming the
  function. Lambda expressions are also known as anonymous functions.

  Lam...'
---

## **Expressions Lambda**

Les expressions Lambda sont idéalement utilisées lorsque nous devons faire quelque chose de simple et que nous sommes plus intéressés à accomplir la tâche rapidement plutôt qu'à nommer formellement la fonction. Les expressions Lambda sont également connues sous le nom de fonctions anonymes.

Les expressions Lambda en Python sont un moyen court de déclarer de petites fonctions anonymes (il n'est pas nécessaire de fournir un nom pour les fonctions lambda).

Les fonctions Lambda se comportent exactement comme les fonctions régulières déclarées avec le mot-clé `def`. Elles sont pratiques lorsque vous voulez définir une petite fonction de manière concise. Elles ne peuvent contenir qu'une seule expression, donc elles ne sont pas les mieux adaptées pour les fonctions avec des instructions de contrôle de flux.

### Syntaxe d'une fonction Lambda

`lambda arguments: expression`

Les fonctions Lambda peuvent avoir n'importe quel nombre d'arguments mais seulement une expression.

### Exemple de code

```py
# Fonction Lambda pour calculer le carré d'un nombre
square = lambda x: x ** 2
print(square(3)) # Sortie: 9

# Fonction traditionnelle pour calculer le carré d'un nombre
def square1(num):
  return num ** 2
print(square(5)) # Sortie: 25
```

Dans l'exemple lambda ci-dessus, `lambda x: x ** 2` produit un objet de fonction anonyme qui peut être associé à n'importe quel nom. Donc, nous avons associé l'objet de fonction à `square`. Désormais, nous pouvons appeler l'objet `square` comme n'importe quelle fonction traditionnelle, par exemple `square(10)`

## **Exemples de fonctions lambda**

### **Débutant**

```py
lambda_func = lambda x: x**2 # Fonction qui prend un entier et retourne son carré
lambda_func(3) # Retourne 9
```

### **Intermédiaire**

```py
lambda_func = lambda x: True if x**2 >= 10 else False
lambda_func(3) # Retourne False
lambda_func(4) # Retourne True
```

### **Complexe**

```py
my_dict = {"A": 1, "B": 2, "C": 3}
sorted(my_dict, key=lambda x: my_dict[x]%3) # Retourne ['C', 'A', 'B']
```

## Cas d'utilisation

Supposons que vous souhaitiez filtrer les nombres impairs d'une `liste`. Vous pourriez utiliser une boucle `for`:

```python
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered = []

for num in my_list:
     if num % 2 != 0:
         filtered.append(num)

print(filtered)      # Python 2: print filtered
# [1, 3, 5, 7, 9]
```

Ou vous pourriez écrire cela en une ligne avec des compréhensions de liste:

```python
filtered = [x for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] if x % 2 != 0]
```

Mais vous pourriez être tenté d'utiliser la fonction intégrée `filter`. Pourquoi ? Le premier exemple est un peu trop verbeux et la version en une ligne peut être plus difficile à comprendre. Mais `filter` offre le meilleur des deux mondes. De plus, les fonctions intégrées sont généralement plus rapides.

```python
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtered = filter(lambda x: x % 2 != 0, my_list)

list(filtered)
# [1, 3, 5, 7, 9]
```

NOTE : dans Python 3, les fonctions intégrées retournent des objets générateurs, donc vous devez appeler `list`. Dans Python 2, en revanche, elles retournent une `liste`, un `tuple` ou une `chaîne`.

Donc, que s'est-il passé ? Vous avez dit à `filter` de prendre chaque élément dans `my_list` et d'appliquer les expressions lambda. Les valeurs qui retournent `False` sont filtrées.

#### **Plus d'informations :**

* [Documentation officielle](https://docs.python.org/3/reference/expressions.html#lambda)