---
title: Tutoriel JavaScript Async/Await – Apprendre les Callbacks, les Promises et
  Async/Await en JS en fabriquant de la glace 🍧🍨🍦
subtitle: ''
author: Joy Shaheb
co_authors: []
series: null
date: '2021-06-02T14:45:18.000Z'
originalURL: https://freecodecamp.org/news/javascript-async-await-tutorial-learn-callbacks-promises-async-await-by-making-icecream
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/FCC-Thumbnail--3-.png
tags:
- name: async/await
  slug: asyncawait
- name: asynchronous programming
  slug: asynchronous-programming
- name: callbacks
  slug: callbacks
- name: JavaScript
  slug: javascript
- name: promises
  slug: promises
- name: Web Development
  slug: web-development
seo_title: Tutoriel JavaScript Async/Await – Apprendre les Callbacks, les Promises
  et Async/Await en JS en fabriquant de la glace 🍧🍨🍦
seo_desc: 'Today we''re going to build and run an ice cream shop and learn asynchronous
  JavaScript at the same time. Along the way, you''ll learn how to use:


  Callbacks

  Promises

  Async / Await



  Here''s what we''ll cover in this article:


  What is Asynchronous JavaSc...'
---

Aujourd'hui, nous allons créer et gérer une **boutique de glaces** et apprendre **JavaScript asynchrone** en même temps. En cours de route, vous apprendrez à utiliser :

* Les Callbacks
* Les Promises
* Async / Await

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/b1j935dg72g9u8zvh2oi.png)

# Voici ce que nous allons couvrir dans cet article :

* Qu'est-ce que JavaScript Asynchrone ?
* JavaScript Synthrone vs Asynchrone
* Comment fonctionnent les Callbacks en JavaScript
* Comment fonctionnent les Promises en JavaScript
* Comment fonctionne Async / Await en JavaScript

Alors, plongeons-nous !

## Vous pouvez également regarder ce tutoriel sur YouTube si vous le souhaitez :

%[https://youtu.be/n5ZtTO1ArWg]

# Qu'est-ce que JavaScript Asynchrone ?

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/7yd96tgxvuowqmfgcx6b.png)

Si vous voulez construire des projets efficacement, alors ce concept est pour vous.

La théorie de l'async JavaScript vous aide à décomposer de grands projets complexes en tâches plus petites.

Ensuite, vous pouvez utiliser l'une de ces trois techniques – **callbacks, promises ou Async/await** – pour exécuter ces petites tâches de manière à obtenir les meilleurs résultats.

Plongeons-nous !🎖️

# JavaScript Synthrone vs Asynchrone

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/arzbf1rc3pi4yi6u8wup.png)

## Qu'est-ce qu'un Système Synthrone ?

Dans un système synthrone, les tâches sont accomplies les unes après les autres.

Imaginez cela comme si vous n'aviez qu'une seule main pour accomplir 10 tâches. Vous devez donc compléter une tâche à la fois.

Regardez le GIF 👋 – une seule chose se passe à la fois ici :

![Système Synthrone](https://media.giphy.com/media/ICIS16DkE9qB9HVxtq/giphy.gif)

Vous verrez que tant que la première image n'est pas complètement chargée, la deuxième image ne commence pas à se charger.

Eh bien, JavaScript est par défaut Synthrone **[mono-thread]**. Pensez-y comme ceci – un thread signifie une main avec laquelle faire des choses.

## Qu'est-ce qu'un Système Asynchrone ?

Dans ce système, les tâches sont accomplies indépendamment.

Ici, imaginez que pour 10 tâches, vous avez 10 mains. Chaque main peut donc faire chaque tâche indépendamment et en même temps.

Regardez le GIF 👋 – vous pouvez voir que chaque image se charge en même temps.

![Système Asynchrone](https://media.giphy.com/media/MMDnmJnE7uhX6KtcKc/giphy.gif)

Encore une fois, toutes les images se chargent à leur propre rythme. Aucune d'entre elles n'attend les autres.

## Pour Résumer Synthrone vs Asynchrone JS :

Lorsque trois images sont dans un marathon, dans un :

* **Système Synthrone**, les trois images sont dans la même voie. L'une ne peut pas dépasser l'autre. La course se termine une par une. Si l'image numéro 2 s'arrête, l'image suivante s'arrête.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/w1r9y4ghhq0t8wjb1u9h.png)

* **Système Asynchrone**, les trois images sont dans des voies différentes. Elles termineront la course à leur propre rythme. Personne ne s'arrête pour personne :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ehknx5shc4orh32s0ktk.png)

## Exemples de Code Synthrone et Asynchrone

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/pzbnpcza9rbj8xgiby95.png)

