---
title: Une introduction aux Observables et leurs différences avec les Promesses
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-01T20:29:18.000Z'
originalURL: https://freecodecamp.org/news/what-are-observables-how-they-are-different-from-promises
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/code_feature.jpeg
tags:
- name: asynchronous
  slug: asynchronous
- name: JavaScript
  slug: javascript
- name: observables
  slug: observables
- name: promises
  slug: promises
- name: RxJS
  slug: rxjs
seo_title: Une introduction aux Observables et leurs différences avec les Promesses
seo_desc: 'By Anchal Nigam

  ‘Observables’, ‘Observables’, ‘Observables’...Yes! Today, we will talk about this
  often discussed word of the market. We''ll also learn how they are different from
  Promises (haven''t heard about Promises? Not to worry! You will know mor...'
---

Par Anchal Nigam

« **Observables** », « **Observables** », « **Observables** »... Oui ! Aujourd'hui, nous allons parler de ce mot souvent discuté sur le marché. Nous allons également apprendre comment ils diffèrent des Promesses (vous n'avez pas entendu parler des Promesses ? Pas de souci ! Vous en saurez plus bientôt). Commençons !

J'ai rencontré pour la première fois le terme **Observable** lorsque j'ai commencé à apprendre Angular. Bien que ce ne soit pas une fonctionnalité spécifique à Angular, c'est une nouvelle façon de gérer les requêtes **asynchrones**. Requête asynchrone ? Vous la connaissez, n'est-ce pas ? Non ! Ce n'est pas grave. Commençons par comprendre ce qu'est une requête **asynchrone**.

## Requêtes Asynchrones

Eh bien ! Vous devez avoir lu sur les fonctionnalités asynchrones dans le monde JavaScript. « **Asynchronie** » dans le monde informatique signifie que le flux du programme se produit indépendamment. Il n'attend pas qu'une tâche soit terminée. Il passe à la tâche suivante.

Maintenant, vous pourriez vous demander - que se passe-t-il avec la tâche qui n'est pas terminée ? Le collègue gère ces tâches inachevées. Oui ! En arrière-plan, un collègue travaille et gère ces tâches inachevées et une fois qu'elles sont terminées, il envoie les données en retour.

Cela peut soulever une autre question sur la façon dont nous gérons les données qui sont retournées. La réponse est **Promesses**, **Observables**, **callbacks** et bien d'autres.

Nous savons que ces opérations asynchrones retournent des réponses, soit des données après succès, soit une erreur. Pour gérer cela, des concepts comme **Promesses**, **callbacks**, **observables** sont apparus sur le marché. Eh bien ! Je ne vais pas m'étendre sur eux maintenant car nous nous sommes écartés de notre sous-sujet, à savoir la requête « **async** ». (Ne vous inquiétez pas ! Ces sujets seront discutés bientôt).

Après avoir discuté des points ci-dessus, vous avez peut-être une image approximative de ce qu'est une requête **async**. Clarifions cela. Une requête **Async** est celle où le client n'attend pas la réponse. Rien n'est bloqué. Comprenons ce concept en examinant un scénario très courant.

Dans le monde du web, il est assez courant de frapper le serveur pour obtenir des données comme les détails d'un utilisateur, une liste, etc. Nous savons que cela prendra du temps et que tout peut suivre (succès/échec).

Dans ce cas, au lieu d'attendre que les données arrivent, nous les gérons de manière asynchrone (sans attente) afin que notre application ne soit pas bloquée. De telles requêtes sont des requêtes asynchrones. Je pense que nous sommes maintenant clairs à ce sujet. Alors, voyons comment nous pouvons réellement gérer ces requêtes asynchrones.

Comme je vous l'ai déjà dit, les Observables nous ont donné une nouvelle façon de gérer les requêtes asynchrones. Les autres façons sont les promesses, les callbacks et async/await. Ce sont les façons populaires. Jetons un coup d'œil à deux d'entre elles qui sont les callbacks et les promesses.

