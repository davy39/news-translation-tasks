---
title: Tutoriel Async Await JavaScript – Comment attendre qu'une fonction se termine
  en JS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-28T22:02:46.000Z'
originalURL: https://freecodecamp.org/news/async-await-javascript-tutorial
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c987e740569d1a4ca1a5b.jpg
tags:
- name: async/await
  slug: asyncawait
- name: asynchronous
  slug: asynchronous
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Tutoriel Async Await JavaScript – Comment attendre qu'une fonction se termine
  en JS
seo_desc: "By Fredrik Strand Oseberg\nWhen does an asynchronous function finish? And\
  \ why is this such a hard question to answer? \nWell it turns out that understanding\
  \ asynchronous functions requires a great deal of knowledge about how JavaScript\
  \ works fundamenta..."
---

Par Fredrik Strand Oseberg

Quand une fonction asynchrone se termine-t-elle ? Et pourquoi est-ce une question si difficile à répondre ?

Eh bien, il s'avère que comprendre les fonctions asynchrones nécessite une grande connaissance de la manière dont JavaScript fonctionne fondamentalement.

Allons explorer ce concept, et apprenons beaucoup de choses sur JavaScript en cours de route.

Êtes-vous prêt ? C'est parti.

## Qu'est-ce que le code asynchrone ?

Par conception, JavaScript est un langage de programmation synchrone. Cela signifie que lorsque le code est exécuté, JavaScript commence en haut du fichier et exécute le code ligne par ligne, jusqu'à ce qu'il soit terminé.

Le résultat de cette décision de conception est qu'une seule chose peut se produire à la fois.

Vous pouvez penser à cela comme si vous jongliez avec six petites balles. Pendant que vous jonglez, vos mains sont occupées et ne peuvent pas gérer autre chose.

C'est la même chose avec JavaScript : une fois le code en cours d'exécution, il a les mains pleines avec ce code. Nous appelons ce type de code synchrone _bloquant_. Parce qu'il bloque effectivement l'exécution d'autres codes.

Revenons à l'exemple du jonglage. Que se passerait-il si vous vouliez ajouter une autre balle ? Au lieu de six balles, vous vouliez jongler avec sept balles. Cela pourrait poser un problème.

Vous ne voulez pas arrêter de jongler, parce que c'est juste trop amusant. Mais vous ne pouvez pas non plus aller chercher une autre balle, car cela signifierait que vous devriez vous arrêter.

La solution ? Déléguer le travail à un ami ou un membre de la famille. Ils ne jonglent pas, donc ils peuvent aller chercher la balle pour vous, puis la lancer dans votre jonglage à un moment où votre main est libre et que vous êtes prêt à ajouter une autre balle en cours de jonglage.

C'est ce qu'est le code asynchrone. JavaScript délègue le travail à autre chose, puis vaque à ses occupations. Ensuite, lorsqu'il est prêt, il recevra les résultats du travail.

## Qui fait l'autre travail ?

D'accord, donc nous savons que JavaScript est synchrone et paresseux. Il ne veut pas faire tout le travail lui-même, donc il le sous-traite à autre chose.

Mais qui est cette entité mystérieuse qui travaille pour JavaScript ? Et comment est-elle engagée pour travailler pour JavaScript ?

Eh bien, regardons un exemple de code asynchrone.

```javascript
const logName = () => {
   console.log("Han")
}

setTimeout(logName, 0)

console.log("Hi there")
```

L'exécution de ce code donne le résultat suivant dans la console :

```javascript
// dans la console
Hi there
Han
```

D'accord. Que se passe-t-il ?

Il s'avère que la manière dont nous sous-traitons le travail en JavaScript est d'utiliser des fonctions et des API spécifiques à l'environnement. Et c'est une source de grande confusion en JavaScript.

**JavaScript s'exécute toujours dans un environnement.**

