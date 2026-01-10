---
title: Les bases de JavaScript – Comment manipuler les chaînes de caractères, les
  tableaux et les objets en JS
subtitle: ''
author: Houssein Badra
co_authors: []
series: null
date: '2023-03-20T20:12:35.000Z'
originalURL: https://freecodecamp.org/news/javascript-basics-strings-arrays-objects
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/js.png
tags:
- name: beginner
  slug: beginner
- name: JavaScript
  slug: javascript
seo_title: Les bases de JavaScript – Comment manipuler les chaînes de caractères,
  les tableaux et les objets en JS
seo_desc: 'JavaScript is a popular programming language that 78% of developers use.
  You can build almost anything with JavaScript.

  The problem is that many developers learn JavaScript in a very short period of time,
  without understanding some of the most essent...'
---

JavaScript est un langage de programmation populaire utilisé par 78 % des développeurs. Vous pouvez presque tout construire avec JavaScript.

Le problème est que de nombreux développeurs apprennent JavaScript en très peu de temps, sans comprendre certaines des fonctionnalités les plus essentielles du langage.

Dans cet article, nous aborderons en détail les tableaux, les chaînes de caractères et les objets JavaScript afin que vous puissiez tirer parti de certaines des méthodes statiques et d'instance les plus efficaces offertes par le langage.

### Voici ce que nous allons couvrir dans ce guide :

* Méthodes d'instance et de classe
* Comment utiliser les chaînes de caractères en JavaScript
* Comment utiliser les tableaux en JavaScript
* Comment utiliser les objets en JavaScript

## Méthodes d'instance et de classe

JavaScript est fortement orienté objet. Il suit un modèle basé sur les prototypes, mais il offre également une syntaxe de classe pour permettre les paradigmes typiques de la POO.

En JavaScript, les chaînes et les tableaux sont des objets, et chaque objet en JavaScript est un modèle qui possède ses propres méthodes et propriétés. Chaque objet hérite des méthodes et des propriétés de son prototype. En JavaScript, chaque objet a accès au **prototype d'Object**.

Les méthodes statiques sont des méthodes disponibles au niveau de la classe – par exemple la méthode **Object.freeze()**. Les méthodes d'instance sont disponibles au niveau de l'instance – par exemple, une instance créée d'un objet **Array** a accès aux méthodes d'instance telles que **.join()**, mais pas aux méthodes statiques.

## Comment utiliser les chaînes de caractères en JavaScript

Les chaînes de caractères (strings) sont utilisées pour contenir des données pouvant être représentées sous forme de texte. Pour créer une chaîne, vous pouvez utiliser le constructeur **String()** ou un littéral de chaîne. Voici un exemple des deux méthodes :

```javascript
 // Utilisation d'un constructeur

let string1 = String('Création de chaîne');

 // Utilisation d'un littéral de chaîne
 
let string2 = 'Création de chaîne';

```

Apprenons maintenant à mieux connaître les méthodes d'instance. Il existe de nombreuses méthodes d'instance, mais je vais aborder ici sept méthodes que je considère comme les plus importantes.

### La méthode .charAt()

Souvent, lorsque nous travaillons avec des chaînes, nous voulons accéder à un caractère à un certain index de la chaîne. Vous pouvez le faire soit avec la méthode **charAt()**, soit avec l'indexation, de la même manière que nous traitons un tableau.

```javascript
 // Disons que nous voulons accéder au premier caractère d'une chaîne donnée
 
 let string = 'Hello World';
 
  // en utilisant l'indexation
  
 let first1 = string[0]; // sortie 'H' et rappelez-vous que l'indexation commence à 0
 
  // en utilisant la méthode charAt()
 
 let first2 = string.charAt(0); // sortie 'H'
```

En JavaScript, le système d'indexation commence à 0 – par exemple, le premier caractère d'une chaîne a l'index 0, et ainsi de suite.

### Les méthodes .toUpperCase() et .toLowerCase()

Supposons maintenant que nous voulions mettre une chaîne en majuscules ou en minuscules. Vous pouvez le faire en utilisant les méthodes d'instance **toUpperCase()** et **toLowerCase()**.

```javascript
 let string = 'Hello';
 
  // Mettons une chaîne en minuscules
 
 let lowerCase = string.toLowerCase(); // sortie 'hello'
 
  // Mettons une chaîne en majuscules
  
 let upperCase = string.toUpperCase(); // sortie 'HELLO'
```

Vous pourriez les utiliser pour voir si deux chaînes contiennent le même mot, par exemple 'Sam' et 'sam'. En réalité, 'sam' === 'Sam' renvoie false, tandis que 'sam'.toLowerCase() === 'Sam'.toLowerCase() renvoie true.

