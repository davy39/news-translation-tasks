---
title: Le try-catch de JavaScript a caché mes bugs !
subtitle: ''
author: Zubin Pratap
co_authors: []
series: null
date: '2019-11-08T14:30:00.000Z'
originalURL: https://freecodecamp.org/news/javascripts-try-catch-hid-my-bugs
coverImage: https://www.freecodecamp.org/news/content/images/2019/11/thomas-smith-doI0mceCxfk-unsplash.jpg
tags:
- name: Code Quality
  slug: code-quality
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
seo_title: Le try-catch de JavaScript a caché mes bugs !
seo_desc: 'Let me start by making one thing clear - JavaScript is a great language,
  and not to blame. I was totally to blame - my mental model of error handling was
  incomplete, and that caused the trouble. Hence, this post.

  But first, let me give you some conte...'
---

Permettez-moi de commencer par clarifier une chose : JavaScript est un excellent langage, et ce n'est pas sa faute. J'étais totalement responsable - mon modèle mental de la gestion des erreurs était incomplet, et c'est ce qui a causé le problème. D'où cet article.

Mais d'abord, laissez-moi vous donner un peu de contexte. J'écrivais un ensemble de code impliquant des API tierces ([les API de facturation récurrente et d'abonnement de Stripe](https://stripe.com/docs/billing/quickstart), pour être précis), et j'avais écrit une classe wrapper et quelques gestionnaires de routes serveur pour répondre aux requêtes de l'application web front-end. L'ensemble de l'application est en React + TypeScript + Node, avec un serveur [Koa](https://koajs.com/).

Dans ce cadre, j'essayais de gérer les erreurs suivantes :

1. Les erreurs lancées par l'API de Stripe
   
2. Les erreurs lancées par ma classe wrapper, notamment lors de la récupération des données utilisateur depuis la base de données
   
3. Les erreurs dans les gestionnaires de routes qui découlent d'une combinaison des deux ci-dessus.
   

Pendant le développement, mes erreurs les plus courantes étaient des données incomplètes dans les requêtes serveur et des données incorrectes passées à Stripe.

Pour vous aider à visualiser le flux de données, laissez-moi vous donner un peu de contexte sur le code côté serveur. Typiquement, voici à quoi ressemblait la chaîne d'appels de fonctions :

*Gestionnaire de route -> Wrapper Stripe -> API Stripe*

La première fonction appelée serait dans le Gestionnaire de route, puis dans la classe Wrapper Stripe, à l'intérieur de laquelle la méthode de l'API Stripe serait appelée. Ainsi, la pile d'appels a le Gestionnaire de route en bas (première fonction appelée) et la méthode de l'API Stripe en haut (dernière fonction appelée).

Le problème était que je ne savais pas où placer ma gestion des erreurs. Si je ne mettais pas de gestionnaire d'erreurs dans le code serveur, alors Node planterait (littéralement, quitterait l'exécution !) et le front-end recevrait une réponse HTTP d'erreur (généralement une erreur HTTP [5xx](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500)). J'ai donc placé quelques gestionnaires `try-catch` à l'intérieur des diverses méthodes appelées, et j'ai ajouté des instructions de journalisation à l'intérieur du bloc `catch`. Ainsi, je pouvais déboguer l'erreur en suivant les logs.

Un exemple de la logique d'appel :

```javascript
 function stripeAPI(arg){
    console.log('this is the first function')
    if(!arg) throw new Error('no arg!')
    // else
    saveToDb()
}

function stripeWrapper(){
    console.log('this is the second function, about to call the first function')
    try{
        stripeAPI()
    } catch(err) {
//         console.log(' this error will not bubble up to the first function that triggered the function calls!')
    }
}

function routeHandler(){
    console.log('this is the third  function, about to call the second function')
    stripeWrapper()
}


function callAll(){
    try{
       routeHandler() 
       return 'done'
    } catch (err){
       console.log('error in callAll():', err)
       return ' not done '
    }
    
}


callAll()
```

Les problèmes ?

1. Si je ne journalisais pas l'erreur, je *perdais* l'erreur ! Dans l'extrait ci-dessus, notez que même si j'ai appelé `first()` sans les arguments requis, l'erreur définie dans la définition de `first` n'a pas été lancée ! De plus, il n'y a pas de méthode `saveToDb()` définie... et pourtant cela n'a pas été capturé ! Si vous exécutez ce code ci-dessus, vous verrez qu'il retourne 'done' - et vous n'avez aucune idée que votre base de données n'a pas été mise à jour et que quelque chose a mal tourné ! ⚠️⚠️⚠️
   
2. Ma console avait beaucoup trop de logs, répétant la même erreur. Cela signifiait également qu'en production, il y avait une journalisation excessive... ?
   
3. Le code avait l'air moche. Presque aussi moche que ma console.
   
4. Les autres qui travaillaient avec le code le trouvaient confus et un cauchemar pour le débogage. ?
   

Aucun de ces résultats n'est bon, et tous sont évitables.

## Les concepts

Alors, clarifions quelques bases. Je suis sûr que vous les connaissez, mais certaines personnes peuvent ne pas les connaître, et ne les laissons pas de côté !

Quelques termes de base :

**Erreur** - également connue sous le nom d'« exception », se produit lorsque quelque chose ne va pas dans le code Node, et le programme se termine immédiatement. Les erreurs, si elles ne sont pas gérées, feront que le programme s'arrêtera brutalement, et des messages disgracieux seront affichés dans la console, avec un long et généralement hideux message de trace de pile d'erreur.

**Throw** - l'opérateur `throw` est la manière dont le langage gère une erreur. En utilisant `throw`, vous générez une exception en utilisant la valeur que vous placez après l'opérateur. Notez que le code après `throw` ne s'exécute pas - en ce sens, c'est comme une instruction `return`.

**Error** - il existe un [objet](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error) JavaScript appelé `Error`. Une erreur est « lancée » afin d'aider le programmeur à savoir que quelque chose doit être géré. Pensez-y comme à une petite bombe à retardement ? qui est lancée d'une fonction à une autre dans une chaîne d'appels de fonctions. Techniquement, vous pouvez lancer n'importe quelle donnée, y compris des primitives JavaScript comme une erreur, mais il est généralement bon de lancer un objet `Error`.

Vous construisez généralement l'objet `Error` en passant une chaîne de message comme ceci : `new Error('Ceci est une erreur')`. Mais simplement créer un nouvel objet `Error` n'est pas utile car ce n'est que la moitié du travail. Vous devez le `lancer` pour qu'il puisse être capturé. C'est ainsi qu'il devient utile.

Les langages viennent généralement avec un [ensemble standard d'erreurs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors), mais vous pouvez créer un message d'erreur personnalisé avec le constructeur `new Error('ceci est mon message d'erreur')`, et votre message d'erreur devrait vous aider à comprendre ce qui se passe. Plus d'informations sur les [erreurs Node](https://nodejs.org/api/errors.html).

**Catch** - c'est ce que vous faites lorsque quelqu'un vous lance quelque chose, n'est-ce pas ? Vous le feriez probablement de manière réflexe même si quelqu'un vous lançait l'un de ceux-ci... ?!

L'instruction `catch` en JavaScript vous permet de gérer une erreur ? qui est lancée. Si vous ne capturez pas l'erreur, alors l'erreur « remonte » (ou descend, selon la manière dont vous voyez la pile d'appels) jusqu'à ce qu'elle atteigne la première fonction appelée et là, elle fera planter le programme.

Dans mon exemple, une erreur lancée par l'API Stripe remontera jusqu'à ma fonction Route-Handler, à moins que je ne la capture quelque part en cours de route et que je la traite. Si je ne gère pas l'erreur, Node lancera une erreur `uncaughtException` et mettra fin au programme.

Revenons à mon exemple :

**Pile d'appels**

*Route-Handler -> Stripe Wrapper -> Stripe API*

**Chemin de l'erreur**

*Stripe API (❌ lancée ici) -> API Wrapper (❌ non capturée) ->* *Route-Handler (❌ toujours non capturée) -> ccrraashh* ???

Nous voulons éviter les plantages de l'application car cela peut corrompre vos données, rendre votre état incohérent et faire penser à votre utilisateur que votre application est nulle. Ainsi, la gestion des erreurs de manière réfléchie nécessite plusieurs niveaux d'analyse.

Il existe des guides détaillés sur la gestion des erreurs en JavaScript et l'un de mes préférés est [ici](http://javascript.info/try-catch), mais je vais résumer mes principales conclusions pour vous ici.

## Instruction Try-Catch

Utilisez-les pour gérer les erreurs de manière élégante, mais soyez prudent quant à *où* et *quand*. Lorsque les erreurs sont capturées et non gérées correctement, elles sont perdues. Ce processus de « remontée » ne se produit que jusqu'à ce que l'erreur rencontre une instruction `catch`. Si une instruction `catch` dans la chaîne d'appels intercepte l'erreur, alors l'erreur ne fera pas planter l'application, mais ne pas la gérer cachera l'erreur ! Ensuite, elle est passée en argument à `catch` et nécessite que vous la gériez là.

```javascript
try{
// logique du code
} catch (error) {
// gérer l'erreur de manière appropriée
}
```

Il est donc très important de capturer *et* gérer l'erreur à un point où cela a le plus de sens logique pour vous lorsque vous devez la déboguer. Il est tentant de penser que vous devez la capturer dès le premier endroit où elle apparaît (la dernière fonction appelée qui se trouve tout en haut de la pile d'appels), mais ce n'est pas vrai !

*Route-Handler -> Stripe Wrapper (ne capturez pas ici !) -> Stripe API*

Si je place mon `try-catch` dans le Stripe Wrapper qui appelle directement l'API de Stripe, alors je n'ai pas d'information sur *où* ma fonction Stripe Wrapper a été appelée. Peut-être que c'était le gestionnaire, peut-être que c'était une autre méthode à l'intérieur de mon wrapper, peut-être que c'était dans un autre fichier ! Dans cet exemple simple, il est évidemment appelé par Route-Handler, mais dans une application réelle, il pourrait être appelé à plusieurs endroits.

Au lieu de cela, il est logique pour moi de placer le `try-catch` dans le Route-Handler, qui est le tout premier endroit où les appels de fonctions commencent et qui ont abouti à l'erreur. Ainsi, vous pouvez tracer la pile d'appels (également appelée déroulement de la pile d'appels) et approfondir l'erreur. Si j'envoie de mauvaises données à Stripe, il lancera une erreur, et cette erreur passera par mon code jusqu'à ce que je la capture.

Mais lorsque je la capture, je dois la gérer correctement, sinon je pourrais involontairement dissimuler cette erreur. La gestion des erreurs signifie généralement décider si mon utilisateur front-end doit savoir que quelque chose a mal tourné (par exemple, leur paiement n'a pas fonctionné), ou s'il s'agit simplement d'une erreur interne du serveur (par exemple, Stripe n'a pas pu trouver l'ID de produit que j'ai passé) que je dois gérer de manière élégante sans perturber mes utilisateurs front-end et sans faire planter le code Node. Si j'ai ajouté des choses à la base de données qui ne sont pas correctes, alors je devrais nettoyer ces écritures erronées maintenant.

Lors de la gestion de l'erreur, il est bon de la journaliser afin que je puisse surveiller l'application pour les bugs et les échecs en production et déboguer efficacement. Donc, au minimum, la gestion inclurait la journalisation de l'erreur dans l'instruction `catch`. Mais...

```javascript
 function stripeAPI(arg){
    console.log('this is the first function')
    if(!arg) throw new Error('no arg!')
    // else
    saveToDb()
}

function stripeWrapper(){
    console.log('this is the second function, about to call the first function')
    try {
        stripeAPI()
    } catch(err) {
        console.log('Oops!  err will not bubble up to the first function that triggered the function calls!')
    }
}

function routeHandler(){
    console.log('this is the third  function, about to call the second function')
    stripeWrapper()
}


function callAll(){
    try {
       routeHandler() 
       return 'done'
    } catch (err){  
       console.log('error in callAll():', err)
       return ' not done '
    }
    
}


callAll()
```

...comme vous pouvez le voir ci-dessus, si je la capture et la journalise au niveau intermédiaire (ma classe Stripe Wrapper), elle n'atteindra pas `routeHandler` ou `callAll`, et mon application ne saura pas que quelque chose a mal tourné. `callAll` retourne toujours `done` et la seule preuve que quelque chose a mal tourné était dans l'instruction de journalisation : `'Oops! err will not bubble up to to first function that triggered the function calls!'`. Si nous n'avions pas mis d'instruction de journalisation là, l'erreur aurait disparu sans laisser de trace.

C'est ce qu'on appelle « masquer les erreurs » et cela rend le débogage pénible. Si j'ajoute un `try-catch` mais que je ne fais rien dans l'instruction `catch`, j'empêcherai mon programme de planter. Mais je finis aussi par « masquer » le problème ! Cela conduit généralement à un état incohérent - certaines parties de mon code serveur pensent que tout va bien, et le disent à mon front-end. Mais une autre partie de mon code serveur a indiqué que quelque chose n'allait pas !

Dans cet exemple simple, c'est facile à démêler, mais pensez à des appels profondément imbriqués dans toute votre application - quel cauchemar !

Si vous devez absolument gérer l'erreur au milieu de votre pile d'appels, assurez-vous de relancer l'erreur de manière appropriée. Cela signifie terminer votre instruction `catch` par une autre opération `throw error`. Ainsi, l'erreur sera relancée et continuera à « remonter » vers la première fonction (bas de la pile d'appels) qui a déclenché la chaîne d'appels où elle peut être gérée à nouveau.

Voici à quoi cela ressemble, en ajoutant simplement une petite relance dans la fonction `stripeWrapper()`. Exécutez le code et voyez la différence de résultat car `callAll()` reçoit maintenant l'erreur !

```plaintext
function stripeWrapper(){
    console.log('this is the second function, about to call the first function')
    try{
        stripeAPI()
    } catch(err) {
        console.log('Oops!  err will not bubble up to to first function that triggered the function calls!')

        throw err  // ajoutez ceci pour relancer !

    }
}

function callAll(){
    try{
       routeHandler() 
       return 'done'
    } catch (err){  // capture l'erreur relancée et l'affiche dans la console !
       console.log('error in callAll():', err)
       return ' not done '
    }
    
}
```

Puisque vous avez relancé l'erreur à l'étape intermédiaire, elle est allée à la frontière extérieure et a été capturée là. Le code retourne `not done` et vous pouvez enquêter sur la raison pour laquelle l'erreur dit 'no arg'. Vous pouvez également voir qu'il n'a jamais exécuté `saveToDb()`, car l'erreur a été lancée avant que ce code ne puisse être exécuté ! Cela pourrait être une bonne chose dans les cas où vous enregistrez des choses dans la base de données *en supposant qu'il n'y avait pas d'erreurs jusqu'à ce point*. Imaginez enregistrer des choses dans la base de données qui n'auraient jamais dû être enregistrées - ce sont des données sales dans la base de données maintenant ! ???

Donc, ne faites pas ce que j'ai fait dans mes premiers jours de programmation et ne journalisez pas simplement l'erreur à *chaque* étape de la pile d'appels et ne la relancez pas. Cela signifie simplement que vous obtiendrez plusieurs logs pour chaque erreur lorsqu'elle passe par la pile d'appels ! N'interceptez l'erreur qu'à un endroit où vous pouvez la gérer de manière efficace et utile, idéalement une seule fois dans une chaîne d'appels donnée.

En général, il est vraiment utile de placer votre instruction `try catch` dans la fonction la plus externe (première fonction appelée) qui se trouve au bas de la pile d'appels. Vous pouvez l'identifier comme l'endroit où l'erreur remontera *juste avant* de lancer une erreur `uncaughtException`. C'est un bon endroit pour la capturer, la journaliser et la gérer.

Pour voir la différence de gestion lorsque vous n'utilisez pas le `try-catch`, modifiez simplement `callAll()` pour qu'il ressemble à ceci :

```plaintext
function callAll(){
    routeHandler()  
    
    // ceci ne s'exécutera pas !
    console.log('This function is not contained inside a try-catch, so will crash the node program.')
}

callAll()
```

Vous noterez que l'instruction `console.log` ne s'exécute jamais ici car le programme plante lorsque `routeHandler()` termine son exécution.

## Règles de base ???

Alors, résumons quelques règles rapides qui couvriront 90 % de vos besoins :

1. Ne jonchez pas votre code d'instructions `try-catch`
   
2. Essayez autant que possible de `capturer` une seule fois dans une chaîne de fonctions donnée
   
3. Essayez de placer ce `catch` à la frontière la plus externe - la première fonction qui commence la chaîne d'appels de fonctions (bas de la pile d'appels)
   
4. Ne laissez pas votre instruction `catch` vide comme moyen d'empêcher votre programme de planter ! Si vous ne la gérez pas, il y a des chances que cela conduise à un état incohérent entre votre front-end et votre back-end. Cela peut être dangereux et conduire à une expérience utilisateur horrible ?!
   
5. N'utilisez pas une instruction `catch` uniquement au milieu de la pile d'appels, et pas à la frontière externe. Cela fera que l'erreur sera « cachée » au milieu de votre code où elle ne vous aidera pas à déboguer ou à gérer les données correctement. Les autres qui travaillent avec votre code trouveront où vous vivez et couperont votre connexion internet.
   
6. Capturez-la là où vous devez savoir, et là où vous pouvez faire de manière significative toutes les choses nécessaires pour nettoyer.
   

*Stripe API (❌ lancée ici) -> API Wrapper (❌ passage) ->* *Route-Handler (❌ capturée, gérée, journalisée) ->* ???

Merci d'avoir lu !

Si vous souhaitez en savoir plus sur mon parcours dans le code, consultez l'[épisode 53](http://podcast.freecodecamp.org/53-zubin-pratap-from-lawyer-to-developer) du [podcast freeCodeCamp](http://podcast.freecodecamp.org/), où Quincy (fondateur de freeCodeCamp) et moi partageons nos expériences en tant que reconvertis professionnels qui pourraient vous aider dans votre parcours. Vous pouvez également accéder au podcast sur [iTunes](https://itunes.apple.com/au/podcast/ep-53-zubin-pratap-from-lawyer-to-developer/id1313660749?i=1000431046274&mt=2), [Stitcher](https://www.stitcher.com/podcast/freecodecamp-podcast/e/59201373?autoplay=true), et [Spotify](https://open.spotify.com/episode/4lG0RGpzriG5vXRMgza05C).

Je vais également organiser quelques AMAs et webinaires dans les mois à venir. Si cela vous intéresse, veuillez me le faire savoir en allant [ici](http://www.matchfitmastery.com/). Et bien sûr, vous pouvez également me tweeter à [@ZubinPratap](https://twitter.com/zubinpratap).

(Photo de bannière par [Thomas Smith](https://unsplash.com/@thomastasy?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) sur [Unsplash](https://unsplash.com/s/photos/bugs?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText))