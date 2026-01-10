---
title: Comment implémenter le multi-threading dans Node.js avec les Worker Threads
  [Guide complet]
subtitle: ''
author: Sumit Saha
co_authors: []
series: null
date: '2025-10-24T16:30:57.309Z'
originalURL: https://freecodecamp.org/news/how-to-implement-multi-threading-in-nodejs-with-worker-threads-full-handbook
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1761323431527/d74eb2ba-edaa-4d19-a041-364e99a705ba.png
tags:
- name: Node.js
  slug: nodejs
- name: multithreading
  slug: multithreading
- name: Worker Thread
  slug: worker-thread
- name: workers
  slug: workers
- name: handbook
  slug: handbook
seo_title: Comment implémenter le multi-threading dans Node.js avec les Worker Threads
  [Guide complet]
seo_desc: 'JavaScript is a single-threaded programming language, and Node.js is the
  runtime environment for JavaScript. This means that JavaScript essentially runs
  within Node.js, and all operations are handled through a single thread.

  But when we perform tasks...'
---

JavaScript est un langage de programmation monothread, et Node.js est l'environnement d'exécution (runtime) pour JavaScript. Cela signifie que JavaScript s'exécute essentiellement au sein de Node.js et que toutes les opérations sont gérées via un seul thread.

Mais lorsque nous effectuons des tâches qui nécessitent un traitement intensif, les performances de Node.js peuvent commencer à décliner. Beaucoup de gens pensent à tort que Node.js n'est pas performant ou que JavaScript présente des défauts. Mais il existe en réalité une solution. JavaScript peut également être utilisé efficacement avec le multi-threading.

Dans cet article, nous nous concentrerons sur le backend : plus précisément, comment implémenter le multi-threading côté serveur en utilisant Node.js.

## **Voici ce que nous allons aborder**