### La méthode .concat()

Il est souvent nécessaire de joindre des chaînes de texte ensemble dans un programme pour créer une nouvelle chaîne. C'est ce qu'on appelle la **concaténation**.

Pour la concaténation de chaînes, nous pouvons utiliser la méthode **concat()**. Elle s'utilise comme suit. Une note importante : cette méthode renvoie une nouvelle chaîne sans modifier l'originale.

```javascript
let string = 'Hello';

 // Concaténation de chaînes à l'aide de la méthode concat
 
let string1 = string.concat(' World'); // sortie 'Hello World'

```

### La méthode .indexOf()

Pour trouver l'index d'un certain caractère ou d'un ensemble de caractères dans une chaîne, nous pouvons utiliser la méthode **indexOf()**. Elle renverra l'index de la première occurrence du caractère ou de l'ensemble de caractères passé en argument.

```javascript
let string = 'Hello World';

 // Trouvons l'index où 'H' apparaît pour la première fois
 
let firstH = string.indexOf('H'); // sortie 0
 
 // Trouvons le premier index où 'World' apparaît pour la première fois
 
let firstWorld = string.indexOf('World'); // sortie 6

 // Dans le cas où un caractère ou un ensemble de caractères   
 // n'apparaît pas dans la chaîne, cette méthode renvoie -1
 
let notThere = string.indexOf('Z'); // sortie -1
 
```

### La méthode .slice()

Une sous-chaîne est un sous-ensemble ou une partie d'une autre chaîne, ou une séquence contiguë de caractères au sein d'une chaîne. Par exemple, "Substring" est une sous-chaîne de "Substring in JavaScript".

Supposons maintenant que nous voulions obtenir une sous-chaîne d'une chaîne donnée. Nous pouvons utiliser la méthode **slice()**. Slice est en fait l'une des méthodes de chaîne les plus importantes. Vous l'utilisez pour obtenir des sous-chaînes et aussi pour copier des chaînes.

Slice prend deux paramètres optionnels : le premier est l'endroit où nous voulons commencer la découpe et le second est l'endroit où nous voulons terminer l'opération de découpe.

Supposons que nous ayons passé **1** et **10** comme paramètres pour la méthode slice. La méthode renverra alors une sous-chaîne commençant à l'index **1** et se terminant à l'index **9.**

Cela signifie que la sous-chaîne n'inclut jamais le caractère situé à l'index de fin. Une note importante est de ne jamais passer un index de fin supérieur à la longueur de la chaîne.

```javascript
let string = 'Hello World';
 
 // pour vérifier la longueur de la chaîne, nous pouvons utiliser la propriété d'instance length
 
let length = string.length; // sortie 11

 // découpage pour obtenir la sous-chaîne de l'index 1 -> 9
 
let string1 = string.slice(1 , 10); // sortie 'ello Worl'

 // ne passer aucun paramètre générera 
 // une copie de la chaîne originale sans mutation
 
let copy = string.slice(); // sortie 'Hello World'
```

### La méthode .split()

La dernière méthode de chaîne que nous allons couvrir est la méthode **split()**. Cette méthode prend un motif comme argument et divise la chaîne en plusieurs sous-chaînes. Le motif décrit l'endroit où les divisions se produisent. Cette méthode renvoie un tableau de ces sous-chaînes.

Vous pourriez vous retrouver à utiliser cette méthode pour analyser une URL ou certaines chaînes de caractères.

```javascript
let string = 'Hello World';

 // Diviser une chaîne en mots
 // Cela peut être fait lorsque le motif passé est un espace
 
let words = string.split(' '); // sortie ['Hello' , 'World']

 // Lorsque le paramètre passé est une chaîne vide, le tableau de sortie
 // contiendra chacun des caractères de la chaîne donnée
 
let chars = string.split(''); 

 // sortie ["H","e","l","l","o"," ","W","o","r","l","d"]
```

Il existe de nombreuses autres méthodes que vous pouvez découvrir, mais ce sont celles avec lesquelles vous travaillerez le plus. Vous pouvez en apprendre davantage en lisant les [documents web officiels de MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String).

## Comment utiliser les tableaux en JavaScript

Comme dans d'autres langages de programmation, les tableaux (arrays) JavaScript vous permettent de stocker une collection de données sous une seule variable. Mais contrairement au C ou au C++, les tableaux peuvent être renvoyés par des appels de fonction.

Les tableaux JavaScript sont dynamiques, vous pouvez donc ajouter ou supprimer des éléments d'un tableau. Vous pouvez également avoir des éléments de plusieurs types de données dans un seul tableau.

