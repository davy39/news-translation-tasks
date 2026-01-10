---
title: Comment utiliser la déstructuration de tableaux et d'objets en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-05T18:54:13.000Z'
originalURL: https://freecodecamp.org/news/array-and-object-destructuring-in-javascript
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9bc8740569d1a4ca2de5.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment utiliser la déstructuration de tableaux et d'objets en JavaScript
seo_desc: 'By Sarah Chima Atuonwu

  The destructuring assignment is a cool feature that came along with ES6. Destructuring
  is a JavaScript expression that makes it possible to unpack values from arrays,
  or properties from objects, into distinct variables. That is...'
---

Par Sarah Chima Atuonwu

L'affectation par déstructuration est une fonctionnalité cool qui est arrivée avec ES6. La déstructuration est une expression JavaScript qui permet de déballer des valeurs de tableaux, ou des propriétés d'objets, dans des variables distinctes. C'est-à-dire que nous pouvons extraire des données de tableaux et d'objets et les assigner à des variables. 

Pourquoi est-ce nécessaire ?

Imaginez que nous voulons extraire des données d'un tableau. Auparavant, comment cela aurait-il été fait ?

```javascript
let introduction = ["Hello", "I" , "am", "Sarah"];
let greeting = introduction[0];
let name = introduction[3];

console.log(greeting);//"Hello"
console.log(name);//"Sarah"

```

Nous pouvons voir que lorsque nous voulons extraire des données d'un tableau, nous devons faire la même chose encore et encore. 

L'affectation par déstructuration ES6 facilite l'extraction de ces données. Comment cela se fait-il ? Tout d'abord, nous allons discuter de l'affectation par déstructuration avec les tableaux. Ensuite, nous passerons à la déstructuration d'objets. 

Commençons.

## Déstructuration de base de tableau

Si nous voulons extraire des données de tableaux, c'est assez simple en utilisant l'affectation par déstructuration. 

Référons-nous à notre premier exemple pour les tableaux. Au lieu de passer par ce processus répétitif, nous ferions ceci :

```javascript
let introduction = ["Hello", "I" , "am", "Sarah"];
let [greeting, pronoun] = introduction;

console.log(greeting);//"Hello"
console.log(pronoun);//"I"


```

Nous pouvons aussi faire ceci avec le même résultat.

```javascript
let [greeting, pronoun] = ["Hello", "I" , "am", "Sarah"];

console.log(greeting);//"Hello"
console.log(pronoun);//"I"
```

### Déclaration de variables avant l'affectation

Les variables peuvent être déclarées avant d'être assignées comme ceci :

```javascript

let greeting, pronoun;
[greeting, pronoun] = ["Hello", "I" , "am", "Sarah"];

console.log(greeting);//"Hello"
console.log(pronoun);//"I"


```

Remarquez que les variables sont définies de gauche à droite. Ainsi, la première variable obtient le premier élément du tableau, la deuxième variable obtient le deuxième élément du tableau, et ainsi de suite.

### Ignorer des éléments dans un tableau

Que se passe-t-il si nous voulons obtenir le premier et le dernier élément de notre tableau au lieu du premier et du deuxième élément, et que nous voulons assigner seulement deux variables ? Cela peut aussi être fait. Regardez l'exemple ci-dessous :

```javascript
let [greeting,,,name] = ["Hello", "I" , "am", "Sarah"];

console.log(greeting);//"Hello"
console.log(name);//"Sarah"


```

Que vient-il de se passer ? 

Regardez le tableau du côté gauche de l'affectation de variable. Remarquez que, au lieu d'avoir une seule virgule, nous en avons trois. Le séparateur de virgule est utilisé pour ignorer des valeurs dans un tableau. Donc, si vous voulez ignorer un élément dans un tableau, utilisez simplement une virgule.

Faisons-en un autre. Ignorons le premier et le troisième élément de la liste. Comment ferions-nous cela ?

```javascript
let [,pronoun,,name] = ["Hello", "I" , "am", "Sarah"];

console.log(pronoun);//"I"
console.log(name);//"Sarah"


```

Ainsi, le séparateur de virgule fait la magie. Donc, si nous voulons ignorer tous les éléments, nous faisons simplement ceci :

```javascript
let [,,,,] = ["Hello", "I" , "am", "Sarah"];


```

### Assigner le reste d'un tableau

Que se passe-t-il si nous voulons assigner une partie du tableau à des variables et le reste des éléments d'un tableau à une variable particulière ? Dans ce cas, nous ferions ceci :

```javascript
let [greeting,...intro] = ["Hello", "I" , "am", "Sarah"];

console.log(greeting);//"Hello"
console.log(intro);//["I", "am", "Sarah"]


```

