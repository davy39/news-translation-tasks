---
title: Modules JavaScript – Expliqués avec des Exemples
subtitle: ''
author: Kingsley Ubah
co_authors: []
series: null
date: '2021-07-28T16:27:49.000Z'
originalURL: https://freecodecamp.org/news/javascript-modules-explained-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/what-is-a-module.png
tags:
- name: JavaScript
  slug: javascript
- name: modules
  slug: modules
- name: Web Development
  slug: web-development
seo_title: Modules JavaScript – Expliqués avec des Exemples
seo_desc: 'A module is a function or group of similar functions. They are grouped
  together within a file and contain the code to execute a specific task when called
  into a larger application.

  You create modules to better organize and structure your codebase. Yo...'
---

Un module est une fonction ou un groupe de fonctions similaires. Ils sont regroupés dans un fichier et contiennent le code pour exécuter une tâche spécifique lorsqu'ils sont appelés dans une application plus grande.

Vous créez des modules pour mieux organiser et structurer votre base de code. Vous pouvez les utiliser pour diviser de grands programmes en morceaux plus petits, plus faciles à gérer et plus indépendants, qui accomplissent une seule tâche ou quelques tâches liées.

Les modules doivent être :

1. **Indépendants/Autonomes** : Un module doit être aussi détaché que possible des autres dépendances.
   
2. **Spécifiques** : Un module doit pouvoir effectuer une seule tâche ou un groupe de tâches liées. L'essence même de leur création est de créer des fonctionnalités séparées. Un module, une (sorte de) tâche.
   
3. **Réutilisables** : Un module doit être facile à intégrer dans divers types de programmes pour accomplir sa tâche.

Pour mieux expliquer, laissez-moi vous donner une analogie :

Supposons que nous voulons construire une grande maison à partir de zéro. Tous les outils dont nous avons besoin pour installer le bâtiment sont entassés dans une seule pièce.

Dans une telle situation, organiser les outils de la bonne manière pour commencer à construire serait difficile.

Au lieu d'avoir les dépendances séparées entassées dans une seule pièce, nous devrions plutôt organiser chaque ensemble d'outils liés et les regrouper dans différentes pièces. Chaque pièce est indépendante et autonome avec ses outils résolvant des tâches spécifiques.

Nous pourrions mettre des étiquettes comme : **"ces outils sont pour la toiture"**, **"ces outils sont pour la pose de briques"**, **"ces outils sont pour le creusement des fondations"** et ainsi de suite.

Chaque fois que nous voulons un outil pour accomplir une tâche particulière, nous savons exactement dans quelle pièce le trouver. De cette manière, tout est beaucoup plus organisé et localisable.

De plus, disons que nous avons terminé de construire la maison et que nous décidons ensuite de construire quelque chose de différent. Nous aurons toujours à notre disposition le même ensemble d'outils. Cela renforce le principe de **réutilisabilité**. Les modules sont réutilisables car ils sont autonomes.

## Exemple d'un Module

Maintenant, dans le contexte du code, les modules sont très importants.

Considérons une illustration simplifiée de cela avec une application de commerce électronique qui permet aux particuliers et aux entreprises de vendre des produits en ligne. Ce programme sera généralement composé de deux tâches ou plus sans rapport. Par exemple,

* un programme pour créer un compte,
   
* un programme pour valider les informations,
   
* un autre programme pour traiter les paiements
   
* un autre programme pour calculer les évaluations des utilisateurs

et ainsi de suite.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/main-task.png align="left")

Au lieu d'avoir tous ces programmes sans rapport ensemble dans un seul module/fichier, il est préférable de créer plusieurs fichiers, ou modules, pour chacune de ces tâches. Dans un tel cas, les modules deviennent des dépendances.

Ensuite, à partir de l'application ou du programme principal, vous importez/chargez simplement les dépendances (c'est-à-dire les modules dont vous avez besoin) et les exécutez en conséquence. En conséquence, votre application principale devient plus propre et plus minimale.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/modules.png align="left")

