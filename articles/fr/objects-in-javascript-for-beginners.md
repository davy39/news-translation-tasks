---
title: Les objets en JavaScript – Un guide pour débutants
subtitle: ''
author: Damilola Oladele
co_authors: []
series: null
date: '2022-07-20T17:50:17.000Z'
originalURL: https://freecodecamp.org/news/objects-in-javascript-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/shelf4.jpg
tags:
- name: JavaScript
  slug: javascript
- name: object
  slug: object
seo_title: Les objets en JavaScript – Un guide pour débutants
seo_desc: 'If you declare multiple variables to hold different values, this can make
  your program messy and clunky.

  For instance, if you need to store three characteristics each for 10 individuals,
  having 30 variables individually declared can make your program...'
---

Si vous déclarez plusieurs variables pour contenir différentes valeurs, cela peut rendre votre programme désordonné et encombrant.

Par exemple, si vous devez stocker trois caractéristiques pour 10 individus, avoir 30 variables déclarées individuellement peut rendre votre programme moins organisé.

Vous avez donc besoin d'un moyen de regrouper des valeurs avec des caractéristiques similaires pour rendre votre code plus lisible. Et en JavaScript, les objets fonctionnent bien à cette fin.

Contrairement à d'autres types de données, les objets sont capables de stocker des valeurs complexes. Pour cette raison, JavaScript s'appuie fortement sur eux. Il est donc important que vous vous familiarisiez avec ce qu'est un objet, comment en créer un et comment vous pouvez l'utiliser avant d'approfondir l'apprentissage de JavaScript.

Cet article vous présentera les bases des objets, la syntaxe des objets, les différentes méthodes de création d'objets, comment copier des objets et comment itérer sur un objet.

Pour tirer le meilleur parti de cet article, vous devez avoir au moins une compréhension de base de JavaScript, en particulier des variables, des fonctions et des types de données.

## Qu'est-ce qu'un objet en JavaScript ?

Un objet est un type de données qui peut contenir des collections de paires clé-valeur.

Une différence majeure entre un objet et d'autres types de données tels que les chaînes de caractères et les nombres en JavaScript est qu'un objet peut stocker différents types de données comme valeurs. En revanche, les types de données primitifs tels que les nombres et les chaînes de caractères ne peuvent stocker que des nombres et des chaînes de caractères, respectivement, comme valeurs.

La clé, également connue sous le nom de nom de propriété, est généralement une chaîne de caractères. Si un autre type de données est utilisé comme nom de propriété autre que les chaînes de caractères, il serait converti en chaîne de caractères.

Vous pouvez visualiser un objet comme une étagère polyvalente contenant de l'espace pour vos gadgets et ornements ainsi qu'un espace de stockage pour les livres et les fichiers.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/shelf1-2.jpg align="left")

*Une étagère avec plusieurs objets dessus*

La caractéristique la plus reconnaissable d'un objet est les accolades qui contiennent la paire clé-valeur.

```javascript
const emptyObject = {};
console.log(typeof emptyObject); //'object'
```

Le contenu d'un objet peut être constitué de variables, de fonctions, ou des deux. Les variables trouvées dans les objets sont des propriétés, tandis que les fonctions sont des méthodes. Les méthodes permettent aux objets d'utiliser les propriétés qu'ils contiennent pour effectuer une sorte d'action.

Par exemple, dans le code ci-dessous, **object1.user**, **object1.nationality** et **object1.profession** sont toutes des propriétés de **object1** tandis que **object1.myBio()** est une méthode :

```javascript
const object1 = {
    user: "alex",
    nationality: "Nigeria",
    profession: "Software Engineer",
    myBio() {
        console.log(`My name is ${this.user}. I'm a ${this.profession} from ${this.nationality}`)
    }
}
console.log(object1.user); //Alex 
console.log(object1.nationality); //Nigeria 
console.log(object1.profession); //Software Engineer 
console.log(object1.myBio()); //My name is alex. I'm a Software Engineer from Nigeria
```

Les clés dans le code ci-dessus sont **user**, **nationality** et **profession** tandis que leurs valeurs sont les valeurs de chaîne qui suivent les deux-points. Remarquez également l'utilisation du mot-clé **this**. Le mot-clé **this** fait simplement référence à l'objet lui-même.

Comme mentionné précédemment dans cet article, la valeur d'une propriété peut être de n'importe quel type de données. Dans le code suivant, les valeurs sont à la fois des tableaux et des objets :

```javascript
 const object2 = { 
        users: ["Alex", "James", "Mohammed"], 
        professions: { 
            alex: "software engineer", 
            james: "lawyer", 
            mohammed: "technical writer" 
        } 
    }; 
    console.log(object2.users); //['Alex', 'James', 'Mohammed'] 
    console.log(object2.professions); //{alex: 'software engineer', james: 'lawyer', mohammed: 'technical writer'}
