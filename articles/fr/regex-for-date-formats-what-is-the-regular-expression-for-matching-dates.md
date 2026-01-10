---
title: "RegEx pour les formats de date \x13 Expressions régulières pour la correspondance\
  \ des dates"
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-05-18T12:41:17.000Z'
originalURL: https://freecodecamp.org/news/regex-for-date-formats-what-is-the-regular-expression-for-matching-dates
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/dateRegEx.png
tags:
- name: Regex
  slug: regex
seo_title: "RegEx pour les formats de date \x13 Expressions régulières pour la correspondance\
  \ des dates"
seo_desc: 'Regular expressions let you match any string, be it in the form of various
  user inputs such as username, password, URL, and even different date formats.

  In this article, I’ll show you several ways you can match a date with regular expressions.

  In the...'
---

Les expressions régulières vous permettent de faire correspondre n'importe quelle chaîne, qu'il s'agisse de diverses entrées utilisateur telles que le nom d'utilisateur, le mot de passe, l'URL, et même différents formats de date.

Dans cet article, je vais vous montrer plusieurs façons de faire correspondre une date avec des expressions régulières.

Dans le monde de la programmation, il existe toujours plusieurs façons de faire la même chose. Ainsi, la manière dont je vais vous montrer comment faire correspondre des formats de date avec regex peut être différente de ce que vous verrez ailleurs.


## Ce que nous allons couvrir
- [Comment faire correspondre des dates avec des expressions régulières](#heading-comment-faire-correspondre-des-dates-avec-des-expressions-regulieres)
  - [Comment faire correspondre des dates avec des expressions régulières  Exemple 1](#heading-comment-faire-correspondre-des-dates-avec-des-expressions-regulieres-exemple-1)
  - [Comment faire correspondre des dates avec des expressions régulières  Exemple 2](#heading-comment-faire-correspondre-des-dates-avec-des-expressions-regulieres-exemple-2)
  - [Comment faire correspondre des dates avec des expressions régulières  Exemple 3](#heading-comment-faire-correspondre-des-dates-avec-des-expressions-regulieres-exemple-3)
- [Conclusion](#heading-conclusion)


## Comment faire correspondre des dates avec des expressions régulières
Les dates sont généralement des nombres sauf si vous les formatez avec certains outils de programmation. Ainsi, les caractères que je vais utiliser pour faire correspondre les dates seront des caractères numériques.


### Comment faire correspondre des dates avec des expressions régulières  Exemple 1
Commençons par quelque chose de moins complexe d'abord. En supposant que le format de date est en `JJ/MM/AAAA` ou `MM/JJ/AAAA`, cela fonctionnerait :

```bash
\d{1,2}\/\d{1,2}\/\d{2,4}
```
Dans la regex ci-dessus :

* `\d{1,2}` correspond à 1 ou 2 chiffres
* `\/` correspond à une barre oblique (le séparateur). Vous pouvez également faire d'un trait d'union (-) le séparateur
* \d{2,4} correspond à 2 ou 4 chiffres

En effet, le motif correspond à une date :

![Screenshot-2023-05-18-at-11.08.02](https://www.freecodecamp.org/news/content/images/2023/05/Screenshot-2023-05-18-at-11.08.02.png) 

Mais ce motif est trop générique car nous ne savons pas lequel est lequel entre la date et le mois. L'année peut également être de 2 ou 4 chiffres. 

En bref, tout ce qui n'est pas une date valide passerait :

![Screenshot-2023-05-18-at-11.11.10](https://www.freecodecamp.org/news/content/images/2023/05/Screenshot-2023-05-18-at-11.11.10.png) 


Ce n'est pas ainsi que vous voulez faire correspondre une date. Je vais vous montrer un meilleur motif ensuite.


### Comment faire correspondre des dates avec des expressions régulières  Exemple 2
Voici un autre motif qui peut faire correspondre une date :

```bash
(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[0,1,2])\/(19|20)\d{2}
```

Dans le motif ci-dessus : 

* `(0[1-9]|[12][0-9]|3[01])` est le premier groupe du motif et il vous permet de spécifier la date uniquement entre `01` et `31`
* `\/` est le séparateur
* `(0[1-9]|1[0,1,2])` représente le mois et il vous permet de le spécifier entre `01` et `12`
* `\/` est un autre séparateur
* `(19|20)\d{2}` représente l'année qui peut être entre 1900 et n'importe quelle année 2000

![Screenshot-2023-05-18-at-11.37.38](https://www.freecodecamp.org/news/content/images/2023/05/Screenshot-2023-05-18-at-11.37.38.png) 

Vous pouvez remplacer le séparateur par un trait d'union de cette manière :

```bash
(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[1,2])-(19|20)\d{2}
```

Et vous pouvez accepter à la fois la barre oblique et le trait d'union comme séparateur :

```bash
(0[1-9]|[12][0-9]|3[01])(\/|-)(0[1-9]|1[1,2])(\/|-)(19|20)\d{2}
```

![Screenshot-2023-05-18-at-11.41.32](https://www.freecodecamp.org/news/content/images/2023/05/Screenshot-2023-05-18-at-11.41.32.png)

Vous pouvez également réorganiser le motif pour qu'il soit au format `MM/JJ/AAAA` de cette manière :

```bash
(0[1-9]|1[1,2])(\/|-)(0[1-9]|[12][0-9]|3[01])(\/|-)(19|20)\d{2}
```

![Screenshot-2023-05-18-at-11.46.46](https://www.freecodecamp.org/news/content/images/2023/05/Screenshot-2023-05-18-at-11.46.46.png)


### Comment faire correspondre des dates avec des expressions régulières  Exemple 3
Souvent, vous n'accepterez qu'une seule date dans votre entrée. Dans ce cas, vous devez spécifier le début et la fin d'une chaîne avec un accent circonflexe (`^`) et un signe dollar (`$`).

Voici comment j'ai élaboré ce motif :

```bash
^(3[01]|[12][0-9]|0?[1-9])(\/|-)(1[0-2]|0?[1-9])\2([0-9]{2})?[0-9]{2}$
```

Et voici ce que fait le motif :

- `^` désigne le début de la chaîne
- `(3[01]|[12][0-9]|0?[1-9])` représente le jour
    - `3[01]` correspond aux nombres de `30` à `31`
    - `[12][0-9]` correspond aux nombres de `10` à `29`
    - `0?[1-9]` correspond aux nombres de `1` à `9`, avec un zéro initial facultatif
- `(\/|-)` correspond à une barre oblique (`/`) ou un trait d'union (`-`)
- `(1[0-2]|0?[1-9])` représente la partie mois
   - `1[0-2]` correspond aux nombres de `10` à `12`
   - `0?[1-9]` correspond aux nombres de `1` à `9`, avec un zéro initial facultatif
- `\2` est une référence arrière qui correspond au même délimiteur capturé dans le deuxième groupe de capture `(\/|-)`. Cela garantit que le délimiteur entre le jour et le mois est cohérent
- `([0-9]{2})?` correspond à la partie année à deux chiffres de manière facultative
- `([0-9]{2})` correspond à n'importe quel deux chiffres représentant une année
- `[0-9]{2}` correspond aux deux derniers chiffres de l'année
- `$` désigne la fin de la chaîne


## Conclusion
Cet article vous a montré comment faire correspondre une date avec des expressions régulières à travers trois exemples.

Le premier exemple est un peu générique et ne fonctionnera pas bien pour faire correspondre une date, mais le deuxième peut faire correspondre des dates valides dans une entrée. Le troisième le fait mieux car il est adapté pour une date valide et unique  ce qui serait probablement ce que vous voulez faire.