Souvent, cet environnement est le navigateur. Mais il peut aussi être sur le serveur avec NodeJS. Mais quelle est la différence ?

La différence – et c'est important – est que le navigateur et le serveur (NodeJS), en termes de fonctionnalités, ne sont pas équivalents. Ils sont souvent similaires, mais ils ne sont pas identiques.

Illustrons cela avec un exemple. Disons que JavaScript est le protagoniste d'un livre de fantasy épique. Juste un enfant de ferme ordinaire.

Maintenant, disons que cet enfant de ferme a trouvé deux armures spéciales qui lui donnaient des pouvoirs au-delà des siens.

Quand il utilisait l'armure du navigateur, il obtenait accès à un certain ensemble de capacités.

Quand il utilisait l'armure du serveur, il obtenait accès à un autre ensemble de capacités.

Ces armures ont quelques chevauchements, car les créateurs de ces armures avaient les mêmes besoins à certains endroits, mais pas à d'autres.

C'est ce qu'est un environnement. Un endroit où le code est exécuté, où il existe des outils qui sont construits sur le langage JavaScript existant. Ils ne font pas partie du langage, mais la ligne est souvent floue parce que nous utilisons ces outils tous les jours lorsque nous écrivons du code.

[setTimeout](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope), [fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API), et [DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model) sont tous des exemples d'API Web. (Vous pouvez [voir la liste complète des API Web ici.](https://developer.mozilla.org/en-US/docs/Web/API)) Ce sont des outils qui sont intégrés dans le navigateur, et qui sont mis à notre disposition lorsque notre code est exécuté.

Et parce que nous exécutons toujours JavaScript dans un environnement, il semble que ces outils fassent partie du langage. Mais ils n'en font pas partie.

Donc, si vous vous êtes déjà demandé pourquoi vous pouvez utiliser fetch en JavaScript lorsque vous l'exécutez dans le navigateur (mais que vous devez installer un package lorsque vous l'exécutez dans NodeJS), c'est pourquoi. Quelqu'un a pensé que fetch était une bonne idée, et l'a construit comme un outil pour l'environnement NodeJS.

Confus ? Oui !

Mais maintenant, nous pouvons enfin comprendre ce qui prend en charge le travail de JavaScript, et comment il est engagé.

Il s'avère que c'est l'environnement qui prend en charge le travail, et la manière de faire en sorte que l'environnement effectue ce travail est d'utiliser des fonctionnalités qui appartiennent à l'environnement. Par exemple, _fetch_ ou _setTimeout_ dans l'environnement du navigateur.

## Que se passe-t-il avec le travail ?

Très bien. Donc l'environnement prend en charge le travail. Ensuite ?

À un moment donné, vous devez récupérer les résultats. Mais réfléchissons à la manière dont cela fonctionnerait.

Revenons à l'exemple du jonglage du début. Imaginez que vous avez demandé une nouvelle balle, et qu'un ami a commencé à vous la lancer alors que vous n'étiez pas prêt.

Ce serait un désastre. Peut-être pourriez-vous avoir de la chance et l'attraper et l'intégrer efficacement dans votre routine. Mais il y a de grandes chances que cela puisse vous faire lâcher toutes vos balles et interrompre votre routine. Ne serait-il pas préférable de donner des instructions strictes sur le moment de recevoir la balle ?

Il s'avère qu'il existe des règles strictes concernant le moment où JavaScript peut recevoir le travail délégué.

Ces règles sont régies par la boucle d'événements et impliquent la file d'attente des micro-tâches et des macro-tâches. Oui, je sais. C'est beaucoup. Mais restez avec moi.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/autodraw-31_08_2020.png)

D'accord. Donc, lorsque nous déléguons du code asynchrone au navigateur, le navigateur prend et exécute le code et assume cette charge de travail. Mais il peut y avoir plusieurs tâches données au navigateur, donc nous devons nous assurer que nous pouvons prioriser ces tâches.

