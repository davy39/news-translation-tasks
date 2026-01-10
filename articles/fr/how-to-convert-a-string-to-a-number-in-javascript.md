---
title: Comment convertir une chaîne de caractères en nombre en JavaScript
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2022-05-02T22:25:54.000Z'
originalURL: https://freecodecamp.org/news/how-to-convert-a-string-to-a-number-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/volkan-olmez-aG-pvyMsbis-unsplash.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment convertir une chaîne de caractères en nombre en JavaScript
seo_desc: "There are many ways to convert a string into a number using JavaScript.\
  \ But what does that look like in code? \nIn this article, I will show you 11 ways\
  \ to convert a string into a number. \nHere's an Interactive Scrim of How to Convert\
  \ a String to a Nu..."
---

Il existe de nombreuses façons de convertir une chaîne de caractères en nombre en utilisant JavaScript. Mais à quoi cela ressemble-t-il en code ?

Dans cet article, je vais vous montrer 11 façons de convertir une chaîne de caractères en nombre.

### Voici un Scrim interactif sur la conversion d'une chaîne de caractères en nombre en JavaScript :

<iframe src="https://scrimba.com/scrim/co2894c679bc693326603ac73?embed=freecodecamp,mini-header" width="100%" height="420"></iframe>

## Comment convertir une chaîne de caractères en nombre en JavaScript en utilisant la fonction `Number()`

Une façon de convertir une chaîne de caractères en nombre serait d'utiliser la fonction `Number()`.

Dans cet exemple, nous avons une chaîne de caractères appelée `quantity` avec la valeur `"12"`.

```js
const quantity = "12";
```

Si nous utilisions l'opérateur `typeof` sur `quantity`, il retournerait le type de chaîne de caractères.

```js
console.log(typeof quantity);
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-9.50.17-AM.png)

Nous pouvons convertir `quantity` en nombre en utilisant la fonction `Number` comme ceci :

```js
Number(quantity)
```

Nous pouvons vérifier qu'il s'agit maintenant d'un nombre en utilisant à nouveau l'opérateur `typeof`.

```js
console.log(typeof Number(quantity));
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-9.57.35-AM.png)

Si vous essayez de passer une valeur qui ne peut pas être convertie en nombre, la valeur de retour serait `NaN` (Not a Number).

```js
console.log(Number("awesome"));
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-10.00.34-AM.png)

## Comment convertir une chaîne de caractères en nombre en JavaScript en utilisant la fonction **`parseInt()`**

Une autre façon de convertir une chaîne de caractères en nombre est d'utiliser la fonction **`parseInt()`**. Cette fonction prend une chaîne de caractères et un radix optionnel.

Un radix est un nombre entre 2 et 36 qui représente la base dans un système numérique. Par exemple, un radix de 2 représenterait le système binaire, tandis qu'un radix de 10 représente le système décimal.

Nous pouvons utiliser la variable `quantity` de l'exemple précédent pour convertir cette chaîne de caractères en nombre.

```js
const quantity = "12";

console.log(parseInt(quantity, 10));
```

Que se passe-t-il si j'essaie de changer la variable `quantity` en `"12.99"` ? Le résultat en utilisant **`parseInt()`** sera-t-il le nombre 12.99 ?

```js
const quantity = "12.99";

console.log(parseInt(quantity, 10));
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-10.45.08-AM.png)

Comme vous pouvez le voir, le résultat est un entier arrondi. Si vous souhaitez retourner un nombre à virgule flottante, vous devrez utiliser **`parseFloat()`**.

## Comment convertir une chaîne de caractères en nombre en JavaScript en utilisant la fonction **`parseFloat()`**

La fonction **`parseFloat()`** prendra une valeur et retournera un nombre à virgule flottante. Des exemples de nombres à virgule flottante seraient 12.99 ou 3.14.

Si nous modifions notre exemple précédent pour utiliser `parseFloat()`, le résultat serait le nombre à virgule flottante 12.99.

```js
const quantity = "12.99";

console.log(parseFloat(quantity));
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-10.55.03-AM.png)

Si vous avez des espaces de début ou de fin dans votre chaîne de caractères, `parseFloat()` convertira toujours cette chaîne de caractères en nombre à virgule flottante.

```js
const quantity = "   12.99    ";

console.log(parseFloat(quantity));
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-11.05.35-AM.png)

Si le premier caractère de votre chaîne de caractères ne peut pas être converti en nombre, `parseFloat()` retournera `NaN`.

```js
const quantity = "F12.99";

console.log(parseFloat(quantity));
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-11.08.33-AM.png)

## Comment convertir une chaîne de caractères en nombre en JavaScript en utilisant l'opérateur unaire plus (`+`)

L'opérateur unaire plus (`+`) convertira une chaîne de caractères en nombre. L'opérateur se placera avant l'opérande.

```js
const quantity = "12";

console.log(+quantity);
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-11.14.51-AM.png)

Nous pouvons également utiliser l'opérateur unaire plus (`+`) pour convertir une chaîne de caractères en nombre à virgule flottante.

```js
const quantity = "12.99";

console.log(+quantity);
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-11.16.38-AM.png)

Si la valeur de la chaîne de caractères ne peut pas être convertie en nombre, le résultat sera `NaN`.

```js
const quantity = "awesome";

console.log(+quantity);
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-11.18.10-AM.png)

## Comment convertir une chaîne de caractères en nombre en JavaScript en multipliant la chaîne de caractères par le nombre 1

Une autre façon de convertir une chaîne de caractères en nombre est d'utiliser une opération mathématique de base. Vous pouvez multiplier la valeur de la chaîne de caractères par 1 et elle retournera un nombre.

