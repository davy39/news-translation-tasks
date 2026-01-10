---
title: 'Apprendre Node.js avec Brigadier Fluffykins Partie II : Événements, EventEmitter
  et la boucle d''événements'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-07-20T16:32:38.000Z'
originalURL: https://freecodecamp.org/news/learn-node-js-with-brigadier-fluffykins-part-ii-events-eventemitter-the-event-loop-6d4c139694fb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4E7_DswXy8rFF2Dzrq1H3A.jpeg
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
seo_title: 'Apprendre Node.js avec Brigadier Fluffykins Partie II : Événements, EventEmitter
  et la boucle d''événements'
seo_desc: 'By Mariya Diminsky

  Welcome to Part II of Learn Node.js With Brigadier Fluffykins, a series created
  to help you easily understand Node.js ❤

  In Part I Brigadier Fluffykins and I introduced Node.js, what you can build with
  it, async/sync concepts. I wal...'
---

Par Mariya Diminsky

Bienvenue à la Partie II de **Apprendre Node.js avec Brigadier Fluffykins**, une série créée pour vous aider à comprendre facilement Node.js 

Dans la [Partie I](https://medium.freecodecamp.com/learn-node-js-with-brigadier-fluffykins-i-basics-async-sync-create-your-first-server-b9e54a45e108#.116vkn9sw), Brigadier Fluffykins et moi avons présenté Node.js, ce que vous pouvez construire avec, les concepts async/sync. Je vous ai guidé à travers l'installation, et ensemble nous avons créé votre premier serveur.

C'était glorieux :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZiX_YkLaq2EHqJTVEBX9ng.gif)

La leçon d'aujourd'hui couvrira :

* Pourquoi Node.js est un langage piloté par événements, et comment cela est important pour le comportement asynchrone
* Comment les événements dans le DOM sont similaires aux événements dans Node.js
* Comment la boucle d'événements traite les requêtes
* Créer des événements personnalisés en utilisant _EventEmitter_

#### La programmation pilotée par événements est géniale

Puisque Node.js est mono-thread, afin de créer de la concurrence et de ne pas être douloureusement lent — comme le modèle client-serveur traditionnel expliqué dans la [Partie I](https://medium.com/free-code-camp/learn-node-js-with-brigadier-fluffykins-i-basics-async-sync-create-your-first-server-b9e54a45e108#.6jgtvz314) — il utilise des événements pour écouter les requêtes.

Cela est différent de, par exemple, Apache, un serveur web qui utilise HTTP multi-thread. Pour chaque requête qu'Apache reçoit, il crée un nouveau thread pour la traiter. Cela signifie que oui, bien que vous puissiez avoir plus d'un processus en cours d'exécution en même temps via des threads, l'inconvénient est que les résultats de toutes les requêtes doivent revenir avant de servir la page.

D'autre part, l'architecture pilotée par événements de Node.js permet de traiter plusieurs requêtes sur un seul thread. Par exemple, une fois qu'un événement de _requête_ est déclenché, les callbacks et les promesses traitent ces requêtes de manière asynchrone.

Cela signifie que si vous avez plusieurs requêtes entrantes et que la requête A est encore en cours de traitement, la requête B commencera à récupérer les résultats — le résultat étant soit que la requête B répond au client avant la requête A, soit en même temps que la requête A.

Puisque tout est traité plus rapidement, le client a une meilleure expérience utilisateur. Discutons de cela plus en détail plus loin dans la leçon.

Il y a quelques inconvénients au modèle de concurrence de Node.js, mais nous les couvrirons dans les prochaines leçons.

#### Les événements dans le DOM sont comme les événements dans Node.js

Pensez aux événements de cette manière : tout comme les événements interagissent avec les objets DOM, de nombreux objets dans Node.js émettent des événements.

Si vous avez fait de la manipulation DOM avec JavaScript, alors vous comprenez que le DOM peut avoir des écouteurs d'événements tels que _click_, _dblclick_, _submit_, _keydown_, _keyup_, etc. Une fois déclenchés, l'événement est traité avec un callback.

Par exemple, lorsque vous configurez un événement _click_, vous pouvez avoir un callback qui dit : « lorsque quelque chose est cliqué, rendre le troisième div bleu ! »

Voici un exemple codé.

Dans votre fichier _index.html_ :

Dans votre fichier _main.js_ :

Et, si vous voulez tester cela dans votre propre navigateur, voici un peu de CSS. Cela devrait aller dans _style.css_ :

Lorsque le client clique sur le bouton, notre événement _click_ est déclenché, et notre callback fait quelque chose au DOM. Dans ce cas, il rend le troisième div bleu et change le texte à l'intérieur du bouton.

Comme l'événement _request_ dans Node.js, lorsque le client clique sur un bouton, c'est comme s'il envoyait une requête dans le fichier main.js où l'événement _click_ écoute — tout comme l'événement _request_ écouterait les requêtes entrantes.

Ensuite, tout comme l'événement _response_ répondrait au client avec certaines informations à l'intérieur du callback, le callback de l'événement _click_ du DOM répond en changeant la couleur de fond du troisième div. Il change également le texte dans le bouton à l'intérieur du fichier html.

La principale différence entre les événements dans Node.js et les événements dans le DOM est que les événements DOM restent principalement attachés à l'objet DOM — côté client — tandis que les événements pour Node.js sont plus axés sur la relation entre le client et le serveur.

Node.js émet des événements à partir d'objets — tels que l'objet serveur web (_http.createServer_). Heureusement pour vous, vous avez déjà utilisé des événements dans la [Partie I](https://medium.com/free-code-camp/learn-node-js-with-brigadier-fluffykins-i-basics-async-sync-create-your-first-server-b9e54a45e108#.6jgtvz314) à l'ÉTAPE #1.5 !

Lors de cette étape, vous avez sauvegardé l'objet serveur web dans sa propre variable et écouté les requêtes entrantes via l'événement _request_ attaché à l'objet _http.createServer_ dans le premier paramètre.

Sous cet objet se trouve le _constructeur EventEmitter_, que nous apprendrons très bientôt. Pour l'instant, passez en revue le code que nous avons configuré dans la [Partie I](https://medium.freecodecamp.com/learn-node-js-with-brigadier-fluffykins-i-basics-async-sync-create-your-first-server-b9e54a45e108#.bvd38wc9b) et voyez si vous avez une meilleure compréhension de ce qui se passe après notre explication sur les événements.

Le voici à nouveau pour référence :

#### La boucle d'événements

D'accord, vous avez une compréhension de base des événements et de leur relation avec Node.js, mais comment Node.js fonctionne-t-il réellement sous le capot ?

La première chose que Node.js fait lorsqu'il lit votre code est de s'abonner aux événements que vous avez utilisés, tels que _request_, _listen_, _connection_ ou _close_. Une fois cela fait, il entre dans la _boucle d'événements_ et écoute continuellement ces événements à l'intérieur d'un seul thread.

Par exemple, dans le serveur que nous avons créé précédemment, il n'écoute que l'événement _request_ et ainsi la boucle d'événements pense :

« Des requêtes sont-elles arrivées ? »

« Et maintenant ? »

« … »

« Maintenant ? »

« Maintenant, non ? »

![Image](https://cdn-media-1.freecodecamp.org/images/1*V-TXRhsZRaB6L4KAhauBbA.png)
_Brigadier Fluffykins aime faire semblant d'être Jules Winfield._

Pas de soucis, la boucle d'événements mono-thread de Node.js n'est pas Jules Winfield. Elle attend et écoute simplement patiemment les événements auxquels elle s'est abonnée en arrière-plan.

Si une requête arrive, elle déclenche l'événement _request_ et exécute le callback que nous avons écrit — dans notre cas, le mini html à l'intérieur de la méthode _end_ dans notre exemple de serveur précédent. Sachez également que les événements peuvent déclencher d'autres événements.

Mais que se passe-t-il si plusieurs requêtes arrivent en même temps ? Comme l'événement _request_ et l'événement _close_ ? La boucle d'événements traitera ces événements un à la fois. Donc d'abord l'événement _request_ sera traité, puis l'événement _close_. Pendant qu'ils sont traités, ils n'empêchent pas d'autres événements d'arriver. Si c'était le cas, notre code mettrait deux fois plus de temps à s'exécuter.

#### Approfondissons ce que tout cela signifie

Donc, lorsque nous disons que JavaScript est mono-thread, nous disons qu'il n'a qu'une seule [_Call Stack_](https://en.wikipedia.org/wiki/Call_stack) — quelque chose qui suit les fonctions qui s'exécuteront dans votre code. Chaque barre dorée représente une fonction à l'intérieur de la _Call Stack_. La dernière fonction ajoutée en haut est la première fonction qui s'exécute et qui est retirée.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2payUr3yb8fWKfaruK5p7g.gif)
_Call Stack — Dernier entré, premier sorti._

Si JavaScript était un langage synchrone, et que nous avions deux requêtes entrantes, que pensez-vous qu'il se passerait ? Nous devrions attendre le résultat de la première requête avant de pouvoir traiter la deuxième requête. Cela signifie que la première requête resterait dans la _Call Stack_, bloquant toute autre requête entrante, jusqu'à ce que ses résultats nécessaires soient retournés.

Une fois les résultats récupérés, la première requête est « retirée », et seulement alors la deuxième requête entrerait dans la _Call Stack_ et serait exécutée :

![Image](https://cdn-media-1.freecodecamp.org/images/1*3e8V0aT6qNsHs3WfbexskA.gif)
_Si JavaScript était synchrone._

JavaScript atteint son modèle de concurrence en stockant les fonctions asynchrones ailleurs pendant que d'autres tâches, beaucoup plus rapides, s'exécutent en premier. Ensuite, lorsque notre fonction asynchrone reçoit ce dont elle a besoin, elle s'exécute éventuellement. Au moins, c'est l'essentiel.

Approfon

Lorsque qu'une fonction asynchrone avec un callback ou un événement entre dans la _Call Stack_, elle se déplace automatiquement dans la _Web API_. La _Web API_ est l'endroit où les événements abonnés à la _boucle d'événements_ sont stockés. Ils attendent les ordres de la _boucle d'événements_, qui écoute si l'un des événements est appelé.

Une fois qu'un événement est déclenché, par exemple l'événement _request_, le callback de cet événement est envoyé dans une _file d'événements_. Cette file est également appelée _file de callbacks_ ou simplement _file de tâches_.

La raison pour laquelle nous avons plusieurs noms pour la file est que le même processus qui se produit pour les événements se produit pour les fonctions asynchrones — ou méthodes — tout ce qui a un callback, y compris les événements DOM et les fonctions d'événements qui ne font pas partie de JavaScript natif comme _ajax_ et _setTimeout_ (Oui, ils font partie de la _Web API_, pas de JavaScript).

Maintenant, la dernière chose qui se produit est que le callback de l'événement _request_ attendra à l'intérieur de cette _file d'événements/callbacks/tâches_ que la _Call Stack_ se vide. Cela a quelque chose à voir avec la manière dont JavaScript traite la mémoire — donc, en gros, sachez simplement qu'une fois que nous arrivons à ce stade, nous devons attendre que toutes les fonctions encore en cours d'exécution se terminent avant de pouvoir ajouter le callback dans la _Call Stack_ et le traiter.

Voici une démonstration visuelle de tout ce que nous venons d'expliquer :

1. JavaScript scanne votre code et empile les fonctions, les événements et tout le reste sur la _Call Stack_.
2. Les barres dorées ci-dessous sont des fonctions régulières, non asynchrones. Les dernières barres roses et vertes sont deux événements _request_. Ces événements sont abonnés à la _boucle d'événements_ (jouée par Brigadier Fluffykins) et attendent à l'intérieur de la _Web API_ d'être appelés.
3. Pendant que les événements attendent, d'autres fonctions sont exécutées sur la _Call Stack_.
4. Une fois qu'un événement est déclenché, la _boucle d'événements_ l'entend et le callback de cet événement particulier se déplace dans la _file_. Cependant, puisque c'est l'événement _request_, il attendrait d'abord les résultats dont il a besoin. Et seulement alors il envoie le callback dans la file.
5. Pendant qu'il y a encore des fonctions en cours d'exécution et en cours de traitement sur la _Call Stack_, les événements doivent attendre que la _Call Stack_ se vide pour pouvoir s'exécuter. Brigadier Fluffykins leur fait savoir si c'est A-OK de se déplacer dans la _Call Stack_ ou non, selon qu'elle est vide ou non.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MNowbF50tQ6K8HnFG8rfDA.gif)
_**Gauche :** Call Stack. **Haut Droite :** Web API. **Bas Droite :** File. **Brigadier Fluffykins est la boucle d'événements.**_

### Créons des événements personnalisés !

Les émetteurs d'événements sont largement utilisés dans les bibliothèques Node.js, alors apprenons à créer les nôtres et à mieux comprendre comment ils fonctionnent !

Tous les objets qui émettent des événements sont des instances de la _classe EventEmitter_ et tous les événements héritent du _constructeur EventEmitter_. Nous allons créer deux événements pour l'émetteur d'événements _bunnyError_ — _bunnyWarning_ et _bunnyNeed_.

Copiez et collez ceci dans un fichier appelé _bunnyEmitter.js_ :

D'accord, que se passe-t-il ici ?

Tout d'abord, nous requérons l'_objet EventEmitter_ de Node.js, puis nous créons une instance d'un nouvel objet EventEmitter que nous allons construire avec des événements personnalisés. Nous appelons cette instance _bunnyError_.

Ensuite, nous créons un écouteur d'événements pour notre premier événement, _bunnyWarning_, avec la méthode _on_, qui écoute l'événement. Nous traitons cet événement lorsqu'il est utilisé en déclenchant un callback qui imprime simplement « BUNNY WARNING: warning. »

Remarquez que j'ai utilisé les _Template Literals_ — une fonctionnalité ES6. Vous pouvez en apprendre plus à leur sujet [ici](https://medium.freecodecamp.com/learn-es6-the-dope-way-part-iii-template-literals-spread-operators-generators-592765337294#.7udhwbjrl). C'est la même chose que de dire _console.log("BUNNY WARNING:" + message)_.

Enfin, nous utilisons la méthode _emit_ pour déclencher ou appeler l'événement. Une fois l'événement appelé, le callback devrait s'exécuter. Nous pouvons faire cela autant de fois que nous le voulons.

En supposant que le fichier est sur votre bureau, tapez _node bunnyEmitter.js_ dans votre shell :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Y0Ls412hP4YI572tVa0liQ.png)

Si vous voulez que votre émetteur d'événements ne se déclenche qu'une seule fois, l'_objet EventEmitter_ a une méthode appelée _.once_ que vous pouvez utiliser à la place de _.on_ :

```
votreEventEmitter.once(votreEvenement, votreCallback)
```

Avec cela, peu importe le nombre de fois où vous émettez _votreEvenement_, il ne fonctionnera qu'une seule fois.

Il est bon de limiter le nombre d'écouteurs d'événements que vous avez. En fait, si vous en avez plus de dix, vous recevrez un avertissement :

```
"(node) warning: possible EventEmitter memory leak detected. 11 listeners added. Use emitter.setMaxListeners() to increase limit."
```

Jusqu'à présent, vous avez vu des termes tels que _événements_, _écouteur d'événements_ et _gestionnaire d'événements_ être utilisés. Clarifions les principales différences avant de continuer :

L'_écouteur d'événements_ est l'_événement_ que vous créez pour écouter tout événement entrant. Le _gestionnaire d'événements_ est le callback qui sera déclenché une fois que l'_écouteur d'événements_ entendra l'_événement_.

Dans notre exemple d'émetteur d'événements personnalisé, les _écouteurs d'événements_ étaient _bunnyWarning_ et _bunnyNeeds_, et les _gestionnaires d'événements_ étaient les callbacks de chaque événement.

#### Consultez ces ressources supplémentaires

* [Documentation Node.js sur les événements](https://nodejs.org/api/events.html)
* [Liste des événements pour le DOM](https://developer.mozilla.org/en-US/docs/Web/Events)
* Vous avez appris à créer une instance d'un émetteur d'événements, mais que faire si vous vouliez l'étendre et l'utiliser dans différents fichiers ? [Consultez ce tutoriel](http://www.hacksparrow.com/node-js-eventemitter-tutorial.html)
* [En savoir plus sur les méthodes de l'objet EventEmitter](http://www.tutorialspoint.com/nodejs/nodejs_event_emitter.htm)
* [Vous voulez en savoir plus sur la boucle d'événements ?](http://www.tutorialspoint.com/nodejs/nodejs_event_loop.htm)

Félicitations ! Vous avez réussi à traverser la **Partie II d'Apprendre Node.js avec Brigadier Fluffykins** ! Dans la leçon d'aujourd'hui, vous avez appris que Node.js est un langage piloté par événements et pourquoi cela est utile pour le comportement asynchrone. Vous avez également appris comment ces événements sont traités via la boucle d'événements.

Nous avons également plongé dans l'apprentissage des similitudes entre les événements DOM et les événements dans Node.js pour vous aider à vous adapter à ce nouveau domaine un peu plus.

Enfin, nous avons créé notre premier EventEmitter et deux événements géniaux !

Apprenons-en plus sur ces sujets ainsi que sur d'autres que nous n'avons fait qu'effleurer dans les prochaines leçons. Merci d'avoir lu et restez à l'écoute.

Gardez votre sagesse à jour en cliquant sur le  ci-dessous et en suivant, car plus de **Apprendre Node.js avec Brigadier Fluffykins** arrive bientôt sur Medium !

[**Partie I : Sync, Async, et Créer Votre Premier Serveur !**](https://medium.freecodecamp.com/learn-node-js-with-brigadier-fluffykins-i-basics-async-sync-create-your-first-server-b9e54a45e108#.bvd38wc9b)

[**Partie II : Événements, EventEmitter et Boucle d'Événements**](https://medium.com/@__Masha__/learn-node-js-with-brigadier-fluffykins-part-ii-events-eventemitter-the-event-loop-6d4c139694fb#.957cacwgv)

[**Partie III : Objet de Requête, Configurer les Routes, Servir des Fichiers**](https://medium.com/@__Masha__/learn-node-js-with-brigadier-fluffykins-part-iii-request-object-configure-routes-serve-files-7666f783dc10#.g5j0faw3x)