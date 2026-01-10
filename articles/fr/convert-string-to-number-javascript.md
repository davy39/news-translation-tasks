---
title: Comment convertir une chaîne de caractères en nombre en JavaScript (avec exemples)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-07T23:20:00.000Z'
originalURL: https://freecodecamp.org/news/convert-string-to-number-javascript
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cb1740569d1a4ca33a5.jpg
tags:
- name: JavaScript
  slug: javascript
- name: toothbrush
  slug: toothbrush
seo_title: Comment convertir une chaîne de caractères en nombre en JavaScript (avec
  exemples)
seo_desc: 'Converting Strings to Numbers

  The parseInt() function parses a string argument and returns an integer of the specified
  radix (the base in mathematical numeral systems).

  parseInt(string, radix);


  Parameters

  string


  The value to parse. If the string ar...'
---

## **Conversion de chaînes de caractères en nombres**

La fonction `parseInt()` analyse un argument de type chaîne et retourne un entier selon le radix spécifié (la base dans les systèmes de numération mathématiques).

```js
parseInt(string, radix);
```

### **Paramètres**

```text
string
```

La valeur à analyser. Si l'argument `string` n'est pas une chaîne, il est converti en chaîne (en utilisant l'opération abstraite `ToString`). Les espaces en début de chaîne sont ignorés.

**radix**
Un entier entre 2 et 36 qui représente le radix (la base dans les systèmes de numération mathématiques) de la chaîne mentionnée ci-dessus. Spécifiez `10` pour le système de numération décimal couramment utilisé par les humains. Spécifiez toujours ce paramètre pour éviter toute confusion et garantir un comportement prévisible. Différentes implémentations produisent des résultats différents lorsqu'un radix n'est pas spécifié, généralement en le définissant par défaut à 10.

**Valeur de retour**
Un nombre entier analysé à partir de la chaîne donnée. Si le premier caractère ne peut pas être converti en nombre, `NaN` est retourné.

### **Description**

La fonction `parseInt` convertit son premier argument en chaîne, l'analyse et retourne un entier ou `NaN`. Si ce n'est pas `NaN`, la valeur retournée sera l'entier qui est le premier argument pris comme un nombre dans le radix (base) spécifié. Par exemple, un radix de 10 indique une conversion à partir d'un nombre décimal, 8 octal, 16 hexadécimal, et ainsi de suite. Pour les radix supérieurs à `10`, les lettres de l'alphabet indiquent des chiffres supérieurs à 9. Par exemple, pour les nombres hexadécimaux (base 16), les lettres `A` à `F` sont utilisées.

Si `parseInt` rencontre un caractère qui n'est pas un chiffre dans le radix spécifié, il l'ignore ainsi que tous les caractères suivants et retourne la valeur entière analysée jusqu'à ce point. `parseInt` tronque les nombres en valeurs entières. Les espaces en début et en fin de chaîne sont autorisés.

Parce que certains nombres incluent le caractère `e` dans leur représentation sous forme de chaîne (par exemple, `6.022e23`), l'utilisation de `parseInt` pour tronquer des valeurs numériques produira des résultats inattendus lorsqu'elle est utilisée sur des nombres très grands ou très petits. `parseInt` ne doit pas être utilisé comme substitut à `Math.floor()`.

Si le radix est `undefined` ou 0 (ou absent), JavaScript suppose ce qui suit :

* Si la chaîne d'entrée commence par "0x" ou "0X", le radix est 16 (hexadécimal) et le reste de la chaîne est analysé.
* Si la chaîne d'entrée commence par "0", le radix est 8 (octal) ou 10 (décimal). Le choix exact du radix dépend de l'implémentation. ECMAScript 5 spécifie que 10 (décimal) est utilisé, mais tous les navigateurs ne supportent pas encore cela. Pour cette raison, spécifiez toujours un radix lors de l'utilisation de parseInt.
* Si la chaîne d'entrée commence par une autre valeur, le radix est 10 (décimal).
* Si le premier caractère ne peut pas être converti en nombre, parseInt retourne NaN.

Pour les calculs arithmétiques, la valeur NaN n'est pas un nombre dans aucun radix. Vous pouvez appeler la fonction isNaN pour déterminer si le résultat de parseInt est NaN. Si NaN est transmis à des opérations arithmétiques, le résultat de l'opération sera également NaN.

Pour convertir le nombre en sa représentation littérale de chaîne dans un radix particulier, utilisez intValue.toString(radix).

### **Exemples**

Utilisation de `parseInt`
Les exemples suivants retournent tous `15` :

```js
parseInt(' 0xF', 16);
parseInt(' F', 16);
parseInt('17', 8);
parseInt(021, 8);
parseInt('015', 10);   // parseInt(015, 10); retournera 15
parseInt(15.99, 10);
parseInt('15,123', 10);
parseInt('FXX123', 16);
parseInt('1111', 2);
parseInt('15 * 3', 10);
parseInt('15e2', 10);
parseInt('15px', 10);
parseInt('12', 13);
```

Les exemples suivants retournent tous `NaN` :

```js
parseInt('Hello', 8); // Ce n'est pas un nombre du tout
parseInt('546', 2);   // Les chiffres ne sont pas valides pour les représentations binaires
```

Les exemples suivants retournent tous `-15` :

```js
parseInt('-F', 16);
parseInt('-0F', 16);
parseInt('-0XF', 16);
parseInt(-15.1, 10)
parseInt(' -17', 8);
parseInt(' -15', 10);
parseInt('-1111', 2);
parseInt('-15e1', 10);
parseInt('-12', 13);
```

Les exemples suivants retournent tous `4` :

```js
parseInt(4.7, 10);
parseInt(4.7 * 1e22, 10); // Un très grand nombre devient 4
parseInt(0.00000000000434, 10); // Un très petit nombre devient 4
```

L'exemple suivant retourne `224` :

```js
parseInt('0e0', 16);
```

#### **Plus d'informations :**

[parseInt sur MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comparison_Operators)

* [parseInt()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseInt) et [parseFloat()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseFloat) tentent de convertir la chaîne en nombre si possible. Par exemple, `var x = parseInt("100"); // x = 100`
* [Number()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/number) convertira en nombre la valeur qui peut être représentée. Cela inclut les dates en nombre de millisecondes depuis le 1er janvier 1970 à minuit UTC, les valeurs booléennes en 1 ou 0, et les valeurs qui ne peuvent pas être converties en un nombre reconnaissable deviendront NaN. Cela signifie "Not a Number" et est également techniquement un nombre !