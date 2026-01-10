---
title: Instruction Switch en Python – Exemple de Switch Case
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-08-05T15:27:56.000Z'
originalURL: https://freecodecamp.org/news/python-switch-statement-switch-case-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/switchCase.png
tags:
- name: Python
  slug: python
seo_title: Instruction Switch en Python – Exemple de Switch Case
seo_desc: 'Until version 3.10, Python never had a feature that implemented what the
  switch statement does in other programming languages.

  So, if you wanted to execute multiple conditional statements, you would''ve had
  to use the elif keyword like this:

  age = 120...'
---

Jusqu'à la version 3.10, Python n'avait jamais eu de fonctionnalité implémentant ce que fait l'instruction switch dans d'autres langages de programmation.

Ainsi, si vous souhaitiez exécuter plusieurs instructions conditionnelles, vous auriez dû utiliser le mot-clé `elif` comme ceci :

```python
age = 120

if age > 90:
    print("Vous êtes trop vieux pour faire la fête, mamie.")
elif age < 0:
    print("Vous n'êtes pas encore né")
elif age >= 18:
    print("Vous êtes autorisé à faire la fête")
else: 
    "Vous êtes trop jeune pour faire la fête"

# Sortie : Vous êtes trop vieux pour faire la fête, mamie.
```

À partir de la version 3.10, Python a implémenté une fonctionnalité de switch case appelée « structural pattern matching ». Vous pouvez implémenter cette fonctionnalité avec les mots-clés `match` et `case`.

Certaines personnes débattent pour savoir si `match` et `case` sont des mots-clés en Python. Cela est dû au fait que vous pouvez utiliser les deux comme noms de variables et de fonctions. Mais c'est une autre histoire pour un autre jour.

Vous pouvez vous référer à ces deux mots-clés comme des « soft keywords » si vous le souhaitez.

Dans cet article, je vais vous montrer comment écrire une instruction switch en Python en utilisant les mots-clés `match` et `case`.

Mais avant cela, je dois vous montrer comment les programmeurs Python simulaient une instruction switch à l'époque.

## Comment les programmeurs Python simulaient le Switch Case

Il existait plusieurs façons pour les Pythonistas de simuler des instructions switch à l'époque.

Utiliser une fonction et le mot-clé `elif` en était une, et vous pouvez le faire de cette manière :

```python
def switch(lang):
    if lang == "JavaScript":
        return "Vous pouvez devenir un développeur web."
    elif lang == "PHP":
        return "Vous pouvez devenir un développeur backend."
    elif lang == "Python":
        return "Vous pouvez devenir un Data Scientist"
    elif lang == "Solidity":
        return "Vous pouvez devenir un développeur Blockchain."
    elif lang == "Java":
        return "Vous pouvez devenir un développeur d'applications mobiles"

print(switch("JavaScript"))   
print(switch("PHP"))   
print(switch("Java"))  

"""
Sortie :
Vous pouvez devenir un développeur web.
Vous pouvez devenir un développeur backend.
Vous pouvez devenir un développeur d'applications mobiles
"""
```  

## Comment implémenter les instructions Switch avec les mots-clés `match` et `case` dans Python 3.10

Pour écrire des instructions switch avec la fonctionnalité de structural pattern matching, vous pouvez utiliser la syntaxe suivante :

```python
match term:
    case pattern-1:
         action-1
    case pattern-2:
         action-2
    case pattern-3:
         action-3
    case _:
        action-default
```

Notez que le symbole de soulignement est ce que vous utilisez pour définir un cas par défaut pour l'instruction switch en Python.

Un exemple d'instruction switch écrite avec la syntaxe match case est montré ci-dessous. Il s'agit d'un programme qui imprime ce que vous pouvez devenir lorsque vous apprenez divers langages de programmation :

```python
lang = input("Quel est le langage de programmation que vous voulez apprendre ? ")

match lang:
    case "JavaScript":
        print("Vous pouvez devenir un développeur web.")

    case "Python":
        print("Vous pouvez devenir un Data Scientist")

    case "PHP":
        print("Vous pouvez devenir un développeur backend")
    
    case "Solidity":
        print("Vous pouvez devenir un développeur Blockchain")

    case "Java":
        print("Vous pouvez devenir un développeur d'applications mobiles")
    case _:
        print("Le langage n'a pas d'importance, ce qui compte, c'est de résoudre des problèmes.")
```

C'est une syntaxe beaucoup plus propre que plusieurs instructions `elif` et la simulation de l'instruction switch avec une fonction.

Vous avez probablement remarqué que je n'ai pas ajouté de mot-clé break à chacun des cas, comme c'est fait dans d'autres langages de programmation. C'est l'avantage que l'instruction switch native de Python a sur celles des autres langages. La fonctionnalité du mot-clé break est faite pour vous en arrière-plan.


## Conclusion

Cet article vous a montré comment écrire des instructions switch avec les mots-clés « match » et « case ». Vous avez également appris comment les programmeurs Python l'écrivaient avant la version 3.10.

Les instructions match et case de Python ont été implémentées pour fournir la fonctionnalité que l'instruction switch dans d'autres langages de programmation tels que JavaScript, PHP, C++, et autres nous offrent.

Merci d'avoir lu.