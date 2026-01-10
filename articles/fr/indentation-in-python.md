---
title: Indentation en Python avec des exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-14T21:46:00.000Z'
originalURL: https://freecodecamp.org/news/indentation-in-python
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ddf740569d1a4ca3a21.jpg
tags:
- name: Python
  slug: python
- name: syntax
  slug: syntax
seo_title: Indentation en Python avec des exemples
seo_desc: It is generally good practice for you not to mix tabs and spaces when coding
  in Python. Doing this can possibly cause a TabError, and your program will crash.
  Be consistent when you code - choose either to indent using tabs or spaces and follow
  your ...
---

Il est généralement bon de ne pas mélanger les tabulations et les espaces lors de la programmation en Python. Cela peut éventuellement causer une `TabError`, et votre programme plantera. Soyez cohérent lorsque vous codez - choisissez soit d'indenter en utilisant des tabulations ou des espaces et suivez votre convention choisie tout au long de votre programme.

### Blocs de code et indentation

L'une des caractéristiques les plus distinctives de Python est son utilisation de l'indentation pour marquer les blocs de code. Considérez l'instruction if de notre programme simple de vérification de mot de passe :

```python
if pwd == 'apple':
    print('Connexion en cours ...')
else:
    print('Mot de passe incorrect.')

print('Tout est terminé !')
```

Les lignes print('Connexion en cours ...') et print('Mot de passe incorrect.') sont deux blocs de code distincts. Ceux-ci se trouvent être d'une seule ligne, mais Python vous permet d'écrire des blocs de code composés de n'importe quel nombre d'instructions.

Pour indiquer un bloc de code en Python, vous devez indenter chaque ligne du bloc du même montant. Les deux blocs de code dans notre exemple d'instruction if sont tous deux indentés de quatre espaces, ce qui est une quantité typique d'indentation pour Python.

Dans la plupart des autres langages de programmation, l'indentation est utilisée uniquement pour aider à rendre le code plus joli. Mais en Python, elle est requise pour indiquer à quel bloc de code une instruction appartient. Par exemple, le dernier print('Tout est terminé !') n'est pas indenté, et ne fait donc pas partie du bloc else.

Les programmeurs familiers avec d'autres langages s'irritent souvent à l'idée que l'indentation compte : de nombreux programmeurs aiment la liberté de formater leur code comme ils le souhaitent. Cependant, les règles d'indentation de Python sont assez simples, et la plupart des programmeurs utilisent déjà l'indentation pour rendre leur code lisible. Python va simplement plus loin et donne un sens à l'indentation.

### Instructions if/elif

Une instruction if/elif est une instruction if généralisée avec plus d'une condition. Elle est utilisée pour prendre des décisions complexes. Par exemple, supposons qu'une compagnie aérienne ait les tarifs de billets "enfant" suivants : les enfants de 2 ans ou moins volent gratuitement, les enfants de plus de 2 ans mais de moins de 13 ans paient un tarif enfant réduit, et toute personne âgée de 13 ans ou plus paie un tarif adulte régulier. Le programme suivant détermine combien un passager doit payer :

```python
# airfare.py
age = int(input('Quel âge avez-vous ? '))
if age <= 2:
    print(' gratuit')
elif 2 < age < 13:
    print(' tarif enfant')
else:
    print('tarif adulte')
```

Après que Python ait obtenu l'âge de l'utilisateur, il entre dans l'instruction if/elif et vérifie chaque condition l'une après l'autre dans l'ordre où elles sont données. Ainsi, il vérifie d'abord si l'âge est inférieur à 2, et si c'est le cas, il indique que le vol est gratuit et sort de la condition elif. Si l'âge n'est pas inférieur à 2, il vérifie alors la condition elif suivante pour voir si l'âge est compris entre 2 et 13. Si c'est le cas, il imprime le message approprié et sort de l'instruction if/elif. Si ni la condition if ni la condition elif n'est vraie, il exécute alors le code dans le bloc else.

### Expressions conditionnelles

Python a un autre opérateur logique que certains programmeurs aiment (et d'autres non !). C'est essentiellement une notation abrégée pour les instructions if qui peut être utilisée directement dans les expressions. Considérez ce code :

```python
food = input("Quel est votre plat préféré ? ")
reply = 'beurk' if food == 'lamb' else 'miam'
```

L'expression du côté droit de = dans la deuxième ligne est appelée une expression conditionnelle, et elle évalue soit 'beurk' soit 'miam'. Elle est équivalente à ce qui suit :

```python
food = input("Quel est votre plat préféré ? ")
if food == 'lamb':
   reply = 'beurk'
else:
   reply = 'miam'
```

Les expressions conditionnelles sont généralement plus courtes que les instructions if/else correspondantes, bien qu'elles ne soient pas aussi flexibles ou faciles à lire. En général, vous devriez les utiliser lorsqu'elles rendent votre code plus simple.

[Documentation Python - Indentation](https://docs.python.org/3/reference/lexical_analysis.html#indentation)