C'est là que la file d'attente des micro-tâches et la file d'attente des macro-tâches entrent en jeu. Le navigateur prendra le travail, le fera, puis placera le résultat dans l'une des deux files d'attente en fonction du type de travail qu'il reçoit.

Les promesses, par exemple, sont placées dans la file d'attente des micro-tâches et ont une priorité plus élevée.

Les événements et setTimeout sont des exemples de travail qui sont placés dans la file d'attente des macro-tâches, et ont une priorité plus faible.

Maintenant, une fois le travail terminé, et placé dans l'une des deux files d'attente, la boucle d'événements ira et viendra et vérifiera si JavaScript est prêt à recevoir les résultats.

Ce n'est que lorsque JavaScript a terminé l'exécution de tout son code synchrone, et est prêt, que la boucle d'événements commencera à prendre dans les files d'attente et à remettre les fonctions à JavaScript pour les exécuter.

Donc, regardons un exemple :

```
setTimeout(() => console.log("hello"), 0) 

fetch("https://someapi/data").then(response => response.json())
                             .then(data => console.log(data))

console.log("What soup?")
```

Quel sera l'ordre ici ?

1. Tout d'abord, setTimeout est délégué au navigateur, qui effectue le travail et place la fonction résultante dans la file d'attente des macro-tâches.
2. Ensuite, fetch est délégué au navigateur, qui prend le travail. Il récupère les données depuis le point de terminaison et place les fonctions résultantes dans la file d'attente des micro-tâches.
3. JavaScript affiche "What soup?".
4. La boucle d'événements vérifie si JavaScript est prêt à recevoir les résultats du travail en file d'attente.
5. Lorsque le console.log est terminé, JavaScript est prêt. La boucle d'événements prend les fonctions en file d'attente de la file d'attente des micro-tâches, qui a une priorité plus élevée, et les remet à JavaScript pour les exécuter.
6. Après que la file d'attente des micro-tâches est vide, le rappel setTimeout est retiré de la file d'attente des macro-tâches et remis à JavaScript pour l'exécuter.

```
Dans la console :
// What soup?
// les données de l'API
// hello
```

## Promesses

Maintenant, vous devriez avoir une bonne connaissance de la manière dont le code asynchrone est géré par JavaScript et l'environnement du navigateur. Donc, parlons des promesses.

Une promesse est une construction JavaScript qui représente une valeur future inconnue. Conceptuellement, une promesse est simplement JavaScript promettant de retourner _une valeur_. Il pourrait s'agir du résultat d'un appel d'API, ou il pourrait s'agir d'un objet d'erreur provenant d'une requête réseau échouée. Vous êtes garanti de recevoir quelque chose.

```
const promise = new Promise((resolve, reject) => {
	// Faire une requête réseau
   if (response.status === 200) {
      resolve(response.body)
   } else {
      const error = { ... }
      reject(error)
   }
})

promise.then(res => {
	console.log(res)
}).catch(err => {
	console.log(err)
})
```

Une promesse peut avoir les états suivants :

* remplie - action terminée avec succès
* rejetée - action échouée
* en attente - aucune action n'a été terminée
* réglée - a été remplie ou rejetée

Une promesse reçoit une fonction resolve et une fonction reject qui peuvent être appelées pour déclencher l'un de ces états.

L'un des grands arguments de vente des promesses est que nous pouvons enchaîner des fonctions que nous voulons exécuter en cas de succès (resolve) ou d'échec (reject) :

* Pour enregistrer une fonction à exécuter en cas de succès, nous utilisons .then
* Pour enregistrer une fonction à exécuter en cas d'échec, nous utilisons .catch