1. [Prérequis](#heading-prequis)
    
2. [Configuration du projet avec ExpressJS](#heading-configuration-du-projet-avec-expressjs)
    
    * [1\. Créer un nouveau dossier de projet](#heading-1-creer-un-nouveau-dossier-de-projet)
        
    * [2\. Initialiser un projet Node.js](#heading-2-initialiser-un-projet-nodejs)
        
    * [3\. Installer Express.js](#heading-3-installer-expressjs)
        
    * [4\. Optionnel : Installer Nodemon pour le développement](#heading-4-optionnel-installer-nodemon-pour-le-developpement)
        
    * [5\. Créer le fichier serveur principal](#heading-5-creer-le-fichier-serveur-principal)
        
    * [6\. Exécuter le projet](#heading-6-executer-le-projet)
        
3. [Comprendre le problème](#heading-comprendre-le-probleme)
    
    * [Observer le comportement](#heading-observer-le-comportement)
        
    * [Pourquoi cela arrive-t-il ?](#heading-pourquoi-cela-arrive-t-il)
        
4. [Comprendre l'exécution de JavaScript](#heading-comprendre-lexecution-de-javascript)
    
    * [Comment fonctionne Libuv](#heading-comment-fonctionne-libuv)
        
    * [Nature asynchrone de Node.js](#heading-nature-asynchrone-de-nodejs)
        
5. [Le problème d'utilisation intensive du CPU](#heading-le-probleme-dutilisation-intensive-du-cpu)
    
6. [Comment implémenter les Worker Threads](#heading-comment-implementer-les-worker-threads)
    
    * [Communication entre les threads](#heading-communication-entre-les-threads)
        
    * [Configuration de la communication des workers](#heading-configuration-de-la-communication-des-workers)
        
7. [Comment optimiser avec plusieurs cœurs](#heading-comment-optimiser-avec-plusieurs-coeurs)
    
    * [Vérifier le nombre de cœurs de votre système](#heading-verifier-le-nombre-de-coeurs-de-votre-systeme)
        
    * [Utiliser plusieurs cœurs pour une exécution plus rapide](#heading-utiliser-plusieurs-coeurs-pour-une-execution-plus-rapide)
        
8. [Comment implémenter l'optimisation multi-cœur](#heading-comment-implementer-loptimisation-multi-coeur)
    
    * [Comprendre le code ligne par ligne](#heading-comprendre-le-code-ligne-par-ligne)
        
    * [Planification et configuration des threads](#heading-planification-et-configuration-des-threads)
        
    * [Diviser le travail entre plusieurs workers](#heading-diviser-le-travail-entre-plusieurs-workers)
        
    * [Gérer des tâches complexes](#heading-gerer-des-taches-complexes)
        
9. [Comparaison des performances](#heading-comparaison-des-performances)
    
    * [Résultats des tests](#heading-resultats-des-tests)
        
    * [Métriques de performance](#heading-metriques-de-performance)
        
    * [Points clés à retenir](#heading-points-cles-a-retenir)
        
10. [Résumé](#heading-resume)
    
    * [Le défi du multi-cœur](#heading-le-defi-du-multi-coeur)
        
    * [Découvrir les cœurs disponibles](#heading-decouvrir-les-coeurs-disponibles)
        
    * [Création asynchrone de workers](#heading-creation-asynchrone-de-workers)
        
    * [Stratégie d'implémentation multi-thread](#heading-strategie-dimplementation-multi-thread)
        
    * [Récapitulatif des concepts clés](#heading-recapitulatif-des-concepts-cles)
        
    * [Ce que nous avons appris](#heading-ce-que-nous-avons-appris)
        
11. [Mot de la fin](#heading-mot-de-la-fin)
    
12. [Ressources supplémentaires](#heading-ressources-supplementaires)
    

## **Prérequis**

Pour suivre ce guide et en tirer le meilleur parti, vous devriez avoir :

1. Des connaissances de base en JavaScript (style ES6)
    
2. Une familiarité avec les fondamentaux de Node.js
    
3. Des bases sur les serveurs web utilisant Express (ou similaire)
    
4. Une compréhension des opérations bloquantes vs non bloquantes dans Node.js / JavaScript
    
5. Une aisance avec le code asynchrone (Promises / async/await) et la gestion basée sur les événements
    
6. La capacité de configurer un environnement de développement simple avec Node.js
    

J'ai également créé une vidéo pour accompagner cet article. Si vous préférez apprendre par la vidéo autant que par le texte, vous pouvez la consulter ici :

%[https://www.youtube.com/watch?v=JTl6tQ4bqYA] 

## Configuration du projet avec ExpressJS

Dans cette section, nous allons passer en revue une configuration détaillée et accessible aux débutants pour un projet Node.js utilisant [Express](https://expressjs.com/). Ce guide explique chaque étape, de sorte que même si vous débutez avec Node.js, vous puissiez suivre facilement.

### 1\. Créer un nouveau dossier de projet

Commencez par créer un nouveau dossier pour votre projet. Ouvrez votre terminal ou invite de commande et exécutez :

```powershell
mkdir node-worker-threads
cd node-worker-threads
```

* `mkdir node-worker-threads` : Cette commande crée un nouveau dossier nommé `node-worker-threads`.
    
* `cd node-worker-threads` : Vous déplace dans le dossier nouvellement créé où tous les fichiers du projet seront stockés.
    

Considérez ce dossier comme la maison de votre projet.

### 2\. Initialiser un projet Node.js

Chaque projet Node.js a besoin d'un fichier `package.json` pour gérer les dépendances et les scripts. Exécutez :

```powershell
npm init -y
```

* `npm init` crée un fichier `package.json`.
    
* Le drapeau `-y` remplit automatiquement les valeurs par défaut, vous faisant gagner du temps.
    

Après cela, vous verrez un fichier `package.json` dans votre dossier de projet. Ce fichier assure le suivi de tous les packages et configurations.

### 3\. Installer Express.js

Express est un Framework web léger pour Node.js. Installez-le avec :

```powershell
npm install express
```

Cela ajoute Express à votre projet et vous permet de créer des routes, de gérer les requêtes et d'envoyer des réponses facilement.

### 4\. Optionnel : Installer Nodemon pour le développement

Nodemon redémarre automatiquement votre serveur chaque fois que vous apportez des modifications. C'est très utile pendant le développement.

```powershell
npm install -D nodemon
```

Le drapeau `-D` installe Nodemon en tant que dépendance de développement.

Ensuite, mettez à jour les scripts du `package.json` :

```json
{
  "scripts": {
    "dev": "nodemon index.js"
  }
}
```

Vous pouvez maintenant démarrer le serveur avec :

```powershell
npm run dev
```

Cela redémarrera automatiquement votre serveur à chaque modification du code.

### 5\. Créer le fichier serveur principal

Créez un fichier appelé `index.js`. Ce sera le point d'entrée principal de votre application :

```powershell
touch index.js
```

Ouvrez `index.js` et ajoutez le code suivant :

```javascript
// index.js 

const express = require("express");

const app = express();
const port = process.env.PORT || 3000;

// Route non bloquante
app.get("/non-blocking", (req, res) => {
  res.status(200).send("Cette page est non bloquante.");
});

// Route bloquante utilisant les Worker Threads
app.get("/blocking", (req, res) => {
  let result = 0;
  for (let i = 0; i < 1000000000; i++) {
    result++;
  }
  res.status(200).send(`Le résultat est ${result}`);
});

// Démarrer le serveur
app.listen(port, () => {
  console.log(`Application à l'écoute sur le port ${port}`);
});
```

Voici ce qui se passe dans ce code :

* `express` : Pour créer le serveur.
    
* `Worker` : Pour exécuter des tâches intensives pour le CPU dans un thread séparé.
    
* Route `/non-blocking` : Envoie une réponse rapide immédiatement.
    
* Route `/blocking` : Exécute un thread Worker pour gérer un calcul lourd.
    
* `app.listen` : Démarre le serveur sur le port 3000 (ou le port d'environnement).
    

Ne vous inquiétez pas si tout n'est pas parfaitement clair pour le moment. Nous explorerons tout plus en détail au fur et à mesure. Préparez-vous, car nous allons décomposer chaque partie étape par étape de la manière la plus simple possible.

### 6\. Exécuter le projet

Démarrez le serveur en utilisant Nodemon :

```powershell
npm run dev
```

Ou sans Nodemon :

```powershell
node index.js
```

Visitez ces URL dans votre navigateur :

* [`http://localhost:3000/non-blocking`](http://localhost:3000/non-blocking) affiche un message simple non bloquant.
    
* [`http://localhost:3000/blocking`](http://localhost:3000/blocking) exécute une tâche intensive pour le CPU en utilisant les Worker Threads.
    

**Félicitations !** Votre projet Node.js avec Express est entièrement configuré et prêt pour le développement.

## Comprendre le problème

Nous avons déjà configuré une application Express.js de base, qui est essentiellement une application Node.js. Dans cette application, nous avons défini **deux routes** :

1. `/non-blocking`
    
2. `/blocking`
    

La route `/non-blocking` est simple : elle renvoie simplement une réponse textuelle disant : "Cette page est non bloquante."

D'un autre côté, la route `/blocking` contient un calcul lourd. Elle exécute une boucle jusqu'à un milliard, calcule la somme de tous ces nombres, puis renvoie le résultat.

Enfin, l'application est configurée pour s'exécuter sur le port 3000 via `app.listen`.

### Observer le comportement

Si vous ouvrez votre navigateur et visitez l'URL [`http://localhost:3000/non-blocking`](http://localhost:3000/non-blocking), elle fonctionne parfaitement et répond immédiatement.

![Navigateur non bloquant](https://cdn.hashnode.com/res/hashnode/image/upload/v1761079165626/6d6a3c24-8095-4243-83db-8a44865e5af9.png align="center")

Mais si vous visitez l'URL [`http://localhost:3000/blocking`](http://localhost:3000/blocking), la page continue de charger et ne répond pas tout de suite.

Ce qui est encore plus intéressant, c'est que si vous essayez d'accéder à [`http://localhost:3000/non-blocking`](http://localhost:3000/non-blocking) **pendant** que `/blocking` est toujours en cours d'exécution, elle devient également insensible.

Cela démontre un concept clé : tant que la route `/blocking` est en cours d'exécution, même la route `/non-blocking` ne peut pas répondre. En d'autres termes, le calcul lourd dans `/blocking` **bloque la boucle d'événements (event loop) de Node.js**, affectant toutes les autres routes.

![Navigateur bloqué](https://cdn.hashnode.com/res/hashnode/image/upload/v1761079338040/ecaf458e-d91a-4752-863e-71ac34081949.gif align="center")

### Pourquoi cela arrive-t-il ?

La raison réside dans le fonctionnement de Node.js. Node.js est essentiellement un environnement d'exécution JavaScript, et comme nous le savons, JavaScript est un langage de programmation **monothread**. Naturellement, Node.js s'exécute également sur un seul thread par défaut.

![Programmation monothread](https://cdn.hashnode.com/res/hashnode/image/upload/v1761079437967/3330b62c-54c2-41a9-bccc-8f962e71287c.gif align="center")

Alors, d'où vient le problème ? Lorsque vous exécutez la route `/blocking`, tout le code JavaScript s'exécute sur le **thread principal**. Pendant ce temps, le thread principal est complètement occupé ou bloqué. Par conséquent, si un autre utilisateur tente d'accéder à la route `/non-blocking`, il n'obtiendra aucune réponse car le thread principal est toujours occupé par la tâche précédente.

C'est pourquoi beaucoup de gens pensent à tort que JavaScript est faible parce qu'il est monothread. Mais cette perception n'est pas tout à fait exacte. Avec la bonne approche et les bonnes techniques, JavaScript **peut également être utilisé de manière multi-thread**, vous permettant de gérer des calculs lourds sans bloquer d'autres opérations.

![JS Faible](https://cdn.hashnode.com/res/hashnode/image/upload/v1761079547228/0799f826-3715-4664-b94b-e8f2e80afd04.gif align="center")

## **Comprendre l'exécution de JavaScript**

Réfléchissons au thread principal où JavaScript s'exécute principalement. Vous pourriez vous demander, où exactement JavaScript s'exécute-t-il ? JavaScript s'exécute à l'intérieur du **moteur JavaScript**, qui est responsable de la conversion du code JavaScript en code machine.

Dans le cas de Node.js, il s'exécute sur le **moteur V8**, qui est le même moteur utilisé dans Google Chrome. Le moteur V8 fonctionne entièrement sur un seul thread, ce qui signifie que tout le code JavaScript s'exécute dans un seul thread principal.

Maintenant, vous pourriez vous demander : existe-t-il des threads autres que le thread principal ? La réponse est oui. En dehors du thread principal, il existe des threads supplémentaires utilisés pour gérer différents types de tâches. La gestion et l'implémentation de ces threads sont assurées par une bibliothèque spéciale appelée **Libuv**.

![Comprendre l'exécution de JavaScript](https://cdn.hashnode.com/res/hashnode/image/upload/v1761079628895/02bc21f7-1d49-4952-9c17-3f57cbbe3488.gif align="center")

### Comment fonctionne Libuv

Libuv est conçu pour fonctionner aux côtés du moteur V8. Tandis que le moteur V8 exécute le code JavaScript sur le thread principal, des threads supplémentaires sont utilisés pour gérer différents types de tâches. Par exemple, des opérations telles que les requêtes de base de données, les requêtes réseau ou les tâches de lecture/écriture de fichiers sont gérées par ces threads supplémentaires, et la bibliothèque Libuv les gère et les coordonne.

Chaque fois que nous effectuons de telles tâches, elles sont en réalité exécutées sur ces threads supplémentaires en dehors du thread principal. Libuv indique au moteur V8 comment gérer ces tâches efficacement. Ces tâches sont communément appelées **opérations d'Entrée/Sortie**, ou opérations I/O en abrégé. En d'autres termes, lors de l'exécution de lecture/écriture de fichiers, de requêtes de base de données ou de requêtes réseau, ces opérations I/O sont exécutées sur des threads séparés sans bloquer le thread principal.

Mais si nous avons des tâches comme une grande boucle `for` dans notre exemple précédent, ou toute opération qui nécessite principalement un **traitement CPU**, elles ne relèvent pas des opérations I/O. Dans de tels cas, la tâche doit être exécutée sur le thread principal, ce qui le bloque inévitablement jusqu'à ce que la tâche soit terminée.

![Comment fonctionne libuv](https://cdn.hashnode.com/res/hashnode/image/upload/v1761079720366/9f01e68c-ad5f-491a-9e68-d91a4ec5f3fb.gif align="center")

### **Nature asynchrone de Node.js**

Considérez un scénario où un client envoie une requête au thread principal, et cette requête nécessite l'exécution d'une requête de base de données.

Lorsque l'utilisateur envoie une telle requête, la requête de base de données est envoyée à la base de données, mais surtout, elle **ne bloque pas** le thread principal. Au lieu de cela, Libuv gère la requête de base de données sur un **thread séparé**, laissant le thread principal libre de gérer d'autres tâches.

Dans cette situation, si un autre utilisateur envoie une requête qui n'implique aucune requête de base de données ou opération I/O, elle peut être exécutée immédiatement sur le thread principal. En conséquence, ce second utilisateur reçoit une réponse sans aucun délai.

Une fois que la requête de base de données s'exécutant sur le thread séparé est terminée, le résultat est renvoyé au thread principal, qui le renvoie ensuite sous forme de réponse à l'utilisateur d'origine. Cette approche garantit que les utilisateurs reçoivent leur résultat efficacement et que le thread principal reste disponible pour d'autres tâches.

Tout ce processus représente la **nature asynchrone** de JavaScript et de Node.js. Les tâches ne sont pas exécutées de manière synchrone – au lieu de cela, elles s'exécutent de manière asynchrone. La requête d'un utilisateur peut être traitée sur un thread séparé pendant que d'autres utilisateurs continuent d'interagir avec le serveur de manière fluide. C'est ainsi que Node.js maintient des performances et une réactivité élevées, même sous de multiples requêtes simultanées.

![Nature asynchrone de Node.js](https://cdn.hashnode.com/res/hashnode/image/upload/v1761079806477/dd7b58e2-48ab-4994-ad09-41fad2f0b78b.gif align="center")

### **Le problème d'utilisation intensive du CPU**

Ainsi, c'est ainsi que tout fonctionne efficacement. Maintenant, la question est : que se passe-t-il si le thread principal a une tâche qui ne nécessite aucun accès à la base de données pour la requête d'un utilisateur mais exige un traitement CPU intensif ? Dans ce cas, le thread principal sera bloqué.

Disons qu'une tâche sur le thread principal consomme beaucoup de CPU. Si nous l'exécutons directement sur le thread principal, la boucle d'événements sera bloquée et les autres requêtes ne pourront pas être traitées.

C'est là que les **worker threads** entrent en jeu dans Node.js. Avec les worker threads, nous pouvons lancer un nouveau thread en dehors du thread principal pour gérer séparément les opérations lourdes pour le CPU. En conséquence, le thread principal reste libre, permettant aux autres requêtes d'être traitées immédiatement.

En d'autres termes, en utilisant des worker threads, nous pouvons exécuter des tâches **liées au CPU (CPU-bound)** de manière **asynchrone**, garantissant que le débit et la réactivité du serveur ne sont pas affectés.

![Problème CPU intensif](https://cdn.hashnode.com/res/hashnode/image/upload/v1761079890972/98686661-0c5f-493e-a0b4-25c744c60938.gif align="center")

## **Comment implémenter les Worker Threads**

Si nous jetons un coup d'œil à notre fichier `index.js` précédent, la tâche dans le gestionnaire de route `/blocking` s'exécute entièrement sur le thread principal, c'est pourquoi elle provoque un blocage. Alors, comment pouvons-nous résoudre ce problème ? La solution consiste à utiliser le module intégré de worker threads de Node.js.

Il n'est **pas nécessaire d'installer de package externe**, car les worker threads sont un module de base de Node.js.  
Nous pouvons directement importer la classe `Worker` du module `worker_threads` et créer un nouveau worker thread.

```javascript
// index.js

const express = require("express");
const { Worker } = require("worker_threads");

const app = express();
const port = process.env.PORT || 3000;

// Route non bloquante
app.get("/non-blocking", (req, res) => {
  res.status(200).send("Cette page est non bloquante.");
});

// Route bloquante utilisant les Worker Threads
app.get("/blocking", (req, res) => {
  const worker = new Worker("./worker.js");

  let result = 0;
  for (let i = 0; i < 1000000000; i++) {
    result++;
  }
  res.status(200).send(`Le résultat est ${result}`);
});

// Démarrer le serveur
app.listen(port, () => {
  console.log(`Application à l'écoute sur le port ${port}`);
});
```

Comment ça marche :

* À l'intérieur du gestionnaire de route `/blocking`, nous créons un nouveau worker en utilisant `new Worker()` et fournissons un chemin de fichier.
    
* Ce fichier (`worker.js`) contient la tâche **lourde pour le CPU** que nous voulons que le worker exécute.
    
* Par exemple, notre boucle `for` lourde est déplacée dans ce fichier séparé.
    

Nous créons un nouveau fichier nommé `worker.js` et y collons la boucle :

```javascript
// worker.js

for (let i = 0; i < 1000000000; i++) {
  result++;
}
```

Lorsque nous passons le chemin vers `worker.js` lors de la création du Worker, Node.js démarre un nouveau thread.

Ce nouveau thread exécute la tâche intensive pour le CPU de manière indépendante, gardant le thread principal libre pour gérer d'autres requêtes entrantes.

En faisant cela, l'application devient plus réactive et peut gérer plusieurs requêtes sans blocage.

### Communication entre les threads

Dans Node.js, nous avons le thread principal et des worker threads supplémentaires. Pour coordonner les tâches entre eux, nous pouvons utiliser un **système de messagerie**. Essentiellement, tous les résultats doivent éventuellement atteindre le thread principal. Sinon, nous ne pourrons fournir aucun résultat à l'utilisateur.

Par exemple, supposons que vous attribuiez une tâche au Thread B et une autre tâche au Thread C. Lorsque ces threads terminent leurs tâches, ils doivent en informer le thread principal. Ils le font en envoyant des messages via le système de messagerie.

Pensez-y comme à l'échange de messages dans une boîte de réception : le Thread C envoie un message directement au thread principal une fois sa tâche terminée. Grâce à cette communication, les worker threads informent le thread principal de l'achèvement de la tâche et envoient toutes les données nécessaires.

C'est exactement le mécanisme que nous utiliserons dans notre exemple pour gérer les tâches lourdes pour le CPU avec des worker threads, garantissant que le thread principal reste libre et réactif.

![Communication entre les threads](https://cdn.hashnode.com/res/hashnode/image/upload/v1761079966779/34f22f5e-9334-4e89-b54f-71de3de90923.gif align="center")

### Configuration de la communication des workers

Nous avons donc créé un fichier `worker.js`. Maintenant, la question est : comment informer le thread principal que la tâche est terminée dans ce fichier ?

Pour y parvenir, nous extrayons `parentPort` du module intégré `worker_threads` de Node.js. Le `parentPort` est un objet spécial qui permet la communication **entre le worker thread et le thread principal**. Il agit comme un pont : chaque fois que le worker termine une tâche, il peut renvoyer le résultat au thread principal via ce canal.

Une fois la tâche terminée, nous utilisons la méthode `parentPort.postMessage(result)` pour envoyer les données finales. En d'autres termes, nous postons un message au thread parent, et dans notre cas, ce message est le résultat calculé de notre boucle.

Voici le code complet du fichier `worker.js` :

```javascript
// worker.js

const { parentPort } = require("worker_threads");

let result = 0;
for (let i = 0; i < 10000000000; i++) {
  result++;
}

parentPort.postMessage(result);
```

Dans cet exemple :

* Nous importons `parentPort` depuis `worker_threads`.
    
* Nous effectuons une tâche lourde – une boucle qui compte jusqu'à 10 milliards.
    
* Après avoir terminé la boucle, nous renvoyons le résultat au thread principal en utilisant `parentPort.postMessage(result)`.
    

C'est ainsi que la communication entre le worker thread et le thread principal a lieu dans Node.js.

Maintenant, la question est : une fois que nous avons envoyé les données depuis le worker, comment les **recevons-nous** dans le gestionnaire `/blocking` de notre fichier `index.js` ?

Pour ce faire, nous devons configurer un **écouteur (listener)** à l'intérieur du gestionnaire. Pour cela, nous utilisons la méthode `worker.on()`.

Alors, qu'écoutons-nous exactement ? Nous écoutons l'événement `"message"` – tout comme nous écoutons `onClick` ou d'autres événements en JavaScript.

Le premier paramètre de `worker.on()` est le nom de l'événement (`"message"`), et le second paramètre est une **fonction de rappel (callback)**. À l'intérieur de ce callback, le premier argument représente les données que nous recevons du worker.

Une fois que nous recevons les données, nous pouvons les renvoyer au navigateur sous forme de réponse en utilisant :

```javascript
// index.js 

// À l'intérieur du gestionnaire de route `/blocking`, nous écoutons les messages du worker thread.
// Chaque fois que le worker termine sa tâche et envoie un message, 
// le callback reçoit les données via le paramètre `data`.
// Nous renvoyons ensuite ces données au client sous forme de réponse HTTP avec le code d'état 200.

worker.on("message", (data) => {
  res.status(200).send(`Le résultat est ${data}`);
});
```

**Explication :**

* `worker.on("message", callback)` écoute les messages envoyés par le worker thread via `parentPort.postMessage()`.
    
* Le paramètre `data` contient le résultat envoyé par le worker.
    
* En utilisant `res.status(200).send(...)`, nous renvoyons le résultat calculé au navigateur.
    
* Cela permet au calcul lourd de se produire dans un thread séparé, gardant le thread principal libre et réactif.
    

En même temps, nous devrions également gérer les erreurs possibles.

Si une erreur survient à l'intérieur du worker, nous pouvons l'écouter en utilisant l'événement **"error"** de la même manière :

```javascript
// index.js 

// Dans le gestionnaire de route `/blocking`, nous écoutons toutes les erreurs qui surviennent dans le worker thread.
// Si une erreur survient, le callback reçoit l'objet d'erreur `err`,
// et nous le renvoyons sous forme de réponse HTTP avec le code d'état 400.

worker.on("error", (err) => {
  res.status(400).send(`Une erreur est survenue : ${err}`);
});
```

**Explication :**

* `worker.on("error", callback)` écoute spécifiquement les erreurs à l'intérieur du worker thread.
    
* Le paramètre `err` contient des détails sur ce qui s'est mal passé dans le worker.
    
* En utilisant `res.status(400).send(...)`, nous renvoyons l'erreur au client afin que la requête ne reste pas suspendue silencieusement.
    

**Voici à quoi ressemble le code complet :**

```javascript
// index.js

const express = require("express");
const { Worker } = require("worker_threads");

const app = express();
const port = process.env.PORT || 3000;

// Route non bloquante
app.get("/non-blocking", (req, res) => {
  res.status(200).send("Cette page est non bloquante.");
});

// Route bloquante utilisant les worker threads
app.get("/blocking", (req, res) => {
  const worker = new Worker("./worker.js");

  worker.on("message", (data) => {
    res.status(200).send(`Le résultat est ${data}`);
  });

  worker.on("error", (err) => {
    res.status(400).send(`Une erreur est survenue : ${err}`);
  });
});

// Démarrer le serveur
app.listen(port, () => {
  console.log(`Application à l'écoute sur le port ${port}`);
});
```

Une fois cela configuré, vous verrez un changement spectaculaire. La route `/blocking` charge, mais même pendant qu'elle charge, rafraîchir à plusieurs reprises la route `/non-blocking` fonctionne parfaitement sans aucun problème !

![Configuration de la communication des workers](https://cdn.hashnode.com/res/hashnode/image/upload/v1761080061445/f1f213c7-6cce-4334-81e5-8cd828682f8e.gif align="center")

Remarquez maintenant que la route `/non-blocking` est accessible, ce qui signifie que même si la route `/blocking` est toujours en cours d'exécution, elle n'affecte rien. Nous avons donc résolu ce problème avec succès. Nous avons déplacé la tâche principale vers un thread séparé en dehors du thread principal. Qu'est-ce que cela signifie ? Le thread principal a créé un nouveau worker thread et lui a assigné la tâche lourde pour le CPU. Le nouveau thread travaille maintenant de manière indépendante, tandis que le thread principal reste libre.

Enfin, lorsque le nouveau thread termine sa tâche, il devient également libre. Ensuite, via le système de messagerie, le nouveau thread informe le thread principal : "Vos données sont prêtes, voici vos données." Le thread principal reçoit ces données et les envoie au client sous forme de réponse.

Par conséquent, les tâches qui étaient automatiquement gérées sur des threads séparés pour les requêtes de base de données ou les opérations de lecture-écriture de fichiers – parce qu'il s'agissait d'opérations I/O – nous avons maintenant initié manuellement un thread et l'avons utilisé pour gérer des tâches CPU intensives similaires.

![Opérations IO](https://cdn.hashnode.com/res/hashnode/image/upload/v1761080131679/148cc279-e4f0-4f68-b2a9-34110abcbc90.gif align="center")

## Comment optimiser avec plusieurs cœurs

Maintenant que vous avez une compréhension claire du fonctionnement du processus, allons un peu plus loin et optimisons-le en utilisant plusieurs cœurs de CPU.

Lorsque vous visitez la route `/blocking`, vous remarquerez peut-être qu'elle prend encore un temps considérable pour répondre. Cela indique que l'optimisation n'est pas encore complète. Jusqu'à présent, nous avons utilisé un thread séparé, ce qui signifie que nous avons utilisé **un cœur de CPU** en dehors du thread principal. Mais la plupart des machines modernes possèdent **plusieurs cœurs**, et nous pouvons en tirer parti pour améliorer les performances.

![Index final](https://cdn.hashnode.com/res/hashnode/image/upload/v1761080243361/dddd924c-9138-4790-ac6c-811b39772c6c.gif align="center")

### Vérifier le nombre de cœurs de votre système

Avant d'assigner plusieurs cœurs, vous pouvez vérifier combien de cœurs sont disponibles sur votre système :

* **macOS (basé sur Unix) :**
    
    ```powershell
    sysctl -n hw.ncpu
    ```
    
    Cette commande renvoie le nombre total de cœurs de CPU sur votre machine. Par exemple, sur mon Mac, elle affiche `10`, ce qui signifie que j'ai dix cœurs disponibles.
    
* **Linux :**
    
    ```powershell
    nproc
    ```
    
    Cela affichera le nombre d'unités de traitement disponibles.
    
* **Windows (Invite de commande) :**
    
    ```powershell
    echo %NUMBER_OF_PROCESSORS%
    ```
    

Chacune de ces commandes vous aidera à déterminer combien de cœurs vous pouvez utiliser pour le traitement parallèle.

### Utiliser plusieurs cœurs pour une exécution plus rapide

Une fois que vous connaissez le nombre de cœurs de votre machine, vous pouvez décider combien d'entre eux allouer à une tâche spécifique. Par exemple, comme mon système possède dix cœurs, je pourrais choisir d'utiliser quatre cœurs pour la tâche.

En répartissant la charge de travail sur plusieurs threads (chacun s'exécutant sur son propre cœur), vous pouvez obtenir des améliorations de performance significatives. Au lieu de compter sur un seul cœur, le système peut exécuter plusieurs parties de la tâche simultanément, réduisant ainsi considérablement le temps d'exécution total.

En résumé, plus vous utilisez de cœurs efficacement, plus vos tâches lourdes en calcul peuvent se terminer rapidement (tant que votre code est conçu pour gérer l'exécution parallèle en toute sécurité).

## Comment implémenter l'optimisation multi-cœur

Maintenant, nous allons optimiser la tâche `/blocking` en utilisant plusieurs worker threads. Tout d'abord, nous allons créer des copies de nos fichiers existants :

* `index.js` → `index-optimized.js`
    
* `worker.js` → `worker-optimized.js`
    

Nous prévoyons d'utiliser quatre threads. Même si la machine peut avoir plus de cœurs, les utiliser tous pourrait surcharger le système, nous allons donc limiter à quatre.

**index-optimize.js :**

```javascript
// index-optimize.js

const express = require("express");
const { Worker } = require("worker_threads");

const app = express();
const port = process.env.PORT || 3000;
const THREAD_COUNT = 4;

function createWorker() {
    return new Promise((resolve, reject) => {
        const worker = new Worker("./worker-optimized.js", {
            workerData: {
                thread_count: THREAD_COUNT,
            },
        });

        worker.on("message", (data) => {
            resolve(data);
        });

        worker.on("error", (err) => {
            reject(`Une erreur est survenue : ${err}`);
        });
    });
}

app.get("/non-blocking", (req, res) => {
    res.status(200).send("Cette page est non bloquante.");
});

app.get("/blocking", async (req, res) => {
    const workerPromise = [];

    for (let i = 0; i < THREAD_COUNT; i++) {
        workerPromise.push(createWorker());
    }

    const threadResults = await Promise.all(workerPromise);
    const total =
        threadResults[0] +
        threadResults[1] +
        threadResults[2] +
        threadResults[3];

    res.status(200).send(`Le résultat est ${total}`);
});

app.listen(port, () => {
    console.log(`Application à l'écoute sur le port ${port}`);
});
```

Ici, nous créons une fonction `createWorker` qui renvoie une Promise. À l'intérieur, le worker est créé, et les événements de message et d'erreur sont gérés. Dans la route `/blocking`, nous créons plusieurs workers de manière asynchrone, attendons qu'ils se terminent tous en utilisant `Promise.all`, puis additionnons les résultats.

**worker-optimize.js :**

```javascript
// worker-optimize.js

const { parentPort, workerData } = require("worker_threads");

let result = 0;
for (let i = 0; i < 10000000000 / workerData.thread_count; i++) {
    result++;
}

parentPort.postMessage(result);
```

Chaque worker reçoit `thread_count` du thread principal et calcule sa partie de la tâche. Une fois terminé, il renvoie le résultat en utilisant `parentPort.postMessage`. De cette façon, le calcul lourd est distribué et le thread principal reste libre.

### Comprendre le code ligne par ligne

D'accord, certains de ces concepts peuvent sembler un peu complexes au début. Mais ne vous inquiétez pas ! Nous allons parcourir tout le code ligne par ligne, en expliquant tout en détail afin que vous compreniez exactement ce qui se passe et pourquoi.

### Planification et configuration des threads

Maintenant, pour en venir au point principal, nous allons utiliser des threads, n'est-ce pas ? Nous avons prévu d'utiliser plusieurs threads. Disons que nous avons décidé d'utiliser quatre threads. Notre machine possède dix cœurs, mais nous ne les utiliserons pas tous car cela consommerait toutes nos ressources système. Nous utiliserons donc quatre threads provenant de quatre des cœurs disponibles.

Pour cette raison, dans le fichier `index-optimized.js`, nous avons créé une constante pour stocker le nombre de threads que nous utiliserons. Disons que nous l'avons réglé sur 4 ici, afin qu'un autre développeur puisse facilement le modifier plus tard si nécessaire.

#### La fonction createWorker

Ensuite, nous avons créé une nouvelle fonction appelée `createWorker`. Le but de cette fonction est de créer un nouveau Worker. Ici, nous renvoyons une promesse car le processus de création d'un Worker est effectué de manière asynchrone.

C'est parce que lorsque nous créons quatre workers, nous voulons que le processus de création lui-même se produise de manière asynchrone, afin que le thread principal ne soit pas bloqué. Après tout, créer un worker est essentiellement un processus séparé.

La meilleure pratique consiste à créer des workers de manière asynchrone. C'est pourquoi nous avons créé la fonction `createWorker`, qui renvoie une promesse. Comme nous le savons, les événements sont écoutés à l'intérieur d'une promesse, où `resolve` et `reject` sont utilisés. Dans le gestionnaire `/blocking`, nous pouvons gérer le résultat du worker ou toute erreur via cette promesse.

#### Création d'un Worker

Pour créer un worker, nous utilisons :

```javascript
const worker = new Worker("./worker-optimized.js");
```

Ici, nous devons fournir le chemin vers le fichier du Worker. Ensuite, en tant que second paramètre, nous pouvons passer quelques options. Par exemple, si nous voulons envoyer des données au Worker, nous utilisons `{ workerData }`. À l'intérieur de ce `workerData`, nous enverrons le `THREAD_COUNT`, qui est stocké dans notre fichier sous le nom `THREAD_COUNT`.

Par exemple, nous pouvons passer un objet dans `workerData` comme :

```javascript
{
  threadCount: THREAD_COUNT;
}
```

Lorsque ce Worker est en cours de création, nous envoyons certaines propriétés de `index-optimized.js` en tant que `workerData`. C'est parce que dans `worker-optimized.js`, le worker peut utiliser `parentPort` pour savoir combien de threads il doit utiliser. Nous avons donc inclus une propriété `threadCount` dans `workerData`. Lorsque le worker démarre, il lit `threadCount` depuis `workerData` et travaille en conséquence. C'est ainsi que nous avons conçu la fonction `createWorker`, qui renvoie simplement une Promise.

#### Gestion des événements et structure de la promesse

Ici, nous avons apporté un changement important par rapport à notre fichier `index.js` d'origine.

Comme nous avons copié tout le code de `index.js` dans `index-optimized.js`, nous avons ajusté le gestionnaire de route `/blocking`. Plus précisément, nous avons supprimé la création directe du Worker du gestionnaire `/blocking`. Au lieu de cela, le Worker est maintenant créé à l'intérieur de la fonction `createWorker`.

De plus, tous les écouteurs d'événements (`message` et `error`) qui se trouvaient auparavant à l'intérieur du gestionnaire `/blocking` ont également été déplacés dans la fonction `createWorker`. Cela signifie que le worker est entièrement géré au sein de la fonction, et le gestionnaire `/blocking` ne gère désormais que les résultats de la promesse, gardant le thread principal propre et organisé.

Mais comme ces événements sont écoutés à l'intérieur d'une promesse, nous ne pouvons pas envoyer la réponse directement de là. Nous enverrons la réponse à l'intérieur du gestionnaire `/blocking`. Donc, depuis la Promise, nous n'utilisons que `resolve` et `reject`.

**Par exemple :**

```javascript
resolve(`Le résultat est ${data}`);
reject(`Une erreur est survenue ${err}`);
```

En d'autres termes, tout le processus de création d'un worker a été déplacé dans la fonction `createWorker`, qui renvoie finalement une promesse.

### Diviser le travail entre plusieurs workers

Maintenant, à l'intérieur du gestionnaire `/blocking`, j'appelle simplement la fonction `createWorker`. Le `workerData` que nous fournissons indique au worker quelle tâche il doit effectuer. Le worker créé est lié à `parentPort` dans le fichier `worker-optimized.js`, qui communique essentiellement avec le thread parent.

Maintenant, nous voulons diviser la boucle `for` s'exécutant jusqu'à un milliard sur quatre cœurs. Le nombre de cœurs à utiliser est envoyé depuis `index-optimized.js` dans le cadre de `workerData`. Comme cette information se trouve dans `workerData`, les workers peuvent automatiquement diviser et gérer les tâches entre eux.

Ainsi, dans le fichier `worker-optimized.js`, nous obtiendrons le `workerData` en utilisant :

```javascript
{ workerData } = require("worker_threads")
```

Ensuite, dans la condition de la boucle `for`, nous utiliserons `workerData.threadCount`. Cela signifie que le `threadCount` envoyé depuis `index-optimized.js` sera utilisé ici au lieu de coder en dur la valeur 4. C'est une meilleure pratique car les données sont transmises au worker au moment de sa création. Dans `worker-optimized.js`, nous utilisons cela pour diviser le travail en quatre parties. Ensuite, quatre workers seront créés, ce qui signifie que la fonction `createWorker` sera appelée quatre fois. Chaque worker prendra une partie du travail, et à la fin, tous les résultats seront combinés. C'est ainsi que l'ensemble du processus est achevé.

Ainsi, dans ce gestionnaire `/blocking`, notre tâche est de collecter les résultats des quatre promesses puis de les additionner. Disons que nous les stockons dans un tableau appelé `workerPromises`. Chaque entrée de ce tableau contiendra le résultat de la promesse d'un worker. Ensuite, en les combinant tous, nous obtenons le résultat final.

Comme nous devons créer quatre Workers, nous allons exécuter une boucle `for` : `for (let i = 0; i < THREAD_COUNT; i++)`. À l'intérieur du corps de cette boucle, nous appellerons la fonction `createWorker` à chaque fois. Cela signifie qu'à chaque itération, un nouveau worker est créé et sa promesse est poussée dans le tableau `workerPromises`.

Ainsi, à l'intérieur du corps de cette boucle, nous appellerons la fonction `createWorker` quatre fois. Chaque appel à `createWorker` renvoie une promesse. Ces quatre promesses sont poussées dans le tableau `workerPromises`, comme `workerPromises.push(createWorker())`. De cette façon, chaque worker a sa propre promesse. À la fin, comme toutes les promesses sont stockées dans le tableau `workerPromises`, nous pouvons facilement appeler `Promise.all(workerPromises)`.

Ainsi, nous avons utilisé `threadResults = await Promise.all(workerPromises)`. Comme nous le savons, `Promise.all` peut gérer plusieurs Promises ensemble. Ici, nous avons passé le tableau `workerPromises`, donc `threadResults` contiendra les résultats des quatre promesses sous forme d'éléments séparés, comme `threadResults[0]`, `threadResults[1]`, `threadResults[2]` et `threadResults[3]`. Ensuite, nous additionnons ces résultats pour obtenir le calcul total, ce qui signifie que `threadResults[0] + threadResults[1] + threadResults[2] + threadResults[3]` donne le résultat final. Comme nous avons utilisé `await`, toute la fonction doit être `async`.

Une fois que tout est fait correctement, nous pouvons envoyer ce résultat total au client en utilisant `res.status(200).send(Le résultat est ${total})`. De cette façon, le calcul total fonctionne correctement, contrairement à avant.

J'espère donc que c'est clair maintenant : nous avons appelé la fonction `createWorker` quatre fois ici. Chaque appel renvoie une promesse. Nous avons ensuite attendu toutes ces promesses ensemble en utilisant `Promise.all`, de sorte que tous les résultats sont arrivés en même temps. Après cela, nous avons additionné ces résultats. Le gestionnaire `/blocking` est essentiellement celui qui exécute notre travail opérationnel.

### Gérer des tâches complexes

Ainsi, dans le fichier `worker-optimized.js`, nous avons essentiellement divisé le travail en quatre parties. Mais il n'est pas nécessaire que la tâche soit toujours une boucle `for`. Il pourrait également s'agir de différents types de tâches complexes, comme le traitement d'images, le traitement de données ou la pagination.

Dans de tels cas, nous ne pouvons pas toujours suivre le même modèle. Nous devons donc envoyer les données nécessaires depuis `index-optimized.js` en tant que `workerData`, et le worker utilisera ces données pour effectuer la tâche dans un processus séparé.

Dans l'exemple précédent, toutes les étapes étaient séquentielles, donc le simple fait d'additionner les résultats nous a donné le total. Mais dans le cas de tâches complexes, nous devons utiliser un traitement piloté par les données.

Dans d'autres applications complexes, vous pourriez avoir besoin d'effectuer différentes tâches. Mais le concept principal est clair : toute donnée ou propriété que nous envoyons d'ici sera reçue par le worker, qui divisera ensuite le travail. Chaque worker – que vous en utilisiez quatre, cinq ou six – gérera sa partie, et tous les résultats devront être accumulés. C'est essentiellement l'ensemble du processus.

## **Comparaison des performances**

Lorsque vous travaillez avec des tâches gourmandes en CPU dans Node.js, diviser le travail à l'aide de worker threads peut considérablement améliorer les performances. Comparons le comportement de notre application avant et après l'optimisation.

### Résultats des tests

L'exécution du fichier `index.js` et l'accès à la route `/blocking` dans le navigateur prennent un temps considérable.

![Index final](https://cdn.hashnode.com/res/hashnode/image/upload/v1761164273474/02892dd3-3524-4e7e-83fa-ac279910d759.gif align="center")

L'exécution du fichier `index-optimized.js` et l'accès à la même route prennent considérablement moins de temps – environ 3 secondes.

![Optimisé final](https://cdn.hashnode.com/res/hashnode/image/upload/v1761164303764/4ba27180-49f7-4485-a1a5-73f2f419ab9b.gif align="center")

L'arrêter et exécuter à nouveau `index.js` montre clairement que l'implémentation d'origine est plus lente.

![Non optimisé final](https://cdn.hashnode.com/res/hashnode/image/upload/v1761164358090/4c3b9056-b936-4341-9302-461c290ea70e.gif align="center")

### Métriques de performance

| **Fichier** | **Route** | **Temps de réponse approx.** | **Notes** |
| --- | --- | --- | --- |
| `index.js` | `/blocking` | Beaucoup plus long | C'est l'implémentation d'origine. La boucle monothread bloque la boucle d'événements, provoquant des retards. |
| `index-optimized.js` | `/blocking` | Environ 3 secondes | Ici, le travail est divisé en plusieurs worker threads, ce qui rend le processus beaucoup plus rapide. |

### Points clés à retenir

Cette comparaison démontre comment la division du travail en plusieurs parties à l'aide de worker threads peut rendre les tâches gourmandes en CPU beaucoup plus efficaces, en gardant le thread principal réactif et en améliorant les performances globales.

## Résumé

Ainsi, nous avons d'abord vu dans `index.js` comment une tâche bloquante peut être gérée de manière `non bloquante` et asynchrone. C'est-à-dire que nous avons exécuté un worker thread, et grâce à ce worker thread, le thread principal n'a pas été bloqué, permettant aux autres utilisateurs de continuer leurs tâches simultanément.

### Le défi du multi-cœur

Mais le problème est que lorsque nous utilisons un nouveau thread sur le serveur, il n'y a pas qu'un seul cœur. Habituellement, il y a plusieurs cœurs, comme `8`, `16` ou plus. Pour utiliser plusieurs cœurs, nous devons d'abord savoir combien de cœurs sont disponibles sur le serveur.

### Découvrir les cœurs disponibles

Si le serveur est sous Linux, nous pouvons facilement connaître le nombre total de cœurs en utilisant la commande `nproc`. Ensuite, nous pouvons décider combien de cœurs utiliser. Par exemple, disons que nous décidons d'utiliser trois cœurs. Dans `index-optimized.js`, nous avons implémenté un moyen de diviser le travail entre ces cœurs.

### Création asynchrone de workers

Ce que nous avons fait, c'est envelopper le processus de création du worker dans une promesse. Comme la création d'un worker prend un certain temps et que son lancement n'est pas instantané, ce processus est effectué de manière asynchrone. De cette façon, même si plusieurs utilisateurs accèdent au point de terminaison pour créer des Workers, le thread principal ne sera pas bloqué.

### Comment implémenter l'optimisation multi-cœur

Nous avons simplement créé des workers, puis en utilisant la fonction `createWorker` à l'intérieur d'une boucle, nous avons engendré quatre workers ou un nombre spécifié en fonction du nombre de threads. Chaque worker poste des messages indépendamment, et via l'écouteur, nous recevons les données de chaque worker. Ces résultats sont collectés via des promesses, stockés ensemble dans un tableau, et enfin, nous additionnons tous les résultats de ce tableau pour obtenir le résultat final.

Ainsi, les autres concepts font tous partie du JavaScript de base. J'espère que vous comprenez maintenant comment fonctionnent les worker threads et comment nous pouvons utiliser des processus multi-thread dans Node.js. C'est un excellent concept et une excellente opportunité d'apprendre en profondeur.

### **Ce que nous avons appris**

Les Worker Threads dans Node.js offrent un moyen puissant de gérer les tâches gourmandes en CPU sans bloquer la boucle d'événements principale. En tirant parti de plusieurs cœurs et en répartissant le travail sur plusieurs threads, nous pouvons considérablement améliorer les performances de l'application tout en maintenant la réactivité pour les autres utilisateurs.

* **Exécution non bloquante** : Les worker threads empêchent le thread principal d'être bloqué
    
* **Utilisation multi-cœur** : Nous pouvons exploiter plusieurs cœurs de CPU pour le traitement parallèle
    
* **Création asynchrone de workers** : Utilisation de promesses pour gérer la création de workers sans blocage
    
* **Agrégation de résultats** : Collecte et combinaison des résultats de plusieurs workers
    
* **Optimisation des performances** : Distribution des calculs lourds sur plusieurs threads
    

Cette approche est particulièrement précieuse pour les applications qui doivent gérer des tâches de calcul intensives tout en restant réactives aux requêtes des utilisateurs.

## Mot de la fin

Si vous avez trouvé les informations ici utiles, n'hésitez pas à les partager avec d'autres personnes qui pourraient en bénéficier. J'apprécierais vraiment vos retours – mentionnez-moi sur X [@sumit_analyzen](https://x.com/sumit_analyzen) ou sur Facebook [@sumit.analyzen](https://facebook.com/sumit.analyzen), [regardez mes tutoriels de codage](https://youtube.com/@logicBaseLabs), [visitez mon site web](https://sumitsaha.me) ou [connectez-vous simplement avec moi](https://www.linkedin.com/in/sumitanalyzen/) sur LinkedIn.

## Ressources supplémentaires

Vous pouvez également consulter la [documentation des Worker Threads de Node.js](https://nodejs.org/api/worker_threads.html) pour un apprentissage plus approfondi. Vous pouvez trouver tout le code source de ce tutoriel dans [ce dépôt GitHub](https://github.com/logicbaselabs/node-worker-threads/). S'il vous a aidé d'une manière ou d'une autre, envisagez de lui donner une étoile pour montrer votre soutien !