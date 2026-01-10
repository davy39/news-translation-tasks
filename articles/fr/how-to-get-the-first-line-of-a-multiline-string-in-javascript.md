---
title: Comment obtenir la première ligne d'une chaîne multiligne en JavaScript
subtitle: ''
author: Furkan Emin Can
co_authors: []
series: null
date: '2024-01-24T23:33:14.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-the-first-line-of-a-multiline-string-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/Cover.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment obtenir la première ligne d'une chaîne multiligne en JavaScript
seo_desc: 'In JavaScript, getting the first element of an array or string is pretty
  easy. But when it comes to getting the first line of a multiline string, some approaches
  can hurt your app''s performance in certain cases.

  In this article, we will look at the t...'
---

En JavaScript, obtenir le premier élément d'un tableau ou d'une chaîne est assez simple. Mais lorsqu'il s'agit d'obtenir la première ligne d'une chaîne multiligne, certaines approches peuvent nuire aux performances de votre application dans certains cas.

Dans cet article, nous examinerons les trois meilleures façons d'obtenir la première ligne d'une chaîne multiligne en JS.

Pour ceux d'entre vous qui sont pressés, voici la meilleure solution :

```javascript
input.slice(0, input.indexOf("\n"));
```

Et maintenant, si vous voulez en savoir plus, plongeons dans les détails.

## Le Problème

Le principal problème dans la plupart des solutions est que, pour simplement obtenir la première ligne de la chaîne, vous devez opérer sur la chaîne entière. Si l'entrée est trop grande, cette opération prend un temps inutilement long et consomme beaucoup de ressources.

Expliquons avec un exemple.

Supposons que j'ai une énorme chaîne qui contient 10 millions de lignes de texte et que je veux obtenir la première ligne. Je choisis donc d'utiliser la méthode `Array.split` comme dans l'exemple suivant :

```javascript
input.split("\n")[0];
```

Dans ce code, la méthode `split` opère sur les 10 millions de lignes pour obtenir seulement la première ligne. Par conséquent, pour obtenir seulement le premier élément, j'ai un tableau contenant 10 millions d'éléments.

Cette opération prend environ `1,7` secondes sur mon PC. C'est inutilement long pour une opération aussi petite.

Examinons les solutions pour surmonter ce problème.

## Les Solutions

Après quelques recherches, j'ai trouvé les trois meilleures façons de faire cette opération :

1. Utiliser les méthodes `String.indexOf` et `String.slice`.
2. Utiliser la méthode `Array.split`.
3. Utiliser la méthode `String.match`.

Voici les résultats de référence de chaque solution :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/benchmarks.png)
_Résultats de référence_