```

## Comment accéder aux objets et créer de nouvelles propriétés ou méthodes d'objet en JavaScript

Il existe deux façons d'accéder aux objets : la notation par point et la notation par crochets. Dans le code précédent, nous avons utilisé la notation par point pour accéder aux propriétés et méthodes dans **object1** et **object2**.

De plus, pour créer de nouvelles propriétés et méthodes après la déclaration d'un objet, vous pouvez utiliser soit la notation par point, soit la notation par crochets. Vous devez simplement indiquer la nouvelle propriété et lui donner une valeur.

Par exemple, nous pouvons ajouter de nouvelles propriétés à **object2** comme ceci :

```javascript
object2.ages = [30, 32, 40];
object2["summary"] = `Object2 has ${object2.users.length} users`;
console.log(object2);
/*
{
    "users": [
        "Alex",
        "James",
        "Mohammed"
    ],
    "professions": {
        "alex": "software engineer",
        "james": "lawyer",
        "mohammed": "technical writer"
    },
    "ages": [
        30,
        32,
        40
    ],
    "summary": "Object2 has 3 users"
}
*/
```

De même, vous pouvez utiliser l'une ou l'autre notation pour changer la valeur d'un objet :

```javascript
object2.users = ["jane", "Williams", "John"];
object2["age"] = [20, 25, 29]
console.log(object2.users); //['jane', 'Williams', 'John']
console.log(object2.ages) //[20, 25, 29]
```

Bien que la notation par point soit la plus couramment utilisée pour accéder aux propriétés et méthodes d'un objet, elle présente certaines limitations. Examinons-les maintenant.

### Vous ne pouvez pas utiliser des valeurs comme noms de propriété avec la notation par point

Si vous souhaitez utiliser la valeur d'une variable comme nom de propriété dans votre objet, vous devez utiliser la notation par crochets et non la notation par point. Que la valeur de la variable soit définie à l'exécution ou non n'a pas d'importance.

L'exécution est une phase d'un programme informatique dans laquelle le programme est exécuté sur un système informatique.

Par exemple :

```javascript
const object3 = {};
const gadget = prompt("enter a gadget type"); 
object3[gadget] = ["jbl", "sony"]; 
console.log(object3) //(réponse entrée dans la boîte de dialogue) : ["jbl","sony"] remarquez que le nom de la propriété est la valeur que vous entrez en réponse au message de la boîte de dialogue
```

Si vous définissez la valeur de la variable dans votre code, et que vous utilisez la notation par point pour définir cette valeur comme nom de propriété de votre objet, la notation par point créera une nouvelle propriété avec le nom de la variable au lieu de la valeur de la variable.

```javascript
const computer = "brands"
object3.computer = ["hp", "dell", "apple"]
console.log(object3.brands); //undefined
console.log(object3.computer)//['hp', 'dell', 'apple']