En utilisant ce modèle, vous pouvez déballer et assigner la partie restante d'un tableau à une variable.

### Affectation par déstructuration avec des fonctions

Nous pouvons également extraire des données d'un tableau retourné par une fonction. Supposons que nous avons une fonction qui retourne un tableau comme dans l'exemple ci-dessous :

```javascript
function getArray() {
    return ["Hello", "I" , "am", "Sarah"];
} 
let [greeting,pronoun] = getArray();

console.log(greeting);//"Hello"
console.log(pronoun);//"I"

```

Nous obtenons les mêmes résultats.

### Utilisation de valeurs par défaut

Des valeurs par défaut peuvent être assignées aux variables au cas où la valeur extraite du tableau serait `undefined` :

```javascript
let [greeting = "hi",name = "Sarah"] = ["hello"];

console.log(greeting);//"Hello"
console.log(name);//"Sarah"

```

Ainsi, `name` revient à "Sarah" parce qu'il n'est pas défini dans le tableau.

### Échange de valeurs en utilisant l'affectation par déstructuration

Une dernière chose. Nous pouvons utiliser l'affectation par déstructuration pour échanger les valeurs de variables :

```javascript
let a = 3;
let b = 6;

[a,b] = [b,a];

console.log(a);//6
console.log(b);//3

```

Ensuite, passons à la déstructuration d'objets.

## Déstructuration d'objets

Tout d'abord, voyons pourquoi il y a un besoin de déstructuration d'objets. 

Supposons que nous voulons extraire des données d'un objet et les assigner à de nouvelles variables. Avant ES6, comment cela aurait-il été fait ?

```javascript
let person = {name: "Sarah", country: "Nigeria", job: "Developer"};

let name = person.name;
let country = person.country;
let job = person.job;

console.log(name);//"Sarah"
console.log(country);//"Nigeria"
console.log(job);//Developer"

```

Voyez comme c'est fastidieux d'extraire toutes les données. Nous devons répéter la même chose. La déstructuration ES6 sauve vraiment la journée. Plongeons-nous dedans.

### Déstructuration d'objets de base

Répétons l'exemple ci-dessus avec ES6. Au lieu d'assigner des valeurs une par une, nous pouvons utiliser l'objet à gauche pour extraire les données :

```javascript
    
let person = {name: "Sarah", country: "Nigeria", job: "Developer"};

let {name, country, job} = person;

console.log(name);//"Sarah"
console.log(country);//"Nigeria"
console.log(job);//Developer"

```

Vous obtiendrez les mêmes résultats. Il est également valide d'assigner des variables à un objet qui n'ont pas été déclarées :

```javascript
let {name, country, job} = {name: "Sarah", country: "Nigeria", job: "Developer"};

console.log(name);//"Sarah"
console.log(country);//"Nigeria"
console.log(job);//Developer"

```

### Variables déclarées avant d'être assignées

Les variables dans les objets peuvent être déclarées avant d'être assignées avec la déstructuration. Essayons cela :

```javascript
let person = {name: "Sarah", country: "Nigeria", job: "Developer"}; 
let name, country, job;

{name, country, job} = person;

console.log(name);// Erreur : "Unexpected token ="


```

Attendez, que vient-il de se passer ?! Oh, nous avons oublié d'ajouter `()` avant les accolades.

Les `( )` autour de l'instruction d'affectation sont une syntaxe requise lors de l'utilisation de l'affectation par déstructuration de l'objet littéral sans déclaration. Cela est dû au fait que les `{}` du côté gauche sont considérés comme un bloc et non comme un objet littéral. Voici donc comment faire cela de la bonne manière :

```javascript
let person = {name: "Sarah", country: "Nigeria", job: "Developer"};
let name, country, job;

({name, country, job} = person);

console.log(name);//"Sarah"
console.log(job);//"Developer"


```

Il est également important de noter que lors de l'utilisation de cette syntaxe, les `()` doivent être précédés d'un point-virgule. Sinon, ils pourraient être utilisés pour exécuter une fonction de la ligne précédente.

Notez que les variables dans l'objet du côté gauche doivent avoir le même nom qu'une clé de propriété dans l'objet `person`. Si les noms sont différents, nous obtiendrons `undefined` :

```javascript
let person = {name: "Sarah", country: "Nigeria", job: "Developer"};

let {name, friends, job} = person;

console.log(name);//"Sarah"
console.log(friends);//undefined

```

Mais si nous voulons utiliser un nouveau nom de variable, eh bien, nous pouvons.

### Utilisation d'un nouveau nom de variable

Si nous voulons assigner les valeurs d'un objet à une nouvelle variable au lieu d'utiliser le nom de la propriété, nous pouvons faire ceci :

