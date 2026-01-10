---
title: Comment utiliser la méthode Map() de JavaScript pour résoudre des problèmes
  de recherche en largeur et en profondeur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-08-30T17:17:31.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-javascript-map-method-to-make-a-breath-first-and-depth-first-search
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/pexels-porapak-apichodilok-346696.jpg
tags:
- name: algorithms
  slug: algorithms
- name: data structures
  slug: data-structures
- name: JavaScript
  slug: javascript
seo_title: Comment utiliser la méthode Map() de JavaScript pour résoudre des problèmes
  de recherche en largeur et en profondeur
seo_desc: 'By Njoku Samson Ebere

  The JavaScript map() method is an object with a key and value pair. An object''s
  key and value are connected using a colon (:) while the key and value of a map are
  connected using an arrow (=>).

  Here''s an example of an object in ...'
---

Par Njoku Samson Ebere

La méthode `map()` de JavaScript est un [objet](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object) avec une paire clé-valeur. La clé et la valeur d'un objet sont connectées à l'aide d'un deux-points (:) tandis que la clé et la valeur d'une map sont connectées à l'aide d'une flèche (=>).

Voici un exemple d'objet en JavaScript :

```javascript
{ a: [ 1, 2, 3 ], b: 2, c: 3 }
```

Et voici un exemple de map en JavaScript :

```javascript
{ 'a' => [ 1, 2, 3 ], 'b' => 2, 'c' => 3 }
```

La méthode `map()` est un bon outil pour résoudre des problèmes d'algorithmes et de structures de données comme les graphes, la distance la plus courte et le meilleur itinéraire. De nombreuses entreprises de transport ont utilisé cette méthode pour construire leur application. Nous allons faire quelque chose de similaire dans ce tutoriel.

J'ai ajouté des vidéos à la fin de diverses sections de ce tutoriel pour ceux qui préfèrent les tutoriels visuels.

## Objectif de cet article

Ce tutoriel vise à vous apprendre comment fonctionne la méthode `map()` et comment vous pouvez l'utiliser pour résoudre des problèmes de recherche en largeur (Breadth-First Search) et de recherche en profondeur (Depth-First Search).

À la fin, vous aurez appris les bases de la méthode `map()`, et vous aurez vu une autre perspective sur la résolution de problèmes d'algorithmes et de structures de données tels que les graphes, la recherche en largeur (BFS) et la recherche en profondeur (DFS).

## Prérequis

Ce tutoriel suppose que vous avez déjà travaillé avec des concepts JavaScript de base tels que les chaînes de caractères, les tableaux, les objets et les ensembles. Il peut également être utile de lire sur les algorithmes et les structures de données.