object3[computer] = ["hp", "dell", "apple"]
console.log(object3.brands) //['hp', 'dell', 'apple']
```

Remarquez l'omission des guillemets à l'intérieur des crochets. Cela est dû au fait que les crochets ont pris une variable.

### Vous ne pouvez pas utiliser des propriétés multi-mots avec la notation par point

Lorsque le nom de la propriété est une chaîne de caractères multi-mots, la notation par point est insuffisante. Par exemple :

```javascript
object3.users height = [5.6, 5.4, 6.0];
Console.log(object3.users height); //SyntaxError
```

Une erreur de syntaxe se produit parce que JavaScript lit la commande comme `object3.users`, mais la chaîne height n'est pas reconnue, donc elle retourne une erreur de syntaxe.

Lorsque vous utilisez la notation par point pour accéder aux objets, les règles habituelles de déclaration d'une variable s'appliquent. Cela signifie que si vous souhaitez utiliser la notation par point pour accéder à un objet ou créer une propriété, le nom de la propriété ne doit pas commencer par un nombre, ne doit pas inclure d'espaces, et ne peut inclure que les caractères spéciaux *$* et \_*.*

Pour éviter ce type d'erreur, vous devez utiliser la notation par crochets. Par exemple, vous pouvez corriger le code précédent comme ceci :

```javascript
object3["users height"] = [5.6, 5.4, 6.0];  
console.log(object3["users height"]); //[5.6, 5.4, 6]
```

## Comment créer des objets avec le constructeur d'objets en JavaScript

Il existe deux méthodes pour créer un objet : un littéral d'objet et le constructeur d'objets. Les objets utilisés jusqu'à présent comme exemples dans cet article sont des littéraux d'objets. Les littéraux d'objets fonctionnent bien si vous souhaitez créer un seul objet.

Mais si vous souhaitez créer plus d'un objet, il est toujours préférable d'utiliser le constructeur d'objets. Cela vous permet d'éviter les répétitions inutiles dans votre code et facilite également la modification des propriétés de votre objet.

En gros, les constructeurs sont des fonctions dont les noms sont généralement en majuscules. La majuscule du nom d'un constructeur n'a aucun effet sur l'objet. Ce n'est qu'un moyen d'identification.

Vous pouvez utiliser un constructeur pour créer un nouvel objet en appelant le constructeur avec le mot-clé **new**. Le mot-clé **new** créera une instance d'un objet et liera le mot-clé **this** au nouvel objet.

Comme mentionné précédemment dans cet article, le mot-clé **this** est une référence à l'objet lui-même.

Un exemple de constructeur d'objet est :

```javascript
function Profile(name, age, nationality) { 
    this.name = name; 
    this.age = age; 
    this.nationality = nationality; 
    this.bio = function () { 
        console.log(`My name is ${this.name}. I'm ${this.age} years old. I'm from ${this.nationality}`) 
    } 
};

const oladele = new Profile("Oladele", 50, "Nigeria" );
console.log(oladele.bio()); //My name is Oladele. I'm 50 years old. I'm from Nigeria
```

## Comment créer des copies d'objets en JavaScript

Contrairement aux types de données primitifs tels que les chaînes de caractères et les nombres, l'assignation d'un objet existant à une autre variable ne produira pas une copie de l'original mais plutôt une référence en mémoire.

Cela signifie que l'objet original et les objets ultérieurs créés en assignant l'objet original comme valeur référencent le même élément en mémoire.

Cela signifie qu'un changement dans la valeur de l'un des objets entraînera également un changement dans les autres. Par exemple :

```javascript
let x = 10;
let y = x;
x = 20;
console.log(x); //20
console.log(y); //10

let object4 = { 
    name: "Alex", 
    age: 40 
}; 
let object5 = object4; 
console.log(object5); //{name: 'Alex', age: 40} 
object4.name = "Jane"; 
console.log(object5); //{name: 'Jane', age: 40}
console.log(object4 === object5); //true
```

Pour créer une copie d'un objet, vous pouvez utiliser l'opérateur de décomposition.

### Qu'est-ce que l'opérateur de décomposition ?

L'opérateur de décomposition est représenté par trois points `...`. Vous pouvez utiliser l'opérateur de décomposition pour copier les valeurs de n'importe quel itérable, y compris les objets.

Un itérable est un objet qui peut être parcouru ou itéré à l'aide d'une boucle for...loop. Les exemples d'itérables incluent les objets, les tableaux, les ensembles, les chaînes de caractères, etc.

Pour utiliser l'opérateur de décomposition, vous devrez le préfixer à l'objet que vous souhaitez copier. Par exemple :

```javascript
let object6 = {...object5}; 
object5.name = "Willaims"; 
console.log(object5); //{name: 'Willaims', age: 40}
console.log(object6); //{name: 'Jane', age: 40}
console.log(object5 === object6); //false
```

Comme vous pouvez le voir, contrairement à l'exemple de code précédent, où un changement dans **object4** a provoqué un changement dans **object5**, le changement dans **object6** n'a pas entraîné de changement dans **object5**.

### Comment utiliser la méthode Object.assign()

La méthode **Object.assign()** copie toutes les propriétés énumérables d'un objet dans un autre, puis retourne l'objet modifié.

La méthode prend deux paramètres. Le premier paramètre est l'objet cible qui prend les propriétés copiées. Le deuxième paramètre est l'objet source qui contient les propriétés que vous souhaitez copier. Par exemple :

```javascript
let object7  = Object.assign({}, object6); 
console.log(object7); //{name: 'Jane', age: 40}
console.log(object7); //{name: 'Jane', age: 40}

