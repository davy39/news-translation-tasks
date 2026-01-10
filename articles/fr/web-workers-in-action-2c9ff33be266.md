---
title: 'Les Web Workers en action : pourquoi ils sont utiles et comment les utiliser'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-12T20:39:37.000Z'
originalURL: https://freecodecamp.org/news/web-workers-in-action-2c9ff33be266
coverImage: https://cdn-media-1.freecodecamp.org/images/1*f1HRu4YeZDn3PAS81QjuNg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
- name: webworker
  slug: webworker
seo_title: 'Les Web Workers en action : pourquoi ils sont utiles et comment les utiliser'
seo_desc: 'By The Hungry Brain

  Javascript is single threaded and multiple scripts can not execute at the same time.
  So if we execute any heavy computation task, then sometimes our page become unresponsive
  and the user can not do anything else until that executi...'
---

Par The Hungry Brain

JavaScript est mono-thread et plusieurs scripts ne peuvent pas s'exécuter en même temps. Ainsi, si nous exécutons une tâche de calcul lourde, notre page peut devenir non réactive et l'utilisateur ne peut rien faire d'autre jusqu'à ce que cette exécution soit terminée.

Par exemple :

```js
average = (numbers) => {
    let startTime = new Date().getTime();
    let len = numbers,
        sum = 0,
        i;

    if (len === 0) {
        return 0;
    }

    for (i = 0; i < len; i++) {
        console.log('i :: ', i)
        sum += i;
    }

    let endTime = new Date().getTime();
    alert('Moyenne - ', sum / len);
}

hello = () => {
    alert("Hello World !!")
}

/*
Collez le code ci-dessus dans la console de l'outil de développement du navigateur
et essayez d'appeler average(10000) et hello un par un
*/
```

Dans l'exemple ci-dessus, si vous appelez _average_ avant la méthode _hello_, votre page deviendra non réactive et vous ne pourrez pas cliquer sur _Hello_ jusqu'à ce que l'exécution de _average_ soit terminée.

Vous pouvez voir que lorsque _average_ est appelé avec 10000 en entrée, il a pris ~1,82 secondes. Pendant ce temps, la page devient non réactive et vous n'avez pas pu cliquer sur le bouton hello.

### Programmation asynchrone

JavaScript offre aux développeurs la possibilité d'écrire du **code asynchrone**. En écrivant du code asynchrone, vous pouvez éviter ce type de problème dans votre application, car cela permet à l'interface utilisateur de votre application d'être réactive, en "planifiant" des parties du code à exécuter un peu plus tard dans la boucle d'événements.

Un bon exemple de programmation asynchrone est la `requête XHR`, dans laquelle nous appelons une API de manière asynchrone et, pendant que nous attendons la réponse, d'autres codes peuvent être exécutés. Mais cela est limité à certains cas d'utilisation liés principalement aux API web.

Une autre façon d'écrire du code asynchrone est d'utiliser la méthode `setTimeout`. Dans certains cas, vous pouvez obtenir de bons résultats en débloquant l'interface utilisateur des calculs plus longs en utilisant `setTimeout`. Par exemple, en regroupant un calcul complexe dans des appels `setTimeout` séparés.

Par exemple :

```js
average = (numbers) => {
    let startTime = new Date().getTime();
    var len = numbers,
        sum = 0,
        i;

    if (len === 0) {
        return 0;
    }

    let calculateSumAsync = (i) => {
        if (i < len) {
            // Place le prochain appel de fonction dans la boucle d'événements.
            setTimeout(() => {
                sum += i;
                calculateSumAsync(i + 1);
            }, 0);
        } else {
            // La fin du tableau est atteinte, nous invoquons donc l'alerte.
            let endTime = new Date().getTime();
            alert('Moyenne - ', sum / len);
        }
    };

    calculateSumAsync(0);
};

hello = () => {
    alert('Hello World !!')
};
```