## Callbacks

Les callbacks sont assez courants. Les fonctions de callback (comme leur nom l'indique) sont appelées en arrière. C'est-à-dire lorsque la requête est terminée et retourne les données ou une erreur, ces fonctions sont appelées. Jetez un coup d'œil au code pour une meilleure compréhension :

```
const request = require('request');
request('https://www.example.com', function (err, response, body) {
  if(error){
    // Gestion des erreurs
  }
  else {
    // Succès 
  }
});
```

C'est une façon de gérer une requête asynchrone. Mais que se passe-t-il lorsque nous voulons à nouveau demander des données au serveur après le succès de la première requête ? Que se passe-t-il si nous voulons faire une troisième requête après cette deuxième requête réussie ? Horrible !

À ce stade, notre code deviendra désordonné et moins lisible. Cela s'appelle « **callback hell** ». Pour le surmonter, les promesses sont apparues. Elles offrent une meilleure façon de gérer une requête asynchrone qui améliore la lisibilité du code. Comprenons un peu plus.

## Promesses

Les promesses sont des objets qui promettent qu'ils auront une valeur dans un avenir proche - soit un succès, soit un échec. Les promesses ont leurs propres méthodes qui sont **then** et **catch**. **.then()** est appelé lorsque le succès arrive, sinon la méthode **catch()** est appelée. Les **Promesses** sont créées en utilisant le constructeur **promise**. Jetez un coup d'œil au code pour mieux comprendre.

```
function myAsyncFunction(name){
     return new Promise(function(resolve, reject){
          if(name == 'Anchal'){
               resolve('Voici Anchal')
         }
         else{
              reject('Oups ! Ce n'est pas Anchal')
        }

     }
} 

myAsyncFunction('Anchal')
.then(function(val){
      // Logique après succès
      console.log(val)     // sortie -  'Voici Anchal'
})
.catch(function(val){
    //Logique après échec
     console.log(val)     // sortie - 'Oups ! Ce n'est pas Anchal'
})
```

Comme vous pouvez le voir, **myAsyncFunction** promet en fait qu'elle aura une certaine valeur dans un avenir proche. **.then()** ou **.catch()** est appelé selon le statut de la promesse. 

Les **Promesses** améliorent la **lisibilité du code**. Vous pouvez voir à quel point le code est lisible en utilisant les promesses. Une meilleure gestion des opérations asynchrones peut être réalisée en utilisant les Promesses. C'est une brève introduction de ce que sont les promesses, comment elles gèrent les données et quelle beauté les promesses portent.

Maintenant, il est temps d'apprendre sur notre sujet principal : les Observables.

## Qu'est-ce que les Observables ?

Les Observables sont également comme les callbacks et les promesses - qui sont responsables de la gestion des requêtes asynchrones. Les Observables font partie de la bibliothèque **_RXJS_**. Cette bibliothèque a introduit les Observables. 

Avant de comprendre ce qu'est réellement un observable, vous devez comprendre deux modèles de communication : **pull** et **push**. Ces deux concepts sont des protocoles de la manière dont les producteurs de données communiquent avec les consommateurs de données.

### Modèle Pull & Push

Comme je vous l'ai déjà dit, Push et Pull sont des protocoles de communication entre les producteurs et les consommateurs de données. Comprenons les deux un par un.

**Modèle Pull :** Dans ce modèle, le **consommateur** de données est **roi**. Cela signifie que le consommateur de données détermine quand il veut des données du producteur. Le producteur ne décide pas quand les données seront livrées. Vous pouvez mieux comprendre si vous reliez les **fonctions** à cela.

Comme nous le savons, les fonctions sont responsables de l'exécution de certaines tâches. Par exemple, **dataProducer** est une fonction qui retourne simplement une chaîne, comme « **Salut Observable** ».

```
function dataProducer(){
   return 'Salut Observable';
}
```

Maintenant, vous pouvez voir que la fonction ci-dessus ne va pas décider quand elle livrera la chaîne 'Salut Observable'. Cela sera décidé par le consommateur, c'est-à-dire le code qui appelle cette fonction. Le consommateur est roi. La raison pour laquelle il est appelé modèle pull est que la tâche **pull** détermine la communication. C'est le **modèle Pull**. Maintenant, passons au **modèle Push**.

**Modèle Push :** Dans ce modèle, le **producteur** de données est **roi**. Le producteur détermine quand envoyer les données au consommateur. Le consommateur ne sait pas quand les données vont arriver. Comprenons cela à l'aide d'un exemple :

J'espère que vous vous souvenez des **promesses**. Oui, les **Promesses** suivent le **modèle push**. Une Promesse (producteur) livre des données au callback (_.then()_ - consommateur). Les callbacks ne savent pas quand les données vont arriver. Ici, la **promesse** (producteur) est roi. Elle détermine la communication. C'est pourquoi on l'appelle **modèle Push** car le producteur est en charge.

Comme les promesses, les Observables suivent également le modèle push. Comment ? Vous obtiendrez la réponse une fois que j'aurai élaboré sur les observables. Revenons donc aux observables.

## Observables en tant que fonctions

Pour comprendre simplement, vous pouvez penser aux observables comme des fonctions. Jetons un coup d'œil aux exemples ci-dessous :

```
function dataProducer(){
    return 'Salut Observable'
}

var result = dataProducer();
console.log(result) // sortie -  'Salut Observable'

```

Vous pouvez obtenir le même comportement en utilisant un observable :

```
var observable = Rx.Observable.create((observer: any) =>{

   observer.next('Salut Observable');

})

observable.subscribe((data)=>{
   console.log(data);    // sortie - 'Salut Observable'
})
```

D'après ce qui précède, vous pouvez voir que les fonctions et les observables montrent le même comportement. Cela peut amener une question à votre esprit - les observables sont-ils les mêmes que les fonctions ? Non. Je vais clarifier dans une minute pourquoi la réponse est non. Jetons un coup d'œil à une version élaborée de l'exemple ci-dessus.

```
function dataProducer(){
    return 'Salut Observable';
    return 'Suis-je compréhensible ?' // pas un code exécutable.
}

var observable = Rx.Observable.create((observer: any) =>{

   observer.next('Salut Observable');
   observer.next( 'Suis-je compréhensible ?' );

})

observable.subscribe((data)=>{
   console.log(data);    
})

Sortie :
'Salut Observable'
'Suis-je compréhensible ?' 
```

J'espère que vous pouvez maintenant voir la différence que je voulais aborder. D'après ce qui précède, vous pouvez voir, **les fonctions et les observables sont tous deux paresseux**. Nous devons appeler (fonctions) ou souscrire (observables) pour obtenir les résultats. 

**Les abonnements aux observables sont assez similaires à l'appel d'une fonction.** Mais là où les observables sont différents, c'est dans leur capacité à retourner **plusieurs** **valeurs** appelées **flux** (un flux est une séquence de données dans le temps). 

Les observables peuvent non seulement retourner une valeur **de manière synchrone**, mais aussi **asynchrone**.

```
var observable = Rx.Observable.create((observer: any) =>{
   observer.next('Salut Observable');
    setTimeout(()=>{
        observer.next('Oui, quelque peu compréhensible !')
    }, 1000)   

   observer.next( 'Suis-je compréhensible ?' );
})

Sortie :

'Salut Observable'
'Suis-je compréhensible ?' 
'Oui, quelque peu compréhensible !'.

```

En bref, vous pouvez dire **les observables sont simplement une fonction capable de donner plusieurs valeurs au fil du temps, soit de manière synchrone, soit asynchrone**_.

Vous avez maintenant un aperçu des observables. Mais comprenons-les mieux en examinant les différentes phases des observables.

## Phases des Observables

Nous avons déjà vu dans l'exemple ci-dessus comment les observables se créent et s'exécutent et entrent en jeu par abonnement. Par conséquent, il y a quatre étapes par lesquelles passent les observables. Ce sont :

1. **Création**
2. **Abonnement.**
3. **Exécution**
4. **Destruction.**

La **création d'un observable** est faite en utilisant une **fonction create**.

```
var observable = Rx.Observable.create((observer: any) =>{
})

```

Pour faire fonctionner un **observable**, nous devons nous y **abonner**. Cela peut être fait en utilisant la méthode subscribe.

```
observable.subscribe((data)=>{
   console.log(data);    
})
```

L'exécution des observables est ce qui se trouve à l'intérieur du bloc create. Laissez-moi illustrer avec l'aide d'un exemple :

```
var observable = Rx.Observable.create((observer: any) =>{

   observer.next('Salut Observable');        
    setTimeout(()=>{
        observer.next('Oui, quelque peu compréhensible !')
    }, 1000)   

   observer.next( 'Suis-je compréhensible ?' );

})

```

Le code ci-dessus à l'intérieur de la fonction create est l'exécution de l'observable. Les **trois** types de **valeurs** qu'un observable peut livrer à l'abonné sont :

```
observer.next('salut');//ceci peut être multiple (plus d'un)

observer.error('une erreur se produit') // cet appel chaque fois qu'une erreur se produit.

Observer.complete('achèvement de la livraison de toutes les valeurs') // cela indique aux abonnements à l'observable qu'il est terminé. Aucune livraison n'aura lieu après cette instruction.
```

Jetons un coup d'œil ci-dessous pour comprendre les trois valeurs :

```
var observable = Rx.Observable.create((observer: any) =>{
try {
   observer.next('Salut Observable');                                       
    setTimeout(()=>{
        observer.next('Oui, quelque peu compréhensible !')
    }, 1000)   

   observer.next( 'Suis-je compréhensible ?' );
   
   observer.complete();
   
   observer.next('Dernière livraison ?');  
   // le bloc ci-dessus ne va pas s'exécuter car la notification de complétion est déjà envoyée.
   }
catch(err){
     observer.error(err);	
  }

})                      
```

La dernière phase qui arrive sur le marché est la destruction. Après une erreur ou une notification de complétion, l'observable est automatiquement désabonné. Mais il y a des cas où nous devons le désabonner manuellement. Pour faire cela manuellement, utilisez simplement :

```
var subscription = observable.subscribe(x => console.log(x)); // Plus tard : subscription.unsubscribe();
```

C'est tout sur les différentes phases par lesquelles passe un observable.

Je pense que maintenant, nous savons ce que sont les observables ? Mais qu'en est-il de l'autre question qui est - comment les observables sont-ils différents des promesses ? Trouvons la réponse à cela.

## Promesses vs Observables

Comme nous le savons, les promesses sont pour gérer les requêtes asynchrones et les observables peuvent aussi faire de même. Mais où diffèrent-ils ?

### Les Observables sont paresseux alors que les promesses ne le sont pas

Cela est assez explicite : les observables sont paresseux, c'est-à-dire que nous devons nous abonner aux observables pour obtenir les résultats. Dans le cas des promesses, elles s'exécutent immédiatement.

### Les Observables gèrent plusieurs valeurs contrairement aux promesses

Les promesses ne peuvent fournir qu'une seule valeur alors que les observables peuvent vous donner plusieurs valeurs.

### Les Observables sont annulables

Vous pouvez annuler les observables en vous désabonnant en utilisant la méthode **unsubscribe** alors que les promesses n'ont pas une telle fonctionnalité.

### Les Observables fournissent de nombreux opérateurs

Il existe de nombreux opérateurs comme **map**, **forEach**, **filter**, etc. Les observables fournissent ceux-ci alors que les promesses n'ont aucun opérateur dans leur panier.

Ce sont les fonctionnalités qui rendent les observables différents des promesses.

Maintenant, il est temps de conclure. J'espère que vous avez une meilleure compréhension du sujet brûlant des observables !

Merci d'avoir lu !