*main.js a été divisé en quatre modules*

Supposons que vous devez traiter les paiements dans une autre application de la base de code, par exemple, il devient très facile de réutiliser la même fonctionnalité. Pas besoin de copier et coller ou de coder une nouvelle fonction à partir de zéro.

## Modules JavaScript

Un module en JavaScript est simplement un fichier contenant du code lié.

En JavaScript, nous utilisons les mots-clés `import` et `export` pour partager et recevoir des fonctionnalités respectivement entre différents modules.

* Le mot-clé `export` est utilisé pour rendre une variable, une fonction, une classe ou un objet accessible à d'autres modules. En d'autres termes, il devient un code public.
   
* Le mot-clé `import` est utilisé pour importer du code public d'un autre module.

Regardons un exemple simple de cela :

```js
function getPower(decimalPlaces) {
	return 10 ** decimalPlaces;
}

function capitalize(word) {
	return word[0].toUpperCase() + word.slice(1);
}

function roundToDecimalPlace(number, decimalPlaces = 2) {
	const round = getPower(decimalPlaces);
	return Math.round(number * round) / round;
}

export { capitalize, roundToDecimalPlace };
```

Ce module a trois fonctions définies dans celui-ci :

* `getPower` : Cette fonction obtient la puissance d'un nombre
   
* `capitalize` : Cette fonction met en majuscule la première lettre d'un mot
   
* `roundToDecimalPlace` : Cette fonction arrondit un nombre donné à un nombre spécifié de décimales.

À la fin du fichier, vous pouvez voir que deux des trois fonctions ont été exportées. En d'autres termes, elles sont devenues des fonctions publiques qui pourraient être utilisées par tout autre script.

Pour exporter deux fonctions sur les trois, vous utilisez le mot-clé `export`, suivi d'un objet contenant les fonctions que vous souhaitez rendre accessibles. Une fois que vous avez fait cela, les fonctions peuvent être accessibles par tout programme dans cette base de code qui en a besoin.

Regardons comment nous pouvons les utiliser :

```js
import { capitalize, roundToDecimalPlace } from './main';

function displayTotal(name, total) {
	return `${capitalize(name)}, your total cost is: ${roundToDecimalPlace(total)}`;
}

displayTotal('kingsley', 20.4444444);
// "Kingsley, your total cost is: 20.44"

export { displayTotal };
```

Le module `displayTotal.js` n'a pas `capitalize()` et `roundToDecimalPlace()` mais souhaite utiliser les fonctionnalités de mise en majuscule et d'arrondi aux décimales. Alors, comment les avons-nous importées ? Avec `import` !

Nous l'avons fait en utilisant le mot-clé `import` suivi du nom des fonctions que nous voulons importer depuis le module, qui dans notre cas sont `capitalize` et `roundToDecimalPlace`.

Et si vous vouliez seulement importer la fonction `capitalize` dans votre programme ?

Simple – importez seulement `capitalize()`, comme ceci :

```js
import { capitalize } from './main';

function warn(name) {
	return `I am warning you, ${capitalize(name)}!`;
}

warn('kingsley');
// I am warning you, Kingsley!

export { warn };
```

> N/B : Comprendre comment fonctionne la structuration des fichiers est très important lorsque vous travaillez avec des modules. Dans l'exemple ci-dessus, nous importons simplement depuis un fichier qui existe dans le même répertoire, c'est pourquoi nous utilisons la notation `'./import'`.

Si vous souhaitez importer toutes les fonctions publiques d'un autre module, utilisez l'astérisque `*` :

```js
import * as mainfunctions from './main';

function warn(name) {
return `I am warning you, ${mainfunctions.capitalize(name)}!`;
}
warn('kingsley');
// I am warning you, Kingsley!

export { warn };
```

> **ASTUCE** : Si vous importez tout depuis un module, vous devriez utiliser l'astérisque au lieu d'écrire explicitement toutes les fonctions une par une.