Dans cet exemple, vous pouvez voir qu'après avoir cliqué sur le bouton _Calculer la moyenne_, vous pouvez toujours cliquer sur le bouton _Hello_ (qui affiche un message d'alerte). Cette façon de programmer est certainement non bloquante mais prend trop de temps et n'est pas réalisable dans les applications réelles.

Ici, pour la même entrée 10000, cela a pris ~60 secondes, ce qui est très inefficace.

**Alors, comment résoudre ces problèmes efficacement ?**

La réponse est **les Web Workers**.

### Qu'est-ce que les Web Workers ?

Les Web Workers en JavaScript sont un excellent moyen d'exécuter certaines tâches très laborieuses et chronophages dans un thread séparé du thread principal. Ils s'exécutent en arrière-plan et effectuent des tâches sans interférer avec l'interface utilisateur.

Les Web Workers ne font pas partie de JavaScript, ce sont une fonctionnalité du navigateur qui peut être accessible via JavaScript.

Les Web Workers sont créés par une fonction constructeur **Worker()** qui exécute un fichier JS nommé.

```js
// créer un Web Worker dédié
const myWorker = new Worker('worker.js');
```

Si le fichier spécifié existe, il sera téléchargé de manière asynchrone et, sinon, le worker échouera silencieusement, de sorte que votre application fonctionnera toujours en cas d'erreur 404.

Nous en apprendrons davantage sur la création et le fonctionnement des Web Workers dans la section suivante.

Le thread du worker a son propre contexte et, par conséquent, vous ne pouvez accéder qu'à certaines fonctionnalités à l'intérieur d'un thread de worker, comme les web sockets, la base de données indexée.

Il existe certaines **restrictions** avec les Web Workers :

1. Vous ne pouvez pas manipuler directement le DOM depuis l'intérieur d'un worker.
2. Vous ne pouvez pas utiliser certaines méthodes et propriétés par défaut de l'objet window, car l'objet window n'est pas disponible à l'intérieur d'un thread de worker.
3. Le contexte à l'intérieur du thread de worker peut être accessible via **_DedicatedWorkerGlobalScope ou SharedWorkerGlobalScope_** selon l'utilisation.

### Fonctionnalités des Web Workers

Il existe deux types de Web Workers :

1. **Dedicated web worker** - Un worker dédié n'est accessible que par le script qui l'a appelé.
2. **Shared web worker** - Un worker partagé est accessible par plusieurs scripts, même s'ils sont accessibles par différentes fenêtres, iframes ou même workers.

Discutons plus en détail de ces deux types de Web Workers.

#### Création d'un Web Worker

La création est pratiquement la même pour un Dedicated et un Shared web worker.

**Dedicated web worker**

* Créer un nouveau worker est simple, il suffit d'appeler le constructeur Worker et de passer le chemin du script que vous souhaitez exécuter en tant que worker.

```js
// créer un Web Worker dédié
const myWorker = new Worker('worker.js');
```

**Shared web worker** :

* Créer un nouveau worker partagé est pratiquement la même chose que pour un worker dédié, mais avec un nom de constructeur différent.

```js
// créer un Web Worker partagé
const mySharedWorker = new SharedWorker('worker.js');
```

#### Communication entre le thread principal et le thread du worker

La communication entre le thread principal et le thread du worker se fait via la méthode _postMessage_ et le gestionnaire d'événements _onmessage_.

**Dedicated web worker**  
Dans le cas d'un worker dédié, le système de communication est simple. Vous devez simplement utiliser la méthode postMessage chaque fois que vous souhaitez envoyer un message au worker.

```js
(() => {
  // nouveau worker
  let myWorker = new Worker('worker.js');

  // gestionnaire d'événements pour recevoir un message du worker
  myWorker.onmessage = (e) => {
    document.getElementById('time').innerHTML = `${e.data.time} secondes`;
  };

  let average = (numbers) => {
    // envoi d'un message au Web Worker avec un argument
    myWorker.postMessage(numbers);
  }

  average(1000);
})();
```

