---
title: Concepts JavaScript essentiels à connaître avant d'apprendre React
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-01-27T20:34:48.000Z'
originalURL: https://freecodecamp.org/news/top-javascript-concepts-to-know-before-learning-react
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/Yellow-and-Purple-Geometric-Covid-19-General-Facts-Twitter-Post-3.jpg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: Concepts JavaScript essentiels à connaître avant d'apprendre React
seo_desc: 'If you want to learn React – or any JavaScript framework – you''ll first
  need to understand the fundamental JavaScript methods and concepts.

  Otherwise it''s like a youngster learning to run before learning to walk.

  Many developers choose a "learn as yo...'
---

Si vous souhaitez apprendre React – ou tout autre framework JavaScript – vous devrez d'abord comprendre les méthodes et concepts fondamentaux de JavaScript.

Sinon, c'est comme un jeune qui apprend à courir avant d'apprendre à marcher.

De nombreux développeurs choisissent une approche "apprendre en cours de route" lorsqu'ils apprennent React. Mais cela ne résulte souvent pas en productivité, et aggrave plutôt les lacunes dans leurs connaissances JavaScript. Cette approche rend l'assimilation de chaque nouvelle fonctionnalité deux fois plus difficile (vous pourriez commencer à confondre JavaScript avec React).