```javascript
// Fetch retourne une promesse
fetch("https://swapi.dev/api/people/1")
	.then((res) => console.log("Cette fonction est exécutée lorsque la requête réussit", res)
    .catch(err => console.log("Cette fonction est exécutée lorsque la requête échoue", err)
           
// Enchaînement de plusieurs fonctions
 fetch("https://swapi.dev/api/people/1")
	.then((res) => doSomethingWithResult(res))
    .then((finalResult) => console.log(finalResult))
    .catch((err => doSomethingWithErr(err))
```

Parfait. Maintenant, regardons de plus près à quoi cela ressemble sous le capot, en utilisant fetch comme exemple :

```javascript
const fetch = (url, options) => {
  // simplifié
  return new Promise((resolve, reject) => {

  const xhr = new XMLHttpRequest()
  // ... faire la requête
  xhr.onload = () => {
    const options = {
        status: xhr.status,
        statusText: xhr.statusText
        ...
    }
    
    resolve(new Response(xhr.response, options))
  }
  
  xhr.onerror = () => {
    reject(new TypeError("La requête a échoué"))
  }
}
 
 fetch("https://swapi.dev/api/people/1")
   // Enregistrer handleResponse pour s'exécuter lorsque la promesse est résolue
	.then(handleResponse)
  .catch(handleError)
  
 // conceptuellement, la promesse ressemble maintenant à ceci :
 // { status: "pending", onsuccess: [handleResponse], onfailure: [handleError] }
  
 const handleResponse = (response) => {
  // handleResponse recevra automatiquement la réponse,
  // car la promesse se résout avec une valeur et l'injecte automatiquement dans la fonction
   console.log(response)
 }
 
  const handleError = (response) => {
  // handleError recevra automatiquement l'erreur,
  // car la promesse se résout avec une valeur et l'injecte automatiquement dans la fonction
   console.log(response)
 }
  
// la promesse se résoudra ou sera rejetée, ce qui entraînera l'exécution de toutes les fonctions enregistrées dans les tableaux respectifs
// en injectant la valeur. Inspectons le chemin heureux :
  
// 1. L'écouteur d'événement XHR se déclenche
// 2. Si la requête a réussi, l'écouteur d'événement onload se déclenche
// 3. L'événement onload déclenche la fonction resolve(VALUE) avec la valeur donnée
// 4. Résoudre déclenche et planifie les fonctions enregistrées avec .then
  
  
```

Nous pouvons donc utiliser les promesses pour effectuer un travail asynchrone, et être sûr que nous pouvons gérer tout résultat de ces promesses. C'est la proposition de valeur. Si vous voulez en savoir plus sur les promesses, vous pouvez lire plus à leur sujet [ici](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) et [ici](https://web.dev/promises/).

Lorsque nous utilisons des promesses, nous enchaînons nos fonctions à la promesse pour gérer les différents scénarios.

Cela fonctionne, mais nous devons toujours gérer notre logique à l'intérieur des rappels (fonctions imbriquées) une fois que nous avons nos résultats. Et si nous pouvions utiliser des promesses mais écrire du code qui ressemble à du code synchrone ? Il s'avère que nous pouvons.

## Async/Await

Async/Await est une manière d'écrire des promesses qui nous permet d'écrire _du code asynchrone de manière synchrone_. Regardons cela.

```
const getData = async () => {
    const response = await fetch("https://jsonplaceholder.typicode.com/todos/1")
    const data = await response.json()
    
    console.log(data)
}

getData()
```

Rien n'a changé sous le capot ici. Nous utilisons toujours des promesses pour récupérer des données, mais maintenant cela ressemble à du code synchrone, et nous n'avons plus de blocs .then et .catch.

Async / Await est en fait juste du sucre syntaxique fournissant un moyen de créer du code qui est plus facile à comprendre, sans changer la dynamique sous-jacente.

Regardons comment cela fonctionne.

Async/Await nous permet d'utiliser des [générateurs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Generator) pour _mettre en pause_ l'exécution d'une fonction. Lorsque nous utilisons async / await, nous ne bloquons pas car la fonction rend le contrôle au programme principal.

