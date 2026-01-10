---
title: 'Une introduction à la programmation comportementale avec React : requête,
  attente et blocage'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-23T21:18:26.000Z'
originalURL: https://freecodecamp.org/news/an-intro-to-behavioral-programming-with-react-request-wait-and-block-ad876e2d235e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*vFUyNVhV5JOKn76HfMJYXw.jpeg
tags:
- name: Behavioral Programming
  slug: behavioral-programming
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: 'Une introduction à la programmation comportementale avec React : requête,
  attente et blocage'
seo_desc: 'By Luca Matteis

  Behavioral Programming (BP) is a paradigm coined in the 2012 article by David Harel,
  Assaf Marron, and Gera Weiss.

  Directly from the abstract:


  Behavioral programming simplifies the task of dealing with underspecification and
  conflict...'
---

Par Luca Matteis

La programmation comportementale (BP) est un paradigme introduit dans l'[article de 2012](http://www.wisdom.weizmann.ac.il/~amarron/BP%20-%20CACM%20-%20Author%20version.pdf) par David Harel, Assaf Marron et Gera Weiss.

Directement depuis le résumé :

> La programmation comportementale simplifie la tâche de gestion de la sous-spécification et des exigences contradictoires en permettant l'ajout de modules logiciels qui peuvent non seulement ajouter mais aussi **modifier les comportements existants**.

### Concepts de haut niveau

Je vais d'abord expliquer les concepts de haut niveau en utilisant un exemple de deux composants React `MoviesList` et `MoviesCount`. L'un affiche une liste de films, l'autre un nombre indiquant combien de films il y a. Ensuite, je vais approfondir le fonctionnement exact de la programmation comportementale.

Les deux composants récupèrent des données depuis la même URL HTTP. Ils ont été développés par deux équipes différentes au sein d'une grande organisation. Lorsque nous rendons les deux composants sur une page, nous avons un problème car ils effectuent la même requête :

```
<>  <MoviesList />  <MoviesCount /></>
```

Ce que nous ne savions pas, c'est que ce sont des **composants comportementaux**. Cela signifie que nous pouvons faire quelque chose de plutôt intelligent pour éviter que les deux requêtes ne se déclenchent :

```
const MoviesCountFromList = withBehavior([  function* () {    // bloquer FETCH_COUNT pour qu'il ne se produise pas    yield { block: ['FETCH_COUNT'] }  },  function* () {    // attendre FETCH_LIST, demandé par l'autre    // composant MoviesList, et dériver le compte    const response = yield { wait: ['FETCH_LIST'] }    this.setState({      count: response.length    })  }])(MoviesCount)
```

Dans l'exemple ci-dessus, nous sommes intervenus dans le composant `MoviesCount`. Nous avons **attendu** et **demandé** que quelque chose se produise. Et, plus particulièrement dans la programmation comportementale, nous avons également **bloqué** quelque chose pour qu'il ne se produise pas.

Parce que nous essayions d'éviter que les deux requêtes ne se déclenchent, nous avons bloqué l'événement `FETCH_COUNT` pour qu'il ne soit pas déclenché (puisque les mêmes données avaient déjà été acquises par l'événement `FETCH_LIST`).

```
<>  <MoviesList />  <MoviesCountFromList /></>
```

Ajouter des fonctionnalités à des composants existants sans modifier leur code est la nouveauté du paradigme de la programmation comportementale.

Intuitivement, cela peut permettre la création de composants plus réutilisables.

Dans le reste de l'article, j'approfondirai le fonctionnement de la programmation comportementale (BP), spécifiquement dans le contexte de **React**.

### Repenser le flux de programmation

Pour atteindre la fonctionnalité ci-dessus, nous devons penser un peu différemment à la programmation des comportements. Plus précisément, les **événements** jouent un rôle crucial dans l'orchestration de la synchronisation entre les divers comportements que nous définissons pour nos composants.

```
const addHotThreeTimes = behavior(  function* () {    yield { request: ['ADD_HOT'] }    yield { request: ['ADD_HOT'] }    yield { request: ['ADD_HOT'] }  })
```

