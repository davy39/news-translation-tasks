---
title: Avant de vous plonger dans les packages, apprenez le runtime Node.js lui-même
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-02T05:43:24.000Z'
originalURL: https://freecodecamp.org/news/before-you-bury-yourself-in-packages-learn-the-node-js-runtime-itself-f9031fbd8b69
coverImage: https://cdn-media-1.freecodecamp.org/images/1*LSfLSMQ1kPuHnyCPLNEKgQ.png
tags:
- name: JavaScript
  slug: javascript
- name: learning to code
  slug: learning-to-code
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Avant de vous plonger dans les packages, apprenez le runtime Node.js lui-même
seo_desc: 'By Samer Buna


  Update: This article is now part of my book “Node.js Beyond The Basics”.

  Read the updated version of this content and more about Node at jscomplete.com/node-beyond-basics.


  This article will challenge the very limits of your Node.js kn...'
---

Par Samer Buna

> **Mise à jour :** Cet article fait maintenant partie de mon livre « Node.js Beyond The Basics ».

> Lisez la version mise à jour de ce contenu et plus sur Node à [**jscomplete.com/node-beyond-basics**](https://jscomplete.com/node-beyond-basics).

Cet article mettra à l'épreuve les limites de vos connaissances sur Node.js.

J'ai commencé à apprendre Node.js peu après que Ryan Dahl l'ait [présenté](https://www.youtube.com/watch?v=ztspvPYybIY) pour la première fois, et je n'ai pas été en mesure de répondre à beaucoup des questions que je pose dans cet article il y a encore un an. Si vous pouvez vraiment répondre à toutes ces questions, alors vos connaissances sur Node.js sont excellentes. Nous devrions être amis.

La raison pour laquelle je pense que ce défi vous surprendra est que beaucoup d'entre nous ont surtout appris Node de la mauvaise manière. La plupart des tutoriels, livres et cours sur Node se concentrent sur l'écosystème Node — et non sur le runtime Node lui-même. Ils se concentrent sur l'enseignement de ce qui peut être fait avec tous les packages disponibles pour vous lorsque vous travaillez avec Node, comme Express et Socket.IO, plutôt que sur l'enseignement des capacités du runtime Node lui-même.

Il y a de bonnes raisons à cela. Node est brut et flexible. Il ne fournit pas de solutions complètes, mais plutôt un runtime riche qui vous permet de mettre en œuvre vos propres solutions. Des bibliothèques comme Express.js et Socket.IO sont plus des solutions complètes, il est donc plus logique d'enseigner ces bibliothèques, afin que vous puissiez permettre aux apprenants d'utiliser ces solutions complètes.

La sagesse conventionnelle semble être que seuls ceux dont le travail est d'écrire des bibliothèques comme Express.js et Socket.IO doivent comprendre tout sur le runtime Node.js. Mais je pense que c'est faux. Une compréhension solide du runtime Node.js lui-même est la meilleure chose que vous puissiez faire avant d'utiliser ces solutions complètes. Vous devriez au moins avoir les connaissances et la confiance pour juger un package par son code, afin de pouvoir prendre une décision éclairée sur son utilisation.

C'est pourquoi j'ai décidé de créer un [cours Pluralsight](https://www.pluralsight.com/courses/nodejs-advanced) entièrement dédié à Node pur. En faisant des recherches pour le cours, j'ai dressé une liste de questions spécifiques pour déterminer si vos connaissances du runtime Node sont déjà suffisamment solides, ou si elles pourraient être améliorées.

Si vous pouvez répondre à la plupart de ces questions et que vous cherchez un emploi, faites-le moi savoir ! Si, en revanche, la plupart de ces questions vous surprennent, vous devez simplement faire de l'apprentissage du runtime Node une priorité. Vos connaissances dans ce domaine feront de vous un développeur beaucoup plus recherché.

### Le défi des connaissances Node.js :

Certaines de ces questions sont courtes et faciles, tandis que d'autres nécessitent des réponses plus longues et des connaissances plus approfondies. Elles sont toutes présentées ici dans un ordre quelconque.

Je sais que vous allez vouloir des réponses après avoir lu cette liste. La section conseils ci-dessous contient certaines réponses, mais je répondrai également à toutes ces questions dans une série d'articles freeCodeCamp après celui-ci. Mais laissez-moi d'abord titiller vos connaissances !

1. Quelle est la relation entre Node.js et V8 ? Node peut-il fonctionner sans V8 ?
2. Comment se fait-il que lorsque vous déclarez une variable globale dans un fichier Node.js, elle n'est pas vraiment globale pour tous les modules ?
3. Lors de l'exportation de l'API d'un module Node, pourquoi pouvons-nous parfois utiliser `exports` et d'autres fois devons-nous utiliser `module.exports` ?
4. Peut-on importer des fichiers locaux sans utiliser de chemins relatifs ?
5. Différentes versions du même package peuvent-elles être utilisées dans la même application ?
6. Qu'est-ce que la boucle d'événements ? Fait-elle partie de V8 ?
7. Qu'est-ce que la pile d'appels ? Fait-elle partie de V8 ?
8. Quelle est la différence entre `setImmediate` et `process.nextTick` ?
9. Comment faire en sorte qu'une fonction asynchrone retourne une valeur ?
10. Les callbacks peuvent-ils être utilisés avec les promesses ou est-ce l'un ou l'autre ?
11. Quel module Node est implémenté par la plupart des autres modules Node ?
12. Quelles sont les principales différences entre `spawn`, `exec` et `fork` ?
13. Comment fonctionne le module cluster ? En quoi est-il différent de l'utilisation d'un équilibreur de charge ?
14. Que sont les flags `--harmony-*` ?
15. Comment pouvez-vous lire et inspecter l'utilisation de la mémoire d'un processus Node.js ?
16. Que fera Node lorsque la pile d'appels et la file d'attente de la boucle d'événements seront vides ?
17. Que sont les modèles d'objets et de fonctions V8 ?
18. Qu'est-ce que libuv et comment Node.js l'utilise-t-il ?
19. Comment pouvez-vous faire en sorte que le REPL de Node utilise toujours le mode strict JavaScript ?
20. Qu'est-ce que `process.argv` ? Quel type de données contient-il ?
21. Comment pouvons-nous effectuer une opération finale avant qu'un processus Node ne se termine ? Cette opération peut-elle être effectuée de manière asynchrone ?
22. Quelles sont certaines des commandes point intégrées que vous pouvez utiliser dans le REPL de Node ?
23. En dehors de V8 et libuv, quelles sont les autres dépendances externes de Node ?
24. Quel est le problème avec l'événement `uncaughtException` du processus ? En quoi est-il différent de l'événement `exit` ?
25. Que signifie le `_` à l'intérieur du REPL de Node ?
26. Les buffers Node utilisent-ils la mémoire V8 ? Peuvent-ils être redimensionnés ?
27. Quelle est la différence entre `Buffer.alloc` et `Buffer.allocUnsafe` ?
28. En quoi la méthode `slice` sur les buffers est-elle différente de celle sur les tableaux ?
29. À quoi sert le module `string_decoder` ? En quoi est-il différent de la conversion des buffers en chaînes de caractères ?
30. Quelles sont les 5 étapes principales que la fonction require effectue ?
31. Comment pouvez-vous vérifier l'existence d'un module local ?
32. À quoi sert la propriété `main` dans `package.json` ?
33. Que sont les dépendances modulaires circulaires dans Node et comment peuvent-elles être évitées ?
34. Quelles sont les 3 extensions de fichiers qui seront automatiquement essayées par la fonction require ?
35. Lors de la création d'un serveur http et de l'écriture d'une réponse pour une requête, pourquoi la fonction `end()` est-elle requise ?
36. Quand est-il acceptable d'utiliser les méthodes `*Sync` du système de fichiers ?
37. Comment pouvez-vous imprimer seulement un niveau d'un objet profondément imbriqué ?
38. À quoi sert le package `node-gyp` ?
39. Les objets `exports`, `require` et `module` sont tous globalement disponibles dans chaque module mais ils sont différents dans chaque module. Comment ?
40. Si vous exécutez un fichier de script node qui contient la ligne unique : `console.log(arguments);`, que va exactement imprimer node ?
41. Comment un module peut-il être à la fois requérable par d'autres modules et exécutable directement en utilisant la commande `node` ?
42. Quel est un exemple de flux intégré dans Node qui est à la fois lisible et inscriptible ?
43. Que se passe-t-il lorsque la ligne cluster.fork() est exécutée dans un script Node ?
44. Quelle est la différence entre l'utilisation des émetteurs d'événements et l'utilisation de simples fonctions de rappel pour permettre la gestion asynchrone du code ?
45. À quoi sert la fonction `console.time` ?
46. Quelle est la différence entre les modes Paused et Flowing des flux lisibles ?
47. Que fait l'argument `--inspect` pour la commande node ?
48. Comment pouvez-vous lire des données à partir d'une socket connectée ?
49. La fonction `require` met toujours en cache le module qu'elle requiert. Que pouvez-vous faire si vous devez exécuter le code dans un module requis plusieurs fois ?
50. Lors de la manipulation de flux, quand utilisez-vous la fonction pipe et quand utilisez-vous des événements ? Ces deux méthodes peuvent-elles être combinées ?

### Mon avis sur la meilleure façon d'apprendre le runtime Node.js

Apprendre Node.js peut être un défi. Voici quelques directives qui, je l'espère, vous aideront dans ce voyage :

#### Apprenez les bonnes parties de JavaScript et son syntaxe moderne (ES2015 et au-delà)

Node est un ensemble de bibliothèques sur le dessus d'un moteur VM qui peut compiler JavaScript, il va donc sans dire que les compétences importantes pour JavaScript lui-même sont un sous-ensemble des compétences importantes pour Node. Vous devriez commencer par JavaScript lui-même.

Comprenez-vous les fonctions, les [portées](https://edgecoders.com/function-scopes-and-block-scopes-in-javascript-25bbd7f293d7#.2h7c9bt6l), la liaison, le mot-clé this, le mot-clé new, les [fermetures](https://medium.freecodecamp.com/whats-a-javascript-closure-in-plain-english-please-6a1fc1d2ff1c#.fs8bxulzo), les classes, les motifs de modules, les prototypes, les callbacks et les promesses ? Êtes-vous conscient des diverses méthodes qui peuvent être utilisées sur les nombres, les chaînes de caractères, les tableaux, les ensembles, les objets et les cartes ? Vous familiariser avec les éléments de cette liste rendra l'apprentissage de l'API Node beaucoup plus facile. Par exemple, essayer d'apprendre les méthodes du module 'fs' avant d'avoir une bonne compréhension des callbacks peut conduire à une confusion inutile.

#### Comprenez la nature non bloquante de Node

Les callbacks et les promesses (et les générateurs/motifs async) sont particulièrement importants pour Node. Vous devez comprendre comment les opérations asynchrones sont de première classe dans Node.

Vous pouvez comparer la nature non bloquante des lignes de code dans un programme Node à la façon dont vous commandez un café chez Starbucks (dans le magasin, pas au drive) :

1. Passez votre commande | Donnez à Node des instructions à exécuter (une fonction)
2. Personnalisez votre commande, par exemple sans crème fouettée | Donnez à la fonction quelques arguments : `({whippedCream: false})`
3. Donnez votre nom au travailleur de Starbucks avec la commande | Donnez à Node un callback avec votre fonction : `({whippedCream: false}, callback)`
4. Écartez-vous et le travailleur de Starbucks prendra les commandes des personnes qui étaient après vous dans la file | Node prendra les instructions des lignes après les vôtres.
5. Lorsque votre commande est prête, le travailleur de Starbucks appellera votre nom et vous donnera votre commande | Lorsque votre fonction est calculée et que Node.js a un résultat prêt pour vous, il appellera votre callback avec ce résultat : `callback(result)`

J'ai écrit un article de blog à ce sujet : [Programmation asynchrone telle que vue chez Starbucks](https://edgecoders.com/asynchronous-programming-as-seen-at-starbucks-fc242cf16aa#.mx2cxr3hi)

### Apprenez le modèle de concurrency JavaScript et comment il est basé sur une boucle d'événements

Il y a une pile, un tas et une file d'attente. Vous pouvez lire des livres sur ce sujet et encore ne pas le comprendre complètement, mais je vous garantis que vous le ferez si vous regardez [ce gars](https://www.youtube.com/watch?v=8aGhZQkoFbQ).

%[https://youtu.be/8aGhZQkoFbQ]

Philip explique la boucle d'événements qui est dans le navigateur, mais presque la même chose s'applique à Node.js (il y a quelques différences).

#### Comprenez comment un processus Node ne dort jamais et se terminera lorsqu'il n'y a plus rien à faire

Un processus Node peut être inactif mais il ne dort jamais. Il garde une trace de tous les callbacks en attente et s'il n'y a plus rien à exécuter, il se terminera simplement. Pour garder un processus Node en cours d'exécution, vous pouvez par exemple utiliser une fonction `setInterval` car cela créerait un callback en attente permanent dans la boucle d'événements.

#### Apprenez les variables globales que vous pouvez utiliser comme process, module et Buffer

Elles sont toutes définies sur une variable globale (qui est généralement comparée à la variable `window` dans les navigateurs). Dans un REPL de Node, tapez `global.` et appuyez sur tab pour voir tous les éléments disponibles (ou simple double-tab sur une ligne vide). Certains de ces éléments sont des structures JavaScript (comme `Array` et `Object`). Certains d'entre eux sont des fonctions de bibliothèque Node (comme `setTimeout`, ou `console` pour imprimer sur `stdout`/`stderr`), et certains d'entre eux sont des objets globaux Node que vous pouvez utiliser pour certaines tâches (par exemple, `process.env` peut être utilisé pour lire les variables d'environnement de l'hôte).

![Image](https://cdn-media-1.freecodecamp.org/images/1*6ejru9JVwgJ9iGxBYpysJw.png)

Vous devez comprendre la plupart de ce que vous voyez dans cette liste.

#### Apprenez ce que vous pouvez faire avec les bibliothèques intégrées qui sont fournies avec Node et comment elles se concentrent sur le « networking »

Certaines d'entre elles vous sembleront familières, comme _Timers_ par exemple, car elles existent également dans le navigateur et Node simule cet environnement. Cependant, il y a beaucoup plus à apprendre, comme `fs`, `path`, `readline`, `http`, `net`, `stream`, `cluster`, ... (La liste d'auto-complétion ci-dessus les contient toutes).

Par exemple, vous pouvez lire/écrire des fichiers avec `fs`, vous pouvez exécuter un serveur web prêt pour le streaming en utilisant « `http` », et vous pouvez exécuter un serveur tcp et programmer des sockets avec « `net` ». Node aujourd'hui est tellement plus puissant qu'il ne l'était il y a encore un an, et il s'améliore à chaque commit. Avant de chercher un package pour effectuer une tâche, assurez-vous de ne pas pouvoir effectuer cette tâche avec les packages Node intégrés en premier.

La bibliothèque `events` est particulièrement importante car la plupart de l'architecture Node est basée sur des événements.

Il y a toujours [plus que vous pouvez apprendre sur l'API Node](https://nodejs.org/api/all.html), alors continuez à élargir vos horizons.

#### Comprenez pourquoi Node est nommé Node

Vous construisez des blocs de construction simples à processus unique (nœuds) qui peuvent être organisés avec de bons protocoles de réseau pour qu'ils communiquent entre eux et montent en puissance pour construire de grands programmes distribués. La mise à l'échelle d'une application Node n'est pas une réflexion après coup — elle est intégrée directement dans le nom.

#### Lisez et essayez de comprendre du code écrit pour Node

Choisissez un framework, comme Express, et essayez de comprendre une partie de son code. Posez des questions spécifiques sur les choses que vous ne comprenez pas. J'essaie de répondre aux questions sur le [canal slack jsComplete](https://slackin-bfcnswvsih.now.sh/) lorsque je peux.

Enfin, écrivez une application web en Node sans utiliser de frameworks. Essayez de gérer autant de cas que possible, répondez avec un fichier HTML, analysez les chaînes de requête, acceptez les entrées de formulaire et créez un endpoint qui répond avec JSON.

Essayez également d'écrire un serveur de chat, de publier un package npm et de contribuer à un projet open-source basé sur Node.

Bonne chance ! Merci d'avoir lu.

Apprendre React ou Node ? Consultez mes livres :

* [Learn React.js by Building Games](http://amzn.to/2peYJZj)
* [Node.js Beyond the Basics](http://amzn.to/2FYfYru)