---
title: Imprimer un saut de ligne en Python – Affichage d'une nouvelle ligne
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-22T19:17:24.000Z'
originalURL: https://freecodecamp.org/news/print-newline-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Shittu-Olumide-Print-Newline-in-Python
seo_title: Imprimer un saut de ligne en Python – Affichage d'une nouvelle ligne
---

Printing-a-New-Line-1.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'Par Shittu Olumide

  Travailler avec des chaînes de caractères ou des données textuelles en programmation implique fréquemment l\'impression d\'un saut de ligne. La fin d\'une ligne est indiquée par un caractère de saut de ligne, qui fait également avancer le curseur au début de la ligne suivante. En utilisant le caractère d\'échappement \n...'
---

Par Shittu Olumide

Travailler avec des chaînes de caractères ou des données textuelles en programmation implique fréquemment l'impression d'un saut de ligne. La fin d'une ligne est indiquée par un caractère de saut de ligne, qui fait également avancer le curseur au début de la ligne suivante. En utilisant le caractère d'échappement `\n`, nous pouvons imprimer un saut de ligne en Python.

D'autres langages de programmation peuvent avoir des règles différentes pour l'impression des caractères de saut de ligne. Alors que certains langages peuvent avoir une fonction ou une méthode intégrée pour imprimer un saut de ligne, d'autres pourraient utiliser une séquence d'échappement différente.

Dans cet article, nous explorerons les différentes manières d'imprimer un saut de ligne en Python. Nous discuterons également de certains résultats de recherche intéressants sur l'utilisation des caractères de saut de ligne dans le code et son impact sur la lisibilité et la maintenabilité.

À la fin de cet article, vous aurez une meilleure compréhension de la façon d'imprimer un caractère de saut de ligne en Python et de la façon d'écrire du code facile à lire et à maintenir.

## Comment imprimer un saut de ligne en utilisant la séquence d'échappement `\n` 

La manière la plus simple et la plus courante d'imprimer un caractère de saut de ligne en Python est d'utiliser la séquence d'échappement `\n`. Par exemple, le code suivant imprimera deux lignes de texte, avec un caractère de saut de ligne entre elles :

```py
print("Hello\nWorld")

```

Sortie :

```bash
Hello
World

```

Bien que l'utilisation de la séquence d'échappement `\n` soit simple et largement comprise, elle n'est pas toujours le meilleur choix pour améliorer la lisibilité et la maintenabilité du code. En particulier, l'utilisation de plusieurs caractères `\n` peut rendre le code plus difficile à lire et à maintenir, surtout lorsqu'on traite de longs blocs de texte.

## Comment imprimer un saut de ligne en utilisant la fonction `print()` avec le paramètre End 

Une autre façon d'imprimer un caractère de saut de ligne en Python est d'utiliser la fonction `print()` avec le paramètre `end`.

Par défaut, la fonction `print()` ajoute un caractère de saut de ligne à la fin de la sortie. Mais nous pouvons changer ce comportement en spécifiant une chaîne différente à utiliser comme paramètre `end`.

Par exemple, le code suivant imprimera deux lignes de texte avec un caractère de saut de ligne entre elles, en utilisant la fonction `print()` :

```py
print("Hello", end='\n')
print("World")

```

Sortie :

```bash
Hello
World

```

La lisibilité du code peut être améliorée en utilisant la fonction `print()` avec le paramètre `end`, ce qui rend plus clair l'endroit où le caractère de saut de ligne est ajouté.

D'un autre côté, cela peut aussi rendre le code verbeux et plus difficile à lire, particulièrement lors du travail avec de longs blocs de texte.

## Comment imprimer un saut de ligne en utilisant la méthode `join()` avec la méthode `split()` 

Une manière plus avancée d'imprimer un caractère de saut de ligne en Python est d'utiliser la méthode `join()` avec la méthode `split()`.

La méthode `split()` est utilisée pour diviser une chaîne en une liste de sous-chaînes, sur la base d'un séparateur spécifié. La méthode `join()` est utilisée pour joindre les éléments d'une liste en une seule chaîne, en utilisant un séparateur spécifié.

En divisant une chaîne sur le caractère de saut de ligne, puis en la regroupant avec un séparateur de caractère de saut de ligne, nous pouvons imprimer plusieurs lignes de texte.

Par exemple, le code suivant imprimera deux lignes de texte avec un caractère de saut de ligne entre elles, en utilisant la méthode `join()` avec la méthode `split()` :

```py
text = "Hello\nWorld"
lines = text.split('\n')

print('\n'.join(lines))

```

Sortie :

```bash
Hello
World

```

En rendant le code plus clair et plus concis en combinant les méthodes `join()` et `split()`, cela améliore la lisibilité du code. Mais lors de l'impression de plusieurs lignes de texte, surtout lorsqu'on traite de longs blocs de texte, cela peut ne pas toujours être la méthode la plus efficace ou la plus performante.

## Comment l'utilisation des caractères de saut de ligne affecte-t-elle le code ?

Plusieurs études ont examiné l'impact des caractères de saut de ligne sur la lisibilité et la maintenabilité du code.

Une étude a révélé que le code avec des caractères de saut de ligne cohérents et prévisibles était plus facile à lire et à comprendre, en particulier pour les programmeurs novices. Une autre étude a révélé que l'utilisation excessive de caractères de saut de ligne, ou l'utilisation incohérente de l'indentation et des espaces, pouvait rendre le code plus difficile à lire et à comprendre.

Il est important d'utiliser les caractères de saut de ligne de manière cohérente et prévisible, en se basant sur les conventions et les directives du langage de programmation.

## Conclusion 

Dans cet article, nous avons examiné trois façons différentes d'imprimer un saut de ligne en Python, et avons également mentionné l'importance d'avoir un code bien formaté en utilisant le caractère de saut de ligne.

Connectons-nous sur [Twitter](https://www.twitter.com/Shittu_Olumide_) et sur [LinkedIn](https://www.linkedin.com/in/olumide-shittu). Vous pouvez également vous abonner à ma chaîne [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A).

Bon codage !