%[https://www.youtube.com/watch?v=LuVfrai8gpI&list=PLOvIwkWvHysOUVGqOwb_4j5mq8ir0fZ1O]

%[https://www.youtube.com/watch?v=2SKmhCr9Hp4&list=PLOvIwkWvHysOUVGqOwb_4j5mq8ir0fZ1O&index=2]

%[https://www.youtube.com/watch?v=VyUntT1sK20&list=PLOvIwkWvHysOUVGqOwb_4j5mq8ir0fZ1O&index=3]

Commençons !

## Le problème

Le Nigeria compte 36 États. Un touriste peut se déplacer d'un État à un autre par la route, l'air et les voies navigables connues sous le nom d'itinéraires. Ce que nous voulons faire, c'est de manière programmatique :

1. Montrer chaque État et les autres États qui y sont connectés dans un graphe.
2. Vérifier si vous pouvez connecter deux (2) États.

Nous avons donc onze (11) des trente-six (36) États du Nigeria avec lesquels travailler :

```js
ENUGU, ABIA, SOKOTO, NIGER, LAGOS, OGUN, BAYELSA, AKWAIBOM, ANAMBRA, IMO, EBONYI
```

Voici les itinéraires :

* ENUGU vers LAGOS
* ENUGU vers NIGER
* NIGER vers SOKOTO
* NIGER vers ANAMBRA
* SOKOTO vers ANAMBRA
* OGUN vers LAGOS
* OGUN vers ABIA
* OGUN vers EBONYI
* OGUN vers BAYELSA
* EBONYI vers ABIA

Utilisons ces données pour résoudre le problème !

## Comment résoudre le problème

Dans la section précédente, nous avons vu le problème. Maintenant, nous allons le résoudre ici. J'utiliserai [Replit](https://replit.com/) pour ce tutoriel.

Replit vous offre un IDE bien équipé pour écrire et tester rapidement des programmes comme celui que nous allons écrire.

### Comment configurer la Map

Le premier problème que nous voulons résoudre est de montrer de manière programmatique chaque État et les autres États qui y sont connectés.

Commencez par définir les onze (11) États et leurs itinéraires. Entrez le code suivant :

```javascript

const states = 'ENUGU ABIA SOKOTO NIGER LAGOS OGUN BAYELSA AKWAIBOM ANAMBRA IMO EBONYI'.split(' ');

const routes = [
  ['ENUGU', 'LAGOS'],
  ['ENUGU', 'NIGER'],
  ['NIGER', 'SOKOTO'],
  ['NIGER', 'ANAMBRA'],
  ['SOKOTO', 'ANAMBRA'],
  ['OGUN', 'LAGOS'],
  ['OGUN', 'ABIA'],
  ['OGUN', 'EBONYI'],
  ['OGUN', 'BAYELSA'],
  ['EBONYI', 'ABIA'],
];

```

Créez une nouvelle `map()` ou un graphe nommé `connections` :

```javascript
const connections = new map();
```

Ensuite, tapez le code suivant :

```javascript
states.forEach((state) => {
  connections.set(state, []);
});
```

Ce code parcourt tous les **states**. Il prend chaque état et le définit comme une clé dans le graphe `connections` avec une valeur par défaut d'un tableau vide (`[]`).

Si vous loggez `connections` dans la console, vous obtiendrez le résultat suivant :

```javascript
Map(11) {
  'ENUGU' => [],
  'ABIA' => [],
  'SOKOTO' => [],
  'NIGER' => [],
  'LAGOS' => [],
  'OGUN' => [],
  'BAYELSA' => [],
  'AKWAIBOM' => [],
  'ANAMBRA' => [],
  'IMO' => [],
  'EBONYI' => []
}
```

Pour l'instant, imaginez le graphe dans la sortie ci-dessus comme dans l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Screenshot-2022-08-10-at-16.44.32.png)
_Représentation graphique des États donnés_

Entrez le code ci-dessous :

```javascript
routes.forEach(route => {
  const departure = [...route][0];
  const destination = [...route][1];
  
  connections.get(departure).push(destination);
  connections.get(destination).push(departure);
});
```

Ce code ajoute des États aux valeurs de tableau vides des clés de l'étape précédente. Il parcourt le tableau des itinéraires et extrait chaque itinéraire.

L'État de départ est défini comme le premier élément du tableau d'itinéraire, tandis que l'État de destination est le second.

Il ajoute ensuite l'État de destination au tableau de valeurs de l'État de départ. Enfin, l'État de départ est inclus dans le tableau de valeurs de l'État de destination.

À ce stade, si vous loggez `connections` dans la console, vous obtiendrez le résultat suivant :

```javascript
Map(11) {
  'ENUGU' => [ 'LAGOS', 'NIGER' ],
  'ABIA' => [ 'OGUN', 'EBONYI' ],
  'SOKOTO' => [ 'NIGER', 'ANAMBRA' ],
  'NIGER' => [ 'ENUGU', 'SOKOTO', 'ANAMBRA' ],
  'LAGOS' => [ 'ENUGU', 'OGUN' ],
  'OGUN' => [ 'LAGOS', 'ABIA', 'EBONYI', 'BAYELSA' ],
  'BAYELSA' => [ 'OGUN' ],
  'AKWAIBOM' => [],
  'ANAMBRA' => [ 'NIGER', 'SOKOTO' ],
  'IMO' => [],
  'EBONYI' => [ 'OGUN', 'ABIA' ]
}
```

Ce type de graphe est non orienté. Un graphe non orienté est un type de graphe où vous pouvez vous déplacer du nœud vers les arêtes et des arêtes vers le nœud. Dans notre cas, le nœud est l'État de départ, tandis que les arêtes sont l'État de destination.

Voici une représentation picturale de la sortie ci-dessus :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Screenshot-2022-08-10-at-16.29.30.png)
_Un graphe non orienté représentant les itinéraires_

La flèche avec un remplissage de couleur noire pointe vers l'État de destination, tandis que la flèche avec un remplissage de couleur blanche pointe vers l'État de départ.

Pour rendre ce graphe orienté, vous pouvez utiliser ce code à la place :

```javascript
routes.forEach(route => {
  connections.get([...route][0]).push([...route][1]);
});
```

Voici la sortie ci-dessous :

```javascript
Map(11) {
  'ENUGU' => [ 'LAGOS', 'NIGER' ],
  'ABIA' => [],
  'SOKOTO' => [ 'ANAMBRA' ],
  'NIGER' => [ 'SOKOTO', 'ANAMBRA' ],
  'LAGOS' => [],
  'OGUN' => [ 'LAGOS', 'ABIA', 'EBONYI', 'BAYELSA' ],
  'BAYELSA' => [],
  'AKWAIBOM' => [],
  'ANAMBRA' => [],
  'IMO' => [],
  'EBONYI' => [ 'ABIA' ]
}
```

Voici une représentation picturale de la sortie ci-dessus :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Screenshot-2022-08-10-at-16.06.57.png)
_Un graphe orienté représentant les itinéraires_

Si vous avez du mal à comprendre, étudiez les sorties et comparez-les avec les itinéraires donnés. Le code deviendra plus facile à mesure que vous pratiquerez.

Nous avons pu montrer comment ces États sont connectés de manière programmatique. Voici à quoi ressemble le code jusqu'à présent :

```javascript

const states = 'ENUGU ABIA SOKOTO NIGER LAGOS OGUN BAYELSA AKWAIBOM ANAMBRA IMO EBONYI'.split(' ');

const routes = [
  ['ENUGU', 'LAGOS'],
  ['ENUGU', 'NIGER'],
  ['NIGER', 'SOKOTO'],
  ['NIGER', 'ANAMBRA'],
  ['SOKOTO', 'ANAMBRA'],
  ['OGUN', 'LAGOS'],
  ['OGUN', 'ABIA'],
  ['OGUN', 'EBONYI'],
  ['OGUN', 'BAYELSA'],
  ['EBONYI', 'ABIA'],
];

const connections = new map();

states.forEach((state) => {
  connections.set(state, []);
});

console.log(connections)

routes.forEach(route => {
  const departure = [...route][0];
  const destination = [...route][1];
  
  connections.get(departure).push(destination);
  connections.get(destination).push(departure);
});

console.log(connections)

```

Nous passons à la partie suivante du problème (vérifier si vous pouvez connecter deux (2) États). Nous allons le faire de deux (2) manières. D'abord, nous allons explorer l'algorithme de recherche en largeur, puis nous allons le faire en utilisant la méthode de recherche en profondeur.

%[https://www.youtube.com/watch?v=OV-FDBlhdBE&list=PLOvIwkWvHysOUVGqOwb_4j5mq8ir0fZ1O&index=4]

### Comment utiliser la recherche en largeur

Le [BFS](https://www.freecodecamp.org/news/breadth-first-search-in-javascript-e655cd824fa4/) est un algorithme utilisé pour inspecter un arbre ou un graphe en explorant les enfants directs (arêtes) d'un parent (nœud) avant de passer aux petits-enfants. Il continue de cette manière jusqu'à la fin de l'arbre ou du graphe.

Par exemple, dans notre cas, disons que nous voulons vérifier s'il existe une connexion possible entre ENUGU et ABIA.

Le BFS commencera par Enugu et vérifiera toutes les routes directes d'Enugu (LAGOS et NIGER). Comme ABIA n'est pas directement connecté à ENUGU, l'algorithme passera à vérifier l'État (les États) attaché(s) à LAGOS.

Ensuite, l'algorithme inspectera l'État (les États) lié(s) à NIGER. Le processus se poursuivra jusqu'à ce qu'il trouve ABIA ou rencontre une impasse. Cela termine le programme.

Le BFS utilise une [file d'attente](https://www.freecodecamp.org/news/queue-data-structure-definition-and-java-example-code/) comme structure de données. Cela signifie que les éléments seront entrés d'un côté et retirés de l'autre côté d'un tableau. Dans notre cas, la file d'attente contiendra tous les États qui n'ont pas encore été visités. À mesure que nous continuons à construire le programme, vous le verrez en action.

Commençons à construire le BFS en créant une fonction nommée `bfs` :

```javascript
function bfs(departureState, destinationState) {

}
```

Cette fonction prend deux (2) arguments, `departureState` et `destinationState`.

À l'intérieur de la fonction, définissez une `queue` et ajoutez-y le `departureState` :

```javascript
  const queue = [departureState];
```

Nous ajoutons le `departureState` au tableau `queue` puisqu'il contient tous les nœuds qui n'ont pas encore été visités.

Ensuite, définissez un nouvel ensemble vide `[Set()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/Set)` nommé `visited` :

```javascript
  const visited = new Set();
```

La variable `visited` gardera une trace de tous les États visités, comme son nom l'indique.

Maintenant, nous commençons la recherche proprement dite en naviguant à travers le graphe en commençant par le `departureState`. Entrez le code ci-dessous :

```javascript
while (queue.length > 0) {
    
}
```

Cette boucle s'exécutera tant que la `queue` n'est pas vide. Cela signifie tant qu'il y a encore des États non visités.

Retirez le `departureState` de la `queue` avant de le visiter pour empêcher le code de tomber dans une boucle infinie. Utilisez le code ci-dessous :

```javascript
    const state = queue.shift();
```

Le code ci-dessus retire chaque `state` du début ou du haut du tableau `queue` puisque une file d'attente utilise le principe Premier Entré, Premier Sorti. Un tableau insère des éléments par l'arrière ou le bas par défaut.

Récupérez les arêtes (`destinations`) connectées à ce nœud (`state`) :

```javascript
    const destinations = connections.get(state);
```

Maintenant que nous avons accès aux enfants (`destinations`) du nœud actuel (`state`), vérifions si l'un d'eux est le `destinationState`.

Parcourez les `destinations` en utilisant ce code :

```javascript
for (const destination of destinations) {
    
}
```

À chaque point de cette boucle, vérifiez si la `destination` est le `destinationState`. Si c'est `true`, loggez un message dans la console :

```javascript
      if (destination === destinationState) {
          console.log("Found => " + destination);
      }
```

Après cela, ajoutez la `destination` aux tableaux `visited` et `queue` si elle n'est pas déjà dans `visited` :

```javascript
      if (!visited.has(destination)) {
        visited.add(destination);
        queue.push(destination);
      }
```

Le programme se termine lorsque tous les États sont dans le tableau `visited` car il n'y aura plus d'État à ajouter à la `queue`.

La fonction `bfs` ressemble maintenant à ceci :

```javascript
function bfs(departureState, destinationState) {
  const queue = [departureState];
  const visited = new Set();

  while (queue.length > 0) {
    const state = queue.shift();
    const destinations = connections.get(state);

    for (const destination of destinations) {
      if (destination === destinationState) {
          console.log("Found => " + destination);
      }

      if (!visited.has(destination)) {
        visited.add(destination);
        queue.push(destination);
      }
    }
  }
}

```

Pour vérifier s'il existe une connexion entre deux (2) États, disons ENUGU et SOKOTO, appelez la fonction `bfs` comme ceci :

```javascript
bfs("ENUGU", "SOKOTO")
```

Voici la sortie :

```javascript
Map(11) {
  'ENUGU' => [],
  'ABIA' => [],
  'SOKOTO' => [],
  'NIGER' => [],
  'LAGOS' => [],
  'OGUN' => [],
  'BAYELSA' => [],
  'AKWAIBOM' => [],
  'ANAMBRA' => [],
  'IMO' => [],
  'EBONYI' => []
}
Map(11) {
  'ENUGU' => [ 'LAGOS', 'NIGER' ],
  'ABIA' => [ 'OGUN', 'EBONYI' ],
  'SOKOTO' => [ 'NIGER', 'ANAMBRA' ],
  'NIGER' => [ 'ENUGU', 'SOKOTO', 'ANAMBRA' ],
  'LAGOS' => [ 'ENUGU', 'OGUN' ],
  'OGUN' => [ 'LAGOS', 'ABIA', 'EBONYI', 'BAYELSA' ],
  'BAYELSA' => [ 'OGUN' ],
  'AKWAIBOM' => [],
  'ANAMBRA' => [ 'NIGER', 'SOKOTO' ],
  'IMO' => [],
  'EBONYI' => [ 'OGUN', 'ABIA' ]
}
Found => SOKOTO
Found => SOKOTO
```

Si ce que nous avons fait jusqu'à présent n'est pas clair, je vous suggère de décomposer le code à différents points pour voir comment le programme fonctionne.

%[https://www.youtube.com/watch?v=N8a8XXIihTQ&list=PLOvIwkWvHysOUVGqOwb_4j5mq8ir0fZ1O&index=5]

%[https://www.youtube.com/watch?v=MCfnFLMpq9E&list=PLOvIwkWvHysOUVGqOwb_4j5mq8ir0fZ1O&index=6]

### Comment utiliser la recherche en profondeur

L'algorithme [DFS](https://www.freecodecamp.org/news/dfs-for-your-next-tech-giant-interview/) prend un enfant d'un nœud à la fois. Il continue à rechercher un enfant à la fois de ce nœud jusqu'à ce qu'il arrive à une impasse avant de revenir en arrière et d'essayer un autre enfant.

Dans notre cas, disons que nous voulons vérifier s'il existe une connexion possible entre ENUGU et ABIA.

Le DFS commencera par Enugu et vérifiera le premier état qui y est connecté (LAGOS). Comme LAGOS n'est pas ABIA, la recherche examinera le premier état lié à LAGOS ensuite. Il continuera jusqu'à ce qu'il localise ABIA ou rencontre une impasse. Ensuite, il reviendra en arrière pour vérifier un autre nœud.

Le DFS utilise une pile pour garder une trace des éléments (état(s) dans notre cas) à visiter. Lorsque la pile devient vide, le processus se termine. Nous utiliserons la récursivité pour écrire le code de l'algorithme DFS. Commençons !

Commencez par créer une fonction nommée `dfs`. Elle prendra trois (3) arguments (`departureState`, `destinationState`, et `visited`) :

```js

function dfs(departureState, destinationState, visited = new Set()) {
    
}
```

Le tableau `visited` contiendra les états visités pour éviter une boucle infinie. La première chose à faire dans la fonction `dfs` est donc d'ajouter le `departureState` dans le tableau `visited`. Entrez ce code :

```js
  visited.add(departureState);
```

Ensuite, obtenez les `destinations` du `departureState` :

```js
  const destinations = connections.get(departureState);
```

Maintenant que nous avons les `destinations` du `departureState`, nous voulons les parcourir. Tapez le code ci-dessous :

```js
  for (let destination of destinations) {
      
  }
```

À l'intérieur de la boucle, vérifiez si la `destination` actuelle est le `destinationState`. Si c'est `true`, affichez un message dans la console. Utilisez le code ci-dessous :

```js
    if (destination === destinationState) {
      console.log("Found => " + destination);
    }
```

Ensuite, si la `destination` actuelle n'a pas encore été visitée, appelez à nouveau la fonction `dfs` (de manière récursive) — mais cette fois, utilisez la `destination` comme `departureState` :

```js
    if (!visited.has(destination)) {
      dfs(destination, destinationState, visited)
    }
```

Le `destinationState` reste constant tandis que le `visited` `Set()` n'est plus vide. À ce stade, ces destinations dans la boucle qui ne sont pas encore dans le tableau visited entrent dans la pile.

Voici à quoi ressemble la fonction `dfs` :

```js

function dfs(departureState, destinationState, visited = new Set()) {
  
  visited.add(departureState);
  
  const destinations = connections.get(departureState);

  for (let destination of destinations) {
    if (destination === destinationState) {
      console.log("Found => " + destination);
    }

    if (!visited.has(destination)) {
      dfs(destination, destinationState, visited)
    }
  }
}
```

Pour vérifier s'il existe une connexion entre deux (2) États, disons ENUGU et SOKOTO, appelez la fonction `dfs` comme ceci :

```javascript
dfs("ENUGU", "SOKOTO")
```

Voir la sortie ci-dessous :

```js
Map(11) {
  'ENUGU' => [],
  'ABIA' => [],
  'SOKOTO' => [],
  'NIGER' => [],
  'LAGOS' => [],
  'OGUN' => [],
  'BAYELSA' => [],
  'AKWAIBOM' => [],
  'ANAMBRA' => [],
  'IMO' => [],
  'EBONYI' => []
}
Map(11) {
  'ENUGU' => [ 'LAGOS', 'NIGER' ],
  'ABIA' => [ 'OGUN', 'EBONYI' ],
  'SOKOTO' => [ 'NIGER', 'ANAMBRA' ],
  'NIGER' => [ 'ENUGU', 'SOKOTO', 'ANAMBRA' ],
  'LAGOS' => [ 'ENUGU', 'OGUN' ],
  'OGUN' => [ 'LAGOS', 'ABIA', 'EBONYI', 'BAYELSA' ],
  'BAYELSA' => [ 'OGUN' ],
  'AKWAIBOM' => [],
  'ANAMBRA' => [ 'NIGER', 'SOKOTO' ],
  'IMO' => [],
  'EBONYI' => [ 'OGUN', 'ABIA' ]
}
Found => SOKOTO
Found => SOKOTO
```

Bien que la sortie ci-dessus soit la même que celle que nous avons obtenue lorsque nous avons exécuté la fonction bfs, le processus pour arriver à ce résultat diffère. Essayez de décomposer le code à différents points pour voir le flux du programme.

%[https://www.youtube.com/watch?v=yl8GjfOSNq0&list=PLOvIwkWvHysOUVGqOwb_4j5mq8ir0fZ1O&index=7]

## Conclusion

Les structures de données et les algorithmes sont devenus une partie importante des entretiens en ingénierie logicielle. La méthode `map()` est un outil puissant en JavaScript qui facilite la résolution de telles tâches complexes comme nous l'avons vu dans ce tutoriel.

Nous avons commencé par créer un graphe en utilisant la méthode `map()`. Ensuite, nous avons recherché des connexions entre les États en utilisant les algorithmes BFS et DFS.

Vous pouvez trouver mon code [ici](https://replit.com/@EBEREGIT/MappingWithStates#index.js)

Cela peut sembler un peu écrasant si vous êtes nouveau dans les algorithmes et les structures de données. Mais avec une pratique répétée, vous vous y habituerez. Donc, si vous avez trouvé cela difficile à comprendre au début, prenez une pause et revenez-y avec un esprit plus clair.