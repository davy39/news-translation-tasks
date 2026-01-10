---
title: 'Comment tester les composants React : le guide complet'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-11T21:18:12.000Z'
originalURL: https://freecodecamp.org/news/testing-react-hooks
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/photo-1562679817-2aac4f5581ec.jpg
tags:
- name: Jest
  slug: jest
- name: React
  slug: react
- name: react testing library
  slug: react-testing-library
- name: Software Testing
  slug: software-testing
seo_title: 'Comment tester les composants React : le guide complet'
seo_desc: 'By Mohammad Iqbal

  When I first started learning to test my apps back in the day, I would get very
  frustrated with the different types, styles and technologies used for testing, along
  with the disbanded array of blog posts, tutorials and articles. I f...'
---

Par Mohammad Iqbal

Lorsque j'ai commencé à apprendre à tester mes applications, je me sentais très frustré par les différents types, styles et technologies utilisés pour les tests, ainsi que par la multitude dispersée d'articles de blog, de tutoriels et d'articles. J'ai trouvé que cela était également vrai pour les tests React.

J'ai donc décidé d'écrire un guide complet sur les tests React en un seul article.

Guide complet, hein, allez-vous couvrir tous les scénarios de test possibles ? Bien sûr que non. Cependant, ce sera un guide fondamental complet sur les tests et suffira pour la plupart des autres cas particuliers.

J'ai également compilé une collection extensive d'articles de blog, d'articles et de tutoriels dans la section lectures complémentaires à la fin, qui devrait vous donner suffisamment de connaissances pour faire partie des 10 % de développeurs en termes de tests.

Vous pouvez trouver le projet complet ici :

[https://github.com/iqbal125/react-hooks-testing-complete](https://github.com/iqbal125/react-hooks-testing-complete)


## Table des matières

	 **Théorie**

*  Qu'est-ce que les tests ?   
*  Pourquoi tester ? 
*  Que tester ? 
*  Que ne pas tester ? 
*  Comment je teste
*  Shallow vs Mount
*  unit vs integration vs e to e

	**Informations préliminaires**

* quelques détails

	**Enzyme**

* Configuration d'Enzyme
* react-test-renderer
* tests de snapshot
* tester les détails d'implémentation

	**React Testing Library**

* useState et props 
* useReducer()
* useContext()
* Formulaires de composants contrôlés
* useEffect() et requêtes API Axios

	**Cypress** 

* Un test complet de bout en bout

	**Intégration Continue**

* Travis.yml
* Couverture de code avec coveralls 

## Théorie

### Qu'est-ce que les tests ?

Commençons par le début et discutons de ce que sont les tests. Les tests sont un processus en 3 étapes qui ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-12.png)

Arranger, votre application est dans un certain état initial. Agir, puis quelque chose se produit (événement de clic, entrée, etc.). Ensuite, vous affirmez, ou faites une hypothèse, du nouvel état de votre application. Les tests réussiront si votre hypothèse est correcte et échoueront si elle est fausse.

Contrairement à vos composants React, vos tests ne sont pas exécutés dans le navigateur. Jest est le test runner et le framework de test utilisé par React. Jest est l'environnement où tous vos tests sont réellement exécutés. C'est pourquoi vous n'avez pas besoin d'importer `expect` et `describe` dans ce fichier. Ces fonctions sont déjà disponibles globalement dans l'environnement Jest.

La syntaxe de vos tests ressemblera à ceci :

```javascript
describe('Test de la somme', () => {
    function sum(a, b) {
       return a + b;
    }

    it('devrait être égal à 4',()=>{
       expect(sum(2,2)).toBe(4);
      })

    test('devrait aussi être égal à 4', () => {
        expect(sum(2,2)).toBe(4);
      }) 
});
```

`describe` enveloppe nos blocs `it` ou `test`, et est un moyen de regrouper nos tests. `it` et `test` sont des mots-clés et peuvent être utilisés indifféremment. La chaîne de caractères sera quelque chose qui devrait se produire avec vos tests et sera imprimée dans la console. `toBe()` est un matcher qui fonctionne avec expect pour vous permettre de faire des assertions. Il existe de nombreux autres matchers et variables globales offerts par Jest, voir les liens ci-dessous pour une liste complète.

