---
title: Développement piloté par les tests avec React et Redux, en utilisant Redux
  TDD
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-29T12:16:32.000Z'
originalURL: https://freecodecamp.org/news/test-driven-development-with-react-and-redux-using-redux-tdd-3fd3be299918
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0ern_Rqaw5d5tTuYRs78IQ.jpeg
tags:
- name: Functional Programming
  slug: functional-programming
- name: React
  slug: react
- name: Redux
  slug: redux
- name: Testing
  slug: testing
- name: Web Development
  slug: web-development
seo_title: Développement piloté par les tests avec React et Redux, en utilisant Redux
  TDD
seo_desc: 'By Luca Matteis

  React and Redux have introduced a lot of functional programming concepts to the
  development of User Interfaces (UIs). This allows us to test our UIs in a simpler
  manner: they are pure functions of state.

  Redux has broken down state ma...'
---

Par Luca Matteis

[React](https://facebook.github.io/react/) et [Redux](http://redux.js.org/) ont introduit de nombreux concepts de programmation fonctionnelle dans le développement des interfaces utilisateur (IU). Cela nous permet de tester nos IU de manière plus simple : elles sont des fonctions pures de l'état.

Redux a décomposé la gestion de l'état en utilisant un flux de données unidirectionnel, où la vue — ou le monde extérieur — génère une **action** qui est passée à un **réducteur**, qui crée un nouvel **état**, et passe cet nouvel état à la **vue** :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Wd0Tu0P9S-KuGiB_ZW77Cw.png)
_Flux de données unidirectionnel de Redux_

Ce qui est important, c'est que chacune des étapes illustrées ci-dessus avec les flèches jaunes est une **fonction pure**.

Cela signifie que nous pouvons tester unitairement chacune de ces étapes individuellement. Cela nous permet de tester des IU complexes en affirmant que les fonctions retournent des données spécifiques.

Voici un exemple de la manière dont nous pourrions tester chacune de ces étapes dans un simple composant `<Counter />` en utilisant [**jest**](https://facebook.github.io/jest/) et [**enzyme**](https://github.com/airbnb/enzyme) :

```js
// Counter.test.js
it('should test the arrows going in and out of the VIEW', () => {
  // entrée de la vue
  wrapper = shallow(<Counter counter={1} />);
  expect(wrapper.contains(<span>1</span>)).toBeTruthy();
  
  // sortie de la vue
  wrapper = shallow(<Counter onClick={incrementAction} />);
  wrapper.find(button).simulate('click');
  expect(incrementAction).toHaveBeenCalled();
})

// reducers.test.js
it('should test the arrows going in and out of the REDUCER', () => {
  // entrée du réducteur
  const newState = reducer({ count: 0 }, incrementAction())
  
  // sortie du réducteur
  expect(newState).toEqual({ count: 1 });
})

// actions.test.js
it('should test the arrows going in and out of the ACTION', () => {
  expect(incrementAction()).toMatchObject({ type: 'INCREMENT' });
})
```

Mais, lorsqu'il s'agit de faire du TDD (développement piloté par les tests), vous voulez généralement tester les choses en succession. Par exemple, lorsqu'un certain clic déclenche un certain changement d'état qui déclenche ensuite un changement d'IU.

Les tests ci-dessus devraient être rationalisés. Il devrait y avoir un moyen facile de les connecter naturellement au lieu d'avoir à écrire des tests unitaires séparés.

Dans cet article, je vais expliquer [**Redux TDD**](https://github.com/lmatteis/redux-tdd). Il s'agit d'un ensemble de fonctions d'assistance simples conçues pour vous aider à rationaliser vos tests en composant chaque partie du flux de données Redux ensemble.

Je vais également discuter d'autres concepts de TDD et de BDD (développement piloté par le comportement) dans le contexte du flux de données de Redux. Et nous explorerons à quoi pourrait ressembler l'avenir des tests des interfaces utilisateur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*uOlxCoXq1faNmKA-3ie2Bg.jpeg)
_([Source de l'image](https://unsplash.com/search/photos/jenga?photo=geNNFqfvw48" rel="noopener" target="_blank" title="))_

### Redux TDD

Plongeons immédiatement dans ce à quoi ressemble Redux TDD :

```jsx
ReduxTdd({ count: 9 }, state => shallow(
  <Counter 
    onIncrement={incrementActionMock} 
    onReset={resetActionMock} 
    count={state.count} />
))      
.simulate(wrapper => wrapper.find('button').simulate('click'))      .action(incrementActionMock).toMatchAction({ type: 'INCREMENT' })      .reducer(reducer).toMatchState({ count: 10 })      .view().contains(<span>10</span>)      
.simulate(wrapper => wrapper.find('button').simulate('click'))      .action(resetActionMock).toMatchAction({ type: 'RESET' })      .reducer(reducer).toMatchState({ count: 0 })
.view().contains(<span>0</span>)
```

Il y a beaucoup de chaînage de points dans ce code, mais il y a une raison à cela. Puisque le flux de données de Redux est unidirectionnel, tester son comportement correspond parfaitement à un modèle de pipeline. Ce qui signifie chaînage.

Chaque opérateur du pipeline est en fait un test unitaire simple.

L'idée est que chaque sortie d'une étape de flux de données unidirectionnel de Redux doit alimenter l'étape suivante. Cela permet un développement plus adapté au TDD.

#### Examinons chaque étape

1. Initialiser le flux avec un état et une vue  
Les autres opérateurs du pipeline ont besoin de cela pour faire des assertions sur l'état et la vue actuels :

```jsx
ReduxTdd({ count: 9 }, state => shallow(
  <Counter 
    onIncrement={incrementActionMock} 
    onReset={resetActionMock} 
    count={state.count} />
))
```

2. Simuler un clic réel  
Nous avons l'enveloppe enzyme de l'opérateur précédent, donc nous pouvons simuler des actions :

```
.simulate(wrapper => wrapper.find('button').simulate('click'))
```

3. C'est là que le plaisir commence  
Nous testons que `incrementActionMock` est appelé à partir de l'étape précédente et qu'il retourne l'objet `{ type: 'INCREMENT' }` :

```js
.action(incrementActionMock).toMatchAction({ type: 'INCREMENT' })
```

4. Nous passons une fonction `myReducer`  
Cela prendra l'état actuel du pipeline et l'action retournée par l'action composée précédente.

Il affirmera que `myReducer({ count: 9 }, { type: 'INCREMENT' })` retourne `{ count: 10 }` :

```js
.reducer(myReducer).toMatchState({ count: 10 })
```

5. Nous testons la vue  
Étant donné l'état actuel, modifié par le réducteur précédent, il affichera la sortie que nous voulons.

```js
.view().contains(<span>10</span>)
```

Ce modèle de chaînage de points vous oblige à tester le flux unidirectionnel de Redux. Il vous oblige à tester chaque étape avec les entrées de l'étape précédente.

![Image](https://cdn-media-1.freecodecamp.org/images/1*4n6RkGZdWcPvmsizsezKgg.png)
_Comment les données circulent à travers le pipeline_

Nous n'introduisons aucun magasin Redux, nous ne distribuons pas d'actions, et nous n'appelons aucune des API Redux. Nous testons uniquement que les fonctions pures retournent des données spécifiques.

#### Actions asynchrones

![Image](https://cdn-media-1.freecodecamp.org/images/1*av3MfP7tEC72pkPKkLAfeQ.jpeg)
_([Source de l'image](https://unsplash.com/search/photos/time?photo=p3Pj7jOYvnM" rel="noopener" target="_blank" title="))_

Jusqu'à présent, nous avons décrit comment tester la partie synchrone du flux de données de Redux. Pourtant, beaucoup des choses que nous faisons dans nos IU impliquent des actions asynchrones.

Dans Redux, cela est géré par des choses appelées **middlewares**. Je ne vais pas entrer dans les détails de leur fonctionnement. Je vais couvrir des exemples montrant comment ces tests peuvent être mis en pipeline contre [redux-observable](https://github.com/redux-observable/redux-observable) et [redux-thunk](https://github.com/gaearon/redux-thunk). Ce sont deux middlewares célèbres utilisés pour gérer les choses asynchrones et les effets secondaires dans Redux.

#### Redux-observable

```js
ReduxTdd({ count: 9 }, state => shallow(
  <Counter 
    onClick={incrementAsyncAction} 
    counter={state.count} />
))  
.simulate(wrapper => wrapper.find(button).simulate('click'))
.action(incrementAsyncAction).toMatchAction({ type: 'INCREMENT_ASYNC' })

.epic(handleIncrementAsyncEpic, { getJSON: () => 
  Observable.of({ foo: 'bar' })
})

// maintenant puisque nous avons simulé l'épopée, 
// nous pouvons continuer le test normal action->réducteur->vue
.action(incrementSuccessAction).toMatchAction(
  { type: 'INCREMENT_SUCCESS' }
)
.reducer(reducer).toMatchState({ count: 10 })
.view().contains(<span>10</span>)
                 
.epic(handleIncrementAsyncEpic, { getJSON: () => 
  // lançons une erreur cette fois 
  Observable.throw({ error: true })
})
                 
// puisque l'épopée a lancé une erreur, 
// nous nous attendons à ce qu'elle appelle la fonction incrementFailureAction
.action(incrementFailureAction).toMatchAction(
  { type: 'INCREMENT_FAILURE' }
)
// il ne l'augmentera pas à 11
.reducer(reducer).toMatchState({ count: 10 })
.view().contains(<span>10</span>)
```

Dans l'exemple ci-dessus, la partie importante du pipeline est l'opérateur `.epic()`.

Nous testons que :  
L'épopée `handleIncrementAsyncEpic` sera exécutée avec un observable émettant une action. Cela est retourné par l'opérateur `.action` précédent (`{ type: 'INCREMENT_ASYNC' }`) et l'observable `getJSON` simulé. Nous forcerons l'observable à émettre une réponse réussie.

Cela est intégré dans le flux Redux. Nous visualisons littéralement chaque partie du diagramme de flux de données Redux en utilisant du code.

L'épopée sera exécutée immédiatement et l'action résultante `{ type: 'INCREMENT_SUCCESS' }` sera passée à l'opérateur suivant dans le flux.

#### Redux-thunk

Les thunks peuvent également être intégrés dans le pipeline. Mais ils sont plus difficiles à tester car ils ne sont pas des fonctions pures :

```js
.thunk(incrementAsyncThunk, () => 
  Promise.resolve({ type: 'INCREMENT_SUCCESS' })
)
.toMatchActions([ 
  { type: 'INCREMENT_ASYNC' }, { type: 'INCREMENT_SUCCESS' } 
])
```

Nous forçons la `promise` du thunk à se résoudre avec succès. Et nous affirmons que les actions sont distribuées dans le même ordre que le tableau `toMatchActions`.

### Développement piloté par le comportement

![Image](https://cdn-media-1.freecodecamp.org/images/1*woIWXYmagRL9ejINlwRHnw.png)

Le principal avantage de composer des tests de cette manière est que cela fonctionne très bien lorsque l'on fait du [BDD](https://en.wikipedia.org/wiki/Behavior-driven_development).

Dans le BDD, vous commencez par écrire de petits tests qui simulent le comportement des utilisateurs. Vous implémentez votre code jusqu'à ce que les tests passent, et vous retournez dans votre fichier de test pour écrire de nouveaux tests qui échouent.

Avec le modèle de chaînage, cela fonctionne plus naturellement car nous **forçons le flux de contrôle**. Vous êtes quelque peu persuadé d'écrire `.action()`, `.reduce()` et `.view()` — dans cet ordre. Et vous n'avez pas à créer des entrées pour chacune de ces étapes car elles sont passées le long du flux en arrière-plan.

### Exemple

![Image](https://cdn-media-1.freecodecamp.org/images/1*H0NItfukULQ4qOLFsc_tLQ.jpeg)
_([Source de l'image](https://www.pexels.com/photo/paper-boats-on-solid-surface-194094/" rel="noopener" target="_blank" title="))_

Prenons Redux TDD pour un essai et essayons d'implémenter un composant `<GithubTrending />` de manière TDD. Ce composant va mettre en avant les projets tendances de la semaine. Il aura un bouton de rafraîchissement et un message de chargement qui apparaît lorsque des requêtes sont faites.

Dans l'esprit du vrai TDD, nous allons commencer à imaginer la forme de notre état et les props que notre vue prendra.

Et nous allons faire échouer le test :

```jsx
ReduxTdd({ projects: [], loading: false }, state => shallow(
  <GithubTrending 
    projects={state.projects} 
    loading={state.loading} 
    onRefresh={refreshAction} />
))
```

Testons immédiatement si notre vue a l'air correcte. Nous étendons le chaînage de l'exemple précédent :

```js
.view()
 .contains(<div class="loading" />, false) // ne devrait pas montrer le chargement
 .contains(<div class="projects">No projects</div>)
 .contains(<button class="refresh">refresh</button>)
```

Avant d'implémenter le composant, nous pouvons simuler un `refresh` et vérifier que l'action correcte est appelée :

```js
.simulate(wrapper => wrapper.find('.refresh').simulate('click'))
.action(refreshAction).toMatchAction({ type: 'REFRESH' })
```

Ensuite, nous nous assurons que notre état est changé correctement. Dans cette étape, nous passons l'action précédente à `githubReducer`. Nous devrions nous attendre à ce qu'il définisse l'attribut `loading` à `true` :

```js
.reducer(githubReducer).toMatchState({ loading: true })
```

À ce stade, nous sommes dans l'état où les projets sont en cours de chargement depuis le serveur, donc notre `.view` devrait ressembler à ceci :

```js
.view().contains(<div class="loading" />)
```

Encore une fois, nous n'avons pas écrit une seule ligne de code d'implémentation.

Continuons le flux en passant à l'état où nous avons reçu les données du serveur et affichons la réponse. Ici, l'`.epic` appellera `handleRefreshEpic` avec l'`.action` exécutée le plus tôt dans le pipeline — dans ce cas `refreshAction`. En tant que sortie pour l'opérateur suivant, nous forçons sa dépendance `getJSON` à produire une réponse. Dans le cas où une épopée émet plusieurs actions, nous pouvons appeler `action->reducer` plusieurs fois pour les gérer.

```js
.epic(handleRefreshEpic, { getJSON: () => 
  Observable.of([
    { name: 'redux-tdd' }, { name: 'redux-cycles' }
  ])
}) 
.action(refreshDoneAction).toMatchAction({ 
  type: 'REFRESH_DONE',
  payload: [{ name: 'redux-tdd' }, { name: 'redux-cycles' }],
})
.reducer(githubReducer).toMatchState({
  loading: false,
  projects: [{ name: 'redux-tdd' }, { name: 'redux-cycles' }]
})
```

Je suis verbeux pour montrer ce qui se passe. Vous voudriez évidemment mettre la réponse simulée dans une variable et la passer le long des tests.

Ensuite, assurons-nous que la `.view` a l'air comme prévu après les changements d'état précédents :

```js
.view()
 .contains(<div class="loading" />, false) // ne devrait pas montrer le chargement
 .contains(<div class="projects">
   <div>redux-tdd</div>
   <div>redux-cycles</div>
 </div>)
```

Et nous avons terminé !

Nous pouvons maintenant commencer à écrire le code d'implémentation réel pour essayer de faire passer chacun de nos tests.

Commençons par faire passer le premier opérateur de test, donc la vue :

```jsx
function GithubTrending({ projects, loading, onRefresh }) {
  return <div>
    { loading && <div class="loading" /> }
    <div class="projects">
      { !projects.length && 'No projects' }
      { projects.map(p => <div>{p.name}</div>) }
    </div>
    <button class="refresh" onClick={onRefresh}>refresh</button>
  </div>
}
```

Ensuite, faisons passer nos `.action`s :

```js
function refreshAction() {
  return { type: 'REFRESH' };
}

function refreshDoneAction(payload) {
  return { type: 'REFRESH_DONE', payload };
}
```

Ensuite, notre réducteur :

```js
const initialState = { projects: [], loading: false };

function githubReducer(state = initialState, action) {
  switch (action.type) {
    case 'REFRESH':
      return { ...state, loading: true };
    case 'REFRESH_DONE':
      return { ...state, loading: false, projects: action.payload };
    default:
      return state;
  }
}
```

Et notre épopée :

```js
function handleRefreshEpic(action$, store, { getJSON }) {
  return action$.ofType('REFRESH')
    .mergeMap(() =>
      getJSON('http://foo.bar')
        .map(response => refreshDoneAction(response))
    );
}
```

Nous pouvons voir à partir de cet exemple que l'écriture du code d'implémentation est en fait la partie facile. Ce qui est difficile, c'est de s'assurer que nous avons des flux de test corrects qui suivent les spécifications de nos IU.

Un avantage de l'écriture de tests unitaires composables de cette manière par rapport à des tests séparés dans divers fichiers est que nous générons des entrées pour les unités pilotées par le comportement réel des utilisateurs.

Par exemple, le test qui vérifie si `refreshDoneAction` a été appelé avec la réponse simulée réelle n'aurait peut-être jamais été écrit si nous n'avions pas pensé au flux de données de Redux de cette manière.

D'autre part, Redux TDD vous pousse à réfléchir — et à tester — comment les données circulent dans votre application.

Voici une vidéo montrant le processus itératif de l'écriture de ces tests en utilisant un observateur pour nous informer constamment de ce qui doit être implémenté :

<iframe width="560" height="315" src="https://www.youtube.com/embed/lW1ytOEZx3Y" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Interaction entre plusieurs composants

Jusqu'à présent, nous avons vu comment une action de composant déclenche un changement d'état qui est alimenté au composant lui-même :

![Image](https://cdn-media-1.freecodecamp.org/images/1*RRokGbGhSvWc97PeEqVS3g.png)

La plupart des actions de composant déclenchent des changements qui alimentent également d'autres composants :

![Image](https://cdn-media-1.freecodecamp.org/images/1*j2dDce96Vw0YM9HlVqEXRw.png)

Pour exprimer ce type de comportement dans Redux TDD, nous pouvons rendre plusieurs composants :

```js
ReduxTdd({ count: 0, show: false }, state => ([
  shallow(
    <Counter 
      onIncrement={incrementAction} 
      counter={state.count} />
  ),
  shallow(
    <Modal
      show={state.show} />
  )
]))
```

Nous pouvons simuler des choses comme avant et nous obtenons les enveloppes sous forme de tableau.

Nous voulons montrer le `<Modal />` lorsque la variable d'état count est impaire :

```js
.simulate(([ counterWrapper, modalWrapper ]) =>
  counterWrapper.props.onIncrement() // simuler un clic
)
.action(incrementAction).toMatchAction({ type: 'INCREMENT' })
.reducer(myReducer).toMatchState({ count: 1, show: true })
.view().contains(([ counter, modal ]) =>
  counter.contains(<span>1</span) &&
  modal.contains(<div class="showModal" />)
)
```

Bien que nous puissions tester chacun de ces composants individuellement, nous devons penser au fait que nos composants ne sont pas encore implémentés. Combiner les interactions entre plusieurs composants nous permet d'imaginer quelles props nos composants prendront de manière TDD.

### Tests d'intégration

![Image](https://cdn-media-1.freecodecamp.org/images/1*lnWj3S8D6P699LB98d9_oQ.gif)

Vous vous demandez peut-être si les pipelines de tests unitaires que nous avons définis jusqu'à présent sont considérés comme des tests d'intégration.

Il n'y a pas de définition stricte de ce que signifient les tests d'intégration. Pourtant, je soutiendrais que, par rapport aux tests unitaires, ils nécessitent un surcoût supplémentaire :

1. Ils sont plus coûteux en calcul à exécuter. Par exemple, ils nécessitent un rendu DOM complet.
2. Ils nécessitent des configurations complexes de choses comme les magasins Redux, la simulation de bibliothèques externes et une configuration supplémentaire.

D'autre part, le pipeline Redux TDD ne teste que des fonctions pures. Il n'y a littéralement aucun état externe et aucune configuration requise puisque chaque étape de la chaîne prend en entrée la sortie de l'étape précédente.

### Impératif vs déclaratif

![Image](https://cdn-media-1.freecodecamp.org/images/1*FZdafW2he_we_WOy_0MvWw.jpeg)
_([Source de l'image](https://www.pexels.com/photo/pile-of-books-in-shallow-focus-photography-264635/" rel="noopener" target="_blank" title="))_

La syntaxe de chaînage de points que nous avons introduite, bien que simple et composable, est encore impérative. Cela signifie qu'à chaque étape de la chaîne, nous avons un effet secondaire. Cela pourrait être l'exécution de `expect()` ou la simulation de clics de souris.

Et si nous pouvions encore avoir un moyen de penser au flux Redux en utilisant un style de programmation plus déclaratif ?

Une idée serait d'utiliser la [composition de fonctions](https://medium.com/making-internets/why-using-chain-is-a-mistake-9bc1f80d51ba) avec des fonctions de currying plutôt que le chaînage de points ou la [programmation point-free](http://lucasmreis.github.io/blog/pointfree-javascript/) :

```js
const myTest = flow(
  action(incrementActionMock)({ type: 'INCREMENT' }),
  reducer(reducer)({ count: 1 }),
  view(<div>{1}</div>)
)(ReduxTdd({ count: 0 }, state => 
  <Counter 
    onIncrement={incrementActionMock} 
    count={state.count} />
))

run(myTest)
```

Le principal avantage de cette approche est que nous décrivons nos flux de test en utilisant `[_.flow](https://lodash.com/docs/4.17.4#flow),` plutôt que de les exécuter. L'appel de la fonction `run` à la fin est ce qui va réellement exécuter nos `expect()s`.

Ce style déclaratif peut évidemment être atteint avec la syntaxe de chaînage de points également. Mais la composition de fonctions point-free offre d'autres avantages.

Par exemple, elle nous permet d'étendre des parties du flux avec nos propres implémentations, au lieu d'être lié aux [fonctions exposées par la bibliothèque](https://medium.com/making-internets/why-using-chain-is-a-mistake-9bc1f80d51ba) :

```js
const myIncrementAction = flow(
  action(incrementAction), 
  action => { // transformer l'action de quelque manière }
)
```

Voici un excellent [article](https://simonsmith.io/dipping-a-toe-into-functional-js-with-lodash-fp/) qui approfondit ces concepts de composition de fonctions.

En termes de la manière dont nous pouvons les utiliser, il reste une question ouverte de savoir si ce style déclaratif de définition des tests est réellement meilleur que son homologue impératif.

### Arbres de tests

![Image](https://cdn-media-1.freecodecamp.org/images/1*zqwlsft8_kItlJnKUS5ojQ.jpeg)
_([Source de l'image](https://www.pexels.com/photo/green-pine-tree-leaves-192136/" rel="noopener" target="_blank" title="))_

Vous pourriez penser que vous pourriez implémenter ces tests Redux composables sans avoir besoin d'une bibliothèque comme Redux TDD.

Redux TDD est une combinaison de fonctions d'assistance mettant en avant l'idée la plus importante. Le flux de données de Redux peut être testé en composant des tests unitaires ensemble.

En prenant un indice de la composition fonctionnelle précédente, on peut imaginer avoir des **arbres de tests** plutôt que les blocs de code `describe()` et `it()` communs.

Nous pouvons représenter ces flux sous forme d'arbres. Au lieu de construire à partir de l'étape la plus précoce, nous pouvons nous ramifier dans d'autres états.

Avec la composition fonctionnelle, décrire ces arbres peut être amusant :

```js
flow(
  flow(
    action(increment),
    reducer(githubReducer),
    view(<div>1</div>)
  ), // cette branche a l'état { count: 1 }
  flow(
    action(decrement),
    reducer(githubReducer),
    view(<div>-1</div>),
    flow(
      action(increment),  
      reducer(githubReducer),
      view(<div>0</div>),
    )
  )({ count: 0 }) // ne pas obtenir l'état de la branche précédente
)({ count: 0 })
```

Encore une fois, je suis verbeux. Mais nous traitons avec des fonctions pures. Par exemple, nous pouvons définir un `simulateClick(increment)` pour éviter une partie du code dupliqué.

Je soutiendrais que le fait d'avoir ces types d'arbres de fonctions décrivant vos flux de test, plutôt qu'un tas de blocs `it('should do this')`, est une approche intéressante qui devrait être étudiée davantage.

Nous pouvons tester des états de nos IU qui se lisent plus comme des spécifications de ce que l'utilisateur a fait.

Si une nouvelle combinaison vient à l'esprit, nous pouvons l'ajouter à l'arbre :

```js
flow(
  branch(
    clickButton, shouldShowModal, clickCloseModal, shouldCloseModal
  ),
  branch(
    clickCloseModal, 
    nothingShouldHappen,
    branch(clickButton, shouldShowModal)
    clickButton,
    shouldShowSpinner
  )
)
```

Les exemples ci-dessus ne sont que des idées. Rien de tout cela n'est encore implémenté dans Redux TDD. Nous pouvons composer les fonctions primitives précédentes pour lire comme si quelque chose se produisait.

La ramification est utile lorsque nous ne voulons pas modifier l'état de la branche parente. Par exemple, le `**clickButton**` dans l'exemple le plus précoce ne saura pas que la branche au-dessus a cliqué sur le même bouton.

Ces types de tests sont similaires au [langage Gherkin](https://github.com/cucumber/cucumber/wiki/Gherkin). Nous décrivons le comportement du logiciel sans détailler comment ce comportement est implémenté.

### L'avenir des tests d'IU dans un monde fantastique

![Image](https://cdn-media-1.freecodecamp.org/images/1*TcWD4gZHNRFeRSUQN5xggg.jpeg)
_([Source de l'image](https://www.pexels.com/photo/close-up-of-leaf-326055/" rel="noopener" target="_blank" title="))_

Bien que la plupart de ces concepts existent déjà dans le contexte du BDD, ils n'ont pas été beaucoup explorés dans le monde Redux.

Décrire ces flux sous forme d'arbres n'est pratique que grâce à la pureté de Redux.

Je ne sais pas personnellement si de tels tests peuvent être décrits de cette manière en utilisant d'autres paradigmes de gestion d'état qui ne sont pas purs et unidirectionnels.

La pureté est un concept critique qui nous permet de construire de tels arbres descriptifs.

⚠️ AVERTISSEMENT : déclarations audacieuses et biaisées dans les prochains paragraphes.

On peut imaginer que la majeure partie du développement futur des IU ne sera rien d'autre que l'écriture d'arbres de tests. Tout le reste n'est qu'un détail d'implémentation.

Je sais que c'est une déclaration audacieuse, mais je suis prêt à parier que les développeurs front-end de l'avenir passeront la plupart de leur temps à écrire des **arbres de tests**.

La manière dont les composants, réducteurs, actions et effets secondaires réels seront écrits dépendra entièrement de tels tests. Ceux-ci :  
(i) peuvent être automatisés si suffisamment de combinaisons sont couvertes par des tests  
(ii) peuvent être facilement externalisés  
(iii) peuvent être trouvés sous forme de bibliothèques.

### Conclusion

Dans cet article, j'ai essayé de jeter un peu de lumière sur le fait que le TDD peut être amusant.

Définir nos tests comme si nous interagissions avec le composant rend plus facile la compréhension de ce qui doit être testé. Les entrées de vos tests unitaires sont générées via le comportement réel des utilisateurs.

Nous avons plongé dans le [monde fantastique de la programmation fonctionnelle](https://github.com/fantasyland/fantasy-land) et discuté de la manière dont certains de ces concepts peuvent être utiles pour écrire des tests.

Le nombre d'interactions qu'un utilisateur effectue sur un composant peut être décrit en utilisant un arbre. Nous avons également examiné les arbres de fonctions et comment nous pouvons combiner des fonctions curryfiées ensemble pour les construire.

J'ai introduit Redux TDD comme un exemple concret de certains de ces concepts. Ses fonctions sont destinées à vous aider à rationaliser vos tests unitaires Redux.

À l'avenir, j'espère présenter une approche plus fonctionnelle, plus proche de l'idée des arbres de fonctions que nous avons discutée ici.

Vous pouvez essayer redux-tdd en le téléchargeant depuis [GitHub](https://github.com/lmatteis/redux-tdd).

Veuillez partager sur les réseaux sociaux si vous avez apprécié cet article.