Vous avez peut-être remarqué le mot-clé `as`. Nous l'utilisons pour importer les fonctions publiques dans un nouvel objet, qui dans notre cas est l'objet `mainfunctions`. Nous accédons ensuite et appelons les fonctions que nous voulons utiliser dans notre programme.

Jusqu'à présent, nous n'avons considéré que des exemples où l'exportation se fait à la fin du fichier. Mais vous pouvez également exporter une fonction, une variable ou une classe en enregistrant le mot-clé `export` juste devant sa définition, comme ceci :

```js
function getPower(decimalPlaces) {
	return 10 ** decimalPlaces;
}

export function capitalize(word) {
	return word[0].toUpperCase() + word.slice(1);
}

export function roundToDecimalPlace(number, decimalPlaces = 2) {
	const round = getPower(decimalPlaces);
	return Math.round(number * round) / round;
}
```

Si vous comparez cela avec le premier exemple, vous remarquerez cette différence syntaxique :

* Dans le premier exemple, le mot-clé `export` a été utilisé pour exporter deux fonctions à la fin du script. Dans l'exemple ci-dessus, le mot-clé `export` est attaché aux deux fonctions lorsqu'elles sont définies.

Cependant, ils produisent tous deux le même résultat : `capitalize` et `roundToDecimalPlace` seront tous deux exportés.

## Exportations par Défaut

Si vous souhaitez exporter les trois fonctions mais avez l'intention d'en faire une par défaut (peut-être parce que vous êtes susceptible d'utiliser cette fonction unique), vous utilisez simplement le mot-clé `default`.

Le mot-clé default facilite l'importation d'une fonction. Considérons l'exemple suivant :

```js
export function getPower(decimalPlaces) {
	return 10 ** decimalPlaces;
	}

export default function capitalize(word) {
	return word[0].toUpperCase() + word.slice(1);
	}

export function roundToDecimalPlace(number, decimalPlaces = 2) {
	const round = getPower(decimalPlaces);
	return Math.round(number * round) / round;
	}
```

Comme vous pouvez le voir, nous avons fait de `capitalize` notre fonction par défaut. Cela signifie essentiellement que nous lui avons donné une sorte de privilège.

Disons que nous voulons importer la fonction `capitalize` depuis le module dans un autre programme. La syntaxe pour cela sera très similaire, sauf que vous n'avez pas à importer la fonction entre accolades :

```js
import capitalize from './main';

function warn(name) {
	return `I am warning you, ${capitalize(name)}!`;
}

warn('kingsley');
// I am warning you, Kingsley!

export { warn };
```

Si vous souhaitez importer la fonction par défaut ainsi que d'autres fonctions, vous mélangez la fonction 'default' nue avec d'autres fonctions entre accolades :

```js
import capitalize, { getPower } from './main';

function warn(name) {
	return `I am warning you, ${capitalize(name)}!`;
}

warn('kingsley');
// I am warning you, Kingsley!

export { warn };
```

## Conclusion

Les modules sont des morceaux de code indépendants et autonomes. Vous les créez en divisant un programme plus grand en parties logiques ou dépendances.

Les modules doivent être indépendants, spécialisés et réutilisables.

Vous utilisez les mots-clés `import` et `export` pour échanger des fonctionnalités entre les modules en JavaScript.

Vous utilisez le mot-clé `default` pour spécifier une fonction, un objet, une variable ou une classe que vous souhaitez être une importation de premier choix.

Avec cela, nous avons couvert les bases des modules en JavaScript.

J'espère que vous avez tiré quelque chose de précieux de cet article. J'écris des articles liés à la programmation chaque semaine sur mon [blog personnel](https://ubahthebuilder.tech)

Merci d'avoir lu.

> **P/S** : Si vous apprenez JavaScript, j'ai créé un eBook qui enseigne 50 sujets en JavaScript avec des notes numériques dessinées à la main. [Découvrez-le ici](https://ubahthebuilder.gumroad.com/l/js-50).