Vous pouvez également accéder aux résultats de référence depuis [ce lien](https://perf.link/#eyJpZCI6InhzeG9lOGh6cDgzIiwidGl0bGUiOiJHZXR0aW5nIHRoZSBmaXJzdCBsaW5lIG9mIGEgbXVsdGlsaW5lIHN0cmluZyIsImJlZm9yZSI6ImNvbnN0IGlucHV0ID0gQXJyYXkuZnJvbShBcnJheSgxMDAwKSwgKF8sIGkpID0%2BIGBJIGFtIHRoZSBsaW5lICR7aSArIDF9YCkuam9pbignXFxuJyk7IiwidGVzdHMiOlt7Im5hbWUiOiJTdHJpbmcuc2xpY2Ugd2l0aCBTdHJpbmcuaW5kZXhPZiIsImNvZGUiOiJpbnB1dC5zbGljZSgwLCBpbnB1dC5pbmRleE9mKCdcXG4nKSk7IiwicnVucyI6WzQ4MzUwMDAsNjQ5OTAwMCwxNDA0MDAwLDQ5NDYwMDAsMjM5MjAwMCwxMjg1MDAwLDcyNDIwMDAsNTg1OTAwMCwyMjk0MDAwLDM0OTIwMDAsNzM5NTAwMCwzOTI3MDAwLDE2NTEwMDAsNTg1OTAwMCw2MTAwMCwxMzY3MDAwLDUwODgwMDAsMTkyMDAwMCw3MzcyMDAwLDEyNjQwMDAsNTczMTAwMCwxNzgxMDAwLDE4NzkwMDAsNjk3ODAwMCw3MzYwMDAwLDU3MzEwMDAsNDA5MDAwMCw2ODI2MDAwLDQ3MzQwMDAsOTUxMDAwLDY0MzAwMCw1MTEwMDAsNjE3NjAwMCw3OTYzMDAwLDE3MjUwMDAsNDYyNjAwMCw0MTQwMDAsNDcwNzAwMCwxODg4MDAwLDcwNzIwMDAsMTcyNzAwMCwxMzMxMDAwLDQ5NDcwMDAsMjYwNDAwMCwyNzc4MDAwLDI5MDkwMDAsMjI4NDAwMCw4NDk2MDAwLDQ5MTIwMDAsNjU4OTAwMCwxNDcwMDAwLDY2MjMwMDAsNDA4MTAwMCwxMTkyMDAwLDUyMzEwMDAsMTY3ODAwMCwyNjIzMDAwLDYwODYwMDAsMzgwNDAwMCwxOTg0MDAwLDYzODUwMDAsMTA2MzAwMCw1MjY5MDAwLDEzOTEwMDAsMTk3ODAwMCw3NTkwMDAwLDIwMTAwMDAsODc0MDAwLDE0OTIwMDAsNjk1NjAwMCw4NzMwMDAsNzEzODAwMCw1NDcwMDAsMjc5NjAwMCw2OTQwMDAsNDA0OTAwMCwzMzYwMDAsMjE4MTAwMCwzOTEwMDAsMjUyNDAwMCw2NTMzMDAwLDE4MTAwMDAsMjEwMjAwMCwxMjcyMDAwLDcyNDUwMDAsNjA4MDAwMCwyNjkzMDAwLDcwMDQwMDAsMjg4ODAwMCwxNDYxMDAwLDUwOTAwMCw5MTAwMDAwLDE0MzQwMDAsMTE5MjAwMCw3NTAwMCwxMDAwMCwyNDc2MDAwLDQ0ODUwMDAsMTQ4OTAwMCw0OTkzMDAwXSwib3BzIjozNTI2NzUwfSx7Im5hbWUiOiJTdHJpbmcuc3BsaXQiLCJjb2RlIjoiaW5wdXQuc3BsaXQoJ1xcbicsIDEpWzBdOyIsInJ1bnMiOlsyMDIzMDAwLDQxMTkwMDAsNzU4MDAwLDI1MzMwMDAsMjE3MDAwMCw3NTkwMDAsMjM5MTAwMCwyNTYwMDAwLDE2NjIwMDAsMTU0NTAwMCwzMTI4MDAwLDE4OTAwMDAsMTI5MDAwMCw0NDQ5MDAwLDE4MDAwLDEzNzcwMDAsMjEyNjAwMCw5NzEwMDAsMjk1MTAwMCwxMzU4MDAwLDIzNTcwMDAsMTY5OTAwMCwxMjcxMDAwLDQyMTgwMDAsMjgxMDAwLDIzNDYwMDAsMzM1MDAwLDI3NjAwMDAsMTgzMjAwMCw2OTUwMDAsNDM4MDAwLDM2MDQwMDAsMjU2MzAwMCw0ODA1MDAwLDE2MzYwMDAsMzgwNTAwMCwxMjgwMDAsMjk0NjAwMCwxMzczMDAwLDUxNzQwMDAsNTkxMDAwLDQ1MDEwMDAsMjAyNTAwMCwxNzQyMDAwLDIwODEwMDAsMTQ5MjAwMCw3MTkwMDAsMzYyMTAwMCwxMzYwMDAwLDM1MzAwMDAsMTQ3OTAwMCwyNDMzMDAwLDMzNTkwMDAsMTQ2MjAwMCwxOTgzMDAwLDE3MTUwMDAsMTI4OTAwMCwzNDY5MDAwLDE3MTEwMDAsMTcxNTAwMCwzMTY3MDAwLDIwNTgwMDAsMjgwODAwMCw2ODcwMDAsMTcwOTAwMCwyODU4MDAwLDEyOTAwMDAsMTA0MjAwMCwxMjU3MDAwLDM0NzUwMDAsMTIxMjAwMCw0MzcxMDAwLDEyMjYwMDAsMjA0OTAwMCwzNzg3MDAwLDIzMDMwMDAsNDUzMDAwLDEyOTAwMDAsMjg4MDAwLDE4NzAwMDAsNDU2MDAwMCwxODg5MDAwLDE0OTkwMDAsNDA4MjAwMCwzNTk0MDAwLDM1NjcwMDAsMTc1MjAwMCwyODgwMDAwLDE0OTQwMDAsMTA3NzAwMCwzNjI3MDAwLDcyODAwMCwzNzUwMDAwLDEyOTAwMDAsMTAwMCwyOTcwMDAwLDI2NjAwMDAsMzEyODAwMCw4MTIwMDAsMjIxMjAwMF0sIm9wcyI6MjEzMzkzMH0seyJuYW1lIjoiU3RyaW5nLm1hdGNoIiwiY29kZSI6ImlucHV0Lm1hdGNoKC8uKig%2BPVxcbikvKVswXTsiLCJydW5zIjpbMjI3MDAwMCwyMzU5MDAwLDI0NTEwMDAsNTU1MDAwLDExNzIwMDAsMjQ3MTAwMCwxODMwMDAwLDEwMDAsMTAwMCwxMDg3MDAwLDIzNjMwMDAsMjQ2MDAwLDE2NDYwMDAsMjIzNTAwMCw2NzYxMDAwLDE3NTcwMDAsMTE3MjAwMCwyOTE5MDAwLDI3NjIwMDAsMjAwMDAwLDMwNzIwMDAsMTExMDAwLDM0ODMwMDAsMTc3ODAwMCwxNTAwMDAsMjgxNjAwMCwyODY0MDAwLDE1NDcwMDAsMTAwMCw5ODkwMDAsMzg1MzAwMCwxNTAyMDAwLDI1MjUwMDAsMjc5NDAwMCwxMDAwLDI2NzcwMDAsMjQ4ODAwMCw5MjgwMDAsMjM3ODAwMCwyOTUwMDAwLDIyODkwMDAsMzI0MDAwMCwxMDAwLDEwMDAsMTgzOTAwMCw0NjYwMDAsMTg3MDAwLDIxOTYwMDAsMTAwMCwyMzc4MDAwLDM3MDYwMDAsNjEyMDAwLDIzNjIwMDAsNzcwMDAwLDc4MDAwLDExMjIwMDAsMTg4NDAwMCwzMDczMDAwLDE1NjYwMDAsMzE5NDAwMCwxMDcyMDAwLDMzOTMwMDAsMTI5NTAwMCwyODcwMDAsMTMwMjAwMCwzOTgzMDAwLDI1MjIwMDAsNDUzMDAwLDI5NTIwMDAsMzQzODAwMCw1MzQwMDAsNDA2MzAwMCwyNTYwMDAsMTQ4MjAwMCwyMjMwMDAwLDgxODAwMCw0MTAwMCw0NTMwMDAsMjAwMDAsMjI2NDAwMCwyODkwMDAwLDc2NzAwMCwyNDE2MDAwLDE3MzEwMDAsMTk0MDAwMCwzMTU3MDAwLDI3NzgwMDAsMTY2MzAwMCw3MDUwMDAsMzEyNTAwMCwxODE5MDAwLDIwMTEwMDAsMTQ0MDAwMCw3NDcwMDAsMTAwMCwxMzAwMDAwLDEzMDIwMDAsMjI0ODAwMCw1MDYwMDAsMTMwMjAwMF0sIm9wcyI6MTcyODM2MH1dLCJ1cGRhdGVkIjoiMjAyNC0wMS0yMlQxOTowNDoxMS4zMzRaIn0%3D) et effectuer vos propres benchmarks.

Explorons chaque solution séparément.

### 1. Utiliser les méthodes `String.indexOf` et `String.slice`

Dans cette solution, nous utiliserons la méthode `String.indexOf` pour trouver l'index du caractère de nouvelle ligne (`\n`), puis nous découperons la chaîne à cet index avec la méthode `String.slice`.

```javascript
input.slice(0, input.indexOf("\n"));
```

Cette solution prend la première place dans les résultats de référence.

### 2. Utiliser la méthode `Array.split`

Comme vous l'avez vu dans le problème, la méthode `Array.split` opère sur la chaîne entière. Mais elle accepte également un paramètre optionnel `limit`. Nous pouvons utiliser ce paramètre pour éviter des opérations inutiles.

```javascript
input.split("\n", 1)[0];
```

Dans ce code, nous avons tiré parti du paramètre optionnel `limit` et ainsi l'opération s'arrête après la première opération de division.

Cette solution prend la deuxième place dans les résultats de référence.

### 3. Utiliser la méthode `String.match`

Cette approche est pour ceux d'entre vous qui veulent particulièrement utiliser des regex.

Nous utiliserons la méthode `String.match` dans ce cas. Nous créerons une expression régulière qui correspond à n'importe quel groupe de caractères suivi d'un caractère de nouvelle ligne, et nous la passerons à la méthode. Le premier élément du tableau retourné (qui est la correspondance) est la première ligne.

```javascript
input.match(/.*(?=\n)/)[0];
```

Cette solution prend la troisième place dans les résultats de référence et est deux fois plus lente que la première solution.

Selon [le MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp#literal_notation_and_constructor) :

> Avant que les expressions régulières puissent être utilisées, elles doivent être compilées.

La dégradation des performances est probablement due à cela.

## Conclusion

Dans cet article, nous avons examiné trois approches différentes pour obtenir la première ligne d'une chaîne multiligne.

En tant que développeurs, même pour une opération aussi petite, nous devons considérer les cas limites pour éviter des problèmes potentiels à l'avenir.

Merci d'avoir lu. Vous pouvez me suivre sur [Twitter](https://twitter.com/femincan) ou explorer davantage sur [mon blog personnel](https://femincan.dev). N'hésitez pas à me contacter — je serais ravi d'avoir de vos nouvelles !