[https://jestjs.io/docs/en/using-matchers](https://jestjs.io/docs/en/using-matchers)

[https://jestjs.io/docs/en/api](https://jestjs.io/docs/en/api)

###   
  
Pourquoi tester ?

Les tests sont effectués pour s'assurer que votre application fonctionnera comme prévu pour vos utilisateurs finaux. Avoir des tests rendra votre application plus robuste et moins sujette aux erreurs. C'est un moyen de vérifier que le code fait ce que les développeurs ont prévu.

Inconvénients potentiels :

* Écrire des tests est chronophage et difficile. 
* Dans certains scénarios, l'exécution de tests dans CI peut coûter de l'argent. 
* Si mal fait, cela peut donner des faux positifs. Vos tests passent, mais votre application ne fonctionne pas comme prévu. 
* Ou des faux négatifs. Vos tests échouent mais votre application fonctionne comme prévu.



### Que tester ?

Pour développer le point précédent, vos tests doivent tester la fonctionnalité de l'application, qui imite la manière dont elle sera utilisée par vos utilisateurs finaux. Cela vous donnera confiance que votre application fonctionnera comme prévu dans votre environnement de production. Nous entrerons bien sûr dans beaucoup plus de détails tout au long de cet article, mais c'est l'essentiel.

### Que ne pas tester ?

J'aime utiliser la philosophie de Kent C Dodds ici, selon laquelle vous ne devriez pas tester les détails d'implémentation.

Les détails d'implémentation signifient tester des choses qui ne sont pas des fonctionnalités pour l'utilisateur final. Nous verrons un exemple de cela dans la section Enzyme ci-dessous.

Il semble que vous testez la fonctionnalité là, mais en réalité, ce n'est pas le cas. Vous testez le nom de la fonction. Parce que vous pouvez changer le nom de la fonction et vos tests échoueront, mais votre application fonctionnera toujours, vous donnant un faux négatif.

Devoir constamment s'inquiéter des noms de fonctions et de variables est un casse-tête, et devoir réécrire les tests chaque fois que vous les changez est fastidieux. Je vais vous montrer une meilleure approche.

**Variables constantes :** ce sont des variables immuables, pas besoin de les tester.

**Bibliothèques tierces :** Ce n'est pas votre travail de tester ces bibliothèques. C'est aux créateurs de ces bibliothèques de les tester. Si vous n'êtes pas sûr qu'une bibliothèque soit testée, vous ne devriez pas l'utiliser. Ou vous pouvez lire le code source pour voir si l'auteur a inclus des tests. Vous pouvez télécharger le code source et exécuter ces tests vous-même. Vous pouvez également demander à l'auteur si sa bibliothèque est prête pour la production ou non.


### Ma philosophie personnelle sur les tests

Une grande partie de ma philosophie de test est basée sur les enseignements de Kent C Dodds, donc vous verrez beaucoup de ses sentiments répétés ici, mais j'ai aussi quelques-unes de mes propres pensées.

Beaucoup de tests d'intégration. Pas de tests de snapshot. Peu de tests unitaires. Peu de tests de bout en bout.

Les tests unitaires sont un cran au-dessus des tests de snapshot, mais ce n'est pas idéal. Ils sont cependant beaucoup plus faciles à comprendre et à maintenir que les tests de snapshot.

Écrivez principalement des tests d'intégration. Les tests unitaires sont bons, mais ils ne ressemblent pas vraiment à la manière dont votre utilisateur final interagit avec votre application. Il est très facile de tester les détails d'implémentation avec les tests unitaires, surtout avec le rendu shallow.

Les tests d'intégration doivent mock le moins possible.

Ne testez pas les détails d'implémentation tels que les noms de fonctions et de variables.

Par exemple, si nous testons un bouton et changeons le nom de la fonction dans la méthode onClick de increment() à handleClick(), nos tests échoueraient, mais notre composant fonctionnerait toujours. C'est une mauvaise pratique car nous testons essentiellement le nom de la fonction, qui est un détail d'implémentation, dont l'utilisateur final ne se soucie pas.



### Shallow vs mount

Mount exécute réellement le code HTML, CSS et JS comme le ferait un navigateur, mais le fait de manière simulée. Il est "headless", par exemple, ce qui signifie qu'il ne rend ou ne peint rien dans une UI, mais agit comme un navigateur web simulé et exécute le code en arrière-plan.

Ne pas passer de temps à peindre quoi que ce soit dans l'UI rend vos tests beaucoup plus rapides. Cependant, les tests mount sont encore beaucoup plus lents que les tests shallow.

C'est pourquoi vous démontez ou nettoyez le composant après chaque test, car c'est presque une application en direct et un test affectera un autre test.

Mount/render est généralement utilisé pour les tests d'intégration et shallow est utilisé pour les tests unitaires.

Le rendu shallow ne rend que le seul composant que nous testons. Il ne rend pas les composants enfants. Cela nous permet de tester notre composant en isolation.

Par exemple, considérons ce composant enfant et parent.

```javascript
import React from 'react';

const App = () => {
  return (
    <div> 
      <ChildComponent /> 
    </div> 
  )
}

const ChildComponent = () => {
  return (
    <div>
     <p> Child components</p>
    </div>
  )
}
```

Si nous utilisions le rendu shallow de `App.js`, nous obtiendrions quelque chose comme ceci, remarquez qu'aucun des nœuds DOM pour le composant enfant n'est présent, d'où le terme rendu shallow.

```
<App>
  <div> 
    <ChildComponent /> 
  </div>
</App> 
```

Maintenant, nous pouvons comparer cela au montage du composant :

```
<App>
  <div> 
    <ChildComponent> 
      <div>
       <p> Child components</p>
      </div>
    </ChildComponent>
   </div>
</App> 
```

Ce que nous avons ci-dessus est beaucoup plus proche de ce à quoi notre application ressemblera dans le navigateur, d'où la supériorité de mount/render.

### unit vs integration vs end to end

**unit testing** : tester une partie isolée de votre application, généralement fait en combinaison avec le rendu shallow. exemple : un composant se rend avec les props par défaut.

**integration testing** : tester si différentes parties fonctionnent ou s'intègrent les unes avec les autres. Habituellement fait avec le montage ou le rendu d'un composant. exemple : tester si un composant enfant peut mettre à jour l'état du contexte dans un parent.

**e to e testing** : Signifie end to end. Habituellement un test en plusieurs étapes combinant plusieurs tests unitaires et d'intégration en un seul grand test. Habituellement, très peu de choses sont mockées ou stubbées. Les tests sont effectués dans un navigateur simulé, il peut y avoir ou non une UI pendant l'exécution du test. exemple : tester un flux d'authentification entier.



## Informations préliminaires

**react-testing-library** : Je préfère personnellement utiliser react-testing-library, mais la méthode courante est d'utiliser Enzyme. Je vais vous montrer un exemple d'Enzyme car il est important d'être conscient d'Enzyme à un niveau basique et le reste des exemples avec react-testing-library.

**Plan des exemples** : Nos exemples suivront un schéma. Je vais d'abord vous montrer le composant React, puis les tests pour celui-ci, avec des explications détaillées de chacun. Vous pouvez également suivre avec le dépôt lié au début.

**Configuration** : Je vais également supposer que vous utilisez create-react-app avec la configuration de test par défaut avec Jest, donc je vais sauter les configurations manuelles.

**Sinon, mocha, chai** : Une grande partie de la fonctionnalité offerte par sinon est disponible par défaut avec Jest, donc vous n'avez pas besoin de sinon. Mocha et chai sont un remplacement pour Jest. Jest vient préconfiguré pour fonctionner avec votre application, donc il n'a pas de sens d'utiliser Mocha et chai.

**Schéma de nommage des composants** : Mon schéma de nommage pour les composants est `<TestSomething />`, mais cela ne signifie pas qu'ils sont de faux composants d'une quelconque manière. Ce sont des composants React réguliers, c'est juste le schéma de nommage.

**npm test et mode watch de Jest** : `yarn test` a fonctionné pour moi. `npm test` n'a pas fonctionné correctement avec le mode watch de Jest.

**tester un seul fichier** : `yarn test` nom du fichier

**React Hooks vs Classes** : J'utilise des composants React Hooks pour la plupart des exemples, mais grâce à la puissance de react-testing-library, tous ces tests fonctionneront directement avec les composants de classe également.

Avec les informations préliminaires hors du chemin, nous pouvons passer en revue du code.



## Enzyme

### Configuration d'Enzyme

Nos bibliothèques tierces

`npm install enzyme enzyme-to-json  enzyme-adapter-react-16`

Commençons d'abord par nos imports

```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import Basic from '../basic_test';

import Enzyme, { shallow, render, mount } from 'enzyme';
import toJson from 'enzyme-to-json';
import Adapter from 'enzyme-adapter-react-16';

Enzyme.configure({ adapter: new Adapter() })
```

Nous commencerons par nos imports de base. Nos trois premiers imports sont pour React et notre composant.

Après cela, nous importons Enzyme. Ensuite, nous importons la fonction toJson de la bibliothèque 'enzyme-to-json'. Nous en aurons besoin pour convertir notre composant rendu en shallow en JSON qui peut être sauvegardé dans le fichier snapshot.

Enfin, nous importons notre Adapter pour faire fonctionner enzyme avec React 16 et l'initialisons comme montré ci-dessus.

  
react-test-renderer

React vient en fait avec son propre test renderer que vous pouvez utiliser au lieu d'enzyme et la syntaxe ressemblera à ceci.

```javascript
// import TestRenderer from 'react-test-renderer';
// import ShallowRenderer from 'react-test-renderer/shallow';


// Basic Test with React-test-renderer
// it('renders correctly react-test-renderer', () => {
//   const renderer = new ShallowRenderer();
//   renderer.render(<Basic />);
//   const result = renderer.getRenderOutput();
//
//   expect(result).toMatchSnapshot();
// });
```

Mais même les docs de react-test-render suggèrent d'utiliser enzyme à la place car il a une syntaxe légèrement plus agréable et fait la même chose. Juste quelque chose à savoir.


### Tests de snapshot

Maintenant, notre premier test qui est un test de snapshot

```javascript
it('renders correctly enzyme', () => {
  const wrapper = shallow(<Basic />)

  expect(toJson(wrapper)).toMatchSnapshot();
});
```

Si vous n'avez pas exécuté cette commande auparavant, un dossier __snapshots__ et un fichier test.js.snap seront créés automatiquement pour vous. À chaque test ultérieur, le nouveau snapshot sera comparé au fichier snapshot existant. Le test réussira si le snapshot n'a pas changé et échouera s'il a changé.

Ainsi, essentiellement, les tests de snapshot vous permettent de voir comment votre composant a changé depuis le dernier test, ligne par ligne. Les lignes de code qui ont changé sont connues sous le nom de diff.

Voici notre composant de base que nous testons avec snapshot :

```
import React from 'react';


const Basic = () => {
  return (
    <div >
      <h1> Basic Test</h1>
         <p> This is a basic Test Component</p>
    </div>
  );
}

export default Basic;
```

  
L'exécution du test ci-dessus générera un fichier qui ressemblera à ceci. Il s'agit essentiellement de notre arbre de nœuds DOM React.

```
// Jest Snapshot v1, https://goo.gl/fbAQLP

exports[`renders correctly enzyme 1`] = `
<div>
  <h1>
     Basic Test
  </h1>
  <p>
     This is a basic Test Component
  </p>
</div>
`;
```

Et produira une structure de dossiers qui ressemblera à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-6.png)

  
Votre sortie de terminal ressemblera à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-7.png)