Avant de commencer notre projet, regardons quelques exemples et clarifions tout doute.

### Exemple de Code Synthrone

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/5m6p1qy522lj3auvl5ty.png)

Pour tester un système synthrone, écrivez ce code en JavaScript :

```javascript
console.log(" Je ");

console.log(" mange ");

console.log(" de la glace ");

```

Voici le résultat dans la console : 👋

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/54izy7zyo52j2z6netls.png)

### Exemple de code asynchrone

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/y5d0o8unbe8c67qeqz0w.png)

Disons qu'il faut deux secondes pour manger de la glace. Maintenant, testons un système asynchrone. Écrivez le code ci-dessous en JavaScript.

**Note :** Ne vous inquiétez pas, nous discuterons de la fonction `setTimeout()` plus tard dans cet article.

```javascript
console.log("Je");

// Cela sera affiché après 2 secondes

setTimeout(()=>{
  console.log("mange");
},2000)

console.log("de la glace")

```

Et voici le résultat dans la console : 👋

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/o44c2t0r7bknkadoumgx.png)

Maintenant que vous connaissez la différence entre les opérations synthrones et asynchrones, construisons notre boutique de glaces.

## Comment configurer notre projet

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/2mzbtcnm67v2iys7cix7.png)

Pour ce projet, vous pouvez simplement ouvrir [Codepen.io](https://codepen.io/) et commencer à coder. Ou, vous pouvez le faire dans VS code ou l'éditeur de votre choix.

Ouvrez la section JavaScript, puis ouvrez votre console de développement. Nous écrivons notre code et verrons les résultats dans la console.

# Que sont les Callbacks en JavaScript ?

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/s5iloofqsv3lcdl4flsi.png)

Lorsque vous imbriquez une fonction à l'intérieur d'une autre fonction en tant qu'argument, cela s'appelle un callback.

Voici une illustration d'un callback :

![Image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/uz3pl56lmoc2pq7wzi2s.png)
_**Un exemple de callback**_

Ne vous inquiétez pas, nous verrons quelques exemples de callbacks dans une minute.

### Pourquoi utilisons-nous des callbacks ?

Lorsque nous effectuons une tâche complexe, nous décomposons cette tâche en étapes plus petites. Pour nous aider à établir une relation entre ces étapes selon le temps (optionnel) et l'ordre, nous utilisons des callbacks.

Regardez cet exemple :👋

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/o05q7ortgctx2oeyntfn.png)
_**Le graphique contient les étapes pour faire de la glace**_

Ce sont les petites étapes que vous devez suivre pour faire de la glace. Notez également que dans cet exemple, l'ordre des étapes et le timing sont cruciaux. Vous ne pouvez pas simplement couper les fruits et servir la glace.

En même temps, si une étape précédente n'est pas terminée, nous ne pouvons pas passer à l'étape suivante.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/2v1rn50smjul9arkneza.png)

Pour expliquer cela plus en détail, commençons notre entreprise de boutique de glaces.

## Mais attendez...

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/cq8exwor5aiciu2j6jwu.png)

La boutique aura deux parties :

* La réserve contiendra tous les ingrédients [Notre Backend]
* Nous produirons de la glace dans notre cuisine [Le frontend]

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/i69bws707m5rvsj34i9o.png)

## Stockez nos données

Maintenant, nous allons stocker nos ingrédients à l'intérieur d'un objet. Commençons !

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ihezrht8dgg9xn8lm2k9.png)

