---
title: Que signifie $ en JavaScript ? Opérateur du symbole dollar en JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2023-04-14T15:10:37.000Z'
originalURL: https://freecodecamp.org/news/what-does-the-dollar-sign-mean-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/cover-template--9-.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Que signifie $ en JavaScript ? Opérateur du symbole dollar en JS
seo_desc: 'As you dive into JavaScript code, you may come across the use of a dollar
  sign ($) in various contexts.

  In this article, we will explore what the dollar sign means in JavaScript, commonly
  known as the "dollar sign operator," and how it is used in Jav...'
---

Lorsque vous plongez dans le code JavaScript, vous pouvez rencontrer l'utilisation d'un symbole dollar ($) dans divers contextes.

Dans cet article, nous allons explorer ce que signifie le symbole dollar en JavaScript, communément appelé "opérateur du symbole dollar", et comment il est utilisé en programmation JavaScript.

## Comprendre l'opérateur du symbole dollar

En JavaScript, le symbole dollar n'est pas un opérateur ou une syntaxe intégrée. Il n'a aucune signification ou fonctionnalité prédéfinie dans le langage JavaScript lui-même.

Au lieu de cela, il est souvent utilisé comme une convention dans les bibliothèques, les frameworks et d'autres codes JavaScript écrits par les développeurs pour diverses raisons. Examinons de plus près quelques cas d'utilisation courants du symbole dollar en JavaScript.

### 1. Utilisation du `$` dans la bibliothèque jQuery

L'une des utilisations les plus connues du symbole dollar en JavaScript est avec la bibliothèque jQuery.

Dans jQuery, le symbole dollar est utilisé comme un alias raccourci pour l'objet `jQuery`. jQuery est une bibliothèque JavaScript puissante qui simplifie la manipulation du DOM et fournit une large gamme de fonctions utilitaires pour le développement web.

Par exemple, vous pouvez voir du code comme ceci :

```js
// Utilisation de l'alias $ pour sélectionner des éléments avec jQuery
$('#myElement').addClass('active');
```

Dans cet exemple, `$` est utilisé comme un raccourci pour l'objet `jQuery`, ce qui vous permet de sélectionner un élément avec l'ID `myElement` et d'ajouter la classe CSS `active` à celui-ci.

Mais il est important de noter que l'utilisation du symbole dollar comme alias pour `jQuery` n'est pas obligatoire, et vous pouvez également utiliser le mot-clé `jQuery` à la place.

### 2. Utilisation du `$` dans d'autres bibliothèques et frameworks JavaScript

En dehors de jQuery, certaines autres bibliothèques et frameworks JavaScript peuvent également utiliser le symbole dollar comme une convention pour leurs propres besoins spécifiques.

Par exemple, dans AngularJS, vous pouvez voir du code comme ceci :

```js
// Utilisation de l'objet $scope dans AngularJS
$scope.name = 'John';
```

Dans cet exemple, `$scope` est un objet prédéfini dans AngularJS qui est utilisé pour lier les données entre la vue et le contrôleur.

Il est important de noter que l'utilisation du symbole dollar dans ces bibliothèques et frameworks est spécifique à leur syntaxe et leurs API respectives, et peut ne pas avoir la même signification ou fonctionnalité dans d'autres contextes.

### 3. Utilisation du `$` dans les littéraux de gabarit

En plus de ces cas d'utilisation, le symbole dollar est également utilisé dans les littéraux de gabarit. Cela a été introduit dans ECMAScript 6 (ES6) pour une interpolation de chaînes et des chaînes multilingues plus pratiques en JavaScript.

Les littéraux de gabarit sont enfermés dans des backticks (`` ` ``) au lieu de guillemets simples ou doubles. Ils vous permettent d'intégrer des expressions directement dans la chaîne à l'aide de placeholders, désignés par `${expression}`. Le symbole dollar suivi d'accolades `${}` est utilisé pour évaluer et intégrer des expressions dynamiquement dans les littéraux de gabarit.

```js
const name = 'John Doe';
const age = 20;

// Utilisation des littéraux de gabarit pour l'interpolation de chaînes
console.log(`Mon nom est ${name} et j'ai ${age} ans.`);
```

Dans cet exemple, les expressions `${name}` et `${age}` sont évaluées et remplacées par leurs valeurs correspondantes dans la chaîne résultante. Cela permet une concaténation de chaînes facile et lisible avec des variables.

## Conclusion

En JavaScript, le symbole dollar n'est pas un opérateur ou une syntaxe prédéfinie, mais il est couramment utilisé comme une convention dans les bibliothèques, les frameworks et le code personnalisé pour diverses raisons.

Il est utilisé comme un alias raccourci pour les objets ou les fonctions dans certaines bibliothèques et frameworks, et il est également utilisé dans les littéraux de gabarit pour l'interpolation de chaînes et les chaînes multilingues.

Il est important de comprendre que l'utilisation du symbole dollar peut avoir différentes significations ou fonctionnalités dans différents contextes, et il est toujours recommandé de suivre les normes de codage et les meilleures pratiques pour écrire du code JavaScript propre, maintenable et lisible.

Amusez-vous bien en codant !

Embarquez pour un voyage d'apprentissage ! [Parcourez plus de 200 articles d'experts sur le développement web](https://joelolawanle.com/contents). Consultez [mon blog](https://joelolawanle.com/posts) pour plus de contenu captivant de ma part !