Cependant, que se passe-t-il si nous changions notre composant de base en ceci

```
import React from 'react';


const Basic = () => {
  return (
    <div >
      <h1> Basic Test</h1>

    </div>
  );
}

export default Basic;
```

Nos snapshots échoueront maintenant


![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-8.png)

Et nous donnera également le diff

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-9.png)

Tout comme dans git, le " - " avant chaque ligne signifie qu'elle a été supprimée.

Nous devons simplement appuyer sur "w" pour activer le mode watch, puis appuyer sur "u" pour mettre à jour le snapshot.

Notre fichier de snapshot sera automatiquement mis à jour avec le nouveau snapshot et passera nos tests.

```
// Jest Snapshot v1, https://goo.gl/fbAQLP

exports[`renders correctly enzyme 1`] = `
<div>
  <h1>
     Basic Test
  </h1>
</div>
`;
```

  
C'est tout pour les tests de snapshot, mais si vous avez lu ma section sur mes pensées personnelles, vous savez que je ne fais pas de tests de snapshot. Je l'ai inclus ici parce que, comme Enzyme, c'est très courant et quelque chose dont vous devriez être conscient, mais ci-dessous, j'essaierai d'expliquer pourquoi je ne l'utilise pas.

Revenons sur ce qu'est le test de snapshot. Il vous permet essentiellement de voir comment votre composant a changé depuis le dernier test. Quels sont les avantages de cela.

* C'est très rapide et facile à mettre en œuvre et nécessite parfois seulement quelques lignes de code.
* Vous pouvez voir si notre composant est rendu correctement. Vous pouvez voir les nœuds DOM clairement avec la fonction .debug().



**Inconvénients, Arguments contre les tests de snapshot :**

* La seule chose qu'un test de snapshot fait est de vous dire si la syntaxe de votre code a changé depuis le dernier test.
* Donc, que teste-t-il vraiment ? Certains diraient pas grand-chose.
* De plus, le rendu de base de l'application correctement est le travail de React, donc vous allez un peu dans le territoire de test d'une bibliothèque tierce.
* De plus, comparer les diffs peut être fait avec le contrôle de version git. Ce ne devrait pas être le travail des tests de snapshot.
* Un test échoué ne signifie pas que votre application ne fonctionne pas comme prévu, seulement que votre code a changé depuis la dernière fois que vous avez exécuté le test. Cela peut conduire à beaucoup de faux négatifs et à un manque de confiance dans le test. Cela peut également conduire les gens à simplement mettre à jour le test sans le regarder de trop près.
* Les tests de snapshot vous disent également si votre JSX est syntaxiquement correct, mais encore une fois, cela peut être facilement fait dans l'environnement de développement. Exécuter un test de snapshot juste pour vérifier les erreurs de syntaxe n'a pas de sens.
* Il peut devenir difficile de comprendre ce qui se passe dans un test de snapshot, puisque la plupart des gens utilisent les tests de snapshot avec le rendu shallow, qui ne rend pas les composants enfants, donc il ne donne aucun aperçu au développeur.


Voir la section lectures complémentaires pour plus d'informations.



### Tester les détails d'implémentation avec Enzyme

Ici, je vais donner un exemple sur pourquoi ne pas tester les détails d'implémentation. Supposons que nous avons un simple composant de compteur comme ceci :

```javascript
import React, { Component } from 'react';


class Counter extends Component {
  constructor(props) {
    super(props)

    this.state = {
      count: 0
    }
  }

  increment = () => {
    this.setState({count: this.state.count + 1})
  }

  //Ce code incorrect fera toujours passer les tests
  // <button onClick={this.incremen}>
  //   Clicked: {this.state.count}
  // </button>

  render() {
    return (
      <div>
        <button className="counter-button" onClick={this.incremen}>
          Clicked: {this.state.count}
        </button>
      </div>
  )}
}

export default Counter;
```

Vous remarquerez que j'ai un commentaire suggérant qu'une application non fonctionnelle fera toujours passer les tests, par exemple en mal orthographiant le nom de la fonction dans l'événement onClick.

Et voyons les tests qui rendront cela clair.

```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import Counter from '../counter';

import Enzyme, { shallow, render, mount } from 'enzyme';
import toJson from 'enzyme-to-json';
import Adapter from 'enzyme-adapter-react-16';

Enzyme.configure({ adapter: new Adapter() })

// incorrect function assignment in the onClick method
// will still pass the tests.

test('the increment method increments count', () => {
  const wrapper = mount(<Counter />)

  expect(wrapper.instance().state.count).toBe(0)

  // wrapper.find('button.counter-button').simulate('click')
  // wrapper.setState({count: 1})
  wrapper.instance().increment()
  expect(wrapper.instance().state.count).toBe(1)
})

```

L'exécution du code ci-dessus passera les tests. Il en sera de même avec `wrapper.setState()`. Nous avons donc des tests qui passent avec une application non fonctionnelle. Je ne sais pas pour vous, mais cela ne me donne pas confiance que notre application fonctionnera comme prévu pour nos utilisateurs finaux.

Simuler un clic sur le bouton ne passera pas les tests, mais cela pourrait nous donner le problème inverse, un faux négatif. Supposons que nous voulons changer le style du bouton en déclarant une nouvelle classe CSS pour celui-ci, une situation très courante. Nos tests échoueront maintenant parce que nous ne pouvons plus trouver notre bouton, mais notre application fonctionnera toujours, nous donnant un faux négatif. Cela est également vrai chaque fois que nous changeons les noms de nos fonctions ou variables d'état.

Chaque fois que nous voulons changer nos noms de fonctions et de classes CSS, nous devons réécrire nos tests, un processus très inefficace et fastidieux.

Alors, que pouvons-nous faire à la place ?

## React-testing-library

### useState

D'après la documentation de react-testing-library, nous voyons que le principe directeur principal est

> Plus vos tests ressemblent à la manière dont votre logiciel est utilisé, plus ils peuvent vous donner confiance.

