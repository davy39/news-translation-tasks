---
title: Comment gérer les rappels asynchrones en JavaScript...Sans rappels ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-04T23:38:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-handle-async-callbacks-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/museums-victoria-TVe0IEdsVc8-unsplash.jpg
tags:
- name: asynchronous
  slug: asynchronous
- name: callbacks
  slug: callbacks
- name: JavaScript
  slug: javascript
seo_title: Comment gérer les rappels asynchrones en JavaScript...Sans rappels ?
seo_desc: "By Tobias Parent\nNoodling about on Discord today, the same question came\
  \ up a few times on a few different servers. I thought it was a great question,\
  \ and it seems my brain doesn't work quite the way others might expect. \nHere's\
  \ the question:\n\n\"So I ..."
---

Par Tobias Parent

En réfléchissant sur Discord aujourd'hui, la même question est revenue plusieurs fois sur différents serveurs. J'ai pensé que c'était une excellente question, et il semble que mon cerveau ne fonctionne pas tout à fait comme les autres pourraient s'y attendre. 

Voici la question :

> "Donc, j'ai une fonction `fetch`, et je fais quelques `then` avec elle pour analyser les données JSON. Je veux retourner cela, mais comment puis-je faire ? Nous ne pouvons pas `return` quelque chose à partir d'un appel de fonction asynchrone !"

C'est une excellente question. Il y a beaucoup de choses en jeu ici. Nous avons des moyens de gérer cela dans React, assez facilement : nous pouvons utiliser `useState` pour créer une variable d'état, nous pouvons exécuter notre `fetch` dans un `useEffect` et charger cette variable d'état, et nous pouvons utiliser _un autre_ `useEffect` pour écouter cette variable d'état changer. Lorsque le changement se produit, nous pouvons déclencher notre fonction personnalisée et faire un effet de bord avec elle.

