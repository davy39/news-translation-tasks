---
title: Comment écrire une Promesse JavaScript
subtitle: ''
author: Brandon Wozniewicz
co_authors: []
series: null
date: '2019-02-05T16:30:16.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-a-javascript-promise-4ed8d44292b8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*RR8oubeQOm63YN90Uth0CA.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: promises
  slug: promises
- name: 'tech '
  slug: tech
seo_title: Comment écrire une Promesse JavaScript
seo_desc: 'What is a promise?

  A JavaScript promise is an object that represents the completion or failure of an
  asynchronous task and its resulting value.¹

  The end.

  I’m kidding of course. So, what does that definition even mean?

  First of all, many things in Jav...'
---

### Qu'est-ce qu'une promesse ?

Une promesse JavaScript est un objet qui représente l'achèvement ou l'échec d'une tâche asynchrone et sa valeur résultante.¹

C'est tout.

Je plaisante bien sûr. Alors, que signifie vraiment cette définition ?

Tout d'abord, beaucoup de choses en JavaScript sont des objets. Vous pouvez créer un objet de plusieurs manières différentes. La manière la plus courante est avec la syntaxe littérale d'objet :

```js
const myCar = {
   color: 'blue',
   type: 'sedan',
   doors: '4',
};
```

Vous pourriez également créer une `class` et l'instancier avec le mot-clé `new`.

```js
class Car {
   constructor(color, type, doors) {
      this.color = color;
      this.type = type;
      this.doors = doors
   }
}

const myCar = new Car('blue', 'sedan', '4');
```

`console.log(myCar);`

