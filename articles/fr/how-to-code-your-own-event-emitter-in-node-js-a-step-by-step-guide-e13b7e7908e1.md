---
title: 'Comment coder votre propre émetteur d''événements en Node.js : un guide étape
  par étape'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-12T22:27:11.000Z'
originalURL: https://freecodecamp.org/news/how-to-code-your-own-event-emitter-in-node-js-a-step-by-step-guide-e13b7e7908e1
coverImage: https://cdn-media-1.freecodecamp.org/images/0*R0F_SNqsLvxWG99J
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: 'Comment coder votre propre émetteur d''événements en Node.js : un guide
  étape par étape'
seo_desc: 'By Rajesh Pillai

  Understand Node internals by coding small packages/modules


  Mastering the Node.JS Internals

  If you are new to Node.js there are many tutorials here on Medium and elsewhere.
  You can check out my article All About Core Node.JS, for exa...'
---

Par Rajesh Pillai

#### Comprendre les internes de Node en codant de petits packages/modules

![Image](https://cdn-media-1.freecodecamp.org/images/UP-9RFQEMzAUWhc-0nnF4mCW2DB43Z59zYwh)
_Maîtriser les internes de Node.JS_

Si vous êtes nouveau dans Node.js, il existe de nombreux tutoriels ici sur Medium et ailleurs. Vous pouvez consulter mon article [All About Core Node.JS](https://codeburst.io/all-about-core-nodejs-part-1-b9f4b0a83278), par exemple.

Mais sans plus tarder, passons au sujet en discussion : les « Event Emitters ». Les Event Emitters jouent un rôle très important dans l'écosystème Node.js.

L'EventEmitter est un module qui facilite la communication/interaction entre les objets dans Node. EventEmitter est au cœur de l'architecture asynchrone pilotée par événements de Node. De nombreux modules intégrés de Node héritent d'EventEmitter, y compris des frameworks populaires comme Express.js.

Le concept est assez simple : les objets émetteurs émettent des événements nommés qui provoquent l'appel des écouteurs précédemment enregistrés. Ainsi, un objet émetteur a essentiellement deux fonctionnalités principales :

* Émettre des événements nommés.
* Enregistrer et désenregistrer des fonctions d'écoute.

C'est un peu comme un modèle de conception pub/sub ou observateur (bien que pas exactement).

#### Ce que nous allons construire dans ce tutoriel

* Classe EventEmitter
* Méthode on / addEventListener
* Méthode off / removeEventListener
* Méthode once
* Méthode emit
* Méthode rawListeners
* Méthode listenerCount

Les fonctionnalités de base ci-dessus sont suffisantes pour implémenter un système complet en utilisant le modèle d'événements.

Avant de nous lancer dans le codage, examinons comment nous allons utiliser la classe EventEmitter. Veuillez noter que notre code imitera l'API exacte du module 'events' de Node.js.

En fait, si vous remplacez notre EventEmitter par le module 'events' intégré de Node.js, vous obtiendrez le même résultat.

#### Exemple 1 — Créer une instance d'émetteur d'événements et enregistrer quelques callbacks

```js
const myEmitter = new EventEmitter();

function c1() {
   console.log('un événement s'est produit !');
}

function c2() {
   console.log('un autre événement s'est produit !');
}

myEmitter.on('eventOne', c1); // S'enregistrer pour eventOne
myEmitter.on('eventOne', c2); // S'enregistrer pour eventOne
```

Lorsque l'événement 'eventOne' est émis, les deux callbacks ci-dessus doivent être invoqués.

```
myEmitter.emit('eventOne');
```

La sortie dans la console sera la suivante :

```
un événement s'est produit !
un autre événement s'est produit !
```

#### Exemple 2 — S'enregistrer pour que l'événement ne soit déclenché qu'une seule fois en utilisant once.

```
myEmitter.once('eventOnce', () => console.log('eventOnce déclenché une fois'));
```

Émettre l'événement 'eventOnce' :

```js
myEmitter.emit('eventOne');
```

La sortie suivante devrait apparaître dans la console :

```
eventOnce déclenché une fois
```

Émettre à nouveau des événements enregistrés avec once n'aura aucun impact.

```js
myEmitter.emit('eventOne');
```

Puisque l'événement n'a été émis qu'une seule fois, l'instruction ci-dessus n'aura aucun impact.

#### Exemple 3 — S'enregistrer pour l'événement avec des paramètres de callback

```js
myEmitter.on('status', (code, msg)=> console.log(`Got ${code} and ${msg}`));
```

Émettre l'événement avec des paramètres :

```js
myEmitter.emit('status', 200, 'ok');
```

La sortie dans la console sera la suivante :

```
Got 200 and ok
```

NOTE : Vous pouvez émettre des événements plusieurs fois (sauf ceux enregistrés avec la méthode once).

#### Exemple 4 — Désenregistrer des événements

```js
myEmitter.off('eventOne', c1);
```

Maintenant, si vous émettez l'événement comme suit, rien ne se passera et ce sera un noop :

```js
myEmitter.emit('eventOne');  // noop
```

#### Exemple 5 — Obtenir le nombre d'écouteurs

```js
console.log(myEmitter.listenerCount('eventOne'));
```

NOTE : Si l'événement a été désenregistré en utilisant la méthode off ou removeListener, alors le compte sera 0.

#### Exemple 6 — Obtenir les écouteurs bruts

```js
console.log(myEmitter.rawListeners('eventOne'));
```

#### Exemple 7 — Démonstration d'un exemple asynchrone

```js
// Exemple 2->Adapté et merci à Sameer Buna
class WithTime extends EventEmitter {
  execute(asyncFunc, ...args) {
    this.emit('begin');
    console.time('execute');
    this.on('data', (data)=> console.log('got data ', data));
    asyncFunc(...args, (err, data) => {
      if (err) {
        return this.emit('error', err);
      }
      this.emit('data', data);
      console.timeEnd('execute');
      this.emit('end');
    });
  }
}
```

Utilisation de l'émetteur d'événements withTime :

```js
const withTime = new WithTime();

withTime.on('begin', () => console.log('About to execute'));
withTime.on('end', () => console.log('Done with execute'));

const readFile = (url, cb) => {
  fetch(url)
    .then((resp) => resp.json()) // Transformer les données en json
    .then(function(data) {
      cb(null, data);
    });
}

withTime.execute(readFile, 'https://jsonplaceholder.typicode.com/posts/1');
```

Vérifiez la sortie dans la console. La liste des posts sera affichée avec d'autres logs.

#### Le modèle Observateur pour notre Event Emitter

![Image](https://cdn-media-1.freecodecamp.org/images/sPkTz3OExo-FXteQwtFkoDVQmZeFfHE56-WJ)

#### Diagramme visuel 1 (Méthodes dans notre EventEmitter)

![Image](https://cdn-media-1.freecodecamp.org/images/plokwquvVbN4xa25kuk-QvYJ9b2ICqXWZ4Hb)

Maintenant que nous comprenons l'API d'utilisation, passons au codage du module.

#### Le code complet de base pour la classe EventEmitter

Nous allons remplir les détails de manière incrémentielle dans les prochaines sections.

```js
class EventEmitter {
  listeners = {};  // paire clé-valeur
  
  addListener(eventName, fn) {}
  on(eventName, fn) {}
  
  removeListener(eventName, fn) {}
  off(eventName, fn) {}
  
  once(eventName, fn) {}
  
  emit(eventName, ...args) { }
  
  listenerCount(eventName) {}
  
  rawListeners(eventName) {}
}
```

Nous commençons par créer le modèle pour la classe EventEmitter ainsi qu'un hash pour stocker les écouteurs. Les écouteurs seront stockés sous forme de paire clé-valeur. La valeur pourrait être un tableau (puisque pour le même événement, nous permettons à plusieurs écouteurs d'être enregistrés).

#### 1. La méthode addListener()

Implémentons maintenant la méthode addListener. Elle prend un nom d'événement et une fonction de callback à exécuter.

```js
  addListener(event, fn) {
    this.listeners[event] = this.listeners[event] || [];
    this.listeners[event].push(fn);
    return this;
  }
```

#### Une petite explication :

La méthode addListener vérifie si l'événement est déjà enregistré. Si oui, elle retourne le tableau, sinon un tableau vide.

```js
this.listeners[event] // retournera un tableau d'événements ou undefined (première inscription)
```

Par exemple...

Comprenons cela avec un exemple d'utilisation. Créons un nouvel eventEmitter et enregistrons un 'test-event'. C'est la première fois que le 'test-event' est enregistré.

```js
const eventEmitter = new EventEmitter();
eventEmitter.addListener('test-event', 
 ()=> { console.log ("test one") } 
);
```

À l'intérieur de la méthode addListener() :

```js
this.listeners[event] =>  this.listeners['test-event'] 
                  => undefined || []
                  => []
```

Le résultat sera :

```js
this.listeners['test-event'] = [];  // tableau vide
```

et ensuite la fonction 'fn' sera ajoutée à ce tableau comme montré ci-dessous :

```js
this.listeners['test-event'].push(fn);
```

J'espère que cela rend la méthode 'addListener' très claire à déchiffrer et à comprendre.

**Note : Plusieurs callbacks peuvent être enregistrés pour le même événement.**

![Image](https://cdn-media-1.freecodecamp.org/images/OOZkAQBbwteVdom2igLABEgFRmvsrkR9E9AB)

#### 2. La méthode on

Ce n'est qu'un alias pour la méthode 'addListener'. Nous utiliserons la méthode 'on' plus que la méthode 'addListener' pour des raisons de commodité.

```js
on(event, fn) {
  return this.addListener(event, fn);
}
```

#### 3. La méthode removeListener(event, fn)

La méthode removeListener prend un eventName et le callback comme paramètres. Elle supprime l'écouteur mentionné du tableau d'événements.

NOTE : Si l'événement a plusieurs écouteurs, les autres écouteurs ne seront pas impactés.

Tout d'abord, jetons un coup d'œil au code complet pour removeListener.

```js
removeListener (event, fn) {
    let lis = this.listeners[event];
    if (!lis) return this;
    for(let i = lis.length; i > 0; i--) {
      if (lis[i] === fn) {
        lis.splice(i,1);
        break;
      }
    }
    return this;
}
```

Voici la méthode removeListener expliquée étape par étape :

* Récupérer le tableau des écouteurs par 'event'
* Si aucun n'est trouvé, retourner 'this' pour le chaînage.
* Si trouvé, parcourir tous les écouteurs. Si l'écouteur actuel correspond au paramètre 'fn', utiliser la méthode splice du tableau pour le supprimer. Sortir de la boucle.
* Retourner 'this' pour continuer le chaînage.

#### 4. La méthode off(event, fn)

Ce n'est qu'un alias pour la méthode 'removeListener'. Nous utiliserons la méthode 'on' plus que la méthode 'addListener' pour des raisons de commodité.

```js
  off(event, fn) {
    return this.removeListener(event, fn);
  }
```

#### 5. La méthode once(eventName, fn)

Ajoute une fonction d'écoute **une seule fois** pour l'événement nommé `eventName`. La prochaine fois que `eventName` est déclenché, cet écouteur est supprimé puis invoqué.

Utilisez pour les événements de type configuration/init.

Jetons un coup d'œil au code.

```js
once(eventName, fn) {
    this.listeners[event] = this.listeners[eventName] || [];
    const onceWrapper = () => {
      fn();
      this.off(eventName, onceWrapper);
    }
    this.listeners[eventName].push(onceWrapper);
    return this;
}
```

Voici la méthode **once** expliquée étape par étape :

* Obtenir l'objet tableau de l'événement. Tableau vide si c'est la première fois.
* Créer une fonction wrapper appelée onceWrapper qui invoquera la fonction fn lorsque l'événement est émis et supprime également l'écouteur.
* Ajouter la fonction enveloppée au tableau.
* Retourner 'this' pour le chaînage.

#### 6. La méthode emit (eventName, ..args)

Appelle de manière synchrone chacun des écouteurs enregistrés pour l'événement nommé `eventName`, dans l'ordre où ils ont été enregistrés, en passant les arguments fournis à chacun.

Retourne `true` si l'événement avait des écouteurs, `false` sinon.

```js
emit(eventName, ...args) {
    let fns = this.listeners[eventName];
    if (!fns) return false;
    fns.forEach((f) => {
      f(...args);
    });
    return true;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/6RYZbGvcpf5QgkKVfVUTeWUvBrdy6NbBUiw6)

Voici la méthode **emit** expliquée étape par étape :

* Obtenir les fonctions pour le paramètre eventName mentionné
* Si aucun écouteur, retourner false
* Pour tous les écouteurs de fonction, invoquer la fonction avec les arguments
* Retourner true lorsque terminé

#### 7. La méthode listenerCount (eventName)

Retourne le nombre d'écouteurs écoutant l'événement nommé `eventName`.

Voici le code source :

```js
listenerCount(eventName) {
    let fns = this.listeners[eventName] || [];
    return fns.length;
}
```

Voici la méthode listenerCount expliquée étape par étape :

* Obtenir les fonctions/écouteurs concernés ou un tableau vide si aucun.
* Retourner la longueur.

#### 8. La méthode rawListeners(eventName)

Retourne une copie du tableau des écouteurs pour l'événement nommé `eventName`, y compris les wrappers (comme ceux créés par `.once()`). Les wrappers once dans cette implémentation ne seront pas disponibles si l'événement a été émis une fois.

```js
rawListeners(event) {
    return this.listeners[event];
}
```

Le code source complet pour référence :

```js
class EventEmitter {
  listeners = {}
  
  addListener(eventName, fn) {
    this.listeners[eventName] = this.listeners[eventName] || [];
    this.listeners[eventName].push(fn);
    return this;
  }

  on(eventName, fn) {
    return this.addListener(eventName, fn);
  }

  once(eventName, fn) {
    this.listeners[eventName] = this.listeners[eventName] || [];
    const onceWrapper = () => {
      fn();
      this.off(eventName, onceWrapper);
    }
    this.listeners[eventName].push(onceWrapper);
    return this;
  }

  off(eventName, fn) {
    return this.removeListener(eventName, fn);
  }

  removeListener (eventName, fn) {
    let lis = this.listeners[eventName];
    if (!lis) return this;
    for(let i = lis.length; i > 0; i--) {
      if (lis[i] === fn) {
        lis.splice(i,1);
        break;
      }
    }
    return this;
  }

  emit(eventName, ...args) {
    let fns = this.listeners[eventName];
    if (!fns) return false;
    fns.forEach((f) => {
      f(...args);
    });
    return true;
  }

  listenerCount(eventName) {
    let fns = this.listeners[eventName] || [];
    return fns.length;
  }

  rawListeners(eventName) {
    return this.listeners[eventName];
  }
}
```

Le code complet est disponible ici :

[https://jsbin.com/gibofab/edit?js,console,output](https://jsbin.com/gibofab/edit?js,console,output)

En tant qu'exercice, n'hésitez pas à implémenter d'autres API d'événements à partir de la documentation [https://nodejs.org/api/events.html](https://nodejs.org/api/events.html).

Si vous avez aimé cet article et souhaitez voir plus d'articles similaires, n'hésitez pas à donner quelques applaudissements :)

**NOTE** : Le code est optimisé pour la lisibilité et non pour la performance. Peut-être, en tant qu'exercice, vous pouvez optimiser le code et le partager dans la section des commentaires. N'a pas été entièrement testé pour les cas limites et certaines validations peuvent être incorrectes car il s'agissait d'une rédaction rapide.

Cet article fait partie du prochain cours vidéo « Node.JS Master Class — Construisez votre propre Framework MVC de type ExpressJS à partir de zéro ».

Le titre du cours n'est pas encore finalisé.