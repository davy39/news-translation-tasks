---
title: 10 Astuces JavaScript Que Tout Développeur Web Doit Connaître
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-12-21T21:57:53.000Z'
originalURL: https://freecodecamp.org/news/javascript-hacks
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fe0fdd6e6787e0983941991.jpg
tags:
- name: JavaScript
  slug: javascript
- name: optimization
  slug: optimization
- name: Productivity
  slug: productivity
- name: Web Development
  slug: web-development
seo_title: 10 Astuces JavaScript Que Tout Développeur Web Doit Connaître
seo_desc: 'By Gert Svaiko

  If you optimize your JavaScript code with these hacks, it can help you write cleaner
  code, save resources, and optimize your programming time.

  According to RedMonk, JavaScript is the most popular programming language. Furthermore,
  Slas...'
---

Par Gert Svaiko

Si vous optimisez votre code JavaScript avec ces astuces, cela peut vous aider à écrire un code plus propre, économiser des ressources et optimiser votre temps de programmation.

Selon [RedMonk](https://redmonk.com/sogrady/2020/07/27/language-rankings-6-20/), JavaScript est le langage de programmation le plus populaire. De plus, SlashData estime qu'environ [12,4 millions de développeurs](https://www.slashdata.co/free-resources/developer-economics-state-of-the-developer-nation-19th-edition?) utilisent JavaScript, ce qui inclut également CoffeeScript et TypeScript de Microsoft.

Cela signifie que des millions de personnes utilisent JavaScript pour travailler en tant que programmeurs, prendre des missions freelance via des sites comme [UpWork](https://www.upwork.com/freelance-jobs/javascript/) et [Freelancer](https://www.freelancer.com/jobs/javascript/), ou même lancer leur propre [entreprise de développement web](https://websitesetup.org/how-to-get-web-design-clients/).

freeCodeCamp propose un excellent [cours de base](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-javascript/) sur JavaScript. Mais, si vous êtes déjà familier avec les fondamentaux et souhaitez améliorer votre maîtrise de JavaScript, voici dix astuces que vous devriez apprendre et intégrer à votre flux de travail.

## 1. Comment Utiliser des Raccourcis pour les Conditionnelles

JavaScript vous permet d'utiliser certains raccourcis pour rendre votre code plus lisible. Dans certains cas simples, vous pouvez utiliser les opérateurs logiques `&&` et `||` au lieu de `if` et `else`.

Regardons l'opérateur `&&` en action.

Exemple de code :

```js
// au lieu de
if (accessible) {
  console.log("C'est ouvert !");
}

// utilisez
accessible && console.log("C'est ouvert !");
```

L'opérateur `||` fonctionne comme une clause "ou". Cependant, utiliser cet opérateur est un peu plus délicat car il peut empêcher l'application de s'exécuter. Mais nous pouvons ajouter une condition pour contourner cela.

Exemple de code :

```js
// au lieu de
if (price.data) {
  return price.data;
} else {
  return 'Récupération du prix';
}

// utilisez
return (price.data || 'Récupération du prix');
```

## 2. Comment Convertir en le Plus Grand Entier en Utilisant l'Opérateur ~~

Utiliser `Math.floor` pour retourner le plus grand entier inférieur ou égal à un nombre donné dans l'équation consomme des ressources, sans compter que c'est une chaîne assez longue à retenir. Une méthode plus efficace consiste à utiliser l'opérateur `~~`.

Voici un exemple :

```js
// au lieu de
Math.floor(Math.random() * 50);

// utilisez
~~(Math.random() * 50);

// Vous pouvez également utiliser l'opérateur ~~ pour convertir n'importe quoi en une valeur numérique.
// Exemple de code :
~~('whitedress') // retourne 0
~~(NaN) // retourne 0
```

## 3. Redimensionner ou Vider un Tableau en Utilisant array.length

Parfois, vous devez ajuster la taille de votre tableau ou le vider. La méthode la plus efficace pour cela est d'utiliser `Array.length`.

Exemple de code :

```js
let array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'];

console.log(array.length); // retourne la longueur comme 10

array.length = 4;

console.log(array.length); // retourne la longueur comme 4
console.log(array); // retourne ['a', 'b', 'c', 'd']
```

Vous pouvez également utiliser `Array.length` pour supprimer toutes les valeurs d'un tableau spécifié.

Exemple de code :

```js
let array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'];

array.length = 0;

console.log(array.length); // retourne la longueur comme 0
console.log(array); // retourne []
```

## 4. Comment Fusionner des Tableaux Sans Provoquer de Surcharge du Serveur

Fusionner des tableaux peut représenter une charge sérieuse pour le serveur, surtout si vous manipulez de grands ensembles de données. Pour garder les choses simples et maintenir les niveaux de performance, utilisez les fonctions `Array.concat()` et `Array.push.apply(arr1, arr2)`.

L'utilisation de l'une ou l'autre de ces fonctions dépend de la taille de vos tableaux.

Voyons comment gérer les petits tableaux.

Exemple de code :

```js
let list1 = ['a', 'b', 'c', 'd', 'e'];
let list2 = ['f', 'g', 'h', 'i', 'j'];

console.log(list1.concat(list2)); // retourne les valeurs fusionnées des deux tableaux, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
```

Lorsque vous utilisez la fonction `Array.concat()` sur de grands ensembles de données, elle consomme beaucoup de mémoire tout en créant un nouveau tableau. Pour éviter la baisse de performance, utilisez `Array.push.apply(arr1, arr2)` qui consolide le deuxième tableau dans le premier sans créer de nouveau tableau.

Exemple de code :

```js
let list1 = ['a', 'b', 'c', 'd', 'e'];
let list2 = ['f', 'g', 'h', 'i', 'j'];

console.log(list1.push.apply(list1, list2)); // retourne 10, la nouvelle longueur de list1
console.log(list1); // retourne ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
```

## 5. Comment Utiliser des Filtres avec des Tableaux

Filtrer un tableau est utile lorsque vous travaillez avec plusieurs colonnes de données correspondantes. Dans ce cas, vous pouvez inclure et exclure des données en fonction de toute caractéristique décrivant un groupe dans votre tableau.

Pour filtrer un tableau, utilisez la fonction `filter()`.

Exemple de code :

```js
const cars = [
  { make: 'Opel', class: 'Regular' },
  { make: 'Bugatti', class: 'Supercar' },
  { make: 'Ferrari', class: 'Supercar' },
  { make: 'Ford', class: 'Regular' },
  { make: 'Honda', class: 'Regular' },
]
const supercar = cars.filter(car => car.class === 'Supercar');
console.table(supercar); // retourne les données de la classe supercar dans un format de tableau
```

Vous pouvez également utiliser `filter()` avec `Boolean` pour supprimer toutes les valeurs `null` ou `undefined` de votre tableau.

Exemple de code :

```js
const cars = [
  { make: 'Opel', class: 'Regular' },
  null,
  undefined
]

cars.filter(Boolean); // retourne [{ make: 'Opel', class: 'Regular' }] 
```

## 6. Comment Extraire des Valeurs Uniques

Supposons que vous avez un ensemble de données avec des valeurs répétées, et que vous devez produire des valeurs uniques à partir de cet ensemble. Vous pouvez le faire avec une combinaison de la syntaxe de décomposition `...` et du type d'objet `Set`. Cette approche fonctionne à la fois avec des mots et des nombres.

Exemple de code :

```js
const cars = ['Opel', 'Bugatti', 'Opel', 'Ferrari', 'Ferrari', 'Opel'];
const unrepeated_cars = [...new Set(cars)];

console.log(unrepeated_cars); // retourne les valeurs Opel, Bugatti, Ferrari
```

## 7. Comment Utiliser le Raccourci de la Fonction Remplacer

Vous devriez être familier avec la fonction `String.replace()`. Cependant, elle ne remplace une chaîne qu'avec une ligne spécifiée une fois et s'arrête là. Supposons que vous avez un ensemble de données plus grand, et que vous devez taper cette fonction plusieurs fois. Cela devient frustrant après un moment.

Pour faciliter votre vie, vous pouvez ajouter `/g` à la fin de l'expression régulière, afin que la fonction s'exécute et remplace toutes les conditions correspondantes sans s'arrêter à la première.

Exemple de code :

```js
const grammar = 'synonym synonym';

console.log(grammar.replace(/syno/, 'anto')); // cela retourne 'antonym synonym'
console.log(grammar.replace(/syno/g, 'anto')); // cela retourne 'antonym antonym'
```

## 8. Comment Mettre en Cache des Valeurs

Lorsque vous travaillez avec de grands tableaux et que vous devez demander des éléments par ID en utilisant `getElementById()`, ou par nom de classe en utilisant `getElementsByClassName()`, JavaScript parcourt le tableau en boucle avec chaque demande d'élément similaire. Cela peut consommer beaucoup de ressources.

Cependant, vous pouvez augmenter les performances en mettant en cache une valeur si vous savez que vous utilisez régulièrement une sélection spécifiée.

Exemple de code :

```js
const carSerial = serials.getElementById('serial1234');
carSerial.addClass('cached-serial1234');
```

## 9. Comment Vérifier si un Objet Contient des Valeurs

Lorsque vous travaillez avec plusieurs objets, il devient difficile de garder une trace de ceux qui contiennent des valeurs réelles et de ceux que vous pouvez supprimer.

Voici une astuce rapide pour vérifier si un objet est vide ou contient une valeur avec la fonction `Object.keys()`.

Exemple de code :

```js
Object.keys(objectName).length // si cela retourne 0 alors l'objet est vide, sinon cela affiche le nombre de valeurs
```

## 10. Comment Minifier vos Fichiers JavaScript

Les grands fichiers JS affectent les performances de chargement et de réponse de votre page. Lors de l'écriture de votre code, vous pouvez vous retrouver avec des lignes inutiles, des commentaires et du code mort. Selon la taille de votre fichier, cela peut s'accumuler et devenir un goulot d'étranglement redondant.

Il existe quelques outils pour vous aider à nettoyer le code et rendre les fichiers JS plus légers - ou les minifier, en termes de développeurs. Même si la minification du fichier JS n'est pas une astuce à proprement parler, il est toujours bénéfique pour les développeurs de le savoir et de l'implémenter.

L'un d'eux est [Google Closure Compiler](https://developers.google.com/closure/compiler), qui analyse votre JavaScript, l'analyse, supprime le code mort, et réécrit et minimise ce qui reste. L'autre est [Microsoft Ajax Minifier](https://archive.codeplex.com/?p=ajaxmin), qui vous permet d'améliorer les performances de votre application web en réduisant la taille de vos fichiers JavaScript.

Voilà. Utilisez ces dix astuces pour rendre votre code plus propre, économiser les ressources du serveur et gagner du temps de programmation.

### Merci d'avoir lu !

Je suis un écrivain passionné par le marketing numérique, le développement web et la cybersécurité. Vous pouvez me contacter sur [LinkedIn ici](https://www.linkedin.com/in/gert-svaiko/).

Vous pourriez également apprécier d'autres articles que j'ai écrits :

* [The Google page experience: What you need to know and five steps to prepare for 2021](https://www.searchenginewatch.com/2020/12/01/the-google-page-experience-what-you-need-to-know-and-five-steps-for-2021/)
* [Web Hosting Security Threats to Watch Out for During This Season](https://www.infosecurity-magazine.com/next-gen-infosec/web-hosting-threats-season/)
* [How to boost sales during the rest of 2020's unusual holiday season](https://www.digitalcommerce360.com/2020/12/08/how-to-boost-sales-during-the-rest-of-2020s-unusual-holiday-season/)