React est un framework JavaScript pour construire des interfaces utilisateur basées sur des composants. Tout son code est écrit en JavaScript, y compris le balisage HTML, qui est écrit en JSX (ceci permet aux développeurs d'écrire facilement HTML et JavaScript ensemble).

Dans cet article, nous allons adopter une approche pratique et passer en revue toutes les idées et techniques JS que vous devrez comprendre avant d'apprendre React.

React est construit en utilisant des fonctionnalités modernes de JavaScript, qui ont été principalement introduites avec ES2015. C'est donc essentiellement ce dont nous allons discuter dans cet article. Pour vous aider à approfondir votre apprentissage, je vais connecter des liens distincts à chaque méthode et concept.

*Commençons…*

# Le JavaScript que vous devez connaître avant d'apprendre React

## Fonctions de rappel (Callback) en JavaScript

Une fonction de rappel est une fonction qui est exécutée après qu'une autre fonction a terminé son exécution. Elle est généralement fournie comme entrée dans une autre fonction.

Les rappels sont essentiels à comprendre car ils sont utilisés dans les méthodes de tableau (telles que `map()`, `filter()`, et ainsi de suite), `setTimeout()`, les écouteurs d'événements (comme clic, défilement, et ainsi de suite), et bien d'autres endroits.

Voici un exemple d'un écouteur d'événement "clic" avec une fonction de rappel qui sera exécutée chaque fois que le bouton est cliqué :

```javascript
//HTML
<button class="btn">Cliquez-moi</button>

//JavaScript
const btn = document.querySelector('.btn');

btn.addEventListener('click', () => {
  let name = 'John doe';
  console.log(name.toUpperCase())
})
```

> **NB :** Une fonction de rappel peut être soit une fonction ordinaire, soit une fonction fléchée.

## Promesses (Promises) en JavaScript

Comme mentionné précédemment, une fonction de rappel est exécutée après que la fonction originale est exécutée. Vous pouvez maintenant commencer à envisager d'empiler autant de fonctions de rappel les unes sur les autres parce que vous ne voulez pas qu'une fonction spécifique s'exécute tant que la fonction parente n'a pas terminé son exécution ou qu'un temps spécifique ne s'est pas écoulé.

Par exemple, essayons d'afficher 5 noms dans la console après 2 secondes chacun – c'est-à-dire, le premier nom apparaît après 2 secondes, le deuxième après 4 secondes, et ainsi de suite...

```javascript
setTimeout(() => {
    console.log("Joel");
    setTimeout(() => {
        console.log("Victoria");
        setTimeout(() => {
            console.log("John");
            setTimeout(() => {
                console.log("Doe");
                setTimeout(() => {
                    console.log("Sarah");
                }, 2000);
            }, 2000);
        }, 2000);
    }, 2000);
}, 2000);
```

Cet exemple ci-dessus fonctionnera, mais il sera difficile à comprendre, à déboguer, ou même à ajouter une gestion des erreurs. Cela est appelé le \*\*"Callback Hell"\*\*. Le callback hell est un gros problème causé par la programmation avec des rappels imbriqués complexes.

La raison principale d'utiliser les promesses est d'éviter le callback hell. Avec les promesses, nous pouvons écrire du code asynchrone de manière synchrone.

**À noter :** Vous pouvez apprendre ce que signifient synchrone et asynchrone en JavaScript via [cet article](https://www.freecodecamp.org/news/synchronous-vs-asynchronous-in-javascript/) par [TAPAS ADHIKARY](https://www.freecodecamp.org/news/author/tapas/).

Une promesse est un objet qui retourne une valeur que vous vous attendez à voir à l'avenir mais que vous ne voyez pas maintenant.

Une utilisation pratique des promesses serait dans les requêtes HTTP, où vous soumettez une requête et ne recevez pas de réponse immédiatement car c'est une activité asynchrone. Vous ne recevez la réponse (données ou erreur) que lorsque le serveur répond.

Syntaxe des promesses JavaScript :

```javascript
const myPromise = new Promise((resolve, reject) => {  
    // condition
});
```

Les promesses ont deux paramètres, un pour le succès (resolve) et un pour l'échec (reject). Chacun a une condition qui doit être satisfaite pour que la promesse soit résolue – sinon, elle sera rejetée :

```javascript
const promise = new Promise((resolve, reject) => {  
    let condition;
    
    if(condition is met) {    
        resolve('La promesse est résolue avec succès.');  
    } else {    
        reject('La promesse est rejetée');  
    }
});
```

Il y a 3 états de l'objet Promise :

* **En attente (Pending) :** par défaut, c'est l'état initial, avant que la promesse ne réussisse ou n'échoue.
    
* **Résolue (Resolved) :** Promesse complétée
    
* **Rejetée (Rejected) :** Promesse échouée
    

Enfin, essayons de réimplémenter le callback hell en tant que promesse :

```javascript
function addName (time, name){
  return new Promise ((resolve, reject) => {
    if(name){
      setTimeout(()=>{
        console.log(name)
        resolve();
      },time)
    }else{
      reject('Aucun nom de ce type');
    }
  })
}

addName(2000, 'Joel')
  .then(()=>addName(2000, 'Victoria'))
  .then(()=>addName(2000, 'John'))
  .then(()=>addName(2000, 'Doe'))
  .then(()=>addName(2000, 'Sarah'))
  .catch((err)=>console.log(err))
```

Vous pouvez consulter [cet article](https://www.freecodecamp.org/news/javascript-es6-promises-for-beginners-resolve-reject-and-chaining-explained/) par [Cem Eygi](https://www.freecodecamp.org/news/author/cemeygi/) pour mieux comprendre les promesses.

## Map() en JavaScript

L'une des méthodes les plus souvent utilisées est `Array.map()`, qui vous permet d'itérer sur un tableau et de modifier ses éléments en utilisant une fonction de rappel. La fonction de rappel sera exécutée sur chaque élément du tableau.

Supposons que nous avons un tableau d'utilisateurs qui contient leurs informations.

```javascript
let users = [
  { firstName: "Susan", lastName: "Steward", age: 14, hobby: "Singing" },
  { firstName: "Daniel", lastName: "Longbottom", age: 16, hobby: "Football" },
  { firstName: "Jacob", lastName: "Black", age: 15, hobby: "Singing" }
];
```

Nous pouvons parcourir en utilisant map et modifier sa sortie

```javascript
let singleUser = users.map((user)=>{
  // ajoutons le prénom et le nom ensemble
  let fullName = user.firstName + ' ' + user.lastName;
  return `
    <h3 class='name'>${fullName}</h3>
    <p class="age">${user.age}</p>
  `
});
```

Vous devez noter que :

* `map()` retourne toujours un nouveau tableau, même s'il s'agit d'un tableau vide.
    
* Il ne change pas la taille du tableau original par rapport à la méthode filter
    
* Il utilise toujours les valeurs de votre tableau original lors de la création d'un nouveau.
    

**À noter :** La méthode map fonctionne presque comme tout autre itérateur JavaScript tel que `forEach()` mais il est approprié d'utiliser toujours la méthode map chaque fois que vous allez **retourner** une valeur.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-83.png align="left")

*Voici une description parfaite par [Simon Høiberg](https://www.linkedin.com/in/simonhoiberg?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAAB5jWWUBOCaKeVgc2EIi88ksmqZBpvsi930&lipi=urn%3Ali%3Apage%3Ad_flagship3_detail_base%3BT8SFpAr6QJeDVQ2s0XRfgg%3D%3D&licu=urn%3Ali%3Acontrol%3Ad_flagship3_detail_base-actor_container&lici=cWhtZHO%2BTnmbu6ZNSGKubw%3D%3D)*

L'une des principales raisons pour lesquelles nous utilisons map est de pouvoir encapsuler nos données dans du HTML, alors que pour React cela se fait simplement en utilisant JSX.

Vous pouvez lire plus sur map() [ici](https://www.freecodecamp.org/news/javascript-map-how-to-use-the-js-map-function-array-method/).

## Filter() et Find() en JavaScript

`Filter()` fournit un nouveau tableau en fonction de certains critères. Contrairement à map(), il peut modifier la taille du nouveau tableau, tandis que `find()` retourne une seule instance (cela peut être un objet ou un élément). Si plusieurs correspondances existent, il retourne la première correspondance – sinon, il retourne indéfini.

Supposons que vous avez une collection de tableaux d'utilisateurs enregistrés avec différents âges :

```javascript
let users = [
  { firstName: "Susan", age: 14 },
  { firstName: "Daniel", age: 16 },
  { firstName: "Bruno", age: 56 },
  { firstName: "Jacob", age: 15 },
  { firstName: "Sam", age: 64 },
  { firstName: "Dave", age: 56 },
  { firstName: "Neils", age: 65 }
];
```

Vous pourriez choisir de trier ces données par groupes d'âge, comme les jeunes individus (âges 1-15), les personnes âgées (âges 50-70), et ainsi de suite...

Dans ce cas, la fonction filter est utile car elle produit un nouveau tableau basé sur les critères. Jetons un coup d'œil à son fonctionnement.

```javascript
// pour les jeunes
const youngPeople = users.filter((person) => {
  return person.age <= 15;
});

// pour les personnes âgées
const seniorPeople = users.filter((person) => person.age >= 50);

console.log(seniorPeople);
console.log(youngPeople);
```

Cela génère un nouveau tableau. Il produit un tableau vide si la condition n'est pas satisfaite (aucune correspondance).

Vous pouvez lire plus à ce sujet [ici](https://www.freecodecamp.org/news/javascript-array-filter-tutorial-how-to-iterate-through-elements-in-an-array/).

### Find()

La méthode `find()`, comme la méthode `filter()`, itère à travers le tableau à la recherche d'une instance/élément qui répond à la condition spécifiée. Une fois qu'elle l'a trouvé, elle retourne cet élément de tableau spécifique et termine immédiatement la boucle. Si aucune correspondance n'est découverte, la fonction retourne indéfini.

**Par exemple :**

```javascript
const Bruno = users.find((person) => person.firstName === "Bruno");

console.log(Bruno);
```

Vous pouvez lire plus sur la méthode find() [ici](https://www.freecodecamp.org/news/javascript-array-find-tutorial-how-to-iterate-through-elements-in-an-array/).

## Déstructuration des tableaux et objets en JavaScript

La déstructuration est une fonctionnalité JavaScript introduite dans ES6 qui permet un accès plus rapide et plus simple aux variables des tableaux et objets, ainsi que leur déballage.

Avant l'introduction de la déstructuration, si nous avions un tableau de fruits et que nous voulions obtenir les premier, deuxième et troisième fruits séparément, nous aurions fini avec quelque chose comme ceci :

```javascript
let fruits= ["Mango", "Pineapple" , "Orange", "Lemon", "Apple"];

let fruit1 = fruits[0];
let fruit2 = fruits[1];
let fruit3 = fruits[2];

console.log(fruit1, fruit2, fruit3); //"Mango" "Pineapple" "Orange"
```

C'est comme répéter la même chose encore et encore, ce qui pourrait devenir fastidieux. Voyons comment cela pourrait être déstructuré pour obtenir les trois premiers fruits.

```javascript
let [fruit1, fruit2, fruit3] = fruits;

console.log(fruit1, fruit2, fruit3); //"Mango" "Pineapple" "Orange"
```

Vous pourriez vous demander comment vous pourriez sauter des données si vous voulez simplement imprimer les premier et dernier fruits, ou les deuxième et quatrième fruits. Vous utiliseriez des virgules comme suit :

```bash
const [fruit1 ,,,, fruit5] = fruits;
const [,fruit2 ,, fruit4,] = fruits;
```

### Déstructuration d'objet

Voyons maintenant comment nous pourrions déstructurer un objet – car dans React vous allez faire beaucoup de déstructuration d'objets.

Supposons que nous avons un objet utilisateur qui contient son prénom, son nom de famille, et bien plus encore,

```javascript
const Susan = {
  firstName: "Susan",
  lastName: "Steward",
  age: 14,
  hobbies: {
    hobby1: "singing",
    hobby2: "dancing"
  }
};
```

Dans l'ancienne méthode, obtenir ces données pouvait être stressant et plein de répétitions :

```javascript
const firstName = Susan.firstName;
const age = Susan.age;
const hobby1 = Susan.hobbies.hobby1;

console.log(firstName, age, hobby1); //"Susan" 14 "singing"
```

mais avec la déstructuration, c'est beaucoup plus facile :

```javascript
const {firstName, age, hobbies:{hobby1}} = Susan;

console.log(firstName, age, hobby1); //"Susan" 14 "singing"
```

Nous pouvons aussi faire cela dans une fonction :

```javascript
function individualData({firstName, age, hobbies:{hobby1}}){
  console.log(firstName, age, hobby1); //"Susan" 14 "singing"
}
individualData(Susan);
```

Vous pouvez lire plus sur la déstructuration des tableaux et objets [ici](https://www.freecodecamp.org/news/array-and-object-destructuring-in-javascript/).

## Opérateurs Rest et Spread en JavaScript

Les opérateurs spread et rest de JavaScript utilisent trois points `...`. L'opérateur rest rassemble ou collecte des éléments – il place le "reste" de certaines valeurs spécifiques fournies par l'utilisateur dans un tableau/objet JavaScript.

Supposons que vous avez un tableau de fruits :

```javascript
let fruits= ["Mango", "Pineapple" , "Orange", "Lemon", "Apple"];
```

Nous pourrions déstructurer pour obtenir les premier et deuxième fruits et ensuite placer le "reste" des fruits dans un tableau en utilisant l'opérateur rest.

```javascript
const [firstFruit, secondFruit, ...rest] = fruits

console.log(firstFruit, secondFruit, rest); //"Mango" "Pineapple" ["Orange","Lemon","Apple"]
```

En regardant le résultat, vous verrez les deux premiers éléments et ensuite le troisième élément est un tableau composé des fruits restants que nous n'avons pas déstructurés. Nous pouvons maintenant effectuer tout type de traitement sur le nouveau tableau généré, comme :

```javascript
const chosenFruit = rest.find((fruit) => fruit === "Apple");

console.log(`This is an ${chosenFruit}`); //"This is an Apple"
```

Il est important de garder à l'esprit que cela doit toujours venir en dernier (le placement est très important).

Nous avons travaillé avec des tableaux – maintenant, traitons avec des objets, qui sont absolument les mêmes.

Supposons que nous avions un objet utilisateur qui a son prénom, son nom de famille, et bien plus. Nous pourrions le déstructurer et ensuite extraire le reste des données.

```javascript
const Susan = {
  firstName: "Susan",
  lastName: "Steward",
  age: 14,
  hobbies: {
    hobby1: "singing",
    hobby2: "dancing"
  }
};

const {age, ...rest} = Susan;
console.log(age, rest);
```

Cela journalisera le résultat suivant :

```javascript
14
{
firstName: "Susan" ,
lastName: "Steward" ,
hobbies: {...}
}
```

Comprenons maintenant comment fonctionne l'opérateur spread, et résumons enfin en différenciant les deux opérateurs.

### Opérateur Spread

L'opérateur spread, comme son nom l'indique, est utilisé pour étaler les éléments d'un tableau. Il nous donne la capacité d'obtenir une liste de paramètres à partir d'un tableau. L'opérateur spread a une syntaxe similaire à l'opérateur rest, sauf qu'il fonctionne dans le sens opposé.

**Note :** Un opérateur spread est efficace uniquement lorsqu'il est utilisé dans des littéraux de tableau, des appels de fonction, ou des objets de propriétés initialisés.

Par exemple, supposons que vous avez des tableaux de différents types d'animaux :

```javascript
let pets= ["cat", "dog" , "rabbits"];

let carnivorous = ["lion", "wolf", "leopard", "tiger"];
```

Vous pourriez vouloir combiner ces deux tableaux en un seul tableau d'animaux. Essayons :

```javascript
let animals = [pets, carnivorous];

console.log(animals); //[["cat", "dog" , "rabbits"], ["lion", "wolf", "leopard", "tiger"]]
```

Ce n'est pas ce que nous voulons – nous voulons tous les éléments dans un seul tableau. Et nous pouvons y parvenir en utilisant l'opérateur spread :

```javascript
let animals = [...pets, ...carnivorous];

console.log(animals); //["cat", "dog" , "rabbits", "lion", "wolf", "leopard", "tiger"]
```

Cela fonctionne également avec les objets. Il est important de noter que l'opérateur spread ne peut pas étendre les valeurs des littéraux d'objet, puisque un objet de propriétés n'est pas un itérable. Mais nous pouvons l'utiliser pour cloner des propriétés d'un objet dans un autre.

Par exemple :

```javascript
let name = {firstName:"John", lastName:"Doe"};
let hobbies = { hobby1: "singing", hobby2: "dancing" }
let myInfo = {...name, ...hobbies};

console.log(myInfo); //{firstName:"John", lastName:"Doe", hobby1: "singing", hobby2: "dancing"}
```

Vous pouvez lire plus sur les opérateurs Spread et Rest de JavaScript [ici](https://www.freecodecamp.org/news/javascript-rest-vs-spread-operators/).

## Valeur unique - Set() en JavaScript

Récemment, j'ai essayé de créer un onglet de catégories pour une application où j'avais besoin de récupérer les valeurs de catégories à partir d'un tableau.

```javascript
let animals = [
  {
    name:'Lion',
    category: 'carnivore'
  },
  {
    name:'dog',
    category:'pet'
  },
  {
    name:'cat',
    category:'pet'
  },
  {
    name:'wolf',
    category:'carnivore'
  }
]
```

La première chose était de parcourir le tableau, mais j'ai obtenu des valeurs répétées :

```javascript
let category = animals.map((animal)=>animal.category);
console.log(category); //["carnivore" , "pet" , "pet" , "carnivore"]
```

Cela signifiait que je devais mettre en place une condition pour éviter la répétition. C'était un peu délicat jusqu'à ce que je tombe sur le constructeur/objet `set()` fourni par ES6 :).

Un set est une collection d'éléments qui sont uniques, c'est-à-dire qu'aucun élément ne peut être répété. Voyons comment nous pouvons implémenter cela facilement.

```javascript
// enveloppez votre itération dans la méthode set comme ceci
let category = [...new Set(animals.map((animal)=>animal.category))];

console.log(category); ////["carnivore" , "pet"]
```

**NB :** J'ai décidé de répandre les valeurs dans un tableau. Vous pouvez lire plus sur les valeurs uniques [ici](https://www.geeksforgeeks.org/sets-in-javascript/).

## Clés d'objet dynamiques en JavaScript

Cela nous permet d'ajouter des clés d'objet en utilisant la notation entre crochets. Cela peut ne pas avoir de sens pour vous maintenant, mais à mesure que vous continuez à apprendre React ou commencez à travailler avec des équipes, vous pourriez en rencontrer.

En JavaScript, nous savons que les objets sont souvent composés de propriétés/clés et de valeurs, et nous pouvons utiliser la notation par points pour ajouter, modifier ou accéder à certaines valeurs. Par exemple :

```javascript
let lion = {
  category: "carnivore"
};

console.log(lion); // { category: "carnivore" }
lion.baby = 'cub';
console.log(lion.category); // carnivore
console.log(lion); // { category: "carnivore" , baby: "cub" }
```

Nous avons également la possibilité d'utiliser la notation entre crochets, qui est utilisée lorsque nous avons besoin de **clés d'objet dynamiques**.

**Que voulons-nous dire par clés d'objet dynamiques ?** Ce sont des clés qui ne suivent peut-être pas la convention de nommage standard des propriétés/clés dans un objet. La [convention de nommage standard](https://stackoverflow.com/questions/55413572/what-is-the-standard-naming-convention-of-properties-in-a-object-camelcase-or-s) ne permet que le camelCase et le snake_case, mais en utilisant la notation entre crochets, nous pouvons résoudre ce problème.

Par exemple, supposons que nous nommons notre clé avec un tiret entre les mots, par exemple (`lion-baby`) :

```javascript
let lion = {
  'lion-baby' : "cub"
};

// notation par points
console.log(lion.lion-baby); // erreur : ReferenceError: baby n'est pas défini
// notation entre crochets
console.log(lion['lion-baby']); // "cub"
```

Vous pouvez voir la différence entre la notation par points et la notation entre crochets. Regardons d'autres exemples :

```javascript
let category = 'carnivore';
let lion = {
  'lion-baby' : "cub",
  [category] : true,
};

console.log(lion); // { lion-baby: "cub" , carnivore: true }
```

Vous pouvez également effectuer des opérations plus complexes en utilisant des conditions dans les crochets, comme ceci :

```javascript
const number = 5;
const gavebirth = true;

let animal = {
  name: 'lion',
  age: 6,
  [gavebirth && 'babies']: number
};

console.log(animal); // { name: "lion" , age: 6 , babies: 5 }
```

Vous pouvez lire plus à ce sujet [ici](https://hackmamba.io/blog/2020/11/dynamic-javascript-object-keys/).

## reduce() en JavaScript

C'est probablement la fonction de tableau la plus puissante. Elle peut remplacer les méthodes `filter()` et `find()` et est également très utile lorsque l'on utilise les méthodes `map()` et `filter()` sur de grandes quantités de données.

Lorsque vous enchaînez les méthodes map et filter ensemble, vous finissez par faire le travail deux fois – d'abord en filtrant chaque valeur individuelle puis en mappant les valeurs restantes. D'autre part, `reduce()` vous permet de filtrer et de mapper en une seule passe. Cette méthode est puissante, mais elle est aussi un peu plus sophistiquée et délicate.

Nous itérons sur notre tableau puis obtenons une fonction de rappel, qui est similaire à `map()`, `filter()`, `find()`, et les autres. La principale distinction est qu'elle réduit notre tableau à une seule valeur, qui peut être un nombre, un tableau ou un objet.

Une autre chose à garder à l'esprit concernant la méthode reduce() est que nous passons deux arguments, ce qui n'a pas été le cas depuis que vous avez commencé à lire ce tutoriel.

Le premier argument est la somme/total de tous les calculs, et le second est la valeur de l'itération actuelle (que vous comprendrez bientôt).

Par exemple, supposons que nous avons une liste de salaires pour notre personnel :

```javascript
let staffs = [
  { name: "Susan", age: 14, salary: 100 },
  { name: "Daniel", age: 16, salary: 120 },
  { name: "Bruno", age: 56, salary: 400 },
  { name: "Jacob", age: 15, salary: 110 },
  { name: "Sam", age: 64, salary: 500 },
  { name: "Dave", age: 56, salary: 380 },
  { name: "Neils", age: 65, salary: 540 }
];
```

Et nous voulons calculer une dîme de 10% pour tout le personnel. Nous pourrions facilement faire cela avec la méthode reduce, mais avant de le faire, faisons quelque chose de plus simple : calculons d'abord le salaire total.

```javascript
const totalSalary = staffs.reduce((total, staff) => {
  total += staff.salary;
  return total;
},0)
console.log(totalSalary); // 2150
```

NB : Nous avons passé un deuxième argument qui est le total, il pourrait être n'importe quoi – par exemple un nombre ou un objet.

Calculons maintenant la dîme de 10% pour tout le personnel et obtenons le total. Nous pourrions simplement obtenir 10% du total ou d'abord l'obtenir de chaque salaire avant de les additionner.

```javascript
const salaryInfo = staffs.reduce(
  (total, staff) => {
    let staffTithe = staff.salary * 0.1;
    total.totalTithe += staffTithe;
    total['totalSalary'] += staff.salary;
    return total;
  },
  { totalSalary: 0, totalTithe: 0 }
);

console.log(salaryInfo); // { totalSalary: 2150 , totalTithe: 215 }
```

**À noter :** Nous avons utilisé un objet comme deuxième argument et nous avons également utilisé des clés d'objet dynamiques. Vous pouvez lire plus sur la méthode reduce [ici](https://www.freecodecamp.org/news/reduce-f47a7da511a9/).

## Chaînage optionnel en JavaScript

Le chaînage optionnel est un moyen sûr d'accéder aux propriétés d'objet imbriquées en JavaScript plutôt que de devoir effectuer plusieurs vérifications de nullité lors de l'accès à une longue chaîne de propriétés d'objet. C'est une nouvelle fonctionnalité introduite dans ES2020.

Par exemple :

```javascript
let users = [
{
    name: "Sam",
    age: 64,
    hobby: "cooking",
    hobbies: {
      hobb1: "cooking",
      hobby2: "sleeping"
    }
  },
  { name: "Bruno", age: 56 },
  { name: "Dave", age: 56, hobby: "Football" },
  {
    name: "Jacob",
    age: 65,
    hobbies: {
      hobb1: "driving",
      hobby2: "sleeping"
    }
  }
];
```

Supposons que vous essayez d'obtenir les hobbies du tableau ci-dessus. Essayons :

```javascript
users.forEach((user) => {
  console.log(user.hobbies.hobby2);
});
```

Lorsque vous regardez dans votre console, vous remarquerez que la première itération a été complétée, mais que la deuxième itération n'avait pas de hobby. Elle a donc dû lancer une erreur et sortir de l'itération – ce qui signifiait qu'elle ne pouvait pas acquérir de données à partir d'autres objets dans le tableau.

**Sortie :**

```bash
"sleeping"
erreur : Uncaught TypeError: user.hobbies est indéfini
```

Cette erreur peut être corrigée avec le chaînage optionnel, bien qu'il existe plusieurs méthodes pour la corriger (par exemple, en utilisant des conditions). Voyons comment nous pourrions faire cela avec des conditions et un chaînage optionnel :

### Méthode de rendu conditionnel :

```javascript
users.forEach((user) => {
  console.log(user.hobbies && user.hobbies.hobby2);
});
```

### Chaînage optionnel :

```javascript
users.forEach((user) => {
  console.log(user ?.hobbies ?.hobby2);
});
```

Sortie :

```bash
"sleeping"
indéfini
indéfini
"sleeping"
```

Cela peut ne pas vraiment avoir de sens pour vous maintenant, mais au moment où vous travaillerez sur quelque chose de plus grand à l'avenir, cela se mettra en place ! Vous pouvez lire plus [ici](https://www.freecodecamp.org/news/javascript-optional-chaining-explained/).

## Fetch API & Erreurs en JavaScript

L'API Fetch, comme son nom l'indique, est utilisée pour obtenir des données à partir d'API. C'est une API de navigateur qui vous permet d'utiliser JavaScript pour faire des requêtes AJAX (Asynchronous JavaScript and XML) de base.

Parce qu'elle est fournie par le navigateur, vous pouvez l'utiliser sans avoir à installer ou importer de packages ou de dépendances (comme axios). Sa configuration est assez simple à comprendre. L'API Fetch livre une promesse par défaut (j'ai couvert les promesses plus tôt dans cet article).

Voyons comment récupérer des données via l'API Fetch. Nous utiliserons une API gratuite qui contient des milliers de citations aléatoires :

```javascript
fetch("https://type.fit/api/quotes")
  .then((response) => response.json())
  .then((data) => console.log(data))
  .catch((err) => console.log(err));
```

Ce que nous avons fait ici :

* **Ligne 1 :** nous avons obtenu les données de l'API, qui a retourné une promesse
    
* **Ligne 2 :** Nous avons ensuite obtenu le format `.json()` des données qui est également une promesse
    
* **Ligne 3 :** Nous avons obtenu nos données qui retournent maintenant du JSON
    
* **Ligne 4 :** Nous avons obtenu les erreurs au cas où il y en aurait
    

Nous verrons comment cela peut être fait avec async/await dans la section suivante. Vous pouvez lire plus sur l'API Fetch [ici](https://www.freecodecamp.org/news/how-to-make-api-calls-with-fetch/).

### Comment gérer les erreurs dans l'API Fetch

Examinons maintenant comment nous pouvons gérer les erreurs de l'API Fetch sans avoir besoin de dépendre du mot-clé catch. La fonction `fetch()` lancera automatiquement une erreur pour les erreurs réseau mais pas pour les erreurs HTTP telles que les réponses 400 à 5xx.

La bonne nouvelle est que `fetch` fournit un simple drapeau `response.ok` qui indique si la requête a échoué ou si le code de statut de la réponse HTTP est dans la plage de succès.

Cela est très simple à implémenter :

```javascript
fetch("https://type.fit/api/quotes")
  .then((response) => {
    if (!response.ok) {
      throw Error(response.statusText);
    }
    return response.json();
  })
  .then((data) => console.log(data))
  .catch((err) => console.log(err));
```

Vous pouvez lire plus sur les erreurs de l'API Fetch [ici](https://www.tjvantoll.com/2015/09/13/fetch-and-errors/).

## Async/Await en JavaScript

Async/Await nous permet d'écrire du code asynchrone de manière synchrone. Cela signifie que vous n'avez pas besoin de continuer à imbriquer des rappels.

Une fonction async **retourne toujours** une promesse.

Vous pourriez vous creuser la tête en vous demandant quelle est la différence entre synchrone et asynchrone. Simplement, synchrone signifie que les tâches sont effectuées les unes après les autres. Asynchrone signifie que les tâches sont effectuées indépendamment.

Notez que nous avons toujours async devant la fonction et que nous ne pouvons utiliser await que lorsque nous avons async. Vous comprendrez bientôt !

Implémentons maintenant le code de l'API Fetch sur lequel nous avons travaillé plus tôt en utilisant async/await :

```javascript
const fetchData = async () =>{
  const quotes = await fetch("https://type.fit/api/quotes");
  const response = await quotes.json();
  console.log(response);
}

fetchData();
```

C'est bien plus facile à lire, n'est-ce pas ?

Vous pourriez vous demander comment nous pouvons gérer les erreurs avec async/await. Oui ! Vous utilisez les mots-clés try et catch :

```javascript
const fetchData = async () => {
  try {
    const quotes = await fetch("https://type.fit/api/quotes");
    const response = await quotes.json();
    console.log(response);
  } catch (error) {
    console.log(error);
  }
};

fetchData();
```

Vous pouvez lire plus sur async/await [ici](https://www.freecodecamp.org/news/javascript-async-await-tutorial-learn-callbacks-promises-async-await-by-making-icecream/).

## Conclusion

Dans cet article, nous avons appris plus de 10 méthodes et concepts JavaScript que tout le monde devrait comprendre parfaitement avant d'apprendre React.

Il y a beaucoup d'autres méthodes et concepts que vous devriez connaître, mais ce sont ceux auxquels vous ne prêterez peut-être pas vraiment attention en apprenant JavaScript. Ceux-ci sont importants à comprendre avant d'apprendre React.

Supposons que vous commencez tout juste avec JavaScript – j'ai compilé une liste impressionnante de ressources qui vous aideront à apprendre les concepts et sujets JavaScript [ici](https://github.com/olawanlejoel/Awesome-Javascript). N'oubliez pas de mettre une étoile et de partager ! :).

Vous pouvez accéder à plus de 200 de mes articles en [visitant mon site web](https://joelolawanle.com/contents). Vous pouvez également utiliser le champ de recherche pour voir si j'ai écrit un article spécifique.