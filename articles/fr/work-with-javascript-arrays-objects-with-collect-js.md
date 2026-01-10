---
title: Tutoriel Collect.js – Comment travailler avec les tableaux et les objets JavaScript
subtitle: ''
author: Zubair Idris Aweda
co_authors: []
series: null
date: '2024-01-08T22:38:20.000Z'
originalURL: https://freecodecamp.org/news/work-with-javascript-arrays-objects-with-collect-js
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/zub.png
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
- name: object
  slug: object
seo_title: Tutoriel Collect.js – Comment travailler avec les tableaux et les objets
  JavaScript
seo_desc: 'JavaScript arrays are one of the most important data structures in the
  language, since everything is already an object in JavaScript.

  They''re useful in so many applications, and many other data structures build on
  top of JavaScript arrays and objects...'
---

Les tableaux JavaScript sont l'une des structures de données les plus importantes du langage, puisque tout est déjà un objet en JavaScript.

Ils sont utiles dans de nombreuses applications, et de nombreuses autres structures de données se construisent sur les tableaux et les objets JavaScript. Bien que le langage fournisse de nombreuses méthodes utiles pour les tableaux et les objets, vous pouvez aller encore plus loin en utilisant Collect.js.

Cet article vous guide à travers :

* [Qu'est-ce que Collect.js](#heading-quest-ce-que-collectjs) ?
* [Comment installer Collect.js](#heading-installation)
* [Comment utiliser Collect.js](#heading-comment-utiliser-collectjs)
* [Quelques méthodes de Collect.js](#heading-quelques-methodes-de-collectjs)

## Qu'est-ce que Collect.js ?

La documentation officielle de Collect.js le décrit comme un "wrapper pratique et sans dépendance pour travailler avec des tableaux et des objets".

Une manière plus simple d'expliquer cela est que Collect.js est une bibliothèque JavaScript pour travailler avec des tableaux et des objets. Elle fournit une couche au-dessus des fonctions intégrées pour faciliter leur utilisation.

Collect.js fonctionne comme les [collections Laravel](https://laravel.com/docs/10.x/collections) (d'où vient l'inspiration). Cela rend le développement très facile pour les développeurs Laravel, lorsqu'ils travaillent avec JavaScript, pour développer aussi rapidement qu'ils le feraient s'ils utilisaient PHP. Mais cela ne signifie pas qu'un développeur natif JavaScript ne le trouverait pas vraiment utile également.

Collect.js grandit progressivement, car il compte actuellement plus de 6k étoiles sur GitHub et environ 200k téléchargements hebdomadaires sur NPM au moment de la rédaction de cet article.

## Comment installer Collect.js

Pour commencer à utiliser Collect.js dans vos projets, vous devez d'abord l'installer. Comme d'autres bibliothèques JavaScript, vous pouvez facilement installer Collect.js en utilisant `npm` ou `yarn`. Vous pouvez également l'installer en utilisant un CDN. Pour ce tutoriel, nous allons l'installer en utilisant npm comme ceci :

```bash
npm i collect.js
```

Après l'installation, vous pouvez l'importer dans les modules où vous en avez besoin, comme ceci :

```js
import collect from 'collect.js';
```

Et une fois importé, vous pouvez commencer à faire de la magie avec Collect.js.

Vous pouvez lire sur d'autres méthodes d'installation sur le [site de documentation officielle](https://collect.js.org/installation.html).

## Comment utiliser Collect.js

Après l'installation et l'importation, pour utiliser Collect.js dans vos projets, vous devrez convertir vos données requises en une **collection** Collect.js.

Une collection Collect.js est un objet JavaScript qui possède des fonctions non disponibles nativement pour les tableaux et objets JavaScript réguliers.

Pour créer une collection, utilisez simplement la méthode `collect` importée précédemment sur n'importe quel tableau ou objet. C'est aussi simple que cela – voici un exemple :

```js
const students = ['John', 'James', 'Ian', 'David'];

const studentsCollection = collect(students);
```

Maintenant, en utilisant un IDE comme WebStorm, vous pouvez voir les méthodes disponibles pour la simple collection que vous venez de créer :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-04-at-17.10.21.png)
_List des méthodes disponibles_

Cet article ne couvre pas toutes ces fonctions, mais vous pouvez voir que vous avez maintenant plus que ce que JavaScript offre originally à travers Collect.js.

## Quelques méthodes de Collect.js

Pour aider à comprendre comment Collect.js simplifie les méthodes courantes de tableaux et d'objets, nous allons maintenant voir comment utiliser certaines méthodes très utiles de Collect.js.

### La méthode `average` (ou avg)

Cette méthode, comme vous pouvez l'imaginer, calcule une moyenne d'une collection de nombres. Voici comment l'utiliser :

```js
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const average = collect(numbers).avg();

console.log(average); // 5.5

```

Dans cet exemple, nous avons créé un tableau de nombres entre 1 et 10, inclus. Ensuite, nous obtenons la moyenne de ces nombres en utilisant Collect.js.

Pour faire cela en JavaScript vanilla, vous devriez d'abord faire la somme des nombres en utilisant `array.reduce` ou une boucle, puis obtenir la longueur du tableau original, et diviser la somme par cette longueur. Voir l'exemple d'implémentation ci-dessous :

```js
const sum = arr => arr.reduce( ( p, c ) => p + c, 0 );
const size = numbers.length;
const average = sum(numbers) / size;

console.log(average); // 5.5

```

Vous pouvez voir que c'est beaucoup plus facile et plus élégant en utilisant Collect.js.

Vous pouvez également utiliser la méthode average directement sur des structures plus complexes comme un tableau d'objets. Voici un exemple où la moyenne des scores d'une classe d'étudiants, stockée dans un tableau de détails d'étudiants avec une clé `scores`, est calculée en utilisant Collect.js :

```js
const studentsDetails = [
	{ name: 'John', score: 40, subject: 'Maths' },
	{ name: 'James', score: 70, subject: 'Science' },
	{ name: 'Ian', score: 50, subject: 'Maths' },
	{ name: 'David', score: 60, subject: 'Science' },
];

const studentsCollection = collect(studentsDetails);
const averageScore = studentsCollection.avg('score');
console.log(averageScore); // 55

```

Ici, la moyenne est obtenue de manière très directe et prend moins d'efforts que de le faire en JavaScript vanilla. Et elle utilise le raccourci `avg` au lieu du plus long `average`.

### La méthode `chunk`

Cette méthode divise un tableau en morceaux plus petits en fonction d'une taille donnée. Il s'agit d'une opération courante lors de la manipulation de tableaux JavaScript dans la vie réelle. Un cas d'utilisation courant serait la pagination des enregistrements.

En utilisant le même tableau `studentsDetails` créé dans le dernier exemple, je pourrais diviser la collection en groupes de deux en utilisant la méthode `chunk`, comme ceci :

```js
const studentsCollection = collect(studentsDetails);
const studentGroups = studentsCollection.chunk(2);
```

Cela divise le tableau `studentsCollection` original en deux sous-collections qui ressemblent à ceci :

```js
Collection {
  items: [
    { name: 'John', score: 40, subject: 'Maths' },
    { name: 'James', score: 70, subject: 'Science' }
  ]
}
Collection {
  items: [
    { name: 'Ian', score: 50, subject: 'Maths' },
    { name: 'David', score: 60, subject: 'Science' }
  ]
}

```

Pour obtenir un résultat similaire en JavaScript vanilla, cela prend plus d'efforts car vous auriez besoin d'une boucle :

```js
const chunkedArray = [];
for (let i = 0; i < studentsDetails.length; i += 2) {
	const chunk = studentsDetails.slice(i, i + 2);
	chunkedArray.push(chunk);
}

console.log(chunkedArray);

```

### La méthode `contains`

Vous pouvez utiliser cette méthode pour vérifier si une clé ou une valeur existe dans une collection. Cette fonction vous permet de vérifier indépendamment de la forme ou de la structure des données.

Par exemple, pour vérifier les `studentDetails` existants pour la matière `Physics`, vous pouvez faire ceci :

```js
const studentsDetailsCollection = collect(studentsDetails);

console.log(studentsDetailsCollection.contains('Physics')); // false

```

Pour vérifier si nous avons un étudiant nommé `Science` au lieu de la matière, nous pourrions spécifier quel champ vérifier en passant le nom du champ comme premier paramètre avant la valeur de recherche :

```js
const studentsDetailsCollection = collect(studentsDetails);

console.log(studentsDetailsCollection.contains('name', 'Science')); // false

```

Vous pouvez même vérifier pour voir si la collection contient des valeurs qui correspondent à une certaine condition. Comme pour voir si un étudiant a obtenu plus de 50 :

```js
const studentsDetailsCollection = collect(studentsDetails);

console.log(studentsDetailsCollection.contains((value, key) => value.score > 50)); // true
```

Pour effectuer l'une de ces vérifications en JavaScript vanilla, il faudrait utiliser une boucle pour vérifier chaque objet dans le tableau. Vous pourriez également le faire en utilisant la méthode `some`.

### La méthode `diff`

Cette méthode est utilisée pour obtenir la différence entre deux collections. Les collections pourraient être des tableaux simples ou des tableaux d'objets.

```js
const numbers = collect([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
const primeNumbers = collect([2, 3, 5, 7]);

console.log(numbers.diff(primeNumbers).all()); // [ 1, 4, 6, 8, 9, 10 ]

```

Ici, nous obtenons les nombres qui ne sont pas premiers entre 1 et 10 inclus en supprimant le tableau des nombres premiers du tableau de ces nombres en utilisant la méthode `diff`.

### La méthode `get`

Cette méthode est utilisée pour obtenir des valeurs d'une collection. Si la collection a été créée à partir d'un tableau, elle peut accepter l'index du tableau pour retourner la valeur à cette position.

Si la collection a été créée à partir d'un objet, elle peut accepter une clé et retourner la valeur pour cette clé. Elle retourne `null` lorsqu'aucune valeur n'est trouvée. Vous pouvez passer une valeur par défaut pour l'empêcher de retourner `null`.

En utilisant la collection `numbers` créée dans le dernier exemple, vous pouvez obtenir les premier et douzième éléments, et retourner 10 s'il n'existe pas, comme ceci :

```js
const firstNumber = numbers.get(0);
const twelfthNumber = numbers.get(11, 10);

console.log(firstNumber); // 1
console.log(twelfthNumber); // 10

```

Le `firstNumber` retourne 1 comme prévu, mais le `twelfthNumber` retourne 10, au lieu de retourner `null` ou de lancer une erreur. Cela est très utile lors de la manipulation des entrées utilisateur et des paramètres optionnels.

### La méthode `all`

Cette méthode a déjà été utilisée dans quelques exemples, donc vous pouvez probablement deviner son utilisation. Vous l'utilisez pour obtenir l'objet ou le tableau sous la collection.

L'utilisation de cette méthode sur la collection `numbers` retourne simplement le tableau original de nombres :

```js
console.log(numbers.all()); // [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

```

### La méthode `groupBy()`

Si vous avez une expérience en SQL, ce nom de méthode vous sera familier. Il fonctionne de manière similaire à la fonction SQL : il regroupe les données dans une collection par une clé donnée.

En utilisant cette méthode, nous pouvons regrouper les étudiants par la matière offerte, comme ceci :

```js
const studentsGroupedBySubject = collect(studentsDetails).groupBy('subject');
console.log(studentsGroupedBySubject.all());

```

Cela créera deux sous-collections pour les deux matières, maths et science.

```js
{
  Maths: Collection { items: [ [Object], [Object] ] },
  Science: Collection { items: [ [Object], [Object] ] }
}

```

### Les méthodes `isEmpty` et `isNotEmpty`

La méthode `isEmpty` vérifie si une collection est vide, et `isNotEmpty` vérifie le contraire. Ces méthodes aident à prévenir la vulnérabilité de [object spoofing](https://learn.snyk.io/lesson/prototype-pollution/).

```js
console.log(numbers.isEmpty()) // false
console.log(numbers.isNotEmpty()) // true

```

### Les méthodes `first` et `last`

Ces noms de méthodes sont aussi descriptifs qu'ils peuvent l'être. La méthode `first` obtient le premier élément d'une collection. Elle peut également être utilisée pour obtenir le premier élément qui correspond à une condition.

Par exemple, pour obtenir le premier étudiant qui a un score supérieur à 40 dans la matière `Maths`, vous pouvez utiliser la méthode `first` comme ceci :

```js
console.log(studentsDetailsCollection.first((student) => student.score > 40 && student.subject === 'Maths'));

```

La méthode `last` est également très similaire à la méthode `first`. Elle obtient le dernier élément d'une collection lorsqu'elle est appelée sans condition. Lorsqu'une condition est spécifiée, elle obtient le dernier élément qui correspond à cette condition.

Par exemple, pour obtenir le dernier étudiant qui échoue en `Maths` dans la `studentsDetailsCollection`, utilisez ce code :

```js
console.log(studentsDetailsCollection.last((student) => student.score < 40 && student.subject === 'Maths'));

```

Cet dernier exemple retourne `undefined` car aucun étudiant n'échoue en maths.

Pour obtenir ces mêmes résultats en utilisant JavaScript vanilla, il faudrait une boucle qui vérifie chaque élément et garde une trace du premier et du dernier qui correspondent à la condition, comme ceci :

```js
const getFirstStudentThatPassesMaths = (studentDetails) => {
	let firstStudentThatPassesMaths = undefined;

	studentDetails.forEach((student) => {
		if (student.subject === 'Maths' && student.score > 40) {
			firstStudentThatPassesMaths = student;
			return false;
		}
	});

	return firstStudentThatPassesMaths;
}

const getLastStudentThatFailsMaths = (studentDetails) => {
	let lastStudentThatFailsMaths = undefined;

	studentDetails.forEach((student) => {
		if (student.subject === 'Maths' && student.score < 40) {
			lastStudentThatFailsMaths = student;
		}
	});

	return lastStudentThatFailsMaths;
}

console.log(getFirstStudentThatPassesMaths(studentsDetails));
console.log(getLastStudentThatFailsMaths(studentsDetails));
```

Voyez à quel point les implémentations Collect.js sont plus simples.

### La méthode `macro`

Cette méthode est très utile, car elle vous permet même d'étendre Collect.js en ajoutant vos propres méthodes. Elle a la structure suivante :

```js
collect().macro('functionName', function () {
	// corps de la fonction
});

```

Ici, `functionName` est le nom de la nouvelle fonction que vous ajoutez, et le corps de la fonction est l'endroit où votre nouvelle logique est placée.

Par exemple, pour attribuer des notes aux étudiants en utilisant notre `studentsDetailsCollection`, nous pouvons créer une nouvelle méthode appelée `grade`. Nous pouvons la rendre un peu plus complexe et faire en sorte que la fonction modifie la collection en ajoutant la note calculée à chaque objet étudiant.

```js
collect().macro('grade', function () {
	return this.map(item => {
		if (item.score >= 70) item.grade = 'A';
		else if (item.score >= 60) item.grade = 'B';
		else if (item.score >= 50) item.grade = 'C';
		else if (item.score >= 45) item.grade = 'D';
		else if (item.score >= 40) item.grade = 'E';
		else item.grade = 'F';

		return item;
	});
});
```

Vous pouvez ensuite appeler la méthode sur la collection comme n'importe quelle autre méthode intégrée comme ceci :

```js
studentsDetailsCollection.grade();

```

Après modification, votre collection ressemblera à ceci :

```js
[
  { name: 'John', score: 40, subject: 'Maths', grade: 'E' },
  { name: 'James', score: 70, subject: 'Science', grade: 'A' },
  { name: 'Ian', score: 50, subject: 'Maths', grade: 'C' },
  { name: 'David', score: 60, subject: 'Science', grade: 'B' }
]

```

## **Résumé**

J'espère que vous comprenez maintenant comment simplifier votre développement JavaScript en utilisant des fonctions simples de Collect.js. Cet article ne couvre que certaines des méthodes les plus utiles, mais il y en a plus disponibles. Pour en savoir plus, consultez la [documentation officielle](https://collect.js.org/api.html).

Si vous avez des questions ou des conseils pertinents, n'hésitez pas à me contacter.

Pour lire plus de mes articles ou suivre mon travail, vous pouvez me rejoindre sur [LinkedIn](https://www.linkedin.com/in/idris-aweda-zubair-5433121a3/), [Twitter](https://twitter.com/AwedaIdris), et [Github](https://github.com/Zubs). C'est rapide, c'est facile, et c'est gratuit !