Vous pouvez stocker les ingrédients à l'intérieur d'objets comme ceci : 👋

```javascript
let stocks = {
    Fruits : ["strawberry", "grapes", "banana", "apple"]
 }

```

Nos autres ingrédients sont ici : 👋

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/6dcwr770l0ubupv0r2gj.png)

Vous pouvez stocker ces autres ingrédients dans des objets JavaScript comme ceci : 👋

```javascript
let stocks = {
    Fruits : ["strawberry", "grapes", "banana", "apple"],
    liquid : ["water", "ice"],
    holder : ["cone", "cup", "stick"],
    toppings : ["chocolate", "peanuts"],
 };

```

Toute l'entreprise dépend de ce qu'un client **commande**. Une fois que nous avons une commande, nous commençons la production et ensuite nous servons la glace. Nous allons donc créer deux fonctions ->

* `order`
* `production`

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/3bnzniiyamo0b9l7e806.png)

Voici comment tout cela fonctionne : 👋

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/r8h8ra9wor8cs3dgddpb.png)
_Obtenir la commande du client, récupérer les ingrédients, commencer la production, puis servir._

Créons nos fonctions. Nous utiliserons des fonctions fléchées ici :

```javascript
let order = () =>{};

let production = () =>{};

```

Maintenant, établissons une relation entre ces deux fonctions en utilisant un callback, comme ceci : 👋

```javascript
let order = (call_production) =>{

  call_production();
};

let production = () =>{};

```

### Faisons un petit test

Nous utiliserons la fonction `console.log()` pour effectuer des tests afin de clarifier tout doute que nous pourrions avoir concernant la manière dont nous avons établi la relation entre les deux fonctions.

```javascript
let order = (call_production) =>{

console.log("Commande passée. Veuillez appeler la production")

// la fonction 👋 est appelée
  call_production();
};

let production = () =>{

console.log("La production a commencé")

};

```

Pour exécuter le test, nous appellerons la fonction **`order`**. Et nous ajouterons la deuxième fonction nommée `production` comme argument.

```javascript
// nom 👋 de notre deuxième fonction
order(production);

```

Voici le résultat dans notre console 👋

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/u41ugdxxed1q8coz5hol.png)

## Faites une pause

Jusqu'à présent, tout va bien – faites une pause !

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/tnr74waq6noc0djln3qx.png)

## Effacez le console.log

Gardez ce code et supprimez tout [ne supprimez pas notre variable stocks]. Dans notre première fonction, passez un autre argument afin que nous puissions recevoir la commande [Nom du fruit] :

```javascript
// Fonction 1

let order = (fruit_name, call_production) =>{

  call_production();
};

// Fonction 2

let production = () =>{};


// Déclencheur 👋

order("", production);

```

Voici nos étapes, et le temps que chaque étape prendra pour s'exécuter.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/rphpp2lqjnk7f0tv5g3d.png)
_**Graphique contenant les étapes pour faire de la glace**_

Dans ce graphique, vous pouvez voir que l'étape 1 est de passer la commande, ce qui prend 2 secondes. Ensuite, l'étape 2 est de couper le fruit (2 secondes), l'étape 3 est d'ajouter de l'eau et de la glace (1 seconde), l'étape 4 est de démarrer la machine (1 seconde), l'étape 5 est de sélectionner le contenant (2 secondes), l'étape 6 est de sélectionner les garnitures (3 secondes) et l'étape 7, l'étape finale, est de servir la glace ce qui prend 2 secondes.

Pour établir le timing, la fonction `setTimeout()` est excellente car elle utilise également un callback en prenant une fonction comme argument.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/qwrg1taugyhvjnkx8xpp.png)
_**Syntaxe d'une fonction setTimeout()**_

Maintenant, sélectionnons notre fruit et utilisons cette fonction :

```javascript
// 1ère Fonction

let order = (fruit_name, call_production) =>{

  setTimeout(function(){

    console.log(`${stocks.Fruits[fruit_name]} was selected`)

// Commande passée. Appeler la production pour démarrer
   call_production();
  },2000)
};

// 2ème Fonction

let production = () =>{
  // vide pour l'instant
};

// Déclencheur 👋
order(0, production);

```