Et à l'intérieur d'un Web Worker, vous pouvez répondre lorsque le message est reçu en écrivant un bloc de gestionnaire d'événements comme ceci :

```js
onmessage = (e) => {
    let numbers = e.data;
    let startTime = new Date().getTime();
    let len = numbers,
        sum = 0,
        i;

    if (len === 0) {
        return 0;
    }

    for (i = 0; i < len; i++) {
        sum += i;
    }

    let endTime = new Date().getTime();
    postMessage({average: sum / len, time: ((endTime - startTime) / 1000)})
};
```

Le gestionnaire `onmessage` permet d'exécuter du code chaque fois qu'un message est reçu. 

Ici, nous calculons la moyenne des nombres, puis utilisons à nouveau `postMessage()`, pour renvoyer le résultat au thread principal.

Comme vous pouvez le voir à la _ligne 6 dans main.js_, nous avons utilisé l'événement onmessage sur l'instance du worker. Ainsi, chaque fois que le thread du worker utilise postMessage, onmessage dans le thread principal est déclenché.

* **Shared web worker**  
Dans le cas d'un worker partagé, le système de communication est un peu différent. Comme un worker est partagé entre plusieurs scripts, nous devons communiquer via l'objet port de l'instance du worker. Cela est fait implicitement dans le cas des workers dédiés. Vous devez utiliser la méthode postMessage chaque fois que vous souhaitez envoyer un message au worker.

```js
(() => {
  // nouveau worker
  let myWorker = new Worker('worker.js');

  // gestionnaire d'événements pour recevoir un message du worker
  myWorker.onmessage = (e) => {
    document.getElementById('time').innerHTML = `${e.data.time} secondes`;
  };

  let average = (numbers) => {
    // envoi d'un message au Web Worker avec un argument
    myWorker.postMessage(numbers);
  }

  average(1000);
```

À l'intérieur d'un Web Worker (_main-shared-worker.js_), c'est un peu plus complexe. Tout d'abord, nous utilisons un gestionnaire `onconnect` pour déclencher du code lorsqu'une connexion au port se produit (_ligne 2_). 
Nous utilisons l'attribut `ports` de cet objet événement pour récupérer le port et le stocker dans une variable (_ligne 4_). 
Ensuite, nous ajoutons un gestionnaire `message` sur le port pour effectuer le calcul et renvoyer le résultat au thread principal (_ligne 7 et ligne 25_) comme ceci :

```js
onmessage = (e) => {
    let numbers = e.data;
    let startTime = new Date().getTime();
    let len = numbers,
        sum = 0,
        i;

    if (len === 0) {
        return 0;
    }

    for (i = 0; i < len; i++) {
        sum += i;
    }

    let endTime = new Date().getTime();
    postMessage({average: sum / len, time: ((endTime - startTime) / 1000)})
};
```

#### Terminaison d'un Web Worker

Si vous devez terminer immédiatement un worker en cours d'exécution depuis le thread principal, vous pouvez le faire en appelant la méthode _terminate_ du worker :

```js
// terminer une instance de Web Worker
myWorker.terminate();
```

Le thread du worker est tué immédiatement sans avoir la possibilité de terminer ses opérations.

### Création de Web Workers

Les workers peuvent créer d'autres workers s'ils le souhaitent. Mais ils doivent être hébergés dans la même origine que la page parente.

### Importation de scripts

Les threads des workers ont accès à une fonction globale, `importScripts()`, qui leur permet d'importer des scripts.

```js
importScripts();                         /* n'importe rien */
importScripts('foo.js');                 /* importe seulement "foo.js" */
importScripts('foo.js', 'bar.js');       /* importe deux scripts */
importScripts('//example.com/hello.js'); /* Vous pouvez importer des scripts depuis d'autres origines */
```

### Démonstration de travail

Nous avons discuté de certaines des approches ci-dessus pour atteindre la programmation asynchrone afin que notre interface utilisateur ne soit pas bloquée par une tâche de calcul lourde. Mais il y a certaines limitations à ces approches. Nous pouvons donc utiliser les Web Workers pour résoudre ces problèmes efficacement.

