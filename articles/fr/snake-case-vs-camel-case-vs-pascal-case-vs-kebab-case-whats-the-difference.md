---
title: Snake Case VS Camel Case VS Pascal Case VS Kebab Case – Quelles sont les différences
  entre les casings ?
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-11-29T16:33:11.000Z'
originalURL: https://freecodecamp.org/news/snake-case-vs-camel-case-vs-pascal-case-vs-kebab-case-whats-the-difference
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/pexels-olia-danilevich-4974912.jpg
tags:
- name: General Programming
  slug: programming
seo_title: Snake Case VS Camel Case VS Pascal Case VS Kebab Case – Quelles sont les
  différences entre les casings ?
seo_desc: 'As a software engineer, you may be familiar with the following quote by
  Leon Bambrick:


  “There are 2 hard problems in computer science: cache invalidation, naming things,
  and off-by-1 errors.”


  Indeed, naming things when programming can be challengin...'
---

En tant qu'ingénieur logiciel, vous êtes peut-être familier avec la citation suivante de [Leon Bambrick](https://twitter.com/secretGeek/status/7269997868?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E7269997868%7Ctwgr%5Eb9b41e252e8f8e5c2863c7a50642e9ec2ff0fe18%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fmartinfowler.com%2Fbliki%2FTwoHardThings.html) :

> « Il y a 2 problèmes difficiles en informatique : l'invalidation du cache, le nommage des choses, et les erreurs de décalage de 1. »

En effet, nommer les choses lors de la programmation peut être un défi lorsque vous avez différentes conventions de nommage disponibles.

Dans cet article, je vais expliquer les différences entre les types de casings les plus largement utilisés en programmation.

Voici ce que nous allons couvrir :