Et voici le résultat dans la console : 👋

**Notez** que le résultat s'affiche après 2 secondes.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/edwji5vauypoezj3bxdk.png)

Si vous vous demandez comment nous avons choisi la fraise dans notre variable de stock, voici le code avec le format 👋

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ia38z3x6b96xpq3aid91.png)

Ne supprimez rien. Maintenant, nous allons commencer à écrire notre fonction de production avec le code suivant.
👋 Nous utiliserons des fonctions fléchées :

```javascript
let production = () =>{

  setTimeout(()=>{
    console.log("production has started")
  },0000)

};

```

Et voici le résultat 👋

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/5yskzvg7rezo2sg4lklq.png)

Nous allons imbriquer une autre fonction `setTimeout` dans notre fonction `setTimeout` existante pour couper le fruit. Comme ceci : 👋

```javascript
let production = () =>{
  
  setTimeout(()=>{
    console.log("production has started")


    setTimeout(()=>{
      console.log("The fruit has been chopped")
    },2000)


  },0000)
};

```

Et voici le résultat 👋

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/4659l1mua0rv40rwyem7.png)

Si vous vous souvenez, voici nos étapes :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/rphpp2lqjnk7f0tv5g3d.png)
_**Graphique contenant les étapes pour faire de la glace**_

Complétons notre production de glace en imbriquant une fonction à l'intérieur d'une autre fonction – cela s'appelle également un callback, vous vous souvenez ?

```javascript
let production = () =>{

  setTimeout(()=>{
    console.log("production has started")
    setTimeout(()=>{
      console.log("The fruit has been chopped")
      setTimeout(()=>{
        console.log(`${stocks.liquid[0]} and ${stocks.liquid[1]} Added`)
        setTimeout(()=>{
          console.log("start the machine")
          setTimeout(()=>{
            console.log(`Ice cream placed on ${stocks.holder[1]}`)
            setTimeout(()=>{
              console.log(`${stocks.toppings[0]} as toppings`)
              setTimeout(()=>{
                console.log("serve Ice cream")
              },2000)
            },3000)
          },2000)
        },1000)
      },1000)
    },2000)
  },0000)

};

```

Et voici le résultat dans la console 👋

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/5mq9bg6fqrc8apj7nu7b.png)

Vous vous sentez confus ?

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/man5l5pwavp9prio1wc0.png)

Cela s'appelle l'enfer des callbacks. Cela ressemble à quelque chose comme ceci (vous vous souvenez de ce code juste au-dessus ?) : 👋

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/d5rk7f8d920jzn22smjh.png)
_**Illustration de l'enfer des callbacks**_

Quelle est la solution à cela ?

# Comment utiliser les Promises pour échapper à l'enfer des callbacks

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/x3neys1hxsrifgg5qm6x.png)

Les Promises ont été inventées pour résoudre le problème de l'enfer des callbacks et pour mieux gérer nos tâches.

## Faites une pause

Mais d'abord, faites une pause !

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/bwfvel7kvm422gqvj0os.png)

Voici à quoi ressemble une promise :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/7qo1zheuin2825osozvc.png)
_**illustration du format d'une promise**_

Décortiquons les promises ensemble.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/gozy5r1nfubzeq5t5t25.png)

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ezi9ogz0ergprgkmu68a.png)
_**Une illustration de la vie d'une promise**_

Comme le montrent les graphiques ci-dessus, une promise a trois états :

* **En attente (Pending)** : C'est l'étape initiale. Rien ne se passe ici. Pensez à cela comme si votre client prenait son temps pour vous donner une commande. Mais ils n'ont encore rien commandé.
* **Résolue (Resolved)** : Cela signifie que votre client a reçu sa nourriture et est heureux.
* **Rejetée (Rejected)** : Cela signifie que votre client n'a pas reçu sa commande et a quitté le restaurant.

Adoptons les promises pour notre étude de cas de production de glace.

## Mais attendez...

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/634b6oyglkyoccsvr8l7.png)

