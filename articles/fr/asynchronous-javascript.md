---
title: Comment fonctionne JavaScript Asynchrone
subtitle: ''
author: Kedar Makode
co_authors: []
series: null
date: '2023-02-17T18:37:03.000Z'
originalURL: https://freecodecamp.org/news/asynchronous-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/pexels-zhang-kaiyv-1168940.jpg
tags:
- name: asynchronous
  slug: asynchronous
- name: asynchronous programming
  slug: asynchronous-programming
- name: JavaScript
  slug: javascript
seo_title: Comment fonctionne JavaScript Asynchrone
seo_desc: 'In this tutorial, you''ll learn all about Asynchronous JavaScript.

  But before we dive into that, we need to make sure you understand what Synchronous
  code is and how it works.

  What is Synchronous Code?

  When we write a program in JavaScript, it execute...'
---

Dans ce tutoriel, vous apprendrez tout sur JavaScript Asynchrone.

Mais avant de plonger dans ce sujet, nous devons nous assurer que vous comprenez ce qu'est le code Synchrone et comment il fonctionne.

## Qu'est-ce que le Code Synchrone ?

Lorsque nous écrivons un programme en JavaScript, il s'exécute ligne par ligne. Lorsqu'une ligne est complètement exécutée, alors et alors seulement le code passe à l'exécution de la ligne suivante.

Regardons un exemple de cela :

```javascript
let greet_one = "Bonjour"
let greet_two = "Monde !!!"
console.log(greet_one)
for(let i=0;i<1000000000;i++){
}
console.log(greet_two);
```

Maintenant, si vous exécutez l'exemple ci-dessus sur votre machine, vous remarquerez que `greet_one` est enregistré en premier. Ensuite, le programme attend quelques secondes et enregistre `greet_two`. Cela est dû au fait que le code s'exécute ligne par ligne. Cela s'appelle le code synchrone.

Cela crée beaucoup de problèmes. Par exemple, si une certaine partie du code prend 10 secondes à s'exécuter, le code qui suit ne pourra pas s'exécuter jusqu'à ce qu'il soit terminé, provoquant des retards.

## Qu'est-ce que le Code Asynchrone ?

Avec le code asynchrone, plusieurs tâches peuvent s'exécuter en même temps pendant que les tâches en arrière-plan se terminent. C'est ce que nous appelons le code non bloquant. L'exécution d'autres codes ne s'arrêtera pas pendant qu'une tâche asynchrone termine son travail.

Regardons un exemple de code asynchrone :

```javascript
let greet_one = "Bonjour"
let greet_two = "Monde !!!"
console.log(greet_one)
setTimeout(function(){
    console.log("Asynchrone");
}, 10000)
console.log(greet_two);
```

Dans l'exemple ci-dessus, si vous exécutez le code sur votre machine, vous verrez `greet_one` et `greet_two` enregistrés même s'il y a du code entre ces deux logs.

Maintenant, setTimeout est asynchrone, donc il s'exécute en arrière-plan, permettant au code qui suit de s'exécuter pendant qu'il fonctionne. Après 10 secondes, `Asynchrone` s'affichera parce que nous avons défini un temps de 10 secondes dans setTimeout pour l'exécuter après 10 secondes.

Dans ce tutoriel, nous allons étudier JavaScript asynchrone en détail afin que vous puissiez apprendre à écrire votre propre code asynchrone. Je voulais simplement vous donner un avant-goût de JavaScript asynchrone en utilisant des fonctions intégrées pour aiguiser votre appétit.

# Comment fonctionnent les Callbacks en JavaScript

