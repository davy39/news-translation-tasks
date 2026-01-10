---
title: Format de chaîne JavaScript – Comment utiliser l'interpolation de chaînes en
  JS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-08T19:27:43.000Z'
originalURL: https://freecodecamp.org/news/javascript-string-format-how-to-use-string-interpolation-in-js
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c98d0740569d1a4ca1c2f.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Format de chaîne JavaScript – Comment utiliser l'interpolation de chaînes
  en JS
seo_desc: "By Catalin Pit\nThe addition of template literals in ECMAScript 6 (ES6)\
  \ allows us to interpolate strings in JavaScript. \nIn simpler words, we can use\
  \ placeholders to inject variables into a string. You can see an example of string\
  \ interpolation using ..."
---

Par Catalin Pit

L'ajout des littéraux de gabarit dans ECMAScript 6 (ES6) nous permet d'interpoler des chaînes en JavaScript. 

En termes plus simples, nous pouvons utiliser des espaces réservés pour injecter des variables dans une chaîne. Vous pouvez voir un exemple d'interpolation de chaînes utilisant des littéraux de gabarit dans l'extrait ci-dessous :

```js
const age = 4.5;
const earthAge = `La Terre est estimée à ${age} milliards d'années.`;

console.log(earthAge);

```

Tout d'abord, vous remarquerez que nous utilisons des backticks pour les littéraux de gabarit. En outre, nous avons le format `${placeholder}`, qui nous permet d'insérer une valeur dynamique dans la chaîne. Tout ce qui se trouve à l'intérieur de `${}` est évalué comme du JavaScript. 

Par exemple, nous pourrions écrire `La Terre est estimée à ${age + 10} milliards d'années.`, et cela fonctionnerait comme si nous avions fait `const age = 4.5 + 10;`.

### Comment faisions-nous avant ? 

Avant les littéraux de gabarit, nous aurions fait comme ceci :

```js
const earthAge = "La Terre est estimée à " + age + " milliards d'années.";

```

Comme vous pouvez le voir, nous avons déjà beaucoup de guillemets pour une simple chaîne. Imaginez que nous devons insérer plusieurs variables. Cela peut rapidement se transformer en une chaîne complexe qui n'est pas très lisible. Ainsi, les littéraux de gabarit rendent les chaînes plus propres et plus lisibles.

Cependant, ce n'est qu'un seul cas. Voyons d'autres cas d'utilisation pour les littéraux de gabarit.

## Chaînes multi-lignes

Une autre utilisation pratique des chaînes de gabarit est les chaînes multi-lignes. Avant les littéraux de gabarit, nous utilisions `\n` pour les nouvelles lignes, comme dans `console.log('ligne 1\n' + 'ligne 2')`. 

Pour deux lignes, cela peut être acceptable. Mais imaginez que nous voulons cinq lignes. Encore une fois, la chaîne devient inutilement complexe.

```js
const earthAge = `La Terre est estimée à ${age} milliards d'années.

Les scientifiques ont sillonné la Terre à la recherche des plus anciennes roches à dater par radiométrie.

Dans le nord-ouest du Canada, ils ont découvert des roches âgées d'environ 4,03 milliards d'années.
`;

```

L'extrait ci-dessus démontre une fois de plus à quel point il devient simple et propre d'écrire des chaînes multi-lignes avec des littéraux de gabarit. 

En guise d'exercice, essayez de convertir la chaîne ci-dessus pour utiliser la concaténation et les nouvelles lignes `\n`.

## Expressions

Avec les littéraux de gabarit, nous pouvons également utiliser des expressions dans les chaînes. Que signifie cela ? 

Par exemple, nous pourrions utiliser des expressions mathématiques telles que multiplier deux nombres. L'extrait ci-dessous illustre cela :

```js
const firstNumber = 10;
const secondNumber = 39;
const result = `Le résultat de la multiplication de ${firstNumber} par ${secondNumber} est ${firstNumber * secondNumber}.`;

console.log(result);

```

Sans les littéraux de gabarit, nous aurions dû faire quelque chose comme ceci :

```js
const result = "Le résultat de la multiplication de " + firstNumber + " par " + secondNumber + " est " + firstNumber * secondNumber + ".";

```

Écrire une chaîne comme celle ci-dessus peut rapidement devenir complexe et confus. Comme nous le voyons, les littéraux de gabarit rendent plus facile et plus élégant l'intégration d'expressions dans la chaîne.

## Opérateur ternaire

Avec l'interpolation de chaînes, nous pouvons même utiliser un opérateur ternaire à l'intérieur d'une chaîne. Cela nous permet de vérifier la valeur d'une variable et d'afficher différentes choses en fonction de cette valeur. 

Regardons l'exemple ci-dessous :

```js
const drinks = 4.99;
const food = 6.65;
const total = drinks + food;

const result = `Le total de la facture est ${total}. ${total > 10 ? `Votre paiement par carte sera refusé` : `Votre paiement par carte sera accepté`}.`

console.log(result);

```

Dans l'exemple ci-dessus, nous vérifions si le montant total est supérieur à dix dollars, par exemple. 

Si le montant est supérieur à dix, nous informons l'utilisateur que le paiement par carte sera refusé. Sinon, le paiement par carte est accepté. Comme vous pouvez le voir, l'interpolation de chaînes nous permet de faire des choses intéressantes avec les chaînes.

# Conclusion

L'ajout des littéraux de gabarit dans ES6 nous permet d'écrire des chaînes meilleures, plus courtes et plus claires. Cela nous donne également la possibilité d'injecter des variables et des expressions dans n'importe quelle chaîne. Essentiellement, tout ce que vous écrivez à l'intérieur des accolades (`${}`) est traité comme du JavaScript.

Ainsi, nous pouvons utiliser les littéraux de gabarit pour :

* écrire des chaînes multi-lignes
* intégrer des expressions
* écrire des chaînes avec l'opérateur ternaire

Merci d'avoir lu ! Si vous souhaitez rester en contact, connectons-nous sur Twitter [@catalinmpit](https://twitter.com/intent/follow?screen_name=catalinmpit). Je publie également régulièrement des articles sur mon blog [catalins.tech](https://catalins.tech) si vous souhaitez lire plus de contenu de ma part.