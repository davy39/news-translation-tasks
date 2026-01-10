---
title: Explorons les avantages de Cycle.js et Model-View-Intent
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-05-14T18:50:02.000Z'
originalURL: https://freecodecamp.org/news/exploring-cycle-js-and-model-view-intent-ada5ed82da22
coverImage: https://cdn-media-1.freecodecamp.org/images/1*r980RzYbz7ShlZEYsd089A.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Explorons les avantages de Cycle.js et Model-View-Intent
seo_desc: 'By Fabio Hiroki

  In the current software development ecosystem, it''s not surprising that Model-View-Controller
  (MVC) architecture doesn’t have a great reputation. Common alternatives have been
  gaining popularity, such as Model-View-Presenter (MVP) and...'
---

Par Fabio Hiroki

Dans l'écosystème actuel du développement logiciel, il n'est pas surprenant que l'architecture Model-View-Controller (MVC) n'ait pas une grande réputation. Des alternatives courantes ont gagné en popularité, telles que Model-View-Presenter (MVP) et Model-View-ViewModel (MVVM).

En tant que développeur mobile, j'ai essayé l'architecture MVP. Et en fait, j'ai eu une meilleure expérience grâce à la séparation des préoccupations et à l'amélioration de la testabilité fournies par cette architecture. Mais elle ne propose pas de modèle pour le flux de données (comme Flux ou Redux), et je me sentais quelque peu insatisfait par cela. Je me demandais s'il existait un moyen de minimiser les bugs et de fournir une meilleure expérience développeur.

### Model-View-Intent (MVI)

Le premier concept qui a attiré mon attention était l'implémentation Model-View-Intent (MVI) sur Android proposée par la bibliothèque [Mosby](https://github.com/sockeqwe/mosby). J'ai décidé de lire son code et d'essayer de comprendre ses principes.

