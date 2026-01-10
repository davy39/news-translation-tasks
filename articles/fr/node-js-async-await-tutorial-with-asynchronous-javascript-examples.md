---
title: Tutoriel Node.js Async Await – Avec des exemples JavaScript asynchrones
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-05-04T16:07:17.000Z'
originalURL: https://freecodecamp.org/news/node-js-async-await-tutorial-with-asynchronous-javascript-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/yoda.jpeg
tags:
- name: async/await
  slug: asyncawait
- name: asynchronous
  slug: asynchronous
- name: JavaScript
  slug: javascript
- name: node js
  slug: node-js
seo_title: Tutoriel Node.js Async Await – Avec des exemples JavaScript asynchrones
seo_desc: 'By Stanley Nguyen

  One of the hardest concepts to wrap your head around when you''re first learning
  JavaScript is the asynchronous processing model of the language. For the majority
  of us, learning asynchronous programming looks pretty much like this


  ...'
---

Par Stanley Nguyen

L'un des concepts les plus difficiles à assimiler lorsque l'on apprend JavaScript pour la première fois est le modèle de traitement asynchrone du langage. Pour la majorité d'entre nous, l'apprentissage de la programmation asynchrone ressemble à peu près à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/async.png)
_Si votre première expérience avec l'asynchrone n'était pas comme ça, considérez-vous comme un génie_

Aussi difficile soit-elle à appréhender, la programmation asynchrone est cruciale à apprendre si vous voulez utiliser JavaScript et Node.js pour construire des applications web et des serveurs – car le code JS est **asynchrone par défaut**.

## Les fondamentaux de la programmation asynchrone

Alors, qu'est-ce que le modèle de traitement asynchrone, ou le modèle `non-blocking I/O` (dont vous avez probablement entendu parler si vous utilisez Node.js) ?

Voici une description courte (TL;DR) : dans un modèle de traitement asynchrone, lorsque le moteur de votre application interagit avec des parties externes (comme un système de fichiers ou un réseau), il n'attend pas d'obtenir un résultat de ces parties. Au lieu de cela, il continue vers les tâches suivantes et ne revient vers ces parties externes précédentes qu'une fois qu'il a reçu un signal de résultat.

Pour comprendre le modèle de traitement asynchrone par défaut de Node.js, jetons un coup d'œil à l'atelier hypothétique du Père Noël. Avant que tout travail ne puisse commencer, le Père Noël doit lire chacune des adorables lettres des enfants du monde entier.

