---
title: Créer un explorateur de dépôt GitHub avec React et Elasticsearch
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-10T21:57:37.000Z'
originalURL: https://freecodecamp.org/news/building-a-github-repo-explorer-with-react-and-elasticsearch-8e1190e59c13
coverImage: https://cdn-media-1.freecodecamp.org/images/1*QunMstJjXbPkRfFwRBVVkg.png
tags:
- name: elasticsearch
  slug: elasticsearch
- name: JavaScript
  slug: javascript
- name: open source
  slug: open-source
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Créer un explorateur de dépôt GitHub avec React et Elasticsearch
seo_desc: 'By Divyanshu Maithani


  _The [GitXplore](https://appbaseio-apps.github.io/gitxplore-app/" rel="noopener"
  target="blank" title=") app

  Elasticsearch is one of the most popular full-text search engines which allows you
  to search huge volumes of data quic...'
---

Par Divyanshu Maithani

![Image](https://cdn-media-1.freecodecamp.org/images/1*QunMstJjXbPkRfFwRBVVkg.png)
_L'application [GitXplore](https://appbaseio-apps.github.io/gitxplore-app/" rel="noopener" target="_blank" title=")_

[Elasticsearch](https://www.elastic.co/products/elasticsearch) est l'un des moteurs de recherche en texte intégral les plus populaires, permettant de rechercher rapidement d'énormes volumes de données, tandis que [React](https://reactjs.org/) est sans doute [la meilleure bibliothèque](http://stateofjs.com/2017/front-end/results/) pour construire des interfaces utilisateur. Au cours des derniers mois, j'ai co-écrit une bibliothèque open-source, [**ReactiveSearch**](https://github.com/appbaseio/reactivesearch), qui fournit des composants React pour Elasticsearch et simplifie le processus de création d'une interface utilisateur de recherche (UI).

Voici l'application que je vais construire dans cette histoire :

![Image](https://cdn-media-1.freecodecamp.org/images/1*KPB8Sq7N3WId2jL57VGT-Q.png)
_Découvrez l'application sur [CodeSandbox](https://codesandbox.io/s/github/appbaseio-apps/gitxplore-app/tree/master/" rel="noopener" target="_blank" title=")_

### Une brève idée d'Elasticsearch

Elasticsearch est une base de données [NoSQL](https://en.wikipedia.org/wiki/NoSQL) qui peut rechercher de grandes quantités de données en peu de temps. Il effectue une [recherche en texte intégral](https://en.wikipedia.org/wiki/Full-text_search) sur les données qui sont stockées sous forme de documents (comme des objets) en examinant tous les mots de chaque document.

Voici ce que disent les [documents Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started.html) :

> Elasticsearch est un moteur de recherche et d'analyse en texte intégral open-source hautement scalable. Il permet de stocker, rechercher et analyser de grands volumes de données rapidement et en temps quasi réel.

Même si vous n'avez jamais utilisé Elasticsearch auparavant, vous devriez pouvoir suivre cette histoire et construire votre propre recherche alimentée par Elasticsearch en utilisant React et ReactiveSearch. ?

### Qu'est-ce que ReactiveSearch ?

[ReactiveSearch](https://github.com/appbaseio/reactivesearch) est une bibliothèque de composants UI React pour Elasticsearch. Afin de rechercher des données dans Elasticsearch, vous devez écrire des [**requêtes**](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html). Ensuite, vous devrez formater et rendre les données JSON dans votre UI. ReactiveSearch simplifie l'ensemble du processus puisque vous n'avez pas à vous soucier d'écrire ces requêtes. Cela facilite la concentration sur la création de l'UI.

Voici un exemple qui génère une UI de boîte de recherche avec des suggestions spécifiques à la catégorie :

```js
<CategorySearch
  componentId="repo"
  dataField={["name", "name.raw"]}
  categoryField="language.raw"
/>
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*2wZ7uDqfizcjV9JCnre0mQ.png)
_Composant rendu à partir du code ci-dessus_

Cela nous aurait probablement pris 100+ lignes sans la bibliothèque, et la connaissance du [DSL de requête Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html) pour construire la requête.

Dans cet article, j'utiliserai différents composants de la bibliothèque pour construire l'UI finale.

Vous devriez essayer [l'application finale](https://appbaseio-apps.github.io/gitxplore-app/) avant de plonger en profondeur. Voici le [lien CodeSandbox](https://codesandbox.io/s/github/appbaseio-apps/gitxplore-app/tree/master/) pour la même application.

### Configuration des éléments

Avant de commencer à construire l'UI, nous aurons besoin du jeu de données contenant les dépôts GitHub dans Elasticsearch. ReactiveSearch fonctionne avec n'importe quel index Elasticsearch et vous pouvez facilement [l'utiliser avec votre propre jeu de données](https://opensource.appbase.io/reactive-manual/getting-started/reactivebase.html).

Pour faire court, vous pouvez utiliser [mon jeu de données](https://opensource.appbase.io/dejavu/live/#?input_state=XQAAAAJDAQAAAAAAAAA9iIqnY-B2BnTZGEQz6wkFsoFSyhi0TotY1ZI3dCbzpZ5wZmCa4HoWjWiBHcRO1KpPWzrR3-ungbYF_FBD7IY3vlhuTW9dQQFtt3qksr-wGqyFf_qxW2Z3widjMRY5xGpv9lCIh4b5Dyi-O2wVMmUzKADc-0pG1tyzQ558Y_SoViZ27V2qq-px_fIGV-GVRTcrO-LdiYhDhtFK4tYVTak07UxRRvGaqeK3GI2sU7O67YnSdDZNv8_5pnc3SPxlPV9t9YdkGW3YkckG3LAVp03TbrSWI7GdN0fMZCgwqWv0FP1iNWHQrUW2v8-B___Y4BHg) ou le cloner pour vous-même en suivant [ce lien](https://opensource.appbase.io/dejavu/live/#?input_state=XQAAAAJDAQAAAAAAAAA9iIqnY-B2BnTZGEQz6wkFsoFSyhi0TotY1ZI3dCbzpZ5wZmCa4HoWjWiBHcRO1KpPWzrR3-ungbYF_FBD7IY3vlhuTW9dQQFtt3qksr-wGqyFf_qxW2Z3widjMRY5xGpv9lCIh4b5Dyi-O2wVMmUzKADc-0pG1tyzQ558Y_SoViZ27V2qq-px_fIGV-GVRTcrO-LdiYhDhtFK4tYVTak07UxRRvGaqeK3GI2sU7O67YnSdDZNv8_5pnc3SPxlPV9t9YdkGW3YkckG3LAVp03TbrSWI7GdN0fMZCgwqWv0FP1iNWHQrUW2v8-B___Y4BHg) et en cliquant sur le bouton _Cloner cette application_. Cela vous permettra de faire une copie du jeu de données en tant que votre propre application.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5tXgJvJROclI-NFXUKziIQ.png)
_Le jeu de données [dataset](https://opensource.appbase.io/dejavu/live/#?input_state=XQAAAAJDAQAAAAAAAAA9iIqnY-B2BnTZGEQz6wkFsoFSyhi0TotY1ZI3dCbzpZ5wZmCa4HoWjWiBHcRO1KpPWzrR3-ungbYF_FBD7IY3vlhuTW9dQQFtt3qksr-wGqyFf_qxW2Z3widjMRY5xGpv9lCIh4b5Dyi-O2wVMmUzKADc-0pG1tyzQ558Y_SoViZ27V2qq-px_fIGV-GVRTcrO-LdiYhDhtFK4tYVTak07UxRRvGaqeK3GI2sU7O67YnSdDZNv8_5pnc3SPxlPV9t9YdkGW3YkckG3LAVp03TbrSWI7GdN0fMZCgwqWv0FP1iNWHQrUW2v8-B___Y4BHg" rel="noopener" target="_blank" title=")_

Après avoir entré un nom d'application, le processus de clonage devrait commencer à importer les 26K+ dépôts dans votre compte.

Tous les dépôts sont structurés dans le format suivant :

```json
{
  "name": "freeCodeCamp",
  "owner": "freeCodeCamp",
  "fullname": "freeCodeCamp~freeCodeCamp",
  "description": "Le code source open source et le programme de https://freeCodeCamp.org. Apprenez à coder et aidez les organisations à but non lucratif.",
  "avatar": "https://avatars0.githubusercontent.com/u/9892522?v=4",
  "url": "https://github.com/freeCodeCamp/freeCodeCamp",
  "pushed": "2017-12-24T05:44:03Z",
  "created": "2014-12-24T17:49:19Z",
  "size": 31474,
  "stars": 291526,
  "forks": 13211,
  "topics": [
    "carrières",
    "certification",
    "communauté",
    "programme",
    "d3",
    "éducation",
    "javascript",
    "apprendre-à-coder",
    "math",
    "nodejs",
    "organisations-à-but-non-lucratif",
    "programmation",
    "react",
    "enseignants"
  ],
  "language": "JavaScript",
  "watchers": 8462
}
```

* Nous utiliserons [create-react-app](https://github.com/facebookincubator/create-react-app.) pour configurer le projet. Vous pouvez installer create-react-app en exécutant la commande suivante dans votre terminal :

```bash
npm install -g create-react-app
```

* Après son installation, vous pouvez créer un nouveau projet en exécutant :

```bash
create-react-app gitxplore
```

* Après la configuration du projet, vous pouvez changer de répertoire de projet et installer la dépendance ReactiveSearch :

```bash
cd gitxplore
npm install @appbaseio/reactivesearch
```

* Vous pouvez également ajouter le CDN de fontawesome, que nous utiliserons pour certaines icônes, en insérant les lignes suivantes dans `/public/index.html` avant la fin de la balise `</body>` :

```html
<script defer src="https://use.fontawesome.com/releases/v5.0.2/js/all.js"></script>
```

### Plongeons dans le code

Je vais suivre une structure de répertoire simple pour l'application. Voici les fichiers importants :

```
src
├── App.css               // Styles de l'application
├── App.js                // Conteneur de l'application
├── components
│   ├── Header.js         // Composant d'en-tête
│   ├── Results.js        // Composant de résultats
│   ├── SearchFilters.js  // Composant de filtres
│   └── Topic.js          // rendu par Results
├── index.css             // styles
├── index.js              // rendu ReactDOM
└── theme.js              // couleurs et polices
public
└── index.html
```

Voici le lien vers le [dépôt final](https://github.com/appbaseio-apps/gitxplore-app) si vous souhaitez vous référer à quelque chose à un moment donné.

#### 1. Ajout de styles

J'ai écrit des styles réactifs pour l'application que vous pouvez copier dans votre application. Lancez simplement votre éditeur de texte préféré et copiez les styles pour `/src/index.css` depuis [ici](https://github.com/appbaseio-apps/gitxplore-app/blob/master/src/index.css) et `/src/App.css` depuis [ici](https://github.com/appbaseio-apps/gitxplore-app/blob/master/src/App.css) respectivement.

Maintenant, créez un fichier `/src/theme.js` où nous ajouterons les couleurs et les polices pour notre application :

```js
const theme = {
	typography: {
		fontFamily: 'Raleway, Helvetica, sans-serif',
	},
	colors: {
		primaryColor: '#008000',
		titleColor: 'white'
	},
	secondaryColor: 'mediumseagreen',
};

export default theme;
```

#### 2. Ajout du premier composant ReactiveSearch

Tous les composants ReactiveSearch sont enveloppés autour d'un composant conteneur [**ReactiveBase**](https://opensource.appbase.io/reactive-manual/getting-started/reactivebase.html) qui fournit des données d'Elasticsearch aux composants enfants ReactiveSearch.

Nous allons l'utiliser dans `/src/App.js` :

```js
import React, { Component } from 'react';
import { ReactiveBase } from '@appbaseio/reactivesearch';
import theme from './theme';
import './App.css';
class App extends Component {
  render() {
    return (
      <section className="container">
        <ReactiveBase
          app="gitxplore-app"
          credentials="4oaS4Srzi:f6966181-1eb4-443c-8e0e-b7f38e7bc316"
          type="gitxplore-latest"
          theme={theme}
        >
          <nav className="navbar">
            <div className="title">GitXplore</div>
          </nav>
        </ReactiveBase>
      </section>
    );
  }
}
export default App;
```

Pour les props `app` et `credentials`, vous pouvez utiliser celles que j'ai fournies ici telles quelles. Si vous avez cloné le jeu de données dans votre propre application plus tôt, vous pouvez les obtenir depuis la [page des identifiants de l'application](https://dashboard.appbase.io/credentials). Si vous êtes déjà familiarisé avec Elasticsearch, vous pouvez plutôt passer une prop `url` faisant référence à [votre propre URL de cluster Elasticsearch](https://opensource.appbase.io/reactive-manual/getting-started/reactivebase.html#props).

![Image](https://cdn-media-1.freecodecamp.org/images/1*bI_3-Hej71eLbiVCGoK_hw.png)
_Obtenir les identifiants de l'application depuis le tableau de bord [dashboard](https://dashboard.appbase.io/credentials" rel="noopener" target="_blank" title="). Il suffit de copier la clé API en lecture seule_

Alternativement, vous pouvez également copier les `credentials` de votre application depuis le [tableau de bord des applications](https://dashboard.appbase.io/apps). Survolez la carte de votre application et cliquez sur _Copier les identifiants de lecture_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5k1jVr3YHGBQ0Ts02gjL7g.png)
_Alternative au lien ci-dessus : Copier les identifiants de lecture depuis le [tableau de bord des applications](https://dashboard.appbase.io/apps" rel="noopener" target="_blank" title=")_

Après avoir ajouté cela, vous devriez voir une mise en page de base comme celle-ci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*P4WcAczVGDzrTm42prVSGA.png)
_Après avoir ajouté le premier composant ReactiveSearch_

#### 3. Ajout d'une DataSearch

![Image](https://cdn-media-1.freecodecamp.org/images/1*yNVLrcjB1KEz1X_1s4RHaQ.png)
_Composant DataSearch_

Ensuite, j'ajouterai un composant [DataSearch](https://opensource.appbase.io/reactive-manual/search-components/datasearch.html) pour rechercher dans les dépôts. Il crée un composant d'UI de recherche et nous permet de rechercher facilement dans un ou plusieurs champs. La fonction `render` mise à jour dans `/src/App.js` ressemblerait à ceci :

```js
// importer DataSearch ici
import { ReactiveBase, DataSearch } from '@appbaseio/reactivesearch';
...
<ReactiveBase ... >
// Ajout de DataSearch ici
    <div className="flex row-reverse app-container">
        <div className="results-container">
            <DataSearch
                componentId="repo"
                filterLabel="Recherche"
                dataField={['name', 'description', 'name.raw', 'fullname', 'owner', 'topics']}
                placeholder="Rechercher des dépôts"
                autosuggest={false}
                iconPosition="left"
                URLParams
                className="data-search-container results-container"
                innerClass={{
                    input: 'search-input',
                }}
            />
        </div>
    </div>
</ReactiveBase>
...
```

Le composant `DataSearch` va à l'intérieur du composant `ReactiveBase` et reçoit toutes les données nécessaires de celui-ci, donc nous n'avons pas à écrire nous-mêmes les requêtes Elasticsearch. Les `div` environnantes ajoutent certaines propriétés `className` pour le style. Celles-ci ajoutent simplement une mise en page à l'application. Vous pouvez parcourir tous les styles dans `/src/App.css` que nous avons créés précédemment. Vous avez peut-être remarqué que nous avons passé certaines props au composant `DataSearch`.

Voici comment elles fonctionnent :

* `componentId` : un identifiant de chaîne unique que nous utiliserons plus tard pour connecter deux composants ReactiveSearch différents.
* `filterLabel` : une valeur de chaîne qui apparaîtra dans le menu des filtres plus tard.
* `dataField` : un tableau de chaînes contenant des champs Elasticsearch sur lesquels la recherche doit être effectuée. Vous pouvez vérifier [le jeu de données](https://opensource.appbase.io/dejavu/live/#?input_state=XQAAAAJiAQAAAAAAAAA9iIqnY-B2BnTZGEQz6wkFsg1HFhlgIIPlpmP5RRZ-FWEcoSd0PjkMiILXm8GQxirVSZVrDiQlmtqn4TuMTBL2E1thSmnTeiFPBGQoqmavHhOSSrRxNeEjhNKDeff0pgxw5r5nv8t-un2YUoHpv1HKzI9aZA8KH8WAmQ6XktDDO-Hn95KeD_KPXp_E76PZ04Hl6H6MrevzUojYDnGynyNwjmI07lj0kXZeqltXcATyP8PMY7ncPHlUw1p1cnfe2JXyFgzRzZcNo7xtVJiEPCuLLKzxYehuirtvUcy6oC_KC15q9kmkWssXUCkBr7dAugoFbtjO5zUdpOFWdcz2wcD3AA3--k7h&editable=false) et voir que ces champs correspondent également au nom de la colonne. Tous les champs spécifiés ici correspondent à la structure des données, par exemple `name` fait référence au nom du dépôt, `description` fait référence à sa description, mais il y a un champ avec un `.raw` ajouté ici, `name.raw` qui est un [champ multi](https://www.elastic.co/guide/en/elasticsearch/reference/current/multi-fields.html) du champ `name`. Elasticsearch peut indexer les mêmes données de différentes manières pour différents usages, que nous pouvons utiliser pour obtenir de meilleurs résultats de recherche.
* `placeholder` : définit la valeur du placeholder dans la boîte d'entrée.
* `autosuggest` : définir une valeur `false` pour la prop fait que les résultats se mettent à jour immédiatement dans les résultats.
* `iconPosition` : définit la position de l'icône ?.
* `URLParams` : est un `boolean` qui indique au composant d'enregistrer le terme de recherche dans l'URL du navigateur afin que nous puissions partager une URL vers une requête de recherche spécifique. Par exemple, vérifiez [ce lien](https://appbaseio-apps.github.io/gitxplore-app/?repo=%22react%22) pour voir tous les résultats liés à "react".
* `className` : ajoute une `classe` pour le style en utilisant CSS.
* `innerClass` : ajoute une `classe` à différentes sections d'un composant pour le style en utilisant CSS. Ici, j'ai ajouté une `classe` à la boîte `input` pour le style. Une description détaillée peut être trouvée dans les [docs](https://opensource.appbase.io/reactive-manual/search-components/datasearch.html#props).

Avec cela, notre application devrait obtenir une barre de recherche fonctionnelle :

![Image](https://cdn-media-1.freecodecamp.org/images/1*OLNYIuRpYi9AuPckJ9G_4w.png)
_Ajout du composant DataSearch_

#### 4. Ajout de la vue des résultats

Ensuite, nous allons ajouter le composant `Results` à `/src/components/Results.js` et l'importer dans `/src/App.js`.

Voici comment vous pouvez écrire le composant `Results` :

```js
import React from 'react';
import { SelectedFilters, ReactiveList } from '@appbaseio/reactivesearch';
const onResultStats = (results, time) => (
  <div className="flex justify-end">
    {results} résultats trouvés en {time}ms
  </div>
);
const onData = (data) => (
  <div className="result-item" key={data.fullname}>
    {data.owner}/{data.name}
  </div>
);
const Results = () => (
  <div className="result-list">
    <SelectedFilters className="m1" />
    <ReactiveList
      componentId="results"
      dataField="name"
      onData={onData}
      onResultStats={onResultStats}
      react={{
        and: ['repo'],
      }}
      pagination
      innerClass={{
        list: 'result-list-container',
        pagination: 'result-list-pagination',
        resultsInfo: 'result-list-info',
        poweredBy: 'powered-by',
      }}
      size={6}
    />
  </div>
);
export default Results;
```

J'ai importé deux nouveaux composants de ReactiveSearch, `SelectedFilters` et `ReactiveList`. [SelectedFilters](https://opensource.appbase.io/reactive-manual/base-components/selectedfilters.html) rendra les filtres pour nos composants ReactiveSearch à un seul endroit :

![Image](https://cdn-media-1.freecodecamp.org/images/1*FAROoZa3fhXuE5-H8_FJog.png)
_SelectedFilters rend les filtres supprimables_

[ReactiveList](https://opensource.appbase.io/reactive-manual/result-components/reactivelist.html) rend les résultats de la recherche. Voici comment ses props fonctionnent :

* `dataField` : trie les résultats en utilisant le champ `name` ici.
* `onData` : accepte une fonction qui retourne un [JSX](https://reactjs.org/docs/glossary.html#jsx). La fonction est passée à chaque résultat individuellement. Ici, nous générons une UI basique que nous modifierons plus tard.
* `onResultStats` : similaire à `onData` mais pour les statistiques des résultats. La fonction est passée au nombre de `résultats` trouvés et au `temps` pris.
* `react` : la prop `[react](https://opensource.appbase.io/reactive-manual/advanced/react.html)` indique à `ReactiveList` d'écouter les changements effectués par le composant `CategorySearch`, nous avons fourni le `componentId` du composant `CategorySearch` ici appelé `repo`. Plus tard, nous ajouterons plus de composants ici.
* `pagination` : un `boolean` qui indique à ReactiveList de diviser les résultats en pages, chaque page contenant le nombre de résultats spécifié dans la prop `size`.

Maintenant, nous pouvons `importer` et utiliser le composant `Results` dans `/src/App.js`. Il suffit de l'ajouter à l'intérieur de la `div` avec la classe `results-container`.

```js
...
import Results from './components/Results';
...
render() {
  return(
    ...
    <div className="results-container">
      <DataSearch ... />
      <Results />
    </div>
    ...
  )
}
```

Avec ce composant, une version basique de notre UI de recherche devrait commencer à se rassembler :

![Image](https://cdn-media-1.freecodecamp.org/images/1*txovjxQldUv-T2V5ALzP_Q.png)
_Ajout du composant Results_

#### 5. Ajout d'un composant Header

Créons un composant `Header` à `/src/components/Header.js` que nous utiliserons pour rendre plus de filtres de recherche.

Voici comment créer un composant `Header` simple :

```js
import React, { Component } from 'react';

import SearchFilters from './SearchFilters';

class Header extends Component {
	constructor(props) {
		super(props);
		this.state = {
			visible: false,
		};
	}

	toggleVisibility = () => {
		const visible = !this.state.visible;
		this.setState({
			visible,
		});
	}

	render() {
		return (
			<nav className={`navbar ${this.state.visible ? 'active' : ''}`}>
				<div className="title">GitXplore</div>
				<div className="btn toggle-btn" onClick={this.toggleVisibility}>Basculer les filtres</div>
				<SearchFilters {...this.props} visible={this.state.visible} />
			</nav>
		);
	}
}

export default Header;

```

J'ai déplacé le code de navigation dans `<nav>..</nav>` de `/src/App.js` ici. Le composant Header a une méthode qui bascule la visibilité dans l'état. Nous utilisons cela pour ajouter une classe qui le ferait prendre toute la taille de l'écran sur la mise en page mobile. J'ai également ajouté un bouton de bascule qui appelle la méthode `toggleVisibility`.

Il rend également un autre composant appelé `SearchFilters` et passe toutes les props du composant parent `App`. Créons ce composant pour voir les choses en action.

Créez un nouveau fichier `/src/components/SearchFilters.js` :

```js
import React from 'react';
const SearchFilters = () => (
    <div>
        Les filtres de recherche vont ici !
    </div>
);
export default SearchFilters;
```

Ensuite, je vais mettre à jour le composant `App` pour utiliser le composant `Header` que nous venons de créer.

#### 6. Mise à jour du composant App et gestion des sujets dans l'état

Nous allons ajouter une variable `state` dans le composant `App` appelée `currentTopics` qui serait un tableau des sujets actuellement sélectionnés dans l'application.

Nous utiliserons ensuite `currentTopics` et les passerons aux composants `Header` et `Results` :

```js
import React, { Component } from 'react';
import { ReactiveBase, DataSearch } from '@appbaseio/reactivesearch';

import Header from './components/Header';
import Results from './components/Results';

import theme from './theme';
import './App.css';

class App extends Component {
	constructor(props) {
		super(props);
		this.state = {
			currentTopics: [],
		};
	}

	setTopics = (currentTopics) => {
		this.setState({
			currentTopics: currentTopics || [],
		});
	}

	toggleTopic = (topic) => {
		const { currentTopics } = this.state;
		const nextState = currentTopics.includes(topic)
			? currentTopics.filter(item => item !== topic)
			: currentTopics.concat(topic);
		this.setState({
			currentTopics: nextState,
		});
	}

	render() {
		return (
			<section className="container">
				<ReactiveBase
					app="gitxplore-app"
					credentials="4oaS4Srzi:f6966181-1eb4-443c-8e0e-b7f38e7bc316"
					type="gitxplore-latest"
					theme={theme}
				>
					<div className="flex row-reverse app-container">
						<Header currentTopics={this.state.currentTopics} setTopics={this.setTopics} />
						<div className="results-container">
							<DataSearch
								componentId="repo"
								filterLabel="Recherche"
								dataField={['name', 'description', 'name.raw', 'fullname', 'owner', 'topics']}
								placeholder="Rechercher des dépôts"
								iconPosition="left"
								autosuggest={false}
								URLParams
								className="data-search-container results-container"
								innerClass={{
									input: 'search-input',
								}}
							/>
							<Results currentTopics={this.state.currentTopics} toggleTopic={this.toggleTopic} />
						</div>
					</div>
				</ReactiveBase>
			</section>
		);
	}
}

export default App;
```

La méthode `setTopics` définira les sujets qui lui sont passés, que nous passerons au composant `Header`. La méthode `toggleTopic` supprimera un sujet de l'état dans `currentTopics` s'il est déjà présent et ajoutera le sujet s'il n'est pas présent.

Nous passerons la méthode `toggleTopic` au composant `Results` :

![Image](https://cdn-media-1.freecodecamp.org/images/1*3Or7_Pwz3wpkUcDv-gryFQ.png)
_Cela commence à se rassembler, santé !_

#### 7. Ajout de plus de filtres

Ajoutons plus de filtres à l'UI dans `/src/components/SearchFilters.js`. J'utiliserai ici trois nouveaux composants de ReactiveSearch, `MultiDropdownList`, `SingleDropdownRange` et `RangeSlider`. Les composants sont utilisés de manière similaire à celle dont nous avons utilisé le composant `DataSearch` précédemment.

Voici le code :

```js
import React from 'react';
import PropTypes from 'prop-types';
import {
	MultiDropdownList,
	SingleDropdownRange,
	RangeSlider,
} from '@appbaseio/reactivesearch';

const SearchFilters = ({ currentTopics, setTopics, visible }) => (
	<div className={`flex column filters-container ${!visible ? 'hidden' : ''}`}>
		<div className="child m10">
			<MultiDropdownList
				componentId="language"
				dataField="language.raw"
				placeholder="Sélectionner des langues"
				title="Langage"
				filterLabel="Langage"
			/>
		</div>
		<div className="child m10">
			<MultiDropdownList
				componentId="topics"
				dataField="topics.raw"
				placeholder="Sélectionner des sujets"
				title="Sujets du dépôt"
				filterLabel="Sujets"
				size={1000}
				queryFormat="and"
				defaultSelected={currentTopics}
				onValueChange={setTopics}
			/>
		</div>
		<div className="child m10">
			<SingleDropdownRange
				componentId="pushed"
				dataField="pushed"
				placeholder="Dépôt dernière activité"
				title="Dernière activité"
				filterLabel="Dernière activité"
				data={[
					{ start: 'now-1M', end: 'now', label: '30 derniers jours' },
					{ start: 'now-6M', end: 'now', label: '6 derniers mois' },
					{ start: 'now-1y', end: 'now', label: 'Dernière année' },
				]}
			/>
		</div>
		<div className="child m10">
			<SingleDropdownRange
				componentId="created"
				dataField="created"
				placeholder="Dépôt créé"
				title="Créé"
				filterLabel="Créé"
				data={[
					{
						start: '2017-01-01T00:00:00Z',
						end: '2017-12-31T23:59:59Z',
						label: '2017',
					},
					{
						start: '2016-01-01T00:00:00Z',
						end: '2016-12-31T23:59:59Z',
						label: '2016',
					},
					{
						start: '2015-01-01T00:00:00Z',
						end: '2015-12-31T23:59:59Z',
						label: '2015',
					},
					{
						start: '2014-01-01T00:00:00Z',
						end: '2014-12-31T23:59:59Z',
						label: '2014',
					},
					{
						start: '2013-01-01T00:00:00Z',
						end: '2013-12-31T23:59:59Z',
						label: '2013',
					},
					{
						start: '2012-01-01T00:00:00Z',
						end: '2012-12-31T23:59:59Z',
						label: '2012',
					},
					{
						start: '2011-01-01T00:00:00Z',
						end: '2011-12-31T23:59:59Z',
						label: '2011',
					},
					{
						start: '2010-01-01T00:00:00Z',
						end: '2010-12-31T23:59:59Z',
						label: '2010',
					},
					{
						start: '2009-01-01T00:00:00Z',
						end: '2009-12-31T23:59:59Z',
						label: '2009',
					},
					{
						start: '2008-01-01T00:00:00Z',
						end: '2008-12-31T23:59:59Z',
						label: '2008',
					},
					{
						start: '2007-01-01T00:00:00Z',
						end: '2007-12-31T23:59:59Z',
						label: '2007',
					},
				]}
			/>
		</div>
		<div className="child m10">
			<RangeSlider
				componentId="stars"
				title="Étoiles du dépôt"
				dataField="stars"
				range={{ start: 0, end: 300000 }}
				showHistogram={false}
				rangeLabels={{
					start: '0 Étoiles',
					end: '300K Étoiles',
				}}
				innerClass={{
					label: 'range-label',
				}}
			/>
		</div>
		<div className="child m10">
			<RangeSlider
				componentId="forks"
				title="Forks du dépôt"
				dataField="forks"
				range={{ start: 0, end: 180500 }}
				showHistogram={false}
				rangeLabels={{
					start: '0 Forks',
					end: '180K Forks',
				}}
				innerClass={{
					label: 'range-label',
				}}
			/>
		</div>
	</div>
);

SearchFilters.propTypes = {
	currentTopics: PropTypes.arrayOf(PropTypes.string),
	setTopics: PropTypes.func,
	visible: PropTypes.bool,
};

export default SearchFilters;

```

Le composant `SearchFilters` que nous avons créé ci-dessus prend trois props du composant `Header`, `currentTopics`, `setTopics` et `visible`. La prop `visible` est simplement utilisée pour ajouter une `className` pour le style.

Le premier composant que nous avons utilisé ici est un `[MultiDropdownList](https://opensource.appbase.io/reactive-manual/list-components/multidropdownlist.html)` qui rend un composant de liste déroulante pour sélectionner plusieurs options. Le premier `MultiDropdownList` a un `dataField` de `language.raw`. Il se remplira avec toutes les langues disponibles dans le jeu de données des dépôts.

![Image](https://cdn-media-1.freecodecamp.org/images/1*BwqnE21ABLW5q-xeCocmFA.png)
_La liste déroulante des langues [MultiDropdownList](https://opensource.appbase.io/reactive-manual/list-components/multidropdownlist.html" rel="noopener" target="_blank" title=")_

Nous avons utilisé un autre `MultiDropdownList` pour rendre une liste de sujets :

```js
<MultiDropdownList
    componentId="topics"
    dataField="topics.raw"
    placeholder="Sélectionner des sujets"
    title="Sujets du dépôt"
    filterLabel="Sujets"
    size={1000}
    queryFormat="and"
    defaultSelected={currentTopics}
    onValueChange={setTopics}
/>
```

Voici comment les props fonctionnent ici :

* `componentId` : similaire aux précédents composants ReactiveSearch, il s'agit d'un identifiant unique que nous associerons plus tard dans le composant `Results` que nous avons créé pour obtenir les résultats de recherche.
* `dataField` : mappe le composant au champ `topics.raw` dans Elasticsearch.
* `placeholder` : définit la valeur du placeholder lorsque rien n'est sélectionné.
* `title` : ajoute un titre pour le composant dans l'UI.
* `filterLabel` : définit le libellé des composants dans les filtres supprimables (le `SelectedFilters` que nous avons utilisé dans le composant `Results`).
* `size` : indique au composant de rendre un maximum de `1000` éléments dans la liste.
* `queryFormat` : lorsqu'il est défini sur `'and'` comme nous l'avons utilisé ici, il donne des résultats qui correspondent à toutes les balises sélectionnées (exactement comme [l'intersection](https://www.google.co.in/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&cad=rja&uact=8&ved=0ahUKEwjq2aSbmLLYAhUBP48KHW7QDVMQFghHMAE&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FIntersection_(set_theory)&usg=AOvVaw3o-ni_Iic1U3sedPMsJMqV)).
* `defaultSelected` : définit les éléments sélectionnés dans le composant. Ici, nous passons `currentTopics` que nous avons stocké dans le `state` à `/src/App.js`.
* `onValueChange` : est une fonction qui sera appelée par le composant lorsque nous modifions sa valeur. Ici, nous appelons la fonction `setTopics` que nous avons reçue dans les props. Par conséquent, chaque fois que nous sélectionnons ou désélectionnons une valeur dans le composant, cela mettra à jour le `currentTopics` dans le `state` du composant principal `App`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GPqMulHiFqd35bXmay2Cww.png)
_Le composant MultiDropdownList des sujets_

Le prochain composant ReactiveSearch que nous avons utilisé ici est un `[SingleDropdownRange](https://opensource.appbase.io/reactive-manual/range-components/singledropdownrange.html)`. Il utilise une nouvelle prop appelée `[data](https://opensource.appbase.io/reactive-manual/range-components/singledropdownrange.html#props)`.

Voici comment cela fonctionne :

```js
<SingleDropdownRange
    ...
    data={[
        { start: 'now-1M', end: 'now', label: '30 derniers jours' },
        { start: 'now-6M', end: 'now', label: '6 derniers mois' },
        { start: 'now-1y', end: 'now', label: 'Dernière année' },
    ]}
/>
```

La prop `data` accepte un tableau d'objets avec des valeurs `start` et `end` et affiche le `label` spécifié dans la liste déroulante. Elle est mappée au champ `pushed` dans le jeu de données qui est un [type de date dans Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/date.html). Une manière intéressante de spécifier une plage de dates dans Elasticsearch est d'utiliser le mot-clé `now`. `now` fait référence à l'heure actuelle, `now-1M` fait référence à un mois avant, `now-6M` à six mois avant et `now-1y` à un an avant `now`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*g6uRRdk37VyzQEqDIX_CCg.png)
_Le composant [SingleDropdownRange](https://opensource.appbase.io/reactive-manual/range-components/singledropdownrange.html" rel="noopener" target="_blank" title=") pour le champ pushed_

J'ai utilisé un autre composant `SingleDropdownRange` pour le champ `created` dans le jeu de données.

Ici, j'ai spécifié des plages d'années en datetime pour différentes années :

```js
<SingleDropdownRange
    ...
    data={[
        {
            start: '2017-01-01T00:00:00Z',
            end: '2017-12-31T23:59:59Z',
            label: '2017',
        },
        {
            start: '2016-01-01T00:00:00Z',
            end: '2016-12-31T23:59:59Z',
            label: '2016',
        },
       ...
    ]}
/>
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*V1J8UQXBUCWJd4-EuC5I7w.png)
_Composant SingleDropdownRange pour le champ créé_

Le troisième composant que j'ai utilisé est un `[RangeSlider](https://opensource.appbase.io/reactive-manual/range-components/rangeslider.html)` qui rend une interface utilisateur de curseur. J'ai utilisé deux composants `RangeSlider`, un pour le champ `stars` et l'autre pour `forks`.

Deux props principales que ce composant introduit sont `range` et `rangeLabels` :

```js
<RangeSlider
    ...
    showHistogram={false}
    range={{ start: 0, end: 300000 }}
    rangeLabels={{
        start: '0 Étoiles',
        end: '300K Étoiles',
    }}
/>
```

* `range` : la prop spécifie une plage pour les données avec une valeur `start` et `end`.
* `rangeLabels` : la prop prend les libellés à afficher sous le curseur.
* `showHistogram` : est une prop `boolean` qui affiche un histogramme avec la distribution des données. Ici, je l'ai définie sur `false` car elle n'est pas nécessaire.

![Image](https://cdn-media-1.freecodecamp.org/images/1*s98sSECpz1cX-9Q_jbUyLQ.png)
_Composants [RangeSlider](https://opensource.appbase.io/reactive-manual/range-components/rangeslider.html" rel="noopener" target="_blank" title=") pour les champs stars et forks_

Maintenant, nous devons simplement connecter ces filtres au composant `Results`. Nous devons simplement mettre à jour une ligne dans le `ReactiveList` rendu par le composant `Results` pour inclure les `componentId` de ces composants.

Mettez à jour la prop `react` dans le `ReactiveList` que nous avons rendu dans le composant `Results` :

```js
const Results = () => (
  <div className="result-list">
    <SelectedFilters className="m1" />
    <ReactiveList
      ... // mise à jour de la prop react ici
      react={{
        and: ['language', 'topics', 'pushed', 'created', 'stars', 'forks', 'repo'],
      }}
    />
  </div>
);
```

Cela devrait faire en sorte que vos résultats se mettent à jour pour tous les filtres ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*fAMt45ayVCNTLy77EI7Szg.png)
_Après avoir connecté les filtres dans le composant ReactiveList_

#### 8. Mise à jour de la vue des résultats

Jusqu'à présent, nous n'avons vu qu'une version basique des résultats. En tant que dernière pièce de cette application, ajoutons un peu de style aux résultats F489F3FB

Nous allons utiliser un autre composant à l'intérieur de nos composants `Results` pour rendre différents sujets.

![Image](https://cdn-media-1.freecodecamp.org/images/1*AyocrMQaO0TQWoYcbhoHlA.png)
_Composant Sujets pour rendre ces petits gars_

Voici comment vous pouvez créer le vôtre à `/src/components/Topic`. N'hésitez pas à ajouter votre propre touche ?

```js

import React, { Component } from 'react';
import PropTypes from 'prop-types';

class Topic extends Component {
	handleClick = () => {
		this.props.toggleTopic(this.props.children);
	}
	render() {
		return (
			<div className={`topic ${this.props.active ? 'active' : ''}`} onClick={this.handleClick}>
				#{this.props.children}
			</div>
		);
	}
}

Topic.propTypes = {
	children: PropTypes.string,
	active: PropTypes.bool,
	toggleTopic: PropTypes.func,
};

export default Topic;
```

Ce composant rend ses `children` et ajoute un gestionnaire de clic pour basculer les sujets qui met à jour le `currentTopics` à l'intérieur de l'état du composant principal `App`.

Ensuite, nous devons simplement mettre à jour notre composant `Results` à `/src/components/Results.js` :

```js
import React from 'react';
import { SelectedFilters, ReactiveList } from '@appbaseio/reactivesearch';
import PropTypes from 'prop-types';

import Topic from './Topic';

const onResultStats = (results, time) => (
	<div className="flex justify-end">
		{results} résultats trouvés en {time}ms
	</div>
);

const onData = (data, currentTopics, toggleTopic) => (
	<div className="result-item" key={data.fullname}>
		<div className="flex justify-center align-center result-card-header">
			<img className="avatar" src={data.avatar} alt="Avatar de l'utilisateur" />
			<a className="link" href={data.url} target="_blank" rel="noopener noreferrer">
				<div className="flex wrap">
					<div>{data.owner}/</div>
					<div>{data.name}</div>
				</div>
			</a>
		</div>
		<div className="m10-0">{data.description}</div>
		<div className="flex wrap justify-center">
			{
				data.topics.slice(0, 7)
					.map(item => (
						<Topic
							key={item}
							active={currentTopics.includes(item)}
							toggleTopic={toggleTopic}
						>
							{item}
						</Topic>
					))
			}
		</div>
		<div className="flex">
			<div><div className="btn card-btn"><i className="card-icon fas fa-star" />{data.stars}</div></div>
			<div><div className="btn card-btn"><i className="card-icon fas fa-code-branch" />{data.forks}</div></div>
			<div><div className="btn card-btn"><i className="card-icon fas fa-eye" />{data.watchers}</div></div>
		</div>
	</div>
);

const Results = ({ toggleTopic, currentTopics }) => (
	<div className="result-list">
		<SelectedFilters className="m1" />
		<ReactiveList
			componentId="results"
			dataField="name"
			onData={data => onData(data, currentTopics, toggleTopic)}
			onResultStats={onResultStats}
			react={{
				and: ['language', 'topics', 'pushed', 'created', 'stars', 'forks', 'repo'],
			}}
			pagination
			innerClass={{
				list: 'result-list-container',
				pagination: 'result-list-pagination',
				resultsInfo: 'result-list-info',
				poweredBy: 'powered-by',
			}}
			size={6}
			sortOptions={[
				{
					label: 'Meilleure correspondance',
					dataField: '_score',
					sortBy: 'desc',
				},
				{
					label: 'Plus d'étoiles',
					dataField: 'stars',
					sortBy: 'desc',
				},
				{
					label: 'Moins d'étoiles',
					dataField: 'stars',
					sortBy: 'asc',
				},
				{
					label: 'Plus de forks',
					dataField: 'forks',
					sortBy: 'desc',
				},
				{
					label: 'Moins de forks',
					dataField: 'forks',
					sortBy: 'asc',
				},
				{
					label: 'A à Z',
					dataField: 'owner.raw',
					sortBy: 'asc',
				},
				{
					label: 'Z à A',
					dataField: 'owner.raw',
					sortBy: 'desc',
				},
				{
					label: 'Récemment mis à jour',
					dataField: 'pushed',
					sortBy: 'desc',
				},
				{
					label: 'Moins récemment mis à jour',
					dataField: 'pushed',
					sortBy: 'asc',
				},
			]}
		/>
	</div>
);

Results.propTypes = {
	toggleTopic: PropTypes.func,
	currentTopics: PropTypes.arrayOf(PropTypes.string),
};

export default Results;
```

J'ai mis à jour la fonction `onData` pour rendre des résultats plus détaillés. Vous remarquerez également une nouvelle prop `sortOptions` dans le `ReactiveList`. Cette prop accepte un tableau d'objets qui rend un menu déroulant pour sélectionner comment vous souhaitez trier les résultats. Chaque objet contient un `label` à afficher comme élément de liste, un `dataField` pour trier les résultats et une clé `sortBy` qui peut être soit `asc` (ascendant) soit `desc` (descendant).

C'est tout, votre propre explorateur de dépôt GitHub devrait être en ligne !

![Image](https://cdn-media-1.freecodecamp.org/images/1*RQ6EPM9NrDsvX_ZdkpB_cw.png)
_GitXplore [aperçu de l'application finale](https://appbaseio-apps.github.io/gitxplore-app/" rel="noopener" target="_blank" title=")_

### Liens utiles

1. Application GitXplore [démo](https://appbaseio-apps.github.io/gitxplore-app/), [CodeSandbox](https://codesandbox.io/s/github/appbaseio-apps/gitxplore-app/tree/master/) et [code source](https://github.com/appbaseio-apps/gitxplore-app)
2. [Dépôt GitHub ReactiveSearch](https://github.com/appbaseio/reactivesearch)
3. Documentation ReactiveSearch [docs](https://opensource.appbase.io/reactive-manual/)

J'espère que vous avez apprécié cette histoire. Si vous avez des pensées ou des suggestions, faites-le moi savoir et partagez votre version de l'application dans les commentaires !

---

Vous pouvez me suivre sur [twitter](https://twitter.com/divyanshu013) pour les dernières mises à jour. J'ai également commencé à publier des articles plus récents sur mon blog personnel [blog](https://divyanshu013.dev/).