Parlons de la façon de créer des tableaux en JavaScript. Vous pouvez facilement créer un tableau en assignant une variable à des crochets vides [ ] ou en utilisant le constructeur **Array()**.

```javascript
 // Création d'un tableau à partir du constructeur
 
let arr1 = Array();
 
 // Méthode préférée
 
let arr2 = [];

```

Parlons maintenant de sept méthodes d'instance et de classe de tableau que je considère comme les plus utiles.

### La méthode .indexOf()

Pour obtenir le premier index d'un tableau donné où un élément apparaît, nous pouvons utiliser la méthode **indexOf()**. Elle se présente comme suit. Si l'argument passé à cette méthode ne figure pas dans le tableau, elle renverra -1.

```javascript
let array = [1, 2, 3];

 // Trouvons l'index où 1 apparaît pour la première fois
 
let first1 = array.indexOf(1); // sortie 0

 // Essayons maintenant de trouver 4 dans le tableau
 
let first4 = array.indexOf(4); // sortie -1
```

### Les méthodes .push() et .pop()

Comme je l'ai mentionné plus tôt, les tableaux JavaScript sont dynamiques. Nous pouvons donc ajouter des éléments en utilisant la méthode **push()** et supprimer le dernier élément en utilisant la méthode **pop()**. Une note importante est que ces deux méthodes modifient le tableau d'origine.

```javascript
let array = [1, 2, 3];

 // ajoutons 4 au tableau
 
array.push(4)

console.log(array) // sortie [1, 2, 3, 4]

 // remettons maintenant le tableau comme avant
 
let removedElement = array.pop() // sortie 4

console.log(array) // sortie [1, 2, 3]
```

Nous allons maintenant discuter de méthodes plus avancées – celles introduites par la mise à jour ES6.

### La méthode .map()

Tout d'abord, supposons que vous vouliez créer un tableau en utilisant des données d'un autre tableau existant – par exemple si vous avez un tableau d'objets représentant des employés.

Chaque objet employé possède une propriété name. Et vous voulez créer un tableau où chaque élément est la valeur de la propriété name de l'objet employé au même index du tableau que vous avez.

C'est là qu'intervient la méthode **map()**. Elle prend une fonction de rappel (callback). Map crée un nouveau tableau et ne modifie jamais l'ancien, et le callback exprime ce que vous voulez faire avec les données du tableau d'origine. Cela ressemblera à ceci :

```javascript
let arr= [{name : 'joe'} , {name : 'john'}];

 // Il est préférable d'utiliser une fonction fléchée

let namesArr = arr.map(elem => elem.name); // sortie ['joe' , 'john']
```

### La méthode .forEach()

Vous en avez assez des boucles for habituelles ? Elles sont un peu ennuyeuses, je sais. Heureusement, la méthode **forEach()** est là pour vous aider.

Cette méthode prend un callback comme argument et ne renvoie rien. Elle itère sur le tableau et exécute une certaine tâche sur chaque élément du tableau. Le callback exprime la tâche. Le code pour cela ressemblera à ceci :

```javascript
let arr= [1, 2, 3];

 // affichons chaque élément dans la console
 
arr.forEach(elem => console.log(elem));

 // sortie 
 // 1
 // 2
 // 3
```

### La méthode .filter()

Disons maintenant que nous avons un tableau de nombres et que nous voulons créer un tableau ne contenant que les nombres qui remplissent une certaine condition.

Dans ce cas, nous pouvons utiliser la méthode **filter()** qui prend également un callback comme argument. Le callback renvoie un booléen – true si l'élément passe le test, sinon false. Seuls les éléments qui passent seront dans le tableau généré et le callback exprime le test. Voici comment cela fonctionne :

```javascript
let arr = [1, 2, 3, 4, 5];

 // Créons un tableau de nombres supérieurs à 3
 
let filteredArray = arr.filter(elem => elem > 3); // sortie [4, 5]
```

### La méthode .some()

Disons maintenant que nous avons un tableau et que nous voulons vérifier s'il existe au moins un nombre qui passe un certain test. Voici la méthode **some()**.

Cette méthode prend un callback comme argument et renvoie un booléen qui est true si au moins un élément du tableau passe le test, et sinon false. Le callback exprime le test et se présente comme suit :

```javascript
let arr = [1, 2, 3, 4, 5];

 // Vérifions si au moins un élément est supérieur à 4
 
let bool = arr.some(elem => elem > 4); // sortie true
```

### La méthode .sort()

Le tri est le processus d'organisation des données dans un ordre significatif afin que vous puissiez les analyser plus efficacement.