Nous devons d'abord comprendre quatre autres choses ->

* Relation entre le temps et le travail
* Chaînage des promises
* Gestion des erreurs
* Le gestionnaire `.finally`

Commençons notre boutique de glaces et comprenons chacun de ces concepts un par un en prenant des petits pas.

## Relation entre le temps et le travail

Si vous vous souvenez, voici nos étapes et le temps que chacune prend pour faire de la glace"

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/rphpp2lqjnk7f0tv5g3d.png)
_**Graphique contenant les étapes pour faire de la glace**_

Pour que cela se produise, créons une variable en JavaScript : 👋

```javascript
let is_shop_open = true;

```

Maintenant, créez une fonction nommée `order` et passez deux arguments nommés `time, work` :

```javascript
let order = ( time, work ) =>{

  }

```

Maintenant, nous allons faire une promise à notre client, "Nous vous servirons de la glace" Comme ceci ->

```javascript
let order = ( time, work ) =>{

  return new Promise( ( resolve, reject )=>{ } )

  }

```

Notre promise a 2 parties :

* Résolue [glace livrée]
* Rejetée [le client n'a pas reçu de glace]

```javascript
let order = ( time, work ) => {

  return new Promise( ( resolve, reject )=>{

    if( is_shop_open ){

      resolve( )

    }

    else{

      reject( console.log("Notre boutique est fermée") )

    }

  })
}

```

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/3wik2xel68yue93yapm6.png)

Ajoutons les facteurs temps et travail à l'intérieur de notre promise en utilisant une fonction `setTimeout()` à l'intérieur de notre instruction `if`. Suivez-moi 👋

**Note :** Dans la vraie vie, vous pouvez également éviter le facteur temps. Cela dépend entièrement de la nature de votre travail.

```javascript
let order = ( time, work ) => {

  return new Promise( ( resolve, reject )=>{

    if( is_shop_open ){

      setTimeout(()=>{

       // le travail 👋 est en train d'être fait ici
        resolve( work() )

// Définir 👋 le temps ici pour 1 travail
       }, time)

    }

    else{
      reject( console.log("Notre boutique est fermée") )
    }

  })
}

```

Maintenant, nous allons utiliser notre fonction nouvellement créée pour commencer la production de glace.

```javascript
// Définir 👋 le temps ici
order( 2000, ()=>console.log(`${stocks.Fruits[0]} was selected`))
//    passer une ⚪ fonction ici pour commencer à travailler

```

Le résultat 👋 après 2 secondes ressemble à ceci :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/erzjup8wt505j502e73n.png)

Bon travail !

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/8taajvjy6pfq35hu90nq.png)

## Chaînage des Promises

Dans cette méthode, nous définissons ce que nous devons faire lorsque la première tâche est terminée en utilisant le gestionnaire `.then`. Cela ressemble à quelque chose comme ceci 👋

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/l27ytifkoedl22kc97lh.png)
_**Illustration du chaînage des promises en utilisant le gestionnaire .then**_

Le gestionnaire .then retourne une promise lorsque notre promise originale est résolue.

#### Voici un exemple :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/1qpeewo19qbhzj47goos.png)

Permettez-moi de simplifier : c'est similaire à donner des instructions à quelqu'un. Vous dites à quelqu'un de "D'abord fais ceci, puis fais cela, puis cette autre chose, puis.., puis.., puis..." et ainsi de suite.

* La première tâche est notre promise originale.
* Le reste des tâches retourne notre promise une fois qu'un petit morceau de travail est terminé

Mettons cela en œuvre dans notre projet. En bas de votre code, écrivez les lignes suivantes. 👋

**Note :** n'oubliez pas d'écrire le mot `return` à l'intérieur de votre gestionnaire `.then`. Sinon, cela ne fonctionnera pas correctement. Si vous êtes curieux, essayez de supprimer le return une fois que nous avons terminé les étapes :

```javascript
order(2000,()=>console.log(`${stocks.Fruits[0]} was selected`))

.then(()=>{
  return order(0000,()=>console.log('production has started'))
})

```

