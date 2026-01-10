---
title: JavaScript Replace – Comment utiliser la méthode String.prototype.replace()
  avec un exemple JS
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-02-08T21:26:21.000Z'
originalURL: https://freecodecamp.org/news/javascript-replace-how-to-use-the-string-prototype-replace-method-js-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/replace.png
tags:
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: JavaScript Replace – Comment utiliser la méthode String.prototype.replace()
  avec un exemple JS
seo_desc: 'The String.prototype.replace() method searches for the first occurrence
  of a string and replaces it with the specified string. It does this without mutating
  the original string.

  This method works for regular expressions, too, so the item you''re searc...'
---

La méthode `String.prototype.replace()` recherche la première occurrence d'une chaîne et la remplace par la chaîne spécifiée. Elle le fait sans modifier la chaîne originale.

Cette méthode fonctionne également pour les expressions régulières, donc l'élément que vous recherchez peut être exprimé sous forme d'expression régulière.

La valeur à retourner en tant que valeur remplacée peut être exprimée sous forme de chaîne ou de fonction.

## Syntaxe de base de la méthode String.prototype.replace()

```js
const variable = variable.replace("stringToReplace", "expectedString");
```

Vous utilisez la méthode `replace()` en :
- assignant la chaîne initiale ou les chaînes à une variable
- déclarant une autre variable
- pour la valeur de la nouvelle variable, en préfixant le nom de la nouvelle variable avec la méthode replace()
- en séparant par des virgules la chaîne que vous souhaitez remplacer et la chaîne attendue dans les crochets

## Exemples de la méthode String.prototype.replace()

Un exemple de base ressemblerait à ceci :

```js
const coding = "I learned how to code from TV";
const replacedString = coding.replace("TV", "freeCodeCamp");

console.log(replacedString); // Résultat : I learned how to code from freeCodeCamp
```

Dans l'exemple ci-dessus :
- J'ai déclaré une variable nommée coding et je lui ai assigné la chaîne « I learned how to code from TV »
- J'ai déclaré une autre variable nommée `replacedString`
- Pour la valeur de la variable `replacedString`, j'ai utilisé la méthode `replace()` et j'ai spécifié que je voulais remplacer « TV » de la variable initiale par « freeCodeCamp ».

Ci-dessous, un exemple démontrant que la chaîne initiale n'est jamais modifiée (changée) par la méthode `replace()` :

```js
const coding = "I learned how to code from TV";
const replacedString = coding.replace("TV", "freeCodeCamp");

console.log(replacedString); // Résultat : I learned how to code from freeCodeCamp
console.log(coding); // Résultat : I learned how to code from TV
```

Dans l'exemple ci-dessous, j'ai utilisé des expressions régulières pour rechercher le texte qui correspond à « TV » et je l'ai remplacé par « freeCodeCamp » :

```js
const coding = "I learned how to code from TV";
const replacedString = coding.replace(/TV/, "freeCodeCamp");

console.log(replacedString); // Résultat : I learned how to code from freeCodeCamp
```

Puisque la méthode `replace()` ne fonctionne que pour la première occurrence d'un texte dans une chaîne, que faites-vous si vous souhaitez remplacer toutes les occurrences d'un mot par un autre mot dans une chaîne ? Vous pouvez utiliser la méthode `replaceAll()`.

## Comment utiliser la méthode `replaceAll()`

Une méthode de chaîne légèrement similaire à la méthode `replace()` est la méthode `replaceAll()`.

Cette méthode remplace toutes les occurrences d'un certain mot dans une chaîne.

### Exemple de la méthode `replaceAll()`

```js
const coding = "I learned how to code from TV. TV remains in my heart for life.";
const replacedString = coding.replaceAll("TV", "freeCodeCamp");

console.log(replacedString); // Résultat : I learned how to code from freeCodeCamp. freeCodeCamp remains in my heart for life.
```

Chaque occurrence de « TV » a été remplacée par « freeCodeCamp » grâce à la méthode `replaceAll()`.

Avec la méthode `replace()` originale, vous pouvez obtenir ce que fait `replaceAll()` en utilisant des expressions régulières pour rechercher chaque occurrence d'un certain mot dans une chaîne et le remplacer par un autre mot.

```js
const coding = "I learned how to code from TV. TV remains in my heart for life.";
const replacedString = coding.replace(/TV/g, "freeCodeCamp");

console.log(replacedString); // Résultat : I learned how to code from freeCodeCamp. freeCodeCamp remains in my heart for life.
```

J'ai pu rechercher chaque mot qui correspond à « TV » avec le drapeau `g` d'une expression régulière et le remplacer par « freeCodeCamp ».

## Comment passer une fonction à la méthode `replace()`

Comme je l'ai dit précédemment, vous pouvez exprimer la valeur que vous souhaitez retourner en tant que valeur remplacée sous forme de fonction.

Dans l'exemple ci-dessous, j'ai converti le titre de cet article en un slug d'URL avec la méthode replace :

```js
const articleTitle = "JavaScript Replace – How to Use the String.prototype.replace() Method";
const slugifyArticleTitle = articleTitle.toLowerCase().replace(/ /g, function (article) {
    return article.split(" ").join("-");
  });

console.log(slugifyArticleTitle); // Résultat : javascript-replace--how-to-use-the-string.prototype.replace()-method
```

Dans le script ci-dessus :
- J'ai déclaré une variable nommée `articleTitle` et j'ai assigné le titre de cet article
- J'ai déclaré une autre variable nommée `slugifyArticleTitle` et j'ai converti le titre de l'article en lettres minuscules avec la méthode `toLowerCase()`
- J'ai utilisé la méthode `replace()` et j'ai recherché chaque espace blanc avec `/ /g`
- J'ai ensuite passé une fonction à la méthode `replace()`, et je lui ai assigné un paramètre de `article`. Ce paramètre fait référence à la chaîne (titre de l'article) convertie en lettres minuscules
- À l'intérieur de la fonction, j'ai retourné que je divise le titre de l'article partout où il y a un espace blanc. Cela a été fait avec la méthode `split()`.
- Après avoir divisé le titre de l'article partout où il y a des espaces blancs, j'ai utilisé la méthode `join()` pour joindre les lettres individuelles de la chaîne avec un trait d'union.

## Conclusion

La méthode `String.prototype.replace()` est une méthode de chaîne puissante avec laquelle vous pouvez accomplir beaucoup de choses tout en travaillant avec des chaînes en JavaScript.

En plus de la méthode `String.prototype.replace()`, je vous ai également montré comment utiliser la méthode `String.prototype.replaceAll()` – un hybride de la méthode `String.prototype.replace()`.

Vous devez être prudent avec la méthode `String.prototype.replaceAll()` car elle n'est pas encore prise en charge par certains navigateurs. Au lieu d'utiliser `replaceAll()`, je vous ai également montré comment vous pouvez obtenir le même résultat en utilisant des expressions régulières pour rechercher toutes les valeurs dans une chaîne particulière.

Si vous trouvez cet article utile, n'hésitez pas à le partager avec vos amis et votre famille.

Merci d'avoir lu.