1. [Pourquoi utiliser des casings en programmation ?](#intro)
    1. [Qu'est-ce que le snake case ?](#snake-case)
    2. [Qu'est-ce que le kebab case ?](#kebab-case)
    3. [Qu'est-ce que le camel case ?](#camel-case)
    4. [Qu'est-ce que le pascal case ?](#pascal-case)

## Pourquoi Utiliser des Casings en Programmation ? <a name="intro"></a>

En programmation, les espaces sont des caractères réservés.

Prenons l'exemple suivant.

Supposons que vous souhaitiez créer une variable dans votre programme, et que le nom de la variable comporte plus d'un mot.

Pour que votre programme ne plante pas, vous ne pouvez pas laisser d'espaces entre les différents mots lors de la création de la variable.

Par exemple, vous ne pouvez pas faire ce qui suit :

```
nombre de donuts = 34
```

Si vous essayiez ce qui précède, vous obtiendriez une erreur.

La plupart (sinon tous) des langages de programmation interprètent chaque mot comme une chose complètement séparée et une unité unique.

`nombre`, `de`, et `donuts` sont traités séparément les uns des autres en raison du caractère espace entre eux.

Pour que votre programme fonctionne correctement, vous devez supprimer tous les espaces et combiner les mots en une seule chaîne de caractères d'une manière spécifique. Et il existe plusieurs façons de les combiner.

Plus précisément, il existe certaines conventions de nommage disponibles dans tous les langages de programmation, également connues sous le nom de :

- snake case
- kebab case
- camel case
- pascal case

En ce qui concerne l'utilisation des styles de casings, il n'y a pas de réponse définitive quant à savoir lequel est le meilleur. Cela dépend.

Lors du choix d'un style de casing, gardez à l'esprit les meilleures pratiques du langage de programmation que vous utilisez dans votre projet.

Et peu importe le casing que vous choisissez, restez cohérent dans votre projet.

Il est considéré comme une bonne pratique de choisir un style de casing et de s'y tenir. Ainsi, votre code restera lisible, facile à comprendre et maintenable pour vous et les autres développeurs avec lesquels vous pourriez travailler en équipe.

Examinons chaque casing plus en détail dans les sections suivantes.

### Qu'est-ce que le Snake Case ? <a name="snake-case"></a>

Le snake case sépare chaque mot avec un caractère de soulignement (`_`).

Lors de l'utilisation du snake case, toutes les lettres doivent être en minuscules.

Voici quelques exemples de la façon dont vous utiliseriez le snake case :

```
nombre_de_donuts = 34

phrase_preferee = "Hello World"
```

Le snake case est utilisé pour créer des noms de variables et de méthodes.

Le snake case est également un bon choix pour nommer des fichiers, car il garde les noms lisibles.

Vous le rencontrerez typiquement le plus lors de la programmation en Python et moins lors de la programmation en Java, JavaScript ou TypeScript.

Vous le rencontrerez également lors de la manipulation de bases de données, car il est utilisé pour créer des noms de tables et de colonnes.

Il existe également une version en majuscules du snake case où toutes les lettres sont en majuscules - également connue sous le nom de screaming snake case.

Voici quelques exemples de la façon dont vous utiliseriez le snake case en majuscules :

```
NOMBRE_DE_DONUTS = 34

PHRASE_PREFEREE = "Hello World"
```

La version en majuscules est utilisée pour déclarer des constantes dans la plupart des langages de programmation. Une constante est un élément de données dont la valeur ne change pas tout au long de la vie d'un programme.

### Qu'est-ce que le Kebab Case ? <a name="kebab-case"></a>

Le kebab case est très similaire au snake case.

La différence entre le snake case et le kebab case est que le kebab case sépare chaque mot avec un caractère de trait d'union, `-`, au lieu d'un soulignement.

Ainsi, tous les mots sont en minuscules, et chaque mot est séparé par un trait d'union.

Le kebab case est une autre des façons les plus lisibles par l'homme de combiner plusieurs mots en un seul mot.

Voici quelques exemples de la façon dont vous utiliseriez le kebab case :

```
nombre-de-donuts = 34

phrase-preferee = "Hello World"
```

Vous rencontrerez le kebab case principalement dans les URLs.

Une URL (abréviation de Uniform Resource Locator) est une adresse unique pour accéder à une ressource sur le Web.

### Qu'est-ce que le Camel Case ? <a name="camel-case"></a>

Lors de l'utilisation du camel case, vous commencez par mettre le premier mot en minuscules. Ensuite, vous mettez en majuscule la première lettre de chaque mot qui suit.

Ainsi, une lettre majuscule apparaît au début du deuxième mot et à chaque nouveau mot suivant.

Voici quelques exemples de la façon dont vous utiliseriez le camel case :

```
nombreDeDonuts = 34

phrasePreferee = "Hello World"
```

Dans l'exemple `nombreDeDonuts`, le premier mot `nombre` est en minuscules. Ensuite, la première lettre du deuxième mot, `De`, est en majuscule, tout comme la première lettre du troisième mot, `Donuts`.

Vous rencontrerez le camel case en Java, JavaScript et TypeScript pour créer des noms de variables, de fonctions et de méthodes.

### Qu'est-ce que le Pascal Case ? <a name="pascal-case"></a>

Le pascal case est similaire au camel case.

La seule différence entre les deux est que le pascal case nécessite que la première lettre du premier mot soit également en majuscule.

Ainsi, lors de l'utilisation du pascal case, chaque mot commence par une lettre majuscule (contrairement au camel case, où le premier mot est en minuscules).

Voici quelques exemples de la façon dont vous utiliseriez le pascal case :

```
NombreDeDonuts = 34

PhrasePreferee = "Hello World"
```

Vous verrez le pascal case utilisé pour nommer des classes dans la plupart des langages de programmation.

## Conclusion

Espérons que cet article vous a aidé à comprendre les différences entre les types de casings en programmation et où vous rencontrerez probablement chacun d'eux.

Merci d'avoir lu, et bon codage !