> ["Une fonction de rappel est une fonction passée dans une autre fonction en tant qu'argument, qui est ensuite invoquée à l'intérieur de la fonction externe pour compléter une sorte de routine ou d'action."](https://developer.mozilla.org/en-US/docs/Glossary/Callback_function) ([MDN](https://developer.mozilla.org/en-US/docs/Glossary/Callback_function))

Regardons un exemple de code pour voir pourquoi utiliser des callbacks serait utile :

```javascript
function compute(action, x, y){
    if(action === "add"){
        return x+y
    }else if(action === "divide"){
        return x/y
    }
}

console.log(compute("add",10,5))   
console.log(compute("divide",10,5))
```

Dans l'exemple ci-dessus, nous avons deux opérations. Mais que faire si nous voulons ajouter plus d'opérations ? Alors le nombre d'instructions if/else augmenterait. Ce code serait long, donc nous utilisons des callbacks à la place :

```javascript
function add(x,y){
    return x+y
}

function divide(x,y){
    return x/y
}

function compute(callBack, x, y){
    return callBack(x,y)
}

console.log(compute(add, 10, 5))    // 2
console.log(compute(divide, 10, 5))
```

Maintenant, lorsque nous appelons `compute` avec trois arguments, l'un d'eux est une opération. Lorsque nous entrons dans la fonction compute, la fonction retourne une fonction avec un nom d'action donné. Elle appelle ensuite cette fonction et retourne le résultat.

## Bienvenue dans l'Enfer des Callbacks

Les callbacks sont géniaux, mais vous ne voulez pas les utiliser de manière excessive. Si vous le faites, vous obtiendrez quelque chose appelé "l'enfer des callbacks". Cela se produit lorsque vous imbriquez des callbacks dans des callbacks sur plusieurs niveaux.

La forme de l'enfer des callbacks ressemble à une pyramide et est également appelée la "pyramide de la mort". Cela rend le code très difficile à maintenir et à comprendre. Voici un exemple de l'enfer des callbacks :

```javascript
setTimeout(() =>{
    console.log("Une Seconde");
    setTimeout(() =>{
        console.log("Deux Secondes");
        setTimeout(() =>{
            console.log("Trois Secondes");
            setTimeout(() =>{
                console.log("Quatre Secondes");
                setTimeout(() =>{
                    console.log("Cinq Secondes");
                }, 1000)
            }, 1000)
        }, 1000)
    }, 1000)
}, 1000)
```

Lorsque une seconde s'est écoulée, le code enregistre "une seconde". Ensuite, il y a un autre appel qui s'exécute après une seconde de plus et enregistre "deux secondes" et ainsi de suite.

Nous pouvons échapper à cet enfer des callbacks en utilisant quelque chose appelé `Promises` en JavaScript asynchrone.

# Comment fonctionnent les Promesses en JavaScript

Une promesse est un espace réservé pour le résultat futur d'une opération asynchrone. En termes simples, nous pouvons dire que c'est un conteneur pour une valeur future.

Lorsque nous utilisons des promesses, nous n'avons pas besoin de nous appuyer sur des callbacks, ce qui nous aide à éviter l'enfer des callbacks.

Avant de vous montrer comment fonctionnent les promesses à travers du code, je vais expliquer les promesses en utilisant l'analogie d'un billet de loterie.

Les promesses sont comme un billet de loterie. Lorsque nous achetons un billet de loterie, il indique que nous recevrons de l'argent si notre résultat est correct. C'est comme une promesse. Le tirage de la loterie se fait de manière asynchrone, et si les numéros correspondent, nous recevons l'argent qui était promis.

Maintenant, regardons un exemple de code :

```javascript
const request = fetch('https://course-api.com/react-store-products')
console.log(request);
```

Le code ci-dessus utilise fetch pour une requête à partir d'une API. Il retourne une promesse qui obtiendra une réponse du serveur.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/1212.png align="left")

Voici à quoi ressemble une promesse. Elle a un état de promesse particulier et un résultat. Lorsqu'une promesse est créée, elle s'exécute de manière asynchrone. Lorsque la tâche donnée est terminée, alors nous disons que la promesse est réglée. Après que la promesse soit réglée, nous pouvons avoir soit un état de promesse rempli ou rejeté en fonction du résultat de la promesse. Nous pouvons gérer ces différents états de différentes manières dans notre code.

### Comment Consommer des Promesses

Nous pouvons consommer une promesse en utilisant la méthode then() sur la promesse. Le code de production est un code qui peut prendre un certain temps à compléter. Le code de consommation est un code qui doit attendre le résultat.

Donc, si nous consommons une promesse, cela signifie que lorsque nous faisons une requête, nous attendons le résultat. Ensuite, après que le résultat arrive, nous effectuons une opération sur ces résultats.

Continuons à utiliser l'exemple ci-dessus pour comprendre comment nous pouvons consommer une promesse.

```javascript
const request = fetch('https://course-api.com/react-store-products').then((response) =>{
    console.log(response);
    return response.json()
}).then((data) =>{
    console.log(data);
})
```

Nous faisons une requête à l'API du pays. Ensuite, après la requête fetch, nous utilisons la méthode `then()` pour consommer la promesse. Après cela, nous retournons un ensemble d'informations comme l'en-tête, le statut, etc. (vous pouvez le voir dans l'image de sortie ci-dessous).