Et voici le résultat : 👋

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/qhhjaakbi6zshxhi6afy.png)

En utilisant le même système, terminons notre projet :👋

```javascript
// étape 1
order(2000,()=>console.log(`${stocks.Fruits[0]} was selected`))

// étape 2
.then(()=>{
  return order(0000,()=>console.log('production has started'))
})

// étape 3
.then(()=>{
  return order(2000, ()=>console.log("Fruit has been chopped"))
})

// étape 4
.then(()=>{
  return order(1000, ()=>console.log(`${stocks.liquid[0]} and ${stocks.liquid[1]} added`))
})

// étape 5
.then(()=>{
  return order(1000, ()=>console.log("start the machine"))
})

// étape 6
.then(()=>{
  return order(2000, ()=>console.log(`ice cream placed on ${stocks.holder[1]}`))
})

// étape 7
.then(()=>{
  return order(3000, ()=>console.log(`${stocks.toppings[0]} as toppings`))
})

// Étape 8
.then(()=>{
  return order(2000, ()=>console.log("Serve Ice Cream"))
})

```

Voici le résultat : 👋

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/y0d0f4ys83ctnevkbgxs.png)

## Gestion des erreurs

Nous avons besoin d'un moyen de gérer les erreurs lorsque quelque chose ne va pas. Mais d'abord, nous devons comprendre le cycle de la promise :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/jlm7zwonbxszeaccyohv.png)

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/z2ajcu52rxzwq64g81vp.png)
_**Une illustration de la vie d'une promise**_

Pour attraper nos erreurs, changeons notre variable en false.

```javascript
let is_shop_open = false;

```

Ce qui signifie que notre boutique est fermée. Nous ne vendons plus de glace à nos clients.

Pour gérer cela, nous utilisons le gestionnaire `.catch`. Tout comme `.then`, il retourne également une promise, mais seulement lorsque notre promise originale est rejetée.

Un petit rappel ici :

* `.then` fonctionne lorsqu'une promise est résolue
* `.catch` fonctionne lorsqu'une promise est rejetée

Descendez tout en bas et écrivez le code suivant :👋

Rappelez-vous simplement qu'il ne doit y avoir rien entre votre gestionnaire `.then` précédent et le gestionnaire `.catch`.

```javascript
.catch(()=>{
  console.log("Customer left")
})

```

Voici le résultat :👋

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/lot6engklu29y05q8xyr.png)

Quelques points à noter sur ce code :

* Le 1er message provient de la partie `reject()` de notre promise
* Le 2ème message provient du gestionnaire `.catch`

## Comment utiliser le gestionnaire .finally()

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/gdq3i0agj4volq46ycue.png)

Il y a quelque chose appelé le gestionnaire `finally` qui fonctionne indépendamment du fait que notre promise ait été résolue ou rejetée.

**Par exemple :** que nous servions aucun client ou 100 clients, notre boutique fermera à la fin de la journée

Si vous êtes curieux de tester cela, venez tout en bas et écrivez ce code : 👋

```javascript
.finally(()=>{
  console.log("end of day")
})

```

Le résultat :👋

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/t2j3jf2uofip1d6y2rtt.png)

Tout le monde, veuillez accueillir Async / Await~

# Comment fonctionne Async / Await en JavaScript ?

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ra7483f90b69pjl2cbae.png)

Cela est censé être la meilleure façon d'écrire des promises et cela nous aide à garder notre code simple et propre.

Tout ce que vous avez à faire est d'écrire le mot `async` avant toute fonction régulière et elle devient une promise.

## Mais d'abord, faites une pause

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/4vujyfxz7dg41jhjtcrx.png)

Jetons un coup d'œil :👋

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/17f08ygj1odk28hgl9eq.png)

## Promises vs Async/Await en JavaScript

Avant async/await, pour faire une promise nous écrivions ceci :

```javascript
function order(){
   return new Promise( (resolve, reject) =>{

    // Écrire le code ici
   } )
}

```

Maintenant, en utilisant async/await, nous en écrivons une comme ceci :

```javascript
//
async function order() {
    // Écrire le code ici
 }

```