```
const addColdThreeTimes = behavior(  function* () {    yield { request: ['ADD_COLD'] }    yield { request: ['ADD_COLD'] }    yield { request: ['ADD_COLD'] }  })
```

```
run(  addHotThreeTimes,  addColdThreeTimes)
```

Lorsque nous exécutons le code ci-dessus, nous obtenons une liste d'événements demandés :

```
ADD_HOTADD_HOTADD_HOTADD_COLDADD_COLDADD_COLD
```

Comme prévu, le premier comportement s'exécute. Une fois terminé, le deuxième comportement continue. Cependant, de nouvelles spécifications pour notre composant nous obligent à changer l'ordre dans lequel les deux événements sont déclenchés. Plutôt que de déclencher `ADD_HOT` trois fois, puis `ADD_COLD` trois fois, nous voulons qu'ils s'entrelacent et déclenchent `ADD_COLD` juste après un `ADD_HOT`. Cela maintiendra la température quelque peu stable.

```
...
```

```
const interleave = behavior(  function* () {    while (true) {      // attendre ADD_HOT tout en bloquant ADD_COLD      yield { wait: ['ADD_HOT'], block: ['ADD_COLD'] }
```

```
      // attendre ADD_COLD tout en bloquant ADD_HOT      yield { wait: ['ADD_COLD'], block: ['ADD_HOT'] }    }  })
```

```
run(  addHotThreeTimes,  addColdThreeTimes,  interleave)
```

Dans l'exemple ci-dessus, nous introduisons un nouveau comportement d'entrelacement qui fait exactement ce dont nous avons besoin.

```
ADD_HOTADD_COLDADD_HOTADD_COLDADD_HOTADD_COLD
```

Nous avons changé l'**ordre** d'exécution des choses, sans avoir à modifier le code des comportements déjà écrits.

Le processus est résumé dans le graphique ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/elehAKVL-hHtde0-NJJ4qaxh5-tUIhFvZfmP)

Les concepts clés de cette façon de programmer sont les opérateurs **request**, **wait** et **block**. La sémantique de ces opérateurs est la suivante :

* **Demander** un événement : proposer que l'événement soit considéré pour être déclenché, et demander à être notifié lorsqu'il est déclenché
* **Attendre** un événement : sans proposer son déclenchement, demander à être notifié lorsque l'événement est déclenché
* **Bloquer** un événement : interdire le déclenchement de l'événement, opposant son veto aux requêtes d'autres b-threads.

Chaque b-thread (thread comportemental) vit de manière indépendante et n'est pas conscient des autres threads. Mais ils sont tous entrelacés à l'exécution, ce qui leur permet d'interagir les uns avec les autres de manière très novatrice.

**La syntaxe du générateur est essentielle au fonctionnement d'un programme comportemental. Nous devons contrôler quand passer à la prochaine instruction yield.**

### Retour à React

Comment ces concepts de BP peuvent-ils être utilisés dans le contexte de React ?

Il s'avère que grâce aux composants d'ordre supérieur (HOC), vous pouvez ajouter cet idiome comportemental à des composants existants de manière très intuitive :

```
class CommentsCount extends React.Component {  render() {    return <div>{this.state.commentsCount}</div>  }}
```

```
const FetchCommentsCount = withBehavior([  function* () {    yield { request: ['FETCH_COMMENTS_COUNT']}    const comments = yield fetchComments()    yield { request: ['FETCH_COMMENTS_COUNT_SUCCESS']}    this.setState({ commentsCount: comments.length })  },])(CommentsCount)
```