![Le Père Noël lisant une lettre pour l'atelier](https://www.freecodecamp.org/news/content/images/2021/05/santa-01.png)

Il détermine ensuite le cadeau demandé, traduit le nom de l'article en [langue elfique](https://en.wikipedia.org/wiki/Elvish_languages), puis transmet les instructions à chacun de nos lutins travailleurs qui ont des spécialisations différentes : les jouets en bois pour Red, les peluches pour Blue et les jouets robotiques pour Green.

![Le Père Noël transmettant les instructions à Red](https://www.freecodecamp.org/news/content/images/2021/05/santa-02.png)

Cette année, en raison de [la pandémie de COVID-19](https://en.wikipedia.org/wiki/COVID-19_pandemic), seule la moitié des lutins du Père Noël peut venir l'aider dans son atelier. Pourtant, parce qu'il est sage, le Père Noël décide qu'au lieu d'attendre que chaque lutin finisse de préparer un cadeau (c'est-à-dire travailler de manière synchrone), il continuera à traduire et à distribuer les instructions de sa pile de lettres.

![Le Père Noël transmettant les instructions à Blue](https://www.freecodecamp.org/news/content/images/2021/05/santa-03.png)

Et ainsi de suite...

![Le Père Noël continue de distribuer les instructions](https://www.freecodecamp.org/news/content/images/2021/05/santa-04.png)

Alors qu'il s'apprête à lire une autre lettre, Red informe le Père Noël qu'il a terminé la préparation du premier cadeau. Le Père Noël reçoit alors le cadeau de Red et le met de côté.

![Le Père Noël recevant le cadeau de Red](https://www.freecodecamp.org/news/content/images/2021/05/santa-05.png)

Puis il continue à traduire et à transmettre les instructions de la lettre suivante.

![Le Père Noël transmettant les instructions à Green](https://www.freecodecamp.org/news/content/images/2021/05/santa-06.png)

Comme il n'a qu'à emballer un robot volant déjà fabriqué, Green peut rapidement terminer la préparation et remettre le cadeau au Père Noël.

![Le Père Noël recevant le cadeau de Green](https://www.freecodecamp.org/news/content/images/2021/05/santa-07.png)

Après une journée entière de travail acharné et asynchrone, le Père Noël et les lutins parviennent à terminer toute la préparation des cadeaux. Grâce à son modèle de travail asynchrone amélioré, l'atelier du Père Noël a terminé en un temps record malgré l'impact de la pandémie.

![Le Père Noël a reçu tous les cadeaux](https://www.freecodecamp.org/news/content/images/2021/05/santa-08.png)

C'est donc l'idée de base d'un modèle de traitement asynchrone ou d'I/O non bloquantes. Voyons maintenant comment cela se passe spécifiquement dans Node.js.

## L'Event Loop de Node.js

Vous avez peut-être entendu dire que Node.js est monothreadé (single-threaded). Cependant, pour être exact, seul l'Event Loop de Node.js, qui interagit avec un pool de threads de travail C++ en arrière-plan, est monothreadé. Il y a quatre composants importants dans le modèle de traitement de Node.js :

* Event Queue (File d'attente d'événements) : Tâches déclarées dans un programme, ou renvoyées par le pool de threads de traitement via des [callbacks](https://nodejs.org/en/knowledge/getting-started/control-flow/what-are-callbacks/). (L'équivalent dans notre atelier du Père Noël est la pile de lettres pour le Père Noël.)
* Event Loop : Le thread principal de Node.js qui facilite les files d'attente d'événements et les pools de threads de travail pour effectuer les opérations – à la fois asynchrones et synchrones. (C'est le Père Noël. 🎅)
* Background thread pool (Pool de threads d'arrière-plan) : Ces threads effectuent le traitement réel des tâches, qui pourraient être bloquantes pour les I/O (par exemple, appeler et attendre une réponse d'une API externe). (Ce sont les lutins travailleurs 🧝🧝‍♀️🧝‍♂️ de notre atelier.)

Vous pouvez visualiser ce modèle de traitement comme ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/processing-model.png)
_Schéma avec l'aimable autorisation de c-sharpcorner.com_

Regardons un extrait de code réel pour voir cela en action :

```js
console.log("Hello");
https.get("https://httpstat.us/200", (res) => {
  console.log(`API returned status: ${res.statusCode}`);
});
console.log("from the other side");

```

Si nous exécutons le code ci-dessus, nous obtiendrons ceci dans notre sortie standard :

```bash
Hello
from the other side
API returned status: 200

```

Alors, comment le moteur Node.js exécute-t-il l'extrait de code ci-dessus ? Il commence par trois fonctions dans la pile d'appels (call stack) :

![Le traitement commence avec 3 fonctions dans la pile d'appels](https://www.freecodecamp.org/news/content/images/2021/05/execution-01-1.png)

"Hello" est ensuite imprimé dans la console et l'appel de fonction correspondant est retiré de la pile.

![Le console log Hello est retiré de la pile](https://www.freecodecamp.org/news/content/images/2021/05/execution-02-1.png)

L'appel de fonction à `https.get` (c'est-à-dire faire une requête GET à l'URL correspondante) est ensuite exécuté et délégué au pool de threads de travail avec un callback attaché.

![https.get délégué au pool de threads](https://www.freecodecamp.org/news/content/images/2021/05/execution-03.png)

L'appel de fonction suivant à `console.log` est exécuté, et "from the other side" est imprimé dans la console.

![Le console.log suivant est exécuté](https://www.freecodecamp.org/news/content/images/2021/05/execution-04.png)

Maintenant que l'appel réseau a renvoyé une réponse, l'appel de la fonction callback sera mis en file d'attente dans la file d'attente des rappels (callback queue). Notez que cette étape pourrait se produire avant l'étape immédiatement précédente (c'est-à-dire l'impression de "from the other side"), bien que normalement ce ne soit pas le cas.

![L'appel réseau se termine et le callback est mis en file d'attente](https://www.freecodecamp.org/news/content/images/2021/05/execution-05.png)

Le callback est ensuite placé dans notre pile d'appels :

![Le callback est placé dans la pile d'appels](https://www.freecodecamp.org/news/content/images/2021/05/execution-06.png)

et nous verrons ensuite "API returned status: 200" dans notre console, comme ceci :

![Le code de statut est imprimé](https://www.freecodecamp.org/news/content/images/2021/05/execution-07.png)

En facilitant la file d'attente des rappels et la pile d'appels, l'Event Loop de Node.js exécute efficacement notre code JavaScript de manière asynchrone.

## Une histoire synchrone de JavaScript et de l'async/await Node.js

Maintenant que vous avez une bonne compréhension de l'exécution asynchrone et du fonctionnement interne de l'Event Loop de Node.js, plongeons dans l'async/await en JavaScript. Nous verrons comment cela a évolué au fil du temps, de l'implémentation originale pilotée par les callbacks aux derniers mots-clés brillants async/await.

### Les Callbacks en JavaScript

La méthode originale pour gérer la nature asynchrone des moteurs JavaScript passait par les callbacks. Les callbacks sont essentiellement des fonctions qui seront exécutées, **généralement**, à la fin d'opérations synchrones ou d'I/O bloquantes.

Un exemple simple de ce modèle est la fonction intégrée `setTimeout` qui attendra un certain nombre de millisecondes avant d'exécuter le callback.

```js
setTimeout(2000, () => {
  console.log("Hello");
});

```

Bien qu'il soit pratique de simplement attacher des callbacks aux opérations bloquantes, ce modèle introduit également quelques problèmes :

* Callback hell (L'enfer des rappels)
* Inversion de contrôle (pas la bonne !)

#### Qu'est-ce que le callback hell ?

Regardons à nouveau un exemple avec le Père Noël et ses lutins. Pour préparer un cadeau, l'atelier du Père Noël doit effectuer quelques étapes différentes (chacune prenant un temps différent simulé à l'aide de `setTimeout`) :

```js
function translateLetter(letter, callback) {
  return setTimeout(2000, () => {
    callback(letter.split("").reverse().join(""));
  });
}
function assembleToy(instruction, callback) {
  return setTimeout(3000, () => {
    const toy = instruction.split("").reverse().join("");
    if (toy.includes("wooden")) {
      return callback(`polished ${toy}`);
    } else if (toy.includes("stuffed")) {
      return callback(`colorful ${toy}`);
    } else if (toy.includes("robotic")) {
      return callback(`flying ${toy}`);
    }
    callback(toy);
  });
}
function wrapPresent(toy, callback) {
  return setTimeout(1000, () => {
    callback(`wrapped ${toy}`);
  });
}

```

Ces étapes doivent être effectuées dans un ordre spécifique :

```js
translateLetter("wooden truck", (instruction) => {
  assembleToy(instruction, (toy) => {
    wrapPresent(toy, console.log);
  });
});
// Cela produira un "wrapped polished wooden truck" comme résultat final

```

En procédant de cette façon, l'ajout de nouvelles étapes au processus signifierait pousser les callbacks internes vers la droite et finir dans un callback hell comme celui-ci :

![Callback Hell](https://www.freecodecamp.org/news/content/images/2021/05/callback-hell.jpeg)

Les callbacks semblent séquentiels, mais parfois l'ordre d'exécution ne suit pas ce qui est affiché sur votre écran. Avec plusieurs couches de callbacks imbriqués, vous pouvez facilement perdre de vue la vue d'ensemble du flux du programme et produire plus de bugs ou simplement devenir plus lent lors de l'écriture de votre code.

Alors, comment résoudre ce problème ? Il suffit de modulariser les callbacks imbriqués dans des fonctions nommées et vous aurez un programme joliment aligné à gauche et facile à lire.

```js
function assembleCb(toy) {
  wrapPresent(toy, console.log);
}
function translateCb(instruction) {
  assembleToy(instruction, assembleCb);
}
translateLetter("wooden truck", translateCb);

```

#### Inversion de contrôle

Un autre problème avec le modèle de callback est que vous ne décidez pas comment les fonctions d'ordre supérieur exécuteront vos callbacks. Elles pourraient l'exécuter à la fin de la fonction, ce qui est conventionnel, mais elles pourraient aussi l'exécuter au début de la fonction ou l'exécuter plusieurs fois.

Fondamentalement, vous êtes à la merci des propriétaires de vos dépendances, et vous ne saurez peut-être jamais quand ils casseront votre code.

Pour résoudre ce problème, en tant qu'utilisateur de dépendance, vous ne pouvez pas faire grand-chose. Cependant, si vous êtes vous-même propriétaire d'une dépendance, veuillez toujours :

* Vous en tenir à la signature de callback conventionnelle avec l'erreur comme premier argument
* N'exécuter un callback qu'une seule fois à la fin de votre fonction d'ordre supérieur
* Documenter tout ce qui sort de la convention et qui est absolument requis, et viser toujours la compatibilité ascendante

### Les Promises en JavaScript

Les [Promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) ont été créées pour résoudre les problèmes mentionnés ci-dessus avec les callbacks. Les Promises garantissent que les utilisateurs de JavaScript :

* S'en tiennent à une convention spécifique avec leurs fonctions de signature `resolve` et `reject`.
* Enchaînent les fonctions de rappel dans un flux bien aligné et de haut en bas.

Notre exemple précédent avec l'atelier du Père Noël préparant des cadeaux peut être réécrit avec des promises comme ceci :

```js
function translateLetter(letter) {
  return new Promise((resolve, reject) => {
    setTimeout(2000, () => {
      resolve(letter.split("").reverse().join(""));
    });
  });
}
function assembleToy(instruction) {
  return new Promise((resolve, reject) => {
    setTimeout(3000, () => {
      const toy = instruction.split("").reverse().join("");
      if (toy.includes("wooden")) {
        return resolve(`polished ${toy}`);
      } else if (toy.includes("stuffed")) {
        return resolve(`colorful ${toy}`);
      } else if (toy.includes("robotic")) {
        return resolve(`flying ${toy}`);
      }
      resolve(toy);
    });
  });
}
function wrapPresent(toy) {
  return new Promise((resolve, reject) => {
    setTimeout(1000, () => {
      resolve(`wrapped ${toy}`);
    });
  });
}

```

avec les étapes effectuées proprement dans une chaîne :

```js
translateLetter("wooden truck")
  .then((instruction) => {
    return assembleToy(instruction);
  })
  .then((toy) => {
    return wrapPresent(toy);
  })
  .then(console.log);
// Cela produirait exactement le même cadeau : wrapped polished wooden truck

```

Cependant, les promises ne sont pas sans problèmes non plus. Les données dans chaque maillon de notre chaîne ont une portée différente et n'ont accès qu'aux données transmises par l'étape immédiatement précédente ou la portée parente.

Par exemple, notre étape d'emballage de cadeau pourrait vouloir utiliser des données de l'étape de traduction :

```js
function wrapPresent(toy, instruction) {
  return Promise((resolve, reject) => {
    setTimeout(1000, () => {
      resolve(`wrapped ${toy} with instruction: "${instruction}`);
    });
  });
}

```

C'est plutôt [un problème classique de "partage de mémoire" avec le threading](https://livebook.manning.com/book/c-plus-plus-concurrency-in-action/chapter-3/1). Pour résoudre ce problème, au lieu d'utiliser des variables dans la portée du parent, nous devrions utiliser `Promise.all` et ["partager les données en communiquant, plutôt que de communiquer en partageant des données"](https://blog.golang.org/codelab-share).

```js
translateLetter("wooden truck")
  .then((instruction) => {
    return Promise.all([assembleToy(instruction), instruction]);
  })
  .then((toy, instruction) => {
    return wrapPresent(toy, instruction);
  })
  .then(console.log);
// Cela produirait le cadeau : wrapped polished wooden truck with instruction: "kcurt nedoow"

```

### Async/Await en JavaScript

Dernier point, mais non le moindre, le petit dernier à la mode est async/await. Il est très facile à utiliser mais présente également certains risques.

Async/await résout les problèmes de partage de mémoire des promises en ayant tout sous la même portée. Notre exemple précédent peut être réécrit facilement comme ceci :

```js
(async function main() {
  const instruction = await translateLetter("wooden truck");
  const toy = await assembleToy(instruction);
  const present = await wrapPresent(toy, instruction);
  console.log(present);
})();
// Cela produirait le cadeau : wrapped polished wooden truck with instruction: "kcurt nedoow"

```

Cependant, même s'il est facile d'écrire du code asynchrone avec async/await, il est également facile de commettre des erreurs qui créent des failles de performance.

Localisons maintenant notre exemple de scénario de l'atelier du Père Noël à l'emballage des cadeaux et à leur chargement sur le traîneau.

```js
function wrapPresent(toy) {
  return Promise((resolve, reject) => {
    setTimeout(5000 * Math.random(), () => {
      resolve(`wrapped ${toy}`);
    });
  });
}
function loadPresents(presents) {
  return Promise((resolve, reject) => {
    setTimeout(5000, () => {
      let itemList = "";
      for (let i = 0; i < presents.length; i++) {
        itemList += `${i}. ${presents[i]}\n`;
      }
    });
  });
}

```

Une erreur courante que vous pourriez commettre est d'effectuer les étapes de cette façon :

```js
(async function main() {
  const presents = [];
  presents.push(await wrapPresent("wooden truck"));
  presents.push(await wrapPresent("flying robot"));
  presents.push(await wrapPresent("stuffed elephant"));
  const itemList = await loadPresents(presents);
  console.log(itemList);
})();

```

Mais le Père Noël a-t-il besoin d'attendre (`await`) que chacun des cadeaux soit emballé un par un avant de charger ? Certainement pas ! Les cadeaux devraient être emballés simultanément. Vous pourriez faire cette erreur souvent car il est si facile d'écrire `await` sans penser à la nature bloquante du mot-clé.

Pour résoudre ce problème, nous devrions regrouper les étapes d'emballage des cadeaux et les exécuter toutes en même temps :

```js
(async function main() {
  const presents = await Promise.all([
    wrapPresent("wooden truck"),
    wrapPresent("flying robot"),
    wrapPresent("stuffed elephant"),
  ]);
  const itemList = await loadPresents(presents);
  console.log(itemList);
})();

```

Voici quelques étapes recommandées pour aborder les problèmes de performance de concurrence dans votre code Node.js :

* Identifiez les points chauds avec plusieurs `await` consécutifs dans votre code
* Vérifiez s'ils sont dépendants les uns des autres (c'est-à-dire qu'une fonction utilise des données renvoyées par une autre)
* Rendez les appels de fonction indépendants concurrents avec `Promise.all`

## Conclusion (de l'article, pas de l'emballage des cadeaux 😂)

Félicitations d'être arrivé à la fin de cet article, j'ai fait de mon mieux pour rendre ce post plus court, mais le sujet de l'asynchrone en JavaScript est tout simplement très vaste.

Voici quelques points clés à retenir :

* Modularisez vos callbacks JavaScript pour éviter le callback hell
* Respectez [la convention pour les callbacks JS](https://gist.github.com/sunnycmf/b2ad4f80a3b627f04ff2)
* Partagez les données en communiquant via `Promise.all` lorsque vous utilisez des promises
* Soyez prudent quant aux implications de performance du code async/await

Nous ❤️ JavaScript :)

## Merci de m'avoir lu !

Enfin, si vous aimez mes écrits, n'hésitez pas à vous rendre sur [mon blog](https://blog.stanleynguyen.me/) pour des commentaires similaires et suivez-[moi sur Twitter](https://twitter.com/stanley_ngn). 🎉