Nous garderons ce principe directeur à l'esprit alors que nous explorerons davantage avec nos tests.

Commençons par un composant React Hooks de base et testons l'état et les props.

```javascript
import React, { useState } from 'react';


const TestHook = (props) => {
  const [state, setState] = useState("Initial State")

  const changeState = () => {
    setState("Initial State Changed")
  }

  const changeNameToSteve = () => {
    props.changeName()
  }

  return (
  <div>
    <button onClick={changeState}>
      State Change Button
    </button>
    <p>{state}</p>
    <button onClick={changeNameToSteve}>
       Change Name
    </button>
    <p>{props.name}</p>
  </div>
  )
}


export default TestHook;
```

Nos props proviennent du composant parent racine

```javascript
  const App = () => {
      const [state, setState] = useState("Some Text")
      const [name, setName] = useState("Moe")
  ...
      const changeName = () => {
        setName("Steve")
      }

      return (
        <div className="App">
         <Basic />
        <h1> Counter </h1>
         <Counter />
        <h1> Basic Hook useState </h1>
         <TestHook name={name} changeName={changeName}/>
    ...     
```

Alors, en gardant notre principe directeur à l'esprit, à quoi ressembleront nos tests ?

La manière dont notre utilisateur final utilisera cette application sera de : voir du texte sur l'UI, voir le texte dans le bouton, puis cliquer dessus, enfin voir du nouveau texte sur l'UI.

C'est ainsi que nous écrirons nos tests en utilisant la bibliothèque de tests React.

Utilisez cette commande pour installer la bibliothèque de tests React.

`npm install @testing-library/react`

**pas**

`npm install react-testing-library`

Maintenant pour nos tests

```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import TestHook from '../test_hook.js';
import {render, fireEvent, cleanup} from '@testing-library/react';
import App from '../../../App'

afterEach(cleanup)

it('Text in state is changed when button clicked', () => {
    const { getByText } = render(<TestHook />);

    expect(getByText(/Initial/i).textContent).toBe("Initial State")

    fireEvent.click(getByText("State Change Button"))

    expect(getByText(/Initial/i).textContent).toBe("Initial State Changed")
 })


it('button click changes props', () => {
  const { getByText } = render(<App>
                                <TestHook />
                               </App>)

  expect(getByText(/Moe/i).textContent).toBe("Moe")

  fireEvent.click(getByText("Change Name"))

  expect(getByText(/Steve/i).textContent).toBe("Steve")
})
```

Nous commençons d'abord par nos imports habituels.

Ensuite, nous avons la fonction `afterEach(cleanup)`. Puisque nous n'utilisons pas le rendu shallow, nous devons démonter ou nettoyer après chaque test. Et c'est exactement ce que fait cette fonction.

`getByText` est la méthode de requête que nous obtenons en utilisant la destructuration d'objet sur la valeur de la fonction render. Il existe plusieurs autres méthodes de requête, mais c'est celle que vous voudrez utiliser la plupart du temps.

Pour tester notre état, remarquez que nous n'utilisons aucun nom de fonction ou les noms de nos variables d'état. Nous respectons notre principe directeur et ne testons pas les détails d'implémentation. Puisqu'un utilisateur verra le texte sur l'UI, c'est ainsi que nous interrogerons les nœuds DOM. Nous interrogerons également le bouton de cette manière et cliquerons dessus. Enfin, nous interrogerons l'état final en fonction du texte également.

`(/Initial/i)` est une expression régulière qui retourne le premier nœud qui contient au moins le texte "Initial".

Nous pouvons faire exactement la même chose avec les props également. Puisque les **props** vont être changées dans `App.js`, nous devrons les rendre avec notre composant. Comme dans l'exemple précédent, nous n'utilisons pas de noms de fonctions et de variables. Nous testons de la même manière qu'un utilisateur utiliserait notre application, c'est-à-dire par le texte qu'il verra.

Espérons que cela vous donne une bonne idée de la manière de tester avec la `react-testing-library` et le principe directeur, vous voulez généralement utiliser `getByText` la plupart du temps. Il y a quelques exceptions que nous verrons au fur et à mesure que nous continuerons.



### useReducer

Maintenant, nous pouvons tester un composant avec le hook useReducer. Nous aurons bien sûr besoin d'actions et de reducers pour travailler avec notre composant, alors configurons-les comme ceci :

Notre reducer

```javascript
import * as ACTIONS from './actions'

export const initialState = {
    stateprop1: false,
}

export const Reducer1 = (state = initialState, action) => {
  switch(action.type) {
    case "SUCCESS":
      return {
        ...state,
        stateprop1: true,
      }
    case "FAILURE":
      return {
        ...state,
        stateprop1: false,
      }
    default:
      return state
  }
}
```

Et les actions :

```



export const SUCCESS = {
  type: 'SUCCESS'
}

export const FAILURE = {
  type: 'FAILURE'
}


```

Nous garderons les choses simples et utiliserons des actions au lieu de créateurs d'actions.

Et enfin le composant qui utilisera ces actions et reducers :

```javascript
import React, { useReducer } from 'react';
import * as ACTIONS from '../store/actions'
import * as Reducer from '../store/reducer'


const TestHookReducer = () => {
  const [reducerState, dispatch] = useReducer(Reducer.Reducer1, Reducer.initialState)

  const dispatchActionSuccess = () => {
    dispatch(ACTIONS.SUCCESS)
  }

  const dispatchActionFailure = () => {
    dispatch(ACTIONS.FAILURE)
  }


  return (
    <div>
       <div>
        {reducerState.stateprop1
           ? <p>stateprop1 is true</p>
           : <p>stateprop1 is false</p>}
       </div>
       <button onClick={dispatchActionSuccess}>
         Dispatch Success
       </button>
    </div>
  )
}


export default TestHookReducer;

```

Il s'agit d'un composant simple qui changera `stateprop1` de false à true en dispatchant une action `SUCCESS`.

Et maintenant pour notre test.

```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import TestHookReducer from '../test_hook_reducer.js';
import {render, fireEvent, cleanup} from '@testing-library/react';
import * as Reducer from '../../store/reducer';
import * as ACTIONS from '../../store/actions';


afterEach(cleanup)

describe('test the reducer and actions', () => {
  it('should return the initial state', () => {
    expect(Reducer.initialState).toEqual({ stateprop1: false })
  })

  it('should change stateprop1 from false to true', () => {
    expect(Reducer.Reducer1(Reducer.initialState, ACTIONS.SUCCESS ))
      .toEqual({ stateprop1: true  })
  })
})

it('Reducer changes stateprop1 from false to true', () => {
   const { container, getByText } = render(<TestHookReducer />);

   expect(getByText(/stateprop1 is/i).textContent).toBe("stateprop1 is false")

   fireEvent.click(getByText("Dispatch Success"))

   expect(getByText(/stateprop1 is/i).textContent).toBe("stateprop1 is true")
})
```

Nous commençons d'abord par tester notre reducer. Et nous pouvons envelopper les tests pour le reducer dans le bloc `describe`. Ce sont des tests assez basiques que nous utilisons pour nous assurer que l'**état initial** est ce que nous voulons et que les actions produisent la sortie que nous voulons.

Vous pouvez argumenter que tester le reducer est tester les détails d'implémentation, mais j'ai trouvé en pratique que tester les actions et les reducers est un test unitaire qui est toujours nécessaire.

