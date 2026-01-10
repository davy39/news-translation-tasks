---
title: Programmation réactive et séquences d'Observables avec RxJS dans Node.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-23T11:16:07.000Z'
originalURL: https://freecodecamp.org/news/rxjs-and-node-8f4e0acebc7c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*gpmVC7PYhD3ZYHBYltyeXw.png
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: Reactive Programming
  slug: reactive-programming
- name: RxJS
  slug: rxjs
- name: TypeScript
  slug: typescript
seo_title: Programmation réactive et séquences d'Observables avec RxJS dans Node.js
seo_desc: 'By Enrico Piccinin

  Dealing with asynchronous non-blocking processing has always been the norm in the
  JavaScript world, and now is becoming very popular in many other contexts. The benefits
  are clear: an efficient use of resources. But the benefits co...'
---

Par Enrico Piccinin

Gérer le traitement asynchrone non bloquant a toujours été la norme dans le monde JavaScript, et cela devient maintenant très populaire dans de nombreux autres contextes. Les avantages sont clairs : une utilisation efficace des ressources. Mais ces avantages ont un coût : une augmentation non négligeable de la complexité.

Au fil du temps, les éditeurs et la communauté open source ont tenté de trouver des moyens de réduire cette complexité sans compromettre les avantages.

Le traitement asynchrone a commencé avec les « callbacks », puis sont venus les Promise et Future, async et await. Récemment, un nouveau venu est arrivé — [ReactiveX](http://reactivex.io/) avec ses diverses implémentations de langages — apportant aux développeurs un nouvel outil puissant, l'Observable.

Dans cet article, nous voulons montrer comment les Observables implémentés par [RxJs](http://reactivex.io/rxjs/) (l'incarnation JavaScript de ReactiveX) peuvent simplifier le code à exécuter avec Node.js, l'environnement JavaScript non bloquant côté serveur très populaire.

### Un cas d'utilisation simple — Lire, Transformer, Écrire et Journaliser

Pour rendre notre raisonnement concret, partons d'un cas d'utilisation simple. Supposons que nous devions lire les fichiers contenus dans un `**Source Dir**`, transformer leur contenu et écrire les nouveaux fichiers transformés dans un `**Target Dir**`, tout en tenant un journal des fichiers que nous avons créés.

![Image](https://cdn-media-1.freecodecamp.org/images/t6BDM5ShfozMhO6juTt2pT5hoxj6C-XnQe8G)
_Lire — Transformer — Écrire — Journaliser_

### Implémentation synchrone

L'implémentation synchrone de ce cas d'utilisation est assez simple. Dans une sorte de représentation en pseudo-code, nous pourrions penser à quelque chose comme :

```
lire les noms des fichiers du Répertoire Source
   pour chaque nom de fichier
      lire le fichier
      transformer le contenu
      écrire le nouveau fichier dans le Répertoire Cible
      journaliser le nom du nouveau fichier
   fin pour
console.log('J\'ai terminé')
```

Il n'y a rien de spécial à commenter ici. Nous pouvons simplement dire que nous sommes sûrs de la séquence d'exécution de chaque ligne et que nous sommes sûrs que les choses se passeront comme décrit par le flux d'événements suivant. Chaque cercle correspond à la fin d'une opération d'E/S.

![Image](https://cdn-media-1.freecodecamp.org/images/VkuJvfZCN7Ps5vLDx4OvCxcU1pfo3MsHYkGc)
_La séquence d'événements dans un monde synchrone_

### Ce qui se passe dans un environnement asynchrone non bloquant comme Node.js

Node.js est un environnement d'exécution asynchrone non bloquant pour JavaScript. Non bloquant signifie que Node.js n'attend pas la fin des opérations d'E/S ou de réseau avant de passer à l'exécution de la ligne de code suivante.

#### **Traitement d'un seul fichier**

La lecture et l'écriture de fichiers sont des opérations d'E/S où Node.js montre sa nature non bloquante. Si un programme Node.js demande la lecture d'un fichier, il doit fournir une fonction à exécuter lorsque le contenu du fichier est disponible (ce qu'on appelle un **callback**) puis passer immédiatement à l'opération suivante à exécuter.

Considérons le cas d'un **seul fichier**. Lire, transformer, écrire **un** fichier et mettre à jour le journal dans Node.js ressemble à ceci :

```javascript
import * as fs from 'fs'; // Module Node pour accéder au système de fichiers
const fileName = 'one-file.txt';
fs.readFile(fileName, callback(err, data) => {
   const newContent = transform(data);
   const newFileName = newFileName(fileName); // calculer le nouveau nom
   fs.writeFile(newFileName, newContent, err => {
      if(err) {// gérer l'erreur};
      fs.appendFile('log.txt', newFileName  + ' écrit', err = {
         if (err) {// gérer l'erreur}
      });
   });
})
```

La syntaxe peut sembler un peu alambiquée avec 2 niveaux d'indentation, mais si nous pensons à ce qui se passe en termes d'événements, nous pouvons toujours prévoir précisément la séquence :

![Image](https://cdn-media-1.freecodecamp.org/images/CZESn-CUe78yiDYRe0a79MZH81ZZuAu7mBrJ)
_Séquence d'événements dans Node lors de la transformation d'un fichier_

#### **Le paradis des Promises**

C'est le cas d'utilisation où les Promises JavaScript brillent. En utilisant les Promises, nous pouvons redonner au code un aspect séquentiel, sans interférer avec la nature asynchrone de Node.js.

En supposant que nous puissions accéder à des fonctions qui effectuent des opérations de lecture et d'écriture sur fichier et renvoient une Promise, notre code ressemblerait à :

```javascript
const fileName = 'my-file.txt';
readFilePromise(fileName)
.then(data => {
   const newContent = transform(data);
   const newFileName = newFileName(fileName); // construire le nouveau nom
   return writeFilePromise(newFileName, newContent)
})
.then(newFileName => appendFile('log.txt', newFileName))
.then(newFileName => console.log(newFileName + ' écrit'))
.catch(err => // gérer l'erreur)
```

Il existe plusieurs façons de transformer les fonctions Node.js en fonctions basées sur des `Promise`. Voici un exemple :

```javascript
function readFilePromise(fileName: string): Promise<Buffer>{
   return new Promise(function(resolve, reject) {
      fs.readFile(fileName, function(err, data: Buffer) {
         if(err !== null) return reject(err);
         resolve(data);
      });
   });
}
```

#### **Traitement de plusieurs fichiers**

Si nous revenons au cas d'utilisation original, où nous devons transformer tous les fichiers contenus dans un répertoire, la complexité augmente et les Promises commencent à montrer certaines limites.

Regardons les événements que l'implémentation Node.js doit gérer :

![Image](https://cdn-media-1.freecodecamp.org/images/PRMavRZ7dF0oaWIHXqkCq6-e0Xfm0HR5m1-u)
_Séquence d'événements lors de la transformation de plusieurs fichiers en parallèle_

Chaque cercle représente la fin d'une opération d'E/S, soit une lecture, soit une écriture. Chaque ligne représente le traitement d'un fichier spécifique, ou une chaîne de Promises.

Étant donné la nature non bloquante de Node.js, il n'y a aucune certitude sur la séquence temporelle de ces événements. Il est possible que nous finissions d'écrire `**File2**` avant d'avoir fini de lire `**File3**`.

Le traitement parallèle de chaque fichier rend l'utilisation des Promises plus complexe (à la fin de cet article, une implémentation basée sur les Promises est fournie). C'est le scénario où ReactiveX — RxJs en particulier — et les Observables brillent et vous permettent de construire des solutions élégantes.

### Que sont les Observables et que pouvez-vous faire avec ?

Il existe de nombreux endroits où les définitions formelles des Observables sont détaillées, à commencer par le site officiel de [ReactiveX](http://reactivex.io/intro.html).

Ici, je veux juste vous rappeler quelques propriétés qui ont toujours attiré mon attention :

* L'Observable modélise un **flux d'événements**
* L'Observable est le frère **« push »** de l'Iterable, qui est « pull »

En tant que frère « push » de l'Iterable, l'Observable offre aux développeurs de nombreuses fonctionnalités intéressantes fournies par les Iterables telles que :

* Transformer des « flux d'événements » ou des Observables, via des opérateurs tels que `map`, `filter` et `skip`
* Appliquer un style de programmation fonctionnelle

Une autre chose très importante que l'Observable offre est la souscription. Via la souscription, le code peut appliquer des « effets secondaires » aux événements et effectuer des actions spécifiques lorsque des événements particuliers se produisent, comme lorsque des erreurs surviennent ou que le flux d'événements se termine.

![Image](https://cdn-media-1.freecodecamp.org/images/ZXgqj1SdhavRZdcReV9aBvtTnLZ3r8jODhNz)
_L'interface de souscription de l'Observable_

Comme vous pouvez le voir, l'interface Observable donne aux développeurs la possibilité de fournir trois fonctions différentes qui définissent quoi faire respectivement quand : un événement est émis avec ses données, une erreur survient, ou le flux d'événements se termine.

Je suppose que tout ce qui précède peut sembler très théorique pour ceux qui n'ont pas encore joué avec les Observables, mais j'espère que la suite de la discussion, axée sur notre cas d'utilisation, rendra ces concepts plus concrets.

### Implémentation du cas d'utilisation Lire, Transformer, Écrire et Journaliser via Observable

Notre cas d'utilisation commence par la lecture de la liste des fichiers contenus dans le `**Source Dir**`. Commençons donc par là.

#### **Lire tous les noms de fichiers contenus dans un répertoire**

Supposons que nous ayons accès à une fonction qui reçoit en entrée le nom d'un répertoire et renvoie un Observable qui émet la liste des noms de fichiers du répertoire une fois que la structure de l'arborescence du répertoire a été lue.

```
readDirObservable(dirName: string) : Observable<Array<string>>
```

Nous pouvons nous abonner à cet Observable et, lorsque tous les noms de fichiers ont été lus, commencer à faire quelque chose avec eux :

![Image](https://cdn-media-1.freecodecamp.org/images/BeSolRYnvm1Cj0rhkQtZXbtqkopSZ-yCELo8)
_Souscription à un Observable qui émet lorsque le répertoire a été lu_

#### **Lire une liste de fichiers**

Supposons maintenant que nous puissions accéder à une fonction qui reçoit en entrée une liste de noms de fichiers et émet chaque fois qu'un fichier a été lu (elle émet le contenu du fichier `Buffer`, et son nom `string`).

```
readFilesObservable(fileList: Array<string>) 
   : Observable<{content: Buffer, fileName: string}>
```

Nous pouvons nous abonner à un tel `Observable` et commencer à faire quelque chose avec le contenu des fichiers.

#### Combiner des Observables — l'opérateur switchMap

Nous avons maintenant deux Observables, l'un qui émet une liste de noms de fichiers lorsque le répertoire a été lu et l'autre qui émet chaque fois qu'un fichier est lu.

Nous devons les combiner pour implémenter la première étape de notre cas d'utilisation, qui est : quand `readDirObservable` émet, nous devons **basculer** vers `readFilesObservable`.

![Image](https://cdn-media-1.freecodecamp.org/images/iWmO0g9KdUw64scmcB5OGgbsOJarDfwyIGZg)
_opérateur switchMap_

L'astuce ici est réalisée par l'opérateur `switchMap`. Le code ressemble à ceci :

```
readDirObservable(dirName)
.switchMap(fileList => readFilesObservable(fileList))
.subscribe(
      data => console.log(data.fileName + ' lu'), // faire des choses avec les données reçues
      err => { // gérer l'erreur },
      () => console.log('Tous les fichiers ont été lus')
)
```

Nous devons mentionner que l'opérateur `switchMap` est plus puissant que cela. Sa pleine puissance ne peut cependant pas être appréciée dans ce cas d'utilisation simple, et sa description complète dépasse le cadre de cet article. Si vous êtes intéressé, voici un [excellent article](https://blog.angular-university.io/rxjs-switchmap-operator/) qui décrit en détail `switchMap`.

#### **Observable générant un flux d'Observables**

Nous avons maintenant un flux d'événements représentant la fin d'une opération de lecture (`read`). Après la lecture, nous devons effectuer une transformation du contenu qui, par souci de simplicité, nous supposons être synchrone, puis nous devons enregistrer le contenu transformé dans un nouveau fichier.

Mais l'écriture d'un nouveau fichier est à nouveau une opération d'E/S, ou une opération non bloquante. Ainsi, chaque événement de « fin de lecture de fichier » commence un nouveau chemin d'élaboration qui reçoit en entrée le contenu et le nom du fichier source, et émet lorsque le nouveau fichier est écrit dans le `Target Dir` (l'événement émis porte le nom du fichier écrit).

Encore une fois, nous supposons que nous sommes capables d'accéder à une fonction qui émet dès que l'opération d'écriture est terminée, et la donnée émise est le nom du fichier écrit.

```
writeFileObservable(fileName: string, content: Buffer) :            Observable<string>
```

Dans ce cas, nous avons différents Observables « write-file », renvoyés par la fonction `writeFileObservable`, qui émettent indépendamment. Il serait intéressant de les **fusionner** dans un nouvel Observable qui émet chaque fois que l'un de ces Observables « write-file » émet.

![Image](https://cdn-media-1.freecodecamp.org/images/uNh9nBU32X6SbsDi-SAmYy90FhR4we4XLcXv)
_Un flux d'Observables que nous aimerions fusionner_

Avec ReactiveX (ou RxJs en JavaScript), nous pouvons atteindre ce résultat en utilisant l'opérateur `mergeMap` (également connu sous le nom de **flatMap**). Voici à quoi ressemble le code :

```
readDirObservable(dir)
.switchMap(fileList => readFilesObservable(fileList))
.map(data => transform(data.fileName, data.content))
.mergeMap(data => writeFileObservable(data.fileName, data.content))
.subscribe(
      file => console.log(data.fileName + ' écrit'),
      err => { // gérer l'erreur },
      () => console.log('Tous les fichiers ont été écrits')
)
```

L'opérateur `mergeMap` a créé un nouvel Observable, le `writeFileObservable` comme illustré dans le diagramme suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/reYH02KG9yTsgGuI7cTiPFMCTURzBsFRC07D)
_Observable renvoyé par l'opérateur mergeMap_

#### Et alors ?

En appliquant la même approche, si nous imaginons simplement que nous avons une nouvelle fonction `writeLogObservable`, qui écrit une ligne dans le journal dès que le fichier est écrit et émet le nom du fichier dès que le journal est mis à jour, le code final pour notre cas d'utilisation ressemblerait à :

```
readDirObservable(dir)
.switchMap(fileList => readFilesObservable(fileList))
.map(data => transform(data.fileName, data.content))
.mergeMap(data => writeFileObservable(data.fileName, data.content))
.mergeMap(fileName => writeLogObservable(fileName))
.subscribe(
      file => console.log(fileName + ' journalisé'),
      err => { // gérer l'erreur },
      () => console.log('Tous les fichiers ont été transformés')
)
```

Nous n'avons pas d'indentations introduites par les callbacks.

Le temps s'écoule uniquement le long de l'axe vertical, nous pouvons donc lire le code ligne par ligne et raisonner sur ce qui se passe ligne après ligne.

Nous avons adopté un style fonctionnel.

En d'autres termes, nous avons vu les avantages de l'Observable en action.

### Créer un Observable à partir de fonctions avec des callbacks

J'espère que vous pensez maintenant que cela a l'air plutôt cool. Mais même dans ce cas, vous pourriez avoir une question. Toutes les fonctions qui rendent ce code cool n'existent tout simplement pas. Il n'y a pas de `readFilesObservable` ou de `writeFileObservable` dans les bibliothèques standard de Node.js. Comment pouvons-nous les créer ?

#### **bindCallback et bindNodeCallback**

Quelques fonctions fournies par Observable, à savoir `bindCallback` (et `bindNodeCallback`), viennent à notre secours.

L'idée centrale derrière elles est de fournir un mécanisme pour transformer une fonction `f` qui accepte un callback `cB(cBInput)` comme paramètre d'entrée en une fonction qui renvoie un Observable `obsBound` qui émet `cBInput`. En d'autres termes, elle transforme l'**invocation** du `cB` en l'**émission** de `cBInput`.

L'abonné de `obsBound` peut définir la fonction qui traitera `cBInput` (qui joue le même rôle que `cB(cBInput)`). La convention appliquée est que la fonction de callback `cB(cBInput)` doit être le dernier argument de `f`.

Il est probablement plus facile de comprendre le mécanisme en regardant le diagramme suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/SfAvPHIPSPJmnk3VLeW6ioBOCITEpiebo-Bf)
_D'une fonction à un Observable_

Le point de départ, la fonction **f(x, cb)** est la même dans les deux cas. Le résultat (ce qui est affiché sur la console) est le même dans les deux cas.

Ce qui est différent, c'est la façon dont le résultat est obtenu. Dans le premier cas, le résultat est déterminé par la fonction de callback passée en entrée. Dans le second cas, il est déterminé par la fonction définie par l'abonné.

Une autre façon de considérer le fonctionnement de `bindCallback` est de regarder la transformation qu'il effectue, comme illustré dans le diagramme ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/MJ-tn3TsJhIDDEPt6ymYxBxgMJ1GYyqNQfHA)
_Transformation effectuée par bindCallback_

Le premier argument de `f` devient la valeur passée à la nouvelle fonction `fBound`. Les arguments utilisés comme paramètres du callback `cb` deviennent les valeurs émises par le nouvel Observable renvoyé par `fBound`.

`bindNodeCallback` est une variante de `bindCallback` basée sur la convention selon laquelle la fonction de callback a un paramètre d'**erreur** comme premier paramètre, conformément à la convention Node.js `fs.readFile(err, cb)`.

#### **Créer des Observables à partir de fonctions sans callback**

`bindNodeCallback` a été conçu pour fonctionner avec des fonctions qui attendent un callback comme dernier argument de leur entrée, mais nous pouvons le faire fonctionner également avec d'autres fonctions.

Considérons la fonction standard Node.js `readLine`. C'est une fonction utilisée pour lire des fichiers ligne par ligne. L'exemple suivant montre comment elle fonctionne :

![Image](https://cdn-media-1.freecodecamp.org/images/41zopDeXW8stNTeBo2BmXMswEucES7U4WASG)
_fonction readLine_

Chaque ligne lue est poussée dans le tableau `lines`. Lorsque le fichier est complètement lu, la fonction `processLinesCb` est appelée.

Imaginez maintenant que nous définissions une nouvelle fonction, `_readLines`, qui enveloppe la logique définie ci-dessus comme le montre l'extrait suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/2SxYnanPtydSbSaJmkEGmxsWSHU7QIAToPpu)
_fonction readLine enveloppée par une fonction de callback_

Une fois toutes les lignes lues, elles sont traitées par la fonction `processLinesCb`, qui est le dernier paramètre d'entrée de `_readLines`. `_readLines` est donc une fonction qui peut être traitée par `bindCallback`. Grâce à cette astuce, nous pouvons transformer la fonction Node.js `fs.readLine` en un Observable en utilisant la fonction habituelle `bindCallback` comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/FMEHXXKXwbucYZ4s1sVj9OkuavNPUMw972va)
_readLine en tant qu'Observable_

### **Conclusion**

Le traitement asynchrone non bloquant est complexe par nature. Nos esprits sont habitués à penser de manière séquentielle — c'est vrai du moins pour ceux d'entre nous qui ont commencé à coder il y a quelques années. Nous trouvons souvent difficile de raisonner sur ce qui se passe réellement dans ces environnements. L'enfer des callbacks (callback-hell) n'est jamais loin.

Les Promises et les Futures ont simplifié certains des cas les plus fréquents tels que les événements asynchrones « uniques », le scénario « requête immédiate — réponse ultérieure » typique des requêtes HTTP.

Si nous passons des événements « uniques » aux « flux d'événements », les Promises commencent à montrer certaines limites. Dans de tels cas, nous pouvons trouver en ReactiveX et les Observables un outil très puissant.

#### **Comme promis : l'implémentation de notre cas d'utilisation basée sur les Promises**

Voici une implémentation du même cas d'utilisation basée sur les Promises :

```
const promises = new Array<Promise>();
readDirPromise(dir)
.then(fileList => {
   for (const file of fileList) {promises.push(
         readFilePromise(file)
         .then(file_content => transform(file_content))
         .then(file => writeLogPromise(file))
      );
   }
   return promises;
}
.then(promises => Promise.all(promises))
.then(() => console.log('J\'ai terminé'))
.catch(err => { // gérer l'erreur })
```