```js
const quantity = "12";

console.log(quantity * 1);
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-11.42.58-AM.png)

Comme vous pouvez le voir, lorsque nous multiplions la valeur `quantity` par 1, elle retourne le nombre 12. Mais comment cela fonctionne-t-il ?

Dans cet exemple, JavaScript convertit notre valeur de chaîne de caractères en nombre puis effectue cette opération mathématique. Si la chaîne de caractères ne peut pas être convertie en nombre, l'opération mathématique ne fonctionnera pas et elle retournera `NaN`.

```js
const quantity = "awesome";

console.log(quantity * 1);
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-11.18.10-AM.png)

Cette méthode fonctionnera également pour les nombres à virgule flottante.

```js
const quantity = "10.5";

console.log(quantity * 1);
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-11.56.19-AM.png)

## Comment convertir une chaîne de caractères en nombre en JavaScript en divisant la chaîne de caractères par le nombre 1

Au lieu de multiplier par 1, vous pouvez également diviser la chaîne de caractères par 1. JavaScript convertit notre valeur de chaîne de caractères en nombre puis effectue cette opération mathématique.

```js
const quantity = "10.5";

console.log(quantity / 1);
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-12.08.37-PM.png)

## Comment convertir une chaîne de caractères en nombre en JavaScript en soustrayant le nombre 0 de la chaîne de caractères

Une autre méthode serait de soustraire 0 de la chaîne de caractères. Comme avant, JavaScript convertit notre valeur de chaîne de caractères en nombre puis effectue cette opération mathématique.

```js
const quantity = "19";

console.log(quantity - 0);
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-12.11.59-PM.png)

## Comment convertir une chaîne de caractères en nombre en JavaScript en utilisant l'opérateur bitwise NOT (`~`)

L'opérateur bitwise NOT (`~`) inversera les bits d'un opérande et convertira cette valeur en un entier signé 32 bits. Un entier signé 32 bits est une valeur qui représente un entier en 32 bits (ou 4 octets).

Si nous utilisons un opérateur bitwise NOT (`~`) sur un nombre, il effectuera cette opération : -(x + 1)

```js
console.log(~19);
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-12.20.18-PM.png)

Mais si nous utilisons deux opérateurs bitwise NOT (`~`), il convertira notre chaîne de caractères en nombre.

```js
const quantity = "19";

console.log(~~quantity);
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-12.28.16-PM.png)

Cette méthode ne fonctionnera pas pour les nombres à virgule flottante car le résultat serait un entier.

```js
const quantity = "19.99";

console.log(~~quantity);
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-12.31.16-PM.png)

Si vous essayez d'utiliser cette méthode sur des caractères non numériques, le résultat serait zéro.

```js
const quantity = "awesome";

console.log(~~quantity);
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-12.32.45-PM.png)

Cette méthode a ses limitations car elle commencera à échouer pour les valeurs considérées comme trop grandes. Il est important de s'assurer que votre nombre est compris entre les valeurs d'un entier signé 32 bits.

```js
const quantity = "2700000000";

console.log(~~quantity);
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-12.36.16-PM.png)

Pour en savoir plus sur l'opérateur bitwise NOT (`~`), veuillez consulter la [documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_NOT).

## Comment convertir une chaîne de caractères en nombre en JavaScript en utilisant la fonction **`Math.floor()`**

Une autre façon de convertir une chaîne de caractères en nombre est d'utiliser la fonction **`Math.floor()`**. Cette fonction arrondira le nombre à l'entier inférieur le plus proche.

```js
const quantity = "13.4";

console.log(Math.floor(quantity));
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-12.44.53-PM.png)

Tout comme dans les exemples précédents, si nous essayons d'utiliser des caractères non numériques, le résultat serait `NaN`.

```js
const quantity = "awesome";

console.log(Math.floor(quantity));
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-12.46.08-PM.png)

## Comment convertir une chaîne de caractères en nombre en JavaScript en utilisant la fonction **`Math.ceil()`**

La fonction `Math.ceil()` arrondira un nombre à l'entier supérieur le plus proche.

```js
const quantity = "7.18";

console.log(Math.ceil(quantity));
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-12.48.15-PM.png)

## Comment convertir une chaîne de caractères en nombre en JavaScript en utilisant la fonction **`Math.round()`**

La fonction **`Math.round()`** arrondira le nombre à l'entier le plus proche.

Si j'ai la valeur 6.3, alors **`Math.round()`** retournera 6.

```js
const quantity = "6.3";

console.log(Math.round(quantity));
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-12.50.20-PM.png)

Mais si je change cette valeur en 6.5, alors **`Math.round()`** retournera 7.

```js
const quantity = "6.5";

console.log(Math.round(quantity));
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screen-Shot-2022-05-01-at-12.51.35-PM.png)

## Conclusion

Dans cet article, je vous ai montré 11 façons de convertir une chaîne de caractères en nombre en utilisant JavaScript.

Voici les 11 méthodes différentes discutées dans l'article.

1. utiliser la fonction `Number()`
2. utiliser la fonction `parseInt()`
3. utiliser la fonction `parseFloat()`
4. utiliser l'opérateur unaire plus (`+`)
5. multiplier la chaîne de caractères par le nombre 1
6. diviser la chaîne de caractères par le nombre 1
7. soustraire le nombre 0 de la chaîne de caractères
8. utiliser l'opérateur bitwise NOT (`~`)
9. utiliser la fonction `Math.floor()`
10. utiliser la fonction `Math.ceil()`
11. utiliser la fonction `Math.round()`

J'espère que vous avez apprécié cet article et bonne chance dans votre parcours JavaScript.