Mosby semblait être une grande bibliothèque, surtout parce que son créateur a bien documenté sa motivation et publié des exemples sur son [blog](http://hannesdorfmann.com/mosby/). Mais malheureusement, Mosby semblait trop complexe. Il avait une courbe d'apprentissage abrupte et n'était pas exactement ce que je cherchais — et représentait seulement une petite amélioration incrémentielle par rapport à MVP.

Le concept MVI n'a pas été introduit pour la première fois par Mosby, mais plutôt par un framework web appelé [Cycle.js](https://cycle.js.org/). J'ai donc décidé d'apprendre les bases. À ma grande surprise, Cycle.js m'a fait aimer l'idée de MVI et m'a donné envie de l'essayer. Principalement parce que le framework est très petit et simple.

Voici les principes de base de MVI, et pourquoi ils ont une grande valeur :

* **Purement réactif** : cela rend beaucoup plus facile la coordination des tâches asynchrones, et apporte tous les [avantages](https://tylermcginnis.com/imperative-vs-declarative-programming/) de la programmation déclarative. Dans le cas de Cycle.js, cela rend votre **vue** testable. Comme nous allons le voir ci-dessous, la vue devient simplement un **observable** commun.
* **Flux de données unidirectionnel** : dans MVI, les données suivent un chemin droit d'**intent**, **modèle**, et **vue**. Je vais discuter de cela en détail dans la section suivante. Mais pour l'instant, cela signifie que vous, en tant que développeur, devez apprendre à organiser votre code pour utiliser ce modèle. Une fois que vous avez surmonté la courbe d'apprentissage, votre application devient plus facile à comprendre. Chaque fonctionnalité de votre application suit la même recette.
* **La** couche de vue est représentée par un seul objet, le modèle : l'état entier de la **vue** est représenté par une source unique de vérité, y compris les états de **chargement** et d'**erreur**. Cela signifie que vous devez regarder et manipuler un seul endroit afin d'afficher correctement la vue.

Plus de détails sur la conception MVI et ses avantages sont décrits dans [cet article](http://futurice.com/blog/reactive-mvc-and-the-virtual-dom) par le créateur de Cycle.js et aussi dans [cet article](https://medium.com/@fkrautwald/plug-and-play-all-your-observable-streams-with-cycle-js-e543fc287872). Je recommande de lire les deux pour avoir une meilleure compréhension même si vous n'avez pas de background en développement web.

### MVI dans une application réelle

![Image](https://cdn-media-1.freecodecamp.org/images/f6tnoMKQNH7s3ekf1IPZob1FoilxvGTYEkjn)
_L'application que j'ai construite en utilisant Cycle.js_

Après avoir acquis une brève compréhension de MVI, j'ai décidé de construire une application en utilisant Cycle.js pour vérifier ses avantages de manière pratique. L'application que j'ai construite fournit une liste initiale de personnages puis effectue des requêtes de recherche sur [Star Wars API](https://swapi.co/) lorsque vous tapez quelque chose dans le champ de texte. Vous pouvez voir le code dans ce [dépôt](https://github.com/fabiothiroki/cyclejs-starwars).

La structure principale d'une application Cycle.js est une abstraction du concept d'interaction homme-machine. Cela est représenté par une seule fonction où toute interaction externe est passée en tant que paramètre de fonction (généralement appelé "sources"), et la sortie "humaine" est l'objet retourné par la fonction (généralement appelé "sinks").

Dans notre application, cela est représenté par la méthode "App" dans le fichier "app.js". Le code placé entre l'entrée et la sortie transformera les "sources" en un **intent observable**, qui est transformé en un **modèle observable**. Ce dernier est ensuite transformé en un **vue observable** qui est retourné à l'intérieur de l'objet "sinks".

```
export function App (sources) {
```

```
  // ...
```

```
  return sinks;}
```

Nous allons construire chaque couche de manière incrémentielle dans le même ordre que le flux de données.

### Intent

L'objet intent contient des **observables** générés à partir de l'objet "sources". Il représente l'intention de l'utilisateur lors de l'interaction avec l'application. Dans notre application, un utilisateur peut faire deux choses :

* Saisir un terme de recherche en tapant sur le champ de texte
* Recevoir les données des personnages de l'API

```
const intents = {  receiveCharacterList: sources.HTTP.select('api').flatten(),
```

```
  changeSearchTerm: sources.DOM.select('#search.form-control')    .events("input")    .map(ev => ev.target.value)    .startWith('')}
```

Vous n'avez pas besoin de vous inquiéter si vous ne comprenez pas la propriété receiveCharacterList de l'objet **intents**. Pour l'instant, pour comprendre le concept MVI, vous devez simplement comprendre ceci : changeSearchTerm reçoit un nouvel **observable** chaque fois que l'utilisateur tape quelque chose dans le champ qui a un id de "search.form-control". Par défaut, il commence avec une chaîne vide.

### Modèle

Le **modèle**, comme je l'ai mentionné ci-dessus, est la représentation de l'état actuel de la **vue**. Il dépend uniquement de l'objet **intents**.

```
const model = Observable.combineLatest(  intents.receiveCharacterList,   intents.changeSearchTerm)  .map((combined) => {
```

```
    const [response, searchTerm] = combined
```

```
    return {      characters: response.body.results,      searchTerm: searchTerm    }; }) .startWith({   characters: [{name: 'Loading…'}],   searchTerm: '' });
```

Ici, nous combinons l'observable contenant la réponse de l'API avec l'observable contenant la **chaîne** tapée. Le résultat est un nouvel observable contenant la liste des personnages et le terme de recherche.

### Vue

La **vue** dans Cycle.js n'est pas représentée par du HTML ou par une couche de contrôleur, comme nous le voyons couramment dans les applications mobiles. La configuration par défaut de Cycle.js utilise une bibliothèque appelée [Cycle DOM](https://cycle.js.org/api/dom.html), qui peut générer un observable à partir d'une abstraction de Virtual DOM [abstraction](https://github.com/snabbdom/snabbdom).

```
const view = model.map((state) => {
```

```
  const list = state.characters.map( character => {    return tr(td(character.name));  });
```

```
  return div("card", [    div('card-header', [      h4('title', 'Star Wars Character Search'),      input('#search.form-control', {props: {type: "text", placeholder: "Type to search", value: state.searchTerm}})    ]),    div('card-content .table-responsive',[      table('.table', [        thead(tr(th(h5('Name')))),        tbody(list)      ])    ])  ]);});
```

Comme je l'ai mentionné ci-dessus, la vue dépend uniquement du **modèle**. Elle génère un tableau HTML pour lister les personnages et remplit le **champ de texte** avec la chaîne tapée.

À la fin de notre fonction "App", la vue fait partie de l'objet "sinks" retourné. Les "sinks" doivent également contenir la configuration de la requête HTTP à l'API :

```
return {  DOM: view,  HTTP: intents.changeSearchTerm.map( searchTerm => {    return {      url: 'https://swapi.co/api/people/?search=' + searchTerm,      category: 'api',    }  })};
```

### Tests unitaires de la vue

Étant donné que la représentation de la vue est simplement une fonction du modèle, nous pouvons facilement écrire des tests unitaires pour celle-ci. Tout d'abord, j'ai extrait la création de la vue dans une méthode et l'ai déplacée dans un fichier séparé. Cela m'a permis de l'utiliser dans l'application et dans les tests. Ensuite, j'ai utilisé le package [chai-virtual-dom](https://github.com/staltz/chai-virtual-dom) pour comparer deux vues.

Les tests que j'ai implémentés suivent cette structure de base :

1. Créer un **mock** du modèle de l'état que nous voulons tester.
2. Utiliser la fonction **vue** en passant le mock créé pour générer sa vue.
3. Vérifier si la vue créée est égale à la vue attendue.

Dans cette application, j'ai créé deux cas de test simples :

* Lorsque l'application charge les données de l'API, la vue doit afficher un état de **chargement** :

```
const model = Observable.of({ characters: [{name: 'Loading…'}], searchTerm: ''});
```

```
const view = view(model);
```

```
const expected = div(".card", [  div('.card-header', [    h4('.title', 'Star Wars Character Search'),    input('#search.form-control', {props: {type: "text", placeholder: "Type to search"}})  ]),  div('.card-content .table-responsive',[    table('.table', [      thead(tr(th(h5('Name')))),        tbody([          tr(td('Darth Vader')),          tr(td('Darth Maul')),        ])      ])    ])  ]);
```

```
expect(view).to.look.exactly.like(expected);
```

* Lorsque l'application a reçu les données des personnages de l'API, la vue doit les afficher :

```
const model = Observable.of({  characters: [{name: 'Darth Vader'}, {name: 'Darth Maul'}],  searchTerm: 'darth'});
```

```
const view = view(model);
```

```
const expected$ = div(".card", [  div('.card-header', [    h4('.title', 'Star Wars Character Search'),    input('#search.form-control', {props: {type: "text", placeholder: "Type to search"}})  ]),  div('.card-content .table-responsive',[    table('.table', [      thead(tr(th(h5('Name')))),        tbody([          tr(td('Darth Vader')),          tr(td('Darth Maul')),        ])      ])    ])  ]);
```

```
expect(view).to.look.exactly.like(expected);
```

### Conclusion

J'ai eu une excellente première impression de l'architecture Model-View-Intent. Le code semble plus organisé et plus facile à comprendre, ce qui offre une meilleure expérience développeur. La communication entre un objet et ses responsabilités est déjà prédéfinie, donc vous n'avez pas à prendre trop de décisions lors de la programmation.

En fin de compte, MVI ne demande pas beaucoup d'efforts pour être appris et semble être un meilleur choix en comparaison avec MVP.

Et Cycle.js ? Je ne suis pas encore à 100 % confiant que je peux commencer à construire une application de production en utilisant Cycle.js. Je pense que je dois explorer davantage le framework pour évaluer ses capacités réelles, comme la création de routes ou d'un système d'authentification.

Avez-vous aimé cet article ? Si oui, veuillez m'applaudir pour que plus de gens le voient. Merci !