Donc, nous avons spécifiquement besoin de données que nous devons convertir en JSON, ce qui retourne une promesse. Les données qui sont retournées lorsque nous faisons une requête API sont retournées sous la forme d'une promesse.

Pour gérer cette promesse, nous utilisons à nouveau la méthode then() pour enregistrer les données de la réponse. L'utilisation de plusieurs méthodes `then()` sur une seule requête est appelée **chaînage de promesses.**

![Image](https://www.freecodecamp.org/news/content/images/2023/01/121212.png align="left")

## Comment Gérer les Promesses Rejetées

Consommer des promesses est bien et tout, mais il est également très important d'apprendre à gérer les promesses rejetées. Dans des situations réelles, il pourrait y avoir des moments où notre application plante en raison de la non-gestion des promesses rejetées.

Prenons donc un exemple : nous allons mettre nos promesses dans une fonction appelée `call()`. En HTML, nous allons créer un bouton et ajouter un écouteur d'événement. Lorsque nous cliquons sur le bouton, il appellera la fonction `call()`.

Voici à quoi cela ressemble :

`index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Promesses</title>
</head>
<body>
    
    <button class="btn">Requête</button>
    <script src="./script.js"></script>
</body>
</html>
```

`script.js`:

```javascript
function call(){

    const request = fetch('https://course-api.com/react-store-products').then((response) =>{
        console.log(response);
        return response.json()
    }).then((data) =>{
        console.log(data);
    })

}

const btn = document.querySelector("button")
btn.addEventListener("click", function(){
    call();
})
```

Pourquoi faisons-nous cela ? Nous configurons la promesse pour qu'elle soit rejetée. Une fois que nous exécutons ce code, allez dans l'inspecteur et sélectionnez l'onglet réseau. Réglez "No throttling" sur hors ligne et cliquez sur le bouton pour envoyer la requête. Vous obtiendrez une promesse rejetée.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/1111.png align="left")

Une fois que nous cliquons sur le bouton, nous obtiendrons une erreur causée par l'absence de connexion Internet.

Cette situation peut se produire dans le monde réel si la connexion Internet d'un utilisateur est lente. Nous faisons une requête API pour laquelle nous avons besoin d'une connexion Internet avec une vitesse décente. Parfois, le client peut avoir un problème avec son Internet. Cela peut conduire à des promesses rejetées qui lanceront une erreur que nous n'avons pas encore vu comment gérer.

Maintenant, nous allons apprendre à gérer cette erreur. Nous avons utilisé then() pour consommer nos promesses. De manière similaire, nous allons chaîner la méthode `catch()` à cette promesse. Regardez le code suivant :

```javascript
function call(){

    const request = fetch('https://course-api.com/react-store-products').then((response) =>{
        console.log(response);
        return response.json()
    }).then((data) =>{
        console.log(data);
    }).catch((err) =>{
        alert(err);
    })

}

const btn = document.querySelector("button")
btn.addEventListener("click", function(){
    call();
})
```

Maintenant, la méthode `catch()` obtiendra une erreur de la promesse rejetée et affichera le message dans une alerte.

Nous obtenons l'erreur parce que nous avons obtenu une promesse rejetée qui indique qu'il y a un problème. Nous pouvons faire ce que nous voulons dans le bloc catch() lorsque nous rencontrons une erreur.

Avec la méthode catch(), il y a une autre méthode utile appelée `finally()`. Nous pouvons la chaîner aux promesses qui s'exécuteront peu importe si la promesse est acceptée ou rejetée.

```javascript
function call(){

    const request = fetch('https://course-api.com/react-store-products').then((response) =>{
        console.log(response);
        return response.json()
    }).then((data) =>{
        console.log(data);
    }).catch((err) =>{
        console.log(err);
    }).finally(() =>{
        console.log("S'exécutera toujours");
    })

}

const btn = document.querySelector("button")
btn.addEventListener("click", function(){
    call();
})
```

Nous pouvons utiliser cette méthode `finally()` pour nettoyer les choses après l'appel API. Il y a de nombreuses façons d'utiliser la méthode `finally()`.

## Comment Créer une Promesse

Nous savons comment consommer des promesses, mais qu'en est-il de la création de vos propres promesses ? Vous pouvez le faire en utilisant `new Promise()`.

Vous pourriez vous demander - pourquoi avons-nous besoin de nos propres promesses ? Premièrement, les promesses sont asynchrones par nature. Nous pouvons créer n'importe quelle tâche pour qu'elle soit asynchrone en créant nos propres promesses. Nous pouvons les gérer en utilisant les méthodes `then()` et `catch()` que nous avons apprises dans la section ci-dessus.

Une fois que vous savez comment créer des promesses, vous pouvez rendre n'importe quel morceau de code asynchrone. Ensuite, il ne bloquera pas l'exécution du code si l'autre code en cours d'exécution prend beaucoup de temps à se terminer.

Voyons comment cela fonctionne en utilisant un exemple :

```javascript
let lottery = new Promise(function(resolve, reject){
    console.log("La loterie est en cours");

    setTimeout(() => {
        if(Math.random() >= 0.5){
            resolve("Vous avez gagné !!!")
        }
        else{
            reject(new Error("Meilleure chance la prochaine fois"))
        }
    }, 5000);

})
```

Tout d'abord, nous avons créé une promesse en utilisant `new Promise()`. Elle aura une fonction avec deux arguments, `resolve` et `reject`.

Nous appellerons `resolve` lorsque notre tâche est réussie, et `reject` lorsque la tâche échoue. Nous utiliserons la terminologie de la loterie que j'ai utilisée pour expliquer le concept de promesses dans la section ci-dessus.

Disons que si `Math.random()` donne une valeur inférieure ou égale à 0,5, nous gagnerons la loterie. Sinon, nous perdrons la loterie. Si la condition n'est pas vraie, le code lance une nouvelle erreur pour une meilleure compréhension de l'erreur dans la console. Donc, nous pouvons lancer nos propres erreurs personnalisées à l'utilisateur pour une meilleure compréhension.

Dans l'exemple ci-dessus, si `Math.random()` est inférieur à 0,5, cela signifie que l'utilisateur a perdu la loterie. Donc, nous lançons notre erreur personnalisée `Meilleure chance la prochaine fois` pour que l'utilisateur comprenne qu'il a perdu la loterie.

Maintenant, nous allons essayer de consommer la promesse que nous avons créée.

```javascript
let lottery = new Promise(function(resolve, reject){
    console.log("La loterie est en cours");

    setTimeout(() => {    
        if(Math.random() >= 0.5){
            resolve("Vous avez gagné !!!")
        }
        else{
            reject(new Error("Meilleure chance la prochaine fois"))
        }   
    }, 5000);

})

lottery.then((response) =>{
    console.log(response);
}).catch((err) =>{
    console.log(err);
})
```

Nous consommons la promesse en utilisant la méthode `then()`. Elle imprimera la réponse que nous avons fournie dans `resolve()`. Si la promesse est rejetée, nous attraperons l'erreur dans la méthode `catch()`. L'erreur proviendra de l'argument `reject()` que nous avons mentionné dans notre propre promesse.

### Comment Consommer des Promesses en utilisant Async/Await

Consommer des promesses en utilisant la méthode then() peut parfois devenir désordonné. Nous avons donc une méthode alternative pour consommer des promesses appelée async/await.

Gardez simplement à l'esprit que async/await utilisera la méthode `then()` en arrière-plan pour consommer des promesses.

Pourquoi utiliser async/await si nous avons la méthode `then()` ? Nous utilisons async/await parce que c'est facile à utiliser. Si nous commençons à chaîner des méthodes aux promesses en utilisant la méthode `then()`, la chaîne sera très longue et deviendra complexe avec l'ajout de plusieurs méthodes then(). Donc async/await est plus simple.

Voici comment fonctionne async/await :

```javascript
const fetchAPI = async function(){
    const res = await fetch('https://cat-fact.herokuapp.com/facts')
    const data = await res.json()
    console.log(data);
}
fetchAPI()
console.log("PREMIER");
```

![Image](https://www.freecodecamp.org/news/content/images/2023/02/123123.png align="left")

Dans le code ci-dessus, nous appelons d'abord fetchAPI() pour voir le comportement asynchrone de la fonction. Ensuite, il enregistre "PREMIER". Selon JavaScript asynchrone, fetchAPI() devrait s'exécuter en arrière-plan et ne pas bloquer l'exécution du code. Par conséquent, "PREMIER" est enregistré, puis le résultat de fetchAPI est affiché.

Maintenant, si vous voulez gérer des tâches asynchrones dans vos fonctions, vous devez rendre cette fonction asynchrone en utilisant le mot-clé async avant la fonction. Partout où des promesses sont retournées, nous devons utiliser await avant pour consommer des promesses.

Maintenant, vous pourriez vous demander, comment devrions-nous gérer les erreurs ? Pour cela, nous pouvons utiliser try...catch() pour gérer les erreurs dans async/await.

# Gestion des Erreurs avec `try...catch()`

Nous pouvons utiliser `try...catch()` en JavaScript vanilla également. Mais il peut également nous aider à gérer les erreurs en JavaScript asynchrone avec async/await.

`try...catch()` est similaire à la méthode `catch()` dans `then()` en utilisant la méthode de chaînage `catch()`. Ici, nous allons essayer le code dans le bloc `try`. Si cela s'exécute avec succès, alors il n'y a pas de problème.

Mais si le code dans le bloc `try` a une erreur, nous pouvons l'attraper dans le bloc `catch`. Nous pouvons vérifier les erreurs dans le bloc try et lancer notre erreur personnalisée qui sera attrapée dans le bloc `catch`. Une fois que nous avons attrapé l'erreur dans le bloc `catch`, nous pouvons faire ce que nous voulons lorsque nous rencontrons une erreur.

Voyons comment cela fonctionne avec l'exemple de code que nous avons utilisé.

```javascript
const fetchAPI = async function(){
    try{
        const res = await fetch('https://cat-fact.herokuapp.com/fact')
        if(!res.ok){
            throw new Error("Erreur Personnalisée")
        }
        const data = await res.json()
        console.log(data);
    } catch(err){
        console.log(err);
    }
}


fetchAPI()
console.log("PREMIER");
```

Tout d'abord, nous enveloppons le code asynchrone dans un bloc `try`. Ensuite, dans le bloc `catch`, nous enregistrons l'erreur. Dans le bloc try, si `res.ok` est faux, nous lançons notre erreur personnalisée en utilisant `throw new Error` que `catch` obtiendra. Ensuite, nous l'enregistrons dans la console.

# Comment Retourner des Valeurs depuis des Fonctions Async

Jusqu'à présent, nous avons appris sur le code asynchrone, les méthodes `then()` et `catch()`, et la gestion du code asynchrone avec async/await. Mais que faire si nous voulons retourner une valeur d'une fonction async en utilisant async/await ?

Lorsque vous travaillez avec du code asynchrone, il est souvent nécessaire de retourner une valeur d'une fonction `async` afin que d'autres parties de votre programme puissent utiliser le résultat de l'opération asynchrone.

Par exemple, si vous faites une requête HTTP pour récupérer des données d'une API, vous voudrez retourner les données de réponse à la fonction appelante afin qu'elles puissent être traitées ou affichées à l'utilisateur.

Eh bien, nous pouvons le faire. Regardez l'exemple ci-dessous :

```javascript
const fetchAPI = async function(){
    try{
        const res = await fetch('https://cat-fact.herokuapp.com/facts')
        if(!res.ok){
            throw new Error("Erreur Personnalisée")
        }
        const data = await res.json()
        console.log(data);
        return "Terminé avec fetchAPI"
    } catch(err){
        console.log(err);
        throw new Error("Erreur Personnalisée")
    }
}


console.log(fetchAPI())
```

Si nous enregistrons fetchAPI, nous obtiendrons une promesse qui est remplie. Vous savez très bien comment gérer ces promesses. Nous allons le faire en utilisant la méthode `then()`.

```javascript
const fetchAPI = async function(){
    try{
        const res = await fetch('https://cat-fact.herokuapp.com/facts')
        if(!res.ok){
            throw new Error("Erreur Personnalisée")
        }
        const data = await res.json()
        console.log(data);
        return "Terminé avec fetchAPI"
    } catch(err){
        console.log(err);
        throw new Error("Erreur Personnalisée")
    }
}


fetchAPI().then((msg) =>{
    console.log(msg);
}).catch((err) =>{
    console.log(err);
})
```

Maintenant, lorsque nous exécutons notre programme, nous verrons notre message retourné du bloc `try` en utilisant async/await enregistré dans la console.

Mais que faire s'il y avait une erreur dans async/await ? La fetchAPI avec la méthode then() l'enregistrerait toujours et elle serait indéfinie.

Pour éviter cela dans le bloc catch, nous lançons à nouveau une nouvelle erreur et utilisons la méthode catch() pour attraper cette erreur après la méthode then().

Essayez de changer les méthodes `then()` et `catch()` avec async/await. Ce serait un bon exercice pour vous pour comprendre ce que vous avez appris dans cet article.

En JavaScript, il y a deux façons courantes de travailler avec des opérations asynchrones : le chaînage de méthodes `then/catch` et `async/await`. Les deux méthodes peuvent être utilisées pour gérer les promesses, qui sont des objets représentant l'achèvement éventuel (ou l'échec) d'une opération asynchrone.

Le chaînage de méthodes `then/catch` est une manière plus traditionnelle de gérer les opérations asynchrones, tandis que `async/await` est une syntaxe plus récente qui offre une alternative plus concise et plus facile à lire.

## Comment Exécuter des Promesses en Parallèle

Disons que nous voulons faire trois requêtes pour trois capitales de pays différents. Nous pouvons faire trois appels fetch différents, chacun attendant que celui au-dessus soit terminé.

```javascript
const fetchAPI = async function(country1,country2,country3){
    try{
        const res1 = await fetch(`https://restcountries.com/v3.1/name/${country1}`)
        const res2 = await fetch(`https://restcountries.com/v3.1/name/${country2}`)
        const res3 = await fetch(`https://restcountries.com/v3.1/name/${country3}`)
        
        
        const data1 = await res1.json()
        const data2 = await res2.json()
        const data3 = await res3.json()
        console.log(data1[0].capital[0]);
        console.log(data2[0].capital[0]);
        console.log(data3[0].capital[0]);
        return "Terminé avec fetchAPI"
    } catch(err){
        console.log(err);
        throw new Error("Erreur Personnalisée")
    }
}


