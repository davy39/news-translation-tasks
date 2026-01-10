---
title: Pourquoi vous devriez expérimenter avec la vérification de type en Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-06T20:43:27.000Z'
originalURL: https://freecodecamp.org/news/the-incredible-hulk-ython-making-python-strong-ly-typed-adc1b6ccf686
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Awcmdb1xwSKXM7aID2TP1A.png
tags:
- name: coding
  slug: coding
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: Pourquoi vous devriez expérimenter avec la vérification de type en Python
seo_desc: 'By Periklis Gkolias

  Python is a wonderful dynamically typed language. But quite a few people consider
  this its biggest disadvantage.

  But why?

  Dynamically typed languages remove the headache of writing “mundane” type declarations.
  This makes writing m...'
---

Par Periklis Gkolias

Python est un langage merveilleux à [typage dynamique](https://stackoverflow.com/questions/1517582/what-is-the-difference-between-statically-typed-and-dynamically-typed-languages). Mais beaucoup de gens considèrent cela comme son plus grand inconvénient.

### Mais pourquoi ?

Les langages à typage dynamique éliminent le casse-tête d'écrire des déclarations de type "mundanes". Cela rend l'écriture plus agréable et un peu plus rapide. L'environnement d'exécution du langage gère le typage dynamique.

Cela signifie que certains bugs qui auraient pu être éliminés presque immédiatement après leur introduction resteront silencieux jusqu'à ce que le code soit invoqué. Et vous savez quand cela va se produire, n'est-ce pas ?

![Image](https://cdn-media-1.freecodecamp.org/images/UaDW4hJ1lDelQm2C0Qish4GrS1fhZPaZ2LWd)

### Travailler avec les types

Python a ajouté, à partir de la version 3.5, un support **optionnel** pour les indications de type via le module [typing](https://docs.python.org/3/library/typing.html).

Il semble qu'ils cherchent à faire un compromis pour les deux côtés. D'un côté, les personnes qui aiment la liberté du typage dynamique peuvent continuer à ignorer les indications de type. De l'autre côté, les personnes qui aiment la sécurité du typage statique peuvent bénéficier de la nouvelle fonctionnalité.

### Comment l'utiliser

La façon de l'utiliser, ou au moins de commencer à l'utiliser, est assez simple et directe. Cela ressemble beaucoup à la manière de TypeScript pour le [typage statique](https://www.typescriptlang.org/docs/handbook/basic-types.html) si vous êtes familier. Voici un exemple :

```py
# Typing est le module principal qui supporte la vérification de type.
# Ici, nous importons List, qui fournit une fonctionnalité équivalente à
# la fonction list() ou le raccourci équivalent []
from typing import List
# Nous définissons une fonction, comme d'habitude, mais nous ajoutons le type attendu
# aux arguments et nous ajoutons également un type de retour
def find_files_of_type(type: str, files_types: List[str]) -> bool:
    return (type in files_types)

files_types: List[str] = ['ppt', 'vcf', 'png']
type_to_search: str = 'ppt'
print('Found files of type {} in list? {}'.format(type_to_search,
    find_files_of_type(type_to_search, files_types)))
```

Un peu maladroit, mais toujours clair, n'est-ce pas ? :)

### Le piège potentiel

Vous avez peut-être remarqué que j'ai mentionné le mot "optionnel" quelques lignes plus haut. Donc, au moment de la rédaction de cet article, il n'y a pas d'application de la vérification de type.

Vous pouvez ajouter n'importe quel type non pertinent à vos variables. Faites les opérations les plus invalides, non pertinentes et "perverties" sur elles, mais Python ne bronche pas.

Si vous voulez **appliquer** la vérification de type, vous devriez utiliser un vérificateur de type comme le formidable [mypy](http://mypy-lang.org/examples.html).

Bien sûr, la plupart des IDE ont une certaine fonctionnalité pour la vérification de type. [Voici](https://www.jetbrains.com/help/pycharm/type-hinting-in-product.html) la documentation pertinente pour Pycharm.

### Ce que j'aimerais voir à l'avenir

* Intégrer un mécanisme de vérification de type dans le cœur du langage
* En résultat de ce qui précède, des indications de type plus transparentes. Par exemple, si la vérification de type est activée, je ne devrais pas avoir à utiliser la classe `List` ou `Tuple` pour le faire. Les raccourcis `[]` et `()` devraient suffire

### Conclusion

Merci d'avoir lu cet article. Ce n'est en aucun cas un guide étendu sur cette grande fonctionnalité de Python. C'est plutôt une introduction que j'espère mènera à plus de recherches.

Si vous commencez un nouveau projet en Python 3.5+, je vous recommande d'expérimenter avec la vérification de type. J'aimerais voir vos suggestions et vos réflexions sur cette fonctionnalité, alors n'hésitez pas à laisser un commentaire.

Publié à l'origine sur [mon blog](http://perigk.github.io).