C'est un exemple simple, donc cela ne semble pas être un gros problème, mais dans des applications plus grandes et plus complexes, ne pas tester les reducers et les actions peut s'avérer désastreux. Donc, les actions et les reducers seraient une exception à la règle de tester les détails d'implémentation.

Ensuite, nous avons nos tests pour le composant réel. Remarquez encore une fois ici que nous ne testons pas les détails d'implémentation. Nous utilisons le même modèle que l'exemple précédent useState, nous obtenons nos nœuds DOM par le texte et trouvons et cliquons également sur le bouton avec le texte.

### useContext

Passons maintenant et testons si un composant enfant peut mettre à jour l'état du contexte dans un composant parent. Cela peut sembler complexe, mais c'est plutôt simple et direct.

Nous aurons d'abord besoin de notre objet de contexte que nous pouvons initialiser dans son propre fichier.

```javascript
import React from 'react';

const Context = React.createContext()

export default Context

```

Nous avons également besoin de notre composant d'application parent qui contiendra le fournisseur de contexte. La valeur transmise au `Provider` sera la valeur d'état et la fonction `setState` du composant `App.js`.

```javascript
import React, { useState } from 'react';
import TestHookContext from './components/react-testing-lib/test_hook_context';


import Context from './components/store/context';


const App = () => {
  const [state, setState] = useState("Some Text")
  

  const changeText = () => {
    setState("Some Other Text")
  }


  return (
    <div className="App">
    <h1> Basic Hook useContext</h1>
     <Context.Provider value={{changeTextProp: changeText,
                               stateProp: state
                                 }} >
        <TestHookContext />
     </Context.Provider>
    </div>
  );
}

export default App;
```

Et pour notre composant

```javascript
import React, { useContext } from 'react';

import Context from '../store/context';

const TestHookContext = () => {
  const context = useContext(Context)

  return (
    <div>
    <button onClick={context.changeTextProp}>
        Change Text
    </button>
      <p>{context.stateProp}</p>
    </div>
  )
}


export default TestHookContext;
```

Nous avons un composant simple qui affiche le texte que nous avons initialisé dans `App.js` et nous passons également la fonction `setState` à la méthode `onClick`.

**Note :** L'état est changé, initialisé et contenu dans notre composant `App.js`. Nous avons simplement transmis la valeur d'état et la fonction `setState` à notre composant enfant via le contexte, mais en fin de compte, l'état est géré dans le composant `App.js`. Cela sera important pour comprendre notre test.

Et notre test :

```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import TestHookContext from '../test_hook_context.js';
import {act, render, fireEvent, cleanup} from '@testing-library/react';
import App from '../../../App'

import Context from '../../store/context';

afterEach(cleanup)

it('Context value is updated by child component', () => {

   const { container, getByText } = render(<App>
                                            <Context.Provider>
                                             <TestHookContext />
                                            </Context.Provider>
                                           </App>);

   expect(getByText(/Some/i).textContent).toBe("Some Text")

   fireEvent.click(getByText("Change Text"))

   expect(getByText(/Some/i).textContent).toBe("Some Other Text")
})

```

Même pour le contexte, vous pouvez voir que nous ne brisons pas notre modèle de tests, nous trouvons et simulons toujours nos événements avec le texte.

J'ai inclus les composants `<Context.Provider/>` et `<TestHookContext />` dans la fonction render car cela rend le code plus facile à lire, mais nous n'en avons en fait besoin d'aucun des deux. Notre test fonctionnera toujours si nous avons passé uniquement le composant `<App />` à la fonction render.

```
const { container, getByText } = render(<App/>) 
```

Pourquoi est-ce le cas ?

Rappelons ce que nous savons sur le contexte. Tout l'état du contexte est géré dans `App.js`, pour cette raison, c'est le composant principal que nous testons réellement, même si cela semble comme si nous testions le composant enfant qui utilise le Hook **useContext**. Ce code fonctionne également grâce à **mount/render**. Comme nous le savons, dans le rendu shallow, les composants enfants ne sont **pas rendus**, mais dans mount/render, ils le sont. Puisque `<Context.Provider />` et `<TestHookContext />` sont tous deux des composants enfants de `<App />`, ils sont rendus automatiquement.



### Formulaires de composants contrôlés

Un formulaire de composant contrôlé signifie essentiellement que le formulaire fonctionnera via l'état React au lieu que le formulaire maintienne son propre état. Cela signifie que le gestionnaire `onChange` sauvegardera le texte d'entrée dans l'état React à chaque frappe.

Tester le formulaire sera un peu différent de ce que nous avons vu jusqu'à présent, mais nous essaierons de garder notre principe directeur à l'esprit.

```javascript
import React, { useState } from 'react';

const HooksForm1 = () => {
  const [valueChange, setValueChange] = useState('')
  const [valueSubmit, setValueSubmit] = useState('')

  const handleChange = (event) => (
    setValueChange(event.target.value)
  );

  const handleSubmit = (event) => {
    event.preventDefault();
    setValueSubmit(event.target.text1.value)
  };

    return (
      <div>
       <h1> React Hooks Form </h1>
        <form data-testid="form" onSubmit={handleSubmit}>
          <label htmlFor="text1">Input Text:</label>
          <input id="text1" onChange={handleChange} type="text" />
          <button type="submit">Submit</button>
        </form>
        <h3>React State:</h3>
          <p>Change: {valueChange}</p>
          <p>Submit Value: {valueSubmit}</p>
        <br />
      </div>
    )
}


export default HooksForm1;
```

Il s'agit d'un formulaire de base que nous avons ici et nous affichons également la valeur du changement et la valeur de soumission dans notre JSX. Nous avons l'attribut `data-testid="form"` que nous utiliserons dans notre test pour interroger le formulaire.

Et nos tests :

```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import HooksForm1 from '../test_hook_form.js';
import {render, fireEvent, cleanup} from '@testing-library/react';

afterEach(cleanup)

//testing a controlled component form.
it('Inputing text updates the state', () => {
    const { getByText, getByLabelText } = render(<HooksForm1 />);

    expect(getByText(/Change/i).textContent).toBe("Change: ")

    fireEvent.change(getByLabelText("Input Text:"), {target: {value: 'Text' } } )

    expect(getByText(/Change/i).textContent).not.toBe("Change: ")
 })


 it('submiting a form works correctly', () => {
     const { getByTestId, getByText } = render(<HooksForm1 />);

     expect(getByText(/Submit Value/i).textContent).toBe("Submit Value: ")

     fireEvent.submit(getByTestId("form"), {target: {text1: {value: 'Text' } } })

     expect(getByText(/Submit Value/i).textContent).not.toBe("Submit Value: ")
  })
```

Puisqu'un élément d'entrée vide n'a pas de texte, nous utiliserons une fonction `getByLabelText()` pour obtenir le nœud d'entrée. Cela respectera toujours notre principe directeur, puisque le texte de l'étiquette est ce que l'utilisateur lira avant de saisir du texte.

Remarquez que nous déclencherons l'événement `.change()` au lieu de l'événement `.click()` habituel. Nous passons également des données factices sous la forme :

`{ target: { value: "Text" } }`

