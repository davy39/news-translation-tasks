---
title: Comment utiliser les Web Workers pour planifier des tâches asynchrones cohérentes
  en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-04T19:46:24.000Z'
originalURL: https://freecodecamp.org/news/how-web-workers-can-help-with-consistent-asynchronous-tasks-in-javascript-cd6d728fa4ee
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tMKwMb5J5ETFpeOUYQyMKQ.png
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment utiliser les Web Workers pour planifier des tâches asynchrones
  cohérentes en JavaScript
seo_desc: 'By Danny Mcwaves

  With the continuous improvements being made to Javascript engines, and the ever-expanding
  list of deprecated and new API’s to the ECMASCRIPT specification, the quest for
  blazing fast web applications has never been more on the rise.

  ...'
---

Par Danny Mcwaves

Avec les améliorations continues apportées aux moteurs Javascript et la liste toujours croissante des API obsolètes et nouvelles de la spécification ECMASCRIPT, la quête d'applications web ultra-rapides n'a jamais été aussi intense.

#### Qu'est-ce que le moteur Javascript ?

Le moteur Javascript est une machine virtuelle. Une `machine virtuelle` fait référence à l'émulation logicielle d'un système informatique donné. Le travail de base d'un moteur Javascript est de prendre le code Javascript qu'un développeur écrit et de le convertir en code rapide et optimisé pouvant être interprété par un navigateur.