fetchAPI("canada", "germany", "russia")
```

Dans le code ci-dessus, nous faisons trois appels fetch, puis nous les convertissons en json() et enregistrons leurs capitales.

Mais si vous inspectez et regardez dans l'onglet réseau, res2 attend que res1 soit terminé et res3 attend que res2 soit terminé.

Cela peut avoir un impact négatif sur les performances de notre application. Parce qu'une promesse qui attend qu'une autre promesse soit terminée peut avoir un impact négatif sur les performances du site web.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/321.png align="left")

Pour surmonter ce problème de performance, nous pouvons utiliser quelque chose appelé `**Promise.all**`. Il appellera trois requêtes fetch simultanément, ce qui réduira notre temps de récupération et améliorera les performances de notre application.

## Comment Utiliser Promise.all()

Avec l'aide de Promise.all(), nous pouvons exécuter plusieurs promesses en parallèle, ce qui améliorera les performances. Promise.all() prend un tableau en argument qui sont des promesses et les exécute en parallèle.

```javascript
let promise1 = new Promise((resolve) =>{
    setTimeout(() =>{
       resolve("Première Promesse")
    }, 2000)
})

let promise2 = Promise.resolve("Deuxième Promesse")

let returnedPromises = Promise.all([promise1,promise2]).then((res) =>{
    console.log(res);
})
```

Le résultat de l'utilisation de promise.all() est que les deux promesses s'exécutaient en parallèle.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/2121.png align="left")

# Conclusion

Après avoir lu ce tutoriel, j'espère que vous avez une meilleure compréhension de JavaScript asynchrone. N'hésitez pas à me contacter pour des discussions et des suggestions.

Vous pouvez me suivre sur :

* [Twitter](https://twitter.com/Kedar__98)
    
* [LinkedIn](https://www.linkedin.com/in/kedar-makode-9833321ab/?originalSubdomain=in)
    
* [Instagram](https://www.instagram.com/kedar_98/)