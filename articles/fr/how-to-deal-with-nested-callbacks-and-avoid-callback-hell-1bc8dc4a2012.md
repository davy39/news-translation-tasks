---
title: Comment gérer les callbacks imbriqués et éviter l'enfer des callbacks
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2019-05-23T15:22:38.000Z'
originalURL: https://freecodecamp.org/news/how-to-deal-with-nested-callbacks-and-avoid-callback-hell-1bc8dc4a2012
coverImage: https://cdn-media-1.freecodecamp.org/images/1*csqpgoE3UUyh-aUsqycOfw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment gérer les callbacks imbriqués et éviter l'enfer des callbacks
seo_desc: 'JavaScript is a strange language. Once in a while, you have to deal with
  a callback that’s in another callback that’s in yet another callback.

  People affectionately call this pattern the callback hell.

  It kinda looks like this:

  firstFunction(args, fu...'
---

JavaScript est un langage étrange. De temps en temps, vous devez gérer un callback qui est dans un autre callback qui est dans un autre callback.

Les gens appellent affectueusement ce schéma l'_enfer des callbacks_.

Cela ressemble un peu à ceci :

```javascript
firstFunction(args, function() {
  secondFunction(args, function() {
    thirdFunction(args, function() {
      // Et ainsi de suite…
    });
  });
});
```

C'est JavaScript pour vous. C'est déroutant de voir des callbacks imbriqués, mais je ne pense pas que ce soit un "enfer". L'"enfer" peut être gérable si vous savez quoi en faire.

### À propos des callbacks

Je suppose que vous savez ce que sont les callbacks si vous lisez cet article. Si ce n'est pas le cas, veuillez lire [cet article](https://zellwk.com/blog/callbacks/) pour une introduction aux callbacks avant de continuer. Nous y parlons de ce que sont les callbacks et pourquoi vous les utilisez en JavaScript.

### Solutions à l'enfer des callbacks

Il existe quatre solutions à l'enfer des callbacks :

1. Écrire des commentaires
2. Diviser les fonctions en fonctions plus petites
3. Utiliser les Promesses
4. Utiliser Async/await

Avant de plonger dans les solutions, construisons ensemble un enfer de callbacks. Pourquoi ? Parce qu'il est trop abstrait de voir `firstFunction`, `secondFunction`, et `thirdFunction`. Nous voulons le rendre concret.

### Construire un enfer de callbacks

Imaginons que nous essayons de faire un burger. Pour faire un burger, nous devons suivre les étapes suivantes :

1. Obtenir les ingrédients (nous allons supposer que c'est un burger au bœuf)
2. Cuire le bœuf
3. Obtenir les petits pains pour burger
4. Mettre le bœuf cuit entre les petits pains
5. Servir le burger

Si ces étapes sont synchrones, vous aurez une fonction qui ressemble à ceci :

```javascript
const makeBurger = () => {
  const beef = getBeef();
  const patty = cookBeef(beef);
  const buns = getBuns();
  const burger = putBeefBetweenBuns(buns, beef);
  return burger;
};

const burger = makeBurger();
serve(burger);
```

Cependant, dans notre scénario, disons que nous ne pouvons pas faire le burger nous-mêmes. Nous devons instruire un assistant sur les étapes à suivre pour faire le burger. Après avoir instruit l'assistant, nous devons _ATTENDRE_ que l'assistant termine avant de commencer l'étape suivante.

Si nous voulons attendre quelque chose en JavaScript, nous devons utiliser un callback. Pour faire le burger, nous devons d'abord obtenir le bœuf. Nous ne pouvons cuire le bœuf qu'après l'avoir obtenu.

```javascript
const makeBurger = () => {
  getBeef(function(beef) {
    // Nous ne pouvons cuire le bœuf qu'après l'avoir obtenu.
  });
};
```

Pour cuire le bœuf, nous devons passer `beef` dans la fonction `cookBeef`. Sinon, il n'y a rien à cuire ! Ensuite, nous devons attendre que le bœuf soit cuit.

Une fois le bœuf cuit, nous obtenons les petits pains.

```javascript
const makeBurger = () => {
  getBeef(function(beef) {
    cookBeef(beef, function(cookedBeef) {
      getBuns(function(buns) {
        // Mettre le steak dans le petit pain
      });
    });
  });
};
```

Après avoir obtenu les petits pains, nous devons mettre le steak entre les petits pains. C'est là que le burger se forme.

```javascript
const makeBurger = () => {
  getBeef(function(beef) {
    cookBeef(beef, function(cookedBeef) {
      getBuns(function(buns) {
        putBeefBetweenBuns(buns, beef, function(burger) {
            // Servir le burger
        });
      });
    });
  });
};
```

Enfin, nous pouvons servir le burger ! Mais nous ne pouvons pas retourner `burger` de `makeBurger` parce que c'est asynchrone. Nous devons accepter un callback pour servir le burger.

```javascript
const makeBurger = nextStep => {
  getBeef(function (beef) {
    cookBeef(beef, function (cookedBeef) {
      getBuns(function (buns) {
        putBeefBetweenBuns(buns, beef, function(burger) {
          nextStep(burger)
        })
      })
    })
  })
}

// Faire et servir le burger
makeBurger(function (burger) => {
  serve(burger)
})
```

(J'ai eu du plaisir à créer cet exemple d'enfer de callbacks 😄).

### Première solution à l'enfer des callbacks : Écrire des commentaires

L'enfer des callbacks `makeBurger` est simple à comprendre. Nous pouvons le lire. Il est juste… pas très joli.

Si vous lisez `makeBurger` pour la première fois, vous pourriez penser "Pourquoi diable avons-nous besoin de tant de callbacks pour faire un burger ? Cela n'a pas de sens !".

Dans un tel cas, vous voudriez laisser des commentaires pour expliquer votre code.

```javascript
// Prépare un burger
// makeBurger contient quatre étapes :
//   1. Obtenir le bœuf
//   2. Cuire le bœuf
//   3. Obtenir les petits pains pour le burger
//   4. Mettre le bœuf cuit entre les petits pains
//   5. Servir le burger (à partir du callback)
// Nous utilisons des callbacks ici parce que chaque étape est asynchrone.
//   Nous devons attendre que l'assistant termine une étape
//   avant de pouvoir commencer l'étape suivante

const makeBurger = nextStep => {
  getBeef(function(beef) {
    cookBeef(beef, function(cookedBeef) {
      getBuns(function(buns) {
        putBeefBetweenBuns(buns, beef, function(burger) {
          nextStep(burger);
        });
      });
    });
  });
};
```

Maintenant, au lieu de penser "wtf ?!" lorsque vous voyez l'enfer des callbacks, vous comprenez pourquoi il doit être écrit de cette manière.

### Deuxième solution à l'enfer des callbacks : Diviser les callbacks en différentes fonctions

Notre exemple d'enfer de callbacks est déjà un exemple de cela. Laissez-moi vous montrer le code impératif étape par étape et vous verrez pourquoi.

Pour `getBeef`, notre premier callback, nous devons aller au réfrigérateur pour obtenir le bœuf. Il y a deux réfrigérateurs dans la cuisine. Nous devons aller au bon réfrigérateur.

```javascript
const getBeef = nextStep => {
  const fridge = leftFright;
  const beef = getBeefFromFridge(fridge);
  nextStep(beef);
};
```

Pour cuire le bœuf, nous devons mettre le bœuf dans un four ; régler le four à 200 degrés, et attendre vingt minutes.

```javascript
const cookBeef = (beef, nextStep) => {
  const workInProgress = putBeefinOven(beef);
  setTimeout(function() {
    nextStep(workInProgress);
  }, 1000 * 60 * 20);
};
```

Maintenant, imaginez si vous devez écrire chacune de ces étapes dans `makeBurger`… vous vous évanouiriez probablement à cause de la quantité de code !

Pour un exemple concret sur la division des callbacks en fonctions plus petites, vous pouvez lire [cette petite section](https://zellwk.com/blog/callbacks#callback-hell) dans mon article sur les callbacks.

### Troisième solution à l'enfer des callbacks : Utiliser les promesses

Je vais supposer que vous savez ce que sont les promesses. Si ce n'est pas le cas, veuillez [lire cet article](https://zellwk.com/blog/js-promises/).

Les promesses peuvent rendre l'enfer des callbacks beaucoup plus facile à gérer. Au lieu du code imbriqué que vous voyez ci-dessus, vous aurez ceci :

```javascript
const makeBurger = () => {
  return getBeef()
    .then(beef => cookBeef(beef))
    .then(cookedBeef => getBuns(beef))
    .then(bunsAndBeef => putBeefBetweenBuns(bunsAndBeef));
};

// Faire et servir le burger
makeBurger().then(burger => serve(burger));
```

Si vous profitez du style à un seul argument avec les promesses, vous pouvez ajuster ce qui précède à ceci :

```javascript
const makeBurger = () => {
  return getBeef()
    .then(cookBeef)
    .then(getBuns)
    .then(putBeefBetweenBuns);
};

// Faire et servir le burger
makeBurger().then(serve);
```

Beaucoup plus facile à lire et à gérer.

Mais la question est de savoir comment convertir le code basé sur les callbacks en code basé sur les promesses.

#### Conversion des callbacks en promesses

Pour convertir les callbacks en promesses, nous devons créer une nouvelle promesse pour chaque callback. Nous pouvons `résoudre` la promesse lorsque le callback est réussi. Ou nous pouvons `rejeter` la promesse si le callback échoue.

```javascript
const getBeefPromise = _ => {
  const fridge = leftFright;
  const beef = getBeefFromFridge(fridge);
  
  return new Promise((resolve, reject) => {
    if (beef) {
      resolve(beef);
    } else {
      reject(new Error("Plus de bœuf !"));
    }
  });
};

const cookBeefPromise = beef => {
  const workInProgress = putBeefinOven(beef);
  
  return new Promise((resolve, reject) => {
    setTimeout(function() {
      resolve(workInProgress);
    }, 1000 * 60 * 20);
  });
};
```

En pratique, les callbacks seraient probablement déjà écrits pour vous. Si vous utilisez Node, chaque fonction qui contient un callback aura la même syntaxe :

1. Le callback serait le dernier argument
2. Le callback aura toujours deux arguments. Et ces arguments sont dans le même ordre. (Erreur en premier, suivi de ce qui vous intéresse).

```javascript
// La fonction qui est définie pour vous
const functionName = (arg1, arg2, callback) => {
  // Faire des choses ici
  callback(err, stuff);
};

// Comment vous utilisez la fonction
functionName(arg1, arg2, (err, stuff) => {
  if (err) {
  console.error(err);
  }
  // Faire des choses
});
```

Si votre callback a la même syntaxe, vous pouvez utiliser des bibliothèques comme [ES6 Promisify](https://www.npmjs.com/package/es6-promisify) ou [Denodeify](https://www.npmjs.com/package/denodeify) (de-node-ify) qui convertissent ce callback en une promesse. Si vous utilisez Node v8.0 et supérieur, vous pouvez utiliser [util.promisify](https://nodejs.org/dist/latest-v8.x/docs/api/util.html#util_util_promisify_original).

Les trois méthodes fonctionnent. Vous pouvez choisir n'importe quelle bibliothèque avec laquelle travailler. Il existe des nuances légères entre chaque méthode, cependant. Je vous laisse vérifier leur documentation pour les instructions.

### Quatrième solution à l'enfer des callbacks : Utiliser les fonctions asynchrones

Pour utiliser les fonctions asynchrones, vous devez d'abord connaître deux choses :

1. Comment convertir les callbacks en promesses (lire ci-dessus)
2. Comment utiliser les fonctions asynchrones ([lire ceci](https://zellwk.com/blog/async-await) si vous avez besoin d'aide).

Avec les fonctions asynchrones, vous pouvez écrire `makeBurger` comme si c'était synchrone à nouveau !

```javascript
const makeBurger = async () => {
  const beef = await getBeef();
  const cookedBeef = await cookBeef(beef);
  const buns = await getBuns();
  const burger = await putBeefBetweenBuns(cookedBeef, buns);
  return burger;
};

// Faire et servir le burger
makeBurger().then(serve);
```

Il y a une amélioration que nous pouvons apporter à `makeBurger` ici. Vous pouvez probablement obtenir deux assistants pour `getBuns` et `getBeef` en même temps. Cela signifie que vous pouvez les `await` tous les deux avec `Promise.all`.

```javascript
const makeBurger = async () => {
  const [beef, buns] = await Promise.all(getBeef, getBuns);
  const cookedBeef = await cookBeef(beef);
  const burger = await putBeefBetweenBuns(cookedBeef, buns);
  return burger;
};

// Faire et servir le burger
makeBurger().then(serve);
```

(Note : Vous pouvez faire la même chose avec les Promesses… mais la syntaxe n'est pas aussi agréable et claire que les fonctions async/await).

### Conclusion

L'enfer des callbacks n'est pas aussi infernal que vous le pensez. Il existe quatre moyens faciles de gérer l'enfer des callbacks :

1. Écrire des commentaires
2. Diviser les fonctions en fonctions plus petites
3. Utiliser les Promesses
4. Utiliser Async/await

Cet article a été initialement publié sur [mon blog](https://zellwk.com/blog/nested-callbacks).  
Inscrivez-vous à ma [newsletter](https://zellwk.com/) si vous voulez plus d'articles pour vous aider à devenir un meilleur développeur frontend.