> _Cliquez [ici](https://bhushangoel.github.io/webworker-demo-1/) pour exécuter cette démonstration en direct._

Ici, vous verrez 3 sections :

1. **Code bloquant** :  
Lorsque vous cliquez sur _calculer la moyenne_, le chargeur ne s'affiche pas et après un certain temps, vous voyez le résultat final et le temps pris. Cela est dû au fait que dès que la méthode _average_ est appelée, j'ai également déclenché la méthode _showLoader_. Mais comme JS est mono-thread, il n'exécutera pas showLoader jusqu'à ce que l'exécution de average soit terminée. Vous ne pourrez donc jamais voir le chargeur dans ce cas.
2. **Code asynchrone** :  
Ici, j'ai essayé d'obtenir la même fonctionnalité en utilisant la méthode setTimeout et en mettant chaque exécution de fonction dans une boucle d'événements. Vous verrez le chargeur dans ce cas, mais la réponse prend du temps par rapport à la méthode définie ci-dessus.
3. **Web worker** :  
Ceci est un exemple d'utilisation d'un Web Worker. Ici, vous verrez le chargeur dès que vous cliquez sur calculer la moyenne et vous obtiendrez une réponse dans le même temps que la méthode 1, pour le même nombre.

Vous pouvez accéder au code source pour cela [ici](https://github.com/bhushangoel/webworker-demo-1/tree/master).

### Concepts avancés

Il existe certains concepts avancés liés aux Web Workers. Nous ne les discuterons pas en détail, mais il est bon de les connaître.

1. **Politique de sécurité du contenu** 
Les Web Workers ont leur propre contexte d'exécution indépendant du document qui les a créés et, pour cette raison, ils ne sont pas régis par la politique de sécurité du contenu du thread/worker parent. 
L'exception à cela est si l'origine du script du worker est un identifiant globalement unique (par exemple, si son URL a un schéma de données ou de blob). Dans ce cas, le worker hérite de la politique de sécurité du contenu du document ou du worker qui l'a créé.
2. **Transfert de données vers et depuis les workers** 
Les données passées entre le thread principal et le thread du worker sont **copiées** et non partagées. Les objets sont sérialisés lorsqu'ils sont transmis au worker, puis désérialisés à l'autre extrémité. La page et le worker **ne partagent pas la même instance**, donc le résultat final est qu'**un duplicata** est créé à chaque extrémité. 
Les navigateurs ont implémenté l'algorithme [**<ins>Structured Cloning</ins>**](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm) pour y parvenir.
3. **Workers intégrés** 
Vous pouvez également intégrer le code d'un worker à l'intérieur d'une page web (html). Pour cela, vous devez ajouter une balise script sans attribut src et lui attribuer un type MIME non exécutable, comme ceci :

```js
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8" />
  <title>worker intégré</title>
  <!--balise script avec MIME non identifié et sans attribut src -->
  <script type="text/js-worker">
    // Ce script NE SERA PAS analysé par les moteurs JS car son type MIME est text/js-worker.
    var myVar = 'Hello World!';
    
    // bloc worker
    function onmessage(e) {
      // code worker
    }
  </script>
</head>
<body></body>
</html>
```

Il existe de nombreux cas d'utilisation pour les Web Workers dans notre application. J'ai simplement discuté d'un petit scénario. J'espère que cela vous aide à comprendre le concept des Web Workers.

#### [Liens]

Dépôt Github : [https://github.com/bhushangoel/webworker-demo-1](https://github.com/bhushangoel/webworker-demo-1) Web worker en action : [https://bhushangoel.github.io/webworker-demo-1/](https://bhushangoel.github.io/webworker-demo-1/) Démonstration JS : [https://bhushangoel.github.io/](https://bhushangoel.github.io/)

Merci pour votre lecture.

Bonne apprentissage :)

_Publié à l'origine sur [www.thehungrybrain.com](https://www.thehungrybrain.com/home/web-workers).