![Image](https://cdn-media-1.freecodecamp.org/images/1*QUB10cb7QMBVBEGM2JRo1g.png align="left")

Une promesse est simplement un objet que nous créons comme dans l'exemple précédent. Nous l'instancions avec le mot-clé `new`. Au lieu des trois paramètres que nous avons passés pour créer notre voiture (couleur, type et portes), nous passons une fonction qui prend deux arguments : `resolve` et `reject`.

En fin de compte, les promesses nous informent sur l'achèvement de la fonction asynchrone à partir de laquelle nous les avons retournées — si elle a fonctionné ou non. Nous disons que la fonction a réussi en disant que la promesse est *résolue*, et qu'elle a échoué en disant que la promesse est *rejetée*.

```js
const myPromise = new Promise(function(resolve, reject) {});
```

`console.log(myPromise);`

![Image](https://cdn-media-1.freecodecamp.org/images/1*z8UFY0q1iVmr4xzOqOvFlA.png align="left")

*Remarquez que la promesse est « en attente ».*

```js
const myPromise = new Promise(function(resolve, reject) {
   resolve(10);
});
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*voamRd9sJg_NZ0vOdbYJgg.png align="left")

*Remarquez que nous avons résolu la promesse avec la valeur 10.*

Vous voyez, ce n'est pas trop effrayant — juste un objet que nous avons créé. Et, si nous l'étendons un peu :

![Image](https://cdn-media-1.freecodecamp.org/images/1*szpVAwKfKzMasjP9Wlpigg.png align="left")

*Remarquez que nous avons accès à certaines méthodes, notamment « then » et « catch ».*

De plus, nous pouvons passer tout ce que nous voulons à resolve et reject. Par exemple, nous pourrions passer un objet au lieu d'une chaîne :

```js
return new Promise((resolve, reject) => {
   if(somethingSuccesfulHappened) {
      const successObject = {
         msg: 'Success',
         data,//...some data we got back
      }
      resolve(successObject); 
   } else {
      const errorObject = {
         msg: 'An error occured',
         error, //...some error we got back
      }
      reject(errorObject);
   }
});
```

Ou, comme nous l'avons vu précédemment, nous n'avons pas à passer quoi que ce soit :

```js
return new Promise((resolve, reject) => {
   if(somethingSuccesfulHappend) {
      resolve()
   } else {
      reject();
   }
});
```

#### Qu'en est-il de la partie « asynchrone » de la définition ?

JavaScript est mono-thread. Cela signifie qu'il ne peut exécuter qu'une seule chose à la fois. Si vous pouvez imaginer une route, vous pouvez penser à JavaScript comme une autoroute à une seule voie. Certains codes (codes asynchrones) peuvent glisser sur l'accotement pour permettre à d'autres codes de les dépasser. Lorsque ce code asynchrone est terminé, il revient sur la chaussée.

> En aparté, nous pouvons retourner une promesse depuis *n'importe quelle* fonction. Elle n'a pas besoin d'être asynchrone. Cela dit, les promesses sont normalement retournées dans les cas où la fonction qui les retourne est asynchrone. Par exemple, une API qui a des méthodes pour sauvegarder des données sur un serveur serait un excellent candidat pour retourner une promesse !

**À retenir :**

Les promesses nous donnent un moyen d'attendre que notre code asynchrone se termine, de capturer certaines valeurs de celui-ci et de transmettre ces valeurs à d'autres parties de notre programme.

*J'ai un article ici qui approfondit ces concepts : [Thrown For a Loop: Understanding Loops and Timeouts in JavaScript.](https://www.freecodecamp.org/news/thrown-for-a-loop-understanding-for-loops-and-timeouts-in-javascript-558d8255d8a4/)*

### Comment utiliser une promesse ?

Utiliser une promesse s'appelle également *consommer* une promesse. Dans notre exemple ci-dessus, notre fonction retourne un objet promesse. Cela nous permet d'utiliser l'enchaînement de méthodes avec notre fonction.

Voici un exemple d'enchaînement de méthodes que vous avez probablement vu :

```js
const a = 'Some awesome string';
const b = a.toUpperCase().replace('ST', '').toLowerCase();

console.log(b); // some awesome ring
```

Maintenant, rappelons notre promesse (fictive) :

```js
const somethingWasSuccesful = true;

function someAsynFunction() {
   return new Promise((resolve, reject){
      if (somethingWasSuccesful) {
         resolve();     
      } else {
         reject()
      }
   });
}
```

Et, consommer notre promesse en utilisant l'enchaînement de méthodes :

```js
someAsyncFunction
   .then(runAFunctionIfItResolved(withTheResolvedValue))
   .catch(orARunAfunctionIfItRejected(withTheRejectedValue));
```

### Un exemple (plus) réel.

Imaginez que vous avez une fonction qui récupère des utilisateurs depuis une base de données. J'ai écrit une fonction d'exemple sur Codepen qui simule une API que vous pourriez utiliser. Elle propose deux options pour accéder aux résultats. Une, vous pouvez fournir une fonction de rappel où vous pouvez accéder à l'utilisateur ou à toute erreur. Ou deux, la fonction retourne une promesse comme moyen d'accéder à l'utilisateur ou à l'erreur.

%[https://codepen.io/brandonwoz/pen/NoNMgJ]

Traditionnellement, nous accédions aux résultats du code asynchrone par l'utilisation de rappels.

```js
rr someDatabaseThing(maybeAnID, function(err, result)) {
   //...Une fois que nous avons récupéré la chose de la base de données...
   if(err) {
      doSomethingWithTheError(error)
   }   else {
      doSomethingWithResults(results);
   }
}
```

L'utilisation de rappels est *acceptable* jusqu'à ce qu'ils deviennent trop imbriqués. En d'autres termes, vous devez exécuter plus de code asynchrone avec chaque nouveau résultat. Ce modèle de rappels dans des rappels peut conduire à ce que l'on appelle « l'enfer des rappels ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*DxEgvtymVuqpLOSx8NJ57A.png align="left")

*Les débuts de l'enfer des rappels*

Les promesses nous offrent une manière plus élégante et lisible de voir le flux de notre programme.

```js
doSomething()
   .then(doSomethingElse) // et si vous voulez bien
   .catch(anyErrorsPlease);
```

### Écrire notre propre promesse : Boucle d'Or, les Trois Ours et un Superordinateur

Imaginez que vous avez trouvé un bol de soupe. Vous aimeriez connaître la température de cette soupe avant de la manger. Vous êtes à court de thermomètres, mais heureusement, vous avez accès à un superordinateur qui vous indique la température du bol de soupe. Malheureusement, ce superordinateur peut prendre jusqu'à 10 secondes pour obtenir les résultats.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XtBW084Eg2feXeR97W2yvw.png align="left")

Voici quelques points à noter.

1. Nous initialisons une variable globale appelée `result`.
   
2. Nous simulons la durée du délai du réseau avec `Math.random()` et `setTimeout()`.
   
3. Nous simulons une température avec `Math.random()`.
   
4. Nous maintenons les valeurs de délai et de température dans une plage en ajoutant un peu de « math » supplémentaire. La plage pour `temp` est de 1 à 300 ; la plage pour `delay` est de 1000ms à 10000ms (1s à 10 secondes).
   
5. Nous enregistrons le délai et la température afin d'avoir une idée de la durée de cette fonction et des résultats que nous nous attendons à voir lorsqu'elle est terminée.
   

Exécutez la fonction et enregistrez les résultats.

```js
getTemperature(); 
console.log(results); // undefined
```

#### La température est indéfinie. Que s'est-il passé ?

La fonction prendra un certain temps à s'exécuter. La variable n'est pas définie avant que le délai ne soit terminé. Ainsi, pendant que nous exécutons la fonction, `setTimeout` est asynchrone. La partie du code dans `setTimeout` se déplace hors du thread principal vers une zone d'attente.

*J'ai un article ici qui approfondit ce processus : [Thrown For a Loop: Understanding Loops and Timeouts in JavaScript.](https://www.freecodecamp.org/news/thrown-for-a-loop-understanding-for-loops-and-timeouts-in-javascript-558d8255d8a4/)*

Puisque la partie de notre fonction qui définit la variable `result` se déplace dans une zone d'attente jusqu'à ce qu'elle soit terminée, notre parseur est libre de passer à la ligne suivante. Dans notre cas, c'est notre `console.log()`. À ce stade, `result` est toujours indéfini puisque notre `setTimeout` n'est pas terminé.

Alors, que pourrions-nous essayer d'autre ? Nous pourrions exécuter `getTemperature()` puis attendre 11 secondes (puisque notre délai maximum est de dix secondes) et *ensuite* afficher les résultats dans la console.

```js
getTemperature();
   setTimeout(() => {
      console.log(result); 
   }, 11000);
   
// Too Hot | Delay: 3323 | Temperature: 209 deg
```

Cela fonctionne, mais le problème avec cette technique est que, bien que dans notre exemple nous connaissions le délai réseau maximum, dans un exemple réel, cela pourrait occasionnellement prendre plus de dix secondes. Et, même si nous pouvions garantir un délai maximum de dix secondes, si le résultat est prêt plus tôt, nous perdons du temps.

### Les promesses à la rescousse

Nous allons refactoriser notre fonction `getTemperature()` pour qu'elle retourne une promesse. Et au lieu de définir le résultat, nous allons rejeter la promesse sauf si le résultat est « Juste Bien », auquel cas nous allons résoudre la promesse. Dans les deux cas, nous allons passer certaines valeurs à la fois à resolve et reject.

![Image](https://cdn-media-1.freecodecamp.org/images/1*4RJERRgVUtHlIYRFm2piVQ.png align="left")

Nous pouvons maintenant utiliser les résultats de notre promesse que nous retournons (également connu sous le nom de *consommation* de la promesse).

```js
getTemperature()
   .then(result => console.log(result))
   .catch(error => console.log(error));
   
// Reject: Too Cold | Delay: 7880 | Temperature: 43 deg
```

`.then` sera appelé lorsque notre promesse sera résolue et retournera les informations que nous passons dans `resolve`.

`.catch` sera appelé lorsque notre promesse sera rejetée et retournera les informations que nous passons dans `reject`.

Très probablement, vous consommerez plus de promesses que vous n'en créerez. Dans les deux cas, elles aident à rendre notre code plus élégant, lisible et efficace.

### Résumé

1. Les promesses sont des objets qui contiennent des informations sur l'achèvement d'un certain code asynchrone et toute valeur résultante que nous voulons passer.
   
2. Pour retourner une promesse, nous utilisons `return new Promise((resolve, reject)=> {})`
   
3. Pour consommer une promesse, nous utilisons `.then` pour obtenir les informations d'une promesse qui a été résolue, et `.catch` pour obtenir les informations d'une promesse qui a été rejetée.
   
4. Vous utiliserez (consommerez) probablement plus de promesses que vous n'en écrirez.
   

#### Références

1.) [*https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global\_Objects/Promise*](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)