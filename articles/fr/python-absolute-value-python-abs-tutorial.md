---
title: Valeur Absolue en Python – Tutoriel sur Python abs
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-06-20T15:55:24.000Z'
originalURL: https://freecodecamp.org/news/python-absolute-value-python-abs-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/markus-krisetya-Vkp9wg-VAsQ-unsplash.jpg
tags:
- name: Math
  slug: math
- name: MathJax
  slug: mathjax
- name: Python
  slug: python
seo_title: Valeur Absolue en Python – Tutoriel sur Python abs
seo_desc: 'In this article, you will learn all about the abs() function in Python.

  You will learn what the abs() function does and why you may want to use it.

  You will also understand how to use abs() with the help of practical examples.

  Here is what we will co...'
---

Dans cet article, vous apprendrez tout sur la fonction `abs()` en Python.

Vous apprendrez ce que fait la fonction `abs()` et pourquoi vous pourriez vouloir l'utiliser.

Vous comprendrez également comment utiliser `abs()` à l'aide d'exemples pratiques.

Voici ce que nous allons couvrir :

1. [Qu'est-ce que la fonction `abs()` en Python ?](#intro)
    1. [Pourquoi les valeurs absolues sont-elles importantes ?](#valeurs-absolues)
    2. [Comment utiliser la fonction `abs()` en Python ? Une analyse de la syntaxe](#utilisation)
2. [Comment utiliser la fonction `abs()` avec des exemples](#exemples)
    1. [Comment utiliser la fonction `abs()` avec un argument entier](#entier)
    2. [Comment utiliser la fonction `abs()` avec un argument de nombre à virgule flottante](#virgule-flottante)
    3. [Comment utiliser la fonction `abs()` avec un argument de nombre complexe](#complexe)

## Qu'est-ce que la Fonction `abs()` en Python ? <a name="intro"></a>

La fonction intégrée `abs()` de Python retourne la valeur absolue d'un nombre.

Mais qu'est-ce qu'une valeur absolue d'un nombre en premier lieu ?

En mathématiques, la valeur absolue d'un nombre fait référence à la distance de ce nombre par rapport à zéro.

Essentiellement, c'est la distance de ce nombre par rapport à zéro sur la ligne des nombres.

Par exemple, la valeur absolue du nombre cinq est cinq puisque la distance de zéro à cinq est de cinq unités.

![Screenshot-2022-06-14-at-9.51.34-AM](https://www.freecodecamp.org/news/content/images/2022/06/Screenshot-2022-06-14-at-9.51.34-AM.png)

Une chose à noter est que la valeur absolue sera toujours une **valeur positive**. Donc, lorsqu'il s'agit de calculer la valeur absolue d'un nombre négatif, le résultat sera toujours la version positive de ce nombre.

Par exemple, la valeur absolue de moins cinq est également cinq :

![Screenshot-2022-06-14-at-10.01.18-AM](https://www.freecodecamp.org/news/content/images/2022/06/Screenshot-2022-06-14-at-10.01.18-AM.png)

### Pourquoi les Valeurs Absolues sont-elles Importantes ? <a name="valeurs-absolues"></a>

Les valeurs absolues sont un concept important et sont couramment utilisées en mathématiques et en physique.

Il peut y avoir des moments où vous n'aurez besoin d'utiliser que des nombres positifs et n'aurez pas besoin d'utiliser des nombres négatifs. En fait, vous devrez peut-être vous assurer qu'il n'y a aucun nombre négatif pour les calculs que vous allez effectuer.

Vous utiliserez probablement des valeurs absolues pour calculer la distance d'un point à un autre.

Quelques autres exemples courants dans le monde réel pourraient être :

- Calculer la différence entre deux points.
- Calculer la quantité d'énergie utilisée.
- Calculer les différences de température, de temps et de vitesse entre deux points.

### Comment Utiliser la Fonction `abs()` en Python ? Une Analyse de la Syntaxe pour les Débutants <a name="utilisation"></a>

La syntaxe générale de la fonction `abs()` ressemble à ceci :

```python
abs(nombre)
```

Décomposons-la :

- La fonction `abs()` prend un seul argument, qui est **requis**. 
- L'argument est toujours un nombre qui peut avoir une valeur négative ou positive.
- Le nombre peut être soit :
    - Un entier, tel que `4`, `-15`, ou `10`.
    - Un nombre à virgule flottante, tel que `4.1`, `-15.06`, ou `2.13`.
    - Un nombre complexe. Un nombre complexe est composé de deux parties - une partie **réelle** qui consiste en un nombre réel tel que `1` ou `4`, et une partie **imaginaire**. En Python, la partie imaginaire est créée en ajoutant la lettre `j` comme suffixe – et non la lettre `i` comme en mathématiques. Vous ajoutez `j` à la fin d'un nombre réel, comme ceci : `1j` ou `4j`. Ainsi, un exemple de nombre complexe en Python est `2 + 4j` ou `1 + 2j`.

Maintenant, en ce qui concerne la valeur de retour de la fonction `abs()` :

- Pour les **nombres entiers**, la fonction `abs()` retourne la valeur absolue du nombre donné.
- Pour les **nombres à virgule flottante**, la fonction `abs()` retourne la valeur absolue du nombre donné.
- Pour les **nombres complexes**, la fonction `abs()` retourne la magnitude du nombre donné.

## Comment Utiliser la Fonction `abs()` avec des Exemples <a name="exemples"></a>

Dans les sections suivantes, vous verrez la fonction `abs()` en action et comment elle se comporte lorsqu'elle a un entier, un nombre à virgule flottante et un nombre complexe comme argument.

### Comment Utiliser la Fonction `abs()` avec un Argument Entier <a name="entier"></a>

Lorsque vous passez un entier comme argument, la fonction `abs()` retournera sa valeur absolue.

Voici un exemple de passage d'un entier positif comme argument :

```python
mon_nombre = 7

valeur_abs = abs(mon_nombre)

print(valeur_abs)

#sortie

#7
```

Et voici un exemple de passage d'un entier négatif comme argument.

N'oubliez pas que la valeur absolue sera toujours positive :

```python
mon_nombre = -17

valeur_abs = abs(mon_nombre)

print(valeur_abs)

#sortie

#17
```

### Comment Utiliser la Fonction `abs()` avec un Argument de Nombre à Virgule Flottante <a name="virgule-flottante"></a>

Lorsque vous passez un nombre à virgule flottante comme argument, la fonction `abs()` retournera sa valeur absolue.

Les exemples suivants fonctionnent de la même manière que les exemples de la section précédente.

Voici un nombre à virgule flottante positif comme argument :

```python
mon_nombre = 34.05

valeur_abs = abs(mon_nombre)

print(valeur_abs)

#sortie

#34.05
```

Et voici un nombre à virgule flottante négatif comme argument :

```python
mon_nombre = -43.2

valeur_abs = abs(mon_nombre)

print(valeur_abs)

#sortie

#43.2
```

### Comment Utiliser la Fonction `abs()` avec un Argument de Nombre Complexe <a name="complexe"></a>

Les nombres complexes fonctionnent différemment des entiers et des flottants.

Lorsque qu'un nombre complexe est passé comme argument à la fonction `abs()`, la valeur de retour est la magnitude de ce nombre.

La magnitude d'un nombre complexe, tel que `a+bj`, est la distance du nombre entre l'origine (0,0) et le point (a,b) dans le plan complexe. Et la magnitude d'un nombre complexe est calculée à l'aide du théorème de Pythagore, \\(\sqrt{a^2 + b^2}\\)

Prenons donc le nombre complexe `3 + 4j` comme exemple. Vous devrez calculer la racine carrée des carrés des nombres de la partie réelle (`3`) et de la partie imaginaire `4` : \\(\sqrt{3^2 + 4^2} = 5\\)

En Python, voici comment vous utiliseriez un nombre complexe avec la fonction `abs()` :

```python
mon_nombre = 3 + 4j

valeur_abs = abs(mon_nombre)

print(valeur_abs)

#sortie

#5.0
```

## Conclusion

Et voilà – vous connaissez maintenant les bases du fonctionnement de la fonction `abs()` de Python !

J'espère que vous avez trouvé cet article utile.

Pour en savoir plus sur le langage de programmation Python, consultez la [Certification en Calcul Scientifique avec Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/) de freeCodeCamp.

Vous commencerez par les bases et apprendrez de manière interactive et adaptée aux débutants. Vous construirez également cinq projets à la fin pour mettre en pratique et renforcer ce que vous avez appris.

Merci beaucoup d'avoir lu et bon codage :)