Puisque la valeur du formulaire sera accessible sous la forme `event.target.value`, c'est ce que nous passons à l'événement simulé.

Puisque nous ne saurons généralement pas quel texte l'utilisateur soumettra, nous pouvons simplement utiliser un mot-clé `.not` pour nous assurer que le texte a changé dans notre méthode de rendu.

Nous pouvons tester la soumission du formulaire de manière similaire. La seule différence est que nous utilisons l'événement `.submit()` et passons des données factices de cette manière :

`{ target: { text1: { value: 'Text' } } }`

C'est ainsi que l'on accède aux données du formulaire à partir de l'événement synthétique lorsqu'un utilisateur soumet un formulaire, où `text1` est l'id de notre élément d'entrée. Nous devrons un peu briser notre modèle ici et utiliser l'attribut `data-testid="form"` pour interroger le formulaire, car il n'y a vraiment pas d'autre moyen d'obtenir le formulaire.

Et c'est tout pour le formulaire. Ce n'est pas si différent de nos autres exemples. Si vous pensez avoir compris, passons à quelque chose d'un peu plus complexe.

### 

### useEffect et requêtes API avec axios

Voyons maintenant comment nous testerions le **hook useEffect** et les requêtes API. Cela sera assez différent de ce que nous avons vu jusqu'à présent.

Supposons que nous avons une URL passée à un composant enfant depuis le parent racine.

```javascript

...

     <TestAxios url='https://jsonplaceholder.typicode.com/posts/1' />
     
 ... 
```

Et le composant lui-même.

```javascript
import React, { useState, useEffect } from 'react';
import axios from 'axios';


const TestAxios = (props) => {
  const [state, setState] = useState()

  useEffect(() => {
    axios.get(props.url)
      .then(res => setState(res.data))
  }, [])


  return (
    <div>
    <h1> Axios Test </h1>
        {state
          ? <p data-testid="title">{state.title}</p>
          : <p>...Loading</p>}
    </div>
  )
}


export default TestAxios;
```

Nous faisons simplement une requête API et sauvegardons les résultats dans l'état local. Nous utilisons également une expression ternaire dans notre méthode de rendu pour attendre que la requête soit terminée avant d'afficher les données de titre de json placeholder.

Vous remarquerez que nous devons à nouveau, par nécessité, utiliser l'attribut `data-testid`, et encore une fois, c'est un détail d'implémentation puisque l'utilisateur ne verra ni n'interagira avec cet attribut de quelque manière que ce soit, mais cela est plus réaliste, puisque nous ne connaîtrons généralement pas le texte d'une requête API à l'avance.

Nous utiliserons également des mocks dans ce test.

Un **mock** est un moyen de simuler un comportement que nous ne voulons pas réellement effectuer dans nos tests. Par exemple, nous mockons les requêtes API parce que nous ne voulons pas faire de vraies requêtes dans nos tests.

Nous ne voulons pas faire de vraies requêtes API dans nos tests pour diverses raisons : cela rendra nos tests beaucoup plus lents, pourrait nous donner un faux négatif, la requête API nous coûtera de l'argent, ou nous allons fausser notre base de données avec des données de test.

```
import React from 'react';
import ReactDOM from 'react-dom';
import TestAxios from '../test_axios.js';
import {act, render, fireEvent, cleanup, waitForElement} from '@testing-library/react';

import axiosMock from "axios";


```

Nous avons nos imports habituels, mais vous remarquerez quelque chose de particulier. Nous importons `axiosMock` de la bibliothèque `axios`. Nous n'importons pas un objet axios mock de la bibliothèque `axios`. Nous mockons en fait la bibliothèque `axios` elle-même.

Comment ?

En utilisant la fonctionnalité de mocking offerte par Jest.

Nous allons d'abord créer un dossier `__mocks__` adjacent à notre dossier de test, quelque chose comme ceci.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-13.png)



Et à l'intérieur du dossier mocks, nous avons un fichier `axios.js` et c'est notre fausse bibliothèque **axios**. Et à l'intérieur de notre fausse bibliothèque **axios**, nous avons notre **fonction mock Jest**.

Les fonctions mock permettent d'utiliser des fonctions dans notre environnement Jest sans avoir à implémenter la logique réelle de la fonction.

Donc, en gros, nous n'allons pas implémenter la logique réelle derrière une requête get axios. Nous utiliserons simplement cette fonction mock à la place.

```javascript
export default {
  get: jest.fn(() => Promise.resolve({ data: {} }) )
};

```

Ici, nous avons notre fausse fonction get. C'est une fonction simple qui est en fait un objet JS. `get` est notre clé et la valeur est la **fonction mock**. Comme une requête API **axios**, nous résolvons une promesse. Nous ne passerons aucune donnée ici, nous le ferons dans notre configuration de test.

Maintenant, notre configuration de test

```javascript
//imports
...

afterEach(cleanup)

it('Async axios request works', async () => {
  axiosMock.get.mockResolvedValue({data: { title: 'some title' } })

  const url = 'https://jsonplaceholder.typicode.com/posts/1'
  const { getByText, getByTestId, rerender } = render(<TestAxios url={url} />);

  expect(getByText(/...Loading/i).textContent).toBe("...Loading")

  const resolvedEl = await waitForElement(() => getByTestId("title"));

  expect((resolvedEl).textContent).toBe("some title")

  expect(axiosMock.get).toHaveBeenCalledTimes(1);
  expect(axiosMock.get).toHaveBeenCalledWith(url);
 })
```

La première chose que nous faisons dans notre test est d'appeler notre fausse **requête get axios**, et de mock la valeur résolue avec, ironiquement, la fonction `mockResolvedValue` offerte par Jest. Cette fonction fait exactement ce que son nom indique, elle résout une promesse avec les données que nous passons, ce qui simule ce que fait axios.

Cette fonction doit être appelée avant notre fonction `render()` sinon le test ne fonctionnera pas. Parce que rappelez-vous, nous mockons la **bibliothèque axios** elle-même. Lorsque notre composant exécute la commande `import axios from 'axios';`, il **importera notre fausse bibliothèque axios** au lieu de la vraie et cette fausse axios sera substituée dans notre composant partout où nous avons utilisé axios.

Ensuite, nous obtenons notre nœud de texte "...Loading" puisque c'est ce qui sera affiché avant que la promesse ne soit résolue. Après cela, nous avons une fonction que nous n'avons pas encore vue, la fonction `waitForElement()`, qui attendra que la promesse soit résolue avant de passer à l'assertion suivante.

Remarquez également les mots-clés **await** et **async**, ceux-ci sont utilisés de la même manière que dans un environnement non test.

Une fois résolu, le nœud DOM aura le texte "some title" qui est la donnée que nous avons passée à notre fausse bibliothèque axios mock.

Ensuite, nous nous assurons que la requête n'a été appelée qu'une seule fois et avec la bonne URL. Même si nous testons l'URL, nous n'avons pas fait de requête API avec cette URL.

Et c'est tout pour les requêtes API avec axios. Dans la section suivante, nous examinerons les tests de bout en bout avec Cypress.

## Cypress

Passons maintenant à Cypress, que je considère comme le meilleur framework pour exécuter des tests de bout en bout. Nous ne sommes plus dans le monde de Jest, nous allons maintenant travailler uniquement avec Cypress qui a son propre environnement et syntaxe de test.