Avec du JavaScript, HTML et CSS purs, cela devient un peu plus compliqué. Pour ceux qui aiment lire la dernière page du roman policier avant le reste, [ce replit](https://replit.com/@TobiasParent/HandlingLateLoadEvents#script.js) est là où nous allons finir.

## Un début peu élégant

Supposons que nous voulons récupérer des todos depuis un serveur, et lorsque nous les avons chargés, nous voulons mettre à jour le DOM. Nous pourrions avoir besoin de les recharger, ou de les ajouter plus tard – nous voulons que des choses se produisent si nos fonctions asynchrones font une sorte de mise à jour de notre _état_.

Et pourtant, je ne sais pas vraiment comment je me sens à ce sujet. Lorsque nous avons un bloc de code comme ceci :

```js
const load = () => {
  fetch("https://jsonplaceholder.typicode.com/todos")
    .then(res => res.json())
    .then(jsonObj => {
      const todoContainer = document.querySelector(".todos-container");
      // maintenant, prenons chaque todo, créons son DOM, et insérons-le.
      jsonObj.forEach( (todo)=>{
        const todoEl = document.createElement("div");
        todoEl.classList.add("todo");
        const todoTitle = document.createElement("h3");
        todoTitle.classList.add("todo-title");
        todoTitle.textContent=todo.title;

        const todoStatus = document.createElement("div");
        todoStatus.classList.add("todo-status");
        todoStatus.textContent = todo.done ? "Complete" : "Incomplete";

        todoEl.append(todoTitle, todoStatus);
        todoContainer.append(todoEl)
    })
}
```

Nous devons _remplir_ le DOM directement dans le bloc `.then()`, car nous ne pouvons pas vraiment dire "hey, quand c'est fait, déclenche cette fonction." 

Nous pourrions simplement attendre chaque Promesse, plutôt que de les enchaîner comme ceci, et simplement retourner le résultat de l'analyse finale :

```js
const load = async () => {
  const result = await fetch("https://jsonplaceholder.typicode.com/todos")
  const jsonObj = await result.json();
  const todoContainer = document.querySelector(".todos-container");

  jsonObj.forEach( (todo)=>{
    const todoEl = document.createElement("div");
    todoEl.classList.add("todo");
    const todoTitle = document.createElement("h3");
    todoTitle.classList.add("todo-title");
    todoTitle.textContent=todo.title;

    const todoStatus = document.createElement("div");
    todoStatus.classList.add("todo-status");
    todoStatus.textContent = todo.done ? "Complete" : "Incomplete";

    todoEl.append(todoTitle, todoStatus);
    todoContainer.append(todoEl)
  })
  // ici, si nous le voulons, nous pourrions même retourner cet objet :
  return jsonObj;
}

// plus tard, nous pouvons faire ceci :
const todos = await load();
// remplit le DOM et assigne tous les todos à cette variable
```

C'est mieux, notre fonction `load()` peut être utilisée non seulement pour mettre ces éléments dans le DOM, mais elle nous retourne également les données. 

Ce n'est toujours pas idéal, cependant – nous devons toujours remplir ce DOM lorsque le résultat est en cours de chargement, et nous devons toujours attendre que le chargement se produise. Nous ne savons pas _quand_ `todos` va devenir quelque chose. Finalement, ce sera le cas, mais nous ne savons pas quand.

## Des rappels, quelqu'un ?

Nous avons l'option d'une fonction de rappel. Il pourrait être utile, au lieu de coder en dur la construction du DOM, de passer cela à autre chose. Cela rend la fonction `load` plus abstraite, car elle n'est pas liée à un endpoint particulier.

Voyons à quoi cela pourrait ressembler :

```js
const load = async (apiEndpoint, callbackFn) => {
  const result = await fetch(apiEndpoint);
  if(!result.ok){
    throw new Error(`An error occurred: ${result.status}`)
  }
  // à ce stade, nous avons un bon résultat :
  const jsonObj = await result.json();
  // exécutons notre fonction de rappel, en passant cet objet
  callbackFn(jsonObj)
}

// Utilisons cela. D'abord, nous allons créer une fonction de rappel :
const todoHandler = (todos) => {
  const todoContainer = document.querySelector(".todos-container");

  todos.forEach( (todo)=>{
    const todoEl = document.createElement("div");
    todoEl.classList.add("todo");
    const todoTitle = document.createElement("h3");
    todoTitle.classList.add("todo-title");
    todoTitle.textContent=todo.title;

    const todoStatus = document.createElement("div");
    todoStatus.classList.add("todo-status");
    todoStatus.textContent = todo.done ? "Complete" : "Incomplete";

    todoEl.append(todoTitle, todoStatus);
    todoContainer.append(todoEl)
  })    
}

load("https://jsonplaceholder.typicode.com/todos", todoHandler);
```

C'est mieux – nous disons maintenant à `load` quoi charger, et quoi faire lorsque ce fetch est terminé. Cela fonctionne. Et il n'y a rien de vraiment _faux_ avec cela. Cependant, cela a quelques inconvénients. 

Mon rappel n'est en aucun cas complet. Nous ne gérons pas les erreurs, nous ne gagnons pas vraiment quoi que ce soit avec cette approche. Nous n'obtenons pas les données de la fonction `load` dans un sens que nous pouvons utiliser, de manière opportune.

Et encore une fois, étant moi-même, j'ai voulu essayer une autre méthode.

## Des rappels sans rappels

D'accord, c'est un peu trompeur. Ce ne sont pas des rappels. Nous allons complètement éviter _d'avoir_ des rappels du tout. Que allons-nous avoir à la place ? Des écouteurs d'événements !

Le DOM est tout au sujet de la communication. Les événements se déclenchent partout – événements de souris, événements de clavier, gestes et médias et fenêtre... Le navigateur est un endroit bruyant. 

Mais tout est _contrôlé_, tout est _intentionnel_ et tout est _bien formé_. Les choses sont bien encapsulées, complètement autonomes, mais elles peuvent communiquer des événements en haut et en bas de l'arbre DOM selon les besoins. Et nous pouvons tirer parti de cela, avec l'API `CustomEvent`.

Créer un `CustomEvent` n'est pas vraiment si difficile, il suffit de fournir le nom de l'événement sous forme de chaîne, et la _charge utile_ – les informations à inclure dans cet événement. Voici un exemple :

```js
const myShoutEvent = new CustomEvent('shout', {
  detail: {
    message: 'BONJOUR LE MONDE !!',
    timeSent: new Date() 
  }
})

// et plus tard, nous pouvons envoyer cet événement :
someDomEl.dispatchEvent(myShoutEvent);
```

C'est tout ce qu'il y a à un événement personnalisé. Nous créons l'événement, y compris les données `detail` personnalisées, puis nous `dispatchEvent` sur un nœud DOM donné. Lorsque cet événement est déclenché sur ce nœud DOM, il rejoint le flux normal de communication, se déplaçant le long des phases de bulle et de capture comme tout événement normal – car il _est_ un événement normal.

## Comment cela nous aide-t-il ? 

Et si nous _écoutions_ cet événement personnalisé quelque part, et placions la responsabilité de la gestion de cet événement (et de ses `detail`) avec le récepteur, plutôt que de dire à la fonction `load` quoi faire lorsque nous obtenons ces données ?

Avec cette approche, nous ne nous soucions pas vraiment _quand_ le fetch termine son traitement, nous ne nous soucions pas d'une valeur de retour dans une variable globale – nous disons simplement au nœud DOM de déclencher un événement... _et de transmettre les données récupérées en tant que `detail`_.

Commençons à jouer avec cette idée :

```js
const load = (apiEndpoint, elementToNotify, eventTitle) => {
  fetch(apiEndpoint)
    .then( result => result.json() )
    .then( data => {
       // voici où nous faisons cela : nous voulons créer cet événement personnalisé
       const customEvent = new CustomEvent(eventTitle, {
         detail: {
           data
         }
       });
       // maintenant, nous disons simplement à l'élément de faire son travail :
      elementToNotify.dispatchEvent(customEvent)
     })
};
```

C'est tout. C'est tout le truc. Nous chargeons un endpoint, nous l'analysons, nous enveloppons les données dans un objet d'événement personnalisé, et nous le lançons dans le DOM. 

Le reste est en dehors des préoccupations de cette fonction `load`. Elle ne _se soucie_ pas de l'apparence des données, elle ne _se soucie_ pas de leur provenance, elle ne _retourne_ rien. Elle fait une seule chose – récupérer des données et ensuite en parler.

Maintenant, avec cela en place, comment pourrions-nous le connecter de l'autre côté ?

```js
// une fonction pour créer l'élément Todo dans le DOM...
const createTodo = ({id, title, completed}) => {
  const todoEl = document.createElement("div");
  todoEl.classList.add("todo");

  const todoTitle = document.createElement("h3");
  todoTitle.classList.add("todo-title");
  todoTitle.textContent=todo.title;

  const todoStatus = document.createElement("div");
  todoStatus.classList.add("todo-status");
  todoStatus.textContent = todo.done ? "Complete" : "Incomplete";

  todoEl.append(todoTitle, todoStatus);
    
  return todoEl;
}

// et lorsque cet événement de chargement est déclenché, nous voulons que ce soit
//  l'écouteur d'événement.
const handleLoad = (event)=>{
  // extraire les données de l'événement personnalisé...
  const data = event.detail.data;
  // et créer un nouveau todo pour chaque objet
  data.forEach( todo => {
    event.target.append( createTodo(todo) )
  })
}

// enfin, nous connectons notre événement personnalisé !
container.addEventListener("todo.load", handleLoad)
```

Cela connecte le `container` pour écouter cet événement personnalisé `todo.load`. Lorsque l'événement se produit, il se déclenche et exécute cet écouteur `handleLoad`. 

Il ne fait rien de particulièrement magique : il obtient simplement les `data` de ce `event.detail` que nous créons dans la fonction `load`. Ensuite, `handleLoad` appelle `createTodo` pour chaque objet dans les `data`, créant notre nœud DOM pour chaque élément todo.

En utilisant cette approche, nous avons bien séparé les parties de récupération des données des parties de présentation. La seule chose restante est de dire à l'un de parler à l'autre :

```js
// rappelez-vous, les paramètres que nous avons définis étaient :
// apiEndpoint : url,
// elementToNotify : HTMLDomNode,
// eventTitle : string
load("https://jsonplaceholder.typicode.com/todos", container, 'todo.load');
```

## Pour résumer

Nous avons commencé avec un désordre de code spaghetti peu élégant – la logique de récupération mélangée avec l'analyse et la présentation. Pas bien. Je veux dire, nous le faisons tous, nous l'utilisons tout le temps, mais cela semble douteux. Il n'y a pas de séparation claire, et il n'y a aucun moyen de travailler avec les données en dehors de ce `.then()`.

En utilisant `async/await`, nous _pouvons_ retourner ces données, et nous pouvons les utiliser en dehors du fetch si nécessaire – mais nous n'avons aucun moyen réel de savoir quand ces données ont été chargées. Nous pouvons toujours traiter en ligne, en chargeant la couche de présentation avec le fetch, mais cela n'apporte aucun gain par rapport au précédent.

En utilisant des rappels, nous pouvons commencer à séparer – avec un rappel, nous pouvons charger les données et, lorsque l'opération asynchrone est terminée, exécuter la fonction de rappel. Cela les maintient bien séparés et cela transmet les données dans le rappel en tant que paramètre. C'est _mieux_ que de mélanger la présentation en ligne, mais nous _pouvons_ faire quelque chose de différent.

Et je veux dire par _différent_ – utiliser l'API `CustomEvent` n'est ni mieux ni pire que d'utiliser des rappels. Les deux ont leurs forces et leurs faiblesses. J'aime la propreté du système `CustomEvent`, j'aime que nous puissions l'étendre. Voici quelques exemples :

* une classe Timer, qui déclenche un événement `"timer.tick"` et `"timer.complete"`. Le parent/conteneur du nœud DOM de ce Timer peut écouter ces événements, _se déclenchant de manière asynchrone_, et répondre de manière appropriée, qu'il s'agisse de mettre à jour l'heure affichée ou de provoquer une réaction lorsque le timer est terminé.
* nos Todos – nous pourrions avoir le conteneur écouter `"todo.load"`, `"todo.update"`, ou tout autre événement personnalisé que nous aimons. Nous pourrions gérer les mises à jour en trouvant le nœud DOM pertinent et en mettant à jour son contenu, ou en supprimant tout et en les remplaçant lors d'un chargement.

Nous séparons entièrement la logique du modèle de la logique de présentation, et définissons une interface entre les deux. Propre, clair, fiable et simple.