![Image](https://cdn-media-1.freecodecamp.org/images/FcPt2Ss0kkGpIIgxjRSIxcRA7vWL-NJBdTOm)
_Pour en savoir plus sur les moteurs javascript, consultez le [moteur javascript v8](https://developers.google.com/v8/" rel="noopener" target="_blank" title=")._

Habituellement, ce processus s'exécute sur un seul **thread** (plus d'informations sur les threads plus tard), chaque instruction du code du développeur étant exécutée une à la fois. Le problème avec les applications/architectures à thread unique est que si une instruction ou un bloc d'instructions prend beaucoup de temps à s'exécuter, toutes les instructions suivantes sont suspendues jusqu'à ce que cette instruction/bloc d'instructions se termine. Cela est connu sous le nom de `BLOCKING`. Pour éviter le blocage, un programme doit être multi-thread.

#### Threading

Un thread est un contexte d'exécution, qui est toutes les informations dont un CPU a besoin pour exécuter un flux d'instructions.

Supposons que vous lisiez un livre et que vous souhaitiez faire une pause maintenant, mais que vous souhaitiez pouvoir revenir et reprendre la lecture à l'endroit exact où vous vous êtes arrêté. Une façon d'y parvenir est de noter le numéro de page, le numéro de ligne et le numéro de mot. Ainsi, votre contexte d'exécution pour la lecture d'un livre est ces trois nombres.

Si vous avez une colocataire et qu'elle utilise la même technique, elle peut prendre le livre pendant que vous ne l'utilisez pas et reprendre la lecture là où elle s'est arrêtée. Ensuite, vous pouvez le reprendre et le reprendre là où vous en étiez.

Les threads fonctionnent de la même manière. Un CPU vous donne l'illusion qu'il effectue plusieurs calculs en même temps. Il le fait en passant un peu de temps sur chaque calcul. Il peut le faire car il dispose d'un contexte d'exécution pour chaque calcul.

Tout comme vous pouvez partager un livre avec votre ami, de nombreuses tâches peuvent partager un CPU. Ce processus est appelé multi-threading et il résout le `BLOCKING`. Pour supporter le multi-threading sur le frontend, les web workers ont été créés.

![Image](https://cdn-media-1.freecodecamp.org/images/iSMf2nmgE9KBYdaUbT8fUvcwsYcR13DXyvwi)
_pour plus d'informations sur le threading, visitez [ici](https://en.wikipedia.org/wiki/Thread_(computing)" rel="noopener" target="_blank" title=")._

#### Web Workers

![Image](https://cdn-media-1.freecodecamp.org/images/-TZuLkY4dl1q3ngPdl3bAy-95GDku8xF105H)
_crédit image à [html5schools](http://www.html5schools.com/html5-api-tutorials/webworkers-introduction//" rel="noopener" target="_blank" title=")._

> L'utilisation la plus simple des workers est d'effectuer une tâche coûteuse en calcul sans interrompre l'interface utilisateur. ([Source](https://en.wikipedia.org/wiki/Web_worker))

Les web workers permettent le multi-threading sur le front-end en créant de nouveaux threads d'arrière-plan et en exécutant des scripts en isolation. Par conséquent, les scripts exécutés par les workers doivent être contenus dans des fichiers séparés. Parce que les web workers exécutent des scripts dans des threads isolés, les scripts n'interfèrent pas avec le thread principal et, par conséquent, n'interrompent pas l'UI.

#### **Création d'un Web Worker**

À des fins didactiques, le script extrait ci-dessous doit être exécuté dans un thread séparé.

```js
### fetch.js

self.addEventListener('message',  e => {
    let url = e.data;
    
    fetch(url).then(res => {
        if (res.ok) {
            self.postMessage(res);
        } else {
            throw new Error('error with server');
        }
    }).catch(err => {
        self.postMessage(err.message);
    });
})
```

> L'appel du constructeur `[Worker()](https://www.w3.org/TR/workers/#dom-worker)` crée un worker et retourne un objet `[Worker](https://www.w3.org/TR/workers/#worker)` représentant ce worker, qui est utilisé pour communiquer avec le worker.

```js
let worker = new Worker('fetch.js');
```

Le constructeur prend le nom du script comme argument. Si le fichier spécifié existe, le worker crée un nouveau thread, puis télécharge et exécute complètement le script. Si le fichier est indisponible, le worker échoue silencieusement.

#### **Utilisation des Web Workers**

Les web workers communiquent avec le thread parent (le créateur du worker) en utilisant un modèle d'[événement](https://developer.mozilla.org/en-US/docs/Web/Events) et des messages. Il utilise des objets `[MessagePort](http://www.w3.org/TR/webmessaging/#message-ports)` en arrière-plan et prend donc en charge toutes les mêmes fonctionnalités, telles que l'envoi de données structurées et le transfert de données binaires.

Pour recevoir des messages d'un worker, utilisez le gestionnaire d'événements `[onmessage](https://www.w3.org/TR/workers/#handler-worker-onmessage)` sur l'objet `Worker`.

```js
worker.onmessage = (e) => { // block statements }
```

Vous pouvez également utiliser la méthode `addEventListener`.

```js
worker.addEventListener('message', (e) => { // block statements })
```

Pour recevoir un message à l'intérieur du worker, la méthode du gestionnaire d'événements `onmessage` est utilisée.

```js
onmessage = (e) => { // blocks of statements }
```

Vous pouvez également utiliser une méthode `addEventListener` comme exemplifié dans `fetch.js`.

Pour envoyer des données à et depuis un worker, utilisez la méthode `[postMessage()](https://www.w3.org/TR/workers/#dom-worker-postmessage)`. Des données structurées telles que du texte et du JSON peuvent être envoyées via ce canal de communication. Lisez plus sur les types de données pris en charge par `messagePort` [ici](https://www.html5rocks.com/en/tutorials/workers/basics/#toc-transferrables).

```js
worker.postMessage('some-lousy-data');
// dans le thread parent

self.postMessage('some-resulting-data');
// dans le thread du worker.
```

Cette limitation particulière de passage de messages est en place pour un certain nombre de raisons : elle maintient le worker enfant en cours d'exécution de manière sécurisée (puisqu'il ne peut pas, de manière flagrante, affecter un script parent) et elle maintient le thread de la page parent sécurisé (avoir le DOM thread-safe serait un cauchemar logistique pour les développeurs de navigateurs).

#### **Terminer un worker et gérer les erreurs**

Si vous devez terminer immédiatement un worker en cours d'exécution depuis le thread principal, vous pouvez le faire en appelant la méthode terminate du worker :

```js
worker.terminate();
```

Dans le thread du worker, les workers peuvent se fermer eux-mêmes en appelant leur propre méthode close :

```js
close();
```

Le thread du worker est tué immédiatement sans avoir la possibilité de compléter ses opérations ou de nettoyer après lui-même.

Les erreurs d'exécution peuvent être gérées en écoutant explicitement un événement d'erreur qui pourrait être déclenché par l'objet `Worker`.

```js
worker.addEventListener('error', (e) => { // block of statements })
```

#### **Limitations des Web Workers**

1. Tous les scripts de web workers doivent être servis depuis le même domaine.
2. Vous ne pouvez pas avoir un accès direct au DOM et au document global.
3. L'objet window expose une API limitée. Par exemple, les objets `location`, `navigator` et `XMLHttpRequest`.
4. Accès local restreint. Les web workers ne fonctionnent pas sur les fichiers statiques. Par exemple, `file://my/file/on/my/computer`.

Si vous utilisez un worker pour gérer une tâche qui doit finalement mettre à jour l'interface utilisateur principale, vous devrez utiliser le système de messagerie pour passer les données entre le worker et l'application principale. L'application principale est alors responsable de la mise à jour de l'UI.

De même, si votre worker a besoin d'accéder à des données provenant du document, de la fenêtre ou des objets parents, vous devrez les envoyer dans l'appel `postMessage()` qui est utilisé pour démarrer le worker.

#### Conclusion

La création de web workers générera de vrais threads au niveau du système d'exploitation qui consomment des ressources système. Soyez simplement conscient que cela affectera les performances de l'ordinateur entier de l'utilisateur, et pas seulement le navigateur web. À ce titre, les web workers doivent être utilisés de manière responsable et fermés lorsqu'ils ne sont plus utilisés pour libérer des ressources pour d'autres applications.

L'utilisation de web workers peut avoir un impact significatif sur les performances des applications web ; et des applications plus réactives ont un bon effet sur l'expérience utilisateur.

Pour des informations plus approfondies sur les web workers, telles que l'importation de scripts dans les workers et les portées des web workers, veuillez visiter [MDN](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers) ou [WHATWG](https://www.w3.org/TR/workers/).

Pour un exemple entièrement fonctionnel de web workers, visitez [ici](https://github.com/DannyMcwaves/web-workers).