## Mais attendez......

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/t1pjzw6zl0h21tyyh9u3.png)

Vous devez comprendre ->

* Comment utiliser les mots-clés `try` et `catch`
* Comment utiliser le mot-clé await

## Comment utiliser les mots-clés Try et Catch

Nous utilisons le mot-clé `try` pour exécuter notre code tandis que nous utilisons `catch` pour attraper nos erreurs. C'est le même concept que nous avons vu lorsque nous avons regardé les promises.

Regardons une comparaison. Nous verrons une petite démonstration du format, puis nous commencerons à coder.

### Promises en JS -> resolve ou reject

Nous avons utilisé resolve et reject dans les promises comme ceci :

```javascript
function kitchen(){

  return new Promise ((resolve, reject)=>{
    if(true){
       resolve("promise is fulfilled")
    }

    else{
        reject("error caught here")
    }
  })
}

kitchen()  // exécuter le code
.then()    // étape suivante
.then()    // étape suivante
.catch()   // erreur attrapée ici
.finally() // fin de la promise [optionnel]

```

### Async / Await en JS -> try, catch

Lorsque nous utilisons async/await, nous utilisons ce format :

```javascript
//
async function kitchen(){

   try{
// Créons un faux problème      
      await abc;
   }

   catch(error){
      console.log("abc does not exist", error)
   }

   finally{
      console.log("Runs code anyways")
   }
}

kitchen()  // exécuter le code

```

Ne paniquez pas, nous discuterons du mot-clé `await` ensuite.

Maintenant, espérons que vous comprenez la différence entre les promises et Async / Await.

## Comment utiliser le mot-clé Await de JavaScript

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/fry577xha7313ead96xy.png)

Le mot-clé `await` fait attendre JavaScript jusqu'à ce qu'une promise soit réglée et retourne son résultat.

### Comment utiliser le mot-clé await en JavaScript

Retourons à notre boutique de glaces. Nous ne savons pas quelle garniture un client pourrait préférer, chocolat ou cacahuètes. Nous devons donc arrêter notre machine et aller demander à notre client ce qu'il aimerait sur sa glace.

Remarquez ici que seule notre cuisine est arrêtée, mais notre personnel à l'extérieur de la cuisine continuera à faire des choses comme :

* faire la vaisselle
* nettoyer les tables
* prendre les commandes, et ainsi de suite.

## Un exemple de code avec le mot-clé Await

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/8r5w5aapofalnq882wat.png)

Créons une petite promise pour demander quelle garniture utiliser. Le processus prend trois secondes.

```javascript
function toppings_choice (){
  return new Promise((resolve,reject)=>{
    setTimeout(()=>{

      resolve( console.log("which topping would you love?") )

    },3000)
  })
}

```

Maintenant, créons notre fonction kitchen avec le mot-clé async d'abord.

```javascript
async function kitchen(){

  console.log("A")
  console.log("B")
  console.log("C")
  
  await toppings_choice()
  
  console.log("D")
  console.log("E")

}

// Déclencher la fonction

kitchen();

```

Ajoutons d'autres tâches en dessous de l'appel `kitchen()`.

```javascript
console.log("doing the dishes")
console.log("cleaning the tables")
console.log("taking orders")

```

Et voici le résultat :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/y0dr669gewtrrd5fd86p.png)

Nous sortons littéralement de notre cuisine pour demander à notre client, "quel est votre choix de garniture ?" En attendant, d'autres choses continuent à être faites.

Une fois que nous avons leur choix de garniture, nous entrons dans la cuisine et terminons le travail.

### Petite note

Lorsque vous utilisez Async/Await, vous pouvez également utiliser les gestionnaires `.then`, `.catch` et `.finally` qui sont une partie centrale des promises.

### Ouvrons à nouveau notre boutique de glaces

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/vzw8gp721oecwo2b3l6s.png)

Nous allons créer deux fonctions ->

* `kitchen` : pour faire de la glace
* `time` : pour assigner la quantité de temps que chaque petite tâche prendra.

Commençons ! Créez d'abord la fonction time :

