---
title: Astuces pour créer des tableaux JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-18T22:59:31.000Z'
originalURL: https://freecodecamp.org/news/https-medium-com-gladchinda-hacks-for-creating-javascript-arrays-a1b80cb372b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Ikt9LNJUhCX7QxbjnwKstA.png
tags:
- name: ES6
  slug: es6
- name: hacks
  slug: hacks
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Astuces pour créer des tableaux JavaScript
seo_desc: 'By Glad Chinda

  Insightful tips for creating and cloning arrays in JavaScript.


  _Original Photo by [Unsplash](https://unsplash.com/photos/FXFz-sW0uwo?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
  rel="noopener" target="_blank" ti...'
---

Par Glad Chinda

#### Conseils judicieux pour créer et cloner des tableaux en JavaScript.

![Image](https://cdn-media-1.freecodecamp.org/images/IH842JnVoctZM6QoKOfXQe8luuYHXHjMuNxf)
_Photo originale par [Unsplash](https://unsplash.com/photos/FXFz-sW0uwo?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Markus Spiske</a> sur <a href="https://unsplash.com/search/photos/code?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Un aspect très important de chaque langage de programmation est les types de données et les structures disponibles dans le langage. La plupart des langages de programmation fournissent des types de données pour représenter et travailler avec des données complexes. Si vous avez travaillé avec des langages comme Python ou Ruby, vous devriez avoir vu des types de données comme les **listes**, **ensembles**, **tuples**, **hashes**, **dictionnaires**, et ainsi de suite.

En JavaScript, il n'y a pas autant de types de données complexes — vous avez simplement des **tableaux** et des **objets**. Cependant, dans ES6, plusieurs types de données et structures ont été ajoutés au langage, tels que les **symboles**, **ensembles**, et **maps**.

> _Les tableaux en JavaScript sont des objets de type liste de haut niveau avec une propriété de longueur et des propriétés entières comme index._

Dans cet article, je partage quelques astuces pour créer de nouveaux tableaux JavaScript ou cloner des tableaux déjà existants.

### Création de tableaux : Le constructeur Array

La méthode la plus populaire pour créer des tableaux est d'utiliser la syntaxe **littérale de tableau**, qui est très simple. Cependant, lorsque vous souhaitez créer des tableaux dynamiquement, la syntaxe littérale de tableau peut ne pas toujours être la meilleure méthode. Une méthode alternative est d'utiliser le constructeur `Array`.

Voici un simple extrait de code montrant l'utilisation du constructeur `Array`.

<script src="https://gist.github.com/gladchinda/fe7eee22be4cd4722d3e0099fadd3919.js"></script>

D'après l'extrait précédent, nous pouvons voir que le constructeur `Array` crée des tableaux différemment selon les arguments qu'il reçoit.

### Nouveaux tableaux : Avec une longueur définie

Examinons de plus près ce qui se passe lors de la création d'un nouveau `Array` d'une longueur donnée. Le constructeur définit simplement la propriété `length` du tableau à la longueur donnée, sans définir les clés.

![Image](https://cdn-media-1.freecodecamp.org/images/HuAR3m0WmxP390Ezk4Ufyam-9vlyDzwNvEzi)

D'après l'extrait ci-dessus, vous pourriez être tenté de penser que chaque clé du tableau a été définie à une valeur `undefined`. Mais la réalité est que ces clés n'ont jamais été définies (elles n'existent pas).

L'illustration suivante rend cela plus clair :

![Image](https://cdn-media-1.freecodecamp.org/images/wtfHBQo1MBofKp-EVs-IB6qqq07cfM18rK8I)

Cela rend inutile toute tentative d'utiliser l'une des méthodes d'itération de tableau telles que `map()`, `filter()` ou `reduce()` pour manipuler le tableau. Supposons que nous voulons remplir chaque index du tableau avec le nombre `5` comme valeur. Nous tenterons ce qui suit :

![Image](https://cdn-media-1.freecodecamp.org/images/1OHTGXHuG93TuWcOpzRVtUNjoB-BFP3Pykq5)

Nous pouvons voir que `map()` n'a pas fonctionné ici, car les propriétés d'index n'existent pas sur le tableau — seule la propriété `length` existe.

Voyons différentes façons de résoudre ce problème.

#### 1. Utilisation de Array.prototype.fill()

La méthode `**fill()**` remplit tous les éléments d'un tableau d'un index de début à un index de fin avec une valeur statique. L'index de fin n'est pas inclus. Vous pouvez en apprendre plus sur `fill()` [ici](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/fill).

**Notez que `fill()` ne fonctionnera que dans les navigateurs avec support ES6.**

Voici une simple illustration :

![Image](https://cdn-media-1.freecodecamp.org/images/w3CWlvnWqG5VEy6qupnAYvTqECGhPdj3P9Wu)

Ici, nous avons pu remplir tous les éléments de notre tableau créé avec `5`. Vous pouvez définir n'importe quelle valeur statique pour différents index du tableau en utilisant la méthode `fill()`.

#### 2. Utilisation de Array.from()

La méthode `**Array.from()**` crée une nouvelle instance de `Array`, copiée en surface, à partir d'un objet de type tableau ou itérable. Vous pouvez en apprendre plus sur `Array.from()` [ici](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/from).

**Notez que `Array.from()` ne fonctionnera que dans les navigateurs avec support ES6.**

Voici une simple illustration :

![Image](https://cdn-media-1.freecodecamp.org/images/XfZGhDWQWU1VwxliMKIjYgHuwYvkfvPSBkVT)

Ici, nous avons maintenant de vraies valeurs `undefined` définies pour chaque élément du tableau en utilisant `Array.from()`. Cela signifie que nous pouvons maintenant utiliser des méthodes comme `.map()` et `.filter()` sur le tableau, puisque les propriétés d'index existent désormais.

Une autre chose à noter à propos de `Array.from()` est qu'elle peut prendre un deuxième argument, qui est une **fonction de mappage**. Elle sera appelée sur chaque élément du tableau. Cela rend redondant l'appel de `.map()` après `Array.from()`.

Voici un simple exemple :

![Image](https://cdn-media-1.freecodecamp.org/images/UgaAHFIo4xzuw4cc4bI1iaxaPzGHKkTCbjYK)

#### 3. Utilisation de l'opérateur de décomposition

L'**opérateur de décomposition** (`...`), ajouté dans ES6, peut être utilisé pour décomposer les éléments du tableau, en définissant les éléments manquants à une valeur `undefined`. Cela produira le même résultat que simplement appeler `Array.from()` avec le tableau comme seul argument.

Voici une simple illustration de l'utilisation de l'opérateur de décomposition :

![Image](https://cdn-media-1.freecodecamp.org/images/gZrwaPsFq15WkPf2BnuAb2wA54JdIEXx7VNv)

Vous pouvez maintenant utiliser des méthodes comme `.map()` et `.filter()` sur le tableau, puisque les propriétés d'index existent désormais.

### Utilisation de Array.of()

Tout comme nous l'avons vu avec la création de nouveaux tableaux en utilisant le constructeur ou la fonction `Array`, `**Array.of()**` se comporte de manière très similaire. En fait, la seule différence entre `Array.of()` et `Array` est la manière dont ils gèrent un argument entier unique passé.

Alors que `**Array.of(5)**` crée un nouveau tableau avec un seul élément, `5`, et une propriété de longueur de `1`, `**Array(5)**` crée un nouveau tableau vide avec 5 emplacements vides et une propriété de longueur de `5`.

```js
var array1 = Array.of(5); // [5]
var array2 = Array(5); // Array(5) {length: 5}
```

Outre cette différence majeure, `Array.of()` se comporte exactement comme le constructeur `Array`. Vous pouvez en apprendre plus sur `Array.of()` [ici](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/of).

**Notez que `Array.of()` ne fonctionnera que dans les navigateurs avec support ES6.**

### Conversion en tableaux : Objets de type tableau et itérables

Si vous avez écrit des fonctions JavaScript depuis suffisamment longtemps, vous devriez déjà connaître l'objet `arguments` — qui est un objet de type **tableau** disponible dans chaque fonction pour contenir la liste des arguments que la fonction a reçus. Bien que l'objet `arguments` ressemble beaucoup à un tableau, il n'a pas accès aux méthodes `Array.prototype`.

Avant ES6, vous verriez généralement un extrait de code comme celui-ci lorsque vous essayez de convertir l'objet `arguments` en un tableau :

![Image](https://cdn-media-1.freecodecamp.org/images/NaMaYAla-PzcPacVZGr3E03twovKgKTuRVwm)

Avec `Array.from()` ou l'opérateur de décomposition, vous pouvez facilement convertir tout objet de type tableau en un tableau. Ainsi, au lieu de faire ceci :

```
var args = Array.prototype.slice.call(arguments);
```

vous pouvez faire l'une de ces deux choses :

```js
// Utilisation de Array.from()
var args = Array.from(arguments);

// Utilisation de l'opérateur de décomposition
var args = [...arguments];
```

Cela s'applique également aux **itérables** comme le montre l'illustration suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/87TEnXS9-qV7Lak1XBBcEYiQVvh96FqXDJXc)

### Étude de cas : Fonction Range

Avant de continuer, nous allons créer une simple fonction `**range()**` pour implémenter le nouveau **hack de tableau** que nous venons d'apprendre. La fonction a la signature suivante :

```js
range(start: number, end: number, step: number) => Array<number>
```

Voici l'extrait de code :

<script src="https://gist.github.com/gladchinda/439981b34aa8f23c661e9663edf762f0.js"></script>

Dans cet extrait de code, nous avons utilisé `Array.from()` pour créer le nouveau tableau de plage de longueur dynamique, puis l'avons peuplé de nombres incrémentés séquentiellement en fournissant une fonction de mappage.

**Notez que l'extrait de code ci-dessus ne fonctionnera pas pour les navigateurs sans support ES6 sauf si vous utilisez des polyfills.**

Voici quelques résultats de l'appel de la fonction `**range()**` définie dans l'extrait de code ci-dessus :

![Image](https://cdn-media-1.freecodecamp.org/images/zFBQwh8KfkoDDWXcZDl8YnDe7e9jBEsocdCa)

Vous pouvez obtenir une démonstration de code en direct en exécutant le pen suivant sur **Codepen** :

<iframe height="500" width="500" style="width: 100%;" scrolling="no" title="QxeXzm" src="//codepen.io/gladchinda/embed/QxeXzm/?height=265&theme-id=0&default-tab=js,result" frameborder="no" allowtransparency="true" allowfullscreen="true">
  See the Pen <a href='https://codepen.io/gladchinda/pen/QxeXzm/'>QxeXzm</a> by Glad Chinda
  (<a href='https://codepen.io/gladchinda'>@gladchinda</a>) on <a href='https://codepen.io'>CodePen</a>.
</iframe>

### Clonage de tableaux : Le défi

En JavaScript, les tableaux et les objets sont des types de référence. Cela signifie que lorsqu'une variable est assignée à un tableau ou un objet, ce qui est assigné à la variable est une référence à l'emplacement en mémoire où le tableau ou l'objet a été stocké.

Les tableaux, comme tout autre objet en JavaScript, sont des types de référence. **Cela signifie que les tableaux sont copiés par référence et non par valeur.**

Stocker des types de référence de cette manière a les conséquences suivantes :

#### **1. Les tableaux similaires ne sont pas égaux.**

![Image](https://cdn-media-1.freecodecamp.org/images/brYlg3Dp3gVRqGqHGkMBR2XR7eLvWQK8xymc)

Ici, nous voyons que bien que `array1` et `array2` contiennent des spécifications de tableau apparemment identiques, ils ne sont pas égaux. Cela est dû au fait que la référence à chacun des tableaux pointe vers un emplacement différent en mémoire.

#### **2. Les tableaux sont copiés par référence et non par valeur.**

![Image](https://cdn-media-1.freecodecamp.org/images/PZF-lU5f4C-OWkNLeF-q4g9T2anP6k88PPr1)

Ici, nous tentons de copier `array1` vers `array2`, mais ce que nous faisons en réalité est de pointer `array2` vers le même emplacement en mémoire que `array1`. Par conséquent, `array1` et `array2` pointent vers le même emplacement en mémoire et sont égaux.

L'implication de cela est que lorsque nous apportons une modification à `array2` en supprimant le dernier élément, le dernier élément de `array1` est également supprimé. Cela est dû au fait que la modification a été apportée au tableau stocké en mémoire, tandis que `array1` et `array2` sont simplement des pointeurs vers cet emplacement en mémoire où le tableau est stocké.

### Clonage de tableaux : Les astuces

#### **1. Utilisation de Array.prototype.slice()**

La méthode `**slice()**` crée une copie superficielle d'une portion d'un tableau sans modifier le tableau. Vous pouvez en apprendre plus sur `slice()` [ici](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice).

L'astuce est d'appeler `slice()` soit avec `0` comme seul argument, soit sans aucun argument du tout :

```js
// avec 0 comme seul argument
array.slice(0);

// sans argument
array.slice();
```

Voici une simple illustration du clonage d'un tableau avec `slice()` :

![Image](https://cdn-media-1.freecodecamp.org/images/-XUoysUS92IrVW9lYY6EkJHXv8vKw0yahdaW)

Ici, vous pouvez voir que `array2` est un clone de `array1` avec les mêmes éléments et la même longueur. Cependant, ils pointent vers différents emplacements en mémoire, et par conséquent ne sont pas égaux. Vous remarquez également que lorsque nous apportons une modification à `array2` en supprimant le dernier élément, `array1` reste inchangé.

#### **2. Utilisation de Array.prototype.concat()**

La méthode `**concat()**` est utilisée pour fusionner deux tableaux ou plus, résultant en un nouveau tableau, tandis que les tableaux originaux restent inchangés. Vous pouvez en apprendre plus sur `concat()` [ici](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/concat).

L'astuce est d'appeler `concat()` soit avec un tableau vide (`[]`) comme argument, soit sans aucun argument du tout :

```js
// avec un tableau vide
array.concat([]);

// sans argument
array.concat();
```

Le clonage d'un tableau avec `concat()` est assez similaire à l'utilisation de `slice()`. Voici une simple illustration du clonage d'un tableau avec `concat()` :

![Image](https://cdn-media-1.freecodecamp.org/images/OXjY30kwODk5622BQraHtZfHxN5d5gewTeZj)

#### 3. Utilisation de Array.from()

Comme nous l'avons vu précédemment, `**Array.from()**` peut être utilisé pour créer un nouveau tableau qui est une copie superficielle du tableau original. Voici une simple illustration :

![Image](https://cdn-media-1.freecodecamp.org/images/kS-1uaQbt9K6zFk4PZWfmnLXHADDnHaVqELf)

#### 4. Utilisation de la déstructuration de tableau

Avec ES6, nous avons des outils plus puissants dans notre boîte à outils tels que la **déstructuration**, l'**opérateur de décomposition**, les **fonctions fléchées**, et ainsi de suite. La déstructuration est un outil très puissant pour extraire des données de types complexes comme les tableaux et les objets.

L'astuce est d'utiliser une technique appelée **paramètres rest**, qui implique une combinaison de déstructuration de tableau et de l'opérateur de décomposition comme le montre l'extrait suivant :

```js
let [...arrayClone] = originalArray;
```

L'extrait ci-dessus crée une variable nommée `arrayClone` qui est un clone de `originalArray`. Voici une simple illustration du clonage d'un tableau en utilisant la déstructuration de tableau :

![Image](https://cdn-media-1.freecodecamp.org/images/aohdaDoLpdH1XJ8Thk5U4JE7u0g89qsaTUcI)

# Clonage : Copie superficielle versus copie profonde

Toutes les techniques de clonage de tableau que nous avons explorées jusqu'à présent produisent une **copie superficielle** du tableau. Cela ne posera pas de problème si le tableau ne contient que des valeurs primitives. Cependant, si le tableau contient des références d'objets imbriqués, ces références resteront intactes même lorsque le tableau est cloné.

Voici une démonstration très simple de cela :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image.png)

Remarquez que la modification du tableau imbriqué dans `array1` a également modifié le tableau imbriqué dans `array2` et vice-versa.

La solution à ce problème est de créer une **copie profonde** du tableau et il existe plusieurs façons de le faire.

## 1. La technique JSON

La manière la plus simple de créer une copie profonde d'un tableau est d'utiliser une combinaison de `[**JSON.stringify()**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)` et `[**JSON.parse()**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse)`.

`JSON.stringify()` convertit une valeur JavaScript en une chaîne JSON valide, tandis que `JSON.parse()` convertit une chaîne JSON en une valeur ou un objet JavaScript correspondant.

Voici un exemple simple :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-1.png)

> La technique JSON présente certains défauts, notamment lorsque des valeurs autres que des chaînes, des nombres et des booléens sont impliquées.

Ces défauts dans la technique JSON peuvent être principalement attribués à la manière dont la méthode `JSON.stringify()` convertit les valeurs en chaîne JSON.

Voici une démonstration simple de ce défaut en essayant de `**JSON.stringify()**` une valeur contenant une fonction imbriquée.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-2.png)

## 2. Aide au clonage profond

Une alternative viable à la technique JSON serait d'implémenter votre propre **fonction d'aide au clonage profond** pour cloner les types de référence, qu'il s'agisse de tableaux ou d'objets.

Voici une fonction de clonage profond très simple et minimaliste appelée `**deepClone**` :

<script src="https://gist.github.com/gladchinda/75355e7f7992e800b5350c8c992df9b0.js"></script>

Ce n'est pas la meilleure des fonctions de clonage profond qui existe, comme vous le verrez bientôt avec certaines bibliothèques JavaScript — cependant, elle effectue un clonage profond à un niveau assez bon.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-3.png)

## 3. Utilisation de bibliothèques JavaScript

La fonction d'aide au clonage profond que nous venons de définir n'est pas assez robuste pour cloner tous les types de données JavaScript qui peuvent être imbriqués dans des objets ou des tableaux complexes.

Des bibliothèques JavaScript comme [**Lodash**](https://lodash.com/) et [**jQuery**](https://jquery.com/) fournissent des fonctions utilitaires de clonage profond plus robustes avec support pour différents types de données JavaScript.

Voici un exemple qui utilise `**_.cloneDeep()**` de la bibliothèque Lodash :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-4.png)

Voici le même exemple mais utilisant `**$.extend()**` de la bibliothèque jQuery :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-5.png)

### Conclusion

Dans cet article, nous avons pu explorer plusieurs techniques pour créer dynamiquement de nouveaux tableaux et cloner des tableaux déjà existants, y compris la conversion d'objets de type tableau et d'itérables en tableaux.

Nous avons également vu comment certaines des nouvelles fonctionnalités et améliorations introduites dans ES6 peuvent nous permettre d'effectuer certaines manipulations sur les tableaux de manière efficace.

Nous avons utilisé des fonctionnalités comme la déstructuration et l'opérateur de décomposition pour cloner et décomposer des tableaux. Vous pouvez en apprendre plus sur la déstructuration à partir de [cet article](https://codeburst.io/es6-destructuring-the-complete-guide-7f842d08b98f).

#### Applaudissements et Suivi

Si vous avez trouvé cet article perspicace, vous êtes libre de donner quelques applaudissements si cela ne vous dérange pas.

Vous pouvez également me suivre sur Medium ([Glad Chinda](https://www.freecodecamp.org/news/https-medium-com-gladchinda-hacks-for-creating-javascript-arrays-a1b80cb372b/undefined)) pour plus d'articles perspicaces que vous pourriez trouver utiles. Vous pouvez également me suivre sur Twitter ([@gladchinda](https://twitter.com/@gladchinda)).

**_Bon hacking…_**