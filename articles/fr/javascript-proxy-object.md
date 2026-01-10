---
title: Comment fonctionne l'objet Proxy de JavaScript – Expliqué avec des cas d'utilisation
subtitle: ''
author: Keyur Paralkar
co_authors: []
series: null
date: '2022-10-31T14:56:30.000Z'
originalURL: https://freecodecamp.org/news/javascript-proxy-object
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/Image-defs.001-1.jpeg
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment fonctionne l'objet Proxy de JavaScript – Expliqué avec des cas
  d'utilisation
seo_desc: "In this tutorial, you are going to learn what a proxy object is, along\
  \ with its limitations. \nWe will also look into some of the use cases that demonstrate\
  \ how you can use proxy objects to solve various problems.\nWithout further ado,\
  \ let’s get starte..."
---

Dans ce tutoriel, vous allez apprendre ce qu'est un objet proxy, ainsi que ses limitations. 

Nous allons également examiner certains cas d'utilisation qui démontrent comment vous pouvez utiliser des objets proxy pour résoudre divers problèmes.

Sans plus attendre, commençons.

## Table des matières

- [Prérequis](#heading-prerequisites)
- [Qu'est-ce qu'un proxy ?](#heading-quest-ce-quun-proxy)
- [Comment restreindre un objet à avoir une propriété spécifique](#heading-comment-restreindre-un-objet-a-avoir-une-propriete-specifique)
- [Une petite parenthèse – qu'est-ce que l'API Reflect ?](#heading-une-petite-parenthese-quest-ce-que-lapi-reflect)
- [Découpage de tableau comme en Python](#heading-decoupage-de-tableau-comme-en-python)
- [Inconvénients de l'utilisation des proxies](#heading-inconvenients-de-lutilisation-des-proxies)
- [Résumé](#heading-resume)


## Prérequis

Je vous recommande vivement de parcourir les sujets suivants pour suivre ce tutoriel :

- [Bases de JavaScript](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics).
- [Méthodes d'instance d'objet.](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object#instance_methods)
- Comment utiliser la [fonction apply en JavaScript.](https://www.freecodecamp.org/news/understand-call-apply-and-bind-in-javascript-with-examples/#how-to-use-the-apply-function-in-javascript)

## Qu'est-ce qu'un proxy ?

D'après [merriam-webster](https://www.merriam-webster.com/dictionary/proxy) :

> *Un proxy peut désigner une personne autorisée à agir pour une autre ou peut désigner la fonction ou l'autorité de servir à la place d'une autre.*
> 

Ainsi, un proxy n'est rien d'autre qu'un médiateur qui parle ou agit au nom de la partie donnée. 

En termes de programmation, le mot proxy signifie également une entité qui agit au nom d'un objet ou d'un système. Maintenant que nous avons clarifié ce terme, comprenons ce qu'il signifie en JavaScript. 

En JavaScript, il existe un objet spécial appelé Proxy. Il vous aide à créer un autre objet au nom de l'objet original. 

Ce nouvel objet proxy agira comme un médiateur entre le monde réel et l'objet original. De cette manière, nous aurons plus de contrôle sur l'interaction avec l'objet original. 

Utiliser un proxy est un moyen puissant d'interagir avec l'objet plutôt que d'interagir directement avec lui. 

Voici la syntaxe pour déclarer un objet proxy :

```jsx
new Proxy(<object>, <handler>)
```

Le `Proxy` prend deux paramètres :

- `<object>` : L'objet qui doit être proxifié.
- `<handler>` : Un objet qui définit la liste des méthodes qui peuvent être interceptées. Ce sont également appelées des pièges.

Examinons un exemple simple :

```jsx
const books = {
	"Deep work": "Cal Newport",
	"Atomic Habits": "James Clear"
}
const proxyBooksObj = new Proxy(books, {
	get: (target, key) => {
		console.log(`Fetching book ${key} by ${target[key]}`);
		return target[key];
	}
})
```

Ici, nous souhaitons intercepter la fonctionnalité `get` de l'objet `books` afin de pouvoir enregistrer le nom du livre et l'auteur du livre dans la console.

Pour y parvenir, nous avons créé un nouvel objet proxy appelé `proxyBooksObj`. Cet objet est construit en utilisant la fonction `Proxy` que nous avons vue précédemment. Il prend `books` comme objet à proxifier, et un objet qui contient des fonctions de gestionnaire qui doivent être piégées. 

Puisque nous devons intercepter la fonctionnalité `get`, nous avons ajouté une propriété `get` qui accepte une fonction. Cette fonction de gestionnaire acceptera une fonction qui prend `target` et `key`. 

C'était un exemple assez simple de proxy en JavaScript. Il existe divers cas d'utilisation d'un proxy – par exemple, il peut aider dans la validation, la mise en forme, la notification et le débogage. 

Pour en savoir plus sur les gestionnaires/pièges disponibles, voici la [liste](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy#a_complete_traps_list_example).

Maintenant, examinons un exemple qui nous fournira plus de clarté sur le fonctionnement des proxies.

## Comment restreindre un objet à avoir une propriété spécifique

Parfois, il peut être utile de restreindre les utilisateurs afin qu'ils n'aient qu'une propriété spécifique, comme le fait `useRef` dans React. Il ne permet de modifier que la propriété `current` de l'objet retourné par `useRef`. 

Créons une fonction proxy qui permettra à l'utilisateur de mettre à jour uniquement la propriété `current` et ne lui permettra pas de créer d'autres propriétés.

```jsx
const data = {};

const newProxy = new Proxy(data, {
  set: function (target, key, value) {
    if (key === "current") {
      Reflect.set(target, key, value);
      return true;
    }
    return false;
  }
});

newProxy.current = 1;
newProxy.point = 1; // Lance une erreur
```

Ici, puisque nous traitons de l'assignation d'une nouvelle valeur à une propriété existante ou de la création d'une nouvelle propriété, nous utilisons la fonction piège `set`. Nous devons exploiter le comportement interne de l'ensemble de l'objet. 

La fonction de gestionnaire `set` prendra `target`, `key` et `value` où la cible sera l'objet cible, et la clé et la valeur sont la propriété et la valeur réelle. 

Nous nous assurons que la clé est `current`. Lorsque c'est le cas, nous définissons la valeur pour cette propriété et retournons true. 

Il est important que nous retournions `true` car cette fonction de gestionnaire s'attend à suivre certains [invariants](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy/set#invariants). Si nous ne voulons pas définir la valeur, nous devons retourner `false`.

Il y a aussi quelque chose à noter sur chaque fonction piège disponible à l'intérieur du proxy qui est invariante. Un invariant n'est rien d'autre qu'une condition qui doit être suivie par chaque fonction piège afin que la fonctionnalité de base ne change pas.

Citant le guide de méta-programmation de MDN :

> [Les sémantiques qui restent inchangées lors de la mise en œuvre d'opérations personnalisées sont appelées *invariants*](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Meta_programming#handlers_and_traps)
> 

### Une petite parenthèse – qu'est-ce que l'API Reflect ?

Nous pouvons également utiliser l'API Reflect ici. JavaScript fournit un objet intégré qui possède un ensemble de fonctions qui peuvent aider à intercepter les opérations JavaScript. Cela peut être des opérations telles que `set`, `get`, `apply`, etc. 

Pour en savoir plus sur les méthodes fournies par l'API Reflect, vous pouvez consulter le [lien](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect#static_methods) suivant. 

Avec cette API, il est vraiment simple de manipuler l'objet cible présent à l'intérieur du proxy. Un fait amusant sur l'API Reflect est qu'elle n'est pas un objet qui peut être instancié. Toutes les méthodes qu'elle fournit sont statiques.

Dans l'exemple précédent, nous avons essayé de retourner la valeur présente à la propriété de l'objet directement en accédant à l'objet original comme ceci : `target[key]`. 

Au lieu de cela, ici nous pouvons utiliser la méthode `get` de Reflect. Ainsi, notre exemple précédent ressemblera à ceci :

```jsx
const books = {
	"Deep work": "Cal Newport",
	"Atomic Habits": "James Clear"
}
const proxyBooksObj = new Proxy(books, {
	get: (target, key) => {
		console.log(`Fetching book ${key} by ${target[key]}`);
		return Reflect.get(target, key);
	}
})
```

Maintenant, nous savons que nous pouvons utiliser Reflect, mais une question se pose - pourquoi utiliser Reflect ?

Nous utilisons Reflect car il nous permet de mettre en œuvre le comportement par défaut des fonctions qui étaient présentes sur l'objet original. Reformulé en termes techniques, cela nous permet de mettre en œuvre le comportement de transfert par défaut à l'intérieur des fonctions pièges. 

De plus, avec Reflect, nous pouvons accéder aux fonctions internes et les appliquer à l'objet enveloppé par le proxy. 

Il est donc bénéfique pour nous d'utiliser les API Reflect à l'intérieur de notre proxy.

## Découpage de tableau comme en Python

Python est un langage vraiment cool. Une fonctionnalité vraiment géniale qu'il fournit est la manière dont vous pouvez découper vos tableaux. Même la bibliothèque [NumPy](https://www.w3schools.com/python/numpy/numpy_array_slicing.asp) de Python fournit cette fonctionnalité de découpage de tableau. 

Vous pouvez simplement fournir un index de début (facultatif) et un index de fin (facultatif) séparés par un deux-points. Voici la syntaxe pour découper un tableau en Python :

```python
arr[<start>:<end>]
```

D'après la syntaxe ci-dessus, il est clair que `start` et `end` signifient les positions d'index de `start` et `end` (exclusif) pour le découpage. 

Voici un exemple de la manière dont vous pouvez découper un tableau en Python :

```python
data = [1,2,3,4]
print(data[1:3]) # Sortie : [2, 3]
```

Voici comment vous pouvez faire la même chose en JavaScript :

```jsx
const data = [1,2,3,4]
console.log(data.slice(1,3)) // Sortie : [2, 3]
```

Vous devez utiliser la fonction `slice` pour découper le tableau `data` de la position d'index `1` à la position d'index `3`. 

Notez que le découpage d'un tableau exclut l'index de fin fourni dans la fonction slice ou dans le mécanisme de découpage de Python.

Ne serait-ce pas génial si nous pouvions réaliser le mécanisme de découpage de Python en JavaScript également ? 

Nous avons à nouveau l'objet Proxy en JavaScript à la rescousse. Comme nous l'avons établi dans une section précédente, les proxies sont un enveloppeur autour de l'objet original. Ils vous aident à gérer l'interaction avec l'objet original. 

Créons à nouveau cet objet proxy – mais cette fois-ci pour qu'il ait le mécanisme de découpage. Voici le code pour implémenter le mécanisme de découpage en JavaScript :

```jsx
const arr = [1,2,3,4];

const arrProxy = new Proxy(arr, {
  get: function (target, key) {
    if (typeof key === "string" && key.includes(":")) {
      let [start, end] = key.split(":");
      if (start === "") {
        start = 0;
      } else if (end === "") {
        end = target.length;
      } else {
        start = parseInt(start, 10);
        end = parseInt(end, 10);
      }

      return Reflect.apply(Array.prototype.slice, target, [start, end]);
    }
    return Reflect.get(target, key);
  }
});

console.log(arrProxy["1:3"]) // [2,3] 
```

Beaucoup de code ici, mais faisons un pas en arrière et comprenons ce qui se passe :

- Nous avons créé un nouvel objet `proxy` par-dessus le tableau `arr`. Puisque nous prévoyons de réaliser le découpage en fournissant les positions de début et de fin séparées par un deux-points, nous devons apporter quelques modifications à la manière de faire la fonctionnalité get d'un tableau.
- Pour ce faire, nous allons utiliser la fonction piège `get` qui modifie le mécanisme get pour un tableau. Nous veillons à ajouter cette fonction piège en tant que propriété `get` à l'intérieur de l'objet `handler` du `Proxy`.
- Une fonction piège [get](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy/get) accepte `target` et `key` comme arguments. Nous utilisons cela pour écrire notre logique.
- Puisque nous faisons quelque chose comme ceci `arrProxy["1:3"]`, dans ce cas, la clé va être de type string et elle va inclure `:` dedans. Notre condition principale sera de distinguer sur cette même condition.
    
```jsx
if (typeof key === "string" && key.includes(":")) 
```
    
Ensuite, nous écrivons quelques conditions qui sont des exigences pour le mécanisme de découpage en Python. Voici les exigences :

- Chaque fois que l'index `start` n'est pas fourni, nous devons définir `start` à 0.
- Chaque fois que l'index `end` n'est pas fourni, nous devons définir `end` à la longueur du tableau original.
- Si les deux sont fournis, alors nous les convertissons en entiers.

Pour ce faire, nous devons utiliser la fonction [slice](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice) en JavaScript.

Nous allons utiliser la méthode [apply](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/apply) de l'[API Reflect](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect), pour exécuter la fonction `slice` avec ce contexte (`target`) étant le tableau original et les arguments de la fonction `slice` étant `[start, end]`.

En fin de compte, si l'argument `key` est d'un autre type de données qu'une chaîne, alors nous retournons directement le tableau avec l'aide de `Reflect.get`.

## Inconvénients de l'utilisation des proxies

Nous savons maintenant comment fonctionne un proxy ainsi que ses cas d'utilisation. Mais il est également important de connaître certains inconvénients de l'utilisation des proxies. 

Tout d'abord, bien qu'il soit cool d'utiliser des proxies, c'est un très mauvais choix dans les scénarios où la performance est un facteur critique.

Deuxièmement, aucun transfert d'opération proxy n'est le mécanisme de transfert de toutes les fonctionnalités de la cible en utilisant un proxy. Voici à quoi ressemble le transfert proxy :
    
```jsx
const data = {};
const newData = new Proxy(data, {}); // Aucune fonction piège.
    
data.point = { x: 1, y: 2};
    
console.log(data);
```
    
Cela fonctionne très bien sur des objets réguliers mais cela ne fonctionnera pas pour des objets tels que les nœuds DOM ou les objets qui ont des slots internes. 

Par exemple, faire quelque chose comme ci-dessous générera une erreur :
        
```jsx
const x = document.createElement("div")
x.className = "hello"
        
const domProxy = new Proxy(x, {});
        
console.log(domProxy.getAttribute("class")); // Lance une erreur de type
```
        
Cela se produit parce que la valeur `this` fait référence à l'objet proxy plutôt qu'à l'objet original. Nous pouvons résoudre cela par une fonction piège get qui aide à faire référence à l'objet original.
        
```jsx
const y = new Proxy(x, {
  get(target, key) {
    const value = Reflect.get(target, key);
    if(typeof value === "function"){
      return value.bind(target)
    }
    return value;
  }
});
        
console.log(y.getAttribute("class")); // Sortie : hello
```

## Résumé

Dans cet article, nous avons appris les proxies en JavaScript ainsi que leurs cas d'utilisation. Nous avons également jeté un coup d'œil à certains inconvénients des proxies.

Si vous aimez l'idée d'utiliser des proxies, alors vous pouvez passer à un niveau supérieur et essayer de les utiliser dans divers scénarios de validation ou de réplication de certaines fonctions de bibliothèque telles que les fonctions [get](https://lodash.com/docs/4.17.15#get) et [set](https://lodash.com/docs/4.17.15#set) de [lodash](https://lodash.com/docs/4.17.15#get).

C'est tout. Merci d'avoir lu.

Suivez-moi sur [Twitter](https://twitter.com/keurplkar), [GitHub](https://github.com/keyurparalkar) et [LinkedIn](https://www.linkedin.com/in/keyur-paralkar-494415107/).