Cypress est assez incroyable et puissant. Tellement incroyable et puissant en fait que nous pouvons exécuter tous les tests que nous venons de passer en revue dans un seul bloc de test et regarder Cypress exécuter ces tests en temps réel dans un navigateur simulé.

Assez cool, hein ?

Je pense que oui. En tout cas, avant de pouvoir faire cela, nous devons configurer Cypress. Étonnamment, Cypress peut être installé comme un module npm régulier.

`npm install cypress`

Pour exécuter Cypress, vous devrez utiliser cette commande.

`node_modules/.bin/cypress open`

Si cela semble fastidieux à écrire chaque fois que vous voulez ouvrir Cypress, vous pouvez l'ajouter à votre package.json.

```javascript
...

  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject",
    "cypress": "node_modules/.bin/cypress open", 
    
   ...
```

Cela vous permettra d'ouvrir Cypress avec la commande `npm run cypress`.

L'ouverture de Cypress vous donnera une interface graphique qui ressemble à ceci.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-14.png)

Pour exécuter réellement les tests Cypress, votre application devra être en cours d'exécution en même temps, ce que nous verrons dans un instant.

L'exécution de la commande `cypress open` vous donnera une configuration de base de Cypress et créera certains fichiers et dossiers pour vous automatiquement. Un dossier Cypress sera créé à la racine du projet. Nous écrirons notre code dans le dossier d'intégration.

Nous pouvons commencer par supprimer le dossier des exemples. Contrairement à Jest, les fichiers Cypress prennent une extension `.spec.js`. Puisque ceci est un test de bout en bout, nous l'exécuterons sur notre fichier principal `App.js`. Vous devriez donc avoir une structure de répertoire qui ressemble maintenant à ceci.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-21.png)



Nous pouvons également définir une URL de base dans le fichier cypress.json. Comme ceci :

`{ "baseUrl": "[http://localhost:3000](http://localhost:3000)" }`

Maintenant pour notre grand test monolithique

```javascript
import React from 'react';

describe ('complete e to e test', () => {
  it('e to e test', () => {
    cy.visit('/')
    //counter test
    cy.contains("Clicked: 0")
      .click()
    cy.contains("Clicked: 1")
    // basic hooks test
    cy.contains("Initial State")
    cy.contains("State Change Button")
      .click()
    cy.contains("Initial State Changed")
    cy.contains("Moe")
    cy.contains("Change Name")
      .click()
    cy.contains("Steve")
    //useReducer test
    cy.contains('stateprop1 is false')
    cy.contains('Dispatch Success')
      .click()
    cy.contains('stateprop1 is true')
    //useContext test
    cy.contains("Some Text")
    cy.contains('Change Text')
      .click()
    cy.contains("Some Other Text")
    //form test
    cy.get('#text1')
      .type('New Text {enter}')
    cy.contains("Change: New Text")
    cy.contains("Submit Value: New Text")
    //axios test
    cy.request('https://jsonplaceholder.typicode.com/posts/1')
      .should(res => {
          expect(res.body).not.to.be.null
          cy.contains(res.body.title)
        })
  });
});
```

Comme mentionné, nous exécutons chaque test que nous venons de passer en revue dans un seul bloc de test. J'ai séparé chaque section avec un commentaire pour que ce soit plus facile à voir.

Notre test peut sembler intimidant au premier abord, mais la plupart des tests individuels suivront un modèle basique d'arrangement-action-assertion.

```javascript

cy.contains(Some innerHTML text of DOM node)

cy.contains (text of button)
.click()

cy.contains(Updated innerHTML text of DOM node)

```

Puisque ceci est un test de bout en bout, vous ne trouverez aucun mocking. Notre application fonctionnera dans sa version de développement complète dans un navigateur simulé avec une UI. Cela sera aussi proche que possible de tester notre application de manière réaliste.

Contrairement aux tests unitaires et d'intégration, nous n'avons pas besoin d'assertions explicites pour certaines choses. Cela est dû au fait que certaines commandes Cypress ont des assertions par défaut intégrées. Les **assertions par défaut** sont exactement ce à quoi elles ressemblent, elles sont assertées par défaut, donc pas besoin d'ajouter un matcher.

[Cypress default assertions](https://docs.cypress.io/guides/core-concepts/introduction-to-cypress.html#Default-Assertions)

Les commandes sont enchaînées, donc l'ordre est important et une commande attendra qu'une commande précédente soit terminée avant de s'exécuter.

Même lors des tests avec Cypress, nous respecterons notre philosophie de ne pas tester les détails d'implémentation. En pratique, cela signifiera que nous n'utiliserons pas les classes, identifiants ou propriétés HTML/CSS comme sélecteurs si nous pouvons l'éviter. La seule fois où nous devrons utiliser un identifiant est pour obtenir notre élément de saisie de formulaire.

Nous utiliserons la commande `cy.contains()` qui retournera un nœud DOM avec le texte correspondant. Voir et interagir avec le texte sur l'UI est ce que notre utilisateur final fera, donc tester de cette manière sera en accord avec notre principe directeur.

Puisque nous ne faisons pas de stubbing ou de mocking, vous remarquerez que nos tests sembleront très simplistes. C'est bien puisque c'est une application en cours d'exécution, nos tests n'auront aucune valeur artificielle.

Dans notre test axios, nous ferons une vraie requête http à notre endpoint. Faire une vraie requête http dans un test de bout en bout est courant. Ensuite, nous vérifierons si cette valeur n'est pas nulle. Puis nous nous assurerons que les données de la réponse apparaissent dans notre UI.

Si cela est fait correctement, vous devriez voir que Cypress a exécuté avec succès les tests dans Chromium.


![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-22.png)



## Intégration Continue

Suivre et exécuter tous ces tests manuellement peut devenir fastidieux. Nous avons donc l'Intégration Continue, un moyen d'exécuter automatiquement nos tests en continu.

### Travis CI

Pour garder les choses simples, nous utiliserons simplement Travis CI pour notre Intégration Continue. Vous devez savoir qu'il existe des configurations CI beaucoup plus complexes utilisant Docker et Jenkins.

Vous devrez vous inscrire à un compte Travis et Github, tous deux sont heureusement gratuits.

Je suggérerais d'utiliser simplement l'option "S'inscrire avec Github" sur Travis CI.

Une fois là-bas, vous pouvez simplement cliquer sur l'icône de votre profil et cliquer sur le bouton curseur à côté du dépôt pour lequel vous voulez CI.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-15.png)

Pour que Travis CI sache quoi faire, nous devrons configurer un fichier .travis.yml à la racine de notre projet.

```yaml
language: node_js

node_js: 
  - stable
  
  
install:
  - npm install

script:
  - npm run test
  - npm run coveralls
```

Cela indique essentiellement à Travis que nous utilisons node_js, téléchargez la version stable, installez les dépendances et exécutez les commandes npm run test et npm run coveralls.

Et c'est tout. Vous pouvez maintenant aller sur le tableau de bord et démarrer la construction. Travis exécutera les tests automatiquement et vous donnera une sortie comme ceci. Si vos tests passent, vous êtes prêt à partir. S'ils échouent, votre construction échouera et vous devrez corriger votre code et redémarrer la construction.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-16.png)



### Coveralls