Ensuite, lorsque la promesse est résolue, nous utilisons le générateur pour rendre le contrôle à la fonction asynchrone avec la valeur de la promesse résolue.

[Vous pouvez lire plus ici pour un excellent aperçu](https://github.com/getify/You-Dont-Know-JS/blob/1st-ed/async%20%26%20performance/ch4.md) des générateurs et du code asynchrone.

En effet, nous pouvons maintenant écrire du code asynchrone qui ressemble à du code synchrone. Ce qui signifie qu'il est plus facile à comprendre, et nous pouvons utiliser des outils synchrones pour la gestion des erreurs tels que try / catch :

```javascript
const getData = async () => {
    try {
    	const response = await fetch("https://jsonplaceholder.typicode.com/todos/1")
    	const data = await response.json()
        console.log(data)
    } catch (err) {
       console.log(err)
    }
    
}

getData()
```

D'accord. Donc, comment l'utilisons-nous ? Pour utiliser async / await, nous devons préfixer la fonction avec async. Cela ne la rend pas asynchrone, cela nous permet simplement d'utiliser await à l'intérieur.

L'omission du mot-clé async entraînera une erreur de syntaxe lors de la tentative d'utilisation de await à l'intérieur d'une fonction régulière.

```javascript
const getData = async () => {
	console.log("Nous pouvons utiliser await dans cette fonction")
}
```

À cause de cela, nous ne pouvons pas utiliser async / await sur le code de niveau supérieur. Mais async et await sont toujours juste du sucre syntaxique sur les promesses. Donc nous pouvons gérer les cas de niveau supérieur avec l'enchaînement de promesses :

```
async function getData() {
  let response = await fetch('http://apiurl.com');
}

// getData est une promesse
getData().then(res => console.log(res)).catch(err => console.log(err); 
```

Cela révèle un autre fait intéressant sur async / await. Lorsque l'on définit une fonction comme async, _elle retournera toujours une promesse_.

L'utilisation de async / await peut sembler magique au début. Mais comme toute magie, ce n'est que de la technologie suffisamment avancée qui a évolué au fil des ans. Espérons que vous avez maintenant une solide compréhension des fondamentaux, et que vous pouvez utiliser async / await en toute confiance.

# Conclusion

Si vous êtes arrivé jusqu'ici, félicitations. Vous venez d'ajouter une pièce clé de connaissance sur JavaScript et son fonctionnement avec ses environnements à votre boîte à outils.

C'est définitivement un sujet confus, et les lignes ne sont pas toujours claires. Mais maintenant, vous avez espérons-le une compréhension de la manière dont JavaScript fonctionne avec le code asynchrone dans le navigateur, et une meilleure maîtrise des promesses et de async / await.

Si vous avez aimé cet article, vous pourriez aussi aimer ma [chaîne YouTube](https://www.youtube.com/channel/UCZTeUahnA2GMoo_YpTBFo9A?view_as=subscriber). J'ai actuellement une [série sur les fondamentaux du web](https://www.youtube.com/watch?v=kmvg9C8hVa0&list=PL_kr51suci7XVVw4SJLZ0QQBAsL2K8Opy) où je passe en revue [HTTP](https://www.youtube.com/watch?v=0ykAOzJb-U8&t=19s), [la construction de serveurs web à partir de zéro](https://www.youtube.com/watch?v=R5uwuG1wPR8) et plus encore.

Il y a aussi une série en cours sur [la construction d'une application complète avec React](https://www.youtube.com/playlist?list=PL_kr51suci7WkVde-b09G4XHEWQrmzcpJ), si c'est votre truc. Et je prévois d'ajouter beaucoup plus de contenu ici à l'avenir en approfondissant les sujets JavaScript.

Et si vous voulez dire bonjour ou discuter du développement web, vous pouvez toujours me contacter sur Twitter à @foseberg. Merci d'avoir lu !