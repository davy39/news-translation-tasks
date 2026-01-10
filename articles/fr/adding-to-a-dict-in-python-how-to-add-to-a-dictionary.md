---
title: Ajouter à un Dict en Python – Comment ajouter à un dictionnaire
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-12-22T18:04:49.000Z'
originalURL: https://freecodecamp.org/news/adding-to-a-dict-in-python-how-to-add-to-a-dictionary
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/addToDict.png
tags:
- name: dictionary
  slug: dictionary
- name: Python
  slug: python
seo_title: Ajouter à un Dict en Python – Comment ajouter à un dictionnaire
seo_desc: "A Python dictionary is like a JavaScript object – it’s a sequence of key:value\
  \ pairs. So, you can create them like this:\nstack_dict = {\n    \"frontend\": \"\
  JavaScript\",\n    \"backend\": \"Node JS\",\n    \"markup\": \"HTML and JSX\",\n\
  }\n\nTo access the value in th..."
---

Un dictionnaire Python est comme un objet JavaScript – c'est une séquence de paires `clé:valeur`. Vous pouvez donc les créer comme ceci :

```py
stack_dict = {
    "frontend": "JavaScript",
    "backend": "Node JS",
    "markup": "HTML et JSX",
}
```

Pour accéder à la valeur dans le dictionnaire, vous pouvez le faire de cette manière : `dict[clé]`. Par exemple, si je veux accéder à ce que la clé `frontend` contient, je peux le faire comme ceci :

```py
print(stack_dict["frontend"])
# JavaScript
```

Mais que faire si vous souhaitez ajouter une autre entrée au dictionnaire sans revenir au dictionnaire pour la mettre là ? C'est ce que nous allons examiner dans cet article. Et je vais vous montrer comment le faire de 3 manières différentes.

## Ce que nous allons couvrir
- [Comment ajouter à un dictionnaire en Python](#heading-comment-ajouter-a-un-dictionnaire-en-python)
- [Comment ajouter à un dictionnaire en mappant une clé au dictionnaire](#commentajouteraundictionnaireenmappantunecleaudictionnaire)
- [Comment ajouter à un dictionnaire en utilisant la méthode `update()`](#commentajouteraundictionnaireenutilisantlamethodeupdate)
- [Comment ajouter à un dictionnaire en utilisant l'instruction `if`](#commentajouteraundictionnaireenutilisantlinstructionif)
- [Conclusion](#heading-conclusion)


## Comment ajouter à un dictionnaire en Python
Vous pouvez ajouter à un dictionnaire de trois manières différentes :
- mapper une clé au dictionnaire 
- utiliser la méthode `update()`
- utiliser une instruction if

### Comment ajouter à un dictionnaire en Python en mappant une clé au dictionnaire
Si vous souhaitez ajouter à un dictionnaire avec cette méthode, vous devrez ajouter la valeur avec l'opérateur d'affectation.

```py
dict["clé"] = "valeur"`
```

Cela écraserait également la valeur d'une clé existante.

Dans le dictionnaire stack que j'ai défini précédemment, il n'y a pas de style là :

```py
stack_dict = {
    "frontend": "JavaScript",
    "backend": "Node JS",
    "markup": "HTML et JSX",
}
```

Alors ajoutons une clé `styling` et une valeur `CSS` au dictionnaire en mappant une nouvelle clé au dictionnaire :

```py
stack_dict["styling"] = "CSS"

print(stack_dict)
# Sortie : {'frontend': 'JavaScript', 'backend': 'Node JS', 'markup': 'HTML et JSX', 'styling': 'CSS'}
```

Vous pouvez voir qu'une nouvelle clé `styling` et une valeur `CSS` ont été ajoutées au dictionnaire.

Si la clé existe déjà, la valeur est écrasée :

```py
stack_dict["markup"] = "HTML seulement"
print(stack_dict)

# {'frontend': 'JavaScript', 'backend': 'Node JS', 'markup': 'HTML seulement'}
```

### Comment ajouter à un dictionnaire en Python en utilisant la méthode `update()`

La stack manque toujours une bibliothèque JavaScript, alors ajoutons-la avec la méthode `update()`. Vous pouvez le faire de cette manière :

```py
dict.update({"clé": "valeur"})`.
```

Donc, pour ajouter le framework/bibliothèque JavaScript, je l'ai fait comme ceci :

```py
stack_dict.update({"JS Framework": "React/Next"})

print(stack_dict)
# {'frontend': 'JavaScript', 'backend': 'Node JS', 'markup': 'HTML et JSX', 'styling': 'CSS', 'JS Framework': 'React/Next'}
```

La méthode `update()` écrase également une valeur existante si elle est différente :

```py
stack_dict.update({"backend": "Django"})

print(stack_dict)
# {'frontend': 'JavaScript', 'backend': 'Django', 'markup': 'HTML et JSX'}
```

### Comment ajouter à un dictionnaire en Python en utilisant l'instruction `if`

Si vous ne souhaitez pas qu'une entrée soit écrasée même si elle existe déjà, vous pouvez utiliser une instruction `if`. Vous pouvez le faire avec cette syntaxe :

```py
if "valeur" not it dict.keys():
    dict["clé"] = "valeur"
```

Je veux ajouter une clé "CSS Framework" avec une valeur "Tailwind CSS" au dictionnaire stack, alors je vais le faire avec l'aide de cette syntaxe :

```py
if "Tailwind CSS" not in stack_dict.keys():
    stack_dict["CSS Framework"] = "Tailwind CSS"

print(stack_dict)
# {'frontend': 'JavaScript', 'backend': 'Node JS', 'markup': 'HTML et JSX', 'styling': 'CSS', 'JS Framework': 'React/Next', 'CSS Framework': 'Tailwind CSS'}
```

Si l'entrée est déjà dans le dictionnaire, elle ne sera pas ajoutée :

```py
if "HTML et JSX" not in stack_dict.keys():
    stack_dict["markup"] = "HTML et JSX"

print(stack_dict)
# {'frontend': 'JavaScript', 'backend': 'Node JS', 'markup': 'HTML et JSX', 'styling': 'CSS', 'JS Framework': 'React/Next'}
```

Si vous n'avez pas envie d'utiliser une instruction `if` pour ajouter au dictionnaire, vous pouvez faire la même chose avec `try...except...` :

```py
try:
  stack_dict["Deployment"] = "Anywhere possible"
except:
  print("Une exception s'est produite")

print(stack_dict)
# {'frontend': 'JavaScript', 'backend': 'Node JS', 'markup': 'HTML et JSX', 'styling': 'CSS', 'JS Framework': 'React/Next', 'Deployment': 'Anywhere possible'}
```

## Conclusion
Cet article vous a montré trois manières différentes d'ajouter à un dictionnaire en Python :
- mapper une clé au dictionnaire 
- utiliser la méthode update()
- utiliser une instruction if 

Nous avons même examiné comment vous pouvez ajouter à un dictionnaire avec l'expression `try...except...`.

Merci d'avoir lu.