```javascript
let is_shop_open = true;

function time(ms) {

   return new Promise( (resolve, reject) => {

      if(is_shop_open){
         setTimeout(resolve,ms);
      }

      else{
         reject(console.log("Shop is closed"))
      }
    });
}


```

Maintenant, créons notre cuisine :

```javascript
async function kitchen(){
   try{

     // instruction ici
   }

   catch(error){
    // gestion des erreurs ici
   }
}

// Déclencheur
kitchen();

```

Donnons de petites instructions et testons si notre fonction kitchen fonctionne ou non :

```javascript
async function kitchen(){
   try{

// temps pris pour effectuer cette 1 tâche
     await time(2000)
     console.log(`${stocks.Fruits[0]} was selected`)
   }

   catch(error){
     console.log("Customer left", error)
   }

   finally{
      console.log("Day ended, shop closed")
    }
}

// Déclencheur
kitchen();

```

Le résultat ressemble à ceci lorsque la boutique est ouverte : 👋

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/lptup827qau72e83deuv.png)

Le résultat ressemble à ceci lorsque la boutique est fermée : 👋

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/r8pjz1qlw58ap8pq7crz.png)

Jusqu'à présent, tout va bien.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/cnkgk63x51wth2byxzfe.png)

Complétons notre projet.

Voici la liste de nos tâches à nouveau : 👋

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/7wthn0jr5vw7vb02e4qg.png)
_**Graphique contenant les étapes pour faire de la glace**_

Tout d'abord, ouvrons notre boutique

```javascript
let is_shop_open = true;

```

Maintenant, écrivez les étapes à l'intérieur de notre fonction `kitchen()` : 👋

```javascript
async function kitchen(){
    try{
	await time(2000)
	console.log(`${stocks.Fruits[0]} was selected`)

	await time(0000)
	console.log("production has started")

	await time(2000)
	console.log("fruit has been chopped")

	await time(1000)
	console.log(`${stocks.liquid[0]} and ${stocks.liquid[1]} added`)

	await time(1000)
	console.log("start the machine")

	await time(2000)
	console.log(`ice cream placed on ${stocks.holder[1]}`)

	await time(3000)
	console.log(`${stocks.toppings[0]} as toppings`)

	await time(2000)
	console.log("Serve Ice Cream")
    }

    catch(error){
	 console.log("customer left")
    }
}

```

Et voici le résultat : 👋

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/qs9yccq9209u7m9lquju.png)

# Conclusion

Félicitations pour avoir lu jusqu'à la fin ! Dans cet article, vous avez appris : 

* La différence entre les systèmes synthrones et asynchrones
* Les mécanismes de JavaScript asynchrone en utilisant 3 techniques (callbacks, promises et Async/Await)

Voici votre médaille pour avoir lu jusqu'à la fin. ❤️

### Les suggestions et critiques sont grandement appréciées ❤️

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/usxsz1lstuwry3jlly4d.png)

**YouTube [/ Joy Shaheb](https://youtube.com/c/joyshaheb)**

**LinkedIn [/ JoyShaheb](https://www.linkedin.com/in/joyshaheb/)**

**Twitter [/ JoyShaheb](https://twitter.com/JoyShaheb)**

**Instagram [/ JoyShaheb](https://www.instagram.com/joyshaheb/)**

# Crédits

* [Collection de toutes les images utilisées](https://www.freepik.com/user/collections/promises-article/2046500)
* [Licornes](https://www.flaticon.com/packs/unicorn-4), [avatar de chaton](https://www.flaticon.com/packs/kitty-avatars-3)
* [chat tabby](https://www.pexels.com/photo/brown-tabby-cat-with-slice-of-loaf-bread-on-head-4587955/), [Femme Astrologue](https://www.pexels.com/photo/young-female-astrologist-predicting-future-with-shining-ball-6658693/), [fille tenant une fleur](https://www.pexels.com/photo/woman-in-white-dress-holding-white-flower-bouquet-3981511/)
* [Émotions des personnages](https://www.vecteezy.com/vector-art/180695-people-mind-emotion-character-cartoon-vector-illustration)