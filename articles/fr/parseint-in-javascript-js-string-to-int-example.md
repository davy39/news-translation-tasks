---
title: parseInt() en JavaScript – Exemple de conversion de chaîne en entier
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-02-11T00:44:09.000Z'
originalURL: https://freecodecamp.org/news/parseint-in-javascript-js-string-to-int-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/parseint.png
tags:
- name: JavaScript
  slug: javascript
seo_title: parseInt() en JavaScript – Exemple de conversion de chaîne en entier
seo_desc: "In this tutorial, we will talk about the parseInt function in JavaScript.\
  \ This function parses (break down) a string and returns an integer or NaN (Not\
  \ a Number). \nHow the parseInt function works\nThe main purpose of using the parseInt\
  \ function is to ..."
---

Dans ce tutoriel, nous allons parler de la fonction `parseInt` en JavaScript. Cette fonction analyse (décompose) une chaîne et retourne un entier ou `NaN` (Not a Number).

## Comment fonctionne la fonction `parseInt`

Le but principal de l'utilisation de la fonction `parseInt` est d'extraire un nombre d'une chaîne. Cela transforme la valeur retournée en un nombre réel.

Voici la syntaxe :

```txt
parseInt(string)
```

Considérons l'exemple ci-dessous :

```javascript
const myNumber = '3';
console.log(2 + myNumber);
// retourne 23
```

Dans l'exemple ci-dessus, 3 est une chaîne et non un nombre réel. Lorsque nous ajoutons 2 à la chaîne, nous obtenons 23 car nous ajoutons simplement 2 à une chaîne qui est sous la forme d'un nombre.

Avec la fonction `parseInt`, nous pouvons extraire 3 de la chaîne et le transformer en un nombre réel. Voici un exemple :

```javascript
const myNumber = '3';
console.log(2 + parseInt(myNumber));
// retourne 5
```

Maintenant, la fonction a extrait 3 de la chaîne et l'a converti en un nombre réel.

De '3' à 3.

Rappelons que nous avons dit que la fonction `parseInt` peut retourner soit un entier, soit `NaN`. Alors, quand obtiendrions-nous une valeur `NaN` ?

Cela se produit lorsque nous avons du texte avant un nombre dans une chaîne. Quelque chose comme "age is 50" retournera une valeur `NaN` car la fonction `parseInt` ne regarde que la première valeur au début de la chaîne. Si la valeur n'est pas un nombre, `NaN` est retourné. Voici :

```javascript
const age = 'age is 50';
console.log(parseInt(age));
// retourne NaN
```

Réorganisons la chaîne et voyons ce qui se passe.

```javascript
const age = '50 is the age';
console.log(parseInt(age));
// retourne 50
```

Maintenant, la première valeur de la chaîne est un nombre et ce nombre nous est retourné.

Notez que la fonction `parseInt` ignore les valeurs flottantes. Si l'âge ci-dessus était 50.05, elle retournerait toujours 50 et ignorerait .05.

De la même manière, si nous avions une chaîne comme ceci : "50 100 150 200", nous n'obtiendrions que 50. Cela est dû au fait que la fonction `parseInt` tente uniquement d'extraire la première valeur d'une chaîne.

Et si la chaîne avait ses valeurs écrites ensemble comme ceci : '50istheage', 50 serait toujours retourné.

## Le paramètre `radix`

La fonction `parseInt` accepte un deuxième paramètre connu sous le nom de `radix`. Ce paramètre spécifie quel système de numération utiliser. Si le radix est omis, alors 10 est pris par défaut.

Voici la syntaxe :

```txt
parseInt(string, radix)
```

Il s'agit généralement d'un entier compris entre 2 et 36. Si la valeur du radix est inférieure à 2 ou supérieure à 36, alors `NaN` est retourné.

Si nous devions spécifier un radix de 12, cela impliquerait que le nombre dans la chaîne doit être analysé à partir de la valeur duodécimale du nombre vers sa valeur décimale.

Voici un exemple rapide :

```javascript
console.log(parseInt("50", 12));
// retourne 60
```

Nous obtenons 60 car la valeur duodécimale de 50 en base 10 (décimal) est 60.

## Conclusion

Dans ce tutoriel, nous avons appris à utiliser la fonction `parseInt` pour extraire des nombres de chaînes.

Nous avons également vu comment utiliser le paramètre `radix` pour spécifier quel système de numération utiliser lors de la conversion de notre entier retourné.

Merci d'avoir lu !