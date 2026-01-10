---
title: Apprenez ES6+ dans ce cours gratuit et interactif en 23 parties
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-26T21:10:00.000Z'
originalURL: https://freecodecamp.org/news/want-to-learn-es6-take-this-free-23-part-course-and-become-a-javascript-ninja-55002db1ff74
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0-gCRnSTrgH7kWyg91ofGA.png
tags:
- name: coding
  slug: coding
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Apprenez ES6+ dans ce cours gratuit et interactif en 23 parties
seo_desc: 'By Per Harald Borgen


  _Click here to get to the course._

  JavaScript is undoubtedly one of the most popular programming languages in the world.
  It’s used almost everywhere: from large-scale web applications to complex servers
  to mobile and IoT devices...'
---

Par Per Harald Borgen

![Image](https://cdn-media-1.freecodecamp.org/images/1*TsmDHkE8rZ7DQMVnqQqtYw.png)
_[Cliquez ici pour accéder au cours.](https://scrimba.com/g/gintrotoes6?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gintrotoes6_launch_article)_

JavaScript est sans aucun doute l'un des langages de programmation les plus populaires au monde. Il est utilisé presque partout : des applications web à grande échelle aux serveurs complexes, en passant par les appareils mobiles et IoT.

Nous nous sommes donc associés avec [Dylan C. Israel](https://medium.com/u/7f21f9c02e5b) — un YouTubeur en programmation et diplômé de freeCodeCamp — et nous lui avons demandé de créer le [cours Introduction à ES6 sur Scrimba.](https://scrimba.com/g/gintrotoes6?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gintrotoes6_launch_article)

Le cours contient 17 leçons et 4 défis interactifs. Il s'adresse aux développeurs JavaScript qui souhaitent apprendre les fonctionnalités modernes de JavaScript introduites dans ES6, ES7 et ES8.

Examinons la structure du cours :

### Partie #1 : Introduction

![Image](https://cdn-media-1.freecodecamp.org/images/1*TsmDHkE8rZ7DQMVnqQqtYw.png)

Dans la vidéo d'introduction, Dylan donne un aperçu de ce à quoi ressemblera son cours et des principaux sujets qu'il abordera. Il se présente également afin que vous soyez familier avec lui avant de plonger dans le code.

### Partie #2 : Littéraux de gabarit

La première fonctionnalité d'ES6 abordée dans le cours est celle des littéraux de gabarit. Les littéraux de gabarit sont une manière plus propre et plus élégante de manipuler des chaînes de caractères. Ils éliminent le besoin de nombreux signes `+` pour concaténer des chaînes.

```js
let str1 = 'Mon nom est :'  
let name = 'Dylan';

let str2 = `${str1} ${name}`

// --> 'Mon nom est : Dylan'

```

Les littéraux de gabarit commencent par une backtick, et nous utilisons le signe `$` et des accolades pour introduire une variable entre les deux.

### Partie #3 : Déstructuration d'objets

Dans la partie 3, vous apprendrez à déstructurer un objet et à extraire les propriétés qui vous intéressent.

```js
let information = { firstName: 'Dylan', lastName: 'Israel'};

let { firstName, lastName } = information;

```

Dans le code ci-dessus, nous extrayons les propriétés `firstName` et `lastName` de l'objet et nous les assignons à des variables en utilisant la déstructuration d'objet.

### Partie #4 : Déstructuration de tableaux

Dans cette partie, vous apprendrez à obtenir le pointeur de l'élément qui nous intéresse dans le tableau en utilisant la déstructuration de tableau.

```js
let [ firstName ] = ['Dylan', 'Israel'];

```

Ici, `firstName` pointe vers le premier élément du tableau du côté droit. Nous pouvons également créer plus de pointeurs du côté gauche des éléments de notre tableau.

### Partie #5 : Littéral d'objet

Dans la partie 5 de notre cours, nous apprendrons une autre fonctionnalité intéressante d'ES6, qui est le littéral d'objet. Les littéraux d'objet vous permettent d'omettre la clé dans l'objet si le nom de la clé et de la valeur sont les mêmes.

```js
let firstName = 'Dylan';  
let information = { firstName };

```

Ainsi, dans l'exemple ci-dessus, nous voulions ajouter la propriété `firstName` dans notre objet `information`. La variable `firstName` est une autre variable avec le même nom. Nous omettons la clé et passons simplement le nom de la variable, et elle créera la propriété et assignera la valeur elle-même.

### Partie #6 : Littéral d'objet (Défi)

Maintenant, il est temps pour le premier défi du cours ! Le but ici est de consigner le nouvel objet city, la nouvelle adresse et le pays qui l'accompagne.

```js
function addressMaker(address) {  
   const newAddress = {  
      city: address.city,  
      state: address.state,  
      country: 'États-Unis'  
   };  
   ...  
}

```

Vous êtes encouragé à utiliser les sujets que nous avons appris jusqu'à présent pour résoudre ce problème. Cela inclut les littéraux de gabarit, la déstructuration d'objet et les littéraux d'objet.

### Partie #7 : Boucle For...Of

Dans la partie 7, vous apprendrez une nouvelle façon de parcourir les éléments. ES6 a introduit une instruction de boucle For...Of, qui crée une boucle qui itère sur des objets itérables comme String, Array, NodeList, et plus encore.

```js
let str = 'bonjour';

for (let char of str) {  console.log(char);}// "b"// "o"// "n"// "j"// "o"// "u"// "r"

```

Dans l'exemple de code ci-dessus, la boucle For...Of parcourt une chaîne et consigne les caractères.

### Partie #8 : Défi de la boucle For...Of

Dans ce défi, on vous demande de deviner ce qui se passe lorsque vous utilisez `let` au lieu de `const` à l'intérieur d'une boucle `for...of`, et d'essayer de manipuler les valeurs à l'intérieur de la boucle.

```js
let revenus = [62000, 67000, 75000];

for (const revenu of revenus) {

}  
console.log(revenus);

```

### Partie #9 : Opérateur de décomposition

Dans la partie 9 du cours, vous apprendrez l'une des fonctionnalités les plus intéressantes incluses dans ES6 : l'opérateur de décomposition.

```js
let arr1 = [1, 2, 3];
let arr2 = [4, 5, 6];
let arr3 = [...arr1, ...arr2];

// arr3 = [1, 2, 3, 4, 5, 6];

```

Le code ci-dessus démontre l'une des nombreuses implémentations intéressantes de l'utilisation de l'opérateur de décomposition. Ici, nous combinons deux tableaux en les plaçant dans un nouveau tableau avec trois points (...) devant le nom du tableau.

### Partie #10 : Opérateur Rest

Dans cette leçon, vous apprendrez quelques cas d'utilisation de l'opérateur Rest. L'opérateur Rest nous aide à gérer les paramètres de fonction de manière plus efficace en nous permettant de représenter le nombre variable de paramètres de fonction sous forme de tableau.

```js
function findLength(...args) {  console.log(args.length);}

findLength();  // 0
findLength(1); // 1
findLength(2, 3, 4); // 3

```

Ici, nous appelons la même fonction avec un nombre différent de paramètres, et l'opérateur Rest gère cela parfaitement pour nous.

### Partie #11 : Fonctions fléchées

Cette leçon nous enseigne l'une des fonctionnalités les plus intéressantes et les plus discutées introduites dans ES6 : les fonctions fléchées. Les fonctions fléchées ont changé la façon dont nous écrivons les fonctions.

```js
const square = num => num * num;


square(2); // 4

```

En utilisant la fonction fléchée, l'apparence d'une fonction de _mise au carré_ a complètement changé. En une seule ligne de code, nous sommes capables de retourner le carré d'un nombre. Les fonctions fléchées ont beaucoup d'autres implémentations géniales, qui sont expliquées dans la leçon.

### Partie #12 : Paramètres par défaut

Les paramètres par défaut nous permettent d'initialiser des fonctions avec une valeur par défaut. Dans cette leçon, vous apprendrez à quel point cette fonctionnalité peut être utile dans les tâches de codage de la vie réelle, car elle vous aide à éviter les erreurs et les bugs. Un exemple simple de paramètres par défaut serait :

```js
function sum (a, b = 1) {    
  return a + b;
}

sum(5); // 6

```

Ici, nous définissons la valeur par défaut de `b` afin que, lorsque nous ne passons aucune valeur pour b, elle utilise la valeur par défaut pour calculer le résultat.

### Partie #13 : includes()

En utilisant la méthode `includes`, nous pouvons découvrir si une chaîne contient un caractère particulier ou une sous-chaîne. Dans cette leçon, vous apprendrez en détail les cas d'utilisation pratiques de cette fonction.

```js
let str = 'Bonjour le monde';

console.log(str.includes('bonjour')); // true

```

Ici, nous découvrons si notre chaîne contient la sous-chaîne `bonjour`. Comme vous pouvez le voir, la méthode includes retourne soit vrai soit faux selon que la condition est remplie ou non.

### Partie #14 : Let et Const

Peut-être la fonctionnalité la plus importante d'ES6 est-elle les deux nouveaux mots-clés pour déclarer des variables : `let` et `const`.

```js
let str = 'Bonjour le monde';

const num = 12345;

```

En utilisant `let`, nous pouvons créer des variables qui peuvent être modifiées plus tard dans le programme. Les variables déclarées avec `const` ne peuvent jamais être modifiées. Nous en apprendrons davantage dans cette leçon.

### Partie #15 : Import et Export

Nous savons tous à quel point il est important d'avoir un code modulaire, surtout si vous travaillez sur des applications à grande échelle. Avec les instructions `import` et `export` en JavaScript, il est devenu extrêmement facile et propre de déclarer et d'utiliser des modules.

Dans la partie 15 de ce cours, vous apprendrez à utiliser les instructions export et import pour créer des modules.

```js
// exporte la fonction 
export function double(num) {   
 return num * num;  
}

```

Dans le code ci-dessus, nous exportons une fonction nommée `double`. Nous importons ensuite la fonction dans un fichier séparé :

```js
// importe la fonction  
import { double } from '..filepath/filename

```

### Partie #16 : padStart() et padEnd()

ES2017 a introduit deux nouvelles méthodes pour manipuler les chaînes, que vous apprendrez en détail dans cette partie. `padStart` et `padEnd` ajouteront simplement un remplissage au début et à la fin de la chaîne.

```js
let str = 'Bonjour';  
str.padStart(3); // '   Bonjour'

str.padEnd(3); // 'Bonjour   '

```

### Partie #17 : Défi padStart() et padEnd()

Dans cette partie, vous aborderez le troisième défi de ce cours. C'est un petit quiz dans lequel Dylan vous demande d'abord de deviner, puis explique ce qui se passe lorsque le code suivant s'exécute :

```js
let example = 'YouTube.com/CodingTutorials360';

// console.log(example.padStart(100));  
// console.log(example.padEnd(1));

```

### Partie #18 : Classes

Les classes ont été introduites dans ES6, et elles ont complètement élevé le niveau pour l'utilisation des motifs orientés objet en JavaScript. Bien qu'il ne s'agisse que de sucre syntaxique sur l'héritage prototypique existant de JavaScript, cela a facilité l'écriture de manière plus orientée objet.

Ainsi, dans cette leçon, vous apprendrez en détail comment utiliser les classes et tirer parti des fonctionnalités de la POO comme, par exemple, l'héritage. Voici un exemple simple d'utilisation des classes.

```js
class Car {
   constructor(wheels, doors) {
      this.wheels = wheels;
      this.doors = doors;
   }
   describeMe() {
     console.log(`Portes : ${this.doors} et Roues : ${this.wheels}`);
   }}


const car1 = new Car(4, 2);  
car1.describeMe(); // Portes : 2 et Roues : 4

```

Ici, nous créons une simple classe Car dans laquelle nous avons un constructeur assignant les roues et les portes. Nous avons également une méthode qui consigne le nombre de portes et de roues de la voiture.

Ensuite, nous créons une nouvelle instance et passons les valeurs des roues et des portes. Enfin, nous appelons la méthode `describeMe` sur celle-ci.

### Partie #19 : Virgules finales

Dans la leçon 19, vous apprendrez à utiliser les virgules finales. Elles facilitent l'ajout de nouveaux éléments, propriétés ou attributs à votre code, car vous pouvez le faire sans avoir à vous soucier d'ajouter une virgule à l'élément précédent.

```js
let arr = [  1,   2,   3, ];arr.length; // 3

```

Ce n'était qu'un simple exemple d'utilisation des virgules finales. Vous en apprendrez davantage à leur sujet dans notre leçon pendant notre cours.

### Partie #20 : Async & Await

Async & Await est ma fonctionnalité préférée d'ES6. Avec Async & Await, nous pouvons écrire du code asynchrone qui ressemble à du code synchrone. Cela est propre, facile à lire et facile à comprendre. Donc, dans cette leçon, vous apprendrez quelques exemples pratiques de son utilisation.

```js
let response = await fetch('https://example.com/books');
console.log('response');

```

Dans l'exemple ci-dessus, nous avons utilisé le mot-clé await avant l'instruction fetch, donc il attendra que le résultat de cette API soit récupéré avant de passer à la ligne suivante.

### Partie #21 : Async & Await (Défi)

Il s'agit du dernier défi de ce cours, et il concerne bien sûr Async & Await. Vous serez invité à essayer de convertir le code suivant basé sur les promesses en utilisant Async & Await :

```js
function resolveAfter3Seconds() {  
   return new Promise(resolve => {  
      setTimeout(() => {  
        resolve('résolu');  
      }, 3000);  
   });  
}

```

Ne vous inquiétez pas si vous ne pouvez pas le résoudre complètement. Dylan expliquera en détail comment faire. À la fin de la leçon, vous serez suffisamment confiant pour commencer à l'utiliser immédiatement.

### Partie #22 : Ensembles

Dans la dernière leçon du cours, vous apprendrez une structure de données très importante, Set. Il s'agit d'un objet qui vous permet de stocker des valeurs uniques. Ainsi, chaque fois que vous souhaitez avoir une collection contenant uniquement des valeurs uniques, vous pouvez utiliser des Sets.

```js
const set1 = new Set([1, 2, 3, 4, 5]);

```

### Partie #23 : Qu'est-ce qui suit ?

![Cliquez sur l'image pour accéder au cours](https://cdn-media-1.freecodecamp.org/images/1*R6H7A7OZqNdCyeN6EXIEPA.png)

Pour conclure le cours, Dylan donne quelques conseils sur la manière de poursuivre cet apprentissage et d'améliorer le code que vous écrivez aujourd'hui.

Et c'est tout ! Si vous arrivez jusqu'ici, vous pouvez vous donner une tape dans le dos ! Vous avez terminé le cours et êtes un peu plus proche de devenir un ninja JavaScript.

Merci d'avoir lu ! Je m'appelle Per, je suis le cofondateur de [Scrimba](https://scrimba.com), et j'adore aider les gens à apprendre de nouvelles compétences. Suivez-moi sur [Twitter](https://twitter.com/perborgen) si vous souhaitez être informé des nouveaux articles et ressources.

---

Merci d'avoir lu ! Je m'appelle Per Borgen, je suis le cofondateur de [Scrimba](https://scrimba.com) – la manière la plus facile d'apprendre à coder. Vous devriez consulter notre [bootcamp de conception web responsive](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gintrotoes6_launch_article) si vous souhaitez apprendre à construire des sites web modernes de manière professionnelle.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Cliquez ici pour accéder au bootcamp avancé.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gintrotoes6_launch_article)_