console.log(object6 === object7); //false
object6.age = 60
console.log(object6); //{name: 'Jane', age: 60}
console.log(object7); //{name: 'Jane', age: 40}
```

Vous pouvez voir dans le code ci-dessus qu'un changement dans la valeur de la propriété **age** de **object6** n'a pas provoqué de changement dans la valeur de la propriété **age** de **object7**.

Notez que l'opérateur de décomposition et la méthode **Object.assign()** ne peuvent faire qu'une copie superficielle d'un objet.

Cela signifie que si vous avez des objets ou des tableaux profondément imbriqués dans votre objet source, seules les références à ces objets sont copiées dans l'objet cible. Ainsi, un changement dans la valeur de l'un des objets profondément imbriqués provoquerait un changement dans la valeur de l'objet profondément imbriqué de l'autre. Par exemple :

```javascript
let objectX = {
    name: 'Mary', 
    age: 40,
    gadgets: { 
        brand: ["apple", "sony"]
    }
};

let objectY = {...objectX};
objectY.name = "Bianca";
objectY.gadgets.brand[0] = "hp";
console.log(objectX);
/*
{
    "name": "Mary",
    "age": 40,
    "gadgets": {
        "brand": [
            "hp",
            "sony"
        ]
    }
}
*/ 

console.log(objectY);
/*
{
    "name": "Bianca",
    "age": 40,
    "gadgets": {
        "brand": [
            "hp",
            "sony"
        ]
    }
}
*/
```

Le code ci-dessus a effectué les actions suivantes :

1. Créé un objet nommé **objectX**.

2. Donné trois propriétés à **objectX** : name, age et gadgets.

3. Donné à la propriété **gadgets** de **objectX** un objet comme valeur.

4. Donné à la valeur objet de la propriété **gadget** une propriété **brand**.

5. Donné à la propriété **brand** un tableau comme valeur.

6. Copié les propriétés de **objectX** dans **objectY** avec l'utilisation de l'opérateur de décomposition.

7. Changé la valeur de la propriété **name** de **objectY** en **Mary**.

8. Changé le premier élément dans la valeur de tableau de la propriété **brand** de **apple** à **hp**.

Dans le code ci-dessus, la valeur de tableau est un objet profondément imbriqué. Remarquez qu'un changement dans la valeur de la propriété **name** de **objectY** n'a pas provoqué de changement dans la valeur de la propriété **name** de **objectX**. Mais un changement dans l'objet profondément imbriqué de **objectY** a provoqué un changement similaire dans l'objet profondément imbriqué de **objectX**.

## Comment itérer sur les objets en JavaScript

Utilisez une boucle **for...in** pour itérer sur un objet et sélectionner ses propriétés. La syntaxe de la boucle **for..in** est la suivante :

```javascript
for(let key in object) {
    //perform action(s) for each key
}
```

Le mot-clé **key** dans la syntaxe ci-dessus est un paramètre pour les propriétés. Vous pouvez donc le remplacer par n'importe quel mot de votre choix. Remplacez le mot-clé object par le nom de l'objet sur lequel vous souhaitez itérer. Par exemple :

```javascript
let objectZ = {
    name: "Ade",
    Pronuon: "he",
    age: 60
};
for(let property in objectZ) {
    console.log(`${property}: ${objectZ[property]}`)
}
/* 
name: Ade
Pronuon: he
age: 60
*/
```

Remarquez l'utilisation de la notation par crochets dans la boucle pour obtenir les valeurs de la propriété. L'utilisation de la notation par point au lieu de la notation par crochets retournerait undefined.

## Conclusion

En JavaScript, les objets sont probablement le type de données le plus important. Les concepts de programmation comme la programmation orientée objet fonctionnent sur le principe de tirer parti de la flexibilité des objets pour stocker des valeurs complexes et de leur capacité distincte d'interagir avec les propriétés et méthodes au sein de l'objet.

Cet article pose une base solide pour comprendre de tels concepts avancés en expliquant les bases des objets.