Coveralls nous donne un rapport de couverture qui nous indique essentiellement combien de notre code est testé.

Vous devrez vous inscrire à Coveralls et synchroniser avec votre compte Github. Similaire à Travis CI, allez simplement dans l'onglet add repos et activez le dépôt que vous avez également activé sur Travis CI.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-17.png)

Ensuite, allez dans votre fichier package.json et ajoutez cette ligne de code

```
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test --coverage",
    "eject": "react-scripts eject",
    "cypress": "node_modules/.bin/cypress open", 
    "coveralls": "cat ./coverage/lcov.info | node node_modules/.bin/coveralls"
  },
```

Assurez-vous d'ajouter le flag `--coverage` à la commande `react-scripts test`. C'est ce qui générera les données de couverture que Coveralls utilisera pour générer un rapport de couverture.

Et vous pouvez en fait voir ces données de couverture sur la console Travis CI après que vos tests ont été exécutés.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-18.png)

Puisque nous ne traitons pas avec un dépôt privé ou Travis CI pro, nous n'avons pas besoin de nous soucier des jetons de dépôt.

Une fois que vous avez terminé, vous pouvez ajouter un badge à votre README de dépôt en copiant le lien fourni sur le tableau de bord.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-19.png)



Il ressemblera à ceci.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-20.png)





## Conclusion

Considérez-vous parmi les 20 % de développeurs en termes de compétences en test React si vous avez réussi à suivre l'ensemble du tutoriel.

Merci d'avoir lu. Santé.

> Vous pouvez me suivre sur Twitter pour plus de tutoriels à l'avenir : [https://twitter.com/iqbal125sf?lang=en](https://twitter.com/iqbal125sf?lang=en)



### Lectures complémentaires


**Articles de blog :**

[https://djangostars.com/blog/what-and-how-to-test-with-enzyme-and-jest-full-instruction-on-react-component-testing/](https://djangostars.com/blog/what-and-how-to-test-with-enzyme-and-jest-full-instruction-on-react-component-testing/#utm_source=medium&utm_medium=blog.bitsrc.io&utm_campaign=react%20components%20testing&utm_content=continue%20reading%20the%20original%20article%20on%20our%C2%A0blog)

[https://engineering.ezcater.com/the-case-against-react-snapshot-testing](https://engineering.ezcater.com/the-case-against-react-snapshot-testing)

[https://medium.com/@tomgold_48918/why-i-stopped-using-snapshot-testing-with-jest-3279fe41ffb2](https://medium.com/@tomgold_48918/why-i-stopped-using-snapshot-testing-with-jest-3279fe41ffb2)

[https://circleci.com/blog/continuously-testing-react-applications-with-jest-and-enzyme/](https://circleci.com/blog/continuously-testing-react-applications-with-jest-and-enzyme/)

[https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html](https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html)

[https://willowtreeapps.com/ideas/best-practices-for-unit-testing-with-a-react-redux-approach](https://willowtreeapps.com/ideas/best-practices-for-unit-testing-with-a-react-redux-approach)

[https://blog.pragmatists.com/genuine-guide-to-testing-react-redux-applications-6f3265c11f63](https://blog.pragmatists.com/genuine-guide-to-testing-react-redux-applications-6f3265c11f63)

[https://hacks.mozilla.org/2018/04/testing-strategies-for-react-and-redux/](https://hacks.mozilla.org/2018/04/testing-strategies-for-react-and-redux/)

[https://codeburst.io/deliberate-practice-what-i-learned-from-reading-redux-mock-store-8d2d79a4b24d](https://codeburst.io/deliberate-practice-what-i-learned-from-reading-redux-mock-store-8d2d79a4b24d)

[https://www.robinwieruch.de/react-testing-tutorial/](https://www.robinwieruch.de/react-testing-tutorial/)

[https://medium.com/@ryandrewjohnson/unit-testing-components-using-reacts-new-context-api-4a5219f4b3fe](https://medium.com/@ryandrewjohnson/unit-testing-components-using-reacts-new-context-api-4a5219f4b3fe)



**Articles de Kent C Dodds sur les tests**

[https://kentcdodds.com/blog/introducing-the-react-testing-library](https://kentcdodds.com/blog/introducing-the-react-testing-library)

[https://kentcdodds.com/blog/unit-vs-integration-vs-e2e-tests](https://kentcdodds.com/blog/unit-vs-integration-vs-e2e-tests)

[https://kentcdodds.com/blog/why-i-never-use-shallow-rendering](https://kentcdodds.com/blog/why-i-never-use-shallow-rendering)

[https://kentcdodds.com/blog/demystifying-testing](https://kentcdodds.com/blog/demystifying-testing)

[https://kentcdodds.com/blog/effective-snapshot-testing](https://kentcdodds.com/blog/effective-snapshot-testing)

[https://kentcdodds.com/blog/testing-implementation-details](https://kentcdodds.com/blog/testing-implementation-details)

[https://kentcdodds.com/blog/common-testing-mistakes](https://kentcdodds.com/blog/common-testing-mistakes)

[https://kentcdodds.com/blog/ui-testing-myths](https://kentcdodds.com/blog/ui-testing-myths)

[https://kentcdodds.com/blog/why-youve-been-bad-about-testing](https://kentcdodds.com/blog/why-youve-been-bad-about-testing)

[https://kentcdodds.com/blog/the-merits-of-mocking](https://kentcdodds.com/blog/the-merits-of-mocking)

[https://kentcdodds.com/blog/how-to-know-what-to-test](https://kentcdodds.com/blog/how-to-know-what-to-test)

[https://kentcdodds.com/blog/avoid-the-test-user](https://kentcdodds.com/blog/avoid-the-test-user)


**Cheat Sheets / fils github**

[https://devhints.io/enzyme](https://devhints.io/enzyme)

[https://devhints.io](https://devhints.io/enzyme)/jest

[https://github.com/ReactTraining/react-router/tree/master/packages/react-router/modules/__tests__](https://github.com/ReactTraining/react-router/tree/master/packages/react-router/modules/__tests__)

[https://github.com/airbnb/enzyme/issues/1938](https://github.com/airbnb/enzyme/issues/1938)

[https://gist.github.com/fokusferit/e4558d384e4e9cab95d04e5f35d4f913](https://gist.github.com/fokusferit/e4558d384e4e9cab95d04e5f35d4f913)

[https://airbnb.io/enzyme/docs/api/selector.html](https://airbnb.io/enzyme/docs/api/selector.html)


**Docs**

[https://docs.cypress.io](https://docs.cypress.io/)

[https://airbnb.io/enzyme/](https://airbnb.io/enzyme/)

[https://github.com/dmitry-zaets/redux-mock-store](https://github.com/dmitry-zaets/redux-mock-store)

[https://jestjs.io/docs/en](https://jestjs.io/docs/en)

[https://testing-library.com/docs/learning](https://testing-library.com/docs/learning)

[https://sinonjs.org/releases/v7.3.2/](https://sinonjs.org/releases/v7.3.2/)

[https://redux.js.org/recipes/writing-tests](https://redux.js.org/recipes/writing-tests)

[https://jestjs.io/docs/en/using-matchers](https://jestjs.io/docs/en/using-matchers)

[https://jestjs.io/docs/en/api](https://jestjs.io/docs/en/api)