```javascript
let person = {name: "Sarah", country: "Nigeria", job: "Developer"};

let {name: foo, job: bar} = person;

console.log(foo);//"Sarah"
console.log(bar);//"Developer"

```

Ainsi, les valeurs extraites sont passées aux nouvelles variables `foo` et `bar`.

### Utilisation de valeurs par défaut

Les valeurs par défaut peuvent également être utilisées dans la déstructuration d'objets, au cas où une variable serait `undefined` dans un objet dont elle veut extraire des données :

```javascript
let person = {name: "Sarah", country: "Nigeria", job: "Developer"};

let {name = "myName", friend = "Annie"} = person;

console.log(name);//"Sarah"
console.log(friend);//"Annie"

```

Ainsi, si la valeur n'est pas indéfinie, la variable stocke la valeur extraite de l'objet comme dans le cas de `name`. Sinon, elle utilise la valeur par défaut comme elle l'a fait pour `friend`.

Nous pouvons également définir des valeurs par défaut lorsque nous assignons des valeurs à une nouvelle variable :

```javascript
let person = {name: "Sarah", country: "Nigeria", job: "Developer"};

let {name:foo = "myName", friend: bar = "Annie"} = person;

console.log(foo);//"Sarah"
console.log(bar);//"Annie"

```

Ainsi, `name` a été extrait de `person` et assigné à une variable différente. `friend`, en revanche, était `undefined` dans `person`, donc la nouvelle variable `bar` a été assignée à la valeur par défaut.

### Nom de propriété calculé

Le nom de propriété calculé est une autre fonctionnalité de l'objet littéral qui fonctionne également pour la déstructuration. Vous pouvez spécifier le nom d'une propriété via une expression si vous la mettez entre crochets :

```javascript
let prop = "name";

let {[prop] : foo} = {name: "Sarah", country: "Nigeria", job: "Developer"};

console.log(foo);//"Sarah"


```

### Combinaison de tableaux avec des objets

Les tableaux peuvent également être utilisés avec des objets dans la déstructuration d'objets :

```javascript
let person = {name: "Sarah", country: "Nigeria", friends: ["Annie", "Becky"]};

let {name:foo, friends: bar} = person;

console.log(foo);//"Sarah"
console.log(bar);//["Annie", "Becky"]

```

### Imbrication dans la déstructuration d'objets

Les objets peuvent également être imbriqués lors de la déstructuration :

```javascript
let person = {
    name: "Sarah",
    place: {
        country: "Nigeria", 
        city: "Lagos" }, 
    friends : ["Annie", "Becky"]
};

let {name:foo,
     place: {
         country : bar,
         city : x}
    } = person;

console.log(foo);//"Sarah"
console.log(bar);//"Nigeria"

```

### Rest dans la déstructuration d'objets

La syntaxe rest peut également être utilisée pour récupérer les clés de propriétés qui ne sont pas déjà récupérées par le modèle de déstructuration. Ces clés et leurs valeurs sont copiées dans un nouvel objet :

```javascript
let person = {name: "Sarah", country: "Nigeria", job: "Developer" friends: ["Annie", "Becky"]};

let {name, friends, ...others} = person;

console.log(name);//"Sarah"
console.log(friends);//["Annie", "Becky"]
console.log(others);// {country: "Nigeria", job: "Developer"}

```

Ici, les propriétés restantes dont les clés ne faisaient pas partie des noms de variables listés ont été assignées à la variable `others`. La syntaxe rest ici est `...others`. `others` peut être renommé en n'importe quelle variable que vous voulez.

Une dernière chose – voyons comment la déstructuration d'objets peut être utilisée dans les fonctions.

### Déstructuration d'objets et fonctions

La déstructuration d'objets peut être utilisée pour assigner des paramètres à des fonctions :

```javascript
function person({name: x, job: y} = {}) {
    console.log(x);
}

person({name: "Michelle"});//"Michelle"
person();//undefined
person(friend);//Erreur : friend n'est pas défini


```

Remarquez les `{}` du côté droit de l'objet des paramètres. Cela nous permet d'appeler la fonction sans passer d'arguments. C'est pourquoi nous avons obtenu `undefined`. Si nous les supprimons, nous obtiendrons un message d'erreur.

Nous pouvons également assigner des valeurs par défaut aux paramètres :

```javascript
function person({name: x = "Sarah", job: y = "Developer"} = {}) {
    console.log(x);
}

person({name});//"Sarah"

```

Nous pouvons faire beaucoup de choses avec la déstructuration de tableaux et d'objets comme nous l'avons vu dans les exemples ci-dessus.

Merci d'avoir lu. :)