Ici, nous utilisons `withBehavior`, de la bibliothèque [b-thread](https://github.com/lmatteis/b-thread), pour faire de `CommentsCount` un composant comportemental. Plus précisément, nous le faisons récupérer les commentaires et afficher les données une fois que les données sont prêtes.

Pour des composants simples, cela peut ne pas être un changement de jeu. Mais imaginons des composants plus complexes, avec beaucoup de logique et d'autres composants à l'intérieur.

Nous pourrions imaginer l'ensemble du site web de Netflix comme un composant `<Netflix />` :

![Image](https://cdn-media-1.freecodecamp.org/images/uPWqKfgGgH0PCYqKsvEyybAcWY5rHQwgG1Ax)
_Capture d'écran du site web de Netflix_

Lorsque nous utilisons ce composant dans notre application, nous aimerions interagir avec lui. Plus précisément, lorsqu'un film est cliqué, nous ne voulons pas démarrer le film immédiatement, mais plutôt faire une requête HTTP, afficher d'autres données sur le film, puis démarrer le film.

Sans changer le code à l'intérieur du composant `<Netflix />`, je soutiendrais que cela serait impossible à réaliser sans qu'il soit un composant comportemental.

Au lieu de cela, imaginons que `<Netflix />` a été développé en utilisant la programmation comportementale :

```
const NetflixWithMovieInfo = withBehavior([  function* () {    // D'abord, bloquer MOVIE_START pour qu'il ne se produise pas    // dans <Netflix /> jusqu'à ce qu'un nouvel    // événement FETCH_MOVIE_INFO_SUCCESS ait été demandé.    // L'instruction yield ci-dessous peut être lue comme :    // attendre FETCH_MOVIE_INFO_SUCCESS tout en bloquant MOVIE_START    yield {       wait: ['FETCH_MOVIE_INFO_SUCCESS'],       block: ['MOVIE_START']     }  },  function* () {    // Ici, nous attendons MOVIE_CLICKED, qui est    // déclenché dans <Netflix />, et nous récupérons nos    // informations sur le film. Une fois cela fait, nous demandons un nouvel événement    // que le comportement précédent attend    const movie = yield { wait: ['MOVIE_CLICKED'] }    const movieInfo = yield fetchMovieInfo(movie)    yield {       request: ['FETCH_MOVIE_INFO_SUCCESS'],       payload: movieInfo     }  }])(Netflix)
```

Ci-dessus, nous avons créé un nouveau composant `NetflixWithMovieInfo` qui modifie le comportement du composant `<Netflix />` (encore une fois, sans changer son code source). L'ajout des comportements ci-dessus fait en sorte que `MOVIE_CLICKED` ne déclenchera pas `MOVIE_START` immédiatement.

Au lieu de cela, il utilise une combinaison d'« attente tout en bloquant » : une **attente** et un **blocage** peuvent être définis dans une seule instruction yield.

![Image](https://cdn-media-1.freecodecamp.org/images/KFzI-ryqH4Y8RJSMj9sQbhlgOewuCahAjVPJ)

L'image ci-dessus décrit, plus en détail, ce qui se passe dans nos composants comportementaux. Chaque petite boîte dans les composants est une instruction yield. Chaque flèche verticale en pointillés représente un comportement (aka b-thread).

En interne, l'implémentation comportementale commencera par examiner toutes les instructions yield de tous les b-threads au point de synchronisation actuel, représenté par une ligne jaune horizontale. Elle ne continuera vers la prochaine instruction yield dans un b-thread que si aucun événement dans d'autres b-threads ne le bloque.

Puisque rien ne bloque `MOVIE_CLICKED`, il sera demandé. Nous pouvons ensuite continuer à la prochaine instruction yield pour le comportement Netflix. Au prochain point de synchronisation, le b-thread à l'extrême droite, qui attend `MOVIE_CLICKED`, passera à sa prochaine instruction yield.

Le comportement du milieu qui attend-et-bloque ne progresse pas. `FETCH_MOVIE_INFO_SUCCESS` n'a pas été demandé par d'autres b-threads, donc il attend toujours-et-bloque. Le prochain point de synchronisation ressemblera à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/q1eZUSHheMd3CdPZLyaaMx2EwdScwta7qHeW)

Comme avant, nous examinerons toutes les instructions yield à ce point de synchronisation. Cette fois, cependant, nous ne pouvons pas demander `MOVIE_START` parce qu'il y a un autre b-thread qui le bloque (l'instruction yield noire). Le composant Netflix ne démarrera donc pas le film.

`FETCH_MOVIE_INFO_SUCCESS` à l'extrême droite, cependant, est libre d'être demandé. Cela débloquera `MOVIE_START` au prochain point de synchronisation.

Tout cela, en pratique, nous a permis de changer l'ordre des choses qui se passent dans d'autres composants, sans modifier directement leur code. Nous avons pu bloquer certains événements jusqu'à ce que d'autres conditions soient remplies dans d'autres composants.

**Cela change la façon dont nous pourrions penser à la programmation** : pas nécessairement un ensemble d'instructions exécutées dans l'ordre, mais **plutôt un entrelacement d'instructions yield toutes synchronisées par des sémantiques d'événements spécifiques.**

Voici une simple animation décrivant la façon dont les b-threads sont exécutés et entrelacés à l'exécution.

![Image](https://cdn-media-1.freecodecamp.org/images/vgOkR26vCmjVgmF6-gJpO5Cetiku9SsaqxFE)
_Ordre d'exécution de différents threads_

### Programmer sans changer l'ancien code

Il y a une autre façon de comprendre cet idiome de programmation. Nous pouvons comparer la façon dont nous programmons actuellement lorsque les spécifications changent, par rapport à la façon dont cela serait fait avec la programmation comportementale.

![Image](https://cdn-media-1.freecodecamp.org/images/uH6c2Q8UiiNHTtir3GipE69BK9ld6ZTY0NYe)
_Chaque comportement ajouté est représenté par un rectangle de couleur différente_

Dans la légende ci-dessus, nous imaginons comment un comportement peut être ajouté à un programme non comportemental. Nous commençons avec un programme décrit uniquement par trois rectangles noirs (à gauche).

Lorsque les spécifications changent, nous réalisons que nous devons modifier le programme et ajouter un nouveau comportement dans diverses sections du programme, représenté par des rectangles colorés nouvellement ajoutés. Nous continuons à faire cela lorsque les exigences de notre logiciel changent.

Chaque ajout de comportement nous oblige à changer le code qui a été écrit, ce qui peut potentiellement introduire des bugs dans l'ancien comportement. De plus, si le programme que nous modifions fait partie de divers autres modules utilisés par différentes personnes, nous pourrions introduire un comportement indésirable dans leur logiciel. Enfin, il peut ne pas être possible de changer des programmes spécifiques car ils peuvent être distribués sous forme de bibliothèques avec un code source sous licence.

![Image](https://cdn-media-1.freecodecamp.org/images/rtjBXCCf8ftal6Utzyt0wX6EIOmvq9k1Qk0n)
_Chaque colonne à gauche est un b-thread_

Dans la figure ci-dessus, nous voyons comment les mêmes modifications de programme peuvent être réalisées en utilisant des idiomes de programmation comportementale. Nous commençons toujours avec nos trois rectangles à gauche comme nous l'avons fait auparavant. Mais lorsque de nouvelles spécifications apparaissent, nous ne les modifions pas. Au lieu de cela, nous ajoutons de nouveaux b-threads, représentés par des colonnes.

Le programme résultant est le même, bien que construit de manière très différente. L'un des avantages de l'approche comportementale est que nous n'avons pas à modifier l'ancien code lorsque les exigences changent.

Vous pouvez également imaginer développer chaque b-thread en parallèle, éventuellement par différentes personnes dans une grande organisation, puisqu'ils ne dépendent pas directement les uns des autres.

L'avantage de cette approche semble également résider dans l'emballage : nous pouvons changer le comportement d'une bibliothèque sans avoir besoin d'accéder ou de modifier son code source.

### API non seulement en tant que props, mais aussi en tant qu'événements

Actuellement, la seule façon pour un composant React de communiquer avec le monde extérieur est via les props (à part l'API Context).

En rendant un composant comportemental, au lieu d'utiliser des props, nous informons le monde extérieur de ce qui se passe dans le composant en générant des événements.

Pour permettre à d'autres développeurs d'interagir avec le comportement d'un composant, nous devons donc documenter les événements qu'il **demande**, les événements qu'il **attend**, et enfin les événements qu'il **bloque**.

**Les événements deviennent la nouvelle API.**

Par exemple, dans un composant `Counter` non comportemental, nous informons le monde extérieur lorsque le compteur est incrémenté et quel est le compte actuel, en utilisant une prop `onIncrement` :

```
class Counter extends React.Component {  state = { currentCount: 0 }  handleClick = () => {    this.setState(prevState => ({      currentCount: prevState.currentCount + 1    }), () => {      this.props.onIncrement(this.state.currentCount)    })  }  render() {    {this.state.currentCount}    <button onClick={this.handleClick}>+</button>  }}
```

```
<Counter   onIncrement={(currentCount) =>     console.log(currentCount)  }/>
```

Et si nous voulons faire autre chose avant que l'état du compteur ne soit incrémenté ? En effet, nous pourrions ajouter une nouvelle prop telle que `onBeforeIncrement`, mais le problème est que nous ne voulons pas ajouter des props et refactoriser le code chaque fois qu'une nouvelle spécification apparaît.

Si nous le transformons en un composant comportemental, nous pouvons éviter le refactoring lorsque de nouvelles spécifications émergent :

```
class Counter extends React.Component {  state = { currentCount: 0 }  handleClick = () => {    bp.event('CLICKED_INCREMENT')  }  render() {    {this.state.currentCount}    <button onClick={this.handleClick}>+</button>  }}
```

```
const BehavioralCounter = withBehavior([  function* () {    yield { wait: ['CLICKED_INCREMENT'] }    yield { request: ['UPDATE_CURRENT_COUNT'] }
```

```
    this.setState(prevState => ({      currentCount: prevState.currentCount + 1    }), () => {      this.props.onIncrement(this.state.currentCount)    })  }])(Counter)
```

Remarquez comment nous avons déplacé la logique de mise à jour de l'état à l'intérieur d'un b-thread. De plus, avant que la mise à jour ne se produise réellement, un nouvel événement `UPDATE_CURRENT_COUNT` est demandé.

Cela permet effectivement à d'autres b-threads de bloquer la mise à jour.

Les composants peuvent également être encapsulés et partagés sous forme de différents packages, et les utilisateurs peuvent ajouter des comportements comme ils le souhaitent.

```
// nom-du-package : movies-listexport const function MoviesList() {  ...}
```

```
// nom-du-package : movies-list-with-paginationexport const MoviesListWithPagination = pipe(  withBehavior(addPagination))(MoviesList)
```

```
// nom-du-package : movies-list-with-pagination-logicexport const MoviesListWithDifferentPaginationLogic = pipe(  withBehavior(changePaginationLogic))(MoviesListWithPagination)
```

Encore une fois, cela est différent de simplement améliorer un composant, comme le ferait un HOC régulier. Nous pouvons bloquer certaines choses dans les composants que nous étendons, modifiant ainsi effectivement leur comportement.

### Conclusion

Cet nouvel idiome de programmation peut sembler inconfortable au début, mais il semble atténuer un problème majeur que nous avons lors de l'utilisation de composants d'interface utilisateur : **il est difficile de réutiliser des composants, car ils ne s'intègrent pas dans l'environnement dans lequel ils ont été placés.**

À l'avenir, peut-être en utilisant ces concepts comportementaux, nous pourrons ajouter de nouveaux comportements aux applications simplement en montant de nouveaux composants. Des choses comme ceci seront possibles :

```
<Environment>  <Netflix />  <Twitter />  <WaitForTwitterBeforeNetflix />  <OnTwitterClickShowLoader /></Environment>
```

De plus, les événements n'ont pas besoin de polluer toute l'application et peuvent être diffusés uniquement dans un environnement spécifique.

Merci d'avoir lu ! Si vous êtes intéressé par une implémentation réelle de la programmation comportementale, veuillez consulter ma bibliothèque actuelle en cours de développement qui fonctionne avec React : [https://github.com/lmatteis/b-thread](https://github.com/lmatteis/b-thread). La [page d'accueil de la programmation comportementale](http://www.wisdom.weizmann.ac.il/~bprogram/) contient également diverses implémentations.

Pour plus d'informations sur ce nouveau concept passionnant, je vous suggère de lire les [articles scientifiques sur la programmation comportementale](https://scholar.google.ca/scholar?hl=en&as_sdt=0%2C5&q=behavioral+programming+harel&btnG=) ou de consulter certains de [mes autres articles](https://medium.com/@lmatteis/on-user-interface-development-appending-to-the-event-log-8d8ca966795d) [sur le sujet](https://medium.com/@lmatteis/statecharts-updating-ui-state-767052b6b129).