En parlant de tableaux, nous devons mentionner le tri. En JavaScript, la méthode **sort()** trie les tableaux sur place (in place) et renvoie la référence au même tableau. Cette méthode modifie le tableau et l'ordre de tri par défaut est croissant.

Vous pouvez implémenter votre propre logique de tri en passant un callback qui exprime une comparaison entre deux éléments et renvoie un nombre. Si le nombre renvoyé est positif, alors le premier des deux éléments comparés apparaîtra en premier dans le tableau trié.

```javascript
let arr = [1, 2, 4, 3];

 // tri par ordre croissant
 
arr.sort();

console.log(arr); // [1, 2, 3, 4]

 // utilisation d'un tri personnalisé pour trier par ordre décroissant
 
arr.sort((elem1 , elem2) => elem2 - elem1);

console.log(arr); // sortie [4, 3, 2, 1]
```

Il existe de nombreuses méthodes de chaînes intéressantes que je n'ai pas mentionnées et qui valent la peine d'être apprises. Si vous souhaitez le faire, vous pouvez consulter les [documents officiels de MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array).

## Comment utiliser les objets en JavaScript

Si vous voulez être un bon développeur JavaScript, vous devriez vraiment avoir une compréhension décente des objets et de la façon dont ils fonctionnent.

Presque chaque objet que vous créez en JavaScript hérite des méthodes du prototype global **`Object`** qui est disponible globalement pour chaque objet en JavaScript. Une exception concerne les objets à prototype nul, dont nous n'allons pas parler. Toutes les méthodes dont je vais parler sont principalement statiques.

Parlons d'abord de la façon de créer des objets en utilisant une paire d'accolades **{ }** ou le constructeur **Object**. Voici à quoi cela ressemble :

```javascript
 // Création d'un objet à partir d'un constructeur
 
let obj1 = Object();

 // Création d'un objet à l'aide d'accolades
 
let obj2 = {};
```

### La méthode .assign()

Supposons maintenant que nous voulions copier un objet. Voici la méthode statique **assign()** pour nous aider à le faire. Je vais vous montrer comment cela fonctionne et une meilleure façon de le faire. J'aborderai également certaines erreurs courantes commises par de nombreux développeurs lorsqu'ils essaient de copier des objets.

```javascript
let obj = {age : 18};

 // Copie à l'aide de la méthode assign
 
let new1 = {};

Object.assign(new1 , obj);

console.log(new1); // sortie {age : 18}

 // Nous pouvons faire la même chose avec l'opérateur de décomposition (spread)
 
let new2 = {...obj}; // sortie {age : 18}
```

Une erreur courante consiste à assigner directement une variable à un objet. Le problème est que les objets sont assignés par référence et non par valeur. Ainsi, tout changement modifiera l'objet d'origine.

```javascript
let obj = {age : 18};

let obj1 = obj;

obj1.age = 17;

console.log(obj); // sortie {age : 17}
```

### Les méthodes .freeze() et .isFrozen()

Disons maintenant que nous voulons rendre un objet immuable. Pour cela, nous pouvons utiliser la méthode statique **freeze()** qui rend impossible l'ajout de propriétés, la modification ou la suppression de prototypes, de méthodes et de propriétés de l'objet gelé.

Pour voir si un objet est gelé, nous pouvons utiliser la méthode statique **isFrozen()**.

```javascript
let obj = {age : 18};

Object.freeze(obj);

 // Essayons de modifier cet objet
 
obj.age = 17; // Lève une erreur en mode strict

let isFrozen = Object.isFrozen(obj); // sortie true
```

### Les méthodes .keys() et .values()

Maintenant, pour obtenir une liste des propriétés d'un certain objet, nous pouvons appeler la méthode statique **keys()**. Pour obtenir une liste des valeurs correspondant à ses propriétés, nous pouvons appeler la méthode statique **values()**. Une note importante est que la liste renvoyée est un tableau.

```javascript
let obj = {name : 'John Doe' ,age : 45};

let keys = Object.keys(obj); // sortie ['name', 'age']

let values = Object.values(obj); // sortie ['John Doe', 45]
```

Vous pouvez consulter les [documents web MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object) pour approfondir le sujet.

## Conclusion

Dans ce tutoriel, nous avons parlé des tableaux, des chaînes de caractères et des objets, ainsi que des méthodes qu'ils proposent. J'espère que vous avez appris quelque chose de nouveau aujourd'hui.

Si vous êtes intéressé par d'autres contenus de ce type, suivez-moi sur [LinkedIn](https://www.linkedin.com/in/houssein-badra-943879214) où je partage beaucoup de ressources intéressantes.